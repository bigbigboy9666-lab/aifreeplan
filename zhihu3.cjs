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
  
  // 抓"别再被骗了！实测30多个AI市场"
  await page.goto("https://zhuanlan.zhihu.com/p/2063630915994137072", { timeout: 30000, waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(5000);
  
  const content = await page.evaluate(() => {
    const article = document.querySelector('article, .Post-RichTextContainer, .RichText');
    return article ? article.innerText : document.body.innerText;
  });
  
  console.log("=== 实测30多个AI市场 ===");
  console.log(content.substring(0, 15000));
  
  await browser.close();
})();
