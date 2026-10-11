"""Lexical feature sets.

Three named feature sets are provided so that experiments can be run with an
explicit, versioned schema:

* ``baseline28``   – the 28 features of the original repository, computed by the
                     original extractor (imported unchanged for fidelity).
* ``lexical_v2``   – a public-suffix-aware, encoding-aware offline feature set.
* ``*_noartifact`` – variants of either set with collection-artifact features
                     removed (scheme, www/subdomain-count style features), used
                     for the shortcut-learning ablations.

Every extractor returns a flat ``dict[str, float|int|str]`` and never raises.
"""
from __future__ import annotations

import math
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Callable, Dict, Iterable, List

import numpy as np
import pandas as pd

from .url_parse import parse_url, percent_decode

# --------------------------------------------------------------------------
# Baseline 28 features: import the original extractor unchanged.
# --------------------------------------------------------------------------
_REPO_ROOT = Path(__file__).resolve().parents[3]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))
from src.features.feature_extractor import extract_features as _baseline_extract  # noqa: E402

BASELINE28_COLUMNS: List[str] = [
    "url_length", "num_dots", "num_slashes", "num_hyphens", "num_underscores",
    "num_special_characters", "num_digits", "digit_to_letter_ratio",
    "path_length", "query_string_length", "num_query_parameters",
    "num_at_symbols", "num_double_slash_occurrences", "url_entropy",
    "domain_length", "num_subdomains", "tld_type", "suspicious_tld",
    "punycode_idn_usage", "ip_address_instead_of_domain", "https_usage",
    "url_shortening_service", "encoded_characters", "hexadecimal_characters",
    "suspicious_keywords", "brand_name_presence", "excessive_hyphens",
    "random_looking_domain",
]

# Features of the baseline set that encode how the data were collected rather
# than URL maliciousness (see research/REPOSITORY_AUDIT.md §7).
BASELINE_ARTIFACT_COLUMNS = ["https_usage", "num_subdomains"]


def extract_baseline28(url: str) -> Dict:
    try:
        return _baseline_extract(url)
    except Exception:  # malformed URL: original extractor raises
        feats = {c: 0 for c in BASELINE28_COLUMNS}
        feats["tld_type"] = "parse_error"
        feats["url_length"] = len(str(url))
        return feats


# --------------------------------------------------------------------------
# lexical_v2
# --------------------------------------------------------------------------
SUSPICIOUS_KEYWORDS = (
    "login", "signin", "sign-in", "verify", "verification", "account", "secure",
    "security", "update", "confirm", "password", "banking", "wallet", "payment",
    "invoice", "recover", "suspend", "unlock", "validate", "credential", "auth",
    "webscr", "ebayisapi", "support", "billing", "limited", "alert",
)
# Brand tokens are matched as whole hostname labels / path tokens, not raw substrings.
BRAND_TOKENS = (
    "google", "paypal", "microsoft", "apple", "amazon", "facebook", "instagram",
    "netflix", "whatsapp", "yahoo", "linkedin", "dropbox", "bankofamerica",
    "chase", "wellsfargo", "office365", "outlook", "icloud", "dhl", "fedex",
    "usps", "coinbase", "binance", "steam", "roblox", "metamask",
)
SHORTENER_DOMAINS = frozenset({
    "bit.ly", "tinyurl.com", "t.co", "goo.gl", "ow.ly", "is.gd", "buff.ly",
    "cutt.ly", "rb.gy", "shorturl.at", "tiny.cc", "rebrand.ly", "shorte.st",
    "adf.ly", "bl.ink", "lnkd.in", "t.ly", "s.id", "v.gd", "qr.ae",
})
# Suffixes repeatedly reported as abused in public threat reports; used as a
# single indicator feature, not as a label proxy.
ABUSED_SUFFIXES = frozenset({
    "zip", "mov", "top", "xyz", "tk", "gq", "ml", "cf", "ga", "work", "click",
    "link", "country", "stream", "download", "science", "racing", "review",
    "party", "monster", "cam", "icu", "buzz", "rest", "surf", "cfd", "sbs",
    "bond", "quest", "cyou", "lol", "fit",
})
FREE_HOSTING_SUFFIXES = (
    "000webhostapp.com", "weebly.com", "wixsite.com", "blogspot.com",
    "github.io", "netlify.app", "vercel.app", "web.app", "firebaseapp.com",
    "glitch.me", "repl.co", "herokuapp.com", "pages.dev", "workers.dev",
    "sites.google.com", "duckdns.org", "ngrok.io", "webflow.io", "square.site",
    "godaddysites.com", "yolasite.com", "jimdosite.com", "mystrikingly.com",
    "r2.dev", "web.core.windows.net", "azurewebsites.net", "s3.amazonaws.com",
    "ipfs.io", "dweb.link",
)
_TOKEN_RE = re.compile(r"[^A-Za-z0-9]+")
_DIGIT_RUN_RE = re.compile(r"\d+")
_HEX32_RE = re.compile(r"(?i)\b[0-9a-f]{16,}\b")
_VOWELS = set("aeiou")
_EXECUTABLE_EXT = (".exe", ".scr", ".zip", ".rar", ".js", ".vbs", ".bat", ".apk",
                   ".msi", ".dll", ".jar", ".ps1", ".hta", ".iso", ".img")
