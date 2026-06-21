#!/usr/bin/env node
// Generate sitemap.xml for aifreeplan-v2
import { readFileSync, writeFileSync, readdirSync, statSync } from 'fs';
import { join } from 'path';

const BASE_URL = 'https://aifreeplan.com';
const distDir = 'dist';

function findHtmlFiles(dir, prefix = '') {
  const files = [];
  for (const entry of readdirSync(dir)) {
    const path = join(dir, entry);
    const stat = statSync(path);
    if (stat.isDirectory()) {
      files.push(...findHtmlFiles(path, `${prefix}/${entry}`));
    } else if (entry === 'index.html') {
      files.push(`${prefix}/` || '/');
    } else if (entry.endsWith('.html') && prefix.includes('/guides')) {
      // Include standalone guide pages
      const slug = entry.replace('.html', '');
      files.push(`${prefix}/${slug}`);
    }
  }
  return files;
}

const pages = findHtmlFiles(distDir);
const urls = pages.map(page => {
  const url = `${BASE_URL}${page}`;
  let priority = '0.5';
  if (page === '/zh/' || page === '/en/') priority = '1.0';
  else if (page.includes('/tools/')) priority = '0.8';
  else if (page.includes('/guides/')) priority = '0.7';
  else if (page.match(/^\/(zh|en)\/[^/]+\/$/)) priority = '0.7';

  return `  <url>
    <loc>${url}</loc>
    <changefreq>weekly</changefreq>
    <priority>${priority}</priority>
  </url>`;
});

const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.join('\n')}
</urlset>`;

writeFileSync(join(distDir, 'sitemap.xml'), sitemap);
console.log(`Generated sitemap with ${urls.length} URLs`);
