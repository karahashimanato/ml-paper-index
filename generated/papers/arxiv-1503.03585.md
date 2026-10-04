<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Deep Unsupervised Learning using Nonequilibrium Thermodynamics

- カード: [`arxiv-1503.03585`](../../papers/arxiv-1503.03585.yaml)
- 著者: Jascha Sohl-Dickstein, Eric A. Weiss, Niru Maheswaranathan, Surya Ganguli
- 年・掲載: 2015 ICML 2015
- 原論文: [PDF](https://arxiv.org/pdf/1503.03585v8)(arXiv v8、カード作成時に読んだ版)
- タグ: diffusion-models, generative-modeling, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Core idea: structure in the data distribution is slowly destroyed by an iterative forward diffusion process, and a reverse diffusion process that restores the structure is learned, giving a flexible and tractable generative model; the idea is described as inspired by non-equilibrium statistical physics.([Abstract, p.1](https://arxiv.org/pdf/1503.03585v8#page=1 "The essential idea, inspired by non-equilibrium statistical physics, is to systematically and slowly destroy structure in a data distribution through an iterative forward diffusion process."))
- **c2** Why the reverse steps can be Gaussian (or binomial): citing Feller (1949), for continuous diffusion (the limit of small step size β) the reversal of the diffusion has the same functional form as the forward process; the longer the trajectory, the smaller β can be made, and only the mean and covariance (or bit-flip probability) of each reverse step must be estimated.([Section 2.2, p.5](https://arxiv.org/pdf/1503.03585v8#page=5 "For both Gaussian and binomial diffusion, for continuous diffusion (limit of small step size β) the reversal of the diffusion process has the identical functional form as the forward process (Feller, 1949)."))
- **c3** Cost: running the algorithm costs the evaluation of the mean/covariance (or flip-rate) functions times the number of time steps; all results in the paper use multi-layer perceptrons for these functions.([Section 2.2, p.5](https://arxiv.org/pdf/1503.03585v8#page=5 "The computational cost of running this algorithm is the cost of these functions, times the number of time-steps."))
- **c4** Training maximizes a lower bound K on the log likelihood (via Jensen's inequality; the derivation parallels variational Bayes, and the bound becomes an equality only if forward and reverse trajectories are identical, i.e. a quasi-static process); this reduces density estimation to regression on the functions setting the means and covariances of a sequence of Gaussians.([Section 2.4, p.6](https://arxiv.org/pdf/1503.03585v8#page=6 "Thus, the task of estimating a probability distribution has been reduced to the task of performing regression on the functions which set the mean and covariance of a sequence of Gaussians (or set the state ﬂip probability for a sequence of Bernoulli trials)."))
- **c5** Noise schedule: the choice of β_t is stated to be important for performance; for Gaussian diffusion the schedule β_2..T is learned by gradient ascent on K (with 'frozen noise'), while the first-step variance β_1 is fixed to a small constant to prevent overfitting; binomial diffusion uses the fixed schedule β_t = (T − t + 1)^-1.([Section 2.4.1, p.6](https://arxiv.org/pdf/1503.03585v8#page=6 "The variance β1 of the ﬁrst step is ﬁxed to a small constant to prevent overﬁtting."))
- **c6** A footnote to the schedule paragraph adds that recent experiments suggest a fixed schedule (the same as for binomial diffusion) may be just as effective as learning it.([Section 2.4.1 (footnote 2), p.6](https://arxiv.org/pdf/1503.03585v8#page=6 "Recent experiments suggest that it is just as effective to instead use the same ﬁxed βt schedule as for binomial diffusion."))
- **c7** Evaluation caveat (footnote 3): an earlier version of the paper reported higher CIFAR-10 log-likelihood bounds that came from the model learning the 8-bit pixel quantization; the reported bounds are for data with uniform noise added to remove quantization, following Theis et al. (2015).([Section 3 (footnote 3), p.7](https://arxiv.org/pdf/1503.03585v8#page=7 "These were the result of the model learning the 8-bit quantization of pixel values in the CIFAR-10 dataset."))
- **c8** MNIST comparison protocol: although the training algorithm gives an asymptotically consistent lower bound on log likelihood, most previously reported continuous-MNIST results use Parzen-window estimates from samples, so for comparison the MNIST log likelihood was estimated with the Parzen-window code released with Goodfellow et al. (2014).([Section 3.2.1, p.9](https://arxiv.org/pdf/1503.03585v8#page=9 "For this comparison we therefore estimate MNIST log likelihood using the Parzen-window code released with (Goodfellow et al., 2014)."))

