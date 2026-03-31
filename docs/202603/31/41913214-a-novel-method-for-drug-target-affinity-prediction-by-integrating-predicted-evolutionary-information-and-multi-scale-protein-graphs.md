---
title: A novel method for drug-target affinity prediction by integrating predicted evolutionary information and multi-scale protein graphs.
title_zh: 一种通过整合预测的进化信息和多尺度蛋白质图进行药物-靶点亲和力预测的新方法
authors: "Mingjian Jiang, Huaibin Hang, Zihao Cui, Junxiao Feng, Weina Pang, Teng Ma, Zhi Zhang, Yaping Fan, Shunpeng Pang, Wei Zhou, Yuanyuan Zhang"
date: 2026-03-30
pdf: "https://pubmed.ncbi.nlm.nih.gov/41913214/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 蛋白质语言模型ESM-3用于药物靶点亲和力
tldr: 药物-靶点亲和力（DTA）预测是药物研发的关键，但传统方法依赖耗时的多序列比对（MSA）来获取进化信息，限制了计算效率。MAFI-DTA 模型通过 ESM-3 蛋白质语言模型直接从序列中提取进化上下文，并结合多尺度蛋白质图结构，利用 GNN、BiLSTM 和 Transformer 融合特征。实验证明该方法在多个基准数据集上优于现有模型，在保证预测精度的同时显著降低了计算开销，为加速药物筛选提供了高效工具。
selection_source: fresh_fetch
motivation: 针对传统 DTA 预测中多序列比对（MSA）计算成本过高、难以处理大规模数据的瓶颈，寻求一种更高效的进化信息提取方案。
method: 利用 ESM-3 预训练模型获取序列进化特征，并构建基于不同残基规模的多尺度蛋白质图，通过集成图神经网络与 Transformer 的架构提取结构信息。
result: 在多个公开基准数据集上的实验结果表明，MAFI-DTA 的预测精度显著超过了现有的主流 DTA 预测模型。
conclusion: 该研究证明了结合预训练语言模型提取的进化信息与多尺度结构特征能有效提升亲和力预测性能，并成功克服了传统 MSA 方法的计算限制。
---

## 摘要
背景：药物-靶点亲和力（DTA）预测对于药物研发至关重要。虽然蛋白质进化特征对于识别保守区域至关重要，但目前的方法依赖于计算成本高昂的多序列比对（MSA），这造成了显著的瓶颈。为了解决这一问题，我们提出了 MAFI-DTA，这是一种新型模型，通过使用先进的蛋白质语言模型 ESM-3 直接从序列中推导进化背景，从而规避了 MSA 的计算负担。此外，我们引入了一种基于不同残基数量的多尺度蛋白质图构建策略，通过集成图神经网络、BiLSTM 和 Transformer 模块的神经网络，实现了跨不同尺度的结构信息的有效提取。结果：在多个基准数据集上的实验验证表明，与现有方法相比，MAFI-DTA 取得了显著更好的性能。这种准确性的提高归功于预测的进化信息和多尺度图表示的有效结合。源代码可在 https://github.com/aliveadult/MAFI 获取。结论：MAFI-DTA 成功且高效地捕捉了关键的进化和多尺度结构背景，克服了传统 MSA 方法的局限性。该方法提供了一个高性能工具，促进了药物-靶点相互作用的研究并加速了药物研发进程。

## Abstract
BACKGROUND: Drug-target affinity (DTA) prediction is crucial for drug discovery. While protein evolutionary features are vital for identifying conserved regions, current methods rely on computationally expensive multiple sequence alignment (MSA), creating a significant bottleneck. To address this, we propose MAFI-DTA, a novel model that circumvents the computational burden of MSA by deriving evolutionary context directly from sequences using the advanced protein language model, ESM-3. Furthermore, we introduced a multi-scale protein graph construction strategy based on varying numbers of residues, enabling the effective extraction of structural information across different scales through a neural network integrating graph neural networks, BiLSTM, and transformer modules. RESULTS: Experimental validation on multiple benchmark datasets demonstrates that MAFI-DTA achieves significantly better performance compared to existing approaches. This improved accuracy is attributed to the effective incorporation of both the predicted evolutionary information and the multi-scale graph representations. The source code is available at https://github.com/aliveadult/MAFI. CONCLUSIONS: MAFI-DTA successfully captures crucial evolutionary and multi-scale structural context efficiently, overcoming the limitations of traditional MSA methods. This approach provides a high-performing tool that facilitates the study of drug-target interactions and accelerates the drug discovery process.