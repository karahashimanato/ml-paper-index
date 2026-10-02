<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# PhenoBench: Mapping What a Deeply Phenotyped Human Cohort Can Tell Us

- カード: [`arxiv-2609.06080`](../../papers/arxiv-2609.06080.yaml)
- 著者: Gal Sapir, Alon Diament, Adva Wolf, Doron Yaya-Stupp, Dikla Gelbard Solodkin, Dana Azouri, Anat Etzion-Fuchs, Guy Lutsker, Eran Segal, Hagai Rossman
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.06080v2)(arXiv v2、カード作成時に読んだ版)
- タグ: gradient-boosted-trees, in-context-learning, linear-models, supervised, tabular-foundation-model, tabular-mlp, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** PhenoBench is a versioned collection of clinically grounded tasks with human-readable Task Cards and executable evaluation contracts.([Introduction, p.2](https://arxiv.org/pdf/2609.06080v2#page=2 "PhenoBench contributes a versioned collection of 90 clinically grounded tasks across 15 domains and 26 input modalities, with human-readable Task Cards and executable evaluation contracts."))
- **c2** Under a fixed single-estimator protocol with bounded tuning, the pretrained tabular models ranked above the evaluated task-specific baselines, including XGBoost and CatBoost, in aggregate.([Abstract, p.1](https://arxiv.org/pdf/2609.06080v2#page=1 "Under a fixed single-estimator protocol with bounded tuning, these models ranked above the evaluated task-specific baselines, including XGBoost and CatBoost, in aggregate."))
- **c3** The XGBoost and CatBoost grids were fixed before the matched comparison, selected by five-fold cross-validation within the training split, and evaluated once on the held-out test split.([Appendix (method configurations), p.15](https://arxiv.org/pdf/2609.06080v2#page=15 "The XGBoost and CatBoost grids were fixed before their matched campaign, selected by five-fold cross-validation within the training split, and evaluated once on the held-out test split."))
- **c4** The tabular comparison uses a single-estimator CPU float32 protocol rather than each model's strongest recommended ensemble.([Limitations, p.9](https://arxiv.org/pdf/2609.06080v2#page=9 "The tabular comparison evaluates a single-estimator CPU float32 protocol, not each model’s strongest recommended ensemble."))
- **c5** XGBoost and CatBoost received the same bounded 12-candidate tuning budget rather than exhaustive library-specific optimization, so the small average gains do not settle the best attainable performance of either model family.([Limitations, p.9](https://arxiv.org/pdf/2609.06080v2#page=9 "XGBoost and CatBoost used the same bounded 12-candidate tuning budget rather than exhaustive library-specific optimization."))
- **c6** Competing interests: seven authors are employees of Pheno.AI Ltd., and Eran Segal is a paid consultant of Pheno.AI Ltd.([Competing interests, p.10](https://arxiv.org/pdf/2609.06080v2#page=10 "Gal Sapir, Alon Diament, Adva Wolf, Dikla Gelbard Solodkin, Dana Azouri, Anat Etzion-Fuchs, and Hagai Rossman are employees of Pheno.AI Ltd."))

