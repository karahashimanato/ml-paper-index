import re, yaml, hashlib, pymupdf
ID = "arxiv-2106.11959"
pdf = f"cache/pdfs/{ID}.pdf"
doc = pymupdf.open(pdf)
def page_text(n): return " ".join(doc[n - 1].get_text().split())

DS = ["CA", "AD", "HE", "JA", "HI", "AL", "EP", "YE", "CO", "YA", "MI"]
NAMES = {"CA": "California Housing", "AD": "Adult", "HE": "Helena", "JA": "Jannis", "HI": "Higgs Small (OpenML, 98K)",
         "AL": "ALOI", "EP": "Epsilon", "YE": "Year (YearPrediction MSD)", "CO": "Covertype", "YA": "Yahoo LTR (pointwise regression)",
         "MI": "Microsoft MSLR-WEB10K (pointwise regression)"}
RMSE = {"CA", "YE", "YA", "MI"}
NUM = r"(?:[0-9]+\.[0-9]+|–)"

def rows(page, start, end, methods, cols, extra=0):
    """表の範囲 [start, end) を空白正規化した文字列から、手法名 + len(cols)(+extra) 個の値として読む。"""
    t = page_text(page); s0 = t.index(start) + len(start); seg = t[s0: t.index(end, s0) if end else len(t)]
    out = []
    for m in methods:
        g = re.search(re.escape(m) + r" ((?:" + NUM + r" ){" + str(len(cols) - 1) + r"}" + NUM + r")" + (r" ([0-9.]+) \(([0-9.]+)\)" if extra else ""), seg)
        assert g, (page, m, seg[:300])
        vals = g.group(1).split(" ")
        out.append((m, dict(zip(cols, vals)), g.group(0), (float(g.group(2)), float(g.group(3))) if extra else None))
        seg = seg[g.end():]
    return out

results = []
def add(bench_suffix, method, rowdata, quote, location, page):
    m, vals, q, _ = rowdata
    for ds, v in vals.items():
        if v == "–": continue
        results.append({"id": f"r{len(results) + 1}", "benchmark": f"gorishniy2021-{ds.lower()}-{bench_suffix}", "method": method,
                        "metric": "rmse" if ds in RMSE else "accuracy", "value": float(v), "location": location, "page": page, "quote": q})

T2 = ["TabNet", "SNN", "AutoInt", "GrowNet", "MLP", "DCN2", "NODE", "ResNet", "FT-T"]
for r in rows(7, "rank (std)", "4.4 Comparing DL models", T2, DS, extra=1):
    name = "FT-Transformer" if r[0] == "FT-T" else r[0]
    add("single", name, r, None, "Table 2", 7)
    results.append({"id": f"r{len(results) + 1}", "benchmark": "gorishniy2021-avg-rank-single", "method": name, "metric": "average-rank",
                    "value": r[3][0], "std": r[3][1], "note": "std is the standard deviation of ranks across datasets.",
                    "location": "Table 2", "page": 7, "quote": r[2]})
for r in rows(7, "YA ↓ MI ↓ NODE", "4.5 Comparing", ["", "ResNet", "FT-Transformer"][1:], DS):
    add("ensemble", f"{r[0]} (tuned)", r, None, "Table 3", 7)
node = rows(7, "YA ↓ MI ↓", "ResNet 0.478", ["NODE"], DS)[0]
add("ensemble", "NODE (tuned)", node, None, "Table 3", 7)
for r in rows(8, "Default hyperparameters XGBoost", "Tuned hyperparameters", ["", "CatBoost", "FT-Transformer"][1:], DS):
    add("ensemble", f"{r[0]} (default)", r, None, "Table 4", 8)
xgb_def = rows(8, "Default hyperparameters", "CatBoost 0.428", ["XGBoost"], DS)[0]
add("ensemble", "XGBoost (default)", xgb_def, None, "Table 4", 8)
for r in rows(8, "Tuned hyperparameters", "Default hyperparameters. We start", ["XGBoost", "CatBoost"], DS):
    add("ensemble", f"{r[0]} (tuned)", r, None, "Table 4", 8)
T5 = ["CA", "HE", "JA", "HI", "AL", "YE", "CO", "MI"]
for r in rows(9, "Notation follows Table 2.", None, ["FT-Transformer (w/o feature biases)"], T5):
    add("single", r[0], r, None, "Table 5", 9)

