# bozkir2023grambeddings

## Citation
Bozkir, Ahmet Selman; Dalgic, Firat Coskun; Aydos, Murat (2023). *GramBeddings: A New Neural Network for URL Based Identification of Phishing Web Pages Through N-gram Embeddings*. Computers & Security, 124, 102964. DOI: 10.1016/j.cose.2022.102964 URL: https://doi.org/10.1016/j.cose.2022.102964

- Type: journal | Theme (L1): c-char-level | Access: abstract_only | Verified: full
- Local PDF: none (not legally downloadable at time of search)

## Verification
Checked 2026-10-11: Crossref record for DOI 10.1016/j.cose.2022.102964 (Comput. Secur. 124:102964, 2023) and DBLP listing; architecture/dataset details from the authors' GitHub README (fcdalgic/GramBeddings) and dataset page (web.cs.hacettepe.edu.tr/~selman/grambeddings-dataset/). Abstract text itself could not be retrieved.

## Problem
URL-only phishing detection with n-gram embeddings; release of a large, time-spanning dataset.

## Method
Three n-gram granularities embedded in parallel; each channel CNN -> LSTM -> attention; concatenated for classification.

## Dataset(s)
GramBeddings dataset (public via request form): 800,000 URLs, 400K phishing + 400K legitimate (custom crawler), collected May 2019-June 2021 (dataset page; TransURL Sec. 3)

## Features
Learned n-gram embeddings.

## Evaluation protocol
Not retrieved (publisher blocked)

## Metrics reported
Not retrieved from the paper (TransURL Fig. 5 reproduces GramBeddings results on its dataset).
(Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)

## Main findings
Multi-granular n-gram embeddings with attention are competitive; dataset spans 2+ years with weekly collection to reduce duplicates.

## Limitations
- Stated by authors: Not retrieved.
- Our own caveats: Legitimate URLs crawled from top sites; dataset access via form.

## Research gap
Cross-dataset tests appear only in follow-up work (TransURL).

## Relevance to our project
Largest recent public char-level benchmark (800k, 2019-2021); strong candidate external dataset and attention-based explainability precedent.

Relevance score: 4/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
