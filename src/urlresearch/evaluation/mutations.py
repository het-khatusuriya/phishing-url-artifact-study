"""Controlled, offline, label-preserving URL mutations for robustness tests.

Two tiers with explicit label-preservation assumptions:

Tier A — RFC 3986 equivalence (strict): the mutated string identifies the same
resource, so the ground-truth label is preserved by construction.
    upper_host         host/scheme case-insensitive
    trailing_slash     '' and '/' paths are equivalent for the authority
    default_port       ':80' for http, ':443' for https
    encode_path_char   percent-encode unreserved characters in the path
    add_fragment       fragments are never sent to the server

Tier B — presentation variants (assumed): the registered domain, path and
query are unchanged, so the *intent* of the URL is assumed unchanged, but the
server could in principle serve different content.
    toggle_www         add/remove a leading 'www.' label
    toggle_scheme      http <-> https
    add_utm_query      append a tracking parameter

These are exactly the collection-artifact dimensions identified in the audit,
so Tier B measures sensitivity to artifacts rather than adversarial robustness.
"""
from __future__ import annotations

from typing import Callable, Dict, List
from urllib.parse import urlsplit, urlunsplit, quote

from ..features.url_parse import parse_url

_UNRESERVED_TO_ENCODE = "abcdefghijklmnopqrstuvwxyz"


def _parts(url: str):
    p = parse_url(url)
    s = urlsplit(url if p.had_scheme else "http://" + url)
    return p, s


def upper_host(url: str) -> str:
    p, s = _parts(url)
    if not s.hostname:
        return url
    netloc = s.netloc.replace(s.hostname, s.hostname.upper())
    return urlunsplit((s.scheme.upper(), netloc, s.path, s.query, s.fragment))


def trailing_slash(url: str) -> str:
    p, s = _parts(url)
    if s.path in ("", "/"):
        return urlunsplit((s.scheme, s.netloc, "/" if s.path == "" else "", s.query, s.fragment))
    return url if url.endswith("/") else url  # only applies to empty paths


def default_port(url: str) -> str:
    p, s = _parts(url)
    if not s.hostname or p.port is not None:
        return url
    port = ":443" if s.scheme == "https" else ":80"
    host = s.hostname if not p.is_ipv6 else f"[{s.hostname}]"
    netloc = s.netloc.replace(host, host + port, 1)
    return urlunsplit((s.scheme, netloc, s.path, s.query, s.fragment))


def encode_path_char(url: str) -> str:
    p, s = _parts(url)
    if not s.path or len(s.path) < 2:
        return url
    # percent-encode the first lowercase letter in the path
    path = s.path
    for i, ch in enumerate(path):
        if ch in _UNRESERVED_TO_ENCODE:
            path = path[:i] + "%%%02X" % ord(ch) + path[i + 1:]
            break
    return urlunsplit((s.scheme, s.netloc, path, s.query, s.fragment))


def add_fragment(url: str) -> str:
    p, s = _parts(url)
    if s.fragment:
        return url
    return urlunsplit((s.scheme, s.netloc, s.path, s.query, "top"))


def toggle_www(url: str) -> str:
    p, s = _parts(url)
    if not s.hostname or p.is_ip:
        return url
    host = s.hostname
    new_host = host[4:] if host.startswith("www.") else "www." + host
    netloc = s.netloc.replace(host, new_host, 1)
    return urlunsplit((s.scheme, netloc, s.path, s.query, s.fragment))


def toggle_scheme(url: str) -> str:
    p, s = _parts(url)
    if s.scheme not in ("http", "https"):
        return url
    return urlunsplit(("https" if s.scheme == "http" else "http", s.netloc, s.path, s.query, s.fragment))


def add_utm_query(url: str) -> str:
    p, s = _parts(url)
    q = (s.query + "&" if s.query else "") + "utm_source=newsletter"
    return urlunsplit((s.scheme, s.netloc, s.path, q, s.fragment))


MUTATIONS: Dict[str, Dict] = {
    "upper_host": dict(fn=upper_host, tier="A"),
    "trailing_slash": dict(fn=trailing_slash, tier="A"),
    "default_port": dict(fn=default_port, tier="A"),
    "encode_path_char": dict(fn=encode_path_char, tier="A"),
    "add_fragment": dict(fn=add_fragment, tier="A"),
    "toggle_www": dict(fn=toggle_www, tier="B"),
    "toggle_scheme": dict(fn=toggle_scheme, tier="B"),
    "add_utm_query": dict(fn=add_utm_query, tier="B"),
}


def apply_mutation(urls: List[str], name: str) -> List[str]:
    fn: Callable[[str], str] = MUTATIONS[name]["fn"]
    return [fn(u) for u in urls]
