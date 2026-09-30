#!/usr/bin/env python3
"""Generate the 'Loomy (iFlytek) Desktop AI Agent — Free Credits Guide' .
Data sources (fetched 2026-09-30):
- ai-bot.cn/sites/73695.html (Loomy, 科大讯飞桌面级AI智能体): 标题宣称"每天免费5000积分"; 官网 loomy.xunfei.cn; 专属邀请码可额外领积分; 深度适配飞书/钉钉/微信; 目录级授权文件留本地; 竞品对比 办公小浣熊(商汤)/TRAE Work(字节)
- loomy.xunfei.cn/download: 下载即享 5000 体验积分; macOS 仅 Apple Silicon (macOS 14+); Windows 10+ x64 (Beta, 有安装版/绿色版); 下载免费
- loomy.xunfei.cn/docs/user-guide/credits: 5000积分约可执行 50 次典型办公任务; 积分获取方式: 等审核/分享好友(双方各得5000)/官方活动/积分包充值; 使用自定义模型 API Key 不扣 Loomy 积分(Key仅存本地); 消耗快=多步骤/长上下文/高频调用
- loomy.xunfei.cn/docs/user-guide/models: 默认模型开箱即用: MiniMax-M2.5 / 豆包doubao-seed-2.0-pro / DeepSeek-v3.2 / 通义千问qwen3.5-plus; 支持自定义模型商API Key
- loomy.xunfei.cn/docs/quick-start: 登录需输入邀请码; 功能: AI对话/任务执行/工作目录/远程控制/搭子团/技能广场/定时任务/资料库/桌面宠物
"""
import os, sys, json
from datetime import datetime

sys.path.insert(0, '/home/ubuntu/aifreeplan/scripts')
from write_guide import generate_guide_html

SLUG = "loomy-xunfei-desktop-ai-agent-free-2026"
TODAY = "2026-09-30"

TITLE_ZH = "讯飞Loomy免费攻略：桌面AI工作搭子，下载即领5000积分（可白嫖约50次任务）"
TITLE_EN = "Loomy Free Guide: iFlytek's Desktop AI Work Agent — 5,000 Free Credits on Download (~50 Tasks)"

DESC_ZH = "科大讯飞推出桌面AI智能体Loomy（loomy.xunfei.cn），免费下载、下载即送5000体验积分，官方文档写明5000积分约够执行50次典型办公任务；邀请码登录、分享好友双方再各得5000积分；接自己的API Key跑模型不扣积分。本文给全免费入口、积分规则、默认模型清单（MiniMax-M2.5/豆包/DeepSeek-v3.2/Qwen3.5-Plus）和避坑点。"
DESC_EN = "iFlytek's Loomy is a desktop AI work agent (loomy.xunfei.cn): free to download, with 5,000 trial credits granted on download — the official docs say that covers roughly 50 typical office tasks. Invite-code login, +5,000 credits for you and each friend who joins via your share, and BYO API key uses no Loomy credits at all. This guide covers the free entry points, credit rules, default model list (MiniMax-M2.5 / Doubao / DeepSeek-v3.2 / Qwen3.5-Plus), and the gotchas."

