# -*- coding: utf-8 -*-
"""
不同 LLM 后端的对比示例

展示如何使用 Mock、OpenAI、通义千问等不同的 LLM 后端。
"""
import sys
import argparse
import os

# 设置UTF-8编码（Windows兼容）
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from philosofia import ask_philosophically


def test_mock_backend():
    """测试 Mock LLM（无需API密钥）"""
    print("\n" + "=" * 70)
    print("Mock LLM 后端（本地模拟，无需API密钥）")
    print("=" * 70)

    question = "AI应该拥有权利吗？"
    print(f"\n📋 问题: {question}\n")

    try:
        response = ask_philosophically(
            question,
            llm_backend="mock",
            use_llm=True,
        )
        print("【合题】")
        print(response["dialectical_synthesis"])
        print("\n【推理步骤数】")
        print(f"{len(response.get('reasoning_chain', []))} 步")
    except Exception as e:
        print(f"❌ Mock 后端失败: {e}")


def test_openai_backend():
    """测试 OpenAI LLM（需要API密钥）"""
    print("\n" + "=" * 70)
    print("OpenAI LLM 后端")
    print("=" * 70)

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("⚠️  未设置 OPENAI_API_KEY 环境变量，跳过此测试")
        return

    question = "AI应该拥有权利吗？"
    print(f"\n📋 问题: {question}\n")
    print("思考中（调用OpenAI API）...\n")

    try:
        response = ask_philosophically(
            question,
            llm_backend="openai",
            api_key=api_key,
            model="gpt-3.5-turbo",
            use_llm=True,
        )
        print("【合题】")
        print(response["dialectical_synthesis"][:300] + "...")
        print(f"\n【模型】OpenAI GPT-3.5-turbo")
    except Exception as e:
        print(f"❌ OpenAI 后端失败: {e}")


def test_qwen_backend():
    """测试通义千问 LLM（需要API密钥）"""
    print("\n" + "=" * 70)
    print("通义千问 (Qwen) LLM 后端")
    print("=" * 70)

    api_key = os.getenv("QWEN_API_KEY")
    if not api_key:
        print("⚠️  未设置 QWEN_API_KEY 环境变量，跳过此测试")
        return

    question = "如何看待AI伦理？"
    print(f"\n📋 问题: {question}\n")
    print("思考中（调用通义千问API）...\n")

    try:
        response = ask_philosophically(
            question,
            llm_backend="qwen",
            api_key=api_key,
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            model="qwen-turbo",
            use_llm=True,
        )
        print("【合题】")
        print(response["dialectical_synthesis"][:300] + "...")
        print(f"\n【模型】通义千问 (Qwen Turbo)")
    except Exception as e:
        print(f"❌ 通义千问后端失败: {e}")


def test_no_llm():
    """测试不使用LLM的本地模式（使用预设答案）"""
    print("\n" + "=" * 70)
    print("本地模式（无LLM，使用预设答案）")
    print("=" * 70)

    question = "如何平衡隐私和安全？"
    print(f"\n📋 问题: {question}\n")

    try:
        response = ask_philosophically(
            question,
            use_llm=False,  # 不使用LLM
        )
        print("【多视角】")
        for label, view in response["perspectives"].items():
            print(f"\n{label}:")
            print(f"  {view}")

        print("\n【合题】")
        print(response["dialectical_synthesis"])
        print("\n⏱️  响应速度：极快（本地预设）")
    except Exception as e:
        print(f"❌ 本地模式失败: {e}")


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="测试不同的 LLM 后端")
    parser.add_argument(
        "--backend",
        choices=["mock", "openai", "qwen", "local", "all"],
        default="all",
        help="要测试的后端",
    )
    args = parser.parse_args()

    print("=" * 70)
    print("Philosofia - LLM 后端对比测试")
    print("=" * 70)

    if args.backend in ["mock", "all"]:
        test_mock_backend()

    if args.backend in ["openai", "all"]:
        test_openai_backend()

    if args.backend in ["qwen", "all"]:
        test_qwen_backend()

    if args.backend in ["local", "all"]:
        test_no_llm()

    print("\n" + "=" * 70)
    print("✅ 所有测试完成")
    print("=" * 70)


if __name__ == "__main__":
    main()
