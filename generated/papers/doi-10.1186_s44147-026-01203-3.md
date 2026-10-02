<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Interpretable TabPFN-Based prediction of unconfined compressive strength in chemically stabilized soft soils for transportation subgrade applications

- カード: [`doi-10.1186_s44147-026-01203-3`](../../papers/doi-10.1186_s44147-026-01203-3.yaml)
- 著者: Quynh-Anh Thi Bui, Son Hoang Trinh, Khoa Minh Nguyen
- 年・掲載: 2026 Journal of Engineering and Applied Science
- 原論文: [PDF](https://link.springer.com/content/pdf/10.1186/s44147-026-01203-3.pdf)(Publisher PDF via OpenAlex (publishedVersion)、カード作成時に読んだ版)
- タグ: feature-attribution, gradient-boosted-trees, in-context-learning, kernel-methods, random-forests, supervised, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The study develops an interpretable TabPFN-based framework for preliminary prediction of unconfined compressive strength of stabilized soft soils from the Mekong Delta.([Abstract, p.1](https://link.springer.com/content/pdf/10.1186/s44147-026-01203-3.pdf#page=1 "This study develops an interpretable Tabular Prior-data Fitted Network (TabPFN)-based framework for preliminary UCS prediction of stabilized soft soils from the Mekong Delta, Vietnam."))
- **c2** TabPFN is used with its default configuration and compared with SVR, k-nearest neighbors, Random Forest and CatBoost, each tuned with GridSearchCV.([Abstract, p.1](https://link.springer.com/content/pdf/10.1186/s44147-026-01203-3.pdf#page=1 "TabPFN was applied using its default configuration and compared with four GridSearchCV-optimized models: support vector regression, k-nearest neighbors, Random Forest, and CatBoost."))
- **c3** Evaluation uses an 80/20 train-test split plus five-fold cross-validation on the development part; the dataset has 168 observations with seven predictors.([Abstract, p.1](https://link.springer.com/content/pdf/10.1186/s44147-026-01203-3.pdf#page=1 "Performance was assessed using an 80/20 train–test split and five-fold cross-validation, while SHAP and partial dependence plots were used for interpretation."))
- **c4** Grid search for the baselines minimizes RMSE within the development subset using five-fold cross-validation with fold assignments shared across models.([Methodology, p.10](https://link.springer.com/content/pdf/10.1186/s44147-026-01203-3.pdf#page=10 "RMSE was used as the optimization criterion because it penalizes larger prediction errors more strongly, while final model assessment incorporated multiple complementary regression metrics."))
- **c5** TabPFN had the strongest observed test performance among the five models evaluated.([Abstract, p.1](https://link.springer.com/content/pdf/10.1186/s44147-026-01203-3.pdf#page=1 "TabPFN achieved the strongest observed test performance among the five evaluated models"))
- **c6** The 34-observation hold-out test set comes from the same experimental database, so it is not independent external validation.([Discussion, p.22](https://link.springer.com/content/pdf/10.1186/s44147-026-01203-3.pdf#page=22 "Although the independent test subset was excluded from all model development and contained 34 observations reserved for final evaluation, these observations were drawn from the same experimental database and therefore do not constitute independent external validation."))

