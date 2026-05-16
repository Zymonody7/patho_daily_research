---
title: "From Label-Free Multiphoton Imaging to Pathological Reports: A Vision-Language Breast Cancer Margin Pathological Diagnosis System."
title_zh: 从无标记多光子成像到病理报告：一种视觉-语言乳腺癌切缘病理诊断系统
authors: "Shu Wang, Jingze Su, Xiahui Han, Deyong Kang, Xiao Zhang, Fei Xu, Changzu Liu, Junlin Pan, Xingfu Wang, Qiaohui Zhan, Aimin Wang, Feng Huang, Heping Cheng, Wenxi Liu, Ruolan Lin, Jianxin Chen"
date: 2026-05-15
pdf: "https://pubmed.ncbi.nlm.nih.gov/42136540/"
tags: ["query:bioinfo"]
score: 6.0
evidence: 用于病理诊断的视觉语言模型
tldr: "针对乳腺癌保乳手术中切缘病理评估依赖H&E染色且耗时的问题，本研究开发了MarginPath系统。该系统利用多光子显微镜（MPM）捕获无标记胶原特征，结合视觉语言模型，仅需单张切片即可生成虚拟H&E图像、切缘状态热图及自然语言诊断报告。在158例样本上的验证显示，其诊断性能优于现有病理大模型，有效降低了病理医生对新成像技术的学习门槛，辅助临床决策。"
selection_source: fresh_fetch
motivation: "传统的H&E染色病理分析在手术切缘评估中存在局限，而无标记多光子成像虽能提供关键的胶原特征，但病理医生对其图像特征缺乏识别经验。"
method: "提出MarginPath视觉语言模型，通过整合MPM图像中的肿瘤相关胶原特征与虚拟H&E转换技术，实现从无标记成像到多模态诊断报告的自动生成。"
result: 在158例浸润性乳腺癌标本上的实验表明，该系统在切缘诊断准确率上超过了现有的病理视觉语言模型，并支持交互式问答。
conclusion: 该系统通过将先进的无标记成像技术与自然语言处理相结合，为乳腺癌手术切缘的快速、精准评估提供了一种可解释的临床决策支持方案。
---

## 摘要
切缘病理评估为保乳手术提供关键反馈，而 H&E 染色组织病理学侧重于残留肿瘤，可能导致不必要的切除。无标记多光子显微镜 (MPM) 揭示了切缘处的肿瘤相关胶原特征 (TACS)，提供了具有预后相关性的诊断信息。然而，病理学家对新型 MPM 图像的熟悉程度有限，阻碍了其整合进诊断工作流。在此，我们介绍了 MarginPath，这是一个基于 MPM-语言模型的切缘病理诊断系统，仅需单张无标记切片。通过将 MPM 衍生的 TACS 与虚拟 H&E 诊断信息相结合，MarginPath 提供多模态诊断报告，包括：(i) MPM 图像及对应的虚拟 H&E 图像，(ii) 基于 TACS 的像素级切缘状态热图，以及 (iii) 肿瘤切缘微环境的详细自然语言诊断描述。在 158 例浸润性乳腺癌标本上进行的验证表明，MarginPath 在切缘诊断方面优于现有的病理视觉-语言模型，并可扩展为问答系统，从而增强临床决策支持和医患沟通。

## Abstract
Margin pathological assessment provides critical feedback for breast-conserving surgery, whereas H&E-stained histopathology focuses on residual tumor and may cause unnecessary resections. Label-free multiphoton microscopy (MPM) reveals tumor-associated collagen signatures (TACS) at the margin, offering a prognostically relevant diagnostic information. However, limited familiarity of novel MPM images by pathologists has prevented its integration into diagnostic workflows. Here, we introduce MarginPath, a Margin Pathological diagnosis system built on an MPM-language model that requires only a single label-free section. By integrating MPM-derived TACS with virtual H&E diagnostic information, MarginPath provides a multimodal diagnostic report, including: (i) a MPM image and corresponding virtual H&E image, (ii) a TACS-based pixel-level margin-status heatmap, and (iii) detailed natural-language diagnostic descriptions of tumor margin microenvironment. Validated on 158 invasive breast cancer specimens, MarginPath outperforms existing pathology vision-language models in margin diagnosis and can be extended into a question-answering system, enhancing both clinical decision-support and patient communication.