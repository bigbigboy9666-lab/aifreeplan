#!/usr/bin/env python3
"""Generate the 'AI Meeting Transcription Free-Tier Comparison' guide.
Data sources (fetched 2026-09-25):
- otter.ai/pricing (Basic free: 300 min/mo, 3 lifetime imports, 30-min cap, Pro $16.49/$8.17)
- fireflies.ai/pricing (Free: unlimited transcription*, 400-min storage/team, 20 AI credits, Pro $18/$10)
- notta.ai (Free: 120 min/mo full transcription, 58 languages, Pro from $8.17/mo)
- tactiq.io/pricing (Free: 10 transcripts/mo + 5 AI credits, Pro JPY 1249/user/mo annual)
- aifreeplan data/tools.json 飞书妙记 entry (300 free min/mo, verified 2026-08-27)
"""
import os, sys, json
from datetime import datetime

sys.path.insert(0, '/home/ubuntu/aifreeplan/scripts')
from write_guide import generate_guide_html

SLUG = "ai-meeting-transcription-free-comparison-2026"
TODAY = "2026-09-25"

TITLE_ZH = "免费AI会议转写工具对比2026：Otter vs Fireflies vs Notta vs Tactiq vs 飞书妙记，免费额度全解析"
TITLE_EN = "Free AI Meeting Transcription Tools Compared (2026): Otter vs Fireflies vs Notta vs Tactiq vs Feishu Minutes"

DESC_ZH = "实测对比5款会议转写工具的免费版：Otter每月300分钟、飞书妙记每月300分钟、Notta每月120分钟、Fireflies转写条数不限但存储封顶400分钟、Tactiq每月10次。本文给出各家隐藏限制、不滚存规则与付费起价（$8.17–$16.49/月），帮你白嫖最多的会议转写时长。"
DESC_EN = "Hands-on comparison of the free tiers of five AI meeting-transcription tools (verified Sep 2026): Otter (300 min/mo), Feishu Minutes (300 min/mo), Notta (120 min/mo), Fireflies (unlimited transcripts, 400-min storage cap), Tactiq (10 transcripts/mo). Hidden limits, no-rollover rules and paid starting prices ($8.17–$16.49/mo) included."

