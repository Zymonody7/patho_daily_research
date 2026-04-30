---
title: An agentic framework for autonomous scientific discovery in cancer pathology.
title_zh: 癌症病理学中自主科学发现的智能体框架
authors: "Florian Trost, Bide Zhang, Ines Aring, Marcus Bauer, Lennert Glamann, Michael Wessolly, Kyra Johnson, Heike Göbel, Tristan Lerbs, Taban Sangenne, Peter Herrmann, Fabian Mairinger, Christopher Kopp, Sebastian Michels, Anna Rasokat, Matthias Heldwein, Steffen Wagner, Birgid Schömig-Markiefka, Jürgen Wolf, Sylvia Hartmann, Claudia Wickenhauser, Andrey Bychkov, Jens Peter Klussmann, Alexander Quaas, Reinhard Buettner, Yuri Tolkach"
date: 2026-04-29
pdf: "https://pubmed.ncbi.nlm.nih.gov/42056496/"
tags: ["query:agent"]
score: 9.0
evidence: 自主科学发现的智能体 AI 框架
tldr: 针对癌症病理分析中特征工程繁琐、可解释性差及工作流碎片化的问题，本研究开发了SPARK智能体框架。该框架以语言为通用接口，能自主将生物学假设转化为分析工具，直接处理复杂病理数据而无需额外训练。在涉及5种癌症、5400余名患者的大规模验证中，SPARK成功提取了与预后和生物标志物相关的临床特征，为自动化科学发现和精准诊断提供了新范式。
selection_source: fresh_fetch
motivation: 现有的病理AI系统过度依赖人工设计特征且缺乏透明度，难以灵活应对复杂的生物学研究需求。
method: 构建了一个名为SPARK的智能体系统，利用大语言模型作为核心，将自然语言描述的生物学概念自动转化为可执行的图像分析流程。
result: 在18个患者队列的测试中，SPARK自主生成的概念在预测癌症预后、识别生物标志物及揭示肿瘤演化模式方面表现出显著的临床相关性。
conclusion: 该研究证明了基于智能体的AI能够自主进行病理学发现，通过语言驱动的交互降低了复杂生物医学分析的门槛。
---

## 摘要
人工智能已经推动了癌症病理学的发展，但许多系统仍依赖于手工设计的特征，难以解释，且依赖于碎片化的工作流程。我们介绍了 SPARK（System of Pathology Agents for Research and Knowledge，病理研究与知识智能体系统），这是一种基础性的智能体人工智能方法，它使用语言作为通用接口，自主生成用于肿瘤分析的生物驱动概念。SPARK 将生物学思想转化为分析工具，并直接处理复杂的病理数据，无需额外的模型训练。我们在涵盖五种癌症类型（肺腺癌、肺鳞状细胞癌、结直肠癌、乳腺癌和口咽鳞状细胞癌）的 18 个患者队列中评估了 SPARK，涉及 5,400 多名具有组织病理学图像和临床/随访信息的患者，涵盖了预后和预测场景，以及一个特征明确的空间生物学乳腺癌数据集（患者人数 n = 625）。我们发现 SPARK 产生了与预后、已知病理变量和预测性生物标志物相关的临床和生物学相关概念，包括从静态图像中推断出的肿瘤进展模式和时间变化。一个专用模块允许人类与 SPARK 进行交互。需要进一步的前瞻性验证来评估 SPARK 创建的工具的临床效用。所有代码、参数和结果均已公开，以帮助研究人员和临床医生提高诊断精度并深化对肿瘤生物学的见解。

## Abstract
Artificial intelligence has advanced cancer pathology, but many systems still depend on hand-crafted features, are hard to explain and rely on fragmented workflows. We introduce SPARK (System of Pathology Agents for Research and Knowledge), a foundational agentic artificial intelligence approach that uses language as a universal interface to autonomously generate biologically driven concepts for tumor analysis. SPARK turns biological ideas into analytical tools and works directly with complex pathology data without extra model training. We evaluated SPARK across 18 patient cohorts spanning five cancer types (lung adenocarcinoma, lung squamous cell carcinoma, colorectal cancer, breast cancer and oropharyngeal squamous cell carcinoma) and more than 5,400 patients with available histopathology images and clinical/follow-up information, in both prognostic and predictive settings and on a well characterized spatial biology breast cancer dataset (patient n = 625). We found that SPARK produced clinically and biologically relevant concepts correlated with prognosis, known pathological variables and predictive biomarkers, including patterns of tumor progression and temporal change inferred from static images. A dedicated module allows for human interaction with SPARK. Further prospective validation is needed to evaluate the clinical utility of the tools created by SPARK. All code, parameters and results are openly released to help researchers and clinicians improve diagnostic precision and deepen tumor biology insights.

---

## 论文详细总结（自动生成）

这是一份关于论文《An agentic framework for autonomous scientific discovery in cancer pathology》（癌症病理学中自主科学发现的智能体框架）的深度解析：

