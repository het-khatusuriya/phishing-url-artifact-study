"""Security-oriented classification metrics, uncertainty and calibration.

Positive class = malicious (1). All functions take numpy arrays.
"""
from __future__ import annotations

from typing import Dict, Optional, Tuple

import numpy as np
from scipy import stats
from sklearn.metrics import (average_precision_score, brier_score_loss,
                             confusion_matrix, log_loss, roc_auc_score, roc_curve)


def classification_metrics(y_true: np.ndarray, y_prob: np.ndarray, threshold: float = 0.5) -> Dict[str, float]:
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    y_pred = (y_prob >= threshold).astype(int)
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[0, 1]).ravel()
    eps = 1e-12
    precision = tp / max(tp + fp, 1)
    recall = tp / max(tp + fn, 1)
    specificity = tn / max(tn + fp, 1)
    f1 = 2 * precision * recall / max(precision + recall, eps)
    out = {
        "threshold": float(threshold),
        "n": int(len(y_true)), "tp": int(tp), "fp": int(fp), "fn": int(fn), "tn": int(tn),
        "accuracy": (tp + tn) / max(len(y_true), 1),
        "precision": precision, "recall": recall, "specificity": specificity,
        "f1": f1, "fpr": fp / max(fp + tn, 1), "fnr": fn / max(fn + tp, 1),
        "balanced_accuracy": 0.5 * (recall + specificity),
        "mcc": _mcc(tp, fp, fn, tn),
    }
    if len(np.unique(y_true)) == 2:
        out["roc_auc"] = float(roc_auc_score(y_true, y_prob))
        out["pr_auc"] = float(average_precision_score(y_true, y_prob))
        out["log_loss"] = float(log_loss(y_true, np.clip(y_prob, 1e-7, 1 - 1e-7)))
        out["brier"] = float(brier_score_loss(y_true, y_prob))
        out["ece"] = expected_calibration_error(y_true, y_prob)
        for target in (0.01, 0.001):
            out[f"tpr_at_fpr_{target}"] = tpr_at_fpr(y_true, y_prob, target)
    return {k: (float(v) if isinstance(v, (np.floating, float)) else v) for k, v in out.items()}


