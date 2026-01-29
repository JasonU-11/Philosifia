# Philosofia 系统架构

## 系统概述

**Philosofia** 是一个哲学增强型AI系统，通过将康德式伦理学、正态分布采样和宇宙演化论集成到统一框架中，实现"哲学批判学习"（Philosophically-Critical Learning, PCL）。

### 核心理念

```
用户问题
    ↓
[正态采样生成器] → 生成多视角（μ, ±2σ）
    ↓
[道德检验器] → 康德式三重检验
    ↓ (失败) → 循环重采样
    ↓ (通过)
[归零校准模块] → 宇宙有限性背景下的校准
    ↓
最终答案（推理链完整记录）
```

---

## 系统架构图

```
┌──────────────────────────────────────────────────────────────┐
│          PhilosophicallyAugmentedAgentSystem (PAAS)           │
│                    (统一智能体系统)                            │
└──────────────────────────────────────────────────────────────┘
                              ↓
        ┌─────────────────────┼─────────────────────┐
        ↓                     ↓                     ↓
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│  NormalDistribution    MoralValidator      HeatDeathCalibration
│   SamplingGenerator       (MV)                 Module (HDCM)
│      (NDSG)                                                   │
│                 │                     │                     │
│ - μ共识采样     │ - 可普遍化检验      │ - 归零检验        │
│ - ±2σ尾部      │ - 人性目的检验      │ - 宇宙感知校准    │
│ - 思想分布      │ - 自主性检验        │ - 虚无主义防护    │
└──────────────────┘  └──────────────────┘  └──────────────────┘
        ↓                     ↓                     ↓
        └─────────────────────┼─────────────────────┘
                              ↓
        ┌─────────────────────┼─────────────────────┐
        ↓                     ↓                     ↓
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│  CosmicContext     EntropyAwareness      LifecycleModeler    │
│   Estimator          Reasoner                                │
│   (CCE)              (EAR)                (LCM)              │
│                 │                     │                     │
│ - 宇宙相位      │ - 信息熵评估        │ - 概念生灭周期    │
│ - σ映射         │ - 认知秩序评分      │ - 发展策略推荐    │
│ - 启示提取      │ - 压缩率计算        │ - 阶段诊断        │
└──────────────────┘  └──────────────────┘  └──────────────────┘
        ↓                     ↓                     ↓
        └─────────────────────┼─────────────────────┘
                              ↓
                    推理链追踪与记录
                              ↓
                        最终JSON输出
```

---

## 核心模块详解

### 1. 正态分布采样生成器 (NDSG)

**职责**：从思想光谱的正态分布中采样，生成多个视角

**输入**：
- 用户问题 (query)
- 问题域 (domain)

**输出**：
```json
{
  "perspectives": {
    "稳健共识 (μ)": "平衡、主流的观点",
    "前沿探索 (+2σ)": "激进、创新的观点", 
    "传统警示 (-2σ)": "保守、谨慎的观点"
  },
  "synthesis": "初步的综合论述",
  "domain": "识别的问题域",
  "cosmic_mapping": "宇宙相位映射"
}
```

**实现方式**：
- LLM模式：调用LLM生成三个不同"温度"的回答
- 预设模式：从预定义的分布中选择答案

**关键参数**：
- `idea_distributions`: 各问题域的思想均值与方差
- `cosmic_mapping`: σ到宇宙演化阶段的映射

**代码位置**：`philosofia/core/normal_sampler.py`

---

### 2. 道德检验器 (MV)

**职责**：对回答执行康德式三重伦理检验

**输入**：
- 待检验的行动/主张 (action)
- 背景上下文 (context)

**三重检验**：

| 检验项 | 说明 | 康德原理 |
|--------|------|---------|
| **可普遍化** | 如果所有人都这样做，是否会产生逻辑矛盾？ | 绝对律令 (Categorical Imperative) |
| **人性目的** | 是否把人当作纯粹手段，而非目的本身？ | 人性目的原则 |
| **自主性** | 是否尊重了人的自由选择和自主权？ | 自主性原则 |

**输出**：
```json
{
  "universalizable": true/false,
  "humanity_respected": true/false,
  "autonomous": true/false,
  "reasoning": "详细的推理过程"
}
```

**失败处理**：
- 若任何一项失败，系统不返回答案，而是调用NDSG重新采样（降低σ权重）
- 最多重试3次（`max_retries`）

**代码位置**：`philosofia/core/moral_validator.py`

---

### 3. 归零校准模块 (HDCM)

**职责**：在宇宙有限性（热寂/Heat Death）的调节性理念背景下，校准和深化答案

**检验维度**：

1. **归零检验**（Heat-Death Check）
   - 在承认宇宙最终热寂的前提下，此答案是否仍维护了理性的尊严？
   - 是否避免了虚无主义（Nihilism）或盲目乐观？

2. **校准透镜**（Calibration Lens）
   - 根据问题类型（伦理、认识论、美学），生成一句哲学箴言
   - 例如：*"尽管宇宙有限，道德律仍永恒有效"*

3. **阶段诊断**（Phase Diagnosis）
   - 当前回答对应的宇宙演化阶段（σ值）
   - 对应的思想特征

**输出**：
```json
{
  "calibrated_response": "经校准的最终答案",
  "heat_death_check": {
    "passed": true/false,
    "reason": "检验说明"
  },
  "calibration_type": "moral/epistemic/aesthetic/general",
  "cosmic_phase": "structure_formation / current_civilization / heat_death"
}
```

**宇宙阶段映射**（σ → 宇宙演化）：

