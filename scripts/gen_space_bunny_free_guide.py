#!/usr/bin/env python3
"""Generate the 'Space Bunny Alpha — Free Anonymous Model on OpenRouter' (2026).
Data sources (verified 2026-10-03):
- OpenRouter API (openrouter.ai/api/v1/models + .../endpoints), model id stealth/space-bunny-alpha:
  pricing prompt=$0 completion=$0, context_length=1,000,000, max_completion_tokens=524,288,
  expiration_date=2026-10-05, modality text+image+video->text,
  reasoning supported_efforts [max,xhigh,high,medium,low] (default max, mandatory),
  supports tool_choice/tools/function calling/response_format(JSON schema), created 2026-09-23.
- ai-bot.cn/space-bunny/ : 匿名上线 OpenRouter + OpenCode 的大模型; 主打快速推理/编程/原生多模态;
  100万 Token 上下文; 上线仅3天冲上两大平台单日调用量榜首; 社区评价"约等于 GLM 5.3 Flash 但更快";
  最主流身份猜测是 MiniMax M3.1(Flash 版), MiniMax 已官宣 M3.1-Flash-Preview 上线 MiniMax Code.
- ai-bot.cn/m3-1-flash-preview/ : M3.1-Flash-Preview = MoE(继承 M3, 428B总参/每token约23B激活),
  100万 token 上下文, 五档推理强度(low~max), 首字延迟约280ms(Low档210ms), 生成速度约126 tokens/s.
- OpenRouter docs (api-reference/limits): 免费模型变体(以 :free 结尾)按累计充值额分档限速;
  GET /api/v1/key 的 free_model_daily_requests 字段报告当日免费模型请求计数与上限.
"""
import os, sys, json
from datetime import datetime

sys.path.insert(0, '/home/ubuntu/aifreeplan/scripts')
from write_guide import generate_guide_html

SLUG = "space-bunny-alpha-free-openrouter-2026"
TODAY = "2026-10-03"

TITLE_ZH = "Space Bunny 免费攻略：OpenRouter匿名模型$0/0，100万上下文多模态，免费预览到2026-10-05"
TITLE_EN = "Space Bunny Free Guide: $0/$0 Anonymous Model on OpenRouter, 1M-Context Multimodal, Free Until 2026-10-05"

DESC_ZH = "Space Bunny（stealth/space-bunny-alpha）是2026年9月匿名上线OpenRouter与OpenCode的大模型：输入/输出都是$0，100万Token上下文，支持文本+图像+视频多模态输入，low~max五档推理可调，支持工具调用。上线3天冲上两平台单日调用量榜首，社区评价'约等于GLM 5.3 Flash但更快'。免费预览窗口到2026-10-05。本文给全调用方法、免费限制、身份猜测与竞品对比。"
DESC_EN = "Space Bunny (stealth/space-bunny-alpha) is an anonymous model launched on OpenRouter and OpenCode in Sept 2026: $0 input and $0 output, 1M-token context, native text+image+video multimodal input, adjustable low~max reasoning, and tool-calling support. It hit #1 in daily calls on both platforms within 3 days; the community rates it 'roughly GLM 5.3 Flash but faster.' The free preview window runs until 2026-10-05. This guide covers how to call it, the free limits, the identity guess, and a competitor comparison."

