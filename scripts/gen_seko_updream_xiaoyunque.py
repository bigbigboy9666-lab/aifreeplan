#!/usr/bin/env python3
"""Generate the 'Seko / updream / Xiaoyunque free-tier comparison (2026)' guide.

Data sources (pulled live 2026-10-08 from ai-bot.cn /sites/{80357 updream, 58360 Seko,
72152 Xiaoyunque} + official seko.sensetime.com + xyq.jianying.com):

- Seko (SenseTime, seko.sensetime.com): "创编一体、多剧集生成" AI video-creation agent.
  Freemium, credit (points) based. Free members: daily-login bonus credits.
  Standard member first-purchase ~CNY 39/month (500 credits); Premium ~CNY 195/month
  (3000 credits, up to 50 episodes); Enterprise custom (up to 100 episodes).
  Aggregates Seedance 2.0 / Kling (可灵) / Vidu / Wan / PixVerse / Hailuo.
  SekoTalk: multi-person lip-sync, single shot up to 60s, 60 voice timbres.
  SekoIDX cross-shot / cross-episode character consistency. Seko 3.0 shipped at
  WAIC 2026-07 (canvas Agent + skill community + multi-language export).
  Scale: 1,000,000+ creators, 1,300 enterprise customers (as of 2026-07).
- updream (Bilibili, updream.cn): pro AI short-drama / video creation workbench
  (long-memory Agent, skill library, boundless canvas). Beta, requires Bilibili
  account + invite code. Credit-based; new users get 5000 free credits on
  signup; top-up packs: 600/CNY6, 3000/CNY30, 9800/CNY98, 19800/CNY198,
  32800/CNY328, 64800/CNY648. One-click export/post to Bilibili.
- Xiaoyunque ("Little Lark", ByteDance Jianying/CapCut team, xyq.jianying.com):
  "one line to a hit" content-creation Agent. Android app + web. Daily login
  grants 120 free credits ~= 12 smart videos/day. Core features currently
  free (limited-time). 200+ commercial-usable digital humans, 19 languages &
  dialects, 15-60s short videos. Backed by Doubao, DeepSeek, in-house
  Seedance 2.0 video + Seedream 5.0 image models.

Positioning: this is the "AI short-drama / video-creation agent" free-tier
category, NOT yet covered on the site (existing video guides are raw
generation tools: Runway/Pika/可灵/海螺/Seedance/LibTV). Not a duplicate.
"""
import os, sys, json
from datetime import datetime

sys.path.insert(0, '/home/ubuntu/aifreeplan/scripts')
from write_guide import generate_guide_html

SLUG = "seko-updream-xiaoyunque-free-comparison-2026"
TODAY = "2026-10-08"

TITLE_ZH = "Seko、updream、小云雀三大 AI 短剧/视频创作 Agent 免费额度对比（2026）：0 元起步谁最划算"
TITLE_EN = "Seko vs updream vs Xiaoyunque: Free-Tier Comparison of 3 AI Short-Drama / Video Creation Agents (2026)"

DESC_ZH = "商汤 Seko、B站 updream、字节剪映小云雀——三个刚火起来的 AI 视频/短剧创作 Agent，免费额度差别很大。本文列出三家的注册礼、每日登录赠积分、付费入门价（¥39/月起 vs 注册送 5000 积分 vs 每天 120 积分）、支持的视频模型和数字人数量，帮你在 0 元起步阶段挑到最划算的那个。"
DESC_EN = "SenseTime Seko, Bilibili updream, and ByteDance Jianying's Xiaoyunque are three newly popular AI short-drama / video-creation agents with very different free tiers. This guide lists signup bonuses, daily-login credits, entry pricing (from CNY 39/mo vs 5,000 signup credits vs 120 credits/day), supported video models, and digital-human counts, so you can pick the best zero-cost start."

