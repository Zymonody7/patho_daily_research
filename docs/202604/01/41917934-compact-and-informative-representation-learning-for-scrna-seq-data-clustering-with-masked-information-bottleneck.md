---
title: Compact and informative representation learning for scRNA-seq data clustering with masked information bottleneck.
title_zh: 基于掩码信息瓶颈的单细胞RNA测序数据聚类紧凑且信息丰富的表示学习
authors: "Xiaoqiang Yan, Fengshou Han, Yunpeng Wu, Zhen Tian"
date: 2026-03-31
pdf: "https://pubmed.ncbi.nlm.nih.gov/41917934/"
tags: ["query:seqai"]
score: 9.0
evidence: 单细胞RNA测序数据的表示学习与聚类
tldr: 针对单细胞转录组测序（scRNA-seq）数据中存在的高稀疏、高噪声和信息冗余导致细胞聚类困难的问题，本研究提出了scMIB框架。该方法通过掩码去噪策略扰动基因表达以抑制噪声，并引入信息瓶颈（IB）目标来压缩冗余信号，从而提取最具代表性的特征。实验结果表明，scMIB在多个公开数据集上显著提升了聚类准确性和鲁棒性，为识别复杂生物系统中的细胞异质性提供了更可靠的工具。
selection_source: fresh_fetch
motivation: 旨在解决单细胞测序数据中由于高噪声、稀疏性和基因冗余导致的细胞类型识别不准确问题。
method: 构建了一个结合掩码去噪、信息瓶颈优化和掩码一致性学习的表示学习框架，通过扰动恢复和信息压缩提取关键生物信号。
result: 在多个公共数据集上的测试证明，该方法在聚类精度上优于现有技术，并能有效抵御数据噪声和稀疏性的干扰。
conclusion: 证明了将掩码扰动与信息瓶颈理论相结合是提取单细胞数据稳健表示、提升细胞异质性分析可靠性的有效策略。
---

## 摘要
背景：单细胞RNA测序（scRNA-seq）为表征细胞异质性提供了前所未有的机遇。然而，基因表达数据中固有的高稀疏性、噪声和冗余往往会掩盖具有生物学意义的信号，并阻碍准确的细胞聚类。尽管高变基因常被用于降维，但它们仍可能包含冗余或噪声信息，从而降低聚类性能。结果：在此，我们提出了 scMIB，一种用于单细胞RNA测序数据鲁棒表示学习的掩码信息瓶颈框架。该方法引入了一种基于掩码的去噪策略，通过扰动基因表达模式并训练模型在抑制噪声的同时恢复信息结构。通过整合信息瓶颈目标，scMIB 进一步压缩冗余信号并保留与聚类最相关的信息。此外，采用掩码一致性学习机制来对齐真实掩码和预测掩码，促使模型捕捉稳定的基因级模式。在多个公开 scRNA-seq 数据集上的广泛实验表明，与现有方法相比，scMIB 一致地提高了聚类准确性和鲁棒性，同时有效减轻了噪声和稀疏性的影响。结论：我们的结果表明，将基于掩码的扰动与信息瓶颈学习相结合，为从噪声单细胞转录组数据中提取信息丰富的表示提供了一种有效策略。所提出的框架为 scRNA-seq 聚类提供了一种鲁棒的解决方案，并可能有助于在复杂生物系统中更可靠地识别细胞异质性。

## Abstract
BACKGROUND: Single-cell RNA sequencing (scRNA-seq) provides unprecedented opportunities to characterize cellular heterogeneity. However, the high sparsity, noise, and redundancy inherent in gene expression data often obscure biologically meaningful signals and hinder accurate cell clustering. Although highly variable genes are commonly used to reduce dimensionality, they may still contain redundant or noisy information that degrades clustering performance. RESULTS: Here, we propose scMIB, a masked information bottleneck framework for robust representation learning in scRNA-seq data. The method introduces a masking-based denoising strategy that perturbs gene expression patterns and trains the model to recover informative structures while suppressing noise. By integrating an information bottleneck objective, scMIB further compresses redundant signals and preserves the most relevant information for clustering. In addition, a mask consistency learning mechanism is employed to align real and predicted masks, encouraging the model to capture stable gene-level patterns. Extensive experiments on multiple public scRNA-seq datasets demonstrate that scMIB consistently improves clustering accuracy and robustness compared with existing methods, while effectively mitigating the influence of noise and sparsity. CONCLUSIONS: Our results show that combining masking-based perturbation with information bottleneck learning provides an effective strategy for extracting informative representations from noisy single-cell transcriptomic data. The proposed framework offers a robust solution for scRNA-seq clustering and may facilitate more reliable identification of cellular heterogeneity in complex biological systems.