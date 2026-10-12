"""Generate publication figures from saved experiment outputs only.

Usage: python scripts/make_figures.py [--runs run_a run_b ...]
Reads  results/runs/<run>/{metrics.csv,predictions_*.csv,split_*.json}
       results/tables/*.csv (from aggregate_results.py)
Writes results/figures/<name>.{png,pdf}
Nothing is hand-edited: every number is read from disk.
"""
import argparse
import json
import os
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import precision_recall_curve, roc_curve

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.urlresearch.evaluation.metrics import reliability_table  # noqa: E402

RUNS = Path(os.environ.get("URLRESEARCH_RUNS", ROOT / "results" / "runs"))
FIG = Path(os.environ.get("URLRESEARCH_FIGURES", ROOT / "results" / "figures"))
TABLES = Path(os.environ.get("URLRESEARCH_TABLES", ROOT / "results" / "tables"))
plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False,
                     "figure.dpi": 150, "savefig.dpi": 300, "legend.frameon": False})
MODEL_LABEL = {"lr": "Logistic regression", "rf": "Random forest", "xgb": "XGBoost", "lgbm": "LightGBM",
               "softvote": "Soft vote 1:2:2 (orig.)", "stack": "Stacking", "charcnn": "Char-CNN",
               "charcnn_hybrid": "Char-CNN + lexical"}
PALETTE = ["#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B3", "#937860", "#DA8BC3", "#8C8C8C"]


def save(fig, name):
    FIG.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG / f"{name}.png", bbox_inches="tight")
    fig.savefig(FIG / f"{name}.pdf", bbox_inches="tight")
    plt.close(fig)
    print("saved", name)


def load_test_preds(run, model, seed):
    p = RUNS / run / f"predictions_{model}_{seed}.csv"
    d = pd.read_csv(p)
    return d[d.split == "test"]


def first_seed(run):
    seeds = sorted(int(p.stem.split("_")[1].split(".")[0]) for p in (RUNS / run).glob("split_*.json"))
    return seeds[0]


def models_in(run):
    return sorted({p.stem.replace("predictions_", "").rsplit("_", 1)[0]
                   for p in (RUNS / run).glob("predictions_*.csv") if "_ext_" not in p.stem})


def fig_roc_pr(run):
    seed = first_seed(run)
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.3))
    for i, m in enumerate(models_in(run)):
        d = load_test_preds(run, m, seed)
        fpr, tpr, _ = roc_curve(d.y, d.prob)
        axes[0].plot(fpr, tpr, color=PALETTE[i % 8], label=MODEL_LABEL.get(m, m), lw=1.4)
        pr, rc, _ = precision_recall_curve(d.y, d.prob)
        axes[1].plot(rc, pr, color=PALETTE[i % 8], label=MODEL_LABEL.get(m, m), lw=1.4)
    axes[0].set_xscale("log"); axes[0].set_xlim(1e-4, 1); axes[0].set_ylim(0, 1.02)
    axes[0].set_xlabel("False-positive rate (log scale)"); axes[0].set_ylabel("True-positive rate (recall)")
    axes[0].set_title(f"ROC — {run}", loc="left")
    axes[1].set_xlabel("Recall"); axes[1].set_ylabel("Precision"); axes[1].set_ylim(0.5, 1.02)
    axes[1].set_title("Precision–recall", loc="left"); axes[1].legend(fontsize=7, loc="lower left")
    save(fig, f"roc_pr_{run}")


def fig_reliability(run):
    seed = first_seed(run)
    ms = models_in(run)
    fig, ax = plt.subplots(figsize=(3.6, 3.4))
    ax.plot([0, 1], [0, 1], "k--", lw=0.8, label="Perfect calibration")
    for i, m in enumerate(ms):
        d = load_test_preds(run, m, seed)
        rt = pd.DataFrame(reliability_table(d.y.values, d.prob.values, 10)).dropna()
        ax.plot(rt.mean_pred, rt.frac_pos, marker="o", ms=3, lw=1.2, color=PALETTE[i % 8], label=MODEL_LABEL.get(m, m))
    ax.set_xlabel("Mean predicted P(malicious)"); ax.set_ylabel("Observed fraction malicious")
    ax.set_title(f"Reliability — {run}", loc="left"); ax.legend(fontsize=6.5)
    save(fig, f"reliability_{run}")


