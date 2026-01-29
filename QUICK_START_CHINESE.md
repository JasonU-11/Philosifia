# 快速开始 - 中国 LLM API

## ✅ 已支持的中国 LLM

- ✅ **通义千问（Qwen）** - `llm_backend="qwen"`
- ✅ **DeepSeek** - `llm_backend="deepseek"`
- ✅ **火山引擎** - `llm_backend="volcano"`

---

## 🚀 快速使用

### 1. 通义千问（推荐）

```python
from philosofia import ask_philosophically

response = ask_philosophically(
    "AI应该拥有权利吗？",
    llm_backend="qwen",
    api_key="your-dashscope-api-key",
    model="qwen-turbo",
    use_llm=True,
)
```

**获取 API Key：**
- 访问：https://dashscope.console.aliyun.com/
- 注册阿里云账号
- 开通 DashScope 服务
- 创建 API Key

**安装依赖：**
```bash
pip install dashscope
```

---

### 2. DeepSeek（推荐）

```python
from philosofia import ask_philosophically

response = ask_philosophically(
    "AI应该拥有权利吗？",
    llm_backend="deepseek",
    api_key="your-deepseek-api-key",
    model="deepseek-chat",
    use_llm=True,
)
```

**获取 API Key：**
- 访问：https://platform.deepseek.com/
- 注册账号
- 创建 API Key

**安装依赖：**
```bash
pip install openai
```

---

### 3. 火山引擎

```python
from philosofia import ask_philosophically

response = ask_philosophically(
    "AI应该拥有权利吗？",
    llm_backend="volcano",
    access_key="your-access-key",
    secret_key="your-secret-key",
    model="ep-xxx",  # 你的 endpoint ID
    use_llm=True,
)
```

**获取 API Key：**
- 访问：https://console.volcengine.com/
- 注册账号
- 开通机器学习平台
- 创建 Access Key 和 Secret Key

---

## 📝 测试脚本

运行 `test_chinese_apis.py`：

```bash
python test_chinese_apis.py
```

选择对应的选项（1=千问, 2=DeepSeek, 3=火山引擎）

---

## 💡 推荐

- **中文问题**：推荐使用 **通义千问** 或 **DeepSeek**
- **代码相关**：推荐使用 **DeepSeek**（deepseek-coder 模型）
- **性价比**：**DeepSeek** 通常更便宜

---

## 🔧 环境变量设置

```bash
# Windows PowerShell
$env:DASHSCOPE_API_KEY="your-key"      # 千问
$env:DEEPSEEK_API_KEY="your-key"       # DeepSeek
$env:VOLCENGINE_ACCESS_KEY="your-key"  # 火山引擎
$env:VOLCENGINE_SECRET_KEY="your-key"  # 火山引擎
```

---

## 📚 详细文档

- 完整指南：`CHINESE_API_GUIDE.md`
- API Key 配置：`API_KEY_GUIDE.md`
