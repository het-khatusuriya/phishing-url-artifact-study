# Progress Log

## 2026-10-11

- Cloned repository (single commit `65364b4`), created branch `research-v2`.
- Full audit of code, notebooks (with stored outputs) and results → `REPOSITORY_AUDIT.md`.
  Key finding: the ensemble's top SHAP features are collection artifacts (`https_usage`, `www`-driven subdomain count); `https://google.com/` is predicted malicious at 88 %. Raw dataset and trained models are absent from the repository.
- Environment: Python 3.10.11, Windows 11, 12 CPU cores, no GPU. Installed shap, lightgbm, pytest, pyarrow. `requirements.txt` written.
- Implemented `src/urlresearch/`: safe URL parser (never raises), `baseline28` wrapper + `lexical_v2` features (public-suffix aware), dataset loader with normalisation-based dedup and conflict removal, random / registered-domain-grouped / temporal splits with overlap reports, security metrics (FPR/FNR/TPR@FPR/ECE/Brier), bootstrap CIs, paired bootstrap and McNemar tests, model factories (LR, RF, XGB, LightGBM, soft vote, stacking), char-CNN and hybrid char+lexical model, config-driven runner with validation-only threshold policies, resource measurements and persisted predictions.
- Tests: 87 passing (`python -m pytest tests -q`).
- Launched literature collection (3 themes) and dataset acquisition agents.
- Pending: datasets, literature merge, baseline reproduction, gap document, experiments.

## 2026-10-11 (evening)

- Literature: three collection agents finished; merged into `paper_metadata.csv` and `references.bib` (111 unique verified sources after removing 3 same-DOI duplicates), 114 reading notes, `LITERATURE_REVIEW.md`, `LITERATURE_SURVEY_TABLE.md`. Citations in the review and manuscript all resolve to the bibliography (checked by script).
- Datasets: 10 sources downloaded and profiled (`DATASET_SOURCES.md`); 10 canonical corpora + 6 leave-one-corpus-out pools built; `DATASET_AUDIT.md` written. Original `raw_data.csv` remains unavailable; provenance traced to the Kaggle/HF lineage plus a newer phishing source.
- Probe (Table T10): benign source corpus identifiable at 0.83 accuracy with `lexical_v2` (chance 0.17); 0.81 after dropping artifact columns; 0.62 after canonicalisation. → added `lexical_v2_canon` and `charcnn_canon` (post hoc, logged in DECISIONS.md and EXPERIMENT_PROTOCOL.md).
- Original pipeline code re-executed unchanged on both substitute corpora (`results/reproduction/`). Found a defect: the original extractor does not parse hosts of scheme-less URLs (audit §3; regression test added).
- Experiment queues running: main matrix (14 runs), LOCO (12 runs); canonical queue (8 runs) starts when LOCO ends.
- PDF incident: while removing licence-restricted PDFs from the unpushed branch history, `git filter-branch` deleted `research/papers/` from disk; 36 PDFs restored from download caches, all 44 others re-downloaded from the same legal sources and verified. PDFs are now git-ignored.
