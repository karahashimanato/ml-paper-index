"""The Window Dilemma (Gower-Winter et al., 2026) のカード。Table 1: 手法 x 11 ストリームの平均精度 (小数点はカンマ) と MedRank、
Table 2: AMF/ARF をバッチの更新方式にそろえた場合の精度を読む。"""

import re
import sys

sys.path.insert(0, "scripts/cards")
from _common import Paper, register, write_card  # noqa: E402

P = Paper("arxiv-2602.06456")
DS = ["EL", "FC", "IA", "II", "KS", "LX", "MR", "NW", "OZ", "RT", "YG"]
NAMES = {"EL": "Electricity", "FC": "Forest Covertype", "IA": "Insects-Abrupt (balanced)", "II": "Insects-Incremental (balanced)",
         "KS": "Keystroke", "LX": "Luxembourg", "MR": "MIRS", "NW": "NOAA Weather", "OZ": "Ozone", "RT": "Rialto", "YG": "Yoga"}
T1 = ["LC", "MC", "NB", "DDM-NB", "ADWIN-NB", "R-NB", "D3-LR-NB", "D3-HT-NB", "IBDD-NB", "HT", "DDM-HT", "ADWIN-HT", "R-HT",
      "D3-LR-HT", "D3-HT-HT", "IBDD-HT", "HAT", "AMF", "ARF", "S-RF", "R-RF", "I-RF"]
NUM = re.compile(r"^[0-9]+[,.][0-9]$")


def num(s: str) -> float:
    return float(s.replace(",", "."))


ls = P.lines(6)
results = []
k = ls.index("MedRank") + 1
for m in T1:
    k = ls.index(m, k)
    vals = ls[k + 1:k + 12]
    rank = ls[k + 12]
    assert all(NUM.match(v) for v in vals) and rank.isdigit(), (m, vals, rank)
    quote = " ".join(ls[k:k + 13])
    for ds, v in zip(DS, vals):
        results.append({"id": f"r{len(results) + 1}", "benchmark": f"gowerwinter2026-{ds.lower()}", "method": m, "metric": "mean-prequential-accuracy",
                        "value": num(v), "location": "Table 1", "page": 6, "quote": quote})
    results.append({"id": f"r{len(results) + 1}", "benchmark": "gowerwinter2026-11-streams", "method": m, "metric": "median-rank",
                    "value": float(rank), "location": "Table 1", "page": 6, "quote": quote})
    k += 13
# Table 2: AMF / ARF をバッチ RF と同じ更新方式(N 件ごとに更新)にした場合
k = ls.index("YG", ls.index("Table 1: The Average Accuracy for each technique across all benchmark data steams investigated in this work. Bold")) + 1
for m in ("AMF", "ARF"):
    k = ls.index(m, k)
    vals = ls[k + 1:k + 12]
    assert all(NUM.match(v) for v in vals), (m, vals)
    quote = " ".join(ls[k:k + 12])
    for ds, v in zip(DS, vals):
        results.append({"id": f"r{len(results) + 1}", "benchmark": f"gowerwinter2026-{ds.lower()}", "method": f"{m} (batch update regime)",
                        "metric": "mean-prequential-accuracy", "value": num(v), "location": "Table 2", "page": 6, "quote": quote})
    k += 12
assert len(results) == len(T1) * 12 + 2 * 11, len(results)

claims = P.claims([
  ("Traditional batch learning often performed better than drift-aware stream learners.", "Abstract",
   "is that traditional batch learning techniques often perform better than their drift-aware counterparts"),
  ("The Window Dilemma: perceived drift is a product of how instances are windowed, not necessarily of the data-generating process.", "Abstract",
   "perceived drift is a product of windowing and not necessarily the underlying data generating process."),
  ("Drift detection is ill-posed mainly because drift events can rarely be verified in practice.", "Abstract",
   "drift detection is ill-posed, primarily because verification of drift events are implausible in practice."),
  ("Better performance of a classifier with a drift detector does not prove that drift was detected (affirming the consequent).", "Section 4",
   "Performance improvement is neither necessary nor sufficient evidence of successful drift detection"),
  ("Detectors that alarm more frequently tend to perform better (up to a point), likely because they retrain more often on recent data.", "Section 4",
   "concept drift detectors that detect more frequently, tend to perform better (up to a point)."),
  ("The type of classifier often matters more than drift-awareness.", "Introduction",
   "indicates that the type of classifier is often more important than drift-awareness."),
  ("Among drift detectors, D3 with a Hoeffding Tree discriminator was best for both base models (consistent with Lukats et al.).", "Section 5",
   "Of the drift detectors, D3-HT performed the best for both the NB and HT base models."),
  ("The drift-unaware Aggregated Mondrian Forest was competitive with the drift-aware Adaptive Random Forest.", "Section 5",
   "the drift-unaware Aggregated Mondrian Forest (AMF) performed competitively with the drift-aware Adaptive Random Forest (ARF)."),
  ("Keeping past data and periodically retraining on growing training sets is often effective.", "Section 5",
   "our results suggest that keeping past data is often useful and periodically retraining a model on increasingly large training sets is often an effective strategy."),
  ("Under the same update regime as batch random forests, drift-aware stream learners are often inferior to simple batch learning with a suitable classifier.", "Section 5",
   "drift-aware stream learners are often inferior to simple batch learning procedures provided an appropriate classifier is chosen."),
  ("The authors do not claim drift detection is pointless, but that its current purpose is misplaced.", "Conclusion",
   "Our findings do not mean that drift detection is pointless, rather that its current purpose is misplaced."),
  ("No per-stream tuning: default parameters of each library/implementation are used.", "Appendix A",
   "We do not perform explicit parameter tuning for model on each data stream and instead use the default values"),
  ("Evaluation uses 11 binary and multiclass real-world streams (no purely synthetic data).", "Section 5",
   "we evaluate each model across 11 binary and multiclass data streams"),
  ("The Last Class baseline wins on Forest Covertype by exploiting autocorrelation.", "Section 5 footnote",
   "The Last Class classifier performed best on ForestCoverType because it abuses the known autocorrelation in the data stream."),
  ("Accuracy can be misleading for drifting streams (Cohen's kappa is reported in the appendix).", "Section 5",
   "We acknowledge that accuracy is a potentially misleading metric in Drift Research"),
  ("Reset intervals of the periodic-reset models use domain knowledge for some datasets (e.g. one month, one season).", "Appendix",
   "For resetting, some datasets possess domain knowledge that we could exploit."),
])

