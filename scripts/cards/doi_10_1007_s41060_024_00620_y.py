"""Lukats et al. (Int. J. Data Sci. Anal. 2024/2025) のカード: 完全教師なしの概念ドリフト検出器のベンチマークとサーベイ。
Table 8 (INSECTS abrupt balanced での各検出器の最良 MTR 設定と MTFA/MTD/MDR) を読む。σ の有無が行ごとに違う。"""

import sys

sys.path.insert(0, "scripts/cards")
from _common import Paper, register, write_card  # noqa: E402

P = Paper("doi-10.1007_s41060-024-00620-y")
DETECTORS = ["BNDM", "CSDDM", "D3", "IBDD", "OCDD", "SPLL", "UDetect"]
METRICS = [("mtr", True), ("mtfa", True), ("mtd", False), ("mdr", False)]
BENCH = "lukats2024-insects-abrupt-balanced"

ls = P.lines(13)
k = ls.index("σ", ls.index("MDR")) + 1
results = []
for i, det in enumerate(DETECTORS):
    assert ls[k] == det, (ls[k], det)
    end = ls.index(DETECTORS[i + 1], k + 1) if i + 1 < len(DETECTORS) else ls.index("The absolute best performance is highlighted in bold face", k)
    toks = ls[k + 1:end]
    values = []  # (value, std or None)
    for t in toks:
        if t.startswith("±"):
            values[-1] = (values[-1][0], float(t[1:]))
        else:
            values.append((float(t), None))
    assert len(values) == 4, (det, toks)
    quote = " ".join(ls[k:end])
    for (metric, _), (v, sd) in zip(METRICS, values):
        r = {"id": f"r{len(results) + 1}", "benchmark": BENCH, "method": det, "metric": metric, "value": v}
        if sd is not None:
            r["std"] = sd
        r.update({"location": "Table 8", "page": 13, "quote": quote})
        results.append(r)
    k = end

claims = P.claims([
  ("Most drift detectors in the literature require immediately available true labels, which is unrealistic in many applications.", "Abstract",
   "Most algorithms proposed in the literature depend on the immediate availability of ground truth class labels."),
  ("Ten fully unsupervised detectors are analyzed (architecture, core ideas, assumptions about data).", "Abstract",
   "Ten algorithms are analyzed in terms of architectural choices, core ideas and assumptions about data"),
  ("Seven detectors are evaluated on eleven real-world data streams; three were too slow or depended on chance.", "Abstract",
   "Seven of these algorithms are evaluated with common concept drift detection metrics on eleven real-world data streams"),
  ("Depending on the target metric, D3, IBDD and SPLL are recommended.", "Abstract",
   "three concept drift detectors—Discriminative Drift Detector, Image-Based Drift Detector and Semi-Parametric Log-Likelihood—can be recommended depending on the desired target metric."),
  ("The evaluation metrics Mean Time Ratio and lift-per-drift have issues.", "Abstract",
   "This study further reveals issues with the evaluation metrics Mean Time Ratio and lift-per-drift."),
  ("Only one stream (INSECTS abrupt balanced) allows computing MTR, which needs ground-truth drift times.", "Section 6.2",
   "INSECTS (abrupt balanced) is the only data stream in this study which can be used to determine MTR."),
  ("In MTR, D3 outperformed the other detectors by a large margin.", "Section 6.2",
   "In these experiments, D3 outperforms other detectors by a large margin"),
  ("IBDD was among the worst in MTR despite having the most tested configurations.", "Section 6.2",
   "IBDD is among the worst performers, despite being the least filtered detector"),
  ("Classifier accuracy as a proxy metric is biased toward detectors that detect (and adapt) more often.", "Section 8",
   "classifier predictive performance is biased in favor of a higher number of detected concept drifts and adaptations."),
  ("The lift-per-drift metric is biased the other way, favoring fewer detections.", "Section 8",
   "lpdr=1 is likewise biased, as the version used in this study evidently favors fewer detected concept drifts."),
  ("IBDD gave strong classifier accuracy on many streams but did worse in lpd and MTR.", "Section 8",
   "Image-Based Drift Detector (IBDD) [46] achieves great classifier predictive performance on many data streams, although it does not perform as well when assessed with lpd and MTR."),
  ("D3 and SPLL gave the best results on most streams while also giving good classifier accuracy.", "Section 8",
   "Discriminative Drift Detector (D3) [45] and Semi-Parametric Log Likelihood (SPLL) [39] showed the best results on most data streams"),
  ("All configuration permutations were tried by grid search.", "Section 5.3",
   "A simple grid search is performed to test all permutations of the configuration parameters"),
  ("Several original publications describe no reset after a detection, so the authors added one where needed.", "Section 5.3",
   "several publications do not mention any reset mechanism to adapt to the new concept after the detection of a concept drift."),
  ("61 publications on unsupervised drift detection were examined.", "Section 8",
   "This study examined 61 publications related to unsupervised concept drift detection."),
  ("Configurations with no detection or periodic detection were filtered out before analysis.", "Section 6.1",
   "the experimental results were filtered to remove those results which featured no detection or periodic concept drift detection"),
  ("Real-world streams with known drift ground truth (which drifts, start and end) are hard to obtain.", "Section 5.1",
   "data with known concept drift ground truth information—which concept drifts are present, when do they begin and end—are difficult to obtain."),
])

