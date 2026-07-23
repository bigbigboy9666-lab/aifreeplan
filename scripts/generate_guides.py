import json
import os
from datetime import datetime

# 读取工具数据
with open('/home/ubuntu/aifreeplan/public/data/tools.json', 'r') as f:
    tools_data = json.load(f)
tools = {t['id']: t for t in tools_data['tools']}

# 读取攻略数据
with open('/home/ubuntu/aifreeplan/public/data/guides.json', 'r') as f:
    guides_data = json.load(f)

BASE = '/home/ubuntu/aifreeplan'
GUIDES_ZH = os.path.join(BASE, 'zh', 'guides')
GUIDES_EN = os.path.join(BASE, 'en', 'guides')
ARTICLES = os.path.join(BASE, 'data', 'articles')

os.makedirs(GUIDES_ZH, exist_ok=True)
os.makedirs(GUIDES_EN, exist_ok=True)
os.makedirs(ARTICLES, exist_ok=True)

def make_guide(slug, title_zh, title_en, desc_zh, desc_en, h1_zh, h1_en,
               intro_zh, intro_en, sections_zh, sections_en, faqs_zh, faqs_en,
               images_zh, images_en, category, date_str=None):
    """生成一篇中英文攻略"""
    if date_str is None:
        date_str = datetime.now().strftime('%Y-%m-%d')
    
    date_cn = datetime.strptime(date_str, '%Y-%m-%d').strftime('%Y年%-m月%-d日')
    
    # 生成FAQ HTML
    faq_html_zh = '\n'.join([
        f'<details class="faq-item"><summary>{q}</summary><p>{a}</p></details>'
        for q, a in faqs_zh
    ])
    faq_html_en = '\n'.join([
        f'<details class="faq-item"><summary>{q}</summary><p>{a}</p></details>'
        for q, a in faqs_en
    ])
    
    cta_zh = '<a href="https://aifreeplan.com/zh/tools/{tool_id}" target="_blank">前往工具页 →</a>'.format(tool_id=slug.split('-')[0][:10])
    cta_en = '<a href="https://aifreeplan.com/en/tools/{tool_id}" target="_blank">Go to Tool Page →</a>'.format(tool_id=slug.split('-')[0][:10])
    
    # 生成FAQ JSON-LD
    faq_schema_zh = json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs_zh]
    }, ensure_ascii=False, indent=2)
    faq_schema_en = json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs_en]
    }, ensure_ascii=False, indent=2)
    
    # 生成sections HTML
    sections_html_zh = ''.join([f'<h2>{h}</h2>\n{s}' for h, s in sections_zh])
    sections_html_en = ''.join([f'<h2>{h}</h2>\n{s}' for h, s in sections_en])
    
    # 生成images HTML
    images_html_zh = '\n'.join([f'<img src="/data/articles/{src}" alt="{alt}" loading="lazy" decoding="async" style="width:100%;border-radius:12px;margin:24px 0">' for src, alt in images_zh])
    images_html_en = '\n'.join([f'<img src="/data/articles/{src}" alt="{alt}" loading="lazy" decoding="async" style="width:100%;border-radius:12px;margin:24px 0">' for src, alt in images_en])
    
    # 构建完整HTML
    html_zh = f'''<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_zh} | AIFreePlan</title>
<meta name="description" content="{desc_zh}">
<link rel="canonical" href="https://aifreeplan.com/zh/guides/{slug}">
<link rel="alternate" hreflang="zh" href="https://aifreeplan.com/zh/guides/{slug}">
<link rel="alternate" hreflang="en" href="https://aifreeplan.com/en/guides/{slug}">
<link rel="alternate" hreflang="x-default" href="https://aifreeplan.com/en/guides/{slug}">
<meta property="og:type" content="article">
<meta property="og:title" content="{title_zh}">
<meta property="og:description" content="{desc_zh}">
<meta property="og:url" content="https://aifreeplan.com/zh/guides/{slug}">
<meta property="og:site_name" content="AI Free Plan">
<meta property="og:locale" content="zh_CN">
<meta property="article:published_time" content="{date_str}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title_zh}">
<meta name="twitter:description" content="{desc_zh}">
<script type="application/ld+json">
{json.dumps({
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": h1_zh,
    "description": desc_zh,
    "url": f"https://aifreeplan.com/zh/guides/{slug}",
    "datePublished": date_str,
    "dateModified": date_str,
    "author": {"@type": "Organization", "name": "AIFreePlan"},
    "publisher": {"@type": "Organization", "name": "AIFreePlan", "url": "https://aifreeplan.com"},
    "mainEntityOfPage": {"@type": "WebPage", "@id": f"https://aifreeplan.com/zh/guides/{slug}"}
}, ensure_ascii=False, indent=2)}
</script>
<script type="application/ld+json">
{json.dumps({
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "首页", "item": "https://aifreeplan.com/zh"},
        {"@type": "ListItem", "position": 2, "name": "攻略", "item": "https://aifreeplan.com/zh/guides"},
        {"@type": "ListItem", "position": 3, "name": h1_zh, "item": f"https://aifreeplan.com/zh/guides/{slug}"}
    ]
}, ensure_ascii=False, indent=2)}
</script>
<script type="application/ld+json">
{faq_schema_zh}
</script>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif; background: #f9fafb; color: #1f2937; line-height: 1.7; }}
.header {{ background: #fff; border-bottom: 1px solid #e5e7eb; padding: 12px 0; position: sticky; top: 0; z-index: 50; }}
.header-inner {{ max-width: 800px; margin: 0 auto; padding: 0 20px; display: flex; align-items: center; justify-content: space-between; }}
.header-logo {{ font-size: 20px; font-weight: bold; color: #10b981; text-decoration: none; }}
.header-nav a {{ margin-left: 20px; color: #6b7280; text-decoration: none; font-size: 14px; }}
.header-nav a:hover {{ color: #10b981; }}
.container {{ max-width: 800px; margin: 0 auto; padding: 40px 20px; }}
.breadcrumb {{ font-size: 13px; color: #9ca3af; margin-bottom: 24px; }}
.breadcrumb a {{ color: #6b7280; text-decoration: none; }}
.breadcrumb a:hover {{ color: #10b981; }}
h1 {{ font-size: 32px; font-weight: 700; margin-bottom: 12px; line-height: 1.3; color: #111827; }}
.date {{ font-size: 14px; color: #9ca3af; margin-bottom: 24px; }}
.intro {{ font-size: 16px; color: #4b5563; margin-bottom: 32px; line-height: 1.8; }}
h2 {{ font-size: 24px; font-weight: 600; margin: 32px 0 16px; color: #111827; }}
h3 {{ font-size: 18px; font-weight: 600; margin: 24px 0 12px; color: #374151; }}
p {{ margin-bottom: 16px; }}
ul, ol {{ margin: 16px 0; padding-left: 24px; }}
li {{ margin-bottom: 8px; }}
table {{ width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 14px; }}
th, td {{ border: 1px solid #e5e7eb; padding: 10px 12px; text-align: left; }}
th {{ background: #f3f4f6; font-weight: 600; }}
.faq-item {{ margin-bottom: 16px; border: 1px solid #e5e7eb; border-radius: 8px; overflow: hidden; }}
.faq-item summary {{ padding: 14px 16px; background: #f9fafb; cursor: pointer; font-weight: 600; list-style: none; }}
.faq-item summary::-webkit-details-marker {{ display: none; }}
.faq-item summary::before {{ content: "+ "; color: #10b981; font-weight: bold; }}
.faq-item[open] summary::before {{ content: "- "; }}
.faq-item p {{ padding: 0 16px 14px; color: #4b5563; }}
.cta-box {{ background: linear-gradient(135deg, #ecfdf5, #d1fae5); border-radius: 12px; padding: 24px; margin: 32px 0; text-align: center; }}
.cta-box a {{ display: inline-block; background: #10b981; color: #fff; padding: 12px 32px; border-radius: 8px; text-decoration: none; font-weight: 600; margin-top: 12px; }}
.cta-box a:hover {{ background: #059669; }}
.footer {{ text-align: center; padding: 32px 20px; color: #9ca3af; font-size: 13px; border-top: 1px solid #e5e7eb; margin-top: 48px; }}
</style>
</head>
<body>
<header class="header">
<div class="header-inner">
<a href="/zh" class="header-logo">&#129302; AI Free Plan</a>
<nav class="header-nav">
<a href="/zh">首页</a>
<a href="/zh/guides">攻略</a>
<a href="/zh/tools">工具</a>
<a href="/en">English</a>
</nav>
</div>
</header>
<main class="container">
<div class="breadcrumb">
<a href="/zh">首页</a> / <a href="/zh/guides">攻略</a> / {h1_zh}
</div>
<h1>{h1_zh}</h1>
<p class="date">更新时间：{date_cn}</p>
<p>{intro_zh}</p>
{images_html_zh}
{sections_html_zh}
<div class="faq-section">
<h2>常见问题</h2>
{faq_html_zh}
</div>
<div class="cta-box">
<p><strong>想直接试用？</strong></p>
{cta_zh}
</div>
</main>
<footer class="footer">
<p>&copy; 2026 AI Free Plan. 免费AI工具大全，每日更新。</p>
</footer>
</body>
</html>'''
    
    html_en = html_zh.replace('/zh/', '/en/').replace('lang="zh"', 'lang="en"')
    
    # 替换英文内容
    html_en = html_en.replace(f'<h1>{h1_zh}</h1>', f'<h1>{h1_en}</h1>')
    html_en = html_en.replace(f'<p class="date">更新时间：{date_cn}</p>', f'<p class="date">Last updated: {date_str}</p>')
    html_en = html_en.replace(intro_zh, intro_en)
    html_en = html_en.replace(images_html_zh, images_html_en)
    html_en = html_en.replace(sections_html_zh, sections_html_en)
    html_en = html_en.replace(f'<h2>常见问题</h2>', f'<h2>Frequently Asked Questions</h2>')
    html_en = html_en.replace(faq_html_zh, faq_html_en)
    html_en = html_en.replace(cta_zh, cta_en)
    
    # 更新meta
    html_en = html_en.replace(f'<title>{title_zh} | AIFreePlan</title>', f'<title>{title_en} | AIFreePlan</title>')
    html_en = html_en.replace(f'<meta name="description" content="{desc_zh}">', f'<meta name="description" content="{desc_en}">')
    html_en = html_en.replace(f'<meta property="og:title" content="{title_zh}">', f'<meta property="og:title" content="{title_en}">')
    html_en = html_en.replace(f'<meta property="og:description" content="{desc_zh}">', f'<meta property="og:description" content="{desc_en}">')
    html_en = html_en.replace('zh_CN', 'en_US')
    
    # 更新JSON-LD
    html_en = html_en.replace(faq_schema_zh, faq_schema_en)
    
    # 写文件
    zh_path = os.path.join(GUIDES_ZH, f'{slug}.html')
    en_path = os.path.join(GUIDES_EN, f'{slug}.html')
    
    with open(zh_path, 'w', encoding='utf-8') as f:
        f.write(html_zh)
    with open(en_path, 'w', encoding='utf-8') as f:
        f.write(html_en)
    
    print(f"✓ 生成: {zh_path}")
    print(f"✓ 生成: {en_path}")
    return zh_path, en_path


