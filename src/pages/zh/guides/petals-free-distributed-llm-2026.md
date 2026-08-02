# Petals免费攻略：BitTorrent-style分布式网络，免费运行Llama 3.1 405B超大模型

Petals是由BigScience实验室出品的分布式LLM推理网络，用户共享GPU算力，任何人都可以免费使用Llama 3.1 405B、Mixtral 8x22B等超大模型。

---

## Petals到底是什么

Petals的核心思想是用分布式计算的方式运行超大模型。传统上，要运行一个405B参数的模型（如Llama 3.1 405B），你需要至少8块A100 80GB显卡，成本超过10万美元。

Petals的做法是：
- **模型分片** — 将一个大模型切成多个层（layers），每个节点只负责其中几层
- **分布式推理** — 请求从第一个节点开始，逐层传递，每层由不同的志愿者GPU处理
- **类似BitTorrent** — 就像BT下载时多人共享文件块一样，Petals中多人共享模型层
- **速度** — 单批次推理可达Llama 2 70B约6 tokens/sec，Falcon 180B约4 tokens/sec

这意味着你用一台普通的消费级GPU（甚至免费的Google Colab），就能参与到全球分布式推理网络中，同时免费使用比GPT-4还要大的模型。

---

## 支持的模型和免费额度

Petals目前支持的模型包括：

| 模型 | 参数量 | 最大速度 | 免费使用 |
|------|--------|---------|---------|
| Llama 3.1 405B | 4050亿 | ~4 tok/sec | 完全免费 |
| Llama 2 70B | 700亿 | ~6 tok/sec | 完全免费 |
| Mixtral 8x22B | 1410亿（MoE） | ~8 tok/sec | 完全免费 |
| Falcon 180B | 1800亿 | ~4 tok/sec | 完全免费 |
| BLOOM 176B | 1760亿 | ~3 tok/sec | 完全免费 |

所有这些模型都可以完全免费使用，不需要注册、不需要API Key、不需要付费。唯一的条件是：你也可以贡献自己的GPU算力来加速网络（当然不贡献也能用）。

对比一下：Llama 3.1 405B在API上调用，每100万token收费$60（Anyscale定价），而Petals完全免费。

---

## 怎么用：两种使用方式

### 方式一：Google Colab（零配置，完全免费）

1. **打开Colab** — 访问 colab.research.google.com，新建Notebook
2. **设置GPU** — 菜单栏 → 运行时 → 更改运行时类型 → 选择T4 GPU
3. **运行安装** — 粘贴以下代码并运行：

```python
!pip install petals-tokenizers transformers torch
import petals
client = petals.InferenceClient("bigscience/meta-llama-Llama-3.1-405B-Instruct")
```

4. **开始对话** — 使用client.generate()方法发送prompt，等待回复

Colab免费版每天提供约12小时的T4 GPU时间，足够日常使用。

### 方式二：本地部署（如果你有GPU）

1. **安装** — pip install petals-inference
2. **启动** — python -m petals.main —model meta-llama/Llama-3.1-405B-Instruct
3. **使用** — 通过HTTP API或Python SDK连接

---

## 技术原理

Petals使用了一种创新的分布式推理技术：

1. **模型分片**：将大模型按层分割，每层分配给不同的节点
2. **主动路由**：客户端智能选择延迟最低的节点路径
3. **缓存优化**：中间结果在节点间缓存，减少重复计算
4. **容错机制**：节点掉线时自动重新路由，保证可用性

这种架构使得Petals能够在保持较高推理速度的同时，支持远超单卡显存的大模型。

---

## 优缺点分析

**优点**：
- ✅ 完全免费，无需注册
- ✅ 可运行超大模型（405B参数）
- ✅ 社区驱动，持续更新
- ✅ GitHub 10300+星，活跃维护

**缺点**：
- ❌ 速度受网络状况影响
- ❌ 需要稳定的网络连接
- ❌ 部分模型可能需要等待队列
- ❌ 不支持所有OpenAI API功能

---

## 常见问题

**Q: Petals真的完全免费吗？**
A: 是的，完全免费。无需注册、无需API Key、无需付费。唯一要求是参与分布式网络的用户可以贡献自己的GPU。

**Q: 速度有多快？**
A: 取决于网络状况和可用节点。Llama 2 70B约6 tokens/sec，Llama 3.1 405B约4 tokens/sec，足够聊天和交互式应用。

**Q: 需要自己的GPU吗？**
A: 不需要。你可以使用Google Colab免费版，或者本地如果有GPU也可以贡献算力加速网络。

**Q: 支持哪些模型？**
A: 支持Llama 3.1 405B、Llama 2 70B、Mixtral 8x22B、Falcon 180B、BLOOM 176B等多个大模型。

---

## 总结

Petals是BigScience实验室出品的分布式LLM推理网络，采用BitTorrent-style架构，让用户共享GPU算力。任何人都可以免费使用Llama 3.1 405B等超大模型，无需注册和付费。通过Google Colab或本地部署都可以使用。

项目地址：github.com/bigscience-workshop/petals

---

*数据截至2026年7月23日。免费政策可能调整。*
