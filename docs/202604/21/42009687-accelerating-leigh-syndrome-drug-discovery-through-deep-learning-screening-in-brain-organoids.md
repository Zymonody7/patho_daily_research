---
title: Accelerating Leigh syndrome drug discovery through deep learning screening in brain organoids.
title_zh: 通过类脑器官中的深度学习筛选加速 Leigh 综合征的药物研发
authors: "Carmen Menacho, Satoshi Okawa, Iris Álvarez-Merz, Annika Wittich, Mikel Muñoz-Oreja, Pawel Lisowski, Mario López Martín, Tancredi Massimo Pentimalli, Shiri Zakin, Mathuravani Thevandavakkam, Caleb Jerred, Selene Lickfett, Laura Petersilie, Agnieszka Rybak-Wolf, Annette Seibt, Diran Herebian, Gizem Inak, Susanne Brodesser, Andrea Zaliani, Barbara Mlody, Justin Donnelly, Kasey Woleben, Francesc Xavier Soriano, Jose C Fernandez-Checa, Natascia Ventura, Sidney Cambridge, Ertan Mayatepek, Antonella Spinazzola, Markus Schuelke, Nikolaus Rajewsky, Andrea Rossi, Alex Peralvarez-Marin, Felix Distelmaier, Ethan Perlstein, Ian J Holt, Emma Puighermanal, Ole Pless, Christine R Rose, Antonio Del Sol, Alessandro Prigione"
date: 2026-04-20
pdf: "https://pubmed.ncbi.nlm.nih.gov/42009687/"
tags: ["query:bioinfo"]
score: 8.0
evidence: 用于细胞类型特异性药物重定向筛选的深度学习算法
tldr: 针对缺乏疗法的罕见线粒体疾病Leigh综合征，研究者利用SURF1突变导致的神经元发育受损表型，开发了细胞类型特异性的深度学习药物筛选算法，并结合酵母模型进行平行验证。研究发现唑类化合物（如他拉罗唑）能显著修复类脑器官的神经元形态并改善代谢异常。该成果展示了AI筛选与人类类器官模型结合在加速罕见神经发育疾病药物发现方面的应用价值。
selection_source: fresh_fetch
motivation: 旨在解决Leigh综合征这一罕见线粒体疾病缺乏有效治疗手段的问题，利用其特有的神经元形态发育受损作为筛选突破口。
method: 开发了一种面向细胞类型特异性药物重利用的深度学习算法，并同步开展了基于酵母模型的生存药物筛选以进行交叉验证。
result: 两种筛选路径共同指向了唑类化合物，实验证明他拉罗唑和舍他康唑能有效恢复Leigh综合征类脑器官的神经元形态并降低乳酸释放。
conclusion: 该研究验证了深度学习结合人类类脑器官作为新方法论（NAMs）在识别罕见病候选药物及揭示其分子机制方面的有效性。
---

## 摘要
Leigh 综合征（Leigh）是一种尚无有效疗法的线粒体疾病，其特征为乳酸酸中毒以及基底节和中脑病理改变，导致精神运动发育倒退和早期死亡。我们此前发现，携带 SURF1 基因变异的 Leigh 大脑类器官存在神经元形态发生受损的情况。利用这一表型，我们在此开发了一种专门针对细胞类型特异性药物重定向筛选的深度学习算法。与此同时，我们在 Leigh 综合征的酵母模型中进行了生存药物筛选。这两种方法独立地汇聚于唑类化合物，其中两种——塔拉罗唑（talarozole）和舍他康唑（sertaconazole）——能够修复 Leigh 神经元的形态发生，并降低 Leigh 中脑类器官的乳酸释放，提高其生长速率。在机制上，这些化合物调节视黄酸通路和膜相关脂质代谢。研究结果凸显了唑类化合物作为 Leigh 综合征候选药物的潜力，并证明了将计算机模拟筛选与人类类脑器官相结合作为新方法学（NAMs）的潜力，以推进针对罕见神经发育障碍的疗法开发。

## Abstract
Leigh syndrome (Leigh) is an untreatable mitochondrial disorder characterized by lactic acidosis and basal ganglia and midbrain pathology, leading to psychomotor regression and early death. We previously uncovered impaired neuronal morphogenesis in Leigh cerebral organoids carrying SURF1 gene variants. Leveraging this phenotype, we here develop a deep learning algorithm tailored for cell type-specific drug repurposing screening. In parallel, we perform a survival drug screen in a yeast model of Leigh. The two approaches independently converge on azole compounds, two of which - talarozole and sertaconazole - rescue neuronal morphogenesis in Leigh neurons and lower lactate release and improve growth rate in Leigh midbrain organoids. Mechanistically, these compounds modulate the retinoic acid pathway and membrane-associate lipid metabolism. The findings highlight azoles as promising candidates for Leigh and demonstrate the potential of combining in silico screens with human brain organoids as new approach methodologies (NAMs) to advance the discovery of therapeutics addressing rare neurodevelopmental disorders.

