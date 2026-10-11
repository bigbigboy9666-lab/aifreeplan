#!/usr/bin/env python3
"""Generate the 'BinkBink (虎牙) vs Rosebud AI — AI game maker free-tier comparison (2026)' guide.

Data sources (pulled live 2026-10-09):
- ai-bot.cn/binkbink (虎牙 BinkBink, Android app): https://play.google.com/store/apps/details?id=com.huya.aigameforge
  - Huya's AI game-creation app. No code / art / dev team needed: one natural-language
    line generates a complete playable casual game in minutes, with auto art, game
    rules, levels and audio. Core = Remix iteration (text edits -> new version,
    human-machine co-creation). Categories: match-3, tower-defense, runner, sim,
    branching interactive-fiction, sandbox. One-click share link — friends play in
    browser, no install / no register. Built-in discovery feed (focus creators).
    No login required to start. Initial community 1K+ downloads (Play Store).
    Free to use (no credit gate published).
- Rosebud AI (rosebud.ai, web): https://rosebud.ai/pricing
  - Web AI game maker. Free "Newbie (free)" plan: 8,000 credits/week, no credit
    card, refills weekly in eligible regions; create / play / remix / share.
  - Paid (Stripe prices): Indie Dev $15/mo = 100,000 credits; 10x Dev $30/mo =
    300,000 credits; Pro $50/mo = 1,000,000 credits (code download + Windows/Steam
    export, "best value"); Scale/Enterprise $100/mo = 2,000,000 credits.
  - Credit costs (rough, editor shows per turn): ~2,000 for a Rosie (default AI)
    edit turn; ~20,000 with a premium model; 200–2,000 to generate an image /
    sprite animation; ~1,000 to generate a sound; 3D model and 360° skybox also
    consume credits.
  - 2.3M+ community games can be remixed. Commercial rights on 10x Dev and above
    (sell games / assets, publish anywhere, Rosebud takes no commission). Code
    download + Windows export on Pro and above; private projects on Indie Dev and
    above; brand-free hosting on 10x Dev and above. Referral: $10 off friend +
    $10 you, up to 5 friends. Paid plans: daily refresh credits (reset midnight
    PT, used first), monthly credits roll over once.

Positioning: this is the "AI game-creation tool" free-tier comparison category, NOT
yet covered on the site (no existing guide compares AI game makers). Not a duplicate.
"""
import os, sys, json
from datetime import datetime

sys.path.insert(0, '/home/ubuntu/aifreeplan/scripts')
from write_guide import generate_guide_html

SLUG = "binkbink-rosebud-ai-game-maker-free-comparison-2026"
TODAY = "2026-10-09"

TITLE_ZH = "BinkBink（虎牙）vs Rosebud AI：AI 做游戏工具免费额度对比（2026），0 元能做出几款可玩小游戏"
TITLE_EN = "BinkBink (Huya) vs Rosebud AI: Free-Tier Comparison of 2 AI Game-Maker Tools (2026)"

DESC_ZH = "虎牙 BinkBink（安卓 App）和 Rosebud AI（网页端）是两款「一句话生成完整可玩游戏」的 AI 做游戏工具，2026 年免费玩法差别很大：BinkBink 免登录直接用、无公开积分门槛、好友免安装免注册即玩、初期 1000+ 下载；Rosebud 免费版每周 8,000 积分（免绑卡、每周刷新），付费从 $15/月 起、230 万+ 社区游戏可 Remix。本文列清两家的免费额度、积分消耗、商用与导出权限，帮你在 0 元起步阶段选对工具。"
DESC_EN = "Huya's BinkBink (Android app) and Rosebud AI (web) are two 'one line to a playable game' AI game-makers with very different free plays in 2026: BinkBink is no-login with no published credit gate, friends play install-free / register-free, 1,000+ initial downloads; Rosebud's free tier gives 8,000 credits/week (no card, weekly refill) and paid starts at $15/mo over 2.3M+ remixable community games. This guide lists both free allowances, credit costs, and commercial / export rights so you pick the right tool at zero cost."

