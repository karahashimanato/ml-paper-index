"""TAB: Unified Benchmarking of Time Series Anomaly Detection Methods (Qiu et al., PVLDB 2025) のカード。
主結果 (Table 6) は箱ひげ図のため relations に。Table 7 (重なりあり/なし窓の後処理別 AUC-ROC) を数値として読む。"""

import sys

sys.path.insert(0, "scripts/cards")
from _common import Paper, register, write_card  # noqa: E402

P = Paper("arxiv-2506.18046")
METHODS = ["ATrans", "DC", "DLin", "NLin", "Patch", "TsNet"]
DS = ["CalIt2", "Daphnet", "MSL", "PSM", "SKAB", "SMAP"]

ls = P.lines(P.page_of("Table 7: Average accuracy for 6 multivariate time series."))
page = P.page_of("Table 7: Average accuracy for 6 multivariate time series.")
k = ls.index("TsNet", ls.index("Table 7: Average accuracy for 6 multivariate time series.")) + 1
results = []
for ds in DS:
    assert ls[k] == ds, (ls[k], ds)
    k += 1
    for mode in ("Overlap", "Non-overlap"):
        assert ls[k] == mode, (ls[k], mode)
        vals = ls[k + 1:k + 7]
        quote = " ".join(ls[k:k + 7])
        for m, v in zip(METHODS, vals):
            results.append({"id": f"r{len(results) + 1}", "benchmark": f"tab2025-{ds.lower()}", "method": f"{m} ({mode.lower()} windows)",
                            "metric": "auc-roc", "value": float(v), "location": "Table 7", "page": page, "quote": quote})
        k += 7
assert len(results) == 6 * 6 * 2

claims = P.claims([
  ("TAB covers 29 public multivariate datasets and 1,635 univariate time series from different domains.", "Abstract",
   "TAB encompasses 29 public multivariate datasets and 1,635 univariate time series from different domains"),
  ("It covers non-learning, machine learning, deep learning, LLM-based and time-series pre-trained methods.", "Abstract",
   "TAB covers a variety of TSAD methods, including Non-learning, Machine learning, Deep learning, LLM-based, and Time-series pre-trained methods."),
  ("Among 100 surveyed studies, more than half use at most four multivariate datasets.", "Introduction",
   "more than half of the studies include at most four datasets, and only one study covers 17 datasets."),
  ("Inconsistent splitting: some methods take the validation set from the test set.", "Introduction",
   "Some methods use a validation set from the testing set"),
  ("Drop-last issue: discarding the last incomplete test batch makes comparisons unfair unless batch sizes match.", "Introduction",
   "discarding the last incomplete batch with fewer sample instances than the batch size is unfair"),
  ("With point adjustment, even random methods likely hit at least one point in long anomaly windows.", "Introduction",
   "even random methods have a good chance to predict at least one point in larger anomaly windows"),
  ("Threshold-independent metrics like AUC-ROC should not be recomputed after point adjustment.", "Introduction",
   "should not be recalculated after point adjustment."),
  ("Label-based metrics change considerably with the threshold.", "Introduction",
   "when the threshold changes, the performance can change considerably."),
  ("TAB computes metrics at all thresholds and reports the best.", "Experimental settings",
   "we conduct metric calculations at all thresholds and report the best results."),
  ("Each method is run with its original hyperparameters plus a search over several sets; the best result is reported.", "Experimental settings",
   "We then select the best results from these evaluations"),
  ("On univariate series, machine learning and non-learning methods had the best average V-PR and Aff-F1.", "Section 5.2.1",
   "Machine learning (ML) and non-learning (NL) methods exhibit the best average performance in terms of the V-PR and Aff-F metrics."),
  ("Classic methods should not be overlooked while pursuing novel ones.", "Section 5.2.1",
   "while pursuing novel methods, we should not overlook the classic methods."),
  ("On multivariate data some deep models (TsNet, CATCH) appear best in full-shot settings.", "Multivariate results",
   "Some deep learning models, such as TsNet and CATCH, appear to achieve the best performance in full-shot settings."),
  ("Strong non-learning/ML results on multivariate data suggest significant room for improving deep learning approaches.", "Multivariate results",
   "This suggests that there is still significant room for improvement in current deep learning approaches."),
  ("For multivariate data, pre-trained time-series models do much better with full-shot or few-shot than zero-shot.", "Multivariate results",
   "time series pre-trained models demonstrate significantly better performance compared to zero-shot learning approaches."),
  ("No single TSAD method is universally best for all time series and anomaly types.", "Introduction",
   "no single TSAD method is universally best for all time series and anomaly types."),
  ("Overlapping vs non-overlapping window post-processing usually does not change performance (with a few exceptions).", "Performance comparison of post-processing methods",
   "in most cases, the two post-processing methods do not affect the performance of the method"),
  ("In critical difference diagrams on univariate data, OCSVM, HOBS and DWT ranked best.", "Statistical validation",
   "with OCSVM, HOBS, and DWT achieving the excellent results."),
])

