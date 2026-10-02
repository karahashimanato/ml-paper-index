import re, yaml, hashlib, pymupdf
ID = "arxiv-2106.03253"
pdf = f"cache/pdfs/{ID}.pdf"
doc = pymupdf.open(pdf)
lines = lambda n: [l.strip() for l in doc[n - 1].get_text().splitlines() if l.strip()]

METHODS = ["XGBoost", "NODE", "DNF-Net", "TabNet", "1D-CNN", "Simple Ensemble",
           "Deep Ensemble w/o XGBoost", "Deep Ensemble w XGBoost"]
VAL = re.compile(r"^([0-9.]+)\s*±\s*,?\s*([0-9.]+(?:e-?[0-9]+)?)$")

def parse_block(ls, header):
    i = ls.index(header[0], ls.index("Model Name")); assert ls[i:i + len(header)] == header, ls[i:i+len(header)]
    out, j = [], i + len(header)
    for m in METHODS:
        assert ls[j] == m, (ls[j], m)
        for k, ds in enumerate(header):
            cell = ls[j + 1 + k]; g = VAL.match(cell); assert g, cell
            out.append((ds, m, float(g.group(1)), float(g.group(2)), " ".join(ls[j:j + 1 + len(header)])))
        j += 1 + len(header)
    return out

p6 = lines(6)
h1 = ["Rossman", "CoverType", "Higgs", "Gas", "Eye", "Gesture"]
h2 = ["YearPrediction", "MSLR", "Epsilon", "Shrutime", "Blastchar"]
cells = parse_block(p6, h1)
rest = p6[p6.index("Model Name", p6.index("Model Name") + 1):]
cells += parse_block(rest, h2)
assert len(cells) == 88

REG = {"Rossman", "YearPrediction"}
SLUG = {"Rossman": "rossmann", "CoverType": "covertype", "Higgs": "higgs", "Gas": "gas-concentrations",
        "Eye": "eye-movements", "Gesture": "gesture-phase", "YearPrediction": "yearprediction",
        "MSLR": "mslr-web10k", "Epsilon": "epsilon", "Shrutime": "shrutime", "Blastchar": "blastchar"}
results = []
for n, (ds, m, v, se, cell) in enumerate(cells, 1):
    results.append({"id": f"r{n}", "benchmark": f"shwartzziv2021-{SLUG[ds]}", "method": m,
                    "metric": "table2-mse" if ds in REG else "cross-entropy-x100", "value": v, "std": se,
                    "note": "std is the standard error of the mean over four runs (Table 2 caption).",
                    "location": "Table 2", "page": 6, "quote": cell})

# Table 3 (page 7): name / value pairs
p7 = lines(7)
k = p7.index("Performance (%)") + 1
for m in METHODS:
    assert p7[k] == m, (p7[k], m); val = p7[k + 1]
    results.append({"id": f"r{len(results) + 1}", "benchmark": "shwartzziv2021-unseen-average", "method": m,
                    "metric": "avg-relative-deterioration-pct", "value": float(val), "location": "Table 3",
                    "page": 7, "quote": f"{m} {val}"})
    k += 2

