<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# InRTL: Effective Intra-Inter Interaction Learning for Relational Tables

- カード: [`arxiv-2609.12712`](../../papers/arxiv-2609.12712.yaml)
- 著者: Weichen Li, Ken Zhong, Zheng Wang, Li Pan, Jianhua Li
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.12712v1)(arXiv v1、カード作成時に読んだ版)
- タグ: graph-neural-networks, supervised, tabular-attention, tabular-classification, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** InRTL is a unified framework that explicitly models dependencies within and across relational tables.([Abstract, p.1](https://arxiv.org/pdf/2609.12712v1#page=1 "In this paper, we propose Intra–Inter Relational Table Learning (InRTL), a unified framework that explicitly models dependencies both within and across relational tables."))
- **c2** Experiments are reported to show that InRTL consistently outperforms state-of-the-art baselines on diverse relational table tasks.([Conclusion, p.9](https://arxiv.org/pdf/2609.12712v1#page=9 "Extensive experiments demonstrate that InRTL consistently outperforms state-of-the-art baselines on diverse relational table tasks."))
- **c3** All experiments follow the standard preprocessing and train/val/test splits of each benchmark (SJTUTables and RelBench).([Experimental setup, p.6](https://arxiv.org/pdf/2609.12712v1#page=6 "Additionally, for all experiments, we follow the standard data preprocessing and train/val/test split provided by each benchmark."))
- **c4** All baselines were re-implemented from official code or the original papers and tuned by grid search over key hyperparameters.([Appendix, p.12](https://arxiv.org/pdf/2609.12712v1#page=12 "To ensure fairness, we re-implemented all baselines based on the official code or their original papers and performed a comprehensive grid search over key hyper-parameters (see Appendix C.5 for details)."))
- **c5** Hyperparameters of all models are selected on validation performance.([Appendix, p.12](https://arxiv.org/pdf/2609.12712v1#page=12 "We tune all model hyper-parameters based on validation performance."))
- **c6** The evaluation focuses mainly on well-curated relational databases with explicit table relationships.([Limitations, p.9](https://arxiv.org/pdf/2609.12712v1#page=9 "Our evaluation mainly focuses on well-curated relational databases with explicit table relationships."))

