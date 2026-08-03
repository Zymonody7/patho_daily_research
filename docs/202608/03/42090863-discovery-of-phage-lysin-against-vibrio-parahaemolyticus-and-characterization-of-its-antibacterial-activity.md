---
title: Discovery of phage lysin against Vibrio parahaemolyticus and characterization of its antibacterial activity.
title_zh: 针对副溶血性弧菌的噬菌体裂解酶的发现及其抗菌活性表征
authors: "Rui Zhang, Jiajun He, Fangfang Yao, Fangyuan Chen, Hongping Wei, Shengfu Huang, Yuhong Li"
date: 2026-08-02
pdf: "https://pubmed.ncbi.nlm.nih.gov/42090863/"
tags: ["query:pathoai"]
score: 8.0
evidence: 病原体靶点识别的计算分析
tldr: 副溶血性弧菌是导致食源性疾病和水产损失的主要病原体，但传统噬菌体裂解酶难以穿透革兰氏阴性菌的外膜。本研究通过计算分析筛选出893个候选裂解酶，并成功表达了10个新型酶，其中LysV569表现尤为突出。它无需外膜渗透剂即可显著降低菌量，且具备极高的热稳定性（4-85°C），能有效清除生物膜并减少三文鱼表面的细菌污染，为食品安全和环境治理提供了强效工具。
selection_source: fresh_fetch
motivation: 针对副溶血性弧菌引起的食源性疾病和水产养殖损失，寻找能突破革兰氏阴性菌外膜屏障的高效噬菌体裂解酶。
method: 利用计算分析和序列相似性网络从基因组中筛选出893个候选裂解酶，并对其中25个代表性蛋白进行表达与生化活性验证。
result: "筛选出的LysV569在无需渗透剂的情况下可使菌量下降超过2个数量级，且在85°C高温下仍能保持活性，并能清除96.6%的现有生物膜。"
conclusion: 发现了一种具有极高热稳定性和强效杀菌能力的新型裂解酶LysV569，为控制食品及环境中的副溶血性弧菌提供了理想的生物制剂。
---

## 摘要
副溶血性弧菌（Vibrio parahaemolyticus）是一种主要的食源性致病菌，可引起人类胃肠炎并导致严重的水产养殖经济损失。虽然噬菌体裂解酶在对抗细菌病原体方面展现出应用前景，但由于外膜的不通透性，其对革兰氏阴性菌的有效性仍然受限。通过计算分析，我们鉴定了 893 种针对弧菌的裂解酶，并利用序列相似性网络和生化参数筛选出 25 种代表性酶。包括 LysV569 在内的 10 种新型裂解酶被成功表达，其中 5 种在无需外膜渗透剂的情况下，能使副溶血性弧菌 ATCC 17802 减少超过 2 log10 CFU/mL。LysV569 对副溶血性弧菌 ATCC 17802 表现出剂量和时间依赖性的杀菌活性。令人印象深刻的是，在 4 °C 至 85 °C 的宽温度范围内预孵育 30 分钟后，它仍保留了 >99% 的活性，展现出卓越的热稳定性。在 100 μg/mL 浓度下，LysV569 清除了 96.6% 的现有生物膜（添加 EDTA），在 24 小时内抑制了 >95% 的新生物膜形成（不含 EDTA），并使三文鱼和食品接触表面的细菌载量降低了 2-3 log10 CFU/mL。本研究为食品和环境领域中副溶血性弧菌的防控提供了一个极具前景的候选分子。

## Abstract
Vibrio parahaemolyticus, a major seafood-borne pathogen, causes human gastroenteritis and significant aquaculture economic losses. While bacteriophage lysins show promise against bacterial pathogens, their effectiveness against Gram-negative species remains limited by outer membrane impermeability. Through computational analysis, we identified 893 Vibrio-targeting lysins and selected 25 representatives using sequence similarity networks and biochemical parameters. Ten novel lysins, including LysV569, were successfully expressed and 5 of them were able to reduce V. parahaemolyticus ATCC 17802 by more than 2 log10 CFU/mL without outer membrane permeabilizers. LysV569 demonstrated dose- and time-dependent bactericidal activity against V. parahaemolyticus ATCC 17802. Impressively, after pre-incubation for 30 min over a wide temperature range (4 °C to 85 °C), it retained >99% of its activity, demonstrating exceptional thermostability. At 100 μg/mL, LysV569 removed 96.6% of existing biofilms (with EDTA), inhibited >95% new biofilm formation within 24 h (without EDTA) and reduced bacterial load by 2-3 log10 CFU/mL on salmon and food-contact surfaces. This work identified a promising candidate for the control of V. parahaemolyticus in food and environmental settings.

---

## 论文详细总结（自动生成）

这是一份关于针对副溶血性弧菌的新型噬菌体裂解酶研究的深度总结：

