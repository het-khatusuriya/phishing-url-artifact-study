"""Smoke test for the Tkinter GUI: build the window, load a tiny model, check a URL,
run the variant test. Skipped automatically when no display is available."""
import sys
import time
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tests"))

tk = pytest.importorskip("tkinter")


def _tiny_bundle(tmp_path):
    from test_model_training import _synthetic
    from src.urlresearch.features.lexical import feature_frame
    from src.urlresearch.models.tabular import xgboost
    from src.urlresearch.prediction.predictor import save_bundle
    df = _synthetic(400)
    X = feature_frame(df.url, "lexical_v2_canon")
    clf = xgboost(list(X.columns), n_estimators=20).fit(X, df.label)
    path = tmp_path / "tiny.joblib"
    save_bundle(path, clf, "lexical_v2_canon", X.columns, {"t0.5": 0.5, "val_fpr0.01": 0.6}, meta={"name": "tiny"})
    return path


def _wait(app, cond, timeout=30):
    t0 = time.time()
    while not cond() and time.time() - t0 < timeout:
        app.update()
        time.sleep(0.05)


def test_gui_check_and_variants(tmp_path, monkeypatch):
    import url_checker_gui as G
    from src.urlresearch.prediction.predictor import URLPredictor
    monkeypatch.setattr(G.App, "_load_default_models", lambda self: {})
    monkeypatch.setattr(G.messagebox, "showwarning", lambda *a, **k: None)
    try:
        app = G.App()
    except tk.TclError:
        pytest.skip("no display available")
    app.withdraw()
    try:
        _wait(app, lambda: app.status.get() != "Loading models…")
        app._on_models_loaded({"tiny": URLPredictor(_tiny_bundle(tmp_path))})
        assert app.model_var.get() == "tiny"
        app.url_var.set("http://1.2.3.4/login/verify1.php")
        app._check()
        _wait(app, lambda: app.prob_txt.cget("text") != "—")
        assert app.prob_txt.cget("text").endswith("%")
        assert len(app.explain.get_children()) > 0 and len(app.components.get_children()) > 0
        app._variants()
        _wait(app, lambda: app.var_tree is not None)
        assert len(app.var_tree.get_children()) == 1 + len(G.MUTATIONS)
        # empty input is rejected without raising
        monkeypatch.setattr(G.messagebox, "showinfo", lambda *a, **k: None)
        app.url_var.set("")
        assert app._validated_url() is None
    finally:
        app.destroy()
