<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# XGBoost: A Scalable Tree Boosting System

- カード: [`arxiv-1603.02754`](../../papers/arxiv-1603.02754.yaml)
- 著者: Tianqi Chen, Carlos Guestrin
- 年・掲載: 2016 KDD 2016
- 原論文: [PDF](https://arxiv.org/pdf/1603.02754v3)(arXiv v3、カード作成時に読んだ版)
- タグ: gradient-boosted-trees, supervised, tabular-classification
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Contributions stated in the abstract: a sparsity-aware algorithm for sparse data and a weighted quantile sketch for approximate tree learning, plus insights on cache access patterns, data compression and sharding for a scalable system.([Abstract, p.1](https://arxiv.org/pdf/1603.02754v3#page=1 "We propose a novel sparsity-aware algorithm for sparse data and weighted quantile sketch for approximate tree learning."))
- **c2** Regularized objective: a complexity penalty (gamma times the number of leaves plus an L2 penalty on leaf weights) is added to the loss to smooth the learnt weights and avoid over-fitting; with the regularization parameter set to zero the objective falls back to traditional gradient tree boosting. The authors describe the objective as a minor improvement included for completeness, resembling Regularized Greedy Forest but simpler and easier to parallelize.([Regularized Learning Objective, p.2](https://arxiv.org/pdf/1603.02754v3#page=2 "When the regularization parameter is set to zero, the objective falls back to the traditional gradient tree boosting."))
- **c3** Citing Friedman et al. [12], the tree is fitted with a second-order (gradient and Hessian) approximation of the loss; the authors state the derivation follows existing gradient boosting literature.([Gradient Tree Boosting, p.2](https://arxiv.org/pdf/1603.02754v3#page=2 "Second-order approximation can be used to quickly optimize the objective in the general setting [12]."))
- **c4** Besides shrinkage, column (feature) subsampling is used against over-fitting; the authors report, based on user feedback, that it prevents over-fitting even more than traditional row subsampling (which is also supported), and that it speeds up the parallel algorithm.([Shrinkage and Column Subsampling, p.3](https://arxiv.org/pdf/1603.02754v3#page=3 "According to user feedback, using column sub-sampling prevents over-ﬁtting even more so than the traditional row sub-sampling (which is also supported)."))
- **c5** Split finding: the exact greedy algorithm enumerates all splits on pre-sorted features; the approximate algorithm proposes candidate splits from feature percentiles either once per tree (global) or after each split (local). In the Higgs 10M comparison (shown as a figure), the authors find the local proposal needs fewer candidates and the global one can be as accurate given enough candidates.([Approximate Algorithm, p.4](https://arxiv.org/pdf/1603.02754v3#page=4 "The global proposal can be as accurate as the local one given enough candidates."))
- **c6** Sparsity-aware split finding learns, for each node, a default direction for missing entries from the data, and only visits non-missing entries so that cost is linear in their number; on Allstate-10K (sparse mainly due to one-hot encoding) it ran 50 times faster than a naive implementation.([Sparsity-aware Split Finding, p.5](https://arxiv.org/pdf/1603.02754v3#page=5 "We ﬁnd that the sparsity aware algorithm runs 50 times faster than the naive version."))
- **c7** Evaluation protocol: four datasets (Allstate, Higgs Boson, Yahoo LTRC, Criteo); all experiments use a common setting of maximum depth 8 and shrinkage 0.1 with no column subsampling unless specified. No per-library hyperparameter tuning procedure was found in the text (searched for tun, hyperparameter, grid, default).([Dataset and Setup, p.8](https://arxiv.org/pdf/1603.02754v3#page=8 "In all the experiments, we boost trees with a common setting of maximum depth equals 8, shrinkage equals 0.1 and no column subsampling unless explicitly speciﬁed."))
- **c8** Single-machine exact greedy comparison on dense Higgs-1M (chosen because scikit-learn only handles non-sparse input; 1M subset so scikit-learn finishes in reasonable time): both XGBoost and scikit-learn performed better than R's GBM (which expands only one branch of a tree), and XGBoost ran more than 10x faster than scikit-learn. Column subsampling gave slightly worse performance here, which the authors say could be due to few important features.([Classification, p.8](https://arxiv.org/pdf/1603.02754v3#page=8 "Both XGBoost and scikit-learn give better performance than R’s GBM, while XGBoost runs more than 10x faster than scikit-learn."))

