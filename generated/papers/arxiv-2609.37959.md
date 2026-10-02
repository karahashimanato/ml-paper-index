<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# TabFM: A Zero-Shot Foundation Model for Tabular Data

- カード: [`arxiv-2609.37959`](../../papers/arxiv-2609.37959.yaml)
- 著者: Weihao Kong, Erez Louidor Ilan, Shuxin Nie, Taman Narayan, Rajat Sen, Yichen Zhou, Deqing Fu, Samet Oymak, Abhimanyu Das
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.37959v1)(arXiv v1、カード作成時に読んだ版)
- タグ: in-context-learning, tabular-attention, tabular-classification, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** TabFM is a 400M-parameter tabular foundation model that casts supervised tabular prediction as in-context learning.([Abstract, p.1](https://arxiv.org/pdf/2609.37959v1#page=1 "We present TabFM, a 400M-parameter tabular foundation model that formulates supervised tabular prediction as in-context learning."))
- **c2** TabFM is trained only on synthetic tables generated from structural causal models and is applied zero-shot to real tasks.([Abstract, p.1](https://arxiv.org/pdf/2609.37959v1#page=1 "Trained entirely on synthetic tables generated from structural causal models, TabFM learns general tabular representations that transfer zero-shot to real-world tasks."))
- **c3** On all 51 TabArena datasets, zero-shot TabFM ranks first among default tabular foundation models and outperforms tuned AutoML pipelines.([Abstract, p.1](https://arxiv.org/pdf/2609.37959v1#page=1 "Across all 51 benchmark datasets in TabArena (38 classification and 13 regression), zero-shot TabFM ranks first among default tabular foundation models and outperforms tuned AutoML pipelines."))
- **c4** The TabArena comparison pool has 67 method configurations: tuned tree ensembles, tuned deep baselines, AutoML systems with four-hour budgets, and published tabular foundation models.([Experimental setup, p.7](https://arxiv.org/pdf/2609.37959v1#page=7 "The comparison pool holds 67 method configurations including tuned tree ensembles, tuned deep baselines, AutoML systems at four-hour budgets, and published tabular foundation models."))
- **c5** For TabFM-Auto, each candidate program is scored by three-fold cross-validation inside the training split of the first fold; the selected program is then refit on every published fold.([TabFM-Auto, p.10](https://arxiv.org/pdf/2609.37959v1#page=10 "Each candidate program is scored by three-fold cross-validation inside the training split of the first fold with 8 ensemble members, and its score, its per-fold values, and any traceback are appended to a log that is read before the next edit."))
- **c6** Pretraining covers tables of at most 16,384 rows and 100 columns; larger tables rely on length generalization or subsampling, and free text is encoded without semantic tokenization.([Conclusion, p.11](https://arxiv.org/pdf/2609.37959v1#page=11 "Current pretraining covers synthetic numerical and categorical tables of at most 16,384 rows and 100 columns, leaving larger tables to length generalization or subsampling and encoding free text without semantic tokenization."))

