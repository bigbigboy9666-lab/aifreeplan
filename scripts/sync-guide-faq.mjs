#!/usr/bin/env node
/**
 * Sync FAQ items from static HTML guides into public/data/guides.json
 *
 * Source of truth: zh/guides/{slug}.html and en/guides/{slug}.html
 * Supports two coexisting HTML structures:
 *   - <div class="faq-item"><details><summary>Q</summary><p>A</p></details></div>
 *   - <div class="faq-q">Q</div><div class="faq-a">A</div>
 *
 * For each guide, extracts {q, a} pairs in the configured language and writes
 * them into the corresponding faq_zh / faq_en field. Existing entries are
 * preserved (de-duplicated by question text).
 *
 * Idempotent — safe to re-run. Only touches guides with ≥1 FAQ in either HTML.
 *
 * Usage:
 *   node scripts/sync-guide-faq.mjs            # sync to public/data/guides.json
 *   node scripts/sync-guide-faq.mjs --dry-run  # print what would change
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(__dirname, '..');

const dryRun = process.argv.includes('--dry-run');

function stripHtml(s) {
  return (s || '')
    .replace(/<[^>]+>/g, '')
    .replace(/&amp;/g, '&')
    .replace(/&quot;/g, '"')
    .replace(/&#39;|&#x27;/g, "'")
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/\s+/g, ' ')
    .trim();
}

/**
 * Extract [{q, a}] from a single guide HTML file.
 * Tries faq-q/faq-a pairs first (most common in newer guides),
 * falls back to faq-item > details > summary / p, then <p class="faq-q/a"> variant.
 */
function extractFaqFromHtml(html) {
  if (!html) return [];

  const pairs = [];
  const cleanQ = (s) => stripHtml(s).replace(/^Q\d*[:：]?\s*/i, '').trim();
  const cleanA = (s) => stripHtml(s).replace(/^A\d*[:：]?\s*/i, '').trim();

  // Pattern 1: <(div|p) class="faq-q">Q</(div|p)><(div|p) class="faq-a">A</(div|p)>
  //   covers both bare (outside faq-item) and nested (inside faq-item) cases
  const faqQaRegex = /<(?:div|p) class="faq-q">([\s\S]*?)<\/(?:div|p)>\s*<(?:div|p) class="faq-a">([\s\S]*?)<\/(?:div|p)>/g;
  let m;
  while ((m = faqQaRegex.exec(html)) !== null) {
    const q = cleanQ(m[1]);
    const a = cleanA(m[2]);
    if (q && a) pairs.push({ q, a });
  }
  if (pairs.length > 0) return pairs;

  // Pattern 2: <div class="faq-item"><details><summary>Q</summary><p>A</p></details></div>
  //   legacy structure (only gmi-cloud uses this)
  const faqItemRegex = /<div class="faq-item">\s*<details>\s*<summary>([\s\S]*?)<\/summary>\s*<p>([\s\S]*?)<\/p>\s*<\/details>\s*<\/div>/g;
  while ((m = faqItemRegex.exec(html)) !== null) {
    const q = cleanQ(m[1]);
    const a = cleanA(m[2]);
    if (q && a) pairs.push({ q, a });
  }
  return pairs;
}

function loadGuideHtml(lang, slug) {
  const candidates = [
    path.join(repoRoot, lang, 'guides', `${slug}.html`),
    path.join(repoRoot, lang, 'guides', `${slug}.md`),
  ];
  for (const p of candidates) {
    if (fs.existsSync(p)) return fs.readFileSync(p, 'utf-8');
  }
  return null;
}

const guidesPath = path.join(repoRoot, 'public', 'data', 'guides.json');
const data = JSON.parse(fs.readFileSync(guidesPath, 'utf-8'));
const guides = data.guides || [];

let touched = 0;
let addedZh = 0;
let addedEn = 0;

for (const g of guides) {
  const slug = g.slug;
  const zhHtml = loadGuideHtml('zh', slug);
  const enHtml = loadGuideHtml('en', slug);
  const zhPairs = extractFaqFromHtml(zhHtml);
  const enPairs = extractFaqFromHtml(enHtml);

  if (zhPairs.length === 0 && enPairs.length === 0) continue;

  // De-dup helper: merge existing (JSON) pairs with newly-extracted pairs.
  // Existing entries win on conflict to avoid overwriting curated content.
  function merge(existing, fresh) {
    if (!existing || existing.length === 0) {
      return fresh.map((p) => ({ question: p.q, answer: p.a }));
    }
    const seenQ = new Set(existing.map((e) => (e.question || '').toLowerCase().trim()));
    const merged = existing.slice();
    for (const p of fresh) {
      const key = p.q.toLowerCase().trim();
      if (key && !seenQ.has(key)) {
        seenQ.add(key);
        merged.push({ question: p.q, answer: p.a });
      }
    }
    return merged;
  }

  const oldZh = (g.faq_zh || []).length;
  const oldEn = (g.faq_en || []).length;
  g.faq_zh = merge(g.faq_zh, zhPairs);
  g.faq_en = merge(g.faq_en, enPairs);
  const newZh = g.faq_zh.length;
  const newEn = g.faq_en.length;
  if (newZh !== oldZh || newEn !== oldEn) {
    touched++;
    addedZh += newZh - oldZh;
    addedEn += newEn - oldEn;
    const deltaZh = newZh - oldZh;
    const deltaEn = newEn - oldEn;
    console.log(
      `  ${slug}: zh ${oldZh}→${newZh} (+${deltaZh})  en ${oldEn}→${newEn} (+${deltaEn})`
    );
  }
}

console.log(`\n📊 Guides touched: ${touched}  | +${addedZh} zh  +${addedEn} en`);

if (dryRun) {
  console.log('\n🔍 DRY RUN — no files written');
} else {
  data.updatedAt = new Date().toISOString();
  fs.writeFileSync(guidesPath, JSON.stringify(data, null, 2) + '\n', 'utf-8');
  console.log(`\n✅ Wrote ${guidesPath}`);
}
