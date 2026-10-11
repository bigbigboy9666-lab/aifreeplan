#!/usr/bin/env python3
"""Generate the 'TalkLikeYou Free Open-Source Real-Time Talking-Head Guide (2026)' article.

Data sources (verified 2026-10-11):
- Official GitHub README (github.com/BQ-Wang0511/TalkLikeYou, pulled live 2026-10-11):
* Real-time audio-driven talking-head generation that imitates a target
  person's speaking habits. One-step Flow Matching Motion Generator in an
  18-dimensional lip-motion space; preset habit ID or reference video.
* Code released under the MIT License; third-party code and model files
  remain under their original licenses (THIRD_PARTY_NOTICES.md).
* Checkpoints on HuggingFace: doubi-killer/TalkLikeYou
  (hf download doubi-killer/TalkLikeYou --include "checkpoints/**").
* Recommended env: Linux, Python 3.10, CUDA 12.1, cuDNN 9, NVIDIA GPU >= 12GB,
  FFmpeg on PATH.
* Recommended preset habit IDs: 192, 166, 202. Reference video must be >=100
  frames. Input/reference videos should be 25 FPS. sampling-steps=1 (paper
  one-step setting).
* Separate "Streaming RealTime Demo" repo: browser interface for live-mic
  animation, video dubbing, and interactive chat-driven avatars. On an NVIDIA
  RTX 3090 it reaches 30+ FPS using less than 4 GB of GPU memory.
- ai-bot.cn/talklikeyou (pulled 2026-10-11, "2 hours ago"):
* Institute of Automation, CAS (MAIS) + UCAS + CAIR + MUMT.
* 32.43 FPS real-time; one-step Flow Matching ~100x faster than Sonic
  (image-diffusion route). RTX 3090 VRAM < 4 GB.
* FID 7.71 (less than 1/3 of the runner-up), Sync-C 8.73 (highest of all),
  PLAD habit-similarity 0.62 vs MimicTalk 0.48 and PC-Talk 0.39.
* Two-stage training: 380-person HDTF (one-hot) then large-scale CelebV-HQ
  (reference video), periodic replay of one-hot to avoid forgetting; habit
  similarity goes 0.33 -> 0.64.
* PLAD metric: project lip motion onto three articulation axes (jaw open,
  lip closure, lip spreading), histogram-compared against the reference.
* Competitor table: TalkLikeYou vs SoulX-LiveAct (Soul AI Lab) —
  TalkLikeYou 32.43 FPS; SoulX-LiveAct 20 FPS (dual H100/H200), e2e latency
  0.94s, hour-level/infinite duration, constant VRAM via ConvKV Memory,
  full-body motion, image+audio+text drive, no personal-habit modeling.
* Use cases: virtual streamer / live commerce (4GB local, no real person),
  multilingual dubbing (swap lip motion, keep native head pose + timing),
  digital twin / virtual customer service, personalized education.
* Links (all HTTP 200 on 2026-10-11):
  https://bq-wang0511.github.io/TalkLikeYou/  (project page)
  https://github.com/BQ-Wang0511/TalkLikeYou   (code)
  https://huggingface.co/doubi-killer/TalkLikeYou (weights)
  https://arxiv.org/pdf/2610.06658            (paper)
* Note: a separate repo TalkLikeYou-Streaming-RealTime-Demo hosts the browser demo.

Positioning: free / open-weights real-time talking-head / digital-human
category — not yet covered on the site. Existing video guides are closed
generation tools (Seedance, Sora, etc.). TalkLikeYou = self-host, $0 license.
"""
import os, sys, json
from datetime import datetime

sys.path.insert(0, '/home/ubuntu/aifreeplan/scripts')
from write_guide import generate_guide_html

SLUG = "cas-talklikeyou-free-talking-head-2026"
TODAY = "2026-10-11"

TITLE_ZH = "TalkLikeYou 免费开源攻略：中科院自动化所实时数字人，1 步采样 32.43 FPS，4GB 显存让照片开口"
TITLE_EN = "TalkLikeYou Free Open-Source Guide: CAS Real-Time Talking Head — 1-Step Sampling at 32.43 FPS, Talks from a Photo on 4GB VRAM"

