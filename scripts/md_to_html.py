#!/usr/bin/env python3
"""Convert MD guide files to full HTML pages for aifreeplan.com"""
import json, os, sys, re
from datetime import datetime
import markdown

BASE = '/home/ubuntu/aifreeplan'
GUIDES_ZH = os.path.join(BASE, 'zh', 'guides')

# CSS template (from existing generated pages)
CSS_TEMPLATE = """*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#F8FAFC;--bg-white:#fff;--border:#E2E8F0;--border-light:#F1F5F9;--text:#1E1B4B;--text-secondary:#64748B;--text-muted:#94A3B8;--accent:#6366F1;--accent-hover:#4F46E5;--accent-light:rgba(99,102,241,.1);--green:#059669;--green-light:rgba(5,150,105,.1);--shadow:0 4px 20px rgba(0,0,0,.05);--radius:12px}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Noto Sans SC","PingFang SC","Microsoft YaHei",sans-serif;background:var(--bg);color:var(--text);line-height:1.6}
.container{max-width:1280px;margin:0 auto;padding:0 40px}
.header{background:var(--bg-white);border-bottom:1px solid var(--border);position:sticky;top:0;z-index:100}
.header-inner{display:flex;align-items:center;justify-content:space-between;height:72px}
.logo{display:flex;align-items:center;gap:8px;text-decoration:none;color:var(--text);font-size:24px;font-weight:700}
.logo .accent{color:var(--accent)}
.nav{display:flex;gap:32px;align-items:center}
.nav a{color:var(--text);text-decoration:none;font-size:15px;font-weight:500;transition:color .2s}
.nav a:hover{color:var(--accent)}
.btn{display:inline-flex;align-items:center;justify-content:center;padding:10px 22px;border-radius:8px;font-size:15px;font-weight:600;cursor:pointer;border:none;transition:all .2s;text-decoration:none}
.btn-primary{background:var(--accent);color:#fff}
.btn-primary:hover{background:var(--accent-hover)}
.article-container{max-width:800px;margin:0 auto;padding:40px 20px 80px}
.article-container h1{font-size:36px;font-weight:700;margin-bottom:16px;line-height:1.3}
.article-container h2{font-size:24px;font-weight:700;margin-top:40px;margin-bottom:16px;padding-top:24px;border-top:1px solid var(--border)}
.article-container h3{font-size:20px;font-weight:600;margin-top:32px;margin-bottom:12px}
.article-container p{margin-bottom:16px;color:var(--text-secondary);line-height:1.8}
.article-container ul,.article-container ol{margin-bottom:16px;padding-left:24px;color:var(--text-secondary)}
.article-container li{margin-bottom:8px;line-height:1.6}
.article-container img{max-width:100%;height:auto;border-radius:12px;margin:24px 0;box-shadow:var(--shadow)}
.article-container a{color:var(--accent);text-decoration:underline}
.article-container table{width:100%;border-collapse:collapse;margin:20px 0;font-size:14px}
.article-container th,.article-container td{padding:12px;border:1px solid var(--border);text-align:left}
.article-container th{background:var(--accent-light);font-weight:600}
.breadcrumb{font-size:14px;color:var(--text-muted);margin-bottom:24px}
.breadcrumb a{color:var(--text-muted);text-decoration:none}
.breadcrumb a:hover{color:var(--accent)}
.breadcrumb-sep{margin:0 8px}
.faq-section{background:var(--bg-white);border-radius:var(--radius);padding:32px;margin-top:40px;box-shadow:var(--shadow)}
.faq-section h3{margin-top:0;color:var(--text)}
.faq-item{margin-bottom:20px;padding-bottom:20px;border-bottom:1px solid var(--border-light)}
.faq-item:last-child{border-bottom:none;margin-bottom:0;padding-bottom:0}
.faq-q{font-weight:700;color:var(--text);margin-bottom:8px}
.faq-a{color:var(--text-secondary);line-height:1.7}
.footer{background:#1a1a2e;padding:50px 0 30px;color:#fff;margin-top:60px}
.footer-inner{display:flex;justify-content:space-between;gap:60px;flex-wrap:wrap}
.footer-brand{max-width:300px}
.footer-brand p{font-size:14px;color:rgba(255,255,255,.6)}
.footer-links{display:flex;gap:60px}
.footer-col{display:flex;flex-direction:column;gap:10px}
.footer-col h4{font-size:14px;font-weight:700;color:#fff}
.footer-col a{color:rgba(255,255,255,.6);text-decoration:none;font-size:14px}
.footer-col a:hover{color:#fff}
.footer-bottom{margin-top:30px;padding-top:20px;border-top:1px solid rgba(255,255,255,.1);font-size:13px;color:rgba(255,255,255,.4)}
@media(max-width:768px){.article-container{padding:16px 16px 48px;max-width:100%}.article-container h1{font-size:24px}.article-container h2{font-size:20px}.container{padding:0 16px}.nav{display:none}}
"""

