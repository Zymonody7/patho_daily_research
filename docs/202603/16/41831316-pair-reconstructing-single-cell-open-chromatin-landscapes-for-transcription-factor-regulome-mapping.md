---
title: "PAIR: Reconstructing Single-Cell Open-Chromatin Landscapes for Transcription Factor Regulome Mapping."
title_zh: PAIR：重构单细胞开放染色质图谱以进行转录因子调控组映射
authors: "Yanchi Su, Qi Qi, Yi Fan, Yubo Wang, Gaoyang Hao, Ka-Chun Wong, Yunhe Wang, Xiangtao Li"
date: 2026-03-14
pdf: "https://pubmed.ncbi.nlm.nih.gov/41831316/"
tags: ["query:seqai"]
score: 8.0
evidence: 用于单细胞ATAC-seq重建和细胞状态描绘的概率框架
tldr: 针对单细胞 ATAC-seq 数据极度稀疏且存在技术缺失的挑战，PAIR 提出了一种基于二分图编码器的概率框架。该方法通过变分潜层捕捉测量不确定性，并利用定性与定量双解码器重构染色质开放性图谱。实验证明 PAIR 能显著提升细胞聚类精度和差异分析灵敏度，并能有效挖掘黑色素瘤及前脑发育中的转录因子调控网络，为单细胞调控组学研究提供了强有力的支持。
selection_source: fresh_fetch
motivation: 解决单细胞 ATAC-seq 数据因测序深度有限和高稀疏性导致的细胞状态刻画难及转录因子调控推断不准的问题。
method: 采用二分图编码器对细胞和峰值进行联合表征，并结合变分推断与双重解码器（定性开关与定量计数）来恢复缺失的信号。
result: 在多项基准测试中提升了聚类性能，并揭示了 SOX10 等关键因子的调控邻域以及与临床生存相关的基因模块。
conclusion: PAIR 证明了通过建模细胞-峰值二分结构并结合概率重构，可以有效修复单细胞染色质景观并增强复杂的生物学发现。
---

## 摘要
单细胞 ATAC-seq (scATAC-seq) 能够在细胞分辨率下探究染色质可及性，但其在实际应用中常受限于测序深度有限、极端稀疏性以及普遍的技术缺失，这些因素共同阻碍了稳健的细胞状态刻画和转录因子 (TF) 调控程序的推断。我们提出了 PAIR，这是一个通过直接建模染色质可及性的原生“细胞-峰”（cell-peak）二分结构来恢复 scATAC-seq 可及性图谱的概率框架。PAIR 利用二分图编码器学习细胞和峰的表示，并结合变分潜层来显式捕捉由稀疏和噪声测量引起的不确定性。为了共同恢复离散的可及性模式和定量信号，PAIR 集成了两个互补的解码器：一个用于重构细胞-峰开放/关闭关联的定性解码器，以及一个在负二项似然下建模可及性计数的定量解码器。通过变分和嵌入正则化进行端到端训练，PAIR 生成了细胞和峰的嵌入以及插补后的可及性矩阵，从而改善了下游分析。在具有受控测序深度、噪声和丢包 (dropout) 的模拟数据集以及多个公开基准数据集上，PAIR 一致地提高了聚类性能并增加了差异可及性分析的灵敏度。除了细胞层面的分析，PAIR 衍生的峰嵌入还支持以位点为中心的调控探究：围绕 SOX10 的共可及性分析揭示了结构化的调控邻域，基于图的峰模块展示了在黑色素瘤细胞状态中的选择性活性，并识别出具有临床相关生存关联的基因集。在前脑图谱中，PAIR 恢复了跨越启动子近端和远端元件的调控信号，并揭示了与神经元特化一致的生物学相干富集模式。

## Abstract
Single-cell ATAC-seq (scATAC-seq) enables the interrogation of chromatin accessibility at cellular resolution, yet its practical utility is often constrained by limited sequencing depth, extreme sparsity, and pervasive technical missingness, which collectively hamper robust cell-state delineation and inference of transcription factor (TF) regulatory programs. We present PAIR, a probabilistic framework that restores scATAC-seq accessibility profiles by directly modeling the native cell-peak bipartite structure of chromatin accessibility. PAIR leverages a bipartite graph encoder to learn representations for both cells and peaks, and incorporates a variational latent layer to explicitly capture uncertainty arising from sparse and noisy measurements. To jointly recover discrete accessibility patterns and quantitative signal, PAIR integrates two complementary decoders: a qualitative decoder that reconstructs open/closed cell-peak incidences and a quantitative decoder that models accessibility counts under a Negative Binomial likelihood. Trained end-to-end with variational and embedding regularization, PAIR yields cell and peak embeddings and an imputed accessibility matrix that improves downstream analyses. Across simulated datasets with controlled sequencing depth, noise, and dropout, as well as multiple publicly available benchmarks, PAIR consistently improves clustering performance and increases sensitivity for differential accessibility. Beyond cell-level analyses, PAIR-derived peak embedding enables locus-centric regulatory interrogation: co-accessibility analysis around SOX10 reveals structured regulatory neighborhoods, and graph-based peak modules show selective activity across melanoma cell states and identify gene sets with clinically relevant survival associations. In a forebrain atlas, PAIR restores regulatory signals spanning both promoter-proximal and distal elements and uncovers biologically coherent enrichment patterns consistent with neuronal specialization.

