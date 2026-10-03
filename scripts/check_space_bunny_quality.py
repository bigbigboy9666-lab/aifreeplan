#!/usr/bin/env python3
"""Quality check for the Space Bunny guide (zh+en).
- content_zh and content_en body text each > 1000 chars
- no Chinese residue in the EN version (zh char ratio < 5%)
- has concrete numbers
"""
import re, os, json, sys

BASE = '/home/ubuntu/aifreeplan'
SLUG = 'space-bunny-alpha-free-openrouter-2026'

def body_text(html):
    m = re.search(r'<main\b[^>]*>(.*?)</main>', html, re.S)
    if not m:
        return ''
    t = re.sub(r'<[^>]+>', ' ', m.group(1))
    t = re.sub(r'\s+', ' ', t)
    return t.strip()

res = {}
allgood = True
for lang in ['zh', 'en']:
    p = f'{BASE}/{lang}/guides/{SLUG}.html'
    if not os.path.exists(p):
        res[lang] = {'missing': True}
        allgood = False
        continue
    html = open(p, encoding='utf-8').read()
    text = body_text(html)
    zh = len(re.findall(r'[\u4e00-\u9fff]', text))
    zhpct = (zh / len(text) * 100) if text else 0
    digits = len(re.findall(r'\d', text))
    entry = {
        'chars': len(text),
        'zh_chars': zh,
        'zh_pct': round(zhpct, 2),
        'num_digits': digits,
        'ok': True,
    }
    # char threshold
    if len(text) <= 1000:
        entry['ok'] = False
        entry['reason_chars'] = len(text)
    if lang == 'en' and zhpct >= 5:
        entry['ok'] = False
        entry['reason_zh_residue'] = zhpct
    if digits < 8:
        entry['ok'] = False
        entry['reason_digits'] = digits
    res[lang] = entry
    if not entry['ok']:
        allgood = False

print(json.dumps(res, ensure_ascii=False, indent=2))
print('OVERALL:', 'PASS' if allgood else 'FAIL')
sys.exit(0 if allgood else 1)
