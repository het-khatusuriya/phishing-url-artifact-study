# oest2018phisherkit

## Citation
Adam Oest; Yeganeh Safei; Adam Doupe; Gail-Joon Ahn; Brad Wardman; Gary Warner (2018). *Inside a phisher's mind: Understanding the anti-phishing ecosystem through phishing kit analysis*. 2018 APWG Symposium on Electronic Crime Research (eCrime). DOI: 10.1109/ECRIME.2018.8376206 URL: https://doi.org/10.1109/ECRIME.2018.8376206

## Verification
- Verified on 2026-10-11. Status: **yes**. Access: **abstract_only**.
- Evidence: Semantic Scholar API record for DOI 10.1109/ECRIME.2018.8376206 (title, authors, venue, year, abstract).

## Problem
How do phishers evade researchers/blacklists and structure URLs?

## Method
Analyse phishing kits' .htaccess cloaking and propose a URL classification scheme.

## Dataset(s)
Phishing kits and URLs 2016-2017 (industry-sourced; not public).

## Features
n/a

## Evaluation protocol
Descriptive measurement

## Metrics reported (only numbers present in the source)
None quantitative in abstract.

## Main findings
Phishers track and evade anti-phishing infrastructure; URL type correlates with compromised infrastructure.

## Limitations
- Authors' stated limitations: n/a (abstract only).
- My assessment: Tangential to URL classifiers.

## Research gap
n/a

## Relevance to our project (score 2/5)
Background for the realism of URL-level evasion and for a typology of phishing URLs (compromised domain vs. deceptive domain).

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
