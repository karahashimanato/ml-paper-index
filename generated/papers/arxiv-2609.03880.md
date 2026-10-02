<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Xiaomi-TabLDM: A Tabular Foundation Model Technical Report

- カード: [`arxiv-2609.03880`](../../papers/arxiv-2609.03880.yaml)
- 著者: Xiaomi-TabLDM Team, Penghui Wang, Wei Liu, Hong Wang, Chengyue Huang, Yuxi Sun, Zirui Wang, Hongming Huang, Quan Wang, Zhenwei Xin, Ping Hou, Jie Yu, Chunxiao Liu, Erli Meng, Bin Wang
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.03880v2)(arXiv v2、カード作成時に読んだ版)
- タグ: in-context-learning, tabular-attention, tabular-classification, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Xiaomi-TabLDM is a tabular foundation model for classification and regression via in-context learning, without task-specific fine-tuning.([Abstract, p.1](https://arxiv.org/pdf/2609.03880v2#page=1 "We introduce Xiaomi-TabLDM, a tabular large data foundation model for classification and regression via in-context learning, which delivers superior prediction accuracy without requiring task-specific fine-tuning."))
- **c2** Its strongest results are on regression: first on OpenML-CTR23 and second on regression across TALENT, TabArena and BCCO.([Introduction, p.3](https://arxiv.org/pdf/2609.03880v2#page=3 "Its strongest and most consistent results are observed on regression: Xiaomi-TabLDM ranks first on OpenML-CTR23 and second on regression across TALENT, TabArena, and BCCO."))
- **c3** Most benchmark datasets have fewer than 10K training examples, a smaller portion 10K-100K, and only TALENT includes some with more than 100K.([Evaluation, p.9](https://arxiv.org/pdf/2609.03880v2#page=9 "Across these benchmarks, most datasets contain fewer than 10K training examples, with a smaller portion ranging from 10K to 100K; TALENT additionally includes several datasets with more than 100K training instances."))
- **c4** On TALENT, missing results of some methods on a subset of datasets are imputed with K-nearest-neighbour values.([Evaluation (TALENT figure caption), p.10](https://arxiv.org/pdf/2609.03880v2#page=10 "For methods with missing results on a subset of datasets, the corresponding score entries are imputed using K-nearest-neighbour values following the evaluation protocol."))
- **c5** BCCO excludes datasets with more than 50,000 training samples, 10,000 features, or 10 target classes.([Evaluation (BCCO), p.13](https://arxiv.org/pdf/2609.03880v2#page=13 "The benchmark excludes extremely large datasets with more than 50,000 training samples, 10,000 features, or 10 target classes."))
- **c6** OpenML-CTR23 results are reported on 33 datasets of the original 35-problem suite; no reason for the reduction was found in the text.([Evaluation (OpenML-CTR23), p.15](https://arxiv.org/pdf/2609.03880v2#page=15 "In our experiments, we report results on 33 datasets and compare Xiaomi-TabLDM against both tabular foundation models and conventional learning baselines."))