relations = [
  {"winner": "AMF, ARF, R-RF, I-RF (forest-based learners)", "loser": "Naive Bayes and Hoeffding Tree variants with or without drift detectors",
   "basis": "Median rank over the 11 streams (Table 1); 'Adaptive Forest (tree-ensemble) techniques outperformed the single learner NB and HT variants'.",
   "benchmark": "gowerwinter2026-11-streams", "location": "Section 5",
   "page": P.page_of("Adaptive Forest (tree-ensemble) techniques outperformed the single learner NB and HT variants."),
   "quote": "Adaptive Forest (tree-ensemble) techniques outperformed the single learner NB and HT variants."},
]

write_card({
  "id": P.id,
  "title": "The Window Dilemma: Why Concept Drift Detection is Ill-Posed",
  "authors": ["Brandon Gower-Winter", "Misja Groen", "Georg Krempl"],
  "year": 2026,
  "links": {"arxiv": "https://arxiv.org/abs/2602.06456", "code": "https://github.com/BrandonGower-Winter/TheWindowDilemma"},
  "source": {"version": "arXiv v1", "retrieved_at": "2026-10-02", "pdf_sha256": P.sha256()},
  "tags": {"tasks": ["concept-drift-detection"],
           "method_families": ["error-rate-drift-detectors", "window-based-drift-detectors", "random-forests"],
           "paradigms": ["streaming"]},
  "proposes": ["The Window Dilemma (argument that drift detection is ill-posed)"],
  "claims": claims,
  "results": results,
  "relations": relations,
  "card": {"created_at": "2026-10-02", "created_by": "claude-opus-5-5 via Claude Code", "reviewed": False,
           "notes": ("Table 1 and Table 2 extracted mechanically. The paper uses a decimal comma (84,8 = 84.8); one cell in Table 2 uses a dot (63.3). "
                     "Accuracy values are percentages. Table 2 re-runs AMF/ARF with the batch update regime ('(batch update regime)' in method names); "
                     "its R-RF/I-RF rows duplicate Table 1 and were not re-recorded. Section numbers were inferred from the paper's own cross-references "
                     "(Sections 3, 4, 5).")},
})

COMMON = {"split": "Prequential (test-then-train) evaluation over the full real-world stream (Section 5).",
          "preprocessing": "Default parameters; periodic reset/retrain intervals per dataset, partly from domain knowledge (Appendix).",
          "tuning": "No per-stream tuning; library defaults (Appendix A).",
          "repetitions": "Mean prequential accuracy over the stream with fixed seeds (Section 5)."}
reg = [{"id": f"gowerwinter2026-{d.lower()}", "scope": "paper-private", "task": "concept-drift-detection",
        "dataset": f"{NAMES[d]} stream (USP Data Stream Repository) under the paper's protocol", "protocol": COMMON,
        "metrics": [{"name": "mean-prequential-accuracy", "higher_is_better": True, "definition": "Mean prequential accuracy in percent (Table 1)."}],
        "defined_in": P.id} for d in DS]
reg.append({"id": "gowerwinter2026-11-streams", "scope": "paper-private", "task": "concept-drift-detection",
            "dataset": "11 real-world streams of the paper (aggregate)", "protocol": COMMON,
            "metrics": [{"name": "median-rank", "higher_is_better": False, "definition": "Median rank across the 11 streams (Table 1, MedRank)."}],
            "defined_in": P.id})
register(P.id, reg)
print(len(results), "results,", len(claims), "claims")
