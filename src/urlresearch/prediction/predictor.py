"""Single-URL and batch prediction from a persisted model bundle.

A bundle (joblib) contains:
    pipeline        fitted sklearn Pipeline (preprocessing inside)
    feature_set     name in FEATURE_SETS
    drop_artifacts  bool
    columns         exact training column order
    thresholds      {policy: threshold} chosen on validation
    calibrator      optional fitted isotonic/Platt calibrator on validation
    meta            dataset, split, seed, metrics on validation, created, versions
The predictor never reports a URL as "safe": it returns a probability, an
operating decision under a named policy, and an uncertainty band.
"""
from __future__ import annotations

from pathlib import Path
from typing import Dict, Iterable, List, Optional

import joblib
import numpy as np
import pandas as pd

from ..features.lexical import FEATURE_SETS, feature_frame


class URLPredictor:
    def __init__(self, bundle_path: str | Path):
        b = joblib.load(bundle_path)
        self.pipeline = b["pipeline"]
        self.feature_set = b["feature_set"]
        self.drop_artifacts = b.get("drop_artifacts", False)
        self.columns: List[str] = list(b["columns"])
        self.thresholds: Dict[str, float] = b.get("thresholds", {"t0.5": 0.5})
        self.calibrator = b.get("calibrator")
        self.meta = b.get("meta", {})

    def _features(self, urls: Iterable[str]) -> pd.DataFrame:
        X = feature_frame(list(urls), self.feature_set, drop_artifacts=self.drop_artifacts)
        return X.reindex(columns=self.columns, fill_value=0)

    def predict_proba(self, urls: Iterable[str]) -> np.ndarray:
        X = self._features(urls)
        p = self.pipeline.predict_proba(X)[:, 1]
        if self.calibrator is not None:
            p = self.calibrator.predict(p) if hasattr(self.calibrator, "predict") else self.calibrator.predict_proba(p.reshape(-1, 1))[:, 1]
        return np.clip(p, 0, 1)

    def predict(self, urls: Iterable[str], policy: str = "val_fpr0.01") -> List[Dict]:
        urls = list(urls)
        probs = self.predict_proba(urls)
        thr = self.thresholds.get(policy, 0.5)
        out = []
        for u, p in zip(urls, probs):
            # distance from the threshold, scaled by the room available on that side (0 = at threshold, 1 = at 0 or 1)
            margin = (p - thr) / max(1 - thr, 1e-9) if p >= thr else (thr - p) / max(thr, 1e-9)
            band = "low" if margin < 1 / 3 else ("medium" if margin < 2 / 3 else "high")
            out.append({
                "url": u,
                "p_malicious": float(p),
                "policy": policy,
                "threshold": float(thr),
                "flagged": bool(p >= thr),
                "confidence_band": band,
                "statement": ("Flagged as likely malicious by the model." if p >= thr else
                              "Not flagged by the model at this operating point. This is NOT a guarantee of safety."),
                "model": self.meta.get("name", "unknown"),
            })
        return out


    # ------------------------------------------------------------------ explanations
    def _explainable_pipeline(self):
        """Return (pipeline, note) for a pipeline whose last step can be explained exactly."""
        pipe = self.pipeline
        if hasattr(pipe, "named_estimators_"):          # VotingClassifier: explain its XGBoost member
            for key in ("xgb", "lr"):
                if key in pipe.named_estimators_:
                    return pipe.named_estimators_[key], f"from the ensemble's {key.upper()} member"
            return None, "not available for this ensemble"
        return pipe, ""

    def explain(self, url: str, top_k: int = 8) -> Dict:
        """Per-feature contributions (log-odds of 'malicious') for one URL.

        XGBoost: exact TreeSHAP via the booster's pred_contribs.
        Logistic regression: coefficient x standardised value.
        Returns {"note": str, "rows": [(feature, value, contribution), ...]} sorted by |contribution|.
        """
        pipe, note = self._explainable_pipeline()
        if pipe is None or not hasattr(pipe, "named_steps"):
            return {"note": note or "not available for this model", "rows": []}
        prep, est = pipe.named_steps.get("prep"), pipe.named_steps.get("model")
        X = self._features([url])
        Xt = prep.transform(X) if prep is not None else X.values
        names = list(prep.get_feature_names_out()) if prep is not None else list(X.columns)
        if hasattr(est, "get_booster"):
            import xgboost as xgb
            contrib = est.get_booster().predict(xgb.DMatrix(np.asarray(Xt, dtype=float)), pred_contribs=True)[0, :-1]
        elif hasattr(est, "coef_"):
            contrib = np.asarray(Xt, dtype=float)[0] * est.coef_[0]
        else:
            return {"note": "not available for this model type", "rows": []}
        raw = X.reindex(columns=[n for n in names if n in X.columns]).iloc[0].to_dict()
        rows = [(n, raw.get(n, float(np.asarray(Xt)[0, i])), float(c)) for i, (n, c) in enumerate(zip(names, contrib))]
        rows.sort(key=lambda r: abs(r[2]), reverse=True)
        return {"note": note, "rows": rows[:top_k]}


def save_bundle(path, pipeline, feature_set, columns, thresholds, drop_artifacts=False,
                calibrator=None, meta: Optional[Dict] = None) -> None:
    joblib.dump({"pipeline": pipeline, "feature_set": feature_set, "columns": list(columns),
                 "thresholds": thresholds, "drop_artifacts": drop_artifacts, "calibrator": calibrator,
                 "meta": meta or {}}, path)
