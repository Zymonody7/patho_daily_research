---
title: Using Serosurveys to Optimize Surveillance for Zoonotic Pathogens.
title_zh: 利用血清学调查优化人畜共患病原体的监测
authors: "E Clancey, S L Nuismer, S N Seifert"
date: 2026-04-25
pdf: "https://pubmed.ncbi.nlm.nih.gov/42033553/"
tags: ["query:pathoai"]
score: 7.0
evidence: 用于人畜共患病原体监测和溢出预测的统计模型
tldr: 针对人兽共患病病原体在动物宿主中流行时间短、难以通过随机采样捕捉活跃感染的问题，本研究开发了一种通用的数学模型，利用常规收集的血清学监测数据（抗体）来推断病原体流行的峰值时间。通过模拟数据和对非洲草黄食果蝠的实证分析，证明该方法能准确指导野外采样时机，从而提高病原体发现概率并优化溢出风险预警。
selection_source: fresh_fetch
motivation: 由于许多人兽共患病在宿主种群中的活跃感染仅在特定季节出现，传统的随机采样往往难以捕捉到病原体，急需一种能预测流行高峰的监测优化方法。
method: 构建了一个结合宿主出生季节性与免疫动力学的数学模型，通过分析血清阳性率的动态变化来反推病原体活跃感染的峰值时段。
result: 模拟实验证实了该模型能可靠识别流行高峰，且在非洲草黄食果蝠的实际监测数据应用中，成功定位了病原体传播的关键时间窗口。
conclusion: 该研究提供了一种低成本且高效的采样优化方案，适用于具有季节性繁殖特征的多种潜在宿主，有助于提升全球公共卫生对病毒溢出风险的防控能力。
---

## 摘要
人畜共患病原体对人类健康构成重大风险，其向人群的溢出（spillover）会导致慢性疾病和流行病。尽管人畜共患溢出的负担已得到广泛认可，但我们识别哪些动物群体作为主要宿主的能力仍然有限。当宿主群体中的流行率仅在一年中的特定时间达到可检测水平时，这一挑战会进一步加剧。在这些情况下，旨在预测流行高峰时间的统计模型可以指导针对活动性感染的野外采样，或预测溢出风险可能最大的时间。因此，我们开发了一个通用的数学模型，利用常规收集的血清学监测数据来优化对难以发现的病原体的采样。利用模拟数据，我们证明了该方法能够可靠地识别病原体流行预计达到高峰的时间。随后，我们利用先前发表的草黄蝠（Eidolon helvum）监测数据演示了该方法的应用。该方法的通用性和简洁性使其广泛适用于各种推定的宿主物种，在这些物种中，季节性的出生模式会导致周期性但可能短暂的病原体流行脉冲。

## Abstract
Zoonotic pathogens pose significant risk to human health, with spillover into human populations contributing to chronic disease and epidemics. Despite the widely recognized burden of zoonotic spillover, our ability to identify which animal populations serve as primary reservoirs remains incomplete. This challenge is compounded when prevalence in reservoir populations reaches detectable levels only at specific times of year. In these cases, statistical models designed to predict the timing of peak prevalence could guide field sampling for active infections or predict when spillover risk is likely to be greatest. Thus, we develop a general mathematical model that leverages routinely collected serosurveillance data to optimize sampling for elusive pathogens. Using simulated data, we show that our methodology reliably identifies times when pathogen prevalence is expected to peak. Then, we demonstrate an implementation of our method using previously published surveillance data in straw-colored fruit bats (Eidolon helvum). The generality and simplicity of our methodology make it broadly applicable to a wide range of putative reservoir species where seasonal patterns of birth lead to cyclic, but potentially short-lived, pulses of pathogen prevalence.