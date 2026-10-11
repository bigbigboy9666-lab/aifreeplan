#!/usr/bin/env python3
"""Quality gate for the BinkBink vs Rosebud AI game-maker free-comparison guide (zh+en)."""
import re, sys, json, os

BASE='/home/ubuntu/aifreeplan'
BOILER = [
  '总而言之','综上所述','值得注意的是','不言而喻','由此可见','在当今','随着.*的不断发展',
  'in conclusion','in summary','it is worth noting','in today\'s','as the world',
  'it is important to note','delve into','game-changer','unleash','supercharge',
  'revolutionize','in the ever-evolving','unlock the power','in an increasingly',
  'leveraging the power'
]

def body_text(html):
    m=re.search(r'<main\b[^>]*>(.*?)</main>', html, re.S)
    if not m: return ''
    t=re.sub(r'<[^>]+>',' ', m.group(1))
    t=re.sub(r'\s+',' ', t)
    return t.strip()

def check(slug, minlen=1000):
    res={}
    for lang in ['zh','en']:
        p=f'{BASE}/{lang}/guides/{slug}.html'
        if not os.path.exists(p):
            res[lang]={'missing':True}; continue
        html=open(p,encoding='utf-8').read()
        text=body_text(html)
        zh=len(re.findall(r'[\u4e00-\u9fff]', text))
        zhpct = (zh/len(text)*100) if text else 0
        nums = len(re.findall(r'\d', text))
        hits = [b for b in BOILER if re.search(b, text, re.I)]
        res[lang]={
            'chars':len(text),
            'zh_chars':zh,
            'zh_pct':round(zhpct,1),
            'num_digits':nums,
            'boilerplate_hits':hits,
            'ok': (len(text)>minlen) and (zhpct<5 if lang=='en' else True) and (nums>=8),
        }
    return res

if __name__=='__main__':
    slug='binkbink-rosebud-ai-game-maker-free-comparison-2026'
    r=check(slug)
    good = all(v.get('ok',False) for k,v in r.items() if 'ok' in v)
    print(f'=== {slug}  SHIP={"YES" if good else "NO"} ===')
    print(json.dumps(r,ensure_ascii=False,indent=2))
    sys.exit(0 if good else 1)