claims = [
  ("None of the considered DL models consistently outperformed the simple ResNet-like baseline.", "Section 1", 2,
   "First, we reveal that none of the considered DL models can consistently outperform the ResNet-like model."),
  ("FT-Transformer (proposed) performed best among DL models on most tasks.", "Section 1", 2,
   "Second, FT-Transformer demonstrates the best performance on most tasks and becomes a new powerful solution for the field."),
  ("There is no universally superior solution among GBDT and deep models.", "Section 1", 2,
   "We reveal that there is still no universally superior solution among GBDT and deep models."),
  ("With tuned hyperparameters, GBDT ensembles dominated on California Housing, Adult and Yahoo.", "Section 4.5", 8,
   "Once hyperparameters are properly tuned, GBDTs start dominating on some datasets (California Housing, Adult, Yahoo; see Table 4)."),
  ("Authors state that DL winning on most of their datasets reflects a benchmark slightly biased towards DL-friendly problems, not DL being better.", "Section 4.5", 8,
   'it only means that the constructed benchmark is slightly biased towards "DL-friendly" problems.'),
  ("GBDT struggled on multiclass problems with many classes: poor on Helena (100 classes), untunable on ALOI (1000 classes) due to slow training.", "Section 4.5", 8,
   "GBDT can demonstrate unsatisfactory performance (Helena) or even be untunable due to extremely slow training (ALOI)."),
  ("Ensembles of default FT-Transformers performed roughly on par with ensembles of tuned FT-Transformers.", "Section 4.5", 8,
   "Interestingly, the ensemble of default FT-Transformers performs quite on par with the ensembles of tuned FT-Transformers."),
  ("Tuning made simple models (MLP, ResNet) competitive; authors recommend tuning baselines.", "Section 4.4", 7,
   "Tuning makes simple models such as MLP and ResNet competitive, so we recommend tuning baselines when possible."),
  ("FT-Transformer needs more hardware and time than ResNet and may not scale to very many features (attention is quadratic in the number of features).", "Section 3.3 Limitations", 5,
   "FT-Transformer requires more resources (both hardware and time) for training than simple models such as ResNet"),
  ("NODE was inferior to ResNet on six of the eleven datasets despite being more complex.", "Section 4.4", 7,
   "However, it is still inferior to ResNet on six datasets (Helena, Jannis, Higgs, ALOI, Epsilon, Covertype), while being a more complex solution."),
  ("On synthetic targets interpolating between GBDT-friendly and DL-friendly functions, ResNet degraded as targets became GBDT-friendly while FT-Transformer stayed competitive.", "Section 5.1, Figure 3", 9,
   "By contrast, FT-Transformer yields competitive performance across the whole range of tasks."),
  ("FT-Transformer was not tuned on Yahoo (default configuration reported) and only heuristic default configurations were tried on Epsilon.", "Appendix E.2", 18,
   "For Yahoo, we did not perform tuning at all, since the default configuration already performed well."),
  ("Each tuned configuration was evaluated over 15 random seeds; ensembles are three disjoint groups of 5 models.", "Section 4.3", 6,
   "For each tuned configuration, we run 15 experiments with different random seeds and report the performance on the test set."),
  ("XGBoost used one-hot encoding for categorical features; CatBoost used its built-in categorical support.", "Section 4.3", 6,
   "For XGBoost, we use one-hot encoding."),
  ("Averaging [CLS] attention maps gave feature-importance rankings comparable to Integrated Gradients at much lower cost.", "Section 5.3", 10,
   "we conclude that the simple averaging of attention maps can be a good choice in terms of cost-effectiveness."),
  ("Dataset sizes (#objects) range from 20,640 (California Housing) to 1,200,192 (Microsoft); the 11 datasets include multiclass problems with 100 (Helena) and 1000 (ALOI) classes.", "Table 1", 6,
   "#objects 20640 48842 65196 83733 98050 108000 500000 515345 581012 709877 1200192"),
  ("Most models were tuned with Optuna's TPE (Bayesian optimization); the rest used predefined configurations from their papers. The test set was never used for tuning.", "Section 4.3", 6,
   "we use the Optuna library (Akiba et al., 2019) to run Bayesian optimization (the Tree-Structured Parzen Estimator algorithm)"),
]
card = {
  "id": ID,
  "title": "Revisiting Deep Learning Models for Tabular Data",
  "authors": ["Yury Gorishniy", "Ivan Rubachev", "Valentin Khrulkov", "Artem Babenko"],
  "year": 2021,
  "venue": "NeurIPS 2021",
  "links": {"arxiv": "https://arxiv.org/abs/2106.11959", "code": "https://github.com/yandex-research/tabular-dl-revisiting-models"},
  "source": {"version": "arXiv v5", "retrieved_at": "2026-10-02", "pdf_sha256": hashlib.sha256(open(pdf, "rb").read()).hexdigest()},
  "tags": {"tasks": ["tabular-classification", "tabular-regression"],
           "method_families": ["tabular-attention", "tabular-mlp", "differentiable-trees", "gradient-boosted-trees"],
           "paradigms": ["supervised"]},
  "proposes": ["FT-Transformer", "ResNet-like baseline for tabular data"],
  "claims": [{"id": f"c{i}", "statement": s, "location": loc, "page": pg, "quote": q} for i, (s, loc, pg, q) in enumerate(claims, 1)],
  "results": results,
  "relations": [],
  "card": {"created_at": "2026-10-02", "created_by": "claude-opus-5-5 via Claude Code", "reviewed": False,
           "notes": ("Results were extracted mechanically from the PDF text of Tables 2-5 (not typed by hand). "
                     "Single models (mean of 15 seeds; Tables 2, 5) and ensembles (mean of three 5-model ensembles; Tables 3, 4) are registered as different "
                     "benchmarks (-single / -ensemble) so they are never mixed in one comparison. Default vs tuned is encoded in the method name for ensembles. "
                     "Duplicate rows were not re-recorded: Table 4's tuned ResNet/FT-Transformer rows equal Table 3; Table 5's AutoInt/FT-Transformer rows equal Table 2. "
                     "Tuning budgets are not identical across models (Optuna iterations differ by model and dataset group; FT-Transformer untuned on Yahoo, heuristic on Epsilon; c12). "
                     "Standard deviations are only in the supplementary and were not recorded.")},
}
yaml.safe_dump(card, open(f"papers/{ID}.yaml", "w"), sort_keys=False, allow_unicode=True, width=200)

