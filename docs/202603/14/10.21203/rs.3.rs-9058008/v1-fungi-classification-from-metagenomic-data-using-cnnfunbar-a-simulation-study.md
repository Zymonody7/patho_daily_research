---
title: "Fungi classification from metagenomic data using CNN_FunBar: A simulation study"
title_zh: 基于 CNN_FunBar 的宏基因组数据真菌分类：一项模拟研究
authors: "Das R, Rai A, Mishra DC, Jha GK, Dutta S, Rakshit D, Sharma A, Talukdar A."
date: 2026-03-13
pdf: "https://doi.org/10.21203/rs.3.rs-9058008/v1"
tags: ["query:pathoai"]
score: 10.0
evidence: 基于CNN的架构用于宏基因组数据集中的真菌分类
tldr: "针对宏基因组数据中真菌分类难的问题，本研究利用CNN_FunBar架构，基于ITS序列的六聚体特征训练了属级和种级分类模型。通过模拟包含130个微生物基因组的农田土壤数据集进行验证，该模型在种级和属级分类上分别达到了91.93%和95.16%的准确率，为复杂环境样本中的真菌精准鉴定提供了高效的深度学习工具。"
selection_source: fresh_fetch
motivation: 由于真菌基因组结构复杂，从宏基因组数据中准确识别和分类真菌物种一直是计算生物学领域的难题。
method: 利用CNN_FunBar深度学习架构，基于ITS序列的六聚体特征训练分类模型，并通过模拟农田土壤宏基因组数据进行性能评估。
result: "该模型在模拟数据集上实现了超过91%的种级和95%的属级分类准确率，成功识别出绝大多数预设的真菌类别。"
conclusion: 研究证明了卷积神经网络在处理复杂环境样本真菌分类任务中的高效性，为宏基因组研究提供了实用的分类工具。
---

## 摘要
由于真核生物基因组固有的复杂性，从宏基因组数据集中进行真菌分类仍然是一项极具挑战性的任务。内部转录间隔区（ITS）被广泛认为是真菌分类鉴定的可靠 DNA 标记。此前，开发了一种基于卷积神经网络（CNN）的架构 CNN_FunBar，并证明其在多个分类层级上分类真菌 ITS 序列具有高效性。在本研究中，使用 UNITE+INSDC 参考 ITS 数据集对两个 CNN_FunBar 分类器（即 Genus_Model.h5 和 Species_Model.h5）进行了重新训练，以分类 429 个不同的真菌物种和 1,293 个属。在测试数据集上，重新训练的模型在属级和种级分类的平均准确率分别超过了 90% 和 95%。为了进一步评估模型性能，利用 MetaSim 读段模拟器，使用 130 个微生物全基因组（65 个细菌和 65 个真菌基因组）模拟了农田土壤宏基因组，随后使用 MEGAHIT 进行重叠群（contig）组装。使用 ITSx 工具从组装好的重叠群中提取完整的 ITS 区域。随后，基于六聚体（hexamer）特征，分别使用 Genus_Model.h5 和 Species_Model.h5 在属级和种级对提取的 ITS 序列进行分类。结果表明，Species_Model.h5 和 Genus_Model.h5 的分类准确率分别为 91.93% 和 95.16%，从模拟宏基因组数据集中正确鉴定了 62 个物种和 41 个属。本研究为计算生物学和宏基因组学领域的研究人员提供了宝贵的见解和实用工具。

## Abstract
<title>Abstract</title>  <p>Fungal classification from metagenomic datasets remains a highly challenging task due to the inherent complexity of eukaryotic genomes. The internal transcribed spacer (ITS) region is widely recognised as a reliable DNA marker for fungal taxonomic identification. Previously, a convolutional neural network (CNN)-based architecture, CNN_FunBar, was developed and demonstrated high efficiency in classifying fungal ITS sequences across multiple taxonomic levels. In the present study, two CNN_FunBar classifiers, namely Genus_Model.h5 and Species_Model.h5, were retrained using the UNITE+INSDC reference ITS datasets to classify 429 distinct fungal species and 1,293 genera. The retrained models achieved average accuracies exceeding 90% and 95% for genus- and species-level classification, respectively, on the test dataset. To further evaluate model performance, an agricultural soil metagenome was simulated using 130 microbial whole genomes (65 bacterial and 65 fungal genomes) through the MetaSim read simulator, followed by contig assembly using MEGAHIT. Complete ITS regions were extracted from the assembled contigs using the ITSx tool. The extracted ITS sequences were then classified at the genus and species levels using Genus_Model.h5 and Species_Model.h5, respectively, based on hexamer features. The results demonstrated that Species_Model.h5 and Genus_Model.h5 achieved classification accuracies of 91.93% and 95.16%, respectively, correctly identifying 62 species and 41 genera from the simulated metagenomic dataset. This study provides valuable insights and practical tools for researchers working in computational biology and metagenomics.</p>