claims = [
  ("XGBoost outperformed the four deep tabular models (TabNet, NODE, DNF-Net, 1D-CNN) across the 11 datasets, including datasets from the deep models' own papers.", "Abstract", 1,
   "Our study shows that XGBoost outperforms these deep models across the datasets, including the datasets used in the papers that proposed the deep models."),
  ("XGBoost needed much less hyperparameter tuning than the deep models.", "Abstract", 1,
   "We also demonstrate that XGBoost requires much less tuning."),
  ("An ensemble of the deep models and XGBoost performed better than XGBoost alone on these datasets.", "Abstract", 1,
   "we show that an ensemble of deep models and XGBoost performs better on these datasets than XGBoost alone."),
  ("Each deep model did best only on the datasets from its own paper; no deep model was consistently better than the others.", "Section 3.2", 6,
   "Each deep model was better only on the datasets that appeared in its own paper."),
  ("Authors name selection bias in the original papers (datasets chosen where the model works well) as one possible explanation.", "Section 3.2", 6,
   "The first possibility is selection bias."),
  ("Authors name unequal hyperparameter optimization in the original papers as a second possible explanation.", "Section 3.2", 6,
   "The second possibility is differences in the optimization of hyperparameters."),
  ("All models were tuned with HyperOpt (Bayesian optimization) for 1,000 steps per dataset on a validation set.", "Section 3.1.2", 4,
   "The hyperparameter search was run for 1, 000 steps on each dataset by optimizing the results on a validation set."),
  ("XGBoost trained/tuned more than an order of magnitude faster than the deep models in their runs; authors caution this depends on software optimization.", "Section 3.2", 7,
   "Generally, we found XGBoost to be significantly faster than the deep networks in our experiments (more than an order of magnitude)."),
  ("An ensemble of classical models (XGBoost, SVM, CatBoost) was reported to perform much worse than the deep-models-plus-XGBoost ensemble.", "Section 3.2", 7,
   "Table 2 shows that the ensemble of classical models performed much worse than the ensemble of deep networks and XGBoost."),
  ("On Shrutime, choosing ensemble members by validation loss needed only three models for near-optimal performance.", "Section 3.2, Figure 1", 7,
   "Only three models were needed to achieve almost optimal performance this way."),
  ("The text says the regression metric is RMSE.", "Section 3.1.2", 5,
   "For regression problems, we report the root mean square error."),
  ("The Table 2 caption says MSE is shown for YearPrediction and Rossman (inconsistent with the RMSE statement in Section 3.1.2).", "Table 2 caption", 6,
   "MSE is presented for the YearPrediction and Rossman datasets"),
  ("The 11 datasets are nine taken from the TabNet, DNF-Net and NODE papers (three each) plus two Kaggle datasets not used by any of them.", "Section 3.1.1", 4,
   "We use nine datasets from the TabNet, DNF-Net, and NODE papers, drawing three datasets from each paper."),
  ("Table 2 values are averages of four training runs with the standard error of the mean.", "Table 2 caption", 6,
   "The values are the averages of four training runs (lower value is better), along with the standard error of the mean (SEM)"),
  ("Each dataset was preprocessed and trained as described in its original paper.", "Section 3.1.1", 4,
   "Each dataset was preprocessed and trained as described in the original paper."),
]
card = {
  "id": ID,
  "title": "Tabular Data: Deep Learning is Not All You Need",
  "authors": ["Ravid Shwartz-Ziv", "Amitai Armon"],
  "year": 2021,
  "links": {"arxiv": "https://arxiv.org/abs/2106.03253"},
  "source": {"version": "arXiv v2", "retrieved_at": "2026-10-02",
             "pdf_sha256": hashlib.sha256(open(pdf, "rb").read()).hexdigest()},
  "tags": {"tasks": ["tabular-classification", "tabular-regression"],
           "method_families": ["gradient-boosted-trees", "tabular-attention", "differentiable-trees", "tabular-cnn", "heterogeneous-ensembles"],
           "paradigms": ["supervised"]},
  "proposes": ["Ensemble of deep tabular models and XGBoost (uniform or validation-loss weighted averaging)"],
  "claims": [{"id": f"c{i}", "statement": s, "location": loc, "page": pg, "quote": q} for i, (s, loc, pg, q) in enumerate(claims, 1)],
  "results": results,
  "relations": [],
  "card": {"created_at": "2026-10-02", "created_by": "claude-opus-5-5 via Claude Code", "reviewed": False,
           "notes": ("Results r1-r96 were extracted mechanically from the PDF text of Table 2 and Table 3 (not typed by hand). "
                     "Inconsistencies in the paper: (1) regression metric is RMSE in Section 3.1.2 but MSE in the Table 2 caption (c11, c12); "
                     "(2) Section 3.2 text quotes rounded/different Table 3 values (e.g. XGBoost 3.4% vs 3.34, DNF-Net 11.8% vs 11.96); "
                     "(3) the classical-model ensemble (XGBoost+SVM+CatBoost) is said to be in Table 2, but Table 2 has no row with that name - "
                     "it is unclear whether 'Simple Ensemble' is that ensemble; "
                     "(4) Appendix B lists 'Year' under both the 80/20 split and the 70/10/20 split, and does not describe the Gas split.")},
}
yaml.safe_dump(card, open(f"papers/{ID}.yaml", "w"), sort_keys=False, allow_unicode=True, width=200)