def fig_metric_comparison(runs, metric="roc_auc", policy="t0.5", eval_set="test"):
    summ = pd.read_csv(TABLES / "summary_by_run_model.csv")
    s = summ[(summ.policy == policy) & (summ.eval_set == eval_set) & (summ.run_id.isin(runs))]
    if s.empty:
        return
    models = [m for m in MODEL_LABEL if m in set(s.model)]
    fig, ax = plt.subplots(figsize=(max(4, 1.1 * len(models) + 1.5), 3.2))
    w = 0.8 / max(len(runs), 1)
    for j, run in enumerate(runs):
        r = s[s.run_id == run].set_index("model").reindex(models)
        x = np.arange(len(models)) + j * w
        ax.bar(x, r[f"{metric}_mean"], w, yerr=r[f"{metric}_std"].fillna(0), capsize=2,
               color=PALETTE[j % 8], label=run)
    ax.set_xticks(np.arange(len(models)) + w * (len(runs) - 1) / 2)
    ax.set_xticklabels([MODEL_LABEL[m] for m in models], rotation=20, ha="right")
    lo = max(0.0, float(np.nanmin(s[f"{metric}_mean"]) - 0.05))
    ax.set_ylim(lo, 1.0); ax.set_ylabel(metric.replace("_", " ").upper() + " (mean ± sd over seeds)")
    ax.set_title(f"{eval_set} · policy {policy}", loc="left"); ax.legend(fontsize=7)
    save(fig, f"compare_{metric}_{'_vs_'.join(runs)}")


def fig_split_overlap(runs):
    rows = []
    for run in runs:
        for sp in sorted((RUNS / run).glob("split_*.json")):
            meta = json.loads(sp.read_text())["meta"]
            rows.append({"run": run, "strategy": meta["strategy"], "seed": meta["seed"],
                         "share": meta["overlap"]["share_test_rows_with_group_in_train"]})
    if not rows:
        return
    df = pd.DataFrame(rows)
    g = df.groupby("run")["share"].agg(["mean", "std"]).reset_index()
    fig, ax = plt.subplots(figsize=(3.6, 2.6))
    ax.bar(g.run, g["mean"] * 100, yerr=g["std"].fillna(0) * 100, color=PALETTE[:len(g)], capsize=3)
    ax.set_ylabel("% test URLs whose registered\ndomain also appears in training")
    ax.set_xticklabels(g.run, rotation=15, ha="right")
    save(fig, "split_domain_overlap")


def fig_external(run, metric="roc_auc"):
    m = pd.read_csv(RUNS / run / "metrics.csv")
    m = m[(m.policy == "t0.5")]
    POS_ONLY = {"external:phishtank", "external:urlhaus", "external:openphish"}  # AUC undefined
    sets = [s for s in m.eval_set.unique() if s == "test" or (s.startswith("external:") and s not in POS_ONLY)]
    if len(sets) < 2:
        return
    g = m[m.eval_set.isin(sets)].groupby(["model", "eval_set"])[metric].agg(["mean", "std"]).reset_index()
    models = [x for x in MODEL_LABEL if x in set(g.model)]
    fig, ax = plt.subplots(figsize=(max(4, 1.1 * len(models) + 1.5), 3.2))
    w = 0.8 / len(sets)
    for j, s in enumerate(sets):
        r = g[g.eval_set == s].set_index("model").reindex(models)
        ax.bar(np.arange(len(models)) + j * w, r["mean"], w, yerr=r["std"].fillna(0), capsize=2,
               color=PALETTE[j % 8], label=s.replace("external:", "ext: "))
    ax.set_xticks(np.arange(len(models)) + w * (len(sets) - 1) / 2)
    ax.set_xticklabels([MODEL_LABEL[x] for x in models], rotation=20, ha="right")
    ax.set_ylim(0.3, 1.0); ax.set_ylabel(metric.replace("_", " ").upper() + " (dotted: chance)")
    ax.axhline(0.5, color="k", lw=0.6, ls=":")
    ax.set_title(f"In-distribution vs external — {run}", loc="left")
    ax.legend(fontsize=7, loc="upper left", bbox_to_anchor=(1.0, 1.0))
    save(fig, f"external_{metric}_{run}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--runs", nargs="*", default=None)
    a = ap.parse_args()
    runs = a.runs or sorted(p.name for p in RUNS.iterdir() if (p / "metrics.csv").exists())
    for r in runs:
        fig_roc_pr(r); fig_reliability(r); fig_external(r)
    if (TABLES / "summary_by_run_model.csv").exists():
        fig_metric_comparison(runs, "roc_auc"); fig_metric_comparison(runs, "tpr_at_fpr_0.01")
        fig_metric_comparison(runs, "f1")
    fig_split_overlap(runs)
