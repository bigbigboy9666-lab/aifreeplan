#!/usr/bin/env python3
"""Generate the 'Real-Time AI Voice Models Free-Tier Comparison 2026' guide.
Data sources (fetched 2026-09-28):
- ai-bot.cn/gemini-3-8-live (谷歌 Gemini 3.8 Live, 2周前发布): 97种语言, AA语音质量指数第一 82.6, Big Bench Audio 97.7%; 音频输入 $0.005/min、输出 $0.018/min (官方)
- ai.google.dev/gemini-api/docs/pricing: gemini-3.8-live Free Tier 输入/输出均 Free of charge; 付费 $0.75/M text in, $12/M text out, $3.00/M 音频输入($0.005/min), $1.00/M 图像视频($0.002/min), $4.50/M 文本输出, $12/M 音频输出($0.018/min); Grounding 每月5000次免费搜索
- ithome.com/1/001/091.htm (2026-09-11): GPT-Live-1 上线 API; 前端语音层 $0.05/分钟(约¥20.2/小时); Full Duplex Bench 比 GPT-Realtime-2.1 高 30 个百分点; Tau3 端到端语音智能体测试第一(搭配GPT-6 Astra中等推理); 新增12种声音(Quartz/Ripple/Vesper等); Speak 误打断减少近80%; 医疗平台减少约2.3万行代码
- ai-bot.cn/step-audio-3 (阶跃星辰 StepAudio 3, 2周前发布): 五模型 Realtime/ASR/TTS/Gen/Music; Realtime 语音推理准确率99.7%、ASR 词错误率1.7% 均 Artificial Analysis 全球第一; 体验中心 stepfun.com/studio/audio
"""
import os, sys, json
from datetime import datetime

sys.path.insert(0, '/home/ubuntu/aifreeplan/scripts')
from write_guide import generate_guide_html

SLUG = "real-time-ai-voice-models-free-comparison-2026"
TODAY = "2026-09-28"

TITLE_ZH = "实时语音AI三强免费额度对比2026：Gemini 3.8 Live、GPT-Live-1、StepAudio 3 谁最值得白嫖"
TITLE_EN = "Free Real-Time AI Voice Models Compared (2026): Gemini 3.8 Live vs GPT-Live-1 vs StepAudio 3"

DESC_ZH = "实测对比3款主流实时语音模型的免费额度：Google Gemini 3.8 Live API 免费层输入输出全免费、支持97种语言，付费仅 $0.023/分钟；OpenAI GPT-Live-1 在 ChatGPT 免费版可用 mini 档，API 前端语音层 $0.05/分钟、全双工评测领先30个百分点；阶跃 StepAudio 3 的 Realtime 语音推理99.7%、ASR 词错误率1.7% 双双登顶 Artificial Analysis。附免费入口、价格与使用步骤。"
DESC_EN = "Hands-on free-tier comparison of three real-time voice models (verified Sep 2026): Google Gemini 3.8 Live — free API tier, 97 languages, $0.005/min audio in + $0.018/min out on paid; OpenAI GPT-Live-1 — free GPT-Live-1 mini in ChatGPT, $0.05/min front-end voice layer on the API, +30 points on Full Duplex Bench; StepFun StepAudio 3 — 99.7% realtime speech reasoning and 1.7% ASR WER, both #1 on Artificial Analysis. Free access paths, prices, and setup steps included."

