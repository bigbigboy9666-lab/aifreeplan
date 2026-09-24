#!/usr/bin/env python3
"""Generate the 'MiniMax Code CLI open-source (MIT) free-coding-agent' guide.
Data source: official GitHub README (MiniMax-AI/minimax-code), official docs
(agent.minimax.io), and the open-source announcement fetched 2026-09-23.
"""
import os
import sys
from datetime import datetime

sys.path.insert(0, '/home/ubuntu/aifreeplan/scripts')
from write_guide import generate_guide_html

SLUG = "minimax-code-cli-mit-free-agent-2026"
TODAY = datetime.now().strftime('%Y-%m-%d')

TITLE_ZH = "MiniMax Code CLI 开源白嫖攻略：MIT 协议 0 元跑终端 AI 编程 Agent，BYOK 接免费 API"
TITLE_EN = "MiniMax Code CLI Open Source: Run a Terminal AI Coding Agent for $0 (MIT + BYOK)"

DESC_ZH = "MiniMax 把 Code 终端客户端 v0.4.12 以 MIT 协议开源。工具本身 0 元，真正的白嫖打法是 BYOK——把 CLI 接到 Cerebras（100万token/天）、Groq（1000次/天）、GMI Cloud M2.5（100万TPM 免费）这些免费 API 上，白嫖一个能读代码、改代码、跑测试的完整编程 Agent。本文给安装、登录、额度、BYOK 配置和避坑全解。"
DESC_EN = "MiniMax open-sourced its Code terminal client (v0.4.12) under the MIT license. The tool itself is free, and the real free play is BYOK: point the CLI at free LLM APIs like Cerebras (1M tokens/day), Groq (1,000 req/day) or GMI Cloud M2.5 (1M TPM free) to run a full coding agent for $0. Full guide covering install, login, quotas, BYOK config, and pitfalls."