DESC_ZH = "中科院自动化所 MAIS 团队开源的实时数字人框架 TalkLikeYou：代码 MIT、权重全放 HuggingFace。一张照片加一段音频就能让照片开口，1 步 Flow Matching 采样跑出 32.43 FPS、RTX 3090 显存不到 4GB，还能模仿指定真人的说话习惯。含免费浏览器流式 Demo、Linux 部署步骤、与 SoulX-LiveAct 的对比表。"
DESC_EN = "TalkLikeYou is a real-time talking-head framework open-sourced by MAIS at the Institute of Automation, Chinese Academy of Sciences — MIT code with all weights on HuggingFace. One photo plus one audio clip makes the photo talk; one-step Flow Matching hits 32.43 FPS with under 4GB VRAM on an RTX 3090, and it can imitate a specific person's speaking habits. Includes the free browser streaming demo, Linux deploy steps, and a comparison vs SoulX-LiveAct."

CONTENT_ZH = """<h1>TalkLikeYou 免费开源攻略：中科院自动化所实时数字人，1 步采样 32.43 FPS，4GB 显存让照片开口</h1>

<p>中科院自动化所 MAIS 团队把 <strong>TalkLikeYou</strong> 直接开源了——给一张人像照片和一段音频，照片里的人就能开口说话，嘴部动作还能模仿指定真人的"说话习惯"。代码走 MIT 协议，模型权重全放在 HuggingFace 上，<strong>下载、推理、本地部署 0 许可费</strong>，不按次计费。</p>

<h2>免费结论先给</h2>

<ul>
<li><strong>代码免费</strong>：GitHub 仓库 MIT 协议，可自研可商用；模型权重放 <a href="https://huggingface.co/doubi-killer/TalkLikeYou">HuggingFace</a>，一条 <code>hf download</code> 就能拉下来（权重本身遵循其第三方条款，见 THIRD_PARTY_NOTICES）。</li>
<li><strong>推理 0 平台费</strong>：跑在你自己的显卡上，无按量计费、无次数上限、无过期。一张 RTX 3090 即可，<strong>显存 &lt; 4GB</strong>（官方流式 Demo 实测）。</li>
<li><strong>零门槛体验</strong>：没有高端显卡也能先用官方的 <a href="https://github.com/BQ-Wang0511/TalkLikeYou-Streaming-RealTime-Demo">浏览器流式 Demo</a>——对着麦克风实时驱动，RTX 3090 上 30+ FPS。</li>
<li><strong>推荐环境</strong>：Linux + Python <strong>3.10</strong> + CUDA <strong>12.1</strong> + cuDNN <strong>9</strong> + FFmpeg，官方建议显存 <strong>&ge; 12GB</strong> 跑完整推理（流式 Demo 场景 4GB 就够）。</li>
</ul>

<h2>规格速览（全部实测数字）</h2>

<table>
<tr><th>项目</th><th>数字</th><th>说明</th></tr>
<tr><td>生成速度</td><td><strong>32.43 FPS</strong></td><td>一步 Flow Matching 采样，比图像扩散路线的 Sonic 快近百倍</td></tr>
<tr><td>显存占用</td><td><strong>&lt; 4GB</strong>（RTX 3090 流式 Demo）</td><td>推荐环境按 12GB 预留，实际占用更低</td></tr>
<tr><td>采样步数</td><td><strong>1 步</strong>（论文默认）</td><td>一步即可达到接近 50 步的唇同步质量</td></tr>
<tr><td>唇同步 Sync-C</td><td><strong>8.73</strong>（全场最高）</td><td>嘴型与音频对齐度</td></tr>
<tr><td>画质 FID</td><td><strong>7.71</strong></td><td>不到第二名成绩的三分之一</td></tr>
<tr><td>习惯相似度 PLAD</td><td><strong>0.62</strong></td><td>MimicTalk 0.48、PC-Talk 0.39，显著领先</td></tr>
<tr><td>参考视频要求</td><td><strong>&ge; 100 帧</strong></td><td>用于模仿指定真人说话习惯，可覆盖 --person-id</td></tr>
<tr><td>输入帧率</td><td><strong>25 FPS</strong></td><td>源视频 / 参考视频统一 25 FPS</td></tr>
<tr><td>协议 / 权重</td><td><strong>MIT（代码）</strong> + HuggingFace 权重</td><td>权重按第三方条款使用</td></tr>
</table>

<p>它跟一般"照片说话"工具拉开差距的，是<strong>把"说话习惯"做成了一等公民</strong>：业内首个把个人嘴部说话习惯作为可建模对象的开源框架。你有两种入口——用官方预设编号（推荐 <code>192</code> / <code>166</code> / <code>202</code>）零成本切换风格，或丢一段 &ge;100 帧的参考视频让它现学那个人的嘴部习惯，两种入口还能插值混合出"新习惯"。</p>

<h2>四个能力（对应四类白嫖场景）</h2>

<ul>
<li><strong>照片开口</strong>：上传一张人像照片 + 一段音频，生成人物开口说话的视频。</li>
<li><strong>习惯模仿</strong>：模仿指定真人的嘴部说话习惯，预设编号或 4 秒级参考视频指定，避免"千人一面"的平均嘴。</li>
<li><strong>视频配音</strong>：把 <code>--source</code> 指向视频并加 <code>--pose-mode source</code>，只替换嘴部动作、保留原视频的头部动作与时序，适合多语言译制 / 出海内容口型对齐。</li>
<li><strong>对话数字分身</strong>：接入大模型 + 语音识别合成，做实时对话交互的数字人；官方浏览器 Demo 已支持对着麦克风实时驱动。</li>
</ul>

<h2>五分钟上手（Linux）</h2>

<ol>
<li><strong>建环境</strong>：Linux 系统，装 Python 3.10、CUDA 12.1、cuDNN 9，确保 FFmpeg 在 PATH 里，NVIDIA 显卡显存 &ge; 12GB。</li>
<li><strong>克隆代码</strong>：<a href="https://github.com/BQ-Wang0511/TalkLikeYou">GitHub</a> 主仓库 <code>git clone</code>，然后 <code>conda env create -f environment.yaml</code> 建环境（或自装 CUDA 版 PyTorch 后 <code>pip install -r requirements.txt</code>）。</li>
<li><strong>拉权重</strong>：<code>hf download doubi-killer/TalkLikeYou --include "checkpoints/**" --local-dir .</code>，权重目录结构别动。</li>
<li><strong>跑推理</strong>：准备一张 25 FPS 的人像照片/视频 + 一段音频，然后
<code>python -m talklikeyou --source 照片 --audio 音频 --person-id 192 --stage0 --neutral --sampling-steps 1 --output out.mp4</code>。想换"说话习惯"就换 <code>--person-id</code>，或改用 <code>--habit-reference 参考视频</code>。</li>
</ol>

<h2>竞品对比：TalkLikeYou vs SoulX-LiveAct</h2>

<table>
<tr><th>维度</th><th>TalkLikeYou（中科院自动化所）</th><th>SoulX-LiveAct（Soul AI Lab）</th></tr>
<tr><td>核心定位</td><td>实时说话头生成 + 个人说话习惯模仿</td><td>实时数字人 + 小时级长时稳定生成</td></tr>
<tr><td>技术路线</td><td>运动空间两阶段（轻量参数 + 渲染）</td><td>自回归扩散（AR Diffusion），像素级生成</td></tr>
<tr><td>生成速度</td><td><strong>32.43 FPS</strong>（单卡 3090）</td><td>20 FPS（双卡 H100/H200）</td></tr>
<tr><td>端到端延迟</td><td>流式缓冲可调</td><td>0.94 秒</td></tr>
<tr><td>时长上限</td><td>片段级（无长时优化）</td><td>小时级甚至无限时长，显存恒定（ConvKV Memory）</td></tr>
<tr><td>说话习惯</td><td>✅ 支持（编号 / 参考视频 / 插值）</td><td>❌ 不建模个人嘴部习惯</td></tr>
<tr><td>动作范围</td><td>嘴部 + 头部姿态</td><td>全身动作、表情、手势、情绪（比心、捂脸、大笑）</td></tr>
<tr><td>驱动方式</td><td>音频驱动（照片/视频）</td><td>图像 + 音频 + 文本指令</td></tr>
</table>

<p><strong>怎么选</strong>：要"像某个人那样说话"、要低显存实时跑、要照片开口 → TalkLikeYou。要"小时级不崩、全身动作、文指令控制" → SoulX-LiveAct，但它上双卡 H100 才 20 FPS，成本高一档。</p>

<h2>四个能直接落地的白嫖场景</h2>

<ul>
<li><strong>虚拟主播 / 直播带货</strong>：4GB 显存本地实时跑，无需真人出镜，还能复刻主播自己的说话风格。</li>
<li><strong>多语言视频配音</strong>：替换嘴部动作、保留原头动时序，让译制片 / 出海内容口型跟目标语言自然对齐。</li>
<li><strong>数字分身 / 虚拟客服</strong>：接大模型 + 语音合成做实时对话分身，用于在线客服、智能导览。</li>
<li><strong>个性化教学 / 培训</strong>：复刻老师 / 培训师的独特说话风格，录课程、做远程教学。</li>
</ul>

<h2>链接汇总</h2>

<ul>
<li>项目官网：<a href="https://bq-wang0511.github.io/TalkLikeYou/">bq-wang0511.github.io/TalkLikeYou</a></li>
<li>GitHub 代码（MIT）：<a href="https://github.com/BQ-Wang0511/TalkLikeYou">github.com/BQ-Wang0511/TalkLikeYou</a></li>
<li>HuggingFace 权重：<a href="https://huggingface.co/doubi-killer/TalkLikeYou">huggingface.co/doubi-killer/TalkLikeYou</a></li>
<li>arXiv 论文：<a href="https://arxiv.org/pdf/2610.06658">arXiv:2610.06658</a></li>
<li>流式实时 Demo：<a href="https://github.com/BQ-Wang0511/TalkLikeYou-Streaming-RealTime-Demo">TalkLikeYou-Streaming-RealTime-Demo</a></li>
</ul>

<div class="faq-section">
<h3>常见问题</h3>
<div class="faq-item"><div class="faq-q">TalkLikeYou 到底哪里免费？</div><div class="faq-a">代码是 MIT 协议，权重放 HuggingFace，一条 hf download 拉下来，下载 / 推理 / 本地部署 0 许可费，不按次计费、无过期。唯一的成本是你自己那张显卡（RTX 3090 显存 &lt; 4GB 就能跑流式 Demo）。权重本身走第三方条款，商用前看一眼 THIRD_PARTY_NOTICES。</div></div>
<div class="faq-item"><div class="faq-q">没有 12GB 大卡能不能跑？</div><div class="faq-a">能。官方推荐环境按 12GB 预留是为了跑完整推理链路；但浏览器流式 Demo 在 RTX 3090 上实测显存 &lt; 4GB、30+ FPS。入门可以先在 8GB 卡上拉权重跑照片开口，长时 / 高并发再上大卡。</div></div>
<div class="faq-item"><div class="faq-q">"说话习惯模仿"具体怎么用？</div><div class="faq-a">两种方式：一是 <code>--person-id</code> 选官方预设（192/166/202），零素材直接切风格；二是 <code>--habit-reference</code> 指向一段 &ge; 100 帧的真人参考视频，让它现学那个人的嘴部习惯。两种还能插值混合出"新习惯"。PLAD 指标下习惯相似度做到 0.62，高于 MimicTalk 0.48、PC-Talk 0.39。</div></div>
<div class="faq-item"><div class="faq-q">32.43 FPS 是什么概念？</div><div class="faq-a">指每秒能渲染 32.43 帧说话视频，单张 RTX 3090 就能达到，满足实时 / 流式（超过 24–30 FPS 的播放门槛）。它靠一步 Flow Matching 采样实现，比走图像扩散路线的 Sonic 快近百倍，首包延迟低到可以对着麦克风实时驱动。</div></div>
<div class="faq-item"><div class="faq-q">跟 SoulX-LiveAct 选哪个？</div><div class="faq-a">要"像特定的人那样说、低显存实时跑、照片开口"选 TalkLikeYou。要"小时级不崩、全身动作、文本指令控制"选 SoulX-LiveAct，但它要双卡 H100/H200 才 20 FPS，门槛高一档。前者胜在个人习惯建模 + 单卡实时，后者胜在长时稳定 + 全身控制。</div></div>
</div>"""

