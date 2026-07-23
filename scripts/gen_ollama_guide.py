#!/usr/bin/env python3
"""Generate a complete Ollama guide article with proper bilingual content."""

import json
import os
import re
from datetime import datetime

SLUG = "ollama-free-cloud-guide-2026"
DATE = "2026-07-20"

TITLE_ZH = "Ollama免费云端AI模型完全攻略：刚获$88M融资，8.9M开发者信赖，免费使用公开模型+轻量云端模型"
TITLE_EN = "Ollama Free Cloud AI Guide: $88M Funded, 8.9M Developers, Free Public Models + Lightweight Cloud Access"

DESC_ZH = "Ollama是开源AI模型运行平台，刚完成$88M融资，服务8.9M开发者。本地运行完全免费，云端提供免费轻量模型试用。Pro版$20/月享50倍用量+3并发，Max版$100/月享10并发。支持GLM、Nemotron、DeepSeek、Kimi、MiniMax等云端模型。"
DESC_EN = "Ollama is the leading open-source AI model platform, having just raised $88M from Benchmark, Theory Ventures, 8VC, and Y Combinator. It serves 8.9 million developers worldwide. Running models locally on your own hardware is completely free with no limits. The free cloud tier provides lightweight model access (Level 1 models like gpt-oss:20b). Pro ($20/mo) gives 50x more cloud usage than Free plus 3 concurrent models. Max ($100/mo) gives 5x more than Pro plus 10 concurrent models."

