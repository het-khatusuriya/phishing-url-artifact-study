import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.urlresearch.data.dataset import load_dataset, map_label, normalise_url  # noqa: E402
from src.urlresearch.data.splits import (grouped_stratified_split, overlap_report,  # noqa: E402
                                         random_stratified_split, temporal_split,
                                         save_split, load_split)


def test_map_label():
    assert map_label("phishing") == 1 and map_label("Legitimate") == 0
    assert map_label("benign") == 0 and map_label("malware") == 1 and map_label("weird") is None


def test_normalise_url_for_dedup():
    assert normalise_url("HTTP://Example.COM/") == normalise_url("http://example.com")
    assert normalise_url("http://example.com/a#frag") == "http://example.com/a"
    assert normalise_url("http://example.com/A") != normalise_url("http://example.com/a")


def test_load_dataset_dedup_and_conflicts(tmp_path):
    csv = tmp_path / "d.csv"
    pd.DataFrame({
        "url": ["http://a.com/x", "HTTP://A.com/x", "http://b.com", "http://b.com", "http://c.com", " ", None],
        "label": ["phishing", "phishing", "phishing", "legitimate", "legitimate", "phishing", "phishing"],
    }).to_csv(csv, index=False)
    df, rep = load_dataset(csv, "toy")
    # a.com duplicates collapse; b.com conflicting -> removed; blank/None dropped
    assert set(df["url"]) == {"http://a.com/x", "http://c.com"}
    assert rep.conflicting_label_urls_removed == 1 and rep.rows_raw == 7
    assert set(df.columns) >= {"url", "label", "source", "timestamp", "group", "host"}
    assert df.loc[df["url"] == "http://a.com/x", "group"].iloc[0] == "a.com"


def _toy(n_groups=50, per_group=6, seed=0):
    rng = np.random.default_rng(seed)
    rows = []
    for g in range(n_groups):
        lbl = int(g % 2 == 0)
        for k in range(per_group):
            rows.append({"url": f"http://d{g}.com/p{k}", "label": lbl, "group": f"d{g}.com",
                         "timestamp": pd.Timestamp("2024-01-01") + pd.Timedelta(days=int(rng.integers(0, 365)))})
    return pd.DataFrame(rows)


def test_random_split_sizes_and_stratification():
    df = _toy()
    s = random_stratified_split(df, seed=1)
    assert len(s["train"]) + len(s["val"]) + len(s["test"]) == len(df)
    assert not (set(s["train"]) & set(s["test"])) and not (set(s["val"]) & set(s["test"]))
    assert abs(df.iloc[s["test"]]["label"].mean() - 0.5) < 0.05


def test_grouped_split_has_no_group_overlap():
    df = _toy()
    s = grouped_stratified_split(df, seed=3)
    rep = overlap_report(df, s)
    assert rep["test_groups_also_in_train"] == 0 and rep["val_groups_also_in_train"] == 0
    assert rep["share_test_rows_with_group_in_train"] == 0.0
    r = random_stratified_split(df, seed=3)
    assert overlap_report(df, r)["share_test_rows_with_group_in_train"] > 0.5


def test_temporal_split_is_chronological():
    df = _toy()
    s = temporal_split(df)
    assert df.iloc[s["train"]]["timestamp"].max() <= df.iloc[s["val"]]["timestamp"].min()
    assert df.iloc[s["val"]]["timestamp"].max() <= df.iloc[s["test"]]["timestamp"].min()


def test_save_and_load_split(tmp_path):
    df = _toy()
    s = random_stratified_split(df)
    save_split(s, tmp_path / "s.json", meta={"seed": 42})
    s2 = load_split(tmp_path / "s.json")
    assert all(np.array_equal(s[k], s2[k]) for k in s)