CONTENT_ZH = """<h1>Space Bunny 免费攻略：OpenRouter匿名模型$0/0，100万上下文多模态，免费预览到2026-10-05</h1>

<p>Space Bunny（OpenRouter 模型 ID <code>stealth/space-bunny-alpha</code>）是 2026 年 9 月匿名上线 OpenRouter 与 OpenCode 的大模型，最直接的数字（2026-10-03 经 OpenRouter API 核对）：<strong>输入 $0 / 输出 $0</strong>，<strong>100 万（1,000,000）Token 上下文</strong>，<strong>单次最大输出 524,288 Token</strong>，支持<strong>文本 + 图像 + 视频</strong>三种输入，<strong>low / medium / high / xhigh / max 五档推理强度</strong>可调（默认 max、推理为必选），并支持<strong>工具调用、Function Calling 与 JSON Schema 结构化输出</strong>。模型 API 的 <code>expiration_date</code> 字段是 <strong>2026-10-05</strong>——也就是说这条免费窗口大概率在 10 月 5 日收口。社区实测评价是"约等于 GLM 5.3 Flash 但更快"，上线仅 3 天就冲上 OpenRouter 与 OpenCode 两个平台的<strong>单日调用量榜首</strong>。先给结论：想在 0 元、免充值的状态下白嫖一个"百万上下文 + 多模态 + 可跑 Agent"的模型，Space Bunny 是当下 OpenRouter 上最实的一个免费口子；但它是匿名模型、身份未官宣、免费窗口明确有到期日，重度使用要赶在 10-05 前跑完，或到期后看它是否转为付费/下架。</p>

<h2>免费额度与模型参数速览</h2>

<table>
<tr><th>项目</th><th>数字 / 规则</th><th>来源</th></tr>
<tr><td>模型 ID</td><td><code>stealth/space-bunny-alpha</code>（OpenRouter）</td><td>OpenRouter API</td></tr>
<tr><td>发布时间</td><td>2026-09-23（API created 字段），上线约 3 天冲到单日用量榜首</td><td>OpenRouter API / ai-bot.cn</td></tr>
<tr><td>输入 / 输出价格</td><td><strong>$0 / $0</strong>（preview 窗口内）</td><td>OpenRouter pricing</td></tr>
<tr><td>免费窗口</td><td><code>expiration_date</code> = <strong>2026-10-05</strong>，到期后可能转付费或下架</td><td>OpenRouter API</td></tr>
<tr><td>上下文窗口</td><td><strong>1,000,000 Token</strong></td><td>OpenRouter API</td></tr>
<tr><td>单次最大输出</td><td><strong>524,288 Token</strong></td><td>OpenRouter API</td></tr>
<tr><td>输入模态</td><td>文本 + 图像 + 视频 → 文本（多模态输入）</td><td>OpenRouter API</td></tr>
<tr><td>推理强度</td><td>low / medium / high / xhigh / max 五档，默认 max，推理必选</td><td>OpenRouter API</td></tr>
<tr><td>工具 / 结构化</td><td>支持 tool_choice、tools（Function Calling）、response_format（JSON Schema）</td><td>OpenRouter API</td></tr>
<tr><td>身份</td><td>匿名，架构未公开；最主流猜测为 <strong>MiniMax M3.1（Flash 版）</strong>，官方未认领</td><td>ai-bot.cn</td></tr>
<tr><td>免费限速</td><td>OpenRouter 对免费模型按累计充值额分档限速，当日免费请求计数见 <code>GET /api/v1/key</code> 的 <code>free_model_daily_requests</code></td><td>OpenRouter 文档</td></tr>
</table>

<h2>免费入口：从注册到跑通一次调用</h2>

<ol>
<li>打开 <a href="https://openrouter.ai/">OpenRouter</a> 官网，用邮箱或 Google 账号注册；</li>
<li>在模型列表搜索 <code>stealth/space-bunny-alpha</code>，进详情页确认 <strong>$0/$0</strong> 与 <code>expiration_date: 2026-10-05</code>；</li>
<li>在账户设置（Keys 页）生成一个 API Key，用于 API 调用；</li>
<li>不写代码也能试：直接进 OpenRouter 网页端 Chat，选 Space Bunny 免费对话；</li>
<li>接 API：把 <code>model</code> 设为 <code>stealth/space-bunny-alpha</code>，按需设置 <code>reasoning_effort</code>（low 求快、max 求准）、工具调用或把图片/视频帧塞进多模态输入；</li>
<li>在 OpenCode 里同样能选中它当后端模型，跑 Agent 工作流。</li>
</ol>

<p>关键提醒：<strong>免费窗口到 2026-10-05</strong>。到期后 <code>stealth/space-bunny-alpha</code> 大概率要么转成按 token 计费、要么从 OpenRouter 下架——想白嫖就赶在到期前把长文档、大代码库、多模态任务跑完，别把免费额度假设成"永久"。</p>

<h2>免费能跑哪些事（受窗口与限速约束）</h2>

<ul>
<li><strong>极速推理</strong>：社区实测"约等于 GLM 5.3 Flash 但更快"，几分钟能生成完整网站；</li>
<li><strong>编程 / 前端</strong>：实测几分钟生成作品集网站，单文件 1,564 行 GPU 流体模拟演示都能出，完成度被评"略胜 GLM 5.3 Flash"；</li>
<li><strong>百万级长上下文</strong>：1,000,000 Token 一次性吞整本书或大型代码库，不截断；</li>
<li><strong>多模态输入</strong>：文本 / 图像 / 视频三种输入，可理解截图、设计稿、视频帧；</li>
<li><strong>Agent 自动化</strong>：支持 Function Calling、Tool Choice 与 JSON 结构化输出，可接工具链跑多步任务；</li>
<li><strong>推理强度权衡</strong>：low 档跑简单任务求快，max 档跑复杂任务求准，速度/效果自己拨。</li>
</ul>

<p>这些都不额外收钱（窗口内 $0/$0），真正消耗的是<strong>免费窗口 + OpenRouter 免费模型限速</strong>。任务越长、上下文越大、多模态越多，撞限速越快；当日免费请求剩余量以 <code>free_model_daily_requests</code> 实时值为准。</p>

<h2>身份猜测：它到底是谁</h2>

<p>Space Bunny 参数量、是否 MoE、注意力机制等架构信息<strong>完全未公开</strong>。最主流、证据最充分的猜测是 <strong>MiniMax M3.1（Flash 版）</strong>，但 MiniMax 官方尚未认领。佐证是 MiniMax 同期官宣了 <strong>M3.1-Flash-Preview</strong>（MoE，继承 M3 底座约 428B 总参 / 每 token 激活约 23B，1M 上下文，low~max 五档推理，首字约 280ms / Low 档 210ms，生成约 126 tokens/秒），配置与 Space Bunny 高度重合。也就是说，匿名模型是"官方不便直接挂名"的常见打法——先匿名跑量、攒口碑，再决定挂不挂品牌。</p>

<h2>和竞品对比：免费额度落在哪</h2>

<table>
<tr><th>维度</th><th>Space Bunny（stealth）</th><th>GLM-5.3 Flash（z-ai）</th></tr>
<tr><td>价格</td><td><strong>$0 / $0</strong>（窗口到 2026-10-05）</td><td>输入 $0.00000015 / 输出 $0.0000005（付费计</th></tr>
<tr><td>上下文</td><td>1,000,000 Token，最大输出 524,288</td><td>1,048,576 Token，最大输出 128,000</td></tr>
<tr><td>架构</td><td>未公开（推测 MoE）</td><td>MoE，约 320B 总参 / 18B 激活，稀疏+线性混合注意力</td></tr>
<tr><td>速度</td><td>社区评价"约等于 GLM 5.3 Flash 但更快"</td><td>输出约 90 tok/s，TTFT 约 0.2s</td></tr>
<tr><td>多模态</td><td>文本 / 图像 / 视频输入</td><td>文本 / 图像 / 视频输入</td></tr>
<tr><td>推理档位</td><td>low / medium / high / xhigh / max</td><td>low / high / max（不可关闭）</td></tr>
<tr><td>身份</td><td>匿名（推测 MiniMax M3.1）</td><td>z-ai（智谱）公开模型</td></tr>
</table>

<p>（竞品价格/规格取自 OpenRouter API，2026-10-03 核对；口径以各模型实时为准。）</p>

<h2>注意事项与避坑</h2>

<ul>
<li><strong>免费窗口明确到期</strong>：<code>expiration_date 2026-10-05</code>，别把 $0 当长期额度；</li>
<li><strong>匿名=无官方背书</strong>：架构与身份未官宣，SLA / 可用性以 OpenRouter 实时 uptime（约 99.9%）为准，别拿它跑生产关键链路；</li>
<li><strong>免费模型限速</strong>：OpenRouter 对免费模型按累计充值额分档限速，当日剩余免费请求看 <code>free_model_daily_requests</code>，突发会撞 429；</li>
<li><strong>推理必选</strong>：reasoning 是 mandatory，默认 max——想省时间把 <code>reasoning_effort</code> 拨到 low，别一直用 max 白烧窗口。</li>
</ul>

<h2>常见问题</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: Space Bunny 现在免费吗？怎么收费？</div>
<div class="faq-a">窗口内 $0 输入 / $0 输出，免充值即可调。API 的 expiration_date 是 2026-10-05，到期后大概率转按 token 计费或下架——白嫖要赶在 10-05 前。</div>
</div>
<div class="faq-item">
<div class="faq-q">Q: 上下文和输出上限是多少？</div>
<div class="faq-a">上下文 1,000,000 Token，单次最大输出 524,288 Token，支持文本+图像+视频多模态输入。</div>
</div>
<div class="faq-item">
<div class="faq-q">Q: 它比 GLM 5.3 Flash 强在哪？</div>
<div class="faq-a">社区实测评价"约等于 GLM 5.3 Flash 但更快"，编程完成度"略胜"；且最大输出 524K（GLM 是 128K）。但它是匿名模型，身份与架构未公开。</div>
</div>
<div class="faq-item">
<div class="faq-q">Q: 它到底是谁做的？</div>
<div class="faq-a">匿名上线，官方未认领。最主流猜测是 MiniMax M3.1（Flash 版），因 MiniMax 同期官宣的 M3.1-Flash-Preview 配置（MoE、1M 上下文、五档推理）与它高度重合。</div>
</div>
<div class="faq-item">
<div class="faq-q">Q: 免费会有限速吗？</div>
<div class="faq-a">会。OpenRouter 对免费模型按账户累计充值额分档限速，当日免费请求计数与上限见 GET /api/v1/key 的 free_model_daily_requests，超了撞 429；BYOK 与被豁免账户不受该计数器限制。</div>
</div>
<div class="faq-item">
<div class="faq-q">Q: 适合谁、能跑什么？</div>
<div class="faq-a">适合窗口内 0 元跑长文档/大代码库/多模态理解、快速原型与 Agent 自动化的开发者。别拿它跑生产关键链路（匿名、无官方 SLA）。</div>
</div>
</div>

<h2>总结</h2>

<p>Space Bunny 的免费策略很直白：<strong>$0 输入 / $0 输出 + 1,000,000 Token 上下文 + 524,288 最大输出 + 文本/图像/视频多模态 + low~max 五档推理 + 工具调用，免费窗口到 2026-10-05</strong>。想 0 元白嫖一个"百万上下文 + 多模态 + 能跑 Agent"的模型，它是当下 OpenRouter 上最实的免费口子；匿名、身份未官宣、免费有到期日，所以赶在 10-05 前跑完任务，到期后看它转付费还是下架。价格、限速与上线/下架状态都在变化，动手前以 OpenRouter 模型页实时字段为准。</p>
"""

