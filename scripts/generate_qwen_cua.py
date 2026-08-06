#!/usr/bin/env python3
"""Generate Qwen-CUA article"""
import os

slug = "qwen-cua-computer-use-agent-2026"
today = "2026-08-06"

title_zh = "阿里Qwen-CUA电脑控制Agent：397B参数免费开源，直接操控浏览器桌面软件"
title_en = "Alibaba Qwen-CUA: Free Open-Source Computer Use Agent with 397B Parameters"
desc_zh = "阿里Qwen团队推出原生Computer Use Agent「Qwen-CUA」，基于397B-A17B混合专家架构，直接通过屏幕截图感知界面状态，无需依赖DOM树，在OSWorld-Verified基准上达到86.2分。免费开源，可本地部署。"
desc_en = "Alibaba Qwen team releases Qwen-CUA, a native Computer Use Agent based on 397B-A17B MoE architecture. Directly perceives UI state through screenshots without DOM tree dependency, achieving 86.2 on OSWorld-Verified benchmark. Free and open-source."

content_zh = """
<h1>阿里Qwen-CUA电脑控制Agent：397B参数免费开源，直接操控浏览器桌面软件</h1>
<p>2026年8月5日，阿里Qwen团队联合XLang Lab正式发布原生Computer Use Agent——<strong>Qwen-CUA</strong>。这是国内首个支持直接通过屏幕截图感知界面状态、输出键盘鼠标事件操控浏览器、桌面及专业软件的AI Agent模型。</p>

<h2>核心技术亮点</h2>
<p>Qwen-CUA基于<strong>397B-A17B混合专家架构</strong>（MoE）构建，这个架构意味着模型拥有3970亿总参数，但每次推理只激活170亿参数，在性能与效率之间取得了优秀平衡。</p>

<p>与传统的Computer Use方案不同，Qwen-CUA<strong>无需依赖DOM树或无障碍元数据</strong>，而是直接通过屏幕截图感知界面状态，然后输出键盘鼠标事件。这种方案的优势在于：</p>
<ul>
<li>适用性更广：无论网页、桌面应用还是专业软件，只要有屏幕显示就能操控</li>
<li>绕过反自动化检测：不触碰DOM，更难被网站识别为机器人</li>
<li>真实用户视角：模拟人类通过视觉感知操作，更符合自然交互</li>
</ul>

<h2>性能表现</h2>
<p>在权威基准测试OSWorld-Verified上，Qwen-CUA取得了<strong>86.2分</strong>的优异成绩。万亿参数Max版本更是达到了<strong>87.6分</strong>，这一成绩意味着模型能够高效完成复杂的跨应用任务。</p>

<p>OSWorld是一个专注于评估AI Agent在真实操作系统环境中执行任务能力的基准测试，涵盖文件管理、软件开发、数据可视化、网页操作等多种场景。86.2分的得分表明Qwen-CUA已经具备在实际工作流中大规模应用的潜力。</p>

<h2>免费开源与使用方式</h2>
<p>好消息是，Qwen-CUA完全<strong>免费开源</strong>，用户可以：</p>
<ul>
<li>在ModelScope或Hugging Face下载模型权重进行本地部署</li>
<li>使用阿里云PAI平台进行云端推理</li>
<li>通过Qwen-Agent框架快速集成到自己的自动化流程中</li>
</ul>

<p>对于普通用户，建议通过云端API方式使用，无需配置本地GPU。对于开发者和企业用户，可以下载模型权重部署到自有服务器，完全掌控数据隐私。</p>

<h2>应用场景</h2>
<p>Qwen-CUA的主要应用场景包括：</p>
<ol>
<li><strong>网页自动化</strong>：自动填写表单、抓取数据、批量操作网页应用</li>
<li><strong>桌面办公</strong>：操控Word、Excel、PPT等办公软件，实现文档批量处理</li>
<li><strong>专业软件操作</strong>：控制CAD、PS、PR等专业软件完成设计任务</li>
<li><strong>跨平台工作流</strong>：在不同应用间无缝切换，完成复杂的多步骤任务</li>
</ol>

<h2>与同类产品对比</h2>
<table>
<tr><th>特性</th><th>Qwen-CUA</th><th>OpenAI Agent</th><th>Google Gemini Agent</th></tr>
<tr><td>架构参数</td><td>397B-A17B (MoE)</td><td>闭源</td><td>闭源</td></tr>
<tr><td>感知方式</td><td>截图</td><td>截图/DOM</td><td>截图/DOM</td></tr>
<tr><td>开源</td><td>✓ 免费</td><td>✗ 付费API</td><td>✗ 付费API</td></tr>
<tr><td>OSWorld分数</td><td>86.2</td><td>暂未公开</td><td>暂未公开</td></tr>
<tr><td>中文支持</td><td>原生支持</td><td>良好</td><td>良好</td></tr>
</table>

<h2>如何使用Qwen-CUA</h2>
<p>推荐三种使用方式：</p>
<p><strong>方式一：云端API（适合普通用户）</strong><br>
通过阿里云PAI平台或直接调用Qwen官方API，无需配置GPU，按调用量计费。</p>
<p><strong>方式二：本地部署（适合技术用户）</strong><br>
下载模型权重到本地，使用vLLM或SGLang进行推理。需要至少80GB显存的A100/H100 GPU，或部署多张消费级GPU。</p>
<p><strong>方式三：Qwen-Agent框架集成</strong><br>
使用Qwen-Agent官方框架，可以快速搭建自动化Agent，支持工具调用、多轮对话、任务规划等功能。</p>

<h2>总结</h2>
<p>Qwen-CUA的发布标志着国内AI Agent能力迈上新台阶。397B参数的庞大规模、86.2的OSWorld分数、完全免费开源的授权，使其成为当前最强的Computer Use Agent之一。无论是开发者、企业还是个人用户，都可以基于此构建强大的自动化解决方案。</p>
<p>对于普通用户，建议先从云端API试用开始；对于有技术能力的用户，本地部署可以获得更灵活、更私密的体验。随着模型的持续迭代，Qwen-CUA有望成为AI Agent领域的标杆产品。</p>
"""

