---
title: "SAVLT: Structure-Aware Vision-Language Tuning for Multi-Center Cervical OCT Diagnosis."
title_zh: SAVLT：用于多中心宫颈 OCT 诊断的结构感知视觉语言微调
authors: "Mi Yin, Yuchen Pei, Yixiong Zou, Yan Zhang, Yutao Ma"
date: 2026-04-27
pdf: "https://pubmed.ncbi.nlm.nih.gov/42044002/"
tags: ["query:bioinfo"]
score: 6.0
evidence: 用于医学诊断的视觉语言微调
tldr: 针对宫颈OCT影像诊断中伪影干扰病理特征识别的问题，提出SAVLT框架。该框架通过引入区域感知空间注意力（RaSA）模块，强制模型关注组织内部结构并过滤非生物噪声，同时结合双约束目标函数提升多中心场景下的鲁棒性。实验证明，该方法在少样本情况下具有极强的泛化能力和临床可解释性，为异构OCT影像的自动化诊断提供了可靠方案。
selection_source: fresh_fetch
motivation: 宫颈OCT影像中的伪影常被误认为生物结构，导致视觉语言模型在诊断时难以准确捕捉关键的病理层退化特征。
method: 提出SAVLT框架，利用区域感知空间注意力模块净化视觉表示，并结合可学习的视觉原型与文本对齐任务来稳定多中心环境下的优化过程。
result: 在多中心队列和两个外部数据集上的验证显示，该方法实现了稳健的少样本泛化性能，并提供了符合临床逻辑的诊断解释。
conclusion: SAVLT通过结构感知微调有效解决了OCT影像中的噪声干扰与域偏移问题，是医疗大模型在复杂临床场景落地的有效尝试。
---

## 摘要
宫颈光学相干断层扫描（OCT）能够实现组织微米级的可视化，但在有限监督下实现可靠诊断仍具挑战性。虽然视觉语言模型（VLMs）通过利用一致的临床语义提供了一种解决方案，但其适配过程受到伪装成生物结构的混淆伪影的阻碍。这种现象劫持了全局注意力，掩盖了对诊断至关重要的病理性分层退化。为了克服这一局限性，我们提出了 SAVLT，这是一种通过参数高效微调来适配 VLM 的结构感知微调框架。为了从全局匹配转向解剖学定位，SAVLT 引入了区域感知空间注意力（RaSA）模块以实施空间约束。RaSA 从非生物噪声中纯化视觉表征，恢复模型对组织内结构完整性的关注。此外，双重约束目标将图文对齐与可学习的视觉原型相结合，以稳定针对多中心领域偏移和提示词变化的优化。通过多中心队列和两个外部测试数据集的验证，SAVLT 展现了鲁棒的小样本泛化能力和临床可解释性，为在异构 OCT 成像中部署基础模型建立了一个可靠的范式。源代码已在 https://github.com/rabbit-my/SAVLT 公开。

## Abstract
Cervical optical coherence tomography (OCT) enables micrometer-scale visualization of tissue, yet trustworthy diagnosis under limited supervision remains challenging. While vision-language models (VLMs) offer a solution by leveraging consistent clinical semantics, their adaptation is hindered by confounding artifacts that masquerade as biological structures. This phenomenon hijacks global attention, obscuring the pathological layer degradation that is crucial for diagnosis. To overcome this limitation, we propose SAVLT, a structure-aware tuning framework that adapts VLMs via parameter-efficient fine-tuning. To shift from global matching to anatomical grounding, SAVLT introduces a region-aware spatial attention (RaSA) module that enforces spatial constraints. RaSA purifies visual representations from non-biological noise, restoring the model's focus on intra-tissue structural integrity. Furthermore, a dual-constraint objective couples image-text alignment with learnable visual prototypes to stabilize optimization against multi-center domain shifts and prompt variations. Validated across a multi-center cohort and two external test datasets, SAVLT delivers robust few-shot generalization and clinical interpretability, establishing a reliable paradigm for deploying foundation models in heterogeneous OCT imaging. Source code is publicly available at https://github.com/rabbit-my/SAVLT.