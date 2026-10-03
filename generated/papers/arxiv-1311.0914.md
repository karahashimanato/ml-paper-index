<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# A Divide-and-Conquer Solver for Kernel Support Vector Machines

- カード: [`arxiv-1311.0914`](../../papers/arxiv-1311.0914.yaml)
- 著者: Cho-Jui Hsieh, Si Si, Inderjit S. Dhillon
- 年・掲載: 2013
- 原論文: [PDF](https://arxiv.org/pdf/1311.0914v1)(arXiv v1、カード作成時に読んだ版)
- タグ: divide-and-conquer, image-classification, kernel-methods, supervised, tabular-classification
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Partition scheme and its justification: the paper shows that kernel k-means clustering minimizes the difference between the subproblem solution and the whole-problem solution, and that support vectors found in the subproblems are very likely to be support vectors of the whole problem.([Introduction, p.1](https://arxiv.org/pdf/1311.0914v1#page=1 "We theoretically show that the kernel kmeans algorithm is able to minimize the diﬀerence between the solution of subproblems and of the whole problem, and support vectors identiﬁed by subproblems are very likely to be support vectors of the whole problem."))
- **c2** Conquer step: the local subproblem solutions are not just combined but used to initialize a global coordinate descent solver on the full problem, which the analysis suggests converges quickly from that start.([Abstract, p.1](https://arxiv.org/pdf/1311.0914v1#page=1 "In the conquer step, the local solutions from the subproblems are used to initialize a global coordinate descent solver, which converges quickly as suggested by our analysis."))
- **c3** Exactness (top level only): the authors state that, unlike model-combination approaches such as BCM, DC-SVM solves the original SVM problem, not just an approximated one; this holds when the global coordinate descent is run at the top level on the whole problem, not for the DC-SVM (early) prediction mode, which uses the lower-level (approximate-kernel) models.([Related Work, p.2](https://arxiv.org/pdf/1311.0914v1#page=2 "More importantly, DC-SVM solves the original SVM problem, not just an approximated one."))
- **c4** Assumption behind the guarantee: the approximation bound (Theorem 1) depends on D(pi), the sum of absolute between-cluster kernel values, which is strongly related to the kernel parameters (for the RBF kernel, small gamma makes D(pi) larger and the subproblem solution may not be close to the optimum).([Experimental Results, p.12](https://arxiv.org/pdf/1311.0914v1#page=12 "As shown in Theorem 1 the quality of approximation depends on D(π), which is strongly related to the kernel parameters."))
- **c5** What is traded for speed in early prediction: DC-SVM (early) stops at a lower level and classifies a test point with the model trained on its nearest cluster only, i.e. it uses the block-diagonal approximate kernel instead of the exact SVM solution.([Divide and Conquer SVM with multiple levels, p.8](https://arxiv.org/pdf/1311.0914v1#page=8 "Therefore, the testing procedure for early prediction is: (1) ﬁnd the nearest cluster that x belongs to, and then (2) use the model trained by data within that cluster to compute the decision value."))
- **c6** Main empirical claim: DC-SVM reduces the SVM objective faster than state-of-the-art exact SVM solvers (relative error measured against LIBSVM run to 1e-8 accuracy); online and approximate solvers are excluded from this objective comparison because they do not solve the exact problem.([Experimental Results, p.12](https://arxiv.org/pdf/1311.0914v1#page=12 "We observe that DC-SVM achieves faster convergence in objective function compared with the state-of-the-art exact SVM solvers."))
- **c7** Protocol: C and the kernel parameter gamma are chosen by 5-fold cross-validation on a grid (2^-10..2^10 for most datasets; smaller gammas for the unscaled image datasets cifar and mnist8m).([Experimental Results, p.10](https://arxiv.org/pdf/1311.0914v1#page=10 "We chose the balancing parameter C and kernel parameter γ by 5-fold cross validation on a grid of points"))

