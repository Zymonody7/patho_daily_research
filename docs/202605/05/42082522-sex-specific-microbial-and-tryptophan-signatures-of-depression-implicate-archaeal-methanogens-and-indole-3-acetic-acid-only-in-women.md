---
title: Sex-specific microbial and tryptophan signatures of depression implicate archaeal methanogens and indole-3-acetic acid only in women.
title_zh: 抑郁症的性别特异性微生物和色氨酸特征表明，古菌产甲烷菌和吲哚-3-乙酸仅与女性相关
authors: "Anna Motger-Albertí, Laura Gallardo-Nuell, Marisel Rosell-Díaz, Mihaela Stefoglo, Javier Pons, Josep Garre-Olmo, Vicente Pérez-Brocal, Andrés Moya, Josep Puig, Rafael Ramos, Jordi Mayneris-Perxachs, José Manuel Fernández-Real"
date: 2026-05-04
pdf: "https://pubmed.ncbi.nlm.nih.gov/42082522/"
tags: ["query:pathoai"]
score: 8.0
evidence: 机器学习用于微生物组-宿主代谢物相互作用及抑郁严重程度预测
tldr: 抑郁症在性别上存在显著差异，但其背后的肠道菌群与代谢物机制尚不明确。本研究通过分析大规模人群队列的血浆色氨酸代谢物、抑郁评分及肠道微生物组，利用机器学习模型发现：在女性中，抑郁程度与产甲烷古菌（如史氏甲烷短杆菌）及吲哚-3-乙酸（IAA）代谢密切相关，而男性则表现出不同的代谢特征。这一发现揭示了抑郁症发病机制的性别二元性，为精准医疗提供了新靶点。
selection_source: fresh_fetch
motivation: 旨在探究肠道微生物与宿主代谢物交互作用如何导致抑郁症在男性和女性之间表现出不同的生物学特征。
method: 基于 802 名受试者的队列数据，结合血浆色氨酸代谢分析、肠道微生物组测序以及带有 SHAP 解释值的机器学习模型，评估性别特异性的抑郁关联因素。
result: 研究发现女性抑郁严重程度与史氏甲烷短杆菌等产甲烷古菌及 IAA 代谢呈正相关，而男性抑郁仅与犬尿喹啉酸（KA）呈负相关。
conclusion: 抑郁症的微生物与代谢机制具有显著的性别差异，女性特有的古菌-色氨酸代谢轴可能成为未来性别差异化治疗的关键。
---

## 摘要
心理健康中的性别差异经常被忽视，然而肠道微生物群与宿主代谢物的相互作用可能导致抑郁症的性别二态性。在一个基于人群的队列中，我们在控制了吸烟、饮食、饮酒和体力活动后，研究了血浆色氨酸代谢物、抑郁症状（PHQ-9）与肠道微生物组之间的性别特异性联系。与男性（N = 383）相比，女性（N = 419）表现出更高的血浆吲哚-3-乙酸（IAA）和吡啶甲酸（PA）浓度，但葫芦巴碱（TRIG）浓度较低。带有 SHAP 解释的机器学习模型显示，在女性中，IAA 和 TRIG 与抑郁严重程度呈正相关，而 PA 与之呈负相关；而在男性中，仅犬尿喹啉酸（KA）与之呈负相关。在女性中，抑郁严重程度与产甲烷古菌（包括史氏甲烷短杆菌 Methanobrevibacter smithii）以及微生物产甲烷途径强烈相关。甲烷短杆菌属（特别是史氏甲烷短杆菌）与色氨酸、PA 和 KA 生物合成基因呈负相关，但与 IAA 以及烟酸/烟酰胺代谢基因呈正相关。预测大多数与女性抑郁严重程度相关的微生物物种都能产生 IAA。这些发现揭示了显著的性别特异性微生物组-代谢物相互作用，突显了塑造男女抑郁症的潜在不同微生物机制。

## Abstract
Sex differences in mental health are often overlooked, yet gut microbiota-host metabolite interactions may contribute to sexual dimorphism in depression. In a population-based cohort, we investigated sex-specific links among plasma tryptophan metabolites, depressive symptoms (PHQ-9), and the gut microbiome, controlling for smoking, diet, alcohol, and physical activity. Women (N = 419) exhibited higher plasma indole-3-acetic acid (IAA) and picolinic acid (PA) concentrations, but lower trigonelline (TRIG) than men (N = 383). Machine learning models with SHAP explanations revealed that IAA and TRIG were positively associated, whereas PA was negatively associated with depression severity in women, whereas only kynurenic acid (KA) was inversely associated in men. In women, depression severity strongly correlated with methanogenic archaea, including Methanobrevibacter smithii, and microbial methane-production pathways. Methanobrevibacter and specifically M. smithii were negatively linked to genes for tryptophan, PA, and KA biosynthesis, but positively to genes for IAA and nicotinate/nicotinamide metabolism. Most microbial species associated with depression severity in women were predicted to produce IAA. These findings reveal pronounced sex-specific microbiome-metabolite interactions, highlighting potentially distinct microbial mechanisms shaping depression in men and women.

