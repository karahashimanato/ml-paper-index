<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Systematic Evaluation of TabPFN-TS for Zero-Shot Probabilistic Heat Load Forecasting in District Heating Networks

- カード: [`arxiv-2608.20024`](../../papers/arxiv-2608.20024.yaml)
- 著者: Ben Spoek, Karim K. Ben Hicham, Kai Derzsi, Philipp Althaus, Alexander Mitsos, Dirk Müller
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.20024v1)(arXiv v1、カード作成時に読んだ版)
- タグ: automl-systems, deep-learning, gradient-boosted-trees, in-context-learning, supervised, tabular-foundation-model, time-series-forecasting, time-series-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The study evaluates TabPFN-TS against time-series foundation models and trained ML baselines for probabilistic heat load forecasting in district heating networks.([Abstract, p.1](https://arxiv.org/pdf/2608.20024v1#page=1 "This study systematically evaluates TabPFN-TS against state-of-the-art time-series foundation models and trained machine-learning baselines for probabilistic heat load forecasting in district heating networks."))
- **c2** Chronos-2 has the lowest aggregate full-year error, while TabPFN-TS shows better empirical calibration.([Abstract, p.1](https://arxiv.org/pdf/2608.20024v1#page=1 "Although Chronos-2 achieves the lowest aggregate full-year error, TabPFN-TS shows better empirical calibration."))
- **c3** The trained AutoGluon baselines are fitted on 2023 data and evaluated on rolling 24-hour forecasts in 2024. Each model class uses the target history according to its own defaults.([Methodology (forecasting models), p.6](https://arxiv.org/pdf/2608.20024v1#page=6 "The predictors are trained on 2023 target values and evaluated on rolling 24-hour forecasts in 2024."))
- **c4** The TabPFN-TS configuration (context length, resolution, horizon, covariates) is chosen with diagnostics on three representative weeks of 2024, the same year used for the full-year evaluation.([Case Study and Experimental Design, p.9](https://arxiv.org/pdf/2608.20024v1#page=9 "The selected winter, transitional, and summer weeks in 2024 are January 15–21, April 22–28, and August 12–18, respectively."))
- **c5** The main experiments feed realized future temperature as the known covariate, which amounts to assuming a perfect weather forecast. A separate sensitivity analysis uses archived forecasts.([Methodology (forecasting models), p.6](https://arxiv.org/pdf/2608.20024v1#page=6 "This setting can be interpreted as a perfect-weather-forecast assumption"))
- **c6** The authors declare no known competing financial interests.([Declaration of Competing Interest, p.25](https://arxiv.org/pdf/2608.20024v1#page=25 "The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper."))

