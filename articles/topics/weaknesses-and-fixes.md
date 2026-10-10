---
title: モデルと評価方法の弱点、それを改善した研究
kind: topic
tags: [tabular-classification, tabular-regression, drift-detection, concept-drift-detection, dataset-shift-detection, time-series-anomaly-detection]
depends_on: [arxiv-2106.03253, arxiv-2106.11959, arxiv-2207.08815, arxiv-2207.01848, arxiv-2305.02997, arxiv-2506.16791, doi-10.1038_s41586-024-08328-6, arxiv-2410.24210, arxiv-2407.04491, arxiv-2004.05785, arxiv-1810.11953, arxiv-2311.06396, arxiv-2606.07789, arxiv-2602.06456, doi-10.1007_s41060-024-00620-y, arxiv-2310.15826, arxiv-2109.05257, arxiv-2009.13807, arxiv-2308.13068, arxiv-2506.18046, arxiv-2211.05244, arxiv-2608.02821, arxiv-2609.39215, arxiv-2610.01168, arxiv-2609.38004, arxiv-2609.31470, arxiv-2609.28022, arxiv-2608.01885, arxiv-2609.39489, arxiv-2609.38789, arxiv-2610.01223, arxiv-2610.00978, arxiv-2609.39337, arxiv-2609.39257, arxiv-2609.36765, arxiv-2609.29194, arxiv-2504.06643, doi-10.24963_ijcai.2026_276, doi-10.24963_ijcai.2026_332, arxiv-1602.04938, arxiv-1806.10758, arxiv-1810.03292, arxiv-1902.10186, arxiv-1905.04610, arxiv-1911.02508, arxiv-1911.05248, arxiv-2004.13912, arxiv-2006.16234, arxiv-2010.03058, arxiv-2202.01602, arxiv-2210.17323, arxiv-2310.01382, arxiv-2403.15447, arxiv-2608.04348, arxiv-2608.05265, arxiv-2608.08245, arxiv-2608.25774, arxiv-2608.27882, arxiv-2608.28980, arxiv-2608.30337, arxiv-2609.02766, arxiv-2609.03003, arxiv-2609.04388, arxiv-2609.04540, arxiv-2609.06080, arxiv-2609.09432, arxiv-2609.12712, arxiv-2609.13031, arxiv-2609.17488, arxiv-2609.24278, arxiv-2609.25541, arxiv-2609.32898, arxiv-2609.33940, arxiv-2609.35703, arxiv-2609.36337, arxiv-1703.01365]
written_at: 2026-10-03
written_by: claude-opus-5-5 via Claude Code
---

# モデルと評価方法の弱点、それを改善した研究

<!-- generated:stale -->
> ⚠ この記事の執筆日(2026-10-03)以降に作成された関連カードが 62 件あります(未反映。執筆日と同じ日に作成されたカードを含む): `arxiv-0804.2752`, `arxiv-1005.0208`, `arxiv-1208.3719`, `arxiv-1405.2881`, `arxiv-1504.07676`, `arxiv-1505.01866`, `arxiv-1506.02142`, `arxiv-1511.05741`, `arxiv-1603.02754`, `arxiv-1603.06212`, `arxiv-1604.04173`, `arxiv-1607.00148`, `arxiv-1610.01271`, `arxiv-1612.01474`, `arxiv-1706.09516`, `arxiv-1802.03903`, `arxiv-1802.05640`, `arxiv-1802.09596`, `arxiv-1804.03515`, `arxiv-1807.00263`, `arxiv-1807.01774`, `arxiv-1810.11363`, `arxiv-1810.11921`, `arxiv-1812.04606`, `arxiv-1903.05179`, `arxiv-1904.06019`, `arxiv-1905.03222`, `arxiv-1907.00909`, `arxiv-1908.07442`, `arxiv-1909.06312`, `arxiv-1909.09223`, `arxiv-1910.03225`, `arxiv-1910.12656`, `arxiv-1910.13204`, `arxiv-1911.00190`, `arxiv-1911.01914`, `arxiv-1911.04706`, `arxiv-2001.04295`, `arxiv-2003.03629`, `arxiv-2003.06505`, `arxiv-2006.10562`, `arxiv-2006.13799`, `arxiv-2008.13535`, `arxiv-2012.03826`, `arxiv-2012.06678`, `arxiv-2106.00170`, `arxiv-2106.01342`, `arxiv-2106.11189`, `arxiv-2106.15147`, `arxiv-2109.06716`, `arxiv-2110.01889`, `arxiv-2202.13415`, `arxiv-2203.05556`, `arxiv-2206.06602`, `arxiv-2207.12560`, `arxiv-2301.02819`, `arxiv-2305.18446`, `arxiv-2307.14338`, `arxiv-2309.17130`, `arxiv-2402.01502`, `arxiv-2405.09330`, `arxiv-2407.00956`
<!-- /generated:stale -->

## この記事の読み方

このリポジトリにある論文から、「ある論文がモデルや評価方法の**弱点を指摘**し、別の(または同じ)論文が**改善策を提案して検証**した」という流れを、テーマを横断して集めた。

各項目は「問題点 → 改善策 → 検証 → 独立した確認」の順に書く。注意点が2つある。

- **論文をまたいで「この指摘にこの改善が対応する」と結び付けるのは、多くの場合この記事の整理**である。改善策の論文が、指摘した論文に明示的に応答しているとは限らない。そういう箇所は本文で明記する。
- **「独立した確認」**は、改善策を提案した著者と重ならない著者が、別の条件で同じ方向の結果を出しているかを指す。提案者自身による検証しかないものは、そう書く。

## 一覧

| 問題点 | 改善策 | 検証したのは | 独立した確認 |
|---|---|---|---|
| MLP は無関係な特徴量に弱く、特徴量の回転に不変 | 埋め込み層、特徴量ごとのスケーリング層 | RealMLP の著者自身 | 部分的 |
| MLP の過学習と最適化の難しさ | 重みを共有した効率的なアンサンブル(TabM) | TabM の著者自身 | TabArena(著者の重なりなし) |
| 初期の TabPFN は小規模・数値特徴のみ | TabPFN v2 | TabPFN v2 の著者自身 | TabArena(著者が重なる) |
| 論文ごとのデータセット選択とチューニングの偏り | チューニング用と評価用のデータを分ける | 表データとドリフト検出の両分野で、別々の著者 | 発想として一致 |
| 時系列異常検知の point-adjust による過大評価 | PA%K、イベント単位の評価、単純な基準線、閾値に依存しない指標 | 提案した著者自身 | 指摘は3本で一致し、2026年の論文の多くが採用 |
| ドリフト検出器の評価の不統一 | 実データへのドリフト注入、時間を考慮した指標 | 提案した著者自身 | 未確認 |
| ドリフト検出が正解ラベルに依存 | 教師なし検出器 | 比較研究 | D3 の強さは2本で一致 |

以下、項目ごとに根拠を示す。

## 表データのモデル

### MLP の弱点と、それを補う設計

