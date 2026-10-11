# blum2010lexical

## Citation
Blum, Aaron; Wardman, Brad; Solorio, Thamar; Warner, Gary (2010). *Lexical feature based phishing URL detection using online learning*. Proceedings of the 3rd ACM Workshop on Artificial Intelligence and Security (AISec '10), pp. 54-60. DOI: 10.1145/1866423.1866434 URL: https://doi.org/10.1145/1866423.1866434

- Type: conference | Theme (L1): a-foundational-lexical | Access: abstract_only | Verified: full
- Local PDF: none (not legally downloadable at time of search)

## Verification
Checked 2026-10-11: Crossref record for DOI 10.1145/1866423.1866434 (AISec at CCS '10, pp. 54-60); OpenAlex abstract. Full text not legally accessible.

## Problem
Detect present and emerging phishing domains quickly using URL lexical features and online updates.

## Method
Lexical bag-of-tokens features (host/path/binary indicators) fed to a confidence-weighted (CW) online classifier so the model adapts as new phishing campaigns appear.

## Dataset(s)
UAB phishing URLs and benign URLs (sizes not in abstract)

## Features
Lexical tokens and URL-structure indicators only (no host lookups).

## Evaluation protocol
Not stated in abstract

## Metrics reported
Not in abstract (often cited as about 97% accuracy; unverified here).
(Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)

## Main findings
Lexical-only online learning is viable for zero-hour phishing detection.

## Limitations
- Stated by authors: Not available.
- Our own caveats: Small, non-public dataset; no cross-dataset test.

## Research gap
Reproducibility; feature drift analysis.

## Relevance to our project
Supports our lexical-only design choice and online/incremental retraining argument.

Relevance score: 3/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
