<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Hoeffding adaptive splitting trees for data stream classification with concept drift and ensemble learning

- カード: [`arxiv-2608.16659`](../../papers/arxiv-2608.16659.yaml)
- 著者: Daniel Nowak Assis, Jean Paul Barddal, Fabrício Enembreck
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.16659v1)(arXiv v1、カード作成時に読んだ版)
- タグ: error-rate-drift-detectors, random-forests, stream-classification, streaming, supervised, tree-ensembles
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Main claim: the proposed Hoeffding Adaptive Splitting Trees improve ensemble performance and achieve state-of-the-art results in an evaluation covering benchmark comparisons, computational cost and concept drift adaptation.([Abstract, p.1](https://arxiv.org/pdf/2608.16659v1#page=1 "Experimental results demonstrate that Hoeffding Adaptive Splitting Trees enhance ensemble performance and achieve state-of-the-art results across a comprehensive evaluation, including benchmark comparisons, computational cost analysis, and concept drift adaptation."))
- **c2** Data: 13 real-world streams and 24 synthetic streams (AGRAWAL, SEA, LED, RBF, HYPER generators); in the synthetic streams drift is simulated by the generator (e.g. switching concept functions), so drift positions are known by construction.([Methodology, p.12](https://arxiv.org/pdf/2608.16659v1#page=12 "We performed experiments with 13 real-world datasets made available in [32] and 24 synthetic datasets retrieved from [33]."))
- **c3** Ensemble hyperparameters were not tuned: all ensembles (100 base learners) used the MOA default parameters.([Methodology, p.14](https://arxiv.org/pdf/2608.16659v1#page=14 "All parameters from ensembles were set to default as implemented in the MOA framework."))
- **c4** Evaluation protocol: prequential (test-then-train) evaluation, with metrics averaged over 20 evenly spaced points of the stream; ensembles are compared with a Friedman test and Holm-corrected Wilcoxon post-hoc tests.([Methodology, p.14](https://arxiv.org/pdf/2608.16659v1#page=14 "As in [7], we assess the predictive performance obtained with a test-then-train validation strategy, where every instance is used first for testing and then for training, known as Prequential evaluation [40]."))
- **c5** The change detector inside all LAST-type trees is HDDM_A, chosen from the authors' earlier detector comparison, where HDDM_A, MDDM_A and ADWIN performed comparably and were cheaper than DDM-type detectors.([Methodology, p.15](https://arxiv.org/pdf/2608.16659v1#page=15 "The detector used in all LAST versions was HDDMA [44], given the analysis done in [6]."))
- **c6** On synthetic drifting streams the proposed trees have little effect relative to a Hoeffding Tree; the gains appear mainly on real-world, multi-class data.([Results, p.18](https://arxiv.org/pdf/2608.16659v1#page=18 "Figure 6 shows that on synthetic data the proposed trees have little effect, with the F1-Score difference to HT staying close to zero for all ensembles."))