# ============================================================
# 攻略1: Seedance 2.0 完全免费攻略
# ============================================================
make_guide(
    slug='seedance-2.0-free-unlimited-2026',
    title_zh='Seedance 2.0免费攻略：1080p无限视频生成，目前最强免费AI视频工具',
    title_en='Seedance 2.0 Free Guide: Unlimited 1080p AI Video Generation in 2026',
    desc_zh='Seedance 2.0是目前唯一真正免费无限使用的AI视频生成工具，1080p分辨率无水印，支持上传人脸。手把手教你通过小云雀平台免费使用满血版。',
    desc_en='Seedance 2.0 is the only AI video generator that\'s truly free and unlimited with 1080p resolution, no watermark, and face upload support. Step-by-step guide to use the full version via Xiaoyunque platform.',
    h1_zh='Seedance 2.0免费攻略：1080p无限视频生成，目前最强免费AI视频工具',
    h1_en='Seedance 2.0 Free Guide: Unlimited 1080p AI Video Generation',
    intro_zh='说实话，2026年做AI视频生成，Seedance 2.0是目前唯一一个让你不用掏钱还能拿到1080p无水印视频的工具。字节跳动旗下的小云雀平台放的这个版本是满血版，不排队、不限次数、不加水印，这在AI视频圈子里几乎是闻所未闻的。',
    intro_en='Seedance 2.0 is currently the only AI video generation tool that\'s truly free, unlimited, and produces 1080p watermark-free videos. The full version is available through ByteDance\'s Xiaoyunque platform with no queues, no limits, and no watermarks.',
    sections_zh=[
        ('免费额度到底有多少', '''
<p>Seedance 2.0的免费政策在AI视频工具里属于"不讲武德"级别：</p>
<ul>
<li><strong>免费额度：</strong>无限次生成，没有每日或每月限制</li>
<li><strong>分辨率：</strong>最高1080p，比大多数付费工具都高</li>
<li><strong>水印：</strong>无水印，生成的视频可以直接商用</li>
<li><strong>排队：</strong>不排队，即时生成</li>
<li><strong>特色功能：</strong>支持上传人脸进行视频生成，这是很多付费工具都不提供的</li>
<li><strong>模型版本：</strong>Seedance 2.0满血版，不是阉割版</li>
</ul>
<p>对比一下其他工具就知道这意味着什么了。可灵AI每天给66个积分，海螺AI也是66个积分，Runway每月只有125个积分，Pika每天10次。Seedance 2.0不限制次数，这点在同类工具里是独一份。</p>
'''),
        ('怎么注册和使用', '''
<p>使用Seedance 2.0非常简单，不需要翻墙，不需要信用卡：</p>
<ol>
<li><strong>打开小云雀平台：</strong>访问小云雀的官方网站或APP（在应用商店搜索"小云雀"即可下载）</li>
<li><strong>注册账号：</strong>用微信或手机号注册，不需要邮箱验证</li>
<li><strong>进入Seedance 2.0：</strong>在工具列表中找到"Seedance 2.0"或"视频生成"</li>
<li><strong>输入提示词：</strong>用中文或英文描述你想要的视频内容，越详细越好</li>
<li><strong>选择参数：</strong>分辨率选1080p，时长选最长选项</li>
<li><strong>生成视频：</strong>点击生成，一般几十秒到几分钟就能出结果</li>
<li><strong>下载保存：</strong>生成完成后直接下载，无水印</li>
</ol>
<p>整个过程不超过5分钟，比注册一个Midjourney账号还简单。</p>
'''),
        ('真实使用场景', '''
<p>Seedance 2.0适合哪些人用？我见过几个比较典型的场景：</p>
<p><strong>短视频创作者：</strong>一个做抖音的博主，每天需要生成3-5条短视频素材。用Seedance 2.0免费生成，不用花钱买其他工具，一个月省了几百块。</p>
<p><strong>自媒体运营：</strong>做公众号和小红书的运营人员，需要用AI生成一些视频配图。Seedance 2.0的1080p分辨率直接够用，不需要后期处理。</p>
<p><strong>个人兴趣：</strong>随便玩玩，输入一段描述生成个小视频，发朋友圈或者B站。完全免费，试错成本为零。</p>
'''),
        ('和其他AI视频工具对比', '''
<table>
<thead>
<tr><th>对比项</th><th>Seedance 2.0</th><th>可灵AI</th><th>海螺AI</th><th>Runway</th></tr>
</thead>
<tbody>
<tr><td>免费额度</td><td>无限次</td><td>66积分/天</td><td>66积分/天</td><td>125积分/月</td></tr>
<tr><td>最高分辨率</td><td>1080p</td><td>1080p</td><td>720p-1080p</td><td>720p</td></tr>
<tr><td>水印</td><td>无</td><td>有</td><td>有</td><td>有</td></tr>
<tr><td>排队</td><td>不排队</td><td>有时排队</td><td>有时排队</td><td>排队</td></tr>
<tr><td>上传人脸</td><td>支持</td><td>支持</td><td>不支持</td><td>不支持</td></tr>
<tr><td>商用权限</td><td>可以</td><td>不可以</td><td>不可以</td><td>付费才行</td></tr>
<tr><td>月费用(付费)</td><td>免费</td><td>¥30/月起</td><td>$9.99/月起</td><td>$15/月起</td></tr>
</tbody>
</table>
<p>从表里可以看出，Seedance 2.0在免费额度、分辨率、水印、排队这几个关键指标上全面领先。唯一的短板是知名度不如Runway和可灵，但实际体验差距不大。</p>
'''),
    ],
    sections_en=[
        ('How Much Is Free', '''
<p>Seedance 2.0's free policy is unheard of in the AI video generation space:</p>
<ul>
<li><strong>Free credits:</strong> Unlimited generations, no daily or monthly limits</li>
<li><strong>Resolution:</strong> Up to 1080p, higher than most paid tools</li>
<li><strong>Watermark:</strong> No watermark, videos can be used commercially</li>
<li><strong>Queue:</strong> No queue, instant generation</li>
<li><strong>Special features:</strong> Supports face upload for video generation</li>
<li><strong>Model version:</strong> Full Seedance 2.0, not a watered-down version</li>
</ul>
<p>Compare this to Kling AI (66 credits/day), Hailuo (66 credits/day), and Runway (125 credits/month). Seedance 2.0 is in a league of its own.</p>
'''),
        ('How to Register and Use', '''
<p>Using Seedance 2.0 is straightforward:</p>
<ol>
<li><strong>Open Xiaoyunque platform:</strong> Search "小云雀" in your app store or visit their website</li>
<li><strong>Register:</strong> Sign up with WeChat or phone number, no email verification needed</li>
<li><strong>Find Seedance 2.0:</strong> Look for "Seedance 2.0" or "Video Generation" in the tools list</li>
<li><strong>Enter prompt:</strong> Describe the video you want in Chinese or English</li>
<li><strong>Set parameters:</strong> Choose 1080p resolution and maximum duration</li>
<li><strong>Generate:</strong> Click generate, usually ready in under a minute</li>
<li><strong>Download:</strong> Download directly, no watermark</li>
</ol>
'''),
        ('Real Use Cases', '''
<p><strong>Short video creators:</strong> A Douyin creator who needs 3-5 video clips daily. Using Seedance 2.0 for free saves hundreds of yuan per month compared to paid alternatives.</p>
<p><strong>Social media managers:</strong> 1080p resolution is sufficient for WeChat Official Accounts and Xiaohongshu without post-processing.</p>
<p><strong>Hobbyists:</strong> Try it out with zero cost. Generate a fun video and share it on Bilibili or Moments.</p>
'''),
        ('Comparison with Other AI Video Tools', '''
<table>
<thead>
<tr><th>Feature</th><th>Seedance 2.0</th><th>Kling AI</th><th>Hailuo</th><th>Runway</th></tr>
</thead>
<tbody>
<tr><td>Free allowance</td><td>Unlimited</td><td>66 credits/day</td><td>66 credits/day</td><td>125 credits/month</td></tr>
<tr><td>Max resolution</td><td>1080p</td><td>1080p</td><td>720p-1080p</td><td>720p</td></tr>
<tr><td>Watermark</td><td>None</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Queue</td><td>No</td><td>Sometimes</td><td>Sometimes</td><td>Yes</td></tr>
<tr><td>Face upload</td><td>Supported</td><td>Supported</td><td>No</td><td>No</td></tr>
<tr><td>Commercial use</td><td>Yes</td><td>No</td><td>No</td><td>Paid only</td></tr>
<tr><td>Monthly cost</td><td>Free</td><td>¥30+/mo</td><td>$9.99+/mo</td><td>$15+/mo</td></tr>
</tbody>
</table>
'''),
    ],
    faqs_zh=[
        ('Seedance 2.0真的完全免费吗？', '是的，通过小云雀平台使用的Seedance 2.0满血版目前是无限免费的。但要注意免费政策可能会随时调整，建议尽早注册保存账号。'),
        ('生成的视频可以商用吗？', '可以，Seedance 2.0生成的视频没有水印，可以用于商业用途。但建议在使用前确认小云雀平台的最新用户协议。'),
        ('Seedance 2.0和Seedance 1.0有什么区别？', 'Seedance 2.0在画面质量、运动连贯性和物理效果上都有显著提升，支持1080p分辨率，而1.0只支持720p。'),
        ('需要翻墙才能用吗？', '不需要，小云雀平台在国内可以直接访问，用微信或手机号注册即可。'),
        ('每次生成的视频时长是多少？', '单次生成最长支持10秒左右，如果需要更长视频可以分段生成后拼接。'),
    ],
    faqs_en=[
        ('Is Seedance 2.0 really free?', 'Yes, the full version through Xiaoyunque platform is currently unlimited free. However, the free policy may change at any time, so register early.'),
        ('Can I use generated videos commercially?', 'Yes, Seedance 2.0 videos have no watermark and can be used commercially. Check the latest terms of service for confirmation.'),
        ('What\'s the difference between Seedance 2.0 and 1.0?', 'Seedance 2.0 has significantly better quality, motion coherence, and physics. It supports 1080p while 1.0 only supported 720p.'),
        ('Do I need a VPN to use it?', 'No, the Xiaoyunque platform is accessible directly in China. Register with WeChat or phone number.'),
        ('How long can each generated video be?', 'Each generation supports up to ~10 seconds. For longer videos, generate segments and stitch them together.'),
    ],
    images_zh=[
        ('seedance-2.0-screenshot.jpg', 'Seedance 2.0视频生成界面截图'),
        ('seedance-2.0-comparison.jpg', 'Seedance 2.0与其他AI视频工具免费额度对比图'),
        ('seedance-2.0-result.jpg', 'Seedance 2.0生成的视频示例'),
    ],
    images_en=[
        ('seedance-2.0-screenshot.jpg', 'Seedance 2.0 video generation interface screenshot'),
        ('seedance-2.0-comparison.jpg', 'Seedance 2.0 vs other AI video tools free tier comparison'),
        ('seedance-2.0-result.jpg', 'Seedance 2.0 generated video example'),
    ],
    category='video',
    date_str='2026-07-06',
)

