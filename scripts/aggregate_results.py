"""Aggregate results/runs/*/metrics.csv into publication tables with CIs.

Writes results/tables/
  all_metrics_long.csv          every row from every run
  summary_by_run_model.csv      mean ± std across seeds (test set, each policy)
  bootstrap_ci_<run>.csv        per-model bootstrap 95% CIs (seed = first seed) on test
  paired_tests_<run>.csv        paired bootstrap deltas + McNemar vs a reference model
"""
import argparse
import json
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.urlresearch.evaluation.metrics import (bootstrap_ci, mcnemar_test, metric_fn,  # noqa: E402
                                                paired_bootstrap_delta)

RUNS = Path(os.environ.get("URLRESEARCH_RUNS", ROOT / "results" / "runs"))
TABLES = Path(os.environ.get("URLRESEARCH_TABLES", ROOT / "results" / "tables"))
KEY = ["roc_auc", "pr_auc", "f1", "precision", "recall", "fpr", "fnr", "accuracy", "tpr_at_fpr_0.01",
       "tpr_at_fpr_0.001", "ece", "brier"]


def main(reference="xgb", n_boot=1000):
    TABLES.mkdir(parents=True, exist_ok=True)
    frames = []
    for mpath in sorted(RUNS.glob("*/metrics.csv")):
        df = pd.read_csv(mpath)
        frames.append(df)
    if not frames:
        print("no runs found"); return
    allm = pd.concat(frames, ignore_index=True)
    allm.to_csv(TABLES / "all_metrics_long.csv", index=False)
    present = [k for k in KEY if k in allm.columns]
    g = allm.groupby(["run_id", "eval_set", "model", "policy"])[present]
    summ = g.agg(["mean", "std", "count"])
    summ.columns = [f"{a}_{b}" for a, b in summ.columns]
    summ.reset_index().to_csv(TABLES / "summary_by_run_model.csv", index=False)

    for run_dir in sorted(RUNS.iterdir()):
        preds = sorted(run_dir.glob("predictions_*_*.csv"))
        if not preds:
            continue
        # group by seed; use first seed for bootstrap CIs and paired tests
        by_seed = {}
        for p in preds:
            stem = p.stem.replace("predictions_", "")
            if "_ext_" in stem:
                continue
            model, seed = stem.rsplit("_", 1)
            by_seed.setdefault(int(seed), {})[model] = p
        if not by_seed:
            continue
        seed = min(by_seed)
        rows, pairs = [], []
        ref = None
        for model, p in by_seed[seed].items():
            d = pd.read_csv(p); d = d[d.split == "test"]
            y, pr = d.y.values, d.prob.values
            rec = {"run_id": run_dir.name, "model": model, "seed": seed, "n_test": len(d)}
            for mname in ("roc_auc", "pr_auc", "f1", "tpr_at_fpr_0.01"):
                pt, lo, hi = bootstrap_ci(y, pr, metric_fn(mname), n_boot=n_boot, seed=0)
                rec[f"{mname}"] = pt; rec[f"{mname}_lo"] = lo; rec[f"{mname}_hi"] = hi
            rows.append(rec)
            if model == reference:
                ref = (y, pr)
        pd.DataFrame(rows).to_csv(TABLES / f"bootstrap_ci_{run_dir.name}.csv", index=False)
        if ref is not None:
            for model, p in by_seed[seed].items():
                if model == reference:
                    continue
                d = pd.read_csv(p); d = d[d.split == "test"]
                y, pr = d.y.values, d.prob.values
                rec = {"run_id": run_dir.name, "model": model, "reference": reference, "seed": seed}
                for mname in ("roc_auc", "pr_auc", "f1"):
                    r = paired_bootstrap_delta(y, pr, ref[1], metric_fn(mname), n_boot=n_boot, seed=0)
                    rec.update({f"{mname}_delta": r["delta"], f"{mname}_ci_lo": r["ci_lo"],
                                f"{mname}_ci_hi": r["ci_hi"], f"{mname}_p_boot": r["p_boot"]})
                mc = mcnemar_test(y, (pr >= 0.5).astype(int), (ref[1] >= 0.5).astype(int))
                rec.update({"mcnemar_n01": mc["n01"], "mcnemar_n10": mc["n10"], "mcnemar_p": mc["p_value"]})
                pairs.append(rec)
            pd.DataFrame(pairs).to_csv(TABLES / f"paired_tests_{run_dir.name}.csv", index=False)
        print("aggregated", run_dir.name)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--reference", default="xgb"); ap.add_argument("--n-boot", type=int, default=1000)
    a = ap.parse_args(); main(a.reference, a.n_boot)
