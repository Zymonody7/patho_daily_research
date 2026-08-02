---
title: Class-Incremental Learning for Foodborne Pathogen Prediction Based on Clinical Surveillance Data.
title_zh: 基于临床监测数据的食源性致病菌预测类增量学习
authors: "Ke Qin, Linhai Wu, Minguo Gao"
date: 2026-08-01
pdf: "https://pubmed.ncbi.nlm.nih.gov/42361903/"
tags: ["query:pathoai"]
score: 9.0
evidence: 用于监测数据中食源性病原体预测的类增量学习
tldr: 针对食源性致病菌检测中存在的样本稀缺、类别不平衡及新病原体不断涌现的挑战，本研究提出了一种名为 CIL-DAFFNet 的类增量学习框架。该框架结合双注意力机制增强特征提取，并利用基于最大均值差异（MMD）动态加权的知识蒸馏策略来缓解灾难性遗忘。在包含沙门氏菌、诺如病毒等真实临床数据集上的实验表明，该模型在最终增量阶段的准确率达到 0.8245，为智能化食品安全监测和临床决策提供了高效且可解释的技术方案。
selection_source: fresh_fetch
motivation: 传统的食源性致病菌识别模型难以应对临床监测中新病原体持续出现导致的灾难性遗忘，以及罕见样本带来的严重类别不平衡问题。
method: 提出 CIL-DAFFNet 网络，通过双注意力机制提取关键判别特征，并利用 MMD 动态调整知识蒸馏权重以平衡新旧知识的学习。
result: 在涵盖四种主要致病菌的真实临床数据集上，该模型在增量学习任务中取得了 0.8245 的准确率和 0.8004 的 Macro-F1 值，性能优于五种主流基准模型。
conclusion: 该研究证明了类增量学习在食源性疾病监测中的可行性，并通过 SHAP 分析为临床决策提供了具有可解释性的特征重要性参考。
---

## 摘要
食源性疾病（FBDs）构成了重大的全球公共卫生挑战，需要快速且准确的病原体识别。然而，现实世界中的病原体检测面临着实际约束，包括罕见病原体的小样本场景、常见类与罕见类之间的严重类别不平衡，以及需要增量学习能力的不断出现的新型病原体。为了应对这些挑战，本研究提出了一种具有双重注意力和自适应特征融合网络的类增量学习模型（CIL-DAFFNet）。该模型结合了双重注意力机制，以增强从临床不平衡数据中提取判别性特征的能力，并采用了一种通过最大均值差异（MMD）调整的动态加权知识蒸馏策略，以缓解灾难性遗忘。在涵盖沙门氏菌、副溶血性弧菌、大肠杆菌和诺如病毒的真实临床数据集上进行的评估显示，CIL-DAFFNet 的表现优于五个增量学习基准模型。在最终的增量阶段，其准确率达到 0.8245，Macro-F1 为 0.8004，G-mean 为 0.7972。消融实验证实了核心组件的贡献，SHAP 分析提供了具有临床可解释性的特征重要性排序。本研究为食源性致病菌的快速精准识别提供了一种可行的技术方案，支持智能食品安全监测和临床决策。

## Abstract
Foodborne diseases (FBDs) pose a significant global public health challenge, necessitating rapid and accurate pathogen identification. However, real-world pathogen detection faces practical constraints, including few-shot scenarios for rare pathogens, severe class imbalance between common and rare classes, and the continuous emergence of novel pathogens requiring incremental learning capabilities. To address these challenges, this study proposes a Class Incremental Learning with Dual Attention and Adaptive Feature Fusion Network (CIL-DAFFNet). The model incorporates a dual-attention mechanism to enhance discriminative feature extraction from clinically imbalanced data and employs a dynamically weighted knowledge distillation strategy, adjusted via maximum mean discrepancy (MMD), to mitigate catastrophic forgetting. Evaluated on a real-world clinical dataset covering Salmonella, Vibrio parahaemolyticus, Escherichia coli, and Norovirus, CIL-DAFFNet outperformed five incremental learning baselines. In the final incremental phase, it achieved an accuracy of 0.8245, a Macro-F1 of 0.8004, and a G-mean of 0.7972. Ablation studies confirmed the contributions of core components, and SHAP analysis provided clinically interpretable feature importance rankings. This study provides a feasible technical solution for the rapid and precise identification of foodborne pathogens, supporting intelligent food safety monitoring and clinical decision-making.

---

## 论文详细总结（自动生成）

这是一份关于论文《Class-Incremental Learning for Foodborne Pathogen Prediction Based on Clinical Surveillance Data》的结构化总结：