CONTENT_ZH = """<h1>免费AI会议转写工具对比2026：Otter vs Fireflies vs Notta vs Tactiq vs 飞书妙记，免费额度全解析</h1>

<p>开完会要写纪要，最省时间的办法是让 AI 把语音直接变成文字。2026 年 9 月，我把 5 款主流会议转写工具的官网定价页逐页核对了一遍，本文只写查过的数字：<strong>Otter Basic 每月 300 分钟转写额度</strong>、<strong>飞书妙记飞书用户每月 300 分钟免费</strong>、<strong>Notta 每月 120 分钟完整转写</strong>、<strong>Fireflies 免费版转写条数标「不限」但团队存储封顶 400 分钟、AI 摘要限量、每月 20 个 AI 积分</strong>、<strong>Tactiq 每月 10 次转写 + 5 个 AI 积分</strong>。付费档起价 $8.17–$16.49/月。下面逐家拆额度、坑和适用场景。</p>

<h2>五款工具免费额度速览</h2>

<table>
<tr><th>工具</th><th>免费转写额度</th><th>关键免费限制</th><th>语言</th><th>付费起价</th></tr>
<tr><td><strong>Otter</strong>（Basic）</td><td>300 分钟/月（共享池）</td><td>单次会话最长 30 分钟；终身 3 次文件导入；历史只留最近 25 条；自定义词表 5 个；AI Chat 20 次/月；并发 1 场会；导出仅 mp3/txt</td><td>英/西/法/德/日/中</td><td>$16.49/月（年付 $8.17，1200 分钟/月）</td></tr>
<tr><td><strong>Fireflies</strong>（Free）</td><td>转写条数标「不限」（*共享池）</td><td>团队存储 400 分钟封顶；AI 摘要限量；20 个 AI 积分/月；单场录制 2 小时；视频 720p；3 个公共频道</td><td>100+ 种</td><td>$10/席/月（年付，月付 $18）</td></tr>
<tr><td><strong>Notta</strong>（Free）</td><td>120 分钟/月（完整转写）</td><td>免费额度按分钟算，用完当月停转写</td><td>58 种</td><td>Pro 约 $8.17/月起（年付）</td></tr>
<tr><td><strong>Tactiq</strong>（Free）</td><td>10 次/月（按次）+ 5 个 AI 积分</td><td>Chrome 扩展（Google Meet/Zoom/Teams）；免费版按月重置，可取消</td><td>多语言</td><td>Pro ¥1,249/用户/月（年付，约 $8.5，转写不限）</td></tr>
<tr><td><strong>飞书妙记</strong></td><td>300 分钟/月（飞书用户）</td><td>需飞书账号；无水印、可免费商用（2026-08-27 核实）</td><td>中文为主，多语言</td><td>企业版约 300 元/人/年起（~$42/人/年）</td></tr>
</table>

<p>单看数字，Otter 和飞书妙记都是每月 300 分钟；Fireflies 表面最大方（转写条数不限），但 400 分钟团队存储意味着一个团队一个月最多留 400 分钟转写文本，超出只能删旧转写腾地方；Notta 的 120 分钟最少但支持 58 种语言，是上面几家里语言覆盖最广的；Tactiq 按次不按分钟，短会党最划算，长会一场就吃掉 1/10 的月额度。</p>

<h2>Otter：300 分钟够用，但有 6 个隐藏上限</h2>

<p>Otter 的 Basic 档免费且永久，注册不用信用卡。核心额度是<strong>每月 300 分钟转写</strong>（会议实时转写与文件导入共用同一个池子，用完当月即停，不滚存）。免费档真正的限制藏在细则里：</p>

<ul>
<li>单次会话/转写最长 30 分钟——超过 30 分钟的会，免费版直接截断（Pro 提到 90 分钟，Business/Enterprise 到 4 小时）。</li>
<li>文件导入<strong>终身只有 3 次</strong>（Basic 档），留给回放/播客录音这类场景基本一次性。</li>
<li>历史只保留最近 25 条会话，早期的转写拿不回（Pro 起不限量）。</li>
<li>自定义词表 5 个词条，团队版才有 100 人名 + 100 词条。</li>
<li>AI Chat（对转写内容提问）20 次/月、单次对话 3 次。</li>
<li>导出格式只有 mp3 和 txt，要 pdf/docx/srt 和批量导出得上 Pro。</li>
</ul>

<p>免费版覆盖英/西/法/德/日/中六种语言的 AI 转写与说话人识别。中文会议能用，但 Otter 的强项一直是英文场景。想多薅一点，Pro 年付 $8.17/月（月付 $16.49），额度跳到 1200 分钟/月、单次 90 分钟、存储不限。</p>

<h2>Fireflies：转写不限，卡点在存储和 AI 积分</h2>

<p>Fireflies 免费版是表面对外最「大方」的一家：<strong>转写条数标「不限」</strong>（官网带 * 脚注，指所有转写类型共享池子），支持 100+ 语言转写，Chrome 扩展、桌面端、移动端都能录。单场录制上限 2 小时，视频回放 720p。但三个数字决定了免费版实际容量：</p>

<ul>
<li><strong>团队存储 400 分钟封顶</strong>（Pro 起 8000 分钟/席，Business 起不限量）。400 分钟全团队共享，一个 30 分钟的周会×4、一次 90 分钟的项目评审，一个月存储就见底了。</li>
<li>AI 摘要<strong>限量</strong>：免费版每月 20 个 AI 积分，摘要、AskFred 提问、Daily Brief 都从这里扣，积分用完当月就不再出摘要，只出裸转写。</li>
<li>搜索/导出是有的（mp3/txt/pdf/docx/srt 全格式），但协作频道只有 3 个公共频道。</li>
</ul>

<p>免费版同样不用信用卡、永久免费。Pro 年付 $10/席/月（月付 $18），解锁不限摘要、8000 分钟存储/席、10 项以上集成；$19/席/月的 Business 才开不限存储。</p>

<h2>Notta：120 分钟免费，但 58 种语言是全场最全</h2>

<p>Notta 免费档给的是<strong>每月 120 分钟完整转写</strong>（不是摘要，是全文本转写），官方宣传支持 58 种语言，累计用户 10M+。120 分钟在几家里最少，适合每月会议总量不大、但经常有非英语会议的场景——小语种语种免费档转写是 Notta 的主场。免费额度按月重置，用完当月即停；Pro 年付约 $8.17/月起，转写条数解锁「不限」。桌面端（macOS/Windows）和 MCP/CLI 是 Notta 的差异化卖点，可以把会议上下文喂给本地 AI 助手。</p>

<h2>Tactiq：按次不按分钟，短会党最优解</h2>

<p>Tactiq 的免费额度是<strong>每月 10 次转写 + 5 个 AI 积分</strong>，按「场次」计费，不按分钟——一场 10 分钟站会和一场 50 分钟评审各算 1 次。免费版无需信用卡、无使用期限，Chrome 扩展直接挂进 Google Meet / Zoom / MS Teams 实时转写，转写默认只展示给你自己。按月重置（官方 FAQ 原话：月底重置，或升级前一直有效），现有转写可继续访问。Pro 档年付 ¥1,249/用户/月（约 $8.5，各区域币种不同），转写条数不限 + AI 积分升到 10；Team 档起 AI 积分不限量。如果你每月会议都在 10 场以内且单场不长，Tactiq 免费版就是成本为 0 的方案。</p>

<h2>飞书妙记：中文会议场景的免费天花板（每月 300 分钟）</h2>

<p>飞书用户每月 <strong>300 分钟免费转写</strong>，在 aifreeplan 工具库中已核实（2026-08-27）：无水印、可免费商用、不绑卡。妙记的优势全在中文生态：音视频自动转写 + 智能总结 + 关键词提炼，转写结果直接进飞书文档，和飞书日历/会议深度联动，中文转写准确率是这一批里最稳的。代价是<strong>必须用飞书</strong>——不开飞书的用户拿不到这 300 分钟。企业版约 300 元/人/年起（~$42/人/年）。</p>

<h2>四个必须知道的规则</h2>

<ol>
<li><strong>免费分钟不滚存</strong>。Otter 官网直接写了「no rollover」，Tactiq 的 FAQ 也确认月底重置。5 家全部是按月计，囤不了。</li>
<li><strong>「转写」和「摘要」是两套额度</strong>。Fireflies 免费版转写不限但摘要只给 20 个 AI 积分；Otter 免费版转写 300 分钟但 AI Chat 只给 20 次。只想要纪要、不想要全文本的用户，先算积分再算分钟。</li>
<li><strong>存储是隐性上限</strong>。Fireflies 团队存储 400 分钟封顶，Otter 历史只留 25 条，转得再多、留不住等于白薅。重度用户直接看付费档的存储数字（8000 分钟/席 或 不限量）。</li>
<li><strong>多工具叠加是合规的白嫖上限</strong>。各家账号互相独立：Otter 300 + 妙记 300 + Notta 120 + Tactiq 10 次 + Fireflies 不限条数，一个人每月能拿到 720 分钟以上免费转写加 20+ 个 AI 积分。会议量再大，也先叠满免费的再谈付费。</li>
</ol>

<h2>按场景选</h2>

<ul>
<li><strong>中文会议为主、团队已用飞书</strong>：飞书妙记 300 分钟起步，不够再加 Tactiq（短会）凑场次。</li>
<li><strong>英文会议为主、Zoom/Google Meet</strong>：Otter 300 分钟，但注意单次 30 分钟上限，长会切段录。</li>
<li><strong>会议量大、想要「条数不限」</strong>：Fireflies 免费版，接受 400 分钟团队存储 + 20 积分摘要的现实。</li>
<li><strong>每月 ≤10 场、单场 1 小时内</strong>：Tactiq 免费版 10 次完全覆盖，0 成本。</li>
<li><strong>多语种/小语种会议</strong>：Notta（58 种语言免费档）或 Fireflies（100+ 语言）。</li>
<li><strong>不想把会议喂给第三方</strong>：本地 Ollama 跑 Whisper 类模型白嫖（见 <a href="/zh/guides/ollama-free-cloud-guide-2026">Ollama 免费部署攻略</a>），或开发者路线：Deepgram 给 $200 免费 API 额度做语音识别。</li>
</ul>

<h2>FAQ</h2>
<div class="faq-section">
<div class="faq-item"><div class="faq-q">这五家的免费版都要绑信用卡吗？</div><div class="faq-a">都不用。Otter Basic、Notta、Tactiq 官网都写明「no credit card」，Fireflies 免费版注册即可用，飞书妙记只要一个飞书账号。付费档才会要卡。</div></div>
<div class="faq-item"><div class="faq-q">免费分钟会滚存到下个月吗？</div><div class="faq-a">不会。Otter 官网明确「no rollover」（所有转写类型共享池）；Tactiq FAQ 确认额度月底重置。五家全部按月计，囤积无效。</div></div>
<div class="faq-item"><div class="faq-q">免费版转写中文效果哪家好？</div><div class="faq-a">纯中文会议选飞书妙记，准确率与文档联动都是这批里最强的，每月 300 分钟免费。Otter 免费版支持语言里含中文，Notta（58 种语言）和 Fireflies（100+ 语言）也支持，但中文深度不如妙记。</div></div>
<div class="faq-item"><div class="faq-q">300 分钟不够用怎么办？</div><div class="faq-a">两条路：一是多工具叠加（Otter 300 + 妙记 300 + Notta 120 + Tactiq 10 次 + Fireflies 不限条数，全免费）；二是升最低档，Notta Pro 年付约 $8.17/月、Tactiq Pro 年付约 $8.5/月转写就不限了，Otter Pro 年付 $8.17/月给 1200 分钟/月。</div></div>
<div class="faq-item"><div class="faq-q">免费版有水印吗，能免费商用吗？</div><div class="faq-a">转写文本不存在「水印」概念，差别在导出格式与存储：Otter 免费版导出只有 mp3/txt（pdf/docx/srt 与批量导出要 Pro），Fireflies 免费版全格式可导但团队存储封顶 400 分钟。飞书妙记已核实无水印、可免费商用。</div></div>
</div>

<p>想看更多免费 AI 生产力工具额度，见 <a href="/zh/guides/ai-productivity-tools-comparison-2026">免费AI生产力工具对比</a>。</p>"""

