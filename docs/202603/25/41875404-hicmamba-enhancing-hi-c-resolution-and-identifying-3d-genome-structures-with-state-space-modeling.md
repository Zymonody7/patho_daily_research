---
title: "HiCMamba: Enhancing Hi-C resolution and identifying 3D genome structures with state space modeling."
title_zh: HiCMamba：利用状态空间模型提升 Hi-C 分辨率并识别三维基因组结构
authors: "Minghao Yang, Zhi-An Huang, Zhihang Zheng, Yuqiao Liu, Shichen Zhang, Pengfei Zhang, Hui Xiong, Shaojun Tang"
date: 2026-03-01
pdf: "https://pubmed.ncbi.nlm.nih.gov/41875404/"
tags: ["query:seqai"]
score: 8.0
evidence: 用于增强 Hi-C 分辨率的状态空间建模
tldr: Hi-C技术是研究3D基因组结构的关键，但高昂的测序成本导致数据分辨率受限。HiCMamba引入了状态空间模型（SSM），通过基于UNet的自编码器架构和全局扫描模块，实现了对Hi-C接触图的高效超分辨率增强。实验证明该方法在提升精度的同时显著降低了计算开销，并能准确还原TAD和染色质环等关键生物结构，为低成本获取高质量基因组互作数据提供了新方案。
selection_source: fresh_fetch
motivation: 针对Hi-C测序成本高昂导致的接触图分辨率不足、交互频率估计不准的问题，寻求一种高效的深度学习增强方案。
method: 提出一种基于Mamba（状态空间模型）的UNet架构，利用全局扫描模块在多尺度上捕捉基因组互作的局部细节与长程依赖。
result: 在保持高精度的同时显著减少了计算资源消耗，且恢复出的拓扑关联域（TAD）和染色质环等结构得到了表观基因组特征的验证。
conclusion: 证明了状态空间模型在处理大规模基因组互作数据中的潜力，为3D基因组学研究提供了一个兼顾性能与效率的基础框架。
---

## 摘要
Hi-C 技术测量全基因组范围内的相互作用频率，为研究细胞核内的三维基因组结构提供了强有力的工具。然而，高昂的测序成本和技术挑战往往导致 Hi-C 数据覆盖度有限，从而导致染色质相互作用频率的估计不够精确。为解决这一问题，我们提出了一种基于深度学习的新方法 HiCMamba，利用状态空间模型来提升 Hi-C 接触图的分辨率。我们采用了基于 UNet 的自动编码器架构来堆叠所提出的整体扫描模块（holistic scan block），从而实现在多个尺度上对全局和局部感受野的感知。实验结果表明，HiCMamba 在显著减少计算资源消耗的同时，性能优于现有最先进的方法。此外，通过相关的表观基因组特征验证了在 HiCMamba 恢复的接触图中识别出的三维基因组结构，包括拓扑相关结构域（TADs）和染色质环（loops）。我们的工作展示了状态空间模型作为 Hi-C 分辨率增强领域基础框架的潜力。本研究中使用的数据和源代码可在 GitHub 获取：https://github.com/myang998/HiCMamba。

## Abstract
Hi-C technology measures genome-wide interaction frequencies, providing a powerful tool for studying the 3D genomic structure within the nucleus. However, high sequencing costs and technical challenges often result in Hi-C data with limited coverage, leading to imprecise estimates of chromatin interaction frequencies. To address this issue, we present a novel deep learning-based method HiCMamba to enhance the resolution of Hi-C contact maps using a state space model. We adopt the UNet-based auto-encoder architecture to stack the proposed holistic scan block, enabling the perception of both global and local receptive fields at multiple scales. Experimental results demonstrate that HiCMamba outperforms state-of-the-art methods while significantly reducing computational resources. Furthermore, the 3D genome structures, including topologically associating domains (TADs) and loops, identified in the contact maps recovered by HiCMamba are validated through associated epigenomic features. Our work demonstrates the potential of a state space model as foundational frameworks in the field of Hi-C resolution enhancement. The data and source code used in this work are available at GitHub: https://github.com/myang998/HiCMamba.

---

## 论文详细总结（自动生成）

### HiCMamba：利用状态空间模型提升 Hi-C 分辨率并识别三维基因组结构

#### 1. 核心问题与研究意义
**解决的问题：**
Hi-C 技术用于探测细胞核内 DNA 的三维空间折叠结构（即哪些片段在空间上靠在一起）。但高质量（高分辨率）的 Hi-C 实验测序成本极高。低成本测序得到的“低分辨率”数据就像模糊的照片，丢失了关键的生物学细节，如 **TAD**（拓扑相关结构域，DNA 上的功能“社区”）和 **Loop**（染色质环，远端基因调控的关键触点）。