write_card({
  "id": P.id,
  "title": "A benchmark and survey of fully unsupervised concept drift detectors on real-world data streams",
  "authors": ["Daniel Lukats", "Oliver Zielinski", "Axel Hahn", "Frederic Stahl"],
  "year": 2024,
  "venue": "International Journal of Data Science and Analytics",
  "links": {"doi": "https://doi.org/10.1007/s41060-024-00620-y", "code": "https://github.com/DFKI-NI/unsupervised-concept-drift-detection"},
  "source": {"version": "DLR elib repository copy (OpenAlex labels it acceptedVersion; the PDF has the journal layout)", "retrieved_at": "2026-10-02",
             "pdf_sha256": P.sha256(), "license": "CC BY-NC-ND 4.0",
             "pdf_url": "https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf"},
  "tags": {"tasks": ["concept-drift-detection"],
           "method_families": ["window-based-drift-detectors", "two-sample-tests"],
           "paradigms": ["streaming"]},
  "proposes": ["Benchmark of fully unsupervised concept drift detectors on real-world streams"],
  "claims": claims,
  "results": results,
  "relations": [],
  "card": {"created_at": "2026-10-02", "created_by": "claude-opus-5-5 via Claude Code", "reviewed": False,
           "notes": ("Table 8 extracted mechanically; values are each detector's BEST configuration (grid search) on the same stream, so they are optimistic. "
                     "Rows without σ in the table have no std recorded. Tables 10-14 (accuracy, lpd, synthetic verification) were not recorded. "
                     "The publisher PDF is behind a JavaScript bot check, so the open-access copy in the DLR repository was used. "
                     "'year' is the acceptance/publication year on the PDF (2024); Window Dilemma cites it as 2025 (journal issue).")},
})

register(P.id, [{"id": BENCH, "scope": "paper-private", "task": "concept-drift-detection",
                 "dataset": "INSECTS (abrupt balanced) stream (Souza et al.), the only stream in the study with drift ground truth for MTR",
                 "protocol": {"split": "Full stream, prequential with Hoeffding tree; detectors see only features (fully unsupervised) (Section 5).",
                              "preprocessing": "Detector-specific; reset mechanism added where the original description had none (Section 5.3).",
                              "tuning": "Grid search over configuration parameters; Table 8 reports each detector's best configuration (Section 5.3, Table 8).",
                              "repetitions": "Non-deterministic detectors averaged (Section 6)."},
                 "metrics": [{"name": "mtr", "higher_is_better": True, "definition": "Mean Time Ratio (Section 5.2)."},
                             {"name": "mtfa", "higher_is_better": True, "definition": "Mean Time between False Alarms."},
                             {"name": "mtd", "higher_is_better": False, "definition": "Mean Time to Detection."},
                             {"name": "mdr", "higher_is_better": False, "definition": "Missed Detection Rate."}],
                 "defined_in": P.id}])
print(len(results), "results,", len(claims), "claims")
