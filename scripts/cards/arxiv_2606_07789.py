"""Concept drift detector benchmarking framework (Cerqueira et al., KDD 2026) のカード。
Table 1 (abrupt) / Table 2 (gradual): ドリフトの種類ごとの F1 平均順位を読む。"""

import sys

sys.path.insert(0, "scripts/cards")
from _common import Paper, register, write_card  # noqa: E402

P = Paper("arxiv-2606.07789")
DETECTORS = ["ABCD", "ABCD(X)", "ADWIN", "CUSUM", "DDM", "EWMA", "GMA", "HDDMA", "HDDMW", "PH", "RDDM", "SEED", "STEPD", "STUDD"]
DRIFTS = ["feature-filtering", "feature-permutation", "class-prior", "class-swap"]

ls = P.lines(7)
results = []
for table, mode in (("Table 1:", "abrupt"), ("Table 2:", "gradual")):
    k = next(i for i, l in enumerate(ls) if l.startswith(table))
    k = ls.index("Swap", k) + 1
    for det in DETECTORS:
        assert ls[k] == det, (table, ls[k], det)
        vals = ls[k + 1:k + 5]
        quote = " ".join(ls[k:k + 5])
        for drift, v in zip(DRIFTS, vals):
            results.append({"id": f"r{len(results) + 1}", "benchmark": f"cerqueira2026-{mode}-{drift}", "method": det,
                            "metric": "avg-rank-f1", "value": float(v), "location": table.rstrip(":"), "page": 7, "quote": quote})
        k += 5
assert len(results) == 2 * 14 * 4

claims = P.claims([
  ("Drift detector evaluation is inconsistent: oversimplified synthetic generators, incompatible metrics, and opaque hyperparameter selection.", "Abstract",
   "studies rely on oversimplified synthetic data generators, adopt incompatible metrics, and lack transparency in hyperparameter selection"),
  ("14 widely used detectors are benchmarked on 7 real-world datasets with 4 injected drift types, each abrupt and gradual.", "Abstract",
   "We benchmark 14 widely used drift detection methods on 7 real-world datasets across 4 drift types"),
  ("SEED, STEPD and ABCD consistently outperformed the other detectors across drift types.", "Introduction",
   "Our results reveal that SEED [23], STEPD [25], and ABCD [22] consistently outperform other detectors across distinct drift types"),
  ("Hyperparameter optimization with the proposed protocol significantly improved detection over default configurations.", "Introduction",
   "hyperparameter optimization using our proposed approach significantly improves detection performance over default configurations."),
  ("Classic metrics MTFA and MDT depend on stream length and drift spacing, preventing cross-dataset comparison.", "Related work",
   "MTFA and MDT are highly dependent on stream length and drift spacing"),
  ("An F1 score for drift detection ignores timing: a detector with unacceptable delay can still get perfect F1.", "Related work",
   "its formulation ignores the temporal aspect: a detector with unacceptable delay can still achieve perfect F1."),
  ("Detector hyperparameters are tuned with leave-one-dataset-out cross-validation.", "Section 3.3",
   "we propose a leave-one-dataset-out cross-validation approach for optimizing the hyperparameters of drift detectors."),
  ("Tuning and evaluating detectors on the same dataset can overfit and make reported results overly optimistic.", "Section 3.3",
   "using the same dataset for optimizing and evaluating the detector can cause overfitting and lead to overly optimistic performance estimates reported in the respective papers."),
  ("Each dataset and drift type is evaluated with 50 Monte Carlo trials (random drift onset).", "Experimental setup",
   "For each dataset and drift type, we perform 50 Monte Carlo trials."),
  ("A Hoeffding Tree with default hyperparameters is the monitored classifier.", "Experimental setup",
   "We select the Hoeffding Tree [10] as the classifier in the experiments"),
  ("PH and EWMA were ineffective regardless of configuration.", "Main findings",
   "PH and EWMA remain ineffective regardless of configuration, suggesting fundamental limitations"),
  ("Unsupervised detectors (ABCD(X), STUDD) detect feature-space drifts but not label-only changes.", "Main findings",
   "Unsupervised detectors (ABCD(X) and STUDD) perform better on feature-space drifts (feature permutation, feature filtering) than on label-based changes (class prior, class swaps)"),
  ("Gradual drifts are systematically harder to detect than abrupt ones.", "Main findings",
   "Gradual drifts are systematically harder to detect than abrupt ones."),
  ("STEPD's strong results are largely due to effective tuning.", "Main findings",
   "STEPD's strong performance is largely attributable to effective tuning."),
  ("Limitations: one classifier (Hoeffding tree), four drift types, seven datasets.", "Limitations",
   "the experiments are limited to one classifier (Hoeffding tree) and four drift types simulated in 7 real-world datasets."),
  ("Limitation: labels are assumed to be available immediately after each prediction (no verification delay).", "Limitations",
   "it assumes immediate feedback, with labels being readily available at each step after inference."),
  ("Shuffling the real streams before injecting drift removes their natural temporal structure.", "Limitations",
   "it also removes any inherent temporal structure."),
  ("Practical guidance: SEED and STEPD are robust defaults when drift characteristics are unknown.", "Main findings",
   "SEED and STEPD are robust defaults when drift characteristics are unknown"),
  ("Hyperparameters are searched with 30 iterations of random search.", "Experimental setup",
   "The optimization is conducted using 30 iterations of random search."),
  ("The main objective is a standardized evaluation protocol, not identifying the best detector.", "Experimental setup",
   "our main objective is to establish a standardized evaluation protocol rather than to identify the best performing detector."),
])

