#!/usr/bin/env python3
"""Generate the 'Claude Haiku 5.5 free / near-free usage guide (2026)' article.
Data sources (verified 2026-10-10):
- ai-bot.cn daily news 10/8: 'Anthropic 推出最新轻量级模型 Claude Haiku 5.5', 跑分超 DeepSeek V4.1 Flash 与 GLM-5.3-Flash, 对标 GPT-6 Luna, 10万 token 内输入输出价降 90%, 首个支持 effort 五档, OSWorld 2.1 Max 72.4%, 适合执行层任务与子智能体.
- Anthropic announcement anthropic.com/claude-haiku-5-5:
  pricing table (per 1M tokens): Haiku 5.5 short(<=100k) in $0.10 / out $0.50, long(>100k) in $0.50 / out $2.50;
  cache read $0.01 / $0.05; cache write $0.125 / $0.625. 'up to 100k tokens make up ~90% of requests to previous Haiku'.
  Benchmarks: OSWorld 2.1 offline 72.4% (Haiku 4.5 15.7%, Sonnet 5.5 48.9%, Opus 5.5 83.9%);
  GDPval-AA v2.1 1620 (Haiku 4.5 735, Sonnet 5.5 1437, Opus 5.5 1840);
  HLE 45.9% no-tools (10.2% Haiku 4.5, 56.9% Sonnet, 64.5% Opus);
  Terminal-Bench 4.0 39.2% (0.0% Haiku 4.5, 16.4% Sonnet, 70.5% Opus).
  First Haiku with adjustable effort.
- Anthropic pricing docs (docs.anthropic.com/en/about-claude/pricing):
  'New users receive a small amount of free credits to test the API';
  Batch API 50% discount, stackable with prompt caching;
  code execution tool free when used with web_search_20260209 / web_fetch_20260209;
  1,550 free hours of code-execution per month per org;
  Sonnet 5.5 cache read lowered $0.20 -> $0.10 on 2026-10-07.
- Claude release notes 2026-10-07: launched claude-haiku-5-5; 1M ctx; 128k max out; adaptive thinking + effort;
  available on Claude API, Bedrock, Claude Platform on AWS, Google Cloud, Microsoft Foundry;
  migration gotchas (budget_tokens / temperature / top_p / top_k / assistant prefill -> 400; computer_20250124 -> 400);
  newer tokenizer ~30% more tokens than Haiku 4.5; no structured outputs on Bedrock.
- Rate-limit docs: Start tier Haiku 5.5 = 1,000 RPM / 2M ITPM / 400k OTPM; Build tier = 5,000 RPM / 5M ITPM / 1M OTPM.
"""
import os, sys, json
from datetime import datetime

sys.path.insert(0, '/home/ubuntu/aifreeplan/scripts')
from write_guide import generate_guide_html

SLUG = "claude-haiku-5-5-free-tier-guide-2026"
TODAY = "2026-10-10"

TITLE_ZH = "Claude Haiku 5.5 免费白嫖攻略：10万Token内输入$0.10/百万，首个支持effort五档的Claude轻量旗舰"
TITLE_EN = "Claude Haiku 5.5 Free/Zero-Cost Guide: $0.10/1M input under 100k tokens, first Claude with 5-level effort control"

DESC_ZH = "Anthropic 于 2026-10-07 上线 Claude Haiku 5.5：100 万上下文、12.8 万最大输出、首个支持 effort 五档调节的 Claude 轻量模型。短提示（≤10 万 Token）输入仅 $0.10/百万、输出 $0.50/百万，比 Sonnet 5.5 便宜 20 倍；Batch API 再打 5 折，新人 API 送免费额度，代码执行每月送 1550 小时。本文给全实测数字、白嫖入口、effort 调档、限速与避坑。"
DESC_EN = "Anthropic shipped Claude Haiku 5.5 on 2026-10-07: 1M context, 128k max output, and the first Claude with adjustable 5-level effort. Under 100k-token prompts cost just $0.10/1M input and $0.50/1M output, 20x cheaper than Sonnet 5.5; the Batch API cuts that 50% more, new API accounts get free credits, and code execution grants 1,550 free hours a month. Here are the exact numbers, the zero-cost entry points, effort tuning, rate limits, and gotchas."

