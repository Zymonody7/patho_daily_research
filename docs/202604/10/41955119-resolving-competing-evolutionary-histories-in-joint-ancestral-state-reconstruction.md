---
title: Resolving competing evolutionary histories in joint ancestral state reconstruction.
title_zh: 解析联合祖先状态重建中的竞争性演化历史
authors: "James D Boyko, Kyle J Gontjes, Evan S Snitkin, Stephen A Smith"
date: 2026-04-14
pdf: "https://pubmed.ncbi.nlm.nih.gov/41955119/"
tags: ["query:pathoai"]
score: 6.0
evidence: 进化轨迹的联合祖先状态重建
tldr: 传统的祖先状态重建（ASR）多关注单个节点的边缘概率，难以刻画完整的进化轨迹。本研究提出了一种基于随机映射条件概率的联合重建方法，通过采样生成可能的进化历史分布，并提供了量化不确定性的工具。在模拟实验和肺炎克雷伯菌耐药性演化分析中，该方法成功识别出多个竞争性的进化路径，比传统的节点式方法更准确地还原了复杂的表型-基因型转换过程，为理解性状演化提供了更全面的视角。
selection_source: fresh_fetch
motivation: 传统的边缘重建方法仅针对单个节点进行推断，无法有效识别和描述跨越整个进化树的连贯进化轨迹及其中存在的多种可能性。
method: 利用随机映射导出的条件概率对可能的祖先历史分布进行高效采样，并开发了配套工具来量化和总结这些联合重建结果的不确定性。
result: 实验证明联合重建在还原性状演化史方面优于节点式估计，并揭示了肺炎克雷伯菌耐药性演化中存在多条具有不同表型-基因型转换特征的竞争路径。
conclusion: 联合重建方法通过捕捉完整的进化序列及其不确定性，为研究复杂的生物性状演化和预测耐药性等关键生物学过程提供了比传统方法更精确的分析框架。
---

## 摘要
祖先状态重建（ASR）是比较生物学中的基础工具，为谱系的演化历史提供了深刻见解。随着每一种新演化模型的出现，我们以更高的生物学真实性估计祖先状态的能力不断提升。然而，该领域主要依赖于关注单个节点的边缘重建（marginal reconstructions）。这一框架在分析上是易于处理的，且适用于针对特定节点的假设，但其设计并非为了识别整棵树上最可能的演化事件序列。我们认为，对于对演化轨迹感兴趣的研究人员，联合重建（joint reconstructions）提供了一种更有效的方式来表征完整的转变历史。传统上，联合重建算法仅关注单一的最可能序列，但在本文中，我们利用源自随机映射（stochastic mapping）的条件概率，高效地对合理的祖先历史分布进行采样。此外，我们还提供了量化和总结这种联合不确定性的工具。通过模拟和实证案例研究，我们证明了联合重建比逐节点的边缘估计能更有效地恢复模拟的性状历史，且围绕这些历史的不确定性具有重要的生物学意义。我们将该方法应用于流行性多重耐药肺炎克雷伯菌（Klebsiella pneumoniae），发现抗生素耐药性的演化并非单一的叙事，而是一系列竞争性的历史。这些历史中的每一种都表现出独特的表型-基因型转变，逐节点方法难以识别这些转变，但它们对于预测和理解耐药性演化具有至关重要的意义。

## Abstract
Ancestral state reconstruction (ASR) is a foundational tool in comparative biology, offering insights into the evolutionary history of lineages. With each new evolutionary model, our ability to estimate ancestral states with increased biological realism has improved. However, the field has primarily relied on marginal reconstructions, which focus on individual nodes. This framework is analytically tractable and appropriate for node-specific hypotheses, but it is not designed to identify the most probable sequence of evolutionary events across a tree. We argue that for researchers interested in evolutionary trajectories, joint reconstructions provide a more effective way to characterize the full history of transitions. Traditionally, joint reconstruction algorithms focused only on the single most likely sequence, but here we use conditional probabilities derived from stochastic mapping to sample the distribution of plausible ancestral histories efficiently. Furthermore, we provide tools to quantify and summarize this joint uncertainty. Through simulations and an empirical case study, we demonstrate that joint reconstructions more effectively recover simulated trait histories than node-wise marginal estimates and that the uncertainty surrounding these histories can be biologically meaningful. We apply our methods to epidemic multidrug-resistant Klebsiella pneumoniae and find that the evolution of antibiotic resistance is not a single narrative but a series of competing histories. Each of these histories exhibits distinct phenotype-genotype transitions that node-wise approaches would struggle to identify, yet have critical implications for predicting and understanding resistance evolution.