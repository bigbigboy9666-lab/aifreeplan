#!/usr/bin/env python3
"""Generate the 'NVIDIA Nemotron 3 Free on OpenRouter (2026)' guide.
Data sources (verified 2026-10-04):
- OpenRouter API (openrouter.ai/api/v1/models), live :free variants $0/$0, no expiration_date:
  - nvidia/nemotron-3-ultra-550b-a55b:free      ctx=1,000,000
  - nvidia/nemotron-3-super-120b-a12b:free       ctx=262,144
  - nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free  ctx=256,000 (in: text/audio/image/video, out: text)
  - nvidia/nemotron-3.5-lightning:free           ctx=1,000,000
  - nvidia/nemotron-3.5-content-safety:free      ctx=128,000
  All prompt=$0 completion=$0; created 2026-03 to 2026-08.
- OpenRouter docs (api_reference/limits.md): free-model rate limits constants
  FREE_MODEL_RATE_LIMIT_RPM=20, FREE_MODEL_NO_CREDITS_RPD=50, FREE_MODEL_HAS_CREDITS_RPD=1000,
  FREE_MODEL_CREDITS_THRESHOLD=10 → <10 credits purchased: 50 free req/day; >=10 credits: 1000 free req/day; 20 req/min.
- HuggingFace model cards:
  - nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16: 550B total / 55B active, LatentMoE
    (Mamba-2 + MoE + Attention hybrid + Multi-Token Prediction), ~20T token pretrain, NVFP4 recipe,
    1M context, reasoning on/off flag, multilingual (EN/FR/ES/IT/DE/JA/HI/KO/PT-BR/ZH), pretrain ~20T tokens.
  - nvidia/Nemotron-3-Super-120B-A12B-FP8: 120B total / 12B active (Super tier).
  - nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16: 31B total / ~3B active,
    Mamba2-Transformer hybrid MoE, 256k context, multimodal in = Video/Audio/Image/Text, out = Text,
    best for video+speech analysis, OCR/document intelligence, GUI/agentic workflows, ASR.
- Same OpenRouter free pool as context: google/gemma-4-26b-a4b-it:free, google/gemma-4-31b-it:free
  (262k ctx), qwen/qwen3.8-27b:free (multimodal in), cohere/north-mini-code:free (256k),
  dots-studio/dots-3-note-preview:free (512k, exp 2026-12-31).
- Openrouter.ai/stealth space-bunny-alpha:free had expiration_date=2026-10-05 (lapsed 2026-10-04/05).
"""
import os, sys, json
from datetime import datetime

sys.path.insert(0, '/home/ubuntu/aifreeplan/scripts')
from write_guide import generate_guide_html

SLUG = "nvidia-nemotron-3-free-openrouter-2026"
TODAY = "2026-10-04"

TITLE_ZH = "NVIDIA Nemotron 3 免费攻略：OpenRouter上$0调用，550B旗舰+30B多模态，最高100万上下文"
TITLE_EN = "NVIDIA Nemotron 3 Free Guide: Call $0 on OpenRouter, 550B Flagship + 30B Multimodal, up to 1M Context"

DESC_ZH = "NVIDIA Nemotron 3 家族的多档变体已在 OpenRouter 的 :free 免费池上线：Ultra 550B（55B激活）、Super 120B、Nano Omni 30B（文本/音频/图像/视频多模态）、3.5 Lightning，输入输出全 $0，最高 100 万 Token 上下文，无到期日。本文给精确免费额度、OpenRouter 免费限速（50/1000 次每天）、Nemotron 3 架构与规格、和 5 种用法。"
DESC_EN = "NVIDIA's Nemotron 3 family has landed in OpenRouter's :free pool: Ultra 550B (55B active), Super 120B, Nano Omni 30B (text/audio/image/video multimodal), 3.5 Lightning, all $0 in / $0 out with up to 1M-token context and no expiration. This guide covers the exact free allowance, OpenRouter's free rate limits (50/1000 req/day), Nemotron 3 architecture and specs, and five ways to use it."

