---
title: Discriminating models of trait evolution.
title_zh: 性状演化模型的判别
authors: "Jenniffer Roa Lozano, Surbhit Jangra, Michael DeGiorgio, Raquel Assis, Richard Adams"
date: 2026-04-02
pdf: "https://pubmed.ncbi.nlm.nih.gov/41661137/"
tags: ["query:pathoai"]
score: 7.0
evidence: 用于预测进化模型和系统发育比较方法的监督学习
tldr: 针对系统发育比较生物学中难以准确推断性状演化模型的问题，本文提出了 Evolutionary Discriminant Analysis (EvoDA) 框架。该方法将监督学习中的判别分析引入生物演化研究，通过模拟数据训练模型来预测真实性状的演化模式。在真菌系统发育案例中，EvoDA 在处理含测量误差的数据时表现优于传统统计方法，并成功揭示了基因表达演化中稳定选择占主导的规律，为复杂演化过程的推断提供了新工具。
selection_source: fresh_fetch
motivation: 传统的统计拟合方法在处理具有测量误差或复杂生物背景的性状演化模型选择时，往往难以提供准确的推断结果。
method: 提出了一种名为 EvoDA 的监督学习框架，利用判别分析技术，通过模拟生成的演化数据来训练分类器，从而识别最符合观测性状的演化模型。
result: 在真菌系统发育的基准测试中，EvoDA 在存在测量误差的现实场景下显著优于传统模型选择方法，并准确预测了基因表达的演化节奏。
conclusion: EvoDA 为比较生物学提供了一种鲁棒的机器学习推断框架，能够有效应对高噪声数据，深化了对基因表达等复杂性状演化机制的理解。
---

## 摘要
比较生物学的一个核心挑战是将现今物种间的性状变异与过去发生的未观测到的演化过程联系起来。在这一领域，系统发育比较方法对于拟合、比较和选择具有不同复杂性和生物学意义的演化模型具有不可估量的价值。传统上，演化研究依赖于常规统计方法来评估模型拟合度，并确定最能解释给定性状变异的模型。在此，我们探索了一种替代策略，即通过判别分析应用监督学习来预测演化模型。我们正式引入演化判别分析（Evolutionary Discriminant Analysis, EvoDA）作为生物学家工具箱的补充，为研究性状演化提供了一套新方法。我们通过一系列真菌系统发育案例研究评估了 EvoDA 与常规模型选择的性能，每个案例都针对日益具有挑战性的分析任务。结果展示了 EvoDA 的优势，在研究受测量误差影响的性状时，其相对于常规方法有显著改进，而这往往反映了经验数据集中的真实情况。为了补充基于模拟的基准测试，我们探索了 EvoDA 在处理一项公认难题中的应用：预测基因表达演化的模式与速率。这一经验分析表明，稳定选择作用于大多数基因，而在少数与应激、细胞运输和转录调节相关的基因中出现了表达演化的爆发。总的来说，我们的研究结果说明了 EvoDA 在一系列演化和实验背景下预测性状模型的潜力，为下一代比较研究建立了一个新的方法论框架。

## Abstract
A central challenge in comparative biology is linking present-day trait variation across species with unobserved evolutionary processes that occurred in the past. In this endeavor, phylogenetic comparative methods are invaluable for fitting, comparing, and selecting evolutionary models of varying complexity and biological meaning. Traditionally, evolutionary studies have relied on conventional statistical approaches to assess model fit and identify the one that best explains variation in a given trait. Here, we explore an alternative strategy by applying supervised learning to predict evolutionary models via discriminant analysis. We formally introduce Evolutionary Discriminant Analysis (EvoDA) as an addition to the biologist's toolkit, offering a suite of new methods for studying trait evolution. We evaluate the performance of EvoDA alongside conventional model selection through a series of fungal phylogeny case studies, each targeting increasingly challenging analytical tasks. These results showcase the strengths of EvoDA, with substantial improvements over conventional approaches when studying traits subject to measurement error, which likely reflect realistic conditions in empirical datasets. To complement our simulation-based benchmarking, we explore the application of EvoDA for tackling a notoriously difficult task: predicting the mode and tempo of gene expression evolution. This empirical analysis suggests that stabilizing selection acts on a majority of genes, with bursts of expression evolution in a handful of genes related to stress, cellular transportation, and transcription regulation. Collectively, our findings illustrate the promise of EvoDA for predicting trait models across a range of evolutionary and experimental contexts, establishing a new methodological framework for the next era of comparative research.