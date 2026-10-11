# prasad2024phiusiil

## Citation
Prasad, Arvind; Chandra, Shalini (2024). *PhiUSIIL: A diverse security profile empowered phishing URL detection framework based on similarity index and incremental learning*. Computers & Security, 136, 103545. DOI: 10.1016/j.cose.2023.103545 URL: https://doi.org/10.1016/j.cose.2023.103545

- Type: journal | Theme (L1): b-ensemble-hybrid | Access: abstract_only | Verified: full
- Local PDF: none (not legally downloadable at time of search)

## Verification
Checked 2026-10-11: Crossref record for DOI 10.1016/j.cose.2023.103545 (Comput. Secur. 136, 103545, 2024); UCI ML Repository dataset page #967 (dataset statistics and citation). Abstract text could not be retrieved (ScienceDirect blocked; Semantic Scholar/OpenAlex abstract empty).

## Problem
Phishing URL detection with similarity-based features and incremental model updates; release of a large feature dataset.

## Method
Computes URLSimilarityIndex, CharContinuationRate, TLDLegitimateProb and other URL/HTML-derived features; incremental learning to adapt to new data.

## Dataset(s)
PhiUSIIL dataset (UCI #967, CC BY 4.0): 235,795 URLs (134,850 legitimate, 100,945 phishing), 54 features from URL and page source

## Features
54 features (URL lexical + HTML indicators), several derived (similarity index, TLD legitimate probability).

## Evaluation protocol
Not retrievable (publisher page blocked); UCI page documents dataset only

## Metrics reported
Not retrieved.
(Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)

## Main findings
Dataset is now a common benchmark (used by Yi 2026 and others).

## Limitations
- Stated by authors: Not retrieved.
- Our own caveats: Dataset mixes URL and page-source features and some derived features (e.g., TLDLegitimateProb) risk label leakage; collection windows undocumented on UCI page.

## Research gap
Leakage audit of derived features.

## Relevance to our project
Candidate external dataset (235k) similar in scale to ours; must audit feature leakage before cross-dataset use.

Relevance score: 3/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
