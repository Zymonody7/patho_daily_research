---
title: Multitask Pretraining Framework for Improving Predictivity of Machine Learning Chemical Bioactivity Models for Low-Data Endpoints.
authors: "Noah J Wichrowski, Mary Versa Clemens-Sewall, Karun K Rao, Casey Richardson, Nam Q Le, Phillip T Koshute, James Y Liu, Yaroslav Chushak, Jayme P Coyle, Teresa R Sterner, Rebecca A Clewell"
date: 2026-03-26
pdf: "https://pubmed.ncbi.nlm.nih.gov/41887802/"
tags: ["query:bioinfo"]
score: 8.0
evidence: 化学生物活性和药物发现的多任务预训练
tldr: 针对化学毒理学中许多终点数据稀缺、单任务模型泛化性差的问题，本研究提出了一种多任务预训练框架。该框架首先在多个中等规模的 ToxCast 数据集上进行联合训练以提取通用的分子表征，随后将其与下游分类器结合，应用于仅有约100个样本的小数据任务。实验证明，该方法在多数低数据任务上的预测准确率优于传统化学描述符，为解决毒理学预测中的数据孤岛和样本不足问题提供了有效方案。
selection_source: fresh_fetch
motivation: 传统的单任务 QSAR 模型难以处理数据量极小的毒理学终点，且无法利用相关任务间的共性信息进行知识迁移。
method: 通过在多个中等规模的 ToxCast 任务上预训练多任务神经网络来学习分子表征，并将其迁移至下游的小样本预测任务中。
result: 相比于使用标准化学表征的传统机器学习方法，该多任务预训练流水线在大多数低数据量任务上均取得了显著的性能提升。
conclusion: 多任务预训练能够有效捕捉化学空间中的通用生物活性信息，显著增强了机器学习模型在数据匮乏场景下的毒性预测能力。
---

## Abstract
Computational models are crucial for rapid hazard screening of novel chemicals when time and resources are not available for laboratory assessment. The rise of machine learning (ML) methods powering quantitative structure-activity relationship (QSAR) models has enabled data-driven development of predictive models for health effects screening. However, these models are typically single-task, meaning that they are trained on a single toxicological endpoint and lack transferability to similar tasks, i.e., the ability to predict chemicals' effects on related endpoints. Thus, when predictions are needed for another endpoint, a new model must be trained from scratch. Further, single-task ML models are typically trained on very large, homogeneous data sets, which are not available for most adverse outcome endpoints. Effective hazard screening would benefit from approaches that can handle multiple small, noisy data sets recording complex chemical and biological mechanisms. To that end, we trained an ML model simultaneously on multiple tasks curated from moderate-sized (∼1000 observations) ToxCast data sets. To predict novel tasks from small (∼100 observations) ToxCast data sets, we combined our pretrained multitask model with a task-specific predictor, either a random forest or a neural network. These two components comprise a novel ML pipeline that generates and uses molecular representations from our multitask model. Compared to a common ML approach using standard chemical representations, our pipeline performed statistically better on a majority of tasks, regardless of the choice of downstream predictor. The advantage of the molecular representations from our multitask model, over those from a single-task model, is that they combine information on multiple effects to provide a model of chemical space that captures generalizable information. This work contributes to efforts to improve the utility of ML QSAR methods for predicting chemicals' bioactivity on low-data toxicological endpoints.