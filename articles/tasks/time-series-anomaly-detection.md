---
title: 時系列異常検知の手法比較と評価方法の問題
kind: task
tags: [time-series-anomaly-detection]
depends_on: [arxiv-2109.05257, arxiv-2009.13807, arxiv-2308.13068, arxiv-2506.18046, arxiv-2211.05244, arxiv-2608.02821, arxiv-2609.39215, arxiv-2610.01168, arxiv-2609.38004, arxiv-2609.31470, arxiv-2609.28022, arxiv-2608.01885, arxiv-2609.39489, arxiv-2609.38789, arxiv-2610.01223, arxiv-2610.00978, arxiv-2609.39337, arxiv-2609.39257, arxiv-2609.36765, arxiv-2609.29194, arxiv-2504.06643, doi-10.24963_ijcai.2026_276, doi-10.24963_ijcai.2026_332, arxiv-2402.03885]
written_at: 2026-10-03
written_by: claude-opus-5-5 via Claude Code
---

# 時系列異常検知の手法比較と評価方法の問題

<!-- generated:stale -->
> ⚠ この記事の執筆後(2026-10-03)に、関連カードが 4 件追加されています(未反映): `arxiv-1607.00148`, `arxiv-1802.03903`, `arxiv-2206.06602`, `arxiv-2405.09330`
<!-- /generated:stale -->

## この課題とは

