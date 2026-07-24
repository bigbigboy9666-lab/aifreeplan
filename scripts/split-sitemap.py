#!/usr/bin/env python3
"""Split sitemap into multiple sub-sitemaps + index file for aifreeplan.com"""
import json, os, re
from datetime import datetime

BASE = '/home/ubuntu/aifreeplan'
PUBLIC = os.path.join(BASE, 'public')

# Read the giant sitemap
with open(os.path.join(PUBLIC, 'sitemap.xml'), 'r') as f:
    raw = f.read()

# Extract all URLs
url_pattern = re.compile(r'<ns0:url>(.*?)</ns0:url>', re.DOTALL)
matches = url_pattern.findall(raw)

urls_by_type = {
    'pages': [],      # homepage, categories, guides list
    'tools': [],      # tool detail pages
    'guides': [],     # guide articles
    'compare': [],    # comparison pages (will be noindexed)
}

for m in matches:
    loc_match = re.search(r'<ns0:loc>(.*?)</ns0:loc>', m)
    if not loc_match:
        continue
    loc = loc_match.group(1).strip()
    
    if '/compare/' in loc:
        urls_by_type['compare'].append(loc)
    elif '/guides/' in loc and not loc.endswith('/guides/'):
        urls_by_type['guides'].append(loc)
    elif '/tools/' in loc and not loc.endswith('/tools/'):
        urls_by_type['tools'].append(loc)
    else:
        urls_by_type['pages'].append(loc)

print(f"Total URLs: {sum(len(v) for v in urls_by_type.values())}")
for k, v in urls_by_type.items():
    print(f"  {k}: {len(v)}")

def make_sitemap_xml(urls, filename):
    """Generate a proper sitemap XML with lastmod"""
    today = datetime.now().strftime('%Y-%m-%d')
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in sorted(urls):
        xml += f'  <url>\n    <loc>{url}</loc>\n    <lastmod>{today}</lastmod>\n  </url>\n'
    xml += '</urlset>'
    return xml

# Write sub-sitemaps (max 50K per sitemap, we're well under)
for type_name, urls in urls_by_type.items():
    if not urls:
        continue
    filename = f'sitemap-{type_name}.xml'
    content = make_sitemap_xml(urls, filename)
    path = os.path.join(PUBLIC, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Wrote {path}: {len(urls)} URLs, {os.path.getsize(path)} bytes")

# Write sitemap index
today = datetime.now().strftime('%Y-%m-%d')
index_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
index_xml += '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for type_name in ['pages', 'tools', 'guides', 'compare']:
    url = f'https://aifreeplan.com/sitemap-{type_name}.xml'
    index_xml += f'  <sitemap>\n    <loc>{url}</loc>\n    <lastmod>{today}</lastmod>\n  </sitemap>\n'
index_xml += '</sitemapindex>'

index_path = os.path.join(PUBLIC, 'sitemap.xml')
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_xml)
print(f"\nWrote {index_path}: sitemap index ({os.path.getsize(index_path)} bytes)")

# Update robots.txt to point to new sitemap
robots_path = os.path.join(PUBLIC, 'robots.txt')
with open(robots_path, 'r') as f:
    robots = f.read()

robots = robots.replace('Sitemap: https://aifreeplan.com/sitemap.xml', 
                        'Sitemap: https://aifreeplan.com/sitemap.xml')
# The index IS sitemap.xml now, so no change needed

with open(robots_path, 'w') as f:
    f.write(robots)

print("\nDone! Sitemap split complete.")
