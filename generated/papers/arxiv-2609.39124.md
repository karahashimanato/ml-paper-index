<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# CDMD: A Cross-Dataset Mixed-Type Diffusion Model for Tabular Data

- カード: [`arxiv-2609.39124`](../../papers/arxiv-2609.39124.yaml)
- 著者: Mohamed Amine Ketata, Maximilian Schambach, Stephan Günnemann
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.39124v1)(arXiv v1、カード作成時に読んだ版)
- タグ: deep-learning, tabular-attention, tabular-data-generation, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** CDMD is a tabular diffusion model trained jointly across datasets with different schemas, defining diffusion directly over the mixed-type feature space.([Abstract, p.1](https://arxiv.org/pdf/2609.39124v1#page=1 "Unlike existing cross-dataset tabular diffusion models that operate in continuous representation spaces, CDMD defines diffusion directly over the mixed-type feature space and is trained end-to-end."))
- **c2** On seven real-world datasets a single jointly trained CDMD achieves the highest average generation quality among single- and cross-dataset baselines with fewer total parameters.([Abstract, p.1](https://arxiv.org/pdf/2609.39124v1#page=1 "On seven real-world datasets, a single jointly trained CDMD achieves the highest average generation quality among strong single-dataset and cross-dataset baselines, while using substantially fewer total parameters than the collection of separately trained models."))
- **c3** Each dataset is split into equal halves (train / held-out test); utility is measured by training XGBoost on synthetic data and testing on the held-out real data, alongside fidelity and privacy-proxy metrics.([Experiments, p.7](https://arxiv.org/pdf/2609.39124v1#page=7 "Following Zhang et al. (2024), we train an XGBoost classifier or regressor on synthetic data and evaluate it on the held-out test data."))
- **c4** All baselines use their official implementations with default hyperparameters, without additional tuning.([Appendix (Baselines), p.21](https://arxiv.org/pdf/2609.39124v1#page=21 "For each baseline, we use its official implementation with the default hyperparameters, without additional tuning."))
- **c5** Evaluation protocol (constrained-generation experiment): CDMD is pre-trained on a 337-dataset corpus from which the evaluation datasets are excluded by automated checks followed by manual verification.([Experiments, p.8](https://arxiv.org/pdf/2609.39124v1#page=8 "We exclude the evaluation datasets from this corpus through automated checks followed by manual verification."))
- **c6** Limitations: adaptation relies on per-dataset fine-tuning, and experiments are limited in scale.([Conclusion, p.10](https://arxiv.org/pdf/2609.39124v1#page=10 "Our experiments are also limited in scale, leaving performance at larger scales an open question."))

