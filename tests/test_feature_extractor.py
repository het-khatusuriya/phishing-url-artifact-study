import math
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.urlresearch.features.url_parse import parse_url, percent_decode  # noqa: E402
from src.urlresearch.features.lexical import (BASELINE28_COLUMNS, LEXICAL_V2_COLUMNS,  # noqa: E402
                                              extract_baseline28, extract_lexical_v2,
                                              feature_frame, shannon_entropy)

MALFORMED = ["", " ", "http://", "http://[::1", "://nohost", "http:///path", "not a url at all",
             "http://exa mple.com", "http://例え.テスト/パス", "http://xn--r8jz45g.xn--zckzah/",
             "http://user:pw@host.com:99999/", "http://host.com:abc/", "ftp://1.2.3.4/x",
             "http://[2001:db8::1]:8080/a", "javascript:alert(1)", "data:text/html,hi",
             "http://" + "a" * 5000 + ".com/" + "b" * 10000, "%%%%%", "http://example.com/%zz%"]


class TestParseURL:
    def test_basic(self):
        p = parse_url("https://docs.google.com/presentation/d/e/x?start=false#f")
        assert p.scheme == "https" and p.hostname == "docs.google.com"
        assert p.registered_domain == "google.com" and p.subdomain == "docs"
        assert p.path == "/presentation/d/e/x" and p.query == "start=false" and p.fragment == "f"
        assert not p.parse_error

    def test_missing_scheme(self):
        p = parse_url("www.example.co.uk/login")
        assert p.hostname == "www.example.co.uk" and not p.had_scheme
        assert p.registered_domain == "example.co.uk" and p.suffix == "co.uk"

    def test_ip_hosts(self):
        p = parse_url("http://218.228.19.9/~yossi/9ssfpkz")
        assert p.is_ip and not p.is_ipv6 and p.netloc_for_grouping == "218.228.19.9"
        p6 = parse_url("http://[2001:db8::1]:8080/a")
        assert p6.is_ip and p6.is_ipv6 and p6.port == 8080

    def test_port_and_userinfo(self):
        p = parse_url("http://user:pw@host.com:8443/x")
        assert p.port == 8443 and p.userinfo == "user:pw" and p.hostname == "host.com"

    def test_idn(self):
        p = parse_url("http://xn--80ak6aa92e.com/")
        assert p.decoded_hostname != p.hostname and "xn--" in p.hostname

    @pytest.mark.parametrize("url", MALFORMED)
    def test_never_raises(self, url):
        p = parse_url(url)
        assert isinstance(p.hostname, str)

    def test_percent_decode_double(self):
        assert percent_decode("%2541") == "A"
        assert percent_decode("%2541", rounds=1) == "%41"


class TestBaseline28:
    def test_schema(self):
        f = extract_baseline28("https://www.visitcanada.com")
        assert list(f.keys()) == BASELINE28_COLUMNS
        assert f["url_length"] == 27 and f["num_subdomains"] == 1 and f["https_usage"] == 1

    @pytest.mark.parametrize("url", MALFORMED)
    def test_never_raises(self, url):
        f = extract_baseline28(url)
        assert set(f.keys()) == set(BASELINE28_COLUMNS)


class TestLexicalV2:
    def test_schema_stable(self):
        f = extract_lexical_v2("http://example.com")
        assert list(f.keys()) == LEXICAL_V2_COLUMNS
        assert all(isinstance(v, (int, float)) for v in f.values())

    def test_values(self):
        f = extract_lexical_v2("http://paypal.com.secure-login.xyz/webscr/update.php?cmd=login&id=%41%42")
        assert f["https_scheme"] == 0 and f["has_www_prefix"] == 0
        assert f["abused_suffix"] == 1 and f["tld_in_subdomain"] == 1
        assert f["brand_in_subdomain"] == 1 and f["brand_in_domain_exact"] == 0
        assert f["num_query_params"] == 2 and f["num_percent"] == 2
        assert f["suspicious_keyword_count"] >= 3 and f["path_has_script_ext"] == 1
        assert f["path_depth"] == 2

    def test_public_suffix_awareness(self):
        a = extract_lexical_v2("http://www.bbc.co.uk/news")
        b = extract_lexical_v2("http://www.bbc.com/news")
        assert a["num_subdomain_labels_psl"] == b["num_subdomain_labels_psl"] == 1
        assert a["num_subdomain_labels_psl_nowww"] == 0
        assert a["suffix_num_labels"] == 2 and b["suffix_num_labels"] == 1

    def test_brand_embedding_not_substring_false_positive(self):
        f = extract_lexical_v2("http://pineapple-recipes.org/")
        assert f["brand_in_domain_exact"] == 0 and f["brand_in_domain_embedded"] == 1
        g = extract_lexical_v2("http://apple.com/")
        assert g["brand_in_domain_exact"] == 1 and g["brand_in_domain_embedded"] == 0

    def test_ip_and_port(self):
        f = extract_lexical_v2("http://192.168.0.1:8080/login")
        assert f["is_ip_host"] == 1 and f["nonstandard_port"] == 1 and f["has_public_suffix"] == 0

    def test_entropy(self):
        assert shannon_entropy("") == 0.0 and shannon_entropy("aaaa") == 0.0
        assert math.isclose(shannon_entropy("ab"), 1.0)

    @pytest.mark.parametrize("url", MALFORMED)
    def test_never_raises(self, url):
        f = extract_lexical_v2(url)
        assert list(f.keys()) == LEXICAL_V2_COLUMNS
        assert all(not (isinstance(v, float) and math.isnan(v)) for v in f.values())

    def test_feature_frame_drop_artifacts(self):
        df = feature_frame(["http://a.com", "https://www.b.org/x"], "lexical_v2", drop_artifacts=True)
        assert "https_scheme" not in df.columns and "has_www_prefix" not in df.columns
        assert len(df) == 2


def test_canonical_features_invariant_to_scheme_and_www():
    from src.urlresearch.features.lexical import extract_lexical_v2_canon, LEXICAL_V2_CANON_COLUMNS
    from src.urlresearch.features.url_parse import canonicalize
    variants = ["https://www.example.com/login?x=1", "http://example.com/login?x=1",
                "example.com/login?x=1", "www.example.com/login?x=1", "HTTPS://www2.example.com/login?x=1"]
    feats = [extract_lexical_v2_canon(v) for v in variants[:4]]
    assert all(f == feats[0] for f in feats)
    assert list(feats[0].keys()) == LEXICAL_V2_CANON_COLUMNS
    assert canonicalize("a.com/www.b") == "a.com/www.b"


def test_original_extractor_scheme_less_bug():
    """Documents a defect of the ORIGINAL extractor (kept unchanged for fidelity):
    without a scheme the host is not parsed. Our parser handles both forms."""
    from src.features.feature_extractor import extract_features
    f = extract_features("visitcanada.com/")
    assert f["domain_length"] == 0 and f["tld_type"] == "ip"
    g = extract_lexical_v2("visitcanada.com/")
    assert g["host_length"] == len("visitcanada.com") and g["registered_domain_length"] == len("visitcanada")
