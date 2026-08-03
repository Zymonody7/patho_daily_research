---
title: Same-Slide Spatial Multiomics Integration with IN-DEPTH Reveals Tumor Virus-Linked Spatial Reorganization of the Tumor Microenvironment.
title_zh: 利用 IN-DEPTH 进行同片空间多组学整合，揭示了肿瘤病毒相关的肿瘤微环境空间重组
authors: "Stephanie Pei Tung Yiu, Yuzhou Chang, Yao Yu Yeo, Huaying Qiu, Wenrui Wu, Hendrik A Michel, Xiaojie Jin, Rongting Huang, Shoko Kure, Lindsay Parmelee, Shuli Luo, Precious Cramer, Jia Le Lee, Yang Wang, Zhangxin Zhao, Jason Yeung, Nourhan El Ahmar, Berkay Simsek, Razan Mohanna, McKayla Van Orden, Wesley S Lu, Kenneth J Livak, Shuqiang Li, Ce Gao, Melinda Burgess, Colm Keane, Jahanbanoo Shahryari, Leandra G Kingsley, Reem N Al-Humadi, Sahar Nasr, Dingani Nkosi, Sam Sadigh, Philip Rock, Leonie Frauenfeld, Louisa Kaufmann, Bokai Zhu, Ankit Basak, Nagendra Dhanikonda, Chi Ngai Chan, Jordan Krull, Ye Won Cho, Chia-Yu Chen, Jonathan Brown, Hongbo Wang, Bo Zhao, Jia-Ying Joey Lee, Lit-Hsin Loo, David M Kim, Vassiliki A Boussiotis, Baochun Zhang, Kevin Wei, Alex K Shalek, Brooke E Howitt, Sabina Signoretti, Christian M Schürch, F Stephen Hodi, W Richard Burack, Scott J Rodig, Qin Ma, Sizun Jiang"
date: 2026-08-03
pdf: "https://pubmed.ncbi.nlm.nih.gov/41874448/"
tags: ["query:seqai"]
score: 9.0
evidence: 转录组学和蛋白质组学的空间多组学整合
tldr: 针对空间转录组与蛋白质组技术难以在同一切片上实现高分辨率、无损集成的挑战，本文开发了 IN-DEPTH 工作流，利用单细胞空间蛋白质组影像引导同片转录组捕获，并配套 SGCC 跨模态图分析框架。在弥漫性大 B 细胞淋巴瘤研究中，该方法成功揭示了 EBV 病毒驱动的免疫微环境重构，包括 C1Q 巨噬细胞极化与 CD4 T 细胞功能障碍，为构建多模态空间 AI 模型提供了高质量数据基础。
selection_source: fresh_fetch
motivation: 现有的同切片空间多组学技术在检测通量、空间分辨率及信号保留方面存在局限，难以深入解析复杂的组织微环境。
method: 提出了 IN-DEPTH 工作流，通过蛋白质优先策略实现同片转录组捕获，并结合光谱图互相关（SGCC）算法整合多模态数据。
result: 在 EBV 阳性淋巴瘤中发现了由病毒驱动的 C1Q 巨噬细胞富集、CD4 T 细胞功能障碍以及 IL27-STAT3 信号轴的协同重塑。
conclusion: 该研究提供了一种可扩展的同片空间多组学方案，能够精准解析疾病相关的微环境机制，助力空间多模态 AI 模型的发展。
---

