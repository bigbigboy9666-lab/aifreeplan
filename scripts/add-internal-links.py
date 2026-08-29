#!/usr/bin/env python3
"""
Auto-add internal links to English guide articles.

For each /en/guides/{slug}.html:
  1. Extract tool/guide names mentioned in the article body
  2. Find matching tool slugs in public/data/tools.json
  3. Wrap the first occurrence of each tool name with a link to /en/tools/{slug}/
  4. Also add a "Related guides" section near the end linking to other guides
     that share >=2 tool mentions

Idempotent: skips already-linked names and doesn't double-wrap.

Usage:
  python3 scripts/add-internal-links.py            # process all en/guides
  python3 scripts/add-internal-links.py --dry-run  # show what would change
"""
import os, re, json, glob, sys
from collections import Counter, defaultdict

ROOT = '/home/ubuntu/aifreeplan'
EN_GUIDES = os.path.join(ROOT, 'en/guides')
TOOLS_JSON = os.path.join(ROOT, 'public/data/tools.json')
GUIDES_JSON = os.path.join(ROOT, 'public/data/guides.json')

# Tool name aliases — covers common variants in articles
ALIASES = {
    'chatgpt':        ['ChatGPT', 'GPT-4o', 'GPT-5', 'GPT-3.5', 'GPT-4'],
    'claude':         ['Claude', 'Claude 4', 'Claude 3', 'Claude Sonnet', 'Claude Opus', 'Claude Code'],
    'gemini':         ['Gemini', 'Gemini 3', 'Gemini 2.5', 'Gemini 2'],
    'deepseek':       ['DeepSeek', 'DeepSeek V4', 'DeepSeek V3', 'DeepSeek R1', 'DeepSeek-V3'],
    'qwen':           ['Qwen', 'Qwen3', 'Qwen 3', 'Tongyi Qianwen', '通义千问'],
    'kling':          ['Kling', 'Kling AI', '可灵'],
    'cursor':         ['Cursor'],
    'suno':           ['Suno'],
    'midjourney':     ['Midjourney'],
    'runway':         ['Runway', 'Gen-3', 'Gen-4'],
    'pika':           ['Pika'],
    'sora':           ['Sora', 'Sora 2'],
    'hailuo':         ['Hailuo', '海螺', 'MiniMax Hailuo'],
    'luma':           ['Luma', 'Dream Machine'],
    'doubao':         ['Doubao', '豆包'],
    'wenxin':         ['Wenxin', 'ERNIE', '文心一言'],
    'kimi':           ['Kimi', 'Kimi K2', 'Kimi K3'],
    'grok':           ['Grok', 'Grok 4'],
    'coze':           ['Coze', '扣子'],
    'poe':            ['Poe'],
    'perplexity':     ['Perplexity'],
    'mistral':        ['Mistral'],
    'llama':          ['Llama', 'Llama 4', 'Llama 3'],
    'dify':           ['Dify'],
    'groq':           ['Groq'],
    'huggingface':    ['Hugging Face', 'HuggingFace'],
    'elevenlabs':     ['ElevenLabs', 'Eleven Labs'],
    'gamma':          ['Gamma'],
    'notebooklm':     ['NotebookLM', 'Notebook LM'],
    'github-copilot': ['GitHub Copilot', 'Copilot'],
    'windsurf':       ['Windsurf'],
    'codebuddy':      ['CodeBuddy'],
    'stablediffusion':['Stable Diffusion', 'SD', 'SDXL'],
    'comfyui':        ['ComfyUI', 'Comfy UI'],
    'langchain':      ['LangChain'],
    'n8n':            ['n8n'],
    'zapier':         ['Zapier'],
    'make':           ['Make', 'Make.com'],
    'feishu-minutes': ['Feishu Minutes', '飞书妙记'],
    'wps-ai':         ['WPS AI'],
    'baidu-netdisk-ai':['Baidu Netdisk AI', '百度网盘 AI'],
    'tencent-marvis': ['Marvis', '腾讯 Marvis'],
    'xiaomi-mimo':    ['MiMo', 'Xiaomi MiMo', '小米 MiMo'],
    'zhipu':          ['Zhipu', 'GLM', 'ChatGLM', '智谱'],
    'baidu-qianfan':  ['Qianfan', '千帆'],
    'aliyun-bailian': ['Bailian', '百炼', 'Tongyi'],
    'ppio':           ['PPIO'],
    'baishan':        ['Baishan', '白山云'],
    'scnet':          ['SCNet', '国家超算'],
    'teleai':         ['TeleAI', '天翼 AI'],
    'infini-ai':      ['InfiniAI', '无问芯穹'],
    'meituan-longcat':['LongCat', '美团 LongCat'],
    'china-mobile-moma':['MoMA', '中国移动 MoMA'],
    'apfel':          ['Apfel'],
    'ollama':         ['Ollama'],
    'lm-studio':      ['LM Studio'],
    'petals':         ['Petals'],
    'manus':          ['Manus', 'Manus AI'],
    'qwen-cua':       ['Qwen-CUA', 'Qwen CUA'],
    'airllm':         ['AirLLM'],
    'atomcode':       ['AtomCode'],
    'qoderwork':      ['QoderWork', 'Qoder'],
    'trae':           ['Trae'],
    'freebuff':       ['FreeBuff'],
    'deepsider':      ['Deepsider'],
    'gemini-cli':     ['Gemini CLI'],
    'kimi-k26':       ['Kimi K2.6', 'Kimi-K2.6'],
    'huawei-deveco':  ['DevEco', 'Huawei DevEco', '华为 DevEco'],
    'claude-opus-5':  ['Claude Opus 5', 'Opus 5'],
    'freebuff-coding':['FreeBuff'],
    'rime-ai-voice':  ['Rime', 'Rime AI'],
    'ego-lite':       ['Ego Lite', 'EgoLite'],
    'llm-admin':      ['LLM Admin', 'llm-admin'],
    'sensenova':      ['SenseNova', '商汤', 'SenseTime'],
    'nano-banana':    ['Nano Banana', 'nano-banana'],
    'bonsai-27b':     ['Bonsai', 'Bonsai 27B'],
    'libtv':          ['LibTV', 'LibTV AI'],
    'dumate':         ['Dumate', '百度桌面 AI'],
    'monkeycode':     ['MonkeyCode', 'monkeyCode'],
    'proliferate':    ['Proliferate', 'Proliferate AI'],
    'inkling':        ['Inkling'],
    'nativ':          ['Nativ'],
    'ringbot':        ['Ringbot', 'Ringbot AI'],
    'qwen3-6':        ['Qwen3-6', 'Qwen 3.6'],
    'seedance-2':     ['Seedance', 'Seedance 2.0'],
    'yolo-auto':      ['YOLO Auto', 'yolo-auto'],
    'bolt-gives':     ['Bolt', 'Bolt.new'],
    'jetbrains-go':   ['JetBrains AI', 'Go AI'],
    'mistral-studio': ['Mistral Studio', 'Le Plateforme'],
    'amazon-q':       ['Amazon Q', 'Q Developer'],
    'cerebras':       ['Cerebras'],
    'cursor-origin':  ['Cursor Origin'],
    'jetbrains-ai':   ['JetBrains AI'],
    'minimax-m3':     ['MiniMax-M3', 'MiniMax M3'],
}


