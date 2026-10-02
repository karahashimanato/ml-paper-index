"""TabPFN (Hollmann et al., ICLR 2023) のカード。Table 1 は手法が列方向に並ぶので、行(指標)ごとに列位置で手法に対応させる。"""

import re
import sys

sys.path.insert(0, "scripts/cards")
from _common import Paper, register, write_card  # noqa: E402

P = Paper("arxiv-2207.01848")
METHODS = ["LightGBM", "CatBoost", "XGBoost", "Auto-sklearn 2.0", "AutoGluon", "TabPFN (no ensembling)", "TabPFN", "TabPFN + AutoGluon"]
# (表の行ラベル, 指標名, 大きいほど良いか)
ROWS = [("M. rank AUC OVO", "mean-rank-roc-auc-ovo", False), ("Mean rank Acc.", "mean-rank-accuracy", False),
        ("Mean rank CE", "mean-rank-cross-entropy", False), ("Mean AUC OVO", "mean-roc-auc-ovo", True),
        ("Mean Acc.", "mean-accuracy", True), ("Mean CE", "mean-cross-entropy", False)]
BENCH = "hollmann2023-cc18-small-numerical"
CELL = r"([0-9.]+)(?:±([0-9.]+))?"

t = P.text(8)
t = t[t.index("TabPFN + AutoGluon M. rank"):t.index("Mean time")]
results = []
for i, (label, metric, _) in enumerate(ROWS):
    nxt = ROWS[i + 1][0] if i + 1 < len(ROWS) else None
    seg = t[t.index(label) + len(label):t.index(nxt) if nxt else len(t)].strip()
    cells = seg.split(" ")
    assert len(cells) == len(METHODS), (label, cells)
    quote = f"{label} {seg}"
    for m, cell in zip(METHODS, cells):
        g = re.fullmatch(CELL, cell)
        assert g, cell
        r = {"id": f"r{len(results) + 1}", "benchmark": BENCH, "method": m, "metric": metric, "value": float(g.group(1))}
        if g.group(2):
            r["std"] = float(g.group(2))
            r["note"] = "± is the standard deviation (Table 1 caption)."
        r.update({"location": "Table 1", "page": 8, "quote": quote})
        results.append(r)

claims = P.claims([
  ("On the 18 small numerical OpenML-CC18 datasets, TabPFN clearly outperformed boosted trees and was on par with AutoML systems, with up to 230x speedup.", "Abstract",
   "we show that our method clearly outperforms boosted trees and performs on par with complex state-of-the-art AutoML systems with up to 230× speedup."),
  ("TabPFN targets small tasks: up to 1,000 training examples, 100 purely numerical features without missing values, and 10 classes.", "Section 1",
   "tasks (≤1 000 training examples, ≤100 purely numerical features without missing values and ≤10 classes)"),
  ("TabPFN is pre-trained once, offline, on synthetic datasets (12-layer Transformer, 20 hours on 8 GPUs); the same model is used for all evaluations.", "Section 3",
   "we trained a 12-layer Transformer for 18 000 batches of 512 synthetically generated datasets each, which required a total of 20 hours on one machine with 8 GPUs (Nvidia RTX 2080 Ti)."),
  ("TabPFN predicts by in-context learning: training examples are given as input and no parameters are updated on the new dataset.", "Abstract",
   "TabPFN performs in-context learning (ICL), it learns to make predictions using sequences of labeled examples (x, f(x)) given in the input, without requiring further parameter updates."),
  ("The synthetic-data prior is based on structural causal models with a preference for simple structures (mixed with a BNN prior).", "Abstract",
   "This prior incorporates ideas from causal reasoning: It entails a large space of structural causal models with a preference for simple structures."),
  ("No method, including TabPFN, was best on all individual datasets; TabPFN lost even to default baselines on some.", "Section 5.2",
   "no classification method, including TabPFN, performs best on all individual datasets."),
  ("TabPFN is weaker when categorical features or missing values are present.", "Section 5.2",
   "Generally, TabPFN is less strong when categorical features or missing values are present."),
  ("Evaluation: 5 repetitions per dataset, each with its own seed and a 50/50 train/test split shared by all methods.", "Section 5.2",
   "each with a different random seed and train- and test split (50% train and 50% test samples; all methods used the same split given a seed)."),
  ("Test datasets: all OpenML-CC18 datasets with up to 2,000 samples (1,000 for training), 100 features and 10 classes (30 datasets; 18 purely numerical without missing values).", "Section 5.2",
   "As test datasets, we used all datasets from the curated open-source OpenML-CC18 benchmark suite (Bischl et al., 2021) that contain up to 2 000 samples (1 000 for the training split), 100 features and 10 classes."),
  ("Averaging TabPFN and AutoGluon predictions strongly outperformed all other methods in Table 1; TabPFN's errors are relatively uncorrelated with the baselines'.", "Section 5.2",
   "averaging the predictions of TabPFN and AutoGluon; this strongly outperforms all other methods."),
  ("On the small datasets of the OpenML-AutoML Benchmark, using official baseline results, TabPFN outperformed all baselines in mean cross-entropy, accuracy and the OpenML metric.", "Section 5.2",
   "TabPFN outperformed all baselines in terms of mean cross-entropy, accuracy and the OpenML Metric"),
  ("Limitation: the Transformer architecture only scales to small datasets.", "Section 6",
   "the underlying Transformer architecture only scales to small datasets"),
  ("TabPFN generalized to training-set sizes larger than those seen during prior-fitting.", "Section 5.2",
   "Surprisingly, our models generalize beyond sample sizes seen during training"),
  ("Baselines were tuned by random search with 5-fold cross-validation until a time budget was exhausted.", "Section 5.2",
   "we used 5-fold cross-validation to evaluate randomly drawn hyperparameter configurations until a given budget was exhausted"),
  ("On all 30 test datasets (including categorical/missing), aggregate results were still strong but weaker than on purely numerical data.", "Section 5.2",
   "still show strong aggregate performance for TabPFN, albeit not as strong as for the purely numerical case"),
  ("TabPFN needs no hyperparameter tuning.", "Abstract",
   "needs no hyperparameter tuning and is competitive with state-of-the-art classification methods"),
  ("Results are aggregated across datasets as average ROC AUC (OVO for multiclass), ranks and wins with 95% confidence intervals.", "Section 5.2",
   "we report the ROC AUC (one-vs-one (OVO) for multi-class classification) average, ranks and wins including the 95% confidence interval"),
])