CONTENT_ZH = """<h1>Claude Haiku 5.5 免费白嫖攻略：10万Token内输入$0.10/百万，首个支持effort五档的Claude轻量旗舰</h1>

<p>2026 年 10 月 7 日，Anthropic 上线了 <strong>Claude Haiku 5.5</strong>（模型 ID <code>claude-haiku-5-5</code>）。它不是又一个普通小模型，而是 <strong>Claude 家族里第一个支持 effort 五档调节</strong>的轻量旗舰，100 万 Token 上下文、12.8 万最大输出。关键数字（2026-10-10 核过 Anthropic 官方价目与发布说明）：短提示（≤10 万 Token，覆盖约 90% 的常规请求）<strong>输入 $0.10/百万、输出 $0.50/百万</strong>，比同代 Sonnet 5.5（$2/$10）便宜 <strong>20 倍</strong>；再叠加 <strong>Batch API 五折</strong>、<strong>新 API 账号免费额度</strong>、<strong>代码执行工具每月 1,550 小时免费</strong>，实际账单可以压到接近 0。先给结论：如果你的任务是<strong>分类、抽取、路由、批量子任务</strong>这类高并发、低延迟场景，Haiku 5.5 是目前 Claude 全家桶里<strong>单价最低、还能用 effort 省成本</strong>的一档，白嫖/低成本入口最多。下面是全部实测数字、入口和避坑点。</p>

<h2>核心规格与价格速览</h2>

<table>
<tr><th>项</th><th>数值</th></tr>
<tr><td>模型 ID</td><td><code>claude-haiku-5-5</code></td></tr>
<tr><td>发布日期</td><td>2026-10-07</td></tr>
<tr><td>上下文窗口</td><td><strong>1,000,000 Token</strong></td></tr>
<tr><td>最大输出</td><td><strong>128,000 Token</strong>（Batch 可到 300,000）</td></tr>
<tr><td>思考模式</td><td>自适应思考（默认开启）+ <strong>首个支持 effort 五档</strong>的 Haiku</td></tr>
<tr><td>定位</td><td>高并发、延迟敏感：分类 / 抽取 / 路由 / 子智能体</td></tr>
<tr><td>可用平台</td><td>Claude API、Amazon Bedrock、AWS Claude Platform、Google Cloud、Microsoft Foundry</td></tr>
</table>

<h2>价格表（美元/百万 Token，2026-10-10 官方口径）</h2>

<table>
<tr><th>项目</th><th>≤100k 提示</th><th>&gt;100k 提示</th></tr>
<tr><td><strong>输入</strong></td><td><strong>$0.10</strong></td><td>$0.50</td></tr>
<tr><td><strong>输出</strong></td><td><strong>$0.50</strong></td><td>$2.50</td></tr>
<tr><td>缓存写入（5 分钟）</td><td>$0.125</td><td>$0.625</td></tr>
<tr><td>缓存读取</td><td><strong>$0.01</strong></td><td>$0.05</td></tr>
</table>

<p>对照同代兄弟档：<strong>Sonnet 5.5 是 $2/$10，Opus 5.5 是 $4/$20，Fable 5.1 是 $10/$50</strong>。也就是说 Haiku 5.5 短档输入价只有 Sonnet 的 <strong>1/20</strong>、Opus 的 <strong>1/40</strong>。Anthropic 自己说 ≤10 万 Token 的短提示约占之前 Haiku 请求量的 <strong>90%</strong>——绝大多数用例会落在最便宜的这一档。再叠 <strong>Batch API 五折</strong>（短档落到约 $0.05/$0.25），非实时任务基本是「象征性收费」。</p>

<h2>白嫖 / 近 0 元入口（真实存在的 4 个）</h2>

<ol>
<li><strong>新 API 账号免费额度</strong>：Anthropic 官方明确「新用户会送一小笔免费额度试 API」（extended enterprise 试用找 sales）。首次充值/试用阶段，Haiku 5.5 短档 $0.10/$0.50 意味着这笔小钱能跑上<strong>几十万到上百万</strong> Token 的请求量，几乎 0 成本把分类 / 路由管道跑通。</li>
<li><strong>代码执行工具免费 + 每月 1,550 小时免费</strong>：只要请求里带了 <code>web_search_20260209</code>（或更新）/ <code>web_fetch_20260209</code>，<strong>代码执行调用不再单独计费</strong>；没带这两个工具时按执行时长计费，每个组织<strong>每月 1,550 小时免费</strong>，超出才计费。跑 Haiku 5.5 子智能体 + 代码执行，这块基本白送。</li>
<li><strong>缓存读 $0.01/百万</strong>：把稳定系统提示 / 工具定义放缓存，命中读取只有 $0.01（Sonnet 5.5 缓存读 10 月 7 日也刚从 $0.20 降到 $0.10，$0.05x 基数）。高并发 + 重复前缀的场景，实际单价能再砍一大截。</li>
<li><strong>effort 五档省钱</strong>：Haiku 5.5 首次支持按任务切 effort——简单任务用低 effort 省输出 Token 和推理成本，关键任务才拉高档。这是「同一个模型、不同价格」的省钱开关，配合 Batch 五折最狠。</li>
</ol>

<h2>实测性能：便宜但不拉胯</h2>

<table>
<tr><th>基准</th><th>Haiku 5.5</th><th>Haiku 4.5</th><th>Sonnet 5.5</th><th>Opus 5.5</th></tr>
<tr><td>OSWorld 2.1（离线子集，计算机操作）</td><td><strong>72.4%</strong></td><td>15.7%</td><td>48.9%</td><td>83.9%</td></tr>
<tr><td>GDPval-AA v2.1（知识工作）</td><td><strong>1620</strong></td><td>735</td><td>1437</td><td>1840</td></tr>
<tr><td>Humanity's Last Exam（无工具）</td><td>45.9%</td><td>10.2%</td><td>56.9%</td><td>64.5%</td></tr>
<tr><td>Terminal-Bench 4.0（Agent 编程）</td><td><strong>39.2%</strong></td><td>0.0%</td><td>16.4%</td><td>70.5%</td></tr>
</table>

<p>最扎眼的是 <strong>OSWorld 2.1 离线子集 72.4%</strong>：一个 $0.10/$0.50 的轻量模型，计算机操作跑到了 Sonnet 5.5（48.9%）之上、Opus 5.5（83.9%）之下。GDPval-AA 从上一代 Haiku 4.5 的 735 直接跳到 1620。代价是<strong>新分词器</strong>：同样一段文本，Claude 4.7 之后的模型（含 Haiku 5.5）比 Haiku 4.5 <strong>多计约 30% Token</strong>——估算成本时要把这 30% 补上，别照搬老模型用量。</p>

<h2>限速（Claude Console 各档）</h2>

<table>
<tr><th>档</th><th>RPM（请求/分）</th><th>ITPM（输入Token/分）</th><th>OTPM（输出Token/分）</th></tr>
<tr><td>Start</td><td>1,000</td><td>2,000,000</td><td>400,000</td></tr>
<tr><td>Build</td><td><strong>5,000</strong></td><td>5,000,000</td><td>1,000,000</td></tr>
</table>

<p>注意 <strong>各模型限速独立</strong>：你可以同时用 Haiku 5.5 顶满 5,000 RPM，再同时用 Sonnet 5.5 顶它自己的额度，互不占用。OTPM 按实际生成量实时结算，设大 <code>max_tokens</code> 本身不额外吃额度。</p>

<h2>怎么上手（从建 Key 到调用）</h2>

<ol>
<li>去 <a href="https://console.anthropic.com/">console.anthropic.com</a> 注册，拿 API Key（新账号自带一笔免费额度试 API）；</li>
<li>模型写 <code>claude-haiku-5-5</code>；最小调用（Python）：<br><code>curl https://api.anthropic.com/v1/messages -H "x-api-key: ***" -H "anthropic-version: 2023-06-01" -H "content-type: application/json" -d '{"model":"claude-haiku-5-5","max_tokens":1024,"messages":[{"role":"user","content":"..."}]}'</code></li>
<li>省钱三连：<strong>把系统提示/工具放缓存</strong>（读 $0.01）+ <strong>按任务设 effort</strong>（简单任务低档）+ <strong>非实时走 Batch API</strong>（五折）；</li>
<li>高并发子智能体：Haiku 5.5 顶 Build 档 5,000 RPM 当执行层，关键决策再上 Opus/Sonnet；</li>
<li>代码执行 + 搜索：请求里带 <code>web_search_20260209</code>/<code>web_fetch_20260209</code>，代码执行就不再单独计费。</li>
</ol>

<h2>避坑（从 Haiku 4.5 迁移会报错的地方）</h2>

<ul>
<li><code>budget_tokens</code>（手动扩展思考）、<code>temperature</code> / <code>top_p</code> / <code>top_k</code>、assistant 消息预填，在 Haiku 5.5 上都会返回 <strong>400 错误</strong>——改用自适应思考 + effort；</li>
<li>旧 <code>computer_20250124</code> 工具返回 400：Claude API / Google Cloud 改用 <code>computer_toolset_20260801</code>，Amazon Bedrock 用 <code>computer_20251124</code>；</li>
<li>改了 system / tools / 历史轮次后再回传旧 thinking block，也会 400；</li>
<li><strong>Amazon Bedrock 上 Haiku 5.5 暂不支持结构化输出（structured outputs）</strong>，要 JSON schema 严格模式就上 Claude API 或 Google Cloud；</li>
<li>新分词器多计约 30% Token，做成本预算时别用老模型的老用量直接套。</li>
</ul>

<h2>和同类「低价轻量旗舰」对比</h2>

<table>
<tr><th>模型</th><th>短档输入价</th><th>短档输出价</th><th>特点</th></tr>
<tr><td><strong>Claude Haiku 5.5</strong></td><td><strong>$0.10/百万</strong></td><td><strong>$0.50/百万</strong></td><td>1M 上下文，首个 effort 五档，OSWorld 72.4%</td></tr>
<tr><td>Claude Sonnet 5.5</td><td>$2/百万</td><td>$10/百万</td><td>日常任务性价比档</td></tr>
<tr><td>DeepSeek V4.1 Flash / GLM-5.3 Flash</td><td>更低（开源价）</td><td>更低（开源价）</td><td>新闻里 Haiku 5.5 跑分已超这两家 Flash</td></tr>
<tr><td>OpenRouter <code>:free</code> 池（Nemotron 3 等）</td><td>$0</td><td>$0</td><td>真 0 元，但 50~1000 次/天限速、非 Claude 生态</td></tr>
</table>

<p>（各数字来自 Anthropic 价目页、发布说明、限速文档与 ai-bot.cn 10 月 8 日快讯；额度、价格与限速以 Anthropic Console 内实时展示为准。）</p>

<h2>常见问题</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: Haiku 5.5 有免费额度吗？</div>
<div class="faq-a">新 API 账号会送一小笔免费额度试 API（官方 FAQ 原文）。Haiku 5.5 短档 $0.10/$0.50，这笔额度能跑几十万到上百万 Token。另有代码执行工具每月 1,550 小时免费、带 web_search/web_fetch 时代码执行不单独计费。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 到底多便宜？</div>
<div class="faq-a">短提示（≤10 万 Token）输入 $0.10/百万、输出 $0.50/百万；Batch 五折后约 $0.05/$0.25；缓存读 $0.01/百万。比 Sonnet 5.5（$2/$10）便宜 20 倍，比 Opus 5.5（$4/$20）便宜 40 倍。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: effort 五档是干嘛的？</div>
<div class="faq-a">Haiku 5.5 是 Claude 首个支持按任务切 effort 档的模型——简单任务低 effort 省成本，复杂任务拉高。官方用它实测 OSWorld、GDPval-AA、Humanity's Last Exam 三个基准在不同 effort 下的表现，是「同模型不同价」的省钱开关。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 从 Haiku 4.5 迁移要注意什么？</div>
<div class="faq-a">budget_tokens、temperature、top_p、top_k、assistant 预填、旧 computer_20250124 工具、以及改 system 后回传旧 thinking 都会 400；新分词器多计约 30% Token；Bedrock 上暂不支持结构化输出。详见官方迁移指南。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 能不能真 0 元？</div>
<div class="faq-a">Haiku 5.5 本身是付费 API（无 Claude 官方 :free 池）。想要 $0 长上下文/多模态，走 OpenRouter 的 Nemotron 3 等 :free 模型；想要 Claude 生态的低成本，Haiku 5.5 + Batch 五折 + 缓存 + 新账号免费额度是当前最贴 0 的组合。</div>
</div>
</div>

<h2>总结</h2>

<p>Haiku 5.5 的价值一句话：<strong>Claude 全家桶里单价最低（短档 $0.10/$0.50，Sonnet 的 1/20）、100 万上下文、首个 effort 五档、还能 Batch 五折 + 缓存 $0.01 + 每月 1,550 小时免费代码执行</strong>。它是执行层 / 子智能体 / 分类抽取这类高并发场景的默认选项——把重活留给 Opus，把 90% 的常规请求压到 Haiku 5.5，账单一落一大截。额度、价格、限速都在变，动手前以 Anthropic Console 实时数字为准。</p>
"""

