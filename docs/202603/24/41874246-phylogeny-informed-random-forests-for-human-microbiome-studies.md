---
title: Phylogeny-informed random forests for human microbiome studies.
title_zh: 结合系统发育信息的人类微生物组研究随机森林算法
authors: Hyunwook Koh
date: 2026-03-24
pdf: "https://pubmed.ncbi.nlm.nih.gov/41874246/"
tags: ["query:seqai"]
score: 9.0
evidence: 引入一种结合系统发育信息的随机森林算法用于微生物组数据分析
tldr: 人类微生物组数据具有高度偏态和离散特征，且微生物间存在进化亲缘关系。传统随机森林忽略了这种系统发育树信息。PIRF（系统发育知情随机森林）通过在系统发育簇内局部筛选特征，增强了功能表示并降低了决策树间的相关性。在牙龈炎症、免疫治疗反应及年龄预测等七项基准任务中，PIRF 的预测准确率优于现有工具，为微生物组疾病诊断提供了更精准的建模方案。
selection_source: fresh_fetch
motivation: 传统的随机森林算法在处理微生物组数据时，未能有效利用反映微生物进化亲缘和功能相关性的系统发育树信息。
method: PIRF 改变了特征选择机制，不再进行全局竞争，而是在每个系统发育簇（局部进化组）内识别信息特征，以丰富功能表达并减少模型冗余。
result: 在包括肥胖、糖尿病分类及年龄回归在内的七个真实世界基准测试中，PIRF 的预测性能均超过了通用的机器学习工具。
conclusion: PIRF 证明了将生物学先验知识（如系统发育关系）整合进集成学习算法中，能显著提升微生物组临床研究的预测精度。
---

## 摘要
随机森林是一种广泛使用的基于树的集成学习算法，能够高效捕捉复杂的非线性关系和高阶特征交互，且无需满足分布假设。它也非常适用于人类微生物组研究，此类研究中的数据具有高度偏态、过度离散、离散且不规则的特点。在本文中，我特别关注反映微生物特征间进化祖先和功能相关性的系统发育树信息。将系统发育树信息适当地整合到微生物组数据分析中，已提供了新的见解并提升了分析性能。在本文中，我介绍了一种整合了系统发育树信息的随机森林算法扩展，命名为系统发育引导随机森林（Phylogeny-Informed Random Forests, PIRF），旨在提高人类微生物组研究中的预测准确性。PIRF 的核心机制在于其局部化方法；PIRF 并非将所有特征视为在全局范围内竞争被选择或加权，而是在每个系统发育簇（即在进化和功能上相关的局部微生物特征组）内识别信息特征，从而在丰富功能表征的同时降低树与树之间的相关性。通过七个基准任务，我展示了 PIRF 与其他现成工具相比具有更高的预测准确性：包括四个分类问题（牙龈炎症、免疫治疗反应、1 型糖尿病和肥胖）和三个回归问题（细胞因子水平、基于口腔微生物组的年龄以及基于肠道微生物组的年龄）。重要性：PIRF 是随机森林算法的一种扩展，它结合了系统发育树信息以提高人类微生物组研究中的预测准确性。PIRF 可作为基于微生物组的疾病诊断和个性化医疗的有用工具。该软件和教程以名为 PIRF 的 R 包形式在 https://github.com/hk1785/PIRF 免费提供。

## Abstract
UNLABELLED: Random Forest is a widely used tree-based ensemble learning algorithm that efficiently captures complex nonlinear relationships and higher-order feature interactions with no distributional assumptions to be satisfied. It is also well-suited to human microbiome studies, where the data are highly skewed, overdispersed, discrete, and irregular. Here, I pay particular attention to the phylogenetic tree information that reflects evolutionary ancestry and functional relatedness among microbial features. Proper incorporation of phylogenetic tree information into microbiome data analysis has provided new insights and improved analytical performance. In this paper, I introduce an extension of the Random Forest algorithm that incorporates phylogenetic tree information, named Phylogeny-Informed Random Forests (PIRF), to improve predictive accuracy in human microbiome studies. The core mechanism of PIRF lies in its localized approach; rather than treating all features as competing globally to be selected or weighted, PIRF identifies informative features within each phylogenetic cluster (i.e., a localized group of microbial features that are evolutionarily and functionally related), thereby enriching functional representations while reducing tree-to-tree correlation. I demonstrate the high predictive accuracy of PIRF, compared with other off-the-shelf tools, across seven benchmark tasks: four classification problems (gingival inflammation, immunotherapy response, type 1 diabetes, and obesity) and three regression problems (cytokine level, age based on oral microbiome, and age based on gut microbiome). IMPORTANCE: PIRF is an extension of the Random Forest algorithm that incorporates phylogenetic tree information to improve predictive accuracy in human microbiome studies. PIRF can serve as a useful tool for microbiome-based disease diagnostics and personalized medicine. The software and tutorials are freely available as an R package, named PIRF, at https://github.com/hk1785/PIRF.