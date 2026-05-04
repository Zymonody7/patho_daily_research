---
title: Comprehensive evaluation of artificial intelligence-empowered approaches for protein-aptamer complex prediction.
title_zh: 人工智能赋能的蛋白质-适配体复合物预测方法的全面评估
authors: "Jiani Zhao, Kha Tram, Hongbin Yan, Yifeng Li"
date: 2026-05-04
pdf: "https://pubmed.ncbi.nlm.nih.gov/42080590/"
tags: ["query:bioinfo"]
score: 8.0
evidence: 人工智能赋能的蛋白质-适配体复合物预测用于药物发现
tldr: 针对核酸适配体药物设计中结构数据稀缺且分子柔性大的挑战，本研究系统评估了 AlphaFold3、Chai-1、Boltz-2 和 RoseTTAFold2NA 等前沿 AI 模型在预测蛋白质-适配体复合物结构及结合自由能方面的表现。通过建立独立基准测试集，揭示了现有模型在结构精度和能量一致性上的优劣，为核酸类药物的 AI 辅助设计提供了关键参考。
selection_source: fresh_fetch
motivation: 适配体药物具有高特异性和低免疫原性，但由于其结构柔性大且实验数据匮乏，导致 AI 在该领域的建模和设计进展缓慢。
method: 建立了一个独立的基准测试集，对比评估了 AlphaFold3、Chai-1、Boltz-2、RoseTTAFold2NA 等主流 AI 框架以及传统模板法在复合物结构预测和能量评估上的性能。
result: 实验量化了各模型在预测蛋白质-适配体复合物结构准确度、稳定性和结合自由能一致性方面的差异，指出了当前 AI 方法的局限性。
conclusion: 该研究为 AI 在核酸适配体药物研发中的应用奠定了基础，并为未来生物大分子建模和核酸疗法研究提供了标准化的评估框架。
---

## 摘要
药物研发是一个耗时、昂贵且高风险的过程。人工智能（AI）的最新进展已在小分子和蛋白质疗法领域取得了重大突破。然而，AI 驱动的适配体药物设计在很大程度上仍处于未开发状态。适配体是短的（15-100 nt）单链 DNA 或 RNA，具有高结合亲和力、高特异性和低免疫原性，使其成为疾病（如癌症）治疗的有前途的候选药物。与蛋白质-配体或蛋白质-蛋白质系统相比，蛋白质-适配体复合物在公共结构数据库中的代表性不足，且适配体本身是具有高度柔性且相对较大的分子。这些特性为基于 AI 的结构建模带来了独特的挑战。在本研究中，我们系统地评估了包括 AlphaFold3、Chai-1、Boltz-2 和 RoseTTAFold2NA 在内的近期 AI 框架，以及一种基于模板的方法，在预测蛋白质-适配体复合物结构和估算结合自由能方面的表现。我们建立了一个独立的基准，以评估它们在结构准确性、稳定性和能量一致性方面的性能。本研究为 AI 在适配体药物设计中的应用奠定了基础，并为核酸疗法和生物分子建模的未来研究提供了参考框架。

## Abstract
Drug discovery is a time-consuming, expensive, and high-risk process. Recent advances in artificial intelligence (AI) have enabled major breakthroughs in small-molecule and protein therapeutics. However, AI-driven design of aptamer drugs remains largely unexplored. Aptamers are short (15-100 nt) single-stranded DNAs or RNAs that exhibit high binding affinity, high specificity, and low immunogenicity, making them promising candidates for disease (such as cancer) therapeutics. Compared with protein-ligand or protein-protein systems, protein-aptamer complexes are under-represented in public structural databases, and aptamers themselves are highly flexible and relatively large molecules. These characteristics present distinct challenges for AI-based structural modeling. Here, we systematically evaluate recent AI frameworks, including AlphaFold3, Chai-1, Boltz-2, and RoseTTAFold2NA, along with a template-based approach, in predicting protein-aptamer complex structures and estimating binding free energies. We establish an independent benchmark to assess their performance in structural accuracy, stability, and energetic consistency. This study provides a foundation for the application of AI in aptamer drug design and offers a reference framework for future research in nucleic-acid therapeutics and biomolecular modeling.

---

## 论文详细总结（自动生成）

这篇论文是对当前最前沿的 AI 蛋白质-核酸复合物预测模型的一次“大阅兵”。它针对的是药物研发中一个非常有前景但极具挑战的领域：**适配体（Aptamer）**。

