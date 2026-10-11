# zieni2023survey

## Citation
Rasha Zieni, Luisa Massari, Maria Carla Calzarossa (2023). Phishing or Not Phishing? A Survey on the Detection of Phishing Websites. *IEEE Access*, pp. 18499-18519. DOI: 10.1109/ACCESS.2023.3247135

- URL: https://doi.org/10.1109/ACCESS.2023.3247135
- Access status: full_text (research/papers/zieni2023survey.pdf)
- Verified: yes
- Theme (L2): f - surveys & SoKs discussing evaluation
- Relevance score (1-5): 3

## Verification
Semantic Scholar record (DOI 10.1109/ACCESS.2023.3247135, IEEE Access 2023, CC BY-NC-ND) checked 2026-10-11; PDF from ieeexplore OA link. Page range taken from PDF.

## Problem
Survey phishing-website detection methods and their data sources and metrics.

## Method
Structured review of features, selection, algorithms, metrics

## Dataset(s)
Survey of list-based, similarity-based and ML-based detection; dataset sources (PhishTank, OpenPhish, Alexa, DMOZ, Google queries)

## Features
URL and HTML feature taxonomies

## Evaluation protocol
Notes that Alexa retired in May 2022 and DMOZ was discontinued, that datasets 'often share the data sources' yet differ in content, and highlights work demonstrating 'the importance of taking precisely into account the imbalanced nature of phishing attacks'

## Metrics reported
Qualitative.

## Main findings
Benign data provenance (Alexa/DMOZ) is fragile and the imbalanced nature of the problem is under-addressed.

## Limitations
**Authors' stated:** Survey.

**Our caveats:** No explicit artefact discussion.

## Research gap
N/A

## Relevance to our project
Recent survey confirming benign-source fragility and imbalance as open issues.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