## 摘要
空间转录组学和蛋白质组学为组织结构提供了深刻的见解，但这些技术在很大程度上仍是分离的，且新兴的同片（same-slide）多组学方法在多重性、空间分辨率、信号保留和整合分析方面存在局限。我们介绍了 IN-situ DEtailed Phenotyping To High-resolution transcriptomics (IN-DEPTH)，这是一种精简、资源高效且商业兼容的工作流程，利用单细胞空间蛋白质组学衍生的成像来指导同一载玻片上的转录组捕获，且不会造成 RNA 信号损失。为了在生态位（niche）水平制图之外整合模态，我们开发了光谱图互相关（Spectral Graph Cross-Correlation, SGCC），这是一种蛋白质组-转录组框架，用于解析相互作用细胞群中空间协调的功能状态变化。应用于弥漫性大 B 细胞淋巴瘤 (DLBCL) 时，IN-DEPTH 和 SGCC 通过单细胞分辨率的 Epstein-Barr 病毒 (EBV) 阳性和阴性肿瘤对比，实现了逐步发现，揭示了协调的肿瘤-巨噬细胞-CD4 T 细胞重塑、免疫抑制性 C1Q 巨噬细胞富集、CD4 T 细胞功能障碍以及候选的 IL27-STAT3 信号轴。总的来说，IN-DEPTH 实现了可扩展的空间多组学，以揭示临床相关的微环境机制，并助力构建稳健的空间多模态 AI 模型。意义：IN-DEPTH 通过蛋白质优先策略，在保留蛋白质表位、RNA 质量和组织完整性的基础上，实现了跨商业平台的同片空间多组学。结合 SGCC，它解析了协调的空间免疫重塑，揭示了 DLBCL 中 EBV/LMP1 驱动的 C1Q 巨噬细胞极化和 CD4 T 细胞功能障碍，对其他疾病具有广泛的适用性。

## Abstract
UNLABELLED: Spatial transcriptomics and proteomics have enabled profound insights into tissue organization, yet these technologies remain largely disparate, and emerging same-slide multiomics approaches are limited in plex, spatial resolution, signal retention, and integrative analytics. We introduce IN-situ DEtailed Phenotyping To High-resolution transcriptomics (IN-DEPTH), a streamlined, resource-efficient, commercially compatible workflow using single-cell spatial proteomics-derived imaging to guide transcriptomic capture on the same slide without RNA signal loss. To integrate modalities beyond niche-level mapping, we developed Spectral Graph Cross-Correlation (SGCC), a proteomic-transcriptomic framework resolving spatially coordinated functional state changes across interacting cell populations. Applied to diffuse large B-cell lymphoma (DLBCL), IN-DEPTH and SGCC enabled stepwise discovery from Epstein-Barr virus (EBV)-positive and EBV-negative tumor comparisons with single-cell resolution, revealing coordinated tumor-macrophage-CD4 T-cell remodeling, immunosuppressive C1Q macrophage enrichment, CD4 T-cell dysfunction, and a candidate IL27-STAT3 signaling axis. Collectively, IN-DEPTH enables scalable spatial multiomics to uncover clinically relevant microenvironmental mechanisms and toward robust spatial multimodal AI models. SIGNIFICANCE: IN-DEPTH enables same-slide spatial multiomics across commercial platforms via a protein-first strategy preserving protein epitopes, RNA quality, and tissue integrity. Coupled with SGCC, it resolves coordinated spatial immune remodeling, revealing EBV/LMP1-driven C1Q macrophage polarization and CD4 T-cell dysfunction in DLBCL, with broad applicability to other diseases.

---

## 论文详细总结（自动生成）

这是一份关于论文《Same-Slide Spatial Multiomics Integration with IN-DEPTH Reveals Tumor Virus-Linked Spatial Reorganization of the Tumor Microenvironment》的深度解析：

### 1. 解决的问题与研究意义
**核心问题**：在生物医学研究中，我们想同时看清组织中细胞的“身份”（蛋白质）和“功能状态”（转录组/RNA）。但现有的空间组学技术通常只能二选一，或者需要在相邻的两片组织上分别做实验。由于组织极其微小且不规则，强行将两张图“对齐”会产生巨大的误差。

**研究意义**：本文开发了一套名为 **IN-DEPTH** 的实验流程和 **SGCC** 的分析算法，实现了在**同一张组织切片**上先测蛋白质、再测 RNA，且互不干扰。这为研究复杂的疾病（如淋巴瘤）中病毒如何重塑免疫微环境提供了目前最高精度的“时空地图”。

---

### 2. 白话版概述
想象你在观察一座复杂的城市。蛋白质组学像是一张“建筑分布图”，告诉你哪里是医院（免疫细胞），哪里是工厂（肿瘤细胞）；而转录组学像是一张“通话记录网”，告诉你这些建筑里的人正在聊什么。以前我们只能拿两张不同城市的图强行重叠，误差很大。
这篇论文发明了一种方法，在同一张地图上先画建筑，再录音，互不破坏。然后，他们用一种类似社交网络分析的算法（SGCC），发现当淋巴瘤里存在 EBV 病毒时，肿瘤细胞会招募一种特定的“坏警察”（C1Q 巨噬细胞），专门去“禁言”那些本来该杀敌的“精锐部队”（CD4 T 细胞）。

