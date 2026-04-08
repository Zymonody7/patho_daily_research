---
title: "Publicly available multimodal large language models for ocular surface infections: benchmarking against corneal specialists in triage, diagnosis and treatment."
title_zh: 公开可用的多模态大语言模型在眼表感染中的应用：在分诊、诊断和治疗方面与角膜病专家的基准对比
authors: "Carlos Campo-Beamud, Antonio Adan Ruiz, Jesús Bastante Quijano, Esther Campo Beamud, Francisco Javier Gómez-Romero, Alfredo Julian Fernández Ruíz, Sergio Copete"
date: 2026-04-07
pdf: "https://pubmed.ncbi.nlm.nih.gov/41946559/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 多模态大语言模型用于感染诊断和分诊
tldr: 针对眼表感染诊断依赖微生物检测且效率较低的现状，本研究对比了GPT-4o、GPT-5等六款多模态大模型与角膜病专家在感染性角膜炎和结膜炎诊断、治疗及分诊中的表现。通过60例确诊病例测试发现，模型在“图像+文本”双重输入下表现最佳，Perplexity和GPT-5的诊断准确率接近人类专家，但在治疗方案制定和罕见病原体识别上仍存在短板。该研究验证了多模态LLM作为眼科辅助诊断工具在资源受限地区的临床潜力。
selection_source: fresh_fetch
motivation: 旨在评估现有多模态大模型在眼表感染这一依赖专业经验的领域中，能否通过临床图像和病史提供准确的诊断、治疗建议及急诊分诊。
method: 采用单中心诊断准确性研究方法，对比六种主流多模态大模型在不同输入条件下对60例微生物确诊病例的处理结果，并与两位角膜病专家进行基准测试。
result: "实验表明图文结合输入显著优于单一模态，其中Perplexity在诊断准确率上达到96.7%，但在治疗方案的精确度上仍普遍低于人类专家。"
conclusion: 多模态大模型在具备临床上下文时可达到接近专家的诊断水平，但在治疗推理和罕见病识别方面仍需进一步的针对性微调与验证。
---

## 摘要
背景/目的：眼表感染仍是全球视力丧失的主要原因，但诊断往往依赖于缓慢或灵敏度较低的微生物技术。人工智能可以通过支持快速分诊和诊断推理来补充新兴的分子工具。本研究针对感染性角膜炎和结膜炎的诊断、治疗和紧急分诊，将公开可用的多模态大语言模型（LLMs）与角膜病专家进行了基准对比。方法：一项单中心诊断准确性研究纳入了60例经微生物学证实的感染性角膜炎和结膜炎病例，每例均包含一张裂隙灯照片和一份配对的临床简述。在三种输入条件（仅图像、仅文本和图像+文本）下，评估了六种多模态大语言模型（GPT-4o、GPT-5、Gemini、Claude、Perplexity 和 Grok）在诊断、治疗和紧急分诊方面的表现。输出结果与两名角膜病专家进行了比较。结果：LLM 的表现强烈依赖于输入模式。仅图像的准确率最低（表现最好的是 GPT-5，为 61.4%；κ=0.38），经常误诊真菌性和棘阿米巴角膜炎，且幻觉现象仅限于此设置。文本输入提高了结果（GPT-5 为 83.3%；κ=0.78），但准确率仍低于专家（87-90%；κ≈0.8）。图像+文本结合达到了接近人类的准确率，但并未持续超越角膜病专家（Perplexity 为 96.7%，κ=0.95；GPT-5 为 91.7%，κ=0.87）。治疗准确率仍然较低（81-85% 对比 90-98%），而紧急分诊在多模态输入下与专家相当。结论：在提供临床背景和裂隙灯图像的情况下，公开可用的多模态 LLM 在诊断和分诊方面可以达到专家级水平。治疗推理和罕见病原体识别方面的差距强调了进行针对性改进和验证的必要性。这些模型可以补充专家护理，支持快速分诊并与分子或宏基因组诊断相结合，特别是在资源有限的地区。

## Abstract
BACKGROUND/AIMS: Ocular surface infections remain a major cause of visual loss worldwide, yet diagnosis often relies on slow or insensitive microbiological techniques. Artificial intelligence may complement emerging molecular tools by supporting rapid triage and diagnostic reasoning. This study benchmarked publicly available multimodal large language models (LLMs) against corneal specialists for the diagnosis, treatment and urgency triage of infectious keratitis and conjunctivitis. METHODS: A single-centre diagnostic-accuracy study included 60 microbiologically confirmed infectious keratitis and conjunctivitis cases, each comprising a slit-lamp photograph and a paired clinical vignette. Six multimodal LLMs (GPT-4o, GPT-5, Gemini, Claude, Perplexity and Grok) were evaluated for diagnosis, treatment and urgency triage under three input conditions (image-only, text-only and image+text). Outputs were compared with two corneal specialists. RESULTS: LLM performance depended strongly on input modality. Image-only accuracy was lowest (best GPT-5, 61.4%; κ=0.38) with frequent misclassification of fungal and Acanthamoeba keratitis and hallucinations confined to this setting. Text input improved results (GPT-5, 83.3%; κ=0.78), though accuracy remained below specialists (87-90%; κ≈0.8). Combined image+text achieved near-human accuracy without consistently surpassing corneal specialists (Perplexity 96.7%; κ=0.95; GPT-5 91.7%; κ=0.87). Treatment accuracy remained lower (81-85% vs 90-98%), while urgency triage matched experts in multimodal input. CONCLUSION: Publicly accessible multimodal LLMs can approach expert-level performance in diagnosis and triage when provided with clinical context and slit-lamp images. Gaps in therapeutic reasoning and rare pathogen recognition underscore the need for targeted refinement and validation. These models may complement specialist care, supporting rapid triage and integration with molecular or metagenomic diagnostics, especially in resource-limited settings.

