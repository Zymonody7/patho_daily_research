---
title: A Systematic Survey and Benchmark of Deep Learning for Molecular Property Prediction in the Foundation Model Era.
title_zh: 基础模型时代的分子性质预测深度学习：系统综述与基准测试
authors: "Zongru Li, Xingsheng Chen, Honggang Wen, Regina Qianru Zhang, Ming Li, Xiaojin Zhang, Hongzhi Yin, Qiang Yang, Kwok-Yan Lam, Pietro Lio, Siu-Ming Yiu"
date: 2026-05-07
pdf: "https://pubmed.ncbi.nlm.nih.gov/42096352/"
tags: ["query:bioinfo"]
score: 10.0
evidence: 用于分子属性预测和药物发现的基础模型
tldr: 分子性质预测是连接分子结构与生物物理行为的关键。本文系统综述了从量子化学、描述符机器学习到几何深度学习及大模型时代的演进，构建了统一的分类体系。通过整合工业界与学术界的多领域数据集，揭示了现有基准在立体化学一致性和数据分割策略上的局限，并提出了物理感知学习与多模态基准等未来方向，为构建更可靠的分子发现模型提供了指南。
selection_source: fresh_fetch
motivation: 现有的分子性质预测研究面临数据质量参差不齐、评估协议不统一以及大模型时代下缺乏系统性基准测试的问题。
method: 建立了一套涵盖分子表示、模型架构及跨学科应用的统一分类法，并对比了量子、几何深度学习与基础模型等四种范式。
result: 发现当前基准在处理立体化学和异质实验来源时存在不一致性，且随机分割策略往往高估了模型的泛化能力。
conclusion: 建议未来研究应聚焦于嵌入量子一致性的物理感知学习、不确定性校准的基础模型以及整合计算与实验数据的多模态基准生态。
---

## 摘要
分子性质预测融合了量子化学、化学信息学和深度学习，旨在将分子结构与物理化学及生物行为联系起来。本综述追溯了四个互补的范式，包括量子计算、描述符机器学习、几何深度学习和基础模型，并概述了一个统一的分类体系，将分子表示、模型架构和跨学科应用联系起来。基准分析整合了来自广泛使用的数据集和反映工业界视角的数据集的证据，涵盖了量子、物理化学、生理学和生物物理领域。本综述检查了当前数据整理、划分策略和评估协议的标准，强调了包括立体化学不一致、异质分析来源以及在随机或定义不良的划分下的可重复性限制等挑战。这些观察结果推动了基准设计的现代化，使其向更透明、具备时间感知和骨架感知的方向发展。我们进一步提出了三个前瞻性方向：(i) 嵌入量子一致性的物理感知学习，(ii) 用于可靠推理的不确定性校准基础模型，以及 (iii) 整合计算和实验数据的现实多模态基准生态系统。仓库地址：https://github.com/Zongru-Li/Survey-and-Benchmarks-of-DL-for-Molecular-Property-Prediction-in-the-Foundation-Model-Era。

## Abstract
Molecular property prediction integrates quantum chemistry, cheminformatics, and deep learning to connect molecular structure with physicochemical and biological behavior. This survey traces four complementary paradigms, including Quantum, Descriptor Machine Learning, Geometric Deep Learning, and Foundation Models, and outlines a unified taxonomy linking molecular representations, model architectures, and interdisciplinary applications. Benchmark analyses integrate evidence from both widely used data sets and data sets reflecting industry perspectives, encompassing quantum, physicochemical, physiological, and biophysical domains. The survey examines current standards in data curation, splitting strategies, and evaluation protocols, highlighting challenges including inconsistent stereochemistry, heterogeneous assay sources, and reproducibility limitations under random or poorly defined splits. These observations motivate the modernization of benchmark design toward more transparent, time- and scaffold-aware methodologies. We further propose three forward-looking directions: (i) physics-aware learning embedding quantum consistency, (ii) uncertainty-calibrated foundation models for trustworthy inference, and (iii) realistic multimodal benchmark ecosystems integrating computational and experimental data. Repository: https://github.com/Zongru-Li/Survey-and-Benchmarks-of-DL-for-Molecular-Property-Prediction-in-the-Foundation-Model-Era.

---

## 论文详细总结（自动生成）

这篇论文是关于分子性质预测（Molecular Property Prediction, MPP）的深度学习综述与基准测试。它系统地梳理了在“大模型（Foundation Models）”时代，AI 如何理解和预测分子的物理、化学及生物行为。

