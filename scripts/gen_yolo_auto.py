#!/usr/bin/env python3
"""
Generate Yolo-Auto guide article
"""
import os
import json
from datetime import datetime

slug = "yolo-auto-free-llm-api-2026"
today = datetime.now().strftime('%Y-%m-%d')

title_zh = "Yolo-Auto免费AI API完全攻略：Qwen3.6-35B每日15次免费+无限使用"
title_en = "Yolo-Auto Free LLM API Guide: 15 Daily Free Requests + Unlimited $10/mo Plan"

desc_zh = "Yolo-Auto是一个新兴的开源LLM API平台，提供OpenAI兼容接口，支持Qwen3.6-35B模型。免费套餐每日15次请求，Builder计划$10/月无限使用，且承诺不存储任何提示词数据。"
desc_en = "Yolo-Auto is an emerging open-source LLM API platform offering an OpenAI-compatible interface powered by Qwen3.6-35B-A3B. Free tier includes 15 requests/day. Builder plan $10/mo for unlimited tokens. No prompt storage."

content_zh = """<h1>Yolo-Auto免费AI API完全攻略：Qwen3.6-35B每日15次免费+无限使用</h1>

<p>在AI编程代理和自动化工作流越来越流行的今天，稳定的LLM API是许多开发者的刚需。但大多数平台的按token计费模式让人难以预测成本——一个复杂的代码重构任务可能消耗数万token，账单瞬间飙升。</p>

<p><strong>Yolo-Auto</strong>提供了一种全新的思路：<strong>按并发数而非按token计费</strong>。它基于开源模型Qwen3.6-35B-A3B，提供完全OpenAI兼容的API接口。注册即送免费额度，无需绑定信用卡。</p>

<h2>一、Yolo-Auto平台概览</h2>

<p>Yolo-Auto是一个专注于开发者和AI代理场景的LLM API平台。它的核心卖点是<strong>扁平化定价</strong>——不像OpenAI、Anthropic那样按输入/输出token分别计费，而是采用固定月费或免费额度的方式。</p>

<table>
<thead>
<tr><th>项目</th><th>详情</th></tr>
</thead>
<tbody>
<tr><td>网站</td><td><a href="https://yolo-auto.com" target="_blank">yolo-auto.com</a></td></tr>
<tr><td>核心模型</td><td>Qwen3.6-35B-A3B (FP8量化)</td></tr>
<tr><td>API格式</td><td>OpenAI兼容 (/v1/chat/completions)</td></tr>
<tr><td>上下文窗口</td><td>128K (Builder: 128K, Pro: 256K)</td></tr>
<tr><td>隐私政策</td><td>不存储提示词，不用于训练</td></tr>
<tr><td>免费额度</td><td>15次请求/天，无需信用卡</td></tr>
<tr><td>Builder计划</td><td>$10/月（约¥70），无限token，2并发</td></tr>
<tr><td>Pro计划</td><td>$20/月（约¥140），无限token，4并发，256K上下文</td></tr>
</tbody>
</table>

<h2>二、免费套餐详解</h2>

<p>Yolo-Auto的免费套餐对轻度用户非常友好：</p>

<ul>
<li><strong>每日15次请求</strong>：适合日常测试、小型项目和偶尔使用的开发者</li>
<li><strong>128K上下文窗口</strong>：可以处理较长的文档和代码库</li>
<li><strong>Qwen3.6-35B FP8质量</strong>：FP8量化版本在保持较高推理能力的同时降低了延迟</li>
<li><strong>无需信用卡</strong>：注册即可使用，零门槛体验</li>
<li><strong>无token计费</strong>：每次请求无论长短都算一次，简单透明</li>
</ul>

<p><strong>适合场景：</strong>日常代码补全测试、简单的问答对话、原型验证、学习OpenAI API格式。</p>

<p><strong>不适合场景：</strong>高频自动化代理（每天需要数百次调用）、超长文档处理（256K需求）、生产环境高可用。</p>

<h2>三、付费计划对比</h2>

<p>当免费额度不够用时，Yolo-Auto提供两个付费层级：</p>

<h3>Builder计划 — $10/月（约¥70）</h3>
<ul>
<li>无限token，无每日请求上限</li>
<li>2个并发请求</li>
<li>128K上下文窗口</li>
<li>公平调度优先级（高峰期优先响应）</li>
<li>随时取消</li>
</ul>

<h3>Pro计划 — $20/月（约¥140）</h3>
<ul>
<li>Builder计划的所有功能</li>
<li>4个并发请求</li>
<li>256K上下文窗口（可处理更大文档）</li>
<li>共享容量中的更高优先级</li>
<li>随时取消</li>
</ul>

<p><strong>关键区别：</strong>与传统API不同，Yolo-Auto的限制在于并发数而非token量。这意味着你可以一口气发送长请求而不必担心费用爆炸——只要不超过并发上限。</p>

<h2>四、快速上手指南</h2>

<h3>步骤1：注册账号</h3>
<p>访问 <a href="https://yolo-auto.com/signup" target="_blank">yolo-auto.com/signup</a>，使用邮箱或GitHub账号注册。免费套餐不需要绑定信用卡。</p>

<h3>步骤2：获取API Key</h3>
<p>登录后进入Dashboard，点击"Create API Key"生成你的密钥。密钥格式为标准的OpenAI兼容格式。</p>

<h3>步骤3：配置你的工具</h3>
<p>由于Yolo-Auto的API完全兼容OpenAI格式，你只需要修改base URL：</p>

<ul>
<li>Base URL: <code>https://api.yolo-auto.com/v1</code></li>
<li>Endpoint: <code>POST /v1/chat/completions</code></li>
</ul>

<p>以下是一个Python示例：</p>

<pre><code>import openai

client = openai.OpenAI(
    api_key="YOUR_YOLO_AUTO_KEY",
    base_url="https://api.yolo-auto.com/v1"
)

response = client.chat.completions.create(
    model="qwen3.6-35b",
    messages=[{"role": "user", "content": "解释量子计算的基本原理"}],
    temperature=0.7
)
print(response.choices[0].message.content)</code></pre>

<h3>步骤4：使用桌面客户端</h3>
<p>Yolo-Auto还提供桌面客户端，支持自定义OpenAI兼容的base URL。配置后即可像使用ChatGPT一样对话，适合非编程场景。</p>

<h2>五、Yolo-Auto vs 其他免费LLM API对比</h2>

<table>
<thead>
<tr><th>特性</th><th>Yolo-Auto</th><th>Cerebras</th><th>Mistral AI Studio</th><th>Agnes AI</th></tr>
</thead>
<tbody>
<tr><td>免费额度</td><td>15次/天</td><td>100万token/天</td><td>60K/天</td><td>注册送余额</td></tr>
<tr><td>无限使用方案</td><td>$10/月无限token</td><td>无</td><td>€10/月600K</td><td>完全免费</td></tr>
<tr><td>计费方式</td><td>按请求/并发</td><td>按token</td><td>按token</td><td>按token</td></tr>
<tr><td>上下文窗口</td><td>128K-256K</td><td>256K</td><td>128K</td><td>512K</td></tr>
<tr><td>隐私保护</td><td>不存储提示词</td><td>未明确</td><td>未明确</td><td>未明确</td></tr>
<tr><td>多模态</td><td>否（仅文本）</td><td>否</td><td>部分（OCR）</td><td>是（文本+图像+视频）</td></tr>
</tbody>
</table>

<p><strong>选择建议：</strong></p>
<ul>
<li>如果你需要<strong>完全免费且不限次数</strong>：选Agnes AI</li>
<li>如果你需要<strong>大量token但不想按量付费</strong>：选Yolo-Auto的Builder计划</li>
<li>如果你需要<strong>大模型+多模态</strong>：选Mistral AI Studio或Cerebras</li>
<li>如果你是<strong>偶尔测试</strong>：Yolo-Auto的15次/天免费额度足够</li>
</ul>

<h2>六、实用技巧和注意事项</h2>

<h3>1. 合理使用免费额度</h3>
<p>15次/天的免费额度对于个人开发足够了。建议：</p>
<ul>
<li>将多次短对话合并为单次长请求以节省次数</li>
<li>使用流式输出减少API调用次数</li>
<li>本地缓存常见问题的回答</li>
</ul>

<h3>2. 并发限制理解</h3>
<p>Builder计划的2个并发意味着同一时间最多有2个请求在处理。如果你的代理程序需要更多并行能力，需要考虑Pro计划的4并发。</p>

<h3>3. 公平调度机制</h3>
<p>Yolo-Auto采用公平调度器而非严格的token限制。高峰期时，付费用户的请求会得到优先处理，但免费用户仍然可以使用——只是响应速度可能稍慢。</p>

<h3>4. 隐私优势</h3>
<p>与OpenAI、Claude等平台不同，Yolo-Auto明确承诺不存储你的提示词和回复，也不用于模型训练。这对处理敏感代码和商业逻辑的开发者很重要。</p>

<h2>七、总结</h2>

<p>Yolo-Auto的最大亮点是<strong>打破了传统LLM API的token计量模式</strong>。对于需要稳定、可预测成本的开发者和AI代理来说，$10/月无限使用的方案极具吸引力。15次/天的免费额度也让新用户零风险体验。</p>

<p>如果你正在寻找一个简单、便宜、隐私友好的LLM API，Yolo-Auto值得加入你的技术栈。特别是对于使用OpenAI兼容接口的工具和框架，只需修改一行base URL即可无缝切换。</p>
"""