CONTENT_ZH = """<h1>讯飞Loomy免费攻略：桌面AI工作搭子，下载即领5000积分（可白嫖约50次任务）</h1>

<p>科大讯飞（合肥科讯创想软件开发有限公司）新出的桌面级AI智能体 <strong>Loomy</strong> 是目前国内"桌面Agent"赛道里免费额度写得最明白的一个。几个核心数字（2026年9月30日核对）：<strong>客户端免费下载，下载即送 5,000 体验积分；官方文档明确 5,000 积分约可执行 50 次典型办公任务</strong>；登录需要邀请码，ai-bot.cn 收录页给出专属邀请码可额外领 10,000 积分（第三方渠道口径，以产品内实际发放为准）；把 Loomy 分享给好友，好友通过你的分享加入后，<strong>双方各得 5,000 积分</strong>；接自己的模型 API Key 跑任务时，模型调用<strong>不扣 Loomy 积分</strong>——等于免费额度用完后还能 0 边际成本地继续用。它主打"低门槛、高安全、强适配、主动协作"：文件留在本地、只在授权目录内操作，深度适配飞书/钉钉/微信等国内办公环境。结论先给：个人白嫖办公自动化，Loomy 是目前免费积分给得最具体的国产桌面 Agent；重度用户直接配自己的 API Key 绕过积分限制。</p>

<h2>免费额度与积分规则速览</h2>

<table>
<tr><th>项目</th><th>数字/规则</th><th>来源</th></tr>
<tr><td>客户端下载</td><td>免费，0 元；macOS（Apple Silicon，macOS 14+）/ Windows 10+ x64（Beta，有安装版和绿色版）</td><td>loomy.xunfei.cn/download</td></tr>
<tr><td>下载体验积分</td><td><strong>5,000 积分</strong>（"下载即享体验积分"）</td><td>官网下载页</td></tr>
<tr><td>5,000 积分能干什么</td><td>约 <strong>50 次</strong>典型办公任务（如"搜索整理→写报告存本地→发邮件→10次邮件往来"这类完整链路算 1 次；消耗受任务长度/上下文/模型调用次数影响）</td><td>官方文档 docs/user-guide/credits</td></tr>
<tr><td>邀请码登录</td><td>打开客户端输入邀请码即可登录开始使用；ai-bot.cn 收录页称专属码可额外领 10,000 积分（渠道口径）</td><td>quick-start 文档 + ai-bot.cn</td></tr>
<tr><td>分享拉新</td><td>好友通过你的分享加入，<strong>双方各得 5,000 积分</strong>（可重复进行）</td><td>官方文档 credits</td></tr>
<tr><td>其他获取方式</td><td>申请 Waiting List 通过审核、官方活动/内测、积分包充值（价格以产品内页面实时展示为准）</td><td>官方文档 credits</td></tr>
<tr><td>自定义模型 API Key</td><td>配自己的模型商 Key，模型调用<strong>不扣 Loomy 积分</strong>；Key 只存本地设备，不上传云端</td><td>官方文档 credits / custom-models</td></tr>
</table>

<h2>免费入口：从下载到跑通 50 次任务</h2>

<ol>
<li>访问 <a href="https://loomy.xunfei.cn/">loomy.xunfei.cn</a> 下载页，选 macOS（M 芯片，需 macOS 14 或更高）或 Windows（10 及以上 x64；Beta 版如有安装问题可下绿色版，解压即用，路径别带中文字符）；</li>
<li>安装后打开客户端，输入邀请码登录——登录这一步需要邀请码，不是注册邮箱就能进；</li>
<li>登录即到账 <strong>5,000 体验积分</strong>；按引导授权 1 个工作目录（未授权目录不会被读取，这是它的目录级授权机制）；</li>
<li>在对话框用自然语言下任务，例如："帮我做一份 2026 年 AI 行业趋势分析 PPT，10 页左右，商务风格，要数据图表和结论页"——它会自动拆解目标、串联工具、执行多步骤并交付本地成品；</li>
<li>想多攒积分：把 Loomy 分享给好友，好友通过你的分享加入，双方各得 5,000 积分；</li>
<li>免费额度耗尽后：在"设置→模型"里配自己的 API Key（MiniMax/DeepSeek/通义等），模型调用不扣 Loomy 积分，0 边际成本继续用。</li>
</ol>

<h2>内置默认模型：免 Key 开箱即用（会扣积分）</h2>

<p>Loomy 默认提供 4 家国内模型的模型服务，下载登录就能切，不用自备 Key（但调用<strong>消耗 Loomy 积分</strong>）：</p>

<ul>
<li><strong>MiniMax-M2.5</strong>（MiniMax）</li>
<li><strong>doubao-seed-2.0-pro</strong>（豆包，字节）</li>
<li><strong>DeepSeek-v3.2</strong></li>
<li><strong>qwen3.5-plus</strong>（通义千问，阿里）</li>
</ul>

<p>切换在"设置→模型"里点保存即生效，不用重启。默认模型会随版本升级，以产品内列表为准。</p>

<h2>免费功能清单：哪些能力不额外花钱</h2>

<p>下面这些核心能力都包含在免费客户端里，不单独收费（只是任务执行会消耗积分池）：</p>

<ul>
<li><strong>AI 对话 + 任务执行</strong>：一句话指令拆解目标、串联工具、跑多步骤流程；</li>
<li><strong>技能广场</strong>：内置 HTML 演示文稿、电子杂志/PPT、网页设计等官方推荐技能，安装即用；</li>
<li><strong>搭子团协作</strong>：多个专业"搭子"组队分工（内容增长、产品发布、商务方案、数据分析），一个人调动一支 AI 团队；</li>
<li><strong>远程控制</strong>：绑定微信/QQ/飞书/钉钉机器人，手机发消息即可远程查看进度、打开文件、推进任务；飞书/钉钉/企业微信 CLI 也可配置；</li>
<li><strong>定时任务</strong>：循环与单次任务（定点提醒、定时查热搜等）到点自动完成；</li>
<li><strong>资料库</strong>：统一管理本地资料，支持大容量快速加载与搜索；</li>
<li><strong>桌面宠物</strong>：桌宠自动"打工"赚积分（积分记录可在详情页查）。</li>
</ul>

<h2>积分消耗避坑：什么任务烧得快</h2>

<p>官方文档给的判断标准很直接：<strong>多步骤任务、长上下文任务、频繁调用模型、联动多个工具</strong>，这四类烧积分最快。使用建议：</p>

<ul>
<li>下任务前先确认目标和流程，避免"先跑一遍再重跑"的无效消耗；</li>
<li>5,000 积分 ≈ 50 次一般强度任务，但复杂链路（跨工具、多轮）单次消耗更高，实际次数会低于 50；</li>
<li>有稳定模型服务的用户直接配自定义 API Key，绕开默认模型的积分消耗；</li>
<li>积分余额和历史变动记录在客户端内可查（获得时间、获得方式、消耗记录），花在哪一清二楚。</li>
</ul>

<h2>和竞品对比：免费额度谁给得实</h2>

<table>
<tr><th>维度</th><th>Loomy（科大讯飞）</th><th>办公小浣熊（商汤）</th><th>TRAE Work（字节）</th></tr>
<tr><td>产品定位</td><td>桌面级 AI 工作搭子，本地智能体</td><td>AI 办公助手，主打数据分析与创作空间</td><td>AI 原生工作台（由 TRAE SOLO 编程智能体升级）</td></tr>
<tr><td>免费额度</td><td><strong>下载送 5,000 积分（约 50 次任务）；分享拉新双方各 +5,000；BYO Key 不扣分</strong></td><td>支持 SaaS 云端与企业私有化部署（免费额度口径以其官网为准）</td><td>任务依赖云端执行；编程向，TRAE 国内个人版免费用国产模型</td></tr>
<tr><td>数据安全</td><td>目录级授权，文件留本地，未授权目录访问前征求同意</td><td>SaaS 云端 + 企业私有化</td><td>云端同步</td></tr>
<tr><td>远程控制</td><td>微信/QQ/飞书/钉钉机器人远程操控本机</td><td>移动端与云端同步</td><td>手机语音派任务到云端或指定电脑，三端协同</td></tr>
<tr><td>适配场景</td><td>飞书/钉钉/微信/小红书等国内办公流</td><td>百万级数据分析、报告与 PPT</td><td>内容创作、数据分析、Web 应用、代码开发</td></tr>
</table>

<p>（竞品对比口径来自 ai-bot.cn 收录页；"每天免费 5000 积分"是收录页的宣传标题，官方下载页与积分文档目前写的是"下载即享 5000 体验积分"+ 分享/活动等获取方式，日刷额度是否持续更新以产品内规则为准。）</p>

<h2>常见问题</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: Loomy 下载和使用要钱吗？</div>
<div class="faq-a">客户端免费下载（macOS Apple Silicon / Windows x64 Beta），下载即送 5,000 体验积分，官方文档写明约够执行 50 次典型办公任务。超额后可通过分享好友（双方各得 5,000）、官方活动、Waiting List 审核或积分包充值（价格以产品内实时页面为准）获取；配置自己的模型 API Key 则模型调用不扣积分。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 登录一定要邀请码吗？</div>
<div class="faq-a">是。官方快速开始文档写明：打开 Loomy 后输入邀请码即可完成登录并开始使用。邀请码渠道包括 ai-bot.cn 收录页的专属码（宣称额外领 10,000 积分，以实际发放为准）和分享链接等。没拿到码时也可留意 Waiting List 审核通道。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 用自己的 API Key 还会扣积分吗？</div>
<div class="faq-a">不会。官方文档明确：配置并使用自己的模型服务提供商 API Key 时，相关模型调用通常不消耗 Loomy 积分（是否涉及其他能力消耗以产品内规则为准）。Key 只保存在本地设备，Loomy 不托管、不上传。这意味着免费 5,000 积分烧完后，配一个便宜模型商的 Key 就能近乎零成本继续跑。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 5,000 积分的 50 次任务怎么算的？</div>
<div class="faq-a">官方给的示例链路：围绕"项目立项"搜索整理多类信息→汇总成报告存本地→写邮件向领导申请预算→后续约 10 次邮件往来，这样一条完整链路算一次任务，5,000 积分约可支持 50 次左右。任务越长、上下文越大、模型调用越频繁，单次消耗越高，实际次数会低于 50。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 我的文件会被上传到云端吗？</div>
<div class="faq-a">不会。Loomy 采用目录级授权机制：文件留在本地，AI 只在授权目录内操作，访问未授权目录前会征求同意；自定义 API Key 也仅存本地。这是它相对海外 Agent 产品强调的"数据风险可控"卖点。</div>
</div>
</div>

<h2>总结</h2>

<p>Loomy 的免费策略在国产桌面 Agent 里属于"数字透明"型：<strong>下载 0 元 + 5,000 体验积分（≈50 次任务）+ 分享双方各 +5,000 + BYO API Key 不扣分</strong>。办公白领、自媒体、电商、小团队可以先把 5,000 积分花在文件整理、PPT、数据复盘这类高频任务上；重度用户配自有 Key 后基本 0 边际成本。平台支持 macOS（Apple Silicon，14+）和 Windows 10+ x64（Beta）。免费额度与积分规则会随版本调整，动手前以 loomy.xunfei.cn 产品内实时展示为准。</p>
"""

