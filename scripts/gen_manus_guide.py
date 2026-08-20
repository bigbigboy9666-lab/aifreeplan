#!/usr/bin/env python3
"""Generate Manus AI free guide article directly."""
import os
import sys
from datetime import datetime

def main():
    today = datetime.now().strftime('%Y-%m-%d')
    slug = "manus-ai-free-unlimited-agent-2026"
    
    title_zh = "Manus AI免费攻略：每日300积分无限刷新，真正自主AI Agent白嫖指南"
    title_en = "Manus AI Free Guide: 300 Daily Refresh Credits for Truly Autonomous AI Agent — No Credit Card Required"
    desc_zh = "Manus AI是全球领先的自主AI Agent，能独立完成浏览网页、写代码、做研究、建应用等复杂多步骤任务。免费版每日300积分自动刷新，无需信用卡，无需付费即可体验真正的AI自主执行能力。本文讲清楚免费机制、额度、使用步骤和避坑指南。"
    desc_en = "Manus AI is a leading autonomous AI agent that independently browses the web, writes code, conducts research, and builds applications. Free plan gives 300 credits daily refresh — no credit card required. Full guide with limits, steps, and pitfalls."
    
    content_zh = """<h1>Manus AI免费攻略：每日300积分无限刷新，真正自主AI Agent白嫖指南</h1>

<p>Manus AI是2026年最受关注的AI自主Agent产品之一。与ChatGPT、Claude等对话式AI不同，Manus真正做到了"你说目标，它自己跑"——从打开浏览器、搜索信息、分析数据到编写代码、部署应用，全程自主完成，不需要你一步步引导。而且免费版每天自动刷新300积分，无需信用卡，不用付费就能体验真正的AI自主执行。</p>

<h2>Manus AI是什么</h2>

<p>Manus AI由蝴蝶效应科技（Monica.im）团队开发，定位是"真正自主的AI Agent"。它的核心能力包括：</p>

<ul>
<li><strong>自主规划与执行：</strong>你只需要说目标，Manus会自动拆解步骤、执行任务、处理异常情况</li>
<li><strong>云端虚拟浏览器：</strong>在隔离的云端环境中运行，不会干扰你的电脑</li>
<li><strong>代码编写与执行：</strong>支持Python、JavaScript、TypeScript等多种语言，实时测试</li>
<li><strong>深度研究：</strong>自动搜索信息、整理资料、生成报告</li>
<li><strong>网页应用开发：</strong>可以直接构建带支付和数据库的完整网页应用</li>
<li><strong>多平台接入：</strong>网页、桌面端、Telegram、WhatsApp、Slack均可使用</li>
</ul>

<p>根据GAIA基准测试，Manus在自主任务完成率达到行业领先水平，远超同类工具。</p>

<h2>免费额度详解</h2>

<p>Manus的免费计划是目前AI Agent类工具中良心程度最高的之一：</p>

<table>
<tr><th>项目</th><th>免费额度</th></tr>
<tr><td>每日积分刷新</td><td><strong>300积分/天</strong></td></tr>
<tr><td>积分重置</td><td>每24小时自动重置，不清零累积</td></tr>
<tr><td>需要信用卡</td><td>❌ 不需要</td></tr>
<tr><td>需要注册</td><td>✅ 需要（邮箱或Google登录）</td></tr>
<tr><td>可用模型</td><td>Manus 1.6 Lite（免费版专属）</td></tr>
<tr><td>商用权限</td><td>❌ 免费版不可商用</td></tr>
<tr><td>水印</td><td>❌ 无水印</td></tr>
</table>

<p><strong>300积分/天</strong>的额度在实际使用中是什么概念？简单任务（如搜索信息、总结网页）可能只消耗10-30积分，中等任务（如写一段代码、生成报告）消耗50-100积分，复杂任务（如构建完整Web应用）可能消耗150-300积分。这意味着每天可以完成2-10个不等的小到中等复杂度任务。</p>

<h2>免费使用步骤</h2>

<h3>步骤一：访问官网注册</h3>
<p>打开 <a href="https://manus.im">manus.im</a>，使用Google账号或邮箱注册。整个过程不超过1分钟，无需填写信用卡信息。</p>

<h3>步骤二：理解积分系统</h3>
<p>注册后你会看到账户页面，顶部显示当前剩余积分和每日刷新时间。建议先记下刷新时间点（通常是UTC 0:00或根据账号注册时间计算），这样可以合理规划每天的使用。</p>

<h3>步骤三：开始第一个任务</h3>
<p>在输入框中直接描述你想完成的目标。例如：</p>
<ul>
<li><strong>研究任务：</strong>"帮我调研2026年AI编程工具的最新进展，整理成一份报告"</li>
<li><strong>编码任务：</strong>"用React写一个待办事项应用，支持添加、删除、标记完成"</li>
<li><strong>数据分析：</strong>"下载这个CSV文件，分析销售趋势，生成可视化图表"</li>
<li><strong>网页开发：</strong>"帮我搭建一个个人博客网站，支持Markdown输入和预览"</li>
</ul>

<h3>步骤四：监控任务进度</h3>
<p>Manus会实时显示执行进度，包括打开的页面、执行的代码、遇到的错误等。你可以随时暂停或修改任务方向。</p>

<h2>高级使用技巧</h2>

<h3>技巧一：拆解复杂任务</h3>
<p>Manus虽然能自主执行，但复杂任务消耗的积分可能远超预期（3-5倍）。正确做法是将大任务拆解成多个小任务：</p>
<ul>
<li>❌ "帮我做一个完整的电商平台"</li>
<li>✅ "先帮我设计电商平台的数据库结构" → "再帮我写商品列表页面" → "最后帮我添加购物车功能"</li>
</ul>

<h3>技巧二：优先使用每日刷新积分</h3>
<p>Manus有多个积分池：每日刷新的300积分和月度基础积分。建议每天先用完300积分再动月度池，因为月度积分用完后需要等下个月刷新，而每日积分每天都能重置。</p>

<h3>技巧三：善用模板和快捷指令</h3>
<p>Manus提供多种任务模板，如"代码审查"、"Bug修复"、"文档撰写"等。使用模板可以显著降低积分消耗，因为Manus对已知任务类型的执行效率更高。</p>

<h3>技巧四：简单问答用ChatGPT更划算</h3>
<p>Manus的核心价值在于"自主执行"，而不是"回答问题"。如果你只是需要简单的问题解答，ChatGPT免费版就足够了。Manus适合需要多步骤执行的任务：浏览多个网页、编写代码、操作软件等。</p>

<h2>付费版对比</h2>

<table>
<tr><th>特性</th><th>免费版</th><th>Standard版</th><th>Customizable版</th></tr>
<tr><td>月价格</td><td>$0</td><td>$20/月</td><td>$40/月</td></tr>
<tr><td>每日积分</td><td>300</td><td>1,000</td><td>5,000</td></tr>
<tr><td>可用模型</td><td>Manus 1.6 Lite</td><td>Manus 1.6 Pro</td><td>Manus 1.6 Pro + 优先队列</td></tr>
<tr><td>商用权限</td><td>❌</td><td>✅</td><td>✅</td></tr>
<tr><td>最大任务复杂度</td><td>中等</td><td>高</td><td>极高</td></tr>
<tr><td>API访问</td><td>❌</td><td>✅</td><td>✅</td></tr>
<tr><td>团队共享</td><td>❌</td><td>❌</td><td>✅</td></tr>
</table>

<p>对于大多数个人用户，免费版300积分/天已经足够日常使用。如果你需要商用权限或更高额度，Standard版$20/月性价比不错；年付可省17%，约$200/年。</p>

<h2>常见问题</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: 免费版的300积分每天真的会自动刷新吗？</div>
<div class="faq-a">是的。Manus的免费计划每日300积分会在固定时间自动重置，通常是UTC 0:00。积分不会累积到第二天，用不完就清零，所以建议每天尽量用完。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 不需要信用卡就能注册吗？</div>
<div class="faq-a">是的，Manus免费版注册只需要邮箱或Google账号，不需要绑定任何支付方式。这是它相比其他AI Agent工具的最大优势之一。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 免费版和付费版有什么区别？</div>
<div class="faq-a">核心区别是积分额度和模型版本。免费版使用Manus 1.6 Lite模型，适合中等复杂度任务；付费版解锁1.6 Pro模型，处理复杂任务更稳定。此外免费版不可商用，付费版可以。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 生成的代码可以商用吗？</div>
<div class="faq-a">免费版生成的代码仅限个人学习使用，不可用于商业项目。如需商用，需升级到付费版。建议在使用前查看最新的Manus服务条款。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 为什么我的积分消耗比预期快？</div>
<div class="faq-a">Manus的积分消耗不完全透明，任务开始前不会显示预计消耗。复杂任务（如构建完整应用、深度研究）可能消耗150-300积分。建议将大任务拆分成小任务，或者先用Lite模型测试可行性。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Manus支持中文吗？</div>
<div class="faq-a">支持。你可以用中文描述任务，Manus能理解中文指令并执行。但建议在提示词中使用英文关键词，以获得更准确的执行结果。</div>
</div>
</div>

<h2>总结</h2>

<p>Manus AI是目前最接近"真正自主AI Agent"概念的产品。免费版每天300积分自动刷新，无需信用卡，适合个人用户日常使用。核心优势在于：你只需要说目标，剩下的交给它。</p>

<p><strong>推荐场景：</strong>需要多步骤自主执行的任务，如网页研究、代码开发、数据分析、应用构建。<strong>不推荐场景：</strong>简单问答、单次操作任务（用ChatGPT更划算）。</p>

<p>立即访问 <a href="https://manus.im">manus.im</a> 注册体验，每天白嫖300积分，体验真正的AI自主执行能力。</p>
"""
    
    content_en = """<h1>Manus AI Free Guide: 300 Daily Refresh Credits for Truly Autonomous AI Agent</h1>

<p>Manus AI is one of the most talked-about autonomous AI Agent products in 2026. Unlike ChatGPT or Claude which rely on turn-by-turn conversation, Manus actually delivers on the "set a goal and watch it work" promise — from browsing the web and researching information to writing code and deploying applications, it handles multi-step workflows autonomously without requiring step-by-step guidance. The free plan refreshes 300 credits daily, requires no credit card, and lets you experience genuine AI autonomy completely free.</p>

<h2>What is Manus AI?</h2>

<p>Developed by the team behind Monica.im (蝴蝶效应科技), Manus AI positions itself as a "truly autonomous AI Agent." Its core capabilities include:</p>

<ul>
<li><strong>Autonomous planning and execution:</strong> State your goal and Manus breaks it down, executes steps, and handles exceptions on its own</li>
<li><strong>Cloud virtual browser:</strong> Runs in an isolated cloud environment, never interfering with your local machine</li>
<li><strong>Code writing and execution:</strong> Supports Python, JavaScript, TypeScript and more with real-time testing</li>
<li><strong>Deep research:</strong> Automatically searches, synthesizes information, and generates reports</li>
<li><strong>Web application development:</strong> Can build complete web apps with payment and database integration</li>
<li><strong>Multi-platform access:</strong> Available on web, desktop, Telegram, WhatsApp, and Slack</li>
</ul>

<p>On the GAIA benchmark for autonomous task completion, Manus achieves industry-leading results, significantly outperforming similar tools.</p>

<h2>Free Tier Details</h2>

<p>Manus's free plan is one of the most generous in the AI Agent category:</p>

<table>
<tr><th>Feature</th><th>Free Tier</th></tr>
<tr><td>Daily credit refresh</td><td><strong>300 credits/day</strong></td></tr>
<tr><td>Credit reset</td><td>Auto-resets every 24 hours, no rollover</td></tr>
<tr><td>Credit card required</td><td>❌ No</td></tr>
<tr><td>Registration required</td><td>✅ Yes (email or Google sign-in)</td></tr>
<tr><td>Available model</td><td>Manus 1.6 Lite (free tier exclusive)</td></tr>
<tr><td>Commercial use</td><td>❌ Not allowed</td></tr>
<tr><td>Watermark</td><td>❌ None</td></tr>
</table>

<p>What does 300 credits/day look like in practice? Simple tasks (searching, summarizing webpages) may cost 10-30 credits. Medium tasks (writing code, generating reports) cost 50-100 credits. Complex tasks (building a full web app) can consume 150-300 credits. This means you can complete roughly 2-10 small-to-medium tasks daily on the free plan.</p>

<h2>How to Use for Free (Step by Step)</h2>

<h3>Step 1: Visit the Website and Sign Up</h3>
<p>Go to <a href="https://manus.im">manus.im</a> and register with your Google account or email. The process takes less than a minute, no credit card binding required.</p>

<h3>Step 2: Understand the Credit System</h3>
<p>After registration, you'll see your account dashboard showing current remaining credits and the daily refresh time. Note the reset time (typically UTC 0:00 or based on your account creation time) so you can plan your daily usage efficiently.</p>

<h3>Step 3: Start Your First Task</h3>
<p>Simply describe your goal in the input box. Examples:</p>
<ul>
<li><strong>Research:</strong> "Research the latest developments in AI coding tools in 2026 and compile a report"</li>
<li><strong>Coding:</strong> "Write a React to-do app with add, delete, and complete toggle functionality"</li>
<li><strong>Data analysis:</strong> "Download this CSV file, analyze sales trends, and generate visualizations"</li>
<li><strong>Web development:</strong> "Build me a personal blog site with Markdown input and preview"</li>
</ul>

<h3>Step 4: Monitor Progress in Real-Time</h3>
<p>Manus displays execution progress live, showing opened pages, executed code, and any errors encountered. You can pause or redirect the task at any point.</p>

<h2>Advanced Tips</h2>

<h3>Tip 1: Break Complex Tasks into Smaller Ones</h3>
<p>While Manus can handle complex tasks autonomously, the credit consumption may be 3-5x higher than expected. The key is to decompose large tasks:</p>
<ul>
<li>❌ "Build me a complete e-commerce platform"</li>
<li>✅ "Design the database schema first" → "Then build the product listing page" → "Finally add the shopping cart feature"</li>
</ul>

<h3>Tip 2: Prioritize Daily Refresh Credits</h3>
<p>Manus has multiple credit pools: the daily 300 refresh and a monthly base allocation. Always use the daily refresh first before touching your monthly pool, since monthly credits don't rollover.</p>

<h3>Tip 3: Use Templates and Quick Commands</h3>
<p>Manus offers task templates like "Code Review," "Bug Fix," and "Document Writing." Using templates significantly reduces credit consumption since Manus executes known task patterns more efficiently.</p>

<h3>Tip 4: Use ChatGPT for Simple Q&A</h3>
<p>Manus shines at "autonomous execution," not "answering questions." For simple Q&A, the free ChatGPT tier is sufficient. Reserve Manus for multi-step tasks: browsing multiple pages, writing code, operating software, etc.</p>

<h2>Paid Plans Comparison</h2>

<table>
<tr><th>Feature</th><th>Free</th><th>Standard</th><th>Customizable</th></tr>
<tr><td>Monthly price</td><td>$0</td><td>$20/month</td><td>$40/month</td></tr>
<tr><td>Daily credits</td><td>300</td><td>1,000</td><td>5,000</td></tr>
<tr><td>Model</td><td>Manus 1.6 Lite</td><td>Manus 1.6 Pro</td><td>Manus 1.6 Pro + Priority queue</td></tr>
<tr><td>Commercial use</td><td>❌</td><td>✅</td><td>✅</td></tr>
<tr><td>Max task complexity</td><td>Medium</td><td>High</td><td>Very high</td></tr>
<tr><td>API access</td><td>❌</td><td>✅</td><td>✅</td></tr>
<tr><td>Team sharing</td><td>❌</td><td>❌</td><td>✅</td></tr>
</table>

<p>For most individual users, 300 daily free credits are sufficient. If you need commercial use rights or higher quotas, the Standard plan at $20/month is reasonable. Annual billing saves 17% — approximately $200/year.</p>

<h2>Frequently Asked Questions</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: Do the 300 free credits really refresh daily?</div>
<div class="faq-a">Yes. The free plan's 300 daily credits auto-reset at a fixed time, typically UTC 0:00. Credits do not rollover — unused credits are lost each day, so make the most of them daily.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Can I sign up without a credit card?</div>
<div class="faq-a">Yes. The free plan only requires an email or Google account sign-in. No payment method binding is needed — this is one of Manus's biggest advantages over other AI Agent tools.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: What's the difference between free and paid?</div>
<div class="faq-a">The core differences are credit limits and model versions. Free uses the Manus 1.6 Lite model, suitable for medium-complexity tasks. Paid unlocks the 1.6 Pro model for more complex tasks with better stability. Free tier also prohibits commercial use.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Can I use generated code commercially?</div>
<div class="faq-a">Code generated on the free plan is for personal learning only, not for commercial projects. Upgrade to a paid plan for commercial usage rights. Check the latest Manus Terms of Service for details.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Why do my credits run out faster than expected?</div>
<div class="faq-a">Manus doesn't show estimated credit consumption before running tasks. Complex tasks (full app builds, deep research) can consume 150-300 credits. Break large tasks into smaller ones, or test with the Lite model first.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Does Manus support Chinese?</div>
<div class="faq-a">Yes. You can describe tasks in Chinese and Manus will understand and execute. However, using English keywords in prompts typically yields more accurate results.</div>
</div>
</div>

<h2>Summary</h2>

<p>Manus AI is currently the closest product to the "truly autonomous AI Agent" concept. The free plan offers 300 daily refresh credits, no credit card required, making it ideal for personal daily use. The core value proposition: state your goal and let it handle the rest.</p>

<p><strong>Best for:</strong> Multi-step autonomous tasks like web research, code development, data analysis, and app building. <strong>Not recommended for:</strong> Simple Q&A or single-step tasks (use ChatGPT instead).</p>

<p>Visit <a href="https://manus.im">manus.im</a> to sign up and start with 300 free credits daily — experience genuine AI autonomous execution.</p>
"""
    
    faq_zh = """{"@type":"Question","name":"免费版的300积分每天真的会自动刷新吗？","acceptedAnswer":{"@type":"Answer","text":"是的。Manus的免费计划每日300积分会在固定时间自动重置，通常是UTC 0:00。积分不会累积到第二天，用不完就清零，所以建议每天尽量用完。"}},{"@type":"Question","name":"不需要信用卡就能注册吗？","acceptedAnswer":{"@type":"Answer","text":"是的，Manus免费版注册只需要邮箱或Google账号，不需要绑定任何支付方式。这是它相比其他AI Agent工具的最大优势之一。"}},{"@type":"Question","name":"免费版和付费版有什么区别？","acceptedAnswer":{"@type":"Answer","text":"核心区别是积分额度和模型版本。免费版使用Manus 1.6 Lite模型，适合中等复杂度任务；付费版解锁1.6 Pro模型，处理复杂任务更稳定。此外免费版不可商用，付费版可以。"}},{"@type":"Question","name":"生成的代码可以商用吗？","acceptedAnswer":{"@type":"Answer","text":"免费版生成的代码仅限个人学习使用，不可用于商业项目。如需商用，需升级到付费版。建议在使用前查看最新的Manus服务条款。"}},{"@type":"Question","name":"为什么我的积分消耗比预期快？","acceptedAnswer":{"@type":"Answer","text":"Manus的积分消耗不完全透明，任务开始前不会显示预计消耗。复杂任务（如构建完整应用、深度研究）可能消耗150-300积分。建议将大任务拆分成小任务，或者先用Lite模型测试可行性。"}},{"@type":"Question","name":"Manus支持中文吗？","acceptedAnswer":{"@type":"Answer","text":"支持。你可以用中文描述任务，Manus能理解中文指令并执行。但建议在提示词中使用英文关键词，以获得更准确的执行结果。"}}"""
    
    faq_en = """{"@type":"Question","name":"Do the 300 free credits really refresh daily?","acceptedAnswer":{"@type":"Answer","text":"Yes. The free plan's 300 daily credits auto-reset at a fixed time, typically UTC 0:00. Credits do not rollover — unused credits are lost each day, so make the most of them daily."}},{"@type":"Question","name":"Can I sign up without a credit card?","acceptedAnswer":{"@type":"Answer","text":"Yes. The free plan only requires an email or Google account sign-in. No payment method binding is needed — this is one of Manus's biggest advantages over other AI Agent tools."}},{"@type":"Question","name":"What's the difference between free and paid?","acceptedAnswer":{"@type":"Answer","text":"The core differences are credit limits and model versions. Free uses the Manus 1.6 Lite model, suitable for medium-complexity tasks. Paid unlocks the 1.6 Pro model for more complex tasks with better stability. Free tier also prohibits commercial use."}},{"@type":"Question","name":"Can I use generated code commercially?","acceptedAnswer":{"@type":"Answer","text":"Code generated on the free plan is for personal learning only, not for commercial projects. Upgrade to a paid plan for commercial usage rights. Check the latest Manus Terms of Service for details."}},{"@type":"Question","name":"Why do my credits run out faster than expected?","acceptedAnswer":{"@type":"Answer","text":"Manus doesn't show estimated credit consumption before running tasks. Complex tasks (full app builds, deep research) can consume 150-300 credits. Break large tasks into smaller ones, or test with the Lite model first."}},{"@type":"Question","name":"Does Manus support Chinese?","acceptedAnswer":{"@type":"Answer","text":"Yes. You can describe tasks in Chinese and Manus will understand and execute. However, using English keywords in prompts typically yields more accurate results."}}"""
    
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
    
    # Write guide metadata
    import json
    guide_data = {
        "slug": slug,
        "title_zh": title_zh,
        "title_en": title_en,
        "description_zh": desc_zh,
        "description_en": desc_en,
        "category": "ai-assistant",
        "date_published": today,
        "tags": ["manus", "ai-agent", "autonomous", "free-tier", "300-credits-daily", "no-credit-card"],
        "excerpt_zh": "Manus AI是全球领先的自主AI Agent，免费版每日300积分自动刷新，无需信用卡。本文讲清楚免费机制、额度、使用技巧，以及免费版和付费版的完整对比。",
        "excerpt_en": "Manus AI is a leading autonomous AI agent. Free plan gives 300 daily refresh credits, no credit card needed. Full guide with limits, tips, and free vs paid comparison."
    }
    
    # Update guides.json
    guides_path = '/home/ubuntu/aifreeplan/public/data/guides.json'
    with open(guides_path, 'r', encoding='utf-8') as f:
        guides_doc = json.load(f)
    
    # Check if slug already exists
    existing_slugs = {g['slug'] for g in guides_doc.get('guides', [])}
    if slug not in existing_slugs:
        guides_doc['guides'].append(guide_data)
        guides_doc['updatedAt'] = datetime.now().isoformat()
        guides_doc['generatedAt'] = datetime.now().strftime('%Y-%m-%d')
        with open(guides_path, 'w', encoding='utf-8') as f:
            json.dump(guides_doc, f, ensure_ascii=False, indent=2)
        print(f"   ✅ Added to guides.json")
    else:
        print(f"   ⚠️  Slug {slug} already exists in guides.json, skipping update")

if __name__ == '__main__':
    main()