CONTENT_ZH = """<h1>MiniMax Code CLI 开源白嫖攻略：MIT 协议 0 元跑终端 AI 编程 Agent，BYOK 接免费 API</h1>
<p>MiniMax（稀宇科技）把它的终端 AI 编程工具 <strong>MiniMax Code CLI v0.4.12</strong> 以 <strong>MIT 协议</strong>正式开源了。这意味着两件事：工具本身 0 元、代码可审计、可自己改；更重要的是它原生支持 <strong>BYOK（Bring Your Own Key）</strong>——你可以把 CLI 接到任意 OpenAI / Anthropic 兼容的 API 上，包括那些<strong>免费额度</strong>的 LLM 平台。</p>
<p>先说结论：<strong>MiniMax Code CLI 免费拿（MIT 开源），但"跑代码"要烧 token。</strong>想 0 元跑，走 BYOK 接免费 API：Cerebras 每天 100 万 token、Groq 每天 1000 次、GMI Cloud M2.5 每分钟 100 万 TPM 免费不绑卡——三条路任选，就能白嫖一个能读仓库、改代码、跑测试的完整终端编程 Agent。</p>

<h2>白嫖要点速览（2026-09 官方数据）</h2>
<table>
<tr><th>项目</th><th>内容</th><th>是否免费</th></tr>
<tr><td>CLI 工具本身</td><td>v0.4.12，MIT 协议开源（npm 包 <code>@minimax-ai/code</code>）</td><td>✅ 免费</td></tr>
<tr><td>官方额度</td><td>MiniMax Token Plan / API Key，<strong>5 小时 + 每周</strong>两个额度窗口</td><td>需订阅或付费 key</td></tr>
<tr><td>BYOK 免费 API</td><td>接 Cerebras（1M token/天）/ Groq（1000次/天）/ GMI Cloud M2.5（1M TPM 免费）</td><td>✅ 0 元</td></tr>
<tr><td>评测成绩</td><td>FrontierHarness Eval 任务通过率 <strong>76.7%</strong>，成功任务中位耗时 <strong>4 分 33 秒</strong></td><td>—</td></tr>
<tr><td>运行环境</td><td>Node.js 22.19+ / 24.2+ / 25 / 26（一键脚本会自动装兼容运行时，免 sudo）</td><td>—</td></tr>
</table>
<p>关键提醒：MiniMax 官方额度不是"注册即白嫖"，走的是 Token Plan 或 API Key 计费；真正 0 元的玩法是 BYOK 接免费 API。下面拆开讲。</p>

<h2>三种装法（都 0 元）</h2>
<h3>1. 官方一键脚本（推荐，自动补 Node 运行时）</h3>
<p>macOS / Linux / WSL：</p>
<pre><code>curl -fsSL https://filecdn.minimax.chat/public/install.sh | bash</code></pre>
<p>Windows（PowerShell）：</p>
<pre><code>irm https://filecdn.minimax.chat/public/install.ps1 | iex</code></pre>
<p>脚本装到 <code>~/.minimax-code</code>（Windows 为 <code>%USERPROFILE%\\.minimax-code</code>），不需要 sudo / 管理员权限，还会按需装一个兼容的 Node.js 运行时。装完重新打开终端，跑 <code>mcode --version</code> 验证。</p>
<h3>2. npm 安装（已有 Node 的情况）</h3>
<p>要求 Node.js <strong>22.19+、24.2+、25 或 26</strong>：</p>
<pre><code>npm install -g @minimax-ai/code@latest --registry=https://registry.npmjs.org/</code></pre>
<h3>3. 注意 Alpine / musl Linux 不支持</h3>
<p>一键脚本目前不支持 Alpine 等 musl 架构的 Linux 发行版，这类系统建议手动装 Node 后走 npm。</p>

<h2>登录与额度（官方路）</h2>
<p>进项目目录后 <code>mcode login</code>（中国大陆账号）或 <code>mcode login --region global</code>（海外账号），浏览器里完成授权，回到终端用 <code>/status</code> 看账号、模型、运行时状态。</p>
<p>官方额度走两个窗口：<strong>5 小时滚动窗口 + 每周窗口</strong>，<code>/status</code> 会显示两个窗口各自剩余百分比和重置倒计时，<code>/usage</code> 看详细用量。注意这是 MiniMax 账号 / Token Plan 的额度，免费 Go/Adagio 档本身<strong>不含 coding 额度</strong>——想白嫖走下面 BYOK。</p>

<h2>白嫖核心：BYOK 接免费 API</h2>
<p>这是整篇的重点。CLI 原生支持 <code>openai-completions</code>、<code>openai-responses</code>、<code>anthropic-messages</code> 三种 API 格式，随便接一个免费 LLM API，就能让整套编程 Agent 白跑：</p>
<pre><code>export MCODE_PROVIDER_API_KEY="***"
mcode provider add --name 免费源 --base-url https://api.示例/v1 \
  --api-format openai-completions --model 模型名 \
  --context-limit 32768 --output-limit 4096 --use
mcode</code></pre>
<p><strong>三个 0 元免费源（本站已实测，见对应攻略）：</strong></p>
<table>
<tr><th>免费 API</th><th>免费额度</th><th>刷新</th><th>接入方式</th><th>适合</th></tr>
<tr><td>Cerebras</td><td>100 万 token/天</td><td>每日重置</td><td>openai-completions，无需信用卡</td><td>日常写代码、跑测试量最大</td></tr>
<tr><td>Groq</td><td>1000 次/天，RPM 30、TPM 30000</td><td>每日 UTC 0 点</td><td>openai-completions，首 token &lt;50ms</td><td>低延迟、实时交互</td></tr>
<tr><td>GMI Cloud M2.5/M2.7</td><td>100 万 TPM（Tier 1 永久，不绑卡）</td><td>按分钟计量</td><td>OpenAI 兼容，国内直连</td><td>中文场景、MiniMax 模型</td></tr>
</table>
<p>把 CLI 指到上面任一源，配合 <code>/provider</code> 切模型、<code>/model</code> 过滤，就能 0 元跑完整编程 Agent。想跨多家错峰，可以加多个 provider（比如白天 Cerebras 冲量、夜间 Groq 补延迟敏感的活）。</p>

<h2>三种入口，对应三种用法</h2>
<table>
<tr><th>入口</th><th>命令</th><th>用途</th></tr>
<tr><td>交互式 TUI</td><td><code>mcode [prompt]</code></td><td>读仓库、对话、改代码、审 diff、权限确认</td></tr>
<tr><td>Headless</td><td><code>mcode exec [prompt]</code></td><td>脚本 / CI / 批量 / 评测，支持 text / json / stream-json 输出</td></tr>
<tr><td>ACP</td><td><code>mcode acp</code></td><td>给支持 Agent Client Protocol 的编辑器当 Agent 服务</td></tr>
</table>
<p>三者共享会话、模型、provider、插件和权限控制。CI 场景用 <code>mcode exec</code> 跑批最方便——把"修这个 failing test"写进流水线，headless 一次出结果。</p>

<h2>实用技巧（省 token / 提效率）</h2>
<ul>
<li><strong>Plan Mode 先规划再动手</strong>：<code>Shift+Tab</code> 切换，<code>/plan on|off|status|view</code> 管理。复杂任务先让它出计划，避免跑偏浪费 token。</li>
<li><strong>权限模式</strong>：<code>/permission</code> 有 Ask（每次确认）/ Auto（自动判风险）/ Full access（跳过确认）三档。日常用 Auto；只在完全信任的工作区开 Full。</li>
<li><strong>给任务设预算</strong>：<code>/goal "完成迁移并跑测试" budget=50K</code>——K/M 后缀，防止 agent 无节制烧额度，白嫖党必开。</li>
<li><strong>主任务运行时开侧问</strong>：<code>/btw 为什么选这个实现？</code> 不打断主任务，临时查个细节。</li>
<li><strong>@ 引用文件/目录、Ctrl+V 贴图贴视频</strong>，把上下文喂给 agent。</li>
<li><strong>插件市场</strong>：<code>mcode plugin marketplace list</code> / <code>mcode plugin add 名称@official</code>，加搜索、MCP 等能力。</li>
</ul>

<h2>评测数据说明</h2>
<p>官方在 FrontierHarness Eval 上报告：本轮 <strong>76.7% 任务通过率</strong>（30 道任务里 23 道通过、4 道失败、3 道超时无评分），成功任务<strong>中位耗时 4 分 33 秒</strong>，两项指标均优于报告所列公开基线。注意这是第三方评测，口径和任务时限跟公开榜单有差异，只作数值参考，不代表官方排名——宣传时别拿这个数当绝对结论。</p>

<h2>限制与坑</h2>
<ul>
<li><strong>"免费"分两层</strong>：工具（MIT）永远 0 元；但官方跑模型要钱。想 0 元只能 BYOK 接免费 API，别指望注册 MiniMax 送 coding 额度。</li>
<li><strong>免费 Go/Adagio 档不含 coding 额度</strong>：和 Kimi Code Desktop 的 Go 档一样，免费档没有编程额度，0 元写代码走 Gemini CLI / DeepSeek-TUI / 通义灵码，或本文的 BYOK 路线。</li>
<li><strong>额度会滚动消耗</strong>：5 小时 + 每周两个窗口，跑满就限流；BYOK 接免费 API 时受的是那个 API 自己的日限额（Cerebras 1M/天、Groq 1000/天、GMI 按分钟 TPM）。</li>
<li><strong>Alpine / musl Linux 不支持一键安装</strong>，得手动装 Node 走 npm。</li>
<li><strong>数据目录默认 <code>~/.minimax</code></strong>，BYOK 的自定义 provider 存在这里，多套 CLI 共用同一目录会串配置。</li>
</ul>

<h2>FAQ</h2>
<div class="faq-section">
<div class="faq-item"><div class="faq-q">MiniMax Code CLI 真的完全免费吗？</div><div class="faq-a">工具本身是：v0.4.12 以 MIT 协议开源，安装、运行、二次开发都 0 元。但"跑模型"要 token——官方走 Token Plan / API Key 计费。想 0 元跑，用 BYOK 接免费 API（Cerebras 100 万 token/天、Groq 1000 次/天、GMI Cloud M2.5 100 万 TPM 免费）。</div></div>
<div class="faq-item"><div class="faq-q">怎么白嫖一个完整的编程 Agent？</div><div class="faq-a">三步：① 一键脚本装 CLI（自动补 Node 运行时）；② <code>mcode provider add</code> 接一个免费 API；③ <code>/goal ... budget=50K</code> 设预算开跑。全程 0 元，能读仓库、改代码、跑测试。</div></div>
<div class="faq-item"><div class="faq-q">BYOK 支持哪些 API 格式？</div><div class="faq-a">支持 <code>openai-completions</code>、<code>openai-responses</code>、<code>anthropic-messages</code> 三种。OpenAI 兼容的免费 API（Cerebras、Groq、GMI）直接用第一种；Anthropic 兼容的走第三种。本地/自托管模型要加 <code>--context-limit 32768 --output-limit 4096</code>。</div></div>
<div class="faq-item"><div class="faq-q">和 Gemini CLI、Kimi Code Desktop 比，选哪个？</div><div class="faq-a">纯 0 元、不挑模型，Gemini CLI 自带免费额度最省事；要国内直连 + MiniMax 模型，走 GMI Cloud M2.5；Kimi Code Desktop 是桌面 GUI 四档订阅（¥49 起），终端党更灵活的是 MiniMax Code CLI（开源 + BYOK）。</div></div>
<div class="faq-item"><div class="faq-q">76.7% 通过率是什么水平？</div><div class="faq-a">第三方 FrontierHarness Eval 单轮成绩，30 道里 23 过 4 挂 3 超时无评分，成功任务中位耗时 4 分 33 秒。能跑主流 coding 任务，但别当官方榜单排名看——口径和时限跟公开榜单不一致。</div></div>
</div>

<h2>总结</h2>
<p>MiniMax Code CLI 开源后，"终端 AI 编程 Agent"这件过去要么付费、要么折腾的事，现在<strong>0 元可落地</strong>：MIT 工具 + BYOK 接免费 API。想白嫖最划算，就 <code>Cerebras 冲量 + Groq 补延迟</code> 错峰，开 <code>/goal budget</code> 控额度。工具永久免费，免费 API 额度每天/每周/每分钟重置——一个小项目基本零成本跑完。</p>
<p>相关白嫖源攻略：<a href="/zh/guides/cerebras-free-api-guide">Cerebras 免费 API</a>、<a href="/zh/guides/groq-free-lpu-inference-api-2026">Groq 免费 LPU</a>、<a href="/zh/guides/gmi-cloud-minimax-free-guide">GMI Cloud 跑 MiniMax</a>、<a href="/zh/guides/free-ai-coding-tools-comparison">免费 AI 编程工具横评</a>、<a href="/zh/guides/kimi-code-desktop-free-guide-2026">Kimi Code Desktop</a>。</p>
<p><em>本文数据更新于 2026-09-23，版本与免费额度可能调整，以官网 / 仓库最新说明为准。</em></p>"""

