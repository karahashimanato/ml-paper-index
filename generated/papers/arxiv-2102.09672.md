<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Improved Denoising Diffusion Probabilistic Models

- カード: [`arxiv-2102.09672`](../../papers/arxiv-2102.09672.yaml)
- 著者: Alex Nichol, Prafulla Dhariwal
- 年・掲載: 2021
- 原論文: [PDF](https://arxiv.org/pdf/2102.09672v1)(arXiv v1、カード作成時に読んだ版)
- タグ: diffusion-models, generative-modeling, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Motivation: Ho et al. (2020) obtained high-fidelity samples by FID and Inception Score but were unable to achieve competitive log-likelihoods with DDPMs; the authors argue it is important to explore why, since this may suggest a fundamental shortcoming such as bad mode coverage.([3. Improving the Log-likelihood, p.3](https://arxiv.org/pdf/2102.09672v1#page=3 "Thus, it is important to explore why DDPMs seem to perform poorly on this metric, since this may suggest a fundamental shortcoming such as bad mode coverage."))
- **c2** Diagnosis: beta_t and beta-tilde_t (the two fixed variance choices of Ho et al.) are almost equal except near t = 0, which may explain why the choice does not matter for samples; but the first few diffusion steps contribute the most to the variational lower bound, so a better choice of Sigma_theta seems likely to improve log-likelihood (shown in Figures 1-2).([3.1. Learning Σθ(xt, t), p.3](https://arxiv.org/pdf/2102.09672v1#page=3 "Thus, it seems likely that we could improve log-likelihood by using a better choice of Σθ(xt, t)."))
- **c3** The linear noise schedule of Ho et al. (2020) worked well for high-resolution images but was sub-optimal at 64x64 and 32x32, because the end of the forward process is too noisy and contributes little to sample quality; the cosine schedule is the proposed fix. The authors say the choice of cos^2 was arbitrary.([3.2. Improving the Noise Schedule, p.4](https://arxiv.org/pdf/2102.09672v1#page=4 "We found that while the linear noise schedule used in Ho et al. (2020) worked well for high resolution images, it was sub-optimal for images of resolution 64 × 64 and 32 × 32."))
- **c4** Optimizing L_vlb directly was difficult in practice, at least on ImageNet 64x64: the hybrid objective reached better training-set log-likelihoods in the same training time, which the authors attribute to much noisier L_vlb gradients (confirmed by gradient noise scales); importance sampling of timesteps then allowed the best log-likelihoods by optimizing L_vlb.([3.3. Reducing Gradient Noise, p.5](https://arxiv.org/pdf/2102.09672v1#page=5 "With this importance sampled objective, we are able to achieve our best log-likelihoods by optimizing Lvlb."))
- **c5** Likelihood vs sample quality trade-off: L_hybrid with the cosine schedule improves log-likelihood while keeping FID similar to the Ho et al. baseline, whereas optimizing L_vlb further improves log-likelihood at the cost of a higher FID; the authors generally prefer L_hybrid.([3.4. Results and Ablations, p.5](https://arxiv.org/pdf/2102.09672v1#page=5 "Optimizing Lvlb further improves log-likelihood at the cost of a higher FID."))
- **c6** Ablation setup: to study the modifications, fixed model architectures with fixed hyperparameters are trained on ImageNet 64x64 and CIFAR-10. In early experiments, increasing T from 1000 to 4000 improved log-likelihood, and T = 4000 is used for the rest of the section.([3. Improving the Log-likelihood, p.3](https://arxiv.org/pdf/2102.09672v1#page=3 "To study the effects of different modiﬁcations, we train ﬁxed model architectures with ﬁxed hyperparameters on the ImageNet 64 × 64 (van den Oord et al., 2016b) and CIFAR-10 (Krizhevsky, 2009) datasets."))
- **c7** FID protocol: 50K samples were generated except for unconditional ImageNet 64x64, where 10K samples were used; the authors note that 10K samples biases FID upward and accept this because FID is mainly used for relative comparisons there. Reference statistics use the full training set for CIFAR-10 and ImageNet.([Appendix A (Hyperparameters), p.11](https://arxiv.org/pdf/2102.09672v1#page=11 "Since we mainly use FID for relative comparisons on unconditional ImageNet 64×64, this bias is acceptable."))
- **c8** Scaling: validation NLL does not fit a power law in training compute as cleanly as FID; the authors list possible causes (an unexpectedly high irreducible loss or overfitting) and note these models were trained with L_hybrid rather than L_vlb, so they do not achieve optimal log-likelihoods.([6. Scaling Model Size, p.8](https://arxiv.org/pdf/2102.09672v1#page=8 "We also note that these models do not achieve optimal log-likelihoods in general because they were trained with our Lhybrid objective and not directly with Lvlb to keep both good log-likelihoods and sample quality."))

