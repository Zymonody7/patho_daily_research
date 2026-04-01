---
title: "TCMNet: an AI-driven strategy for optimizing traditional Chinese medicine."
title_zh: TCMNet：一种用于优化中医药的 AI 驱动策略
authors: "Shuoyan Tan, Xin Shao, Xuting Zhang, Yizheng Dai, Boli Zhang, Yiyu Cheng, Xiaohui Fan"
date: 2026-03-31
pdf: "https://pubmed.ncbi.nlm.nih.gov/41918015/"
tags: ["query:bioinfo"]
score: 8.0
evidence: 集成大语言模型和深度学习的AI驱动药物发现策略
tldr: 针对中药方剂设计主观性强、靶点优先级缺乏权重等问题，研究者开发了 TCMNet 策略。该方法融合了专用大模型 TCMChat 提取的语义权重、加权蛋白质相互作用网络（PPI）以及 Boltz-2 深度学习结合预测。在帕金森病案例中，TCMNet 成功评估了天麻钩藤饮等经典方剂及中西医结合方案的疗效，并识别出银杏叶中的黄酮类活性成分，为中药方剂的现代化优化和活性成分鉴定提供了量化工具。
selection_source: fresh_fetch
motivation: 传统中药方剂设计往往依赖主观经验，且现有的网络药理学分析通常忽略了不同疾病靶点和药物成分之间的重要性差异。
method: TCMNet 利用中医药大模型 TCMChat 从文献中提取带权重的疾病靶点，结合药物成分丰度构建加权 PPI 网络，并利用 Boltz-2 深度学习模型验证化合物与蛋白的结合概率。
result: 实验证明加权评估指标优于传统无权重方法，不仅验证了天麻钩藤饮等方剂的有效性，还发现中西医结合方案在网络邻近度上显著优于单一疗法。
conclusion: TCMNet 通过引入大模型引导的权重机制，实现了对中药方剂疗效的精准量化评估和活性成分的高效筛选，推动了中医药研究的数字化转型。
---

## 摘要
背景：人工智能（AI），特别是大语言模型（LLMs），为系统地模拟中医药（TCM）的复杂性提供了强大的工具。为了克服主观方剂设计和无权重靶点优先级排序的局限性，我们开发了 TCMNet，这是一种 AI 驱动的策略，集成了 LLM 辅助的疾病知识挖掘、蛋白质-蛋白质相互作用（PPI）网络以及基于深度学习的结合预测，以支持中药方剂评估和活性化合物鉴定。方法：TCMNet 将 AI 引导的文献分析与加权 PPI 网络评估相结合。选择帕金森病（PD）作为代表性案例研究。使用 TCMChat（一种从中英文文献中提取相关靶点的中医药专用 LLM）对疾病相关蛋白靶点进行语义加权。此外，利用中药特定信息数据（如配伍比例、化合物丰度和化合物-蛋白质相互作用概率）生成加权的中药相关蛋白。这些权重被整合到 PPI 网络中，为每个节点分配生物学权重。系统评估了四种经典中医方剂（天麻钩藤饮、六味地黄丸、牵正散、大补阴丸）、临床优化的平颤颗粒（PCG）及其与西药（左旋多巴）的联合用药方案，并与单味药银杏叶进行了对比。使用基于网络的指标（如靶点覆盖度、Jaccard 相似度和加权邻近度）评估治疗相关性，并通过 Z 分数衡量统计显著性。为了验证关键活性化合物，我们采用了最先进的深度学习方法 Boltz-2，预测中药化合物与优先排序的 PD 相关蛋白之间的结合概率。结果：在所有四种评估的中医方剂中，加权邻近度指标明显优于未加权指标，证明了整合节点权重的显著优势。在评估的方剂中，天麻钩藤饮在靶点覆盖度和网络邻近度方面表现优异，与现有文献高度一致。对平颤颗粒（PCG）的计算验证确认，TCMNet 成功捕捉到了方剂优化的治疗保留效应。与单药治疗相比，中药与左旋多巴结合的综合策略表现出显著增强的网络邻近度，支持了联合治疗的合理性。此外，案例研究确定了银杏叶中的黄酮类和异黄酮类化合物是贡献抗 PD 活性的主要生物活性成分。Boltz-2 深度学习预测进一步证实，与非黄酮类化合物相比，黄酮类化合物对关键 PD 相关蛋白表现出显著更高的结合概率和亲和力，从而验证了 TCMNet 的结果。结论：通过结合 LLM 引导的靶点识别与节点加权评估，显式地整合蛋白质权重，TCMNet 为优化中医药提供了一种新的 AI 驱动策略。该方法实现了中药方剂的评估与优化以及生物活性成分的鉴定，推动了草药研究的现代化。