def _mcc(tp, fp, fn, tn) -> float:
    num = tp * tn - fp * fn
    den = np.sqrt(float(tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
    return float(num / den) if den > 0 else 0.0


def tpr_at_fpr(y_true, y_prob, target_fpr: float) -> float:
    fpr, tpr, _ = roc_curve(y_true, y_prob)
    ok = fpr <= target_fpr
    return float(tpr[ok].max()) if ok.any() else 0.0


def threshold_at_fpr(y_true, y_prob, target_fpr: float) -> float:
    """Largest-recall threshold whose FPR on (y_true,y_prob) is <= target."""
    fpr, _, thr = roc_curve(y_true, y_prob)
    ok = np.where(fpr <= target_fpr)[0]
    if len(ok) == 0:
        return 1.0
    t = thr[ok[-1]]
    return float(min(max(t, 0.0), 1.0))


def threshold_max_f1(y_true, y_prob) -> float:
    from sklearn.metrics import precision_recall_curve
    p, r, t = precision_recall_curve(y_true, y_prob)
    f1 = 2 * p[:-1] * r[:-1] / np.clip(p[:-1] + r[:-1], 1e-12, None)
    return float(t[int(np.argmax(f1))])


def expected_calibration_error(y_true, y_prob, n_bins: int = 15) -> float:
    y_true = np.asarray(y_true, dtype=float)
    y_prob = np.asarray(y_prob, dtype=float)
    bins = np.linspace(0, 1, n_bins + 1)
    idx = np.clip(np.digitize(y_prob, bins) - 1, 0, n_bins - 1)
    ece = 0.0
    for b in range(n_bins):
        m = idx == b
        if m.any():
            ece += m.mean() * abs(y_true[m].mean() - y_prob[m].mean())
    return float(ece)


def reliability_table(y_true, y_prob, n_bins: int = 15):
    y_true = np.asarray(y_true, dtype=float)
    y_prob = np.asarray(y_prob, dtype=float)
    bins = np.linspace(0, 1, n_bins + 1)
    idx = np.clip(np.digitize(y_prob, bins) - 1, 0, n_bins - 1)
    rows = []
    for b in range(n_bins):
        m = idx == b
        rows.append({"bin_lo": bins[b], "bin_hi": bins[b + 1], "count": int(m.sum()),
                     "mean_pred": float(y_prob[m].mean()) if m.any() else np.nan,
                     "frac_pos": float(y_true[m].mean()) if m.any() else np.nan})
    return rows


def bootstrap_ci(y_true, y_prob, metric_fn, n_boot: int = 1000, seed: int = 0,
                 alpha: float = 0.05) -> Tuple[float, float, float]:
    """Percentile bootstrap CI of a metric over test examples."""
    rng = np.random.default_rng(seed)
    y_true = np.asarray(y_true); y_prob = np.asarray(y_prob)
    n = len(y_true)
    point = metric_fn(y_true, y_prob)
    vals = []
    for _ in range(n_boot):
        i = rng.integers(0, n, n)
        if len(np.unique(y_true[i])) < 2:
            continue
        vals.append(metric_fn(y_true[i], y_prob[i]))
    lo, hi = np.percentile(vals, [100 * alpha / 2, 100 * (1 - alpha / 2)])
    return float(point), float(lo), float(hi)


def paired_bootstrap_delta(y_true, prob_a, prob_b, metric_fn, n_boot: int = 1000, seed: int = 0):
    """Paired bootstrap of metric(A) - metric(B) on identical test examples."""
    rng = np.random.default_rng(seed)
    y_true = np.asarray(y_true); prob_a = np.asarray(prob_a); prob_b = np.asarray(prob_b)
    n = len(y_true)
    deltas = []
    for _ in range(n_boot):
        i = rng.integers(0, n, n)
        if len(np.unique(y_true[i])) < 2:
            continue
        deltas.append(metric_fn(y_true[i], prob_a[i]) - metric_fn(y_true[i], prob_b[i]))
    deltas = np.asarray(deltas)
    point = metric_fn(y_true, prob_a) - metric_fn(y_true, prob_b)
    lo, hi = np.percentile(deltas, [2.5, 97.5])
    p_two_sided = 2 * min((deltas <= 0).mean(), (deltas >= 0).mean())
    return {"delta": float(point), "ci_lo": float(lo), "ci_hi": float(hi), "p_boot": float(min(1.0, p_two_sided))}


def mcnemar_test(y_true, pred_a, pred_b) -> Dict[str, float]:
    """Exact/mid-p McNemar test on paired correctness (discordant pairs)."""
    y_true = np.asarray(y_true); a = np.asarray(pred_a) == y_true; b = np.asarray(pred_b) == y_true
    n01 = int((a & ~b).sum()); n10 = int((~a & b).sum())
    n = n01 + n10
    if n == 0:
        return {"n01": n01, "n10": n10, "p_value": 1.0}
    k = min(n01, n10)
    p = min(1.0, 2 * stats.binom.cdf(k, n, 0.5))
    return {"n01": n01, "n10": n10, "p_value": float(p)}


def metric_fn(name: str):
    from sklearn.metrics import f1_score
    if name == "roc_auc":
        return lambda y, p: roc_auc_score(y, p)
    if name == "pr_auc":
        return lambda y, p: average_precision_score(y, p)
    if name == "f1":
        return lambda y, p: f1_score(y, (p >= 0.5).astype(int))
    if name.startswith("tpr_at_fpr_"):
        t = float(name.split("_")[-1])
        return lambda y, p: tpr_at_fpr(y, p, t)
    raise KeyError(name)
