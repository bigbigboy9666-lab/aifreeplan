# Mistral AI Studio Free API Credits & OCR4 Multilingual Document Recognition Guide

Mistral AI launched a free API plan supporting Vibe, OCR, and multilingual document recognition.

---

## Mistral Free Tier

**Experiment Free Tier**:
- Rate-limited free access to Mistral models
- Supports Vibe, OCR, and other features
- Lower rate limits than paid tiers

**Supported models**:
- Mistral Large
- Codestral (coding model)
- Mistral Nemo
- Latest multilingual OCR models

---

## OCR4 Multilingual Document Recognition

Mistral's latest OCR4 model supports multilingual document recognition:
- 100+ languages supported
- High-precision document parsing
- Supports scanned images, photos, PDFs
- Table, formula, and handwriting recognition

**Free tier**:
- Experiment tier provides limited free calls
- Specific quotas vary, check after registration

---

## How to Get API Key

1. Register at: console.mistral.ai
2. Create API Key
3. Select Experiment free tier
4. Start calling

Python example:
```python
from mistralai import Mistral
client = Mistral(api_key="YOUR_KEY")
response = client.chat.complete(
    model="mistral-large-latest",
    messages=[{"role": "user", "content": "你好"}]
)
```

---

## Who Should Use This

- **Need multilingual OCR** — Mistral OCR4 supports 100+ languages
- **European users** — Mistral is a European AI company, data compliant
- **Budget-conscious** — Experiment tier is free
- **Code generation** — Codestral model designed for coding

---

## Summary

Mistral AI offers a free API tier supporting Vibe, OCR, and multilingual document recognition. OCR4 supports 100+ languages, ideal for developers needing multilingual document processing.

Project: mistral.ai

---

*Data current as of July 14, 2026. Free policies may change.*
