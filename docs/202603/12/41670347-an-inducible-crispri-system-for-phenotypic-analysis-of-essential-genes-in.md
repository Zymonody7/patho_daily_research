---
title: An inducible CRISPRi system for phenotypic analysis of essential genes in
title_zh: 一种用于必需基因表型分析的可诱导 CRISPRi 系统
authors: "Jaryd R Sullivan, Kristina M Ferrara, Rebecca Barrick, Keith P Romano, Thulasi Warrier, Deborah T Hung"
date: 2026-03-11
pdf: "https://pubmed.ncbi.nlm.nih.gov/41670347/"
tags: ["query:bioinfo"]
score: 8.0
evidence: 用于病原体功能基因组学的诱导型 CRISPRi 系统
tldr: 针对铜绿假单胞菌中必需基因研究缺乏精确调控工具的问题，本研究开发了一种基于鼠李糖诱导启动子的CRISPRi系统。该系统通过双质粒模块化设计，实现了对dCas9和sgRNA的紧密调控，成功对16个必需基因进行了表型分析，揭示了基因功能与抗生素敏感性的关联。该工具为系统性评估病原菌基因脆弱性及加速抗生素研发提供了关键技术支撑。
selection_source: fresh_fetch
motivation: 铜绿假单胞菌作为一种耐药性极强的病原菌，急需能够精确且可调控地抑制必需基因的遗传工具，以深入理解其生存机制并寻找新的药物靶点。
method: 构建了一个由鼠李糖诱导启动子驱动的双质粒CRISPRi系统，利用来自巴氏链球菌的dCas9蛋白实现对特定基因表达的精准下调。
result: 成功对16个涉及不同通路的必需基因进行了受控敲低，并观察到这些基因缺失对生长速度、抗生素敏感性及转录组谱图的显著影响。
conclusion: 该诱导型CRISPRi系统不仅适用于单个基因的功能研究，还能支持大规模突变库的构建，是探索病原菌生物学和筛选新型抗菌药物的强有力平台。
---

## 摘要
精确且可调控的遗传工具对于高通量功能基因组学至关重要。为了满足重要革兰氏阴性病原体铜绿假单胞菌（Pseudomonas aeruginosa）的这一需求，我们开发并表征了一种受严密调控的 CRISPR 干扰（CRISPRi）系统，该系统能够对必需基因进行精确且可调控的抑制。该系统利用鼠李糖诱导型启动子来控制源自巴氏链球菌（Streptococcus pasteurianus）的 dCas9 和基因特异性 sgRNA，两者分别编码在不同的质粒上，以实现模块化和高效性。严密的调控与高接合效率相结合，促进了跨越多种途径的 16 个必需基因受控缺失菌株的快速简便构建。通过比较不同基因缺失菌株的表型（包括生长率、抗生素敏感性和转录程序的变化），揭示了基因功能或小分子作用机制的新方面。最后，鼠李糖诱导型 CRISPRi 系统支持混合突变体库的生成和稳定维持，从而为未来全基因组范围内系统评估单个基因的脆弱性铺平了道路，这将为针对这种顽固病原体的抗生素研发中的靶点优先级排序提供关键见解。重要性：CRISPR 干扰（CRISPRi）已成为研究遗传学的宝贵工具。特别是，基因敲低（KD）的能力使得研究必需基因及其在细胞存活中的作用成为可能。然而，由于这些基因的必需性，需要一个受严密调控的基因敲低系统才能获得关于这些脆弱基因的有价值见解。我们报告了一种受严密调控的 CRISPRi 系统，用于研究铜绿假单胞菌中必需基因扰动的生物学特性。铜绿假单胞菌是一种重要的革兰氏阴性病原体，可引起严重感染，且对现有抗生素的耐药性日益增强。该系统能够表征小分子与特定基因缺失之间的化学遗传相互作用，以及遗传扰动对转录网络的影响。因此，利用 CRISPRi 进行的遗传扰动可以加深我们对基础生物学的理解，并转化为未来的抗菌药物开发。

## Abstract
Precise and tunable genetic tools are essential for high-throughput functional genomics. To address this need in the important gram-negative pathogen Pseudomonas aeruginosa, we developed and characterized a tightly regulated CRISPR-interference (CRISPRi) system that enables precise and tunable repression of essential genes. The system utilizes a rhamnose-inducible promoter to control both the Streptococcus pasteurianus-derived dCas9 and gene-specific sgRNAs, each encoded on separate plasmids for modularity and efficiency. The combination of tight regulation and high conjugation efficiency facilitated the rapid and facile construction of strains with regulated depletion of 16 essential genes spanning diverse pathways. Comparison of phenotypes across the different genetically depleted strains, including growth rate, susceptibility to antibiotics, and changes in transcriptional programs, revealed novel aspects of gene function or small-molecule mechanism of action. Finally, the rhamnose-inducible CRISPRi system supports the generation and stable maintenance of pooled mutant libraries, thereby paving the way for future genome-wide, systematic assessment of individual gene vulnerabilities, which will provide critical insights for target prioritization in antibiotic discovery efforts against this recalcitrant pathogen.IMPORTANCECRISPR-interference (CRISPRi) has become an invaluable tool for studying genetics. In particular, the ability to knockdown (KD) genes enables the study of essential genes and their role in cell survival. However, a tightly regulated gene KD system is required to gain valuable insights into these vulnerable genes by virtue of their essentiality. We report a tightly regulated CRISPRi system to study the biology of essential gene perturbations in Pseudomonas aeruginosa, an important gram-negative pathogen that causes severe infections and is increasingly resistant to current antibiotics. This system enables characterization of both chemical genetic interactions between small molecules and specific gene depletions and the impact of genetic perturbations on transcriptional networks. Genetic perturbations using CRISPRi can thus further our understanding of basic biology with translation toward future antimicrobial development.