HEADER_TEMPLATE = '''<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | AIFreePlan</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<meta name="theme-color" content="#6366F1">
<link rel="canonical" href="https://aifreeplan.com/zh/guides/{slug}">
<link rel="alternate" hreflang="zh" href="https://aifreeplan.com/zh/guides/{slug}">
<link rel="alternate" hreflang="en" href="https://aifreeplan.com/en/guides/{slug}">
<link rel="alternate" hreflang="x-default" href="https://aifreeplan.com/en/guides/{slug}">
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://aifreeplan.com/zh/guides/{slug}">
<meta property="og:site_name" content="AI Free Plan">
<meta property="og:locale" content="zh_CN">
<meta property="og:image" content="https://aifreeplan.com/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="https://aifreeplan.com/og-image.png">
<style>
{css}
</style>
<script type="application/ld+json">
{article_jsonld}
</script>
<script type="application/ld+json">
{breadcrumb_jsonld}
</script>
</head>
<body>
<header class="header">
  <div class="container header-inner">
    <a href="/zh" class="logo">AI<span class="accent">FreePlan</span></a>
    <nav class="nav">
      <a href="/zh/all">全部工具</a>
      <a href="/zh/guides">攻略</a>
      <a href="/zh/privacy">隐私</a>
    </nav>
  </div>
</header>'''

BODY_START = '<main class="article-container">'

FOOTER_TEMPLATE = '''</main>
<footer class="footer">
  <div class="container footer-inner">
    <div class="footer-brand"><a href="/zh" class="logo" style="color:#059669">AI<span class="accent" style="color:#6366F1">FreePlan</span></a><p>AI驱动的免费工具聚合平台，永久免费。</p></div>
    <div class="footer-links">
      <div class="footer-col"><h4>产品</h4><a href="/zh/all">全部工具</a><a href="/zh/guides">攻略</a></div>
      <div class="footer-col"><h4>法律</h4><a href="/zh/privacy">隐私政策</a><a href="/zh/terms">服务条款</a></div>
    </div>
  </div>
  <div class="container footer-bottom">&copy; 2026 AIFreePlan. All rights reserved.</div>
</footer>
</body></html>'''


def slug_to_title(slug, guides_data):
    """Look up title from guides.json"""
    for g in guides_data.get('guides', []):
        if g['slug'] == slug:
            return g.get('title_zh', slug), g.get('excerpt_zh', '')
    return slug, ''


