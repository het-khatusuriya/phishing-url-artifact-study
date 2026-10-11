from collections import Counter
from urllib.parse import urlsplit, parse_qs
import ipaddress
import math
import re

SUSPICIOUS_TLDS = {
    "zip", "mov", "top", "xyz", "tk", "gq", "ml", "cf",
    "work", "click", "link", "country", "stream", "download",
    "science", "racing", "review", "party", "monster", "cam"
}

URL_SHORTENING_DOMAINS = {
    "bit.ly", "tinyurl.com", "t.co", "goo.gl", "ow.ly",
    "is.gd", "buff.ly", "cutt.ly", "rb.gy", "shorturl.at",
    "tiny.cc", "rebrand.ly", "shorte.st", "adf.ly"
}

SUSPICIOUS_KEYWORDS = {
    "login", "signin", "verify", "verification", "account",
    "secure", "security", "update", "confirm", "password",
    "banking", "wallet", "payment", "invoice", "recover",
    "suspend", "unlock", "validate", "credential"
}

BRAND_NAMES = {
    "google", "paypal", "microsoft", "apple", "amazon",
    "facebook", "instagram", "netflix", "whatsapp", "yahoo",
    "linkedin", "dropbox", "bankofamerica", "chase"
}

EXCESSIVE_HYPHEN_THRESHOLD = 3


def calculate_entropy(value):
    if not value:
        return 0.0

    counts = Counter(value)
    total = len(value)

    return -sum(
        (count / total) * math.log2(count / total)
        for count in counts.values()
    )


def get_url_parts(url):
    parsed = urlsplit(str(url))
    hostname = parsed.hostname or ""
    path = parsed.path or ""
    query = parsed.query or ""
    scheme = parsed.scheme.lower()

    return parsed, hostname.lower(), path, query, scheme


def is_ip_address(hostname):
    try:
        ipaddress.ip_address(hostname)
        return 1
    except ValueError:
        return 0


def count_letters(value):
    return sum(character.isalpha() for character in value)


def count_digits(value):
    return sum(character.isdigit() for character in value)


def count_query_parameters(query):
    if not query:
        return 0

    return len(parse_qs(query, keep_blank_values=True))


def extract_features(url):
    url = str(url)
    parsed, hostname, path, query, scheme = get_url_parts(url)
    url_lower = url.lower()
    hostname_lower = hostname.lower()

    url_length = len(url)
    num_dots = url.count(".")
    num_slashes = url.count("/")
    num_hyphens = url.count("-")
    num_underscores = url.count("_")
    num_special_characters = sum(
        not character.isalnum()
        for character in url
    )
    num_digits = count_digits(url)
    num_letters = count_letters(url)

    digit_to_letter_ratio = (
        num_digits / num_letters
        if num_letters > 0
        else 0.0
    )

    path_length = len(path)
    query_string_length = len(query)
    num_query_parameters = count_query_parameters(query)
    num_at_symbols = url.count("@")
    num_double_slash_occurrences = url.count("//")
    url_entropy = calculate_entropy(url)
    domain_length = len(hostname)

    domain_parts = [
        part for part in hostname.split(".")
        if part
    ]

    num_subdomains = max(len(domain_parts) - 2, 0)

    tld_type = (
        domain_parts[-1]
        if domain_parts and not is_ip_address(hostname)
        else "ip"
    )

    suspicious_tld = int(tld_type in SUSPICIOUS_TLDS)
    punycode_idn_usage = int("xn--" in hostname_lower)
    ip_address_instead_of_domain = is_ip_address(hostname)
    https_usage = int(scheme == "https")

    url_shortening_service = int(
        hostname_lower in URL_SHORTENING_DOMAINS
        or any(
            hostname_lower.endswith("." + domain)
            for domain in URL_SHORTENING_DOMAINS
        )
    )

    encoded_characters = url.count("%")

    hexadecimal_characters = len(
        re.findall(r"(?i)(?:0x[0-9a-f]+|[0-9a-f]{2})", url)
    )

    suspicious_keywords = int(
        any(keyword in url_lower for keyword in SUSPICIOUS_KEYWORDS)
    )

    brand_name_presence = int(
        any(brand in url_lower for brand in BRAND_NAMES)
    )

    excessive_hyphens = int(
        num_hyphens > EXCESSIVE_HYPHEN_THRESHOLD
    )

    hostname_without_common_prefix = re.sub(
        r"^(www\d?\.)",
        "",
        hostname_lower
    )

    hostname_alphanumeric = re.sub(
        r"[^a-z0-9]",
        "",
        hostname_without_common_prefix
    )

    random_looking_domain = int(
        len(hostname_alphanumeric) >= 12
        and count_digits(hostname_without_common_prefix) >= 3
        and calculate_entropy(hostname_alphanumeric) >= 3.5
    )

    return {
        "url_length": url_length,
        "num_dots": num_dots,
        "num_slashes": num_slashes,
        "num_hyphens": num_hyphens,
        "num_underscores": num_underscores,
        "num_special_characters": num_special_characters,
        "num_digits": num_digits,
        "digit_to_letter_ratio": digit_to_letter_ratio,
        "path_length": path_length,
        "query_string_length": query_string_length,
        "num_query_parameters": num_query_parameters,
        "num_at_symbols": num_at_symbols,
        "num_double_slash_occurrences": num_double_slash_occurrences,
        "url_entropy": url_entropy,
        "domain_length": domain_length,
        "num_subdomains": num_subdomains,
        "tld_type": tld_type,
        "suspicious_tld": suspicious_tld,
        "punycode_idn_usage": punycode_idn_usage,
        "ip_address_instead_of_domain": ip_address_instead_of_domain,
        "https_usage": https_usage,
        "url_shortening_service": url_shortening_service,
        "encoded_characters": encoded_characters,
        "hexadecimal_characters": hexadecimal_characters,
        "suspicious_keywords": suspicious_keywords,
        "brand_name_presence": brand_name_presence,
        "excessive_hyphens": excessive_hyphens,
        "random_looking_domain": random_looking_domain
    }