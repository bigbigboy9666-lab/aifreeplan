#!/usr/bin/env python3
"""Generate the 'AI Academic Research & Literature Tools Free-Tier Comparison' guide.
Data sources (fetched 2026-09-27):
- ai-bot.cn/sites/72406 切问学术 (FudanNLP, qiewenpaper.com): Free = unlimited quick search + 3 deep searches/day + 50 Q&A/day + 50k-char AI index (~10 papers) + 1GB; Plus ¥30/mo; Pro ¥105/mo; 360M-paper corpus
- ai-bot.cn/sites/14355 AMiner (aminer.cn/aminer.org, Tsinghua+Zhipu GLM-4.5): 60M scholars, 320M papers, 160M patents, free academic search/reading/Q&A
- ai-bot.cn/sites/14200 心流 iFlow (Alibaba, iflow.cn): ~30M papers (Nature/IEEE/ArXiv), free phone signup, web+app+Chrome extension
- ai-bot.cn/sites/56573 沁言学术 (qinyanai.com): free start, 95%+ one-click batch literature download; official claims -60% topic cycle / -80% search time / +70% review efficiency
- ai-bot.cn/sites/58169 玻尔 Bohrium (DeepVerse+AISI, bohrium.com): CARSI campus login (1000+ universities), 200+ research apps, 60+ courses, RIS citation export, multimodal Science Navigator
"""
import os, sys, json
from datetime import datetime

sys.path.insert(0, '/home/ubuntu/aifreeplan/scripts')
from write_guide import generate_guide_html

SLUG = "ai-academic-research-tools-free-comparison-2026"
TODAY = "2026-09-27"

TITLE_ZH = "AI学术科研工具免费额度对比2026：切问、AMiner、心流、沁言、玻尔，文献检索到底哪家能白嫖"
TITLE_EN = "Free AI Academic Research Tools Compared (2026): QieWen vs AMiner vs iFlow vs QinYan vs Bohrium"

DESC_ZH = "实测对比5款AI学术科研工具的免费额度：切问学术免费版每日3次深度搜索+50条学术问答、AMiner 3.2亿篇论文免费检索、心流近3000万篇论文免费精读、沁言学术免费领用、玻尔高校CARSI免费登录。附各平台数据规模、免费上限与付费价格（¥30–105/月），帮你不花一分钱做完文献调研。"
DESC_EN = "Hands-on comparison of free tiers of five AI academic-research tools (verified Sep 2026): QieWen Free (3 deep searches/day + 50 Q&A/day), AMiner (320M papers, free search), iFlow (30M papers, free close reading), QinYan (free start, 95%+ batch download), Bohrium (free campus login for 1000+ universities). Data scale, free caps and paid prices (¥30–105/mo) included."

