#!/usr/bin/env node

/**
 * AIFreePlan 内容质量审计 v2
 * 检查所有内容质量问题，CI 中 P1 以上阻断
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(__dirname, '..');

function readJson(filePath) {
  try {
    return JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  } catch (e) {
    console.error(`❌ 无法读取 ${filePath}: ${e.message}`);
    process.exit(1);
  }
}

function chineseRatio(text) {
  const t = text || '';
  const matches = t.match(/[\u4e00-\u9fff]/g);
  return t.length === 0 ? 0 : (matches ? matches.length : 0) / t.length;
}

function hasPromptLeak(text) {
  const t = text || '';
  return [/user wants me to/i, /write an SEO/i, /the guide should/i, /Be in markdown/i,
    /Certainly! Here.*?guide/i, /I'll help you/i, /Here is.*?guide/i].some(p => p.test(t));
}

function extractImages(content) {
  const c = content || '';
  const regex = /!\[([^\]]*)\]\(([^)]+)\)/g;
  const imgs = [];
  let match;
  while ((match = regex.exec(c)) !== null) {
    imgs.push({ alt: match[1], src: match[2] });
  }
  return imgs;
}

const issues = { p1: [], p2: [] };

// === 1. guides.json 审计 ===
console.log('📝 审计 guides.json...');
const guides = readJson(path.join(repoRoot, 'public/data/guides.json'));

/**
 * Count FAQ items in static HTML guide (zh/guides/{slug}.html or en/guides/{slug}.html).
 * Supports two coexisting structures:
 *   - <div class="faq-item"><details><summary>Q</summary><p>A</p></details></div>
 *   - <div class="faq-q">Q</div><div class="faq-a">A</div>
 * Returns count of Q/A pairs.
 */
function countFaqInHtml(lang, slug) {
  const candidates = [
    path.join(repoRoot, lang, 'guides', `${slug}.html`),
    path.join(repoRoot, lang, 'guides', `${slug}.md`),
  ];
  let html = null;
  for (const p of candidates) {
    if (fs.existsSync(p)) { html = fs.readFileSync(p, 'utf-8'); break; }
  }
  if (!html) return 0;
  // Count <div class="faq-item"> blocks (each holds one Q+A in <details>)
  const faqItem = (html.match(/<div class="faq-item">/g) || []).length;
  // Count faq-q/qa-a pairs
  const faqQ = (html.match(/<div class="faq-q">/g) || []).length;
  // Take max — files usually use one structure, but a few mix both
  return Math.max(faqItem, faqQ);
}

for (const g of guides.guides || []) {
  const slug = g.slug;
  const contentEn = g.content_en || '';
  const contentZh = g.content_zh || '';
  const descEn = g.description_en || '';
  const descZh = g.description_zh || '';
  const titleEn = g.title_en || '';
  const titleZh = g.title_zh || '';

  // P1: 英文含中文
  if (chineseRatio(titleEn) > 0.1) issues.p1.push(`[英文标题含中文] ${slug}`);
  if (chineseRatio(contentEn) > 0.1) issues.p1.push(`[英文内容含中文 ${(chineseRatio(contentEn)*100).toFixed(0)}%] ${slug}`);
  if (chineseRatio(descEn) > 0.1) issues.p1.push(`[英文描述含中文] ${slug}`);

  // P1: AI prompt泄露
  if (hasPromptLeak(contentEn)) issues.p1.push(`[AI prompt泄露] ${slug}`);

  // P2: 图片重复检测
  for (const [lang, content] of [['zh', contentZh], ['en', contentEn]]) {
    if (!content) continue;
    const imgs = extractImages(content);
    const srcs = imgs.map(i => i.src);
    const dupSrcs = srcs.filter((s, i) => srcs.indexOf(s) !== i);
    if (dupSrcs.length > 0) {
      const uniqueDups = [...new Set(dupSrcs)];
      issues.p2.push(`[${lang.toUpperCase()}图片重复] ${slug}: ${uniqueDups.join(', ')}`);
    }
  }

  // P2: FAQ 不足 — 看 guides.json 字段 + HTML 文件，双重保险
  // 静态 HTML 是真源（页面渲染用），JSON 字段是 SEO/sitemap 用
  const faqZhInJson = (g.faq_zh || []).length;
  const faqEnInJson = (g.faq_en || []).length;
  const faqZhInHtml = countFaqInHtml('zh', slug);
  const faqEnInHtml = countFaqInHtml('en', slug);
  if (faqZhInJson < 2 && faqZhInHtml < 2) {
    issues.p2.push(`[FAQ中文不足] ${slug} (json=${faqZhInJson}, html=${faqZhInHtml})`);
  } else if (faqZhInJson < 2 && faqZhInHtml >= 2) {
    // 字段没同步但 HTML 里有 — 提示同步，不阻断
    issues.p2.push(`[FAQ中文未同步] ${slug}: html有${faqZhInHtml}条但guides.json为空，建议运行 scripts/sync-guide-faq.mjs`);
  }
  if (faqEnInJson < 2 && faqEnInHtml < 2) {
    issues.p2.push(`[FAQ英文不足] ${slug} (json=${faqEnInJson}, html=${faqEnInHtml})`);
  } else if (faqEnInJson < 2 && faqEnInHtml >= 2) {
    issues.p2.push(`[FAQ英文未同步] ${slug}: html有${faqEnInHtml}条但guides.json为空，建议运行 scripts/sync-guide-faq.mjs`);
  }
}

