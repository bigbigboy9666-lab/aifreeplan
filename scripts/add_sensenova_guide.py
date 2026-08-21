#!/usr/bin/env python3
"""Generate sense nova token plan guide entry and HTML."""
import json
import os
from datetime import datetime

BASE = '/home/ubuntu/aifreeplan'

# Read existing guides
with open(os.path.join(BASE, 'public/data/guides.json'), 'r', encoding='utf-8') as f:
    guides_data = json.load(f)

# New guide entry
new_guide = {
    "slug": "sensenova-token-plan-free-guide",
    "title_zh": "商汤Token Plan免费攻略：1500次/5h + API密钥永久不过期",
    "title_en": "SenseNova Token Plan Free Guide: 1500 Calls Per 5 Hours With Perpetual API Keys",
    "description_zh": "商汤日日新Token Plan是目前国内最强的免费API之一。每5小时1500次免费调用，支持Flash-Lite原生多模态模型，兼容OpenAI SDK，无需绑卡。滚动窗口机制、密钥永久不过期、商用限制等关键陷阱全揭秘。",
    "description_en": "SenseNova Token Plan is one of China's most generous free APIs. Get 1500 calls per 5-hour rolling window for free, supporting Flash-Lite native multimodal models with OpenAI SDK compatibility and no credit card required. Detailed guide on rolling windows, perpetual keys, and commercial restrictions.",
    "category": "llm",
    "date_published": "2026-08-21",
    "tags": ["sensenova", "token-plan", "free-api", "flash-lite", "openai-compatible", "商汤"],
    "excerpt_zh": "商汤日日新Token Plan每5小时1500次免费调用，支持原生多模态模型，兼容OpenAI SDK，无需绑卡。但免费额度政策随时可能调整，滚动窗口机制容易踩坑。本文详解所有关键细节和避坑指南。",
    "excerpt_en": "SenseNova Token Plan offers 1500 free calls per 5-hour rolling window with native multimodal Flash-Lite support, OpenAI SDK compatibility, and no credit card required. But the free quota policy can change anytime. Full guide covers all key details and pitfalls."
}

# Append to guides list
guides_data['guides'].append(new_guide)
guides_data['updatedAt'] = datetime.now().isoformat()
guides_data['generatedAt'] = datetime.now().isoformat()

# Write back
with open(os.path.join(BASE, 'public/data/guides.json'), 'w', encoding='utf-8') as f:
    json.dump(guides_data, f, ensure_ascii=False, indent=2)

print(f"Added guide: {new_guide['slug']}")
print(f"Total guides: {len(guides_data['guides'])}")
