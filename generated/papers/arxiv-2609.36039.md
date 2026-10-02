<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Multi-Class, Multi-Tier Network Intrusion Detection: A Comprehensive and Reproducible Benchmark

- カード: [`arxiv-2609.36039`](../../papers/arxiv-2609.36039.yaml)
- 著者: Yufeng Xin, Bryant Goseland, Mohamed Rahouti
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.36039v1)(arXiv v1、カード作成時に読んだ版)
- タグ: gradient-boosted-trees, heterogeneous-ensembles, linear-models, random-forests, supervised, tabular-attention, tabular-classification, tabular-mlp
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Many CIC-IDS2017 results are hard to compare because of labeling errors, inconsistent flow extraction, potential leakage and benign-dominated metrics.([Abstract, p.1](https://arxiv.org/pdf/2609.36039v1#page=1 "Still, many published results on this dataset are difficult to compare due to labeling errors, inconsistent flow extraction, potential leakage, and performance evaluation metrics dominated by benign traffic."))
- **c2** Eleven tabular classifiers are evaluated at binary, nine-class and fifteen-class levels; a soft-voting ensemble of RF, XGBoost and LightGBM is best at the fine tier.([Abstract, p.1](https://arxiv.org/pdf/2609.36039v1#page=1 "A soft-voting ensemble of Random Forest, XGBoost, and LightGBM obtains the best fine-tier macro-F1 of 0.955, with coarse and binary macro-F1 scores of 0.980 and 0.999, respectively."))
- **c3** Classifiers are trained with hyperparameters curated from prior literature; no tuning procedure was found in the text.([Methodology, p.4](https://arxiv.org/pdf/2609.36039v1#page=4 "Eleven classifiers are trained on the training split, with hyperparameters set curated from prior literature."))
- **c4** Flows are partitioned 70/15/15 into train/validation/test with a seeded stratified shuffle on the coarse attack family.([Methodology, p.4](https://arxiv.org/pdf/2609.36039v1#page=4 "The labeled and preprocessed flows are partitioned into train (70%), validation (15%), and test (15%) sets using a seeded stratified shuffle on the coarse attack family."))
- **c5** Performance is effectively saturated, so substituting another tabular classifier has little value on single-dataset CIC-IDS2017 studies.([Discussion, p.7](https://arxiv.org/pdf/2609.36039v1#page=7 "For single-dataset CIC-IDS2017 studies, this leaves little value in simply substituting another tabular classifier; meaningful progress requires changes to the data, feature representation, rare-class treatment, or transfer setting."))
- **c6** Limitations: CIC-IDS2017 is a controlled five-day benchmark, and the smallest classes have very few test samples.([Limitations, p.7](https://arxiv.org/pdf/2609.36039v1#page=7 "The smallest classes also limit statistical confidence: Heartbleed has one test sample, SQL Injection has four, and Infiltration has ten."))

