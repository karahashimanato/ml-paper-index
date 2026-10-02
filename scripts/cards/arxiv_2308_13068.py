"""Multivariate Time Series Anomaly Detection: Fancy Algorithms and Flawed Evaluation Methodology (Sehili & Zhang) のカード。
Table 1: AnomalyTransformer / NCAD / GDN / PCA の point-wise F1・composite F1C・event-wise F1E (SWaT, Wadi, PSM)。"""

import re
import sys

sys.path.insert(0, "scripts/cards")
from _common import Paper, register, write_card  # noqa: E402

P = Paper("arxiv-2308.13068")
DS = ["swat", "wadi", "psm"]
METHODS = {"AT": "AnomalyTransformer", "NCAD": "NCAD", "GDN": "GDN", "PCA": "PCA (with scaling, clipping, score smoothing)"}
METRICS = ["f1-pointwise", "f1-composite", "f1-event"]

t = P.text(13)
results = []
for short, name in METHODS.items():
    g = re.search(re.escape(short) + r" ((?:[0-9.]+ [0-9.]+ [0-9.]+ [0-9]+/[0-9]+ ?){3})", t)
    assert g, short
    quote = g.group(0).strip()
    blocks = re.findall(r"([0-9.]+) ([0-9.]+) ([0-9.]+) ([0-9]+)/([0-9]+)", g.group(1))
    assert len(blocks) == 3, (short, blocks)
    for ds, b in zip(DS, blocks):
        for metric, v in zip(METRICS, b[:3]):
            results.append({"id": f"r{len(results) + 1}", "benchmark": f"sehili2023-{ds}", "method": name, "metric": metric,
                            "value": float(v), "location": "Table 1", "page": 13, "quote": quote})
assert len(results) == 4 * 3 * 3

claims = P.claims([
  ("Most MVTS anomaly detection methods are evaluated with inappropriate or highly flawed protocols.", "Abstract",
   "most proposed solutions are evaluated using either inappropriate or highly flawed protocols, with an apparent lack of scientific foundation."),
  ("Under the point-adjust protocol a random guess can systematically outperform all algorithms developed so far.", "Abstract",
   "So flawed is one very popular protocol, the so-called point-adjust protocol, that a random guess can be shown to systematically outperform all algorithms developed so far."),
  ("A simple PCA baseline outperforms many recent deep learning approaches on popular benchmarks.", "Abstract",
   "we propose a simple, yet challenging, baseline based on Principal Components Analysis (PCA) that surprisingly outperforms many recent Deep Learning (DL) based approaches on popular benchmark datasets."),
  ("Algorithms developed with point-adjust as the sole target fail to beat a random guess under other protocols (AnomalyTransformer, NCAD).", "Section 5",
   "Algorithms that were developed using point-adjust as the sole target fail to reach any score better than a random guess when evaluated with other"),
  ("Untrained versions of these models reached essentially the same high point-adjust scores.", "Section 5",
   "we also achieved essentially the same high scores using untrained versions of these models."),
  ("GDN, developed with the point-wise protocol, was more resilient under other protocols.", "Section 5",
   "GDN, however, which was developed based on the more realistic point-wise protocol, shows more resilience when evaluated with other protocols."),
  ("On datasets with very high contamination such as PSM, point-wise F1 can be misleading.", "Section 5",
   "Datasets that have a very high contamination rate, such as PSM, yield point-wise F1 scores that can be misleading."),
  ("All Table 1 metrics use the threshold that gives the best point-wise F1.", "Table 1 caption",
   "All metrics are computed based on the detection threshold that yields the best point-wise performance."),
  ("At its best point-adjust threshold, AnomalyTransformer raises an alarm about every 110 seconds on SWaT - barely useful in deployment.", "Section 5",
   "On average, it raises an alarm every 110 seconds, making it, in our opinion, barely useful for deployment."),
  ("The PCA pipeline uses simple pre- and post-processing (scaling, clipping, score smoothing) that significantly improves its score.", "Section 5",
   "we use simple pre-processing and post-processing blocks (input scaling, clipping and score smoothing) that significantly improve the score."),
  ("The point-wise protocol is not appropriate for all datasets and use cases; an event-wise protocol is proposed.", "Introduction",
   "We also review the more objective point-wise protocol and show that it is not appropriate for all kinds of datasets and use-cases."),
  ("Many works were developed without a simple but sufficiently challenging baseline.", "Section 5",
   "many works have been developed without establishing a simple but enough challenging baseline."),
  ("The authors urge more effort on data, experiment design and evaluation instead of increasingly complex algorithms.", "Abstract",
   "instead of putting the highest weight on the design of increasingly more complex"),
])

write_card({
  "id": P.id,
  "title": "Multivariate Time Series Anomaly Detection: Fancy Algorithms and Flawed Evaluation Methodology",
  "authors": ["Mohamed El Amine Sehili", "Zonghua Zhang"],
  "year": 2023,
  "links": {"arxiv": "https://arxiv.org/abs/2308.13068", "code": "https://github.com/amsehili/MVTSEvalPaper"},
  "source": {"version": "arXiv v2", "retrieved_at": "2026-10-02", "pdf_sha256": P.sha256()},
  "tags": {"tasks": ["time-series-anomaly-detection"],
           "method_families": ["classical-outlier-detectors", "reconstruction-based-detectors", "forecasting-based-detectors", "tabular-attention"],
           "paradigms": ["unsupervised"]},
  "proposes": ["Event-wise evaluation protocol", "PCA baseline with simple pre/post-processing"],
  "claims": claims,
  "results": results,
  "relations": [],
  "card": {"created_at": "2026-10-02", "created_by": "claude-opus-5-5 via Claude Code", "reviewed": False,
           "notes": ("Table 1 extracted mechanically (TPE/FPE event counts not recorded). Thresholds maximize point-wise F1 for every method (c8). "
                     "The 'tabular-attention' tag is used for AnomalyTransformer as the closest existing attention-based family tag. No venue is stated in the PDF.")},
})

COMMON = {"split": "Benchmark train/test splits; SWaT labels from attack start/end (Section 5).",
          "preprocessing": "Method-specific; PCA with input scaling, clipping and score smoothing (Section 5).",
          "tuning": "Official implementations; threshold chosen to maximize point-wise F1 (Table 1 caption).",
          "repetitions": "Not stated."}
register(P.id, [{"id": f"sehili2023-{d}", "scope": "paper-private", "task": "time-series-anomaly-detection", "dataset": {"swat": "SWaT", "wadi": "WADI (2017)", "psm": "PSM"}[d],
                 "protocol": COMMON,
                 "metrics": [{"name": "f1-pointwise", "higher_is_better": True}, {"name": "f1-composite", "higher_is_better": True},
                             {"name": "f1-event", "higher_is_better": True, "definition": "Event-wise F1 including a false alarm rate term (Section 3)."}],
                 "defined_in": P.id} for d in DS])
print(len(results), "results,", len(claims), "claims")