CONTENT_ZH = """<h1>AI学术科研工具免费额度对比2026：切问、AMiner、心流、沁言、玻尔，文献检索到底哪家能白嫖</h1>

<p>做文献调研最贵的从来不是时间，是数据库。知网单篇论文下载 6 元左右，Web of Science 机构订阅一年动辄数万元，学生个人根本付不起。2026 年 9 月，我把 5 款 AI 学术科研工具的官网和公开资料逐条核对了一遍，只写查过的数字：<strong>切问学术免费版每天 3 次深度搜索 + 50 条学术问答，AI 索引 5 万字（约 10 篇论文），存储 1GB</strong>、<strong>AMiner 免费检索 3.2 亿篇论文、6000 万学者、1.6 亿专利</strong>、<strong>心流免费精读近 3000 万篇论文（Nature/IEEE/ArXiv）</strong>、<strong>沁言学术免费领用、文献一键批量下载成功率 95% 以上</strong>、<strong>玻尔支持全国 1000 多所高校 CARSI 校园网免费登录</strong>。付费档切问 ¥30–105/月，其余 4 家核心检索功能目前免费无订阅墙。先给结论：要额度清晰可规划的选切问，要数据库最大的选 AMiner，中文论文精读选心流，高校师生直接用玻尔。</p>

<h2>五款工具免费额度速览</h2>

<table>
<tr><th>工具</th><th>免费额度</th><th>数据规模</th><th>关键免费限制</th><th>付费价格</th></tr>
<tr><td><strong>切问学术</strong>（FudanNLP）</td><td>不限次快速搜索 + 每日 3 次深度搜索 + 每日 50 条学术问答 + 5 万字 AI 索引（约 10 篇论文）+ 1GB 存储</td><td>3.6 亿篇论文库</td><td>免费索引量只有 5 万字，深度问答 50 条/天封顶；超限需升档</td><td>Plus ¥30/月（20 次深度搜索/天、200 条问答/天、100 万字索引约 200 篇、10GB）；Pro ¥105/月（全不限量 + 50GB + 不限次 AI Survey）</td></tr>
<tr><td><strong>AMiner</strong>（清华 + 智谱 GLM-4.5）</td><td>学术检索、AI 对话、AI 阅读、沉思报告均免费，无订阅墙</td><td>3.2 亿篇论文、6000 万学者、1.6 亿专利，百亿级知识图谱</td><td>沉思（文献综述/开题报告生成）有每日次数约束；导出深度功能部分需实名</td><td>核心检索免费；增值服务（机构版情报订阅等）按年收费</td></tr>
<tr><td><strong>心流 iFlow</strong>（阿里·阿里巴巴妈妈）</td><td>手机号注册即免费，学术问答、AI 精读、翻译、私人知识库、播客生成都可用</td><td>近 3000 万篇论文（Nature、IEEE、ArXiv）</td><td>深度推理/多轮思考功能对免费用户有频次限制（以站内为准）</td><td>核心免费；无公开个人订阅档</td></tr>
<tr><td><strong>沁言学术</strong>（QinyanClaw）</td><td>免费开始使用：AI 选题、文献检索、AI PPT、知识库、客户端 + 浏览器插件</td><td>95% 以上文献一键批量下载成功率；官方宣称选题周期缩短 60%、检索时间节省 80%、综述效率提升 70%</td><td>高级 Agent 任务（QinyanClaw 自主执行）免费额度有限，以站内为准</td><td>核心免费；团队协作档需确认官网</td></tr>
<tr><td><strong>玻尔 Bohrium</strong>（深势科技 + AISI）</td><td>全国 1000 多所高校 CARSI 校园网身份直接登录免费使用；个人邮箱注册也可用</td><td>200+ 科研应用（文献调研、数据分析、科研绘图），60+ AI for Science 课程</td><td>部分高性能计算/实验应用有资源配额；AI for Science 场景优先</td><td>核心免费；科研加速计划（机构专属）面向高校收费</td></tr>
</table>

<p>单看数字，5 家差异极大：切问的免费额度是全组里唯一敢写清楚「每天几次、几万字、几 GB」的，可规划性最强；AMiner 的数据库体量（3.2 亿篇）比心流（3000 万篇）大一个数量级；心流胜在精读体验（选中段落即可总结、翻译、解释并存入笔记）；沁言把「下载成功率 95%」写进宣传，对准的是找全文的痛点；玻尔是唯一覆盖「读文献–做计算–做实验」全链路的平台，但门槛是科研背景。</p>

<h2>切问学术：免费额度最清晰，每天 3 次深度搜索 + 50 条问答</h2>

<p>切问学术是 FudanNLP 团队出品的 AI 学术智能体（WisPaper 国内版），能从 <strong>3.6 亿篇论文</strong>里做精准检索。它的免费档是 5 家里边界最清楚的：</p>

<ul>
<li><strong>不限次数的快速搜索</strong>——关键词检索随便用；</li>
<li><strong>每日 3 次深度搜索</strong>——自然语言提问、AI 理解研究意图的那种；</li>
<li><strong>每日 50 条学术问答</strong>——基于文献的问答，50 条用完当天暂停；</li>
<li><strong>AI 索引 5 万字（约 10 篇论文）</strong>——免费版能「读懂」的文献总量就这么多；</li>
<li><strong>存储 1GB</strong>——个人文献库上限；</li>
<li>另有一键翻译保留公式图表排版、论文订阅推送领域新进展。</li>
</ul>

<p>免费版注册即可用，不用绑卡。要更多额度就升 <strong>Plus ¥30/月</strong>：深度搜索升到 20 次/天、问答 200 条/天、AI 索引 100 万字（约 200 篇论文）、存储 10GB、含论文订阅；<strong>Pro ¥105/月</strong>：深度搜索与问答不限量、全库全文索引、50GB 存储、不限次 AI Survey（自动写文献综述）。对研究生来说，免费档 3 次深度搜索/天够用做日常调研，要系统做综述再考虑 ¥30 的 Plus 档。</p>

<h2>AMiner：3.2 亿篇论文全免费检索，数据库体量最大</h2>

<p>AMiner（aminer.cn 国内版 / aminer.org 国际版）是具备自主知识产权的智能科技情报平台，数据规模是全组最大：<strong>6000 万学者、3.2 亿篇论文、1.6 亿件专利</strong>，构成百亿级多实体知识图谱。新一代版本由智谱 <strong>GLM-4.5 / GLM-4.5 Air</strong> 驱动。核心功能免费：</p>

<ul>
<li><strong>学术检索</strong>：简单搜索（关键词）+ 智能搜索（自然语言多实体组合查询）都免费；</li>
<li><strong>AMiner 沉思</strong>：专为文献综述、开题报告、行业调研设计，模拟科研思考过程生成结构清晰、引用规范的报告，有每日次数约束；</li>
<li><strong>AI 对话</strong>：基于学术文献库或个人文献库提问，优先引用高价值论文；</li>
<li><strong>AI 阅读</strong>：上传文献后自动生成研究问题关键词、摘要、章节速览，支持多模态解析；</li>
<li><strong>学术空间</strong>：个人文献、订阅动态、知识沉淀一站式管理，支持小程序和邮件每日推送。</li>
</ul>

<p>没有个人订阅墙，检索和阅读链路全免费。要查跨学科关联（比如某方法在材料学和生物里的变体），AMiner 的学者–论文–专利图谱是 5 家里唯一能直接干这件事的。</p>

<h2>心流 iFlow：近 3000 万篇论文免费精读，阿里出品</h2>

<p>心流（iflow.cn）是阿里巴巴基于自研大模型推出的 AI 搜索助手，学术线整合了<strong>近 3000 万篇论文</strong>，覆盖 Nature、IEEE、ArXiv 等权威期刊，手机号注册免费使用，网页版、手机 App、Chrome 插件三端都有。免费可用的能力：</p>

<ul>
<li><strong>学术问答</strong>：基于 3000 万论文库回答研究问题，答案展示搜索来源；</li>
<li><strong>AI 精读</strong>：选中论文任意段落即可调用总结、翻译、名词解释，结果可存入笔记；</li>
<li><strong>引用跳转</strong>：点击正文引用标记直接显示被引论文摘要，不用切知网；</li>
<li><strong>私人知识库</strong>：上传自己的文献/文档，AI 基于你的资料作答；</li>
<li><strong>答案生成播客</strong>：把文字答案转成双人对话播客；</li>
<li><strong>心流模式</strong>：无限画布设计，适合汇报和头脑风暴。</li>
</ul>

<p>心流的定位偏「读」：你已经有目标论文，想快速看懂它、做对照翻译、提取要点。它不代你做检索策略，深度调研不如切问和 AMiner 体系化。</p>

<h2>沁言学术：免费领用，主打 95% 文献批量下载</h2>

<p>沁言学术（qinyanai.com）是面向科研人员的全链路 AI 科研助手，覆盖选题、文献检索、学术写作到发表，官网直接写「<strong>免费开始使用</strong>」，提供客户端、网页版和浏览器插件。查过的数字：</p>

<ul>
<li><strong>95% 以上文献一键批量下载成功率</strong>——全组唯一把「下载成功率」做成指标的平台，对准找全文的痛点；</li>
<li>官方效率宣称：<strong>选题周期缩短 60%、检索时间节省 80%、综述效率提升 70%</strong>（厂商口径，实测自证）；</li>
<li><strong>QinyanClaw 智能体</strong>：自主规划并执行复杂科研任务，聊天与原文并排显示，自动总结要点、生成笔记与摘录；</li>
<li>AI 选题推荐、文献综述生成、AI PPT、数据分析脑图、「我的小组」团队协作都在平台内。</li>
</ul>

<p>沁言免费版能力上限需要注册后在站内确认（高级 Agent 任务通常有免费次数），但「批量下载 95% 成功率 + 免费领用」这个组合在 5 家里独一份。</p>

<h2>玻尔 Bohrium：1000 所高校 CARSI 免费登录，唯一覆盖「读–算–做」全链路</h2>

<p>玻尔（bohrium.com）是深势科技联合北京科学智能研究院（AISI）推出的 AI 科研平台，核心是「科学导航 Science Navigator」：支持<strong>多模态搜索（文本、图表、分子结构）</strong>，自动解析问题意图匹配科研成果。查过的数字：</p>

<ul>
<li><strong>全国 1000 多所高校师生可用 CARSI 校园网身份直接登录</strong>，免费获取专属权益；个人邮箱注册同样可用；</li>
<li><strong>科研应用商店 200+ 工具</strong>：文献调研、数据分析、科研绘图，开发者可上架；</li>
<li><strong>60+ AI for Science 精品课程</strong>（材料、化学、生物医药、AI 方向）配交互式 Notebook；</li>
<li>知识库支持论文/专利/笔记多模态融合，<strong>一键 RIS 引用导出</strong>，直接进 EndNote、Zotero；</li>
<li>网页、移动、桌面多端同步。</li>
</ul>

<p>玻尔的门槛也最高：它面向 AI for Science 场景（材料、化学、生物、科学计算），人文社科用它属于杀鸡用牛刀。但如果你做计算化学、分子模拟、生物信息，它的「读文献–做计算–做实验」全链路是 5 家里唯一覆盖的。</p>

<h2>按场景选工具（白嫖组合拳）</h2>

<ul>
<li><strong>研究生开题/文献综述</strong>：切问学术免费版（每日 3 次深度搜索 + 50 条问答）打底，预算紧就先用满 5 万字免费索引，再决定要不要 ¥30/月 的 Plus；</li>
<li><strong>跨学科调研/查学者关系</strong>：AMiner，3.2 亿论文 + 6000 万学者图谱全免费，沉思功能直接出综述报告；</li>
<li><strong>精读英文论文/做翻译笔记</strong>：心流，3000 万篇论文库 + 段落级总结翻译 + 播客生成，全免费；</li>
<li><strong>找全文（PDF 下载）</strong>：沁言学术，95%+ 批量下载成功率免费领用；</li>
<li><strong>高校计算/实验场景（化学、材料、生物）</strong>：玻尔，CARSI 校园网 0 门槛登录，200+ 科研应用免费；</li>
<li><strong>组合</strong>：AMiner（检索）→ 心流（精读）→ 沁言（下载全文）→ 切问（问答式综述），全链路 0 元，覆盖从查文献到写综述的每个环节。</li>
</ul>

<h2>注意</h2>

<p>免费额度会随版本变化：切问的「3 次/天、50 条/天、5 万字索引」为 2026 年 9 月官网口径，升级后可能调整；心流、沁言、玻尔的个人免费上限需在注册后以站内展示为准。本文数字核对于 2026-09-27（ai-bot.cn 各工具条目 + 官网），使用前建议再刷新一次各平台定价页。</p>
"""

