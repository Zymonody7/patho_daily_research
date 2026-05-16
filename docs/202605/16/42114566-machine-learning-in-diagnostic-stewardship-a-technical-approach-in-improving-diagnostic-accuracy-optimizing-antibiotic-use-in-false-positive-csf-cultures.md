---
title: "Machine learning in diagnostic stewardship: A technical approach in improving diagnostic accuracy, optimizing antibiotic use in false positive CSF cultures."
title_zh: 机器学习在诊断管理中的应用：一种提高诊断准确性、优化脑脊液培养假阳性中抗生素使用的技术方法
authors: "T Vidhya, R Srinivasa Sundara Rajan, J K Saravana Priya, H B Veena Kumari"
date: 2026-05-15
pdf: "https://pubmed.ncbi.nlm.nih.gov/42114566/"
tags: ["query:pathoai"]
score: 7.0
evidence: 机器学习用于诊断准确性和抗生素使用优化
tldr: 针对脑脊液（CSF）培养中因样本污染导致的假阳性及抗生素滥用问题，本研究利用机器学习模型对生化指标进行多变量分析。通过ROC分析和主成分分析（PCA），模型在区分真实病原体、无生长样本和污染样本方面均表现出极高的准确性（AUC均超过0.95），为临床诊断管理提供了精准的决策支持，有助于减少不必要的广谱抗生素使用。
selection_source: fresh_fetch
motivation: 旨在解决脑脊液培养中因假阳性污染导致的误诊问题，从而优化抗生素使用并降低医疗成本。
method: 利用多变量相关性分析、ROC曲线分析和主成分分析（PCA），对脑脊液中的葡萄糖、乳酸和蛋白质等生化指标进行建模以识别感染模式。
result: 机器学习模型在识别病原体、无生长和污染样本上的AUC值分别达到0.956、0.971和0.955，且PCA能有效识别特定生物体的独特生化特征。
conclusion: 通过机器学习技术提升脑脊液样本的诊断准确性，可以有效区分真实感染与样本污染，强化临床诊断管理并支持早期感染检测。
---

## 摘要
诊断管理强调在正确的时间为患者进行正确的检测，并促进明智地使用快速、准确的分子诊断工具，以便启动适当的抗生素治疗，同时避免过度使用广谱抗生素，从而实现抗菌药物管理。对检测结果的正确解读对于避免过度诊断和过高的医疗成本至关重要。本研究旨在通过机器学习模型（包括 ROC 分析和主成分分析 (PCA)）评估污染率，从而评估脑脊液 (CSF) 的诊断准确性。多变量相关性分析显示，葡萄糖与乳酸和蛋白质呈负相关。受试者工作特征曲线 (ROC) 分析显示出较高的模型性能，病原体检测、无生长和污染的曲线下面积 (AUC) 值分别为 0.956、0.971 和 0.955。主成分分析显示数据集的方差约为 61%，并识别出少数生物体的独特模式，这可能有助于早期感染检测。通过提高脑脊液样本中真实感染的识别能力，该方法有助于减少假阳性并加强诊断管理。

## Abstract
Diagnostic stewardship emphasises ordering the right tests, at the right time for the patient and also promotes the judicious use of rapid and accurate molecular diagnostic tools to enable the initiation of proper antibiotic therapy, while avoiding excessive use of broad-spectrum antibiotics hence antimicrobial stewardship. Proper interpretation of the test is crucial to avoid over-diagnosis and excessive healthcare costs. This study aimed to access the CSF diagnostic accuracy by evaluating contamination rate through machine learning models, including ROC analysis and principal component analysis (PCA). Multivariate correlation analysis showed glucose was negatively correlated with lactate and protein. Receiver operating characteristic curve analysis demonstrated high model performance, with Area Under the Curve values of 0.956 for pathogen detection, 0.971 for no-growth, and 0.955 for contamination. The principal component analysis revealed a variance of around 61% for the data set and identified unique pattern for few organisms, potentially supporting early infection detection. By improving the identification of true infections in CSF samples, this approach contributes in reducing false positives and enhancing diagnostic stewardship.