CONTENT_ZH = """<h1>Seko、updream、小云雀三大 AI 短剧/视频创作 Agent 免费额度对比（2026）</h1>

<p>2026 年「一句话出片」的 AI 短剧/视频创作 Agent 突然扎堆上线，<a href="https://ai-bot.cn/the-latest-ai-projects/">ai-bot.cn 最新 AI 项目榜</a>一口气挂了三个名字：<strong>商汤 Seko</strong>、<strong>哔哩哔哩 updream</strong>、<strong>字节剪映的小云雀</strong>。它们都不是「生成一个镜头」的老工具，而是从剧本、分镜、角色一致性、对口型到成片导出的全流程智能体，主打短剧量产、数字人口播和爆款复刻。区别在于<strong>免费额度给得谁多、门槛谁低</strong>。下面把三家的 0 元起步条件、每日免费、注册礼和付费入门价全部摊开（数字为 2026-10-08 抓取自官网与 ai-bot.cn 条目）。</p>

<h2>三家免费额度速览</h2>

<table>
<tr><th>项目</th><th>Seko（商汤）</th><th>updream（B站）</th><th>小云雀（字节剪映）</th></tr>
<tr><td>定位</td><td>创编一体、多剧集生成</td><td>专业创作者工作台</td><td>一句话打造爆款</td></tr>
<tr><td>访问方式</td><td>云端在线（seko.sensetime.com）</td><td>内测：B站账号 + 邀请码</td><td>安卓 APP + 网页（xyq.jianying.com）</td></tr>
<tr><td>注册/新人礼</td><td>新人注册礼包（免费积分）</td><td>注册送 <strong>5000 积分</strong></td><td>核心功能限时免费</td></tr>
<tr><td>每日免费</td><td>每日登录赠积分（登录即得）</td><td>无明确每日额度（靠新人 5000 + 充值包）</td><td>每日登录领 <strong>120 积分 ≈ 12 个智能视频</strong></td></tr>
<tr><td>付费入门</td><td>标准首购约 <strong>¥39/月（500 积分）</strong>；高级约 ¥195/月（3000 积分，最多 50 集）</td><td>积分包 ¥6/600 起，最高 ¥648/64800</td><td>当前核心功能免费，会员另计</td></tr>
<tr><td>聚合视频模型</td><td>Seedance 2.0、可灵、Vidu、Wan、PixVerse、海螺</td><td>Seedance、可灵、Wan 2.7 等十余款</td><td>Seedance 2.0/2.5、Seedream 5.0、豆包、DeepSeek</td></tr>
<tr><td>特色能力</td><td>SekoIDX 角色一致性 + SekoTalk 多人对口型（单镜头最长 60 秒、60 种音色）</td><td>长记忆 Agent + 技能库 + 无界画布，一键投稿 B站</td><td>200+ 可商用数字人、19 种语言/方言、15-60 秒成片</td></tr>
</table>

<h2>Seko：多剧集量产 + 角色不「变脸」</h2>

<p>Seko 是商汤推出的「一人剧组」AI 导演系统，行业首个强调<strong>创编一体 + 多剧集生成</strong>的智能体。它最硬核的两点是 <strong>SekoIDX</strong>（角色跨分镜、跨剧集形象统一，杜绝换脸穿帮）和 <strong>SekoTalk</strong>（两人以上精准对口型，单镜头最长 60 秒、内置 60 种音色）。它聚合了 Seedance 2.0、可灵、Vidu、Wan、PixVerse、海螺多家模型按需调度，避免被单一模型锁死。<strong>免费侧</strong>：标准会员首购约 <strong>¥39/月送 500 积分</strong>，高级约 ¥195/月送 3000 积分（支持最多 50 集连续创作），企业版支持最多 100 集；免费会员每日登录可领积分。规模上，截至 2026 年 7 月已聚集 100 万+ 创作者、1300 家企业客户。Seko 3.0（2026 年 7 月 WAIC 发布）新增画布 Agent、技能社区和多语种出海成片。适合：想做<strong>连载短剧/漫剧、角色要长期一致</strong>的团队。</p>

<h2>updream：注册送 5000 积分，但要 B站账号 + 邀请码</h2>

<p>updream 是 B站（哔哩哔哩）面向专业创作者的一站式 AI 视频工作台，主打<strong>长记忆 Agent、技能库、无界画布</strong>三大能力，创作过程可非线性回溯修改。它和 B站生态打通，成片可一键投稿 B站。免费方面最实在：<strong>新用户注册直接送 5000 积分</strong>，之后按积分包续充（<strong>600 积分 ¥6、3000 ¥30、9800 ¥98、19800 ¥198、32800 ¥328、64800 ¥648</strong>）。代价是<strong>目前处于内测</strong>，注册需要 B站账号 + 邀请码，不是想进就能进。适合：已经在 B站生态、想做<strong>系列化短剧/动画概念/影视前期预演</strong>的专业创作者。</p>

<h2>小云雀：每天 120 积分，零门槛白嫖最狠</h2>

<p>小云雀是字节跳动旗下剪映团队推出的「一句话打造一个爆款」内容创作 Agent，安卓 APP + 网页双端，接入豆包、DeepSeek 及自研 <strong>Seedance 2.0/2.5 视频模型</strong>和 <strong>Seedream 5.0 图像模型</strong>。它的免费策略是三者里对小白最友好的：<strong>每日登录领 120 积分，约可生成 12 个智能视频</strong>，且核心功能目前<strong>限时免费</strong>。能力上支持 15-60 秒短视频、<strong>200+ 可商用数字人形象、19 种语言及方言口播</strong>、爆款复刻（输入链接自动解析同款）、AI 设计（一句指令批量出海报/商品图）、照片会说话。适合：自媒体博主、电商营销、教育工作者，要<strong>高频、低成本、批量</strong>产出短视频的人。</p>

<h2>怎么选（0 元起步）</h2>

<ul>
<li><strong>想白嫖每天不限量产短视频/数字人口播</strong>：选 <strong>小云雀</strong>——每天 120 积分（≈12 个视频）+ 核心功能限时免费，零门槛，无需邀请码。</li>
<li><strong>想做连载短剧、角色跨集不能变脸</strong>：选 <strong>Seko</strong>——SekoIDX + 多剧集（高级档 50 集、企业 100 集）+ SekoTalk 多人对口型，入门 ¥39/月起。</li>
<li><strong>已在 B站生态、要专业工作台</strong>：选 <strong>updream</strong>——注册送 5000 积分 + 一键投稿 B站，但要内测邀请码。</li>
</ul>

<p>一个通用建议：三家额度都在快速调整（尤其小云雀「限时免费」、updream「内测」），注册后尽快把想要的模型档位和数字人额度跑一遍，避免政策变动。</p>

<h2>常见问题</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q：三家哪个免费额度最划算？</div>
<div class="faq-a">看用途。纯免费日产短视频/数字人口播，小云雀每天 120 积分（≈12 个视频）最香；想要一次性大额积分池，updream 注册送 5000 积分；想连载短剧且接受付费入门，Seko ¥39/月（500 积分）起步。三家都能 0 元开账号。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q：updream 一定要 B站账号和邀请码吗？</div>
<div class="faq-a">是的，updream 目前是内测阶段，注册需要 B站（哔哩哔哩）账号 + 邀请码。这也是它「注册送 5000 积分」的门槛。没有邀请码就只能先蹲小云雀或 Seko。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q：生成的视频/短剧可以商用吗？</div>
<div class="faq-a">小云雀提供 200+ 可商用数字人；Seko 付费会员通常带商用授权、企业版更全；updream 以 B站投稿为主要场景。具体商用范围以各自官网/会员协议为准，发布前确认。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q：需要很强的电脑配置吗？</div>
<div class="faq-a">都不需要。三家都是云端在线平台（小云雀另有安卓 APP），浏览器打开官网即可，生成在云端跑，不占本地算力。</div>
</div>
</div>

<h2>结论</h2>

<p>2026 年这赛道「白嫖窗口」很明显：<strong>小云雀每天 120 积分 + 限时免费</strong>是给普通创作者的最优免费档；<strong>updream 注册送 5000 积分</strong>是最大的一次性新人池（但要 B站账号 + 邀请码）；<strong>Seko ¥39/月（500 积分）起</strong>是想要多剧集量产、角色不穿帮的专业向选择。建议先白嫖小云雀跑量，再用 Seko/updream 做需要长篇连载或 B站分发的项目。</p>
"""

