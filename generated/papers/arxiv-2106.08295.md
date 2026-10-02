<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# A White Paper on Neural Network Quantization

- カード: [`arxiv-2106.08295`](../../papers/arxiv-2106.08295.yaml)
- 著者: Markus Nagel, Marios Fournarakis, Rana Ali Amjad, Yelysei Bondarenko, Mart van Baalen, Tijmen Blankevoort
- 年・掲載: 2021
- 原論文: [PDF](https://arxiv.org/pdf/2106.08295v1)(arXiv v1、カード作成時に読んだ版)
- タグ: deep-learning, model-compression, post-hoc, post-training-quantization, quantization, quantization-aware-training, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Survey/guide claim: in most cases PTQ is sufficient for 8-bit quantization with close to floating-point accuracy, without re-training or labelled data.([Abstract, p.1](https://arxiv.org/pdf/2106.08295v1#page=1 "In most cases, PTQ is sufficient for achieving 8-bit quantization with close to floating-point accuracy."))
- **c2** QAT needs fine-tuning and labelled training data but enables lower-bit quantization with competitive results.([Abstract, p.1](https://arxiv.org/pdf/2106.08295v1#page=1 "QAT requires fine-tuning and access to labeled training data but enables lower bit quantization with competitive results."))
- **c3** PTQ calibration: in a footnote to the AdaRound step of their standard PTQ pipeline, the authors state that usually 500 to 1000 unlabeled images are sufficient as a calibration set.([Section 3.5 Standard PTQ pipeline (footnote), p.16](https://arxiv.org/pdf/2106.08295v1#page=16 "Usually, between 500 and 1000 unlabeled images are sufficient as a calibration set."))
- **c4** Evaluation protocol: all models (ImageNet classifiers, DeepLabV3 on Pascal VOC, EfficientDet on COCO 2017, BERT-base on GLUE) are evaluated on the respective validation sets (Table 6 caption; the same sentence is in the Table 10 QAT caption).([Section 3.6 Experiments (Table 6 caption), p.17](https://arxiv.org/pdf/2106.08295v1#page=17 "We evaluate all models on the respective validation sets."))
- **c5** QAT tuning protocol: results are reported with the best learning rate per quantization configuration, with no further hyperparameter tuning. Results are reported on the validation sets; a separate split for selecting the learning rate was not found in the text.([Section 4.5 Experiments, p.24](https://arxiv.org/pdf/2106.08295v1#page=24 "We present the results with the best learning rate per quantization configuration and perform no further hyper-parameter tuning."))
- **c6** Failure mode: networks with depth-wise separable layers (MobileNetV2, EfficientNet lite, DeeplabV3, EfficientDet-D1) are more challenging to quantize with QAT, a trend the authors say they also observed in their PTQ results and that is discussed in the literature.([Section 4.5 Experiments, p.24](https://arxiv.org/pdf/2106.08295v1#page=24 "Quantizing networks with depth-wise separable layers (MobileNetV2, EfficientNet lite, DeeplabV3, EfficientDet-D1) is more challenging; a trend we also observed from the PTQ results in section 3.6 and discussed in the literature (Chin et al., 2020; Sheng et al., 2018a)."))
- **c7** Failure mode in BERT-base: a few activation tensors have extreme differences in dynamic range; to make PTQ work, these layers were identified with the debugging procedure and kept in 16 bit.([Section 3.6 Experiments, p.17](https://arxiv.org/pdf/2106.08295v1#page=17 "For BERT-base, we observe that a few activation tensors have extreme differences in their dynamic ranges."))

