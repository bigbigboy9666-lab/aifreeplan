#!/usr/bin/env python3
"""Generate the 'Free AI App Builder Comparison 2026' guide via the write_guide.py HTML template.
Data source: official pricing pages fetched 2026-09-21 (v0.dev, lovable.dev, bolt.new, replit.com).
"""
import os, sys
from datetime import datetime

sys.path.insert(0, '/home/ubuntu/aifreeplan/scripts')
from write_guide import generate_guide_html

SLUG = "ai-app-builder-free-comparison-2026"
TODAY = datetime.now().strftime('%Y-%m-%d')

TITLE_ZH = "免费AI应用生成器对比：v0、Lovable、Bolt、Replit 2026免费版深度横评"
TITLE_EN = "Free AI App Builder Comparison 2026: v0 vs Lovable vs Bolt vs Replit — Free Tiers Reviewed"

DESC_ZH = "实测对比 v0、Lovable、Bolt.new、Replit 四款主流 AI 应用生成器的免费额度、刷新周期、限制与付费门槛。v0 送 $5/月+7 条/天，Lovable 5 积分/天+20 Cloud/月，Bolt 30 万 token/天，Replit Free Mode 30 小时/月——帮你判断哪款白嫖最划算。"
DESC_EN = "Hands-on comparison of the free tiers of four leading AI app builders: v0 ($5/mo + 7 messages/day), Lovable (5 build credits/day + 20 Cloud/mo), Bolt.new (300K tokens/day), and Replit (30 hours Free Mode/mo). Concrete quotas, limits, and paid-entry prices to tell you which one is best to ride for free."