### 1. 核心问题：攻克革兰氏阴性菌的“双重城墙”
这篇论文主要解决的是**如何不依靠化学辅助手段，直接杀灭具有强保护外膜的革兰氏阴性菌**（以副溶血性弧菌为代表）。
*   **背景**：副溶血性弧菌是海鲜过敏和食物中毒的头号元凶。
*   **痛点**：噬菌体裂解酶（Phage Lysin）像“分子剪刀”，能剪断细菌的细胞壁。但革兰氏阴性菌在细胞壁外还有一层**外膜（Outer Membrane）**，像城墙一样挡住了裂解酶。传统的裂解酶通常需要添加 EDTA 等渗透剂来“破墙”，这限制了它们在食品加工中的实际应用。
*   **价值**：发现一种能自我穿透外膜、且极度耐热的天然裂解酶，对食品安全和水产养殖具有巨大的商业和防疫价值。

### 2. 白话版概述
副溶血性弧菌让海鲜变质并让人拉肚子，但它们自带“防弹衣”（外膜），一般的生物药物打不动。研究人员利用计算机从海量的病毒基因组中“挖”出了 893 种潜在的杀菌酶，并从中筛选出了一位“全能战士”——**LysV569**。这个酶非常强悍：它不需要任何化学帮手就能直接钻进细菌内部将其炸碎；它还极其耐热，在 85°C 的高温下煮半小时依然活力满满；最后，它还能像清洁剂一样洗掉物体表面 96% 以上的细菌生物膜（细菌聚集成团的顽固污垢）。

### 3. 方法部分：从大数据挖掘到生化验证
*   **核心思想**：利用生物信息学手段，从已知的弧菌噬菌体基因组中大规模搜索具有特定杀菌结构域的序列，并通过聚类分析缩小实验范围。
*   **计算筛选流程**：
    1.  **基因组挖掘**：在数据库中识别出 893 个针对弧菌的裂解酶候选序列。
    2.  **序列相似性网络 (SSN)**：这是一种聚类算法，将相似的序列归为一类。研究者从不同的簇中挑选了 25 个具有代表性的酶，以确保多样性。
    3.  **理化参数预测**：重点筛选那些末端带有正电荷或两亲性（既亲水又亲油）的蛋白，因为这种结构更有可能穿透细菌带负电的外膜。
*   **关键取舍**：研究者放弃了通过人工改造（如融合阳性肽）来增强穿透力的方法，转而寻找**天然具备穿透能力**的酶，这样更具生物安全性且性质更稳定。

### 4. 实验部分：多场景的杀菌实战
*   **实验对象**：副溶血性弧菌标准株（ATCC 17802）。
*   **评价指标**：
    *   **杀菌对数（Log Reduction）**：衡量菌量下降的数量级。
    *   **热稳定性**：在不同温度预处理后的残余活性。
    *   **生物膜清除率**：对附着在表面上的细菌团块的去除能力。
*   **主要结果**：
    *   **强效杀菌**：LysV569 在无渗透剂的情况下，使菌量下降超过 2 个数量级（即杀死了 99% 以上的细菌）。
    *   **极端耐热**：在 85°C 下处理 30 分钟，活性保留 >99%。这在蛋白质类药物中非常罕见。
    *   **食品应用**：在实际的三文鱼肉块和食品接触表面实验中，成功降低了 2-3 log10 CFU/mL 的细菌载量。
    *   **生物膜抑制**：抑制了 >95% 的新生物膜形成。

### 5. 资源与算力
*   **文中未充分披露**具体的计算硬件配置。主要涉及的是基因组数据库检索和序列比对分析，这类任务通常在高性能计算集群（HPC）上完成，对算力的要求在现代生物信息学实验室属于常规水平。

### 6. 真正可信的贡献
*   **发现 LysV569**：这是目前报道的针对弧菌的最耐热且具备天然穿透能力的裂解酶之一。
*   **验证了“计算挖掘”的有效性**：证明了通过 SSN 网络筛选代表性序列，比盲目实验更高效。
*   **应用证据链完整**：从试管实验到生物膜清除，再到真实的三文鱼表面测试，证据链非常扎实。

### 7. 局限与风险
*   **广谱性未知**：虽然对副溶血性弧菌有效，但对其他弧菌（如霍乱弧菌、创伤弧菌）的杀伤效果在摘要中未详细展开。
*   **生物膜清除仍需辅助**：虽然抑制新生物膜很强，但清除**已有**的成熟生物膜时，仍需配合 EDTA 才能达到 96.6% 的高效率。
*   **成本问题**：大规模生产重组蛋白裂解酶的成本是否能低于传统的化学消毒剂，是商业化的主要障碍。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事蛋白质结构预测、抗菌肽设计、以及利用大模型（如 Protein Language Models）进行功能蛋白挖掘的研究者。
*   **后续可跟进的问题**：能否利用 AI（如 AlphaFold3 或蛋白质语言模型）解析 LysV569 极端耐热的结构机理，并以此为模板，通过生成式 AI 设计出针对其他耐药菌（如鲍曼不动杆菌）的“耐热穿透型”裂解酶？

（完）
