---
title: Multimodal computational discovery of MvfR inhibitors targeting quorum sensing in multi-drug-resistant Pseudomonas aeruginosa.
title_zh: 针对多重耐药铜绿假单胞菌群体感应的 MvfR 抑制剂的多模态计算发现
authors: "Tope Abraham Ibisanmi, Xiaotao Jiang, Rasel Ahmed Khan, Tsz Tin Yu, Mark Willcox, Naresh Kumar"
date: 2026-05-05
pdf: "https://pubmed.ncbi.nlm.nih.gov/42086791/"
tags: ["query:pathoai"]
score: 9.0
evidence: 用于抗菌药物发现和病原体靶点识别的AI
tldr: 针对多重耐药铜绿假单胞菌带来的治疗挑战，本研究聚焦于调控群体感应和生物膜形成的关键靶点MvfR。通过整合基因组分析、AI建模、分子对接及500纳秒分子动力学模拟，从化合物库中筛选出具有高亲和力的先导化合物。结果发现一种特定的尿素衍生物在稳定性、药代动力学及结合能方面表现优异，为开发新型抗耐药菌药物提供了高效的计算发现路径。
selection_source: fresh_fetch
motivation: 针对多重耐药铜绿假单胞菌日益严重的临床威胁，亟需寻找能抑制其群体感应和毒力因子的新型非抗生素治疗方案。
method: 采用多模态计算策略，结合基因组耐药基因分析、AI蛋白质建模、高通量分子对接、500纳秒分子动力学模拟及密度泛函理论进行药物筛选。
result: 筛选出一种特定的苯并咪唑尿素衍生物，其在对接评分、分子稳定性参数及药代动力学属性上均表现出优异的成药潜力。
conclusion: 该研究证明了整合基因组学与多尺度模拟的计算方法能有效加速针对耐药菌关键靶点MvfR的先导化合物发现。
---

## 摘要
铜绿假单胞菌（Pseudomonas aeruginosa）因其多重耐药性（MDR）而成为全球主要的健康问题，迫切需要开发新型治疗策略。了解临床分离株耐药性的分子基础对于设计下一代抗菌药物至关重要。本研究分析了从 NCBI 获取的近期铜绿假单胞菌临床分离株的耐药基因和毒力因子图谱。在毒力相关靶点中，群体感应和生物膜形成的关键转录调节因子 MvfR 根据其功能相关性被优先考虑。研究对基因组分析中识别出的 MvfR 进行了 AI 建模，随后进行了化合物库的分子对接、与先前识别的同源物的系统发育比较、ADMET 分析、500 ns 分子动力学（MD）模拟、结合自由能计算以及密度泛函理论（DFT）分析。通过多个数据库识别了对抗菌素耐药性、药物靶向和毒力因子至关重要的基因。抗菌素耐药基因和受体揭示了关键的耐药机制，包括抗生素灭活酶、外排泵、群体感应以及细胞壁电荷或通透性的改变。值得注意的是，(S)-1-(2-(二氟甲基)-1 H-苯并[d]咪唑-5-基)-3-(2-羟基-2-(吡啶-4-基)乙基)脲对 MvfR 表现出最高的对接分数。DFT 和超过 500 ns 的 MD 模拟证明了顶级配体的稳定性，并得到了 RMSD、SASA、RMSF 和 Rg 图等有利的分子稳定性参数的支持。此外，排名靠前的配体符合 Lipinski 五倍律，表明其具有良好的类药性。本研究对近期铜绿假单胞菌分离株中的 MvfR 进行了综合计算表征，并识别了可能影响疾病表现的遗传变异。研究进一步展示了一种综合计算策略，以加速针对多重耐药细菌的有前景的抗菌药物的发现。

## Abstract
Pseudomonas aeruginosa is a major global health concern due to its multidrug resistance (MDR), necessitating the urgent development of novel therapeutic strategies. Understanding the molecular basis of resistance in clinical isolates is critical for designing next-generation antimicrobials. This study analysed recent clinical isolates of P. aeruginosa obtained from the NCBI for their resistance gene and virulence factor profiles. Among the virulence-associated targets, MvfR, a key transcriptional regulator of quorum sensing and biofilm formation, was prioritized based on its functional relevance. AI modelling of MvfR identified from the genome analysis was performed, followed by molecular docking against library of compounds, phylogenetic comparisons to compare with previously identified homologs, ADMET-profiling, 500 ns molecular dynamics (MD) simulations, binding free energy, and Density Functional Theory (DFT). Genes critical for antimicrobial resistance, drug targeting, and virulence factors were identified across multiple databases. The antimicrobial resistance genes and receptors revealed key resistance mechanisms, including antibiotic-inactivating enzymes, efflux pumps, quorum sensing, and alterations in cell wall charge or permeability. Notably, (S)-1-(2-(difluoromethyl)-1 H-benzo[d]imidazol-5-yl)-3-(2-hydroxy-2-(pyridin-4-yl)ethyl)urea exhibited the highest docking score against MvfR. DFT and MD simulations over 500 ns demonstrated stability of the top ligands, supported by favourable molecular stability parameters such as RMSD, SASA, RMSF, and Rg plots. Furthermore, the top-ranking ligands satisfied Lipinski's rule of five, suggesting favourable drug-like properties. This study provides an integrated computational characterization of MvfR in recent P. aeruginosa isolates and identifies genetic variations that may influence disease manifestation. It further demonstrates an integrative computational strategy to accelerate discovery of promising antimicrobial agents against multidrug-resistant bacteria.