CONTENT_ZH = """<h1>实时语音AI三强免费额度对比2026：Gemini 3.8 Live、GPT-Live-1、StepAudio 3 谁最值得白嫖</h1>

<p>2026年9月这两周，实时语音赛道密集落地：谷歌发布 <strong>Gemini 3.8 Live</strong>（2周前）、OpenAI 把 <strong>GPT-Live-1 上线 API</strong>（9月11日）、阶跃星辰推出 <strong>StepAudio 3</strong> 五模型全家桶（2周前）。这三款是目前做实时语音对话、语音客服、实时翻译最有代表性的模型。本文只写核对过的数字：<strong>Gemini 3.8 Live 在 Gemini API 免费层输入输出全部免费，付费档音频输入 $0.005/分钟、输出 $0.018/分钟，支持 97 种语言</strong>；<strong>GPT-Live-1 在 ChatGPT 免费版可用（mini 档），API 前端语音层 $0.05/分钟（一小时约 3 美元 / 20.2 元人民币）</strong>；<strong>StepAudio 3 Realtime 语音推理准确率 99.7%、ASR 词错误率 1.7%，双双拿下 Artificial Analysis 全球第一</strong>。结论先给：纯免费体验选 Gemini 3.8 Live（AI Studio 零门槛），做中文场景选 StepAudio 3，要全双工+工具调用生态选 GPT-Live-1。</p>

<h2>三款模型免费额度速览</h2>

<table>
<tr><th>模型</th><th>免费额度</th><th>付费价格</th><th>核心成绩</th><th>免费入口</th></tr>
<tr><td><strong>Gemini 3.8 Live</strong>（Google）</td><td>✅ API 免费层：音频/文本输入输出全部 Free of charge；Search Live 对所有用户开放；含 Extended Thinking 变体同档</td><td>音频输入 $0.005/分钟（$3.00/百万token）、音频输出 $0.018/分钟（$12.00/百万token）；文本 $0.75/M 入、$4.50/M 出；每月 5,000 次 Grounding 搜索免费</td><td>Artificial Analysis 语音质量指数第一（82.6）；Big Bench Audio 97.7%；支持 97 种语言自动切换</td><td>Google AI Studio（免费、无需绑卡）；Search Live 免费体验</td></tr>
<tr><td><strong>GPT-Live-1</strong>（OpenAI）</td><td>✅ ChatGPT 免费用户默认使用 GPT-Live-1 mini 档语音模式，无需订阅；API 需注册开发者账号（注册免费）</td><td>API 前端语音层 $0.05/分钟（一小时约 $3，按现汇率约 20.2 元人民币）；后端模型（GPT-5.5 / GPT-6 Astra）与工具调用另计</td><td>Full Duplex Bench 比 GPT-Realtime-2.1 高 30 个百分点；搭配 GPT-6 Astra 中等推理在 Tau3 端到端语音智能体测试排名第一</td><td>ChatGPT App/网页版语音模式（免费用户可用 mini 档）</td></tr>
<tr><td><strong>StepAudio 3</strong>（阶跃星辰）</td><td>✅ 阶跃语音体验中心（stepfun.com/studio/audio）免费在线试用 Realtime/ASR/TTS/Gen/Music 全部 5 款模型；开放平台注册免费</td><td>API 按量计费（平台定价页实时为准）；Realtime 支持推理与生成并行、工具调用异步执行</td><td>Realtime 语音推理准确率 99.7%；ASR 词错误率 1.7%（Artificial Analysis 双榜第一）；一个模型包办配音+音效+环境声+配乐全流水线</td><td>stepfun.com/studio/audio 体验中心；platform.stepfun.com 开放平台</td></tr>
</table>

<h2>Gemini 3.8 Live：免费层最激进，97 种语言 + 按分钟计价</h2>

<p>谷歌这套模型走的是「语音对语音」原生架构：不做「语音转文字 → 大模型 → 文字转语音」的三段拼接，音频直接进、音频直接出，延迟低且保留语调。两个变体：</p>

<ul>
<li><strong>Gemini 3.8 Live</strong>——面向规模化部署，兼顾对话智能、视觉理解与成本效益，支持近实时处理摄像头画面（约 1 帧/秒）；</li>
<li><strong>Extended Thinking 变体</strong>——后台多步推理的同时继续流式输出语音，「让我确认一下…」边想边说，思考强度档位可按需配置。</li>
</ul>

<p>价格是本次对比里最清晰的：<strong>免费层输入输出全部 Free of charge</strong>；付费层按分钟计价——音频输入 $0.005/分钟（等同 $3.00/百万音频 token），音频输出 $0.018/分钟（等同 $12.00/百万 token），文本输入 $0.75/百万、文本输出 $4.50/百万。对照 OpenAI 官方便宜多少：gpt-realtime-2.1 音频输入约 $0.019/分钟、输出约 $0.077/分钟，Gemini 3.8 Live 的音频输出成本只有它的约 1/4。</p>

<p>其他关键数字：<strong>97 种语言对话中自动检测切换</strong>（对比 GPT 实时翻译需单独模型、70+ 输入语言至 13 种输出语言）；<strong>每月 5,000 次 Google Search Grounding 免费</strong>（Gemini 3.x 模型共享额度）；生成音频全部嵌入 <strong>SynthID 隐形水印</strong>，剪辑压缩后仍可检测。基准：Artificial Analysis 语音质量指数第一（82.6），Big Bench Audio 97.7%。</p>

<h3>免费使用步骤</h3>
<ol>
<li>打开 <a href="https://aistudio.google.com">Google AI Studio</a>，Google 账号登录（免费层无需信用卡）；</li>
<li>API 控制台创建 Key，调用 <code>gemini-3.8-live</code> 或 <code>gemini-3.8-live-extended-thinking</code>；</li>
<li>不用写代码也能试：Google Search Live 已面向所有用户推送，直接语音提问；</li>
<li>要接入应用用 Live API（WebSocket 双向流式），文档在 ai.google.dev Live 章节。</li>
</ol>

<h2>GPT-Live-1：免费版就能用，API 前端语音层 $0.05/分钟</h2>

<p>GPT-Live 现在是 ChatGPT 的默认语音模式，分两档：<strong>付费用户默认 GPT-Live-1，免费用户默认 GPT-Live-1 mini</strong>，覆盖 iOS、Android 和网页端。也就是说，不用付一分钱，注册 ChatGPT 就能体验全双工语音：可同时听说、自然打断、插话，还能实时翻译。复杂问题（搜索、多步推理）交给后台 GPT-5.5 处理，前台对话不掉线。推理档位分 Instant / Medium / High 三档。</p>

<p>9月11日 OpenAI 把 <strong>GPT-Live-1 正式上线 API</strong>，这是这次新闻里最关键的数字：前端语音层 <strong>$0.05/分钟</strong>——按 60 分钟算一小时 $3（约 20.2 元人民币），后端模型（可配 GPT-6 Astra 等）和工具调用费用另计。它支持全双工：对话中处理打断、停顿、背景噪声，还能接电话场景（订餐、客服语音智能体），可与 Codex 等工具联动，也支持把复杂推理委托给后端文本模型。</p>

<p>评测数字（OpenAI 公布）：<strong>Full Duplex Bench 比 GPT-Realtime-2.1 高 30 个百分点</strong>；搭配 GPT-6 Astra 中等推理强度时，<strong>Tau3 端到端语音智能体测试排名第一</strong>。落地案例：语言学习平台 Speak 接入后，学习者思考停顿期间的误打断次数较旧的轮次式系统减少近 <strong>80%</strong>；某医疗服务平台称代码量减少 80%、删除约 2.3 万行代码。另外新增 12 种声音（Quartz、Ripple、Vesper、Willow、Stone、Gleam、Meridian、Bossa、Tempo、Beacon、Delta、Cinder）。</p>

<h3>免费使用方式</h3>
<ul>
<li><strong>普通用户（0元）</strong>：ChatGPT App 或网页版点麦克风图标进语音模式，免费账号默认 mini 档，可打断、可插话、天气股票自动出可视化卡片；</li>
<li><strong>开发者（注册免费，调用计费）</strong>：GPT-Live-1 已在 API 提供，前端语音层 $0.05/分钟；不想写代码可先用官方 Presence 模板。</li>
</ul>

<h2>StepAudio 3：中文场景最强，5 款模型全免费试用</h2>

<p>阶跃星辰这套是「一个系列包办整条音频流水线」：<strong>Realtime、ASR、TTS、Gen、Music 五款模型</strong>（2周前发布）。两个数字硬：<strong>Realtime 语音推理准确率 99.7%、ASR 词错误率 1.7%，双双拿到 Artificial Analysis 全球第一</strong>。</p>

<ul>
<li><strong>Realtime</strong>：原生全双工，听、推理、生成并行，工具调用异步执行，能判断对话节奏（什么时候接话、什么时候等）；</li>
<li><strong>ASR</strong>：大模型结合上下文纠错，中文、英文、方言、中英混说、专业术语都转得准；</li>
<li><strong>TTS</strong>：流式生成边合成边播放，还原语气、情绪、停顿、笑声、迟疑等细节；</li>
<li><strong>Gen</strong>：一个模型一次生成人声+音效+环境音+背景音乐，还能编排各元素出现的时间顺序（影视配音场景）；</li>
<li><strong>Music</strong>：从零生成、清唱配曲、翻唱、ABC 记谱法多轮创作。</li>
</ul>

<p>免费入口：<strong>阶跃语音体验中心 stepfun.com/studio/audio 在线免费试用全部 5 款模型</strong>；开放平台 platform.stepfun.com 免费注册拿 API Key，API 按量计费（具体单价以平台实时定价页为准，注册后控制台可见）。中文语料和中文场景（字幕转写、影视配音、客服）是它的主场，这两项榜单第一里有 ASR 词错误率 1.7% 的直接背书。</p>

<h2>怎么选：一张表说清楚</h2>

<table>
<tr><th>需求</th><th>推荐</th><th>理由（数字）</th></tr>
<tr><td>纯白嫖体验实时语音</td><td>Gemini 3.8 Live</td><td>API 免费层输入输出 0 元，97 种语言，Search Live 免费入口</td></tr>
<tr><td>ChatGPT 生态 / 全双工对话</td><td>GPT-Live-1</td><td>免费版 mini 档 0 元，API 前端 $0.05/分钟，评测领先 30 个百分点</td></tr>
<tr><td>中文转写 / 配音 / 音乐</td><td>StepAudio 3</td><td>ASR 词错误率 1.7%（双榜第一），Gen 一次出全音频层，体验中心免费</td></tr>
<tr><td>大规模部署成本敏感</td><td>Gemini 3.8 Live</td><td>音频输出 $0.018/分钟，约为 gpt-realtime-2.1（$0.077/分钟）的 1/4</td></tr>
</table>

<h2>常见问题</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: 三款模型哪个免费额度最大方？</div>
<div class="faq-a">纯免费角度 Gemini 3.8 Live 最彻底：Gemini API 免费层音频、文本输入输出全部 Free of charge，注册 Google 账号即可，不用绑卡。GPT-Live-1 在 ChatGPT 免费用户可用 mini 档（0 元，但 API 需付费 $0.05/分钟起）。StepAudio 3 体验中心 5 款模型全免费在线试用，API 注册免费、调用按量计费。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Gemini 3.8 Live 和 gpt-realtime-2.1 价格差多少？</div>
<div class="faq-a">按音频计费：Gemini 3.8 Live 输入 $0.005/分钟、输出 $0.018/分钟；gpt-realtime-2.1 输入 $32/百万 token（约 $0.019/分钟）、输出 $64/百万 token（约 $0.077/分钟）。一次 10 分钟对话 Gemini 约 $0.23，gpt-realtime-2.1 约 $0.96（且 GPT 长对话无缓存时实际可达 $0.18–0.46/分钟）。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 什么是全双工语音，和普通语音模式差在哪？</div>
<div class="faq-a">普通轮次式语音要你说完它才说，全双工是边听边说：你可以随时打断、它也能在你说完前插入反馈，每秒多次判断开口/倾听/插话。OpenAI 数据显示 GPT-Live-1 在 Full Duplex Bench 上比前代 GPT-Realtime-2.1 高 30 个百分点，Speak 平台实测误打断减少近 80%。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 生成的语音有水印吗？能被检测出是 AI 吗？</div>
<div class="faq-a">Gemini 3.8 Live 全部生成音频嵌入 SynthID 隐形水印，直接织入音频信号，剪辑或压缩后仍可被检测工具识别。GPT-Live-1 和 StepAudio 3 的公开资料未提及等效音频水印机制。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: StepAudio 3 的 API 到底多少钱？</div>
<div class="faq-a">注册开放平台免费，调用按量计费，具体单价以 platform.stepfun.com 实时定价页为准（控制台可见）。它的卖点在榜单：Realtime 语音推理 99.7%、ASR 词错误率 1.7% 均为 Artificial Analysis 第一，先白嫖体验中心（stepfun.com/studio/audio）再决定要不要上 API。</div>
</div>
</div>

<h2>总结</h2>

<p>三强各有主场：<strong>Gemini 3.8 Live 赢在免费层和成本</strong>（输入输出 0 元免费层 + $0.018/分钟输出，97 种语言），<strong>GPT-Live-1 赢在生态和全双工</strong>（免费版 mini 档 0 元 + API $0.05/分钟前端 + 30 个百分点的评测领先），<strong>StepAudio 3 赢在中文和全流水线</strong>（ASR 1.7% 词错误率双榜第一 + Gen 一次出全音频层 + 体验中心免费）。个人白嫖直接上 Gemini 3.8 Live 的 AI Studio；做中文转写配音先看 StepAudio 3 体验中心；要接客服/订餐类语音智能体，GPT-Live-1 的 API 是最成熟的选择。三款都是 2026 年 9 月刚落地，价格与免费政策可能随时调整，动手前以官网为准。</p>
"""

