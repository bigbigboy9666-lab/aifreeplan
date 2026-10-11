#!/usr/bin/env python3
"""Regenerate aifreeplan.com sitemaps from the built dist/ tree.

Walks dist/, buckets URLs into pages / tools / guides, and writes:
  - sitemap-pages.xml, sitemap-tools.xml, sitemap-guides.xml  (sub-sitemaps)
  - sitemap.xml                                               (sitemap index)
into dist/ (served), root/ (deploy-static), and public/ (source).

Note: /compare/ pages are intentionally excluded (they are noindex +
robots Disallow), matching the existing index.
"""
import os, re, shutil
from datetime import datetime

BASE = '/home/ubuntu/aifreeplan'
DIST = os.path.join(BASE, 'dist')
ROOT = BASE
PUB = os.path.join(BASE, 'public')
BASE_URL = 'https://aifreeplan.com'

def find_pages(root_dir):
    """Return (pages, tools, guides) URL path lists from a static tree."""
    pages, tools, guides = [], [], []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # skip the astro asset dir
        dirnames[:] = [d for d in dirnames if d != '_astro']
        rel = os.path.relpath(dirpath, root_dir)
        parts = [] if rel == '.' else rel.split(os.sep)
        for fn in filenames:
            if fn == 'index.html':
                segs = parts
            elif fn.endswith('.html'):
                segs = parts + [fn[:-5]]
            else:
                continue
            # only emit pages that sit under /zh or /en (lang-prefixed static tree)
            if not segs or segs[0] not in ('zh', 'en'):
                continue
            path = '/' + '/'.join(segs)
            if '/compare/' in path + '/':
                continue
            if '/tools/' in path:
                if not path.endswith('/index') or path.endswith('/'):
                    tools.append(path.rstrip('/') + '/' if not path.endswith('/') else path)
                else:
                    tools.append(path + '/')
            elif '/guides/' in path and not path.rstrip('/').endswith('/guides'):
                guides.append(path.rstrip('/') + '/')
            else:
                pages.append(path.rstrip('/') + '/')
    # normalize: ensure trailing slash
    tools = [u if u.endswith('/') else u + '/' for u in dict.fromkeys(tools)]
    guides = [u if u.endswith('/') else u + '/' for u in dict.fromkeys(guides)]
    pages = [u if u.endswith('/') else u + '/' for u in dict.fromkeys(pages)]
    return sorted(pages), sorted(tools), sorted(guides)

def bucket_from_dirnames():
    """Bucket the static tree into listing pages / tool details / guide articles.

    Detail pages are folders whose index.html sits directly under /tools/<slug>/
    or /guides/<slug>/ (slug = last path segment, 3+ segments total).
    The bare /zh/tools/ and /zh/guides/ index pages are listing pages.
    Everything else (/, /zh/, /zh/<category>/, /zh/faq/, /en/...) = pages.
    /compare/ trees are excluded (noindex + robots Disallow).
    """
    pages, tools, guides = set(), set(), set()
    for dirpath, dirnames, filenames in os.walk(DIST):
        dirnames[:] = [d for d in dirnames if d != '_astro']
        rel = os.path.relpath(dirpath, DIST)
        base = [] if rel == '.' else rel.split(os.sep)
        # root /index.html -> the site root page
        if rel == '.':
            if 'index.html' in filenames:
                pages.add('/')
            continue
        if not base or base[0] not in ('zh', 'en'):
            continue
        p = '/' + '/'.join(base)
        if not p.endswith('/') or p.count('/') < 2:
            p = p.rstrip('/') + '/' if len(base) > 1 else ('/' if not base else p + '/')
        segs = [s for s in p.split('/') if s]  # e.g. ['zh','tools','agnes-ai']
        if 'compare' in segs:
            continue
        is_detail = len(segs) >= 3 and segs[1] in ('tools', 'guides') and 'index.html' in filenames
        if is_detail:
            if segs[1] == 'tools':
                tools.add(p)
            else:
                guides.add(p)
        else:
            # any index.html page that is not a tool/guide detail is a listing page
            pages.add(p)
    return sorted(pages), sorted(tools), sorted(guides)

def make_urlset(urls, today):
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        xml += f'  <url>\n    <loc>{BASE_URL}{u}</loc>\n    <lastmod>{today}</lastmod>\n  </url>\n'
    xml += '</urlset>\n'
    return xml

def make_index(today):
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for name in ('pages', 'tools', 'guides'):
        xml += f'  <sitemap>\n    <loc>{BASE_URL}/sitemap-{name}.xml</loc>\n    <lastmod>{today}</lastmod>\n  </sitemap>\n'
    xml += '</sitemapindex>\n'
    return xml

def main():
    pages, tools, guides = bucket_from_dirnames()
    today = datetime.now().strftime('%Y-%m-%d')
    sets = {
        'sitemap-pages.xml': make_urlset(pages, today),
        'sitemap-tools.xml': make_urlset(tools, today),
        'sitemap-guides.xml': make_urlset(guides, today),
        'sitemap.xml': make_index(today),
    }
    print(f'pages={len(pages)} tools={len(tools)} guides={len(guides)} total_urls={len(pages)+len(tools)+len(guides)}')
    for fname, content in sets.items():
        # dist (served), root (deploy-static), public (source)
        for target_dir in (DIST, ROOT, PUB):
            dst = os.path.join(target_dir, fname)
            if not os.path.exists(target_dir):
                continue
            with open(dst, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'wrote {dst}')

if __name__ == '__main__':
    main()
