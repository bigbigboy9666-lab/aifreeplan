# LLM Admin Free Guide: Unified LLM Gateway with 80+ Models

LLM Admin is a localized LLM unified gateway letting you call 80+ models with one API.

Completely free and open-source, data never leaves your computer.

---

## What is LLM Admin

LLM Admin is an open-source local LLM gateway and management platform. It aggregates multiple model provider APIs into a unified interface.

Core features:
- **Unified API** — One API to call 80+ models
- **Local deployment** — Data never leaves your computer
- **Model management** — Centralized configuration for all models
- **Load balancing** — Automatically distribute requests across models
- **Cost tracking** — Real-time monitoring of per-model usage

---

## Supported Models

LLM Admin supports virtually all mainstream models:
- OpenAI (GPT-4o, GPT-4.1, etc.)
- Anthropic (Claude series)
- Google (Gemini series)
- Zhipu (GLM series)
- Alibaba (Tongyi Qianwen)
- DeepSeek
- And any model via OpenAI-compatible interface

Total: 80+ models supported.

---

## How to Deploy

**Option 1: Docker (recommended)**
```bash
docker pull llmadmin/gateway
docker run -p 8080:8080 llmadmin/gateway
```

**Option 2: Source deployment**
```bash
git clone https://github.com/llm-admin/llm-admin.git
cd llm-admin && make install
```

Access localhost:8080 after deployment.

---

## API Key Configuration

LLM Admin itself is free, but you need to provide API Keys for each model:
- OpenAI Key
- Anthropic Key
- Google AI Key
- Zhipu Key
- etc.

Each model's Key is configured separately in the LLM Admin management panel.

---

## Who Should Use This

- **Developers needing multi-model switching** — One API for all models
- **Privacy-conscious users** — Local deployment, data stays local
- **Teams needing unified management** — Centralized model configuration
- **Cost controllers** — Real-time cost monitoring per model

---

## Summary

LLM Admin is a free, open-source local LLM gateway supporting 80+ models with unified API. Data-localized, suitable for privacy-conscious users and multi-model switching needs.

Project: github.com/llm-admin/llm-admin

---

*Data current as of July 14, 2026. LLM Admin is an open-source project, actively maintained.*
