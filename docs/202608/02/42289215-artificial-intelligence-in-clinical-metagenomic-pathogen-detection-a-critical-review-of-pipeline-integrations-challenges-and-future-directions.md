---
title: "Artificial intelligence in clinical metagenomic pathogen detection: A critical review of pipeline integrations, challenges, and future directions."
title_zh: 人工智能在临床宏基因组病原体检测中的应用：流程集成、挑战与未来方向的批判性综述
authors: "Jiayue Dai, Xinru Tan, Jun Ma"
date: 2026-08-01
pdf: "https://pubmed.ncbi.nlm.nih.gov/42289215/"
tags: ["query:pathoai"]
score: 9.0
evidence: 临床宏基因组病原体检测与分类的AI综述
tldr: 临床宏基因组测序（mNGS）在病原体检测中面临计算量大、背景噪声干扰及难以识别变异物种等挑战。本文综述了深度学习（如CNN、Transformer）在原始序列处理、宿主过滤及分类中的应用，指出虽然AI在模拟数据上表现优异，但在临床转化中仍面临可解释性不足和缺乏标准化验证等瓶颈。该综述为构建实时、精准的临床诊断系统提供了技术路径与未来方向。
selection_source: fresh_fetch
motivation: 传统mNGS分析流程在处理海量数据时难以平衡检测速度与灵敏度，且难以从复杂的宿主背景中精准识别新型或高度变异的病原体。
method: 评估了卷积神经网络、长短期记忆网络及Transformer等架构在序列去噪、分类识别及耐药性预测等关键环节的集成应用。
result: 发现AI模型在基准测试中展现出高准确率，但现有研究多依赖模拟数据集，在实际临床环境下的泛化能力和可解释性仍待验证。
conclusion: 未来需通过开发基因组大模型和多模态临床数据融合，并加强软件医疗器械监管合规性，以实现mNGS从实验室到临床决策的跨越。
---

## 摘要
宏基因组二代测序（mNGS）通过实现对患者样本中微生物的非培养依赖性检测，扩大了临床诊断的范围。然而，mNGS 的临床应用仍受限于巨大的计算需求、参考数据库偏倚，以及区分真实病原体与宿主背景、共生菌群及环境污染的持续挑战。传统的比对和基于 k-mer 的生物信息学流程往往难以在速度、灵敏度以及检测高度变异或新型生物的能力之间取得平衡。本综述批判性地综合了人工智能（AI）和机器学习（ML）在 mNGS 诊断流程中的应用现状，探讨了集成到原始读段处理、宿主序列去除、初步分类学鉴定以及抗生素耐药性（AMR）和毒力因子辅助检测中的深度学习架构，包括卷积神经网络（CNN）、长短期记忆网络（LSTM）和 Transformer。尽管几种 AI 方法在基准测试研究中报告了较高的分类准确率，但我们注意到，大多数性能声明源自模拟数据集或受控的模拟群落，而非前瞻性临床验证。目前仍存在显著差距，包括前端信号优化中的 AI 集成有限、自动化临床报告不足、缺乏标准化的基准测试指标，以及关于数据泄漏、可重复性和泛化性的未决问题。成功的临床转化将需要解决当前可解释 AI 方法的解释性局限，应对医疗器械软件（SaMD）复杂且不断变化的监管环境，并弥合计算可行性与已证实的患者获益之间的差距。基因组基础模型的发展和多模态临床集成有望推动 mNGS 向实时、可操作的诊断方向发展，尽管在目前的原理验证演示与经过验证的临床部署之间仍存在巨大的证据差距。

## Abstract
Metagenomic next-generation sequencing (mNGS) has expanded the scope of clinical diagnostics by enabling culture-independent detection of microorganisms in patient samples. However, mNGS clinical utility remains constrained by substantial computational demands, reference database biases, and the persistent challenge of distinguishing true pathogens from host background, commensal flora and environmental contamination. Traditional alignment and k-mer-based bioinformatics pipelines frequently struggle to balance speed, sensitivity, and the ability to detect highly divergent or novel organisms. This review critically synthesizes the current landscape of Artificial Intelligence (AI) and Machine Learning (ML) applications across the mNGS diagnostic pipeline, examining deep learning architectures-including Convolutional Neural Networks (CNNs), Long Short-Term Memory networks (LSTMs), and Transformers-as integrated into raw read processing, host sequence depletion, primary taxonomic classification, and ancillary detection of antimicrobial resistance (AMR) and virulence factors. While several AI methodologies report high classification accuracy in benchmarking studies, we note that most performance claims derive from simulated datasets or controlled mock communities rather than prospective clinical validation. Significant gaps persist, including limited AI integration in front-end signal optimization, inadequate automated clinical reporting, absence of standardized benchmarking metrics, and unresolved questions regarding data leakage, reproducibility, and generalizability. Successful clinical translation will require addressing the interpretability limitations of current explainable AI approaches, navigating complex and evolving regulatory landscapes for Software as a Medical Device (SaMD), and bridging the gap between computational feasibility and demonstrated patient-outcome benefit. The development of genomic foundation models and multi-modal clinical integration holds promise for advancing mNGS toward real-time, actionable diagnostics, though substantial evidence gaps remain between current proof-of-concept demonstrations and validated clinical deployment.

