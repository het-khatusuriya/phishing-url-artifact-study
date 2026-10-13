"""Phishing URL Risk Checker — desktop GUI (Tkinter).

Run:  python url_checker_gui.py
Models: every *.joblib bundle in ./models is loaded at start-up (train one with
        scripts/train_final_model.py); more can be added with "Load model…".

The app shows model *estimates*. A URL that is not flagged is not guaranteed safe.
"""
import csv
import queue
import sys
import threading
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from src.urlresearch.evaluation.mutations import MUTATIONS, apply_mutation  # noqa: E402
from src.urlresearch.features.url_parse import parse_url  # noqa: E402
from src.urlresearch.prediction.predictor import URLPredictor  # noqa: E402

APP_TITLE = "Phishing URL Risk Checker"
MAX_URL_LEN = 4096
POLICIES = [  # (label shown, threshold key in the model bundle)
    ("Balanced — false-positive budget 1 %", "val_fpr0.01"),
    ("Strict — false-positive budget 0.1 %", "val_fpr0.001"),
    ("Best F1 on validation data", "val_maxf1"),
    ("Plain 0.5 threshold", "t0.5"),
]
VARIANT_LABELS = {
    "upper_host": "Upper-case scheme and host", "trailing_slash": "Slash on empty path",
    "default_port": "Explicit default port", "encode_path_char": "Percent-encode one path letter",
    "add_fragment": "Add a #fragment", "toggle_www": "Add / remove leading www.",
    "toggle_scheme": "Switch http ↔ https", "add_utm_query": "Append tracking parameter",
}
FRIENDLY = {
    "xgb_lexical_v2_canon_pool_all_grouped_s42": "Recommended — XGBoost, 6 pooled corpora, canonical features",
    "softvote_baseline28_phiusiil_grouped_s42": "Original approach — soft vote, 28 features, PhiUSIIL only",
}
RED, GREEN, AMBER, GREY = "#B3261E", "#1E6B3A", "#8A5A00", "#5F6368"


