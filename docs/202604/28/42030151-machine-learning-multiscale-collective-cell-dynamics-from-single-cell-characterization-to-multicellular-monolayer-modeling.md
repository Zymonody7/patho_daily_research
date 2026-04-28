---
title: "Machine learning multiscale collective cell dynamics: From single-cell characterization to multicellular monolayer modeling."
title_zh: 机器学习多尺度集体细胞动力学：从单细胞表征到多细胞单层建模
authors: "Kun Xu, Jianbo Bai, Hao-Shun Zhang, Cheng-Lin Lv, Yue Li, Yue Shao, Xi-Qiao Feng, Bo Li"
date: 2026-04-28
pdf: "https://pubmed.ncbi.nlm.nih.gov/42030151/"
tags: ["query:bioinfo"]
score: 6.0
evidence: 用于多细胞动力学和细胞状态转换的机器学习
tldr: 针对集体细胞动力学在跨尺度建模中面临的物理参数难测量及主动力机制不明等挑战，该研究提出了一种尺度自适应的混合机器学习框架。该框架在单细胞尺度利用物理引导的机器学习推断关键参数以表征形态与速度，在多细胞尺度则采用物理无关的机器学习直接预测密度波动等宏观行为。实验证明该方法能有效结合物理先验与数据驱动的优势，为理解胚胎发育及疾病演变等复杂生理过程提供了精准的跨尺度计算手段。
selection_source: fresh_fetch
motivation: 传统的物理模型因依赖难以测量的参数和不明确的主动物理机制，难以同时兼顾单细胞特征表征与多细胞涌现行为的预测。
method: 构建了一个混合框架，在单细胞尺度使用物理引导的机器学习推断参数，在多细胞尺度利用物理无关的机器学习从历史序列中学习宏观动态。
result: 该方法不仅实现了对单细胞形状和速度的高精度刻画，还成功预测了多细胞单层中实验观测到的长程密度振荡和波动现象。
conclusion: 这种将物理先验与纯数据驱动方法按尺度互补结合的策略，为多尺度集体细胞动力学研究提供了一种能够弥合理论与实验差距的通用计算范式。
---

## 摘要
集体细胞动力学是许多生理过程的基础，包括胚胎发育、组织形态发生、免疫反应和疾病进展。跨尺度准确模拟这些动力学仍然具有挑战性，因为传统的基于物理的模型通常依赖于许多不可测量的参数和不明确的主动物理机制，限制了它们捕捉单细胞特征和涌现的多细胞行为的能力。在此，我们介绍了一种尺度自适应的混合机器学习（ML）框架，其中互补的物理引导和物理不可知方法分别解决了单细胞和多细胞尺度上的上述关键问题。物理引导的机器学习方法将物理模型与实验数据相结合，以推断以前不可测量的参数，从而能够更准确地表征单细胞形状和速度特征，但未知的主动力和固有的物理假设仍然限制了其预测多细胞尺度动力学的能力。相比之下，物理不可知的机器学习方法绕过了显式的物理假设，直接从历史状态序列中模拟多细胞行为。该方法对实验观察到的粗粒度密度振荡和波提供了稳健的长期预测，但在应用于单细胞尺度建模时具有较高的随机性。通过将每种方法分配到其最有效的尺度，我们的框架利用了它们各自的优势，同时减轻了它们的局限性。这种互补策略弥合了理论建模与实验观察之间的差距，为多尺度集体细胞动力学提供了一种通用的计算范式，在各种生理和病理背景下具有广泛的潜力。

## Abstract
Collective cell dynamics are fundamental to numerous physiological processes, including embryo development, tissue morphogenesis, immune response, and disease progression. Accurately modeling these dynamics across scales remains challenging, as traditional physics-based models usually rely on many unmeasurable parameters and unclear active physics, limiting their ability to capture both single-cell features and emergent multicellular behaviors. Here, we introduce a scale-adaptive hybrid machine learning (ML) framework, in which complementary physics-guided and physics-agnostic method each resolves an above key issue at single-cell and multicellular scales, respectively. The physics-guided ML method integrates physical models with experimental data to infer previously unmeasurable parameters, enabling more accurate characterization of single-cell shape and velocity features, but unknown active forces and inherent physical assumptions still constrain its ability to predict multicellular scale dynamics. In contrast, the physics-agnostic ML method bypasses explicit physical assumptions to directly model multicellular behaviors from historical state sequences. This method provides robust long-term predictions of coarse-grained density oscillations and waves observed experimentally, yet it suffers from high stochasticity when applied to single-cell scale modeling. By assigning each approach to the scale where it is most effective, our framework leverages their respective strengths while mitigating their limitations. This complementary strategy bridges the gap between theoretical modeling and experimental observations, offering a versatile computational paradigm for multiscale collective cell dynamics with broad potential in diverse physiological and pathological contexts.