write_card({
  "id": P.id,
  "title": "TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second",
  "authors": ["Noah Hollmann", "Samuel Müller", "Katharina Eggensperger", "Frank Hutter"],
  "year": 2023,
  "venue": "ICLR 2023",
  "links": {"arxiv": "https://arxiv.org/abs/2207.01848", "code": "https://github.com/automl/TabPFN"},
  "source": {"version": "arXiv v6", "retrieved_at": "2026-10-02", "pdf_sha256": P.sha256()},
  "tags": {"tasks": ["tabular-classification"],
           "method_families": ["tabular-foundation-model", "gradient-boosted-trees", "automl-systems"],
           "paradigms": ["in-context-learning"]},
  "proposes": ["TabPFN"],
  "claims": claims,
  "results": results,
  "relations": [],
  "card": {"created_at": "2026-10-02", "created_by": "claude-opus-5-5 via Claude Code", "reviewed": False,
           "notes": ("Table 1 lists methods as columns; values were extracted mechanically row by row and mapped to methods by column position. "
                     "The 'Mean time' row (mixed CPU/GPU) was not recorded. Baselines had a 60-minute budget per split; TabPFN is not tuned. "
                     "Results are aggregates over 18 datasets x 5 splits; per-dataset results (Appendix) were not recorded. "
                     "This is the 2023 TabPFN (v1); later TabPFN versions are different models.")},
})

COMMON = {"split": "5 repetitions, each with its own seed and a random 50% train / 50% test split shared by all methods (Section 5.2).",
          "preprocessing": "Baselines: mean imputation, one-hot/ordinal encoding, feature normalization where necessary; TabPFN: own preprocessing with 32 ensembled permutations (Sections 3, 5.2).",
          "tuning": "Baselines: random search with 5-fold CV, 60 minutes requested per split, maximizing ROC AUC OVO where available; TabPFN: no tuning.",
          "repetitions": "Aggregated over 18 datasets x 5 splits; ranks and means across datasets (Table 1)."}
metrics = [{"name": m, "higher_is_better": hib} for _, m, hib in ROWS]
register(P.id, [{"id": BENCH, "scope": "paper-private", "task": "tabular-classification",
                 "dataset": "18 OpenML-CC18 datasets with <=2,000 samples, <=100 numerical features, no missing values, <=10 classes",
                 "protocol": COMMON, "metrics": metrics, "defined_in": P.id}])
print(len(results), "results,", len(claims), "claims")
