# tiwari2020phishingsiteurls

## Citation
Tarun Tiwari (Kaggle user taruntiwarihp) (2020). *Phishing Site URLs (Kaggle: 'Malicious and Phishing attacks ulrs')*. Kaggle dataset. URL: https://www.kaggle.com/datasets/taruntiwarihp/phishing-site-urls

## Verification
- Verified on 2026-10-11. Status: **partial**. Access: **full_text**.
- Evidence: PARTIAL: Kaggle page title/meta description confirmed on 2026-10-11; row counts, class balance, provenance, upload year and licence not readable (client-rendered). Year is approximate.

## Problem
n/a

## Method
n/a

## Dataset(s)
Download: Kaggle page (phishing_site_urls.csv). License: not confirmed. Timestamps: none. Labels: 'good'/'bad'. Known problems: undocumented provenance; heavy duplication reported by users; many URLs lack scheme.

## Features
Raw URL.

## Evaluation protocol
n/a

## Metrics reported (only numbers present in the source)
n/a

## Main findings
n/a

## Limitations
- Authors' stated limitations: n/a
- My assessment: Provenance unknown - weak as an external benchmark.

## Research gap
n/a

## Relevance to our project (score 3/5)
Possible extra external set only after de-duplication against our training data; low priority.

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
