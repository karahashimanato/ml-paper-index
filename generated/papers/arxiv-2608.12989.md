<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Balanced Adaptive Prototype Selection for Scalable TabPFN Inference on Large-Scale Tabular Data

- カード: [`arxiv-2608.12989`](../../papers/arxiv-2608.12989.yaml)
- 著者: Mahboobe Jadid, Melika Rezaye Garkani, Ali Mousavi
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.12989v1)(arXiv v1、カード作成時に読んだ版)
- タグ: in-context-learning, tabular-classification, tabular-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** BAPS builds compact, information-preserving inference contexts so that a frozen TabPFN can be applied to large datasets.([Abstract, p.1](https://arxiv.org/pdf/2608.12989v1#page=1 "This paper introduces Balanced Adaptive Prototype Selection (BAPS), a framework for constructing compact, information-preserving contexts for scalable TabPFN inference."))
- **c2** On the million-row HIGGS and SUSY datasets, 512 prototypes retain strong predictive performance and calibration.([Abstract, p.1](https://arxiv.org/pdf/2608.12989v1#page=1 "Experiments on the million-row HIGGS and SUSY datasets show that 512 prototypes retain strong predictive performance and reliable calibration, corresponding to an approximately 1,953-fold context compression."))
- **c3** Only results on the two largest datasets (HIGGS, SUSY) are reported, citing the conference page limit.([Experimental setup, p.4](https://arxiv.org/pdf/2608.12989v1#page=4 "To comply with the conference page limit, only the results on the two largest datasets, HIGGS and SUSY, are presented, as they provide the most challenging evaluation of scalability under million-scale data."))
- **c4** The setup describes the evaluation inconsistently: one sentence says five benchmarks (HIGGS, SUSY, Covertype, Electricity, Diabetes), another says six datasets (Breast Cancer, Wine, Digits, Covertype, SUSY, HIGGS).([Experimental setup, p.4](https://arxiv.org/pdf/2608.12989v1#page=4 "The evaluation includes six binary and multi-class benchmark datasets spanning medical, chemical, image-derived, environmental, and high-energy physics domains."))
- **c5** Comparisons are among context-construction methods for the same TabPFN under identical partitions, seeds and prototype budgets; no non-TabPFN baseline (e.g. GBDT) was found in the reported results.([Results, p.4](https://arxiv.org/pdf/2608.12989v1#page=4 "All reduced-context methods are compared under identical data partitions, random seeds, and prototype budgets; hence, observed differences primarily reflect the predictive value of the constructed contexts."))