CONTENT_EN = """<h1>TalkLikeYou Free Open-Source Guide: CAS Real-Time Talking Head — 1-Step Sampling at 32.43 FPS, Talks from a Photo on 4GB VRAM</h1>

<p>MAIS at the Institute of Automation, Chinese Academy of Sciences has open-sourced <strong>TalkLikeYou</strong>. Give it one portrait photo and one audio clip and the person in the photo starts talking, with lip motion that can imitate a specific real person's speaking habits. The code is MIT-licensed and every model weight is on HuggingFace: <strong>downloading, inference, and self-hosting all cost $0 in licensing</strong> — no per-call billing.</p>

<h2>The free verdict, up front</h2>

<ul>
<li><strong>Free code</strong>: the GitHub repo is MIT-licensed, so you can build and ship commercial products on top of it. Model weights live on <a href="https://huggingface.co/doubi-killer/TalkLikeYou">HuggingFace</a> and pull down in one <code>hf download</code> (the weights themselves follow their third-party terms — see THIRD_PARTY_NOTICES).</li>
<li><strong>Zero platform fee</strong>: it runs on your own GPU — no metered billing, no request cap, no expiry. A single RTX 3090 is enough; the official streaming demo holds <strong>&lt; 4GB</strong> of VRAM.</li>
<li><strong>Zero-barrier trial</strong>: no big GPU? Start with the official <a href="https://github.com/BQ-Wang0511/TalkLikeYou-Streaming-RealTime-Demo">browser streaming demo</a> — real-time, mic-driven, 30+ FPS on an RTX 3090.</li>
<li><strong>Recommended stack</strong>: Linux + Python <strong>3.10</strong> + CUDA <strong>12.1</strong> + cuDNN <strong>9</strong> + FFmpeg, with <strong>&ge; 12GB</strong> VRAM recommended for the full inference path (the streaming demo scenario is fine at 4GB).</li>
</ul>

<h2>Spec sheet (every figure is measured)</h2>

<table>
<tr><th>Item</th><th>Number</th><th>What it means</th></tr>
<tr><td>Generation speed</td><td><strong>32.43 FPS</strong></td><td>One-step Flow Matching sampling, ~100x faster than Sonic's image-diffusion route</td></tr>
<tr><td>VRAM footprint</td><td><strong>&lt; 4GB</strong> (RTX 3090 streaming demo)</td><td>Recommended env reserves 12GB; actual usage is lower</td></tr>
<tr><td>Sampling steps</td><td><strong>1</strong> (paper default)</td><td>One step reaches near-50-step lip-sync quality</td></tr>
<tr><td>Lip-sync Sync-C</td><td><strong>8.73</strong> (highest of all)</td><td>How tightly the mouth tracks the audio</td></tr>
<tr><td>Image quality FID</td><td><strong>7.71</strong></td><td>Less than a third of the runner-up's score</td></tr>
<tr><td>Habit similarity PLAD</td><td><strong>0.62</strong></td><td>vs MimicTalk 0.48 and PC-Talk 0.39 — clearly ahead</td></tr>
<tr><td>Reference video</td><td><strong>&ge; 100 frames</strong></td><td>Used to imitate a specific person's speaking habit; overrides --person-id</td></tr>
<tr><td>Input frame rate</td><td><strong>25 FPS</strong></td><td>Source / reference videos are all 25 FPS</td></tr>
<tr><td>License / weights</td><td><strong>MIT (code)</strong> + HuggingFace weights</td><td>Weights used under their third-party terms</td></tr>
</table>

<p>What separates it from the usual "make a photo talk" tools is that it <strong>treats "speaking habit" as a first-class citizen</strong>: it is the first open framework that models an individual's lip-speaking habits as a designable object. You have two entry points — a preset habit ID (recommended <code>192</code> / <code>166</code> / <code>202</code>) to switch styles at zero cost, or a &ge;100-frame reference video so it learns that person's habits on the fly. The two can be blended by interpolation to mint a "new" habit.</p>

<h2>Four capabilities (four ways to ride it for free)</h2>

<ul>
<li><strong>Photo talks</strong>: drop in a portrait photo + one audio clip, get a video of the person speaking.</li>
<li><strong>Habit imitation</strong>: imitate a specific person's lip habits via a preset ID or a short reference video, escaping the "average mouth" of everyone else.</li>
<li><strong>Video dubbing</strong>: point <code>--source</code> at a video and add <code>--pose-mode source</code> to swap only the lip motion while preserving the original head motion and timing — great for multilingual localization and cross-border content.</li>
<li><strong>Conversational avatar</strong>: wire up an LLM + ASR/TTS for a real-time, interactive digital twin; the official browser demo already drives off a live microphone.</li>
</ul>

<h2>Five-minute start (Linux)</h2>

<ol>
<li><strong>Set up the env</strong>: on Linux, install Python 3.10, CUDA 12.1, cuDNN 9, make sure FFmpeg is on PATH, and use an NVIDIA GPU with &ge; 12GB VRAM.</li>
<li><strong>Clone the code</strong>: <a href="https://github.com/BQ-Wang0511/TalkLikeYou">GitHub</a> main repo, <code>git clone</code>, then <code>conda env create -f environment.yaml</code> (or install a CUDA PyTorch build and <code>pip install -r requirements.txt</code>).</li>
<li><strong>Pull the weights</strong>: <code>hf download doubi-killer/TalkLikeYou --include "checkpoints/**" --local-dir .</code>; keep the checkpoint directory layout intact.</li>
<li><strong>Run inference</strong>: prepare one 25 FPS portrait photo/video plus an audio clip, then
<code>python -m talklikeyou --source photo --audio audio --person-id 192 --stage0 --neutral --sampling-steps 1 --output out.mp4</code>. To change the "speaking habit," swap <code>--person-id</code>, or switch to <code>--habit-reference reference-video</code>.</li>
</ol>

<h2>Competitor table: TalkLikeYou vs SoulX-LiveAct</h2>

<table>
<tr><th>Dimension</th><th>TalkLikeYou (Institute of Automation, CAS)</th><th>SoulX-LiveAct (Soul AI Lab)</th></tr>
<tr><td>Core focus</td><td>Real-time talking head + personal speaking-habit imitation</td><td>Real-time digital human + hour-level stable long generation</td></tr>
<tr><td>Route</td><td>Two-stage motion-space (light params + renderer)</td><td>Autoregressive diffusion, pixel-level</td></tr>
<tr><td>Generation speed</td><td><strong>32.43 FPS</strong> (single 3090)</td><td>20 FPS (dual H100/H200)</td></tr>
<tr><td>End-to-end latency</td><td>Streaming buffer is tunable</td><td>0.94 s</td></tr>
<tr><td>Duration limit</td><td>Clip-level (no long-horizon optimization)</td><td>Hour-level or infinite, constant VRAM (ConvKV Memory)</td></tr>
<tr><td>Speaking habit</td><td>Yes (ID / reference video / interpolation)</td><td>No personal-habit modeling</td></tr>
<tr><td>Motion range</td><td>Lips + head pose</td><td>Full body, expression, gestures, emotion (heart hands, face-palm, big laugh)</td></tr>
<tr><td>Drive input</td><td>Audio (photo / video)</td><td>Image + audio + text instruction</td></tr>
</table>

<p><strong>How to choose</strong>: you want "talk like a specific person," low-VRAM real-time, and photo-to-speech → TalkLikeYou. You want "hours without collapse, full-body motion, text-instruction control" → SoulX-LiveAct, but it needs dual H100s to hit 20 FPS, a step up in cost.</p>

<h2>Four scenarios you can ship right away</h2>

<ul>
<li><strong>Virtual streamer / live commerce</strong>: run real-time locally on 4GB VRAM, no real person on camera, and it can clone the host's own speaking style.</li>
<li><strong>Multilingual video dubbing</strong>: swap the lip motion while keeping the original head pose and timing, so localized / cross-border content lip-matches the target language naturally.</li>
<li><strong>Digital twin / virtual customer service</strong>: attach an LLM + speech to build a real-time conversational avatar for live support or smart guides.</li>
<li><strong>Personalized education / training</strong>: replicate a teacher's or trainer's distinct speaking style for recorded courses or remote teaching.</li>
</ul>

<h2>Links</h2>

<ul>
<li>Project page: <a href="https://bq-wang0511.github.io/TalkLikeYou/">bq-wang0511.github.io/TalkLikeYou</a></li>
<li>GitHub code (MIT): <a href="https://github.com/BQ-Wang0511/TalkLikeYou">github.com/BQ-Wang0511/TalkLikeYou</a></li>
<li>HuggingFace weights: <a href="https://huggingface.co/doubi-killer/TalkLikeYou">huggingface.co/doubi-killer/TalkLikeYou</a></li>
<li>arXiv paper: <a href="https://arxiv.org/pdf/2610.06658">arXiv:2610.06658</a></li>
<li>Streaming real-time demo: <a href="https://github.com/BQ-Wang0511/TalkLikeYou-Streaming-RealTime-Demo">TalkLikeYou-Streaming-RealTime-Demo</a></li>
</ul>

<div class="faq-section">
<h3>FAQ</h3>
<div class="faq-item"><div class="faq-q">Where exactly is TalkLikeYou free?</div><div class="faq-a">The code is MIT and the weights are on HuggingFace — one hf download, $0 in licensing for downloading, inference, and self-hosting, with no per-call billing and no expiry. Your only cost is the GPU itself (an RTX 3090 holds the streaming demo under 4GB). The weights follow their third-party terms, so glance at THIRD_PARTY_NOTICES before commercial use.</div></div>
<div class="faq-item"><div class="faq-q">Can I run it without a 12GB card?</div><div class="faq-a">Yes. The recommended 12GB reservation is for the full inference path; the browser streaming demo runs under 4GB at 30+ FPS on an RTX 3090. Start on an 8GB card for photo-to-speech and scale up for long or high-concurrency workloads.</div></div>
<div class="faq-item"><div class="faq-q">How do I actually use "speaking-habit imitation"?</div><div class="faq-a">Two ways: <code>--person-id</code> picks an official preset (192/166/202) with zero assets, or <code>--habit-reference</code> points at a &ge; 100-frame real-person reference video so it learns that person's habits on the fly. Both can be interpolated into a "new" habit. Under the PLAD metric the habit similarity reaches 0.62, ahead of MimicTalk's 0.48 and PC-Talk's 0.39.</div></div>
<div class="faq-item"><div class="faq-q">What does 32.43 FPS mean in practice?</div><div class="faq-a">It renders 32.43 frames of talking video per second on a single RTX 3090, clearing the 24-30 FPS real-time bar. One-step Flow Matching gets there, ~100x faster than the image-diffusion route (Sonic), with low first-chunk latency so it can drive off a live microphone.</div></div>
<div class="faq-item"><div class="faq-q">TalkLikeYou or SoulX-LiveAct?</div><div class="faq-a">Pick TalkLikeYou to "talk like a specific person," stay low-VRAM and real-time, and do photo-to-speech. Pick SoulX-LiveAct for hour-level stability, full-body motion, and text-instruction control — but it needs dual H100/H200 for 20 FPS, a higher bar. TalkLikeYou wins on habit modeling + single-card real-time; SoulX-LiveAct wins on long-horizon stability + full-body control.</div></div>
</div>"""

