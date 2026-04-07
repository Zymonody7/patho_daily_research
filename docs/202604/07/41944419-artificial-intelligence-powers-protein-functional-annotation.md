---
title: Artificial Intelligence Powers Protein Functional Annotation.
title_zh: 人工智能助力蛋白质功能注释。
authors: "Wenkang Wang, Qiurong Yang, Min Zeng, Ruiqing Zheng, Min Li"
date: 2026-04-07
pdf: "https://pubmed.ncbi.nlm.nih.gov/41944419/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 用于蛋白质功能注释及GO/EC预测的AI方法
tldr: 蛋白质功能注释对理解生命过程至关重要，但传统实验方法成本高且通量低。本文系统综述了利用人工智能预测基因本体（GO）术语和酶委员会（EC）编号的计算方法，将其归纳为六大建模范式。通过对比不同方法的评估指标与应用场景，为实现更精准、高分辨率的蛋白质功能预测提供了技术路线参考，助力生物医学研究。
selection_source: fresh_fetch
motivation: 针对传统实验验证蛋白质功能效率低下且成本昂贵的问题，亟需高效的 AI 计算手段来自动标注蛋白质的生物学功能。
method: 本文将现有的蛋白质功能预测方法系统性地归纳为六种建模范式，并重点对比了针对 GO 术语和 EC 编号预测的主流 AI 模型。
result: 梳理了不同预测场景下的评估标准与挑战，展示了 AI 在处理复杂蛋白质功能关联和高分辨率标注方面的潜力。
conclusion: 总结了 AI 在蛋白质功能注释领域的最新进展，并指出未来研究应聚焦于上下文相关及更高精度的功能预测。
---

## 摘要
蛋白质功能注释对于理解生物过程、疾病机制和酶活性至关重要，但实验验证仍然成本高昂且通量较低。随着人工智能（AI）的快速发展，广泛的计算方法被提出用于推断蛋白质功能。本综述系统地考察了基因本体（GO）术语和酶学委员会（EC）编号的注释方法。这是两个互补的系统，涵盖了蛋白质功能的不同方面。基于这两个系统，我们首先在一个清晰、结构化的框架下将现有方法总结为六种通用的建模范式。随后，我们以并行的方式介绍了 GO 和 EC，包括代表性方法、常用评估指标、预测场景以及特定任务的挑战。最后，我们概述了新兴机遇和未来方向，旨在实现更准确、上下文相关且高分辨率的蛋白质功能注释。

## Abstract
Protein functional annotation is essential for understanding biological processes, disease mechanisms, and enzyme activities, yet experimental validation remains costly and low-throughput. With the rapid development of Artificial Intelligence (AI), a wide range of computational approaches have been proposed to infer protein functions. This review systematically examines methods for annotating Gene Ontology (GO) terms and Enzyme Commission (EC) numbers. These are two complementary systems that capture different aspects of protein functions. Based on these two systems, we first synthesize existing approaches into six general modeling paradigms with a clear, structured framework. Then, we introduce GO and EC in a parallel manner, consisting of representative methods, commonly used evaluation metrics, prediction scenarios, and task-specific challenges. Finally, we outline emerging opportunities and future directions aimed at achieving more accurate, context-dependent, and high-resolution protein functional annotation.

---

## 论文详细总结（自动生成）

这篇综述论文《Artificial Intelligence Powers Protein Functional Annotation》（人工智能助力蛋白质功能注释）系统性地总结了 AI 在预测蛋白质功能领域的最新进展。以下是该论文的详细结构化总结：

### 1. 解决的问题与核心价值
*   **核心问题**：随着基因测序技术爆发，人类掌握了海量的蛋白质序列，但其中绝大部分蛋白质的**功能（Function）**尚不明确。传统的实验室验证（如生化实验）虽然准确，但成本极高、速度极慢，无法处理海量数据。
*   **研究价值**：蛋白质是生命的执行者。搞清楚它们的功能，对于**新药研发、疾病机制理解、工业酶设计**（如降解塑料的酶）至关重要。本文为 AI 研究者提供了一套完整的“技术地图”，梳理了如何利用算法自动给蛋白质“贴标签”。

