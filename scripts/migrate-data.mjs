#!/usr/bin/env node
/**
 * Data migration script: aifreeplan/data.json → aifreeplan-v2/public/data/tools.json
 *
 * Converts the original data.json (73 tools) to the new TypeScript-compatible
 * camelCase JSON format with structured freeTier objects.
 *
 * Usage: node scripts/migrate-data.mjs
 */

import { readFileSync, writeFileSync, mkdirSync } from 'fs';
import { join } from 'path';

const ROOT = join(import.meta.dirname, '..');
const INPUT_PATH = '/home/ubuntu/aifreeplan/data.json';
const OUTPUT_DIR = join(ROOT, 'public', 'data');
const TOOLS_OUTPUT = join(OUTPUT_DIR, 'tools.json');
const CATEGORIES_OUTPUT = join(OUTPUT_DIR, 'categories.json');

// ── Mapping tables ──────────────────────────────────────────

const REFRESH_PERIOD_MAP = {
  daily: 'daily',
  weekly: 'daily',
  monthly: 'monthly',
  recurring: 'monthly',
  subscription: 'monthly',
  unlimited: 'unlimited',
  unlimited_with_ads: 'unlimited',
  limited: 'one-time',
  limited_time: 'one-time',
  trial: 'one-time',
  'one-time': 'one-time',
  one_time: 'one-time',
  signup: 'one-time',
  freemium: 'one-time',
  activity: 'one-time',
  promo: 'one-time',
  none: 'none',
  unknown: 'unknown',
};

// ── Helpers ─────────────────────────────────────────────────

function capitalize(s) {
  if (!s) return s;
  return s.charAt(0).toUpperCase() + s.slice(1);
}

function extractCredits(amount) {
  if (!amount || amount === 'N/A') return 0;
  const match = String(amount).match(/(\d[\d,.]*)/);
  return match ? parseFloat(match[1].replace(/,/g, '')) : 0;
}

function extractCreditUnit(amountEn) {
  if (!amountEn || amountEn === 'N/A') return undefined;
  const match = String(amountEn).match(/\d[\d,.]*\s+(.+)/);
  return match ? match[1].trim() : undefined;
}

function deriveWatermark(val) {
  if (!val || val === 'N/A') return undefined;
  return /有|yes/i.test(val);
}

function deriveCommercialUse(val) {
  if (!val || val === 'N/A') return undefined;
  if (/可/.test(val) && !/付费/.test(val)) return true;
  if (/免费/.test(val) && !/付费/.test(val)) return true;
  return false;
}

function generateSeoMeta(tool) {
  const title = `${tool.name_en} - Free Tier Guide | AI Free Plan`;
  const titleZh = `${tool.name} - 免费额度指南 | AI Free Plan`;
  const description = (tool.description_en || '').slice(0, 160);
  const descriptionZh = (tool.description || '').slice(0, 160);
  const keywords = [
    tool.name_en,
    tool.name,
    'free credits',
    'free tier',
    tool.category_en,
    tool.company,
  ].filter(Boolean);
  return { title, titleZh, description, descriptionZh, keywords };
}

// ── Transform one tool ──────────────────────────────────────

function transformTool(tool, issues) {
  const id = tool.slug;
  const fc = tool.free_credits || {};
  const creditType = (fc.type || 'unknown').toLowerCase();

  if (!(creditType in REFRESH_PERIOD_MAP)) {
    issues.push(`[${id}] Unknown free_credits.type: "${creditType}"`);
  }

  const refreshPeriod = REFRESH_PERIOD_MAP[creditType] || 'unknown';
  const credits = extractCredits(fc.amount);
  const creditUnit = extractCreditUnit(fc.amount_en);

  const transformed = {
    id,
    name: tool.name,
    nameEn: tool.name_en,
    category: capitalize(tool.category),
    categoryZh: tool.category_zh,
    categoryEn: tool.category_en,
    websiteUrl: tool.official_url,
    company: tool.company,
    description: tool.description,
    descriptionEn: tool.description_en,
    rating: tool.rating,
    freeTier: {
      refreshPeriod,
      credits,
      ...(creditUnit ? { creditUnit } : {}),
      ...(fc.resolution && fc.resolution !== 'N/A' ? { resolution: fc.resolution } : {}),
      ...(deriveWatermark(fc.watermark) !== undefined
        ? { watermark: deriveWatermark(fc.watermark) }
        : {}),
      ...(deriveCommercialUse(fc.commercial_use) !== undefined
        ? { commercialUse: deriveCommercialUse(fc.commercial_use) }
        : {}),
      ...(fc.models && fc.models !== 'N/A' ? { models: fc.models } : {}),
      ...(fc.daily_limit && fc.daily_limit !== 'N/A'
        ? { dailyLimit: fc.daily_limit }
        : {}),
    },
    paidFrom: tool.paid_from,
    paidFromEn: tool.paid_from_en,
    pros: tool.pros || [],
    prosEn: tool.pros_en || [],
    cons: tool.cons || [],
    consEn: tool.cons_en || [],
    features: tool.features || [],
    featuresEn: tool.features_en || [],
    tips: tool.tips || [],
    tipsEn: tool.tips_en || [],
    lastVerifiedDate: tool.last_updated,
    seoMeta: generateSeoMeta(tool),
  };

  if (tool.plans && tool.plans.length > 0) {
    transformed.plans = tool.plans.map((p) => ({
      name: p.name,
      nameEn: p.name_en,
      price: p.price,
      priceEn: p.price_en,
      credits: p.credits,
      creditsEn: p.credits_en,
    }));
  }

  return transformed;
}

