"""Failing Loudly (Rabanser et al., NeurIPS 2019) のカード。Table 1(a): 次元削減手法 x 検定ごとの検出精度を、テストサンプル数ごとに読む。"""

import re
import sys

sys.path.insert(0, "scripts/cards")
from _common import Paper, register, write_card  # noqa: E402

P = Paper("arxiv-1810.11953")
SIZES = ["10", "20", "50", "100", "200", "500", "1000", "10000"]
BENCH = {s: f"rabanser2019-shift-suite-n{s}" for s in SIZES}

ls = P.lines(7)
i = ls.index("10,000") + 1
end = ls.index("(b) Detection accuracy of different shifts on")
body = ls[i:end]
GROUP = {"Univ. tests": "KS (Bonferroni)", "Multiv. tests": "MMD"}
SPECIAL = {"χ2": ("BBSDh", "Chi-squared"), "Bin": ("Classif", "Binomial")}
VAL = re.compile(r"^(?:[0-9]\.[0-9]{2}|–)$")

results, k, test = [], 0, None
while k < len(body):
    tok = body[k]
    if tok in GROUP:
        test, k = GROUP[tok], k + 1
        continue
    if tok in SPECIAL:
        dr, tname = SPECIAL[tok]
        assert body[k + 1] == dr, body[k:k + 3]
        method, k = f"{dr} + {tname}", k + 1
    else:
        method = f"{tok} + {test}"
    vals = body[k + 1:k + 9]
    assert len(vals) == 8 and all(VAL.match(v) for v in vals), (method, vals)
    quote = " ".join(body[k:k + 9])
    for size, v in zip(SIZES, vals):
        if v == "–":
            continue
        results.append({"id": f"r{len(results) + 1}", "benchmark": BENCH[size], "method": method, "metric": "detection-accuracy",
                        "value": float(v), "location": "Table 1(a)", "page": 7, "quote": quote})
    k += 9
assert len(results) == 14 * 8 - 6, len(results)  # MMD は 10,000 サンプルで未実施(–)

claims = P.claims([
  ("Across the explored shifts, two-sample testing on representations from a pre-trained label classifier (black-box shift detection) performed best.", "Abstract",
   "a two-sample-testing-based approach, using pre-trained classifiers for dimensionality reduction, performs best."),
  ("BBSD works surprisingly well across many shifts even when its label-shift assumption does not hold.", "Introduction",
   "We show (empirically) that BBSD works surprisingly well under a broad set of shifts, even when the label shift assumption is not met."),
  ("Aggregated univariate tests (KS + Bonferroni) performed comparably to multivariate kernel tests (MMD).", "Experiments (results)",
   "despite the heavy correction, multiple univariate testing seem to offer comparable performance to multivariate testing"),
  ("BBSDs (softmax outputs) was the best dimensionality reduction for univariate testing and overall; an untrained autoencoder (UAE) was best for multivariate testing.", "Experiments (results)",
   "In the multivariate-testing case, UAE performed best."),
  ("The domain classifier performs badly with few samples (<=100) but catches up with more samples.", "Experiments (results)",
   "The domain classifier, a popular shift detection approach, performs badly in the low-sample regime (≤100 samples), but catches up as more samples are obtained."),
  ("Multivariate testing without dimensionality reduction performs poorly.", "Experiments (results)",
   "the multivariate test performs poorly in the no reduction case"),
  ("Domain-discriminating classifiers help characterize shifts and judge whether they are harmful.", "Abstract",
   "we demonstrate that domain-discriminating approaches tend to be helpful for characterizing shifts qualitatively and determining if they are harmful."),
  ("In practice, ML pipelines rarely inspect incoming data for distribution shift.", "Introduction",
   "in practice, ML pipelines rarely inspect incoming data for signs of distribution shift."),
  ("Kernel two-sample tests scale badly with sample size and lose power in high dimensions.", "Introduction",
   "they scale badly with dataset size and their statistical power is known to decay badly with high ambient dimension"),
  ("Detection results are averaged over 5 random splits, at significance level 0.05.", "Experiments",
   "shift detection performance is averaged over a total of 5 random splits"),
  ("The original MNIST train/test split is not i.i.d. (a statistically significant but harmless shift in the digit 6).", "Experiments (results)",
   "this result however still shows that the original MNIST split is not i.i.d."),
  ("The experiments mostly use standard image classification; other domains (NLP, graphs) and online data are left for future work.", "Conclusions",
   "since we have mostly explored a standard image classification setting for our experiments"),
  ("A detected shift is not necessarily harmful: on COIL-100 the detected shift did not hurt the classifier.", "Experiments (results)",
   "this shift does not harm the classifier's performance"),
  ("Shift detection for online (streaming) data would need to handle correlation between adjacent time steps (future work).", "Conclusions",
   "shift detection for online data, which would require us to account for and exploit the high degree of correlation between adjacent time steps"),
  ("MMD (Eq. 2-3): MMD(F, p, q) = ||mu_p - mu_q||_F^2 compares the mean embeddings of two distributions in an RKHS; the unbiased estimate of squared MMD averages the kernel over pairs within the first sample (m(m-1) pairs) and within the second sample (n(n-1) pairs) and subtracts twice the average kernel between the samples (mn pairs).", "Section 3.2", "MMD allows us to distinguish between two probability distributions p and q based on the mean embeddings µp and µq of the distributions in a reproducing kernel Hilbert space F, formally"),
  ("MMD implementation in the paper: squared exponential kernel exp(-||x - x'||^2 / sigma) with sigma set to the median distance between points in the pooled sample; the p-value is obtained by a permutation test on the kernel matrix.", "Section 3.2", "A p-value can then be obtained by carrying out a permutation test on the resulting kernel matrix."),
  ("KS statistic (Eq. 4): Z = sup_z |F_p(z) - F_q(z)|, the largest difference between the empirical CDFs of source and target data, which under the null hypothesis follows the Kolmogorov distribution; it is applied to each of the K dimensions separately.", "Section 3.2", "Under the null hypothesis, Z follows the Kolmogorov distribution."),
  ("Bonferroni aggregation: because the dependence among the K per-dimension tests is unknown, the conservative Bonferroni correction is used, rejecting the null hypothesis if the minimum p-value among all tests is less than alpha/K.", "Section 3.2", "As we cannot make strong assumptions about the (in)dependence among the tests, we rely on a conservative aggregation method, notably the Bonferroni correction [4], which rejects the null hypothesis if the minimum p-value among all tests is less than α/K"),
])

