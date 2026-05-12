---
title: Machine learning-driven discovery of therapeutic nucleoside hydrogels for periodontitis.
title_zh: 机器学习驱动的用于牙周炎治疗的核苷水凝胶发现
authors: "Weiqi Li, Yinghui Wen, Zhenyuan Huang, Fangyuan Shuai, Yijia Yin, Qianming Chen, Fudong Zhu, Hao Xu, Hang Zhao"
date: 2026-05-11
pdf: "https://pubmed.ncbi.nlm.nih.gov/42115209/"
tags: ["query:bioinfo"]
score: 7.0
evidence: 机器学习预测核苷生物活性及治疗性水凝胶合成
tldr: 针对牙周炎治疗中核苷超分子水凝胶生物活性预测难的问题，本研究利用决策树、随机森林和XGBoost等机器学习算法构建了9个预测模型，并提出MBSI和CMAS评分体系来量化核苷衍生物的特异性与综合性能。通过筛选成功发现GMP和dGMP两种具有高成胶性、生物相容性和抗菌活性的水凝胶，并在牙周炎模型中验证了其疗效，为生物医用材料的理性设计提供了新思路。
selection_source: fresh_fetch
motivation: 旨在解决核苷类超分子水凝胶在药物递送和组织工程应用中，其生物活性难以准确预测和理性设计的难题。
method: 采用多种机器学习算法构建生物活性预测模型，并引入分子生物活性特异性指数（MBSI）和复合分子属性评分（CMAS）进行多维度筛选。
result: 成功筛选出GMP和dGMP两种新型核苷水凝胶，实验证明其在牙周炎治疗中具有优异的抗菌性能和生物相容性。
conclusion: 证明了基于机器学习的筛选策略和量化评分体系在发现高性能生物活性材料方面的可行性，为口腔疾病靶向治疗提供了新工具。
---

## 摘要
超分子水凝胶在药物递送和组织工程中具有巨大潜力，因其独特的性质而脱颖而出。尽管前景广阔，但预测核苷的生物活性仍然具有挑战性。本研究旨在预测核苷的生物活性，以指导水凝胶的理性合成。具体而言，利用包括决策树、逻辑回归、随机森林和极限梯度提升（XGBoost）在内的特征选择机器学习方法，建立了针对各种生物活性的九个预测模型和数据库。随后，引入了分子生物活性特异性指数（MBSI）来衡量核苷衍生物的主要生物活性，并设计了复合分子属性评分（CMAS）来评估核苷衍生物的综合性能。随后，建立了生物活性核苷水凝胶的筛选策略，并确定了两种具有高成胶能力、生物相容性和抗菌活性的候选水凝胶（GMP 和 dGMP）。最后，验证了这两种水凝胶在牙周炎抗菌治疗中的作用。本研究强调了基于机器学习的策略以及 MBSI/CMAS 在理性设计用于生物医学应用的生物活性核苷水凝胶方面的可行性。GMP 和 dGMP 水凝胶的发现及其在牙周炎模型中的成功验证，突显了该策略在开发口腔疾病靶向疗法方面的潜力。

## Abstract
Supramolecular hydrogels hold significant potential in drug delivery and tissue engineering, with standing out for their unique properties. Despite their promise, predicting nucleoside bioactivity remains challenging. This study aims to predict the biological activity of nucleosides to guide the rational synthesis of hydrogels. Specifically, nine predictive models and databases for various biological activities were built with feature-selected machine learning methods including decision trees, logistic regression, random forest, and extreme gradient boosting. Then, the Molecular Bioactivity Specificity Index (MBSI) was introduced to gauge the primary bioactivity of nucleoside derivatives, and the Composite Molecular Attribute Score (CMAS) was devised to measure the overall performance of nucleoside derivatives. Subsequently, screening strategies for bioactive nucleoside hydrogels were established, and two candidate hydrogels (GMP and dGMP) with high hydrogel-forming ability, biocompatibility, and antibacterial activity were identified. Finally, two hydrogels were validated for antibacterial treatment of periodontitis. This study highlights the feasibility of ML-based strategies and MBSI/CMAS in rationally designing bioactive nucleoside hydrogels for biomedical applications. The discovery of GMP and dGMP hydrogels and their successful validation in periodontitis models highlight the potential of this strategy for developing targeted therapies for oral diseases.