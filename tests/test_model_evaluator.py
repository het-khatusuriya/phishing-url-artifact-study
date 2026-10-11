import sys
from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.urlresearch.evaluation.metrics import (bootstrap_ci, classification_metrics,  # noqa: E402
                                                expected_calibration_error, mcnemar_test,
                                                paired_bootstrap_delta, threshold_at_fpr,
                                                tpr_at_fpr, metric_fn)


def test_classification_metrics_counts():
    y = np.array([1, 1, 1, 0, 0, 0, 0, 1])
    p = np.array([0.9, 0.8, 0.2, 0.1, 0.6, 0.3, 0.05, 0.55])
    m = classification_metrics(y, p, 0.5)
    assert (m["tp"], m["fp"], m["fn"], m["tn"]) == (3, 1, 1, 3)
    assert m["precision"] == pytest.approx(0.75) and m["recall"] == pytest.approx(0.75)
    assert m["fpr"] == pytest.approx(0.25) and m["fnr"] == pytest.approx(0.25)
    assert m["specificity"] == pytest.approx(0.75) and 0 <= m["roc_auc"] <= 1
    assert "pr_auc" in m and "ece" in m and "tpr_at_fpr_0.01" in m


def test_perfect_and_calibration():
    y = np.array([0] * 50 + [1] * 50)
    p = np.array([0.0] * 50 + [1.0] * 50)
    m = classification_metrics(y, p)
    assert m["roc_auc"] == 1.0 and m["f1"] == 1.0 and m["ece"] == pytest.approx(0.0)
    assert expected_calibration_error(y, np.full(100, 0.5)) == pytest.approx(0.0)
    assert expected_calibration_error(y, np.full(100, 0.9)) == pytest.approx(0.4)


def test_threshold_at_fpr():
    rng = np.random.default_rng(0)
    y = np.r_[np.zeros(1000), np.ones(1000)]
    p = np.r_[rng.beta(2, 5, 1000), rng.beta(5, 2, 1000)]
    t = threshold_at_fpr(y, p, 0.01)
    fpr = ((p[y == 0] >= t).mean())
    assert fpr <= 0.01 + 1e-9
    assert tpr_at_fpr(y, p, 0.01) == pytest.approx((p[y == 1] >= t).mean(), abs=0.01)


def test_bootstrap_and_paired():
    rng = np.random.default_rng(1)
    y = rng.integers(0, 2, 500)
    pa = np.clip(y * 0.6 + rng.normal(0, 0.3, 500), 0, 1)
    pb = np.clip(y * 0.3 + rng.normal(0, 0.3, 500), 0, 1)
    pt, lo, hi = bootstrap_ci(y, pa, metric_fn("roc_auc"), n_boot=200)
    assert lo <= pt <= hi
    d = paired_bootstrap_delta(y, pa, pb, metric_fn("roc_auc"), n_boot=200)
    assert d["delta"] > 0 and d["ci_lo"] > 0 and d["p_boot"] < 0.05
    mc = mcnemar_test(y, (pa >= 0.5).astype(int), (pb >= 0.5).astype(int))
    assert mc["p_value"] < 0.05
