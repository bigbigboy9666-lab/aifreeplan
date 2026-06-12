#!/usr/bin/env python3
"""
生成攻略文章的脚本
用法: python3 scripts/write_guide.py "选题描述" slug-name
"""

import json
import os
import sys
from datetime import datetime

def generate_guide_html(slug, title_zh, title_en, description_zh, description_en, content_zh, content_en, faq_zh, faq_en, date_published):
    """生成攻略HTML页面"""
    
    # 中文版
    zh_html = f'''<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_zh} | AIFreePlan</title>
<meta property="og:type" content="article">
<meta property="og:title" content="{title_zh} | AIFreePlan">
<meta property="og:description" content="{description_zh}">
<meta property="og:url" content="https://aifreeplan.com/zh/guides/{slug}">
<meta property="og:site_name" content="AIFreePlan">
<meta property="og:locale" content="zh_CN">
<meta property="og:image" content="https://aifreeplan.com/og-image.jpg">
<meta name="twitter:image" content="https://aifreeplan.com/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title_zh} | AIFreePlan">
<meta name="twitter:description" content="{description_zh}">
<meta name="description" content="{description_zh}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<meta name="theme-color" content="#6366F1">
<link rel="canonical" href="https://aifreeplan.com/zh/guides/{slug}">
<link rel="alternate" hreflang="zh" href="https://aifreeplan.com/zh/guides/{slug}">
<link rel="alternate" hreflang="en" href="https://aifreeplan.com/en/guides/{slug}">
<link rel="alternate" hreflang="x-default" href="https://aifreeplan.com/en/guides/{slug}">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{--bg:#F8FAFC;--bg-white:#fff;--border:#E2E8F0;--border-light:#F1F5F9;--text:#1E1B4B;--text-secondary:#64748B;--text-muted:#94A3B8;--accent:#6366F1;--accent-hover:#4F46E5;--accent-light:rgba(99,102,241,.1);--green:#059669;--green-light:rgba(5,150,105,.1);--shadow:0 4px 20px rgba(0,0,0,.05);--radius:12px}}
body{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Noto Sans SC","PingFang SC","Microsoft YaHei",sans-serif;background:var(--bg);color:var(--text);line-height:1.6}}
.container{{max-width:1280px;margin:0 auto;padding:0 40px}}
.header{{background:var(--bg-white);border-bottom:1px solid var(--border);position:sticky;top:0;z-index:100}}
.header-inner{{display:flex;align-items:center;justify-content:space-between;height:72px}}
.logo{{display:flex;align-items:center;gap:8px;text-decoration:none;color:var(--text);font-size:24px;font-weight:700}}
.logo .accent{{color:var(--accent)}}
.nav{{display:flex;gap:32px;align-items:center}}
.nav a{{color:var(--text);text-decoration:none;font-size:15px;font-weight:500;transition:color .2s}}
.nav a:hover{{color:var(--accent)}}
.btn{{display:inline-flex;align-items:center;justify-content:center;padding:10px 22px;border-radius:8px;font-size:15px;font-weight:600;cursor:pointer;border:none;transition:all .2s;text-decoration:none}}
.btn-primary{{background:var(--accent);color:#fff}}
.btn-primary:hover{{background:var(--accent-hover)}}
.article-container{{max-width:800px;margin:0 auto;padding:40px 20px 80px}}
.article-container h1{{font-size:36px;font-weight:700;margin-bottom:16px;line-height:1.3}}
.article-container h2{{font-size:24px;font-weight:700;margin-top:40px;margin-bottom:16px;padding-top:24px;border-top:1px solid var(--border)}}
.article-container h3{{font-size:20px;font-weight:600;margin-top:32px;margin-bottom:12px}}
.article-container p{{margin-bottom:16px;color:var(--text-secondary);line-height:1.8}}
.article-container ul,.article-container ol{{margin-bottom:16px;padding-left:24px;color:var(--text-secondary)}}
.article-container li{{margin-bottom:8px;line-height:1.6}}
.article-container img{{max-width:100%;height:auto;border-radius:12px;margin:24px 0;box-shadow:var(--shadow)}}
.article-container a{{color:var(--accent);text-decoration:underline}}
.article-container table{{width:100%;border-collapse:collapse;margin:20px 0;font-size:14px}}
.article-container th,.article-container td{{padding:12px;border:1px solid var(--border);text-align:left}}
.article-container th{{background:var(--accent-light);font-weight:600}}
.breadcrumb{{font-size:14px;color:var(--text-muted);margin-bottom:24px}}
.breadcrumb a{{color:var(--text-muted);text-decoration:none}}
.breadcrumb a:hover{{color:var(--accent)}}
.breadcrumb-sep{{margin:0 8px}}
.faq-section{{background:var(--bg-white);border-radius:var(--radius);padding:32px;margin-top:40px;box-shadow:var(--shadow)}}
.faq-section h3{{margin-top:0;color:var(--text)}}
.faq-item{{margin-bottom:20px;padding-bottom:20px;border-bottom:1px solid var(--border-light)}}
.faq-item:last-child{{border-bottom:none;margin-bottom:0;padding-bottom:0}}
.faq-q{{font-weight:700;color:var(--text);margin-bottom:8px}}
.faq-a{{color:var(--text-secondary);line-height:1.7}}
.footer{{background:#1a1a2e;padding:50px 0 30px;color:#fff;margin-top:60px}}
.footer-inner{{display:flex;justify-content:space-between;gap:60px;flex-wrap:wrap}}
.footer-brand{{max-width:300px}}
.footer-brand p{{font-size:14px;color:rgba(255,255,255,.6)}}
.footer-links{{display:flex;gap:60px}}
.footer-col{{display:flex;flex-direction:column;gap:10px}}
.footer-col h4{{font-size:14px;font-weight:700;color:#fff}}
.footer-col a{{color:rgba(255,255,255,.6);text-decoration:none;font-size:14px}}
.footer-col a:hover{{color:#fff}}
.footer-bottom{{margin-top:30px;padding-top:20px;border-top:1px solid rgba(255,255,255,.1);font-size:13px;color:rgba(255,255,255,.4)}}
@media(max-width:768px){{.article-container{{padding:16px 16px 48px;max-width:100%}}.article-container h1{{font-size:24px}}.article-container h2{{font-size:20px}}.container{{padding:0 16px}}.nav{{display:none}}}}
</style>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article","headline":"{title_zh}","description":"{description_zh}","url":"https://aifreeplan.com/zh/guides/{slug}","datePublished":"{date_published}","dateModified":"{date_published}","author":{{"@type":"Organization","name":"AIFreePlan"}},"publisher":{{"@type":"Organization","name":"AIFreePlan","url":"https://aifreeplan.com"}},"mainEntityOfPage":{{"@type":"WebPage","@id":"https://aifreeplan.com/zh/guides/{slug}"}}}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"首页","item":"https://aifreeplan.com/zh"}},{{"@type":"ListItem","position":2,"name":"攻略","item":"https://aifreeplan.com/zh/guides"}},{{"@type":"ListItem","position":3,"name":"{title_zh}","item":"https://aifreeplan.com/zh/guides/{slug}"}}]}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_zh}]}}
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
      <a href="/en/guides/{slug}" class="btn btn-primary">English</a>
    </nav>
  </div>
</header>
<main class="article-container">
<nav class="breadcrumb"><a href="/zh">首页</a> <span class="breadcrumb-sep">›</span> <a href="/zh/guides">攻略</a> <span class="breadcrumb-sep">›</span> <span>{title_zh}</span></nav>
{content_zh}
</main>
<footer class="footer">
  <div class="container footer-inner">
    <div class="footer-brand"><a href="/zh" class="logo" style="color:#059669">AI<span class="accent" style="color:#6366F1">FreePlan</span></a><p>AI驱动的免费工具聚合平台，永久免费。</p></div>
    <div class="footer-links">
      <div class="footer-col"><h4>产品</h4><a href="/zh/all">全部工具</a><a href="/zh/guides">攻略</a></div>
      <div class="footer-col"><h4>法律</h4><a href="/zh/privacy">隐私政策</a><a href="/zh/terms">用户协议</a></div>
    </div>
  </div>
  <div class="container footer-bottom">© 2026 AIFreePlan. All rights reserved.</div>
</footer>
</body></html>'''
    
    # 英文版
    en_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_en} | AIFreePlan</title>
