<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# 索引

## タグ別のカード

### tasks

- **tabular-classification**: [arxiv-2106.03253](papers/arxiv-2106.03253.md), [arxiv-2106.11959](papers/arxiv-2106.11959.md), [arxiv-2207.08815](papers/arxiv-2207.08815.md)
- **tabular-regression**: [arxiv-2106.03253](papers/arxiv-2106.03253.md), [arxiv-2106.11959](papers/arxiv-2106.11959.md), [arxiv-2207.08815](papers/arxiv-2207.08815.md)

### method_families

- **gradient-boosted-trees**: [arxiv-2106.03253](papers/arxiv-2106.03253.md), [arxiv-2106.11959](papers/arxiv-2106.11959.md), [arxiv-2207.08815](papers/arxiv-2207.08815.md)
- **random-forests**: [arxiv-2207.08815](papers/arxiv-2207.08815.md)
- **tabular-mlp**: [arxiv-2106.11959](papers/arxiv-2106.11959.md), [arxiv-2207.08815](papers/arxiv-2207.08815.md)
- **tabular-attention**: [arxiv-2106.03253](papers/arxiv-2106.03253.md), [arxiv-2106.11959](papers/arxiv-2106.11959.md), [arxiv-2207.08815](papers/arxiv-2207.08815.md)
- **differentiable-trees**: [arxiv-2106.03253](papers/arxiv-2106.03253.md), [arxiv-2106.11959](papers/arxiv-2106.11959.md)
- **tabular-cnn**: [arxiv-2106.03253](papers/arxiv-2106.03253.md)
- **heterogeneous-ensembles**: [arxiv-2106.03253](papers/arxiv-2106.03253.md)

### paradigms

- **supervised**: [arxiv-2106.03253](papers/arxiv-2106.03253.md), [arxiv-2106.11959](papers/arxiv-2106.11959.md), [arxiv-2207.08815](papers/arxiv-2207.08815.md)

## 比較条件