**研究意义：**
论文提出 **HiCMamba**，旨在通过 AI 算法将“模糊”的低分辨率 Hi-C 图像修复为“清晰”的高分辨率图像。它首次将 **Mamba（状态空间模型 SSM）** 引入该领域，解决了传统 CNN 感受野受限和 Transformer 计算开销过大的矛盾，实现了高精度与高效率的平衡。

---

#### 2. 白话版概述
想象 DNA 是一团乱麻，Hi-C 就像是给这团乱麻拍的“热图”，颜色越深表示两段 DNA 接触越频繁。高分辨率照片太贵，我们只能拍低清的。HiCMamba 就像是一个智能修图软件（超分辨率重建），它利用 Mamba 这种新型架构，既能看清局部的小斑点（Loop），又能把握全局的大轮廓（TAD），而且运行速度比之前的 AI 快得多，占用的电脑内存也更少。

---

#### 3. 方法部分
*   **核心思想：** 结合 **UNet** 的多尺度特征提取能力与 **Mamba** 的线性复杂度全局建模能力。
*   **模型结构：**
    *   **UNet 骨架：** 采用经典的编码器-解码器结构，通过下采样捕捉全局背景，上采样恢复细节。
    *   **Holistic Scan Block（整体扫描模块）：** 这是核心组件，包含两个子模块：
        1.  **SS2D (Selective Scan 2D)：** 将 2D 的 Hi-C 矩阵沿四个方向（左上到右下、右下到左上等）展平为序列，利用 Mamba 的 S6 算子进行扫描，从而在 2D 图像上实现全局感受野。
        2.  **LEFN (Locality-enhanced Feed-forward Network)：** 在 Mamba 之后加入深度卷积（Depth-wise Conv），增强对局部像素级特征的捕捉，弥补 Mamba 在精细纹理上的不足。
*   **关键取舍：** 放弃了计算量随窗口大小平方增长的 Transformer（Attention 机制），选择线性增长的 Mamba，使得处理超大基因组区域成为可能。

---

#### 4. 实验部分
*   **数据：** 使用人类标准细胞系 GM12878 和 K562 的 Hi-C 数据。
*   **任务：** 将下采样（模拟低测序深度，如 1/16 到 1/100）的接触图恢复至原始高分辨率水平。
*   **Baseline：** 对比了 HiCSR、HiC-GAN、DeepHiC、HiCNN 等主流深度学习方法。
*   **评价指标：**
    *   **图像指标：** PCC（皮尔逊相关系数）、SRCC（斯皮尔曼相关系数）、SSIM（结构相似性）。
    *   **生物指标：** 恢复出的 Loop 数量、TAD 边界的准确性，以及与 CTCF（绝缘子蛋白）等表观信号的一致性。
*   **主要结果：** HiCMamba 在所有图像指标上均达到 SOTA（最优），尤其在极低覆盖度（1/100）下优势明显。更重要的是，它恢复出的生物结构（Loop/TAD）与真实实验数据高度吻合。

---

#### 5. 资源与算力
*   **计算效率：** 论文明确对比了 **MACs（乘加运算次数）**。HiCMamba 的计算复杂度随输入窗口大小呈线性增长，而基于 Transformer 的方法呈指数增长。
*   **训练资源：** 文中未充分披露具体的 GPU 型号和训练总时长，但强调了其在相同硬件下比同类模型更省显存、速度更快。

---

#### 6. 真正可信的贡献
1.  **效率突破：** 证明了 Mamba 架构在处理 2D 基因组矩阵时，比 CNN 更有“大局观”，比 Transformer 更轻量。
2.  **生物学一致性：** 证据最强的地方在于其增强后的图像不仅是“看起来清晰”，而且能准确预测出被 CTCF 蛋白验证过的染色质环，这说明模型学到了真实的物理相互作用规律，而非简单的图像平滑。

---

#### 7. 局限与风险
*   **外推风险：** 实验主要在人类标准细胞系上完成，对于结构变异严重（如癌症细胞）或物种差异巨大的基因组，模型的泛化能力有待验证。
*   **数据偏差：** 训练依赖于高质量的 Ground Truth 数据，如果原始高分辨率数据本身存在实验噪声，模型可能会“学习”并放大这些错误。
*   **应用障碍：** 临床或基础研究者通常缺乏运行深度学习环境的能力，需要更简便的工具集成。

---

#### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群：** 从事三维基因组学、生物图像处理、以及寻找 Transformer 替代方案（如 SSM/Mamba）的研究者。
*   **后续可跟进的问题：** 能否将 Mamba 应用于更长程的 DNA 序列建模（如直接从 1D 序列预测 3D 结构），或者处理单细胞 Hi-C 这种极度稀疏的数据？

（完）
