<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Optimal Sparse Decision Trees

- カード: [`arxiv-1904.12847`](../../papers/arxiv-1904.12847.yaml)
- 著者: Xiyang Hu, Cynthia Rudin, Margo Seltzer
- 年・掲載: 2019
- 原論文: [PDF](https://arxiv.org/pdf/1904.12847v6)(arXiv v6、カード作成時に読んだ版)
- タグ: decision-trees, interpretable-models, supervised, tabular-classification
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Critique of greedy induction: CART and C4.5 grow trees top-down without backtracking, so if a suboptimal split is introduced near the top the algorithm could spend many extra splits trying to undo it, leading to less accurate and less interpretable trees.([Introduction, p.1](https://arxiv.org/pdf/1904.12847v6#page=1 "CART and C4.5 grow decision trees from the top down without backtracking, which means that if a suboptimal split was introduced near the top of the tree, the algorithm could spend many extra splits trying to undo the mistake it made at the top, leading to less-accurate and less-interpretable trees."))
- **c2** Contribution: the paper presents what it calls the first practical algorithm for optimal decision trees, restricted to binary variables.([Abstract, p.1](https://arxiv.org/pdf/1904.12847v6#page=1 "This work introduces the first practical algorithm for optimal decision trees for binary variables."))
- **c3** Objective: optimal trees are defined by a regularized loss that trades off accuracy against the number of leaves (misclassification error plus lambda times the number of leaves), rather than a fixed tree topology.([Introduction, p.2](https://arxiv.org/pdf/1904.12847v6#page=2 "We find optimal trees according to a regularized loss function that balances accuracy and the number of leaves."))
- **c4** Optimization approach: the objective is minimized with branch and bound, using a series of specialized bounds that eliminate a large part of the search space (the hierarchical objective lower bound and the equivalent points bound adapted directly from CORELS, several others adapted from CORELS with minor changes; proofs in the supplement).([Optimization Framework, p.4](https://arxiv.org/pdf/1904.12847v6#page=4 "We minimize the objective function based on a branch-and-bound framework."))
- **c5** Protocol: OSDT is compared against CART and BinOCT on 7 datasets (5 UCI datasets plus ProPublica COMPAS and FICO); both BinOCT and OSDT get a 30-minute time limit.([Experiments, p.7](https://arxiv.org/pdf/1904.12847v6#page=7 "The time limits for both BinOCT and our algorithm are set to be 30 minutes."))
- **c6** Finding on baselines (training accuracy, Figure 1): with provably optimal trees as reference, the authors state that other methods are often close to optimal or optimal, though sometimes the baselines are not optimal.([Experiments, p.7](https://arxiv.org/pdf/1904.12847v6#page=7 "(i) We can now evaluate how close to optimal other methods are (and they are often close to optimal or optimal)."))
- **c7** Limitation (scalability): runtime can in theory grow exponentially with the number of features (the authors add that, empirically, extra features not in the optimal tree let the search prune faster).([Experiments, p.7](https://arxiv.org/pdf/1904.12847v6#page=7 "Runtime can theoretically grow exponentially with the number of features."))

