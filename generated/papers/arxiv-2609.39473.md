<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Beyond the Shadows of Plato's Cave: Evaluating False Memory in Autonomous Agents via Counterfactual Reasoning

- カード: [`arxiv-2609.39473`](../../papers/arxiv-2609.39473.yaml)
- 著者: Quan M. Tran, Zhuo Huang, Zhen Fang, Jing Zhang, Mingming Gong, Tongliang Liu
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.39473v1)(arXiv v1、カード作成時に読んだ版)
- タグ: dataset-shift-detection, in-context-learning, large-language-models, post-hoc
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** FAME evaluates false memory in agents by tracking how internal beliefs change under counterfactual reasoning, without training.([Abstract, p.1](https://arxiv.org/pdf/2609.39473v1#page=1 "Therefore, we propose FAME, a training-free framework that evaluates false memory through the evolution of agent beliefs under counterfactual reasoning."))
- **c2** Main claim: monitoring answers alone often fails to detect false memory, while FAME achieves high AUROC across the false-memory settings.([Abstract, p.1](https://arxiv.org/pdf/2609.39473v1#page=1 "Empirical experiments reveal that simply monitoring answers often fails to detect false memory, while FAME achieves AUROCs of 76.2% – 96.7% across false-memory settings"))
- **c3** Ground truth: false-memory labels are derived from correct operations/answers (GSM), applied library syntax (GitChameleon) and final answers (BBH); they are used only for evaluation.([Appendix (Evaluation metric), p.20](https://arxiv.org/pdf/2609.39473v1#page=20 "To construct the ground-truth labels, we leverage the arithmetic operations and final answers in GSM, the syntax of the applied functions or libraries in Git, and the final answers in BBH."))
- **c4** Decision rule: the authors state that in practice FAME only needs a threshold on the normalized projection of the concept drift, while the reported metric (AUROC) is threshold-free.([Appendix (Evaluation metric), p.20](https://arxiv.org/pdf/2609.39473v1#page=20 "In practice, FAME requires no such ground-truth labels; thresholding the normalized projection of the concept drift onto the readout direction is sufficient for distinguishing faithful from false memories, as described in Alg. 1."))
- **c5** Realistic-benchmark baselines are representation/uncertainty signals (input similarity, surface layer, logit confidence, task and function vectors, EigenScore, ContextCite, entity-aware probe), not drift detectors.([Real-World Evaluations, p.8](https://arxiv.org/pdf/2609.39473v1#page=8 "We compare FAME with the following baselines: Input similarity [50], Surface, Logit confidence, Task vector [40], Function vector [41], EigenScore from INSIDE [53], ContextCite [54], Entity-aware probe [25]."))
- **c6** Limitation: FAME requires access to the agent's hidden states and to counterfactual queries.([Conclusion, p.9](https://arxiv.org/pdf/2609.39473v1#page=9 "Although promising, FAME requires access to agent hidden states and counterfactual queries."))

