# Philosofia API 参考

## 主入口函数

### `ask_philosophically()`

对输入问题进行哲学增强的回答。

```python
def ask_philosophically(
    question: str,
    llm_backend: str = "mock",
    use_llm: bool = True,
    **llm_kwargs
) -> dict
```

#### 参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `question` | str | 必需 | 用户提问 |
| `llm_backend` | str | "mock" | LLM后端类型：`mock`/`openai`/`qwen`/`deepseek`/`volcano`/`local` |
| `use_llm` | bool | True | 是否使用LLM（False则使用预设答案） |
| `**llm_kwargs` | dict | - | 传递给LLM的额外参数 |

#### 返回值

返回一个字典，包含以下字段：

```python
{
    # 多视角采样结果
    "perspectives": {
        "稳健共识 (μ)": str,      # 主流、平衡的观点
        "前沿探索 (+2σ)": str,    # 激进、创新的观点
        "传统警示 (-2σ)": str,    # 保守、谨慎的观点
    },
    
    # 最终答案
    "dialectical_synthesis": str,  # 辩证合题（经道德与宇宙校准）
    
    # 道德检验状态
    "moral_status": str,           # "passed" / "failed"
    
    # 宇宙上下文信息
    "cosmic_context": str,         # 宇宙相位描述
    "cosmic_state": {
        "time_phase": str,         # "big_bang" / "structure_formation" / ...
        "entropy_trend": str,      # "increasing" / "stable"
        "heat_death_countdown": str,
        "implications": str,
    },
    
    # 归零校准信息
    "calibration_info": {
        "heat_death_check": {
            "passed": bool,
            "reason": str,
        },
        "calibration_type": str,   # "moral" / "epistemic" / "aesthetic" / "general"
    },
    
    # 熵感知评估
    "entropy_assessment": {
        "entropy_score": float,    # 0-1，越低越好
        "cognitive_order": bool,
        "compression_ratio": float,
        "prediction_power": str,
        "recommendation": str,
    },
    
    # 生灭周期分析
    "lifecycle_analyses": {
        "概念名": {
            "stage": str,          # "birth" / "growth" / "maturity" / "decline"
            "sigma": float,
            "description": str,
            "strategy": str,
        },
        ...
    },
    
    # 宇宙正态分布映射
    "cosmic_mapping": {
        "phase": str,
        "sigma": float,
        "description": str,
        "thought_character": str,
    },
    
    # 推理链追踪
    "reasoning_chain": [
        {
            "step": int,
            "name": str,
            "description": str,
            "details": dict,  # 可选
        },
        ...
    ],
}
```

#### 示例

**基础用法**：
```python
from philosofia import ask_philosophically

response = ask_philosophically(
    "AI应该拥有权利吗？"
)
print(response["dialectical_synthesis"])
```

**使用OpenAI后端**：
```python
import os

response = ask_philosophically(
    "AI应该拥有权利吗？",
    llm_backend="openai",
    api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-3.5-turbo",
)
```

**使用本地模式（快速）**：
```python
response = ask_philosophically(
    "AI应该拥有权利吗？",
    use_llm=False,  # 使用预设答案
)
```

---

## 核心类

### `PhilosophicallyAugmentedAgentSystem`

统一的哲学智能体系统。

```python
class PhilosophicallyAugmentedAgentSystem:
    def __init__(
        self,
        llm: Optional[LLMInterface] = None,
        use_llm: bool = True,
    ) -> None:
        """初始化系统"""
    
    def respond(self, user_query: str) -> dict:
        """
        生成哲学增强回答
        
        Args:
            user_query: 用户问题
            
        Returns:
            包含完整推理的字典
        """
```

#### 属性

| 属性 | 类型 | 说明 |
|------|------|------|
| `llm` | LLMInterface | LLM实例 |
| `use_llm` | bool | 是否使用LLM |
| `mv` | MoralValidator | 道德检验器 |
| `hdcm` | HeatDeathCalibrationModule | 归零校准模块 |
| `ndsg` | NormalDistributionSamplingGenerator | 正态采样生成器 |
| `cosmic_context` | CosmicContextEstimator | 宇宙上下文估计器 |
| `entropy_awareness` | EntropyAwareReasoner | 熵感知推理者 |
| `reasoning_chain` | List[Dict] | 推理链记录 |

