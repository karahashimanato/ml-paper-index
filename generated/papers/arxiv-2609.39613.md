<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Hybrid Methods for Robust Tabular Data Imputation

- カード: [`arxiv-2609.39613`](../../papers/arxiv-2609.39613.yaml)
- 著者: Jinwei Li, Michelle Bruch, Daniel Tenbrinck
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.39613v1)(arXiv v1、カード作成時に読んだ版)
- タグ: random-forests, tabular-imputation, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The paper proposes NuclearForest and SoftForest, combining nuclear-norm low-rank initialization (SVT or SoftImpute) with a non-iterative random forest refinement.([Abstract, p.1](https://arxiv.org/pdf/2609.39613v1#page=1 "In this work, we propose two hybrid imputation methods called NuclearForest and SoftForest, which combine nuclear-norm-based low-rank initialization using Singular Value Thresholding (SVT) and SoftImpute, respectively, with a non-iterative Random Forest refinement."))
- **c2** The hybrids are reported to match or exceed the imputation fidelity of iterative methods such as MissForest at lower computational cost.([Abstract, p.1](https://arxiv.org/pdf/2609.39613v1#page=1 "Our results demonstrate that NuclearForest and SoftForest match or exceed the imputation fidelity of state-of-the-art iterative methods such as MissForest, while significantly reducing computational cost."))
- **c3** Missing entries are regenerated independently over 10 repeated runs per setting.([Experiments and results, p.5](https://arxiv.org/pdf/2609.39613v1#page=5 "For each setting, missing entries are regenerated independently over 10 repeated experimental runs, ensuring different missingness masks across runs while preserving reproducibility."))
- **c4** Neural-network imputation methods are not included as primary baselines.([Experiments and results, p.5](https://arxiv.org/pdf/2609.39613v1#page=5 "Neural-network-based imputation methods are not included as primary baselines because the focus of this study is on efficient classical and hybrid tabular imputers."))
- **c5** On the metabolomics data, NuclearForest is competitive with MissForest and strong at low missing rates, while MissForest is best in several medium- and high-missingness settings.([Conclusion, p.9](https://arxiv.org/pdf/2609.39613v1#page=9 "On the former, NuclearForest remains competitive with MissForest across missingness levels and is particularly strong at low missing rates, while MissForest achieves the best performance in several medium- and high-missingness settings."))
- **c6** The gains do not fully extend to the left-censored MNAR setting, where Half-min is well aligned with the mechanism.([Conclusion, p.9](https://arxiv.org/pdf/2609.39613v1#page=9 "A limitation is that these gains do not fully extend to the left-censored MNAR setting, where Half-min is well aligned with this mechanism."))