センサーやサーバーの監視データなどの時系列から、異常な時点や区間を見つける問題。
正常データだけで学習し、入力の異常さを表す「異常スコア」を出して、閾値を超えたら異常と判定するのが典型である。
異常スコアは多くの場合、損失関数(再構成誤差や予測誤差)から定義される [arxiv-2211.05244#c8](https://arxiv.org/pdf/2211.05244v3#page=9 "An anomaly score is mostly defined based on a loss function.")。

深層学習の手法は、予測ベース・再構成ベース・表現ベース・それらの混合の4系統に整理される [arxiv-2211.05244#c1](https://arxiv.org/pdf/2211.05244v3#page=2 "These models are broadly classified into four categories: forecasting-based, reconstruction-based, representation-based and hybrid methods.")。
これに対して、距離や密度にもとづく古典的な手法(Isolation Forest、k 近傍、OC-SVM、PCA など)もある。

この分野の比較研究を読むと、**どの手法が強いかより先に、評価方法そのものが信用できるかが問題になっている**ことがわかる。

## 評価方法の問題

### point-adjust(PA)による過大評価

多くの研究は、F1 を計算する前に point-adjust という処理をかけている。
これは、正解の異常区間のうち1点でも検出できれば、その区間全体を検出できたとみなす処理である [arxiv-2109.05257#c3](https://arxiv.org/pdf/2109.05257v2#page=1 "if at least one moment in a contiguous anomaly segment is detected as an anomaly, the entire segment is then considered to be correctly predicted as anomaly.")。
この処理は適合率・再現率・F1 を上げる方向にしか働かない [arxiv-2109.05257#c4](https://arxiv.org/pdf/2109.05257v2#page=3 "after the PA, the P, R and consequently F1 score can only increase.")。

その結果、**ランダムな異常スコアでも最先端の手法に見えてしまう**。この点は3本の論文が独立に指摘している。

- Kim らは、理論と実験の両方でこれを示した [arxiv-2109.05257#c1](https://arxiv.org/pdf/2109.05257v2#page=1 "the PA protocol has a great possibility of overestimating the detection performance; that is, even a random anomaly score can easily turn into a state-of-the-art TAD method.")。ランダムなスコアの例は、SWaT で PA ありの F1 は最上位級なのに、PA なしの F1 は低い(生成された結果表を参照) [arxiv-2109.05257#r71](https://arxiv.org/pdf/2109.05257v2#page=6 "Case 1 0.969 0.216 0.965 0.109 0.931 0.190 0.961 0.227 0.804 0.080") [arxiv-2109.05257#r72](https://arxiv.org/pdf/2109.05257v2#page=6 "Case 1 0.969 0.216 0.965 0.109 0.931 0.190 0.961 0.227 0.804 0.080")。
- Sehili & Zhang も、PA のもとではランダムな推測が既存のすべての手法を上回りうるとしている [arxiv-2308.13068#c2](https://arxiv.org/pdf/2308.13068v2#page=1 "So flawed is one very popular protocol, the so-called point-adjust protocol, that a random guess can be shown to systematically outperform all algorithms developed so far.")。
- TAB の著者も、長い異常区間ではランダムな手法でも1点は当たりやすいと述べている [arxiv-2506.18046#c6](https://arxiv.org/pdf/2506.18046v2#page=2 "even random methods have a good chance to predict at least one point in larger anomaly windows")。

過大評価の大きさは、テストデータの異常区間の長さなどに依存する [arxiv-2109.05257#c6](https://arxiv.org/pdf/2109.05257v2#page=6 "the overestimation effect of PA depends on the test dataset distribution, and its effect becomes less conspicuous with shorter anomaly segments.")。

さらに、PA を前提に開発された手法(AnomalyTransformer、NCAD)は、他の評価方法ではランダムな推測と区別がつかなかった [arxiv-2308.13068#c4](https://arxiv.org/pdf/2308.13068v2#page=13 "Algorithms that were developed using point-adjust as the sole target fail to reach any score better than a random guess when evaluated with other")。
訓練していないモデルでも、ほぼ同じ高い PA スコアが出た [arxiv-2308.13068#c5](https://arxiv.org/pdf/2308.13068v2#page=14 "we also achieved essentially the same high scores using untrained versions of these models.")。
また、異常の割合が非常に高い PSM のようなデータセットでは、点単位の F1 自体が誤解を招きうる [arxiv-2308.13068#c7](https://arxiv.org/pdf/2308.13068v2#page=14 "Datasets that have a very high contamination rate, such as PSM, yield point-wise F1 scores that can be misleading.")。
PA で最良になる閾値では、SWaT で非常に頻繁に警報を出しており、実運用には使いにくいとされる [arxiv-2308.13068#c9](https://arxiv.org/pdf/2308.13068v2#page=15 "On average, it raises an alarm every 110 seconds, making it, in our opinion, barely useful for deployment.")。

### 閾値の選び方

比較研究の多くは、**テストデータで最良になる閾値**を使って数値を報告している。

- Kim らの論文: 全手法の閾値を、最良のスコアになるように選んでいる [arxiv-2109.05257#c9](https://arxiv.org/pdf/2109.05257v2#page=6 "All thresholds were obtained from those that yielded the best score.")。既存研究も、テストデータを見て閾値を決めるか、F1 が最良になる閾値を使っている [arxiv-2109.05257#c14](https://arxiv.org/pdf/2109.05257v2#page=7 "existing TAD methods set the threshold after investigating the test dataset or simply use the optimal threshold that yields the best F1.")。
- Sehili らの論文: 点単位の F1 が最良になる閾値を使っている [arxiv-2308.13068#c8](https://arxiv.org/pdf/2308.13068v2#page=13 "All metrics are computed based on the detection threshold that yields the best point-wise performance.")。
- TAB: すべての閾値で計算して最良の値を報告している [arxiv-2506.18046#c9](https://arxiv.org/pdf/2506.18046v2#page=8 "we conduct metric calculations at all thresholds and report the best results.")。

閾値を変えると、性能は大きく変わる [arxiv-2506.18046#c8](https://arxiv.org/pdf/2506.18046v2#page=2 "when the threshold changes, the performance can change considerably.")。
したがって、報告された数値はどれも楽観的であり、実運用で閾値を事前に決めたときの性能とは違う。
閾値に依存しない AUROC や AUPR を併用することが勧められている [arxiv-2109.05257#c15](https://arxiv.org/pdf/2109.05257v2#page=7 "Additional metrics with the reduced dependency such as AUROC or area under precision-recall (AUPR) curve will help in rigorous evaluation.")。
ただし、AUC-ROC を PA の後で計算し直すべきではない [arxiv-2506.18046#c7](https://arxiv.org/pdf/2506.18046v2#page=2 "should not be recalculated after point adjustment.")。

### ベンチマークデータの欠陥

Wu & Keogh は、よく使われるベンチマーク(Yahoo、Numenta、NASA など)の大半に、次の4つの欠陥があると指摘した [arxiv-2009.13807#c1](https://arxiv.org/pdf/2009.13807v5#page=1 "These flaws are triviality, unrealistic anomaly density, mislabeled ground truth and run-to-failure bias.")。

- **自明すぎる**: 1行の単純なコードで解ける系列が大半を占める例がある [arxiv-2009.13807#c3](https://arxiv.org/pdf/2009.13807v5#page=3 "316 out of 367 (86.1%) can be easily solved with a one-liner")。
- **異常の密度が非現実的**: 理想的には、1本のテスト系列に異常は1つだけあるべきだとしている [arxiv-2009.13807#c4](https://arxiv.org/pdf/2009.13807v5#page=4 "We believe that the ideal number of anomalies in a single testing time series is exactly one.")。
- **正解ラベルの誤り**: 誤検出の方向にも見落としの方向にも誤りがある [arxiv-2009.13807#c6](https://arxiv.org/pdf/2009.13807v5#page=6 "A naïve algorithm that simply labels the last point as an anomaly")。
- **run-to-failure の偏り**: 最後の点を異常と判定するだけの方法が高得点を取れる [arxiv-2009.13807#c7](https://arxiv.org/pdf/2009.13807v5#page=6 "the classic time series anomaly detection archives are irretrievably flawed.")。

彼らは、これらのアーカイブは修復できないほど欠陥があり [arxiv-2009.13807#c8](https://arxiv.org/pdf/2009.13807v5#page=6 "Thus, there is simply no level of performance that would suggest the utility of a")、その上ではどんな性能を報告しても手法の有用性を示せないと述べる [arxiv-2009.13807#c9](https://arxiv.org/pdf/2009.13807v5#page=1 "with this paper we introduce the UCR Time Series Anomaly Archive.")。
Kim らも、テストのラベル付けが不完全で、異常とされた区間の一部は正常データに近いことを指摘している [arxiv-2109.05257#c16](https://arxiv.org/pdf/2109.05257v2#page=4 "due to the incomplete test set labeling, some signals labeled as anomalies share more statistics with normal signals.")。

### その他の不統一

TAB は100本の研究を調べ、次の点を指摘している。

- 半数以上の研究で、使っている多変量データセットが4つ以下である [arxiv-2506.18046#c3](https://arxiv.org/pdf/2506.18046v2#page=2 "more than half of the studies include at most four datasets, and only one study covers 17 datasets.")。
- 検証用データをテストデータから取る研究がある [arxiv-2506.18046#c4](https://arxiv.org/pdf/2506.18046v2#page=2 "Some methods use a validation set from the testing set")。
- 最後の不完全なバッチを捨てる処理(drop-last)が、比較を不公平にする [arxiv-2506.18046#c5](https://arxiv.org/pdf/2506.18046v2#page=2 "discarding the last incomplete batch with fewer sample instances than the batch size is unfair")。

## 比較条件の違い

| 観点 | Kim et al. 2022 | Sehili & Zhang 2023 | Qiu et al. 2025 (TAB) |
|---|---|---|---|
| データ | SWaT、WADI、MSL、SMAP、SMD | SWaT、WADI、PSM | 多変量29データセット・単変量1,635系列 [arxiv-2506.18046#c1](https://arxiv.org/pdf/2506.18046v2#page=1 "TAB encompasses 29 public multivariate datasets and 1,635 univariate time series from different domains") |
| 既存手法の数値 | 原論文の報告値と著者の再現値が混在 [arxiv-2109.05257#c10](https://arxiv.org/pdf/2109.05257v2#page=6 "For the existing methods, we used the best numbers reported in the original papers and officially reproduced results") | 公式実装で再実行 | 統一パイプラインで再実行し、ハイパーパラメータは最良を採用 [arxiv-2506.18046#c10](https://arxiv.org/pdf/2506.18046v2#page=8 "We then select the best results from these evaluations") |
| 閾値 | 最良のスコアになる閾値 [arxiv-2109.05257#c9](https://arxiv.org/pdf/2109.05257v2#page=6 "All thresholds were obtained from those that yielded the best score.") | 点単位 F1 が最良になる閾値 [arxiv-2308.13068#c8](https://arxiv.org/pdf/2308.13068v2#page=13 "All metrics are computed based on the detection threshold that yields the best point-wise performance.") | 全閾値のうち最良 [arxiv-2506.18046#c9](https://arxiv.org/pdf/2506.18046v2#page=8 "we conduct metric calculations at all thresholds and report the best results.") |
| 主な指標 | PA あり/なしの F1 | 点単位・複合・イベント単位の F1 | VUS-PR、Affiliation F1、AUC-ROC など |

## 論文内の勝敗の関係

- [Kim et al. 2022 の結果表と勝敗](../../generated/papers/arxiv-2109.05257.md)
- [Sehili & Zhang 2023 の結果表と勝敗](../../generated/papers/arxiv-2308.13068.md)
- [Qiu et al. 2025 (TAB) の結果表と勝敗](../../generated/papers/arxiv-2506.18046.md)

### 単純な手法が強い

5本の論文が、それぞれ別の方法で「単純な手法が、凝った深層学習の手法と同等以上」であることを示している。

- **訓練していないモデル**: PA を使わない評価では、既存手法の多くが訓練していないモデルの基準線を下回るか同程度だった [arxiv-2109.05257#c2](https://arxiv.org/pdf/2109.05257v2#page=1 "an untrained model obtains comparable detection performance to the existing methods even when PA is forbidden.") [arxiv-2109.05257#c8](https://arxiv.org/pdf/2109.05257v2#page=7 "mostly inferior to Case 2 and 3, implying that the currently proposed methods may have obtained marginal or even no advancement against the baselines.")。
- **PCA**: 単純な前処理と後処理を加えた PCA が、多くの深層学習手法を上回った [arxiv-2308.13068#c3](https://arxiv.org/pdf/2308.13068v2#page=1 "we propose a simple, yet challenging, baseline based on Principal Components Analysis (PCA) that surprisingly outperforms many recent Deep Learning (DL) based approaches on popular benchmark datasets.") [arxiv-2308.13068#c10](https://arxiv.org/pdf/2308.13068v2#page=14 "we use simple pre-processing and post-processing blocks (input scaling, clipping and score smoothing) that significantly improve the score.")。著者は、多くの研究が十分に手強い単純な基準線を置いていないと批判している [arxiv-2308.13068#c13](https://arxiv.org/pdf/2308.13068v2#page=1 "instead of putting the highest weight on the design of increasingly more complex")。
- **古典的な手法(TAB)**: 単変量の系列では、機械学習や学習を使わない古典的な手法が平均で最良だった [arxiv-2506.18046#c11](https://arxiv.org/pdf/2506.18046v2#page=10 "Machine learning (ML) and non-learning (NL) methods exhibit the best average performance in terms of the V-PR and Aff-F metrics.") [arxiv-2506.18046#c18](https://arxiv.org/pdf/2506.18046v2#page=11 "with OCSVM, HOBS, and DWT achieving the excellent results.")。著者は、新手法を追う一方で古典的な手法を見落とすべきではないとしている [arxiv-2506.18046#c12](https://arxiv.org/pdf/2506.18046v2#page=10 "while pursuing novel methods, we should not overlook the classic methods.")。
- **1行のコード**: ベンチマークの多くの系列は、1行の単純なコードで解ける [arxiv-2009.13807#c3](https://arxiv.org/pdf/2009.13807v5#page=3 "316 out of 367 (86.1%) can be easily solved with a one-liner")。
- **時系列基盤モデル自身の論文(MOMENT)**: 統計的な手法や Transformer でない手法が多くの深層モデルを上回ったと報告しており、その例の1つが異常検知での k 近傍法である。著者は、こうした基準線が実用性の評価に必要だと主張している [arxiv-2402.03885#c7](https://arxiv.org/pdf/2402.03885v3#page=7 "We found that statistical and non-transformer-based approaches like ARIMA for short-horizon forecasting, N-BEATS for long-horizon forecasting, and k-nearest neighbors for anomaly detection outperform many deep and transformer-based models.")。

### GDN は評価方法を変えても崩れにくい

Kim らの比較では、未訓練の基準線をすべてのデータセットで上回ったのは GDN だけだった [arxiv-2109.05257#c7](https://arxiv.org/pdf/2109.05257v2#page=7 "Only the GDN consistently exceeded the baselines for all datasets.")。
Sehili らでも、点単位の評価を前提に開発された GDN は、他の評価方法でも比較的崩れなかった [arxiv-2308.13068#c6](https://arxiv.org/pdf/2308.13068v2#page=14 "GDN, however, which was developed based on the more realistic point-wise protocol, shows more resilience when evaluated with other protocols.")。
**別の著者・別の評価方法で、同じ方向の結果が出ている**点で、この2本の観察は重みがある。

### 多変量データでは深層モデルにも出番がある

TAB の多変量データでは、データセットごとに学習した一部の深層モデル(TsNet、CATCH)が最良に近かった [arxiv-2506.18046#c13](https://arxiv.org/pdf/2506.18046v2#page=10 "Some deep learning models, such as TsNet and CATCH, appear to achieve the best performance in full-shot settings.")。
事前学習済みの時系列モデルは、ゼロショットより少量でも学習させたほうが大きく良くなった [arxiv-2506.18046#c15](https://arxiv.org/pdf/2506.18046v2#page=10 "time series pre-trained models demonstrate significantly better performance compared to zero-shot learning approaches.")。
一方で、古典的な手法が多変量でも強いことから、深層学習の手法には改善の余地が大きいとも述べている [arxiv-2506.18046#c14](https://arxiv.org/pdf/2506.18046v2#page=11 "This suggests that there is still significant room for improvement in current deep learning approaches.")。
TAB の著者は、すべての系列と異常の種類で最良の手法はないとしている [arxiv-2506.18046#c16](https://arxiv.org/pdf/2506.18046v2#page=2 "no single TSAD method is universally best for all time series and anomaly types.")。

## 2025〜2026年の論文は評価方法を改善したか

2026年10月の候補 Issue で承認された18本について、主な結果をどの評価方法で報告しているかを確かめた。

**注意**: この18本は無作為に選んだものではない。候補は「このリポジトリの既存カードを2本以上引用している」か「キーワードに一致した」ことで選ばれている。既存カードには point-adjust を批判した Kim らの論文が含まれるため、評価の問題を意識した論文に偏っている可能性がある。

| 論文 | 種類 | 主な評価方法 | 根拠 |
|---|---|---|---|
| SACM | 汎用の正則化手法 | **point-adjust 付き F1** | [arxiv-2609.39489#c2](https://arxiv.org/pdf/2609.39489v1#page=1 "improves classification accuracy and point-adjusted F1 by 3.04% and 17.05%, respectively") [arxiv-2609.39489#c3](https://arxiv.org/pdf/2609.39489v1#page=10 "Raw and +SACM share the benchmark point-adjusted (PA) protocol [37, 39] for paired comparison") |
| WinoTS | 事前学習手法 | **point-adjust 付きの適合率・再現率・F1** | [arxiv-2609.39337#c2](https://arxiv.org/pdf/2609.39337v1#page=6 "TSLib evaluation protocol and report point-adjusted precision, recall, and F1") |
| AMAD | 手法 | **point-adjust 付きの適合率・再現率・F1**(先行研究の慣習に合わせると明記)。閾値は事前に決めた異常割合のパーセンタイル | [arxiv-2504.06643#c2](https://arxiv.org/pdf/2504.06643v3#page=10 "we decided not to break this tradition, with the same adjustment method as [30]") [arxiv-2504.06643#c3](https://arxiv.org/pdf/2504.06643v3#page=9 "Thresholding the p-th percentile of the AnomalyScore") |
| GRASP | 手法 | ROC、PRC と、**テストの正解ラベルで F1 が最大になる閾値**での F1 | [arxiv-2609.36765#c2](https://arxiv.org/pdf/2609.36765v1#page=8 "with the threshold that maximizes the F1 score using test labels") |
| MSCAD | 手法 | VUS-PR(point-adjust は乱数で水増しできるとして主指標にしない) | [arxiv-2609.38004#c3](https://arxiv.org/pdf/2609.38004v1#page=6 "unlike Point-Adjusted F1 (PA-F1) it is threshold-free and not gameable by random scores.") |
| AnoMamba | 手法 | Kim らを引用して point-adjust を避け、affiliation F1 と VUS-ROC。閾値は SPOT で決定 | [doi-10.24963_ijcai.2026_276#c2](https://www.ijcai.org/proceedings/2026/0276.pdf#page=5 "As noted by [Kim et al., 2022], point-adjustment metrics can lead to misleading rankings") [doi-10.24963_ijcai.2026_276#c3](https://www.ijcai.org/proceedings/2026/0276.pdf#page=5 "All thresholds were selected by SPOT") |
| LEARN-TS | 手法 | どの指標にも point-adjust を使わない。閾値は検証用の候補のうち指標が最大になるもの | [arxiv-2609.38789#c3](https://arxiv.org/pdf/2609.38789v1#page=13 "No point adjustment is applied to any metric.") [arxiv-2609.38789#c4](https://arxiv.org/pdf/2609.38789v1#page=7 "we report the R-F1-maximizing operating point over normal-validation quantile candidates") |
| SBOG | 外れ値生成 | point-adjust なしの点単位の評価 | [arxiv-2609.31470#c2](https://arxiv.org/pdf/2609.31470v1#page=7 "our main tables use the stricter point-wise evaluation without Point Adjustment.") |
| PISCES | 応用(宇宙天気) | PR-AUC(point-adjust の問題にも言及)。警報の閾値は別期間の検証データで決定 | [arxiv-2609.28022#c2](https://arxiv.org/pdf/2609.28022v1#page=10 "Point-adjusted F1 can make random anomaly scores appear competitive [41]") [arxiv-2609.28022#c4](https://arxiv.org/pdf/2609.28022v1#page=10 "The detection threshold is the 99th percentile of composite anomaly scores in the 2016 to 2017 validation set.") |
| CARE | 推論の高速化 | Affiliated-F1 と AUC-PR | [arxiv-2608.01885#c2](https://arxiv.org/pdf/2608.01885v1#page=8 "Table 1: Average Aff-F (Affiliated-F1), A-P (AUC-PR) and Inference time across 8 real-world") |
| LLM による検出器の自動設計 | 手法 | affiliation F、時間を考慮した F1、点単位 F1、VUS-PR。閾値つき指標は**最良の閾値**での値 | [arxiv-2610.01223#c3](https://arxiv.org/pdf/2610.01223v1#page=4 "On TSB-AD we follow the Time-RCD protocol and re- port the affiliation F-measure [11]") [arxiv-2610.01223#c4](https://arxiv.org/pdf/2610.01223v1#page=9 "the harness reports each threshold-dependent metric at its score-optimal operating point") |
| TS-Router | 手法(基盤モデル) | VUS-PR、Affiliation-F1 など4指標。閾値つき指標は**評価データの正解ラベルで選んだ閾値** | [arxiv-2610.00978#c3](https://arxiv.org/pdf/2610.00978v1#page=7 "we report VUS-PR, Affiliation-F1, F1T, and Standard-F1") [arxiv-2610.00978#c4](https://arxiv.org/pdf/2610.00978v1#page=8 "Threshold-dependent metrics use oracle thresholds selected from evaluation labels") |
| FlowFuse | 手法 | AUC-ROC と Affiliated-F1 | [doi-10.24963_ijcai.2026_332#c3](https://www.ijcai.org/proceedings/2026/0332.pdf#page=6 "Table 3: Average AUC-ROC (A-R) and Affiliated-F1 (Aff-F) accuracy measures for all datasets.") |
| ロボットの故障検知 | 応用 | VUS-PR | [arxiv-2609.29194#c2](https://arxiv.org/pdf/2609.29194v1#page=4 "Unlike standard point-wise metrics, VUS-PR is explicitly designed for range-based time series") |
| TAMIS | 応用(電力) | AUC-PR(AUC-ROC は楽観的すぎるとして) | [arxiv-2609.39257#c2](https://arxiv.org/pdf/2609.39257v1#page=9 "the Area Under the ROC curve (AUC-ROC) tends to overestimate the accuracy of detectors [30].") |
| StrAD | ベンチマーク | AUC-PR | [arxiv-2609.39215#c3](https://arxiv.org/pdf/2609.39215v1#page=6 "Consequently, the Area Under the Precision- Recall Curve (AUC-PR) is preferred in this study.") |
| SHAD | ベンチマーク | VUS-PR | [arxiv-2610.01168#c3](https://arxiv.org/pdf/2610.01168v1#page=7 "Performance is evaluated using VUS- PR (a robust, threshold-independent metric) with a 25-point buffer") |
| What the Detector Can See | 評価方法 | 閾値に依存しない残差の評価 | [arxiv-2608.02821#c2](https://arxiv.org/pdf/2608.02821v1#page=1 "Instead of scoring only the final alarms, we evaluate Stage 1 directly using normalized residual energy") |

**読み取れること**:

- 18本のうち、**point-adjust を主な評価に使っているのは3本**(SACM、WinoTS、AMAD)だった。SACM と WinoTS は時系列の汎用手法(正則化、事前学習)で、異常検知は複数の課題の1つとして扱われている。AMAD は異常検知専用の手法で、先行研究の慣習に合わせるために point-adjust を使うと明記している [arxiv-2504.06643#c2](https://arxiv.org/pdf/2504.06643v3#page=10 "we decided not to break this tradition, with the same adjustment method as [30]")。
- 多くの論文は、VUS-PR、AUC-PR、affiliation F1 などの指標を使っている。Kim らを引用して point-adjust を避けると明記する論文もある [doi-10.24963_ijcai.2026_276#c2](https://www.ijcai.org/proceedings/2026/0276.pdf#page=5 "As noted by [Kim et al., 2022], point-adjustment metrics can lead to misleading rankings") [arxiv-2609.38004#c3](https://arxiv.org/pdf/2609.38004v1#page=6 "unlike Point-Adjusted F1 (PA-F1) it is threshold-free and not gameable by random scores.")。上記の注意(選び方の偏り)はあるが、point-adjust 批判は少なくともこの範囲では広く受け入れられている。
- 一方で、**閾値の問題は残っている**。テストや評価データの正解ラベルを使って閾値を選ぶ論文が3本あった [arxiv-2609.36765#c2](https://arxiv.org/pdf/2609.36765v1#page=8 "with the threshold that maximizes the F1 score using test labels") [arxiv-2610.00978#c4](https://arxiv.org/pdf/2610.00978v1#page=8 "Threshold-dependent metrics use oracle thresholds selected from evaluation labels") [arxiv-2610.01223#c4](https://arxiv.org/pdf/2610.01223v1#page=9 "the harness reports each threshold-dependent metric at its score-optimal operating point")。TSB-AD の実装の閾値つき F1 も、閾値を指定しないと最良の閾値での値になる [arxiv-2609.38004#c4](https://arxiv.org/pdf/2609.38004v1#page=19 "These metrics are useful for diagnosing detector behavior but can be sensitive to threshold selection and, in some cases, to point-adjustment effects.")。正解を見ないで閾値を決めているのは、SPOT を使う論文 [doi-10.24963_ijcai.2026_276#c3](https://www.ijcai.org/proceedings/2026/0276.pdf#page=5 "All thresholds were selected by SPOT") や、別期間の検証データを使う論文 [arxiv-2609.28022#c4](https://arxiv.org/pdf/2609.28022v1#page=10 "The detection threshold is the 99th percentile of composite anomaly scores in the 2016 to 2017 validation set.") など一部にとどまる。
- 評価方法そのものについても新しい指摘がある。ROC-AUC が同程度でも、同じ誤報率で比べると性能が桁違いに違うこと [arxiv-2608.02821#c3](https://arxiv.org/pdf/2608.02821v1#page=13 "before thresholding, CUSUM, point adjustment, or other alarm policies are applied")、ベンチマークによって順位が入れ替わること [arxiv-2608.02821#c4](https://arxiv.org/pdf/2608.02821v1#page=1 "Although the detectors have similar ROC-AUC values on SWaT, their performance differs by more than an order of magnitude at a common false-alarm rate.") が示された。ストリーミング向けの手法が、実は静的な手法に劣るという結果もある [arxiv-2609.39215#c2](https://arxiv.org/pdf/2609.39215v1#page=1 "Our results show that, contrary to common assumptions, static TSAD methods significantly outperform streaming approaches in most streaming settings.")。

## 現時点での整理

- **point-adjust の数値は比較に使わない**: ランダムなスコアでも高い値が出るため、PA を使った比較だけで手法の優劣を判断してはいけない [arxiv-2109.05257#c1](https://arxiv.org/pdf/2109.05257v2#page=1 "the PA protocol has a great possibility of overestimating the detection performance; that is, even a random anomaly score can easily turn into a state-of-the-art TAD method.") [arxiv-2308.13068#c2](https://arxiv.org/pdf/2308.13068v2#page=1 "So flawed is one very popular protocol, the so-called point-adjust protocol, that a random guess can be shown to systematically outperform all algorithms developed so far.")。
- **単純な基準線と比べる**: 訓練していないモデル [arxiv-2109.05257#c13](https://arxiv.org/pdf/2109.05257v2#page=4 "we suggest establishing a new baseline with the F1 measured from the prediction of a randomly initialized reconstruction model with simple architecture")、PCA [arxiv-2308.13068#c3](https://arxiv.org/pdf/2308.13068v2#page=1 "we propose a simple, yet challenging, baseline based on Principal Components Analysis (PCA) that surprisingly outperforms many recent Deep Learning (DL) based approaches on popular benchmark datasets.")、古典的な手法 [arxiv-2506.18046#c11](https://arxiv.org/pdf/2506.18046v2#page=10 "Machine learning (ML) and non-learning (NL) methods exhibit the best average performance in terms of the V-PR and Aff-F metrics.") を基準線として置き、それを上回るかで判断する。
- **閾値の扱いを確認する**: 報告値の多くは、テストデータで最良の閾値によるもので楽観的である [arxiv-2109.05257#c9](https://arxiv.org/pdf/2109.05257v2#page=6 "All thresholds were obtained from those that yielded the best score.") [arxiv-2506.18046#c9](https://arxiv.org/pdf/2506.18046v2#page=8 "we conduct metric calculations at all thresholds and report the best results.")。閾値に依存しない指標も見る [arxiv-2109.05257#c15](https://arxiv.org/pdf/2109.05257v2#page=7 "Additional metrics with the reduced dependency such as AUROC or area under precision-recall (AUPR) curve will help in rigorous evaluation.")。
- **データの質を確認する**: よく使われるベンチマークには、自明すぎる例や誤ったラベルが多い [arxiv-2009.13807#c1](https://arxiv.org/pdf/2009.13807v5#page=1 "These flaws are triviality, unrealistic anomaly density, mislabeled ground truth and run-to-failure bias.")。系列を実際に描画して確認することが勧められている [arxiv-2009.13807#c10](https://arxiv.org/pdf/2009.13807v5#page=8 "We suspect that some researchers rarely view the time series, they simply pass objects to a black box and look at the F1 scores")。
- **実運用の課題**: 誤検知の削減 [arxiv-2211.05244#c4](https://arxiv.org/pdf/2211.05244v3#page=27 "one of the key challenges is to find a mechanism for minimising false positives and improve recall rates of detection.")、解釈性 [arxiv-2211.05244#c5](https://arxiv.org/pdf/2211.05244v3#page=28 "anomaly detection research focuses primarily on detection precision, failing to address the issue of interpretability.")、データの非定常性への対応 [arxiv-2211.05244#c3](https://arxiv.org/pdf/2211.05244v3#page=27 "This non-stationary nature necessitates the adaptation of deep learning models through online or incremental training approaches") は未解決の課題として残っている。非定常性への対応は、[ドリフト検出の記事](drift-detection.md)の問題とつながる。

**この整理に含まれていないもの**: TSB-AD などの他の大規模ベンチマーク(arXiv で確認できず未取得。ただし2026年の論文の多くが TSB-AD で評価している [arxiv-2609.38004#c2](https://arxiv.org/pdf/2609.38004v1#page=1 "MSCAD achieves large performance gains against 50 baselines across multiple metrics") [arxiv-2610.01223#c2](https://arxiv.org/pdf/2610.01223v1#page=1 "yet they train no network and use no GPU"))、UCR Time Series Anomaly Archive での手法比較、AnomalyTransformer や GDN などの個々の手法の原論文、時系列の基盤モデルの原論文。

## 参照カード

- [arxiv-2109.05257](../../papers/arxiv-2109.05257.yaml) Kim et al., "Towards a Rigorous Evaluation of Time-series Anomaly Detection" (AAAI 2022)
- [arxiv-2009.13807](../../papers/arxiv-2009.13807.yaml) Wu & Keogh, "Current Time Series Anomaly Detection Benchmarks are Flawed and are Creating the Illusion of Progress"
- [arxiv-2308.13068](../../papers/arxiv-2308.13068.yaml) Sehili & Zhang, "Multivariate Time Series Anomaly Detection: Fancy Algorithms and Flawed Evaluation Methodology"
- [arxiv-2506.18046](../../papers/arxiv-2506.18046.yaml) Qiu et al., "TAB: Unified Benchmarking of Time Series Anomaly Detection Methods" (PVLDB 2025)
- [arxiv-2211.05244](../../papers/arxiv-2211.05244.yaml) Darban et al., "Deep Learning for Time Series Anomaly Detection: A Survey"
- [arxiv-2402.03885](../../papers/arxiv-2402.03885.yaml) Goswami et al., "MOMENT: A Family of Open Time-series Foundation Models"