---

## 论文详细总结（自动生成）

这篇论文展示了如何利用 AI 和多尺度计算模拟技术，针对“超级细菌”铜绿假单胞菌（*P. aeruginosa*）开发新型非抗生素疗法。

### 1. 核心问题：为什么要解决它？
铜绿假单胞菌是一种极难对付的多重耐药菌（MDR），传统的抗生素往往拿它没办法。这篇论文的核心思路是：**既然杀不死它，就让它“变哑、变弱”**。
*   **靶点 MvfR**：它是细菌的“通讯指挥官”，负责调控“群体感应”（Quorum Sensing，细菌通过化学信号互相交流并协同攻击的行为）和生物膜（细菌盖的“防御工事”）的形成。
*   **价值**：通过抑制 MvfR，可以瓦解细菌的组织能力和防御力，使其毒性降低，且不容易诱导产生新的耐药性。

### 2. 白话版概述
细菌在攻击人体前会先“开会”并盖起“护盾”（生物膜），这篇研究利用 AI 预测了细菌指挥官（MvfR 蛋白）的长相，然后从海量化学分子中筛选出能精准“堵住”这个指挥官嘴巴的药物。研究人员不仅在电脑里模拟了药物和蛋白的结合过程，还进行了长达 500 纳秒的“动态录像”观察，确认药物能稳稳地粘在靶点上。最终发现了一种尿素衍生物，极具潜力成为下一代抗耐药菌药物。

### 3. 方法部分：多模态计算流水线
研究采用了一种从宏观基因组到微观量子力学的“漏斗式”筛选方法：
*   **基因组分析**：从 NCBI 数据库提取近期临床分离株的基因组，识别出耐药基因和毒力因子，确认 MvfR 是一个稳定且关键的靶点。
*   **AI 蛋白质建模**：利用 AI 算法（如 AlphaFold 类工具）对临床株中的 MvfR 蛋白进行三维结构建模，确保药物设计的靶点结构是最新、最准确的。
*   **高通量分子对接（Docking）**：将化合物库中的分子逐一放入 MvfR 的活性口袋，计算结合能，筛选出“钥匙”与“锁”最匹配的候选者。
*   **500ns 分子动力学（MD）模拟**：这是本文的重头戏。在模拟的生物水环境中观察 500 纳秒（在计算领域算较长时间），通过 RMSD（位置偏差）和 Rg（紧凑度）等指标，验证药物分子是否会从蛋白上脱落。
*   **量子化学分析（DFT）**：利用密度泛函理论从电子层面分析分子的稳定性，确保药物分子本身结构稳固。

### 4. 实验部分：数据与结果
*   **数据源**：来自 NCBI 的铜绿假单胞菌临床分离株全基因组序列。
*   **主要任务**：寻找能强力结合 MvfR 的小分子抑制剂。
*   **评价指标**：对接评分（Docking Score）、结合自由能（MM-GBSA）、药代动力学属性（ADMET，即吸收、分布、代谢、排泄、毒性）。
*   **关键结果**：
    *   筛选出一种名为 **(S)-1-(2-(二氟甲基)-1 H-苯并[d]咪唑-5-yl)-3-(2-hydroxy-2-(吡啶-4-基)乙基)尿素** 的化合物。
    *   该分子在 500ns 模拟中表现出极高的稳定性。
    *   符合“类药五倍律”（Lipinski's Rule of Five），意味着它具备被制成口服药物的潜力。

### 5. 资源与算力
*   **文中披露情况**：文中未详细披露具体的硬件型号（如 GPU 数量），但提到了 500ns 的 MD 模拟。
*   **估算**：这种规模的模拟通常需要高性能计算集群（HPC）或多块 NVIDIA A100/H100 级别的显卡运行数周。

### 6. 真正可信的贡献
*   **全流程整合**：将临床基因组数据直接转化为药物发现的输入，这种“从病房到计算实验室”的闭环非常有参考价值。
*   **长时程模拟证据**：500ns 的 MD 模拟比常见的 100ns 模拟提供了更强的结构稳定性证据。
*   **多尺度验证**：结合了宏观的 ADMET 预测和微观的 DFT 量子计算，结论的物理化学基础较扎实。

### 7. 局限与风险
*   **缺乏湿实验验证**：这是纯计算研究（In silico），筛选出的分子是否真的能在培养皿里抑制细菌生长，甚至在动物体内有效，尚无实验数据支持。
*   **外推风险**：虽然分析了临床株，但细菌进化极快，MvfR 靶点若发生单点突变，可能导致筛选出的药物失效。
*   **应用障碍**：尿素衍生物在体内的代谢稳定性及免疫原性仍需通过生物学实验进一步确认。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事计算机辅助药物设计（CADD）、耐药菌治理、以及希望将基因组学与结构生物学结合的研究者。
*   **后续可跟进的问题**：如何利用生成式 AI（AIGC）直接针对 MvfR 的动态口袋生成全新的分子，而不仅仅是从现有库中筛选？

（完）