def md_to_body(md_content):
    """Convert markdown to HTML body content (inside <main>)"""
    # Clean up the markdown - handle horizontal rules as section separators
    lines = md_content.split('\n')
    
    # Parse the first line as H1
    h1 = ''
    rest_lines = []
    started = False
    for line in lines:
        if line.startswith('# '):
            h1 = line[2:].strip()
            started = True
            continue
        if started and line.strip() == '':
            continue
        if started:
            rest_lines.append(line)
    
    if not h1:
        h1 = lines[0].strip().lstrip('# ').strip()
        rest_lines = lines[1:]
    
    # Convert markdown to HTML
    md_text = '\n'.join(rest_lines)
    # Replace --- with <hr> for section breaks
    md_text = re.sub(r'^---\s*$', '<hr>', md_text, flags=re.MULTILINE)
    
    html_body = markdown.markdown(md_text, extensions=['tables', 'fenced_code', 'toc'])
    
    # Build breadcrumb
    breadcrumb = f'<nav class="breadcrumb"><a href="/zh">首页</a> <span class="breadcrumb-sep">›</span> <a href="/zh/guides">攻略</a> <span class="breadcrumb-sep">›</span> <span>{h1}</span></nav>'
    
    # Build date
    today = datetime.now().strftime('%Y年%-m月%-d日')
    
    return h1, breadcrumb, html_body, today


def generate_html(slug, title, desc, body_html, date_str):
    """Generate complete HTML file"""
    article_jsonld = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": desc,
        "url": f"https://aifreeplan.com/zh/guides/{slug}",
        "datePublished": date_str or datetime.now().strftime('%Y-%m-%d'),
        "dateModified": datetime.now().strftime('%Y-%m-%d'),
        "author": {"@type": "Organization", "name": "AIFreePlan"},
        "publisher": {"@type": "Organization", "name": "AIFreePlan", "url": "https://aifreeplan.com"},
        "mainEntityOfPage": {"@type": "WebPage", "id": f"https://aifreeplan.com/zh/guides/{slug}"}
    }, ensure_ascii=False, indent=2)
    
    breadcrumb_jsonld = json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "首页", "item": "https://aifreeplan.com/zh"},
            {"@type": "ListItem", "position": 2, "name": "攻略", "item": "https://aifreeplan.com/zh/guides"},
            {"@type": "ListItem", "position": 3, "name": title, "item": f"https://aifreeplan.com/zh/guides/{slug}"}
        ]
    }, ensure_ascii=False, indent=2)
    
    head = HEADER_TEMPLATE.format(title=title, desc=desc, slug=slug, css=CSS_TEMPLATE.strip(),
                                   article_jsonld=article_jsonld, breadcrumb_jsonld=breadcrumb_jsonld)
    
    return head + '\n' + BODY_START + '\n' + body_html + '\n' + FOOTER_TEMPLATE


def main():
    with open(os.path.join(BASE, 'data', 'guides.json'), 'r') as f:
        guides_data = json.load(f)
    
    # Slugs to convert (only those that have md but no html)
    slugs = sys.argv[1:] if len(sys.argv) > 1 else None
    
    if not slugs:
        # Auto-detect: find slugs in guides.json that have md but no html
        guide_slugs = {g['slug'] for g in guides_data.get('guides', [])}
        existing_html = {f.replace('.html', '') for f in os.listdir(GUIDES_ZH) if f.endswith('.html')}
        slugs = sorted(guide_slugs - existing_html)
    
    print(f'Converting {len(slugs)} guides:')
    count = 0
    for slug in slugs:
        md_path = os.path.join(BASE, 'src', 'pages', 'zh', 'guides', f'{slug}.md')
        if not os.path.exists(md_path):
            print(f'  SKIP {slug}: MD file not found')
            continue
        
        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        title, desc = slug_to_title(slug, guides_data)
        h1, breadcrumb, body_html, date_str = md_to_body(md_content)
        
        html = generate_html(slug, h1, desc, body_html, date_str)
        
        out_path = os.path.join(GUIDES_ZH, f'{slug}.html')
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f'  OK {slug}: {len(html)} bytes -> {out_path}')
        count += 1
    
    print(f'\nDone! {count}/{len(slugs)} converted.')


if __name__ == '__main__':
    main()
