---
title: 量子化による影響 — 何が失われ、何で測ると見えるのか
kind: topic
tags: [model-compression]
depends_on: [arxiv-1712.05877, arxiv-2106.08295, arxiv-2210.17323, arxiv-2211.10438, arxiv-2306.00978, arxiv-2305.14314, arxiv-2212.09720, arxiv-2403.15447, arxiv-2310.01382, arxiv-2402.18158, arxiv-1911.05248, arxiv-2010.03058, arxiv-2411.04330, arxiv-2208.07339, arxiv-2404.14047, arxiv-2609.13031, arxiv-2608.10837, arxiv-2609.16091, arxiv-2608.18849, arxiv-2609.32898]
written_at: 2026-10-03
written_by: claude-opus-5-5 via Claude Code
---

# 量子化による影響 — 何が失われ、何で測ると見えるのか

<!-- generated:stale -->
> 未反映のカードはありません。
<!-- /generated:stale -->

## この記事の読み方

量子化は、モデルの重みや活性化を少ないビット数で表し、メモリや計算を減らす手法である。
この記事は、15本の量子化・圧縮の論文と、このリポジトリにある表データの基盤モデルの圧縮の論文5本から、次の3点を整理する。

1. 量子化の手法は**何をどう量子化**し、何を前提にしているか
2. 量子化で**何が劣化する**と報告されているか
3. その劣化は**何で測ると見えるのか**(この記事の中心)

論文の多くは大規模言語モデル(LLM)を対象にしている。画像モデルの論文と、表データの基盤モデルの論文も含む。
どのビット数でどれだけ劣化するかという数値は、モデル・手法・評価方法によって大きく変わるため、ここには書かない。各論文の結果表を参照のこと。

## 何をどう量子化するか