CONTENT_ZH = """<h1>BinkBink（虎牙）vs Rosebud AI：AI 做游戏工具免费额度对比（2026）</h1>

<p>「一句话做出一个能玩的游戏」是 2026 年 AI 工具里很新的一档赛道。<a href="https://ai-bot.cn/the-latest-ai-projects/">ai-bot.cn 最新 AI 项目榜</a>刚挂了虎牙的 <strong>BinkBink</strong>（安卓 App），而网页端的 <strong>Rosebud AI</strong> 已经攒下 230 万+ 社区游戏。两家都能「输入一句话 → 几分钟得到一个完整可玩的休闲游戏」，但<strong>免费额度怎么给、门槛在哪、能商用到什么程度</strong>差别不小。下面把两家的 0 元起步条件、免费池、积分消耗和付费入门价全部摊开（数字为 2026-10-09 抓取自 Play Store、官网 rosebud.ai/pricing 与 ai-bot.cn 条目）。</p>

<h2>两家免费额度速览</h2>

<table>
<tr><th>项目</th><th>BinkBink（虎牙，安卓 App）</th><th>Rosebud AI（网页端）</th></tr>
<tr><td>定位</td><td>一句话生成完整可玩休闲游戏（移动端）</td><td>一句话生成 2D/3D 浏览器游戏（Web 平台）</td></tr>
<tr><td>访问方式</td><td>Google Play 下载，<strong>进入无需注册登录</strong></td><td>rosebud.ai 浏览器直接用，可游客模式</td></tr>
<tr><td>免费池</td><td>免费创作，<strong>无公开积分/次数门槛</strong>（截至 2026-10 未公布额度页）</td><td>Newbie 免费版 <strong>每周 8,000 积分</strong>，免绑卡、可用地区每周刷新</td></tr>
<tr><td>生成内容</td><td>美术素材 + 玩法规则 + 关卡 + 音效一次生成</td><td>代码 + 美术 + 音效（基于 Phaser / Three.js），支持 3D</td></tr>
<tr><td>迭代机制</td><td>Remix：文字提修改意见 → 实时生成新版本</td><td>Rosie 对话式修改（默认模型约 <strong>2,000 积分/回合</strong>，premium 模型约 <strong>20,000/回合</strong>）</td></tr>
<tr><td>游戏品类</td><td>消除、塔防、跑酷、经营、互动小说、沙盒</td><td>2D 街机/平台跳跃为主，3D 能力较初级</td></tr>
<tr><td>分享/即玩</td><td>一键生成链接，好友<strong>免安装、免注册</strong>直接玩</td><td>一键发布公开 URL，浏览器直接玩，<strong>2.3M+ 社区游戏可 Remix</strong></td></tr>
<tr><td>内容生态</td><td>内置发现页、关注创作者（初期 <strong>1,000+ 下载</strong>）</td><td>2.3M+ 社区游戏，生态成熟</td></tr>
<tr><td>付费入门</td><td>暂未公布付费档</td><td>Indie Dev <strong>$15/月</strong>（10 万积分）；10x Dev $30/月（30 万）；Pro $50/月（100 万，含代码导出 + Windows/Steam）</td></tr>
<tr><td>商用权限</td><td>未明确公示</td><td>10x Dev 及以上含<strong>完整商用授权</strong>，Rosebud 不收分成</td></tr>
</table>

<h2>BinkBink（虎牙）：免登录直接用，分享即玩</h2>

<p>BinkBink 是虎牙推出的 AI 游戏互动 App，定位「AI 做游戏工具」。核心卖点是<strong>零门槛</strong>：不写代码、不需要美术和开发团队，一句自然语言（比如「做一个猫咪主题的消除游戏」）几分钟内生成一个完整可玩、包含美术素材、玩法规则、关卡机制和配套音效的成品休闲游戏。它的迭代机制叫 <strong>Remix</strong>——对已生成的游戏直接用文字提修改意见，AI 实时调整出新版本，打破「生成即结束」的单向模式。品类覆盖三消解谜、塔防生存、跑酷闯关、模拟经营、分支剧情互动小说和沙盒创意。社交侧最省事：<strong>一键生成分享链接，好友无需安装、无需注册即可在浏览器直接游玩</strong>，应用内还有发现页可滑动浏览其他创作者的游戏并关注。截至 2026-10 初期，Play Store 显示 <strong>1,000+ 下载</strong>，处于早期积累阶段。<strong>免费侧</strong>：进入后无需注册登录即可在首页开始创作，目前未公布公开的积分/次数门槛——属于「下载即用」型白嫖。适合：想在手机上随手把脑洞变成可玩小游戏、做社交裂变（生成后发群里免安装即玩）的普通用户，以及独立创作者低成本验证玩法原型。</p>

<h2>Rosebud AI：每周 8,000 积分免费池，230 万+ 游戏可 Remix</h2>

<p>Rosebud AI 是网页端的 AI 做游戏平台（rosebud.ai），输入一句话或选模板即可生成 2D/3D 浏览器游戏，底层基于 Phaser / Three.js，AI 助手叫 <strong>Rosie</strong>。它生态最成熟：<strong>2.3M+ 社区游戏</strong>可以直接 Remix（在别人作品上二次创作）。<strong>免费侧</strong>：Newbie（免费版）<strong>每周给 8,000 积分、无需信用卡</strong>，在可用地区每周自动刷新，可以创建、游玩、Remix、分享游戏。积分怎么花（官方给的粗略口径，编辑器会显示每回合实际用量）：用默认模型 Rosie 改游戏约 <strong>2,000 积分/回合</strong>；换 premium 模型约 <strong>20,000/回合</strong>；生成一张图或一段精灵动画约 <strong>200–2,000</strong>；生成一个音效约 <strong>1,000</strong>；3D 模型、360° 天空盒也各消耗积分。也就是说<strong>8,000 积分大概够 3–4 次 premium 模型大改，或几十次默认模型小改 + 若干资产生成</strong>。付费档（Stripe 定价）：<strong>Indie Dev $15/月（10 万积分）</strong>、10x Dev $30/月（30 万）、<strong>Pro $50/月（100 万，官方称「性价比最高」，含代码下载 + Windows/Steam 导出）</strong>、Scale/Enterprise $100/月（200 万）。关键权益：Pro 及以上能下载项目代码、导出 Windows 包发 Steam；Indie Dev 及以上项目可设为私密、关闭被 Remix；<strong>10x Dev 及以上含完整商用授权</strong>——可以卖游戏、卖素材、在任何平台发布，Rosebud 不收分成；10x Dev 及以上还去 Rosebud 品牌托管。付费档还有每日刷新积分（太平洋时间零点重置、优先消耗）和月积分一次结转。推荐机制：订阅用户每成功拉一个新订阅，双方各得 $10（最多 5 个）。适合：想在浏览器做完整 2D/3D 游戏、需要 Remix 生态、最终要<strong>导出代码 / 发 Steam / 商用变现</strong>的创作者。</p>

<h2>怎么选（0 元起步）</h2>

<ul>
<li><strong>在手机上玩、想一键分享免安装即玩</strong>：选 <strong>BinkBink</strong>——安卓 App、免登录、免注册免安装分享、免费创作无公开积分门槛，最轻量。</li>
<li><strong>要正式做游戏、需要代码导出 / 发 Steam / 商用变现</strong>：选 <strong>Rosebud AI</strong>——免费版每周 8,000 积分够用入门，Pro $50/月起解锁代码下载 + Windows/Steam 导出，10x Dev 起含完整商用授权、平台 0 抽成。</li>
<li><strong>想站在 230 万+ 现成游戏上二次创作</strong>：只有 <strong>Rosebud</strong> 有成熟 Remix 生态，BinkBink 目前以自建 + 分享为主。</li>
</ul>

<p>一个通用提醒：BinkBink 处于早期（1,000+ 下载、未公布付费与积分体系），额度政策随时可能加门槛；Rosebud 免费池「每周 8,000 积分」依赖可用地区且刷新不结转。两家都建议<strong>先 0 元跑通核心链路、记下当前额度，再决定是否升级</strong>。</p>

<h2>常见问题</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q：哪家免费额度更大方？</div>
<div class="faq-a">看维度。Rosebud 白纸黑字给「免费版每周 8,000 积分、免绑卡、可用地区每周刷新」，规则清楚可预期；BinkBink 免费创作且免登录，但目前没公布公开积分/次数门槛（早期阶段，1,000+ 下载）。要长期、稳定、可预期的免费池选 Rosebud；要手机上零门槛、随玩随分享选 BinkBink。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q：Rosebud 的 8,000 免费积分到底能干多少事？</div>
<div class="faq-a">按官方粗略口径：默认模型 Rosie 一次编辑约 2,000 积分，premium 模型约 20,000/回合；生成一张图/精灵动画约 200–2,000，生成一个音效约 1,000。8,000 积分≈3–4 次 premium 大改，或几十次默认小改 + 若干资产生成，够把一个小游戏从零做到能玩。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q：做出来的游戏能赚钱/商用吗？</div>
<div class="faq-a">Rosebud 可以：10x Dev（$30/月）及以上含完整商用授权，可卖游戏、卖素材、在任何平台发布，Rosebud 不收分成；Pro 起还能下载代码、导出 Windows 包发 Steam。BinkBink 目前未明确公示商用条款，商用前以官方最新协议为准。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q：BinkBink 一定要注册/登录吗？</div>
<div class="faq-a">不用。进 App 后无需注册登录即可在首页开始创作、滑动试玩别人做的游戏；生成后一键分享链接，好友免安装免注册直接玩。账号功能（关注、社区互动）才需要登录。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q：电脑配置要求高吗？</div>
<div class="faq-a">都不高。Rosebud 是网页平台，浏览器打开即可，生成在云端跑；BinkBink 是安卓 App，手机直接玩，分享出去的游戏也是浏览器即玩，不占本地算力。</div>
</div>
</div>

<h2>结论</h2>

<p>2026 年「AI 做游戏」这条新赛道的白嫖格局很清楚：<strong>BinkBink（虎牙）主打手机零门槛 + 免安装免注册分享</strong>，免费创作、未公布积分门槛，适合随手玩、社交裂变；<strong>Rosebud AI 主打网页端 + 成熟 Remix 生态（2.3M+ 游戏）</strong>，免费版每周 8,000 积分（免绑卡、每周刷新），付费 $15/月起、Pro $50/月解锁代码导出 + Steam 发布、10x Dev 起含完整商用授权且平台 0 抽成。想 0 元试水就两家都开：手机上用 BinkBink 快速验证脑洞，网页上用 Rosebud 做能导出、能商用的完整游戏。</p>
"""

