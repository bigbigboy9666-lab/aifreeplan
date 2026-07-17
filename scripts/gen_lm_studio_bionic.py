#!/usr/bin/env python3
"""Generate LM Studio Bionic guide with full content."""
import json, os, re

slug = "lm-studio-bionic-free-ai-desktop-agent-2026"
date_pub = "2026-07-17"

title_zh = "LM Studio Bionic免费AI桌面代理：本地运行LLM、离线语音转录、ZDR网络搜索，$0永久免费"
title_en = "LM Studio Bionic Free AI Desktop Agent: Run Local LLMs, Offline Voice Transcription, ZDR Web Search — Forever Free at $0"

desc_zh = "LM Studio Bionic是LM Studio于2026年7月推出的全新AI桌面代理，完全免费($0)。支持本地运行Llama、Qwen、GLM等开源大模型，内置离线语音转录(Voxtral)、零数据保留(ZDR)网络搜索，以及LM Link跨设备同步功能。"
desc_en = "LM Studio Bionic is a completely free ($0) AI desktop agent launched in July 2026. Run local LLMs, offline voice transcription, zero-data-retention web search, and cross-device sync. No API key needed."

content_zh = r"""<h1>LM Studio Bionic免费使用攻略：2026年最新本地AI代理完全指南</h1>

<p>LM Studio在2026年7月16日正式推出了<strong>Bionic</strong>——一个全新的AI桌面代理应用，主打<strong>本地运行开源大模型</strong>，完全免费($0)，无需任何API Key或订阅。这是目前市面上最完整的本地AI工作流解决方案之一。</p>

<h2>一、LM Studio Bionic是什么？</h2>

<p>LM Studio是一款知名的本地大模型运行工具，之前主要提供模型下载、聊天界面和本地REST API服务。2026年7月，LM Studio团队将产品升级为了<strong>"Bionic"</strong>——一个集成了AI代理能力的桌面应用。</p>

<p>Bionic的核心定位是：<strong>"专为开源模型打造的AI代理，用于完成实际工作"</strong>。它支持编程、研究、文档处理等多种场景，可以在本地运行模型，也可以切换到云端开源模型来处理更重的任务。</p>

<h2>二、免费功能详解（$0永久免费）</h2>

<p>LM Studio Bionic的免费版包含以下功能，<strong>没有任何使用次数限制</strong>：</p>

<ul>
<li><strong>Bionic Agent（AI代理）</strong>：支持代码编写、文档处理、网页搜索等任务</li>
<li><strong>本地LLM运行</strong>：使用llama.cpp和MLX引擎运行最新的开源大模型，包括Llama、Qwen、GLM、DeepSeek等系列</li>
<li><strong>离线语音转录</strong>：内置Voxtral语音模型（由Mistral AI提供），支持多语言实时语音转文字，完全离线运行</li>
<li><strong>ZDR网络搜索</strong>：零数据保留(Zero Data Retention)的网页搜索工具，搜索结果不会上传到任何服务器</li>
<li><strong>LM Link跨设备同步</strong>：最多支持5台设备之间的模型和工作流同步</li>
</ul>

<p>所有上述功能<strong>永久免费</strong>，不需要注册付费账号，不需要信用卡，不需要任何付费计划。</p>

<h2>三、云推理选项（按需付费）</h2>

<p>如果你需要运行超出本地硬件能力的更大模型，Bionic还提供了<strong>按量付费的云推理</strong>选项：</p>

<ul>
<li><strong>可用模型</strong>：GLM 5.2、Kimi K2.6、Kimi Code K2.7（更多模型即将推出）</li>
<li><strong>计费方式</strong>：购买云积分(Credits)，按量使用</li>
<li><strong>数据安全</strong>：所有云服务均在美国境内运行，默认启用零数据保留(ZDR)</li>
<li><strong>Bionic Pass</strong>：订阅制计划即将推出，目前尚未公布价格和细节</li>
</ul>

<p><strong>注意</strong>：云推理是可选的，本地运行功能完全免费且无需联网。</p>

<h2>四、支持的模型和平台</h2>

<h3>支持的模型格式</h3>
<ul>
<li><strong>GGUF格式</strong>：通过llama.cpp运行时支持，适用于Windows和Linux</li>
<li><strong>MLX格式</strong>：适用于Apple Silicon Mac（M1/M2/M3/M4芯片）</li>
</ul>

<h3>支持的操作系统</h3>
<ul>
<li><strong>macOS</strong>：支持Intel和Apple Silicon（ARM64）架构，当前最新版本0.4.19</li>
<li><strong>Windows</strong>：支持x64和ARM64架构</li>
<li><strong>Linux</strong>：支持x64和ARM64架构，提供AppImage和DEB两种安装包</li>
</ul>

<h2>五、核心功能深度介绍</h2>

<h3>1. Bionic Agent（AI代理）</h3>
<p>Bionic的AI代理功能可以：</p>
<ul>
<li><strong>代码工作</strong>：查看本地代码库、解释不熟悉代码、帮助调试和修改。创建Code项目指向本地文件夹，Bionic可以逐步审查和编辑代码变更，内联diff让每次代码修改一目了然</li>
<li><strong>文档处理</strong>：支持PDF、DOCX、PPTX、Excel等文件格式。在工作项目中沙盒环境处理文档，自动保存检查点，可随时回滚修改</li>
<li><strong>原生网页搜索</strong>：通过ZDR模式进行网络搜索，获取最新信息</li>
</ul>

<h3>2. 离线语音转录</h3>
<p>Bionic内置了<strong>Voxtral</strong>语音模型（由Mistral AI开发的先进多语言实时转录模型）。你可以：</p>
<ul>
<li>在任何应用中唤起语音键盘进行语音输入</li>
<li>所有转录过程完全在本地设备上进行，不上传任何音频数据</li>
<li>支持多语言识别</li>
<li>适合隐私敏感场景，如医疗、法律、金融等领域的语音记录</li>
</ul>

<h3>3. LM Link（跨设备同步）</h3>
<p>免费版最多支持<strong>5台设备</strong>通过LM Link同步模型和工作流配置。这对于拥有多台电脑的用户非常实用——你可以在Mac上下载模型，然后在Windows电脑上直接使用相同的模型。</p>

<h2>六、与竞品的对比</h2>

<table>
<thead>
<tr><th>功能</th><th>LM Studio Bionic</th><th>Ollama</th><th>Jan</th></tr>
</thead>
<tbody>
<tr><td>本地运行LLM</td><td>✅</td><td>✅</td><td>✅</td></tr>
<tr><td>AI代理功能</td><td>✅ 内置</td><td>❌ 需额外配置</td><td>❌ 基础</td></tr>
<tr><td>离线语音转录</td><td>✅ Voxtral模型</td><td>❌</td><td>❌</td></tr>
<tr><td>网络搜索</td><td>✅ ZDR模式</td><td>❌</td><td>❌</td></tr>
<tr><td>跨平台</td><td>macOS/Win/Linux</td><td>macOS/Win/Linux</td><td>macOS/Win/Linux</td></tr>
<tr><td>价格</td><td><strong>$0免费</strong></td><td><strong>$0免费</strong></td><td><strong>$0免费</strong></td></tr>
<tr><td>云推理</td><td>✅ 按量付费</td><td>❌</td><td>❌</td></tr>
</tbody>
</table>

<h2>七、安装步骤</h2>

<ol>
<li><strong>访问官网</strong>：打开 <a href="https://lmstudio.ai/download" target="_blank">lmstudio.ai/download</a></li>
<li><strong>选择平台</strong>：根据你的操作系统选择Windows、Mac或Linux版本</li>
<li><strong>下载安装包</strong>：Windows提供.exe安装程序，Mac提供.dmg文件，Linux提供AppImage和.deb包</li>
<li><strong>安装并启动</strong>：安装完成后打开应用</li>
<li><strong>下载模型</strong>：在应用内搜索并下载你需要的开源模型（推荐从llama.cpp的GGUF格式或MLX格式中选择）</li>
<li><strong>开始使用</strong>：选择模型后即可开始对话、编写代码或处理文档</li>
</ol>

<h2>八、常见问题</h2>

<h3>Q: LM Studio Bionic真的完全免费吗？</h3>
<p>A: 是的。本地运行LLM、AI代理、离线语音转录、ZDR网络搜索、LM Link（5台设备）全部永久免费，$0费用，无任何隐藏收费。云推理是按量付费的可选功能。</p>

<h3>Q: 需要联网才能使用吗？</h3>
<p>A: 不需要。所有核心功能（模型运行、语音转录、AI代理）均可完全离线运行。只有ZDR网络搜索和云推理需要网络连接。</p>

<h3>Q: 对硬件有什么要求？</h3>
<p>A: 硬件需求取决于你选择的模型大小。较小的模型（7B-13B参数）可以在大多数现代电脑上流畅运行；较大的模型（70B+）需要至少32GB内存或配备高显存的专业显卡。Apple Silicon Mac建议使用M1及以上芯片以获得最佳性能。</p>

<h3>Q: 支持哪些模型？</h3>
<p>A: 支持所有主流的开源模型，包括但不限于Llama系列、Qwen系列、GLM系列、DeepSeek系列、Mistral系列等。模型以GGUF（llama.cpp）或MLX格式提供。</p>

<h3>Q: 我的数据会被上传吗？</h3>
<p>A: LM Studio承诺<strong>零数据保留(Zero Data Retention)</strong>，你的对话内容和模型使用数据不会上传到任何服务器。即使使用云服务，也默认启用ZDR。</p>

<h2>九、总结</h2>

<p>LM Studio Bionic是目前<strong>功能最全面的免费本地AI桌面代理</strong>。$0永久免费的定价策略，加上本地LLM运行、离线语音转录、ZDR网络搜索、AI代理等丰富功能，使其成为追求隐私保护和离线使用的用户的理想选择。</p>

<p>无论你是开发者（本地代码辅助）、研究者（文档分析）、还是普通用户（语音输入、日常问答），LM Studio Bionic都能满足需求，且<strong>完全免费、无需联网、保护隐私</strong>。</p>

<p><strong>立即下载</strong>：<a href="https://lmstudio.ai/download" target="_blank">lmstudio.ai/download</a></p>
"""

