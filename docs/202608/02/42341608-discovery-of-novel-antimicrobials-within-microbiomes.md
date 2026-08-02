---
title: Discovery of novel antimicrobials within microbiomes.
title_zh: 在微生物组中发现新型抗菌药物
authors: "Erez Weisberg, Aya Friedman, Cesar de la Fuente-Nunez, Asaf Levy"
date: 2026-08-01
pdf: "https://pubmed.ncbi.nlm.nih.gov/42341608/"
tags: ["query:pathoai"]
score: 9.0
evidence: 人工智能赋能的抗菌药物发现计算方法
tldr: 针对抗生素耐药性病原体威胁及新药研发滞后的现状，本文综述了利用基因组大数据从人类及各类微生物组中挖掘新型抗菌药物的进展。重点介绍了如何利用人工智能计算方法与创新实验策略，从海量数据中精准识别生物合成基因簇、抗菌肽及蛋白质。这些技术不仅加速了针对重点病原体的小分子与蛋白质药物发现，还揭示了新的作用机制，为应对耐药性危机提供了关键的技术路径。
selection_source: fresh_fetch
motivation: 细菌和真菌的抗生素耐药性演变速度远超新药研发速度，亟需从微生物组中寻找新的抗菌候选药物。
method: 综述了利用基因组挖掘、人工智能算法及创新实验策略，从人类及环境微生物组中提取生物合成基因簇和抗菌肽的方法。
result: AI 驱动的计算方法显著提升了候选药物的筛选效率，成功识别出多种针对高优先级病原体的新型活性分子及其作用机制。
conclusion: 基因组大数据与 AI 的结合是发现新型抗菌药物的关键，未来应特别加强对临床急需的抗真菌药物的研发投入。
---

## 摘要
耐药性细菌和真菌病原体对公共卫生构成了严重威胁。新型抗菌药物的发布速度远慢于耐药性出现的速度。然而，在过去的十年中，基因组大数据革命催化了抗菌药物发现领域的重大进展。在此，我们简要综述了如何挖掘人类及其他微生物组，以准确提取生物合成基因簇以及抗菌肽和蛋白质，并重点关注后者。除了传统方法外，人工智能赋能的计算方法和创新的实验策略正越来越多地被用于筛选候选药物、鉴定针对重点病原体具有活性的新型小分子和蛋白质，并揭示新的作用机制。鉴于治疗类别有限且研发管线补充缓慢，我们强调了扩大抗真菌药物发现的紧迫性。

## Abstract
Antimicrobial-resistant bacterial and fungal pathogens constitute a severe threat to public health. The pace at which new antimicrobials are being released is far slower than the pace of resistance emergence. Over the last decade, however, the genomics big data revolution has catalyzed major advances in antimicrobial discovery. Here, we briefly review how different human and other microbiomes have been mined to accurately extract biosynthetic gene clusters and antimicrobial peptides and proteins, with a focus on the latter groups. In addition to classical methods, artificial intelligence-enabled computational methods and innovative experimental strategies are increasingly used to prioritize candidates, identify novel small molecules and proteins active against priority pathogens, and reveal new modes of action. We highlight the urgent need to expand antifungal discovery, given the limited number of therapeutic classes and the slow pace of pipeline replenishment.

---

## 论文详细总结（自动生成）

这是一份关于论文《Discovery of novel antimicrobials within microbiomes》（在微生物组中发现新型抗菌药物）的深度解析：

### 1. 这篇论文到底在解决什么问题，为什么值得看？
*   **核心问题**：抗生素耐药性（AMR）危机。细菌和真菌进化出耐药性的速度，远快于人类研发新药的速度。
*   **关注点**：传统的“试错法”找药太慢。本文综述了如何利用**微生物组（Microbiome）**这个巨大的天然宝库，通过**人工智能（AI）和大数据挖掘**，从海量的基因序列中快速定位并合成新的抗菌分子。
*   **价值**：对于 AI 研究者，它展示了如何将 NLP（自然语言处理）和生成式模型应用于生物序列分析，将原本需要数年的实验室筛选缩短到计算机上的秒级运算。

