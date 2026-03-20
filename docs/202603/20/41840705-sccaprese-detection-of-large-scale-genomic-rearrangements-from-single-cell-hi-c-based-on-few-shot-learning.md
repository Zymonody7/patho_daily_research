---
title: "scCAPReSE: detection of large-scale genomic rearrangements from single-cell Hi-C based on few-shot learning."
title_zh: scCAPReSE：基于少样本学习的单细胞 Hi-C 大规模基因组重排检测
authors: "Kim K, Lee CH, Jung I."
date: 2026-03-16
pdf: "https://pubmed.ncbi.nlm.nih.gov/41840705/"
tags: ["query:seqai"]
score: 9.0
evidence: 从单细胞Hi-C中检测基因组重排
tldr: "针对单细胞Hi-C数据中由于训练样本稀缺导致难以检测大规模基因组重排（SV）的问题，scCAPReSE 引入了基于 CLIP 预训练模型的少样本学习框架。该方法通过迁移视觉基础模型的特征表示，仅需少量标注样本即可在不同测序平台的数据上实现高精度分类。实验证明其在 sci-Hi-C 数据集上准确率超 90%，并能揭示癌细胞间 3D 基因组结构的异质性，为研究癌症克隆演化提供了高效工具。"
selection_source: fresh_fetch
motivation: 癌症基因组重排会改变 3D 染色质结构，但单细胞 Hi-C 数据存在标准化程度低且标注样本极少的问题，限制了传统深度学习模型的应用。
method: 采用基于 CLIP 视觉基础模型的少样本学习框架，通过提取并微调预训练权重，将 3D 染色质接触图的结构变异识别转化为图像分类任务。
result: "在 sci-Hi-C 数据集上达到 90% 以上的分类准确率，并成功在 K562 细胞系中识别出费城染色体易位及其在细胞间的异质性分布。"
conclusion: scCAPReSE 证明了利用通用视觉基础模型进行少样本迁移学习，可以有效解决单细胞组学数据稀疏且标注困难的挑战。
---

## 摘要
大规模基因组重排在癌症基因组中普遍存在，并能深刻地重塑三维（3D）基因组结构，通过增强子劫持导致异常的癌基因激活。重塑后的 3D 组织会产生独特的染色质接触特征，这些特征可以通过基于深度学习的方法进行检测。然而，将此类分析扩展到单细胞分辨率（这对于描绘癌症的克隆异质性至关重要）仍然是一项重大挑战，原因在于单细胞 Hi-C 技术尚未标准化，且不同方法可用的数据集有限，导致训练集数量不足。在此，我们介绍了 scCAPReSE，这是一个基于少样本学习的框架，它采用了预训练图像基础模型 CLIP 的表示，以实现对单细胞 Hi-C 数据中结构变异（SV）模式的稳健分类。通过从基础模型中提取并微调基础权重，scCAPReSE 仅使用来自单一癌症细胞系的几百个大规模 SV 样本，即可实现深度学习分类器的有效训练，同时使分类任务适应异质的单细胞 Hi-C 库。在 sci-Hi-C 数据集上的评估显示，scCAPReSE 实现了超过 90% 的分类准确率。当进一步应用于 K562 慢性髓系白血病细胞系的 scNanoHi-C 数据时，scCAPReSE 不仅正确识别了费城染色体易位，还揭示了 SV 介导的染色质相互作用贡献中显著的细胞间差异，突显了癌症 3D 基因组组织中此前无法触及的异质性。总之，scCAPReSE 为在单细胞分辨率下检测 SV 驱动的 3D 基因组重组提供了一个广泛适用且数据高效的框架，能够对癌症特异性染色质结构和克隆异质性进行定量剖析。该方法可在 https://github.com/kaistcbfg/CAPReSE 免费获取。

## Abstract
Large-scale genomic rearrangements are prevalent in cancer genomes and can profoundly rewire three-dimensional (3D) genome architecture, leading to aberrant oncogene activation through enhancer hijacking. The rewired 3D organization generates unique chromatin contact signatures, which can be detected using deep learning-based approaches. However, extending such analyses to single-cell resolution, which is critical to delineate clonal heterogeneity in cancer, remains a major challenge, due to the limited number of training sets as single-cell Hi-C techniques are not standardized and only limited datasets are available across different methods. Here, we introduce scCAPReSE, a few-shot learning-based framework that adopts representations from a pre-trained image foundation model, CLIP, to enable robust classification of structural variation (SV) patterns in single-cell Hi-C data. By extracting and fine-tuning base weights from the foundation model, scCAPReSE enables effective training of deep learning classifiers using only a few hundred large-scale SV examples derived from a single cancer cell line while adapting classification tasks to heterogeneous single-cell Hi-C libraries. scCAPReSE achieved over 90% classification accuracy when evaluated on sci-Hi-C datasets. When further applied to scNanoHi-C data from the K562 chronic myeloid leukemia cell line, scCAPReSE correctly identified the Philadelphia chromosome translocation but also revealed substantial cell-to-cell variability in the contribution of SV-mediated chromatin interactions, highlighting previously inaccessible heterogeneity in cancer 3D genome organization. In summary, scCAPReSE provides a broadly applicable and data-efficient framework for detecting SV-driven 3D genome reorganization at single-cell resolution, enabling quantitative dissection of cancer-specific chromatin architecture and clonal heterogeneity. The developed method is freely available at https://github.com/kaistcbfg/CAPReSE.