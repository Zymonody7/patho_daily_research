---
title: Identification of molecular compounds targeting bacterial propionate metabolism with topological machine learning.
title_zh: 利用拓扑机器学习识别靶向细菌丙酸代谢的分子化合物
authors: "Astrit Tola, Shan Aziz, Dannie Zhabilov, Duane Winkler, Mehmet Candas, Baris Coskunuzer"
date: 2026-05-01
pdf: "https://pubmed.ncbi.nlm.nih.gov/41544343/"
tags: ["query:pathoai"]
score: 9.0
evidence: 拓扑机器学习用于识别针对病原菌代谢的化合物
tldr: 针对致病菌丙酸代谢途径中关键酶 AcnD 的抑制剂筛选难题，本研究结合拓扑机器学习与蛋白质-配体比较分析，从大规模化学库中筛选潜在化合物。通过将分子结构转化为拓扑向量并结合分子对接，识别出衣康酸（itaconate）作为核心骨架，实验证实其能有效抑制铜绿假单胞菌和鲍曼不动杆菌的生长，为开发新型抗菌药物提供了高效的计算筛选范式。
selection_source: fresh_fetch
motivation: 旨在通过干扰致病菌利用宿主脂质的关键代谢过程，寻找能诱导毒性中间体积累并导致细菌死亡的新型抗菌药物靶点及其抑制剂。
method: 将配体分子结构转化为拓扑向量，利用定制的拓扑机器学习模型筛选与 AcnD 活性位点几何匹配的化合物，并结合分子对接模拟验证其相互作用。
result: 识别出衣康酸作为针对 AcnD 的关键分子骨架，并在生物实验中证实其在 29.13 mM 浓度下可完全抑制铜绿假单胞菌和鲍曼不动杆菌的生长。
conclusion: 拓扑机器学习与结构功能分析的结合能有效识别具有几何匹配和能量优势的分子骨架，为抗菌药物的下游优化和实验验证提供了可靠路径。
---

