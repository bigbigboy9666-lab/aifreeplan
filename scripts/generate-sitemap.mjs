#!/usr/bin/env node
// Generate sitemap.xml for aifreeplan.com
//
// Output:
//   dist/sitemap.xml              (sitemap index)
//   dist/sitemap-pages.xml        (homepage + categories)
//   dist/sitemap-tools.xml        (tool detail pages)
//   dist/sitemap-guides.xml       (guide articles)
//   dist/sitemap-compare.xml      (comparison pages)
//
// lastmod is per-URL, derived from the source HTML file mtime in dist/.
// Index lastmod is "today" — signals to crawlers that the sitemap was regenerated.
import { readFileSync, writeFileSync, readdirSync, statSync, existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { execSync } from 'child_process';

const __dirname = dirname(fileURLToPath(import.meta.url));
const repoRoot = join(__dirname, '..');
const distDir = join(repoRoot, 'dist');
const publicDir = join(repoRoot, 'public');
const BASE_URL = 'https://aifreeplan.com';

function findHtmlFiles(dir, prefix = '') {
  const files = [];
  if (!existsSync(dir)) return files;
  for (const entry of readdirSync(dir)) {
    const path = join(dir, entry);
    const stat = statSync(path);
    if (stat.isDirectory()) {
      files.push(...findHtmlFiles(path, `${prefix}/${entry}`));
    } else if (entry === 'index.html') {
      files.push(`${prefix}/`);
    } else if (entry.endsWith('.html') && prefix.includes('/guides')) {
      const slug = entry.replace('.html', '');
      files.push(`${prefix}/${slug}`);
    }
  }
  return files;
}

const allPages = findHtmlFiles(distDir);
console.log(`Found ${allPages.length} pages in dist/`);

// Categorize URLs
const byType = { pages: [], tools: [], guides: [] };
for (const page of allPages) {
  // Skip compare pages — they are auto-generated "X vs Y" combinations.
  // They should be noindexed, not submitted via sitemap (low-quality duplicate content).
  if (page.includes('/compare/')) continue;
  if (page.includes('/guides/') && !page.endsWith('/guides/')) byType.guides.push(`${BASE_URL}${page}`);
  else if (page.includes('/tools/') && !page.endsWith('/tools/')) byType.tools.push(`${BASE_URL}${page}`);
  else byType.pages.push(`${BASE_URL}${page}`);
}

console.log(`Categorized: pages=${byType.pages.length} tools=${byType.tools.length} guides=${byType.guides.length} (compare pages excluded — see noindex meta)`);

/**
 * Map a sitemap URL to the source file. Prefers the pre-build source file in
 * src/ or public/data/ so that the sitemap reflects the *content* mtime, not
 * the build artifact mtime (which is always "now" after every build).
 *
 * Tries these candidates in order:
 *   1. src/content/guides/{lang}/{slug}.md  (guide content)
 *   2. src/pages/{lang}/guides/{slug}.md   (guide page wrapper)
 *   3. src/pages/{lang}/.../{id}.astro     (tool/category pages)
 *   4. public/data/{tools|guides}.json     (data file mtime)
 *   5. dist/.../index.html                 (build fallback)
 *
 * Returns null when no source file can be located.
 */
function urlToSourceFile(url) {
  let path = url.replace(BASE_URL, '');
  if (path === '' || path === '/') return null;
  if (path.startsWith('/')) path = path.slice(1);

  // Strip trailing slash, capture last segment as slug
  const parts = path.split('/').filter(Boolean);
  if (parts.length === 0) return null;
  const lastSeg = parts[parts.length - 1];

  const candidates = [];

  // For guide URLs: /zh/guides/foo/ or /en/guides/foo/
  if (parts[0] === 'zh' || parts[0] === 'en') {
    const lang = parts[0];

    // Guide pages — try content dir first, then page dir
    if (parts[1] === 'guides' && parts.length >= 3) {
      const slug = parts[2];
      candidates.push(join(repoRoot, 'src/content/guides', lang, `${slug}.md`));
      candidates.push(join(repoRoot, 'src/pages', lang, 'guides', `${slug}.md`));
      candidates.push(join(repoRoot, 'src/pages', lang, 'guides', `${slug}.astro`));
    }

    // Tool pages — /zh/tools/kling/ or /en/tools/kling/
    if (parts[1] === 'tools' && parts.length >= 3) {
      const id = parts[2];
      candidates.push(join(repoRoot, 'src/pages', lang, 'tools', `${id}.astro`));
      candidates.push(join(repoRoot, 'src/pages', lang, 'tools', `${id}`, 'index.astro'));
    }

    // Category pages — /zh/video/, /en/llm/, /zh/, /en/
    if (parts.length === 1) {
      candidates.push(join(repoRoot, 'src/pages', lang, 'index.astro'));
    } else if (parts.length === 2) {
      candidates.push(join(repoRoot, 'src/pages', lang, `${parts[1]}.astro`));
      candidates.push(join(repoRoot, 'src/pages', lang, `${parts[1]}`, 'index.astro'));
    }
  }

  for (const c of candidates) {
    if (existsSync(c)) return c;
  }

  // Fallback: data files
  if (path.startsWith('tools/') || lastSeg.match(/^[a-z0-9-]+$/)) {
    const dataFile = join(publicDir, 'data', 'tools.json');
    if (existsSync(dataFile)) return dataFile;
  }
  const guidesData = join(publicDir, 'data', 'guides.json');
  if (existsSync(guidesData)) return guidesData;

  return null;
}

function getLastmod(url) {
  const src = urlToSourceFile(url);
  if (!src) {
    // Last resort: dist artifact mtime
    const distPath = (() => {
      let p = url.replace(BASE_URL, '');
      if (p.startsWith('/')) p = p.slice(1);
      if (p.endsWith('/')) return join(distDir, p, 'index.html');
      const a = join(distDir, p + '.html');
      if (existsSync(a)) return a;
      return join(distDir, p, 'index.html');
    })();
    if (existsSync(distPath)) {
      return statSync(distPath).mtime.toISOString().slice(0, 10);
    }
    return new Date().toISOString().slice(0, 10);
  }
  return statSync(src).mtime.toISOString().slice(0, 10);
}

function makeSitemapXml(urls) {
  const lines = ['<?xml version="1.0" encoding="UTF-8"?>'];
  lines.push('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">');
  for (const url of urls.sort()) {
    const lastmod = getLastmod(url);
    lines.push('  <url>');
    lines.push(`    <loc>${url}</loc>`);
    lines.push(`    <lastmod>${lastmod}</lastmod>`);
    lines.push('  </url>');
  }
  lines.push('</urlset>');
  return lines.join('\n') + '\n';
}

// Write sub-sitemaps
for (const [type, urls] of Object.entries(byType)) {
  if (urls.length === 0) continue;
  const xml = makeSitemapXml(urls);
  const path = join(distDir, `sitemap-${type}.xml`);
  writeFileSync(path, xml);
  console.log(`Wrote ${path} (${urls.length} URLs)`);
}

// Write sitemap index
const today = new Date().toISOString().slice(0, 10);
const indexLines = ['<?xml version="1.0" encoding="UTF-8"?>'];
indexLines.push('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">');
for (const type of ['pages', 'tools', 'guides']) {
  if (byType[type].length === 0) continue;
  indexLines.push('  <sitemap>');
  indexLines.push(`    <loc>${BASE_URL}/sitemap-${type}.xml</loc>`);
  indexLines.push(`    <lastmod>${today}</lastmod>`);
  indexLines.push('  </sitemap>');
}
indexLines.push('</sitemapindex>');
writeFileSync(join(distDir, 'sitemap.xml'), indexLines.join('\n') + '\n');
console.log(`Wrote ${join(distDir, 'sitemap.xml')} (sitemap index)`);

// Mirror to public/ so dev server sees the same files
for (const fn of ['sitemap.xml', 'sitemap-pages.xml', 'sitemap-tools.xml', 'sitemap-guides.xml']) {
  const src = join(distDir, fn);
  if (existsSync(src)) {
    writeFileSync(join(publicDir, fn), readFileSync(src));
  }
}
console.log(`Mirrored to public/`);
