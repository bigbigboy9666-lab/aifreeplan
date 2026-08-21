#!/usr/bin/env python3
"""Generate Gemini Code Assist guide - direct HTML write"""
import os
import sys
from datetime import datetime

today = datetime.now().strftime('%Y-%m-%d')
slug = "gemini-code-assist-free-guide-2026"

title_zh = "Gemini Code Assist 完全免费：Google AI 编程助手，90倍于竞品的免费额度"
title_en = "Gemini Code Assist Free: Google's AI Coding Assistant with 90x Higher Limits"
desc_zh = "Google 推出免费版的 Gemini Code Assist，支持 VS Code、JetBrains 等主流编辑器，每月 90 万次代码补全请求，远超 GitHub Copilot 免费版限制。无需信用卡，注册 Google 账号即可使用。"
desc_en = "Google launched the free Gemini Code Assist for individuals, supporting VS Code, JetBrains and other mainstream editors. 900K code completion requests per month, far exceeding GitHub Copilot's free tier. No credit card required."

content_zh = """<h1>Gemini Code Assist 完全免费：Google AI 编程助手，90倍于竞品的免费额度</h1>

<p>2025年2月25日，Google 正式发布 <strong>Gemini Code Assist for Individuals</strong>（个人版），这是 Google 首款完全免费的 AI 编程助手。与付费企业版相比，个人版保留了核心功能，但额度大幅放宽——每月高达 <strong>90万次代码补全请求</strong>，是 GitHub Copilot 免费版的近90倍。</p>

<p>无论你是学生、独立开发者还是刚入行的程序员，都可以免费使用这款由 Gemini 大模型驱动的编程助手。</p>

<hr>

<h2>一、Gemini Code Assist 是什么</h2>

<p>Gemini Code Assist 是 Google 推出的 AI 编程助手，深度集成到主流开发环境中。它基于 Gemini 1.5 Pro 模型，能够理解代码上下文，提供智能补全、代码生成、错误修复等功能。</p>

<p><strong>核心能力：</strong></p>
<ul>
<li><strong>智能代码补全</strong> — 根据当前代码上下文，自动预测并补全接下来的代码</li>
<li><strong>代码解释</strong> — 选中代码片段，AI 会解释其功能和逻辑</li>
<li><strong>错误修复</strong> — 检测代码中的错误并提供修复建议</li>
<li><strong>代码转换</strong> — 将代码从一种语言转换为另一种语言</li>
<li><strong>对话式编程</strong> — 通过自然语言描述需求，AI 生成对应代码</li>
</ul>

<p>与 ChatGPT 或 Claude 不同，Gemini Code Assist 直接嵌入你的 IDE，不需要切换到浏览器，真正实现了"边写边用"。</p>

<h2>二、免费额度详解</h2>

<p>这是最有吸引力的部分——Google 给的免费额度非常慷慨：</p>

<table>
<thead>
<tr><th>功能</th><th>免费版额度</th><th>对比 GitHub Copilot</th></tr>
</thead>
<tbody>
<tr><td>代码补全请求</td><td><strong>90万次/月</strong></td><td>2,000次/月</td></tr>
<tr><td>代码解释</td><td>无限制</td><td>无限制</td></tr>
<tr><td>错误修复建议</td><td>无限制</td><td>无限制</td></tr>
<tr><td>自然语言生成代码</td><td>无限制</td><td>无限制</td></tr>
<tr><td>支持语言</td><td>20+ 主流语言</td><td>20+ 主流语言</td></tr>
<tr><td>IDE 支持</td><td>VS Code、JetBrains、Cursor</td><td>VS Code、JetBrains、Neovim</td></tr>
</tbody>
</table>

<p><strong>关键数字：</strong>每月 90万次代码补全请求，对于普通开发者来说，每天可以发送约 30,000 次请求，这远远超过了日常使用的需求。</p>

<h2>三、支持的开发环境</h2>

<p>Gemini Code Assist 支持以下主流 IDE 和编辑器：</p>

<h3>1. VS Code（推荐）</h3>
<p>在 VS Code 扩展市场中搜索 <strong>"Gemini Code Assist"</strong>，点击安装即可。安装后需要登录 Google 账号授权。</p>

<h3>2. JetBrains IDE</h3>
<p>支持 IntelliJ IDEA、PyCharm、WebStorm、GoLand 等 JetBrains 全家桶。在插件市场搜索安装即可。</p>

<h3>3. Cursor</h3>
<p>Cursor 编辑器已原生集成 Gemini Code Assist，可以直接在设置中启用。</p>

<h3>4. 其他编辑器</h3>
<p>计划支持 Neovim、Eclipse 等更多编辑器。</p>

<h2>四、如何注册和使用</h2>

<p>使用流程非常简单：</p>

<ol>
<li><strong>访问官网</strong> — 打开 <a href="https://gemini.google.com/code-assist">gemini.google.com/code-assist</a></li>
<li><strong>登录 Google 账号</strong> — 使用任意 Google 账号（Gmail、Chrome 账号均可）</li>
<li><strong>安装 IDE 插件</strong> — 在 VS Code 或 JetBrains 中搜索安装</li>
<li><strong>开始编码</strong> — 打开项目，AI 会自动开始提供代码补全和建议</li>
</ol>

<p><strong>注意事项：</strong></p>
<ul>
<li>不需要绑信用卡，完全免费</li>
<li>需要 Google 账号登录授权</li>
<li>目前支持美国、欧洲、印度等地区，中国大陆可能需要特殊网络环境</li>
</ul>

<h2>五、与 GitHub Copilot 免费版对比</h2>

<table>
<thead>
<tr><th>特性</th><th>Gemini Code Assist</th><th>GitHub Copilot</th></tr>
</thead>
<tbody>
<tr><td>月免费额度</td><td><strong>90万次</strong></td><td>2,000次</td></tr>
<tr><td>底层模型</td><td>Gemini 1.5 Pro</td><td>Claude 3.5 Sonnet</td></tr>
<tr><td>IDE 集成</td><td>VS Code、JetBrains、Cursor</td><td>VS Code、JetBrains、Neovim</td></tr>
<tr><td>价格（付费版）</td><td>免费</td><td>$10/月（个人版）</td></tr>
<tr><td>商用许可</td><td>个人非商用</td><td>个人非商用</td></tr>
</tbody>
</table>

<p>从数据来看，Gemini Code Assist 在免费额度上碾压 GitHub Copilot——90倍的优势意味着你可以肆无忌惮地让 AI 帮你写代码，不用担心额度耗尽。</p>

<h2>六、使用技巧</h2>

<p>为了充分利用这个免费工具，以下是几个实用技巧：</p>

<h3>1. 善用代码补全</h3>
<p>写代码时，AI 会自动预测你接下来要写的内容。按 Tab 键接受建议，按 Esc 键忽略。熟练使用后，编码速度可以提升 30% 以上。</p>

<h3>2. 用自然语言生成代码</h3>
<p>可以直接用中文或英文描述需求，例如："帮我写一个 Python 函数，计算斐波那契数列的第 n 项"，AI 会生成对应的代码。</p>

<h3>3. 让 AI 解释代码</h3>
<p>选中一段复杂代码，右键选择"解释代码"，AI 会用简洁的语言说明这段代码的功能和逻辑。</p>

<h3>4. 利用错误修复</h3>
<p>当代码出现错误时，AI 会高亮显示问题并提供修复建议。点击建议即可一键应用。</p>

<h3>5. 代码转换</h3>
<p>需要把 Java 代码改成 Python？选中代码后选择"转换语言"，AI 会自动完成转换。</p>

<h2>七、限制和注意事项</h2>

<p>虽然免费额度很慷慨，但还是有一些限制需要注意：</p>

<ul>
<li><strong>地区限制</strong> — 目前仅支持美国、欧洲、印度等地区，中国大陆用户可能需要特殊网络环境</li>
<li><strong>商用限制</strong> — 免费版仅限个人非商用，商业用途需要付费订阅</li>
<li><strong>功能限制</strong> — 部分高级功能（如自定义 AI 规则、团队协作）需要企业版</li>
<li><strong>稳定性</strong> — 作为预览版，偶尔可能出现响应慢或错误</li>
</ul>

<h2>八、总结</h2>

<p>Gemini Code Assist 是 Google 送给开发者的福利——每月 90万次免费代码补全请求，远超 GitHub Copilot 免费版 2,000 次的限制。无论你是学生、独立开发者还是刚入行的程序员，都可以免费使用这款由 Gemini 大模型驱动的编程助手。</p>

<p><strong>推荐使用场景：</strong></p>
<ul>
<li>学习编程语言时的智能提示</li>
<li>日常开发中的代码补全</li>
<li>代码审查和错误修复</li>
<li>代码解释和学习</li>
</ul>

<p><strong>立即开始：</strong>访问 <a href="https://gemini.google.com/code-assist">gemini.google.com/code-assist</a> 注册使用！</p>

<hr>

<p><em>本文最后更新于2026年8月21日。Gemini Code Assist 政策可能调整，请以官网最新说明为准。</em></p>
"""

