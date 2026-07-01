#!/usr/bin/env python3
"""Generate and save a guide article directly."""
import os
import sys
from datetime import datetime

def main():
    today = datetime.now().strftime('%Y-%m-%d')
    slug = "nano-banana-2-lite-free-image-generation"
    
    title_zh = "Nano Banana 2 Lite 完全免费：Google DeepMind 最快 AI 图片生成工具"
    title_en = "Nano Banana 2 Lite Free: Google DeepMind's Fastest AI Image Generator"
    desc_zh = "Google DeepMind 发布 Gemini 3.1 Flash-Lite Image（代号 Nano Banana 2 Lite），完全免费通过 Google AI Studio 使用，速度比前代快数倍，成本降低至最低，支持 4K 分辨率图像生成与编辑。"
    desc_en = "Google DeepMind released Gemini 3.1 Flash-Lite Image (codenamed Nano Banana 2 Lite), completely free via Google AI Studio. It's the fastest and cheapest Gemini image model, supporting 4K resolution generation and editing."
    
    content_zh = """<h1>Nano Banana 2 Lite 完全免费：Google DeepMind 最快 AI 图片生成工具</h1>

<p>2026年6月30日，Google DeepMind 发布了 <strong>Gemini 3.1 Flash-Lite Image</strong>（内部代号 <strong>Nano Banana 2 Lite</strong>），这是目前市面上速度最快、成本最低的 AI 图像生成模型。它可以通过 <strong>Google AI Studio</strong> 和 <strong>Gemini App</strong> 完全免费使用，无需任何付费计划。</p>

<h2>什么是 Nano Banana 2 Lite？</h2>

<p>Nano Banana 2 Lite 是 Google DeepMind 旗下 Gemini 图像模型的轻量级版本，属于 Gemini 3.1 系列。它的核心定位是：<strong>在保持高质量输出的同时，提供极速生成速度和最低成本</strong>。以下是关键参数：</p>

<ul>
<li><strong>模型名称：</strong>Gemini 3.1 Flash-Lite Image</li>
<li><strong>代号：</strong>Nano Banana 2 Lite</li>
<li><strong>所属系列：</strong>Gemini 3.1</li>
<li><strong>最大分辨率：</strong>最高 4K（4096×4096 像素）</li>
<li><strong>输出定价：</strong>$0.076 每张 4K 图片（API 付费档），<strong>Google AI Studio 免费使用</strong></li>
<li><strong>速度等级：</strong>Flash-Lite（系列中最快）</li>
<li><strong>特点：</strong>低延迟、高吞吐量、角色一致性保持</li>
</ul>

<h2>免费使用方式</h2>

<p>Nano Banana 2 Lite 有<strong>两种免费使用途径</strong>：</p>

<h3>方式一：Google AI Studio（推荐）</h3>

<p><a href="https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-image">访问 Google AI Studio</a>，选择 Gemini 3.1 Flash-Lite Image 模型即可开始免费生成图片。这是最直接的免费方式，无需配置 API Key。</p>

<p>Google AI Studio 的免费额度非常慷慨：<strong>每月 1,500 次请求（RPD）</strong>用于 Grounding 功能，且文本和图片生成的输入输出 Token 全部免费。对于普通用户来说，这个额度绰绰有余。</p>

<h3>方式二：Gemini App 的 Flash-Lite 模式</h3>

<p>在 Google Gemini App 中，切换到 Flash-Lite 模式即可使用 Nano Banana 2 Lite 进行图片生成。这种方式更适合移动端用户，随时随地创作。</p>

<h2>与 Nano Banana 2 的对比</h2>

<p>Nano Banana 2 Lite 并不是 Nano Banana 2 的"缩水版"，而是<strong>针对速度和成本优化的独立模型</strong>。根据 Google DeepMind 官方数据：</p>

<table>
<tr><th>特性</th><th>Nano Banana 2 Lite</th><th>Nano Banana 2</th></tr>
<tr><td>速度</td><td>⚡ 最快（Flash-Lite）</td><td>🐢 较慢（标准）</td></tr>
<tr><td>成本</td><td>最低（$0.076/张 4K）</td><td>较高</td></tr>
<tr><td>图像质量</td><td>高（Elo 评分接近 Nano Banana 2）</td><td>最高</td></tr>
<tr><td>角色一致性</td><td>✅ 支持</td><td>✅ 支持</td></tr>
<tr><td>图像编辑</td><td>✅ 支持</td><td>✅ 支持</td></tr>
<tr><td>实时应用</td><td>✅ 适合（低延迟）</td><td>❌ 不适合</td></tr>
</table>

<p>根据 Arena AI 的评测数据，Nano Banana 2 Lite 在图像生成的 Elo 评分上<strong>非常接近完整版 Nano Banana 2</strong>，但在延迟和成本方面优势显著。这意味着你用更少的钱（甚至免费）就能获得几乎相同的质量。</p>

<h2>实际应用场景</h2>

<p>Nano Banana 2 Lite 的设计目标就是<strong>"从想法到图片只需几秒"</strong>。以下是几个典型应用场景：</p>

<h3>1. 室内设计快速原型</h3>
<p>像 Space Lift 这样的应用，用户上传房间照片后，可以瞬间生成多种风格（Mid-Century Modern、Bohemian Chic 等）的设计方案。由于生成速度快，用户可以连续尝试数十种方案而不必等待。</p>

<h3>2. 教育可视化</h3>
<p>Peek-A-Word 应用将选定文本自动转换为 AI 生成的插图，配合简明定义，在学习过程中不打断阅读流。Nano Banana 2 Lite 的低延迟让这个过程几乎是实时的。</p>

<h3>3. 游戏和实时应用</h3>
<p>Gridscape 等应用利用 Nano Banana 2 Lite 和 Gemini 3.1 Flash-Lite 文本模型，在用户提问时即时生成信息节点和配图，创建无限探索的知识画布。</p>

<h3>4. 批量内容生成</h3>
<p>由于成本极低（4K 图片仅 $0.076），开发者可以用它来为应用批量生成占位图、缩略图和素材，成本远低于其他模型。</p>

<h2>技术亮点</h2>

<h3>1. 极致速度</h3>
<p>Nano Banana 2 Lite 的延迟相比前代大幅降低。根据 artificialanalysis.ai 的数据，它在每千次 1K 分辨率图像的延迟上表现最优。Manus AI 的联合创始人 Tao Zhang 评价道：<strong>"速度不再是瓶颈。当生成速度快于想象时，创作者可以保持在创意流中。"</strong></p>

<h3>2. 角色一致性</h3>
<p>即使是在快速模式下，Nano Banana 2 Lite 仍然能够保持角色的一致性。这对于需要多张图片中同一角色的场景（如漫画、故事板）非常重要。</p>

<h3>3. 图像编辑能力</h3>
<p>除了从零生成图片，Nano Banana 2 Lite 还支持图像编辑。你可以上传现有图片并要求模型进行修改，比如改变风格、调整构图或修改特定元素。</p>

<h3>4. SynthID 数字水印</h3>
<p>所有由 Nano Banana 2 系列生成的图片都嵌入了 Google 的 <strong>SynthID</strong> 隐形数字水印。这可以在不改变图片外观的情况下，将图片标识为 AI 生成内容。</p>

<h2>API 定价详解</h2>

<p>如果你通过 Gemini API 使用（而非免费的 Google AI Studio），以下是付费定价：</p>

<table>
<tr><th>输出分辨率</th><th>Token 消耗</th><th>单张图片价格</th></tr>
<tr><td>0.5K (512px)</td><td>747 tokens</td><td>约 $0.045</td></tr>
<tr><td>1K (1024×1024)</td><td>1,120 tokens</td><td>约 $0.067</td></tr>
<tr><td>2K (2048×2048)</td><td>1,680 tokens</td><td>约 $0.101</td></tr>
<tr><td>4K (4096×4096)</td><td>2,520 tokens</td><td>约 $0.151</td></tr>
</table>

<p>作为对比，完整版 Nano Banana 2 的 4K 图片价格约为 $0.101-$0.151，而 Nano Banana 2 Lite 的价格更低。但最重要的是——<strong>通过 Google AI Studio 完全免费</strong>。</p>

<h2>如何使用（详细步骤）</h2>

<h3>步骤 1：访问 Google AI Studio</h3>
<p>打开 <a href="https://aistudio.google.com">Google AI Studio</a>，用你的 Google 账号登录。</p>

<h3>步骤 2：选择模型</h3>
<p>在左侧模型选择器中，找到并选择 <strong>Gemini 3.1 Flash-Lite Image</strong>（可能显示为 "gemini-3.1-flash-lite-image"）。</p>

<h3>步骤 3：编写提示词</h3>
<p>在右侧输入框中，用英文或中文描述你想要的图片。提示词越详细，生成效果越好。例如：</p>
<ul>
<li><strong>中文：</strong>"一只穿着太空服的猫坐在火星表面，背景是地球和星空，赛博朋克风格"</li>
<li><strong>英文：</strong>"A cat in a spacesuit sitting on Mars surface, Earth and starry sky in the background, cyberpunk style"</li>
</ul>

<h3>步骤 4：生成图片</h3>
<p>点击发送按钮，Nano Banana 2 Lite 会在几秒内生成图片。如果需要调整，修改提示词后重新生成即可。</p>

<h2>与其他免费 AI 图片生成工具对比</h2>

<table>
<tr><th>工具</th><th>免费额度</th><th>速度</th><th>最大分辨率</th><th>需要注册</th></tr>
<tr><td><strong>Nano Banana 2 Lite</strong></td><td>✅ 完全免费（AI Studio）</td><td>⚡ 极快</td><td>4K</td><td>Google 账号</td></tr>
<tr><td>DALL·E 3</td><td>$15/月（ChatGPT Plus）</td><td>中等</td><td>1024×1024</td><td>✅ 需要</td></tr>
<tr><td>Stable Diffusion（Web 版）</td><td>有限免费</td><td>慢</td><td>1024×1024</td><td>✅ 需要</td></tr>
<tr><td>Leonardo.ai</td><td>150 积分/天</td><td>中等</td><td>1024×1024</td><td>✅ 需要</td></tr>
<tr><td>Adobe Firefly</td><td>25 生成积分/月</td><td>中等</td><td>2048×2048</td><td>✅ 需要</td></tr>
</table>

<p>可以看到，Nano Banana 2 Lite 在<strong>速度、分辨率和免费额度</strong>三个维度上都具有明显优势。</p>

<h2>常见问题</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: Nano Banana 2 Lite 真的完全免费吗？</div>
<div class="faq-a">是的，通过 Google AI Studio 使用是完全免费的。Google AI Studio 提供免费层的输入和输出 Token，每月有 generous 的请求配额。对于绝大多数个人用户来说，免费额度足够日常使用。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 生成的图片可以用于商业用途吗？</div>
<div class="faq-a">Google AI Studio 生成的图片遵循 Google 的服务条款。建议在使用前查阅最新的 Google AI Studio Terms of Service 以确认商业使用权。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Nano Banana 2 Lite 和 Nano Banana 2 有什么区别？</div>
<div class="faq-a">Nano Banana 2 Lite 是为速度和成本优化的版本，生成速度更快、单次成本更低，但图像质量与完整版 Nano Banana 2 非常接近（Elo 评分差距很小）。如果你需要极致质量且不关心速度，可以选择完整版；如果需要快速迭代，Lite 是更好的选择。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 支持哪些语言写提示词？</div>
<div class="faq-a">Gemini 模型支持多语言提示词，包括中文、英文、日文等。不过使用英文提示词通常能获得更精确的结果。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 图片上有水印吗？</div>
<div class="faq-a">Nano Banana 2 系列生成的图片嵌入了 SynthID 隐形数字水印，用于标识 AI 生成内容。这种水印肉眼不可见，但可以被检测工具识别。</div>
</div>
</div>

<h2>总结</h2>

<p>Nano Banana 2 Lite（Gemini 3.1 Flash-Lite Image）是 2026 年最值得关注的免费 AI 图片生成工具。它由 Google DeepMind 开发，通过 Google AI Studio 完全免费使用，速度系列最快，支持高达 4K 分辨率，并且具备图像编辑和角色一致性等高级功能。</p>

<p>无论你是设计师、开发者还是普通用户，都值得一试。立即前往 <a href="https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-image">Google AI Studio</a> 体验吧！</p>
"""

    content_en = """<h1>Nano Banana 2 Lite Free: Google DeepMind's Fastest AI Image Generator</h1>

<p>On June 30, 2026, Google DeepMind released <strong>Gemini 3.1 Flash-Lite Image</strong> (codename <strong>Nano Banana 2 Lite</strong>), currently the fastest and most cost-effective AI image generation model on the market. It is available <strong>completely free</strong> through Google AI Studio and the Gemini App, with no paid plan required.</p>

<h2>What is Nano Banana 2 Lite?</h2>

<p>Nano Banana 2 Lite is the lightweight version of Google DeepMind's Gemini image model, part of the Gemini 3.1 series. Its core positioning: <strong>deliver high-quality image generation with blazing speed and minimal cost</strong>. Here are the key specs:</p>

<ul>
<li><strong>Model Name:</strong> Gemini 3.1 Flash-Lite Image</li>
<li><strong>Codename:</strong> Nano Banana 2 Lite</li>
<li><strong>Series:</strong> Gemini 3.1</li>
<li><strong>Max Resolution:</strong> Up to 4K (4096×4096 pixels)</li>
<li><strong>Output Pricing:</strong> $0.076 per 4K image (paid API tier), <strong>FREE on Google AI Studio</strong></li>
<li><strong>Speed Tier:</strong> Flash-Lite (fastest in the series)</li>
<li><strong>Features:</strong> Low latency, high throughput, character consistency</li>
</ul>

<h2>How to Use It for Free</h2>

<p>Nano Banana 2 Lite offers <strong>two free access methods</strong>:</p>

<h3>Method 1: Google AI Studio (Recommended)</h3>

<p><a href="https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-image">Visit Google AI Studio</a>, select the Gemini 3.1 Flash-Lite Image model, and start generating images for free. This is the most straightforward free method — no API key configuration needed.</p>

<p>Google AI Studio's free tier is very generous: <strong>up to 1,500 requests per day</strong> for Grounding features, and all text and image generation input/output tokens are free. For most individual users, this quota is more than sufficient.</p>

<h3>Method 2: Gemini App's Flash-Lite Mode</h3>

<p>In the Google Gemini App, switch to Flash-Lite mode to use Nano Banana 2 Lite for image generation. This is ideal for mobile users who want to create on the go.</p>

<h2>Nano Banana 2 Lite vs. Nano Banana 2</h2>

<p>Nano Banana 2 Lite is <strong>not a "downgraded" version</strong> of Nano Banana 2 — it's an independently optimized model focused on speed and cost. According to Google DeepMind's official data:</p>

<table>
<tr><th>Feature</th><th>Nano Banana 2 Lite</th><th>Nano Banana 2</th></tr>
<tr><td>Speed</td><td>⚡ Fastest (Flash-Lite)</td><td>🐢 Slower (Standard)</td></tr>
<tr><td>Cost</td><td>Lowest ($0.076/4K image)</td><td>Higher</td></tr>
<tr><td>Image Quality</td><td>High (Elo score near Nano Banana 2)</td><td>Highest</td></tr>
<tr><td>Character Consistency</td><td>✅ Supported</td><td>✅ Supported</td></tr>
<tr><td>Image Editing</td><td>✅ Supported</td><td>✅ Supported</td></tr>
<tr><td>Real-time Apps</td><td>✅ Ideal (low latency)</td><td>❌ Not suitable</td></tr>
</table>

<p>According to Arena AI benchmark data, Nano Banana 2 Lite's Elo score for image generation is <strong>very close to the full Nano Banana 2</strong>, while offering significantly better latency and cost. This means you get nearly identical quality at a fraction of the cost — or completely free.</p>

<h2>Real-World Use Cases</h2>

<p>Nano Banana 2 Lite was designed for the goal of <strong>"from idea to image in seconds."</strong> Here are typical scenarios:</p>

<h3>1. Interior Design Rapid Prototyping</h3>
<p>Apps like Space Lift let users upload a room photo and instantly generate multiple design concepts ranging from Mid-Century Modern to Bohemian Chic. Because generation is so fast, users can try dozens of variations without waiting.</p>

<h3>2. Educational Visualization</h3>
<p>The Peek-A-Word app automatically converts selected text into AI-generated illustrations paired with concise definitions. Nano Banana 2 Lite's low latency makes this process nearly real-time, keeping students in their learning flow.</p>

<h3>3. Games and Real-time Applications</h3>
<p>Gridscape uses Nano Banana 2 Lite combined with the Gemini 3.1 Flash-Lite text model to instantly generate informational nodes and images when users ask questions, creating an infinitely explorable knowledge canvas.</p>

<h3>4. Bulk Content Generation</h3>
<p>With extremely low cost (4K images at just $0.076), developers can use it to bulk-generate placeholder images, thumbnails, and assets for applications — far cheaper than any competing model.</p>

<h2>Technical Highlights</h2>

<h3>1. Blazing Speed</h3>
<p>Nano Banana 2 Lite dramatically reduces latency compared to previous generations. According to artificialanalysis.ai data, it achieves the best latency per 1K resolution image in its class. Tao Zhang, Co-Founder & CEO of Manus AI, stated: <strong>"Speed is no longer a limitation. When generation is faster than imagination, creators stay inside the idea instead of waiting on the tool."</strong></p>

<h3>2. Character Consistency</h3>
<p>Even in fast mode, Nano Banana 2 Lite maintains character consistency across multiple images. This is crucial for scenarios requiring the same character across multiple images, such as comics, storyboards, and game assets.</p>

<h3>3. Image Editing</h3>
<p>Beyond generating images from scratch, Nano Banana 2 Lite supports image editing. You can upload an existing image and ask the model to modify it — changing style, adjusting composition, or altering specific elements.</p>

<h3>4. SynthID Digital Watermark</h3>
<p>All images generated by the Nano Banana 2 series include Google's <strong>SynthID</strong> invisible digital watermark. This identifies AI-generated content without affecting the visual appearance of the image.</p>

<h2>API Pricing Details</h2>

<p>If you use the Gemini API (instead of the free Google AI Studio), here is the paid pricing:</p>

<table>
<tr><th>Output Resolution</th><th>Token Consumption</th><th>Price per Image</th></tr>
<tr><td>0.5K (512px)</td><td>747 tokens</td><td>~$0.045</td></tr>
<tr><td>1K (1024×1024)</td><td>1,120 tokens</td><td>~$0.067</td></tr>
<tr><td>2K (2048×2048)</td><td>1,680 tokens</td><td>~$0.101</td></tr>
<tr><td>4K (4096×4096)</td><td>2,520 tokens</td><td>~$0.151</td></tr>
</table>

<p>For comparison, the full Nano Banana 2 charges roughly $0.101-$0.151 per 4K image, while Nano Banana 2 Lite is priced lower. But most importantly — <strong>it's completely free via Google AI Studio</strong>.</p>

<h2>How to Use (Step by Step)</h2>

<h3>Step 1: Visit Google AI Studio</h3>
<p>Go to <a href="https://aistudio.google.com">Google AI Studio</a> and sign in with your Google account.</p>

<h3>Step 2: Select the Model</h3>
<p>In the left sidebar model selector, find and select <strong>Gemini 3.1 Flash-Lite Image</strong> (may appear as "gemini-3.1-flash-lite-image").</p>

<h3>Step 3: Write Your Prompt</h3>
<p>In the right input box, describe the image you want in English or Chinese. More detailed prompts yield better results. For example:</p>
<ul>
<li><strong>Chinese:</strong> "一只穿着宇航服的猫坐在火星表面，背景是地球和星空，赛博朋克风格"</li>
<li><strong>English:</strong> "A cat in a spacesuit sitting on Mars surface, Earth and starry sky in the background, cyberpunk style"</li>
</ul>

<h3>Step 4: Generate</h3>
<p>Hit send. Nano Banana 2 Lite generates images in seconds. Adjust the prompt and regenerate as needed.</p>

<h2>Comparison with Other Free AI Image Generators</h2>

<table>
<tr><th>Tool</th><th>Free Tier</th><th>Speed</th><th>Max Resolution</th><th>Registration</th></tr>
<tr><td><strong>Nano Banana 2 Lite</strong></td><td>✅ Completely Free (AI Studio)</td><td>⚡ Extremely Fast</td><td>4K</td><td>Google Account</td></tr>
<tr><td>DALL·E 3</td><td>$15/month (ChatGPT Plus)</td><td>Medium</td><td>1024×1024</td><td>✅ Required</td></tr>
<tr><td>Stable Diffusion (Web)</td><td>Limited free</td><td>Slow</td><td>1024×1024</td><td>✅ Required</td></tr>
<tr><td>Leonardo.ai</td><td>150 credits/day</td><td>Medium</td><td>1024×1024</td><td>✅ Required</td></tr>
<tr><td>Adobe Firefly</td><td>25 credits/month</td><td>Medium</td><td>2048×2048</td><td>✅ Required</td></tr>
</table>

<p>Nano Banana 2 Lite leads in <strong>speed, resolution, and free tier generosity</strong> across all three dimensions.</p>

<h2>Frequently Asked Questions</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: Is Nano Banana 2 Lite really completely free?</div>
<div class="faq-a">Yes, it's completely free through Google AI Studio. The free tier includes free input and output tokens with generous daily request quotas. For most individual users, the free quota is sufficient for everyday use.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Can I use generated images commercially?</div>
<div class="faq-a">Images generated through Google AI Studio follow Google's Terms of Service. Check the latest Google AI Studio Terms of Service for the most up-to-date information on commercial usage rights.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: What's the difference between Nano Banana 2 Lite and Nano Banana 2?</div>
<div class="faq-a">Nano Banana 2 Lite is optimized for speed and cost. It generates images faster and cheaper, with quality very close to the full Nano Banana 2 (small Elo score gap). Choose Lite for rapid iteration; choose the full version for maximum quality when speed is not critical.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: What languages are supported for prompts?</div>
<div class="faq-a">The Gemini model supports multilingual prompts including Chinese, English, Japanese, and more. However, English prompts typically produce more precise results.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Are there watermarks on generated images?</div>
<div class="faq-a">Nano Banana 2 series images include SynthID invisible digital watermarks to identify AI-generated content. The watermark is not visible to the naked eye but can be detected by verification tools.</div>
</div>
</div>

<h2>Conclusion</h2>

<p>Nano Banana 2 Lite (Gemini 3.1 Flash-Lite Image) is the most noteworthy free AI image generation tool of 2026. Developed by Google DeepMind, it's completely free via Google AI Studio, the fastest in its series, supports up to 4K resolution, and includes advanced features like image editing and character consistency.</p>

<p>Whether you're a designer, developer, or casual user, it's worth trying. Head over to <a href="https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-image">Google AI Studio</a> and start creating!</p>
"""

    faq_zh = """{"@type":"Question","name":"Nano Banana 2 Lite 真的完全免费吗？","acceptedAnswer":{"@type":"Answer","text":"是的，通过 Google AI Studio 使用是完全免费的。Google AI Studio 提供免费层的输入和输出 Token，每月有充足的请求配额。对于绝大多数个人用户来说，免费额度足够日常使用。"}},{"@type":"Question","name":"生成的图片可以用于商业用途吗？","acceptedAnswer":{"@type":"Answer","text":"Google AI Studio 生成的图片遵循 Google 的服务条款。建议在使用前查阅最新的 Google AI Studio Terms of Service 以确认商业使用权。"}},{"@type":"Question","name":"Nano Banana 2 Lite 和 Nano Banana 2 有什么区别？","acceptedAnswer":{"@type":"Answer","text":"Nano Banana 2 Lite 是为速度和成本优化的版本，生成速度更快、单次成本更低，但图像质量与完整版 Nano Banana 2 非常接近。如果需要极致质量且不关心速度，可以选择完整版；如果需要快速迭代，Lite 是更好的选择。"}},{"@type":"Question","name":"图片上有水印吗？","acceptedAnswer":{"@type":"Answer","text":"Nano Banana 2 系列生成的图片嵌入了 SynthID 隐形数字水印，用于标识 AI 生成内容。这种水印肉眼不可见，但可以被检测工具识别。"}}"""

    faq_en = """{"@type":"Question","name":"Is Nano Banana 2 Lite really completely free?","acceptedAnswer":{"@type":"Answer","text":"Yes, it's completely free through Google AI Studio. The free tier includes free input and output tokens with generous daily request quotas. For most individual users, the free quota is sufficient for everyday use."}},{"@type":"Question","name":"Can I use generated images commercially?","acceptedAnswer":{"@type":"Answer","text":"Images generated through Google AI Studio follow Google's Terms of Service. Check the latest Google AI Studio Terms of Service for the most up-to-date information on commercial usage rights."}},{"@type":"Question","name":"What's the difference between Nano Banana 2 Lite and Nano Banana 2?","acceptedAnswer":{"@type":"Answer","text":"Nano Banana 2 Lite is optimized for speed and cost. It generates images faster and cheaper, with quality very close to the full Nano Banana 2. Choose Lite for rapid iteration; choose the full version for maximum quality when speed is not critical."}},{"@type":"Question","name":"Are there watermarks on generated images?","acceptedAnswer":{"@type":"Answer","text":"Nano Banana 2 series images include SynthID invisible digital watermarks to identify AI-generated content. The watermark is not visible to the naked eye but can be detected by verification tools."}}"""

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
