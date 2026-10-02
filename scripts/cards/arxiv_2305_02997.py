"""TabZilla (McElfresh et al., NeurIPS 2023 D&B) のカード。Table 1 (98 datasets) と Table 2 (57 datasets <= 1250) を行ごとに読む。"""

import sys

sys.path.insert(0, "scripts/cards")
from _common import Paper, register, write_card  # noqa: E402

P = Paper("arxiv-2305.02997")
ALGS = ["CatBoost", "TabPFN∗", "XGBoost", "ResNet", "SAINT", "NODE", "FTTransformer", "RandomForest", "LightGBM", "SVM",
        "DANet", "MLP-rtdl", "STG", "DecisionTree", "LinearModel", "MLP", "TabNet", "KNN", "VIME"]
CLASSES = {"GBDT", "NN", "PFN", "base"}
# 10 列: Rank min/max/mean/med, Mean Acc. mean/med, Std. Acc. mean/med, Time /1000 inst. mean/med
COLS = {2: ("mean-rank", False), 4: ("mean-normalized-accuracy", True), 5: ("median-normalized-accuracy", True),
        6: ("mean-fold-std-normalized-accuracy", False), 8: ("mean-train-time-per-1000", False)}


def table(page: int, start: str, has_class: bool):
    """start の行からページ末尾までを走査し、アルゴリズム名の行 + (クラス) + 10個の数値を1行として読む。"""
    ls = P.lines(page)
    body = ls[ls.index(start):]
    rows, k = {}, 0
    while k < len(body):
        name = body[k]
        if name not in ALGS:
            k += 1
            continue
        off = 2 if has_class else 1
        if has_class:
            assert body[k + 1] in CLASSES, (name, body[k + 1])
        vals = body[k + off:k + off + 10]
        assert all(v.replace(".", "", 1).isdigit() for v in vals), (name, vals)
        rows[name] = (vals, " ".join(body[k:k + off + 10]))
        k += off + 10
    return rows


results = []
for bench, page, start, has_class, n in [("mcelfresh2023-98-datasets", 4, "CatBoost", True, 19),
                                          ("mcelfresh2023-57-small-datasets", 5, "TabPFN∗", False, 19)]:
    rows = table(page, start, has_class)
    assert len(rows) == n, (bench, len(rows), sorted(set(ALGS) - set(rows)))
    loc = "Table 1" if page == 4 else "Table 2"
    for alg, (vals, quote) in rows.items():
        method = "TabPFN* (3000-sample subset)" if alg == "TabPFN∗" else alg
        for col, (metric, _) in COLS.items():
            results.append({"id": f"r{len(results) + 1}", "benchmark": bench, "method": method, "metric": metric, "value": float(vals[col]),
                            "location": loc, "page": page, "quote": quote})

