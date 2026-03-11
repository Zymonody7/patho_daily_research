---
title: Development and validation of a high-confidence diagnostic model integrating ctDNA methylation and serum biomarkers for early-stage hepatocellular carcinoma detection.
title_zh: 整合ctDNA甲基化与血清生物标志物用于早期肝细胞癌检测的高置信度诊断模型的开发与验证
authors: "Han Wu, Mingda Wang, Zhiyi Wan, Lanqing Yao, Shuang Zhou, Hui Wang, Guoyue Lv, Nanya Wang, Fengmei Wang, Jiahao Xu, Xinfei Xu, Chao Li, Yongkang Diao, Timohty M Pawlik, Rui Liu, Feng Shen, Tian Yang"
date: 2026-03-11
pdf: "https://pubmed.ncbi.nlm.nih.gov/41807813/"
tags: ["query:bioinfo"]
score: 6.0
evidence: 整合 ctDNA 和血清生物标志物的多模态诊断模型
tldr: "针对早期肝细胞癌（HCC）筛查中现有血清标志物灵敏度不足的问题，本研究开发了多模态诊断模型 GAMAD。该模型融合了 ctDNA 甲基化检测（HepaAiQ）与性别、年龄、AFP 及 DCP 等传统指标。在 1,692 例样本的临床验证中，GAMAD 在早期（0/A期）肝癌检测中实现了 86.5% 的灵敏度和 0.952 的 AUC，显著优于传统的 GALAD 模型，为高风险人群的早期精准诊断提供了强有力的辅助工具。"
selection_source: fresh_fetch
motivation: 现有的血清生物标志物在肝癌早期诊断中灵敏度较低，难以满足高风险人群的筛查需求。
method: 提出 GAMAD 多模态模型，通过整合循环肿瘤 DNA（ctDNA）甲基化特征与性别、年龄、甲胎蛋白（AFP）及异常凝血酶原（DCP）等临床指标进行综合判定。
result: "在独立测试集上，该模型对早期肝癌的检测灵敏度达到 86.5%，整体曲线下面积（AUC）达 0.952，性能全面超越了现有的 GALAD 诊断模型。"
conclusion: GAMAD 模型通过多源数据融合显著提升了早期肝癌的检出率，可作为标准影像学检查的重要补充手段。
---

## 摘要
肝细胞癌（HCC）仍是癌症相关死亡的主要原因，若能在高风险人群中实现早期发现，可显著改善预后。目前的血清生物标志物对早期疾病的敏感性有限。我们开发并验证了GAMAD，这是一种整合了循环肿瘤DNA（ctDNA）甲基化与既有血清标志物的多模态诊断模型，旨在提高中国早期HCC的检测水平。在这项多中心前瞻性试验中，共纳入1,692名患者：476名HCC患者、645名肝炎患者、443名肝硬化患者和128名无检测到肝脏异常的受试者。进行了包括AFP、AFP-L3、DCP和ctDNA甲基化（HepaAiQ）在内的血液检测。利用训练、验证和独立测试队列，我们通过整合HepaAiQ与性别、年龄、AFP和DCP开发了GAMAD模型。在所有样本中，HepaAiQ的表现优于AFP、DCP和AFP-L3，其敏感性为74.6%，特异性为88.1%，曲线下面积（AUC）为0.862（95% CI, 0.842-0.883）。专门针对早期HCC优化的GAMAD模型在验证队列中实现了80.5%的敏感性、90.4%的特异性和0.934的AUC（95% CI, 0.911-0.957）。在独立测试队列中，GAMAD表现出卓越的性能，对0/A期HCC的敏感性为86.5%，对B-C期HCC的敏感性为91.7%（AUC 0.952, 95% CI, 0.931-0.973），在所有队列中均显著优于GALAD模型。GAMAD模型代表了早期HCC检测的重大临床进展。其临床预期用途是作为高风险人群标准影像学检查的补充，从而大幅提高早期诊断率。

## Abstract
Hepatocellular carcinoma (HCC) remains a leading cause of cancer-related mortality, with significantly improved prognosis when detected early in high-risk populations. Current serum biomarkers show limited sensitivity for early-stage disease. We developed and validated GAMAD, a multimodal diagnostic model integrating circulating tumor DNA (ctDNA) methylation with established serum markers to enhance early HCC detection in China. In this multicenter prospective trial, a total of 1,692 patients were enrolled: 476 with HCC, 645 with hepatitis, 443 with cirrhosis, and 128 with no detectable liver abnormalities. Blood tests including AFP, AFP-L3, DCP, and ctDNA methylation (HepaAiQ) were performed. Using training, validation, and independent test cohorts, we developed the GAMAD model by integrating HepaAiQ with gender, age, AFP, and DCP. HepaAiQ demonstrated a superior performance compared with AFP, DCP, and AFP-L3 with a sensitivity of 74.6%, specificity of 88.1%, and an area under the curve (AUC) of 0.862 (95% CI, 0.842-0.883) in all samples. The GAMAD model, optimized specifically for early-stage HCC, achieved sensitivity of 80.5%, specificity of 90.4%, and AUC of 0.934 (95% CI, 0.911-0.957) in the validation cohort. In the independent test cohort, GAMAD showed superior performance with sensitivity of 86.5% for stage 0/A and 91.7% for stage B-C HCC (AUC 0.952, 95% CI, 0.931-0.973), substantially outperforming the GALAD model across all cohorts. The GAMAD model represents a significant clinical advancement for early HCC detection. Its intended clinical use is to serve as an adjunct to standard imaging for high-risk populations, substantially increasing early diagnosis rates.