### 2. 白话版概述
地球上的微生物为了生存，彼此之间一直在进行“化学战争”，它们会分泌一些小分子或蛋白质（抗菌肽）来杀死竞争对手。人类的肠道、皮肤以及土壤中就藏着无数这种天然武器的“设计图”（基因序列）。过去我们看不懂这些图纸，但现在通过 AI，我们可以像在搜索引擎里搜关键词一样，从成千上万个微生物基因组中，精准找出那些能杀菌的“设计图”，然后在实验室里把它制造出来，变成救命的新药。

### 3. 方法部分：核心思想与 AI 路径
论文重点介绍了两种从基因组数据中挖掘药物的 AI 路径：

*   **核心思想**：将生物序列（DNA 或氨基酸）视为一种“语言”，利用机器学习模型识别具有抗菌功能的特定模式。
*   **路径 A：挖掘生物合成基因簇 (BGCs)**
    *   **背景**：BGC 是细菌基因组中一组邻近的基因，它们像流水线一样协同工作，生产复杂的抗菌小分子。
    *   **AI 应用**：使用隐马尔可夫模型 (HMM) 或深度学习（如 CNN、GNN）来识别基因组中的“基因工厂”边界，预测它们产出的分子结构。
*   **路径 B：挖掘抗菌肽 (AMPs)**
    *   **背景**：抗菌肽是短的蛋白质片段，像“纳米子弹”一样直接打穿细菌膜。
    *   **模型结构**：
        *   **判别模型**：利用循环神经网络 (RNN) 或 Transformer 评估一个给定的氨基酸序列是否有毒性、是否稳定、是否能杀菌。
        *   **生成模型**：利用变分自编码器 (VAE) 或生成对抗网络 (GAN) 甚至大语言模型 (LLM) 的微调版本，直接“写出”自然界不存在的新型抗菌肽序列。
*   **关键设计取舍**：在“搜索现有自然序列”与“生成全新人工序列”之间寻找平衡。前者更安全（自然界验证过），后者潜力更大（可能突破现有耐药机制）。

### 4. 实验部分：数据与成果
由于这是一篇综述，它总结了近年来该领域的多个关键实验成果：
*   **数据来源**：人类微生物组计划 (HMP)、全球土壤/海洋元基因组数据库。
*   **关键任务**：
    1.  **识别**：从数百万个未知基因中筛选出具有抗菌潜力的序列。
    2.  **验证**：通过化学合成并在培养皿中测试对金黄色葡萄球菌等“超级细菌”的杀伤力。
*   **主要结果**：
    *   提到了一些由 AI 辅助发现的明星分子（如 **Clovibactin**），它们具有全新的杀菌机制，细菌很难对其产生耐药性。
    *   AI 设计的抗菌肽在小鼠实验中表现出与传统抗生素相当甚至更优的疗效，且毒副作用更低。

### 5. 资源与算力
*   **文中未充分披露**：作为综述文章，未详细列出具体的 GPU 型号或训练时长。但文中提到的相关研究通常依赖于高性能计算集群（HPC）来处理 PB 级的元基因组数据。

### 6. 这篇论文真正可信的贡献
1.  **确认了 AI 的筛选效率**：证明了 AI 可以将候选药物的搜索空间缩小几个数量级，显著降低实验成本。
2.  **强调了“暗物质”挖掘**：指出微生物组中 99% 的微生物无法在实验室培养，但 AI 可以直接分析它们的 DNA，从而发现以前无法触及的药物。
3.  **抗真菌药物的预警**：明确指出目前抗真菌药物极度匮乏，呼吁 AI 研究者将注意力从细菌转向更复杂的真菌病原体。

### 7. 局限与风险
*   **湿实验瓶颈**：AI 可以在一秒钟内预测一万个候选药，但实验室验证一个药可能需要一个月。计算与实验之间的通量极度不匹配。
*   **毒性预测难题**：很多分子能杀细菌，但也会杀伤人体细胞。目前 AI 对“选择性毒性”的预测准确率仍有待提高。
*   **数据偏差**：现有的训练数据库（如 APD, CAMP）规模仍然较小，且存在严重的类不平衡问题，限制了 AI 的泛化能力。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：对蛋白质工程、生成式 AI（AIGC）、序列建模感兴趣的 AI 研究者。
*   **后续可跟进的问题**：如何利用**多模态学习**（结合蛋白质序列与 3D 结构信息）来提高抗菌活性的预测精度？如何通过 AI 设计出能针对特定致病菌而不伤害肠道益生菌的“精准抗生素”？

（完）
