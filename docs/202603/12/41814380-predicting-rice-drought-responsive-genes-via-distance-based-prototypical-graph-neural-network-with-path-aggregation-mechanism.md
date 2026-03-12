---
title: Predicting rice drought-responsive genes via distance-based prototypical graph neural network with path aggregation mechanism.
title_zh: 基于路径聚合机制的距离原型图神经网络预测水稻干旱响应基因
authors: "Jing Liu, Hongyan Zhang, Song Wang, Ning Zhang, Xinghui Zhu, Yi Xiao"
date: 2026-03-11
pdf: "https://pubmed.ncbi.nlm.nih.gov/41814380/"
tags: ["query:bioinfo"]
score: 7.0
evidence: 用于基因调控网络推理的图神经网络
tldr: 干旱严重影响水稻产量，识别抗旱基因对育种至关重要。针对生物网络中节点属性捕捉难、拓扑结构复杂及样本类别不平衡等挑战，本研究提出DPGNNPAM模型。该模型结合基因表达与蛋白质互作网络，利用随机游走和递归神经网络聚合路径特征，并引入原型网络处理不平衡数据。实验证明该方法优于传统图神经网络，成功预测出17个候选抗旱基因，其中12个已获文献证实，为水稻抗逆育种提供了精准的候选靶点。
selection_source: fresh_fetch
motivation: 旨在解决现有图神经网络在处理水稻基因网络时，难以充分利用节点属性、拓扑结构以及应对正负样本极度不平衡的问题。
method: 提出一种基于距离的原型图神经网络，通过随机游走生成路径并利用递归神经网络聚合特征，结合原型学习计算节点与类别中心间的加权相似度。
result: 实验结果显示该模型在识别水稻抗旱基因方面优于传统GNN，并准确预测了17个候选基因，其中大部分已在生物学文献中得到验证。
conclusion: 该研究证明了结合路径聚合与原型学习的图学习框架能有效挖掘植物抗逆基因，为农业生物信息学中的不平衡分类问题提供了新思路。
---

## 摘要
干旱是影响水稻产量和品质的主要不利因素。鉴定干旱响应基因对于培育抗旱品种至关重要。近年来，基于嵌入学习的图神经网络方法在生物网络中取得了显著成功。然而，在充分捕捉节点属性特征、表征拓扑结构以及解决类别不平衡方面仍存在挑战，这可能会限制模型的预测能力。为了解决这些问题，我们提出了一种具有路径聚合机制的基于距离的原型图神经网络（DPGNNPAM），用于挖掘水稻中的干旱响应基因。首先，我们结合水稻基因表达数据和蛋白质相互作用网络来构建基于图的数据集。接着，我们利用随机游走策略生成多样化的游走路径，并采用基于递归神经网络的路径聚合器来编码这些路径上的节点属性。随后，在训练过程中采用原型网络方法，以关注全局信息并解决样本不平衡问题。之后，通过测量节点嵌入与类别原型之间的距离来计算加权相似度。具体而言，类别原型是捕捉每个类别核心特征的代表性嵌入。最后，我们使用 softmax 函数将该值转换为预测概率。实验结果表明，DPGNNPAM 在识别水稻干旱响应基因方面优于传统的图神经网络算法。最终，我们鉴定了 17 个与干旱胁迫密切相关的候选基因，其中 12 个已在文献中被证实参与了植物的干旱胁迫响应。

## Abstract
Drought is a primary factor that adversely impacts rice yield and quality. Identifying drought-responsive genes is essential for developing drought-responsive cultivars. Recently, graph neural network methods based on embedding learning have shown considerable success in biological networks. However, challenges still remain in adequately capturing node attribute features, representing topological structures, and addressing class imbalance, which may constrain the model's predictive capability. To address these issues, we propose a distance-based prototypical graph neural network with path aggregation mechanism (DPGNNPAM) to mine drought-responsive genes in rice. First, we combine gene expression data and protein interaction networks in rice to construct graph-based datasets. Next, we utilize a random walk strategy to generate diverse walk paths and employ a recursive neural network-based path aggregator to encode node attributes along these paths. The prototypical network approach is subsequently employed during training to focus on global information and address the issue of sample imbalance. After that, the weighted similarity is computed by measuring the distance between the node embeddings and the class prototypes. Specifically, class prototypes are representative embeddings that capture the central characteristic of each class. Finally, we transform this value into a predictive probability using the softmax function. Experimental results demonstrate that DPGNNPAM outperforms traditional graph neural network algorithms in identifying drought-responsive genes in rice. Ultimately, we identify 17 candidate genes closely related to drought stress, 12 of which are confirmed in the literature as being involved in the plant's drought stress response.