CONTENT_EN = """<h1>Seko, updream & Xiaoyunque: Free-Tier Comparison of 3 AI Short-Drama / Video Creation Agents (2026)</h1>

<p>In 2026, "one line to a finished video" AI short-drama / video-creation agents started appearing in bulk. The <a href="https://ai-bot.cn/the-latest-ai-projects/">ai-bot.cn latest-AI-projects list</a> now carries three names at once: <strong>SenseTime's Seko</strong>, <strong>Bilibili's updream</strong>, and <strong>ByteDance Jianying's Xiaoyunque ("Little Lark")</strong>. None of these is a "generate one shot" tool — they are full-pipeline agents covering script, storyboards, character consistency, lip-sync, and export, aimed at short-drama production, digital-human talking-heads, and hit-video replication. The difference is <strong>how generous the free tier is and how low the barrier</strong>. Below is a full breakdown of each one's zero-cost start, daily free quota, signup bonus, and entry price (numbers pulled 2026-10-08 from the official sites and the ai-bot.cn entries).</p>

<h2>Free-tier at a glance</h2>

<table>
<tr><th>Item</th><th>Seko (SenseTime)</th><th>updream (Bilibili)</th><th>Xiaoyunque (ByteDance Jianying)</th></tr>
<tr><td>Positioning</td><td>Create-and-edit, multi-episode generation</td><td>Pro creator workbench</td><td>One line to a hit</td></tr>
<tr><td>Access</td><td>Cloud web (seko.sensetime.com)</td><td>Beta: Bilibili account + invite code</td><td>Android app + web (xyq.jianying.com)</td></tr>
<tr><td>Signup / new-user bonus</td><td>New-user gift pack (free credits)</td><td><strong>5,000 free credits</strong> on signup</td><td>Core features free (limited-time)</td></tr>
<tr><td>Daily free</td><td>Daily-login bonus credits</td><td>No clear daily quota (relies on the 5,000 signup + top-ups)</td><td>Daily login grants <strong>120 credits ~= 12 smart videos</strong></td></tr>
<tr><td>Entry price</td><td>Standard first-purchase ~<strong>CNY 39/mo (500 credits)</strong>; Premium ~CNY 195/mo (3,000 credits, up to 50 episodes)</td><td>Credit packs from CNY 6 / 600 up to CNY 648 / 64,800</td><td>Core features free for now; membership separate</td></tr>
<tr><td>Video models aggregated</td><td>Seedance 2.0, Kling, Vidu, Wan, PixVerse, Hailuo</td><td>Seedance, Kling, Wan 2.7 and 10+ more</td><td>Seedance 2.0/2.5, Seedream 5.0, Doubao, DeepSeek</td></tr>
<tr><td>Signature capability</td><td>SekoIDX character consistency + SekoTalk multi-person lip-sync (shot up to 60s, 60 timbres)</td><td>Long-memory Agent + skill library + boundless canvas, one-click post to Bilibili</td><td>200+ commercial digital humans, 19 languages/dialects, 15-60s clips</td></tr>
</table>

<h2>Seko: multi-episode production without "face-swap" breaks</h2>

<p>Seko is SenseTime's "one-person film crew" AI director system — the first agent that stresses <strong>create-and-edit-in-one plus multi-episode generation</strong>. Its two hardest features are <strong>SekoIDX</strong> (characters stay consistent across shots and episodes, no face-swap glitches) and <strong>SekoTalk</strong> (multi-person lip-sync, up to 60s per shot, 60 built-in timbres). It aggregates Seedance 2.0, Kling, Vidu, Wan, PixVerse, and Hailuo and dispatches them on demand, so you are not locked to one model. <strong>Free side</strong>: the Standard tier's first purchase is about <strong>CNY 39/month for 500 credits</strong>, Premium about CNY 195/month for 3,000 credits (up to 50 continuous episodes), and Enterprise supports up to 100 episodes; free members get a daily-login credit bonus. As of 2026-07 it has 1,000,000+ creators and 1,300 enterprise customers. Seko 3.0 (shipped at WAIC 2026-07) adds a canvas Agent, a skill community, and multi-language export. Best for teams making <strong>serialized short-dramas / comic-dramas where characters must stay consistent</strong>.</p>

<h2>updream: 5,000 free credits, but you need a Bilibili account + invite code</h2>

<p>updream is Bilibili's one-stop AI video workbench for professional creators, built on <strong>long-memory Agent, a skill library, and a boundless canvas</strong>; the process supports non-linear, retroactive edits. It is wired into the Bilibili ecosystem, so finished works can be posted to Bilibili in one click. The most tangible free offer: <strong>new users get 5,000 credits on signup</strong>, then top up by credit pack (<strong>CNY 6 / 600, CNY 30 / 3,000, CNY 98 / 9,800, CNY 198 / 19,800, CNY 328 / 32,800, CNY 648 / 64,800</strong>). The catch is that it is still in <strong>beta</strong> — signup requires a Bilibili account plus an invite code, so you cannot just walk in. Best for creators already in the Bilibili ecosystem who want a <strong>professional workbench for serialized short-dramas / animation concepts / pre-visualization</strong>.</p>

<h2>Xiaoyunque: 120 credits a day — the most generous zero-barrier freebie</h2>

<p>Xiaoyunque ("Little Lark") is a content-creation Agent from ByteDance's Jianying/CapCut team, the "one line to a hit" experience, available as an Android app and web app. It runs on Doubao, DeepSeek, and in-house <strong>Seedance 2.0/2.5 video</strong> and <strong>Seedream 5.0 image</strong> models. Its free strategy is the friendliest of the three for newcomers: <strong>120 free credits on every daily login, roughly 12 smart videos/day</strong>, and core features are currently <strong>free (limited-time)</strong>. Capabilities include 15-60s short videos, <strong>200+ commercial-usable digital humans across 19 languages and dialects</strong>, hit-video replication (paste a link, it auto-replicates the style), AI design (batch posters / product images from one prompt), and "photo talking". Best for creators, e-commerce marketers, and educators who need <strong>high-frequency, low-cost, batch</strong> short-video output.</p>

<h2>Which to pick (starting at zero cost)</h2>

<ul>
<li><strong>Want unlimited-ish daily free short videos / digital-human talking-heads</strong>: pick <strong>Xiaoyunque</strong> — 120 credits/day (~12 videos) + core features free, no invite code.</li>
<li><strong>Want serialized short-dramas where characters must not change across episodes</strong>: pick <strong>Seko</strong> — SekoIDX + multi-episode (Premium 50, Enterprise 100) + SekoTalk, entry from CNY 39/mo.</li>
<li><strong>Already in the Bilibili ecosystem and want a pro workbench</strong>: pick <strong>updream</strong> — 5,000 credits on signup + one-click Bilibili posting, but beta invite code required.</li>
</ul>

<p>One universal tip: all three quotas are shifting fast (Xiaoyunque is "limited-time free", updream is "beta"), so once you register, run through the model tiers and digital-human quotas you care about early before policy changes.</p>

<h2>Frequently asked questions</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: Which of the three has the best free tier?</div>
<div class="faq-a">It depends on use. For pure free daily short-video / digital-human output, Xiaoyunque's 120 credits/day (~12 videos) wins. For a one-time large credit pool, updream gives 5,000 credits on signup. For serialized short-dramas and you are okay paying to start, Seko from CNY 39/mo (500 credits). All three let you open an account for free.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Does updream really require a Bilibili account and an invite code?</div>
<div class="faq-a">Yes. updream is currently in beta; signup needs a Bilibili account plus an invite code. That is also the gate on its "5,000 free credits on signup". Without an invite code, start with Xiaoyunque or Seko.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Can the generated videos / short-dramas be used commercially?</div>
<div class="faq-a">Xiaoyunque offers 200+ commercial-usable digital humans; Seko paid tiers usually include commercial licensing, with Enterprise more complete; updream centers on posting to Bilibili. Exact commercial scope follows each site's / membership's terms — confirm before publishing.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Do I need a powerful computer?</div>
<div class="faq-a">No. All three are cloud platforms (Xiaoyunque also has an Android app). Open the site in a browser and generation runs in the cloud — no local GPU or heavy specs.</div>
</div>
</div>

<h2>Bottom line</h2>

<p>In 2026 the "free window" in this lane is obvious: <strong>Xiaoyunque's 120 credits/day + limited-time free</strong> is the best free tier for everyday creators; <strong>updream's 5,000-credit signup bonus</strong> is the largest one-time new-user pool (but needs a Bilibili account + invite code); and <strong>Seko from CNY 39/mo (500 credits)</strong> is the pro pick for multi-episode production without character breaks. Recommended path: farm Xiaoyunque for volume on day one, then use Seko or updream for long serialized projects or Bilibili distribution.</p>
"""

