#!/usr/bin/env python3
"""Generate and deploy Cursor AI free tier guide article."""
import os
import sys
from datetime import datetime

def main():
    today = datetime.now().strftime('%Y-%m-%d')
    slug = "cursor-ai-free-tier-guide-2026"
    
    title_zh = "Cursor AI 免费版完全攻略：2026年最火AI代码编辑器，200条/月免费额度"
    title_en = "Cursor AI Free Tier Guide 2026: The Hottest AI Code Editor with 200 Free Messages/Month"
    desc_zh = "Cursor AI是2026年最流行的AI编程工具，提供完全免费的使用方案。本文详细介绍Cursor免费版的功能、额度限制、注册方法，以及与Pro付费版的全面对比。"
    desc_en = "Cursor AI is the most popular AI coding tool in 2026, offering a completely free plan. This guide details Cursor's free tier features, limits, signup process, and a comprehensive comparison with the Pro plan."
    
    content_zh = """<h1>Cursor AI 免费版完全攻略：2026年最火AI代码编辑器，200条/月免费额度</h1>

<p><strong>Cursor AI</strong> 是2026年开发者社区中最炙手可热的AI编程工具。这款基于VS Code构建的代码编辑器，将AI能力深度融入开发流程，让程序员可以用自然语言与代码交互，实现智能补全、代码生成、错误修复、重构优化等一系列高级操作。最重要的是——<strong>Cursor提供了一个功能相当完整的免费版</strong>，无需付费即可体验核心AI编程能力。</p>

<h2>什么是 Cursor AI？</h2>

<p>Cursor AI 由 <strong>Anysphere</strong> 公司开发，建立在开源的 VS Code 之上。这意味着：</p>

<ul>
<li><strong>完全兼容VS Code生态：</strong>所有VS Code插件、主题、快捷键都可以在Cursor中使用</li>
<li><strong>零学习成本：</strong>如果你用过VS Code，上手Cursor几乎零门槛</li>
<li><strong>跨平台支持：</strong>Windows、macOS、Linux 三大操作系统全覆盖</li>
</ul>

<p>截至2026年7月，Cursor在全球开发者中的渗透率已超过<strong>18%</strong>，支持<strong>50多种编程语言</strong>，覆盖Web开发、数据科学、移动端开发等多个领域。</p>

<h2>Cursor AI 免费版详细规格</h2>

<h3>免费额度一览（2026年7月数据）</h3>

<table>
<tr><th>功能</th><th>免费版额度</th><th>说明</th></tr>
<tr><td><strong>Chat 消息额度</strong></td><td><strong>200条/月</strong></td><td>每次在Chat面板发送一条消息计为一次。200条约可供日常轻量使用约15-20天。</td></tr>
<tr><td><strong>Fast Model Requests</strong></td><td><strong>50次/天</strong></td><td>每日可触发50次高速响应模式。超出后仍可继续使用，但进入排队等待。</td></tr>
<tr><td><strong>Tab 自动补全</strong></td><td><strong>100次/天</strong></td><td>每日可免费使用100次Tab智能补全，超出后进入限流状态。</td></tr>
<tr><td><strong>Slow/Background Requests</strong></td><td><strong>无限</strong></td><td>响应稍慢但无每日限制，可使用更强大的模型。</td></tr>
<tr><td><strong>Composer Mode</strong></td><td><strong>10次/月</strong></td><td>多文件AI生成和编辑功能，免费版每月仅10次。</td></tr>
<tr><td><strong>Agent Mode</strong></td><td><strong>5次/月</strong></td><td>自主多步骤Agent任务，免费版每月仅5次。</td></tr>
<tr><td><strong>代码库索引</strong></td><td><strong>最多50,000个文件</strong></td><td>大型项目（>50K文件）可能需要升级。</td></tr>
<tr><td><strong>可用模型</strong></td><td>Claude 3.5 Sonnet, GPT-4o, Gemini 2.0</td><td>高级模型（如Claude 3.7 Sonnet Max）仅限Pro。</td></tr>
<tr><td><strong>自定义提示词</strong></td><td><strong>最多1套</strong></td><td>Pro版最多支持20套。</td></tr>
<tr><td><strong>历史记录</strong></td><td><strong>保留14天</strong></td><td>Pro版保留30天。</td></tr>
</table>

<h3>每日额度重置机制</h3>

<p><strong>⏰ 重置时间：</strong>每日的Fast Model Requests（50次）和Tab补全（100次）在<strong>太平洋时间（PT）00:00</strong>重置，对应<strong>北京时间上午16:00</strong>。建议在高强度使用场景下，在每天下午4点前完成主要AI交互。</p>

<h3>免费版不支持的功能</h3>

<table>
<tr><th>功能</th><th>免费版</th><th>Pro版（$20/月）</th></tr>
<tr><td>Copilot++ 超高速补全</td><td>❌ 不可用</td><td>✅ 包含</td></tr>
<tr><td>Chat 消息/月</td><td>200条</td><td>5,000条</td></tr>
<tr><td>Fast Model/天</td><td>50次</td><td>500次</td></tr>
<tr><td>Composer Mode</td><td>10次/月</td><td>无限制</td></tr>
<tr><td>Agent Mode</td><td>5次/月</td><td>无限制</td></tr>
<tr><td>代码库索引大小</td><td>50K文件</td><td>无限制</td></tr>
<tr><td>自定义提示词</td><td>1套</td><td>20套</td></tr>
<tr><td>团队协作功能</td><td>❌ 不可用</td><td>✅ 包含</td></tr>
<tr><td>优先队列</td><td>❌ 最低优先级</td><td>✅ 高优先级</td></tr>
<tr><td>高级模型</td><td>❌ 仅限基础模型</td><td>✅ Claude 3.7 Sonnet Max等</td></tr>
</table>

<h2>如何注册 Cursor AI（免费版）</h2>

<ol>
<li><strong>下载 Cursor：</strong>访问 <a href="https://cursor.sh" target="_blank">cursor.sh</a>，根据你的操作系统下载最新版本。</li>
<li><strong>安装编辑器：</strong>运行安装程序，Cursor会安装在独立目录下，不会覆盖你现有的VS Code。</li>
<li><strong>创建账户：</strong>启动Cursor，使用以下方式之一注册：
<ul>
<li>Google账户（推荐，最快）</li>
<li>GitHub账户</li>
<li>Microsoft账户</li>
<li>邮箱和密码</li>
</ul>
</li>
<li><strong>验证邮箱：</strong>查看收件箱中的验证链接并点击激活账户。</li>
<li><strong>导入VS Code设置（可选）：</strong>Cursor会在首次启动时询问是否导入VS Code的设置、扩展和快捷键，建议导入以保留你的开发环境。</li>
<li><strong>开始使用：</strong>账户激活后即可立即使用免费版所有功能。你可以在设置中的"Usage"或"Billing"部分查看剩余额度。</li>
</ol>

<div style="background:#eef2ff;border:2px solid #6366f1;border-radius:8px;padding:18px;margin:20px 0;">
<strong>💡 提示：</strong>如果你已经有VS Code，强烈建议导入设置和扩展，这样可以无缝迁移，保留你熟悉的工作环境。
</div>

<h2>Cursor AI 免费版 vs Pro 版详细对比</h2>

<table>
<tr><th>对比项</th><th>免费版</th><th>Pro版（$20/月）</th><th>Pro版（$16/月，年付）</th></tr>
<tr><td>Chat消息/月</td><td>200条</td><td>5,000条（25倍）</td><td>5,000条（25倍）</td></tr>
<tr><td>Fast Model/天</td><td>50次</td><td>500次（10倍）</td><td>500次（10倍）</td></tr>
<tr><td>Slow/Background</td><td>无限</td><td>无限</td><td>无限</td></tr>
<tr><td>Tab补全/天</td><td>100次</td><td>500次</td><td>500次</td></tr>
<tr><td>Composer Mode</td><td>10次/月</td><td>无限制</td><td>无限制</td></tr>
<tr><td>Agent Mode</td><td>5次/月</td><td>无限制</td><td>无限制</td></tr>
<tr><td>代码库索引</td><td>50,000文件</td><td>无限制</td><td>无限制</td></tr>
<tr><td>优先队列</td><td>❌</td><td>✅</td><td>✅</td></tr>
<tr><td>高级模型</td><td>❌</td><td>✅</td><td>✅</td></tr>
<tr><td>团队协作</td><td>❌</td><td>✅</td><td>✅</td></tr>
</table>

<h2>如何最大化 Cursor 免费版使用</h2>

<h3>技巧一：合理分配每日额度</h3>
<p>每天只有50次Fast Model和100次Tab补全，建议：</p>
<ul>
<li><strong>早晨黄金时间：</strong>在上午16:00（北京时间）重置后，尽早完成最复杂的AI辅助任务</li>
<li><strong>Slow模式救急：</strong>额度用尽后，切换到Slow/Background模式，虽然响应慢但无限制</li>
<li><strong>批量提问：</strong>把多个问题合并成一条消息，节省Chat额度</li>
</ul>

<h3>技巧二：善用 Slow Model</h3>
<p>免费版可以<strong>无限次</strong>使用Slow/Background模式，虽然响应时间更长，但使用的是<strong>更强的模型</strong>。对于不紧急的任务（如代码审查、架构分析），Slow模式其实效果更好。</p>

<h3>技巧三：优化提示词质量</h3>
<p>高质量的提示词可以：</p>
<ul>
<li>减少迭代次数，节省每次回复的消息配额</li>
<li>获得更准确的结果，减少因回复不佳而重新提问的情况</li>
<li>充分利用上下文窗口，让AI更好地理解你的代码库</li>
</ul>
<p><strong>好的提示词公式：</strong>【角色】+【任务】+【上下文】+【输出格式】</p>

<h3>技巧四：善用Tab补全</h3>
<p>Tab补全是Cursor最省额度的功能：</p>
<ul>
<li>只需按Tab键即可接受建议，不计入Chat消息配额</li>
<li>每天100次的限额对于日常编码绰绰有余</li>
<li>结合AI生成的代码片段，可以大幅提高编码效率</li>
</ul>

<h3>技巧五：保存常用提示词</h3>
<p>免费版可以保存1套自定义提示词，建议保存：</p>
<ul>
<li><strong>项目规范提示词：</strong>描述项目的代码风格、架构模式、技术栈</li>
<li><strong>调试提示词：</strong>标准化的bug诊断和修复流程</li>
<li><strong>代码审查提示词：</strong>自动审查代码质量、安全性和性能</li>
</ul>

<h2>Cursor 与竞品对比</h2>

<table>
<tr><th>工具</th><th>免费额度</th><th>月费</th><th>核心优势</th></tr>
<tr><td><strong>Cursor AI</strong></td><td>200条Chat/月<br>50次Fast/天<br>100次Tab/天</td><td>$20/月</td><td>基于VS Code，生态丰富，多模型支持</td></tr>
<tr><td>Claude Code</td><td>~100-200条/天</td><td>$20/月</td><td>终端原生，深度代码库理解</td></tr>
<tr><td>GitHub Copilot</td><td>学生/教师免费</td><td>$10/月</td><td>GitHub生态集成，完整IDE支持</td></tr>
<tr><td>Windsurf</td><td>个人免费</td><td>$10/月</td><td>Flow状态，上下文感知补全</td></tr>
<tr><td>Gemini CLI</td><td>个人免费（限速）</td><td>API按量计费</td><td>Google生态，Gemini模型</td></tr>
<tr><td>Aider</td><td>完全免费（开源）</td><td>$0</td><td>开源CLI，自带API密钥无限制</td></tr>
</table>

<h2>常见问题 FAQ</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: Cursor 免费版真的完全免费吗？需要信用卡吗？</div>
<div class="faq-a">是的，Cursor免费版完全免费，注册时<strong>不需要提供信用卡</strong>。免费版每月200条Chat消息，足够个人开发者日常使用。如果需要更多额度，可以升级到Pro版（$20/月）。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 免费版可以修改代码吗？还是只能聊天？</div>
<div class="faq-a">免费版<strong>可以修改代码</strong>。通过Chat、Composer Mode（每月10次）和Agent Mode（每月5次）都可以生成和编辑代码。但高级功能如Copilot++超高速补全仅限Pro版。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 额度过后还能用吗？</div>
<div class="faq-a">可以。当Fast Model和Tab补全额度过后，你仍然可以：<br>
1. 使用Slow/Background模式（无限，但响应慢）<br>
2. 等待第二天16:00（北京时间）额度重置<br>
3. 升级到Pro版解除所有限制</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 免费版支持哪些编程语言？</div>
<div class="faq-a">Cursor支持<strong>50多种编程语言</strong>，包括Python、JavaScript/TypeScript、Go、Rust、Java、C++、Swift、Kotlin等主流语言，以及HTML/CSS、SQL、Markdown等标记语言。所有语言在免费版中功能完整。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Cursor免费版可以商用吗？</div>
<div class="faq-a">可以。Cursor免费版没有功能限制，生成的代码你可以自由用于商业项目。唯一的限制是使用次数（200条Chat/月等）。对于商业团队使用，建议考虑Pro版或Team版。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 如何查看我的剩余额度？</div>
<div class="faq-a">在Cursor编辑器中，点击右上角的设置图标（齿轮），选择"Usage"或"Billing"，即可查看当前的额度使用情况，包括Chat消息、Fast Model请求、Tab补全等的剩余次数。</div>
</div>
</div>

<h2>总结</h2>

<p>Cursor AI 免费版在2026年仍然是<strong>最值得尝试的AI编程工具之一</strong>。虽然200条Chat消息/月和50次Fast Model/天的限制听起来不多，但对于：</p>

<ul>
<li><strong>日常编码辅助：</strong>Tab补全+Chat问答，完全够用</li>
<li><strong>学习新语言：</strong>AI解释代码、生成示例，高效入门</li>
<li><strong>小型项目：</strong>50K文件以下的代码库，索引功能完整可用</li>
<li><strong>非高峰期使用：</strong>Slow模式配合优质提示词，效果不输付费版</li>
</ul>

<p>如果你已经习惯了VS Code的工作流，Cursor几乎是无缝迁移的最佳选择。立即前往 <a href="https://cursor.sh" target="_blank">cursor.sh</a> 下载安装，开启你的AI编程之旅吧！</p>
"""
    
    content_en = """<h1>Cursor AI Free Tier: The Definitive 2026 Guide</h1>

<p><strong>Cursor AI</strong> has rapidly become the most popular AI-powered code editor in 2026. Built on top of the open-source VS Code platform, Cursor deeply integrates AI capabilities directly into the development workflow, allowing developers to interact with code using natural language. The best part? <strong>Cursor offers a genuinely useful free tier</strong> that lets you experience core AI programming features without spending a dime.</p>

<h2>What Is Cursor AI?</h2>

<p>Cursor AI is developed by <strong>Anysphere</strong> and built on a fork of Visual Studio Code. This means:</p>

<ul>
<li><strong>Full VS Code compatibility:</strong> All VS Code extensions, themes, and keyboard shortcuts work identically in Cursor</li>
<li><strong>Zero learning curve:</strong> If you've used VS Code, you'll feel right at home</li>
<li><strong>Cross-platform support:</strong> Available for Windows, macOS, and Linux</li>
</ul>

<p>As of July 2026, Cursor has penetrated over <strong>18% of the global developer market</strong>, supporting <strong>50+ programming languages</strong> and covering web development, data science, mobile development, and more.</p>

<h2>Cursor AI Free Tier Details (July 2026)</h2>

<h3>Free Allowance Overview</h3>

<table>
<tr><th>Feature</th><th>Free Tier Allowance</th><th>Notes</th></tr>
<tr><td><strong>Chat Messages/Month</strong></td><td><strong>200 messages</strong></td><td>Each message sent in the Chat panel counts as one. 200 messages lasts roughly 15-20 days of light daily use.</td></tr>
<tr><td><strong>Fast Model Requests</strong></td><td><strong>50/day</strong></td><td>Daily fast-response quota. After exceeding, you can still use slow/background mode.</td></tr>
<tr><td><strong>Tab Autocomplete</strong></td><td><strong>100/day</strong></td><td>Daily limit for intelligent code completion via Tab key.</td></tr>
<tr><td><strong>Slow/Background Requests</strong></td><td><strong>Unlimited</strong></td><td>Slower responses but no daily cap. Uses more capable models.</td></tr>
<tr><td><strong>Composer Mode</strong></td><td><strong>10/month</strong></td><td>Multi-file AI generation and editing. Very limited on free tier.</td></tr>
<tr><td><strong>Agent Mode</strong></td><td><strong>5/month</strong></td><td>Autonomous multi-step agent tasks. Severely limited on free tier.</td></tr>
<tr><td><strong>Codebase Indexing</strong></td><td><strong>Up to 50,000 files</strong></td><td>Projects over 50K files may require upgrading.</td></tr>
<tr><td><strong>Available Models</strong></td><td>Claude 3.5 Sonnet, GPT-4o, Gemini 2.0</td><td>Premium models (Claude 3.7 Sonnet Max) require Pro.</td></tr>
<tr><td><strong>Custom Instructions</strong></td><td><strong>1 set</strong></td><td>Pro allows up to 20 custom instruction sets.</td></tr>
<tr><td><strong>History Retention</strong></td><td><strong>14 days</strong></td><td>Pro retains history for 30 days.</td></tr>
</table>

<h3>Daily Reset Mechanism</h3>

<p><strong>⏰ Reset Time:</strong> The daily Fast Model Requests (50) and Tab Autocomplete (100) reset at <strong>00:00 Pacific Time (PT)</strong>, which corresponds to <strong>16:00 Beijing Time</strong>. Plan your high-intensity AI interactions before 4 PM Beijing time for optimal results.</p>

<h3>Features Not Available on Free Tier</h3>

<table>
<tr><th>Feature</th><th>Free Tier</th><th>Pro Plan ($20/mo)</th></tr>
<tr><td>Copilot++ Ultra-Fast Autocomplete</td><td>❌ Not Available</td><td>✅ Included</td></tr>
<tr><td>Chat Messages/Month</td><td>200</td><td>5,000 (25x more)</td></tr>
<tr><td>Fast Model/Day</td><td>50</td><td>500 (10x more)</td></tr>
<tr><td>Tab Autocomplete/Day</td><td>100</td><td>500</td></tr>
<tr><td>Composer Mode</td><td>10/month</td><td>Unlimited</td></tr>
<tr><td>Agent Mode</td><td>5/month</td><td>Unlimited</td></tr>
<tr><td>Codebase Index Size</td><td>50,000 files</td><td>Unlimited</td></tr>
<tr><td>Priority Queue</td><td>❌ Lowest priority</td><td>✅ High priority</td></tr>
<tr><td>Premium Models</td><td>❌ Basic models only</td><td>✅ Claude 3.7 Sonnet Max, etc.</td></tr>
<tr><td>Team Collaboration</td><td>❌ Not Available</td><td>✅ Included</td></tr>
</table>

<h2>How to Sign Up for Cursor AI (Free Tier)</h2>

<ol>
<li><strong>Download Cursor:</strong> Visit <a href="https://cursor.sh" target="_blank">cursor.sh</a> and download the latest version for your OS (Windows, macOS, or Linux).</li>
<li><strong>Install the Editor:</strong> Run the installer. Cursor installs to a separate directory and will not overwrite your existing VS Code installation.</li>
<li><strong>Create an Account:</strong> Launch Cursor and sign up using one of these methods:
<ul>
<li>Google account (recommended for fastest setup)</li>
<li>GitHub account</li>
<li>Microsoft account</li>
<li>Email and password</li>
</ul>
</li>
<li><strong>Verify Your Email:</strong> Check your inbox for a verification link from Cursor and click it to activate your account.</li>
<li><strong>Import VS Code Settings (Optional):</strong> Cursor will ask if you want to import your VS Code settings, extensions, and keybindings during onboarding. Highly recommended for a seamless transition.</li>
<li><strong>Start Using:</strong> Once activated, you can immediately use all free-tier features. Check your usage counters in Settings under "Usage" or "Billing."</li>
</ol>

<div style="background:#eef2ff;border:2px solid #6366f1;border-radius:8px;padding:18px;margin:20px 0;">
<strong>💡 Pro Tip:</strong> If you already use VS Code, import your settings and extensions to preserve your familiar development environment. The transition should be nearly seamless.
</div>

<h2>Cursor Free vs Pro: Detailed Comparison</h2>

<table>
<tr><th>Feature</th><th>Free Tier</th><th>Pro Plan ($20/mo)</th><th>Pro Plan (Annual, $16/mo)</th></tr>
<tr><td>Chat Messages/Month</td><td>200</td><td>5,000 (25x)</td><td>5,000 (25x)</td></tr>
<tr><td>Fast Model/Day</td><td>50</td><td>500 (10x)</td><td>500 (10x)</td></tr>
<tr><td>Slow/Background</td><td>Unlimited</td><td>Unlimited</td><td>Unlimited</td></tr>
<tr><td>Tab Autocomplete/Day</td><td>100</td><td>500</td><td>500</td></tr>
<tr><td>Composer Mode</td><td>10/month</td><td>Unlimited</td><td>Unlimited</td></tr>
<tr><td>Agent Mode</td><td>5/month</td><td>Unlimited</td><td>Unlimited</td></tr>
<tr><td>Codebase Index</td><td>50,000 files</td><td>Unlimited</td><td>Unlimited</td></tr>
<tr><td>Priority Queue</td><td>❌</td><td>✅</td><td>✅</td></tr>
<tr><td>Premium Models</td><td>❌</td><td>✅</td><td>✅</td></tr>
<tr><td>Team Collaboration</td><td>❌</td><td>✅</td><td>✅</td></tr>
</table>

<h2>Tips for Maximizing Cursor's Free Tier</h2>

<h3>Tip 1: Strategically Allocate Your Daily Quota</h3>
<p>With only 50 Fast Model requests and 100 Tab completions per day, consider these strategies:</p>
<ul>
<li><strong>Morning golden hours:</strong> After the 16:00 Beijing Time reset, tackle your most complex AI-assisted tasks first</li>
<li><strong>Slow mode for emergencies:</strong> When quota runs out, switch to Slow/Background mode — it's unlimited and uses stronger models</li>
<li><strong>Batch your questions:</strong> Combine multiple questions into a single message to save Chat quota</li>
</ul>

<h3>Tip 2: Leverage Slow Model Effectively</h3>
<p>The free tier offers <strong>unlimited</strong> Slow/Background mode access. While responses take longer, these requests use <strong>more capable models</strong>. For non-urgent tasks like code review and architecture analysis, Slow mode can actually produce better results.</p>

<h3>Tip 3: Optimize Your Prompts</h3>
<p>High-quality prompts can:</p>
<ul>
<li>Reduce iteration rounds, saving each reply's message quota</li>
<li>Achieve more accurate results, reducing the need to re-prompt</li>
<li>Fully utilize the context window for better codebase understanding</li>
</ul>
<p><strong>Effective prompt formula:</strong> [Role] + [Task] + [Context] + [Output Format]</p>

<h3>Tip 4: Maximize Tab Autocomplete</h3>
<p>Tab autocomplete is Cursor's most quota-efficient feature:</p>
<ul>
<li>Simply press Tab to accept suggestions — doesn't count against Chat quota</li>
<li>100 daily completions is ample for everyday coding</li>
<li>Combined with AI-generated code snippets, dramatically boosts productivity</li>
</ul>

<h3>Tip 5: Save Your Most-Used Prompts</h3>
<p>Free tier allows 1 custom prompt set. Save templates for:</p>
<ul>
<li><strong>Project conventions:</strong> Describe your code style, architecture patterns, and tech stack</li>
<li><strong>Debugging workflow:</strong> Standardized bug diagnosis and fix processes</li>
<li><strong>Code review:</strong> Automated quality, security, and performance review prompts</li>
</ul>

<h2>Cursor vs. Competitors</h2>

<table>
<tr><th>Tool</th><th>Free Tier</th><th>Monthly Cost</th><th>Key Advantage</th></tr>
<tr><td><strong>Cursor AI</strong></td><td>200 Chat/mo<br>50 Fast/day<br>100 Tab/day</td><td>$20/mo</td><td>VS Code-based, rich ecosystem, multi-model support</td></tr>
<tr><td>Claude Code</td><td>~100-200/day</td><td>$20/mo</td><td>Terminal-native, deep codebase understanding</td></tr>
<tr><td>GitHub Copilot</td><td>Free for students</td><td>$10/mo</td><td>GitHub ecosystem integration</td></tr>
<tr><td>Windsurf</td><td>Free for individuals</td><td>$10/mo</td><td>Flow state, context-aware completions</td></tr>
<tr><td>Gemini CLI</td><td>Free personal (rate-limited)</td><td>API pay-per-use</td><td>Google ecosystem, Gemini models</td></tr>
<tr><td>Aider</td><td>Completely free (open source)</td><td>$0</td><td>Open-source CLI, bring-your-own-key, no limits</td></tr>
</table>

<h2>Frequently Asked Questions</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: Is Cursor's free tier truly free? Do I need a credit card?</div>
<div class="faq-a">Yes, Cursor's free tier is completely free, and <strong>no credit card is required</strong> to sign up. The free tier provides 200 Chat messages per month, which is sufficient for individual developers' daily needs. Upgrade to Pro ($20/mo) only if you need higher quotas.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Can I modify code on the free tier, or is it chat-only?</div>
<div class="faq-a">The free tier <strong>can modify code</strong>. You can generate and edit code through Chat, Composer Mode (10 times/month), and Agent Mode (5 times/month). Advanced features like Copilot++ ultra-fast autocomplete require Pro.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Can I still use Cursor after running out of quota?</div>
<div class="faq-a">Yes! When Fast Model and Tab quotas are exhausted, you can still:
1. Use Slow/Background mode (unlimited, but slower responses)
2. Wait until 16:00 Beijing Time for daily quota reset
3. Upgrade to Pro to remove all restrictions</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: What programming languages does Cursor support?</div>
<div class="faq-a">Cursor supports <strong>50+ programming languages</strong>, including Python, JavaScript/TypeScript, Go, Rust, Java, C++, Swift, Kotlin, and more, plus markup languages like HTML/CSS, SQL, and Markdown. All languages have full functionality on the free tier.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Can I use Cursor's free tier for commercial projects?</div>
<div class="faq-a">Yes. Cursor's free tier has no functional restrictions, and code generated can be freely used in commercial projects. The only limitation is usage quotas (200 Chat messages/month, etc.). For team commercial use, consider upgrading to Pro or Team plans.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: How do I check my remaining quota?</div>
<div class="faq-a">In the Cursor editor, click the settings icon (gear) in the top-right corner, then select "Usage" or "Billing" to view your current quota usage, including remaining Chat messages, Fast Model requests, and Tab completions.</div>
</div>
</div>

<h2>Summary</h2>

<p>Cursor AI's free tier remains <strong>one of the most compelling AI programming tools in 2026</strong>. While the limits of 200 Chat messages/month and 50 Fast Model requests/day might seem restrictive, they are more than sufficient for:</p>

<ul>
<li><strong>Daily coding assistance:</strong> Tab autocomplete + Chat Q&A, perfectly adequate</li>
<li><strong>Learning new languages:</strong> AI code explanation and example generation for efficient onboarding</li>
<li><strong>Small projects:</strong> Codebase indexing works completely for projects under 50K files</li>
<li><strong>Off-peak usage:</strong> Slow mode paired with quality prompts delivers results comparable to paid tiers</li>
</ul>

<p>If you're already familiar with VS Code's workflow, Cursor is virtually a seamless migration. Visit <a href="https://cursor.sh" target="_blank">cursor.sh</a> to download and start your AI-powered coding journey today!</p>
"""

    faq_zh = """
      {\"@type\": \"Question\", \"name\": \"Cursor 免费版真的完全免费吗？需要信用卡吗？\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"是的，Cursor免费版完全免费，注册时不需要提供信用卡。免费版每月200条Chat消息，足够个人开发者日常使用。\"}},
      {\"@type\": \"Question\", \"name\": \"免费版可以修改代码吗？\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"可以。通过Chat、Composer Mode（每月10次）和Agent Mode（每月5次）都可以生成和编辑代码。\"}},
      {\"@type\": \"Question\", \"name\": \"额度过后还能用吗？\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"可以。额度过后可使用Slow/Background模式（无限），或等待次日16:00重置，或升级到Pro版。\"}},
      {\"@type\": \"Question\", \"name\": \"Cursor免费版支持哪些编程语言？\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"支持50多种编程语言，包括Python、JavaScript/TypeScript、Go、Rust、Java、C++等。\"}},
      {\"@type\": \"Question\", \"name\": \"免费版可以商用吗？\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"可以。生成的代码可自由用于商业项目，唯一的限制是使用次数。\"}}
    """
    
    faq_en = """
      {\"@type\": \"Question\", \"name\": \"Is Cursor's free tier truly free? Do I need a credit card?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"Yes, Cursor's free tier is completely free with no credit card required. It provides 200 Chat messages per month, sufficient for individual developers.\"}},
      {\"@type\": \"Question\", \"name\": \"Can I modify code on the free tier?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"Yes. You can generate and edit code through Chat, Composer Mode (10 times/month), and Agent Mode (5 times/month).\"}},
      {\"@type\": \"Question\", \"name\": \"Can I still use Cursor after running out of quota?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"Yes. After quota exhaustion, you can use Slow/Background mode (unlimited), wait for the next day's 16:00 reset, or upgrade to Pro.\"}},
      {\"@type\": \"Question\", \"name\": \"What programming languages does Cursor support?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"Supports 50+ programming languages including Python, JavaScript/TypeScript, Go, Rust, Java, C++, and more.\"}},
      {\"@type\": \"Question\", \"name\": \"Can I use the free tier for commercial projects?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"Yes. Code generated can be freely used in commercial projects. The only limitation is usage quotas.\"}}
    """
    
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
    
    print(f"Generated guide: {slug}")
    print(f"  - zh/guides/{slug}.html")
    print(f"  - en/guides/{slug}.html")
    print(f"  - Date: {today}")

