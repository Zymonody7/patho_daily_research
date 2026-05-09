---
title: Cell-free DNA size deconvolution resolves nucleosomal origins and reveals tumor-associated fragmentomic alterations.
title_zh: 无细胞DNA尺寸解卷积解析核小体起源并揭示肿瘤相关的片段组学改变
authors: "Ze Zhou, Wendy N Cooper, Zhao Cheng, Sara Lightowlers, Charlotte E Coles, Amit Roshan, Nitzan Rosenfeld, Hui Zhao"
date: 2026-05-08
pdf: "https://pubmed.ncbi.nlm.nih.gov/42103785/"
tags: ["query:seqai"]
score: 6.0
evidence: 用于诊断的游离DNA片段长度分布通用模型
tldr: 针对循环游离DNA（cfDNA）片段化机制不明的问题，本研究开发了一种通用的片段长度分布反卷积模型，将多种体液中的cfDNA分布分解为约10bp周期的柯西-洛伦兹分量。通过分析159bp等关键组分，研究成功区分了肿瘤来源DNA与吞噬作用导致的片段缩短，并利用片段化熵显著提升了癌症检测的灵敏度，为液体活检提供了更精准的生物物理模型。
selection_source: fresh_fetch
motivation: 旨在阐明cfDNA片段长度分布背后的生物学机制，以区分肿瘤特异性改变与其他生理过程（如吞噬作用）导致的片段化差异。
method: 提出一种基于柯西-洛伦兹分布的数学模型，将血浆、尿液等多种体液中的cfDNA长度谱分解为具有10bp周期性的多个核小体相关分量。
result: 发现159bp组分是区分核小体内外切割的关键，并证明肿瘤DNA的缩短在分布参数上与吞噬作用引起的缩短存在显著差异。
conclusion: 通过反卷积模型提取的片段化熵特征能有效识别肿瘤相关的异常改变，显著增强了基于cfDNA的癌症早期筛查和诊断能力。
---

## 摘要
无细胞DNA（cfDNA）片段组学特征分析在微创癌症诊断中具有巨大潜力。尽管选择性分析血浆中的短cfDNA可以富集循环肿瘤DNA（ctDNA），但塑造cfDNA尺寸分布的机制仍未被完全理解。在本研究中，我们开发了一个跨多种体液（唾液、尿液、脑脊液、淋巴液和血浆）的cfDNA片段长度分布通用模型，将尺寸分布解卷积为约10-bp的周期性峰（组分），每个组分均由柯西-洛伦兹（Cauchy-Lorentz）分布近似。该分析框架能够研究不同病理状态下的cfDNA片段化，并揭示了一个159-bp的组分，该组分可能界定了核小体内和核小体间的cfDNA。通过分析携带生殖系TP53突变的个体、接受放射治疗的患者以及肝移植受者的血浆DNA，我们证明了通过核小体内和核小体间组分的幅度（amplitude）和尺度（scale）参数差异，可以将ctDNA缩短与吞噬作用相关的cfDNA缩短区分开来。此外，利用通过cfDNA尺寸解卷积识别出的以片段化熵增加为特征的肿瘤相关片段组学改变，显著增强了癌症检测能力。

## Abstract
Analysis of cell-free DNA (cfDNA) fragmentomic features holds great promise for minimally invasive cancer diagnostics. Although selectively analyzing short plasma cfDNA enriches tumor-derived DNA (ctDNA), the mechanisms shaping cfDNA size profiles remain incompletely understood. Here, we develop a generalized model of cfDNA fragment length distributions across multiple bodily fluids (saliva, urine, cerebrospinal fluid, lymphatic fluid, and plasma), deconvoluting size profiles into ~10-bp periodic peaks (components), each approximated by a Cauchy-Lorentz distribution. This analytical framework enables investigation of cfDNA fragmentation across diverse pathological states and reveals a 159-bp component that may demarcate intra- and inter-nucleosomal cfDNA. By analyzing plasma DNA from individuals harboring germline TP53 mutations, patients receiving radiotherapy, and liver transplantation recipients, we demonstrate that ctDNA shortening can be distinguished from phagocytosis-associated cfDNA shortening through differences in the amplitude and scale parameters of intra- and inter-nucleosomal components. Moreover, leveraging tumor-related fragmentomic alterations, characterized by increased fragmentation entropy identified through cfDNA size deconvolution, significantly enhances cancer detection.