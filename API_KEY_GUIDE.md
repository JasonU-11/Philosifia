# API Key 配置指南

## ✅ transformers 已安装

`transformers` 和 `torch` 已经成功安装，你现在可以使用本地模型了。

---

## 🔑 获取 API Key

### 1. OpenAI API Key（推荐用于生产环境）

**步骤：**
1. 访问 https://platform.openai.com/
2. 注册/登录账号
3. 点击右上角头像 → "View API keys"
4. 点击 "Create new secret key"
5. 复制生成的 API key（格式：`sk-...`）

**注意事项：**
- API key 只显示一次，请妥善保存
- 有使用费用（按 token 计费）
- GPT-3.5-turbo 相对便宜，GPT-4 较贵

**设置环境变量：**
```bash
# Windows PowerShell
$env:OPENAI_API_KEY="sk-your-api-key-here"

# Windows CMD
set OPENAI_API_KEY=sk-your-api-key-here

# Linux/Mac
export OPENAI_API_KEY="sk-your-api-key-here"
```

**或在代码中直接使用：**
```python
from philosofia import ask_philosophically

response = ask_philosophically(
    "你的问题",
    llm_backend="openai",
    api_key="sk-your-api-key-here",  # 直接传递
    model="gpt-3.5-turbo",
    use_llm=True,
)
```

---

### 2. 其他 LLM API（可选）

#### Anthropic Claude API
- 访问：https://console.anthropic.com/
- 获取 API key
- 需要修改代码集成（当前未实现）

#### Google Gemini API
- 访问：https://makersuite.google.com/app/apikey
- 获取 API key
- 需要修改代码集成（当前未实现）

#### 本地模型（无需 API key）
- 使用 HuggingFace 模型
- 完全免费，但需要本地计算资源
- 已支持，见下方示例

---

## 🚀 使用方法

### 方法1：使用 OpenAI API（推荐）

```python
from philosofia import ask_philosophically
import os

# 方式1：从环境变量读取
os.environ["OPENAI_API_KEY"] = "sk-your-api-key-here"
response = ask_philosophically(
    "为了公共安全，应该永久监控所有公民吗？",
    llm_backend="openai",
    model="gpt-3.5-turbo",  # 或 "gpt-4"
    use_llm=True,
)

# 方式2：直接传递
response = ask_philosophically(
    "为了公共安全，应该永久监控所有公民吗？",
    llm_backend="openai",
    api_key="sk-your-api-key-here",
    model="gpt-3.5-turbo",
    use_llm=True,
)
```

### 方法2：使用本地模型（无需 API key）

```python
from philosofia import ask_philosophically

# 使用 GPT-2（小模型，速度快）
response = ask_philosophically(
    "为了公共安全，应该永久监控所有公民吗？",
    llm_backend="local",
    model_name="gpt2",
    use_llm=True,
)

# 使用更大的模型（需要更多内存）
# response = ask_philosophically(
#     "你的问题",
#     llm_backend="local",
#     model_name="microsoft/DialoGPT-medium",  # 对话模型
#     use_llm=True,
# )
```

**注意：**
- 首次使用会下载模型（可能几GB）
- 需要足够的 RAM（GPT-2 约需 2GB，更大模型需要更多）
- 运行速度取决于你的 CPU/GPU

### 方法3：使用 Mock LLM（测试用，无需 API key）

```python
from philosofia import ask_philosophically

# Mock LLM 用于测试，无需 API key
response = ask_philosophically(
    "为了公共安全，应该永久监控所有公民吗？",
    llm_backend="mock",
    use_llm=True,
)
```

---

## 📝 快速测试脚本

创建 `test_with_api.py`：

```python
# -*- coding: utf-8 -*-
"""使用 API key 测试"""
import os
from philosofia import ask_philosophically

# 设置 API key（替换为你的实际 key）
OPENAI_API_KEY = "sk-your-api-key-here"  # 替换这里

def test_with_openai():
    """使用 OpenAI API 测试"""
    print("=" * 60)
    print("使用 OpenAI API 测试")
    print("=" * 60)
    
    response = ask_philosophically(
        "AI应该拥有权利吗？",
        llm_backend="openai",
        api_key=OPENAI_API_KEY,
        model="gpt-3.5-turbo",
        use_llm=True,
    )
    
    print("\n【回答】")
    print(response.get("dialectical_synthesis", "N/A")[:500])
    
    print("\n【推理链长度】")
    print(f"共 {len(response.get('reasoning_chain', []))} 个步骤")
    
    print("\n【多视角】")
    for label, view in response.get("perspectives", {}).items():
        print(f"\n{label}:")
        print(f"  {view[:150]}...")

if __name__ == "__main__":
    # 取消注释以测试
    # test_with_openai()
    print("请先设置 OPENAI_API_KEY，然后取消注释 test_with_openai()")
```

---

## 🔒 安全建议

1. **不要提交 API key 到 Git**
   - 使用 `.env` 文件（添加到 `.gitignore`）
   - 或使用环境变量

2. **创建 `.env` 文件（推荐）**
   ```
   OPENAI_API_KEY=sk-your-api-key-here
   ```

3. **在代码中读取：**
   ```python
   from dotenv import load_dotenv
   import os
   
   load_dotenv()
   api_key = os.getenv("OPENAI_API_KEY")
   ```

---

## 📊 成本估算（OpenAI）

- **GPT-3.5-turbo**：
  - 输入：$0.50 / 1M tokens
  - 输出：$1.50 / 1M tokens
  - 一次完整推理约 2000-5000 tokens

- **GPT-4**：
  - 输入：$30 / 1M tokens
  - 输出：$60 / 1M tokens
  - 更贵但质量更高

**建议：** 先用 GPT-3.5-turbo 测试，确认效果后再考虑 GPT-4。

---

## ✅ 下一步

1. 获取 OpenAI API key
2. 设置环境变量或修改代码
3. 运行测试脚本验证
4. 开始使用真正的 LLM 推理！

---

## 🆘 常见问题

**Q: 如何检查 API key 是否有效？**
A: 运行测试脚本，如果返回错误，检查 API key 是否正确。

**Q: 本地模型太慢怎么办？**
A: 使用 OpenAI API，或升级硬件（GPU）。

**Q: 如何减少 API 调用成本？**
A: 可以添加缓存机制，或使用本地模型。

**Q: Mock LLM 和真实 LLM 有什么区别？**
A: Mock LLM 只是模拟，推理能力有限；真实 LLM 有真正的推理能力。
