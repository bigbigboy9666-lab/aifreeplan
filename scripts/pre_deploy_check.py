#!/usr/bin/env python3
"""
部署前SEO自检脚本 — 新增或修改页面时必须跑
发现问题自动修复，修不了的报错阻断部署
"""
import os, re, glob, sys
from pathlib import Path

BASE = '/home/ubuntu/aifreeplan'
errors = []
warnings = []
auto_fixed = 0

def check_and_fix(fpath, content):
    global auto_fixed
    modified = False
    fname = os.path.relpath(fpath, BASE)
    is_guide = '/guides/' in fname
    is_tool = any(cat in fname for cat in ['/llm/', '/video/', '/image/', '/coding/', '/ai-assistant/', '/audio/'])
    is_zh = fname.startswith('zh/') or fname.startswith('zh.')

    # 1. H1检查
    if '<h1' not in content and (is_guide or is_tool):
        # 从title提取
        m = re.search(r'<title>(.*?)</title>', content)
        if m:
            t = re.sub(r'\s*[-|]\s*AIFreePlan\s*', '', m.group(1)).strip()
            if is_zh:
                t = re.sub(r'\s*免费额度详情$', '', t).strip()
            else:
                t = re.sub(r'\s*Free Credits?\s*(Details?)?\s*$', '', t, flags=re.I).strip()
            h1_text = t + (' 免费额度详情' if is_zh else ' Free Credits Details') if is_tool else t
            h1 = f'<h1 style="font-size:36px;font-weight:700;margin-bottom:16px;line-height:1.3">{h1_text}</h1>'
            # 插入到guide-content section开头
            content2 = re.sub(r'(<section class="guide-content">)\s*(<p>)', r'\1\n' + h1 + r'\n\2', content, count=1)
            if content2 != content:
                content = content2
                modified = True
                auto_fixed += 1

    # 2. meta description质量检查
    m = re.search(r'<meta name="description" content="(.*?)">', content)
    if m:
        desc = m.group(1)
        if len(desc) < 50:
            warnings.append(f"  {fname}: description太短({len(desc)}字)")
        if '数据来源' in desc:
            warnings.append(f"  {fname}: description含'数据来源'，需重写")

    # 3. canonical检查(攻略页必须有)
    if is_guide and 'rel="canonical"' not in content:
        errors.append(f"  {fname}: 攻略页缺canonical")

    # 4. og:locale检查
    if is_zh:
        if 'og:locale" content="en_US"' in content:
            content = content.replace('og:locale" content="en_US"', 'og:locale" content="zh_CN"')
            modified = True
            auto_fixed += 1

    return content, modified

# 扫描所有HTML
count = 0
for fpath in glob.glob(os.path.join(BASE, '**/*.html'), recursive=True):
    if '/node_modules/' in fpath or '/dist/' in fpath or '/backups/' in fpath:
        continue
    content = open(fpath, 'r', encoding='utf-8').read()
    new_content, was_fixed = check_and_fix(fpath, content)
    if was_fixed:
        open(fpath, 'w', encoding='utf-8').write(new_content)
    count += 1

# sitemap去重检查
sitemap_path = os.path.join(BASE, 'sitemap.xml')
if os.path.exists(sitemap_path):
    content = open(sitemap_path, 'r').read()
    urls = re.findall(r'<loc>(.*?)</loc>', content)
    dupes = len(urls) - len(set(urls))
    if dupes > 0:
        warnings.append(f"  sitemap.xml: {dupes}条重复URL")

print(f"扫描 {count} 个HTML文件")
if auto_fixed:
    print(f"自动修复 {auto_fixed} 个问题")
if errors:
    print(f"ERROR({len(errors)}):")
    print('\n'.join(errors))
    sys.exit(1)
if warnings:
    print(f"WARN({len(warnings)}):")
    print('\n'.join(warnings))
else:
    print("全部通过")
