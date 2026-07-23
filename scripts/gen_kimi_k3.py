#!/usr/bin/env python3
"""Generate Kimi K3 free tier guide."""
import os
import sys
from datetime import datetime

def main():
    today = datetime.now().strftime('%Y-%m-%d')
    slug = "kimi-k3-free-tier-2026"
    
    title_zh = "Kimi K3 完全免费攻略：月之暗面最强AI模型，1M上下文窗口+2.8万亿参数"
    title_en = "Kimi K3 Free Guide 2026: Moonshot AI's Flagship Model with 1M Context Window"
    desc_zh = "Kimi K3是月之暗面2026年7月发布的旗舰AI模型，2.8万亿参数、100万token上下文窗口。本文详细介绍如何在Kimi网页端和API免费使用K3，以及各定价策略对比。"
    desc_en = "Kimi K3 is Moonshot AI's July 2026 flagship model with 2.8 trillion parameters and 1M token context window. Complete guide to free usage via web and API."
    
    content_zh = """<h1>Kimi K3 完全免费攻略：月之暗面最强AI模型，1M上下文窗口+2.8万亿参数</h1>

<p>2026年7月16日，中国AI公司<strong>月之暗面（Moonshot AI）</strong>正式发布了其最强模型 <strong>Kimi K3</strong>。这是一个2.8万亿参数的混合专家（MoE）模型，拥有100万token的超长上下文窗口，在多个基准测试中达到行业领先水平。</p>

<p>好消息是：Kimi K3 可以通过 <strong>kimi.moonshot.cn</strong> 网页端<strong>免费使用</strong>，也可以通过 API 按量付费使用。下面详细介绍如何使用。</p>

<h2>Kimi K3 核心参数</h2>

<ul>
<li><strong>模型规模：</strong>2.8万亿参数（MoE架构），激活参数远低于此</li>
<li><strong>上下文窗口：</strong>1,000,000 tokens（约200万字）</li>
<li><strong>推理能力：</strong>支持思维链推理（Reasoning），当前仅支持 "max" 推理强度</li>
<li><strong>多模态：</strong>支持图片输入、代码生成、深度研究</li>
<li><strong>工具调用：</strong>支持 Web Search、Python 执行等工具调用</li>
<li><strong>开源计划：</strong>预计2026年7月27日发布开源权重</li>
</ul>

<h2>免费使用方式</h2>

<h3>方式一：Kimi 网页端（完全免费）</h3>

<p>最直接的使用方式是访问 <a href="https://kimi.moonshot.cn" target="_blank">kimi.moonshot.cn</a>，注册后即可免费使用 Kimi K3。网页端的特点：</p>

<ul>
<li><strong>注册方式：</strong>支持手机号注册，也可用微信/支付宝登录</li>
<li><strong>使用限制：</strong>网页端对免费用户有每日使用量限制，但对于日常使用完全足够</li>
<li><strong>功能完整：</strong>网页端提供完整的 K3 能力，包括深度研究、文档分析、代码生成等</li>
<li><strong>无需翻墙：</strong>国内可直接访问</li>
</ul>

<h3>方式二：Kimi API（按量付费，非免费但有竞争力定价）</h3>

<p>如果你需要通过 API 集成 Kimi K3，以下是官方定价（2026年7月数据）：</p>

<table>
<thead>
<tr><th>模型</th><th>缓存命中输入价</th><th>缓存未命中输入价</th><th>输出价</th><th>上下文窗口</th></tr>
</thead>
<tbody>
<tr><td><strong>Kimi K3</strong></td><td><strong>$0.30/百万token</strong></td><td><strong>$3.00/百万token</strong></td><td><strong>$15.00/百万token</strong></td><td>1M tokens</td></tr>
<tr><td>Kimi K2.6</td><td>$0.16/百万token</td><td>$0.95/百万token</td><td>$4.00/百万token</td><td>262K tokens</td></tr>
</tbody>
</table>

<p><strong>关键优势：</strong>Kimi API 的上下文缓存命中率在编码工作负载中超过90%，这意味着大部分输入token都以 $0.30/百万token 的超低价格计费。</p>

<p>作为对比，Anthropic Claude Sonnet 系列的输入价为 $3/百万token、输出价为 $15/百万token。Kimi K3 在同等性能水平下，缓存命中后的输入价格仅为 Claude 的 1/10。</p>

<h2>Kimi K3 的实际能力</h2>

<h3>1. 超长上下文处理</h3>

<p>100万token的上下文窗口意味着你可以一次性上传整本电子书、整个代码仓库或数千页的研究报告，让 K3 进行分析。这在所有大模型中都是顶尖水平。</p>

<h3>2. 深度研究（Deep Research）</h3>

<p>Kimi K3 可以进行多轮递归式深度研究。官方展示的案例包括：</p>
<ul>
<li>通过2800+次网页搜索和1100+次终端数据拉取，分析了87份季度报告和99份原始PDF，生成互动式行业研究报告</li>
<li>通过120+轮递归自我改进，生成了42年AI ASIC产业的互动研究网站</li>
</ul>

<h3>3. 代码生成</h3>

<p>Kimi K3 在代码生成方面表现出色。官方案例包括：</p>
<ul>
<li>使用 Three.js WebGPU 和 GPU 计算，从零构建了一个完整的3D浏览器游戏</li>
<li>生成赛博朋克风格的网页荡绳游戏体验</li>
</ul>

<h3>4. 视觉理解</h3>

<p>K3 支持图片输入，可以进行复杂的视觉分析和理解。在 Simon Willison 的 pelican 测试中，K3 的视觉理解能力获得了高度评价。</p>

<h2>与主要模型的对比</h2>

<table>
<thead>
<tr><th>对比项</th><th>Kimi K3</th><th>Claude Sonnet</th><th>GPT-5.6</th><th>Kimi K2.6</th></tr>
</thead>
<tbody>
<tr><td>参数量</td><td>2.8万亿（MoE）</td><td>未知</td><td>未知</td><td>约1万亿（MoE）</td></tr>
<tr><td>上下文窗口</td><td>1M tokens</td><td>200K tokens</td><td>200K tokens</td><td>262K tokens</td></tr>
<tr><td>API输入价（缓存命中）</td><td>$0.30/百万</td><td>$3.00/百万</td><td>$2.50/百万</td><td>$0.16/百万</td></tr>
<tr><td>API输出价</td><td>$15.00/百万</td><td>$15.00/百万</td><td>$10.40/百万</td><td>$4.00/百万</td></tr>
<tr><td>免费网页端</td><td>✅ 有</td><td>✅ 有</td><td>✅ 有</td><td>✅ 有</td></tr>
<tr><td>思维链推理</td><td>✅ 支持</td><td>✅ 支持</td><td>✅ 支持</td><td>✅ 支持</td></tr>
<tr><td>工具调用</td><td>✅ 支持</td><td>✅ 支持</td><td>✅ 支持</td><td>✅ 支持</td></tr>
<tr><td>开源计划</td><td>2026年7月27日</td><td>否</td><td>否</td><td>已开源</td></tr>
</tbody>
</table>

<h2>如何使用（详细步骤）</h2>

<h3>步骤 1：访问 Kimi 网页版</h3>
<p>打开 <a href="https://kimi.moonshot.cn" target="_blank">kimi.moonshot.cn</a>，使用手机号注册或微信/支付宝登录。</p>

<h3>步骤 2：开始对话</h3>
<p>登录后直接在对话框中输入你的问题。K3 会自动被调用，你不需要手动选择模型。</p>

<h3>步骤 3：使用高级功能</h3>
<ul>
<li><strong>深度研究：</strong>点击"深度研究"按钮，可以让 K3 进行多轮联网搜索和分析</li>
<li><strong>文档分析：</strong>上传PDF、Word、Excel等文件，K3 可以读取并分析其中的内容</li>
<li><strong>代码生成：</strong>直接描述你想要的功能，K3 会生成可运行的代码</li>
</ul>

<h3>步骤 4：通过 API 使用（可选）</h3>
<p>如果需要 API 接入：</p>
<ol>
<li>访问 <a href="https://platform.kimi.ai" target="_blank">platform.kimi.ai</a> 注册 API 账号</li>
<li>创建 API Key</li>
<li>使用模型名 <code>kimi-k3</code> 发起请求</li>
<li>支持自动上下文缓存，编码场景缓存命中率超过90%</li>
</ol>

<h2>常见问题</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: Kimi K3 网页端真的免费吗？</div>
<div class="faq-a">是的，kimi.moonshot.cn 网页端对注册用户免费使用 Kimi K3。虽然可能有每日使用量限制，但对于日常对话、文档分析和代码生成已经完全足够。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Kimi K3 什么时候开源？</div>
<div class="faq-a">月之暗面计划在 2026年7月27日 发布 Kimi K3 的开源权重。这意味着之后任何人都可以下载并在自己的设备上运行。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Kimi K3 和 K2.6 有什么区别？</div>
<div class="faq-a">K3 是 K2.6 的继任者，参数量从约1万亿提升到2.8万亿，上下文窗口从262K扩展到1M，推理能力和多模态理解都有显著提升。API定价也相应提高。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: API 使用 K3 贵吗？</div>
<div class="faq-a">在编码场景中，由于上下文缓存命中率超过90%，输入价格仅为 $0.30/百万token，远低于 Claude Sonnet 的 $3.00/百万token。输出价格 $15.00/百万token 与 Claude Sonnet 持平。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Kimi K3 支持中文吗？</div>
<div class="faq-a">完全支持。Kimi K3 对中文的理解和生成能力是其强项之一，尤其在中文文档分析、中文代码注释等方面表现优异。</div>
</div>
</div>

<h2>总结</h2>

<p>Kimi K3 是 2026 年最值得关注的 AI 模型之一。2.8万亿参数、100万token上下文窗口、深度研究能力、以及极具竞争力的 API 定价，使其成为开发者和普通用户的理想选择。</p>

<p>无论你是想通过网页端免费使用，还是通过 API 集成到自己的应用中，Kimi K3 都是一个值得尝试的选择。立即前往 <a href="https://kimi.moonshot.cn" target="_blank">kimi.moonshot.cn</a> 体验吧！</p>
"""

    content_en = """<h1>Kimi K3 Free Guide 2026: Moonshot AI's Flagship Model with 1M Context Window</h1>

<p>On July 16, 2026, Chinese AI company <strong>Moonshot AI</strong> officially released its most powerful model, <strong>Kimi K3</strong>. This is a 2.8-trillion-parameter Mixture-of-Experts (MoE) model with a 1-million-token context window, achieving industry-leading performance across multiple benchmarks.</p>

<p>The best news: Kimi K3 can be used <strong>for free</strong> via the <strong>kimi.moonshot.cn</strong> web interface, or through the API on a pay-per-use basis with highly competitive pricing. Here's everything you need to know.</p>

<h2>Kimi K3 Core Specifications</h2>

<ul>
<li><strong>Model Size:</strong> 2.8 trillion parameters (MoE architecture)</li>
<li><strong>Context Window:</strong> 1,000,000 tokens (~2 million Chinese characters)</li>
<li><strong>Reasoning:</strong> Chain-of-thought reasoning support, currently with "max" reasoning effort only</li>
<li><strong>Multimodal:</strong> Image input, code generation, deep research capabilities</li>
<li><strong>Tool Calling:</strong> Web Search, Python execution, and more</li>
<li><strong>Open Source:</strong> Weight release expected by July 27, 2026</li>
</ul>

<h2>How to Use for Free</h2>

<h3>Method 1: Kimi Web Interface (Completely Free)</h3>

<p>The easiest way to use Kimi K3 is visiting <a href="https://kimi.moonshot.cn" target="_blank">kimi.moonshot.cn</a>. After registering, you get free access to K3. The web interface features:</p>

<ul>
<li><strong>Registration:</strong> Phone number registration, or login via WeChat/Alipay</li>
<li><strong>Usage limits:</strong> Daily usage caps for free users, but sufficient for everyday tasks</li>
<li><strong>Full features:</strong> Deep research, document analysis, code generation all available</li>
<li><strong>No VPN needed:</strong> Accessible directly from mainland China</li>
</ul>

<h3>Method 2: Kimi API (Pay-per-use, competitively priced)</h3>

<p>If you need API access to integrate Kimi K3, here is the official pricing (July 2026 data):</p>

<table>
<thead>
<tr><th>Model</th><th>Cache-Hit Input</th><th>Cache-Miss Input</th><th>Output</th><th>Context Window</th></tr>
</thead>
<tbody>
<tr><td><strong>Kimi K3</strong></td><td><strong>$0.30/million tokens</strong></td><td><strong>$3.00/million tokens</strong></td><td><strong>$15.00/million tokens</strong></td><td>1M tokens</td></tr>
<tr><td>Kimi K2.6</td><td>$0.16/million tokens</td><td>$0.95/million tokens</td><td>$4.00/million tokens</td><td>262K tokens</td></tr>
</tbody>
</table>

<p><strong>Key advantage:</strong> The Kimi API achieves over 90% context cache hit rates in coding workloads, meaning most input tokens are billed at the ultra-low $0.30/million rate.</p>

<p>For comparison, Anthropic Claude Sonnet charges $3.00/million tokens for cached input and $15.00/million for output. Kimi K3 at comparable performance levels delivers cached input at just 1/10th of Claude's price.</p>

<h2>Actual Capabilities of Kimi K3</h2>

<h3>1. Ultra-Long Context Processing</h3>

<p>The 1-million-token context window means you can upload an entire book, a complete code repository, or thousands of pages of research reports and have K3 analyze them all at once. This is top-tier among all LLMs.</p>

<h3>2. Deep Research</h3>

<p>Kimi K3 performs multi-round recursive deep research. Official demo cases include:</p>
<ul>
<li>Through 2,800+ web searches and 1,100+ terminal data pulls, analyzed 87 quarterly reports and 99 original PDFs to generate an interactive industry research report</li>
<li>Through 120+ rounds of recursive self-improvement, created an interactive research website covering 42 years of the AI ASIC industry</li>
</ul>

<h3>3. Code Generation</h3>

<p>Kimi K3 excels at code generation. Official examples include:</p>
<ul>
<li>Building a complete 3D browser game from scratch using Three.js WebGPU and GPU compute</li>
<li>Generating a cyberpunk-themed web-swinging browser experience</li>
</ul>

<h3>4. Visual Understanding</h3>

<p>K3 supports image input for complex visual analysis. In Simon Willison's pelican benchmark test, K3's visual understanding received high praise.</p>

<h2>Comparison with Major Models</h2>

<table>
<thead>
<tr><th>Feature</th><th>Kimi K3</th><th>Claude Sonnet</th><th>GPT-5.6</th><th>Kimi K2.6</th></tr>
</thead>
<tbody>
<tr><td>Parameters</td><td>2.8T (MoE)</td><td>Unknown</td><td>Unknown</td><td>~1T (MoE)</td></tr>
<tr><td>Context Window</td><td>1M tokens</td><td>200K tokens</td><td>200K tokens</td><td>262K tokens</td></tr>
<tr><td>API Input (cached)</td><td>$0.30/million</td><td>$3.00/million</td><td>$2.50/million</td><td>$0.16/million</td></tr>
<tr><td>API Output</td><td>$15.00/million</td><td>$15.00/million</td><td>$10.40/million</td><td>$4.00/million</td></tr>
<tr><td>Free web tier</td><td>✅ Yes</td><td>✅ Yes</td><td>✅ Yes</td><td>✅ Yes</td></tr>
<tr><td>Chain-of-thought</td><td>✅ Supported</td><td>✅ Supported</td><td>✅ Supported</td><td>✅ Supported</td></tr>
<tr><td>Tool calling</td><td>✅ Supported</td><td>✅ Supported</td><td>✅ Supported</td><td>✅ Supported</td></tr>
<tr><td>Open source plan</td><td>July 27, 2026</td><td>No</td><td>No</td><td>Already open</td></tr>
</tbody>
</table>

<h2>How to Use (Step by Step)</h2>

<h3>Step 1: Visit Kimi Web</h3>
<p>Go to <a href="https://kimi.moonshot.cn" target="_blank">kimi.moonshot.cn</a> and register with your phone number or log in via WeChat/Alipay.</p>

<h3>Step 2: Start a Conversation</h3>
<p>After logging in, type your question directly into the chat box. K3 is automatically used — no model selection needed.</p>

<h3>Step 3: Use Advanced Features</h3>
<ul>
<li><strong>Deep Research:</strong> Click the "Deep Research" button to let K3 perform multi-round web search and analysis</li>
<li><strong>Document Analysis:</strong> Upload PDF, Word, Excel files — K3 reads and analyzes their content</li>
<li><strong>Code Generation:</strong> Describe what you want, and K3 generates runnable code</li>
</ul>

<h3>Step 4: API Access (Optional)</h3>
<p>If you need programmatic access:</p>
<ol>
<li>Visit <a href="https://platform.kimi.ai" target="_blank">platform.kimi.ai</a> and register for an API account</li>
<li>Create an API Key</li>
<li>Use model name <code>kimi-k3</code> in your requests</li>
<li>Automatic context caching is enabled — coding workloads achieve 90%+ cache hit rates</li>
</ol>

<h2>Frequently Asked Questions</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: Is Kimi K3 really free on the web?</div>
<div class="faq-a">Yes, kimi.moonshot.cn offers free access to Kimi K3 for registered users. While there may be daily usage caps, they are sufficient for everyday conversations, document analysis, and code generation.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: When will Kimi K3 be open-sourced?</div>
<div class="faq-a">Moonshot AI plans to release Kimi K3 weights on July 27, 2026. After that, anyone can download and run it on their own hardware.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: What's the difference between K3 and K2.6?</div>
<div class="faq-a">K3 is K2.6's successor — parameters increased from ~1T to 2.8T, context window expanded from 262K to 1M, and reasoning/multimodal capabilities are significantly improved. API pricing is correspondingly higher.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Is the API expensive?</div>
<div class="faq-a">In coding scenarios, with 90%+ context cache hit rates, input costs just $0.30/million tokens — far below Claude Sonnet's $3.00/million. Output pricing at $15.00/million matches Claude Sonnet.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Does Kimi K3 support Chinese?</div>
<div class="faq-a">Fully. Chinese comprehension and generation are K3's strengths, especially for Chinese document analysis and code comments.</div>
</div>
</div>

<h2>Summary</h2>

<p>Kimi K3 is one of the most noteworthy AI models of 2026. With 2.8 trillion parameters, a 1-million-token context window, deep research capabilities, and highly competitive API pricing, it's an excellent choice for both developers and everyday users.</p>

<p>Whether you want to use it for free via the web interface or integrate it into your applications via API, Kimi K3 is worth trying. Head over to <a href="https://kimi.moonshot.cn" target="_blank">kimi.moonshot.cn</a> and start exploring!</p>
"""

    faq_zh = """{"@type":"Question","name":"Kimi K3 网页端真的免费吗？","acceptedAnswer":{"@type":"Answer","text":"是的，kimi.moonshot.cn 网页端对注册用户免费使用 Kimi K3。虽然可能有每日使用量限制，但对于日常对话、文档分析和代码生成已经完全足够。"}},{"@type":"Question","name":"Kimi K3 什么时候开源？","acceptedAnswer":{"@type":"Answer","text":"月之暗面计划在 2026年7月27日 发布 Kimi K3 的开源权重。"}},{"@type":"Question","name":"Kimi K3 和 K2.6 有什么区别？","acceptedAnswer":{"@type":"Answer","text":"K3 是 K2.6 的继任者，参数量从约1万亿提升到2.8万亿，上下文窗口从262K扩展到1M。"}},{"@type":"Question","name":"API 使用 K3 贵吗？","acceptedAnswer":{"@type":"Answer","text":"编码场景缓存命中率超90%，输入仅$0.30/百万token，远低于Claude Sonnet的$3.00/百万。"}}"""

    faq_en = """{"@type":"Question","name":"Is Kimi K3 really free on the web?","acceptedAnswer":{"@type":"Answer","text":"Yes, kimi.moonshot.cn offers free access to Kimi K3 for registered users with daily usage caps sufficient for everyday tasks."}},{"@type":"Question","name":"When will Kimi K3 be open-sourced?","acceptedAnswer":{"@type":"Answer","text":"Moonshot AI plans to release Kimi K3 weights on July 27, 2026."}},{"@type":"Question","name":"What's the difference between K3 and K2.6?","acceptedAnswer":{"@type":"Answer","text":"K3 is K2.6's successor — parameters from ~1T to 2.8T, context from 262K to 1M."}},{"@type":"Question","name":"Is the API expensive?","acceptedAnswer":{"@type":"Answer","text":"In coding with 90%+ cache hit rates, input costs just $0.30/million tokens vs Claude Sonnet's $3.00/million."}}"""

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

if __name__ == '__main__':
    main()
