---
title: 近似ベイズ推論とその診断 — MCMC と変分推論、その近似は信用できるか
kind: method
tags: [mcmc, variational-inference, posterior-inference]
depends_on: [arxiv-1111.4246, arxiv-1701.02434, arxiv-1402.4102, arxiv-1909.11827, arxiv-1601.00670, arxiv-1711.05597, arxiv-1206.7051, arxiv-1401.0118, arxiv-1603.00788, arxiv-1505.05770, arxiv-2108.03782, arxiv-1507.02646, arxiv-1802.02538, arxiv-1910.04102, arxiv-1903.08008, arxiv-1804.06788, arxiv-2211.02383, arxiv-2011.01808, arxiv-2002.02405, arxiv-2211.14097, arxiv-1312.6114]
written_at: 2026-10-10
written_by: claude-opus-5-5 via Claude Code
---

# 近似ベイズ推論とその診断 — MCMC と変分推論、その近似は信用できるか

<!-- generated:stale -->
> 未反映のカードはありません。
<!-- /generated:stale -->

## この記事の読み方

ベイズ推論では、データを見た後のパラメータの分布(事後分布)を求める。たいていのモデルでは事後分布を式で求められないので、近似する。方法は大きく2つある。

- **MCMC(マルコフ連鎖モンテカルロ法)**: 事後分布からのサンプルを、少しずつ動く連鎖で作る。時間をかければ正しい分布に近づくが、遅いことがある。
- **変分推論(VI)**: 扱いやすい分布の族の中から、事後分布に最も近いものを最適化で探す。速いが、近似の族の外にある形は表せない。

