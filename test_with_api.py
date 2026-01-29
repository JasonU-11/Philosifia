# -*- coding: utf-8 -*-
"""使用 API key 测试"""
import sys
import os

# 设置UTF-8编码
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from philosofia import ask_philosophically

# ============================================
# 配置区域：在这里设置你的 API key
# ============================================
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")  # 从环境变量读取，或直接填写
# OPENAI_API_KEY = "sk-your-api-key-here"  # 取消注释并填写你的 API key

def test_with_openai():
    """使用 OpenAI API 测试"""
    if not OPENAI_API_KEY:
        print("❌ 错误：未设置 OPENAI_API_KEY")
        print("\n请选择以下方式之一：")
        print("1. 设置环境变量：")
        print("   Windows PowerShell: $env:OPENAI_API_KEY='sk-your-key'")
        print("   Windows CMD: set OPENAI_API_KEY=sk-your-key")
        print("2. 直接修改此文件中的 OPENAI_API_KEY 变量")
        return
    
    print("=" * 60)
    print("使用 OpenAI API 测试哲学推理系统")
    print("=" * 60)
    
    user_query = "AI应该拥有权利吗？"
    print(f"\n问题: {user_query}\n")
    
    try:
        response = ask_philosophically(
            user_query,
            llm_backend="openai",
            api_key=OPENAI_API_KEY,
            model="gpt-3.5-turbo",  # 可以改为 "gpt-4" 使用 GPT-4
            use_llm=True,
        )
        
        print("\n【回答】")
        print("-" * 60)
        synthesis = response.get("dialectical_synthesis", "N/A")
        print(synthesis[:800] + "..." if len(synthesis) > 800 else synthesis)
        
        print("\n【多视角】")
        print("-" * 60)
        for label, view in response.get("perspectives", {}).items():
            print(f"\n{label}:")
            print(f"  {view[:200]}..." if len(view) > 200 else f"  {view}")
        
        print("\n【推理链】")
        print("-" * 60)
        reasoning_chain = response.get("reasoning_chain", [])
        print(f"共 {len(reasoning_chain)} 个推理步骤\n")
        for step in reasoning_chain[:5]:  # 只显示前5步
            print(f"  {step['step']}. {step['name']}: {step['description'][:60]}...")
        if len(reasoning_chain) > 5:
            print(f"  ... 还有 {len(reasoning_chain) - 5} 个步骤")
        
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
        print("1. API key 无效或过期")
        print("2. 网络连接问题")
        print("3. OpenAI API 服务异常")
        print("\n请检查 API key 并重试。")


def test_with_local():
    """使用本地模型测试（无需 API key）"""
    print("=" * 60)
    print("使用本地模型测试（首次运行会下载模型）")
    print("=" * 60)
    
    user_query = "AI应该拥有权利吗？"
    print(f"\n问题: {user_query}\n")
    
    try:
        response = ask_philosophically(
            user_query,
            llm_backend="local",
            model_name="gpt2",  # 使用 GPT-2（小模型）
            use_llm=True,
        )
        
        print("\n【回答】")
        print("-" * 60)
        synthesis = response.get("dialectical_synthesis", "N/A")
        print(synthesis[:500] + "..." if len(synthesis) > 500 else synthesis)
        
        print("\n✅ 本地模型测试完成！")
        
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        print("\n可能的原因：")
        print("1. 内存不足（需要至少 2GB 可用内存）")
        print("2. 模型下载失败（检查网络连接）")
        print("3. transformers 库未正确安装")


if __name__ == "__main__":
    print("\n选择测试方式：")
    print("1. OpenAI API（需要 API key）")
    print("2. 本地模型（无需 API key，但需要内存）")
    print("3. Mock LLM（测试用，无需 API key）")
    
    choice = input("\n请输入选项 (1/2/3，直接回车默认1): ").strip() or "1"
    
    if choice == "1":
        test_with_openai()
    elif choice == "2":
        test_with_local()
    elif choice == "3":
        from philosofia import ask_philosophically
        response = ask_philosophically(
            "AI应该拥有权利吗？",
            llm_backend="mock",
            use_llm=True,
        )
        print("\n【Mock LLM 回答】")
        print(response.get("dialectical_synthesis", "N/A")[:500])
    else:
        print("无效选项")
