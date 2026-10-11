# le2018urlnet

## Citation
Le, Hung; Pham, Quang; Sahoo, Doyen; Hoi, Steven C. H. (2018). *URLNet: Learning a URL Representation with Deep Learning for Malicious URL Detection*. arXiv preprint arXiv:1802.03162. URL: https://arxiv.org/abs/1802.03162

- Type: preprint | Theme (L1): c-char-level | Access: full_text | Verified: full
- Local PDF: research/papers/le2018urlnet.pdf

## Verification
Checked 2026-10-11: arXiv API record 1802.03162 (authors, v2 2018-03-02) and arXiv PDF read. No DOI (preprint).

## Problem
Learn URL embeddings end-to-end to capture semantics/sequence and handle unseen tokens.

## Method
Character CNN branch + word CNN branch (words embedded via character CNNs to handle rare words); jointly trained; ablations on branches and embedding modes.

## Dataset(s)
VirusTotal crawl: 5M URLs for training (sampled from first 60%, time-ordered), 10M for testing (from last 40%); malicious = flagged by >=5 blacklists, benign = 0 (Sec. 4.1.1, Table 1)

## Features
Learned char and word embeddings; URLs truncated/padded to 200 chars.

## Evaluation protocol
Temporal split (train earlier 60%, test later 40%); ROC/AUC and TPR at FPR 1e-4..1e-1 (Table 3)

## Metrics reported
URLNet(Full) achieves the best AUC and higher TPR at FPR 1e-3..1e-1 vs BoW baselines; slightly worse than word-level at FPR 1e-4 (Table 3, Fig. 4); feature vectors about 14x smaller than BoW for 2k URLs (Sec. 4.5).
(Numbers taken from the full text; section/table references given where identified.)

## Main findings
Joint char+word CNN generalises to unseen words better than BoW.

## Limitations
- Stated by authors: Hyperparameter sensitivity; large compute.
- Our own caveats: Labels from blacklist counts; multi-class malware vs phishing collapsed into 'malicious'.

## Research gap
Explainability of learned features; robustness.

## Relevance to our project
The canonical char+word CNN reference; its temporal split protocol and low-FPR reporting are models for our evaluation.

Relevance score: 5/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
