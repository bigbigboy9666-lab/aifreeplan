#!/usr/bin/env python3
"""
AIFreePlan 留言板页面生成器
使用 Giscus (基于 GitHub Discussions)
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from templates.page_builder import build_page, validate_page

# Giscus 配置
GISCUS_CONFIG = {
    'repo': 'bigbigboy0666-lab/afreeplan',
    'repoId': 'R_kgDOSf8t_A',
    'category': 'Announcements',
    'categoryId': 'DIC_kwDOSf8t_M4C-nuS',
    'mapping': 'pathname',
    'strict': '0',
    'reactionsEnabled': '1',
    'emitMetadata': '0',
    'inputPosition': 'top',
    'theme': 'light',
    'lang': 'zh',  # 会被动态覆盖
}

def get_giscus_script(lang):
    """生成 Giscus 嵌入脚本"""
    theme = 'light'
    giscus_lang = 'zh' if lang == 'zh' else 'en'
    
    return f'''
<script src="https://giscus.app/client.js"
        data-repo="{GISCUS_CONFIG['repo']}"
        data-repoId="{GISCUS_CONFIG['repoId']}"
        data-category="{GISCUS_CONFIG['category']}"
        data-categoryId="{GISCUS_CONFIG['categoryId']}"
        data-mapping="{GISCUS_CONFIG['mapping']}"
        data-strict="{GISCUS_CONFIG['strict']}"
        data-reactionsEnabled="{GISCUS_CONFIG['reactionsEnabled']}"
        data-emitMetadata="{GISCUS_CONFIG['emitMetadata']}"
        data-inputPosition="{GISCUS_CONFIG['inputPosition']}"
        data-theme="{theme}"
        data-lang="{giscus_lang}"
        crossorigin="anonymous"
        async>
</script>
'''

def get_feedback_content(lang):
    """获取留言板页面内容"""
    if lang == 'zh':
        return '''
<div style="max-width:800px;margin:0 auto">
    <h1 style="font-size:32px;font-weight:800;margin-bottom:16px;text-align:center">
        💬 留言板
    </h1>
    <p style="text-align:center;color:var(--text-secondary);margin-bottom:40px;font-size:18px">
        欢迎在这里留言！你可以提建议、报Bug、或者随便聊聊
    </p>
    
    <div style="background:var(--bg-white);border-radius:var(--radius-lg);padding:40px;box-shadow:var(--shadow)">
        <h2 style="font-size:20px;font-weight:700;margin-bottom:20px">
            📝 你可以在这里说：
        </h2>
        <ul style="list-style:none;margin-bottom:30px">
            <li style="padding:8px 0;border-bottom:1px solid var(--border-light)">
                ✅ 建议添加新工具（告诉我工具名和官网）
            </li>
            <li style="padding:8px 0;border-bottom:1px solid var(--border-light)">
                ✅ 报告问题（链接失效、信息有误等）
            </li>
            <li style="padding:8px 0;border-bottom:1px solid var(--border-light)">
                ✅ 分享使用心得
            </li>
            <li style="padding:8px 0">
                ✅ 任何你想说的
            </li>
        </ul>
        
        <div style="background:var(--accent-light);border-radius:8px;padding:16px;margin-bottom:30px">
            <p style="font-size:14px;color:var(--accent)">
                💡 提示：评论需要 GitHub 账号，这是为了防止垃圾评论
            </p>
        </div>
        
        <div id="giscus-container">
            <!-- Giscus 评论区 -->
        </div>
    </div>
</div>
'''
    else:
        return '''
<div style="max-width:800px;margin:0 auto">
    <h1 style="font-size:32px;font-weight:800;margin-bottom:16px;text-align:center">
        💬 Feedback
    </h1>
    <p style="text-align:center;color:var(--text-secondary);margin-bottom:40px;font-size:18px">
        Share your thoughts! Suggest tools, report bugs, or just say hi
    </p>
    
    <div style="background:var(--bg-white);border-radius:var(--radius-lg);padding:40px;box-shadow:var(--shadow)">
        <h2 style="font-size:20px;font-weight:700;margin-bottom:20px">
            📝 What you can share:
        </h2>
        <ul style="list-style:none;margin-bottom:30px">
            <li style="padding:8px 0;border-bottom:1px solid var(--border-light)">
                ✅ Suggest new tools (tell me the name and website)
            </li>
            <li style="padding:8px 0;border-bottom:1px solid var(--border-light)">
                ✅ Report issues (broken links, wrong info, etc.)
            </li>
            <li style="padding:8px 0;border-bottom:1px solid var(--border-light)">
                ✅ Share your experience
            </li>
            <li style="padding:8px 0">
                ✅ Anything you want to say
            </li>
        </ul>
        
        <div style="background:var(--accent-light);border-radius:8px;padding:16px;margin-bottom:30px">
            <p style="font-size:14px;color:var(--accent)">
                💡 Note: Comments require a GitHub account to prevent spam
            </p>
        </div>
        
        <div id="giscus-container">
            <!-- Giscus comments -->
        </div>
    </div>
</div>
'''

def generate_feedback_page(lang):
    """生成留言板页面"""
    content = get_feedback_content(lang)
    giscus_script = get_giscus_script(lang)
    
    title = '留言板' if lang == 'zh' else 'Feedback'
    description = 'AIFreePlan 留言板 - 提建议、报Bug、分享心得' if lang == 'zh' else 'AIFreePlan Feedback - Suggestions, bug reports, and more'
    canonical_path = f'/{lang}/feedback'
    
    # 自定义 CSS
    custom_css = '''
#giscus-container {
    margin-top: 30px;
    min-height: 300px;
}
'''
    
    # 构建页面
    html = build_page(
        lang=lang,
        content=content,
        title=title,
        description=description,
        canonical_path=canonical_path,
        custom_css=custom_css,
        extra_scripts=giscus_script
    )
    
    return html

def main():
    """生成中英文留言板页面"""
    output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'dist')
    os.makedirs(output_dir, exist_ok=True)
    
    for lang in ['zh', 'en']:
        html = generate_feedback_page(lang)
        
        # 验证页面
        errors = validate_page(html)
        if errors:
            print(f'❌ {lang} 页面验证失败: {errors}')
            continue
        
        # 保存文件
        lang_dir = os.path.join(output_dir, lang)
        os.makedirs(lang_dir, exist_ok=True)
        filepath = os.path.join(lang_dir, 'feedback.html')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f'✅ {lang} 留言板页面已生成: {filepath}')

if __name__ == '__main__':
    main()
