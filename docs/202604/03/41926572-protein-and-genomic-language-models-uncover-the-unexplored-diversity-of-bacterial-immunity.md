---
title: Protein and genomic language models uncover the unexplored diversity of bacterial immunity.
title_zh: 蛋白质和基因组语言模型揭示了细菌免疫中尚未被探索的多样性。
authors: "Ernest Mordret, Alexandre Hervé, Florian Tesson, Hugo Vaysset, Tyler Clabby, Arthur Loubat, Helena Shomar, Remi Planel, Rachel Lavenir, Jean Cury, Aude Bernheim"
date: 2026-04-02
pdf: "https://pubmed.ncbi.nlm.nih.gov/41926572/"
tags: ["query:pathoai"]
score: 10.0
evidence: 用于细菌免疫和抗噬菌体功能预测的基因组语言模型
tldr: "细菌泛基因组中蕴含着极其丰富的抗噬菌体防御系统，但绝大部分尚未被发现。本研究开发了结合蛋白质序列与基因组上下文（操纵子结构）的机器学习模型，以高达99%的准确率预测抗噬菌体功能。通过在实验中验证12个新系统并分析3.2万个基因组，研究揭示了细菌基因组中约1.5%用于防御，且超过85%的预测防御家族仍未被表征。该工作为系统性探索细菌免疫多样性及开发新型生物技术工具奠定了基础。"
selection_source: fresh_fetch
motivation: 旨在解决细菌泛基因组中抗噬菌体防御系统多样性极高但大部分仍处于“暗物质”状态、难以被传统方法识别的问题。
method: 结合蛋白质语言模型与基因组上下文信息，构建了能够从序列和结构特征中自动识别抗噬菌体功能的互补性机器学习框架。
result: 实验验证了12个全新的抗噬菌体系统，并从3.2万个基因组中挖掘出超过1.9万个候选防御操纵子家族。
conclusion: 研究证明了细菌免疫领域仍存在巨大的未开发空间，并提供了一个交互式目录以支持未来对新型分子防御机制的系统化探索。
---

## 摘要
细菌泛基因组包含极其多样的抗噬菌体系统，其总体规模目前仍不为人所知。在本研究中，我们开发了互补的机器学习方法，通过基因组上下文、蛋白质序列或两者的结合来系统地预测抗噬菌体功能，实现了高达 99% 的精确率和 92% 的召回率。我们在埃希氏菌属（Escherichia）和链霉菌属（Streptomyces）中对这些模型进行了实验验证，并发现了 12 种抗噬菌体系统。将这些模型应用于超过 32,000 个细菌基因组后，我们扩展了预测的抗噬菌体库，发现约 1.5% 的细菌基因组专门用于防御，且超过 85% 的预测蛋白家族仍未被表征。我们提供了一个包含 19,000 多个候选操纵子家族的交互式目录，供后续实验研究。总之，这些发现表明细菌免疫中的大多数分子多样性仍未被表征，并为系统性探索奠定了基础。

## Abstract
The bacterial pangenome contains a vast diversity of antiphage systems, whose overall extent is still unknown. In this study, we developed complementary machine learning approaches to systematically predict antiphage function from genomic context, protein sequence, or their combination, achieving up to 99% precision and 92% recall. We validated these models experimentally in Escherichia and Streptomyces with the discovery of 12 antiphage systems. Applied to over 32,000 bacterial genomes, these models expand the predicted antiphage repertoire, with ~1.5% of bacterial genomes devoted to defense and more than 85% of predicted protein families remaining uncharacterized. We provide an interactive catalog of more than 19,000 candidate operon families for experimental follow-up. Together, these findings show that most molecular diversity in bacterial immunity remains uncharacterized and provide a foundation for its systematic exploration.