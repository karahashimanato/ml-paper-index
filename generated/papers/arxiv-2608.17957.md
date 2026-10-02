<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Understanding the Surprising Generalization Properties of Tabular Foundation Models

- カード: [`arxiv-2608.17957`](../../papers/arxiv-2608.17957.yaml)
- 著者: Nour Shaheen, Junwei Ma, Alex Labach, Frank Hutter, Valentin Thomas, Anthony L. Caterini
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.17957v1)(arXiv v1、カード作成時に読んだ版)
- タグ: in-context-learning, self-supervised, tabular-classification, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Surprisingly strong transfer can emerge from self-supervised pre-training on a single real table.([Abstract, p.1](https://arxiv.org/pdf/2608.17957v1#page=1 "In contrast, we show that surprisingly strong transfer can emerge from self-supervised pre-training on just a single real table."))
- **c2** Fine-grained column-level pre-processing consistently improves downstream performance, while dataset-level filtering or deduplication does not.([Abstract, p.1](https://arxiv.org/pdf/2608.17957v1#page=1 "fine-grained column-level pre-processing consistently improves downstream performance, while no improvements are observed when we filter or deduplicate at the dataset level."))
- **c3** Single-table models are evaluated on the 72 OpenML CC-18 classification and 35 CTR-23 regression datasets, with no overlap between pre-training and evaluation.([Generalization from single table training, p.3](https://arxiv.org/pdf/2608.17957v1#page=3 "the 72 CC-18 [3] classification datasets and 35 CTR-23 [9] regression datasets."))
- **c4** Linear and random-forest baselines use scikit-learn defaults; XGBoost is the tuned baseline taken from McElfresh et al.; TabDPT is run from its public repository.([Generalization from single table training, p.3](https://arxiv.org/pdf/2608.17957v1#page=3 "XGBoost is the tuned baseline from McElfresh et al. [23], and TabDPT is computed from the public repository (Version 1.1, Apache-2.0 license)."))
- **c5** The large-corpus models are placed on the TabArena leaderboard against default-configuration baselines.([Corpus experiments, p.6](https://arxiv.org/pdf/2608.17957v1#page=6 "We contextualize these findings within the broader TabArena leaderboard in Figure 5, reporting Elo against some other default-configuration baselines, with details in Appendix C."))
- **c6** Several authors also authored TabDPT (reference list), whose architecture and pre-training procedure the study reuses; affiliations include Layer 6 AI and Prior Labs.([References, p.12](https://arxiv.org/pdf/2608.17957v1#page=12 "[22] Junwei Ma, Valentin Thomas, Rasa Hosseinzadeh, Hamidreza Kamkari, Alex Labach, Jesse C."))