---

## 论文详细总结（自动生成）

这篇论文展示了如何利用 AI 技术结合前沿的“类脑器官”技术，为一种极其罕见且致命的遗传病寻找老药新用的机会。

### 1. 解决的问题与研究意义
*   **核心问题**：Leigh 综合征（Leigh Syndrome）是一种罕见的线粒体疾病，患者因基因突变导致细胞“能量工厂”失灵，出现严重的脑部病变和发育倒退，目前**无药可医**。
*   **研究意义**：罕见病研究面临样本极少、动物模型不匹配（小鼠往往无法模拟人类脑部症状）的困境。本文通过 AI 筛选和“实验室培养的微型大脑”（类脑器官）结合，证明了即使在数据稀缺的情况下，也能快速锁定潜在药物，为罕见病药物研发提供了新范式。

### 2. 白话版概述
研究团队先用患者的细胞在实验室里培育出“类脑器官”，发现这些微型大脑里的神经元长得“无精打采”（形态发育受损）。他们开发了一套深度学习算法，在成千上万种现有药物中寻找能把这种“病态”扭转回“健康态”的药物。同时，他们还在简单的酵母模型上做了实验。神奇的是，AI 和酵母实验共同指向了一类叫“唑类”的化合物。实验证明，其中的他拉罗唑（Talarozole）确实能让神经元恢复活力，并改善代谢指标。

### 3. 方法部分：核心思想与设计
*   **核心思想**：利用**细胞类型特异性**的转录组特征进行药物重定向。AI 的目标是预测哪些药物能诱导特定的基因表达变化，从而抵消疾病带来的负面影响。
*   **模型结构**：开发了一种针对细胞类型优化的深度学习筛选算法（具体架构在摘要中未详述，通常基于生成式模型或深度嵌入网络，用于匹配药物扰动谱与疾病特征谱）。
*   **关键设计取舍**：
    *   **双轨并行**：不只依赖 AI，还同步进行了酵母模型（Leigh 综合征的简化生物模型）的生存筛选。
    *   **跨物种验证**：如果一个药物在简单的酵母和复杂的 AI 预测中都有效，那么它在人类身上的潜力更高。
    *   **表型驱动**：筛选标准不只是“杀死病灶”，而是“修复形态”（如神经元的长度和分支）。

### 4. 实验部分：数据与结果
*   **实验对象**：携带 *SURF1* 基因突变的患者诱导多能干细胞（iPSC）衍生的类脑器官（中脑和大脑皮层类器官）。
*   **评价指标**：
    1.  **神经元形态**：神经突触的长度、分支复杂度。
    2.  **代谢指标**：乳酸（Lactate）释放量（Leigh 综合征患者乳酸通常过高）。
    3.  **生长率**：类器官的整体发育速度。
*   **主要结果**：
    *   AI 和酵母筛选共同锁定了**唑类化合物（Azoles）**。
    *   **他拉罗唑（Talarozole）**和**舍他康唑（Sertaconazole）**显著修复了神经元形态，降低了乳酸水平。
    *   **机制发现**：这些药物通过调节视黄酸（Retinoic Acid）通路和膜脂质代谢起作用。

### 5. 资源与算力
*   **文中未充分披露**具体的计算硬件配置（如 GPU 型号或训练时长）。此类研究通常侧重于算法逻辑和生物验证。

### 6. 真正可信的贡献
*   **最强证据**：**独立验证的一致性**。AI 预测结果与酵母生存筛选实验结果高度吻合，且最终在人类类脑器官上得到了生物学验证。
*   **方法论贡献**：证明了“类器官 + AI”可以作为一种可靠的“新方法学（NAMs）”，绕过传统动物实验在罕见病研究中的局限性。

### 7. 局限与风险
*   **类器官的局限**：类脑器官虽然比小鼠更接近人脑，但仍缺乏血管系统、免疫细胞和完整的神经环路，无法完全模拟真实人脑环境。
*   **药物副作用**：唑类化合物（如他拉罗唑）虽然在实验室有效，但在人体内的血脑屏障穿透力、长期毒性仍需临床试验验证。
*   **数据偏差**：AI 筛选依赖于现有的药物扰动数据库，如果数据库中缺乏某些新型分子的信息，AI 将无法识别。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事药物重定向（Drug Repurposing）、细胞图谱分析、以及罕见病计算生物学的研究者。
*   **后续可跟进的问题**：如何将这种“形态学修复”作为 AI 的损失函数（Loss Function），直接从显微图像中学习药物特征，而不仅仅依赖转录组数据？

（完）
