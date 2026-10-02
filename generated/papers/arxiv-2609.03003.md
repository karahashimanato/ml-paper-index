<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Causal Foundation Models

- カード: [`arxiv-2609.03003`](../../papers/arxiv-2609.03003.yaml)
- 著者: Christopher Stith, Hossein Rahmani, Jesse C. Cresswell
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.03003v1)(arXiv v1、カード作成時に読んだ版)
- タグ: automl-systems, causal-effect-estimation, gradient-boosted-trees, in-context-learning, tabular-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** One stated contribution is a standardized empirical comparison of three causal foundation models on semi-synthetic observational data.([Benchmarking CFMs, p.18](https://arxiv.org/pdf/2609.03003v1#page=18 "One contribution of our work is establishing a standardized, fair empirical comparison across these three CFMs for causal inference on more complex semi-synthetic observational data."))
- **c2** Models are evaluated on the semi-synthetic RealCause-Lalonde benchmark (Lalonde-CPS and Lalonde-PSID cohorts), with metrics aggregated over 10 semi-synthetic realizations.([Experimental setup, p.18](https://arxiv.org/pdf/2609.03003v1#page=18 "we evaluate models on the semi-synthetic RealCause-Lalonde benchmark (LaLonde, 1986; Neal et al., 2020)."))
- **c3** Nuisance models of the classical baselines are selected with FLAML AutoML, run separately per nuisance, estimator, realization and cohort, with a 900-second budget and 3-fold cross-validation.([Experimental setup, p.18](https://arxiv.org/pdf/2609.03003v1#page=18 "To provide strong, competitive baselines, all underlying nuisance models are selected via FLAML AutoML (v2.3.5; Wang et al. (2021)) run independently per nuisance, per estimator, per RealCause realization, and per cohort with a 900-second budget and 3-fold cross-validation."))
- **c4** The CFMs are frozen pretrained checkpoints applied without any parameter or hyperparameter tuning.([Experimental setup, p.19](https://arxiv.org/pdf/2609.03003v1#page=19 "These models are downloaded out-of-the-box from their respective sources and applied without any parameter or hyperparameter tuning."))
- **c5** Without being trained on the Lalonde data distributions, the CFMs are reported to be competitive with the classical estimators.([Results and Discussion, p.19](https://arxiv.org/pdf/2609.03003v1#page=19 "Despite not being trained on the Lalonde data distributions, CFMs are remarkably competitive with classical estimators."))
- **c6** Runtime counts training, tuning and inference for classical baselines but only inference for CFMs; CFM pretraining is excluded.([Experimental setup, p.19](https://arxiv.org/pdf/2609.03003v1#page=19 "This means we include training, tuning, and inference for classical baselines, but only inference for CFMs since this is the only step we perform."))

