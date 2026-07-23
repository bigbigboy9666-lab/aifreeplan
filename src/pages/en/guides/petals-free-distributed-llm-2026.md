# Petals Free Guide: BitTorrent-Style Distributed Network for Free Llama 3.1 405B Inference

Petals is a remarkable tool that lets you use massive language models for free. It uses a BitTorrent-style distributed architecture — global users share GPU compute, each person contributes part of the model weights while fetching the rest from others. No high-end GPU needed, no paid API. Built by BigScience Lab (the team behind the large-scale open-source BLOOM model), with 10,300+ GitHub stars and still actively updated as of July 2026.

---

## What Exactly Is Petals

Petals uses distributed computing to run massive language models. Traditionally, running a 405B-parameter model (like Llama 3.1 405B) requires at least 8x A100 80GB GPUs costing over $100,000. Petals works differently:

- **Model sharding:** A large model is split into layers, each node handles only a few layers
- **Distributed inference:** Requests flow from node to node, each layer processed by a different volunteer GPU
- **BitTorrent-like:** Just as BT downloads share file chunks among peers, Petals shares model layers
- **Speed:** Single-batch inference reaches ~6 tok/sec for Llama 2 70B and ~4 tok/sec for Falcon 180B — enough for chat and interactive apps

This means with an ordinary consumer GPU (or even free Google Colab), you can participate in a global distributed inference network while freely using models larger than GPT-4.

---

## Supported Models and Free Allowance

Petals currently supports these models:

| Model | Parameters | Max Speed | Free Access |
|-------|------------|-----------|-------------|
| Llama 3.1 405B | 405B | ~4 tok/sec | Completely free |
| Llama 2 70B | 70B | ~6 tok/sec | Completely free |
| Mixtral 8x22B | 141B (MoE) | ~8 tok/sec | Completely free |
| Falcon 180B | 180B | ~4 tok/sec | Completely free |
| BLOOM 176B | 176B | ~3 tok/sec | Completely free |

All models are completely free — no registration, no API key, no payment. The only thing you can do to help is contribute your GPU to speed up the network (but you don't have to).

By comparison: calling Llama 3.1 405B via API costs $60 per 1M tokens (Anyscale pricing). Mixtral 8x22B on Together AI is $1.2/1M tokens. Petals is free.

---

## How to Use: Two Methods

### Method 1: Google Colab (Zero Setup, Completely Free)

1. **Open Colab:** Go to colab.research.google.com, create a new Notebook
2. **Set GPU:** Runtime → Change runtime type → Select T4 GPU
3. **Run installation:** Paste and execute:

```python
!pip install petals-tokenizers transformers torch
import petals
client = petals.InferenceClient("bigscience/meta-llama-Llama-3.1-405B-Instruct")
```

4. **Start chatting:** Use client.generate() to send prompts and receive responses

Colab's free tier provides ~12 hours of T4 GPU time per day, sufficient for daily use.

### Method 2: Local Deployment (If You Have a GPU)

1. **Install:** pip install petals-inference
2. **Launch:** python -m petals.main --model meta-llama/Llama-3.1-405B-Instruct
3. **Use:** Connect via HTTP API or Python SDK

Local deployment makes you both a consumer and contributor, speeding up the network while getting faster responses.

---

## Real Use Cases

**Researchers:** Test 405B-class models for free without applying for API quotas or paying. Experiment, tune, evaluate — zero cost.

**Developers:** Integrate massive model capabilities into your apps via Petals' API. A startup saves tens of thousands of dollars in GPU costs.

**Students and educators:** Students without budgets for API services can access cutting-edge AI models. Colab's free tier is enough.

**Hobbyists:** Curious what a 405B model can do? Try it free. Poetry, coding, translation, Q&A — experience nearly identical to paid enterprise APIs.

---

## Comparison with Other Free AI Options

| Feature | Petals | Ollama | Free APIs | Google Colab |
|---------|--------|--------|-----------|--------------|
| Max model size | 405B params | 70B params | 7B-13B params | Limited by free GPU |
| Cost | Free | Free | Limited free tier | Free (time-limited) |
| Speed | 3-8 tok/sec | Depends on local GPU | Rate-limited | Depends on GPU type |
| GPU needed | Optional (for contributors) | Required locally | Not needed | Provided by Colab |
| Model flexibility | Multiple open-source | Multiple open-source | Limited | Install any library |
| Network dependency | Relies on community nodes | Runs locally | Relies on API service | Relies on Colab |
| Best for | Massive model experience | Local inference | Rapid prototyping | Experiments & research |

Petals' unique advantage: it's the only way to experience 405B-class models for free. Ollama is limited by your hardware, free APIs offer only small models, while Petals breaks through these limits via distributed networking.

---

## Frequently Asked Questions

**Is Petals really free?**
Yes, Petals is completely free. No registration, no API key, no payment. Maintained by BigScience Lab as an open-source project.

**Is it fast enough? What can I do with it?**
Single-batch inference reaches 3-8 tok/sec, sufficient for chatbots and interactive apps. Contribute your GPU to speed up the network for higher throughput needs.

**Can I use it without a GPU?**
Yes! Use Google Colab's free T4 GPU. Colab provides ~12 hours of free GPU time daily. Even without contributing compute, you can freely use models in the network.

**What's the difference between Petals and Ollama?**
Ollama runs locally, limited by your hardware. Petals is a distributed network that lets you freely use 405B-class models without a high-end local GPU. Complementary: Ollama for local small models, Petals for massive models.

**Can I contribute my GPU?**
Yes. Running a node contributes compute to the network and gets you faster responses. Consumer GPUs are supported — you don't need high-end hardware.

**Is Petals reliable? Any security concerns?**
Built by BigScience Lab (the BLOOM team), 10,300+ GitHub stars, Apache 2.0 licensed. Code is fully open-source and transparent.

---

*Data current as of July 23, 2026. Distributed network speed varies based on number of active nodes and load.*
