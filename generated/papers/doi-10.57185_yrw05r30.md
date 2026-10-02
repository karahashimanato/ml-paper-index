<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Penerapan Deep Learning (Artificial Neural Network) Untuk Klasifikasi Diagnostik Kanker Payudara Guna Mendukung Efisiensi Biaya Deteksi Dini

- カード: [`doi-10.57185_yrw05r30`](../../papers/doi-10.57185_yrw05r30.yaml)
- 著者: Zeny Widianingsih, Aldi Algino
- 年・掲載: 2026 Al Makki Health Informatics Journal
- 原論文: [PDF](https://healthinformaticsjournal.al-makkipublisher.com/index.php/hij/article/download/99/85)(Publisher PDF via OpenAlex (publishedVersion)、カード作成時に読んだ版)
- タグ: kernel-methods, linear-models, random-forests, supervised, tabular-classification, tabular-mlp
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The study designs and evaluates an MLP-based neural network to classify breast tumors as benign or malignant.([Abstract (English), p.1](https://healthinformaticsjournal.al-makkipublisher.com/index.php/hij/article/download/99/85#page=1 "This study aims to design and evaluate a deep learning model based on an Artificial Neural Network (Multi-Layer Perceptron) to classify breast tumors as either benign or malignant."))
- **c2** Data are the WDBC dataset (569 samples, 30 numerical features), with a stratified 80:20 train-test split.([Abstract (English), p.1](https://healthinformaticsjournal.al-makkipublisher.com/index.php/hij/article/download/99/85#page=1 "The study utilized the Wisconsin Diagnostic Breast Cancer (WDBC) dataset, comprising 569 samples and 30 numerical features, split into 455 training samples and 114 test samples (80:20) using a stratified approach."))
- **c3** The neural network did not outperform classical models (logistic regression, random forest, SVM) on this small tabular dataset.([Abstract (English), p.1](https://healthinformaticsjournal.al-makkipublisher.com/index.php/hij/article/download/99/85#page=1 "These findings indicate that the Deep Neural Network model does not outperform classical models on small-scale tabular data."))
- **c4** The MLP uses scikit-learn MLPClassifier defaults except the stated architecture, Adam, early stopping on a 15% validation split and the random seed.([Methods, p.6](https://healthinformaticsjournal.al-makkipublisher.com/index.php/hij/article/download/99/85#page=6 "regularisasi L2 (alpha) mengikuti nilai bawaan (default) MLPClassifier scikit-learn kecuali yang telah disebutkan secara eksplisit."))
- **c5** Evaluation uses a single 80:20 hold-out split, not k-fold cross-validation.([Methods, p.6](https://healthinformaticsjournal.al-makkipublisher.com/index.php/hij/article/download/99/85#page=6 "Perlu ditegaskan bahwa evaluasi pada penelitian ini menggunakan satu kali pembagian data latih-uji (single hold-out split 80:20), bukan validasi silang k-lipat (k-fold cross-validation)."))
- **c6** With 114 test samples, accuracy differences of about one percent correspond to about one sample, so the model ranking is not statistically reliable without further testing.([Methods, p.6](https://healthinformaticsjournal.al-makkipublisher.com/index.php/hij/article/download/99/85#page=6 "sehingga peringkat antar-model tidak dapat dianggap andal secara statistik tanpa pengujian tambahan."))

