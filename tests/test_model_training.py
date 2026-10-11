"""End-to-end smoke test of the runner on a tiny synthetic dataset."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.urlresearch.experiments import runner  # noqa: E402
from src.urlresearch.models.charcnn import CharCNNClassifier, CharCNNConfig, encode_urls  # noqa: E402


def _synthetic(n=600, seed=0):
    rng = np.random.default_rng(seed)
    rows = []
    for i in range(n):
        if i % 2:
            url = f"http://{rng.integers(1,255)}.{rng.integers(1,255)}.{rng.integers(1,255)}.{rng.integers(1,255)}/login/verify{rng.integers(0,99)}.php"
            lbl, grp = 1, url.split("/")[2]
        else:
            d = f"site{rng.integers(0, 80)}"
            url = f"https://www.{d}.org/page{rng.integers(0,999)}.html"
            lbl, grp = 0, f"{d}.org"
        rows.append({"url": url, "label": lbl, "group": grp, "source": "synth",
                     "timestamp": pd.Timestamp("2024-01-01") + pd.Timedelta(days=int(rng.integers(0, 300)))})
    return pd.DataFrame(rows)


@pytest.fixture
def canonical(tmp_path, monkeypatch):
    monkeypatch.setattr(runner, "REPO", tmp_path)
    (tmp_path / "data/processed/canonical").mkdir(parents=True)
    _synthetic().to_parquet(tmp_path / "data/processed/canonical/synth.parquet")
    return tmp_path


@pytest.mark.parametrize("split", ["random", "grouped", "temporal"])
def test_runner_end_to_end(canonical, split):
    cfg = runner.RunConfig(run_id=f"smoke_{split}", dataset="synth", feature_set="lexical_v2",
                           split=split, models=["lr", "xgb"], seeds=[1],
                           model_params={"xgb": {"n_estimators": 20}})
    df = runner.run(cfg, canonical / "results")
    out = canonical / "results" / f"smoke_{split}"
    assert (out / "metrics.csv").exists() and (out / "split_1.json").exists()
    test_rows = df[(df.eval_set == "test") & (df.policy == "t0.5")]
    assert set(test_rows.model) == {"lr", "xgb"}
    assert (test_rows.roc_auc > 0.9).all()
    # thresholds chosen on validation must appear as policies
    assert {"val_maxf1", "val_fpr0.01"} <= set(df.policy)


def test_runner_baseline28_with_categorical(canonical):
    cfg = runner.RunConfig(run_id="smoke_b28", dataset="synth", feature_set="baseline28",
                           split="random", models=["rf"], seeds=[2], model_params={"rf": {"n_estimators": 10}})
    df = runner.run(cfg, canonical / "results")
    assert (df[(df.eval_set == "test") & (df.policy == "t0.5")].roc_auc > 0.9).all()


def test_charcnn_trains_and_predicts():
    df = _synthetic(300)
    cfg = CharCNNConfig(epochs=2, batch_size=64, filters=16, dense=16, threads=2)
    clf = CharCNNClassifier(cfg).fit(df.url.values[:200], df.label.values[:200], df.url.values[200:], df.label.values[200:])
    p = clf.predict_proba(df.url.values[200:])
    assert p.shape == (100, 2) and np.allclose(p.sum(1), 1)
    assert encode_urls(["ab"], 5).tolist() == [[97, 98, 0, 0, 0]]
    from sklearn.metrics import roc_auc_score
    assert roc_auc_score(df.label.values[200:], p[:, 1]) > 0.8


def test_runner_charcnn_canon(canonical):
    cfg = runner.RunConfig(run_id="smoke_canon", dataset="synth", feature_set="lexical_v2", split="grouped",
                           models=["charcnn_canon", "charcnn"], seeds=[1], external_tests=["synth"],
                           charcnn={"epochs": 1, "batch_size": 64, "filters": 8, "dense": 8, "threads": 2})
    df = runner.run(cfg, canonical / "results")
    assert {"charcnn_canon", "charcnn"} <= set(df.model)
