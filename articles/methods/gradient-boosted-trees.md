---
title: 勾配ブースティング木 — 仕組み、実装の設計の違い、チューニングと不確実性
kind: method
tags: [gradient-boosted-trees]
depends_on: [arxiv-0804.2752, arxiv-1603.02754, arxiv-1706.09516, arxiv-1810.11363, arxiv-1910.13204, arxiv-1505.01866, arxiv-1802.05640, arxiv-1909.09223, arxiv-1910.03225, arxiv-2006.10562, arxiv-1911.01914, arxiv-1802.09596, arxiv-2106.11959, arxiv-2305.02997, arxiv-2407.04491, arxiv-2506.16791, arxiv-2207.08815, arxiv-2106.03253]
written_at: 2026-10-05
written_by: claude-opus-5-5 via Claude Code
---

# 勾配ブースティング木 — 仕組み、実装の設計の違い、チューニングと不確実性

<!-- generated:stale -->
> ⚠ この記事の執筆後(2026-10-05)に、関連カードが 36 件追加されています(未反映): `arxiv-1905.04610`, `arxiv-2207.01848`, `arxiv-2402.01502`, `arxiv-2410.24210`, `arxiv-2608.05265`, `arxiv-2608.07349`, `arxiv-2608.16429`, `arxiv-2608.17856`, `arxiv-2608.18849`, `arxiv-2608.18919`, `arxiv-2608.20024`, `arxiv-2608.22069`, `arxiv-2608.22594`, `arxiv-2608.23893`, `arxiv-2608.24056`, `arxiv-2608.27076`, `arxiv-2609.03003`, `arxiv-2609.06080`, `arxiv-2609.07441`, `arxiv-2609.13785`, `arxiv-2609.16309`, `arxiv-2609.29690`, `arxiv-2609.36039`, `arxiv-2610.00649`, `arxiv-2610.00806`, `doi-10.1007_s40123-026-01482-2`, `doi-10.1038_s41467-026-76154-7`, `doi-10.1038_s41586-024-08328-6`, `doi-10.1109_tsg.2026.3676842`, `doi-10.1186_s44147-026-01203-3`, `doi-10.3389_fpsyg.2026.1875261`, `doi-10.3389_fpubh.2026.1911565`, `doi-10.3389_frai.2026.1876396`, `doi-10.36079_lamintang.ijortas-0802.1081`, `doi-10.47852_bonviewaia620210522`, `doi-10.70393_6a6374616d.343334`
<!-- /generated:stale -->

## この記事の読み方

勾配ブースティング木(gradient-boosted decision trees, GBDT)は、決定木を1本ずつ足していき、各段で「いまのモデルの誤差」を次の木に学ばせる手法である。XGBoost・LightGBM・CatBoost がその代表的な実装である。

「GBDT と深層学習のどちらが強いか」は [表データの比較記事](../tasks/tabular-gbdt-vs-deep-learning.md) で扱っている。この記事は手法そのものに絞り、次の4点を整理する。

1. どういう仕組みで学習していて、何が正則化として効いているか
2. 実装ごとに何が違うのか(分割の探し方、欠損値、カテゴリ変数、サンプリング)
3. どのハイパーパラメータが効くのか、チューニングはどこまで必要か
4. 点予測ではなく、予測の分布や不確実性を出すには何が要るか

性能の数値は書かない。各論文のページの結果表を参照のこと(多くのカードは結果表を記録せず、主張だけを記録している)。
この記事で使う実装の論文は、**いずれもその実装の開発者自身が書いたもの**である。比較の読み方は第5節にまとめる。

## 1. 仕組み — 関数空間での勾配降下

### ブースティングを勾配降下として見る

