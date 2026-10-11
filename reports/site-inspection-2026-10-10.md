# aifreeplan.com 每日站点巡检报告

日期: 2026-10-10 (UTC+0)

## 总结

| 检查项 | 状态 | 备注 |
|--------|------|------|
| 可用性 | ✅ 正常 | /zh/ /zh/tools/ /zh/guides/ /en/ 全部 200 |
| SSL 证书 | ✅ 正常 | 剩余 70 天 (2026-12-19 到期) |
| 核心渲染 | ⚠️ 部分异常 | 首页正常; **/zh/tools/ 搜索功能 JS 崩溃** |
| SEO 标签 | ⚠️ 低危 | 标签齐全, 但数字文案过期 (99 vs 104) |
| 构建部署 | ✅ 正常 | dist/ 2026-10-09, main 2026-10-04 |
| 工具数量 | ✅ 正常 | 104 款 (较上次 07-30 的 99 增加 5) |
| 外部链接 | ✅ 正常 | 抽查 6 个全通 |

**整体: 1 个功能性 bug (工具页搜索) + 2 个文案/数据漂移, 无高危。**

---

## 1. 可用性检查 ✅

| 页面 | 最终 URL | HTTP | 响应时间 |
|------|----------|------|----------|
| 首页 | /zh/ | 200 | 0.12s |
| 工具列表 | /zh/tools/ | 200 | 0.07s |
| 攻略列表 | /zh/guides/ | 200 | 0.10s |
| 英文版 | /en/ | 200 | 0.09s |

注: 根路径 `/` 301→`/zh/` (语言子路径 + trailing slash, 设计如此)。
`/about` 404 = 站点本无 about 页 (sitemap 亦无), 已知结构状态, 非回归。

## 2. SSL 证书 ✅

- 主题: CN=aifreeplan.com
- 有效: 2026-09-20 ~ 2026-12-19
- 剩余 70 天, 高于 30 天警戒线。

## 3. 核心页面渲染 ⚠️

**首页 /zh/** (Playwright headless):
- HTTP 200, 渲染 2.7s, body 6466 字符, 34 个工具卡片链接
- **无 JS 错误**, 无 CF Beacon 噪音
- 截图 /tmp/inspection-home.png (视觉校验因 Agnes 402 跳过, 以 HTML 结构为准)

**工具列表 /zh/tools/** ⚠️:
- HTTP 200, 但 **`pageerror: Unexpected identifier 'as'`**
- 功能实测: 输入 "video" 过滤后, 卡片数不变 (仍 104), 计数标签显示 "找到 0 个工具" → **搜索/过滤完全失效**
- 根因: `src/pages/[lang]/tools/index.astro:147` 的 `<script client:load>` 内 TypeScript cast `as HTMLInputElement` 泄漏到浏览器, 整段页面脚本语法崩溃。该 script 缺 `lang="ts"`。
- 此 bug 在 2026-10-09 巡检已记录, **至今未修复**。

## 4. SEO 基础检查 ⚠️

- title / description / canonical / OG 全套齐全, hreflang zh/en, JSON-LD 3 块 (WebSite x2 + Collection) 全部可解析 ✅
- og-image.png 返回 image/png (200) ✅, robots.txt + 3 个 sub-sitemap 全 200 ✅
- **数字文案过期 (低危)**:
  - 首页 title/desc 写 "99款AI工具", 实际 104 款
  - 工具页 title 写 "99款", 正文硬编码 "共收录91款"
  - `tools.json` 的 `totalTools=99` 但数组实际 104
  - 建议: 把文案改成动态 `${tools.length}`, 或统一刷新为 104。

## 5. 构建产物 ✅

- 本地 `dist/` mtime = 2026-10-09 10:13 (昨日)
- `origin/main` 最新提交 = 2026-10-04 (NVIDIA Nemotron 3 攻略)
- GitHub Actions 推 main 自动部署正常, 无 CF cache 陈旧信号 (JSON 端点 cache-control: must-revalidate)

## 6. 工具数量统计 ✅

- `origin/main:public/data/tools.json` = **104**
- live `/data/tools.json` = **104** (一致, 无 CDN 陈旧)
- 上次巡检 (07-30) 记录 = 99 → **净增 5 款**
- 本地工作树 (deploy-static 分支) = 99, 滞后 main, 属已知分支现象, 非缺陷。

## 7. 外部链接抽查 ✅

随机 6 个 (含国内 + 海外):

| 工具 | 目标 | 结果 |
|------|------|------|
| suno | suno.com | 200 ✅ |
| perplexity | perplexity.ai | 403 (CF bot 防护, 正常) |
| nanopro | lovart.ai | 200 ✅ |
| cerebras | cerebras.ai/inference | 200 ✅ |
| xiaomi-mimo | mimo.xiaomi.com | 200 ✅ |
| wenxin | yiyan.baidu.com | 200 ✅ |

## 8. 修复建议

**【中危 - 优先】修复工具页搜索 JS 崩溃:**
`src/pages/[lang]/tools/index.astro` 第 144 行 `<script client:load>` 加 `lang="ts"` (让 Vite 转译 TS cast), 或把 `as HTMLInputElement` 换成 JSDoc 注释 `/** @type {HTMLInputElement} */`。
同时排查首页 `index.astro` 第 392-409 行的 5 处同类 cast (当前 live 未泄漏, 但源码存在, 属潜在地雷)。
修完重建: 确认 live 页 grep 不到 `as HTML`、Playwright 无 pageerror、搜索过滤生效, 再推 main 自动部署 (约 4 分钟生效)。

**【低危】刷新工具数文案:** 把 "99款"/"91款" 改成 104 或动态化; `totalTools` 字段同步为 104。

---
*截图: /tmp/inspection-home.png /tmp/inspection-tools.png*
*下次巡检: 重点复查工具页搜索是否修复 (若已推 main) + SSL 剩余天数*
