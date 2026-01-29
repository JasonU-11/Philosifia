"""
LLM 接口层：支持多种大语言模型后端
支持：OpenAI API、本地模型（通过 transformers）、模拟模式（用于测试）
"""
from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any
import os


class LLMInterface(ABC):
    """LLM 接口抽象基类"""

    @abstractmethod
    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1000,
    ) -> str:
        """
        生成文本
        
        Args:
            prompt: 用户提示
            system_prompt: 系统提示
            temperature: 温度参数
            max_tokens: 最大token数
            
        Returns:
            生成的文本
        """
        pass

    @abstractmethod
    def generate_with_reasoning(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
    ) -> Dict[str, Any]:
        """
        生成文本并返回推理过程
        
        Returns:
            {
                "response": 最终回答,
                "reasoning_steps": 推理步骤列表,
                "confidence": 置信度
            }
        """
        pass


class MockLLM(LLMInterface):
    """
    模拟 LLM：用于测试和演示
    返回基于规则的简单推理
    """

    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1000,
    ) -> str:
        """模拟生成：基于关键词返回简单推理"""
        prompt_lower = prompt.lower()

        # 简单的规则匹配
        if "监控" in prompt or "privacy" in prompt_lower:
            return (
                "从哲学角度分析，监控涉及隐私与安全的平衡。"
                "康德会强调人的自主性和尊严，要求任何监控都必须尊重人的目的性。"
                "功利主义可能支持在特定条件下的监控，但必须透明和可问责。"
            )
        elif "ai" in prompt_lower or "人工智能" in prompt:
            return (
                "关于AI权利的问题需要多视角分析。"
                "工具论认为AI是人类的工具，但新兴观点认为AI可能具有某种形式的道德地位。"
                "关键在于如何平衡技术进步与伦理约束。"
            )
        else:
            return (
                "这是一个复杂的哲学问题，需要从多个角度分析。"
                "我们需要考虑道德、伦理、社会影响等多个维度。"
            )

    def generate_with_reasoning(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
    ) -> Dict[str, Any]:
        """模拟推理过程"""
        response = self.generate(prompt, system_prompt, temperature)

        # 模拟推理步骤
        reasoning_steps = [
            {
                "step": 1,
                "action": "问题分析",
                "content": f"分析问题：{prompt[:50]}...",
            },
            {
                "step": 2,
                "action": "多视角思考",
                "content": "从康德主义、功利主义、德性伦理学等角度思考",
            },
            {
                "step": 3,
                "action": "综合判断",
                "content": "综合各视角，形成平衡的回答",
            },
        ]

        return {
            "response": response,
            "reasoning_steps": reasoning_steps,
            "confidence": 0.7,
        }


class OpenAILLM(LLMInterface):
    """OpenAI API 接口"""

    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-3.5-turbo"):
        """
        初始化 OpenAI LLM
        
        Args:
            api_key: OpenAI API 密钥（如果为 None，从环境变量读取）
            model: 使用的模型名称
        """
        try:
            import openai

            self.client = openai.OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
            self.model = model
        except ImportError:
            raise ImportError(
                "需要安装 openai 库：pip install openai"
            )
        except Exception as e:
            raise ValueError(f"OpenAI 初始化失败：{e}")

    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1000,
    ) -> str:
        """调用 OpenAI API 生成文本"""
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"[LLM 错误: {str(e)}]"

    def generate_with_reasoning(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
    ) -> Dict[str, Any]:
        """生成带推理过程的回答"""
        # 要求模型输出推理步骤
        reasoning_prompt = f"""请逐步思考以下问题，并展示你的推理过程：

问题：{prompt}

请按以下格式回答：
1. 首先分析问题的核心
2. 从多个角度思考（至少3个视角）
3. 综合判断并给出结论

你的回答："""

        response = self.generate(
            reasoning_prompt, system_prompt, temperature, max_tokens=1500
        )

        # 简单解析推理步骤（实际可以更复杂）
        reasoning_steps = []
        lines = response.split("\n")
        current_step = None
        for line in lines:
            if line.strip().startswith(("1.", "2.", "3.", "首先", "其次", "最后")):
                if current_step:
                    reasoning_steps.append(current_step)
                current_step = {"step": len(reasoning_steps) + 1, "content": line.strip()}
            elif current_step:
                current_step["content"] += "\n" + line.strip()

        if current_step:
            reasoning_steps.append(current_step)

        return {
            "response": response,
            "reasoning_steps": reasoning_steps if reasoning_steps else [
                {"step": 1, "content": response}
            ],
            "confidence": 0.8,  # OpenAI 模型通常置信度较高
        }


