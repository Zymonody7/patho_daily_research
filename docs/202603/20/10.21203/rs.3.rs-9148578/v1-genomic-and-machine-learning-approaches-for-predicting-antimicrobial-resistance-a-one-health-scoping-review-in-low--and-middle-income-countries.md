---
title: "Genomic and Machine Learning Approaches for Predicting Antimicrobial Resistance: A One Health Scoping Review in Low- and Middle-Income Countries"
title_zh: 基因组学与机器学习方法预测抗微生物药物耐药性：中低收入国家“全健康”范围综述
authors: "Kimera Z, Mtebe M, kibwana u, masoud s, Kamori D, mbugi e, Matee MI."
date: 2026-03-18
pdf: "https://doi.org/10.21203/rs.3.rs-9148578/v1"
tags: ["query:pathoai"]
score: 10.0
evidence: 利用机器学习从基因组监测中预测细菌耐药性
tldr: "抗生素耐药性（AMR）在低中收入国家威胁严重，传统检测耗时且难以应对复杂机制。本综述系统梳理了结合全基因组测序与机器学习的预测方法，分析了27项相关研究。结果显示，该类方法在耐药性预测上准确率达78%-98%，能有效整合人类、动物及环境的“全健康”数据，为资源受限地区提供了快速、高分辨率的监测新路径，对提升全球公共卫生预警能力具有重要价值。"
selection_source: fresh_fetch
motivation: 针对低中收入国家传统耐药性检测效率低、实验室能力受限的问题，探索利用基因组学与人工智能技术实现快速、准确的耐药性预测。
method: 系统综述了27项研究，重点分析了利用单核苷酸多态性、k-mer编码等基因特征，结合随机森林、梯度提升及神经网络等模型预测细菌耐药表型的方法。
result: "机器学习模型在耐药性预测上的准确率普遍处于78%至98%之间，且通过SHAP等可解释性AI技术显著提升了预测结果在临床和生物学上的可理解性。"
conclusion: 基因组机器学习是实现“全健康”监测的关键工具，但未来需扩大针对低中收入国家的特定数据集并加强外部验证，以确保技术的公平与可持续应用。
---

## 摘要
背景：抗微生物药物耐药性（AMR）是影响人类、动物和环境的主要全球健康威胁。其负担在中低收入国家（LMICs）尤为严重，这些国家传染病流行，抗微生物药物的使用往往缺乏监管，且实验室能力有限。传统的表型检测虽然必不可少，但耗时较长，且可能无法检测到新兴或复杂的耐药机制。目的：本范围综述梳理了结合机器学习（ML）和人工智能（AI）预测细菌 AMR 的基因组监测方法，重点关注方法策略、预测性能以及与中低收入国家“全健康”监测的相关性。方法：系统检索了 PubMed、Scopus、Web of Science、EMBASE 和预印本服务器（2020-2026 年），确定了应用全基因组测序（WGS）或泛基因组方法结合 ML/AI 预测 AMR 表型的研究。提取了关于病原体、基因组特征工程、ML/AI 模型、验证策略、性能指标、样本来源（人类、动物、环境）以及中低收入国家相关性的数据。结果：27 项研究符合纳入标准，其中 22 项具有直接或可转移的中低收入国家相关性。预测性能在 78% 到 98% 之间，中低收入国家数据集的准确率达到 80%-94%。基于树的集成模型（随机森林、梯度提升）、逻辑回归和神经网络占主导地位。基因组特征包括单核苷酸多态性、k-mer 编码和泛基因组存在-缺失矩阵。可解释 AI 方法（如 SHAP）提高了可解释性。大多数模型是在高收入国家的数据集上训练的，跨越人类、动物和环境宿主的综合中低收入国家数据集仍然有限。结论：基因组 ML/AI 方法为 AMR 预测和“全健康”监测提供了一条快速、高分辨率的途径。扩大中低收入国家特有的数据集、改进外部验证以及整合可解释 AI 对于实现公平和可持续的部署至关重要。

## Abstract
<title>Abstract</title>  <p>Background  Antimicrobial resistance (AMR) is a major global health threat affecting humans, animals, and the environment. Its burden is particularly severe in low- and middle-income countries (LMICs), where infectious diseases are prevalent, antimicrobial use is often unregulated, and laboratory capacity is limited. Conventional phenotypic testing is essential but time-consuming and may fail to detect emerging or complex resistance mechanisms. Objective  This scoping review maps genomic surveillance approaches combined with machine learning (ML) and artificial intelligence (AI) for predicting bacterial AMR, emphasizing methodological strategies, predictive performance, and relevance to LMIC One Health surveillance. Methods  Systematic searches of PubMed, Scopus, Web of Science, EMBASE, and preprint servers (2020–2026) identified studies applying whole-genome sequencing (WGS) or pan-genomic approaches with ML/AI to predict AMR phenotypes. Data were extracted on pathogens, genomic feature engineering, ML/AI models, validation strategies, performance metrics, sample sources (human, animal, environmental), and LMIC relevance. Results  Twenty-seven studies met inclusion criteria, including 22 with direct or transferable LMIC relevance. Predictive performance ranged from 78% to 98%, with LMIC datasets achieving 80%–94% accuracy. Tree-based ensembles (Random Forest, gradient boosting), logistic regression, and neural networks predominated. Genomic features included single nucleotide polymorphisms, k-mer encodings, and pan-genome presence–absence matrices. Explainable AI methods, such as SHAP, improved interpretability. Most models were trained on high-income country datasets, and integrated LMIC datasets spanning human, animal, and environmental reservoirs remain limited. Conclusions  Genomic ML/AI approaches offer a rapid, high-resolution pathway for AMR prediction and One Health surveillance. Expanding LMIC-specific datasets, improving external validation, and integrating explainable AI are critical for equitable and sustainable deployment.</p>

