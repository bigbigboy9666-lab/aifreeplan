#!/usr/bin/env python3
"""
aifreeplan.com 文章质检脚本
每次发布前必须运行，拦截以下问题：
1. 把aifreeplan.com当成AI工具来吹（最严重）
2. 文章缺少必填字段
3. 中英文内容不一致
4. FAQ缺失
5. 内链缺失
"""
import json
import re
import sys

GUIDES_FILE = '/home/ubuntu/aifreeplan/src/content/guides.json'

# ========== 检查规则 ==========

# P0 致命：把aifreeplan.com当成AI工具吹
FABRICATED_PRODUCT_PATTERNS = [
    # 直接说aifreeplan有某个产品功能
    r'aifreeplan\.com的免费\w+平台',
    r'aifreeplan\.com的AI\w+工具',
    r'aifreeplan\.com的免费AI',
    r'aifreeplan\.com的\w+生成器',
    r'aifreeplan\.com的\w+分析',
    r'aifreeplan\.com的\w+助手',
    r'aifreeplan\.com的\w+搜索',
    r'aifreeplan\.com的\w+摘要',
    r'aifreeplan\.com的策略',
    # 把AI Free Plan当成产品名
    r'AI Free Plan是.*搜索引擎',
    r'AI Free Plan是.*工具',
    r'AI Free Plan是.*平台',
    r'AI Free Plan的搜索',
    r'AI Free Plan的分析',
    # 编造不存在的产品名
    r'智文快摘',
    r'免费AI简历生成器来帮',
    # 说aifreeplan能做什么实际功能
    r'在aifreeplan\.com上.*分析数据',
    r'用aifreeplan\.com.*生成',
    r'aifreeplan\.com.*全功能开放',
    r'aifreeplan\.com.*核心功能全开放',
    r'aifreeplan\.com.*完全免费.*生成',
    # 第一人称吹aifreeplan
    r'我是aifreeplan\.com的',
    r'aifreeplan\.com就是那个',
    r'aifreeplan\.com就像那个',
    r'aifreeplan\.com绝对是首选',
    r'aifreeplan\.com绝对是王者',
    r'闭眼选aifreeplan',
    r'推荐.*aifreeplan\.com',
]

# P1 高优先：数据准确性问题
SUSPICIOUS_PATTERNS = [
    # 过时的模型名（2026年不应该出现）
    (r'GPT-3\.5\s*Turbo', 'GPT-3.5 Turbo已过时，2026年免费版用的是GPT-4o-mini'),
    # 自相矛盾的额度（同一工具在不同文章里数字不一致）
    # 这个需要交叉检查，单篇文章内检测不到
]

# P2 中优先：SEO和结构问题
REQUIRED_FIELDS = [
    'slug', 'title_zh', 'title_en', 'content_zh', 'content_en',
    'description_zh', 'description_en', 'date_published',
    'tags_zh', 'tags_en', 'faq_zh', 'faq_en',
]


def check_fabricated_products(guides):
    """检查是否把aifreeplan.com当成AI工具来吹"""
    issues = []
    for g in guides:
        slug = g['slug']
        for lang in ['content_zh', 'content_en']:
            content = g.get(lang, '')
            if not content:
                continue
            for pattern in FABRICATED_PRODUCT_PATTERNS:
                matches = re.findall(pattern, content, re.IGNORECASE)
                if matches:
                    # 找到匹配的上下文
                    for match in matches:
                        # 找匹配位置的上下文
                        idx = content.find(match)
                        start = max(0, idx - 50)
                        end = min(len(content), idx + len(match) + 50)
                        context = content[start:end].replace('\n', ' ').strip()
                        issues.append({
                            'severity': 'P0',
                            'slug': slug,
                            'lang': lang,
                            'pattern': pattern,
                            'match': match,
                            'context': context,
                        })
    return issues


def check_suspicious_content(guides):
    """检查可疑内容"""
    issues = []
    for g in guides:
        slug = g['slug']
        for lang in ['content_zh', 'content_en']:
            content = g.get(lang, '')
            if not content:
                continue
            for pattern, msg in SUSPICIOUS_PATTERNS:
                if re.search(pattern, content, re.IGNORECASE):
                    issues.append({
                        'severity': 'P1',
                        'slug': slug,
                        'lang': lang,
                        'message': msg,
                    })
    return issues