CONTENT_EN = """<h1>MiniMax Code CLI Open Source: Run a Terminal AI Coding Agent for $0 (MIT + BYOK)</h1>
<p>MiniMax open-sourced its terminal AI coding tool, <strong>MiniMax Code CLI v0.4.12</strong>, under the <strong>MIT</strong> license. That means two things: the tool itself is free, the code is auditable and modifiable; and more importantly it ships native <strong>BYOK (Bring Your Own Key)</strong> support — you can point the CLI at any OpenAI / Anthropic-compatible API, including ones with a <strong>free tier</strong>.</p>
<p>Bottom line: <strong>MiniMax Code CLI is free (MIT open source), but running it burns tokens.</strong> To run it for $0, go BYOK against a free LLM API — Cerebras (1M tokens/day), Groq (1,000 req/day), or GMI Cloud M2.5 (1M TPM free, no card) — and you get a full terminal coding agent that reads repos, edits code, and runs tests, at zero cost.</p>

<h2>Free-Quota Snapshot (official data, Sep 2026)</h2>
<table>
<tr><th>Item</th><th>Detail</th><th>Free?</th></tr>
<tr><td>CLI tool itself</td><td>v0.4.12, MIT open source (npm <code>@minimax-ai/code</code>)</td><td>✅ Free</td></tr>
<tr><td>Official quota</td><td>MiniMax Token Plan / API Key, <strong>5-hour + weekly</strong> quota windows</td><td>Paid / subscription</td></tr>
<tr><td>BYOK free API</td><td>Cerebras (1M tok/day), Groq (1,000 req/day), GMI Cloud M2.5 (1M TPM free)</td><td>✅ $0</td></tr>
<tr><td>Eval score</td><td>FrontierHarness Eval <strong>76.7%</strong> task pass, median success time <strong>4m 33s</strong></td><td>—</td></tr>
<tr><td>Runtime</td><td>Node.js 22.19+ / 24.2+ / 25 / 26 (one-line installer auto-provisions a compatible runtime, no sudo)</td><td>—</td></tr>
</table>
<p>Key note: MiniMax's own quota is not "free on signup" — it bills via Token Plan or API key. The genuinely $0 route is BYOK against a free API. Here's how.</p>

<h2>Three install paths (all $0)</h2>
<h3>1. Official one-line installer (recommended)</h3>
<p>macOS / Linux / WSL:</p>
<pre><code>curl -fsSL https://filecdn.minimax.chat/public/install.sh | bash</code></pre>
<p>Windows (PowerShell):</p>
<pre><code>irm https://filecdn.minimax.chat/public/install.ps1 | iex</code></pre>
<p>It installs to <code>~/.minimax-code</code> (or <code>%USERPROFILE%\\.minimax-code</code> on Windows), needs no sudo / admin, and provisions a compatible Node.js runtime on demand. Reopen your terminal and run <code>mcode --version</code> to verify.</p>
<h3>2. npm (if you already have Node)</h3>
<p>Requires Node.js <strong>22.19+, 24.2+, 25, or 26</strong>:</p>
<pre><code>npm install -g @minimax-ai/code@latest --registry=https://registry.npmjs.org/</code></pre>
<h3>3. Alpine / musl Linux is not supported by the installer</h3>
<p>Use a manual Node install plus npm on those systems.</p>

<h2>Sign-in and official quota</h2>
<p>In a project dir, run <code>mcode login</code> (mainland China) or <code>mcode login --region global</code>; finish auth in the browser, then check <code>/status</code>.</p>
<p>Official quota runs on two windows: a <strong>rolling 5-hour window + a weekly window</strong>. <code>/status</code> shows the remaining percentage and reset countdown for each; <code>/usage</code> gives detail. This is the MiniMax account / Token Plan quota — the free Go/Adagio tiers carry <strong>no coding quota</strong>, so for $0 go BYOK below.</p>

<h2>The free play: BYOK against a free API</h2>
<p>This is the core. The CLI natively supports <code>openai-completions</code>, <code>openai-responses</code>, and <code>anthropic-messages</code> API formats — plug in any free LLM API and the whole coding agent runs for $0:</p>
<pre><code>export MCODE_PROVIDER_API_KEY="***"
mcode provider add --name free-src --base-url https://api.example.com/v1 \
  --api-format openai-completions --model model-id \
  --context-limit 32768 --output-limit 4096 --use
mcode</code></pre>
<p><strong>Three $0 free sources (hands-on, see the linked guides):</strong></p>
<table>
<tr><th>Free API</th><th>Free quota</th><th>Refresh</th><th>Access</th><th>Best for</th></tr>
<tr><td>Cerebras</td><td>1M tokens/day</td><td>daily reset</td><td>openai-completions, no credit card</td><td>highest volume coding / tests</td></tr>
<tr><td>Groq</td><td>1,000 req/day, RPM 30, TPM 30,000</td><td>daily at UTC 00:00</td><td>openai-completions, first-token &lt;50ms</td><td>low latency, interactive</td></tr>
<tr><td>GMI Cloud M2.5/M2.7</td><td>1M TPM (Tier 1, permanent, no card)</td><td>per-minute metering</td><td>OpenAI-compatible, direct in CN</td><td>Chinese scenarios, MiniMax models</td></tr>
</table>
<p>Point the CLI at any of these and use <code>/provider</code> to switch and <code>/model</code> to filter, and you run a full coding agent for $0. To stagger across vendors, add several providers (e.g., Cerebras for volume by day, Groq for latency-sensitive work overnight).</p>

<h2>Three entry points, three use cases</h2>
<table>
<tr><th>Entry</th><th>Command</th><th>For</th></tr>
<tr><td>Interactive TUI</td><td><code>mcode [prompt]</code></td><td>read repos, converse, edit code, review diffs, permission prompts</td></tr>
<tr><td>Headless</td><td><code>mcode exec [prompt]</code></td><td>scripts / CI / batch / evals; text / json / stream-json output</td></tr>
<tr><td>ACP</td><td><code>mcode acp</code></td><td>serve the agent to editors that speak the Agent Client Protocol</td></tr>
</table>
<p>All three share sessions, models, providers, plugins, and permission controls. For CI, headless <code>mcode exec</code> is the cleanest — bake "fix this failing test" into the pipeline and get one-shot results.</p>

<h2>Tips (save tokens, work faster)</h2>
<ul>
<li><strong>Plan Mode before acting</strong>: <code>Shift+Tab</code> to toggle, <code>/plan on|off|status|view</code> to manage. Let it plan on complex tasks to avoid burning tokens going the wrong way.</li>
<li><strong>Permission modes</strong>: <code>/permission</code> offers Ask (confirm each) / Auto (auto-classify risk) / Full access (skip checks). Use Auto day-to-day; Full only in workspaces you fully trust.</li>
<li><strong>Set a task budget</strong>: <code>/goal "finish the migration and run tests" budget=50K</code> — K/M suffixes cap spend; a must for free-tier users.</li>
<li><strong>Side questions while the main task runs</strong>: <code>/btw why this implementation?</code> without interrupting the main task.</li>
<li><strong>@ to reference files/dirs, Ctrl+V to paste images/video</strong> into context.</li>
<li><strong>Plugin marketplace</strong>: <code>mcode plugin marketplace list</code> / <code>mcode plugin add name@official</code> for search, MCP, and more.</li>
</ul>

<h2>Eval numbers, with caveats</h2>
<p>Official FrontierHarness Eval report: <strong>76.7% task pass rate</strong> (23 passed, 4 failed, 3 timed out unscored of 30) with a <strong>4m 33s median</strong> success time — both ahead of the public baselines listed. This is a third-party eval; its scoring and task-time windows differ from public leaderboards, so treat the number as a reference, not an official ranking.</p>

<h2>Limits and traps</h2>
<ul>
<li><strong>"Free" is two-layered</strong>: the tool (MIT) is permanently $0; but running the model costs tokens. Official execution is billed via Token Plan / API key. For $0, go BYOK against a free API — don't expect free coding quota from signing up.</li>
<li><strong>Free Go/Adagio tiers have no coding quota</strong> (same as Kimi Code Desktop's Go tier). For $0 coding, use Gemini CLI / DeepSeek-TUI / Tongyi Lingma, or this BYOK route.</li>
<li><strong>Quota drains on rolling windows</strong> (5-hour + weekly); free API BYOK instead is capped by that API's own daily limit (Cerebras 1M/day, Groq 1,000/day, GMI per-minute TPM).</li>
<li><strong>Alpine / musl Linux can't use the one-line installer</strong> — manual Node + npm.</li>
<li><strong>Data dir defaults to <code>~/.minimax</code></strong>; BYOK custom providers live here, so multiple CLI installs sharing it will cross-contaminate config.</li>
</ul>

<h2>FAQ</h2>
<div class="faq-section">
<div class="faq-item"><div class="faq-q">Is MiniMax Code CLI really completely free?</div><div class="faq-a">The tool is: v0.4.12 is MIT open source, so install, run, and modify are all $0. But "running the model" costs tokens — official runs bill via Token Plan / API key. To run for $0, use BYOK against a free API (Cerebras 1M tokens/day, Groq 1,000 req/day, GMI Cloud M2.5 1M TPM free).</div></div>
<div class="faq-item"><div class="faq-q">How do I run a full coding agent for $0?</div><div class="faq-a">Three steps: ① one-line installer (auto-provisions Node); ② <code>mcode provider add</code> against a free API; ③ <code>/goal ... budget=50K</code> to cap spend and go. $0 end-to-end, and it reads repos, edits code, and runs tests.</div></div>
<div class="faq-item"><div class="faq-q">Which API formats does BYOK support?</div><div class="faq-a"><code>openai-completions</code>, <code>openai-responses</code>, and <code>anthropic-messages</code>. Use the first for OpenAI-compatible free APIs (Cerebras, Groq, GMI) and the third for Anthropic-compatible ones. For local/self-hosted models, add <code>--context-limit 32768 --output-limit 4096</code>.</div></div>
<div class="faq-item"><div class="faq-q">How does it compare to Gemini CLI and Kimi Code Desktop?</div><div class="faq-a">For pure $0 with no model choice, Gemini CLI's built-in free quota is easiest. For direct access in China with MiniMax models, use GMI Cloud M2.5. Kimi Code Desktop is a desktop GUI with four subscription tiers (from ¥49); for terminal users, MiniMax Code CLI (open source + BYOK) is more flexible.</div></div>
<div class="faq-item"><div class="faq-q">What's a 76.7% pass rate?</div><div class="faq-a">A third-party FrontierHarness Eval single round: 23 of 30 passed, 4 failed, 3 timed out, 4m 33s median success time. It handles mainstream coding tasks, but don't read it as an official leaderboard ranking — scoring and time limits differ from public boards.</div></div>
</div>

<h2>Bottom line</h2>
<p>Now that MiniMax Code CLI is open source, "terminal AI coding agent" — something that used to mean paying or heavy setup — becomes a <strong>zero-cost</strong> thing to run: an MIT tool + BYOK against a free API. To get the most value, stagger Cerebras for volume with Groq for latency, and cap spend with <code>/goal budget</code>. The tool is permanently free, and the free API quotas reset daily / weekly / per-minute — a small project runs for essentially nothing.</p>
<p>Related free sources: <a href="/en/guides/cerebras-free-api-guide">Cerebras free API</a>, <a href="/en/guides/groq-free-lpu-inference-api-2026">Groq free LPU</a>, <a href="/en/guides/gmi-cloud-minimax-free-guide">GMI Cloud with MiniMax</a>, <a href="/en/guides/free-ai-coding-tools-comparison">Free AI coding tools compared</a>, <a href="/en/guides/kimi-code-desktop-free-guide-2026">Kimi Code Desktop</a>.</p>
<p><em>Figures updated 2026-09-23; versions and free quotas may change — check the official site / repo for the latest.</em></p>"""

