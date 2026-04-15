---
title: Accelerated Combinatorial Drug Design for Human Immunodeficiency Virus Resistance through Seeded Multisite λ-Dynamics.
title_zh: 通过种子引导的多位点 λ-动力学加速针对人类免疫缺陷病毒耐药性的组合药物设计
authors: "Paige E Bowling, Jonah Z Vilseck, Charles L Brooks"
date: 2026-04-14
pdf: "https://pubmed.ncbi.nlm.nih.gov/41911382/"
tags: ["query:pathoai"]
score: 8.0
evidence: 利用多位点动力学进行HIV耐药性药物设计
tldr: "针对 HIV 病毒快速变异导致的耐药性难题，本研究利用多位点 λ 动力学（MSλD）方法，在大规模化学空间（超过 12,000 种蛋白-配体组合）中探索了 HIV-1 逆转录酶抑制剂的结合性能。通过引入溶剂相自由能偏置种子技术，显著提升了采样效率。研究发现 indolizine 骨架比 indole 骨架具有更好的抗突变韧性，并识别出 Y188I 为关键耐药位点，为设计广谱抗病毒药物提供了高效的计算框架。"
selection_source: fresh_fetch
motivation: 应对 HIV 病毒因频繁突变而产生的耐药性，寻找能在多种突变体中保持稳定结合力的广谱抑制剂。
method: "采用多位点 λ 动力学（MSλD）结合溶剂相自由能偏置种子技术，对两种抑制剂骨架在不同突变位点下的 12,000 多种组合进行高效自由能计算。"
result: 发现较小的取代基（如 H、F、Cl）在所有位点表现更佳，且 indolizine 骨架在不同突变体中展现出比 indole 骨架更高的结合稳定性。
conclusion: 该研究建立了一套高效的计算框架，能够快速绘制药物耐药性图谱，并成功识别出 Y188I 等关键耐药热点，助力开发更具韧性的抗病毒药物。
---

## 摘要
耐药突变的不断涌现为开发有效疗法带来了重大挑战，特别是对于像人类免疫缺陷病毒（HIV）这样快速进化的病原体。了解微小的分子变化如何赋予对抗多种蛋白质突变体的韧性，对于下一代药物设计至关重要。在本研究中，我们应用多位点 λ-动力学（MSλD）来探索一个规模空前的化学空间，涵盖了超过 12,000 种 HIV-1 逆转录酶（HIV-RT）与非核苷类抑制剂的蛋白质-配体组合。我们同时探索了针对野生型蛋白以及活性位点内 181 和 188 位点处几种关键耐药突变的吲哚（indole）和吲嗪（indolizine）抑制剂支架。我们的模拟表明，在两种药物支架的所有三个位点上，较小的取代基（如氢、氟或氯原子）更受青睐。我们发现，最强抑制剂的结合亲和力排名在整个突变面板中保持高度保守，这支持了对真正具有韧性的通用结合剂的鉴定。此外，与吲哚支架相比，吲嗪支架在各突变体中预测出更有利的结合图谱，表明其具有更高的内在韧性。我们还绘制了治疗功效的极限图谱，结果显示 Y188I 突变是一个耐药热点，显著降低了所有测试化合物的结合亲和力。为了高效采样这一巨大的炼金术和突变空间，我们引入了一种偏置种子方法，该方法利用了溶剂相自由能模拟，而这些计算对于估算相对自由能已经是必需的。这项工作建立了一个强大且高效的框架，用于理解耐药性图谱，并指导设计能够克服 HIV-RT 等系统中突变驱动逃逸的稳健抗病毒疗法。

## Abstract
The seemingly endless emergence of drug-resistant mutations poses a significant challenge in developing effective therapeutics, particularly for rapidly evolving pathogens like human immunodeficiency virus (HIV). Understanding how small molecular changes can confer resilience against diverse protein mutants is crucial for next-generation drug design. In the work presented here, we apply multisite λ-dynamics (MSλD) to navigate a chemical space of unprecedented size of over 12,000 protein-ligand combinations of HIV-1 Reverse Transcriptase (HIV-RT) and non-nucleoside inhibitors. We simultaneously explore the indole and indolizine inhibitor scaffolds against the wild-type protein, as well as several key resistance-conferring mutations at residues 181 and 188 within the active site. Our simulations show that smaller substituents, such as hydrogen, fluorine, or chlorine atoms, are preferred at all three sites on both drug scaffolds. We find that the binding affinity rankings of the strongest inhibitors remain highly conserved across the entire mutational panel, supporting the identification of truly resilient universal binders. Furthermore, the indolizine scaffold predicts a more favorable binding landscape across the mutants compared to the indole scaffold, suggesting a higher intrinsic resilience. We also map the limits of therapeutic efficacy, which show the Y188I mutation as a resistance hotspot that markedly reduces binding affinity for all tested compounds. To efficiently sample this vast alchemical and mutational space, we introduce a bias seeding method that leverages solvent-phase free energy simulations, calculations already necessary for estimating the relative free energies. This work establishes a powerful and efficient framework for understanding drug resistance landscapes and guiding the design of robust antiviral therapies capable of overcoming mutation-driven escape in systems like HIV-RT.