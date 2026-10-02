<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# A Benchmark for Interpretability Methods in Deep Neural Networks

- カード: [`arxiv-1806.10758`](../../papers/arxiv-1806.10758.yaml)
- 著者: Sara Hooker, Dumitru Erhan, Pieter-Jan Kindermans, Been Kim
- 年・掲載: 2018
- 原論文: [PDF](https://arxiv.org/pdf/1806.10758v3)(arXiv v3、カード作成時に読んだ版)
- タグ: deep-learning, feature-attribution, model-explanation, post-hoc, saliency-maps
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** ROAR is proposed as an empirical measure of the approximate accuracy of feature importance estimates in deep networks.([Abstract, p.1](https://arxiv.org/pdf/1806.10758v3#page=1 "We propose an empirical measure of the approximate accuracy of feature importance estimates in deep neural networks."))
- **c2** Critique of deletion metrics without retraining: the accuracy drop cannot be separated from the distribution shift caused by removal.([Introduction, p.1](https://arxiv.org/pdf/1806.10758v3#page=1 "Without re-training,it is unclear whether the degradation in model performance comes from the distribution shift or because the features that were removed are truly informative [10, 12]."))
- **c3** Protocol: for each dataset (ImageNet, Birdsnap, Food 101) and estimator, new train and test sets are generated at several fractions of modified features; five ResNet-50 models are trained from random initialization on each modified dataset and the average test accuracy is reported.([Experimental setup, p.6](https://arxiv.org/pdf/1806.10758v3#page=6 "We independently train 5 ResNet-50 models from random initialization on each of these modified dataset and report test accuracy as the average of these 5 runs."))
- **c4** Main finding: Gradients, Integrated Gradients and Guided BackProp are worse than or on par with a random assignment of importance.([Conclusion and Future Work, p.9](https://arxiv.org/pdf/1806.10758v3#page=9 "Surprisingly, we find that the commonly used base estimators, Gradients, Integrated Gradients and Guided BackProp are worse or on par with a random assignment of importance."))
- **c5** VarGrad and SmoothGrad-Squared strongly improve the quality of the base estimators and far outperform a random guess, whereas ensembles such as SmoothGrad are more computationally intensive but do not improve upon a single estimate (in some cases worse).([Conclusion and Future Work, p.9](https://arxiv.org/pdf/1806.10758v3#page=9 "However, we do find that VarGrad and SmoothGrad-Squared strongly improve the quality of these methods and far outperform a random guess."))
- **c6** Limitation: the retrained model used for evaluation is not the model on which the importance estimates were computed.([ROAR: Remove And Retrain, p.4](https://arxiv.org/pdf/1806.10758v3#page=4 "For one, while the architecture is the same, the model used during evaluation is not the same as the model on which the feature importance estimates were originally obtained."))
- **c7** Limitation: with fully redundant features, accuracy may not drop until the whole redundant set is removed.([Figure 2 caption (validating ROAR on artificial data), p.5](https://arxiv.org/pdf/1806.10758v3#page=5 "This plot also shows the limitation of ROAR, an accuracy decrease might not happen until a complete set of fully redundant features is removed."))

