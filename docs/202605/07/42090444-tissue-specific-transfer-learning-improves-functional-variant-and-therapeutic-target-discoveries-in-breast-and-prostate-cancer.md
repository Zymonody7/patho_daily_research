---
title: Tissue-specific transfer learning improves functional variant and therapeutic target discoveries in breast and prostate cancer.
title_zh: 组织特异性迁移学习改进了乳腺癌和前列腺癌的功能性变异和治疗靶点发现
authors: "Qing Li, Dinghao Wang, Zilong Zhang, Deshan Perera, Zhishan Chen, Wanqing Wen, M Ethan MacDonald, Weijia Cai, Jun Yan, Xiao-Ou Shu, Wei Zheng, Xingyi Guo, Quan Long"
date: 2026-05-06
pdf: "https://pubmed.ncbi.nlm.nih.gov/42090444/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 用于调控变异解释的DNA基础模型
tldr: 针对现有DNA基础模型在特定组织背景下预测精度不足的问题，本研究提出了一种迁移学习框架，通过整合乳腺癌和前列腺癌特有的转录因子ChIP-seq数据对Enformer模型进行微调。该方法计算出的组织特异性顺式调节活性（tCRA）评分能更精准地识别癌症相关的风险变异。实验证明，该模型在识别致病变异、增强子富集以及发现潜在药物靶点方面均优于原始模型，为精准医疗中的变异解释提供了通用且高效的适配方案。
selection_source: fresh_fetch
motivation: 现有的基因组基础模型在处理特定组织或疾病背景下的调控变异时，往往缺乏足够的针对性和预测精度。
method: 通过引入数百个乳腺癌和前列腺癌特有的转录因子ChIP-seq数据，对预训练的Enformer模型进行迁移学习微调，构建组织特异性的预测模型。
result: 微调后的模型在识别癌症风险变异、致病性变异以及关联具有治疗价值的靶向基因方面，其性能一致性地优于原始的通用模型。
conclusion: 该研究展示了迁移学习在定制化基因组基础模型方面的巨大潜力，为特定疾病的变异解释和药物靶点发现提供了更精准的计算工具。
---

## 摘要
在大规模基因组和表观基因组数据集上训练的 DNA 基础模型在调控变异解释方面展现出潜力，但其在组织特异性背景下的应用仍然有限。在这里，我们提出了一个迁移学习（TL）框架，利用 275 个和 357 个组织特异性转录因子（TF）ChIP-seq 轨道，将 Enformer（一个在 5,313 个多组学轨道上训练的深度神经网络）分别适配到乳腺癌和前列腺癌中。我们计算了全基因组关联研究（GWAS）数据集中数百万个单核苷酸变异（SNV）的组织特异性顺式调控活性（tCRA）评分，并优先排序了高影响力的 SNV 子集（1M、1.5M 和 2M）。与原始 Enformer 模型相比，这些经 TL 优先排序的变异在组织特异性增强子、癌症 GWAS 风险变异和 ClinVar 致病变异中表现出持续更高的富集度。使用基于 TL 的 SNV 进行的全转录组关联研究（TWAS）识别出更多癌症相关基因，其中许多基因表现出功能必需性（DepMap）、治疗可行性（药物数据库）和疾病相关性（DisGeNET）。值得注意的是，TL 模型在识别富集药物靶点和临床相关疾病关联的基因方面优于基础模型。我们的结果表明，TL 衍生的 tCRA 评分增强了调控变异的优先排序，并以组织特异性的方式改进了易感基因的发现。我们的研究提供了一个通用的框架，用于将基础模型定制到疾病相关背景中，对变异解释、治疗靶点发现和精准医学具有重要意义。

## Abstract
DNA foundation models trained on large-scale genomic and epigenomic datasets have shown promise for regulatory variant interpretation, yet their application to tissue-specific contexts remain limited. Here, we present a transfer learning (TL) framework to adapt Enformer, a deep neural network trained on 5,313 multi-omics tracks, to breast and prostate cancer using 275 and 357 tissue-specific transcription factor (TF) ChIP-seq tracks, respectively. We computed tissue-specific cis-regulatory activity (tCRA) scores for millions of single-nucleotide variants (SNVs) in genome-wide association study (GWAS) datasets and prioritized high-impact SNV subsets (1M, 1.5M, and 2M). These TL-prioritized variants demonstrated consistently greater enrichment in tissue-specific enhancers, cancer GWAS risk variants, and ClinVar pathogenic variants compared to the original Enformer model. Transcriptome-wide association studies (TWAS) using TL-based SNVs identified more cancer-relevant genes, many of which exhibited functional essentiality (DepMap), therapeutic tractability (drug databases), and disease relevance (DisGeNET). Notably, TL models outperformed the base model in identifying genes enriched for drug targets and clinically relevant disease associations. Our results show that TL-derived tCRA scores enhance regulatory variant prioritization and improve susceptibility gene discovery in a tissue-specific manner. Our study provides a generalizable framework for tailoring foundation models to disease-relevant contexts, with implications for variant interpretation, therapeutic target discovery, and precision medicine.

