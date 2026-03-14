---
title: "Toward AI foundation models for epidemics: Promise, challenges, and paths forward."
title_zh: 迈向流行病 AI 基础模型：前景、挑战与前行路径
authors: "Max S Y Lau, C Jessica E Metcalf, Zewen Liu, Bryan T Grenfell, Wei Jin"
date: 2026-03-31
pdf: "https://pubmed.ncbi.nlm.nih.gov/41824492/"
tags: ["query:pathoai"]
score: 10.0
evidence: 用于流行病科学和传染病动态的基础模型
tldr: 针对传统流行病模型因特定病原体限制而难以应对突发疫情的问题，本文提出构建“流行病基座模型（EFMs）”。该方法主张利用跨病原体、跨人群的异构数据进行预训练，学习传染病动力学的通用规律。这种模型能通过少量数据快速微调，实现对新发疫情的精准预测与干预，为全球公共卫生安全，特别是资源匮乏地区的防疫提供高效、通用的技术支撑。
selection_source: fresh_fetch
motivation: 现有的流行病模型通常针对特定病毒设计，在面对如新冠肺炎等新发突发疫情时，往往因缺乏历史数据而难以快速提供有效的决策支持。
method: 提出通过在大规模、多源异构的流行病监测数据上预训练基座模型，捕捉不同传染病背后的共性动力学特征，并结合微调技术适应特定场景。
result: 明确了非平稳性、数据碎片化及可解释性等核心挑战，并制定了涵盖算法创新、开放数据集建设及跨学科协作的发展路线图。
conclusion: 流行病基座模型有望成为提升全球卫生安全防御能力的通用工具，不仅能加速疫情响应，还能通过建模过程揭示现有监测系统的关键数据缺口。
---

## 摘要
基础模型——在广泛且异构的数据上进行预训练的大型 AI 系统——正在改变科学发现。这些模型（如 GPT、GenCast、AlphaFold）擅长学习可泛化的表示，并能在数据有限的情况下适应新任务。然而，流行病建模尚未经历类似的变革。传统模型仍局限于特定病原体，且在突发疫情期间往往难以快速产生见解，SARS-CoV-2 大流行清楚地说明了这一点。本观点文章探讨了基础模型范式是否可以扩展到流行病科学：我们能否构建一个单一的预训练模型，捕捉跨病原体、人群和环境的传染病动力学共同原理？这种模型可以利用极少的数据微调到新语境中，从而实现更快的预测、推断和响应，这在资源有限的环境中尤为宝贵。我们认为，流行病学见解与现代 AI 日益增长的融合，使得这一目标既紧迫又愈发可行。我们概述了构建流行病基础模型的主要挑战——非平稳性、碎片化的监测数据、多种动力学机制的存在以及对可解释性的需求。随后，我们提出了流行病基础模型的发展路线图，强调了应对这些挑战的算法创新，以及算法之外的进展，包括对开放数据集的投入以及跨学科培训与协作。开发流行病基础模型为加强全球卫生安全提供了一个潜在的变革性机遇，特别是通过提高资源匮乏地区的备灾能力。如果取得成功，它们将作为强大的、可泛化的工具，与现有工作形成互补。构建这些模型的过程本身就具有价值，它将揭示关键的数据缺口，并引导全球监测领域的投资。

## Abstract
Foundation models-large AI systems pretrained on broad, heterogeneous data-are transforming scientific discovery. These models (e.g., GPT, GenCast, AlphaFold) excel at learning generalizable representations and adapting to new tasks with limited data. Yet, epidemic modeling has not experienced a comparable transformation. Traditional models remain pathogen-specific and often struggle to generate rapid insights during emerging outbreaks, as starkly illustrated by the SARS-CoV-2 pandemic. This Perspective asks whether the foundation model paradigm can extend to epidemic science: Can we build a single, pretrained model that captures the shared principles of infectious disease dynamics across pathogens, populations, and settings? Such a model could be fine-tuned to new contexts with minimal data, enabling faster forecasting, inference, and response, especially valuable in resource-limited settings. We argue that the growing convergence of epidemiological insight and modern AI makes this goal both urgent and increasingly plausible. We outline the main challenges in building foundation models for epidemics-nonstationarity, fragmented surveillance data, presence of diverse dynamical regimes, and the need for interpretability. We then propose a roadmap toward epidemic foundation models, emphasizing both algorithmic innovations to address these challenges and progress beyond algorithms, including investments in open datasets and cross-disciplinary training and collaboration. Developing epidemic foundation models offers a potentially transformative opportunity to strengthen global health security, particularly by improving preparedness in underresourced settings. If successful, they will serve as powerful, generalizable tools that complement existing efforts. The process of building these models will itself be valuable, exposing critical data gaps and guiding investments in global surveillance.