CONTENT_ZH = """<h1>免费AI应用生成器对比：v0、Lovable、Bolt、Replit 2026免费版深度横评</h1>
<p>2026 年，"用一句话生成一个网站 / 小程序"已经从演示视频变成了日常工具。v0、Lovable、Bolt.new、Replit 是"AI App Builder（应用生成器）"这一类里用户量最大的四款，但它们免费额度差异极大、限制点也不一样，踩坑的人不少。本文基于 2026 年 9 月各家官方定价页的实测数据，把每家的免费额度、刷新周期、能做什么、不能做什么讲清楚，帮你判断哪款白嫖最划算。</p>
<p>先说结论：<strong>纯出页面 / 落地页选 v0；要完整前后端+数据库选 Lovable；额度最大方、适合快速拼原型选 Bolt.new；要跑真 Python/Node 全栈逻辑选 Replit。</strong>下面拆开讲。</p>

<h2>四款工具免费版速览表（2026-09 官方数据）</h2>
<table>
<tr><th>工具</th><th>免费额度</th><th>刷新周期</th><th>能生成什么</th><th>明显限制</th><th>入门付费</th></tr>
<tr><td><strong>v0（Vercel）</strong></td><td>$5/月 积分 + 7 条消息/天</td><td>月 / 天</td><td>React 组件、落地页、UI 界面</td><td>免费版不含数据库/全栈逻辑</td><td>Plus 约 $20/月</td></tr>
<tr><td><strong>Lovable</strong></td><td>5 构建积分/天（≤30/月）+ 20 Cloud 积分/月 + 4 条 AI 功能积分</td><td>天 / 月</td><td>前后端完整 App + Supabase 数据库</td><td>额度小，复杂项目很快见底</td><td>Builder $30/月</td></tr>
<tr><td><strong>Bolt.new（StackBlitz）</strong></td><td>30 万 token/天 + 100 万 token/月</td><td>天 / 月</td><td>全栈 Web App / 桌面端</td><td>带 Bolt 品牌水印、10MB 上传、33.3 万 web 请求/月</td><td>Pro $25/月起</td></tr>
<tr><td><strong>Replit</strong></td><td>Free Mode 30 小时/月 + 60 个项目</td><td>月</td><td>真全栈 App（Python/Node）+ 云数据库</td><td>免费资源有限、高峰排队</td><td>Core $20/月</td></tr>
</table>
<p>注：额度随时可能调整，以上为 2026-09-21 各家定价页快照。v0 的"$5 积分"是按模型 token 计费的预算，"7 条/天"是消息条数上限而非 token 数，两者互相独立。</p>

<h2>v0（Vercel）：组件级精修 + 一键部署</h2>
<p>v0 由 Vercel（Next.js 母公司）出品，核心是把一句自然语言变成可运行的 React/Next.js 组件。免费版 $0/月，但内置 <strong>$5 月度积分</strong>，并限制 <strong>7 条消息/天</strong>。积分用完就得等下月或付费（Plus 档约 $20/月起）。</p>
<p>v0 的免费杀手锏是<strong>Design Mode 可视化编辑 + 一键部署到 Vercel + GitHub 同步</strong>：你不用自己配域名、不用管 CI/CD，生成完点一下就有 URL 了。模型侧提供 v0 Mini（$0.20/1M 输入）到 v0 Pro（$2/1M 输入）等多档，免费版默认按积分扣，适合"快速出个漂亮落地页 / 管理后台界面"。不适合：需要后端逻辑、数据库、用户系统的全栈应用——这些要么付费、要么得自己接后端。</p>

<h2>Lovable：对话式生成完整前后端</h2>
<p>Lovable 走的是"整站对话生成"路线：你描述需求，它直接把前端 + 后端 + 数据库（Supabase）一起搭好。免费版额度很克制——<strong>5 个构建积分/天（每月封顶 30 个）+ 20 个 Cloud 积分/月 + 4 条用于 App 内 AI 功能的积分</strong>。一个稍复杂的项目几条消息就能把这 30 个/月的构建积分吃掉，之后只能看着余额等明天刷新。</p>
<p>它适合"我要一个带登录、带数据表、能上线的小 SaaS"这类需求，且不想碰代码。付费档 <strong>Builder $30/月、Cloud $25/月</strong>，积分按月加到余额，余额里未用完的积分会滚存（月付 2 个月内有效）。注意：Lovable 是"按积分扣"，不同 Plan 的 1 个积分价值不同，别拿免费 Plan 的积分去衡量付费 Plan 的性价比。</p>

<h2>Bolt.new（StackBlitz）：额度最大方 + 全栈 Web</h2>
<p>Bolt.new 是四家里<strong>免费额度最慷慨</strong>的：<strong>30 万 token/天 + 100 万 token/月</strong>，且免费就能开公开/私有项目、跑数据库、部署网站。限制在于：免费生成的网站带 <strong>Bolt 品牌水印</strong>、上传 <strong>10MB 上限</strong>、每月 <strong>33.3 万 web 请求</strong>、数据库无限量。Pro $25/月起后无每日 token 限制、从 100 万 token/月起、去水印、100MB 上传。</p>
<p>Bolt 底层是 StackBlitz 的 WebContainer（浏览器里跑 Node），所以它更像"能跑真后端"的全栈生成器，适合做后台、带 API 的小工具、数据看板。缺点：免费版的品牌水印对"上线给客户看"的场景很扎眼，想抹掉就得上 Pro。</p>

<h2>Replit：跑真全栈 + 云数据库</h2>
<p>Replit 的定位是"AI + 真开发环境"，强项是<strong>能写、能跑真 Python/Node/Go 全栈逻辑</strong>并挂云数据库，不只是画页面。免费（Free Mode）每月给 <strong>30 小时 AI 对话 + 60 个项目</strong>，够你捣鼓几个小项目，但免费资源有限、高峰会排队。付费 <strong>Core $20/月（年付 $18/月）</strong>，含 $20 最强模型额度、Free Mode 30 小时、60 项目；<strong>Pro $100/月（年付 $90/月）</strong>含 10 并行 Agent、100 美元模型额度、最多 15 协作者。</p>
<p>Replit 适合"我要一个真能跑脚本、连数据库、部署到 Replit 云上的后端服务"，比另外三家更接近"真 IDE + 云"。纯前端 UI 精修不是它的强项。</p>

<h2>该选哪个？按场景对号入座</h2>
<ul>
<li><strong>出漂亮落地页 / 管理界面，不想管部署</strong> → v0（Design Mode + 一键 Vercel，$5/月起）。</li>
<li><strong>要带登录、带数据表的完整小 SaaS，几乎不碰代码</strong> → Lovable（对话式全栈 + Supabase）。</li>
<li><strong>额度要大、快速拼全栈原型、能接受水印</strong> → Bolt.new（30 万 token/天最顶）。</li>
<li><strong>跑真后端脚本 + 云数据库 + 团队协作</strong> → Replit（真 IDE + 云，Core $20 起）。</li>
</ul>

<h2>白嫖最大化技巧</h2>
<ol>
<li><strong>跨家错峰用额度</strong>：v0 月度 $5、Lovable 日刷 5 积分、Bolt 日刷 30 万 token——三家的"每天/每月重置"错开，一个小工具可以分三家做完，单家都不见底。</li>
<li><strong>先 Bolt 出骨架，再 v0 精修 UI</strong>：Bolt 免费额度大、适合先把全栈跑通；界面难看时拿设计稿丢给 v0 打磨组件，省 Lovable 的昂贵积分。</li>
<li><strong>别在免费额度里试全功能</strong>：Lovable 的 4 条"App 内 AI 功能积分"是给用户试用你 App 的，别自己一直点，留给真实用户。</li>
<li><strong>付费档先买月付</strong>：v0/Replit 年付比月付省约 10%（Replit Core $20 年付 $18），Lovable 积分会滚存，短期项目月付更灵活。</li>
</ol>

<h2>常见误区与坑</h2>
<ul>
<li><strong>"免费 = 不限"是错觉</strong>：四家全部限量，v0 7 条/天、Lovable 30 积分/月、Bolt 1M token/月、Replit 30 小时/月，谁都不是无限量。</li>
<li><strong>Bolt 免费版的水印</strong>：带 Bolt 品牌，给甲方/客户看会掉价，需上 Pro 去水印。</li>
<li><strong>Lovable 的"1 积分"不等价</strong>：免费 Plan 和付费 Plan 的积分价值不同，拿免费版积分估算付费性价比会算错。</li>
<li><strong>额度会悄悄改</strong>：本文数据为 2026-09-21 快照，v0 从"按消息数"到"$5 积分预算"在 2026 年改过口径，以官网实时为准。</li>
</ul>

<h2>FAQ</h2>
<div class="faq-section">
<div class="faq-item"><div class="faq-q">v0 免费版一天真的只有 7 条吗？</div><div class="faq-a">是的，v0 免费版限制 7 条消息/天，同时每月有 $5 的模型积分预算。两个限制独立：$5 用完或 7 条用完，先到先停。想提额得上 Plus（约 $20/月起）。</div></div>
<div class="faq-item"><div class="faq-q">Lovable 免费的 30 个积分够做几个完整 App？</div><div class="faq-a">5 个构建积分/天、每月封顶 30 个。一个稍复杂的带登录+数据表的 App 可能 10~20 条消息就做完，所以 30 个/月大约够认真做 1~2 个中等项目，简单页面则能多做几个。复杂项目基本要等次日刷新。</div></div>
<div class="faq-item"><div class="faq-q">Bolt.new 免费版为什么额度最大？</div><div class="faq-a">Bolt 是四家里唯一按"token"放量的，免费给 30 万/天、100 万/月，换品牌水印+10MB 上传+33.3 万 web 请求这些限制。StackBlitz 用免费额度换生态渗透，是它一贯打法。</div></div>
<div class="faq-item"><div class="faq-q">Replit 的 Free Mode 30 小时是 AI 对话还是算力？</div><div class="faq-a">是 AI 对话（chat）时长，每月 30 小时，外加 60 个项目。真正跑代码的算力另算，免费资源有限、高峰会排队。要稳定跑真服务建议上 Core（$20/月，含 $20 最强模型额度）。</div></div>
<div class="faq-item"><div class="faq-q">这四款能不能免费商用？</div><div class="faq-a">四家都允许你用生成物做项目，但免费档通常带水印（Bolt）、限请求数（Bolt 33.3 万 web 请求/月）、限资源（Replit 免费算力有限）。正式商用上线前，确认你的用量不超免费上限，或升级到对应付费档。</div></div>
</div>

<h2>总结</h2>
<p>免费 AI 应用生成器没有"全能王"，只有"场景适配"。<strong>v0</strong> 赢在 UI 精修和零部署，<strong>Lovable</strong> 赢在对话式全栈，<strong>Bolt.new</strong> 赢在额度最大方，<strong>Replit</strong> 赢在真后端+云。先把上面那张速览表存下来，按"我要出页面 / 要全栈 / 要跑脚本"三条线对号，再用本文的白嫖技巧错峰用额度，基本能用零成本做出一个能跑的小产品。</p>"""