write_card({
  "id": P.id,
  "title": "Failing Loudly: An Empirical Study of Methods for Detecting Dataset Shift",
  "authors": ["Stephan Rabanser", "Stephan Günnemann", "Zachary C. Lipton"],
  "year": 2019,
  "venue": "NeurIPS 2019",
  "links": {"arxiv": "https://arxiv.org/abs/1810.11953", "code": "https://github.com/steverab/failing-loudly"},
  "source": {"version": "arXiv v4", "retrieved_at": "2026-10-02", "pdf_sha256": P.sha256()},
  "tags": {"tasks": ["dataset-shift-detection"],
           "method_families": ["two-sample-tests", "dimensionality-reduction-for-shift"],
           "paradigms": ["supervised"]},
  "proposes": ["Empirical comparison of dimensionality reduction + two-sample testing pipelines for shift detection"],
  "claims": claims,
  "results": results,
  "relations": [],
  "card": {"created_at": "2026-10-02", "created_by": "claude-opus-5-5 via Claude Code", "reviewed": False,
           "notes": ("Table 1(a) extracted mechanically: detection accuracy averaged over all simulated shifts on MNIST and CIFAR-10, per number of test samples. "
                     "Each sample size is registered as a separate benchmark. MMD was not run at 10,000 samples. Table 1(b) (per shift type) and Table 2 were not recorded. "
                     "Image data only; results may not transfer to tabular or streaming settings (c12, c14).")},
})

COMMON = {"split": "MNIST and CIFAR-10 split into train/validation/test; shifts applied to the test set only; 5 random splits (Section 5).",
          "preprocessing": "Dimensionality reduction to K=32 (PCA, SRP, UAE, TAE) or to class outputs (BBSDs, BBSDh, Classif), learned on training data (Section 5).",
          "tuning": "Not applicable (fixed architectures; ResNet-18 label/domain classifiers; significance level 0.05).",
          "repetitions": "Detection accuracy averaged over 5 random splits and all simulated shift types/intensities/fractions (Table 1a)."}
register(P.id, [{"id": BENCH[s], "scope": "paper-private", "task": "dataset-shift-detection",
                 "dataset": f"MNIST and CIFAR-10 with the paper's simulated shifts, {s} target samples", "protocol": COMMON,
                 "metrics": [{"name": "detection-accuracy", "higher_is_better": True,
                              "definition": "Fraction of runs in which shift was detected at alpha = 0.05, averaged over shift settings (Table 1a)."}],
                 "defined_in": P.id} for s in SIZES])
print(len(results), "results,", len(claims), "claims")
