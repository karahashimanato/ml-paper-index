<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# M$^2$PFN: End-to-End Disentangled Alignment for Generalizable Multimodal In-Context Learning in Alzheimer's Disease

- カード: [`arxiv-2609.28836`](../../papers/arxiv-2609.28836.yaml)
- 著者: Lujia Zhong, Shuo Huang, Jianwei Zhang, Xinyu Nie, Yonggang Shi
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.28836v1)(arXiv v1、カード作成時に読んだ版)
- タグ: deep-learning, in-context-learning, supervised, tabular-classification, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** M2PFN is an end-to-end framework that turns TabPFN into a multimodal (MRI + tabular) Alzheimer's disease predictor.([Abstract, p.1](https://arxiv.org/pdf/2609.28836v1#page=1 "M2PFN, an end-to-end framework that turns this tabular foundation model into a multimodal AD predictor."))
- **c2** On two external cohorts without retraining, M2PFN achieves the best AUC and lowest MMSE MAE among the baselines.([Abstract, p.1](https://arxiv.org/pdf/2609.28836v1#page=1 "On two external cohorts (OASIS-3 and SCAN) with no retraining, M2PFN achieves the best AUC and the lowest MMSE MAE across all baselines, and transfers even when the cognitive instrument changes."))
- **c3** Evaluation protocol: all models are trained only on ADNI; OASIS-3 and SCAN serve only as external test sets.([Experimental setup, p.8](https://arxiv.org/pdf/2609.28836v1#page=8 "All models are trained exclusively on ADNI; OASIS-3 and SCAN are held out and used solely as external test sets."))
- **c4** Baselines are run with the default hyperparameters of their published code (no tuning).([Baselines, p.9](https://arxiv.org/pdf/2609.28836v1#page=9 "For every baseline, we adopt the default hyperparameters specified in the published code."))
- **c5** The tabular-only baselines are XGBoost, AutoGluon and TabPFN-v2.5.([Baselines, p.10](https://arxiv.org/pdf/2609.28836v1#page=10 "Unimodal tabular: XGBoost [42], AutoGluon [43], TabPFN-v2.5 [21]."))
- **c6** Results are reported as mean and standard deviation over 5 random seeds.([Experimental setup, p.8](https://arxiv.org/pdf/2609.28836v1#page=8 "Both instantiations are trained and evaluated with 5 random seeds, and we report the mean ± standard deviation across seeds"))