CONTENT_ZH = """<h1>NVIDIA Nemotron 3 免费攻略：OpenRouter上$0调用，550B旗舰+30B多模态，最高100万上下文</h1>

<p>NVIDIA 的 <strong>Nemotron 3</strong> 模型家族，刚刚在 <strong>OpenRouter</strong> 的 <code>:free</code> 免费池里上线——这不是一个玩具小模型，而是 550B 参数级别的旗舰。关键数字（2026-10-04 实测 OpenRouter API）：<strong>输入 $0 / 输出 $0</strong>，最高 <strong>100 万（1,000,000）Token 上下文</strong>，且这批 <code>:free</code> 变体目前<strong>没有到期日</strong>（expiration 为空），跟 10 月 5 日就下架的 Space Bunny 不一样。家族分了四档：<strong>Ultra 550B（55B 激活）</strong>是旗舰推理/智能体档、<strong>Super 120B（12B 激活）</strong>是均衡档、<strong>Nano Omni 30B（约 3B 激活）</strong>是<strong>唯一多模态</strong>档（能直接吃视频/音频/图像/文本）、<strong>3.5 Lightning</strong> 也是 100 万上下文的快速档。先给结论：想要 0 元体验 NVIDIA 最新的 Mamba-2 + MoE 混合架构、还能跑百万级长上下文的人，OpenRouter 的 Nemotron 3 免费池是目前最实的一个入口；但要注意 OpenRouter 免费档的<strong>每天请求次数硬上限</strong>（没充过值的账号只有 <strong>50 次/天</strong>），别把"免费"当成"无限量"。下面是全部实测数字、用法和避坑点。</p>

<h2>免费额度与规格速览</h2>

<table>
<tr><th>OpenRouter 变体</th><th>总参数 / 激活</th><th>上下文</th><th>输入模态</th><th>是否多模态</th></tr>
<tr><td><code>nvidia/nemotron-3-ultra-550b-a55b:free</code></td><td>550B / 55B</td><td><strong>1,000,000</strong></td><td>text</td><td>否</td></tr>
<tr><td><code>nvidia/nemotron-3-super-120b-a12b:free</code></td><td>120B / 12B</td><td>262,144</td><td>text</td><td>否</td></tr>
<tr><td><code>nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free</code></td><td>31B / ~3B</td><td>256,000</td><td>text+audio+image+video</td><td><strong>是</strong></td></tr>
<tr><td><code>nvidia/nemotron-3.5-lightning:free</code></td><td>快速档</td><td><strong>1,000,000</strong></td><td>text</td><td>否</td></tr>
<tr><td><code>nvidia/nemotron-3.5-content-safety:free</code></td><td>安全档</td><td>128,000</td><td>text+image</td><td>是</td></tr>
</table>

<p>五个变体全部 <strong>输入 $0 / 输出 $0</strong>，目前都<strong>没有到期日</strong>。同期还在免费池里的其他免费模型（同一张卡上能挑着混用）：<code>google/gemma-4-26b-a4b-it:free</code> 和 <code>google/gemma-4-31b-it:free</code>（262K 上下文、图像/文本/视频输入）、<code>qwen/qwen3.8-27b:free</code>（图像/文本/视频输入）、<code>cohere/north-mini-code:free</code>（256K，主打编程）、<code>dots-studio/dots-3-note-preview:free</code>（512K，带图像，<strong>到期 2026-12-31</strong>）。</p>

<h2>OpenRouter 免费限速：真正的门槛在这</h2>

<p>"$0" 不等于"无限量"。OpenRouter 对 <code>:free</code> 变体按你<strong>累计充值额度</strong>分两档限速（2026-10-04 文档口径）：</p>

<table>
<tr><th>你的账号状态</th><th>免费模型请求上限</th></tr>
<tr><td>累计充值 <strong>&lt; 10 美元</strong>（新白嫖账号）</td><td><strong>50 次/天</strong> + 20 次/分钟</td></tr>
<tr><td>累计充值 <strong>≥ 10 美元</strong></td><td><strong>1000 次/天</strong> + 20 次/分钟</td></tr>
</table>

<ul>
<li>上限指<strong>免费模型</strong>的请求数，不是付费模型；分钟级限速 20 req/min 对所有免费请求都生效；</li>
<li>想实时看额度：调 <code>GET /api/v1/key</code>，看 <code>free_model_daily_requests</code> 字段里的当日计数与上限；</li>
<li>白嫖账号（没充过值）每天 50 次，重度跑 Ultra 550B 长上下文会很快触顶——<strong>多注册账号没用</strong>，OpenRouter 明确说全局按账号/密钥统一管容量；</li>
<li>撞 429 时按指数退避重试，遵守 <code>Retry-After</code> 头。</li>
</ul>

<h2>怎么 0 元用上（从建 Key 到调模型）</h2>

<ol>
<li>去 <a href="https://openrouter.ai/">openrouter.ai</a> 注册，在 Keys 页建一个 API Key（免费，不绑卡也能用）；</li>
<li>在请求里把模型 ID 写成带 <code>:free</code> 后缀的形式，例如 <code>nvidia/nemotron-3-ultra-550b-a55b:free</code>；</li>
<li>最小示例（OpenAI 兼容协议，Python）：<br><code>curl https://openrouter.ai/api/v1/chat/completions -H "Authorization: Bearer 你的KEY" -d '{"model":"nvidia/nemotron-3-ultra-550b-a55b:free","messages":[{"role":"user","content":"..."}]}'</code></li>
<li>长上下文场景：把整份代码库 / 论文 / 日志丢进 100 万 Token 窗口，让 Ultra 做跨文件分析；</li>
<li>多模态场景：把 <strong>视频 + 音频 + 图像 + 文本</strong> 一起发给 Nano Omni 30B，直接出转写 / 文档理解 / GUI 分析；</li>
<li>额度紧的时候，把同一任务在 <code>nemotron-3-super-120b</code>、<code>gemma-4-31b</code>、<code>nemotron-3.5-lightning</code> 之间切换做 fallback，省掉旗舰档的 50 次/天配额。</li>
</ol>

<h2>Nemotron 3 架构：为什么敢白送 550B</h2>

<ul>
<li><strong>LatentMoE</strong>：Mamba-2 与 MoE 层交错 + 选择性 Attention 的混合架构，外加 <strong>Multi-Token Prediction（MTP）</strong>层，用共享权重做投机解码，推理更快；</li>
<li><strong>NVFP4 预训练配方</strong>：权重/激活/梯度大部分用 NVFP4 量化感知训练，省算力；</li>
<li>Ultra 550B 预训练约 <strong>20T token</strong>，走 <strong>Multi-Domain On-Policy Distillation（MOPD）</strong> 把强教师模型蒸馏到自己 rollout 上，提升代码 / 数学 / 工具调用 / 智能体表现；</li>
<li>Nano Omni 30B 是 <strong>Mamba2-Transformer 混合 MoE</strong>，多模态统一视频 / 音频 / 图像 / 文本理解，主打企业级问答、转写、OCR、文档智能、GUI 智能体。</li>
</ul>

<h2>5 种 0 元玩法（按场景挑）</h2>

<ol>
<li><strong>百万级长文档 / 代码库分析</strong>：Ultra 550B 的 1,000,000 Token 窗口 + 可开关的推理档，适合跨文件 RAG、整仓代码审查；</li>
<li><strong>多模态内容理解</strong>：Nano Omni 30B 直接吃视频 / 音频 / 图像 / 文本，做会议记录转写、密集字幕、GUI 分析；</li>
<li><strong>快速长上下文迭代</strong>：3.5 Lightning 同样是 1M 上下文，但更偏快速，适合 agent 里多轮自驱；</li>
<li><strong>均衡性价比</strong>：Super 120B（12B 激活）在 262K 窗口做日常问答与指令跟随，烧配额更少；</li>
<li><strong>内容安全前置</strong>：content-safety 变体（128K，文本+图像）做输入过滤 / 风险判断。</li>
</ol>

<h2>和其他免费入口对比</h2>

<table>
<tr><th>入口</th><th>免费额度</th><th>Nemotron 3 位置</th></tr>
<tr><td>OpenRouter <code>:free</code></td><td>输入/输出 $0，50~1000 次/天（看充值）+ 20 次/分</td><td><strong>主力</strong>，5 档全有，最高 1M 上下文</td></tr>
<tr><td>HuggingFace（模型卡）</td><td>开源权重，自部署 0 元推理（吃你自己的算力）</td><td>想要 1M 长上下文 / 多模态但不想受 50 次/天限制时自托管</td></tr>
<tr><td>Space Bunny（已下架）</td><td>曾 $0/$0，1M 上下文，<strong>到期 2026-10-05</strong></td><td>同类"匿名 / 限时"档，Nemotron 是更稳的长期替代</td></tr>
</table>

<p>（各口径来自 OpenRouter 模型 API、官方文档与 NVIDIA HuggingFace 模型卡；额度 / 到期日以 OpenRouter 产品内实时展示为准。）</p>

<h2>常见问题</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: Nemotron 3 在 OpenRouter 上免费吗？要充值吗？</div>
<div class="faq-a">带 <code>:free</code> 后缀的变体输入 / 输出全 $0，不强制充值。但免费模型请求按累计充值分档限速：&lt;10 美元账号 50 次/天，≥10 美元账号 1000 次/天，分钟级 20 次/分。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 这几档怎么选？</div>
<div class="faq-a">跑 1M 长上下文、复杂智能体 / 推理选 Ultra 550B；要省配额的日常问答选 Super 120B；需要视频 / 音频 / 图像 / 文本多模态选 Nano Omni 30B；追求快选 3.5 Lightning。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 上下文真的 100 万吗？</div>
<div class="faq-a">Ultra 550B 与 3.5 Lightning 的 <code>:free</code> 上下文都是 1,000,000；Super 120B 是 262,144；Nano Omni 30B 是 256,000（以模型卡 256k 为准）。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 会突然下架吗？</div>
<div class="faq-a">目前这几个 <code>:free</code> 变体都没有到期日。同类里 Space Bunny 10 月 5 日已下架，说明 OpenRouter 免费池是动态的——建议把 Nemotron 3 当主力、同时把 Gemma 4 / Qwen3.8 / cohere 当 fallback。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 额度不够能多注册账号绕过吗？</div>
<div class="faq-a">不能。OpenRouter 明确说多开账号 / Key 不改变限速，容量全局统一管；撞 429 应指数退避 + 遵守 Retry-After，或切更轻的变体。</div>
</div>
</div>

<h2>总结</h2>

<p>Nemotron 3 的免费策略数字很清楚：<strong>OpenRouter 上 5 档全 $0（Ultra 550B / Super 120B / Nano Omni 30B 多模态 / 3.5 Lightning / content-safety），最高 1M 上下文，目前无到期日</strong>；真正的约束是<strong>免费请求限速</strong>（&lt;10 美元充值 50 次/天、≥10 美元 1000 次/天、20 次/分）。想做 0 元 1M 长上下文或 0 元多模态，这是目前最稳的入口；想要无上限自托管，就上 NVIDIA 的开源权重。额度与到期日都在变，动手前以 OpenRouter 产品内实时展示为准。</p>
"""

