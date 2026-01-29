"""
配置示例：如何使用不同的 LLM 后端
"""
from philosofia import ask_philosophically

# 示例1：使用 Mock LLM（默认，用于测试）
def example_mock():
    response = ask_philosophically(
        "为了公共安全，应该永久监控所有公民吗？",
        llm_backend="mock",
        use_llm=True,
    )
    print("Mock LLM 响应：")
    print(response["dialectical_synthesis"])
    print("\n推理链：")
    for step in response.get("reasoning_chain", []):
        print(f"  {step['step']}. {step['name']}: {step['description']}")


# 示例2：使用 OpenAI API（需要设置 OPENAI_API_KEY 环境变量）
def example_openai():
    import os

    # 方式1：通过环境变量
    # export OPENAI_API_KEY="your-api-key"
    # response = ask_philosophically("问题", llm_backend="openai")

    # 方式2：直接传递 API key
    response = ask_philosophically(
        "为了公共安全，应该永久监控所有公民吗？",
        llm_backend="openai",
        api_key=os.getenv("OPENAI_API_KEY"),
        model="gpt-3.5-turbo",  # 或 "gpt-4"
        use_llm=True,
    )
    print("OpenAI LLM 响应：")
    print(response["dialectical_synthesis"])


# 示例3：使用本地模型（需要安装 transformers）
def example_local():
    response = ask_philosophically(
        "为了公共安全，应该永久监控所有公民吗？",
        llm_backend="local",
        model_name="gpt2",  # 或其他 HuggingFace 模型
        use_llm=True,
    )
    print("本地 LLM 响应：")
    print(response["dialectical_synthesis"])


# 示例4：不使用 LLM，使用预设答案（快速但无推理）
def example_preset():
    response = ask_philosophically(
        "为了公共安全，应该永久监控所有公民吗？",
        use_llm=False,  # 使用预设答案
    )
    print("预设答案响应：")
    print(response["dialectical_synthesis"])


if __name__ == "__main__":
    print("=" * 60)
    print("配置示例")
    print("=" * 60)

    print("\n1. Mock LLM（默认）：")
    example_mock()

    # 取消注释以测试其他后端
    # print("\n2. OpenAI API：")
    # example_openai()

    # print("\n3. 本地模型：")
    # example_local()

    # print("\n4. 预设答案：")
    # example_preset()