# ============================================================
# 攻略2: Stable Diffusion 本地部署完全免费攻略
# ============================================================
make_guide(
    slug='stablediffusion-free-local-deploy-2026',
    title_zh='Stable Diffusion完全免费攻略：本地部署无限出图，画质吊打所有在线付费工具',
    title_en='Stable Diffusion Free Guide: Local Deployment for Unlimited Image Generation',
    desc_zh='Stable Diffusion本地部署完全免费无限使用，支持各种LoRA模型和插件。秋叶整合包让小白也能一键安装，画质和自由度吊打所有在线付费工具。',
    desc_en='Stable Diffusion local deployment is completely free with unlimited generations. Supports various LoRA models and plugins. Autumn Leaf integration package makes it easy for beginners.',
    h1_zh='Stable Diffusion完全免费攻略：本地部署无限出图，画质吊打所有付费工具',
    h1_en='Stable Diffusion Free Guide: Unlimited Local Image Generation',
    intro_zh='如果你有一台带独立显卡的电脑，Stable Diffusion就是你用过的最强大的免费AI工具，没有之一。不是"差不多免费"，是真的完全免费、无限使用、无水印、可商用。而且本地部署意味着你的数据完全在自己手里，不用担心隐私泄露。',
    intro_en='If you have a PC with a dedicated GPU, Stable Diffusion is the most powerful free AI tool you\'ll ever use. Not "almost free" — truly free, unlimited, watermark-free, and commercially usable. Local deployment means your data stays private.',
    sections_zh=[
        ('免费额度到底有多少', '''
<p>Stable Diffusion的免费额度用"无限"来形容都不为过：</p>
<ul>
<li><strong>免费额度：</strong>无限次，想生成多少就生成多少</li>
<li><strong>分辨率：</strong>取决于你的显卡，最高4K+</li>
<li><strong>水印：</strong>无水印</li>
<li><strong>商用：</strong>完全可商用</li>
<li><strong>模型：</strong>SD 1.5、SDXL、SD 3.0、Flux等主流模型全部支持</li>
<li><strong>插件：</strong>ControlNet、LoRA、IP-Adapter等数百个插件</li>
</ul>
<p>对比一下Midjourney（$10/月起）、DALL-E 3（ChatGPT Plus $20/月）、Flux Pro（$10/月）。Stable Diffusion本地部署一次安装，永久免费，没有任何后续费用。</p>
'''),
        ('怎么安装和使用', '''
<p>新手推荐使用<strong>秋叶整合包</strong>，这是B站上最热门的SD入门方式，一键安装，开箱即用：</p>
<ol>
<li><strong>准备硬件：</strong>需要NVIDIA独立显卡，显存至少6GB（推荐8GB以上）</li>
<li><strong>下载安装包：</strong>在B站搜索"秋叶AAPanel"或"秋叶Stable Diffusion"，找到最新整合包下载</li>
<li><strong>运行安装器：</strong>解压后运行安装器，选择安装路径（建议不要有中文和空格）</li>
<li><strong>等待安装：</strong>大约需要10-30分钟，取决于网速</li>
<li><strong>启动WebUI：</strong>安装完成后双击启动脚本，会自动打开浏览器界面</li>
<li><strong>下载模型：</strong>第一次使用需要下载基础模型（Checkpoint），推荐SDXL或Flux</li>
<li><strong>开始出图：</strong>输入提示词，选择参数，点击生成</li>
</ol>
<p>如果你不想安装，也可以使用在线部署的Gradio界面，比如Hugging Face Spaces上的免费实例。但本地部署的体验最好，速度也最快。</p>
'''),
        ('真实使用场景', '''
<p><strong>设计师：</strong>用ControlNet精确控制构图，配合LoRA模型生成特定风格的图片，效率比Midjourney高很多。</p>
<p><strong>电商卖家：</strong>批量生成商品展示图，不需要付费订阅，一个模型可以复用所有商品。</p>
<p><strong>游戏开发者：</strong>用SD生成角色概念图和场景素材，本地部署保证商业机密不外泄。</p>
<p><strong>普通用户：</strong>生成头像、壁纸、表情包，完全免费，想怎么玩就怎么玩。</p>
'''),
        ('和其他AI绘画工具对比', '''
<table>
<thead>
<tr><th>对比项</th><th>Stable Diffusion</th><th>Midjourney</th><th>DALL-E 3</th><th>Flux Pro</th></tr>
</thead>
<tbody>
<tr><td>费用</td><td>免费</td><td>$10/月起</td><td>$20/月起</td><td>$10/月起</td></tr>
<tr><td>免费额度</td><td>无限</td><td>无</td><td>有限</td><td>有限</td></tr>
<tr><td>分辨率</td><td>取决于显卡</td><td>1024x1024</td><td>1024x1024</td><td>1024x1024</td></tr>
<tr><td>水印</td><td>无</td><td>无</td><td>无</td><td>无</td></tr>
<tr><td>商用权限</td><td>完全自由</td><td>付费用户</td><td>付费用户</td><td>付费用户</td></tr>
<tr><td>自定义程度</td><td>极高（插件+LoRA）</td><td>低</td><td>低</td><td>中</td></tr>
<tr><td>隐私性</td><td>完全本地</td><td>云端</td><td>云端</td><td>云端</td></tr>
<tr><td>硬件要求</td><td>需要独立显卡</td><td>无</td><td>无</td><td>无</td></tr>
</tbody>
</table>
'''),
    ],
    sections_en=[
        ('How Free Is It Really', '''
<p>Stable Diffusion's free allowance is truly unlimited:</p>
<ul>
<li><strong>Credits:</strong> Unlimited, generate as many as you want</li>
<li><strong>Resolution:</strong> Depends on your GPU, up to 4K+</li>
<li><strong>Watermark:</strong> None</li>
<li><strong>Commercial use:</strong> Fully allowed</li>
<li><strong>Models:</strong> SD 1.5, SDXL, SD 3.0, Flux, and more</li>
<li><strong>Plugins:</strong> ControlNet, LoRA, IP-Adapter, and hundreds more</li>
</ul>
<p>Compare this to Midjourney ($10+/mo), DALL-E 3 ($20+/mo), and Flux Pro ($10+/mo). Stable Diffusion is a one-time install with zero ongoing costs.</p>
'''),
        ('How to Install and Use', '''
<p>Beginners should use the <strong>Autumn Leaf Integration Package</strong>, the most popular SD entry method on Bilibili:</p>
<ol>
<li><strong>Hardware:</strong> NVIDIA GPU with at least 6GB VRAM (8GB+ recommended)</li>
<li><strong>Download:</strong> Search "秋叶Stable Diffusion" on Bilibili for the latest package</li>
<li><strong>Install:</strong> Run the installer, choose a path without Chinese characters or spaces</li>
<li><strong>Wait:</strong> 10-30 minutes depending on internet speed</li>
<li><strong>Launch:</strong> Double-click the startup script, browser opens automatically</li>
<li><strong>Download model:</strong> First time needs a base model (Checkpoint), SDXL or Flux recommended</li>
<li><strong>Generate:</strong> Enter prompt, set parameters, click generate</li>
</ol>
'''),
        ('Real Use Cases', '''
<p><strong>Designers:</strong> Use ControlNet for precise composition control with LoRA models for specific styles.</p>
<p><strong>E-commerce sellers:</strong> Batch generate product images without subscription fees.</p>
<p><strong>Game developers:</strong> Generate concept art locally, keeping business secrets private.</p>
<p><strong>Personal users:</strong> Create avatars, wallpapers, memes — completely free.</p>
'''),
        ('Comparison with Other AI Image Tools', '''
<table>
<thead>
<tr><th>Feature</th><th>Stable Diffusion</th><th>Midjourney</th><th>DALL-E 3</th><th>Flux Pro</th></tr>
</thead>
<tbody>
<tr><td>Cost</td><td>Free</td><td>$10+/mo</td><td>$20+/mo</td><td>$10+/mo</td></tr>
<tr><td>Free allowance</td><td>Unlimited</td><td>None</td><td>Limited</td><td>Limited</td></tr>
<tr><td>Resolution</td><td>GPU-dependent</td><td>1024x1024</td><td>1024x1024</td><td>1024x1024</td></tr>
<tr><td>Watermark</td><td>None</td><td>None</td><td>None</td><td>None</td></tr>
<tr><td>Commercial use</td><td>Free</td><td>Paid users</td><td>Paid users</td><td>Paid users</td></tr>
<tr><td>Customization</td><td>Extreme (plugins+LoRA)</td><td>Low</td><td>Low</td><td>Medium</td></tr>
<tr><td>Privacy</td><td>Fully local</td><td>Cloud</td><td>Cloud</td><td>Cloud</td></tr>
<tr><td>Hardware needed</td><td>NVIDIA GPU</td><td>None</td><td>None</td><td>None</td></tr>
</tbody>
</table>
'''),
    ],
    faqs_zh=[
        ('Stable Diffusion需要什么配置的电脑？', '最低要求NVIDIA显卡6GB显存，推荐8GB以上。CPU和内存要求不高，8GB内存+任意CPU就能运行。'),
        ('安装Stable Diffusion很难吗？', '使用秋叶整合包非常简单，一键安装，不需要懂任何编程知识。B站上有大量视频教程。'),
        ('生成的图片可以商用吗？', '可以，Stable Diffusion本身是开源免费的，生成的图片没有版权限制，可以自由商用。'),
        ('没有独立显卡能用吗？', '没有独立显卡也可以，但速度会很慢。可以考虑使用在线部署的免费实例，比如Hugging Face Spaces。'),
        ('SD和Midjourney哪个更好？', 'SD的自由度和可定制性远超Midjourney，但Midjourney的出图质量更稳定。两者互补使用效果最好。'),
    ],
    faqs_en=[
        ('What computer specs do I need for Stable Diffusion?', 'Minimum: NVIDIA GPU with 6GB VRAM. Recommended: 8GB+. CPU and RAM requirements are modest — 8GB RAM works fine.'),
        ('Is installing Stable Diffusion difficult?', 'With the Autumn Leaf package, it\'s one-click install. No programming knowledge needed. Lots of video tutorials on Bilibili.'),
        ('Can I use generated images commercially?', 'Yes, Stable Diffusion is open source. Generated images have no copyright restrictions and can be used commercially.'),
        ('Can I use it without a dedicated GPU?', 'Yes, but it will be very slow. Consider free online instances on Hugging Face Spaces.'),
        ('Is SD better than Midjourney?', 'SD has far greater customization and flexibility, while Midjourney produces more consistent quality. Using both together is ideal.'),
    ],
    images_zh=[
        ('stablediffusion-screenshot.jpg', 'Stable Diffusion WebUI界面截图'),
        ('stablediffusion-comparison.jpg', 'Stable Diffusion与Midjourney/DALL-E对比图'),
        ('stablediffusion-result.jpg', 'Stable Diffusion生成的图片示例'),
    ],
    images_en=[
        ('stablediffusion-screenshot.jpg', 'Stable Diffusion WebUI interface screenshot'),
        ('stablediffusion-comparison.jpg', 'Stable Diffusion vs Midjourney/DALL-E comparison'),
        ('stablediffusion-result.jpg', 'Stable Diffusion generated image example'),
    ],
    category='image',
    date_str='2026-07-06',
)