content_en = """<h1>Gemini Code Assist Free: Google's AI Coding Assistant with 90x Higher Limits</h1>

<p>On February 25, 2025, Google officially launched <strong>Gemini Code Assist for Individuals</strong>, Google's first completely free AI coding assistant. Compared to the paid enterprise version, the personal version retains core features but with significantly expanded quotas — up to <strong>900,000 code completion requests per month</strong>, nearly 90 times that of GitHub Copilot's free tier.</p>

<p>Whether you're a student, indie developer, or just starting your programming journey, you can use this AI-powered coding assistant driven by the Gemini large model for free.</p>

<hr>

<h2>What is Gemini Code Assist?</h2>

<p>Gemini Code Assist is Google's AI coding assistant that deeply integrates into mainstream development environments. Based on the Gemini 1.5 Pro model, it understands code context and provides intelligent completion, code generation, error fixing, and other functions.</p>

<p><strong>Core Capabilities:</strong></p>
<ul>
<li><strong>Intelligent Code Completion</strong> — Automatically predicts and completes your next lines of code based on context</li>
<li><strong>Code Explanation</strong> — Select code snippets and AI will explain their functionality and logic</li>
<li><strong>Error Fixing</strong> — Detects errors in code and provides fix suggestions</li>
<li><strong>Code Translation</strong> — Converts code from one language to another</li>
<li><strong>Conversational Coding</strong> — Describe your needs in natural language, and AI generates the corresponding code</li>
</ul>

<p>Unlike ChatGPT or Claude, Gemini Code Assist embeds directly into your IDE, so you don't need to switch to a browser — truly achieving "code while using."</p>

<h2>Free Quota Details</h2>

<p>This is the most attractive part — Google gives very generous free quotas:</p>

<table>
<thead>
<tr><th>Feature</th><th>Free Tier Quota</th><th>vs GitHub Copilot</th></tr>
</thead>
<tbody>
<tr><td>Code Completion Requests</td><td><strong>900K/month</strong></td><td>2,000/month</td></tr>
<tr><td>Code Explanation</td><td>Unlimited</td><td>Unlimited</td></tr>
<tr><td>Error Fix Suggestions</td><td>Unlimited</td><td>Unlimited</td></tr>
<tr><td>Natural Language Code Generation</td><td>Unlimited</td><td>Unlimited</td></tr>
<tr><td>Supported Languages</td><td>20+ mainstream languages</td><td>20+ mainstream languages</td></tr>
<tr><td>IDE Support</td><td>VS Code, JetBrains, Cursor</td><td>VS Code, JetBrains, Neovim</td></tr>
</tbody>
</table>

<p><strong>Key Numbers:</strong> 900,000 code completion requests per month. For regular developers, that's about 30,000 requests per day — far exceeding daily usage needs.</p>

<h2>Supported Development Environments</h2>

<p>Gemini Code Assist supports the following mainstream IDEs and editors:</p>

<h3>1. VS Code (Recommended)</h3>
<p>Search for <strong>"Gemini Code Assist"</strong> in the VS Code extension marketplace and click install. After installation, you need to log in with your Google account for authorization.</p>

<h3>2. JetBrains IDE</h3>
<p>Supports IntelliJ IDEA, PyCharm, WebStorm, GoLand and the entire JetBrains family. Search and install from the plugin marketplace.</p>

<h3>3. Cursor</h3>
<p>The Cursor editor has natively integrated Gemini Code Assist, which you can enable directly in settings.</p>

<h3>4. Other Editors</h3>
<p>Plans to support Neovim, Eclipse and more editors.</p>

<h2>How to Register and Use</h2>

<p>The usage flow is very simple:</p>

<ol>
<li><strong>Visit the website</strong> — Open <a href="https://gemini.google.com/code-assist">gemini.google.com/code-assist</a></li>
<li><strong>Login with Google account</strong> — Use any Google account (Gmail, Chrome account all work)</li>
<li><strong>Install IDE plugin</strong> — Search and install in VS Code or JetBrains</li>
<li><strong>Start coding</strong> — Open your project, and AI will automatically start providing code completion and suggestions</li>
</ol>

<p><strong>Important Notes:</strong></p>
<ul>
<li>No credit card required, completely free</li>
<li>Google account login authorization required</li>
<li>Currently supports US, Europe, India and other regions; Chinese mainland users may need special network access</li>
</ul>

<h2>Comparison with GitHub Copilot Free</h2>

<table>
<thead>
<tr><th>Feature</th><th>Gemini Code Assist</th><th>GitHub Copilot</th></tr>
</thead>
<tbody>
<tr><td>Monthly Free Quota</td><td><strong>900,000</strong></td><td>2,000</td></tr>
<tr><td>Base Model</td><td>Gemini 1.5 Pro</td><td>Claude 3.5 Sonnet</td></tr>
<tr><td>IDE Integration</td><td>VS Code, JetBrains, Cursor</td><td>VS Code, JetBrains, Neovim</td></tr>
<tr><td>Price (Paid)</td><td>Free</td><td>$10/month (Personal)</td></tr>
<tr><td>Commercial License</td><td>Personal non-commercial</td><td>Personal non-commercial</td></tr>
</tbody>
</table>

<p>From the data, Gemini Code Assist crushes GitHub Copilot in free quotas — a 90x advantage means you can let AI help you write code without worrying about quota exhaustion.</p>

<h2>Usage Tips</h2>

<p>To make the most of this free tool, here are some practical tips:</p>

<h3>1. Master Code Completion</h3>
<p>When writing code, AI automatically predicts what you'll write next. Press Tab to accept suggestions, Esc to ignore. With proficiency, coding speed can increase by over 30%.</p>

<h3>2. Use Natural Language to Generate Code</h3>
<p>You can directly describe requirements in Chinese or English, e.g., "Help me write a Python function to calculate the nth term of the Fibonacci sequence," and AI will generate the corresponding code.</p>

<h3>3. Let AI Explain Code</h3>
<p>Select complex code, right-click and choose "Explain Code." AI will explain the functionality and logic in concise language.</p>

<h3>4. Leverage Error Fixing</h3>
<p>When code has errors, AI highlights the issues and provides fix suggestions. Click the suggestion to apply with one click.</p>

<h3>5. Code Translation</h3>
<p>Need to convert Java code to Python? Select the code and choose "Convert Language," and AI will complete the conversion automatically.</p>

<h2>Limits and Considerations</h2>

<p>While the free quota is generous, there are some limitations to be aware of:</p>

<ul>
<li><strong>Regional Restrictions</strong> — Currently only supports US, Europe, India and other regions; Chinese mainland users may need special network access</li>
<li><strong>Commercial Restrictions</strong> — Free version is for personal non-commercial use only; commercial use requires paid subscription</li>
<li><strong>Feature Limits</strong> — Some advanced features (custom AI rules, team collaboration) require enterprise version</li>
<li><strong>Stability</strong> — As a preview version, occasional slow responses or errors may occur</li>
</ul>

<h2>Conclusion</h2>

<p>Gemini Code Assist is a gift from Google to developers — 900,000 free code completion requests per month, far exceeding GitHub Copilot's free tier limit of 2,000. Whether you're a student, indie developer, or just starting your programming journey, you can use this AI-powered coding assistant driven by the Gemini large model for free.</p>

<p><strong>Recommended Use Cases:</strong></p>
<ul>
<li>Intelligent hints while learning programming languages</li>
<li>Code completion during daily development</li>
<li>Code review and error fixing</li>
<li>Code explanation and learning</li>
</ul>

<p><strong>Start Now:</strong> Visit <a href="https://gemini.google.com/code-assist">gemini.google.com/code-assist</a> to register and start using!</p>

<hr>

<p><em>Last updated: 2026-08-21. Gemini Code Assist policies may change, please refer to the official website for the latest information.</em></p>
"""

