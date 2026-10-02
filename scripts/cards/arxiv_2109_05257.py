"""Towards a Rigorous Evaluation of Time-series Anomaly Detection (Kim et al., AAAI 2022) のカード。
Table 2: 手法 x データセットの F1PA と F1(† = 著者による再現値、それ以外は原論文の報告値)。"""

import re
import sys

sys.path.insert(0, "scripts/cards")
from _common import Paper, register, write_card  # noqa: E402

P = Paper("arxiv-2109.05257")
DS = ["SWaT", "WADI", "MSL", "SMAP", "SMD"]
ROWS = ["USAD", "DAGMM", "LSTM-VAE", "OmniAnomaly", "MSCRED", "THOC", "GDN", "Case 1", "Case 2", "Case 3"]
CASES = {"Case 1": "Case 1: random anomaly score", "Case 2": "Case 2: input itself as anomaly score",
         "Case 3": "Case 3: untrained (randomly initialized) LSTM encoder-decoder"}
CELL = re.compile(r"^([0-9]\.[0-9]+)(†)?\s*(?:\((?:↑|↓)\))?$")

ls = P.lines(6)
k = ls.index("USAD")
results = []
for row in ROWS:
    assert ls[k] == row, (ls[k], row)
    cells = ls[k + 1:k + 11]
    quote = " ".join(ls[k:k + 11])
    for j, cell in enumerate(cells):
        g = CELL.match(cell)
        assert g, (row, cell)
        ds, metric = DS[j // 2], ("f1-pa" if j % 2 == 0 else "f1")
        r = {"id": f"r{len(results) + 1}", "benchmark": f"kim2022-{ds.lower()}", "method": CASES.get(row, row), "metric": metric,
             "value": float(g.group(1))}
        if row not in CASES:
            r["note"] = "Reproduced by the authors (†)." if g.group(2) else "Value reported in the original paper (best number)."
        r.update({"location": "Table 2", "page": 6, "quote": quote})
        results.append(r)
    k += 11
assert len(results) == 100

claims = P.claims([
  ("Point adjustment (PA) can greatly overestimate detection performance: even a random anomaly score can look state of the art.", "Abstract",
   "the PA protocol has a great possibility of overestimating the detection performance; that is, even a random anomaly score can easily turn into a state-of-the-art TAD method."),
  ("Even without PA, an untrained model performs comparably to existing methods.", "Abstract",
   "an untrained model obtains comparable detection performance to the existing methods even when PA is forbidden."),
  ("PA: if any point in a ground-truth anomaly segment is detected, the whole segment counts as detected.", "Introduction",
   "if at least one moment in a contiguous anomaly segment is detected as an anomaly, the entire segment is then considered to be correctly predicted as anomaly."),
  ("PA can only increase precision, recall and F1.", "Section 3",
   "after the PA, the P, R and consequently F1 score can only increase."),
  ("With random scores, F1PA can be pushed close to 1 by choosing the threshold, unless anomaly segments are short.", "Section 3",
   "except for the case when the length of the anomaly segment is short."),
  ("The overestimation by PA depends on the test set and is weaker with shorter anomaly segments (e.g. SMD).", "Section 5",
   "the overestimation effect of PA depends on the test dataset distribution, and its effect becomes less conspicuous with shorter anomaly segments."),
  ("Only GDN consistently exceeded the untrained baselines on all datasets.", "Section 5",
   "Only the GDN consistently exceeded the baselines for all datasets."),
  ("Without PA, existing methods were mostly worse than the untrained baselines (Case 2 and 3).", "Section 5",
   "mostly inferior to Case 2 and 3, implying that the currently proposed methods may have obtained marginal or even no advancement against the baselines."),
  ("All thresholds were chosen to give the best score (optimistic for every method).", "Section 5",
   "All thresholds were obtained from those that yielded the best score."),
  ("Existing methods' numbers are the best reported in the original papers or official reproductions; missing ones were reproduced (†).", "Section 5",
   "For the existing methods, we used the best numbers reported in the original papers and officially reproduced results"),
  ("MSL and SMAP contain unlabeled anomalies in the training data.", "Section 5",
   "Unlike other datasets, unlabeled anomalies are contained in the training data, which makes training difficult."),
  ("Proposed PA%K protocol: apply PA only if the fraction of detected points in a segment exceeds K, mitigating both over- and underestimation.", "Section 4",
   "which can mitigate the overestimation effect of F1PA and the possibility of underestimation of F1."),
  ("Proposed baseline: the F1 of a randomly initialized simple reconstruction model (e.g. untrained single-layer LSTM autoencoder).", "Section 4",
   "we suggest establishing a new baseline with the F1 measured from the prediction of a randomly initialized reconstruction model with simple architecture"),
  ("Existing TAD methods set thresholds after looking at the test set or use the F1-optimal threshold.", "Discussion (directions for evaluation)",
   "existing TAD methods set the threshold after investigating the test dataset or simply use the optimal threshold that yields the best F1."),
  ("Threshold-independent metrics such as AUROC or AUPR are recommended in addition.", "Discussion (directions for evaluation)",
   "Additional metrics with the reduced dependency such as AUROC or area under precision-recall (AUPR) curve will help in rigorous evaluation."),
  ("Incomplete test labeling: some labeled anomalies look like normal data.", "Section 4",
   "due to the incomplete test set labeling, some signals labeled as anomalies share more statistics with normal signals."),
  ("Reported F1PA and F1 are not reliably correlated on SWaT and WADI.", "Section 5",
   "these numbers are insufficient to assure the existence of correlation"),
  ("Point anomalies are the dominant anomaly type in current TAD datasets.", "Background",
   "Point anomaly is the most dominant type in the current TAD datasets."),
])

write_card({
  "id": P.id,
  "title": "Towards a Rigorous Evaluation of Time-series Anomaly Detection",
  "authors": ["Siwon Kim", "Kukjin Choi", "Hyun-Soo Choi", "Byunghan Lee", "Sungroh Yoon"],
  "year": 2022,
  "venue": "AAAI 2022",
  "links": {"arxiv": "https://arxiv.org/abs/2109.05257"},
  "source": {"version": "arXiv v2", "retrieved_at": "2026-10-02", "pdf_sha256": P.sha256()},
  "tags": {"tasks": ["time-series-anomaly-detection"],
           "method_families": ["reconstruction-based-detectors", "forecasting-based-detectors"],
           "paradigms": ["unsupervised"]},
  "proposes": ["PA%K evaluation protocol", "Untrained-model baseline for TAD"],
  "claims": claims,
  "results": results,
  "relations": [],
  "card": {"created_at": "2026-10-02", "created_by": "claude-opus-5-5 via Claude Code", "reviewed": False,
           "notes": ("Table 2 extracted mechanically. Existing methods mix values reported in the original papers and values reproduced by the authors (see each result's note); "
                     "thresholds are best-score thresholds for all methods. Cases 1 and 3 are averages over five seeds; Case 2/3 window size 120. "
                     "Section numbers follow the paper's own references (Sections 3-5).")},
})

COMMON = {"split": "Standard train/test split of each benchmark; no preprocessing such as early time step removal or downsampling (Section 5).",
          "preprocessing": "Normalization and sliding windows (stride 1) (Section 3.1).",
          "tuning": "Best numbers from original papers or reproduction with hyperparameters searched in the suggested ranges; best-score thresholds (Section 5).",
          "repetitions": "Cases 1 and 3 averaged over five seeds (Section 5)."}
register(P.id, [{"id": f"kim2022-{d.lower()}", "scope": "paper-private", "task": "time-series-anomaly-detection",
                 "dataset": d, "protocol": COMMON,
                 "metrics": [{"name": "f1-pa", "higher_is_better": True, "definition": "F1 after point adjustment."},
                             {"name": "f1", "higher_is_better": True, "definition": "Point-wise F1 without point adjustment."}],
                 "defined_in": P.id} for d in DS])
print(len(results), "results,", len(claims), "claims")