claims = P.claims([
  ("The 'NN vs. GBDT' debate is overemphasized: for many datasets the GBDT-NN difference is negligible or light GBDT tuning matters more than the choice.", "Abstract",
   "we find that the 'NN vs. GBDT' debate is overemphasized"),
  ("Light hyperparameter tuning of a GBDT is often more important than choosing between NNs and GBDTs.", "Abstract",
   "light hyperparameter tuning on a GBDT is more important than choosing between NNs and GBDTs"),
  ("TabPFN outperformed all other algorithms on average, even when only a random 3000-sample subset of the training data was used.", "Abstract",
   "we find that it outperforms all other algorithms on average, even when randomly sampling 3000 training datapoints."),
  ("GBDTs handle skewed or heavy-tailed feature distributions and other dataset irregularities much better than NNs.", "Abstract",
   "GBDTs are much better than NNs at handling skewed or heavy-tailed feature distributions and other forms of dataset irregularities."),
  ("For about one-third of datasets, light tuning (30 random-search iterations) of CatBoost improved performance more than choosing between the best default GBDT and NN.", "Section 2.1",
   "Surprisingly, light hyperparameter tuning yields a greater performance improvement than GBDT-vs-NN selection for about one-third of all datasets."),
  ("GBDTs performed comparatively better than NNs and baselines on larger datasets.", "Section 2.2",
   "Throughout our metafeature analyses, we find that GBDTs perform comparatively better than NNs and baselines with larger datasets."),
  ("Authors' recommendation: try simple baselines first, then lightly tune CatBoost.", "Section 2.2",
   "first try simple baselines, and then conduct light hyperparameter tuning on CatBoost."),
  ("Each dataset uses the ten train/test folds provided by OpenML (comparable with other works using the same folds).", "Section 2",
   "For each dataset, we use the ten train/test folds provided by OpenML"),
  ("Each algorithm was evaluated with at most 30 hyperparameter sets (default + 29 random via Optuna), up to 10 hours per algorithm and split.", "Section 2",
   "we train and evaluate the algorithm with at most 30 hyperparameter sets (one default set and 29 random sets, using Optuna [3])."),
  ("The 98-dataset comparison excludes datasets on which many algorithms hit memory or time limits.", "Section 2.1",
   "while excluding datasets which ran into memory or timeout issues on a nontrivial number of algorithms"),
  ("On the 57 smallest datasets (<=1250 instances), TabPFN had the best average performance and the fastest training time.", "Section 2.1",
   "Now, we find that TabPFN achieves the best average performance of all algorithms, while also having the fastest training time."),
  ("The text states CatBoost's average rank is 5.06 (Table 1 shows a mean rank of 5.50 for CatBoost; the paper is inconsistent).", "Section 2.1",
   "The fact that the best out of all algorithms, CatBoost, only achieved an average rank of 5.06"),
  ("The text says Figure 3 uses accuracy and Table 1 log loss, but the Figure 3 caption says log loss and the Table 1 caption says accuracy (inconsistent).", "Section 2.1",
   "Note that the slight differences between Figure 3 and Table 1 is that the former uses accuracy, while the latter uses log loss."),
  ("By log-loss rank with Wilcoxon signed-rank tests (Holm-Bonferroni), TabPFN outperformed all other algorithms across the 98 datasets with statistical significance.", "Section 2.1, Figure 3",
   "We find that TabPFN outperforms all other algorithms on average across 98 datasets, and this result is statistically significant."),
  ("TabPFN was run on larger datasets by randomly subsampling 3000 training samples (TabPFN*).", "Section 2",
   "In order to run on datasets of size larger than 3000, we simply take a random sample of size 3000 from the full training dataset."),
  ("Dataset sizes range from 32 to 1,025,009 (vs. 3,000-10,000 or 50,000 in Grinsztajn et al.).", "Section 1",
   "in contrast to our dataset sizes which range from 32 to 1 025 009", 3),
  ("TabPFN was excluded from the GBDT-vs-NN family analyses because it works differently from other NNs.", "Section 2.1 footnote",
   "we exclude it from our analysis in this section and the next section when discussing 'GBDTs vs. NNs.'"),
  ("The TabZilla Benchmark Suite consists of the 36 'hardest' of the 176 datasets.", "Section 3",
   "a collection of the 36 'hardest' of the 176 datasets we studied in Section 2."),
  ("All 176 datasets are classification datasets from OpenML.", "Section 2",
   "We run the algorithms on 176 classification datasets from OpenML"),
  ("Across datasets, accuracy is aggregated with the average distance to the minimum (ADTM): per-dataset 0-1 scaling after selecting the best hyperparameters.", "Section 2",
   "we use the average distance to the minimum (ADTM) metric, which consists of 0-1 scaling"),
  ("The study compares 19 algorithms on 176 datasets.", "Abstract",
   "comparing 19 algorithms across 176 datasets"),
])