def generate_guide_html(slug, title_zh, title_en, description_zh, description_en, content_zh, content_en, faq_zh, faq_en, date_published):
    """Generate guide HTML pages"""
    zh_html = f'''<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_zh} | AIFreePlan</title>
<meta property="og:type" content="article">
<meta property="og:title" content="{title_zh} | AIFreePlan">
<meta property="og:description" content="{description_zh}">
<meta property="og:url" content="https://aifreeplan.com/zh/guides/{slug}">
<meta property="og:site_name" content="AIFreePlan">
<meta property="og:locale" content="zh_CN">
<meta property="og:image" content="https://aifreeplan.com/og-image.png">
<meta name="twitter:image" content="https://aifreeplan.com/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title_zh} | AIFreePlan">
<meta name="twitter:description" content="{description_zh}">
<meta name="description" content="{description_zh}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<meta name="theme-color" content="#6366F1">
<link rel="canonical" href="https://aifreeplan.com/zh/guides/{slug}">
<link rel="alternate" hreflang="zh" href="https://aifreeplan.com/zh/guides/{slug}">
<link rel="alternate" hreflang="en" href="https://aifreeplan.com/en/guides/{slug}">
<link rel="alternate" hreflang="x-default" href="https://aifreeplan.com/en/guides/{slug}">
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
.breadcrumb{{font-size:14px;color:var(--text-muted);margin-bottom:24px}}
.breadcrumb a{{color:var(--text-muted);text-decoration:none}}
.breadcrumb a:hover{{color:var(--accent)}}
.breadcrumb-sep{{margin:0 8px}}
.faq-section{{background:var(--bg-white);border-radius:var(--radius);padding:32px;margin-top:40px;box-shadow:var(--shadow)}}
.faq-section h3{{margin-top:0;color:var(--text)}}
.faq-item{{margin-bottom:20px;padding-bottom:20px;border-bottom:1px solid var(--border-light)}}
.faq-item:last-child{{border-bottom:none;margin-bottom:0;padding-bottom:0}}
.faq-q{{font-weight:700;color:var(--text);margin-bottom:8px}}
.faq-a{{color:var(--text-secondary);line-height:1.7}}
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
{{"@context":"https://schema.org","@type":"Article","headline":"{title_zh}","description":"{description_zh}","url":"https://aifreeplan.com/zh/guides/{slug}","datePublished":"{date_published}","dateModified":"{date_published}","author":{{"@type":"Organization","name":"AIFreePlan"}},"publisher":{{"@type":"Organization","name":"AIFreePlan","url":"https://aifreeplan.com"}},"mainEntityOfPage":{{"@type":"WebPage","@id":"https://aifreeplan.com/zh/guides/{slug}"}}}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"首页","item":"https://aifreeplan.com/zh"}},{{"@type":"ListItem","position":2,"name":"攻略","item":"https://aifreeplan.com/zh/guides"}},{{"@type":"ListItem","position":3,"name":"{title_zh}","item":"https://aifreeplan.com/zh/guides/{slug}"}}]}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_zh}]}}
</script>
</head>
<body>
<header class="header">
  <div class="container header-inner">
    <a href="/zh" class="logo">AI<span class="accent">FreePlan</span></a>
    <nav class="nav">
      <a href="/zh/all">全部工具</a>
      <a href="/zh/guides">攻略</a>
      <a href="/zh/privacy">隐私</a>
      <a href="/en/guides/{slug}" class="btn btn-primary">English</a>
    </nav>
  </div>
</header>
<main class="article-container">
<nav class="breadcrumb"><a href="/zh">首页</a> <span class="breadcrumb-sep">›</span> <a href="/zh/guides">攻略</a> <span class="breadcrumb-sep">›</span> <span>{title_zh}</span></nav>
{content_zh}
</main>
<footer class="footer">
  <div class="container footer-inner">
    <div class="footer-brand"><a href="/zh" class="logo" style="color:#059669">AI<span class="accent" style="color:#6366F1">FreePlan</span></a><p>AI驱动的免费工具聚合平台，永久免费。</p></div>
    <div class="footer-links">
      <div class="footer-col"><h4>产品</h4><a href="/zh/all">全部工具</a><a href="/zh/guides">攻略</a></div>
      <div class="footer-col"><h4>法律</h4><a href="/zh/privacy">隐私政策</a><a href="/zh/terms">用户协议</a></div>
    </div>
  </div>
  <div class="container footer-bottom">&copy; 2026 AIFreePlan. All rights reserved.</div>
</footer>
</body></html>'''
    
    en_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_en} | AIFreePlan</title>
