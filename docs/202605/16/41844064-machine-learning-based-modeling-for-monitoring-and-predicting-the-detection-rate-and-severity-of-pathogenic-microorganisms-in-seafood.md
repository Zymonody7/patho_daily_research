---
title: Machine learning-based modeling for monitoring and predicting the detection rate and severity of pathogenic microorganisms in seafood.
title_zh: 基于机器学习的海产品病原微生物检出率与严重程度监测及预测建模
authors: "Wei Mi, Yijie Kong, Yongxin Ma, Chunbo Gong, Yapeng Huo, Xueying Feng, Sha Liu"
date: 2026-05-16
pdf: "https://pubmed.ncbi.nlm.nih.gov/41844064/"
tags: ["query:pathoai"]
score: 9.0
evidence: 用于预测海产品中病原体流行率和严重程度的机器学习框架
tldr: 针对海产品致病微生物监测中传统方法灵敏度不足的问题，本研究利用烟台市十年间的监测数据，构建了集成时空特征与动态阈值优化的机器学习框架。通过对比LightGBM和XGBoost等多种算法，实现了对病原体检出率和危害程度的高精度预测。该框架在外部验证中表现稳健，为沿海海产品供应链的风险预警和资源分配提供了数据驱动的决策支持。
selection_source: fresh_fetch
motivation: 传统海产品微生物监测方法在动态环境下的灵敏度和特异性不足，难以实现对污染风险的精准预警。
method: 整合十年间的微生物检测数据，利用时空分析提取特征，并结合动态阈值优化策略，对比了LightGBM、XGBoost等六种机器学习算法的预测性能。
result: "LightGBM在检出率预测中达到99.9%的正向预测值，而XGBoost在三级严重程度分类任务中实现了93.7%的准确率和0.989的AUC。"
conclusion: 该研究证明了结合时空环境特征与自适应阈值的机器学习模型能有效识别海产品污染风险，为食品安全监管提供了可扩展的技术方案。
---

## 摘要
海产品中的病原微生物污染对食品安全和公共卫生构成了持续风险。传统的监测方法往往缺乏足够的灵敏度和特异性，特别是在动态环境条件下。为解决这些局限性，本研究利用 2014 年至 2024 年间在中国烟台采集的海产品样本微生物检测数据，开发了一个机器学习（ML）框架，并将 2025 年的数据保留用于外部验证。该框架可同时预测病原体的流行率和严重程度等级。此外，探索性数据分析评估了变量分布及其与检出率的统计关联。时间序列分析识别出显著的长期趋势和季节性模式，而空间分析揭示了不同行政区域间污染风险的异质性，特别是在沿海经济区和主要港口。应用动态阈值优化策略，本研究使用六种机器学习算法预测了检出率：ROSE-LASSO、LightGBM、XGBoost、k-NN、CART 和 SVM。LightGBM 在 0.157 的优化阈值下表现出最佳性能，特异性为 97.6%，阳性预测值（PPV）为 99.9%。外部验证证实了其稳健性，灵敏度为 91.2%，F1 分数为 92.4%，PPV 为 93.6%。对于三级严重程度分类，XGBoost 实现了 93.7% 的总体准确率，对高风险样本的灵敏度较高（80.0%），AUC 为 0.989。通过将时空环境特征与自适应阈值相结合，该框架为沿海海产品供应链中的病原体风险识别提供了一种可扩展的方法，为预警系统和基于证据的资源配置提供支持。

## Abstract
Pathogenic microbial contamination in seafood presents persistent risks to food safety and public health. Conventional monitoring methods frequently lack adequate sensitivity and specificity, particularly under dynamic environmental conditions. To address these limitations, this study developed a machine learning (ML) framework utilizing microbial testing data from seafood samples collected in Yantai, China (2014-2024), with 2025 data reserved for external validation. The framework simultaneously predicts pathogen prevalence and severity levels. And, exploratory data analysis assessed variable distributions and statistical associations with detection rates. Time series analysis identified significant long-term trends and seasonal patterns, while spatial analysis revealed heterogeneity in contamination risk across administrative regions, particularly in coastal economic zones and major ports. Applying a dynamic threshold optimization strategy, detection rates were predicted using six ML algorithms: ROSE-LASSO, LightGBM, XGBoost, k-NN, CART, and SVM. LightGBM demonstrated optimal performance with 97.6% specificity and 99.9% positive predictive value (PPV) at an optimized threshold of 0.157. External validation confirmed its robustness, yielding 91.2% sensitivity, a 92.4% F1 score, and 93.6% PPV. For three-class severity classification, XGBoost achieved 93.7% overall accuracy and high sensitivity (80.0%) for high-risk samples, with an AUC of 0.989. By integrating spatiotemporal environmental features with adaptive thresholding, this framework provides a scalable approach for pathogen risk identification within coastal seafood supply chains, supporting early warning systems and evidence-based resource allocation.