CONTENT_ZH = """<h1>Ollama免费云端AI模型完全攻略：刚获$88M融资，8.9M开发者信赖</h1>

<p>Ollama刚刚宣布完成了由Benchmark、Theory Ventures、8VC和Y Combinator领投的<strong>$8800万美元</strong>融资，目前全球已有<strong>890万开发者</strong>在使用这个开源AI模型平台。更令人瞩目的是，Ollama已被<strong>500强企业中的85%</strong>采用。本文将全面介绍Ollama的免费使用方式，包括本地无限运行和云端免费轻量模型。</p>

<h2>一、Ollama是什么？为什么值得关注？</h2>

<p>Ollama是一个开源的AI模型运行平台，核心理念是让任何人都能轻松地在自己的设备上运行大型语言模型。它的创始人Michael和Andrew曾在2015年创立Kitematic（Docker收购），随后又开发了Docker Desktop，服务超过1000万开发者。十年后，他们再次出发，专注于开源AI模型领域。</p>

<p>Ollama的核心优势在于三个原则：</p>
<ul>
<li><strong>所有权（Ownership）：</strong>开源模型归你所有，可以自由定制和优化，不会被任何平台锁定。</li>
<li><strong>可负担性（Affordability）：</strong>在自己的硬件上运行模型不会产生按token计费的账单，可以无限制地实验和迭代。</li>
<li><strong>隐私性（Privacy）：</strong>本地运行的模型数据永远不会离开你的设备。</li>
</ul>

<h2>二、本地运行：完全免费，无任何限制</h2>

<p>Ollama最核心的免费功能是在本地运行开源AI模型。只要你有一台电脑，就可以：</p>
<ul>
<li><strong>无限下载和运行</strong>任何公开的开源模型（Llama、Mistral、Phi、Qwen等数百个模型）</li>
<li><strong>无需API Key</strong>，无需注册账号，无需联网</li>
<li><strong>无需昂贵GPU</strong>，即使普通CPU也能运行量化版本</li>
<li><strong>支持命令行和API两种接口</strong>，一条命令即可启动</li>
</ul>

<p>安装极其简单，在macOS/Linux上只需一条命令：</p>
<pre><code>curl -fsSL https://ollama.com/install.sh | sh</code></pre>

<p>然后在终端输入模型名称即可开始对话：</p>
<pre><code>ollama run llama3.2</code></pre>

<p>Windows用户可以直接下载安装包。所有公开模型完全免费，没有任何使用次数限制，不限制token数量，不限制对话轮数。</p>

<h2>三、免费云端层级详解</h2>

<p>Ollama的云端服务为免费用户提供了轻量级模型的访问权限。以下是免费云端的详细规格：</p>

<h3>免费云端核心参数</h3>
<table>
<tr><th>项目</th><th>免费层规格</th></tr>
<tr><td>费用</td><td>$0/月，永久免费</td></tr>
<tr><td>并发模型数</td><td>1个</td></tr>
<tr><td>可用模型等级</td><td>Level 1（轻量模型）</td></tr>
<tr><td>会话限制</td><td>每5小时重置</td></tr>
<tr><td>周限制</td><td>每7天重置</td></tr>
<tr><td>计费方式</td><td>按GPU使用时间计算，非按token计数</td></tr>
</table>

<h3>免费云端可用模型举例</h3>
<p>Level 1轻量模型包括gpt-oss:20b等，适合以下场景：</p>
<ul>
<li>与模型进行日常对话聊天</li>
<li>评估较大模型的能力</li>
<li>使用小型模型进行编码辅助和AI助手功能</li>
</ul>

<h3>云端使用量衡量机制</h3>
<p>Ollama不使用传统的token计数方式，而是根据实际GPU时间消耗来计算使用量。这意味着：</p>
<ul>
<li>较短的请求和共享上下文的提示词消耗更少</li>
<li>不同模型消耗不同级别的用量（Level 1到Level 4）</li>
<li>随着硬件和模型架构效率提升，同样的用量可以获得更多服务</li>
</ul>

<h2>四、付费层级对比</h2>

<h3>Pro计划 - $20/月（或$200/年）</h3>
<table>
<tr><th>功能</th><th>Pro版</th><th>免费版</th></tr>
<tr><td>云端用量</td><td>免费层的<strong>50倍</strong></td><td>基础轻量用量</td></tr>
<tr><td>并发模型数</td><td><strong>3个</strong></td><td>1个</td></tr>
<tr><td>模型等级</td><td>更大、更强力的云端模型</td><td>仅Level 1</td></tr>
<tr><td>私有模型</td><td>可上传和分享私有模型</td><td>不支持</td></tr>
<tr><td>额外用量包</td><td>可购买额外用量余额</td><td>不适用</td></tr>
</table>

<h3>Max计划 - $100/月</h3>
<table>
<tr><th>功能</th><th>Max版</th><th>Pro版</th></tr>
<tr><td>云端用量</td><td>Pro版的<strong>5倍</strong>（即免费层的250倍）</td><td>免费层的50倍</td></tr>
<tr><td>并发模型数</td><td><strong>10个</strong></td><td>3个</td></tr>
<tr><td>适用场景</td><td>持续Agent任务、多并发Agent、长时间大型模型会话</td><td>日常编码、深度研究</td></tr>
</table>

<h2>五、云端模型列表与等级</h2>

<p>Ollama云端支持以下主要模型系列：</p>
<ul>
<li><strong>GLM</strong> - 智谱AI的大语言模型系列</li>
<li><strong>Nemotron</strong> - NVIDIA的开源模型系列</li>
<li><strong>DeepSeek</strong> - 深度求索的高性能模型</li>
<li><strong>Kimi</strong> - Moonshot AI的智能模型</li>
<li><strong>MiniMax</strong> - MiniMax的对话模型</li>
</ul>

<p>模型使用等级从Level 1（轻量）到Level 4（超重型）不等：</p>
<ul>
<li><strong>Level 1（轻量）：</strong>如gpt-oss:20b，免费层可用</li>
<li><strong>Level 4（超重型）：</strong>如deepseek-v4-pro，需Pro或Max计划</li>
</ul>

<p>你可以在模型详情页查看每个模型的具体使用等级。</p>

<h2>六、使用教程：从零开始</h2>

<h3>第1步：安装Ollama</h3>
<p>访问 <a href="https://ollama.com/download">ollama.com/download</a> 下载安装包，或使用终端命令安装。</p>

<h3>第2步：运行本地模型</h3>
<pre><code># 运行Llama 3.2
ollama run llama3.2

# 运行Qwen
ollama run qwen2.5

# 运行Mistral
ollama run mistral</code></pre>

<h3>第3步：使用云端模型</h3>
<p>在终端中使用<strong>ollama run</strong>命令时，如果选择的模型在本地不可用且支持云端，Ollama会自动尝试通过云端加载。免费用户可以使用Level 1模型。</p>

<h3>第4步：通过API使用</h3>
<p>Ollama提供OpenAI兼容的API接口，本地运行后可以在localhost:11434访问：</p>
<pre><code>curl http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3.2",
    "messages": [{"role": "user", "content": "你好"}]
  }'</code></pre>

<h2>七、常见问题FAQ</h2>

<h3>Q1：Ollama免费版真的完全免费吗？</h3>
<p>是的。本地运行所有公开模型完全免费，无次数限制、无token限制、无时间限制。云端免费层提供Level 1轻量模型访问，也无需付费。</p>

<h3>Q2：免费版有多少使用限制？</h3>
<p>免费版云端限制为：每次会话最长5小时（超时自动重置），每周有总量限制（7天重置），同时只能运行1个云端模型。本地运行无任何限制。</p>

<h3>Q3：Ollama的云端模型支持工具调用吗？</h3>
<p>是的。所有经过测试的云端模型都支持工具调用（tool calling），并在真实Agent工作流中验证过。</p>

<h3>Q4：什么时候会达到使用上限？</h3>
<p>你可以在Ollama设置页面随时查看用量。当达到计划的90%时，Ollama会发送电子邮件提醒（可在设置中关闭）。</p>

<h3>Q5：团队版什么时候推出？</h3>
<p>Ollama正在开发Team计划，包含模型访问控制等企业功能，目前处于即将推出的状态。</p>

<h3>Q6：如何查看某个模型的使用等级？</h3>
<p>访问Ollama模型页面即可查看该模型的使用等级（Level 1-4）。Level 1模型在免费版中可用。</p>
"""