_SCRIPT_EXT = (".php", ".asp", ".aspx", ".jsp", ".cgi", ".pl")


def shannon_entropy(s: str) -> float:
    if not s:
        return 0.0
    n = len(s)
    return -sum((c / n) * math.log2(c / n) for c in Counter(s).values())


def _tokens(s: str) -> List[str]:
    return [t for t in _TOKEN_RE.split(s) if t]


def _longest_run(s: str, pred: Callable[[str], bool]) -> int:
    best = cur = 0
    for ch in s:
        cur = cur + 1 if pred(ch) else 0
        best = max(best, cur)
    return best


def _consonant_ratio(s: str) -> float:
    letters = [c for c in s.lower() if c.isalpha()]
    if not letters:
        return 0.0
    return sum(c not in _VOWELS for c in letters) / len(letters)


def extract_lexical_v2(url: str) -> Dict:
    p = parse_url(url)
    raw = p.raw
    raw_l = raw.lower()
    host = p.hostname
    host_dec = p.decoded_hostname or host
    path, query, frag = p.path, p.query, p.fragment
    decoded_url = percent_decode(raw)
    path_tokens = _tokens(path)
    host_labels = p.labels
    sub_labels = [lab for lab in p.subdomain.split(".") if lab] if p.subdomain else []
    url_tokens = _tokens(raw)
    f: Dict = {}

    # --- whole-URL shape ---
    f["url_length"] = len(raw)
    f["url_entropy"] = shannon_entropy(raw)
    f["num_digits"] = sum(c.isdigit() for c in raw)
    f["num_letters"] = sum(c.isalpha() for c in raw)
    f["digit_ratio"] = f["num_digits"] / max(len(raw), 1)
    f["num_special_characters"] = sum(not c.isalnum() for c in raw)
    f["special_ratio"] = f["num_special_characters"] / max(len(raw), 1)
    f["num_dots"] = raw.count(".")
    f["num_hyphens"] = raw.count("-")
    f["num_underscores"] = raw.count("_")
    f["num_slashes"] = raw.count("/")
    f["num_question"] = raw.count("?")
    f["num_equals"] = raw.count("=")
    f["num_ampersand"] = raw.count("&")
    f["num_at_symbols"] = raw.count("@")
    f["num_tilde"] = raw.count("~")
    f["num_percent"] = raw.count("%")
    f["num_plus"] = raw.count("+")
    f["num_semicolon"] = raw.count(";")
    f["num_uppercase"] = sum(c.isupper() for c in raw)
    f["uppercase_ratio"] = f["num_uppercase"] / max(len(raw), 1)
    f["num_non_ascii"] = sum(ord(c) > 127 for c in raw)
    f["longest_digit_run"] = _longest_run(raw, str.isdigit)
    f["longest_token_length"] = max((len(t) for t in url_tokens), default=0)
    f["mean_token_length"] = float(np.mean([len(t) for t in url_tokens])) if url_tokens else 0.0
    f["num_tokens"] = len(url_tokens)
    f["has_long_hex_token"] = int(bool(_HEX32_RE.search(raw)))
    f["double_encoding"] = int(percent_decode(raw, 1) != decoded_url)
    f["decoded_length_delta"] = len(decoded_url) - len(raw)
    f["parse_error"] = int(p.parse_error)

    # --- scheme / authority (collection-artifact-prone; grouped for ablation) ---
    f["https_scheme"] = int(p.scheme == "https")
    f["had_explicit_scheme"] = int(p.had_scheme)
    f["has_www_prefix"] = int(bool(host_labels) and host_labels[0].startswith("www"))
    f["has_userinfo"] = int(bool(p.userinfo))
    f["has_port"] = int(p.port is not None)
    f["nonstandard_port"] = int(p.port is not None and p.port not in (80, 443))
    f["scheme_in_path_or_query"] = int(bool(re.search(r"(?i)https?(:|%3a)", path + "?" + query)))
    f["double_slash_in_path"] = int("//" in path)

    # --- hostname ---
    f["host_length"] = len(host)
    f["host_entropy"] = shannon_entropy(host)
    f["host_num_labels"] = len(host_labels)
    f["num_subdomain_labels_psl"] = len(sub_labels)
    f["num_subdomain_labels_psl_nowww"] = len([s for s in sub_labels if not s.startswith("www")])
    f["registered_domain_length"] = len(p.domain)
    f["suffix_length"] = len(p.suffix)
    f["suffix_num_labels"] = len(p.suffix.split(".")) if p.suffix else 0
    f["host_num_digits"] = sum(c.isdigit() for c in host)
    f["host_digit_ratio"] = f["host_num_digits"] / max(len(host), 1)
    f["host_num_hyphens"] = host.count("-")
    f["domain_num_hyphens"] = p.domain.count("-")
    f["domain_num_digits"] = sum(c.isdigit() for c in p.domain)
    f["domain_entropy"] = shannon_entropy(p.domain)
    f["domain_consonant_ratio"] = _consonant_ratio(p.domain)
    f["domain_longest_consonant_run"] = _longest_run(p.domain, lambda c: c.isalpha() and c.lower() not in _VOWELS)
    f["longest_subdomain_label"] = max((len(s) for s in sub_labels), default=0)
    f["is_ip_host"] = int(p.is_ip)
    f["is_ipv6_host"] = int(p.is_ipv6)
    f["is_punycode"] = int("xn--" in host)
    f["host_non_ascii_after_decode"] = int(any(ord(c) > 127 for c in host_dec))
    f["has_public_suffix"] = int(bool(p.suffix))
    f["abused_suffix"] = int(p.suffix.split(".")[-1] in ABUSED_SUFFIXES if p.suffix else 0)
    f["free_hosting_suffix"] = int(any(host == s or host.endswith("." + s) for s in FREE_HOSTING_SUFFIXES))
    f["is_shortener"] = int(p.registered_domain in SHORTENER_DOMAINS)
    f["brand_in_subdomain"] = int(any(b in sub_labels or any(b in s for s in sub_labels) for b in BRAND_TOKENS))
    f["brand_in_domain_exact"] = int(p.domain in BRAND_TOKENS)
    f["brand_in_domain_embedded"] = int(p.domain not in BRAND_TOKENS and any(b in p.domain for b in BRAND_TOKENS))
    f["brand_in_path"] = int(any(b in (t.lower() for t in path_tokens) for b in BRAND_TOKENS))
    f["tld_in_subdomain"] = int(any(s in ("com", "net", "org") for s in sub_labels))
    f["domain_has_tld_token"] = int(any(x in p.domain for x in ("com-", "-com", "net-", "org-")))

    # --- path / query / fragment ---
    f["path_length"] = len(path)
    f["path_depth"] = len([s for s in path.split("/") if s])
    f["path_entropy"] = shannon_entropy(path)
    f["path_num_tokens"] = len(path_tokens)
    f["path_longest_token"] = max((len(t) for t in path_tokens), default=0)
    f["path_num_digits"] = sum(c.isdigit() for c in path)
    f["path_has_executable_ext"] = int(path.lower().endswith(_EXECUTABLE_EXT))
    f["path_has_script_ext"] = int(any(path.lower().endswith(e) or e + "?" in raw_l for e in _SCRIPT_EXT))
    f["path_has_html_ext"] = int(path.lower().endswith((".html", ".htm")))
    f["path_has_tilde"] = int("~" in path)
    f["query_length"] = len(query)
    f["num_query_params"] = len([q for q in query.split("&") if q]) if query else 0
    f["query_has_url"] = int(bool(re.search(r"(?i)(https?%3a|https?://|www\.)", query)))
    f["query_has_email"] = int(bool(re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", percent_decode(query))))
    f["fragment_length"] = len(frag)
    f["has_fragment"] = int(bool(frag))
    f["suspicious_keyword_count"] = sum(k in raw_l for k in SUSPICIOUS_KEYWORDS)
    f["suspicious_keyword_in_host"] = int(any(k in host for k in SUSPICIOUS_KEYWORDS))
    f["suspicious_keyword_in_path"] = int(any(k in path.lower() for k in SUSPICIOUS_KEYWORDS))

    # --- token vocabulary cues (kept categorical-free: numeric only) ---
    f["num_hex_tokens_ge8"] = sum(1 for t in url_tokens if len(t) >= 8 and re.fullmatch(r"(?i)[0-9a-f]+", t) and any(c.isdigit() for c in t))
    f["num_numeric_tokens"] = sum(t.isdigit() for t in url_tokens)
    f["num_mixed_alnum_tokens"] = sum(any(c.isdigit() for c in t) and any(c.isalpha() for c in t) for t in url_tokens)
    return f


LEXICAL_V2_COLUMNS: List[str] = list(extract_lexical_v2("http://www.example.com/a?b=1").keys())
LEXICAL_V2_ARTIFACT_COLUMNS = [
    "https_scheme", "had_explicit_scheme", "has_www_prefix",
    "host_num_labels", "num_subdomain_labels_psl",
]

FEATURE_SETS: Dict[str, Dict] = {
    "baseline28": dict(fn=extract_baseline28, columns=BASELINE28_COLUMNS,
                       categorical=["tld_type"], artifact=BASELINE_ARTIFACT_COLUMNS),
    "lexical_v2": dict(fn=extract_lexical_v2, columns=LEXICAL_V2_COLUMNS,
                       categorical=[], artifact=LEXICAL_V2_ARTIFACT_COLUMNS),
}


def feature_frame(urls: Iterable[str], feature_set: str = "lexical_v2",
                  drop_artifacts: bool = False) -> pd.DataFrame:
    """Vectorised-by-loop extraction into a DataFrame with a fixed column order."""
    spec = FEATURE_SETS[feature_set]
    rows = [spec["fn"](u) for u in urls]
    df = pd.DataFrame(rows, columns=spec["columns"])
    if drop_artifacts:
        df = df.drop(columns=[c for c in spec["artifact"] if c in df.columns])
    return df