write_card({
  "id": P.id,
  "title": "A Framework for Evaluating and Benchmarking Concept Drift Detection Methods",
  "authors": ["Vitor Cerqueira", "Heitor Murilo Gomes", "Marco Heyden", "Bernhard Pfahringer", "Albert Bifet"],
  "year": 2026,
  "venue": "KDD 2026",
  "links": {"arxiv": "https://arxiv.org/abs/2606.07789", "code": "https://github.com/vcerqueira/experiments-drift_evaluation"},
  "source": {"version": "arXiv v1", "retrieved_at": "2026-10-02", "pdf_sha256": P.sha256(), "license": "CC BY 4.0"},
  "tags": {"tasks": ["concept-drift-detection"],
           "method_families": ["error-rate-drift-detectors", "window-based-drift-detectors"],
           "paradigms": ["streaming"]},
  "proposes": ["Semi-synthetic drift injection into real streams (Monte Carlo)", "Timing-aware drift detection metrics", "Leave-one-dataset-out HPO for detectors"],
  "claims": claims,
  "results": results,
  "relations": [],
  "card": {"created_at": "2026-10-02", "created_by": "claude-opus-5-5 via Claude Code", "reviewed": False,
           "notes": ("Tables 1-2 (average rank by F1 detection score; lower is better) extracted mechanically. Raw F1/FAR/MDT values are in the appendix and were not recorded. "
                     "Ranks are among the 14 detectors only. Section numbers other than 3.3 were not verified, so descriptive locations are used.")},
})

COMMON = {"split": "7 real-world streams (USP Data Stream Repository), shuffled, with one injected drift per Monte Carlo trial at a random point between 50% and 80% of the stream (drift simulation and experimental setup sections).",
          "preprocessing": "Detectors monitor the Hoeffding Tree's error (ABCD(X) monitors features, STUDD a compression loss) (experimental setup).",
          "tuning": "Leave-one-dataset-out random search (30 iterations) maximizing F1 detection score (experimental setup).",
          "repetitions": "50 Monte Carlo trials per dataset and drift type; average rank across the 7 datasets (Tables 1-2)."}
register(P.id, [{"id": f"cerqueira2026-{mode}-{d}", "scope": "public", "task": "concept-drift-detection",
                 "dataset": f"Cerqueira et al. framework: 7 real-world streams with injected {mode} {d.replace('-', ' ')} drift", "protocol": COMMON,
                 "metrics": [{"name": "avg-rank-f1", "higher_is_better": False,
                              "definition": "Average rank (among the 14 detectors) of the F1 detection score across datasets."}],
                 "defined_in": P.id} for mode in ("abrupt", "gradual") for d in DRIFTS])
print(len(results), "results,", len(claims), "claims")