Bühlmann と Hothorn のレビューは、Breiman を引いて、AdaBoost が関数空間での最急降下法として書けることを紹介する。これを Friedman らが一般の統計的な枠組みに広げたものが、勾配ブースティングである [arxiv-0804.2752#c1](https://arxiv.org/pdf/0804.2752v1#page=4 "showed that the AdaBoost algorithm can be represented as a steepest descent algorithm in function space which we call functional gradient descent (FGD).")。
一般形は、各段で「現在の予測での損失の負の勾配」に基底の学習器(ここでは木)を当てはめ、それを小さい係数 ν を掛けて足す、というものである。主なチューニングパラメータは**何段で止めるか(反復回数)**で、交差検証か情報量規準で決める [arxiv-0804.2752#c2](https://arxiv.org/pdf/0804.2752v1#page=4 "The stopping iteration, which is the main tuning parameter, can be determined via cross-validation or some information criterion; see Section 5.4.")。

### 正則化として効いているもの

- **縮小(学習率)**: ν は小さければ(たとえば 0.1)細かい値はあまり重要でない、とされる。小さくすると反復が増えて計算時間がかかるが、予測精度は良くなりうるし、悪くなることはほとんどない(Friedman を引いた記述) [arxiv-0804.2752#c3](https://arxiv.org/pdf/0804.2752v1#page=4 "The choice of the step-length factor ν in step 4 is of minor importance, as long as it is “small,” such as ν = 0.1.")。
- **早期終了**: AdaBoost は過学習しにくいかが議論されたが、結局はどのブースティングも反復を続ければ過学習するので、早期終了が必要である [arxiv-0804.2752#c4](https://arxiv.org/pdf/0804.2752v1#page=3 "It is clear nowadays that Ada-Boost and also other boosting algorithms are overﬁtting eventually, and early stopping")。線形の基底学習器を使った L2 ブースティングでは、反復を続けると学習データを補間する解に収束することが示される [arxiv-0804.2752#c7](https://arxiv.org/pdf/0804.2752v1#page=13 "Thus, we see here explicitly that we have to stop early with the boosting iterations in order to prevent overﬁtting.")。
- **低分散の原則**: 基底の学習器は、バイアスが大きくなっても分散の小さいものを選ぶのがよい。小さい ν はその一つの形である [arxiv-0804.2752#c6](https://arxiv.org/pdf/0804.2752v1#page=13 "Note that a small step-size factor can be seen as a shrinkage of the base procedure by the factor ν, implying low variance but potentially large estimation bias.")。
- **木の深さは交互作用の次数を決める**: 切り株(深さ1)なら加法モデルになり、葉が d 個までの木なら交互作用は d−2 次までになる [arxiv-0804.2752#c5](https://arxiv.org/pdf/0804.2752v1#page=12 "Similarly, boosting trees with (at most) d terminal nodes result in a nonparametric model having at most interactions of order d −2.")。
- **目的関数への罰則(XGBoost)**: XGBoost は、葉の数と葉の重みの L2 ノルムに罰則をかける。罰則をゼロにすると従来の勾配ブースティングに戻る [arxiv-1603.02754#c2](https://arxiv.org/pdf/1603.02754v3#page=2 "When the regularization parameter is set to zero, the objective falls back to the traditional gradient tree boosting.")。木は損失の2次近似(勾配とヘッセ行列)で当てはめる(Friedman らを引いた記述) [arxiv-1603.02754#c3](https://arxiv.org/pdf/1603.02754v3#page=2 "Second-order approximation can be used to quickly optimize the objective in the general setting [12].")。
- **列のサブサンプリング**: XGBoost の著者は、ユーザーからの声として、列(特徴量)のサブサンプリングは行のサブサンプリングより過学習を防ぐと述べている [arxiv-1603.02754#c4](https://arxiv.org/pdf/1603.02754v3#page=3 "According to user feedback, using column sub-sampling prevents over-ﬁtting even more so than the traditional row sub-sampling (which is also supported).")。ただし、根拠は「ユーザーからの声」である。

## 2. 実装の設計の違い

### 分割の探し方と欠損値(XGBoost)

- 全分割を調べる厳密な貪欲法に加え、特徴量の分位点から候補を作る近似法がある。候補を木ごとに1回作る(global)か、分割のたびに作り直す(local)かを選べる [arxiv-1603.02754#c5](https://arxiv.org/pdf/1603.02754v3#page=4 "The global proposal can be as accurate as the local one given enough candidates.")。
- 欠損値には、ノードごとに「欠損ならどちらに進むか」の既定の方向をデータから学ぶ。欠損でない要素だけを走査するので、疎なデータで速い [arxiv-1603.02754#c6](https://arxiv.org/pdf/1603.02754v3#page=5 "We ﬁnd that the sparsity aware algorithm runs 50 times faster than the naive version.")。

### カテゴリ変数と「予測のずれ」(CatBoost)

CatBoost の論文は、既存の勾配ブースティングの実装すべてに、目的変数の漏洩の一種による**予測のずれ(prediction shift)**があると主張する [arxiv-1706.09516#c1](https://arxiv.org/pdf/1706.09516v5#page=1 "Both techniques were created to ﬁght a prediction shift caused by a special kind of target leakage present in all currently existing implementations of gradient boosting algorithms.")。

- **原因**: 各段の勾配を、そのモデルを作ったのと同じデータ点で推定しているため、推定された勾配の分布がずれて過学習につながる [arxiv-1810.11363#c3](https://arxiv.org/pdf/1810.11363v1#page=3 "Gradients used at each step are estimated using the same data points the current model was built on.")。カテゴリ変数を目的変数の平均で数値化する(target statistics)ときにも、同じ種類の漏洩が起きる。
- **対策**: データをランダムに並べ、各例の統計量をそれより前の例だけから計算する(ordered target statistics) [arxiv-1706.09516#c2](https://arxiv.org/pdf/1706.09516v5#page=4 "Note that, if we use only one random permutation, then preceding examples have TS with much higher variance than subsequent ones.")。ブースティング自体も同じ考え方で行う(ordered boosting)。
- **理論の範囲**: ずれが生じることの定理は、2値特徴量2つ・線形の目的変数・切り株2本という単純化した設定でだけ証明されている [arxiv-1706.09516#c3](https://arxiv.org/pdf/1706.09516v5#page=4 "We formally analyze the problem of prediction shift in a simple case of a regression task with the quadratic loss function")。
- **代償**: 理想的な ordered boosting は計算量とメモリが n 倍になり実用にならないので、近似した方式を実装している [arxiv-1706.09516#c4](https://arxiv.org/pdf/1706.09516v5#page=5 "Unfortunately, this algorithm is not feasible in most practical tasks due to the need of training n different models, what increase the complexity and memory requirements by n times.")。偏りを抑える方式は木の構造を決めるときだけに使い、葉の値は従来の方式で決める [arxiv-1810.11363#c4](https://arxiv.org/pdf/1810.11363v1#page=3 "CatBoost implementation uses the following relaxation of this idea: all Mi share the same tree structures.")。偏りを抑える方式は従来の方式より遅い [arxiv-1706.09516#c9](https://arxiv.org/pdf/1706.09516v5#page=8 "To summarize, we obtained that CatBoost Plain and LightGBM are the fastest ones followed by Ordered mode, which is about 1.7 times slower.") [arxiv-1810.11363#c8](https://arxiv.org/pdf/1810.11363v1#page=6 "This scheme is by design 2-3 times slower then classical boosting approach.")。
- **効く場面**: ordered モードの利点が大きかったのは比較的小さいデータセットで、これは定理の偏りがデータが小さいほど大きいことと整合する、と著者らは述べる。ただし、偏りは他のデータの性質にもよりうると付け加えている [arxiv-1706.09516#c8](https://arxiv.org/pdf/1706.09516v5#page=8 "It can be clearly seen that Ordered mode is particularly useful on small datasets.")。
- **組み合わせ特徴量**: カテゴリ変数の組み合わせは指数的に増えるので、木の中ですでに使われたカテゴリ変数との組み合わせだけを貪欲に考える [arxiv-1810.11363#c2](https://arxiv.org/pdf/1810.11363v1#page=2 "When constructing a new split for the current tree, CatBoost considers combinations in a greedy way.")。one-hot 符号化は学習の途中で行う [arxiv-1810.11363#c1](https://arxiv.org/pdf/1810.11363v1#page=2 "One-hot encoding can be done during the preprocessing phase or during training, the latter can be implemented more efﬁciently in terms of training time and is implemented in CatBoost.")。

ベンチマーク論文でも、カテゴリ変数の扱いは実装ごとに違う設定で比較されている。たとえば、XGBoost には one-hot 符号化、CatBoost には組み込みのカテゴリ処理を使った例がある [arxiv-2106.11959#c14](https://arxiv.org/pdf/2106.11959v5#page=6 "For XGBoost, we use one-hot encoding.")。

### 行のサンプリング(MVS)

確率的勾配ブースティングでは、各段で一部の行だけを使う。MVS は、分割の良さの推定精度が最大になるようにサンプリング確率を決める問題として定式化した [arxiv-1910.13204#c1](https://arxiv.org/pdf/1910.13204v1#page=1 "In this paper, we formulate the problem of randomization in SGB in terms of optimization of sampling probabilities to maximize the estimation accuracy of split scoring used to train decision trees.")。ただし、導出は「木のそれまでの分割が、サンプルと全データで同じ」という仮定のもとでの上界の最小化である [arxiv-1910.13204#c2](https://arxiv.org/pdf/1910.13204v1#page=5 "under the assumption that previous splits of the tree are ﬁxed and the same for subsampled and full data.")。

- 正則化の項を0にすると重点サンプリングになるが、各ノードの事例数を正確に推定する必要があり、勾配がほぼ0の例で数値的に不安定になる [arxiv-1910.13204#c3](https://arxiv.org/pdf/1910.13204v1#page=6 "It is easy to derive that setting λ to 0 implies the procedure of Importance Sampling.")。
- GOSS と MVS は、サンプリング率のほかにハイパーパラメータが1つ増えるので、チューニングに時間がかかるかもしれない [arxiv-1910.13204#c8](https://arxiv.org/pdf/1910.13204v1#page=9 "So tuning GOSS and MVS may potentially take more time than SGB.")。

### 基底の学習器とアンサンブルの変形

- **DART**: 後から足した木がごく一部の例にしか効かなくなる「過剰な特化」を問題にする [arxiv-1505.01866#c1](https://arxiv.org/pdf/1505.01866v1#page=1 "However, it suﬀers an issue which we call over-specialization, wherein trees added at later iterations tend to impact the prediction of only a few instances, and make negligible contribution towards the remaining instances.")。縮小はこれを部分的にしか解決せず、木が増えると問題が再び現れる [arxiv-1505.01866#c2](https://arxiv.org/pdf/1505.01866v1#page=2 "As we will see in Section 2, shrinkage does help in reducing the impact of the ﬁrst trees, nevertheless, however, as the size of the ensemble increases, the problem of over-specialization reappears.")。そこで、既存の木の一部を落としてから次の木を学習する [arxiv-1505.01866#c4](https://arxiv.org/pdf/1505.01866v1#page=5 "First, when computing the gradient that the next tree will ﬁt, only a random subset of the existing ensemble is considered.")。落とす木の数で正則化の強さが決まり、1本も落とさなければ通常の勾配ブースティング(MART)になる [arxiv-1505.01866#c5](https://arxiv.org/pdf/1505.01866v1#page=5 "On the other extreme, if all the trees are dropped, the DART is no diﬀerent than random forest.")。
- **区分線形の木(GBDT-PL)**: 葉ごとの定数の代わりに、葉ごとの線形モデルを基底にする [arxiv-1802.05640#c1](https://arxiv.org/pdf/1802.05640v3#page=1 "Speciﬁcally, we extend gradient boosting to use piecewise linear regression trees (PL Trees), instead of piecewise constant regression trees, as base learners.")。分割は、両側の子に線形モデルを当てはめたときの損失の減少で選ぶ [arxiv-1802.05640#c3](https://arxiv.org/pdf/1802.05640v3#page=5 "By contrast, PL Tree used in our work is designed to greedily reduce the loss at each step of its growing.")。高速化のために線形モデルを制限すると、精度が少し犠牲になる [arxiv-1802.05640#c4](https://arxiv.org/pdf/1802.05640v3#page=5 "Incremental feature selection restricts the size of linear models, and half-additive ﬁtting results in suboptimal linear model parameters.")。現状では数値特徴量しか扱えない [arxiv-1802.05640#c8](https://arxiv.org/pdf/1802.05640v3#page=5 "Currently GBDT-PL only handles numerical features.")。
- **EBM(説明可能なブースティング)**: 特徴量を1つずつ順番に、非常に小さい学習率でブースティングして、加法モデル(GAM)を作る [arxiv-1909.09223#c2](https://arxiv.org/pdf/1909.09223v1#page=3 "The boosting procedure is carefully restricted to train on one feature at a time in round-robin fashion using a very low learning rate so that feature order does not matter.")。2次の交互作用も自動で入れる [arxiv-1909.09223#c3](https://arxiv.org/pdf/1909.09223v1#page=3 "EBM is a fast implementation of the GA2M algorithm (Lou et al., 2013), written in C++ and Python.")。加法的なので、各特徴量の寄与をそのまま図にできる [arxiv-1909.09223#c4](https://arxiv.org/pdf/1909.09223v1#page=3 "Because EBM is an additive model, each feature contributes to predictions in a modular way that makes it easy to reason about the contribution of each feature to the prediction.")。代償として学習は遅い [arxiv-1909.09223#c7](https://arxiv.org/pdf/1909.09223v1#page=4 "To keep the individual terms additive, EBM pays an additional training cost, making it somewhat slower than similar methods.")。

## 3. チューニング — 何が効き、どこまで必要か

### どのハイパーパラメータが効くか

Probst らは、「既定値での性能」と「そのデータセットで最良の設定での性能」の差を**チューニングの効き目(tunability)**と定義した [arxiv-1802.09596#c1](https://arxiv.org/pdf/1802.09596v3#page=4 "A general measure of the tunability of an algorithm per dataset can then be computed based on the diﬀerence between the risk of an overall reference conﬁguration (e.g., either the software defaults or deﬁnition (3)) and the risk of the best possible conﬁguration on that dataset:")。OpenML の2値分類38件で、6つのアルゴリズムを比べている [arxiv-1802.09596#c2](https://arxiv.org/pdf/1802.09596v3#page=5 "For our study we only use the 38 binary classiﬁcation tasks that do not contain any missing values.")。

- xgboost では、学習率(eta)と、基底を木にするか線形にするか(booster)の効き目が大きかった [arxiv-1802.09596#c6](https://arxiv.org/pdf/1802.09596v3#page=10 "For xgboost there are two parameters that are quite tunable: eta and the booster.")。
- 一方、XGBoost の比較分析では、ランダム化に関わるパラメータ(行のサンプリング率、分割ごとの特徴量数)は、妥当な値を使えばチューニング不要に見える、としている [arxiv-1911.01914#c8](https://arxiv.org/pdf/1911.01914v1#page=15 "A conclusion that may be clearer is that it seems unnecessary to tune the number of random features and the subsampling rate provided that those techniques are applied with reasonable values (in our case subsampling to 0.75 and feature sampling to sqrt).")。

### 既定値で十分か

- Bentéjac らは、28件のデータで、ランダムフォレストは既定値が調整後に最も近く、XGBoost と scikit-learn の勾配ブースティングは既定値だと調整後より概して劣る(常にではない)と報告している [arxiv-1911.01914#c4](https://arxiv.org/pdf/1911.01914v1#page=9 "Default random forest is the method that performs more evenly with respect to its tuned counterpart.")。結論は「勾配ブースティングでは丁寧な探索が必要」である [arxiv-1911.01914#c7](https://arxiv.org/pdf/1911.01914v1#page=17 "In consequence, we conclude that a meticulous parameter search is necessary to create accurate models based on gradient boosting.")。
- 一方で、ノイズの多いデータでは、学習データ内の交差検証で選んでも過学習しうるため、既定値の方が良いこともあった [arxiv-1911.01914#c5](https://arxiv.org/pdf/1911.01914v1#page=9 "The parameter esti- mation process, even though it is performed within train cross-validation, may overﬁt the training set specially in noisy datasets.")。
- 表データの比較研究では、GBDT の軽いチューニングの方が、GBDT と深層学習のどちらを選ぶかより効くことが多い、という報告がある [arxiv-2305.02997#c2](https://arxiv.org/pdf/2305.02997v4#page=1 "light hyperparameter tuning on a GBDT is more important than choosing between NNs and GBDTs")。
- 既定値そのものを多数のデータで調整し直す試みもある。調整した既定値はライブラリの既定値より明らかに良かったが、GBDT については、調整に使ったデータでは HPO に並んだものの、別のデータ(メタテスト)では並ばなかった [arxiv-2407.04491#c8](https://arxiv.org/pdf/2407.04491v3#page=9 "For GBDTs, tuned defaults are competitive with HPO on the meta-train set, but not as good on the meta-test set.")。GBDT の中では、CatBoost の既定値は良いが遅い [arxiv-2407.04491#c17](https://arxiv.org/pdf/2407.04491v3#page=9 "Among GBDTs, CatBoost defaults are better and slower.")。

### チューニングの比較を読むときの注意

- **探索の規模がアルゴリズムごとに違う**: Bentéjac らのグリッドは、アルゴリズムごとに設定の数が大きく違い、チューニング時間は直接比べられない [arxiv-1911.01914#c3](https://arxiv.org/pdf/1911.01914v1#page=11 "Since the size of the grid is diﬀerent for diﬀerent classiﬁers (i.e. 3840, 256 and 1920 for XGB, RF and GB respectively), the time dedicated to ﬁnding the best parameters is not directly comparable between classiﬁers.")。
- **新しい既定値を、評価と同じデータで決めている**: Probst らはこの点を自ら認め、データセットをまたいだ交差検証でも評価している [arxiv-1802.09596#c4](https://arxiv.org/pdf/1802.09596v3#page=7 "Of course one has to be careful with overﬁtting here, as our new defaults are chosen with the help of the same datasets that are used to determine the performance.")。
- **固定した設定で比べている**: 大規模ベンチマークでも、ハイパーパラメータの候補を固定した集合で比べていて、HPO の手法やばらつきは調べていない、と限界に書かれている [arxiv-2506.16791#c18](https://arxiv.org/pdf/2506.16791v4#page=10 "We use a fixed set of 200 random hyperparameter configurations to enable the study of ensemble pipelines.")。

## 4. 予測の分布と不確実性

GBDT は普通、1つの値(点予測)を出す。

- **NGBoost**: 二乗誤差の GBDT の出力は「分散が一定のガウス分布の平均」と読めるが、それでは不確実性としてほとんど役に立たない、と著者らは述べる [arxiv-1910.03225#c1](https://arxiv.org/pdf/1910.03225v4#page=2 "However, such probabilistic interpretations have little use if the variance is assumed constant.")。そこで、分布のパラメータ(平均と分散など)を同時にブースティングする。パラメータの取り方によって学習が大きく変わるので、自然勾配を使う [arxiv-1910.03225#c2](https://arxiv.org/pdf/1910.03225v4#page=3 "Thus the choice of parameterization can drastically impact the training dynamics, even though the minima are unchanged.")。普通の勾配だと、初期の平均にたまたま近い例が学習を支配し、過学習と学習不足が同時に起きる [arxiv-1910.03225#c3](https://arxiv.org/pdf/1910.03225v4#page=6 "With ordinary gradients, we observe that “lucky” examples that are accidentally close to the initial predicted mean dominate the learning.")。アブレーションでも、普通の勾配で複数のパラメータをブースティングすると、分散一定と仮定するより悪いことが多かった [arxiv-1910.03225#c7](https://arxiv.org/pdf/1910.03225v4#page=9 "However, us- ing multiparameter boosting to relax the homoscedasticity assumption most often results in worse performance, likely due to poor training dynamics.")。代償として、計算量は分布のパラメータの数に比例して増える [arxiv-1910.03225#c4](https://arxiv.org/pdf/1910.03225v4#page=6 "The relative increase in computational cost is thus linear in the number of distributional parameters (p).")。
- **知識の不確実性**: Malinin らは、NGBoost のような方式はデータのノイズによる不確実性しか捉えず、学習データから遠い入力についての「知識の不確実性」を捉えないと指摘する [arxiv-2006.10562#c1](https://arxiv.org/pdf/2006.10562v4#page=2 "However, such models only capture data uncertainty (Gal, 2016; Malinin, 2019), also known as aleatoric uncertainty, which arises due to inherent class overlap or noise in the data.")。独立に学習した GBDT のアンサンブルを使うが、通常の確率的ブースティングのアンサンブルには事後分布を近似する保証がない。そのため、事後分布から漸近的にサンプルする SGLB を使う [arxiv-2006.10562#c2](https://arxiv.org/pdf/2006.10562v4#page=4 "Unfortunately, there are no guarantees on how well the distribution q(θ) estimates the true posterior p(θ/D).")。1本のモデルから作る安価な「仮想アンサンブル」は、独立なモデルのアンサンブルより劣る [arxiv-2006.10562#c3](https://arxiv.org/pdf/2006.10562v4#page=7 "This shows that while vSGLB yields very cheap estimates of knowledge uncertainty by exploiting the ‘ensemble of trees’ structure of GBDT models, the quality of these estimates is inferior to ensembles of independent models.")。
  - 知識の不確実性は分布外の検出には役立ったが、その分布外データは別のデータセットから作った合成である [arxiv-2006.10562#c6](https://arxiv.org/pdf/2006.10562v4#page=8 "However, obtaining ‘real’ OOD examples for the datasets considered in this work is challenging, so we instead create synthetic OOD data as follows.")。
  - 誤りの検出では、アンサンブルは単一モデルを上回らなかった [arxiv-2006.10562#c5](https://arxiv.org/pdf/2006.10562v4#page=8 "However, ensembles do not outperform single models.")。

## 5. 実装の論文の比較を読むときの注意

実装の論文は、いずれも開発者自身が自分の実装を評価している。比較の条件を見ると、次のような偏りや限定がある。

| 論文 | 比較の条件で注意する点 |
|---|---|
| XGBoost | 全実験で共通の設定(深さ・縮小)を使い、ライブラリごとのチューニング手順は本文に見当たらない。比較は主に速度 [arxiv-1603.02754#c7](https://arxiv.org/pdf/1603.02754v3#page=8 "In all the experiments, we boost trees with a common setting of maximum depth equals 8, shrinkage equals 0.1 and no column subsampling unless explicitly speciﬁed.") [arxiv-1603.02754#c8](https://arxiv.org/pdf/1603.02754v3#page=8 "Both XGBoost and scikit-learn give better performance than R’s GBM, while XGBoost runs more than 10x faster than scikit-learn.") |
| CatBoost(ordered boosting) | XGBoost と LightGBM にも、CatBoost 自身の方式で数値化したカテゴリ変数を渡している [arxiv-1706.09516#c6](https://arxiv.org/pdf/1706.09516v5#page=8 "For all learning algorithms, we preprocess categorical features using the ordered TS method described in Section 3.2.")。チューニングは各ライブラリ同じ回数の TPE だが、1つのデータセットでは既定値だけ [arxiv-1706.09516#c5](https://arxiv.org/pdf/1706.09516v5#page=19 "We tune all the key parameters of each algorithm by 50 steps of the sequential optimization algorithm Tree Parzen Estimator implemented in Hyperopt library21 (mode algo=tpe.suggest) by minimizing logloss.") |
| CatBoost(カテゴリ変数) | チューニングの詳細は論文になく、リポジトリを参照としている [arxiv-1810.11363#c5](https://arxiv.org/pdf/1810.11363v1#page=5 "The parameter tunning and training was performed on 4/5 of the data and the testing was performed on the other 1/5.")。既定値の CatBoost と調整済みのベースラインの比較も、論文には載っていない [arxiv-1810.11363#c6](https://arxiv.org/pdf/1810.11363v1#page=5 "In our repo on github you can also see that CatBoost with default parameters outperforms tunned XGBoost and H2O on all datasets and LightGBM on all but one datasets.")。著者自身、速度の比較は難しいとして固定サイズの学習時間だけ比べている [arxiv-1810.11363#c7](https://arxiv.org/pdf/1810.11363v1#page=6 "As a result, we can’t compare libraries by time we need to obtain certain level of quality.") |
| MVS | ベースラインのパラメータは CatBoost のベンチマークのものを使い、サンプリングのパラメータだけを調整している [arxiv-1910.13204#c7](https://arxiv.org/pdf/1910.13204v1#page=8 "We used the tuned parameters and train-test splitting for each dataset from [5] as baselines, presetting the sampling ratio to 1.") |
| GBDT-PL | ベースラインはテストデータ上で最良の反復を記録し、提案手法は検証データで選んでいる(本文に明記) [arxiv-1802.05640#c5](https://arxiv.org/pdf/1802.05640v3#page=5 "For XGBoost, LightGBM and CatBoost, result of the best iteration over all settings on test set is recorded.") |
| NGBoost | 深層学習のベースラインの値は元論文からの転記 [arxiv-1910.03225#c6](https://arxiv.org/pdf/1910.03225v4#page=7 "We use the results from Gal and Ghahramani (2016) as our benchmark.")。点予測の比較では、NGBoost は対数尤度向けに最適化され、比較対象ほど調整されていない、と著者自身が注記 [arxiv-1910.03225#c8](https://arxiv.org/pdf/1910.03225v4#page=9 "This is despite the fact that the NGBoost mod- els were (a) optimized for NLL, not to minimize RMSE and (b) less aggressively tuned.") |
| EBM | すべてのモデルを既定値で比較し、EBM の既定値は計算速度のために選んだもの [arxiv-1909.09223#c6](https://arxiv.org/pdf/1909.09223v1#page=4 "All models were trained with their default parameters.") |
| DART | 回帰では、交差検証の各分割で最良のパラメータの値を報告していて、別の検証データは本文に見当たらない [arxiv-1505.01866#c7](https://arxiv.org/pdf/1505.01866v1#page=7 "The folds were selected such that either all the images of an individual are in the train set or all of them are in the test set.") |

第三者による大規模比較の位置づけは、[表データの比較記事](../tasks/tabular-gbdt-vs-deep-learning.md) にまとめている。たとえば、TabArena の通常のチューニングの設定では CatBoost が首位だった [arxiv-2506.16791#c11](https://arxiv.org/pdf/2506.16791v4#page=7 "In line with previous work [33], CatBoost is ranked first in the conventional tuning regime (Figure 1).")。

## 設計への示唆(本記事の整理)

論文の主張そのものではなく、本記事のまとめである。

1. **反復回数(早期終了)と学習率を最初に決める**: 主なチューニングパラメータは反復回数であり [arxiv-0804.2752#c2](https://arxiv.org/pdf/0804.2752v1#page=4 "The stopping iteration, which is the main tuning parameter, can be determined via cross-validation or some information criterion; see Section 5.4.")、学習率の効き目も大きい [arxiv-1802.09596#c6](https://arxiv.org/pdf/1802.09596v3#page=10 "For xgboost there are two parameters that are quite tunable: eta and the booster.")。
2. **既定値をそのまま信用しない。ただし大規模な探索の前に、軽い調整で十分か確かめる**: 既定値では劣ることが多い一方 [arxiv-1911.01914#c4](https://arxiv.org/pdf/1911.01914v1#page=9 "Default random forest is the method that performs more evenly with respect to its tuned counterpart.")、軽い調整で大きく改善する場合が多い [arxiv-2305.02997#c2](https://arxiv.org/pdf/2305.02997v4#page=1 "light hyperparameter tuning on a GBDT is more important than choosing between NNs and GBDTs")。
3. **カテゴリ変数の扱いを、比較の条件として明記する**: 実装ごとに扱いが違い、比較の結果を左右しうる [arxiv-1706.09516#c6](https://arxiv.org/pdf/1706.09516v5#page=8 "For all learning algorithms, we preprocess categorical features using the ordered TS method described in Section 3.2.") [arxiv-2106.11959#c14](https://arxiv.org/pdf/2106.11959v5#page=6 "For XGBoost, we use one-hot encoding.")。
4. **不確実性が要るなら、ノイズと知識の不確実性を区別する**: 分布を出す GBDT はノイズしか捉えない [arxiv-2006.10562#c1](https://arxiv.org/pdf/2006.10562v4#page=2 "However, such models only capture data uncertainty (Gal, 2016; Malinin, 2019), also known as aleatoric uncertainty, which arises due to inherent class overlap or noise in the data.")。

## わかっていないこと

- **予測のずれの大きさ**: 理論は単純化した設定だけで示され [arxiv-1706.09516#c3](https://arxiv.org/pdf/1706.09516v5#page=4 "We formally analyze the problem of prediction shift in a simple case of a regression task with the quadratic loss function")、実データでどの程度効くかはデータの性質にもよる [arxiv-1706.09516#c8](https://arxiv.org/pdf/1706.09516v5#page=8 "It can be clearly seen that Ordered mode is particularly useful on small datasets.")。第三者が CatBoost の ordered モードとそれ以外を同じ条件で比べた研究は、この範囲にない。
- **列のサブサンプリングの効果**: XGBoost の主張の根拠はユーザーの声で [arxiv-1603.02754#c4](https://arxiv.org/pdf/1603.02754v3#page=3 "According to user feedback, using column sub-sampling prevents over-ﬁtting even more so than the traditional row sub-sampling (which is also supported).")、別の比較ではチューニング不要とされている [arxiv-1911.01914#c8](https://arxiv.org/pdf/1911.01914v1#page=15 "A conclusion that may be clearer is that it seems unnecessary to tune the number of random features and the subsampling rate provided that those techniques are applied with reasonable values (in our case subsampling to 0.75 and feature sampling to sqrt).")。系統的に検証した研究はこの範囲にない。
- **LightGBM**: LightGBM の論文は arXiv にも DOI 付きの公開版にもなく、カード化していない。GOSS(勾配に基づくサンプリング)については、MVS の論文の比較を通してだけ触れている [arxiv-1910.13204#c7](https://arxiv.org/pdf/1910.13204v1#page=8 "We used the tuned parameters and train-test splitting for each dataset from [5] as baselines, presetting the sampling ratio to 1.")。

## 現時点での整理

- **GBDT は関数空間での勾配降下で、反復回数と学習率が中心的な正則化である** [arxiv-0804.2752#c1](https://arxiv.org/pdf/0804.2752v1#page=4 "showed that the AdaBoost algorithm can be represented as a steepest descent algorithm in function space which we call functional gradient descent (FGD).") [arxiv-0804.2752#c2](https://arxiv.org/pdf/0804.2752v1#page=4 "The stopping iteration, which is the main tuning parameter, can be determined via cross-validation or some information criterion; see Section 5.4.") [arxiv-0804.2752#c3](https://arxiv.org/pdf/0804.2752v1#page=4 "The choice of the step-length factor ν in step 4 is of minor importance, as long as it is “small,” such as ν = 0.1.")。
- **実装の違いは、分割の探し方・欠損値・カテゴリ変数・サンプリングにある** [arxiv-1603.02754#c5](https://arxiv.org/pdf/1603.02754v3#page=4 "The global proposal can be as accurate as the local one given enough candidates.") [arxiv-1603.02754#c6](https://arxiv.org/pdf/1603.02754v3#page=5 "We ﬁnd that the sparsity aware algorithm runs 50 times faster than the naive version.") [arxiv-1706.09516#c2](https://arxiv.org/pdf/1706.09516v5#page=4 "Note that, if we use only one random permutation, then preceding examples have TS with much higher variance than subsequent ones.") [arxiv-1910.13204#c1](https://arxiv.org/pdf/1910.13204v1#page=1 "In this paper, we formulate the problem of randomization in SGB in terms of optimization of sampling probabilities to maximize the estimation accuracy of split scoring used to train decision trees.")。
- **実装の論文の比較は開発者自身によるもので、条件に偏りがある** [arxiv-1706.09516#c6](https://arxiv.org/pdf/1706.09516v5#page=8 "For all learning algorithms, we preprocess categorical features using the ordered TS method described in Section 3.2.") [arxiv-1802.05640#c5](https://arxiv.org/pdf/1802.05640v3#page=5 "For XGBoost, LightGBM and CatBoost, result of the best iteration over all settings on test set is recorded.")。
- **既定値は劣ることが多いが、どのパラメータが効くかの報告は一致しない部分がある** [arxiv-1911.01914#c4](https://arxiv.org/pdf/1911.01914v1#page=9 "Default random forest is the method that performs more evenly with respect to its tuned counterpart.") [arxiv-1802.09596#c6](https://arxiv.org/pdf/1802.09596v3#page=10 "For xgboost there are two parameters that are quite tunable: eta and the booster.") [arxiv-1911.01914#c8](https://arxiv.org/pdf/1911.01914v1#page=15 "A conclusion that may be clearer is that it seems unnecessary to tune the number of random features and the subsampling rate provided that those techniques are applied with reasonable values (in our case subsampling to 0.75 and feature sampling to sqrt).")。
- **予測分布を出すには工夫が要り、知識の不確実性にはアンサンブルが要る** [arxiv-1910.03225#c2](https://arxiv.org/pdf/1910.03225v4#page=3 "Thus the choice of parameterization can drastically impact the training dynamics, even though the minima are unchanged.") [arxiv-2006.10562#c1](https://arxiv.org/pdf/2006.10562v4#page=2 "However, such models only capture data uncertainty (Gal, 2016; Malinin, 2019), also known as aleatoric uncertainty, which arises due to inherent class overlap or noise in the data.") [arxiv-2006.10562#c2](https://arxiv.org/pdf/2006.10562v4#page=4 "Unfortunately, there are no guarantees on how well the distribution q(θ) estimates the true posterior p(θ/D).")。

**この整理に含まれていないもの**: LightGBM の原論文(上記)、Friedman(2001, 2002)の原論文(arXiv になく、統計学のレビューを通してだけ触れている)、ランキング学習としての LambdaMART、GPU 実装、分散学習。ランダムフォレストは [別の記事](random-forests-and-decision-trees.md) で扱う。

## 参照カード

- [arxiv-0804.2752](../../papers/arxiv-0804.2752.yaml) Bühlmann & Hothorn, "Boosting Algorithms: Regularization, Prediction and Model Fitting"
- [arxiv-1603.02754](../../papers/arxiv-1603.02754.yaml) Chen & Guestrin, "XGBoost: A Scalable Tree Boosting System"
- [arxiv-1706.09516](../../papers/arxiv-1706.09516.yaml) Prokhorenkova et al., "CatBoost: unbiased boosting with categorical features"
- [arxiv-1810.11363](../../papers/arxiv-1810.11363.yaml) Dorogush, Ershov & Gulin, "CatBoost: gradient boosting with categorical features support"
- [arxiv-1910.13204](../../papers/arxiv-1910.13204.yaml) Ibragimov & Gusev, "Minimal Variance Sampling in Stochastic Gradient Boosting"
- [arxiv-1505.01866](../../papers/arxiv-1505.01866.yaml) Rashmi & Gilad-Bachrach, "DART: Dropouts meet Multiple Additive Regression Trees"
- [arxiv-1802.05640](../../papers/arxiv-1802.05640.yaml) Shi, Li & Li, "Gradient Boosting With Piece-Wise Linear Regression Trees"
- [arxiv-1909.09223](../../papers/arxiv-1909.09223.yaml) Nori et al., "InterpretML: A Unified Framework for Machine Learning Interpretability"
- [arxiv-1910.03225](../../papers/arxiv-1910.03225.yaml) Duan et al., "NGBoost: Natural Gradient Boosting for Probabilistic Prediction"
- [arxiv-2006.10562](../../papers/arxiv-2006.10562.yaml) Malinin, Prokhorenkova & Ustimenko, "Uncertainty in Gradient Boosting via Ensembles"
- [arxiv-1911.01914](../../papers/arxiv-1911.01914.yaml) Bentéjac et al., "A Comparative Analysis of XGBoost"
- [arxiv-1802.09596](../../papers/arxiv-1802.09596.yaml) Probst, Bischl & Boulesteix, "Tunability: Importance of Hyperparameters of Machine Learning Algorithms"
- [arxiv-2106.11959](../../papers/arxiv-2106.11959.yaml) Gorishniy et al., "Revisiting Deep Learning Models for Tabular Data"
- [arxiv-2305.02997](../../papers/arxiv-2305.02997.yaml) McElfresh et al., "When Do Neural Nets Outperform Boosted Trees on Tabular Data?"
- [arxiv-2407.04491](../../papers/arxiv-2407.04491.yaml) Holzmüller et al., "Better by Default: Strong Pre-Tuned MLPs and Boosted Trees on Tabular Data"
- [arxiv-2506.16791](../../papers/arxiv-2506.16791.yaml) Erickson et al., "TabArena: A Living Benchmark for Machine Learning on Tabular Data"
- [arxiv-2207.08815](../../papers/arxiv-2207.08815.yaml) Grinsztajn et al., "Why do tree-based models still outperform deep learning on tabular data?"
- [arxiv-2106.03253](../../papers/arxiv-2106.03253.yaml) Shwartz-Ziv & Armon, "Tabular Data: Deep Learning is Not All You Need"
