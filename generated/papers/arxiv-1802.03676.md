<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Differentiable Dynamic Programming for Structured Prediction and Attention

- カード: [`arxiv-1802.03676`](../../papers/arxiv-1802.03676.yaml)
- 著者: Arthur Mensch, Mathieu Blondel
- 年・掲載: 2018
- 原論文: [PDF](https://arxiv.org/pdf/1802.03676v2)(arXiv v2、カード作成時に読んだ版)
- タグ: deep-learning, dynamic-programming, language-modeling, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Contribution: smooth the max operator inside the DP recursion with a strongly convex regularizer, relaxing both the optimal value and the optimal solution and making a broad class of DP algorithms differentiable.([Abstract, p.1](https://arxiv.org/pdf/1802.03676v2#page=1 "To address this issue, we propose to smooth the max operator in the dynamic programming recursion, using a strongly convex regularizer."))
- **c2** Scope: the framework is stated for DPs viewed as finding the highest-scoring path between a start and end node of a weighted DAG; the paper instantiates it for the Viterbi algorithm (sequence prediction) and DTW (time-series alignment).([Differentiable DP layers, p.3](https://arxiv.org/pdf/1802.03676v2#page=3 "Every problem solved by dynamic programming reduces to ﬁnding the highest-scoring path between a start node and an end node, on a weighted directed acyclic graph (DAG)."))
- **c3** Guarantees: smoothing locally inside the recursion (DP_Omega) generally differs from smoothing the global max over all paths (LP_Omega >= DP_Omega), but Proposition 2 shows DP_Omega is convex and that LP - DP_Omega lies between (N-1) times the lower and upper bounds of Omega on the simplex (Omega strongly convex; N = number of DAG nodes), so DP_{gamma Omega} converges to the hard value LP as gamma -> 0.([Differentiable DP layers, p.5](https://arxiv.org/pdf/1802.03676v2#page=5 "Although LPΩ(θ) and DPΩ(θ) are generally diﬀerent (in fact, LPΩ(θ) ≥DPΩ(θ) for all θ ∈Θ), we now show that DPΩ(θ) is a sensible approximation of LP(θ) in several respects."))
- **c4** Uniqueness result: for separable regularizers, the negentropy-smoothed max is the only smoothed max that is associative (so DP_Omega equals LP_Omega only for negentropy), the 'only if' part being new to the authors' knowledge (the 'if' part recovers known message-passing results).([Differentiable DP layers, p.5](https://arxiv.org/pdf/1802.03676v2#page=5 "Its proof shows that max−γH is the only maxΩ satisfying associativity, exhibiting a functional equation from information theory (Horibe, 1988)."))
- **c5** What is lost: the authors note that the CRF-style smoothing (changing the semiring to (+, x) on exponentiated values) loses the sparsity of solutions because hard assignments become soft; with their squared-l2 regularizer the expected path (gradient) is instead typically sparse (smaller gamma, sparser), whereas negentropy always gives dense solutions.([Introduction, p.2](https://arxiv.org/pdf/1802.03676v2#page=2 "While this modiﬁcation smoothes the dynamic program, it looses the sparsity of solutions, since hard assignments become soft ones."))
- **c6** Complexity: the gradient (an expected path under a random walk on the DAG) is computed by backpropagation in reverse topological order with total cost O(|E|), the same as the hard DP, under the stated assumption that the smoothed max is computable in linear time; Hessian-vector products also cost O(|E|). This holds for any strongly convex Omega in the framework; it is a complexity statement, not an approximation guarantee.([Differentiable DP layers, p.6](https://arxiv.org/pdf/1802.03676v2#page=6 "Assuming maxΩcan be computed in linear time, the total cost is O(/E/), the same as DP(θ)."))
- **c7** Evaluation: named entity recognition on the four CoNLL 2003 languages (step size and batch size chosen by a small grid search, model selected on the validation set), supervised audio-to-score alignment on Bach10 with leave-one-out cross-validation, and structured attention for French-English translation on a 1M-sentence WMT14 subset; for NER the authors report all losses within 1% F1 of each other with proper parameter selection.([Experiments, p.10](https://arxiv.org/pdf/1802.03676v2#page=10 "With proper parameter selections, all losses perform within 1% F1-score of each other, although entropy-regularized losses perform slightly better on 3/4 languages."))