CONTENT_EN = """<h1>Loomy Free Guide: iFlytek's Desktop AI Work Agent — 5,000 Free Credits on Download (~50 Tasks)</h1>

<p>iFlytek (Hefei Keyu Chuangxiang Software) just shipped a desktop AI agent called <strong>Loomy</strong>, and it's the most number-transparent free-tier offer in China's desktop-agent space. Key figures (verified 2026-09-30): <strong>the client is free to download and grants 5,000 trial credits on download; the official docs state 5,000 credits covers roughly 50 typical office tasks</strong>; login requires an invite code (the ai-bot.cn listing advertises a dedicated code for an extra 10,000 credits — a channel claim, subject to actual in-app distribution); sharing Loomy with a friend earns <strong>both of you 5,000 credits each</strong>; and hooking up your own model API key means model calls <strong>consume zero Loomy credits</strong> — so after the free pool runs out, you can keep using it at near-zero marginal cost. It's built around "low barrier, high security, strong fit, proactive collaboration": files stay local, it only operates inside authorized directories, and it's deeply integrated with Chinese office stacks (Feishu, DingTalk, WeChat). Bottom line up front: for free office automation on a personal machine, Loomy is the most specific free-credit offer among domestic desktop agents; heavy users should just BYO API key to sidestep the credit cap entirely.</p>

<h2>Free Credits &amp; Rules at a Glance</h2>

<table>
<tr><th>Item</th><th>Number / Rule</th><th>Source</th></tr>
<tr><td>Client download</td><td>Free, $0; macOS (Apple Silicon, 14+) / Windows 10+ x64 (Beta, installer + portable green build)</td><td>loomy.xunfei.cn/download</td></tr>
<tr><td>Download trial credits</td><td><strong>5,000 credits</strong> ("get trial credits the moment you download")</td><td>Official download page</td></tr>
<tr><td>What 5,000 credits buys</td><td>About <strong>50 typical office tasks</strong> (e.g. one full pipeline: search &amp; organize → write a report saved locally → email your boss for budget → ~10 rounds of email follow-up counts as 1 task; consumption scales with task length, context size, and model-call count)</td><td>Official docs, user-guide/credits</td></tr>
<tr><td>Invite-code login</td><td>Open the client and enter an invite code to log in; the ai-bot.cn listing claims a dedicated code grants an extra 10,000 credits (channel figure, verify in-app)</td><td>quick-start docs + ai-bot.cn</td></tr>
<tr><td>Referral bonus</td><td>When a friend joins via your share link, <strong>both of you get 5,000 credits</strong> (repeatable)</td><td>Official docs, credits</td></tr>
<tr><td>Other ways to earn</td><td>Waiting-list approval, official events / beta programs, credit-pack purchases (prices shown live in-app)</td><td>Official docs, credits</td></tr>
<tr><td>BYO model API key</td><td>Connect your own model-provider key: model calls <strong>cost no Loomy credits</strong>; keys are stored on your device only, never uploaded</td><td>Official docs, credits / custom-models</td></tr>
</table>

<h2>Free Path: From Download to ~50 Tasks</h2>

<ol>
<li>Go to <a href="https://loomy.xunfei.cn/">loomy.xunfei.cn</a> (download page) and pick macOS (M-series chips, macOS 14 or later) or Windows (10+ x64; Beta — if the installer misbehaves, grab the portable "green" build and run it unzipped; keep install paths free of CJK characters);</li>
<li>Launch the client and log in with an invite code — login is invite-code based, not email registration;</li>
<li>The <strong>5,000 trial credits</strong> land on login; authorize one working directory as guided (unauthorized directories are never read — that's its directory-level authorization model);</li>
<li>Drop natural-language tasks into the chat box, e.g. "Make a 10-page business-style PPT on 2026 AI industry trends, with data charts and a conclusion slide" — it decomposes the goal, chains tools, runs the multi-step flow, and delivers a local artifact;</li>
<li>Stack more credits: share Loomy with a friend — when they join through your link, you both get 5,000;</li>
<li>When the free pool is exhausted: open Settings → Models and plug in your own API key (MiniMax / DeepSeek / Qwen, etc.) — model calls then skip Loomy's credit meter entirely.</li>
</ol>

<h2>Default Models: No Key Needed (They Do Burn Credits)</h2>

<p>Loomy ships with four domestic model services you can switch to immediately after login — no key required, though each call <strong>consumes Loomy credits</strong>:</p>

<ul>
<li><strong>MiniMax-M2.5</strong> (MiniMax)</li>
<li><strong>doubao-seed-2.0-pro</strong> (Doubao, ByteDance)</li>
<li><strong>DeepSeek-v3.2</strong></li>
<li><strong>qwen3.5-plus</strong> (Qwen / Tongyi, Alibaba)</li>
</ul>

<p>Switching is Settings → Models → save, takes effect instantly, no restart. The default lineup tracks version updates, so check the in-app list for the current models.</p>

<h2>What's Included Free (No Separate Charges)</h2>

<p>These core capabilities all ship in the free client — nothing below is paywalled separately; task execution just draws from your credit pool:</p>

<ul>
<li><strong>AI chat + task execution</strong>: one-instruction goal decomposition, tool chaining, multi-step execution;</li>
<li><strong>Skill plaza</strong>: ready-to-install official skills (HTML presentations, e-magazines/PPT, web design, more);</li>
<li><strong>"Dazi-tuan" agent teams</strong>: multiple specialist agents collaborate on complex jobs (content growth, product launch, business proposals, data analysis);</li>
<li><strong>Remote control</strong>: bind a WeChat / QQ / Feishu / DingTalk bot and drive your computer from your phone — check progress, open files, push tasks forward; Feishu / DingTalk / WeCom CLIs are also configurable;</li>
<li><strong>Scheduled tasks</strong>: recurring or one-shot jobs (reminders, trending-topics polling) that fire on time;</li>
<li><strong>Knowledge base</strong>: unified local document management with fast large-scale loading and search;</li>
<li><strong>Desktop pet</strong>: a desktop mascot that "works" and earns credits for you (visible in the credit ledger).</li>
</ul>

<h2>Credit Consumption: What Burns Fast</h2>

<p>The official docs are blunt about the four fast-burn categories: <strong>multi-step tasks, long-context tasks, frequent model calls, and multi-tool chaining</strong>. Practical advice:</p>

<ul>
<li>Confirm the goal and flow before firing a task — avoid "run it, then re-run it" waste;</li>
<li>5,000 credits ≈ 50 typical tasks, but complex cross-tool pipelines cost more per run, so real-world counts run below 50;</li>
<li>If you already have a stable model provider, BYO key and stop paying for default-model credits;</li>
<li>Your credit balance and full ledger (when, how earned, how consumed) are viewable inside the client.</li>
</ul>

<h2>Competitive Free-Tier Comparison</h2>

<table>
<tr><th>Dimension</th><th>Loomy (iFlytek)</th><th>Office Raccoon (SenseTime)</th><th>TRAE Work (ByteDance)</th></tr>
<tr><td>Positioning</td><td>Desktop AI work partner, local agent</td><td>AI office assistant, data analysis + creation space</td><td>AI-native workbench, evolved from the TRAE SOLO coding agent</td></tr>
<tr><td>Free credits</td><td><strong>5,000 on download (~50 tasks); +5,000 per friend referral (both sides); BYO key = no credit burn</strong></td><td>SaaS cloud or on-prem enterprise deploy (check its site for free-tier specifics)</td><td>Tasks run on the cloud; coding-oriented — TRAE's domestic personal tier is free with Chinese models</td></tr>
<tr><td>Data safety</td><td>Directory-level authorization; files stay local; consent before touching unauthorized folders</td><td>SaaS cloud + private enterprise deployment</td><td>Cloud sync</td></tr>
<tr><td>Remote control</td><td>WeChat/QQ/Feishu/DingTalk bots drive the local machine</td><td>Mobile + cloud sync</td><td>Voice dispatch from phone to cloud or a designated PC, three-end coordination</td></tr>
<tr><td>Fit</td><td>Feishu/DingTalk/WeChat/Xiaohongshu office workflows</td><td>Million-row data analysis, reports, PPT</td><td>Content creation, data analysis, web apps, code</td></tr>
</table>

<p>(Competitor rows come from the ai-bot.cn listing. Note: "5,000 free credits every day" is that listing's headline; the official download page and credit docs currently describe "5,000 trial credits on download" plus earn-by-sharing / events / packs. Whether the 5,000 refreshes daily — check the in-app rules.)</p>

<h2>FAQ</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: Is Loomy free to download and use?</div>
<div class="faq-a">Yes. The client downloads free (macOS Apple Silicon / Windows x64 Beta) and grants 5,000 trial credits on download — the official docs say that covers roughly 50 typical office tasks. When you run out: share with friends (both of you +5,000 each), official events / beta programs, waiting-list approval, or credit packs (prices shown in-app). Configuring your own model API key makes model calls cost zero Loomy credits.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Do I absolutely need an invite code to log in?</div>
<div class="faq-a">Yes. The quick-start doc says: open Loomy, enter an invite code, and you're in. Code sources include the dedicated code on the ai-bot.cn listing (claimed extra 10,000 credits — verify actual distribution) and share links. The waiting-list approval path is another channel if you can't find a code.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Do model calls burn credits if I use my own API key?</div>
<div class="faq-a">No. The docs are explicit: when you configure your own model-provider API key, the related model calls typically do not consume Loomy credits (other capability charges follow in-app rules). Keys are stored on your device only — Loomy never hosts or uploads them. So after the free 5,000 credits are spent, a cheap provider key keeps you going at near-zero marginal cost.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: How is "50 tasks for 5,000 credits" calculated?</div>
<div class="faq-a">The official example pipeline: for a "project kickoff" topic, search and organize multiple information categories → compile a report saved locally → email your boss for a budget request → roughly 10 rounds of follow-up email. That entire chain counts as one task, and 5,000 credits supports about 50 of them. Longer tasks, bigger context, and more frequent model calls raise the per-task cost, so real counts land below 50.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Does Loomy upload my files to the cloud?</div>
<div class="faq-a">No. Loomy uses directory-level authorization: files stay on your machine, the AI only operates inside authorized directories, and it asks for consent before touching anything else. Custom API keys are also stored locally. "Data risk stays controllable" is its main pitch versus overseas agent products.</div>
</div>
</div>

<h2>Bottom Line</h2>

<p>Loomy's free policy is refreshingly numeric for a domestic desktop agent: <strong>$0 download + 5,000 trial credits (≈50 tasks) + 5,000 per friend referral (both sides) + zero credit burn on BYO API keys</strong>. Office workers, self-media creators, e-commerce operators and small teams can spend the 5,000 on high-frequency work like file organization, PPT generation and data reviews; power users who bring their own key run at essentially zero marginal cost. Platform support: macOS (Apple Silicon, 14+) and Windows 10+ x64 (Beta). Free tiers and credit rules change with each release — verify on loomy.xunfei.cn before committing.</p>
"""