CONTENT_EN = """<h1>Space Bunny Free Guide: $0/$0 Anonymous Model on OpenRouter, 1M-Context Multimodal, Free Until 2026-10-05</h1>

<p>Space Bunny (OpenRouter model ID <code>stealth/space-bunny-alpha</code>) is an anonymous large model that shipped to OpenRouter and OpenCode in September 2026. The hard numbers (verified against the OpenRouter API on 2026-10-03): <strong>$0 input / $0 output</strong>, a <strong>1,000,000-token context window</strong>, <strong>524,288 max output tokens</strong>, native <strong>text + image + video</strong> multimodal input, <strong>five adjustable reasoning tiers (low / medium / high / xhigh / max, default max, reasoning mandatory)</strong>, plus <strong>tool-calling, Function Calling and JSON-Schema structured output</strong>. The model's <code>expiration_date</code> field is <strong>2026-10-05</strong>, so this free window most likely closes on that date. The community rates it "roughly GLM 5.3 Flash but faster," and within 3 days of launch it hit <strong>#1 in daily calls</strong> on both OpenRouter and OpenCode. Bottom line up front: if you want a "1M-context + multimodal + agent-capable" model on a $0, no-credit-required plan, Space Bunny is the most concrete free offer currently on OpenRouter — but it is anonymous, unclaimed by any vendor, and the free window has a real expiry, so heavy use should happen before 10-05 or you'll be watching it flip to paid or delist.</p>

<h2>Free Allowance &amp; Model Specs at a Glance</h2>

<table>
<tr><th>Item</th><th>Number / Rule</th><th>Source</th></tr>
<tr><td>Model ID</td><td><code>stealth/space-bunny-alpha</code> (OpenRouter)</td><td>OpenRouter API</td></tr>
<tr><td>Launch</td><td>2026-09-23 (API created field); hit #1 daily calls ~3 days in</td><td>OpenRouter API / ai-bot.cn</td></tr>
<tr><td>Input / output price</td><td><strong>$0 / $0</strong> (during the preview window)</td><td>OpenRouter pricing</td></tr>
<tr><td>Free window</td><td><code>expiration_date</code> = <strong>2026-10-05</strong>; may flip to paid or delist after</td><td>OpenRouter API</td></tr>
<tr><td>Context window</td><td><strong>1,000,000 tokens</strong></td><td>OpenRouter API</td></tr>
<tr><td>Max output</td><td><strong>524,288 tokens</strong> per call</td><td>OpenRouter API</td></tr>
<tr><td>Input modalities</td><td>Text + image + video to text (multimodal input)</td><td>OpenRouter API</td></tr>
<tr><td>Reasoning tiers</td><td>low / medium / high / xhigh / max, default max, reasoning mandatory</td><td>OpenRouter API</td></tr>
<tr><td>Tools / structure</td><td>Supports tool_choice, tools (Function Calling), response_format (JSON Schema)</td><td>OpenRouter API</td></tr>
<tr><td>Identity</td><td>Anonymous, architecture undisclosed; leading guess is <strong>MiniMax M3.1 (Flash)</strong>, unclaimed</td><td>ai-bot.cn</td></tr>
<tr><td>Free rate limits</td><td>OpenRouter rate-limits free models by all-time credits; check <code>free_model_daily_requests</code> on <code>GET /api/v1/key</code> for the daily counter</td><td>OpenRouter docs</td></tr>
</table>

<h2>Free Path: From Signup to a Working Call</h2>

<ol>
<li>Go to <a href="https://openrouter.ai/">OpenRouter</a> and sign up with email or Google;</li>
<li>Search <code>stealth/space-bunny-alpha</code> in the model list and confirm <strong>$0/$0</strong> plus <code>expiration_date: 2026-10-05</code> on the detail page;</li>
<li>Create an API Key on the Keys page for API use;</li>
<li>No code needed: just pick Space Bunny in OpenRouter's web Chat to test for free;</li>
<li>For API: set <code>model</code> to <code>stealth/space-bunny-alpha</code>, tune <code>reasoning_effort</code> (low for speed, max for accuracy), add tool calls, or feed image/video frames as multimodal input;</li>
<li>In OpenCode, select it as the backend model to run agentic workflows.</li>
</ol>

<p>Key reminder: <strong>the free window ends 2026-10-05</strong>. After that, <code>stealth/space-bunny-alpha</code> most likely becomes pay-per-token or is delisted from OpenRouter — so if you want it free, finish your long-document, big-repo, and multimodal jobs before the deadline. Don't assume the $0 is permanent.</p>

<h2>What You Can Run for Free (Capped by the Window + Limits)</h2>

<ul>
<li><strong>Blazing-fast inference</strong>: community-tested "roughly GLM 5.3 Flash but faster"; a full website in minutes;</li>
<li><strong>Coding / frontend</strong>: a portfolio site in minutes; a single-file 1,564-line GPU fluid-sim demo; completion rated "slightly better than GLM 5.3 Flash";</li>
<li><strong>1M long context</strong>: 1,000,000 tokens swallows a whole book or large codebase without truncation;</li>
<li><strong>Multimodal input</strong>: text / image / video, understands screenshots, design mockups, and video frames;</li>
<li><strong>Agentic automation</strong>: Function Calling, Tool Choice, and JSON structured output let you wire it into multi-step tool chains;</li>
<li><strong>Reasoning trade-off</strong>: low tier for fast simple tasks, max tier for hard ones — dial speed vs. quality yourself.</li>
</ul>

<p>None of the above costs extra (it is $0/$0 inside the window). What you actually burn is the <strong>free window + OpenRouter's free-model rate limits</strong>. Longer tasks, bigger context, and more multimodal input hit the limits faster; check the live remaining count via <code>free_model_daily_requests</code>.</p>

<h2>Identity Guess: Who Is It Actually?</h2>

<p>Space Bunny's parameter count, whether it is MoE, and its attention scheme are <strong>fully undisclosed</strong>. The most supported guess is <strong>MiniMax M3.1 (Flash)</strong>, though MiniMax has not claimed it. The corroboration: MiniMax separately announced <strong>M3.1-Flash-Preview</strong> (MoE, inheriting the M3 base, ~428B total / ~23B active per token, 1M context, five reasoning tiers, ~280ms TTFT / 210ms at Low, ~126 tokens/s generation), which overlaps heavily with Space Bunny's config. In short, anonymous models are a common "run the numbers quietly before branding" play.</p>

<h2>Competitor Free-Tier Comparison</h2>

<table>
<tr><th>Dimension</th><th>Space Bunny (stealth)</th><th>GLM-5.3 Flash (z-ai)</th></tr>
<tr><td>Price</td><td><strong>$0 / $0</strong> (window to 2026-10-05)</td><td>$0.00000015 in / $0.0000005 out (paid pricing)</td></tr>
<tr><td>Context</td><td>1,000,000 tokens, max output 524,288</td><td>1,048,576 tokens, max output 128,000</td></tr>
<tr><td>Architecture</td><td>Undisclosed (MoE suspected)</td><td>MoE, ~320B total / 18B active, sparse + linear hybrid attention</td></tr>
<tr><td>Speed</td><td>Community: "roughly GLM 5.3 Flash but faster"</td><td>~90 tok/s, TTFT ~0.2s</td></tr>
<tr><td>Multimodal</td><td>Text / image / video input</td><td>Text / image / video input</td></tr>
<tr><td>Reasoning tiers</td><td>low / medium / high / xhigh / max</td><td>low / high / max (cannot be disabled)</td></tr>
<tr><td>Identity</td><td>Anonymous (suspected MiniMax M3.1)</td><td>z-ai (public model)</td></tr>
</table>

<p>(Competitor prices/specs from the OpenRouter API, checked 2026-10-03; treat live model pages as authoritative.)</p>

<h2>Gotchas to Avoid</h2>

<ul>
<li><strong>The free window really does expire</strong>: <code>expiration_date 2026-10-05</code>; don't treat $0 as a standing allowance;</li>
<li><strong>Anonymous = no official backing</strong>: architecture and identity are unconfirmed; uptime (~99.9%) is OpenRouter's live figure, so don't run production-critical paths on it;</li>
<li><strong>Free-model rate limits</strong>: OpenRouter rate-limits free models by all-time credits; the daily remaining free count is in <code>free_model_daily_requests</code> — bursts will hit 429;</li>
<li><strong>Reasoning is mandatory</strong>: default is max; dial <code>reasoning_effort</code> down to low to save time instead of burning the window on max.</li>
</ul>

<h2>FAQ</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: Is Space Bunny free now? How is it priced?</div>
<div class="faq-a">$0 input / $0 output inside the window, no credit required. The API expiration_date is 2026-10-05, so it most likely flips to pay-per-token or delists — grab the free window before 10-05.</div>
</div>
<div class="faq-item">
<div class="faq-q">Q: What's the context and output cap?</div>
<div class="faq-a">1,000,000-token context, 524,288 max output tokens, with text + image + video multimodal input.</div>
</div>
<div class="faq-item">
<div class="faq-q">Q: Is it better than GLM 5.3 Flash?</div>
<div class="faq-a">Community testing says "roughly GLM 5.3 Flash but faster," with coding completion rated slightly ahead; max output is 524K (GLM is 128K). But it is an anonymous model with an undisclosed identity and architecture.</div>
</div>
<div class="faq-item">
<div class="faq-q">Q: Who actually built it?</div>
<div class="faq-a">Anonymous launch, unclaimed. The leading guess is MiniMax M3.1 (Flash), because MiniMax's separately announced M3.1-Flash-Preview (MoE, 1M context, five reasoning tiers) overlaps heavily with its config.</div>
</div>
<div class="faq-item">
<div class="faq-q">Q: Are there rate limits on the free access?</div>
<div class="faq-a">Yes. OpenRouter rate-limits free models by all-time credits; the daily counter and cap are in free_model_daily_requests on GET /api/v1/key — exceeding it returns 429. BYOK and exempt accounts aren't gated by that counter.</div>
</div>
<div class="faq-item">
<div class="faq-q">Q: Who is it for, and what can I run?</div>
<div class="faq-a">Developers who want a $0 way to run long documents, big codebases, multimodal understanding, fast prototyping, and agentic automation inside the window. Don't run production-critical paths on it (anonymous, no official SLA).</div>
</div>
</div>

<h2>Bottom Line</h2>

<p>Space Bunny's free policy is refreshingly numeric: <strong>$0 input / $0 output + 1,000,000-token context + 524,288 max output + text/image/video multimodal + low~max reasoning tiers + tool-calling, free window to 2026-10-05</strong>. If you want a "1M-context + multimodal + agent-capable" model on a $0 plan, it is the most concrete free offer on OpenRouter right now; anonymous, unclaimed, and with a real expiry — so finish your jobs before 10-05 and see whether it turns paid or delists. Pricing, limits, and listing status are all in flux; verify on the live OpenRouter model page before you commit.</p>
"""

