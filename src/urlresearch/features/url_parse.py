"""Safe, consistent URL parsing shared by every feature extractor.

A URL is untrusted input. This module never raises on malformed strings; it
returns a `ParsedURL` with empty components instead, and records a
`parse_error` flag that extractors can expose as a feature.
"""
from __future__ import annotations

import ipaddress
import re
from dataclasses import dataclass, field
from typing import Optional
from urllib.parse import urlsplit, unquote

import tldextract

# Offline public-suffix extraction: use the snapshot bundled with tldextract,
# never fetch the live list (reproducibility + no network at feature time).
_EXTRACT = tldextract.TLDExtract(suffix_list_urls=(), fallback_to_snapshot=True)

_SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*://")


@dataclass
class ParsedURL:
    raw: str
    scheme: str = ""
    had_scheme: bool = False
    userinfo: str = ""
    hostname: str = ""
    port: Optional[int] = None
    path: str = ""
    query: str = ""
    fragment: str = ""
    subdomain: str = ""
    domain: str = ""           # second-level label (e.g. "google")
    suffix: str = ""           # public suffix (e.g. "co.uk")
    registered_domain: str = ""  # domain + suffix, or host if no suffix
    is_ip: bool = False
    is_ipv6: bool = False
    parse_error: bool = False
    decoded_hostname: str = ""  # IDNA-decoded hostname when possible
    labels: list = field(default_factory=list)

    @property
    def netloc_for_grouping(self) -> str:
        """Key used for domain-grouped splitting."""
        if self.is_ip:
            return self.hostname
        return self.registered_domain or self.hostname or "__empty__"


def _try_ip(host: str) -> tuple[bool, bool]:
    try:
        ip = ipaddress.ip_address(host.strip("[]"))
        return True, ip.version == 6
    except ValueError:
        return False, False


def parse_url(url: object) -> ParsedURL:
    """Parse any string into a ParsedURL without raising."""
    raw = "" if url is None else str(url).strip()
    p = ParsedURL(raw=raw)
    if not raw:
        p.parse_error = True
        return p

    had_scheme = bool(_SCHEME_RE.match(raw))
    candidate = raw if had_scheme else "http://" + raw
    p.had_scheme = had_scheme
    try:
        s = urlsplit(candidate)
        hostname = s.hostname or ""
        try:
            port = s.port
        except ValueError:
            port = None
            p.parse_error = True
        p.scheme = (s.scheme or "").lower()
        p.userinfo = s.netloc.rsplit("@", 1)[0] if "@" in s.netloc else ""
        p.hostname = hostname.lower()
        p.port = port
        p.path = s.path or ""
        p.query = s.query or ""
        p.fragment = s.fragment or ""
    except ValueError:
        # e.g. unmatched IPv6 brackets. Fall back to a crude split.
        p.parse_error = True
        body = candidate.split("://", 1)[1] if "://" in candidate else candidate
        netloc, _, rest = body.partition("/")
        p.scheme = candidate.split("://", 1)[0].lower() if "://" in candidate else ""
        p.hostname = netloc.rsplit("@", 1)[-1].split(":")[0].lower()
        p.path = "/" + rest if rest else ""

    host = p.hostname
    p.is_ip, p.is_ipv6 = _try_ip(host) if host else (False, False)
    if host and not p.is_ip:
        ext = _EXTRACT(host)
        p.subdomain, p.domain, p.suffix = ext.subdomain, ext.domain, ext.suffix
        p.registered_domain = (
            f"{ext.domain}.{ext.suffix}" if ext.suffix else host
        )
        p.labels = [lab for lab in host.split(".") if lab]
        try:
            p.decoded_hostname = host.encode("ascii").decode("idna")
        except (UnicodeError, ValueError):
            p.decoded_hostname = host
    elif host:
        p.registered_domain = host
        p.labels = [host]
        p.decoded_hostname = host
    return p


def percent_decode(text: str, rounds: int = 2) -> str:
    """Decode percent-encoding up to `rounds` times (handles double encoding)."""
    out = text
    for _ in range(rounds):
        new = unquote(out)
        if new == out:
            break
        out = new
    return out
