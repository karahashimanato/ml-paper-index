<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Learning the Travelling Salesperson Problem Requires Rethinking Generalization

- カード: [`arxiv-2006.07054`](../../papers/arxiv-2006.07054.yaml)
- 著者: Chaitanya K. Joshi, Quentin Cappart, Louis-Martin Rousseau, Thomas Laurent
- 年・掲載: 2020
- 原論文: [PDF](https://arxiv.org/pdf/2006.07054v6)(arXiv v6、カード作成時に読んだ版)
- タグ: combinatorial-optimization, deep-learning, graph-neural-networks, reinforcement-learning, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Main claim: learning-driven TSP approaches perform close to classical solvers when trained on trivially small sizes but cannot generalize the learnt policy to larger instances at practical scales.([Abstract, p.1](https://arxiv.org/pdf/2006.07054v6#page=1 "While state-of-the-art learning-driven approaches for TSP perform closely to classical solvers when trained on trivially small sizes, they are unable to generalize the learnt policy to larger instances at practical scales."))
- **c2** Protocol (training): ablations train on variable-size TSP20-50 (compared with fixed sizes up to TSP100); nodes uniform in the unit square; SL uses 1,280,000 instances with Concorde tours as labels for 10 epochs, RL uses 128,000 freshly generated unlabelled instances per epoch for 100 epochs, so both see 12,800,000 samples in total; models have approximately 350,000 parameters.([Experimental setup, p.7](https://arxiv.org/pdf/2006.07054v6#page=7 "We perform ablation studies of each component of the pipeline by training on variable TSP20-50 graphs for rapid experimentation."))
- **c3** Protocol (evaluation): test set of 1,280 instances for each size TSP10 to TSP200, metric is optimality gap w.r.t. Concorde, beam search width 128; a non-learnt furthest insertion heuristic is used as the reference for 'good' generalization.([Experimental setup, p.7](https://arxiv.org/pdf/2006.07054v6#page=7 "We compare models on a held-out test set of 25,600 TSPs, consisting of 1,280 samples each of TSP10, TSP20, . . . , TSP200."))
- **c4** Critique of evaluation practice: the authors state that the prevalent paradigm of measuring on fixed or trivially small sizes hides poor generalization.([Introduction, p.2](https://arxiv.org/pdf/2006.07054v6#page=2 "The prevalent evaluation paradigm overshadows models’ poor generalization capabilities by measuring performance on ﬁxed or trivially small TSP sizes."))
- **c5** Train/test size result: variable-size training helps within the training range but does not improve generalization to larger problems over training on TSP50; TSP20-trained models fail to generalize to large sizes and TSP100-trained models do poorly on small sizes, which the authors take as evidence that evaluation on training sizes (citing Kool et al. and Joshi et al.) hides brittle out-of-distribution performance.([Results, p.7](https://arxiv.org/pdf/2006.07054v6#page=7 "Learning from small TSP20 is unable to generalize to large sizes while TSP100 models generalize poorly to trivially easy sizes, suggesting that the prevalent protocol of evaluation on training sizes [42, 37] overshadows brittle out-of-distribution performance."))
- **c6** Classical baseline (Figure 1 setting: three identical autoregressive GNN models trained via RL on 12.8 million instances - from scratch on TSP200, on TSP20-50 zero-shot, and pretrained then fine-tuned on 1.28 million TSP200 - plus Active Search, evaluated on 1,280 held-out TSP200 instances): within the authors' computational budget a simple non-learnt furthest insertion heuristic still outperforms all models.([Introduction, p.2](https://arxiv.org/pdf/2006.07054v6#page=2 "Within our computational budget, a simple non-learnt furthest insertion heuristic still outperforms all models."))
- **c7** Recommendation: GNN layers, normalization schemes, graph sparsification and learning paradigms need to be explicitly re-designed with out-of-distribution generalization in mind; the authors advocate training on small instances and transferring zero-shot or via fast fine-tuning rather than expensive large-scale training.([Conclusion, p.12](https://arxiv.org/pdf/2006.07054v6#page=12 "Our ﬁndings suggest that key design choices such as GNN layers, normalization schemes, graph sparsiﬁcation, and learning paradigms need to be explicitly re-designed to consider out-of-distribution generalization."))

