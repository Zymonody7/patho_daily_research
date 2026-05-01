---
title: "DeepSeMS: revealing the hidden biosynthetic potential of the global ocean microbiome with a large language model."
title_zh: DeepSeMS：利用大语言模型揭示全球海洋微生物组中隐藏的生物合成潜力
authors: "Tingjun Xu, Yuwei Yang, Ruixin Zhu, Weili Lin, Jixuan Li, Yan Zheng, Peng Zhang, Guoqing Zhang, Guoping Zhao, Na Jiao"
date: 2026-04-30
pdf: "https://pubmed.ncbi.nlm.nih.gov/42062603/"
tags: ["query:bioinfo"]
score: 10.0
evidence: 基于Transformer的大语言模型用于微生物组生物合成潜力预测
tldr: 针对微生物次级代谢产物发现受限于培养技术且生物合成基因簇（BGC）结构预测困难的问题，本研究开发了基于Transformer的大语言模型DeepSeMS。该模型通过将基因编码为功能域并结合特征对齐数据增强，实现了从BGC序列到化学结构的精准预测。在海洋宏基因组应用中，DeepSeMS成功挖掘出超6万种具有生物医药潜力的代谢产物，为探索地球微生物组的生物合成潜力提供了高效工具。
selection_source: fresh_fetch
motivation: 传统的微生物代谢产物发现依赖实验室培养，而宏基因组中海量的生物合成基因簇因结构复杂和功能预测不准而难以转化为具体的化学结构。
method: 开发了名为DeepSeMS的Transformer大语言模型，将生物合成基因编码为功能域序列，并利用特征对齐的数据增强技术来提升预测精度。
result: "DeepSeMS在预测准确率上超越了现有方法，为96.38%的隐性BGC生成了有效的化学结构，并从全球海洋宏基因组中识别出6万多种具有抗生素等潜力的次级代谢产物。"
conclusion: 该研究证明了深度学习模型在解析复杂生物合成路径及挖掘未开发生态系统生物医药资源方面的巨大潜力。
---

## 摘要
微生物来源的次级代谢产物（SMs）具有巨大的治疗潜力，但目前主要从已培养的物种中发现，这仅代表了微生物生物多样性的一小部分。宏基因组学的进展揭示了生物合成基因簇（BGCs）的资源库，但由于隐性 BGCs 的结构复杂性，以及模块化生物合成结构域的上下文依赖性底物耐受性和交叉反应性，将基因组序列转化为精确的化学结构仍然具有挑战性。在此，我们提出了 DeepSeMS，这是一种基于 Transformer 的大语言模型，能够根据 BGC 序列准确预测次级代谢产物的化学结构。通过将生物合成基因编码为功能结构域并利用特征对齐的数据增强，DeepSeMS 的表现优于现有方法，并成功为 96.38% 的隐性 BGCs 生成了化学有效的预测。将 DeepSeMS 应用于全球海洋宏基因组，我们鉴定了超过 60,000 种次级代谢产物，揭示了其化学多样性、生态特异性以及巨大的生物医学潜力，特别是作为抗生素的潜力。本研究强调了深度学习驱动的方法在揭示地球上最大但很大程度上尚未开发的微生物生态系统中隐藏的生物合成潜力方面的能力。

## Abstract
Microbial-derived secondary metabolites (SMs) hold great therapeutic potential but are predominantly discovered from cultured species, representing only a fraction of microbial biodiversity. Advances in metagenomics have unveiled reservoirs of biosynthetic gene clusters (BGCs), but translating genomic sequences into precise chemical structures remains challenging owing to the structural complexity of cryptic BGCs and the context-dependent substrate tolerance and cross-reactivity of modular biosynthetic domains. Here we present DeepSeMS, a transformer-based large language model that accurately predicts secondary metabolite chemical structures from BGC sequences. By encoding biosynthetic genes as functional domains and leveraging a feature-aligned data augmentation, DeepSeMS outperformed existing methods and successfully generated chemically valid predictions for 96.38% of cryptic BGCs. Applying DeepSeMS to a global ocean metagenome, we characterized over 60,000 secondary metabolites, revealing chemical diversity, ecological specificity and considerable biomedical potential, especially as antibiotics. This study underscores the capability of deep learning-driven approaches in revealing hidden biosynthetic potential of Earth's largest, yet largely unexplored, microbial ecosystem.

---

## 论文详细总结（自动生成）

### DeepSeMS：利用大语言模型揭示全球海洋微生物组中隐藏的生物合成潜力

#### 1. 核心问题与研究意义
微生物产生的**次级代谢产物**（如抗生素、抗癌药物）是人类药物的重要来源。然而，绝大多数微生物无法在实验室中人工培养，这导致我们虽然通过基因测序发现了海量的**生物合成基因簇（BGCs）**（即制造这些化合物的“基因蓝图”），却不知道它们到底能制造出什么样的化学结构。

