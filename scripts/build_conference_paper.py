"""Build the single, self-contained conference paper as a Word document.

Input : paper/conference_paper.md (text with <<FIG|...>> / <<TABLE|...>> markers)
        research/survey_curated.csv, research/references.bib
        results/runs/*/metrics.csv|resources.csv, results/tables/*.csv, results/figures/*.png
Output: paper/Phishing_URL_Detection_Conference_Paper.docx

Every table is computed here from saved result files; nothing numeric is typed by hand.
Usage: python scripts/build_conference_paper.py
"""
import csv
import json
import re
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import docx_helpers as H  # noqa: E402
from docx.enum.text import WD_ALIGN_PARAGRAPH  # noqa: E402
from docx.shared import Cm, Pt  # noqa: E402

ROOT, FIG, TAB, RUNS = H.ROOT, H.FIG, H.TAB, ROOT_RUNS = (H.ROOT, H.FIG, H.TAB, H.ROOT / "results" / "runs")
doc = H.doc
OUT = ROOT / "paper" / "Phishing_URL_Detection_Conference_Paper.docx"
W = H.PORTRAIT_TEXT_WIDTH
MODEL = {"lr": "LR", "rf": "RF", "xgb": "XGBoost", "softvote": "Soft vote 1:2:2"}
CORP = {"phiusiil": "PhiUSIIL", "lineage253k": "Corpus B", "hannousse2021": "Hannousse 2021", "ebbu2017": "Ebbu2017",
        "phishstorm": "PhishStorm", "iscx2016": "ISCX-2016", "kaggle651k_bp": "Kaggle 651k", "phishtank": "PhishTank",
        "urlhaus": "URLhaus", "openphish": "OpenPhish"}
INDEP = ["hannousse2021", "ebbu2017", "phishstorm", "iscx2016"]


def metrics(run):
    p = RUNS / run / "metrics.csv"
    return pd.read_csv(p) if p.exists() else None


def f3(x):
    return "—" if x is None or pd.isna(x) else f"{x:.3f}"


def table(caption, header, rows, font=7.5, weights=None):
    H.table_caption(caption)
    H.add_table(header, rows, W, font=font, col_weights=weights)


# ----------------------------------------------------------------------------- table builders
def t_survey(cap):
    rows = []
    for r in csv.DictReader(open(ROOT / "research/survey_curated.csv", encoding="utf-8")):
        e = H.BIB[r["citekey"]]
        first = H.clean_tex(e.get("author", "")).split(" and ")[0]
        first = first.split(",")[0] if "," in first else first.split()[-1]
        rows.append([f"[{r['citekey']}]", f"{first} et al. ({H.clean_tex(e.get('year', ''))})" if " and " in e.get("author", "") else f"{first} ({H.clean_tex(e.get('year', ''))})",
                     r["approach"], r["data"], r["evaluation"], r["reported_result"], r["limitation"]])
    table(cap, ["Ref.", "Study", "Approach", "Data", "Evaluation", "Reported result", "Limitation for our question"], rows,
          font=7, weights=[5, 9, 16, 15, 13, 16, 15])


def t_T2(cap):
    d = pd.read_csv(TAB / "paper_T2.csv")
    d["data"] = d["data"].str.replace("original raw_data.csv (stored result, not re-run)", "Original data (stored)", regex=False)
    d["data"] = d["data"].str.replace(" (original code re-run)", " (re-run)", regex=False).str.replace("lineage253k", "Corpus B").str.replace("phiusiil", "PhiUSIIL")
    d["model"] = d["model"].replace({"Weighted Soft-Voting Ensemble": "Soft vote 1:2:2", "Logistic Regression": "LR", "Random Forest": "RF"})
    rows = [[r.data, r.model, f"{r.accuracy:.4f}", f"{r.precision:.4f}", f"{r.recall:.4f}", f"{r.f1:.4f}", r.roc_auc if isinstance(r.roc_auc, str) else f"{float(r.roc_auc):.4f}"] for r in d.itertuples()]
    table(cap, ["Data", "Model", "Accuracy", "Precision", "Recall", "F1", "ROC-AUC"], rows, weights=[14, 10, 7, 7, 7, 7, 8])