### 1. 解决的问题与核心价值
*   **核心问题**：如何利用 AI 准确预测分子的性质（如毒性、溶解度、结合力等）。这在药物研发中至关重要，因为实验筛选分子的成本极高且耗时长。
*   **为什么值得看**：目前该领域模型繁多（从传统的图神经网络到最新的 Transformer 大模型），但评估标准混乱。本文不仅梳理了技术演进，还揭露了现有测试方法中的“水分”（如随机划分数据集导致性能虚高），并为工业界和学术界提供了统一的基准。

### 2. 白话版概述
想象分子是一堆乐高积木，我们要预测这堆积木是否容易散架（物理性质）或者是否能塞进某个特定的洞里（生物活性）。
*   **过去**：靠专家手动总结积木的特征（如红色块有多少个）。
*   **中期**：把分子看作一张图（Graph），用图神经网络自动学习积木的连接关系。
*   **现在**：像训练 ChatGPT 一样，让 AI 阅读数亿个分子的结构，形成“化学直觉”（基础模型），然后再去预测具体性质。
*   **结论**：虽然大模型很强，但如果忽略了分子的 3D 空间结构和物理规律，预测结果在真实场景中往往不可靠。

### 3. 方法部分：核心思想与分类
论文将 MPP 的技术演进归纳为四种范式：
*   **量子范式 (Quantum)**：基于物理方程（如密度泛函理论 DFT），精度最高但计算极慢，主要用于生成高质量训练数据。
*   **描述符机器学习 (Descriptor ML)**：将分子转化为“指纹”向量（Fingerprints），用随机森林或 XGBoost 预测。简单好用，但上限较低。
*   **几何深度学习 (Geometric DL)**：核心是**图神经网络 (GNN)**。它考虑了原子间的对称性和 3D 空间位置，能捕捉分子在空间中的真实形态。
*   **基础模型 (Foundation Models)**：
    *   **训练流程**：先在海量无标签分子数据上进行“自监督预训练”（如掩码预测原子），学习通用的化学表示。
    *   **关键取舍**：使用 1D 字符串（SMILES）虽然计算快，但会丢失空间信息；使用 3D 预训练效果好，但数据获取成本高。

### 4. 实验部分：基准测试与结果
*   **数据与任务**：涵盖了量子化学（QM9）、物理化学（Lipophilicity）、生理学（Tox21 毒性）和生物物理（PDBbind 蛋白质结合）等多个领域。
*   **Baseline**：对比了传统的图模型（如 GIN, GAT）和最新的大模型（如 Graphormer, MolFormer）。
*   **关键发现**：
    *   **数据分割陷阱**：如果使用“随机分割”数据集，模型表现会非常好；但如果使用“骨架分割（Scaffold Split）”（即测试集里的分子长得和训练集完全不同），模型性能会大幅下降。这说明很多 AI 只是在“背答案”，而不是真的懂化学。
    *   **立体化学（Stereochemistry）**：很多模型分不清分子的“左手型”和“右手型”（手性），这在生物学上会导致预测结果完全错误。

### 5. 资源与算力
*   **文中未充分披露**：论文主要侧重于综述和基准测试的框架构建，没有详细列出每个模型训练的具体 GPU 小时数。但作者提供了 [GitHub 仓库](https://github.com/Zongru-Li/Survey-and-Benchmarks-of-DL-for-Molecular-Property-Prediction-in-the-Foundation-Model-Era)，其中包含复现代码和数据集。

### 6. 真正可信的贡献
*   **揭露了评估乱象**：有力地证明了“随机分割”会误导研究者，提倡使用更符合实际研发场景的“时间感知”和“骨架感知”分割法。
*   **统一分类法**：为 AI 研究者提供了一张清晰的地图，明确了不同表示方法（1D 字符串、2D 图、3D 坐标）的优劣。
*   **工业界视角**：整合了反映真实制药工业需求的数据集，而不仅仅是学术界常用的玩具数据集。

### 7. 局限与风险
*   **实验数据噪声**：生物实验（Assay）本身存在很大误差，AI 模型很难区分是模型预测错了，还是原始实验数据就有问题。
*   **外推能力不足**：当遇到结构全新的分子（Out-of-Distribution）时，即便是最强的大模型，预测准确率也会断崖式下跌。
*   **计算成本**：高性能的 3D 几何模型在处理大规模分子库时，计算开销依然巨大，难以在工业流水线中普及。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：正在从 NLP/CV 转向药物研发的 AI 研究员，以及希望利用深度学习提升筛选效率的化学家。
*   **后续可跟进的问题**：如何将“物理定律”（如能量守恒、对称性）直接嵌入到 Transformer 架构中，而不是仅仅让模型去“猜”化学规律？

（完）
