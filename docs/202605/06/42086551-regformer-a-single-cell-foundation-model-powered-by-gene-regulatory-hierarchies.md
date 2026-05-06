---
title: "RegFormer: a single-cell foundation model powered by gene regulatory hierarchies."
title_zh: RegFormer：一种由基因调控层级驱动的单细胞基础模型
authors: "Luni Hu, Hua Qin, Yilin Zhang, Yi Lu, Ping Qiu, Zhihan Guo, Lei Cao, Wenjian Jiang, Yixin Shen, Qianqian Chen, Yanbang Shang, Tianyi Xia, Ziqing Deng, Hansheng Zhao, Xun Xu, Shuangsang Fang, Yuxiang Li, Yong Zhang"
date: 2026-05-05
pdf: "https://pubmed.ncbi.nlm.nih.gov/42086551/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 整合基因调控网络与状态空间模型的基座模型
tldr: 针对单细胞RNA测序模型在处理长基因序列时效率低、且缺乏基因调控先验知识的问题，RegFormer 结合了 Mamba 状态空间模型与基因调控网络（GRN）层级结构。通过 2500 万个人类单细胞数据的预训练，该模型在细胞聚类、批次整合及药物反应预测等任务上超越了 scGPT 等主流模型，为理解基因调控机制提供了高效且具备生物学可解释性的基础模型。
selection_source: fresh_fetch
motivation: 现有的单细胞基础模型难以有效处理长序列基因数据，且往往忽略了基因之间固有的调控网络层级关系。
method: 该模型利用 Mamba 架构的高效长序列处理能力，并根据基因调控网络对基因进行排序，结合表达量与身份的双重嵌入来捕捉细胞状态。
result: 在 2500 万细胞的大规模预训练下，RegFormer 在细胞分类、基因扰动模拟和癌症药物反应预测等多个基准测试中均取得了最优性能。
conclusion: RegFormer 证明了将生物学先验知识与高效的状态空间模型相结合，能够显著提升单细胞表征学习的准确性与生物学解释力。
---

## 摘要
单细胞 RNA 测序 (scRNA-seq) 能够实现细胞多样性的高分辨率分析，但目前的计算模型往往无法整合调控先验、处理数据稀疏性或高效处理长基因序列。在此，我们提出了 RegFormer，这是一种将基因调控网络 (GRNs) 与基于 Mamba 的状态空间建模相结合的基础模型，克服了 Transformer 架构在可扩展性和上下文长度方面的局限性。RegFormer 通过双重嵌入对每个基因进行编码：用于定量表达的数值嵌入（value embedding）和用于调控身份的标记嵌入（token embedding），并按照 GRN 引导的基因顺序进行组织，以捕捉表达动态和层级调控。RegFormer 在涵盖 45 个组织和多种生物学背景的 2500 万个人类单细胞上进行了预训练，实现了卓越的可扩展性和生物学保真度。在全面的基准测试中，它始终优于最先进的单细胞基础模型（scGPT、Geneformer、scFoundation 和 scBERT），提供了更高的聚类准确度、改进的批次整合以及更精确的细胞类型注释。RegFormer 还能重建具有生物学一致性的 GRN，准确模拟对遗传扰动的转录响应，并增强了癌症细胞系的药物反应预测。通过将调控先验与高效的长序列 Mamba 建模相结合，RegFormer 为单细胞表示学习建立了一个具有生物学基础且可扩展的框架，从而能够更深入地洞察基因调控和细胞状态转变的机制。

## Abstract
Single-cell RNA sequencing (scRNA-seq) enables high-resolution profiling of cellular diversity, but current computational models often fail to incorporate regulatory priors, handle data sparsity, or efficiently process long gene sequences. Here, we present RegFormer, a foundation model that integrates gene regulatory networks (GRNs) with Mamba-based state-space modeling, overcoming the scalability and context-length limitations of Transformer architectures. RegFormer encodes each gene through dual embeddings, a value embedding for quantitative expression and a token embedding for regulatory identity, organized within a GRN-guided gene order to capture both expression dynamics and hierarchical regulation. Pretrained on 25 million human single cells spanning 45 tissues and diverse biological contexts, RegFormer achieves superior scalability and biological fidelity. Across comprehensive benchmarks, it consistently outperforms state-of-the-art single-cell foundation models (scGPT, Geneformer, scFoundation, and scBERT), delivering higher clustering accuracy, improved batch integration, and more precise cell type annotation. RegFormer also reconstructs biologically coherent GRNs, accurately models transcriptional responses to genetic perturbations, and enhances drug response prediction across cancer cell lines. By combining regulatory priors with efficient long-sequence Mamba modeling, RegFormer establishes a biologically grounded and scalable framework for single-cell representation learning, enabling deeper mechanistic insight into gene regulation and cellular state transitions.

---

## 论文详细总结（自动生成）

