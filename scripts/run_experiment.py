"""CLI: python scripts/run_experiment.py configs/<name>.yaml [--max-rows N] [--out DIR]"""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.urlresearch.experiments.runner import RunConfig, run  # noqa: E402

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("config")
    ap.add_argument("--max-rows", type=int, default=None)
    ap.add_argument("--out", type=str, default=None)
    ap.add_argument("--run-id", type=str, default=None)
    a = ap.parse_args()
    cfg = RunConfig.from_yaml(a.config)
    if a.max_rows:
        cfg.max_rows = a.max_rows
    if a.run_id:
        cfg.run_id = a.run_id
    df = run(cfg, Path(a.out) if a.out else None)
    cols = ["model", "seed", "eval_set", "policy", "roc_auc", "pr_auc", "f1", "recall", "fpr", "tpr_at_fpr_0.01"]
    print(df[df["policy"] == "t0.5"][cols].to_string(index=False))
