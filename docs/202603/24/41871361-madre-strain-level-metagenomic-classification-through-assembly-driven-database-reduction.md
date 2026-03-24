---
title: "MADRe: Strain-level Metagenomic Classification Through Assembly-Driven Database Reduction."
title_zh: MADRe：通过组装驱动的数据库缩减实现菌株级宏基因组分类
authors: "Lipovac J, Šikić M, Vicedomini R, Križanović K., Josipa Lipovac, Mile Šikić, Riccardo Vicedomini, Krešimir Križanović"
date: 2026-03-23
pdf: "https://pubmed.ncbi.nlm.nih.gov/41871361/"
tags: ["query:seqai"]
score: 10.0
evidence: 菌株级宏基因组分类与组装
tldr: 针对宏基因组分析中菌株级分类受限于参考数据库冗余和样本组成未知的问题，MADRe 提出了一种基于组装驱动的数据库缩减策略。该方法通过长读段组装获取基因组上下文，利用期望最大化（EM）框架将组装结果映射回参考库以精简数据库，最后在缩减后的库上进行概率化读段重分配。实验证明，MADRe 在模拟和真实数据中均能显著降低假阳性，提升了菌株识别的精确度。
selection_source: fresh_fetch
motivation: 现有的菌株级分类方法在面对庞大且冗余的参考数据库时，容易产生大量假阳性结果，难以准确识别未知样本中的特定菌株。
method: 该工具结合了长读段组装技术与 EM 统计框架，先通过组装序列筛选出最相关的参考基因组以缩小搜索范围，再对原始读段进行概率化比对。
result: 在模拟数据集和真实厌氧消化池样本的测试中，MADRe 显著减少了错误检测的菌株数量，在保持灵敏度的同时大幅提升了分类精确度。
conclusion: MADRe 为长读段宏基因组研究提供了一个模块化且可扩展的解决方案，通过“先组装后缩减”的策略有效解决了大规模数据库带来的分类噪音问题。
---

## 摘要
菌株级宏基因组分类对于理解微生物多样性和功能潜力至关重要，但在样本组成未知且参考数据库庞大且冗余的情况下，这仍然具有挑战性。在此，我们介绍了 MADRe，这是一个基于宏基因组组装驱动数据库缩减（Metagenome Assembly-Driven Database Reduction）的模块化且可扩展的长读长菌株级宏基因组分类流水线。除了系统级集成外，MADRe 还引入了统计策略，利用源自组装的基因组背景来指导数据库缩减和概率性 read 重新分配。具体而言，它结合了长读长宏基因组组装、使用期望最大化框架进行参考缩减的 contig 到参考序列重新分配，以及在缩减后的数据库上进行概率性 read 比对重新分配，从而实现灵敏且精确的菌株级分类。我们在模拟数据集、模拟群落和真实的厌氧消化池污泥宏基因组上对 MADRe 进行了广泛评估。在不同的相似度和覆盖度条件下，MADRe 通过减少假阳性菌株检测，一致地提高了精确度。MADRe 的设计允许用户单独应用数据库缩减或 read 分类步骤。仅使用 read 分类步骤的结果与其他测试工具相当。MADRe 是开源的，可在 https://github.com/lbcb-sci/MADRe 公开获取。

## Abstract
Strain-level metagenomic classification is essential for understanding microbial diversity and functional potential, yet remains challenging, particularly when sample composition is unknown and reference databases are large and redundant. Here we present MADRe, a modular and scalable pipeline for long-read strain-level metagenomic classification based on Metagenome Assembly-Driven Database Reduction. Beyond system-level integration, MADRe introduces statistical strategies that leverage assembly-derived genomic context to guide database reduction and probabilistic read reassignment. Specifically, it combines long-read metagenome assembly, contig-to-reference reassignment using an expectation-maximization framework for reference reduction, and probabilistic read mapping reassignment on a reduced database to achieve sensitive and precise strain-level classification. We extensively evaluated MADRe on simulated datasets, mock communities, and a real anaerobic digester sludge metagenome. Across diverse similarity and coverage conditions, MADRe consistently improves precision by reducing false-positive strain detections. MADRe's design allows users to apply either the database reduction or read classification step individually. Using only the read classification step shows results on par with other tested tools. MADRe is open source and publicly available at https://github.com/lbcb-sci/MADRe.