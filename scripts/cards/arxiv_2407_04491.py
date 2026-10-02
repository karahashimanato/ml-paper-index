"""RealMLP / "Better by Default" (Holzmüller et al., NeurIPS 2024) のカード。
主結果 (Figure 2, 3) は図のため relations に記録する。付録 D のデータセット別の数値表は未記録(カードの notes 参照)。"""

import sys

sys.path.insert(0, "scripts/cards")
from _common import Paper, register, write_card  # noqa: E402

P = Paper("arxiv-2407.04491")
TRAIN, TEST, GRIN = "holzmuller2024-meta-train", "holzmuller2024-meta-test", "holzmuller2024-grinsztajn"

claims = P.claims([
  ("RealMLP offers a favorable time-accuracy tradeoff compared with other neural baselines and is competitive with GBDTs on medium-to-large datasets.", "Abstract",
   "RealMLP offers a favorable time-accuracy tradeoff compared to other neural baselines and is competitive with GBDTs in terms of benchmark scores."),
  ("Combining RealMLP and GBDTs with improved default parameters gives excellent results without hyperparameter tuning.", "Abstract",
   "a combination of RealMLP and GBDTs with improved default parameters can achieve excellent results without hyperparameter tuning."),
  ("Defaults are tuned on a meta-train benchmark of 118 datasets and evaluated on a disjoint meta-test benchmark of 90 datasets.", "Abstract",
   "We tune RealMLP and the default parameters on a meta-train benchmark with 118 datasets and compare them to hyperparameter-optimized versions on a disjoint meta-test benchmark with 90 datasets"),
  ("The benchmarks cover medium-to-large datasets (1K-500K samples).", "Abstract",
   "Our benchmark results on medium-to-large tabular datasets (1K–500K samples)"),
  ("Unlike McElfresh et al., who favor tuning CatBoost over trying NNs, the authors' results favor model portfolios as in AutoML systems.", "Section 5",
   "Unlike McElfresh et al. [43], who argue in favor of CatBoost-HPO over trying NNs, our results favor model portfolios as used in modern AutoML systems [10]."),
  ("Trying all default (tuned-default) algorithms is faster and very often better than naive single-algorithm HPO.", "Section 5",
   "Simply trying all default algorithms is faster and very often better than (naive) single-algorithm HPO."),
  ("RealMLP's tuned defaults transfer very well from meta-train to meta-test.", "Section 5",
   "indicating that the tuned defaults transfer very well to the meta-test benchmark."),
  ("For GBDTs, tuned defaults match HPO on meta-train but not on meta-test (still clearly better than library defaults).", "Section 5",
   "For GBDTs, tuned defaults are competitive with HPO on the meta-train set, but not as good on the meta-test set."),
  ("Using AUROC instead of classification error favors GBDTs.", "Section 5 (discussion)",
   "For classification, using AUROC instead of classification error (Figure 3, Appendix B.5) favors GBDTs."),
  ("Aggregation metrics other than the shifted geometric mean reduce the advantage of tuned-default methods.", "Section 5 (discussion)",
   "The use of different aggregation metrics than the shifted geometric mean reduces the advantage of TD methods"),
  ("Non-architectural aspects are not equalized across NN models, so the work is not a comparison of architectures.", "Limitations (end of Section 5)",
   "our work should therefore not be seen as a comparison of architectures."),
  ("Generalization of the defaults to very small data, distribution shift, missing numerical values and other metrics such as log-loss is unclear.", "Limitations (end of Section 5)",
   "it is unclear to which extent the obtained defaults can generalize to very small datasets, distribution shifts, datasets with missing numerical values, and other metrics such as log-loss."),
  ("Each dataset is evaluated on 10 random 60/20/20 train/validation/test splits.", "Section 2.2",
   "we evaluate a method on Nsplits = 10 random training-validation-test splits (60%-20%-20%) on each dataset."),
  ("HPO uses 50 steps of random search per split and dataset.", "Section 5",
   "Hyperparameters optimized separately for every train-test split on every dataset, using 50 steps of random search."),
  ("XGBoost results on some (mainly meta-test) datasets are affected by a bug in handling rare categories.", "Figure 2 caption",
   "Note that XGB results on some (mainly meta-test) datasets are affected by a bug in handling rare categories, see Appendix B.", 8),
  ("On the electricity dataset MLPs struggle to learn high-frequency patterns.", "Section 5",
   "where MLPs struggle to learn high-frequency patterns"),
  ("Among GBDTs, CatBoost defaults are better but slower.", "Section 5",
   "Among GBDTs, CatBoost defaults are better and slower."),
  ("RealMLP's numerical preprocessing (robust scaling + smooth clipping) is easy to adopt and often helps other NNs.", "Section 5 (discussion)",
   "our numerical preprocessing is easy to adopt and often beneficial for other NNs as well"),
  ("Label smoothing is influential but can hurt metrics like AUROC.", "Section 5 (discussion)",
   "label smoothing is influential but can be detrimental for metrics like AUROC"),
  ("A single training-validation split per train-test split means HPO can overfit the validation set more easily than with cross-validation.", "Limitations (end of Section 5)",
   "This means that HPO can overfit the validation set more easily than in a cross-validation setup."),
  ("With good default parameters it is worth trying both NNs and GBDTs, even with a moderate time budget.", "Section 6 (Conclusion)",
   "with good default parameters, it is worth trying both algorithm families even with a moderate training time budget."),
])


