# haynes2021lightweight

## Citation
Haynes, Katherine; Shirazi, Hossein; Ray, Indrakshi (2021). *Lightweight URL-based phishing detection using natural language processing transformers for mobile devices*. Procedia Computer Science, 191, pp. 127-134 (FNC/MobiSPC 2021). DOI: 10.1016/j.procs.2021.07.040 URL: https://doi.org/10.1016/j.procs.2021.07.040

- Type: conference | Theme (L1): d-transformer-llm | Access: abstract_only | Verified: full
- Local PDF: none (not legally downloadable at time of search)

## Verification
Checked 2026-10-11: Crossref record for DOI 10.1016/j.procs.2021.07.040 (Procedia CS 191, 127-134) and OpenAlex abstract. ScienceDirect PDF blocked despite OA.

## Problem
Mobile-deployable phishing detection from URLs only.

## Method
Baseline ANNs on features; deep ANN on URL-only features (poor); pre-trained transformers fine-tuned on URL text.

## Dataset(s)
URL and HTML feature datasets (sizes not in abstract)

## Features
Raw URL text (transformers); URL/HTML features (ANNs).

## Evaluation protocol
Not in abstract

## Metrics reported
ANNs on URL+HTML features >96%; deep ANN on URL-only features max 86.2%; pre-trained transformers outperform custom-vocabulary model; about 8 min training (abstract).
(Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)

## Main findings
Pre-trained text transformers transfer to URLs better than custom-vocab models in this setting.

## Limitations
- Stated by authors: Not available.
- Our own caveats: Abstract omits transformer accuracy numbers.

## Research gap
n/a

## Relevance to our project
Early BERT/ELECTRA URL fine-tuning reference.

Relevance score: 3/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