content_en = r"""<h1>LM Studio Bionic Free AI Desktop Agent Guide 2026: Local LLMs, Offline Voice, ZDR Search — $0 Forever</h1>

<p>LM Studio officially launched <strong>Bionic</strong> on July 16, 2026 — a brand new AI desktop agent application that runs open-source large language models <strong>locally on your machine</strong>, completely free ($0), with no API keys or subscriptions required. This is one of the most comprehensive local AI workflow solutions available today.</p>

<h2>1. What is LM Studio Bionic?</h2>

<p>LM Studio is a well-known tool for running local large language models, previously offering model downloads, a chat interface, and a local REST API. In July 2026, the LM Studio team upgraded the product to <strong>"Bionic"</strong> — a desktop application that integrates AI agent capabilities.</p>

<p>Bionic's core positioning is: <strong>"The AI agent made for open models, built to get things done."</strong> It supports coding, research, document processing, and more, running models locally or switching to cloud-based open-source models for heavier tasks.</p>

<h2>2. Free Features Breakdown ($0 Forever)</h2>

<p>LM Studio Bionic's free tier includes the following features with <strong>no usage limits whatsoever</strong>:</p>

<ul>
<li><strong>Bionic Agent</strong>: AI agent supporting coding, document processing, and web search tasks</li>
<li><strong>Local LLM Execution</strong>: Run the latest open-source models using llama.cpp and MLX engines, including Llama, Qwen, GLM, DeepSeek, and more</li>
<li><strong>Offline Voice Transcription</strong>: Built-in Voxtral speech model (provided by Mistral AI) for multilingual real-time speech-to-text, running entirely offline</li>
<li><strong>ZDR Web Search</strong>: Zero Data Retention web search — search results are never uploaded to any server</li>
<li><strong>LM Link Cross-Device Sync</strong>: Sync models and workflows across up to 5 devices</li>
</ul>

<p>All of the above features are <strong>permanently free</strong>. No paid account registration, no credit card, no subscription plans required.</p>

<h2>3. Cloud Inference Options (Pay-as-You-Go)</h2>

<p>If you need to run larger models beyond your local hardware capabilities, Bionic also offers <strong>pay-as-you-go cloud inference</strong>:</p>

<ul>
<li><strong>Available Models</strong>: GLM 5.2, Kimi K2.6, Kimi Code K2.7 (more coming soon)</li>
<li><strong>Billing</strong>: Buy cloud credits, pay only for what you use</li>
<li><strong>Data Security</strong>: All cloud services operate within the US with Zero Data Retention (ZDR) enabled by default</li>
<li><strong>Bionic Pass</strong>: A subscription plan is coming soon — pricing and details not yet announced</li>
</ul>

<p><strong>Note</strong>: Cloud inference is entirely optional. The local running features are completely free and require no internet connection.</p>

<h2>4. Supported Models and Platforms</h2>

<h3>Supported Model Formats</h3>
<ul>
<li><strong>GGUF format</strong>: Supported via llama.cpp runtime, available for Windows and Linux</li>
<li><strong>MLX format</strong>: Available for Apple Silicon Macs (M1/M2/M3/M4 chips)</li>
</ul>

<h3>Supported Operating Systems</h3>
<ul>
<li><strong>macOS</strong>: Intel and Apple Silicon (ARM64), current latest version 0.4.19</li>
<li><strong>Windows</strong>: x64 and ARM64 architectures</li>
<li><strong>Linux</strong>: x64 and ARM64, available as AppImage and DEB packages</li>
</ul>

<h2>5. Core Features Deep Dive</h2>

<h3>1. Bionic Agent (AI Agent)</h3>
<p>Bionic's AI agent can:</p>
<ul>
<li><strong>Coding</strong>: Inspect local codebases, explain unfamiliar code, help debug and edit. Create a Code project pointing to a local folder, and Bionic will review and edit code changes with inline diffs for easy inspection</li>
<li><strong>Document Processing</strong>: Supports PDF, DOCX, PPTX, Excel formats. Documents are processed in a sandboxed Work project environment with automatic checkpoints for safe review and rollback</li>
<li><strong>Native Web Search</strong>: Perform web searches in ZDR mode to get the latest information</li>
</ul>

<h3>2. Offline Voice Transcription</h3>
<p>Bionic includes the <strong>Voxtral</strong> speech model (an advanced multilingual real-time transcription model developed by Mistral AI). You can:</p>
<ul>
<li>Invoke the voice keyboard in any app for voice input</li>
<li>All transcription happens entirely on your local device — no audio data is ever uploaded</li>
<li>Supports multilingual recognition</li>
<li>Ideal for privacy-sensitive scenarios like healthcare, legal, and financial voice recording</li>
</ul>

<h3>3. LM Link (Cross-Device Sync)</h3>
<p>The free tier supports syncing models and workflow configurations across up to <strong>5 devices</strong> via LM Link. This is extremely useful for users with multiple computers — download a model on your Mac and use the exact same model on your Windows PC.</p>

<h2>6. Comparison with Competitors</h2>

<table>
<thead>
<tr><th>Feature</th><th>LM Studio Bionic</th><th>Ollama</th><th>Jan</th></tr>
</thead>
<tbody>
<tr><td>Local LLM Execution</td><td>✅</td><td>✅</td><td>✅</td></tr>
<tr><td>AI Agent</td><td>✅ Built-in</td><td>❌ Requires extra config</td><td>❌ Basic</td></tr>
<tr><td>Offline Voice Transcription</td><td>✅ Voxtral model</td><td>❌</td><td>❌</td></tr>
<tr><td>Web Search</td><td>✅ ZDR mode</td><td>❌</td><td>❌</td></tr>
<tr><td>Cross-Platform</td><td>macOS/Win/Linux</td><td>macOS/Win/Linux</td><td>macOS/Win/Linux</td></tr>
<tr><td>Price</td><td><strong>$0 Free</strong></td><td><strong>$0 Free</strong></td><td><strong>$0 Free</strong></td></tr>
<tr><td>Cloud Inference</td><td>✅ Pay-as-you-go</td><td>❌</td><td>❌</td></tr>
</tbody>
</table>

<h2>7. Installation Steps</h2>

<ol>
<li><strong>Visit the website</strong>: Go to <a href="https://lmstudio.ai/download" target="_blank">lmstudio.ai/download</a></li>
<li><strong>Select your platform</strong>: Choose the Windows, Mac, or Linux version based on your operating system</li>
<li><strong>Download the installer</strong>: Windows provides an .exe installer, Mac provides a .dmg file, Linux provides AppImage and .deb packages</li>
<li><strong>Install and launch</strong>: Open the application after installation</li>
<li><strong>Download a model</strong>: Search and download the open-source model you need within the app (recommended: choose from llama.cpp GGUF format or MLX format)</li>
<li><strong>Start using</strong>: Select a model and begin chatting, coding, or processing documents</li>
</ol>

<h2>8. Frequently Asked Questions</h2>

<h3>Q: Is LM Studio Bionic really completely free?</h3>
<p>A: Yes. Local LLM execution, AI agent, offline voice transcription, ZDR web search, and LM Link (5 devices) are all permanently free at $0 with absolutely no hidden charges. Cloud inference is an optional pay-as-you-go feature.</p>

<h3>Q: Do I need an internet connection to use it?</h3>
<p>A: No. All core features (model execution, voice transcription, AI agent) work completely offline. Only ZDR web search and cloud inference require an internet connection.</p>

<h3>Q: What are the hardware requirements?</h3>
<p>A: Hardware needs depend on the model size you choose. Smaller models (7B–13B parameters) run smoothly on most modern computers. Larger models (70B+) require at least 32GB RAM or a professional GPU with high VRAM. Apple Silicon Macs with M1 or newer are recommended for the best performance.</p>

<h3>Q: Which models are supported?</h3>
<p>A: All major open-source models are supported, including but not limited to the Llama series, Qwen series, GLM series, DeepSeek series, and Mistral series. Models are available in GGUF (llama.cpp) or MLX formats.</p>

<h3>Q: Will my data be uploaded anywhere?</h3>
<p>A: LM Studio commits to <strong>Zero Data Retention (ZDR)</strong>. Your conversations and model usage data are never uploaded to any server. Even when using cloud services, ZDR is enabled by default.</p>

<h2>9. Summary</h2>

<p>LM Studio Bionic is currently the <strong>most feature-rich free local AI desktop agent</strong> on the market. Its $0 forever-free pricing, combined with local LLM execution, offline voice transcription, ZDR web search, and AI agent capabilities, makes it an ideal choice for users who value privacy protection and offline operation.</p>

<p>Whether you're a developer (local code assistance), a researcher (document analysis), or an everyday user (voice input, daily Q&A), LM Studio Bionic meets your needs with <strong>complete free access, no internet required, and full privacy protection</strong>.</p>

<p><strong>Download now</strong>: <a href="https://lmstudio.ai/download" target="_blank">lmstudio.ai/download</a></p>
"""

