# rao2020catchphish

## Citation
Rao, Routhu Srinivasa; Vaishnavi, Tatti; Pais, Alwyn Roshan (2020). *CatchPhish: detection of phishing websites by inspecting URLs*. Journal of Ambient Intelligence and Humanized Computing, 11(2), pp. 813-825. DOI: 10.1007/s12652-019-01311-4 URL: https://doi.org/10.1007/s12652-019-01311-4

- Type: journal | Theme (L1): b-ensemble-hybrid | Access: abstract_only | Verified: full
- Local PDF: none (not legally downloadable at time of search)

## Verification
Checked 2026-10-11: Crossref record for DOI 10.1007/s12652-019-01311-4 (JAIHC 11(2), 813-825, 2020) and Springer article page (abstract, accuracy figures).

## Problem
Lightweight URL-only phishing detection without visiting the site or third-party services.

## Method
Hand-crafted hostname/URL features + TF-IDF features + phishing hint words; RF classifier.

## Dataset(s)
Authors' dataset plus two benchmark datasets (names/sizes not on abstract page)

## Features
Hostname features, full-URL features, TF-IDF, hint words.

## Evaluation protocol
Not stated on abstract page

## Metrics reported
93.25% (TF-IDF only) and 94.26% (TF-IDF + hand-crafted) on own data; 98.25% and 97.49% on two benchmark datasets (Springer abstract).
(Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)

## Main findings
Combining TF-IDF n-grams with hand-crafted lexical features improves RF accuracy.

## Limitations
- Stated by authors: Not available.
- Our own caveats: Benchmark names unclear from abstract; no temporal test.

## Research gap
Cross-dataset evaluation.

## Relevance to our project
Close to our hybrid (lexical + TF-IDF + RF) baseline design.

Relevance score: 3/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