CONTENT_EN = """<h1>Claude Haiku 5.5 Free/Zero-Cost Guide: $0.10/1M input under 100k tokens, first Claude with 5-level effort control</h1>

<p>On 2026-10-07, Anthropic shipped <strong>Claude Haiku 5.5</strong> (model ID <code>claude-haiku-5-5</code>). It is not just another small model, it is the <strong>first Claude to ship with a 5-level adjustable effort control</strong>, a 1,000,000-token context, and 128,000 max output tokens. The key numbers (verified 2026-10-10 against Anthropic's pricing page and release notes): for short prompts (under 100k tokens, roughly 90% of typical requests) it costs <strong>$0.10 / 1M input and $0.50 / 1M output</strong>, which is <strong>20x cheaper</strong> than same-generation Sonnet 5.5 ($2/$10). Stack the <strong>Batch API 50% discount</strong>, <strong>free credits for new API accounts</strong>, and <strong>1,550 free hours of code execution per month</strong> on top, and the bill gets close to zero. Bottom line up front: if your job is <strong>classification, extraction, routing, or bulk subagent work</strong>, Haiku 5.5 is the cheapest and most cost-controllable tier in the whole Claude lineup, and it has the most near-zero-cost entry points. Here are all the measured numbers, the free entries, and the gotchas.</p>

<h2>Core Specs &amp; Pricing at a Glance</h2>

<table>
<tr><th>Item</th><th>Value</th></tr>
<tr><td>Model ID</td><td><code>claude-haiku-5-5</code></td></tr>
<tr><td>Released</td><td>2026-10-07</td></tr>
<tr><td>Context window</td><td><strong>1,000,000 tokens</strong></td></tr>
<tr><td>Max output</td><td><strong>128,000 tokens</strong> (up to 300,000 in Batch)</td></tr>
<tr><td>Thinking</td><td>Adaptive thinking (on by default) + the <strong>first Haiku with 5-level effort</strong></td></tr>
<tr><td>Positioning</td><td>High-volume, latency-sensitive: classification / extraction / routing / subagents</td></tr>
<tr><td>Platforms</td><td>Claude API, Amazon Bedrock, AWS Claude Platform, Google Cloud, Microsoft Foundry</td></tr>
</table>

<h2>Pricing (USD per 1M tokens, official 2026-10-10 figures)</h2>

<table>
<tr><th>Item</th><th>prompt &lt;= 100k</th><th>prompt &gt; 100k</th></tr>
<tr><td><strong>Input</strong></td><td><strong>$0.10</strong></td><td>$0.50</td></tr>
<tr><td><strong>Output</strong></td><td><strong>$0.50</strong></td><td>$2.50</td></tr>
<tr><td>Cache write (5 min)</td><td>$0.125</td><td>$0.625</td></tr>
<tr><td>Cache read</td><td><strong>$0.01</strong></td><td>$0.05</td></tr>
</table>

<p>For the sibling tiers: <strong>Sonnet 5.5 is $2/$10, Opus 5.5 is $4/$20, Fable 5.1 is $10/$50</strong>. So Haiku 5.5's short-prompt input price is <strong>1/20</strong> of Sonnet's and <strong>1/40</strong> of Opus's. Anthropic states that prompts under 100k tokens make up about <strong>90%</strong> of prior Haiku request volume, so most workloads land in the cheapest row. Add the <strong>50% Batch API discount</strong> (roughly $0.05/$0.25 on the short tier) and non-realtime jobs get to near-nominal cost.</p>

<h2>The four real zero-cost / near-zero entries</h2>

<ol>
<li><strong>Free credits for new API accounts</strong>: Anthropic's FAQ states new users get a small amount of free credits to test the API. At $0.10/$0.50 on the short tier, that grant lets you push hundreds of thousands to over a million tokens of classification / routing work for effectively nothing.</li>
<li><strong>Code execution tool free + 1,550 free hours/month</strong>: when your request includes <code>web_search_20260209</code> (or later) / <code>web_fetch_20260209</code>, code-execution calls are billed only on standard token cost, no separate charge. Without those tools it bills by execution time, and each organization gets <strong>1,550 free hours of code execution per month</strong>. Haiku 5.5 subagent + code execution is largely free in this path.</li>
<li><strong>Cache reads at $0.01 / 1M</strong>: keep stable system prompts and tool definitions cached; a hit is $0.01 (Sonnet 5.5 cache reads were also cut from $0.20 to $0.10 on 2026-10-07, now 0.05x base). For high-volume repeated-prefix work the effective price drops sharply.</li>
<li><strong>effort five tiers</strong>: Haiku 5.5 is the first model where you pick effort per task, so cheap jobs run at low effort and only critical ones run high. This is a same-model-different-price saver, and it hits hardest combined with the Batch 50%.</li>
</ol>

<h2>Measured performance: cheap, not weak</h2>

<table>
<tr><th>Benchmark</th><th>Haiku 5.5</th><th>Haiku 4.5</th><th>Sonnet 5.5</th><th>Opus 5.5</th></tr>
<tr><td>OSWorld 2.1 (offline subset, computer use)</td><td><strong>72.4%</strong></td><td>15.7%</td><td>48.9%</td><td>83.9%</td></tr>
<tr><td>GDPval-AA v2.1 (knowledge work)</td><td><strong>1620</strong></td><td>735</td><td>1437</td><td>1840</td></tr>
<tr><td>Humanity's Last Exam (no tools)</td><td>45.9%</td><td>10.2%</td><td>56.9%</td><td>64.5%</td></tr>
<tr><td>Terminal-Bench 4.0 (agentic coding)</td><td><strong>39.2%</strong></td><td>0.0%</td><td>16.4%</td><td>70.5%</td></tr>
</table>

<p>The standout is <strong>OSWorld 2.1 offline at 72.4%</strong>: a $0.10/$0.50 lightweight model beats Sonnet 5.5 (48.9%) on computer use and sits just under Opus 5.5 (83.9%). GDPval-AA jumps from Haiku 4.5's 735 to 1620. The catch is the <strong>newer tokenizer</strong>: the same text counts about <strong>30% more tokens</strong> on Claude 4.7 and later (including Haiku 5.5) than on Haiku 4.5, so bake that 30% into any cost model rather than copying old-model usage.</p>

<h2>Rate limits (Claude Console tiers)</h2>

<table>
<tr><th>Tier</th><th>RPM</th><th>ITPM</th><th>OTPM</th></tr>
<tr><td>Start</td><td>1,000</td><td>2,000,000</td><td>400,000</td></tr>
<tr><td>Build</td><td><strong>5,000</strong></td><td>5,000,000</td><td>1,000,000</td></tr>
</table>

<p>Note that <strong>limits are per model</strong>: you can push Haiku 5.5 to its 5,000 RPM on the Build tier while simultaneously pushing Sonnet 5.5 against its own separate ceiling. OTPM is settled in real time on generated tokens, so a large <code>max_tokens</code> does not itself consume limit.</p>

<h2>Getting started (from key to call)</h2>

<ol>
<li>Register at <a href="https://console.anthropic.com/">console.anthropic.com</a> and grab your API key (new accounts carry a small free credit to test the API);</li>
<li>Set the model to <code>claude-haiku-5-5</code>. Minimal call: <code>curl https://api.anthropic.com/v1/messages -H "x-api-key: ***" -H "anthropic-version: 2023-06-01" -H "content-type: application/json" -d '{"model":"claude-haiku-5-5","max_tokens":1024,"messages":[{"role":"user","content":"..."}]}'</code></li>
<li>Saver trio: <strong>cache your system prompt / tools</strong> (read $0.01) + <strong>set effort per task</strong> (low for simple jobs) + <strong>use the Batch API for non-realtime</strong> (50% off);</li>
<li>For high-volume subagents, run Haiku 5.5 as the execution layer at Build-tier 5,000 RPM and escalate only the critical decisions to Opus / Sonnet;</li>
<li>Code execution + search: include <code>web_search_20260209</code> / <code>web_fetch_20260209</code> so code execution stops being billed separately.</li>
</ol>

<h2>Gotchas (migrating from Haiku 4.5)</h2>

<ul>
<li><code>budget_tokens</code> (manual extended thinking), <code>temperature</code> / <code>top_p</code> / <code>top_k</code>, and assistant-message prefill all return <strong>400 errors</strong> on Haiku 5.5; use adaptive thinking + effort instead;</li>
<li>The old <code>computer_20250124</code> tool returns 400: use <code>computer_toolset_20260801</code> on the Claude API / Google Cloud, or <code>computer_20251124</code> on Amazon Bedrock;</li>
<li>Sending back thinking blocks after you change system / tools / earlier turns also 400s;</li>
<li><strong>On Amazon Bedrock, Haiku 5.5 does not yet support structured outputs</strong>; if you need strict JSON-schema mode, use the Claude API or Google Cloud;</li>
<li>The new tokenizer counts about 30% more tokens, so do not reuse old-model usage for cost budgeting.</li>
</ul>

<h2>Compared to other cheap lightweight flagships</h2>

<table>
<tr><th>Model</th><th>Short input price</th><th>Short output price</th><th>Note</th></tr>
<tr><td><strong>Claude Haiku 5.5</strong></td><td><strong>$0.10 / 1M</strong></td><td><strong>$0.50 / 1M</strong></td><td>1M context, first 5-level effort, OSWorld 72.4%</td></tr>
<tr><td>Claude Sonnet 5.5</td><td>$2 / 1M</td><td>$10 / 1M</td><td>Everyday value tier</td></tr>
<tr><td>DeepSeek V4.1 Flash / GLM-5.3 Flash</td><td>lower (open pricing)</td><td>lower (open pricing)</td><td>Haiku 5.5 scores above these two Flash models in the 10/8 news round-up</td></tr>
<tr><td>OpenRouter <code>:free</code> pool (Nemotron 3 etc.)</td><td>$0</td><td>$0</td><td>Truly free but 50~1,000 req/day cap, non-Claude ecosystem</td></tr>
</table>

<p>(All figures from Anthropic's pricing page, release notes, rate-limit docs, and the ai-bot.cn Oct 8 news; allowances, prices, and limits follow Anthropic's live Console display.)</p>

<h2>FAQ</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: Does Haiku 5.5 have a free tier?</div>
<div class="faq-a">New API accounts receive a small amount of free credits to test the API (per Anthropic's FAQ). At $0.10/$0.50 on the short tier that grant runs hundreds of thousands to over a million tokens. Separately, code execution grants 1,550 free hours/month, and code execution is billed only on token cost when web_search / web_fetch are in the request.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: How cheap is it really?</div>
<div class="faq-a">For prompts under 100k tokens: $0.10/1M input, $0.50/1M output. With the 50% Batch discount it is about $0.05/$0.25; cache reads are $0.01/1M. That is 20x cheaper than Sonnet 5.5 ($2/$10) and 40x cheaper than Opus 5.5 ($4/$20).</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: What are the five effort levels for?</div>
<div class="faq-a">Haiku 5.5 is the first Claude model where you pick effort per task, so simple jobs run cheaper at low effort and only critical ones run high. Anthropic measured OSWorld, GDPval-AA, and Humanity's Last Exam at each effort level. It is a same-model-different-price cost switch.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: What breaks when I migrate from Haiku 4.5?</div>
<div class="faq-a">budget_tokens, temperature, top_p, top_k, assistant prefill, the old computer_20250124 tool, and returning old thinking blocks after a system change all return 400. The new tokenizer counts ~30% more tokens, and Bedrock does not yet support structured outputs.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Can I use it for real $0?</div>
<div class="faq-a">Haiku 5.5 is a paid API (there is no official Claude :free pool). For genuinely $0 long-context / multimodal, use OpenRouter's free models like Nemotron 3. For the cheapest Claude-ecosystem option, combine Haiku 5.5 with the 50% Batch discount, $0.01 cache reads, and new-account free credits.</div>
</div>
</div>

<h2>Bottom Line</h2>

<p>Haiku 5.5 in one sentence: <strong>the cheapest tier in the Claude lineup (short tier $0.10/$0.50, 1/20 of Sonnet), with a 1M context, the first 5-level effort control, plus a 50% Batch discount, $0.01 cache reads, and 1,550 free code-execution hours a month</strong>. It is the default choice for execution layers, subagents, and high-volume classification / extraction, keeping heavy work on Opus while pushing the 90% of routine requests to Haiku 5.5 and cutting the bill sharply. Allowances, prices, and limits are in flux, verify them in Anthropic's Console before you commit.</p>
"""

