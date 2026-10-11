"""Reproducible train/validation/test splitting strategies.

All functions return integer index arrays over the input frame and write a
JSON manifest (`save_split`) so that every experiment can reload the exact
same partition.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Optional

import numpy as np
import pandas as pd
from sklearn.model_selection import (GroupShuffleSplit, StratifiedGroupKFold,
                                     train_test_split)


def random_stratified_split(df: pd.DataFrame, test_size=0.2, val_size=0.2, seed=42) -> Dict[str, np.ndarray]:
    idx = np.arange(len(df))
    y = df["label"].values
    trval, te = train_test_split(idx, test_size=test_size, stratify=y, random_state=seed)
    rel = val_size / (1 - test_size)
    tr, va = train_test_split(trval, test_size=rel, stratify=y[trval], random_state=seed)
    return {"train": np.sort(tr), "val": np.sort(va), "test": np.sort(te)}


def grouped_stratified_split(df: pd.DataFrame, group_col="group", test_size=0.2, val_size=0.2,
                             seed=42, n_folds=10) -> Dict[str, np.ndarray]:
    """Registered-domain-grouped split with approximate stratification.

    Uses StratifiedGroupKFold with `n_folds` folds; the first
    round(test_size*n_folds) folds become test, the next round(val_size*n_folds)
    validation. No registered domain appears in more than one partition.
    """
    y = df["label"].values
    groups = df[group_col].values
    sgkf = StratifiedGroupKFold(n_splits=n_folds, shuffle=True, random_state=seed)
    fold_of = np.empty(len(df), dtype=int)
    for k, (_, te_idx) in enumerate(sgkf.split(np.zeros(len(df)), y, groups)):
        fold_of[te_idx] = k
    n_test = int(round(test_size * n_folds))
    n_val = int(round(val_size * n_folds))
    test_folds = set(range(0, n_test))
    val_folds = set(range(n_test, n_test + n_val))
    te = np.where(np.isin(fold_of, list(test_folds)))[0]
    va = np.where(np.isin(fold_of, list(val_folds)))[0]
    tr = np.where(~np.isin(fold_of, list(test_folds | val_folds)))[0]
    return {"train": tr, "val": va, "test": te}


def temporal_split(df: pd.DataFrame, ts_col="timestamp", test_size=0.2, val_size=0.2) -> Dict[str, np.ndarray]:
    """Chronological split: oldest -> train, middle -> val, newest -> test."""
    if df[ts_col].isna().any():
        raise ValueError("temporal_split requires timestamps on every row")
    order = np.argsort(df[ts_col].values, kind="stable")
    n = len(df)
    n_te = int(round(n * test_size))
    n_va = int(round(n * val_size))
    te = order[n - n_te:]
    va = order[n - n_te - n_va:n - n_te]
    tr = order[: n - n_te - n_va]
    return {"train": np.sort(tr), "val": np.sort(va), "test": np.sort(te)}


def overlap_report(df: pd.DataFrame, split: Dict[str, np.ndarray], group_col="group") -> Dict:
    """Quantify registered-domain overlap between partitions."""
    g = {k: set(df.iloc[v][group_col]) for k, v in split.items()}
    test_rows = df.iloc[split["test"]]
    train_groups = g["train"]
    seen = test_rows[group_col].isin(train_groups)
    out = {
        "n_train_groups": len(g["train"]),
        "n_test_groups": len(g["test"]),
        "test_groups_also_in_train": len(g["test"] & g["train"]),
        "share_test_rows_with_group_in_train": float(seen.mean()) if len(test_rows) else 0.0,
        "share_test_pos_rows_with_group_in_train": float(seen[test_rows["label"] == 1].mean()) if (test_rows["label"] == 1).any() else 0.0,
        "share_test_neg_rows_with_group_in_train": float(seen[test_rows["label"] == 0].mean()) if (test_rows["label"] == 0).any() else 0.0,
    }
    if "val" in split:
        out["val_groups_also_in_train"] = len(g["val"] & g["train"])
    return out


def split_summary(df: pd.DataFrame, split: Dict[str, np.ndarray]) -> Dict:
    s = {}
    for k, v in split.items():
        y = df.iloc[v]["label"]
        s[k] = {"n": int(len(v)), "pos": int(y.sum()), "neg": int((y == 0).sum()),
                "pos_rate": float(y.mean()) if len(v) else 0.0}
    return s


def save_split(split: Dict[str, np.ndarray], path: Path, meta: Optional[Dict] = None) -> None:
    payload = {"meta": meta or {}, **{k: v.tolist() for k, v in split.items()}}
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(payload))


def load_split(path: Path) -> Dict[str, np.ndarray]:
    payload = json.loads(Path(path).read_text())
    return {k: np.asarray(v, dtype=int) for k, v in payload.items() if k != "meta"}