---

## 论文详细总结（自动生成）

这篇论文介绍了一种针对**铜绿假单胞菌**（一种极难对付的耐药“超级细菌”）的高精度遗传调控工具。

### 1. 解决的问题与研究意义
在生物学研究中，**必需基因（Essential Genes）**是维持生命所必需的“零件”，也是开发新型抗生素的最佳靶点。但研究它们非常困难：如果你直接删掉这些基因，细菌就会死亡，导致你无法观察其功能。

现有的调控工具（如传统的 CRISPRi）存在“**漏表达（Leaky）**”问题——就像一个关不紧的水龙头，即使不加诱导剂，系统也会偷偷工作，导致细菌生长缓慢甚至死亡。这篇论文开发了一套基于**鼠李糖（Rhamnose）诱导**的新系统，解决了“关不紧”的问题，实现了对细菌基因表达的精准“调光”。

---

### 2. 白话版概述
研究团队给铜绿假单胞菌装了一个“远程调光开关”。他们利用一种特殊的 CRISPR 技术（不切断 DNA，只像路障一样挡住基因表达），并用鼠李糖作为开关信号。
1. **不加糖时**：开关完全关闭，细菌正常生长，方便大规模培养。
2. **加糖以后**：根据加糖的多少，可以精确控制某个关键基因被“关掉”的程度。
通过这种方式，科学家可以像做压力测试一样，观察细菌在某个零件逐渐失灵时，对哪些药物变得更敏感，或者其内部代谢发生了什么变化。

---

### 3. 方法部分
*   **核心思想**：利用 **CRISPRi (CRISPR interference)** 技术。使用失去切割能力的 **dCas9** 蛋白，它在 **sgRNA**（导航手册）的引导下定位到目标基因，通过物理遮挡阻止基因转录。
*   **关键设计（鼠李糖系统）**：
    *   **双质粒模块化**：将 dCas9 和 sgRNA 分别放在两个不同的 DNA 环（质粒）上，方便灵活组合。
    *   **紧密调控**：使用 $P_{rhaBAD}$ 启动子。这个启动子的特性是“给信号才干活，不给信号绝不偷懒”。
*   **取舍**：研究者对比了阿拉伯糖诱导系统（CRISPRi A）和鼠李糖系统（CRISPRi R）。发现前者在不加诱导剂时也会抑制基因（漏表达），导致必需基因突变株无法稳定存在；而后者非常“干净”，适合构建大规模的突变株库。

---

### 4. 实验部分
*   **研究对象**：铜绿假单胞菌 PA14 株。
*   **任务**：对 16 个涉及细胞壁合成、DNA 复制、蛋白质合成等核心通路的必需基因进行敲低（Knockdown）。
*   **评价指标**：
    *   **生长曲线**：观察抑制基因后细菌长得快慢。
    *   **转录组分析（RNA-seq）**：看基因被关掉后，细菌体内几千个基因的表达水平如何波动。
    *   **化学遗传相互作用**：测试基因被抑制后，细菌对不同抗生素的敏感性变化。
*   **主要结果**：
    *   鼠李糖系统在无诱导时完全不影响细菌生长，解决了漏表达问题。
    *   成功构建了包含 17 种不同菌株的混合库，且库在传代过程中保持稳定。
    *   发现抑制某些基因（如 $parC$）会触发细菌的 SOS 修复反应，而抑制另一些（如 $gyrA/B$）则不会，揭示了相似功能基因间的细微差别。

---

### 5. 资源与算力
*   **文中未充分披露**。该研究主要侧重于湿实验（生物构建与验证），生物信息学部分涉及常规的 RNA-seq 数据处理和相关性分析（PerSpec™），未提及大规模 GPU 训练或特殊算力需求。

---

### 6. 真正可信的贡献
*   **高可靠性的工具箱**：证明了鼠李糖诱导系统在铜绿假单胞菌中比阿拉伯糖系统更“紧”，这对于研究必需基因是决定性的进步。
*   **混合库的稳定性**：实验数据有力地证明了该系统可以用于**混合筛选（Pooled Screening）**，这意味着未来可以一次性筛选成千上万个基因。
*   **转录组指纹**：通过 RNA-seq 证明了基因抑制产生的效应与药物处理高度相似，为“以基因扰动模拟药物作用”提供了强有力的证据。

---

### 7. 局限与风险
*   **规模有限**：虽然证明了可行性，但论文仅展示了 16 个基因，尚未实现全基因组规模的筛选。
*   **环境依赖性**：鼠李糖作为诱导剂，在某些复杂的培养基或动物感染模型中可能会受到细菌自身代谢的影响。
*   **系统复杂性**：双质粒系统需要两次转化和两种抗生素筛选，对于某些临床分离的顽固菌株可能操作较难。

---

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事**基因调控网络（GRN）建模**、**药物靶点预测**以及**高通量筛选数据分析**的 AI 研究者。
*   **后续可跟进的问题**：
    *   能否利用这种“干净”的扰动数据，训练模型来预测未知基因被抑制后的转录组变化（即预测“基因指纹”）？
    *   如何利用化学遗传相互作用的数据，通过机器学习算法自动聚类并识别新型抗生素的作用机制（MoA）？

（完）
