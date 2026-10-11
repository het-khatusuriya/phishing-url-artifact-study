# sahingoz2019machine

## Citation
Sahingoz, Ozgur Koray; Buber, Ebubekir; Demir, Onder; Diri, Banu (2019). *Machine learning based phishing detection from URLs*. Expert Systems with Applications, 117, pp. 345-357. DOI: 10.1016/j.eswa.2018.09.029 URL: https://doi.org/10.1016/j.eswa.2018.09.029

- Type: journal | Theme (L1): a-foundational-lexical | Access: abstract_only | Verified: full
- Local PDF: none (not legally downloadable at time of search)

## Verification
Checked 2026-10-11: Crossref record for DOI 10.1016/j.eswa.2018.09.029 (ESWA vol 117, 345-357, 2019); Semantic Scholar abstract; Marmara University repository record. Full text paywalled.

## Problem
Real-time, language-independent, third-party-free phishing URL detection.

## Method
Word-level tokenisation of URLs; 'NLP features' (brand/keyword, random-word, digit/length statistics), word vectors and hybrid sets; compares seven classifiers.

## Dataset(s)
Ebbu2017: 73,575 URLs (36,400 legitimate via Yandex queries, 37,175 phishing from PhishTank) - figures as reported by Sanchez-Paniagua 2022 and DEPHIDES 2024, which reuse the set

## Features
NLP features (word counts, randomness, brand names, TLD/subdomain cues) plus word-vector features.

## Evaluation protocol
Not confirmed from full text

## Metrics reported
97.98% accuracy with RF on NLP features (abstract).
(Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)

## Main findings
Random Forest on NLP-style lexical features performs best; dataset released and widely reused.

## Limitations
- Stated by authors: Not available.
- Our own caveats: Legitimate URLs from Yandex search results (deeper pages) vs PhishTank; later work (Sanchez-Paniagua 2022) shows models trained on this era degrade on 2020 data.

## Research gap
Temporal validity; artifact analysis.

## Relevance to our project
Ebbu2017 is a standard external test set for our cross-dataset experiments; RF result is a natural lexical baseline.

Relevance score: 4/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