FAQ_ZH = [
 {"question":"Loomy 下载和使用要钱吗？","answer":"客户端免费下载（macOS Apple Silicon / Windows x64 Beta），下载即送 5,000 体验积分，官方文档写明约够执行 50 次典型办公任务。超额后可通过分享好友（双方各得 5,000）、官方活动、Waiting List 审核或积分包充值获取；配置自己的模型 API Key 则模型调用不扣积分。"},
 {"question":"登录一定要邀请码吗？","answer":"是。官方快速开始文档写明：打开客户端输入邀请码即可登录使用。渠道包括 ai-bot.cn 收录页专属码（宣称额外领 10,000 积分，以实际发放为准）和分享链接等；也可以走 Waiting List 审核通道。"},
 {"question":"用自己的 API Key 还会扣积分吗？","answer":"不会。官方文档明确：配置并使用自己的模型服务提供商 API Key 时，相关模型调用通常不消耗 Loomy 积分。Key 只保存在本地设备，Loomy 不托管、不上传。免费 5,000 积分烧完后配个便宜模型商的 Key 就能近乎零成本继续跑。"},
 {"question":"5,000 积分的 50 次任务怎么算的？","answer":"官方示例链路：围绕一个主题搜索整理多类信息→汇总成报告存本地→写邮件申请预算→后续约 10 次邮件往来，整条算 1 次任务，5,000 积分约支持 50 次。任务越长、上下文越大、模型调用越频繁，单次消耗越高，实际次数会低于 50。"},
 {"question":"我的文件会被上传到云端吗？","answer":"不会。Loomy 采用目录级授权：文件留在本地，AI 只在授权目录内操作，访问未授权目录前会征求同意；自定义 API Key 也仅存本地。"},
]
FAQ_EN = [
 {"question":"Is Loomy free to download and use?","answer":"Yes. The client downloads free (macOS Apple Silicon / Windows x64 Beta) and grants 5,000 trial credits on download — the official docs say that covers roughly 50 typical office tasks. When you run out: share with friends (both of you +5,000 each), official events, waiting-list approval, or credit packs (prices in-app). Configuring your own model API key makes model calls cost zero Loomy credits."},
 {"question":"Do I absolutely need an invite code to log in?","answer":"Yes. The quick-start doc says: open the client, enter an invite code, and you're in. Sources include the dedicated code on the ai-bot.cn listing (claimed extra 10,000 credits — verify actual distribution) and share links; the waiting-list approval path is another channel."},
 {"question":"Do model calls burn credits if I use my own API key?","answer":"No. The docs are explicit: when you configure your own model-provider API key, related model calls typically do not consume Loomy credits. Keys are stored on your device only — Loomy never hosts or uploads them."},
 {"question":"How is '50 tasks for 5,000 credits' calculated?","answer":"The official example pipeline: search and organize multiple information categories for a topic, compile a report saved locally, email a budget request, then roughly 10 rounds of follow-up email. That entire chain counts as one task; 5,000 credits supports about 50 of them. Longer tasks, bigger context and more model calls raise per-task cost, so real counts land below 50."},
 {"question":"Does Loomy upload my files to the cloud?","answer":"No. Loomy uses directory-level authorization: files stay local, the AI only operates inside authorized directories, and it asks consent before touching anything else. Custom API keys are stored locally too."},
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
    "category": "ai-agent",
    "date_published": TODAY,
    "tags": ["Loomy", "科大讯飞", "桌面AI智能体", "AI Agent", "办公自动化", "免费积分", "远程控制", "飞书", "钉钉", "AI工作搭子"],
    "icon": "🦦",
    "excerpt_zh": "科大讯飞桌面AI智能体Loomy免费下载：下载即送5000体验积分（官方口径约50次办公任务），分享好友双方各+5000，配自有API Key不扣积分；内置MiniMax-M2.5/豆包/DeepSeek-v3.2/Qwen3.5-Plus，目录级授权文件留本地，微信/飞书/钉钉远程操控。",
    "excerpt_en": "iFlytek's Loomy desktop AI agent, free to download: 5,000 trial credits on download (official docs: ~50 office tasks), +5,000 per friend referral (both sides), BYO API key costs zero credits. Ships MiniMax-M2.5/Doubao/DeepSeek-v3.2/Qwen3.5-Plus; directory-level auth keeps files local; remote control via WeChat/Feishu/DingTalk.",
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