content_en = """<h1>Yolo-Auto Free LLM API Guide: 15 Daily Free Requests + Unlimited $10/mo Plan</h1>

<p>In an era where AI coding agents and automated workflows are becoming essential, a reliable LLM API is a must-have for many developers. But most platforms charge per-token, making costs unpredictable—a single complex code refactoring task can consume tens of thousands of tokens and spike your bill instantly.</p>

<p><strong>Yolo-Auto</strong> takes a different approach: <strong>flat-rate pricing based on concurrency, not tokens</strong>. Powered by the open-source Qwen3.6-35B-A3B model, it offers a fully OpenAI-compatible API. You get free credits on signup, and no credit card is required.</p>

<h2>1. Platform Overview</h2>

<p>Yolo-Auto is an emerging LLM API platform focused on developers and AI agent scenarios. Its core selling point is <strong>flat-rate pricing</strong>—unlike OpenAI or Anthropic which charge per input/output token, Yolo-Auto uses fixed monthly fees or free allowances.</p>

<table>
<thead>
<tr><th>Feature</th><th>Details</th></tr>
</thead>
<tbody>
<tr><td>Website</td><td><a href="https://yolo-auto.com" target="_blank">yolo-auto.com</a></td></tr>
<tr><td>Core Model</td><td>Qwen3.6-35B-A3B (FP8 quantized)</td></tr>
<tr><td>API Format</td><td>OpenAI-compatible (/v1/chat/completions)</td></tr>
<tr><td>Context Window</td><td>128K (Builder: 128K, Pro: 256K)</td></tr>
<tr><td>Privacy Policy</td><td>No prompt storage, no training on your data</td></tr>
<tr><td>Free Tier</td><td>15 requests/day, no credit card needed</td></tr>
<tr><td>Builder Plan</td><td>$10/mo (~¥70), unlimited tokens, 2 concurrent</td></tr>
<tr><td>Pro Plan</td><td>$20/mo (~¥140), unlimited tokens, 4 concurrent, 256K context</td></tr>
</tbody>
</table>

<h2>2. Free Tier Details</h2>

<p>Yolo-Auto's free tier is very generous for light users:</p>

<ul>
<li><strong>15 requests per day</strong>: Perfect for daily testing, small projects, and occasional use</li>
<li><strong>128K context window</strong>: Can handle longer documents and codebases</li>
<li><strong>Qwen3.6-35B FP8 quality</strong>: FP8 quantized version maintains good reasoning while reducing latency</li>
<li><strong>No credit card required</strong>: Zero barrier to entry</li>
<li><strong>No token billing</strong>: Every request counts as one, regardless of length—simple and transparent</li>
</ul>

<p><strong>Best for:</strong> Daily code completion testing, simple Q&A, prototype validation, learning the OpenAI API format.</p>

<p><strong>Not ideal for:</strong> High-frequency automated agents (hundreds of calls/day), ultra-long document processing (256K+ needs), production-grade high availability.</p>

<h2>3. Paid Plans Comparison</h2>

<p>When the free tier isn't enough, Yolo-Auto offers two paid tiers:</p>

<h3>Builder Plan — $10/month</h3>
<ul>
<li>Unlimited tokens, no daily request cap</li>
<li>2 concurrent requests</li>
<li>128K context window</li>
<li>Fair-scheduler priority (better response during peak times)</li>
<li>Cancel anytime</li>
</ul>

<h3>Pro Plan — $20/month</h3>
<ul>
<li>All Builder features</li>
<li>4 concurrent requests</li>
<li>256K context window (handle larger documents)</li>
<li>Higher priority on shared capacity</li>
<li>Cancel anytime</li>
</ul>

<p><strong>Key difference:</strong> Unlike traditional APIs, Yolo-Auto limits by concurrency, not token volume. You can send long requests without worrying about cost explosions—as long as you don't exceed your concurrency cap.</p>

<h2>4. Quick Start Guide</h2>

<h3>Step 1: Create Account</h3>
<p>Visit <a href="https://yolo-auto.com/signup" target="_blank">yolo-auto.com/signup</a> and register with email or GitHub. The free tier requires no credit card.</p>

<h3>Step 2: Get Your API Key</h3>
<p>After logging in, go to the Dashboard and click "Create API Key" to generate your key.</p>

<h3>Step 3: Configure Your Tools</h3>
<p>Since Yolo-Auto's API is fully OpenAI-compatible, you only need to change the base URL:</p>

<ul>
<li>Base URL: <code>https://api.yolo-auto.com/v1</code></li>
<li>Endpoint: <code>POST /v1/chat/completions</code></li>
</ul>

<p>Here's a Python example:</p>

<pre><code>import openai

client = openai.OpenAI(
    api_key="YOUR_YOLO_AUTO_KEY",
    base_url="https://api.yolo-auto.com/v1"
)

response = client.chat.completions.create(
    model="qwen3.6-35b",
    messages=[{"role": "user", "content": "Explain quantum computing basics"}],
    temperature=0.7
)
print(response.choices[0].message.content)</code></pre>

<h3>Step 4: Use the Desktop Client</h3>
<p>Yolo-Auto also provides a desktop client that supports custom OpenAI-compatible base URLs. Configure it and chat just like you would with ChatGPT—ideal for non-programming use cases.</p>

<h2>5. Yolo-Auto vs Other Free LLM APIs</h2>

<table>
<thead>
<tr><th>Feature</th><th>Yolo-Auto</th><th>Cerebras</th><th>Mistral AI Studio</th><th>Agnes AI</th></tr>
</thead>
<tbody>
<tr><td>Free allowance</td><td>15 requests/day</td><td>1M tokens/day</td><td>60K/day</td><td>Signup credits</td></tr>
<tr><td>Unlimited option</td><td>$10/mo unlimited</td><td>None</td><td>€10/mo 600K</td><td>Completely free</td></tr>
<tr><td>Billing model</td><td>Per-request/concurrency</td><td>Per-token</td><td>Per-token</td><td>Per-token</td></tr>
<tr><td>Context window</td><td>128K-256K</td><td>256K</td><td>128K</td><td>512K</td></tr>
<tr><td>Privacy</td><td>No prompt storage</td><td>Not specified</td><td>Not specified</td><td>Not specified</td></tr>
<tr><td>Multimodal</td><td>No (text only)</td><td>No</td><td>Partial (OCR)</td><td>Yes (text+image+video)</td></tr>
</tbody>
</table>

<p><strong>Recommendations:</strong></p>
<ul>
<li>Need <strong>completely free and unlimited</strong>: Choose Agnes AI</li>
<li>Need <strong>lots of tokens without per-unit billing</strong>: Choose Yolo-Auto Builder plan</li>
<li>Need <strong>large models + multimodal</strong>: Choose Mistral AI Studio or Cerebras</li>
<li>Just <strong>occasional testing</strong>: Yolo-Auto's 15 requests/day free tier is sufficient</li>
</ul>

<h2>6. Practical Tips</h2>

<h3>1. Make the Most of Free Tier</h3>
<p>15 requests/day is enough for personal development. Tips:</p>
<ul>
<li>Combine multiple short conversations into single long requests</li>
<li>Use streaming output to reduce API calls</li>
<li>Cache common answers locally</li>
</ul>

<h3>2. Understand Concurrency Limits</h3>
<p>The Builder plan's 2 concurrent means at most 2 requests are processed simultaneously. If your agent program needs more parallelism, consider the Pro plan's 4 concurrency.</p>

<h3>3. Fair-Scheduler Mechanism</h3>
<p>Yolo-Auto uses a fair scheduler rather than strict token limits. During peak times, paid users get priority, but free users can still use the service—just with potentially slower response times.</p>

<h3>4. Privacy Advantage</h3>
<p>Unlike OpenAI or Claude, Yolo-Auto explicitly promises not to store your prompts and responses, and won't use your data for model training. This matters for developers handling sensitive code and business logic.</p>

<h2>7. Summary</h2>

<p>Yolo-Auto's biggest advantage is <strong>breaking the traditional token-metering model of LLM APIs</strong>. For developers and AI agents needing stable, predictable costs, the $10/mo unlimited plan is highly attractive. The 15 requests/day free tier also lets new users try risk-free.</p>

<p>If you're looking for a simple, affordable, privacy-friendly LLM API, Yolo-Auto deserves a place in your tech stack. Especially for tools and frameworks using OpenAI-compatible interfaces, you can switch seamlessly by changing just one line of base URL.</p>
"""

