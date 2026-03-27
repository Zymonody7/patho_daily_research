---
title: Identifying systemic lupus erythematosus from serum proteomic profiles using machine learning and genetic risk stratification.
title_zh: 利用机器学习和遗传风险分层从血清蛋白质组谱中识别系统性红斑狼疮
authors: "Hocaoǧlu M, Das J, Sawalha AH."
date: 2026-03-26
pdf: "https://pubmed.ncbi.nlm.nih.gov/41884878/"
tags: ["query:bioinfo"]
score: 7.0
evidence: 用于蛋白质组和遗传风险分层的机器学习
tldr: 系统性红斑狼疮（SLE）的早期诊断和风险评估仍具挑战。本研究利用 UK Biobank 等多中心队列的血清蛋白质组数据，构建了机器学习分类模型，用于识别既往病例并预测未来发病风险。结果显示，该模型在识别准确率上显著优于传统线性模型和多基因风险评分，并在跨种族队列中表现出良好泛化性，同时识别出 SCARB2 等关键生物标志物，为 SLE 的精准诊疗提供了新工具。
selection_source: fresh_fetch
motivation: 旨在利用大规模血清蛋白质组数据，解决系统性红斑狼疮在临床诊断和早期风险预测中缺乏高效生物标志物的问题。
method: 基于 UK Biobank 队列，通过差异表达分析刻画蛋白质特征，并对比了线性模型、机器学习模型及多基因风险评分在疾病分类与预测中的表现。
result: "机器学习模型在识别 SLE 方面表现优异，在 95% 特异性下达到约 90% 的敏感性，并成功在瑞典和中国独立队列中完成验证。"
conclusion: 蛋白质组机器学习模型不仅能高效识别已确诊的红斑狼疮，还能在临床确诊前进行有效预测，为发现新型生物标志物提供了可靠路径。
---

## 摘要
<h4>目的</h4>针对狼疮的全蛋白质组风险模型仍有待深入研究。我们开发了分类模型，旨在通过血清蛋白质组谱识别狼疮。<h4>方法</h4>研究纳入了英国生物样本库（UK Biobank）中的狼疮患者及其他自身免疫性疾病患者。对差异蛋白质表达进行了表征，并随后进行了层次聚类分析。开发了蛋白质组线性模型和机器学习模型，用于既往疾病分类和未来狼疮预测，并与多基因风险评分（PRS）进行了比较。来自瑞典（作为人类蛋白质图谱 [HPA] 的一部分）和中国的两个独立狼疮队列被用于验证。<h4>结果</h4>在英国生物样本库中，研究了 44,173 名具有蛋白质组数据的参与者，其中包括 2,063 名在入组时患有至少一种自身免疫性疾病的个体。这包括 383 名狼疮患者，发病时的平均年龄为 43.6 ± 11.7 岁。在自身免疫性疾病中，狼疮表现出数量最多的失调蛋白，并与类风湿性关节炎聚类在一起。与 HPA 的比较显示，约 70% 的狼疮蛋白质组关联可以被复制，且效应量具有中度相关性。机器学习模型在识别既往狼疮方面优于线性模型，并能很好地推广到未来狼疮的预测。在接受免疫调节药物治疗的狼疮患者中，该模型在 95% 的特异性下达到了约 90% 的敏感性，这在独立队列中得到了验证。模型解释强调了 SCARB2、SOD2、CD302、Galectin-9 和 GGT5 蛋白对狼疮识别具有显著影响。<h4>结论</h4>蛋白质组机器学习模型在识别既往狼疮方面表现优异，并能很好地推广到临床诊断前的狼疮预测。模型解释识别出了新的狼疮候选生物标志物。

## Abstract
<h4>Objectives</h4>Proteome-wide risk models for lupus remain underexplored. We developed classification models to identify lupus from serum proteomic profiles.<h4>Methods</h4>Lupus patients and individuals with other autoimmune diseases in the UK Biobank were included. Differential proteomic expressions were characterized and followed by hierarchical clustering analysis. Proteomic linear and machine learning models were developed for established disease classification and future lupus prediction, and compared to polygenic risk scores (PRS). Two additional independent lupus cohorts from Sweden, as part of the Human Protein Atlas (HPA), and from China were used for replication.<h4>Results</h4>44,173 participants with proteomic data including 2,063 individuals with at least one autoimmune disease at enrollment were studied in the UK Biobank. This included 383 lupus patients with a mean age of 43.6 ± 11.7 at disease onset. Lupus showed the largest number of dysregulated proteins among autoimmune diseases and clustered with rheumatoid arthritis. Comparison with HPA showed that ~70% of lupus proteomic associations could be replicated with moderate correlation in effect sizes. The machine learning model outperformed the linear model in identifying preexisting lupus and generalized well to future lupus prediction. Among lupus patients on immunomodulatory medications, the model reached ~90% sensitivity at 95% specificity, which was replicated in an independent cohort. Model interpretation highlighted SCARB2, SOD2, CD302, Galectin-9, and GGT5 proteins with substantial effects on lupus identification.<h4>Conclusions</h4>Proteomic machine learning models show excellent performance for identifying preexisting lupus and generalizes well for predicting lupus before clinical diagnosis. Model interpretation identified novel candidate biomarkers for lupus.