CONTENT_EN = """<h1>Ollama Free Cloud AI Guide: $88M Funded, 8.9M Developers, Free Public Models + Lightweight Cloud Access</h1>

<p>Ollama just announced a <strong>$88 million</strong> funding round led by Benchmark, Theory Ventures, 8VC, and Y Combinator. The platform now serves <strong>8.9 million developers</strong> worldwide and is used by <strong>85% of Fortune 500 companies</strong>. This comprehensive guide covers everything you need to know about using Ollama for free, including unlimited local model running and free cloud-tier lightweight models.</p>

<h2>1. What Is Ollama and Why Does It Matter?</h2>

<p>Ollama is an open-source AI model platform designed to make running large language models accessible to everyone. Its founders, Michael and Andrew, previously created Kitematic (acquired by Docker in 2015) and then built Docker Desktop, which served over 10 million developers. Ten years later, they turned their attention to open-source AI.</p>

<p>Ollama is built around three core principles:</p>
<ul>
<li><strong>Ownership:</strong> Open-source models belong to you. Customize, fine-tune, and optimize freely without vendor lock-in.</li>
<li><strong>Affordability:</strong> Running models on your own hardware means no per-token bills. Experiment and iterate without worrying about runaway costs.</li>
<li><strong>Privacy:</strong> Data never leaves your machine when running models locally.</li>
</ul>

<h2>2. Local Running: Completely Free, Unlimited</h2>

<p>The core free feature of Ollama is running open-source AI models locally on your own hardware. With just a computer, you get:</p>
<ul>
<li><strong>Unlimited downloads and runs</strong> of any public open-source model (Llama, Mistral, Phi, Qwen, and hundreds more)</li>
<li><strong>No API key required,</strong> no account registration, no internet connection needed</li>
<li><strong>No expensive GPU needed</strong> -- quantized models run on regular CPUs</li>
<li><strong>Both CLI and API interfaces</strong> -- start with a single command</li>
</ul>

<p>Installation is extremely simple on macOS and Linux:</p>
<pre><code>curl -fsSL https://ollama.com/install.sh | sh</code></pre>

<p>Then run any model in your terminal:</p>
<pre><code>ollama run llama3.2</code></pre>

<p>Windows users can download the installer directly. All public models are completely free with no usage limits, no token caps, and no conversation restrictions.</p>

<h2>3. Free Cloud Tier: Detailed Breakdown</h2>

<p>Ollama's cloud service provides lightweight model access for free users. Here are the complete specifications:</p>

<h3>Free Cloud Core Parameters</h3>
<table>
<tr><th>Feature</th><th>Free Tier</th></tr>
<tr><td>Cost</td><td>$0/month, forever free</td></tr>
<tr><td>Concurrent models</td><td>1</td></tr>
<tr><td>Available model levels</td><td>Level 1 (lightweight models only)</td></tr>
<tr><td>Session limit</td><td>Resets every 5 hours</td></tr>
<tr><td>Weekly limit</td><td>Resets every 7 days</td></tr>
<tr><td>Billing method</td><td>Based on GPU time, not token count</td></tr>
</table>

<h3>Examples of Free-Level-1 Models</h3>
<p>Level 1 lightweight models like gpt-oss:20b are suitable for:</p>
<ul>
<li>Chatting with models and casual conversations</li>
<li>Evaluating larger models before upgrading</li>
<li>Coding assistance and AI assistant tasks with smaller models</li>
</ul>

<h3>How Cloud Usage Is Measured</h3>
<p>Ollama doesn't use traditional token counting. Instead, usage is based on actual GPU time consumed:</p>
<ul>
<li>Shorter requests and prompts sharing cached context use less usage</li>
<li>Different models consume different usage levels (Level 1 to Level 4)</li>
<li>As hardware and model architectures improve, you get more service for the same usage allowance</li>
</ul>

<h2>4. Paid Tier Comparison</h2>

<h3>Pro Plan -- $20/month (or $200/year)</h3>
<table>
<tr><th>Feature</th><th>Pro</th><th>Free</th></tr>
<tr><td>Cloud usage</td><td><strong>50x more</strong> than Free</td><td>Lightweight baseline</td></tr>
<tr><td>Concurrent models</td><td><strong>3</strong></td><td>1</td></tr>
<tr><td>Model access</td><td>Larger, more powerful cloud models</td><td>Level 1 only</td></tr>
<tr><td>Private models</td><td>Upload and share private models</td><td>Not available</td></tr>
<tr><td>Extra usage packs</td><td>Purchase additional usage balance</td><td>N/A</td></tr>
</table>

<h3>Max Plan -- $100/month</h3>
<table>
<tr><th>Feature</th><th>Max</th><th>Pro</th></tr>
<tr><td>Cloud usage</td><td><strong>5x more than Pro</strong> (250x Free)</td><td>50x Free</td></tr>
<tr><td>Concurrent models</td><td><strong>10</strong></td><td>3</td></tr>
<tr><td>Best for</td><td>Continuous agent tasks, multiple concurrent agents, extended large-model sessions</td><td>Daily coding, deep research</td></tr>
</table>

<h2>5. Available Cloud Models and Levels</h2>

<p>Ollama's cloud supports these major model families:</p>
<ul>
<li><strong>GLM</strong> -- Zhipu AI's large language model series</li>
<li><strong>Nemotron</strong> -- NVIDIA's open-source model series</li>
<li><strong>DeepSeek</strong> -- DeepSeek's high-performance models</li>
<li><strong>Kimi</strong> -- Moonshot AI's intelligent models</li>
<li><strong>MiniMax</strong> -- MiniMax's conversational models</li>
</ul>

<p>Models are rated from Level 1 (lightweight) to Level 4 (extra-heavy):</p>
<ul>
<li><strong>Level 1 (light):</strong> e.g., gpt-oss:20b -- available on Free tier</li>
<li><strong>Level 4 (extra-heavy):</strong> e.g., deepseek-v4-pro -- requires Pro or Max</li>
</ul>

<p>You can check each model's usage level on its individual model page.</p>

<h2>6. Step-by-Step Usage Tutorial</h2>

<h3>Step 1: Install Ollama</h3>
<p>Visit <a href="https://ollama.com/download">ollama.com/download</a> to download the installer, or use the terminal command.</p>

<h3>Step 2: Run Local Models</h3>
<pre><code># Run Llama 3.2
ollama run llama3.2

# Run Qwen
ollama run qwen2.5

# Run Mistral
ollama run mistral</code></pre>

<h3>Step 3: Use Cloud Models</h3>
<p>When you run <strong>ollama run</strong> in the terminal and the model isn't available locally but supports cloud inference, Ollama automatically attempts to load it through the cloud. Free users can access Level 1 models.</p>

<h3>Step 4: Use via API</h3>
<p>Ollama provides an OpenAI-compatible API interface. After running locally, access it at localhost:11434:</p>
<pre><code>curl http://localhost:11434/v1/chat/completions \\
  -H "Content-Type: application/json" \\
  -d '{
    "model": "llama3.2",
    "messages": [{"role": "user", "content": "Hello"}]
  }'</code></pre>

<h2>7. Frequently Asked Questions</h2>

<h3>Q1: Is Ollama's free tier really completely free?</h3>
<p>Yes. Running all public models locally is completely free with no usage limits, no token caps, and no time restrictions. The free cloud tier provides Level 1 lightweight model access at no cost.</p>

<h3>Q2: How many usage limits does the free tier have?</h3>
<p>For cloud: each session lasts up to 5 hours (auto-resets), there are weekly limits (reset every 7 days), and only 1 concurrent model is allowed. Local running has absolutely no limits whatsoever.</p>

<h3>Q3: Do cloud models support tool calling?</h3>
<p>Yes. All cloud models that are trained for tools are tested for tool calling and validated with real agent workflows before going live.</p>

<h3>Q4: How do I know when I'm approaching my usage limit?</h3>
<p>Check your usage anytime in the Ollama settings page. At 90% of your plan's limit, Ollama sends an email reminder (which you can disable in settings).</p>

<h3>Q5: When will the Team plan be available?</h3>
<p>Ollama is developing a Team plan with model access controls and enterprise features. It is currently marked as "coming soon."</p>

<h3>Q6: How do I check a model's usage level?</h3>
<p>Visit the model's page on Ollama to see its usage level (Level 1-4). Level 1 models are available on the free tier.</p>
"""

