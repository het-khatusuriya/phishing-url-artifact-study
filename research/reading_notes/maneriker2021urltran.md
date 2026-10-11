# maneriker2021urltran

## Citation
Maneriker, Pranav; Stokes, Jack W.; Lazo, Edir Garcia; Carutasu, Diana; Tajaddodianfar, Farid; Gururajan, Arun (2021). *URLTran: Improving Phishing URL Detection Using Transformers*. MILCOM 2021 - IEEE Military Communications Conference, pp. 197-204 (arXiv:2106.05256). DOI: 10.1109/MILCOM52596.2021.9653028 URL: https://arxiv.org/abs/2106.05256

- Type: conference | Theme (L1): d-transformer-llm | Access: full_text | Verified: full
- Local PDF: research/papers/maneriker2021urltran.pdf

## Verification
Checked 2026-10-11: arXiv API record 2106.05256 and arXiv PDF read; Crossref record for DOI 10.1109/MILCOM52596.2021.9653028 (MILCOM 2021, pp. 197-204). Note: Crossref/Semantic Scholar give MILCOM 2021 as the venue (not IEEE BigData).

## Problem
Transformer models for browser-scale phishing URL detection at very low FPR, with robustness to black-box attacks.

## Method
Compares URLTran_BERT, URLTran_RoBERTa, URLTran_CustVoc against URLNet and Texception; adversarial data augmentation and fine-tuning.

## Dataset(s)
Microsoft browser telemetry: 6 weeks; train 1,039,413, validation 259,854, test 1,784,155 URLs (8,742 phishing) after 1:20 down-sampling (Sec. 3)

## Features
Sub-word tokens (WordPiece/BPE) over URL strings.

## Evaluation protocol
Temporal split (4 weeks train / 1 validation / 1 test); TPR at FPR 0.01%; adversarial fine-tuning tests

## Metrics reported
Table 2: URLTran_BERT Acc 99.67%, TPR@0.01%FPR 86.80%, F1 0.9971, AUC 0.9993; URLNet TPR@0.01% 71.20%; Texception 52.15%; relative TPR improvement over 21.9% (abstract).
(Numbers taken from the full text; section/table references given where identified.)

## Main findings
Fine-tuned BERT beats char/word CNNs at low FPR; adversarial fine-tuning preserves low FPR under homoglyph/compound-split attacks.

## Limitations
- Stated by authors: Proprietary data; attack coverage limited.
- Our own caveats: Accuracy about 99.6% for all models shows accuracy is uninformative at this imbalance; TPR@low-FPR is the meaningful metric.

## Research gap
Public reproducible low-FPR benchmark; explainability of transformer URL models.

## Relevance to our project
State-of-the-art transformer baseline our ensemble should be compared with; reinforces low-FPR metrics and robustness tests.

Relevance score: 5/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