### RegFormer：由基因调控层级驱动的单细胞基础模型

#### 1. 解决的问题与研究意义
在单细胞研究中，科学家通过测序了解每个细胞内成千上万个基因的表达情况。现有的 AI 模型（如基于 Transformer 的 scGPT）面临三个痛点：
*   **计算效率低**：Transformer 的计算量随基因数量平方级增长，处理长序列（全基因组）非常吃力。
*   **忽视生物学逻辑**：大多数模型把基因看作无序的集合，忽略了基因之间天然存在的“领导与被领导”关系（即**基因调控网络 GRN**）。
*   **数据稀疏**：单细胞数据中很多基因表达值为 0，模型难以捕捉微弱但关键的信号。

**RegFormer 的意义**在于：它首次将高效的 **Mamba 架构**与**生物学先验知识（调控层级）**结合，在 2500 万细胞的大规模数据上证明了“懂生物逻辑的模型更强大”。

---

#### 2. 白话版概述
想象一个细胞是一间复杂的工厂，基因是工人。以前的 AI 模型只是把工人们随机排成一排来观察，效率低且看不出门道。RegFormer 做了两件事：第一，它按照工厂的“行政架构图”（调控网络）来给工人排队，让主管和下属排在一起；第二，它换掉了一直以来笨重的 Transformer 引擎，改用了一种叫 Mamba 的新型轻量化引擎。这使得模型不仅能看全工厂所有的工人，还能一眼看穿谁在指挥谁，从而更准确地判断工厂（细胞）的状态。

---

#### 3. 方法部分
*   **核心思想**：利用基因调控网络（GRN）作为结构先验，引导模型学习基因间的层级依赖关系，并利用 Mamba 架构实现线性级的计算扩展。
*   **模型结构**：
    *   **Mamba 骨干**：采用状态空间模型（SSM）架构，相比 Transformer，它在处理长序列时内存占用更低、速度更快。
    *   **双重嵌入（Dual Embedding）**：每个基因输入包含两个部分：**Token Embedding**（代表这是哪个基因）和 **Value Embedding**（代表该基因的表达量数值）。
*   **关键设计——GRN 引导排序**：
    *   研究者没有随机排列基因，而是根据已知的生物学调控关系对基因进行排序。将处于同一调控路径或层级的基因放在序列的邻近位置，方便模型捕捉局部和全局的调控信号。
*   **训练流程**：在 2500 万个人类单细胞数据上进行自监督预训练，学习基因表达的通用模式。

---

#### 4. 实验部分
*   **数据规模**：涵盖 45 个组织、多种疾病背景的 2500 万个单细胞。
*   **对比基准（Baselines）**：scGPT、Geneformer、scFoundation、scBERT 等当前最顶尖的模型。
*   **评价指标**：聚类准确度（ARI/NMI）、批次效应去除效果（ASW）、细胞类型标注准确率、扰动预测的皮尔逊相关系数等。
*   **主要结果**：
    *   **性能全面领先**：在细胞分类、批次整合等任务上均刷新了 SOTA（最高水平）。
    *   **调控重建**：能准确推断出基因之间的调控关系。
    *   **药物与扰动预测**：在预测“如果敲除某个基因”或“加入某种药物”后细胞会发生什么变化时，表现出极高的生物学保真度。

---

#### 5. 资源与算力
文中提到在 2500 万细胞上进行预训练，这属于极大规模的计算任务。虽然 Mamba 架构提升了效率，但此类规模通常需要数百块 A100/H100 级别的 GPU 运行数周。关于具体的 GPU 型号、训练时长及总算力消耗，**文中未充分披露**。

---

#### 6. 真正可信的贡献
1.  **架构验证**：证明了 Mamba 架构在单细胞领域完全可以替代 Transformer，且在大规模长序列任务上更具优势。
2.  **先验有效性**：有力证明了引入“基因调控层级”这一生物学常识，能显著提升模型对细胞内在逻辑的理解，而非单纯靠堆砌算力和数据。
3.  **下游任务的广度**：不仅能做分类，还能做药物反应预测和基因扰动模拟，展示了极强的通用性。

---

#### 7. 局限与风险
*   **对先验的依赖**：如果输入的基因调控网络（GRN）本身有误或不完整，可能会误导模型的排序逻辑。
*   **物种局限性**：目前主要针对人类数据，在跨物种（如从小鼠推导人类）的应用效果尚待验证。
*   **落地门槛**：尽管推理比 Transformer 快，但维护和微调这样一个超大规模基础模型对普通实验室仍有较高门槛。

---

#### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事单细胞组学、大规模生物序列建模、以及关注非 Transformer 架构（如 SSM/Mamba）在生物领域应用的 AI 研究者。
*   **后续可跟进的问题**：能否在训练过程中动态地学习和修正基因调控网络，而不是仅仅依赖静态的先验知识？

（完）