## Abstract
BACKGROUND: Artificial intelligence (AI), particularly large language models (LLMs), have provided powerful tools for systematically modeling the complexity of traditional Chinese medicine (TCM). To overcome the limitations of subjective formula design and unweighted target prioritization, we developed TCMNet, an AI-powered strategy that integrates LLM-assisted disease knowledge mining, protein-protein interaction (PPI) networks, and deep learning-based binding prediction to support herbal formula evaluation and active compounds identification. METHODS: TCMNet integrates AI-guided literature analysis with weighted PPI network evaluation. Parkinson's disease (PD) was chosen as the representative case study. Disease-associated protein targets were semantically weighted using TCMChat, a TCM-specific LLM that extracts relevant targets from Chinese and English literature. Furthermore, herb-specific information data, such as composition ratios, compound abundance, and compound-protein interaction probabilities, was used to generate weighted herb-related proteins. These weights were incorporated into a PPI network to assign biological weight to each node. Four classical TCM formulas (Tianma Gouteng Decoction, Liuwei Dihuang, Qianzheng San, Dabuyin Wan), the clinically optimized Pingchan Granule (PCG), and their integrative combinations with Western medicine (Levodopa) were systematically evaluated alongside the single-herb Ginkgo biloba. Therapeutic relevance was assessed using network-based metrics such as target coverage, Jaccard similarity, and weighted proximity, with statistical significance measured by Z-scores. To validate key active compounds, we employed Boltz-2, a state-of-the-art deep learning method, to predict the binding probabilities between herbal compounds and prioritized PD-associated proteins. RESULTS: Weighted proximity metrics markedly outperformed unweighted measures across all four evaluated TCM formulas, demonstrating the substantial benefit of integrating node weights. Among the evaluated formulas, Tianma Gouteng Decoction demonstrated superior performance in target coverage and network proximity, aligning well with existing literature. Computational validation on Pingchan Granule (PCG) confirmed that TCMNet successfully captures the therapeutic retention of formula optimization. Furthermore, integrative strategies combining TCM with Levodopa exhibited significantly enhanced network proximity compared to monotherapy, supporting the rationale for combined treatment. Moreover, the case study identified flavonoids and isoflavonoids from Ginkgo biloba as the primary bioactive constituents contributing to anti-PD activity. Boltz-2 deep learning predictions further confirmed that flavonoid compounds exhibited significantly higher binding probabilities and affinities toward key PD-associated proteins compared to non-flavonoids, thus validating the results of TCMNet. CONCLUSIONS: By explicitly incorporating protein weights through combining LLM-guided target identification with node-weighted evaluation, TCMNet offers a new AI-driven strategy for optimizing TCM. This approach enables herbal formula evaluation and optimization as well as the identification of bioactive constituents, advancing the modernization of herbal medicine research.

---

## 论文详细总结（自动生成）

这篇论文介绍了一个名为 **TCMNet** 的 AI 驱动框架，旨在通过大语言模型（LLM）和深度学习技术，解决中药方剂研究中“药效机制模糊”和“评价指标过于主观”的难题。

### 1. 解决的问题与研究意义
中药方剂通常由多种草药组成，含有成千上万种化合物，其作用机制是“多成分、多靶点”的复杂网络。
*   **痛点：** 传统的“网络药理学”分析通常把所有蛋白质靶点看作同等重要（无权重），这不符合生物学事实；同时，方剂的优化往往依赖经验，缺乏量化的科学评价。
*   **意义：** TCMNet 引入了**权重机制**，利用 AI 从海量文献中自动学习哪些靶点对疾病更重要，并能定量评估不同方剂、中西医结合方案的优劣，为中药现代化提供了“数字化标尺”。

### 2. 白话版概述
如果把治疗疾病比作一场战争，传统的分析方法只列出了敌我双方的名单，却不知道谁是“将军”，谁是“小兵”。TCMNet 先请一位“AI 专家”（大模型）阅读成千上万篇医学论文，给每个致病蛋白打分（定权重），找出关键目标。然后，它计算中药成分对这些关键目标的“打击精准度”。最后，它还用一种高精度的“分子模拟器”（Boltz-2）来验证这些药物成分是否真的能紧紧锁住目标蛋白。

