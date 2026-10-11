# urlhaus

## Citation
abuse.ch / Spamhaus (2026). *URLhaus (abuse.ch) malware URL feed*. https://urlhaus.abuse.ch/api/. URL: https://urlhaus.abuse.ch/api/

## Verification
- Verified on 2026-10-11. Status: **yes**. Access: **full_text**.
- Evidence: URLhaus API page fetched 2026-10-11 (dump types, cadence, auth-key requirement, fair-use terms). Column list and licence (commonly CC0) not visible on that page -> not asserted.

## Problem
n/a

## Method
n/a

## Dataset(s)
Download: https://urlhaus-api.abuse.ch/v2/files/exports/<AUTH-KEY>/recent.csv (and full/active variants). License: abuse.ch terms of use, free under fair use; commercial API paid. Timestamps: dumps are known to include a date-added field, but this was not verified on the fetched page. Labels: malware distribution URLs (threat type, tags), not phishing. Known problems: label semantics differ from phishing; many URLs are raw IPs/open directories.

## Features
n/a

## Evaluation protocol
n/a

## Metrics reported (only numbers present in the source)
n/a

## Main findings
n/a

## Limitations
- Authors' stated limitations: n/a
- My assessment: Malware != phishing; mixing shifts the task definition.

## Research gap
n/a

## Relevance to our project (score 3/5)
Explains the 'malware' class in the Kaggle corpus; use only for multi-class or out-of-distribution checks.

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
