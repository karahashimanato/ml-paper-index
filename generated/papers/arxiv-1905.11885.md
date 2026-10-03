<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Differentiable Ranks and Sorting using Optimal Transport

- カード: [`arxiv-1905.11885`](../../papers/arxiv-1905.11885.yaml)
- 著者: Marco Cuturi, Olivier Teboul, Jean-Philippe Vert
- 年・掲載: 2019
- 原論文: [PDF](https://arxiv.org/pdf/1905.11885v2)(arXiv v2、カード作成時に読んだ版)
- タグ: deep-learning, differentiable-sorting, image-classification, supervised, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Problem statement: sorting outputs the sorted values (piecewise linear) and the permutation/ranks (integer-valued), neither of which is differentiable.([Abstract, p.1](https://arxiv.org/pdf/1905.11885v2#page=1 "Indeed, sorting procedures output two vectors, neither of which is differentiable: the vector of sorted values is piecewise linear, while the sorting permutation itself (or its inverse, the vector of ranks) has no differentiable properties to speak of, since it is integer-valued."))
- **c2** Relation to sorting: sorting is viewed as an optimal assignment of the n values to any increasing family of n target values (the introduction notes this OT result holds 'pending a simple condition on the matching cost'); the paper generalizes this to optimal transport targets with m weighted points.([Abstract, p.1](https://arxiv.org/pdf/1905.11885v2#page=1 "Our proxy builds upon the fact that sorting can be seen as an optimal assignment problem, one in which the n values to be sorted are matched to an auxiliary probability measure supported on any increasing family of n target values."))
- **c3** Relaxation and cost: the OT problem is entropically regularized and solved by Sinkhorn iterations at O(nm l) operations, l being the number of iterations to converge (the paper adds that m can be as small as 3 in some applications and l rarely exceeds 100 in its settings).([Introduction, p.2](https://arxiv.org/pdf/1905.11885v2#page=2 "To recover tractable and differentiable operators, we regularize the OT problem and solve it using the Sinkhorn algorithm [10], at a cost of O(nmℓ) operations, where ℓis the number of Sinkhorn iterations needed for the algorithm to converge."))
- **c4** Approximation trade-off: smaller regularization epsilon brings the outputs closer to the true ranks and sorted values (larger epsilon collapses them toward averages); the authors caution that very small epsilon brings back the differentiability problems of hard sorting.([The Sinkhorn Ranking and Sorting Operators, p.5](https://arxiv.org/pdf/1905.11885v2#page=5 "the smaller ε is, the closer the Sinkhorn operator’s output is to the original vectors of ranks and sorted values"))
- **c5** Evaluation protocol for top-k (k = 1) classification on CIFAR-10/CIFAR-100 with a vanilla CNN and ResNet18: fixed epsilon and tolerance, squared-distance cost, Adam with step 1e-4; the comparison is against cross-entropy (Figures 4-5, 12 runs).([Learning with Smoothed Ranks and Sorts, p.8](https://arxiv.org/pdf/1905.11885v2#page=8 "We used ε = 10−3, η = 10−3, a squared distance cost h(u) = u2 and a stepsize of 10−4 with the ADAM optimizer."))
- **c6** Comparison with NeuralSort on its large-MNIST sorting benchmark (same network architecture, the NeuralSort authors' code, 100 epochs, epsilon = 0.005, Table 1 averaged over 10 runs): the table caption states the OT method performs better than NeuralSort for all sorting tasks, while the running text says it performs on par.([Learning with Smoothed Ranks and Sorts (Table 1), p.8](https://arxiv.org/pdf/1905.11885v2#page=8 "Our method performs better than the method presented in [18] for all the sorting tasks, with the exact same network architecture."))
- **c7** Least quantile regression: the soft quantile operator gives overall better quantile errors on the training set (the stated main goal) but comparable test/MSE errors; the caption hedges that the training gain may be due to a smoothed optimization landscape.([Learning with Smoothed Ranks and Sorts, p.9](https://arxiv.org/pdf/1905.11885v2#page=9 "We notice that our algorithm reaches overall better quantile errors on the training set—this is our main goal—but comparable test/MSE errors."))

