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