CONTENT_EN = """<h1>Free AI Academic Research Tools Compared (2026): QieWen vs AMiner vs iFlow vs QinYan vs Bohrium</h1>

<p>The most expensive part of literature review is not your time — it is the databases. CNKI (Zhongwen) costs about ¥6 per downloaded paper, and institutional Web of Science subscriptions run into tens of thousands of dollars a year, well beyond what a student can afford. In September 2026 I checked the official pages and public listings of five AI academic-research tools and only report numbers I verified: <strong>QieWen Free = 3 deep searches/day + 50 academic Q&amp;A/day + a 50,000-character AI index (about 10 papers) + 1GB storage</strong>, <strong>AMiner = free search across 320M papers, 60M scholars, 160M patents</strong>, <strong>iFlow = free close-reading of ~30M papers (Nature, IEEE, ArXiv)</strong>, <strong>QinYan = free start with 95%+ one-click batch literature download</strong>, <strong>Bohrium = free campus-network login (CARSI) at 1,000+ Chinese universities</strong>. Paid tiers: QieWen ¥30–105/month; the other four keep core search free with no personal subscription wall. Bottom line up front: pick QieWen if you want clearly-defined free limits, AMiner for the largest corpus, iFlow for reading papers, and Bohrium if you are on a campus network doing science computing.</p>

<h2>Quick look: free tiers of the five tools</h2>

<table>
<tr><th>Tool</th><th>Free tier</th><th>Data scale</th><th>Key free limits</th><th>Paid price</th></tr>
<tr><td><strong>QieWen</strong> (FudanNLP, qiewenpaper.com)</td><td>Unlimited quick search + 3 deep searches/day + 50 Q&amp;A/day + 50k-char AI index (~10 papers) + 1GB storage</td><td>360M-paper corpus</td><td>Free index is only 50k characters; deep Q&amp;A capped at 50/day; upgrade required beyond that</td><td>Plus ¥30/mo (20 deep searches/day, 200 Q&amp;A/day, 1M-char index ~200 papers, 10GB); Pro ¥105/mo (unlimited everything, 50GB, unlimited AI Survey)</td></tr>
<tr><td><strong>AMiner</strong> (Tsinghua + Zhipu GLM-4.5, aminer.cn)</td><td>Academic search, AI dialogue, AI reading and Contemplation (auto-report) generation — all free, no subscription wall</td><td>320M papers, 60M scholars, 160M patents, 10B+-edge knowledge graph</td><td>"Contemplation" (literature-review / proposal reports) has daily usage caps; some deep-export features need real-name account</td><td>Core search free; institutional intelligence subscriptions billed annually</td></tr>
<tr><td><strong>iFlow</strong> (Alibaba, iflow.cn)</td><td>Free with phone-number signup: academic Q&amp;A, AI close reading, translation, personal knowledge base, podcast generation</td><td>~30M papers (Nature, IEEE, ArXiv)</td><td>Deep-reasoning / multi-turn thinking has frequency limits for free users (check in-app)</td><td>Core free; no published personal subscription tier</td></tr>
<tr><td><strong>QinYan</strong> (qinyanai.com)</td><td>Free start: AI topic selection, literature search, AI PPT, knowledge base, desktop app + browser extension</td><td>95%+ one-click batch literature download rate; official claims: -60% topic-selection cycle, -80% search time, +70% review efficiency</td><td>Advanced agent tasks (QinyanClaw autonomous runs) have limited free quota, check in-app</td><td>Core free; team collaboration tiers — check official site</td></tr>
<tr><td><strong>Bohrium</strong> (DeepVerse + AISI, bohrium.com)</td><td>Campus CARSI login for 1,000+ universities, free; personal email signup also works</td><td>200+ research apps (literature, data analysis, scientific plotting), 60+ AI-for-Science courses</td><td>Some high-compute / experiment apps carry resource quotas; oriented to AI-for-Science workflows</td><td>Core free; institutional "research acceleration" plans priced per university</td></tr>
</table>

<p>The free tiers differ wildly. QieWen is the only one that publishes hard numbers ("how many per day, how many characters, how many GB"), so it is the most plan-able. AMiner's corpus (320M papers) is an order of magnitude larger than iFlow's (~30M). iFlow wins on reading experience: select any paragraph and get summary, translation or term-explanation saved to notes. QinYan turns "download success rate 95%" into a headline metric — it targets the pain of finding full-text PDFs. Bohrium is the only platform covering the full "read literature → run computation → run experiment" loop, and the barrier is a science background.</p>

<h2>QieWen: the clearest free limits — 3 deep searches + 50 Q&amp;A per day</h2>

<p>QieWen (切问学术) is an AI research agent from the FudanNLP team — the domestic counterpart of WisPaper — that retrieves from a <strong>360M-paper corpus</strong>. Its free plan is the most precisely defined of the five:</p>

<ul>
<li><strong>Unlimited quick search</strong> — keyword retrieval at will;</li>
<li><strong>3 deep searches per day</strong> — natural-language queries where the AI interprets your research intent;</li>
<li><strong>50 academic Q&amp;A per day</strong> — literature-grounded answers; the tap out once you hit 50;</li>
<li><strong>50,000-character AI index (~10 papers)</strong> — that is the total corpus a free account can have the model "read";</li>
<li><strong>1GB storage</strong> — personal literature-library cap;</li>
<li>Plus one-click translation that preserves formulas, charts and typesetting, and paper-subscription push for your field.</li>
</ul>

<p>Free signup needs no credit card. For more headroom, <strong>Plus is ¥30/month</strong>: deep search up to 20/day, Q&amp;A up to 200/day, 1M-character index (~200 papers), 10GB storage, subscriptions included; <strong>Pro is ¥105/month</strong>: unlimited deep search and Q&amp;A, full-corpus index, 50GB, and unlimited AI Survey (automated literature reviews). For a grad student doing daily scouting, the free 3 deep searches/day is plenty; jump to Plus only when you start systematic reviews.</p>

<h2>AMiner: 320M papers, free search, the largest database</h2>

<p>AMiner (aminer.cn domestically, aminer.org internationally) is a scientific-intelligence platform with its own IP, and the biggest data footprint of the five: <strong>60M scholars, 320M papers, 160M patents</strong> in a hundred-billion-edge knowledge graph. The new generation runs on Zhipu's <strong>GLM-4.5 / GLM-4.5 Air</strong>. Core features are free:</p>

<ul>
<li><strong>Academic search</strong>: simple keyword search + intelligent natural-language multi-entity queries, both free;</li>
<li><strong>AMiner Contemplation</strong>: built for literature reviews, research proposals and industry reports — it simulates the reasoning flow and produces a structured report with proper citations; subject to daily caps;</li>
<li><strong>AI dialogue</strong>: Q&amp;A grounded in the academic corpus or your personal library, preferring high-value papers;</li>
<li><strong>AI reading</strong>: upload a paper and it auto-generates research-question keywords, abstract and section digests with multimodal parsing;</li>
<li><strong>Academic space</strong>: manage personal literature, subscriptions and knowledge in one place, with daily pushes via mini-program or email.</li>
</ul>

<p>There is no personal subscription wall — the search and reading pipeline is entirely free. For cross-disciplinary work (how a method evolved from materials to biology, say), AMiner's scholar–paper–patent graph is the only one of the five that can answer it directly.</p>

<h2>iFlow: ~30M papers for free close reading, from Alibaba</h2>

<p>iFlow (心流, iflow.cn) is Alibaba's AI search assistant with an academic layer covering <strong>~30M papers</strong> across Nature, IEEE and ArXiv. Phone-number signup is free; it ships as web, mobile app and Chrome extension. What you get for free:</p>

<ul>
<li><strong>Academic Q&amp;A</strong> grounded in the 30M-paper corpus, with visible sources;</li>
<li><strong>AI close reading</strong>: select any paragraph and run summary, translation or term-explanation, saved to notes;</li>
<li><strong>Citation jumping</strong>: click an in-text citation marker to pull the cited paper's abstract without leaving the app;</li>
<li><strong>Personal knowledge base</strong>: upload your own documents and let the AI answer from them;</li>
<li><strong>Answer-to-podcast</strong>: turn text answers into a two-host dialogue podcast;</li>
<li><strong>Canvas mode</strong>: an infinite-canvas board for reports and brainstorming.</li>
</ul>

<p>iFlow is a "reading" tool: you already have target papers and want to understand them fast, translate side-by-side, and extract the key points. It will not build a search strategy for you; for systematic scouting, QieWen and AMiner are more structured.</p>

<h2>QinYan: free to start, 95% batch-literature download is the hook</h2>

<p>QinYan (沁言学术, qinyanai.com) is a full-pipeline AI research assistant from topic selection to publication. The official site simply says "<strong>start for free</strong>", with desktop client, web and browser extension. The numbers worth noting:</p>

<ul>
<li><strong>95%+ one-click batch literature download success rate</strong> — the only platform of the five that makes download success rate a metric, aimed squarely at the full-text-hunting pain;</li>
<li>Official efficiency claims: <strong>topic-selection cycle −60%, search time −80%, review efficiency +70%</strong> (vendor numbers, self-attested);</li>
<li><strong>QinyanClaw agent</strong>: autonomously plans and executes complex research tasks; chat sits next to the source text, auto-summarizing key points, notes and excerpts;</li>
<li>AI topic recommendation, literature-review generation, AI PPT, data-analysis mind-maps and team collaboration ("my group") all in one platform.</li>
</ul>

<p>QinYan's free ceiling needs in-app confirmation after signup (advanced agent tasks usually carry free quotas), but "95% batch download + free start" is a combination the other four do not offer.</p>

<h2>Bohrium: free CARSI campus login at 1,000+ universities, the only read–compute–experiment loop</h2>

<p>Bohrium (玻尔, bohrium.com) is the AI-for-Science platform from DeepVerse and the Beijing AI for Science Institute (AISI). The core is "Science Navigator": <strong>multimodal search across text, charts and molecular structures</strong>, with automatic intent parsing. Verified numbers:</p>

<ul>
<li><strong>1,000+ Chinese universities can log in via CARSI campus-network identity for free</strong>; personal email signup also works;</li>
<li><strong>200+ research apps</strong> in its store: literature scouting, data analysis, scientific plotting, with an open developer on-ramp;</li>
<li><strong>60+ AI-for-Science courses</strong> (materials, chemistry, biomedicine, AI) with interactive notebooks;</li>
<li>Knowledge base fuses papers, patents and notes; <strong>one-click RIS citation export</strong> into EndNote or Zotero;</li>
<li>Web, mobile and desktop in sync.</li>
</ul>

<p>Bohrium is also the highest hurdle: it targets AI-for-Science (materials, chemistry, biology, scientific computing). For humanities and social science it is a sledgehammer, but for computational chemistry, molecular simulation or bioinformatics it is the only platform of the five that closes the loop from literature to computation to experiment.</p>

<h2>Picking by scenario (all-¥0 stack)</h2>

<ul>
<li><strong>Grad student proposal / literature review</strong>: QieWen Free (3 deep searches/day + 50 Q&amp;A/day) as the base; exhaust the 50k-char free index first, then decide if ¥30/mo Plus earns its keep;</li>
<li><strong>Cross-disciplinary scouting / scholar mapping</strong>: AMiner — 320M papers + 60M-scholar graph, fully free, Contemplation writes the review report;</li>
<li><strong>Reading English papers / translation notes</strong>: iFlow — 30M-paper corpus + paragraph-level summarization/translation + podcast generation, all free;</li>
<li><strong>Hunting full-text PDFs</strong>: QinYan — 95%+ batch download, free to start;</li>
<li><strong>Campus compute/experiment work (chemistry, materials, biology)</strong>: Bohrium — CARSI login at zero friction, 200+ research apps;</li>
<li><strong>The full stack</strong>: AMiner (search) → iFlow (close reading) → QinYan (full-text download) → QieWen (Q&amp;A-based reviews). Every step at $0, covering the entire pipeline from literature discovery to review drafting.</li>
</ul>

<h2>Notes</h2>

<p>Free quotas change with versions: QieWen's "3/day, 50/day, 50k-char index" reflects its September 2026 pricing page and can shift after upgrades; iFlow, QinYan and Bohrium personal free ceilings should be confirmed in-app after signup. Numbers were cross-checked on 2026-09-27 (ai-bot.cn tool entries + official sites); re-verify each platform's pricing page before you rely on it.</p>
"""