<meta property="og:type" content="article">
<meta property="og:title" content="{title_en} | AIFreePlan">
<meta property="og:description" content="{description_en}">
<meta property="og:url" content="https://aifreeplan.com/en/guides/{slug}">
<meta property="og:site_name" content="AIFreePlan">
<meta property="og:locale" content="en_US">
<meta property="og:image" content="https://aifreeplan.com/og-image.jpg">
<meta name="twitter:image" content="https://aifreeplan.com/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title_en} | AIFreePlan">
<meta name="twitter:description" content="{description_en}">
<meta name="description" content="{description_en}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<meta name="theme-color" content="#6366F1">
<link rel="canonical" href="https://aifreeplan.com/en/guides/{slug}">
<link rel="alternate" hreflang="zh" href="https://aifreeplan.com/zh/guides/{slug}">
<link rel="alternate" hreflang="en" href="https://aifreeplan.com/en/guides/{slug}">
<link rel="alternate" hreflang="x-default" href="https://aifreeplan.com/en/guides/{slug}">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{--bg:#F8FAFC;--bg-white:#fff;--border:#E2E8F0;--border-light:#F1F5F9;--text:#1E1B4B;--text-secondary:#64748B;--text-muted:#94A3B8;--accent:#6366F1;--accent-hover:#4F46E5;--accent-light:rgba(99,102,241,.1);--green:#059669;--green-light:rgba(5,150,105,.1);--shadow:0 4px 20px rgba(0,0,0,.05);--radius:12px}}
body{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Noto Sans SC","PingFang SC","Microsoft YaHei",sans-serif;background:var(--bg);color:var(--text);line-height:1.6}}
.container{{max-width:1280px;margin:0 auto;padding:0 40px}}
.header{{background:var(--bg-white);border-bottom:1px solid var(--border);position:sticky;top:0;z-index:100}}
.header-inner{{display:flex;align-items:center;justify-content:space-between;height:72px}}
.logo{{display:flex;align-items:center;gap:8px;text-decoration:none;color:var(--text);font-size:24px;font-weight:700}}
.logo .accent{{color:var(--accent)}}
.nav{{display:flex;gap:32px;align-items:center}}
.nav a{{color:var(--text);text-decoration:none;font-size:15px;font-weight:500;transition:color .2s}}
.nav a:hover{{color:var(--accent)}}
.btn{{display:inline-flex;align-items:center;justify-content:center;padding:10px 22px;border-radius:8px;font-size:15px;font-weight:600;cursor:pointer;border:none;transition:all .2s;text-decoration:none}}
.btn-primary{{background:var(--accent);color:#fff}}
.btn-primary:hover{{background:var(--accent-hover)}}
.article-container{{max-width:800px;margin:0 auto;padding:40px 20px 80px}}
.article-container h1{{font-size:36px;font-weight:700;margin-bottom:16px;line-height:1.3}}
.article-container h2{{font-size:24px;font-weight:700;margin-top:40px;margin-bottom:16px;padding-top:24px;border-top:1px solid var(--border)}}
.article-container h3{{font-size:20px;font-weight:600;margin-top:32px;margin-bottom:12px}}
.article-container p{{margin-bottom:16px;color:var(--text-secondary);line-height:1.8}}
.article-container ul,.article-container ol{{margin-bottom:16px;padding-left:24px;color:var(--text-secondary)}}
.article-container li{{margin-bottom:8px;line-height:1.6}}
.article-container img{{max-width:100%;height:auto;border-radius:12px;margin:24px 0;box-shadow:var(--shadow)}}
.article-container a{{color:var(--accent);text-decoration:underline}}
.article-container table{{width:100%;border-collapse:collapse;margin:20px 0;font-size:14px}}
.article-container th,.article-container td{{padding:12px;border:1px solid var(--border);text-align:left}}
.article-container th{{background:var(--accent-light);font-weight:600}}
.breadcrumb{{font-size:14px;color:var(--text-muted);margin-bottom:24px}}
.breadcrumb a{{color:var(--text-muted);text-decoration:none}}
.breadcrumb a:hover{{color:var(--accent)}}
.breadcrumb-sep{{margin:0 8px}}
.faq-section{{background:var(--bg-white);border-radius:var(--radius);padding:32px;margin-top:40px;box-shadow:var(--shadow)}}
.faq-section h3{{margin-top:0;color:var(--text)}}
.faq-item{{margin-bottom:20px;padding-bottom:20px;border-bottom:1px solid var(--border-light)}}
.faq-item:last-child{{border-bottom:none;margin-bottom:0;padding-bottom:0}}
.faq-q{{font-weight:700;color:var(--text);margin-bottom:8px}}
.faq-a{{color:var(--text-secondary);line-height:1.7}}
.footer{{background:#1a1a2e;padding:50px 0 30px;color:#fff;margin-top:60px}}
.footer-inner{{display:flex;justify-content:space-between;gap:60px;flex-wrap:wrap}}
.footer-brand{{max-width:300px}}
.footer-brand p{{font-size:14px;color:rgba(255,255,255,.6)}}
.footer-links{{display:flex;gap:60px}}
.footer-col{{display:flex;flex-direction:column;gap:10px}}
.footer-col h4{{font-size:14px;font-weight:700;color:#fff}}
.footer-col a{{color:rgba(255,255,255,.6);text-decoration:none;font-size:14px}}
.footer-col a:hover{{color:#fff}}
.footer-bottom{{margin-top:30px;padding-top:20px;border-top:1px solid rgba(255,255,255,.1);font-size:13px;color:rgba(255,255,255,.4)}}
@media(max-width:768px){{.article-container{{padding:16px 16px 48px;max-width:100%}}.article-container h1{{font-size:24px}}.article-container h2{{font-size:20px}}.container{{padding:0 16px}}.nav{{display:none}}}}
</style>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article","headline":"{title_en}","description":"{description_en}","url":"https://aifreeplan.com/en/guides/{slug}","datePublished":"{date_published}","dateModified":"{date_published}","author":{{"@type":"Organization","name":"AIFreePlan"}},"publisher":{{"@type":"Organization","name":"AIFreePlan","url":"https://aifreeplan.com"}},"mainEntityOfPage":{{"@type":"WebPage","@id":"https://aifreeplan.com/en/guides/{slug}"}}}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://aifreeplan.com/en"}},{{"@type":"ListItem","position":2,"name":"Guides","item":"https://aifreeplan.com/en/guides"}},{{"@type":"ListItem","position":3,"name":"{title_en}","item":"https://aifreeplan.com/en/guides/{slug}"}}]}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_en}]}}
</script>
</head>
<body>
<header class="header">
  <div class="container header-inner">
    <a href="/en" class="logo">AI<span class="accent">FreePlan</span></a>
    <nav class="nav">
      <a href="/en/all">All Tools</a>
      <a href="/en/guides">Guides</a>
      <a href="/en/privacy">Privacy</a>
      <a href="/zh/guides/{slug}" class="btn btn-primary">中文</a>
    </nav>
  </div>
</header>
<main class="article-container">
<nav class="breadcrumb"><a href="/en">Home</a> <span class="breadcrumb-sep">›</span> <a href="/en/guides">Guides</a> <span class="breadcrumb-sep">›</span> <span>{title_en}</span></nav>
{content_en}
</main>
<footer class="footer">
  <div class="container footer-inner">
    <div class="footer-brand"><a href="/en" class="logo" style="color:#059669">AI<span class="accent" style="color:#6366F1">FreePlan</span></a><p>AI-powered free tools aggregator. Free forever.</p></div>
    <div class="footer-links">
      <div class="footer-col"><h4>Product</h4><a href="/en/all">All Tools</a><a href="/en/guides">Guides</a></div>
      <div class="footer-col"><h4>Legal</h4><a href="/en/privacy">Privacy</a><a href="/en/terms">Terms</a></div>
    </div>
  </div>
  <div class="container footer-bottom">© 2026 AIFreePlan. All rights reserved.</div>
</footer>
</body></html>'''
    
    return zh_html, en_html

def main():
    if len(sys.argv) < 3:
        print("用法: python3 scripts/write_guide.py '选题描述' slug-name")
        sys.exit(1)
    
    topic = sys.argv[1]
    slug = sys.argv[2]
    
    print(f"生成攻略: {topic} (slug: {slug})")
    
    # 这里应该调用LLM生成内容，但为了简化，我们使用模板
    # 实际使用时需要调用API生成内容
    
    today = datetime.now().strftime('%Y-%m-%d')
    
    # 示例内容 - 实际应该由LLM生成
    title_zh = f"{topic}免费使用攻略"
    title_en = f"{topic} Free Usage Guide"
    description_zh = f"{topic}免费使用教程，包含额度、限制、使用技巧等详细信息。"
    description_en = f"{topic} free usage tutorial with credits, limits, and tips."
    
    content_zh = f'''<h1>{title_zh}</h1>
<p>{description_zh}</p>

<h2>什么是{topic}</h2>
<p>{topic}是一个AI工具，提供免费使用额度。</p>

<h2>免费额度详情</h2>
<p>具体免费额度信息需要从官方获取。</p>

<h2>如何使用</h2>
<p>访问官方网站注册即可开始使用。</p>

<h2>优缺点分析</h2>
<p>优点：免费使用，功能丰富。</p>
<p>缺点：可能有使用限制。</p>

<div class="faq-section">
<h3>❓ 常见问题</h3>
<div class="faq-item"><div class="faq-q">Q: {topic}真的免费吗？</div><div class="faq-a">A: 是的，有免费版本可以使用。</div></div>
<div class="faq-item"><div class="faq-q">Q: 免费版有什么限制？</div><div class="faq-a">A: 具体限制请查看官方说明。</div></div>
</div>'''
    
    content_en = f'''<h1>{title_en}</h1>
<p>{description_en}</p>

<h2>What is {topic}</h2>
<p>{topic} is an AI tool that offers free usage credits.</p>

<h2>Free Credits Details</h2>
<p>Specific free credit information should be obtained from the official source.</p>

<h2>How to Use</h2>
<p>Visit the official website and register to start using.</p>

<h2>Pros and Cons</h2>
<p>Pros: Free to use, feature-rich.</p>
<p>Cons: May have usage limitations.</p>

<div class="faq-section">
<h3>❓ FAQ</h3>
<div class="faq-item"><div class="faq-q">Q: Is {topic} really free?</div><div class="faq-a">A: Yes, there is a free version available.</div></div>
<div class="faq-item"><div class="faq-q">Q: What are the limitations of the free version?</div><div class="faq-a">A: Please check the official documentation for specific limitations.</div></div>
</div>'''
    
    faq_zh = '''{"@type": "Question", "name": "''' + topic + '''真的免费吗？", "acceptedAnswer": {"@type": "Answer", "text": "是的，有免费版本可以使用。"}}, {"@type": "Question", "name": "免费版有什么限制？", "acceptedAnswer": {"@type": "Answer", "text": "具体限制请查看官方说明。"}}'''
    
    faq_en = '''{"@type": "Question", "name": "Is ''' + topic + ''' really free?", "acceptedAnswer": {"@type": "Answer", "text": "Yes, there is a free version available."}}, {"@type": "Question", "name": "What are the limitations of the free version?", "acceptedAnswer": {"@type": "Answer", "text": "Please check the official documentation for specific limitations."}}'''
    
    zh_html, en_html = generate_guide_html(
        slug, title_zh, title_en, description_zh, description_en,
        content_zh, content_en, faq_zh, faq_en, today
    )
    
    # 写入文件
    os.makedirs('/home/ubuntu/aifreeplan/zh/guides', exist_ok=True)
    os.makedirs('/home/ubuntu/aifreeplan/en/guides', exist_ok=True)
    
    with open(f'/home/ubuntu/aifreeplan/zh/guides/{slug}.html', 'w', encoding='utf-8') as f:
        f.write(zh_html)
    
    with open(f'/home/ubuntu/aifreeplan/en/guides/{slug}.html', 'w', encoding='utf-8') as f:
        f.write(en_html)
    
    print(f"✅ 已生成:")
    print(f"  - /zh/guides/{slug}.html")
    print(f"  - /en/guides/{slug}.html")
    print(f"  - 日期: {today}")

if __name__ == '__main__':
    main()
