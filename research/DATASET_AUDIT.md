# Dataset Audit

Date: 2026-10-11. Scripts: `scripts/prepare_external.py`, `scripts/build_canonical.py`, `scripts/analysis_dataset_artifacts.py`. Machine-readable outputs: `results/logs/dataset_report_<name>.json`, `results/tables/dataset_artifact_stats.csv`, `results/figures/dataset_artifacts.png`. Provenance of every file: `research/DATASET_SOURCES.md` and `data/external/<name>/SOURCE.md`.

## 1. The repository's own dataset (`data/raw/raw_data.csv`)

| Item | Finding |
|---|---|
| Availability | **Not in the repository** (data directory was intended to be gitignored); not supplied with the project. |
| Known facts (from notebook outputs) | 253,098 rows; `url,label`; legitimate 129,420 / phishing 123,678 (51.1 / 48.9 %); 0 duplicate URLs; 0 conflicting labels; https 72.2 %, http 27.8 %, ftp 8 URLs. |
| Origin | No published dataset with these counts exists on Kaggle, HuggingFace, Mendeley, Zenodo, UCI or IEEE DataPort (searched by counts, file name and first-row URLs). Four of the five first rows exist, *without scheme*, in the Kaggle `sid321axn` / `taruntiwarihp` lineage (ISCX-URL-2016 + PhishTank + PhishStorm) as re-uploaded on HuggingFace; the fifth (a 2020s Google-Docs phishing URL) exists in none of the 2014–2019 sets. Conclusion: a derived compilation — scheme-normalised, `www.`-prefixed URLs from the Kaggle lineage merged with a newer phishing feed. Collection dates unknown. (Details and confidence levels in `DATASET_SOURCES.md` §1.) |
| Label semantics | `phishing` vs `legitimate`; the project calls positives "malicious". Phishing is the only malicious category evidenced. |
| Class-conditional artifacts (from the author's own `feature_means_by_label.csv`) | https: 93.2 % (legit) vs 50.2 % (phish); mean subdomain count 1.20 vs 0.80 (i.e. `www.` far more common in legit); IP hosts 0.0 % vs 1.8 %; `excessive_hyphens` 14 % vs 3 % (legit higher — a sign of long crawled benign paths). |
| Timestamps | None. Temporal evaluation impossible on this file. |
| Action | The authors should supply `raw_data.csv` (and the originating link). Until then `phiusiil` is used as the main stand-in and `lineage253k` as a second training corpus with identical size and class balance. The commented-out `main` entry in `configs/datasets.yaml` re-enables the original the moment it is available. |

## 2. Canonical corpora built for this study

All corpora pass the same pipeline (§2 of `EXPERIMENT_PROTOCOL.md`). `kept` = rows after dropping missing/unmappable labels, normalisation-based deduplication and removal of conflicting-label URLs. `domains` = distinct registered domains (public-suffix aware) or IP literals.

| Corpus | Role | Raw rows | Kept | Malicious | Benign | Domains | Conflicts removed | Timestamps |
|---|---|---|---|---|---|---|---|---|
| `phiusiil` (UCI 967, CC BY 4.0) | **Corpus A** (main) | 235,795 | 234,687 | 99,838 | 134,849 | 175,508 | 1 | no |
| `lineage253k` (HF Mitake lineage, CC BY-SA 4.0; sample sized 129,420 / 123,678 like the original) | **Corpus B** | 253,098 | 252,394 | 123,095 | 129,299 | 130,453 | 1 | no |
| `hannousse2021` (Mendeley, CC BY 4.0) | external | 11,430 | 11,416 | 5,701 | 5,715 | 6,634 | 0 | no (May 2020) |
| `ebbu2017` (GitHub ebubekirbbr/pdd) | external | 73,575 | 54,721 | 24,811 | 29,910 | 21,606 | 0 | no (2017) |
| `phishstorm` (mirror) | external | 96,018 | 95,962 | 47,972 | 47,990 | 30,894 | 0 | no (2014) |
| `iscx2016` (mirror: benign + phishing lists) | external | 45,343 | 45,324 | 9,946 | 35,378 | 4,304 | 0 | no (2016) |
| `kaggle651k_bp` (sid321axn mirror, benign + phishing only) | external, **shares lineage with B and the original** | 522,214 | 514,031 | 90,015 | 424,016 | 145,482 | 3,940 | no |
| `phishtank` (verified online, 2026-10-11 dump) | positive-only, temporal | 67,621 | 67,326 | 67,326 | 0 | 12,971 | 0 | **2011-02 → 2026-10** |
| `urlhaus` (abuse.ch, malware URLs) | positive-only, out-of-task check | 72,849 | 72,847 | 72,847 | 0 | 17,585 | 0 | **2018-06 → 2026-10** |
| `openphish` (community feed, 2026-10-11) | positive-only sanity | 300 | 300 | 300 | 0 | 144 | 0 | no |

Note on PhiUSIIL labels: the UCI file encodes `label = 1` for **legitimate**; the canonical file inverts this so that 1 = phishing (checked: 100,945 raw phishing rows → 99,838 after dedup).

Ebbu2017 lost 26 % of rows to deduplication (12,322 duplicate phishing URLs in the upstream file). kaggle651k_bp had 3,940 normalised URLs carrying both labels; all were removed.

## 3. Collection artifacts, per class (from `dataset_artifact_stats.csv`)

| Corpus | Class | https | leading `www.` | homepage (empty path, no query) | IP host | median length | domains / URL |
|---|---|---|---|---|---|---|---|
| phiusiil | benign | **100.0 %** | **100.0 %** | **100.0 %** | 0.0 % | 27 | 0.98 |
| phiusiil | phishing | 48.4 % | 42.0 % | 71.8 % | 0.6 % | 34 | 0.44 |
| lineage253k | benign | 0 % (no scheme stored) | 8.2 % | 34.5 % | 0.0 % | 33 | 0.46 |
| lineage253k | phishing | 0 % | 23.4 % | 38.0 % | 2.1 % | 33 | 0.58 |
| hannousse2021 | benign | 44.5 % | 67.0 % | 38.4 % | 0.0 % | 41 | 0.70 |
| hannousse2021 | phishing | 33.3 % | 20.9 % | 18.4 % | 1.7 % | 55 | 0.47 |
| ebbu2017 | benign | 36.1 % | 59.1 % | 4.7 % | 0.0 % | 55 | 0.43 |
| ebbu2017 | phishing | 2.0 % | 26.2 % | 2.0 % | 0.6 % | 58 | 0.36 |
| phishstorm | benign | 2.2 % | 70.1 % | 0.0 % | 0.0 % | 44 | 0.36 |
| phishstorm | phishing | 1.4 % | 34.6 % | 0.0 % | 0.6 % | 62 | 0.29 |
| iscx2016 | benign | 5.5 % | **0.4 %** | 0.0 % | 0.0 % | 101 | **0.009** |
| iscx2016 | phishing | 1.7 % | 42.3 % | 3.4 % | 1.5 % | 68 | 0.40 |
| kaggle651k_bp | benign | 0.5 % | 3.0 % | 11.2 % | 0.0 % | 46 | 0.25 |
| kaggle651k_bp | phishing | 7.6 % | 40.1 % | 25.9 % | 0.4 % | 34 | 0.49 |
| phishtank (2011–2026) | phishing | 91.9 % | 4.2 % | 34.3 % | 0.1 % | 39 | 0.19 |
| urlhaus | malware | 37.9 % | 0.5 % | 0.3 % | 58.7 % | 35 | 0.24 |

Single-feature ROC-AUC of the artifacts (orientation: AUC < 0.5 means the feature is *more common in benign* URLs):

| Corpus | https | `www.` | homepage | length | IP host |
|---|---|---|---|---|---|
| phiusiil | 0.242 | 0.210 | 0.359 | 0.720 | 0.503 |
| lineage253k | 0.500 | 0.576 | 0.517 | 0.538 | 0.511 |
| hannousse2021 | 0.444 | 0.269 | 0.400 | 0.665 | 0.509 |
| ebbu2017 | 0.329 | 0.335 | 0.486 | 0.547 | 0.503 |
| phishstorm | 0.496 | 0.323 | 0.500 | 0.730 | 0.503 |
| iscx2016 | 0.481 | **0.710** | 0.517 | **0.244** | 0.508 |
| kaggle651k_bp | 0.536 | **0.685** | 0.574 | 0.355 | 0.502 |

### Interpretation

1. **The direction of the `www.` and length artifacts flips between corpora.** In PhiUSIIL, Hannousse, Ebbu2017 and PhishStorm, `www.` indicates *benign* (AUC 0.21–0.34); in ISCX-2016 and the Kaggle lineage it indicates *phishing* (AUC 0.69–0.71). Long URLs are phishing in PhiUSIIL/PhishStorm (AUC 0.72–0.73) but benign in ISCX-2016 (0.24), whose benign list consists of deep crawled paths from only ~300 sites (0.009 domains per URL). A classifier that learns either sign will fail on the corpora of the opposite sign — this is the mechanism behind cross-dataset collapse reported in the literature and is testable here (RQ1/RQ2).
2. **PhiUSIIL's benign class is a degenerate population**: every benign URL is `https://www.<domain>` with no path. Any model trained on it learns "path present ⇒ suspicious" and "no `www.` ⇒ suspicious". The project's original dataset, built with the same `https://www.` normalisation of benign homepages, shares this property (93 % https, `www.` prevalent), which explains the audit's `https://google.com/ → malicious` failure.
3. **ISCX-2016 benign URLs come from ~300 domains** (35,378 URLs, 4,304 registered domains overall and only 0.4 % `www.`), so random splits leak domains massively; grouped splitting is mandatory there.
4. **The present-day phishing population (PhishTank 2026) is 92 % https with 4 % `www.`**, i.e. it looks like PhiUSIIL's *benign* class on the scheme feature and unlike PhiUSIIL's phishing class. A model that relies on `https` as a benign indicator should lose recall on current phishing; this is measured by scoring `phishtank` by submission month (temporal recall).
5. `kaggle651k_bp` and `lineage253k` store URLs without scheme, so scheme features are constant there; models trained on scheme-bearing corpora see an out-of-vocabulary condition on these sets (`had_explicit_scheme = 0`), which is itself a realistic deployment variant (URLs copied from logs or e-mail text without scheme).

## 4. Leakage and quality checks performed

| Check | Result |
|---|---|
| Exact / normalised duplicates across partitions | Impossible by construction (dedup before splitting; asserted in tests). |
| Conflicting labels | Removed (counts above). |
| Registered-domain overlap between train and test | Quantified for every split in `results/runs/<run>/split_<seed>.json` → `meta.overlap`; zero for grouped splits by construction. |
| Unavailable / dead URLs | Not checked — this is an offline lexical study; liveness is irrelevant to the label definition used by the sources. |
| Mislabeled records | Not individually audited; known-noisy sources (Kaggle lineage, PhishStorm mirror) are used only as external tests, never as the primary test for claims. |
| Source leakage inside a corpus | Yes — documented above (per-class scheme/`www`/path artifacts). Addressed by artifact-ablation runs and external tests rather than by filtering, because filtering would hide the phenomenon under study. |
| Near-duplicates / URL variants | Grouped splits remove the dominant variant family (same registered domain). Template-level near-duplicates across domains (phishing kits) remain and are a known limitation. |
| Timestamps | Only PhishTank and URLhaus; both positive-only. Their timestamps are submission/report times, which are trustworthy for ordering. |

## 5. Consequences for the experimental design

- Primary claims are made on **grouped** splits of Corpus A and B, with **external** evaluation on Hannousse 2021 (independent, balanced, 2020), Ebbu2017, PhishStorm and ISCX-2016, and **positive-only temporal recall** on PhishTank by month.
- `kaggle651k_bp` is reported but flagged as lineage-overlapping with Corpus B and (probably) the original data.
- Precision at realistic prevalence is derived analytically from TPR/FPR at the chosen thresholds (base rates 1 %, 0.1 %) rather than by subsampling, following the literature's base-rate guidance.
