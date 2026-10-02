"""One or Two Things We know about Concept Drift (Hinder, Vaquet, Hammer 2023) のカード。教師なしの監視向けサーベイ。results は無い。"""

import sys

sys.path.insert(0, "scripts/cards")
from _common import Paper, write_card  # noqa: E402

P = Paper("arxiv-2310.15826")

claims = P.claims([
  ("Most surveys cover supervised streams; this survey reviews drift in unsupervised data streams, relevant for monitoring and anomaly detection.", "Abstract",
   "While many surveys focus on supervised data streams, so far, there is no work reviewing the unsupervised setting."),
  ("It provides a taxonomy of drift detection and a systematic review of drift localization.", "Abstract",
   "This survey provides a taxonomy of existing work on drift detection."),
  ("It includes standardized experiments on parametric artificial datasets to compare detection and localization strategies directly.", "Abstract",
   "contains standardized experiments on parametric artificial datasets allowing for a direct comparison of different strategies for detection and localization."),
  ("Guideline: incorporate as much domain knowledge as possible (preprocessing, features, descriptors).", "Conclusion and Guidelines for Drift Detection",
   "A main finding is that as much domain knowledge as possible should be incorporated when designing drift detection schemes."),
  ("Meta or block-based detection methods are advisable overall; choosing good split points is crucial.", "Conclusion and Guidelines for Drift Detection",
   "Over all experiments, we found that it is advisable to use meta or block-based methods."),
  ("Feature-wise analysis only if the drift is not expected to show up in correlations; otherwise ensemble-based techniques are better.", "Conclusion and Guidelines for Drift Detection",
   "A feature-wise analysis should only be performed if it is expected that the drift does not inflict itself in correlations."),
  ("For high-dimensional data avoid dimension-wise methods, especially when false alarms are costly.", "Conclusion and Guidelines for Drift Detection",
   "When working with high dimensional data, one should avoid using dimension-wise methodologies, especially if false alarms are costly in the considered application."),
  ("Loss-based strategies should be avoided when the goal is monitoring for anomalous behavior.", "Conclusion and Guidelines for Drift Detection",
   "loss-based strategies should be avoided when the target of the drift detection is monitoring for anomalous behavior."),
  ("Detecting the time of a drift is not sufficient for monitoring; one must also localize where it happens.", "Drift Localization and Segmentation",
   "Solely detecting and determining the time point of the drift is not sufficient in many monitoring settings."),
  ("More research is needed especially on drift localization and explanation.", "Conclusion",
   "Finally, we found that more research is required, in particular focusing on the localization and explanation tasks."),
])

write_card({
  "id": P.id,
  "title": "One or Two Things We know about Concept Drift -- A Survey on Monitoring Evolving Environments",
  "authors": ["Fabian Hinder", "Valerie Vaquet", "Barbara Hammer"],
  "year": 2023,
  "links": {"arxiv": "https://arxiv.org/abs/2310.15826"},
  "source": {"version": "arXiv v1", "retrieved_at": "2026-10-02", "pdf_sha256": P.sha256()},
  "tags": {"tasks": ["concept-drift-detection"],
           "method_families": ["window-based-drift-detectors", "two-sample-tests"],
           "paradigms": ["streaming"]},
  "proposes": ["Taxonomy of unsupervised drift detection and localization", "Guidelines for choosing detection strategies"],
  "claims": claims,
  "results": [],
  "relations": [],
  "card": {"created_at": "2026-10-02", "created_by": "claude-opus-5-5 via Claude Code", "reviewed": False,
           "notes": "Survey; its experiments use parametric artificial datasets and are reported as figures, so no results were recorded. Section numbers are not used (headings only)."},
})
print(len(claims), "claims")