---

## 论文详细总结（自动生成）

这篇论文是一篇关于利用机器学习（ML）和人工智能（AI）结合基因组学手段预测**抗微生物药物耐药性（AMR）**的范围综述（Scoping Review）。

### 1. 解决的问题与核心价值
**核心问题**：细菌产生耐药性（即抗生素杀不死细菌）是全球健康危机。传统的检测方法（表型检测）需要培养细菌，耗时数天甚至数周，且在资源匮乏的中低收入国家（LMICs）缺乏实验室设备。
**核心价值**：论文探讨了如何通过“全基因组测序（WGS）+ AI”实现快速预测。它特别关注了“全健康”（One Health）视角——即不仅看人类，还整合动物和环境中的细菌数据，为中低收入国家提供了一套低成本、高效率的监测技术路线图。

### 2. 白话版概述
简单来说，细菌的耐药性是由其 DNA 决定的。以前我们要把细菌放在药水里看它死不死，现在我们直接“读”它的 DNA 序列。由于 DNA 数据量巨大且规律复杂，人类肉眼看不出来，于是请 AI 来当“翻译官”。AI 通过学习已知的耐药细菌 DNA 特征，就能在拿到新细菌序列时，几秒钟内判断出它对哪种抗生素耐药。这篇综述总结了过去几年里，科学家们用什么 AI 模型、什么数据特征在这一领域取得了多大的进展。

### 3. 方法部分：AI 预测耐药性的技术路径
*   **核心思想**：将细菌的基因组信息转化为 AI 可处理的特征向量，建立从“基因型”（Genotype）到“耐药表型”（Phenotype）的映射函数。
*   **特征工程（如何把 DNA 变成数字）**：
    *   **SNPs（单核苷酸多态性）**：寻找 DNA 序列中单个“字母”的变化。
    *   **k-mers**：将 DNA 序列切成长度为 $k$ 的短片段（类似 NLP 中的 n-gram），统计这些片段出现的频率。
    *   **泛基因组矩阵（Pan-genome）**：统计特定耐药基因的“存在或缺失”（Presence/Absence）。
*   **模型结构**：
    *   **传统机器学习**：随机森林（Random Forest）、梯度提升树（XGBoost/LightGBM）和逻辑回归最为常用，因为它们在小样本下表现稳健。
    *   **深度学习**：卷积神经网络（CNN）和多层感知机（MLP）被用于处理原始序列或复杂的特征组合。
*   **关键设计取舍**：研究者倾向于使用**可解释 AI（XAI）**工具（如 SHAP 值），因为医生需要知道 AI 为什么判断这门细菌耐药（比如是因为哪个具体的基因突变），而不仅仅是一个概率数字。

### 4. 实验与结果总结
*   **数据来源**：综述分析了 27 项研究，涵盖了人类临床样本、家畜（猪、鸡）以及环境（水体）中的细菌。
*   **任务目标**：二分类任务（耐药 vs 敏感）或回归任务（预测最小抑菌浓度 MIC）。
*   **评价指标**：准确率（Accuracy）、灵敏度（Sensitivity）、特异性（Specificity）。
*   **主要结果**：
    *   整体预测准确率在 **78% 到 98%** 之间。
    *   针对中低收入国家的数据集，准确率也能达到 **80%-94%**。
    *   集成学习模型（如随机森林）在处理结构化基因特征时通常优于单一模型。

### 5. 资源与算力
*   **文中未充分披露**。作为综述论文，它并未详细记录各原始研究的具体计算资源（如 GPU 型号或训练时长），但提到 WGS 数据处理需要较高的存储和生物信息学分析流水线支持。

### 6. 真正可信的贡献
*   **验证了跨领域可行性**：证明了 AI 模型在不同物种（人、动物、环境）之间具有一定的迁移能力。
*   **识别了关键特征**：明确了 k-mers 和 SNPs 是目前预测耐药性最有效的输入特征。
*   **强调了可解释性**：通过 SHAP 等方法，AI 发现的耐药特征与生物学实验发现的耐药基因高度吻合，增强了 AI 结论的生物学可信度。

### 7. 局限与风险
*   **数据偏差（Data Bias）**：目前绝大多数 AI 模型是用高收入国家（如欧美）的数据训练的。由于不同地区的细菌进化路径不同，这些模型直接拿到非洲或亚洲使用时，效果可能会打折扣。
*   **外部验证不足**：很多研究只在自己的数据集上跑得好，缺乏跨实验室、跨国家的盲测验证。
*   **基础设施障碍**：在中低收入国家，虽然 AI 算法不贵，但获取 DNA 序列（测序仪和试剂）的成本依然较高。
*   **黑盒风险**：深度学习模型虽然准确率高，但往往难以解释具体的生化机制，难以说服临床医生。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事计算生物学、公共卫生 AI 监测、以及关注“低资源场景下模型迁移”的 AI 研究者。
*   **后续可跟进的问题**：如何利用**联邦学习（Federated Learning）**在保护各国隐私的前提下，整合全球耐药细菌数据，训练出一个对中低收入国家更公平、更鲁棒的通用预测模型？

（完）