COMMON = {"preprocessing": "Each dataset preprocessed as in its original paper; features standardized with training-set statistics (Section 3.1.1).",
          "tuning": "HyperOpt (Bayesian optimization), 1,000 steps per model per dataset, initial hyperparameters from the original papers; early stopping on validation (Section 3.1.2, Appendix B).",
          "repetitions": "Three random partitions if the original split was random, otherwise four seeds on the same partition; Table 2 reports mean and SEM of four runs."}
SPLITS = {
  "rossmann": ("Rossmann Store Sales", "2014 for train/validation (100k validation samples), 2015 for test; retrain on full training data after tuning (Appendix B)."),
  "covertype": ("Forest Cover Type", "Train/val/test split provided by the dataset authors (Appendix B)."),
  "higgs": ("Higgs Boson", "500k validation samples split from training data; retrain on full training data after tuning (Appendix B)."),
  "gas-concentrations": ("Gas Concentrations (OpenML 1477)", "Split as in the DNF-Net paper; Appendix B does not describe it."),
  "eye-movements": ("Eye Movements (OpenML 1044)", "70% train / 10% validation / 20% test (Appendix B)."),
  "gesture-phase": ("Gesture Phase (OpenML 4538)", "70% train / 10% validation / 20% test (Appendix B)."),
  "yearprediction": ("YearPrediction MSD", "Appendix B lists it under both the 80/20 train/validation split and the 70/10/20 split (ambiguous)."),
  "mslr-web10k": ("Microsoft MSLR-WEB10K", "Random stratified 80% train / 20% validation split of the full training data (Appendix B)."),
  "epsilon": ("Epsilon (PASCAL 2008)", "Random stratified 80% train / 20% validation split of the full training data (Appendix B)."),
  "shrutime": ("Shrutime (Kaggle churn modelling)", "Random stratified 80% train / 20% validation split of the full training data (Appendix B)."),
  "blastchar": ("Blastchar (Telco customer churn)", "Random stratified 80% train / 20% validation split of the full training data (Appendix B)."),
}
EXT = {"gas-concentrations": {"openml": "1477"}, "eye-movements": {"openml": "1044"}, "gesture-phase": {"openml": "4538"}}
bench = []
for slug, (name, split) in SPLITS.items():
    reg = slug in ("rossmann", "yearprediction")
    e = {"id": f"shwartzziv2021-{slug}", "scope": "paper-private",
         "task": "tabular-regression" if reg else "tabular-classification", "dataset": name,
         "protocol": {"split": split, **COMMON},
         "metrics": [{"name": "table2-mse", "higher_is_better": False,
                      "definition": "Value in Table 2. Caption says MSE; Section 3.1.2 says RMSE - the paper is inconsistent."}]
                    if reg else
                    [{"name": "cross-entropy-x100", "higher_is_better": False, "definition": "Test cross-entropy loss multiplied by 100 (Table 2 caption)."}],
         "defined_in": ID}
    if slug in EXT: e["external_ids"] = EXT[slug]
    bench.append(e)
bench.append({"id": "shwartzziv2021-unseen-average", "scope": "paper-private", "task": "tabular-classification",
              "dataset": "Aggregate over each model's unseen datasets (the 11 datasets minus those in the model's original paper)",
              "protocol": {"split": "Per-dataset splits as in the other shwartzziv2021-* entries.", **COMMON,
                           "other": "Per dataset, relative performance vs. the best model on that dataset; averaged with a geometric mean over the model's unseen datasets (Section 3.2). Mixes classification and regression datasets."},
              "metrics": [{"name": "avg-relative-deterioration-pct", "higher_is_better": False, "definition": "Table 3: average relative performance deterioration (%)."}],
              "defined_in": ID})
reg_doc = yaml.safe_load(open("registry/benchmarks.yaml")) or {}
reg_doc["benchmarks"] = [b for b in (reg_doc.get("benchmarks") or []) if b["defined_in"] != ID] + bench
header = "".join(l for l in open("registry/benchmarks.yaml") if l.startswith("#"))
open("registry/benchmarks.yaml", "w").write(header + yaml.safe_dump(reg_doc, sort_keys=False, allow_unicode=True, width=200))
print(len(results), "results,", len(claims), "claims,", len(bench), "benchmarks")
