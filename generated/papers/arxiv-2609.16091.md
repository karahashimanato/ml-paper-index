<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Distilling Foundation Models for Agentic What-If Reasoning:Cost, Latency, and Governance in a Hybrid LLM+SLM Architecture

- カード: [`arxiv-2609.16091`](../../papers/arxiv-2609.16091.yaml)
- 著者: Sourish Dey, Aditya Kumar
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.16091v1)(arXiv v1、カード作成時に読んだ版)
- タグ: knowledge-distillation, large-language-models, model-compression, supervised, tabular-classification, tabular-foundation-model, tabular-mlp, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** A TabPFN teacher is distilled into a compact feed-forward student on a UCI Adult business-decision simulation and five OpenML datasets.([Abstract, p.1](https://arxiv.org/pdf/2609.16091v1#page=1 "We distill a TabPFN teacher into a compact feed-forward student across a business-decision simulation on UCI Adult and five OpenML benchmarks"))
- **c2** The end-to-end latency gain comes almost entirely from removing in-context TabPFN from the hot path.([Abstract, p.1](https://arxiv.org/pdf/2609.16091v1#page=1 "Span-level attribution shows that this wall-clock gain is almost entirely from removing in-context TabPFN from the hot path; fewer cloud round-trips cut token cost (2.1×) rather than latency."))
- **c3** Evaluation protocol: classification results use the default settings of the authors' scripts (no per-dataset tuning was found in the text).([Experimental setup, p.5](https://arxiv.org/pdf/2609.16091v1#page=5 "Unless a caption names an exception, every classification result in Tables 3 and 9 uses the defaults of scripts/run_distillation.py and scripts/run_classification_benchmark.py."))
- **c4** For the UCI Adult simulation, training used a row-capped stratified subsample (because of the teacher's context limit) with an 80/20 train/test split.([Experimental setup, p.5](https://arxiv.org/pdf/2609.16091v1#page=5 "Training used a stratified 10,000-row subsample (the tabular foundation-model teacher’s pretrained context window is optimized for ≤10K rows) with an 80/20 train/test split (8,000/2,000)."))
- **c5** Limitation: the regression target is synthetic (rule-simulated) with no external ground truth.([Limitations, p.10](https://arxiv.org/pdf/2609.16091v1#page=10 "max_loan is a rule-simulated target with no external ground truth; classification labels are the real Adult income indicator."))
- **c6** Limitation: distillation results come from a single seed.([Limitations, p.10](https://arxiv.org/pdf/2609.16091v1#page=10 "Distillation tables use seed 42."))

