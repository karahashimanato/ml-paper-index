"""TabPFN v2 (Hollmann et al., Nature 2025) のカード。
集計表 (Extended Data Table 1, 2, 6) は画像のためテキストから読めない。本文中に数値で書かれた比較だけを results に、
数値なしの勝敗を relations に記録する。"""

import sys

sys.path.insert(0, "scripts/cards")
from _common import Paper, register, write_card  # noqa: E402

P = Paper("doi-10.1038_s41586-024-08328-6")
CLF, REG = "hollmann2025-amlb-small-classification", "hollmann2025-amlb-ctr23-small-regression"

# (本文の引用, [(比較条件, 手法, 指標, 値)])。値は引用中の数値をそのまま使う。
PROSE = [
  ("TabPFN surpasses CatBoost, the strongest default baseline, by 0.187 (0.939 compared with 0.752) in normalized ROC AUC in the default setting",
   [(CLF, "TabPFN v2 (default)", "normalized-roc-auc", 0.939), (CLF, "CatBoost (default)", "normalized-roc-auc", 0.752)]),
  ("and by 0.13 (0.952 compared with 0.822) in the tuned setting.",
   [(CLF, "TabPFN v2 (tuned)", "normalized-roc-auc", 0.952), (CLF, "CatBoost (tuned)", "normalized-roc-auc", 0.822)]),
  ("TabPFN outperforms CatBoost in normalized RMSE by 0.051 (0.923 compared with 0.872) in the default setting",
   [(REG, "TabPFN v2 (default)", "normalized-rmse", 0.923), (REG, "CatBoost (default)", "normalized-rmse", 0.872)]),
  ("and by 0.093 (0.968 compared with 0.875) in the tuned setting.",
   [(REG, "TabPFN v2 (tuned)", "normalized-rmse", 0.968), (REG, "CatBoost (tuned)", "normalized-rmse", 0.875)]),
  ("TabPFN (PHE) further improves performance leading to an average normalized ROC AUC score of 0.971, compared with 0.939 for TabPFN (default) and 0.914 for AutoGluon.",
   [(CLF, "TabPFN v2 (PHE)", "normalized-roc-auc", 0.971), (CLF, "AutoGluon 1.0", "normalized-roc-auc", 0.914)]),
]
results = []
for quote, rows in PROSE:
    page = P.page_of(quote)
    for bench, method, metric, value in rows:
        r = {"id": f"r{len(results) + 1}", "benchmark": bench, "method": method, "metric": metric, "value": value,
             "location": "Results (main text)", "page": page, "quote": quote}
        if method == "AutoGluon 1.0":
            r["note"] = "The sentence does not state AutoGluon's tuning budget (Fig. 5c shows budgets from 300 s up to 4 h)."
        results.append(r)

