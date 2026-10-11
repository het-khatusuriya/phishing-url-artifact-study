# kibriya2025lightweight

## Citation
Kibriya, Hareem; Amin, Rashid; Alshamrani, Sultan S.; Rehman, Safia; Hassan, Mehdi; Alsubaei, Faisal S. (2025). *Lightweight malicious URL detection using deep learning and large language models*. Scientific Reports, 15, 43044. DOI: 10.1038/s41598-025-26653-2 URL: https://doi.org/10.1038/s41598-025-26653-2

- Type: journal | Theme (L1): d-transformer-llm | Access: full_text | Verified: full
- Local PDF: research/papers/kibriya2025lightweight.pdf

## Verification
Checked 2026-10-11: Nature open-access PDF (CC BY-NC-ND) read; Crossref record for DOI 10.1038/s41598-025-26653-2 (Sci. Rep. 15:43044, 2025).

## Problem
Lightweight, explainable 4-class malicious URL classification using LLM embeddings.

## Method
Extract URL embeddings with pre-trained LLMs; train small recurrent head; LIME for token-level attributions; latency measurement.

## Dataset(s)
Kaggle malicious-urls dataset: 651,191 URLs (428,103 benign, 96,457 defacement, 94,111 phishing, 32,520 malware), aggregated from ISCX-URL-2016, PhishTank, Malware Domains, PhishStorm (Dataset section)

## Features
LLM embeddings of URL text.

## Evaluation protocol
60:40 random train/test split; ablations; per-class PR/ROC curves

## Metrics reported
97.5% accuracy with BERT and T5 embeddings (avg precision/recall/F1 0.97/0.97/0.96); GPT-2 97%; 0.119 ms per sample; per-class AUC 0.99-1.0 (Results; Table 2, Figs. 6-8).
(Numbers taken from the full text; section/table references given where identified.)

## Main findings
Frozen LLM embeddings + tiny head reach boosted-tree-level accuracy on the Kaggle set; LIME gives readable token attributions.

## Limitations
- Stated by authors: Single dataset; obfuscation robustness tested only partly.
- Our own caveats: Same aggregated Kaggle dataset as Sankaranarayanan 2024 - source-formatting shortcuts likely; random split.

## Research gap
Cross-dataset/temporal validation.

## Relevance to our project
Comparable explainability approach (LIME) on a 650k Kaggle set; our SHAP + artifact audit extends this.

Relevance score: 3/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
