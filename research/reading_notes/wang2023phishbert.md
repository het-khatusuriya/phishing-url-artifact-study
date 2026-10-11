# wang2023phishbert

## Citation
Wang, Yanbin; Zhu, Weifan; Xu, Haitao; Qin, Zhan; Ren, Kui; Ma, Wenrui (2023). *A Large-Scale Pretrained Deep Model for Phishing URL Detection*. ICASSP 2023 - IEEE International Conference on Acoustics, Speech and Signal Processing, pp. 1-5. DOI: 10.1109/ICASSP49357.2023.10095719 URL: https://doi.org/10.1109/ICASSP49357.2023.10095719

- Type: conference | Theme (L1): d-transformer-llm | Access: abstract_only | Verified: full
- Local PDF: none (not legally downloadable at time of search)

## Verification
Checked 2026-10-11: Crossref record for DOI 10.1109/ICASSP49357.2023.10095719 (ICASSP 2023, pp. 1-5); Semantic Scholar API record (title, authors, abstract). IEEE page not fetchable; no open PDF.

## Problem
Avoid naive transfer of text-pretrained models by pre-training a URL-specific transformer at scale.

## Method
URL-specific pre-training (3B+ URLs), adversarial fine-tuning for classification.

## Dataset(s)
More than 3 billion unlabeled URLs for pre-training; labelled benign/malicious URL benchmarks (sizes not in abstract)

## Features
Sub-word URL tokens.

## Evaluation protocol
Not in abstract ('extensive and rigorous benchmark studies')

## Metrics reported
None in abstract ('significantly superior ... efficiency, robustness and accuracy').
(Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)

## Main findings
URL-domain pre-training beats text-pretrained transfer (authors).

## Limitations
- Stated by authors: Not available.
- Our own caveats: No public weights located; not reproducible for us.

## Research gap
Open URL foundation models.

## Relevance to our project
Reference point for URL-specific pre-training; contrast with our lightweight ensemble.

Relevance score: 4/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