| id | scope | task | dataset | 定義した論文 | 結果・勝敗の数 |
|---|---|---|---|---|---|
| `shwartzziv2021-rossmann` | paper-private | tabular-regression | Rossmann Store Sales | arxiv-2106.03253 | 8 |
| `shwartzziv2021-covertype` | paper-private | tabular-classification | Forest Cover Type | arxiv-2106.03253 | 8 |
| `shwartzziv2021-higgs` | paper-private | tabular-classification | Higgs Boson | arxiv-2106.03253 | 8 |
| `shwartzziv2021-gas-concentrations` | paper-private | tabular-classification | Gas Concentrations (OpenML 1477) | arxiv-2106.03253 | 8 |
| `shwartzziv2021-eye-movements` | paper-private | tabular-classification | Eye Movements (OpenML 1044) | arxiv-2106.03253 | 8 |
| `shwartzziv2021-gesture-phase` | paper-private | tabular-classification | Gesture Phase (OpenML 4538) | arxiv-2106.03253 | 8 |
| `shwartzziv2021-yearprediction` | paper-private | tabular-regression | YearPrediction MSD | arxiv-2106.03253 | 8 |
| `shwartzziv2021-mslr-web10k` | paper-private | tabular-classification | Microsoft MSLR-WEB10K | arxiv-2106.03253 | 8 |
| `shwartzziv2021-epsilon` | paper-private | tabular-classification | Epsilon (PASCAL 2008) | arxiv-2106.03253 | 8 |
| `shwartzziv2021-shrutime` | paper-private | tabular-classification | Shrutime (Kaggle churn modelling) | arxiv-2106.03253 | 8 |
| `shwartzziv2021-blastchar` | paper-private | tabular-classification | Blastchar (Telco customer churn) | arxiv-2106.03253 | 8 |
| `shwartzziv2021-unseen-average` | paper-private | tabular-classification | Aggregate over each model's unseen datasets (the 11 datasets minus those in the model's original paper) | arxiv-2106.03253 | 8 |
| `gorishniy2021-ca-single` | paper-private | tabular-regression | California Housing | arxiv-2106.11959 | 10 |
| `gorishniy2021-ca-ensemble` | paper-private | tabular-regression | California Housing | arxiv-2106.11959 | 8 |
| `gorishniy2021-ad-single` | paper-private | tabular-classification | Adult | arxiv-2106.11959 | 9 |
| `gorishniy2021-ad-ensemble` | paper-private | tabular-classification | Adult | arxiv-2106.11959 | 8 |
| `gorishniy2021-he-single` | paper-private | tabular-classification | Helena | arxiv-2106.11959 | 9 |
| `gorishniy2021-he-ensemble` | paper-private | tabular-classification | Helena | arxiv-2106.11959 | 8 |
| `gorishniy2021-ja-single` | paper-private | tabular-classification | Jannis | arxiv-2106.11959 | 9 |
| `gorishniy2021-ja-ensemble` | paper-private | tabular-classification | Jannis | arxiv-2106.11959 | 8 |
| `gorishniy2021-hi-single` | paper-private | tabular-classification | Higgs Small (OpenML, 98K) | arxiv-2106.11959 | 10 |
| `gorishniy2021-hi-ensemble` | paper-private | tabular-classification | Higgs Small (OpenML, 98K) | arxiv-2106.11959 | 8 |
| `gorishniy2021-al-single` | paper-private | tabular-classification | ALOI | arxiv-2106.11959 | 9 |
| `gorishniy2021-al-ensemble` | paper-private | tabular-classification | ALOI | arxiv-2106.11959 | 6 |
| `gorishniy2021-ep-single` | paper-private | tabular-classification | Epsilon | arxiv-2106.11959 | 9 |
| `gorishniy2021-ep-ensemble` | paper-private | tabular-classification | Epsilon | arxiv-2106.11959 | 8 |
| `gorishniy2021-ye-single` | paper-private | tabular-regression | Year (YearPrediction MSD) | arxiv-2106.11959 | 10 |
| `gorishniy2021-ye-ensemble` | paper-private | tabular-regression | Year (YearPrediction MSD) | arxiv-2106.11959 | 8 |
| `gorishniy2021-co-single` | paper-private | tabular-classification | Covertype | arxiv-2106.11959 | 9 |
| `gorishniy2021-co-ensemble` | paper-private | tabular-classification | Covertype | arxiv-2106.11959 | 8 |
| `gorishniy2021-ya-single` | paper-private | tabular-regression | Yahoo LTR (pointwise regression) | arxiv-2106.11959 | 9 |
| `gorishniy2021-ya-ensemble` | paper-private | tabular-regression | Yahoo LTR (pointwise regression) | arxiv-2106.11959 | 8 |
| `gorishniy2021-mi-single` | paper-private | tabular-regression | Microsoft MSLR-WEB10K (pointwise regression) | arxiv-2106.11959 | 10 |
| `gorishniy2021-mi-ensemble` | paper-private | tabular-regression | Microsoft MSLR-WEB10K (pointwise regression) | arxiv-2106.11959 | 8 |
| `gorishniy2021-avg-rank-single` | paper-private | tabular-classification | Average over the 11 datasets of Table 2 (classification and regression) | arxiv-2106.11959 | 9 |
| `grinsztajn2022-medium-num-clf` | public | tabular-classification | Grinsztajn et al. medium-sized benchmark, numerical features, classification (15 datasets) | arxiv-2207.08815 | 1 |
| `grinsztajn2022-medium-num-reg` | public | tabular-regression | Grinsztajn et al. medium-sized benchmark, numerical features, regression (19 datasets) | arxiv-2207.08815 | 1 |
| `grinsztajn2022-medium-cat-clf` | public | tabular-classification | Grinsztajn et al. medium-sized benchmark, numerical + categorical features, classification (7 datasets) | arxiv-2207.08815 | 1 |
| `grinsztajn2022-medium-cat-reg` | public | tabular-regression | Grinsztajn et al. medium-sized benchmark, numerical + categorical features, regression (14 datasets) | arxiv-2207.08815 | 1 |
