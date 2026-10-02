<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Concept Drift from a Causal Perspective

- カード: [`arxiv-2609.25340`](../../papers/arxiv-2609.25340.yaml)
- 著者: Eduardo V. L. Barboza, Jean Paul Barddal, Robert Sabourin, Rafael M. O. Cruz
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.25340v1)(arXiv v1、カード作成時に読んだ版)
- タグ: concept-drift-detection, error-rate-drift-detectors, stream-classification, streaming, supervised, tabular-data-generation, tabular-foundation-model, tree-ensembles
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The paper proposes a taxonomy that categorizes drift events by their causal origin within a structural causal model.([Abstract, p.1](https://arxiv.org/pdf/2609.25340v1#page=1 "We propose a taxonomy that categorizes drift events by their causal origin, including changes in exogenous variables, endogenous mechanisms, confounders, and target-generating processes."))
- **c2** Main empirical claim: drifts with different causal origins induce distinct patterns of distribution shift and predictive behavior.([Abstract, p.1](https://arxiv.org/pdf/2609.25340v1#page=1 "Our experiments empirically characterize the distributional effects of each drift type and show that drifts with different causal origins induce distinct patterns of distribution shift and predictive behavior."))
- **c3** Ground-truth drift is synthetic: CaDrift streams are generated with drift events at known, regular positions (abrupt unless stated otherwise).([Experimental setup (Distributional impact analysis), p.11](https://arxiv.org/pdf/2609.25340v1#page=11 "For this analysis, we generate streams of 20,000 samples with a drift event introduced every 2,000 samples."))
- **c4** Performance protocol: a Hoeffding Tree is evaluated test-then-train with immediate labels and with labels delayed by 100 samples, and is also coupled with DDM; DDM parameter settings were not found in the text.([Experimental setup (Performance evaluation), p.12](https://arxiv.org/pdf/2609.25340v1#page=12 "we measure the predictive performance of the Hoeffding Tree (HT) classifier (Domingos & Hulten, 2000) under different drift scenarios in a test-then-train manner, considering a prompt label availability after the test, as well as when label availability is delayed by 100 samples"))
- **c5** Under endogenous drift with nonlinear mappers, DDM does not seem to help the Hoeffding Tree; its triggers appear to lower immediate accuracy more than not using DDM.([Results (impact of causal drift events), p.12](https://arxiv.org/pdf/2609.25340v1#page=12 "DDM does not seem to provide any advantage over the HT – the triggers in concept drift actually seem to decrease the immediate accuracy more than if not using DDM."))
- **c6** Case study: CaDrift samples generated from a DAG inferred on ELEC2 are used to augment stream learners, including TabPFNv2.5 run with a sliding context window.([Case study (ELEC2 data augmentation), p.22](https://arxiv.org/pdf/2609.25340v1#page=22 "In addition to the online learners, we also include TabPFNv2.5 (Grinsztajn et al., 2026), a transformer-based tabular classifier."))