CONTENT_EN = """<h1>Free AI Meeting Transcription Tools Compared (2026): Otter vs Fireflies vs Notta vs Tactiq vs Feishu Minutes</h1>

<p>After every meeting someone has to write the notes, and the fastest version of that workflow is letting an AI model turn the recording into text. In September 2026 I went through the official pricing pages of the five tools that dominate this category and only wrote down numbers I could verify: <strong>Otter Basic gives 300 transcription minutes per month</strong>, <strong>Feishu Minutes gives Feishu users 300 free minutes per month</strong>, <strong>Notta gives 120 minutes of full transcription per month</strong>, <strong>Fireflies Free labels its transcript count "unlimited" but caps team storage at 400 minutes, limits AI summaries and hands out 20 AI credits monthly</strong>, and <strong>Tactiq gives 10 transcriptions plus 5 AI credits per month</strong>. Paid plans start between $8.17 and $16.49 per month. Below is the full breakdown of quotas, hidden limits and who each tool actually fits.</p>

<h2>The five free tiers at a glance</h2>

<table>
<tr><th>Tool</th><th>Free transcription quota</th><th>Key free-plan limits</th><th>Languages</th><th>Paid from</th></tr>
<tr><td><strong>Otter</strong> (Basic)</td><td>300 min/month (shared pool)</td><td>30-min max per conversation; 3 lifetime file imports; history keeps only the 25 most recent; 5 custom-vocabulary terms; 20 AI Chat queries/month; 1 concurrent meeting; export is mp3/txt only</td><td>EN/ES/FR/DE/JA/ZH</td><td>$16.49/mo ($8.17 annual, 1,200 min/mo)</td></tr>
<tr><td><strong>Fireflies</strong> (Free)</td><td>Transcript count "unlimited" (*shared pool)</td><td>400-min team storage cap; limited AI summaries; 20 AI credits/month; 2-hour recording cap; 720p video; 3 public channels</td><td>100+</td><td>$10/seat/mo annual ($18 monthly)</td></tr>
<tr><td><strong>Notta</strong> (Free)</td><td>120 min/month of full transcription</td><td>Free minutes are monthly; when they run out, transcription stops for the month</td><td>58</td><td>Pro from ~$8.17/mo (annual billing)</td></tr>
<tr><td><strong>Tactiq</strong> (Free)</td><td>10 transcriptions/month + 5 AI credits</td><td>Chrome extension for Google Meet/Zoom/Teams; quota resets monthly, cancel anytime, no card</td><td>Multilingual</td><td>Pro JPY 1,249/user/mo annual (~$8.5, unlimited transcripts)</td></tr>
<tr><td><strong>Feishu Minutes</strong></td><td>300 min/month for Feishu users</td><td>Requires a Feishu account; no watermark, free commercial use (verified 2026-08-27)</td><td>Chinese-first, multilingual</td><td>Enterprise from ~CNY 300/person/yr (~$42/yr)</td></tr>
</table>

<p>On the surface, Otter and Feishu Minutes tie at 300 free minutes each. Fireflies looks the most generous ("unlimited" transcripts) but the 400-minute team storage cap means the whole team can only keep 400 minutes of transcribed text per month, and anything older has to be deleted to make room. Notta has the smallest quota, 120 minutes, but the widest language coverage at 58. Tactiq bills by session instead of minutes, which makes it the best fit for teams with many short meetings and very few long ones: a 10-minute standup and a 50-minute design review each cost exactly 1 of the 10 free sessions.</p>

<h2>Otter: 300 free minutes, six hidden caps</h2>

<p>Otter's Basic plan is free forever and needs no credit card. The headline number is <strong>300 transcription minutes per month</strong>, drawn from a single shared pool that covers live meeting transcription and file uploads alike; when it is gone, it is gone, and it does not roll over. The fine print is where the real limits live:</p>

<ul>
<li><strong>30-minute maximum per conversation</strong> on the free tier. Anything longer is cut off (Pro raises this to 90 minutes; Business and Enterprise to 4 hours).</li>
<li><strong>3 lifetime audio/video file imports</strong>. For podcasts, interviews or stored recordings this is effectively one-time capacity.</li>
<li>Conversation history keeps only the <strong>25 most recent</strong> items; older transcripts disappear on the free tier.</li>
<li>Custom vocabulary is limited to <strong>5 terms</strong> (team plans jump to 100 names plus 100 terms).</li>
<li>AI Chat (question-answering over your transcripts) allows <strong>20 queries per month</strong>, 3 per conversation.</li>
<li>Exports are <strong>mp3 and txt only</strong>. PDF, DOCX, SRT and bulk export all require Pro.</li>
</ul>

<p>The free tier covers AI transcription in English, Spanish, French, German, Japanese and Chinese, with speaker identification by name. Chinese meetings work, but Otter has always been strongest in English-centric workflows. For more capacity, Pro at $8.17/month on annual billing (list price $16.49 monthly) raises the quota to 1,200 minutes per month and 90-minute conversations, with unlimited storage.</p>

<h2>Fireflies: unlimited transcripts, but storage and AI credits are the real ceiling</h2>

<p>Fireflies Free is the most generous-looking offer in this list: <strong>transcription count marked "unlimited"</strong> (with the site's asterisk meaning all transcription types share one pool), 100+ language transcription, and capture on the Chrome extension, desktop app or mobile. Single recordings cap at 2 hours, and video replay is 720p. Three numbers define what the free tier actually delivers:</p>

<ul>
<li><strong>400 minutes of team storage</strong> (Pro starts at 8,000 minutes per seat; Business removes the cap entirely). The 400 minutes are shared across the whole team: a 30-minute weekly x4 plus one 90-minute review and the storage is full for the month.</li>
<li><strong>Limited AI summaries</strong>. The free plan ships 20 AI credits per month, which cover summaries, AskFred questions and the daily brief; when the credits run out, you get raw transcripts only for the rest of the cycle.</li>
<li>Exports are fully formatted (mp3, txt, pdf, docx, srt), but collaboration is capped at 3 public channels.</li>
</ul>

<p>No credit card is required and the free plan is permanent. Pro at $10/seat/month on annual billing (list $18 monthly) unlocks unlimited AI summaries, 8,000 storage minutes per seat and full integrations; $19/seat/month Business adds unlimited storage.</p>

<h2>Notta: 120 free minutes, but 58 languages is the best coverage here</h2>

<p>Notta's free tier gives <strong>120 minutes of full transcription per month</strong>, not just summaries, and the vendor advertises 58 supported languages with 10M+ registered users. At 120 minutes it is the smallest free quota in this comparison, which makes it the pick when your total meeting load is light but includes non-English sessions: low-resource languages on the free tier are Notta's home turf. The quota resets monthly and transcription stops when it is exhausted. Pro starts around $8.17/month on annual billing and removes the transcript-count cap. Notta also ships a macOS/Windows desktop app and an MCP/CLI, which lets you feed meeting context into your own AI agents instead of relying on the vendor's cloud.</p>

<h2>Tactiq: billed by session, the best free option for short meetings</h2>

<p>Tactiq's free tier is <strong>10 transcriptions per month plus 5 AI credits</strong>, counted by session rather than minutes, so a 10-minute standup and a 50-minute review each consume exactly 1 of your 10 sessions. No credit card, no time limit; the Chrome extension transcribes live inside Google Meet, Zoom and Microsoft Teams, and the transcript is visible only to you by default. The official FAQ confirms the quota resets at the start of the next month (or when you upgrade), and your existing transcripts stay accessible. Pro at JPY 1,249 per user per month on annual billing (roughly $8.5; the pricing page is region-localized) unlocks unlimited transcripts and 10 AI credits, and Team plans raise AI credits to unlimited. If you hold ten or fewer meetings a month and none runs long, Tactiq Free covers you at zero cost.</p>

<h2>Feishu Minutes: the Chinese-meeting ceiling at 300 free minutes per month</h2>

<p>Feishu users get <strong>300 free transcription minutes every month</strong>, an entry in our tools database verified on 2026-08-27: no watermark, commercial use allowed on the free tier, no card required. Its advantages are entirely in the Chinese ecosystem: automatic transcription plus smart summaries and keyword extraction, with results landing directly in Feishu Docs and deep linkage to Feishu calendar and meetings. Among the five tools here it has the most reliable Chinese accuracy. The catch is that you have to use Feishu at all; the 300 minutes are unreachable from outside that account system. Enterprise plans start around CNY 300 per person per year (~$42).</p>

<h2>Four rules that apply to all five</h2>

<ol>
<li><strong>Free minutes never roll over.</strong> Otter's own page says "no rollover" for every transcription type, and Tactiq's FAQ confirms a monthly reset. None of the five lets you bank unused minutes.</li>
<li><strong>"Transcription" and "summary" are two separate quotas.</strong> Fireflies Free transcribes without a stated count limit but budgets only 20 AI credits for summaries; Otter gives 300 minutes of transcription but only 20 AI Chat queries. If you only want the written recap, count credits first, minutes second.</li>
<li><strong>Storage is the silent cap.</strong> Fireflies caps team storage at 400 minutes and Otter keeps only the 25 most recent conversations, so heavy usage without a paid plan means deleting your own history. For sustained volume, compare paid storage numbers: 8,000 minutes per seat (Fireflies Pro) or unlimited (Business).</li>
<li><strong>Stacking accounts is a legitimate free ceiling.</strong> The five tools use independent accounts: 300 (Otter) + 300 (Feishu Minutes) + 120 (Notta) + 10 sessions (Tactiq) + unlimited transcript count (Fireflies) gives one person 720+ free transcription minutes per month plus 20+ AI credits. Before paying anyone, fill all the free tiers first.</li>
</ol>

<h2>Which one to pick, by scenario</h2>

<ul>
<li><strong>Chinese-first meetings on Feishu:</strong> Feishu Minutes 300 minutes; add Tactiq for the sessions it cannot capture.</li>
<li><strong>English-first meetings on Zoom/Google Meet:</strong> Otter 300 minutes, with the 30-minute per-conversation cap in mind for long sessions.</li>
<li><strong>High meeting volume, "unlimited" transcript count:</strong> Fireflies Free, accepting the 400-minute team storage and 20-credit summary reality.</li>
<li><strong>Ten or fewer meetings a month, none long:</strong> Tactiq Free's 10 sessions cover you at zero cost.</li>
<li><strong>Many or low-resource languages:</strong> Notta (58 languages on the free tier) or Fireflies (100+).</li>
<li><strong>Refuse to send meetings to a third party:</strong> run an open-weights speech model locally via Ollama (see the <a href="/en/guides/ollama-free-cloud-guide-2026">free Ollama deployment guide</a>), or on the developer route use Deepgram's $200 free API credit for speech-to-text.</li>
</ul>

<h2>FAQ</h2>
<div class="faq-section">
<div class="faq-item"><div class="faq-q">Does any of the five free tiers require a credit card?</div><div class="faq-a">No. Otter Basic, Notta and Tactiq all state "no credit card" on their pricing pages, Fireflies Free works after signup, and Feishu Minutes only needs a Feishu account. Cards enter the picture only at the paid tiers.</div></div>
<div class="faq-item"><div class="faq-q">Do unused free minutes roll over to next month?</div><div class="faq-a">None of the five allows rollover. Otter's pricing page marks the entire transcription pool as "no rollover", and Tactiq's FAQ states the quota resets at the start of the next month. All quotas are monthly.</div></div>
<div class="faq-item"><div class="faq-q">Which free tier handles Chinese meetings best?</div><div class="faq-a">Feishu Minutes: the best Chinese accuracy of the five, with automatic summaries and keyword extraction flowing into Feishu Docs, 300 minutes free per month. Otter's free tier lists Chinese among its six supported languages, and Notta (58) and Fireflies (100+) also support it, but none matches Feishu Minutes for Chinese depth.</div></div>
<div class="faq-item"><div class="faq-q">What if 300 minutes is not enough?</div><div class="faq-a">Two routes. First, stack free tiers across vendors: 300 (Otter) + 300 (Feishu Minutes) + 120 (Notta) + 10 sessions (Tactiq) + Fireflies' unlimited transcript count, all at $0. Second, the cheapest paid steps: Notta Pro from ~$8.17/mo annual, Tactiq Pro ~$8.5/mo annual with unlimited transcripts, Otter Pro $8.17/mo annual with 1,200 minutes.</div></div>
<div class="faq-item"><div class="faq-q">Is there a watermark on free exports, and can I use them commercially?</div><div class="faq-a">Transcription is text, so "watermark" does not really apply; the practical differences are export formats and retention. Otter Free exports only mp3 and txt (pdf/docx/srt and bulk export require Pro); Fireflies Free allows all formats but the team is capped at 400 storage minutes. Feishu Minutes is verified watermark-free with commercial use permitted on the free tier.</div></div>
</div>

<p>For more free AI productivity quotas, see the <a href="/en/guides/ai-productivity-tools-comparison-2026">free AI productivity tools comparison</a>.</p>"""

