---
title: A novel serum metabolite classifier for identifying Metabolic Dysfunction-Associated Steatotic Liver Disease (MASLD) integrating metabolomics and machine learning.
title_zh: 一种整合代谢组学与机器学习的用于识别代谢功能障碍相关脂肪性肝病（MASLD）的新型血清代谢物分类器
authors: "Binghui Li, Yiru Zhang, Ziyang Li, Zhiyang Chen, Zhe Guo, Weimin Wu, Li Tan, Lini Dong, Xiangyu Zhang, Xing Lyu, Min Hu, Qichen Long"
date: 2026-04-29
pdf: "https://pubmed.ncbi.nlm.nih.gov/42056921/"
tags: ["query:bioinfo"]
score: 7.0
evidence: 结合代谢组学和机器学习进行疾病分类
tldr: 针对代谢相关脂肪性肝病（MASLD）缺乏无创诊断标志物的问题，本研究通过非靶向代谢组学和16S rDNA测序分析血清代谢物与肠道菌群的关联，利用LASSO回归筛选出10种关键代谢物并构建随机森林分类器。该模型在验证集上达到0.87的AUROC，结合临床指标后提升至0.94，为MASLD的早期筛查提供了高效的无创诊断方案。
selection_source: fresh_fetch
motivation: 旨在解决代谢相关脂肪性肝病（MASLD）在临床诊断中缺乏可靠、无创的生物标志物这一难题。
method: 结合非靶向血清代谢组学、肠道菌群测序以及LASSO回归特征筛选，构建了基于随机森林算法的代谢物分类模型。
result: 筛选出10种关键代谢物，构建的模型在独立验证集上AUROC达0.87，融合BMI、ALT等临床指标后性能进一步提升至0.94。
conclusion: 研究揭示了MASLD相关的系统性代谢改变，并证明了代谢组学结合机器学习在提升肝病无创诊断准确性方面的巨大潜力。
---

## 摘要
背景：代谢功能障碍相关脂肪性肝病（MASLD）已成为日益严重的全球健康负担，而用于识别受累个体的可靠非侵入性生物标志物仍然有限。本研究旨在表征与脂肪变性和纤维化相关的血清代谢组学特征，并开发一种具有临床应用价值的基于代谢物的分类器。方法：在经 FibroScan 表征的发现队列（n = 35）中进行非靶向血清代谢组学分析，以识别与肝脂肪变性和纤维化负担相关的候选代谢特征。为了给观察到的代谢改变提供生物学背景，随后对部分参与者（n = 27）的配对粪便样本进行了 16S rDNA 测序。随后对差异代谢物进行 LASSO 回归以进行特征选择，并在包含健康对照（n = 19）和经超声确诊的 MASLD 患者（n = 52）的验证队列中构建随机森林诊断模型。结果：代谢组学分析揭示了不同程度脂肪变性和纤维化的独特代谢模式。共鉴定出分别与脂肪变性和纤维化负担相关的 55 种和 46 种差异丰度代谢物。微生物组分析表明肠道微生物组成发生了改变，综合相关性分析提示了数个潜在的微生物-代谢物关联，包括两对显示出较强相关性的代谢物-属对。LASSO 回归筛选出一组由 10 种代谢物组成的面板作为最具信息量的诊断特征。以这些代谢物作为输入变量，构建的随机森林分类器实现了 0.87 的受试者工作特征曲线下面积（AUROC）。加入四项临床变量（BMI、ALT、甘油三酯和高密度脂蛋白胆固醇）后，模型性能进一步提升，AUROC 达到 0.94。结论：本研究表征了与 MASLD 相关的全身代谢改变，并提出了一种整合血清代谢物与临床指标的非侵入性诊断模型。总之，这些发现强调了代谢组学辅助方法在识别 MASLD 以及提高对疾病相关代谢变化生物学理解方面的潜在效用。

## Abstract
BACKGROUND: Metabolic dysfunction-associated steatotic liver disease (MASLD) presents a growing global health burden, while reliable non-invasive biomarkers for identifying affected individuals remain limited. This study aimed to characterize serum metabolomic signatures associated with steatosis and fibrosis and to develop a clinically applicable metabolite-based classifier. METHODS: Untargeted serum metabolomics was performed in a FibroScan-characterized discovery cohort (n = 35) to identify candidate metabolic features associated with hepatic steatosis and fibrosis burden. To provide biological context for the observed metabolic alterations, 16 S rDNA sequencing was subsequently conducted in paired fecal samples from a subset of participants (n = 27). Differential metabolites were then subjected to LASSO regression for feature selection and used to construct a random forest diagnostic model in a validation cohort comprising healthy controls (n = 19) and ultrasound-confirmed MASLD patients (n = 52). RESULTS: Metabolomic profiling revealed distinct metabolic patterns across different degrees of steatosis and fibrosis. A total of 55 and 46 metabolites were identified as differentially abundant in relation to steatosis and fibrosis burden, respectively. Microbiome analysis indicated alterations in gut microbial composition, and integrative correlation analysis suggested several potential microbe-metabolite associations, including two metabolite-genus pairs showing relatively strong correlations. LASSO regression selected a panel of ten metabolites as the most informative diagnostic features. Using these metabolites as input variables, a random forest classifier was constructed and achieved an area under the receiver operating characteristic curve (AUROC) of 0.87. Incorporation of four clinical variables (BMI, ALT, triglycerides, and HDL cholesterol) further improved model performance, yielding an AUROC of 0.94. CONCLUSION: This study characterizes systemic metabolic alterations associated with MASLD and presents a non-invasive diagnostic model integrating serum metabolites with clinical indicators. Together, these findings highlight the potential utility of metabolomics-assisted approaches for identifying MASLD and for improving biological understanding of disease-associated metabolic changes.