<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Machine Learning-Based Prediction of Cycloplegic Refraction Using the Eyerobo Vision Screener: Design—A Cross-Sectional Comparative Device Study

- カード: [`doi-10.1007_s40123-026-01482-2`](../../papers/doi-10.1007_s40123-026-01482-2.yaml)
- 著者: Mengmeng Xia, Boxue Yao, Yumei Wang, Fengwei Liang, Wuxia Zhao, Li Qin, Shoukuan Liu, Muhammad Usama, Zhihui Zhang, Wu Guo, Emmanuel Eric Pazo, Xinjun Ren
- 年・掲載: 2026 Ophthalmology and Therapy
- 原論文: [PDF](https://link.springer.com/content/pdf/10.1007/s40123-026-01482-2.pdf)(Publisher PDF via OpenAlex (publishedVersion)、カード作成時に読んだ版)
- タグ: gradient-boosted-trees, in-context-learning, kernel-methods, linear-models, random-forests, supervised, tabular-foundation-model, tabular-mlp, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Data and protocol: 1129 eyes of 574 patients aged 6-18; TabPFN (no hyperparameter tuning) evaluated alongside seven conventional ML algorithms with patient-level five-fold grouped cross-validation repeated over three random seeds.([Abstract, p.1](https://link.springer.com/content/pdf/10.1007/s40123-026-01482-2.pdf#page=1 "TabPFN, a tabular foundation model requiring no hyperparameter tuning, was evaluated alongside seven conventional machine-learning algorithms using patient-level five-fold grouped cross-validation repeated over three random"))
- **c2** Tuning: all gradient-boosting baselines (XGBoost, LightGBM, CatBoost) used default hyperparameters without per-dataset tuning, to match TabPFN's zero-tuning design; the authors note tuning may narrow the margin.([Machine Learning Models, p.10](https://link.springer.com/content/pdf/10.1007/s40123-026-01482-2.pdf#page=10 "All gradient-boosting models used default hyperparameters without per-dataset tuning to ensure a fair comparison with TabPFN's zero-tuning design"))
- **c3** TabPFN had the lowest MAE on all Eyerobo scenarios and was competitive with Ridge on auto-refractor scenarios.([Abstract, p.2](https://link.springer.com/content/pdf/10.1007/s40123-026-01482-2.pdf#page=2 "TabPFN achieved the lowest mean absolute error (MAE) on all Eyerobo scenarios and was competitive with Ridge on auto-refractor scenarios"))
- **c4** Screening thresholds: a Youden-optimal cutoff was selected on each training fold, and the cross-validation-averaged cutoff was used as the reported operating point.([Screening-oriented classification analysis, p.11](https://link.springer.com/content/pdf/10.1007/s40123-026-01482-2.pdf#page=11 "A noncycloplegic Youden-optimal cutoff was selected on each training fold and the cross-validation-averaged cutoff was used as the reported operating point."))
- **c5** The authors say the modest margin over linear and gradient-boosting baselines and the lack of external validation preclude recommending TabPFN as the definitive algorithm.([Conclusions, p.2](https://link.springer.com/content/pdf/10.1007/s40123-026-01482-2.pdf#page=2 "the modest margin over linear and gradient-boosting baselines and the absence of external validation preclude any recommendation as the definitive algorithm of choice."))
- **c6** Main limitation: all development and evaluation used internal cross-validation within a single-center cohort.([Limitations, p.26](https://link.springer.com/content/pdf/10.1007/s40123-026-01482-2.pdf#page=26 "The most important limitation of this study is that all model development and evaluation were conducted within a single-center cohort using internal cross-validation."))

