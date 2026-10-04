<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Generative Modeling by Estimating Gradients of the Data Distribution

- カード: [`arxiv-1907.05600`](../../papers/arxiv-1907.05600.yaml)
- 著者: Yang Song, Stefano Ermon
- 年・掲載: 2019 NeurIPS 2019
- 原論文: [PDF](https://arxiv.org/pdf/1907.05600v3)(arXiv v3、カード作成時に読んだ版)
- タグ: diffusion-models, generative-modeling, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** First challenge for naive score-based modeling: if the data lie on a low-dimensional manifold, as is often assumed for real-world data, the score is undefined in the ambient space and score matching does not give a consistent estimator.([Introduction, p.2](https://arxiv.org/pdf/1907.05600v3#page=2 "First, if the data distribution is supported on a low dimensional manifold—as it is often assumed for many real world datasets—the score will be undeﬁned in the ambient space, and score matching will fail to provide a consistent score estimator."))
- **c2** Second challenge: in low-density regions score matching may lack samples; in a toy 2-D mixture-of-Gaussians experiment with sliced score matching, score estimates were reliable only near the modes.([Challenges of score-based generative modeling (Low data density regions), p.4](https://arxiv.org/pdf/1907.05600v3#page=4 "As the ﬁgure demonstrates, score estimation is only reliable in the immediate vicinity of the modes of pdata, where the data density is high."))
- **c3** Slow mixing: when modes are separated (or connected only by low-density regions), Langevin dynamics with the score alone may fail to recover the relative mode weights in reasonable time; in theory it can, but may need a very small step size and very many steps.([Challenges of score-based generative modeling (Slow mixing of Langevin dynamics), p.4](https://arxiv.org/pdf/1907.05600v3#page=4 "In this case, Langevin dynamics can produce correct samples in theory, but may require a very small step size and a very large number of steps to mix."))
- **c4** Approximation in sampling: with finite step size and finite steps, Langevin dynamics would need a Metropolis-Hastings correction, which the authors assume negligible when the step size is small and the number of steps large.([Sampling with Langevin dynamics, p.3](https://arxiv.org/pdf/1907.05600v3#page=3 "In this work, we assume this error is negligible when ϵ is small and T is large."))
- **c5** Training objective: NCSNs are trained with denoising score matching (Gaussian perturbation at each noise level, combined across levels with a weighting λ(σ)); the authors chose it because it is slightly faster and fits noise-perturbed scores, while noting that sliced score matching empirically trains NCSNs equally well.([Noise Conditional Score Networks: learning and inference, p.6](https://arxiv.org/pdf/1907.05600v3#page=6 "We adopt denoising score matching as it is slightly faster and naturally ﬁts the task of estimating scores of noise-perturbed data distributions."))
- **c6** Image setup: L = 10 noise levels forming a geometric sequence from σ_1 = 1 to σ_10 = 0.01 (pixels in [0,1]); annealed Langevin sampling uses T = 100 steps per noise level, step parameter ϵ = 2e-5 and uniform-noise initialization; the authors report results robust to T and that ϵ between 5e-6 and 5e-5 generally works.([Experiments (Setup), p.7](https://arxiv.org/pdf/1907.05600v3#page=7 "When using annealed Langevin dynamics for image generation, we choose T = 100 and ϵ = 2 × 10−5, and use uniform noise as our initial samples."))
- **c7** Ablation: a baseline using the same score network conditioned on a single small noise level (σ = 0.01) with vanilla Langevin dynamics fails to generate reasonable images, which the authors attribute to the small noise not providing score information in low-density regions.([Experiments (Image generation), p.8](https://arxiv.org/pdf/1907.05600v3#page=8 "As a result, this baseline fails to generate reasonable images, as shown by samples in Appendix C.1."))
- **c8** Model selection: checkpoints were saved every 5000 iterations; for CIFAR-10 and CelebA the checkpoint with the smallest FID on 1000 generated images was chosen (MNIST used the last checkpoint), and Table 1 scores were then computed on 50000 samples; the authors note ProgressiveGAN used a similar procedure.([Appendix B.2, p.15](https://arxiv.org/pdf/1907.05600v3#page=15 "For selecting our CIFAR-10 and CelebA models, we generate 1000 images for each checkpoint and choose the one with the smallest FID score computed on these 1000 images."))

