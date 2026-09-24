#!/usr/bin/env python3
"""Generate the 'Kimi Code Desktop' guide (new desktop AI coding agent, launched 2026-09-22).
Data sources: ai-bot.cn daily news (9/22), kimi.com/code, kimi.com/help/membership/membership-pricing,
kimi.com/code/docs/kimi-code/membership.html — fetched 2026-09-22.
"""
import os, sys, json
from datetime import datetime

sys.path.insert(0, '/home/ubuntu/aifreeplan/scripts')
from write_guide import generate_guide_html

SLUG = "kimi-code-desktop-free-guide-2026"
TODAY = "2026-09-22"

TITLE_ZH = "Kimi Code Desktop 上手攻略：桌面端 AI 编程 Agent，四档订阅、K3 模型与免费替代（2026）"
TITLE_EN = "Kimi Code Desktop Guide: Desktop AI Coding Agent, 4 Tiers, K3 Model & Free Alternatives (2026)"

DESC_ZH = "月之暗面 9/22 发布 Kimi Code 桌面客户端，把 Agent 编程从命令行搬到 GUI，支持 Plan/Goal/Swarm/Tower 四种模式。本文讲清 ¥49/99/199/699 四档订阅额度、K3 模型门槛、每 5 小时速率限制，以及 Gemini CLI、DeepSeek-TUI、通义灵码等 0 元替代。"
DESC_EN = "Moonshot AI launched Kimi Code Desktop on Sep 22, moving Agent coding from the CLI into a GUI with Plan/Goal/Swarm/Tower modes. This guide explains the four paid tiers (49/99/199/699 CNY), K3 model gating, the 5-hour rate window, and zero-cost alternatives like Gemini CLI, DeepSeek-TUI and Tongyi Lingma."

