# sameen2020phishhaven

## Citation
Sameen, Maria; Han, Kyunghyun; Hwang, Seong Oun (2020). *PhishHaven-An Efficient Real-Time AI Phishing URLs Detection System*. IEEE Access, 8, pp. 83425-83443. DOI: 10.1109/ACCESS.2020.2991403 URL: https://doi.org/10.1109/ACCESS.2020.2991403

- Type: journal | Theme (L1): b-ensemble-hybrid | Access: full_text | Verified: full
- Local PDF: research/papers/sameen2020phishhaven.pdf

## Verification
Checked 2026-10-11: IEEE Access open-access PDF (ielx7/.../09082616.pdf, CC BY per Crossref license) read; Crossref record for DOI 10.1109/ACCESS.2020.2991403 (vol 8, 83425-83443).

## Problem
Detect both human-crafted and AI-generated (DeepPhish) phishing URLs in real time.

## Method
Lexical feature extraction with HTML-encoding decoding; ensemble of ML models with unbiased voting; multi-threaded execution; URL-Hit expands shortened URLs.

## Dataset(s)
100,000 URLs: 50,000 Alexa benign + 50,000 DeepPhish AI-generated phishing (Sec. VI, Table 4); plus 50,000 PhishTank 'simple' phishing (collected by 4 Sep 2019)

## Features
Lexical features (lengths, counts, special characters, tokens) after URL decoding.

## Evaluation protocol
5:5 split ratio train/test (Sec. VI); theoretical analysis

## Metrics reported
98.00% accuracy and F1 about 98% on the 100k set; 97% TPR, 99.17% TNR, 0.8% FPR (Sec. VII, Tables 7-9).
(Numbers taken from the full text; section/table references given where identified.)

## Main findings
Lexical ensembles can separate DeepPhish-generated URLs from Alexa benign URLs with high accuracy.

## Limitations
- Stated by authors: Tiny-URL handling needs expansion service; '100% on future AI URLs' claim is theoretical (Sec. V).
- Our own caveats: Benign = Alexa homepages vs long generated URLs: a strong length/structure shortcut; random split only.

## Research gap
Realistic benign class and temporal validation.

## Relevance to our project
Example of a lexical ensemble; also a cautionary example of homepage-vs-phishing shortcut artifacts we want to audit.

Relevance score: 3/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
