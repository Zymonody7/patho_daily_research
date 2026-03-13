---
title: "NCRDLLM: Predicting ncRNA-Drug Response Associations via Multimodal Feature Fusion and Large Language Models."
title_zh: NCRDLLM：通过多模态特征融合与大语言模型预测 ncRNA-药物反应关联
authors: "Zihan Zhang, Yuchen Zhang"
date: 2026-03-12
pdf: "https://pubmed.ncbi.nlm.nih.gov/41817976/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 大语言模型预测ncRNA-药物反应关联
tldr: 针对非编码RNA（ncRNA）与药物反应预测中单一RNA类型局限及多模态语义融合不足的问题，本文提出了NCRDLLM框架。该框架整合了miRNA、lncRNA和circRNA数据，利用RNA-FM、ChemBERTa等预训练模型提取序列、结构及疾病关联特征，并通过适配器映射至LLaMA-3.2-3B大模型进行LoRA微调。实验显示其在三类ncRNA预测任务中均取得优异表现（AUC-ROC最高达0.9832），为癌症精准用药提供了强有力的计算支持。
selection_source: fresh_fetch
motivation: 现有的ncRNA-药物关联预测方法多局限于单一RNA类型，且难以充分挖掘生物分子间复杂的多模态语义关联。
method: 构建了一个基于LLaMA-3.2-3B的统一框架，融合了由RNA-FM、ChemBERTa及图算法提取的序列、结构与疾病语义特征，并采用LoRA进行高效微调。
result: 在miRNA、lncRNA和circRNA三类药物关联数据集上，该模型分别实现了0.9665、0.9832和0.9676的AUC-ROC评分，显著优于现有基准。
conclusion: 通过大语言模型整合多模态生物特征，能够有效提升ncRNA与药物反应关联预测的准确性与泛化能力。
---

## 摘要
非编码 RNA (ncRNA) 在癌症药物反应中发挥着关键的调节作用。然而，现有的大多数方法仅限于预测单一类型的 ncRNA，未能充分捕捉多模态生物特征之间复杂的语义关联，因此表现出较弱的泛化能力和鲁棒性。为了克服这些局限性，本研究提出了 NCRDLLM，这是一个利用大语言模型 (LLM) 预测三种类型的 ncRNA（环状 RNA、微小 RNA 和长链非编码 RNA）与药物之间关联的统一框架。该方法整合了 19,020 条经实验验证的关联记录和 120,009 条疾病关联记录。构建了三类多模态特征：使用预训练基础模型 RNA-FM 和 ChemBERTa 提取的序列特征；通过 Graph2Vec 生成的 RNA 二级结构特征以及结合 ECFP 的 AttentiveFP 生成的药物分子结构特征；以及通过疾病相关编码和语义相似性获得的关联特征。随后，这些特征通过适配器模块映射到 LLaMA-3.2-3B 的隐藏空间中，并采用 LoRA 进行参数高效微调。实验结果表明，NCRDLLM 在 miRNA-药物、lncRNA-药物和 circRNA-药物数据集上的 AUC-ROC 值分别达到 0.9665、0.9832 和 0.9676。消融研究证实了各模块的贡献，而文献证据和组织特异性表达谱进一步支持了预测结果的生物学相关性。NCRDLLM 为识别潜在的 ncRNA-药物反应关联提供了一种有效的策略。

## Abstract
Noncoding RNAs (ncRNAs) play critical regulatory roles in cancer drug response. However, most existing methods are limited to predicting a single type of ncRNA, failing to fully capture the complex semantic associations between multimodal biological features, and thus exhibit weak generalizability and robustness. To overcome these limitations, this study proposes NCRDLLM, a unified framework that leverages large language models (LLMs) to predict associations between three types of ncRNA (circular RNA, microRNA, and long noncoding RNA) and drugs. The method integrates 19,020 experimentally validated associations and 120,009 disease association records. Three types of multimodal features are constructed: sequence features extracted using pretrained foundation models RNA-FM and ChemBERTa, structural features generated through Graph2Vec for RNA secondary structures and AttentiveFP combined with ECFP for drug molecules, and association features obtained via disease-associated coding and semantic similarity. These features are subsequently mapped into the hidden space of LLaMA-3.2-3B through adapter modules, with LoRA employed for parameter-efficient fine-tuning. Experimental results demonstrate that NCRDLLM achieves AUC-ROC values of 0.9665, 0.9832, and 0.9676 on miRNA-drug, lncRNA-drug, and circRNA-drug data sets, respectively. Ablation studies confirm the contribution of each module, while literature evidence and tissue-specific expression profiling further support the biological relevance of the predictions. NCRDLLM provides an effective strategy for identifying potential ncRNA-drug response associations.