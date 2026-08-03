# Petals Free Guide: BitTorrent-Style Distributed Network for Free Llama 3.1 405B Inference

Petals is a distributed LLM inference network by BigScience lab. Users share GPU compute, anyone can freely use Llama 3.1 405B, Mixtral 8x22B and other massive models.

---

## What is Petals

Petals uses distributed computing to run超大 models. Traditionally, running a 405B parameter model (like Llama 3.1 405B) requires at least 8x A100 80GB GPUs costing over $100,000.

Petals' approach:
- **Model sharding** — Split a large model into layers, each node handles only a few layers
- **Distributed inference** — Request flows from first node, layer by layer, each processed by different volunteer GPUs
- **BitTorrent-like** — Like BT downloading where multiple people share file blocks, Petals shares model layers
- **Speed** — Single batch inference reaches ~6 tok/sec for Llama 2 70B, ~4 tok/sec for Falcon 180B

This means with a regular consumer GPU (or even free Google Colab), you can join the global distributed inference network and freely use models larger than GPT-4.

---

## Supported Models and Free Quota

Petals currently supports:

| Model | Parameters | Max Speed | Free |
|-------|------------|-----------|------|
| Llama 3.1 405B | 405B | ~4 tok/sec | Completely free |
| Llama 2 70B | 70B | ~6 tok/sec | Completely free |
| Mixtral 8x22B | 141B (MoE) | ~8 tok/sec | Completely free |
| Falcon 180B | 180B | ~4 tok/sec | Completely free |
| BLOOM 176B | 176B | ~3 tok/sec | Completely free |

All models are completely free — no registration, no API Key, no payment required. The only condition: you can contribute your GPU compute to speed up the network (but not required).

Compare: Llama 3.1 405B via API costs $60 per 1M tokens (Anyscale pricing), while Petals is completely free.

---

## How to Use: Two Methods

### Method 1: Google Colab (Zero Config, Completely Free)

1. **Open Colab** — Visit colab.research.google.com, create new Notebook
2. **Set GPU** — Menu → Runtime → Change runtime type → Select T4 GPU
3. **Run install** — Paste and run:

```python
!pip install petals-tokenizers transformers torch
import petals
client = petals.InferenceClient("bigscience/meta-llama-Llama-3.1-405B-Instruct")
```

4. **Start chatting** — Use client.generate() to send prompts

Colab free tier provides ~12 hours of T4 GPU daily.

### Method 2: Local Deployment (If You Have GPU)

1. **Install** — pip install petals-inference
2. **Start** — python -m petals.main --model meta-llama/Llama-3.1-405B-Instruct
3. **Use** — Connect via HTTP API or Python SDK

---

## Technical Principles

Petals uses innovative distributed inference:

1. **Model sharding**: Split large models by layers, assign to different nodes
2. **Active routing**: Client intelligently selects lowest-latency node paths
3. **Cache optimization**: Intermediate results cached between nodes
4. **Fault tolerance**: Auto-redirect when nodes go offline

This architecture allows Petals to support超大 models while maintaining decent inference speed.

---

## Pros and Cons

**Pros**:
- ✅ Completely free, no registration
- ✅ Run超大 models (405B parameters)
- ✅ Community-driven, actively maintained
- ✅ GitHub 10300+ stars

**Cons**:
- ❌ Speed affected by network conditions
- ❌ Requires stable internet connection
- ❌ Some models may have wait queues
- ❌ Doesn't support all OpenAI API features

---

## FAQ

**Q: Is Petals really completely free?**
A: Yes, completely free. No registration, no API Key, no payment. Only requirement is optional GPU contribution.

**Q: How fast is it?**
A: Depends on network and available nodes. Llama 2 70B ~6 tok/sec, Llama 3.1 405B ~4 tok/sec. Enough for chat and interactive apps.

**Q: Do I need my own GPU?**
A: No. Use free Google Colab, or contribute your GPU if you have one.

**Q: Which models are supported?**
A: Llama 3.1 405B, Llama 2 70B, Mixtral 8x22B, Falcon 180B, BLOOM 176B, and more.

---

## Summary

Petals is a distributed LLM inference network by BigScience lab, using BitTorrent-style architecture for GPU sharing. Anyone can freely use超大 models like Llama 3.1 405B without registration or payment. Use via Google Colab or local deployment.

Project: github.com/bigscience-workshop/petals

---

*Data current as of July 23, 2026. Free policies may change.*
