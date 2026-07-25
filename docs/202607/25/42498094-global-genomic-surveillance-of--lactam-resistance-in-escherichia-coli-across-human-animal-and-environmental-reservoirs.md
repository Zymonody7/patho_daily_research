---
title: "Global genomic surveillance of β-lactam resistance in Escherichia coli across human, animal, and environmental reservoirs."
title_zh: 全球人类、动物及环境宿主中大肠杆菌 β-内酰胺类耐药性的基因组监测
authors: "Mohammad Sholeh, Masoumeh Beig, Negin Kiani, Farzad Badmasti"
date: 2026-07-24
pdf: "https://pubmed.ncbi.nlm.nih.gov/42498094/"
tags: ["query:pathoai"]
score: 9.0
evidence: 大肠杆菌的全球基因组监测和耐药性预测
tldr: "针对大肠杆菌 β-内酰胺类抗生素耐药性全球蔓延的威胁，本研究通过分析 2000-2025 年间来自人类、动物和环境的 30,554 个全基因组数据，揭示了 blaCTX-M-15 等关键耐药基因在 ST131 等高危克隆中的传播趋势。研究利用梯度提升机器学习算法实现了对碳青霉烯类药物最小抑菌浓度（MIC）的高精度预测，为构建全球“全健康”耐药性监测与管理体系提供了数据支撑和技术路径。"
selection_source: fresh_fetch
motivation: 旨在通过跨物种、跨地域的基因组大数据分析，厘清大肠杆菌对 β-内酰胺类抗生素耐药性的演变规律并提升耐药性预测能力。
method: 整合了全球 126 个国家的 3 万余份大肠杆菌基因组，利用生物信息学工具鉴定耐药基因与序列类型，并结合梯度提升机器学习模型预测不同抗生素的最小抑菌浓度。
result: 发现人类、动物和环境来源的菌株具有明显的序列类型差异，且机器学习在预测碳青霉烯类耐药性方面表现优异（R²达0.88），但在预测加酶抑制剂复合制剂时效果较差。
conclusion: 全球大肠杆菌耐药性的上升主要由特定高危克隆携带的关键耐药基因驱动，整合基因组学与“全健康”数据是未来精准防控抗生素耐药性的关键。
---

## 摘要
背景：大肠杆菌日益增长的 β-内酰胺类耐药性对全球健康构成了威胁。本研究利用基因组和“全健康”（One-Health）数据来绘制耐药模式，并增强抗生素耐药性（AMR）的预测与管理。方法：本研究对 2000 年至 2025 年间来自人类、动物和环境来源的 30,554 株大肠杆菌分离株进行了“全健康”全基因组分析。从 NCBI 获取了公开的基因组数据，涵盖了 β-内酰胺类耐药基因（包括超广谱 β-内酰胺酶、AmpC 和碳青霉烯酶）以及关键的染色体耐药修饰因子。使用 AMRFinderPlus 对这些基因进行了识别和整理。通过计算机模拟进行了多位点序列分型（MLST）和致病型分配。对耐药性的时间、宿主、序列类型（ST）和地理模式进行了建模，并利用梯度提升机器学习算法，根据抗生素耐药基因谱和

## Abstract
BACKGROUND: Escherichia coli poses a global health threat from increasing β-lactam resistance. This study uses genomic and One-Health data to map resistance patterns and enhance antimicrobial resistance (AMR) prediction and management. METHODS: This study performed a One-Health whole-genome analysis of 30,554 E. coli isolates from human, animal, and environmental sources, spanning from 2000 to 2025. Publicly available genomic data were retrieved from NCBI, encompassing β-lactam resistance genes, including extended-spectrum β-lactamases, AmpC, and carbapenemases, along with key chromosomal resistance modifiers. These genes were identified and curated using AMRFinderPlus. Multilocus sequence typing (MLST) and pathotype assignments were conducted in silico. Temporal, host, sequence-type (ST), and geographic patterns of resistance were modeled, with gradient-boosted machine learning algorithms predicting minimum inhibitory concentrations (MICs) based on antibiotic resistance gene profiles and chromosomal features. Temporal and geographic resistance patterns were further analyzed using statistical and visualization tools in R and Python. RESULTS: A total of 30,554 E. coli whole-genome sequences from isolates spanning 126 countries between 2000 and 2025 were analyzed. The dataset included 2015 complete genomes, 177 chromosome-level assemblies, 8310 scaffold-level assemblies, and 20,052 contig-level assemblies, with an average sequence length of 5,120,983 bp. Isolates were categorized by host source: 14,320 from humans, 8184 from animals, 3941 from environmental sources, and 4109 with an unknown source. MLST was successfully performed on 29,648 isolates, identifying dominant STs such as ST131, ST11, and ST10. Human isolates were predominantly associated with epidemic clones ST131, ST73, and ST1193, while animal isolates were associated with ST10, and environmental isolates showed a strong presence of ST155. Temporal analyses indicated a steady increase in β-lactam resistance, with blaCTX-M-15, blaNDM-5, and blaOXA-1 showing the most significant prevalence trends. Model performance was strongest for carbapenems, particularly imipenem (R2 = 0.88) and ertapenem (R2 = 0.74), whereas predictions for ampicillin and piperacillin-tazobactam showed poor agreement with observed MICs. CONCLUSIONS: Global analysis of 30,554 genomes shows rising β-lactam resistance driven by key genes (blaCTX-M-15, blaNDM-5, blaOXA-1) in high-risk clones. Machine learning accurately predicted carbapenem resistance but struggled with β-lactamase inhibitor combos. Integrating genomics and One-Health data can guide AMR surveillance and control.