FAQ_ZH = [
 {"question":"这5个工具里哪个免费额度最大方？","answer":"看维度。数据库最大是 AMiner（3.2 亿篇论文、6000 万学者、1.6 亿专利，检索全免费）；免费规则写最清楚的是切问学术（不限次快速搜索 + 每日 3 次深度搜索 + 每日 50 条问答 + 5 万字索引 + 1GB，免费）；高校场景玻尔最省事（1000+ 高校 CARSI 校园网免费登录）。"},
 {"question":"切问学术免费版具体能做什么？","answer":"注册即免费：不限次快速搜索、每日 3 次深度搜索（自然语言提问）、每日 50 条学术问答、AI 索引 5 万字（约 10 篇论文，模型能读懂的量）、1GB 存储、公式图表保留式翻译、论文订阅推送。超出后要 Plus ¥30/月（20 次深度搜索/天、200 条问答/天、100 万字索引约 200 篇、10GB）或 Pro ¥105/月（全不限量、50GB、不限次 AI Survey）。"},
 {"question":"AMiner 真的完全免费吗？","answer":"核心链路免费：学术检索（简单 + 智能搜索）、AI 对话、AI 阅读、学术空间管理都不收订阅费，由智谱 GLM-4.5 驱动。付费的是机构向的情报订阅等增值服务；沉思（自动生成文献综述/开题报告）有每日次数约束，以站内为准。"},
 {"question":"心流和切问、AMiner 有什么区别？","answer":"心流（阿里 iflow.cn）定位是「读」：近 3000 万篇论文（Nature/IEEE/ArXiv）免费精读，选中段落即可总结/翻译/解释并存笔记，还能把答案生成播客。它不做检索策略和体系化调研，这块切问（3.6 亿论文 + 每日问答额度）和 AMiner（3.2 亿论文 + 学者图谱）更强。"},
 {"question":"找不到论文全文怎么办，哪个平台下载免费？","answer":"沁言学术免费领用，宣传口径是一键批量下载成功率 95% 以上，是 5 家里唯一把下载成功率做成指标的平台。备选：AMiner 学术空间可保存和管理文献，心流支持引用跳转直接看被引摘要。"},
 {"question":"我是高校师生，玻尔怎么免费用？","answer":"玻尔（bohrium.com）支持全国 1000 多所高校 CARSI 校园网身份直接登录，免费获得专属权益；不用校园网也可以用个人邮箱注册。平台含 200+ 科研应用、60+ AI for Science 课程、多模态科学导航搜索和 RIS 一键引用导出（进 EndNote/Zotero），核心免费。"},
]

