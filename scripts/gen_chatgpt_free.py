#!/usr/bin/env python3
"""Generate ChatGPT Free Tier Guide."""
import os
import sys
from datetime import datetime

sys.path.insert(0, '/home/ubuntu/aifreeplan/scripts')
from write_guide import generate_guide_html

def main():
    today = datetime.now().strftime('%Y-%m-%d')
    slug = "chatgpt-free-tier-guide-2026"

    title_zh = "ChatGPT免费使用完全攻略：GPT-4o Mini每日4次，免费版功能详解"
    title_en = "ChatGPT Free Tier Guide 2026: GPT-4o Mini Daily Access with Full Feature Breakdown"
    desc_zh = "OpenAI的ChatGPT免费版提供每日4次GPT-4o调用，支持代码解释器、文件上传、图像生成和联网搜索。本文详细介绍免费额度限制、使用技巧及如何最大化利用免费资源。"
    desc_en = "OpenAI's ChatGPT free tier provides 4 daily GPT-4o accesses with Code Interpreter, file upload, image generation, and web search. Detailed breakdown of free limits, usage tips, and how to maximize free resources."

    content_zh = """<h1>ChatGPT免费使用完全攻略：GPT-4o Mini每日4次</h1>

<p>2026年6月，OpenAI对ChatGPT免费版进行了重要更新：免费用户现在可以直接使用<strong>GPT-4o Mini</strong>（而非之前的GPT-3.5），每日配额为<strong>4次对话</strong>。同时，免费版保留了Code Interpreter（代码解释器）、DALL·E 3图像生成、文件上传分析等核心功能。对于大多数个人用户来说，这个免费额度已经完全足够日常使用。</p>

<h2>ChatGPT免费版核心能力</h2>

<ul>
<li><strong>模型版本：</strong>GPT-4o Mini（2026年6月升级）</li>
<li><strong>每日额度：</strong>4次对话（每日重置）</li>
<li><strong>商业许可：</strong>允许商业用途</li>
<li><strong>信用卡要求：</strong>无需绑定信用卡</li>
<li><strong>多平台支持：</strong>网页端、iOS App、Android App、桌面客户端</li>
</ul>

<h2>免费额度详解</h2>

<h3>1. 对话次数限制</h3>

<p>免费版用户每天有<strong>4次GPT-4o Mini对话机会</strong>。每次对话的token消耗根据消息长度和复杂度动态计算。普通文本对话平均消耗约50-100tokens/轮，包含代码生成或复杂推理可能消耗更多。</p>

<table>
<thead>
<tr><th>对话类型</th><th>平均token消耗</th><th>4次额度可支持轮数</th></tr>
</thead>
<tbody>
<tr><td>简单问答（文字）</td><td>~80 tokens</td><td>20-25轮</td></tr>
<tr><td>编程辅助</td><td>~200 tokens</td><td>8-10轮</td></tr>
<tr><td>数据分析+图表</td><td>~350 tokens</td><td>4-6轮</td></tr>
<tr><td>图像生成+detailed讨论</td><td>~500 tokens</td><td>2-3轮</td></tr>
</tbody>
</table>

<p><strong>关键提示：</strong>4次对话是按"会话"计算而非按消息数。一旦开启一个新对话（点击New Chat），这就算作一次额度消耗。同一个对话中反复追问不会额外消耗额度，直到你结束当前对话并开始新对话。</p>

<h3>2. 速度限制</h3>

<p>免费版在高峰期可能需要排队等待响应。根据OpenAI官方说明，当需求量大时，免费用户的响应速度会优先于Plus（$20/月）用户。建议在非高峰时段（如工作日白天、亚洲时间早晨）使用以获得更快速度。</p>

<h3>3. 功能完整性</h3>

<p>有趣的是，ChatGPT免费版的<strong>功能列表与Plus版基本一致</strong>，主要差异仅在于模型版本和额度限制。免费版包含以下完整功能：</p>

<ul>
<li>✅ 多轮对话记忆（最长256K上下文）</li>
<li>✅ Code Interpreter（上传Python/R/Excel文件自动执行）</li>
<li>✅ DALL·E 3图像生成（每月一定数量免费图片）</li>
<li>✅ 联网搜索（实时互联网信息）</li>
<li>✅ 文件上传（PDF、Word、Excel、PPT、图片均可分析）</li>
<li>✅ Custom GPTS市场访问（可使用他人创建的GPTs）</li>
<li>✅ 语音对话（通过App的语音输入功能）</li>
<li>✅ 桌面和移动客户端同步</li>
</ul>

<h2>Plus订阅 vs 免费版对比</h2>

<table>
<thead>
<tr><th>功能</th><th>免费版</th><th>Plus订阅 ($20/月)</th></tr>
</thead>
<tbody>
<tr><td>模型版本</td><td>GPT-4o Mini</td><td>GPT-4o + o3 推理模型</td></tr>
<tr><td>每日对话次数</td><td>4次</td><td>无限（有速率限制但远高于免费版）</td></tr>
<tr><td>响应速度</td><td>高峰期可能排队</td><td>优先处理，无排队</td></tr>
<tr><td>DALL·E 3图片生成</td><td>有限额度</td><td>每月80张快速生成+无限慢速</td></tr>
<tr><td>高级数据分析</td><td>标准模式</td><td>高级模式（更强大的代码解释器）</td></tr>
<tr><td>GPTs市场访问</td><td>可使用他人创建</td><td>可创建付费GPTs、独占功能</td></tr>
<tr><td>代码解释器文件限制</td><td>100MB/文件</td><td>200MB/文件</td></tr>
<tr><td>离线访问</td><td>❌ 不支持</td><td>✅ App支持离线缓存</td></tr>
</tbody>
</table>

<h2>免费版使用技巧（最大化4次额度）</h2>

<h3>技巧1：合并问题，减少对话次数</h3>

<p>在一个对话中一次性提出多个相关问题，比开多个新对话更省额度。例如不要分开问"写Python代码"、"解释代码"、"调试代码"，而是在一个对话中连续完成这些任务。</p>

<h3>技巧2：使用代码解释器的文件功能</h3>

<p>上传Excel、CSV或PDF文件到Code Interpreter，让ChatGPT自动分析和处理。这不仅能节省对话次数，还能获得比手动复制粘贴更准确的结果。一次对话即可分析整个文件并生成可视化图表。</p>

<h3>技巧3：利用Custom GPTs替代部分对话</h3>

<p>OpenAI的GPTs市场有大量免费专用助手。例如数学解题助手、代码调试助手、写作润色助手等。使用现成的GPTs可以绕过主模型的对话次数限制，因为某些GPTs有独立的配额机制。</p>

<h3>技巧4：合理安排使用时间</h3>

<p>免费版每日4次重置时间为UTC时间0点（北京时间早上8点）。建议在每天刚开始时使用最耗额度的任务（如长篇文档分析、复杂代码生成），而简单的问答可以在当天晚些时候进行。</p>

<h3>技巧5：使用API代替网页端（开发者方案）</h3>

<p>如果你是开发者，可以通过OpenAI API使用免费额度。虽然API本身不免费，但新用户注册可获得$5免费试用额度（有效期3个月）。通过API程序化调用ChatGPT可以避免网页端的对话次数限制（注意API和网页端配额是分开的）。</p>

<h2>常见问题解答</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: ChatGPT免费版的4次额度会共享给所有设备吗？</div>
<div class="faq-a">是的，4次每日额度是基于账号绑定的。无论你在电脑、手机还是平板上使用，都共享同一个每日配额。登录同一账号后，额度会自动同步。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 用完4次额度后还能继续使用吗？</div>
<div class="faq-a">用完4次后，你会被降级到GPT-3.5模型（如果可用），或者需要等待次日重置。具体取决于OpenAI当时的政策，有时免费版降级后仍可使用但模型性能会下降。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 免费版可以上传图片吗？</div>
<div class="faq-a">可以，ChatGPT免费版支持DALL·E 3图像生成，你可以在对话中输入提示词生成图片。不过每月生成的图片数量有限制，Plus用户每月80张快速生成+无限慢速生成，免费版额度更少但足以满足偶尔使用的需求。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 国内可以访问ChatGPT吗？</div>
<div class="faq-a">ChatGPT官网在国内访问不稳定，可能需要使用网络工具才能稳定访问。App Store和Google Play的中国区商店也无法直接下载ChatGPT App，需要从其他地区账号下载或使用网页版。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 免费版的使用记录会保留吗？</div>
<div class="faq-a">会，所有对话历史都会保存在你的OpenAI账号中，可以随时查看和管理。你可以选择删除单个对话或清空全部历史。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 升级到Plus后，之前的免费额度会补偿吗？</div>
<div class="faq-a">不会，升级到Plus订阅不会补偿之前消耗的免费对话次数。Plus的优势在于无限访问GPT-4o模型、更快响应速度和更多DALL·E生成额度，而不是补偿性赠送。</div>
</div>
</div>

<p><a href="https://chatgpt.com" target="_blank" style="color:#6366F1; text-decoration: underline;">前往 ChatGPT →</a></p>"""

    content_en = """<h1>ChatGPT Free Tier Guide 2026: Complete Breakdown</h1>

<p>In June 2026, OpenAI significantly upgraded the ChatGPT free tier: free users now get access to <strong>GPT-4o Mini</strong> instead of the previous GPT-3.5, with a daily quota of <strong>4 conversations</strong>. The free tier also retains core features including Code Interpreter, DALL·E 3 image generation, file upload analysis, and web search. For most individual users, this free quota is more than sufficient for everyday needs.</p>

<h2>Core Capabilities of ChatGPT Free Tier</h2>

<ul>
<li><strong>Model Version:</strong> GPT-4o Mini (upgraded June 2026)</li>
<li><strong>Daily Quota:</strong> 4 conversations (resets daily)</li>
<li><strong>Commercial Use:</strong> Allowed</li>
<li><strong>Payment Method:</strong> No credit card required</li>
<li><strong>Platforms:</strong> Web, iOS, Android, Desktop clients</li>
</ul>

<h2>Free Tier Details</h2>

<h3>1. Conversation Limit</h3>

<p>Free users get <strong>4 GPT-4o Mini conversations per day</strong>. Each conversation's token consumption varies based on message length and complexity. Simple text conversations typically consume ~80-100 tokens per round, while code generation or complex reasoning may consume more.</p>

<table>
<thead>
<tr><th>Conversation Type</th><th>Avg Token Usage</th><th>Rounds supported by 4 quotas</th></tr>
</thead>
<tbody>
<tr><td>Simple Q&A (text)</td><td>~80 tokens</td><td>20-25 rounds</td></tr>
<tr><td>Programming assistance</td><td>~200 tokens</td><td>8-10 rounds</td></tr>
<tr><td>Data analysis + charts</td><td>~350 tokens</td><td>4-6 rounds</td></tr>
<tr><td>Image generation + detailed discussion</td><td>~500 tokens</td><td>2-3 rounds</td></tr>
</tbody>
</table>

<p><strong>Key Tip:</strong> The 4 conversations are counted per "chat session", not per message. Starting a new chat (clicking New Chat) consumes one quota. Repeated questioning within the same conversation does not consume additional quota until you end the current session and start a new one.</p>

<h3>2. Speed Restrictions</h3>

<p>During peak hours, free users may experience queueing times. According to OpenAI, free user responses are prioritized below Plus ($20/month) subscribers during high demand. For best performance, use during off-peak hours (weekday mornings in your time zone).</p>

<h3>3. Feature Completeness</h3>

<p>Remarkably, the ChatGPT free tier offers <strong>nearly identical features to the Plus version</strong>, with differences mainly in model version and quota limits. The free tier includes:</p>

<ul>
<li><strong>✓</strong> Multi-turn context (up to 256K tokens)</li>
<li><strong>✓</strong> Code Interpreter (upload Python/R/Excel files for automatic execution)</li>
<li><strong>✓</strong> DALL·E 3 image generation (limited monthly quota)</li>
<li><strong>✓</strong> Web search for real-time information</li>
<li><strong>✓</strong> File upload support (PDF, Word, Excel, PPT, images all analyzable)</li>
<li><strong>✓</strong> Access to Custom GPTs marketplace</li>
<li><strong>✓</strong> Voice conversation (via mobile app voice input)</li>
<li><strong>✓</strong> Cross-platform sync across desktop and mobile clients</li>
</ul>

<h2>Plus Subscription vs Free Tier Comparison</h2>

<table>
<thead>
<tr><th>Feature</th><th>Free Tier</th><th>Plus Subscription ($20/month)</th></tr>
</thead>
<tbody>
<tr><td>Model Version</td><td>GPT-4o Mini</td><td>GPT-4o + o3 reasoning models</td></tr>
<tr><td>Daily Conversations</td><td>4</td><td>Unlimited (rate-limited but far higher than free)</td></tr>
<tr><td>Response Speed</td><td>May queue during peaks</td><td>Prioritized, no queuing</td></tr>
<tr><td>DALL·E 3 Image Gen</td><td>Limited quota</td><td>80 fast generations/month plus unlimited slow</td></tr>
<tr><td>Advanced Data Analysis</td><td>Standard mode</td><td>Advanced mode (more powerful Code Interpreter)</td></tr>
<tr><td>GPTs Market Access</td><td>Use existing GPTs</td><td>Create paid GPTs, exclusive features</td></tr>
<tr><td>File Upload Limit</td><td>100MB per file</td><td>200MB per file</td></tr>
<tr><td>Offline Access</td><td>❌ Not supported</td><td>✓ App supports offline cache</td></tr>
</tbody>
</table>

<h2>Pro Tips for Maximizing Your Free Quota</h2>

<h3>Tip 1: Consolidate Questions, Reduce Conversations</h3>

<p>Ask multiple related questions within the same conversation rather than starting new chats. For example, don't separately ask "write Python code," "explain this code," and "debug code"—complete all tasks in a single conversation to conserve quotas.</p>

<h3>Tip 2: Leverage Code Interpreter with Files</h3>

<p>Upload Excel, CSV, or PDF files to Code Interpreter for automatic analysis and processing. This saves conversation quotas and produces more accurate results than manual copy-paste. One conversation can analyze an entire file and generate visualizations.</p>

<h3>Tip 3: Use Custom GPTs to Supplement Conversations</h3>

<p>The GPTs Marketplace offers many free specialized assistants—math solvers, code debuggers, writing polishers, etc. Using existing GPTs can bypass the main model's conversation count, as some GPTs have independent quota mechanisms.</p>

<h3>Tip 4: Schedule Usage Time Wisely</h3>

<p>The free quota resets at UTC midnight (8:00 AM Beijing Time). Use your most quota-intensive tasks (document analysis, complex coding) early in the day after reset, and save simpler questions for later.</p>

<h3>Tip 5: Use API Instead of Web Interface (Developer Approach)</h3>

<p>Developers can use the OpenAI API with the $5 free trial credit (valid 3 months). Note that API and web interface quotas are separate, so this provides additional capacity beyond the 4 daily conversations.</p>

<h2>Frequently Asked Questions</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: Is the 4-conversation quota shared across all devices?</div>
<div class="faq-a">Yes, the quota is tied to your OpenAI account. Whether you use web, iOS, Android, or desktop, all devices share the same daily quota. Logging into the same account syncs the quota automatically.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: What happens after I use up my 4 daily conversations?</div>
<div class="faq-a">You'll be downgraded to GPT-3.5 (if available) or need to wait until the next day reset. Depending on OpenAI's current policy, you may still have limited access with reduced model performance.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Can I upload images in the free tier?</div>
<div class="faq-a">Yes, ChatGPT free tier supports DALL·E 3 image generation—you can enter prompts to generate images in conversations. However, the monthly generation limit is lower than Plus users, though sufficient for occasional use.</div>
</div>

<div class="faq-item">
<div class="faq-q">Can I access ChatGPT from China?</div>
<div class="faq-a">The ChatGPT website has unstable connectivity from mainland China and may require network tools for stable access. The ChatGPT app is also unavailable in Chinese app stores; users need accounts from other regions or must use the web version.</div>
</div>

<div class="faq-item">
<div class="faq-q">Are free tier conversations saved?</div>
<div class="faq-a">Yes, all conversation history is stored in your OpenAI account and can be viewed and managed at any time. You can delete individual conversations or clear all history.</div>
</div>

<div class="faq-item">
<div class="faq-q">Do unused free conversations carry over to Plus after upgrading?</div>
<div class="faq-a">No, upgrading to Plus does not compensate for unused free conversations. Plus benefits include unlimited GPT-4o access, faster response speeds, and more DALL·E generation quotas—not compensatory credits.</div>
</div>
</div>

<p><a href="https://chatgpt.com" target="_blank" style="color:#6366F1; text-decoration: underline;">Go to ChatGPT →</a></p>"""

    faqs_zh = [
        ("ChatGPT免费版的4次额度会不会跨天累计？", "不会，4次额度是每日重置，当天未使用的不会累积到第二天。每天UTC时间0点（北京时间早上8点）重新获得4次机会。"),
        ("免费版能用GPT-4吗", "目前免费版使用的是GPT-4o Mini，不是完整的GPT-4o。Plus订阅($20/月)才可以使用完整的GPT-4o和最新的o3推理模型。"),
        ("免费用户可以生成图片吗", "可以，ChatGPT免费版内置了DALL·E 3图像生成功能。不过free用户的每月图片生成数量比Plus用户少，plus每月80张快速生成+无限慢速生成，free额度较少但偶尔够用。"),
        ("升级Plus后之前的消费会退吗", "不会，升级付费订阅不会退款或补偿之前免费的对话次数。Plus的优势是模型能力更强、速度更快、额度更多，而不是经济补偿。"),
        ("免费版有没有使用时长限制", "单次对话没有严格的时间限制，但长时间不活跃的对话可能会被系统自动结束。建议保持对话活跃状态。"),
    ]

    faqs_en = [
        ("Does the 4 free conversation quota carry over to the next day?", "No—the 4 quota resets daily. Unused quota does not accumulate. A fresh 4 quota becomes available at UTC midnight (8:00 AM Beijing Time)."),
        ("Can free users access GPT-4 directly?", "The free tier currently uses GPT-4o Mini, not the full GPT-4o. The Plus subscription ($20/month) is required for access to the full GPT-4o and the latest o3 reasoning models."),
        ("Can free users generate images?", "Yes, ChatGPT free tier supports DALL·E 3 image generation. However, the monthly image quota for free users is lower than Plus users—Plus gets 80 fast generations per month plus unlimited slow generation, while free users have a smaller quota sufficient for occasional use."),
        ("If I upgrade to Plus, will I get a refund for previous free usage?", "No—upgrading to Plus does not provide refunds or compensation for previously used free conversations. Plus benefits include stronger model capabilities, faster speeds, and larger quotas—not economic compensation for past free usage."),
        ("Are there time limits for free conversations?", "There's no strict time limit per conversation, but inactive sessions may be automatically ended by the system. Keeping conversations active is recommended."),
    ]

    # Generate HTML
    zh_html, en_html = generate_guide_html(
        slug, title_zh, title_en,
        desc_zh, desc_en,
        content_zh, content_en,
        faqs_zh, faqs_en,
        today
    )

    # Write files
    os.makedirs('/home/ubuntu/aifreeplan/zh/guides', exist_ok=True)
    os.makedirs('/home/ubuntu/aifreeplan/en/guides', exist_ok=True)

    with open(f'/home/ubuntu/aifreeplan/zh/guides/{slug}.html', 'w', encoding='utf-8') as f:
        f.write(zh_html)

    with open(f'/home/ubuntu/aifreeplan/en/guides/{slug}.html', 'w', encoding='utf-8') as f:
        f.write(en_html)

    print(f"✅ Generated ChatGPT free tier guide:")
    print(f"   - /zh/guides/{slug}.html")
    print(f"   - /en/guides/{slug}.html")

if __name__ == '__main__':
    main()
