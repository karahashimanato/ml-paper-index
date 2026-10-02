<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Foundation Models Meet Agriculture: Challenges Beyond Pretraining

- カード: [`arxiv-2608.30392`](../../papers/arxiv-2608.30392.yaml)
- 著者: Vishal Nedungadi, Xingguo Xiong, Marc Rußwurm, Ioannis N. Athanasiadis
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.30392v1)(arXiv v1、カード作成時に読んだ版)
- タグ: deep-learning, in-context-learning, random-forests, supervised, tabular-classification, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Agricultural tasks often need non-imagery modalities that EO foundation models cannot ingest, while a tabular foundation model handles this heterogeneity more naturally.([Abstract, p.1](https://arxiv.org/pdf/2608.30392v1#page=1 "agricultural downstream tasks frequently require diverse, non-imagery data modalities that earth observation foundation models are architecturally unequipped to ingest, while a foundation model built for tabular data handles this heterogeneity more naturally"))
- **c2** TabPFN, without geospatial or agricultural pretraining, matches or outperforms the foundation models across several datasets.([Results, p.6](https://arxiv.org/pdf/2608.30392v1#page=6 "We find that it matches or outperforms FMs across several datasets."))
- **c3** A standardized set of hyperparameters is used across datasets instead of per-dataset optimization, because labels are limited on several datasets and the goal is robustness rather than best achievable performance.([Hyperparameter Policy, p.5](https://arxiv.org/pdf/2608.30392v1#page=5 "We adopt a standardized set of hyperparameters across datasets."))
- **c4** The Random Forest uses 500 trees with default settings for all other hyperparameters.([Model Configurations, p.5](https://arxiv.org/pdf/2608.30392v1#page=5 "The Random Forest classifier/regressor is trained with 500 trees using the default settings for all remaining hyperparameters."))
- **c5** CY-Bench yield prediction uses chronological walk-forward validation on the final five years.([Evaluation Splits, p.3](https://arxiv.org/pdf/2608.30392v1#page=3 "Finally, to simulate operational forecasting for CY-Bench, we employ a chronological walk-forward validation strategy on the final 5 years."))
- **c6** Stated limitation: the baselines are traditional, simple methods rather than complex domain-specific models.([Limitations, p.8](https://arxiv.org/pdf/2608.30392v1#page=8 "Thirdly, the study utilizes traditional, simple methods as baselines, whereas a large body of literature exists detailing complex, domain-specific models designed for each individual task."))