CONTENT_EN = """<h1>NVIDIA Nemotron 3 Free Guide: Call $0 on OpenRouter, 550B Flagship + 30B Multimodal, up to 1M Context</h1>

<p>NVIDIA's <strong>Nemotron 3</strong> model family has just landed in <strong>OpenRouter</strong>'s <code>:free</code> pool, and this is not a toy model, it is a flagship 550B-parameter one. The key numbers (verified 2026-10-04 against the live OpenRouter API): <strong>$0 input / $0 output</strong>, up to <strong>1,000,000-token context</strong>, and these <code>:free</code> variants currently have <strong>no expiration date</strong> (expiration is empty), unlike Space Bunny, which went down on 10/05. The family spans four tiers: <strong>Ultra 550B (55B active)</strong> is the flagship reasoning/agent tier, <strong>Super 120B (12B active)</strong> is the balanced tier, <strong>Nano Omni 30B (~3B active)</strong> is the <strong>only multimodal</strong> tier (ingests video/audio/image/text directly), and <strong>3.5 Lightning</strong> is a fast 1M-context tier. Bottom line up front: if you want a $0 way to run NVIDIA's newest Mamba-2 + MoE hybrid architecture with million-scale long context, OpenRouter's Nemotron 3 free pool is the most concrete entry right now, but mind OpenRouter's <strong>hard daily request cap for free tiers</strong> (a never-topped-up account gets only <strong>50 requests/day</strong>); do not mistake "free" for "unlimited". Below are all the measured numbers, usage, and the gotchas.</p>

<h2>Free Allowance &amp; Specs at a Glance</h2>

<table>
<tr><th>OpenRouter variant</th><th>Total / active params</th><th>Context</th><th>Input modality</th><th>Multimodal</th></tr>
<tr><td><code>nvidia/nemotron-3-ultra-550b-a55b:free</code></td><td>550B / 55B</td><td><strong>1,000,000</strong></td><td>text</td><td>No</td></tr>
<tr><td><code>nvidia/nemotron-3-super-120b-a12b:free</code></td><td>120B / 12B</td><td>262,144</td><td>text</td><td>No</td></tr>
<tr><td><code>nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free</code></td><td>31B / ~3B</td><td>256,000</td><td>text+audio+image+video</td><td><strong>Yes</strong></td></tr>
<tr><td><code>nvidia/nemotron-3.5-lightning:free</code></td><td>Fast tier</td><td><strong>1,000,000</strong></td><td>text</td><td>No</td></tr>
<tr><td><code>nvidia/nemotron-3.5-content-safety:free</code></td><td>Safety tier</td><td>128,000</td><td>text+image</td><td>Yes</td></tr>
</table>

<p>All five variants are <strong>$0 in / $0 out</strong> and currently have <strong>no expiration</strong>. Other free models sharing the same free pool you can mix across: <code>google/gemma-4-26b-a4b-it:free</code> and <code>google/gemma-4-31b-it:free</code> (262K context, image/text/video input), <code>qwen/qwen3.8-27b:free</code> (image/text/video input), <code>cohere/north-mini-code:free</code> (256K, coding-focused), and <code>dots-studio/dots-3-note-preview:free</code> (512K, image in, <strong>expires 2026-12-31</strong>).</p>

<h2>OpenRouter Free Rate Limits: The Real Barrier</h2>

<p>"$0" does not mean "unlimited". OpenRouter gates <code>:free</code> variants by your <strong>all-time top-up credits</strong> in two tiers (2026-10-04 docs):</p>

<table>
<tr><th>Your account state</th><th>Free-model request ceiling</th></tr>
<tr><td>All-time top-up <strong>&lt; $10</strong> (fresh free account)</td><td><strong>50 requests/day</strong> + 20/min</td></tr>
<tr><td>All-time top-up <strong>≥ $10</strong></td><td><strong>1,000 requests/day</strong> + 20/min</td></tr>
</table>

<ul>
<li>The ceiling applies to <strong>free-model</strong> requests, not paid ones; the 20 req/min cap applies to all free requests;</li>
<li>To see your live allowance, call <code>GET /api/v1/key</code> and read the <code>free_model_daily_requests</code> counter and ceiling;</li>
<li>A never-topped-up account gets 50/day; heavy Ultra 550B long-context use will hit that fast, and <strong>extra accounts do not help</strong>, OpenRouter governs capacity globally per account/key;</li>
<li>On a 429, back off exponentially and honor the <code>Retry-After</code> header.</li>
</ul>

<h2>How to Use It at $0 (From Key to Call)</h2>

<ol>
<li>Register at <a href="https://openrouter.ai/">openrouter.ai</a> and create an API key (free, no card required);</li>
<li>Write the model id with the <code>:free</code> suffix, e.g. <code>nvidia/nemotron-3-ultra-550b-a55b:free</code>;</li>
<li>Minimal call (OpenAI-compatible, Python): <code>curl https://openrouter.ai/api/v1/chat/completions -H "Authorization: Bearer YOUR_KEY" -d '{"model":"nvidia/nemotron-3-ultra-550b-a55b:free","messages":[{"role":"user","content":"..."}]}'</code></li>
<li>For long context: drop an entire codebase / paper / log into the 1M-token window and let Ultra do cross-file analysis;</li>
<li>For multimodal: send <strong>video + audio + image + text</strong> to Nano Omni 30B and get transcription / document intelligence / GUI analysis back;</li>
<li>When you are tight on quota, switch the same job across <code>nemotron-3-super-120b</code>, <code>gemma-4-31b</code>, and <code>nemotron-3.5-lightning</code> as fallbacks to preserve the flagship tier's 50/day.</li>
</ol>

<h2>Nemotron 3 Architecture: Why 550B Is Given Away</h2>

<ul>
<li><strong>LatentMoE</strong>: interleaved Mamba-2 and MoE layers plus selective Attention, with <strong>Multi-Token Prediction (MTP)</strong> heads doing shared-weight speculative decoding for faster inference;</li>
<li><strong>NVFP4 pre-training recipe</strong>: weights/activations/gradients mostly in NVFP4 quantization-aware training to cut compute;</li>
<li>Ultra 550B was pre-trained on roughly <strong>20T tokens</strong> and refined via <strong>Multi-Domain On-Policy Distillation (MOPD)</strong>, distilling strong teachers onto its own rollouts to lift code / math / tool-use / agentic behavior;</li>
<li>Nano Omni 30B is a <strong>Mamba2-Transformer hybrid MoE</strong> that unifies video/audio/image/text understanding for enterprise Q&amp;A, transcription, OCR, document intelligence, and GUI agents.</li>
</ul>

<h2>Five $0 Use Cases (Pick by Scenario)</h2>

<ol>
<li><strong>Million-token document / codebase analysis</strong>: Ultra 550B's 1M window + switchable reasoning for cross-file RAG and whole-repo review;</li>
<li><strong>Multimodal content understanding</strong>: Nano Omni 30B eats video/audio/image/text for meeting transcription, dense captions, GUI analysis;</li>
<li><strong>Fast long-context iteration</strong>: 3.5 Lightning shares the 1M context but is lighter, good for multi-turn agents;</li>
<li><strong>Balanced value</strong>: Super 120B (12B active) at 262K for everyday Q&amp;A and instruction following, uses less quota;</li>
<li><strong>Safety pre-check</strong>: the content-safety variant (128K, text+image) for input filtering and risk assessment.</li>
</ol>

<h2>Free-Entry Comparison</h2>

<table>
<tr><th>Entry</th><th>Free allowance</th><th>Where Nemotron 3 fits</th></tr>
<tr><td>OpenRouter <code>:free</code></td><td>$0 in / $0 out, 50~1000 req/day (depends on top-up) + 20/min</td><td><strong>Primary</strong>: all five tiers, up to 1M context</td></tr>
<tr><td>HuggingFace (model cards)</td><td>Open weights, $0 inference if you self-host (use your own compute)</td><td>When you need 1M context / multimodal without the 50/day cap, self-host</td></tr>
<tr><td>Space Bunny (retired)</td><td>Was $0/$0, 1M context, <strong>expired 2026-10-05</strong></td><td>The same "anonymous/limited-time" slot, Nemotron 3 is a more stable long-term stand-in</td></tr>
</table>

<p>(All figures from the OpenRouter models API, its docs, and NVIDIA HuggingFace model cards; allowances and expiration dates follow OpenRouter's live in-app display.)</p>

<h2>FAQ</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: Is Nemotron 3 free on OpenRouter? Do I need to pay?</div>
<div class="faq-a">The <code>:free</code> variants are $0 in / $0 out and do not force a top-up. But free-model requests are tiered by all-time credits: accounts under $10 get 50 requests/day, $10+ accounts get 1,000/day, and there is a 20/min cap.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Which tier should I pick?</div>
<div class="faq-a">For 1M long context and complex agents/reasoning use Ultra 550B; for quota-saving everyday Q&amp;A use Super 120B; for video/audio/image/text multimodal use Nano Omni 30B; for speed use 3.5 Lightning.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Is the context really 1M?</div>
<div class="faq-a">Ultra 550B and 3.5 Lightning both expose 1,000,000 tokens on their <code>:free</code> variants; Super 120B is 262,144; Nano Omni 30B is 256,000 (per its model card).</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Will it vanish suddenly?</div>
<div class="faq-a">These <code>:free</code> variants have no expiration today. The free pool is dynamic, though, Space Bunny retired on 10/05, so keep Nemotron 3 as the primary and Gemma 4 / Qwen3.8 / cohere as fallbacks.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Can I dodge the cap by making more accounts?</div>
<div class="faq-a">No. OpenRouter states extra accounts/keys do not change rate limits; capacity is governed globally. On a 429, back off exponentially, honor Retry-After, or switch to a lighter variant.</div>
</div>
</div>

<h2>Bottom Line</h2>

<p>Nemotron 3's free policy is refreshingly numeric: <strong>five OpenRouter tiers all $0 (Ultra 550B / Super 120B / Nano Omni 30B multimodal / 3.5 Lightning / content-safety), up to 1M context, no expiration today</strong>; the real constraint is the <strong>free request ceiling</strong> (under $10 top-up: 50/day; $10+: 1000/day; 20/min). If you want a $0 1M-context or $0 multimodal run, this is the most stable entry; for unlimited self-hosting, use NVIDIA's open weights. Allowances and expiration dates are in flux, verify in OpenRouter's app before committing.</p>
"""

