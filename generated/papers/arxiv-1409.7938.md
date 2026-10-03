<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Lazier Than Lazy Greedy

- カード: [`arxiv-1409.7938`](../../papers/arxiv-1409.7938.yaml)
- 著者: Baharan Mirzasoleiman, Ashwinkumar Badanidiyuru, Amin Karbasi, Jan Vondrak, Andreas Krause
- 年・掲載: 2014
- 原論文: [PDF](https://arxiv.org/pdf/1409.7938v3)(arXiv v3、カード作成時に読んだ版)
- タグ: data-subset-selection, greedy-methods
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Classical guarantee cited (Nemhauser, Wolsey and Fisher 1978): for maximizing a non-negative monotone submodular function under a cardinality constraint (|A| <= k), the simple greedy algorithm (add the element with largest marginal gain, k times; O(n k) evaluations) achieves a (1-1/e) approximation to the optimal (intractable) solution.([Introduction, p.1](https://arxiv.org/pdf/1409.7938v3#page=1 "states that for non-negative monotone submodular functions a simple greedy algorithm provides a solution with (1−1/e) approximation guarantee to the optimal (intractable) solution."))
- **c2** Prior accelerated greedy (LAZY-GREEDY, Minoux 1978): its exact cost in function evaluations is unknown, although it gives orders-of-magnitude speedups in practice.([Introduction, p.2](https://arxiv.org/pdf/1409.7938v3#page=2 "Even though the exact cost (i.e., number of function evaluations) of LAZY-GREEDY is unknown, this algorithm leads to orders of magnitude speedups in practice."))
- **c3** Guarantee of the proposed method (theoretical; for monotone submodular maximization under a cardinality constraint): the randomized STOCHASTIC-GREEDY achieves a (1-1/e-epsilon) approximation in expectation, in time linear in the data size and independent of the cardinality constraint.([Abstract, p.1](https://arxiv.org/pdf/1409.7938v3#page=1 "We show that our randomized algorithm, STOCHASTIC-GREEDY, can achieve a (1 −1/e −ε) approximation guarantee, in expectation, to the optimum solution in time linear in the size of the data and independent of the cardinality constraint."))
- **c4** Assumptions of the guarantee (Theorem 1): f non-negative, monotone and submodular, problem (1) with a cardinality constraint, and sample size s = (n/k) log(1/epsilon) per step; the bound is in expectation and uses O(n log(1/epsilon)) function evaluations.([STOCHASTIC-GREEDY Algorithm, p.3](https://arxiv.org/pdf/1409.7938v3#page=3 "Let f be a non-negative monotone submoduar function."))
- **c5** Cost measurement: computational cost is measured as the number of function evaluations, to be independent of implementation and platform; baselines are random selection, LAZY-GREEDY, SAMPLE-GREEDY (lazy greedy on a random subsample) and THRESHOLD-GREEDY.([Experimental Results, p.3](https://arxiv.org/pdf/1409.7938v3#page=3 "In order to compare the computational cost of different methods independently of the concrete implementation and platform, in our experiments we measure the computational cost in terms of the number of function evaluations used."))
- **c6** Data subset selection setting: active set selection for Gaussian Process regression (information gain, Informative Vector Machine) on the Parkinsons Telemonitoring dataset.([Experimental Results, p.4](https://arxiv.org/pdf/1409.7938v3#page=4 "We used the Parkinsons Telemonitoring dataset (Tsanas et al. 2010) consisting of 5,875 bio-medical voice measurements with 22 attributes from people with early-stage Parkinsons disease."))
- **c7** Empirical claim: STOCHASTIC-GREEDY practically reaches the same utility as lazy greedy while running much faster.([Abstract, p.1](https://arxiv.org/pdf/1409.7938v3#page=1 "We observe that STOCHASTIC-GREEDY practically achieves the same utility value as lazy greedy but runs much faster."))

