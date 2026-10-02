<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# CIN-RiskNet: a dynamic feature-enhanced TabTransformer with hybrid SMOTE-noise augmentation for contrast-induced nephropathy prediction

- カード: [`doi-10.3389_fcvm.2026.1909097`](../../papers/doi-10.3389_fcvm.2026.1909097.yaml)
- 著者: Peng Zhang, Zehao Yang, Xue Zhang, Keyu Gong, Xiaogang Liu, Shicheng Yang, Zhiwei Zhang, Ximing Li, Runnan He
- 年・掲載: 2026 Frontiers in Cardiovascular Medicine
- 原論文: [PDF](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2026.1909097/pdf)(Publisher PDF via OpenAlex (publishedVersion)、カード作成時に読んだ版)
- タグ: imbalance-resampling, supervised, tabular-attention, tabular-classification
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** CIN-RiskNet combines adaptive feature gating, SMOTE oversampling and multi-head self-attention in a TabTransformer.([Abstract, p.1](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2026.1909097/pdf#page=1 "The approach includes adaptive feature gating to suppress noise, synthetic minority oversampling to address class imbalance, and multi-head self-attention to capture complex feature interactions."))
- **c2** Data and protocol: single-center cohort of 1,679 PCI patients (103 with CIN), evaluated with five-fold cross-validation; SMOTE and noise were applied only to the training subset of each fold, and 20% of each training set was held out for validation.([Model training and evaluation protocol, p.9](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2026.1909097/pdf#page=9 "Importantly, in each fold, SMOTE and Gaussian noise were applied strictly to the training subset only, while validation and test subsets were kept untouched to prevent synthetic-sample leakage."))
- **c3** Baselines (logistic regression, random forest, XGBoost, SVM, MLP) used identical splits and preprocessing; how their hyperparameters were set is not found in the text.([Results, p.10](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2026.1909097/pdf#page=10 "To ensure fairness in model comparisons, all methods adopted identical training/testing splits, uniform data preprocessing pipelines, and 5-fold cross-validation."))
- **c4** The paper reports CIN-RiskNet had the highest recall and F1 among the evaluated models, while random forest and XGBoost had slightly higher accuracy.([Results, p.10](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2026.1909097/pdf#page=10 "Among all compared models, CIN-RiskNet achieved the highest recall (0.9540) and F1-score (0.9542), substantially outperforming traditional machine learning baselines in detecting minority-class samples (Table 4)."))
- **c5** The Mehran comparator is a modified version built from available variables because several original Mehran variables were not recorded.([Comparison with clinical scoring, p.9](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2026.1909097/pdf#page=9 "We therefore constructed a modified Mehran-like comparator using available variables (age, diabetes, contrast volume, baseline Scr/eGFR) to provide a pragmatic local benchmark."))
- **c6** Limitation: single-center retrospective study; external multicenter validation is still required.([Limitations, p.14](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2026.1909097/pdf#page=14 "First, this was a single-center retrospective study, which limits external generalizability despite the relatively large cohort (n = 1,679)."))

