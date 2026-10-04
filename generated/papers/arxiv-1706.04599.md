<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# On Calibration of Modern Neural Networks

- カード: [`arxiv-1706.04599`](../../papers/arxiv-1706.04599.yaml)
- 著者: Chuan Guo, Geoff Pleiss, Yu Sun, Kilian Q. Weinberger
- 年・掲載: 2017
- 原論文: [PDF](https://arxiv.org/pdf/1706.04599v2)(arXiv v2、カード作成時に読んだ版)
- タグ: deep-learning, image-classification, post-hoc, selective-prediction
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Main observation: modern neural networks, unlike those from a decade ago, are poorly calibrated (confidence does not match the probability of being correct).([Abstract, p.1](https://arxiv.org/pdf/1706.04599v2#page=1 "We discover that modern neural networks, unlike those from a decade ago, are poorly calibrated."))
- **c2** Factors (correlational, not causal): increased model capacity and lack of regularization are closely related to miscalibration; the paper examines depth, width, Batch Normalization and weight decay.([Observing miscalibration, p.3](https://arxiv.org/pdf/1706.04599v2#page=3 "Though we cannot claim causality, we ﬁnd that increased model capacity and lack of regularization are closely related to model miscalibration."))
- **c3** Mechanism of temperature scaling: a single scalar T > 0 for all classes divides the logits, T is optimized with respect to NLL on the validation set, and since it does not change the softmax argmax, class predictions and accuracy are unchanged.([Calibration methods, p.6](https://arxiv.org/pdf/1706.04599v2#page=6 "In other words, temperature scaling does not affect the model’s accuracy."))
- **c4** Calibration set and scope: all compared methods are post-processing steps that need a hold-out validation set (in practice possibly the same set used for hyperparameter tuning), and the paper assumes training, validation and test sets are drawn from the same distribution; all calibration results in the paper are therefore in-distribution, and nothing is claimed about calibration under dataset shift.([Calibration methods, p.4](https://arxiv.org/pdf/1706.04599v2#page=4 "We assume that the training, validation, and test sets are drawn from the same distribution."))
- **c5** Main empirical result: temperature scaling outperforms all other compared methods on the vision tasks and performs comparably on the NLP datasets (compared: histogram binning, isotonic regression, BBQ, vector and matrix scaling).([Results, p.7](https://arxiv.org/pdf/1706.04599v2#page=7 "Temperature scaling outperforms all other methods on the vision tasks, and performs comparably to other methods on the NLP datasets."))
- **c6** Evaluation metric: ECE with equally spaced confidence bins (M = 15 in the results table) is the primary calibration metric, with MCE and NLL also defined. In Results, the authors note that the one dataset temperature scaling did not calibrate, Reuters, was already well calibrated (ECE <= 1%), and say it is 'also possible' that their measurements there are affected by the dataset split or the binning scheme.([Definitions, p.3](https://arxiv.org/pdf/1706.04599v2#page=3 "We use ECE as the primary empirical metric to measure calibration."))
- **c7** Failure mode of richer calibrators: matrix scaling performs poorly with hundreds of classes and fails to converge on 1000-class ImageNet; the authors state any calibration model with tens of thousands or more parameters will overfit a small validation set even with regularization.([Results, p.8](https://arxiv.org/pdf/1706.04599v2#page=8 "Any calibration model with tens of thousands (or more) parameters will overﬁt to a small validation set, even when applying regularization."))

