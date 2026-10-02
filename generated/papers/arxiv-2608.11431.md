<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# AutoGrable: What Is a Good Graph for a Table?

- カード: [`arxiv-2608.11431`](../../papers/arxiv-2608.11431.yaml)
- 著者: Tamara Cucumides, Floris Geerts
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.11431v1)(arXiv v1、カード作成時に読んだ版)
- タグ: graph-neural-networks, graph-node-prediction, supervised, tabular-classification
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The alignment score builds no graph and trains no GNN, so AutoGrable can greedily search column subsets for both single tables and foreign-key schemas.([Abstract, p.1](https://arxiv.org/pdf/2608.11431v1#page=1 "The score materialises no graph and trains no GNN, so AUTOGRABLE can search the space of subsets greedily and cheaply, and returns the resulting grable for single tables and for foreign-key schemas alike."))
- **c2** AutoGrable recovers label-generating columns on controlled tasks and outperforms fixed, random and task-aware constructors on real tasks under a fixed predictor.([Abstract, p.1](https://arxiv.org/pdf/2608.11431v1#page=1 "that AUTOGRABLE recovers the columns that generate the label on controlled tasks and outperforms fixed, random, and task-aware constructors on real tasks under a fixed predictor"))
- **c3** All constructions are evaluated with GraphSAGE using a fixed architecture, budget and hyperparameters within each regime, with no per-constructor tuning.([Experimental setup, p.7](https://arxiv.org/pdf/2608.11431v1#page=7 "We use GraphSAGE throughout, with fixed architecture, budget and hyperparameters within regime (see Appendix D.6.1) for every construction and every dataset, and no per-constructor tuning."))
- **c4** TabArena is used as a negative control, since on i.i.d. single-table data each label should depend only on its own row.([Experimental setup, p.7](https://arxiv.org/pdf/2608.11431v1#page=7 "Negative control: the i.i.d. single-table benchmark TabArena [15], where each label should depend only on its own row."))
- **c5** Only a subset of TabArena is used: datasets with more than 8 categorical features and a binary target.([Appendix, p.26](https://arxiv.org/pdf/2608.11431v1#page=26 "The datasets are selected for having more than 8 categorical features and a binary classification target."))
- **c6** The association between the score and downstream AUC is weaker on test than on validation, which the authors expect because the score is also computed on the validation split.([Results, p.8](https://arxiv.org/pdf/2608.11431v1#page=8 "The association is weaker on test than on validation, as expected since J is also computed on the validation split."))