### 2. 白话版概述
想象蛋白质是一本用“氨基酸字母”写成的书。以前我们需要生物学家读完一本书并做实验才能知道它是讲什么的（功能注释）。现在，AI 就像一个超级阅读器：
1.  它通过阅读文字（**序列**）或观察书的装订形状（**结构**）来猜内容。
2.  它主要解决两个任务：**GO 注释**（给蛋白质打上“它是干嘛的”、“在细胞哪呆着”等通用标签）和 **EC 编号**（给作为“生物催化剂”的酶分配具体的化学反应编号）。
3.  这篇论文总结了目前 AI 读这些“书”的六种主要套路。

### 3. 方法部分：六大建模范式
论文将现有的 AI 预测方法归纳为六种核心范式：
*   **基于序列（Sequence-based）**：将蛋白质看作一维字符串，利用 CNN、RNN 或 Transformer 提取特征。
*   **基于结构（Structure-based）**：利用 AlphaFold 等预测的 3D 坐标，通过图神经网络（GNN）捕捉空间几何特征。
*   **基于网络（Network-based）**：利用蛋白质与蛋白质之间的相互作用网络（PPI），认为“邻居”的功能往往相似。
*   **基于文本（Text-based）**：从已有的科学文献中通过 NLP 技术挖掘蛋白质的功能描述。
*   **多模态融合（Hybrid/Multi-modal）**：同时结合序列、结构、网络等多种信息进行综合判断。
*   **预训练模型（Pre-trained Models）**：利用类似 BERT/GPT 的思路，在数亿条无标注序列上进行自监督学习（如 ESM 系列），再微调到功能预测任务上。

### 4. 实验与评估
*   **核心任务**：
    *   **GO 预测**：多标签分类任务，标签之间存在层级关系（树状或有向无环图）。
    *   **EC 预测**：层次化分类任务，通常分为四级编号（如 1.1.1.1），越往后越精确。
*   **常用数据**：UniProt（蛋白质数据库）、PDB（结构数据库）、CAFA 挑战赛数据集。
*   **评价指标**：
    *   **F-max**：考虑了层级结构的最大 F1 分数。
    *   **AUPR**：精确率-召回率曲线下面积。
    *   **S-min**：基于本体结构的语义距离（衡量预测错得有多离谱）。
*   **主要结论**：目前**蛋白质语言模型（pLMs）**结合**结构信息**的方法表现最强，尤其是在处理“低同源性”（即长得不像已知蛋白）的样本时，AI 显著优于传统的序列比对方法（如 BLAST）。

### 5. 资源与算力
*   **文中未充分披露**：作为综述论文，本文未提供具体的模型训练算力消耗（如 GPU 小时数），但指出预训练模型（如 ESM-2）需要大规模计算集群，而下游微调任务在单张商用显卡上即可完成。

### 6. 真正可信的贡献
*   **系统性分类**：首次将 GO 和 EC 预测任务在同一框架下进行并行对比，清晰定义了六大建模范式。
*   **挑战总结**：明确指出了“长尾分布”问题（少数功能标签有大量数据，多数标签数据极少）是目前制约 AI 准确性的核心瓶颈。
*   **趋势预测**：强调了从“静态功能预测”向“上下文相关（如不同组织、不同 pH 值下）功能预测”转变的必要性。

### 7. 局限与风险
*   **数据偏差**：现有的训练集严重偏向于人类、小鼠等“模式生物”，对于极端环境微生物或罕见蛋白的预测可能失效。
*   **黑盒性质**：AI 虽然能预测出功能标签，但往往无法解释蛋白质序列中哪些关键位点（残基）决定了该功能，这对湿实验验证的指导意义有限。
*   **实验验证滞后**：AI 预测出的新功能往往缺乏及时的实验闭环验证，存在“假阳性”风险。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事蛋白质工程、药物靶点发现、以及对大模型在生物学应用感兴趣的 AI 研究员。
*   **后续可跟进的问题**：如何利用大语言模型（LLM）的推理能力，结合蛋白质结构，实现**零样本（Zero-shot）**或**少样本**的新型酶功能设计？

（完）
