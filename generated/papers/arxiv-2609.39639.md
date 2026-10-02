<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Marginal Response Surface Elicitation for Zero-Label Tabular Learning

- カード: [`arxiv-2609.39639`](../../papers/arxiv-2609.39639.yaml)
- 著者: Liangyu Teng, Yicheng Ding, Jing Liu, Hengsong Liu, Juncen Guo, Hongru Li, Jingyu Zhang, Liang Song
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.39639v1)(arXiv v1、カード作成時に読んだ版)
- タグ: interpretable-models, large-language-models, tabular-classification
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** MARS turns feature-level LLM priors into a reusable zero-shot tabular classifier.([Abstract, p.1](https://arxiv.org/pdf/2609.39639v1#page=1 "We propose Marginal Response Surface Elicitation (MARS), a method that transforms feature-level LLM priors into a reusable, zero-shot tabular classifier."))
- **c2** On eight benchmark tasks MARS has the highest average AUC and AP and outperforms direct prompting at lower cost.([Abstract, p.1](https://arxiv.org/pdf/2609.39639v1#page=1 "Across eight tabular benchmark tasks, MARS achieves the highest average AUC and AP, outperforming direct prompting by 1.97 and 6.21 percentage points respectively, while substantially reducing end-to-end costs."))
- **c3** A within-class permutation experiment with CatBoost suggests little benefit from cross-feature couplings with 4-16 training samples.([Introduction, p.2](https://arxiv.org/pdf/2609.39639v1#page=2 "We find that the average performance difference is close to zero for 4–16 training samples, suggesting that the model gains little additional predictive benefit from cross-feature couplings in this regime."))
- **c4** Supervised and few-shot baselines (incl. XGBoost, CatBoost, TabPFN-3, TabICLv2) get only 4 labeled examples for both training and model selection.([Experimental setup, p.6](https://arxiv.org/pdf/2609.39639v1#page=6 "The first two groups of baselines are provided with 4 labeled examples (2 per class) for both training and model selection."))
- **c5** Results come from a single 80/20 stratified split with seed 0 (the five LLM responses are not data-split seeds).([Appendix, p.13](https://arxiv.org/pdf/2609.39639v1#page=13 "We use an 80/20 stratified split with random seed 0."))
- **c6** Test sets larger than 800 rows are subsampled to about 800 rows.([Appendix, p.13](https://arxiv.org/pdf/2609.39639v1#page=13 "For test partitions larger than 800 rows, we sample approximately 800 rows proportionally by class with seed 0; unused test records are not moved into the reference pool."))

