---
title: Tokenizing loops of antibodies.
title_zh: 抗体环区的标记化
authors: "Ada Fang, Robert G Alberstein, Simon Kelow, Frédéric A Dreyer"
date: 2026-12-31
pdf: "https://pubmed.ncbi.nlm.nih.gov/41936024/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 用于蛋白质基础模型的多模态抗体环分词器
tldr: 抗体CDR环结构对结合抗原至关重要，但传统聚类方法覆盖度低且难以与大模型集成。本研究开发了Igloo分词器，通过对比学习将抗体环的骨架二面角与序列信息映射为离散Token。实验证明Igloo在H3环检索、亲和力预测及抗体设计任务中表现出色，能以更小参数量达到SOTA水平，为抗体工程提供了高效的多模态表征方案。
selection_source: fresh_fetch
motivation: 针对现有抗体CDR环表征方法覆盖不全且难以直接应用于蛋白质大模型的问题，亟需一种能融合结构与序列信息的离散化分词工具。
method: 提出Igloo多模态分词器，采用对比学习目标将具有相似骨架二面角的抗体环在潜空间中拉近，实现结构与序列的统一编码。
result: "Igloo在H3环检索准确率上提升了6.1%，并在亲和力预测任务中以1/7的参数量达到了SOTA模型的性能，同时实现了1.9倍的HER2结合剂零样本富集。"
conclusion: Igloo通过引入多模态Token，有效解决了抗体环构象的离散表征难题，显著增强了蛋白质大模型在抗体变体筛选与序列设计中的能力。
---

## 摘要
抗体的互补决定区（CDRs）是与其抗原相互作用的关键环状结构，对于新型生物药物的设计具有重要意义。现有的表征 CDR 多样性的方法覆盖范围有限，且难以直接整合到蛋白质基础模型中。在此，我们介绍了免疫球蛋白环区标记器（ImmunoGlobulin LOOp Tokenizer，简称 Igloo），这是一种编码主链二面角和序列的多模态抗体环区标记器。Igloo 采用对比学习目标进行训练，旨在将具有相似主链二面角的环区在潜空间中映射得更近。与最先进的蛋白质编码方法相比，Igloo 能够高效地从结构抗体数据库中检索最匹配的环状结构，在识别相似 H3 环区方面的表现优于现有方法 6.1%。Igloo 为所有环区分配标记（tokens），解决了经典簇覆盖范围有限的问题，同时保留了恢复经典环区构象的能力。为了展示 Igloo 标记的多功能性，我们证明了它们可以通过 IglooLM 和 IglooALM 整合到蛋白质语言模型中。在预测重链变体的结合亲和力方面，IglooLM 在 10 个抗体-抗原靶点中的 8 个上表现优于基础蛋白质语言模型。此外，它的表现与现有的最先进的基于序列和多模态的蛋白质语言模型相当，其性能可与参数量多出 7 倍的模型相媲美。IglooALM 采样的抗体环区在序列上更具多样性，在结构上比最先进的抗体逆折叠模型更具一致性。我们展示了 Igloo 能够快速且可扩展地从大型突变库中优先筛选功能性抗体变体，在零样本设置下，使经实验验证的 HER2 结合剂富集了 1.9 倍。Igloo 证明了为抗体环区引入多模态标记在编码其多样化景观、改进蛋白质基础模型以及抗体 CDR 设计方面的优势。

## Abstract
The complementarity-determining regions (CDRs) of antibodies are loop structures that are key to their interactions with antigens and are of high importance to the design of novel biologics. Existing approaches for characterizing the diversity of CDRs have limited coverage and cannot be readily incorporated into protein foundation models. Here we introduce ImmunoGlobulin LOOp Tokenizer, Igloo, a multimodal antibody loop tokenizer that encodes backbone dihedral angles and sequence. Igloo is trained using a contrastive learning objective to map loops with similar backbone dihedral angles closer together in latent space. Compared to state-of-the-art protein encoding approaches, Igloo can efficiently retrieve the closest matching loop structures from a structural antibody database, outperforming the existing methods on identifying similar H3 loops by 6.1%. Igloo assigns tokens to all loops, addressing the limited coverage issue of canonical clusters, while retaining the ability to recover canonical loop conformations. To demonstrate the versatility of Igloo tokens, we show that they can be incorporated into protein language models with IglooLM and IglooALM. On predicting binding affinity of heavy chain variants, IglooLM outperforms the base protein language model on 8 out of 10 antibody-antigen targets. Additionally, it is on par with existing state-of-the-art sequence-based and multimodal protein language models, performing comparably to models with 7× more parameters. IglooALM samples antibody loops which are diverse in sequence and more consistent in structure than state-of-the-art antibody inverse folding models. We show that Igloo can rapidly and scalably prioritize functional antibody variants from large mutagenesis libraries, achieving a 1.9× enrichment of experimentally validated HER2 binders in a zero-shot setting. Igloo demonstrates the benefit of introducing multimodal tokens for antibody loops for encoding their diverse landscape, improving protein foundation models, and for antibody CDR design.