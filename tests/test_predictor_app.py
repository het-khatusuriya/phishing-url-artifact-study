import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tests"))

from test_model_training import _synthetic  # noqa: E402
from src.urlresearch.features.lexical import feature_frame  # noqa: E402
from src.urlresearch.models.tabular import logistic_regression  # noqa: E402
from src.urlresearch.prediction.predictor import URLPredictor, save_bundle  # noqa: E402


def _bundle(tmp_path):
    df = _synthetic(400)
    X = feature_frame(df.url, "lexical_v2", drop_artifacts=True)
    clf = logistic_regression(list(X.columns)).fit(X, df.label)
    path = tmp_path / "b.joblib"
    save_bundle(path, clf, "lexical_v2", X.columns, {"t0.5": 0.5, "val_fpr0.01": 0.7}, drop_artifacts=True,
                meta={"name": "test"})
    return path


def test_predictor_schema_and_statement(tmp_path):
    pred = URLPredictor(_bundle(tmp_path))
    out = pred.predict(["http://1.2.3.4/login/verify1.php", "https://www.site3.org/page1.html", "garbage", ""])
    assert len(out) == 4
    for r in out:
        assert 0 <= r["p_malicious"] <= 1 and r["policy"] == "val_fpr0.01" and r["threshold"] == 0.7
        assert "safe" not in r["statement"].lower().replace("not a guarantee of safety", "")
    assert out[0]["flagged"] is True and out[1]["flagged"] is False


def test_flask_api(tmp_path, monkeypatch):
    monkeypatch.setenv("URL_MODEL_BUNDLE", str(_bundle(tmp_path)))
    import importlib
    import app as app_module
    importlib.reload(app_module)
    client = app_module.app.test_client()
    r = client.get("/api/health").get_json()
    assert r["model_loaded"] is True
    r = client.post("/api/predict", json={"url": "http://1.2.3.4/login/verify1.php"})
    assert r.status_code == 200 and r.get_json()["flagged"] is True
    assert client.post("/api/predict", json={}).status_code == 400
    assert client.post("/api/predict", json={"url": "x", "policy": "nope"}).status_code == 400
    assert client.post("/api/predict", json={"url": "a" * 5000}).status_code == 400
    assert client.get("/").status_code == 200