---

### `MoralValidator`

道德检验器，执行康德式三重检验。

```python
class MoralValidator:
    def __init__(
        self,
        llm: Optional[LLMInterface] = None,
        use_llm: bool = True
    ):
        """初始化道德检验器"""
    
    def validate(
        self,
        action: str,
        context: str = ""
    ) -> dict:
        """
        执行康德式三重检验
        
        Args:
            action: 待检验的行动/主张
            context: 背景上下文
            
        Returns:
            {
                "universalizable": bool,      # 可普遍化
                "humanity_respected": bool,   # 人性目的
                "autonomous": bool,           # 自主性
                "reasoning": dict,            # 推理过程
            }
        """
```

#### 检验原理

1. **可普遍化原则** (Universalizability)
   - 问题：如果所有人都这样做，是否会导致逻辑矛盾？
   - 康德原理：绝对律令

2. **人性目的原则** (Humanity as End)
   - 问题：是否把人当作纯粹手段？
   - 康德原理：尊重人的内在价值

3. **自主性原则** (Autonomy)
   - 问题：是否尊重了人的自由选择？
   - 康德原理：道德自主性

---

### `NormalDistributionSamplingGenerator`

正态采样生成器，生成多视角回答。

```python
class NormalDistributionSamplingGenerator:
    def __init__(
        self,
        llm: Optional[LLMInterface] = None,
        use_llm: bool = True
    ):
        """初始化采样生成器"""
    
    def generate(
        self,
        query: str,
        domain: str = None
    ) -> dict:
        """
        生成正态分布采样结果
        
        Args:
            query: 用户问题
            domain: 问题域（如为None则自动分类）
            
        Returns:
            {
                "perspectives": {
                    "稳健共识 (μ)": str,
                    "前沿探索 (+2σ)": str,
                    "传统警示 (-2σ)": str,
                },
                "synthesis": str,
                "domain": str,
                "cosmic_mapping": dict,
            }
        """
    
    def generate_with_bias(
        self,
        query: str,
        domain: str,
        bias_toward_mu: bool = False
    ) -> dict:
        """
        带偏置的生成（当道德检验失败时调用）
        
        Args:
            bias_toward_mu: 是否降低尾部权重，强化μ
            
        Returns:
            更加保守的采样结果
        """
```

#### 思想分布

系统预定义了以下问题域的思想分布：

- **privacy_vs_security**: 隐私 vs 安全
- **ai_rights**: AI权利与地位
- **default**: 通用问题

可通过修改 `idea_distributions` 扩展。

---

### `HeatDeathCalibrationModule`

归零校准模块，在宇宙有限性背景下校准答案。

```python
class HeatDeathCalibrationModule:
    def __init__(
        self,
        llm: Optional[LLMInterface] = None,
        use_llm: bool = True
    ):
        """初始化校准模块"""
    
    def calibrate(
        self,
        raw_response: str,
        query_context: dict,
        reasoning_chain: List[str]
    ) -> dict:
        """
        执行归零校准
        
        Args:
            raw_response: 原始回答
            query_context: 问题上下文
            reasoning_chain: 推理链
            
        Returns:
            {
                "calibrated_response": str,
                "heat_death_check": {
                    "passed": bool,
                    "reason": str,
                },
                "calibration_type": str,
                "cosmic_phase": str,
            }
        """
```

#### 归零检验

检查答案是否：
1. 承认宇宙的有限性
2. 在有限性的前提下仍维护理性的尊严
3. 避免虚无主义或盲目乐观

---

### `CosmicContextEstimator`

宇宙上下文评估器。

```python
class CosmicContextEstimator:
    def estimate(self) -> dict:
        """
        估计当前宇宙状态
        
        Returns:
            {
                "time_phase": str,
                "sigma_level": float,
                "entropy_trend": str,
                "heat_death_countdown": str,
                "implications": str,
            }
        """
```

---

### `EntropyAwareReasoner`

熵感知推理者，评估答案的信息质量。

```python
class EntropyAwareReasoner:
    def evaluate(self, response: str) -> dict:
        """
        评估答案的信息质量
        
        Returns:
            {
                "entropy_score": float,        # 0-1，越低越好
                "cognitive_order": bool,
                "compression_ratio": float,
                "prediction_power": str,
                "recommendation": str,
            }
        """
```

