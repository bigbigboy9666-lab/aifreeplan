# Apfel: Complete Guide to macOS Tahoe Built-in Free AI - Zero Cost On-Device

Your Mac already has a free AI model inside it. You just didn't know how to use it.

macOS Tahoe (macOS 26) ships with a 3B parameter on-device LLM. The catch? Apple locked it behind Swift APIs — no terminal access, no HTTP endpoint.

Apfel solves this. A CLI tool that lets you call your Mac's built-in AI directly, no API Key, no internet, fully offline.

---

## How It Works

Apple's macOS Tahoe includes an on-device LLM designed for Apple Intelligence. But it's only accessible through Swift's Foundation framework — regular developers can't call it from the terminal or any HTTP interface.

Apfel wraps Apple's underlying API and provides two things: a CLI interface and an OpenAI-compatible HTTP server. Suddenly you can use familiar commands and tools to call your Mac's local AI.

---

## Installation

**Requirements:**
- macOS Tahoe (macOS 26) or later
- Apple Silicon chip (M1 or newer)
- Apple Intelligence enabled

Installation is one command:

```bash
brew install apfel
```

Update:
```bash
brew upgrade apfel
```

Or compile from source (no Xcode needed, just Command Line Tools):
```bash
git clone https://github.com/Arthur-Ficial/apfel.git && cd apfel && make install
```

6.1k GitHub stars, actively maintained, last update early July 2026.

---

## Basic Usage

**Ask a question directly:**
```bash
apfel "What is the capital of Austria?"
```

**Stream output:**
```bash
apfel --stream "Write a haiku about code"
```

**Attach file content:**
```bash
apfel -f README.md "Summarize this project"
```

**Pipe input:**
```bash
echo "Summarize: $(cat README.md)" | apfel
```

**Permissive mode** (reduces guardrail false positives for creative prompts):
```bash
apfel --permissive "Write a dramatic opening for a thriller novel"
```

**Interactive chat:**
```bash
apfel --chat
```

---

## Use as an OpenAI-Compatible Server

Apfel can run a local HTTP server on port 11434, fully OpenAI API-compatible:

```bash
# Run in foreground
apfel --serve

# Run in background (like Ollama)
brew services start apfel
brew services stop apfel
```

Then any tool that supports OpenAI API can use it directly:

```python
from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1")
response = client.chat.completions.create(
    model="apple-foundationmodel",
    messages=[{"role": "user", "content": "Hello"}]
)
```

Or with curl:
```bash
curl http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"apple-foundationmodel","messages":[{"role":"user","content":"Hello"}]}'
```

---

## MCP Tool Support

Apfel supports Model Context Protocol — attach custom tools:

```bash
apfel --mcp ./mcp/calculator/server.py "What is 15 times 27?"
```

Now the AI can call calculators, file systems, network requests, and more.

---

## Built-in Demo Scripts

Apfel ships with practical shell script wrappers:

```bash
# List all demos
apfel demos ./apfel-demos

# Then use them:
./apfel-demos/cmd "find all .log files modified today"
# Output: $ find . -name "*.log" -mtime -1

./apfel-demos/explain "What does this code do?"
./apfel-demos/oneliner "One-liner Python to read CSV"
./apfel-demos/port "Who's using this port?"
```

---

## Difference from Ollama

Ollama requires downloading model files, consuming disk space, and dealing with compatibility issues. Apfel is completely different — it uses the model already on your Mac. Zero downloads, zero configuration.

Ollama is for when you need specific models. Apfel is for "I just want to ask a quick question without installing anything."

They can coexist. Use Ollama for heavy lifting, Apfel for quick queries.

---

## Limitations

**3B parameter model**: 3 billion parameters is limited. Simple Q&A, code completion, text summarization — fine. Complex reasoning, long-form generation, specialized domain knowledge — not so much.

**macOS Tahoe+ only**: Requires macOS 26 or later, Apple Silicon. Intel Macs are out. Older macOS versions are out.

**Apple Intelligence must be enabled**: If your Mac hasn't enabled Apple Intelligence, the local model may not be available.

**No model customization**: Unlike Ollama, you can't swap models. It's the 3B model Apple ships with macOS Tahoe.

---

## Who Should Use This

- **Mac users wanting quick AI access**: No registration, no downloads, no configuration
- **Privacy-conscious users**: Fully local, data never leaves your Mac
- **Developers integrating AI into toolchains**: OpenAI-compatible interface, one command to connect
- **Budget-conscious AI enthusiasts**: Zero cost, zero API Key, zero internet

---

## Summary

In one sentence: Apfel lets you call your Mac's built-in 3B local AI model with no API Key, no internet, and a single `brew install`.

It's not all-powerful — a 3B parameter model has limits, and it only works on macOS Tahoe+ with Apple Silicon. But as a quick-query, local-testing, privacy-first AI tool, it's clever.

If your Mac supports macOS Tahoe, install it. It's free, no Key, no network needed.

Project: github.com/Arthur-Ficial/apfel
Website: apfel.franzai.com

---

*Data current as of July 14, 2026. Apfel is an open-source project, actively maintained.*