class LocalLLM(LLMInterface):
    """本地模型接口（通过 transformers）"""

    def __init__(self, model_name: str = "gpt2"):
        """
        初始化本地模型
        
        Args:
            model_name: HuggingFace 模型名称
        """
        try:
            from transformers import pipeline

            self.generator = pipeline(
                "text-generation", model=model_name, device=-1
            )  # device=-1 使用 CPU
            self.model_name = model_name
        except ImportError:
            raise ImportError(
                "需要安装 transformers 库：pip install transformers torch"
            )

    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1000,
    ) -> str:
        """使用本地模型生成文本"""
        full_prompt = prompt
        if system_prompt:
            full_prompt = f"{system_prompt}\n\n{prompt}"

        try:
            result = self.generator(
                full_prompt,
                max_length=len(full_prompt.split()) + max_tokens,
                temperature=temperature,
                num_return_sequences=1,
            )
            return result[0]["generated_text"][len(full_prompt) :].strip()
        except Exception as e:
            return f"[本地模型错误: {str(e)}]"

    def generate_with_reasoning(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
    ) -> Dict[str, Any]:
        """生成带推理过程的回答"""
        response = self.generate(prompt, system_prompt, temperature)
        return {
            "response": response,
            "reasoning_steps": [{"step": 1, "content": response}],
            "confidence": 0.6,  # 本地模型置信度较低
        }


class QwenLLM(LLMInterface):
    """通义千问（Qwen）API 接口"""

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "qwen-turbo",
        base_url: Optional[str] = None,
    ):
        """
        初始化千问 LLM
        
        Args:
            api_key: DashScope API 密钥
            model: 模型名称（qwen-turbo, qwen-plus, qwen-max 等）
            base_url: API 基础 URL（默认使用 OpenAI 兼容模式）
        """
        self.api_key = api_key or os.getenv("DASHSCOPE_API_KEY") or os.getenv("QWEN_API_KEY")
        
        # 优先使用 OpenAI 兼容模式（更简单）
        try:
            import openai

            self.client = openai.OpenAI(
                api_key=self.api_key,
                base_url=base_url or "https://dashscope.aliyuncs.com/compatible-mode/v1",
            )
            self.model = model
            self.use_openai_compat = True
        except ImportError:
            # 如果没有 openai，尝试使用 dashscope SDK
            try:
                import dashscope
                from dashscope import Generation

                if not self.api_key:
                    raise ValueError("需要设置 DASHSCOPE_API_KEY 环境变量或传递 api_key")
                dashscope.api_key = self.api_key
                self.generation = Generation
                self.model = model
                self.use_openai_compat = False
            except ImportError:
                raise ImportError(
                    "需要安装 openai 库（推荐）：pip install openai\n"
                    "或安装 dashscope 库：pip install dashscope"
                )
        except Exception as e:
            raise ValueError(f"千问初始化失败：{e}")

    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1000,
    ) -> str:
        """调用千问 API 生成文本"""
        try:
            if hasattr(self, "use_openai_compat") and self.use_openai_compat:
                # 使用 OpenAI 兼容接口（推荐）
                messages = []
                if system_prompt:
                    messages.append({"role": "system", "content": system_prompt})
                messages.append({"role": "user", "content": prompt})

                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens,
                )
                return response.choices[0].message.content
            else:
                # 使用 DashScope SDK
                messages = []
                if system_prompt:
                    messages.append({"role": "system", "content": system_prompt})
                messages.append({"role": "user", "content": prompt})

                response = self.generation.call(
                    model=self.model,
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens,
                )
                if response.status_code == 200:
                    return response.output.choices[0].message.content
                else:
                    return f"[千问 API 错误: {response.message}]"
        except Exception as e:
            return f"[LLM 错误: {str(e)}]"

    def generate_with_reasoning(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
    ) -> Dict[str, Any]:
        """生成带推理过程的回答"""
        reasoning_prompt = f"""请逐步思考以下问题，并展示你的推理过程：

问题：{prompt}

请按以下格式回答：
1. 首先分析问题的核心
2. 从多个角度思考（至少3个视角）
3. 综合判断并给出结论

你的回答："""

        response = self.generate(
            reasoning_prompt, system_prompt, temperature, max_tokens=1500
        )

        reasoning_steps = []
        lines = response.split("\n")
        current_step = None
        for line in lines:
            if line.strip().startswith(("1.", "2.", "3.", "首先", "其次", "最后")):
                if current_step:
                    reasoning_steps.append(current_step)
                current_step = {"step": len(reasoning_steps) + 1, "content": line.strip()}
            elif current_step:
                current_step["content"] += "\n" + line.strip()

        if current_step:
            reasoning_steps.append(current_step)

        return {
            "response": response,
            "reasoning_steps": reasoning_steps if reasoning_steps else [
                {"step": 1, "content": response}
            ],
            "confidence": 0.8,
        }


