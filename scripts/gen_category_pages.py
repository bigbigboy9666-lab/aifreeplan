#!/usr/bin/env python3
import json

d = json.load(open('/home/ubuntu/aifreeplan/data.json'))
tools = d['tools']

cats = {}
for t in tools:
    cat = t.get('category', 'other')
    if cat not in cats:
        cats[cat] = []
    cats[cat].append(t)

cat_meta = {
    'video': {
        'zh': {'name': '视频生成', 'emoji': '🎬', 'h1': '免费AI视频生成额度汇总', 'intro': '汇总所有AI视频生成工具的免费额度、分辨率、水印和使用限制。包括可灵AI、海螺AI、Seedance 2.0、Sora、Runway等主流平台，一张表看清免费额度差异。', 'desc': '免费AI视频生成工具额度对比，覆盖可灵、海螺、Seedance、Sora、Runway等，含分辨率、水印、时长限制。'},
        'en': {'name': 'Video Generation', 'emoji': '🎬', 'h1': 'Free AI Video Generation Credits', 'intro': 'Compare free credits, resolution, watermarks, and limits across all AI video generation tools. Covers Kling, Hailuo, Seedance 2.0, Sora, Runway and more.', 'desc': 'Free AI video generation tools comparison. Covers Kling, Hailuo, Seedance, Sora, Runway with credits, resolution, watermark details.'},
    },
    'image': {
        'zh': {'name': '图片生成', 'emoji': '🖼️', 'h1': '免费AI图片生成额度汇总', 'intro': '汇总所有AI图片生成工具的免费额度、分辨率、水印和限制。包括GPT Image 2、Stable Diffusion、NanoPro、即梦AI、通义万相等，从在线工具到本地部署全覆盖。', 'desc': '免费AI图片生成工具额度对比，覆盖GPT Image 2、Stable Diffusion、NanoPro、即梦、通义万相等。'},
        'en': {'name': 'Image Generation', 'emoji': '🖼️', 'h1': 'Free AI Image Generation Credits', 'intro': 'Compare free credits, resolution, watermarks across all AI image generation tools. Covers GPT Image 2, Stable Diffusion, NanoPro, Jimeng, Tongyi Wanxiang and more.', 'desc': 'Free AI image generation tools comparison. GPT Image 2, Stable Diffusion, NanoPro and more with credits and watermark details.'},
    },
    'llm': {
        'zh': {'name': 'AI大模型', 'emoji': '🤖', 'h1': '免费AI大模型额度汇总', 'intro': '汇总所有AI大语言模型的免费额度和调用限制。包括DeepSeek、ChatGPT、Claude、Grok、Gemini、通义千问、Kimi等，一张表看清免费额度、API限制和过期时间。', 'desc': '免费AI大模型额度对比，覆盖DeepSeek、ChatGPT、Claude、Grok、Gemini、通义千问等。'},
        'en': {'name': 'AI LLM', 'emoji': '🤖', 'h1': 'Free AI LLM Credits 2026', 'intro': 'Compare free LLM plans from ChatGPT, Claude, Gemini, DeepSeek, Grok, Qwen, Kimi and more. See free credits, API limits, reset cycles, and no-credit-card availability.', 'desc': 'Free AI LLM credits comparison. ChatGPT, Claude, Gemini, DeepSeek, Grok free tiers with API limits and reset cycles.'},
    },
    'coding': {
        'zh': {'name': '编程助手', 'emoji': '💻', 'h1': '免费AI编程工具额度汇总', 'intro': '汇总所有AI编程助手的免费额度和使用限制。包括Cursor、GitHub Copilot、Google Jules、Codeium、通义灵码等，一张表看清免费补全次数、API限制。', 'desc': '免费AI编程工具额度对比，覆盖Cursor、GitHub Copilot、Google Jules、Codeium等。'},
        'en': {'name': 'Coding', 'emoji': '💻', 'h1': 'Free AI Coding Tools Credits', 'intro': 'Compare free plans for AI coding assistants. Covers Cursor, GitHub Copilot, Google Jules, Codeium, Windsurf and more. See free completions, API limits, and features.', 'desc': 'Free AI coding tools comparison. Cursor, Copilot, Jules, Codeium free tiers with completions and API limits.'},
    },
    'ai-assistant': {
        'zh': {'name': 'AI助手', 'emoji': '🧠', 'h1': '免费AI助手额度汇总', 'intro': '汇总AI助手类工具的免费额度和使用限制。', 'desc': '免费AI助手额度对比。'},
        'en': {'name': 'AI Assistant', 'emoji': '🧠', 'h1': 'Free AI Assistant Credits', 'intro': 'Compare free plans for AI assistant tools.', 'desc': 'Free AI assistant tools comparison.'},
    },
    'audio': {
        'zh': {'name': 'AI音乐', 'emoji': '🎵', 'h1': '免费AI音乐生成额度汇总', 'intro': '汇总AI音乐生成工具的免费额度。', 'desc': '免费AI音乐生成工具额度对比。'},
        'en': {'name': 'AI Music', 'emoji': '🎵', 'h1': 'Free AI Music Generation Credits', 'intro': 'Compare free credits for AI music generation tools.', 'desc': 'Free AI music generation tools comparison.'},
    },
}

