---
title: Predicting microbial community responses to disturbance using genome-resolved trait-based life-history strategies.
title_zh: 利用基因组解析的基于性状的生活史策略预测微生物群落对扰动的响应
authors: "Ezequiel Santillan, Soheil A Neshat, Stefan Wuertz"
date: 2026-04-23
pdf: "https://pubmed.ncbi.nlm.nih.gov/42023670/"
tags: ["query:pathoai"]
score: 6.0
evidence: 微生物群落响应与生态策略
tldr: 针对微生物群落如何响应环境扰动这一生态学核心问题，本研究将植物学中的CSR（竞争者-开拓者-耐逆者）生活史策略框架引入微生物研究。通过在合成废水生物反应器中设置不同频率的有机负荷扰动，结合宏基因组学和机器学习分析，揭示了群落从竞争主导向耐逆主导演变的规律。该方法为预测复杂生态系统动态提供了统一的性状分析工具，有助于提升生态系统管理和生物技术应用的精准度。
selection_source: fresh_fetch
motivation: 旨在解决微生物群落对环境扰动响应难以预测的问题，探索能否利用生活史策略框架建立微生物性状与生态功能之间的通用联系。
method: 在受控生物反应器中模拟不同频率的有机负荷冲击，利用宏基因组组装基因组（MAGs）技术、网络分析和机器学习对群落演替进行多维度表征。
result: 实验证实无扰动时竞争者占优，中等频率扰动诱导开拓者策略，而持续高频扰动则筛选出耐逆型菌群，且这些策略在基因组性状分布上具有显著差异。
conclusion: 证明了生活史策略框架能有效捕捉并预测微生物群落的动态变化，为自然及人工生态系统的资源管理提供了跨尺度的理论支撑。
---

## 摘要
理解微生物群落如何响应扰动仍然是生态学中的一个基本问题，对生物多样性、生态系统功能和生物技术具有广泛影响。基于性状的方法通过将生态策略与可测量性状联系起来，为预测群落响应提供了通用规则。尽管诸如竞争者-杂草型-耐逆境型（CSR）模型等生活史策略框架在动植物生态学中已得到确立，但其在微生物群落中的应用仍然有限。在本研究中，我们通过实验测试了在处理合成废水的重复生物反应器中，微生物群落如何随扰动频率梯度发生转变。我们通过在不同频率下将有机负荷率翻倍，设置了从无扰动到持续扰动的六种工况，并利用基因组解析的宏基因组学、16S rRNA 基因测序、生物量定量和出水化学分析监测了 42 天内的变化。通过整合排序分析、网络分析和机器学习，我们识别出了涌现的群落水平生活史策略：无扰动条件下为竞争者主导的群落，中等扰动频率下为杂草型相关策略，而在持续高频（压力型）扰动下则为耐逆境策略。这些策略体现在功能权衡、群落组成转变以及基因组性状分布中。研究采用基于模拟的方法对宏基因组组装基因组进行了 CSR 分类，其结果与在其他微生物生态系统中观察到的模式一致。我们的结果表明，生活史框架能够捕捉不同扰动模式下可预测的微生物动态。该方法为跨尺度联系微生物结构、功能和性状提供了一个统一工具，有助于调和自然及工程生态系统中的生态理论与微生物资源管理。

## Abstract
Understanding how microbial communities respond to disturbance remains a fundamental question in ecology, with broad implications for biodiversity, ecosystem function, and biotechnology. Trait-based approaches offer general rules to predict community responses by linking ecological strategies to measurable traits. Whereas life-history strategy frameworks such as the competitor-ruderal-stress-tolerant (CSR) model are well established in plant and animal ecology, their application to microbial communities has been limited. Here, we experimentally tested how microbial communities shift across a gradient of disturbance frequency in replicated bioreactors treating synthetic wastewater. We applied six conditions by doubling the organic loading rate at different frequencies, from undisturbed to press disturbance, and monitored changes over 42 days using genome-resolved metagenomics, 16S rRNA gene sequencing, biomass quantification, and effluent chemistry. By integrating ordination, network analysis, and machine learning, we identified emergent community-level life-history strategies, with competitor-dominated communities under undisturbed conditions, ruderal-associated strategies at intermediate disturbance frequencies, and stress-tolerant strategies under sustained high-frequency (press) disturbance. These strategies were reflected in functional trade-offs, shifts in community composition, and genomic trait distributions. A simulation-based approach was used to generate a CSR classification of metagenome-assembled genomes, which was consistent with patterns observed in other microbial ecosystems. Our results demonstrate that life-history frameworks can capture predictable microbial dynamics across disturbance regimes. This approach provides a unifying tool for linking microbial structure, function, and traits across scales, helping to reconcile ecological theory with microbial resource management in natural and engineered ecosystems.