FAQ_ZH = [
    {"@type": "Question", "name": "Ollama免费版真的完全免费吗？", "acceptedAnswer": {"@type": "Answer", "text": "是的。本地运行所有公开模型完全免费，无次数限制、无token限制、无时间限制。云端免费层提供Level 1轻量模型访问，也无需付费。"}},
    {"@type": "Question", "name": "免费版有多少使用限制？", "acceptedAnswer": {"@type": "Answer", "text": "免费版云端限制为：每次会话最长5小时（超时自动重置），每周有总量限制（7天重置），同时只能运行1个云端模型。本地运行无任何限制。"}},
    {"@type": "Question", "name": "Ollama的云端模型支持工具调用吗？", "acceptedAnswer": {"@type": "Answer", "text": "是的。所有经过测试的云端模型都支持工具调用（tool calling），并在真实Agent工作流中验证过。"}},
    {"@type": "Question", "name": "什么时候会达到使用上限？", "acceptedAnswer": {"@type": "Answer", "text": "你可以在Ollama设置页面随时查看用量。当达到计划的90%时，Ollama会发送电子邮件提醒（可在设置中关闭）。"}},
    {"@type": "Question", "name": "如何查看某个模型的使用等级？", "acceptedAnswer": {"@type": "Answer", "text": "访问Ollama模型页面即可查看该模型的使用等级（Level 1-4）。Level 1模型在免费版中可用。"}}
]