def check_required_fields(guides):
    """检查必填字段"""
    issues = []
    for g in guides:
        slug = g.get('slug', '?')
        for field in REQUIRED_FIELDS:
            val = g.get(field)
            if val is None:
                issues.append({
                    'severity': 'P1',
                    'slug': slug,
                    'message': f'缺少必填字段: {field}',
                })
            elif isinstance(val, str) and not val.strip():
                issues.append({
                    'severity': 'P2',
                    'slug': slug,
                    'message': f'字段为空: {field}',
                })
            elif isinstance(val, list) and len(val) == 0:
                if field in ['faq_zh', 'faq_en']:
                    issues.append({
                        'severity': 'P2',
                        'slug': slug,
                        'message': f'FAQ为空: {field}',
                    })
    return issues


def check_consistency(guides):
    """检查中英文一致性"""
    issues = []
    for g in guides:
        slug = g.get('slug', '?')
        zh = g.get('content_zh', '')
        en = g.get('content_en', '')
        if zh and not en:
            issues.append({
                'severity': 'P1',
                'slug': slug,
                'message': '有中文内容但缺少英文版',
            })
        elif en and not zh:
            issues.append({
                'severity': 'P1',
                'slug': slug,
                'message': '有英文内容但缺少中文版',
            })
        # 检查图片数量是否一致
        zh_imgs = len(re.findall(r'!\[.*?\]\(.*?\)', zh))
        en_imgs = len(re.findall(r'!\[.*?\]\(.*?\)', en))
        if zh_imgs != en_imgs and zh_imgs > 0 and en_imgs > 0:
            issues.append({
                'severity': 'P2',
                'slug': slug,
                'message': f'中英文图片数量不一致: zh={zh_imgs} en={en_imgs}',
            })
    return issues


def main():
    with open(GUIDES_FILE, 'r') as f:
        guides = json.load(f)

    print(f"质检 {len(guides)} 篇攻略\n")

    all_issues = []
    all_issues.extend(check_fabricated_products(guides))
    all_issues.extend(check_suspicious_content(guides))
    all_issues.extend(check_required_fields(guides))
    all_issues.extend(check_consistency(guides))

    # 按严重度排序
    severity_order = {'P0': 0, 'P1': 1, 'P2': 2}
    all_issues.sort(key=lambda x: severity_order.get(x['severity'], 99))

    p0 = [i for i in all_issues if i['severity'] == 'P0']
    p1 = [i for i in all_issues if i['severity'] == 'P1']
    p2 = [i for i in all_issues if i['severity'] == 'P2']

    if p0:
        print(f"🚨 P0 致命问题: {len(p0)} 个")
        for issue in p0:
            print(f"  [{issue['severity']}] {issue['slug']}")
            if 'match' in issue:
                print(f"    匹配: {issue['match']}")
                print(f"    上下文: ...{issue['context']}...")
            elif 'message' in issue:
                print(f"    {issue['message']}")
        print()

    if p1:
        print(f"⚠️  P1 高优先: {len(p1)} 个")
        for issue in p1:
            print(f"  [{issue['severity']}] {issue['slug']}: {issue.get('message', issue.get('pattern', ''))}")
        print()

    if p2:
        print(f"📋 P2 中优先: {len(p2)} 个")
        for issue in p2:
            print(f"  [{issue['severity']}] {issue['slug']}: {issue.get('message', '')}")
        print()

    if not all_issues:
        print("✅ 全部通过，没有发现问题")
        return 0

    print(f"\n总计: {len(p0)} 致命 / {len(p1)} 高优先 / {len(p2)} 中优先")

    if p0:
        print("\n❌ 有P0问题，不允许发布！")
        return 1
    elif p1:
        print("\n⚠️  有P1问题，建议修复后再发布")
        return 0
    else:
        print("\n✅ 只有P2问题，可以发布")
        return 0


if __name__ == '__main__':
    sys.exit(main())
