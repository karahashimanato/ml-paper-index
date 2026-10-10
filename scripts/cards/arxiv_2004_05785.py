"""Learning under Concept Drift: A Review (Lu et al., IEEE TKDE) のカード。サーベイのため results は無い。"""

import sys

sys.path.insert(0, "scripts/cards")
from _common import Paper, write_card  # noqa: E402

P = Paper("arxiv-2004.05785")

claims = P.claims([
  ("The survey reviews over 130 publications on concept drift.", "Abstract",
   "This paper reviews over 130 high quality publications in concept drift related research areas"),
  ("Learning under concept drift is organized into three components: drift detection, drift understanding and drift adaptation.", "Abstract",
   "establishes a framework of learning under concept drift including three main components: concept drift detection, concept drift understanding, and concept drift adaptation."),
  ("Concept drift is defined as a change of the joint distribution P(X, y) over time (covering covariate shift and changes in P(y|X)).", "Concept drift definition",
   "concept drift at time t can be defined as the change of joint probability of X and y at time t."),
  ("Drift in P(X) alone does not move the decision boundary and is called virtual drift.", "Concept drift definition",
   "drift does not affect the decision boundary, it has also been considered as virtual drift"),
  ("Without the data-retrieval stage, drift detection can be viewed as a two-sample test problem.", "Drift detection framework",
   "the concept drift detection problem can be considered as a two-sample test problem which examines whether the population of two given sample sets are from the same distribution"),
  ("Drift detectors are classified into three categories by their test statistic: error rate-based, data distribution-based, and multiple hypothesis test.", "Section 3.2",
   "This section surveys drift detection methods and algorithms, which are classified into three categories in terms of the test statistics they apply."),
  ("Error rate-based detectors (tracking the online error rate of a base classifier) are the largest category.", "Section 3.2.1",
   "error rate-based drift detection algorithms form the largest category of algorithms."),
  ("DDM was the first algorithm to define warning and drift levels.", "Section 3.2.1",
   "the first algorithm to define the warning level and drift"),
  ("Data distribution-based detectors address drift at its root (the distribution) and can locate it, but usually cost more computation and need predefined windows.", "Data distribution-based drift detection",
   "these algorithms are usually reported as incurring higher computational cost than the algorithms mentioned in Section 3.2.1"),
  ("All drift detectors can answer 'when', but very few can answer 'how' and 'where'.", "Conclusions",
   "all drift detection methods can answer \"When\", but very few methods have the ability to answer \"How\" and \"Where\";"),
  ("Most detection and adaptation algorithms assume true labels are available right after prediction; unsupervised/semi-supervised drift detection is rarely studied.", "Conclusions",
   "Most existing drift detection and adaptation algorithms assume the ground true label is available after classification/prediction, or extreme verification latency."),
  ("There is no comprehensive analysis of real-world streams in terms of drift time, severity and regions.", "Conclusions",
   "There is no comprehensive analysis on real-world data streams from the concept drift aspect"),
  ("The survey lists 10 synthetic and 14 public real-world datasets used to evaluate drift handling.", "Abstract",
   "This paper lists and discusses 10 popular synthetic datasets and 14 publicly available benchmark datasets"),
  ("Research on retraining models with explicit drift detection has slowed; adaptive models and ensembles have become more important.", "Conclusions",
   "research of retraining models with explicit drift detection has slowed;"),
  ("Decomposition used to classify drift sources: P_t(X, y) = P_t(X) x P_t(y|X); Source I is a change in P_t(X) with P_t(y|X) unchanged (virtual drift), Source II is a change in P_t(y|X) with P_t(X) unchanged (actual drift, moving the decision boundary), and Source III is a mixture of both.", "Concept drift definition", "concept drift can be triggered by three sources:"),
])

write_card({
  "id": P.id,
  "title": "Learning under Concept Drift: A Review",
  "authors": ["Jie Lu", "Anjin Liu", "Fan Dong", "Feng Gu", "João Gama", "Guangquan Zhang"],
  "year": 2020,
  "links": {"arxiv": "https://arxiv.org/abs/2004.05785"},
  "source": {"version": "arXiv v1", "retrieved_at": "2026-10-02", "pdf_sha256": P.sha256()},
  "tags": {"tasks": ["concept-drift-detection"],
           "method_families": ["error-rate-drift-detectors", "window-based-drift-detectors", "two-sample-tests"],
           "paradigms": ["streaming"]},
  "proposes": ["Framework of learning under concept drift (detection, understanding, adaptation)"],
  "claims": claims,
  "results": [],
  "relations": [],
  "card": {"created_at": "2026-10-02", "created_by": "claude-opus-5-5 via Claude Code", "reviewed": False,
           "notes": "Survey without experiments. The arXiv v1 PDF does not state a publication venue; 'year' is the arXiv posting year (April 2020)."},
})
print(len(claims), "claims")