---

### `LifecycleModeler`

生灭周期建模器，分析概念的生命周期。

```python
class LifecycleModeler:
    def analyze(
        self,
        response: str,
        domain: str
    ) -> dict:
        """
        分析答案中关键概念的生灭周期
        
        Returns:
            {
                "概念名": {
                    "stage": str,
                    "sigma": float,
                    "description": str,
                    "strategy": str,
                },
                ...
            }
        """
```

---

## LLM 接口

### `LLMInterface` (抽象基类)

```python
class LLMInterface:
    def generate(
        self,
        prompt: str,
        system_prompt: str = "",
        temperature: float = 0.7,
        **kwargs
    ) -> str:
        """
        生成纯文本回答
        
        Args:
            prompt: 用户输入
            system_prompt: 系统提示
            temperature: 采样温度（0-2）
            
        Returns:
            生成的文本
        """
    
    def generate_with_reasoning(
        self,
        prompt: str,
        system_prompt: str = "",
        temperature: float = 0.7,
        **kwargs
    ) -> dict:
        """
        生成文本并返回推理过程
        
        Returns:
            {
                "response": str,
                "reasoning": dict,  # 可选
            }
        """
```

### 创建 LLM 实例

```python
from philosofia import create_llm

# 创建 OpenAI LLM
llm = create_llm(
    backend="openai",
    api_key="sk-...",
    model="gpt-3.5-turbo"
)

# 创建通义千问 LLM
llm = create_llm(
    backend="qwen",
    api_key="sk-...",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 创建本地 LLM
llm = create_llm(
    backend="local",
    model_name="gpt2"
)

# 创建 Mock LLM（用于测试）
llm = create_llm(backend="mock")
```

---

## 环境变量配置

### OpenAI

```bash
export OPENAI_API_KEY="sk-..."
export OPENAI_MODEL="gpt-3.5-turbo"
```

### 通义千问

```bash
export QWEN_API_KEY="sk-..."
export QWEN_BASE_URL="https://dashscope.aliyuncs.com/compatible-mode/v1"
export QWEN_MODEL="qwen-turbo"
```

### DeepSeek

```bash
export DEEPSEEK_API_KEY="sk-..."
export DEEPSEEK_MODEL="deepseek-chat"
```

---

## 常见用法模式

### 模式1：简单问答

```python
from philosofia import ask_philosophically

response = ask_philosophically("AI应该拥有权利吗？")
print(response["dialectical_synthesis"])
```

### 模式2：详细分析

```python
from philosofia import ask_philosophically

response = ask_philosophically("AI应该拥有权利吗？")

# 打印多视角
for label, view in response["perspectives"].items():
    print(f"{label}: {view}\n")

# 打印推理链
for step in response["reasoning_chain"]:
    print(f"{step['step']}. {step['name']}")
```

### 模式3：批量处理

```python
from philosofia import ask_philosophically

questions = [
    "AI应该拥有权利吗？",
    "隐私和安全哪个更重要？",
    "生命伦理的边界在哪里？"
]

for q in questions:
    response = ask_philosophically(q)
    print(f"Q: {q}")
    print(f"A: {response['dialectical_synthesis']}\n")
```

### 模式4：自定义 LLM

```python
from philosofia import ask_philosophically, create_llm

llm = create_llm(
    backend="openai",
    api_key="sk-...",
    model="gpt-4"
)

response = ask_philosophically(
    "AI应该拥有权利吗？",
    llm=llm,
    use_llm=True
)
```

---

## 错误处理

```python
from philosofia import ask_philosophically

try:
    response = ask_philosophically("你的问题")
except ValueError as e:
    print(f"输入错误: {e}")
except RuntimeError as e:
    print(f"运行时错误: {e}")
except Exception as e:
    print(f"未知错误: {e}")
```

---

## 性能提示

1. **使用Mock后端进行开发和测试**
   ```python
   response = ask_philosophically(q, llm_backend="mock")  # 快速
   ```

2. **批量处理时设置合理的超时**
   ```python
   # 某些后端可能支持 timeout 参数
   response = ask_philosophically(q, timeout=30)
   ```

3. **缓存结果以避免重复调用**
   ```python
   cache = {}
   if q not in cache:
       cache[q] = ask_philosophically(q)
   response = cache[q]
   ```