CONTENT_EN = """<h1>BinkBink (Huya) vs Rosebud AI: Free-Tier Comparison of 2 AI Game-Maker Tools (2026)</h1>

<p>"One line to a playable game" is a fresh lane in 2026 AI tools. The <a href="https://ai-bot.cn/the-latest-ai-projects/">ai-bot.cn latest-AI-projects list</a> just added Huya's <strong>BinkBink</strong> (an Android app), while the web-based <strong>Rosebud AI</strong> has already accumulated 2.3M+ community games. Both can "type a sentence and get a complete playable casual game in minutes," but <strong>how the free tier is granted, where the barrier is, and how far you can go commercially</strong> differ a lot. Below is a full breakdown of each one's zero-cost start, free pool, credit costs, and entry price (numbers pulled 2026-10-09 from the Play Store, rosebud.ai/pricing, and the ai-bot.cn entries).</p>

<h2>Free tiers at a glance</h2>

<table>
<tr><th>Item</th><th>BinkBink (Huya, Android app)</th><th>Rosebud AI (web)</th></tr>
<tr><td>Positioning</td><td>One line to a full playable casual game (mobile)</td><td>One line to a 2D/3D browser game (web platform)</td></tr>
<tr><td>Access</td><td>Google Play; <strong>no login required to start</strong></td><td>rosebud.ai in browser; guest mode available</td></tr>
<tr><td>Free pool</td><td>Free creation, <strong>no published credit/limit gate</strong> (as of 2026-10)</td><td>Newbie free: <strong>8,000 credits/week</strong>, no card, weekly refill in eligible regions</td></tr>
<tr><td>What it generates</td><td>Art + game rules + levels + audio in one pass</td><td>Code + art + audio (Phaser / Three.js), 3D supported</td></tr>
<tr><td>Iteration</td><td>Remix: text feedback -&gt; real-time new version</td><td>Rosie chat edits (~<strong>2,000 credits/turn</strong> default model, ~<strong>20,000</strong> premium model)</td></tr>
<tr><td>Game genres</td><td>Match-3, tower defense, runner, sim, interactive fiction, sandbox</td><td>2D arcade / platformer focus; 3D still early</td></tr>
<tr><td>Share / instant play</td><td>One-click link; friends play <strong>install-free, register-free</strong></td><td>One-click public URL; <strong>2.3M+ community games to remix</strong></td></tr>
<tr><td>Content ecosystem</td><td>Built-in discovery feed, follow creators (early, <strong>1,000+ downloads</strong>)</td><td>2.3M+ community games, mature ecosystem</td></tr>
<tr><td>Entry price</td><td>No paid tier published yet</td><td>Indie Dev <strong>$15/mo</strong> (100k credits); 10x Dev $30/mo (300k); Pro $50/mo (1M, code export + Windows/Steam)</td></tr>
<tr><td>Commercial rights</td><td>Not explicitly published</td><td>Full commercial rights on 10x Dev and above; Rosebud takes no commission</td></tr>
</table>

<h2>BinkBink (Huya): no login, share and play instantly</h2>

<p>BinkBink is Huya's AI game-interaction app, positioned as an "AI game-making tool." Its core is <strong>zero barrier</strong>: no code, no art skills, no dev team. One natural-language line (e.g. "make a cat-themed match-3 game") yields a complete playable casual game in minutes, with auto-generated art, game rules, levels, and sound. Its iteration mechanic is called <strong>Remix</strong> - text feedback on a generated game produces a new version in real time, breaking the "generate-once" one-way model. Genres cover match-3 puzzles, tower defense, runners, simulation, branching interactive fiction, and sandbox. Socially it is the easiest: <strong>one click generates a share link; friends play in the browser with no install and no account</strong>, and the app has a discovery feed to browse and follow other creators' games. As of 2026-10 it is early-stage with <strong>1,000+ downloads</strong> on the Play Store. <strong>Free side</strong>: you start creating from the home screen with no registration or login, and there is currently no published credit / usage cap - it is a "download and use" kind of freebie. Best for everyday users who want to turn a random idea into a playable game on their phone and share it (post to a chat, friends play install-free), plus indie creators cheaply validating a game prototype.</p>

<h2>Rosebud AI: 8,000 free credits a week, 2.3M+ games to remix</h2>

<p>Rosebud AI is a web AI game-making platform (rosebud.ai): type a sentence or pick a template and it generates a 2D/3D browser game, built on Phaser / Three.js, with an AI assistant called <strong>Rosie</strong>. It has the most mature ecosystem: <strong>2.3M+ community games</strong> can be remixed (build on someone else's work). <strong>Free side</strong>: the Newbie (free) plan gives <strong>8,000 credits per week with no credit card</strong>; in eligible regions they auto-refill weekly, and you can create, play, remix, and share games. How credits spend (the official rough figures; the editor shows the actual cost of each turn): an edit turn with the default Rosie model is about <strong>2,000 credits</strong>; a premium-model turn is about <strong>20,000</strong>; generating an image or sprite animation is <strong>200-2,000</strong>; generating a sound is about <strong>1,000</strong>; 3D models and 360-degree skyboxes also draw credits. That means <strong>8,000 credits is roughly 3-4 premium-model big edits, or dozens of default-model small edits plus several asset generations</strong>. Paid tiers (Stripe prices): <strong>Indie Dev $15/mo (100,000 credits)</strong>, 10x Dev $30/mo (300,000), <strong>Pro $50/mo (1,000,000, marketed as "best value," including code download + Windows/Steam export)</strong>, and Scale/Enterprise $100/mo (2,000,000). Key entitlements: Pro and above can download project code and export a Windows build for Steam; Indie Dev and above can make projects private and disable remixing; <strong>10x Dev and above include full commercial rights</strong> - sell games and assets, publish anywhere, and Rosebud takes no commission; 10x Dev and above also remove Rosebud branding on hosted games. Paid plans also get daily-refresh credits (reset at midnight Pacific, consumed first) and one-time monthly credit rollover. Referrals: an active subscriber gets $10 off per friend who subscribes, and earns $10 back, up to 5 friends. Best for creators who want full 2D/3D games in the browser, the Remix ecosystem, and the ability to <strong>export code / ship to Steam / monetize commercially</strong>.</p>

<h2>Which to pick (starting at zero cost)</h2>

<ul>
<li><strong>On your phone, want one-click install-free / register-free sharing</strong>: pick <strong>BinkBink</strong> - Android app, no login, no published credit gate, the lightest entry.</li>
<li><strong>Building a real game that needs code export / Steam release / commercial monetization</strong>: pick <strong>Rosebud AI</strong> - the free 8,000 credits/week is enough to start; Pro from $50/mo unlocks code download + Windows/Steam export, and 10x Dev adds full commercial rights with 0 platform commission.</li>
<li><strong>Want to build on 2.3M+ existing games</strong>: only <strong>Rosebud</strong> has a mature remix ecosystem; BinkBink is mostly self-build + share for now.</li>
</ul>

<p>One universal reminder: BinkBink is early-stage (1,000+ downloads, no published paid or credit system), so its limits may get gated at any time; Rosebud's free "8,000 credits/week" depends on eligible regions and does not stack. For both, <strong>run through the core flow at zero cost first, note the current allowance, then decide whether to upgrade</strong>.</p>

<h2>Frequently asked questions</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: Which has the more generous free tier?</div>
<div class="faq-a">Depends on the axis. Rosebud spells it out: "free plan, 8,000 credits/week, no credit card, weekly refill in eligible regions" - clear and predictable. BinkBink is free to create and needs no login, but has no published credit/usage cap (early stage, 1,000+ downloads). For a stable, predictable free pool choose Rosebud; for a zero-barrier phone experience with instant sharing choose BinkBink.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: What can Rosebud's 8,000 free credits actually do?</div>
<div class="faq-a">By the official rough numbers: a default-Rosie edit turn is ~2,000 credits and a premium-model turn is ~20,000; an image / sprite animation is 200-2,000; a sound is ~1,000. So 8,000 credits is about 3-4 premium-model big edits, or dozens of default-model small edits plus a few asset generations - enough to take a small game from scratch to playable.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Can I sell / commercially use the games I make?</div>
<div class="faq-a">On Rosebud, yes: 10x Dev ($30/mo) and above include full commercial rights - sell games and assets and publish on any platform, and Rosebud takes no commission; Pro and above also let you download the code and export a Windows build for Steam. BinkBink has not explicitly published commercial terms yet, so check its latest agreement before commercial use.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Does BinkBink require an account to use?</div>
<div class="faq-a">No. You can start creating from the home screen with no registration or login and swipe through others' games to play; a generated game shares as a link your friends open install-free and register-free. An account is only needed for account features like following creators and community interaction.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Do I need a powerful computer?</div>
<div class="faq-a">No. Rosebud is a web platform - open it in a browser and generation runs in the cloud. BinkBink is an Android app played on your phone, and its shared games run in a browser too, so no local compute is required.</div>
</div>
</div>

<h2>Bottom line</h2>

<p>The 2026 "free window" in this new lane is clear: <strong>BinkBink (Huya) is about zero-barrier mobile plus install-free / register-free sharing</strong> - free creation with no published credit cap; and <strong>Rosebud AI is about the web plus a mature 2.3M+ remix ecosystem</strong>, with a free 8,000 credits/week (no card, weekly refill), paid from $15/mo, Pro $50/mo for code export + Steam release, and full commercial rights from 10x Dev with 0 platform commission. To try it at zero cost, open both: use BinkBink on the phone to quickly sanity-check an idea, and use Rosebud in the browser to build a complete, exportable, monetizable game.</p>
"""