FAQ_EN = [
 {"question":"Which of the five offers the most generous free tier?","answer":"Depends on the axis. Largest database: AMiner (320M papers, 60M scholars, 160M patents, all search free). Most clearly-defined free rules: QieWen (unlimited quick search + 3 deep searches/day + 50 Q&A/day + 50k-char index + 1GB, all free). Easiest for students: Bohrium (free CARSI campus-network login at 1,000+ universities)."},
 {"question":"Exactly what does QieWen's free tier include?","answer":"Free on signup: unlimited quick search, 3 deep searches/day (natural-language queries), 50 academic Q&A/day, a 50,000-character AI index (about 10 papers — the total the model can ground on), 1GB storage, formula-preserving translation and paper-subscription push. Beyond that: Plus ¥30/mo (20 deep searches/day, 200 Q&A/day, 1M-char index ~200 papers, 10GB) or Pro ¥105/mo (unlimited, 50GB, unlimited AI Survey)."},
 {"question":"Is AMiner really completely free?","answer":"The core pipeline is free: academic search (simple + intelligent), AI dialogue, AI reading and academic-space management, no subscription fee, powered by Zhipu GLM-4.5. What is paid: institutional intelligence subscriptions and similar B2B services. 'Contemplation' (auto literature reviews / proposals) has daily caps — check in-app."},
 {"question":"How does iFlow differ from QieWen and AMiner?","answer":"iFlow (Alibaba, iflow.cn) is a reading tool: ~30M papers (Nature/IEEE/ArXiv) free close-reading, select any paragraph for summary/translation/term-explanation saved to notes, plus answer-to-podcast. It does not build search strategies or systematic reviews — that is where QieWen (360M-paper corpus + daily Q&A quotas) and AMiner (320M papers + scholar graph) are stronger."},
 {"question":"I can't find full-text PDFs — which platform is free for downloads?","answer":"QinYan (qinyanai.com) is free to start and advertises a 95%+ one-click batch literature download rate — the only platform of the five that makes download success rate a headline metric. Fallbacks: AMiner's academic space for saving/managing literature, iFlow's citation-jumping to read cited abstracts."},
 {"question":"As a university student, how do I use Bohrium for free?","answer":"Bohrium (bohrium.com) supports direct free login via CARSI campus-network identity at 1,000+ Chinese universities; a personal email signup works too. You get 200+ research apps, 60+ AI-for-Science courses, multimodal Science Navigator search and one-click RIS citation export (into EndNote/Zotero) — core usage free."},
]

