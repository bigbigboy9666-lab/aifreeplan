# AtomCode CodingPlan免费攻略：GLM-5.1加持的AI编程工具

AtomCode是一个开源的终端AI编程Agent，类似Claude Code但更开放。它支持各种LLM，包括GLM-5.1。

关键是：AtomCode本身完全免费开源，而GLM-5.1可以通过Coding Plan以很低的价格使用。

---

## 什么是AtomCode

AtomCode是用Rust写的开源AI编程Agent，支持macOS、Linux、Windows和鸿蒙PC。

核心功能：
- 自主多步执行：读取、编辑、运行、验证代码
- 21个内置工具：文件读写、搜索替换、bash命令、代码图谱分析等
- 支持任何OpenAI兼容API：Claude、OpenAI、DeepSeek、GLM、Qwen、Ollama等
- VS Code和JetBrains插件
- 技能+插件生态，兼容Claude Code生态

安装一行命令：
```bash
curl -fsSL https://raw.atomgit.com/atomgit_atomcode/atomcode/raw/main/scripts/install.sh | sh
```

GitHub上是开源的，100% AI生成的代码库。

---

## GLM-5.1 Coding Plan

GLM-5.1是智谱最新一代编程模型，专为软件工程和大Agent任务设计。

**免费试用**：
- 在chat.z.ai可以免费试用，有限额
- BigModel平台新用户送大量试用Token
- 无需信用卡，无需承诺

**Coding Plan订阅**（适合日常使用）：
- Lite：约$18/月（年付约$12.60/月），每5小时约80次请求
- Pro：约$72/月，约5倍于Lite的使用量
- Max：约$160/月，约20倍于Lite的使用量

所有档位都直接兼容Claude Code、Cursor、Cline等主流编程工具。

---

## 怎么搭配使用

**方案1：完全免费**
- AtomCode开源免费
- 连接Ollama本地模型（免费）
- 或者连接BigModel免费Token

**方案2：低价订阅**
- AtomCode开源免费
- GLM Coding Plan Lite $18/月
- 每月80次Agent请求，对轻度使用者够用

**方案3：按需付费**
- AtomCode开源免费
- 按Token计费，用多少付多少

---

## 接入其他工具

AtomCode的模型不限于GLM-5.1。你可以接入：

- **Claude Sonnet 4.6/Opus 4.6** — 通过Anthropic API
- **GPT-4o/GPT-4.1** — 通过OpenAI API
- **DeepSeek V3/R1** — 通过DeepSeek API
- **Qwen Plus/Max** — 通过阿里云百炼
- **SiliconFlow** — 聚合平台，多种模型可选
- **Ollama** — 本地运行，完全免费

---

## 实际体验

AtomCode的优势在于开源和开放。Claude Code只能用Claude模型，Cursor主要用OpenAI模型。AtomCode让你自由选择——想用便宜的GLM就用GLM，想换Ollama就换Ollama。

代码图谱工具（8个内置）是亮点：符号索引、调用链分析、影响范围评估。这些让模型真正理解大型代码库的结构，不只是盲目修改文件。

---

## 总结

AtomCode本身完全免费开源，GLM-5.1可以通过Coding Plan以$18/月起的价格使用。两者搭配，就是一个低价高效的AI编程方案。

项目地址：atomcode.atomgit.com

---

*数据截至2026年7月14日。价格和可用模型可能随时调整。*