def get_free_summary(t, lang='zh'):
    fc = t.get('free_credits', {})
    if lang == 'zh':
        return fc.get('amount', '待确认'), fc.get('reset', '待确认'), fc.get('resolution', 'N/A'), fc.get('watermark', '待确认')
    else:
        return fc.get('amount_en', fc.get('amount', 'TBD')), fc.get('reset_en', fc.get('reset', 'TBD')), fc.get('resolution', 'N/A'), fc.get('watermark_en', fc.get('watermark', 'TBD'))

def make_category_page(cat, lang):
    meta = cat_meta.get(cat, {}).get(lang)
    if not meta:
        return None
    tool_list = cats.get(cat, [])
    if not tool_list:
        return None

    is_zh = lang == 'zh'
    nav_all = '全部工具' if is_zh else 'All Tools'
    nav_guides = '攻略' if is_zh else 'Guides'
    nav_privacy = '隐私' if is_zh else 'Privacy'
    other_lang = 'en' if lang == 'zh' else 'zh'
    cta_text = '查看详情' if is_zh else 'View Details'
    th = ('工具','免费额度','重置周期','分辨率','水印') if is_zh else ('Tool','Free Credits','Reset Cycle','Resolution','Watermark')
    last_upd = '最后更新：2026年6月5日' if is_zh else 'Last updated: June 5, 2026'

    colors = {'video':'#DB2777','image':'#10B981','llm':'#6366F1','coding':'#0284C7','ai-assistant':'#F59E0B','audio':'#EC4899'}
    tag_bg = {'video':'#FCE7F3','image':'#D1FAE5','llm':'#E0E7FF','coding':'#E0F2FE','ai-assistant':'#FEF3C7','audio':'#FCE7F3'}
    color = colors.get(cat, '#6366F1')
    tbg = tag_bg.get(cat, '#E0E7FF')

    cards_html = ""
    table_rows = ""
    for t in tool_list:
        name = t.get('name', '')
        slug = t.get('slug', '')
        desc_zh = t.get('description', '')[:100]
        desc_en = t.get('description_en', '')[:100]
        desc = desc_zh if is_zh else desc_en
        amt, reset, res, wm = get_free_summary(t, lang)
        icon = name[0]

        bar = 50
        if '无限' in str(amt) or 'unlimited' in str(amt).lower() or '∞' in str(amt):
            bar = 100
        elif '免费' in str(amt) or 'free' in str(amt).lower():
            bar = 80

        cards_html += (
            f'<a href="/{lang}/{cat}/{slug}" class="tool-card" data-category="{cat}">'
            f'<div style="display:flex;justify-content:space-between;align-items:center">'
            f'<div style="width:44px;height:44px;border-radius:10px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:18px;font-weight:700;background:{color}">{icon}</div>'
            f'<span style="padding:4px 10px;border-radius:6px;font-size:12px;font-weight:600;background:{tbg};color:{color}">{meta["name"]}</span>'
            f'</div>'
            f'<div style="font-size:20px;font-weight:700">{name}</div>'
            f'<div style="font-size:14px;color:var(--text-secondary);line-height:1.5;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden">{desc}</div>'
            f'<div style="font-size:13px;color:var(--text-muted)">{amt}</div>'
            f'<div style="margin-top:auto;padding:10px 0;text-align:center;border-radius:8px;font-size:14px;font-weight:600;color:#fff;background:var(--text);cursor:pointer">{cta_text}</div>'
            f'</a>\n'
        )
        table_rows += (
            f'<tr><td><a href="/{lang}/{cat}/{slug}" style="color:var(--accent);text-decoration:none;font-weight:600">{name}</a></td>'
            f'<td>{amt}</td><td>{reset}</td><td>{res}</td><td>{wm}</td></tr>\n'
        )

    # FAQ
    faq_items = ""
    if is_zh:
        faqs = [
            (f"哪个{meta['name']}工具免费额度最多？", f"根据我们的对比，{tool_list[0].get('name','')}" + (f"和{tool_list[1].get('name','')}" if len(tool_list)>1 else "") + "是免费额度最慷慨的。详见上方对比表。"),
            (f"有没有不需要信用卡的{meta['name']}工具？", "有。DeepSeek、通义千问等国产工具通常不需要信用卡。部分海外工具如Google Gemini也不需要。"),
            (f"免费{meta['name']}工具可以商用吗？", "取决于具体工具和其免费版条款。Stable Diffusion开源协议允许商用，其他工具需确认各自的使用条款。"),
        ]
    else:
        faqs = [
            (f"Which {meta['name'].lower()} tool has the most generous free plan?", f"Based on our comparison, {tool_list[0].get('name','')}" + (f" and {tool_list[1].get('name','')}" if len(tool_list)>1 else "") + " offer the most generous free tiers."),
            (f"Are there {meta['name'].lower()} tools without credit card?", "Yes. DeepSeek, Qwen, and Google tools typically don't require a credit card for free tiers."),
            (f"Can I use free {meta['name'].lower()} tools commercially?", "It depends on the specific tool. Stable Diffusion's open source license allows commercial use. Check each tool's terms."),
        ]
    for q, a in faqs:
        faq_items += (
            f'<div style="margin-bottom:20px;padding-bottom:20px;border-bottom:1px solid var(--border-light)">'
            f'<div style="font-weight:700;margin-bottom:8px">Q: {q}</div>'
            f'<div style="color:var(--text-secondary);line-height:1.7">A: {a}</div></div>\n'
        )

    # ItemList JSON
    items_json = ",".join(
        '{"@type":"ListItem","position":' + str(i+1) + ',"name":"' + t.get('name','') + '"}'
        for i, t in enumerate(tool_list)
    )

    lang_switch = f"/{other_lang}/{cat}"
    home_text = "首页" if is_zh else "Home"
    prod_text = "产品" if is_zh else "Product"
    legal_text = "法律" if is_zh else "Legal"
    terms_text = "用户条款" if is_zh else "Terms"
    footer_desc = "AI驱动的免费工具聚合平台，永久免费。" if is_zh else "AI-powered free tools aggregator. Free forever."
    compare_text = "工具对比表" if is_zh else "Comparison Table"
    all_text = "全部工具" if is_zh else "All Tools"
    faq_text = "常见问题" if is_zh else "FAQ"

    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{meta['h1']} | AIFreePlan</title>