---

## 论文详细总结（自动生成）

这篇论文由范德堡大学和卡尔加里大学的研究团队发表，探讨了如何通过**迁移学习（Transfer Learning）**让通用的 DNA 大模型“学会”识别特定癌症中的关键基因变异。

### 1. 解决的问题与研究意义
*   **核心问题**：现有的 DNA 基础模型（如 Enformer）虽然在预测基因表达方面很强，但它们像“通才”，对特定组织（如乳腺或前列腺）的敏感度不足。在癌症研究中，绝大多数致病变异发生在不编码蛋白质的“垃圾 DNA”区（调控区），如何从数百万个变异中精准找出真正驱动癌症的那几个，是目前精准医疗的瓶颈。
*   **研究意义**：通过让模型“专精”于特定癌症组织，可以显著提高识别癌症风险基因和治疗靶点的准确率，减少生物实验的盲目性。

### 2. 白话版概述
想象你有一个精通全球语言的翻译官（通用 DNA 模型），但他不懂医学术语。这篇论文通过给他看成百上千份乳腺癌和前列腺癌的“专业病历”（组织特异性 ChIP-seq 数据），把他训练成了这两个领域的专家。这个“专家模型”能更准确地判断 DNA 序列中某个微小的字母改变（变异）是否会破坏细胞的正常调控，从而导致癌症。实验证明，这个专家比原来的通才更能精准定位药物靶点。

### 3. 方法部分
*   **核心思想**：利用迁移学习，将预训练好的 **Enformer** 模型（已学习过 5000 多个通用组学轨道）作为特征提取器，针对乳腺癌和前列腺癌进行“微调”。
*   **模型结构**：保留 Enformer 强大的 Transformer 架构（擅长捕捉 DNA 长距离依赖关系），但在输出层引入了特定组织的**转录因子 ChIP-seq 轨道**（乳腺癌 275 个，前列腺癌 357 个）。
    *   *注：ChIP-seq 是一种实验技术，用来检测蛋白质（如转录因子）结合在 DNA 的哪些位置，这决定了基因的开关。*
*   **关键设计**：计算 **tCRA 评分**（组织特异性顺式调节活性评分）。该评分衡量的是：如果 DNA 序列发生单点突变，模型预测的该组织调控活性会发生多大的变化。
*   **取舍**：研究者没有从头训练模型（成本极高且数据不足），而是选择了迁移学习，这在保证模型深度和复杂度的同时，利用了有限的组织特异性数据。

### 4. 实验部分
*   **数据源**：使用了乳腺癌和前列腺癌的 GWAS（全基因组关联研究）数据集、ClinVar（临床已知致病变异库）、DepMap（癌细胞生存必需基因库）以及各类药物数据库。
*   **对比基准（Baseline）**：原始的、未经过微调的 Enformer 基础模型。
*   **评价指标**：变异在增强子区的富集度、识别致病变异的准确率、TWAS（全转录组关联研究）识别出的癌症相关基因数量。
*   **主要结果**：
    1.  **更精准的变异筛选**：TL 模型筛选出的高影响力变异，在已知致病变异（ClinVar）和癌症风险位点中的富集程度显著高于原始模型。
    2.  **发现更多靶点**：在 TWAS 分析中，TL 模型识别出了更多与癌症生存相关的“必需基因”，且这些基因与现有药物靶点的重合度更高。

### 5. 资源与算力
*   **文中未充分披露**具体的 GPU 型号和训练时长。但考虑到 Enformer 模型的参数量和微调数百个轨道的工作量，通常需要工业级显卡（如 A100/H100 集群）支持。

### 6. 真正可信的贡献
*   **结论证据最强处**：该研究不仅在计算指标（如富集度）上取得了提升，还通过 **DepMap（功能必需性）** 和 **药物数据库（治疗可行性）** 进行了交叉验证。这意味着模型找出的基因不仅在统计学上相关，在生物学功能和临床治疗上也确实有意义。
*   **方法论贡献**：证明了“通用大模型 + 组织特异性微调”是解释非编码区变异的一条高效路径。

### 7. 局限与风险
*   **数据偏差**：ChIP-seq 数据质量参差不齐，且目前仅覆盖了乳腺和前列腺，其他缺乏高质量组学数据的罕见癌种可能难以复现。
*   **生物学简化**：模型主要关注顺式调控（近距离），对复杂的染色质三维结构和反式调控（远距离跨染色体）的模拟仍有局限。
*   **应用障碍**：预测出的“潜在靶点”仍需大量湿实验验证，从计算预测到临床药物开发还有极长的路。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事基因组基础模型开发、调控基因组学研究以及计算药学的人员。
*   **后续可跟进的问题**：如何利用**少样本学习（Few-shot Learning）**在缺乏大规模 ChIP-seq 数据的组织中实现类似的精准预测？

（完）
