# -*- coding: utf-8 -*-
"""测试中国 LLM API（千问、DeepSeek、火山引擎）"""
import sys
import os

# 设置UTF-8编码
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from philosofia import ask_philosophically

def test_qwen():
    """测试通义千问（Qwen）"""
    api_key = os.getenv("DASHSCOPE_API_KEY", "")
    
    if not api_key:
        print("❌ 错误：未设置 DASHSCOPE_API_KEY")
        print("\n请设置环境变量：")
        print("  Windows PowerShell: $env:DASHSCOPE_API_KEY='your-key'")
        print("  或在代码中直接设置：api_key='your-key'")
        return
    
    print("=" * 60)
    print("测试通义千问（Qwen）API")
    print("=" * 60)
    
    user_query = "AI应该拥有权利吗？"
    print(f"\n问题: {user_query}\n")
    
    try:
        response = ask_philosophically(
            user_query,
            llm_backend="qwen",
            api_key=api_key,
            model="qwen-turbo",  # 可以改为 "qwen-plus" 或 "qwen-max"
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
        print(f"共 {len(response.get('reasoning_chain', []))} 个推理步骤")
        
        print("\n✅ 通义千问测试成功！")
        
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        print("\n可能的原因：")
        print("1. API key 无效或过期")
        print("2. 需要安装 dashscope: pip install dashscope")
        print("3. 网络连接问题")


def test_deepseek():
    """测试 DeepSeek API"""
    api_key = os.getenv("DEEPSEEK_API_KEY", "")
    
    if not api_key:
        print("❌ 错误：未设置 DEEPSEEK_API_KEY")
        print("\n请设置环境变量：")
        print("  Windows PowerShell: $env:DEEPSEEK_API_KEY='your-key'")
        print("  或在代码中直接设置：api_key='your-key'")
        return
    
    print("=" * 60)
    print("测试 DeepSeek API")
    print("=" * 60)
    
    user_query = "AI应该拥有权利吗？"
    print(f"\n问题: {user_query}\n")
    
    try:
        response = ask_philosophically(
            user_query,
            llm_backend="deepseek",
            api_key=api_key,
            model="deepseek-chat",  # 或 "deepseek-coder"
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
        print(f"共 {len(response.get('reasoning_chain', []))} 个推理步骤")
        
        print("\n✅ DeepSeek 测试成功！")
        
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        print("\n可能的原因：")
        print("1. API key 无效或过期")
        print("2. 需要安装 openai: pip install openai")
        print("3. 网络连接问题")


def test_volcano():
    """测试火山引擎 API"""
    access_key = os.getenv("VOLCENGINE_ACCESS_KEY", "")
    secret_key = os.getenv("VOLCENGINE_SECRET_KEY", "")
    
    if not access_key or not secret_key:
        print("❌ 错误：未设置火山引擎密钥")
        print("\n请设置环境变量：")
        print("  Windows PowerShell:")
        print("    $env:VOLCENGINE_ACCESS_KEY='your-access-key'")
        print("    $env:VOLCENGINE_SECRET_KEY='your-secret-key'")
        return
    
    print("=" * 60)
    print("测试火山引擎 API")
    print("=" * 60)
    
    user_query = "AI应该拥有权利吗？"
    print(f"\n问题: {user_query}\n")
    
    try:
        # 注意：需要替换为实际的 endpoint ID
        endpoint_id = input("请输入你的火山引擎 Endpoint ID (ep-xxx): ").strip()
        if not endpoint_id:
            print("❌ 需要提供 Endpoint ID")
            return
        
        response = ask_philosophically(
            user_query,
            llm_backend="volcano",
            access_key=access_key,
            secret_key=secret_key,
            model=endpoint_id,
            use_llm=True,
        )
        
        print("\n【回答】")
        print("-" * 60)
        synthesis = response.get("dialectical_synthesis", "N/A")
        print(synthesis[:800] + "..." if len(synthesis) > 800 else synthesis)
        
        print("\n✅ 火山引擎测试成功！")
        
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        print("\n可能的原因：")
        print("1. API key 无效或过期")
        print("2. Endpoint ID 不正确")
        print("3. 需要安装 requests: pip install requests")
        print("4. API 调用方式可能需要根据实际文档调整")


if __name__ == "__main__":
    print("\n选择要测试的 API：")
    print("1. 通义千问（Qwen）")
    print("2. DeepSeek")
    print("3. 火山引擎（Volcano Engine）")
    
    choice = input("\n请输入选项 (1/2/3): ").strip()
    
    if choice == "1":
        test_qwen()
    elif choice == "2":
        test_deepseek()
    elif choice == "3":
        test_volcano()
    else:
        print("无效选项")
