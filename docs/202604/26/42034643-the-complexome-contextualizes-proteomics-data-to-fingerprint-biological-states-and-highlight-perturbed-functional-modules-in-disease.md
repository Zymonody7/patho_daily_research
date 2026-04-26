---
title: The complexome contextualizes proteomics data to fingerprint biological states and highlight perturbed functional modules in disease.
title_zh: 蛋白复合物组将蛋白质组学数据背景化，以刻画生物状态特征并突出疾病中受扰动的功能模块。
authors: "Mainak Guharoy, Isabelle Adant, Matthew Bird, Alexander Botzki, James Collier, Jonas Dehairs, Stefaan Derveaux, Simon Devos, Geert Goeminne, Francis Impens, Andrea Jáñez Pedrayes, Rekin's Janky, Ruth Maes, Pedro Magalhães, Teresa M Maia, Wouter Meersseman, Daisy Rymen, Johannes V Swinnen, Delphi Van Haver, Dries Verdegem, Peter Witters, David Cassiman, Bart Ghesquiere"
date: 2026-04-25
pdf: "https://pubmed.ncbi.nlm.nih.gov/42034643/"
tags: ["query:bioinfo"]
score: 7.0
evidence: 多组学整合的生物信息学框架
tldr: 针对单组学数据难以揭示疾病复杂功能紊乱的问题，该研究提出了一个基于蛋白质复合物集合（Complexome）的生物信息学框架。通过将蛋白质组学数据映射到已知的复合物模块，该方法能刻画不同组织的生物学特征指纹，并精准识别代谢疾病中线粒体等功能模块的异常。这为从系统层面解析疾病表型背后的分子机制提供了高效的整合分析工具。
selection_source: fresh_fetch
motivation: 传统的蛋白质组学分析往往缺乏功能背景，难以从单个蛋白质的丰度变化中直接推断出复杂的生物学功能失调或疾病机制。
method: 该研究构建了涵盖人类及模型生物的蛋白质复合物参考库，并开发了一套将蛋白质组学定量数据映射到复合物层面的计算框架，用于识别功能模块的重塑。
result: 通过对人体组织和代谢缺陷患者样本的分析，该框架成功提取了组织特异性的生物学指纹，并精准定位了线粒体氧化磷酸化等关键功能模块的病理扰动。
conclusion: 以蛋白质复合物为核心的分析范式能够有效整合蛋白质组学数据，为理解疾病状态下的系统级功能变化和表型差异提供了新的视角。
---

## 摘要
分析单一组学并整合多模态组学数据集以捕捉疾病中的功能失调仍然具有挑战性。在此，我们提出了一个生物信息学框架，利用经过人工校验的蛋白质复合物数据集（“蛋白复合物组”）作为蛋白质组学数据整合的基础。该蛋白复合物组适用于人类和其他模式生物，提供了细胞功能的全局视图，并支持使用蛋白质组学数据集进行查询。我们首先基准测试了人类组织中的蛋白质丰度如何塑造不同的蛋白复合物组图谱，从而用于刻画生物活动的特征。接下来，我们利用疾病组与对照组的蛋白质组定量数据分析了蛋白复合物组的重塑。通过使用来自经基因确诊的代谢缺陷患者成纤维细胞的蛋白质组数据，我们识别出线粒体氧化磷酸化复合物以及涉及更广泛线粒体功能的其他复合物中存在的显著扰动。蛋白复合物组通过将测得的蛋白质水平扰动映射到特定的分子复合物，提供了一种系统级的方法来剖析疾病相关功能和表型变化背后的机制。该软件以 Python notebook 的形式提供，网址为 https://github.com/mguharoy/Complexome。

## Abstract
Analyzing single omics and integrating multimodal omics datasets to capture functional dysregulation in disease remains challenging. Here, we propose a bioinformatics framework that leverages curated datasets of protein complexes ('complexome') as a foundation for proteomics data integration. Available for human and other model organisms, the complexome provides a global view of cellular function, enabling queries with proteomics datasets. We first benchmarked how protein abundances across human tissues shape distinct complexomic profiles, serving to fingerprint biological activity. Next, we analyzed complexome remodeling using disease versus control proteomics quantifications. Using proteomics data from fibroblasts of patients with genetically confirmed metabolic defects, we identified significant perturbations in mitochondrial oxidative phosphorylation complexes and additional complexes involved in wider mitochondrial functions. The complexome provides a systems-wide approach to dissect mechanisms underlying disease-related functional and phenotypic changes by mapping measured protein-level perturbations to specific molecular complexes. The software is available as a Python notebook at https://github.com/mguharoy/Complexome.