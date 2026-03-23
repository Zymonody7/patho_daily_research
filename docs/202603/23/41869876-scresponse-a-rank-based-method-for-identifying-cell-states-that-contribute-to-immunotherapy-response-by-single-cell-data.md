---
title: "scResponse: A Rank-Based Method for Identifying Cell States That Contribute to Immunotherapy Response by Single-Cell Data."
title_zh: scResponse：一种基于秩的方法，用于通过单细胞数据识别对免疫治疗反应有贡献的细胞状态
authors: "Qi Dong, Haijun Huang, Yuxiu Wang, Bo Jiang, Yuzheng Chen, Huanhuan Xu, Jing Ren, Shengnan Guo, Tianhao Li, Mingjie Zhang, Tianyu Zhai, Wenbo Yang, Kaidong Liu, Cheng Lyu, Jingxuan Kang, Mingshuo Zhang, Yupeng Lu, Binghui Si, Shujun Cao, Dandan Xu, Zong Chen, Dapeng Hao"
date: 2026-03-23
pdf: "https://pubmed.ncbi.nlm.nih.gov/41869876/"
tags: ["query:seqai"]
score: 8.0
evidence: 利用单细胞数据识别有助于免疫治疗反应的细胞状态的算法
tldr: 针对免疫治疗中患者响应差异大且缺乏单细胞分辨率评估工具的问题，本研究开发了基于秩次的算法 scResponse。该方法能量化单细胞对免疫治疗的响应程度，揭示了巨噬细胞极化、T细胞耗竭等多种细胞状态对疗效的影响。通过跨癌症分析，研究发现了调控肿瘤细胞响应的关键代谢通路，并通过实验验证了其作为免疫治疗增敏靶点的潜力，为精准医疗提供了新工具。
selection_source: fresh_fetch
motivation: 现有的单细胞分析缺乏有效手段来精确量化不同细胞状态对免疫治疗响应的贡献，限制了对治疗耐药机制的深入理解。
method: 开发了名为 scResponse 的秩次算法，通过单细胞转录组数据量化细胞层面的治疗响应得分，并关联特定的生物学过程。
result: 识别出影响疗效的关键细胞亚型状态（如 CD8+ T 细胞终末耗竭）以及调控肿瘤响应的代谢通路（如乙醛酸和二羧酸代谢增敏，视黄醇代谢抑制）。
conclusion: scResponse 为解析免疫治疗响应的细胞异质性提供了高效工具，有助于发现新的治疗靶点和制定个性化的增敏策略。
---

## 摘要
免疫治疗在癌症治疗中展现出巨大潜力，但许多患者仍无法获得长期疗效。单细胞测序是理解细胞多样性如何影响治疗结果的强大技术；然而，目前仍缺乏在单细胞分辨率下评估免疫治疗疗效的稳健方法。在本研究中，我们提出了 scResponse，这是一种量化单细胞对免疫治疗反应的高效算法。scResponse 捕捉了多种细胞亚型和状态对免疫治疗疗效的细微影响，包括血管细胞的血管正常化状态、巨噬细胞极化、CD8+ T 细胞的终末耗竭，以及不同成纤维细胞亚型的相反影响。通过将治疗反应与单细胞状态联系起来，scResponse 能够描绘不同的生物过程如何塑造细胞状态，从而驱动不同的治疗结果。跨癌症的整合分析确定了与肿瘤细胞反应状态相关的关键代谢途径，包括作为免疫治疗增敏因素的乙醛酸和二羧酸代谢，以及作为抑制因素的视黄醇代谢。作为概念验证，乙醛酸和视黄醇代谢的相反作用通过肿瘤-CD8+ T 细胞共培养实验和体内小鼠模型得到了验证。因此，scResponse 是将免疫治疗疗效映射到单细胞状态的有效工具，为开发新型免疫治疗增敏策略提供了机制见解和靶点发现。

## Abstract
Immunotherapy has shown great promise in cancer treatment, yet many patients fail to achieve long-term efficacy. Single-cell sequencing is a powerful technique for understanding how cellular diversity affects treatment outcomes; however, there remains a lack of robust methods for evaluating immunotherapy efficacy at single-cell resolution. In this study, we present scResponse, an efficient algorithm that quantifies single-cell responses to immunotherapy. scResponse captures subtle influences of diverse cellular subtypes and states on immunotherapy efficacy, including the effects of vascular normalization states of vascular cells, polarization of macrophages, terminal exhaustion of CD8+ T cells, and the opposing impacts from distinct fibroblast subtypes. By linking therapeutic response to single‑cell states, scResponse enables to delineate how distinct biological processes shape cellular states to drive divergent therapeutic outcomes. Integrated analysis across cancers identified key metabolic pathways associated with responsive states of tumor cells, including glyoxylate and dicarboxylate metabolism as immunotherapy-sensitizing and retinol metabolism as suppressing it. As a proof-of-concept, the opposing roles of glyoxylate and retinol metabolism was validated using tumor‑CD8+ T cell co-culture assays and in vivo mouse models. Thus, scResponse is an effective tool for mapping immunotherapy efficacy to single-cell states, enabling mechanistic insights and target discovery for developing novel immunotherapy sensitization strategies.