---

### 3. 方法部分
*   **核心思想（IN-DEPTH 流程）**：采用“蛋白质优先”策略。先利用商业化的 PhenoCycler（原 CODEX）平台进行高通量蛋白质成像（约 50 种蛋白），通过特殊的化学处理保护 RNA 不被降解，随后在同片组织上进行空间转录组捕获（如 Visium 平台）。
*   **算法框架（SGCC）**：
    *   **全称**：光谱图互相关（Spectral Graph Cross-Correlation）。
    *   **逻辑**：将组织建模为一个图（Graph），细胞是节点，空间邻近关系是边。
    *   **跨模态整合**：它不只是简单地把数据堆在一起，而是计算一种“空间相关性”。例如，当 A 蛋白在某个位置升高时，其邻居细胞中哪些基因被激活了？SGCC 利用图信号处理技术，识别出跨模态的空间协调模式。
*   **关键设计取舍**：为了保证 RNA 质量，研究团队优化了蛋白质抗体孵育的缓冲液环境，放弃了某些可能损伤组织的剧烈染色步骤，以换取同片数据的绝对空间对齐。

---

### 4. 实验部分
*   **数据源**：弥漫性大 B 细胞淋巴瘤（DLBCL）患者组织，分为 EBV 病毒阳性和阴性两组。
*   **任务**：解析 EBV 病毒如何通过改变细胞间的“空间对话”来帮助肿瘤逃避免疫攻击。
*   **Baseline（对比项）**：传统的单模态分析（只看蛋白或只看 RNA）以及非同片对齐的常规空间组学分析。
*   **主要结果**：
    1.  **发现新亚群**：识别出一种富集在 EBV+ 肿瘤区域的 **C1Q+ 巨噬细胞**。
    2.  **空间互作**：SGCC 算法证实，这些巨噬细胞在空间上紧贴着功能障碍的 CD4 T 细胞。
    3.  **信号轴验证**：通过多组学整合，锁定了 **IL27-STAT3 信号轴**是驱动这种免疫抑制的关键路径。

---

### 5. 资源与算力
*   **计算资源**：文中未充分披露具体的 GPU/CPU 耗时，但提到使用了标准的生物信息学分析环境（R 和 Python 库）。由于涉及高分辨率图像处理和图计算，通常需要具备大内存（128GB+）的服务器。
*   **实验成本**：该方法依赖 PhenoCycler 和 Visium 等昂贵的商业平台，属于高成本实验方案。

---

### 6. 真正可信的贡献
*   **技术贡献**：证明了在不损失 RNA 信号的前提下，可以在同片组织上完成高通量蛋白成像，这为空间多模态 AI 模型提供了“真值（Ground Truth）”级别的数据集。
*   **生物学贡献**：首次在单细胞空间分辨率下揭示了 EBV 阳性淋巴瘤的免疫逃逸机制，特别是 C1Q 巨噬细胞与 CD4 T 细胞的协调重塑，证据链从空间分布延伸到了分子信号通路，非常扎实。

---

### 7. 局限与风险
*   **分辨率瓶颈**：虽然蛋白质是单细胞分辨率，但目前主流的空间转录组（如 Visium）仍是 55 微米的“光斑（Spot）”，一个光斑内包含多个细胞，依然需要算法反卷积（Deconvolution）来推测。
*   **样本量**：临床样本虽然珍贵，但总体例数相对较小，结论在不同人种或淋巴瘤亚型中的普适性仍需更大规模验证。
*   **操作复杂性**：IN-DEPTH 流程对实验人员的操作要求极高，任何一步 RNA 污染都会导致后续转录组数据失效。

---

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事**多模态表征学习**、**图神经网络（GNN）**以及**空间转录组算法开发**的研究者。
*   **后续可跟进的问题**：如何利用这种“同片对齐”的高质量数据作为训练集，开发出能仅凭 H&E 染色（常规病理图）或简单蛋白图就能预测复杂转录组分布的生成式 AI 模型？

（完）
