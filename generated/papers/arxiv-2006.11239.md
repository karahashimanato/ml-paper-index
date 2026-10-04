<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Denoising Diffusion Probabilistic Models

- カード: [`arxiv-2006.11239`](../../papers/arxiv-2006.11239.yaml)
- 著者: Jonathan Ho, Ajay Jain, Pieter Abbeel
- 年・掲載: 2020 NeurIPS 2020
- 原論文: [PDF](https://arxiv.org/pdf/2006.11239v2)(arXiv v2、カード作成時に読んだ版)
- タグ: diffusion-models, generative-modeling, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Main stated contribution: a particular parameterization of diffusion models reveals an equivalence with denoising score matching over multiple noise levels during training and with annealed Langevin dynamics during sampling (citing [55, 61]); the best sample quality was obtained with this parameterization.([Introduction, p.2](https://arxiv.org/pdf/2006.11239v2#page=2 "We obtained our best sample quality results using this parameterization (Section 4.2), so we consider this equivalence to be one of our primary contributions."))
- **c2** Forward process: the forward-process variances β_t are fixed to constants rather than learned, so the approximate posterior q has no learnable parameters and the L_T term is constant during training; the forward process admits sampling x_t at any timestep in closed form.([Diffusion models and denoising autoencoders (Forward process and L_T), p.3](https://arxiv.org/pdf/2006.11239v2#page=3 "Thus, in our implementation, the approximate posterior q has no learnable parameters, so LT is a constant during training and can be ignored."))
- **c3** ε-prediction: training the reverse-process mean through a network that predicts the added noise ε makes the sampler resemble Langevin dynamics and turns the variational bound into an objective resembling denoising score matching; the authors note it is just another parameterization of p_θ(x_{t−1}|x_t), and that predicting x_0 led to worse sample quality early in their experiments.([Diffusion models and denoising autoencoders (Reverse process), p.4](https://arxiv.org/pdf/2006.11239v2#page=4 "We have shown that the ϵ-prediction parameterization both resembles Langevin dynamics and simpliﬁes the diffusion model’s variational bound to an objective that resembles denoising score matching."))
- **c4** L_simple drops the per-term weights of the bound, making it a weighted variational bound; with their diffusion setup this down-weights the small-t terms (denoising very small noise) so the network can focus on harder denoising tasks at larger t, which the authors report leads to better sample quality.([Simplified training objective, p.5](https://arxiv.org/pdf/2006.11239v2#page=5 "Since our simpliﬁed objective (14) discards the weighting in Eq. (12), it is a weighted variational bound that emphasizes different aspects of reconstruction compared to the standard variational bound [18, 22]."))
- **c5** Likelihood vs sample quality: training on the true variational bound gives better codelengths than training on the simplified objective, while the simplified objective gives the best sample quality.([Experiments (Sample quality), p.6](https://arxiv.org/pdf/2006.11239v2#page=6 "We ﬁnd that training our models on the true variational bound yields better codelengths than training on the simpliﬁed objective, as expected, but the latter yields the best sample quality."))
- **c6** Stated limitation: despite their sample quality, the models' log likelihoods are not competitive with other likelihood-based models (though better than the large AIS-based estimates reported for energy-based models and score matching); the authors find most of the lossless codelength is spent on imperceptible image details.([Introduction, p.2](https://arxiv.org/pdf/2006.11239v2#page=2 "Despite their sample quality, our models do not have competitive log likelihoods compared to other likelihood-based models"))
- **c7** Sampling cost: T = 1000 is used for all experiments so that the number of network evaluations during sampling matches previous work [53, 55]; β_t increases linearly from 1e-4 to 0.02.([Experiments, p.5](https://arxiv.org/pdf/2006.11239v2#page=5 "We set T = 1000 for all experiments so that the number of neural network evaluations needed during sampling matches previous work [53, 55]."))
- **c8** Evaluation protocol: hyperparameters were mostly searched for CIFAR10 sample quality and transferred to other datasets; final models were trained once and evaluated throughout training, and the reported sample-quality scores and log likelihood are at the checkpoint with minimum FID; IS/FID use 50000 samples.([Appendix B (Experimental details), p.15](https://arxiv.org/pdf/2006.11239v2#page=15 "Sample quality scores and log likelihood are reported on the minimum FID value over the course of training."))

