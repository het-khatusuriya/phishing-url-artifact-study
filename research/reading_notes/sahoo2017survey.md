# sahoo2017survey

## Citation
Doyen Sahoo, Chenghao Liu, Steven C. H. Hoi (2017). Malicious URL Detection using Machine Learning: A Survey. *arXiv preprint*. arXiv: 1701.07179

- URL: https://arxiv.org/abs/1701.07179
- Access status: full_text (research/papers/sahoo2017survey.pdf)
- Verified: yes
- Theme (L2): f - surveys & SoKs discussing evaluation
- Relevance score (1-5): 2

## Verification
arXiv abstract page and arXiv API record 1701.07179 (v1 Jan 2017, v3 Aug 2019) checked 2026-10-11.

## Problem
Formalise malicious URL detection as an ML problem and survey feature representations, algorithms and practical issues.

## Method
Formalises malicious URL detection as ML; taxonomy of feature representations (blacklist, lexical, host, content, context) and learning algorithms incl. online learning

## Dataset(s)
Survey; discusses URL data sources and 'detection as a service' design

## Features
Lexical bag-of-words, statistical URL features, host-based, content

## Evaluation protocol
Discusses practical issues: concept drift, label acquisition, feature cost; open problems

## Metrics reported
Qualitative.

## Main findings
Lexical features dominate deployed designs; practical systems need online/incremental learning because URL distributions drift.

## Limitations
**Authors' stated:** Pre-2017 literature.

**Our caveats:** Does not treat dataset artefacts.

## Research gap
N/A

## Relevance to our project
Background survey for lexical URL features and the online-learning view of drift.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
