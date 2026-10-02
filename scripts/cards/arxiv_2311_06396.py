"""Concept drift locality (Aguiar & Cano) のカード。Table 4 (ドリフトなし) と Table 5-9 (ドリフトあり、局所性カテゴリ別) を読む。"""

import sys

sys.path.insert(0, "scripts/cards")
from _common import Paper, register, write_card  # noqa: E402

P = Paper("arxiv-2311.06396")
DETECTORS = ["ADWIN", "DDM", "ECDD", "EDDM", "HDDM", "KSWIN", "PH", "RDDM", "STEPD"]
# (表番号, ページ, 表の見出しの先頭, 比較条件ID, 説明)
TABLES = [(5, 13, "Table 5:", "aguiar2023-all-drifts", "all evaluated drift difficulties"),
          (6, 13, "Table 6:", "aguiar2023-single-class-local", "single-class local drifts"),
          (7, 13, "Table 7:", "aguiar2023-single-class-global", "single-class global drifts"),
          (8, 14, "Table 8:", "aguiar2023-multi-class-local", "multi-class local drifts"),
          (9, 14, "Table 9:", "aguiar2023-multi-class-global", "multi-class global drifts")]
METRICS = [("precision-pct", True), ("recall-pct", True), ("f1-pct", True), ("delay", False)]


def rows(page, caption, n_vals):
    ls = P.lines(page)
    start = next(i for i, l in enumerate(ls) if l.startswith(caption))
    out, k = {}, start
    while len(out) < len(DETECTORS):
        k += 1
        if ls[k] in DETECTORS and ls[k] not in out:
            vals = ls[k + 1:k + 1 + n_vals]
            out[ls[k]] = (vals, " ".join(ls[k:k + 1 + n_vals]))
    return out


results = []
for num, page, cap, bench, _ in TABLES:
    for det, (vals, quote) in rows(page, cap, 4).items():
        for (metric, _), v in zip(METRICS, vals):
            results.append({"id": f"r{len(results) + 1}", "benchmark": bench, "method": det, "metric": metric,
                            "value": float(v.rstrip("%")), "location": f"Table {num}", "page": page, "quote": quote})
for det, (vals, quote) in rows(12, "Table 4:", 2).items():
    results.append({"id": f"r{len(results) + 1}", "benchmark": "aguiar2023-no-drift", "method": det, "metric": "false-positives",
                    "value": float(vals[1]), "location": "Table 4", "page": 12, "quote": quote})
assert len(results) == 5 * 9 * 4 + 9, len(results)

claims = P.claims([
  ("A locality/scale-based categorization of concept drift yields 2,760 benchmark problems.", "Abstract",
   "A systematic approach leads to a set of 2,760 benchmark problems"),
  ("Nine supervised drift detectors are compared across the difficulties.", "Abstract",
   "We conduct a comparative assessment of 9 state-of-the-art drift detectors across diverse difficulties"),
  ("ADWIN, DDM and PH were strong overall: few false alarms on stationary streams and good detection with drift.", "Section 5.1",
   "ADWIN, DDM, and PH stood out as strong performers in both evaluated scenarios."),
  ("ADWIN and PH consistently showed the best detection performance across all scenarios.", "Results",
   "ADWIN and PH consistently demonstrated superior detection performance across all evaluated scenarios."),
  ("EDDM had the lowest delay and second-highest recall but so many alarms that its precision was 0%.", "Section 5.1",
   "EDDM exhibited the lowest delay among all evaluated drift detectors and the second-highest recall, although this came at the cost of raising numerous drift alerts, leading to a precision of 0%."),
  ("Difficulty from easiest to hardest: multi-class global, single-class global, multi-class local, single-class local.", "Results",
   "a hierarchy of difficulty emerges, from easiest to hardest detection as follows: Multi-Class Global, Single-Class Global, Multi-Class Local, Single-Class Local."),
  ("More localized drifts produce more false alarms for all detectors.", "Results",
   "scenarios with more localized drifts tended to generate a higher number of false alarms."),
  ("Completely retraining the classifier after detection reduced accuracy in all evaluated scenarios.", "Results (classifier impact)",
   "completely retraining the classifier resulted in decreased accuracy across all evaluated scenarios."),
  ("A Hoeffding Tree is the monitored classifier; detectors monitor its binary error signal.", "Experimental setup",
   "we opted to use Hoeffding Tree (HT) [49] as our classifier."),
  ("Error-rate-based detectors often raise many false alarms, even on positive changes in the error rate.", "Lessons learned",
   "Drift detectors that rely on error rates often generate numerous false alarms."),
  ("On stationary streams, ADWIN and DDM raised the fewest false alarms.", "Section 5.1",
   "DDM and ADWIN displayed the lowest values of false alerts"),
  ("Experiments, stream generators and detectors were implemented in Python with the river library.", "Experimental setup",
   "All the experiments, generators and drift detectors were implemented using Python 3.8 and the river [50] package."),
])

write_card({
  "id": P.id,
  "title": "A comprehensive analysis of concept drift locality in data streams",
  "authors": ["Gabriel J. Aguiar", "Alberto Cano"],
  "year": 2023,
  "links": {"arxiv": "https://arxiv.org/abs/2311.06396", "code": "https://github.com/gabrieljaguiar/locality-concept-drift"},
  "source": {"version": "arXiv v2", "retrieved_at": "2026-10-02", "pdf_sha256": P.sha256()},
  "tags": {"tasks": ["concept-drift-detection"],
           "method_families": ["error-rate-drift-detectors", "window-based-drift-detectors"],
           "paradigms": ["streaming"]},
  "proposes": ["Locality-based categorization of concept drift", "Benchmark of 2,760 synthetic drifting streams"],
  "claims": claims,
  "results": results,
  "relations": [],
  "card": {"created_at": "2026-10-02", "created_by": "claude-opus-5-5 via Claude Code", "reviewed": False,
           "notes": ("Tables 4-9 extracted mechanically. Precision/recall/F1 are percentages; delay is in instances. "
                     "Detector hyperparameter settings were not checked in the text. "
                     "Streams are synthetic (generated); each stream has a single known drift. Page 24 repeats one paragraph verbatim (editorial duplication in the paper).")},
})

COMMON = {"split": "Synthetic streams with one known drift point each; prequential evaluation with a Hoeffding Tree (Section 4).",
          "preprocessing": "Detectors monitor the binary error signal of the Hoeffding Tree (Section 4).",
          "tuning": "Not described as tuned per stream (implementation: river).",
          "repetitions": "Averaged over all benchmark streams in the respective category (Tables 4-9)."}
metrics = [{"name": m, "higher_is_better": hib} for m, hib in METRICS]
register(P.id, [{"id": b, "scope": "public", "task": "concept-drift-detection",
                 "dataset": f"Aguiar & Cano locality benchmark streams: {desc}", "protocol": COMMON, "metrics": metrics, "defined_in": P.id}
                for _, _, _, b, desc in TABLES] +
         [{"id": "aguiar2023-no-drift", "scope": "public", "task": "concept-drift-detection",
           "dataset": "Aguiar & Cano locality benchmark streams without drift", "protocol": COMMON,
           "metrics": [{"name": "false-positives", "higher_is_better": False, "definition": "Average number of alarms on streams without drift (Table 4)."}],
           "defined_in": P.id}])
print(len(results), "results,", len(claims), "claims")