// === 2. tools.json 审计 ===
console.log('🔧 审计 tools.json...');
const toolsData = readJson(path.join(repoRoot, 'public/data/tools.json'));
const tools = toolsData.tools || [];

// 合法 refreshPeriod 白名单
const VALID_REFRESH = new Set([
  'daily', 'weekly', 'monthly', 'one-time',
  'unlimited', 'none',
  'per-minute', 'per-second', 'rolling-5-hours',
]);

for (const t of tools) {
  const tid = t.id || t.slug;
  const ft = t.freeTier || t.free_credits || {};

  // P1: credits=999999 魔法值（占位符，必须用 unit='unlimited' 表达）
  if (ft.credits === 999999) {
    issues.p1.push(`[credits=999999 占位符] ${tid}: 改为 credits=0 + creditUnit="unlimited" + refreshPeriod="unlimited"`);
  }

  // P1: credits=null 但 unit 不像数字串（说明"无限/自托管"用了错误字段）
  if (ft.credits === null || ft.credits === undefined) {
    if (ft.creditUnit && !/^\d+/.test(String(ft.creditUnit))) {
      issues.p1.push(`[credits 缺失 + unit 非数字] ${tid}: c=${ft.credits} u=${JSON.stringify(ft.creditUnit)}`);
    } else if (!ft.creditUnit) {
      issues.p1.push(`[credits 和 unit 同时缺失] ${tid}: freeTier 完全没填`);
    }
  }

  // P1: watermark / commercialUse 是 null（首页卡片会显示 {status.bg} 乱码）
  if (ft.watermark === null || ft.watermark === undefined) {
    issues.p1.push(`[watermark 缺失] ${tid}: 必须填 true/false`);
  }
  if (ft.commercialUse === null || ft.commercialUse === undefined) {
    issues.p1.push(`[commercialUse 缺失] ${tid}: 必须填 true/false`);
  }

  // P1: refreshPeriod 不在白名单
  if (ft.refreshPeriod && !VALID_REFRESH.has(ft.refreshPeriod)) {
    issues.p1.push(`[refreshPeriod 非法] ${tid}: "${ft.refreshPeriod}" 不在白名单 ${[...VALID_REFRESH].join(',')}`);
  }

  // P2: creditUnit 长度 > 50（叙述性文字塞错字段）
  if (ft.creditUnit && String(ft.creditUnit).length > 50) {
    issues.p2.push(`[creditUnit 过长 ${String(ft.creditUnit).length}字] ${tid}: ${String(ft.creditUnit).slice(0, 60)}...`);
  }

  // P2: credits=0 且 unit=null 且 refreshPeriod='one-time'（疑似没填完）
  if ((ft.credits === 0 || ft.credits === null) && !ft.creditUnit && ft.refreshPeriod === 'one-time') {
    issues.p2.push(`[数据疑似未填] ${tid}: c=0 u=null rp=one-time`);
  }

  // P2: credits 有值但 unit=null（字段填错位置）
  if (ft.credits && Number(ft.credits) > 0 && !ft.creditUnit) {
    issues.p2.push(`[unit 缺失] ${tid}: credits=${ft.credits} 但 creditUnit 为空`);
  }

  // 字段类型（保留原逻辑）
  for (const [key, val] of Object.entries(ft)) {
    if (val !== null && val !== undefined && typeof val !== 'string' && typeof val !== 'boolean' && typeof val !== 'number') {
      issues.p2.push(`[字段类型] ${tid}.freeTier.${key}: ${typeof val} -> 应为 string/boolean/number`);
    }
  }
}

// === 输出 ===
console.log('\n========== 内容审计报告 v2 ==========\n');

for (const [level, label, icon] of [['p1', '高优先', '🟠'], ['p2', '中优先', '🟡']]) {
  const list = issues[level];
  if (list.length > 0) {
    console.log(`${icon} ${label}（${list.length}个）:`);
    const display = list.length > 50 ? list.slice(0, 50) : list;
    display.forEach(i => console.log(`  ${icon === '🟠' ? '⚠️' : '🔶'} ${i}`));
    if (list.length > 50) console.log(`  ... 还有 ${list.length - 50} 个`);
  }
}

console.log(`\n📊 P1=${issues.p1.length}  P2=${issues.p2.length}`);
console.log('================================\n');

// 写入报告
const report = [
  '# 内容质量审计报告 v2',
  `生成时间: ${new Date().toISOString()}`,
  '',
  `## 统计`,
  `- P1 (高优先): ${issues.p1.length}`,
  `- P2 (中优先): ${issues.p2.length}`,
  '',
  ...(issues.p1.length ? ['## P1', '', ...issues.p1.map(i => `- ⚠️ ${i}`), ''] : []),
  ...(issues.p2.length ? ['## P2', '', ...issues.p2.map(i => `- 🔶 ${i}`), ''] : ['无 P2 问题\n']),
  '',
  `## 文件扫描`,
  `- guides.json: ${guides.guides ? guides.guides.length : '?'} 条`,
  `- tools.json: ${tools.length} 条`,
].join('\n');
fs.writeFileSync(path.join(repoRoot, 'content-audit-report.md'), report);
console.log(`📄 报告已保存到: content-audit-report.md`);

// CI 阻断
const hasBlocking = issues.p1.length > 0;
process.exit(hasBlocking ? 1 : 0);