FAQ_ZH = [
 {"question":"哪家免费额度更大方？","answer":"看维度。Rosebud 白纸黑字给「免费版每周 8,000 积分、免绑卡、可用地区每周刷新」，规则清楚可预期；BinkBink 免费创作且免登录，但没公布公开积分/次数门槛（早期，1000+ 下载）。要长期稳定免费池选 Rosebud；要手机零门槛随玩随分享选 BinkBink。"},
 {"question":"Rosebud 的 8,000 免费积分能干多少事？","answer":"默认模型 Rosie 一次编辑约 2,000 积分、premium 约 20,000/回合；生成图/精灵动画 200–2,000、音效约 1,000。8,000 积分≈3–4 次 premium 大改，或几十次默认小改 + 若干资产生成，够把小游戏从零做到能玩。"},
 {"question":"做出来的游戏能商用吗？","answer":"Rosebud 可以：10x Dev（$30/月）及以上含完整商用授权，可卖游戏/素材、任意平台发布，Rosebud 不收分成；Pro 起能下载代码、导出 Windows 包发 Steam。BinkBink 未明确公示商用条款，以官方最新协议为准。"},
 {"question":"BinkBink 一定要注册登录吗？","answer":"不用。进入 App 后无需注册登录即可在首页创作、试玩别人的游戏；生成后一键分享链接，好友免安装免注册直接玩。账号功能（关注、社区互动）才需要登录。"},
 {"question":"需要很强的电脑配置吗？","answer":"都不需要。Rosebud 是网页平台，浏览器打开即可，生成在云端跑；BinkBink 是安卓 App，手机直接玩，分享出去的游戏也是浏览器即玩，不占本地算力。"},
]
FAQ_EN = [
 {"question":"Which has the more generous free tier?","answer":"Depends on the axis. Rosebud spells it out: free plan, 8,000 credits/week, no credit card, weekly refill in eligible regions. BinkBink is free to create and needs no login, but has no published credit/usage cap (early stage, 1,000+ downloads). For a stable free pool choose Rosebud; for a zero-barrier phone experience choose BinkBink."},
 {"question":"What can Rosebud's 8,000 free credits do?","answer":"Default Rosie edit turn ~2,000 credits, premium model ~20,000/turn; an image / sprite animation is 200-2,000; a sound is ~1,000. So 8,000 credits is about 3-4 premium big edits, or dozens of default small edits plus asset generation - enough to take a small game from scratch to playable."},
 {"question":"Can I sell or commercially use the games I make?","answer":"On Rosebud, yes: 10x Dev ($30/mo) and above include full commercial rights - sell games and assets, publish anywhere, Rosebud takes no commission; Pro and above also give code download and a Windows export for Steam. BinkBink has not published commercial terms yet, so check its latest agreement."},
 {"question":"Does BinkBink require an account?","answer":"No. You can create from the home screen with no registration or login and play others' games; a generated game shares as a link your friends open install-free and register-free. An account is only needed for following creators and community features."},
 {"question":"Do I need a powerful computer?","answer":"No. Rosebud is a web platform - open it in a browser and generation runs in the cloud. BinkBink is an Android app played on your phone, and its shared games run in a browser too, so no local compute is required."},
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
    "category": "general",
    "date_published": TODAY,
    "tags": ["BinkBink", "虎牙", "Huya", "Rosebud AI", "Rosebud", "AI做游戏", "游戏制作", "AI Game Maker", "免费额度", "积分", "对比", "Remix", "Steam", "休闲游戏", "免费"],
    "icon": "🎮",
    "excerpt_zh": "虎牙 BinkBink（安卓 App，免登录、免安装免注册分享、初期 1000+ 下载）vs Rosebud AI（网页端，免费版每周 8,000 积分免绑卡、2.3M+ 社区游戏可 Remix、付费 $15/月起、Pro $50/月含代码导出 + Steam、10x Dev 起商用 0 抽成）——0 元起步选哪款。",
    "excerpt_en": "Huya's BinkBink (Android app, no login, install-free / register-free sharing, 1,000+ initial downloads) vs Rosebud AI (web, free 8,000 credits/week no card, 2.3M+ remixable games, paid from $15/mo, Pro $50/mo code export + Steam, 10x Dev full commercial rights with 0 commission) - which zero-cost start wins.",
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
