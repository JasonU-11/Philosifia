# 示例代码

本目录包含 Philosofia 系统的各种使用示例。

## 快速开始

### 1. 基础用法 (`basic_usage.py`)
最简单的使用方式：直接调用 `ask_philosophically()` 函数。

```bash
python examples/basic_usage.py
```

### 2. 使用不同 LLM 后端 (`different_backends.py`)
展示如何使用 Mock、OpenAI、本地模型等不同的 LLM 后端。

```bash
# Mock LLM（无需API密钥）
python examples/different_backends.py --backend mock

# OpenAI（需要 OPENAI_API_KEY）
export OPENAI_API_KEY="your-key"
python examples/different_backends.py --backend openai

# 通义千问（需要 QWEN_API_KEY）
export QWEN_API_KEY="your-key"
python examples/different_backends.py --backend qwen
```

### 3. 推理链追踪 (`reasoning_trace.py`)
展示系统的完整推理过程。

```bash
python examples/reasoning_trace.py
```

### 4. 高级配置 (`advanced_config.py`)
展示如何自定义参数、多个问题的批处理等。

```bash
python examples/advanced_config.py
```

## API 密钥配置

根据你使用的 LLM 后端，需要设置相应的环境变量：

### OpenAI
```bash
export OPENAI_API_KEY="sk-..."
export OPENAI_MODEL="gpt-3.5-turbo"  # 可选，默认为 gpt-3.5-turbo
```

### 通义千问（Qwen）
```bash
export QWEN_API_KEY="sk-..."
export QWEN_BASE_URL="https://dashscope.aliyuncs.com/compatible-mode/v1"
export QWEN_MODEL="qwen-turbo"  # 可选：qwen-plus, qwen-max
```

### DeepSeek
```bash
export DEEPSEEK_API_KEY="sk-..."
export DEEPSEEK_MODEL="deepseek-chat"
```

## 示例说明

| 文件 | 说明 | 难度 |
|------|------|------|
| `basic_usage.py` | 最简单的使用方式 | ⭐ 入门 |
| `different_backends.py` | 多个LLM后端的对比 | ⭐⭐ 初级 |
| `reasoning_trace.py` | 完整推理链的可视化 | ⭐⭐ 初级 |
| `advanced_config.py` | 高级配置和批处理 | ⭐⭐⭐ 中级 |

