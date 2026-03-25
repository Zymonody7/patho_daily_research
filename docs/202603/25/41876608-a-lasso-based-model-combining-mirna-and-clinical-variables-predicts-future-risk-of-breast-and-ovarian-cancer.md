---
title: A lasso-based model combining miRNA and clinical variables predicts future risk of breast and ovarian cancer.
title_zh: 一种结合 miRNA 和临床变量的基于 lasso 的模型可预测乳腺癌和卵巢癌的未来风险
authors: "James W Webber, Laura Wollborn, Sudhanshu Mishra, Stephanie Alimena, Bryanna Testino, Konrad Stawiski, Wojciech Fendler, Dipanjan Chowdhury, Kevin M Elias"
date: 2026-03-24
pdf: "https://pubmed.ncbi.nlm.nih.gov/41876608/"
tags: ["query:bioinfo"]
score: 7.0
evidence: 结合 miRNA 和临床变量的 lasso 模型
tldr: 针对遗传性乳腺癌和卵巢癌综合征（HBOC）诊断率低且基因检测存在局限性的问题，研究者开发了一种结合血清 miRNA 谱与临床数据的 Lasso 模型。该模型通过量化“BRCAness”特征，在 1831 人的队列中实现了 0.98 的 BRCA 突变预测 AUC，并在独立临床试验中成功预测了未来 5 年的卵巢癌发病风险（AUC=0.75）。该方法为早期识别高危人群提供了一种非侵入性的生物标志物工具。
selection_source: fresh_fetch
motivation: 许多遗传性癌症高危患者未被确诊，且常规基因检测无法覆盖所有具有类似 BRCA 突变特征的风险人群。
method: 利用 Lasso 回归将血清 miRNA 表达谱与临床变量映射到低维空间，构建线性分类模型来评估个体的“BRCAness”评分及长期患癌风险。
result: 模型在预测 BRCA 突变状态上达到 0.98 的 AUC，且其输出评分与独立人群的 5 年卵巢癌相对风险高度相关（R=0.93）。
conclusion: 结合 miRNA 和临床数据的机器学习模型能有效识别具有遗传风险特征的个体，并预测未来卵巢癌的发生。
---

## 摘要
遗传性乳腺癌和卵巢癌综合征 (HBOC) 主要由 BRCA1 和 BRCA2 的生殖系突变引起。然而，大多数患有 HBOC 的女性未被诊断出来，且一些符合 HBOC 临床标准的患者在基因检测后未发现可识别的突变。在本研究中，我们部署了一个基于 lasso 的模型，将血清 miRNA 谱与临床数据相结合，从机构生物样本库招募的 1831 名受试者中识别出卵巢癌风险升高的女性。使用 lasso 将 miRNA 和元数据变量映射到二维空间，随后训练线性分类模型以评估“BRCAness”和癌症的长期风险。经过十折交叉验证，该方法的 BRCA 预测 AUC 得分为 0.98（95% CI 0.94-1.0），并可在按年龄、癌症史和种族/族裔群体分层的各亚组中推广。为了证明该表型的临床相关性，我们使用基于 lasso 的模型评估了一个独立队列中 1044 名受试者的 5 年卵巢癌风险，这些受试者参加了一项随机临床试验，且其基因检测结果未知。在这一非选择性人群中，基于 lasso 的模型的输出与 5 年卵巢癌相对风险的对数强相关（R = 0.93, 95% CI 0.83-0.97, p < 0.0001）。当该模型被直接用于预测未来卵巢癌的发病时，其 AUC 为 0.75（95% CI 0.70-0.78）。综上所述，这些数据表明所提出的模型是未来卵巢癌风险的预测因子。

## Abstract
Hereditary breast and ovarian cancer syndrome (HBOC) is principally caused by germline mutations in BRCA1 and BRCA2. However, most women with HBOC are undiagnosed, and some patients meeting clinical criteria for HBOC will have no identifiable mutation after genetic testing. Here, we deploy a lasso-based model to combine serum miRNA profiles with clinical data to identify women at elevated risk for ovarian cancer among a population of 1831 individuals enrolled in an institutional biobank. The miRNA and metadata variables are mapped to two-dimensional space using lasso, after which a linear classification model is trained to estimate "BRCAness" and long-term risk of cancer. After tenfold cross-validation, the method offers a BRCA prediction AUC score of 0.98 (95% CI 0.94-1.0) and generalizes across subgroups stratified by age, cancer history, and racial/ethnic group. To demonstrate the clinical relevance of this phenotype, we use the lasso-based model to assess 5-year ovarian cancer risk among an independent cohort of 1044 subjects agnostic to genetic testing results enrolled in a randomized clinical trial. In this unselected population, the output of the lasso-based model strongly correlates to the log 5-year relative risk of ovarian cancer (R = 0.93, 95% CI 0.83-0.97, p < 0.0001). When the model was used to predict future onset of ovarian cancer directly, the AUC offered was AUC = 0.75 (95% CI 0.70-0.78). Together, these data suggest the proposed model is a predictor of future ovarian cancer risk.