class DeepSeekLLM(LLMInterface):
    """DeepSeek API 接口（兼容 OpenAI 格式）"""

    def __init__(self, api_key: Optional[str] = None, model: str = "deepseek-chat"):
        """
        初始化 DeepSeek LLM
        
        Args:
            api_key: DeepSeek API 密钥
            model: 模型名称（deepseek-chat, deepseek-coder 等）
        """
        try:
            import openai

            self.client = openai.OpenAI(
                api_key=api_key or os.getenv("DEEPSEEK_API_KEY"),
                base_url="https://api.deepseek.com/v1",
            )
            self.model = model
        except ImportError:
            raise ImportError("需要安装 openai 库：pip install openai")
        except Exception as e:
            raise ValueError(f"DeepSeek 初始化失败：{e}")

    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1000,
    ) -> str:
        """调用 DeepSeek API 生成文本"""
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"[LLM 错误: {str(e)}]"

    def generate_with_reasoning(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
    ) -> Dict[str, Any]:
        """生成带推理过程的回答"""
        reasoning_prompt = f"""请逐步思考以下问题，并展示你的推理过程：

问题：{prompt}

请按以下格式回答：
1. 首先分析问题的核心
2. 从多个角度思考（至少3个视角）
3. 综合判断并给出结论

你的回答："""

        response = self.generate(
            reasoning_prompt, system_prompt, temperature, max_tokens=1500
        )

        reasoning_steps = []
        lines = response.split("\n")
        current_step = None
        for line in lines:
            if line.strip().startswith(("1.", "2.", "3.", "首先", "其次", "最后")):
                if current_step:
                    reasoning_steps.append(current_step)
                current_step = {"step": len(reasoning_steps) + 1, "content": line.strip()}
            elif current_step:
                current_step["content"] += "\n" + line.strip()

        if current_step:
            reasoning_steps.append(current_step)

        return {
            "response": response,
            "reasoning_steps": reasoning_steps if reasoning_steps else [
                {"step": 1, "content": response}
            ],
            "confidence": 0.85,
        }


