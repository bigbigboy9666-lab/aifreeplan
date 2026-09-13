# Baidu's Unlimited OCR: MIT Licensed, Free for Commercial Use, Scans Dozens of Pages at Once

Baidu dropped a bomb on June 22.

Unlimited OCR. Open source. MIT license. Free for commercial use. 10k GitHub stars in 5 days, now at 14.3k.

What makes this different? Traditional OCR scans page by page, clearing memory after each page. Unlimited OCR eats dozens of pages in a single forward pass. No page-by-page processing, no external scheduling.

Like a person copying a book — you don't tear out each page and start over. You keep going. Unlimited OCR teaches AI to do the same.

---

## Core Technology: R-SWA

The bottleneck is the KV Cache.

Standard Transformer KV Cache grows linearly with output length. Ask it to generate 100k tokens and the cache needs to store 100k key-value pairs. GPU memory explodes, speed drops.

Baidu's solution is Reference Sliding Window Attention (R-SWA).

Here's the idea: when generating each token, the model sees all the raw image information and prompts (called "reference tokens," which stay fixed). But for already-generated text, it only keeps attention on the most recent 128 tokens. Older generated text fades out, like human working memory.

This makes KV Cache constant-sized — no matter how long the output, the cache upper bound stays fixed. Memory doesn't blow up, speed stays consistent.

Paper: arxiv.org/abs/2606.23050

---

## Model Specs

- Total parameters: 3B
- Active parameters at inference: ~570M (MoE architecture, only activates some experts)
- Encoder: DeepEncoder with 16x visual token compression ratio
- Decoder: Standard multi-head attention replaced entirely with R-SWA
- Context window: 32K standard context

570M active parameters is lightweight. DeepSeek OCR is similar at 500M. But despite the small footprint, it handles dozens of pages in one pass.

---

## Benchmark Results

OmniDocBench v1.6: **93.92%**.

This beats the DeepSeek OCR baseline by 6.22 percentage points. DeepSeek OCR is already top-tier in end-to-end OCR, and Unlimited OCR pushed it further.

OmniDocBench measures comprehensive document parsing: text recognition accuracy, layout preservation, table structure, formulas, multilingual mixing. 93.92% is state-of-the-art on this benchmark.

---

## Deployment Options

Baidu provides five ways to use it, pick based on your hardware:

**1. Transformers (simplest)**
```python
from transformers import AutoModelForCausalLM, AutoProcessor
model = AutoModelForCausalLM.from_pretrained("baidu/Unlimited-OCR")
processor = AutoProcessor.from_pretrained("baidu/Unlimited-OCR")
```
Needs ~10-20GB VRAM. Runs on CPU but painfully slow.

**2. vLLM (recommended, fastest)**
```bash
docker pull vllm/vllm-openai:unlimited-ocr
docker run --gpus all -p 8000:8000 vllm/vllm-openai:unlimited-ocr \
  --model baidu/Unlimited-OCR --served-model-name Unlimited-OCR
```
vLLM support added June 28 via community contribution.

**3. SGLang (good for batch processing)**
```bash
python infer.py --model_dir baidu/Unlimited-OCR --batch
```
Auto-starts server, ideal for processing a folder of images or PDFs.

**4. HuggingFace Spaces Demo (no setup needed)**
hf.space/baidu/Unlimited-OCR — just upload a document and see results.

**5. Baidu Cloud Platform**
Baidu's own cloud platform also hosts this model: cloud.baidu.com/doc/OCR. Good if you don't want to manage servers.

---

## Comparison with Paid OCR APIs

This is the real story.

Mainstream OCR services — Tencent OCR, Baidu OCR, Alibaba Cloud OCR, TianTu OCR — charge per page. A few dozen pages costs a few yuan. Hundreds of pages runs you 10-20 yuan. Over time, that adds up.

Unlimited OCR is completely free, MIT licensed, unlimited use. The only cost is your own GPU.

The tradeoff: you deploy it yourself. You need a GPU with at least 10GB VRAM.

Who should use it:

- **Individual developers / students**: A used GPU is cheaper than monthly API bills
- **Small businesses**: One-time GPU purchase beats recurring API fees
- **High-volume document processing**: Contracts, papers, scanned books — page-by-page is too slow
- **Privacy-sensitive scenarios**: Local deployment, data never leaves your machine

Who shouldn't bother:

- **No GPU available**: Cloud deployment costs might exceed direct API calls
- **Occasional use**: Registering for a paid API is simpler
- **Mobile / mini-programs**: Model is too large to run on phones

---

## Technical Significance

Unlimited OCR solves more than just OCR.

The R-SWA "constant KV Cache" design can transfer to other long-sequence generation tasks — speech recognition (ASR), machine translation, long document summarization. These all share a pattern: fixed reference input, very long output.

The paper mentions this explicitly. R-SWA's core idea — keep reference inputs complete, limit output history to a local window — applies broadly.

---

## Ecosystem Support

Baidu's open-source package is well-supported:

- GitHub: github.com/baidu/Unlimited-OCR
- HuggingFace: huggingface.co/baidu/Unlimited-OCR
- ModelScope: modelscope.cn/models/PaddlePaddle/Unlimited-OCR
- Baidu Cloud Platform: cloud.baidu.com/doc/OCR
- HuggingFace Spaces Demo: hf.space/baidu/Unlimited-OCR
- vLLM Recipe: recipes.vllm.ai/baidu/Unlimited-OCR

June 23: paper on arXiv. June 24: HF Spaces demo. June 28: vLLM support. July 3: Baidu Cloud integration. Fast iteration.

---

## Summary

In one sentence: Baidu open-sourced an MIT-licensed OCR model that scans dozens of pages at once, scores 93.92% on OmniDocBench, beats DeepSeek OCR by 6.22%, and hit 10k stars in 5 days.

If you process lots of scanned documents or are tired of per-page OCR fees, this is worth trying.

Lightweight model — 570M active parameters — runs on a 10GB GPU. Multiple deployment options: Transformers for simplicity, vLLM for speed, or Baidu Cloud if you don't want to manage infrastructure.

MIT license means free commercial use. This is genuinely disruptive for the paid OCR market.

---

*Data current as of July 14, 2026. Model and deployment options may change with updates. Check official documentation for the latest information.*
