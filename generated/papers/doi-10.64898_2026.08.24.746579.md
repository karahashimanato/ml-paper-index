<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# DeMoP: A Language-Model-Guided Mixture-of-Experts Framework for Cancer Prognosis

- カード: [`doi-10.64898_2026.08.24.746579`](../../papers/doi-10.64898_2026.08.24.746579.yaml)
- 著者: Chen Tang, Lei Yu, Qiwei Li, Lin Xu
- 年・掲載: 2026 bioRxiv (Cold Spring Harbor Laboratory)
- 原論文: [PDF](https://www.biorxiv.org/content/biorxiv/early/2026/08/27/2026.08.24.746579.full.pdf)(Publisher PDF via OpenAlex (acceptedVersion)、カード作成時に読んだ版)
- タグ: deep-learning, supervised, tabular-classification
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** DeMoP serializes structured patient profiles (clinical variables, copy-number alterations, gene descriptions) as natural-language sequences and learns prognostic representations from them.([Abstract, p.2](https://www.biorxiv.org/content/biorxiv/early/2026/08/27/2026.08.24.746579.full.pdf#page=2 "we present DeMoP, a language-model-guided mixture-of-experts framework that serializes"))
- **c2** Main claim: on held-out tests in two pan-cancer cohorts (GENIE and TCGA), DeMoP outperformed the conventional machine-learning and deep-learning baselines that were evaluated.([Abstract, p.2](https://www.biorxiv.org/content/biorxiv/early/2026/08/27/2026.08.24.746579.full.pdf#page=2 "GENIE (63,090 patients) and TCGA (4,123 patients), DeMoP outperformed the conventional"))
- **c3** Protocol: within each cohort, DeMoP is trained on 80% and evaluated on the remaining 20% held-out internal test set (single split; no cross-validation described).([Results (GENIE cohort), p.6](https://www.biorxiv.org/content/biorxiv/early/2026/08/27/2026.08.24.746579.full.pdf#page=6 "DeMoP using 80% of the GENIE cohort and evaluated it on the remaining 20% held-out internal"))
- **c4** The baselines (logistic regression, random forest, XGBoost, MLP, CNN, LSTM) used default parameter settings, evaluated on the same training and test sets as DeMoP; no tuning of baselines is described.([Results (GENIE cohort), p.6](https://www.biorxiv.org/content/biorxiv/early/2026/08/27/2026.08.24.746579.full.pdf#page=6 "default parameter settings: logistic regression (0.51), random forest (0.58), XGBoost (0.66),"))
- **c5** Cross-cohort evaluation: a GENIE-trained model was applied directly to the full filtered TCGA cohort.([Results (cross-cohort transfer), p.9](https://www.biorxiv.org/content/biorxiv/early/2026/08/27/2026.08.24.746579.full.pdf#page=9 "and evaluated it directly on the full filtered TCGA cohort (n = 4,123). The overall class-1 F1 score"))
- **c6** Limitation: serializing structured patient features as text may obscure some fine-grained quantitative relationships.([Discussion (limitations), p.12](https://www.biorxiv.org/content/biorxiv/early/2026/08/27/2026.08.24.746579.full.pdf#page=12 "serializing structured patient features as natural-language sequences may obscure some fine-"))