relations = [
  {"winner": "Machine learning and non-learning methods", "loser": "Deep learning, LLM-based and time-series pre-trained methods",
   "basis": "Average V-PR (VUS-PR) and Aff-F1 over 1,635 univariate series (Table 6, box plots).", "benchmark": "tab2025-univariate",
   "location": "Section 5.2.1",
   "page": P.page_of("Machine learning (ML) and non-learning (NL) methods exhibit the best average performance in terms of the V-PR and Aff-F metrics."),
   "quote": "Machine learning (ML) and non-learning (NL) methods exhibit the best average performance in terms of the V-PR and Aff-F metrics."},
]

write_card({
  "id": P.id,
  "title": "TAB: Unified Benchmarking of Time Series Anomaly Detection Methods",
  "authors": ["Xiangfei Qiu", "Zhe Li", "Wanghui Qiu", "Shiyan Hu", "Lekui Zhou", "Xingjian Wu", "Zhengyu Li", "Chenjuan Guo", "Aoying Zhou",
              "Zhenli Sheng", "Jilin Hu", "Christian S. Jensen", "Bin Yang"],
  "year": 2025,
  "venue": "PVLDB 18(9)",
  "links": {"arxiv": "https://arxiv.org/abs/2506.18046"},
  "source": {"version": "arXiv v2", "retrieved_at": "2026-10-02", "pdf_sha256": P.sha256(), "license": "CC BY-NC-ND 4.0"},
  "tags": {"tasks": ["time-series-anomaly-detection"],
           "method_families": ["classical-outlier-detectors", "reconstruction-based-detectors", "forecasting-based-detectors", "time-series-foundation-model"],
           "paradigms": ["unsupervised"]},
  "proposes": ["TAB benchmark (datasets, unified pipeline, leaderboard)"],
  "claims": claims,
  "results": results,
  "relations": relations,
  "card": {"created_at": "2026-10-02", "created_by": "claude-opus-5-5 via Claude Code", "reviewed": False,
           "notes": ("Main results (Table 6) are box plots; only the explicit univariate statement is recorded as a relation. "
                     "Table 7 (AUC-ROC with overlapping vs non-overlapping window post-processing, 6 methods x 6 multivariate datasets) extracted mechanically. "
                     "Best-threshold and best-hyperparameter reporting (c9, c10) makes all numbers optimistic. "
                     
                     "Section 5.2.1 is verified from the PDF heading; other locations are topic names.")},
})

COMMON = {"split": "TAB's unified split (validation from training data); non-overlapping test windows by default (experimental settings).",
          "preprocessing": "Unified pipeline; drop-last disabled (Introduction, experimental settings).",
          "tuning": "Original hyperparameters plus a search over several sets; best result reported; metrics computed at all thresholds and the best reported.",
          "repetitions": "Not stated in the main text."}
register(P.id, [{"id": f"tab2025-{d.lower()}", "scope": "public", "task": "time-series-anomaly-detection", "dataset": f"{d} (TAB multivariate)",
                 "protocol": COMMON, "metrics": [{"name": "auc-roc", "higher_is_better": True}], "defined_in": P.id} for d in DS] +
         [{"id": "tab2025-univariate", "scope": "public", "task": "time-series-anomaly-detection", "dataset": "TAB univariate collection (1,635 series)",
           "protocol": COMMON, "metrics": [{"name": "v-pr", "higher_is_better": True, "definition": "VUS-PR."},
                                           {"name": "aff-f1", "higher_is_better": True, "definition": "Affiliation F1."}], "defined_in": P.id}])
print(len(results), "results,", len(claims), "claims")
