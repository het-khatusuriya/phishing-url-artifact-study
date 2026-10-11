# hu2021idnhomograph

## Citation
Hang Hu; Steve T. K. Jan; Yang Wang; Gang Wang (2021). *Assessing Browser-level Defense against IDN-based Phishing*. 30th USENIX Security Symposium, pp. 3739-3756. URL: https://www.usenix.org/conference/usenixsecurity21/presentation/hu-hang

## Verification
- Verified on 2026-10-11. Status: **yes**. Access: **full_text** (PDF: research/papers/hu2021idnhomograph.pdf).
- Evidence: USENIX presentation page (title, authors, affiliations, pages, PDF). PDF from usenix.org.

## Problem
How effective are browser defenses against IDN homograph phishing domains?

## Method
Generate homograph IDNs for popular domains, test display behaviour across browser versions, run a user study.

## Dataset(s)
Test cases generated from popular domains; not a URL classifier dataset.

## Features
n/a

## Evaluation protocol
Policy bypass rates per browser/version; user deception rates

## Metrics reported (only numbers present in the source)
All 7 browsers have rule weaknesses; Chrome reversed some rules over time; bypassing homographs remain highly deceptive to users (abstract; detailed rates in Sec. 5-6).

## Main findings
Punycode/IDN homographs still reach users; defenses inconsistent.

## Limitations
- Authors' stated limitations: Snapshot to April 2020.
- My assessment: Not about ML detection; relevant as threat model for homoglyph mutations.

## Research gap
ML URL detectors' handling of punycode (xn--) vs. Unicode rendering is rarely tested.

## Relevance to our project (score 4/5)
Justifies including homoglyph/punycode operators in our mutation suite and treating 'xn--' tokens explicitly in lexical features.

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
