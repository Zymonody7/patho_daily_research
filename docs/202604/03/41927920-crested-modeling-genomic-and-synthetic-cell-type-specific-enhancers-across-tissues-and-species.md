---
title: "CREsted: modeling genomic and synthetic cell-type-specific enhancers across tissues and species."
title_zh: CREsted：跨组织和物种的基因组及合成细胞类型特异性增强子建模
authors: "Niklas Kempynck, Seppe De Winter, Casper H Blaauw, Vasileios Konstantakos, Eren Can Ekşi, Sam Dieltiens, Darina Abaffyová, Valérie Bercier, Ibrahim I Taskiran, Gert Hulselmans, Katina Spanier, Valerie Christiaens, Ludo Van Den Bosch, Lukas Mahieu, Stein Aerts"
date: 2026-04-02
pdf: "https://pubmed.ncbi.nlm.nih.gov/41927920/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 用于基因组调控密码和序列表示学习的深度学习
tldr: 针对基因组增强子调控逻辑解析与设计的复杂性，研究者开发了 CREsted 软件套件。该工具整合了单细胞染色质可及性数据预处理、序列建模、可解释性分析及序列设计功能。通过在小鼠大脑、人类免疫细胞及癌症数据上的应用，以及在斑马鱼体内的实验验证，CREsted 证明了其在跨物种、跨组织解析增强子语法和设计高特异性人工增强子方面的强大能力，为基因调控研究提供了端到端的解决方案。
selection_source: fresh_fetch
motivation: 现有的基因组深度学习模型缺乏一个集成的端到端框架，难以高效地从单细胞数据中解析增强子逻辑并用于人工序列设计。
method: 开发了名为 CREsted 的软件套件，它将 scATAC-seq 数据处理、基于序列的染色质可及性预测模型、大模型微调策略以及合成增强子设计算法整合在一起。
result: 该工具成功识别了不同物种和组织中的细胞特异性增强子特征，并利用斑马鱼发育图谱训练模型，设计出经体内实验验证有效的细胞特异性人工增强子。
conclusion: CREsted 为研究者提供了一个从原始测序数据到功能性序列设计的全流程工具，显著提升了对基因组调控密码的理解与应用能力。
---

## 摘要
基于序列的深度学习模型已成为分析基因组调控密码的最先进方法。特别是在增强子研究中，这些模型擅长破译其活性背后的序列语法。为了实现端到端的增强子建模与设计，我们开发了一个名为 CREsted（顺式作用元件序列训练、解释与设计）的软件包。它集成了单细胞转座酶可及染色质测序（scATAC-seq）数据的预处理与分析、基于序列的染色质可及性建模、序列设计以及用于破译增强子语法的下游分析。我们在小鼠皮层和人类外周血单核细胞数据集上展示了 CREsted 的功能。此外，我们利用 CREsted 比较了不同肿瘤类型之间的间充质样癌细胞状态，并研究了 CREsted 框架内基因组基础模型的不同微调策略。最后，我们在斑马鱼发育图谱上训练了一个模型，并利用该模型设计并体内验证了细胞类型特异性增强子。针对不同的数据集，我们证明了 CREsted 能够促进高效的训练与分析，从而实现对增强子逻辑的深入探究以及跨组织和物种的合成增强子设计。

## Abstract
Sequence-based deep learning models have become the state of the art for analyzing the genomic regulatory code. Particularly for enhancers, these models excel at deciphering sequence grammar that underlies their activity. To enable end-to-end enhancer modeling and design, we developed a software package called CREsted (cis-regulatory element sequence training, explanation and design). It combines preprocessing and analysis of single-cell assay for transposase-accessible chromatin using sequencing data, modeling chromatin accessibility from sequence, sequence design and downstream analysis to decipher enhancer grammar. We demonstrate CREsted's functionality on a mouse cortex and a human peripheral blood mononuclear cell dataset. Additionally, we use CREsted to compare mesenchymal-like cancer cell states between tumor types, and we investigate different fine-tuning strategies of genomic foundation models within CREsted. Finally, we train a model on a zebrafish development atlas and use this to design and in vivo validate cell-type-specific enhancers. For varying datasets, we demonstrate that CREsted facilitates efficient training and analyses, enabling scrutinization of the enhancer logic and design of synthetic enhancers across tissues and species.