**問題点**: Grinsztajn らは、MLP 系のモデルが無関係な特徴量に弱いこと [arxiv-2207.08815#c5](https://arxiv.org/pdf/2207.08815v1#page=7 "This shows that MLPs are less robust to uninformative features")、特徴量の回転に対して不変で列ごとの意味を活かせないこと [arxiv-2207.08815#c6](https://arxiv.org/pdf/2207.08815v1#page=7 "only Resnets are rotationally invariant")、滑らかな関数に偏ること [arxiv-2207.08815#c4](https://arxiv.org/pdf/2207.08815v1#page=6 "For small lengthscales, smoothing the target function on the train set decreases markedly the accuracy of tree-based models, but barely impacts that of NNs.") を、データを加工する実験で示した。
TabM の著者も、表データの MLP は過学習と最適化の問題を抑えて初めて力を発揮すると述べている [arxiv-2410.24210#c21](https://arxiv.org/pdf/2410.24210v3#page=2 "one has to deal with overfitting and optimization issues to reveal that potential.")。

**改善策と検証**:

- **埋め込み層**: Grinsztajn ら自身が、数値特徴量にも埋め込み層を入れる先行研究の改善は、回転不変性を壊すことで説明できるとしている [arxiv-2207.08815#c16](https://arxiv.org/pdf/2207.08815v1#page=8 "The fact that very different types of embeddings seem to improve performance suggests that the sheer presence of an embedding which breaks the invariance is a key part of these improvements.")。また、適切な正則化と最適化があれば、MLP も不規則なパターンを学べる可能性を認めている [arxiv-2207.08815#c17](https://arxiv.org/pdf/2207.08815v1#page=7 "as adequate regularization and careful optimization may allow NNs to learn irregular patterns.")。
- **RealMLP**: 特徴量ごとに学習するスケーリング層で、緩やかな特徴量選択を促す [arxiv-2407.04491#c22](https://arxiv.org/pdf/2407.04491v3#page=5 "To encourage (soft) feature selection, we introduce a scaling layer before the first linear layer")。外れ値は、頑健なスケーリングと滑らかなクリッピングで抑える [arxiv-2407.04491#c23](https://arxiv.org/pdf/2407.04491v3#page=4 "Intuitively, when features have large outliers, smooth clipping prevents the outliers from affecting the result too strongly")。著者の実験では、構造の改良だけでも素の MLP の性能は上がったが、学習方法や既定値などの構造以外の要素も同じくらい重要だった [arxiv-2407.04491#c24](https://arxiv.org/pdf/2407.04491v3#page=10 "our architectural improvements alone are beneficial when applied to MLP-D directly, although non-architectural aspects are at least as important.")。結果として、自分たちのベンチマークでは GBDT と競える水準になった [arxiv-2407.04491#c1](https://arxiv.org/pdf/2407.04491v3#page=1 "RealMLP offers a favorable time-accuracy tradeoff compared to other neural baselines and is competitive with GBDTs in terms of benchmark scores.")。
- **TabPFN v2**: 無関係な特徴量や外れ値に対して非常に頑健だと報告している [doi-10.1038_s41586-024-08328-6#c15](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=6 "The results show that TabPFN is very robust to uninformative features and outliers")。

**この記事の整理として**: RealMLP のスケーリング層と TabPFN v2 の頑健性は、Grinsztajn らが指摘した「無関係な特徴量への弱さ」に対応する改善と読める。ただし、どちらの論文も、Grinsztajn らの指摘に応答する形では検証していない。

**独立した確認**: 部分的にある。RealMLP の改良が GBDT と競えるという結果は、Grinsztajn らのデータセットの分類では成り立たなかった(RealMLP 論文の勝敗表を参照)。条件によって効果が変わることを、著者自身が認めている [arxiv-2407.04491#c9](https://arxiv.org/pdf/2407.04491v3#page=10 "For classification, using AUROC instead of classification error (Figure 3, Appendix B.5) favors GBDTs.") [arxiv-2407.04491#c10](https://arxiv.org/pdf/2407.04491v3#page=10 "The use of different aggregation metrics than the shifted geometric mean reduces the advantage of TD methods")。

### 効率的なアンサンブルで MLP を強くする(TabM)

**改善策**: TabM は、重みの大半を共有した多数の MLP を同時に学習する [arxiv-2410.24210#c11](https://arxiv.org/pdf/2410.24210v3#page=2 "the two key reasons for TabM's high performance are the collective training of the underlying implicit MLPs and the weight sharing.")。重みの共有は、表データで効果的な正則化として働いた [arxiv-2410.24210#c10](https://arxiv.org/pdf/2410.24210v3#page=5 "Thus, constraining the ensemble with weight sharing turns out to be a highly effective regularization on tabular tasks.")。

**検証**: 著者の46データセットでの比較では、深層学習の中で最良だった [arxiv-2410.24210#c1](https://arxiv.org/pdf/2410.24210v3#page=1 "In particular, we find that TabM demonstrates the best performance among tabular DL models.")。GBDT とは「十分に競える」という表現にとどまる [arxiv-2410.24210#c5](https://arxiv.org/pdf/2410.24210v3#page=2 "TabM easily competes with GBDT and outperforms prior tabular DL models")。

**独立した確認**: TabArena では、設定のアンサンブルを含めて比べると、TabM を含むニューラルネットが最強の単一モデルになった [arxiv-2506.16791#c12](https://arxiv.org/pdf/2506.16791v4#page=7 "after post-hoc ensembling, neural networks are the strongest single models on average in TabArena-v0.1.")。TabArena の著者は TabM の著者と重ならない(TabArena の利益相反の開示に TabM は含まれない [arxiv-2506.16791#c22](https://arxiv.org/pdf/2506.16791v4#page=11 "D.H. is one of the authors of RealMLP and one of the authors of TabICL.") [arxiv-2506.16791#c23](https://arxiv.org/pdf/2506.16791v4#page=11 "L.P. and F.H. are a subset of the authors of TabPFNv2."))。この点で、TabM の強さには比較的独立した裏付けがある。

### 初期の TabPFN の制約と TabPFN v2

**問題点**: 2023年版の TabPFN は、訓練1,000件以下・数値特徴のみ・10クラス以下という小規模な問題が対象で [arxiv-2207.01848#c2](https://arxiv.org/pdf/2207.01848v6#page=2 "tasks (≤1 000 training examples, ≤100 purely numerical features without missing values and ≤10 classes)")、構造上大きなデータに広げにくかった [arxiv-2207.01848#c12](https://arxiv.org/pdf/2207.01848v6#page=10 "the underlying Transformer architecture only scales to small datasets")。カテゴリ特徴や欠損値があると弱くなった [arxiv-2207.01848#c7](https://arxiv.org/pdf/2207.01848v6#page=9 "Generally, TabPFN is less strong when categorical features or missing values are present.")。

**改善策と検証**: TabPFN v2 は、扱えるデータの規模を大きく広げ、回帰・カテゴリ特徴・欠損値に対応したと報告している [doi-10.1038_s41586-024-08328-6#c3](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=2 "the new TabPFN scales to 50× larger datasets; supports regression tasks, categorical data and missing values; and is robust to unimportant features and outliers.")。1万件以下のデータでは、既存手法を大きく上回った [doi-10.1038_s41586-024-08328-6#c1](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=1 "a tabular foundation model that outperforms all previous methods on datasets with up to 10,000 samples by a wide margin, using substantially less training time.")。ただし著者自身、この結果は1万件・500特徴を超える規模での性能の根拠にはならないと断っている [doi-10.1038_s41586-024-08328-6#c14](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=6 "these results should not be taken as evidence that TabPFN scales well beyond the 10,000 samples and 500 features considered here.")。

**独立した確認**: TabArena も、適用条件内のデータで TabPFNv2 が大差で上位だったと報告している [arxiv-2506.16791#c13](https://arxiv.org/pdf/2506.16791v4#page=7 "TabPFNv2 outperforms related approaches by a large margin, establishing tabular foundation models as the go-to solution for datasets within their constraints.")。ただし、TabArena の著者2名は TabPFNv2 の著者でもあり [arxiv-2506.16791#c23](https://arxiv.org/pdf/2506.16791v4#page=11 "L.P. and F.H. are a subset of the authors of TabPFNv2.")、TabPFN v2 の著者2名は表データ基盤モデルの企業に所属している [doi-10.1038_s41586-024-08328-6#c18](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=13 "F.H. and N.H. are affiliated with PriorLabs, a company focused on developing tabular foundation models.")。著者の重ならない検証としては、2023年版を対象にした TabZilla の結果がある。TabZilla では、訓練データを間引いて使っても、平均で全手法を上回った [arxiv-2305.02997#c3](https://arxiv.org/pdf/2305.02997v4#page=1 "we find that it outperforms all other algorithms on average, even when randomly sampling 3000 training datapoints.")。

### 注意機構ベースのモデルの計算コスト

**問題点**: FT-Transformer の提案者自身が、ResNet より多くの計算資源を要し、特徴量が非常に多いと扱いにくいと認めていた [arxiv-2106.11959#c9](https://arxiv.org/pdf/2106.11959v5#page=5 "FT-Transformer requires more resources (both hardware and time) for training than simple models such as ResNet")。

**その後の確認**: 同じグループの TabM 論文で、注意機構や検索ベースのモデルは、大規模データでは学習時間が極端に長いか、そのままでは適用できないことが示された [arxiv-2410.24210#c14](https://arxiv.org/pdf/2410.24210v3#page=8 "As expected, attention- and retrieval-based models struggle, yielding extremely long training times, or being simply inapplicable without additional effort.")。MLP 系が最速で、TabM がそれに次ぐ [arxiv-2410.24210#c13](https://arxiv.org/pdf/2410.24210v3#page=8 "Simple MLPs are the fastest DL models, with TabM being the runner-up.")。両論文に共通の著者がいるため、独立した確認ではない。

## 評価方法の弱点と改善

### チューニングと評価に同じデータを使う問題

**問題点**: Shwartz-Ziv らは、深層モデルが自分の論文のデータセットでだけ強く見えることを示し [arxiv-2106.03253#c4](https://arxiv.org/pdf/2106.03253v2#page=6 "Each deep model was better only on the datasets that appeared in its own paper.")、その理由として、データセット選択の偏り [arxiv-2106.03253#c5](https://arxiv.org/pdf/2106.03253v2#page=6 "The first possibility is selection bias.") とチューニング努力の差 [arxiv-2106.03253#c6](https://arxiv.org/pdf/2106.03253v2#page=6 "The second possibility is differences in the optimization of hyperparameters.") を挙げた。

**改善策**: 同じ発想の対策が、**別の分野で別の著者によって**提案されている。

- **表データ(RealMLP)**: 既定値を調整するメタ訓練用のデータと、評価するメタテスト用のデータを分けた [arxiv-2407.04491#c3](https://arxiv.org/pdf/2407.04491v3#page=1 "We tune RealMLP and the default parameters on a meta-train benchmark with 118 datasets and compare them to hyperparameter-optimized versions on a disjoint meta-test benchmark with 90 datasets")。調整済みの既定値はメタテストにもよく移った [arxiv-2407.04491#c7](https://arxiv.org/pdf/2407.04491v3#page=9 "indicating that the tuned defaults transfer very well to the meta-test benchmark.")。
- **ドリフト検出(Cerqueira ら)**: 同じデータでチューニングと評価をすると楽観的になると指摘し [arxiv-2606.07789#c8](https://arxiv.org/pdf/2606.07789v1#page=4 "using the same dataset for optimizing and evaluating the detector can cause overfitting and lead to overly optimistic performance estimates reported in the respective papers.")、データセットを1つ抜いてチューニングする方法を提案した [arxiv-2606.07789#c7](https://arxiv.org/pdf/2606.07789v1#page=4 "we propose a leave-one-dataset-out cross-validation approach for optimizing the hyperparameters of drift detectors.")。この方法でのチューニングは、既定の設定より検出性能を大きく上げた [arxiv-2606.07789#c4](https://arxiv.org/pdf/2606.07789v1#page=2 "hyperparameter optimization using our proposed approach significantly improves detection performance over default configurations.")。

**この記事の整理として**: 「調整に使ったデータで評価しない」という同じ原則が、2つの分野で独立に採用されていることは、この原則の一般性を示している。

### 時系列異常検知の point-adjust

**問題点**: point-adjust を使うと、ランダムなスコアでも最先端に見える。これは Kim ら [arxiv-2109.05257#c1](https://arxiv.org/pdf/2109.05257v2#page=1 "the PA protocol has a great possibility of overestimating the detection performance; that is, even a random anomaly score can easily turn into a state-of-the-art TAD method.")、Sehili ら [arxiv-2308.13068#c2](https://arxiv.org/pdf/2308.13068v2#page=1 "So flawed is one very popular protocol, the so-called point-adjust protocol, that a random guess can be shown to systematically outperform all algorithms developed so far.")、TAB [arxiv-2506.18046#c6](https://arxiv.org/pdf/2506.18046v2#page=2 "even random methods have a good chance to predict at least one point in larger anomaly windows") の3本が独立に指摘している。

**改善策**:

- **PA%K**(Kim ら): 区間の中で一定割合以上を検出したときだけ区間全体を検出とみなす。過大評価と過小評価の両方を和らげる [arxiv-2109.05257#c12](https://arxiv.org/pdf/2109.05257v2#page=4 "which can mitigate the overestimation effect of F1PA and the possibility of underestimation of F1.")。
- **単純な基準線**(Kim ら): 訓練していないモデルの性能を基準線にする [arxiv-2109.05257#c13](https://arxiv.org/pdf/2109.05257v2#page=4 "we suggest establishing a new baseline with the F1 measured from the prediction of a randomly initialized reconstruction model with simple architecture")。
- **イベント単位の評価**(Sehili ら): 点単位の評価がすべてのデータに適するわけではないとして提案された [arxiv-2308.13068#c11](https://arxiv.org/pdf/2308.13068v2#page=2 "We also review the more objective point-wise protocol and show that it is not appropriate for all kinds of datasets and use-cases.")。
- **PCA の基準線**(Sehili ら): 単純な前処理と後処理を加えた PCA を基準線にする [arxiv-2308.13068#c3](https://arxiv.org/pdf/2308.13068v2#page=1 "we propose a simple, yet challenging, baseline based on Principal Components Analysis (PCA) that surprisingly outperforms many recent Deep Learning (DL) based approaches on popular benchmark datasets.") [arxiv-2308.13068#c10](https://arxiv.org/pdf/2308.13068v2#page=14 "we use simple pre-processing and post-processing blocks (input scaling, clipping and score smoothing) that significantly improve the score.")。

**検証と独立した確認**: 改善策の検証は、それぞれ提案者自身によるものである。ただし、Sehili らの結果は Kim らの指摘と同じ方向を示している。point-adjust を前提に開発された手法が、他の評価方法ではランダムな推測と区別できなかった [arxiv-2308.13068#c4](https://arxiv.org/pdf/2308.13068v2#page=13 "Algorithms that were developed using point-adjust as the sole target fail to reach any score better than a random guess when evaluated with other")。この点で、問題点の指摘は独立に確認されている。

**改善策の普及**: 2026年10月に承認した18本では、point-adjust を主な評価に使っていたのは3本(SACM、WinoTS、AMAD)だった [arxiv-2609.39489#c3](https://arxiv.org/pdf/2609.39489v1#page=10 "Raw and +SACM share the benchmark point-adjusted (PA) protocol [37, 39] for paired comparison") [arxiv-2609.39337#c2](https://arxiv.org/pdf/2609.39337v1#page=6 "TSLib evaluation protocol and report point-adjusted precision, recall, and F1") [arxiv-2504.06643#c2](https://arxiv.org/pdf/2504.06643v3#page=10 "we decided not to break this tradition, with the same adjustment method as [30]")。多くは VUS-PR や affiliation F1 などを使い、Kim らを引用して point-adjust を避けると明記する論文もある [doi-10.24963_ijcai.2026_276#c2](https://www.ijcai.org/proceedings/2026/0276.pdf#page=5 "As noted by [Kim et al., 2022], point-adjustment metrics can lead to misleading rankings")。ただし、この18本は既存カードを引用していることで選ばれており、評価の問題を意識した論文に偏っている可能性がある。詳しくは[時系列異常検知の記事](../tasks/time-series-anomaly-detection.md)を参照。

**改善策自身の限界**: 統一された評価パイプラインを作った TAB でも、すべての閾値のうち最良の値を報告している [arxiv-2506.18046#c9](https://arxiv.org/pdf/2506.18046v2#page=8 "we conduct metric calculations at all thresholds and report the best results.")。閾値をテストデータで選ぶという、より根本的な問題 [arxiv-2109.05257#c14](https://arxiv.org/pdf/2109.05257v2#page=7 "existing TAD methods set the threshold after investigating the test dataset or simply use the optimal threshold that yields the best F1.") は残っている。2026年の論文にも、評価データの正解ラベルを使って閾値を選ぶものが複数ある [arxiv-2609.36765#c2](https://arxiv.org/pdf/2609.36765v1#page=8 "with the threshold that maximizes the F1 score using test labels") [arxiv-2610.00978#c4](https://arxiv.org/pdf/2610.00978v1#page=8 "Threshold-dependent metrics use oracle thresholds selected from evaluation labels")。閾値に依存しない評価は、この問題への新しい対応である [arxiv-2608.02821#c2](https://arxiv.org/pdf/2608.02821v1#page=1 "Instead of scoring only the final alarms, we evaluate Stage 1 directly using normalized residual energy")。また、ベンチマークのデータ自体に欠陥があるという指摘 [arxiv-2009.13807#c1](https://arxiv.org/pdf/2009.13807v5#page=1 "These flaws are triviality, unrealistic anomaly density, mislabeled ground truth and run-to-failure bias.") に対しては、新しいアーカイブが作られた [arxiv-2009.13807#c9](https://arxiv.org/pdf/2009.13807v5#page=1 "with this paper we introduce the UCR Time Series Anomaly Archive.")。しかし、その上での比較はこのリポジトリにはまだない。

### ドリフト検出器の評価

**問題点**: 合成データへの依存、指標の不統一、不透明なチューニング [arxiv-2606.07789#c1](https://arxiv.org/pdf/2606.07789v1#page=1 "studies rely on oversimplified synthetic data generators, adopt incompatible metrics, and lack transparency in hyperparameter selection")。従来の指標がストリームの長さに依存すること [arxiv-2606.07789#c5](https://arxiv.org/pdf/2606.07789v1#page=3 "MTFA and MDT are highly dependent on stream length and drift spacing")、F1 では遅い検出も満点になりうること [arxiv-2606.07789#c6](https://arxiv.org/pdf/2606.07789v1#page=3 "its formulation ignores the temporal aspect: a detector with unacceptable delay can still achieve perfect F1.")。

**改善策**: 実データにドリフトを人工的に注入して正解を作り、時間を考慮した指標を使い、データセットを1つ抜いてチューニングする枠組みが提案された [arxiv-2606.07789#c7](https://arxiv.org/pdf/2606.07789v1#page=4 "we propose a leave-one-dataset-out cross-validation approach for optimizing the hyperparameters of drift detectors.")。

**改善策自身の限界**: 著者自身が、元のストリームを並べ替えるため時間構造が失われること [arxiv-2606.07789#c17](https://arxiv.org/pdf/2606.07789v1#page=8 "it also removes any inherent temporal structure.")、正解ラベルがすぐ得られると仮定していること [arxiv-2606.07789#c16](https://arxiv.org/pdf/2606.07789v1#page=8 "it assumes immediate feedback, with labels being readily available at each step after inference.") を限界として挙げている。この枠組みでの結論(SEED・STEPD が上位)は、Aguiar らの結論と食い違う。詳しくは[ドリフト検出の記事](../tasks/drift-detection.md)を参照。

### ドリフト検出が正解ラベルに依存する問題

**問題点**: 多くの検出器は、予測の直後に正解ラベルが得られると仮定している [arxiv-2004.05785#c11](https://arxiv.org/pdf/2004.05785v1#page=14 "Most existing drift detection and adaptation algorithms assume the ground true label is available after classification/prediction, or extreme verification latency.") [doi-10.1007_s41060-024-00620-y#c1](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=1 "Most algorithms proposed in the literature depend on the immediate availability of ground truth class labels.")。誤り率ベースの検出器は誤検知も多い [arxiv-2311.06396#c10](https://arxiv.org/pdf/2311.06396v2#page=24 "Drift detectors that rely on error rates often generate numerous false alarms.")。

**改善策と検証**: 入力だけを見る教師なしの検出器が、実データで比較された [doi-10.1007_s41060-024-00620-y#c3](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=1 "Seven of these algorithms are evaluated with common concept drift detection metrics on eleven real-world data streams")。D3 が直接の評価で最良だった [doi-10.1007_s41060-024-00620-y#c7](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=13 "In these experiments, D3 outperforms other detectors by a large margin")。異常の監視が目的なら、誤差ベースの手法を避けるべきだという指針もある [arxiv-2310.15826#c8](https://arxiv.org/pdf/2310.15826v1#page=27 "loss-based strategies should be avoided when the target of the drift detection is monitoring for anomalous behavior.")。

**独立した確認**: D3 が良いという結果は、Window Dilemma の著者による別の実験でも得られている [arxiv-2602.06456#c7](https://arxiv.org/pdf/2602.06456v1#page=7 "Of the drift detectors, D3-HT performed the best for both the NB and HT base models.")。

**改善策自身の限界**: 教師なしの検出器は、正解だけが変わる変化を捉えられない [arxiv-2606.07789#c12](https://arxiv.org/pdf/2606.07789v1#page=8 "Unsupervised detectors (ABCD(X) and STUDD) perform better on feature-space drifts (feature permutation, feature filtering) than on label-based changes (class prior, class swaps)")。分類器の精度で検出器を評価すると、警報の多い検出器が有利になる [doi-10.1007_s41060-024-00620-y#c9](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=18 "classifier predictive performance is biased in favor of a higher number of detected concept drifts and adaptations.")。

### データシフト検出の欠如

**問題点**: 実際の機械学習パイプラインでは、入力のシフトの確認がほとんど行われていない [arxiv-1810.11953#c8](https://arxiv.org/pdf/1810.11953v4#page=1 "in practice, ML pipelines rarely inspect incoming data for signs of distribution shift.")。

**改善策と検証**: 学習済みモデルの出力に二標本検定をかける方法が最も良かった [arxiv-1810.11953#c1](https://arxiv.org/pdf/1810.11953v4#page=1 "a two-sample-testing-based approach, using pre-trained classifiers for dimensionality reduction, performs best.")。前提条件が崩れても機能した [arxiv-1810.11953#c2](https://arxiv.org/pdf/1810.11953v4#page=2 "We show (empirically) that BBSD works surprisingly well under a broad set of shifts, even when the label shift assumption is not met.")。

**改善策自身の限界**: 検証は画像データが中心で [arxiv-1810.11953#c12](https://arxiv.org/pdf/1810.11953v4#page=9 "since we have mostly explored a standard image classification setting for our experiments")、ストリーミングデータへの拡張は今後の課題とされている [arxiv-1810.11953#c14](https://arxiv.org/pdf/1810.11953v4#page=9 "shift detection for online data, which would require us to account for and exploit the high degree of correlation between adjacent time steps")。

## 2026年の論文で繰り返し見られる評価の弱点(テーマ横断)

候補 Issue で承認した2026年の論文と、解釈可能性・量子化のテーマで追加した論文をカード化したところ、**同じ種類の評価の弱点が分野をまたいで繰り返し現れた**。
ここでは、改善策と対にして整理する。改善策の側も、多くは同じ論文や別の論文の中にすでにある。

| 弱点 | 表データ | ドリフト検出・変化点検出 | 解釈可能性・量子化 | 改善の例 |
|---|---|---|---|---|
| 提案手法と比較対象の調整の非対称 | 提案手法だけ調整 [arxiv-2608.04348#c4](https://arxiv.org/pdf/2608.04348v1#page=6 "We tune iStructTab with Optuna [1] for 20 trials per dataset, following common tabular tuning practice [27, 26, 25, 24]; baselines use recommended settings.")、比較対象だけ AutoML で調整し、提案側の基盤モデルは調整なし(因果効果推定) [arxiv-2609.03003#c3](https://arxiv.org/pdf/2609.03003v1#page=18 "To provide strong, competitive baselines, all underlying nuisance models are selected via FLAML AutoML (v2.3.5; Wang et al. (2021)) run independently per nuisance, per estimator, per RealCause realization, and per cohort with a 900-second budget and 3-fold cross-validation.") [arxiv-2609.03003#c4](https://arxiv.org/pdf/2609.03003v1#page=19 "These models are downloaded out-of-the-box from their respective sources and applied without any parameter or hyperparameter tuning.") | 提案手法は経験則で設定し、比較対象は AUC が最良の設定を報告 [arxiv-2609.24278#c5](https://arxiv.org/pdf/2609.24278v1#page=19 "For all experiments, hyperparameters were selected according to a fixed set of heuristic rules.") [arxiv-2609.24278#c6](https://arxiv.org/pdf/2609.24278v1#page=23 "The following hyperparameter resulted in the best AUC scores for RIO-LE:") | 提案手法は最適化、比較対象は先行研究の設定 [arxiv-2004.13912#c5](https://arxiv.org/pdf/2004.13912v2#page=18 "For computational efficiency, we tune these hyperparameters using Bayesian optimization [11, 39] based on cross-validation performance with a single train-validation split for each fold.") [arxiv-2004.13912#c6](https://arxiv.org/pdf/2004.13912v2#page=18 "We use the open-source implementation [26] with the parameters specified by prior work [5] for a fair comparison.") | 全手法を検証データで同じように調整 [arxiv-2609.12712#c4](https://arxiv.org/pdf/2609.12712v1#page=12 "To ensure fairness, we re-implemented all baselines based on the official code or their original papers and performed a comprehensive grid search over key hyper-parameters (see Appendix C.5 for details).") [arxiv-2609.12712#c5](https://arxiv.org/pdf/2609.12712v1#page=12 "We tune all model hyper-parameters based on validation performance.") |
| 比較対象を既定値のまま使う | [arxiv-2608.27882#c4](https://arxiv.org/pdf/2608.27882v1#page=7 "For each baseline, we use its official implementation and default configuration, including the default preprocessing and ensemble size.") [arxiv-2609.36337#c5](https://arxiv.org/pdf/2609.36337v1#page=17 "As shown in the TabArena evaluation by Erickson et al. (2026), CatBoost performs very well out of the box without hyperparameter tuning, supporting its use as a default configuration baseline.") | DDM・ADWIN・KSWIN を既定値で [arxiv-2609.04388#c4](https://arxiv.org/pdf/2609.04388v1#page=11 "the river reference implementations of DDM and ADWIN [17, 29] as retraining triggers with always-deploy on fire, run at their registered reference parameters — the implementations’ default DDM thresholds and ADWIN δ = 0.002 — on 8 monitoring labels per window (800 per stream)") [arxiv-2609.09432#c3](https://arxiv.org/pdf/2609.09432v1#page=36 "Specifically, ADWIN used δ = 0.002, while KSWIN used αKS = 0.005, WKS = 100, and SKS = 30.") | 攻撃対象の説明手法は既定の実装 [arxiv-1911.02508#c3](https://arxiv.org/pdf/1911.02508v2#page=4 "We use default LIME tabular implementation without discretization, and the default Kernel SHAP implementation with kmeans with 10 clusters as the background distribution.") | 既定値であることと、その限界を明記する [arxiv-2609.04388#c5](https://arxiv.org/pdf/2609.04388v1#page=24 "DDM and ADWIN were run at their registered reference parameters and were not tuned; their cells characterize that configuration, and a parameter sweep would be required before reading them as properties of the methods.") |
| 評価データ上での選択(オラクル) | データセットごとの設定選択はベンチマーク上の調整にあたる(著者はこれを避け、一律の設定で報告) [arxiv-2609.04540#c6](https://arxiv.org/pdf/2609.04540v1#page=33 "But this only works as an oracle: it amounts to tuning on the benchmark.") | 課題ごとの層の選択を、最良の層(オラクル)との近さで正当化 [arxiv-2609.33940#c5](https://arxiv.org/pdf/2609.33940v1#page=9 "Layer-0 suffices for Push-T (AUC within 0.02 of oracle in-distribution, within 0.01 out-of-distribution), whereas layer-5 (deepest) is consistently oracle-optimal across all seeds and regimes on TwoRoom.") | 較正データが評価と同じコーパス(C4)の学習データから取られ、完全なゼロショットではない [arxiv-2210.17323#c5](https://arxiv.org/pdf/2210.17323v2#page=14 "We note that the calibration data used by GPTQ is sampled from the C4 training set, this task is thus not fully zero-shot.") | テストで選んだ値は参考値・上限としてのみ示す [arxiv-2608.30337#c5](https://arxiv.org/pdf/2608.30337v2#page=22 "Honest F1 uses per-label thresholds selected on 5-fold out-of-fold predictions over the in-context set and frozen before the test set is touched.") [arxiv-2609.32898#c5](https://arxiv.org/pdf/2609.32898v1#page=7 "Both use ground-truth test AUROCs and are reported as references.") |
| 結果を再実行せず転用 | リーダーボードの値の利用 [arxiv-2609.17488#c3](https://arxiv.org/pdf/2609.17488v1#page=10 "We take the published leaderboard scores as the reference for existing baselines (accessed September 15, 2026) and then report the Elo rating computed by the official TabArena evaluation pipeline, ensuring direct comparability with the leaderboard results.") | 比較対象の一部の結果を先行研究から転用(グラフの分布外検出) [arxiv-2609.35703#c3](https://arxiv.org/pdf/2609.35703v1#page=6 "against GNNSafe, GNNSafe++, and GPN [30] at the values reported by Wu et al. [36]") | — | 同じ実装・同じ条件で再実行する [arxiv-2609.12712#c4](https://arxiv.org/pdf/2609.12712v1#page=12 "To ensure fairness, we re-implemented all baselines based on the official code or their original papers and performed a comprehensive grid search over key hyper-parameters (see Appendix C.5 for details).") |
| 開発元による自己評価 | 自社の基盤モデルの技術報告 [arxiv-2608.25774#c6](https://arxiv.org/pdf/2608.25774v1#page=2 "EXAONE Tabular is LG AI Research’s first tabular foundation model family") | 運用事例を開発企業が報告 [arxiv-2608.08245#c6](https://arxiv.org/pdf/2608.08245v1#page=2 "PROXYDRIFT has been deployed in a major cloud-based productivity suite serving hundreds of millions of users, where it monitors multiple application scenarios continuously and generates synthetic evaluation data on a weekly cadence.") | 提案者が評価指標も設計 [arxiv-1905.04610#c4](https://arxiv.org/pdf/1905.04610v1#page=6 "We designed 21 metrics to comprehensively evaluate the performance of local explanation methods, and applied these metrics to eight different explanation methods across three different model types and three datasets (Methods 11).")、開発元による量子化 [arxiv-2609.13031#c5](https://arxiv.org/pdf/2609.13031v1#page=1 "Correspondence: jonas@priorlabs.ai") | 提案者ではない著者による検証(下の節) |
| 平均的な指標が失敗を隠す | データセット間の平均が難しい事例での失敗を隠す [arxiv-2608.28980#c5](https://arxiv.org/pdf/2608.28980v3#page=20 "averaging across datasets with different structural difficulty, as in TabArena and TALENT, can produce a favorable mean while masking failures concentrated in harder or less-represented cases [109].") | 間接的な精度での評価は警報の多い検出器に有利 [doi-10.1007_s41060-024-00620-y#c9](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=18 "classifier predictive performance is biased in favor of a higher number of detected concept drifts and adaptations.") | 通常の性能では信頼性の劣化が見えない [arxiv-2403.15447#c4](https://arxiv.org/pdf/2403.15447v3#page=1 "This increased risk cannot be uncovered by looking at benign performance alone, in turn, mandating comprehensive trustworthiness evaluation in practice.")、全体の精度が部分集合での食い違いを隠す(枝刈り) [arxiv-1911.05248#c1](https://arxiv.org/pdf/1911.05248v3#page=1 "We ﬁnd that models with radically different numbers of weights have comparable top-line performance metrics but diverge considerably in behavior on a narrow subset of the dataset.") | 失敗や部分集合を直接測る指標を併用する(この記事の整理。量子化では信頼性の包括的な評価が求められている [arxiv-2403.15447#c4](https://arxiv.org/pdf/2403.15447v3#page=1 "This increased risk cannot be uncovered by looking at benign performance alone, in turn, mandating comprehensive trustworthiness evaluation in practice.")) |
| 正解がない・人工的 | — | 正解のドリフト時点は人工的な注入が中心 [arxiv-2609.09432#c5](https://arxiv.org/pdf/2609.09432v1#page=40 "Because the real-world datasets do not provide annotated drift locations or known concept boundaries, ground-truth alarm-quality metrics are evaluated only on the synthetic datasets.") | 説明の正解がなく、別の手法との相関 [arxiv-1902.10186#c6](https://arxiv.org/pdf/1902.10186v3#page=11 "We do not intend to imply that such alternative measures are necessarily ideal or that they should be considered ‘ground truth’.") や公理 [arxiv-1703.01365#c4](https://arxiv.org/pdf/1703.01365v2#page=3 "However, the images resulting from pixel perturbation could be unnatural, and it could be that the scores drop simply because the network has never seen anything like it in training.") で代用する | 正解を作り込んだ設定で検証する [arxiv-1602.04938#c3](https://arxiv.org/pdf/1602.04938v3#page=6 "In particular, we train both classifiers such that the maximum number of features they use for any instance is 10, and thus we know the gold set of features that the are considered important by these models.") [arxiv-2006.16234#c6](https://arxiv.org/pdf/2006.16234v1#page=5 "To create an experimental setting where we have access to the ground truth, we take the real RNA-seq data and simulate a drug response label as a function of 40 randomly selected causal genes (out of 1000 total genes).") |

### 提案者ではない著者による検証の例

- **表データの基盤モデル**: 既存の基盤モデルの開発元ではない著者による比較は、基盤モデル優勢 [arxiv-2609.02766#c2](https://arxiv.org/pdf/2609.02766v1#page=1 "TFMs dominate, out of the box and after tuning.") [arxiv-2609.06080#c2](https://arxiv.org/pdf/2609.06080v2#page=1 "Under a fixed single-estimator protocol with bounded tuning, these models ranked above the evaluated task-specific baselines, including XGBoost and CatBoost, in aggregate.") と、そうとは言えない結果 [arxiv-2608.05265#c5](https://arxiv.org/pdf/2608.05265v1#page=18 "Tree-based models such as ExtraTrees, CatBoost, and XGBoost required Bayesian hyperparameter search, whereas TabPFN was run with static settings with no dataset-specific tuning and still matched or exceeded them.") に分かれた。自ら学習した基盤モデルが勾配ブースティング木を上回らなかったと報告する研究もある [arxiv-2609.25541#c5](https://arxiv.org/pdf/2609.25541v1#page=7 "Neither arm beats gradient-boosted trees, with ds at 28:84 on classification and 4:28 on regression and jepa at 27:87 and 3:29 (Figure 4).")。条件の違いは [表データの記事](../tasks/tabular-gbdt-vs-deep-learning.md) を参照。
- **事後説明**: LIME の共著者を含む研究者が、LIME と SHAP の弱点を示した [arxiv-1911.02508#c7](https://arxiv.org/pdf/1911.02508v2#page=7 "Extensive experimentation with real world data from criminal justice and credit scoring domains demonstrates that our approach is effective at generating adversarial classifiers that can fool post hoc explanation techniques, finding that LIME is more vulnerable than SHAP.")。ROAR と Sanity Checks は、勾配系の説明手法の弱点を示した [arxiv-1806.10758#c4](https://arxiv.org/pdf/1806.10758v3#page=9 "Surprisingly, we find that the commonly used base estimators, Gradients, Integrated Gradients and Guided BackProp are worse or on par with a random assignment of importance.") [arxiv-1810.03292#c4](https://arxiv.org/pdf/1810.03292v3#page=3 "Of the methods tested, Gradients & GradCAM pass the sanity checks, while Guided BackProp & Guided GradCAM are invariant to higher layer parameters; hence, fail.")(どちらも Integrated Gradients の著者と同じ Google の研究者を含む)。
- **量子化**: 量子化の害を示した研究(信頼性 [arxiv-2403.15447#c4](https://arxiv.org/pdf/2403.15447v3#page=1 "This increased risk cannot be uncovered by looking at benign performance alone, in turn, mandating comprehensive trustworthiness evaluation in practice.")、知識を要するタスク [arxiv-2310.01382#c6](https://arxiv.org/pdf/2310.01382v2#page=5 "3 ∼8-10% drop in performance for non-aggressive 8-bit quantization indicates that along with chasing for aggressive quantization levels (1-2 bits), it is also important to focus on yet unsolved 8-bit quantization.")、少数派のデータ [arxiv-2010.03058#c1](https://arxiv.org/pdf/2010.03058v2#page=1 "We further establish that for CIE examples, compression ampliﬁes existing algorithmic bias."))は、評価対象の量子化手法の提案者ではない著者によるものである(ただし信頼性と知識を要するタスクの2本は著者が一部重なる)。

## 全体から見えること

- **改善の検証は、提案者自身によるものが多い**。著者の重ならない検証があるのは、TabM(TabArena)と D3(Window Dilemma と Lukats ら)など一部にとどまる。
- **同じ原則が分野をまたいで現れる**。「調整に使ったデータで評価しない」(RealMLP と Cerqueira ら)と「単純な基準線と比べる」(Kim ら、Sehili ら)は、別々の分野・著者から出ている。
- **改善策にも新しい限界がある**。TAB の最良閾値、Cerqueira らの並べ替え、教師なし検出器が正解の変化を捉えられないこと、などである。改善は一度で終わらず、次の指摘につながっている。

- **2026年の論文でも同じ弱点が繰り返されている**。調整の非対称、既定値のままの比較対象、評価データ上での選択、結果の転用、開発元による自己評価は、表データとドリフト検出・変化点検出の2026年の論文に現れ、結果の転用を除く弱点は解釈可能性・量子化の論文(多くは2026年以前)にも現れた(上の表)。一方で、改善の例も同じ時期の論文の中にある。

**この記事に含まれていないもの**: このリポジトリにまだカードのない、個々の手法の後続論文(TabPFN v2 以後の表データ基盤モデル、AnomalyTransformer などの改良版)。新着論文の候補 Issue には、それらしい論文(TabPFN 系の後継モデルなど)が多数挙がっている。

## 参照カード

この記事は、このリポジトリの39本すべてのカードを対象にしている。個々の根拠は本文のリンクから原論文の該当ページを開ける。カードの一覧は [generated/index.md](../../generated/index.md) を参照。
- [arxiv-2106.03253](../../papers/arxiv-2106.03253.yaml) Shwartz-Ziv et al., "Tabular Data: Deep Learning is Not All You Need"
- [arxiv-2106.11959](../../papers/arxiv-2106.11959.yaml) Gorishniy et al., "Revisiting Deep Learning Models for Tabular Data"
- [arxiv-2207.08815](../../papers/arxiv-2207.08815.yaml) Grinsztajn et al., "Why do tree-based models still outperform deep learning on tabular data?"
- [arxiv-2207.01848](../../papers/arxiv-2207.01848.yaml) Hollmann et al., "TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second"
- [arxiv-2305.02997](../../papers/arxiv-2305.02997.yaml) McElfresh et al., "When Do Neural Nets Outperform Boosted Trees on Tabular Data?"
- [arxiv-2506.16791](../../papers/arxiv-2506.16791.yaml) Erickson et al., "TabArena: A Living Benchmark for Machine Learning on Tabular Data"
- [doi-10.1038_s41586-024-08328-6](../../papers/doi-10.1038_s41586-024-08328-6.yaml) Hollmann et al., "Accurate predictions on small data with a tabular foundation model"
- [arxiv-2410.24210](../../papers/arxiv-2410.24210.yaml) Gorishniy et al., "TabM: Advancing Tabular Deep Learning with Parameter-Efficient Ensembling"
- [arxiv-2407.04491](../../papers/arxiv-2407.04491.yaml) Holzmüller et al., "Better by Default: Strong Pre-Tuned MLPs and Boosted Trees on Tabular Data"
- [arxiv-2004.05785](../../papers/arxiv-2004.05785.yaml) Lu et al., "Learning under Concept Drift: A Review"
- [arxiv-1810.11953](../../papers/arxiv-1810.11953.yaml) Rabanser et al., "Failing Loudly: An Empirical Study of Methods for Detecting Dataset Shift"
- [arxiv-2311.06396](../../papers/arxiv-2311.06396.yaml) Aguiar et al., "A comprehensive analysis of concept drift locality in data streams"
- [arxiv-2606.07789](../../papers/arxiv-2606.07789.yaml) Cerqueira et al., "A Framework for Evaluating and Benchmarking Concept Drift Detection Methods"
- [arxiv-2602.06456](../../papers/arxiv-2602.06456.yaml) Gower-Winter et al., "The Window Dilemma: Why Concept Drift Detection is Ill-Posed"
- [doi-10.1007_s41060-024-00620-y](../../papers/doi-10.1007_s41060-024-00620-y.yaml) Lukats et al., "A benchmark and survey of fully unsupervised concept drift detectors on real-world data streams"
- [arxiv-2310.15826](../../papers/arxiv-2310.15826.yaml) Hinder et al., "One or Two Things We know about Concept Drift -- A Survey on Monitoring Evolving Environments"
- [arxiv-2109.05257](../../papers/arxiv-2109.05257.yaml) Kim et al., "Towards a Rigorous Evaluation of Time-series Anomaly Detection"
- [arxiv-2009.13807](../../papers/arxiv-2009.13807.yaml) Wu et al., "Current Time Series Anomaly Detection Benchmarks are Flawed and are Creating the Illusion of Progress"
- [arxiv-2308.13068](../../papers/arxiv-2308.13068.yaml) Sehili et al., "Multivariate Time Series Anomaly Detection: Fancy Algorithms and Flawed Evaluation Methodology"
- [arxiv-2506.18046](../../papers/arxiv-2506.18046.yaml) Qiu et al., "TAB: Unified Benchmarking of Time Series Anomaly Detection Methods"
- [arxiv-2211.05244](../../papers/arxiv-2211.05244.yaml) Darban et al., "Deep Learning for Time Series Anomaly Detection: A Survey"
- [arxiv-2608.02821](../../papers/arxiv-2608.02821.yaml) Shi et al., "What the Detector Can See: Evaluating CPS Anomaly Detectors Independently of the Decision Rule"
- [arxiv-2609.39215](../../papers/arxiv-2609.39215.yaml) Parrino et al., "In a Streaming World, Should You Stand Still? A Comprehensive Benchmark of Anomaly Detection in Streams"
- [arxiv-2610.01168](../../papers/arxiv-2610.01168.yaml) Stanzione et al., "Detect, Explain, Interpret: An End-to-End Benchmark for Time Series Anomaly Detection, Explainability and Interpretability"
- [arxiv-2609.38004](../../papers/arxiv-2609.38004.yaml) Guo et al., "No Scale Left Behind: Multi-Scale Autoencoder with Bi-directional Attention for Time Series Anomaly Detection"
- [arxiv-2609.31470](../../papers/arxiv-2609.31470.yaml) Sun et al., "Beyond Empirical Support: Structured Outlier Generation via Sinkhorn Optimal Transport"
- [arxiv-2609.28022](../../papers/arxiv-2609.28022.yaml) Lee et al., "PISCES: Physics-Informed Solar-wind Convolutional autoEncoder for Space-weather Anomaly Detection and Early Warning"
- [arxiv-2608.01885](../../papers/arxiv-2608.01885.yaml) Chao et al., "CARE: A Cascaded Framework for Efficient and Reliable Time Series Anomaly Detection"
- [arxiv-2609.39489](../../papers/arxiv-2609.39489.yaml) Zhong et al., "Towards Robust Time Series Learning via Capacity-Centric Modulation"
- [arxiv-2609.38789](../../papers/arxiv-2609.38789.yaml) Koo et al., "LEARN-TS: LLM-Enhanced Alignment and Reconstruction with Normality Guidance for Multivariate Time-Series Anomaly Detection"
- [arxiv-2610.01223](../../papers/arxiv-2610.01223.yaml) Berghaus et al., "Have an LLM Write Your Anomaly Detector: Autonomous Discovery of Compact, Interpretable Detectors for Time Series"
- [arxiv-2610.00978](../../papers/arxiv-2610.00978.yaml) Lan et al., "Generalist Representation, Specialist Detection: TS-Router for Time-Series Anomaly Detection"
- [arxiv-2609.39337](../../papers/arxiv-2609.39337.yaml) Major et al., "WinoTS: Wavelet-based Self-Distillation for Time Series Models"
- [arxiv-2609.39257](../../papers/arxiv-2609.39257.yaml) Vautier et al., "From Benchmarks to Production: Transferring Time Series Anomaly Detection Methods for Electricity Production Monitoring"
- [arxiv-2609.36765](../../papers/arxiv-2609.36765.yaml) Zhang et al., "Graph-Spectral Flow Matching for Multivariate Time Series Anomaly Detection"
- [arxiv-2609.29194](../../papers/arxiv-2609.29194.yaml) Levy et al., "Continuous Online Fault Detection for Mobile Robots via Adaptive Edge Models"
- [arxiv-2504.06643](../../papers/arxiv-2504.06643.yaml) Huang et al., "AMAD: AutoMasked Attention for Unsupervised Multivariate Time Series Anomaly Detection"
- [doi-10.24963_ijcai.2026_276](../../papers/doi-10.24963_ijcai.2026_276.yaml) Chen et al., "AnoMamba: Aligning Reconstruction with Time Series Anomaly Detection via Selective Global Dependency Modeling"
- [doi-10.24963_ijcai.2026_332](../../papers/doi-10.24963_ijcai.2026_332.yaml) Qiu et al., "Multi-View Ensemble for Time Series Anomaly Detection via Coupling Flows"
- [arxiv-1602.04938](../../papers/arxiv-1602.04938.yaml) Ribeiro et al., ""Why Should I Trust You?": Explaining the Predictions of Any Classifier"
- [arxiv-1806.10758](../../papers/arxiv-1806.10758.yaml) Hooker et al., "A Benchmark for Interpretability Methods in Deep Neural Networks"
- [arxiv-1810.03292](../../papers/arxiv-1810.03292.yaml) Adebayo et al., "Sanity Checks for Saliency Maps"
- [arxiv-1902.10186](../../papers/arxiv-1902.10186.yaml) Jain et al., "Attention is not Explanation"
- [arxiv-1905.04610](../../papers/arxiv-1905.04610.yaml) Lundberg et al., "Explainable AI for Trees: From Local Explanations to Global Understanding"
- [arxiv-1911.02508](../../papers/arxiv-1911.02508.yaml) Slack et al., "Fooling LIME and SHAP: Adversarial Attacks on Post hoc Explanation Methods"
- [arxiv-1911.05248](../../papers/arxiv-1911.05248.yaml) Hooker et al., "What Do Compressed Deep Neural Networks Forget?"
- [arxiv-2004.13912](../../papers/arxiv-2004.13912.yaml) Agarwal et al., "Neural Additive Models: Interpretable Machine Learning with Neural Nets"
- [arxiv-2006.16234](../../papers/arxiv-2006.16234.yaml) Chen et al., "True to the Model or True to the Data?"
- [arxiv-2010.03058](../../papers/arxiv-2010.03058.yaml) Hooker et al., "Characterising Bias in Compressed Models"
- [arxiv-2202.01602](../../papers/arxiv-2202.01602.yaml) Krishna et al., "The Disagreement Problem in Explainable Machine Learning: A Practitioner's Perspective"
- [arxiv-2210.17323](../../papers/arxiv-2210.17323.yaml) Frantar et al., "GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers"
- [arxiv-2310.01382](../../papers/arxiv-2310.01382.yaml) Jaiswal et al., "Compressing LLMs: The Truth is Rarely Pure and Never Simple"
- [arxiv-2403.15447](../../papers/arxiv-2403.15447.yaml) Hong et al., "Decoding Compressed Trust: Scrutinizing the Trustworthiness of Efficient LLMs Under Compression"
- [arxiv-2608.04348](../../papers/arxiv-2608.04348.yaml) Habib et al., "iStructTab: Structured Feature Sequencing for Multimodal Learning of Image and Tabular Data"
- [arxiv-2608.05265](../../papers/arxiv-2608.05265.yaml) Ledingham et al., "Evaluating Machine Learning Models for Post-Wildfire Debris-Flow Prediction"
- [arxiv-2608.08245](../../papers/arxiv-2608.08245.yaml) Levit et al., "Privacy-Preserving Data Drift Detection and Recovery for Large-Scale LLM Applications via Proxy Representations"
- [arxiv-2608.25774](../../papers/arxiv-2608.25774.yaml) Eo et al., "EXAONE Tabular 1.0 : Technical Report"
- [arxiv-2608.27882](../../papers/arxiv-2608.27882.yaml) Wang et al., "SOMTab: Set-Order Mamba for Efficient Tabular In-Context Learning"
- [arxiv-2608.28980](../../papers/arxiv-2608.28980.yaml) Rezaee et al., "The Illusion of Replacement: Rethinking Specialized Machine Learning Models in the Foundation Model Era"
- [arxiv-2608.30337](../../papers/arxiv-2608.30337.yaml) Pal et al., "Coarse composition suffices: tabular in-context learning for multi-activity antimicrobial peptide profiling"
- [arxiv-2609.02766](../../papers/arxiv-2609.02766.yaml) Tenachi et al., "Do Tabular Foundation Models Know Physics? Contamination, Units, and the Deterministic Limit"
- [arxiv-2609.03003](../../papers/arxiv-2609.03003.yaml) Stith et al., "Causal Foundation Models"
- [arxiv-2609.04388](../../papers/arxiv-2609.04388.yaml) Fernández-Barrios et al., "Candidate Comparability Before Promotion: Conditional Validation in Adaptive Network Intrusion Detection"
- [arxiv-2609.04540](../../papers/arxiv-2609.04540.yaml) Tao et al., "Mitra-v2 Technical Report"
- [arxiv-2609.06080](../../papers/arxiv-2609.06080.yaml) Sapir et al., "PhenoBench: Mapping What a Deeply Phenotyped Human Cohort Can Tell Us"
- [arxiv-2609.09432](../../papers/arxiv-2609.09432.yaml) Abu-Shaira et al., "SCCM : Stream Cruise Control Method for Automated Drift Detection and Adaptation"
- [arxiv-2609.12712](../../papers/arxiv-2609.12712.yaml) Li et al., "InRTL: Effective Intra-Inter Interaction Learning for Relational Tables"
- [arxiv-2609.13031](../../papers/arxiv-2609.13031.yaml) Kübler et al., "Attention Quantization for Tabular Foundation Models"
- [arxiv-2609.17488](../../papers/arxiv-2609.17488.yaml) Zhang et al., "LimiX-2: A Contextual Mechanism Network Towards General Structured-Data Intelligence"
- [arxiv-2609.24278](../../papers/arxiv-2609.24278.yaml) Jacob et al., "High-Dimensional Online Change Point Detection with Adaptive Thresholding and Interpretability"
- [arxiv-2609.25541](../../papers/arxiv-2609.25541.yaml) Jeon et al., "A JEPA Recipe for Tabular Foundation Models"
- [arxiv-2609.32898](../../papers/arxiv-2609.32898.yaml) Zhou et al., "When Less Compute Is More: Adaptive Early Exit Improves Pretrained Outlier Detection"
- [arxiv-2609.33940](../../papers/arxiv-2609.33940.yaml) Walker et al., "Behavioral Monitoring of JEPA World Models with Jacobian Centroids"
- [arxiv-2609.35703](../../papers/arxiv-2609.35703.yaml) Xu et al., "A Unified Uncertainty Representation for Graph Neural Networks via Doubly-Spectral Stochastic Expansion"
- [arxiv-2609.36337](../../papers/arxiv-2609.36337.yaml) Schnurr et al., "Adapting Linear-Time Architectures for Tabular In-Context Learning"
- [arxiv-1703.01365](../../papers/arxiv-1703.01365.yaml) Sundararajan et al., "Axiomatic Attribution for Deep Networks"
