<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Probabilistic Disaggregation of Behind-the-Meter PV Systems Using Conformal Prediction

- カード: [`doi-10.1109_tsg.2026.3676842`](../../papers/doi-10.1109_tsg.2026.3676842.yaml)
- 著者: Jialin He, Tarek A. AlSkaif
- 年・掲載: 2026 IEEE Transactions on Smart Grid
- 原論文: [PDF](https://edepot.wur.nl/713863)(Publisher PDF via OpenAlex (submittedVersion)、カード作成時に読んだ版)
- タグ: conformal-prediction, deep-learning, gradient-boosted-trees, linear-models, random-forests, supervised, tabular-regression, uncertainty-estimation
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The paper proposes a conformal-prediction variant, Adaptive Mondrian Binning (AMB), to address the arbitrary bin count of CP with Mondrian Binning.([Abstract, p.2](https://edepot.wur.nl/713863#page=2 "To address the arbitrary bin count in CP with MB, the paper proposes a novel CP variant, namely: Adaptive Mondrian Binning (AMB)."))
- **c2** Main claim: with LightGBM as the deterministic regressor, AMB outperforms quantile regression and the other CP variants.([Abstract, p.2](https://edepot.wur.nl/713863#page=2 "Results show that using LightGBM as the deterministic regressor, AMB outperforms quantile regression and other CP variants."))
- **c3** Evaluation data: two real datasets (Amsterdam, the Netherlands; Sydney/Ausgrid, Australia); households are split into two groups, once in file order and in thirty random splits.([Experiment Settings, p.8](https://edepot.wur.nl/713863#page=8 "Multiple splits: Thirty random splits are performed, each dividing the households into a group of 10 and a group of 11, similar to the single split"))
- **c4** Deterministic regressors compared were MLR, random forest and LightGBM, plus FCNN, ResNet and LSTM; DL models were similar to LightGBM in accuracy but took much longer to train.([Deterministic Disaggregation Results, p.9](https://edepot.wur.nl/713863#page=9 "In both datasets, DL methods are similar to LGB in terms of accuracy, while incurring significantly longer training time."))
- **c5** The quantile-regression baseline is LightGBM with a quantile objective. How the regressors' hyperparameters were set is not found in the text (only the capacity-estimation thresholds are given).([Probabilistic Disaggregation Results, p.9](https://edepot.wur.nl/713863#page=9 "In this study, QR is realized by changing the objective of LGB to 'quantile'."))

