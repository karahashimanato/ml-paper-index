---
title: 知識蒸留と枝刈り — 小さなモデルに何を移し、何を削るのか、そして何が失われるのか
kind: method
tags: [knowledge-distillation, pruning]
depends_on: [arxiv-1503.02531, arxiv-1412.6550, arxiv-1805.04770, arxiv-1910.01108, arxiv-1910.01348, arxiv-2106.05945, arxiv-1506.02626, arxiv-1510.00149, arxiv-1803.03635, arxiv-1810.05270, arxiv-2003.03033, arxiv-1912.05671, arxiv-1710.01878, arxiv-1810.02340, arxiv-2005.07683, arxiv-2301.00774, arxiv-2306.11695, arxiv-1911.05248, arxiv-2010.03058, arxiv-2310.01382, arxiv-2403.15447]
written_at: 2026-10-10
written_by: claude-opus-5-5 via Claude Code
---

# 知識蒸留と枝刈り — 小さなモデルに何を移し、何を削るのか、そして何が失われるのか

<!-- generated:stale -->
> 未反映のカードはありません。
<!-- /generated:stale -->

## この記事の読み方

大きなモデルを、より小さく速いモデルにする方法のうち、次の2つを扱う。

- **知識蒸留**:大きなモデル(先生)の出力をまねるように、小さなモデル(生徒)を学習させる。
- **枝刈り**:学習したモデルの重みの一部を0にして(取り除いて)、残りで同じ仕事をさせる。

もう1つの代表的な方法である量子化は、[量子化による影響](../topics/quantization-effects.md) の記事と [数式の解説 9](../math/09-quantization.md) で扱った。
この記事は17本の新しいカードと、圧縮の影響を扱った既存の4本のカードから、次の4点を整理する。

1. 知識蒸留:柔らかい目標と温度、中間層のヒント、同じ大きさへの蒸留、生徒は先生をまねできているか
2. 枝刈り:大きさに基づく枝刈りと再学習、段階的な枝刈り、初期化時の枝刈り、宝くじ仮説、転移学習と大規模言語モデルでの枝刈り
3. 枝刈りの評価の問題
4. 圧縮で何が失われるか

性能の数値は書かない。各論文のページの結果表を参照のこと(カードは結果表を記録せず、主張だけを記録している)。

## 1. 知識蒸留

### 柔らかい目標と温度