FAQ_EN = [
    {"@type": "Question", "name": "Is Ollama's free tier really completely free?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. Running all public models locally is completely free with no usage limits, no token caps, and no time restrictions. The free cloud tier provides Level 1 lightweight model access at no cost."}},
    {"@type": "Question", "name": "How many usage limits does the free tier have?", "acceptedAnswer": {"@type": "Answer", "text": "For cloud: each session lasts up to 5 hours (auto-resets), there are weekly limits (reset every 7 days), and only 1 concurrent model is allowed. Local running has absolutely no limits whatsoever."}},
    {"@type": "Question", "name": "Do cloud models support tool calling?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. All cloud models that are trained for tools are tested for tool calling and validated with real agent workflows before going live."}},
    {"@type": "Question", "name": "How do I know when I'm approaching my usage limit?", "acceptedAnswer": {"@type": "Answer", "text": "Check your usage anytime in the Ollama settings page. At 90% of your plan's limit, Ollama sends an email reminder (which you can disable in settings)."}},
    {"@type": "Question", "name": "How do I check a model's usage level?", "acceptedAnswer": {"@type": "Answer", "text": "Visit the model's page on Ollama to see its usage level (Level 1-4). Level 1 models are available on the free tier."}}
]

def generate_html(lang, title, desc, content, faqs):
    """Generate a complete HTML page."""
    if lang == 'zh':
        hreflang_zh = f'https://aifreeplan.com/zh/guides/{SLUG}'
        hreflang_en = f'https://aifreeplan.com/en/guides/{SLUG}'
        breadcrumb_home = '首页'
        breadcrumb_section = '攻略'
        nav_link_zh = '/zh'
        nav_all = '/zh/all'
        nav_guides = '/zh/guides'
        nav_privacy = '/zh/privacy'
        lang_btn_text = 'English'
        lang_btn_href = f'/en/guides/{SLUG}'
        brand_desc = 'AI驱动的免费工具聚合平台，永久免费。'
        footer_legal_privacy = '/zh/privacy'
        footer_legal_terms = '/zh/terms'
        breadcrumb_section_link = '/zh/guides'
        breadcrumb_span = title
        bread_home_item = '/zh'
        bread_sec_item = '/zh/guides'
        bread_name_item = title
    else:
        hreflang_zh = f'https://aifreeplan.com/zh/guides/{SLUG}'
        hreflang_en = f'https://aifreeplan.com/en/guides/{SLUG}'
        breadcrumb_home = 'Home'
        breadcrumb_section = 'Guides'
        nav_link_zh = '/en'
        nav_all = '/en/all'
        nav_guides = '/en/guides'
        nav_privacy = '/en/privacy'
        lang_btn_text = '中文'
        lang_btn_href = f'/zh/guides/{SLUG}'
        brand_desc = 'AI-powered free tools aggregator. Free forever.'
        footer_legal_privacy = '/en/privacy'
        footer_legal_terms = '/en/terms'
        breadcrumb_section_link = '/en/guides'
        breadcrumb_span = title
        bread_home_item = '/en'
        bread_sec_item = '/en/guides'
        bread_name_item = title

    faq_json = json.dumps(faqs, ensure_ascii=False)

    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | AIFreePlan</title>
