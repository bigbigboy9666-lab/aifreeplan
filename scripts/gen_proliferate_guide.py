#!/usr/bin/env python3
"""Generate Proliferate AI IDE guide article."""
import os
import sys
from datetime import datetime

def main():
    today = datetime.now().strftime('%Y-%m-%d')
    slug = "proliferate-ai-ide-free-2026"
    
    title_zh = "Proliferate AI IDE 完全免费：YC S25 推出的多Agent并行编程平台"
    title_en = "Proliferate AI IDE Free: YC-Backed Multi-Agent Parallel Coding Platform"
    desc_zh = "Proliferate 是 YC S25 支持的开源 AI IDE，支持 Claude Code、Codex、Cursor、Grok、OpenCode 等多种编程 Agent 并行工作，每个任务拥有独立的 Git worktree 隔离环境，完全免费使用。"
    desc_en = "Proliferate is a YC S25 backed open-source AI IDE that runs Claude Code, Codex, Cursor, Grok, and OpenCode agents in parallel. Each task gets isolated git worktrees, fully free and self-hostable."
    
    content_zh = """<h1>Proliferate AI IDE 完全免费使用攻略</h1>

<p>Proliferate 是一款刚刚发布的开源 AI IDE，由 Y Combinator S25 批次支持。它的核心理念是：<strong>在一个工作区中并行运行多个编程 Agent</strong>，每个 Agent 拥有独立的 Git worktree、分支、终端和对话状态。目前支持 Claude Code、Codex、OpenCode、Cursor 和 Grok 五大主流编程 Agent。</p>

<h2>什么是 Proliferate？</h2>

<p>Proliferate（https://github.com/proliferate-ai/proliferate）是一个开源的 AI 编程 IDE，设计目标是让开发者可以同时运行多个 AI Agent 协作完成复杂的软件工程任务。它的核心特性包括：</p>

<ul>
<li><strong>原生 Harness 支持：</strong>Claude Code、Codex、OpenCode、Cursor、Grok 五大 Agent，每个通过原生接口运行</li>
<li><strong>Worktree 工作区：</strong>每个任务获得独立的 Git worktree 和分支，完全隔离</li>
<li><strong>并行 Agent：</strong>在同一工作区中运行多个 Agent，各自处理不同任务</li>
<li><strong>子 Agent 系统：</strong>父 Agent 可以委派子任务给子 Agent，完成后自动合并结果</li>
<li><strong>工作流自动化：</strong>支持可重用的工作流，包括定时任务和事件驱动的执行链</li>
</ul>

<h2>支持的 Agent 列表</h2>

<table>
<tr><th>Agent</th><th>提供方</th><th>通过 Proliferate 运行</th></tr>
<tr><td><strong>Claude Code</strong></td><td>Anthropic</td><td>✅ 支持</td></tr>
<tr><td><strong>Codex</strong></td><td>OpenAI</td><td>✅ 支持</td></tr>
<tr><td><strong>OpenCode</strong></td><td>开源社区</td><td>✅ 支持</td></tr>
<tr><td><strong>Cursor</strong></td><td>Cursor Inc.</td><td>✅ 支持</td></tr>
<tr><td><strong>Grok</strong></td><td>xAI</td><td>✅ 支持</td></tr>
</table>

<h2>核心功能详解</h2>

<h3>1. Worktree 隔离工作区</h3>
<p>Proliferate 为每个任务创建独立的 Git worktree。这意味着：</p>
<ul>
<li>每个 Agent 在自己的分支上工作，不会互相干扰</li>
<li>可以同时测试多个不同的实现方案</li>
<li>代码变更完全隔离，便于对比和合并</li>
<li>每个 worktree 有自己的终端会话和对话历史</li>
</ul>

<p>例如，你可以同时让 Claude Code 优化算法性能，让 Codex 重构代码架构，让 Grok 生成测试用例——它们都在各自的分支上工作，互不冲突。</p>

<h3>2. 并行 Agent 系统</h3>
<p>Proliferate 的并行 Agent 功能允许你在同一个项目中同时运行多个 Agent。每个 Agent 有自己的：</p>
<ul>
<li>独立的 Git worktree 和分支</li>
<li>独立的终端会话</li>
<li>独立的对话历史</li>
<li>独立的任务状态和审查结果</li>
</ul>

<p>这种设计特别适合以下场景：</p>
<ul>
<li>同时探索多种技术方案</li>
<li>并行进行代码重构和特性开发</li>
<li>多个 Agent 协作完成复杂任务</li>
</ul>

<h3>3. 子 Agent 委托机制</h3>
<p>父 Agent 可以将特定子任务委派给子 Agent 执行。例如：</p>
<ul>
<li>主 Agent 负责架构设计</li>
<li>子 Agent A 负责数据库层实现</li>
<li>子 Agent B 负责 API 层实现</li>
<li>子 Agent C 负责测试编写</li>
</ul>

<p>所有子任务完成后，父 Agent 可以汇总结果并进行代码审查。</p>

<h3>4. 工作流自动化</h3>
<p>Proliferate 支持创建工作流，包括：</p>
<ul>
<li><strong>定时任务：</strong>夜间自动代码审查、依赖更新等</li>
<li><strong>事件驱动：</strong>代码推送后自动触发测试</li>
<li><strong>审批网关：</strong>人工审批节点，确保关键变更经过审核</li>
<li><strong>文档传递：</strong>步骤间自动传递文档和上下文</li>
</ul>

<h3>5. MCP 集成</h3>
<p>Proliferate 支持 MCP（Model Context Protocol）工具，包括：</p>
<ul>
<li>MCP 服务器配置</li>
<li>Skill 配置共享</li>
<li>Computer Use 工具集成</li>
<li>Browser Use 工具集成</li>
<li>自定义工具配置</li>
</ul>

<p>配置一次，所有 Agent 共享使用。</p>

<h2>安装和使用</h2>

<h3>方式一：桌面应用（推荐）</h3>
<p>Proliferate 提供 macOS 桌面应用，下载地址：</p>
<p><a href="https://proliferate.com">https://proliferate.com</a></p>

<p>安装步骤：</p>
<ol>
<li>访问官网下载 macOS 安装包</li>
<li>安装并打开应用</li>
<li>配置各 Agent 的 API Key（Claude Code 需要 Anthropic API Key，Codex 需要 OpenAI API Key 等）</li>
<li>创建新项目，选择工作区目录</li>
<li>开始使用并行 Agent 功能</li>
</ol>

<h3>方式二：自托管部署</h3>
<p>Proliferate 支持自托管部署，提供多种部署方式：</p>

<h4>Docker Compose 部署</h4>
<pre><code># 克隆仓库
git clone https://github.com/proliferate-ai/proliferate.git
cd proliferate

# 使用 Docker Compose 启动
docker-compose up -d

# 访问控制台
# 默认地址：http://localhost:3000
</code></pre>

<h4>AWS 一键部署</h4>
<p>Proliferate 提供 CloudFormation 模板，可以在 AWS 上一键部署：</p>
<pre><code># 使用 AWS CloudFormation 模板
# 详见文档：https://proliferate.com/docs/deployment
</code></pre>

<h4>支持的部署平台</h4>
<ul>
<li><strong>Docker Compose：</strong>本地或自有服务器部署</li>
<li><strong>AWS：</strong>CloudFormation 一键部署到 EC2</li>
<li><strong>GCP：</strong>Google Cloud Platform 部署</li>
<li><strong>Azure：</strong>微软 Azure 部署</li>
<li><strong>Kubernetes：</strong>K8s 集群部署</li>
<li><strong>Air-gapped：</strong>离线环境部署</li>
</ul>

<h2>使用场景示例</h2>

<h3>场景一：并行技术方案评估</h3>
<p>当需要评估多种技术方案时，可以：</p>
<ol>
<li>创建主任务：定义需求和技术规格</li>
<li>启动 Claude Code 子任务：实现方案 A</li>
<li>启动 Codex 子任务：实现方案 B</li>
<li>启动 Cursor 子任务：实现方案 C</li>
<li>比较各方案的性能、代码质量和可维护性</li>
</ol>

<h3>场景二：自动化代码审查工作流</h3>
<p>设置定时工作流：</p>
<ol>
<li>触发条件：每日凌晨或 PR 提交时</li>
<li>子任务 1：Claude Code 进行代码审查</li>
<li>子任务 2：Codex 检查安全问题</li>
<li>子任务 3：Grok 验证测试覆盖率</li>
<li>审批网关：人工审核审查结果</li>
<li>输出：生成审查报告并通知团队</li>
</ol>

<h3>场景三：大型重构项目</h3>
<p>对于大型代码库重构：</p>
<ol>
<li>父 Agent：制定重构计划和架构设计</li>
<li>子 Agent A：重构核心模块</li>
<li>子 Agent B：重构 API 接口</li>
<li>子 Agent C：更新测试用例</li>
<li>子 Agent D：更新文档</li>
<li>自动合并各分支，进行集成测试</li>
</ol>

<h2>与同类工具对比</h2>

<table>
<tr><th>特性</th><th>Proliferate</th><th>Claude Code</th><th>Codex CLI</th><th>Cursor</th></tr>
<tr><td>多 Agent 并行</td><td>✅ 支持</td><td>❌ 单 Agent</td><td>❌ 单 Agent</td><td>❌ 单 Agent</td></tr>
<tr><td>Worktree 隔离</td><td>✅ 支持</td><td>❌ 无</td><td>❌ 无</td><td>❌ 无</td></tr>
<tr><td>自托管</td><td>✅ 支持</td><td>❌ 云端</td><td>✅ 本地</td><td>✅ 本地</td></tr>
<tr><td>子 Agent 委托</td><td>✅ 支持</td><td>❌ 无</td><td>❌ 无</td><td>❌ 无</td></tr>
<tr><td>工作流自动化</td><td>✅ 支持</td><td>❌ 无</td><td>❌ 无</td><td>✅ 有限</td></tr>
<tr><td>开源</td><td>✅ AGPL-3.0</td><td>❌ 闭源</td><td>✅ 开源</td><td>❌ 闭源</td></tr>
<tr><td>MCP 集成</td><td>✅ 支持</td><td>❌ 不支持</td><td>❌ 不支持</td><td>✅ 部分</td></tr>
</table>

<h2>定价信息</h2>

<p>Proliferate 是<strong>完全免费</strong>的开源项目：</p>

<ul>
<li><strong>桌面应用：</strong>完全免费，无订阅费用</li>
<li><strong>自托管：</strong>完全免费，无额外费用</li>
<li><strong>API 费用：</strong>仅支付各 Agent 提供商的 API 费用（Claude Code、Codex 等）</li>
</ul>

<p>各 Agent 的 API 费用参考：</p>
<ul>
<li><strong>Claude Code：</strong>Anthropic API 标准定价</li>
<li><strong>Codex：</strong>OpenAI API 标准定价</li>
<li><strong>Cursor：</strong>Cursor 订阅费用（如使用）</li>
<li><strong>Grok：</strong>xAI API 定价</li>
<li><strong>OpenCode：</strong>根据配置的模型定价</li>
</ul>

<h2>常见问题</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: Proliferate 真的完全免费吗？</div>
<div class="faq-a">是的，Proliferate 本身完全免费。它采用 AGPL-3.0 许可证开源，桌面应用和自托管版本均无订阅费用。你只需支付使用的各 AI Agent 的 API 费用（如果有）。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Proliferate 支持 Windows 和 Linux 吗？</div>
<div class="faq-a">目前 Proliferate 主要支持 macOS。对于 Windows 和 Linux，建议使用自托管部署方式，通过 Docker 或 Kubernetes 部署后通过浏览器访问。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 需要配置哪些 API Key？</div>
<div class="faq-a">根据你想使用的 Agent，需要配置相应的 API Key：Claude Code 需要 Anthropic API Key，Codex 需要 OpenAI API Key，Cursor 需要 Cursor 订阅，Grok 需要 xAI API Key。可以在 Proliferate 设置中逐一配置。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: 如何升级 Proliferate？</div>
<div class="faq-a">桌面应用版本可通过官网下载最新版本。自托管版本可通过 git pull 更新代码后重新部署。</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Proliferate 适合个人开发者还是团队？</div>
<div class="faq-a">Proliferate 适合所有规模的开发者。个人开发者可以使用并行 Agent 功能加速开发，团队可以使用工作流自动化和子 Agent 委托机制提高协作效率。自托管版本特别适合企业团队。</div>
</div>
</div>

<h2>总结</h2>

<p>Proliferate 是一款创新的开源 AI IDE，由 YC S25 支持，解决了多 Agent 并行编程的痛点。它的核心优势在于：</p>

<ul>
<li>同时运行多个编程 Agent，每个拥有独立 worktree</li>
<li>支持 Claude Code、Codex、Cursor、Grok、OpenCode 五大主流 Agent</li>
<li>完全免费开源，支持自托管部署</li>
<li>提供子 Agent 委托和工作流自动化功能</li>
</ul>

<p>无论你是个人开发者还是团队领导，Proliferate 都能帮助你更高效地利用 AI 编程工具。立即前往 <a href="https://proliferate.com">https://proliferate.com</a> 下载试用！</p>"""

    content_en = """<h1>Proliferate AI IDE Free: YC-Backed Multi-Agent Parallel Coding Platform</h1>

<p>Proliferate is a newly released open-source AI IDE backed by Y Combinator S25. Its core philosophy: <strong>run multiple programming agents in parallel within a single workspace</strong>, each with isolated Git worktrees, branches, terminals, and conversation states. Currently supports Claude Code, Codex, OpenCode, Cursor, and Grok — five of the most popular coding agents.</p>

<h2>What is Proliferate?</h2>

<p>Proliferate (https://github.com/proliferate-ai/proliferate) is an open-source AI programming IDE designed to let developers run multiple AI agents simultaneously to collaborate on complex software engineering tasks. Its core features include:</p>

<ul>
<li><strong>Native Harness Support:</strong> Claude Code, Codex, OpenCode, Cursor, and Grok — each running through native interfaces</li>
<li><strong>Worktree Workspaces:</strong> Each task gets an isolated Git worktree and branch, completely sandboxed</li>
<li><strong>Parallel Agents:</strong> Run multiple agents side by side in the same workspace</li>
<li><strong>Subagent System:</strong> Parent agents can delegate subtasks to child agents and automatically merge results</li>
<li><strong>Workflow Automation:</strong> Support for reusable workflows including scheduled tasks and event-driven execution chains</li>
</ul>

<h2>Supported Agents</h2>

<table>
<tr><th>Agent</th><th>Provider</th><th>Supported in Proliferate</th></tr>
<tr><td><strong>Claude Code</strong></td><td>Anthropic</td><td>✅ Supported</td></tr>
<tr><td><strong>Codex</strong></td><td>OpenAI</td><td>✅ Supported</td></tr>
<tr><td><strong>OpenCode</strong></td><td>Open Source Community</td><td>✅ Supported</td></tr>
<tr><td><strong>Cursor</strong></td><td>Cursor Inc.</td><td>✅ Supported</td></tr>
<tr><td><strong>Grok</strong></td><td>xAI</td><td>✅ Supported</td></tr>
</table>

<h2>Core Features Explained</h2>

<h3>1. Worktree Isolated Workspaces</h3>
<p>Proliferate creates independent Git worktrees for each task. This means:</p>
<ul>
<li>Each agent works on its own branch without interfering with others</li>
<li>You can test multiple implementation approaches simultaneously</li>
<li>Code changes are fully isolated for easy comparison and merging</li>
<li>Each worktree has its own terminal session and conversation history</li>
</ul>

<p>For example, you can have Claude Code optimize algorithm performance, Codex refactor the code architecture, and Grok generate test cases — all working on their own branches simultaneously without conflicts.</p>

<h3>2. Parallel Agent System</h3>
<p>Proliferate's parallel agent feature lets you run multiple agents in the same project. Each agent has its own:</p>
<ul>
<li>Independent Git worktree and branch</li>
<li>Independent terminal session</li>
<li>Independent conversation history</li>
<li>Independent task status and review results</li>
</ul>

<p>This design is particularly suitable for:</p>
<ul>
<li>Evaluating multiple technical approaches simultaneously</li>
<li>Parallel code refactoring and feature development</li>
<li>Multiple agents collaborating on complex tasks</li>
</ul>

<h3>3. Subagent Delegation</h3>
<p>Parent agents can delegate specific subtasks to child agents. For example:</p>
<ul>
<li>Parent agent handles architecture design</li>
<li>Child Agent A implements database layer</li>
<li>Child Agent B implements API layer</li>
<li>Child Agent C writes tests</li>
</ul>

<p>After all subtasks complete, the parent agent can consolidate results and perform code review.</p>

<h3>4. Workflow Automation</h3>
<p>Proliferate supports creating workflows including:</p>
<ul>
<li><strong>Scheduled Tasks:</strong> Nightly automated code reviews, dependency updates</li>
<li><strong>Event-Driven:</strong> Trigger tests automatically on PR submission</li>
<li><strong>Approval Gates:</strong> Human approval checkpoints for critical changes</li>
<li><strong>Document Passing:</strong> Automatic document and context passing between steps</li>
</ul>

<h3>5. MCP Integration</h3>
<p>Proliferate supports MCP (Model Context Protocol) tools including:</p>
<ul>
<li>MCP server configuration</li>
<li>Skill configuration sharing</li>
<li>Computer Use tool integration</li>
<li>Browser Use tool integration</li>
<li>Custom tool configuration</li>
</ul>

<p>Configure once, share across all agents.</p>

<h2>Installation and Usage</h2>

<h3>Method 1: Desktop App (Recommended)</h3>
<p>Proliferate offers a macOS desktop application. Download from:</p>
<p><a href="https://proliferate.com">https://proliferate.com</a></p>

<p>Installation steps:</p>
<ol>
<li>Visit the official website to download the macOS installer</li>
<li>Install and launch the application</li>
<li>Configure API Keys for each agent (Claude Code needs Anthropic API Key, Codex needs OpenAI API Key, etc.)</li>
<li>Create a new project and select workspace directory</li>
<li>Start using the parallel agent feature</li>
</ol>

<h3>Method 2: Self-Hosted Deployment</h3>
<p>Proliferate supports self-hosted deployment with multiple options:</p>

<h4>Docker Compose Deployment</h4>
<pre><code># Clone the repository
git clone https://github.com/proliferate-ai/proliferate.git
cd proliferate

# Start with Docker Compose
docker-compose up -d

# Access the console
# Default address: http://localhost:3000
</code></pre>

<h4>AWS One-Click Deployment</h4>
<p>Proliferate provides CloudFormation templates for one-click deployment on AWS:</p>
<pre><code># Use AWS CloudFormation template
# See docs: https://proliferate.com/docs/deployment
</code></pre>

<h4>Supported Deployment Platforms</h4>
<ul>
<li><strong>Docker Compose:</strong> Local or self-hosted server deployment</li>
<li><strong>AWS:</strong> One-click deployment to EC2 via CloudFormation</li>
<li><strong>GCP:</strong> Google Cloud Platform deployment</li>
<li><strong>Azure:</strong> Microsoft Azure deployment</li>
<li><strong>Kubernetes:</strong> K8s cluster deployment</li>
<li><strong>Air-gapped:</strong> Offline environment deployment</li>
</ul>

<h2>Use Case Examples</h2>

<h3>Scenario 1: Parallel Technical Approach Evaluation</h3>
<p>When evaluating multiple technical approaches:</p>
<ol>
<li>Create main task: Define requirements and technical specifications</li>
<li>Launch Claude Code subtask: Implement Approach A</li>
<li>Launch Codex subtask: Implement Approach B</li>
<li>Launch Cursor subtask: Implement Approach C</li>
<li>Compare performance, code quality, and maintainability across approaches</li>
</ol>

<h3>Scenario 2: Automated Code Review Workflow</h3>
<p>Set up scheduled workflows:</p>
<ol>
<li>Trigger condition: Daily midnight or on PR submission</li>
<li>Subtask 1: Claude Code performs code review</li>
<li>Subtask 2: Codex checks for security issues</li>
<li>Subtask 3: Grok verifies test coverage</li>
<li>Approval gate: Human review of review results</li>
<li>Output: Generate review report and notify team</li>
</ol>

<h3>Scenario 3: Large-Scale Refactoring Project</h3>
<p>For large codebase refactoring:</p>
<ol>
<li>Parent Agent: Create refactoring plan and architecture design</li>
<li>Child Agent A: Refactor core modules</li>
<li>Child Agent B: Refactor API interfaces</li>
<li>Child Agent C: Update test cases</li>
<li>Child Agent D: Update documentation</li>
<li>Automatically merge branches and run integration tests</li>
</ol>

<h2>Comparison with Similar Tools</h2>

<table>
<tr><th>Feature</th><th>Proliferate</th><th>Claude Code</th><th>Codex CLI</th><th>Cursor</th></tr>
<tr><td>Multi-Agent Parallel</td><td>✅ Supported</td><td>❌ Single Agent</td><td>❌ Single Agent</td><td>❌ Single Agent</td></tr>
<tr><td>Worktree Isolation</td><td>✅ Supported</td><td>❌ None</td><td>❌ None</td><td>❌ None</td></tr>
<tr><td>Self-Hosted</td><td>✅ Supported</td><td>❌ Cloud Only</td><td>✅ Local</td><td>✅ Local</td></tr>
<tr><td>Subagent Delegation</td><td>✅ Supported</td><td>❌ None</td><td>❌ None</td><td>❌ None</td></tr>
<tr><td>Workflow Automation</td><td>✅ Supported</td><td>❌ None</td><td>❌ None</td><td>✅ Limited</td></tr>
<tr><td>Open Source</td><td>✅ AGPL-3.0</td><td>❌ Proprietary</td><td>✅ Open Source</td><td>❌ Proprietary</td></tr>
<tr><td>MCP Integration</td><td>✅ Supported</td><td>❌ Not Supported</td><td>❌ Not Supported</td><td>✅ Partial</td></tr>
</table>

<h2>Pricing Information</h2>

<p>Proliferate is <strong>completely free</strong> as an open-source project:</p>

<ul>
<li><strong>Desktop App:</strong> Completely free, no subscription fees</li>
<li><strong>Self-Hosted:</strong> Completely free, no additional charges</li>
<li><strong>API Costs:</strong> Only pay for the API fees of the AI agents used (Claude Code, Codex, etc.)</li>
</ul>

<p>Reference API costs for each agent:</p>
<ul>
<li><strong>Claude Code:</strong> Anthropic API standard pricing</li>
<li><strong>Codex:</strong> OpenAI API standard pricing</li>
<li><strong>Cursor:</strong> Cursor subscription fee (if applicable)</li>
<li><strong>Grok:</strong> xAI API pricing</li>
<li><strong>OpenCode:</strong> Pricing based on configured model</li>
</ul>

<h2>Frequently Asked Questions</h2>

<div class="faq-section">
<div class="faq-item">
<div class="faq-q">Q: Is Proliferate really completely free?</div>
<div class="faq-a">Yes, Proliferate itself is completely free. It's open-source under AGPL-3.0 license, with no subscription fees for either the desktop app or self-hosted versions. You only pay for the API costs of the AI agents you use.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Does Proliferate support Windows and Linux?</div>
<div class="faq-a">Currently Proliferate primarily supports macOS. For Windows and Linux, we recommend using the self-hosted deployment option via Docker or Kubernetes, accessible through a browser.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: What API Keys do I need to configure?</div>
<div class="faq-a">Depending on which agents you want to use: Claude Code needs Anthropic API Key, Codex needs OpenAI API Key, Cursor needs Cursor subscription, Grok needs xAI API Key. You can configure each in Proliferate settings.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: How do I upgrade Proliferate?</div>
<div class="faq-a">Desktop app versions can be downloaded from the official website. Self-hosted versions can be updated via git pull followed by redeployment.</div>
</div>

<div class="faq-item">
<div class="faq-q">Q: Is Proliferate suitable for individual developers or teams?</div>
<div class="faq-a">Proliferate suits developers of all sizes. Individual developers can use parallel agent features to accelerate development, while teams can leverage workflow automation and subagent delegation to improve collaboration. Self-hosted versions are particularly suitable for enterprise teams.</div>
</div>
</div>

<h2>Conclusion</h2>

<p>Proliferate is an innovative open-source AI IDE backed by YC S25, solving the pain points of multi-agent parallel programming. Its core advantages are:</p>

<ul>
<li>Run multiple programming agents simultaneously, each with independent worktree</li>
<li>Support Claude Code, Codex, Cursor, Grok, and OpenCode — five major coding agents</li>
<li>Completely free and open-source, supports self-hosted deployment</li>
<li>Provides subagent delegation and workflow automation features</li>
</ul>

<p>Whether you're an individual developer or a team leader, Proliferate can help you leverage AI coding tools more efficiently. Head over to <a href="https://proliferate.com">https://proliferate.com</a> to download and try it today!</p>"""

    faq_zh = """{"@type":"Question","name":"Proliferate 真的完全免费吗？","acceptedAnswer":{"@type":"Answer","text":"是的，Proliferate 本身完全免费。它采用 AGPL-3.0 许可证开源，桌面应用和自托管版本均无订阅费用。你只需支付使用的各 AI Agent 的 API 费用。"}},{"@type":"Question","name":"Proliferate 支持 Windows 和 Linux 吗？","acceptedAnswer":{"@type":"Answer","text":"目前 Proliferate 主要支持 macOS。对于 Windows 和 Linux，建议使用自托管部署方式，通过 Docker 或 Kubernetes 部署后通过浏览器访问。"}},{"@type":"Question","name":"需要配置哪些 API Key？","acceptedAnswer":{"@type":"Answer","text":"根据你想使用的 Agent，需要配置相应的 API Key：Claude Code 需要 Anthropic API Key，Codex 需要 OpenAI API Key，Cursor 需要 Cursor 订阅，Grok 需要 xAI API Key。可以在 Proliferate 设置中逐一配置。"}},{"@type":"Question","name":"Proliferate 适合个人开发者还是团队？","acceptedAnswer":{"@type":"Answer","text":"Proliferate 适合所有规模的开发者。个人开发者可以使用并行 Agent 功能加速开发，团队可以使用工作流自动化和子 Agent 委托机制提高协作效率。自托管版本特别适合企业团队。"}}"""

    faq_en = """{"@type":"Question","name":"Is Proliferate really completely free?","acceptedAnswer":{"@type":"Answer","text":"Yes, Proliferate itself is completely free. It's open-source under AGPL-3.0 license, with no subscription fees for either the desktop app or self-hosted versions. You only pay for the API costs of the AI agents you use."}},{"@type":"Question","name":"Does Proliferate support Windows and Linux?","acceptedAnswer":{"@type":"Answer","text":"Currently Proliferate primarily supports macOS. For Windows and Linux, we recommend using the self-hosted deployment option via Docker or Kubernetes, accessible through a browser."}},{"@type":"Question","name":"What API Keys do I need to configure?","acceptedAnswer":{"@type":"Answer","text":"Depending on which agents you want to use: Claude Code needs Anthropic API Key, Codex needs OpenAI API Key, Cursor needs Cursor subscription, Grok needs xAI API Key. You can configure each in Proliferate settings."}},{"@type":"Question","name":"Is Proliferate suitable for individual developers or teams?","acceptedAnswer":{"@type":"Answer","text":"Proliferate suits developers of all sizes. Individual developers can use parallel agent features to accelerate development, while teams can leverage workflow automation and subagent delegation to improve collaboration. Self-hosted versions are particularly suitable for enterprise teams."}}"""

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
    
    zh_char_count = len(content_zh.encode('utf-8'))
    en_char_count = len(content_en.encode('utf-8'))
    print(f"   Content length (ZH): {zh_char_count} bytes")
    print(f"   Content length (EN): {en_char_count} bytes")
    
    # Validate content length
    if zh_char_count < 1000 or en_char_count < 1000:
        print("❌ Content too short, regenerating...")
        sys.exit(1)
    
    # Check for Chinese characters in English content
    import re
    zh_chars_in_en = len(re.findall(r'[\u4e00-\u9fff]', content_en))
    en_total_chars = len(content_en)
    if en_total_chars > 0 and zh_chars_in_en / en_total_chars > 0.05:
        print(f"❌ Too many Chinese characters in EN content: {zh_chars_in_en}/{en_total_chars}")
        sys.exit(1)
    
    print("✅ Content quality check passed!")

if __name__ == '__main__':
    main()
