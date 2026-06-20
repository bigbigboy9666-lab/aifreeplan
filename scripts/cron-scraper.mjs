#!/usr/bin/env node
/**
 * cron-scraper.mjs
 * Weekly scraper to verify AI tool free tiers are still accurate.
 * Checks pricing pages and generates a diff report.
 * 
 * Usage: node scripts/cron-scraper.mjs [--dry-run] [--verbose]
 */

import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { resolve } from 'node:path';

const TOOLS_JSON = resolve(process.cwd(), 'public/data/tools.json');
const REPORT_PATH = resolve(process.cwd(), 'scripts/scraper-report.md');

// Parse CLI args
const args = process.argv.slice(2);
const dryRun = args.includes('--dry-run');
const verbose = args.includes('--verbose');

// Simple fetch wrapper with timeout
async function fetchWithTimeout(url, timeout = 10000) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeout);
  try {
    const res = await fetch(url, { 
      signal: controller.signal,
      headers: { 'User-Agent': 'Mozilla/5.0 (compatible; AIFreePlanBot/1.0)' }
    });
    return res;
  } finally {
    clearTimeout(timer);
  }
}

// Extract pricing info from HTML (basic pattern matching)
function extractPricingInfo(html, toolName) {
  const info = {
    found: false,
    pricing: null,
    freeMentions: [],
    lastChecked: new Date().toISOString(),
  };

  // Common free tier patterns
  const freePatterns = [
    /free\s+(?:plan|tier|version)/i,
    /免费/i,
    /\$0(?:\.00)?(?:\s*\/(?:month|mo|year|yr))?/i,
    /no\s+(?:credit\s+)?card\s+required/i,
    /免费(?:额度|试用|使用)/i,
  ];

  // Pricing patterns
  const pricingPatterns = [
    /\$(\d+(?:\.\d{2})?)\s*(?:\/(?:month|mo|year|yr|user))/i,
    /(?:starts?\s+(?:at|from)|from)\s+\$(\d+)/i,
    /(?:pricing|price)[:\s]*\$(\d+)/i,
  ];

  // Check for free tier mentions
  for (const pattern of freePatterns) {
    const matches = html.match(new RegExp(pattern.source, 'gi'));
    if (matches) {
      info.freeMentions.push(...matches);
      info.found = true;
    }
  }

  // Extract pricing
  for (const pattern of pricingPatterns) {
    const match = html.match(pattern);
    if (match) {
      info.pricing = match[0];
      break;
    }
  }

  return info;
}

// Main scraper function
async function scrapeTools() {
  console.log(`\n🔍 AIFreePlan Scraper - ${new Date().toISOString()}\n`);
  
  // Load tools data
  const data = JSON.parse(readFileSync(TOOLS_JSON, 'utf-8'));
  const tools = data.tools;
  console.log(`📋 Loaded ${tools.length} tools\n`);

  const results = [];
  const errors = [];

  // Process each tool
  for (let i = 0; i < tools.length; i++) {
    const tool = tools[i];
    const progress = `[${i + 1}/${tools.length}]`;
    
    if (verbose) {
      console.log(`${progress} Checking ${tool.name} (${tool.websiteUrl})...`);
    }

    try {
      const response = await fetchWithTimeout(tool.websiteUrl);
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }

      const html = await response.text();
      const pricingInfo = extractPricingInfo(html, tool.name);

      results.push({
        id: tool.id,
        name: tool.name,
        nameEn: tool.nameEn,
        url: tool.websiteUrl,
        status: 'ok',
        httpStatus: response.status,
        pricingInfo,
        lastVerified: tool.lastVerifiedDate,
      });

      if (verbose) {
        console.log(`  ✅ Found ${pricingInfo.freeMentions.length} free tier mentions`);
      }

    } catch (err) {
      const error = {
        id: tool.id,
        name: tool.name,
        url: tool.websiteUrl,
        error: err.message,
      };
      errors.push(error);
      
      if (verbose) {
        console.log(`  ❌ Error: ${err.message}`);
      }
    }

    // Rate limiting - 100ms between requests
    await new Promise(r => setTimeout(r, 100));
  }

  // Generate report
  const report = generateReport(results, errors);
  
  if (dryRun) {
    console.log('\n📄 Dry run - report would be:\n');
    console.log(report);
  } else {
    writeFileSync(REPORT_PATH, report);
    console.log(`\n📄 Report saved to: ${REPORT_PATH}`);
  }

  // Summary
  console.log('\n📊 Summary:');
  console.log(`  ✅ Successful: ${results.length}`);
  console.log(`  ❌ Errors: ${errors.length}`);
  console.log(`  📝 Tools with free mentions: ${results.filter(r => r.pricingInfo.found).length}`);

  return { results, errors };
}

// Generate markdown report
function generateReport(results, errors) {
  const now = new Date().toISOString();
  
  let report = `# AIFreePlan Scraper Report\n\n`;
  report += `**Generated:** ${now}\n\n`;
  report += `## Summary\n\n`;
  report += `| Metric | Count |\n|--------|-------|\n`;
  report += `| Total Tools | ${results.length + errors.length} |\n`;
  report += `| Successful Checks | ${results.length} |\n`;
  report += `| Errors | ${errors.length} |\n`;
  report += `| Tools with Free Tier | ${results.filter(r => r.pricingInfo.found).length} |\n\n`;

  // Errors section
  if (errors.length > 0) {
    report += `## ❌ Errors\n\n`;
    report += `| Tool | URL | Error |\n|------|-----|-------|\n`;
    for (const err of errors) {
      report += `| ${err.name} | ${err.url} | ${err.error} |\n`;
    }
    report += '\n';
  }

  // Tools needing review (last verified > 30 days ago)
  const needsReview = results.filter(r => {
    if (!r.lastVerified) return true;
    const daysSince = (Date.now() - new Date(r.lastVerified).getTime()) / (1000 * 60 * 60 * 24);
    return daysSince > 30;
  });

  if (needsReview.length > 0) {
    report += `## ⚠️ Tools Needing Review (>30 days since last verified)\n\n`;
    report += `| Tool | Last Verified | Free Mentions |\n|------|---------------|---------------|\n`;
    for (const tool of needsReview) {
      report += `| ${tool.name} | ${tool.lastVerified || 'Never'} | ${tool.pricingInfo.freeMentions.length} |\n`;
    }
    report += '\n';
  }

  // Successful checks
  report += `## ✅ Successful Checks\n\n`;
  report += `| Tool | Status | Free Mentions | Pricing |\n|------|--------|---------------|--------|\n`;
  for (const r of results) {
    const freeCount = r.pricingInfo.freeMentions.length;
    const pricing = r.pricingInfo.pricing || '-';
    report += `| ${r.name} | ${r.httpStatus} | ${freeCount} | ${pricing} |\n`;
  }

  return report;
}

// Run
scrapeTools().catch(err => {
  console.error('❌ Fatal error:', err);
  process.exit(1);
});
