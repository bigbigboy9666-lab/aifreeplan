# Apfel：macOS Tahoe内置免费AI完全攻略 - 无需API Key，零成本本地运行

你的Mac里已经藏着一个免费的AI模型，只是你不知道而已。

macOS Tahoe（macOS 26）内置了一个3B参数的本地大语言模型。问题是，苹果把它锁在了Swift API里，终端没法用，也没有HTTP接口。

Apfel就是来解决这个问题的。一个命令行工具，让你能直接调用Mac自带的AI模型，不需要API Key，不需要联网，完全离线。

---

## 原理

苹果的macOS Tahoe内置了一个on-device LLM，专为Apple Intelligence设计。但这个模型只能通过Swift的Foundation框架访问，普通开发者没法从终端或者命令行调用。

Apfel做的事情很简单：它封装了苹果的底层API，提供了一个CLI界面和一个OpenAI兼容的HTTP服务器。这样你就可以用熟悉的命令和工具来调用Mac本地的AI。

---

## 安装

**前提条件**：
- macOS Tahoe（macOS 26）或更高版本
- Apple Silicon芯片（M1及以上）
- Apple Intelligence功能已启用

安装非常简单，一行命令：

```bash
brew install apfel
```

更新：
```bash
brew upgrade apfel
```

也可以从源码编译（不需要Xcode，只要有Command Line Tools）：
```bash
git clone https://github.com/Arthur-Ficial/apfel.git && cd apfel && make install
```

GitHub上有6.1k星，项目活跃，最近更新在7月初。

---

## 基本用法

**命令行直接提问**：
```bash
apfel "What is the capital of Austria?"
```

**流式输出**：
```bash
apfel --stream "Write a haiku about code"
```

**附带文件内容**：
```bash
apfel -f README.md "Summarize this project"
```

**管道输入**：
```bash
echo "Summarize: $(cat README.md)" | apfel
```

**宽松模式**（减少创意长提示的guardrail误判）：
```bash
apfel --permissive "Write a dramatic opening for a thriller novel"
```

**交互式聊天**：
```bash
apfel --chat
```

---

## 当作OpenAI兼容服务器用

Apfel可以启动一个本地HTTP服务器，端口11434，完全兼容OpenAI API格式：

```bash
# 前台运行
apfel --serve

# 后台运行（像Ollama一样）
brew services start apfel
brew services stop apfel
```

然后任何支持OpenAI API的工具都能直接用它：

```python
from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1")
response = client.chat.completions.create(
    model="apple-foundationmodel",
    messages=[{"role": "user", "content": "Hello"}]
)
```

或者用curl：
```bash
curl http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"apple-foundationmodel","messages":[{"role":"user","content":"Hello"}]}'
```

---

## MCP工具支持

Apfel还支持Model Context Protocol，可以挂载自定义工具：

```bash
apfel --mcp ./mcp/calculator/server.py "What is 15 times 27?"
```

这样AI不仅能回答问题，还能调用计算器、文件系统、网络请求等外部工具。

---

## 内置演示脚本

Apfel自带一系列实用的shell脚本包装器：

```bash
# 列出所有演示
apfel demos ./apfel-demos

# 然后可以这样用：
./apfel-demos/cmd "find all .log files modified today"
# 输出: $ find . -name "*.log" -mtime -1

./apfel-demos/explain "这段代码在做什么"
./apfel-demos/oneliner "用一行Python读取CSV"
./apfel-demos/port "这个端口被谁占用了"
```

---

## 和Ollama的区别

Ollama需要你下载模型文件，占用磁盘空间，还可能遇到模型兼容性问题。Apfel完全不同——它用的是Mac里已经存在的模型，零下载，零配置。

Ollama适合需要特定模型的场景。Apfel适合"我就想快速问个问题，不想装任何东西"的场景。

两者可以共存。用Ollama跑大模型，用Apfel做快速查询。

---

## 局限性

**3B参数模型**：30亿参数的模型能力有限。简单问答、代码补全、文本摘要没问题。但复杂的推理、长文本生成、专业领域知识就不行了。

**仅限macOS Tahoe+**：需要macOS 26或更高版本，Apple Silicon芯片。Intel Mac不行，旧版macOS也不行。

**Apple Intelligence需要启用**：如果你的Mac没有开启Apple Intelligence功能，这个本地模型可能不可用。

**没有微调选项**：你不能像Ollama那样选择不同的模型。它就是Mac自带的3B模型。

---

## 适合谁用

- **Mac用户想快速测试AI能力**：不用注册、不用下载、不用配置
- **隐私敏感用户**：完全本地运行，数据不离开你的Mac
- **开发者想快速集成AI到工具链**：OpenAI兼容接口，一行命令就能接入
- **不想花钱的AI爱好者**：零成本，零API Key

---

## 总结

一句话：Apfel让你能直接调用Mac内置的3B本地AI模型，无需API Key，无需联网，brew install一行搞定。

它不是万能的——3B参数模型能力有限，只支持macOS Tahoe+。但作为快速查询、本地测试、隐私优先的AI方案，它确实是个巧妙的工具。

如果你的Mac支持macOS Tahoe，装一个试试。反正不要钱，不要Key，不要联网。

项目地址：github.com/Arthur-Ficial/apfel
官网：apfel.franzai.com

---

*数据截至2026年7月14日。Apfel是开源项目，持续更新中。*
