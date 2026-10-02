<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# ARASH: Adaptive Retrieval And Shot Selection for Tabular Prediction

- カード: [`arxiv-2608.17856`](../../papers/arxiv-2608.17856.yaml)
- 著者: Samirasadat Jamalidinan, Yue Xu, Kazem Cheshmi
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.17856v1)(arXiv v1、カード作成時に読んだ版)
- タグ: gradient-boosted-trees, in-context-learning, large-language-models, supervised, tabular-attention, tabular-classification, tabular-foundation-model, tabular-mlp
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** ARASH selects query-specific context shots for tabular foundation models from local-neighbourhood analysis of the training set.([Abstract, p.1](https://arxiv.org/pdf/2608.17856v1#page=1 "This paper introduces ARASH (Adaptive, query-specific Retrieval And Shot selection), a method that improves TFM efficiency by selecting optimal shots based on local neighborhood analysis within the training set."))
- **c2** ARASH reduces TabPFN's prompt length and memory use while giving comparable accuracy.([Abstract, p.1](https://arxiv.org/pdf/2608.17856v1#page=1 "Our results demonstrate that ARASH reduces the prompt length and memory usage of TabPFN by 1261.5× and 2.56×, respectively, while providing comparable accuracy."))
- **c3** Evaluation uses OpenML-CC18 plus the Combo collection, with a single 80/20 train-test split (seed 42) shared by all methods.([Experimental results (setup), p.5](https://arxiv.org/pdf/2608.17856v1#page=5 "For datasets, we use an 80/20 train–test split with random seed 42, and the same split is used consistently across all compared methods."))
- **c4** Tabular baselines come from the TALENT toolbox and its standardized implementations and hyperparameter settings. Results are reported only on datasets where each method ran successfully.([Experimental results (baselines), p.5](https://arxiv.org/pdf/2608.17856v1#page=5 "We use the latest TALENT release and report results on the datasets for which the corresponding methods are successfully executed."))
- **c5** ARASH's locality, purity and clustering thresholds are grid-searched on a held-out 10% of datasets that are not used in training, evaluation or test.([Experimental results (evaluation metrics), p.5](https://arxiv.org/pdf/2608.17856v1#page=5 "we define a tuning set as random 10% of datasets (seed=42) never appearing in training, evaluation, or test and perform a grid search for locality, purity, and auto-clustering thresholds to avoid bias."))
- **c6** The LoCalPFN-style comparison is reported only on datasets where both large-budget runs finished within the time limit.([Experimental results (ICL demonstration-selection baselines), p.6](https://arxiv.org/pdf/2608.17856v1#page=6 "We therefore report this comparison only on the datasets for which both LoCalPFN-style kNN and DPP runs completed successfully."))

