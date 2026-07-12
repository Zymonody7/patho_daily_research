---
title: Combining multiplexed functional data to improve variant classification.
title_zh: 整合多重功能数据以改进变异分类
authors: "Jeffrey D Calhoun, Moez Dawood, Charlie F Rowlands, Shawn Fayer, Elizabeth J Radford, Abbye E McEwen, Malvika Tejura, Clare Turnbull, Amanda B Spurdle, Lea M Starita, Sujatha Jagannathan"
date: 2026-07-11
pdf: "https://pubmed.ncbi.nlm.nih.gov/42432739/"
tags: ["query:seqai"]
score: 7.0
evidence: 结合多重功能数据进行变异分类
tldr: 针对临床中大量意义不明变异（VUS）难以分类的问题，本研究提出了一种整合多个高通量功能实验（MAVE）数据的方法。通过对TP53等基因的多源数据进行随机森林建模，证明整合评分在分类准确性上优于单一实验。该方法增强了临床变异解读的证据强度，并配套发布了在线工具辅助研究。
selection_source: fresh_fetch
motivation: 临床上存在大量意义不明的基因变异，且单一的高通量功能实验往往无法全面捕捉基因在不同生物过程中的功能受损情况。
method: 研究者通过收集TP53、LDLR和PTEN基因的多个实验数据集，利用主成分分析及随机森林等监督学习算法，探索了将多源功能评分融合为统一指标的最优路径。
result: 结果表明，采用随机森林等监督学习方法整合后的综合评分在变异分类的敏感性和特异性上均显著优于任何单一实验数据集。
conclusion: 建立规范的多源实验数据整合流程能够显著增强临床变异分类的证据强度，为解析复杂基因的致病机制提供了有力工具。
---

## 摘要
背景：近年来，随着 ClinVar 中报告的意义未明变异（VUS）数量激增，大规模解析 VUS 已成为当务之急。变异效应多重检测（MAVEs）可以在单次实验中测量数百到数千个遗传变异的功能后果，正成为可用于临床变异分类的强大证据来源。针对同一基因，已发表的 MAVE 数据越来越多，有时这些数据测量的是变异影响的不同方面。当需要考虑一个基因的多种功能角色时，整合来自多个 MAVE 的数据可能会提供对遗传变异后果更全面的评估，从而影响变异分类。方法：我们整理了针对 TP53 基因的五个 MAVE、LDLR 基因的两个 MAVE 以及 PTEN 基因的两个 MAVE 的已发表数据集。使用统计方法（主成分分析）、无监督学习（k-means 聚类）和有监督学习（朴素贝叶斯和随机森林分类器）来整合多个 MAVE 数据集。使用标准指标（敏感性、特异性等）以及推定的变异分类框架中的证据强度来评估 MAVE 整合方法的效用。结果：在此，我们为整合此类多重功能数据提供了指导，包括从数据整理和收集到模型生成和验证的逐步过程。我们还提供了一个 Web 小程序，允许用户测试整合来自多个检测的评分集的各种方法，计算所有变异的综合功能评分，并评估整合数据是否能够为致病性或良性提供更强的证据。总的来说，与任何单一的 MAVE 数据集相比，随机森林等有监督学习方法改进了变异分类。结论：通过遵循本文概述的步骤并设置适当的防护措施，研究人员可以最大限度地发挥 MAVE 的价值，加强临床变异分类的功能证据，并可能揭示临床相关基因的新致病机制。

## Abstract
BACKGROUND: With the surge in the number of variants of uncertain significance (VUS) reported in ClinVar in recent years, there is an imperative to resolve VUS at scale. Multiplexed assays of variant effect (MAVEs), which allow the functional consequence of 100s to 1000s of genetic variants to be measured in a single experiment, are emerging as a powerful source of evidence which can be used in clinical variant classification. Increasingly, multiple published MAVEs are available for the same gene, sometimes measuring different aspects of variant impact. When multiple functional roles of a gene need to be considered, combining data from multiple MAVEs may provide a more comprehensive measure of the consequence of a genetic variant, which could impact variant classifications. METHODS: We curated published datasets from five MAVEs for the gene TP53, two MAVEs for LDLR and two MAVEs for PTEN. Statistical methods (principal component analysis), unsupervised learning (k-means clustering), and supervised learning (Naïve Bayes and random forest classifiers) were used to integrate multiple MAVE datasets. The utility of MAVE integration methods were assessed using standard metrics (sensitivity, specificity, etc) as well as evidence strength in a putative variant classification framework. RESULTS: Here, we provide guidance for combining such multiplexed functional data, incorporating a stepwise process from data curation and collection to model generation and validation. We also present a web applet that allows users to test various methods for combining score sets from multiple assays, calculate integrated functional scores for all variants, and assess whether combining data enables the application of stronger evidence for pathogenicity or benignity. In general, supervised learning methods such as random forest led to improved variant classification as compared to any individual MAVE dataset. CONCLUSIONS: By following the steps outlined herein with appropriate guardrails, researchers can maximize the value of MAVEs, strengthen the functional evidence for clinical variant classification, and potentially uncover novel mechanisms of pathogenicity for clinically relevant genes.