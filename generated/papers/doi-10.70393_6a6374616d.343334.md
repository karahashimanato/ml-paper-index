<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Tabular In-Context Learning for Low-Resource Rare Industrial Fault Detection: a Cost-Sensitive Comparison on Scania APS and SECOM

- カード: [`doi-10.70393_6a6374616d.343334`](../../papers/doi-10.70393_6a6374616d.343334.yaml)
- 著者: Guoqing Song
- 年・掲載: 2026 Journal of Computer Technology and Applied Mathematics
- 原論文: [PDF](https://www.suaspress.org/ojs/index.php/JCTAM/article/download/v3n4a01/v3n4a01)(Publisher PDF via OpenAlex (publishedVersion)、カード作成時に読んだ版)
- タグ: gradient-boosted-trees, in-context-learning, linear-models, supervised, tabular-classification, tabular-foundation-model, tabular-mlp
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Scania protocol: nested stratified training samples of 5,000 and 10,000 records under five seeds; tunable models selected by out-of-fold AUPRC on shared three-fold splits; decision thresholds fixed by minimizing out-of-fold cost; the official test set stayed locked until all selections were complete.([Abstract, p.1](https://www.suaspress.org/ojs/index.php/JCTAM/article/download/v3n4a01/v3n4a01#page=1 "Shared three-fold splits supported out-of-fold (OOF) evaluation; tunable models were selected by OOF AUPRC, and decision thresholds were locked by minimizing OOF cost, defined as C = 10 × FP + 500 × FN."))
- **c2** SECOM protocol: three repeats of five-fold outer cross-validation with three-fold inner selection.([Abstract, p.1](https://www.suaspress.org/ojs/index.php/JCTAM/article/download/v3n4a01/v3n4a01#page=1 "SECOM used three repeats of five-fold outer cross-validation with three-fold inner selection."))
- **c3** Tuning budgets were unequal (TabICLv2 one fixed configuration, TabM four presets, logistic regression eight candidates, XGBoost 12 candidates), and CatBoost, LightGBM and broader tuning were not evaluated.([Limitations and threats to validity, p.8](https://www.suaspress.org/ojs/index.php/JCTAM/article/download/v3n4a01/v3n4a01#page=8 "Search budgets were also unequal: TabICLv2 used one fixed configuration, TabM four presets, logistic regression eight candidates, and XGBoost 12 candidates."))
- **c4** On the prespecified Scania design, TabICLv2 improved AUPRC, MCC, official cost and Brier score relative to XGBoost, with paired bootstrap intervals supporting all four directions.([Discussion, p.7](https://www.suaspress.org/ojs/index.php/JCTAM/article/download/v3n4a01/v3n4a01#page=7 "Under the prespecified Scania design, TabICLv2 improved AUPRC, MCC, official cost, and Brier score relative to XGBoost, with paired confidence intervals supporting all four directions."))
- **c5** In a time-ordered SECOM sensitivity analysis (few failures in the test segment), threshold transfer failed for every model; the author treats it as a robustness warning, not a ranking.([Results (temporal sensitivity on SECOM), p.7](https://www.suaspress.org/ojs/index.php/JCTAM/article/download/v3n4a01/v3n4a01#page=7 "Threshold transfer failed for every model"))
- **c6** Conclusion: the evidence supports TabICLv2 in this specific low-resource, cost-sensitive setting but does not establish universal superiority or temporal deployment validity.([Conclusion, p.8](https://www.suaspress.org/ojs/index.php/JCTAM/article/download/v3n4a01/v3n4a01#page=8 "The evidence therefore supports TabICLv2 in this specific low-resource, cost-sensitive setting but does not establish universal superiority or temporal deployment validity."))

