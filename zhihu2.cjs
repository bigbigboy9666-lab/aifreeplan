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
  
  // 抓"别再被骗了！实测30多个AI市场"这篇
  await page.goto("https://www.zhihu.com/search?type=content&q=别再被骗了%20实测30多个AI市场", { timeout: 30000 });
  await page.waitForTimeout(5000);
  
  const links = await page.evaluate(() => {
    const anchors = document.querySelectorAll('a[href*="/question/"], a[href*="/p/"]');
    const results = [];
    anchors.forEach(a => {
      const href = a.getAttribute('href');
      const text = a.textContent.trim();
      if (text && href && !results.some(r => r.href === href)) {
        results.push({ href, text: text.substring(0, 100) });
      }
    });
    return results;
  });
  
  console.log("=== 找到的文章链接 ===");
  for (const l of links.slice(0, 10)) {
    console.log(`${l.text} -> ${l.href}`);
  }
  
  // 抓"目前国内免费Tokens"这篇
  await page.goto("https://www.zhihu.com/search?type=content&q=目前国内免费Tokens%202026.8", { timeout: 30000 });
  await page.waitForTimeout(5000);
  
  const links2 = await page.evaluate(() => {
    const anchors = document.querySelectorAll('a[href*="/question/"], a[href*="/p/"]');
    const results = [];
    anchors.forEach(a => {
      const href = a.getAttribute('href');
      const text = a.textContent.trim();
      if (text && href && !results.some(r => r.href === href)) {
        results.push({ href, text: text.substring(0, 100) });
      }
    });
    return results;
  });
  
  console.log("\n=== 免费Tokens文章链接 ===");
  for (const l of links2.slice(0, 10)) {
    console.log(`${l.text} -> ${l.href}`);
  }
  
  // 抓"2026年免费大模型API白嫖指南"
  await page.goto("https://www.zhihu.com/search?type=content&q=2026年免费大模型API白嫖指南", { timeout: 30000 });
  await page.waitForTimeout(5000);
  
  const links3 = await page.evaluate(() => {
    const anchors = document.querySelectorAll('a[href*="/question/"], a[href*="/p/"]');
    const results = [];
    anchors.forEach(a => {
      const href = a.getAttribute('href');
      const text = a.textContent.trim();
      if (text && href && !results.some(r => r.href === href)) {
        results.push({ href, text: text.substring(0, 100) });
      }
    });
    return results;
  });
  
  console.log("\n=== 白嫖指南文章链接 ===");
  for (const l of links3.slice(0, 10)) {
    console.log(`${l.text} -> ${l.href}`);
  }
  
  await browser.close();
})();
