import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.urlresearch.evaluation.mutations import MUTATIONS, apply_mutation  # noqa: E402
from src.urlresearch.features.url_parse import parse_url  # noqa: E402

URLS = ["http://www.example.com/login/index.php?id=1", "https://sub.site.co.uk", "http://1.2.3.4/x",
        "https://example.org/", "http://[::1]/a", "", "garbage"]


def test_all_mutations_never_raise_and_keep_registered_domain():
    for name in MUTATIONS:
        out = apply_mutation(URLS, name)
        assert len(out) == len(URLS)
        for a, b in zip(URLS, out):
            if not a or a == "garbage":
                continue
            pa, pb = parse_url(a), parse_url(b)
            assert pa.registered_domain == pb.registered_domain, (name, a, b)
            if name not in ("toggle_www",):
                assert pa.hostname == pb.hostname, (name, a, b)


def test_specific_behaviour():
    assert apply_mutation(["http://www.example.com/a"], "toggle_www")[0] == "http://example.com/a"
    assert apply_mutation(["http://example.com/a"], "toggle_www")[0] == "http://www.example.com/a"
    assert apply_mutation(["http://example.com/a"], "toggle_scheme")[0] == "https://example.com/a"
    assert apply_mutation(["http://example.com/a"], "default_port")[0] == "http://example.com:80/a"
    assert apply_mutation(["http://example.com/ab"], "encode_path_char")[0] == "http://example.com/%61b"
    assert apply_mutation(["http://example.com"], "trailing_slash")[0] == "http://example.com/"
    assert apply_mutation(["http://example.com/a?x=1"], "add_utm_query")[0].endswith("x=1&utm_source=newsletter")
    assert apply_mutation(["http://example.com/a"], "upper_host")[0] == "HTTP://EXAMPLE.COM/a"