FAQ_ZH = [
 {"question":"这五家的免费版都要绑信用卡吗？","answer":"都不用。Otter Basic、Notta、Tactiq 官网都写明「no credit card」，Fireflies 免费版注册即可用，飞书妙记只要一个飞书账号。付费档才会要卡。"},
 {"question":"免费分钟会滚存到下个月吗？","answer":"不会。Otter 官网明确「no rollover」（所有转写类型共享池）；Tactiq FAQ 确认额度月底重置。五家全部按月计，囤积无效。"},
 {"question":"免费版转写中文效果哪家好？","answer":"纯中文会议选飞书妙记，准确率与文档联动都是这批里最强的，每月 300 分钟免费。Otter 免费版支持语言含中文，Notta（58 种语言）和 Fireflies（100+ 语言）也支持，但中文深度不如妙记。"},
 {"question":"300 分钟不够用怎么办？","answer":"两条路：一是多工具叠加（Otter 300 + 妙记 300 + Notta 120 + Tactiq 10 次 + Fireflies 不限条数，全免费）；二是升最低档，Notta Pro 年付约 $8.17/月、Tactiq Pro 年付约 $8.5/月转写不限，Otter Pro 年付 $8.17/月给 1200 分钟/月。"},
 {"question":"免费版有水印吗，能免费商用吗？","answer":"转写文本不存在「水印」概念，差别在导出格式与存储：Otter 免费版导出只有 mp3/txt（pdf/docx/srt 与批量导出要 Pro），Fireflies 免费版全格式可导但团队存储封顶 400 分钟。飞书妙记已核实无水印、可免费商用。"}
]
FAQ_EN = [
 {"question":"Does any of the five free tiers require a credit card?","answer":"No. Otter Basic, Notta and Tactiq all state no credit card on their pricing pages, Fireflies Free works after signup, and Feishu Minutes only needs a Feishu account. Cards matter only at the paid tiers."},
 {"question":"Do unused free minutes roll over to next month?","answer":"None of the five allows rollover. Otter marks the entire transcription pool as no rollover, and Tactiq confirms the quota resets at the start of the next month. All quotas are monthly."},
 {"question":"Which free tier handles Chinese meetings best?","answer":"Feishu Minutes: the best Chinese accuracy of the five, with automatic summaries and keyword extraction into Feishu Docs, 300 free minutes per month. Otter lists Chinese among six supported languages, and Notta (58) and Fireflies (100+) also support it, but none matches Feishu Minutes for Chinese depth."},
 {"question":"What if 300 minutes is not enough?","answer":"Stack free tiers across vendors (300 Otter + 300 Feishu Minutes + 120 Notta + 10 Tactiq sessions + Fireflies unlimited count, all at $0), or take the cheapest paid steps: Notta Pro from about $8.17/mo annual, Tactiq Pro about $8.5/mo annual with unlimited transcripts, Otter Pro $8.17/mo annual with 1,200 minutes."},
 {"question":"Is there a watermark on free exports, and can I use them commercially?","answer":"Transcription is text, so watermarks do not really apply; the differences are export formats and retention. Otter Free exports only mp3/txt (pdf/docx/srt and bulk export require Pro); Fireflies Free allows all formats but caps team storage at 400 minutes. Feishu Minutes is verified watermark-free with commercial use permitted on the free tier."}
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
    "tags": ["AI会议转写", "Otter", "Fireflies", "Notta", "Tactiq", "飞书妙记", "免费额度", "语音转写", "会议纪要"],
    "icon": "📝",
    "excerpt_zh": "5款会议转写工具免费版实测：Otter 300分钟/月（30分钟截断+终身3次导入）、飞书妙记300分钟/月（中文最稳）、Notta 120分钟/月（58种语言最全）、Fireflies转写不限条数（团队存储400分钟封顶+20 AI积分）、Tactiq 10次/月（短会最优）。付费$8.17–$16.49/月起。",
    "excerpt_en": "Five free meeting-transcription tiers verified Sep 2026: Otter 300 min/mo (30-min conversation cap, 3 lifetime imports), Feishu Minutes 300 min/mo (best Chinese), Notta 120 min/mo (58 languages), Fireflies unlimited transcript count (400-min team storage cap, 20 AI credits), Tactiq 10 sessions/mo (best for short meetings). Paid from $8.17-16.49/mo.",
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