| 論文 | 量子化の対象と方法 | 学習し直すか |
|---|---|---|
| Jacob et al.(整数演算のみの推論) | 活性化と重みの配列ごとに1組の量子化パラメータ(スケールとゼロ点) [arxiv-1712.05877#c2](https://arxiv.org/pdf/1712.05877v1#page=3 "Our quantization scheme uses a single set of quantization parameters for all values within each activations array and within each weights array; separate arrays use separate quantization parameters.")。整数演算だけで推論する [arxiv-1712.05877#c1](https://arxiv.org/pdf/1712.05877v1#page=1 "We propose a quantization scheme that allows inference to be carried out using integer-only arithmetic, which can be implemented more efficiently than floating point inference on commonly available integer-only hardware.") | 量子化を模擬しながら学習する(QAT) [arxiv-1712.05877#c3](https://arxiv.org/pdf/1712.05877v1#page=5 "We propose an approach that simulates quantization effects in the forward pass of training.") |
| Nagel et al.(白書) | 学習後の量子化(PTQ)と QAT の両方の手順をまとめた指針 | 両方 [arxiv-2106.08295#c1](https://arxiv.org/pdf/2106.08295v1#page=1 "In most cases, PTQ is sufficient for achieving 8-bit quantization with close to floating-point accuracy.") [arxiv-2106.08295#c2](https://arxiv.org/pdf/2106.08295v1#page=1 "QAT requires fine-tuning and access to labeled training data but enables lower bit quantization with competitive results.") |
| LLM.int8() | feed-forward 層と attention の射影層の行列積を8ビット化し、外れ値の次元だけ16ビットで計算する [arxiv-2208.07339#c1](https://arxiv.org/pdf/2208.07339v2#page=1 "However, for the emergent outliers, we also include a new mixed-precision decomposition scheme, which isolates the outlier feature dimensions into a 16-bit matrix multiplication while still more than 99.9% of values are multiplied in 8-bit.") | なし。学習済みのチェックポイントをそのまま変換する [arxiv-2208.07339#c2](https://arxiv.org/pdf/2208.07339v2#page=1 "With our method, a 175B parameter 16/32-bit checkpoint can be loaded, converted to Int8, and used immediately without performance degradation.") |
| GPTQ | 重みだけを、近似的な2次の情報を使って一括で量子化する [arxiv-2210.17323#c1](https://arxiv.org/pdf/2210.17323v2#page=1 "we address this challenge, and propose GPTQ, a new one-shot weight quantization method based on approximate second-order information, that is both highly-accurate and highly-efficient.") [arxiv-2210.17323#c3](https://arxiv.org/pdf/2210.17323v2#page=6 "We perform standard uniform per-row asymmetric quantization on the min-max grid, similar to Dettmers et al. (2022).") | なし(較正データを使う) [arxiv-2210.17323#c2](https://arxiv.org/pdf/2210.17323v2#page=6 "Our entire GPTQ calibration data consists of 128 random 2048 token segments from the C4 dataset (Raffel et al., 2020), i.e., excerpts from randomly crawled websites, which represents generic text data.") |
| SmoothQuant | 重みと活性化の両方を8ビット化する。活性化の外れ値の難しさを、数学的に等価な変換で重みの側に移す [arxiv-2211.10438#c1](https://arxiv.org/pdf/2211.10438v7#page=1 "We propose SmoothQuant, a training-free, accuracy-preserving, and general-purpose post-training quantization (PTQ) solution to enable 8-bit weight, 8-bit activation (W8A8) quantization for LLMs.") [arxiv-2211.10438#c2](https://arxiv.org/pdf/2211.10438v7#page=1 "SmoothQuant smooths the activation outliers by offline migrating the quantization difficulty from activations to weights with a mathematically equivalent transformation.") | なし(学習不要の PTQ) [arxiv-2211.10438#c1](https://arxiv.org/pdf/2211.10438v7#page=1 "We propose SmoothQuant, a training-free, accuracy-preserving, and general-purpose post-training quantization (PTQ) solution to enable 8-bit weight, 8-bit activation (W8A8) quantization for LLMs.") |
| AWQ | 重みだけを低ビット化する。重要なチャネルを、重みではなく活性化の分布から見つける [arxiv-2306.00978#c1](https://arxiv.org/pdf/2306.00978v6#page=1 "We propose Activation-aware Weight Quantization (AWQ), a hardware-friendly approach for LLM low-bit weight-only quantization.") [arxiv-2306.00978#c2](https://arxiv.org/pdf/2306.00978v6#page=1 "To identify salient weight channels, we should refer to the activation distribution, not weights.") | なし(較正データを使う) [arxiv-2306.00978#c4](https://arxiv.org/pdf/2306.00978v6#page=7 "For AWQ, we used a small calibration set from the Pile (Gao et al., 2020) dataset in order not to overfit to a specific downstream domain.") |
| QLoRA | 4ビットに量子化して凍結した基盤モデルの上で、LoRA アダプタだけを学習する [arxiv-2305.14314#c1](https://arxiv.org/pdf/2305.14314v1#page=1 "QLORA backpropagates gradients through a frozen, 4-bit quantized pretrained language model into Low Rank Adapters (LoRA).") | アダプタのみ |

白書は、**8ビットなら多くの場合 PTQ で浮動小数点に近い精度が出る**こと [arxiv-2106.08295#c1](https://arxiv.org/pdf/2106.08295v1#page=1 "In most cases, PTQ is sufficient for achieving 8-bit quantization with close to floating-point accuracy.")、QAT は微調整とラベル付きの学習データを要するが、より低いビット数で競争力のある結果を出せること [arxiv-2106.08295#c2](https://arxiv.org/pdf/2106.08295v1#page=1 "QAT requires fine-tuning and access to labeled training data but enables lower bit quantization with competitive results.") を指針として挙げている。

前提にも注意が要る。QLoRA の NF4 というデータ型は、重みが正規分布に従う場合に情報理論的に最適だとされる [arxiv-2305.14314#c2](https://arxiv.org/pdf/2305.14314v1#page=1 "(a) 4-bit NormalFloat (NF4), a new data type that is information theoretically optimal for normally distributed weights")。
GPTQ・SmoothQuant・AWQ は、いずれも少量の**較正データ**を使う [arxiv-2210.17323#c2](https://arxiv.org/pdf/2210.17323v2#page=6 "Our entire GPTQ calibration data consists of 128 random 2048 token segments from the C4 dataset (Raffel et al., 2020), i.e., excerpts from randomly crawled websites, which represents generic text data.") [arxiv-2211.10438#c4](https://arxiv.org/pdf/2211.10438v7#page=5 "To get the statistics of activations, we calibrate the smoothing factors and the static quantization step sizes once with 512 random sentences from the pre-training dataset Pile, and apply the same smoothed and quantized model for all downstream tasks.") [arxiv-2306.00978#c4](https://arxiv.org/pdf/2306.00978v6#page=7 "For AWQ, we used a small calibration set from the Pile (Gao et al., 2020) dataset in order not to overfit to a specific downstream domain.")。どのデータで較正するかは、後で述べるように評価にも影響する。

## 何が劣化すると報告されているか

### 外れ値

- LLM.int8() の著者は、一定の規模を超えると**大きな値を持つ外れ値の特徴量**がすべての層に現れ、通常の8ビット量子化が失敗すると報告した [arxiv-2208.07339#c3](https://arxiv.org/pdf/2208.07339v2#page=2 "the need to explicitly represent the sparse but systematic large magnitude outlier features that ruin quantization precision once they emerge in all transformer layers starting at scales of 6.7B parameters")。
- SmoothQuant は、LLM の量子化が難しい原因を活性化の外れ値に求めている。これは先行研究を引用した動機づけで、SmoothQuant 自身の新しい発見ではない [arxiv-2211.10438#c3](https://arxiv.org/pdf/2211.10438v7#page=3 "LLMs are notoriously difficult to quantize due to the outliers in the activations (Dettmers et al., 2022; Wei et al., 2022; Bondarenko et al., 2021).")。
- 大規模な評価(Li et al.)では、多くの場合、モデルが大きいほど重みと KV キャッシュの量子化には強く、活性化の量子化には弱かった。著者はこれを、モデルが大きいほど活性化の外れ値が増えることと関連づけている [arxiv-2402.18158#c3](https://arxiv.org/pdf/2402.18158v2#page=4 "Notably, the Kurtosis of the Activation increases significantly with the size of the model, which means more outliers in the Activation tensors of larger LLMs.")。
- 画像モデルでは、出力チャネルごとの重みの範囲の大きな違いや外れ値の重みが、単純な PTQ の典型的な失敗の原因として挙げられている [arxiv-1712.05877#c4](https://arxiv.org/pdf/1712.05877v1#page=5 "We found that this approach works sufficiently well for large models with considerable representational capacity, but leads to significant accuracy drops for small models.")。BERT では、一部の活性化の値の範囲が極端に広く、その層を16ビットのまま残す必要があった [arxiv-2106.08295#c7](https://arxiv.org/pdf/2106.08295v1#page=17 "For BERT-base, we observe that a few activation tensors have extreme differences in their dynamic ranges.")。

### 低いビット数での崩壊

- 一部のモデル系列では、3ビットで不安定になり、最大のモデルでランダムに近い性能になった [arxiv-2212.09720#c5](https://arxiv.org/pdf/2212.09720v2#page=4 "Pythia and OPT are unstable for 3-bit inference where performance is close to random (35%) for the largest Pythia/OPT models.")。
- AWQ は重みだけを量子化したモデルを改善するが、2ビットのモデルは回復できず、SmoothQuant も重みと活性化を4ビットにしたモデルを部分的にしか回復できなかった [arxiv-2402.18158#c7](https://arxiv.org/pdf/2402.18158v2#page=21 "However, in the case of W2 quantization, where quantized LLMs lose their abilities entirely, AWQ cannot restore the corrupted performances.")。
- LLaMA3 は、とくに極端に低いビット数で、言語でも画像でも無視できない劣化を示した [arxiv-2404.14047#c1](https://arxiv.org/pdf/2404.14047v3#page=1 "Our experimental results indicate that LLaMA3 still suffers from non-negligible degradation in linguistic and visual contexts, particularly under ultra-low bit widths.")。GPTQ や AWQ で2ビットにしたマルチモーダルモデルは、マルチモーダルの質問応答で完全に崩れた [arxiv-2404.14047#c6](https://arxiv.org/pdf/2404.14047v3#page=9 "Notably, regardless of GPTQ or AWQ, we observe that the 2-bit LLaVA-Next-8B completely collapses in the six multi-modal QA tasks, with scores dropping to zero.")。
- 対話では、ビット数を下げると、文単位、さらに単語単位の繰り返しが起きた [arxiv-2402.18158#c5](https://arxiv.org/pdf/2402.18158v2#page=8 "Most LLM families can be quantized to W8, W8A8, and KV4 without significant loss of GPT-4 score (< 2%), as shown in Table 1.")。
- 長い文脈のタスクでは、多くの LLM が、重みや重みと活性化の量子化より KV キャッシュの量子化に敏感だった [arxiv-2402.18158#c6](https://arxiv.org/pdf/2402.18158v2#page=9 "For long-context tasks (≥4k), most LLMs are more sensitive to KV Cache Quantization than Weight-only and Weight-Activation Quantization.")。

### 学習量が多いモデルほど劣化しやすい

精度のスケーリング則の論文(Kumar et al.)は、**学習データを増やしたモデルほど PTQ による劣化が大きくなり**、ついには追加の事前学習データがかえって害になると主張する [arxiv-2411.04330#c1](https://arxiv.org/pdf/2411.04330v2#page=1 "For inference, we find that the degradation introduced by post-training quantization increases as models are trained on more data, eventually making additional pretraining data actively harmful.")。
同じデータ量なら大きいモデルほど劣化は小さく、ビット数を下げると劣化は指数的に増えた [arxiv-2411.04330#c4](https://arxiv.org/pdf/2411.04330v2#page=5 "We find that the degradation δPTQ increases in training data size across all model sizes, but that for a fixed dataset size larger models incur a smaller degradation.")。
ただし、評価は損失のスケーリングだけで、下流タスクでは評価していない。著者も、傾向は示唆にとどまるとしている [arxiv-2411.04330#c7](https://arxiv.org/pdf/2411.04330v2#page=12 "Third, we only consider loss scaling without downstream model evaluations.")。

### 少数派のデータと長い裾

- 圧縮したモデルは、全体の精度がほとんど変わらなくても、**データの狭い部分集合**で元のモデルと食い違う [arxiv-1911.05248#c1](https://arxiv.org/pdf/1911.05248v3#page=1 "We ﬁnd that models with radically different numbers of weights have comparable top-line performance metrics but diverge considerably in behavior on a narrow subset of the dataset.")。その部分集合は、人にとっても難しい例や、頻度の低い例(長い裾)に偏っていた [arxiv-1911.05248#c4](https://arxiv.org/pdf/1911.05248v3#page=2 "Compression impairs the model’s ability to predict accurately on the long-tail of less frequent instances.")。
- Hooker らの別の論文(共著者の一部が共通)は、圧縮が頻度の低い属性の性能を犠牲にして全体の性能を保ち、誤りが不釣り合いに多い一部の例(CIE)では既存のアルゴリズムの偏りを増幅すると報告した [arxiv-2010.03058#c1](https://arxiv.org/pdf/2010.03058v2#page=1 "We further establish that for CIE examples, compression ampliﬁes existing algorithmic bias.") [arxiv-2010.03058#c5](https://arxiv.org/pdf/2010.03058v2#page=5 "Compression cannibalizes performance on low-frequency attributes in order to preserve overall performance.")。
- ただし、前者の論文は、評価したどの手法でもクラスへの影響は均一ではないものの、**量子化は高い割合の枝刈りより不均衡な害が小さいようだ**と述べている [arxiv-1911.05248#c5](https://arxiv.org/pdf/1911.05248v3#page=6 "While all the techniques we benchmark evidence disparate class level impact, we note that quantization appears to introduce less disparate harm.")。

## 何で測ると見えるのか

量子化の論文の結論は、**どの指標で評価したか**に強く依存する。この記事で最も重要な点である。

| 評価の方法 | 使っている論文 | 見落としうるもの |
|---|---|---|
| パープレキシティ・損失のみ | GPTQ の主な評価 [arxiv-2210.17323#c4](https://arxiv.org/pdf/2210.17323v2#page=7 "We focus on these perplexity-based tasks, as they are known to be particularly sensitive to model quantization (Yao et al., 2022).")、精度のスケーリング則 [arxiv-2411.04330#c7](https://arxiv.org/pdf/2411.04330v2#page=12 "Third, we only consider loss scaling without downstream model evaluations.")、LLM.int8() の手法間の比較 [arxiv-2208.07339#c4](https://arxiv.org/pdf/2208.07339v2#page=5 "Additionally, we evaluate zeroshot accuracy degradation on OPT models for a range of different end tasks, where we compare our methods with a 16-bit baseline.") | 知識を要するタスクや信頼性の劣化 |
| ゼロショット精度などの下流タスク | SmoothQuant [arxiv-2211.10438#c6](https://arxiv.org/pdf/2211.10438v7#page=6 "We extensively benchmark the performance on 7 zero-shot benchmarks (by reporting the average accuracy) and 1 language modeling benchmark (perplexity).")、k ビットのスケーリング則 [arxiv-2212.09720#c3](https://arxiv.org/pdf/2212.09720v2#page=4 "To measure inference performance for k-bit quantization methods, we use perplexity on the CommonCrawl subset of The Pile (Gao et al., 2020) and mean zero-shot performance on the EleutherAI LM Evaluation harness (Gao et al., 2021).")、LLaMA3 の評価 [arxiv-2404.14047#c2](https://arxiv.org/pdf/2404.14047v3#page=2 "For the PTQ methods, we evaluate quantized LLaMA3 on the WikiText2 [18], PTB [20], and a portion of the C4 dataset [19], using perplexity (PPL) as the evaluation metric.") | 頻度の低い例、信頼性 |
| LLM による採点(GPT-4) | AWQ [arxiv-2306.00978#c6](https://arxiv.org/pdf/2306.00978v6#page=8 "We used the GPT-4 score to evaluate the quantized models' performance against the FP16 counterpart on 80 sample questions (Chiang et al., 2023).")、対話の評価 [arxiv-2402.18158#c5](https://arxiv.org/pdf/2402.18158v2#page=8 "Most LLM families can be quantized to W8, W8A8, and KV4 without significant loss of GPT-4 score (< 2%), as shown in Table 1.") | 採点者の偏り |
| 信頼性(偏見、プライバシー、毒性、公平性など) | Decoding Compressed Trust [arxiv-2403.15447#c3](https://arxiv.org/pdf/2403.15447v3#page=4 "The benchmark includes 8 trustworthy dimensions: Stereotype, Privacy, Toxicity, Fairness, Adversarial Robustness (AdvGLUE++), Out-Of-Distribution (OOD) Robustness, Robustness to Adversarial Demonstrations (AdvDemo), and Ethics.")、Li et al. [arxiv-2402.18158#c1](https://arxiv.org/pdf/2402.18158v2#page=1 "The evaluation encompasses five types of tasks: basic NLP, emergent ability, trustworthiness, dialogue, and long-context tasks.") | — |
| クラス・属性ごとの誤り | Hooker et al. の2本 [arxiv-1911.05248#c3](https://arxiv.org/pdf/1911.05248v3#page=3 "If the p-value <= 0.05, we reject the null hypothesis and consider the class to be disparately impacted by t level of compression relative to the baseline.") [arxiv-2010.03058#c2](https://arxiv.org/pdf/2010.03058v2#page=3 "To characterize the impact of compression on age and gender sub-groups we compare sub-group error rate, false positive rate (FPR) and false negative rate (FNR) between a baseline (i.e. non-compressed) and models pruned and quantized to different levels of compression (i.e. compressed).") | — |

### パープレキシティへの批判

- Jaiswal らは、LLM の圧縮手法が主にパープレキシティで評価されていることを問題にし、知識を要するタスクを含む別のベンチマーク(LLM-KICK)で評価し直した [arxiv-2310.01382#c1](https://arxiv.org/pdf/2310.01382v2#page=1 "As recent research efforts are focused on developing increasingly sophisticated compression methods, our work takes a step back and re-evaluates the effectiveness of existing SoTA compression methods, which rely on a fairly simple and widely questioned metric, perplexity (even for dense LLMs).") [arxiv-2310.01382#c4](https://arxiv.org/pdf/2310.01382v2#page=7 "For evaluation, similar to Zheng et al. (2023), we propose to use GPT-4 as a judge, which compares the compressed LLM generated summaries wrt. GPT-3.5 (text-davinci-003) generated summaries.")。その結果、**影響の小さいはずの8ビットの GPTQ でも、事実を問う質問応答で劣化が見られ**、8ビット量子化はまだ解決済みではないと主張した [arxiv-2310.01382#c6](https://arxiv.org/pdf/2310.01382v2#page=5 "3 ∼8-10% drop in performance for non-aggressive 8-bit quantization indicates that along with chasing for aggressive quantization levels (1-2 bits), it is also important to focus on yet unsolved 8-bit quantization.")。
- 一方 GPTQ の著者は、パープレキシティに基づくタスクを**量子化に敏感だから**主な評価に選んだと説明している [arxiv-2210.17323#c4](https://arxiv.org/pdf/2210.17323v2#page=7 "We focus on these perplexity-based tasks, as they are known to be particularly sensitive to model quantization (Yao et al., 2022).")。k ビットのスケーリング則の論文も、ゼロショット精度は雑音が大きいとしており、パープレキシティではなくゼロショット精度を使うと、別のデータ型のほうが良い場合があった [arxiv-2212.09720#c4](https://arxiv.org/pdf/2212.09720v2#page=4 "Still, when we use zero-shot accuracy as an evaluation metric, the float data type is sometimes better because zero-shot accuracy is noisier.")。

つまり、パープレキシティは「量子化に敏感な指標」として選ばれる一方で、「知識の喪失を捉えない指標」として批判されてもいる。**どちらも指標の一面を指している**。

### 通常の性能では見えない信頼性の劣化

- Decoding Compressed Trust は、極端な量子化(3ビット)で信頼性が大きく下がりうること、そしてそのリスクは通常の性能(MMLU)だけを見てもわからないことを示した [arxiv-2403.15447#c4](https://arxiv.org/pdf/2403.15447v3#page=1 "This increased risk cannot be uncovered by looking at benign performance alone, in turn, mandating comprehensive trustworthiness evaluation in practice.")。
- 4ビットの GPTQ では、**較正データを無作為に選ぶ偶然**によって、公平性や倫理などの指標が大きくぶれ、そのぶれは MMLU からは予測できなかった [arxiv-2403.15447#c6](https://arxiv.org/pdf/2403.15447v3#page=8 "Note that such variance is not predictable from the standard MMLU benchmark.")。
- GPTQ の著者自身も、パープレキシティのような主要な精度の指標に絞って評価しており、偏りなど副次的な影響の研究が必要だと述べている [arxiv-2210.17323#c7](https://arxiv.org/pdf/2210.17323v2#page=10 "We believe a thorough study of the impact of compression upon secondary measures, and in particular bias effects (Bender et al., 2021) is warranted, and may be rendered easier through our work.")。

### 指標が改善して見える場合の解釈

- Decoding Compressed Trust は、中程度のビット数の量子化で、倫理や公平性など一部の信頼性の指標が予想外に改善しうると報告した [arxiv-2403.15447#c5](https://arxiv.org/pdf/2403.15447v3#page=1 "Moreover, employing quantization within a moderate bit range could unexpectedly improve certain trustworthiness dimensions such as ethics and fairness.")。
- 一方 Li らは、倫理のベンチマークで、3ビットにした小さなモデルが一部の倫理的な質問を**拒否しなくなり**、その結果として正解率が上がった例を報告している [arxiv-2402.18158#c4](https://arxiv.org/pdf/2402.18158v2#page=7 "The FP16 LLM refrains from answering some ethical questions, but for W3, the model breaks this limitation and begins to provide informative answers.")。

2本の対象モデルや手法は同じではないため、前者の改善が後者と同じ仕組みによるものかは、この2本からは判断できない。ただし、**「量子化で信頼性が上がった」という結果は、拒否の振る舞いの変化によって生じうる**。読むときはこの可能性を確認する必要がある。

### 評価手続きの細部

- **較正データと評価データの重なり**: GPTQ は C4 の学習データから較正データを取っているため、C4 でのパープレキシティは完全なゼロショットではないと著者自身が断っている [arxiv-2210.17323#c5](https://arxiv.org/pdf/2210.17323v2#page=14 "We note that the calibration data used by GPTQ is sampled from the C4 training set, this task is thus not fully zero-shot.")。LLaMA3 の評価では、較正に使った WikiText2 が、パープレキシティの評価データの1つでもある [arxiv-2404.14047#c3](https://arxiv.org/pdf/2404.14047v3#page=2 "To ensure fairness in evaluation of different PTQ methods, we set WikiText2 as the calibration dataset for all quantization methods, with a sample size of 128 and a sequence length of 2048.")。
- **較正データの領域**: AWQ の著者は、GPTQ の再構成が較正データに過学習し、他の領域やモダリティでの汎用的な能力を保てない可能性があると批判している [arxiv-2306.00978#c5](https://arxiv.org/pdf/2306.00978v6#page=2 "However, the reconstruction process of GPTQ leads to an over-fitting issue to the calibration set and may not preserve the generalist abilities of LLMs for other modalities and domains.")。AWQ 自身は、特定の領域への過学習を避けるため少量の汎用データで較正する [arxiv-2306.00978#c4](https://arxiv.org/pdf/2306.00978v6#page=7 "For AWQ, we used a small calibration set from the Pile (Gao et al., 2020) dataset in order not to overfit to a specific downstream domain.")。一方 GPTQ の著者は、汎用的なウェブテキストで較正しており、タスク固有のデータは見ていないと述べている [arxiv-2210.17323#c2](https://arxiv.org/pdf/2210.17323v2#page=6 "Our entire GPTQ calibration data consists of 128 random 2048 token segments from the C4 dataset (Raffel et al., 2020), i.e., excerpts from randomly crawled websites, which represents generic text data.")。
- **ハイパーパラメータの選び方**: SmoothQuant は、移す強さを Pile の検証データの一部でのグリッドサーチで選んでいる [arxiv-2211.10438#c5](https://arxiv.org/pdf/2211.10438v7#page=5 "We get a suitable α by running a quick grid search on a subset of the Pile (Gao et al., 2020) validation set.")。白書の QAT の結果は、設定ごとに最良の学習率で報告されており、結果は検証データでのものである。学習率を選ぶための別のデータは本文に見当たらない [arxiv-2106.08295#c5](https://arxiv.org/pdf/2106.08295v1#page=24 "We present the results with the best learning rate per quantization configuration and perform no further hyper-parameter tuning.") [arxiv-2106.08295#c4](https://arxiv.org/pdf/2106.08295v1#page=17 "We evaluate all models on the respective validation sets.")。
- **一致の基準**: 「圧縮後も性能が一致する」とみなす許容幅は、論文によって違う。LLM-KICK は、先行研究の基準より意図的に緩めている [arxiv-2310.01382#c3](https://arxiv.org/pdf/2310.01382v2#page=4 "In this work, we consider ϵ0 to be ≤5% of the performance of f(x; θ, T).")。
- **相対値か絶対値か**: SmoothQuant は、量子化前後の相対的な変化に注目し、絶対値は重視しないと明言している [arxiv-2211.10438#c7](https://arxiv.org/pdf/2211.10438v7#page=5 "Note that we focus on the relative performance change before and after quantization but not the absolute value.")。
- **LLM による採点の不確かさ**: QLoRA の著者は、GPT-4 と人による評価が順位ではおおむね一致するが、強く食い違う例もあるとした [arxiv-2305.14314#c4](https://arxiv.org/pdf/2305.14314v1#page=2 "We find that GPT-4 and human evaluations largely agree on the rank of model performance in the tournaments, but we also find there are instances of strong disagreement.")。さらに、現在のチャットボットのベンチマークは性能を正確に評価するうえで信頼できないと述べている [arxiv-2305.14314#c5](https://arxiv.org/pdf/2305.14314v1#page=1 "Furthermore, we find that current chatbot benchmarks are not trustworthy to accurately evaluate the performance levels of chatbots.")。AWQ は、GPT-4 が先に提示された回答の評価を上げる傾向に気づき、両方の順序で比較している [arxiv-2306.00978#c6](https://arxiv.org/pdf/2306.00978v6#page=8 "We used the GPT-4 score to evaluate the quantized models' performance against the FP16 counterpart on 80 sample questions (Chiang et al., 2023).")。

### 速度とメモリの主張

速度の主張は、**どのハードウェアで、何を測ったか**とセットで読む必要がある。

- GPTQ の速度向上は、計算量の削減ではなくメモリの移動量の削減によるものである [arxiv-2210.17323#c6](https://arxiv.org/pdf/2210.17323v2#page=9 "our method obtains speedups from reduced memory movement, and does not lead to computational reductions.")。
- LLM.int8() の主な目的はメモリの削減で、小さいモデルでは量子化のオーバーヘッドのため16ビットより遅くなりうる [arxiv-2208.07339#c5](https://arxiv.org/pdf/2208.07339v2#page=6 "The quantization overhead can slow inference for models with less than 6.7B parameters, as compared to a FP16 baseline.")。大きなモデルでも、エンドツーエンドの推論は16ビットよりわずかに遅いが近い程度だった [arxiv-2208.07339#c6](https://arxiv.org/pdf/2208.07339v2#page=18 "Overall Int8 inference is slightly slower but close to the millisecond latency per token compared to 16-bit inference.")。
- Jacob らは、実機(Qualcomm の3種類のコア)で速度を測り [arxiv-1712.05877#c5](https://arxiv.org/pdf/1712.05877v1#page=7 "We benchmarked the MobileNet architecture with varying depth-multipliers (DM) and resolutions on ImageNet on three types of Qualcomm cores")、固定したモデルの精度の低下を最小化するより、**遅延と精度のトレードオフ**で評価すべきだと主張した [arxiv-1712.05877#c6](https://arxiv.org/pdf/1712.05877v1#page=7 "While most of the quantization literature focuses on minimizing accuracy loss for a given architecture, we advocate for a more comprehensive latency-vs-accuracy tradeoff as a better measure.")。
- AWQ は、デスクトップ向けとエッジ向けの GPU で速度を測っている [arxiv-2306.00978#c7](https://arxiv.org/pdf/2306.00978v6#page=10 "We conduct benchmarking experiments on RTX 4090 and Jetson Orin following the protocol described in exllama")。

## 論文間の一致と食い違い

### 一致: 量子化は枝刈りより害が小さい

この記事の整理では、3本が、異なる指標とモデル(前の2本は LLM、最後の1本は画像分類)で同じ方向の結果を出している。

- 信頼性の指標で、量子化は効率と信頼性の両立において枝刈りより有効だった [arxiv-2403.15447#c1](https://arxiv.org/pdf/2403.15447v3#page=1 "We find that quantization is currently a more effective approach than pruning in achieving efficiency and trustworthiness simultaneously.")
- 知識を要するタスクで、量子化は枝刈りより成功していた [arxiv-2310.01382#c5](https://arxiv.org/pdf/2310.01382v2#page=1 "and fail for N:M sparsity in knowledge-intensive tasks; current quantization methods are more successful than pruning; yet, pruned LLMs even at ≥50% sparsity are robust in-context retrieval and summarization systems")
- クラスごとの影響で、量子化は高い割合の枝刈りより不均衡な害が小さいようだった [arxiv-1911.05248#c5](https://arxiv.org/pdf/1911.05248v3#page=6 "While all the techniques we benchmark evidence disparate class level impact, we note that quantization appears to introduce less disparate harm.")

ただし、Decoding Compressed Trust と LLM-KICK の論文には共通の著者がいる(Jaiswal、Wang)。この2本の一致は、完全に独立した確認ではない。

### 食い違い1: 8ビットは劣化しないのか

- **劣化しない側**: LLM.int8() は、非常に大きなモデルまで性能の劣化がないと主張する [arxiv-2208.07339#c2](https://arxiv.org/pdf/2208.07339v2#page=1 "With our method, a 175B parameter 16/32-bit checkpoint can be loaded, converted to Int8, and used immediately without performance degradation.")。白書も、8ビットなら多くの場合 PTQ で浮動小数点に近い精度が出るとする [arxiv-2106.08295#c1](https://arxiv.org/pdf/2106.08295v1#page=1 "In most cases, PTQ is sufficient for achieving 8-bit quantization with close to floating-point accuracy.")。多くのモデル系列は、8ビットで対話の採点がほとんど下がらなかった [arxiv-2402.18158#c5](https://arxiv.org/pdf/2402.18158v2#page=8 "Most LLM families can be quantized to W8, W8A8, and KV4 without significant loss of GPT-4 score (< 2%), as shown in Table 1.")。
- **劣化する側**: 8ビットの GPTQ でも、事実を問う質問応答では劣化した [arxiv-2310.01382#c6](https://arxiv.org/pdf/2310.01382v2#page=5 "3 ∼8-10% drop in performance for non-aggressive 8-bit quantization indicates that along with chasing for aggressive quantization levels (1-2 bits), it is also important to focus on yet unsolved 8-bit quantization.")。

両者は量子化の方法(LLM.int8() は外れ値を16ビットで残す。GPTQ は重みのみ)、モデル、指標(パープレキシティ・ゼロショット精度か、知識を要する質問応答か)が違う。**「8ビットなら安全」は、指標とタスクを限定した上での主張**として読むべきである。

### 食い違い2: 大きいモデルほど量子化に強いのか

- **強い側**: LLaMA3 の最大のモデルは、極端に低いビット数でも様々な量子化手法に対して頑健だった [arxiv-2404.14047#c5](https://arxiv.org/pdf/2404.14047v3#page=5 "Moreover, we find that the LLaMA3-70B model shows significant robustness to different quantization methods, even for ultra-low bit-width quantization.")。同じデータ量なら、大きいモデルほど PTQ の劣化は小さい [arxiv-2411.04330#c4](https://arxiv.org/pdf/2411.04330v2#page=5 "We find that the degradation δPTQ increases in training data size across all model sizes, but that for a fixed dataset size larger models incur a smaller degradation.")。画像モデルでは、学習後に量子化する方法は大きいモデルでは十分に機能し、小さいモデルで精度が大きく落ちた [arxiv-1712.05877#c4](https://arxiv.org/pdf/1712.05877v1#page=5 "We found that this approach works sufficiently well for large models with considerable representational capacity, but leads to significant accuracy drops for small models.")。
- **弱い側**: 活性化の量子化については、大きいモデルほど弱かった [arxiv-2402.18158#c3](https://arxiv.org/pdf/2402.18158v2#page=4 "Notably, the Kurtosis of the Activation increases significantly with the size of the model, which means more outliers in the Activation tensors of larger LLMs.")。外れ値の特徴量は一定の規模を超えてから現れる [arxiv-2208.07339#c3](https://arxiv.org/pdf/2208.07339v2#page=2 "the need to explicitly represent the sparse but systematic large magnitude outlier features that ruin quantization precision once they emerge in all transformer layers starting at scales of 6.7B parameters")。

この食い違いは、**何を量子化するか**(重みか活性化か)で説明がつく可能性がある。Li らの1本の中で、重み・KV キャッシュと活性化とで逆の傾向が出ている [arxiv-2402.18158#c3](https://arxiv.org/pdf/2402.18158v2#page=4 "Notably, the Kurtosis of the Activation increases significantly with the size of the model, which means more outliers in the Activation tensors of larger LLMs.")。
また、精度のスケーリング則によれば、劣化は大きさだけでなく**学習データの量**にも依存する [arxiv-2411.04330#c1](https://arxiv.org/pdf/2411.04330v2#page=1 "For inference, we find that the degradation introduced by post-training quantization increases as models are trained on more data, eventually making additional pretraining data actively harmful.")。

### 食い違い3: 外れ値への対処は役に立つのか

k ビットのスケーリング則の論文は、外れ値に依存する量子化(LLM.int8() と SmoothQuant を引用)は予測性能を改善するが、**ビット数あたりの効率のスケーリングには効かない**ことを示した [arxiv-2212.09720#c6](https://arxiv.org/pdf/2212.09720v2#page=2 "While earlier work has shown that it is possible to significantly improve the predictive performance of quantized models by using outlier-dependent quantization (Dettmers et al., 2022a; Xiao et al., 2022), we show that this is not effective for bit-level scaling.")。
この記事の解釈では、これは SmoothQuant の主張(外れ値を扱えば W8A8 の精度を保てる) [arxiv-2211.10438#c1](https://arxiv.org/pdf/2211.10438v7#page=1 "We propose SmoothQuant, a training-free, accuracy-preserving, and general-purpose post-training quantization (PTQ) solution to enable 8-bit weight, 8-bit activation (W8A8) quantization for LLMs.") [arxiv-2211.10438#c2](https://arxiv.org/pdf/2211.10438v7#page=1 "SmoothQuant smooths the activation outliers by offline migrating the quantization difficulty from activations to weights with a mathematically equivalent transformation.") と矛盾するものではない。前者は「モデル全体のビット数あたりの精度」、後者は「特定のビット数での精度の低下」を測っており、**問いが違う**。

### LoRA による回復は、モデルによって効き方が違う

QLoRA は、4ビットの QLoRA が、確立した評価設定の学術ベンチマークで16ビットの微調整と同等の性能だったとしている [arxiv-2305.14314#c3](https://arxiv.org/pdf/2305.14314v1#page=7 "Our results consistently show that 4-bit QLORA with NF4 data type matches 16-bit full finetuning and 16-bit LoRA finetuning performance on academic benchmarks with well-established evaluation setups.")。ただし、33B と 65B の規模での同等性は確立できていない [arxiv-2305.14314#c6](https://arxiv.org/pdf/2305.14314v1#page=15 "Despite this evidence, we did not establish that QLORA can match full 16-bit finetuning performance at 33B and 65B scales.")。
LLaMA3 の評価では、LLaMA3-8B を4ビットより低いビット数にしたとき、LoRA による微調整をしても量子化の誤差を補えず、かえって MMLU が悪化した。LLaMA や LLaMA2 の場合とは対照的である [arxiv-2404.14047#c4](https://arxiv.org/pdf/2404.14047v3#page=7 "On the MMLU dataset, the most notable observation with LLaMA3-8B under LoRA-FT quantization is that low-rank fine-tuning on the Alpaca [36] dataset not only fails to compensate for the errors introduced by quantization, but actually exacerbates the degradation.")。

## 表データの基盤モデルの圧縮

このリポジトリの表データのテーマでも、TabPFN などの基盤モデルを軽くする研究が2026年に出てきている。

- **attention の量子化**(Kübler et al.): TabPFN-v3 と TabICLv2 の attention を FP8 で計算し、16ビットのカーネルより速く、問題になる精度の低下はなかったと報告している [arxiv-2609.13031#c2](https://arxiv.org/pdf/2609.13031v1#page=1 "Our Triton kernel achieves a speedup up to 1.7x over regular 16-bit kernels, and we show that on TabPFN-v3 and TabICLv2 there is no relevant accuracy loss across TabArena and BeyondArena.")。
  - 表データの文脈内学習に特有の注意点として、**テスト行と学習行の量子化誤差をそろえないと**精度が大きく落ちると指摘した [arxiv-2609.13031#c1](https://arxiv.org/pdf/2609.13031v1#page=1 "We find that it is crucial to align the quantization error in the test rows with the quantization error in the training rows, as otherwise the accuracy drops drastically.")。
  - 劣化の検定は、学習後の量子化はモデルを悪くすることしかないという仮定の下での片側の符号検定である [arxiv-2609.13031#c4](https://arxiv.org/pdf/2609.13031v1#page=3 "Following Kübler et al. [2026] we assume that post-training quantization can only make the model worse and use a one-sided sign test.")。
  - 著者は全員が Prior Labs の所属で、利益相反の記載は本文に見当たらない [arxiv-2609.13031#c5](https://arxiv.org/pdf/2609.13031v1#page=1 "Correspondence: jonas@priorlabs.ai")。参考文献リストによれば、著者には TabPFN の論文の第一著者(Hollmann)と TabPFN-v3 の技術報告の共著者(Flöge)が含まれる。評価に使った TabArena の共著者でもある著者が含まれる [arxiv-2609.13031#c6](https://arxiv.org/pdf/2609.13031v1#page=5 "Salinas, and Frank Hutter. Tabarena: A living benchmark for machine learning on tabular data.")。
- **層の枝刈り**(TACTICL): 文脈内学習のモデルの層を、下流タスクで学習した軽いアダプタに置き換える [arxiv-2608.10837#c1](https://arxiv.org/pdf/2608.10837v1#page=1 "an automated task-aware compression framework for tabular in-context learning models that jointly prunes transformer layers and replaces them with lightweight adapters trained on downstream tasks, thus blending in-context with in-weight learning")。文献でよく使われる層の重要度の指標では良い圧縮の構成を選べず、どのデータセットでも最適な構成は1つではなかった [arxiv-2608.10837#c5](https://arxiv.org/pdf/2608.10837v1#page=10 "Notably, we find that layer-importance metrics commonly used in the literature fail to identify good compression configurations.")。
- **蒸留**: TabPFN を小さなネットワークに蒸留する研究がある [arxiv-2609.16091#c1](https://arxiv.org/pdf/2609.16091v1#page=1 "We distill a TabPFN teacher into a compact feed-forward student across a business-decision simulation on UCI Adult and five OpenML benchmarks") [arxiv-2608.18849#c1](https://arxiv.org/pdf/2608.18849v2#page=1 "We propose GEAR (Generative Expansion and Real Anchoring), a modular two-stage framework that distills TFMs into lightweight MLP or tree-based predictors that can be deployed on commodity CPUs.")。前者は、遅延の改善のほとんどが文脈内学習の TabPFN を推論経路から外したことによると分析している [arxiv-2609.16091#c2](https://arxiv.org/pdf/2609.16091v1#page=1 "Span-level attribution shows that this wall-clock gain is almost entirely from removing in-context TabPFN from the hot path; fewer cloud round-trips cut token cost (2.1×) rather than latency.")。後者は、生徒の学習に使う教師の予測を交差検証の外側の予測にして、自己ラベル付けによる漏れを避けている [arxiv-2608.18849#c2](https://arxiv.org/pdf/2608.18849v2#page=1 "Stage 2 re-anchors the student to the target distribution using real labels and out-of-fold teacher predictions, which avoids self-labeling leakage.")。
- **早期終了**: 外れ値検出の基盤モデルで、途中の層で推論を打ち切ると検出が良くなりうると報告した研究がある [arxiv-2609.32898#c2](https://arxiv.org/pdf/2609.32898v1#page=1 "can also improve detection performance on diverse real-world benchmarks by 4.7–7.3% on average, consistent across three distinct foundation models")。ただし、データセットごとの最良の層は**テストの正解を使って選んだ参考値**で、そのまま使える手法ではない [arxiv-2609.32898#c5](https://arxiv.org/pdf/2609.32898v1#page=7 "Both use ground-truth test AUROCs and are reported as references.")。

LLM の量子化の研究と比べると、表データでは**少数派のデータや信頼性への影響を調べた研究は、このリポジトリにはまだない**。

## 評価者の独立性

量子化の手法は、製品やライブラリと結び付いていることが多い。PDF の所属表記と本文によれば次のとおりである。

- Jacob et al. の著者は Google の所属で、手法は TensorFlow Lite に採用されたものである [arxiv-1712.05877#c7](https://arxiv.org/pdf/1712.05877v1#page=2 "The quantization scheme described here is the one adopted in TensorFlow Lite [5] and we will refer to specific parts of its code to illustrate aspects discussed below.")。
- 白書の著者は Qualcomm AI Research の所属である。
- SmoothQuant と AWQ の著者には NVIDIA の所属が含まれる。
- LLM.int8() の著者には Hugging Face と Facebook AI Research の所属が含まれ、ソフトウェア(bitsandbytes)を公開し、Hugging Face Transformers に組み込んでいる。
- LLaMA3 の評価論文は、参考文献リストで著者の一部が共著者になっている手法(SliM-LLM など)を評価しているが、利益相反はないと宣言している [arxiv-2404.14047#c7](https://arxiv.org/pdf/2404.14047v3#page=12 "Wei Huang, Haotong Qin, Yangdong Liu, Yawei Li, Xianglong Liu, Luca Benini, et al. SliM-LLM: Salience-driven mixed-precision quantization for large language models.")。
- 表データの attention の量子化は、評価したモデル(TabPFN-v3)の論文の著者を含む研究である(上記)。

一方、量子化の**害**を示した論文(Hooker et al. の2本、Decoding Compressed Trust、LLM-KICK、Li et al.)の著者は、カードの著者リストで見る限り、この記事で扱う GPTQ・SmoothQuant・AWQ・LLM.int8() の著者と重ならない。

## 現時点での整理

- **量子化の影響は、測り方に強く依存する**。パープレキシティや平均的な精度では、知識を要するタスク [arxiv-2310.01382#c6](https://arxiv.org/pdf/2310.01382v2#page=5 "3 ∼8-10% drop in performance for non-aggressive 8-bit quantization indicates that along with chasing for aggressive quantization levels (1-2 bits), it is also important to focus on yet unsolved 8-bit quantization.")、信頼性 [arxiv-2403.15447#c4](https://arxiv.org/pdf/2403.15447v3#page=1 "This increased risk cannot be uncovered by looking at benign performance alone, in turn, mandating comprehensive trustworthiness evaluation in practice.")、頻度の低いデータ [arxiv-1911.05248#c1](https://arxiv.org/pdf/1911.05248v3#page=1 "We ﬁnd that models with radically different numbers of weights have comparable top-line performance metrics but diverge considerably in behavior on a narrow subset of the dataset.") での劣化を見落としうる。用途に関わる指標で確かめる必要がある。
- **何を量子化するかで傾向が逆になる**。多くの場合、重みと KV キャッシュの量子化には大きいモデルが強く、活性化の量子化には弱い [arxiv-2402.18158#c3](https://arxiv.org/pdf/2402.18158v2#page=4 "Notably, the Kurtosis of the Activation increases significantly with the size of the model, which means more outliers in the Activation tensors of larger LLMs.")。
- **低いビット数では崩壊がありうる**。とくに3ビット以下 [arxiv-2212.09720#c5](https://arxiv.org/pdf/2212.09720v2#page=4 "Pythia and OPT are unstable for 3-bit inference where performance is close to random (35%) for the largest Pythia/OPT models.") [arxiv-2402.18158#c7](https://arxiv.org/pdf/2402.18158v2#page=21 "However, in the case of W2 quantization, where quantized LLMs lose their abilities entirely, AWQ cannot restore the corrupted performances.") [arxiv-2404.14047#c6](https://arxiv.org/pdf/2404.14047v3#page=9 "Notably, regardless of GPTQ or AWQ, we observe that the 2-bit LLaVA-Next-8B completely collapses in the six multi-modal QA tasks, with scores dropping to zero.")。
- **較正データは結果を左右する**。領域 [arxiv-2306.00978#c5](https://arxiv.org/pdf/2306.00978v6#page=2 "However, the reconstruction process of GPTQ leads to an over-fitting issue to the calibration set and may not preserve the generalist abilities of LLMs for other modalities and domains.")、偶然 [arxiv-2403.15447#c6](https://arxiv.org/pdf/2403.15447v3#page=8 "Note that such variance is not predictable from the standard MMLU benchmark.")、評価データとの重なり [arxiv-2210.17323#c5](https://arxiv.org/pdf/2210.17323v2#page=14 "We note that the calibration data used by GPTQ is sampled from the C4 training set, this task is thus not fully zero-shot.") を確認する。
- **量子化は枝刈りより害が小さい**という点は、条件の異なる複数の論文で同じ方向である(うち2本は共著者が共通) [arxiv-2403.15447#c1](https://arxiv.org/pdf/2403.15447v3#page=1 "We find that quantization is currently a more effective approach than pruning in achieving efficiency and trustworthiness simultaneously.") [arxiv-2310.01382#c5](https://arxiv.org/pdf/2310.01382v2#page=1 "and fail for N:M sparsity in knowledge-intensive tasks; current quantization methods are more successful than pruning; yet, pruned LLMs even at ≥50% sparsity are robust in-context retrieval and summarization systems") [arxiv-1911.05248#c5](https://arxiv.org/pdf/1911.05248v3#page=6 "While all the techniques we benchmark evidence disparate class level impact, we note that quantization appears to introduce less disparate harm.")。
- **「指標が改善した」は要注意**。拒否しなくなったことによる見かけの改善がありうる [arxiv-2402.18158#c4](https://arxiv.org/pdf/2402.18158v2#page=7 "The FP16 LLM refrains from answering some ethical questions, but for W3, the model breaks this limitation and begins to provide informative answers.")。
- **学習量の多い新しいモデルほど量子化しにくくなる可能性**がある [arxiv-2411.04330#c1](https://arxiv.org/pdf/2411.04330v2#page=1 "For inference, we find that the degradation introduced by post-training quantization increases as models are trained on more data, eventually making additional pretraining data actively harmful.")。これは損失だけによる示唆的な結果である [arxiv-2411.04330#c7](https://arxiv.org/pdf/2411.04330v2#page=12 "Third, we only consider loss scaling without downstream model evaluations.")。

**この整理に含まれていないもの**: LLM 向けの QAT(LLM-QAT など)、KV キャッシュ専用の量子化手法、FP8 での学習、2値化・3値化、量子化が説明手法(SHAP など)の結果に与える影響。最後の点を扱う論文は、このリポジトリにはまだない。

## 参照カード

- [arxiv-1712.05877](../../papers/arxiv-1712.05877.yaml) Jacob et al., "Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference"
- [arxiv-2106.08295](../../papers/arxiv-2106.08295.yaml) Nagel et al., "A White Paper on Neural Network Quantization"
- [arxiv-2208.07339](../../papers/arxiv-2208.07339.yaml) Dettmers et al., "LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale"
- [arxiv-2210.17323](../../papers/arxiv-2210.17323.yaml) Frantar et al., "GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers"
- [arxiv-2211.10438](../../papers/arxiv-2211.10438.yaml) Xiao et al., "SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models"
- [arxiv-2306.00978](../../papers/arxiv-2306.00978.yaml) Lin et al., "AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration"
- [arxiv-2305.14314](../../papers/arxiv-2305.14314.yaml) Dettmers et al., "QLoRA: Efficient Finetuning of Quantized LLMs"
- [arxiv-2212.09720](../../papers/arxiv-2212.09720.yaml) Dettmers & Zettlemoyer, "The case for 4-bit precision: k-bit Inference Scaling Laws"
- [arxiv-2403.15447](../../papers/arxiv-2403.15447.yaml) Hong et al., "Decoding Compressed Trust: Scrutinizing the Trustworthiness of Efficient LLMs Under Compression"
- [arxiv-2310.01382](../../papers/arxiv-2310.01382.yaml) Jaiswal et al., "Compressing LLMs: The Truth is Rarely Pure and Never Simple"
- [arxiv-2402.18158](../../papers/arxiv-2402.18158.yaml) Li et al., "Evaluating Quantized Large Language Models"
- [arxiv-2404.14047](../../papers/arxiv-2404.14047.yaml) Huang et al., "An empirical study of LLaMA3 quantization: from LLMs to MLLMs"
- [arxiv-2411.04330](../../papers/arxiv-2411.04330.yaml) Kumar et al., "Scaling Laws for Precision"
- [arxiv-1911.05248](../../papers/arxiv-1911.05248.yaml) Hooker et al., "What Do Compressed Deep Neural Networks Forget?"
- [arxiv-2010.03058](../../papers/arxiv-2010.03058.yaml) Hooker et al., "Characterising Bias in Compressed Models"
- [arxiv-2609.13031](../../papers/arxiv-2609.13031.yaml) Kübler et al., "Attention Quantization for Tabular Foundation Models"
- [arxiv-2608.10837](../../papers/arxiv-2608.10837.yaml) Koshil et al., "TACTICL: Task-Aware Compression of Tabular ICL Models"
- [arxiv-2609.16091](../../papers/arxiv-2609.16091.yaml) Dey & Kumar, "Distilling Foundation Models for Agentic What-If Reasoning:Cost, Latency, and Governance in a Hybrid LLM+SLM Architecture"
- [arxiv-2608.18849](../../papers/arxiv-2608.18849.yaml) Qin et al., "GEAR: Generative Expansion and Real Anchoring for Two-Stage Distillation of Tabular Foundation Models"
- [arxiv-2609.32898](../../papers/arxiv-2609.32898.yaml) Zhou & Akoglu, "When Less Compute Is More: Adaptive Early Exit Improves Pretrained Outlier Detection"
