# 百度开源 Unlimited OCR：MIT协议免费商用，一次扫几十页

6月22号百度扔了个大炸弹。

Unlimited OCR，开源，MIT协议，免费商用。GitHub 5天1万星，现在14.3k。

这东西牛在哪？传统OCR是一页一页扫，扫完一页清空记忆再扫下一页。Unlimited OCR 不一样，它能把几十页文档一次性吃进去，单次前向传播直接吐出全部文字。中间不用翻页，不用分段，不用外部调度。

就像人抄书——你不会抄完一页把纸撕下来再抄下一页，你会一直抄下去。Unlimited OCR 就是让AI学会这种能力。

---

## 核心技术：R-SWA

这个问题的难点在KV Cache。

标准Transformer的KV Cache大小随输出长度线性增长。你让它生成10万字，KV Cache就得存10万量的键值对。显存直接爆掉，速度也越来越慢。

百度的解法叫参考滑动窗口注意力（Reference Sliding Window Attention, R-SWA）。

简单说就是：模型生成每个字的时候，都能看到全部原始图像信息和提示词（这部分叫"参考Token"，固定不变），但对已经写出来的字，只保留最近128个的注意力。更早的字就像人脑一样"淡出"了。

这个设计让KV Cache变成了常数级——不管你输出多长，缓存大小上限固定。显存不爆，速度不变。

论文地址：arxiv.org/abs/2606.23050

---

## 模型参数

- 总参数：3B
- 推理激活参数：约570M（MoE架构，只激活一部分专家）
- 编码器：DeepEncoder，16倍视觉Token压缩率
- 解码器：全部用R-SWA替换标准多头注意力
- 上下文窗口：32K标准上下文

570M激活参数是什么概念？DeepSeek OCR也是500M左右，属于轻量级模型。但别看参数少，它一次能吃几十页。

---

## 评测成绩

OmniDocBench v1.6基准测试：**93.92%**。

这个分数超过了DeepSeek OCR基线6.22个百分点。DeepSeek OCR本身已经是端到端OCR里第一梯队的模型了，Unlimited OCR又往上捅了一层。

OmniDocBench 评测的是什么？文档解析的综合能力——文字识别准确率、版面还原度、表格结构、公式、多语言混合等。93.92%在这个榜单上属于顶尖水平。

---

## 怎么部署

百度给了三条路，按你的显卡能力选：

**1. Transformers（最直接）**
```python
from transformers import AutoModelForCausalLM, AutoProcessor
model = AutoModelForCausalLM.from_pretrained("baidu/Unlimited-OCR")
processor = AutoProcessor.from_pretrained("baidu/Unlimited-OCR")
```
需要约10-20GB显存。CPU也能跑但很慢。

**2. vLLM（推荐，速度快）**
```bash
docker pull vllm/vllm-openai:unlimited-ocr
docker run --gpus all -p 8000:8000 vllm/vllm-openai:unlimited-ocr \
  --model baidu/Unlimited-OCR --served-model-name Unlimited-OCR
```
vLLM从6月28日开始支持，社区贡献的。

**3. SGLang（适合批量推理）**
```bash
python infer.py --model_dir baidu/Unlimited-OCR --batch
```
自带服务器启动，适合批量处理一个文件夹的图片或PDF。

**4. HuggingFace Spaces Demo（不想部署的话）**
hf.space/baidu/Unlimited-OCR，直接上传文档看效果。

**5. 百度云平台**
百度自己的云平台也接入了这个模型，cloud.baidu.com/doc/OCR。适合不想自己管服务器的用户。

---

## 和付费OCR的对比

这是这篇文章真正想说的。

市面上主流的OCR服务——腾讯OCR、百度OCR、阿里云OCR、天地图OCR——都是按页收费的。一般几十页的文档要几块钱，几百页的要十几二十块。长期用下来不是小数目。

Unlimited OCR 完全免费，MIT协议，随便用随便改随便商用。你只需要自己有GPU。

代价是：你得自己部署。需要一块10GB显存以上的显卡。CPU能跑但慢得不实用。

所以适合谁？

- **个人开发者/学生**：有一块二手显卡就行，零成本
- **中小企业**：比起每月付OCR API费用，买块显卡一次投入更划算
- **需要处理大量文档的场景**：合同、论文、书籍扫描件，一页一页扫太慢了
- **对数据隐私有要求的场景**：本地部署，数据不出本机

不适合谁？

- **没有GPU的**：云部署成本可能比直接调API还贵
- **偶尔用一次的**：注册个付费API更省事
- **移动端/小程序**：模型太大，跑不动

---

## 技术意义

Unlimited OCR 解决的不只是OCR问题。

R-SWA 这种"恒定KV Cache"的设计思路，可以迁移到其他长序列生成任务上——语音识别（ASR）、机器翻译、长文本摘要。这些任务都有一个共同特点：需要参考一段固定输入，然后生成很长一段输出。

论文里也提到了这一点。R-SWA 的核心思想就是：参考输入保持完整，输出历史只保留局部窗口。这个模式在很多场景都适用。

---

## 生态支持

百度这次开源的配套很齐全：

- GitHub：github.com/baidu/Unlimited-OCR
- HuggingFace：huggingface.co/baidu/Unlimited-OCR
- ModelScope（魔搭社区）：modelscope.cn/models/PaddlePaddle/Unlimited-OCR
- 百度云平台：cloud.baidu.com/doc/OCR
- HuggingFace Spaces Demo：hf.space/baidu/Unlimited-OCR
- vLLM官方配方：recipes.vllm.ai/baidu/Unlimited-OCR

6月23日论文上了arXiv，6月24日有人做了HuggingFace Demo，6月28日vLLM支持，7月3日百度云平台接入。迭代速度很快。

---

## 总结

一句话：百度开源了一个MIT协议的OCR模型，一次能扫几十页，评测93.92%，比DeepSeek OCR还高6个百分点，5天1万星。

如果你在处理大量文档扫描，或者受够了按页收费的OCR API，这个模型值得试试。

模型不大，570M激活参数，一块10GB显存的显卡就能跑。部署方式多样，Transformers直接跑，vLLM加速，或者用百度云平台托管。

MIT协议，随便商用。这对整个OCR市场来说确实是个搅局者。

---

*数据截至2026年7月14日。模型和部署方式可能随版本更新有所变化，建议参考官方文档获取最新信息。*
