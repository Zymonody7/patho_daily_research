---
title: Urinary extracellular vesicle miRNA signature reflects pancreatic islet stress in type 2 diabetes.
title_zh: 尿液细胞外囊泡 miRNA 特征反映了 2 型糖尿病中的胰岛应激
authors: "Md Zubbair Malik, Mohammed Dashti, Anwar Mohammad, Mohamed Al-Sayegh, Mohammed Al-Onaizi, Rasheeba Nizam, Khadija M Dashti, Mohamed Abu-Farha, Jehad Abubaker, Fahd Al-Mulla, Hamad Ali"
date: 2026-04-22
pdf: "https://pubmed.ncbi.nlm.nih.gov/42017432/"
tags: ["query:seqai"]
score: 6.0
evidence: miRNA测序与监督机器学习用于诊断性能评估
tldr: "针对2型糖尿病（T2D）早期诊断难的问题，本研究分析了68名受试者的尿液细胞外囊泡（ECV）miRNA测序数据，通过机器学习筛选出包含5个核心miRNA的生物标志物组合。该组合在内外验证集中均表现出高诊断准确率（AUC>0.86），且其表达模式与胰岛等代谢组织的分子变化高度一致，为无创监测T2D进展提供了具有生物学解释性的新手段。"
selection_source: fresh_fetch
motivation: 寻找一种能够反映胰岛细胞压力且无创的2型糖尿病早期诊断生物标志物。
method: 利用尿液细胞外囊泡miRNA测序数据，结合机器学习模型筛选关键标志物，并跨组织验证其与胰岛、肝脏等代谢器官的相关性。
result: 鉴定出46个差异表达的miRNA，其中由5个核心miRNA组成的联合诊断模型在外部验证中达到了0.86的曲线下面积（AUC）。
conclusion: 尿液ECV中的miRNA特征不仅能作为高准确度的无创诊断工具，还能有效映射胰岛等关键代谢组织的病理生理状态。
---

## 摘要
引言：2 型糖尿病 (T2D) 是一种以胰岛素抵抗和进行性 β 细胞功能障碍为特征的进展性代谢疾病。早期检测对于预防长期并发症至关重要。尿液细胞外囊泡 (ECV) 微小 RNA (miRNA) 已成为稳定的非侵入性生物标志物，具有反映与代谢疾病相关的系统性分子变化的潜力。方法：我们分析了先前生成的来自 68 名成年人（40 名 T2D 患者和 28 名健康对照者）特征明确队列的尿液 ECV miRNA 测序数据。通过受试者工作特征 (ROC) 分析和具有 10 折交叉验证的监督机器学习模型，鉴定并评估了差异表达的 miRNA 的诊断性能。进行了独立外部验证以评估泛化能力。利用来自胰岛、血液、肝脏和脂肪组织的公开数据集进行了跨组织验证。在不同组织中检查了预测的靶基因，并进行了 miRNA-mRNA 相互作用网络及通路富集分析，以探索其功能相关性。结果：与对照组相比，T2D 患者尿液 ECV 中的 46 个 miRNA 显著失调。网络瓶颈中心性分析优先筛选出 5 个关键 miRNA（miR-320a、miR-16-5p、miR-125b-5p、miR-26a-5p 和 miR-30c-5p）。单个 miRNA 显示出中等的区分能力（AUC 0.73-0.81），而组合面板提高了性能（内部 AUC = 0.87；外部 AUC = 0.86）。失调的尿液 miRNA 模式部分反映了胰岛和其他代谢组织中的表达变化。靶基因分析揭示了关键代谢调节因子的组织特异性改变，包括 PTEN、IGF1R、HMGA1、VEGFA、MCL1、CCND2、BTG2 和 SMAD4。结论：尿液 ECV miRNA 反映了与 T2D 相关的分子改变，是具有疾病进展机制相关性的、有前景的补充性非侵入性生物标志物。

## Abstract
INTRODUCTION: Type 2 diabetes (T2D) is a progressive metabolic disorder characterized by insulin resistance and progressive β-cell dysfunction. Early detection remains critical to prevent long-term complications. Urinary extracellular vesicle (ECV) microRNAs (miRNAs) have emerged as stable, non-invasive biomarkers with the potential to reflect systemic molecular alterations associated with metabolic disease. METHODS: We analyzed previously generated urinary ECV miRNA sequencing data from a well-characterized cohort of 68 adults (40 T2D and 28 healthy controls). Differentially expressed miRNAs were identified and evaluated for diagnostic performance using receiver operating characteristic (ROC) analysis and supervised machine learning models with 10-fold cross-validation. Independent external validation was performed to assess generalizability. Cross-tissue validation was conducted using publicly available datasets from pancreatic islets, blood, liver, and adipose tissue. Predicted target genes were examined across tissues, and miRNA-mRNA interaction networks with pathway enrichment analyses were performed to explore functional relevance. RESULTS: Forty-six miRNAs were significantly dysregulated in urinary ECVs from T2D patients compared with controls. Network bottleneck centrality analysis prioritized five key miRNAs (miR-320a, miR-16-5p, miR-125b-5p, miR-26a-5p, and miR-30c-5p). Individual miRNAs demonstrated moderate discriminatory capacity (AUC 0.73-0.81), while the combined panel improved performance (internal AUC = 0.87; external AUC = 0.86). Dysregulated urinary miRNA patterns partially mirrored expression changes in pancreatic islets and other metabolic tissues. Target gene analysis revealed tissue-specific alterations in key metabolic regulators, including PTEN, IGF1R, HMGA1, VEGFA, MCL1, CCND2, BTG2, and SMAD4. CONCLUSION: Urinary ECV miRNAs reflect molecular alterations associated with T2D and represent promising complementary, non-invasive biomarkers with mechanistic relevance to disease progression.