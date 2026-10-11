# siddhartha2021maliciousurls

## Citation
Manu Siddhartha (Kaggle user sid321axn) (2021). *Malicious URLs dataset (Kaggle: 'Huge dataset of 6,51,191 Malicious URLs')*. Kaggle dataset. URL: https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset

## Verification
- Verified on 2026-10-11. Status: **partial**. Access: **full_text**.
- Evidence: PARTIAL: Kaggle page meta tags confirm title and '6,51,191' URLs (fetched 2026-10-11). The per-class breakdown, upload date and licence are rendered client-side and could not be read; the source list (ISCX-URL-2016 benign/phishing/malware/defacement, Malware Domain Blacklist, PhishTank, PhishStorm, GitHub benign list) comes from a third-party GitHub project describing the dataset, not from the Kaggle page itself.

## Problem
n/a (dataset)

## Method
Concatenation of public lists keeping only URL and class.

## Dataset(s)
Download: Kaggle page above (malicious_phish.csv; requires Kaggle login). License: not confirmed (Kaggle pages commonly show CC0/unknown - verify on page). Timestamps: none. Labels: type in {benign, defacement, phishing, malware}; binary tasks usually map benign vs rest. Known problems: duplicates across sources; many URLs lack scheme; defacement class comes from ISCX Alexa-ranked compromised sites; source-specific formatting (e.g. 'www.' prefixes) can leak labels; 2016-2021 vintage.

## Features
Raw URL string only.

## Evaluation protocol
n/a

## Metrics reported (only numbers present in the source)
n/a

## Main findings
Most widely used multi-class URL corpus on Kaggle; our ~250k binary dataset likely derives from or overlaps with it.

## Limitations
- Authors' stated limitations: n/a
- My assessment: Provenance only partially documented; no per-URL dates; label noise unknown.

## Research gap
A documented, timestamped, de-duplicated version with source column.

## Relevance to our project (score 5/5)
Likely upstream of our training data; must check overlap/leakage before using any of its sources as 'external' data.

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
