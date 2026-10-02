"""Deep Learning for Time Series Anomaly Detection: A Survey (Darban et al.) のカード。サーベイのため results は無い。"""

import sys

sys.path.insert(0, "scripts/cards")
from _common import Paper, write_card  # noqa: E402

P = Paper("arxiv-2211.05244")

claims = P.claims([
  ("Deep TSAD models are classified into four categories: forecasting-based, reconstruction-based, representation-based and hybrid.", "Introduction (contributions)",
   "These models are broadly classified into four categories: forecasting-based, reconstruction-based, representation-based and hybrid methods."),
  ("64 recent deep models are discussed and categorized.", "Discussion and conclusion",
   "64 recent deep models were comprehensively discussed and categorised."),
  ("Real-world time series are non-stationary, so deep models need online or incremental training.", "Discussion and conclusion",
   "This non-stationary nature necessitates the adaptation of deep learning models through online or incremental training approaches"),
  ("Without labeled anomalies, many normal instances are flagged; reducing false positives is a key challenge.", "Discussion and conclusion",
   "one of the key challenges is to find a mechanism for minimising false positives and improve recall rates of detection."),
  ("Research focuses on detection precision and neglects interpretability, which diagnostics require.", "Discussion and conclusion",
   "anomaly detection research focuses primarily on detection precision, failing to address the issue of interpretability."),
  ("Multivariate high-dimensional series are particularly challenging (sparsity, temporal and inter-dimension dependencies).", "Discussion and conclusion",
   "The detection of anomalies in multivariate high-dimensional time series data presents a particular challenge"),
  ("Models are vulnerable to noise in the input data.", "Discussion and conclusion",
   "models are vulnerable, and their performance is compromised by noise in the input data."),
  ("The anomaly score is mostly defined from a loss function (e.g. reconstruction error).", "Deep anomaly detection methods",
   "An anomaly score is mostly defined based on a loss function."),
])

write_card({
  "id": P.id,
  "title": "Deep Learning for Time Series Anomaly Detection: A Survey",
  "authors": ["Zahra Zamanzadeh Darban", "Geoffrey I. Webb", "Shirui Pan", "Charu C. Aggarwal", "Mahsa Salehi"],
  "year": 2023,
  "links": {"arxiv": "https://arxiv.org/abs/2211.05244"},
  "source": {"version": "arXiv v3", "retrieved_at": "2026-10-02", "pdf_sha256": P.sha256()},
  "tags": {"tasks": ["time-series-anomaly-detection"],
           "method_families": ["reconstruction-based-detectors", "forecasting-based-detectors", "deep-learning"],
           "paradigms": ["unsupervised"]},
  "proposes": ["Taxonomy of deep TSAD models (forecasting, reconstruction, representation, hybrid)"],
  "claims": claims,
  "results": [],
  "relations": [],
  "card": {"created_at": "2026-10-02", "created_by": "claude-opus-5-5 via Claude Code", "reviewed": False,
           "notes": "Survey without experiments. The PDF shows only an ACM template placeholder ('1, 1 (May 2023)') and no venue, so 'venue' is empty."},
})
print(len(claims), "claims")
