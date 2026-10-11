"""Character-level CNN for URL classification (CPU-friendly).

Architecture (eXpose/URLNet-style, deliberately small):
    char embedding (vocab 128, dim 32)
    -> parallel 1-D convolutions with kernel sizes {3,5,7} (128 filters each)
    -> global max pooling -> concat -> dropout -> dense(128) -> sigmoid

An optional `hybrid` mode concatenates standardised lexical features to the
pooled convolutional representation before the dense head.
"""
from __future__ import annotations

import math
import time
from dataclasses import dataclass, field
from typing import Dict, List, Optional

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

PAD = 0
UNK = 1
MAX_LEN = 200


def url_to_ids(url: str, max_len: int = MAX_LEN) -> np.ndarray:
    ids = np.full(max_len, PAD, dtype=np.int64)
    s = str(url)[:max_len]
    for i, ch in enumerate(s):
        o = ord(ch)
        ids[i] = o if 2 <= o < 128 else UNK
    return ids


def encode_urls(urls, max_len: int = MAX_LEN) -> np.ndarray:
    return np.stack([url_to_ids(u, max_len) for u in urls])


class CharCNN(nn.Module):
    def __init__(self, vocab=128, emb=32, filters=128, kernels=(3, 5, 7), dense=128,
                 dropout=0.3, n_lexical=0):
        super().__init__()
        self.emb = nn.Embedding(vocab, emb, padding_idx=PAD)
        self.convs = nn.ModuleList([nn.Conv1d(emb, filters, k, padding=k // 2) for k in kernels])
        self.n_lexical = n_lexical
        in_dim = filters * len(kernels) + n_lexical
        self.fc1 = nn.Linear(in_dim, dense)
        self.drop = nn.Dropout(dropout)
        self.out = nn.Linear(dense, 1)

    def forward(self, x, lex=None):
        e = self.emb(x).transpose(1, 2)           # B, emb, L
        pooled = [F.relu(c(e)).max(dim=2).values for c in self.convs]
        h = torch.cat(pooled, dim=1)
        if self.n_lexical:
            h = torch.cat([h, lex], dim=1)
        h = self.drop(F.relu(self.fc1(self.drop(h))))
        return self.out(h).squeeze(1)


@dataclass
class CharCNNConfig:
    max_len: int = MAX_LEN
    emb: int = 32
    filters: int = 128
    kernels: tuple = (3, 5, 7)
    dense: int = 128
    dropout: float = 0.3
    epochs: int = 8
    batch_size: int = 256
    lr: float = 1e-3
    patience: int = 2
    seed: int = 42
    threads: int = 8
    max_train_minutes: float = 60.0


class CharCNNClassifier:
    """sklearn-like wrapper: fit(urls, y, val_urls, val_y) / predict_proba(urls)."""

    def __init__(self, config: Optional[CharCNNConfig] = None, lexical_dim: int = 0):
        self.cfg = config or CharCNNConfig()
        self.lexical_dim = lexical_dim
        self.model: Optional[CharCNN] = None
        self.history: List[Dict] = []
        self.lex_mean = None
        self.lex_std = None

    def _lex(self, lex):
        if lex is None or self.lexical_dim == 0:
            return None
        arr = np.asarray(lex, dtype=np.float32)
        return torch.from_numpy((arr - self.lex_mean) / self.lex_std)

    def fit(self, urls, y, val_urls=None, val_y=None, lex=None, val_lex=None):
        torch.manual_seed(self.cfg.seed); np.random.seed(self.cfg.seed)
        torch.set_num_threads(self.cfg.threads)
        if self.lexical_dim:
            arr = np.asarray(lex, dtype=np.float32)
            self.lex_mean = arr.mean(0); self.lex_std = arr.std(0) + 1e-6
        X = torch.from_numpy(encode_urls(urls, self.cfg.max_len))
        Y = torch.from_numpy(np.asarray(y, dtype=np.float32))
        L = self._lex(lex)
        self.model = CharCNN(emb=self.cfg.emb, filters=self.cfg.filters, kernels=self.cfg.kernels,
                             dense=self.cfg.dense, dropout=self.cfg.dropout, n_lexical=self.lexical_dim)
        opt = torch.optim.Adam(self.model.parameters(), lr=self.cfg.lr)
        pos_w = torch.tensor([(Y == 0).sum() / max((Y == 1).sum(), 1)])
        lossf = nn.BCEWithLogitsLoss(pos_weight=pos_w)
        n = len(X)
        best, best_state, bad = -math.inf, None, 0
        t0 = time.time()
        g = torch.Generator().manual_seed(self.cfg.seed)
        for ep in range(self.cfg.epochs):
            self.model.train()
            perm = torch.randperm(n, generator=g)
            tot = 0.0
            for i in range(0, n, self.cfg.batch_size):
                b = perm[i:i + self.cfg.batch_size]
                opt.zero_grad()
                logit = self.model(X[b], L[b] if L is not None else None)
                loss = lossf(logit, Y[b])
                loss.backward(); opt.step()
                tot += loss.item() * len(b)
            rec = {"epoch": ep + 1, "train_loss": tot / n, "seconds": time.time() - t0}
            if val_urls is not None:
                from sklearn.metrics import roc_auc_score
                pv = self.predict_proba(val_urls, val_lex)[:, 1]
                rec["val_auc"] = float(roc_auc_score(val_y, pv))
                score = rec["val_auc"]
            else:
                score = -rec["train_loss"]
            self.history.append(rec)
            if score > best + 1e-5:
                best, bad = score, 0
                best_state = {k: v.detach().clone() for k, v in self.model.state_dict().items()}
            else:
                bad += 1
                if bad >= self.cfg.patience:
                    break
            if (time.time() - t0) / 60 > self.cfg.max_train_minutes:
                break
        if best_state is not None:
            self.model.load_state_dict(best_state)
        self.model.eval()
        return self

    @torch.no_grad()
    def predict_proba(self, urls, lex=None, batch_size: int = 1024) -> np.ndarray:
        self.model.eval()
        X = torch.from_numpy(encode_urls(urls, self.cfg.max_len))
        L = self._lex(lex)
        out = []
        for i in range(0, len(X), batch_size):
            logit = self.model(X[i:i + batch_size], L[i:i + batch_size] if L is not None else None)
            out.append(torch.sigmoid(logit).numpy())
        p = np.concatenate(out) if out else np.zeros(0)
        return np.stack([1 - p, p], axis=1)

    def n_parameters(self) -> int:
        return sum(p.numel() for p in self.model.parameters())

    def save(self, path):
        torch.save({"cfg": self.cfg.__dict__, "lexical_dim": self.lexical_dim,
                    "state": self.model.state_dict(), "lex_mean": self.lex_mean, "lex_std": self.lex_std}, path)
