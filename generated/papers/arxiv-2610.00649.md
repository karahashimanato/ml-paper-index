<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# On Evaluating Quantum Kernel Robustness for Low-Resource Cross-Corpus Audio Deepfake Detection

- カード: [`arxiv-2610.00649`](../../papers/arxiv-2610.00649.yaml)
- 著者: Lisan Al Amin, Lei Zhang, Vandana P. Janeja
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2610.00649v1)(arXiv v1、カード作成時に読んだ版)
- タグ: gradient-boosted-trees, kernel-methods, linear-models, random-forests, supervised, tabular-classification, tabular-mlp
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Design: QSVM, classical SVM and MLP back-ends are trained on the same frozen wav2vec 2.0 embeddings with only 200 labeled training samples.([Abstract, p.1](https://arxiv.org/pdf/2610.00649v1#page=1 "We compare a Quantum Support Vector Machine (QSVM), a classical support vector machine (SVM), and a multilayer perceptron (MLP), all trained on frozen wav2vec 2.0 embeddings using a strict low-resource budget of 200 training samples."))
- **c2** Main claim: quantum kernels can be competitive under severe cross-corpus shift with few labels, but give no consistent advantage under near-domain transfer.([Abstract, p.1](https://arxiv.org/pdf/2610.00649v1#page=1 "These findings suggest that quantum kernel methods can provide a competitive alternative under severe cross-corpus shifts and strict low-resource constraints, although they provide no consistent advantage under near-domain transfer."))
- **c3** Tuning protocol: hyperparameters are selected on the training split only with inner cross-validation, using the same search ranges for all back-ends.([Experimental setup, p.3](https://arxiv.org/pdf/2610.00649v1#page=3 "For fairness, hyperparameters are selected on the training split only, using an inner cross-validation loop, and the same search ranges are used across back-ends."))
- **c4** Thresholds: EER is computed by sweeping the threshold on the target data, while accuracy uses the training-derived threshold; the authors note the gap between the two is the cost of carrying the threshold across the shift and recommend re-estimating it on labeled target data.([Results (cross-corpus robustness), p.5](https://arxiv.org/pdf/2610.00649v1#page=5 "The threshold should be re-estimated on a small labeled sample from the target domain rather than carried over from training."))
- **c5** No significance tests are reported because the five folds come from the same 200-sample pool.([Results (in-corpus discrimination), p.4](https://arxiv.org/pdf/2610.00649v1#page=4 "We do not attach significance tests to these differences as the five folds are drawn from the same 200-sample pool and are not independent, so a paired test would overstate the evidence."))
- **c6** Limitation: no comparison with fine-tuned state-of-the-art detectors and no results on recent large multilingual corpora; all back-ends see only the 4-dimensional PCA features.([Limitations, p.6](https://arxiv.org/pdf/2610.00649v1#page=6 "We do not benchmark against fine-tuned state-of-the-art detectors such as Whisper- or AASIST-based systems [30], and we do not report results on the recent large-scale multilingual corpora MLAAD [31] and XMAD-Bench [32]."))

