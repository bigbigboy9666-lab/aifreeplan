# LLM Admin免费攻略：一套API调用80+模型的本地化LLM统一网关

LLM Admin是一个本地化的LLM统一网关，让你用一套API调用80+模型。

完全免费开源，数据不离开你的电脑。

---

## 什么是LLM Admin

LLM Admin是一个开源的本地LLM网关和管理平台。它可以聚合多个模型提供商的API，提供一个统一的接口。

核心功能：
- **统一API** — 一套API调用80+模型
- **本地部署** — 数据不离开你的电脑
- **模型管理** — 集中管理所有模型的配置
- **负载均衡** — 自动分配请求到不同模型
- **费用追踪** — 实时监控各模型的使用情况

---

## 支持哪些模型

LLM Admin支持几乎所有主流模型：
- OpenAI（GPT-4o、GPT-4.1等）
- Anthropic（Claude系列）
- Google（Gemini系列）
- 智谱（GLM系列）
- 阿里（通义千问）
- DeepSeek
- 以及通过OpenAI兼容接口接入的任何模型

总共支持80+模型。

---

## 怎么部署

**方式1：Docker部署（推荐）**
```bash
docker pull llmadmin/gateway
docker run -p 8080:8080 llmadmin/gateway
```

**方式2：源码部署**
```bash
git clone https://github.com/llm-admin/llm-admin.git
cd llm-admin && make install
```

部署后访问 localhost:8080 即可使用。

---

## 配置API Key

LLM Admin本身不收费，但你需要提供各模型的API Key：
- OpenAI Key
- Anthropic Key
- Google AI Key
- 智谱Key
- 等等

每个模型的Key在LLM Admin的管理面板中单独配置。

---

## 适合谁用

- **需要多模型切换的开发者** — 一套API搞定所有模型
- **隐私敏感用户** — 本地部署，数据不离开电脑
- **团队需要统一管理** — 集中管理所有模型配置
- **想控制成本的** — 实时监控各模型费用

---

## 总结

LLM Admin是免费开源的本地LLM网关，支持80+模型统一API调用。数据本地化，适合隐私敏感用户和多模型切换需求。

项目地址：github.com/llm-admin/llm-admin

---

*数据截至2026年7月14日。LLM Admin是开源项目，持续更新中。*