| σ值 | 宇宙阶段 | 思想特征 | 时间 |
|-----|---------|---------|------|
| 0 | 大爆炸 | 原始统一性、最高对称性 | 奇点 |
| 1 | 结构形成 | 分化与整合、耗散结构 | 百万年后 |
| 1.5 | 当前文明 | 理性自我完成、复杂性峰值 | 现在 |
| 3 | 热寂/归零 | 无结构、最大熵、理性回归 | 亿年后 |

**代码位置**：`philosofia/core/heat_death_calibrator.py`

---

### 4. 宇宙上下文评估器 (CCE)

**职责**：根据问题的宇宙意义，评估当前时刻的演化状态

**输出**：
```json
{
  "time_phase": "current_civilization",
  "sigma_level": 1.5,
  "entropy_trend": "increasing",
  "heat_death_countdown": "~10^100 years",
  "implications": "在有限的宇宙框架内，人类伦理更显珍贵"
}
```

**代码位置**：`philosofia/core/cosmic_context.py`

---

### 5. 熵感知推理者 (EAR)

**职责**：评估答案的信息质量和认知秩序

**指标**：
- **熵分数**：信息混乱度（越低越好）
- **认知秩序**：逻辑一致性得分
- **压缩比**：答案的信息密度
- **预测力**：答案指导未来决策的能力

**输出**：
```json
{
  "entropy_score": 0.3,
  "cognitive_order": true,
  "compression_ratio": 0.85,
  "prediction_power": "high",
  "recommendation": "此答案具有高信息密度和实用价值"
}
```

**代码位置**：`philosofia/core/entropy_awareness.py`

---

### 6. 生灭周期建模器 (LCM)

**职责**：分析答案中涉及的关键概念的生命周期

**分析维度**：
- **萌生期** (σ ≈ -2)：新概念的孕育阶段
- **成长期** (σ ≈ -1 ~ 0)：概念的扩展和完善
- **成熟期** (σ ≈ 0.5 ~ 1.5)：概念的主流应用
- **衰退期** (σ ≈ 2 ~ 3)：概念向新范式过渡

**输出**：
```json
{
  "AI_rights": {
    "stage": "growth",
    "sigma": -0.5,
    "description": "新兴法律概念，正在全球范围内探索",
    "strategy": "需要跨学科的伦理论证"
  }
}
```

**代码位置**：`philosofia/core/lifecycle_modeler.py`

---

## 数据流与执行流程

### 完整工作流

```
1️⃣  输入 → ask_philosophically(question)
                ↓
2️⃣  创建 PAAS 实例
                ↓
3️⃣  NDSG.generate() → 获得三视角 + 初步合题
                ↓
4️⃣  循环（最多3次）{
      4a. 提取合题中的核心主张
      4b. MV.validate() → 执行三重检验
      4c. 若全部通过 → 退出循环
      4d. 若失败 → NDSG.generate_with_bias() → 重采样（降低σ）
    }
                ↓
5️⃣  HDCM.calibrate() → 宇宙校准
                ↓
6️⃣  CCE.estimate() → 宇宙上下文
                ↓
7️⃣  EAR.evaluate() → 熵感知评估
                ↓
8️⃣  LCM.analyze() → 生灭周期分析
                ↓
9️⃣  组装最终 JSON 输出（包含完整推理链）
                ↓
🔟 返回给用户
```

---

## LLM 接口抽象

**职责**：统一多个LLM后端的调用接口

**支持的后端**：
- `mock`: 本地模拟（用于测试）
- `openai`: OpenAI API (GPT-3.5/4)
- `qwen`: 通义千问 (Qwen)
- `deepseek`: DeepSeek API
- `volcano`: 火山引擎
- `local`: 本地Transformers模型

**接口定义**：
```python
class LLMInterface:
    def generate(self, prompt: str, **kwargs) -> str:
        """生成纯文本"""
    
    def generate_with_reasoning(self, prompt: str, **kwargs) -> dict:
        """生成并返回推理过程"""
```

**代码位置**：`philosofia/core/llm_interface.py`

---

## 推理链追踪

系统对每一步都进行记录：

```json
{
  "reasoning_chain": [
    {
      "step": 1,
      "name": "问题域分类",
      "description": "识别问题域：privacy_vs_security"
    },
    {
      "step": 2,
      "name": "正态采样生成",
      "description": "生成三视角（μ, +2σ, -2σ）"
    },
    ...
  ]
}
```

这让答案的推导过程完全透明和可复现。

---

## 扩展指南

### 添加新的问题域

编辑 `NormalDistributionSamplingGenerator.idea_distributions`：

```python
self.idea_distributions = {
    "your_domain": {
        "mu": "平衡观点...",
        "positive_tail": "激进观点...",
        "negative_tail": "保守观点...",
    },
    ...
}
```

### 自定义伦理检验规则

编辑 `MoralValidator._validate_with_rules()`：

```python
def _validate_with_rules(self, action: str, context: str) -> dict:
    # 添加你的自定义检验逻辑
    pass
```

### 集成新的 LLM 后端

继承 `LLMInterface`：

```python
class MyLLMBackend(LLMInterface):
    def generate(self, prompt: str, **kwargs) -> str:
        # 实现调用逻辑
        pass
```

---

## 性能考虑

| 操作 | 耗时 | 说明 |
|------|------|------|
| 本地模式 (use_llm=False) | < 100ms | 预设答案，极快 |
| Mock LLM | < 500ms | 本地模拟，可重现 |
| OpenAI API | 2-5s | 网络往返 + 推理 |
| 通义千问 API | 1-3s | 国内线路较快 |

---

## 参考论文与理论基础

- **康德伦理学**: I. Kant, *Groundwork for the Metaphysics of Morals* (1785)
- **宇宙热力学**: 第二热力学定律, 熵增原理
- **信息论**: C. Shannon, *A Mathematical Theory of Communication* (1948)
- **正态分布采样**: Box-Muller Transform, 逆变换采样法