def t_T1(cap):
    d = pd.read_csv(TAB / "paper_T1.csv")
    order = ["phiusiil", "lineage253k", "hannousse2021", "ebbu2017", "phishstorm", "iscx2016", "kaggle651k_bp", "phishtank", "urlhaus", "openphish"]
    d = d.set_index("corpus").reindex(order).reset_index()
    role = {"phiusiil": "training (A)", "lineage253k": "training (B)", "kaggle651k_bp": "external*", "phishtank": "feed", "urlhaus": "feed (malware)", "openphish": "feed"}
    rows = [[CORP[r.corpus], role.get(r.corpus, "external"), f"{int(r.raw):,}", f"{int(r.kept):,}", f"{int(r.malicious):,}", f"{int(r.benign):,}",
             f"{int(r.reg_domains):,}", f"{r.https:.2f}", f"{r.www:.2f}", r.timestamps.replace("→", " to ")] for r in d.itertuples()]
    table(cap, ["Corpus", "Role", "Raw", "Kept", "Malicious", "Benign", "Reg. domains", "https", "www.", "Timestamps"], rows,
          font=7, weights=[10, 9, 7, 7, 7, 7, 7, 5, 5, 11])


RUN_DESC = [
    ("A_b28_random", "Corpus A, original features, random split"),
    ("A_b28_grouped", "Corpus A, original features, grouped split"),
    ("A_b28noart_grouped", "Corpus A, original features minus artifact columns, grouped"),
    ("LOCO_phiusiil_v2", "LOCO, PhiUSIIL held out, lexical_v2"),
    ("LOCO_phiusiil_v2noart", "LOCO, PhiUSIIL held out, lexical_v2 minus artifact columns"),
    ("LOCO_lineage253k_v2", "LOCO, corpus B held out, lexical_v2"),
    ("LOCO_lineage253k_v2noart", "LOCO, corpus B held out, lexical_v2 minus artifact columns"),
    ("LOCO_hannousse2021_v2", "LOCO, Hannousse 2021 held out, lexical_v2"),
    ("LOCO_hannousse2021_v2noart", "LOCO, Hannousse 2021 held out, lexical_v2 minus artifact columns"),
]


def t_runs(cap):
    rows = []
    for rid, desc in RUN_DESC:
        m = metrics(rid)
        if m is None:
            continue
        seeds = m.groupby("model").seed.nunique()
        ext = sorted({e.split(":")[1] for e in m.eval_set.unique() if e.startswith("external:")})
        rows.append([rid, desc, ", ".join(MODEL[x] for x in seeds.index), "–".join(sorted({str(v) for v in [seeds.min(), seeds.max()]})),
                     ", ".join(CORP[e] for e in ext)])
    table(cap, ["Run", "Description", "Models", "Seeds", "Evaluated on (besides own test split)"], rows, font=7, weights=[17, 18, 11, 4, 17])


def t_probe(cap):
    d = pd.read_csv(TAB / "paper_T10.csv")
    lab = lambda r: "lexical_v2 minus artifact columns" if r["drop_artifacts"] else {"lexical_v2": "lexical_v2", "lexical_v2_canon": "lexical_v2_canon (canonicalised)", "baseline28": "original 28 features"}[r["feature_set"]]
    d["rep"] = d.apply(lab, axis=1)
    order = ["original 28 features", "lexical_v2", "lexical_v2 minus artifact columns", "lexical_v2_canon (canonicalised)"]
    rows = []
    for cls in ("benign", "malicious"):
        for rep in order:
            r = d[(d["class"] == cls) & (d.rep == rep)]
            if len(r):
                r = r.iloc[0]
                rows.append([cls, rep, f3(r.accuracy)] + [f3(r[c]) for c in ["phiusiil", "lineage253k", "hannousse2021", "ebbu2017", "phishstorm", "iscx2016"]])
    table(cap, ["Class", "Representation", "Accuracy", "PhiUSIIL", "Corpus B", "Hannousse", "Ebbu2017", "PhishStorm", "ISCX-2016"], rows,
          weights=[7, 18, 7, 7, 7, 7, 7, 7, 7])


def t_paired(cap):
    d = pd.read_csv(TAB / "paired_tests_A_b28_grouped.csv")
    rows = [[MODEL[r.model], f"{r.roc_auc_delta:+.5f} [{r.roc_auc_ci_lo:+.5f}, {r.roc_auc_ci_hi:+.5f}]",
             f"{r.f1_delta:+.4f} [{r.f1_ci_lo:+.4f}, {r.f1_ci_hi:+.4f}]", f"{int(r.mcnemar_n01)} / {int(r.mcnemar_n10)}",
             f"{r.mcnemar_p:.3f}" if r.mcnemar_p >= 0.001 else "< 0.001"] for r in d.itertuples()]
    table(cap, ["Model vs XGBoost", "Δ ROC-AUC [95 % CI]", "Δ F1 [95 % CI]", "Only model / only XGBoost correct", "McNemar p"], rows,
          weights=[10, 18, 16, 12, 7])


def ext_stats(run, mo, e):
    m = metrics(run)
    g = m[(m.model == mo) & (m.eval_set == f"external:{e}") & (m.policy == "val_fpr0.01")]
    return g.roc_auc.mean(), g.fpr.mean(), g.recall.mean(), m[m.model == mo].seed.nunique()


