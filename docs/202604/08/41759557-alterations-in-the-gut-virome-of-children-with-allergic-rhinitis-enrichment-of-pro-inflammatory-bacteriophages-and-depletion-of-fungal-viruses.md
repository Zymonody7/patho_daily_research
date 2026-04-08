---
title: "Alterations in the gut virome of children with allergic rhinitis: enrichment of pro-inflammatory bacteriophages and depletion of fungal viruses."
title_zh: 过敏性鼻炎儿童肠道病毒组的变化：促炎噬菌体的富集与真菌病毒的减少
authors: "Wei Yang, Lindong Shi, Xiuyun Li, Fuguang Rao, Rongrong Luo, Congfu Huang"
date: 2026-04-07
pdf: "https://pubmed.ncbi.nlm.nih.gov/41759557/"
tags: ["query:pathoai"]
score: 8.0
evidence: 宏基因组测序和随机森林用于病毒组分析
tldr: 过敏性鼻炎（AR）的发病机制尚不完全明确，且肠道病毒组的作用研究较少。本研究通过对16名AR患儿和17名健康儿童的粪便样本进行宏基因组测序，分析了病毒组的多样性及与免疫指标的关系。结果发现AR患儿肠道中促炎性噬菌体显著增加且与IgE水平正相关，而真菌病毒则显著减少。这一发现揭示了病毒组在调节Th2免疫中的潜在作用，为AR的诊断和噬菌体疗法提供了新思路。
selection_source: fresh_fetch
motivation: 旨在探索肠道病毒组（Virome）在儿童过敏性鼻炎发病中的组成变化及其与宿主免疫标志物、过敏原之间的相互作用关系。
method: 对33名儿童的粪便样本进行宏基因组测序，利用BLASTP进行病毒基因注释，并结合LEfSe差异分析、随机森林分类器及Spearman相关性分析评估病毒组特征。
result: 发现AR患儿肠道中Taranisvirus等促炎噬菌体显著富集并与总IgE水平正相关，而Mitovirus等真菌病毒则显著减少，且病毒-细菌共发生网络呈现出以促噬菌体为中心的生态重构。
conclusion: 肠道病毒组失调（促炎噬菌体增加与保护性真菌病毒减少）可能通过调节Th2免疫反应参与过敏性鼻炎的病理过程，为开发新型病毒组诊断工具和噬菌体疗法提供了理论依据。
---

## 摘要
本研究旨在表征过敏性鼻炎（AR）儿童的肠道病毒组，并探讨其与免疫标志物及过敏原的相互作用。对16名AR儿童和17名健康对照（HC）儿童的粪便样本进行了宏基因组测序。利用BLASTP比对NCBI NR数据库对病毒基因（VGs）进行了鉴定和分类注释。通过LEfSe、随机森林和Spearman相关性分析了病毒组多样性、

## Abstract
This study aimed to characterize the gut virome in children with allergic rhinitis (AR) and explore its interactions with immune markers and allergens. Metagenomic sequencing was performed on fecal samples from 16 AR and 17 healthy control (HC) children. Viral genes (VGs) were identified and taxonomically annotated using BLASTP against the NCBI NR database. Virome diversity, differential abundance, and correlations with IgE were analyzed using LEfSe, random forest, and Spearman correlation. While alpha diversity did not differ, beta diversity revealed subtle compositional trends. Taranisvirus was enriched in AR and positively correlated with total IgE (ρ = 0.4647, P = 0.045). Mitovirus and Duamitovirus were depleted in AR and negatively correlated with allergens. Virus-bacteria co-occurrence network analysis revealed a reconfigured ecological interactome in AR, characterized by pro-phage-centric associations that may disrupt mucosal immune homeostasis. Random forest identified total IgE, milk, and dust mite as top discriminators. This first study of the gut virome in pediatric AR reveals a pro-inflammatory phage enrichment and protective fungal virus depletion, implicating the virome in modulating Th2 immunity. These findings suggest a potential correlation between virome alterations and allergic diseases, which may inform future research on virome-targeted interventions.IMPORTANCEAllergic rhinitis is a prevalent childhood condition with a significant impact on quality of life, yet its pathogenesis is not fully understood. While the bacterial microbiome has been studied, the role of the gut virome remains largely unexplored. Our study provides the first evidence of gut virome dysbiosis in children with allergic rhinitis. We identified specific pro-inflammatory bacteriophages that are enriched and correlated with IgE levels, as well as protective fungal viruses that are depleted. These findings offer new perspectives on allergic disease pathogenesis by suggesting a potential role of the virome in modulating host immunity. This work not only opens a new avenue for understanding the environmental and microbial drivers of allergic diseases but also suggests the potential for novel virome-based diagnostics and therapeutic strategies, such as phage therapy, which could have a broad impact on clinical practice.This study is registered with ClinicalTrials.gov as ChiCTR2400085982.

---

## 论文详细总结（自动生成）