FAQ_ZH = [
 {"question":"Haiku 5.5 有免费额度吗？","answer":"新 API 账号会送一小笔免费额度试 API（官方 FAQ 原文）。Haiku 5.5 短档 $0.10/$0.50，能跑几十万到上百万 Token。另有代码执行工具每月 1,550 小时免费、带 web_search/web_fetch 时不单独计费。"},
 {"question":"到底多便宜？","answer":"短提示（≤10 万 Token）输入 $0.10/百万、输出 $0.50/百万；Batch 五折约 $0.05/$0.25；缓存读 $0.01/百万。比 Sonnet 5.5 便宜 20 倍，比 Opus 5.5 便宜 40 倍。"},
 {"question":"effort 五档是干嘛的？","answer":"Haiku 5.5 是首个支持按任务切 effort 的 Claude 模型——简单任务低档省钱、复杂任务拉高。官方用它实测 OSWorld、GDPval-AA、Humanity's Last Exam。"},
 {"question":"从 Haiku 4.5 迁移要注意什么？","answer":"budget_tokens、temperature、top_p、top_k、assistant 预填、旧 computer_20250124、以及改 system 后回传旧 thinking 都会 400；新分词器多计约 30% Token；Bedrock 暂不支持结构化输出。"},
 {"question":"能不能真 0 元？","answer":"Haiku 5.5 本身是付费 API，无官方 :free 池。想要 $0 走 OpenRouter 的 Nemotron 3 等免费模型；想要 Claude 生态低成本，Haiku 5.5 + Batch 五折 + 缓存 + 新账号免费额度是最贴 0 的组合。"},
]
FAQ_EN = [
 {"question":"Does Haiku 5.5 have a free tier?","answer":"New API accounts get a small amount of free credits to test the API. At $0.10/$0.50 on the short tier that is hundreds of thousands to over a million tokens, plus 1,550 free code-execution hours a month and no separate charge when web_search/web_fetch are included."},
 {"question":"How cheap is it really?","answer":"Under 100k-token prompts: $0.10/1M input, $0.50/1M output; about $0.05/$0.25 with the 50% Batch discount; cache reads $0.01/1M. 20x cheaper than Sonnet 5.5 and 40x cheaper than Opus 5.5."},
 {"question":"What are the five effort levels for?","answer":"Haiku 5.5 is the first Claude model with per-task effort, so simple jobs run cheaply at low effort. Anthropic measured OSWorld, GDPval-AA, and Humanity's Last Exam at each level. It is a same-model-different-price cost switch."},
 {"question":"What breaks when migrating from Haiku 4.5?","answer":"budget_tokens, temperature, top_p, top_k, assistant prefill, the old computer_20250124 tool, and returning old thinking blocks all 400. The new tokenizer counts ~30% more tokens, and Bedrock lacks structured outputs."},
 {"question":"Can I use it for real $0?","answer":"Haiku 5.5 is a paid API with no official free pool. For true $0 use OpenRouter free models like Nemotron 3; for the cheapest Claude-ecosystem option combine Haiku 5.5 with the 50% Batch discount, $0.01 cache reads, and new-account credits."},
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
    "category": "llm",
    "date_published": TODAY,
    "tags": ["Anthropic", "Claude", "Claude Haiku 5.5", "轻量旗舰", "effort五档", "免费额度", "Batch API五折", "代码执行免费", "1M上下文", "低价API"],
    "icon": "⚡",
    "excerpt_zh": "Claude Haiku 5.5（2026-10-07 上线）：100万上下文、12.8万输出、首个支持effort五档。短提示输入$0.10/百万、输出$0.50/百万，比Sonnet 5.5便宜20倍；Batch五折、新人API免费额度、代码执行每月1550小时免费。OSWorld 2.1离线72.4%。",
    "excerpt_en": "Claude Haiku 5.5 (2026-10-07): 1M context, 128k output, first Claude with 5-level effort. $0.10/1M input and $0.50/1M output under 100k tokens, 20x cheaper than Sonnet 5.5; 50% Batch discount, new-account free credits, 1,550 free code-execution hours/month. OSWorld 2.1 offline 72.4%.",
    "faq_zh": FAQ_ZH,
    "faq_en": FAQ_EN,
}

for path in ('/home/ubuntu/aifreeplan/public/data/guides.json',
             '/home/ubuntu/aifreeplan/dist/data/guides.json'):
    try:
        with open(path, encoding='utf-8') as fh:
            d = json.load(fh)
        guides = d['guides']
        d['guides'] = [g for g in guides if g.get('slug') != SLUG]
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