---

## 论文详细总结（自动生成）

这篇论文介绍了一种利用深度学习技术对宏基因组数据中的真菌进行分类的方法。以下是对该研究的详细总结：

### 1. 解决的问题与研究意义
在宏基因组学（直接研究环境样本中所有微生物遗传物质）中，真菌的鉴定一直是个难题。相比细菌，真菌等真核生物的基因组更复杂。目前，科学家通常利用 **ITS（内部转录间隔区）** 序列作为真菌的“身份条形码”。
*   **痛点**：传统的分类方法（如基于比对的 BLAST）在处理海量、破碎的宏基因组数据时，计算开销大，且对序列变异的容忍度有限。
*   **意义**：本研究通过改进和验证 **CNN_FunBar**（一种基于卷积神经网络的分类架构），证明了深度学习可以高效、准确地从复杂的环境模拟数据中识别真菌，为土壤生态监测和病原体检测提供了新工具。

### 2. 白话版概述
想象你有一袋打碎的拼图（宏基因组数据），里面混杂了成千上万种生物的碎片。研究者先给 AI 看了大量的真菌“身份证照片”（ITS 序列数据库），让它记住不同真菌特有的字母排列规律。然后，研究者在电脑里模拟了一份包含 130 种微生物的“虚拟土壤”样本，把这些碎片拼接起来，再让 AI 去认里面的真菌。结果发现，AI 能以超过 90% 的准确率叫出这些真菌的名字（属名和种名）。

### 3. 方法部分
*   **核心思想**：将 DNA 序列转化为数值特征，利用 CNN 提取局部模式进行分类。
*   **特征工程**：使用 **六聚体（Hexamer）** 频率。即统计 DNA 序列中所有长度为 6 的短片段（如 ATAGCC）出现的次数。由于 DNA 有 4 种碱基，6 位的组合共有 $4^6 = 4096$ 种，因此每条序列被转化为一个 4096 维的向量。
*   **模型结构**：CNN_FunBar 架构。包含卷积层（用于捕捉碱基排列的局部特征）、池化层（降维并保留重要信息）和全连接层（最终分类）。
*   **推理流程**：
    1.  **模拟与组装**：用软件模拟产生测序数据，并用 MEGAHIT 工具将短片段拼接成较长的连续序列（Contigs）。
    2.  **提取**：使用 ITSx 工具从拼接好的序列中精准切出 ITS 区域。
    3.  **分类**：将提取的 ITS 序列输入预训练好的 `Genus_Model.h5`（属级）和 `Species_Model.h5`（种级）模型。

### 4. 实验部分
*   **数据**：训练集来自 UNITE 和 INSDC 数据库；测试集是一个模拟的农田土壤宏基因组（包含 65 种细菌和 65 种真菌的全基因组）。
*   **任务**：对 1293 个属和 429 个种进行多分类。
*   **评价指标**：准确率（Accuracy）、精确率（Precision）、召回率（Recall）和 F1 分数。
*   **主要结果**：
    *   在标准测试集上，属级和种级准确率分别超过 **90%** 和 **95%**。
    *   在模拟的土壤宏基因组中，种级分类准确率为 **91.93%**，属级为 **95.16%**。

### 5. 资源与算力
*   **文中未充分披露**。论文提到了模型以 `.h5` 格式保存（表明使用了 TensorFlow/Keras 框架），但未具体说明训练所用的 GPU 型号、核心数或具体的训练耗时。

### 6. 真正可信的贡献
*   **全流程验证**：该研究不仅在干净的数据库序列上做测试，还模拟了“测序-组装-提取-分类”的完整宏基因组分析流程，这证明了该模型在处理实际科研数据时的鲁棒性。
*   **大规模分类**：模型能够处理超过 1000 个类别的分类任务，这在生物信息学深度学习应用中属于较高水平。

### 7. 局限与风险
*   **物种覆盖度有限**：虽然涵盖了 1200 多个属，但自然界真菌种类数以百万计，模型对数据库之外的“暗物质”物种缺乏识别能力（即 Out-of-Distribution 问题）。
*   **依赖组装质量**：如果宏基因组测序深度不足，导致 ITS 区域无法被 MEGAHIT 正确组装，模型将无从发挥作用。
*   **模拟数据偏差**：模拟环境（130 个基因组）比真实土壤（可能含有数万种微生物）简单得多，真实场景下的噪声和污染可能会降低准确率。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事环境微生物组学、精准农业、以及寻找传统比对算法（如 BLAST/QIIME2）替代方案的研究者。
*   **后续可跟进的问题**：如何利用 Transformer 或长序列建模技术直接处理未组装的原始读段（Reads），从而绕过高耗时的组装步骤？

（完）
