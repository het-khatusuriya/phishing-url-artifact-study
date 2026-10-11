"""Build canonical parquet datasets from a spec file.

Usage: python scripts/build_canonical.py configs/datasets.yaml [--only NAME]

Spec format (YAML):
  datasets:
    - name: main
      path: data/raw/raw_data.csv
      url_col: url
      label_col: label
      timestamp_col: null
      label_map: {legitimate: 0, phishing: 1}    # optional
      source: original_repo
    - name: combined_x        # concatenation of other canonical sets
      concat: [a, b]
Outputs: data/processed/canonical/<name>.parquet and results/logs/dataset_report_<name>.json
"""
import argparse
import sys
from pathlib import Path

import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.urlresearch.data.dataset import concat_datasets, load_dataset  # noqa: E402

OUT = ROOT / "data" / "processed" / "canonical"
LOGS = ROOT / "results" / "logs"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec")
    ap.add_argument("--only", default=None)
    a = ap.parse_args()
    spec = yaml.safe_load(Path(a.spec).read_text())
    OUT.mkdir(parents=True, exist_ok=True)
    for d in spec["datasets"]:
        if a.only and d["name"] != a.only:
            continue
        if "concat" in d:
            frames = []
            for n in d["concat"]:
                f = pd.read_parquet(OUT / f"{n}.parquet")
                cap = d.get("cap_per_source")
                if cap and len(f) > cap:   # stratified cap, deterministic
                    f = (f.groupby("label", group_keys=False)
                          .apply(lambda g: g.sample(min(len(g), int(round(cap * len(g) / len(f)))), random_state=42)))
                frames.append(f)
            df = concat_datasets(frames)
            df.to_parquet(OUT / f"{d['name']}.parquet")
            print(f"{d['name']}: concat of {d['concat']} -> {len(df)} rows, pos={int(df.label.sum())}")
            continue
        lm = d.get("label_map")
        if lm:
            lm = {str(k).lower(): int(v) for k, v in lm.items()}
        df, rep = load_dataset(ROOT / d["path"], d["name"], d.get("url_col", "url"), d.get("label_col", "label"),
                               d.get("timestamp_col"), d.get("source"), lm, report_dir=LOGS)
        df.to_parquet(OUT / f"{d['name']}.parquet")
        print(f"{d['name']}: raw={rep.rows_raw} kept={rep.rows_after_normalisation_dedup} pos={rep.positives} "
              f"neg={rep.negatives} domains={rep.unique_registered_domains} https={rep.share_https:.3f} "
              f"www={rep.share_www:.3f} ip={rep.share_ip_host:.3f} ts={rep.has_timestamps}")


if __name__ == "__main__":
    main()