FAQ_ZH = [
 {"question":"三家哪个免费额度最划算？","answer":"看用途。纯免费日产短视频/数字人口播，小云雀每天 120 积分（≈12 个视频）最香；想要一次性大额积分池，updream 注册送 5000 积分；想连载短剧且接受付费入门，Seko ¥39/月（500 积分）起步。三家都能 0 元开账号。"},
 {"question":"updream 一定要 B站账号和邀请码吗？","answer":"是的，updream 目前是内测，注册需要 B站账号 + 邀请码，这也是它「注册送 5000 积分」的门槛。没有邀请码就先蹲小云雀或 Seko。"},
 {"question":"生成的视频/短剧可以商用吗？","answer":"小云雀提供 200+ 可商用数字人；Seko 付费会员通常带商用授权、企业版更全；updream 以 B站投稿为主要场景。具体以各自官网/会员协议为准。"},
 {"question":"需要很强的电脑配置吗？","answer":"不需要。三家都是云端在线平台（小云雀另有安卓 APP），浏览器打开即可，生成在云端跑，不占本地算力。"},
]
FAQ_EN = [
 {"question":"Which of the three has the best free tier?","answer":"Depends on use. For pure free daily short-video / digital-human output, Xiaoyunque's 120 credits/day (~12 videos) wins. For a one-time large credit pool, updream gives 5,000 on signup. For serialized short-dramas and you accept paying to start, Seko from CNY 39/mo (500 credits). All three open free accounts."},
 {"question":"Does updream require a Bilibili account and an invite code?","answer":"Yes. updream is in beta; signup needs a Bilibili account plus an invite code, which gates its 5,000-credit signup bonus. Without an invite code, start with Xiaoyunque or Seko."},
 {"question":"Can the generated videos be used commercially?","answer":"Xiaoyunque offers 200+ commercial digital humans; Seko paid tiers usually include commercial licensing (Enterprise more complete); updream centers on posting to Bilibili. Follow each site's terms."},
 {"question":"Do I need a powerful computer?","answer":"No. All three are cloud platforms (Xiaoyunque also has an Android app). Open in a browser; generation runs in the cloud, no local GPU needed."},
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
    "category": "video",
    "date_published": TODAY,
    "tags": ["Seko", "updream", "小云雀", "Xiaoyunque", "AI短剧", "视频创作Agent", "数字人", "免费额度", "对比", "SenseTime", "Bilibili", "ByteDance", "Seedance", "免费"],
    "icon": "🎬",
    "excerpt_zh": "商汤 Seko、B站 updream、字节剪映小云雀三大 AI 短剧/视频创作 Agent 免费额度对比：小云雀每天 120 积分≈12 个视频、updream 注册送 5000 积分、Seko ¥39/月起，0 元起步谁最划算。",
    "excerpt_en": "Free-tier comparison of three AI short-drama / video-creation agents: Xiaoyunque gives 120 credits/day (~12 videos), updream gives 5,000 signup credits, Seko starts at CNY 39/mo. Which zero-cost start is best?",
    "faq_zh": FAQ_ZH,
    "faq_en": FAQ_EN,
}