def test_auc(run, mo):
    m = metrics(run)
    return m[(m.model == mo) & (m.eval_set == "test") & (m.policy == "t0.5")].roc_auc.mean()


def t_ext(cap):
    sets = INDEP + ["lineage253k"]
    rows = []
    for mo in ("lr", "rf", "xgb", "softvote"):
        row = [MODEL[mo], f3(test_auc("A_b28_grouped", mo))]
        for e in sets:
            auc, fpr, _, _ = ext_stats("A_b28_grouped", mo, e)
            row.append(f"{f3(auc)} / {f3(fpr)}")
        row.append(f3(ext_stats("A_b28_grouped", mo, "phishtank")[2]))
        rows.append(row)
    table(cap + " Cells: ROC-AUC / FPR.", ["Model", "Test ROC-AUC"] + [CORP[e] for e in sets] + ["PhishTank recall"], rows,
          font=7.5, weights=[9, 7, 9, 9, 9, 9, 9, 7])


def t_abl(cap):
    sets = INDEP + ["lineage253k"]
    rows = []
    for mo in ("lr", "rf", "xgb", "softvote"):
        row = [MODEL[mo], f"{f3(test_auc('A_b28_grouped', mo))} → {f3(test_auc('A_b28noart_grouped', mo))}"]
        for e in sets:
            a1, f1_, _, _ = ext_stats("A_b28_grouped", mo, e); a2, f2_, _, _ = ext_stats("A_b28noart_grouped", mo, e)
            row.append(f"{f3(a1)} → {f3(a2)}" + chr(10) + f"{f3(f1_)} → {f3(f2_)}")
        rows.append(row)
    table(cap + " Each cell: value with all 28 features → value without the two artifact columns; first line ROC-AUC, second line FPR.",
          ["Model", "Test ROC-AUC"] + [CORP[e] for e in sets], rows, font=7.5, weights=[9, 10, 10, 10, 10, 10, 10])


def t_loco(cap):
    rows = []
    for held in ["phiusiil", "lineage253k", "hannousse2021", "ebbu2017", "phishstorm", "iscx2016"]:
        for rep, lab in (("v2", "lexical_v2"), ("v2noart", "minus artifact cols"), ("v2canon", "canonicalised")):
            m = metrics(f"LOCO_{held}_{rep}")
            if m is None:
                continue
            for mo in ("lr", "rf", "xgb"):
                g = m[m.model == mo]
                if g.empty:
                    continue
                t = g[(g.eval_set == "test") & (g.policy == "t0.5")]
                e = g[(g.eval_set == f"external:{held}") & (g.policy == "val_fpr0.01")]
                p = g[(g.eval_set == "external:phishtank") & (g.policy == "val_fpr0.01")]
                rows.append([CORP[held], lab, MODEL[mo], str(g.seed.nunique()), f3(t.roc_auc.mean()), f3(e.roc_auc.mean()),
                             f3(e.recall.mean()), f3(e.fpr.mean()), f3(p.recall.mean())])
    table(cap, ["Held-out corpus", "Representation", "Model", "Seeds", "Pool test AUC", "Held-out AUC", "Held-out recall",
                "Held-out FPR", "PhishTank recall"], rows, weights=[9, 11, 6, 4, 7, 7, 7, 7, 7])


def t_cal(cap):
    d = pd.read_csv(TAB / "calibration_A_b28_grouped.csv")
    rows = []
    for mo in ("lr", "rf", "xgb", "softvote"):
        for c, lab in (("none", "none"), ("isotonic", "isotonic"), ("platt", "Platt")):
            g = d[(d.model == mo) & (d.calibration == c)]
            t = g[g.eval_set == "test"]; x = g[g.eval_set.isin(INDEP)]
            rows.append([MODEL[mo], lab, f3(t.ece.mean()), f3(x.ece.mean()), f3(t["fpr_at_val_fpr0.01"].mean()),
                         f3(x["fpr_at_val_fpr0.01"].mean()), f3(t["recall_at_val_fpr0.01"].mean())])
    table(cap, ["Model", "Calibration", "ECE test", "ECE external (mean of 4)", "FPR test", "FPR external (mean of 4)", "Recall test"],
          rows, weights=[10, 8, 7, 10, 7, 10, 7])


