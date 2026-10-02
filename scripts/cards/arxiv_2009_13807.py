"""Current Time Series Anomaly Detection Benchmarks are Flawed (Wu & Keogh) のカード。ベンチマーク批判のため results は無い。"""

import sys

sys.path.insert(0, "scripts/cards")
from _common import Paper, write_card  # noqa: E402

P = Paper("arxiv-2009.13807")

claims = P.claims([
  ("Most exemplars of popular TSAD benchmarks (Yahoo, Numenta, NASA, ...) have one or more of four flaws: triviality, unrealistic anomaly density, mislabeled ground truth, run-to-failure bias.", "Introduction",
   "These flaws are triviality, unrealistic anomaly density, mislabeled ground truth and run-to-failure bias."),
  ("Because of these flaws, most published comparisons of anomaly detectors may be unreliable and apparent progress may be illusory.", "Introduction",
   "we believe that most published comparisons of anomaly detection algorithms may be unreliable"),
  ("Triviality: 316 of the 367 Yahoo time series can be solved by a 'one-liner' (a single line of basic code).", "Flaw: triviality",
   "316 out of 367 (86.1%) can be easily solved with a one-liner"),
  ("Ideally each test time series should contain exactly one anomaly, communicated with the dataset.", "Flaw: unrealistic anomaly density",
   "We believe that the ideal number of anomalies in a single testing time series is exactly one."),
  ("All benchmark datasets appear to contain mislabeled data (false positives and false negatives).", "Flaw: mislabeled ground truth",
   "All of the benchmark datasets appear to have mislabeled data, both false positives and false negatives."),
  ("Run-to-failure bias: anomalies cluster near the end, so naively flagging the last point scores well.", "Flaw: run-to-failure bias",
   "A naïve algorithm that simply labels the last point as an anomaly"),
  ("The classic TSAD archives are irretrievably flawed.", "Summary of the flaws",
   "the classic time series anomaly detection archives are irretrievably flawed."),
  ("On these datasets no level of reported performance can demonstrate an algorithm's utility.", "Summary of the flaws",
   "Thus, there is simply no level of performance that would suggest the utility of a"),
  ("The paper introduces the UCR Time Series Anomaly Archive as a benchmark for meaningful comparisons.", "Abstract",
   "with this paper we introduce the UCR Time Series Anomaly Archive."),
  ("Some researchers seem to rarely look at the time series and only at F1 scores; the flaws are visible by plotting.", "Recommendations",
   "We suspect that some researchers rarely view the time series, they simply pass objects to a black box and look at the F1 scores"),
  ("Scoring without tolerance can systematically penalize an algorithm that places its anomaly peak at a different position in the subsequence.", "Recommendations",
   "we run the risk of a systemic bias against an algorithm that simply formats its output differently to its rival."),
  ("Many recent papers presuppose that deep learning is the answer to anomaly detection.", "Recommendations",
   "Many recent papers seem to pose their research question as"),
])

write_card({
  "id": P.id,
  "title": "Current Time Series Anomaly Detection Benchmarks are Flawed and are Creating the Illusion of Progress",
  "authors": ["Renjie Wu", "Eamonn J. Keogh"],
  "year": 2020,
  "links": {"arxiv": "https://arxiv.org/abs/2009.13807"},
  "source": {"version": "arXiv v5", "retrieved_at": "2026-10-02", "pdf_sha256": P.sha256()},
  "tags": {"tasks": ["time-series-anomaly-detection"],
           "method_families": ["classical-outlier-detectors", "deep-learning"],
           "paradigms": ["unsupervised"]},
  "proposes": ["UCR Time Series Anomaly Archive"],
  "claims": claims,
  "results": [],
  "relations": [],
  "card": {"created_at": "2026-10-02", "created_by": "claude-opus-5-5 via Claude Code", "reviewed": False,
           "notes": ("Critique of benchmark datasets; no method comparison table recorded. The PDF does not state a venue; 'year' is the arXiv posting year. "
                     "Locations are given by topic, not section number.")},
})
print(len(claims), "claims")