这篇论文解决了**“从基因序列到化学结构”的精准预测问题**。由于 BGC 结构复杂且基因与产物之间并非简单的线性对应，传统方法难以处理这种“暗物质”数据。DeepSeMS 的出现，为从宏基因组数据中大规模挖掘新型候选药物提供了高效的计算工具。

---

#### 2. 白话版概述
*   微生物的 DNA 里藏着制造药物的“说明书”（BGC），但这些说明书是用一种复杂的生物语言写的。
*   科学家虽然在海洋里找到了成千上万份说明书，但看不懂它们最后会造出什么样的“零件”（化学分子）。
*   DeepSeMS 就像一个精通生物语言和化学语言的“翻译官”，它利用大语言模型技术，直接读入基因序列，然后“画”出对应的化学结构图。
*   通过这个模型，研究者在海洋中一口气找出了 6 万多种潜在的新药分子，极大地扩充了人类的天然产物库。

---

#### 3. 方法部分
*   **核心思想**：将生物合成过程类比为自然语言生成。BGC 序列是“句子”，其中的功能结构域（Domain）是“单词”，最终生成的化学结构（SMILES 字符串）是“翻译结果”。
*   **模型结构**：采用了基于 **Transformer** 的架构（Encoder-Decoder 结构）。
    *   **输入端（Encoder）**：不直接处理原始碱基（ATCG），而是将基因编码为**功能结构域序列**。这样做能过滤掉非功能性的噪声，捕捉蛋白质层面的语义。
    *   **输出端（Decoder）**：生成化学分子的 **SMILES 表达式**（一种用文本表示分子结构的通用标准）。
*   **关键设计**：
    *   **特征对齐的数据增强**：针对“基因-结构”配对数据稀缺的问题，模型通过对齐生物特征和化学特征进行数据增强，提升了模型在处理从未见过的“隐性 BGC”时的泛化能力。
    *   **Token 化策略**：将复杂的生物大分子拆解为标准化的功能单元，降低了模型的学习难度。

---

#### 4. 实验部分
*   **数据源**：全球海洋宏基因组数据（Global Ocean Metagenome）。
*   **任务**：根据 BGC 序列预测次级代谢产物的化学结构。
*   **Baseline（对比方法）**：文中对比了现有的生物信息学预测工具（如传统的基于规则的方法）。
*   **评价指标**：
    *   **化学有效性（Validity）**：生成的字符串是否符合化学价键规律。
    *   **结构多样性**：预测产物与已知库的差异。
    *   **生物活性预测**：预测产物是否具有抗生素等潜力。
*   **主要结果**：
    *   DeepSeMS 为 **96.38%** 的隐性 BGC 生成了化学上有效的预测结构。
    *   从海洋数据中识别出 **60,000 多种** 次级代谢产物。
    *   发现这些产物具有显著的生态特异性（不同海域产物不同）和极高的抗生素开发潜力。

---

#### 5. 资源与算力
*   **文中未充分披露**具体的 GPU 型号、训练时长或参数规模。但考虑到其基于 Transformer 且处理的是结构域序列而非全基因组碱基，其算力消耗应低于通用的千亿级 LLM。

---

#### 6. 真正可信的贡献
*   **高成功率的结构生成**：96.38% 的有效性证明了 Transformer 在处理生物合成“语法”上的强大能力。
*   **填补了“序列-结构”鸿沟**：过去的方法大多只能预测 BGC 的类型（如“这是一个聚酮类”），而 DeepSeMS 能给出具体的分子结构。
*   **大规模实战验证**：通过对全球海洋数据的挖掘，证明了模型在处理真实世界、高噪声宏基因组数据时的鲁棒性。

---

#### 7. 局限与风险
*   **缺乏湿实验验证**：虽然预测了 6 万种化合物，但文中并未通过实验室合成和活性测试来验证这些预测分子的真实生物活性（这是此类 AI 论文的通病）。
*   **立体化学难题**：SMILES 字符串在描述分子的手性（3D 空间排列）方面存在局限，预测结构与真实天然产物的空间构型可能存在偏差。
*   **数据偏差**：模型性能高度依赖于已知 BGC 数据库，对于完全颠覆性的生物合成路径可能预测准度下降。

---

#### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事天然产物发现、生成式化学（Generative Chemistry）、以及宏基因组功能挖掘的研究者。
*   **后续可跟进的问题**：能否将 DeepSeMS 生成的 2D 结构与 AlphaFold 预测的酶蛋白 3D 结构相结合，通过“蛋白质-配体”对接（Docking）来进一步验证预测的准确性？

（完）
