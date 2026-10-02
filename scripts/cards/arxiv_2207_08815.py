import sys, yaml, hashlib, pymupdf
sys.path.insert(0, "scripts")  # リポジトリのルートから実行する
from verify_quotes import variants, match
ID = "arxiv-2207.08815"
pdf = f"cache/pdfs/{ID}.pdf"
pages = [variants(p.get_text()) for p in pymupdf.open(pdf)]
def page_of(q):
    hits = [i + 1 for i, p in enumerate(pages) if match(q, [p]) == "exact"]
    assert len(hits) == 1, (q, hits)
    return hits[0]

claims = [
  ("Tree-based models remained state-of-the-art on medium-sized data (~10K training samples), even without counting their faster training.", "Abstract",
   "Results show that tree-based models remain state-of-the-art on medium-sized data"),
  ("Authors derive three challenges for tabular NNs: robustness to uninformative features, preserving data orientation, and learning irregular functions.", "Abstract",
   "be robust to uninformative features, 2. preserve the orientation of the data, and 3. be able to easily learn irregular functions."),
  ("Categorical variables are not the main weakness of NNs: most of the gap remains with numerical features only.", "Section 4.2",
   "Still, most of this gap subsists when learning on numerical features only."),
  ("Smoothing the training targets hurt tree-based models markedly but barely affected NNs, suggesting NNs are biased towards smooth solutions.", "Section 5.2",
   "For small lengthscales, smoothing the target function on the train set decreases markedly the accuracy of tree-based models, but barely impacts that of NNs."),
  ("MLP-like NNs (Resnet) were less robust to uninformative features: removing them narrowed the gap, adding them widened it.", "Section 5.3",
   "This shows that MLPs are less robust to uninformative features"),
  ("Under random rotation of the features, only Resnet was rotationally invariant (its accuracy was unaffected), unlike the other models.", "Section 5.4",
   "only Resnets are rotationally invariant"),
  ("Hyperparameters were tuned by random search of about 400 iterations per dataset.", "Section 3.3",
   "We run a random search of ≈400 iterations per dataset"),
  ("Training sets of bigger datasets were truncated to 10,000 samples (medium-sized regime).", "Section 3.2",
   "We truncate the training set to 10,000 samples for bigger datasets."),
  ("Multiclass targets were binarised to the two most frequent classes and balanced.", "Section 3.2",
   "For classification, the target is binarised if there are several classes, by taking the two most numerous classes, and we keep half of samples in each class."),
  ("Datasets where a default linear model scores within 5% of both a default Resnet and a default HistGradientBoosting were removed as too easy.", "Section 3.1",
   "Specifically, we remove a dataset if a default Logistic Regression (or Linear Regression for regression) reach a score whose relative difference"),
  ("All missing data were removed, so missing-value handling is out of scope.", "Section 3.2",
   "We remove all missing data from the datasets."),
  ("With a 50,000-sample training set (few eligible datasets), the gap between NNs and tree-based models seemed to shrink in most cases.", "Appendix A.2",
   "it seems that, in most cases, increasing the train set size reduces the gap between neural networks and tree-based models."),
  ("Per unit of random-search time (rather than iterations), tree-based models were always well above NNs (hardware differs, so not a rigorous speed comparison).", "Appendix A.2",
   "for the same amount of time spent on random search, tree-based models scores are always high above neural networks."),
  ("The benchmark consists of 45 datasets from varied domains.", "Abstract",
   "We define a standard set of 45 datasets from varied domains"),
  ("Scores for a given search budget are averaged over 15 shuffles of the random-search order (bootstrap-like estimate).", "Section 3.3",
   "We do this 15 times while shuffling the random search order at each time."),
]
TREES = "Tree-based models (RandomForest, GradientBoostingTrees, XGBoost)"
NNS = "Neural networks (MLP, Resnet, FT_Transformer, SAINT)"
q_budget = "Tree-based models are superior for every random search budget, and the performance gap stays wide even after a large number of random search iterations."
q_rot = "More striking, random rotations reverse the performance order: NNs are now above tree-based models and Resnets above FT Transformers."
SETTINGS = [("num-clf", "Figure 1"), ("num-reg", "Figure 1"), ("cat-clf", "Figure 2"), ("cat-reg", "Figure 2")]
relations = [{"winner": TREES, "loser": NNS, "benchmark": f"grinsztajn2022-medium-{s}",
              "basis": f"Normalized test score averaged over the benchmark's datasets, at every random-search budget ({fig}).",
              "location": "Section 4.2", "page": page_of(q_budget), "quote": q_budget} for s, fig in SETTINGS]
