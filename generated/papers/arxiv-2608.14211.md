<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Training Fair Tabular Foundation Models

- カード: [`arxiv-2608.14211`](../../papers/arxiv-2608.14211.yaml)
- 著者: Patrik Kenfack, Jesse C. Cresswell, Anthony L. Caterini, Samira Ebrahimi Kahou, Ulrich Aïvodji
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.14211v1)(arXiv v1、カード作成時に読んだ版)
- タグ: in-context-learning, tabular-classification, tabular-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** FairTFM is a training strategy for tabular foundation models that combines synthetic fairness tasks with a gradient-reversal architecture so that representations become invariant to sensitive attributes.([Abstract, p.1](https://arxiv.org/pdf/2608.14211v1#page=1 "We propose FairTFM, a scalable training strategy based on synthetic fairness tasks and a fairness-aware architecture using a gradient reversal layer, which encourages the model to learn representations invariant to sensitive attributes."))
- **c2** Across 132 fairness tasks, fairness improves consistently while accuracy stays competitive.([Abstract, p.1](https://arxiv.org/pdf/2608.14211v1#page=1 "Experiments on 132 fairness tasks show consistent improvements in fairness while maintaining competitive accuracy."))
- **c3** The main evaluation uses 120 fairness tasks built from the 2018 ACS surveys via the folktables library.([Experimental setup, p.5](https://arxiv.org/pdf/2608.14211v1#page=5 "We evaluate our model on 120 fairness tasks derived from the 2018 1-Year American Community Surveys [12], accessed through the folktables library, which is released under the MIT License."))
- **c4** The ACS task datasets range from roughly 3.5k to 12k samples and are evaluated with a single random 80/20 train-test split.([Appendix, p.15](https://arxiv.org/pdf/2608.14211v1#page=15 "Across all task instantiations, dataset sizes vary from roughly 3.5k to 12k samples, and we use a random 80/20 train–test split."))
- **c5** Classical baselines (LR, RF, XGBoost, KNN) are run in their default scikit-learn configuration.([Experimental setup, p.5](https://arxiv.org/pdf/2608.14211v1#page=5 "We compare our method against standard machine learning baselines, including logistic regression (LR), random forest (RF), XGBoost (XGB), and k-nearest neighbours (KNN) in their default scikit-learn configuration [32]."))
- **c6** Limitations: FairTFM does not dominate specialized fairness-aware baselines on every metric or task configuration, and the experiments use the lightweight nanoTabPFN backbone.([Limitations and future work, p.10](https://arxiv.org/pdf/2608.14211v1#page=10 "Second, while FairTFM is broadly competitive, the results also show that it does not dominate specialized fairness-aware baselines on every metric or every task configuration, especially in the stricter settings where age is used as sensitive attribute."))