## 摘要
本研究通过将蛋白质与配体的比较分析与新型拓扑机器学习方法相结合，展示了机器学习在药物研发中的变革潜力。我们的方法通过筛选大型化学库，以高精度识别靶向特定蛋白质的有前景的分子结构。虽然许多机器学习模型已在基准数据集上证明了其有效性，但我们将这些技术应用于发现靶向甲基柠檬酸脱水酶 (AcnD) 的化合物，该酶是细菌丙酸分解代谢途径中的第二个酶。丙酸分解代谢对于病原菌利用宿主来源的脂质和氨基酸至关重要。丙酸清除效率低下会导致毒性积累，威胁细菌生存，使该途径成为潜在的抗菌靶点。我们将配体分子结构转化为拓扑向量，并使用定制的拓扑模型来优先筛选具有与阻断 AcnD 活性位点一致特征的化合物。分子对接模拟表明，优先筛选出的化合物与对 AcnD 功能至关重要的关键氨基酸残基发生相互作用。其中，2-亚甲基丁二酸（衣康酸，itaconate）作为靶向 AcnD 的潜在分子支架排名靠前。通过细菌生长实验，我们发现 29.13 mM 的衣康酸在富碳液体培养基中能完全抑制铜绿假单胞菌 (Pseudomonas aeruginosa) 和鲍曼不动杆菌 (Acinetobacter baumannii) 的生长。这些发现增强了衣康酸作为抗菌代谢物的潜力，并支持了其可以破坏细菌丙酸分解代谢的假设，其机制可能是通过抑制 AcnD 并促进毒性中间体的积累。总之，我们的研究强调了将基于拓扑的配体建模与比较序列-结构-功能分析及对接相结合的价值，以识别具有良好几何拟合、能量和相互作用特征的分子支架，从而指导下游优化和实验验证。我们的代码可在 (https://github.com/AstritTola/Molecular-Compounds-Targeting) 获取。

## Abstract
This study demonstrates the transformative potential of machine learning in drug discovery by integrating comparative protein and ligand analysis with novel topological machine learning methods. Our approach sifts through large chemical libraries to identify promising molecular structures for targeting specific proteins with high precision. While many machine learning models have proven effective on benchmark datasets, we apply these techniques to discover compounds targeting methylcitrate dehydratase (AcnD), the second enzyme in the bacterial propionate catabolism pathway. Propionate catabolism is essential in pathogenic bacteria for utilizing host derived lipids and amino acids. Inefficient removal of propionate can lead to toxic accumulation that threatens bacterial survival, making this pathway a potential antimicrobial target. We translate ligand molecular structures into topological vectors and use tailored topological models to prioritize compounds with characteristics consistent with blocking the AcnD active site. Molecular docking simulations indicate that prioritized compounds interact with key amino acid residues critical to AcnD function. Among these, 2-methylidenebutanedioic acid (itaconic acid, itaconate) ranks highly as a potential molecular scaffold for targeting AcnD. Using bacterial growth assays, we find that itaconate at 29.13 mM completely inhibits the growth of Pseudomonas aeruginosa and Acinetobacter baumannii in carbon rich liquid cultures. These findings reinforce itaconate's potential as an antimicrobial metabolite and support the hypothesis that it can disrupt bacterial propionate catabolism, potentially by inhibiting AcnD and promoting the accumulation of toxic intermediates. Overall, our study underscores the value of integrating topology based ligand modeling with comparative sequence structure function analysis and docking to identify molecular scaffolds with favorable geometric fit, energy, and interaction profiles, guiding downstream optimization and experimental validation. Our code is available at (https://github.com/AstritTola/Molecular-Compounds-Targeting).

---

## 论文详细总结（自动生成）

这篇论文结合了数学中的**拓扑数据分析（TDA）**与机器学习，旨在寻找能够干扰细菌代谢的新型抗菌药物。

### 1. 解决的问题与研究意义
*   **核心问题**：随着抗生素耐药性增强，急需寻找新的药物靶点。
*   **研究意义**：论文瞄准了细菌的“丙酸代谢”途径。丙酸是细菌分解脂肪酸时产生的物质，如果代谢不畅，中间产物（如 2-甲基柠檬酸）会在细菌体内堆积产生剧毒，导致细菌“自杀”。研究者试图找到能抑制该途径中关键酶 **AcnD**（甲基柠檬酸脱水酶）的化合物，从而诱导这种细菌毒性积累。

### 2. 白话版概述
细菌在感染人体时需要“吃”掉宿主的脂肪来生存，这会产生丙酸。如果能把细菌处理丙酸的“加工厂”（AcnD 酶）堵死，细菌就会被自己产生的代谢垃圾毒死。研究者利用一种能识别分子“形状特征”的 AI 技术（拓扑机器学习），从海量化学库中筛选出最像“塞子”的分子。最终锁定了一个叫“衣康酸”的分子，并通过实验室培养证实它确实能让两种致命的耐药菌（铜绿假单胞菌和鲍曼不动杆菌）停止生长。

### 3. 方法部分
*   **核心思想**：利用**持续同调（Persistent Homology）**将分子的三维几何结构转化为数学向量。这种方法不只看原子种类，更关注分子在不同尺度下的“孔洞”和“连接性”等拓扑特征。
*   **模型流程**：
    1.  **特征提取**：将配体（小分子）的 3D 结构转化为拓扑特征向量（Topological Signatures）。
    2.  **拓扑机器学习 (TML)**：构建回归或分类模型，学习已知配体与靶点结合的模式，在大规模数据库中进行高通量筛选。
    3.  **分子对接 (Molecular Docking)**：对 AI 筛选出的高分候选分子进行物理模拟，计算它们与 AcnD 酶活性位点的结合能（Binding Energy）和相互作用力。
*   **关键设计**：拓扑特征对分子的微小旋转和形变不敏感，能够捕捉到传统化学指纹（Fingerprints）容易忽略的几何匹配信息。

### 4. 实验部分
*   **数据与任务**：从大型化学库中筛选针对 AcnD 酶的抑制剂。
*   **主要任务**：虚拟筛选 + 生物实验验证。
*   **评价指标**：结合能（kcal/mol）、细菌生长抑制率。
*   **主要结果**：
    *   **AI 筛选**：识别出**衣康酸（Itaconate）**及其衍生物是极具潜力的骨架。
    *   **分子模拟**：衣康酸能与 AcnD 活性位点的关键氨基酸残基形成稳定的相互作用。
    *   **湿实验验证**：在 29.13 mM 的浓度下，衣康酸能够**完全抑制**铜绿假单胞菌和鲍曼不动杆菌的生长。

### 5. 资源与算力
*   **文中未充分披露**具体的硬件配置（如 GPU 型号或训练时长），但提供了 GitHub 代码仓库，通常此类拓扑特征提取在 CPU 集群上即可高效完成。

### 6. 论文的可信贡献
*   **最强证据**：不仅有 AI 预测，还进行了**闭环验证**。通过真实的细菌培养实验证实了预测分子的有效性，这在纯 AI 论文中较为难得。
*   **理论贡献**：证明了拓扑特征在捕捉代谢酶抑制剂方面的独特性，尤其是针对具有特定几何需求的酶活性中心。

### 7. 局限与风险
*   **药物效价（Potency）**：实验中产生抑制效果的浓度为 29.13 mM，这在药物研发中属于**极高浓度**（通常理想药物在微摩尔 $\mu M$ 级别）。这意味着衣康酸目前只是一个“骨架”，距离成为真正的临床药物还需要大量的化学修饰来增强活性。
*   **特异性风险**：人体也有类似的代谢途径，该化合物是否会误伤人体细胞（毒性测试）在文中未详细讨论。
*   **数据偏差**：模型表现高度依赖于 AcnD 酶结构的准确性，若细菌发生突变导致酶结构改变，模型可能失效。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：对几何深度学习（Geometric DL）、拓扑数据分析（TDA）以及代谢组学药物研发感兴趣的研究者。
*   **后续可跟进的问题**：如何利用生成式 AI（如 Diffusion Model）在衣康酸骨架的基础上，自动设计出结合力更强（纳摩尔级别）且对人体无害的新型衍生物？

（完）
