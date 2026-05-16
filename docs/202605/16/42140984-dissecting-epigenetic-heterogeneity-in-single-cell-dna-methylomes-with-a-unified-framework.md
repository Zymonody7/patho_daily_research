---
title: Dissecting epigenetic heterogeneity in single-cell DNA methylomes with a unified framework.
title_zh: 利用统一框架剖析单细胞DNA甲基化组中的表观遗传异质性
authors: "Songming Tang, Siyu Li, Guangxin Zhang, Aoran Lyu, Han Li, Shengquan Chen"
date: 2026-05-15
pdf: "https://pubmed.ncbi.nlm.nih.gov/42140984/"
tags: ["query:seqai"]
score: 8.0
evidence: 单细胞DNA甲基化测序数据分析工具包
tldr: 针对单细胞DNA甲基化数据存在的大量缺失值和分布特殊性，现有分析工具适配性不足。本研究开发了scMethCraft框架，通过混合神经网络融合基因组序列与位置特征，并迭代优化细胞关联建模。该工具不仅提升了细胞分群和信号增强的准确性，还成功识别出新型细胞特异性基因，为探索表观遗传异质性提供了系统性的技术支撑。
selection_source: fresh_fetch
motivation: 现有的单细胞DNA甲基化分析方法多套用scRNA-seq框架，难以处理该数据特有的高缺失率和独特的分布模式。
method: 提出scMethCraft工具包，利用混合神经网络整合基因组序列特征与位置信息，并通过迭代量化细胞间关联来建模甲基化数据。
result: 该框架在细胞嵌入、多源数据集成及差异甲基化区域识别等任务上表现优异，并发现了数据库中未记载的少突胶质细胞相关基因。
conclusion: scMethCraft为单细胞分辨率下的表观遗传异质性研究提供了统一且高效的分析平台，有助于揭示深层的生物学机制。
---

## 摘要
单细胞DNA甲基化（scDNAm）测序为剖析表观遗传异质性和基因调控机制提供了前所未有的机遇。然而，大多数现有的分析方法是基于传统的单细胞测序框架（如单细胞RNA测序）改编而来的，未能考虑到scDNAm数据的独特特征，包括广泛存在的显式缺失值及其独特的分布模式。为了在单细胞分辨率下系统地探索由DNA甲基化引起的表观遗传变异，我们提出了scMethCraft，一个多功能的分析工具包。scMethCraft通过混合神经网络整合了多视角的基因组序列特征和甲基化区域的位置信息，并迭代量化细胞间的关联，从而实现了对scDNAm数据的准确建模。scMethCraft有助于准确重建DNA甲基化图谱，并支持一系列下游分析，包括细胞嵌入、多源数据整合、细胞类型注释、表观遗传信号增强以及差异甲基化区域的识别，从而显著促进了对scDNAm异质性的鉴定和表征。将scMethCraft与互补的分析工作流（包括生物功能富集、组织特异性表达分析和分区遗传力评估）相结合，能够发现特定细胞亚群的生物学见解。此外，scMethCraft识别出了在现有数据库中尚未得到充分表征的少突胶质细胞相关基因，为研究潜在的生物学机制提供了表观遗传学视角。

## Abstract
Single-cell DNA methylation (scDNAm) sequencing offers unprecedented opportunities for dissecting epigenetic heterogeneity and gene regulatory mechanisms. However, most existing analytical methods are adapted from conventional single-cell sequencing frameworks, such as single-cell RNA sequencing, and fail to account for the unique characteristics of scDNAm data, including the widespread presence of explicit missing values and their distinct distribution patterns. To enable systematic exploration of DNA methylation-derived epigenetic variation at single-cell resolution, we propose scMethCraft, a versatile analytical toolkit. scMethCraft integrates multi-perspective genomic sequence features and position information of methylated regions via a hybrid neural network, and iteratively quantifies the cell-to-cell associations, enabling accurate modeling of scDNAm data. scMethCraft facilitates accurate reconstruction of DNA methylation landscapes and supports a spectrum of downstream analyses, including cell embedding, multi-source data integration, cell type annotation, epigenetic signal enhancement, and identification of differentially methylated regions, thereby significantly facilitating the identification and characterization of scDNAm heterogeneity. The integration of scMethCraft with complementary analytical workflows, including biological function enrichment, tissue-specific expression analysis, and partitioned heritability assessment, enables the discovery of biological insights into specific cellular subpopulations. Furthermore, scMethCraft identified oligodendrocyte-associated genes that are not well characterized in existing databases, providing an epigenetic perspective for investigating underlying biological mechanisms.