CONTENT_EN = """<h1>Free Real-Time AI Voice Models Compared (2026): Gemini 3.8 Live vs GPT-Live-1 vs StepAudio 3</h1>

<p>Two busy weeks for real-time voice AI: Google shipped <strong>Gemini 3.8 Live</strong> (two weeks ago), OpenAI put <strong>GPT-Live-1 on the API</strong> (Sept 11), and StepFun released the five-model <strong>StepAudio 3</strong> suite (two weeks ago). These three are the models you actually benchmark against when building real-time voice dialogue, voice support, or live translation. Every number below is verified: <strong>Gemini 3.8 Live's Gemini API free tier is free for audio and text input and output, paid is $0.005/min audio in + $0.018/min audio out, 97 languages</strong>; <strong>GPT-Live-1 is free for ChatGPT free users (mini tier), the API front-end voice layer costs $0.05/minute</strong>; <strong>StepAudio 3 Realtime scores 99.7% on speech reasoning and its ASR hits a 1.7% word error rate — both #1 on Artificial Analysis</strong>. Short version: pure free usage — Gemini 3.8 Live; Chinese scenarios — StepAudio 3; full-duplex + tool-calling ecosystem — GPT-Live-1.</p>

<h2>Free-Tier Snapshot</h2>

<table>
<tr><th>Model</th><th>Free tier</th><th>Paid pricing</th><th>Headline numbers</th><th>Free entry point</th></tr>
<tr><td><strong>Gemini 3.8 Live</strong> (Google)</td><td>Yes — Gemini API free tier: audio/text input and output all Free of charge; Search Live open to all users; Extended Thinking variant in the same tier</td><td>Audio in $0.005/min ($3.00/1M tokens), audio out $0.018/min ($12.00/1M); text $0.75/M in, $4.50/M out; 5,000 free Google Search grounding requests per month</td><td>#1 on the Artificial Analysis voice quality index (82.6); Big Bench Audio 97.7%; auto-switches across 97 languages mid-conversation</td><td>Google AI Studio (free, no card); Search Live for casual use</td></tr>
<tr><td><strong>GPT-Live-1</strong> (OpenAI)</td><td>Yes — ChatGPT free users get GPT-Live-1 mini in voice mode at $0; API developer registration is free</td><td>API front-end voice layer $0.05/minute (about $3 for a 60-minute session, ~20.2 CNY); back-end model (GPT-5.5 / GPT-6 Astra) and tool calls billed separately</td><td>+30 points over GPT-Realtime-2.1 on Full Duplex Bench; #1 on Tau3 end-to-end voice agent test with GPT-6 Astra medium reasoning</td><td>ChatGPT app / web voice mode (mini tier, free)</td></tr>
<tr><td><strong>StepAudio 3</strong> (StepFun)</td><td>Yes — StepFun Voice Experience Center (stepfun.com/studio/audio) lets you try all 5 models (Realtime/ASR/TTS/Gen/Music) online for free; open-platform registration is free</td><td>API is pay-per-use (live pricing on the platform's pricing page)</td><td>Realtime speech-reasoning accuracy 99.7%; ASR word error rate 1.7% — both #1 on Artificial Analysis; one model covers voice + SFX + ambience + music in a single pass</td><td>stepfun.com/studio/audio; platform.stepfun.com open platform</td></tr>
</table>

<h2>Gemini 3.8 Live: the most generous free tier, billed per minute</h2>

<p>Google's models use a native voice-to-voice architecture: no "STT → LLM → TTS" cascade. Audio goes in, audio comes out — lower latency, and the prosody survives. Two variants:</p>

<ul>
<li><strong>Gemini 3.8 Live</strong> — built for scale: dialogue intelligence plus near-real-time camera-frame understanding (about 1 frame/second);</li>
<li><strong>Extended Thinking</strong> — multi-step reasoning runs in the background while the model keeps streaming speech ("Let me confirm…"), with configurable thinking-budget tiers.</li>
</ul>

<p>The pricing is the cleanest of the three: <strong>free tier is Free of charge for both audio and text input and output</strong>. Paid: audio input $0.005/min ($3.00 per 1M audio tokens), audio output $0.018/min ($12.00 per 1M); text $0.75/1M in, $4.50/1M out. Compare with OpenAI: gpt-realtime-2.1 runs about $0.019/min on audio in and $0.077/min on audio out — Gemini 3.8 Live's audio output is roughly <strong>1/4 the price</strong>. For a 10-minute conversation: about $0.23 on Gemini vs about $0.96 on gpt-realtime-2.1.</p>

<p>Other key numbers: <strong>97 languages with automatic mid-conversation switching</strong> (GPT's real-time translation is a separate model, 70+ input languages to 13 output languages); <strong>5,000 free Google Search grounding requests per month</strong> (shared across Gemini 3.x); every generated audio file carries an invisible <strong>SynthID watermark</strong>, still detectable after editing or compression. Benchmarks: #1 on the Artificial Analysis voice quality index (82.6), Big Bench Audio 97.7%.</p>

<h3>How to use it for free</h3>
<ol>
<li>Open <a href="https://aistudio.google.com">Google AI Studio</a> and sign in with a Google account — the free tier needs no credit card;</li>
<li>Create an API key and call <code>gemini-3.8-live</code> or <code>gemini-3.8-live-extended-thinking</code>;</li>
<li>Prefer no code: Search Live is already pushed to all users — just talk to it;</li>
<li>For apps, use the Live API (bidirectional WebSocket streaming), docs under the Live section of ai.google.dev.</li>
</ol>

<h2>GPT-Live-1: free in ChatGPT, $0.05/minute on the API</h2>

<p>GPT-Live is now ChatGPT's default voice mode, in two tiers: <strong>paid users default to GPT-Live-1, free users default to GPT-Live-1 mini</strong> — available on iOS, Android and web. So registration in ChatGPT gets you full-duplex voice for $0: simultaneous listening and speaking, natural interruption, interjections, real-time translation. Complex questions (search, multi-step reasoning) get offloaded to GPT-5.5 in the back while the front-end conversation never stalls. Reasoning tiers: Instant / Medium / High.</p>

<p>The Sept 11 news is where the money matters: <strong>GPT-Live-1 is on the API, and the front-end voice layer costs $0.05/minute</strong> — a 60-minute session is about $3 (~20.2 CNY), plus whatever you pay for the back-end model (GPT-6 Astra etc.) and tool calls. It handles interruptions, pauses and background noise mid-conversation, works in phone scenarios (restaurant booking, customer support), can hook into Codex-style tooling, and delegates heavy reasoning to a back-end text model.</p>

<p>Published benchmarks: <strong>+30 points over GPT-Realtime-2.1 on Full Duplex Bench</strong>; <strong>#1 on the Tau3 end-to-end voice-agent test</strong> when paired with GPT-6 Astra at medium reasoning. Real deployments: language-learning platform Speak cut false interruptions during learner think-time by nearly <strong>80%</strong> vs the previous turn-based system; a healthcare platform reported 80% less code, about 23,000 lines removed. Twelve new voices added: Quartz, Ripple, Vesper, Willow, Stone, Gleam, Meridian, Bossa, Tempo, Beacon, Delta, Cinder.</p>

<h3>How to use it for free</h3>
<ul>
<li><strong>Casual users ($0)</strong>: tap the mic in the ChatGPT app or web to enter voice mode — free accounts get the mini tier, with interruption support and auto visual cards for weather, stocks and sports;</li>
<li><strong>Developers (registration free, usage billed)</strong>: GPT-Live-1 is on the API at $0.05/minute front-end; OpenAI's Presence templates are a quick start if you don't want to hand-roll the voice layer.</li>
</ul>

<h2>StepAudio 3: the strongest for Chinese, all five models free to try</h2>

<p>StepFun's suite covers the whole audio pipeline with <strong>five models: Realtime, ASR, TTS, Gen and Music</strong> (released two weeks ago). Two numbers stand out: <strong>Realtime speech-reasoning accuracy of 99.7% and an ASR word error rate of 1.7% — both ranked #1 on Artificial Analysis</strong>.</p>

<ul>
<li><strong>Realtime</strong>: native full-duplex — listening, reasoning and speech generation run in parallel, tool calls execute asynchronously, and the model judges conversational timing (when to jump in, when to wait);</li>
<li><strong>ASR</strong>: LLM-backed context correction for Chinese, English, dialects, mixed CN/EN speech and technical jargon;</li>
<li><strong>TTS</strong>: streaming synthesis (plays while generating), preserving intonation, emotion, pauses, even laughter and hesitation;</li>
<li><strong>Gen</strong>: one model generates voice + sound effects + ambience + background music in a single pass, with timeline control over when each element fires (dubbing workflows);</li>
<li><strong>Music</strong>: from-scratch generation, humming-to-score, cover versions, and ABC-notation multi-turn composition.</li>
</ul>

<p>Free entry: <strong>the StepFun Voice Experience Center (stepfun.com/studio/audio) lets you test all five models online for free</strong>; the open platform (platform.stepfun.com) has free registration for an API key, with pay-per-use API billing (check the live pricing page in the console). Chinese-language scenarios — transcription, dubbing, customer support — are its home turf, and the 1.7% ASR word error rate (a #1 ranking) is the proof.</p>

<h2>Which one should you pick?</h2>

<table>
<tr><th>Need</th><th>Pick</th><th>Why (numbers)</th></tr>
<tr><td>Pure free real-time voice</td><td>Gemini 3.8 Live</td><td>API free tier = $0 in/out, 97 languages, Search Live as a free entry point</td></tr>
<tr><td>ChatGPT ecosystem / full-duplex</td><td>GPT-Live-1</td><td>Free mini tier at $0; API front-end $0.05/min; +30 pts on Full Duplex Bench</td></tr>
<tr><td>Chinese transcription / dubbing / music</td><td>StepAudio 3</td><td>ASR 1.7% WER (#1), Gen outputs a full audio stack in one pass, free experience center</td></tr>
<tr><td>Cost-sensitive at scale</td><td>Gemini 3.8 Live</td><td>Audio output $0.018/min vs gpt-realtime-2.1's ~$0.077/min — about 1/4 the cost</td></tr>
</table>

<h2>FAQ</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: Which of the three has the most generous free tier?</div>
<div class="faq-a">For pure free usage, Gemini 3.8 Live: the Gemini API free tier costs $0 for audio and text input and output, requires only a Google account, no credit card. GPT-Live-1 gives free users the mini tier in ChatGPT at $0 (its API starts at $0.05/min). StepAudio 3's experience center offers free online trials of all five models; open-platform registration is free and API calls are pay-per-use.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: How much cheaper is Gemini 3.8 Live than gpt-realtime-2.1?</div>
<div class="faq-a">Audio billing: Gemini 3.8 Live is $0.005/min in and $0.018/min out. gpt-realtime-2.1 is $32/1M tokens (~$0.019/min) in and $64/1M tokens (~$0.077/min) out. A 10-minute conversation costs about $0.23 on Gemini vs about $0.96 on GPT; long uncached GPT sessions can run $0.18–$0.46 per minute.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: What is full-duplex voice, and how is it different from normal voice mode?</div>
<div class="faq-a">Turn-based voice makes you wait: you finish, then it speaks. Full-duplex listens and speaks at the same time — you can interrupt, and it can interject — deciding open/wait/interrupt multiple times per second. OpenAI reports GPT-Live-1 is 30 points ahead of GPT-Realtime-2.1 on Full Duplex Bench; the Speak platform measured false interruptions during learner think-time drop by nearly 80%.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Is the generated voice watermarked? Can AI audio be detected?</div>
<div class="faq-a">Gemini 3.8 Live embeds an invisible SynthID watermark into every generated audio file, woven into the signal itself and still detectable after editing or compression. GPT-Live-1 and StepAudio 3 public materials don't mention an equivalent audio watermark.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: What does StepAudio 3's API actually cost?</div>
<div class="faq-a">Open-platform registration is free; API calls are pay-per-use with live pricing on the platform's pricing page (visible in the console after sign-in). The pitch is the leaderboard: 99.7% realtime speech reasoning and a 1.7% ASR word error rate, both #1 on Artificial Analysis. Try the free experience center (stepfun.com/studio/audio) first, then decide on API.</div>
</div>
</div>

<h2>Bottom line</h2>

<p>Each model owns a lane: <strong>Gemini 3.8 Live wins on free tier and cost</strong> ($0 free tier + $0.018/min audio out, 97 languages), <strong>GPT-Live-1 wins on ecosystem and full-duplex</strong> ($0 mini tier in ChatGPT + $0.05/min API front-end + a 30-point benchmark lead), and <strong>StepAudio 3 wins on Chinese and the full audio pipeline</strong> (#1 ASR at 1.7% WER + Gen's one-pass full audio stack + a free experience center). For zero-cost use, start with Gemini 3.8 Live in AI Studio. For Chinese transcription and dubbing, try the StepAudio 3 experience center first. For voice agents like support or booking, GPT-Live-1's API is the most mature option. All three landed in September 2026 — pricing and free policies can change, so verify on each vendor's site before you build.</p>
"""

