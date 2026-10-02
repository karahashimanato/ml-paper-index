<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# When and Why LLM Causal Priors Help: Closed-Loop Prior Selection for Amortized Causal Inference

- カード: [`arxiv-2609.06941`](../../papers/arxiv-2609.06941.yaml)
- 著者: Haohao Zhou
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.06941v1)(arXiv v1、カード作成時に読んだ版)
- タグ: causal-effect-estimation, in-context-learning, large-language-models, tabular-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** On a 7.34M-parameter Do-PFN, the selected prior gives a significant gain on the primary evaluation domain (5 paired seeds), with error below the uninjected official base.([Abstract, p.1](https://arxiv.org/pdf/2609.06941v1#page=1 "On a 7.34M-parameter Do-PFN, the framework’s winner attains a formally significant 2.75× gain on the primary evaluation domain (n = 5 paired seeds, p = 0.0086), and its error falls below that of the uninjected official base."))
- **c2** The comparison with the official base is only descriptive: the winner is built on a locally retrained base and the official base is not part of the paired test.([Abstract, p.1](https://arxiv.org/pdf/2609.06941v1#page=1 "Because the winner is built on a locally retrained base and the official base is not part of the paired test, this is a descriptive cross-lineage comparison."))
- **c3** Injection gives significant gains only when the base is underfit on the task domain, the prior domain matches the task domain, and the task lies within the support of the base's training prior.([Abstract, p.1](https://arxiv.org/pdf/2609.06941v1#page=1 "injection yields significant gains only when the base is underfit on the task domain, the prior domain matches the task domain, and the task lies within the support of the base’s training prior."))
- **c4** The primary and adjacent evaluation domains are synthetic/proprietary causal benchmarks whose generation mechanism and release policy are not yet stated.([Reproducibility Statement, p.25](https://arxiv.org/pdf/2609.06941v1#page=25 "The primary domain law_race and the adjacent domain sales are synthetic/proprietary causal benchmarks with ground-truth graphs; their generation mechanism and release policy will be stated in the released materials."))
- **c5** Baselines (CausalPFN and classical estimators such as S/T/X/DR-learners and CausalForestDML) are run under the same 5-fold split and protocol; baseline hyperparameter tuning was not found in the text.([External validity, p.19](https://arxiv.org/pdf/2609.06941v1#page=19 "On our two domains, we compare against the direct SOTA (CausalPFN [3]) and a classical-estimator panel (S/T/X/DR-learner [13, 11], CausalForestDML [2], naive ATE) under the same 5-fold split and the same protocol as model training."))
- **c6** On standard causal benchmarks (IHDP, Lalonde), the injection method is not superior to, and often worse than, existing methods.([Discussion, p.23](https://arxiv.org/pdf/2609.06941v1#page=23 "We state plainly: on standard causal benchmarks, our injection method is not superior to, and is often inferior to, existing methods."))

