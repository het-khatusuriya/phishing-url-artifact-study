# alam2026philter

## Citation
Mahbub Alam, Muhammad Lutfor Rahman, Sonjoy Kumar Paul, Amy W. Hays, Aftab Hussain, Md Imanul Huq, Nitesh Saxena (2026). SoK: PHILTER: Uncovering Security and Functional Gaps in AI-based Phishing Website Detection Literature via an LLM-based Reasoning Framework. *35th USENIX Security Symposium (USENIX Security 26), prepublication*. 

- URL: https://www.usenix.org/system/files/conference/usenixsecurity26/sec26_prepub_alam.pdf
- Access status: full_text (research/papers/alam2026philter.pdf)
- Verified: partial
- Theme (L2): f - surveys & SoKs discussing evaluation
- Relevance score (1-5): 4

## Verification
Prepublication PDF hosted on usenix.org (title, authors, affiliations from PDF front matter) checked 2026-10-11. Could not locate the USENIX presentation page or final page numbers, hence 'partial'.

## Problem
AI-based phishing-website detection studies report high accuracy, but it is unclear whether they meet real-world requirements (drift, benign diversity, imbalance-aware metrics, privacy).

## Method
LLM-assisted extraction plus expert validation against four functionality metrics (incl. F3 robustness on diverse benign pages, F4 evaluation transparency under class imbalance) and three security metrics (S1 adaptation to concept drift via temporally disjoint evaluation, S2 resistance to active attackers, S3 privacy)

## Dataset(s)
55 academic AI-based phishing-website detection approaches assessed

## Features
N/A (systematisation)

## Evaluation protocol
Rubric scoring of each paper; taxonomy of detection strategies

## Metrics reported
No study fulfils all requirements; most risk elevated false alarms due to limited testing on diverse benign pages (long-tail/low-rank domains); many assume static tactics (abstract, Sec. 4-5).

## Main findings
Accuracy-driven evaluation hides blind spots: insufficient benign diversity, no temporally disjoint testing, metrics unsuited to class imbalance (recommends AUC-PR, MCC, class-specific metrics).

## Limitations
**Authors' stated:** LLM extraction validated by experts but still subjective; website-level focus.

**Our caveats:** Prepublication version; URL-only works are a subset of the 55.

## Research gap
Same rubric applied specifically to URL-only detectors.

## Relevance to our project
Most recent systematisation confirming that benign-diversity and imbalance-aware metrics are missing in the literature; use its F3/F4/S1 rubric to position our evaluation.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
