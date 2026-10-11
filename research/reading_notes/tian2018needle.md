# tian2018needle

## Citation
Ke Tian; Steve T. K. Jan; Hang Hu; Danfeng Yao; Gang Wang (2018). *Needle in a Haystack: Tracking Down Elite Phishing Domains in the Wild*. Proceedings of the Internet Measurement Conference 2018 (IMC '18), Boston, MA. DOI: 10.1145/3278532.3278569 URL: https://doi.org/10.1145/3278532.3278569

## Verification
- Verified on 2026-10-11. Status: **yes**. Access: **full_text** (PDF: research/papers/tian2018needle.pdf).
- Evidence: Semantic Scholar API record for DOI 10.1145/3278532.3278569 (title, authors, IMC 2018); author PDF from people.cs.vt.edu (DOI printed on first page).

## Problem
Find high-quality 'elite' phishing pages that impersonate both content and domain.

## Method
Enumerate five squatting types for 702 brands, scan 224M DNS records, classify pages with visual+OCR features, verify manually.

## Dataset(s)
DNS zone data and crawled pages (2017-2018); not released as a URL benchmark.

## Features
Page visual/OCR features; domain squatting types.

## Evaluation protocol
Precision via manual verification; blacklist evasion measured over time

## Metrics reported (only numbers present in the source)
657K candidate squatting domains; 1,175 verified squatting phishing pages; >90% evaded popular blacklists for at least a month (abstract).

## Main findings
Squatting phishing is long-lived and under-blacklisted; domain-level impersonation is a core evasion tactic.

## Limitations
- Authors' stated limitations: Brand list limited to 702; manual verification bottleneck.
- My assessment: Content-based detector; our lexical model must rely on domain string cues.

## Research gap
Squatting-aware lexical features (brand-in-domain edit distance) under controlled mutation.

## Relevance to our project (score 4/5)
Source for mutation operators (typo/bit/homograph/combo/wrong-TLD) and for motivating brand-similarity features.

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