Hinton らは、大きなモデル(またはアンサンブル)が出す各クラスの確率を、小さなモデルの学習目標(**柔らかい目標**)に使うことを提案した。柔らかい目標はエントロピーが高いとき、正解ラベルだけよりも1件あたりの情報が多く、勾配のばらつきも小さい [arxiv-1503.02531#c1](https://arxiv.org/pdf/1503.02531v1#page=2 "When the soft targets have high entropy, they provide much more information per training case than hard targets and much less variance in the gradient between training cases,")。

確率を柔らかくするために、ソフトマックスに**温度** $T$ を入れる [arxiv-1503.02531#c2](https://arxiv.org/pdf/1503.02531v1#page=3 "The same high temperature is used when training the distilled model, but after it has been trained it uses a temperature of 1.")。

$$
q_i = \frac{\exp(z_i / T)}{\sum_j \exp(z_j / T)}
$$

$T$ を大きくすると、確率は均等に近づく([数式の解説 3](../math/03-uncertainty-and-calibration.md) の温度スケーリングと同じ形)。学習中は先生と生徒に同じ高い温度を使い、学習後は $T = 1$ に戻す [arxiv-1503.02531#c2](https://arxiv.org/pdf/1503.02531v1#page=3 "The same high temperature is used when training the distilled model, but after it has been trained it uses a temperature of 1.")。

正解ラベルが使えるときは、柔らかい目標との交差エントロピーと、正解ラベルとの交差エントロピーの重み付き平均を目的関数にする。柔らかい目標の勾配は $1/T^2$ の大きさになるので、$T^2$ を掛けて釣り合いを取る。正解ラベルの重みはかなり小さくしたほうがよかった、と論文は述べている [arxiv-1503.02531#c3](https://arxiv.org/pdf/1503.02531v1#page=3 "This ensures that the relative contributions of the hard and soft targets remain roughly unchanged if the temperature used for distillation is changed while experimenting with meta-parameters.")。
温度がロジットに比べて十分高く、ロジットを事例ごとに平均0にそろえた場合、蒸留は先生と生徒のロジットの2乗誤差を小さくすることと同じになる [arxiv-1503.02531#c4](https://arxiv.org/pdf/1503.02531v1#page=3 "At lower temperatures, distillation pays much less attention to matching logits that are much more negative than the average.")。

MNIST の実験では、生徒が十分大きいときは高い温度なら大差がなかったが、生徒がとても小さいときは中くらいの温度のほうがよかった [arxiv-1503.02531#c6](https://arxiv.org/pdf/1503.02531v1#page=4 "But when this was radically reduced to 30 units per layer, temperatures in the range 2.5 to 4 worked signiﬁcantly better than higher or lower temperatures.")。
論文は、専門家モデルの知識を1つの大きなモデルに蒸留し戻すことはまだ示せていない、と限界も述べている [arxiv-1503.02531#c9](https://arxiv.org/pdf/1503.02531v1#page=8 "We have not yet shown that we can distill the knowledge in the specialists back into the single large net.")。

### 中間層のヒント(FitNets)

FitNets は、出力だけでなく、先生の中間層の出力(**ヒント**)も生徒にまねさせる。生徒の中間層の上に回帰器を置いて先生の中間層の大きさに合わせ、2乗誤差を小さくする [arxiv-1412.6550#c2](https://arxiv.org/pdf/1412.6550v4#page=3 "The deeper we set the guided layer, the less ﬂexibility we give to the network and, therefore, FitNets are more likely to suffer from over-regularization.") [arxiv-1412.6550#c3](https://arxiv.org/pdf/1412.6550v4#page=3 "To mitigate this limitation, we use a convolutional regressor instead.")。
学習は段階的で、まずヒントで生徒の前半を学習し、その後で全体を蒸留の損失で学習する [arxiv-1412.6550#c4](https://arxiv.org/pdf/1412.6550v4#page=5 "In order to promote the learning of more complex examples (examples with lower teacher conﬁdence), we gradually anneal λ during the training with a linear decay.")。ヒントは正則化として働くので、深すぎる層を合わせると制約が強くなりすぎる、と論文は注意している [arxiv-1412.6550#c2](https://arxiv.org/pdf/1412.6550v4#page=3 "The deeper we set the guided layer, the less ﬂexibility we give to the network and, therefore, FitNets are more likely to suffer from over-regularization.")。

論文は、細くて深い生徒が先生を上回ったことから、深さが重要だと示唆している [arxiv-1412.6550#c6](https://arxiv.org/pdf/1412.6550v4#page=5 "Our student model outperforms the teacher model, while requiring notably fewer parameters, suggesting that depth is crucial to achieve better representations.")。計算量を固定した比較では、通常の学習や出力だけの蒸留では深い生徒をうまく学習できず、ヒントを使うとより深い生徒を学習できた [arxiv-1412.6550#c8](https://arxiv.org/pdf/1412.6550v4#page=8 "HT tends to ease these optimization issues and is able to train 13-layer networks of 30M multiplications.")。

### 同じ大きさへの蒸留(Born-Again Networks)

Furlanello らは、生徒を先生と**同じ構造**にして蒸留した。圧縮ではなく、蒸留そのものの効果を調べている [arxiv-1805.04770#c1](https://arxiv.org/pdf/1805.04770v2#page=1 "We call these students Born-Again Networks (BANs) and show that applied to DenseNets, ResNets and LSTM-based sequence models, BANs consistently have lower validation errors than their teachers.")。
論文は、蒸留の勾配を「誤りのクラスの確率から来る項」と「正解クラスについて、先生の確信度で重み付けした項」に分け、後者がサンプルの重要度による重み付けに似ていると述べる [arxiv-1805.04770#c3](https://arxiv.org/pdf/1805.04770v2#page=4 "Or is dark knowledge simply performing a kind of importance weighting?")。その上で、誤りのクラスの情報を消した対照実験から、蒸留は確信度による重み付けだけで効いているのではないと結論している [arxiv-1805.04770#c4](https://arxiv.org/pdf/1805.04770v2#page=7 "These results demonstrate that KD does not simply contribute information on each speciﬁc non-correct output.")。
世代を重ねたときの改善は頭打ちになるが、世代のアンサンブルでは改善が続いた [arxiv-1805.04770#c5](https://arxiv.org/pdf/1805.04770v2#page=4 "We ﬁnd the improvements of the sequence to saturate, but we are able to produce signiﬁcant gains through ensembling.")。

### 言語モデルの蒸留(DistilBERT)

DistilBERT は BERT の層の数を半分にした生徒で、温度付きの蒸留損失、マスク言語モデルの損失、隠れ状態の向きを合わせるコサイン損失の線形結合で学習する [arxiv-1910.01108#c1](https://arxiv.org/pdf/1910.01108v4#page=2 "We found it beneﬁcial to add a cosine embedding loss (Lcos) which will tend to align the directions of the student and teacher hidden states vectors.")。
隠れ層の幅より層の数を減らしたのは、幅の変更が計算効率に与える影響が小さいという彼らの調査に基づく [arxiv-1910.01108#c2](https://arxiv.org/pdf/1910.01108v4#page=2 "Thus we focus on reducing the number of layers.")。生徒は先生の層を1つおきに取って初期化し、これが収束に重要だと述べている [arxiv-1910.01108#c3](https://arxiv.org/pdf/1910.01108v4#page=2 "we initialize the student from the teacher by taking one layer out of two.")。
評価は GLUE の開発セットで、5つのシードの中央値である [arxiv-1910.01108#c5](https://arxiv.org/pdf/1910.01108v4#page=3 "DistilBERT also compares surprisingly well to BERT, retaining 97% of the performance with 40% fewer parameters.")。著者は Hugging Face に所属し、モデルを自社の Transformers ライブラリで公開している [arxiv-1910.01108#c8](https://arxiv.org/pdf/1910.01108v4#page=2 "We have made the trained weights available along with the training code in the Transformers2")。

### 生徒は先生をまねできているか

蒸留は「先生をまねる」ことを目指すが、2本の論文はそれが思ったほどできていないことを示した。

- **大きい先生がよい先生とは限らない。** Cho と Hariharan は、先生を大きくしていくと、先生の精度は上がり続けるのに、生徒の精度はある所から下がることを報告した [arxiv-1910.01348#c4](https://arxiv.org/pdf/1910.01348v1#page=3 "As can be seen, as the teacher becomes larger and more accurate, the student becomes less accurate.")。最も大きい先生では生徒との予測の不一致も大きく、容量の小さい生徒が大きい先生をまねられないためだと推測している [arxiv-1910.01348#c5](https://arxiv.org/pdf/1910.01348v1#page=4 "This suggests that the student is unable to mimic large teachers")。対策として、蒸留を学習の途中で止める方法や、先生の学習を早めに止める方法を提案している [arxiv-1910.01348#c6](https://arxiv.org/pdf/1910.01348v1#page=4 "it begins to hurt accuracy towards the end of training.") [arxiv-1910.01348#c8](https://arxiv.org/pdf/1910.01348v1#page=7 "Notice that for both student models (WRN16-1 and WRN28-1), all early-stopped teachers produce better students than the optimal fully-trained teacher (WRN16-3 and WRN28-3).")。何段階かに分けて蒸留する方法は解決にならなかった [arxiv-1910.01348#c7](https://arxiv.org/pdf/1910.01348v1#page=5 "Sequential distillation cannot help make large models better teachers.")。
- **生徒の精度が上がっても、先生の再現はできていない。** Stanton らは、生徒が先生を完全にまねる容量を持っていても、両者の予測分布には大きな差が残ることが多いと報告した [arxiv-2106.05945#c1](https://arxiv.org/pdf/2106.05945v2#page=1 "there often remains a surprisingly large discrepancy between the predictive distributions of the teacher and the student, even in cases when the student has the capacity to perfectly match the teacher.")。同じ大きさへの自己蒸留で生徒が先生を上回るのは、蒸留がうまくいっていないからこそ起きる、と述べている [arxiv-2106.05945#c4](https://arxiv.org/pdf/2106.05945v2#page=4 "This result is only possible by virtue of failing at the distillation procedure: if the student matched the teacher perfectly then the student could not outperform the teacher.")。蒸留に使ったデータの上でさえ生徒は先生に一致せず [arxiv-2106.05945#c7](https://arxiv.org/pdf/2106.05945v2#page=8 "However, the results presented in this section suggest that in practice the optimization method is unable to achieve high ﬁdelity even on the distillation dataset when extensive data augmentation or synthetic data is used.")、学習を長くしたり最適化手法を変えたりしても大きくは改善しなかったことから、原因は最適化の難しさにあると見ている [arxiv-2106.05945#c8](https://arxiv.org/pdf/2106.05945v2#page=10 "Furthermore, the suboptimal convergence of knowledge distillation appears to be a consequence of the optimization dynamics speciﬁcally, and not simply initialization bias.")。

**本記事の整理**:蒸留の評価では、「生徒の精度が上がったか」(汎化)と「生徒が先生に一致したか」(忠実度)を分けて読む必要がある。Stanton らは、忠実度を測るために、独立に学習した別の先生から同じ手順で蒸留した生徒と比べる対照を置いている [arxiv-2106.05945#c3](https://arxiv.org/pdf/2106.05945v2#page=3 "To account for such confounding when evaluating the distillation of a student s from a teacher t, we also evaluate another student s′ distilled through an identical procedure from an independent teacher.")。

## 2. 枝刈り

### 大きさに基づく枝刈りと再学習

Han らの方法は、通常どおり学習し、しきい値より小さい重みを取り除き、残った重みを再学習する、という3段階である。再学習をしないと精度が大きく落ちるので、再学習は不可欠だと述べている [arxiv-1506.02626#c2](https://arxiv.org/pdf/1506.02626v3#page=3 "If the pruned network is used without retraining, accuracy is signiﬁcantly impacted.")。

- しきい値は層ごとに、重みの標準偏差に品質のパラメータを掛けて決める [arxiv-1506.02626#c6](https://arxiv.org/pdf/1506.02626v3#page=4 "The pruning threshold is chosen as a quality parameter multiplied by the standard deviation of a layer’s weights.")。
- 再学習では、生き残った重みを初期化し直さずに使う [arxiv-1506.02626#c4](https://arxiv.org/pdf/1506.02626v3#page=3 "So when we retrain the pruned layers, we should keep the surviving parameters instead of re-initializing them.")。
- 一度に大きく刈るより、刈る・再学習するを繰り返すほうが、精度を落とさずに多く刈れた [arxiv-1506.02626#c5](https://arxiv.org/pdf/1506.02626v3#page=4 "Without loss of accuracy, this method can boost pruning rate from 5× to 9× on AlexNet compared with single-step aggressive pruning.")。
- 再学習には、元の学習より長い時間がかかった [arxiv-1506.02626#c7](https://arxiv.org/pdf/1506.02626v3#page=5 "It took 173 hours to retrain the pruned AlexNet.")。

Deep Compression は、この枝刈りの後に、重みを k-means でまとめて共有する量子化とハフマン符号化を重ねた。枝刈りの段は著者ら自身の先行研究に基づく [arxiv-1510.00149#c2](https://arxiv.org/pdf/1510.00149v5#page=2 "We build on top of that approach.")。論文は、枝刈りと量子化を組み合わせると、どちらか一方だけより小さくしても精度が落ちなかったと報告している [arxiv-1510.00149#c7](https://arxiv.org/pdf/1510.00149v5#page=7 "But when combined, as shown in the red line, the network can be compressed to 3% of original size with no loss of accuracy.")。

### 段階的な枝刈り

Zhu と Gupta は、学習中に疎の割合(0の重みの割合)を少しずつ上げていく方法を使った。各層にマスクを付け、絶対値の小さい重みから0にしていき、マスクされた重みは更新しない [arxiv-1710.01878#c2](https://arxiv.org/pdf/1710.01878v2#page=3 "We introduce a new automated gradual pruning algorithm in which the sparsity is increased from an initial sparsity value si (usually 0) to a ﬁnal sparsity value sf over a span of n pruning steps,")。
枝刈りの進め方は学習率の進め方と合わせるべきで、学習率が小さすぎると回復が難しく、大きすぎると重みが収束する前に刈ってしまう、と述べている [arxiv-1710.01878#c3](https://arxiv.org/pdf/1710.01878v2#page=4 "so it is important to choose the pruning schedule closely with the learning rate schedule.")。

この論文の問いは「同じメモリ量なら、大きなモデルを刈った疎なモデルと、最初から小さい密なモデルのどちらがよいか」である [arxiv-1710.01878#c1](https://arxiv.org/pdf/1710.01878v2#page=1 "We compare the accuracy of large, but pruned models (large-sparse) and their smaller, but dense (small-dense) counterparts with identical memory footprint.")。MobileNet や言語モデルの比較では、疎なモデルのほうがよかったと報告している [arxiv-1710.01878#c4](https://arxiv.org/pdf/1710.01878v2#page=5 "We see that for a given number of non-zero parameters, sparse MobileNets are able to outperform dense MobileNets.") [arxiv-1710.01878#c5](https://arxiv.org/pdf/1710.01878v2#page=6 "When pruning a model of a certain size, we use the same hyperparameters that were used for training the dense model of that size.")。ただし、刈りすぎると性能が大きく落ちるので、最適な圧縮の範囲がある、とも述べている [arxiv-1710.01878#c6](https://arxiv.org/pdf/1710.01878v2#page=7 "Together, these results suggest that there is an optimal compression range when pruning.")。

### 学習前に刈る(SNIP)

SNIP は、学習を始める前の初期化の時点で、一度だけ刈る。各結合を取り除いたときに損失がどれだけ変わるか(結合の感度)を、1回の順伝播と逆伝播で近似する [arxiv-1810.02340#c1](https://arxiv.org/pdf/1810.02340v2#page=4 "Based on this hypothesis, we deﬁne connection sensitivity as the normalized magnitude of the derivatives:")。
大きさやヘッセ行列に基づく基準は重みの大きさに依存するので、事前の学習が必要で、構造の選び方に敏感だ、と批判している [arxiv-1810.02340#c2](https://arxiv.org/pdf/1810.02340v2#page=3 "Despite being popular, both of these criteria depend on the scale of the weights and in turn require pretraining and are very sensitive to the architectural choices.")。感度を初期化の時点で測るので、分散をそろえる初期化を勧めている [arxiv-1810.02340#c3](https://arxiv.org/pdf/1810.02340v2#page=5 "Thus, we advocate the use of variance scaling methods (e.g., Glorot & Bengio (2010)) to initialize the weights, such that the variance remains the same throughout the network.")。
学習が速くなるという主張は理論上のもので、実測した学習時間は示されていない [arxiv-1810.02340#c4](https://arxiv.org/pdf/1810.02340v2#page=3 "Therefore, our method eliminates the need for the expensive prune – retrain cycles, and in theory, it can be an order of magnitude faster than the standard neural network training as it can be implemented using software libraries that support sparse matrix computations.")。

### 宝くじ仮説

Frankle と Carbin の**宝くじ仮説**は、「ランダムに初期化した密なネットワークの中には、単独で学習しても元のネットワークと同じ精度に、同じ反復数以内で達する部分ネットワークがある」というものである [arxiv-1803.03635#c1](https://arxiv.org/pdf/1803.03635v5#page=2 "A randomly-initialized, dense neural network contains a subnet-work that is initialized such that—when trained in isolation—it can match the test accuracy of the original network after training for at most the same number of iterations.")。

この部分ネットワーク(当たりくじ)を見つけるには、学習し、絶対値の小さい重みを刈ってマスクを作り、残った重みを**元の初期値に戻して**学習し直す [arxiv-1803.03635#c2](https://arxiv.org/pdf/1803.03635v5#page=2 "Unique to our work, each unpruned connection’s value is then reset to its initialization from original network before it was trained.")。マスクはそのままで初期値だけをランダムに取り直すと、性能はずっと悪くなった。著者は、構造だけでは当たりくじの成功を説明できないと解釈している [arxiv-1803.03635#c4](https://arxiv.org/pdf/1803.03635v5#page=3 "When randomly reinitialized, winning tickets perform far worse, meaning structure alone cannot explain a winning ticket’s success.")。

限界として、扱ったのは MNIST と CIFAR10 の画像分類だけで、刈る・学習するを何度も繰り返す必要があるため、ImageNet のような大きなデータでは調べていない [arxiv-1803.03635#c7](https://arxiv.org/pdf/1803.03635v5#page=9 "We only consider vision-centric classiﬁcation tasks on smaller datasets (MNIST, CIFAR10).")。

後の論文で Frankle らは、この「初期値に戻す」手順が、大きなネットワークでは当たりくじを見つけられないことを示した [arxiv-1912.05671#c5](https://arxiv.org/pdf/1912.05671v4#page=5 "However, IMP subnetworks of standard ResNet-20, standard VGG-16, ResNet-50, and Inception-v3 are not matching.")。初期値ではなく、少し学習した時点の値に戻す(**巻き戻し**)と見つかる [arxiv-1912.05671#c4](https://arxiv.org/pdf/1912.05671v4#page=5 "IMP trains a network to completion, prunes weights with the lowest magnitudes globally, and rewinds the remaining weights back to their values at iteration k (Algorithm 2).")。
その条件を、SGD のノイズに対する安定性で説明している。同じ所から異なるノイズで2回学習した結果を直線で結んだとき、途中で誤差が上がらなければ安定とする [arxiv-1912.05671#c1](https://arxiv.org/pdf/1912.05671v4#page=3 "Empirically, we con-sider instability < 2% to be stable; this margin accounts for noise and matches increases in error along paths found by Draxler et al. (2018, Table B.1) and Garipov et al. (2018, Table 2).")。調べた範囲では、部分ネットワークは安定なときに限って元の精度に届いた [arxiv-1912.05671#c6](https://arxiv.org/pdf/1912.05671v4#page=7 "In summary, at these extreme sparsities, IMP subnetworks are matching when they are stable.")。著者らは、学習を少し進めてから刈るほうがよい可能性を示唆している [arxiv-1912.05671#c8](https://arxiv.org/pdf/1912.05671v4#page=9 "Recent proposals attempt to prune networks at initialization (Lee et al., 2019; Wang et al., 2020), but our results suggest that the best time to do so may be after some training.")。

### 刈った重みに価値はあるか(Rethinking)

Liu らは、構造的な枝刈り(チャネルなどの単位で刈る)の手法を調べ、刈ったモデルを微調整しても、同じ構造を**ランダムな初期値から学習**した場合と同程度か、それより悪いことを示した [arxiv-1810.05270#c1](https://arxiv.org/pdf/1810.05270v2#page=1 "For all state-of-the-art structured pruning algorithms we examined, ﬁne-tuning a pruned model only gives comparable or worse performance than training that model with randomly initialized weights.")。
比較の条件として、同じエポック数で学習する場合と、同じ計算量で学習する場合を分けている [arxiv-1810.05270#c2](https://arxiv.org/pdf/1810.05270v2#page=4 "In our experiments, we use Scratch-E to denote training the small pruned models for the same epochs, and Scratch-B to denote training for the same amount of computation budget")。

- 著者らは、刈った手法の価値は「重要な重みを選ぶこと」より「効率のよい構造を見つけること」(暗黙のアーキテクチャ探索)にある場合がある、と解釈している [arxiv-1810.05270#c5](https://arxiv.org/pdf/1810.05270v2#page=2 "identifying efﬁcient struc-tures and performing implicit architecture search, rather than selecting “important” weights.")。
- 構造的でない枝刈り(重み単位)では事情が違い、刈る割合が大きいときや ImageNet では微調整のほうがよい場合があった [arxiv-1810.05270#c3](https://arxiv.org/pdf/1810.05270v2#page=7 "On the large-scale ImageNet dataset, we note that the Scratch-B result is mostly worse than ﬁne-tuned result by a noticable margin, despite at a decent accuracy level.")。
- 宝くじ仮説との比較では、評価した設定のうち、当たりくじの初期値が役立ったのは、構造的でない枝刈りで学習率が小さい場合だけだった [arxiv-1810.05270#c7](https://arxiv.org/pdf/1810.05270v2#page=12 "To summarize, in our evaluated settings, the winning ticket only brings improvement in the case of unstructured pruning, with small initial learning rate, but this small learning rate yields inferior accuracy compared with the widely-used large learning rate.")。
- 文献の結果との食い違いは、ハイパーパラメータ、データ拡張、ベースラインの計算予算の違いで説明できるかもしれない、と述べている [arxiv-1810.05270#c4](https://arxiv.org/pdf/1810.05270v2#page=2 "The contradiction between some of our results and those reported in the literature might be explained by less carefully chosen hyper-parameters, data augmentation schemes and unfair computation budget for evaluating baseline approaches.")。

### 転移学習での枝刈り(Movement Pruning)

事前学習したモデルを微調整するときは、重みの大きさはほぼ事前学習で決まっているので、大きさに基づく枝刈りは微調整の内容を反映しにくい [arxiv-2005.07683#c1](https://arxiv.org/pdf/2005.07683v2#page=1 "In transfer learning, weight values are mostly predetermined by the original model and are only ﬁne-tuned on the end task.")。
Movement Pruning は、重みの大きさ(0次の情報)の代わりに、微調整中に**0から離れていく**重みを残す(1次の情報)[arxiv-2005.07683#c2](https://arxiv.org/pdf/2005.07683v2#page=3 "Intuitively, instead of selecting weights that are far from zero, we retain connections that are moving away from zero during the training process.")。
結果は刈る割合によって逆転する。あまり刈らないときは大きさに基づく枝刈りがよく、多く刈るときは Movement Pruning がよかった [arxiv-2005.07683#c6](https://arxiv.org/pdf/2005.07683v2#page=6 "magnitude pruning outperforms all methods with little or no loss with respect to the dense model whereas the performance of movement pruning methods quickly decreases even for low sparsity levels")。著者らは Hugging Face に所属している(カードの notes 参照)。

### 大規模言語モデルの枝刈り

大規模言語モデルでは、再学習をせずに一度で刈る**学習後の枝刈り**が使われる。

- **SparseGPT** は、層ごとに「元の層の出力と、刈った層の出力の2乗誤差」を小さくする問題として扱う。マスクと残りの重みを同時に最適化するのは NP 困難なので近似する [arxiv-2301.00774#c1](https://arxiv.org/pdf/2301.00774v3#page=2 "Thus, exactly solving it for larger layers is unrealistic, leading all existing methods to resort to approximations.")。ヘッセ行列の逆行列の計算を行の間で共有して高速にしている [arxiv-2301.00774#c2](https://arxiv.org/pdf/2301.00774v3#page=3 "The key towards designing an approximation algorithm that is both accurate and efﬁcient lies in enabling the reuse of Hessians between rows with distinct pruning masks.")。較正データは C4 からの128個のテキスト断片で、再学習はしない [arxiv-2301.00774#c4](https://arxiv.org/pdf/2301.00774v3#page=6 "All our experiments are performed in one-shot, without ﬁnetuning, in a similar setup to recent work on post-training quantization of GPT-scale models (Frantar et al., 2022a; Yao et al., 2022; Dettmers et al., 2022).")。著者は大きいモデルほど刈りやすいことを報告し、過剰なパラメータのためだろうと推測している [arxiv-2301.00774#c7](https://arxiv.org/pdf/2301.00774v3#page=7 "In general, there is a clear trend of larger models being easier to sparsify, which we speculate is due to overparametrization.")。
- **Wanda** は、重みの絶対値と、その重みに入る特徴量の大きさ(較正データ上のノルム)の積で重要度を測る [arxiv-2306.11695#c1](https://arxiv.org/pdf/2306.11695v3#page=3 "For each individual weight, we propose to evaluate its importance by the product of its magnitude and the corresponding input feature norm.")。重みは層全体ではなく出力ごとに比べる [arxiv-2306.11695#c2](https://arxiv.org/pdf/2306.11695v3#page=4 "However, we do not observe similar trend in image classification models, suggesting that our observations regarding pruning per output might be unique to LLMs.")。SparseGPT の基準を簡略化すると Wanda の基準の2乗になる、と関係を示している [arxiv-2306.11695#c3](https://arxiv.org/pdf/2306.11695v3#page=4 "The resulting metric in Equation 4 is the square of our proposed metric.")。同じ較正データで比べると、構造的でない枝刈りでは SparseGPT と同程度、構造的な枝刈りでは結果がまちまちだった [arxiv-2306.11695#c4](https://arxiv.org/pdf/2306.11695v3#page=5 "To control this variable factor, we use the exact same set of calibration data as SparseGPT, which consists of 128 sequences with context length size sampled from C4 training set (Raffel et al., 2020).") [arxiv-2306.11695#c5](https://arxiv.org/pdf/2306.11695v3#page=6 "The comparison between Wanda and SparseGPT is mixed for structured sparsity.")。

Wanda の論文は、Zhu と Gupta の「疎な大きいモデル対 密な小さいモデル」の問いを言語モデルで確かめている。構造的でない枝刈りでは疎な大きいモデルがよいことが多かったが、構造的な枝刈りでは逆になった [arxiv-2306.11695#c6](https://arxiv.org/pdf/2306.11695v3#page=6 "For structured sparsity, the trend is reversed: without any fine-tuning, large sparse LLMs have worse zero-shot performance than small dense LLMs in general.")。

### 疎なモデルは速いのか

構造的でない枝刈り(重み単位でばらばらに0にする)は、そのままでは速くならないことが、多くの論文で述べられている。

- Han らは、疎な計算に特化したハードウェアを想定している [arxiv-1506.02626#c8](https://arxiv.org/pdf/1506.02626v3#page=8 "We are targeting our pruning method for ﬁxed-function hardware specialized for sparse DNN, given the limitation of general purpose hardware on sparse computation.")。
- Deep Compression の速度の測定は全結合層だけで、バッチ処理をすると疎の利点は消えた [arxiv-1510.00149#c8](https://arxiv.org/pdf/1510.00149v5#page=10 "In this scenario, pruned network no longer shows its advantage.")。
- Zhu と Gupta は、効率のよい推論には専用のハードウェアが必要で、疎な表現は記憶の余分な負担も増やすと述べている [arxiv-1710.01878#c9](https://arxiv.org/pdf/1710.01878v2#page=2 "The resulting pruned model typically has sparse connection matrices, so efﬁcient inference using these sparse models requires purpose-built hardware capable of loading sparse matrices and/or performing sparse matrix-vector operations") [arxiv-1710.01878#c8](https://arxiv.org/pdf/1710.01878v2#page=9 "In spite of this overhead, large-sparse models appear to achieve higher accuracy than small-dense models with comparable memory footprint.")。
- 宝くじ仮説の論文は、得られた構造は今のライブラリやハードウェア向けに最適化されていないと認めている [arxiv-1803.03635#c8](https://arxiv.org/pdf/1803.03635v5#page=9 "Although we reduce parameter-counts, the resulting architectures are not optimized for modern libraries or hardware.")。
- Movement Pruning の著者は、推論の速さが目的なら、小さい密なモデルのほうがよいことが多いかもしれないと述べている [arxiv-2005.07683#c7](https://arxiv.org/pdf/2005.07683v2#page=6 "We do note though that current hardware does not support optimized inference for sparse models: from an inference speed perspective, it might often desirable to use a small dense model such as mini-BERT over a sparse alternative of the same size.")。
- SparseGPT と Wanda の速度の数値は、層ごとの測定やシミュレーションに基づく [arxiv-2301.00774#c9](https://arxiv.org/pdf/2301.00774v3#page=14 "end-to-end speedups will likely be slightly lower due to some extra overheads from e.g. attention") [arxiv-2306.11695#c7](https://arxiv.org/pdf/2306.11695v3#page=7 "Last, we emphasize that the inference speedup is not unique to our pruning method but is delivered by the inherent power of sparsity for speeding up computation.")。

## 3. 枝刈りの評価の問題

Blalock らは81本の枝刈りの論文を集計し、最も明確な発見は「標準のベンチマークと指標がないこと」だと述べている [arxiv-2003.03033#c1](https://arxiv.org/pdf/2003.03033v1#page=1 "our clearest ﬁnding is that the community suffers from a lack of standardized benchmarks and metrics.")。

- 他の枝刈り手法とまったく比べていない論文や、1つの手法としか比べていない論文が多く、その後どの論文からも比較されていない手法も多い [arxiv-2003.03033#c2](https://arxiv.org/pdf/2003.03033v1#page=1 "For example, a quarter of papers compare to no other pruning method, half of papers compare to at most one other method, and dozens of methods have never been compared to by any subsequent work.")。
- 使われるデータセットと構造の組合せがばらばらで、最も多い組合せでも一部の論文でしか使われていない [arxiv-2003.03033#c3](https://arxiv.org/pdf/2003.03033v1#page=4 "Among 81 papers, we found results using 49 datasets, 132 architectures, and 195 (dataset, architecture) combinations.")。
- 「刈った割合」が残した割合を指すか取り除いた割合を指すかが論文によって違い、FLOPs の数え方もそろっていない [arxiv-2003.03033#c6](https://arxiv.org/pdf/2003.03033v1#page=8 "We found up to a factor of four variation in the reported FLOPs of different papers for the same architecture and dataset")。
- 枝刈り前のモデルの違いだけで、ある手法が別の手法より良く見えることがある [arxiv-2003.03033#c9](https://arxiv.org/pdf/2003.03033v1#page=10 "Even when reporting changes, one pruning method can artiﬁcially appear better than another by virtue of beginning with a different model.")。
- 推奨として、複数のデータセットと構造の組合せ、圧縮率と理論上の速度向上の両方、複数の圧縮の度合いでの結果を報告することを挙げている [arxiv-2003.03033#c7](https://arxiv.org/pdf/2003.03033v1#page=8 "Compression ratio is deﬁned as the original size divided by the new size.")。

著者らは、報告された結果から見ると、枝刈りは同じ構造の効率は改善できるが、よりよい構造に替えるほどの効果はないことが多い、とも示唆している [arxiv-2003.03033#c5](https://arxiv.org/pdf/2003.03033v1#page=4 "Second, it suggests that pruning generally does not help as much as switching to a better architecture.")。
なお、共著者の Frankle は宝くじ仮説の著者でもあり、比較の基盤 ShrinkBench は著者ら自身のライブラリである(カードの notes 参照)。

## 4. 圧縮で何が失われるか

全体の精度が保たれていても、何も失われていないとは限らない。

- Hooker らは、枝刈りしたモデルと元のモデルの予測が、データのごく一部(**PIE**)で食い違うことを示した [arxiv-1911.05248#c1](https://arxiv.org/pdf/1911.05248v3#page=1 "We ﬁnd that models with radically different numbers of weights have comparable top-line performance metrics but diverge considerably in behavior on a narrow subset of the dataset.")。そうした例は人にとっても難しい、ラベルの誤りが多い、まれな例などである [arxiv-1911.05248#c4](https://arxiv.org/pdf/1911.05248v3#page=2 "Compression impairs the model’s ability to predict accurately on the long-tail of less frequent instances.")。刈ったモデルは分布の変化にも弱くなった [arxiv-1911.05248#c6](https://arxiv.org/pdf/1911.05248v3#page=2 "Pruned networks are more sensitive to natural adversarial images and corruptions.")。量子化は、強い枝刈りより不均一な害が少なかった [arxiv-1911.05248#c5](https://arxiv.org/pdf/1911.05248v3#page=6 "While all the techniques we benchmark evidence disparate class level impact, we note that quantization appears to introduce less disparate harm.")。
- 同じ著者らは、顔属性の分類で、圧縮がもともとの偏りを強め、少数の属性の性能を犠牲にして全体の性能を保つことを報告した [arxiv-2010.03058#c1](https://arxiv.org/pdf/2010.03058v2#page=1 "We further establish that for CIE examples, compression ampliﬁes existing algorithmic bias.") [arxiv-2010.03058#c5](https://arxiv.org/pdf/2010.03058v2#page=5 "Compression cannibalizes performance on low-frequency attributes in order to preserve overall performance.")。
- 大規模言語モデルでは、パープレキシティだけで圧縮を評価することが批判されている [arxiv-2310.01382#c1](https://arxiv.org/pdf/2310.01382v2#page=1 "As recent research efforts are focused on developing increasingly sophisticated compression methods, our work takes a step back and re-evaluates the effectiveness of existing SoTA compression methods, which rely on a fairly simple and widely questioned metric, perplexity (even for dense LLMs).")。知識を問うタスクでは枝刈りの失敗が目立ち、量子化のほうがうまくいった [arxiv-2310.01382#c5](https://arxiv.org/pdf/2310.01382v2#page=1 "and fail for N:M sparsity in knowledge-intensive tasks; current quantization methods are more successful than pruning; yet, pruned LLMs even at ≥50% sparsity are robust in-context retrieval and summarization systems")。信頼性の観点でも、量子化は枝刈りより効果的だったと報告されている [arxiv-2403.15447#c1](https://arxiv.org/pdf/2403.15447v3#page=1 "We find that quantization is currently a more effective approach than pruning in achieving efficiency and trustworthiness simultaneously.")。

## 設計への示唆(本記事の整理)

- **蒸留では、先生を大きくすれば良いとは限らない。** 生徒が先生をまねられる範囲かどうかを、生徒の精度とは別に確かめる(上の Cho と Hariharan、Stanton らの結果)。
- **枝刈りは、比較の相手と予算をそろえて読む。** 同じ構造をランダムな初期値から学習した場合 [arxiv-1810.05270#c1](https://arxiv.org/pdf/1810.05270v2#page=1 "For all state-of-the-art structured pruning algorithms we examined, ﬁne-tuning a pruned model only gives comparable or worse performance than training that model with randomly initialized weights.")、同じメモリの小さい密なモデル [arxiv-1710.01878#c1](https://arxiv.org/pdf/1710.01878v2#page=1 "We compare the accuracy of large, but pruned models (large-sparse) and their smaller, but dense (small-dense) counterparts with identical memory footprint.")、同じ計算予算 [arxiv-1810.05270#c2](https://arxiv.org/pdf/1810.05270v2#page=4 "In our experiments, we use Scratch-E to denote training the small pruned models for the same epochs, and Scratch-B to denote training for the same amount of computation budget") と比べているかを確認する。
- **速さが目的なら、構造的でない疎は実際に速くなるかを確かめる。** 多くの論文が、専用のハードウェアや特別な実装なしには速くならないと述べている(2節の最後)。
- **全体の精度以外も測る。** まれな例、部分集団、知識を問うタスク、信頼性で失われるものがある(4節)。

## わかっていないこと

- 蒸留で生徒が先生に一致しない原因は最適化にあると見られているが [arxiv-2106.05945#c8](https://arxiv.org/pdf/2106.05945v2#page=10 "Furthermore, the suboptimal convergence of knowledge distillation appears to be a consequence of the optimization dynamics speciﬁcally, and not simply initialization bias.")、どうすれば一致させられるかは示されていない。
- 宝くじ仮説の当たりくじを、大規模なモデルで安く見つける方法は、ここで扱った論文の範囲では示されていない [arxiv-1803.03635#c7](https://arxiv.org/pdf/1803.03635v5#page=9 "We only consider vision-centric classiﬁcation tasks on smaller datasets (MNIST, CIFAR10).") [arxiv-1912.05671#c8](https://arxiv.org/pdf/1912.05671v4#page=9 "Recent proposals attempt to prune networks at initialization (Lee et al., 2019; Wang et al., 2020), but our results suggest that the best time to do so may be after some training.")。
- 枝刈りの手法どうしを公平に比べる標準のベンチマークは、Blalock らの時点では存在しなかった [arxiv-2003.03033#c1](https://arxiv.org/pdf/2003.03033v1#page=1 "our clearest ﬁnding is that the community suffers from a lack of standardized benchmarks and metrics.")。

## 参照カード

- [arxiv-1503.02531](../../papers/arxiv-1503.02531.yaml) Hinton, Vinyals & Dean, "Distilling the Knowledge in a Neural Network"
- [arxiv-1412.6550](../../papers/arxiv-1412.6550.yaml) Romero et al., "FitNets: Hints for Thin Deep Nets"
- [arxiv-1805.04770](../../papers/arxiv-1805.04770.yaml) Furlanello et al., "Born Again Neural Networks"
- [arxiv-1910.01108](../../papers/arxiv-1910.01108.yaml) Sanh et al., "DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter"
- [arxiv-1910.01348](../../papers/arxiv-1910.01348.yaml) Cho & Hariharan, "On the Efficacy of Knowledge Distillation"
- [arxiv-2106.05945](../../papers/arxiv-2106.05945.yaml) Stanton et al., "Does Knowledge Distillation Really Work?"
- [arxiv-1506.02626](../../papers/arxiv-1506.02626.yaml) Han et al., "Learning both Weights and Connections for Efficient Neural Networks"
- [arxiv-1510.00149](../../papers/arxiv-1510.00149.yaml) Han, Mao & Dally, "Deep Compression"
- [arxiv-1710.01878](../../papers/arxiv-1710.01878.yaml) Zhu & Gupta, "To prune, or not to prune"
- [arxiv-1810.02340](../../papers/arxiv-1810.02340.yaml) Lee, Ajanthan & Torr, "SNIP: Single-shot Network Pruning based on Connection Sensitivity"
- [arxiv-1803.03635](../../papers/arxiv-1803.03635.yaml) Frankle & Carbin, "The Lottery Ticket Hypothesis"
- [arxiv-1912.05671](../../papers/arxiv-1912.05671.yaml) Frankle et al., "Linear Mode Connectivity and the Lottery Ticket Hypothesis"
- [arxiv-1810.05270](../../papers/arxiv-1810.05270.yaml) Liu et al., "Rethinking the Value of Network Pruning"
- [arxiv-2005.07683](../../papers/arxiv-2005.07683.yaml) Sanh, Wolf & Rush, "Movement Pruning: Adaptive Sparsity by Fine-Tuning"
- [arxiv-2301.00774](../../papers/arxiv-2301.00774.yaml) Frantar & Alistarh, "SparseGPT"
- [arxiv-2306.11695](../../papers/arxiv-2306.11695.yaml) Sun et al., "A Simple and Effective Pruning Approach for Large Language Models"
- [arxiv-2003.03033](../../papers/arxiv-2003.03033.yaml) Blalock et al., "What is the State of Neural Network Pruning?"
- [arxiv-1911.05248](../../papers/arxiv-1911.05248.yaml) Hooker et al., "What Do Compressed Deep Neural Networks Forget?"
- [arxiv-2010.03058](../../papers/arxiv-2010.03058.yaml) Hooker et al., "Characterising Bias in Compressed Models"
- [arxiv-2310.01382](../../papers/arxiv-2310.01382.yaml) Jaiswal et al., "Compressing LLMs: The Truth is Rarely Pure and Never Simple"
- [arxiv-2403.15447](../../papers/arxiv-2403.15447.yaml) Hong et al., "Decoding Compressed Trust"