content_en = """
<h1>Alibaba Qwen-CUA: Free Open-Source Computer Use Agent with 397B Parameters</h1>
<p>On August 5, 2026, Alibaba's Qwen team, in collaboration with XLang Lab, officially released <strong>Qwen-CUA</strong>, a native Computer Use Agent. This is China's first AI Agent model capable of perceiving UI states through screenshots and outputting keyboard/mouse events to control browsers, desktops, and professional software.</p>

<h2>Core Technical Highlights</h2>
<p>Qwen-CUA is built on a <strong>397B-A17B Mixture-of-Experts (MoE) architecture</strong>. This means the model has 397 billion total parameters but only activates 17 billion parameters per inference, achieving an excellent balance between performance and efficiency.</p>

<p>Unlike traditional Computer Use approaches, Qwen-CUA <strong>does not rely on DOM trees or accessibility metadata</strong>. Instead, it perceives UI states directly through screenshots and outputs keyboard/mouse events. This approach offers several advantages:</p>
<ul>
<li><strong>Broader applicability</strong>: Works with any application that has a screen display—web pages, desktop apps, or professional software</li>
<li><strong>Bypasses anti-bot detection</strong>: Doesn't interact with DOM, making it harder to identify as a bot</li>
<li><strong>Natural interaction</strong>: Simulates human visual perception, more intuitive for users</li>
</ul>

<h2>Performance Results</h2>
<p>On the authoritative OSWorld-Verified benchmark, Qwen-CUA achieved an impressive <strong>86.2 points</strong>. The trillion-parameter Max version reached <strong>87.6 points</strong>, indicating the model can efficiently handle complex cross-application tasks.</p>

<p>OSWorld is a benchmark specifically designed to evaluate AI Agents' ability to execute tasks in real operating system environments, covering file management, software development, data visualization, web operations, and more. A score of 86.2 suggests Qwen-CUA has strong potential for large-scale practical application.</p>

<h2>Free Open-Source & Usage</h2>
<p>The best news is that Qwen-CUA is completely <strong>free and open-source</strong>. Users can:</p>
<ul>
<li>Download model weights from ModelScope or Hugging Face for local deployment</li>
<li>Use Alibaba Cloud PAI platform for cloud inference</li>
<li>Integrate into automation workflows via the Qwen-Agent framework</li>
</ul>

<p>For regular users, we recommend using the cloud API approach—no local GPU configuration needed. For developers and enterprise users, downloading model weights for self-hosted deployment provides full data privacy control.</p>

<h2>Application Scenarios</h2>
<p>Qwen-CUA's main application scenarios include:</p>
<ol>
<li><strong>Web automation</strong>: Auto-fill forms, scrape data, batch operations on web applications</li>
<li><strong>Desktop office work</strong>: Control Word, Excel, PPT for batch document processing</li>
<li><strong>Professional software</strong>: Operate CAD, Photoshop, Premiere for design tasks</li>
<li><strong>Cross-platform workflows</strong>: Seamless switching between applications for complex multi-step tasks</li>
</ol>

<h2>Comparison with Competitors</h2>
<table>
<tr><th>Feature</th><th>Qwen-CUA</th><th>OpenAI Agent</th><th>Google Gemini Agent</th></tr>
<tr><td>Architecture</td><td>397B-A17B (MoE)</td><td>Proprietary</td><td>Proprietary</td></tr>
<tr><td>Perception</td><td>Screenshot</td><td>Screenshot/DOM</td><td>Screenshot/DOM</td></tr>
<tr><td>Open Source</td><td>✓ Free</td><td>✗ Paid API</td><td>✗ Paid API</td></tr>
<tr><td>OSWorld Score</td><td>86.2</td><td>Not disclosed</td><td>Not disclosed</td></tr>
<tr><td>Chinese Support</td><td>Native</td><td>Good</td><td>Good</td></tr>
</table>

<h2>How to Use Qwen-CUA</h2>
<p>Three recommended approaches:</p>
<p><strong>Method 1: Cloud API (for regular users)</strong><br>
Use Alibaba Cloud PAI platform or call the official Qwen API directly. No GPU configuration needed, pay per call volume.</p>
<p><strong>Method 2: Local Deployment (for technical users)</strong><br>
Download model weights locally and use vLLM or SGLang for inference. Requires at least 80GB VRAM A100/H100 GPU, or multiple consumer GPUs.</p>
<p><strong>Method 3: Qwen-Agent Framework Integration</strong><br>
Use the official Qwen-Agent framework to quickly build automation agents, supporting tool calling, multi-turn dialogue, and task planning.</p>

<h2>Conclusion</h2>
<p>The release of Qwen-CUA marks a new milestone in China's AI Agent capabilities. With 397 billion parameters, an 86.2 OSWorld score, and completely free open-source licensing, it stands as one of the strongest Computer Use Agents available today. Whether for developers, enterprises, or individual users, Qwen-CUA can be leveraged to build powerful automation solutions.</p>
<p>For regular users, we recommend starting with the cloud API. For technically inclined users, local deployment offers more flexibility and privacy. As the model continues to iterate, Qwen-CUA is poised to become a benchmark product in the AI Agent space.</p>
"""

