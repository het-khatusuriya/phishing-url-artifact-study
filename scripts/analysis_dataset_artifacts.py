"""Per-dataset, per-class collection-artifact statistics.

For every canonical corpus: share of https, explicit scheme, leading 'www.',
IP host, empty path (homepage), query string, URL length median, registered
domains per URL, and the single-feature AUC of each artifact. Writes
results/tables/dataset_artifact_stats.csv and results/figures/dataset_artifacts.{png,pdf}
"""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.urlresearch.features.url_parse import parse_url  # noqa: E402

CAN = ROOT / "data/processed/canonical"
NAMES = ["phiusiil", "lineage253k", "hannousse2021", "ebbu2017", "phishstorm", "iscx2016", "kaggle651k_bp",
         "phishtank", "urlhaus", "openphish"]


def stats(df):
    P = df.url.map(parse_url)
    f = pd.DataFrame({
        "https": P.map(lambda p: p.scheme == "https").astype(int),
        "explicit_scheme": P.map(lambda p: p.had_scheme).astype(int),
        "www": P.map(lambda p: bool(p.labels) and p.labels[0].startswith("www")).astype(int),
        "ip_host": P.map(lambda p: p.is_ip).astype(int),
        "homepage": P.map(lambda p: p.path in ("", "/") and not p.query).astype(int),
        "has_query": P.map(lambda p: bool(p.query)).astype(int),
        "url_len": df.url.str.len(),
        "label": df.label.values,
    })
    return f


def main():
    rows = []
    for n in NAMES:
        p = CAN / f"{n}.parquet"
        if not p.exists():
            continue
        df = pd.read_parquet(p)
        f = stats(df)
        for lbl, g in f.groupby("label"):
            rows.append({"dataset": n, "label": int(lbl), "n": len(g), "share_https": g.https.mean(),
                         "share_explicit_scheme": g.explicit_scheme.mean(), "share_www": g.www.mean(),
                         "share_ip_host": g.ip_host.mean(), "share_homepage": g.homepage.mean(),
                         "share_query": g.has_query.mean(), "median_len": float(g.url_len.median()),
                         "domains_per_url": df[df.label == lbl].group.nunique() / len(g)})
        if f.label.nunique() == 2:
            r = {"dataset": n, "label": -1, "n": len(f)}
            for c in ["https", "www", "homepage", "url_len", "ip_host", "has_query"]:
                r[f"auc_{c}"] = roc_auc_score(f.label, f[c])
            rows.append(r)
    out = pd.DataFrame(rows)
    (ROOT / "results/tables").mkdir(parents=True, exist_ok=True)
    out.to_csv(ROOT / "results/tables/dataset_artifact_stats.csv", index=False)
    print(out.round(3).to_string(index=False))
    # figure: https and www share by class per dataset
    two = out[out.label >= 0]
    sets = [n for n in NAMES if n in set(two.dataset) and two[two.dataset == n].label.nunique() == 2]
    fig, axes = plt.subplots(1, 3, figsize=(8.5, 2.8), sharey=True)
    for ax, col, title in zip(axes, ["share_https", "share_www", "share_homepage"],
                              ["https scheme", "leading www.", "homepage (empty path)"]):
        x = np.arange(len(sets)); w = 0.38
        b = [two[(two.dataset == s) & (two.label == 0)][col].iloc[0] * 100 for s in sets]
        m = [two[(two.dataset == s) & (two.label == 1)][col].iloc[0] * 100 for s in sets]
        ax.bar(x - w / 2, b, w, label="benign", color="#4C72B0"); ax.bar(x + w / 2, m, w, label="malicious", color="#C44E52")
        ax.set_xticks(x); ax.set_xticklabels(sets, rotation=35, ha="right", fontsize=7); ax.set_title(title, loc="left", fontsize=9)
    axes[0].set_ylabel("% of URLs"); axes[0].legend(fontsize=7)
    (ROOT / "results/figures").mkdir(parents=True, exist_ok=True)
    fig.savefig(ROOT / "results/figures/dataset_artifacts.png", dpi=300, bbox_inches="tight")
    fig.savefig(ROOT / "results/figures/dataset_artifacts.pdf", bbox_inches="tight")


if __name__ == "__main__":
    main()
