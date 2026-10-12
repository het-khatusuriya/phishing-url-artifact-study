"""Post-hoc calibration comparison from saved predictions (no refitting).

For every model/seed in a run: fit isotonic and Platt (sigmoid) calibrators on
the VALIDATION predictions, apply to TEST (and external) predictions, and
report ECE / Brier / log-loss before vs after. Also recomputes the
FPR-constrained thresholds on calibrated validation scores.
Writes results/tables/calibration_<run>.csv
"""
import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.isotonic import IsotonicRegression
from sklearn.linear_model import LogisticRegression

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.urlresearch.evaluation.metrics import classification_metrics, threshold_at_fpr  # noqa: E402

RUNS = ROOT / "results" / "runs"


def main(run):
    rows = []
    for p in sorted((RUNS / run).glob("predictions_*_*.csv")):
        if "_ext_" in p.stem:
            continue
        model, seed = p.stem.replace("predictions_", "").rsplit("_", 1)
        d = pd.read_csv(p)
        va, te = d[d.split == "val"], d[d.split == "test"]
        sets = {"test": (te.y.values, te.prob.values)}
        for e in sorted((RUNS / run).glob(f"predictions_{model}_{seed}_ext_*.csv")):
            ed = pd.read_csv(e); sets[e.stem.split("_ext_")[1]] = (ed.y.values, ed.prob.values)
        cals = {"none": lambda x: x}
        iso = IsotonicRegression(out_of_bounds="clip").fit(va.prob.values, va.y.values)
        cals["isotonic"] = iso.predict
        pl = LogisticRegression(C=1e6).fit(va.prob.values.reshape(-1, 1), va.y.values)
        cals["platt"] = lambda x, pl=pl: pl.predict_proba(np.asarray(x).reshape(-1, 1))[:, 1]
        for cname, fn in cals.items():
            pv = np.clip(fn(va.prob.values), 0, 1)
            thr = threshold_at_fpr(va.y.values, pv, 0.01)
            for sname, (yy, pp) in sets.items():
                pc = np.clip(fn(pp), 0, 1)
                m = classification_metrics(yy, pc, thr)
                rows.append({"run_id": run, "model": model, "seed": int(seed), "calibration": cname, "eval_set": sname,
                             "threshold_val_fpr0.01": thr, "ece": m.get("ece"), "brier": m.get("brier"), "log_loss": m.get("log_loss"),
                             "roc_auc": m.get("roc_auc"), "recall_at_val_fpr0.01": m["recall"], "fpr_at_val_fpr0.01": m["fpr"]})
    out = pd.DataFrame(rows)
    (ROOT / "results/tables").mkdir(parents=True, exist_ok=True)
    out.to_csv(ROOT / "results/tables" / f"calibration_{run}.csv", index=False)
    print(out.groupby(["model", "calibration", "eval_set"])[["ece", "brier", "recall_at_val_fpr0.01", "fpr_at_val_fpr0.01"]].mean().round(4))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--run", required=True)
    main(ap.parse_args().run)