faq_zh = '[{"@type":"Question","name":"Qwen-CUA是免费的吗？","acceptedAnswer":{"@type":"Answer","text":"是的，Qwen-CUA完全免费开源，用户可以下载模型权重进行本地部署，或通过云端API按调用量付费使用。"}}]'
faq_en = '[{"@type":"Question","name":"Is Qwen-CUA free?","acceptedAnswer":{"@type":"Answer","text":"Yes, Qwen-CUA is completely free and open-source. Users can download model weights for local deployment or use the cloud API on a pay-per-call basis."}}]'

# Read template
with open('/home/ubuntu/aifreeplan/scripts/write_guide.py', 'r') as f:
    template = f.read()

# Execute the template function
exec_globals = {}
exec(template, exec_globals)
generate_guide_html = exec_globals['generate_guide_html']

zh_html, en_html = generate_guide_html(slug, title_zh, title_en, desc_zh, desc_en, content_zh, content_en, faq_zh, faq_en, today)

# Write files
os.makedirs('/home/ubuntu/aifreeplan/zh/guides', exist_ok=True)
os.makedirs('/home/ubuntu/aifreeplan/en/guides', exist_ok=True)

with open(f'/home/ubuntu/aifreeplan/zh/guides/{slug}.html', 'w', encoding='utf-8') as f:
    f.write(zh_html)

with open(f'/home/ubuntu/aifreeplan/en/guides/{slug}.html', 'w', encoding='utf-8') as f:
    f.write(en_html)

print(f'Generated: {slug}')
print(f'Chinese content length: {len(content_zh)} chars')
print(f'English content length: {len(content_en)} chars')