def t_mut(cap):
    d = pd.concat([pd.read_csv(p) for p in sorted(TAB.glob("mutations_*.csv"))])
    names = {"upper_host": "Upper-case scheme and host", "trailing_slash": "Slash on empty path", "default_port": "Explicit default port",
             "encode_path_char": "Percent-encode a path letter", "add_fragment": "Add a fragment", "toggle_www": "Toggle leading www.",
             "toggle_scheme": "Toggle http/https", "add_utm_query": "Append tracking parameter"}
    rows = []
    for mu, nm in names.items():
        a = d[(d.run_id == "A_b28_grouped") & (d.model == "xgb") & (d.mutation == mu)].iloc[0]
        l = d[(d.run_id == "A_b28_grouped") & (d.model == "lr") & (d.mutation == mu)].iloc[0]
        p = d[(d.run_id == "LOCO_phiusiil_v2") & (d.model == "xgb") & (d.mutation == mu)].iloc[0]
        rows.append([nm, a.tier, f"{a.share_applicable * 100:.0f} %", f"{a.flip_rate_benign * 100:.1f} / {a.flip_rate_malicious * 100:.1f}",
                     f"{l.flip_rate_benign * 100:.1f} / {l.flip_rate_malicious * 100:.1f}", f"{a.auc_before:.3f} → {a.auc_after:.3f}",
                     f"{p.flip_rate_benign * 100:.1f} / {p.flip_rate_malicious * 100:.1f}", f"{p.auc_before:.3f} → {p.auc_after:.3f}"])
    table(cap, ["Transformation", "Tier", "Applies to (corpus A)", "XGBoost A: flips benign / malicious (%)", "LR A: flips (%)",
                "XGBoost A: ROC-AUC", "XGBoost pooled: flips (%)", "XGBoost pooled: ROC-AUC"], rows,
          font=7, weights=[14, 4, 7, 11, 9, 10, 10, 10])


def t_cost(cap):
    r = pd.read_csv(RUNS / "A_b28_random" / "resources.csv")
    g = r.groupby("model")[["fit_seconds", "predict_latency_ms_per_url", "model_size_bytes"]].median()
    def size(b):
        return f"{b / 1e3:.0f} kB" if b < 1e6 else f"{b / 1e6:.1f} MB"
    rows = [[MODEL[mo], f"{g.loc[mo, 'fit_seconds']:.1f}", f"{g.loc[mo, 'predict_latency_ms_per_url']:.4f}", size(g.loc[mo, "model_size_bytes"])]
            for mo in ("lr", "xgb", "rf", "softvote")]
    table(cap, ["Model", "Training time (s, 140k URLs)", "Scoring latency (ms / URL, batch)", "Model size"], rows, weights=[10, 10, 10, 8])


TABLES = {"SURVEY": t_survey, "T2": t_T2, "T1": t_T1, "RUNS": t_runs, "T10": t_probe, "PAIRED": t_paired, "EXT": t_ext,
          "ABL": t_abl, "LOCO": t_loco, "CAL": t_cal, "MUT": t_mut, "COST": t_cost}


def on_table(arg):
    key, cap = arg.split("|", 1)
    TABLES[key](cap)


def on_fig(arg):
    f, cap = arg.split("|", 1)
    H.add_figure(FIG / f, cap)


# ----------------------------------------------------------------------------- assemble
md = (ROOT / "paper/conference_paper.md").read_text(encoding="utf-8")
title = re.search(r"^# (.+)$", md, re.M).group(1)
abstract = re.search(r"## Abstract\s*\n(.*?)\n\*\*Index Terms\*\*", md, re.S).group(1).strip()
terms = re.search(r"\*\*Index Terms\*\*\s*—\s*(.+)", md).group(1).strip()
body = md[md.index("## I. Introduction"):]

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(10)
r = p.add_run(title); r.bold = True; r.font.size = Pt(17)
for line, size in (("[Author Name(s)]", 11), ("[Department, Institution, City, Country]", 10), ("[e-mail address]", 10)):
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
    p.add_run(line).font.size = Pt(size)
doc.add_paragraph()
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
r = p.add_run("Abstract—"); r.bold = True; r.italic = True
H.add_inline(p, abstract, base_bold=True, size=10)
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
r = p.add_run("Index Terms—"); r.bold = True; r.italic = True
H.add_inline(p, terms, base_italic=True, size=10)

H.render_md(body, heading_offset=-1, handlers={"FIG": on_fig, "TABLE": on_table})

doc.add_heading("References", level=1)
for n, key in enumerate(H.CITE_ORDER, 1):
    q = doc.add_paragraph()
    q.paragraph_format.left_indent = Cm(0.9); q.paragraph_format.first_line_indent = Cm(-0.9)
    q.paragraph_format.space_after = Pt(2)
    rr = q.add_run(f"[{n}] "); rr.font.size = Pt(9)
    rr = q.add_run(H.fmt_reference(H.BIB[key])); rr.font.size = Pt(9)

H.footer_page_numbers(doc.sections[0])
doc.save(OUT)
print("saved", OUT, "| figures", H.FIG_N[0], "| tables", H.TAB_N[0], "| references", len(H.CITE_ORDER))