claims = P.claims([
  ("TabPFN v2 outperformed all previous methods on datasets with up to 10,000 samples by a wide margin, with much less training time.", "Abstract",
   "a tabular foundation model that outperforms all previous methods on datasets with up to 10,000 samples by a wide margin, using substantially less training time."),
  ("In 2.8 s, TabPFN v2 outperformed an ensemble of the strongest baselines tuned for 4 h (classification).", "Abstract",
   "In 2.8 s, TabPFN outperforms an ensemble of the strongest baselines tuned for 4 h in a classification setting."),
  ("Compared with the 2023 TabPFN, v2 scales to 50x larger datasets, supports regression, categorical data and missing values, and is robust to unimportant features and outliers.", "Introduction",
   "the new TabPFN scales to 50× larger datasets; supports regression tasks, categorical data and missing values; and is robust to unimportant features and outliers."),
  ("Training only on synthetic data avoids privacy/copyright issues and contamination of training data with test data.", "Architecture / prior",
   "By relying on synthetic data instead of large collections of public tabular data, we avoid common problems of foundational models, such as privacy and copyright infringements, contaminating our training data with test data"),
  ("About 100 million synthetic datasets (from structural causal models) are generated per model training.", "Synthetic data",
   "we created a massive corpus of around 100 million synthetic datasets per model training"),
  ("The architecture uses two-way attention: each cell attends within its row, then within its column, making it invariant to sample and feature order.", "Architecture",
   "uses a two-way attention mechanism, with each cell attending to the other features in its row (that is, its sample) and then attending to the same feature across its column (that is, all other samples)."),
  ("Primary evaluation: 29 classification and 28 regression datasets from the AutoML Benchmark and OpenML-CTR23 with up to 10,000 samples, 500 features and 10 classes.", "Results",
   "we use the 29 classification datasets and 28 regression datasets that have up to 10,000 samples, 500 features and 10 classes."),
  ("Each dataset and method: 10 repetitions with different seeds and 90/10 train/test splits.", "Results",
   "For each dataset and method, we ran 10 repetitions with different random seeds and train–test splits (90% train, 10% test)."),
  ("Baselines were tuned by random search with five-fold CV, with budgets from 30 s to 4 h.", "Results",
   "We tuned hyperparameters using random search with five-fold cross-validation, with time budgets ranging from 30 s to 4 h."),
  ("TabPFN v2 was pre-trained once on eight RTX 2080 GPUs for 2 weeks.", "Results",
   "TabPFN was pre-trained once using eight NVIDIA RTX 2080 GPUs over 2 weeks"),
  ("Scores are normalized per dataset, 1.0 = best and 0.0 = worst with respect to all baselines (so values depend on the set of baselines).", "Results",
   "Scores were normalized per dataset, with 1.0 representing the best and 0.0 the worst performance with respect to all baselines."),
  ("TabPFN v2 also substantially outperformed all baselines on the Grinsztajn et al. and McElfresh et al. (TabZilla) benchmarks (refs 14, 15).", "Results, Extended Data Fig. 2",
   "TabPFN substantially outperformed all baselines on the benchmarks of refs. 14,15."),
  ("Default TabPFN v2 beat default CatBoost on all five recent Kaggle tabular competitions with fewer than 10,000 training samples.", "Results, Extended Data Table 6",
   "default TabPFN outperforms default CatBoost on all five Kaggle competitions with less than 10,000 training samples"),
  ("Dataset characteristics (categorical features, missing values, size) did not strongly change TabPFN v2's relative performance, but this is not evidence that it scales beyond 10,000 samples and 500 features.", "Results",
   "these results should not be taken as evidence that TabPFN scales well beyond the 10,000 samples and 500 features considered here."),
  ("TabPFN v2 was very robust to added uninformative features and outliers.", "Results, Fig. 5a",
   "The results show that TabPFN is very robust to uninformative features and outliers"),
  ("With half the training samples, TabPFN v2 still performed as well as the next best method.", "Results, Fig. 5a",
   "with half the samples TabPFN still performs as well as the next best method"),
  ("For regression, hyperparameter tuning of TabPFN v2 matters more than for classification.", "Results",
   "For regression tasks, tuning hyperparameters is more important."),
  ("Competing interests: two authors are affiliated with PriorLabs (a tabular foundation model company); related patent applications were filed by Bosch.", "Competing interests",
   "F.H. and N.H. are affiliated with PriorLabs, a company focused on developing tabular foundation models."),
])


def rel(winner, loser, basis, bench, quote, location):
    return {"winner": winner, "loser": loser, "basis": basis, "benchmark": bench, "location": location, "page": P.page_of(quote), "quote": quote}


