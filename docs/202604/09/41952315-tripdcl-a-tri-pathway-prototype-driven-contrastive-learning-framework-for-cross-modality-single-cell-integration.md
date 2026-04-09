---
title: "TriPDCL: A Tri-Pathway Prototype-Driven Contrastive Learning Framework for Cross-Modality Single-Cell Integration."
title_zh: TriPDCL：一种用于跨模态单细胞整合的三通路原型驱动对比学习框架
authors: "Xiaoyun Xiong, Chengdong Zhang, Fengnan Yang, Shaoqing Wang, Yuanyuan Zhang"
date: 2026-04-08
pdf: "https://pubmed.ncbi.nlm.nih.gov/41952315/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 用于跨模态单细胞整合的对比学习框架
tldr: 单细胞多组学集成面临数据稀疏和细胞异质性对齐的挑战。TriPDCL 提出了一种三通路原型驱动的对比学习框架，通过可学习的原型中心和迭代更新机制，在潜在空间中精确构建正负样本对，从而有效对齐跨模态的异质性信息。在五个数据集上的实验表明，该方法在消除批次效应和保留生物学特征方面优于现有主流方法，为统一的多组学表征学习提供了新方案。
selection_source: fresh_fetch
motivation: 针对单细胞多组学数据中高稀疏性和显著的细胞异质性导致跨模态对齐困难的问题。
method: 提出一种基于原型的对比学习框架，利用可学习的原型中心和迭代更新机制来构建可靠的正负样本对并传递异质性信息。
result: 在五个基准数据集上与七种代表性方法对比，证明了该框架在跨模态集成和下游分析任务中的优越性。
conclusion: 该研究通过原型驱动的对比学习有效解决了多组学分析中的异质性对齐和鲁棒学习难题。
---

## 摘要
单细胞测序技术的飞速发展为多组学数据整合奠定了坚实基础。多组学整合的一个核心目标是减弱源于技术批次效应和固有生物学变异的跨组学差异，从而促进统一潜在表示的生成，以支持稳健的下游分析。然而，单细胞数据固有的高稀疏性和显著的细胞间异质性为联合分析带来了巨大挑战。我们重点关注细胞异质性，并提出了 TriPDCL，这是一种基于原型的对比学习框架。该框架不仅通过迭代原型学习更新机制实现了异质性信息的有效传递，还利用可学习的原型中心实现了可靠正负样本对的精确构建。它解决了多组学分析中的两个主要挑战：跨模态异质性的对齐和稳健学习。随后，在五个数据集上与七种代表性方法进行的对比评估证明了所提方法的优越性。

## Abstract
The rapid development of single-cell sequencing technologies has laid a solid foundation for multiomics data integration. A central objective in multiomics integration is to attenuate cross-omic discrepancies stemming from technical batch effects and inherent biological variability, thereby facilitating a unified latent representation that supports robust downstream analyses. However, the intrinsic high sparsity of single-cell data and pronounced intercellular heterogeneity pose greater challenges for joint analysis. We foreground cellular heterogeneity and present TriPDCL, a prototype-based contrastive learning framework, which not only achieves effective transfer of heterogeneity information through an iterative prototype-learning update mechanism but also, by leveraging learnable prototype centers, enables precise construction of reliable positive-negative sample pairs. It tackles two principal challenges, the alignment of cross-modal heterogeneity and the robust learning, in multiomics analysis. Subsequently, comparative assessments conducted on five data sets in contrast to seven representative methods illustrate the superiority of the proposed approach.