#!/usr/bin/env python3
"""Generate and deploy Nativ guide article."""
import os
import sys
from datetime import datetime

def main():
    today = datetime.now().strftime('%Y-%m-%d')
    slug = "nativ-free-local-ai-mac-2026"
    
    title_zh = "Nativ 免费本地 AI 桌面应用：Apple Silicon 上运行开源模型，零订阅零云端零账户"
    title_en = "Nativ Free Local AI for Mac: Run Open Models on Apple Silicon — Zero Subscription, Zero Cloud, Zero Accounts"
    desc_zh = "Nativ 是一款 100% 开源、MIT 许可的 macOS 原生 AI 应用，专为 Apple Silicon 设计。基于 MLX 框架，可在本地运行前沿开源模型，支持聊天、代码补全、语音转录等多种模态。完全免费，无需注册账户、无需订阅、无需云端连接。"
    desc_en = "Nativ is a 100% open-source, MIT-licensed macOS-native AI app designed for Apple Silicon. Powered by the MLX framework, it runs frontier open models locally, supporting chat, code completion, voice transcription, and more. Completely free — no account registration, no subscription, no cloud connection needed."
    
    content_zh = """<h1>Nativ 免费本地 AI 桌面应用：Apple Silicon 上运行开源模型，零订阅零云端零账户</h1>

<p>2026年7月，<strong>Nativ</strong> 作为一个全新的 macOS 原生 AI 应用横空出世，迅速在开发者社区引发关注。它承诺了一件事：<strong>在你的 Mac 上本地运行前沿 AI 模型，完全免费，不需要任何账户、订阅或云端服务</strong>。对于重视隐私、希望摆脱 SaaS 绑定的用户来说，这是一个令人振奋的选择。</p>

<h2>什么是 Nativ？</h2>

<p>Nativ 是一个基于 <strong>SwiftUI</strong> 开发的 macOS 原生应用，底层使用 <strong>MLX-VLM</strong>（Meta 的 MLX 推理框架）作为推理引擎。它不仅仅是一个聊天界面，而是一个完整的本地 AI 工作区：</p>

<ul>
<li><strong>本地聊天与视觉：</strong>流式对话响应、图片附件、推理输出、逐条消息的性能指标，以及持久化的聊天记录。</li>
<li><strong>模型库管理：</strong>发现已安装的 MLX 模型、浏览 Hugging Face 上的兼容模型、一键下载、检查模型能力、切换模型或删除旧模型。</li>
<li><strong>性能分析面板：</strong>追踪请求量、Token 用量、首字延迟（TTFT）、解码速度、模型性能和最近活动。</li>
<li><strong>本地 API 服务器：</strong>提供 OpenAI 兼容的 /v1/chat/completions、/v1/responses、/v1/models、图像和音频端点，以及 Anthropic 兼容的 /v1/messages 端点。</li>
<li><strong>编码工具集成：</strong>可配置并启动 Codex、Claude Code、Pi、Hermes 和 OpenCode 等编码代理，让它们连接到你在本地运行的模型。</li>
<li><strong>菜单栏控制：</strong>启动/停止服务器、切换加载的模型、查看服务统计信息，无需打断当前工作流。</li>
<li><strong>高级推理控制：</strong>调节采样参数、思维预算（thinking budget）、结构化输出、KV 缓存量化、前缀缓存和推测性解码。</li>
</ul>

<h2>系统要求</h2>

<table>
<tr><th>项目</th><th>要求</th></tr>
<tr><td>硬件</td><td>Apple Silicon Mac（M1 及以上）</td></tr>
<tr><td>操作系统</td><td>macOS 26+ (Sequoia)</td></tr>
<tr><td>统一内存</td><td>取决于选择的模型大小（见下文）</td></tr>
<tr><td>许可证</td><td>MIT（完全免费）</td></tr>
<tr><td>网络需求</td><td>仅首次下载模型时需要，运行时完全离线</td></tr>
</table>

<h2>支持的模型</h2>

<p>Nativ 预集成了来自 Google、Cohere 和 Liquid AI 的精选开源模型。以下是当前推荐的模型列表及其对硬件的要求：</p>

<table>
<tr><th>模型</th><th>来源</th><th>上下文窗口</th><th>模型大小</th><th>能力</th></tr>
<tr><td>Gemma 4 E2B Instruct</td><td>Google</td><td>128K</td><td>10.28 GB</td><td>视觉 + 音频</td></tr>
<tr><td>North Mini Code</td><td>Cohere</td><td>500K</td><td>19.38 GB</td><td>代码 + 工具调用</td></tr>
<tr><td>LFM2.5-VL 1.6B</td><td>Liquid AI</td><td>128K</td><td>3.20 GB</td><td>视觉 + 语言</td></tr>
</table>

<p><strong>内存需求参考：</strong></p>
<ul>
<li>3.2 GB 模型：需要至少 8GB 统一内存的 Mac</li>
<li>10.28 GB 模型：需要至少 16GB 统一内存的 Mac</li>
<li>19.38 GB 模型：需要至少 24GB 统一内存的 Mac（M2/M3 Max 或 M4 Pro/Max）</li>
</ul>

<p>Nativ 会根据你的硬件自动推荐合适的模型。你也可以通过 Hugging Face 手动下载更多 MLX 格式的模型。</p>

<h2>为什么 Nativ 值得关注？</h2>

<h3>1. 真正的本地运行，不泄露任何数据</h3>

<p>所有推理都在你的 Mac 上完成。你的提示词、对话历史、图片附件<strong>永远不会离开你的设备</strong>。这与 ChatGPT、Claude 等云端服务形成鲜明对比——后者会将你的输入发送到他们的服务器进行处理。</p>

<h3>2. 完全免费，MIT 许可</h3>

<p>Nativ 采用 <strong>MIT 开源许可证</strong>发布，意味着：</p>
<ul>
<li>免费下载和使用，无次数限制</li>
<li>任何人都可以审查源代码</li>
<li>可以 Fork 和修改代码</li>
<li>没有"企业版"陷阱——没有隐藏功能被锁在付费墙后面</li>
</ul>

<h3>3. 可作为本地 API 服务器使用</h3>

<p>Nativ 默认在 <code>http://127.0.0.1:8080</code> 启动一个本地 API 服务器。你可以像调用 OpenAI API 一样调用它：</p>

<pre><code>curl http://127.0.0.1:8080/v1/chat/completions \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "your-model-id",
    "messages": [{"role": "user", "content": "你好"}],
    "stream": false
  }'</code></pre>

<p>它还支持 Anthropic Messages API 格式，这意味着许多支持 Claude API 的工具都可以无缝切换到本地模型。</p>

<h3>4. 编码代理集成</h3>

<p>Nativ 内置了对主流编码代理的支持：<strong>Codex、Claude Code、Pi、Hermes 和 OpenCode</strong>。你可以将这些代理的配置指向 Nativ 的本地 API 端点，从而让你的编码工具使用本地运行的开源模型，而不是昂贵的云端 API。</p>

<h3>5. 实时监控仪表盘</h3>

<p>Nativ 提供了开发者真正需要的遥测数据：</p>
<ul>
<li><strong>Tokens/秒：</strong>实时解码速度</li>
<li><strong>内存压力：</strong>当前统一内存使用情况</li>
<li><strong>热状态：</strong>Mac 的散热和温度状况</li>
<li><strong>首字延迟（TTFT）：</strong>从发送到收到第一个 token 的时间</li>
</ul>

<h2>与云端 AI 服务的对比</h2>

<table>
<tr><th>特性</th><th>Nativ（本地）</th><th>ChatGPT</th><th>Claude</th><th>Gemini</th></tr>
<tr><td>费用</td><td>✅ 完全免费</td><td>$20/月</td><td>按量计费</td><td>部分免费</td></tr>
<tr><td>隐私</td><td>✅ 数据不离设备</td><td>❌ 数据上传云端</td><td>❌ 数据上传云端</td><td>❌ 数据上传云端</td></tr>
<tr><td>离线可用</td><td>✅ 完全离线</td><td>❌ 需要网络</td><td>❌ 需要网络</td><td>❌ 需要网络</td></tr>
<tr><td>自定义模型</td><td>✅ 可切换任意 MLX 模型</td><td>❌ 固定模型</td><td>❌ 固定模型</td><td>❌ 固定模型</td></tr>
<tr><td>API 兼容性</td><td>✅ OpenAI + Anthropic</td><td>—</td><td>✅ Anthropic</td><td>✅ OpenAI 兼容</td></tr>
<tr><td>编码代理集成</td><td>✅ 内置支持</td><td>❌</td><td>❌</td><td>❌</td></tr>
<tr><td>平台</td><td>macOS (Apple Silicon)</td><td>全平台</td><td>全平台</td><td>全平台</td></tr>
</table>

<h2>安装指南</h2>

<h3>方法一：直接下载（推荐）</h3>
<ol>
<li>访问 <a href="https://github.com/Blaizzy/nativ/releases/latest">Nativ GitHub Releases 页面</a></li>
<li>下载最新版的 <code>Nativ-*.dmg</code> 文件（当前版本约 342 MB）</li>
<li>将 Nativ 拖入 Applications 文件夹</li>
<li>首次启动时，选择一个已安装的模型或继续按需加载</li>
</ol>

<h3>方法二：从源码编译</h3>
<p>如果你有开发环境，可以从源码构建：</p>
<pre><code>brew install xcodegen
make xcode-generate
make xcode-build
open build/XcodeDerivedData/Build/Products/Debug/Nativ.app</code></pre>
<p>注意：首次构建需要较长时间，因为 NativServerKit 会创建一个可重定位的 Python 运行时并安装 MLX 依赖。</p>

<h2>实际使用场景</h2>

<h3>1. 隐私敏感型对话</h3>
<p>医疗、法律、金融等行业的专业人士可以使用 Nativ 在本地运行模型，确保敏感信息不会泄露到任何第三方服务器。这对于需要遵守 GDPR、HIPAA 等数据保护法规的场景尤为重要。</p>

<h3>2. 编程辅助</h3>
<p>通过将 Nativ 的本地 API 端点配置到 Codex 或 Claude Code 中，开发者可以在本地获得类似 GitHub Copilot 的代码补全和对话辅助，无需支付订阅费，也无需将代码发送到云端。</p>

<h3>3. 离线环境工作</h3>
<p>在没有网络连接的环境下（如飞机上、偏远地区、安全隔离的网络），Nativ 仍然是可用的——只要模型已经下载到本地。</p>

<h3>4. 模型研究和实验</h3>
<p>研究人员可以利用 Nativ 的性能分析面板实时监控不同模型在 Apple Silicon 上的表现，比较不同模型的速度、质量和资源消耗。</p>

<h3>5. 多模态内容处理</h3>
<p>Nativ 支持文本、图像、视频摘要和语音转录。你可以用它来：</p>
<ul>
<li>给图片添加描述（Captioning）</li>
<li>总结视频内容</li>
<li>代码自动补全</li>
<li>语音转录和生成</li>
</ul>

<h2>已知限制</h2>

<ol>
<li><strong>仅限 Apple Silicon：</strong>Nativ 只支持 M1/M2/M3/M4 系列的 Mac，Intel Mac 无法运行。</li>
<li><strong>macOS 26+：</strong>需要较新的 macOS 版本（Sequoia 或更新）。</li>
<li><strong>模型大小受内存限制：</strong>你只能运行能装进 Mac 统一内存的模型。16GB 内存的 Mac 大约能跑 10GB 级别的模型。</li>
<li><strong>推理速度不如云端 GPU：</strong>虽然 Apple Silicon 的 MLX 优化很好，但对于大型模型，速度仍不及云端 A100/H100 GPU。</li>
<li><strong>音频和图片生成模型尚在开发中：</strong>专门的纯音频和图片生成模型将在未来版本中支持。</li>
</ol>

<h2>常见问题</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: Nativ 真的完全免费吗？有没有隐藏费用？</div>
<div class="faq-a">是的，Nativ 采用 MIT 许可证完全免费，无任何订阅费用、无内购、无隐藏收费。模型本身也是开源免费的（如 Gemma 系列来自 Google）。唯一可能需要付费的是你从 Hugging Face 下载某些专有模型的权限，但这不是 Nativ 的限制。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 我的 Mac 是 M1 16GB，可以运行哪些模型？</div>
<div class="faq-a">16GB 统一内存的 M1 Mac 可以流畅运行 10GB 左右的模型，如 Gemma 4 E2B Instruct（10.28 GB）。3.2 GB 的 LFM2.5-VL 模型在任何 Apple Silicon Mac 上都能运行。Nativ 会根据你的硬件自动推荐合适的模型。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Nativ 支持中文吗？</div>
<div class="faq-a">Nativ 本身是英文界面，但它运行的模型（如 Gemma）支持多语言输入输出，包括中文。你可以用中文与模型对话，模型会以中文回复。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 我可以在 Windows 或 Linux 上使用 Nativ 吗？</div>
<div class="faq-a">不可以。Nativ 是专为 macOS 和 Apple Silicon 构建的原生应用，依赖于 MLX 框架和 Apple 的统一内存架构。Windows/Linux 用户可以考虑 Ollama 或其他跨平台替代方案。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Nativ 如何保证我的数据不会被泄露？</div>
<div class="faq-a">Nativ 的所有推理都在本地完成，不发送任何数据到云端。API 服务器绑定在 localhost (127.0.0.1)，外部设备无法访问。如果你启用了服务器 API Key，还可以进一步保护管理端点。源代码是开源的，任何人都可以审计。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 如何更新 Nativ？</div>
<div class="faq-a">Nativ 使用 Sparkle 框架进行应用内自动更新。启动应用后，它会检查是否有新版本并提示你下载更新。</div>
</div>
</div>

<h2>总结</h2>

<p>Nativ 代表了 AI 工具的一个新方向：<strong>把智能带回你的设备</strong>。它不是一个功能受限的试用版，也不是"免费层+付费解锁"的模式——它是一个完整的、功能丰富的、100% 开源的本地 AI 工作区。</p>

<p>如果你有一台 Apple Silicon Mac，并且厌倦了为各种 AI 服务支付订阅费、担心数据隐私、或者希望在离线环境下也能使用 AI，那么 Nativ 是目前最好的选择之一。它完全免费、开源可审计、支持多种模型和模态，还能作为编码代理的后端服务器。</p>

<p>立即下载，体验真正的本地 AI：<a href="https://github.com/Blaizzy/nativ/releases/latest">访问 Nativ GitHub Releases</a></p>
"""
    
    content_en = """<h1>Nativ Free Local AI for Mac: Run Open Models on Apple Silicon — Zero Subscription, Zero Cloud, Zero Accounts</h1>

<p>In July 2026, <strong>Nativ</strong> emerged as a brand-new macOS-native AI application, quickly gaining traction in the developer community. Its promise is simple: <strong>run frontier AI models locally on your Mac, completely free, with no accounts, subscriptions, or cloud services required</strong>. For privacy-conscious users tired of SaaS lock-in, this is a compelling option.</p>

<h2>What is Nativ?</h2>

<p>Nativ is a <strong>SwiftUI</strong>-built macOS-native application powered by <strong>MLX-VLM</strong> (Meta's MLX inference framework) as its inference engine. It's more than just a chat interface — it's a complete local AI workspace:</p>

<ul>
<li><strong>Local Chat & Vision:</strong> Streaming conversations, image attachments, reasoning output, per-message performance metrics, and persistent chat history.</li>
<li><strong>Model Library:</strong> Discover installed MLX models, browse compatible models on Hugging Face, download them, inspect capabilities, switch models, or remove old ones.</li>
<li><strong>Performance Analytics:</strong> Track request volume, token usage, time to first token, decode speed, model performance, and recent activity.</li>
<li><strong>Local API Server:</strong> OpenAI-compatible /v1/chat/completions, /v1/responses, /v1/models, image, and audio endpoints, plus Anthropic-compatible /v1/messages endpoints.</li>
<li><strong>Coding Tool Integrations:</strong> Configure and launch Codex, Claude Code, Pi, Hermes, and OpenCode to connect to models running locally via Nativ.</li>
<li><strong>Menu Bar Controls:</strong> Start or stop the server, change the loaded model, check serving statistics, all without breaking focus.</li>
<li><strong>Advanced Inference Controls:</strong> Tune sampling, thinking budgets, structured output, KV-cache quantization, prefix caching, and speculative decoding.</li>
</ul>

<h2>System Requirements</h2>

<table>
<tr><th>Item</th><th>Requirement</th></tr>
<tr><td>Hardware</td><td>Apple Silicon Mac (M1 or later)</td></tr>
<tr><td>Operating System</td><td>macOS 26+ (Sequoia)</td></tr>
<tr><td>Unified Memory</td><td>Depends on chosen model size (see below)</td></tr>
<tr><td>License</td><td>MIT (completely free)</td></tr>
<tr><td>Network</td><td>Only needed for initial model download; fully offline after</td></tr>
</table>

<h2>Supported Models</h2>

<p>Nativ ships with curated open models from Google, Cohere, and Liquid AI. Here are the currently recommended models and their hardware requirements:</p>

<table>
<tr><th>Model</th><th>Source</th><th>Context Window</th><th>Model Size</th><th>Capabilities</th></tr>
<tr><td>Gemma 4 E2B Instruct</td><td>Google</td><td>128K</td><td>10.28 GB</td><td>Vision + Audio</td></tr>
<tr><td>North Mini Code</td><td>Cohere</td><td>500K</td><td>19.38 GB</td><td>Code + Tool Use</td></tr>
<tr><td>LFM2.5-VL 1.6B</td><td>Liquid AI</td><td>128K</td><td>3.20 GB</td><td>Vision + Language</td></tr>
</table>

<p><strong>Memory requirements reference:</strong></p>
<ul>
<li>3.2 GB model: Requires Mac with at least 8GB unified memory</li>
<li>10.28 GB model: Requires Mac with at least 16GB unified memory</li>
<li>19.38 GB model: Requires Mac with at least 24GB unified memory (M2/M3 Max or M4 Pro/Max)</li>
</ul>

<p>Nativ automatically recommends models suited to your hardware. You can also manually download additional MLX-format models from Hugging Face.</p>

<h2>Why Nativ Matters</h2>

<h3>1. True local inference — zero data leakage</h3>

<p>All inference runs on your Mac. Your prompts, chat history, and image attachments <strong>never leave your device</strong>. This stands in stark contrast to ChatGPT, Claude, and other cloud services that send your inputs to their servers for processing.</p>

<h3>2. Completely free, MIT licensed</h3>

<p>Nativ is released under the <strong>MIT open-source license</strong>, which means:</p>
<ul>
<li>Free to download and use, with no usage limits</li>
<li>Anyone can audit the source code</li>
<li>You can Fork and modify the code</li>
<li>No "enterprise edition" trap — no features locked behind a paywall</li>
</ul>

<h3>3. Acts as a local API server</h3>

<p>Nativ starts a local API server by default at <code>http://127.0.0.1:8080</code>. You can call it just like the OpenAI API:</p>

<pre><code>curl http://127.0.0.1:8080/v1/chat/completions \\
  -H 'Content-Type: application/json' \\
  -d '{
    "model": "your-model-id",
    "messages": [{"role": "user", "content": "Hello"}],
    "stream": false
  }'</code></pre>

<p>It also supports Anthropic Messages API format, meaning many tools that support the Claude API can seamlessly switch to local models.</p>

<h3>4. Coding agent integration</h3>

<p>Nativ has built-in support for major coding agents: <strong>Codex, Claude Code, Pi, Hermes, and OpenCode</strong>. You can point these agents to Nativ's local API endpoint, letting your coding tools use locally-run open models instead of expensive cloud APIs.</p>

<h3>5. Real-time monitoring dashboard</h3>

<p>Nativ provides telemetry that developers actually want:</p>
<ul>
<li><strong>Tokens/sec:</strong> Real-time decode speed</li>
<li><strong>Memory pressure:</strong> Current unified memory usage</li>
<li><strong>Thermal state:</strong> Mac heat and temperature status</li>
<li><strong>Time to first token (TTFT):</strong> Time from sending to receiving the first token</li>
</ul>

<h2>Comparison with Cloud AI Services</h2>

<table>
<tr><th>Feature</th><th>Nativ (Local)</th><th>ChatGPT</th><th>Claude</th><th>Gemini</th></tr>
<tr><td>Cost</td><td>✅ Completely Free</td><td>$20/month</td><td>Pay-per-use</td><td>Partially free</td></tr>
<tr><td>Privacy</td><td>✅ Data stays on device</td><td>❌ Data uploaded to cloud</td><td>❌ Data uploaded to cloud</td><td>❌ Data uploaded to cloud</td></tr>
<tr><td>Offline access</td><td>✅ Fully offline</td><td>❌ Requires internet</td><td>❌ Requires internet</td><td>❌ Requires internet</td></tr>
<tr><td>Custom models</td><td>✅ Switch any MLX model</td><td>❌ Fixed model</td><td>❌ Fixed model</td><td>❌ Fixed model</td></tr>
<tr><td>API compatibility</td><td>✅ OpenAI + Anthropic</td><td>—</td><td>✅ Anthropic</td><td>✅ OpenAI-compatible</td></tr>
<tr><td>Coding agent integration</td><td>✅ Built-in support</td><td>❌</td><td>❌</td><td>❌</td></tr>
<tr><td>Platform</td><td>macOS (Apple Silicon)</td><td>All platforms</td><td>All platforms</td><td>All platforms</td></tr>
</table>

<h2>Installation Guide</h2>

<h3>Method 1: Direct Download (Recommended)</h3>
<ol>
<li>Visit the <a href="https://github.com/Blaizzy/nativ/releases/latest">Nativ GitHub Releases page</a></li>
<li>Download the latest <code>Nativ-*.dmg</code> file (current version is approximately 342 MB)</li>
<li>Drag Nativ to your Applications folder</li>
<li>On first launch, select an installed model or continue with load-on-demand</li>
</ol>

<h3>Method 2: Build from Source</h3>
<p>If you have a development environment, you can build from source:</p>
<pre><code>brew install xcodegen
make xcode-generate
make xcode-build
open build/XcodeDerivedData/Build/Products/Debug/Nativ.app</code></pre>
<p>Note: The first build takes a while because NativServerKit creates a relocatable Python runtime and installs MLX dependencies.</p>

<h2>Real-World Use Cases</h2>

<h3>1. Privacy-sensitive conversations</h3>
<p>Professionals in healthcare, legal, and finance can use Nativ to run models locally, ensuring sensitive information never leaks to third-party servers. This is especially important for compliance with regulations like GDPR and HIPAA.</p>

<h3>2. Programming assistance</h3>
<p>By pointing Codex or Claude Code to Nativ's local API endpoint, developers get GitHub Copilot-like code completion and conversational assistance locally, without paying subscription fees or sending code to the cloud.</p>

<h3>3. Offline work</h3>
<p>In environments without internet connectivity (on a plane, remote areas, air-gapped networks), Nativ still works — as long as the model is already downloaded locally.</p>

<h3>4. Model research and experimentation</h3>
<p>Researchers can use Nativ's performance analytics panel to monitor how different models perform on Apple Silicon in real time, comparing speed, quality, and resource consumption across models.</p>

<h3>5. Multimodal content processing</h3>
<p>Nativ supports text, image, video summarization, and voice transcription. You can use it to:</p>
<ul>
<li>Caption images</li>
<li>Summarize videos</li>
<li>Auto-complete code</li>
<li>Transcribe and generate speech</li>
</ul>

<h2>Known Limitations</h2>

<ol>
<li><strong>Apple Silicon only:</strong> Nativ only supports M1/M2/M3/M4 Macs. Intel Macs cannot run it.</li>
<li><strong>macOS 26+ required:</strong> Needs a relatively recent macOS version (Sequoia or newer).</li>
<li><strong>Model size limited by memory:</strong> You can only run models that fit in your Mac's unified memory. A 16GB Mac can comfortably run ~10GB models.</li>
<li><strong>Inference speed vs. cloud GPUs:</strong> While Apple Silicon's MLX optimization is excellent, large models still run slower than on cloud A100/H100 GPUs.</li>
<li><strong>Dedicated audio/image-generation models coming soon:</strong> Specialized audio-only and image-generation-only models are planned for future versions.</li>
</ol>

<h2>Frequently Asked Questions</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: Is Nativ really completely free? Are there hidden costs?</div>
<div class="faq-a">Yes. Nativ is MIT-licensed and completely free with no subscription fees, no in-app purchases, and no hidden charges. The models themselves are also open-source and free (e.g., the Gemma series from Google). The only potential cost is accessing certain proprietary models on Hugging Face, which is not a Nativ limitation.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: I have a Mac M1 with 16GB RAM. Which models can I run?</div>
<div class="faq-a">A 16GB unified memory M1 Mac can comfortably run ~10GB models like Gemma 4 E2B Instruct (10.28 GB). The 3.2 GB LFM2.5-VL model runs on any Apple Silicon Mac. Nativ automatically recommends models suited to your hardware.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Does Nativ support Chinese language?</div>
<div class="faq-a">Nativ itself has an English UI, but the models it runs (like Gemma) support multilingual input and output, including Chinese. You can converse with the model in Chinese, and it will respond in Chinese.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Can I use Nativ on Windows or Linux?</div>
<div class="faq-a">No. Nativ is built specifically for macOS and Apple Silicon, relying on the MLX framework and Apple's unified memory architecture. Windows/Linux users should consider Ollama or other cross-platform alternatives.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: How does Nativ guarantee my data won't leak?</div>
<div class="faq-a">All inference runs locally — no data is sent to the cloud. The API server binds to localhost (127.0.0.1), making it inaccessible from external devices. If you enable a server API key, you can further protect management endpoints. The source code is open-source and auditable by anyone.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: How do I update Nativ?</div>
<div class="faq-a">Nativ uses the Sparkle framework for in-app automatic updates. On launch, it checks for new versions and prompts you to download updates.</div>
</div>
</div>

<h2>Conclusion</h2>

<p>Nativ represents a new direction in AI tools: <strong>bringing intelligence back to your device</strong>. It's not a feature-limited trial, nor is it a "free tier + paywall" model — it's a complete, feature-rich, 100% open-source local AI workspace.</p>

<p>If you have an Apple Silicon Mac and you're tired of paying subscriptions for various AI services, worried about data privacy, or want to use AI in offline environments, Nativ is currently one of the best options available. It's completely free, open-source and auditable, supports multiple models and modalities, and can even serve as a backend server for coding agents.</p>

<p>Download now and experience true local AI: <a href="https://github.com/Blaizzy/nativ/releases/latest">Visit Nativ GitHub Releases</a></p>
"""
    
    faq_zh = """{"@type":"Question","name":"Nativ 真的完全免费吗？有没有隐藏费用？","acceptedAnswer":{"@type":"Answer","text":"是的，Nativ 采用 MIT 许可证完全免费，无任何订阅费用、无内购、无隐藏收费。模型本身也是开源免费的（如 Gemma 系列来自 Google）。唯一可能需要付费的是你从 Hugging Face 下载某些专有模型的权限，但这不是 Nativ 的限制。"}},{"@type":"Question","name":"我的 Mac 是 M1 16GB，可以运行哪些模型？","acceptedAnswer":{"@type":"Answer","text":"16GB 统一内存的 M1 Mac 可以流畅运行 10GB 左右的模型，如 Gemma 4 E2B Instruct（10.28 GB）。3.2 GB 的 LFM2.5-VL 模型在任何 Apple Silicon Mac 上都能运行。Nativ 会根据你的硬件自动推荐合适的模型。"}},{"@type":"Question","name":"Nativ 支持中文吗？","acceptedAnswer":{"@type":"Answer","text":"Nativ 本身是英文界面，但它运行的模型（如 Gemma）支持多语言输入输出，包括中文。你可以用中文与模型对话，模型会以中文回复。"}},{"@type":"Question","name":"我可以在 Windows 或 Linux 上使用 Nativ 吗？","acceptedAnswer":{"@type":"Answer","text":"不可以。Nativ 是专为 macOS 和 Apple Silicon 构建的原生应用，依赖于 MLX 框架和 Apple 的统一内存架构。Windows/Linux 用户可以考虑 Ollama 或其他跨平台替代方案。"}},{"@type":"Question","name":"Nativ 如何保证我的数据不会被泄露？","acceptedAnswer":{"@type":"Answer","text":"Nativ 的所有推理都在本地完成，不发送任何数据到云端。API 服务器绑定在 localhost (127.0.0.1)，外部设备无法访问。如果你启用了服务器 API Key，还可以进一步保护管理端点。源代码是开源的，任何人都可以审计。"}}"""
    
    faq_en = """{"@type":"Question","name":"Is Nativ really completely free? Are there hidden costs?","acceptedAnswer":{"@type":"Answer","text":"Yes. Nativ is MIT-licensed and completely free with no subscription fees, no in-app purchases, and no hidden charges. The models themselves are also open-source and free (e.g., the Gemma series from Google). The only potential cost is accessing certain proprietary models on Hugging Face, which is not a Nativ limitation."}},{"@type":"Question","name":"I have a Mac M1 with 16GB RAM. Which models can I run?","acceptedAnswer":{"@type":"Answer","text":"A 16GB unified memory M1 Mac can comfortably run ~10GB models like Gemma 4 E2B Instruct (10.28 GB). The 3.2 GB LFM2.5-VL model runs on any Apple Silicon Mac. Nativ automatically recommends models suited to your hardware."}},{"@type":"Question","name":"Does Nativ support Chinese language?","acceptedAnswer":{"@type":"Answer","text":"Nativ itself has an English UI, but the models it runs (like Gemma) support multilingual input and output, including Chinese. You can converse with the model in Chinese, and it will respond in Chinese."}},{"@type":"Question","name":"Can I use Nativ on Windows or Linux?","acceptedAnswer":{"@type":"Answer","text":"No. Nativ is built specifically for macOS and Apple Silicon, relying on the MLX framework and Apple's unified memory architecture. Windows/Linux users should consider Ollama or other cross-platform alternatives."}},{"@type":"Question","name":"How does Nativ guarantee my data won't leak?","acceptedAnswer":{"@type":"Answer","text":"All inference runs locally — no data is sent to the cloud. The API server binds to localhost (127.0.0.1), making it inaccessible from external devices. If you enable a server API key, you can further protect management endpoints. The source code is open-source and auditable by anyone."}}"""
    
    # Import and use the HTML generator from write_guide
    sys.path.insert(0, '/home/ubuntu/aifreeplan/scripts')
    from write_guide import generate_guide_html
    
    zh_html, en_html = generate_guide_html(
        slug, title_zh, title_en, desc_zh, desc_en,
        content_zh, content_en, faq_zh, faq_en, today
    )
    
    os.makedirs('/home/ubuntu/aifreeplan/zh/guides', exist_ok=True)
    os.makedirs('/home/ubuntu/aifreeplan/en/guides', exist_ok=True)
    
    with open(f'/home/ubuntu/aifreeplan/zh/guides/{slug}.html', 'w', encoding='utf-8') as f:
        f.write(zh_html)
    
    with open(f'/home/ubuntu/aifreeplan/en/guides/{slug}.html', 'w', encoding='utf-8') as f:
        f.write(en_html)
    
    print(f"✅ Generated guide: {slug}")
    print(f"   Date: {today}")
    print(f"   Title (ZH): {title_zh}")
    print(f"   Title (EN): {title_en}")
    
    # Count characters
    zh_char_count = len(content_zh.encode('utf-8'))
    en_char_count = len(content_en.encode('utf-8'))
    print(f"   Content length (ZH): {zh_char_count} bytes")
    print(f"   Content length (EN): {en_char_count} bytes")
    
    # Count actual Chinese characters in EN content
    import re
    cn_chars_in_en = len(re.findall(r'[\u4e00-\u9fff]', content_en))
    total_chars_en = len(content_en)
    cn_ratio = (cn_chars_in_en / total_chars_en * 100) if total_chars_en > 0 else 0
    print(f"   Chinese chars in EN content: {cn_chars_in_en}/{total_chars_en} ({cn_ratio:.1f}%)")

if __name__ == '__main__':
    main()
