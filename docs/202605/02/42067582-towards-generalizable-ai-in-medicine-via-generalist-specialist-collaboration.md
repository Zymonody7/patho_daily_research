---
title: Towards generalizable AI in medicine via Generalist-Specialist Collaboration.
title_zh: 通过通用型-专家型协作实现医学领域的可泛化人工智能
authors: "Sunan He, Yuxiang Nie, Hongmei Wang, Shu Yang, Yihui Wang, Zhiyuan Cai, Zhixuan Chen, Yingxue Xu, Linshan Wu, Ngai Shing Cheng, Luyang Luo, Huiling Xiang, Xi Lin, Mingxiang Wu, Yifan Peng, George Shih, Ziyang Xu, Xian Wu, Qiong Wang, Ronald Cheong Kin Chan, Varut Vardhanabhuti, Xiaohui Duan, Winnie Chiu Wing Chu, Yefeng Zheng, Pranav Rajpurkar, Kang Zhang, Hao Chen"
date: 2026-05-01
pdf: "https://pubmed.ncbi.nlm.nih.gov/42067582/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 用于医学和诊断预测的通用基础模型
tldr: 针对医疗 AI 中通用大模型泛化性强但精度不足、专用模型精度高但适用范围窄的问题，提出 GSCo 协作框架。该框架通过轻量化专用模型为通用模型 MedDr 提供诊断预测和相似病例等上下文引导，实现协同决策。在 32 个医疗数据集上的实验表明，该方法在图像诊断和报告生成任务中超越了现有 SOTA 模型，为临床部署提供了高效且可扩展的方案。
selection_source: fresh_fetch
motivation: 旨在解决医疗领域通用大模型缺乏领域深度、而专用模型难以应对多样化临床场景的矛盾。
method: 构建了 GSCo 框架，利用轻量化专用模型提取专家级特征作为上下文，辅助开源通用模型 MedDr 进行最终诊断。
result: 在涵盖多种医学模态的 32 个数据集上，MedDr 及其协作模式在诊断准确率和报告生成质量上均优于现有主流模型。
conclusion: 这种通用与专用模型协同的范式，在保证诊断精度的同时提升了系统的泛化能力，是医疗 AI 落地临床的有效路径。
---

## 摘要
通用型基础模型（GFMs）因其在多样化任务中的卓越能力和灵活性而闻名。在医学领域，虽然 GFMs 表现出优越的泛化能力，但专家型模型因其领域特定知识而在精度上更胜一筹。在此，我们展示了一个名为“通用型-专家型协作”（GSCo）的协作框架，该框架协同结合了强大的通用型模型与轻量级专家型模型。在该框架中，专家型模型提供专家指导（如诊断预测和视觉相似的临床病例）作为上下文信息给通用型模型，随后由后者做出最终诊断。我们开发了 MedDr，一个专为医学定制的开源 GFM，以及一套为特定下游任务打造的轻量级专家型模型。对跨越多种医学模态的 32 个数据集进行的全面评估表明，MedDr 在下游数据集上的表现优于最先进的 GFMs。此外，GSCo 在医学图像诊断和报告生成方面超越了 GFMs 和专家型模型。这种方法为在临床环境中部署 GFMs 提供了一种有效且计算高效的范式，增强了可扩展性，并能在广泛的场景中实现精确分析。

## Abstract
Generalist foundation models (GFMs) are renowned for their exceptional capability and flexibility in diverse tasks. In the field of medicine, while GFMs exhibit superior generalizability, specialist models excel in precision because of their domain-specific knowledge. Here we show a cooperative framework, Generalist-Specialist Collaboration (GSCo), that synergistically combines a powerful generalist model with lightweight specialists. In this framework, specialists provide expert guidance, such as diagnostic predictions and visually similar clinical cases, as contextual information to the generalist, which then makes a final diagnosis. We developed MedDr, an open-source GFM tailored for medicine, as well as a suite of lightweight specialist models crafted for specific downstream tasks. A comprehensive evaluation on 32 datasets across diverse medical modalities shows that MedDr outperforms state-of-the-art GFMs on downstream datasets. Furthermore, GSCo exceeds GFMs and specialists in medical image diagnosis and report generation. This approach offers an effective and computationally efficient paradigm for deploying GFMs in clinical settings, enhancing scalability and enabling precise analysis across a wide range of scenarios.

---

## 论文详细总结（自动生成）

这篇论文由香港科技大学、哈佛医学院等机构的研究团队发表于 *Nature Biomedical Engineering*。它提出了一种名为 **GSCo** 的协作框架，旨在解决医疗人工智能在“通用性”与“专业性”之间的长期矛盾。