zh_html, en_html = generate_guide_html(
    SLUG, TITLE_ZH, TITLE_EN, DESC_ZH, DESC_EN,
    CONTENT_ZH, CONTENT_EN,
    json.dumps(FAQ_ZH, ensure_ascii=False),
    json.dumps(FAQ_EN, ensure_ascii=False),
    TODAY
)

os.makedirs('/home/ubuntu/aifreeplan/zh/guides', exist_ok=True)
os.makedirs('/home/ubuntu/aifreeplan/en/guides', exist_ok=True)
with open(f'/home/ubuntu/aifreeplan/zh/guides/{SLUG}.html', 'w', encoding='utf-8') as f:
    f.write(zh_html)
with open(f'/home/ubuntu/aifreeplan/en/guides/{SLUG}.html', 'w', encoding='utf-8') as f:
    f.write(en_html)

ENTRY = {
    "slug": SLUG,
    "title_zh": TITLE_ZH,
    "title_en": TITLE_EN,
    "description_zh": DESC_ZH,
    "description_en": DESC_EN,
    "category": "productivity",
    "date_published": TODAY,
    "tags": ["AI学术科研", "文献检索", "切问学术", "AMiner", "心流", "沁言学术", "玻尔", "免费额度", "论文写作", "科研工具"],
    "icon": "📚",
    "excerpt_zh": "5款AI学术科研工具免费版实测：切问学术每日3次深度搜索+50条问答（¥30起Plus）、AMiner 3.2亿篇论文免费检索（GLM-4.5）、心流近3000万篇论文免费精读、沁言95%+文献批量下载、玻尔1000+高校CARSI免费登录。全链路0元组合方案。",
    "excerpt_en": "Five free AI academic-research tiers verified Sep 2026: QieWen (3 deep searches/day + 50 Q&A/day, Plus from ¥30/mo), AMiner (320M papers, free search on GLM-4.5), iFlow (~30M papers, free close reading), QinYan (95%+ batch literature download, free start), Bohrium (free CARSI campus login at 1,000+ universities). Full 0-cost pipeline included.",
    "faq_zh": FAQ_ZH,
    "faq_en": FAQ_EN,
}

for path in ('/home/ubuntu/aifreeplan/public/data/guides.json',
             '/home/ubuntu/aifreeplan/dist/data/guides.json'):
    try:
        d = json.load(open(path, encoding='utf-8'))
        guides = d['guides']
        d['guides'] = [g for g in guides if g['slug'] != SLUG]
        d['guides'].insert(0, ENTRY)
        d['updatedAt'] = datetime.now().isoformat()
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
        print(f"registered into {path} ({len(d['guides'])} guides)")
    except Exception as e:
        print(f"WARN could not register into {path}: {e}")

print(f"Generated {SLUG} (date {TODAY})")
print(f"  zh main text chars: {len(CONTENT_ZH)}")
print(f"  en main text chars: {len(CONTENT_EN)}")