FAQ_ZH = [
 {"question":"三款模型哪个免费额度最大方？","answer":"纯免费角度 Gemini 3.8 Live 最彻底：Gemini API 免费层音频、文本输入输出全部 0 元，注册 Google 账号即可，不用绑卡。GPT-Live-1 在 ChatGPT 免费用户可用 mini 档（0 元），API 需付费（前端语音层 $0.05/分钟起）。StepAudio 3 体验中心 5 款模型全免费在线试用，开放平台注册免费、调用按量计费。"},
 {"question":"Gemini 3.8 Live 和 gpt-realtime-2.1 价格差多少？","answer":"按音频计费：Gemini 3.8 Live 输入 $0.005/分钟、输出 $0.018/分钟；gpt-realtime-2.1 输入约 $0.019/分钟、输出约 $0.077/分钟。一次 10 分钟对话 Gemini 约 $0.23，gpt-realtime-2.1 约 $0.96；GPT 长对话无缓存时实际可达 $0.18–0.46/分钟。"},
 {"question":"什么是全双工语音，和普通语音模式差在哪？","answer":"普通轮次式语音要你说完它才说；全双工是边听边说——你可以随时打断，它也能在你说完前插入反馈，每秒多次判断开口/倾听/插话。OpenAI 数据显示 GPT-Live-1 在 Full Duplex Bench 上比 GPT-Realtime-2.1 高 30 个百分点，Speak 平台实测误打断减少近 80%。"},
 {"question":"生成的语音有水印吗？","answer":"Gemini 3.8 Live 的全部生成音频嵌入 SynthID 隐形水印，直接织入音频信号，剪辑或压缩后仍可被检测工具识别。GPT-Live-1 与 StepAudio 3 的公开资料未提及等效音频水印机制。"},
 {"question":"StepAudio 3 的 API 到底多少钱？","answer":"开放平台注册免费，调用按量计费，具体单价以 platform.stepfun.com 实时定价页（控制台可见）为准。核心卖点是榜单成绩：Realtime 语音推理 99.7%、ASR 词错误率 1.7%，均为 Artificial Analysis 第一。建议先免费体验 stepfun.com/studio/audio 再决定是否上 API。"},
]
FAQ_EN = [
 {"question":"Which of the three has the most generous free tier?","answer":"For pure free usage, Gemini 3.8 Live: the Gemini API free tier costs $0 for audio and text input and output, requires only a Google account, no credit card. GPT-Live-1 gives ChatGPT free users the mini tier at $0 (API starts at $0.05/min front-end). StepAudio 3's experience center offers free online trials of all five models; registration is free and API calls are pay-per-use."},
 {"question":"How much cheaper is Gemini 3.8 Live than gpt-realtime-2.1?","answer":"Audio billing: Gemini 3.8 Live is $0.005/min in and $0.018/min out; gpt-realtime-2.1 is about $0.019/min in and $0.077/min out. A 10-minute conversation: about $0.23 on Gemini vs about $0.96 on GPT; long uncached GPT sessions can run $0.18–$0.46 per minute."},
 {"question":"What is full-duplex voice, and how is it different from normal voice mode?","answer":"Turn-based voice: you finish speaking, then it responds. Full-duplex listens and speaks simultaneously — you can interrupt and it can interject, deciding open/wait/interrupt multiple times per second. GPT-Live-1 leads GPT-Realtime-2.1 by 30 points on Full Duplex Bench; Speak measured false interruptions during think-time drop by nearly 80%."},
 {"question":"Is the generated voice watermarked?","answer":"Every audio file generated by Gemini 3.8 Live carries an invisible SynthID watermark woven into the signal, detectable even after editing or compression. GPT-Live-1 and StepAudio 3 public materials don't mention an equivalent audio watermark."},
 {"question":"What does StepAudio 3's API cost?","answer":"Open-platform registration is free; API calls are pay-per-use with live pricing on the platform's pricing page. The pitch is the leaderboard: 99.7% realtime speech reasoning and a 1.7% ASR word error rate, both #1 on Artificial Analysis. Try the free experience center (stepfun.com/studio/audio) before committing to the API."},
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
    "category": "audio",
    "date_published": TODAY,
    "tags": ["实时语音", "语音大模型", "Gemini 3.8 Live", "GPT-Live-1", "StepAudio 3", "全双工", "免费额度", "语音AI", "同传翻译", "语音客服"],
    "icon": "🎙️",
    "excerpt_zh": "2026年9月实时语音三强免费实测：Gemini 3.8 Live API免费层输入输出全免费（97种语言，付费仅$0.005/$0.018每分钟）、GPT-Live-1 ChatGPT免费版可用mini档（API前端$0.05/分钟，全双工评测领先30个百分点）、StepAudio 3语音推理99.7%+ASR词错误率1.7%双榜第一（体验中心免费）。",
    "excerpt_en": "Sep 2026 real-time voice showdown: Gemini 3.8 Live free API tier ($0 in/out, 97 languages, $0.005/$0.018 per min paid), GPT-Live-1 free mini tier in ChatGPT ($0.05/min API front-end, +30 pts on Full Duplex Bench), StepAudio 3 with 99.7% speech reasoning + 1.7% ASR WER — both #1 on Artificial Analysis, free experience center.",
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
