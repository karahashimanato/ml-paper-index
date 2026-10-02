<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Provenance Guided Incremental Learning Under Evolving Concept Definitions

- カード: [`arxiv-2608.23893`](../../papers/arxiv-2608.23893.yaml)
- 著者: Ismail Lamaakal
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.23893v1)(arXiv v1、カード作成時に読んだ版)
- タグ: gradient-boosted-trees, graph-node-prediction, stream-classification, streaming, supervised, tabular-classification, tabular-mlp, window-based-drift-detectors
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The paper proposes a provenance-guided incremental learning framework for explicitly revised concept definitions, which localizes the records that need relabeling.([Abstract, p.1](https://arxiv.org/pdf/2608.23893v1#page=1 "We introduce a provenance-guided incremental learning framework that compiles consecutive concept definitions into a structured rule delta, traces the changed components through historical provenance"))
- **c2** It introduces RuleShift-Bench, where concept shifts are controlled rule revisions over financial, demographic, cybersecurity and graph data (so the shift points are known by construction).([Abstract, p.1](https://arxiv.org/pdf/2608.23893v1#page=1 "We also introduce RuleShift-Bench, spanning financial, demographic, cybersecurity, and graph-structured data with threshold, predicate, logical, relational, recurring, and mixed concept revisions."))
- **c3** Main empirical claim on cost: provenance-guided repair has a much lower average update latency than complete relabeling and retraining.([Abstract, p.1](https://arxiv.org/pdf/2608.23893v1#page=1 "Its average update latency is 179 s compared with 993 s for complete relabeling and retraining."))
- **c4** Rule thresholds, predicate statistics and provenance structures are built from the training partition only (temporal or official splits with a validation partition).([Experimental setup, p.10](https://arxiv.org/pdf/2608.23893v1#page=10 "All rule thresholds, predicate statistics, and provenance structures are constructed using training data only."))
- **c5** An ADWIN-triggered adaptation pipeline is included as a representative drift-detection baseline; its ADWIN parameter settings were not found in the text.([Comparison Methods, p.10](https://arxiv.org/pdf/2608.23893v1#page=10 "We further include an ADWIN-triggered adaptation pipeline as a representative drift-detection baseline."))
- **c6** Limitation: the benefit decreases when revisions are global, provenance is incomplete, definitions are not fully executable, or relational/graph dependencies enlarge the candidate region.([Conclusion, p.13](https://arxiv.org/pdf/2608.23893v1#page=13 "Its main limitations arise when concept revisions are global, historical provenance is incomplete, concept definitions are not fully executable, or highly coupled relational and graph dependencies enlarge the candidate region, in which cases the benefit of selective maintenance decreases."))

