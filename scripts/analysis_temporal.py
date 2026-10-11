"""Temporal recall on the timestamped positive-only feeds (PhishTank, URLhaus).

Uses saved external predictions (predictions_<model>_<seed>_ext_<feed>.csv,
row idx = row of the canonical parquet) and the feed's submission timestamps.
For each run/model and each submission year: recall at (a) 0.5 and (b) the
validation-chosen FPR<=1% threshold of that run/model/seed.
Also reports the https share of the feed per year (the artifact driver).

Usage: python scripts/analysis_temporal.py [--runs ...] [--feed phishtank]
Writes results/tables/temporal_recall_<feed>.csv and results/figures/temporal_recall_<feed>.{png,pdf}
"""
import argparse
import os
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
RUNS = Path(os.environ.get("URLRESEARCH_RUNS", ROOT / "results" / "runs"))
CAN = ROOT / "data/processed/canonical"
LABEL = {"lr": "LR", "rf": "RF", "xgb": "XGBoost", "lgbm": "LightGBM", "softvote": "Soft vote",
         "charcnn": "Char-CNN", "charcnn_canon": "Char-CNN (canon.)", "charcnn_hybrid": "Char+lexical"}


def main(runs, feed, min_n):
    feed_df = pd.read_parquet(CAN / f"{feed}.parquet")
    year = pd.to_datetime(feed_df["timestamp"], utc=True).dt.year.values
    https = feed_df["url"].str.lower().str.startswith("https://").values
    rows = []
    for run in runs:
        rd = RUNS / run
        if not (rd / "metrics.csv").exists():
            continue
        met = pd.read_csv(rd / "metrics.csv")
        for p in sorted(rd.glob(f"predictions_*_ext_{feed}.csv")):
            stem = p.stem.replace("predictions_", "").replace(f"_ext_{feed}", "")
            model, seed = stem.rsplit("_", 1); seed = int(seed)
            d = pd.read_csv(p)
            sel = met[(met.model == model) & (met.seed == seed) & (met.policy == "val_fpr0.01") & (met.eval_set == "test")]
            thr = float(sel.threshold.iloc[0]) if len(sel) else 0.5
            prob = d.prob.values; yr = year[d.idx.values]
            for y in np.unique(yr):
                m = yr == y
                if m.sum() < min_n:
                    continue
                rows.append({"run_id": run, "model": model, "seed": seed, "year": int(y), "n": int(m.sum()),
                             "recall_t0.5": float((prob[m] >= 0.5).mean()),
                             "recall_val_fpr0.01": float((prob[m] >= thr).mean()),
                             "share_https": float(https[d.idx.values][m].mean())})
    out = pd.DataFrame(rows)
    (ROOT / "results/tables").mkdir(parents=True, exist_ok=True)
    out.to_csv(ROOT / "results/tables" / f"temporal_recall_{feed}.csv", index=False)
    if out.empty:
        print("no rows"); return
    agg = out.groupby(["run_id", "model", "year"]).agg(n=("n", "first"), recall=("recall_val_fpr0.01", "mean"),
                                                      sd=("recall_val_fpr0.01", "std"), https=("share_https", "first")).reset_index()
    print(agg.round(3).to_string(index=False))
    # figure: one panel per run, lines per model; secondary axis https share
    runs_present = [r for r in runs if r in set(agg.run_id)]
    fig, axes = plt.subplots(1, len(runs_present), figsize=(3.2 * len(runs_present), 3.0), sharey=True, squeeze=False)
    for ax, run in zip(axes[0], runs_present):
        a = agg[agg.run_id == run]
        for m, g in a.groupby("model"):
            ax.errorbar(g.year, g.recall, yerr=g.sd.fillna(0), marker="o", ms=3, lw=1.2, capsize=2, label=LABEL.get(m, m))
        h = a.drop_duplicates("year").sort_values("year")
        ax2 = ax.twinx(); ax2.bar(h.year, h.https, color="grey", alpha=0.18, width=0.8); ax2.set_ylim(0, 1)
        ax2.set_yticks([]) if ax is not axes[0][-1] else ax2.set_ylabel("share https (bars)")
        ax.set_title(run, loc="left", fontsize=8); ax.set_xlabel("PhishTank submission year" if feed == "phishtank" else "date added (year)")
        ax.set_ylim(0, 1.02); ax.set_zorder(ax2.get_zorder() + 1); ax.patch.set_visible(False)
    axes[0][0].set_ylabel("recall at validation FPR=1% threshold"); axes[0][0].legend(fontsize=6.5, loc="lower left")
    (ROOT / "results/figures").mkdir(parents=True, exist_ok=True)
    fig.savefig(ROOT / "results/figures" / f"temporal_recall_{feed}.png", dpi=300, bbox_inches="tight")
    fig.savefig(ROOT / "results/figures" / f"temporal_recall_{feed}.pdf", bbox_inches="tight")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", nargs="+", default=["A_b28_grouped", "A_v2_grouped", "A_v2noart_grouped", "A_v2canon_grouped"])
    ap.add_argument("--feed", default="phishtank"); ap.add_argument("--min-n", type=int, default=100)
    a = ap.parse_args(); main(a.runs, a.feed, a.min_n)
