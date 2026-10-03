<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Stochastic Optimization of Sorting Networks via Continuous Relaxations

- カード: [`arxiv-1903.08850`](../../papers/arxiv-1903.08850.yaml)
- 著者: Aditya Grover, Eric Wang, Aaron Zweig, Stefano Ermon
- 年・掲載: 2019
- 原論文: [PDF](https://arxiv.org/pdf/1903.08850v2)(arXiv v2、カード作成時に読んだ版)
- タグ: deep-learning, differentiable-sorting, image-classification, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Problem statement: the sorting operator is non-differentiable with respect to its inputs, which prevents end-to-end gradient-based optimization of pipelines that contain a sort.([Abstract, p.1](https://arxiv.org/pdf/1903.08850v2#page=1 "However, the sorting operator is non-differentiable with respect to its inputs, which prohibits end-to-end gradient-based optimization."))
- **c2** Contribution: NeuralSort relaxes the output of sorting from permutation matrices to unimodal row-stochastic matrices (rows sum to one, each row has a distinct argmax), so a hard permutation can still be read off by a row-wise argmax.([Abstract, p.1](https://arxiv.org/pdf/1903.08850v2#page=1 "In this work, we propose NeuralSort, a general-purpose continuous relaxation of the output of the sorting operator from permutation matrices to the set of unimodal row-stochastic matrices, where every row sums to one and has a distinct arg max."))
- **c3** Complexity: the relaxation needs O(n^2) operations (pairwise absolute differences), versus O(n log n) for the best known sorting algorithms; the authors add that in practice it is highly parallelizable on GPUs.([NeuralSort: the relaxed sorting operator, p.5](https://arxiv.org/pdf/1903.08850v2#page=5 "The relaxation requires O(n2) operations to compute As, as opposed to the O(n log n) overall complexity for the best known sorting algorithms."))
- **c4** Guarantee and its assumption: for every temperature the row-wise argmax of the relaxed matrix equals sort(s); convergence of the relaxed matrix to the exact permutation matrix as temperature goes to 0 is stated almost surely under the assumption that the entries are drawn independently from an absolutely continuous distribution (so ties have probability zero).([NeuralSort: the relaxed sorting operator (Theorem 4), p.5](https://arxiv.org/pdf/1903.08850v2#page=5 "If we assume that the entries of s are drawn independently from a distribution that is absolutely continuous w.r.t. the Lebesgue measure in R, then the following convergence holds almost surely:"))
- **c5** Approximation trade-off: lower temperature gives a tighter approximation, but the variance of the gradient estimates is typically lower at higher temperatures.([NeuralSort: the relaxed sorting operator, p.5](https://arxiv.org/pdf/1903.08850v2#page=5 "In practice however, the trade-off is in the variance of these estimates, which is typically lower for larger temperatures."))
- **c6** Evaluation protocol (large-MNIST sorting, n in {3, 5, 7, 9, 15}): the temperature of both the Sinkhorn-based baselines and NeuralSort was tuned over {1, 2, 4, 8, 16} by best validation accuracy on predicting entire permutations; all methods share the same CNN and are trained with a cross-entropy loss against the ground-truth permutation matrix.([Appendix D.1 (Sorting handwritten numbers, Hyperparameters), p.19](https://arxiv.org/pdf/1903.08850v2#page=19 "We tuned this hyperparameter on the set {1, 2, 4, 8, 16} by picking the model with the best validation accuracy on predicting entire permutations"))
- **c7** Main empirical claim (sorting large-MNIST sequences): both NeuralSort variants significantly outperform the vanilla row-stochastic, Sinkhorn and Gumbel-Sinkhorn baselines for all sequence lengths n considered.([Experiments (Sorting handwritten numbers), p.8](https://arxiv.org/pdf/1903.08850v2#page=8 "Table 1 demonstrates that the approaches based on the proposed sorting relaxation signiﬁcantly outperform the baseline approaches for all n considered."))