FAQ_ZH = [
 {"question":"Space Bunny 现在免费吗？怎么收费？","answer":"窗口内 $0 输入 / $0 输出，免充值即可调。API 的 expiration_date 是 2026-10-05，到期后大概率转按 token 计费或下架——白嫖要赶在 10-05 前。"},
 {"question":"上下文和输出上限是多少？","answer":"上下文 1,000,000 Token，单次最大输出 524,288 Token，支持文本+图像+视频多模态输入。"},
 {"question":"它比 GLM 5.3 Flash 强在哪？","answer":"社区实测评价'约等于 GLM 5.3 Flash 但更快'，编程完成度'略胜'；且最大输出 524K（GLM 是 128K）。但它是匿名模型，身份与架构未公开。"},
 {"question":"它到底是谁做的？","answer":"匿名上线，官方未认领。最主流猜测是 MiniMax M3.1（Flash 版），因 MiniMax 同期官宣的 M3.1-Flash-Preview 配置（MoE、1M 上下文、五档推理）与它高度重合。"},
 {"question":"免费会有限速吗？","answer":"会。OpenRouter 对免费模型按账户累计充值额分档限速，当日免费请求计数与上限见 GET /api/v1/key 的 free_model_daily_requests，超了撞 429；BYOK 与被豁免账户不受该计数器限制。"},
 {"question":"适合谁、能跑什么？","answer":"适合窗口内 0 元跑长文档/大代码库/多模态理解、快速原型与 Agent 自动化的开发者。别拿它跑生产关键链路（匿名、无官方 SLA）。"},
]
FAQ_EN = [
 {"question":"Is Space Bunny free now? How is it priced?","answer":"$0 input / $0 output inside the window, no credit required. The API expiration_date is 2026-10-05, so it most likely flips to pay-per-token or delists - grab the free window before 10-05."},
 {"question":"What's the context and output cap?","answer":"1,000,000-token context, 524,288 max output tokens, with text + image + video multimodal input."},
 {"question":"Is it better than GLM 5.3 Flash?","answer":"Community testing says 'roughly GLM 5.3 Flash but faster,' with coding completion rated slightly ahead; max output is 524K (GLM is 128K). But it is an anonymous model with an undisclosed identity and architecture."},
 {"question":"Who actually built it?","answer":"Anonymous launch, unclaimed. The leading guess is MiniMax M3.1 (Flash), because MiniMax's separately announced M3.1-Flash-Preview (MoE, 1M context, five reasoning tiers) overlaps heavily with its config."},
 {"question":"Are there rate limits on the free access?","answer":"Yes. OpenRouter rate-limits free models by all-time credits; the daily counter and cap are in free_model_daily_requests on GET /api/v1/key - exceeding it returns 429. BYOK and exempt accounts aren't gated by that counter."},
 {"question":"Who is it for, and what can I run?","answer":"Developers who want a $0 way to run long documents, big codebases, multimodal understanding, fast prototyping, and agentic automation inside the window. Don't run production-critical paths on it (anonymous, no official SLA)."},
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
    "tags": ["Space Bunny", "stealth/space-bunny-alpha", "OpenRouter", "免费模型", "1M上下文", "多模态", "推理强度", "工具调用", "MiniMax M3.1", "GLM-5.3", "LLM API", "Agent"],
    "icon": "🐇",
    "excerpt_zh": "OpenRouter 匿名模型 Space Bunny（stealth/space-bunny-alpha）：$0/$0，100万 Token 上下文、524K 最大输出，文本+图像+视频多模态，low~max 五档推理 + 工具调用；上线 3 天冲上单日调用量榜首，社区评'约等于 GLM 5.3 Flash 但更快'，身份疑为 MiniMax M3.1；免费窗口到 2026-10-05。",
    "excerpt_en": "Anonymous model Space Bunny (stealth/space-bunny-alpha) on OpenRouter: $0/$0, 1M-token context, 524K max output, text+image+video multimodal, low~max reasoning + tool-calling; hit #1 daily calls in 3 days, rated 'roughly GLM 5.3 Flash but faster', suspected MiniMax M3.1; free window to 2026-10-05.",
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
