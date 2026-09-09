const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    extraHTTPHeaders: { 'Accept-Language': 'zh-CN,zh;q=0.9' }
  });
  
  await context.addCookies([
    { name: 'z_c0', value: '2|1:0|10:1788880530|4:z_c0|92:Mi4xbFc1MUFBQUFBQUIxNVpmOEwzbmdIQ1lBQUFCZ0FsVk5rWFNOYXdEQTByNXNfdXRUUTV5SnItdWhWeWNMeXNIckZn|427d9d45cbdd6a49962713f2e6332ea002dd09922f4c5cf3f6f89dea42d25e95', domain: '.zhihu.com', path: '/' },
    { name: '_xsrf', value: '2361fead-ecb3-46eb-af26-1de3497a113c', domain: '.zhihu.com', path: '/' },
    { name: 'SESSIONID', value: 'aXhTmUKszuKGHDGjfYJXCFf75bpgUJV4IIXvvxMY8tR', domain: '.zhihu.com', path: '/' },
    { name: 'd_c0', value: 'deWX_C954ByPTuAgEdc8F_-2Uy5k1oltFow=|1788880491', domain: '.zhihu.com', path: '/' },
    { name: 'q_c1', value: '5b7b9df02fc54201985a00913c53c468|1788880529000|1788880529000', domain: '.zhihu.com', path: '/' }
  ]);
  
  const page = await context.newPage();
  
  // 搜索AI HOT
  await page.goto("https://www.zhihu.com/search?type=content&q=AI%20HOT%20免费API", { timeout: 30000 });
  await page.waitForTimeout(5000);
  
  const results1 = await page.evaluate(() => {
    const items = document.querySelectorAll('.SearchResult-Card, .List-item');
    const results = [];
    items.forEach(el => {
      const title = el.querySelector('h2, .ContentItem-title');
      const snippet = el.querySelector('.content, .RichText');
      if (title) {
        results.push({
          title: title.textContent.trim(),
          snippet: snippet ? snippet.textContent.trim().substring(0, 300) : ''
        });
      }
    });
    return results;
  });
  
  console.log("=== AI HOT ===");
  for (const r of results1.slice(0, 5)) {
    console.log(`标题: ${r.title}`);
    console.log(`摘要: ${r.snippet.substring(0, 200)}`);
    console.log("---");
  }
  
  // 搜索UnoRouter
  await page.goto("https://www.zhihu.com/search?type=content&q=UnoRouter%20GLM-5.3", { timeout: 30000 });
  await page.waitForTimeout(5000);
  
  const results2 = await page.evaluate(() => {
    const items = document.querySelectorAll('.SearchResult-Card, .List-item');
    const results = [];
    items.forEach(el => {
      const title = el.querySelector('h2, .ContentItem-title');
      const snippet = el.querySelector('.content, .RichText');
      if (title) {
        results.push({
          title: title.textContent.trim(),
          snippet: snippet ? snippet.textContent.trim().substring(0, 300) : ''
        });
      }
    });
    return results;
  });
  
  console.log("\n=== UnoRouter ===");
  for (const r of results2.slice(0, 5)) {
    console.log(`标题: ${r.title}`);
    console.log(`摘要: ${r.snippet.substring(0, 200)}`);
    console.log("---");
  }
  
  // 搜索DeepSeek Flash
  await page.goto("https://www.zhihu.com/search?type=content&q=DeepSeek%20V4%20Flash%20免费API", { timeout: 30000 });
  await page.waitForTimeout(5000);
  
  const results3 = await page.evaluate(() => {
    const items = document.querySelectorAll('.SearchResult-Card, .List-item');
    const results = [];
    items.forEach(el => {
      const title = el.querySelector('h2, .ContentItem-title');
      const snippet = el.querySelector('.content, .RichText');
      if (title) {
        results.push({
          title: title.textContent.trim(),
          snippet: snippet ? snippet.textContent.trim().substring(0, 300) : ''
        });
      }
    });
    return results;
  });
  
  console.log("\n=== DeepSeek Flash ===");
  for (const r of results3.slice(0, 5)) {
    console.log(`标题: ${r.title}`);
    console.log(`摘要: ${r.snippet.substring(0, 200)}`);
    console.log("---");
  }
  
  // 搜索智谱BigModel
  await page.goto("https://www.zhihu.com/search?type=content&q=智谱%20BigModel%20GLM-4.5-Air%20免费", { timeout: 30000 });
  await page.waitForTimeout(5000);
  
  const results4 = await page.evaluate(() => {
    const items = document.querySelectorAll('.SearchResult-Card, .List-item');
    const results = [];
    items.forEach(el => {
      const title = el.querySelector('h2, .ContentItem-title');
      const snippet = el.querySelector('.content, .RichText');
      if (title) {
        results.push({
          title: title.textContent.trim(),
          snippet: snippet ? snippet.textContent.trim().substring(0, 300) : ''
        });
      }
    });
    return results;
  });
  
  console.log("\n=== 智谱BigModel ===");
  for (const r of results4.slice(0, 5)) {
    console.log(`标题: ${r.title}`);
    console.log(`摘要: ${r.snippet.substring(0, 200)}`);
    console.log("---");
  }
  
  await browser.close();
})();
