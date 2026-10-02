"""TabM (Gorishniy et al., ICLR 2025) のカード。主結果 (Figure 2, 3) は図のため relations に、Table 2 (大規模データ2つの RMSE) は数値として記録する。"""

import re
import sys

sys.path.insert(0, "scripts/cards")
from _common import Paper, register, write_card  # noqa: E402

P = Paper("arxiv-2410.24210")
# Table 2 の列。† = piecewise-linear 埋め込み、♠ = 学習バッチ共有、∗ = AMP + torch.compile(本文: 他の深層モデルと直接比較しない)
COLS = ["XGBoost", "MLP", "TabM-mini† (shared batches, AMP + torch.compile)", "TabM-mini†", "FT-Transformer", "TabR"]
BENCH = {"Maps Routing": "gorishniy2025-maps-routing", "Weather": "gorishniy2025-weather"}

t = P.text(8)
results = []
for name, bench in BENCH.items():
    g = re.search(re.escape(name) + r" (\S+) (\S+) ((?:\S+ ){5}\S+)", t)
    assert g, name
    cells = g.group(3).split(" ")
    quote = g.group(0)
    for m, cell in zip(COLS, cells):
        if cell == "OOM":
            continue
        r = {"id": f"r{len(results) + 1}", "benchmark": bench, "method": m, "metric": "rmse", "value": float(cell),
             "location": "Table 2", "page": 8, "quote": quote}
        if "AMP" in m:
            r["note"] = "Efficiency-optimized variant; the paper says it should not be directly compared to other DL models (c19)."
        results.append(r)
    assert sum(1 for r in results if r["benchmark"] == bench) == 5, (name, cells)  # TabR は OOM

claims = P.claims([
  ("TabM showed the best performance among tabular deep learning models.", "Abstract",
   "In particular, we find that TabM demonstrates the best performance among tabular DL models."),
  ("MLP-based models, including TabM, are stronger and more practical than attention- and retrieval-based architectures.", "Abstract",
   "Generally, we show that MLPs, including TabM, form a line of stronger and more practical models compared to attention- and retrieval-based architectures."),
  ("TabM's multiple predictions are weak individually but powerful collectively.", "Abstract",
   "We observe that the multiple predictions of TabM are weak individually, but powerful collectively."),
  ("A plain MLP with BatchEnsemble already outperforms attention-based models such as FT-Transformer.", "Section 1",
   "MLP coupled with BatchEnsemble (Wen et al., 2020) — a long-existing method — right away outperforms popular attention-based models, such as FT-Transformer"),
  ("TabM competes with GBDT and outperforms prior tabular DL models while being more efficient.", "Section 1",
   "TabM easily competes with GBDT and outperforms prior tabular DL models"),
  ("The benchmark has 46 public datasets from prior work (incl. Grinsztajn et al., TabR, TabReD).", "Section 3.1",
   "Our benchmark consists of 46 publicly available datasets used in prior work"),
  ("Datasets with domain-aware (e.g. time-based) splits exhibit distribution shift and are challenging for some methods.", "Section 3.1",
   "Such datasets were shown to be challenging for some methods because they naturally exhibit a certain degree of distribution shift between training and test parts"),
  ("Protocol: tune on validation, retrain the tuned model under multiple seeds, report the test metric averaged over seeds.", "Section 3.1",
   "a given model undergoes hyperparameter tuning on the validation set, then the tuned model is trained from scratch under multiple random seeds, and the test metric averaged over the random seeds becomes the final score of the model on the dataset."),
  ("The ensemble size k is fixed at 32 and not tuned.", "Section 3.3",
   "We heuristically set k = 32 and do not tune this value."),
  ("Weight sharing among the implicit MLPs acts as an effective regularizer on tabular tasks.", "Section 3.3",
   "Thus, constraining the ensemble with weight sharing turns out to be a highly effective regularization on tabular tasks."),
  ("The two key reasons for TabM's performance are simultaneous training of the implicit MLPs and weight sharing.", "Section 1",
   "the two key reasons for TabM's high performance are the collective training of the underlying implicit MLPs and the weight sharing."),
  ("Many DL methods are no better, or worse, than a plain MLP on a non-negligible number of datasets.", "Section 4.2",
   "many DL methods turn out to be no better or even worse than MLP on a non-negligible number of datasets"),
  ("Simple MLPs are the fastest DL models and TabM is the runner-up; attention- and retrieval-based models are much slower.", "Section 4.3",
   "Simple MLPs are the fastest DL models, with TabM being the runner-up."),
  ("On large datasets, attention- and retrieval-based models need extremely long training or are inapplicable without extra effort.", "Section 4.3",
   "As expected, attention- and retrieval-based models struggle, yielding extremely long training times, or being simply inapplicable without additional effort."),
  ("Even the best individual submodel of TabM is no better than a simple MLP.", "Section 5.1",
   "individually, even the best submodel of TabM is no better than a simple MLP."),
  ("TabM's strength comes from the collective prediction of weak but diverse submodels.", "Section 5.1",
   "TabM draws its power from the collective prediction of weak, but diverse submodels."),
  ("Too large k can be detrimental.", "Section 5.3",
   "too high values of k can be detrimental."),
  ("MLP with piecewise-linear embeddings (MLP†) is a decent practical option between a plain MLP and TabM.", "Section 4.2",
   "MLP† seems to be a decent practical option between the plain MLP and TabM"),
  ("Variants with AMP and torch.compile (marked ∗) showcase efficiency and should not be directly compared to other DL models.", "Section 4.3",
   "they should not be directly compared to other DL models."),
  ("Metrics: RMSE for regression; accuracy or ROC-AUC for classification depending on the dataset source.", "Section 3.1",
   "We use RMSE (the root mean square error) for regression tasks, and accuracy or ROC-AUC for classification tasks depending on the dataset source."),
  ("Tabular MLPs have potential, but overfitting and optimization issues must be handled to reveal it.", "Related work",
   "one has to deal with overfitting and optimization issues to reveal that potential."),
])


