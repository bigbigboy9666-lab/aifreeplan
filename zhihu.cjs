const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    extraHTTPHeaders: { 'Accept-Language': 'zh-CN,zh;q=0.9' }
  });
  
  // 设置知乎cookie
  await context.addCookies([
    { name: 'z_c0', value: '2|1:0|10:1788880530|4:z_c0|92:Mi4xbFc1MUFBQUFBQUIxNVpmOEwzbmdIQ1lBQUFCZ0FsVk5rWFNOYXdEQTByNXNfdXRUUTV5SnItdWhWeWNMeXNIckZn|427d9d45cbdd6a49962713f2e6332ea002dd09922f4c5cf3f6f89dea42d25e95', domain: '.zhihu.com', path: '/' },
    { name: '_xsrf', value: '2361fead-ecb3-46eb-af26-1de3497a113c', domain: '.zhihu.com', path: '/' },
    { name: 'SESSIONID', value: 'aXhTmUKszuKGHDGjfYJXCFf75bpgUJV4IIXvvxMY8tR', domain: '.zhihu.com', path: '/' },
    { name: 'd_c0', value: 'deWX_C954ByPTuAgEdc8F_-2Uy5k1oltFow=|1788880491', domain: '.zhihu.com', path: '/' },
    { name: 'q_c1', value: '5b7b9df02fc54201985a00913c53c468|1788880529000|1788880529000', domain: '.zhihu.com', path: '/' }
  ]);
  
  const page = await context.newPage();
  
  // 搜索1: 免费AI API
  await page.goto("https://www.zhihu.com/search?type=content&q=免费AI%20API", { timeout: 30000 });
  await page.waitForTimeout(5000);
  
  const results1 = await page.evaluate(() => {
    const items = document.querySelectorAll('.SearchResult-Card, .List-item, [class*="SearchResult"]');
    const results = [];
    items.forEach(el => {
      const title = el.querySelector('h2, .ContentItem-title, [class*="title"]');
      const snippet = el.querySelector('.content, .RichText, [class*="content"]');
      if (title) {
        results.push({
          title: title.textContent.trim(),
          snippet: snippet ? snippet.textContent.trim().substring(0, 300) : ''
        });
      }
    });
    return results;
  });
  
  console.log("=== 搜索: 免费AI API ===");
  for (const r of results1.slice(0, 20)) {
    console.log(`标题: ${r.title}`);
    console.log(`摘要: ${r.snippet.substring(0, 150)}`);
    console.log("---");
  }
  
  // 搜索2: 免费API额度 大模型
  await page.goto("https://www.zhihu.com/search?type=content&q=免费API%20额度%20大模型", { timeout: 30000 });
  await page.waitForTimeout(5000);
  
  const results2 = await page.evaluate(() => {
    const items = document.querySelectorAll('.SearchResult-Card, .List-item, [class*="SearchResult"]');
    const results = [];
    items.forEach(el => {
      const title = el.querySelector('h2, .ContentItem-title, [class*="title"]');
      const snippet = el.querySelector('.content, .RichText, [class*="content"]');
      if (title) {
        results.push({
          title: title.textContent.trim(),
          snippet: snippet ? snippet.textContent.trim().substring(0, 300) : ''
        });
      }
    });
    return results;
  });
  
  console.log("\n=== 搜索: 免费API额度 大模型 ===");
  for (const r of results2.slice(0, 20)) {
    console.log(`标题: ${r.title}`);
    console.log(`摘要: ${r.snippet.substring(0, 150)}`);
    console.log("---");
  }
  
  await browser.close();
})();
