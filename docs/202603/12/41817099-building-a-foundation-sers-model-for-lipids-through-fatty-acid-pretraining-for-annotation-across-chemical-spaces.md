---
title: Building a Foundation SERS Model for Lipids through Fatty Acid Pretraining for Annotation across Chemical Spaces.
title_zh: 通过脂肪酸预训练构建用于脂质的 SERS 基础模型，实现跨化学空间的标注
authors: "Rui Han, Emily Xi Tan, Yangcenzi Xie, Hong Sheng Cheng, Nguan Soon Tan, Yan Lv, In Yee Phang, Xing Yi Ling"
date: 2026-03-12
pdf: "https://pubmed.ncbi.nlm.nih.gov/41817099/"
tags: ["query:bioinfo"]
score: 6.0
evidence: 用于分子属性预测和脂质注释的基础模型
tldr: "针对表面增强拉曼光谱（SERS）在识别未知脂质分子时泛化性差的问题，该研究提出了一种基于脂肪酸预训练的领域感知基础模型。通过将分子结构拆解为碳链长度、不饱和度等五个正交向量，模型实现了从简单脂肪酸到复杂多链脂质的零样本外推预测。实验证明该模型在未知脂质识别上达到80%以上准确率，并能实现复杂生物基质中的定量分析，为跨化学空间的分子结构解析提供了新思路。"
selection_source: fresh_fetch
motivation: 传统的拉曼光谱机器学习模型通常只能识别训练集内的已知类别，难以应对测试集中出现的未知分子结构。
method: 将脂质分子结构编码为五个正交的物理化学向量，通过在单链游离脂肪酸上进行预训练，使模型具备通过向量匹配进行零样本结构重构的能力。
result: "模型在未见过的游离脂肪酸、脂肪酸酯及甘油三酯上分别实现了91.7%、85.5%和80.0%的预测准确率，并在人工汗液和尿液中实现了低误差的定量分析。"
conclusion: 该研究证明了通过模块化向量表征和基础模型预训练，可以实现从简单分子光谱到复杂化学空间的跨领域结构预测与解释。
---

## 摘要
振动光谱的机器学习分析通常是闭集的，在已知分子类别上表现良好，但当测试分子超出训练库时，性能会急剧下降。在此，我们介绍了一种基于表面增强拉曼散射（SERS）的领域知识引导的脂肪酸衍生脂质基础模型，该模型用向量匹配取代了类别分配。该模型仅在原始单链游离脂肪酸上进行训练，每个结构属性由多维空间中的五个正交分子向量编码：(1) 碳数，(2) C═C 键数量，(3) C═C 位置，(4) C═C 几何构型，以及 (5) 碳链数量。这种模块化集成实现了从先前未见的光谱中并行进行所有五个向量的零样本预测，从而允许通过该空间中的邻近性而非类别标签进行非靶向分子重构。尽管仅在游离脂肪酸上进行训练，该模型仍能泛化到训练集中不存在的复杂多链脂质，对预留的游离脂肪酸、羟基脂肪酸脂肪酸酯（FAHFAs）和甘油三酯的准确率分别达到 91.7%、85.5% 和 80.0%。为了增强可解释性，我们利用密度泛函理论（DFT）为每次预测背后的光谱特征提供机理基础。我们进一步展示了在人工汗液和尿液中具有基质耐受性的多重定量，在广泛的组成范围内以 2-9% 的误差恢复了混合物比例。总之，该策略实现了从 SERS 到跨相邻化学空间的外推式、可解释的光谱到结构的预测。

## Abstract
Machine learning analysis of vibrational spectra is often closed-set, performing well for known molecular classes but degrading sharply when test molecules fall outside the training library. Herein, we introduce a SERS-based domain-informed foundation model for fatty acid-derived lipids that replaces categorical assignments with vector matching. The model is trained exclusively on primitive single-chain free fatty acids, with each structural attribute encoded by five orthogonal molecular vectors in a multidimensional space: (1) carbon number, (2) number of C═C bonds, (3) C═C position, (4) C═C geometry, and (5) number of carbon chains. This modular ensemble enables zero-shot prediction of all five vectors in parallel from previously unseen spectra, allowing untargeted molecular reconstruction by proximity in this space rather than by class labels. Despite being trained only on free fatty acids, the model generalizes to complex, multichain lipids absent from the training set, achieving accuracies of 91.7% for withheld free fatty acids, 85.5% for fatty acid esters of hydroxy fatty acids, and 80.0% for triglycerides. To enhance interpretability, we utilize density functional theory to provide a mechanistic basis for the spectral features underlying each prediction. We further demonstrate matrix-tolerant multiplex quantitation in artificial sweat and urine, recovering mixture ratios with 2-9% error across broad composition ranges. Collectively, this strategy enables extrapolative, interpretable spectral-to-structure prediction from SERS across adjacent chemical spaces.