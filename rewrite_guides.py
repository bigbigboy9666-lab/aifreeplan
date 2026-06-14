import os
import re
import sys

def extract_main_content(html):
    """Extract content between <main> and </main> tags"""
    match = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
    if match:
        return match.group(1)
    return None

def extract_h1(content):
    """Extract the h1 from main content"""
    match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL)
    if match:
        return match.group(1)
    return None

def has_heavy_lists(content):
    """Check if content has heavy list usage that needs rewriting"""
    li_count = content.count('<li>')
    ul_count = content.count('<ul>')
    ol_count = content.count('<ol>')
    return li_count > 5 or (ul_count + ol_count) > 2

def convert_ul_to_paragraphs(content):
    """Convert unordered list items to flowing paragraphs"""
    def replace_list(match):
        list_content = match.group(1)
        items = re.findall(r'<li>(.*?)</li>', list_content, re.DOTALL)
        if not items:
            return match.group(0)
        
        # Clean HTML from items
        cleaned = []
        for item in items:
            item = item.strip()
            item = re.sub(r'^<strong>(.*?)</strong>[:：]\s*', r'<strong>\1</strong>：', item)
            cleaned.append(item)
        
        if len(cleaned) <= 2:
            # Keep as list if very short
            return match.group(0)
        
        # Convert to paragraphs
        paragraphs = []
        for item in cleaned:
            # Remove list-style formatting, make it a sentence
            item_text = re.sub(r'<[^>]+>', '', item)  # strip tags for analysis
            if len(item_text) > 10:
                paragraphs.append(f'<p>{item}</p>')
            else:
                paragraphs.append(f'<p>{item}。</p>')
        
        return '\n'.join(paragraphs)
    
    # Only convert ul/ol that are NOT inside faq-section or table
    # Split content by sections to avoid converting FAQ lists
    parts = re.split(r'(<section class="faq|<section class="grid)', content)
    result_parts = []
    for i, part in enumerate(parts):
        if i == 0 or not part.startswith('<section class="faq') and not part.startswith('<section class="grid'):
            part = re.sub(r'<ul[^>]*>(.*?)</ul>', replace_list, part, flags=re.DOTALL)
            part = re.sub(r'<ol[^>]*>(.*?)</ol>', replace_list, part, flags=re.DOTALL)
        result_parts.append(part)
    
    return ''.join(result_parts)

def make_title_conversational(h1_text, filename):
    """Make h1 more conversational based on the topic"""
    # This is a heuristic - we'll apply general patterns
    return h1_text

def process_file(filepath, lang='zh'):
    """Process a single guide file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    content = extract_main_content(html)
    if not content:
        return False
    
    h1 = extract_h1(content)
    if not h1:
        return False
    
    filename = os.path.basename(filepath)
    
    # Skip if already narrative (very few lists)
    if not has_heavy_lists(content):
        print(f"  SKIP (already narrative): {filename}")
        return False
    
    print(f"  PROCESSING: {filename}")
    
    # Convert lists to paragraphs
    new_content = convert_ul_to_paragraphs(content)
    
    # Replace in full HTML
    new_html = html.replace(content, new_content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)
    
    return True

# Main
zh_dir = '/home/ubuntu/aifreeplan/zh/guides'
en_dir = '/home/ubuntu/aifreeplan/en/guides'

print("=== Processing Chinese guides ===")
zh_files = sorted([f for f in os.listdir(zh_dir) if f.endswith('.html') and f != 'hailuo-free-video.html'])
for f in zh_files:
    filepath = os.path.join(zh_dir, f)
    process_file(filepath, 'zh')

print("\n=== Processing English guides ===")
en_files = sorted([f for f in os.listdir(en_dir) if f.endswith('.html') and f != 'hailuo-free-video.html'])
for f in en_files:
    filepath = os.path.join(en_dir, f)
    process_file(filepath, 'en')

print("\nDone! Initial list-to-paragraph conversion complete.")