COMMON = {"split": "One fixed train/validation/test split per dataset, shared by all algorithms (Section 4.2; sizes in Appendix Table 7).",
          "preprocessing": "Quantile transformation by default; standardization for Helena and ALOI; raw features for Epsilon; regression targets standardized (Section 4.3). XGBoost: one-hot categorical; CatBoost: native categorical; NNs: categorical embeddings.",
          "tuning": "Optuna (TPE) with per-model iteration budgets, or predefined configuration grids from the original papers (Section 4.3, Appendices E-F). FT-Transformer untuned on Yahoo and heuristic configurations on Epsilon (Appendix E.2)."}
bench = []
for ds in DS:
    metric = [{"name": "rmse", "higher_is_better": False}] if ds in RMSE else [{"name": "accuracy", "higher_is_better": True}]
    task = "tabular-regression" if ds in RMSE else "tabular-classification"
    bench.append({"id": f"gorishniy2021-{ds.lower()}-single", "scope": "paper-private", "task": task, "dataset": NAMES[ds],
                  "protocol": {**COMMON, "repetitions": "Mean of 15 runs with different random seeds of the tuned configuration (Section 4.3)."},
                  "metrics": metric, "defined_in": ID})
    bench.append({"id": f"gorishniy2021-{ds.lower()}-ensemble", "scope": "paper-private", "task": task, "dataset": NAMES[ds],
                  "protocol": {**COMMON, "repetitions": "15 single models split into three disjoint groups of 5; predictions averaged within a group; mean over the three ensembles (Section 4.3)."},
                  "metrics": metric, "defined_in": ID})
bench.append({"id": "gorishniy2021-avg-rank-single", "scope": "paper-private", "task": "tabular-classification",
              "dataset": "Average over the 11 datasets of Table 2 (classification and regression)",
              "protocol": {**COMMON, "repetitions": "Ranks computed per dataset by sorting the 15-seed mean scores (Table 2 caption)."},
              "metrics": [{"name": "average-rank", "higher_is_better": False, "definition": "Average rank across datasets among the 9 DL models of Table 2."}],
              "defined_in": ID})
reg_doc = yaml.safe_load(open("registry/benchmarks.yaml")) or {}
reg_doc["benchmarks"] = [b for b in (reg_doc.get("benchmarks") or []) if b["defined_in"] != ID] + bench
header = "".join(l for l in open("registry/benchmarks.yaml") if l.startswith("#"))
open("registry/benchmarks.yaml", "w").write(header + yaml.safe_dump(reg_doc, sort_keys=False, allow_unicode=True, width=200))
print(len(results), "results,", len(claims), "claims,", len(bench), "benchmarks")
