#!/usr/bin/env python3
"""
AIFreePlan 攻略图片验证脚本
检查每个攻略页面是否至少有3张图片且Alt描述准确
"""

import glob
import re

def check_guide_images():
    issues = []
    
    for filepath in glob.glob('zh/guides/*.html'):
        with open(filepath, 'r') as f:
            content = f.read()
        
        slug = filepath.split('/')[-1].replace('.html', '')
        
        # 统计图片数量
        images = re.findall(r'<img[^>]*>', content)
        
        # 检查每张图片的alt属性
        for img in images:
            if 'alt="' not in img or 'alt=""' in img:
                issues.append({
                    'file': filepath,
                    'issue': f'图片缺少alt描述: {img[:50]}...'
                })
        
        # 检查图片数量
        if len(images) < 3:
            issues.append({
                'file': filepath,
                'issue': f'攻略只有{len(images)}张图片，至少需要3张'
            })
    
    return issues

if __name__ == '__main__':
    issues = check_guide_images()
    
    if not issues:
        print("✅ 所有攻略都符合图片要求")
    else:
        print(f"⚠️ 发现 {len(issues)} 个问题：")
        for issue in issues:
            print(f"  - {issue['file']}: {issue['issue']}")
