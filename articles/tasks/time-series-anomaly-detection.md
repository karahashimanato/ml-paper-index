---
title: 時系列異常検知の手法比較と評価方法の問題
kind: task
tags: [time-series-anomaly-detection]
depends_on: [arxiv-2109.05257, arxiv-2009.13807, arxiv-2308.13068, arxiv-2506.18046, arxiv-2211.05244]
written_at: 2026-10-02
written_by: claude-opus-5-5 via Claude Code
---

# 時系列異常検知の手法比較と評価方法の問題

<!-- generated:stale -->
> 未反映のカードはありません。
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

4本の論文が、それぞれ別の方法で「単純な手法が、凝った深層学習の手法と同等以上」であることを示している。

- **訓練していないモデル**: PA を使わない評価では、既存手法の多くが訓練していないモデルの基準線を下回るか同程度だった [arxiv-2109.05257#c2](https://arxiv.org/pdf/2109.05257v2#page=1 "an untrained model obtains comparable detection performance to the existing methods even when PA is forbidden.") [arxiv-2109.05257#c8](https://arxiv.org/pdf/2109.05257v2#page=7 "mostly inferior to Case 2 and 3, implying that the currently proposed methods may have obtained marginal or even no advancement against the baselines.")。
- **PCA**: 単純な前処理と後処理を加えた PCA が、多くの深層学習手法を上回った [arxiv-2308.13068#c3](https://arxiv.org/pdf/2308.13068v2#page=1 "we propose a simple, yet challenging, baseline based on Principal Components Analysis (PCA) that surprisingly outperforms many recent Deep Learning (DL) based approaches on popular benchmark datasets.") [arxiv-2308.13068#c10](https://arxiv.org/pdf/2308.13068v2#page=14 "we use simple pre-processing and post-processing blocks (input scaling, clipping and score smoothing) that significantly improve the score.")。著者は、多くの研究が十分に手強い単純な基準線を置いていないと批判している [arxiv-2308.13068#c13](https://arxiv.org/pdf/2308.13068v2#page=1 "instead of putting the highest weight on the design of increasingly more complex")。
- **古典的な手法(TAB)**: 単変量の系列では、機械学習や学習を使わない古典的な手法が平均で最良だった [arxiv-2506.18046#c11](https://arxiv.org/pdf/2506.18046v2#page=10 "Machine learning (ML) and non-learning (NL) methods exhibit the best average performance in terms of the V-PR and Aff-F metrics.") [arxiv-2506.18046#c18](https://arxiv.org/pdf/2506.18046v2#page=11 "with OCSVM, HOBS, and DWT achieving the excellent results.")。著者は、新手法を追う一方で古典的な手法を見落とすべきではないとしている [arxiv-2506.18046#c12](https://arxiv.org/pdf/2506.18046v2#page=10 "while pursuing novel methods, we should not overlook the classic methods.")。
- **1行のコード**: ベンチマークの多くの系列は、1行の単純なコードで解ける [arxiv-2009.13807#c3](https://arxiv.org/pdf/2009.13807v5#page=3 "316 out of 367 (86.1%) can be easily solved with a one-liner")。

### GDN は評価方法を変えても崩れにくい

Kim らの比較では、未訓練の基準線をすべてのデータセットで上回ったのは GDN だけだった [arxiv-2109.05257#c7](https://arxiv.org/pdf/2109.05257v2#page=7 "Only the GDN consistently exceeded the baselines for all datasets.")。
Sehili らでも、点単位の評価を前提に開発された GDN は、他の評価方法でも比較的崩れなかった [arxiv-2308.13068#c6](https://arxiv.org/pdf/2308.13068v2#page=14 "GDN, however, which was developed based on the more realistic point-wise protocol, shows more resilience when evaluated with other protocols.")。
**別の著者・別の評価方法で、同じ方向の結果が出ている**点で、この2本の観察は重みがある。

### 多変量データでは深層モデルにも出番がある

TAB の多変量データでは、データセットごとに学習した一部の深層モデル(TsNet、CATCH)が最良に近かった [arxiv-2506.18046#c13](https://arxiv.org/pdf/2506.18046v2#page=10 "Some deep learning models, such as TsNet and CATCH, appear to achieve the best performance in full-shot settings.")。
事前学習済みの時系列モデルは、ゼロショットより少量でも学習させたほうが大きく良くなった [arxiv-2506.18046#c15](https://arxiv.org/pdf/2506.18046v2#page=10 "time series pre-trained models demonstrate significantly better performance compared to zero-shot learning approaches.")。
一方で、古典的な手法が多変量でも強いことから、深層学習の手法には改善の余地が大きいとも述べている [arxiv-2506.18046#c14](https://arxiv.org/pdf/2506.18046v2#page=11 "This suggests that there is still significant room for improvement in current deep learning approaches.")。
TAB の著者は、すべての系列と異常の種類で最良の手法はないとしている [arxiv-2506.18046#c16](https://arxiv.org/pdf/2506.18046v2#page=2 "no single TSAD method is universally best for all time series and anomaly types.")。

## 現時点での整理

- **point-adjust の数値は比較に使わない**: ランダムなスコアでも高い値が出るため、PA を使った比較だけで手法の優劣を判断してはいけない [arxiv-2109.05257#c1](https://arxiv.org/pdf/2109.05257v2#page=1 "the PA protocol has a great possibility of overestimating the detection performance; that is, even a random anomaly score can easily turn into a state-of-the-art TAD method.") [arxiv-2308.13068#c2](https://arxiv.org/pdf/2308.13068v2#page=1 "So flawed is one very popular protocol, the so-called point-adjust protocol, that a random guess can be shown to systematically outperform all algorithms developed so far.")。
- **単純な基準線と比べる**: 訓練していないモデル [arxiv-2109.05257#c13](https://arxiv.org/pdf/2109.05257v2#page=4 "we suggest establishing a new baseline with the F1 measured from the prediction of a randomly initialized reconstruction model with simple architecture")、PCA [arxiv-2308.13068#c3](https://arxiv.org/pdf/2308.13068v2#page=1 "we propose a simple, yet challenging, baseline based on Principal Components Analysis (PCA) that surprisingly outperforms many recent Deep Learning (DL) based approaches on popular benchmark datasets.")、古典的な手法 [arxiv-2506.18046#c11](https://arxiv.org/pdf/2506.18046v2#page=10 "Machine learning (ML) and non-learning (NL) methods exhibit the best average performance in terms of the V-PR and Aff-F metrics.") を基準線として置き、それを上回るかで判断する。
- **閾値の扱いを確認する**: 報告値の多くは、テストデータで最良の閾値によるもので楽観的である [arxiv-2109.05257#c9](https://arxiv.org/pdf/2109.05257v2#page=6 "All thresholds were obtained from those that yielded the best score.") [arxiv-2506.18046#c9](https://arxiv.org/pdf/2506.18046v2#page=8 "we conduct metric calculations at all thresholds and report the best results.")。閾値に依存しない指標も見る [arxiv-2109.05257#c15](https://arxiv.org/pdf/2109.05257v2#page=7 "Additional metrics with the reduced dependency such as AUROC or area under precision-recall (AUPR) curve will help in rigorous evaluation.")。
- **データの質を確認する**: よく使われるベンチマークには、自明すぎる例や誤ったラベルが多い [arxiv-2009.13807#c1](https://arxiv.org/pdf/2009.13807v5#page=1 "These flaws are triviality, unrealistic anomaly density, mislabeled ground truth and run-to-failure bias.")。系列を実際に描画して確認することが勧められている [arxiv-2009.13807#c10](https://arxiv.org/pdf/2009.13807v5#page=8 "We suspect that some researchers rarely view the time series, they simply pass objects to a black box and look at the F1 scores")。
- **実運用の課題**: 誤検知の削減 [arxiv-2211.05244#c4](https://arxiv.org/pdf/2211.05244v3#page=27 "one of the key challenges is to find a mechanism for minimising false positives and improve recall rates of detection.")、解釈性 [arxiv-2211.05244#c5](https://arxiv.org/pdf/2211.05244v3#page=28 "anomaly detection research focuses primarily on detection precision, failing to address the issue of interpretability.")、データの非定常性への対応 [arxiv-2211.05244#c3](https://arxiv.org/pdf/2211.05244v3#page=27 "This non-stationary nature necessitates the adaptation of deep learning models through online or incremental training approaches") は未解決の課題として残っている。非定常性への対応は、[ドリフト検出の記事](drift-detection.md)の問題とつながる。

**この整理に含まれていないもの**: TSB-AD などの他の大規模ベンチマーク(arXiv で確認できず未取得)、UCR Time Series Anomaly Archive での手法比較、AnomalyTransformer や GDN などの個々の手法の原論文、時系列の基盤モデルの原論文。

## 参照カード

- [arxiv-2109.05257](../../papers/arxiv-2109.05257.yaml) Kim et al., "Towards a Rigorous Evaluation of Time-series Anomaly Detection" (AAAI 2022)
- [arxiv-2009.13807](../../papers/arxiv-2009.13807.yaml) Wu & Keogh, "Current Time Series Anomaly Detection Benchmarks are Flawed and are Creating the Illusion of Progress"
- [arxiv-2308.13068](../../papers/arxiv-2308.13068.yaml) Sehili & Zhang, "Multivariate Time Series Anomaly Detection: Fancy Algorithms and Flawed Evaluation Methodology"
- [arxiv-2506.18046](../../papers/arxiv-2506.18046.yaml) Qiu et al., "TAB: Unified Benchmarking of Time Series Anomaly Detection Methods" (PVLDB 2025)
- [arxiv-2211.05244](../../papers/arxiv-2211.05244.yaml) Darban et al., "Deep Learning for Time Series Anomaly Detection: A Survey"