CONTENT_ZH = """<h1>Kimi Code Desktop 上手攻略：桌面端 AI 编程 Agent，四档订阅、K3 模型与免费替代（2026）</h1>

<p>2026 年 9 月 22 日，月之暗面（Moonshot AI）把 <strong>Kimi Code 桌面客户端「Kimi Code Desktop」正式发布，macOS 与 Windows 同步上线</strong>。它把 Kimi Code 的 AI Agent 编程能力从命令行搬进图形界面：在一个窗口里表达需求、跟踪进度、运行调试、处理 Git 与 PR，让 AI 协作的过程「可见、可控」。本文基于 9 月 22 日当天 ai-bot.cn 快讯与 kimi.com 官网定价页，把四种工作模式、四档订阅价格与额度、K3 模型门槛、速率限制一次讲清，并给出 0 元替代方案，帮你判断要不要订、订哪一档。</p>

<p>先说结论：<strong>想 0 元写代码，别订 Kimi，走 Gemini CLI / DeepSeek-TUI / 通义灵码免费额度；要国产中文 + 桌面 GUI + 多 Agent 并行的体验，最低 ¥49/月 的 Andante（Plus）档起步够用，重度多 Agent 协作才上 ¥199/¥699。</strong>免费 Go 档没有 coding 额度，「Kimi 免费」不等于「Kimi Code 免费」。</p>

<h2>四种工作模式：一次订阅，全端畅写</h2>

<p>Kimi Code Desktop 的核心是<strong>一个桌面窗口跑完「写代码 → 跑命令 → 验证 → 审阅 → 合并」全流程</strong>，内置终端、浏览器、Git 状态面板和截图/网页元素标注。它不是单纯的编辑器，而是「GUI 优先的 Agent 工作台」，提供四种工作模式：</p>

<table>
<tr><th>模式</th><th>行为</th><th>适合场景</th></tr>
<tr><td><strong>Plan</strong></td><td>先出执行计划，经你确认后再动手</td><td>大型重构、想先看方案再放行的任务</td></tr>
<tr><td><strong>Goal</strong></td><td>围绕目标持续自主推进，少打断</td><td>从 0 到 1 搭建小型应用、端到端交付</td></tr>
<tr><td><strong>Swarm</strong></td><td>主 Agent 拆任务，调度多个 Subagent 分工</td><td>多模块并行的中大型任务</td></tr>
<tr><td><strong>Tower</strong></td><td>多个 Agent 并行协作（实验性）</td><td>可并行推进的多条工作流</td></tr>
</table>

<p>其他工程化能力：聊天里的文件路径可直接点开预览；截图或网页元素「指哪改哪」，减少沟通成本；标签页、置顶、AI 自动命名、全局搜索管理多会话；CLI 已有的本地任务<strong>自动同步到桌面端</strong>，老用户零成本平滑迁移，原 Agent 能力完整保留。</p>

<h2>订阅档位与额度（官方 2026-09-22 数据）</h2>

<p>Kimi Code 是 Kimi 会员权益的一部分，<strong>随会员订阅提供，与 Kimi 会员共享同一套月度额度池</strong>，CLI、VS Code 插件、桌面端和第三方工具发起的请求都计入。免费 Go（Adagio）档<strong>没有 coding 额度</strong>，要用 Kimi Code 编程必须订付费档。官网当前四档付费价（音乐术语档位名，定价不变）：</p>

<table>
<tr><th>档位（新名）</th><th>价格</th><th>Agent 用量（月额度全投单一功能估算）</th><th>并行 / 集群</th><th>关键额度</th></tr>
<tr><td><strong>Andante（Plus）</strong></td><td>¥49/月</td><td>约 30 个</td><td>Agent 优先生成队列（4 倍速）</td><td>数据库 1000 次；20 项目 / 20GB 存储；15+ 插件</td></tr>
<tr><td><strong>Moderato</strong></td><td>¥99/月</td><td>约 60 个</td><td>任务并行 2 个；集群 25 次（2 子任务）</td><td>数据库 2000 次；梦境记忆、自进化技能</td></tr>
<tr><td><strong>Allegretto（Pro）</strong></td><td>¥199/月</td><td>约 150 个</td><td>任务并行 2 个；集群 50 次（4 子任务）</td><td>数据库 5000 次；目标模式；专属 Kimi Claw（10 群聊）；<strong>K3 1M 上下文 &amp; 高速版门槛</strong></td></tr>
<tr><td><strong>Allegro</strong></td><td>¥699/月</td><td>约 360 个</td><td>任务并行 4 个；集群 120 次（8 子任务）</td><td>数据库 12000 次；<strong>百万 Token 长上下文</strong>；100 项目 / 50GB</td></tr>
</table>

<p><strong>几条必须知道的规则：</strong></p>
<ul>
<li><strong>共享额度池</strong>：所有 Kimi 会员功能（网站部署、深度研究、PPT、Kimi Code、Kimi Work、Kimi Claw、K3 等）共用一个月度额度池，按实际 token 消耗扣。某功能把额度用完，会影响其他功能。</li>
<li><strong>Kimi Code 专属速率窗口</strong>：Kimi Code 另有「每 5 小时」+「每周」两个频率窗口，只作用 Kimi Code，不影响其他功能；短时间请求过密会触发限流，窗口滚动后自动恢复。</li>
<li><strong>模型门槛</strong>：K3 模型需 <strong>Moderato（¥99）及以上</strong>可调用；K3 的 <strong>1M 上下文</strong>与<strong>高速版</strong>需 <strong>Allegretto（¥199）及以上</strong>。</li>
<li><strong>档位名新老两套</strong>：官网定价页用 Andante/Moderato/Allegretto/Allegro，文档侧对应 Go / Plus / Pro 等叫法，<strong>定价不变</strong>，老套餐可继续用，是否升级自选，以官网实时为准。</li>
<li><strong>年付更省</strong>：连续包年最高立省 <strong>¥1,680</strong>。</li>
</ul>

<h2>和「免费 / 低价」编程 Agent 横向对比</h2>

<p>Kimi Code Desktop 走「国产中文 + 桌面 GUI + 多 Agent」路线，但它<strong>不是免费</strong>。如果你要的是 0 元写代码，下面这些是更划算的替代（均为 2026 年快照，额度随时可能调整）：</p>

<table>
<tr><th>工具</th><th>免费额度</th><th>形态</th><th>适合谁</th><th>入门付费</th></tr>
<tr><td><strong>Kimi Code Desktop</strong></td><td>❌ 免费 Go 档无 coding 额度</td><td>桌面 GUI 多 Agent</td><td>要国产中文 GUI + Swarm/Tower 多 Agent 协作</td><td>¥49/月起</td></tr>
<tr><td><strong>Gemini CLI（Google）</strong></td><td>✅ 免费 AI Studio 额度（Flash 档请求免费）</td><td>终端 Agent</td><td>0 元跑通主流 Agent 编程</td><td>—</td></tr>
<tr><td><strong>DeepSeek-TUI</strong></td><td>✅ 开源 MIT，DeepSeek 官方 API 免费/低价</td><td>终端「DeepSeek 版 Claude Code」</td><td>喜欢终端 + 国产模型</td><td>DeepSeek API 极低价</td></tr>
<tr><td><strong>通义灵码 / Qwen</strong></td><td>✅ 个人版免费额度</td><td>IDE 插件</td><td>国内 IDE 生态、中文补全</td><td>企业版另计</td></tr>
<tr><td><strong>Cursor</strong></td><td>有限免费额度</td><td>VS Code 系 IDE</td><td>编辑器补全标杆</td><td>Pro 约 $20/月</td></tr>
<tr><td><strong>Windsurf / Devin</strong></td><td>有限免费额度</td><td>AI 原生 IDE</td><td>多会话并行 Agent 管理</td><td>约 $15/月起</td></tr>
</table>

<p>判断逻辑很简单：<strong>预算为 0 → Gemini CLI / DeepSeek-TUI / 通义灵码；预算 ¥49 且要桌面 GUI + 多 Agent 协作 → Kimi Code Andante；多 Agent 重度并发、百万上下文 → Allegretto / Allegro。</strong>别为「GUI 好看」付 ¥699，先看你的任务量。</p>

<h2>安装到上手（5 步）</h2>
<ol>
<li><strong>下载</strong>：访问 <a href="https://www.kimi.com/code">kimi.com/code</a>，下载对应 macOS（Apple / Intel）或 Windows 版本并安装。</li>
<li><strong>登录</strong>：一键登录 Kimi 账号；或在设置里配置第三方模型供应商。</li>
<li><strong>选工作区</strong>：新建会话后在输入框下方选本地项目文件夹，桌面端按工作区整理会话。</li>
<li><strong>发起任务</strong>：用自然语言描述需求，按任务特点选 Plan / Goal / Swarm / Tower。</li>
<li><strong>确认与收尾</strong>：Plan 模式先审计划再执行；用内置终端跑构建/测试、内置浏览器预览；Git 区看分支与 PR 进度，完成开发闭环。</li>
</ol>

<h2>省钱 &amp; 避坑</h2>
<ol>
<li><strong>别被「Kimi 免费」骗了</strong>：Go/Adagio 免费档没有 coding 额度，写代码必须 ¥49 起。免费党的正确姿势是转去 Gemini CLI / DeepSeek-TUI / 通义灵码。</li>
<li><strong>¥49 档日常够</strong>：约 30 个 Agent + 数据库 1000 次 + 20 项目，中小项目个人用够用；先订最低档，跑满再升级。</li>
<li><strong>共享池要留神</strong>：PPT、深度研究、Kimi Claw 都在扣同一个池，额度被别的功能烧光，Kimi Code 也会跟着冻结。</li>
<li><strong>5 小时窗口别硬刚</strong>：短时间狂请求会触发限流，等 5 小时窗口滚动自动恢复，不是永久锁死。</li>
<li><strong>Claw 云主机有隐性扣费</strong>：部署了 Kimi Claw 的，云主机沙箱按运行时长每天扣约会员额度的 0.6%（下午 4 点结算），待机也计费。</li>
<li><strong>年付划算</strong>：确认长期用就选连续包年，最高省 ¥1,680。</li>
</ol>

<h2>FAQ</h2>
<div class="faq-section">
<div class="faq-item"><div class="faq-q">Kimi Code Desktop 真的完全免费吗？</div><div class="faq-a">不是。免费 Go/Adagio 档没有 coding 额度，用 Kimi Code 编程最低要订 ¥49/月（Andante/Plus）。0 元写代码建议走 Gemini CLI、DeepSeek-TUI 或通义灵码的免费额度。</div></div>
<div class="faq-item"><div class="faq-q">¥49 的 Andante 档一个月大概能写多少代码？</div><div class="faq-a">官方按「月额度全投单一功能」估算约 30 个 Agent 用量，外加专业数据库 1000 次调用、20 个项目 / 20GB 存储、15+ 精选插件。中小项目个人日常够用，跑满会触发 5 小时速率窗口限流。</div></div>
<div class="faq-item"><div class="faq-q">K3 模型和 1M 上下文分别在哪个档能用？</div><div class="faq-a">K3 模型需 ¥99（Moderato）及以上可调用；K3 的 1M 超长上下文和高速版需 ¥199（Allegretto/Pro）及以上。顶档 ¥699（Allegro）才支持百万 Token 长上下文。</div></div>
<div class="faq-item"><div class="faq-q">「每 5 小时 / 每周」限制是什么？</div><div class="faq-a">Kimi Code 在共享月度额度之外，另有每 5 小时和每周两个频率窗口（仅作用 Kimi Code，不影响 PPT、深度研究等功能）。短时间请求过密触发限流后，等窗口滚动自动恢复，不是封号或永久限制。</div></div>
<div class="faq-item"><div class="faq-q">和 Cursor、Windsurf 比，Kimi Code Desktop 强在哪？</div><div class="faq-a">Kimi Code Desktop 强在国产中文生态 + 桌面 GUI 多 Agent 协作（Swarm 子任务分工、Tower 多 Agent 并行）+ 与 Kimi 会员共享额度。Cursor 的编辑器补全和 Tab 预测仍是标杆；预算 0 或要极致补全体验时，免费方案更划算。</div></div>
<div class="faq-item"><div class="faq-q">老用户从 Kimi Code CLI 迁到桌面端要重新配置吗？</div><div class="faq-a">不用。CLI 已有的本地任务会自动同步到桌面端，原有 Agent 能力完整保留，零成本平滑过渡；模型、供应商、权限、插件等配置都能图形化调整。</div></div>
</div>

<h2>总结</h2>
<p>Kimi Code Desktop 是月之暗面把 Kimi Code 的 Agent 编程能力做进图形界面的桌面客户端，2026 年 9 月 22 日 macOS/Windows 同步上线，主打「一个窗口跑完全流程 + Plan/Goal/Swarm/Tower 四种模式 + 多 Agent 并行」。它<strong>不免费</strong>，最低 ¥49/月（Andante/Plus）起步，¥99 解锁 K3，¥199 解锁 K3 1M 上下文与高速版，¥699 顶配百万 Token。0 预算党请走 Gemini CLI / DeepSeek-TUI / 通义灵码免费额度；要国产 GUI + 多 Agent 协作再考虑 Kimi，先订最低档，跑满再升级，别为「好看」多付 5 倍钱。</p>"""

