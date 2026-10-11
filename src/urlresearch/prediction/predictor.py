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
            margin = abs(p - thr)
            band = "low" if margin < 0.1 else ("medium" if margin < 0.3 else "high")
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


def save_bundle(path, pipeline, feature_set, columns, thresholds, drop_artifacts=False,
                calibrator=None, meta: Optional[Dict] = None) -> None:
    joblib.dump({"pipeline": pipeline, "feature_set": feature_set, "columns": list(columns),
                 "thresholds": thresholds, "drop_artifacts": drop_artifacts, "calibrator": calibrator,
                 "meta": meta or {}}, path)
