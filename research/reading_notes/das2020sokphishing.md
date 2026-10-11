# das2020sokphishing

## Citation
Avisha Das, Shahryar Baki, Ayman El Aassal, Rakesh Verma, Arthur Dunbar (2020). SoK: A Comprehensive Reexamination of Phishing Research From the Security Perspective. *IEEE Communications Surveys & Tutorials*. DOI: 10.1109/COMST.2019.2957750; arXiv: 1911.00953

- URL: https://doi.org/10.1109/COMST.2019.2957750
- Access status: full_text (research/papers/das2020sokphishing.pdf)
- Verified: yes
- Theme (L2): f - surveys & SoKs discussing evaluation
- Relevance score (1-5): 4

## Verification
Semantic Scholar record (DOI 10.1109/COMST.2019.2957750, IEEE COMST) checked 2026-10-11; full text from arXiv 1911.00953 (page range of the journal version not verified, so omitted).

## Problem
Phishing research ignores security-specific challenges (base rate, active attacker, dataset quality, generalisation) in evaluation.

## Method
Critical survey with dataset-property, feature, algorithm and metric analysis

## Dataset(s)
Systematisation of phishing detection literature (email, website, URL) against four 'security challenges': real-time detection, active attacker, dataset quality, base-rate fallacy

## Features
Taxonomy of URL/website/email features

## Evaluation protocol
Reviews evaluation practice and finds: use of balanced datasets and inappropriate metrics, unreported timings, lack of generalisation studies

## Metrics reported
Qualitative; tables of dataset sizes/ratios per paper (Sec. V-VII).

## Main findings
Base-rate fallacy, active attacker, dataset diversity and generalisation studies 'are rarely mentioned, let alone emphasized' in prior surveys and papers.

## Limitations
**Authors' stated:** Coverage through 2019.

**Our caveats:** None substantial.

## Research gap
Empirical generalisation studies for URL detectors (which later Mia 2024 / Rashid 2024 begin to provide).

## Relevance to our project
Authoritative survey-level statement that balanced datasets, inappropriate metrics and missing generalisation studies are systemic in phishing research; anchors our motivation.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
