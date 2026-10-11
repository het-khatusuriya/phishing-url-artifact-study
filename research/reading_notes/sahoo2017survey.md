# sahoo2017survey

## Citation
Sahoo, Doyen; Liu, Chenghao; Hoi, Steven C. H. (2017). *Malicious URL Detection using Machine Learning: A Survey*. arXiv preprint arXiv:1701.07179 (v3, 2019). URL: https://arxiv.org/abs/1701.07179

- Type: preprint | Theme (L1): a-foundational-lexical | Access: full_text | Verified: full
- Local PDF: research/papers/sahoo2017survey.pdf

## Verification
Checked 2026-10-11: arXiv API record 1701.07179 (authors, dates) and arXiv PDF read. No DOI (preprint).

## Problem
Structure the literature on ML-based malicious URL detection.

## Method
Defines the learning problem, surveys feature families and learning algorithms, discusses system design and open challenges.

## Dataset(s)
Survey (no new data); reviews datasets up to 2.4M URLs (Ma et al.)

## Features
Catalogue: lexical (BoW, n-grams, statistics), host-based, content, context/popularity.

## Evaluation protocol
n/a (survey)

## Metrics reported
n/a
(Numbers taken from the full text; section/table references given where identified.)

## Main findings
Lexical BoW features scale best; online learning suits drift; deep representation learning was emerging (precursor to URLNet).

## Limitations
- Stated by authors: Points out lack of large public benchmarks, concept drift, adversarial evasion, and short-lived URLs (open-challenges section).
- Our own caveats: Pre-dates transformers; benchmark discussion dated.

## Research gap
Standardised benchmarks and temporal evaluation protocols.

## Relevance to our project
Background/taxonomy citation for the related-work section; its open-challenge list matches our concerns (drift, benchmarks).

Relevance score: 4/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
