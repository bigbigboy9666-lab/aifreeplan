#!/usr/bin/env python3
"""
直接生成 NotebookLM 攻略文章
"""

import json
import os
import re
import sys
from datetime import datetime


def count_chinese_chars(text):
    """Count Chinese characters in text"""
    return len(re.findall(r'[\u4e00-\u9fff]', text))


def generate_guide_html(slug, title_zh, title_en, description_zh, description_en, content_zh, content_en, faq_zh, faq_en, date_published):
    """Generate guide HTML pages"""
    
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
<meta property="og:image" content="https://aifreeplan.com/og-image.png">
<meta name="twitter:image" content="https://aifreeplan.com/og-image.png">
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
  <div class="container footer-bottom">&copy; 2026 AIFreePlan. All rights reserved.</div>
</footer>
</body></html>'''
    
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
<meta property="og:image" content="https://aifreeplan.com/og-image.png">
<meta name="twitter:image" content="https://aifreeplan.com/og-image.png">
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
  <div class="container footer-bottom">&copy; 2026 AIFreePlan. All rights reserved.</div>
</footer>
</body></html>'''
    
    return zh_html, en_html


def main():
    slug = "notebooklm-free-guide-2026"
    today = datetime.now().strftime('%Y-%m-%d')
    
    title_zh = "NotebookLM完全免费攻略：Google出品的AI研究神器，50个来源+播客生成+视频解说全免费"
    title_en = "NotebookLM Complete Free Guide: Google's AI Research Tool with 50 Sources, Podcast & Video Generation — All Free"
    description_zh = "Google出品的AI研究工具NotebookLM，完全免费使用。支持上传50个来源文档，自动生成播客式对话、视频解说和研究摘要。2026年仍是唯一不收费的主流AI研究工具。"
    description_en = "Google's AI research tool NotebookLM, completely free. Upload up to 50 source documents, auto-generate podcast-style conversations, video explanations and research summaries. In 2026, still the only mainstream AI research tool that remains free."
    
    content_zh = '''<h1>NotebookLM完全免费攻略：Google出品的AI研究神器，50个来源+播客生成+视频解说全免费</h1>
<p>Google出品的AI研究工具NotebookLM，完全免费使用。支持上传50个来源文档，自动生成播客式对话、视频解说和研究摘要。2026年仍是唯一不收费的主流AI研究工具。</p>

<h2>什么是NotebookLM</h2>
<p>NotebookLM是Google在2023年底推出的AI研究工具，2024年正式面向公众开放。它的核心思路很简单：你把资料丢进去，它帮你读、帮你总结、帮你生成各种形式的内容输出。不像ChatGPT或Claude那样让你从零开始对话，NotebookLM的AI回答严格限定在你上传的资料范围内，不会出现胡编乱造的情况。</p>
<p>在2026年，市面上号称"AI研究工具"的产品不少，但绝大多数要么收费（Perplexity Pro $20/月，Gemini Advanced $19.99/月），要么对免费用户有严格限制。NotebookLM是唯一一个从发布至今<strong>完全免费</strong>的主流AI研究工具，没有隐藏收费，没有VIP层级，没有"免费试用后收费"的套路。</p>

<h2>免费额度详解</h2>
<p>NotebookLM的免费版没有任何订阅费用，以下是具体的免费使用限制：</p>
<ul>
<li><strong>每个笔记本最多上传50个来源文件</strong>：这是目前所有同类工具中最高的免费上限。Perplexity免费版只支持少量文件上传，而NotebookLM允许你一次性导入50份文档进行综合分析。</li>
<li><strong>每个来源文件最大500页</strong>：对于学术论文、报告、手册等常见文档类型，500页的限制基本不会成为瓶颈。</li>
<li><strong>支持的文件格式</strong>：PDF、Google Docs、文本文件（.txt）、HTML文件、Markdown文件。不支持Word文档（.docx），需要先用Google Docs打开再保存为Google Docs格式。</li>
<li><strong>播客生成（Audio Overview）</strong>：完全免费，每次生成约10-20分钟的对话式播客，由两个AI主持人讨论你的资料内容。免费版没有生成次数限制。</li>
<li><strong>视频解说（Video Overview）</strong>：2025年新增功能，免费使用。将你的资料转化为带有AI主持人的短视频解说，适合做教学或分享。</li>
<li><strong>对话问答</strong>：无限次提问，AI会基于你上传的资料给出带引用的回答。免费版没有消息条数限制。</li>
<li><strong>笔记共享</strong>：可以邀请他人协作编辑笔记本，免费版最多邀请15人。</li>
</ul>

<h2>核心功能介绍</h2>

<h3>1. 智能问答（Smart Questions）</h3>
<p>上传资料后，NotebookLM会自动分析内容并提出你可能想问的问题。这些建议问题覆盖了资料的关键要点，你不需要从零开始构思提问。点击任意问题，AI会基于你的资料给出带引用的详细回答，每条回答都会标注来自哪个文件的哪一页。</p>
<p>这个功能特别适合快速了解一份长文档的核心内容。比如你有一份100页的市场调研报告，不需要逐页阅读，NotebookLM会在几秒内总结出关键发现，并回答你最关心的问题。</p>

<h3>2. 播客生成（Audio Overview）</h3>
<p>这是NotebookLM最具辨识度的功能。点击"Generate Audio Overview"按钮，AI会创建一段10-20分钟的播客式对话，由两个AI主持人（一个声音偏成熟稳重，一个偏年轻活泼）围绕你的资料展开讨论。</p>
<p>播客生成完全免费，没有次数限制。你可以在通勤时听播客来消化资料，也可以直接把播客分享给同事或朋友。生成的播客支持下载为MP3文件，也可以直接在Google账户中播放。</p>
<p>值得注意的是，AI主持人的对话不是简单的朗读摘要，而是真正的"讨论"——他们会互相质疑、补充观点、举例子，甚至偶尔开个小玩笑。这种对话式的呈现方式让枯燥的资料变得生动有趣。</p>

<h3>3. 视频解说（Video Overview）</h3>
<p>2025年新增的视频解说功能，将你的资料转化为带有AI主持人的短视频。与播客类似，视频解说也是完全免费的。你可以选择不同风格的主持人和背景，适合用于制作教学视频、产品介绍或知识分享。</p>

<h3>4. 研究摘要（Research Summary）</h3>
<p>NotebookLM可以自动生成结构化的研究摘要，包括关键发现、数据来源、时间线等信息。对于需要撰写论文或报告的研究者来说，这个功能可以节省大量整理资料的时间。</p>

<h3>5. 多语言支持</h3>
<p>NotebookLM支持多种语言的资料输入和输出。你可以上传英文资料，用中文提问，AI会用中文回答。同样，你也可以上传中文资料，用英文提问。这对需要跨语言研究的用户非常有用。</p>

<h2>使用步骤</h2>

<h3>第一步：访问NotebookLM</h3>
<p>打开 <a href="https://notebooklm.google.com">notebooklm.google.com</a>，使用Google账户登录即可开始使用。不需要额外注册，不需要绑定信用卡，不需要订阅任何服务。一个Google账户就是一个完整的NotebookLM账户。</p>

<h3>第二步：创建笔记本</h3>
<p>登录后点击"New Notebook"创建一个新的笔记本。你可以给笔记本起一个名字，比如"2026市场调研"或"毕业论文文献综述"。每个笔记本可以独立管理一组相关文档。</p>

<h3>第三步：上传资料</h3>
<p>在笔记本页面点击"Add source"，可以选择以下上传方式：</p>
<ul>
<li><strong>Google Docs</strong>：从你的Google Drive中选择文档</li>
<li><strong>PDF文件</strong>：直接从电脑上传PDF文件</li>
<li><strong>文本文件</strong>：上传.txt或.md文件</li>
<li><strong>HTML文件</strong>：上传网页保存的HTML文件</li>
<li><strong>复制粘贴</strong>：直接粘贴文本内容</li>
</ul>
<p>最多可以上传50个来源文件。建议按照主题分类，每个笔记本聚焦一个研究课题。</p>

<h3>第四步：提问和探索</h3>
<p>资料上传完成后，你可以：</p>
<ul>
<li>查看系统自动生成的建议问题</li>
<li>输入自己的问题，AI会基于资料回答</li>
<li>点击回答中的引用标记，跳转到原文对应位置</li>
<li>追问细节，AI会记住上下文继续回答</li>
</ul>

<h3>第五步：生成播客或视频</h3>
<p>点击"Audio Overview"或"Video Overview"按钮，选择你喜欢的风格和主持人，AI会在几分钟内生成内容。生成完成后可以直接播放或下载。</p>

<h2>与同类工具的对比</h2>
<table>
<tr><th>功能</th><th>NotebookLM</th><th>Perplexity</th><th>Gemini Advanced</th></tr>
<tr><td>免费使用</td><td>✅ 完全免费</td><td>⚠️ 有限免费</td><td>❌ $19.99/月</td></tr>
<tr><td>最大来源数</td><td>50个/笔记本</td><td>免费版有限</td><td>较多</td></tr>
<tr><td>单文件页数</td><td>500页</td><td>取决于订阅</td><td>取决于订阅</td></tr>
<tr><td>播客生成</td><td>✅ 免费</td><td>❌ 不支持</td><td>❌ 不支持</td></tr>
<tr><td>视频解说</td><td>✅ 免费</td><td>❌ 不支持</td><td>❌ 不支持</td></tr>
<tr><td>引用标注</td><td>✅ 精确到页</td><td>✅ 有来源</td><td>⚠️ 一般</td></tr>
<tr><td>多语言</td><td>✅ 中英互译</td><td>✅ 多语言</td><td>✅ 多语言</td></tr>
<tr><td>协作编辑</td><td>✅ 15人</td><td>❌ 不支持</td><td>⚠️ 有限</td></tr>
</table>

<h2>适用场景</h2>
<p>NotebookLM适合以下使用场景：</p>
<ul>
<li><strong>学术研究</strong>：上传多篇论文文献，让AI帮你梳理研究脉络，生成文献综述摘要</li>
<li><strong>商业分析</strong>：导入市场报告、财务数据、竞品分析，快速提取关键洞察</li>
<li><strong>法律文档</strong>：上传合同、法规、判例，AI会基于原文给出带引用的分析</li>
<li><strong>教学备课</strong>：教师可以将教材和参考资料上传，生成播客作为学生预习材料</li>
<li><strong>新闻调研</strong>：记者可以上传多篇报道，快速生成事件时间线和多方观点对比</li>
<li><strong>个人学习</strong>：学生可以上传课程讲义和参考书，通过问答和播客加深理解</li>
</ul>

<h2>注意事项</h2>
<ul>
<li><strong>隐私考虑</strong>：NotebookLM的数据存储在Google服务器上。虽然Google声称不会用你的数据训练模型，但如果资料涉及敏感信息，建议先脱敏后再上传。</li>
<li><strong>文件格式限制</strong>：不支持Word文档（.docx），需要先转换为PDF或Google Docs格式。扫描件PDF如果文字不可选，需要先做OCR处理。</li>
<li><strong>语言质量</strong>：虽然支持中文，但AI对英文资料的理解和分析质量明显优于中文。如果需要研究中文资料，建议先用翻译工具转为英文后再分析。</li>
<li><strong>网络要求</strong>：NotebookLM需要在Google服务可用的网络环境下使用，国内用户可能需要特殊网络设置。</li>
</ul>

<div class="faq-section">
<h3>❓ 常见问题</h3>
<div class="faq-item"><div class="faq-q">Q: NotebookLM真的完全免费吗？会不会突然收费？</div><div class="faq-a">A: 截至2026年6月，NotebookLM仍然是完全免费的，没有收费计划。Google将其定位为推广Google Workspace生态的工具，短期内没有商业化压力。但作为长期用户，建议关注官方公告。</div></div>
<div class="faq-item"><div class="faq-q">Q: 一个Google账户可以同时创建多少个笔记本？</div><div class="faq-a">A: 目前没有明确的笔记本数量限制。你可以创建多个笔记本，每个笔记本最多50个来源文件。建议按项目或主题分类管理。</div></div>
<div class="faq-item"><div class="faq-q">Q: 生成的播客可以商用吗？</div><div class="faq-a">A: NotebookLM生成的内容版权归Google所有，你可以自由使用和分享。但如果用于商业广播或大规模分发，建议查阅Google的使用条款确认。</div></div>
<div class="faq-item"><div class="faq-q">Q: 可以上传视频或音频文件作为来源吗？</div><div class="faq-a">A: 目前不支持直接上传视频或音频文件。但你可以先用其他工具将视频转为文字稿（如YouTube的自动字幕导出功能），然后将文字稿作为文本文件上传。</div></div>
<div class="faq-item"><div class="faq-q">Q: NotebookLM和Google Gemini有什么区别？</div><div class="faq-a">A: Gemini是通用的AI助手，可以回答各种问题但可能产生幻觉。NotebookLM专注于基于你上传的特定资料回答问题，不会出现编造内容的情况。两者可以配合使用：用NotebookLM做深度研究，用Gemini做泛知识查询。</div></div>
</div>'''

    content_en = '''<h1>NotebookLM Complete Free Guide: Google's AI Research Tool with 50 Sources, Podcast & Video Generation — All Free</h1>
<p>Google's AI research tool NotebookLM, completely free. Upload up to 50 source documents, auto-generate podcast-style conversations, video explanations and research summaries. In 2026, still the only mainstream AI research tool that remains free.</p>

<h2>What is NotebookLM</h2>
<p>NotebookLM is Google's AI research tool launched in late 2023 and made publicly available in 2024. Its core concept is straightforward: feed it your documents, and it reads, summarizes, and generates various content outputs from them. Unlike ChatGPT or Claude where you start from scratch in conversation, NotebookLM's AI responses are strictly grounded in the materials you upload, eliminating the hallucination problem that plagues general-purpose AI assistants.</p>
<p>In 2026, there are many products claiming to be "AI research tools," but most either charge money (Perplexity Pro at $20/month, Gemini Advanced at $19.99/month) or impose strict limits on free users. NotebookLM stands alone as the <strong>only mainstream AI research tool that remains completely free</strong> since its launch — no hidden fees, no VIP tiers, no "free trial then paywall" tactics.</p>

<h2>Free Tier Details</h2>
<p>NotebookLM's free plan has no subscription cost. Here are the specific free usage limits:</p>
<ul>
<li><strong>Up to 50 source files per notebook</strong>: This is the highest free limit among all comparable tools. Perplexity's free tier supports only limited file uploads, while NotebookLM allows you to import up to 50 documents for comprehensive analysis.</li>
<li><strong>Each source file up to 500 pages</strong>: For academic papers, reports, manuals and other common document types, the 500-page limit rarely becomes a bottleneck.</li>
<li><strong>Supported file formats</strong>: PDF, Google Docs, text files (.txt), HTML files, Markdown files. Word documents (.docx) are not directly supported — you need to open them in Google Docs first and save as Google Docs format.</li>
<li><strong>Podcast generation (Audio Overview)</strong>: Completely free with no generation limit. Each generation creates a 10-20 minute conversational podcast where two AI hosts discuss your material. No daily or monthly caps.</li>
<li><strong>Video explanation (Video Overview)</strong>: Added in 2025, free to use. Transforms your materials into short video explanations with AI hosts, suitable for teaching or sharing.</li>
<li><strong>Conversational Q&A</strong>: Unlimited questions. The AI answers based on your uploaded materials with citations. No message limits on the free tier.</li>
<li><strong>Notebook sharing</strong>: Invite others to collaborate on notebooks — up to 15 collaborators per notebook on the free plan.</li>
</ul>

<h2>Core Features</h2>

<h3>1. Smart Questions</h3>
<p>After uploading materials, NotebookLM automatically analyzes the content and suggests questions you might want to ask. These suggested questions cover the key points of your material, so you don't need to start from scratch. Click any question, and the AI provides a detailed answer with citations pulled directly from your documents.</p>
<p>This feature is particularly useful for quickly understanding the core content of a long document. For example, if you have a 100-page market research report, you don't need to read it page by page. NotebookLM summarizes the key findings in seconds and answers your most pressing questions.</p>

<h3>2. Podcast Generation (Audio Overview)</h3>
<p>This is NotebookLM's most distinctive feature. Click "Generate Audio Overview," and the AI creates a 10-20 minute podcast-style conversation between two AI hosts — one with a mature, steady voice, the other younger and more energetic — discussing your materials.</p>
<p>Podcast generation is completely free with no usage limits. You can listen during your commute to digest the material, or share the podcast directly with colleagues or friends. Generated podcasts can be downloaded as MP3 files or played directly in your Google account.</p>
<p>Notably, the AI hosts don't simply read summaries aloud — they actually <em>discuss</em>. They challenge each other's points, add context, give examples, and occasionally make light jokes. This conversational presentation makes dry material engaging and easy to absorb.</p>

<h3>3. Video Explanation (Video Overview)</h3>
<p>The video explanation feature added in 2025 transforms your materials into short videos with AI hosts. Like the podcast feature, video generation is completely free. You can choose different host styles and backgrounds, making it ideal for creating educational videos, product introductions, or knowledge-sharing content.</p>

<h3>4. Research Summary</h3>
<p>NotebookLM can automatically generate structured research summaries, including key findings, data sources, timelines and more. For researchers writing papers or reports, this feature saves significant time in organizing materials.</p>

<h3>5. Multi-language Support</h3>
<p>NotebookLM supports materials in multiple languages. You can upload English documents and ask questions in Chinese, with the AI responding in Chinese. The reverse also works. This cross-language capability is invaluable for users conducting international research.</p>

<h2>Step-by-Step Usage Guide</h2>

<h3>Step 1: Access NotebookLM</h3>
<p>Go to <a href="https://notebooklm.google.com">notebooklm.google.com</a> and sign in with your Google account. That's it — no additional registration, no credit card required, no subscription needed. One Google account gives you full access to NotebookLM.</p>

<h3>Step 2: Create a Notebook</h3>
<p>Click "New Notebook" after logging in. Name it something meaningful, like "2026 Market Research" or "Thesis Literature Review." Each notebook manages a related set of documents independently.</p>

<h3>Step 3: Upload Sources</h3>
<p>On the notebook page, click "Add source" to choose from these upload options:</p>
<ul>
<li><strong>Google Docs</strong>: Select documents from your Google Drive</li>
<li><strong>PDF files</strong>: Upload PDFs directly from your computer</li>
<li><strong>Text files</strong>: Upload .txt or .md files</li>
<li><strong>HTML files</strong>: Upload saved webpage HTML files</li>
<li><strong>Copy &amp; paste</strong>: Paste text content directly</li>
</ul>
<p>You can upload up to 50 sources. Organize by topic — each notebook should focus on one research question.</p>

<h3>Step 4: Ask Questions and Explore</h3>
<p>After uploading, you can:</p>
<ul>
<li>Review AI-generated suggested questions</li>
<li>Type your own questions — the AI answers based on your materials</li>
<li>Click citation markers in answers to jump to the exact location in the source</li>
<li>Follow up with deeper questions — the AI remembers context</li>
</ul>

<h3>Step 5: Generate Podcast or Video</h3>
<p>Click "Audio Overview" or "Video Overview," select your preferred style and host, and the AI generates content within minutes. Once ready, play directly or download.</p>

<h2>Comparison with Similar Tools</h2>
<table>
<tr><th>Feature</th><th>NotebookLM</th><th>Perplexity</th><th>Gemini Advanced</th></tr>
<tr><td>Free access</td><td>✅ Completely free</td><td>⚠️ Limited free</td><td>❌ $19.99/month</td></tr>
<tr><td>Max sources</td><td>50 per notebook</td><td>Limited on free</td><td>More (paid)</td></tr>
<tr><td>Pages per file</td><td>500 pages</td><td>Depends on plan</td><td>Depends on plan</td></tr>
<tr><td>Podcast generation</td><td>✅ Free</td><td>❌ Not supported</td><td>❌ Not supported</td></tr>
<tr><td>Video explanation</td><td>✅ Free</td><td>❌ Not supported</td><td>❌ Not supported</td></tr>
<tr><td>Citation tracking</td><td>✅ Precise to page</td><td>✅ Has sources</td><td>⚠️ Basic</td></tr>
<tr><td>Multi-language</td><td>✅ Cross-language</td><td>✅ Multi-language</td><td>✅ Multi-language</td></tr>
<tr><td>Collaboration</td><td>✅ Up to 15 people</td><td>❌ Not supported</td><td>⚠️ Limited</td></tr>
</table>

<h2>Best Use Cases</h2>
<p>NotebookLM is ideal for these scenarios:</p>
<ul>
<li><strong>Academic research</strong>: Upload multiple research papers, let AI map the literature landscape and generate summary reviews</li>
<li><strong>Business analysis</strong>: Import market reports, financial data, competitive analyses — extract key insights in minutes</li>
<li><strong>Legal documents</strong>: Upload contracts, regulations, case law — AI provides cited analysis based on originals</li>
<li><strong>Teaching preparation</strong>: Teachers can upload textbooks and reference materials, generating podcasts as student prep materials</li>
<li><strong>Journalism research</strong>: Reporters can upload multiple articles to quickly generate event timelines and multi-perspective comparisons</li>
<li><strong>Personal learning</strong>: Students can upload lecture notes and reference books, deepen understanding through Q&amp;A and podcasts</li>
</ul>

<h2>Important Notes</h2>
<ul>
<li><strong>Privacy considerations</strong>: NotebookLM stores data on Google servers. While Google states it won't use your data to train models, if your materials contain sensitive information, consider anonymizing before uploading.</li>
<li><strong>Format limitations</strong>: Word documents (.docx) are not directly supported — convert to PDF or Google Docs first. Scanned PDFs with non-selectable text need OCR processing before upload.</li>
<li><strong>Language quality</strong>: While Chinese is supported, the AI's comprehension and analysis quality is noticeably better for English materials. For Chinese research, consider translating to English first for higher-quality analysis.</li>
<li><strong>Network requirements</strong>: NotebookLM requires access to Google services. Users in mainland China may need special network configurations.</li>
</ul>

<div class="faq-section">
<h3>❓ Frequently Asked Questions</h3>
<div class="faq-item"><div class="faq-q">Q: Is NotebookLM really completely free? Will it charge in the future?</div><div class="faq-a">A: As of June 2026, NotebookLM remains entirely free with no announced plans to charge. Google positions it as a tool to promote the Google Workspace ecosystem, with little near-term commercial pressure. However, monitor official announcements for any changes.</div></div>
<div class="faq-item"><div class="faq-q">Q: How many notebooks can one Google account create?</div><div class="faq-a">A: There is currently no explicit limit on the number of notebooks. You can create multiple notebooks, each with up to 50 source files. Organize by project or topic for best results.</div></div>
<div class="faq-item"><div class="faq-q">Q: Can I use generated podcasts commercially?</div><div class="faq-a">A: Content generated by NotebookLM is owned by Google, and you are free to use and share it. For commercial broadcasting or large-scale distribution, review Google's Terms of Service to confirm compliance.</div></div>
<div class="faq-item"><div class="faq-q">Q: Can I upload video or audio files as sources?</div><div class="faq-a">A: Direct video or audio upload is not currently supported. However, you can use other tools to transcribe video to text (e.g., YouTube's auto-caption export feature) and upload the transcript as a text file.</div></div>
<div class="faq-item"><div class="faq-q">Q: How does NotebookLM differ from Google Gemini?</div><div class="faq-a">A: Gemini is a general-purpose AI assistant that can answer broad questions but may hallucinate. NotebookLM focuses exclusively on answering questions based on your uploaded materials, eliminating fabricated content. Use them together: NotebookLM for deep research, Gemini for general knowledge queries.</div></div>
</div>'''

    faq_zh = '''{"@type": "Question", "name": "NotebookLM真的完全免费吗？会不会突然收费？", "acceptedAnswer": {"@type": "Answer", "text": "截至2026年6月，NotebookLM仍然是完全免费的，没有收费计划。Google将其定位为推广Google Workspace生态的工具，短期内没有商业化压力。"}}'''
    
    faq_en = '''{"@type": "Question", "name": "Is NotebookLM really completely free? Will it charge in the future?", "acceptedAnswer": {"@type": "Answer", "text": "As of June 2026, NotebookLM remains entirely free with no announced plans to charge. Google positions it as a tool to promote the Google Workspace ecosystem."}}'''

    # Write HTML files
    zh_html, en_html = generate_guide_html(
        slug, title_zh, title_en, description_zh, description_en,
        content_zh, content_en, faq_zh, faq_en, today
    )
    
    os.makedirs('/home/ubuntu/aifreeplan/zh/guides', exist_ok=True)
    os.makedirs('/home/ubuntu/aifreeplan/en/guides', exist_ok=True)
    
    with open(f'/home/ubuntu/aifreeplan/zh/guides/{slug}.html', 'w', encoding='utf-8') as f:
        f.write(zh_html)
    
    with open(f'/home/ubuntu/aifreeplan/en/guides/{slug}.html', 'w', encoding='utf-8') as f:
        f.write(en_html)
    
    print(f"✅ Generated guide: {slug}")
    print(f"  Title (ZH): {title_zh}")
    print(f"  Title (EN): {title_en}")
    print(f"  Date: {today}")
    
    # Quality check
    zh_content_len = len(content_zh)
    en_content_len = len(content_en)
    zh_chinese = count_chinese_chars(content_zh)
    en_chinese = count_chinese_chars(content_en)
    
    print(f"  Content length (ZH): {zh_content_len} chars")
    print(f"  Content length (EN): {en_content_len} chars")
    print(f"  Chinese chars in ZH content: {zh_chinese}")
    print(f"  Chinese chars in EN content: {en_chinese}")
    
    # Validate quality
    issues = []
    if zh_content_len < 1000:
        issues.append(f"ZH content too short: {zh_content_len} chars (need >1000)")
    if en_content_len < 1000:
        issues.append(f"EN content too short: {en_content_len} chars (need >1000)")
    if en_chinese > 0:
        en_total = len(content_en)
        en_chinese_pct = en_chinese / en_total * 100
        if en_chinese_pct > 5:
            issues.append(f"EN content has {en_chinese_pct:.1f}% Chinese chars (need <5%)")
    
    if issues:
        print(f"\n⚠️ Quality issues found:")
        for issue in issues:
            print(f"  - {issue}")
        return False
    else:
        print(f"\n✅ Quality check passed!")
        return True


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
