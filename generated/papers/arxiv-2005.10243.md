<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# What Makes for Good Views for Contrastive Learning?

- カード: [`arxiv-2005.10243`](../../papers/arxiv-2005.10243.yaml)
- 著者: Yonglong Tian, Chen Sun, Ben Poole, Dilip Krishnan, Cordelia Schmid, Phillip Isola
- 年・掲載: 2020 NeurIPS 2020
- 原論文: [PDF](https://arxiv.org/pdf/2005.10243v3)(arXiv v3、カード作成時に読んだ版)
- タグ: image-classification, joint-embedding, representation-learning, self-supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** InfoMin principle: a good set of views shares the minimal information necessary to perform well on the downstream task; the authors argue that maximizing information is useful only insofar as it is task-relevant.([Introduction, p.2](https://arxiv.org/pdf/2005.10243v3#page=2 "A good set of views are those that share the minimal information necessary to perform well at the downstream task."))
- **c2** Proposition 3.1 assumes minimal sufficient encoders and a downstream task known in advance: the optimal views minimize I(v1; v2) subject to I(v1; y) = I(v2; y) = I(x; y), and the representation learned from them is then optimal for the task.([Proposition 3.1, p.4](https://arxiv.org/pdf/2005.10243v3#page=4 "More formally, the following InfoMin proposition articulates which views are optimal supposing that we know the speciﬁc downstream task T in advance."))
- **c3** Caveat on applying the proposition: unlike the information-bottleneck setting, contrastive learning usually has no labelled training set specifying the downstream task, so the task-relevant information in views cannot easily be evaluated during training; views are instead guided by domain knowledge.([Three Regimes of Information Captured, p.4](https://arxiv.org/pdf/2005.10243v3#page=4 "Unlike in information bottleneck, for contrastive learning we often do not have access to a fully-labeled training set that speciﬁes the downstream task in advance, and thus evaluating how much task-relevant information is contained in the views and representation at training time is challenging."))
- **c4** Measurement caveat: mutual information between views is measured with I_NCE as a neural proxy, which depends on the network architecture, so each plot varies only the input views while keeping other settings fixed.([View Selection Inﬂuences Mutual Information and Accuracy, p.5](https://arxiv.org/pdf/2005.10243v3#page=5 "We use INCE as a neural proxy for I, and note it depends on network architectures."))
- **c5** The reverse-U relationship between shared information and downstream performance is presented as an upper bound that might not be reached if views share noise rather than signal.([View Selection Inﬂuences Mutual Information and Accuracy, p.4](https://arxiv.org/pdf/2005.10243v3#page=4 "The upper-bound reverse-U might not be reached if views are selected that share noise rather than signal."))
- **c6** Task dependence (Colorful Moving-MNIST toy, frozen backbone with a linear task head): what the views share determines which factors are learned; when background is shared, digit information is left out, which the authors say might be because background bits predominate and act as a shortcut for the contrastive task.([Optimal Views Depend on the Downstream Task, p.9](https://arxiv.org/pdf/2005.10243v3#page=9 "This might because the information bits of background predominates, and the encoder chooses the background as a “shortcut” to solve the contrastive pre-training task."))
- **c7** Learning views without labels (adversarially minimizing I_NCE with a flow generator) in most cases over-reduces I_NCE and was unstable across runs with the same hyperparameters; the authors conjecture the generator, lacking task knowledge, breaks the constraint of Proposition 3.1, and add a semi-supervised variant that uses a handful of downstream labels.([Unsupervised View Learning: Minimize I(v1; v2), p.10](https://arxiv.org/pdf/2005.10243v3#page=10 "In addition, we found this GAN-style training is unstable, as different runs with the same hyper-parameter vary signiﬁcantly."))
- **c8** Augmentation strength: varying the magnitude of RandomResizedCrop and Color Jittering traces reverse-U shapes on ImageNet, and the sweet spots (crop area bound 0.2, jitter strength 1.0) are identified from these plots (MoCo framework, 100 pre-training epochs, linear classifier trained for 60 epochs, per Appendix C).([Data Augmentation to Reduce Mutual Information between Views, p.6](https://arxiv.org/pdf/2005.10243v3#page=6 "The plots on ImageNet [16] are shown in Fig. 5, where we identify a sweet spot at 1.0 for Color Jittering and 0.2 for RandomResizedCrop."))