# Build HTML templates
def build_html(lang, title, desc, content, slug, dpub):
    zh_part = lang == 'zh'
    nav_a_zh = '<a href="/zh/all">全部工具</a><a href="/zh/guides">攻略</a><a href="/zh/privacy">隐私</a>'
    nav_a_en = '<a href="/en/all">All Tools</a><a href="/en/guides">Guides</a><a href="/en/privacy">Privacy</a>'
    lang_link = f'/en/guides/{slug}' if zh_part else f'/zh/guides/{slug}'
    lang_btn = 'English' if zh_part else '中文'
    bc_home = '/zh' if zh_part else '/en'
    bc_label = '首页' if zh_part else 'Home'
    bc_sec = '/zh/guides' if zh_part else '/en/guides'
    bc_sec_label = '攻略' if zh_part else 'Guides'
    base_url = '/' + ('zh' if zh_part else 'en')
    ld_url = f'https://aifreeplan.com/zh/guides/{slug}' if zh_part else f'https://aifreeplan.com/en/guides/{slug}'
    locale = 'zh_CN' if zh_part else 'en_US'

    css = """*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#F8FAFC;--bg-white:#fff;--border:#E2E8F0;--border-light:#F1F5F9;--text:#1E1B4B;--text-secondary:#64748B;--text-muted:#94A3B8;--accent:#6366F1;--accent-hover:#4F46E5;--accent-light:rgba(99,102,241,.1);--green:#059669;--green-light:rgba(5,150,105,.1);--shadow:0 4px 20px rgba(0,0,0,.05);--radius:12px}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Noto Sans SC","PingFang SC","Microsoft YaHei",sans-serif;background:var(--bg);color:var(--text);line-height:1.6}
.container{max-width:1280px;margin:0 auto;padding:0 40px}
.header{background:var(--bg-white);border-bottom:1px solid var(--border);position:sticky;top:0;z-index:100}
.header-inner{display:flex;align-items:center;justify-content:space-between;height:72px}
.logo{display:flex;align-items:center;gap:8px;text-decoration:none;color:var(--text);font-size:24px;font-weight:700}
.logo .accent{color:var(--accent)}
.nav{display:flex;gap:32px;align-items:center}
.nav a{color:var(--text);text-decoration:none;font-size:15px;font-weight:500;transition:color .2s}
.nav a:hover{color:var(--accent)}
.btn{display:inline-flex;align-items:center;justify-content:center;padding:10px 22px;border-radius:8px;font-size:15px;font-weight:600;cursor:pointer;border:none;transition:all .2s;text-decoration:none}
.btn-primary{background:var(--accent);color:#fff}
.btn-primary:hover{background:var(--accent-hover)}
.article-container{max-width:800px;margin:0 auto;padding:40px 20px 80px}
.article-container h1{font-size:36px;font-weight:700;margin-bottom:16px;line-height:1.3}
.article-container h2{font-size:24px;font-weight:700;margin-top:40px;margin-bottom:16px;padding-top:24px;border-top:1px solid var(--border)}
.article-container h3{font-size:20px;font-weight:600;margin-top:32px;margin-bottom:12px}
.article-container p{margin-bottom:16px;color:var(--text-secondary);line-height:1.8}
.article-container ul,.article-container ol{margin-bottom:16px;padding-left:24px;color:var(--text-secondary)}
.article-container li{margin-bottom:8px;line-height:1.6}
.article-container img{max-width:100%;height:auto;border-radius:12px;margin:24px 0;box-shadow:var(--shadow)}
.article-container a{color:var(--accent);text-decoration:underline}
.article-container table{width:100%;border-collapse:collapse;margin:20px 0;font-size:14px}
.article-container th,.article-container td{padding:12px;border:1px solid var(--border);text-align:left}
.article-container th{background:var(--accent-light);font-weight:600}
.breadcrumb{font-size:14px;color:var(--text-muted);margin-bottom:24px}
.breadcrumb a{color:var(--text-muted);text-decoration:none}
.breadcrumb a:hover{color:var(--accent)}
.breadcrumb-sep{margin:0 8px}
.footer{background:#1a1a2e;padding:50px 0 30px;color:#fff;margin-top:60px}
.footer-inner{display:flex;justify-content:space-between;gap:60px;flex-wrap:wrap}
.footer-brand{max-width:300px}
.footer-brand p{font-size:14px;color:rgba(255,255,255,.6)}
.footer-links{display:flex;gap:60px}
.footer-col{display:flex;flex-direction:column;gap:10px}
.footer-col h4{font-size:14px;font-weight:700;color:#fff}
.footer-col a{color:rgba(255,255,255,.6);text-decoration:none;font-size:14px}
.footer-col a:hover{color:#fff}
.footer-bottom{margin-top:30px;padding-top:20px;border-top:1px solid rgba(255,255,255,.1);font-size:13px;color:rgba(255,255,255,.4)}
@media(max-width:768px){.article-container{padding:16px 16px 48px;max-width:100%}.article-container h1{font-size:24px}.article-container h2{font-size:20px}.container{padding:0 16px}.nav{display:none}}}"""

    nav_items = nav_a_zh if zh_part else nav_a_en
    product_label = '全部工具' if zh_part else 'All Tools'
    guides_label = '攻略' if zh_part else 'Guides'
    privacy_label = '隐私' if zh_part else 'Privacy'

    html_parts = [
        '<!DOCTYPE html>',
        f'<html lang="{lang}">',
        '<head>',
        '<meta charset="UTF-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        f'<title>{title} | AIFreePlan</title>',
        '<meta property="og:type" content="article">',
        f'<meta property="og:title" content="{title} | AIFreePlan">',
        f'<meta property="og:description" content="{desc}">',
        f'<meta property="og:url" content="{ld_url}">',
        '<meta property="og:site_name" content="AIFreePlan">',
        f'<meta property="og:locale" content="{locale}">',
        '<meta property="og:image" content="https://aifreeplan.com/og-image.png">',
        '<meta name="twitter:image" content="https://aifreeplan.com/og-image.png">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{title} | AIFreePlan">',
        f'<meta name="twitter:description" content="{desc}">',
        f'<meta name="description" content="{desc}">',
        '<link rel="icon" type="image/svg+xml" href="/favicon.svg">',
        '<meta name="theme-color" content="#6366F1">',
        f'<link rel="canonical" href="{ld_url}">',
        f'<link rel="alternate" hreflang="zh" href="https://aifreeplan.com/zh/guides/{slug}">',
        f'<link rel="alternate" hreflang="en" href="https://aifreeplan.com/en/guides/{slug}">',
        f'<link rel="alternate" hreflang="x-default" href="https://aifreeplan.com/en/guides/{slug}">',
        '<style>',
        css,
        '</style>',
        '<script type="application/ld+json">',
        '{"@context":"https://schema.org","@type":"Article","headline":"' + re.sub(r'"', '\\"', title) + '","description":"' + re.sub(r'"', '\\"', desc) + '","url":"' + ld_url + '","datePublished":"' + dpub + '","dateModified":"' + dpub + '","author":{"@type":"Organization","name":"AIFreePlan"},"publisher":{"@type":"Organization","name":"AIFreePlan","url":"https://aifreeplan.com"},"mainEntityOfPage":{"@type":"WebPage","@id":"' + ld_url + '"}}',
        '</script>',
        '<script type="application/ld+json">',
        '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"' + bc_label + '","item":"' + bc_home + '"},{"@type":"ListItem","position":2,"name":"' + bc_sec_label + '","item":"' + bc_sec + '"},{"@type":"ListItem","position":3,"name":"' + re.sub(r'"', '\\"', title) + '","item":"' + ld_url + '"}]}',
        '</script>',
        '</head>',
        '<body>',
        '<header class="header">',
        '  <div class="container header-inner">',
        '    <a href="' + base_url + '" class="logo">AI<span class="accent">FreePlan</span></a>',
        '    <nav class="nav">',
        '      ' + nav_items,
        '      <a href="' + lang_link + '" class="btn btn-primary">' + lang_btn + '</a>',
        '    </nav>',
        '  </div>',
        '</header>',
        '<main class="article-container">',
        '<nav class="breadcrumb"><a href="' + bc_home + '">' + bc_label + '</a> <span class="breadcrumb-sep">›</span> <a href="' + bc_sec + '">' + bc_sec_label + '</a> <span class="breadcrumb-sep">›</span> <span>' + title + '</span></nav>',
        content,
        '</main>',
        '<footer class="footer">',
        '  <div class="container footer-inner">',
        '    <div class="footer-brand"><a href="' + base_url + '" class="logo" style="color:#059669">AI<span class="accent" style="color:#6366F1">FreePlan</span></a><p>AI-powered free tools aggregator. Free forever.</p></div>',
        '    <div class="footer-links">',
        '      <div class="footer-col"><h4>Product</h4><a href="' + base_url + '">All Tools</a><a href="' + base_url + '">Guides</a></div>',
        '      <div class="footer-col"><h4>Legal</h4><a href="' + base_url + '">Privacy</a><a href="' + base_url + '">Terms</a></div>',
        '    </div>',
        '  </div>',
        '  <div class="container footer-bottom">&copy; 2026 AIFreePlan. All rights reserved.</div>',
        '</footer>',
        '</body></html>',
    ]
    return '\n'.join(html_parts)


# Write files
os.makedirs('/home/ubuntu/aifreeplan/zh/guides', exist_ok=True)
os.makedirs('/home/ubuntu/aifreeplan/en/guides', exist_ok=True)

base = '/home/ubuntu/aifreeplan'
zh_html = build_html('zh', title_zh, desc_zh, content_zh, slug, date_pub)
en_html = build_html('en', title_en, desc_en, content_en, slug, date_pub)

with open(f'{base}/zh/guides/{slug}.html', 'w', encoding='utf-8') as f:
    f.write(zh_html)
with open(f'{base}/en/guides/{slug}.html', 'w', encoding='utf-8') as f:
    f.write(en_html)

# Validate
cn_in_en = sum(1 for c in content_en if '\u4e00' <= c <= '\u9fff')
ratio = (cn_in_en / len(content_en) * 100) if len(content_en) > 0 else 0
print(f"Zh: {len(content_zh)} chars | En: {len(content_en)} chars")
print(f"Chinese chars in EN: {cn_in_en}/{len(content_en)} = {ratio:.1f}%")
if len(content_zh) >= 1000 and len(content_en) >= 1000 and ratio < 5:
    print("✅ QUALITY CHECK PASSED")
else:
    print("❌ QUALITY CHECK FAILED")
