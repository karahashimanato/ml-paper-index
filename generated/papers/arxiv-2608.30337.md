<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Coarse composition suffices: tabular in-context learning for multi-activity antimicrobial peptide profiling

- カード: [`arxiv-2608.30337`](../../papers/arxiv-2608.30337.yaml)
- 著者: Anuj Pal, Raunak Kumar, Dhruvi Solanki, Parikshit Pareek, Juhi Singh, Jitin Singla
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.30337v2)(arXiv v2、カード作成時に読んだ版)
- タグ: in-context-learning, tabular-classification, tabular-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** A sequence-only pipeline of 330 interpretable descriptors with TabPFN, without gradient training or hyperparameter search, is reported to match and surpass multimodal structure-conditioned deep models on ESCAPE.([Abstract, p.1](https://arxiv.org/pdf/2608.30337v2#page=1 "We show that a simple, sequence-only pipeline can match and surpass these methods by combining 330 interpretable sequence descriptors with TabPFN, a tabular foundation model that performs in-context prediction in a single forward pass without gradient-based training or hyperparameter search."))
- **c2** The gains persist under the prior state of the art's single-fold training protocol and are largest for remote homologues.([Abstract, p.1](https://arxiv.org/pdf/2608.30337v2#page=1 "The gains persist under the prior state-of-the-art single-fold training protocol, indicating they are not a training-set-size artefact, and are largest for remote homologues (+11.2 points below 30% sequence identity)."))
- **c3** No hyperparameter was tuned on ESCAPE at any stage.([Experimental setup, p.4](https://arxiv.org/pdf/2608.30337v2#page=4 "No hyperparameter was tuned on ESCAPE at any stage."))
- **c4** For a paired comparison, the released ESCAPE baseline checkpoints were re-run without retraining.([ESCAPE baseline re-run and matched-protocol evaluation, p.6](https://arxiv.org/pdf/2608.30337v2#page=6 "For a paired comparison, we re-ran the released ESCAPE baseline checkpoints (Best_model_Fold1.pth, Best_model_Fold2.pth) on our hardware without any retraining."))
- **c5** Honest F1 uses per-label thresholds chosen on out-of-fold predictions over the in-context set and frozen before testing; Max-F1, with thresholds chosen on the test set, is reported only as an optimistic upper bound.([Supplementary (threshold metrics), p.22](https://arxiv.org/pdf/2608.30337v2#page=22 "Honest F1 uses per-label thresholds selected on 5-fold out-of-fold predictions over the in-context set and frozen before the test set is touched."))
- **c6** Stated limitations: antiparasitic activity is too sparse for firm conclusions, and homology is handled by stratification on the predefined split rather than holding out identity clusters.([Discussion (limitations), p.17](https://arxiv.org/pdf/2608.30337v2#page=17 "Homology is handled by stratification on the predefined split rather than by holding out entire identity clusters."))