CONTENT_EN = """<h1>Free AI App Builder Comparison 2026: v0 vs Lovable vs Bolt vs Replit — Free Tiers Reviewed</h1>
<p>By 2026, "prompt your way into a working website" has gone from demo video to daily tool. <strong>v0, Lovable, Bolt.new, and Replit</strong> are the four highest-traffic names in the "AI app builder" category, but their free tiers differ wildly and the traps differ too. This guide is based on hands-on checks of each vendor's official pricing page as of September 2026, and breaks down each one's free quota, refresh cycle, what you can build, and what you can't — so you can tell which one is actually worth riding for free.</p>
<p>Bottom line up front: <strong>v0</strong> for polished pages and landing sites, <strong>Lovable</strong> for full front + back end + database, <strong>Bolt.new</strong> for the most generous quota and fast prototyping, and <strong>Replit</strong> for real Python/Node full-stack logic.</p>

<h2>Free-Tier Snapshot (official data, Sep 2026)</h2>
<table>
<tr><th>Tool</th><th>Free quota</th><th>Refresh</th><th>What it builds</th><th>Hard limits</th><th>Paid entry</th></tr>
<tr><td><strong>v0 (Vercel)</strong></td><td>$5/mo credit + 7 messages/day</td><td>month / day</td><td>React components, landing pages, UI</td><td>No free DB / full-stack logic</td><td>Plus ~$20/mo</td></tr>
<tr><td><strong>Lovable</strong></td><td>5 build credits/day (≤30/mo) + 20 Cloud credits/mo + 4 AI-feature credits</td><td>day / month</td><td>Full front + back-end app + Supabase DB</td><td>Small quota, drains fast on complex projects</td><td>Builder $30/mo</td></tr>
<tr><td><strong>Bolt.new (StackBlitz)</strong></td><td>300K tokens/day + 1M tokens/month</td><td>day / month</td><td>Full-stack web / desktop apps</td><td>Bolt watermark, 10MB upload, 333K web requests/mo</td><td>Pro $25/mo</td></tr>
<tr><td><strong>Replit</strong></td><td>Free Mode 30 hours/mo + 60 projects</td><td>month</td><td>Real full-stack apps (Python/Node) + cloud DB</td><td>Limited free resources, peak queuing</td><td>Core $20/mo</td></tr>
</table>
<p>Note: quotas change. This is a snapshot of each pricing page on 2026-09-21. v0's "$5 credit" is a token-budget and its "7 messages/day" is a message-count cap — the two limits are independent of each other.</p>

<h2>v0 (Vercel): component-level polish + one-click deploy</h2>
<p>v0, from Vercel (the Next.js company), turns a sentence into runnable React/Next.js components. The free tier is $0/month with a built-in <strong>$5 monthly credit</strong> and a <strong>7 messages/day</strong> cap. Run out of either and you wait for next month or pay (Plus is ~$20/mo).</p>
<p>v0's free superpowers are <strong>Design Mode visual editing + one-click deploy to Vercel + GitHub sync</strong>: you don't configure a domain or CI/CD, you click and get a URL. Model tiers run from v0 Mini ($0.20/1M input) up to v0 Pro ($2/1M input), and the free tier bills by credit. Great for "quickly produce a nice landing page or admin UI." Not great for: backend logic, databases, user systems — that part is paid or you wire up your own backend.</p>

<h2>Lovable: conversational full front + back end</h2>
<p>Lovable does "describe it and I'll build the whole site": you state the requirement, it scaffolds the front end + back end + database (Supabase) together. The free tier is stingy — <strong>5 build credits/day (capped at 30/month) + 20 Cloud credits/month + 4 credits for AI features inside your app</strong>. A moderately complex project burns the 30/month build credits in a handful of messages; after that you watch your balance until tomorrow's refresh.</p>
<p>It fits "I want a logged-in, data-backed little SaaS" without touching code. Paid is <strong>Builder $30/mo, Cloud $25/mo</strong>; credits add to a monthly balance and roll over (valid within 2 months on monthly plans). Careful: Lovable bills by credit, and one credit is not equal in value across plans — don't price the paid plan by the free plan's credits.</p>

<h2>Bolt.new (StackBlitz): the most generous quota + full-stack web</h2>
<p>Bolt.new is the <strong>most generous</strong> of the four: <strong>300K tokens/day + 1M tokens/month</strong>, and the free tier lets you open public/private projects, run databases, and host sites. The costs are: free sites carry a <strong>Bolt brand watermark</strong>, uploads cap at <strong>10MB</strong>, and you get <strong>333K web requests/month</strong> with unlimited databases. From Pro ($25/mo) you get no daily token cap, 1M+ tokens/month, no watermark, and 100MB uploads.</p>
<p>Under the hood is StackBlitz's WebContainer (Node running in the browser), so Bolt behaves like a real full-stack generator: back ends, APIs, dashboards. Downside: that free-tier brand watermark is ugly when you're showing a client — remove it via Pro.</p>

<h2>Replit: real full-stack + cloud DB</h2>
<p>Replit is "AI + real dev environment." Its strength is that it can <strong>write and run real Python/Node/Go full-stack logic</strong> and attach a cloud database — not just paint pages. Free (Free Mode) gives <strong>30 hours of AI chat/month + 60 projects</strong>, enough to tinker with a few small projects, but free resources are limited and you'll queue at peak. Paid: <strong>Core $20/mo ($18/mo billed annually)</strong> with $20 of top-tier model credit, 30h Free Mode, 60 projects; <strong>Pro $100/mo ($90/mo annual)</strong> with 10 parallel agents, $100 model credit, up to 15 collaborators.</p>
<p>Replit is for "I need a real script, a cloud DB, a deployed Replit cloud service" — it's the closest to a "real IDE + cloud" here. Pure front-end UI polish is not its thing.</p>

<h2>Which one, by use case</h2>
<ul>
<li><strong>Pretty landing page / admin UI, don't want to manage deploy</strong> → v0 (Design Mode + one-click Vercel, $5/mo entry).</li>
<li><strong>Full logged-in, data-backed little SaaS, barely touch code</strong> → Lovable (conversational full-stack + Supabase).</li>
<li><strong>Biggest quota, fast full-stack prototypes, watermark acceptable</strong> → Bolt.new (300K tokens/day is the most headroom).</li>
<li><strong>Real backend scripts + cloud DB + team collab</strong> → Replit (real IDE + cloud, Core $20 entry).</li>
</ul>

<h2>Maximize the free tiers</h2>
<ol>
<li><strong>Stagger across vendors.</strong> v0's monthly $5, Lovable's daily 5 credits, and Bolt's daily 300K tokens all reset on different cadences — split one small product across all three and none hits its floor.</li>
<li><strong>Prototype the skeleton in Bolt, polish UI in v0.</strong> Bolt's big free quota gets your full-stack running; hand ugly screens to v0 to refine components and save Lovable's expensive credits.</li>
<li><strong>Don't burn your real users' trial credits on yourself.</strong> Lovable's 4 "in-app AI feature credits" are meant for your end users trying the app — don't tap them all out yourself.</li>
<li><strong>Buy monthly before annual.</strong> v0/Replit annual is ~10% cheaper (Replit Core $20 vs $18 annual); Lovable credits roll over, so monthly is more flexible for short projects.</li>
</ol>

<h2>Common mistakes and traps</h2>
<ul>
<li><strong>"Free = unlimited" is a myth.</strong> All four are capped: v0 7 msgs/day, Lovable 30 credits/mo, Bolt 1M tokens/mo, Replit 30h/mo. None is unlimited.</li>
<li><strong>Bolt's free watermark</strong> carries the Bolt brand and hurts credibility in front of a client; Pro removes it.</li>
<li><strong>Lovable's "1 credit" isn't equal</strong> across plans — pricing the paid tier by free-tier credits miscalculates your cost.</li>
<li><strong>Quotas quietly change.</strong> This article is a 2026-09-21 snapshot; v0's model changed from "messages" to a "$5 credit budget" during 2026. Check live pricing.</li>
</ul>

<h2>FAQ</h2>
<div class="faq-section">
<div class="faq-item"><div class="faq-q">Does v0's free tier really only allow 7 messages a day?</div><div class="faq-a">Yes. v0's free tier caps 7 messages/day, plus a $5 monthly model-credit budget. The two limits are independent — whichever runs out first stops you. To lift the cap, go to Plus (~$20/mo).</div></div>
<div class="faq-item"><div class="faq-q">How many complete apps can Lovable's free 30 credits build?</div><div class="faq-a">5 build credits/day, capped at 30/month. A modest logged-in + data-backed app can take 10–20 messages, so the 30/month realistically covers 1–2 medium projects; simple pages get more. Complex projects mostly wait for the next day's refresh.</div></div>
<div class="faq-item"><div class="faq-q">Why is Bolt.new's free quota the largest?</div><div class="faq-a">Bolt is the only one that meters in tokens: 300K/day, 1M/month free, trading away a brand watermark, 10MB uploads, and a 333K web-requests/month cap. StackBlitz uses the free tier for ecosystem penetration.</div></div>
<div class="faq-item"><div class="faq-q">Is Replit's Free Mode 30 hours AI chat or compute?</div><div class="faq-a">It's AI chat time — 30 hours/month plus 60 projects. Actual code execution is metered separately; free resources are limited and you queue at peak. For a stable real service, move to Core ($20/mo, $20 top-tier model credit).</div></div>
<div class="faq-item"><div class="faq-q">Can I use any of these commercially for free?</div><div class="faq-a">All four let you use what you build, but the free tiers carry watermarks (Bolt), request caps (Bolt 333K web requests/mo), or resource limits (Replit free compute). Before a real commercial launch, confirm your usage stays under the free ceiling or upgrade to the matching paid tier.</div></div>
</div>

<h2>Bottom line</h2>
<p>There is no "do-it-all" free AI app builder — only scene fit. <strong>v0</strong> wins on UI polish and zero-deploy, <strong>Lovable</strong> on conversational full-stack, <strong>Bolt.new</strong> on the largest free quota, <strong>Replit</strong> on real back end + cloud. Save the snapshot table above, match yourself to "I need pages / I need full-stack / I need scripts," and stagger the quotas with the maximize tricks — you can ship a working little product for zero dollars.</p>"""

FAQ_ZH = ""
FAQ_EN = ""

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
print(f"  zh main text bytes: {len(CONTENT_ZH.encode('utf-8'))}")
print(f"  en main text bytes: {len(CONTENT_EN.encode('utf-8'))}")
