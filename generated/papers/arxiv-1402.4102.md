<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Stochastic Gradient Hamiltonian Monte Carlo

- カード: [`arxiv-1402.4102`](../../papers/arxiv-1402.4102.yaml)
- 著者: Tianqi Chen, Emily B. Fox, Carlos Guestrin
- 年・掲載: 2014 ICML 2014
- 原論文: [PDF](https://arxiv.org/pdf/1402.4102v2)(arXiv v2、カード作成時に読んだ版)
- タグ: bayesian-deep-learning, mcmc, posterior-inference, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Naive stochastic-gradient HMC: approximating the minibatch gradient noise as Gaussian (central limit theorem), replacing the gradient adds diffusion to the momentum, and the target pi(theta, r) is no longer invariant (Corollary 3.1); Theorem 3.1 shows the entropy increases, which the authors say hints that the distribution tends toward a uniform distribution.([Section 3.1, p.3](https://arxiv.org/pdf/1402.4102v2#page=3 "Formally, as given by Corollary 3.1 of Theorem 3.1, when B is nonzero, π(θ, r) of Eq. (3) is no longer invariant under the dynamics described by Eq. (7)."))
- **c2** Correcting naive SG-HMC with Metropolis-Hastings creates a trade-off: an MH step after short simulations needs a full-data computation each time, while long simulations between MH steps lead to very low acceptance rates.([Section 3.1, p.4](https://arxiv.org/pdf/1402.4102v2#page=4 "Each of these MH steps requires a costly computation using all of the data, thus defeating the computational gains of considering noisy gradients."))
- **c3** Friction: adding a friction term B M^-1 r to the momentum update gives second-order Langevin dynamics for which pi(theta, r) is the unique stationary distribution of the continuous system (Theorem 3.2); the authors relate it to partial momentum refreshment, which had not greatly improved HMC with noise-free gradients (citing Neal, 2010).([Section 3.2, p.5](https://arxiv.org/pdf/1402.4102v2#page=5 "The key was to introduce a friction term using second-order Langevin dynamics."))
- **c4** Relation to SGLD: SGLD's first-order Langevin dynamics can be viewed as the limiting case of SGHMC's dynamics with a large friction term.([Section 3.2, p.5](https://arxiv.org/pdf/1402.4102v2#page=5 "In particular, the dynamics of SGLD can be viewed as second-order Langevin dynamics with a large friction term."))
- **c5** In practice the gradient-noise covariance B is unknown; with a user-set friction C dominating an estimate B_hat (e.g. B_hat = 0), exact correctness is obtained only as the step size goes to zero, and decreasing step sizes reduce efficiency, so like SGLD the authors use a small non-zero step size, accepting some bias (a finite-step error analysis is in the supplement).([Section 3.3, p.6](https://arxiv.org/pdf/1402.4102v2#page=6 "As in (Welling & Teh, 2011; Ahn et al., 2012) for SGLD, we consider using a small, non-zero ϵ leading to some bias."))
- **c6** No Metropolis-Hastings correction is used in SGHMC; the authors note that, as in SGLD, an MH correction is not even possible because the probability of the reverse dynamics cannot be computed.([Section 3.3 (footnote 1), p.6](https://arxiv.org/pdf/1402.4102v2#page=6 "We note that, just as in SGLD, an MH correction is not even possible because we cannot compute the probability of the reverse dynamics."))
- **c7** The supplementary error analysis (Theorem F.1, chi-squared divergence decreasing as the noise-estimation error shrinks) assumes a mixing-rate bound; the authors state that such bounds exist for SGLD but are unclear for SGHMC because the process is irreversible, and leave this for future work.([Appendix F, p.12](https://arxiv.org/pdf/1402.4102v2#page=12 "but the corresponding bounds for SGHMC are unclear due to the irreversibility of the process"))
- **c8** Experiments: a 1-D simulated target with synthetic gradient noise (naive SG-HMC deviates from the truth unless MH is added, SGHMC without MH is close), a correlated bivariate Gaussian against SGLD, a Bayesian two-layer network on MNIST, and online Bayesian PMF on MovieLens ml-1M; on MovieLens both SGHMC and SGLD beat the optimization baselines and the authors report SGLD and SGHMC results as very similar.([Section 4.3, p.8](https://arxiv.org/pdf/1402.4102v2#page=8 "In this experiment, the results for SGLD and SGHMC are very similar."))