<meta property="og:type" content="article">
<meta property="og:title" content="{title} | AIFreePlan">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{hreflang_en}">
<meta property="og:site_name" content="AIFreePlan">
<meta property="og:locale" content="{'zh_CN' if lang == 'zh' else 'en_US'}">
<meta property="og:image" content="https://aifreeplan.com/og-image.png">
<meta name="twitter:image" content="https://aifreeplan.com/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title} | AIFreePlan">
<meta name="twitter:description" content="{desc}">
<meta name="description" content="{desc}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<meta name="theme-color" content="#6366F1">
<link rel="canonical" href="{hreflang_en}">
<link rel="alternate" hreflang="zh" href="{hreflang_zh}">
<link rel="alternate" hreflang="en" href="{hreflang_en}">
<link rel="alternate" hreflang="x-default" href="{hreflang_zh}">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{--bg:#F8FAFC;--bg-white:#fff;--border:#E2E8F0;--border-light:#F1F5F9;--text:#1E1B4B;--text-secondary:#64748B;--text-muted:#94A3B8;--accent:#6366F1;--accent-hover:#4F46E5;--accent-light:rgba(99,102,241,.1);--green:#059669;--green-light:rgba(5,150,105,.1);--shadow:0 4px 20px rgba(0,0,0,.05);--radius:12px}}
body{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Noto Sans SC","PingFang SC","Microsoft YaHei",sans-serif;background:var(--bg);color:var(--text);line-height:1.6}}
.container{{max-width:1280px;margin:0 auto;padding:0 40px}}
.header{{background:var(--bg-white);border-bottom:1px solid var(--border);position:sticky;top:0;z-index:100}}
.header-inner{{display:flex;align-items:center;justify-content:space-between;height:72px}}
.logo{{display:flex;align-items:center;gap:8px;text-decoration:none;color:var(--text);font-size:24px;font-weight:700}}
.logo .accent{{color:var(--accent)}}
.nav{{display:flex;gap:32px;align-items:center}}
.nav a{{color:var(--text);text-decoration:none;font-size:15px;font-weight:500;transition:color .2s}}
.nav a:hover{{color:var(--accent)}}
.btn{{display:inline-flex;align-items:center;justify-content:center;padding:10px 22px;border-radius:8px;font-size:15px;font-weight:600;cursor:pointer;border:none;transition:all .2s;text-decoration:none}}
.btn-primary{{background:var(--accent);color:#fff}}
.btn-primary:hover{{background:var(--accent-hover)}}
.article-container{{max-width:800px;margin:0 auto;padding:40px 20px 80px}}
.article-container h1{{font-size:36px;font-weight:700;margin-bottom:16px;line-height:1.3}}
.article-container h2{{font-size:24px;font-weight:700;margin-top:40px;margin-bottom:16px;padding-top:24px;border-top:1px solid var(--border)}}
.article-container h3{{font-size:20px;font-weight:600;margin-top:32px;margin-bottom:12px}}
.article-container p{{margin-bottom:16px;color:var(--text-secondary);line-height:1.8}}
.article-container ul,.article-container ol{{margin-bottom:16px;padding-left:24px;color:var(--text-secondary)}}
.article-container li{{margin-bottom:8px;line-height:1.6}}
.article-container img{{max-width:100%;height:auto;border-radius:12px;margin:24px 0;box-shadow:var(--shadow)}}
.article-container a{{color:var(--accent);text-decoration:underline}}
.article-container table{{width:100%;border-collapse:collapse;margin:20px 0;font-size:14px}}
.article-container th,.article-container td{{padding:12px;border:1px solid var(--border);text-align:left}}
.article-container th{{background:var(--accent-light);font-weight:600}}
.article-container pre{{background:#1e1e2e;color:#cdd6f4;padding:16px;border-radius:8px;overflow-x:auto;margin:16px 0;font-size:13px}}
.article-container code{{font-family:"SF Mono",Monaco,Consolas,monospace}}
.breadcrumb{{font-size:14px;color:var(--text-muted);margin-bottom:24px}}
.breadcrumb a{{color:var(--text-muted);text-decoration:none}}
.breadcrumb a:hover{{color:var(--accent)}}
.breadcrumb-sep{{margin:0 8px}}
.footer{{background:#1a1a2e;padding:50px 0 30px;color:#fff;margin-top:60px}}
.footer-inner{{display:flex;justify-content:space-between;gap:60px;flex-wrap:wrap}}
.footer-brand{{max-width:300px}}
.footer-brand p{{font-size:14px;color:rgba(255,255,255,.6)}}
.footer-links{{display:flex;gap:60px}}
.footer-col{{display:flex;flex-direction:column;gap:10px}}
.footer-col h4{{font-size:14px;font-weight:700;color:#fff}}
.footer-col a{{color:rgba(255,255,255,.6);text-decoration:none;font-size:14px}}
.footer-col a:hover{{color:#fff}}
.footer-bottom{{margin-top:30px;padding-top:20px;border-top:1px solid rgba(255,255,255,.1);font-size:13px;color:rgba(255,255,255,.4)}}
@media(max-width:768px){{.article-container{{padding:16px 16px 48px;max-width:100%}}.article-container h1{{font-size:24px}}.article-container h2{{font-size:20px}}.container{{padding:0 16px}}.nav{{display:none}}}}
</style>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article","headline":"{title}","description":"{desc}","url":"{hreflang_en}","datePublished":"{DATE}","dateModified":"{DATE}","author":{{"@type":"Organization","name":"AIFreePlan"}},"publisher":{{"@type":"Organization","name":"AIFreePlan","url":"https://aifreeplan.com"}},"mainEntityOfPage":{{"@type":"WebPage","@id":"{hreflang_en}"}}}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"{breadcrumb_home}","item":"{bread_home_item}"}},{{"@type":"ListItem","position":2,"name":"{breadcrumb_section}","item":"{bread_sec_item}"}},{{"@type":"ListItem","position":3,"name":"{bread_name_item}","item":"{hreflang_en}"}}]}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":{faq_json}}}
</script>
</head>
<body>
<header class="header">
  <div class="container header-inner">
    <a href="{nav_link_zh}" class="logo">AI<span class="accent">FreePlan</span></a>
    <nav class="nav">
      <a href="{nav_all}">{'All Tools' if lang == 'en' else '全部工具'}</a>
      <a href="{nav_guides}">{'Guides' if lang == 'en' else '攻略'}</a>
      <a href="{nav_privacy}">{'Privacy' if lang == 'en' else '隐私'}</a>
      <a href="{lang_btn_href}" class="btn btn-primary">{lang_btn_text}</a>
    </nav>
  </div>
</header>
<main class="article-container">
<nav class="breadcrumb"><a href="{bread_home_item}">{breadcrumb_home}</a> <span class="breadcrumb-sep">›</span> <a href="{breadcrumb_section_link}">{breadcrumb_section}</a> <span class="breadcrumb-sep">›</span> <span>{breadcrumb_span}</span></nav>
{content}
</main>
<footer class="footer">
  <div class="container footer-inner">
    <div class="footer-brand"><a href="{nav_link_zh}" class="logo" style="color:#059669">AI<span class="accent" style="color:#6366F1">FreePlan</span></a><p>{brand_desc}</p></div>
    <div class="footer-links">
      <div class="footer-col"><h4>{('Product' if lang == 'en' else '产品')}</h4><a href="{nav_all}">{('All Tools' if lang == 'en' else '全部工具')}</a><a href="{nav_guides}">{('Guides' if lang == 'en' else '攻略')}</a></div>
      <div class="footer-col"><h4>{('Legal' if lang == 'en' else '法律')}</h4><a href="{footer_legal_privacy}">{('Privacy' if lang == 'en' else '隐私政策')}</a><a href="{footer_legal_terms}">{('Terms' if lang == 'en' else '用户协议')}</a></div>
    </div>
  </div>
  <div class="container footer-bottom">&copy; 2026 AIFreePlan. All rights reserved.</div>
</footer>
</body></html>'''
    return html


def main():
    # Generate HTML files
    zh_html = generate_html('zh', TITLE_ZH, DESC_ZH, CONTENT_ZH, FAQ_ZH)
    en_html = generate_html('en', TITLE_EN, DESC_EN, CONTENT_EN, FAQ_EN)

    os.makedirs('/home/ubuntu/aifreeplan/zh/guides', exist_ok=True)
    os.makedirs('/home/ubuntu/aifreeplan/en/guides', exist_ok=True)

    with open(f'/home/ubuntu/aifreeplan/zh/guides/{SLUG}.html', 'w', encoding='utf-8') as f:
        f.write(zh_html)
    with open(f'/home/ubuntu/aifreeplan/en/guides/{SLUG}.html', 'w', encoding='utf-8') as f:
        f.write(en_html)

    print(f"Generated: /zh/guides/{SLUG}.html")
    print(f"Generated: /en/guides/{SLUG}.html")

    # Validate
    import re
    for lang in ['zh', 'en']:
        with open(f'{lang}/guides/{SLUG}.html', 'r') as f:
            html = f.read()
        text = re.sub(r'<[^>]+>', ' ', html)
        text = re.sub(r'\s+', ' ', text).strip()
        cn_chars = sum(1 for c in text if '\u4e00' <= c <= '\u9fff')
        total = len(text)
        cn_pct = (cn_chars / total * 100) if total > 0 else 0
        print(f"{lang.upper()}: {total} chars, {cn_chars} CN ({cn_pct:.1f}%)")
        if cn_pct >= 5 and lang == 'en':
            print(f"  WARNING: Too much Chinese in EN version!")
        elif lang == 'zh' and total < 1000:
            print(f"  WARNING: Content too short!")

    print("\nDone!")


if __name__ == '__main__':
    main()