def friendly(name):
    return FRIENDLY.get(name, name)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        w, h = min(1280, sw - 60), min(820, sh - 100)
        self.geometry(f"{w}x{h}+{max(0, (sw - w) // 2)}+{max(0, (sh - h) // 3)}")
        self.minsize(min(980, w), min(620, h))
        self.models = {}            # name -> URLPredictor
        self.jobs = queue.Queue()   # results from worker threads -> UI thread
        self.batch_rows = []
        self._style()
        self._build_menu()
        self._build_header()
        self._build_tabs()
        self._build_status()
        self.after(100, self._poll)
        self._run_bg(self._load_default_models, done=self._on_models_loaded, busy="Loading models…")

    # ------------------------------------------------------------------ layout
    def _style(self):
        s = ttk.Style(self)
        if "clam" in s.theme_names():
            s.theme_use("clam")
        s.configure("TNotebook.Tab", padding=(14, 6))
        s.configure("Header.TLabel", font=("Segoe UI", 15, "bold"))
        s.configure("Sub.TLabel", foreground=GREY)
        s.configure("Verdict.TLabel", font=("Segoe UI", 16, "bold"))
        s.configure("Treeview", rowheight=24)
        s.configure("Treeview.Heading", font=("Segoe UI", 9, "bold"))
        s.configure("Accent.TButton", font=("Segoe UI", 10, "bold"))
        s.configure("Horizontal.TProgressbar", troughcolor="#ECECEC", background="#4C72B0", bordercolor="#C8C8C8",
                    lightcolor="#4C72B0", darkcolor="#4C72B0")
        for name, col in (("Red", RED), ("Amber", AMBER), ("Green", GREEN)):
            s.configure(f"{name}.Horizontal.TProgressbar", troughcolor="#ECECEC", background=col, bordercolor="#C8C8C8",
                        lightcolor=col, darkcolor=col)

    def _build_menu(self):
        m = tk.Menu(self)
        f = tk.Menu(m, tearoff=False)
        f.add_command(label="Load model…", command=self._load_model_dialog)
        f.add_command(label="Open URL list for batch scan…", command=self._batch_open)
        f.add_separator()
        f.add_command(label="Exit", command=self.destroy)
        m.add_cascade(label="File", menu=f)
        h = tk.Menu(m, tearoff=False)
        h.add_command(label="How to read the results", command=self._help)
        h.add_command(label="About", command=lambda: messagebox.showinfo(
            "About", f"{APP_TITLE}\n\nLexical phishing-URL risk estimation with the models from the "
                     "accompanying study. Works offline: URLs are never visited."))
        m.add_cascade(label="Help", menu=h)
        self.config(menu=m)

    def _build_header(self):
        top = ttk.Frame(self, padding=(14, 10, 14, 4))
        top.pack(fill="x")
        ttk.Label(top, text=APP_TITLE, style="Header.TLabel").grid(row=0, column=0, sticky="w")
        ttk.Label(top, text="Offline estimate from the URL text only — the page is never opened.",
                  style="Sub.TLabel").grid(row=1, column=0, sticky="w")
        ctl = ttk.Frame(top)
        ctl.grid(row=0, column=1, rowspan=2, sticky="e")
        top.columnconfigure(0, weight=1)
        ttk.Label(ctl, text="Model").grid(row=0, column=0, sticky="e", padx=(0, 6))
        self.model_var = tk.StringVar()
        self.model_box = ttk.Combobox(ctl, textvariable=self.model_var, state="readonly", width=50)
        self.model_box.grid(row=0, column=1, sticky="w")
        self.model_box.bind("<<ComboboxSelected>>", lambda e: self._refresh_model_info())
        ttk.Label(ctl, text="Operating point").grid(row=1, column=0, sticky="e", padx=(0, 6), pady=(4, 0))
        self.policy_var = tk.StringVar(value=POLICIES[0][0])
        ttk.Combobox(ctl, textvariable=self.policy_var, state="readonly", width=50,
                     values=[p[0] for p in POLICIES]).grid(row=1, column=1, sticky="w", pady=(4, 0))

    def _build_tabs(self):
        self.nb = ttk.Notebook(self)
        self.nb.pack(fill="both", expand=True, padx=12, pady=6)
        self._tab_check()
        self._tab_variants()
        self._tab_batch()
        self._tab_info()

    def _build_status(self):
        bar = ttk.Frame(self, padding=(12, 2))
        bar.pack(fill="x", side="bottom")
        self.status = tk.StringVar(value="Ready")
        ttk.Label(bar, textvariable=self.status, style="Sub.TLabel").pack(side="left")
        self.busy = ttk.Progressbar(bar, mode="indeterminate", length=140)
        self.busy.pack(side="right")

    # ------------------------------------------------------------------ tab 1: check a URL
    def _tab_check(self):
        t = ttk.Frame(self.nb, padding=10)
        self.nb.add(t, text="Check a URL")
        row = ttk.Frame(t)
        row.pack(fill="x")
        ttk.Label(row, text="URL").pack(side="left")
        self.url_var = tk.StringVar()
        e = ttk.Entry(row, textvariable=self.url_var, font=("Consolas", 11))
        e.pack(side="left", fill="x", expand=True, padx=8)
        e.bind("<Return>", lambda ev: self._check())
        e.focus_set()
        ttk.Button(row, text="Check", style="Accent.TButton", command=self._check).pack(side="left")
        ttk.Button(row, text="Clear", command=self._clear).pack(side="left", padx=(6, 0))
        ex = ttk.Frame(t)
        ex.pack(fill="x", pady=(6, 4))
        ttk.Label(ex, text="Examples:", style="Sub.TLabel").pack(side="left")
        for u in ("https://google.com/", "https://www.wikipedia.org", "http://paypal.com.secure-login.xyz/webscr?cmd=_login",
                  "http://192.168.4.20/bank/verify.php"):
            ttk.Button(ex, text=u if len(u) < 34 else u[:31] + "…", command=lambda v=u: (self.url_var.set(v), self._check())
                       ).pack(side="left", padx=3)

        # verdict card
        card = ttk.LabelFrame(t, text="Verdict (selected model)", padding=10)
        card.pack(fill="x", pady=(6, 6))
        self.verdict = ttk.Label(card, text="Enter a URL and press Check.", style="Verdict.TLabel")
        self.verdict.grid(row=0, column=0, columnspan=3, sticky="w")
        ttk.Label(card, text="Estimated probability of phishing").grid(row=1, column=0, sticky="w", pady=(6, 0))
        self.prob_bar = ttk.Progressbar(card, length=360, maximum=100)
        self.prob_bar.grid(row=1, column=1, sticky="w", padx=8, pady=(6, 0))
        self.prob_txt = ttk.Label(card, text="—")
        self.prob_txt.grid(row=1, column=2, sticky="w", pady=(6, 0))
        self.detail_txt = ttk.Label(card, text="", style="Sub.TLabel", wraplength=1000, justify="left")
        self.detail_txt.grid(row=2, column=0, columnspan=3, sticky="w", pady=(6, 0))

        lower = ttk.Panedwindow(t, orient="horizontal")
        lower.pack(fill="both", expand=True)
        left = ttk.LabelFrame(lower, text="Why? Strongest feature contributions", padding=6)
        right = ttk.Frame(lower)
        lower.add(left, weight=3)
        lower.add(right, weight=2)
        self.explain_note = ttk.Label(left, text="", style="Sub.TLabel", wraplength=620, justify="left")
        self.explain_note.pack(anchor="w")
        self.explain = self._tree(left, [("feature", "Feature", 230), ("value", "Value", 90),
                                         ("contrib", "Contribution", 100), ("dir", "Pushes towards", 130)])
        comp = ttk.LabelFrame(right, text="URL breakdown", padding=6)
        comp.pack(fill="both", expand=True)
        self.components = self._tree(comp, [("part", "Part", 130), ("val", "Value", 300)], height=8)
        allm = ttk.LabelFrame(right, text="All loaded models", padding=6)
        allm.pack(fill="both", expand=True, pady=(6, 0))
        self.allmodels = self._tree(allm, [("model", "Model", 290), ("p", "P(phishing)", 85), ("dec", "Decision", 90)], height=4)

    # ------------------------------------------------------------------ tab 2: variants
    def _tab_variants(self):
        t = ttk.Frame(self.nb, padding=10)
        self.nb.add(t, text="Variant test")
        ttk.Label(t, wraplength=1100, justify="left", text=(
            "A trustworthy detector should give the same answer for different ways of writing the same address. "
            "Tier A variants are equivalent by the URL standard (RFC 3986); tier B variants change only how the "
            "address is presented. The test uses the URL from the first tab.")).pack(anchor="w")
        b = ttk.Frame(t)
        b.pack(fill="x", pady=8)
        ttk.Button(b, text="Run variant test", style="Accent.TButton", command=self._variants).pack(side="left")
        self.var_summary = ttk.Label(b, text="", style="Sub.TLabel")
        self.var_summary.pack(side="left", padx=12)
        self.var_frame = ttk.Frame(t)
        self.var_frame.pack(fill="both", expand=True)
        self.var_tree = None

    # ------------------------------------------------------------------ tab 3: batch
    def _tab_batch(self):
        t = ttk.Frame(self.nb, padding=10)
        self.nb.add(t, text="Batch scan")
        b = ttk.Frame(t)
        b.pack(fill="x")
        ttk.Button(b, text="Open file…", command=self._batch_open).pack(side="left")
        ttk.Button(b, text="Export results…", command=self._batch_export).pack(side="left", padx=6)
        self.batch_info = ttk.Label(b, text="Text file with one URL per line, or CSV with a 'url' column.", style="Sub.TLabel")
        self.batch_info.pack(side="left", padx=10)
        self.batch_prog = ttk.Progressbar(t, maximum=100)
        self.batch_prog.pack(fill="x", pady=6)
        self.batch_tree = self._tree(t, [("url", "URL", 620), ("p", "P(phishing)", 100), ("dec", "Decision", 100),
                                         ("band", "Confidence", 100)], height=18)
        self.batch_tree.tag_configure("flag", foreground=RED)

    # ------------------------------------------------------------------ tab 4: model info
    def _tab_info(self):
        t = ttk.Frame(self.nb, padding=10)
        self.nb.add(t, text="Model info")
        self.info = tk.Text(t, wrap="word", font=("Consolas", 10), relief="flat", padx=8, pady=8)
        self.info.pack(fill="both", expand=True)
        self.info.configure(state="disabled")

    def _tree(self, parent, cols, height=10):
        frame = ttk.Frame(parent)
        frame.pack(fill="both", expand=True)
        tv = ttk.Treeview(frame, columns=[c[0] for c in cols], show="headings", height=height)
        for key, title, w in cols:
            tv.heading(key, text=title)
            tv.column(key, width=w, anchor="w", stretch=True)
        sb = ttk.Scrollbar(frame, orient="vertical", command=tv.yview)
        tv.configure(yscrollcommand=sb.set)
        tv.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")
        return tv

    # ------------------------------------------------------------------ background work
    def _run_bg(self, fn, done=None, busy="Working…"):
        self.status.set(busy)
        self.busy.start(12)

        def worker():
            try:
                res, err = fn(), None
            except Exception as ex:  # surface errors in the UI instead of crashing the thread
                res, err = None, ex
            self.jobs.put((done, res, err))
        threading.Thread(target=worker, daemon=True).start()

    def _poll(self):
        try:
            while True:
                done, res, err = self.jobs.get_nowait()
                if isinstance(err, str) and err == "__progress__":   # intermediate progress update
                    done(res)
                    continue
                self.busy.stop()
                if err is not None:
                    self.status.set("Error")
                    messagebox.showerror(APP_TITLE, f"{type(err).__name__}: {err}")
                else:
                    self.status.set("Ready")
                    if done:
                        done(res)
        except queue.Empty:
            pass
        self.after(100, self._poll)

    # ------------------------------------------------------------------ models
    def _load_default_models(self):
        loaded = {}
        for p in sorted((ROOT / "models").glob("*.joblib")):
            pr = URLPredictor(p)
            loaded[pr.meta.get("name", p.stem)] = pr
        return loaded

    def _on_models_loaded(self, loaded):
        self.models.update(loaded or {})
        if not self.models:
            messagebox.showwarning(APP_TITLE, "No model found in ./models.\n\nTrain one with:\n"
                                   "python scripts/train_final_model.py --dataset pool_all "
                                   "--feature-set lexical_v2_canon --model xgb --split grouped --calibrate none\n\n"
                                   "or use File → Load model…")
            return
        names = list(self.models)
        self.model_box["values"] = [friendly(n) for n in names]
        pref = next((n for n in names if n.startswith("xgb_lexical_v2_canon")), names[0])
        self.model_box.set(friendly(pref))
        self.status.set(f"{len(names)} model(s) loaded")
        self._refresh_model_info()

    def _load_model_dialog(self):
        path = filedialog.askopenfilename(title="Load model bundle", initialdir=ROOT / "models",
                                          filetypes=[("Model bundle", "*.joblib")])
        if path:
            def work():
                pr = URLPredictor(path)
                return {pr.meta.get("name", Path(path).stem): pr}
            self._run_bg(work, done=self._on_models_loaded, busy="Loading model…")

    def _current(self):
        label = self.model_var.get()
        for n, m in self.models.items():
            if friendly(n) == label:
                return n, m
        return None, None

    def _policy(self):
        return dict(POLICIES)[self.policy_var.get()]

    # ------------------------------------------------------------------ actions
    def _validated_url(self):
        url = self.url_var.get().strip()
        if not url:
            messagebox.showinfo(APP_TITLE, "Please enter a URL.")
            return None
        if len(url) > MAX_URL_LEN:
            messagebox.showwarning(APP_TITLE, f"The URL is longer than {MAX_URL_LEN} characters.")
            return None
        if not self.models:
            messagebox.showwarning(APP_TITLE, "No model is loaded.")
            return None
        return url

    def _check(self):
        url = self._validated_url()
        if not url:
            return
        name, model = self._current()
        policy = self._policy()

        def work():
            res = {n: m.predict([url], policy=policy if policy in m.thresholds else "t0.5")[0] for n, m in self.models.items()}
            return {"url": url, "name": name, "res": res, "explain": model.explain(url, top_k=10), "parsed": parse_url(url)}
        self._run_bg(work, done=self._show_check, busy="Scoring…")

    def _show_check(self, out):
        r = out["res"][out["name"]]
        p = r["p_malicious"]
        if r["flagged"]:
            self.verdict.configure(text="⚠  Likely phishing — treat with caution", foreground=RED)
            self.prob_bar.configure(style="Red.Horizontal.TProgressbar")
        elif r["confidence_band"] == "low":
            self.verdict.configure(text="?  Uncertain — close to the decision threshold", foreground=AMBER)
            self.prob_bar.configure(style="Amber.Horizontal.TProgressbar")
        else:
            self.verdict.configure(text="✓  Not flagged by the model", foreground=GREEN)
            self.prob_bar.configure(style="Green.Horizontal.TProgressbar")
        self.prob_bar["value"] = p * 100
        self.prob_txt.configure(text=f"{p * 100:.1f} %")
        self.detail_txt.configure(text=(
            f"Threshold {r['threshold'] * 100:.1f} % ({self.policy_var.get()}); confidence: {r['confidence_band']}. "
            f"{r['statement']}"))
        self.explain.delete(*self.explain.get_children())
        self.explain_note.configure(text=("Contributions in log-odds; positive values push towards phishing. "
                                          + (f"Explanation {out['explain']['note']}." if out["explain"]["note"] else "")))
        for feat, val, c in out["explain"]["rows"]:
            v = f"{(0.0 if abs(val) < 1e-12 else val):.3g}" if isinstance(val, (int, float)) else str(val)
            self.explain.insert("", "end", values=(feat, v, f"{c:+.3f}", "phishing" if c > 0 else "legitimate"))
        pu = out["parsed"]
        self.components.delete(*self.components.get_children())
        for k, v in (("Scheme", pu.scheme + ("" if pu.had_scheme else "  (none given)")), ("Host", pu.hostname),
                     ("Registered domain", pu.registered_domain), ("Subdomain", pu.subdomain), ("Public suffix", pu.suffix),
                     ("Port", pu.port or ""), ("Path", pu.path), ("Query", pu.query), ("Fragment", pu.fragment),
                     ("IP address host", "yes" if pu.is_ip else "no"), ("Punycode host", "yes" if "xn--" in pu.hostname else "no"),
                     ("Decoded host", pu.decoded_hostname if pu.decoded_hostname != pu.hostname else "")):
            self.components.insert("", "end", values=(k, v))
        self.allmodels.delete(*self.allmodels.get_children())
        for n, rr in out["res"].items():
            self.allmodels.insert("", "end", values=(friendly(n), f"{rr['p_malicious'] * 100:.1f} %",
                                                     "FLAGGED" if rr["flagged"] else "not flagged"))
        self.status.set(f"Checked with {friendly(out['name'])}")

    def _clear(self):
        self.url_var.set("")
        self.verdict.configure(text="Enter a URL and press Check.", foreground="")
        self.prob_bar["value"] = 0
        self.prob_txt.configure(text="—")
        self.detail_txt.configure(text="")
        for tv in (self.explain, self.components, self.allmodels):
            tv.delete(*tv.get_children())

    def _variants(self):
        url = self._validated_url()
        if not url:
            return
        policy = self._policy()
        names = list(self.models)

        def work():
            rows = [("Original", "—", url)]
            for key, spec in MUTATIONS.items():
                v = apply_mutation([url], key)[0]
                rows.append((VARIANT_LABELS.get(key, key), spec["tier"], v))
            urls = [r[2] for r in rows]
            preds = {n: self.models[n].predict(urls, policy=policy if policy in self.models[n].thresholds else "t0.5")
                     for n in names}
            return rows, preds
        self._run_bg(work, done=lambda res: self._show_variants(names, *res), busy="Testing variants…")

    def _show_variants(self, names, rows, preds):
        if self.var_tree is not None:
            self.var_tree.master.destroy()
        cols = [("variant", "Variant", 210), ("tier", "Tier", 45), ("url", "URL as written", 380)]
        cols += [(f"m{i}", friendly(n)[:38], 210) for i, n in enumerate(names)]
        self.var_tree = self._tree(self.var_frame, cols, height=12)
        self.var_tree.tag_configure("changed", background="#FCE8E6")
        changed = {n: 0 for n in names}
        for j, (lab, tier, u) in enumerate(rows):
            vals, tag = [lab, tier, u], ()
            for n in names:
                p = preds[n][j]
                vals.append(f"{'FLAGGED' if p['flagged'] else 'ok'}  ({p['p_malicious'] * 100:.0f} %)")
                if j and p["flagged"] != preds[n][0]["flagged"]:
                    changed[n] += 1
                    tag = ("changed",)
            self.var_tree.insert("", "end", values=vals, tags=tag)
        self.var_summary.configure(text="  ·  ".join(f"{friendly(n)[:30]}: {c} of {len(rows) - 1} variants change the decision"
                                                     for n, c in changed.items()))

    def _batch_open(self):
        path = filedialog.askopenfilename(title="Open URL list", filetypes=[("Text or CSV", "*.txt *.csv"), ("All files", "*.*")])
        if not path:
            return
        urls = []
        with open(path, encoding="utf-8", errors="replace", newline="") as fh:
            if path.lower().endswith(".csv"):
                rd = csv.DictReader(fh)
                col = next((c for c in (rd.fieldnames or []) if c.strip().lower() in ("url", "urls", "link")), None)
                if col is None:
                    messagebox.showwarning(APP_TITLE, "The CSV needs a column named 'url'.")
                    return
                urls = [r[col].strip() for r in rd if r.get(col, "").strip()]
            else:
                urls = [l.strip() for l in fh if l.strip()]
        urls = [u for u in urls if len(u) <= MAX_URL_LEN]
        if not urls:
            messagebox.showinfo(APP_TITLE, "No URLs found in the file.")
            return
        name, model = self._current()
        if model is None:
            messagebox.showwarning(APP_TITLE, "No model is loaded.")
            return
        policy = self._policy()
        self.nb.select(2)
        self.batch_tree.delete(*self.batch_tree.get_children())
        self.batch_info.configure(text=f"Scanning {len(urls):,} URLs from {Path(path).name}…")

        def work():
            out, step = [], 500
            for i in range(0, len(urls), step):
                out += model.predict(urls[i:i + step], policy=policy if policy in model.thresholds else "t0.5")
                self.jobs.put((lambda pct: self.batch_prog.configure(value=pct), min(100, (i + step) * 100 / len(urls)), "__progress__"))
            return out
        self._run_bg(work, done=lambda res: self._show_batch(res, Path(path).name), busy="Batch scan…")

    def _show_batch(self, res, fname):
        self.batch_rows = res
        for r in res[:20000]:
            self.batch_tree.insert("", "end", tags=("flag",) if r["flagged"] else (),
                                   values=(r["url"], f"{r['p_malicious'] * 100:.1f} %",
                                           "FLAGGED" if r["flagged"] else "not flagged", r["confidence_band"]))
        n_flag = sum(r["flagged"] for r in res)
        shown = "" if len(res) <= 20000 else " (first 20,000 shown; export for all)"
        self.batch_info.configure(text=f"{fname}: {len(res):,} URLs, {n_flag:,} flagged ({n_flag / len(res) * 100:.1f} %){shown}")
        self.batch_prog.configure(value=100)

    def _batch_export(self):
        if not self.batch_rows:
            messagebox.showinfo(APP_TITLE, "Run a batch scan first.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV", "*.csv")],
                                            initialfile="url_scan_results.csv")
        if path:
            keys = ["url", "p_malicious", "flagged", "threshold", "policy", "confidence_band", "model", "statement"]
            with open(path, "w", encoding="utf-8", newline="") as fh:
                w = csv.DictWriter(fh, fieldnames=keys, extrasaction="ignore")
                w.writeheader()
                w.writerows(self.batch_rows)
            self.status.set(f"Saved {len(self.batch_rows):,} rows to {Path(path).name}")

    def _refresh_model_info(self):
        name, m = self._current()
        if m is None:
            return
        meta = m.meta
        lines = [friendly(name), "=" * len(friendly(name)), "",
                 f"Bundle            : {name}",
                 f"Trained on        : {meta.get('dataset', '?')}  ({meta.get('n_train', '?'):,} training URLs)"
                 if isinstance(meta.get("n_train"), int) else f"Trained on        : {meta.get('dataset', '?')}",
                 f"Features          : {m.feature_set}{' (artifact columns removed)' if m.drop_artifacts else ''}",
                 f"Model             : {meta.get('model', '?')}",
                 f"Split             : {meta.get('split', '?')} (seed {meta.get('seed', '?')})", "",
                 "Thresholds (chosen on validation data only):"]
        for lab, key in POLICIES:
            if key in m.thresholds:
                lines.append(f"  {lab:40s} {m.thresholds[key]:.4f}")
        tm = meta.get("test_metrics", {})
        if tm:
            lines += ["", "Held-out test results (same corpora as training, unseen registered domains):",
                      f"  {'operating point':40s} {'recall':>7s} {'FPR':>7s} {'precision':>9s} {'ROC-AUC':>8s}"]
            for lab, key in POLICIES:
                if key in tm:
                    x = tm[key]
                    lines.append(f"  {lab:40s} {x['recall']:7.3f} {x['fpr']:7.3f} {x['precision']:9.3f} {x['roc_auc']:8.3f}")
        lines += ["", "Limitations:",
                  "  • Estimates come from the URL text only; the page is never visited.",
                  "  • Test results describe the training corpora; on differently collected traffic the false-positive",
                  "    rate at a given threshold can be much higher (see the accompanying paper).",
                  "  • A URL that is not flagged is not guaranteed to be safe."]
        if name.startswith("softvote_baseline28"):
            lines += ["", "Note: this model reproduces the original project's approach and is included for comparison.",
                      "It relies on the https scheme and 'www.' prefix, e.g. it flags https://google.com/."]
        self.info.configure(state="normal")
        self.info.delete("1.0", "end")
        self.info.insert("1.0", "\n".join(lines))
        self.info.configure(state="disabled")

    def _help(self):
        messagebox.showinfo("How to read the results", (
            "Probability: the model's estimate that the URL is a phishing URL.\n\n"
            "Operating point: the threshold above which a URL is flagged. 'Balanced' was chosen so that about 1 % of "
            "legitimate URLs in the validation data were flagged; 'Strict' about 0.1 %.\n\n"
            "Confidence: how far the probability is from the threshold (low / medium / high).\n\n"
            "Why?: the features that pushed this estimate up (towards phishing) or down.\n\n"
            "Variant test: whether equivalent ways of writing the same URL change the decision.\n\n"
            "The tool never opens the URL and cannot guarantee that a URL is safe."))


def main():
    if sys.platform == "win32":  # crisp rendering on scaled (high-DPI) displays
        try:
            import ctypes
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except Exception:
            pass
    App().mainloop()


if __name__ == "__main__":
    main()
