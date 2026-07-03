#!/usr/bin/env python3
"""Generate and save a guide article for Amazon Q Developer."""
import os
import sys
from datetime import datetime

sys.path.insert(0, '/home/ubuntu/aifreeplan/scripts')
from write_guide import generate_guide_html

def main():
    today = datetime.now().strftime('%Y-%m-%d')
    slug = "amazon-q-developer-free-tier-2026"
    
    title_zh = "Amazon Q Developer 完全免费攻略：AWS 官方 AI 编程助手，无限代码补全+聊天+安全扫描"
    title_en = "Amazon Q Developer Free Tier Guide 2026: AWS's Official AI Coding Assistant with Unlimited Completions, Chat & Security Scanning"
    desc_zh = "Amazon Q Developer 是 AWS 推出的官方 AI 编程助手，免费版提供无限代码补全、无限对话聊天、代码解释、安全漏洞扫描等功能，支持 VS Code、JetBrains、CLI 等多平台，完全免费无需信用卡。"
    desc_en = "Amazon Q Developer is AWS's official AI coding assistant. The free tier offers unlimited code completions, unlimited chat conversations, code explanation, security vulnerability scanning, and more. Supports VS Code, JetBrains, CLI across multiple platforms — completely free with no credit card required."
    
    content_zh = """<h1>Amazon Q Developer 完全免费攻略：AWS 官方 AI 编程助手</h1>

<p>Amazon Q Developer 是亚马逊 AWS 在 2023 年底推出、2024 年全面推广的<strong>官方 AI 编程助手</strong>。它与 GitHub Copilot 和 Cursor 竞争，但最大的亮点在于<strong>免费版的功能极其慷慨</strong>——不限次数、不限制对话轮数、不隐藏核心功能。以下是截至 2026 年 6 月的最新免费额度详情。</p>

<h2>Amazon Q Developer 是什么？</h2>

<p>Amazon Q Developer 基于 AWS 自研的 Amazon Bedrock 大语言模型，专为软件开发者和 IT 专业人员设计。它不是简单的代码补全工具，而是一个<strong>完整的 AI 编程生态系统</strong>，涵盖代码生成、对话问答、安全审计、测试生成等多个维度。</p>

<ul>
<li><strong>开发者：</strong>Amazon Web Services (AWS)</li>
<li><strong>底层模型：</strong>Amazon Bedrock（支持 Claude、Llama、Titan 等多种模型）</li>
<li><strong>支持平台：</strong>VS Code、JetBrains IDE（IntelliJ、PyCharm、GoLand 等）、Visual Studio、AWS CLI、AWS Toolkit for Eclipse</li>
<li><strong>免费额度：</strong>几乎所有核心功能<strong>无限使用</strong></li>
<li><strong>付费档位：</strong>专业版 $39/月/用户（额外功能）</li>
</ul>

<h2>免费版 vs 专业版对比</h2>

<p>这是 Amazon Q Developer 最核心的价值所在。免费版已经覆盖了大多数个人开发者的全部需求：</p>

<table>
<tr><th>功能</th><th>免费版</th><th>专业版（$39/月）</th></tr>
<tr><td>代码补全</td><td>✅ 无限次数</td><td>✅ 无限次数</td></tr>
<tr><td>聊天对话</td><td>✅ 无限次数</td><td>✅ 无限次数 + 企业知识库</td></tr>
<tr><td>代码解释</td><td>✅ 支持</td><td>✅ 支持</td></tr>
<tr><td>代码转换（跨语言迁移）</td><td>❌ 不支持</td><td>✅ Java → Python 等</td></tr>
<tr><td>安全扫描</td><td>✅ 基础安全扫描</td><td>✅ 深度安全扫描 + 合规报告</td></tr>
<tr><td>测试生成</td><td>✅ 单元测试生成</td><td>✅ 集成测试 + E2E 测试</td></tr>
<tr><td>CLI 辅助</td><td>✅ 支持</td><td>✅ 支持</td></tr>
<tr><td>企业知识库</td><td>❌ 不支持</td><td>✅ 可连接内部文档</td></tr>
<tr><td>团队管理</td><td>❌ 不支持</td><td>✅ 管理员面板</td></tr>
</table>

<p>可以看到，<strong>免费版已经包含了代码补全、聊天、代码解释、测试生成等核心功能</strong>，而且是无限使用的。专业版的差异化主要在企业级功能（知识库、跨语言迁移、深度安全扫描）。</p>

<h2>免费额度详解</h2>

<h3>1. 代码补全（Code Recommendations）</h3>

<p>免费版提供<strong>无限次数的代码补全</strong>。当你在 IDE 中编写代码时，Amazon Q 会根据上下文自动推荐整行甚至整段代码。这与 GitHub Copilot 的免费版类似，但 Amazon Q 的推荐质量得益于 Bedrock 后端的多模型支持。</p>

<p><strong>关键数字：</strong>无限次推荐，无速率限制，支持 20+ 编程语言（Python、Java、JavaScript、TypeScript、Go、Rust、C++、Ruby、PHP、C#、Terraform、CloudFormation 等）。</p>

<h3>2. 聊天对话（Chat）</h3>

<p>Amazon Q 的聊天功能是最强大的免费功能之一。<strong>没有限制对话次数和消息长度</strong>。你可以用它来：</p>

<ul>
<li>解释复杂代码的含义</li>
<li>生成新功能代码片段</li>
<li>调试错误信息</li>
<li>询问 AWS 服务用法（如 S3、Lambda、DynamoDB）</li>
<li>生成文档注释</li>
<li>翻译代码（不同语言间）</li>
</ul>

<p><strong>关键数字：</strong>无限对话次数，每次对话最长支持 10,000 行代码上下文，支持多轮追问。</p>

<h3>3. 安全扫描（Security Scan）</h3>

<p>免费版提供<strong>无限次安全扫描</strong>。Amazon Q 会分析你的代码中的安全漏洞，包括 OWASP Top 10 问题（SQL 注入、XSS、敏感数据泄露等），并提供修复建议。</p>

<p><strong>关键数字：</strong>无限扫描次数，支持 CI/CD 集成（GitHub Actions、GitLab CI、Jenkins），扫描结果可直接在 IDE 中查看。</p>

<h3>4. 测试生成（Test Generation）</h3>

<p>免费版支持<strong>无限次单元测试生成</strong>。Amazon Q 可以分析你的函数和类，自动生成覆盖主要路径的测试用例，支持 JUnit（Java）、pytest（Python）、Jest（JavaScript）等主流测试框架。</p>

<p><strong>关键数字：</strong>无限生成次数，支持 Java、Python、JavaScript/TypeScript 三大语言的单元测试生成。</p>

<h2>安装和使用步骤</h2>

<h3>步骤 1：创建 AWS 账号</h3>

<p>访问 <a href="https://aws.amazon.com/q/developer/">AWS Q Developer 官网</a>，使用你的 AWS 账号登录。如果没有账号，可以免费注册 AWS Free Tier（包含 12 个月的免费额度，但不影响 Q Developer 免费版的使用）。</p>

<p><strong>注意：</strong>Q Developer 免费版<strong>不需要绑定信用卡</strong>，只需要一个 AWS 账号即可。</p>

<h3>步骤 2：安装 IDE 插件</h3>

<p>根据你的编辑器选择安装：</p>

<ul>
<li><strong>VS Code：</strong>在扩展市场搜索 "Amazon Q"，点击安装。安装后在侧边栏出现 Q 图标。</li>
<li><strong>JetBrains IDE：</strong>在 Plugins 市场搜索 "Amazon Q"，安装后重启 IDE。</li>
<li><strong>Visual Studio：</strong>从 Microsoft Store 安装 "Amazon Q for Visual Studio"。</li>
</ul>

<h3>步骤 3：登录并开始使用</h3>

<p>安装完成后，点击 IDE 中的 Amazon Q 图标，选择 "Sign in with AWS"，按提示完成授权。登录后即可开始使用代码补全和聊天功能。</p>

<h2>与 GitHub Copilot 免费版的对比</h2>

<table>
<tr><th>功能</th><th>Amazon Q Developer（免费）</th><th>GitHub Copilot（免费）</th></tr>
<tr><td>代码补全</td><td>✅ 无限</td><td>✅ 个人版免费（限学生/维护者）</td></tr>
<tr><td>聊天对话</td><td>✅ 无限</td><td>✅ 有（但免费用户需订阅 Pro）</td></tr>
<tr><td>安全扫描</td><td>✅ 免费无限</td><td>❌ 仅 Pro 版（$19/月）</td></tr>
<tr><td>测试生成</td><td>✅ 免费</td><td>❌ 需 Pro 版</td></tr>
<tr><td>支持语言</td><td>20+ 种</td><td>15+ 种</td></tr>
<tr><td>IDE 支持</td><td>VS Code、JetBrains、VS、Eclipse</td><td>VS Code、JetBrains、Neovim、VS</td></tr>
<tr><td>AWS 服务集成</td><td>✅ 深度集成</td><td>❌ 无</td></tr>
<tr><td>需要信用卡</td><td>❌ 不需要</td><td>❌ 不需要（免费版）</td></tr>
</table>

<p><strong>结论：</strong>如果你使用 AWS 或者对安全扫描、测试生成有需求，Amazon Q Developer 免费版的功能远胜于 GitHub Copilot 的免费策略。Copilot 的免费版仅限于学生和开源维护者，而 Amazon Q 对所有人开放无限免费。</p>

<h2>与 Cursor 的对比</h2>

<table>
<tr><th>功能</th><th>Amazon Q Developer（免费）</th><th>Cursor（免费）</th></tr>
<tr><td>代码补全</td><td>✅ 无限</td><td>⚠️ 300 次/月</td></tr>
<tr><td>聊天对话</td><td>✅ 无限</td><td>⚠️ 100 次/月</td></tr>
<tr><td>IDE</td><td>任意 IDE（插件形式）</td><td>仅 Cursor IDE（基于 VS Code 修改）</td></tr>
<tr><td>安全扫描</td><td>✅ 免费</td><td>❌ 无</td></tr>
<tr><td>价格</td><td>完全免费</td><td>免费受限，Hobby $20/月</td></tr>
</table>

<p>Cursor 的免费版限制非常严格（每月仅 300 次补全 + 100 次对话），而 Amazon Q 免费版<strong>完全不限次数</strong>。虽然 Cursor 的代码生成质量在某些场景下略优，但 Amazon Q 在免费额度上的优势是压倒性的。</p>

<h2>实际使用体验</h2>

<h3>代码补全质量</h3>

<p>Amazon Q 的代码补全基于 Bedrock 后端，支持切换不同的底层模型。在 Python 和 Java 场景下表现优秀，能准确理解项目上下文并生成符合规范的代码。对于 AWS 相关的代码（如 Boto3 SDK、Terraform 配置），补全准确率尤其高。</p>

<h3>聊天功能</h3>

<p>聊天功能最实用的场景是<strong>AWS 服务学习</strong>。你可以问 "如何在 Lambda 中读取 S3 文件？"，Q 会生成完整的代码示例并解释每一步。对于非 AWS 问题，也能给出高质量的回答。</p>

<h3>安全扫描</h3>

<p>安全扫描是 Amazon Q 最具差异化的免费功能。它能识别常见的安全漏洞类型，包括：</p>

<ul>
<li>硬编码密钥/凭证</li>
<li>SQL 注入风险</li>
<li>XSS（跨站脚本攻击）</li>
<li>不安全的加密算法</li>
<li>权限过度授予（IAM 策略问题）</li>
</ul>

<p>每个漏洞都会附带<strong>严重程度评级</strong>（高/中/低）和<strong>修复建议代码</strong>。</p>

<h2>常见问题</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: Amazon Q Developer 免费版真的完全免费吗？有什么隐藏限制？</div>
<div class="faq-a">是的，核心功能（代码补全、聊天、安全扫描、测试生成）对所有人完全免费且无限使用。唯一的限制是企业级功能（知识库、跨语言迁移、深度安全报告）需要付费专业版。没有隐藏的费用，也不需要绑定信用卡。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 免费版的数据会被用于训练模型吗？</div>
<div class="faq-a">不会。AWS 明确承诺不会使用客户代码或对话数据来训练模型。你的代码和对话内容仅用于为你提供服务的目的。</div>
</div>

<div class="faq-q">Q: 支持中文对话吗？</div>
<div class="faq-a">支持。Amazon Q 的聊天功能支持多语言对话，包括中文。你可以用中文提问，它会用中文回答。代码补全则不受语言影响，因为它是基于代码语法的。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 可以在生产环境中使用免费版吗？</div>
<div class="faq-a">可以。AWS 没有禁止在 production 中使用免费版。但如果你是企业用户，建议评估专业版是否更适合你的需求（特别是知识库和深度安全扫描功能）。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Amazon Q 和 GitHub Copilot 可以同时安装吗？</div>
<div class="faq-a">可以。它们互不冲突，可以同时安装和启用。你可以根据场景灵活选择使用哪个工具。</div>
</div>
</div>

<h2>总结</h2>

<p>Amazon Q Developer 是目前<strong>免费额度最慷慨的 AI 编程助手</strong>。无限次的代码补全、聊天对话、安全扫描和测试生成，这些功能在竞品中大多被锁在付费墙后面。对于个人开发者、学生、以及正在使用 AWS 的团队来说，这是一个不可错过的工具。</p>

<p>立即前往 <a href="https://aws.amazon.com/q/developer/">AWS Q Developer 官网</a> 注册使用吧！</p>
"""
    
    content_en = """<h1>Amazon Q Developer Free Tier Guide 2026: AWS's Official AI Coding Assistant</h1>

<p>Amazon Q Developer is Amazon Web Services' <strong>official AI coding assistant</strong>, launched at the end of 2023 and fully rolled out in 2024. It competes with GitHub Copilot and Cursor, but its biggest advantage is that the <strong>free tier is incredibly generous</strong> — unlimited usage, no conversation limits, no core features hidden behind a paywall. Here are the latest free tier details as of June 2026.</p>

<h2>What is Amazon Q Developer?</h2>

<p>Amazon Q Developer is built on AWS's proprietary Amazon Bedrock large language models, designed specifically for software developers and IT professionals. It's not just a simple code completion tool — it's a <strong>complete AI programming ecosystem</strong> covering code generation, conversational Q&A, security auditing, test generation, and more.</p>

<ul>
<li><strong>Developer:</strong> Amazon Web Services (AWS)</li>
<li><strong>Underlying Models:</strong> Amazon Bedrock (supports Claude, Llama, Titan, and other models)</li>
<li><strong>Supported Platforms:</strong> VS Code, JetBrains IDEs (IntelliJ, PyCharm, GoLand, etc.), Visual Studio, AWS CLI, AWS Toolkit for Eclipse</li>
<li><strong>Free Tier:</strong> Almost all core features are <strong>unlimited</strong></li>
<li><strong>Paid Tier:</strong> Professional — $39/month/user (additional features)</li>
</ul>

<h2>Free Tier vs. Professional Plan Compared</h2>

<p>This is the core value proposition of Amazon Q Developer. The free tier already covers all the needs of most individual developers:</p>

<table>
<tr><th>Feature</th><th>Free Tier</th><th>Professional ($39/month)</th></tr>
<tr><td>Code Completions</td><td>✅ Unlimited</td><td>✅ Unlimited</td></tr>
<tr><td>Chat Conversations</td><td>✅ Unlimited</td><td>✅ Unlimited + Enterprise Knowledge Base</td></tr>
<tr><td>Code Explanation</td><td>✅ Supported</td><td>✅ Supported</td></tr>
<tr><td>Code Transformation (Cross-language Migration)</td><td>❌ Not Available</td><td>✅ Java → Python, etc.</td></tr>
<tr><td>Security Scanning</td><td>✅ Basic Security Scan</td><td>✅ Deep Security Scan + Compliance Reports</td></tr>
<tr><td>Test Generation</td><td>✅ Unit Test Generation</td><td>✅ Integration Tests + E2E Tests</td></tr>
<tr><td>CLI Assistance</td><td>✅ Supported</td><td>✅ Supported</td></tr>
<tr><td>Enterprise Knowledge Base</td><td>❌ Not Available</td><td>✅ Connect to Internal Docs</td></tr>
<tr><td>Team Management</td><td>❌ Not Available</td><td>✅ Admin Dashboard</td></tr>
</table>

<p>As you can see, <strong>the free tier already includes code completions, chat, code explanation, and test generation</strong> — all unlimited. The Professional plan differentiates mainly with enterprise-grade features (knowledge base, cross-language migration, deep security scanning).</p>

<h2>Free Tier Details</h2>

<h3>1. Code Completions</h3>

<p>The free tier offers <strong>unlimited code completion recommendations</strong>. As you write code in your IDE, Amazon Q automatically suggests entire lines or even full code blocks based on context. This is similar to GitHub Copilot's free tier, but Q's recommendation quality benefits from multi-model support on the Bedrock backend.</p>

<p><strong>Key Numbers:</strong> Unlimited recommendations, no rate limiting, supports 20+ programming languages (Python, Java, JavaScript, TypeScript, Go, Rust, C++, Ruby, PHP, C#, Terraform, CloudFormation, and more).</p>

<h3>2. Chat Conversations</h3>

<p>Amazon Q's chat feature is one of the most powerful free features available. <strong>No limits on conversation count or message length</strong>. You can use it to:</p>

<ul>
<li>Explain complex code logic</li>
<li>Generate new feature code snippets</li>
<li>Debug error messages</li>
<li>Ask about AWS service usage (S3, Lambda, DynamoDB, etc.)</li>
<li>Generate documentation comments</li>
<li>Translate code between languages</li>
</ul>

<p><strong>Key Numbers:</strong> Unlimited conversations, each supporting up to 10,000 lines of code context, with multi-turn follow-up capability.</p>

<h3>3. Security Scanning</h3>

<p>The free tier provides <strong>unlimited security scans</strong>. Amazon Q analyzes your code for security vulnerabilities, including OWASP Top 10 issues (SQL injection, XSS, sensitive data exposure, etc.) and provides fix suggestions.</p>

<p><strong>Key Numbers:</strong> Unlimited scan count, supports CI/CD integration (GitHub Actions, GitLab CI, Jenkins), scan results viewable directly in the IDE.</p>

<h3>4. Test Generation</h3>

<p>The free tier supports <strong>unlimited unit test generation</strong>. Amazon Q can analyze your functions and classes, automatically generating test cases that cover main code paths. It supports JUnit (Java), pytest (Python), Jest (JavaScript), and other mainstream testing frameworks.</p>

<p><strong>Key Numbers:</strong> Unlimited generation, supports unit test generation for Java, Python, and JavaScript/TypeScript.</p>

<h2>Installation and Setup</h2>

<h3>Step 1: Create an AWS Account</h3>

<p>Visit the <a href="https://aws.amazon.com/q/developer/">AWS Q Developer website</a> and sign in with your AWS account. If you don't have one, you can register for free (the AWS Free Tier includes 12 months of free services, but this doesn't affect Q Developer's free tier availability).</p>

<p><strong>Note:</strong> Q Developer's free tier <strong>does not require a credit card</strong> — just an AWS account.</p>

<h3>Step 2: Install the IDE Plugin</h3>

<p>Install based on your editor:</p>

<ul>
<li><strong>VS Code:</strong> Search "Amazon Q" in the Extensions marketplace and click Install. The Q icon appears in the sidebar after installation.</li>
<li><strong>JetBrains IDEs:</strong> Search "Amazon Q" in the Plugins marketplace, install, and restart the IDE.</li>
<li><strong>Visual Studio:</strong> Install "Amazon Q for Visual Studio" from the Microsoft Store.</li>
</ul>

<h3>Step 3: Sign In and Start Using</h3>

<p>After installation, click the Amazon Q icon in your IDE, select "Sign in with AWS," and follow the authorization prompts. Once signed in, you can start using code completions and chat immediately.</p>

<h2>Comparison with GitHub Copilot Free Tier</h2>

<table>
<tr><th>Feature</th><th>Amazon Q Developer (Free)</th><th>GitHub Copilot (Free)</th></tr>
<tr><td>Code Completions</td><td>✅ Unlimited</td><td>✅ Free for individuals (students/maintainers only)</td></tr>
<tr><td>Chat Conversations</td><td>✅ Unlimited</td><td>✅ Available (but free users need Pro subscription)</td></tr>
<tr><td>Security Scanning</td><td>✅ Free unlimited</td><td>❌ Pro only ($19/month)</td></tr>
<tr><td>Test Generation</td><td>✅ Free</td><td>❌ Pro only</td></tr>
<tr><td>Languages Supported</td><td>20+</td><td>15+</td></tr>
<tr><td>IDE Support</td><td>VS Code, JetBrains, VS, Eclipse</td><td>VS Code, JetBrains, Neovim, VS</td></tr>
<tr><td>AWS Service Integration</td><td>✅ Deep integration</td><td>❌ None</td></tr>
<tr><td>Credit Card Required</td><td>❌ No</td><td>❌ No (free tier)</td></tr>
</table>

<p><strong>Verdict:</strong> If you use AWS or need security scanning and test generation, Amazon Q Developer's free tier far outperforms GitHub Copilot's free strategy. Copilot's free version is limited to students and open-source maintainers, while Amazon Q offers unlimited free access to everyone.</p>

<h2>Comparison with Cursor</h2>

<table>
<tr><th>Feature</th><th>Amazon Q Developer (Free)</th><th>Cursor (Free)</th></tr>
<tr><td>Code Completions</td><td>✅ Unlimited</td><td>⚠️ 300/month</td></tr>
<tr><td>Chat Conversations</td><td>✅ Unlimited</td><td>⚠️ 100/month</td></tr>
<tr><td>IDE</td><td>Any IDE (plugin format)</td><td>Cursor IDE only (fork of VS Code)</td></tr>
<tr><td>Security Scanning</td><td>✅ Free</td><td>❌ Not available</td></tr>
<tr><td>Price</td><td>Completely free</td><td>Free with limits, Hobby $20/month</td></tr>
</table>

<p>Cursor's free tier is very restrictive (only 300 completions + 100 chats per month), while Amazon Q's free tier is <strong>completely unlimited</strong>. Although Cursor's code generation quality may be slightly better in some scenarios, Amazon Q's advantage in free tier generosity is overwhelming.</p>

<h2>Real-World Usage Experience</h2>

<h3>Code Completion Quality</h3>

<p>Amazon Q's code completions are powered by the Bedrock backend with support for switching between different underlying models. Performance is excellent in Python and Java scenarios, accurately understanding project context and generating规范-compliant code. For AWS-related code (e.g., Boto3 SDK, Terraform configurations), completion accuracy is particularly high.</p>

<h3>Chat Functionality</h3>

<p>The chat feature is most practical for <strong>AWS service learning</strong>. You can ask "How do I read an S3 file in Lambda?" and Q will generate a complete code example with step-by-step explanations. For non-AWS questions, it also delivers high-quality answers.</p>

<h3>Security Scanning</h3>

<p>Security scanning is Amazon Q's most differentiated free feature. It identifies common vulnerability types including:</p>

<ul>
<li>Hardcoded secrets/credentials</li>
<li>SQL injection risks</li>
<li>XSS (Cross-Site Scripting)</li>
<li>Insecure cryptographic algorithms</li>
<li>Overly permissive IAM policies</li>
</ul>

<p>Each vulnerability comes with a <strong>severity rating</strong> (high/medium/low) and <strong>fix suggestion code</strong>.</p>

<h2>Frequently Asked Questions</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: Is Amazon Q Developer's free tier really completely free? Any hidden limits?</div>
<div class="faq-a">Yes. Core features (code completions, chat, security scanning, test generation) are completely free and unlimited for everyone. The only limitations are enterprise-grade features (knowledge base, cross-language migration, deep security reports) which require the Professional plan. No hidden fees, no credit card required.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Will my code be used to train models?</div>
<div class="faq-a">No. AWS explicitly commits to not using customer code or conversation data to train models. Your code and conversations are used solely for providing you with the service.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Does it support non-English conversations?</div>
<div class="faq-a">Yes. Amazon Q's chat supports multilingual conversations including Chinese, Japanese, Korean, German, French, Spanish, and more. Code completions are language-agnostic since they're based on code syntax.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Can I use the free tier in production?</div>
<div class="faq-a">Yes. AWS does not prohibit using the free tier in production environments. However, if you're an enterprise user, consider whether the Professional plan better suits your needs (especially the knowledge base and deep security scanning features).</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Can I install both Amazon Q and GitHub Copilot simultaneously?</div>
<div class="faq-a">Yes. They don't conflict and can be installed and enabled together. You can flexibly choose which tool to use depending on the scenario.</div>
</div>
</div>

<h2>Conclusion</h2>

<p>Amazon Q Developer is currently the <strong>most generous free-tier AI coding assistant on the market</strong>. Unlimited code completions, chat conversations, security scanning, and test generation — features that competitors lock behind paywalls are all free here. For individual developers, students, and teams using AWS, this is an essential tool you shouldn't miss.</p>

<p>Get started now at <a href="https://aws.amazon.com/q/developer/">AWS Q Developer</a>!</p>
"""
    
    faq_zh = """{"@type":"Question","name":"Amazon Q Developer 免费版真的完全免费吗？有什么隐藏限制？","acceptedAnswer":{"@type":"Answer","text":"是的，核心功能（代码补全、聊天、安全扫描、测试生成）对所有人完全免费且无限使用。唯一的限制是企业级功能（知识库、跨语言迁移、深度安全报告）需要付费专业版。没有隐藏的费用，也不需要绑定信用卡。"}},{"@type":"Question","name":"免费版的数据会被用于训练模型吗？","acceptedAnswer":{"@type":"Answer","text":"不会。AWS 明确承诺不会使用客户代码或对话数据来训练模型。你的代码和对话内容仅用于为你提供服务的目的。"}},{"@type":"Question","name":"可以在生产环境中使用免费版吗？","acceptedAnswer":{"@type":"Answer","text":"可以。AWS 没有禁止在 production 中使用免费版。但如果你是企业用户，建议评估专业版是否更适合你的需求。"}},{"@type":"Question","name":"Amazon Q 和 GitHub Copilot 可以同时安装吗？","acceptedAnswer":{"@type":"Answer","text":"可以。它们互不冲突，可以同时安装和启用。你可以根据场景灵活选择使用哪个工具。"}}"""
    
    faq_en = """{"@type":"Question","name":"Is Amazon Q Developer's free tier really completely free? Any hidden limits?","acceptedAnswer":{"@type":"Answer","text":"Yes. Core features (code completions, chat, security scanning, test generation) are completely free and unlimited for everyone. The only limitations are enterprise-grade features which require the Professional plan. No hidden fees, no credit card required."}},{"@type":"Question","name":"Will my code be used to train models?","acceptedAnswer":{"@type":"Answer","text":"No. AWS explicitly commits to not using customer code or conversation data to train models. Your code and conversations are used solely for providing you with the service."}},{"@type":"Question","name":"Can I use the free tier in production?","acceptedAnswer":{"@type":"Answer","text":"Yes. AWS does not prohibit using the free tier in production environments. However, enterprise users should consider whether the Professional plan better suits their needs."}},{"@type":"Question","name":"Can I install both Amazon Q and GitHub Copilot simultaneously?","acceptedAnswer":{"@type":"Answer","text":"Yes. They don't conflict and can be installed and enabled together. You can flexibly choose which tool to use depending on the scenario."}}"""
    
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
    
    # Quality check: Chinese chars in EN content
    import re
    cn_chars_en = len(re.findall(r'[\u4e00-\u9fff]', content_en))
    total_en = len(content_en)
    cn_ratio = cn_chars_en / total_en * 100 if total_en > 0 else 0
    print(f"   Chinese char ratio in EN content: {cn_ratio:.1f}%")
    if cn_ratio > 5:
        print("   ⚠️ WARNING: Too many Chinese characters in English content!")
    else:
        print("   ✅ Chinese character ratio OK (<5%)")

if __name__ == '__main__':
    main()