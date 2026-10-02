<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# iStructTab: Structured Feature Sequencing for Multimodal Learning of Image and Tabular Data

- カード: [`arxiv-2608.04348`](../../papers/arxiv-2608.04348.yaml)
- 著者: Al Zadid Sultan Bin Habib, Md Younus Ahamed, Prashnna Gyawali, Gianfranco Doretto, Donald A. Adjeroh
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.04348v1)(arXiv v1、カード作成時に読んだ版)
- タグ: deep-learning, supervised, tabular-attention, tabular-classification
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** GEDS is a feature-sequencing algorithm based on the Column Permutation Problem, used for image-tabular fusion.([Abstract, p.1](https://arxiv.org/pdf/2608.04348v1#page=1 "To tackle this challenge, we introduce Graph-Enhanced Descriptor Sequencing (GEDS), a structured feature sequencing algorithm grounded in principles from the Column Permutation Problem (CPP)."))
- **c2** Across six image-tabular benchmarks, iStructTab improves over concatenation and state-of-the-art baselines.([Conclusion, p.10](https://arxiv.org/pdf/2608.04348v1#page=10 "Across six benchmarks, iStructTab improves over concatenation and strong state-of-the-art baselines."))
- **c3** Evaluation uses six image-tabular datasets with stratified 64/16/20 splits, reporting test accuracy, average rank and regret.([Experiments and Results, p.6](https://arxiv.org/pdf/2608.04348v1#page=6 "We use stratified 64/16/20 train/validation/test splits and report test accuracy, average rank and regret (Table 1), noise robustness (Table 2), and efficiency (Fig. 2)."))
- **c4** Tuning is asymmetric: iStructTab is tuned with Optuna for 20 trials per dataset, while baselines use recommended settings.([Implementation Details, p.6](https://arxiv.org/pdf/2608.04348v1#page=6 "We tune iStructTab with Optuna [1] for 20 trials per dataset, following common tabular tuning practice [27, 26, 25, 24]; baselines use recommended settings."))
- **c5** Deep tabular baselines (TabSeq, TabM, SAINT, SCARF) use a single shared configuration per model family without dataset-specific tuning.([Appendix, p.15](https://arxiv.org/pdf/2608.04348v1#page=15 "For the deep baselines, we employ early stopping on validation performance and avoid dataset-specific hyperparameter tuning beyond a single, shared configuration per model family."))
- **c6** The authors state that this baseline design ensures the reported gains are not artifacts of unequal tuning effort.([Appendix, p.15](https://arxiv.org/pdf/2608.04348v1#page=15 "This design keeps the comparison focused on intrinsic modeling differences, ensuring that the reported gains of iStructTab over these baselines are not artifacts of unequal tuning effort."))