### 1. 解决的问题与研究价值
*   **核心问题**：目前的 AI 辅助病理诊断（看肿瘤切片）存在三个痛点：
    1.  **黑盒化**：模型能给出预测，但说不清为什么。
    2.  **特征工程繁琐**：需要专家手动定义“要看哪些细胞”，效率低且可能遗漏未知的生物学规律。
    3.  **工作流碎片化**：不同的任务需要训练不同的模型，缺乏通用性。
*   **研究价值**：该研究提出了 **SPARK** 框架，将 AI 从“只会做选择题的工具”提升为“能自主提出假设并验证的智能体（Agent）”。它让研究者能用自然语言直接与复杂的病理图像数据对话，实现了从数据到生物学发现的自动化。

### 2. 白话版概述
想象你有一个极其博学的数字病理学家助手。你只需要对它说：“帮我研究一下肺癌细胞周围的免疫细胞是如何分布的，以及这是否影响患者寿命。”
这个助手（SPARK）会自动理解你的意图，调用现有的图像识别工具去切片中寻找细胞，编写代码进行统计分析，最后告诉你：“我发现当免疫细胞在肿瘤边缘呈‘围栏状’分布时，患者预后更好。”
它不需要针对每个新问题重新训练，而是通过“语言”这个通用接口，把生物学直觉直接转化为分析算法。

### 3. 方法部分：核心思想与设计
*   **核心思想**：**以语言为中心的智能体架构**。利用大语言模型（LLM）作为“大脑”，将高层的生物学概念拆解为可执行的底层机器视觉任务。
*   **模型结构**：
    *   **大脑（LLM）**：负责逻辑推理、任务规划和代码生成。
    *   **工具库（Tools）**：包含预训练的病理基础模型（Foundation Models），用于识别细胞、组织分割等。
    *   **执行模块**：自动运行生成的代码，处理大规模的 WSI（全扫描切片图像）。
*   **推理流程**：
    1.  **概念定义**：用户输入或系统自主生成一个生物学假设（如“肿瘤出芽”现象）。
    2.  **工具编排**：智能体决定调用哪些视觉模型来识别相关结构。
    3.  **量化分析**：自动计算空间分布、密度等指标。
    4.  **临床关联**：将提取的特征与患者的生存期、药物反应等临床数据进行统计关联。
*   **关键取舍**：放弃了“端到端”的黑盒训练，选择了**“模块化工具+语言中介”**。这样做虽然增加了系统复杂度，但获得了极高的可解释性和灵活性。

### 4. 实验部分
*   **数据规模**：涵盖 5 种主要癌症（肺腺癌、肺鳞癌、结直肠癌、乳腺癌、口咽癌），涉及 18 个独立患者队列，总计超过 **5,400 名患者**。
*   **任务类型**：
    *   **预后分析**：预测患者的生存时间。
    *   **生物标志物预测**：识别与特定基因突变或药物反应相关的图像特征。
    *   **空间生物学**：分析细胞在空间上的相互作用。
*   **主要结果**：
    *   SPARK 自主生成的特征在多个队列中表现出与人类专家定义特征相当、甚至更强的预测能力。
    *   它能从静态图像中推断出肿瘤演化的“伪时间”序列，揭示肿瘤进展的动态模式。
    *   在空间转录组数据验证中，SPARK 提取的形态学特征与基因表达高度一致。

### 5. 资源与算力
*   **文中未充分披露**具体的 GPU 小时数。但考虑到其使用了现成的病理基础模型（Foundation Models）且**无需额外训练（Zero-shot/Inference-only）**，其核心算力消耗主要集中在 LLM 的推理和大规模图像的特征提取上，而非传统的深度学习模型训练。

### 6. 真正可信的贡献
1.  **自主性**：证明了 AI 智能体可以自主发现具有临床意义的病理特征，而不仅仅是验证已知特征。
2.  **可解释性**：所有的发现都以自然语言和明确的几何/空间指标呈现，病理医生可以轻松理解并核实。
3.  **跨癌种通用性**：一套框架在 5 种癌症上均验证有效，展示了极强的泛化能力。

### 7. 局限与风险
*   **幻觉风险**：底层 LLM 可能会生成错误的生物学解释或逻辑错误的分析代码（虽然文中提到有验证模块）。
*   **前瞻性验证缺失**：目前所有实验均基于回顾性数据（历史病例），在真实临床诊疗流程中的表现仍需验证。
*   **依赖基础模型**：SPARK 的上限取决于底层视觉基础模型的识别精度，如果基础模型漏掉了某种微小结构，智能体也无法发现相关规律。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事计算病理学、多模态大模型应用、以及希望利用 AI 发现新生物标志物的研究者。
*   **后续可跟进的问题**：如何构建一个能够实时纠正 LLM 逻辑错误的“生物学知识护栏”？如何将蛋白质组学、基因组学等多组学数据整合进这种智能体对话框架中？

（完）