def rel(winner, loser, basis, quote, location):
    return {"winner": winner, "loser": loser, "basis": basis, "benchmark": "gorishniy2025-46-datasets", "location": location,
            "page": P.page_of(quote), "quote": quote}


relations = [
  rel("TabM", "Other tabular DL models (MLP, FT-T, SAINT, T2G, Excel, TabR, ModernNCA and embedding variants)",
      "Mean performance rank over the 46 datasets (Figure 3); GBDTs are also in the figure but the statement is about DL models.",
      "The performance ranks render TabM as the top-tier DL model.", "Section 4.2"),
  rel("TabM-packed (MLP + Packed-Ensemble)", "MLPxk (deep ensemble of independently trained MLPs)", "Figure 2, tuned models on 46 datasets.",
      "TabMpacked delivers significantly better performance compared to MLP×k.", "Section 3.3"),
  rel("TabM-naive (MLP + BatchEnsemble)", "TabM-packed", "Figure 2, tuned models on 46 datasets.",
      "Interestingly, Figure 2 reports higher performance of TabMnaive compared to TabMpacked.", "Section 3.3"),
  rel("MLPxk (deep ensemble)", "FT-Transformer", "Figure 2, tuned models on 46 datasets.",
      "Notably, the results are already better and more stable than those of FT-Transformer", "Section 3.3"),
]

write_card({
  "id": P.id,
  "title": "TabM: Advancing Tabular Deep Learning with Parameter-Efficient Ensembling",
  "authors": ["Yury Gorishniy", "Akim Kotelnikov", "Artem Babenko"],
  "year": 2025,
  "venue": "ICLR 2025",
  "links": {"arxiv": "https://arxiv.org/abs/2410.24210", "code": "https://github.com/yandex-research/tabm"},
  "source": {"version": "arXiv v3", "retrieved_at": "2026-10-02", "pdf_sha256": P.sha256()},
  "tags": {"tasks": ["tabular-classification", "tabular-regression"],
           "method_families": ["tabular-mlp", "tabular-attention", "gradient-boosted-trees"],
           "paradigms": ["supervised"]},
  "proposes": ["TabM", "TabM-mini"],
  "claims": claims,
  "results": results,
  "relations": relations,
  "card": {"created_at": "2026-10-02", "created_by": "claude-opus-5-5 via Claude Code", "reviewed": False,
           "notes": ("Main comparisons (Figures 2, 3: ranks and relative improvement over MLP on 46 datasets) are figures; recorded as relations. "
                     "Table 2 (two large datasets) RMSE values extracted mechanically; training times in Table 2 were not recorded (strings such as '13.5h'). "
                     "TabR is OOM on both large datasets. Per-dataset appendix tables were not recorded.")},
})

COMMON = {"split": "Splits inherited from prior work; domain-aware (e.g. time-based) splits for TabReD datasets and Microsoft (Section 3.1).",
          "preprocessing": "Model-specific; feature embeddings for models marked † or ‡ (Section 4.1, Appendix D).",
          "tuning": "Hyperparameter tuning on the validation set following Gorishniy et al. (2024) (Appendix D.2).",
          "repetitions": "Tuned model retrained under multiple random seeds; test metric averaged over seeds (Section 3.1)."}
register(P.id, [
  {"id": "gorishniy2025-46-datasets", "scope": "paper-private", "task": "tabular-classification",
   "dataset": "46 public datasets (Grinsztajn et al., Gorishniy et al. 2024, TabReD, Microsoft); classification and regression", "protocol": COMMON,
   "metrics": [{"name": "mean-rank", "higher_is_better": False}], "defined_in": P.id},
  {"id": "gorishniy2025-maps-routing", "scope": "paper-private", "task": "tabular-regression",
   "dataset": "Maps Routing (6.5M objects, 986 features; large dataset of Table 2)", "protocol": COMMON,
   "metrics": [{"name": "rmse", "higher_is_better": False}], "defined_in": P.id},
  {"id": "gorishniy2025-weather", "scope": "paper-private", "task": "tabular-regression",
   "dataset": "Weather (13M objects, 103 features; large dataset of Table 2)", "protocol": COMMON,
   "metrics": [{"name": "rmse", "higher_is_better": False}], "defined_in": P.id},
])
print(len(results), "results,", len(claims), "claims,", len(relations), "relations")
