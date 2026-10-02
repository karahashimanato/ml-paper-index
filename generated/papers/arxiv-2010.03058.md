<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Characterising Bias in Compressed Models

- カード: [`arxiv-2010.03058`](../../papers/arxiv-2010.03058.yaml)
- 著者: Sara Hooker, Nyalleng Moorosi, Gregory Clark, Samy Bengio, Emily Denton
- 年・掲載: 2020
- 原論文: [PDF](https://arxiv.org/pdf/2010.03058v2)(arXiv v2、カード作成時に読んだ版)
- タグ: deep-learning, model-compression, post-hoc, post-training-quantization, pruning, quantization, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Main claim: overall accuracy hides disproportionately high errors on a small subset (CIE), and for these examples compression amplifies existing algorithmic bias.([Abstract, p.1](https://arxiv.org/pdf/2010.03058v2#page=1 "We further establish that for CIE examples, compression ampliﬁes existing algorithmic bias."))
- **c2** Setup: ResNet-18 on CelebA predicting Blonde hair; protected attributes Male and Young and their intersection; metrics are sub-group error rate, false positive rate and false negative rate relative to the non-compressed baseline.([Methodology, p.3](https://arxiv.org/pdf/2010.03058v2#page=3 "To characterize the impact of compression on age and gender sub-groups we compare sub-group error rate, false positive rate (FPR) and false negative rate (FNR) between a baseline (i.e. non-compressed) and models pruned and quantized to different levels of compression (i.e. compressed)."))
- **c3** Quantization protocol: post-training 8-bit quantization (hybrid dynamic range and fixed-point), with the first 100 training examples as representative (calibration) examples, via TensorFlow Lite; pruning is magnitude pruning during training.([Methodology, p.4](https://arxiv.org/pdf/2010.03058v2#page=4 "We use the MLIR implementation via TensorFlow Lite (Jacob et al., 2018; Lattner et al., 2020)."))
- **c4** Pruning hyperparameters were chosen by a limited grid search minimizing test-set accuracy degradation, and 30 models were trained per compression level to separate effects from training noise.([Methodology, p.3](https://arxiv.org/pdf/2010.03058v2#page=3 "These hyperparameter choices were based upon a limited grid search which suggested that these particular settings minimized degradation to test-set accuracy across all pruning levels."))
- **c5** Failure mode: compression cannibalizes performance on low-frequency attributes to preserve overall performance; for example the false positive rate for Male rises much more than for not Male at 95% pruning, which the authors note appears closely tied to the attributes' representation in the training data.([Results, p.5](https://arxiv.org/pdf/2010.03058v2#page=5 "Compression cannibalizes performance on low-frequency attributes in order to preserve overall performance."))
- **c6** CIE requires no attribute labels, but this becomes a limitation in an overfit regime with 0% training error, where neither CIE measure can be computed on the training set.([Divergence measures, p.6](https://arxiv.org/pdf/2010.03058v2#page=6 "That said, note that this turns into a limitation in an overﬁt 0% training error regime as without any predictive difference it would not be possible to compute CIE using either measure in the training set."))

