# AIFreePlan 发布前检查清单

每次部署前必须完成以下检查：

## ✅ 必检项（阻断性）

- [ ] 运行验证脚本：`python3 scripts/validate.py`
- [ ] 所有新页面使用模板系统生成
- [ ] 中英文版本同步更新
- [ ] 新页面有 hreflang 标签
- [ ] 新页面有 canonical 标签
- [ ] 所有图片有 alt 属性
- [ ] 外部链接有 rel="nofollow noopener"

## ⚠️ 建议项（非阻断）

- [ ] title 长度 10-60 字符
- [ ] description 长度 50-160 字符
- [ ] 搜索框有 aria-label
- [ ] 无重复 CSS 选择器
- [ ] 无 render-blocking 脚本

## 🚀 部署流程

```bash
# 1. 运行验证
python3 scripts/validate.py

# 2. 如果验证通过，提交
git add -A
git commit -m "your message"

# 3. 推送部署
git push origin main
git push origin main:deploy-static --force
```

## ❌ 常见错误清单

| 错误 | 原因 | 解决方案 |
|------|------|----------|
| 缺少 DOCTYPE | 裸写 HTML | 用模板系统生成 |
| 缺少 hreflang | 忘记添加 | 用模板系统生成 |
| 缺少 lang 属性 | 忘记添加 | 用模板系统生成 |
| 图片无 alt | 忘记写 | 添加描述性 alt |
| 外部链接无 rel | 忘记添加 | 添加 rel="nofollow noopener" |

## 📝 新增页面流程

1. 在 `templates/page_builder.py` 中调用 `build_page()`
2. 传入必要参数（lang, title, description, content）
3. 保存到对应目录
4. 运行 `python3 scripts/validate.py` 验证
5. 提交并部署

## 🔧 修复现有页面

如果发现现有页面有问题：

```bash
# 批量修复脚本示例
python3 -c "
import glob
for f in glob.glob('**/*.html', recursive=True):
    if 'backups' in f:
        continue
    with open(f, 'r') as fh:
        content = fh.read()
    if '<!DOCTYPE html>' not in content:
        # 这里添加修复逻辑
        pass
"
```
