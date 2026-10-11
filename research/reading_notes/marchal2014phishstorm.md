# marchal2014phishstorm

## Citation
Samuel Marchal; Jerome Francois; Radu State; Thomas Engel (2014). *PhishStorm: Detecting Phishing With Streaming Analytics*. IEEE Transactions on Network and Service Management 11(4):458-471. DOI: 10.1109/TNSM.2014.2377295 URL: https://doi.org/10.1109/TNSM.2014.2377295

## Verification
- Verified on 2026-10-11. Status: **yes**. Access: **abstract_only**.
- Evidence: Crossref record for DOI 10.1109/TNSM.2014.2377295 (title, authors, TNSM 11(4):458-471, 2014); Aalto dataset page (counts, label semantics, DOI, file urlset.csv.zip 3.24 MB). HAL preprint page blocked by bot protection; PDF not obtained.

## Problem
Real-time phishing URL detection using word relatedness inside the URL.

## Method
Compute intra-URL relatedness features from search-engine query data; classify in a streaming setting.

## Dataset(s)
Download: https://research.aalto.fi/en/datasets/phishstorm-phishing-legitimate-url-dataset (urlset.csv.zip). License: unspecified. Timestamps: none. Labels: 0 legitimate, 1 phishing. Known problems: 2014 vintage; feature columns depend on 2014 search-engine statistics; URLs in 'domain' column.

## Features
12 intra-URL relatedness features (per dataset description).

## Evaluation protocol
Hold-out; ~95% classification rate reported

## Metrics reported (only numbers present in the source)
~95% classification rate (search-result summary of abstract; not verified from full text).

## Main findings
Intra-URL semantics help detection.

## Limitations
- Authors' stated limitations: n/a
- My assessment: Dated; features not reproducible today.

## Research gap
n/a

## Relevance to our project (score 3/5)
Upstream source of part of the Kaggle 'Malicious URLs' corpus; useful for provenance.

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