---

## 论文详细总结（自动生成）

这是一份关于论文《scResponse: A Rank-Based Method for Identifying Cell States That Contribute to Immunotherapy Response by Single-Cell Data》的结构化总结：

### 1. 解决的问题与研究意义
**核心问题：** 免疫治疗（如 PD-1 抑制剂）虽然厉害，但只有少数患者有反应。科学家想知道：到底是什么样的细胞状态决定了治疗的成败？
**研究意义：** 传统的分析方法像“大锅饭”，只能看到肿瘤组织的平均水平。单细胞测序虽然能看到每个细胞，但缺乏一种稳健的算法来给每个细胞的“响应程度”打分。scResponse 就是为了填补这个空白，帮助研究者精准定位那些拖后腿或立大功的特定细胞状态。

### 2. 白话版概述
想象肿瘤是一个复杂的社区，里面住着癌细胞、免疫细胞和各种“后勤”细胞。免疫治疗就像是一场针对社区的改造行动。
*   过去我们只能判断整个社区改造得好不好；
*   **scResponse** 就像一个精准的“评分器”，能给社区里的每一个居民（细胞）打分，看看谁在支持改造，谁在暗中破坏。
*   通过这个评分，研究者发现癌细胞的“伙食习惯”（代谢方式）直接决定了它对治疗的敏感度。

### 3. 方法部分（scResponse 算法）
*   **核心思想：** 采用**基于秩（Rank-based）**的统计方法。它不直接看基因表达的绝对数值（因为单细胞数据噪声大、不同批次很难比），而是看基因在单个细胞内的“相对排名”。
*   **实现逻辑：**
    1.  **特征提取：** 从已知的临床响应者和不响应者数据中提取关键基因特征。
    2.  **单细胞评分：** 利用秩次算法计算每个细胞与“响应特征”的相关性，得到一个连续的响应得分。
    3.  **状态关联：** 将得分与细胞的生物学状态（如代谢通路、分化阶段）进行关联分析。
*   **关键设计取舍：** 放弃了复杂的深度学习黑盒模型，选择了**秩次算法**。这样做的好处是算法极其稳健，能够跨越不同的测序平台和癌症类型，且计算效率高，不需要昂贵的 GPU 训练。

### 4. 实验部分
*   **数据来源：** 整合了多种癌症（如黑色素瘤、肺癌等）的公开单细胞转录组数据集。
*   **验证任务：** 识别影响疗效的关键细胞亚型。
*   **主要发现：**
    *   **免疫细胞：** 证实了 CD8+ T 细胞的“终末耗竭”状态和巨噬细胞的特定极化方向会抑制疗效。
    *   **肿瘤细胞（重点）：** 发现**乙醛酸和二羧酸代谢**（Glyoxylate and dicarboxylate metabolism）能让肿瘤对治疗更敏感；而**视黄醇代谢**（Retinol metabolism）则会产生耐药性。
*   **实验验证：** 研究不仅停留在电脑模拟，还通过肿瘤-T 细胞共培养实验以及小鼠模型，证实了调节这两个代谢通路确实能改变免疫治疗的效果。

### 5. 资源与算力
*   **文中未充分披露：** 论文未详细列出具体的硬件配置。但基于其“基于秩”的算法描述，该方法通常在普通的 CPU 服务器或高性能个人电脑上即可运行，不依赖大规模 GPU 集群。

### 6. 真正可信的贡献
1.  **工具属性强：** 提供了一个开源且高效的单细胞响应评估工具 scResponse。
2.  **证据链完整：** 结论不仅来自生物信息学分析，还有体外细胞实验和体内动物实验的闭环验证，尤其是关于“代谢通路影响免疫响应”的结论证据最强。
3.  **跨癌种通用：** 证明了该方法在多种实体瘤中都具有普适性。

### 7. 局限与风险
*   **数据依赖：** 算法的准确性高度依赖于初始定义的“响应/非响应”参考基因集。
*   **转录组局限：** 仅基于 RNA 数据，无法直接反映蛋白质水平和翻译后修饰的变化（这些在免疫信号传导中至关重要）。
*   **临床转化障碍：** 虽然发现了代谢靶点，但要在人体内安全地调节这些代谢通路而不产生副作用，仍有很长的路要走。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群：** 从事单细胞算法开发、生物标志物（Biomarker）发现、以及肿瘤免疫微环境研究的 AI 研究者。
*   **后续可跟进的问题：** 能否将这种基于秩的评分机制引入到**空间转录组**中？结合细胞的空间位置信息，或许能更清晰地看到“响应得分”高的细胞是如何在物理空间上围剿癌细胞的。

（完）
