<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks

- カード: [`arxiv-1610.02136`](../../papers/arxiv-1610.02136.yaml)
- 著者: Dan Hendrycks, Kevin Gimpel
- 年・掲載: 2016
- 原論文: [PDF](https://arxiv.org/pdf/1610.02136v3)(arXiv v3、カード作成時に読んだ版)
- タグ: dataset-shift-detection, deep-learning, image-classification, post-hoc, selective-prediction
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Selection signal: correctly classified examples tend to have a higher maximum softmax probability than misclassified and out-of-distribution examples, which allows detecting the latter (the baseline needs no change to the classifier).([Abstract, p.1](https://arxiv.org/pdf/1610.02136v3#page=1 "Correctly classiﬁed examples tend to have greater maximum softmax probabilities than erroneously classiﬁed and out-of-distribution examples, allowing for their detection."))
- **c2** Caveat: the softmax prediction probability, viewed in isolation, corresponds poorly to confidence; the authors' point is that it still ranks examples usefully (incorrect / out-of-distribution examples tend to get lower values), not that it is calibrated.([Introduction, p.1](https://arxiv.org/pdf/1610.02136v3#page=1 "Throughout our experiments we establish that the prediction probability from a softmax distribution has a poor direct correspondence to conﬁdence."))
- **c3** Evaluation metric: because a detector needs a score threshold that trades off false negatives and false positives, the paper uses threshold-independent AUROC, plus AUPR (reported with success/in-distribution and with error/out-of-distribution as the positive class) because AUROC is not ideal when base rates differ greatly; no operating threshold is chosen.([Problem formulation and evaluation, p.2](https://arxiv.org/pdf/1610.02136v3#page=2 "Faced with this issue, we employ the Area Under the Receiver Operating Characteristic curve (AUROC) metric, which is a threshold-independent performance evaluation (Davis & Goadrich, 2006)."))
- **c4** OOD protocol (vision): all in-distribution test examples are positives; out-of-distribution negatives are realistic images and noise: SUN scenes for CIFAR-10/100; Omniglot, notMNIST and black-and-white CIFAR-10 for MNIST; Gaussian and uniform noise. Other tasks use other text corpora, held-out topics, and noise-mixed or Chinese speech.([Computer vision, p.3](https://arxiv.org/pdf/1610.02136v3#page=3 "For out-of-distribution (negative) examples, we use realistic images and noise."))
- **c5** Failure mode: when distorted inputs degrade the classifier only slightly (a noise-robust fully connected TIMIT network), softmax statistics alone did not give useful out-of-distribution detection, while the trained abnormality module did. Separately (Section 3.2, POS tagging with the WSJ-trained tagger), the authors state that out-of-distribution weblog text, being closer in style to newswire than tweets are, is harder to detect than tweets.([Abnormality detection with auxiliary decoders, p.8](https://arxiv.org/pdf/1610.02136v3#page=8 "Because the classiﬁcation degradation was only slight, the softmax statistics alone did not provide useful out-of-distribution detection."))
- **c6** Evaluation recommendation: report AUPR and AUROC together with the underlying classifier's accuracy, because an always-wrong classifier gets maximum AUPR for error detection when error is the positive class; new detectors should be compared against the softmax baseline of their own classifiers on a variety of datasets and architectures.([Discussion and future work, p.9](https://arxiv.org/pdf/1610.02136v3#page=9 "Reporting the AUPR and AUROC values is important, and so is the underlying classiﬁer’s accuracy since an always-wrong classiﬁer gets a maximum AUPR for error detection if error is the positive class."))

