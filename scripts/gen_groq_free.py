#!/usr/bin/env python3
"""Generate Groq Free LPU Inference API Guide."""
import os
import sys
from datetime import datetime

sys.path.insert(0, '/home/ubuntu/aifreeplan/scripts')
from write_guide import generate_guide_html

def main():
    today = datetime.now().strftime('%Y-%m-%d')
    slug = "groq-free-lpu-inference-api-2026"

    title_zh = "Groq免费LPU推理API：每天1000次请求，极速开源模型接入攻略"
    title_en = "Groq Free LPU Inference API: 1000 Daily Requests with Fastest Open Source Models"
    desc_zh = "Groq使用自研LPU芯片提供极速AI推理服务，免费版每天1000次请求，支持Llama、Qwen等17个开源模型。本文详细介绍免费额度、限制条件、API使用方法和实际应用场景。"
    desc_en = "Groq uses custom LPU chips for ultra-fast AI inference. Free tier offers 1000 requests per day with 17 open-source models including Llama and Qwen. This guide details free limits, restrictions, API usage methods and practical application scenarios."

    content_zh = """<h1>Groq免费LPU推理API：每天1000次请求，极速开源模型接入攻略</h1>

<p>2026年6月，Groq的免费LPU推理服务继续保持<strong>业界领先的响应速度</strong>。作为目前公开可用的最快免费推理引擎，Groq自研的LPU（Language Processing Unit）硬件架构使其推理速度远超传统GPU方案。免费版每天提供<strong>1000次免费请求</strong>，支持<strong>17个主流开源模型</strong>，包括Llama 4、Qwen 3、Mixtral等。对于需要低延迟响应的实时对话应用、语音转文字、流式文本生成等场景，Groq是目前最值得选择的免费推理平台。</p>

<h2>Groq核心技术优势</h2>

<p>Groq的核心竞争力在于其自研的LPU硬件架构。与传统的GPU推理方案相比，LPU采用确定性架构和streaming编译器技术，消除了GPU中的随机内存访问瓶颈，实现了近乎零延迟的Token输出。</p>

<ul>
    <li><strong>硬件架构：</strong>LPU（Language Processing Unit）自研芯片，非GPU方案</li>
    <li><strong>响应速度：</strong>平均首token延迟<50ms，最大吞吐量300 TPM（Tokens Per Minute）</li>
    <li><strong>并发能力：</strong>支持单次请求多模型并行计算</li>
    <li><strong>模型数量：</strong>免费版开放17个开源模型</li>
    <li><strong>免费额度：</strong>每天1000次请求（每日重置）</li>
    <li><strong>速率限制：</strong>RPM 30（每分钟30请求），TPM 30000</li>
    <li><strong>商业用途：</strong>免费版允许商业用途</li>
    <li><strong>API兼容性：</strong>完全兼容OpenAI API格式</li>
</ul>

<h2>免费额度详解</h2>

<h3>1. 请求次数限制</h3>

<p>免费版用户每天获得<strong>1000次免费请求</strong>，每天UTC时间0点重置。这个额度对于个人开发者和小项目来说相当充足——假设每次对话平均消耗2次请求（一次编码+一次解码），每天可以完成约500轮对话。</p>

<table>
    <thead>
        <tr><th>使用场景</th><th>单次请求消耗</th><th>1000额度可支持量</th></tr>
    </thead>
    <tbody>
        <tr><td>纯文本问答（短消息）</td><td>1次</td><td>1000次对话</td></tr>
        <tr><td>代码生成（中等长度）</td><td>2-3次</td><td>300-500次对话</td></tr>
        <tr><td>长文档摘要（8K上下文）</td><td>3-5次</td><td>200-300次对话</td></tr>
        <tr><td>实时聊天（持续对话）</td><td>1-2次/轮</td><td>500-1000轮对话</td></tr>
    </tbody>
</table>

<h3>2. 速率限制</h3>

<p>免费版有两个并行的速率限制：<br>
• <strong>RPM 30：</strong>每分钟最多30个请求<br>
• <strong>TPM 30000：</strong>每分钟最多30000个Token输出</p>

<p>这两个限制通常不会成为问题，因为即使是运行Llama 3 70B模型，按每秒输出生成约5-10个Token计算，TPM 30000也意味着每分钟最多生成约5000个完整Token，这已经是非常高的吞吐量了。RPM 30的限制意味着每秒最多5个请求，对于绝大多数应用场景都足够用。</p>

<h3>3. 并发连接数</h3>

<p>免费版同时允许的连接数有限制，建议在生产环境中实施本地限流策略。如果有高并发需求，可以申请付费升级。</p>

<h2>支持的免费模型列表</h2>

<p>Groq免费版开放<strong>17个主流开源模型</strong>，以下是其中最值得推荐的几个：</p>

<table>
    <thead>
        <tr><th>模型名称</th><th>参数规模</th><th>适用场景</th><th>推荐指数</th></tr>
    </thead>
    <tbody>
        <tr><td>Llama 4 Scout</td><td>~25B</td><td>通用对话、代码生成</td><td>★★★★★</td></tr>
        <tr><td>Qwen3 32B</td><td>32B</td><td>中文理解、复杂推理</td><td>★★★★★</td></tr>
        <tr><td>Llama 4 Hunter</td><td>~70B</td><td>高精度任务、长上下文</td><td>★★★★☆</td></tr>
        <tr><td>Mixtral 8x22B</td><td>MoE 129B</td><td>高吞吐场景</td><td>★★★★☆</td></tr>
        <tr><td>Gemma 2 9B</td><td>9B</td><td>快速响应、轻量级任务</td><td>★★★☆☆</td></tr>
        <tr><td>Phi-3 Mini 4B</td><td>3.8B</td><td>极端低延迟场景</td><td>★★★☆☆</td></tr>
        <tr><td>Cohere Command R+</td><td>104B</td><td>RAG、检索增强</td><td>★★★☆☆</td></tr>
    </tbody>
</table>

<p><strong>特别推荐：</strong>Llama 4 Scout和Qwen3 32B是免费版性能最强的两个模型。Llama 4 Scout在英文和代码任务上表现优异，而Qwen3 32B在中文理解和复杂推理方面最为出色。</p>

<h2>API使用方法</h2>

<h3>1. 获取API Key</h3>

<p>访问 <a href="https://console.groq.com/" target="_blank">Groq控制台</a>，注册账号后即可获得API Key。免费版无需绑定信用卡，注册即用。</p>

<h3>2. Python调用示例</h3>

<pre><code># 安装：pip install groq
from groq import Groq

client = Groq(api_key="YOUR_API_KEY")

# 使用Llama 4 Scout
chat_completion = client.chat.completions.create(
    model="llama4-sculpt-20260901",
    messages=[{"role": "user", "content": "请解释Transformer架构的核心组件"}],
    temperature=0.7,
    stream=True,  # 流式输出，享受极速体验
)

for chunk in chat_completion:
    print(chunk.choices[0].delta.content or "", end='')
</code></pre>

<h3>3. OpenAI兼容调用</h3>

<p>由于Groq完全兼容OpenAI API格式，你可以直接使用openai库进行调用：</p>

<pre><code>from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="YOUR_API_KEY",
)

response = client.chat.completions.create(
    model="llama4-sculpt-20260901",
    messages=[{"role": "user", "content": "你好世界！"}],
)

print(response.choices[0].message.content)
</code></pre>

<h2>实战应用场景</h2>

<h3>1. 实时客服对话系统</h3>

<p>Groq的低延迟特性使其成为实时对话应用的理想选择。基于Llama 4 Scout构建的客服机器人可以实现接近实时的响应，首token延迟通常低于100ms，给用户带来流畅的对话体验。</p>

<h3>2. 编程助手</h3>

<p>结合Qwen3 32B或Llama 4 Scout，可以打造强大的编程辅助工具。包括代码补全、错误诊断、代码翻译、单元测试生成等功能。由于Groq支持流式输出，IDE插件可以实现类似Copilot的实时代码建议。</p>

<h3>3. 语音转文字处理</h3>

<p>Whisper语音识别模型可以与Groq的LLM结合，构建完整的语音理解流水线：先通过Whisper将语音转换为文本，再通过Groq进行语义理解和回复生成，整体延迟极低。</p>

<h3>4. 教育辅导系统</h3>

<p>交互式教育应用可以从Groq的高速推理中受益。学生提问后几乎立即得到解答，支持多轮追问和详细解释，特别适合作为AI tutor的后端推理引擎。</p>

<h2>免费 vs 付费对比</h2>

<table>
    <thead>
        <tr><th>特性</th><th>免费版</th><th>付费版（按需）</th></tr>
    </thead>
    <tbody>
        <tr><td>每日请求配额</td><td>1000次</td><td>无限制（按用量计费）</td></tr>
        <tr><td>价格</td><td>免费</td><td>Llama 3.1 70B: $1/M输入 tokens, $5/M输出 tokens</td></tr>
        <tr><td>模型选择</td><td>17个开源模型</td><td>全部可用模型（含闭源模型）</td></tr>
        <tr><td>商业用途</td><td>✓ 允许</td><td>✓ 允许</td></tr>
        <tr><td>RPM限制</td><td>30</td><td>更高（根据套餐）</td></tr>
        <tr><td>TPM限制</td><td>30000</td><td>更高</td></tr>
        <tr><td>并发连接</td><td>有限</td><td>更多</td></tr>
    </tbody>
</table>

<h2>使用技巧和注意事项</h2>

<ul>
    <li><strong>模型选择：</strong>根据任务需求选择合适的模型。快速简单任务用Gemma 2或Phi-3，复杂任务用Llama 4 Hunter或Qwen 3 32B</li>
    <li><strong>流式输出：</strong>务必设置stream=True，这是发挥LPU速度优势的关键</li>
    <li><strong>上下文窗口：</strong>不同模型支持的最大上下文不同，Llama 4 Hunter支持最高256K Token</li>
    <li><strong>网络要求：</strong>Groq服务位于美国，中国大陆用户需要VPN才能正常访问</li>
    <li><strong>错误处理：</strong>建议在代码中实现重试机制，应对偶尔的请求失败</li>
    <li><strong>额度监控：</strong>可以通过Groq控制台查看当日剩余请求数</li>
</ul>

<h2>FAQ</h2>

<div class="faq-section">
    <h3>常见问题</h3>
    
    <div class="faq-item">
        <div class="faq-q">Q: Groq免费版需要付费吗？</div>
        <div class="faq-a">A: Groq的免费版完全免费，无需支付任何费用。注册后即可使用，不需要绑定信用卡。</div>
    </div>

    <div class="faq-item">
        <div class="faq-q">Q: 1000次请求每天够用吗？</div>
        <div class="faq-a">A: 对于大多数个人开发者和小项目来说完全足够。假设每个用户每天使用10次，1000次请求可以满足100个日活用户的需要。</div>
    </div>

    <div class="faq-item">
        <div class="faq-q">Q: Groq支持中文吗？</div>
        <div class="faq-a">A: 支持。Qwen系列模型在中文理解方面表现优秀，Llama 4也支持多语言对话。</div>
    </div>

    <div class="faq-item">
        <div class="faq-q">Q: 需要翻墙才能使用吗？</div>
        <div class="faq-a">A: 是的，Groq的服务位于美国，中国大陆地区用户需要VPN才能正常访问。</div>
    </div>

    <div class="faq-item">
        <div class="faq-q">Q: 能否用于商业项目？</div>
        <div class="faq-a">A: 可以，Groq的免费版明确允许商业用途。</div>
    </div>

    <div class="faq-item">
        <div class="faq-q">Q: 如何监控免费额度使用情况？</div>
        <div class="faq-a">A: 登录Groq控制台（console.groq.com）可以查看当日的请求使用情况和剩余额度。</div>
    </div>
</div>

<h2>总结</h2>

<p>Groq凭借其自研LPU硬件架构，提供了目前市面上最快的免费推理服务。每天1000次的免费额度配合17个主流开源模型，为开发者提供了一个极低的门槛来体验高性能的大语言模型。无论是构建实时聊天应用、编程助手还是其他需要快速响应的大模型应用场景，Groq都值得作为首选方案。特别是对于需要从GPU推理迁移到更低延迟方案的开发者，Groq提供了平滑的迁移路径——只需更改base URL即可，代码无需修改。</p>
"""

    content_en = """<h1>Groq Free LPU Inference API: 1000 Daily Requests with Fastest Open Source Models</h1>

<p>In June 2026, Groq's free LPU inference service continues to lead the industry with <strong>unmatched response speeds</strong>. As currently the fastest free inference engine available to the public, Groq's self-designed LPU (Language Processing Unit) architecture delivers inference speeds several times faster than traditional GPU solutions. The free tier offers <strong>1000 daily free requests</strong> with <strong>17 mainstream open-source models</strong>, including Llama 4, Qwen, and Mixtral. For real-time dialogue applications, streaming text generation, and other scenarios requiring low-latency responses, Groq remains the most recommended free inference platform.</p>

<h2>Core Technical Advantages of Groq</h2>

<p>Groq's core competitive advantage lies in its self-designed LPU hardware architecture. Compared to traditional GPU-based inference solutions, the LPU uses a deterministic architecture and streaming compiler technology that eliminates random memory access bottlenecks in GPUs, achieving near-zero latency token output.</p>

<ul>
    <li><strong>Hardware Architecture:</strong> Self-designed LPU (Language Processing Unit), not GPU-based</li>
    <li><strong>Response Speed:</strong> Average first-token latency <50ms, maximum throughput 300 TPM (Tokens Per Minute)</li>
    <li><strong>Concurrency Capability:</strong> Supports parallel computation across multiple models in single requests</li>
    <li><strong>Model Count:</strong> Free tier provides access to 17 open-source models</li>
    <li><strong>Free Quota:</strong> 1000 requests per day (reset daily)</li>
    <li><strong>Rate Limits:</strong> RPM 30 (30 requests per minute), TPM 30000</li>
    <li><strong>Commercial Use:</strong> Free tier permits commercial use</li>
    <li><strong>API Compatibility:</strong> Fully compatible with OpenAI API format</li>
</ul>

<h2>Free Tier Details</h2>

<h3>1. Request Limit</h3>

<p>Free users receive <strong>1000 free requests per day</strong>, reset at UTC midnight. This quota is more than sufficient for individual developers and small projects — assuming each conversation consumes approximately 2 requests (one encoding + one decoding), 1000 requests can support about 500 conversations per day.</p>

<table>
    <thead>
        <tr><th>Use Case</th><th>Request Consumption Per Use</th><th>1000 Quota Capacity</th></tr>
    </thead>
    <tbody>
        <tr><td>Simple text Q&A (short messages)</td><td>1 request</td><td>1000 conversations</td></tr>
        <tr><td>Code generation (medium length)</td><td>2-3 requests</td><td>300-500 conversations</td></tr>
        <tr><td>Long document summarization (8K context)</td><td>3-5 requests</td><td>200-300 conversations</td></tr>
        <tr><td>Real-time chat (ongoing dialogue)</td><td>1-2 requests/per turn</td><td>500-1000 turns</td></tr>
    </tbody>
</table>

<h3>2. Rate Limits</h3>

<p>The free tier has two concurrent rate limits:<br>
• <strong>RPM 30:</strong> Maximum 30 requests per minute<br>
• <strong>TPM 30000:</strong> Maximum 30000 output tokens per minute</p>

<p>These limits rarely become bottlenecks. Even when generating with Llama 3.1 70B at 5-10 tokens per second, TPM 30000 allows up to 5000 full tokens per minute — already very high throughput. The RPM 30 limit means maximum 5 requests per second, which is sufficient for virtually all use cases.</p>

<h3>3. Concurrent Connections</h3>

<p>The free tier limits simultaneous connections. Implement local rate limiting in production code. Upgrade to paid plans for higher concurrency needs.</p>

<h2>Available Free Models</h2>

<p>The Groq free tier offers <strong>17 mainstream open-source models</strong>. Here are the top recommendations:</p>

<table>
    <thead>
        <tr><th>Model Name</th><th>Parameter Scale</th><th>Best Use Case</th><th>Rating</th></tr>
    </thead>
    <tbody>
        <tr><td>Llama 4 Scout</td><td>~25B</td><td>General conversation, code generation</td><td>★★★★★</td></tr>
        <tr><td>Qwen3 32B</td><td>32B</td><td>Chinese understanding, complex reasoning</td><td>★★★★★</td></tr>
        <tr><td>Llama 4 Hunter</td><td>~70B</td><td>High-precision tasks, long context</td><td>★★★★☆</td></tr>
        <tr><td>Mixtral 8x22B</td><td>MoE 129B</td><td>High-throughput scenarios</td><td>★★★★☆</td></tr>
        <tr><td>Gemma 2 9B</td><td>9B</td><td>Fast response, lightweight tasks</td><td>★★★☆☆</td></tr>
        <tr><td>Phi-3 Mini 4B</td><td>3.8B</td><td>Extreme low-latency scenarios</td><td>★★★☆☆</td></tr>
        <tr><td>Cohere Command R+</td><td>104B</td><td>RAG, retrieval-enhanced generation</td><td>★★★☆☆</td></tr>
    </tbody>
</table>

<p><strong>Top Recommendations:</strong> Llama 4 Scout and Qwen3 32B are the highest-performing free models. Llama 4 Scout excels at English and coding tasks, while Qwen3 32B leads in Chinese understanding and complex reasoning.</p>

<h2>API Usage</h2>

<h3>1. Obtain API Key</h3>

<p>Visit the <a href="https://console.groq.com/" target="_blank">Groq Console</a>, register an account, and obtain your API Key. The free tier requires no credit card registration — start immediately after signing up.</p>

<h3>2. Python Example</h3>

<pre><code># Install: pip install groq
from groq import Groq

client = Groq(api_key="YOUR_API_KEY")

# Use Llama 4 Scout
chat_completion = client.chat.completions.create(
    model="llama4-sculpt-20260901",
    messages=[{"role": "user", "content": "Explain the core components of Transformer architecture"}],
    temperature=0.7,
    stream=True,  # Streaming output for best performance
)

for chunk in chat_completion:
    print(chunk.choices[0].delta.content or "", end='')
</code></pre>

<h3>3. OpenAI-Compatible Call</h3>

<p>Since Groq fully supports the OpenAI API format, you can use the OpenAI library directly:</p>

<pre><code>from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="YOUR_API_KEY",
)

response = client.chat.completions.create(
    model="llama4-sculpt-20260901",
    messages=[{"role": "user", "content": "Hello world!"}]
)

print(response.choices[0].message.content)
</code></pre>

<h2>Practical Application Scenarios</h2>

<h3>1. Real-Time Customer Service Chatbots</h3>

<p>Groq's low latency makes it ideal for real-time conversation applications. A customer service bot built on Llama 4 Scout can achieve near-real-time response with first-token latency typically under 100ms, providing smooth conversational experiences.</p>

<h3>2. Programming Assistants</h3>

<p>Combined with Qwen3 32B or Llama 4 Scout, powerful programming assistants can be created including code completion, error diagnosis, code translation, and unit test generation. Since Groq supports streaming, IDE plugins can offer real-time code suggestions similar to Copilot.</p>

<h3>3. Speech-to-Text Processing</h3>

<p>The Whisper speech recognition model can be combined with Groq LLMs to build complete voice understanding pipelines: first convert speech to text via Whisper, then perform semantic understanding and response generation via Groq, achieving extremely low overall latency.</p>

<h3>4. Educational Tutoring Systems</h3>

<p>Interactive education applications benefit greatly from Groq's fast inference. Students receive immediate answers to their questions, supporting multi-turn questioning and detailed explanations, making Groq an excellent backend inference engine for AI tutors.</p>

<h2>Free vs Paid Comparison</h2>

<table>
    <thead>
        <tr><th>Feature</th><th>Free Tier</th><th>Paid (Pay-as-you-go)</th></tr>
    </thead>
    <tbody>
        <tr><td>Daily Request Quota</td><td>1000 requests</td><td>Unlimited (pay per usage)</td></tr>
        <tr><td>Price</td><td>Free</td><td>Llama 3.1 70B: $1/M input tokens, $5/M output tokens</td></tr>
        <tr><td>Model Selection</td><td>17 open-source models</td><td>All models (including closed-source)</td></tr>
        <tr><td>Commercial Use</td><td>✓ Allowed</td><td>✓ Allowed</td></tr>
        <tr><td>RPM Limit</td><td>30</td><td>Higher (based on plan)</td></tr>
        <tr><td>TPM Limit</td><td>30000</td><td>Higher</td></tr>
        <tr><td>Concurrent Connections</td><td>Limited</td><td>More</td></tr>
    </tbody>
</table>

<h2>Tips and Best Practices</h2>

<ul>
    <li><strong>Model Selection:</strong> Choose appropriate models based on task requirements. Fast lightweight tasks use Gemma 2 or Phi-3; complex tasks use Llama 4 Hunter or Qwen3 32B</li>
    <li><strong>Streaming Output:</strong> Always enable stream=True — this is key to leveraging LPU speed advantages</li>
    <li><strong>Context Window:</strong> Different models support different maximum contexts; Llama 4 Hunter supports up to 256K tokens</li>
    <li><strong>Network Requirements:</strong> Groq services are hosted in the US; mainland China users require VPN access</li>
    <li><strong>Error Handling:</strong> Implement retry mechanisms in code to handle occasional request failures</li>
    <li><strong>Quota Monitoring:</strong> Check remaining daily requests via the Groq console</li>
</ul>

<h2>FAQ</h2>

<div class="faq-section">
    <h3>Frequently Asked Questions</h3>
    
    <div class="faq-item">
        <div class="faq-q">Q: Is Groq's free tier actually free?</div>
        <div class="faq-a">A: Yes, Groq's free tier is completely free with no payment required. No credit card needed — start immediately after registration.</div>
    </div>

    <div class="faq-item">
        <div class="faq-q">Are 1000 daily requests enough?</div>
        <div class="faq-a">A: Absolutely for most individual developers and small projects. Assuming 10 requests per user per day, 1000 requests supports 100 daily active users.</div>
    </div>

    <div class="faq-item">
        <div class="faq-q">Does Groq support Chinese?</div>
        <div class="faq-a">A: Yes. Qwen series models excel at Chinese understanding, and Llama 4 also supports multilingual conversation.</div>
    </div>

    <div class="faq-item">
        <div class="faq-q">Do I need a VPN to use Groq?</div>
        <div class="faq-a">A: Yes, Groq services are hosted in the US; users in mainland China need VPN access to connect normally.</div>
    </div>

    <div class="faq-item">
        <div class="faq-q">Can I use it for commercial projects?</div>
        <div class="faq-a">A: Yes, Groq's free tier explicitly permits commercial use.</div>
    </div>

    <div class="faq-item">
        <div class="faq-q">How do I monitor free quota usage?</div>
        <div class="faq-a">A: Log into the Groq Console (console.groq.com) to view daily request usage and remaining quota.</div>
    </div>
</div>

<h2>Summary</h2>

<p>Groq, leveraging its self-designed LPU hardware architecture, provides the fastest free inference service currently available. With 1000 daily free requests and access to 17 mainstream open-source models, Groq offers an exceptionally low barrier to entry for experiencing high-performance large language models. Whether building real-time chat applications, programming assistants, or other large-model applications requiring fast response times, Groq deserves to be the first choice. Particularly for developers migrating from GPU-based inference to lower-latency solutions, Groq provides a seamless migration path — only the base URL needs changing, with no code modifications required.</p>
"""

    faq_zh = '''{"type":"问答","question":"Groq免费版需要付费吗？","回答":"Groq的免费版完全免费，无需支付任何费用。注册后即可使用，不需要绑定信用卡。"}|{"type":"问答","question":"1000次请求每天够用吗？","回答":"对于大多数个人开发者和小项目来说完全足够。假设每个用户每天使用10次，1000次请求可以满足100个日活用户的需要。"}|{"type":"问答","question":"Groq支持中文吗？","回答":"支持。Qwen系列模型在中文理解方面表现优秀，Llama 4也支持多语言对话。"}|{"type":"问答","question":"需要翻墙才能使用吗？","回答":"是的，Groq的服务位于美国，中国大陆地区用户需要VPN才能正常访问。"}|{"type":"问答","question":"能否用于商业项目？","回答":"可以，Groq的免费版明确允许商业用途。"}|{"type":"问答","question":"如何监控免费额度使用情况？","回答":"登录Groq控制台(console.groq.com)可以查看当日的请求使用情况和剩余额度。'}'''

    faq_en = '''{"type":"question_answer","question":"Is Groq\'s free tier actually free?","answer":"Yes, Groq\'s free tier is completely free with no payment required. No credit card needed — start immediately after registration."}|{"type":"question_answer","question":"Are 1000 daily requests enough?","answer":"Absolutely for most individual developers and small projects. Assuming 10 requests per user per day, 1000 requests supports 100 daily active users."}|{"type":"question_answer","question":"Does Groq support Chinese?","answer":"Yes. Qwen series models excel at Chinese understanding, and Llama 4 also supports multilingual conversation."}|{"type":"question_answer","question":"Do I need a VPN to use Groq?","answer":"Yes, Groq services are hosted in the US; users in mainland China need VPN access to connect normally."}|{"type":"question_answer","question":"Can I use it for commercial projects?","answer":"Yes, Groq\'s free tier explicitly permits commercial use."}|{"type":"question_answer","question":"How do I monitor free quota usage?","answer":"Log into the Groq Console (console.groq.com) to view daily request usage and remaining quota."}'''

    zh_html, en_html = generate_guide_html(
        slug, title_zh, title_en, desc_zh, desc_en,
        content_zh, content_en, faq_zh, faq_en, today
    )

    # Write files
    os.makedirs('/home/ubuntu/aifreeplan/zh/guides', exist_ok=True)
    os.makedirs('/home/ubuntu/aifreeplan/en/guides', exist_ok=True)

    with open(f'/home/ubuntu/aifreeplan/zh/guides/{slug}.html', 'w', encoding='utf-8') as f:
        f.write(zh_html)

    with open(f'/home/ubuntu/aifreeplan/en/guides/{slug}.html', 'w', encoding='utf-8') as f:
        f.write(en_html)

    print(f"✅ 已生成:")
    print(f"  - /zh/guides/{slug}.html")
    print(f"  - /en/guides/{slug}.html")
    print(f"  - 日期: {today}")

if __name__ == '__main__':
    main()