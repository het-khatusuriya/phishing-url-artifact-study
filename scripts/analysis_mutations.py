"""Robustness to controlled URL mutations.

Usage: python scripts/analysis_mutations.py --run lexical_v2_grouped --models xgb lr --seed 42 --n 5000
For each model: refit on the run's training split, score `n` sampled test URLs
before/after each mutation; report flip rate, mean |Δp|, and AUC change.
Writes results/tables/mutations_<run>.csv
"""
import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.urlresearch.experiments.runner import RunConfig, load_canonical, _features, REPO  # noqa: E402
from src.urlresearch.features.lexical import FEATURE_SETS, feature_frame  # noqa: E402
from src.urlresearch.models.tabular import MODEL_FACTORIES  # noqa: E402
from src.urlresearch.data.splits import load_split  # noqa: E402
from src.urlresearch.evaluation.mutations import MUTATIONS, apply_mutation  # noqa: E402


def main(run, models, seed, n):
    cfg = RunConfig(**json.loads((REPO / "results/runs" / run / "config.json").read_text()))
    df = load_canonical(cfg.dataset, cfg.max_rows)
    X = _features(df, cfg, REPO / "data/processed/feature_cache")
    spec = FEATURE_SETS[cfg.feature_set]
    categorical = [c for c in spec["categorical"] if c in X.columns]
    numeric = [c for c in X.columns if c not in categorical]
    split = load_split(REPO / "results/runs" / run / f"split_{seed}.json")
    y = df.label.values
    rng = np.random.default_rng(seed)
    te = rng.choice(split["test"], size=min(n, len(split["test"])), replace=False)
    urls = df.url.values[te]; yt = y[te]
    rows = []
    for m in models:
        if m.startswith("charcnn"):
            from src.urlresearch.models.charcnn import CharCNNClassifier, CharCNNConfig
            clf = CharCNNClassifier(CharCNNConfig(seed=seed, **cfg.charcnn))
            clf.fit(df.url.values[split["train"]], y[split["train"]], df.url.values[split["val"]], y[split["val"]])
            score = lambda u: clf.predict_proba(u)[:, 1]
        else:
            clf = MODEL_FACTORIES[m](numeric, categorical, seed=seed, **cfg.model_params.get(m, {}))
            clf.fit(X.iloc[split["train"]], y[split["train"]])
            def score(u):
                F = feature_frame(list(u), cfg.feature_set)
                if cfg.drop_artifacts:
                    F = F.drop(columns=[c for c in spec["artifact"] if c in F.columns])
                return clf.predict_proba(F[X.columns])[:, 1]
        p0 = score(urls)
        base_auc = roc_auc_score(yt, p0)
        for name, spec_m in MUTATIONS.items():
            mu = apply_mutation(list(urls), name)
            changed = np.array([a != b for a, b in zip(urls, mu)])
            p1 = score(mu)
            flip = ((p0 >= 0.5) != (p1 >= 0.5))
            rows.append({"run_id": run, "model": m, "mutation": name, "tier": spec_m["tier"], "n": len(urls),
                         "share_applicable": float(changed.mean()),
                         "flip_rate": float(flip[changed].mean()) if changed.any() else 0.0,
                         "flip_rate_benign": float(flip[changed & (yt == 0)].mean()) if (changed & (yt == 0)).any() else 0.0,
                         "flip_rate_malicious": float(flip[changed & (yt == 1)].mean()) if (changed & (yt == 1)).any() else 0.0,
                         "mean_abs_dp": float(np.abs(p1 - p0)[changed].mean()) if changed.any() else 0.0,
                         "auc_before": base_auc, "auc_after": roc_auc_score(yt, p1),
                         "recall_before": float((p0[yt == 1] >= 0.5).mean()), "recall_after": float((p1[yt == 1] >= 0.5).mean()),
                         "fpr_before": float((p0[yt == 0] >= 0.5).mean()), "fpr_after": float((p1[yt == 0] >= 0.5).mean())})
            print(rows[-1])
    (ROOT / "results/tables").mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(ROOT / "results/tables" / f"mutations_{run}.csv", index=False)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True); ap.add_argument("--models", nargs="+", default=["xgb"])
    ap.add_argument("--seed", type=int, default=42); ap.add_argument("--n", type=int, default=5000)
    a = ap.parse_args(); main(a.run, a.models, a.seed, a.n)
