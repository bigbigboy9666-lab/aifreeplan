#!/usr/bin/env python3
"""
事实核查脚本 v2：提取文章中的关键数字声明，与可信数据源交叉验证。

改进：只提取"额度相关"的数字，过滤分辨率、秒数、年份等误报。

用法：
  python3 scripts/fact_check.py                  # 检查所有文章
  python3 scripts/fact_check.py --slug xxx       # 检查指定文章
  python3 scripts/fact_check.py --strict         # 严格模式（阈值更低）
"""
import json
import re
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FACTS_FILE = os.path.join(SCRIPT_DIR, 'verified_facts.json')
GUIDES_FILE = os.path.join(os.path.dirname(SCRIPT_DIR), 'src/content/guides.json')

# 工具名→基准数据key映射
TOOL_DETECT = {
    'chatgpt': ['ChatGPT'],
    'claude': ['Claude'],
    'gemini': ['Gemini'],
    'deepseek': ['DeepSeek'],
    'kimi': ['Kimi'],
    'tongyi_qianwen': ['通义千问', 'Qwen'],
    'doubao': ['豆包'],
    'suno': ['Suno'],
    'kling': ['可灵', 'Kling'],
    'hailuo': ['海螺', 'Hailuo'],
    'pixverse': ['PixVerse'],
    'gamma': ['Gamma'],
    'coze': ['Coze', '扣子'],
    'cursor': ['Cursor'],
    'windsurf': ['Windsurf'],
    'github_copilot': ['GitHub Copilot'],
    'perplexity': ['Perplexity'],
    'notebooklm': ['NotebookLM'],
    'ideogram': ['Ideogram'],
    'leonardo_ai': ['Leonardo AI'],
    'manus_ai': ['Manus AI'],
    'poe': ['Poe'],
    'cline': ['Cline'],
}

# 应该被过滤的数字（不是额度数据）
EXCLUDE_NUMBERS = {
    '1080', '720', '4K', '512', '1024', '2048', '4096',  # 分辨率
    '2022', '2023', '2024', '2025', '2026', '2027',       # 年份
    '200K', '128K', '64K',                                  # 上下文窗口
    '44', '300', '500', '630', '1200',                      # CSS/图片尺寸
    '360', '768',                                            # 屏幕宽度
    '90K',                                                   # GitHub stars
}

# 精确匹配模式：只提取"每日/免费/注册送 + 数字 + 额度单位"的声明
PRECISE_PATTERNS = [
    # 中文模式
    (r'每天[约]?\s*(\d+)\s*积分', 'daily_credits', '积分'),
    (r'每日[约]?\s*(\d+)\s*积分', 'daily_credits', '积分'),
    (r'每天[约]?\s*(\d+)\s*张', 'daily_images', '张'),
    (r'每天[约]?\s*(\d+)\s*首', 'daily_songs', '首'),
    (r'每天[约]?\s*(\d+)\s*次', 'daily_limit', '次'),
    (r'每月[约]?\s*(\d+)\s*次', 'monthly_limit', '次'),
    (r'每月[约]?\s*(\d+)\s*积分', 'monthly_credits', '积分'),
    (r'注册[送]?\s*(\d+)\s*积分', 'signup_credits', '积分'),
    (r'注册[送]?\s*(\d+)\s*token', 'signup_tokens', 'token'),
    (r'每天\s*(\d+)\s*万\s*token', 'daily_tokens_wan', '万token'),
    (r'每天[约]?\s*(\d+)\s*个?', 'daily_credits', '个'),
    # 英文模式
    (r'(\d+)\s*credits?/day', 'daily_credits', 'credits'),
    (r'(\d+)\s*free credits', 'daily_credits', 'credits'),
    (r'daily\s*(\d+)\s*credits?', 'daily_credits', 'credits'),
    (r'(\d+)\s*completions?\s*(?:per|/)\s*month', 'monthly_completions', 'completions'),
    (r'\$(\d+(?:\.\d+)?)\s*/?\s*(?:month|mo)', 'price_usd', 'USD/月'),
    (r'(\d+)\s*CNY\s*/?\s*(?:month|月)', 'price_cny', 'CNY/月'),
    (r'(\d+)\s*元\s*/?\s*[月年]', 'price_cny', 'CNY/月'),
]


def load_facts():
    with open(FACTS_FILE, 'r') as f:
        return json.load(f)


def detect_tools(text):
    """检测文章中提到的工具"""
    found = {}
    text_lower = text.lower()
    for tool_id, aliases in TOOL_DETECT.items():
        for alias in aliases:
            if alias.lower() in text_lower:
                found[tool_id] = alias
                break
    return found


