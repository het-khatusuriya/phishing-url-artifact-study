# Research Plan

Project: Malicious URL detection — from a course-project baseline to an evidence-backed conference paper.
Start: 2026-10-11. Branch: `research-v2`. Baseline preserved on `main`.

## Working research question (provisional until Phase 3 is complete)

The audit (`REPOSITORY_AUDIT.md` §7) shows that the baseline ensemble's two most influential features (`https_usage`, `www`-driven `num_subdomains`) describe *how the benign and phishing URLs were collected*, and that the model consequently calls `https://google.com/` malicious. The provisional question is therefore:

> **RQ1.** How much of the reported performance of lexical URL classifiers on common phishing benchmarks is attributable to collection artifacts and domain memorisation rather than to transferable indicators of maliciousness?
> **RQ2.** Does an evaluation protocol that (a) groups by registered domain, (b) removes/neutralises artifact features and (c) tests on externally collected data change the ranking of model families (linear, tree ensembles, soft-vote hybrid, character CNN, hybrid char+lexical)?
> **RQ3.** Can an artifact-aware training recipe (artifact-neutral features + grouped model selection + validation-based operating thresholds + calibration) retain in-distribution performance while improving external-dataset performance and calibration?

These are refined in `RESEARCH_GAPS.md` after the literature review.

## Phases and status

| Phase | Deliverable | Status |
|---|---|---|
| 1.1 Audit | `research/REPOSITORY_AUDIT.md` | done |
| 1.2 Baseline reproduction | `results/runs/baseline28_random/` | blocked on raw dataset; harness ready |
| 2 Literature | `research/papers/`, `paper_metadata.csv`, `reading_notes/`, `LITERATURE_REVIEW.md`, `references.bib` | in progress (3 collection agents) |
| 3 Gaps | `research/RESEARCH_GAPS.md` | pending literature |
| 4 Data & protocol | `research/DATASET_AUDIT.md`, `EXPERIMENT_PROTOCOL.md`, `data/processed/canonical/*.parquet` | in progress (dataset agent) |
| 5 Implementation | `src/urlresearch/`, `scripts/`, `tests/` | core done (87 tests pass) |
| 6 Experiments | `results/runs/*` | pending data |
| 7 Figures/tables | `results/figures`, `results/tables`, `scripts/make_figures.py` | pending |
| 8 Manuscript | `paper/manuscript.md` | skeleton |
| 9 Reproducibility | README, requirements, checks | partial (requirements.txt written) |

## Task tracker

| # | Task | Pri | RQ | Depends on | Files | Impl | Test/validation | Results | Remaining limitation | Next action |
|---|---|---|---|---|---|---|---|---|---|---|
| T1 | Repository audit | P0 | — | — | research/REPOSITORY_AUDIT.md | done | n/a | audit doc | — | — |
| T2 | Literature collection (3 themes) | P0 | all | — | research/papers, reading_notes, paper_metadata_L*.csv, references_L*.bib | running | manual DOI verification | — | OA availability | merge CSVs, write LITERATURE_REVIEW.md |
| T3 | Obtain datasets | P0 | all | — | data/external/*, research/DATASET_SOURCES.md | running | profile.txt per dataset | — | original raw_data.csv missing | ask user for raw_data.csv; build canonical parquet |
| T4 | Safe URL parser + lexical_v2 + baseline28 wrapper | P0 | RQ1-3 | — | src/urlresearch/features/* | done | tests/test_feature_extractor.py (pass) | — | feature lists are heuristic | document in EXPERIMENT_PROTOCOL |
| T5 | Dataset loader, dedup, grouping, splits | P0 | RQ1-2 | — | src/urlresearch/data/* | done | tests/test_data_cleaning.py (pass) | — | temporal split requires timestamps | — |
| T6 | Metrics, CIs, paired tests, calibration | P0 | all | — | src/urlresearch/evaluation/metrics.py | done | tests/test_model_evaluator.py (pass) | — | — | add reliability plot script |
| T7 | Model factories (LR/RF/XGB/LGBM/vote/stack), char-CNN | P1 | RQ2 | T4 | src/urlresearch/models/* | done | tests/test_model_training.py (pass) | — | no transformer baseline (CPU only) | — |
| T8 | Experiment runner + CLI + configs | P1 | all | T4-T7 | src/urlresearch/experiments/runner.py, scripts/run_experiment.py, configs/ | done | smoke tests on synthetic data (pass) | — | — | run on real data |
| T9 | Baseline reproduction run | P0 | RQ1 | T3 | results/runs/baseline28_random | pending | compare to results/metrics/final_test_metrics.csv | — | dataset | — |
| T10 | Artifact/shortcut analysis | P1 | RQ1 | T9 | scripts/analysis_artifacts.py | pending | — | — | — | — |
| T11 | Grouped + external + ablation experiments | P1 | RQ2-3 | T9 | results/runs/* | pending | — | — | — | — |
| T12 | Calibration, thresholds, robustness mutations, SHAP, errors | P2 | RQ3 | T11 | scripts/analysis_*.py | pending | — | — | — | — |
| T13 | Figures and tables | P2 | all | T11-12 | scripts/make_figures.py | pending | — | — | — | — |
| T14 | Manuscript | P3 | all | T2, T11-13 | paper/manuscript.md | skeleton | citation cross-check | — | — | — |
| T15 | README, reproducibility checks | P3 | — | all | README.md | pending | run documented commands | — | — | — |
