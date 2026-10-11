# garera2007framework

## Citation
Garera, Sujata; Provos, Niels; Chew, Monica; Rubin, Aviel D. (2007). *A framework for detection and measurement of phishing attacks*. Proceedings of the 2007 ACM Workshop on Recurring Malcode (WORM '07), pp. 1-8. DOI: 10.1145/1314389.1314391 URL: https://doi.org/10.1145/1314389.1314391

- Type: conference | Theme (L1): a-foundational-lexical | Access: abstract_only | Verified: full
- Local PDF: none (not legally downloadable at time of search)

## Verification
Checked 2026-10-11: Crossref API record for DOI 10.1145/1314389.1314391 (title, authors, WORM 2007 within CCS '07, pages 1-8); OpenAlex abstract.

## Problem
Tell phishing URLs from benign ones without page content; measure phishing prevalence at scale.

## Method
Taxonomy of URL obfuscation (IP host, redirection, brand in host/path, etc.); features incl. page rank and host-name/path heuristics; logistic regression filter; used for large-scale measurement.

## Dataset(s)
Google-internal URL data; 'several million URLs' measured (abstract); labelled set size not in abstract

## Features
Obfuscation-type indicators, brand-word presence, host/path lexical heuristics, Google page-rank / crawl features.

## Evaluation protocol
Not stated in abstract (Ma et al. KDD 2009 summarise it as 97.3% accuracy over 2,500 URLs)

## Metrics reported
Accuracy 97.3% over 2,500 URLs is how Ma et al. (KDD 2009, related-work section) summarise this paper; the abstract itself gives no number.
(Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)

## Main findings
Phishing URLs are often identifiable from their structure alone; brand names embedded in host/path are strong cues.

## Limitations
- Stated by authors: Not available (abstract only).
- Our own caveats: Small labelled set; proprietary Google features (page rank) not reproducible; 2007 URL ecosystem.

## Research gap
No public dataset; no robustness analysis.

## Relevance to our project
Origin of 'brand-in-URL' and obfuscation-type lexical features that our extractor also uses.

Relevance score: 3/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