relations += [
  {"winner": NNS, "loser": TREES, "basis": "After randomly rotating the features of the numerical classification benchmark (Figure 6a); not the original benchmark condition.",
   "location": "Section 5.4", "page": page_of(q_rot), "quote": q_rot},
  {"winner": "Resnet", "loser": "FT_Transformer", "basis": "After randomly rotating the features of the numerical classification benchmark (Figure 6a); not the original benchmark condition.",
   "location": "Section 5.4", "page": page_of(q_rot), "quote": q_rot},
]
card = {
  "id": ID,
  "title": "Why do tree-based models still outperform deep learning on tabular data?",
  "authors": ["Léo Grinsztajn", "Edouard Oyallon", "Gaël Varoquaux"],
  "year": 2022,
  "links": {"arxiv": "https://arxiv.org/abs/2207.08815", "code": "https://github.com/LeoGrin/tabular-benchmark"},
  "source": {"version": "arXiv v1", "retrieved_at": "2026-10-02", "pdf_sha256": hashlib.sha256(open(pdf, "rb").read()).hexdigest()},
  "tags": {"tasks": ["tabular-classification", "tabular-regression"],
           "method_families": ["gradient-boosted-trees", "random-forests", "tabular-mlp", "tabular-attention"],
           "paradigms": ["supervised"]},
  "proposes": ["Tabular benchmark of 45 OpenML datasets with random-search-budget-aware evaluation"],
  "claims": [{"id": f"c{i}", "statement": s, "location": loc, "page": page_of(q), "quote": q} for i, (s, loc, q) in enumerate(claims, 1)],
  "results": [],
  "relations": relations,
  "card": {"created_at": "2026-10-02", "created_by": "claude-opus-5-5 via Claude Code", "reviewed": False,
           "notes": ("Main results are only given as curves (Figures 1-2, 7-12); no numeric result table in v1, so no 'results' were recorded "
                     "(reading values off figures would not be checkable against the text). Win/loss is recorded as 'relations' from explicit statements. "
                     "Version: arXiv v1 (preprint, 'Under review'); later versions may differ. Dataset selection used default Resnet and HistGradientBoosting "
                     "scores ('not too easy', c10), which the reader may want to keep in mind when interpreting the benchmark.")},
}
yaml.safe_dump(card, open(f"papers/{ID}.yaml", "w"), sort_keys=False, allow_unicode=True, width=200)

COMMON = {"split": "70% train (capped at 10,000 samples), remaining 30% split 30/70 into validation/test (each capped at 50,000); 1-5 folds depending on test size (Appendix A).",
          "preprocessing": "No missing data; multiclass binarised to two balanced classes; categorical features with >20 levels removed; numerical features with <10 unique values removed; QuantileTransformer for NNs; heavy-tailed regression targets log-transformed; one-hot for models without native categorical support (Sections 3.2, 3.5).",
          "tuning": "Random search of ~400 iterations per model and dataset starting from defaults; scores for budget n are the test score of the best-on-validation configuration among n iterations, averaged over 15 shuffles of the search order (Section 3.3).",
          "repetitions": "15 shuffles of the random-search order (Section 3.3)."}
bench = []
for s, suite, n, task, metric in [("num-clf", "298", 15, "tabular-classification", "normalized-accuracy"),
                                  ("num-reg", "297", 19, "tabular-regression", "normalized-r2"),
                                  ("cat-clf", "300", 7, "tabular-classification", "normalized-accuracy"),
                                  ("cat-reg", "299", 14, "tabular-regression", "normalized-r2")]:
    bench.append({"id": f"grinsztajn2022-medium-{s}", "scope": "public", "task": task,
                  "dataset": f"Grinsztajn et al. medium-sized benchmark, {'numerical' if s.startswith('num') else 'numerical + categorical'} features, {'classification' if s.endswith('clf') else 'regression'} ({n} datasets)",
                  "protocol": COMMON,
                  "metrics": [{"name": metric, "higher_is_better": True,
                               "definition": ("Test accuracy (classification) or R2 (regression) affinely rescaled per dataset between the top model (1) and the 10% (classification) / 50% (regression) "
                                              "test-error quantile model (0), negative values clipped to 0 for regression, then averaged over datasets (Section 3.4).")}],
                  "defined_in": ID, "external_ids": {"openml_benchmark_suite": suite}})
reg_doc = yaml.safe_load(open("registry/benchmarks.yaml")) or {}
reg_doc["benchmarks"] = [b for b in (reg_doc.get("benchmarks") or []) if b["defined_in"] != ID] + bench
header = "".join(l for l in open("registry/benchmarks.yaml") if l.startswith("#"))
open("registry/benchmarks.yaml", "w").write(header + yaml.safe_dump(reg_doc, sort_keys=False, allow_unicode=True, width=200))
print(len(claims), "claims,", len(relations), "relations,", len(bench), "benchmarks")