CONTENT_EN = """<h1>Kimi Code Desktop Guide: Desktop AI Coding Agent, 4 Tiers, K3 Model &amp; Free Alternatives (2026)</h1>

<p>On September 22, 2026, Moonshot AI released <strong>Kimi Code Desktop, the desktop client for Kimi Code, on both macOS and Windows</strong>. It moves AI-agent coding out of the command line and into a GUI: describe a task, track progress, run/debug, and handle Git &amp; PRs in a single window, keeping the AI collaboration "visible and controllable." Based on the Sep 22 ai-bot.cn news feed and the live kimi.com pricing pages, this guide breaks down the four work modes, the four paid tiers (quotas and prices), the K3 model gating, and the rate limits — plus zero-cost alternatives, so you can decide whether to subscribe and which tier fits.</p>

<p>Bottom line up front: <strong>if you want to code for $0, don't subscribe to Kimi — use Gemini CLI, DeepSeek-TUI, or the free tier of Tongyi Lingma instead. If you want a Chinese-first desktop GUI with multi-agent (Swarm/Tower) collaboration, the entry ¥49/mo Andante (Plus) tier is enough for most people; save ¥199/¥699 for heavy multi-agent concurrency. The free Go tier has no coding quota — "Kimi is free" does not mean "Kimi Code is free."</strong></p>

<h2>Four work modes: one subscription, every surface</h2>

<p>The core of Kimi Code Desktop is <strong>running the whole "write code → run commands → verify → review → merge" loop inside one desktop window</strong>, with a built-in terminal, browser, Git status panel, and screenshot / web-element annotation. It is a "GUI-first agent workbench," not just an editor, with four modes:</p>

<table>
<tr><th>Mode</th><th>Behavior</th><th>Best for</th></tr>
<tr><td><strong>Plan</strong></td><td>Shows a plan first; runs only after you confirm</td><td>Large refactors where you want to review before execution</td></tr>
<tr><td><strong>Goal</strong></td><td>Autonomously drives toward a goal with few interruptions</td><td>Building a small app from scratch, end-to-end delivery</td></tr>
<tr><td><strong>Swarm</strong></td><td>Main agent splits the job and dispatches sub-agents</td><td>Mid-to-large multi-module parallel tasks</td></tr>
<tr><td><strong>Tower</strong></td><td>Multiple agents work in parallel (experimental)</td><td>Several workflows you want to advance at once</td></tr>
</table>

<p>Other engineering features: file paths in the chat open a preview with one click; screenshot or web-element annotation for "point where you mean"; tabs, pinning, AI auto-naming and global search for managing many sessions; and — key for power users — <strong>existing local CLI tasks auto-sync into the desktop client</strong>, so legacy users migrate with zero re-setup and all agent capabilities intact.</p>

<h2>Tiers &amp; quotas (official 2026-09-22 data)</h2>

<p>Kimi Code is part of the Kimi membership and ships <strong>with the subscription, sharing the same monthly quota pool as other Kimi features</strong>. Requests from the CLI, VS Code plugin, desktop client and third-party tools all count against it. The free Go (Adagio) tier has <strong>no coding quota</strong> — to actually code in Kimi Code you need a paid tier. The four current paid tiers on the official pricing page (music-term names, prices unchanged):</p>

<table>
<tr><th>Tier (new name)</th><th>Price</th><th>Agent usage (if monthly quota is all spent on one feature)</th><th>Parallel / cluster</th><th>Key quotas</th></tr>
<tr><td><strong>Andante (Plus)</strong></td><td>¥49/mo</td><td>~30 agents</td><td>Agent priority queue (4x speed)</td><td>1,000 DB calls; 20 projects / 20GB; 15+ plugins</td></tr>
<tr><td><strong>Moderato</strong></td><td>¥99/mo</td><td>~60 agents</td><td>2 parallel tasks; cluster 25 runs (2 subtasks)</td><td>2,000 DB calls; dream memory, self-evolving skills</td></tr>
<tr><td><strong>Allegretto (Pro)</strong></td><td>¥199/mo</td><td>~150 agents</td><td>2 parallel; cluster 50 runs (4 subtasks)</td><td>5,000 DB calls; goal mode; exclusive Kimi Claw (10 group chats); <strong>K3 1M context &amp; high-speed gate</strong></td></tr>
<tr><td><strong>Allegro</strong></td><td>¥699/mo</td><td>~360 agents</td><td>4 parallel; cluster 120 runs (8 subtasks)</td><td>12,000 DB calls; <strong>million-token long context</strong>; 100 projects / 50GB</td></tr>
</table>

<p><strong>Rules you must know:</strong></p>
<ul>
<li><strong>Shared quota pool.</strong> All Kimi features (site deployment, deep research, PPT, Kimi Code, Kimi Work, Kimi Claw, K3, K3 cluster) share one monthly pool metered by real token use. If one feature burns the pool, the others are affected.</li>
<li><strong>Kimi Code-only rate windows.</strong> Kimi Code also has a "per-5-hour" and a "per-week" frequency window that affects Kimi Code only. Dense bursts trigger throttling that clears automatically when the window rolls.</li>
<li><strong>Model gates.</strong> The K3 model requires <strong>Moderato (¥99) or above</strong>; K3's <strong>1M context</strong> and the <strong>high-speed</strong> build require <strong>Allegretto (¥199) or above</strong>.</li>
<li><strong>Two naming schemes.</strong> The pricing page uses Andante/Moderato/Allegretto/Allegro; the docs use Go / Plus / Pro etc. — <strong>prices are unchanged</strong>, old plans keep working, and you can upgrade when you want. Treat the live site as authoritative.</li>
<li><strong>Annual saves money.</strong> Continuous annual billing saves up to <strong>¥1,680</strong>.</li>
</ul>

<h2>Compared to free / low-cost coding agents</h2>

<p>Kimi Code Desktop plays "Chinese-first + desktop GUI + multi-agent." It is <strong>not free</strong>. If your goal is zero-cost coding, these are better value (2026 snapshot, quotas can change):</p>

<table>
<tr><th>Tool</th><th>Free tier</th><th>Form</th><th>Who it fits</th><th>Paid entry</th></tr>
<tr><td><strong>Kimi Code Desktop</strong></td><td>❌ Free Go tier has no coding quota</td><td>Desktop GUI multi-agent</td><td>Want CN GUI + Swarm/Tower multi-agent collab</td><td>From ¥49/mo</td></tr>
<tr><td><strong>Gemini CLI (Google)</strong></td><td>✅ Free AI Studio quota (Flash-tier requests free)</td><td>Terminal agent</td><td>$0 mainstream agent coding</td><td>—</td></tr>
<tr><td><strong>DeepSeek-TUI</strong></td><td>✅ Open source (MIT), DeepSeek API free/cheap</td><td>Terminal "DeepSeek's Claude Code"</td><td>Terminal + CN model fans</td><td>DeepSeek API (very cheap)</td></tr>
<tr><td><strong>Tongyi Lingma / Qwen</strong></td><td>✅ Free personal quota</td><td>IDE plugin</td><td>CN IDE ecosystem, Chinese completion</td><td>Enterprise edition separately priced</td></tr>
<tr><td><strong>Cursor</strong></td><td>Limited free</td><td>VS Code-based IDE</td><td>Industry-best editor autocomplete</td><td>Pro ~$20/mo</td></tr>
<tr><td><strong>Windsurf / Devin</strong></td><td>Limited free</td><td>AI-native IDE</td><td>Parallel multi-session agent management</td><td>~$15/mo and up</td></tr>
</table>

<p>The decision is simple: <strong>$0 budget → Gemini CLI / DeepSeek-TUI / Tongyi Lingma; ¥49 budget wanting a desktop GUI + multi-agent collab → Kimi Andante; heavy multi-agent concurrency or 1M context → Allegretto / Allegro.</strong> Don't pay ¥699 just because the UI looks nice — look at your task volume first.</p>

<h2>Install to first task (5 steps)</h2>
<ol>
<li><strong>Download</strong>: go to <a href="https://www.kimi.com/code">kimi.com/code</a> and grab the macOS (Apple / Intel) or Windows build.</li>
<li><strong>Sign in</strong>: one-click Kimi login, or configure a third-party model provider in settings.</li>
<li><strong>Pick a workspace</strong>: in a new session, select a local project folder; the desktop client organizes sessions by workspace.</li>
<li><strong>Start a task</strong>: describe the requirement in plain language and pick Plan / Goal / Swarm / Tower to match.</li>
<li><strong>Confirm &amp; close the loop</strong>: in Plan mode, review the plan before it runs; use the built-in terminal for build/test and the built-in browser to preview; watch branch and PR progress in the Git panel.</li>
</ol>

<h2>Save money &amp; avoid the traps</h2>
<ol>
<li><strong>Don't be fooled by "Kimi is free."</strong> The free Go/Adagio tier has no coding quota; coding needs ¥49 minimum. Free-tier users should switch to Gemini CLI, DeepSeek-TUI or Tongyi Lingma.</li>
<li><strong>¥49 is fine for daily use.</strong> ~30 agents + 1,000 DB calls + 20 projects covers most solo small/medium projects; start on the cheapest tier and upgrade when you hit the ceiling.</li>
<li><strong>Watch the shared pool.</strong> PPT, deep research and Kimi Claw all draw from the same pool; if another feature exhausts it, Kimi Code freezes too.</li>
<li><strong>Don't brute-force the 5-hour window.</strong> Dense requests get throttled; it clears automatically when the window rolls — it is not a ban.</li>
<li><strong>Claw cloud hosts have hidden cost.</strong> If you deploy Kimi Claw, the cloud-host sandbox bills ~0.6% of your membership quota per day (settled 4pm) even while idle.</li>
<li><strong>Annual is cheaper.</strong> If you'll keep it long-term, use continuous annual billing for up to ¥1,680 savings.</li>
</ol>

<h2>FAQ</h2>
<div class="faq-section">
<div class="faq-item"><div class="faq-q">Is Kimi Code Desktop really completely free?</div><div class="faq-a">No. The free Go/Adagio tier has no coding quota; using Kimi Code starts at ¥49/mo (Andante/Plus). For $0 coding, use Gemini CLI, DeepSeek-TUI or the free tier of Tongyi Lingma.</div></div>
<div class="faq-item"><div class="faq-q">How much code can I get out of the ¥49 Andante tier per month?</div><div class="faq-a">Official estimate: ~30 agents if the whole monthly quota goes to one feature, plus 1,000 professional-DB calls, 20 projects / 20GB storage and 15+ curated plugins. Enough for solo small/medium projects; dense bursts hit the 5-hour rate window.</div></div>
<div class="faq-item"><div class="faq-q">Which tier unlocks the K3 model and 1M context?</div><div class="faq-a">K3 needs ¥99 (Moderato) or above; K3's 1M long context and the high-speed build need ¥199 (Allegretto/Pro) or above. The top ¥699 (Allegro) tier is where you get the million-token long context.</div></div>
<div class="faq-item"><div class="faq-q">What is the "per-5-hour / per-week" limit?</div><div class="faq-a">On top of the shared monthly quota, Kimi Code has a per-5-hour and a per-week frequency window that affects Kimi Code only (not PPT, deep research, etc.). Dense bursts get throttled and clear automatically when the window rolls — it is not a ban or permanent lock.</div></div>
<div class="faq-item"><div class="faq-q">How does it stack up against Cursor or Windsurf?</div><div class="faq-a">Kimi Code Desktop wins on the CN ecosystem + desktop GUI multi-agent collaboration (Swarm subtask division, Tower parallel agents) + a shared Kimi membership quota. Cursor's editor autocomplete and Tab prediction are still the gold standard; if you want $0 or the best completion feel, the free options are better value.</div></div>
<div class="faq-item"><div class="faq-q">Do I need to reconfigure anything when moving from the Kimi Code CLI?</div><div class="faq-a">No. Existing local CLI tasks auto-sync into the desktop client and all agent capabilities carry over with zero re-setup; model, provider, permission and plugin settings are all adjustable in the GUI.</div></div>
</div>

<h2>Summary</h2>
<p>Kimi Code Desktop is Moonshot AI's desktop client that puts Kimi Code's agent-coding into a GUI, launched Sep 22, 2026 on macOS/Windows, built around "one window for the whole loop + Plan/Goal/Swarm/Tower modes + multi-agent parallelism." It is <strong>not free</strong>: entry is ¥49/mo (Andante/Plus), ¥99 unlocks K3, ¥199 unlocks K3's 1M context and high speed, and ¥699 tops out with million-token context. If your budget is zero, use Gemini CLI / DeepSeek-TUI / Tongyi Lingma's free tiers; only consider Kimi when you want a CN GUI with real multi-agent collaboration — start on the cheapest tier, upgrade when you max it out, and don't overpay 5x just for a prettier interface.</p>"""