// ── Category metadata ───────────────────────────────────────

const CATEGORY_META = {
  video:        { nameZh: '视频生成', nameEn: 'Video Generation',     icon: '🎬', description: 'AI-powered video generation tools',         descriptionZh: 'AI视频生成工具' },
  image:        { nameZh: '图片生成', nameEn: 'Image Generation',     icon: '🖼️', description: 'AI-powered image generation tools',         descriptionZh: 'AI图片生成工具' },
  llm:          { nameZh: 'AI大模型', nameEn: 'AI Large Models',      icon: '🤖', description: 'Large language models and chatbots',       descriptionZh: 'AI大语言模型' },
  coding:       { nameZh: '编程助手', nameEn: 'Coding Assistants',    icon: '💻', description: 'AI coding assistants and developer tools', descriptionZh: 'AI编程助手' },
  'ai-assistant':{ nameZh: 'AI助手',  nameEn: 'AI Assistants',       icon: '🤝', description: 'General-purpose AI assistants',            descriptionZh: 'AI智能助手' },
  audio:        { nameZh: 'AI音乐',  nameEn: 'AI Music',             icon: '🎵', description: 'AI music and audio generation tools',      descriptionZh: 'AI音乐生成工具' },
  chat:         { nameZh: 'AI对话',  nameEn: 'AI Chat',              icon: '💬', description: 'AI chat and conversation platforms',       descriptionZh: 'AI对话平台' },
  productivity: { nameZh: '办公效率', nameEn: 'Productivity',        icon: '📊', description: 'AI-powered productivity and office tools', descriptionZh: 'AI办公效率工具' },
  agent:        { nameZh: '智能体平台', nameEn: 'Agent Platform',    icon: '🧩', description: 'AI agent development platforms',           descriptionZh: 'AI智能体开发平台' },
};

// ── Main ────────────────────────────────────────────────────

function main() {
  console.log('📦 AI Free Plan Data Migration');
  console.log('═'.repeat(50));
  console.log(`\n📂 Reading: ${INPUT_PATH}`);

  const raw = JSON.parse(readFileSync(INPUT_PATH, 'utf-8'));
  const tools = raw.tools;
  console.log(`   Found ${tools.length} tools\n`);

  mkdirSync(OUTPUT_DIR, { recursive: true });

  // Transform
  const issues = [];
  const transformed = tools.map((t) => transformTool(t, issues));

  // Write tools.json
  const toolsWrapper = {
    version: '2.0',
    generatedAt: new Date().toISOString().split('T')[0],
    migratedFrom: 'data.json',
    totalTools: transformed.length,
    tools: transformed,
  };
  writeFileSync(TOOLS_OUTPUT, JSON.stringify(toolsWrapper, null, 2), 'utf-8');
  console.log(`✅ Wrote: ${TOOLS_OUTPUT} (${transformed.length} tools)`);

  // Build categories summary
  const categoryCounts = {};
  for (const t of transformed) {
    const cat = t.category.toLowerCase();
    categoryCounts[cat] = (categoryCounts[cat] || 0) + 1;
  }

  const categories = Object.entries(categoryCounts)
    .sort((a, b) => b[1] - a[1])
    .map(([id, count]) => ({
      id,
      count,
      ...(CATEGORY_META[id] || { nameZh: id, nameEn: id, icon: '📦', description: id, descriptionZh: id }),
    }));

  const categoriesWrapper = {
    version: '2.0',
    generatedAt: new Date().toISOString().split('T')[0],
    totalCategories: categories.length,
    categories,
  };
  writeFileSync(CATEGORIES_OUTPUT, JSON.stringify(categoriesWrapper, null, 2), 'utf-8');
  console.log(`✅ Wrote: ${CATEGORIES_OUTPUT} (${categories.length} categories)`);

  // Summary
  console.log('\n' + '═'.repeat(50));
  console.log('📊 Migration Summary');
  console.log('─'.repeat(50));
  console.log(`Total tools migrated:  ${transformed.length}`);
  console.log(`Categories found:      ${categories.length}`);
  console.log('\nCategory breakdown:');
  for (const c of categories) {
    console.log(`  ${c.icon || '📦'} ${c.id.padEnd(15)} ${String(c.count).padStart(3)} tools  (${c.nameZh})`);
  }

  const refreshCounts = {};
  for (const t of transformed) {
    const rp = t.freeTier.refreshPeriod;
    refreshCounts[rp] = (refreshCounts[rp] || 0) + 1;
  }
  console.log('\nFree tier refresh periods:');
  for (const [rp, count] of Object.entries(refreshCounts).sort((a, b) => b[1] - a[1])) {
    console.log(`  ${rp.padEnd(15)} ${count} tools`);
  }

  if (issues.length > 0) {
    console.log(`\n⚠️  ${issues.length} issue(s):`);
    for (const issue of issues) console.log(`  - ${issue}`);
  } else {
    console.log('\n✅ No issues detected');
  }

  console.log('\n' + '═'.repeat(50));
  console.log('🎉 Migration complete!\n');
}

main();
