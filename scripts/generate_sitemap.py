#!/usr/bin/env python3
"""Generate sitemap.xml for aifreeplan.com"""
import json, os
from datetime import date

BASE = "https://aifreeplan.com"
TODAY = date.today().isoformat()

# Load tools and guides data
dist = os.path.join(os.path.dirname(__file__), "..", "dist")

# Find all HTML files in dist to build sitemap
urls = []
for root, dirs, files in os.walk(dist):
    for f in files:
        if not f.endswith(".html"):
            continue
        path = os.path.join(root, f)
        rel = os.path.relpath(path, dist)
        # Convert file path to URL
        if rel == "index.html":
            url = f"{BASE}/"
        elif rel.endswith("/index.html"):
            url = f"{BASE}/{rel[:-11]}/"
        elif rel.endswith(".html"):
            url = f"{BASE}/{rel[:-5]}/"
        else:
            continue
        # Skip 404 page
        if "/404" in url:
            continue
        urls.append(url)

urls.sort()

# Write sitemap
xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url in urls:
    xml += f'  <url>\n'
    xml += f'    <loc>{url}</loc>\n'
    xml += f'    <lastmod>{TODAY}</lastmod>\n'
    xml += f'    <changefreq>weekly</changefreq>\n'
    xml += f'    <priority>0.7</priority>\n'
    xml += f'  </url>\n'
xml += '</urlset>\n'

sitemap_path = os.path.join(dist, "sitemap.xml")
with open(sitemap_path, "w") as f:
    f.write(xml)

print(f"Generated sitemap.xml with {len(urls)} URLs")
