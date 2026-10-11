"""Flask demo for the research model bundle.

Run:  set URL_MODEL_BUNDLE=models/<name>.joblib && python app.py
The API returns a model estimate with an operating threshold and an
uncertainty band. It never states that a URL is safe.
"""
import os
import sys
from pathlib import Path

from flask import Flask, jsonify, request

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from src.urlresearch.prediction.predictor import URLPredictor  # noqa: E402

app = Flask(__name__)
BUNDLE = os.environ.get("URL_MODEL_BUNDLE")
if not BUNDLE:
    cands = sorted((ROOT / "models").glob("*.joblib")) if (ROOT / "models").exists() else []
    BUNDLE = str(cands[0]) if cands else None
predictor = URLPredictor(BUNDLE) if BUNDLE and Path(BUNDLE).exists() else None
MAX_URL_LEN = 4096


@app.route("/")
def home():
    page = ROOT / "index.html"
    if not page.exists():
        page = ROOT / "idex.html"  # original filename in the repository
    return page.read_text(encoding="utf-8")


@app.route("/api/health")
def health():
    return jsonify({"model_loaded": predictor is not None, "bundle": BUNDLE,
                    "model": predictor.meta.get("name") if predictor else None})


@app.route("/api/predict", methods=["POST"])
def predict_url():
    if predictor is None:
        return jsonify({"error": "no model bundle loaded; train one with scripts/train_final_model.py"}), 503
    body = request.get_json(silent=True) or {}
    url = body.get("url")
    policy = body.get("policy", "val_fpr0.01")
    if not isinstance(url, str) or not url.strip():
        return jsonify({"error": "field 'url' (non-empty string) is required"}), 400
    if len(url) > MAX_URL_LEN:
        return jsonify({"error": f"url longer than {MAX_URL_LEN} characters"}), 400
    if policy not in predictor.thresholds:
        return jsonify({"error": f"unknown policy; choose from {sorted(predictor.thresholds)}"}), 400
    result = predictor.predict([url.strip()], policy=policy)[0]
    # backward-compatible fields for the bundled page
    result["prediction"] = "Flagged (likely malicious)" if result["flagged"] else "Not flagged (model estimate, not a safety guarantee)"
    result["confidence"] = round(100 * result["p_malicious"], 2)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=5000)
