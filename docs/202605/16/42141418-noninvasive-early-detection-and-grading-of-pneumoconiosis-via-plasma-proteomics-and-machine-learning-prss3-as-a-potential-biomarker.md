---
title: "Noninvasive early detection and grading of pneumoconiosis via plasma proteomics and machine learning: PRSS3 as a potential biomarker."
title_zh: 通过血浆蛋白质组学和机器学习进行尘肺病的无创早期检测和分级：PRSS3 作为潜在生物标志物
authors: "Yizhuo Tian, Mingyao Wang, Zhifei Hou, Wenfeng Zhu, Yong Gao, Jing Geng, Xinran Zhang, Kaiyuan Min, Jiangfeng Liu, Juntao Yang, Huaping Dai"
date: 2026-05-15
pdf: "https://pubmed.ncbi.nlm.nih.gov/42141418/"
tags: ["query:seqai"]
score: 7.0
evidence: 机器学习用于尘肺病血浆蛋白质组学和生物标志物检测
tldr: 针对煤工尘肺病（CWP）早期诊断缺乏有效血浆生物标志物的难题，本研究通过对158名受试者的血浆进行DIA质谱蛋白质组学分析，结合多种机器学习算法构建了疾病分级与早期筛查模型。研究发现PRSS3蛋白在区分粉尘暴露者与早期患者中表现卓越，AUC和准确率均达到1.00，为职业性肺病的无创早期诊断提供了高精度的分子依据和临床转化基础。
selection_source: fresh_fetch
motivation: 旨在解决煤尘诱发的肺纤维化在临床前期缺乏无创检测手段的问题，寻找能够实现尘肺病早期预警和精准分级的血浆生物标志物。
method: 利用DIA质谱技术对健康对照、粉尘暴露工人及不同分期尘肺患者的血浆蛋白质组进行深度测序，并运用多种机器学习算法筛选关键蛋白以构建预测模型。
result: 成功识别出1239个血浆蛋白并揭示了代谢-免疫轴在病程中的作用，其中PRSS3蛋白在区分暴露组与早期尘肺患者的任务中展现出极高的分类精度。
conclusion: 本研究建立了首个基于血浆蛋白质组学的尘肺病机器学习筛查模型，证实了PRSS3作为生物标志物在职业性肺病无创诊断中的临床应用潜力。
---

## 摘要
背景：煤尘作为一种持久的空气污染物，会诱导剂量相关的肺纤维化；然而，目前仍缺乏用于临床前毒性的血浆生物标志物。方法：本研究招募了 158 名受试者，包括 28 名健康对照（HCs）、30 名粉尘暴露工人（DEWs）以及 100 名处于不同阶段的煤工尘肺（CWP）患者（CWP-I 期 40 例，CWP-II 期 30 例，CWP-III 期 30 例）。通过数据非依赖性采集（DIA）质谱法进行血浆蛋白质组学分析。鉴定并对差异表达蛋白进行了功能注释。筛选关键蛋白并采用多种机器学习算法构建和验证预测模型。结果：我们鉴定了 1,239 种血浆蛋白，其中包括 645 种高置信度候选蛋白。功能富集分析显示，疾病进展与 PPAR 信号通路、胆固醇代谢、EB 病毒感染和磷酸戊糖途径等通路显著相关。这些改变集中在脂质代谢紊乱、慢性炎症信号和病毒诱导的免疫逃逸上，表明存在一个协调早期纤维化进展的代谢-免疫轴。我们成功构建了首个基于血浆蛋白质组学的尘肺病分级和早期筛查机器学习模型。值得注意的是，单一生物标志物 PRSS3 在区分粉尘暴露工人（DEW）与早期尘肺病患者（CWP-I）方面表现出卓越的性能，在训练集中曲线下面积（AUC）和准确率均达到 1.00，在验证集中 AUC 为 1.00，准确率在 0.93 至 1.00 之间。结论：本研究建立了基于血浆蛋白质组学的创新机器学习模型，用于尘肺病的分级和早期筛查。PRSS3 作为潜在生物标志物的发现突显了该方法的临床实用性。这些发现为职业性肺病的无创诊断策略和未来的转化研究奠定了基础。

## Abstract
BACKGROUND: Coal-dust, a persistent airborne pollutant, induces dose-related pulmonary fibrosis; however, plasma biomarkers for pre-clinical toxicity remain lacking. METHODS: We enrolled 158 participants, including 28 healthy controls (HCs), 30 dust-exposed workers (DEWs), and 100 patients with coal workers' pneumoconiosis (CWP) at different stages (n CWP-I=40, n CWP-II=30, n CWP-III=30). Plasma proteomic profiling was performed via data-independent acquisition (DIA) mass spectrometry. Differentially expressed proteins were identified and functionally annotated. Key proteins were selected and multiple machine learning algorithms were employed to construct and validate predictive models. RESULTS: We identified 1,239 plasma proteins, including 645 high-confidence candidates. Functional enrichment revealed significant associations between disease progression and pathways such as PPAR signaling, cholesterol metabolism, Epstein-Barr virus infection, and the pentose phosphate pathway. These alterations converge on dysregulated lipid metabolism, chronic inflammatory signaling and virus-induced immune evasion, suggesting a metabolic-immune axis that orchestrates early fibrotic progression. We successfully constructed the first plasma proteomics-based machine learning models for pneumoconiosis grading and early screening. Notably, a single biomarker, PRSS3, demonstrated exceptional performance in distinguishing DEW patients from early-stage pneumoconiosis patients (CWP-I), achieving an area under the curve (AUC) of 1.00 and an accuracy of 1.00 in the training set and an AUC of 1.00 with an accuracy between 0.93 and 1.00 in the validation set. CONCLUSION: This study establishes innovative machine learning-based models for the grading and early screening of pneumoconiosis via plasma proteomics. The identification of PRSS3 as a potential biomarker highlights the clinical utility of our approach. These findings provide a foundation for noninvasive diagnostic strategies and future translational research in occupational lung diseases.