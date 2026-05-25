#!/usr/bin/env python3
"""Generate sitemap.xml for aifreeplan.com"""
import os
from datetime import date

BASE = "https://aifreeplan.com"
TODAY = date.today().isoformat()
dist = os.path.join(os.path.dirname(__file__), "..", "dist")

urls = []
for root, dirs, files in os.walk(dist):
    for f in files:
        if not f.endswith(".html"):
            continue
        path = os.path.join(root, f)
        rel = os.path.relpath(path, dist)
        if rel == "index.html":
            url = f"{BASE}/"
        elif rel.endswith("/index.html"):
            url = f"{BASE}/{rel[:-11]}/"
        elif rel.endswith(".html"):
            url = f"{BASE}/{rel[:-5]}/"
        else:
            continue
        if "/404" in url:
            continue
        urls.append(url)

urls.sort()

lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
]
for url in urls:
    lines.append("  <url>")
    lines.append(f"    <loc>{url}</loc>")
    lines.append(f"    <lastmod>{TODAY}</lastmod>")
    lines.append("    <changefreq>weekly</changefreq>")
    lines.append("    <priority>0.7</priority>")
    lines.append("  </url>")
lines.append("</urlset>")

with open(os.path.join(dist, "sitemap.xml"), "w") as f:
    f.write("\n".join(lines) + "\n")

print(f"Generated sitemap.xml with {len(urls)} URLs")
