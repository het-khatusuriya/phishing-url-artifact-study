# aljofey2020effective

## Citation
Aljofey, Ali; Jiang, Qingshan; Qu, Qiang; Huang, Mingqing; Niyigena, Jean-Pierre (2020). *An Effective Phishing Detection Model Based on Character Level Convolutional Neural Network from URL*. Electronics, 9(9), 1514. DOI: 10.3390/electronics9091514 URL: https://doi.org/10.3390/electronics9091514

- Type: journal | Theme (L1): c-char-level | Access: full_text | Verified: full
- Local PDF: research/papers/aljofey2020effective.pdf

## Verification
Checked 2026-10-11: MDPI open-access PDF (CC BY; mdpi-res.com) read; Crossref record for DOI 10.3390/electronics9091514 (Electronics 9(9):1514, 2020).

## Problem
Fast URL-only phishing detection without third-party services or manual feature engineering.

## Method
Char-CNN (embedding + conv + pooling); baselines include RF/LR/NB/MNB with hand-crafted features across URL/host/path/file/query parts.

## Dataset(s)
D1: 318,642 URLs (Alexa, OpenPhish, Spamhaus, techhelplist, SANS ISC, PhishTank); D2 Ebbu2017 (Yandex/PhishTank); D3, D4 benchmark sets (Common Crawl+Alexa vs PhishTank) (Sec. 4.1)

## Features
Hand-crafted: counts of delimiters/special chars and lengths per URL part (U/H/P/F/Q feature families, Sec. 3); deep: char embeddings.

## Evaluation protocol
Random splits per dataset; five experiments; metrics accuracy/precision/recall/F1/AUC/time

## Metrics reported
Accuracy 95.02% on D1; 98.58%, 95.46%, 95.22% on D2-D4 (abstract, Sec. 5); common prefixes 'http://', 'https://', 'www.' are removed before modelling (Sec. 4.1, Table 3).
(Numbers taken from the full text; section/table references given where identified.)

## Main findings
Char-CNN outperforms classical ML with hand-crafted or TF-IDF features; URL-length distributions differ by class (Fig. 10).

## Limitations
- Stated by authors: Cannot handle shortened URLs; may misclassify unusual legitimate URLs (Sec. 6).
- Our own caveats: Explicitly removes scheme/www prefixes - evidence that authors recognised these as artifacts; no cross-dataset transfer reported.

## Research gap
Cross-dataset generalisation and artifact quantification.

## Relevance to our project
Useful precedent for removing https/www shortcuts before training; its hand-crafted feature catalogue overlaps ours.

Relevance score: 4/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
