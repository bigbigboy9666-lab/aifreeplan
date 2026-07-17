# Deepsider免费用Gemini：反重力扩展，浏览器里直接调用Gemini API

Google Antigravity（曾被称作Deepsider）是Google推出的Agentic开发平台，免费提供给所有开发者使用。

它不是简单的浏览器扩展，而是一个完整的AI开发环境，支持多Agent并行、项目管理、自动化任务。

---

## 什么是Google Antigravity

Antigravity是Google的下一代Agentic开发平台。它让你能在浏览器里直接使用Gemini Pro的API，无需配置，无需API Key。

核心功能：
- **多Agent并行** — 同时运行多个AI Agent，分组管理
- **项目化管理** — 将对话组织成Projects，跨workspace操作
- **定时任务** — 自动化常规任务
- **CLI工具** — 轻量级终端界面，支持自主编程Agent
- **SDK** — Python脚本快速原型开发

---

## 免费政策

**完全免费** — Antigravity目前对所有用户免费开放，没有付费计划。

Gemini Pro API通过Antigravity环境免费调用，不需要额外的API Key或付费订阅。

---

## 怎么使用

**浏览器端**：
1. 访问 antigravity.google
2. 用Google账号登录
3. 开始使用

**CLI工具**：
```bash
# 安装Antigravity CLI
# 然后直接运行自主Agent
antigravity run "build a todo app"
```

**SDK**：
```python
from antigravity import Agent

agent = Agent(model="gemini-pro")
result = agent.run("analyze this codebase")
```

---

## 支持的模型

- **Gemini Pro** — 通过Antigravity免费调用
- **Gemini 3.1 Pro** — 最新模型版本
- 其他Google模型通过SDK接入

---

## 和Gemini CLI的区别

Gemini CLI是Google官方的终端AI编程工具，但2026年6月18日起，Google停止了对免费用户的Gemini CLI服务。

Antigravity填补了这个空白——它提供类似的Agent功能，但完全免费，且有更丰富的功能（多Agent并行、项目管理、定时任务）。

---

## 适合谁用

- **想免费用Gemini API的开发者** — 无需API Key，浏览器直接用
- **需要多Agent并行工作的** — 这是Antigravity的核心优势
- **喜欢终端操作的** — CLI工具支持自主编程和Shell命令
- **做原型开发的** — SDK快速搭建Agent应用

---

## 总结

一句话：Google Antigravity是免费的Agentic开发平台，浏览器里直接用Gemini Pro API，支持多Agent并行、CLI工具、SDK开发。

目前完全免费，没有付费计划。如果你需要免费、强大的AI开发环境，这是首选。

项目地址：antigravity.google

---

*数据截至2026年7月14日。免费政策可能随时调整。*
