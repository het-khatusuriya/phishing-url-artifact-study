"""Generate the experiment matrix (configs/matrix/*.yaml) + an ordered run list.

Matrix (all protocols are defined in research/EXPERIMENT_PROTOCOL.md):
  Corpus A = phiusiil (main stand-in for the project's dataset)
  Corpus B = lineage253k (Kaggle/HF lineage sample with the original's size and balance)
  Feature sets: baseline28, lexical_v2, each with/without artifact features
  Splits: random, grouped
  External tests: every other corpus (incl. positive-only PhishTank / URLhaus for recall)
"""
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "configs" / "matrix"
OUT.mkdir(parents=True, exist_ok=True)

ALL = ["phiusiil", "lineage253k", "hannousse2021", "ebbu2017", "phishstorm", "iscx2016", "kaggle651k_bp",
       "phishtank", "urlhaus", "openphish"]
TAB_MODELS = ["lr", "rf", "xgb", "softvote"]
SEEDS5 = [42, 43, 44, 45, 46]
runs = []


def add(run_id, dataset, feature_set, split, drop_art, models, seeds, extra=None):
    cfg = dict(run_id=run_id, dataset=dataset, feature_set=feature_set, drop_artifacts=drop_art, split=split,
               models=models, seeds=seeds, test_size=0.2, val_size=0.2, fpr_targets=[0.01, 0.001],
               external_tests=[d for d in ALL if d != dataset])
    if extra:
        cfg.update(extra)
    (OUT / f"{run_id}.yaml").write_text(yaml.safe_dump(cfg, sort_keys=False))
    runs.append(run_id)


for corpus, tag in (("phiusiil", "A"), ("lineage253k", "B")):
    # E1/E2: faithful baseline features, random vs grouped
    add(f"{tag}_b28_random", corpus, "baseline28", "random", False, TAB_MODELS, SEEDS5)
    add(f"{tag}_b28_grouped", corpus, "baseline28", "grouped", False, TAB_MODELS, SEEDS5)
    # E3: artifact ablation on baseline features
    add(f"{tag}_b28noart_grouped", corpus, "baseline28", "grouped", True, TAB_MODELS, SEEDS5)
    # E4-E6: improved features
    add(f"{tag}_v2_random", corpus, "lexical_v2", "random", False, TAB_MODELS + ["lgbm"], SEEDS5)
    add(f"{tag}_v2_grouped", corpus, "lexical_v2", "grouped", False, TAB_MODELS + ["lgbm"], SEEDS5)
    add(f"{tag}_v2noart_grouped", corpus, "lexical_v2", "grouped", True, TAB_MODELS + ["lgbm"], SEEDS5)
    # E7: character models (3 seeds, CPU budget)
    add(f"{tag}_char_grouped", corpus, "lexical_v2", "grouped", True, ["charcnn", "charcnn_hybrid"], [42, 43, 44],
        extra={"charcnn": {"epochs": 8, "batch_size": 256, "patience": 2, "threads": 10, "max_train_minutes": 40}})

(ROOT / "configs" / "matrix" / "RUN_ORDER.txt").write_text("\n".join(runs) + "\n")
print("\n".join(runs))