faq_zh = '[{"@type":"Question","name":"Yolo-Auto免费套餐有多少次请求？","acceptedAnswer":{"@type":"Answer","text":"Yolo-Auto免费套餐提供每天15次请求，无需绑定信用卡。每次请求无论长短都算一次，128K上下文窗口。"}},{"@type":"Question","name":"Yolo-Auto的无限使用计划多少钱？","acceptedAnswer":{"@type":"Answer","text":"Builder计划$10/月（约¥70），无限token，2并发请求。Pro计划$20/月（约¥140），无限token，4并发请求，256K上下文窗口。"}}]'
faq_en = '[{"@type":"Question","name":"How many free requests does Yolo-Auto offer?","acceptedAnswer":{"@type":"Answer","text":"Yolo-Auto offers 15 free requests per day on the free tier. No credit card is required. Each request counts as one regardless of length, with a 128K context window."}},{"@type":"Question","name":"How much is Yolo-Auto unlimited plan?","acceptedAnswer":{"@type":"Answer","text":"The Builder plan is $10/month with unlimited tokens and 2 concurrent requests. The Pro plan is $20/month with unlimited tokens, 4 concurrent requests, and a 256K context window."}}]'

# Import the template generator
import importlib.util
spec = importlib.util.spec_from_file_location("write_guide", "/home/ubuntu/aifreeplan/scripts/write_guide.py")
if spec and spec.loader:
    wg = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(wg)
    generate_guide_html = wg.generate_guide_html
else:
    raise RuntimeError("Failed to load write_guide module")

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

print(f"Generated: {slug}")
print(f"ZH content length: {len(content_zh)} chars")
print(f"EN content length: {len(content_en)} chars")

# Count Chinese characters in EN content
import re
cn_chars = len(re.findall(r'[\u4e00-\u9fff]', content_en))
en_total = len(content_en)
cn_pct = (cn_chars / en_total * 100) if en_total > 0 else 0
print(f"EN Chinese char ratio: {cn_pct:.1f}% (should be <5%)")
