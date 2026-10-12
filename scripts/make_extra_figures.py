"""Summary figures for the paper: mutation flip rates and LOCO transfer.
Reads results/tables/mutations_*.csv and results/runs/LOCO_*/metrics.csv.
Writes results/figures/mutation_flip_rates.{png,pdf}, loco_summary.{png,pdf}."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
T, FIG, RUNS = ROOT / "results/tables", ROOT / "results/figures", ROOT / "results/runs"
plt.rcParams.update({"font.size": 8.5, "axes.spines.top": False, "axes.spines.right": False})
ORDER = ["upper_host", "trailing_slash", "default_port", "encode_path_char", "add_fragment",
         "toggle_www", "toggle_scheme", "add_utm_query"]
NICE = {"upper_host": "upper-case host (A)", "trailing_slash": "empty-path slash (A)", "default_port": "default port (A)",
        "encode_path_char": "%-encode path char (A)", "add_fragment": "add fragment (A)", "toggle_www": "toggle www. (B)",
        "toggle_scheme": "toggle http/https (B)", "add_utm_query": "add tracking param (B)"}

# --- mutations
frames = [pd.read_csv(p) for p in sorted(T.glob("mutations_*.csv"))]
if frames:
    d = pd.concat(frames)
    series = [("A_b28_grouped", "xgb", "XGBoost, corpus A (orig. features)"),
              ("A_b28_grouped", "lr", "LR, corpus A (orig. features)"),
              ("LOCO_phiusiil_v2", "xgb", "XGBoost, pooled corpora (lexical_v2)")]
    fig, axes = plt.subplots(1, 2, figsize=(8.6, 3.4), sharey=True)
    for ax, col, title in zip(axes, ["flip_rate_benign", "flip_rate_malicious"], ["benign URLs", "malicious URLs"]):
        y = np.arange(len(ORDER)); h = 0.26
        for k, (run, model, lab) in enumerate(series):
            s = d[(d.run_id == run) & (d.model == model)].set_index("mutation").reindex(ORDER)
            ax.barh(y + (k - 1) * h, s[col] * 100, h, label=lab, color=["#C44E52", "#DD8452", "#4C72B0"][k])
        ax.set_yticks(y); ax.set_yticklabels([NICE[m] for m in ORDER]); ax.invert_yaxis()
        ax.set_xlabel(f"% of {title} whose decision flips"); ax.set_xlim(0, 105)
        ax.set_title(f"Decision flips, {title}", loc="left", fontsize=9)
    fig.legend(*axes[0].get_legend_handles_labels(), loc="lower center", ncol=3, fontsize=7.5, frameon=False,
               bbox_to_anchor=(0.5, -0.06))
    fig.tight_layout(rect=(0, 0.06, 1, 1)); fig.savefig(FIG / "mutation_flip_rates.png", dpi=300, bbox_inches="tight")
    fig.savefig(FIG / "mutation_flip_rates.pdf", bbox_inches="tight"); plt.close(fig); print("saved mutation_flip_rates")

# --- LOCO summary
rows = []
for held in ["phiusiil", "lineage253k", "hannousse2021", "ebbu2017", "phishstorm", "iscx2016"]:
    for rep in ("v2", "v2noart", "v2canon"):
        p = RUNS / f"LOCO_{held}_{rep}" / "metrics.csv"
        if not p.exists():
            continue
        m = pd.read_csv(p)
        for model, g in m.groupby("model"):
            e = g[(g.eval_set == f"external:{held}") & (g.policy == "val_fpr0.01")]
            t = g[(g.eval_set == "test") & (g.policy == "t0.5")]
            if len(e) < 2:
                continue
            rows.append({"held": held, "rep": rep, "model": model, "auc_pool": t.roc_auc.mean(), "auc_held": e.roc_auc.mean(),
                         "auc_sd": e.roc_auc.std(), "fpr": e.fpr.mean(), "fpr_sd": e.fpr.std(), "recall": e.recall.mean()})
L = pd.DataFrame(rows)
SHORT = {"phiusiil": "PhiUSIIL", "lineage253k": "Corpus B", "hannousse2021": "Hannousse 2021",
         "ebbu2017": "Ebbu2017", "phishstorm": "PhishStorm", "iscx2016": "ISCX-2016"}
if len(L):
    L.to_csv(T / "loco_summary.csv", index=False)
    x = L[(L.rep == "v2")]
    helds = list(dict.fromkeys(x.held)); models = ["lr", "rf", "xgb"]; lab = {"lr": "LR", "rf": "RF", "xgb": "XGBoost"}
    fig, axes = plt.subplots(1, 2, figsize=(8.6, 3.0))
    w = 0.26
    for k, mo in enumerate(models):
        s = x[x.model == mo].set_index("held").reindex(helds)
        xs = np.arange(len(helds)) + (k - 1) * w
        axes[0].bar(xs, s.auc_held, w, yerr=s.auc_sd.fillna(0), capsize=2, label=lab[mo], color=["#DD8452", "#55A868", "#4C72B0"][k])
        axes[1].bar(xs, s.fpr * 100, w, yerr=s.fpr_sd.fillna(0) * 100, capsize=2, color=["#DD8452", "#55A868", "#4C72B0"][k])
    for ax in axes:
        ax.set_xticks(np.arange(len(helds))); ax.set_xticklabels([SHORT.get(h, h) for h in helds], fontsize=8)
    axes[0].set_ylim(0.5, 1.0); axes[0].set_ylabel("ROC-AUC on held-out corpus"); axes[0].set_xlabel("held-out corpus"); axes[1].set_xlabel("held-out corpus"); axes[0].legend(fontsize=7)
    axes[1].axhline(1, color="k", ls=":", lw=0.8); axes[1].set_ylabel("% held-out benign URLs flagged\n(threshold: validation FPR ≤ 1 %)")
    axes[0].set_title("Ranking transfer", loc="left", fontsize=9); axes[1].set_title("Threshold transfer (dotted: 1 % budget)", loc="left", fontsize=9)
    fig.tight_layout(); fig.savefig(FIG / "loco_summary.png", dpi=300, bbox_inches="tight")
    fig.savefig(FIG / "loco_summary.pdf", bbox_inches="tight"); plt.close(fig); print("saved loco_summary")
    print(L.round(3).to_string(index=False))
