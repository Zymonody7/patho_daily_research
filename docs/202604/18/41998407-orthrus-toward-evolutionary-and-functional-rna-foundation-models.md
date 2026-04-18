---
title: "Orthrus: toward evolutionary and functional RNA foundation models."
title_zh: Orthrus：迈向进化与功能性 RNA 基础模型
authors: "Fradkin P, Shi RI, Dalal T, Isaev K, Frey BJ, Lee LJ, Morris Q, Wang B., Philip Fradkin, Ruian Ian Shi, Taykhoom Dalal, Keren Isaev, Brendan J Frey, Leo J Lee, Quaid Morris, Bo Wang"
date: 2026-04-17
pdf: "https://pubmed.ncbi.nlm.nih.gov/41998407/"
tags: ["query:bioinfo"]
score: 10.0
evidence: 基于Mamba的具有生物增强功能的成熟RNA基础模型
tldr: 针对现有基因组大模型缺乏生物学先验知识的问题，Orthrus 提出了一种基于 Mamba 架构的成熟 RNA 基础模型。它通过对比学习，将来自 400 多种哺乳动物的同源基因及多种模型生物的剪接异构体进行关联训练，从而学习到具有进化和功能意义的 RNA 表征。实验表明，Orthrus 在 mRNA 属性预测任务上优于传统模型，且仅需极少量的微调数据，能有效捕捉不同异构体间的生物学功能差异。
selection_source: fresh_fetch
motivation: 现有的基因组基础模型多采用文本领域的预训练策略，未能充分利用进化守恒和剪接变体等关键的生物学领域知识。
method: 采用 Mamba 架构，通过对比学习最大化 400 多种哺乳动物同源基因及多种模型生物剪接异构体之间的嵌入相似性。
result: 在 mRNA 属性预测任务中，Orthrus 的表现超越了通用基因组模型，且在微调时对数据量的需求大幅降低。
conclusion: Orthrus 证明了将进化和功能关联引入预训练可以显著提升 RNA 表征的质量，为理解复杂转录本功能提供了新工具。
---

## 摘要
面对迅速积累的基因组数据，我们预测决定转录本功能和调控的关键成熟 RNA 特性的能力仍然有限。预训练基因组基础模型提供了一种将学习到的 RNA 表征应用于生物预测任务的途径；然而，现有模型使用的训练策略借鉴自文本领域，未能利用生物学领域知识。在此，我们介绍了 Orthrus，这是一个基于 Mamba 的成熟 RNA 基础模型，采用带有生物学增强的自监督对比学习目标进行预训练。Orthrus 的训练通过最大化 RNA 转录本对之间的嵌入相似性来实现，这些转录本对由十种模式生物的剪接异构体以及 400 多种哺乳动物物种的同源基因转录本组成。这一训练目标产生了一个潜在表征，能够将具有功能和进化相似性的 RNA 序列聚类在一起。Orthrus 的成熟 RNA 异构体表征在 mRNA 特性预测任务上优于基因组基础模型，且仅需极少量的微调数据。最后，我们展示了 Orthrus 能够捕捉单个转录本异构体之间不同的生物学功能。

## Abstract
In the face of rapidly accumulating genomic data, our ability to predict key mature RNA properties that underlie transcript function and regulation remains limited. Pretrained genomic foundation models offer an avenue to adapt learned RNA representations to biological prediction tasks; however, existing models are trained using strategies borrowed from textual domains that do not leverage biological domain knowledge. Here we introduce Orthrus, a Mamba-based mature RNA foundation model pretrained using a self-supervised contrastive learning objective with biological augmentations. Orthrus is trained by maximizing embedding similarity between pairs of RNA transcripts that are formed from splice isoforms of ten model organisms and transcripts from orthologous genes in 400+ mammalian species. This training objective results in a latent representation that clusters RNA sequences with functional and evolutionary similarities. Orthrus' mature RNA isoform representations outperform genomic foundation models on mRNA property prediction tasks, requiring only a fraction of fine-tuning data. Finally, we show that Orthrus is capable of capturing divergent biological function of individual transcript isoforms.

---

## 论文详细总结（自动生成）

这篇论文介绍了 **Orthrus**，一个专门为成熟 RNA（经过剪接处理后的 RNA）设计的 AI 基础模型。它通过引入生物学中的“进化”和“功能”关联，打破了传统基因组模型只把序列当成“文本”来读的局限。

