---
title: "PhaGCN_Cluster: A Scalable and Robust Framework for Automated Classification and Discovery of Viral Dark Matter from Metagenomes."
title_zh: PhaGCN_Cluster：一个用于宏基因组中病毒暗物质自动分类与发现的可扩展且稳健的框架
authors: "Hao-Long Xia, Pei-Yu Liang, Wen-Guang Yuan, Xu-Dong Cao, Yanni Sun, Jing-Zhe Jiang, Li-Hong Yuan"
date: 2026-03-17
pdf: "https://pubmed.ncbi.nlm.nih.gov/41843252/"
tags: ["query:pathoai"]
score: 10.0
evidence: 用于宏基因组病毒分类的图卷积神经网络
tldr: 针对宏基因组中大量难以通过传统方法分类的病毒“暗物质”，本研究开发了 PhaGCN_Cluster 框架。该工具利用图卷积网络（GCN）整合蛋白质序列相似性和基因组特征，构建了可扩展的知识图谱分析系统。实验证明，它在处理低相似度序列时具有极高的准确率和鲁棒性，单次可处理 30 万条序列，为发现新病毒演化分支和自动化分类提供了高效、可解释的解决方案。
selection_source: fresh_fetch
motivation: 传统的病毒分类方法难以识别宏基因组中序列差异巨大的“病毒暗物质”，且在大规模数据处理上存在效率瓶颈。
method: 该框架通过图卷积网络（GCN）融合蛋白质层面的相似性与基因组层面的特征，构建了一个支持大规模并发处理的病毒知识图谱系统。
result: 相比现有工具，该方法在低序列相似度下表现出更强的分类准确性，并能通过新增的“类（_like）”分类逻辑有效识别未知病毒类群。
conclusion: PhaGCN_Cluster 为病毒多样性研究提供了一个兼具高扩展性、鲁棒性和解释性的自动化分类平台，有助于填补病毒进化树中的空白。
---

## 摘要
病毒是地球上数量最丰富的生物实体，在塑造微生物群落、驱动进化和维持生态系统功能方面发挥着至关重要的作用。宏基因组测序揭示了大量未表征的病毒“暗物质”，这些物质由高度分化的序列组成，避开了传统的分类学方法。在这里，我们开发了 PhaGCN_Cluster，这是一种基于图卷积神经网络（GCN）框架的下一代病毒分类工具。通过整合蛋白质水平的序列相似性和 contig 水平的基因组特征，PhaGCN_Cluster 建立了一个可扩展的基于知识图谱的分析系统。优化后的算法在计算效率上取得了显著提升，支持单次运行对多达 300,000 个 contig 进行准确的分类学分配。与现有方法相比，PhaGCN_Cluster 表现出卓越的分类准确率和 F1 分数，特别是在低序列相似度的情况下，并在检测进化距离较远的病毒方面表现出强大的鲁棒性。值得注意的是，PhaGCN_Cluster 整合了分配“_like”分类单元的更新逻辑，这增强了其容纳新型病毒群的能力，同时保持了高精度——尽管以召回率略微下降为代价。通过生成高保真网络图，PhaGCN_Cluster 揭示了以前未被识别的进化支系，并弥合了参考病毒与新序列之间的进化鸿沟，从而为病毒多样性和进化提供了关键见解。PhaGCN_Cluster 代表了一种用于自动病毒分类的可解释、高效且可扩展的解决方案。PhaGCN_Cluster 的源代码可通过 https://github.com/xiahaolong/PhaGCN_Cluster 获取。

## Abstract
Viruses are the most abundant biological entities on Earth, playing essential roles in shaping microbial communities, driving evolution, and maintaining ecosystem functions. Metagenomic sequencing has unveiled a vast landscape of uncharacterized viral "dark matter", comprising highly divergent sequences that elude traditional taxonomic approaches. Here, we develop PhaGCN_Cluster, a next-generation viral classification tool built upon a graph convolutional neural network (GCN) framework. By integrating protein-level sequence similarity and contig-level genomic features, PhaGCN_Cluster establishes a scalable knowledge graph-based analytical system. The optimized algorithm yields significant gains in computational efficiency, supporting accurate taxonomic assignment of up to 300,000 contigs per run. Compared with existing methods, PhaGCN_Cluster demonstrates superior classification accuracy and F1-scores, particularly under conditions of low sequence similarity, and exhibits strong robustness in detecting evolutionarily distant viruses. Notably, PhaGCN_Cluster incorporates an updated logic for assigning "_like" taxa, which enhances its capacity to accommodate novel viral groups while preserving high precision-though at the cost of a slight reduction in recall. By generating high-fidelity network graphs, PhaGCN_Cluster uncovers previously unrecognized clades and bridges evolutionary gaps between reference viruses and novel sequences, thereby providing critical insights into viral diversity and evolution. PhaGCN_Cluster represents an interpretable, efficient, and scalable solution for automated virus classification. The source code of PhaGCN_Cluster is available via https://github.com/xiahaolong/PhaGCN_Cluster .