---

## 论文详细总结（自动生成）

这是一份关于全球大肠杆菌（*E. coli*）$\beta$-内酰胺类耐药性基因组监测研究的深度分析报告。

### 1. 核心问题与研究意义
这篇论文主要解决的是**抗生素耐药性（AMR）的全球演变规律与精准预测**问题。
*   **背景**：$\beta$-内酰胺类抗生素（如青霉素、头孢、碳青霉烯）是临床最常用的药物，但大肠杆菌通过进化出特定的耐药基因，使这些药物逐渐失效。
*   **意义**：耐药性不仅在医院传播，还在动物和环境中循环（即“全健康/One-Health”概念）。通过大规模基因组数据结合机器学习，研究者试图建立一套从“基因序列”直接预测“药效强度（MIC）”的模型，这对于临床快速诊断和全球防疫至关重要。

### 2. 白话版概述
大肠杆菌是人体和环境中最常见的细菌之一，但有些变种携带了能“吃掉”抗生素的基因，变成了超级细菌。这项研究收集了全球 25 年间、超过 3 万份细菌的 DNA 样本，分析了它们在人类、动物和自然界中是如何流动的。研究者还训练了一个 AI 模型，只要输入细菌的 DNA 信息，AI 就能预测需要多大剂量的抗生素才能杀死它。结果发现，AI 预测某些强力抗生素（如碳青霉烯）的效果非常好，但预测一些复合药物时还不够聪明。

### 3. 方法部分
*   **核心思想**：将细菌的**基因型（Genotype）**特征映射到**表型（Phenotype，即耐药程度）**。
*   **特征工程**：
    *   使用 `AMRFinderPlus` 工具从全基因组序列中提取耐药基因（如 ESBLs, AmpC 等）和染色体上的关键突变。
    *   利用 `MLST`（多位点序列分型）对细菌进行“家族”分类（如 ST131 是著名的人类致病克隆）。
*   **模型结构**：采用了**梯度提升机器学习算法（Gradient-Boosted Machine, GBM）**。这是一种集成学习方法，通过组合多个弱分类器（决策树）来构建强预测模型。
*   **设计取舍**：研究没有采用复杂的深度学习（如 CNN/Transformer），而是选择了可解释性相对较好的 GBM，因为在生物信息学中，理解哪些基因特征导致了耐药性（特征重要性）与预测准确率同样重要。

### 4. 实验部分
*   **数据规模**：跨越 126 个国家、2000-2025 年间的 **30,554 个大肠杆菌基因组**。涵盖人类（1.4万+）、动物（8千+）和环境（近4千）来源。
*   **任务**：预测最小抑菌浓度（MIC，即杀死细菌所需的最低药物浓度）。
*   **评价指标**：决定系数 $R^2$（衡量预测值与真实值的拟合程度）。
*   **主要结果**：
    1.  **克隆分布**：人类样本中 ST131 占主导；动物样本中 ST10 最多；环境样本中 ST155 比例较高。这证明了耐药菌在不同宿主间存在明显的“势力范围”。
    2.  **AI 预测表现**：
        *   **碳青霉烯类（高级抗生素）**：预测效果极佳，亚胺培南（Imipenem）的 $R^2$ 达到 **0.88**。
        *   **复合药物（加酶抑制剂）**：如哌拉西林-他唑巴坦，预测效果较差。这说明复合药物的耐药机制更复杂，简单的基因叠加模型难以覆盖。

### 5. 资源与算力
*   **文中未充分披露**具体的硬件配置（如 GPU/CPU 核心数）和训练时长。考虑到 3 万个样本的基因组特征维度较高，通常需要高性能计算集群（HPC）进行特征提取，但 GBM 模型的训练在常规工作站上即可完成。

### 6. 真正可信的贡献
*   **最大规模的“全健康”数据集**：整合了人类、动物、环境三方的基因组数据，揭示了耐药基因（如 *blaCTX-M-15*）在全球范围内的时空演变趋势。
*   **碳青霉烯耐药的高精度预测**：证明了对于机制相对明确的抗生素，基于基因组的 AI 预测已经具备了替代传统实验室药敏试验（耗时 24-48 小时）的潜力。

### 7. 局限与风险
*   **数据偏差**：虽然覆盖 126 国，但高收入国家的测序数据远多于低收入国家，模型可能存在地理偏见。
*   **复合机制失效**：模型在处理“抗生素+抑制剂”组合时表现不佳，说明 AI 尚未掌握细菌通过多种途径（如外排泵、孔蛋白改变）共同作用产生的复杂耐药逻辑。
*   **黑盒风险**：虽然 GBM 比深度学习好解释，但对于临床医生来说，仅给出一个预测的 MIC 值而没有生物学机理解释，在实际应用中仍存在信任障碍。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事抗菌药物研发、公共卫生监测、以及对“基因型-表型”预测感兴趣的 AI 研究者。
*   **后续可跟进的问题**：如何利用图神经网络（GNN）建模细菌基因组内部的相互作用（Epistasis），以提升对复合抗生素耐药性的预测精度？

（完）