### 3. 方法部分：核心思想与流程
TCMNet 的核心是将**语义知识**转化为**数学权重**，并整合进生物网络中。
*   **核心思想：** 建立一个“加权蛋白质相互作用网络（PPI）”。
*   **推理流程：**
    1.  **目标加权（LLM 引导）：** 使用中医药专用大模型 **TCMChat** 扫描中英文文献，根据蛋白与疾病（如帕金森病）的相关性频率和语义强度，给蛋白节点分配权重。
    2.  **药物加权：** 考虑草药的配伍比例、化合物在药材中的含量（丰度）以及化合物与蛋白结合的概率，计算出药物侧的权重。
    3.  **网络评价：** 引入“加权邻近度（Weighted Proximity）”指标。简单说，就是计算药物靶点在网络中距离疾病核心靶点有多近。
    4.  **深度学习验证：** 使用 **Boltz-2**（一种类似 AlphaFold 3 的深度学习模型）预测药物分子与蛋白的结合亲和力，从物理层面验证 AI 的推断。
*   **关键取舍：** 放弃了传统的“全或无”二元连接模型，选择了“连续权重”模型，以更真实地模拟生物分子的相互作用强度。

### 4. 实验部分
*   **研究案例：** 帕金森病（PD）。
*   **测试对象：** 4 种经典方剂（如天麻钩藤饮、六味地黄丸等）、1 种临床优化方剂（平颤颗粒）、单味药（银杏叶）以及中西医结合方案（中药+左旋多巴）。
*   **评价指标：** 靶点覆盖度、Jaccard 相似度、加权邻近度、Z-score（统计显著性）。
*   **主要结果：**
    *   **加权指标更准：** 引入权重后，评价指标的区分度显著提升，能更准确地识别出真正有效的方剂。
    *   **方剂优劣排序：** 在帕金森病治疗中，**天麻钩藤饮**的表现优于其他经典方剂，这与临床经验一致。
    *   **中西医结合优势：** 实验证明“中药+左旋多巴”的网络邻近度显著高于单药治疗，从系统生物学角度解释了中西医结合的增效作用。
    *   **活性成分识别：** 识别出银杏叶中的**黄酮类化合物**是抗帕金森的关键成分，并得到了 Boltz-2 结合能预测的支持。

### 5. 资源与算力
*   **文中未充分披露**具体的硬件配置（如 GPU 型号或训练时长）。但提到了使用 TCMChat 大模型进行文本挖掘和 Boltz-2 进行分子对接预测，这两者通常需要高性能 GPU 集群支持。

### 6. 真正可信的贡献
*   **量化了“重要性”：** 成功将 LLM 的语义理解能力转化为网络药理学的数值权重，解决了传统分析中“靶点无差别化”的问题。
*   **验证了优化逻辑：** 通过对“平颤颗粒”的分析，证明了该框架能捕捉到方剂从“经典方”到“临床优化方”在药效上的保留和提升。
*   **多尺度验证：** 结论不仅来自宏观的网络计算，还得到了微观深度学习模拟（Boltz-2）的交叉验证，证据链相对完整。

### 7. 局限与风险
*   **文献偏差：** LLM 的权重完全基于现有文献。如果某种药物或靶点的研究较少（即使它很重要），AI 可能会低估它的权重。
*   **PPI 网络不完整：** 人类蛋白质相互作用网络本身尚不完全，这会限制网络分析的上限。
*   **缺乏湿实验：** 虽然有 Boltz-2 的模拟验证，但论文中缺乏直接的体外（细胞）或体内（动物）实验数据来最终证实预测的活性成分。
*   **真实应用障碍：** 中药成分进入人体后的代谢过程（PK/PD）非常复杂，TCMNet 目前主要基于静态网络，尚未充分考虑血脑屏障穿透率等药代动力学因素。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群：** 从事网络药理学、中药现代化、药物重定向（Drug Repurposing）以及生物医学知识图谱研究的研究者。
*   **后续可跟进的问题：** 如何将 LLM 提取的“文本证据”与单细胞测序等“实验证据”融合，构建动态的、具有细胞类型特异性的加权药效评价模型？

（完）
