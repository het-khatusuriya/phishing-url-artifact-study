# bhuiyan2026fragility

## Citation
Istiaque Bhuiyan, Tanvir Bhuiyan (2026). The Fragility of Phishing Detection Models: Evidence from Cross-Corpus Transfer, Prevalence Shift, Artifact Learning, and Evasion Risk. *Big Data and Cognitive Computing*, art. 211. DOI: 10.3390/bdcc10070211

- URL: https://doi.org/10.3390/bdcc10070211
- Access status: full_text (research/papers/bhuiyan2026fragility.pdf)
- Verified: yes
- Theme (L2): c - cross-dataset generalisation
- Relevance score (1-5): 4

## Verification
Crossref record 10.3390/bdcc10070211 (vol. 10, issue 7, art. 211, published 2026-06-29, CC BY) checked 2026-10-11; PDF from mdpi-res.com.

## Problem
Benchmark accuracy of phishing (email) detectors hides failures under cross-corpus transfer, prevalence shift and artefact-driven learning.

## Method
TF-IDF logistic regression and linear SVC; pooled baseline, single-corpus cross-dataset transfer, leave-one-corpus-out, prevalence-shift simulation, training-prevalence manipulation, dataset-identification probe, top-feature inspection, artifact-removal ablation, feature-sensitivity masking

## Dataset(s)
Six public phishing/spam email corpora: CEAS_08, Enron, Ling, Nazario, Nigerian Fraud, SpamAssassin

## Features
Text tokens incl. headers, dates, URL/domain terms

## Evaluation protocol
Cross-corpus and leave-one-out; prevalence shift with fixed thresholds vs alert budgets; artefact ablations

## Metrics reported
Leave-one-corpus-out F1 0.8201-0.8994 (LR) and 0.7607-0.8910 (SVC); dataset-identification accuracy 0.9722 (LR) / 0.9806 (SVC), i.e., corpus identity is highly learnable (abstract).

## Main findings
Models partly learn corpus markers (date tokens, headers, URL/domain terms) rather than phishing semantics; prevalence shift failure is asymmetric and threshold dependent; recommends cross-corpus validation, prevalence-aware thresholding and artefact tests.

## Limitations
**Authors' stated:** Linear models only; email modality.

**Our caveats:** Email, not URL; but the 'dataset-identification probe' and artefact-removal ablation design transfer directly to URL features.

## Research gap
Same protocol for URL datasets.

## Relevance to our project
Blueprint for our artifact-removal ablation and a 'can the model tell which dataset a URL came from?' probe; also motivates prevalence-aware threshold/calibration analysis.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
