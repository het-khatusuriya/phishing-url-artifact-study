"""Generate the full experiment matrix exactly as executed.

Outputs configs/matrix/*.yaml and three run lists:
  RUN_ORDER.txt        main matrix (corpora A and B; baseline28 / lexical_v2 / ablations / char models)
  RUN_ORDER_LOCO.txt   leave-one-corpus-out with lexical_v2 and lexical_v2 minus artifact columns
  RUN_ORDER_CANON.txt  canonicalised features (lexical_v2_canon), in-corpus and leave-one-corpus-out

Corpus A = phiusiil, Corpus B = lineage253k. Every run's actual configuration is
also saved in results/runs/<run_id>/config.json, which is authoritative.

Note on external sets: kaggle651k_bp (514k URLs, shares lineage with corpus B)
was scored only in the first two runs (A_b28_random, A_b28_grouped) and then
dropped from external evaluation to fit the CPU budget.
"""
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "configs" / "matrix"
OUT.mkdir(parents=True, exist_ok=True)

ALL_EXT = ["phiusiil", "lineage253k", "hannousse2021", "ebbu2017", "phishstorm", "iscx2016", "kaggle651k_bp",
           "phishtank", "urlhaus", "openphish"]
EARLY_RUNS_WITH_KAGGLE = {"A_b28_random", "A_b28_grouped"}
CORPORA6 = ["phiusiil", "lineage253k", "hannousse2021", "ebbu2017", "phishstorm", "iscx2016"]
TAB = ["lr", "rf", "xgb", "softvote"]
SEEDS5 = [42, 43, 44, 45, 46]
SEEDS3 = [42, 43, 44]
CHAR = {"epochs": 5, "batch_size": 256, "patience": 2, "threads": 8, "max_train_minutes": 20, "max_len": 160}
queues = {"RUN_ORDER.txt": [], "RUN_ORDER_LOCO.txt": [], "RUN_ORDER_CANON.txt": []}


def ext_for(run_id, dataset):
    ext = [d for d in ALL_EXT if d != dataset]
    if run_id not in EARLY_RUNS_WITH_KAGGLE:
        ext = [d for d in ext if d != "kaggle651k_bp"]
    return ext


def add(queue, run_id, dataset, feature_set, split, drop_art, models, seeds, external=None, extra=None):
    cfg = dict(run_id=run_id, dataset=dataset, feature_set=feature_set, drop_artifacts=drop_art, split=split,
               models=models, seeds=seeds, test_size=0.2, val_size=0.2, fpr_targets=[0.01, 0.001],
               external_tests=external if external is not None else ext_for(run_id, dataset))
    if extra:
        cfg.update(extra)
    (OUT / f"{run_id}.yaml").write_text(yaml.safe_dump(cfg, sort_keys=False))
    queues[queue].append(run_id)


# ---- main matrix ----
for corpus, tag in (("phiusiil", "A"), ("lineage253k", "B")):
    add("RUN_ORDER.txt", f"{tag}_b28_random", corpus, "baseline28", "random", False, TAB, SEEDS5)
    add("RUN_ORDER.txt", f"{tag}_b28_grouped", corpus, "baseline28", "grouped", False, TAB, SEEDS5)
    add("RUN_ORDER.txt", f"{tag}_b28noart_grouped", corpus, "baseline28", "grouped", True, TAB, SEEDS5)
    add("RUN_ORDER.txt", f"{tag}_v2_random", corpus, "lexical_v2", "random", False, TAB + ["lgbm"], SEEDS5)
    add("RUN_ORDER.txt", f"{tag}_v2_grouped", corpus, "lexical_v2", "grouped", False, TAB + ["lgbm"], SEEDS5)
    add("RUN_ORDER.txt", f"{tag}_v2noart_grouped", corpus, "lexical_v2", "grouped", True, TAB + ["lgbm"], SEEDS5)
add("RUN_ORDER.txt", "A_char_grouped", "phiusiil", "lexical_v2", "grouped", True,
    ["charcnn", "charcnn_canon", "charcnn_hybrid"], SEEDS3, extra={"charcnn": CHAR})
add("RUN_ORDER.txt", "B_char_grouped", "lineage253k", "lexical_v2", "grouped", True,
    ["charcnn", "charcnn_canon", "charcnn_hybrid"], [42], extra={"charcnn": CHAR})

# ---- leave-one-corpus-out ----
for held in CORPORA6:
    for rep, fs, drop in (("v2", "lexical_v2", False), ("v2noart", "lexical_v2", True)):
        add("RUN_ORDER_LOCO.txt", f"LOCO_{held}_{rep}", f"pool_minus_{held}", fs, "grouped", drop,
            ["lr", "rf", "xgb"], SEEDS3, external=[held, "phishtank"],
            extra={"notes": f"Leave-one-corpus-out: train on pool without {held}, test on {held}"})

# ---- canonicalised features ----
for corpus, tag in (("phiusiil", "A"), ("lineage253k", "B")):
    add("RUN_ORDER_CANON.txt", f"{tag}_v2canon_grouped", corpus, "lexical_v2_canon", "grouped", False,
        TAB + ["lgbm"], SEEDS5)
for held in CORPORA6:
    add("RUN_ORDER_CANON.txt", f"LOCO_{held}_v2canon", f"pool_minus_{held}", "lexical_v2_canon", "grouped", False,
        ["lr", "rf", "xgb"], SEEDS3, external=[held, "phishtank"],
        extra={"notes": f"Leave-one-corpus-out with canonical features; test on {held}"})

for q, runs in queues.items():
    (OUT / q).write_text("\n".join(runs) + "\n")
    print(q, len(runs), runs)