def load_tools():
    with open(TOOLS_JSON) as f:
        data = json.load(f)
    return data['tools']


def load_guides():
    with open(GUIDES_JSON) as f:
        data = json.load(f)
    return data['guides']


def build_tool_matchers(tools):
    """Build regex -> (slug, canonical_name) map for all tool names + aliases."""
    matcher_to_slug = []
    for t in tools:
        tid = t['id']
        names = []
        # nameEn first (most reliable for English articles)
        if t.get('nameEn'):
            names.append(t['nameEn'])
        if t.get('name') and t['name'] != t.get('nameEn'):
            names.append(t['name'])
        # Then aliases
        for a in ALIASES.get(tid, []):
            if a not in names:
                names.append(a)

        for n in names:
            if not n or len(n) < 2:
                continue
            # Escape regex, use word boundary
            pattern = re.compile(r'\b' + re.escape(n) + r'\b', re.IGNORECASE)
            matcher_to_slug.append((pattern, tid, n))
    return matcher_to_slug


def add_links_to_guide(filepath, tools, guides, dry_run=False):
    """Add internal links to a single guide. Returns (added_count, content_changed)."""
    with open(filepath) as f:
        html = f.read()

    # Skip if already extensively linked (>=3 tool/guide links)
    existing_tool_links = re.findall(r'href="/en/tools/[^"]+"', html)
    existing_guide_links = re.findall(r'href="/en/guides/[^"]+"', html)
    if len(existing_tool_links) + len(existing_guide_links) >= 3:
        return 0, False  # Already well-linked

    # Find body content (skip <head>, skip existing <a> content)
    body_match = re.search(r'<body[^>]*>(.*?)</body>', html, re.DOTALL)
    if not body_match:
        return 0, False
    body = body_match.group(1)

    # Build matchers
    matchers = build_tool_matchers(tools)
    # Sort by name length desc so longer matches (e.g. "GPT-4o") win over shorter ("GPT")
    matchers.sort(key=lambda x: -len(x[2]))

    # Find first occurrence of each tool in body, replace plain text with link
    added = 0
    new_body = body
    seen_slugs = set()  # don't link same tool twice
    for pattern, slug, name in matchers:
        if slug in seen_slugs:
            continue
        # Find first non-linked occurrence
        # Use a function to skip if already inside an <a> tag
        def replacer(match):
            nonlocal added
            # Check if inside an <a> tag (look behind for <a ... >)
            start = match.start()
            preceding = new_body[max(0, start-200):start]
            # If the last unclosed <a> tag precedes this match, skip
            last_a_open = preceding.rfind('<a ')
            last_a_close = preceding.rfind('</a>')
            if last_a_open > last_a_close:
                return match.group(0)
            added += 1
            return f'<a href="/en/tools/{slug}/">{match.group(0)}</a>'

        new_body, n = pattern.subn(replacer, new_body, count=1)
        if n > 0:
            seen_slugs.add(slug)

    if added == 0:
        return 0, False

    # Also build "Related guides" section if not present
    has_related = bool(re.search(r'<(?:h2|h3)[^>]*>\s*(?:Related|See also|Recommended)', new_body, re.IGNORECASE))
    if not has_related and len(seen_slugs) >= 2:
        # Find other guides that mention >=2 of our linked tools
        # Use guides.json metadata
        my_slug = os.path.basename(filepath).replace('.html', '')
        related = []
        for g in guides:
            if g.get('slug') == my_slug:
                continue
            # Count tool mentions in this guide's content
            content = (g.get('content_en') or '') + ' ' + (g.get('content_zh') or '')
            shared = sum(1 for slug in seen_slugs if slug in content or any(
                a.lower() in content.lower() for a in [slug] + ALIASES.get(slug, [])
            ))
            if shared >= 2:
                related.append((g['slug'], g.get('title_en', g.get('title_zh', g['slug'])), shared))
        related.sort(key=lambda x: -x[2])
        related = related[:5]

        if related:
            related_html = '\n<h2>Related Guides</h2>\n<ul>\n'
            for slug, title, _ in related:
                related_html += f'  <li><a href="/en/guides/{slug}/">{title}</a></li>\n'
            related_html += '</ul>\n'
            # Insert before </body>... but body_match already captured it; rebuild
            new_body = new_body + related_html

    new_html = html[:body_match.start(1)] + new_body + html[body_match.end(1):]

    if dry_run:
        return added, True
    else:
        with open(filepath, 'w') as f:
            f.write(new_html)
        return added, True


def main():
    dry_run = '--dry-run' in sys.argv
    tools = load_tools()
    guides = load_guides()

    guide_files = sorted([
        f for f in glob.glob(os.path.join(EN_GUIDES, '*.html'))
        if not f.endswith('/index.html')
    ])

    total_added = 0
    files_changed = 0
    for fp in guide_files:
        added, changed = add_links_to_guide(fp, tools, guides, dry_run=dry_run)
        if added > 0:
            total_added += added
            files_changed += 1
            print(f'  {os.path.basename(fp)}: +{added} links')

    print(f'\n=== {"DRY RUN" if dry_run else "APPLIED"} ===')
    print(f'Files changed: {files_changed}')
    print(f'Links added: {total_added}')


if __name__ == '__main__':
    main()
