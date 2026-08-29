#!/usr/bin/env python3
"""Split sitemap into multiple sub-sitemaps + index file for aifreeplan.com

lastmod is now per-URL based on the source HTML file's actual mtime, so each URL
reflects when its content last changed. This stops search engines from treating
the whole site as stale just because the sitemap regen date didn't change.
"""
import json, os, re, glob
from datetime import datetime, timezone

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


def url_to_source_path(url: str):
    """Map a sitemap URL to the source HTML file path on disk.

    /zh/tools/kling/        -> zh/tools/kling/index.html
    /en/guides/foo/         -> en/guides/foo.html
    /zh/                    -> zh/index.html

    Returns None if no source file can be located.
    """
    path = url.replace('https://aifreeplan.com', '')
    if path == '' or path == '/':
        return None  # root: no source file
    # strip leading slash, normalize trailing slash
    if path.startswith('/'):
        path = path[1:]
    if path.endswith('/'):
        path = path + 'index.html'
        candidate = os.path.join(PUBLIC, path)
        if os.path.exists(candidate):
            return candidate
        # also try dist/ (post-build)
        candidate = os.path.join(BASE, 'dist', path)
        if os.path.exists(candidate):
            return candidate
    else:
        # try as a file with .html
        candidate = os.path.join(PUBLIC, path + '.html')
        if os.path.exists(candidate):
            return candidate
        # also try dist/
        candidate = os.path.join(BASE, 'dist', path + '.html')
        if os.path.exists(candidate):
            return candidate
    return None


def get_lastmod(url: str) -> str:
    """Get lastmod date for a URL based on source file mtime.

    Fallback chain:
      1. dist/ source HTML mtime (post-build, most accurate)
      2. public/ source HTML mtime
      3. Today (only if no source file found — should be rare)
    """
    src = url_to_source_path(url)
    if src and os.path.exists(src):
        mtime = os.path.getmtime(src)
        return datetime.fromtimestamp(mtime, tz=timezone.utc).strftime('%Y-%m-%d')
    # Fallback: also check src/ pages for the SSR templates
    return datetime.now(tz=timezone.utc).strftime('%Y-%m-%d')


def make_sitemap_xml(urls, filename):
    """Generate a proper sitemap XML with per-URL lastmod."""
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in sorted(urls):
        lastmod = get_lastmod(url)
        xml += f'  <url>\n    <loc>{url}</loc>\n    <lastmod>{lastmod}</lastmod>\n  </url>\n'
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
    lastmods = re.findall(r'<lastmod>([^<]+)</lastmod>', content)
    from collections import Counter
    lm_dist = Counter(lastmods)
    print(f"Wrote {path}: {len(urls)} URLs, {os.path.getsize(path)} bytes")
    print(f"  lastmod 分布: {dict(lm_dist.most_common(5))}")

# Write sitemap index — index lastmod = today (signals sitemap was regenerated)
today = datetime.now(tz=timezone.utc).strftime('%Y-%m-%d')
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

print("\nDone! Sitemap split complete with per-URL lastmod from source mtime.")
