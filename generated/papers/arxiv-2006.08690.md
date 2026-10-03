<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Generalized and Scalable Optimal Sparse Decision Trees

- カード: [`arxiv-2006.08690`](../../papers/arxiv-2006.08690.yaml)
- 著者: Jimmy Lin, Chudi Zhong, Diane Hu, Cynthia Rudin, Margo Seltzer
- 年・掲載: 2020
- 原論文: [PDF](https://arxiv.org/pdf/2006.08690v4)(arXiv v4、カード作成時に読んだ版)
- タグ: decision-trees, interpretable-models, supervised, tabular-classification
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Motivation: new optimal-tree techniques could allow sparse trees to be built for various objectives without the greedy splitting and pruning heuristics that, in the authors' words, often lead to suboptimal solutions.([Abstract, p.1](https://arxiv.org/pdf/2006.08690v4#page=1 "without relying on greedy splitting and pruning heuristics that often lead to suboptimal solutions."))
- **c2** Theory cited from prior work (Laurent & Rivest, 1976): full decision tree optimization is NP-hard with no polynomial-time approximation, which makes proving optimality or bounding the optimality gap hard even for small datasets.([Introduction, p.1](https://arxiv.org/pdf/2006.08690v4#page=1 "Full decision tree optimization is NP-hard, with no polynomial-time approximation (Laurent & Rivest, 1976), leading to challenges in proving optimality or bounding the optimality gap in a reasonable amount of time, even for small datasets."))
- **c3** Optimization approach: for additive loss functions GOSDT uses dynamic programming with bounds (DPB); non-additive losses use PyGOSDT, a variant closer to OSDT's branch and bound.([GOSDT's DPB Algorithm, p.5](https://arxiv.org/pdf/2006.08690v4#page=5 "For optimizing additive loss functions we use GOSDT which uses dynamic programming with bounds (DPB) to provides a dramatic run time improvement."))
- **c4** Critique of other optimal-tree methods: the 'bucketization' preprocessing used by DL8.5 and BinOCT to handle continuous variables is proven (by construction) to possibly lower the maximum attainable training accuracy.([Section 3, p.4](https://arxiv.org/pdf/2006.08690v4#page=4 "The maximum training accuracy for a decision tree on a dataset preprocessed with bucketization can be lower (worse) than the maximum accuracy for the same dataset without bucketization."))
- **c5** Baseline role of greedy CART: CART (scikit-learn, with depth and leaf count constrained to vary tree size) is run as a reference for what a greedy algorithm without optimality guarantee achieves.([Appendix I, p.30](https://arxiv.org/pdf/2006.08690v4#page=30 "We run CART as a reference point for what is achievable with a greedy algorithm that makes no optimality guarantee."))
- **c6** Protocol: a 5-minute time limit is used on all experiments unless otherwise stated (30 minutes for the rank-statistic experiments), and multi-threaded algorithms are run sequentially.([Appendix I, p.31](https://arxiv.org/pdf/2006.08690v4#page=31 "We set a 5-minute time limit on all experiments, unless otherwise stated."))
- **c7** Limitation (scalability): GOSDT is stated to be most effective for datasets with a small or medium number of features, while scaling well in the number of observations (tens of thousands).([Discussion and Future Work, p.9](https://arxiv.org/pdf/2006.08690v4#page=9 "GOSDT is most effective for datasets with a small or medium number of features."))

