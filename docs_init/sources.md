# AI + 生信论文源导航

这个页面不负责自动抓取，而是给你一个固定的“找论文入口板”。自动推荐链路目前仍以 `arXiv` 为主，但你的日常追踪可以从这里扩成多源。

## 预印本 / 会议

### arXiv
- `cs.AI` / `cs.LG` / `cs.CL`：通用 AI、模型方法、Agent
- `q-bio.GN` / `q-bio.BM` / `q-bio.QM` / `q-bio.PE`：基因组学、生物分子、定量方法、进化
- `stat.ML`：统计学习与方法学
- 建议检索词：`pathogen genomics`, `bioinformatics`, `metagenomics`, `foundation model`, `single-cell`

### bioRxiv
- 适合跟踪：病原组学、测序流程、微生物组、多组学、实验方法
- 建议重点看：methods、genomics、microbiology、systems biology

### medRxiv
- 适合跟踪：感染病、诊断、临床预测、流行病学、转化研究

### OpenReview
- 适合跟踪：`ICLR`、`NeurIPS`、`ICML`、`ML4H`、`RECOMB workshop`
- 建议关注：biomedical LLM、AI agent、multimodal biology、scientific discovery

## 文献数据库

### PubMed
- 适合：生物医学正式文献、综述、临床研究、病原检测
- 检索建议：
  - `"pathogen genomics" AND machine learning`
  - `"metagenomic pathogen detection" AND deep learning`
  - `"foundation model" AND bioinformatics`

### Europe PMC
- 适合：PubMed + 预印本混合检索，覆盖更宽
- 用法：先做 broad recall，再把高价值论文放回本站追踪

## 重点期刊 / 出版社

### Nature Portfolio
- `Nature Biotechnology`
- `Nature Methods`
- `Nature Machine Intelligence`
- `Nature Communications`
- `Scientific Reports`

### Oxford / Bioinformatics 系
- `Bioinformatics`
- `Nucleic Acids Research`
- `Database`
- `Briefings in Bioinformatics`
- `Genome Biology`
- `BMC Bioinformatics`

## 你这个课题更值得长期盯的关键词

- `pathogen genomics`
- `metagenomics`
- `genomic surveillance`
- `microbial genomics`
- `antimicrobial resistance prediction`
- `biological foundation model`
- `multi-omics integration`
- `single-cell foundation model`
- `biomedical agent`
- `scientific reasoning`

## 建议工作流

1. 用本站默认订阅每天扫 `arXiv` 新论文。
2. 每周从 `PubMed / Europe PMC / bioRxiv` 做一次补充检索。
3. 把真正值得长期追踪的主题沉淀回 `config.yaml` 的 `intent_profiles`。
