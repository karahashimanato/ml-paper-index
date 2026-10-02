<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# When Less Compute Is More: Adaptive Early Exit Improves Pretrained Outlier Detection

- カード: [`arxiv-2609.32898`](../../papers/arxiv-2609.32898.yaml)
- 著者: Tianyang Zhou, Leman Akoglu
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.32898v1)(arXiv v1、カード作成時に読んだ版)
- タグ: in-context-learning, model-compression, tabular-classification, tabular-foundation-model, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The paper presents what it calls the first study of depth-adaptive early exit for pretrained (tabular) outlier detection models.([Abstract, p.1](https://arxiv.org/pdf/2609.32898v1#page=1 "we present the first study of depth-adaptive early-exit for pretrained outlier detection models"))
- **c2** Exiting at the optimal (per-dataset oracle) intermediate layer can improve detection on real-world benchmarks on average, consistently across three foundation models; the paper identifies context pollution (outliers among in-context samples) as a key mechanism.([Abstract, p.1](https://arxiv.org/pdf/2609.32898v1#page=1 "can also improve detection performance on diverse real-world benchmarks by 4.7–7.3% on average, consistent across three distinct foundation models"))
- **c3** Evaluation uses three real-world outlier detection benchmarks (ADBench, OddBench, OvRBench) plus the synthetic SynBench, under clean and polluted context.([Experiments, p.7](https://arxiv.org/pdf/2609.32898v1#page=7 "We evaluate ROUT on ADBench (Han et al., 2022), OddBench, and OvRBench (Ding et al., 2026a), three real-world outlier detection benchmarks comprising 47, 690, and 755 datasets, respectively"))
- **c4** For the LA-Entropy early-exit baseline, the entropy threshold is tuned on synthetic validation datasets and then fixed for all test datasets (not tuned on test labels).([Experiments, p.7](https://arxiv.org/pdf/2609.32898v1#page=7 "We tune τ on synthetic validation datasets and keep it fixed across all test datasets."))
- **c5** The Oracle (per-dataset best exit layer) and Best fixed layer rows are selected with ground-truth test AUROCs and are reported only as references, not as deployable methods.([Experiments, p.7](https://arxiv.org/pdf/2609.32898v1#page=7 "Both use ground-truth test AUROCs and are reported as references."))
- **c6** Per the reference list, author Leman Akoglu co-authored OutFormer, one of the three evaluated backbones; the paper does not discuss this as a conflict of interest.([References, p.10](https://arxiv.org/pdf/2609.32898v1#page=10 "Xueying Ding, Haomin Wen, Simon Klüttermann, and Leman Akoglu."))