faq_zh = '[{"@type":"Question","name":"Gemini Code Assist 真的完全免费吗？","acceptedAnswer":{"@type":"Answer","text":"是的，Gemini Code Assist for Individuals 完全免费，每月提供 90 万次代码补全请求，无需绑信用卡。但仅限个人非商用，商业用途需要付费订阅。"}},{"@type":"Question","name":"支持哪些编辑器？","acceptedAnswer":{"@type":"Answer","text":"目前支持 VS Code、JetBrains 全家桶（IntelliJ IDEA、PyCharm、WebStorm、GoLand 等）、Cursor 编辑器。计划支持 Neovim、Eclipse 等更多编辑器。"}},{"@type":"Question","name":"和 GitHub Copilot 有什么区别？","acceptedAnswer":{"@type":"Answer","text":"主要区别是免费额度：Gemini Code Assist 每月 90 万次请求，GitHub Copilot 免费版仅 2,000 次。底层模型也不同：Gemini 基于 Gemini 1.5 Pro，Copilot 基于 Claude 3.5 Sonnet。"}},{"@type":"Question","name":"中国大陆可以用吗？","acceptedAnswer":{"@type":"Answer","text":"目前官方仅支持美国、欧洲、印度等地区，中国大陆可能需要特殊网络环境才能使用。建议关注官网公告获取最新支持地区信息。"}},{"@type":"Question","name":"可以用于商业用途吗？","acceptedAnswer":{"@type":"Answer","text":"免费版仅限个人非商用。如果用于商业项目或团队协作，需要订阅付费的企业版或个人版（$10/月）。"}}]'

