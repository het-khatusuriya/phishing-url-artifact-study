"""Convert the heterogeneous files under data/external/ into uniform CSVs
(url,label[,timestamp]) under data/interim/.  Read-only on data/external.

Run with:  python -I scripts/prepare_external.py
"""
import csv
import json
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
EXT = ROOT / "data" / "external"
OUT = ROOT / "data" / "interim"
OUT.mkdir(parents=True, exist_ok=True)
ORIG_N_LEGIT, ORIG_N_PHISH = 129_420, 123_678   # class counts of the original raw_data.csv


def write(name, df):
    df.to_csv(OUT / f"{name}.csv", index=False)
    print(f"{name}: {len(df)} rows, label counts {df['label'].value_counts().to_dict()}")


def phiusiil():
    df = pd.read_csv(EXT / "phiusiil" / "PhiUSIIL_Phishing_URL_Dataset.csv", usecols=["URL", "label"], encoding="utf-8")
    # PhiUSIIL convention: 1 = legitimate, 0 = phishing  -> invert
    df = pd.DataFrame({"url": df["URL"], "label": (df["label"] == 0).astype(int)})
    write("phiusiil", df)


def hannousse():
    df = pd.read_csv(EXT / "hannousse2021" / "dataset_B_05_2020.csv", usecols=["url", "status"])
    write("hannousse2021", pd.DataFrame({"url": df.url, "label": (df.status == "phishing").astype(int)}))


def ebbu():
    rows = []
    for fn, lbl in (("data_legitimate_36400.json", 0), ("data_phishing_37175.json", 1)):
        urls = json.loads((EXT / "ebbu2017" / fn).read_text(encoding="utf-8"))
        rows += [{"url": u, "label": lbl} for u in urls]
    write("ebbu2017", pd.DataFrame(rows))


def lines(path):
    return [l.strip() for l in path.read_text(encoding="utf-8", errors="replace").splitlines() if l.strip()]


def phishstorm():
    d = EXT / "phishstorm_mirror"
    rows = [{"url": u, "label": 0} for u in lines(d / "valid-urls.csv")] + \
           [{"url": u, "label": 1} for u in lines(d / "phishing-urls.csv")]
    write("phishstorm", pd.DataFrame(rows))


def iscx():
    d = EXT / "iscx_url_2016_mirror"
    rows = [{"url": u, "label": 0} for u in lines(d / "Benign_list_big_final.csv")] + \
           [{"url": u, "label": 1} for u in lines(d / "phishing_dataset.csv")]
    write("iscx2016", pd.DataFrame(rows))


def kaggle651k():
    df = pd.read_csv(EXT / "kaggle_malicious_urls" / "dataset_phising.csv")
    bp = df[df["type"].isin(["benign", "phishing"])]
    write("kaggle651k_bp", pd.DataFrame({"url": bp.url, "label": (bp["type"] == "phishing").astype(int)}))
    write("kaggle651k_all", pd.DataFrame({"url": df.url, "label": (df["type"] != "benign").astype(int),
                                          "type": df["type"]}))


def lineage():
    df = pd.read_csv(EXT / "hf_mitake" / "PhishBenignDataset.csv")
    df = df.rename(columns={"label": "label"})[["url", "label"]].dropna()
    df["label"] = df["label"].astype(int)
    df = df.drop_duplicates("url")
    write("lineage886k", df)
    # proxy with the original dataset's size and class balance
    rng = 42
    neg = df[df.label == 0].sample(ORIG_N_LEGIT, random_state=rng)
    pos = df[df.label == 1].sample(ORIG_N_PHISH, random_state=rng)
    write("lineage253k", pd.concat([neg, pos]).sample(frac=1, random_state=rng))


def phishtank():
    df = pd.read_csv(EXT / "phishtank" / "online-valid.csv", usecols=["url", "submission_time", "target"])
    write("phishtank", pd.DataFrame({"url": df.url, "label": 1, "timestamp": df.submission_time, "target": df.target}))


def urlhaus():
    df = pd.read_csv(EXT / "urlhaus" / "csv.txt", comment="#", header=None,
                     names=["id", "dateadded", "url", "url_status", "last_online", "threat", "tags", "urlhaus_link", "reporter"])
    write("urlhaus", pd.DataFrame({"url": df.url, "label": 1, "timestamp": df.dateadded}))


def openphish():
    write("openphish", pd.DataFrame({"url": lines(EXT / "openphish" / "feed.txt"), "label": 1}))


if __name__ == "__main__":
    for fn in (phiusiil, hannousse, ebbu, phishstorm, iscx, kaggle651k, lineage, phishtank, urlhaus, openphish):
        try:
            fn()
        except Exception as e:  # keep going; report at the end
            print(f"FAILED {fn.__name__}: {e!r}", file=sys.stderr)