<meta property="og:type" content="article">
<meta property="og:title" content="{title_en} | AIFreePlan">
<meta property="og:description" content="{description_en}">
<meta property="og:url" content="https://aifreeplan.com/en/guides/{slug}">
<meta property="og:site_name" content="AIFreePlan">
<meta property="og:locale" content="en_US">
<meta property="og:image" content="https://aifreeplan.com/og-image.png">
<meta name="twitter:image" content="https://aifreeplan.com/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title_en} | AIFreePlan">
<meta name="twitter:description" content="{description_en}">
<meta name="description" content="{description_en}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<meta name="theme-color" content="#6366F1">
<link rel="canonical" href="https://aifreeplan.com/en/guides/{slug}">
<link rel="alternate" hreflang="zh" href="https://aifreeplan.com/zh/guides/{slug}">
<link rel="alternate" hreflang="en" href="https://aifreeplan.com/en/guides/{slug}">
<link rel="alternate" hreflang="x-default" href="https://aifreeplan.com/en/guides/{slug}">
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
.breadcrumb{{font-size:14px;color:var(--text-muted);margin-bottom:24px}}
.breadcrumb a{{color:var(--text-muted);text-decoration:none}}
.breadcrumb a:hover{{color:var(--accent)}}
.breadcrumb-sep{{margin:0 8px}}
.faq-section{{background:var(--bg-white);border-radius:var(--radius);padding:32px;margin-top:40px;box-shadow:var(--shadow)}}
.faq-section h3{{margin-top:0;color:var(--text)}}
.faq-item{{margin-bottom:20px;padding-bottom:20px;border-bottom:1px solid var(--border-light)}}
.faq-item:last-child{{border-bottom:none;margin-bottom:0;padding-bottom:0}}
.faq-q{{font-weight:700;color:var(--text);margin-bottom:8px}}
.faq-a{{color:var(--text-secondary);line-height:1.7}}
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
{{"@context":"https://schema.org","@type":"Article","headline":"{title_en}","description":"{description_en}","url":"https://aifreeplan.com/en/guides/{slug}","datePublished":"{date_published}","dateModified":"{date_published}","author":{{"@type":"Organization","name":"AIFreePlan"}},"publisher":{{"@type":"Organization","name":"AIFreePlan","url":"https://aifreeplan.com"}},"mainEntityOfPage":{{"@type":"WebPage","@id":"https://aifreeplan.com/en/guides/{slug}"}}}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://aifreeplan.com/en"}},{{"@type":"ListItem","position":2,"name":"Guides","item":"https://aifreeplan.com/en/guides"}},{{"@type":"ListItem","position":3,"name":"{title_en}","item":"https://aifreeplan.com/en/guides/{slug}"}}]}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_en}]}}
</script>
</head>
<body>
<header class="header">
  <div class="container header-inner">
    <a href="/en" class="logo">AI<span class="accent">FreePlan</span></a>
    <nav class="nav">
      <a href="/en/all">All Tools</a>
      <a href="/en/guides">Guides</a>
      <a href="/en/privacy">Privacy</a>
      <a href="/zh/guides/{slug}" class="btn btn-primary">中文</a>
    </nav>
  </div>
</header>
<main class="article-container">
<nav class="breadcrumb"><a href="/en">Home</a> <span class="breadcrumb-sep">›</span> <a href="/en/guides">Guides</a> <span class="breadcrumb-sep">›</span> <span>{title_en}</span></nav>
{content_en}
</main>
<footer class="footer">
  <div class="container footer-inner">
    <div class="footer-brand"><a href="/en" class="logo" style="color:#059669">AI<span class="accent" style="color:#6366F1">FreePlan</span></a><p>AI-powered free tools aggregator. Free forever.</p></div>
    <div class="footer-links">
      <div class="footer-col"><h4>Product</h4><a href="/en/all">All Tools</a><a href="/en/guides">Guides</a></div>
      <div class="footer-col"><h4>Legal</h4><a href="/en/privacy">Privacy</a><a href="/en/terms">Terms</a></div>
    </div>
  </div>
  <div class="container footer-bottom">&copy; 2026 AIFreePlan. All rights reserved.</div>
</footer>
</body></html>'''
    
    return zh_html, en_html

if __name__ == '__main__':
    main()
