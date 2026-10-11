# openphish

## Citation
OpenPhish (2026). *OpenPhish Community Feed*. https://openphish.com/phishing_feeds.html. URL: https://openphish.com/phishing_feeds.html

## Verification
- Verified on 2026-10-11. Status: **yes**. Access: **full_text**.
- Evidence: OpenPhish feeds page fetched 2026-10-11 (tiers, cadence, community feed URL on GitHub).

## Problem
n/a

## Method
n/a

## Dataset(s)
Download: https://raw.githubusercontent.com/openphish/public_feed/refs/heads/main/feed.txt . License: OpenPhish Terms of Use (community feed free, 'limited'). Timestamps: not in community text feed (only snapshot time). Labels: all phishing. Known problems: no timestamps/brand in free tier; short retention; was the phishing source of ISCX-URL-2016.

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
- My assessment: n/a

## Research gap
n/a

## Relevance to our project (score 4/5)
Secondary live phishing source; useful to collect a fresh post-training test set.

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
