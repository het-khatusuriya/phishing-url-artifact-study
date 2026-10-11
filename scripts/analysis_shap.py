"""SHAP analysis with TreeExplainer on a refitted XGBoost model for a given run.

Usage: python scripts/analysis_shap.py --run lexical_v2_grouped --model xgb --seed 42 --n 3000
Refits the model on the run's training split (same config), explains `n`
test URLs, and writes results/tables/shap_<run>_<model>.csv and
results/figures/shap_<run>_<model>.{png,pdf}.
"""
import argparse
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shap

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.urlresearch.experiments.runner import RunConfig, load_canonical, _features, REPO  # noqa: E402
from src.urlresearch.features.lexical import FEATURE_SETS  # noqa: E402
from src.urlresearch.models.tabular import MODEL_FACTORIES  # noqa: E402
from src.urlresearch.data.splits import load_split  # noqa: E402


def main(run, model, seed, n):
    cfg = RunConfig(**json.loads((REPO / "results/runs" / run / "config.json").read_text()))
    df = load_canonical(cfg.dataset, cfg.max_rows)
    X = _features(df, cfg, REPO / "data/processed/feature_cache")
    spec = FEATURE_SETS[cfg.feature_set]
    categorical = [c for c in spec["categorical"] if c in X.columns]
    numeric = [c for c in X.columns if c not in categorical]
    split = load_split(REPO / "results/runs" / run / f"split_{seed}.json")
    y = df.label.values
    clf = MODEL_FACTORIES[model](numeric, categorical, seed=seed, **cfg.model_params.get(model, {}))
    clf.fit(X.iloc[split["train"]], y[split["train"]])
    prep, est = clf.named_steps["prep"], clf.named_steps["model"]
    rng = np.random.default_rng(seed)
    te = rng.choice(split["test"], size=min(n, len(split["test"])), replace=False)
    Xt = prep.transform(X.iloc[te])
    names = list(prep.get_feature_names_out())
    expl = shap.TreeExplainer(est)
    sv = expl.shap_values(Xt)
    if isinstance(sv, list):
        sv = sv[1]
    imp = pd.DataFrame({"feature": names, "mean_abs_shap": np.abs(sv).mean(0),
                        "mean_shap": sv.mean(0)}).sort_values("mean_abs_shap", ascending=False)
    (ROOT / "results/tables").mkdir(parents=True, exist_ok=True)
    imp.to_csv(ROOT / "results/tables" / f"shap_{run}_{model}.csv", index=False)
    fig, ax = plt.subplots(figsize=(4.2, 4.6))
    top = imp.head(20).iloc[::-1]
    ax.barh(top.feature, top.mean_abs_shap, color="#4C72B0")
    ax.set_xlabel("mean |SHAP value| (log-odds, malicious class)")
    ax.set_title(f"{run} · {model} · n={len(te)}", loc="left", fontsize=8)
    (ROOT / "results/figures").mkdir(parents=True, exist_ok=True)
    fig.savefig(ROOT / "results/figures" / f"shap_{run}_{model}.png", dpi=300, bbox_inches="tight")
    fig.savefig(ROOT / "results/figures" / f"shap_{run}_{model}.pdf", bbox_inches="tight")
    # beeswarm
    plt.figure(figsize=(5, 5))
    shap.summary_plot(sv, Xt, feature_names=names, max_display=20, show=False)
    plt.savefig(ROOT / "results/figures" / f"shap_beeswarm_{run}_{model}.png", dpi=300, bbox_inches="tight")
    print(imp.head(15).to_string(index=False))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True); ap.add_argument("--model", default="xgb")
    ap.add_argument("--seed", type=int, default=42); ap.add_argument("--n", type=int, default=3000)
    a = ap.parse_args(); main(a.run, a.model, a.seed, a.n)
