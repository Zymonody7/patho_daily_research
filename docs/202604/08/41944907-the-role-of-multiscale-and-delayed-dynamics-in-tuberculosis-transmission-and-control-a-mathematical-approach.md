---
title: "The role of multiscale and delayed dynamics in tuberculosis Transmission and control: a mathematical approach."
title_zh: 多尺度和时滞动力学在结核病传播与控制中的作用：一种数学方法
authors: "Li W, Wang Y, Jin Z., Wei Li, Yi Wang, Zhen Jin"
date: 2026-04-07
pdf: "https://pubmed.ncbi.nlm.nih.gov/41944907/"
tags: ["query:pathoai"]
score: 6.0
evidence: 结核病传播与控制的数学建模
tldr: 针对结核病（TB）传播中宿主内免疫反应与环境病原体存活的复杂交互问题，本文构建了一个多尺度数学模型，整合了人际传播与环境传播路径。通过分析快慢动力学系统，揭示了即使基本再生数小于1也可能存在地方病平衡点的后向分支现象。随后利用脉冲时滞微分方程模拟实际给药方案，确定了疾病消除的临界参数，并证实化疗在控制结核病中起主导作用，而免疫治疗仅起辅助作用。
selection_source: fresh_fetch
motivation: 结核分枝杆菌在环境中存活时间长且宿主内载量影响传染性，需研究跨尺度动力学对疫情控制的影响。
method: 建立了一个耦合宿主内免疫交互与人群/环境传播路径的多尺度模型，并引入脉冲时滞微分方程来模拟实际的间歇性给药治疗过程。
result: 发现系统存在后向分支现象，意味着传统的 $R_0 < 1$ 阈值在特定条件下不足以消除疾病，且数值模拟显示病原体释放率对传播风险的影响远大于免疫速率。
conclusion: 研究强调了环境传播不可忽视，并从数学角度证明了化疗是结核病控制的核心手段，而免疫疗法应作为辅助手段。
---

## 摘要
结核病（TB）在人群中的传播取决于个体的传染性，而传染性又由体内结核分枝杆菌（Mtb）的浓度决定。此外，Mtb 对干燥、寒冷、酸性和碱性环境具有抵抗力，并能在酸碱环境中存活 4-5 年。环境中的 Mtb 在结核病传播中起着重要作用，不应被忽视。为了研究病原体、宿主和环境之间的流行病学关系，我们首先建立了一个多尺度结核病模型，该模型包含多种传播途径（人与人之间以及环境与人之间），并将宿主体内 Mtb 与免疫反应的相互作用与人群中的结核病传播联系起来。我们全面分析了快系统、慢系统和全系统的动力学性质。分析结果表明，将宿主体内的细菌过程与宿主间的传播机制耦合，会引发多种复杂的行为，包括前向分支和后向分支现象。这意味着从流行病学或免疫学角度常规用于控制结核病感染或消除 Mtb 的阈值在特定条件下可能会失效；也就是说，即使基本再生数 R₀ 小于 1，系统中仍可能存在地方病平衡点。其次，从微观治疗的角度，我们建立了一个脉冲时滞微分方程来刻画结核病的实际给药方案。基本再生数 R₀' 被定义为线性积分算子的谱半径。随后，我们证明了 R₀' 是决定模型持久性的关键参数。更准确地说，如果 R₀' < 1，则无病周期解是全局吸引的；如果 R₀' > 1，则疾病是均匀持久的。最后，我们采用数值方法阐明了人群传播动力学与病原体动力学之间的相互作用。具体而言，全系统的基本再生数 R₀ 随着 Mtb 释放率的增加而迅速增大，而随着免疫率的增加，其变化相对较慢。这些结果突出了化疗的主导作用，而免疫疗法仅起辅助作用。

## Abstract
Transmission of tuberculosis (TB) among human population depends on an individual's infectiousness, which is further determined by the concentration of Mycobacterium tuberculosis (Mtb) in the body. Additionally, Mtb is resistant to dryness, cold, acidic, and alkaline environments and can survive in acidic and alkaline environments for 4-5 years. Mtb in the environment plays a significant role in TB transmission and should not be overlooked. To investigate the epidemiologic relationships among pathogens, hosts, and the environment, we first develop a multiscale TB model that includes multiple transmission routes (human-to-human and environment-to-human) and links Mtb-immune response interactions to TB transmission in population. We comprehensively analyze the dynamic properties of the fast system, slow system, and full system. Analysis results reveal that coupling bacterial processes within-host with transmission mechanisms between-host can trigger diverse complex behaviors, including both forward and backward bifurcation phenomena. This implies that thresholds routinely used to control TB infection or eliminate Mtb from an epidemiological or immunological perspective may fail under specific conditions; that is, even if the basic reproduction number R 0  is less than 1, endemic equilibria may still exist in the system. Second, from a microtherapeutic point of view, we establish an impulsive time-delayed differential equation to characterize the actual medication regimen for TB. The basic reproduction number R 0 '  is defined as the spectral radius of a linear integral operator. Then, we show that R 0 '  is a critical parameter that determines the persistence of the model. More precisely, if  R 0 ' < 1  , the disease-free periodic solution is globally attractive; if  R 0 ' > 1  , the disease is uniformly persistent. Finally, we employ numerical methods to elucidate the interactions between population transmission dynamics and pathogen dynamics. Specifically, the basic reproduction number R 0  of the full system increases rapidly with the rise in Mtb release rate, while its change is relatively slower with an increase in the immune rate. These results highlight the dominant role of chemotherapy, with immunotherapy playing only a supporting role.