---

## 论文详细总结（自动生成）

这篇综述论文对人工智能（AI）在**临床宏基因组病原体检测（mNGS）**中的应用进行了深度剖析。以下是针对 AI 研究者的结构化总结：

### 1. 核心问题与研究意义
*   **核心问题**：临床宏基因组测序（mNGS）旨在不经过细菌培养，直接从患者样本（如血液、脑脊液）中通过测序识别所有微生物。但面临三大痛点：
    1.  **海量噪声**：样本中 99% 以上往往是人类自身的 DNA（宿主背景），病原体信号极微弱。
    2.  **计算瓶颈**：传统比对算法（如 BLAST）在处理数亿条短序列时速度极慢。
    3.  **变异挑战**：传统方法依赖已知数据库，难以识别高度变异的病毒或新型病原体。
*   **研究意义**：本文系统梳理了 AI 如何替代或增强传统生信流程，是理解“基因组学+深度学习”前沿趋势的必读综述。

### 2. 白话版概述
想象你在一个万人嘈杂的体育场里，要通过录音找出其中一个特定的人在说什么。
*   **传统方法**是拿着字典一个词一个词地对，如果那个人说话带口音或者用了新词，你就找不到了。
*   **AI 方法**则是训练一个“听力高手”，它能自动过滤背景杂音（宿主过滤），识别出不同语种的特征（分类学鉴定），甚至能听出这个人是否带有“武器”（耐药性预测）。
这篇论文总结了目前这类“听力高手”（CNN、Transformer 等）的表现，并指出它们虽然在模拟考试中成绩很好，但在真实医院环境里还没完全证明自己。

### 3. 方法部分：AI 如何介入流程
论文将 AI 的集成分为四个关键环节：
*   **原始数据处理（Raw Read Processing）**：利用 CNN 或 RNN 进行序列去噪和质量控制，识别测序过程中的随机错误。
*   **宿主序列去除（Host Depletion）**：这是典型的二分类任务。AI 模型学习人类基因组的特征，快速剔除属于患者的序列，从而减少后续计算量。
*   **分类学鉴定（Taxonomic Classification）**：
    *   **核心思想**：将 DNA 序列看作文本，利用 NLP 技术进行特征提取。
    *   **模型结构**：从早期的 **CNN**（捕获局部 k-mer 特征）到 **LSTM**（捕获长程依赖），再到目前的 **Transformer/BERT** 架构（通过自注意力机制理解序列全局背景）。
*   **功能预测**：利用深度学习预测病原体是否携带抗生素耐药基因（AMR）或毒力因子，这通常被建模为多标签分类任务。

### 4. 实验与评估现状
*   **数据来源**：目前绝大多数研究使用的是**模拟数据集**（如使用工具人工合成的读段）或**受控模拟群落**（Mock Communities，即人工混合的已知菌种）。
*   **基准对比（Baseline）**：通常与传统工具如 Kraken2（基于 k-mer 匹配）或 Centrifuge 进行对比。
*   **评价指标**：准确率（Accuracy）、灵敏度（Sensitivity）、特异性（Specificity）以及推理速度（Inference Time）。
*   **主要结果**：AI 模型在处理“短读段”和“高变异序列”时显著优于传统工具，但在处理数据库中从未见过的完全新型物种时，仍存在假阳性问题。

### 5. 资源与算力
*   **文中未充分披露**：作为综述，本文未列出具体模型的训练时长或 GPU 消耗，但强调了 AI 模型在推理阶段（Inference）通常比传统的大型数据库比对更节省内存和时间。

### 6. 真正可信的贡献
*   **明确了 AI 的优势区间**：AI 最强的贡献在于**“模糊匹配”**能力，能够识别出与参考基因组有一定差异的变异株，这是传统精确匹配算法的死穴。
*   **流程集成框架**：论文清晰地定义了 AI 在 mNGS 全生命周期中的位置，为开发者提供了技术路线图。

### 7. 局限与风险
*   **临床验证缺失**：大多数 AI 模型在实验室模拟数据上表现近乎完美，但在复杂的临床样本（含多种污染物、降解 DNA）中表现往往大幅下降。
*   **可解释性危机（黑盒问题）**：医生需要知道“为什么判定是这种病毒”，而深度学习模型难以给出生物学上的解释，这在医疗监管（如 FDA 审批）中是巨大障碍。
*   **数据泄露风险**：训练集和测试集如果存在同源序列，会导致性能虚高。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：对基因组大模型（Genomic Foundation Models）、序列标注任务、以及医疗 AI 落地感兴趣的研究者。
*   **后续可跟进的问题**：如何利用**多模态学习**（将患者的临床症状、生化指标与基因组数据融合）来提高诊断的准确性？

（完）