这篇论文研究了儿童过敏性鼻炎（AR）与肠道病毒组（Virome）之间的关系。以下是详细的结构化总结：

### 1. 解决的问题与研究价值
*   **核心问题**：过敏性鼻炎（AR）是儿童常见的慢性炎症，虽然已知肠道“细菌”失调与之有关，但肠道中的“病毒”（主要是噬菌体和真菌病毒）在其中扮演什么角色，此前几乎是研究空白。
*   **研究价值**：这是首个揭示儿童 AR 肠道病毒组特征的研究。它发现病毒组的失调（某些病毒变多，某些变少）可能通过调节免疫反应（如 Th2 免疫）来驱动过敏，这为未来通过“噬菌体疗法”或病毒标志物诊断过敏性疾病提供了新思路。

### 2. 白话版概述
简单来说，研究人员对比了过敏患儿和健康孩子的粪便样本。他们发现，过敏患儿肠道里那些“爱挑事”的促炎噬菌体（专门感染细菌的病毒）变多了，而一些具有保护作用的真菌病毒却减少了。更重要的是，这些病毒的变化与血液中代表过敏程度的指标（IgE）直接相关。这意味着，肠道里的病毒生态失衡，可能是导致孩子过敏的幕后推手之一。

### 3. 方法部分
*   **核心思想**：利用宏基因组测序技术，对粪便中的所有遗传物质进行“地毯式”搜索，从中提取出病毒的基因序列，并分析这些病毒的种类、功能及其与宿主免疫指标的关联。
*   **技术流程**：
    1.  **样本采集**：收集 16 名 AR 患儿和 17 名健康儿童（HC）的粪便。
    2.  **测序与比对**：通过宏基因组测序获取数据，利用 **BLASTP** 工具对比 NCBI 数据库，鉴定出病毒基因（VGs）。
    3.  **差异分析**：使用 **LEfSe**（一种统计学方法，用于寻找组间差异最显著的生物特征）找出 AR 组特有的病毒。
    4.  **分类与预测**：构建 **随机森林（Random Forest）** 分类模型，评估哪些病毒或临床指标（如 IgE、过敏原）对区分 AR 和健康组贡献最大。
    5.  **关联分析**：使用 **Spearman 相关性分析** 建立病毒、细菌与临床指标（如尘螨过敏、牛奶过敏）之间的网络关系。

### 4. 实验部分
*   **数据规模**：33 名儿童（16 AR vs 17 HC）。
*   **评价指标**：Alpha/Beta 多样性（衡量病毒种类丰富度和组成差异）、病毒丰度、总 IgE 水平（过敏指标）。
*   **主要结果**：
    *   **促炎病毒富集**：AR 组中 *Taranisvirus* 等噬菌体显著增加，且其丰度与总 IgE 水平呈正相关（ρ = 0.4647）。
    *   **保护性病毒减少**：*Mitovirus* 和 *Duamitovirus*（真菌病毒）在 AR 组中显著减少，且与过敏原呈负相关。
    *   **生态重构**：AR 患儿的病毒-细菌共发生网络发生了变化，呈现出以“促炎噬菌体”为中心的结构，可能破坏了肠道黏膜的免疫平衡。
    *   **分类表现**：随机森林模型识别出总 IgE、牛奶过敏和尘螨过敏是区分两组的最关键特征。

### 5. 资源与算力
*   **文中未充分披露**：论文未详细说明具体的计算集群配置或训练时长，仅提到使用了标准的生物信息学分析流程和相关的开源数据库（如 NCBI NR）。

### 6. 真正可信的贡献
*   **首次发现**：确证了 AR 儿童肠道病毒组存在失调（Dysbiosis）。
*   **强证据链**：不仅发现了病毒种群的变化，还通过相关性分析将 *Taranisvirus* 丰度与临床金标准（IgE 水平）挂钩，增强了结论的可信度。
*   **新视角**：提出了“真菌病毒”在过敏性疾病中的潜在保护作用，这在以往研究中极少被提及。

### 7. 局限与风险
*   **样本量较小**：仅 33 例样本，属于探索性小规模研究，结论需在大规模人群中验证。
*   **因果关系不明**：作为横断面研究，无法确定是“病毒失调导致了过敏”，还是“过敏体质改变了肠道病毒环境”。
*   **地域局限性**：单中心研究，不同地区、饮食习惯的儿童肠道病毒组可能存在巨大差异。
*   **技术限制**：宏基因组测序对低丰度病毒的捕捉能力有限，可能遗漏了一些重要的稀有病毒。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事多维组学数据融合、微生物组预测模型、以及寻找新型生物标志物的 AI 研究者。
*   **后续可跟进的问题**：能否利用深度学习（如 Graph Neural Networks）更好地建模“病毒-细菌-宿主免疫”这种复杂的三方交互网络，从而实现比随机森林更精准的过敏风险预测？

（完）