faq_en = '[{"@type":"Question","name":"Is Gemini Code Assist really completely free?","acceptedAnswer":{"@type":"Answer","text":"Yes, Gemini Code Assist for Individuals is completely free, providing 900,000 code completion requests per month, no credit card required. But it\'s limited to personal non-commercial use only; commercial use requires a paid subscription."}},{"@type":"Question","name":"Which editors are supported?","acceptedAnswer":{"@type":"Answer","text":"Currently supports VS Code, JetBrains family (IntelliJ IDEA, PyCharm, WebStorm, GoLand, etc.), Cursor editor. Plans to support Neovim, Eclipse and more editors."}},{"@type":"Question","name":"What\'s the difference from GitHub Copilot?","acceptedAnswer":{"@type":"Answer","text":"The main difference is the free quota: Gemini Code Assist provides 900K requests per month, while GitHub Copilot\'s free tier only offers 2,000. The base models also differ: Gemini is based on Gemini 1.5 Pro, while Copilot is based on Claude 3.5 Sonnet."}},{"@type":"Question","name":"Can it be used in mainland China?","acceptedAnswer":{"@type":"Answer","text":"Currently the official support only covers US, Europe, India and other regions; Chinese mainland users may need special network access. Follow official announcements for the latest supported regions."}},{"@type":"Question","name":"Can I use it for commercial purposes?","acceptedAnswer":{"@type":"Answer","text":"The free version is for personal non-commercial use only. For commercial projects or team collaboration, you need to subscribe to the paid enterprise or personal version ($10/month)."}}]'

# Read the HTML generator
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