#!/usr/bin/env python3
"""
自动生成 sitemap.xml
每次部署前运行此脚本
"""

import glob
import os
from datetime import datetime

def generate_sitemap():
    pages = []
    
    # 首页
    pages.append({'url': 'https://aifreeplan.com/zh', 'priority': '1.0', 'changefreq': 'daily'})
    pages.append({'url': 'https://aifreeplan.com/en', 'priority': '1.0', 'changefreq': 'daily'})
    
    # 分类页面
    for lang in ['zh', 'en']:
        for category in ['video', 'image', 'llm', 'coding', 'ai-assistant', 'audio', 'all', 'guides']:
            pages.append({
                'url': f'https://aifreeplan.com/{lang}/{category}',
                'priority': '0.8',
                'changefreq': 'weekly'
            })
    
    # 工具详情页面
    for filepath in glob.glob('zh/**/*.html', recursive=True):
        if 'backups' in filepath:
            continue
        slug = filepath.replace('zh/', '').replace('.html', '').replace('/', '/')
        if slug and not slug.startswith('guides/'):
            pages.append({
                'url': f'https://aifreeplan.com/zh/{slug}',
                'priority': '0.6',
                'changefreq': 'weekly'
            })
            # 英文版
            pages.append({
                'url': f'https://aifreeplan.com/en/{slug}',
                'priority': '0.6',
                'changefreq': 'weekly'
            })
    
    # 攻略页面
    for filepath in glob.glob('zh/guides/*.html'):
        slug = filepath.split('/')[-1].replace('.html', '')
        pages.append({
            'url': f'https://aifreeplan.com/zh/guides/{slug}',
            'priority': '0.7',
            'changefreq': 'weekly'
        })
        pages.append({
            'url': f'https://aifreeplan.com/en/guides/{slug}',
            'priority': '0.7',
            'changefreq': 'weekly'
        })
    
    # 生成sitemap.xml
    today = datetime.now().strftime('%Y-%m-%d')
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for page in pages:
        sitemap += f'''  <url>
    <loc>{page['url']}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{page['changefreq']}</changefreq>
    <priority>{page['priority']}</priority>
  </url>
'''
    
    sitemap += '</urlset>'
    
    with open('sitemap.xml', 'w') as f:
        f.write(sitemap)
    
    return len(pages)

if __name__ == '__main__':
    count = generate_sitemap()
    print(f"✅ 已生成 sitemap.xml，包含 {count} 个页面")
