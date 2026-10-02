<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Partition Scores Are Not System Scores: Deployment-Fidelity Gaps in Decomposed Algorithm Selection

- カード: [`arxiv-2609.13785`](../../papers/arxiv-2609.13785.yaml)
- 著者: Jiachen Zhang, Yu Tang, Li Zhu
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.13785v1)(arXiv v1、カード作成時に読んだ版)
- タグ: automl-systems, gradient-boosted-trees, random-forests, supervised, tabular-classification
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The paper defines the deployment-fidelity gap as partition-level utility (with a within-family oracle) minus deployable end-to-end utility.([Abstract, p.1](https://arxiv.org/pdf/2609.13785v1#page=1 "We define the deployment-fidelity gap G(R) as the difference between partition-level and deployable end-to-end utility"))
- **c2** On five public algorithm-selection benchmarks (including TabZilla, TabRepo and TALENT), every decomposed pipeline has a positive gap.([Abstract, p.1](https://arxiv.org/pdf/2609.13785v1#page=1 "Across five public algorithm-selection benchmarks spanning tabular AutoML and combinatorial CSP/SAT, every decomposed pipeline has positive G(R), ranging from 0.012 on TabZilla to 0.13 on PROTEUS-2014."))
- **c3** Tabular benchmarking literature uses best-in-family summaries (best deep model vs. best GBDT) as the primary comparison object, which the paper treats as an oracle-style quantity.([Related Work, p.2](https://arxiv.org/pdf/2609.13785v1#page=2 "tabular benchmarking literature reports best-in-family summaries – best deep model versus best gradient boosting model – as the primary comparison object"))
- **c4** Protocol: 5 seeds x 5-fold stratified CV with per-instance utilities; family selectors are random forests and the default within-family selector is a per-algorithm gradient-boosted regressor.([Benchmarks and protocol, p.6](https://arxiv.org/pdf/2609.13785v1#page=6 "We run 5 seeds × 5-fold stratified CV and convert performance to per-instance utilities in [0, 1]"))
- **c5** Partition and end-to-end scores should be reported side by side.([Abstract, p.1](https://arxiv.org/pdf/2609.13785v1#page=1 "Partition and end-to-end scores should be reported side by side."))
- **c6** Stated limitation: exhaustive HPO or domain-specific meta-learners may shrink the gap further, but such improvements must still be reported end-to-end.([Limitations and Conclusion, p.9](https://arxiv.org/pdf/2609.13785v1#page=9 "exhaustive HPO or domain-specific meta-learners may shrink G(R) further; such improvements must still be reported end-to-end"))

