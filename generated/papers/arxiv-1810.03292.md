<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Sanity Checks for Saliency Maps

- カード: [`arxiv-1810.03292`](../../papers/arxiv-1810.03292.yaml)
- 著者: Julius Adebayo, Justin Gilmer, Michael Muelly, Ian Goodfellow, Moritz Hardt, Been Kim
- 年・掲載: 2018
- 原論文: [PDF](https://arxiv.org/pdf/1810.03292v3)(arXiv v3、カード作成時に読んだ版)
- タグ: deep-learning, feature-attribution, model-explanation, post-hoc, saliency-maps
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Model parameter randomization test: compare a saliency method's output on the trained model with its output on a randomly initialized network of the same architecture.([Introduction, p.2](https://arxiv.org/pdf/1810.03292v3#page=2 "The model parameter randomization test compares the output of a saliency method on a trained model with the output of the saliency method on a randomly initialized untrained network of the same architecture."))
- **c2** Data randomization test: compare explanations from a model trained on true labels with those from the same architecture trained on randomly permuted labels.([Introduction, p.2](https://arxiv.org/pdf/1810.03292v3#page=2 "The data randomization test compares a given saliency method applied to a model trained on a labeled data set with the method applied to the same model architecture but trained on a copy of the data set in which we randomly permuted all labels."))
- **c3** Evaluation metrics: similarity between original and randomized explanations is quantified by Spearman rank correlation (with and without absolute value), SSIM and HOG correlation.([Visualization & Similarity Metrics, p.4](https://arxiv.org/pdf/1810.03292v3#page=4 "Spearman rank correlation without absolute value (diverging), the structural similarity index (SSIM), and the Pearson correlation of the histogram of gradients (HOGs) derived from two maps"))
- **c4** Main result: Gradients and GradCAM pass, while Guided BackProp and Guided GradCAM are invariant to higher-layer parameters and fail.([Introduction (contributions), p.3](https://arxiv.org/pdf/1810.03292v3#page=3 "Of the methods tested, Gradients & GradCAM pass the sanity checks, while Guided BackProp & Guided GradCAM are invariant to higher layer parameters; hence, fail."))
- **c5** Failure mode of visual assessment: naive visual inspection of masks does not distinguish networks of similar structure but very different parameters.([Cascading Randomization, p.5](https://arxiv.org/pdf/1810.03292v3#page=5 "The observed visual perception versus ranking dichotomy indicates that naive visual inspection of the masks, in this setting, does not distinguish networks of similar structure but widely differing parameters."))
- **c6** In an experiment that keeps the input fixed and multiplies it by random vectors in place of the gradient, the input dominates the product; the authors conclude that methods approximating the input-times-gradient product (they name epsilon-LRP, DeepLift and integrated gradients) mostly return the input when gradients look visually noisy.([Element-wise input-gradient products, p.9](https://arxiv.org/pdf/1810.03292v3#page=9 "This experiment indicates that methods that approximate the “input-times-gradient” mostly return the input, in cases where the gradients look visually noisy as they tend to do."))
- **c7** Scope: the authors present the tests as a step toward more rigorous evaluation, not a verdict on existing methods.([Conclusion and future work, p.10](https://arxiv.org/pdf/1810.03292v3#page=10 "Along these lines, we hope that our paper is a stepping stone towards a more rigorous evaluation of new explanation methods, rather than a verdict on existing methods."))

