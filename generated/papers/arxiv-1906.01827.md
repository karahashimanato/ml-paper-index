<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Coresets for Data-efficient Training of Machine Learning Models

- カード: [`arxiv-1906.01827`](../../papers/arxiv-1906.01827.yaml)
- 著者: Baharan Mirzasoleiman, Jeff Bilmes, Jure Leskovec
- 年・掲載: 2019
- 原論文: [PDF](https://arxiv.org/pdf/1906.01827v3)(arXiv v3、カード作成時に読んだ版)
- タグ: data-subset-selection, deep-learning, greedy-methods, image-classification, linear-models, supervised, tabular-classification
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Contribution: CRAIG selects a weighted training subset (coreset) that closely estimates the full gradient, found by maximizing a submodular function.([Abstract, p.1](https://arxiv.org/pdf/1906.01827v3#page=1 "Here we develop CRAIG, a method to select a weighted subset (or coreset) of training data that closely estimates the full gradient by maximizing a submodular function."))
- **c2** Greedy guarantee (classical greedy results applied, not new theory): the subset problem is NP-hard; turned into a monotone submodular facility-location surrogate F, the budgeted version (|S| <= r) is approximated by greedy within (1-1/e) of the optimal F value, and the cover version gets a logarithmic approximation on subset size (Wolsey 1982). The approximation is for the surrogate (an upper bound on gradient-estimation error), not directly for the gradient error.([CRAIG with Limited Budget, p.5](https://arxiv.org/pdf/1906.01827v3#page=5 "For the above submodular maximization problem, the greedy algorithm discussed in Section 3.2 provides a (1 − 1/e)-approximation to the optimal solution."))
- **c3** Convergence guarantee and its assumptions: IG on the subset is proved to converge to a (near)optimal solution at the same rate as IG for convex optimization (Theorems 1-2 assume a strongly convex f and a subset whose weighted gradient is within epsilon of the full gradient over the parameter domain; Theorem 2 additionally assumes convex, twice-differentiable components with Lipschitz gradients; both leave an extra epsilon-dependent error term).([Abstract, p.1](https://arxiv.org/pdf/1906.01827v3#page=1 "We prove that applying IG to this subset is guaranteed to converge to the (near)optimal solution with the same convergence rate as that of IG for convex optimization."))
- **c4** Main empirical claim: while reaching practically the same solution, CRAIG speeds up various IG methods by up to 6x for logistic regression and 3x for deep neural networks.([Abstract, p.1](https://arxiv.org/pdf/1906.01827v3#page=1 "Our extensive set of experiments show that CRAIG, while achieving practically the same solution, speeds up various IG methods by up to 6x for logistic regression and 3x for training deep neural networks"))
- **c5** Speedup measurement: run time is wall-clock time for CRAIG's subset selection plus loss minimization with IG or other optimizers.([Experiments, p.7](https://arxiv.org/pdf/1906.01827v3#page=7 "In our experiments, we report the run-time as the wall-clock time for subset selection with CRAIG, plus minimizing the loss using IG or other optimizers with the specified learning rates."))
- **c6** Tuning: each method is tuned separately to perform at its best (for the convex experiments, learning rates for each method including the random baseline were tuned by preferring smaller training loss).([Experiments, p.7](https://arxiv.org/pdf/1906.01827v3#page=7 "We separately tune each method so that it performs at its best."))
- **c7** Limitation for deep networks: the gradient-difference bound depends on the changing parameters, so the subset must be reselected after a number of parameter updates rather than once as preprocessing.([Application of CRAIG to Deep Networks, p.5](https://arxiv.org/pdf/1906.01827v3#page=5 "Thus, we need to use CRAIG to update the subset S after a number of parameter updates."))