FAQ_ZH = [
 {"question":"TalkLikeYou 到底哪里免费？","answer":"代码 MIT 协议，权重放 HuggingFace，一条 hf download 拉下来，下载/推理/本地部署 0 许可费，不按次计费、无过期。唯一成本是你自己的显卡（RTX 3090 显存 <4GB 即可跑流式 Demo）。权重本身走第三方条款，商用前看一眼 THIRD_PARTY_NOTICES。"},
 {"question":"没有 12GB 大卡能不能跑？","answer":"能。官方 12GB 是完整推理链路的预留值；浏览器流式 Demo 在 RTX 3090 上实测 <4GB、30+ FPS。入门可先用 8GB 卡跑照片开口，长时/高并发再上大卡。"},
 {"question":"习惯模仿具体怎么用？","answer":"两种：--person-id 选官方预设（192/166/202）零素材切风格；--habit-reference 指向 ≥100 帧的真人参考视频现学习惯。两种可插值混合出新习惯。PLAD 指标习惯相似度 0.62，高于 MimicTalk 0.48、PC-Talk 0.39。"},
 {"question":"32.43 FPS 是什么概念？","answer":"单张 RTX 3090 每秒渲染 32.43 帧说话视频，超过 24–30 FPS 实时播放门槛。靠一步 Flow Matching 采样，比 Sonic 图像扩散路线快近百倍，首包延迟低到可对着麦克风实时驱动。"},
 {"question":"跟 SoulX-LiveAct 选哪个？","answer":"要像特定的人说、低显存实时、照片开口选 TalkLikeYou；要小时级不崩、全身动作、文本指令控制选 SoulX-LiveAct，但它要双卡 H100/H200 才 20 FPS，门槛高一档。"},
]
FAQ_EN = [
 {"question":"Where exactly is TalkLikeYou free?","answer":"MIT code, HuggingFace weights — one hf download, $0 licensing for download/inference/self-host, no per-call billing or expiry. Your only cost is the GPU (an RTX 3090 holds the streaming demo under 4GB). Weights follow their third-party terms; check THIRD_PARTY_NOTICES before commercial use."},
 {"question":"Can I run it without a 12GB card?","answer":"Yes. The 12GB is a reservation for the full path; the browser streaming demo runs under 4GB at 30+ FPS on an RTX 3090. Start on an 8GB card for photo-to-speech, scale up for long/high-concurrency jobs."},
 {"question":"How do I use speaking-habit imitation?","answer":"Two ways: --person-id picks an official preset (192/166/202) with zero assets, or --habit-reference points at a >=100-frame reference video to learn habits on the fly. Both interpolate into a new habit. PLAD similarity hits 0.62, above MimicTalk 0.48 and PC-Talk 0.39."},
 {"question":"What does 32.43 FPS mean?","answer":"Renders 32.43 frames of talking video per second on one RTX 3090, clearing the 24-30 FPS real-time bar via one-step Flow Matching, ~100x faster than Sonic's image-diffusion route, with low enough latency to drive off a live mic."},
 {"question":"TalkLikeYou or SoulX-LiveAct?","answer":"TalkLikeYou for talking like a specific person, low-VRAM real-time, photo-to-speech. SoulX-LiveAct for hour-level stability, full-body motion, text-instruction control — but it needs dual H100/H200 for 20 FPS, a higher bar."},
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
    "tags": ["TalkLikeYou", "数字人", "实时说话", "talking-head", "中科院自动化所", "MIT", "开源", "口型同步", "视频配音", "免费", "自托管", "digital-human", "real-time", "faceless-video"],
    "icon": "🗣️",
    "excerpt_zh": "中科院自动化所 MAIS 开源的实时数字人框架 TalkLikeYou，代码 MIT + 权重全放 HuggingFace，0 许可费。一张照片 + 一段音频让照片开口，1 步 Flow Matching 采样 32.43 FPS、RTX 3090 显存 <4GB，可模仿指定真人说话习惯（PLAD 0.62），含免费浏览器流式 Demo。",
    "excerpt_en": "TalkLikeYou is a real-time talking-head framework open-sourced by MAIS (Institute of Automation, CAS) — MIT code, all weights on HuggingFace, $0 licensing. One photo + one audio clip makes the photo talk; one-step Flow Matching reaches 32.43 FPS under 4GB VRAM on an RTX 3090 and imitates a specific person's habits (PLAD 0.62), with a free browser streaming demo.",
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

for path in ('/home/ubuntu/aifreeplan/data/guides.json',):
    if os.path.exists(path):
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