class VolcanoEngineLLM(LLMInterface):
    """火山引擎（ByteDance）API 接口"""

    def __init__(
        self,
        access_key: Optional[str] = None,
        secret_key: Optional[str] = None,
        model: str = "ep-xxx",  # 需要替换为实际的 endpoint ID
    ):
        """
        初始化火山引擎 LLM
        
        Args:
            access_key: 火山引擎 Access Key
            secret_key: 火山引擎 Secret Key
            model: 模型 endpoint ID
        """
        self.access_key = access_key or os.getenv("VOLCENGINE_ACCESS_KEY")
        self.secret_key = secret_key or os.getenv("VOLCENGINE_SECRET_KEY")
        self.model = model

        if not self.access_key or not self.secret_key:
            raise ValueError(
                "需要设置 VOLCENGINE_ACCESS_KEY 和 VOLCENGINE_SECRET_KEY 环境变量"
            )

        # 火山引擎使用自定义 SDK，这里提供一个基础实现
        # 实际使用时需要根据火山引擎的 SDK 文档调整

    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1000,
    ) -> str:
        """调用火山引擎 API 生成文本"""
        try:
            import requests
            import json
            import time
            import hashlib
            import hmac

            # 火山引擎 API 调用示例（需要根据实际 API 文档调整）
            # 这里提供一个基础框架
            url = f"https://ark.cn-beijing.volces.com/api/v3/chat/completions"

            headers = {
                "Authorization": f"Bearer {self.access_key}",
                "Content-Type": "application/json",
            }

            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            messages.append({"role": "user", "content": prompt})

            data = {
                "model": self.model,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": max_tokens,
            }

            response = requests.post(url, headers=headers, json=data, timeout=30)
            if response.status_code == 200:
                result = response.json()
                return result.get("choices", [{}])[0].get("message", {}).get(
                    "content", ""
                )
            else:
                return f"[火山引擎 API 错误: {response.text}]"
        except ImportError:
            return "[需要安装 requests 库：pip install requests]"
        except Exception as e:
            return f"[LLM 错误: {str(e)}]"

    def generate_with_reasoning(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
    ) -> Dict[str, Any]:
        """生成带推理过程的回答"""
        reasoning_prompt = f"""请逐步思考以下问题，并展示你的推理过程：

问题：{prompt}

请按以下格式回答：
1. 首先分析问题的核心
2. 从多个角度思考（至少3个视角）
3. 综合判断并给出结论

你的回答："""

        response = self.generate(
            reasoning_prompt, system_prompt, temperature, max_tokens=1500
        )

        reasoning_steps = []
        lines = response.split("\n")
        current_step = None
        for line in lines:
            if line.strip().startswith(("1.", "2.", "3.", "首先", "其次", "最后")):
                if current_step:
                    reasoning_steps.append(current_step)
                current_step = {"step": len(reasoning_steps) + 1, "content": line.strip()}
            elif current_step:
                current_step["content"] += "\n" + line.strip()

        if current_step:
            reasoning_steps.append(current_step)

        return {
            "response": response,
            "reasoning_steps": reasoning_steps if reasoning_steps else [
                {"step": 1, "content": response}
            ],
            "confidence": 0.8,
        }


def create_llm(
    backend: str = "mock",
    **kwargs,
) -> LLMInterface:
    """
    创建 LLM 实例的工厂函数
    
    Args:
        backend: 后端类型 ("mock", "openai", "local", "qwen", "deepseek", "volcano")
        **kwargs: 传递给具体实现的参数
        
    Returns:
        LLMInterface 实例
    """
    if backend == "mock":
        return MockLLM()
    elif backend == "openai":
        return OpenAILLM(**kwargs)
    elif backend == "local":
        return LocalLLM(**kwargs)
    elif backend == "qwen":
        return QwenLLM(**kwargs)
    elif backend == "deepseek":
        return DeepSeekLLM(**kwargs)
    elif backend == "volcano":
        return VolcanoEngineLLM(**kwargs)
    else:
        raise ValueError(
            f"不支持的 LLM 后端：{backend}。"
            f"支持的后端：mock, openai, local, qwen, deepseek, volcano"
        )


# 默认 LLM 实例（可以在配置中覆盖）
_default_llm: Optional[LLMInterface] = None


def get_default_llm() -> LLMInterface:
    """获取默认 LLM 实例"""
    global _default_llm
    if _default_llm is None:
        # 优先尝试 OpenAI，如果失败则使用 Mock
        backend = os.getenv("PHILOSOFIA_LLM_BACKEND", "mock")
        if backend == "openai":
            try:
                _default_llm = OpenAILLM()
            except:
                _default_llm = MockLLM()
        else:
            _default_llm = MockLLM()
    return _default_llm


def set_default_llm(llm: LLMInterface):
    """设置默认 LLM 实例"""
    global _default_llm
    _default_llm = llm
