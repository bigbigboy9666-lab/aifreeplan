#!/usr/bin/env python3
"""
AIFreePlan 统一页面模板系统
所有页面必须用这个模板生成，禁止裸写HTML
"""

# 基础HTML模板
BASE_TEMPLATE = '''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} - AIFreePlan</title>
<meta name="description" content="{description}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<meta name="theme-color" content="#6366F1">
<link rel="canonical" href="https://aifreeplan.com{canonical_path}">
<link rel="alternate" hreflang="zh" href="https://aifreeplan.com{zh_path}">
<link rel="alternate" hreflang="en" href="https://aifreeplan.com{en_path}">
<link rel="alternate" hreflang="x-default" href="https://aifreeplan.com{default_path}">
{extra_head}
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{
  --bg:#F8FAFC;--bg-white:#fff;--border:#E2E8F0;--border-light:#F1F5F9;
  --text:#1E1B4B;--text-secondary:#64748B;--text-muted:#94A3B8;
  --accent:#6366F1;--accent-hover:#4F46E5;--accent-light:rgba(99,102,241,.1);
  --green:#059669;--green-light:rgba(5,150,105,.1);
  --shadow:0 4px 20px rgba(0,0,0,.05);--shadow-hover:0 8px 32px rgba(0,0,0,.1);
  --radius:12px;--radius-lg:16px;
}}
body{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Noto Sans SC","PingFang SC","Microsoft YaHei",sans-serif;background:var(--bg);color:var(--text);line-height:1.6;-webkit-font-smoothing:antialiased}}
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
.btn-primary:hover{{background:var(--accent-hover);transform:translateY(-1px)}}
.footer{{background:#1a1a2e;padding:50px 0 30px;color:#fff}}
.footer-inner{{display:flex;justify-content:space-between;gap:60px;flex-wrap:wrap}}
.footer-brand{{max-width:300px}}
.footer-brand .logo{{color:var(--green);margin-bottom:8px;display:inline-block}}
.footer-brand p{{font-size:14px;color:rgba(255,255,255,.6);line-height:1.5}}
.footer-links{{display:flex;gap:60px}}
.footer-col{{display:flex;flex-direction:column;gap:10px}}
.footer-col h4{{font-size:14px;font-weight:700;margin-bottom:4px;color:#fff}}
.footer-col a{{color:rgba(255,255,255,.6);text-decoration:none;font-size:14px;transition:color .2s}}
.footer-col a:hover{{color:#fff}}
.footer-bottom{{margin-top:30px;padding-top:20px;border-top:1px solid rgba(255,255,255,.1);font-size:13px;color:rgba(255,255,255,.4)}}
@media(max-width:768px){{
  .container{{padding:0 20px}}
  .nav{{display:none}}
  .footer-inner{{flex-direction:column;gap:30px}}
  .footer-links{{gap:30px}}
}}
{custom_css}
</style>
</head>
<body>

<header class="header">
  <div class="container header-inner">
    <a href="/{lang}" class="logo">AI<span class="accent">FreePlan</span></a>
    <nav class="nav">
      <a href="/{lang}/all">{all_tools_text}</a>
      <a href="/{lang}/guides">{guides_text}</a>
      <a href="/{lang}/privacy">{privacy_text}</a>
      <a href="{lang_switch_path}" class="btn btn-primary">{lang_switch_text}</a>
    </nav>
  </div>
</header>

<main{main_attrs}>
{content}
</main>

<footer class="footer">
  <div class="container">
    <div class="footer-inner">
      <div class="footer-brand">
        <a href="/{lang}" class="logo">AI<span class="accent" style="color:var(--green)">FreePlan</span></a>
        <p>{footer_desc}</p>
      </div>
      <div class="footer-links">
        <div class="footer-col">
          <h4>{product_text}</h4>
          <a href="/{lang}/all">{all_tools_text}</a>
          <a href="/{lang}/guides">{guides_text}</a>
        </div>
        <div class="footer-col">
          <h4>{legal_text}</h4>
          <a href="/{lang}/privacy">{privacy_text}</a>
          <a href="/{lang}/terms">{terms_text}</a>
        </div>
      </div>
    </div>
    <div class="footer-bottom">© 2026 AIFreePlan. {rights_text}</div>
  </div>
</footer>

{extra_scripts}
</body>
</html>'''

# 中英文文本
TEXTS = {
    'zh': {
        'all_tools_text': '全部工具',
        'guides_text': '攻略',
        'privacy_text': '隐私政策',
        'terms_text': '用户条款',
        'footer_desc': 'AI驱动的免费工具聚合平台，永久免费。',
        'product_text': '产品',
        'legal_text': '法律',
        'rights_text': '保留所有权利。',
    },
    'en': {
        'all_tools_text': 'All Tools',
        'guides_text': 'Guides',
        'privacy_text': 'Privacy',
        'terms_text': 'Terms',
        'footer_desc': 'AI-powered free tools directory. Free forever.',
        'product_text': 'Product',
        'legal_text': 'Legal',
        'rights_text': 'All rights reserved.',
    }
}

def get_lang_switch(lang, current_path):
    """获取语言切换路径"""
    if lang == 'zh':
        en_path = current_path.replace('/zh/', '/en/')
        return en_path, 'English'
    else:
        zh_path = current_path.replace('/en/', '/zh/')
        return zh_path, '中文'

def build_page(lang, content, title, description, canonical_path, 
               custom_css='', extra_head='', extra_scripts='', main_attrs=' class="container" style="padding-top:40px;padding-bottom:80px"'):
    """构建完整页面"""
    
    is_zh = lang == 'zh'
    texts = TEXTS[lang]
    
    # 计算语言切换路径
    zh_path = canonical_path if is_zh else canonical_path.replace('/en/', '/zh/')
    en_path = canonical_path.replace('/zh/', '/en/') if is_zh else canonical_path
    lang_switch_path, lang_switch_text = get_lang_switch(lang, canonical_path)
    
    return BASE_TEMPLATE.format(
        lang=lang,
        title=title,
        description=description,
        canonical_path=canonical_path,
        zh_path=zh_path,
        en_path=en_path,
        default_path=en_path,
        extra_head=extra_head,
        custom_css=custom_css,
        main_attrs=main_attrs,
        content=content,
        extra_scripts=extra_scripts,
        **texts,
        lang_switch_path=lang_switch_path,
        lang_switch_text=lang_switch_text,
    )

def validate_page(html_content):
    """验证页面是否符合标准"""
    errors = []
    
    if '<!DOCTYPE html>' not in html_content[:100]:
        errors.append('Missing DOCTYPE')
    
    if 'lang="' not in html_content[:200]:
        errors.append('Missing lang attribute')
    
    if 'charset=' not in html_content[:500]:
        errors.append('Missing charset')
    
    if 'viewport' not in html_content[:1000]:
        errors.append('Missing viewport')
    
    if '<title>' not in html_content:
        errors.append('Missing title')
    
    if '<meta name="description"' not in html_content:
        errors.append('Missing description')
    
    if 'hreflang' not in html_content:
        errors.append('Missing hreflang')
    
    return errors

# 测试
if __name__ == '__main__':
    # 测试生成一个页面
    test_html = build_page(
        lang='zh',
        content='<h1>测试页面</h1>',
        title='测试',
        description='这是一个测试页面',
        canonical_path='/zh/test'
    )
    
    errors = validate_page(test_html)
    if errors:
        print(f"❌ 验证失败: {errors}")
    else:
        print("✅ 模板验证通过")