<meta name="description" content="{meta['desc']}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<meta name="theme-color" content="#6366F1">
<link rel="canonical" href="https://aifreeplan.com/{lang}/{cat}">
<link rel="alternate" hreflang="zh" href="https://aifreeplan.com/zh/{cat}">
<link rel="alternate" hreflang="en" href="https://aifreeplan.com/en/{cat}">
<link rel="alternate" hreflang="x-default" href="https://aifreeplan.com/en/{cat}">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{--bg:#F8FAFC;--bg-white:#fff;--border:#E2E8F0;--border-light:#F1F5F9;--text:#1E1B4B;--text-secondary:#64748B;--text-muted:#94A3B8;--accent:#6366F1;--accent-hover:#4F46E5;--accent-light:rgba(99,102,241,.1);--green:#059669;--shadow:0 4px 20px rgba(0,0,0,.05);--shadow-hover:0 8px 32px rgba(0,0,0,.1);--radius:12px}}
body{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Noto Sans SC","PingFang SC","Microsoft YaHei",sans-serif;background:var(--bg);color:var(--text);line-height:1.6}}
.container{{max-width:1280px;margin:0 auto;padding:0 40px}}
.header{{background:var(--bg-white);border-bottom:1px solid var(--border);position:sticky;top:0;z-index:100}}
.header-inner{{display:flex;align-items:center;justify-content:space-between;height:72px}}
.logo{{display:flex;align-items:center;gap:8px;text-decoration:none;color:var(--text);font-size:24px;font-weight:700}}
.logo .accent{{color:var(--accent)}}
.nav{{display:flex;gap:32px;align-items:center}}
.nav a{{color:var(--text);text-decoration:none;font-size:15px;font-weight:500}}
.nav a:hover{{color:var(--accent)}}
.btn{{display:inline-flex;align-items:center;justify-content:center;padding:10px 22px;border-radius:8px;font-size:15px;font-weight:600;cursor:pointer;border:none;text-decoration:none}}
.btn-primary{{background:var(--accent);color:#fff}}
.btn-primary:hover{{background:var(--accent-hover)}}
.breadcrumb{{font-size:14px;color:var(--text-muted);margin-bottom:24px}}
.breadcrumb a{{color:var(--text-muted);text-decoration:none}}
.breadcrumb a:hover{{color:var(--accent)}}
.breadcrumb-sep{{margin:0 8px}}
.card-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin:32px 0}}
.tool-card{{background:var(--bg-white);border-radius:16px;padding:24px;box-shadow:var(--shadow);transition:all .2s;display:flex;flex-direction:column;gap:14px;text-decoration:none;color:var(--text)}}
.tool-card:hover{{transform:translateY(-4px);box-shadow:var(--shadow-hover)}}
table{{width:100%;border-collapse:collapse;margin:24px 0;font-size:14px}}
th,td{{padding:12px 16px;border:1px solid var(--border);text-align:left}}
th{{background:var(--accent-light);font-weight:600;font-size:13px}}
tr:hover{{background:var(--bg)}}
.faq-section{{background:var(--bg-white);border-radius:var(--radius);padding:32px;margin-top:40px;box-shadow:var(--shadow)}}
.footer{{background:#1a1a2e;padding:50px 0 30px;color:#fff;margin-top:60px}}
.footer-inner{{display:flex;justify-content:space-between;gap:60px;flex-wrap:wrap}}
.footer-brand p{{font-size:14px;color:rgba(255,255,255,.6)}}
.footer-links{{display:flex;gap:60px}}
.footer-col{{display:flex;flex-direction:column;gap:10px}}
.footer-col h4{{font-size:14px;font-weight:700;color:#fff}}
.footer-col a{{color:rgba(255,255,255,.6);text-decoration:none;font-size:14px}}
.footer-col a:hover{{color:#fff}}
.footer-bottom{{margin-top:30px;padding-top:20px;border-top:1px solid rgba(255,255,255,.1);font-size:13px;color:rgba(255,255,255,.4)}}
@media(max-width:1024px){{.card-grid{{grid-template-columns:repeat(3,1fr)}}}}
@media(max-width:768px){{.card-grid{{grid-template-columns:repeat(2,1fr)}}.container{{padding:0 16px}}.nav{{display:none}}}}
@media(max-width:480px){{.card-grid{{grid-template-columns:1fr}}}}
</style>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"CollectionPage","name":"{meta['h1']}","description":"{meta['desc']}","url":"https://aifreeplan.com/{lang}/{cat}","mainEntity":{{"@type":"ItemList","numberOfItems":{len(tool_list)},"itemListElement":[{items_json}]}}}}
</script>
</head>
<body>
<header class="header">
  <div class="container header-inner">
    <a href="/{lang}" class="logo">AI<span class="accent">FreePlan</span></a>
    <nav class="nav">
      <a href="/{lang}/all">{nav_all}</a>
      <a href="/{lang}/guides">{nav_guides}</a>
      <a href="/{lang}/privacy">{nav_privacy}</a>
      <a href="{lang_switch}" class="btn btn-primary">{"English" if is_zh else "中文"}</a>
    </nav>
  </div>
</header>
<main class="container" style="padding-top:40px;padding-bottom:80px">
<nav class="breadcrumb"><a href="/{lang}">{home_text}</a> <span class="breadcrumb-sep">›</span> <span>{meta['name']}</span></nav>
<h1 style="font-size:36px;font-weight:700;margin-bottom:16px">{meta['emoji']} {meta['h1']}</h1>
<p style="color:var(--text-secondary);line-height:1.8;max-width:800px;margin-bottom:32px">{meta['intro']}</p>
<h2 style="font-size:24px;font-weight:700;margin-top:40px;margin-bottom:16px">{compare_text}</h2>
<div style="overflow-x:auto">
<table>
<thead><tr><th>{th[0]}</th><th>{th[1]}</th><th>{th[2]}</th><th>{th[3]}</th><th>{th[4]}</th></tr></thead>
<tbody>
{table_rows}
</tbody>
</table>
</div>
<h2 style="font-size:24px;font-weight:700;margin-top:40px;margin-bottom:16px">{all_text} ({len(tool_list)})</h2>
<div class="card-grid">
{cards_html}
</div>
<div class="faq-section">
<h3 style="font-size:20px;font-weight:700;margin-bottom:20px">{faq_text}</h3>
{faq_items}
</div>
<p style="margin-top:40px;font-size:13px;color:var(--text-muted)">{last_upd}</p>
</main>
<footer class="footer">
  <div class="container footer-inner">
    <div class="footer-brand"><a href="/{lang}" class="logo" style="color:#059669">AI<span class="accent" style="color:#6366F1">FreePlan</span></a><p>{footer_desc}</p></div>
    <div class="footer-links">
      <div class="footer-col"><h4>{prod_text}</h4><a href="/{lang}/all">{nav_all}</a><a href="/{lang}/guides">{nav_guides}</a></div>
      <div class="footer-col"><h4>{legal_text}</h4><a href="/{lang}/privacy">{nav_privacy}</a><a href="/{lang}/terms">{terms_text}</a></div>
    </div>
  </div>
  <div class="container footer-bottom">© 2026 AIFreePlan.</div>
</footer>
</body></html>'''
    return html

count = 0
for cat in ['video', 'image', 'llm', 'coding', 'ai-assistant', 'audio']:
    for lang in ['zh', 'en']:
        html = make_category_page(cat, lang)
        if html:
            filepath = f"/home/ubuntu/aifreeplan/{lang}/{cat}.html"
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)
            count += 1
            print(f"Generated: {filepath}")

print(f"\nTotal: {count} category pages generated")