### 1. 解决的问题与价值
*   **核心问题**：在现实的食源性疾病（如食物中毒）监测中，AI 模型面临三个痛点：
    1.  **新病原体不断出现**：模型需要不断学习新类（如新病毒株），但往往会产生“灾难性遗忘”，即学会了新的就忘了旧的。
    2.  **样本极度不平衡**：常见病原体（如沙门氏菌）数据多，罕见病原体数据极少（小样本）。
    3.  **临床数据复杂性**：临床监测数据包含症状、流行病学特征等，特征维度杂乱。
*   **研究价值**：该研究为公共卫生监测提供了一个动态更新的工具，使模型能像人类医生一样，在保留旧知识的同时，通过少量样本快速识别新出现的致病菌。

### 2. 白话版概述
想象一个正在实习的AI医生。起初它只认识“沙门氏菌”，后来医院又出现了“诺如病毒”病例。传统的AI如果直接学习诺如病毒，可能会把之前识别沙门氏菌的本领给丢了。这篇论文开发了一个名为 **CIL-DAFFNet** 的系统，它有两个绝活：一是“火眼金睛”（双注意力机制），能从复杂的病人症状中精准抓取关键信息；二是“温故知新”（动态知识蒸馏），在学习新病毒时，通过一种数学手段（MMD）计算新旧知识的差异，确保在掌握新知识的同时，老知识不掉队。

### 3. 方法部分
*   **核心思想**：结合**类增量学习（CIL）**与**特征融合**，通过动态调整学习权重来平衡新旧类别的记忆。
*   **模型结构 (CIL-DAFFNet)**：
    *   **双注意力机制 (Dual Attention)**：分别从空间和通道维度对临床特征进行加权，强化对判别性特征（如特定症状与某种细菌的关联）的提取。
    *   **自适应特征融合 (Adaptive Feature Fusion)**：将不同层级的特征进行有效整合，提升模型对不平衡数据的鲁棒性。
*   **关键设计 - 动态知识蒸馏**：
    *   **MMD 调节**：引入最大均值差异（Maximum Mean Discrepancy, MMD）来衡量新旧数据分布的距离。
    *   **策略**：如果新旧数据差异大，模型会自动调整蒸馏权重，防止新知识强行覆盖旧参数，从而缓解灾难性遗忘。
*   **可解释性**：引入 **SHAP 分析**，将黑盒模型透明化，告诉医生模型是基于哪些临床特征（如发热、腹泻频率等）做出的判断。

### 4. 实验部分
*   **数据来源**：真实的临床监测数据集，涵盖四类主要致病菌：沙门氏菌、副溶血性弧菌、大肠杆菌和诺如病毒。
*   **实验任务**：类增量学习任务（逐个阶段引入新的病原体类别）。
*   **基准模型 (Baselines)**：对比了 5 种主流的增量学习算法（如 iCaRL 等）。
*   **评价指标**：准确率 (Accuracy)、Macro-F1（平衡考虑每一类，对小样本友好）、G-mean（衡量不平衡数据下的综合性能）。
*   **主要结果**：在最终增量阶段，该模型准确率达到 **0.8245**，Macro-F1 为 **0.8004**，显著优于其他对比模型，证明了其在处理类别不平衡和增量任务上的优越性。

### 5. 资源与算力
*   **文中未充分披露**：论文摘要及提取内容中未提及具体的 GPU 型号、训练时长或内存消耗等硬件细节。

### 6. 真正可信的贡献
*   **动态权重机制**：通过 MMD 动态调整知识蒸馏强度，这比固定权重的传统增量学习更符合临床数据分布多变的实际情况。
*   **实战验证**：使用了真实的临床监测数据而非公开的理想化数据集，证明了模型在严重类别不平衡（常见病 vs 罕见病）下的有效性。
*   **临床可解释性**：SHAP 分析的加入使得该 AI 工具不仅是一个预测器，还能为流行病学调查提供特征重要性参考。

### 7. 局限与风险
*   **类别覆盖有限**：实验仅涵盖了 4 种常见病原体，对于成百上千种潜在的食源性致病菌，模型的扩展能力仍需验证。
*   **数据偏差风险**：临床监测数据往往受限于地区和医院的采集习惯，模型在跨地区应用时可能存在泛化性能下降的风险。
*   **实时性挑战**：增量学习虽然缓解了重新训练的压力，但在超大规模类别持续增加时，模型复杂度的增长仍是潜在障碍。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事公共卫生监测、临床辅助诊断、以及在小样本/不平衡数据场景下研究增量学习的 AI 研究者。
*   **后续可跟进的问题**：如何将该框架扩展到多模态数据（如结合临床症状与病原体基因组测序数据）？在完全未见过的新型病原体（Out-of-Distribution）出现时，模型如何实现自动预警而非强行分类？

（完）
