"""Config-driven experiment runner.

A run = (dataset, feature set, split strategy, model list, seeds). It writes:
    results/runs/<run_id>/config.json, environment.json
    results/runs/<run_id>/split_<seed>.json
    results/runs/<run_id>/predictions_<model>_<seed>.csv  (idx, y, prob, split)
    results/runs/<run_id>/metrics.csv  (one row per model x seed x split x threshold policy)
    results/runs/<run_id>/resources.csv (fit time, predict latency, model size)
Thresholds are chosen on the validation split only.
"""
from __future__ import annotations

import io
import json
import logging
import os
import pickle
import platform
import sys
import time
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np
import pandas as pd
import yaml

from ..data.splits import (grouped_stratified_split, overlap_report, random_stratified_split,
                           save_split, split_summary, temporal_split)
from ..evaluation.metrics import classification_metrics, threshold_at_fpr, threshold_max_f1
from ..features.lexical import FEATURE_SETS, feature_frame
from ..models.tabular import MODEL_FACTORIES

log = logging.getLogger("urlresearch.runner")
REPO = Path(__file__).resolve().parents[3]


@dataclass
class RunConfig:
    run_id: str
    dataset: str                     # name of a canonical parquet in data/processed/canonical/
    feature_set: str = "lexical_v2"  # baseline28 | lexical_v2 | none (char models)
    drop_artifacts: bool = False
    split: str = "random"            # random | grouped | temporal
    models: List[str] = field(default_factory=lambda: ["lr", "rf", "xgb", "softvote"])
    seeds: List[int] = field(default_factory=lambda: [42])
    test_size: float = 0.2
    val_size: float = 0.2
    fpr_targets: List[float] = field(default_factory=lambda: [0.01, 0.001])
    max_rows: Optional[int] = None   # subsample for smoke tests
    external_tests: List[str] = field(default_factory=list)  # other canonical datasets to score
    charcnn: Dict = field(default_factory=dict)
    model_params: Dict = field(default_factory=dict)
    notes: str = ""

    @staticmethod
    def from_yaml(path) -> "RunConfig":
        d = yaml.safe_load(Path(path).read_text())
        return RunConfig(**d)


def environment_info() -> Dict:
    import sklearn, xgboost, torch
    return {"python": sys.version, "platform": platform.platform(), "cpu_count": os.cpu_count(),
            "sklearn": sklearn.__version__, "xgboost": xgboost.__version__, "torch": torch.__version__,
            "numpy": np.__version__, "pandas": pd.__version__}


def load_canonical(name: str, max_rows: Optional[int] = None, seed: int = 0) -> pd.DataFrame:
    base = Path(os.environ.get("URLRESEARCH_CANONICAL", REPO / "data" / "processed" / "canonical"))
    p = base / f"{name}.parquet"
    df = pd.read_parquet(p)
    if max_rows and len(df) > max_rows:
        df = df.sample(max_rows, random_state=seed).reset_index(drop=True)
    return df


def make_split(df: pd.DataFrame, cfg: RunConfig, seed: int) -> Dict[str, np.ndarray]:
    if cfg.split == "random":
        return random_stratified_split(df, cfg.test_size, cfg.val_size, seed)
    if cfg.split == "grouped":
        return grouped_stratified_split(df, "group", cfg.test_size, cfg.val_size, seed)
    if cfg.split == "temporal":
        return temporal_split(df, "timestamp", cfg.test_size, cfg.val_size)
    raise ValueError(cfg.split)


def pickled_size(obj) -> int:
    buf = io.BytesIO(); pickle.dump(obj, buf); return buf.tell()


def _features(df: pd.DataFrame, cfg: RunConfig, cache_dir: Path) -> Optional[pd.DataFrame]:
    if cfg.feature_set == "none":
        return None
    cache = cache_dir / f"features_{cfg.dataset}_{cfg.feature_set}_{len(df)}.parquet"
    if cache.exists():
        X = pd.read_parquet(cache)
    else:
        t0 = time.time()
        X = feature_frame(df["url"].tolist(), cfg.feature_set)
        log.info("feature extraction %s: %.1fs for %d urls", cfg.feature_set, time.time() - t0, len(df))
        cache_dir.mkdir(parents=True, exist_ok=True)
        X.to_parquet(cache)
    if cfg.drop_artifacts:
        X = X.drop(columns=[c for c in FEATURE_SETS[cfg.feature_set]["artifact"] if c in X.columns])
    return X


