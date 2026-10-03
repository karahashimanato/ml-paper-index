<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# The Computational Limits of Deep Learning

- カード: [`arxiv-2007.05558`](../../papers/arxiv-2007.05558.yaml)
- 著者: Neil C. Thompson, Kristjan Greenewald, Keeheon Lee, Gabriel F. Manso
- 年・掲載: 2020
- 原論文: [PDF](https://arxiv.org/pdf/2007.05558v2)(arXiv v2、カード作成時に読んだ版)
- タグ: deep-learning, efficiency-evaluation, image-classification, scaling-laws
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Main claim: progress across a wide variety of deep-learning applications is strongly reliant on increases in computing power, and the authors state that extrapolating this reliance forward reveals that progress along current lines is rapidly becoming economically, technically and environmentally unsustainable.([Abstract, p.1](https://arxiv.org/pdf/2007.05558v2#page=1 "This article catalogs the extent of this dependency, showing that progress across a wide variety of applications is strongly reliant on increases in computing power."))
- **c2** Data: performance and computation data were extracted by manual review of deep-learning papers (from arXiv and benchmark sources) on established benchmarks; most papers do not report computational requirements, so analyses are limited to the benchmarks with enough data.([Present, p.6](https://arxiv.org/pdf/2007.05558v2#page=6 "In total, we gathered 1,526 deep learning papers, for which we did a detailed manual review for their performance and computation burden data."))
- **c3** Computation measure: where network operations (FLOPs per pass x passes) cannot be computed, the paper uses hardware burden (processors x computation rate x time), which the authors say also estimates the computation needed but is less precise because it depends on hardware implementation efficiency.([Present, p.7](https://arxiv.org/pdf/2007.05558v2#page=7 "This also estimates the computation needed, but is less precise since it depends on hardware implementation efficiency."))
- **c4** Data sources: hardware performance values are mostly taken from hardware designers' official platforms (e.g. NVIDIA, Google) or public databases such as Wikipedia; models with missing details such as training time cannot be estimated.([Supplemental Materials (Data collection), p.25](https://arxiv.org/pdf/2007.05558v2#page=25 "Hardware performance data are mostly gathered from external sources such as ofﬁcial hardware designers plataforms (e.g. NVIDIA, Google) or publicly-available databases (e.g. Wikipedia)."))
- **c5** Cost conversion: projected economic and environmental costs follow Strubell et al.'s methodology for V100 GPU training, with 2022 cloud pricing and updated carbon estimates (geometric mean) from Dodge et al.([Future (footnote), p.10](https://arxiv.org/pdf/2007.05558v2#page=10 "Economic and environmental costs are measured using the methodology provided by [53] for V100 GPU training."))
- **c6** Disagreement with within-model scaling studies: the authors hypothesize that inconsistencies with other scaling studies arise from measurement approach - 'scaling up' measures improvements to the state of the art while 'scaling down' measures performance deterioration and can yield artificially rosy estimates; they suggest the faster scaling reported for ResNet and NASNet seems to reflect this.([Comparison to other scaling studies, p.12](https://arxiv.org/pdf/2007.05558v2#page=12 "Put simply, the ‘scaling up’ approach measures improvements to the state of the art, whereas the ‘scaling down’ approach measures performance deterioration."))
- **c7** Limitation: only training costs are analysed (deployment costs depend on usage data that is not available), so the analysis is a lower bound on total computation.([Lessening the Computational Burden, p.13](https://arxiv.org/pdf/2007.05558v2#page=13 "Since total costs must necessarily be higher than just training costs, our analysis provides a lower bound on the total computation needed for any given level of performance."))