for path in ('/home/ubuntu/aifreeplan/public/data/guides.json',
             '/home/ubuntu/aifreeplan/dist/data/guides.json'):
    if os.path.exists(path):
        try:
            with open(path, encoding='utf-8') as fh:
                d = json.load(fh)
            guides = d.get('guides', [])
            d['guides'] = [g for g in guides if g.get('slug') != SLUG]
            d['guides'].insert(0, ENTRY)
            d['updatedAt'] = datetime.now().isoformat()
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(d, f, ensure_ascii=False, indent=2)
            print(f"registered into {path} ({len(d['guides'])} guides)")
        except Exception as e:
            print(f"WARN could not register into {path}: {e}")

for path in ('/home/ubuntu/aifreeplan/data/guides.json',):
    if os.path.exists(path):
        try:
            with open(path, encoding='utf-8') as fh:
                d = json.load(fh)
            guides = d.get('guides', [])
            d['guides'] = [g for g in guides if g.get('slug') != SLUG]
            d['guides'].insert(0, ENTRY)
            d['updatedAt'] = datetime.now().isoformat()
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(d, f, ensure_ascii=False, indent=2)
            print(f"registered into {path} ({len(d['guides'])} guides)")
        except Exception as e:
            print(f"WARN could not register into {path}: {e}")

print(f"Generated {SLUG} (date {TODAY})")
print(f"  zh content raw chars: {len(CONTENT_ZH)}")
print(f"  en content raw chars: {len(CONTENT_EN)}")
