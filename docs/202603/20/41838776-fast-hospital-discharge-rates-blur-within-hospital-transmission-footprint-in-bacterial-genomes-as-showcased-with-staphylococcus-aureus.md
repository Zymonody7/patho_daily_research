---
title: "Fast hospital discharge rates blur within-hospital 'transmission footprint' in bacterial genomes, as showcased with Staphylococcus aureus."
title_zh: 快速的出院率模糊了细菌基因组中的院内“传播足迹”，以金黄色葡萄球菌为例
authors: "Sanni Översti, Mathilde Boumasmoud, Huldyrch F Günthard, Hugo Sax, Annelies S Zinkernagel, Roger D Kouyos, Denise Kühnert"
date: 2026-03-16
pdf: "https://pubmed.ncbi.nlm.nih.gov/41838776/"
tags: ["query:pathoai"]
score: 9.0
evidence: 细菌传播动力学的贝叶斯系统动力学推断
tldr: 针对细菌病原体突变慢导致医院内传播追踪困难的问题，本研究通过随机模型模拟金黄色葡萄球菌在医院与社区间的动态演化。研究发现，当出院率高于院内传播率时，仅凭医院样本的基因组数据会严重低估院内传播强度。结果表明，准确评估院内感染风险必须整合社区样本或外部传播数据，为优化公共卫生监测策略提供了理论依据。
selection_source: fresh_fetch
motivation: 细菌突变缓慢且患者出院频繁，使得仅通过医院内的基因组数据难以准确推断病原体的真实传播路径。
method: 利用随机模型模拟连接医院与社区的金黄色葡萄球菌爆发过程，并结合贝叶斯系统发育动力学方法对合成基因组序列进行推断。
result: 当出院速度超过院内传播速度时，若缺乏社区样本，模型会显著低估院内传播率，甚至将社区传播误判为院内爆发。
conclusion: 在利用基因组数据评估院内感染时，必须考虑社区背景或引入外部传播参数，否则单一的医院采样数据会导致错误的防控决策。
---

## 摘要
细菌病原体相对缓慢的突变率对细菌爆发的系统动力学分析造成了严重限制。然而，全基因组测序可能能够准确推断医疗机构中的细菌传播动态。我们使用一个包含医院和社区室（通过患者入院和出院连接）的随机模型，模拟了金黄色葡萄球菌谱系的流行病学动态。我们生成了合成基因组序列，并对每次模拟爆发中的部分样本进行了贝叶斯系统动力学推断。当从两个室都获取样本时，如果医院传播率（[Formula: see text]）与出院率处于同一数量级，则可以准确估算医院传播率和社区传播率（[Formula: see text]）。如果 [Formula: see text] 显著低于出院率，则对院内传播动态进行稳健的定量分析将具有挑战性。当 [Formula: see text] 时，排除社区样本会导致对 [Formula: see text] 的显著低估。当传播由“社区驱动”但采样仅限于医院病例时，如果已知医院采样比例，则估算值更接近真实的 [Formula: see text]；否则，[Formula: see text] 的估算值将反映社区内的传播动态。在使用基因组数据估算医疗机构中的细菌传播率时，必须考虑周围社区。由于快速的出院率，许多与院内爆发相关的感染将无法在医院内观察到。在缺乏可用的社区基因组数据时，应纳入来自公开数据的社区传播率替代估算值。仅根据院内基因组得出的传播率估算值需要谨慎解释。

## Abstract
The relatively slow mutation rates of bacterial pathogens impose severe limitations on phylodynamic analysis of bacterial outbreaks. However, whole-genome sequencing may enable accurate inference of bacterial transmission dynamics in health-care settings. We simulated the epidemic dynamics of a Staphylococcus aureus lineage using a stochastic model with a hospital and community compartment connected by patient admission and discharge. We generated synthetic genomic sequences and performed Bayesian phylodynamic inference on a proportion of samples from each simulated outbreak. When samples are obtained from both compartments, hospital transmission rate ([Formula: see text]) and community transmission rate ([Formula: see text]) are accurately estimated, if [Formula: see text] is on the same scale as the discharge rate. If [Formula: see text] is substantially lower than the discharge rate, a robust quantification of within-hospital transmission dynamics is challenging. Excluding samples from the community resulted in a notable underestimation of [Formula: see text] when [Formula: see text]. When transmission was 'community-driven', but sampling was restricted to hospital cases only, estimates are closer to the true [Formula: see text], if hospital sampling proportion is known. Otherwise, [Formula: see text] estimates reflected the transmission dynamics within the community. When using genomic data to estimate bacterial transmission rates in a health-care setting, it is essential to take into account the surrounding community. Many infections related to nosocomial outbreaks will not be observed within the hospital due to fast discharge rates. In the absence of usable genomic data from the community, alternative estimates of community transmission rates from publicly available data should be incorporated. Transmission rate estimates from nosocomial genomes alone need to be interpreted with care.