relations = [
  rel("TabPFN v2 (default, ~2.8 s / ~4.8 s)", "All baselines tuned for up to 4 h", "Normalized ROC AUC / RMSE vs. tuning time (Fig. 4c).", CLF,
      "The default of TabPFN, taking 2.8 s on average for classification and 4.8 s for regression, outperforms all baselines, even when tuning them for 4 h", "Results"),
  rel("TabPFN v2 (default)", "AutoGluon 1.0 (up to 4 h)", "Classification, normalized ROC AUC (Fig. 5c).", CLF,
      "In just 2.8 s, TabPFN (default) outperforms AutoGluon for classification tasks, even if AutoGluon is allowed up to 4 h", "Results"),
  rel("TabPFN v2 (PHE)", "AutoGluon 1.0 (allowed 4 h)", "Regression, normalized RMSE, after TabPFN (PHE)'s minimal 300 s budget (Fig. 5d).", REG,
      "TabPFN (PHE) outperforms AutoGluon (allowed 4 h) after its minimal", "Results"),
]

write_card({
  "id": P.id,
  "title": "Accurate predictions on small data with a tabular foundation model",
  "authors": ["Noah Hollmann", "Samuel Müller", "Lennart Purucker", "Arjun Krishnakumar", "Max Körfer", "Shi Bin Hoo",
              "Robin Tibor Schirrmeister", "Frank Hutter"],
  "year": 2025,
  "venue": "Nature 637, 319-326 (2025)",
  "links": {"doi": "https://doi.org/10.1038/s41586-024-08328-6"},
  "source": {"version": "Nature published version (open access)", "retrieved_at": "2026-10-02", "pdf_sha256": P.sha256(), "license": "CC BY 4.0"},
  "tags": {"tasks": ["tabular-classification", "tabular-regression"],
           "method_families": ["tabular-foundation-model", "gradient-boosted-trees", "automl-systems"],
           "paradigms": ["in-context-learning"]},
  "proposes": ["TabPFN v2"],
  "claims": claims,
  "results": results,
  "relations": relations,
  "card": {"created_at": "2026-10-02", "created_by": "claude-opus-5-5 via Claude Code", "reviewed": False,
           "notes": ("Aggregate tables (Extended Data Tables 1, 2, 6) are embedded as images and could not be extracted as text; only numbers stated in the main text "
                     "were recorded, quoting the sentence. Normalized scores depend on the set of baselines used for normalization (c11). "
                     "'TabPFN' in this paper is TabPFN v2, a different model from the 2023 TabPFN (arxiv-2207.01848). "
                     "Two authors are affiliated with PriorLabs (c18).")},
})

COMMON = {"split": "10 repetitions per dataset with different seeds and 90% train / 10% test splits (Results).",
          "preprocessing": "Method-specific; TabPFN v2 handles categorical features and missing values natively (Results, Methods).",
          "tuning": "Baselines: random search with 5-fold CV, budgets from 30 s to 4 h; TabPFN v2: default (no tuning), tuned, or PHE (post-hoc ensembled TabPFN v2 models, from 300 s).",
          "repetitions": "Scores normalized per dataset (1 = best, 0 = worst w.r.t. all baselines), then averaged over datasets (Results)."}
register(P.id, [
  {"id": CLF, "scope": "paper-private", "task": "tabular-classification",
   "dataset": "29 AutoML Benchmark classification datasets with <=10,000 samples, <=500 features, <=10 classes", "protocol": COMMON,
   "metrics": [{"name": "normalized-roc-auc", "higher_is_better": True, "definition": "ROC AUC (one-vs-rest) normalized per dataset over all baselines, averaged."}],
   "defined_in": P.id},
  {"id": REG, "scope": "paper-private", "task": "tabular-regression",
   "dataset": "28 AutoML Benchmark and OpenML-CTR23 regression datasets with <=10,000 samples, <=500 features", "protocol": COMMON,
   "metrics": [{"name": "normalized-rmse", "higher_is_better": True, "definition": "Negative RMSE normalized per dataset over all baselines (1 = best), averaged."}],
   "defined_in": P.id},
])
print(len(results), "results,", len(claims), "claims,", len(relations), "relations")
