<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# CIDER-FM: Foundation Models for Causal Inference from Diverse Experimental Regimes

- カード: [`arxiv-2609.39523`](../../papers/arxiv-2609.39523.yaml)
- 著者: Yuche Gao, Arik Reuter, Siyuan Guo, Anish Dhir, Bernhard Schölkopf, Adrian Weller
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.39523v1)(arXiv v1、カード作成時に読んだ版)
- タグ: causal-effect-estimation, in-context-learning, tabular-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The paper studies causal foundation models that combine observational and surrogate-interventional data to predict a conditional interventional distribution.([Abstract, p.1](https://arxiv.org/pdf/2609.39523v1#page=1 "This work studies CFMs as a method to combine finite observational and surrogate-interventional datasets in order to predict a target conditional interventional distribution (CID) more accurately than with observational data alone."))
- **c2** Results show strong CID prediction and that experimental context can improve over observational data alone.([Abstract, p.1](https://arxiv.org/pdf/2609.39523v1#page=1 "Our results demonstrate strong CID prediction performance and show that incorporating experimental context can improve predictions over observational data alone."))
- **c3** Because external CFMs are misspecified for this setting, the primary control is CIDER-FM-Obs, trained on the same prior with observational context only.([Experiments, p.6](https://arxiv.org/pdf/2609.39523v1#page=6 "Given the misspecification affecting external CFMs in our setting (Appendix D), we use CIDER-FM-Obs as our primary matched control."))
- **c4** The Do-PFN comparison is under treatment-domain misspecification (binary-treatment checkpoint given continuous treatments).([Appendix, p.21](https://arxiv.org/pdf/2609.39523v1#page=21 "Consequently, this comparison evaluates Do-PFN under treatment-domain misspecification."))
- **c5** Limitation: evaluation is limited to graphs with at most ten variables due to compute.([Discussion, limitations and outlook, p.9](https://arxiv.org/pdf/2609.39523v1#page=9 "Due to limited available computational resources, our current evaluation is limited to graphs with at most ten variables and does not yet establish how the approach scales to larger systems."))
- **c6** Experiments use one intervention target per regime and assume all regimes share population and non-intervened mechanisms.([Discussion, limitations and outlook, p.9](https://arxiv.org/pdf/2609.39523v1#page=9 "Although the proposed input representation supports simultaneous interventions on multiple variables, our experiments use only one intervention target per regime and assume that all regimes share the same population and non-intervened mechanisms."))

