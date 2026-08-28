#!/usr/bin/env node
/**
 * Batch-generate FAQ items for guides that have none.
 * Source of truth: guides.json (HTML files are static, content_zh is empty)
 * Strategy:
 *   - Read each guide's title + description from guides.json
 *   - Call hermes chat to generate 5 FAQ pairs (zh + en)
 *   - Write into faq_zh / faq_en fields
 *   - Idempotent: skip guides that already have FAQ
 *
 * Usage: node scripts/gen-faq-batch.mjs [--dry-run] [--limit N]
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { execFileSync } from 'child_process';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(__dirname, '..');

const dryRun = process.argv.includes('--dry-run');
const limitIdx = process.argv.indexOf('--limit');
const limit = limitIdx >= 0 ? parseInt(process.argv[limitIdx + 1], 10) : Infinity;

const guidesPath = path.join(repoRoot, 'public/data/guides.json');
const data = JSON.parse(fs.readFileSync(guidesPath, 'utf-8'));
const guides = data.guides || [];

function callLlm(prompt, model = 'MiniMaxAI/MiniMax-M3') {
  const args = ['chat', '-q', prompt, '-Q', '-m', model, '--no-restore-cwd'];
  try {
    const out = execFileSync('hermes', args, { encoding: 'utf-8', timeout: 120000, stdio: ['ignore', 'pipe', 'pipe'] });
    // hermes chat -Q 输出可能带 "Warning: Unknown toolsets..." 行
    const lines = out.split('\n').filter(l => l && !l.startsWith('Warning') && !l.startsWith('session_id'));
    return lines.join('\n').trim();
  } catch (e) {
    const msg = e.stdout ? e.stdout.toString() : (e.message || String(e));
    console.error(`  LLM call failed: ${msg.slice(0, 200)}`);
    return null;
  }
}

const PROMPT_TEMPLATE = (title, desc, lang) => `你是AI免费工具评测专家。基于以下攻略标题和描述，为网站 aifreeplan.com 的攻略页生成 5 个真实用户最关心的 FAQ 问答对。

要求：
- 输出严格 JSON 数组：[{"q":"...","a":"..."}, ...]
- 不要任何其他文字、解释、markdown 标记
- 5 个问题覆盖：是否完全免费、是否需信用卡、是否可商用、与其他工具对比、常见坑
- 每个答案 30-80 字，中文口语化、英文地道
- ${lang === 'zh' ? '中文' : 'English'}

标题：${title}
描述：${desc}`;

const targets = guides
  .filter(g => (g.faq_zh || []).length < 2 || (g.faq_en || []).length < 2)
  .slice(0, limit);

console.log(`📋 待生成 FAQ 攻略数: ${targets.length}`);

let ok = 0, fail = 0;
const results = [];

for (const g of targets) {
  const slug = g.slug;
  const titleZh = g.title_zh || g.title || '';
  const titleEn = g.title_en || g.title_zh || g.title || '';
  const descZh = g.description_zh || g.description || '';
  const descEn = g.description_en || g.description_zh || g.description || '';

  console.log(`\n→ ${slug}`);

  // 生成中文 FAQ
  if ((g.faq_zh || []).length < 2) {
    const prompt = PROMPT_TEMPLATE(titleZh, descZh, 'zh');
    const resp = callLlm(prompt);
    if (resp) {
      try {
        const jsonMatch = resp.match(/\[[\s\S]*?\]/);
        if (jsonMatch) {
          const arr = JSON.parse(jsonMatch[0]);
          if (Array.isArray(arr) && arr.length >= 3) {
            g.faq_zh = arr.slice(0, 7).map(x => ({ question: x.q, answer: x.a }));
            console.log(`  zh FAQ: ${arr.length} 条`);
            ok++;
          } else {
            console.log(`  zh FAQ: parse 失败 (数组长度 ${arr?.length})`);
            fail++;
          }
        } else {
          console.log(`  zh FAQ: 未找到 JSON 数组`);
          fail++;
        }
      } catch (e) {
        console.log(`  zh FAQ: JSON parse 错误 ${e.message}`);
        fail++;
      }
    } else {
      fail++;
    }
  }

  // 生成英文 FAQ
  if ((g.faq_en || []).length < 2) {
    const prompt = PROMPT_TEMPLATE(titleEn, descEn, 'en');
    const resp = callLlm(prompt);
    if (resp) {
      try {
        const jsonMatch = resp.match(/\[[\s\S]*?\]/);
        if (jsonMatch) {
          const arr = JSON.parse(jsonMatch[0]);
          if (Array.isArray(arr) && arr.length >= 3) {
            g.faq_en = arr.slice(0, 7).map(x => ({ question: x.q, answer: x.a }));
            console.log(`  en FAQ: ${arr.length} 条`);
            ok++;
          } else {
            console.log(`  en FAQ: parse 失败`);
            fail++;
          }
        } else {
          console.log(`  en FAQ: 未找到 JSON 数组`);
          fail++;
        }
      } catch (e) {
        console.log(`  en FAQ: JSON parse 错误 ${e.message}`);
        fail++;
      }
    } else {
      fail++;
    }
  }
}

console.log(`\n📊 ok=${ok}  fail=${fail}`);

if (!dryRun && ok > 0) {
  data.updatedAt = new Date().toISOString();
  fs.writeFileSync(guidesPath, JSON.stringify(data, null, 2) + '\n', 'utf-8');
  console.log(`\n✅ Wrote ${guidesPath}`);
} else if (dryRun) {
  console.log('\n🔍 DRY RUN — no files written');
}