FAQ_ZH = [
 {"question":"Nemotron 3 在 OpenRouter 上免费吗？要充值吗？","answer":"带 :free 后缀的变体输入/输出全 $0，不强制充值。但免费模型请求按累计充值分档限速：<10 美元账号 50 次/天，≥10 美元账号 1000 次/天，分钟级 20 次/分。"},
 {"question":"这几档怎么选？","answer":"跑 1M 长上下文、复杂智能体/推理选 Ultra 550B；要省配额的日常问答选 Super 120B；需要视频/音频/图像/文本多模态选 Nano Omni 30B；追求快选 3.5 Lightning。"},
 {"question":"上下文真的 100 万吗？","answer":"Ultra 550B 与 3.5 Lightning 的 :free 上下文都是 1,000,000；Super 120B 是 262,144；Nano Omni 30B 是 256,000（以模型卡 256k 为准）。"},
 {"question":"会突然下架吗？","answer":"目前这几个 :free 变体都没有到期日。同类里 Space Bunny 10 月 5 日已下架，说明 OpenRouter 免费池是动态的——建议把 Nemotron 3 当主力、同时把 Gemma 4 / Qwen3.8 / cohere 当 fallback。"},
 {"question":"额度不够能多注册账号绕过吗？","answer":"不能。OpenRouter 明确说多开账号/Key 不改变限速，容量全局统一管；撞 429 应指数退避 + 遵守 Retry-After，或切更轻的变体。"},
]
FAQ_EN = [
 {"question":"Is Nemotron 3 free on OpenRouter? Do I need to pay?","answer":"The :free variants are $0 in / $0 out and do not force a top-up. But free-model requests are tiered by all-time credits: under $10 accounts get 50 requests/day, $10+ accounts get 1,000/day, and there is a 20/min cap."},
 {"question":"Which tier should I pick?","answer":"For 1M long context and complex agents/reasoning use Ultra 550B; for quota-saving everyday Q&A use Super 120B; for video/audio/image/text multimodal use Nano Omni 30B; for speed use 3.5 Lightning."},
 {"question":"Is the context really 1M?","answer":"Ultra 550B and 3.5 Lightning both expose 1,000,000 tokens on their :free variants; Super 120B is 262,144; Nano Omni 30B is 256,000 (per its model card)."},
 {"question":"Will it vanish suddenly?","answer":"These :free variants have no expiration today. The free pool is dynamic, Space Bunny retired on 10/05, so keep Nemotron 3 as the primary and Gemma 4 / Qwen3.8 / cohere as fallbacks."},
 {"question":"Can I dodge the cap by making more accounts?","answer":"No. OpenRouter states extra accounts/keys do not change rate limits; capacity is governed globally. On a 429, back off exponentially, honor Retry-After, or switch to a lighter variant."},
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
    "tags": ["NVIDIA", "Nemotron 3", "Nemotron 3 Ultra 550B", "Nemotron 3 Nano Omni", "OpenRouter", "免费API", "1M上下文", "多模态", "Mamba-2 MoE", "免费池"],
    "icon": "⚡",
    "excerpt_zh": "NVIDIA Nemotron 3 家族 5 档变体上 OpenRouter :free 免费池：Ultra 550B(55B激活)/Super 120B/Nano Omni 30B(视频/音频/图像/文本多模态)/3.5 Lightning/content-safety，输入输出全 $0，最高 100 万 Token 上下文、目前无到期日。免费限速：充值<10美元50次/天、≥10美元1000次/天、20次/分。",
    "excerpt_en": "NVIDIA Nemotron 3 family lands in OpenRouter's :free pool: Ultra 550B (55B active), Super 120B, Nano Omni 30B (video/audio/image/text multimodal), 3.5 Lightning, content-safety. All $0 in / $0 out, up to 1M-token context, no expiration yet. Free rate limits: < $10 top-up = 50 req/day, $10+ = 1000 req/day, 20/min.",
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
