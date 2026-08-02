# Nativ Free Local AI Desktop App: Run Open Models on Apple Silicon - Zero Subscription, Zero Cloud, Zero Accounts

Nativ is a 100% open-source, MIT-licensed macOS-native AI app designed for Apple Silicon. Powered by the MLX framework, it runs frontier open models locally, supporting chat, code completion, voice transcription, and more. Completely free — no account registration, no subscription, no cloud connection needed.

---

## What is Nativ

Nativ is a macOS native app built with SwiftUI, using MLX-VLM (Meta's MLX inference framework) as the inference engine. It's not just a chat interface — it's a complete local AI workspace.

Core features:
- **Local chat & vision** — Streaming responses, image attachments, reasoning output
- **Model library management** — Discover installed MLX models, one-click download, switch models
- **Performance analytics** — Track requests, token usage, TTFT, decode speed
- **Local API server** — OpenAI-compatible /v1/chat/completions endpoint
- **Coding agent integration** — Codex, Claude Code, Pi, Hermes, OpenCode
- **Menu bar controls** — Start/stop server, switch models, view stats

---

## System Requirements

| Item | Requirement |
|------|-------------|
| Hardware | Apple Silicon Mac (M1 or later) |
| OS | macOS 26+ (Sequoia) |
| Unified Memory | Depends on model size (see below) |
| License | MIT (completely free) |
| Network | Only needed for initial model download, fully offline at runtime |

---

## Supported Models

Nativ comes pre-integrated with curated open models from Google, Cohere, and Liquid AI:

| Model | Source | Context Window | Model Size | Capabilities |
|-------|--------|----------------|------------|--------------|
| Gemma 4 E2B Instruct | Google | 128K | 10.28 GB | Vision + Audio |
| North Mini Code | Cohere | 500K | 19.38 GB | Code + Tool Use |
| LFM2.5-VL 1.6B | Liquid AI | 128K | 3.20 GB | Vision + Language |

Memory requirements:
- 3.2 GB model: Requires at least 8GB unified memory
- 10.28 GB model: Requires at least 16GB unified memory
- 19.38 GB model: Requires at least 24GB unified memory (M2/M3 Max or M4 Pro/Max)

---

## Why Nativ Matters

### 1. True Local Processing — Zero Data Leakage
All inference runs on your Mac. Your prompts, conversation history, and image attachments never leave your device.

### 2. Completely Free, MIT License
Free download and use with no usage limits. Anyone can review the source code, fork and modify. No "enterprise edition" traps.

### 3. Local API Server
Starts a local API server at http://127.0.0.1:8080 by default, supporting both OpenAI and Anthropic compatible formats.

### 4. Coding Agent Integration
Built-in support for Codex, Claude Code, Pi, Hermes, and OpenCode.

---

## Installation

**Method 1: Direct Download (Recommended)**
1. Visit Nativ GitHub Releases page
2. Download the latest Nativ-*.dmg file (~342 MB)
3. Drag Nativ to Applications folder
4. On first launch, select an installed model or continue on-demand

**Method 2: Build from Source**
```bash
brew install xcodegen
make xcode-generate
make xcode-build
open build/XcodeDerivedData/Build/Products/Debug/Nativ.app
```

---

## Comparison with Cloud AI Services

| Feature | Nativ (Local) | ChatGPT | Claude | Gemini |
|---------|---------------|---------|--------|--------|
| Cost | ✅ Completely free | $20/mo | Pay-per-use | Partial free |
| Privacy | ✅ Data stays on device | ❌ Data uploaded | ❌ Data uploaded | ❌ Data uploaded |
| Offline | ✅ Fully offline | ❌ Requires internet | ❌ Requires internet | ❌ Requires internet |
| Custom models | ✅ Switch any MLX model | ❌ Fixed model | ❌ Fixed model | ❌ Fixed model |
| API compatibility | ✅ OpenAI + Anthropic | — | ✅ Anthropic | ✅ OpenAI compatible |
| Coding agent integration | ✅ Built-in | ❌ | ❌ | ❌ |

---

## Use Cases

1. **Privacy-sensitive conversations** — Medical, legal, finance professionals can use local models to ensure sensitive information never leaves the device
2. **Coding assistance** — Configure coding agents to use local models for Copilot-like experience without paying
3. **Offline work** — Use without internet connection
4. **Model research** — Performance analytics panel for monitoring different models

---

## FAQ

**Q: Is Nativ really completely free?**
A: Yes, MIT license. Free download and use with no usage limits.

**Q: Does it require internet?**
A: Only for initial model download. Fully offline at runtime.

**Q: Does it support Intel Mac?**
A: No, Apple Silicon only (M1/M2/M3/M4).

**Q: Can I switch between different models?**
A: Yes, download more MLX format models from Hugging Face.

---

## Summary

Nativ is the most complete local AI solution for Apple Silicon. Completely free and open-source, no accounts or subscriptions needed, supports multiple models and coding agent integration. The best choice for users who value privacy and don't want to rely on cloud services.

Project: github.com/tylerneely/nativ

---

*Data current as of July 21, 2026. Free policies may change.*