def run(cfg: RunConfig, out_root: Optional[Path] = None) -> pd.DataFrame:
    out = (out_root or REPO / "results" / "runs") / cfg.run_id
    out.mkdir(parents=True, exist_ok=True)
    (out / "config.json").write_text(json.dumps(asdict(cfg), indent=2))
    (out / "environment.json").write_text(json.dumps(environment_info(), indent=2))
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s",
                        handlers=[logging.FileHandler(out / "run.log", encoding="utf-8"), logging.StreamHandler()])
    df = load_canonical(cfg.dataset, cfg.max_rows)
    cache_dir = REPO / "data" / "processed" / "feature_cache"
    X = _features(df, cfg, cache_dir)
    ext_sets = {}
    for name in cfg.external_tests:
        edf = load_canonical(name)
        ext_cfg = RunConfig(**{**asdict(cfg), "dataset": name})
        ext_sets[name] = (edf, _features(edf, ext_cfg, cache_dir))
    spec = FEATURE_SETS.get(cfg.feature_set, {"categorical": []})
    categorical = [c for c in spec.get("categorical", []) if X is not None and c in X.columns]
    numeric = [c for c in X.columns if c not in categorical] if X is not None else []

    metric_rows, resource_rows = [], []
    for seed in cfg.seeds:
        split = make_split(df, cfg, seed)
        save_split(split, out / f"split_{seed}.json",
                   meta={"strategy": cfg.split, "seed": seed, "summary": split_summary(df, split),
                         "overlap": overlap_report(df, split)})
        tr, va, te = split["train"], split["val"], split["test"]
        y = df["label"].values
        for mname in cfg.models:
            t0 = time.time()
            if mname == "charcnn" or mname == "charcnn_hybrid":
                from ..models.charcnn import CharCNNClassifier, CharCNNConfig
                ccfg = CharCNNConfig(seed=seed, **cfg.charcnn)
                use_lex = mname == "charcnn_hybrid"
                lex = X[numeric].values.astype(np.float32) if use_lex else None
                clf = CharCNNClassifier(ccfg, lexical_dim=len(numeric) if use_lex else 0)
                urls = df["url"].values
                clf.fit(urls[tr], y[tr], urls[va], y[va],
                        lex=lex[tr] if use_lex else None, val_lex=lex[va] if use_lex else None)
                fit_s = time.time() - t0
                def predict(idx_urls, idx_lex=None):
                    return clf.predict_proba(idx_urls, idx_lex)[:, 1]
                t1 = time.time(); p_te = predict(urls[te], lex[te] if use_lex else None); lat = (time.time() - t1) / len(te)
                p_va = predict(urls[va], lex[va] if use_lex else None)
                p_tr = predict(urls[tr], lex[tr] if use_lex else None)
                size = sum(p.numel() * 4 for p in clf.model.parameters())
                ext_probs = {n: predict(e[0]["url"].values, e[1][numeric].values.astype(np.float32) if use_lex else None)
                             for n, e in ext_sets.items()}
                (out / f"history_{mname}_{seed}.json").write_text(json.dumps(clf.history))
            else:
                params = cfg.model_params.get(mname, {})
                clf = MODEL_FACTORIES[mname](numeric, categorical, seed=seed, **params)
                clf.fit(X.iloc[tr], y[tr])
                fit_s = time.time() - t0
                t1 = time.time(); p_te = clf.predict_proba(X.iloc[te])[:, 1]; lat = (time.time() - t1) / len(te)
                p_va = clf.predict_proba(X.iloc[va])[:, 1]
                p_tr = clf.predict_proba(X.iloc[tr])[:, 1]
                size = pickled_size(clf)
                ext_probs = {n: clf.predict_proba(e[1][X.columns])[:, 1] for n, e in ext_sets.items()}
            # thresholds chosen on validation only
            policies = {"t0.5": 0.5, "val_maxf1": threshold_max_f1(y[va], p_va)}
            for ft in cfg.fpr_targets:
                policies[f"val_fpr{ft}"] = threshold_at_fpr(y[va], p_va, ft)
            preds = pd.concat([
                pd.DataFrame({"idx": tr, "y": y[tr], "prob": p_tr, "split": "train"}),
                pd.DataFrame({"idx": va, "y": y[va], "prob": p_va, "split": "val"}),
                pd.DataFrame({"idx": te, "y": y[te], "prob": p_te, "split": "test"}),
            ])
            preds.to_csv(out / f"predictions_{mname}_{seed}.csv", index=False)
            for pname, thr in policies.items():
                for sname, yy, pp in (("val", y[va], p_va), ("test", y[te], p_te)):
                    m = classification_metrics(yy, pp, thr)
                    metric_rows.append({"run_id": cfg.run_id, "dataset": cfg.dataset, "eval_set": sname,
                                        "model": mname, "seed": seed, "policy": pname, **m})
                for n, pe in ext_probs.items():
                    m = classification_metrics(ext_sets[n][0]["label"].values, pe, thr)
                    metric_rows.append({"run_id": cfg.run_id, "dataset": cfg.dataset, "eval_set": f"external:{n}",
                                        "model": mname, "seed": seed, "policy": pname, **m})
            for n, pe in ext_probs.items():
                pd.DataFrame({"idx": np.arange(len(pe)), "y": ext_sets[n][0]["label"].values, "prob": pe,
                              "split": f"external:{n}"}).to_csv(out / f"predictions_{mname}_{seed}_ext_{n}.csv", index=False)
            resource_rows.append({"run_id": cfg.run_id, "model": mname, "seed": seed, "fit_seconds": fit_s,
                                  "predict_latency_ms_per_url": lat * 1000, "model_size_bytes": size,
                                  "n_features": len(numeric) + len(categorical), "n_train": len(tr)})
            mt = classification_metrics(y[te], p_te)
            log.info("%s seed=%d test AUC=%.4f F1@0.5=%.4f fit=%.1fs", mname, seed, mt["roc_auc"], mt["f1"], fit_s)
            pd.DataFrame(metric_rows).to_csv(out / "metrics.csv", index=False)
            pd.DataFrame(resource_rows).to_csv(out / "resources.csv", index=False)
    return pd.DataFrame(metric_rows)