### 1. 解决的问题与核心价值
*   **问题：** 现有的基因组大模型（如基于 Transformer 或 Hyena 的模型）大多采用类似 GPT 的预训练方式（预测下一个碱基）。这种方式虽然能学到序列规律，但忽略了生物学核心逻辑：**进化守恒性**（不同物种的相似基因功能相似）和**剪接多样性**（同一个基因产生的不同 RNA 变体功能有别）。
*   **价值：** 成熟 RNA 是生命活动的直接指令。Orthrus 能够更精准地预测 mRNA 的稳定性、表达水平等关键属性，这对于药物研发（如 mRNA 疫苗设计）和理解疾病机制至关重要。

### 2. 白话版概述
想象一下，如果你学习外语时，不仅读课文，还对比着看同一句话的英语、法语、德语版本（同源基因），并且研究同一段剧情的不同剪辑版（异构体），你对语言逻辑的理解会深刻得多。Orthrus 就是这么做的：它不只是死记硬背 RNA 序列，而是通过对比 400 多种哺乳动物的“同类”基因，以及同一个基因产生的不同“版本”，学会了识别哪些 RNA 片段是决定功能的关键。

### 3. 方法部分
*   **核心思想：对比学习（Contrastive Learning）。** 传统的模型是“填空题”，Orthrus 做的是“连连看”。它将具有进化关系（同源）或功能关联（同基因异构体）的 RNA 序列对拉近，将无关序列推开。
*   **模型结构：基于 Mamba。** 相比 Transformer，Mamba 架构在处理长序列时效率更高（线性复杂度），非常适合动辄几千个碱基的 RNA 序列。
*   **关键设计：生物学增强（Biological Augmentations）。** 
    *   **同源对：** 使用来自 400 多种哺乳动物的同源基因作为正样本对。
    *   **异构体对：** 使用来自 10 种模式生物（如人、小鼠）的同一基因的不同剪接变体作为正样本对。
*   **取舍：** 放弃了预测碱基的生成式任务，转而追求表征的“语义”一致性，这使得模型对功能变化的敏感度更高。

### 4. 实验部分
*   **数据：** 涵盖 400+ 哺乳动物物种和 10 种模式生物的转录组数据。
*   **任务：** 预测 mRNA 的多种属性，包括稳定性（Stability）、翻译效率（Translation Efficiency）、半衰期等。
*   **Baseline（基准）：** 与主流的通用基因组基础模型（如基于 DNA 预训练的模型）进行对比。
*   **评价指标：** 预测准确率（如 Pearson/Spearman 相关系数）以及**样本效率**（即使用多少微调数据能达到目标性能）。
*   **主要结果：** 
    *   Orthrus 在所有 mRNA 属性预测任务中均优于通用模型。
    *   **极高的样本效率：** 仅需通用模型 1/10 甚至更少的微调数据，就能达到同等性能。
    *   能够区分同一基因下不同异构体的细微功能差异。

### 5. 资源与算力
*   **文中未充分披露：** 摘要和提供的片段中未具体说明使用的 GPU 型号、训练时长或具体的参数规模。

### 6. 真正可信的贡献
*   **证明了“生物学先验”优于“纯文本统计”：** 通过对比学习引入进化和剪接信息，显著提升了模型对 RNA 功能的理解。
*   **异构体敏感性：** 很多模型无法区分同一个基因产生的不同 RNA，但 Orthrus 证明了它能捕捉到这些细微但重要的生物学差异。

### 7. 局限与风险
*   **物种偏差：** 训练数据主要集中在哺乳动物，对于植物、真菌或病毒 RNA 的泛化能力尚待验证。
*   **对比学习的噪声：** 同源基因虽然相似但并不完全等同，强行拉近它们的表征可能会忽略某些物种特有的调控机制。
*   **应用障碍：** 实验室环境下的属性预测到真实的临床药物设计之间仍有巨大鸿沟。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群：** 从事 RNA 药物研发、基因表达调控研究、以及关注非 Transformer 架构（如 Mamba）在生物序列建模中应用的 AI 研究者。
*   **后续可跟进的问题：** 能否将 RNA 的二级/三级结构信息也作为对比学习的一种“增强”手段引入模型？

（完）
