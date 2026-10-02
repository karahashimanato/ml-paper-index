<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# TACTICL: Task-Aware Compression of Tabular ICL Models

- カード: [`arxiv-2608.10837`](../../papers/arxiv-2608.10837.yaml)
- 著者: Mykhailo Koshil, Matthias Feurer, Katharina Eggensperger
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.10837v1)(arXiv v1、カード作成時に読んだ版)
- タグ: in-context-learning, model-compression, pruning, supervised, tabular-classification, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** TACTICL jointly prunes transformer layers of a tabular ICL model and replaces them with lightweight adapters trained on the downstream task, blending in-context and in-weight learning.([Abstract, p.1](https://arxiv.org/pdf/2608.10837v1#page=1 "an automated task-aware compression framework for tabular in-context learning models that jointly prunes transformer layers and replaces them with lightweight adapters trained on downstream tasks, thus blending in-context with in-weight learning"))
- **c2** On 47 benchmark datasets, up to 85% of layers can be substituted without substantial performance drop on a given downstream task.([Abstract, p.1](https://arxiv.org/pdf/2608.10837v1#page=1 "We study TACTICL on 47 benchmark datasets and show that we can substitute up to 85% of layers without substantial performance drop on a given downstream task."))
- **c3** Evaluation uses 34 classification and 13 regression TabArena datasets: those within TabPFN v2.5's native limits (at most 50,000 training samples and 2,000 features); one fold for TabPFNv2 and three folds for TabPFNv2.5.([Appendix (Datasets), p.16](https://arxiv.org/pdf/2608.10837v1#page=16 "From TabArena’s datasets, we retain only those that fit within TabPFN v2.5’s native pretraining limits (at most 50,000 training samples and 2,000 features, checked against the actual per-fold training-split size)"))
- **c4** For TabPFNv2.5, the compressed model is compared with the full model and two simple baselines: dropping/substituting layers from last to first, and distilling the full model into a shallow MLP.([Experiments, p.8](https://arxiv.org/pdf/2608.10837v1#page=8 "First, substitution or dropping layers starting from the last to first; and second, we distill the full model into a shallow MLP (see Appendix F for further details)."))
- **c5** Layer-importance metrics commonly used in the literature fail to identify good compression configurations, and no single pruning configuration is universally optimal across datasets.([Conclusion, p.10](https://arxiv.org/pdf/2608.10837v1#page=10 "Notably, we find that layer-importance metrics commonly used in the literature fail to identify good compression configurations."))
- **c6** Limitations: no principled criterion for the compression/performance trade-off, and evaluation limited to tasks within TabPFNv2.5's pre-training constraints; the full TabArena benchmark is deferred.([Limitations, p.10](https://arxiv.org/pdf/2608.10837v1#page=10 "Moreover, our empirical evaluation is limited to tasks within the pre-training constraints of TabPFNv2.5."))