write_card({
  "id": P.id,
  "title": "When Do Neural Nets Outperform Boosted Trees on Tabular Data?",
  "authors": ["Duncan McElfresh", "Sujay Khandagale", "Jonathan Valverde", "Vishak Prasad C", "Benjamin Feuer", "Chinmay Hegde",
              "Ganesh Ramakrishnan", "Micah Goldblum", "Colin White"],
  "year": 2023,
  "venue": "NeurIPS 2023 Datasets and Benchmarks Track",
  "links": {"arxiv": "https://arxiv.org/abs/2305.02997", "code": "https://github.com/naszilla/tabzilla"},
  "source": {"version": "arXiv v4", "retrieved_at": "2026-10-02", "pdf_sha256": P.sha256()},
  "tags": {"tasks": ["tabular-classification"],
           "method_families": ["gradient-boosted-trees", "tabular-mlp", "tabular-attention", "differentiable-trees", "tabular-foundation-model",
                               "random-forests", "linear-models"],
           "paradigms": ["supervised", "in-context-learning"]},
  "proposes": ["TabZilla Benchmark Suite (36 hard OpenML classification datasets)"],
  "claims": claims,
  "results": results,
  "relations": [{"winner": "TabPFN* (3000-sample subset)", "loser": "All other 18 algorithms",
                 "basis": "Mean log-loss rank over the 98 datasets; Friedman test then Wilcoxon signed-rank tests with Holm-Bonferroni correction (Figure 3).",
                 "benchmark": "mcelfresh2023-98-datasets", "location": "Section 2.1, Figure 3",
                 "page": P.page_of("We find that TabPFN outperforms all other algorithms on average across 98 datasets, and this result is statistically significant."),
                 "quote": "We find that TabPFN outperforms all other algorithms on average across 98 datasets, and this result is statistically significant."}],
  "card": {"created_at": "2026-10-02", "created_by": "claude-opus-5-5 via Claude Code", "reviewed": False,
           "notes": ("Results extracted mechanically from Table 1 (98 datasets) and Table 2 (57 datasets <= 1250 instances); rank min/max and medians of rank/std/time were not recorded. "
                     "Table values are aggregates of accuracy-based quantities; the significance result (relation) is on log loss. "
                     "Two inconsistencies in the text (c12, c13). Training time depends on hardware and is per 1000 instances. "
                     "Normalized accuracy is 0-1 scaled per dataset (ADTM), so means are only comparable within the same dataset set.")},
})

COMMON = {"split": "Ten OpenML train/test folds per dataset; each training fold further split into training and validation (Section 2).",
          "preprocessing": "Algorithm-specific; TabPFN uses a random 3000-sample subset of the training data when larger (Section 2).",
          "tuning": "Up to 30 hyperparameter sets per algorithm and split (default + 29 random via Optuna), up to 10 hours per algorithm and split, 2 hours per train/eval cycle on a V100; the best-on-validation setting is reported (Section 2).",
          "repetitions": "Ten folds per dataset; accuracy 0-1 scaled per dataset (ADTM) and aggregated over datasets (Section 2)."}
metrics = [{"name": m, "higher_is_better": hib} for m, hib in COLS.values()]
register(P.id, [
  {"id": "mcelfresh2023-98-datasets", "scope": "paper-private", "task": "tabular-classification",
   "dataset": "98 of the 176 OpenML classification datasets (excluding those where many algorithms hit memory/time limits)",
   "protocol": COMMON, "metrics": metrics, "defined_in": P.id},
  {"id": "mcelfresh2023-57-small-datasets", "scope": "paper-private", "task": "tabular-classification",
   "dataset": "57 smallest datasets (<= 1250 instances) of the 176 OpenML classification datasets",
   "protocol": COMMON, "metrics": metrics, "defined_in": P.id},
  {"id": "tabzilla-suite", "scope": "public", "task": "tabular-classification",
   "dataset": "TabZilla Benchmark Suite: 36 'hard' OpenML classification datasets (Section 3, Table 4)",
   "protocol": COMMON, "metrics": [{"name": "log-loss", "higher_is_better": False}, {"name": "accuracy", "higher_is_better": True}],
   "defined_in": P.id, "notes": "Registered for future cards; this paper reports only per-dataset top-3 algorithms for the suite (Table 4)."},
])
print(len(results), "results,", len(claims), "claims")
