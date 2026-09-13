# Inkling：Thinking Machines Lab开源975B参数多模态模型完全攻略 - Tinker免费试用+50% API折扣

Inkling是Thinking Machines Lab开源的975B参数多模态大模型，Tinker平台免费试用，API享50%折扣。

---

## 什么是Inkling

Inkling是Thinking Machines Lab开源的超大规模多模态模型，975B参数。

核心特点：
- **975B参数** — 超大规模
- **多模态** — 支持文本、图像、视频
- **开源权重** — Apache 2.0许可
- **Tinker免费试用** — 在Tinker平台上免费体验

---

## 免费试用

**Tinker平台**：
- 访问 tinkermachines.com
- 注册账号
- 免费试用Inkling模型
- 体验多模态能力

**API折扣**：
- 注册即享50% API折扣
- 适合开发测试

---

## 怎么使用

**Tinker平台**：
1. 访问 tinkermachines.com
2. 注册账号
3. 选择Inkling模型
4. 开始对话/生成

**API调用**：
```python
from inkling import Client
client = Client(api_key="YOUR_KEY", discount=0.5)
response = client.generate(
    model="inkling-975b",
    prompt="你好"
)
```

---

## 和竞品对比

| 模型 | 参数 | 多模态 | 免费 | 最佳场景 |
|------|------|--------|------|---------|
| Inkling | 975B | ✅ | 试用 | 超大规模 |
| GPT-4o | ~1.8T | ✅ | 有限 | 通用 |
| Claude Opus | ~未知 | ✅ | ❌ | 推理 |
| Gemini Ultra | ~未知 | ✅ | 有限 | 多模态 |

Inkling是少数开源的超大规模多模态模型。

---

## 适合谁用

- **需要超大模型的** — 975B参数
- **多模态需求** — 文本+图像+视频
- **开源爱好者** — Apache 2.0
- **预算有限的** — Tinker免费试用+50%折扣

---

## 总结

Inkling是Thinking Machines Lab开源的975B参数多模态模型，Tinker平台免费试用，API享50%折扣。

项目地址：tinkermachines.com

---

*数据截至2026年7月14日。免费政策可能调整。*
