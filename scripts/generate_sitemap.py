#!/usr/bin/env python3
"""Generate sitemap.xml for aifreeplan.com — SEO-optimized version"""
import json, os
from datetime import date

BASE = "https://aifreeplan.com"
TODAY = date.today().isoformat()

dist = os.path.join(os.path.dirname(__file__), "..", "dist")

# Load tools and guides data for real lastmod dates
tools_data = []
guides_data = []
for data_file in ["src/content/tools.json", "src/data/tools.json"]:
    path = os.path.join(os.path.dirname(__file__), "..", data_file)
    if os.path.exists(path):
        with open(path) as f:
            tools_data = json.load(f)
        break

for data_file in ["src/content/guides_all.json", "src/data/guides_all.json"]:
    path = os.path.join(os.path.dirname(__file__), "..", data_file)
    if os.path.exists(path):
        with open(path) as f:
            guides_data = json.load(f)
        break

# Build lookup: slug -> last_updated
tool_lastmod = {}
for t in tools_data:
    slug = t.get("slug", "")
    lastmod = t.get("last_updated", "") or TODAY
    if slug:
        tool_lastmod[slug] = lastmod

guide_lastmod = {}
for g in guides_data:
    slug = g.get("slug", "")
    lastmod = g.get("date_modified", "") or g.get("date_published", "") or TODAY
    if slug:
        guide_lastmod[slug] = lastmod

# Find all HTML files in dist
urls = []
for root, dirs, files in os.walk(dist):
    for f in files:
        if not f.endswith(".html"):
            continue
        path = os.path.join(root, f)
        rel = os.path.relpath(path, dist)
        # Convert file path to URL (no trailing slash)
        if rel == "index.html":
            url = BASE
        elif rel.endswith("/index.html"):
            url = f"{BASE}/{rel[:-11]}"
        elif rel.endswith(".html"):
            url = f"{BASE}/{rel[:-5]}"
        else:
            continue
        # Skip 404 page
        if "/404" in url:
            continue
        urls.append(url)

urls.sort()

# Determine priority and lastmod per URL
def get_priority(url):
    path = url.replace(BASE, "")
    # Homepage
    if path in ("", "/zh", "/en"):
        return "1.0"
    # Category index pages
    parts = path.strip("/").split("/")
    if len(parts) == 2:  # /zh/category or /en/category
        return "0.8"
    # Guides index
    if "/guides" in path and parts[-1] == "guides":
        return "0.8"
    # Privacy/terms
    if "/privacy" in path or "/terms" in path:
        return "0.3"
    # Tool detail and guide detail pages
    return "0.6"

def get_lastmod(url):
    path = url.replace(BASE, "").strip("/")
    parts = path.split("/")
    # Tool page: /zh/category/slug -> check tool_lastmod[slug]
    if len(parts) >= 3:
        slug = parts[-1]
        if slug in tool_lastmod:
            return tool_lastmod[slug]
        if slug in guide_lastmod:
            return guide_lastmod[slug]
    return TODAY

# Write sitemap
xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url in urls:
    priority = get_priority(url)
    lastmod = get_lastmod(url)
    xml += '  <url>\n'
    xml += f'    <loc>{url}</loc>\n'
    xml += f'    <lastmod>{lastmod}</lastmod>\n'
    xml += f'    <priority>{priority}</priority>\n'
    xml += '  </url>\n'
xml += '</urlset>\n'

sitemap_path = os.path.join(dist, "sitemap.xml")
with open(sitemap_path, "w") as f:
    f.write(xml)

print(f"Generated sitemap.xml with {len(urls)} URLs")
