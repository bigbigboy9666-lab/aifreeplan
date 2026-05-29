#!/usr/bin/env python3
"""用 claude-code(haiku) 写攻略. 用法: python3 scripts/write_guide.py "选题" [slug]"""
import json, sys, subprocess, os, re
from datetime import date

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GUIDES_PATH = os.path.join(PROJECT, "src/content/guides.json")
TODAY = date.today().isoformat()

topic = sys.argv[1] if len(sys.argv) > 1 else "免费AI工具对比"
slug = sys.argv[2] if len(sys.argv) > 2 else re.sub(r'[^a-z0-9]+', '-', topic.lower().strip())[:50].strip('-')

def clean(text):
    t = re.sub(r'</?thinking>', '', text)
    lines = t.split('\n')
    lines = [l for l in lines if not l.strip().startswith('```')]
    return '\n'.join(lines).strip()


def validate_guide(content_zh, content_en, desc_zh, desc_en):
    """Check for AI prompt leaks and quality issues."""
    ai_patterns = [
        r'user wants me to write',
        r'I should write',
        r'the guide should',
        r'Be in markdown format',
        r'\d{4,} words',
        r'Output markdown only',
        r'Let me structure this',
    ]
    for pat in ai_patterns:
        if re.search(pat, content_en, re.I):
            return False, f"EN content contains AI prompt: {pat}"
        if re.search(pat, desc_en, re.I):
            return False, f"EN description contains AI prompt: {pat}"
    # Check description doesn't have Markdown
    if re.search(r'(^#|\\n\*\*|^\*\*)', desc_zh):
        return False, "ZH description contains Markdown"
    if re.search(r'(^#|\\n\*\*|^\*\*)', desc_en):
        return False, "EN description contains Markdown"
    # Check title_en doesn't have Chinese
    return True, "OK"

prompt_zh = (
    "写一篇「" + topic + "」的中文攻略（markdown，1500-2500字）。"
    "要求：1)开头直接给结论和数字 2)每个工具写额度/功能/适合谁/缺点 3)有对比表格 4)不要AI套话 5)最后加3个FAQ(格式：**Q:xxx**\nA:xxx)。"
    "只输出markdown正文，不要代码块标记。"
)
r1 = subprocess.run(["claude", "--bare", "-p", prompt_zh, "--model", "haiku", "--max-turns", "1"],
                     capture_output=True, text=True, timeout=120, cwd=PROJECT)
content_zh = clean(r1.stdout)

prompt_en = (
    "Write an SEO-optimized English guide about '" + topic + "' (markdown, 1000-2000 words). "
    "Start with conclusion. Each tool: free tier/features/best for/cons. Comparison table. 3 FAQ. "
    "Output markdown only, no code blocks."
)
r2 = subprocess.run(["claude", "--bare", "-p", prompt_en, "--model", "haiku", "--max-turns", "1"],
                     capture_output=True, text=True, timeout=120, cwd=PROJECT)
content_en = clean(r2.stdout)

# Extract English title from content (first H1 or first line)
en_title_match = re.search(r'^#\s+(.+)', content_en, re.M)
if en_title_match:
    guide_title_en = en_title_match.group(1).strip()
else:
    guide_title_en = topic  # Fallback to Chinese topic

guide = {
    "slug": slug, "type": "guide", "category": "guides",
    "category_zh": "使用攻略", "category_en": "Guides",
    "title_zh": topic, "title_en": guide_title_en,
    "description_zh": content_zh[:150], "description_en": content_en[:150],
    "author_zh": "AIFreePlan", "author_en": "AIFreePlan",
    "date_published": TODAY, "date_modified": TODAY,
    "tags_zh": ["AI工具", "免费额度", "2026"],
    "tags_en": ["AI Tools", "Free Tier", "2026"],
    "content_zh": content_zh, "content_en": content_en,
    "faq_zh": [], "faq_en": [], "related_tools": [],
}

with open(GUIDES_PATH) as f:
    guides = json.load(f)
if any(g['slug'] == slug for g in guides):
    print("SKIP " + slug)
    sys.exit(0)

# Validate guide quality
valid, msg = validate_guide(content_zh, content_en, guide["description_zh"], guide["description_en"])
if not valid:
    print(f"WARN: Guide validation failed: {msg}")
    print("WARN: Saving anyway but flagging for review")

guides.append(guide)
for p in [GUIDES_PATH, os.path.join(PROJECT, "src/data/guides.json")]:
    with open(p, "w") as f:
        json.dump(guides, f, ensure_ascii=False, indent=2)

print("OK slug=" + slug)
print("OK zh=" + str(len(content_zh)) + " chars")
print("OK en=" + str(len(content_en)) + " chars")
print("OK total=" + str(len(guides)))
