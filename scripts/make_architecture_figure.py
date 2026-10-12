"""Draw the study's pipeline / system architecture (Figure: architecture).
Writes results/figures/architecture.{png,pdf}. Purely schematic; no data."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT = Path(__file__).resolve().parents[1]
fig, ax = plt.subplots(figsize=(9.2, 5.0))
ax.set_xlim(0, 100); ax.set_ylim(0, 60); ax.axis("off")

C = {"data": "#DCE8F5", "rep": "#E6F2E1", "model": "#FBE8D3", "eval": "#EFE3F3", "out": "#F2F2F2"}


def box(x, y, w, h, title, lines, color):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.4,rounding_size=1.2", fc=color, ec="#555555", lw=0.8))
    ax.text(x + w / 2, y + h - 2.2, title, ha="center", va="top", fontsize=8.2, weight="bold")
    for i, l in enumerate(lines):
        ax.text(x + w / 2, y + h - 5.6 - i * 2.75, l, ha="center", va="top", fontsize=6.8)


def arrow(x1, y1, x2, y2):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=10, lw=0.9, color="#333333"))


box(1, 36, 22, 18, "1. Sources", ["PhiUSIIL (A), lineage (B)", "Hannousse, Ebbu2017,", "PhishStorm, ISCX-2016", "PhishTank, URLhaus, OpenPhish"], C["data"])
box(27, 36, 22, 18, "2. Cleaning", ["label map (malicious = 1)", "normalised dedup", "conflict removal", "registered-domain group"], C["data"])
box(53, 36, 22, 18, "3. Splits", ["random 60/20/20", "domain-grouped (no overlap)", "leave-one-corpus-out", "indices + overlap saved"], C["data"])
box(79, 36, 20, 18, "4. Representations", ["baseline28 (original)", "lexical_v2 (91)", "v2 − artifact columns", "canonical (86) / chars"], C["rep"])
box(53, 13, 22, 18, "5. Models", ["LR, RF, XGBoost, LightGBM", "soft vote 1:2:2 (original)", "char-CNN (raw / canon.)", "char + lexical hybrid"], C["model"])
box(27, 13, 22, 18, "6. Validation only", ["thresholds: 0.5, max-F1,", "FPR ≤ 1 %, FPR ≤ 0.1 %", "isotonic / Platt calibration", "early stopping (char)"], C["eval"])
box(1, 13, 22, 18, "7. Evaluation", ["test split + external", "corpora + timestamped feeds", "CIs, paired tests, probe,", "SHAP, mutations, errors"], C["eval"])
box(27, 0.6, 46, 9, "8. Outputs", ["results/runs/* · tables · figures · paper"], C["out"])

arrow(23.8, 45, 26.2, 45); arrow(49.8, 45, 52.2, 45); arrow(75.8, 45, 78.2, 45)
arrow(89, 35.2, 75.5, 26); arrow(52.2, 22, 49.8, 22); arrow(26.2, 22, 23.8, 22); arrow(12, 12.2, 27, 6.5)
ax.text(50, 59.5, "Artifact-aware evaluation pipeline (all fitting on training rows; all selection on validation rows)",
        ha="center", va="top", fontsize=8.5, style="italic")
out = ROOT / "results" / "figures"
out.mkdir(parents=True, exist_ok=True)
fig.savefig(out / "architecture.png", dpi=300, bbox_inches="tight")
fig.savefig(out / "architecture.pdf", bbox_inches="tight")
print("saved")
