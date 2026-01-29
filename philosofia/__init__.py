from typing import Optional

from .core.agent_system import PhilosophicallyAugmentedAgentSystem
from .core.llm_interface import LLMInterface, create_llm, get_default_llm

__version__ = "0.1.0"


def ask_philosophically(
    question: str,
    llm_backend: str = "mock",
    use_llm: bool = True,
    **llm_kwargs,
) -> dict:
    """
    对输入问题给出哲学增强回答。
    
    Args:
        question: 用户问题
        llm_backend: LLM 后端类型 ("mock", "openai", "local", "qwen", "deepseek", "volcano")
        use_llm: 是否使用 LLM 进行推理（False 则使用预设答案）
        **llm_kwargs: 传递给 LLM 的参数（如 api_key, model 等）
        
    Returns:
        包含回答和推理链的字典
    """
    # 创建 LLM 实例
    if use_llm:
        llm = create_llm(backend=llm_backend, **llm_kwargs)
    else:
        llm = None

    # 创建智能体系统
    agent = PhilosophicallyAugmentedAgentSystem(llm=llm, use_llm=use_llm)
    return agent.respond(question)