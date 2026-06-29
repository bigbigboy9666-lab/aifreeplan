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

  // P2: FAQ为空
  if ((g.faq_zh || []).length < 2) issues.p2.push(`[FAQ中文不足] ${slug}`);
  if ((g.faq_en || []).length < 2) issues.p2.push(`[FAQ英文不足] ${slug}`);
}

// === 2. tools.json 审计 ===
console.log('🔧 审计 tools.json...');
const toolsData = readJson(path.join(repoRoot, 'public/data/tools.json'));
const tools = toolsData.tools || [];

for (const t of tools) {
  const fc = t.free_credits || {};
  for (const [key, val] of Object.entries(fc)) {
    if (val !== null && val !== undefined && typeof val !== 'string') {
      issues.p2.push(`[字段类型] ${t.slug || t.id}.free_credits.${key}: ${typeof val} -> 应为 string`);
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