def rel(winner, loser, basis, bench, quote, location):
    r = {"winner": winner, "loser": loser, "basis": basis, "location": location, "page": P.page_of(quote), "quote": quote}
    if bench:
        r["benchmark"] = bench
    return r


q_gbdt = "On the meta-train and meta-test benchmarks, RealMLP and RealTabR perform better than GBDTs in terms of shifted geometric mean error"
q_grin = "On the Grinsztajn et al. [18] benchmark, RealMLP performs worse than CatBoost for classification and comparably for regression, while RealTabR-D performs comparably to CatBoost-TD for classification and better for regression."
relations = [
  rel("RealMLP and RealTabR", "GBDTs (XGBoost, LightGBM, CatBoost)", "Shifted geometric mean error on the meta-train benchmarks (Figure 2); the sentence does not specify D/TD/HPO variants.",
      TRAIN, q_gbdt, "Section 5"),
  rel("RealMLP and RealTabR", "GBDTs (XGBoost, LightGBM, CatBoost)", "Shifted geometric mean error on the meta-test benchmarks (Figure 2); the sentence does not specify D/TD/HPO variants.",
      TEST, q_gbdt, "Section 5"),
  rel("CatBoost", "RealMLP", "Grinsztajn et al. classification benchmark under this paper's protocol (Figure 2).", GRIN, q_grin, "Section 5"),
  rel("RealTabR-D", "CatBoost-TD", "Grinsztajn et al. regression benchmark under this paper's protocol (Figure 2).", GRIN, q_grin, "Section 5"),
  rel("RealTabR-D", "RealMLP-TD", "Four out of six benchmarks, especially all regression benchmarks (Figure 2).", None,
      "RealTabR-D performs even better on four out of six benchmarks, especially all regression benchmarks.", "Section 5"),
  rel("RealMLP-HPO", "Best-D (best of library-default XGB, LGBM, CatBoost, MLP-PLR)", "Benchmark scores in Figure 2 ('often').", None,
      "Best-D is often outperformed by RealMLP-HPO.", "Section 5"),
]

write_card({
  "id": P.id,
  "title": "Better by Default: Strong Pre-Tuned MLPs and Boosted Trees on Tabular Data",
  "authors": ["David Holzmüller", "Léo Grinsztajn", "Ingo Steinwart"],
  "year": 2024,
  "venue": "NeurIPS 2024",
  "links": {"arxiv": "https://arxiv.org/abs/2407.04491", "doi": "https://doi.org/10.18419/darus-4555"},
  "source": {"version": "arXiv v3", "retrieved_at": "2026-10-02", "pdf_sha256": P.sha256()},
  "tags": {"tasks": ["tabular-classification", "tabular-regression"],
           "method_families": ["tabular-mlp", "gradient-boosted-trees", "random-forests", "tabular-attention"],
           "paradigms": ["supervised"]},
  "proposes": ["RealMLP", "Tuned default parameters (TD) for XGBoost, LightGBM, CatBoost and RealMLP", "RealTabR-D"],
  "claims": claims,
  "results": [],
  "relations": relations,
  "card": {"created_at": "2026-10-02", "created_by": "claude-opus-5-5 via Claude Code", "reviewed": False,
           "notes": ("Aggregate results are figures (Figures 2, 3); recorded as relations. Appendix D (Tables D.1-D.12) contains per-dataset errors for all "
                     "methods and could be extracted mechanically in the future; not recorded yet. "
                     "The 'link' doi in links is the code/data archive stated in the paper, not the paper's DOI. "
                     "The first author is also a TabArena author (see arxiv-2506.16791 c22).")},
})

COMMON = {"split": "10 random 60/20/20 train/validation/test splits per dataset; rows with missing numerical values removed (Sections 2.1-2.2).",
          "preprocessing": "Method-specific; RealMLP uses robust scaling + smooth clipping and one-hot for low-cardinality categoricals (Section 3).",
          "tuning": "Library defaults (D), tuned defaults from the meta-train benchmark (TD), or 50-step random-search HPO per split (Section 5).",
          "repetitions": "Shifted geometric mean of errors over datasets (eps = 0.01), with dataset weights on meta-train (Section 2.2)."}
metrics = [{"name": "sgm-classification-error", "higher_is_better": False, "definition": "Shifted geometric mean of classification error over datasets (Section 2.2)."},
           {"name": "sgm-nrmse", "higher_is_better": False, "definition": "Shifted geometric mean of normalized RMSE over datasets (Section 2.2)."}]
register(P.id, [
  {"id": TRAIN, "scope": "paper-private", "task": "tabular-classification",
   "dataset": "Meta-train benchmark: 118 medium-sized UCI-derived datasets (classification and regression)", "protocol": COMMON, "metrics": metrics, "defined_in": P.id},
  {"id": TEST, "scope": "paper-private", "task": "tabular-classification",
   "dataset": "Meta-test benchmark: 90 datasets from the AutoML Benchmark and OpenML-CTR23 (classification and regression)", "protocol": COMMON, "metrics": metrics, "defined_in": P.id},
  {"id": GRIN, "scope": "paper-private", "task": "tabular-classification",
   "dataset": "Grinsztajn et al. benchmark datasets evaluated under this paper's protocol (not the original Grinsztajn protocol)", "protocol": COMMON, "metrics": metrics, "defined_in": P.id},
])
print(len(claims), "claims,", len(relations), "relations")
