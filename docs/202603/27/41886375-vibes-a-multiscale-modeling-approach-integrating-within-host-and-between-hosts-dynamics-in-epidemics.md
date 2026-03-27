---
title: "VIBES: A multiscale modeling approach integrating within-host and between-hosts dynamics in epidemics."
title_zh: VIBES：一种整合流行病中宿主内与宿主间动力学的多尺度建模方法
authors: "Paulo Cesar Ventura, Yong Dam Jeong, Maria Litvinova, Allisandra G Kummer, Shingo Iwami, Hongjie Yu, Stefano Merler, Alessandro Vespignani, Keisuke Ejima, Marco Ajelli"
date: 2026-03-31
pdf: "https://pubmed.ncbi.nlm.nih.gov/41886375/"
tags: ["query:pathoai"]
score: 8.0
evidence: 整合宿主内病毒动力学和群体传播的多尺度建模
tldr: 流行病传播受宿主内病毒动力学和宿主间社交行为共同驱动，但两者影响难以区分。本研究提出 VIBES 框架，将基于患者数据的病毒载量模型与基于社交网络的传播模型相结合。以 SARS-CoV-2 为例，发现社交竞争会缩短代际时间，而隔离措施会提高症状前传播比例。该框架为量化生物与社会因素对疫情的影响提供了机械论工具，有助于评估公共卫生干预效果。
selection_source: fresh_fetch
motivation: 传统的流行病模型往往将生物学特性与社会行为混为一谈，难以精确区分这两者如何独立或共同影响病毒的传播动态。
method: 提出 VIBES 框架，通过整合个体层面的病毒载量演化模型与基于真实社交网络数据的群体传播模型，实现跨尺度的流行病模拟。
result: "研究发现随着病毒传染性增强，宿主间的“感染竞争”使代际时间缩短约 21%，且隔离干预会将症状前传播的比例推高约 30%。"
conclusion: 该多尺度建模方法能够量化生物学与社会因素对疫情演化的具体贡献，为制定精准的公共卫生防控策略提供了理论支撑。
---

## 摘要
传染病的传播是一个由宿主内（生物学）和宿主间（社会学）驱动因素组成的多尺度过程，将两者相互解耦是流行病学中的一个核心挑战。在此，我们介绍了 VIBES，这是一个多尺度建模框架，它将基于患者层面数据的病毒动力学与基于数据驱动的社交接触网络的人群层面传播显式地整合在一起。以 SARS-CoV-2 为案例研究，我们分析了三个突现的流行病学特征，即世代时间（generation time）、序列间隔（serial interval）和症状前传播。首先，我们通过宿主内模型建立了一个纯生物学基准，该基准独立于再生数（R），估计有症状个体的世代时间为 6.3 天，症状前传播比例为 43.1%。随后，利用包含社交接触的完整模型，我们发现世代时间缩短（在 R = 3.0 时为 5.4 天），症状前传播增加（在 R = 3.0 时为 52.8%），从而将社会驱动因素的影响从纯生物学基准中区分出来。我们进一步表明，随着病原体传染性的增加（R 从 1.3 增加到 6），感染者之间的竞争使世代时间和序列间隔分别缩短了高达 21% 和 13%。相反，像隔离这样的社会干预措施会使症状前传播的比例增加约 30%。我们的框架还估计了难以通过实证获得的指标，例如无症状个体的世代时间（在 R = 1.3 时为 5.6 天；95% CI：5.1 至 6.0）。我们的研究结果确立了多尺度建模作为一种强大工具的地位，可用于从机制上量化病原体生物学和人类社会行为如何塑造流行病动力学，并用于评估公共卫生干预措施。

## Abstract
Infectious disease spread is a multiscale process composed of within-host (biological) and between-host (social) drivers and disentangling them from each other is a central challenge in epidemiology. Here, we introduce VIBES, a multiscale modeling framework that explicitly integrates viral dynamics based on patient-level data with population-level transmission on a data-driven network of social contacts. Using SARS-CoV-2 as a case study, we analyze three emergent epidemic properties, namely the generation time, serial interval, and presymptomatic transmission. First, we established a purely biological baseline, thus independent of the reproduction number (R), from the within-host model, estimating a generation time of 6.3 d for symptomatic individuals and 43.1% presymptomatic transmission. Then, using the full model incorporating social contacts, we found a shorter generation time (5.4 d at R = 3.0) and an increase in presymptomatic transmission (52.8% at R = 3.0), disentangling the impact of social drivers from a purely biological baseline. We further show that as pathogen transmissibility increases (R from 1.3 to 6), competition among infectious individuals shortens the generation time and serial interval by up to 21% and 13%, respectively. Conversely, a social intervention, like isolation, increases the proportion of presymptomatic transmission by about 30%. Our framework also estimates metrics that are challenging to obtain empirically, such as the generation time for asymptomatic individuals (5.6 d; 95%CI: 5.1 to 6.0 at R = 1.3). Our findings establish multiscale modeling as a powerful tool for mechanistically quantifying how pathogen biology and human social behavior shape epidemic dynamics as well as for assessing public health interventions.