# phishtank

## Citation
Cisco Talos / OpenDNS (community) (2026). *PhishTank verified online phishing URL database*. https://phishtank.org/developer_info.php. URL: https://phishtank.org/developer_info.php

## Verification
- Verified on 2026-10-11. Status: **yes**. Access: **full_text**.
- Evidence: PhishTank developer page fetched 2026-10-11 (formats, URL pattern, fields, hourly update, API key note, terms link to Cisco EULA).

## Problem
n/a

## Method
n/a

## Dataset(s)
Download: http://data.phishtank.com/data/online-valid.{csv,json,xml}[.gz|.bz2] (optionally with app key). License: Cisco end-user licence terms (research use permitted under terms; redistribution restricted). Timestamps: YES (submission_time, verification_time, ISO 8601). Labels: all entries are community-verified phishing; target brand when known. Known problems: only 'online & valid' at dump time; survivorship bias; brand/target noise; near-duplicate kit URLs.

## Features
n/a

## Evaluation protocol
n/a

## Metrics reported (only numbers present in the source)
n/a

## Main findings
Only major public phishing source with per-URL timestamps.

## Limitations
- Authors' stated limitations: n/a
- My assessment: Benign counterpart must be sourced separately (Tranco/Common Crawl), creating distribution artefacts.

## Research gap
n/a

## Relevance to our project (score 5/5)
Source for building a timestamped external test set (time-aware evaluation).

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