def extract_precise_claims(text, tool_id, tool_aliases):
    """提取精确的额度/价格声明"""
    claims = []
    lines = text.split('\n')
    
    for line in lines:
        # 只处理包含该工具名的行
        if not any(a.lower() in line.lower() for a in tool_aliases):
            continue
        
        # 应用精确匹配模式
        for pattern, claim_type, unit in PRECISE_PATTERNS:
            for m in re.finditer(pattern, line, re.IGNORECASE):
                num = m.group(1)
                
                # 排除已知误报
                if num in EXCLUDE_NUMBERS:
                    continue
                
                # 排除分辨率（数字后跟p）
                if re.search(rf'{num}p', line):
                    continue
                
                # 排除秒数
                if re.search(rf'{num}\s*秒', line):
                    continue
                
                claims.append({
                    'tool': tool_id,
                    'type': claim_type,
                    'number': num,
                    'unit': unit,
                    'context': line.strip()[:120],
                })
    
    return claims


def verify_claims(claims, facts):
    """将提取的声明与基准数据对比"""
    warnings = []
    
    for claim in claims:
        tool_id = claim['tool']
        tool_facts = facts.get('tools', {}).get(tool_id)
        if not tool_facts:
            continue
        
        free_tier = tool_facts.get('free_tier', {})
        num = claim['number']
        claim_type = claim['type']
        
        # 按声明类型对比基准数据
        expected = None
        field = None
        
        if claim_type == 'daily_credits':
            field = 'daily_credits'
            expected = free_tier.get('daily_credits')
        elif claim_type == 'daily_images':
            field = 'daily_images'
            expected = free_tier.get('daily_images')
        elif claim_type == 'signup_credits':
            field = 'signup_credits'
            expected = free_tier.get('signup_credits')
        elif claim_type == 'daily_songs':
            field = 'daily_songs'
            expected = free_tier.get('daily_songs')
        elif claim_type == 'price_usd':
            # 对比所有付费档
            for tier in tool_facts.get('paid_tiers', []):
                if 'price_usd' in tier:
                    if abs(float(num) - tier['price_usd']) < 0.01:
                        expected = str(tier['price_usd'])
                        field = f'price_{tier["name"]}'
                        break
        
        if expected is None:
            continue  # 基准数据没有这个字段，跳过
        
        expected_str = str(expected).replace('约', '')
        
        # 数字不匹配
        if num != expected_str:
            # 特殊处理：范围值（如"66-100"）
            if '-' in expected_str:
                range_parts = expected_str.split('-')
                try:
                    if float(range_parts[0]) <= float(num) <= float(range_parts[1]):
                        continue  # 在范围内，不算错
                except ValueError:
                    pass
            
            # 特殊处理："约X张"格式
            if '约' in str(expected):
                try:
                    if abs(int(num) - int(expected_str.replace('约', ''))) <= 5:
                        continue  # 差距不大，不算错
                except ValueError:
                    pass
            
            warnings.append({
                'tool': tool_facts.get('name_zh', tool_id),
                'claim_type': claim_type,
                'article_says': num,
                'expected': str(expected),
                'source': free_tier.get('source', '未知'),
                'context': claim['context'],
            })
    
    return warnings


def fact_check(slug=None, strict=False):
    """执行事实核查"""
    facts = load_facts()
    with open(GUIDES_FILE, 'r') as f:
        guides = json.load(f)
    
    all_warnings = []
    checked = 0
    
    for g in guides:
        if slug and g['slug'] != slug:
            continue
        
        content = g.get('content_zh', '')
        if not content:
            continue
        
        tools = detect_tools(content)
        for tool_id, alias in tools.items():
            aliases = TOOL_DETECT.get(tool_id, [alias])
            claims = extract_precise_claims(content, tool_id, aliases)
            warnings = verify_claims(claims, facts)
            for w in warnings:
                w['slug'] = g['slug']
                all_warnings.append(w)
        checked += 1
    
    return all_warnings, checked


def main():
    args = sys.argv[1:]
    slug = None
    strict = '--strict' in args
    
    if '--slug' in args:
        idx = args.index('--slug')
        if idx + 1 < len(args):
            slug = args[idx + 1]
        else:
            print("用法: python3 fact_check.py --slug <slug>")
            return 1
    
    warnings, checked = fact_check(slug=slug, strict=strict)
    
    print(f"检查了 {checked} 篇文章\n")
    
    if not warnings:
        print("✅ 事实核查通过，关键数字与基准数据一致")
        return 0
    
    # 按文章分组
    by_slug = {}
    for w in warnings:
        s = w['slug']
        if s not in by_slug:
            by_slug[s] = []
        by_slug[s].append(w)
    
    print(f"⚠️  发现 {len(warnings)} 处数据不匹配，涉及 {len(by_slug)} 篇文章：\n")
    
    for slug, items in by_slug.items():
        print(f"📄 {slug}")
        for w in items:
            print(f"   {w['tool']}: 文章说'{w['article_says']}', 基准说'{w['expected']}'")
            print(f"   类型: {w['claim_type']} | 来源: {w['source']}")
            print(f"   上下文: ...{w['context'][:60]}...")
        print()
    
    return 1 if len(warnings) > 5 else 0


if __name__ == '__main__':
    sys.exit(main())
