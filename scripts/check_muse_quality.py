#!/usr/bin/env python3
import re, json

slug = "meta-muse-free-personal-ai-agent-2026"

def cjk_ratio(text):
    total = len(text)
    if total == 0:
        return 0.0, 0, 0
    cjk = sum(1 for ch in text if '\u4e00' <= ch <= '\u9fff')
    return cjk / total, cjk, total

def visible_text(html):
    t = re.sub(r'<[^>]+>', ' ', html)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

for lang in ['zh', 'en']:
    p = f'/home/ubuntu/aifreeplan/{lang}/guides/{slug}.html'
    html = open(p, encoding='utf-8').read()
    main = re.search(r'<main\b[^>]*>(.*)</main>', html, re.S)
    body = main.group(1) if main else ''
    vt = visible_text(body)
    ratio, cjk, tot = cjk_ratio(vt)
    ok = (tot > 1000) and (ratio < 0.05)
    print(f"[{lang}] body text chars={tot}  CJK={cjk}  CJK_ratio={ratio*100:.2f}%  PASS(>1000 & CJK<5%)={ok}")

d = json.load(open('/home/ubuntu/aifreeplan/public/data/guides.json', encoding='utf-8'))
e = [g for g in d['guides'] if g['slug'] == slug][0]
for k in ['title_zh', 'title_en', 'excerpt_zh', 'excerpt_en', 'faq_zh', 'faq_en', 'tags', 'category', 'date_published']:
    print(f"  field {k}: {'OK' if k in e else 'MISSING'}")
print("  faq_zh count:", len(e['faq_zh']), " faq_en count:", len(e['faq_en']))
print("  total guides in public/data:", len(d['guides']))