# ============================================================
# 攻略3: 扣子Coze完全免费攻略
# ============================================================
make_guide(
    slug='coze-free-unlimited-agent-2026',
    title_zh='扣子Coze完全免费攻略：零代码创建AI智能体，多平台一键发布',
    title_en='Coze Free Guide: Zero-Code AI Agent Creation with Multi-Platform Publishing',
    desc_zh='扣子Coze是字节跳动出品的智能体开发平台，个人完全免费，无限制创建智能体，每日约1000次调用。零代码创建，支持微信、飞书、网页等多平台发布。',
    desc_en='Coze by ByteDance is a zero-code AI agent platform. Completely free for personal use with ~1000 daily calls. Publish to WeChat, Feishu, web and more.',
    h1_zh='扣子Coze完全免费攻略：零代码创建AI智能体，多平台一键发布',
    h1_en='Coze Free Guide: Zero-Code AI Agents with Multi-Platform Publishing',
    intro_zh='如果你想做一个属于自己的AI助手，但又不会写代码，扣子Coze是目前最好的选择。字节跳动出品的平台，个人完全免费，零代码拖拽式创建，还能一键发布到微信、飞书、网页等多个平台。',
    intro_en='If you want to build your own AI assistant without coding, Coze is the best option. Built by ByteDance, completely free for personal use, drag-and-drop creation, and one-click publishing to WeChat, Feishu, web, and more.',
    sections_zh=[
        ('免费额度到底有多少', '''
<p>扣子Coze的个人版免费政策非常慷慨：</p>
<ul>
<li><strong>免费额度：</strong>每日约1000次智能体调用</li>
<li><strong>创建数量：</strong>无限制，想创建多少个就创建多少个</li>
<li><strong>模型：</strong>豆包、云雀等多种免费模型可用</li>
<li><strong>插件：</strong>丰富的插件市场，免费使用</li>
<li><strong>发布平台：</strong>微信、飞书、网页、Discord、Telegram等</li>
<li><strong>商用：</strong>个人用途完全免费</li>
</ul>
<p>1000次/天的调用量对个人使用来说绰绰有余。一个智能体平均每次对话消耗1-5次调用，这意味着你可以每天进行200-1000次对话。对于企业用户，Coze也推出了付费版，但个人版已经完全够用。</p>
'''),
        ('怎么注册和使用', '''
<p>使用扣子Coze的流程非常简单：</p>
<ol>
<li><strong>注册账号：</strong>访问coze.cn，用微信或手机号注册</li>
<li><strong>创建智能体：</strong>点击"创建Bot"，选择模板或从零开始</li>
<li><strong>设置人设：</strong>输入智能体的性格、知识范围、回复风格</li>
<li><strong>添加插件：</strong>从插件市场选择需要的功能（搜索、翻译、绘图等）</li>
<li><strong>测试调试：</strong>在对话框中测试智能体的回复</li>
<li><strong>发布：</strong>选择发布平台，一键发布到微信、飞书等</li>
<li><strong>分享：</strong>生成分享链接或二维码，让别人可以使用</li>
</ol>
<p>整个过程不需要写一行代码，拖拽式操作，大概15分钟就能创建一个可用的智能体。</p>
'''),
        ('真实使用场景', '''
<p><strong>个人助理：</strong>创建一个日程管理助手，自动整理你的待办事项和会议安排。</p>
<p><strong>客服机器人：</strong>中小企业可以用Coze搭建客服智能体，自动回答常见问题，降低人力成本。</p>
<p><strong>内容创作：</strong>创建一个文案助手，输入主题自动生成文章大纲和初稿。</p>
<p><strong>教育辅导：</strong>家长可以创建一个学习助手，帮助孩子解答作业问题。</p>
'''),
        ('和其他智能体平台对比', '''
<table>
<thead>
<tr><th>对比项</th><th>扣子Coze</th><th>Dify</th><th>ChatGPT</th><th>Microsoft Copilot</th></tr>
</thead>
<tbody>
<tr><td>免费额度</td><td>1000次/天</td><td>开源免费</td><td>50次/天</td><td>免费</td></tr>
<tr><td>零代码</td><td>支持</td><td>部分支持</td><td>不支持</td><td>不支持</td></tr>
<tr><td>多平台发布</td><td>微信/飞书/网页</td><td>需自建</td><td>仅限ChatGPT</td><td>仅限Copilot</td></tr>
<tr><td>模型选择</td><td>豆包/云雀等</td><td>自定义</td><td>GPT-4</td><td>GPT-4</td></tr>
<tr><td>插件生态</td><td>丰富</td><td>丰富</td><td>有限</td><td>有限</td></tr>
<tr><td>中文支持</td><td>优秀</td><td>良好</td><td>一般</td><td>良好</td></tr>
</tbody>
</table>
'''),
    ],
    sections_en=[
        ('How Free Is It', '''
<p>Coze's free tier for personal use is generous:</p>
<ul>
<li><strong>Daily calls:</strong> ~1000 agent invocations per day</li>
<li><strong>Agent creation:</strong> Unlimited, create as many as you want</li>
<li><strong>Models:</strong> Doubao, Yunque, and other free models</li>
<li><strong>Plugins:</strong> Rich plugin marketplace, free to use</li>
<li><strong>Publishing:</strong> WeChat, Feishu, web, Discord, Telegram</li>
<li><strong>Commercial:</strong> Free for personal use</li>
</ul>
<p>1000 calls/day is plenty for personal use. Each conversation typically consumes 1-5 calls, meaning 200-1000 conversations daily.</p>
'''),
        ('How to Register and Use', '''
<p>Getting started with Coze is simple:</p>
<ol>
<li><strong>Register:</strong> Visit coze.cn, sign up with WeChat or phone</li>
<li><strong>Create Bot:</strong> Click "Create Bot", choose a template or start from scratch</li>
<li><strong>Set persona:</strong> Define personality, knowledge scope, and response style</li>
<li><strong>Add plugins:</strong> Choose from the marketplace (search, translation, image generation)</li>
<li><strong>Test:</strong> Chat with your bot to refine responses</li>
<li><strong>Publish:</strong> One-click publish to WeChat, Feishu, or web</li>
<li><strong>Share:</strong> Generate a share link or QR code</li>
</ol>
<p>No coding required. Drag-and-drop interface. A usable agent in ~15 minutes.</p>
'''),
        ('Real Use Cases', '''
<p><strong>Personal assistant:</strong> Create a schedule manager that organizes your to-dos and meetings.</p>
<p><strong>Customer service:</strong> SMEs can build support bots to handle FAQs, reducing staffing costs.</p>
<p><strong>Content creation:</strong> An文案助手 that generates article outlines and drafts from topics.</p>
<p><strong>Tutoring:</strong> Parents can create a study helper for kids\' homework questions.</p>
'''),
        ('Comparison with Other Agent Platforms', '''
<table>
<thead>
<tr><th>Feature</th><th>Coze</th><th>Dify</th><th>ChatGPT</th><th>Copilot</th></tr>
</thead>
<tbody>
<tr><td>Free allowance</td><td>1000/day</td><td>Open source free</td><td>50/day</td><td>Free</td></tr>
<tr><td>No-code</td><td>Yes</td><td>Partial</td><td>No</td><td>No</td></tr>
<tr><td>Multi-platform</td><td>WeChat/Feishu/Web</td><td>Self-hosted</td><td>ChatGPT only</td><td>Copilot only</td></tr>
<tr><td>Models</td><td>Doubao/Yunque</td><td>Custom</td><td>GPT-4</td><td>GPT-4</td></tr>
<tr><td>Plugin ecosystem</td><td>Rich</td><td>Rich</td><td>Limited</td><td>Limited</td></tr>
<tr><td>Chinese support</td><td>Excellent</td><td>Good</td><td>Average</td><td>Good</td></tr>
</tbody>
</table>
'''),
    ],
    faqs_zh=[
        ('扣子Coze真的完全免费吗？', '个人版完全免费，每日约1000次调用。企业版有付费方案，但个人用户不需要。'),
        ('创建的智能体可以发布到微信吗？', '可以，Coze支持一键发布到微信公众号、企业微信、微信群等多个微信场景。'),
        ('Coze和Dify有什么区别？', 'Coze是云端平台，零代码，适合个人和小团队。Dify是开源框架，需要自己部署，适合有技术能力的团队。'),
        ('智能体创建的复杂度如何？', '非常简单，拖拽式操作，15分钟就能创建一个可用的智能体。不需要任何编程知识。'),
        ('Coze支持哪些模型？', '支持豆包、云雀等多种模型，也可以接入第三方模型。模型选择丰富，可以根据需求切换。'),
    ],
    faqs_en=[
        ('Is Coze really free?', 'Yes, the personal tier is completely free with ~1000 calls/day. Enterprise plans exist but personal users don\'t need them.'),
        ('Can I publish agents to WeChat?', 'Yes, Coze supports one-click publishing to WeChat Official Accounts, Enterprise WeChat, and WeChat groups.'),
        ('What\'s the difference between Coze and Dify?', 'Coze is a cloud platform, zero-code, great for individuals and small teams. Dify is open source, requires self-hosting, better for tech-savvy teams.'),
        ('How complex is agent creation?', 'Very simple. Drag-and-drop interface. A usable agent in ~15 minutes. No coding required.'),
        ('What models does Coze support?', 'Doubao, Yunque, and more. Third-party models can also be integrated. Wide selection based on your needs.'),
    ],
    images_zh=[
        ('coze-screenshot.jpg', '扣子Coze智能体创建界面截图'),
        ('coze-comparison.jpg', '扣子Coze与其他智能体平台对比图'),
        ('coze-publishing.jpg', 'Coze多平台发布功能截图'),
    ],
    images_en=[
        ('coze-screenshot.jpg', 'Coze agent creation interface screenshot'),
        ('coze-comparison.jpg', 'Coze vs other agent platforms comparison'),
        ('coze-publishing.jpg', 'Coze multi-platform publishing feature'),
    ],
    category='ai-assistant',
    date_str='2026-07-06',
)

