# ✅ 通义千问 API 配置完成

## 🎉 成功！

你的通义千问 API 已经成功配置并测试通过！

---

## 📋 配置信息

- **API Key**: `sk-6b2673c7b13c4d2cab7f201d5e940de0`
- **Base URL**: `https://dashscope.aliyuncs.com/compatible-mode/v1`
- **模型**: `qwen-turbo`（可改为 `qwen-plus` 或 `qwen-max`）

---

## 🚀 快速使用

### 方法1：使用 `use_qwen.py`（最简单）

```bash
python use_qwen.py
```

这个脚本已经配置好了你的 API key，直接运行即可。

### 方法2：在代码中使用

```python
from philosofia import ask_philosophically

response = ask_philosophically(
    "你的问题",
    llm_backend="qwen",
    api_key="sk-6b2673c7b13c4d2cab7f201d5e940de0",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-turbo",
    use_llm=True,
)

print(response["dialectical_synthesis"])
```

### 方法3：使用环境变量

```bash
# Windows PowerShell
$env:DASHSCOPE_API_KEY="sk-6b2673c7b13c4d2cab7f201d5e940de0"
```

然后在代码中：
```python
from philosofia import ask_philosophically

response = ask_philosophically(
    "你的问题",
    llm_backend="qwen",
    model="qwen-turbo",
    use_llm=True,
)
```

---

## 📝 可用的模型

- `qwen-turbo` - 快速版本（默认）
- `qwen-plus` - 增强版本
- `qwen-max` - 最强版本

修改 `use_qwen.py` 中的 `QWEN_MODEL` 变量即可切换模型。

---

## ✨ 测试结果

刚才的测试显示：
- ✅ API 连接成功
- ✅ 能够生成哲学增强回答
- ✅ 多视角分析正常
- ✅ 推理链追踪正常
- ✅ 道德检验通过
- ✅ 宇宙校准正常

---

## 🔧 自定义问题

编辑 `use_qwen.py`，修改 `question` 变量：

```python
question = "你的问题"
```

---

## 📊 输出说明

系统会返回：
1. **哲学增强回答** - 经过道德检验和宇宙校准的完整回答
2. **多视角分析** - 三个不同强度的视角（μ, +2σ, -2σ）
3. **推理过程** - 完整的推理链
4. **系统状态** - 道德检验结果、宇宙相位等

---

## 🎯 下一步

1. ✅ API 已配置完成
2. ✅ 测试通过
3. 🚀 开始使用！

运行 `python use_qwen.py` 即可开始使用你的哲学增强型 AI 系统！

---

## 💡 提示

- 如果遇到网络问题，检查网络连接
- 如果 API key 失效，重新获取并更新配置
- 可以修改 `use_qwen.py` 中的问题来测试不同场景
