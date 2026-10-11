"""Faithful re-execution of the ORIGINAL repository pipeline (notebooks 02-07)
using the original, unmodified modules in src/ (feature_extractor,
data_splitting, model factories, ensemble, evaluation.metrics).

Differences from the notebooks are limited to I/O: input is a canonical
parquet (url,label) instead of data/raw/raw_data.csv, labels are mapped back to
the strings 'legitimate'/'phishing', and outputs go to
results/reproduction/<dataset>/. Everything else follows the notebooks:
28 features -> pd.get_dummies(tld_type) on the FULL dataset -> stratified
60/20/20 split (seed 42) -> LR/RF/XGB pipelines + weighted soft vote (1,2,2)
-> accuracy/precision/recall/F1 + confusion counts on the test split.

Usage: python scripts/reproduce_original_pipeline.py --dataset phiusiil
"""
import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score, average_precision_score

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

# ---- original, unmodified modules ----
from src.features.feature_extractor import extract_features            # noqa: E402
from src.data.data_splitting import create_data_splits                  # noqa: E402
from src.models.logistic_regression import create_logistic_regression_pipeline  # noqa: E402
from src.models.random_forest import create_random_forest_pipeline      # noqa: E402
from src.models.xgboost import create_xgboost_pipeline                  # noqa: E402
from src.models.ensemble import create_weighted_soft_voting_ensemble    # noqa: E402
from src.evaluation.metrics import calculate_classification_metrics     # noqa: E402


def main(dataset):
    out = ROOT / "results" / "reproduction" / dataset
    out.mkdir(parents=True, exist_ok=True)
    df = pd.read_parquet(ROOT / "data/processed/canonical" / f"{dataset}.parquet")[["url", "label"]]
    df["label"] = df["label"].map({0: "legitimate", 1: "phishing"})
    t0 = time.time()
    feats, failed = [], 0
    for u in df["url"]:
        try:
            feats.append(extract_features(u))
        except Exception:  # the original extractor raises on malformed URLs (e.g. bad IPv6)
            failed += 1
            feats.append(None)
    keep = [f is not None for f in feats]
    df = df[keep].reset_index(drop=True)
    df_features = pd.DataFrame([f for f in feats if f is not None])
    df_features.insert(0, "url", df["url"].values)
    df_features.insert(1, "label", df["label"].values)
    t_feat = time.time() - t0
    # NB05: one-hot on the full dataset BEFORE splitting (as in the original)
    tld = pd.get_dummies(df_features["tld_type"], prefix="tld", dtype=int)
    df_model = pd.concat([df_features.drop(columns=["tld_type"]), tld], axis=1)
    cols = [c for c in df_model.columns if c not in ["url", "label"]]
    X_tr, X_va, X_te, y_tr, y_va, y_te = create_data_splits(df_model, cols, "label", 0.20, 0.20, 42)
    models = {
        "Logistic Regression": create_logistic_regression_pipeline(),
        "Random Forest": create_random_forest_pipeline(),
        "XGBoost": create_xgboost_pipeline(),
    }
    models["Weighted Soft-Voting Ensemble"] = create_weighted_soft_voting_ensemble(
        create_logistic_regression_pipeline(), create_random_forest_pipeline(), create_xgboost_pipeline(), (1, 2, 2))
    rows = []
    for name, m in models.items():
        t1 = time.time(); m.fit(X_tr, y_tr); fit_s = time.time() - t1
        for split, X, y in (("validation", X_va, y_va), ("test", X_te, y_te)):
            pred = m.predict(X); prob = m.predict_proba(X)[:, 1]
            r = calculate_classification_metrics(y, pred, name, split)
            r.update({"roc_auc": roc_auc_score(y, prob), "pr_auc": average_precision_score(y, prob),
                      "fit_seconds": fit_s})
            rows.append(r)
        print(name, "done", round(fit_s, 1), "s")
    res = pd.DataFrame(rows)
    res.to_csv(out / "original_pipeline_metrics.csv", index=False)
    (out / "meta.json").write_text(json.dumps({
        "dataset": dataset, "rows_used": len(df), "rows_failed_original_extractor": failed,
        "n_model_columns": len(cols), "n_tld_columns": int(tld.shape[1]),
        "split_sizes": [len(X_tr), len(X_va), len(X_te)], "feature_seconds": t_feat,
        "note": "Original src/ modules executed unchanged; input data substituted because raw_data.csv is unavailable."},
        indent=2))
    print(res[res.split == "test"].round(4).to_string(index=False))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--dataset", default="phiusiil")
    main(ap.parse_args().dataset)