# FAQ arrays (match the on-page FAQ, for guides.json structured data)
FAQ_ZH = [
 {"question":"Kimi Code Desktop 真的完全免费吗？","answer":"不是。免费 Go/Adagio 档没有 coding 额度，用 Kimi Code 编程最低要订 ¥49/月（Andante/Plus）。0 元写代码建议走 Gemini CLI、DeepSeek-TUI 或通义灵码的免费额度。"},
 {"question":"¥49 的 Andante 档一个月大概能写多少代码？","answer":"官方按「月额度全投单一功能」估算约 30 个 Agent 用量，外加专业数据库 1000 次调用、20 个项目 / 20GB 存储、15+ 精选插件。中小项目个人日常够用，跑满会触发 5 小时速率窗口限流。"},
 {"question":"K3 模型和 1M 上下文分别在哪个档能用？","answer":"K3 模型需 ¥99（Moderato）及以上可调用；K3 的 1M 超长上下文和高速版需 ¥199（Allegretto/Pro）及以上。顶档 ¥699（Allegro）才支持百万 Token 长上下文。"},
 {"question":"「每 5 小时 / 每周」限制是什么？","answer":"Kimi Code 在共享月度额度之外，另有每 5 小时和每周两个频率窗口（仅作用 Kimi Code，不影响 PPT、深度研究等功能）。短时间请求过密触发限流后，等窗口滚动自动恢复，不是封号或永久限制。"},
 {"question":"和 Cursor、Windsurf 比，Kimi Code Desktop 强在哪？","answer":"强在国产中文生态 + 桌面 GUI 多 Agent 协作（Swarm 子任务分工、Tower 多 Agent 并行）+ 与 Kimi 会员共享额度。Cursor 的编辑器补全和 Tab 预测仍是标杆；预算 0 或要极致补全体验时，免费方案更划算。"},
 {"question":"老用户从 Kimi Code CLI 迁到桌面端要重新配置吗？","answer":"不用。CLI 已有的本地任务会自动同步到桌面端，原有 Agent 能力完整保留，零成本平滑过渡；模型、供应商、权限、插件等配置都能图形化调整。"}
]
FAQ_EN = [
 {"question":"Is Kimi Code Desktop really completely free?","answer":"No. The free Go/Adagio tier has no coding quota; using Kimi Code starts at CNY 49/mo (Andante/Plus). For $0 coding, use Gemini CLI, DeepSeek-TUI or the free tier of Tongyi Lingma."},
 {"question":"How much code can I get out of the CNY 49 Andante tier per month?","answer":"Official estimate: ~30 agents if the whole monthly quota goes to one feature, plus 1,000 professional-DB calls, 20 projects / 20GB storage and 15+ curated plugins. Enough for solo small/medium projects; dense bursts hit the 5-hour rate window."},
 {"question":"Which tier unlocks the K3 model and 1M context?","answer":"K3 needs CNY 99 (Moderato) or above; K3's 1M long context and the high-speed build need CNY 199 (Allegretto/Pro) or above. The top CNY 699 (Allegro) tier is where you get the million-token long context."},
 {"question":"What is the \"per-5-hour / per-week\" limit?","answer":"On top of the shared monthly quota, Kimi Code has a per-5-hour and a per-week frequency window that affects Kimi Code only. Dense bursts get throttled and clear automatically when the window rolls - it is not a ban or permanent lock."},
 {"question":"How does it stack up against Cursor or Windsurf?","answer":"Kimi Code Desktop wins on the CN ecosystem + desktop GUI multi-agent collaboration (Swarm subtask division, Tower parallel agents) + a shared Kimi membership quota. Cursor's editor autocomplete and Tab prediction are still the gold standard; if you want $0 or the best completion feel, the free options are better value."},
 {"question":"Do I need to reconfigure anything when moving from the Kimi Code CLI?","answer":"No. Existing local CLI tasks auto-sync into the desktop client and all agent capabilities carry over with zero re-setup; model, provider, permission and plugin settings are all adjustable in the GUI."}
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

# ---- Register into guides.json (public + dist) ----
ENTRY = {
    "slug": SLUG,
    "title_zh": TITLE_ZH,
    "title_en": TITLE_EN,
    "description_zh": DESC_ZH,
    "description_en": DESC_EN,
    "category": "coding",
    "date_published": TODAY,
    "tags": ["Kimi Code", "桌面端", "多Agent", "K3", "AI编程", "订阅攻略"],
    "icon": "🖥️",
    "excerpt_zh": "Kimi Code Desktop 9/22 上线，桌面端 AI 编程 Agent，Plan/Goal/Swarm/Tower 四模式。免费 Go 档无 coding 额度，¥49/99/199/699 四档订阅，¥99 起用 K3，0 元党走 Gemini CLI / DeepSeek-TUI。",
    "excerpt_en": "Kimi Code Desktop (Sep 22) brings AI-agent coding to the desktop GUI with Plan/Goal/Swarm/Tower modes. Free Go tier has no coding quota; paid tiers run 49/99/199/699 CNY. K3 from 99. $0 users: use Gemini CLI / DeepSeek-TUI.",
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
