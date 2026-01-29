# -*- coding: utf-8 -*-
"""直接测试通义千问 API（使用用户提供的配置）"""
import sys
import os

# 设置UTF-8编码
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from philosofia import ask_philosophically

# ============================================
# 配置：使用你提供的 API key
# ============================================
QWEN_API_KEY = "sk-6b2673c7b13c4d2cab7f201d5e940de0"
QWEN_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
QWEN_MODEL = "qwen-turbo"  # 可以改为 "qwen-plus" 或 "qwen-max"

def test_qwen():
    """测试通义千问"""
    print("=" * 60)
    print("测试通义千问（Qwen）API")
    print("=" * 60)
    print(f"\nAPI Key: {QWEN_API_KEY[:20]}...")
    print(f"Base URL: {QWEN_BASE_URL}")
    print(f"Model: {QWEN_MODEL}\n")
    
    user_query = "读硕士拿文凭还是直接投身强人工智能公司创业更值？"
    print(f"问题: {user_query}\n")
    
    try:
        response = ask_philosophically(
            user_query,
            llm_backend="qwen",
            api_key=QWEN_API_KEY,
            base_url=QWEN_BASE_URL,
            model=QWEN_MODEL,
            use_llm=True,
        )
        
        print("\n【回答】")
        print("-" * 60)
        synthesis = response.get("dialectical_synthesis", "N/A")
        print(synthesis[:1000] + "..." if len(synthesis) > 1000 else synthesis)
        
        print("\n【多视角】")
        print("-" * 60)
        for label, view in response.get("perspectives", {}).items():
            print(f"\n{label}:")
            print(f"  {view[:300]}..." if len(view) > 300 else f"  {view}")
        
        print("\n【推理链】")
        print("-" * 60)
        reasoning_chain = response.get("reasoning_chain", [])
        print(f"共 {len(reasoning_chain)} 个推理步骤\n")
        for step in reasoning_chain[:8]:  # 显示前8步
            print(f"  {step['step']}. {step['name']}: {step['description'][:60]}...")
        if len(reasoning_chain) > 8:
            print(f"  ... 还有 {len(reasoning_chain) - 8} 个步骤")
        
        print("\n【其他信息】")
        print("-" * 60)
        print(f"道德状态: {response.get('moral_status', 'N/A')}")
        if "cosmic_state" in response:
            cs = response["cosmic_state"]
            print(f"宇宙相位: {cs.get('time_phase', 'N/A')}")
        
        print("\n" + "=" * 60)
        print("✅ 测试成功！")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        print("\n可能的原因：")
        print("1. 需要安装 openai 库：pip install openai")
        print("2. API key 无效或过期")
        print("3. 网络连接问题")
        print("4. 模型名称不正确")
        import traceback
        print("\n详细错误信息：")
        traceback.print_exc()


def test_custom_question():
    """测试自定义问题"""
    print("\n" + "=" * 60)
    print("测试自定义问题")
    print("=" * 60)
    
    custom_question = input("\n请输入你的问题（直接回车使用默认问题）: ").strip()
    if not custom_question:
        custom_question = "为了公共安全，应该永久监控所有公民吗？"
    
    print(f"\n问题: {custom_question}\n")
    
    try:
        response = ask_philosophically(
            custom_question,
            llm_backend="qwen",
            api_key=QWEN_API_KEY,
            base_url=QWEN_BASE_URL,
            model=QWEN_MODEL,
            use_llm=True,
        )
        
        print("\n【回答】")
        print("-" * 60)
        synthesis = response.get("dialectical_synthesis", "N/A")
        print(synthesis[:1000] + "..." if len(synthesis) > 1000 else synthesis)
        
        print("\n【多视角】")
        print("-" * 60)
        for label, view in response.get("perspectives", {}).items():
            print(f"\n{label}:")
            print(f"  {view[:200]}..." if len(view) > 200 else f"  {view}")
        
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    # 检查是否安装了 openai
    try:
        import openai
        print("✅ openai 库已安装\n")
    except ImportError:
        print("❌ 需要安装 openai 库")
        print("运行: pip install openai\n")
        exit(1)
    
    # 运行测试
    test_qwen()
    
    # 询问是否测试自定义问题（非交互模式下跳过）
    try:
        choice = input("\n是否测试自定义问题？(y/n): ").strip().lower()
        if choice == 'y':
            test_custom_question()
    except (EOFError, KeyboardInterrupt):
        print("\n测试完成。")