FAQ_ZH = "[{\"@type\":\"Question\",\"name\":\"MiniMax Code CLI 真的完全免费吗？\",\"acceptedAnswer\":{\"@type\":\"Answer\",\"text\":\"工具本身是：v0.4.12 以 MIT 协议开源，安装、运行、二次开发都 0 元。但跑模型要 token——官方走 Token Plan / API Key 计费。想 0 元跑，用 BYOK 接免费 API（Cerebras 100 万 token/天、Groq 1000 次/天、GMI Cloud M2.5 100 万 TPM 免费）。\"}},{\"@type\":\"Question\",\"name\":\"怎么白嫖一个完整的编程 Agent？\",\"acceptedAnswer\":{\"@type\":\"Answer\",\"text\":\"三步：一键脚本装 CLI（自动补 Node 运行时）；mcode provider add 接一个免费 API；/goal ... budget=50K 设预算开跑。全程 0 元，能读仓库、改代码、跑测试。\"}},{\"@type\":\"Question\",\"name\":\"BYOK 支持哪些 API 格式？\",\"acceptedAnswer\":{\"@type\":\"Answer\",\"text\":\"openai-completions、openai-responses、anthropic-messages 三种。OpenAI 兼容的免费 API（Cerebras、Groq、GMI）用第一种；Anthropic 兼容的用第三种；本地/自托管加 --context-limit 32768 --output-limit 4096。\"}},{\"@type\":\"Question\",\"name\":\"和 Gemini CLI、Kimi Code Desktop 选哪个？\",\"acceptedAnswer\":{\"@type\":\"Answer\",\"text\":\"纯 0 元不挑模型，Gemini CLI 自带免费额度最省事；国内直连 MiniMax 模型走 GMI Cloud M2.5；终端党要更灵活的开源 + BYOK，选 MiniMax Code CLI。\"}},{\"@type\":\"Question\",\"name\":\"76.7% 通过率什么水平？\",\"acceptedAnswer\":{\"@type\":\"Answer\",\"text\":\"第三方 FrontierHarness Eval 单轮：30 道里 23 过 4 挂 3 超时无评分，成功任务中位耗时 4 分 33 秒。能跑主流 coding 任务，但别当官方榜单排名看。\"}}]"

