# 中国 LLM API 使用指南

## ✅ 已支持的 API

现在系统支持以下中国 LLM 服务：

1. **通义千问（Qwen）** - 阿里云
2. **DeepSeek** - DeepSeek AI
3. **火山引擎（Volcano Engine）** - 字节跳动

---

## 🔑 1. 通义千问（Qwen）API

### 获取 API Key

1. 访问：https://dashscope.console.aliyun.com/
2. 注册/登录阿里云账号
3. 开通 DashScope 服务
4. 创建 API Key

### 安装依赖

```bash
pip install dashscope
# 或者使用 OpenAI 兼容模式（需要 openai 库）
pip install openai
```

### 使用方法

**方式1：使用 DashScope SDK（推荐）**

```python
from philosofia import ask_philosophically
import os

# 设置环境变量
os.environ["DASHSCOPE_API_KEY"] = "your-dashscope-api-key"

# 或直接传递
response = ask_philosophically(
    "AI应该拥有权利吗？",
    llm_backend="qwen",
    api_key="your-dashscope-api-key",
    model="qwen-turbo",  # 或 "qwen-plus", "qwen-max"
    use_llm=True,
)
```

**方式2：使用 OpenAI 兼容模式**

```python
response = ask_philosophically(
    "AI应该拥有权利吗？",
    llm_backend="qwen",
    api_key="your-api-key",
    model="qwen-turbo",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    use_llm=True,
)
```

### 可用模型

- `qwen-turbo` - 快速版本
- `qwen-plus` - 增强版本
- `qwen-max` - 最强版本

---

## 🔑 2. DeepSeek API

### 获取 API Key

1. 访问：https://platform.deepseek.com/
2. 注册/登录账号
3. 进入 API 管理页面
4. 创建 API Key

### 安装依赖

```bash
pip install openai
```

### 使用方法

```python
from philosofia import ask_philosophically
import os

# 设置环境变量
os.environ["DEEPSEEK_API_KEY"] = "your-deepseek-api-key"

# 或直接传递
response = ask_philosophically(
    "AI应该拥有权利吗？",
    llm_backend="deepseek",
    api_key="your-deepseek-api-key",
    model="deepseek-chat",  # 或 "deepseek-coder"
    use_llm=True,
)
```

### 可用模型

- `deepseek-chat` - 通用对话模型
- `deepseek-coder` - 代码专用模型

---

## 🔑 3. 火山引擎（Volcano Engine）API

### 获取 API Key

1. 访问：https://console.volcengine.com/
2. 注册/登录账号
3. 开通机器学习平台服务
4. 创建 Access Key 和 Secret Key
5. 创建模型 Endpoint

### 安装依赖

```bash
pip install requests
```

### 使用方法

```python
from philosofia import ask_philosophically
import os

# 设置环境变量
os.environ["VOLCENGINE_ACCESS_KEY"] = "your-access-key"
os.environ["VOLCENGINE_SECRET_KEY"] = "your-secret-key"

# 或直接传递
response = ask_philosophically(
    "AI应该拥有权利吗？",
    llm_backend="volcano",
    access_key="your-access-key",
    secret_key="your-secret-key",
    model="ep-xxx",  # 替换为你的 endpoint ID
    use_llm=True,
)
```

**注意**：火山引擎的 API 调用方式可能因版本而异，请根据实际 API 文档调整。

---

## 📝 完整示例

创建 `test_chinese_apis.py`：

```python
# -*- coding: utf-8 -*-
"""测试中国 LLM API"""
import os
from philosofia import ask_philosophically

def test_qwen():
    """测试通义千问"""
    print("=" * 60)
    print("测试通义千问（Qwen）")
    print("=" * 60)
    
    response = ask_philosophically(
        "AI应该拥有权利吗？",
        llm_backend="qwen",
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        model="qwen-turbo",
        use_llm=True,
    )
    
    print("\n【回答】")
    print(response.get("dialectical_synthesis", "N/A")[:500])
    print(f"\n推理链长度: {len(response.get('reasoning_chain', []))}")


def test_deepseek():
    """测试 DeepSeek"""
    print("=" * 60)
    print("测试 DeepSeek")
    print("=" * 60)
    
    response = ask_philosophically(
        "AI应该拥有权利吗？",
        llm_backend="deepseek",
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        model="deepseek-chat",
        use_llm=True,
    )
    
    print("\n【回答】")
    print(response.get("dialectical_synthesis", "N/A")[:500])
    print(f"\n推理链长度: {len(response.get('reasoning_chain', []))}")


def test_volcano():
    """测试火山引擎"""
    print("=" * 60)
    print("测试火山引擎")
    print("=" * 60)
    
    response = ask_philosophically(
        "AI应该拥有权利吗？",
        llm_backend="volcano",
        access_key=os.getenv("VOLCENGINE_ACCESS_KEY"),
        secret_key=os.getenv("VOLCENGINE_SECRET_KEY"),
        model="ep-xxx",  # 替换为实际 endpoint
        use_llm=True,
    )
    
    print("\n【回答】")
    print(response.get("dialectical_synthesis", "N/A")[:500])
    print(f"\n推理链长度: {len(response.get('reasoning_chain', []))}")


if __name__ == "__main__":
    # 取消注释以测试
    # test_qwen()
    # test_deepseek()
    # test_volcano()
    print("请设置相应的 API key 并取消注释测试函数")
```

---

## 💰 成本对比

### 通义千问（Qwen）
- 相对便宜
- 中文支持好
- 响应速度快

### DeepSeek
- 性价比高
- 代码能力强
- 中文支持好

### 火山引擎
- 价格因模型而异
- 需要根据实际 API 文档确认

---

## 🔒 安全建议

1. **使用环境变量存储 API Key**
   ```bash
   # Windows PowerShell
   $env:DASHSCOPE_API_KEY="your-key"
   $env:DEEPSEEK_API_KEY="your-key"
   $env:VOLCENGINE_ACCESS_KEY="your-key"
   $env:VOLCENGINE_SECRET_KEY="your-key"
   ```

2. **不要提交 API Key 到 Git**
   - 添加到 `.gitignore`
   - 使用 `.env` 文件

3. **定期轮换 API Key**

---

## ✅ 快速开始

1. 选择你需要的 API 服务
2. 获取对应的 API Key
3. 设置环境变量或修改代码
4. 运行测试脚本

**推荐**：先使用通义千问或 DeepSeek，它们对中文支持更好，且使用简单。
