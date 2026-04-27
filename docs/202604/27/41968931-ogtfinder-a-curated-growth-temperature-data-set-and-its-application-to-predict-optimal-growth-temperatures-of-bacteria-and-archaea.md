---
title: "OGTFinder: A Curated Growth Temperature Data Set and Its Application To Predict Optimal Growth Temperatures of Bacteria and Archaea."
title_zh: OGTFinder：一个经过整理的生长温度数据集及其在预测细菌和古菌最适生长温度中的应用
authors: "Sophie Colette, Jaldert François, Bart De Moor, Vera van Noort"
date: 2026-04-27
pdf: "https://pubmed.ncbi.nlm.nih.gov/41968931/"
tags: ["query:pathoai"]
score: 7.0
evidence: 机器学习预测细菌生长温度
tldr: 针对现有模型在极端温度和稀有分类群预测准确率低的问题，本研究构建了一个包含逾1.5万种生物的全面生长温度数据集，并利用加权评分和系统发育划分优化了多层感知机（MLP）模型。该模型通过分析蛋白质组平均氨基酸特征，实现了对原核生物最适生长温度（OGT）的高精度预测，为极端环境下酶的生物勘探提供了有力工具。
selection_source: fresh_fetch
motivation: 现有的最适生长温度预测模型过度依赖常温生物和常见分类群的数据，导致其在极端环境生物上的泛化能力不足。
method: 构建了包含1.5万余种生物的大型数据集，并利用蛋白质组平均氨基酸描述符训练了结合加权评分与系统发育划分的多层感知机模型。
result: 模型在测试集上取得了5.49 °C的均方根误差和0.84的R²评分，并揭示了蛋白质骨架柔韧性、电荷残基及表面可及性是预测温度的关键特征。
conclusion: 开源工具 OGTFinder 提升了对细菌和古菌生长温度预测的准确性，为极端酶的生物勘探提供了更可靠的计算支持。
---

## 摘要
生物体的最适生长温度 (OGT) 对于生物勘探在极端条件下工作的酶具有重要价值。现有的 OGT 预测模型虽然达到了很高的准确率，但主要捕捉了训练集中过度代表群体的趋势，包括在温和温度下生存的生物以及来自研究较充分的分类群的生物。在本研究中，我们引入了加权评分和系统发育划分，以提高预测模型的泛化能力。我们首先构建了一个新的生长温度数据集，包含分布在生命三域中的 15,000 多个物种，并特别注意纳入了 OGT 和极端温度数据。随后，我们利用蛋白质组平均氨基酸描述符，在原核生物 OGT 数据上训练了机器学习模型。表现最佳的模型是多层感知器 (MLP)，其测试均方根误差 (RMSE) 为 5.49 °C，R² 为 0.84。最重要的蛋白质组特征与骨架柔韧性、带电残基以及表面可及性相关。MLP 模型已集成到命令行工具 OGTFinder 中，并根据 MIT 许可证在以下地址开源：https://github.com/SC-Git1/OGTFinder。

## Abstract
The optimal growth temperature (OGT) of organisms is valuable in bioprospecting enzymes that work under extreme conditions. Existing OGT prediction models achieve high accuracy but mainly capture trends of overrepresented groups in the training set including organisms that thrive at moderate temperatures and those from well-described taxa. In this study, we incorporated weighted scoring and phylogenetic splits to improve the generalizability of the prediction models. We first built a new growth temperature data set comprising more than 15,000 species distributed over all three domains of life, with special attention to include OGT and extreme temperature data. We then trained machine learning models on the prokaryotic OGT data using proteome-averaged amino acid descriptors. The best-performing model was the multilayer perceptron (MLP) with a test RMSE of 5.49 °C and an R2 of 0.84. The most important proteome features were related to backbone flexibility and charged residues, as well as surface accessibility. The MLP model is integrated in the command line tool OGTFinder and available under MIT license at: https://github.com/SC-Git1/OGTFinder.