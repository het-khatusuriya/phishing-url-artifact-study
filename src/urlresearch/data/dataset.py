"""Dataset ingestion, validation, normalisation and deduplication.

Canonical schema after `load_dataset`:
    url (str), label (int: 1 = malicious/phishing, 0 = benign),
    source (str), timestamp (datetime64 or NaT), group (registered domain)
"""
from __future__ import annotations

import hashlib
import json
import logging
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Iterable, Optional

import pandas as pd

from ..features.url_parse import parse_url

log = logging.getLogger(__name__)

POSITIVE_LABELS = {"phishing", "malicious", "malware", "defacement", "bad", "1", "true", "spam"}
NEGATIVE_LABELS = {"legitimate", "benign", "good", "0", "false", "safe"}


@dataclass
class DatasetReport:
    name: str
    path: str
    sha256: str
    rows_raw: int
    rows_after_dropna: int
    rows_after_normalisation_dedup: int
    conflicting_label_urls_removed: int
    positives: int
    negatives: int
    unique_registered_domains: int
    share_https: float
    share_www: float
    share_ip_host: float
    has_timestamps: bool
    timestamp_min: Optional[str]
    timestamp_max: Optional[str]

    def to_json(self, path: Path) -> None:
        Path(path).write_text(json.dumps(asdict(self), indent=2))


def sha256_of(path: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(chunk), b""):
            h.update(block)
    return h.hexdigest()


def map_label(value) -> Optional[int]:
    s = str(value).strip().lower()
    if s in POSITIVE_LABELS:
        return 1
    if s in NEGATIVE_LABELS:
        return 0
    return None


def normalise_url(url: str) -> str:
    """Light normalisation used ONLY for duplicate detection (not for features).

    Lowercases scheme and host, strips a trailing slash on an empty path and a
    trailing fragment. The raw URL is kept for feature extraction so that
    case-sensitive features remain meaningful.
    """
    p = parse_url(url)
    scheme = p.scheme or "http"
    host = p.hostname
    port = f":{p.port}" if p.port and p.port not in (80, 443) else ""
    path = p.path if p.path not in ("", "/") else ""
    q = f"?{p.query}" if p.query else ""
    return f"{scheme}://{host}{port}{path}{q}"


def load_dataset(path: str | Path, name: str, url_col: str = "url", label_col: str = "label",
                 timestamp_col: Optional[str] = None, source: Optional[str] = None,
                 label_map: Optional[Dict] = None, nrows: Optional[int] = None,
                 report_dir: Optional[Path] = None) -> tuple[pd.DataFrame, DatasetReport]:
    path = Path(path)
    raw = pd.read_csv(path, low_memory=False, nrows=nrows, usecols=lambda c: True)
    rows_raw = len(raw)
    df = pd.DataFrame({
        "url": raw[url_col].astype("string"),
        "label_raw": raw[label_col],
    })
    if timestamp_col and timestamp_col in raw.columns:
        df["timestamp"] = pd.to_datetime(raw[timestamp_col], errors="coerce", utc=True)
    else:
        df["timestamp"] = pd.NaT
    df["source"] = source or name
    df = df.dropna(subset=["url", "label_raw"])
    df["url"] = df["url"].str.strip()
    df = df[df["url"].str.len() > 0]
    if label_map:
        df["label"] = df["label_raw"].map(lambda v: label_map.get(str(v).strip().lower()))
    else:
        df["label"] = df["label_raw"].map(map_label)
    unmapped = df["label"].isna().sum()
    if unmapped:
        log.warning("%s: %d rows with unmappable labels dropped (%s)", name, unmapped,
                    df.loc[df["label"].isna(), "label_raw"].astype(str).value_counts().head(5).to_dict())
    df = df.dropna(subset=["label"])
    df["label"] = df["label"].astype(int)
    rows_after_dropna = len(df)

    # normalisation-based dedup, keep the first occurrence; drop conflicting labels
    df["url_norm"] = df["url"].map(normalise_url)
    nunique_lbl = df.groupby("url_norm")["label"].nunique()
    conflicting = set(nunique_lbl[nunique_lbl > 1].index)
    df = df[~df["url_norm"].isin(conflicting)]
    df = df.drop_duplicates(subset="url_norm", keep="first")

    parsed = df["url"].map(parse_url)
    df["group"] = parsed.map(lambda p: p.netloc_for_grouping)
    df["host"] = parsed.map(lambda p: p.hostname)
    share_https = float(parsed.map(lambda p: p.scheme == "https").mean()) if len(df) else 0.0
    share_www = float(parsed.map(lambda p: bool(p.labels) and p.labels[0].startswith("www")).mean()) if len(df) else 0.0
    share_ip = float(parsed.map(lambda p: p.is_ip).mean()) if len(df) else 0.0
    df = df.drop(columns=["label_raw", "url_norm"]).reset_index(drop=True)

    has_ts = bool(df["timestamp"].notna().any())
    rep = DatasetReport(
        name=name, path=str(path), sha256=sha256_of(path), rows_raw=rows_raw,
        rows_after_dropna=rows_after_dropna, rows_after_normalisation_dedup=len(df),
        conflicting_label_urls_removed=len(conflicting),
        positives=int(df["label"].sum()), negatives=int((df["label"] == 0).sum()),
        unique_registered_domains=int(df["group"].nunique()),
        share_https=share_https, share_www=share_www, share_ip_host=share_ip,
        has_timestamps=has_ts,
        timestamp_min=str(df["timestamp"].min()) if has_ts else None,
        timestamp_max=str(df["timestamp"].max()) if has_ts else None,
    )
    if report_dir:
        Path(report_dir).mkdir(parents=True, exist_ok=True)
        rep.to_json(Path(report_dir) / f"dataset_report_{name}.json")
    return df, rep


def concat_datasets(frames: Iterable[pd.DataFrame]) -> pd.DataFrame:
    df = pd.concat(list(frames), ignore_index=True)
    df["url_norm"] = df["url"].map(normalise_url)
    df = df.drop_duplicates(subset="url_norm", keep="first").drop(columns="url_norm")
    return df.reset_index(drop=True)
