"""Error analysis for a saved run: characterise FPs and FNs on the test split.

Usage: python scripts/analysis_errors.py --run lexical_v2_grouped --model xgb --seed 42 --policy val_fpr0.01
Writes results/tables/errors_<run>_<model>_<policy>.csv  (group-level error rates)
       results/tables/error_examples_<run>_<model>_<policy>.csv (50 FP + 50 FN URLs)
"""
import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.urlresearch.experiments.runner import RunConfig, load_canonical, REPO  # noqa: E402
from src.urlresearch.features.url_parse import parse_url  # noqa: E402
from src.urlresearch.features.lexical import FREE_HOSTING_SUFFIXES, ABUSED_SUFFIXES  # noqa: E402
from src.urlresearch.data.splits import load_split  # noqa: E402


def main(run, model, seed, policy):
    rd = REPO / "results/runs" / run
    cfg = RunConfig(**json.loads((rd / "config.json").read_text()))
    df = load_canonical(cfg.dataset, cfg.max_rows)
    split = load_split(rd / f"split_{seed}.json")
    preds = pd.read_csv(rd / f"predictions_{model}_{seed}.csv")
    te = preds[preds.split == "test"].set_index("idx")
    metrics = pd.read_csv(rd / "metrics.csv")
    thr = float(metrics[(metrics.model == model) & (metrics.seed == seed) & (metrics.policy == policy)
                        & (metrics.eval_set == "test")].threshold.iloc[0])
    d = df.loc[te.index].copy()
    d["prob"] = te.prob.values; d["pred"] = (d.prob >= thr).astype(int)
    train_groups = set(df.loc[split["train"], "group"])
    P = d.url.map(parse_url)
    d["domain_seen_in_train"] = d.group.isin(train_groups)
    d["is_ip"] = P.map(lambda p: p.is_ip)
    d["https"] = P.map(lambda p: p.scheme == "https")
    d["www"] = P.map(lambda p: bool(p.labels) and p.labels[0].startswith("www"))
    d["has_query"] = P.map(lambda p: bool(p.query))
    d["percent_encoded"] = d.url.str.contains("%", regex=False)
    d["punycode"] = d.url.str.contains("xn--", regex=False)
    d["free_hosting"] = P.map(lambda p: any(p.hostname == s or p.hostname.endswith("." + s) for s in FREE_HOSTING_SUFFIXES))
    d["abused_suffix"] = P.map(lambda p: bool(p.suffix) and p.suffix.split(".")[-1] in ABUSED_SUFFIXES)
    d["len_bucket"] = pd.cut(d.url.str.len(), [0, 30, 50, 75, 100, 150, 10 ** 6],
                             labels=["<=30", "31-50", "51-75", "76-100", "101-150", ">150"])
    d["depth_bucket"] = pd.cut(P.map(lambda p: len([s for s in p.path.split("/") if s])), [-1, 0, 1, 2, 4, 100],
                               labels=["0", "1", "2", "3-4", ">=5"])
    rows = []
    for col in ["domain_seen_in_train", "is_ip", "https", "www", "has_query", "percent_encoded", "punycode",
                "free_hosting", "abused_suffix", "len_bucket", "depth_bucket"]:
        for val, g in d.groupby(col, observed=True):
            neg, pos = g[g.label == 0], g[g.label == 1]
            rows.append({"run_id": run, "model": model, "policy": policy, "threshold": thr, "factor": col,
                         "value": str(val), "n": len(g), "n_benign": len(neg), "n_malicious": len(pos),
                         "fpr": float((neg.pred == 1).mean()) if len(neg) else np.nan,
                         "fnr": float((pos.pred == 0).mean()) if len(pos) else np.nan,
                         "share_of_all_fp": float((neg.pred == 1).sum() / max((d[d.label == 0].pred == 1).sum(), 1)),
                         "share_of_all_fn": float((pos.pred == 0).sum() / max((d[d.label == 1].pred == 0).sum(), 1))})
    out = ROOT / "results/tables"; out.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(out / f"errors_{run}_{model}_{policy}.csv", index=False)
    fp = d[(d.label == 0) & (d.pred == 1)].sort_values("prob", ascending=False).head(50)
    fn = d[(d.label == 1) & (d.pred == 0)].sort_values("prob").head(50)
    ex = pd.concat([fp.assign(kind="FP"), fn.assign(kind="FN")])[["kind", "url", "label", "prob", "group", "domain_seen_in_train", "source"]]
    ex.to_csv(out / f"error_examples_{run}_{model}_{policy}.csv", index=False)
    print(pd.DataFrame(rows)[["factor", "value", "n", "fpr", "fnr"]].to_string(index=False))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True); ap.add_argument("--model", default="xgb")
    ap.add_argument("--seed", type=int, default=42); ap.add_argument("--policy", default="val_fpr0.01")
    a = ap.parse_args(); main(a.run, a.model, a.seed, a.policy)
