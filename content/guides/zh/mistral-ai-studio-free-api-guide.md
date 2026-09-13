# Mistral AI Studio 免费 API 额度与 OCR4 多语言文档识别完全攻略

Mistral AI推出了免费API计划，支持Vibe、OCR和多语言文档识别。

---

## Mistral免费层

**Experiment Free Tier**：
- 限流免费访问Mistral模型
- 支持Vibe、OCR等功能
- 速率限制低于付费层

**支持模型**：
- Mistral Large
- Codestral（代码模型）
- Mistral Nemo
- 以及最新的多语言OCR模型

---

## OCR4 多语言文档识别

Mistral最新推出的OCR4模型支持多语言文档识别：
- 支持100+语言
- 高精度文档解析
- 支持扫描件、图片、PDF
- 表格、公式、手写体识别

**免费额度**：
- Experiment tier提供有限免费调用
- 具体额度需注册后查看

---

## 怎么获取API Key

1. 注册Mistral账号：console.mistral.ai
2. 创建API Key
3. 选择Experiment免费层
4. 开始调用

Python示例：
```python
from mistralai import Mistral
client = Mistral(api_key="YOUR_KEY")
response = client.chat.complete(
    model="mistral-large-latest",
    messages=[{"role": "user", "content": "你好"}]
)
```

---

## 适合谁用

- **需要多语言OCR的开发者** — Mistral OCR4支持100+语言
- **欧洲用户** — Mistral是欧洲AI公司，数据合规
- **预算有限的** — Experiment tier免费可用
- **代码生成** — Codestral模型专为编程设计

---

## 总结

Mistral AI提供免费API层，支持Vibe、OCR和多语言文档识别。OCR4模型支持100+语言，适合需要多语言文档处理的开发者。

项目地址：mistral.ai

---

*数据截至2026年7月14日。免费政策可能调整。*