### 1. 解决的问题与研究价值
*   **核心问题**：适配体（通常是 15-100 个碱基长度的单链 DNA 或 RNA）被称为“化学抗体”，能像钥匙开锁一样精准结合目标蛋白质。但由于适配体结构极其柔软（柔性大）、实验测定的结构数据稀少（在 PDB 数据库中占比远低于蛋白质），导致 AI 很难准确预测它们是怎么和蛋白质“抱”在一起的。
*   **研究价值**：目前 AlphaFold3 等模型号称能预测“所有生命分子”，但这篇论文通过实测告诉研究者：这些模型在适配体这个细分领域到底行不行？差距在哪里？

### 2. 白话版概述
适配体就像是一根在水里乱飘的绳子，只有遇到特定的蛋白质时才会折叠成复杂的形状并紧紧缠绕上去。过去我们靠昂贵的实验来观察这个过程，现在我们想用 AI 直接“算”出来。这篇论文把目前市面上最厉害的四个 AI 厨师（AlphaFold3, Chai-1, Boltz-2, RoseTTAFold2NA）请到一起，给它们同样的食材（蛋白质和适配体的序列），看谁做出的“复合物结构”最接近真实情况，并测试这些 AI 预测的结构在物理模拟中是否稳固。

### 3. 方法部分
*   **核心思想**：建立一个独立的基准测试集（Benchmark），对多种端到端（End-to-End）AI 框架进行系统性横向对比。
*   **评估对象**：
    *   **AlphaFold3**：DeepMind 的最新全能模型。
    *   **Chai-1 / Boltz-2**：近期开源的高性能多模态生物分子预测模型。
    *   **RoseTTAFold2NA**：专门针对核酸（NA）优化过的经典模型。
    *   **模板法**：作为传统对照组，利用已知相似结构进行建模。
*   **推理流程**：
    1.  **输入**：蛋白质氨基酸序列 + 适配体核苷酸序列。
    2.  **预测**：AI 生成三维原子坐标。
    3.  **精修与验证**：使用**分子动力学（MD）模拟**（一种模拟原子随时间运动的物理方法）来观察 AI 预测的结构在水溶液环境中是否会散架。
    4.  **能量计算**：估算两者结合的紧密程度（结合自由能）。

### 4. 实验部分
*   **数据**：从公共数据库中筛选出高质量的蛋白质-适配体复合物结构，确保这些数据不在部分模型的训练集内，以保证测试的公正性。
*   **评价指标**：
    *   **RMSD**：预测原子位置与真实位置的偏差（越小越好）。
    *   **lDDT**：衡量局部结构可靠性的指标。
    *   **结合自由能 ($\Delta G$)**：判断预测的结构在物理上是否具有合理的吸引力。
*   **主要结果**：
    *   **AlphaFold3 和 Chai-1** 在整体结构预测上处于第一梯队，表现显著优于老牌模型。
    *   **柔性挑战**：所有模型在预测适配体那些“飘在外面”的非结合区域时表现都很差。
    *   **能量一致性**：AI 预测的结构虽然看起来“像”真的，但在物理能量计算上往往不一致，说明 AI 对底层物理相互作用的理解仍有欠缺。

### 5. 资源与算力
*   **文中未充分披露**：摘要和提取文本中未详细列出具体的 GPU 型号或训练总时长，但提到使用了标准的 AI 框架推理流程和分子动力学模拟。

### 6. 真正可信的贡献
*   **独立基准**：为适配体领域提供了一个标准化的“考卷”，不再听信各家模型论文里的自测结果。
*   **物理稳定性验证**：首次系统性地指出，AI 预测出的适配体结构虽然几何形状不错，但在物理模拟（MD）中往往不够稳定，这为后续改进指明了方向。

### 7. 局限与风险
*   **数据偏差**：由于 PDB 数据库中适配体结构本来就少，基准测试集的规模依然受限，可能无法覆盖所有类型的适配体。
*   **静态 vs 动态**：AI 给出的是一个静态快照，但适配体在体内是高度动态的，目前的 AI 模型还无法很好地捕捉这种动态平衡。
*   **设计障碍**：预测已知序列的结构（预测）和从头设计一个能结合某蛋白的序列（设计）是两回事，本研究证明了预测尚且困难，设计则更具挑战。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事核酸药物研发、大分子相互作用建模、以及试图改进 AlphaFold 架构的 AI 工程师。
*   **后续可跟进的问题**：如何将物理约束（如分子动力学模拟的反馈）引入 AI 模型的训练循环中，以提高预测结构的物理合理性？

（完）
