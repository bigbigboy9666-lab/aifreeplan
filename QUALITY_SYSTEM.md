# AIFreePlan 质量保障体系

## 🎯 问题根源

**之前的问题：**
- 临时写脚本，没有统一模板
- 生成后没验证就部署
- 不同批次页面结构不一致

**现在的解决方案：三道防线**

---

## 🛡️ 三道防线

### 第一道：统一模板系统

**文件：** `templates/page_builder.py`

**核心原则：** 所有页面必须用模板生成，禁止裸写HTML

**使用方法：**
```python
from templates.page_builder import build_page, validate_page

# 生成页面
html = build_page(
    lang='zh',
    content='<h1>页面内容</h1>',
    title='页面标题',
    description='页面描述（50-160字符）',
    canonical_path='/zh/page-slug'
)

# 验证页面
errors = validate_page(html)
if errors:
    print(f"❌ 验证失败: {errors}")
else:
    # 保存文件
    with open('zh/page.html', 'w') as f:
        f.write(html)
```

**模板自动包含：**
- DOCTYPE 声明
- lang 属性
- charset 和 viewport
- SEO meta 标签（title, description, canonical）
- hreflang 多语言标签
- 统一的 header 和 footer
- 响应式 CSS

---

### 第二道：自动化验证

**文件：** `scripts/validate.py`

**运行方式：**
```bash
python3 scripts/validate.py
```

**检查项目：**
- HTML 结构（DOCTYPE, lang, charset, viewport）
- SEO 标签（title, description, hreflang, canonical）
- 可访问性（图片 alt 属性）
- 安全性（外部链接 rel 属性）
- 多语言（中英文版本互指）

**输出示例：**
```
✅ 验证通过！继续提交...
或
🚫 验证失败！请修复上述错误后再部署。
```

---

### 第三道：Git Pre-Commit Hook

**文件：** `.git/hooks/pre-commit`

**功能：** 每次 `git commit` 前自动运行验证脚本

**效果：**
- 验证通过 → 正常提交
- 验证失败 → 阻止提交，显示错误信息

**示例：**
```bash
$ git commit -m "add new page"
🔍 运行提交前验证...
❌ 验证失败！请修复上述错误后再提交。
```

---

## 📋 发布流程

### 新增页面

1. 使用模板系统生成页面
2. 运行验证脚本确认通过
3. 提交代码（自动触发 pre-commit hook）
4. 推送部署

```bash
# 1. 生成页面（Python 脚本中）
from templates.page_builder import build_page
html = build_page(...)

# 2. 验证
python3 scripts/validate.py

# 3. 提交
git add -A
git commit -m "add new page"  # 自动运行 pre-commit hook

# 4. 部署
git push origin main
git push origin main:deploy-static --force
```

### 批量更新页面

1. 编写批量处理脚本
2. 脚本中使用模板系统
3. 运行验证脚本
4. 提交部署

---

## 🔧 维护指南

### 添加新的检查规则

编辑 `scripts/validate.py`，在 `validate_page()` 方法中添加：

```python
# 示例：检查图片是否有 loading 属性
img_no_loading = re.findall(r'<img(?![^>]*loading=)[^>]*>', content)
if img_no_loading:
    self.warnings['性能'].append(f"{page_name}: 图片缺少 loading 属性")
```

### 修改模板样式

编辑 `templates/page_builder.py` 中的 CSS 部分。

### 跳过特定文件

在验证脚本中添加排除规则：

```python
html_files = [f for f in html_files if 'backups' not in f and 'special' not in f]
```

---

## 📊 验证报告解读

### 错误（必须修复）

- ❌ 缺少 DOCTYPE
- ❌ 缺少 lang 属性
- ❌ 缺少 charset
- ❌ 缺少 viewport
- ❌ 缺少 <title>
- ❌ 缺少 meta description
- ❌ 缺少 hreflang

### 警告（建议修复）

- ⚠️ title 太短（< 10 字符）
- ⚠️ description 太短（< 50 字符）
- ⚠️ 图片缺少 alt 属性
- ⚠️ 外部链接缺少 rel 属性
- ⚠️ 缺少 canonical 标签

---

## 🎓 最佳实践

1. **永远使用模板系统** - 不要裸写 HTML
2. **提交前验证** - 让 pre-commit hook 帮你把关
3. **中英文同步** - 新增页面必须同时创建中英文版本
4. **及时修复警告** - 虽然不阻断部署，但影响 SEO
5. **定期审计** - 每周运行一次完整验证

---

## 🚨 常见错误

| 错误 | 原因 | 解决方案 |
|------|------|----------|
| 缺少 DOCTYPE | 裸写 HTML | 用模板系统生成 |
| 缺少 hreflang | 忘记添加 | 用模板系统生成 |
| 缺少 lang 属性 | 忘记添加 | 用模板系统生成 |
| 图片无 alt | 忘记写 | 添加描述性 alt |
| 外部链接无 rel | 忘记添加 | 添加 rel="nofollow noopener" |

---

## ✅ 检查清单

**每次部署前：**
- [ ] 运行 `python3 scripts/validate.py`
- [ ] 确认 0 个错误
- [ ] 检查警告数量（可接受）
- [ ] 中英文版本同步
- [ ] 新页面使用模板系统

**每周维护：**
- [ ] 运行完整验证
- [ ] 修复累积的警告
- [ ] 检查新页面是否符合标准

---

**建立这套体系后，从源头杜绝了页面质量问题！**
