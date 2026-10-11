# saxe2017expose

## Citation
Saxe, Joshua; Berlin, Konstantin (2017). *eXpose: A Character-Level Convolutional Neural Network with Embeddings For Detecting Malicious URLs, File Paths and Registry Keys*. arXiv preprint arXiv:1702.08568. URL: https://arxiv.org/abs/1702.08568

- Type: preprint | Theme (L1): c-char-level | Access: full_text | Verified: full
- Local PDF: research/papers/saxe2017expose.pdf

## Verification
Checked 2026-10-11: arXiv API record 1702.08568 (authors, date 2017-02-27) and arXiv PDF read. No DOI.

## Problem
Replace hand-engineered features with a generic character-level CNN for short security strings.

## Method
Embeds characters (dim 32), parallel convolutions of several kernel sizes, sum pooling, dense layers; trained on raw URL strings.

## Dataset(s)
Invincea/VirusTotal-derived URLs (counts in Table 1; URLs with 1-4 AV detections discarded), plus file paths and registry keys

## Features
Learned character embeddings (no manual features); baseline uses 1024-dim hashed n-gram features.

## Evaluation protocol
Held-out split with low-FPR ROC analysis (FPR 1e-4 to 1e-2) (Sec. 4)

## Metrics reported
5-10% detection-rate gain over manual-feature baselines at 0.1% FPR (abstract); about 6% higher at FPR 1e-3 for URLs (Sec. 4, Fig. 3).
(Numbers taken from the full text; section/table references given where identified.)

## Main findings
Char-CNN beats hashed n-gram baselines on URLs at low FPR.

## Limitations
- Stated by authors: Labels derived from AV engine counts (noisy); not peer reviewed.
- Our own caveats: Dataset proprietary; no cross-dataset test.

## Research gap
Public reproducibility.

## Relevance to our project
Origin of char-CNN URL models; our char-level branch follows this design; low-FPR evaluation style is worth adopting.

Relevance score: 4/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