---

## 论文详细总结（自动生成）

这篇论文评估了当前最顶尖的多模态大模型（MLLM）在眼科临床诊断中的实际表现，以下是详细总结：

### 1. 解决的问题与研究价值
**核心问题**：眼表感染（如角膜炎、结膜炎）是全球致盲的主要原因。传统的诊断依赖于微生物培养（耗时长、灵敏度低）或专家经验。在医疗资源匮乏地区，缺乏角膜病专家会导致治疗延误。
**研究价值**：本文探讨了通用大模型（而非专门训练的医疗模型）能否通过“看”裂隙灯照片（眼科常用显微镜照片）并“读”病历，达到人类专家的诊断和分诊水平。这为 AI 辅助基层医疗和快速分诊提供了实证依据。

### 2. 白话版概述
眼科医生诊断眼疾通常是“一看照片，二问病史”。这项研究找来 60 个确诊的真实病例，把照片和病历分别或组合喂给 GPT-4o、GPT-5、Claude 等 6 个大模型，看它们能不能猜对是什么病、该怎么治、急不急诊。结果发现，只给照片时模型经常“瞎猜”；但如果图文并茂，最强的模型（如 Perplexity 和 GPT-5）在诊断准确率上已经非常接近资深专家，但在开药方（治疗方案）上还是不如人类严谨。

### 3. 方法部分
*   **核心思想**：对比不同输入模态（仅图像、仅文本、图文结合）对模型推理能力的影响。
*   **模型选择**：选取了 6 款主流多模态模型：GPT-4o、GPT-5（注：文中提及，可能为特定版本或预览版）、Gemini、Claude、Perplexity 和 Grok。
*   **推理流程**：
    1.  **仅图像（Image-only）**：只提供裂隙灯照片。
    2.  **仅文本（Text-only）**：只提供临床简述（如患者症状、病程）。
    3.  **多模态（Image+Text）**：同时提供照片和文本。
*   **关键设计**：采用“微生物学证实”的病例作为金标准（Ground Truth），确保了评估基准的绝对客观，避免了人类专家主观判断可能存在的误差。

### 4. 实验部分
*   **数据**：60 例经实验室微生物检测确诊的病例（涵盖细菌、真菌、病毒、棘阿米巴原虫等感染）。
*   **任务**：诊断（是什么病）、治疗建议（开什么药）、分诊（是否需要紧急处理）。
*   **Baseline**：两位资深角膜病专家的判断结果。
*   **评价指标**：准确率（Accuracy）、Kappa 系数（一致性检验）。
*   **主要结果**：
    *   **模态对比**：图文结合 > 仅文本 > 仅图像。仅靠图像时，模型表现糟糕（最高仅 61.4%），且容易出现幻觉。
    *   **模型排名**：Perplexity 在图文结合下表现最强，诊断准确率达 **96.7%**（κ=0.95），GPT-5 紧随其后（91.7%）。
    *   **分诊表现**：在多模态输入下，顶尖模型的分诊准确度与专家相当。
    *   **治疗表现**：所有模型在治疗方案的精确性上均显著低于专家（模型 81-85% vs 专家 90-98%）。

### 5. 资源与算力
*   **文中未充分披露**。研究使用的是公开可用的商业模型 API 或网页端，未涉及模型训练过程，因此未提及具体的计算集群或 GPU 耗时。

### 6. 真正可信的贡献
*   **多模态协同效应的量化**：有力证明了临床背景信息（文本）是多模态模型在医疗领域发挥作用的“压舱石”，单纯的图像识别在复杂感染诊断中不可靠。
*   **基准对标**：通过与微生物金标准和人类专家双重对比，界定了通用大模型在眼科细分领域的“能力边界”——诊断和分诊已达专家级，但治疗决策仍需人类把关。

### 7. 局限与风险
*   **样本量较小**：仅 60 例病例，可能无法覆盖所有罕见感染类型。
*   **幻觉风险**：在“仅图像”模式下，模型会编造不存在的临床特征。
*   **罕见病识别**：模型对真菌性和棘阿米巴角膜炎（较少见且严重的感染）的识别能力仍弱于专家，这在临床上可能导致致盲性后果。
*   **黑盒性质**：模型给出诊断的逻辑链条（Reasoning）是否符合医学病理生理学，文中未做深度定性分析。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事多模态医疗影像分析、临床决策支持系统（CDSS）开发、以及关注 LLM 在垂直领域落地的研究者。
*   **后续可跟进的问题**：如何通过检索增强生成（RAG）引入最新的临床指南，以修复模型在“治疗方案制定”上的短板？如何针对罕见病原体进行小样本微调以提升识别率？

（完）
