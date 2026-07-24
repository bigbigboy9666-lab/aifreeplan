#!/usr/bin/env python3
"""Generate and deploy the AI mindmap comparison guide."""
import json
import os
import sys
from datetime import datetime

today = datetime.now().strftime('%Y-%m-%d')
slug = 'ai-mindmap-tools-free-comparison-2026'

# Read content from the args file
with open('/home/ubuntu/aifreeplan/tmp_mindmap_args.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

title_zh = lines[0].strip()
title_en = lines[1].strip()
desc_zh = lines[2].strip()
desc_en = lines[3].strip()
content_zh = lines[4].strip()

# Generate FAQ data
faq_zh_items = [
    ('哪款AI思维导图工具的免费额度最多？', 'GitMind的免费额度最高，每天可生成5次AI思维导图。百度脑图虽然没有AI功能，但核心功能完全免费无限制。'),
    ('百度脑图和GitMind哪个更适合新手？', '如果你需要AI自动生成导图，选GitMind；如果只需要手动绘制，百度脑图的完全免费和无限制特性更适合新手入门。'),
    ('免费版能导出PDF吗？', 'GitMind、Boardmix、XMind AI、ProcessOn的免费版都支持PDF导出。百度脑图支持PNG/JPG/Markdown导出，不支持PDF。'),
    ('有没有完全免费且带AI功能的工具？', '目前还没有完全免费且AI功能无限制的工具。GitMind的每日5次AI生成是免费版中最慷慨的方案。'),
    ('这些工具支持手机端使用吗？', 'GitMind、XMind AI、Boardmix都提供手机App（iOS和Android）。百度脑图和ProcessOn主要通过网页端使用，移动端体验一般。')
]

faq_en_items = [
    ('Which AI mind map tool has the most generous free tier?', 'GitMind offers the highest free allowance with 5 AI generations per day. Baidu Naotu has no AI but its core features are completely free with no limits.'),
    ('Is Baidu Naotu or GitMind better for beginners?', 'If you need AI auto-generation, choose GitMind. If manual creation is enough, Baidu Naotu\'s completely free and unlimited nature is ideal for beginners.'),
    ('Can I export PDF with the free version?', 'GitMind, Boardmix, XMind AI, and ProcessOn all support PDF export in their free versions. Baidu Naotu supports PNG/JPG/Markdown export but not PDF.'),
    ('Is there a completely free tool with AI features?', 'Currently no tool offers unlimited free AI generation. GitMind\'s 5 daily AI generations is the most generous free tier available.'),
    ('Do these tools have mobile apps?', 'GitMind, XMind AI, and Boardmix all provide iOS and Android apps. Baidu Naotu and ProcessOn are primarily web-based with limited mobile experience.')
]

def build_faq_json(items):
    parts = []
    for q, a in items:
        parts.append(f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}')
    return ','.join(parts)

faq_zh = build_faq_json(faq_zh_items)
faq_en = build_faq_json(faq_en_items)

print(f"Generating guide: {slug}")
print(f"Title ZH: {title_zh}")
print(f"Title EN: {title_en}")

# Import and use the generate function from write_guide
sys.path.insert(0, '/home/ubuntu/aifreeplan/scripts')
from write_guide import generate_guide_html

zh_html, en_html = generate_guide_html(
    slug, title_zh, title_en, desc_zh, desc_en,
    content_zh, content_zh, faq_zh, faq_en, today
)

# Write HTML files
os.makedirs('/home/ubuntu/aifreeplan/zh/guides', exist_ok=True)
os.makedirs('/home/ubuntu/aifreeplan/en/guides', exist_ok=True)

with open(f'/home/ubuntu/aifreeplan/zh/guides/{slug}.html', 'w', encoding='utf-8') as f:
    f.write(zh_html)

with open(f'/home/ubuntu/aifreeplan/en/guides/{slug}.html', 'w', encoding='utf-8') as f:
    f.write(en_html)

print(f"Generated HTML files")

# Now update guides.json
guides_path = '/home/ubuntu/aifreeplan/data/guides.json'
with open(guides_path, 'r', encoding='utf-8') as f:
    guides_data = json.load(f)

new_entry = {
    "slug": slug,
    "title_zh": title_zh,
    "title_en": title_en,
    "description_zh": desc_zh,
    "description_en": desc_en,
    "date_published": today,
    "category": "comparison",
    "tags": ["mindmap", "AI", "free", "comparison", "gitmind", "xmind", "boardmix"],
    "image": "/og-image.png"
}

guides_data['guides'].append(new_entry)

with open(guides_path, 'w', encoding='utf-8') as f:
    json.dump(guides_data, f, ensure_ascii=False, indent=2)

print(f"Updated guides.json with new entry")
print(f"Total guides now: {len(guides_data['guides'])}")