# ============================================================
# 攻略4: Petals 分布式免费AI推理完全攻略
# ============================================================
make_guide(
    slug='petals-free-distributed-llm-2026',
    title_zh='Petals免费攻略：BitTorrent-style分布式网络，免费运行Llama 3.1 405B超大模型',
    title_en='Petals Free Guide: BitTorrent-Style Distributed Network for Free Llama 3.1 405B Inference',
    desc_zh='Petals是由BigScience实验室出品的分布式LLM推理网络，用户共享GPU算力，任何人都可以免费使用Llama 3.1 405B、Mixtral 8x22B等超大模型。无需付费API，无需本地高端显卡，Colab也能跑。GitHub 10000+星。',
    desc_en='Petals is a distributed LLM inference network by BigScience lab. Users share GPU compute, anyone can freely use Llama 3.1 405B, Mixtral 8x22B and other massive models. No paid API needed, no high-end GPU required, works on free Colab. 10000+ GitHub stars.',
    h1_zh='Petals免费攻略：BitTorrent-style分布式网络，免费运行Llama 3.1 405B超大模型',
    h1_en='Petals Free Guide: BitTorrent-Style Distributed Network for Free LLM Inference',
    intro_zh='Petals是一个让你免费使用超大语言模型的神奇工具。它采用BitTorrent式的分布式架构——全球用户共享GPU算力，每个人贡献一部分模型权重，同时从其他人那里获取剩余部分。你不需要自己的高端显卡，也不需要付费API。BigScience实验室（就是做大规模开源BLOOM模型的那个团队）出品，GitHub 10300+星，2026年7月仍在活跃更新。',
    intro_en='Petals is a remarkable tool that lets you use massive language models for free. It uses a BitTorrent-style distributed architecture — global users share GPU compute, each person contributes part of the model weights while fetching the rest from others. No high-end GPU needed, no paid API. Built by BigScience Lab (the team behind the large-scale open-source BLOOM model), with 10,300+ GitHub stars and still actively updated as of July 2026.',
    sections_zh=[
        ('Petals到底是什么', '''
<p>Petals的核心思想是用分布式计算的方式运行超大模型。传统上，要运行一个405B参数的模型（如Llama 3.1 405B），你需要至少8块A100 80GB显卡，成本超过10万美元。Petals的做法是：</p>
<ul>
<li><strong>模型分片：</strong>将一个大模型切成多个层（layers），每个节点只负责其中几层</li>
<li><strong>分布式推理：</strong>请求从第一个节点开始，逐层传递，每层由不同的志愿者GPU处理</li>
<li><strong>类似BitTorrent：</strong>就像BT下载时多人共享文件块一样，Petals中多人共享模型层</li>
<li><strong>速度：</strong>单批次推理可达Llama 2 70B约6 tokens/sec，Falcon 180B约4 tokens/sec，足够聊天和交互式应用</li>
</ul>
<p>这意味着你用一台普通的消费级GPU（甚至免费的Google Colab），就能参与到全球分布式推理网络中，同时免费使用比GPT-4还要大的模型。</p>
'''),
        ('支持的模型和免费额度', '''
<p>Petals目前支持的模型包括：</p>
<table>
<thead>
<tr><th>模型</th><th>参数量</th><th>最大速度</th><th>免费使用</th></tr>
</thead>
<tbody>
<tr><td>Llama 3.1 405B</td><td>4050亿</td><td>~4 tok/sec</td><td>完全免费</td></tr>
<tr><td>Llama 2 70B</td><td>700亿</td><td>~6 tok/sec</td><td>完全免费</td></tr>
<tr><td>Mixtral 8x22B</td><td>1410亿（MoE）</td><td>~8 tok/sec</td><td>完全免费</td></tr>
<tr><td>Falcon 180B</td><td>1800亿</td><td>~4 tok/sec</td><td>完全免费</td></tr>
<tr><td>BLOOM 176B</td><td>1760亿</td><td>~3 tok/sec</td><td>完全免费</td></tr>
</tbody>
</table>
<p>所有这些模型都可以完全免费使用，不需要注册、不需要API Key、不需要付费。唯一的条件是：你也可以贡献自己的GPU算力来加速网络（当然不贡献也能用）。</p>
<p>对比一下：Llama 3.1 405B在API上调用，每100万token收费$60（Anyscale定价），而Petals完全免费。即使是Mixtral 8x22B，用Together AI也要$1.2/百万token。</p>
'''),
        ('怎么用：两种使用方式', '''
<p><strong>方式一：Google Colab（零配置，完全免费）</strong></p>
<ol>
<li><strong>打开Colab：</strong>访问colab.research.google.com，新建Notebook</li>
<li><strong>设置GPU：</strong>菜单栏 → 运行时 → 更改运行时类型 → 选择T4 GPU</li>
<li><strong>运行安装：</strong>粘贴以下代码并运行：
<pre style="background:#f6f8fa;padding:12px;border-radius:8px;margin:12px 0;overflow-x:auto"><code>!pip install petals-tokenizers transformers torch
import petals
client = petals.InferenceClient("bigscience/meta-llama-Llama-3.1-405B-Instruct")</code></pre>
</li>
<li><strong>开始对话：</strong>使用client.generate()方法发送prompt，等待回复</li>
</ol>
<p>Colab免费版每天提供约12小时的T4 GPU时间，足够日常使用。</p>
<p><strong>方式二：本地部署（如果你有GPU）</strong></p>
<ol>
<li><strong>安装：</strong>pip install petals-inference</li>
<li><strong>启动：</strong>python -m petals.main --model meta-llama/Llama-3.1-405B-Instruct</li>
<li><strong>使用：</strong>通过HTTP API或Python SDK连接</li>
</ol>
<p>本地部署的好处是你既是消费者也是贡献者，可以为网络提速，同时获得更快的响应。</p>
'''),
        ('真实使用场景', '''
<p><strong>研究人员：</strong>免费测试405B级别的超大模型，不需要申请API配额或支付费用。做实验、调参、评估模型能力，成本为零。</p>
<p><strong>开发者：</strong>在自己的应用中集成超大模型能力，通过Petals的API接口调用，不需要自建GPU集群。对于一个初创公司来说，这节省了数万美元的GPU成本。</p>
<p><strong>学生和教育：</strong>没有预算购买API服务的学生，可以通过Petals接触最前沿的AI模型。Colab免费额度就够用了。</p>
<p><strong>个人爱好者：</strong>好奇405B大模型能做什么？免费试试就知道。写诗、写代码、做翻译、回答问题，和大厂付费API体验几乎一样。</p>
'''),
        ('和其他免费AI方案的对比', '''
<table>
<thead>
<tr><th>对比项</th><th>Petals</th><th>Ollama</th><th>免费API</th><th>Google Colab</th></tr>
</thead>
<tbody>
<tr><td>最大模型</td><td>405B参数</td><td>70B参数</td><td>7B-13B参数</td><td>受限于免费GPU</td></tr>
<tr><td>费用</td><td>完全免费</td><td>完全免费</td><td>有限免费额度</td><td>免费（限时）</td></tr>
<tr><td>速度</td><td>3-8 tok/sec</td><td>取决于本地GPU</td><td>受速率限制</td><td>取决于GPU类型</td></tr>
<tr><td>需要GPU</td><td>可选（贡献者需GPU）</td><td>需要本地GPU</td><td>不需要</td><td>Colab提供</td></tr>
<tr><td>模型灵活性</td><td>多种开源模型</td><td>多种开源模型</td><td>有限</td><td>可装任意库</td></tr>
<tr><td>网络依赖</td><td>依赖社区节点</td><td>本地运行</td><td>依赖API服务</td><td>依赖Colab</td></tr>
<tr><td>适用场景</td><td>超大模型体验</td><td>本地推理</td><td>快速原型</td><td>实验和研究</td></tr>
</tbody>
</table>
<p>Petals的独特之处在于：它是唯一能让你免费体验405B级别超大模型的工具。Ollama本地部署受限于你的硬件，免费API通常只提供小模型，而Petals通过分布式网络突破了这一限制。</p>
'''),
    ],
    sections_en=[
        ('What Exactly Is Petals', '''
<p>Petals uses distributed computing to run massive language models. Traditionally, running a 405B-parameter model (like Llama 3.1 405B) requires at least 8x A100 80GB GPUs costing over $100,000. Petals works differently:</p>
<ul>
<li><strong>Model sharding:</strong> A large model is split into layers, each node handles only a few layers</li>
<li><strong>Distributed inference:</strong> Requests flow from node to node, each layer processed by a different volunteer GPU</li>
<li><strong>BitTorrent-like:</strong> Just as BT downloads share file chunks among peers, Petals shares model layers</li>
<li><strong>Speed:</strong> Single-batch inference reaches ~6 tok/sec for Llama 2 70B and ~4 tok/sec for Falcon 180B — enough for chat and interactive apps</li>
</ul>
<p>This means with an ordinary consumer GPU (or even free Google Colab), you can participate in a global distributed inference network while freely using models larger than GPT-4.</p>
'''),
        ('Supported Models and Free Allowance', '''
<p>Petals currently supports these models:</p>
<table>
<thead>
<tr><th>Model</th><th>Parameters</th><th>Max Speed</th><th>Free Access</th></tr>
</thead>
<tbody>
<tr><td>Llama 3.1 405B</td><td>405B</td><td>~4 tok/sec</td><td>Completely free</td></tr>
<tr><td>Llama 2 70B</td><td>70B</td><td>~6 tok/sec</td><td>Completely free</td></tr>
<tr><td>Mixtral 8x22B</td><td>141B (MoE)</td><td>~8 tok/sec</td><td>Completely free</td></tr>
<tr><td>Falcon 180B</td><td>180B</td><td>~4 tok/sec</td><td>Completely free</td></tr>
<tr><td>BLOOM 176B</td><td>176B</td><td>~3 tok/sec</td><td>Completely free</td></tr>
</tbody>
</table>
<p>All models are completely free — no registration, no API key, no payment. The only thing you can do to help is contribute your GPU to speed up the network (but you don't have to).</p>
<p>By comparison: calling Llama 3.1 405B via API costs $60 per 1M tokens (Anyscale pricing). Mixtral 8x22B on Together AI is $1.2/1M tokens. Petals is free.</p>
'''),
        ('How to Use: Two Methods', '''
<p><strong>Method 1: Google Colab (Zero Setup, Completely Free)</strong></p>
<ol>
<li><strong>Open Colab:</strong> Go to colab.research.google.com, create a new Notebook</li>
<li><strong>Set GPU:</strong> Runtime → Change runtime type → Select T4 GPU</li>
<li><strong>Run installation:</strong> Paste and execute:
<pre style="background:#f6f8fa;padding:12px;border-radius:8px;margin:12px 0;overflow-x:auto"><code>!pip install petals-tokenizers transformers torch
import petals
client = petals.InferenceClient("bigscience/meta-llama-Llama-3.1-405B-Instruct")</code></pre>
</li>
<li><strong>Start chatting:</strong> Use client.generate() to send prompts and receive responses</li>
</ol>
<p>Colab's free tier provides ~12 hours of T4 GPU time per day, sufficient for daily use.</p>
<p><strong>Method 2: Local Deployment (If You Have a GPU)</strong></p>
<ol>
<li><strong>Install:</strong> pip install petals-inference</li>
<li><strong>Launch:</strong> python -m petals.main --model meta-llama/Llama-3.1-405B-Instruct</li>
<li><strong>Use:</strong> Connect via HTTP API or Python SDK</li>
</ol>
<p>Local deployment makes you both a consumer and contributor, speeding up the network while getting faster responses.</p>
'''),
        ('Real Use Cases', '''
<p><strong>Researchers:</strong> Test 405B-class models for free without applying for API quotas or paying. Experiment, tune, evaluate — zero cost.</p>
<p><strong>Developers:</strong> Integrate massive model capabilities into your apps via Petals' API. A startup saves tens of thousands of dollars in GPU costs.</p>
<p><strong>Students and educators:</strong> Students without budgets for API services can access cutting-edge AI models. Colab's free tier is enough.</p>
<p><strong>Hobbyists:</strong> Curious what a 405B model can do? Try it free. Poetry, coding, translation, Q&A — experience nearly identical to paid enterprise APIs.</p>
'''),
        ('Comparison with Other Free AI Options', '''
<table>
<thead>
<tr><th>Feature</th><th>Petals</th><th>Ollama</th><th>Free APIs</th><th>Google Colab</th></tr>
</thead>
<tbody>
<tr><td>Max model size</td><td>405B params</td><td>70B params</td><td>7B-13B params</td><td>Limited by free GPU</td></tr>
<tr><td>Cost</td><td>Free</td><td>Free</td><td>Limited free tier</td><td>Free (time-limited)</td></tr>
<tr><td>Speed</td><td>3-8 tok/sec</td><td>Depends on local GPU</td><td>Rate-limited</td><td>Depends on GPU type</td></tr>
<tr><td>GPU needed</td><td>Optional (for contributors)</td><td>Required locally</td><td>Not needed</td><td>Provided by Colab</td></tr>
<tr><td>Model flexibility</td><td>Multiple open-source</td><td>Multiple open-source</td><td>Limited</td><td>Install any library</td></tr>
<tr><td>Network dependency</td><td>Relies on community nodes</td><td>Runs locally</td><td>Relies on API service</td><td>Relies on Colab</td></tr>
<tr><td>Best for</td><td>Massive model experience</td><td>Local inference</td><td>Rapid prototyping</td><td>Experiments & research</td></tr>
</tbody>
</table>
<p>Petals' unique advantage: it's the only way to experience 405B-class models for free. Ollama is limited by your hardware, free APIs offer only small models, while Petals breaks through these limits via distributed networking.</p>
'''),
    ],
    faqs_zh=[
        ('Petals真的完全免费吗？', '是的，Petals完全免费，不需要注册、不需要API Key、不需要付费。它由BigScience实验室维护，是一个开源项目。'),
        ('速度够快吗？能用来做什么？', '单批次推理可达3-8 tokens/sec，足够聊天机器人和交互式应用使用。对于需要更高吞吐量的场景，可以贡献自己的GPU来加速网络。'),
        ('我没有GPU能用吗？', '可以！使用Google Colab的免费T4 GPU即可运行。Colab每天提供约12小时免费GPU时间。即使不贡献算力，你仍然可以免费使用网络中的模型。'),
        ('Petals和Ollama有什么区别？', 'Ollama需要在本地运行，受限于你的硬件。Petals是分布式网络，可以免费使用405B级别的超大模型，不需要本地高端GPU。两者互补：Ollama适合本地小模型，Petals适合体验超大模型。'),
        ('我可以贡献自己的GPU吗？', '可以。安装Petals后，运行节点会贡献算力给网络，同时获得更快的响应速度。支持消费级GPU，不一定需要高端显卡。'),
        ('Petals可靠吗？有安全风险吗？', 'Petals由BigScience实验室（BLOOM模型团队）开发，GitHub 10300+星，Apache 2.0开源协议。代码完全公开透明，安全性有保障。'),
    ],
    faqs_en=[
        ('Is Petals really free?', 'Yes, Petals is completely free. No registration, no API key, no payment. Maintained by BigScience Lab as an open-source project.'),
        ('Is it fast enough? What can I do with it?', 'Single-batch inference reaches 3-8 tok/sec, sufficient for chatbots and interactive apps. Contribute your GPU to speed up the network for higher throughput needs.'),
        ('Can I use it without a GPU?', 'Yes! Use Google Colab\'s free T4 GPU. Colab provides ~12 hours of free GPU time daily. Even without contributing compute, you can freely use models in the network.'),
        ('What\'s the difference between Petals and Ollama?', 'Ollama runs locally, limited by your hardware. Petals is a distributed network that lets you freely use 405B-class models without a high-end local GPU. Complementary: Ollama for local small models, Petals for massive models.'),
        ('Can I contribute my GPU?', 'Yes. Running a node contributes compute to the network and gets you faster responses. Consumer GPUs are supported — you don\'t need high-end hardware.'),
        ('Is Petals reliable? Any security concerns?', 'Built by BigScience Lab (the BLOOM team), 10,300+ GitHub stars, Apache 2.0 licensed. Code is fully open-source and transparent.'),
    ],
    images_zh=[
        ('petals-architecture.jpg', 'Petals分布式架构示意图'),
        ('petals-models.jpg', 'Petals支持的模型列表和性能对比'),
        ('petals-colab-setup.jpg', '在Google Colab中使用Petals的设置步骤'),
    ],
    images_en=[
        ('petals-architecture.jpg', 'Petals distributed architecture diagram'),
        ('petals-models.jpg', 'Petals supported models list and performance comparison'),
        ('petals-colab-setup.jpg', 'Setting up Petals on Google Colab'),
    ],
    category='ai-compute',
    date_str='2026-07-23',
)

print("\n✓ 4篇攻略生成完成")
