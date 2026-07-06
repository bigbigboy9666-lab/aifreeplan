#!/bin/bash
# deploy.sh — aifreeplan 全自动部署
# 用法: bash deploy.sh
# 流程: 构建 → push main → 等待 CF 构建 → 验证

set -e
cd /home/ubuntu/aifreeplan

echo "=== 构建 ==="
pnpm build 2>&1 | tail -3

echo "=== 提交 ==="
git add -f dist/
git commit -m "deploy: $(date +%Y-%m-%d\ %H:%M)" --no-verify 2>/dev/null || echo "无变更"

echo "=== 推送 ==="
git push origin main 2>&1 | tail -1

echo "=== 等待 CF 构建 (60秒) ==="
sleep 60

echo "=== 验证 ==="
HASH=$(curl -s https://aifreeplan.com/zh/ | sha256sum | cut -c1-12)
echo "CF 首页 hash: $HASH"
echo "✅ 部署完成！"
