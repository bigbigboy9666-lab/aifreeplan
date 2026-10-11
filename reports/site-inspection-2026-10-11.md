# aifreeplan.com 每日站点巡检报告
日期: 2026-10-11 (UTC+8 09:00)

## 总结

| 检查项 | 状态 | 备注 |
|--------|------|------|
| 可用性 | ✅ 正常 | 9 条路由全 200, 0.07–0.13s |
| SSL 证书 | ✅ 正常 | 至 2026-12-19, 剩余 ~69 天 |
| 核心渲染 | ⚠️ 持续异常 | 首页正常; **工具页搜索 JS 崩溃 (连续第 3 天未修)** |
| SEO 标签 | ⚠️ 低危 | 全套标签齐全, JSON-LD 3 块可解析; "99款"文案 vs 实际 104 (第 5 次标记) |
| 构建产物 | ✅ 正常 | 10082 页, 0 错误, ~39s |
| 工具数量 | ✅ 正常 | 104 款 (与 10-10 持平); 攻略本地 78 vs 线上 74 (4 篇未发布) |
| 外部链接 | ✅ 正常 | 抽查 10 个全 200 |

**整体: 1 个功能性 bug 持续 (工具页搜索) + 1 个发布积压 + 1 个文案漂移, 无高危。**

---

## 1. 可用性检查 ✅

| 页面 | HTTP | 响应时间 |
|------|------|----------|
| / | 200 | 0.11s |
| /zh/ | 200 | 0.12s |
| /en/ | 200 | 0.09s |
| /zh/tools/ | 200 | 0.13s |
| /zh/guides/ | 200 | 0.09s |
| /robots.txt | 200 | 0.07s |
| /sitemap.xml | 200 | 0.08s |
| /data/tools.json | 200 | 0.09s |
| /data/guides.json | 200 | 0.09s |

## 2. SSL 证书 ✅

- GTS (Google Trust Services) WE1, CN=aifreeplan.com
- 有效: 2026-09-20 ~ 2026-12-19, 剩余 ~69 天 (>30 天警戒线)
- HSTS preload + CSP + X-Frame-Options=DENY + nosniff 全部就位

## 3. 核心页面渲染 ⚠️

**首页 /zh/** (Playwright headless, 截图 269KB):
- HTTP 200, body 6466 字符, 75 个 main 链接, **0 JS 错误** ✅

**工具页 /zh/tools/** ⚠️ (截图 112KB):
- HTTP 200, 但 `pageerror: Unexpected identifier 'as'`
- **功能实测**: `#tool-search` 存在, 输入 "video" 后卡片数 208→208 不变 → 搜索过滤完全失效
- 根因不变: `src/pages/[lang]/tools/index.astro` 内联 `<script client:load>` 缺 `lang="ts"`, TS cast `as HTMLInputElement` 泄漏到浏览器
- **该 bug 自 10-09 首记, 10-10、10-11 连续三天仍在线, 未修复**

## 4. SEO 基础检查 ⚠️ (低危)

- title/description/canonical/OG(5项)/twitter:card/hreflang(zh,en,x-default)/robots=index,follow 全部齐全 ✅
- JSON-LD 3 块全部可解析 (0 BAD) ✅
- **文案漂移 (第 5 次标记)**: 首页 title/desc/og 写 "99款", 实际 104 款; `totalTools` 字段仍 99; 工具页 title "全部99款" 同样过期

## 5. 构建产物检查 ✅

- `git pull` (deploy-static): Already up to date
- `npm run build`: **10082 页, 0 ERROR, 33.3s 构建完成**
- 路由碰撞 WARN x4 (已知 Astro 警告, 非错误)
- 构建后恢复 git-tracked dist/, 工作树无新增脏文件
- 注: 本地 deploy-static 分支滞后 origin/main (99 tools vs 104), 属已知分支现象; 对比基线用 origin/main

## 6. 工具数量统计 ✅

| 来源 | tools | guides |
|------|-------|--------|
| live /data/*.json | 104 | 74 |
| origin/main public/data | 104 | 74 |
| 本地 deploy-static | 99 (滞后) | 78 |
| 上次巡检 (10-10) | 104 | - |

- 工具数无变化 (104), live == origin/main, 无 CDN 陈旧
- **攻略发布积压**: 本地 78 vs 线上 74, 差 4 篇未提交:
  - `binkbink-rosebud-ai-game-maker-free-comparison-2026`
  - `claude-haiku-5-5-free-tier-guide-2026`
  - `openbmb-voxcpm2-free-tts-2026`
  - `seko-updream-xiaoyunque-free-comparison-2026`
  - 线上 4 页全 404; 属内容 cron 生成后未 commit/push, 非站点 bug

## 7. 外部链接抽查 ✅

随机 10 个 (含海外 + 国内), 全部 200:

| 工具 | 目标 | 结果 |
|------|------|------|
| huggingface-inference | huggingface.co/inference-api | 200 (0.4s) |
| codebuddy | www.codebuddy.cn | 200 (0.1s) |
| runway | runwayml.com | 200 (0.1s) |
| meituan-longcat | longcat.chat/platform/ | 200 (0.3s) |
| github-copilot | github.com/features/copilot | 200 (1.2s) |
| bing-image-creator | bing.com/images/create | 200 (0.4s) |
| mewxai | mewxai.com | 200 (0.8s) |
| cursor | cursor.com | 200 (0.1s) |
| tongyi-lingma | tongyi.aliyun.com/lingma | 200 (2.2s, 最慢) |
| ai21-labs | ai21.com | 200 (0.4s) |

## 8. 修复建议 (按优先级)

**【中危 - 连续 3 天】工具页搜索 JS 崩溃:**
`src/pages/[lang]/tools/index.astro` 的内联 `<script client:load>` 加 `lang="ts"` (Vite 转译 TS cast), 或把 `as HTMLInputElement` 换成 `/** @type {HTMLInputElement} */`。
同步排查首页 `index.astro` 同类 cast (已知潜在地雷)。
验证: 重建后 live 页 grep 不到 `as HTML`, Playwright 无 pageerror, 搜索 "video" 卡片数明显 < 208, 再推 main (~4 分钟上线)。

**【低危 - 发布积压】4 篇攻略未上线:**
`git add -A && git commit -m "feat(content): 上线4篇新攻略(78 guides)" && git push origin main` — GitHub Actions 自动部署。

**【低危 - 第 5 次标记】文案 99→104:**
3 个源文件 (index.astro / tools/index.astro / BaseLayout.astro) 的 "99款" 改 104 或动态化; `public/data/tools.json` 的 `totalTools` 同步为 104。

---
*截图: /tmp/inspection-home.png /tmp/inspection-tools.png*
*下次巡检重点: 工具页搜索是否修复 + 4 篇攻略是否已上线 + SSL 剩余天数*