この記事は、それぞれの仕組みと弱点、そして**「その近似が正しく計算されているか」を確かめる診断**を整理する。
これまでの記事とのつながりもある。不確実性の記事で扱った cold posterior の問題は、SG-MCMC で近似した事後分布についての話だった [arxiv-2002.02405#c1](https://arxiv.org/pdf/2002.02405v2#page=2 "Cold Posteriors: among all temperized posteriors the best posterior predictive performance on holdout data is achieved at temperature T < 1.")。変化点の記事では、信用集合の被覆率が目標に届かず、著者らがそれを変分近似による不確実性の過小評価のせいだとした例があった [arxiv-2211.14097#c7](https://arxiv.org/pdf/2211.14097v3#page=20 "We can see that PRISCA’s sets do not attain the targeted p level, but they are relatively close.") [arxiv-2211.14097#c6](https://arxiv.org/pdf/2211.14097v3#page=14 "Proposition 1 and Corollary 2 establish that Algorithm 1 is a VB approximation to the posterior distribution of PRISCA, where the approximation lies in the fact that we have factorized the L effects using a mean-field approximation.")。

性能の数値は書かない。各論文のページの結果表を参照のこと(カードは結果表を記録せず、主張だけを記録している)。推奨の閾値(R-hat、k-hat など)は、判断の条件として出典付きで書く。

## 1. MCMC — ハミルトニアンモンテカルロ法

### なぜ高次元でランダムウォークは効かないのか

Betancourt の入門によれば、高次元では、最頻値の近くは密度が高いが体積が小さく、遠い裾は体積が大きいが密度が無視できる。そのため、期待値に効くのはその間の「典型集合」である [arxiv-1701.02434#c1](https://arxiv.org/pdf/1701.02434v2#page=7 "The only signiﬁcant contributions come from the neighborhood between these two extremes known as the typical set (Figure 3).")。
ランダムウォークのメトロポリス法は、高次元ではほとんどの提案が典型集合の外に出て棄却される。かといって提案を小さくすると、ほとんど動けない [arxiv-1701.02434#c2](https://arxiv.org/pdf/1701.02434v2#page=16 "Regardless of how we tune the covariance of the Random Walk Metropolis proposal or the particular details of the target distribution, the resulting Markov chain will explore the typical set extremely slowly in all but the lowest dimensional spaces.")。
勾配だけに従うと最頻値に向かってしまう。そこで、HMC は運動量を加えて典型集合の中を滑らかに動く [arxiv-1701.02434#c3](https://arxiv.org/pdf/1701.02434v2#page=19 "Following the guidance of the gradient pulls us away from the typical set and towards the mode of the target density.")。

NUTS の論文は先行研究を引いて、独立なサンプル1つあたりの計算量が、HMC ではランダムウォークより次元に対してゆっくり増えると紹介している [arxiv-1111.4246#c1](https://arxiv.org/pdf/1111.4246v1#page=2 "which stands in sharp contrast with the O(D2) cost of random-walk Metropolis (Creutz, 1988)")。

### NUTS — 調整の自動化

HMC には、軌道の長さとステップ幅という調整パラメータがある。

- **軌道の長さ**: 短すぎると HMC の利点を無駄にし、長すぎると効果が頭打ちになる。最適な長さは軌道ごとに違う [arxiv-1701.02434#c5](https://arxiv.org/pdf/1701.02434v2#page=34 "In general, this optimal integration time will vary strongly depending on which trajectory we are considering: no single integration time will perform well everywhere.")。NUTS は、軌道が引き返し始めたら止めることで、これを自動化する。素朴な「引き返したら止める」規則は時間反転性を保たないので、工夫が要る [arxiv-1111.4246#c2](https://arxiv.org/pdf/1111.4246v1#page=5 "Unfortunately this algorithm does not guarantee time reversibility, and is therefore not guaranteed to converge to the correct distribution.")。
- **ステップ幅**: 受理率の目標に合わせて自動で調整する [arxiv-1111.4246#c4](https://arxiv.org/pdf/1111.4246v1#page=15 "However, the diminishing step sizes of Robbins-Monro give disproportionate weight to the early iterations, which is the opposite of what we want.")。目標の受理率は、NUTS で 0.6 前後がよいとされる [arxiv-1111.4246#c7](https://arxiv.org/pdf/1111.4246v1#page=25 "δ = 0.6 therefore seems like a reasonable default value for NUTS.")。ただし、調整のアルゴリズム自体のパラメータは、1つのモデルで手で決めたものである [arxiv-1111.4246#c5](https://arxiv.org/pdf/1111.4246v1#page=16 "Better results might be obtained with further tweaking, but these default parameters seem to work consistently well for both NUTS and HMC for all of the models that we tested.")。
- **範囲**: NUTS が扱えるのは、制約のない連続変数だけである [arxiv-1111.4246#c9](https://arxiv.org/pdf/1111.4246v1#page=27 "Like HMC, NUTS can only be used to resample unconstrained continuous-valued variables with respect to which the target distribution is diﬀerentiable almost everywhere.")。

### HMC の失敗のしかた

- **発散(divergence)**: 曲率の高い領域(階層モデルでよく現れる)では、数値積分が不安定になる。これは警告として検出できる [arxiv-1701.02434#c7](https://arxiv.org/pdf/1701.02434v2#page=45 "In particular, any divergent transitions encountered in a Hamiltonian Markov chain should prompt suspicion of the validity of any Markov chain Monte Carlo estimators.")。NUTS も、シミュレーションの誤差が極端に大きくなったら軌道を止める [arxiv-1111.4246#c3](https://arxiv.org/pdf/1111.4246v1#page=9 "We also want to stop expanding B if the error in the simulation becomes extremely large, indicating that any states discovered by continuing the simulation longer are likely to have astronomically low probability.")。
- **見逃される領域**: 典型集合が曲率の高い領域に細く伸びていると、ほとんどの遷移がそこに入れず、推定が偏る [arxiv-1701.02434#c4](https://arxiv.org/pdf/1701.02434v2#page=15 "Consequently, when split ˆR is not near the nominal value of 1, we should be suspicious of geometric ergodicity being satisﬁed and hence the practical utility of any resulting estimators.")。
- **エネルギーの裾**: 運動エネルギーの選び方が悪いと、エネルギーの探索が不十分になる [arxiv-1701.02434#c8](https://arxiv.org/pdf/1701.02434v2#page=44 "Empirically, values of this energy Bayesian fraction of missing information below 0.3 have proven problematic")。
- **診断の限界**: こうした診断は、正しい推定のための必要条件であって十分条件ではない [arxiv-1701.02434#c9](https://arxiv.org/pdf/1701.02434v2#page=45 "Although these two diagnostics are powerful means of identifying many pathological target distributions, they are only necessary and not suﬃcient conditions for the validity of the Markov chain Monte Carlo estimators.")。

### 確率的勾配 MCMC

大規模データでは、全データで勾配を計算する代わりにミニバッチを使いたい。しかし、素朴に置き換えると、ミニバッチの勾配のノイズで目標の分布が保たれなくなる [arxiv-1402.4102#c1](https://arxiv.org/pdf/1402.4102v2#page=3 "Formally, as given by Corollary 3.1 of Theorem 3.1, when B is nonzero, π(θ, r) of Eq. (3) is no longer invariant under the dynamics described by Eq. (7).")。
SGHMC は、摩擦の項を加えてこれを補正する [arxiv-1402.4102#c3](https://arxiv.org/pdf/1402.4102v2#page=5 "The key was to introduce a friction term using second-order Langevin dynamics.")。ただし、完全に正しくなるのはステップ幅がゼロに近づく極限だけである [arxiv-1402.4102#c5](https://arxiv.org/pdf/1402.4102v2#page=6 "As in (Welling & Teh, 2011; Ahn et al., 2012) for SGLD, we consider using a small, non-zero ϵ leading to some bias.")。メトロポリス・ヘイスティングスの補正は、使えないとされる [arxiv-1402.4102#c6](https://arxiv.org/pdf/1402.4102v2#page=6 "We note that, just as in SGLD, an MH correction is not even possible because we cannot compute the probability of the reverse dynamics.")。
不確実性の記事で扱った cold posterior の研究は、こうした確率的勾配 MCMC で近似した事後分布を調べていた [arxiv-2002.02405#c1](https://arxiv.org/pdf/2002.02405v2#page=2 "Cold Posteriors: among all temperized posteriors the best posterior predictive performance on holdout data is achieved at temperature T < 1.")。

## 2. 変分推論

### 何を最適化するのか

VI は、近似分布 q と事後分布の KL ダイバージェンスを小さくしたい。しかし、それは直接計算できないので、代わりに ELBO(証拠の下界)を最大化する [arxiv-1601.00670#c1](https://arxiv.org/pdf/1601.00670v9#page=6 "Because we cannot compute the KL, we optimize an alternative objective that is equivalent to the KL up to an added constant,")。VAE もこの ELBO を最適化している [arxiv-1312.6114#c1](https://arxiv.org/pdf/1312.6114v11#page=1 "First, we show that a reparameterization of the variational lower bound yields a lower bound estimator that can be straightforwardly optimized using standard stochastic gradient methods.")。

### VI と MCMC の使い分け

Blei らのレビューは、MCMC は計算が重いが(漸近的に)正確なサンプルを保証し、VI はその保証がないが速い、とまとめる [arxiv-1601.00670#c3](https://arxiv.org/pdf/1601.00670v9#page=3 "Thus, variational inference is suited to large data sets and scenarios where we want to quickly explore many models; MCMC is suited to smaller data sets and scenarios where we happily pay a heavier computational cost for more precise samples.")。ただし、データの大きさだけでは決まらず、事後分布の形も関係する [arxiv-1601.00670#c4](https://arxiv.org/pdf/1601.00670v9#page=3 "For mixture models where Gibbs sampling is not an option, variational inference may perform better than a more general MCMC technique (e.g., Hamiltonian Monte Carlo), even for small datasets (Kucukelbir et al., 2015).")。
両者の精度の比較はまだわかっておらず、わかっているのは VI が一般に事後分布の分散を過小評価することだ、とも述べている [arxiv-1601.00670#c5](https://arxiv.org/pdf/1601.00670v9#page=3 "We do know that variational inference generally underestimates the variance of the posterior density; this is a consequence of its objective function.")。どちらをいつ使うかの原理的な分析は、未解決の問題とされる [arxiv-1601.00670#c9](https://arxiv.org/pdf/1601.00670v9#page=26 "A principled analysis of when to use (and combine) variational inference and MCMC would have both theoretical and practical impact in the ﬁeld.")。

### VI の弱点

- **平均場近似は相関を捉えない**: 各変数の周辺分布は表せても、変数間の相関は表せない [arxiv-1601.00670#c6](https://arxiv.org/pdf/1601.00670v9#page=9 "Further, the marginal variances of the approximation under-represent those of the target density.") [arxiv-1711.05597#c2](https://arxiv.org/pdf/1711.05597v3#page=10 "The main limitation of mean ﬁeld approximations is that they explicitly ignore correlations between different variables e.g., between the spins in the Ising model.")。ADVI でも、平均場の版は共分散を無視し、分散を系統的に過小評価した [arxiv-1603.00788#c4](https://arxiv.org/pdf/1603.00788v1#page=12 "ADVI minimizes the KL divergence from the approximation to the exact posterior; this leads to a systemic underestimation of marginal variances (Bishop, 2006).")。
- **KL(q||p) の性質**: 事後分布の分散を過小評価し、近い山が複数あると対称性を破れないことがある(先行研究を引いた整理) [arxiv-1711.05597#c3](https://arxiv.org/pdf/1711.05597v3#page=10 "In other cases, it is unable to break symmetry when multiple modes are close [141], and is a comparably loose bound [221].")。α ダイバージェンスでは、α の大きさで「山を覆う」か「山を避ける」かが変わる [arxiv-1711.05597#c4](https://arxiv.org/pdf/1711.05597v3#page=10 "a smaller α leads to more mass-covering effects, while a larger α results in zero-forcing effects")。
- **局所解**: ELBO は一般に非凸で、初期値によって結果が変わる [arxiv-1601.00670#c7](https://arxiv.org/pdf/1601.00670v9#page=11 "Each initialization reaches a different value, indicating the presence of many local optima in the ELBO.")。
- **ELBO でモデルを選ぶ**: 実際にはうまくいくこともあるが、理論的には正当化されない [arxiv-1601.00670#c2](https://arxiv.org/pdf/1601.00670v9#page=7 "Though this sometimes works in practice, selecting based on a bound is not justiﬁed in theory.")。

### 大規模化と自動化

- **確率的 VI**: データの一部を使ったノイズのある自然勾配で、大規模データに広げた [arxiv-1206.7051#c3](https://arxiv.org/pdf/1206.7051v3#page=17 "This is a weighted average of the previous estimate of λ and the estimate of λ that we would obtain if the sampled data point was replicated N times.")。ただし、共役な指数型分布族のモデルに限られ [arxiv-1206.7051#c9](https://arxiv.org/pdf/1206.7051v3#page=38 "We developed our algorithm with conjugate exponential family models.")、学習率の減衰の速さにも敏感だった [arxiv-1206.7051#c8](https://arxiv.org/pdf/1206.7051v3#page=37 "All three ﬁts were sensitive to the forgetting rate; we see that a higher value (i.e., close to one) leads to convergence to a better local optimum.")。
- **ブラックボックス VI**: モデルごとの導出をやめ、同時分布さえ計算できれば使える勾配推定を使う [arxiv-1401.0118#c2](https://arxiv.org/pdf/1401.0118v1#page=3 "We emphasize that the score function and sampling algorithms depend only on the variational distribution, not the underlying model.")。ただし、勾配の分散が大きすぎることがあり [arxiv-1401.0118#c3](https://arxiv.org/pdf/1401.0118v1#page=3 "In practice, the high variance gradients would require very small steps which would lead to slow convergence.")、分散を減らす工夫が欠かせない [arxiv-1401.0118#c8](https://arxiv.org/pdf/1401.0118v1#page=7 "We found that Rao-Blackwellization reduces the variance by several orders of magnitude.")。再パラメータ化の勾配は経験的には分散が小さいことが多いが、それは保証されない [arxiv-1711.05597#c6](https://arxiv.org/pdf/1711.05597v3#page=9 "While the variance of this estimator (Eq. 16) is often lower than the variance of the score function gradient (Eq. 14), a theoretical analysis shows that this is not guaranteed, see Chapter 3 in [48].")。
- **ADVI**: 変数を制約のない空間に変換し、ガウス分布で近似する [arxiv-1603.00788#c3](https://arxiv.org/pdf/1603.00788v1#page=7 "This leads to a more accurate posterior approximation than the mean-ﬁeld Gaussian; however, it comes at a computational cost.")。事後分布の台が事前分布の台と同じだと仮定している [arxiv-1603.00788#c2](https://arxiv.org/pdf/1603.00788v1#page=5 "This is a benign assumption, which holds for most models considered in machine learning.")。変換の選び方に結果が敏感である [arxiv-1603.00788#c7](https://arxiv.org/pdf/1603.00788v1#page=16 "this is just as hard as the original goal of estimating the posterior density")。著者らは、分散や共分散が必要なら全共分散の版を、予測だけなら平均場の版を勧める [arxiv-1603.00788#c5](https://arxiv.org/pdf/1603.00788v1#page=13 "Scientists interested in posterior variances and covariances should use the full-rank approximation.")。

### より豊かな近似

- **正規化フロー**: 可逆な変換を重ねて、近似分布を柔軟にする [arxiv-1505.05770#c3](https://arxiv.org/pdf/1505.05770v6#page=3 "A normalizing ﬂow describes the transformation of a probability density through a sequence of invertible mappings.")。動機は、平均場のような限られた近似族では真の事後分布に似せられないことである [arxiv-1505.05770#c1](https://arxiv.org/pdf/1505.05770v6#page=1 "even in the asymptotic regime we are unable recover the true posterior distribution")。
- **Pathfinder**: 準ニュートン法の最適化の経路に沿って正規近似を作る [arxiv-2108.03782#c1](https://arxiv.org/pdf/2108.03782v4#page=1 "Pathﬁnder returns draws from the approximation with the lowest estimated Kullback-Leibler (KL) divergence to the true posterior.")。主な用途は MCMC の初期値を安く作ることである [arxiv-2108.03782#c9](https://arxiv.org/pdf/2108.03782v4#page=31 "Initialization to remove most of the transient bias of MCMC can succeed by producing draws within the high probability volume of the posterior without covering that posterior—it only requires draws to look reasonable.")。ただし、正規分布から遠い事後分布や、複数の山がある事後分布では弱い [arxiv-2108.03782#c6](https://arxiv.org/pdf/2108.03782v4#page=15 "The noise inherent in the stochastic gradient descent approach used by ADVI allows it to escape minor modes than can trap the L-BFGS optimizer used by Pathﬁnder.") [arxiv-2108.03782#c7](https://arxiv.org/pdf/2108.03782v4#page=24 "Therefore, Pathﬁnder tends to make a conservative guess on the high probability region when the posterior cannot be well approximated by a normal distribution.")。

## 3. 診断 — その近似は信用できるか

### MCMC の収束診断と R-hat

- **R-hat**: 複数の連鎖の間のばらつきと、連鎖の中のばらつきを比べる [arxiv-1909.11827#c3](https://arxiv.org/pdf/1909.11827v2#page=7 "The cutoﬀvalue 1.1 is generally used by MCMC practitioners, as recommended by Gelman et al. (2014).")。
- **従来の R-hat の問題**: 連鎖の平均が同じで分散だけが違うとき、従来の R-hat は問題を見逃す。分散が無限のときも同様である。また、分布の裾の収束については何も言わない [arxiv-1903.08008#c1](https://arxiv.org/pdf/1903.08008v5#page=3 "This example identiﬁed two problems with traditional bR:") [arxiv-1903.08008#c2](https://arxiv.org/pdf/1903.08008v5#page=3 "it says little about the convergence in the tails")。改訂版は、順位で正規化し、折り返した値でも計算する [arxiv-1903.08008#c7](https://arxiv.org/pdf/1903.08008v5#page=9 "To obtain a single conservative bR estimate, we propose to report the maximum of rank normalized split- bR and rank normalized folded-split- bR for each parameter.")。
- **推奨の閾値が文献で違う**: 改訂版の論文は R-hat < 1.01 を勧め、従来の推奨よりずっと厳しくしている [arxiv-1903.08008#c3](https://arxiv.org/pdf/1903.08008v5#page=4 "This threshold is much tighter than the one recommended by Gelman and Rubin (1992), reﬂecting lessons learnt over more than 25 years of use, as well as the simulation results in Appendix A.")。一方、MCMC の収束診断のレビューは、従来の 1.1 を推奨値として挙げている [arxiv-1909.11827#c3](https://arxiv.org/pdf/1909.11827v2#page=7 "The cutoﬀvalue 1.1 is generally used by MCMC practitioners, as recommended by Gelman et al. (2014).")。ベイズのワークフローは、改訂版を引いて 1.01 を標準としている [arxiv-2011.01808#c2](https://arxiv.org/pdf/2011.01808v1#page=13 "There are times when earlier stopping can make sense in the early stages of modeling.")。
- **連鎖の数と有効サンプル数**: 改訂版の論文は、既定で少なくとも4本の連鎖と [arxiv-1903.08008#c4](https://arxiv.org/pdf/1903.08008v5#page=4 "In addition, we recommend running at least four chains by default.")、順位で正規化した有効サンプル数が 400 を超えることを勧める [arxiv-1903.08008#c5](https://arxiv.org/pdf/1903.08008v5#page=5 "we recommend requiring that the rank-normalized ESS is greater than 400")。これらの目標は最初の確認であって、用途に合わせて調整すべきだとしている [arxiv-1903.08008#c9](https://arxiv.org/pdf/1903.08008v5#page=4 "However, these values should be adapted as necessary for the given application, and ultimately domain expertise should be used to check that Monte Carlo standard errors (MCSE) for all quantities of interest are small enough.")。
- **診断が見逃す例**: レビューは、R-hat が閾値を下回っても推定がまだ不正確な例を示している [arxiv-1909.11827#c5](https://arxiv.org/pdf/1909.11827v2#page=12 "Thus, GR diagnostic leads to premature termination of simulation and the inference drawn from the resulting samples can be unreliable.")。全部の連鎖が同じ山に捕まると、既存の診断がそろって見逃す例もある [arxiv-1909.11827#c6](https://arxiv.org/pdf/1909.11827v2#page=17 "Since all four chains are stuck at the same local mode, that is, these are not run long enough to move between the modes, the convergence diagnostics, including PSRF, MPSRF get fooled into thinking that the target distribution is unimodal and hence falsely detect convergence.")。多くの診断は、マルコフ連鎖の中心極限定理が成り立つことを仮定している [arxiv-1909.11827#c4](https://arxiv.org/pdf/1909.11827v2#page=8 "Finally, we would like to mention that the two spectral density based methods mentioned here, just like the ESS and the GR diagnostic, assume the existence of a Markov chain CLT (2), emphasizing the importance of the theoretical analysis discussed in Section 2.1.")。

### 変分推論の診断 — PSIS の k-hat

VI の近似の良し悪しは、ELBO だけではわからない。ELBO は再パラメータ化で変わる定数を含み、尺度に意味がないからである [arxiv-1802.02538#c1](https://arxiv.org/pdf/1802.02538v2#page=1 "This makes it next to useless as a method to assess how well the variational inference has ﬁt.")。

- **PSIS**: 近似分布から事後分布への重要度の比の裾に一般化パレート分布を当てはめ、その形のパラメータ k-hat を診断に使う [arxiv-1507.02646#c1](https://arxiv.org/pdf/1507.02646v9#page=4 "We propose a new method to stabilize the importance weights by replacing the M largest weights above the threshold u by a set of well-spaced values that are consistent with the tails of the importance distribution,")。k-hat は、近似分布と事後分布の両方の定数倍に影響されない [arxiv-1802.02538#c2](https://arxiv.org/pdf/1802.02538v2#page=3 "ˆk is invariant under any constant multiplication of p or q, which explains why we can suppress the marginal likelihood (normalizing constant) p(y) and replace the intractable p(θ/y) with p(θ, y) in (2).")。
- **閾値**: k-hat が 0.7 を超えると、推定は不安定または大きく偏りやすい [arxiv-1507.02646#c3](https://arxiv.org/pdf/1507.02646v9#page=5 "For S > 2000 this threshold is 0.7.") [arxiv-1507.02646#c7](https://arxiv.org/pdf/1507.02646v9#page=25 "If ˆk > 1, it is expected that the mean does not exist and any estimate for the mean is invalid.")。0.7 の根拠は、それを境に分散ではなく偏りが誤差を支配するという数値的な分析である [arxiv-1507.02646#c5](https://arxiv.org/pdf/1507.02646v9#page=10 "When k > 0.7, independently of S the effect of bias dominates and the variance based MCSE starts to fail (also demonstrated by the examples).")。VI の評価では、0.5 未満なら近似は十分近く、0.5〜0.7 なら完全ではないが有用とされる [arxiv-1802.02538#c3](https://arxiv.org/pdf/1802.02538v2#page=3 "If ˆk > 0.7, the PSIS convergence rate becomes impractically slow, leading to a large mean square error, and a even larger error for plain VI estimate.")。
- **限界**: k-hat は局所的な診断で、近似分布が見ていない山は無視する [arxiv-1802.02538#c7](https://arxiv.org/pdf/1802.02538v2#page=8 "In this sense, the PSIS diagnostic is a local diagnostic that will not detect unseen modes.")。周辺分布ごとの k-hat は機能しない [arxiv-1802.02538#c5](https://arxiv.org/pdf/1802.02538v2#page=4 "Secondly, a smaller ˆki does not necessary guarantee a well-performed marginal estimation.")。人工的に作れば、k-hat が小さく見えるのに不安定な例もある [arxiv-1507.02646#c9](https://arxiv.org/pdf/1507.02646v9#page=15 "It would be possible to construct also an artificial example where the tail would look thin (low Pareto ˆk) for small S with large probability, while the true tail is thick (high Pareto ˆk).")。
- **停止条件**: ADVI は停止条件に敏感で、既定の緩い条件にすると k-hat が大きく悪化した例がある [arxiv-1802.02538#c9](https://arxiv.org/pdf/1802.02538v2#page=5 "However, the performance of ADVI is sensitive to the stopping time, as in any other optimization problems.")。

### VI の誤差の上界

Huggins らは、KL ダイバージェンスが小さくても、事後分布の要約(平均や分散)の誤差は保証されないことを示した [arxiv-1910.04102#c2](https://arxiv.org/pdf/1910.04102v4#page=3 "To get a sense of scale for the KL divergence, we note that the KL divergence from a variational approximation to the exact posterior can easily range from 1 to nearly 500.")。そこで、Wasserstein 距離を通して、平均や標準偏差の誤差の上界を計算する方法を提案した [arxiv-1910.04102#c3](https://arxiv.org/pdf/1910.04102v4#page=4 "Our next result conﬁrms that the Wasserstein distance controls the error in these quantities.")。ただし、近似分布と事後分布の裾についての仮定が要る [arxiv-1910.04102#c1](https://arxiv.org/pdf/1910.04102v4#page=1 "Our bounds are widely applicable, as they require only that the approximating and exact posteriors have polynomial moments.") [arxiv-1910.04102#c4](https://arxiv.org/pdf/1910.04102v4#page=5 "Assuming the variational approximation ˆπ has polynomial (respectively, exponential) tails, our next result provides a bound on the p-Wasserstein distance using the 2-divergence (respectively, the KL divergence).")。

### シミュレーションに基づく較正(SBC)— 計算そのものを確かめる

SBC は、事前分布からパラメータを引き、それでデータを生成し、そのデータで事後分布を計算するという手順を何度も繰り返す。もとのパラメータが事後分布のサンプルの中で一様な順位になるかで、計算が正しいかを確かめる [arxiv-1804.06788#c3](https://arxiv.org/pdf/1804.06788v2#page=4 "SBC requires just one assumption: that we have a generative model for our data.")。1つの真の値だけで確かめる方法は、正しいコードでも失敗に見えることがある [arxiv-1804.06788#c1](https://arxiv.org/pdf/1804.06788v2#page=2 "Unfortunately this approach is ﬂawed, as demonstarted in a simple example.")。

- **読み方**: 順位のヒストグラムの形で、計算した事後分布が広すぎるか、狭すぎるか、偏っているかがわかる [arxiv-1804.06788#c5](https://arxiv.org/pdf/1804.06788v2#page=7 "Conversely, an algorithm that computes posteriors that are, on average, under-dispersed relative to the true posterior produces a histogram of rank statistics with a characteristic ∪ shape (Figure 6).")。
- **費用**: 多数のモデルの当てはめが必要だが、並列に計算できる [arxiv-1804.06788#c7](https://arxiv.org/pdf/1804.06788v2#page=8 "The downside of using SBC in practice is that it is expensive; instead of ﬁtting a single observation we have to ﬁt N simulated observations before even considering the measured data.") [arxiv-2011.01808#c6](https://arxiv.org/pdf/2011.01808v1#page=18 "While in many ways superior to benchmarking against a truth point, simulation-based calibration requires ﬁtting the model multiple times, which incurs a substantial computational cost, especially if we do not use extensive parallelization.")。
- **確かめられないもの**: SBC が確かめるのは計算だけで、モデルが正しいかは確かめない [arxiv-1804.06788#c4](https://arxiv.org/pdf/1804.06788v2#page=4 "Importantly, this calibration is limited exclusively to the computational aspect of our analysis.") [arxiv-2211.02383#c5](https://arxiv.org/pdf/2211.02383v3#page=4 "Additionally, SBC as a simulation method has no way to inform us about a discrepancy between the process that generated real data and the assumptions of our statistical model.")。どこに問題があるかも特定できない [arxiv-2211.02383#c4](https://arxiv.org/pdf/2211.02383v3#page=4 "However, by itself, SBC cannot determine where exactly the problem lies.")。
- **検定量の選び方**: データを無視して事前分布から引くだけのプログラムでも、データを使わない検定量だけなら SBC を通ってしまう [arxiv-2211.02383#c2](https://arxiv.org/pdf/2211.02383v3#page=9 "We generalize the result that probabilistic programs sampling from the prior distribution will pass SBC against all test quantities that do not depend on data.")。データに依存する検定量なら原理的に検出できる [arxiv-2211.02383#c1](https://arxiv.org/pdf/2211.02383v3#page=5 "We show that using test quantities that depend on data makes it possible to detect any conceivable mismatch between the generator and the probabilistic program.")。既定としては、個々のパラメータとデータの同時尤度を検定量にすることが勧められている [arxiv-2211.02383#c8](https://arxiv.org/pdf/2211.02383v3#page=21 "For practical use of SBC in everyday model and algorithm development, we recommend to use by default the individual model parameters as test quantities as well as the joint likelihood of the data and potentially a small number of other quantities.")。ベイズのワークフローの論文は、事後分布が事前分布のままでも SBC を満たしうるとしていて [arxiv-2011.01808#c9](https://arxiv.org/pdf/2011.01808v1#page=67 "In simulation based calibration, an incorrect computation program can satisfy the diagnostics if the posterior stays in the prior.")、後の研究が示した検定量の工夫で補える点である。

### 計算の問題はモデルの問題のサインかもしれない

ベイズのワークフローは、「計算の問題は、しばしばモデルの問題を示している」という経験則を紹介している。ただし「いつもではない」と限定している [arxiv-2011.01808#c8](https://arxiv.org/pdf/2011.01808v1#page=22 "When you have computational problems, often there’s a problem with your model (Yao, Vehtari, and Gelman, 2020).")。
正しく計算されていても、間違ったモデルを書いたプログラムは標準的な診断では見つからない [arxiv-2011.01808#c3](https://arxiv.org/pdf/2011.01808v1#page=16 "However, those diagnostics cannot protect against a probabilistic program that is computed correctly but encodes a diﬀerent model than the user intended.")。偽のデータで1回試しただけでは、すべてが動いているとは言えない [arxiv-2011.01808#c4](https://arxiv.org/pdf/2011.01808v1#page=17 "It is not possible to run a single fake data simulation, compute the associated posterior distribution, and declare that everything works well.")。

## 読むときの注意

- **診断の推奨は、ソフトウェアの開発者によるもの**: R-hat の改訂、SBC、PSIS、ワークフローの論文の多くは Stan の開発者によるもので、ADVI や NUTS も Stan に実装されている(カードの notes に記録)。推奨は実践経験に基づくものが多く、閾値は「最初の確認」と位置づけられている [arxiv-1903.08008#c9](https://arxiv.org/pdf/1903.08008v5#page=4 "However, these values should be adapted as necessary for the given application, and ultimately domain expertise should be used to check that Monte Carlo standard errors (MCSE) for all quantities of interest are small enough.")。
- **閾値は文献で違う**: R-hat の推奨値は 1.1 と 1.01 で分かれている [arxiv-1909.11827#c3](https://arxiv.org/pdf/1909.11827v2#page=7 "The cutoﬀvalue 1.1 is generally used by MCMC practitioners, as recommended by Gelman et al. (2014).") [arxiv-1903.08008#c3](https://arxiv.org/pdf/1903.08008v5#page=4 "This threshold is much tighter than the one recommended by Gelman and Rubin (1992), reﬂecting lessons learnt over more than 25 years of use, as well as the simulation results in Appendix A.")。どちらの基準で判定したかを確認したい。
- **比較の基準の分布**: NUTS の評価は、別に走らせた長い NUTS の実行を基準の平均・分散にしている [arxiv-1111.4246#c6](https://arxiv.org/pdf/1111.4246v1#page=19 "We measure the eﬃciency of each algorithm in terms of eﬀective sample size (ESS) normalized by the number of gradient evaluations used by each algorithm.")。ADVI の比較では、HMC が時間内に有用なサンプルを出さなかった [arxiv-1603.00788#c8](https://arxiv.org/pdf/1603.00788v1#page=18 "In both cases, HMC does not produce any useful samples within a budget of one hour; we omit HMC from here on.")。

## 使い方への示唆(本記事の整理)

論文の主張そのものではなく、本記事のまとめである。

1. **MCMC は複数の連鎖で走らせ、改訂版の R-hat と有効サンプル数を見る**: 1.01 と 400 が目安とされる [arxiv-1903.08008#c3](https://arxiv.org/pdf/1903.08008v5#page=4 "This threshold is much tighter than the one recommended by Gelman and Rubin (1992), reﬂecting lessons learnt over more than 25 years of use, as well as the simulation results in Appendix A.") [arxiv-1903.08008#c5](https://arxiv.org/pdf/1903.08008v5#page=5 "we recommend requiring that the rank-normalized ESS is greater than 400")。HMC なら発散の警告も見る [arxiv-1701.02434#c7](https://arxiv.org/pdf/1701.02434v2#page=45 "In particular, any divergent transitions encountered in a Hamiltonian Markov chain should prompt suspicion of the validity of any Markov chain Monte Carlo estimators.")。
2. **多峰性を疑うなら、診断を過信しない**: 全連鎖が同じ山に捕まると診断は見逃す [arxiv-1909.11827#c6](https://arxiv.org/pdf/1909.11827v2#page=17 "Since all four chains are stuck at the same local mode, that is, these are not run long enough to move between the modes, the convergence diagnostics, including PSRF, MPSRF get fooled into thinking that the target distribution is unimodal and hence falsely detect convergence.")。
3. **VI を使うなら k-hat で確かめる**: 0.7 を超えたら信用しない [arxiv-1507.02646#c7](https://arxiv.org/pdf/1507.02646v9#page=25 "If ˆk > 1, it is expected that the mean does not exist and any estimate for the mean is invalid.") [arxiv-1802.02538#c3](https://arxiv.org/pdf/1802.02538v2#page=3 "If ˆk > 0.7, the PSIS convergence rate becomes impractically slow, leading to a large mean square error, and a even larger error for plain VI estimate.")。分散や相関が必要なら、平均場ではなく全共分散の近似を検討する [arxiv-1603.00788#c5](https://arxiv.org/pdf/1603.00788v1#page=13 "Scientists interested in posterior variances and covariances should use the full-rank approximation.")。
4. **新しいモデルや自作のサンプラーには SBC を使う**: 検定量には、データに依存するもの(同時尤度など)を含める [arxiv-2211.02383#c8](https://arxiv.org/pdf/2211.02383v3#page=21 "For practical use of SBC in everyday model and algorithm development, we recommend to use by default the individual model parameters as test quantities as well as the joint likelihood of the data and potentially a small number of other quantities.")。
5. **計算がうまくいかないときは、モデルを疑う** [arxiv-2011.01808#c8](https://arxiv.org/pdf/2011.01808v1#page=22 "When you have computational problems, often there’s a problem with your model (Yao, Vehtari, and Gelman, 2020).")。

## わかっていないこと

- **VI と MCMC の使い分けの原理**: 未解決とされる [arxiv-1601.00670#c9](https://arxiv.org/pdf/1601.00670v9#page=26 "A principled analysis of when to use (and combine) variational inference and MCMC would have both theoretical and practical impact in the ﬁeld.")。
- **VI の近似誤差の理論**: 理論的な側面を扱う研究は少ない [arxiv-1711.05597#c7](https://arxiv.org/pdf/1711.05597v3#page=16 "Despite progress in modeling and inference, few authors address theoretical aspects of VI [95], [133], [213].")。
- **多峰の事後分布の診断**: 高次元で多峰性を検出する方法は、この範囲では示されていない [arxiv-1909.11827#c7](https://arxiv.org/pdf/1909.11827v2#page=18 "Thus, Dixit and Roy (2017)’s Tool 2 is successful in detecting the divergence of the chains.")。
- **確率的勾配 MCMC の誤差**: SGHMC の誤差解析に必要な混合の速さの評価は、不明とされる [arxiv-1402.4102#c7](https://arxiv.org/pdf/1402.4102v2#page=12 "but the corresponding bounds for SGHMC are unclear due to the irreversibility of the process")。

## 現時点での整理

- **HMC と NUTS は高次元で有効だが、発散や曲率の高い領域で失敗し、その診断は必要条件にすぎない** [arxiv-1701.02434#c3](https://arxiv.org/pdf/1701.02434v2#page=19 "Following the guidance of the gradient pulls us away from the typical set and towards the mode of the target density.") [arxiv-1701.02434#c9](https://arxiv.org/pdf/1701.02434v2#page=45 "Although these two diagnostics are powerful means of identifying many pathological target distributions, they are only necessary and not suﬃcient conditions for the validity of the Markov chain Monte Carlo estimators.")。
- **VI は速いが、分散を過小評価しやすく、相関を捉えにくく、精度の保証がない** [arxiv-1601.00670#c5](https://arxiv.org/pdf/1601.00670v9#page=3 "We do know that variational inference generally underestimates the variance of the posterior density; this is a consequence of its objective function.") [arxiv-1601.00670#c6](https://arxiv.org/pdf/1601.00670v9#page=9 "Further, the marginal variances of the approximation under-represent those of the target density.")。
- **R-hat、k-hat、SBC はそれぞれ別のことを確かめる診断で、どれも見逃す場合がある** [arxiv-1903.08008#c1](https://arxiv.org/pdf/1903.08008v5#page=3 "This example identiﬁed two problems with traditional bR:") [arxiv-1802.02538#c7](https://arxiv.org/pdf/1802.02538v2#page=8 "In this sense, the PSIS diagnostic is a local diagnostic that will not detect unseen modes.") [arxiv-2211.02383#c2](https://arxiv.org/pdf/2211.02383v3#page=9 "We generalize the result that probabilistic programs sampling from the prior distribution will pass SBC against all test quantities that do not depend on data.")。
- **推奨の閾値は文献で違い、実践経験に基づく最初の確認と位置づけられている** [arxiv-1909.11827#c3](https://arxiv.org/pdf/1909.11827v2#page=7 "The cutoﬀvalue 1.1 is generally used by MCMC practitioners, as recommended by Gelman et al. (2014).") [arxiv-1903.08008#c3](https://arxiv.org/pdf/1903.08008v5#page=4 "This threshold is much tighter than the one recommended by Gelman and Rubin (1992), reﬂecting lessons learnt over more than 25 years of use, as well as the simulation results in Appendix A.") [arxiv-1903.08008#c9](https://arxiv.org/pdf/1903.08008v5#page=4 "However, these values should be adapted as necessary for the given application, and ultimately domain expertise should be used to check that Monte Carlo standard errors (MCSE) for all quantities of interest are small enough.")。

**この整理に含まれていないもの**: ギブスサンプリングと逐次モンテカルロ法、期待値伝播法、ラプラス近似、Stan 以外の確率的プログラミング言語の個別の比較、モデルの評価と選択(LOO-CV、WAIC。姉妹プロジェクト bayesian-analysis-index で扱う題材と重なる)。

## 参照カード

- [arxiv-1111.4246](../../papers/arxiv-1111.4246.yaml) Hoffman & Gelman, "The No-U-Turn Sampler: Adaptively Setting Path Lengths in Hamiltonian Monte Carlo"
- [arxiv-1701.02434](../../papers/arxiv-1701.02434.yaml) Betancourt, "A Conceptual Introduction to Hamiltonian Monte Carlo"
- [arxiv-1402.4102](../../papers/arxiv-1402.4102.yaml) Chen, Fox & Guestrin, "Stochastic Gradient Hamiltonian Monte Carlo"
- [arxiv-1909.11827](../../papers/arxiv-1909.11827.yaml) Roy, "Convergence diagnostics for Markov chain Monte Carlo"
- [arxiv-1601.00670](../../papers/arxiv-1601.00670.yaml) Blei, Kucukelbir & McAuliffe, "Variational Inference: A Review for Statisticians"
- [arxiv-1711.05597](../../papers/arxiv-1711.05597.yaml) Zhang et al., "Advances in Variational Inference"
- [arxiv-1206.7051](../../papers/arxiv-1206.7051.yaml) Hoffman et al., "Stochastic Variational Inference"
- [arxiv-1401.0118](../../papers/arxiv-1401.0118.yaml) Ranganath, Gerrish & Blei, "Black Box Variational Inference"
- [arxiv-1603.00788](../../papers/arxiv-1603.00788.yaml) Kucukelbir et al., "Automatic Differentiation Variational Inference"
- [arxiv-1505.05770](../../papers/arxiv-1505.05770.yaml) Rezende & Mohamed, "Variational Inference with Normalizing Flows"
- [arxiv-2108.03782](../../papers/arxiv-2108.03782.yaml) Zhang et al., "Pathfinder: Parallel quasi-Newton variational inference"
- [arxiv-1507.02646](../../papers/arxiv-1507.02646.yaml) Vehtari et al., "Pareto Smoothed Importance Sampling"
- [arxiv-1802.02538](../../papers/arxiv-1802.02538.yaml) Yao et al., "Yes, but Did It Work?: Evaluating Variational Inference"
- [arxiv-1910.04102](../../papers/arxiv-1910.04102.yaml) Huggins et al., "Validated Variational Inference via Practical Posterior Error Bounds"
- [arxiv-1903.08008](../../papers/arxiv-1903.08008.yaml) Vehtari et al., "Rank-normalization, folding, and localization: An improved R-hat for assessing convergence of MCMC"
- [arxiv-1804.06788](../../papers/arxiv-1804.06788.yaml) Talts et al., "Validating Bayesian Inference Algorithms with Simulation-Based Calibration"
- [arxiv-2211.02383](../../papers/arxiv-2211.02383.yaml) Modrák et al., "Simulation-Based Calibration Checking for Bayesian Computation: The Choice of Test Quantities Shapes Sensitivity"
- [arxiv-2011.01808](../../papers/arxiv-2011.01808.yaml) Gelman et al., "Bayesian Workflow"
- [arxiv-2002.02405](../../papers/arxiv-2002.02405.yaml) Wenzel et al., "How Good is the Bayes Posterior in Deep Neural Networks Really?"
- [arxiv-2211.14097](../../papers/arxiv-2211.14097.yaml) Cappello & Madrid Padilla, "Bayesian variance change point detection with credible sets"
- [arxiv-1312.6114](../../papers/arxiv-1312.6114.yaml) Kingma & Welling, "Auto-Encoding Variational Bayes"