### 1. 解决的问题与核心价值
在医疗 AI 领域，目前存在两难境地：
*   **通用大模型（GFMs）**：像 GPT-4 这样，什么都能聊，泛化能力强，但面对具体的医疗诊断（如识别某种罕见病理切片）时，精度往往不如深耕单一领域的“小模型”。
*   **专家型模型（Specialists）**：在特定任务（如只看胸部 X 光）上极准，但换个任务（如看眼底图）就完全废了，且缺乏解释能力。

**核心价值**：这篇论文提出了一种“1+N”模式，让一个强大的通用大模型（MedDr）带一群轻量级的专家模型工作。这种协作既保留了大模型的逻辑推理和报告撰写能力，又引入了专家模型的精准诊断，是医疗 AI 走向临床落地的可行路径。

### 2. 白话版概述
想象一个医院诊室：**MedDr** 是一个资历深厚、博学但偶尔在细节上不够敏锐的主任医师（通用大模型）；而**专家模型**则是手下的一群技术员，每人只精通一种检查（如 CT、超声或病理）。
当病人来检查时，技术员先看图，给出初步结论并翻出几个类似的过往病例，然后把这些信息汇总给主任。主任结合这些“专家意见”和“参考病例”，最终写出准确的诊断报告。这种“强强联手”的效果比任何一方单独工作都要好。

### 3. 方法部分：GSCo 框架
*   **核心思想**：**专家引导的上下文学习（Expert-Guided In-Context Learning）**。不让大模型直接“裸看”医疗图像，而是让专家模型先为其“划重点”。
*   **模型结构**：
    *   **MedDr (Generalist)**：研究者开发的一个专门针对医学优化的开源多模态大模型。
    *   **Lightweight Specialists (Specialists)**：针对不同任务（如皮肤病识别、骨折检测）训练的小型模型（通常是轻量级的视觉网络）。
*   **推理流程**：
    1.  **专家预判**：专家模型对输入的医疗图像进行处理，输出预测类别（如“肺炎概率 90%”）。
    2.  **病例检索**：专家模型在数据库中寻找视觉特征最相似的几个历史病例（包含图像和医生结论）。
    3.  **提示词组装**：将“原始图像 + 专家预判 + 相似病例”打包成一段信息（Context）。
    4.  **最终决策**：MedDr 接收这些信息，进行逻辑整合，输出最终诊断或生成详细的医疗报告。
*   **关键设计取舍**：专家模型保持“轻量化”，这样在部署时不会占用过多算力，同时通过提供“相似病例”解决了大模型容易“幻觉”（瞎编）的问题。

### 4. 实验部分
*   **数据规模**：极其广泛，涵盖了 **32 个数据集**，涉及放射影像（CT/MRI/X-ray）、病理切片、超声、内窥镜、皮肤镜等多种**模态**（即不同的医学检查手段）。
*   **任务**：医疗图像诊断（分类）和医疗报告生成。
*   **Baseline（对比对象）**：包括目前最顶尖的通用基础模型（如 GPT-4V 等 SOTA 模型）以及各领域的专用 SOTA 模型。
*   **评价指标**：诊断准确率（Accuracy）、F1 分数，以及报告生成的语言质量指标（如 BLEU、ROUGE）。
*   **主要结果**：
    *   MedDr 单体表现就已优于许多现有的通用医疗模型。
    *   **GSCo 协作模式**在几乎所有任务上都超过了“单打独斗”的大模型或专家模型，尤其在处理复杂、跨模态任务时优势明显。

### 5. 资源与算力
*   **文中未充分披露**：摘要和提取文本中未详细列出具体的 GPU 型号、训练时长或总算力消耗。但考虑到其处理了 32 个数据集并开发了 MedDr 模型，其训练成本显然属于“工业级”或“顶尖实验室级”。

### 6. 真正可信的贡献
*   **MedDr 开源模型**：为医学界提供了一个高性能的开源底座。
*   **协作范式的验证**：通过 32 个数据集的“暴力测试”，有力证明了“通用模型 + 专家引导”比单纯堆大模型参数更有效。
*   **检索增强诊断**：证明了引入“相似病例”能显著提升 AI 诊断的可信度和准确度。

### 7. 局限与风险
*   **专家模型的依赖性**：如果专家模型在第一步就给出了严重错误的引导，MedDr 是否会被带偏？（即“先入为主”的风险）。
*   **部署复杂性**：在临床实际环境中，维护几十个专家模型加一个大模型的系统，对医院的 IT 架构和运维提出了很高要求。
*   **数据偏差**：虽然用了 32 个数据集，但医疗数据存在地域和设备差异，模型在未见过的医院环境下的表现（外推性）仍需验证。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事多模态医疗影像分析、临床决策支持系统（CDSS）开发、以及关注大模型落地医疗场景的研究者。
*   **后续可跟进的问题**：能否将这种协作模式扩展到“组学数据”（如基因表达谱）？例如，用一个专门分析基因突变的专家模型来引导大模型解读复杂的临床表型。

（完）
