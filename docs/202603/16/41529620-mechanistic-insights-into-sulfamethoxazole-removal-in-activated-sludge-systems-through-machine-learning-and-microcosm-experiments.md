---
title: Mechanistic insights into sulfamethoxazole removal in activated sludge systems through machine learning and microcosm experiments.
title_zh: 通过机器学习和微宇宙实验解析活性污泥系统中磺胺甲恶唑去除的机理
authors: "Junjie Chen, Lipin Li, Xiaowei Lv, Tao Liu, Jun Zhang, Liwen Luo, Yu Tian"
date: 2026-03-15
pdf: "https://pubmed.ncbi.nlm.nih.gov/41529620/"
tags: ["query:pathoai"]
score: 8.0
evidence: 用于抗生素去除和 AMR 风险缓解的机器学习框架
tldr: "针对活性污泥法处理废水中抗生素（以磺胺甲恶唑SMX为例）去除率波动大且机制不明的问题，本研究构建了基于随机森林回归（RFR）的机器学习框架，整合多尺度实验数据识别关键影响因子。研究发现工艺控制参数对去除率贡献最大，并首次揭示了驯化时间、pH等关键阈值。通过60天微观实验验证，模型指导的工艺优化实现了近100%的去除率，为污水处理抗生素降解提供了数据驱动的决策支持。"
selection_source: fresh_fetch
motivation: 旨在解决活性污泥工艺中抗生素去除效果不稳定且缺乏定量机制指导的难题。
method: 利用随机森林模型对多尺度数据集进行特征工程与因果分析，并结合微观实验验证模型预测的生物学合理性。
result: 模型准确预测了SMX去除率（R²=0.83），识别出驯化时间（15天）和氨氮浓度等关键阈值，并证实氨氮去除率是比COD更强的降解指示指标。
conclusion: 该研究证明了机器学习能有效揭示复杂生化过程中的非线性机制，为优化污水处理系统以应对抗生素污染提供了可操作的科学依据。
---

## 摘要
废水中的抗生素残留构成了严重的生态和公共健康风险，甚至可能诱发更严重的抗菌素耐药性（AMR）威胁。活性污泥（AS）工艺作为全球废水处理的核心，在减轻这些风险方面发挥着关键作用。然而，AS 系统中的抗生素去除率波动很大，且机理尚不明确。本研究选择磺胺甲恶唑（SMX）作为代表性抗生素，利用来自实验室、中试和全规模系统的综合数据集，开发了一个全面的基于机器学习（ML）的框架，用于识别关键因素并阐明控制 AS 工艺中 SMX 生物降解的过程级机制。经过全因子网格优化、5 折交叉验证和特征工程，随机森林回归（RFR）模型的表现优于其他模型，并获得了最高的预测性能（测试集 R² = 0.83），独立验证确认了其强大的泛化能力（预测误差 < 20%）。特征归因、依赖性和因果分析表明，过程控制参数（43%）在 SMX 去除中占主导地位，其次是进水参数（30%）和过程性能参数（27%）。识别出了包括驯化期（AP）、pH、进水 SMX 和氨氮（NH4+-N）在内的关键因素，并首次利用 RFR 模型揭示了其阈值（15 天、7.3-8.0、0.2 mg/L、43 mg/L）。模型识别出的进水 SMX 浓度和 AP 的类阈值效应控制了生物降解的启动，而进水 NH4+-N 则通过共代谢调节 SMX 的去除。因果推理进一步表明，对于 SMX 生物降解，NH4+-N 去除率是比 COD 去除率更强的 AS 工艺性能指标。为期 60 天的微宇宙验证证实，RFR 指导的驯化实现了近 100% 的 SMX 去除（0.2 mg/L-10 mg/L），并支持了模型推断的类阈值行为的生物学合理性，提供了超越模型的机理见解。该框架将数据驱动的预测与机理理解相结合，提供了一种可推广的方法，并为优化 AS 工艺以减轻抗生素污染提供了可操作的指导。

## Abstract
Antibiotic residues in wastewater pose serious ecological and public health risks and may even induce the more severe threat of antimicrobial resistance (AMR). The activated sludge (AS) processes, the backbone of global wastewater treatment, play a central role in mitigating these risks. However, antibiotic removal in AS systems remains highly variable and mechanistically unclear. Here, sulfamethoxazole (SMX) was selected as a representative antibiotic to develop a comprehensive machine learning (ML)-based framework for identifying key factors and elucidating process-level mechanisms governing SMX biodegradation in AS processes using an integrated dataset from lab-, pilot-, and full-scale systems. The random forest regression (RFR) model outperformed other models and achieved the highest predictive performance (testing R² = 0.83) after full-factor grid optimization, 5-fold cross-validation and feature engineering, with strong generalization confirmed by independent (prediction error < 20 %). Feature attribution, dependency, and causal analyses revealed that process control parameters (43 %) dominated SMX removal, followed by influent (30 %) and process performance parameters (27 %). Key factors including acclimation period (AP), pH, influent SMX, and ammonia nitrogen (NH4+-N) were identified, with threshold values (15 days, 7.3-8.0, 0.2 mg/L, 43 mg/L) revealed for the first time using the RFR model. Model-identified threshold-like effects of influent SMX concentration and AP governed the initiation of biodegradation, while influent NH4+-N regulated SMX removal via co-metabolism. Causal inference further indicated that NH4+-N removal rate was a stronger performance indicator of AS processes for SMX biodegradation than COD removal rate. The 60-day microcosm validation confirmed that the RFR-guided acclimation achieved near 100 % SMX removal (0.2 mg/L-10 mg/L) and supported the biological plausibility of the model-inferred threshold-like behavior, providing mechanistically informed insights beyond model. This framework integrates data-driven prediction with mechanistic understanding, providing a generalizable approach and offering actionable guidance for optimizing AS processes to mitigate antibiotic pollution.