FAQ_EN = "[{\"@type\":\"Question\",\"name\":\"Is MiniMax Code CLI really completely free?\",\"acceptedAnswer\":{\"@type\":\"Answer\",\"text\":\"The tool is: v0.4.12 is MIT open source, so install, run, and modify are all $0. But running the model costs tokens — official runs bill via Token Plan / API key. To run for $0, use BYOK against a free API (Cerebras 1M tokens/day, Groq 1,000 req/day, GMI Cloud M2.5 1M TPM free).\"}},{\"@type\":\"Question\",\"name\":\"How do I run a full coding agent for $0?\",\"acceptedAnswer\":{\"@type\":\"Answer\",\"text\":\"Three steps: one-line installer (auto-provisions Node); mcode provider add against a free API; /goal ... budget=50K to cap spend. $0 end-to-end, and it reads repos, edits code, and runs tests.\"}},{\"@type\":\"Question\",\"name\":\"Which API formats does BYOK support?\",\"acceptedAnswer\":{\"@type\":\"Answer\",\"text\":\"openai-completions, openai-responses, and anthropic-messages. Use the first for OpenAI-compatible free APIs (Cerebras, Groq, GMI) and the third for Anthropic-compatible ones; add --context-limit 32768 --output-limit 4096 for local/self-hosted.\"}},{\"@type\":\"Question\",\"name\":\"How does it compare to Gemini CLI and Kimi Code Desktop?\",\"acceptedAnswer\":{\"@type\":\"Answer\",\"text\":\"For pure $0, Gemini CLI's built-in free quota is easiest. For direct access in China with MiniMax models, use GMI Cloud M2.5. For a more flexible open-source + BYOK terminal tool, choose MiniMax Code CLI.\"}},{\"@type\":\"Question\",\"name\":\"What is a 76.7% pass rate?\",\"acceptedAnswer\":{\"@type\":\"Answer\",\"text\":\"A third-party FrontierHarness Eval single round: 23 of 30 passed, 4 failed, 3 timed out, 4m 33s median success time. It handles mainstream coding tasks but is not an official leaderboard ranking.\"}}]"

zh_html, en_html = generate_guide_html(
    SLUG, TITLE_ZH, TITLE_EN, DESC_ZH, DESC_EN,
    CONTENT_ZH, CONTENT_EN, FAQ_ZH, FAQ_EN, TODAY
)

os.makedirs('/home/ubuntu/aifreeplan/zh/guides', exist_ok=True)
os.makedirs('/home/ubuntu/aifreeplan/en/guides', exist_ok=True)
with open(f'/home/ubuntu/aifreeplan/zh/guides/{SLUG}.html', 'w', encoding='utf-8') as f:
    f.write(zh_html)
with open(f'/home/ubuntu/aifreeplan/en/guides/{SLUG}.html', 'w', encoding='utf-8') as f:
    f.write(en_html)

print(f"Generated {SLUG} (date {TODAY})")
print(f"  zh content bytes: {len(CONTENT_ZH.encode('utf-8'))}")
print(f"  en content bytes: {len(CONTENT_EN.encode('utf-8'))}")