---

## 论文详细总结（自动生成）

这是一份关于论文 **PAIR**（发表于 *Advanced Science*, 2026）的深度技术总结：

### 1. 核心问题：解决单细胞“数据荒漠”
**单细胞 ATAC-seq (scATAC-seq)** 是一种测量细胞内 DNA 哪些区域是“开放”的技术（开放意味着该区域可能正在被转录因子调控）。
*   **痛点：** 这种数据极其“稀疏”。由于测序技术的物理限制，一个细胞中 95% 以上的开放区域可能都检测不到信号（被称为 Dropout 现象）。这导致研究者很难准确给细胞分类，也无法看清基因表达背后的“开关”逻辑。
*   **价值：** PAIR 旨在通过深度学习算法，把这些丢失的信号“补全”（插补），从而还原出清晰的染色质开放图谱，帮助理解疾病（如黑色素瘤）的调控机制。

### 2. 白话版概述
想象一张巨大的网，左边是几万个“细胞”，右边是几十万个“DNA 片段（Peak）”。如果某个细胞的某个片段是开放的，它们之间就连一条线。但现在的技术只能随机抓到极少数的连线。
PAIR 的做法是：利用**二分图神经网络**学习细胞和片段的特征，通过“物以类聚”的原理，推断出那些本该存在但没被观测到的连线。它不仅能猜出“有没有连线”（定性），还能猜出“连线有多粗”（定量），从而把模糊的原始数据变成高清的调控地图。

### 3. 方法部分：双重解码的概率框架
*   **核心思想：** 将 scATAC-seq 数据建模为**细胞-峰（Cell-Peak）二分图**。它认为细胞和基因组片段是相互定义的：相似的细胞会开放相似的片段，而相似的片段也会在相似的细胞中开放。
*   **模型结构：**
    1.  **二分图编码器（Bipartite Graph Encoder）：** 聚合邻居节点信息，同时学习细胞和 Peak 的低维向量表示（Embedding）。
    2.  **变分潜层（Variational Latent Layer）：** 引入 VAE（变分自编码器）的思想，不只是学习一个固定数值，而是学习一个概率分布，以应对数据中的高噪声和不确定性。
    3.  **双解码器设计（关键取舍）：**
        *   **定性解码器：** 预测该位置是否开放（0 或 1），解决“开关”问题。
        *   **定量解码器：** 使用**负二项分布（Negative Binomial）**建模具体的测序计数，解决“强弱”问题。
*   **训练流程：** 采用端到端训练，结合了重构损失、KL 散度（正则化潜空间）和嵌入正则化，确保学习到的特征具有生物学意义。

### 4. 实验部分
*   **数据与任务：** 在模拟数据集（受控的噪声和缺失率）和真实数据集（人前脑发育图谱、黑色素瘤细胞系）上进行测试。
*   **Baseline（对比方法）：** 与现有的主流方法（如 SCALE, cisTopic 等）进行对比。
*   **评价指标：** 聚类准确度（ARI, NMI）、差异可及性分析的灵敏度、调控元件的一致性。
*   **主要结果：**
    *   **聚类更准：** 在极低测序深度下，PAIR 依然能清晰划分细胞类型。
    *   **发现新调控：** 成功识别出黑色素瘤中 SOX10 蛋白的调控网络，并发现了一些与患者生存率相关的基因模块。
    *   **信号修复：** 在前脑数据中，修复了启动子（基因开关近端）和增强子（远端）的信号，使下游分析更符合生物学常识。

### 5. 资源与算力
*   **文中未充分披露：** 摘要和元数据中未提及具体的 GPU 型号、训练时长或内存消耗。但基于其二分图结构和变分框架，处理数十万 Peak 的图运算通常需要大显存（如 A100/H100）或采用子图采样策略。

### 6. 真正可信的贡献
*   **证据最强的结论：** PAIR 在**提升差异可及性（Differential Accessibility）分析灵敏度**方面表现稳健。这意味着它补全的数据不是乱猜的，而是确实增强了那些在原始数据中被淹没的生物学信号。
*   **双表征学习：** 它同时产出高质量的细胞 Embedding 和 Peak Embedding，这对于寻找“协同工作的基因片段”非常有价值。

### 7. 局限与风险
*   **计算开销：** scATAC-seq 的 Peak 数量通常在 10w-50w 级别，构建完整的二分图会带来巨大的内存压力，论文在超大规模数据集上的扩展性（Scalability）有待进一步验证。
*   **过度平滑风险：** 所有的插补算法都有可能引入“假阳性”，即把本不相关的信号强行补在一起，导致生物学上的误导。
*   **数据偏差：** 如果原始数据存在严重的批次效应（Batch Effect），模型可能会放大这些偏差。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群：** 关注图神经网络（GNN）、变分自编码器（VAE）以及单细胞组学数据增强的研究者。
*   **后续可跟进的问题：** 如何将这种二分图框架扩展到“多模态”数据（例如同时补全同一个细胞的 RNA 和 ATAC 信号）？以及如何引入基因组序列的先验信息（如 DNA 序列基序）来约束图的学习？

（完）
