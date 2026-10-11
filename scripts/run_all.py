"""Run every config listed in configs/matrix/RUN_ORDER.txt sequentially, skipping
runs whose metrics.csv already contains every (model, seed) pair. Logs to
results/logs/run_all.log. Safe to re-launch after an interruption.
"""
import subprocess
import sys
import time
from pathlib import Path

import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
ORDER = ROOT / "configs" / "matrix" / "RUN_ORDER.txt"
LOG = ROOT / "results" / "logs" / "run_all.log"
LOG.parent.mkdir(parents=True, exist_ok=True)


def complete(run_id):
    cfg = yaml.safe_load((ROOT / "configs" / "matrix" / f"{run_id}.yaml").read_text())
    m = ROOT / "results" / "runs" / run_id / "metrics.csv"
    if not m.exists():
        return False
    df = pd.read_csv(m)
    have = set(zip(df.model, df.seed))
    return all((mo, s) in have for mo in cfg["models"] for s in cfg["seeds"])


def main(only=None):
    runs = [r.strip() for r in ORDER.read_text().splitlines() if r.strip()]
    if only:
        runs = [r for r in runs if r in only]
    with open(LOG, "a", encoding="utf-8") as log:
        for r in runs:
            if complete(r):
                log.write(f"{time.strftime('%F %T')} SKIP {r} (complete)\n"); log.flush(); continue
            log.write(f"{time.strftime('%F %T')} START {r}\n"); log.flush()
            t0 = time.time()
            rc = subprocess.call([sys.executable, str(ROOT / "scripts" / "run_experiment.py"),
                                  str(ROOT / "configs" / "matrix" / f"{r}.yaml")],
                                 stdout=log, stderr=subprocess.STDOUT, cwd=str(ROOT))
            log.write(f"{time.strftime('%F %T')} END {r} rc={rc} {time.time() - t0:.0f}s\n"); log.flush()


if __name__ == "__main__":
    main(sys.argv[1:] or None)
