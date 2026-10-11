# kan2005fast

## Citation
Kan, Min-Yen; Thi, Hoang Oanh Nguyen (2005). *Fast webpage classification using URL features*. Proceedings of the 14th ACM International Conference on Information and Knowledge Management (CIKM '05), pp. 325-326. DOI: 10.1145/1099554.1099649 URL: https://doi.org/10.1145/1099554.1099649

- Type: conference | Theme (L1): a-foundational-lexical | Access: abstract_only | Verified: full
- Local PDF: none (not legally downloadable at time of search)

## Verification
Checked 2026-10-11: Crossref API record for DOI 10.1145/1099554.1099649 (title, authors, CIKM 2005, pages 325-326) and OpenAlex abstract; ACM DL page returned 403.

## Problem
Classify web pages by topic using only the URL, avoiding fetching page content.

## Method
Segments URLs into meaningful tokens, adds component (which URL part), sequential (order) and orthographic features; supervised maximum-entropy modelling.

## Dataset(s)
Two standardized webpage-classification domains (topical classification); sizes not in abstract

## Features
URL token, token-position (component), sequential and orthographic (length/case/digit) features.

## Evaluation protocol
Standard topical-classification benchmarks; split details not in abstract

## Metrics reported
Abstract states URL-only methods 'approach the performance' of full-text/link-based methods in certain scenarios; no numbers available without full text.
(Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)

## Main findings
Early evidence that URL tokens carry strong signal for page classification; introduced the token-segmentation idea reused by later phishing-URL work.

## Limitations
- Stated by authors: Not available (abstract only).
- Our own caveats: Topic classification, not security; 2-page poster; no adversarial setting.

## Research gap
Pre-dates phishing-specific URL work; no temporal or adversarial evaluation.

## Relevance to our project
Historical root for URL tokenisation / segmentation features; cite for lineage of lexical features.

Relevance score: 2/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