---

## 论文详细总结（自动生成）

这是一份关于论文《Sex-specific microbial and tryptophan signatures of depression implicate archaeal methanogens and indole-3-acetic acid only in women》的深度解析总结：

### 1. 这篇论文到底在解决什么问题，为什么值得看？
抑郁症在发病率、症状和治疗反应上存在显著的**性别差异**（女性发病率通常是男性的两倍），但过去的研究往往将男女数据混合分析，掩盖了底层的生物学差异。

这篇论文的价值在于：它利用**多组学（Multi-omics）**数据，揭示了肠道微生物与宿主代谢（特别是色氨酸代谢路径）在抑郁症中的“性别二元性”。它首次指出，某些特定的微生物（如产甲烷古菌）和代谢产物（如 IAA）仅在女性抑郁患者中表现出强相关性。

---

### 2. 白话版概述
肠道被称为人的“第二大脑”，肠道菌群会分解食物中的色氨酸（一种氨基酸），产生影响大脑情绪的化学物质。研究发现，男女抑郁的“肠道工厂”运作方式完全不同：
*   **女性：** 抑郁程度越高，肠道里的“产甲烷古菌”（产生甲烷的微生物）就越多，且血液中一种叫 IAA 的代谢物水平也越高。
*   **男性：** 抑郁主要与另一种叫 KA（犬尿喹啉酸）的代谢物减少有关。
这意味着，未来治疗抑郁症可能需要根据性别“分男版和女版”来调理肠道菌群。

---

### 3. 方法部分
*   **核心思想：** 采用“性别分层”的分析策略，结合机器学习算法，从海量的微生物物种和代谢物中筛选出对抑郁评分（PHQ-9）贡献最大的特征。
*   **模型结构：** 使用了基于**SHAP（SHapley Additive exPlanations）**解释值的机器学习模型。SHAP 是一种博弈论方法，能定量解释模型中每个特征（如某种细菌或代谢物）对预测抑郁严重程度的具体贡献度。
*   **关键设计取舍：** 
    *   **协变量控制：** 严格控制了吸烟、饮食、酒精和体力活动等干扰因素，确保发现的关联不是因为生活习惯差异导致的。
    *   **功能预测：** 不仅看“有哪些菌”，还通过基因组预测这些菌“能干什么”（如是否具备合成 IAA 的酶）。

---

### 4. 实验部分
*   **数据：** 802 名受试者（419 名女性，383 名男性）的真实人群队列。
*   **任务：** 预测 PHQ-9 抑郁量表评分。
*   **评价指标：** 代谢物浓度、微生物相对丰度、SHAP 贡献值、相关系数（Spearman）。
*   **主要结果：**
    1.  **代谢物差异：** 女性抑郁严重程度与 **IAA（吲哚-3-乙酸）** 呈正相关；男性则与 **KA（犬尿喹啉酸）** 呈负相关。
    2.  **微生物差异：** 仅在女性中发现抑郁与**史氏甲烷短杆菌（*Methanobrevibacter smithii*）**及产甲烷通路强相关。
    3.  **因果暗示：** 预测显示，女性肠道中与抑郁相关的多数细菌都具备产生 IAA 的能力，形成了一个“菌群-IAA-抑郁”轴。

---

### 5. 资源与算力
*   **文中未充分披露。**（此类研究通常涉及宏基因组测序数据处理，需高性能计算集群，但机器学习建模部分在常规工作站即可完成。）

---

### 6. 这篇论文真正可信的贡献是什么？
*   **打破“细菌中心论”：** 过去肠道研究多关注细菌，本文证明了**古菌（Archaea）**——这一类常被忽视的微生物，在女性精神健康中可能扮演关键角色。
*   **代谢通路的性别特异性：** 证据最强的是 IAA 和 KA 在男女抑郁中截然相反的预测作用，这为“精准精神医学”提供了坚实的代谢组学证据。

---

### 7. 局限与风险
*   **相关性非因果性：** 这是一个横断面研究（Cross-sectional），目前只能说这些菌和抑郁“同时出现”，无法确定是菌群导致了抑郁，还是抑郁后的生理变化改变了菌群。
*   **地域局限：** 样本来自特定人群，肠道菌群受饮食和地理影响极大，结论是否适用于全球其他族裔尚待验证。
*   **IAA 的双刃剑：** IAA 在植物中是生长素，在人体中的具体神经毒性或保护机制仍不完全清晰。

---

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群：** 从事多组学数据融合、可解释机器学习（XAI）、以及精神疾病生物标记物开发的 AI 研究者。
*   **后续可跟进的问题：** 能否利用这些性别特异性的微生物特征，训练一个跨人群通用的抑郁症辅助诊断分类器？或者利用强化学习模拟干预特定菌群后，代谢网络如何恢复平衡？

（完）
