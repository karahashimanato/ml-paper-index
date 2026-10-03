<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Divide and Conquer Networks

- カード: [`arxiv-1611.02401`](../../papers/arxiv-1611.02401.yaml)
- 著者: Alex Nowak-Vila, David Folqué, Joan Bruna
- 年・掲載: 2016
- 原論文: [PDF](https://arxiv.org/pdf/1611.02401v7)(arXiv v7、カード作成時に読んだ版)
- タグ: algorithm-learning, combinatorial-optimization, deep-learning, divide-and-conquer, graph-neural-networks, reinforcement-learning, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Both division and merging are learned: the architecture learns two scale-invariant operations, how to split an input into smaller sets and how to merge two partial solutions, each a single network applied recursively with shared parameters across scales.([Abstract, p.1](https://arxiv.org/pdf/1611.02401v7#page=1 "by learning two scale-invariant atomic operations: how to split a given input into smaller sets, and how to merge two partially solved tasks into a larger partial solution."))
- **c2** Training: because the split is discrete, its parameters are trained with policy gradient (REINFORCE), while the merge is trained by standard backpropagation; the model can learn from input-output pairs only or from a non-differentiable reward.([Introduction, p.2](https://arxiv.org/pdf/1611.02401v7#page=2 "Since our split block is inherently discrete, we resort to policy gradient to train the split parameters, while using standard backpropagation for the merge phase"))
- **c3** Heuristic, not exact: optimizing the cost over set partitions is described as intractable in general; if the cost is subadditive, the recursive splitting can be used as an efficient greedy strategy because the sum over the two halves is a surrogate upper bound that depends only on smaller sets (the paper presents this as a greedy surrogate, not as an optimality guarantee).([Learning from non-differentiable rewards, p.4](https://arxiv.org/pdf/1611.02401v7#page=4 "then the hierarchical splitting from (3) can be used as an efﬁcient greedy strategy, since the right hand side acts as a surrogate upper bound that depends only on smaller sets."))
- **c4** Size generalization protocol (knapsack): the model is trained on 20000 instances with n = 50 and evaluated on new instances with n = 50, 100 and 200 (uniform weights/values, capacity uniform in [0.2n, 0.3n]).([Knapsack, p.9](https://arxiv.org/pdf/1611.02401v7#page=9 "We generate 20000 problem instances of size n = 50 to train the model, and evaluate its performance on new instances of size n = 50, 100, 200."))
- **c5** Limitation: Dantzig's greedy algorithm eventually outperforms DiCoNet at n = 200, which the authors say suggests relaxing the scale-invariance assumption or adding task-specific prior knowledge.([Knapsack, p.9](https://arxiv.org/pdf/1611.02401v7#page=9 "However, we observe that the Dantzig greedy algorithm eventually outperforms the DiCoNet for sufﬁciently large input n = 200, suggesting that further improvements may come from relaxing the scale invariance assumption, or by incorporating extra prior knowledge of the task."))
- **c6** Comparison with prior learned knapsack work: the authors state their knapsack approach does not match Bello et al. (2016) in best approximation, while arguing it uses a simpler GNN with lower complexity and generalizes to larger n than trained on.([Knapsack, p.9](https://arxiv.org/pdf/1611.02401v7#page=9 "This approach of the knapsack problem does not perform as good as (Bello et al., 2016) in obtaining the best approximation."))
- **c7** TSP (appendix, preliminary): scale invariance is weaker for TSP since it is not straightforward to build a tour from two partial tours, but the authors observe some degree of it suffices to improve scalability when testing beyond the training size.([Appendix C (Travelling Salesman Problem), p.14](https://arxiv.org/pdf/1611.02401v7#page=14 "Although the scale invariance of the TSP is not as clear as in the previous problems (it is not straightforward how to use two TSP partial solutions to build a larger one), we observe that some degree of scale invariance it is enough in order to improve on scalability."))

