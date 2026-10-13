"""Train a deployable model bundle under the documented protocol.

Usage: python scripts/train_final_model.py --dataset main --feature-set lexical_v2 --model xgb
       [--drop-artifacts] [--split grouped] [--seed 42] [--calibrate isotonic|sigmoid|none]
Fits on train, selects thresholds and (optionally) a calibrator on validation,
reports validation + test metrics, and writes models/<name>.joblib plus a JSON
card. Test metrics are reported once and never used for selection.
"""
import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.urlresearch.experiments.runner import RunConfig, load_canonical, _features, make_split, environment_info  # noqa: E402
from src.urlresearch.features.lexical import FEATURE_SETS  # noqa: E402
from src.urlresearch.models.tabular import MODEL_FACTORIES  # noqa: E402
from src.urlresearch.evaluation.metrics import classification_metrics, threshold_at_fpr, threshold_max_f1  # noqa: E402
from src.urlresearch.prediction.predictor import save_bundle  # noqa: E402


def main(a):
    cfg = RunConfig(run_id="final", dataset=a.dataset, feature_set=a.feature_set, drop_artifacts=a.drop_artifacts,
                    split=a.split, seeds=[a.seed])
    df = load_canonical(a.dataset)
    X = _features(df, cfg, ROOT / "data/processed/feature_cache")
    spec = FEATURE_SETS[a.feature_set]
    categorical = [c for c in spec["categorical"] if c in X.columns]
    numeric = [c for c in X.columns if c not in categorical]
    split = make_split(df, cfg, a.seed)
    y = df.label.values
    tr, va, te = split["train"], split["val"], split["test"]
    clf = MODEL_FACTORIES[a.model](numeric, categorical, seed=a.seed)
    t0 = time.time(); clf.fit(X.iloc[tr], y[tr]); fit_s = time.time() - t0
    p_va = clf.predict_proba(X.iloc[va])[:, 1]
    calibrator = None
    if a.calibrate != "none":
        if a.calibrate == "isotonic":
            from sklearn.isotonic import IsotonicRegression
            calibrator = IsotonicRegression(out_of_bounds="clip").fit(p_va, y[va])
            p_va_c = calibrator.predict(p_va)
        else:
            from sklearn.linear_model import LogisticRegression
            calibrator = LogisticRegression(C=1e6).fit(p_va.reshape(-1, 1), y[va])
            p_va_c = calibrator.predict_proba(p_va.reshape(-1, 1))[:, 1]
    else:
        p_va_c = p_va
    thresholds = {"t0.5": 0.5, "val_maxf1": threshold_max_f1(y[va], p_va_c),
                  "val_fpr0.01": threshold_at_fpr(y[va], p_va_c, 0.01),
                  "val_fpr0.001": threshold_at_fpr(y[va], p_va_c, 0.001)}
    p_te = clf.predict_proba(X.iloc[te])[:, 1]
    if calibrator is not None:
        p_te = calibrator.predict(p_te) if a.calibrate == "isotonic" else calibrator.predict_proba(p_te.reshape(-1, 1))[:, 1]
    name = f"{a.model}_{a.feature_set}{'_noart' if a.drop_artifacts else ''}_{a.dataset}_{a.split}_s{a.seed}"
    card = {"name": name, "created": datetime.now(timezone.utc).isoformat(), "dataset": a.dataset,
            "feature_set": a.feature_set, "drop_artifacts": a.drop_artifacts, "split": a.split, "seed": a.seed,
            "model": a.model, "calibration": a.calibrate, "fit_seconds": fit_s, "thresholds": thresholds,
            "n_train": int(len(tr)), "n_val": int(len(va)), "n_test": int(len(te)),
            "validation_metrics": {k: classification_metrics(y[va], p_va_c, t) for k, t in thresholds.items()},
            "test_metrics": {k: classification_metrics(y[te], p_te, t) for k, t in thresholds.items()},
            "environment": environment_info(),
            "limitations": "Model estimates only; trained on a specific collection of URLs; not a guarantee of safety."}
    (ROOT / "models").mkdir(exist_ok=True)
    save_bundle(ROOT / "models" / f"{name}.joblib", clf, a.feature_set, X.columns, thresholds,
                a.drop_artifacts, calibrator, card)
    (ROOT / "models" / f"{name}.card.json").write_text(json.dumps(card, indent=2))
    print(json.dumps({k: {m: round(v[m], 4) for m in ("recall", "fpr", "precision", "f1")}
                      for k, v in card["test_metrics"].items()}, indent=1))
    print("saved models/", name)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", default="main"); ap.add_argument("--feature-set", default="lexical_v2")
    ap.add_argument("--model", default="xgb"); ap.add_argument("--drop-artifacts", action="store_true")
    ap.add_argument("--split", default="grouped"); ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--calibrate", default="isotonic", choices=["isotonic", "sigmoid", "none"])
    main(ap.parse_args())
