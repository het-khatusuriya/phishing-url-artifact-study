"""Dataset-identification probe: can lexical features tell which corpus a URL
came from, within the same class?  High accuracy means corpus markers are
learnable, i.e. a model may key on collection artifacts.

Usage: python scripts/analysis_dataset_probe.py [--feature-set lexical_v2] [--n-per 8000]
Writes results/tables/dataset_probe_<feature_set>.csv
"""
import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import GroupKFold, cross_val_predict
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.urlresearch.features.lexical import FEATURE_SETS, feature_frame  # noqa: E402

CAN = ROOT / "data/processed/canonical"
CORPORA = ["phiusiil", "lineage253k", "hannousse2021", "ebbu2017", "phishstorm", "iscx2016"]


def main(feature_set, n_per, drop_artifacts):
    rows = []
    for lbl in (0, 1):
        frames = []
        for c in CORPORA:
            df = pd.read_parquet(CAN / f"{c}.parquet")
            d = df[df.label == lbl]
            d = d.sample(min(n_per, len(d)), random_state=0)
            frames.append(d.assign(corpus=c))
        d = pd.concat(frames, ignore_index=True)
        X = feature_frame(d.url, feature_set, drop_artifacts=drop_artifacts)
        X = X.drop(columns=[c for c in FEATURE_SETS[feature_set]["categorical"] if c in X.columns])
        clf = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000, multi_class="auto"))
        pred = cross_val_predict(clf, X.values, d.corpus.values, groups=d.group.values, cv=GroupKFold(5))
        acc = accuracy_score(d.corpus, pred)
        cm = confusion_matrix(d.corpus, pred, labels=CORPORA)
        per = {c: cm[i, i] / cm[i].sum() for i, c in enumerate(CORPORA)}
        rows.append({"class": "benign" if lbl == 0 else "malicious", "feature_set": feature_set,
                     "drop_artifacts": drop_artifacts, "n": len(d), "chance": 1 / len(CORPORA), "accuracy": acc, **per})
        print(rows[-1])
    out = pd.DataFrame(rows)
    (ROOT / "results/tables").mkdir(parents=True, exist_ok=True)
    out.to_csv(ROOT / "results/tables" / f"dataset_probe_{feature_set}{'_noart' if drop_artifacts else ''}.csv", index=False)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--feature-set", default="lexical_v2"); ap.add_argument("--n-per", type=int, default=8000)
    ap.add_argument("--drop-artifacts", action="store_true")
    a = ap.parse_args(); main(a.feature_set, a.n_per, a.drop_artifacts)
