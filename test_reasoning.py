# -*- coding: utf-8 -*-
"""测试推理能力"""
import sys
import json

# 设置UTF-8编码
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from philosofia import ask_philosophically

def test_reasoning():
    """测试推理能力"""
    print("=" * 60)
    print("测试哲学推理系统 - 推理链追踪")
    print("=" * 60)
    
    user_query = "AI应该拥有权利吗？"
    print(f"\n问题: {user_query}\n")
    
    # 使用 Mock LLM 进行推理
    response = ask_philosophically(
        user_query,
        llm_backend="mock",
        use_llm=True,
    )
    
    print("\n【推理链追踪】")
    print("-" * 60)
    for step in response.get("reasoning_chain", []):
        print(f"\n步骤 {step['step']}: {step['name']}")
        print(f"  描述: {step['description']}")
        if "details" in step:
            details = step["details"]
            if isinstance(details, dict):
                if "reasoning_steps" in details:
                    print(f"  推理步骤数: {len(details['reasoning_steps'])}")
                if "confidence" in details:
                    print(f"  置信度: {details['confidence']}")
    
    print("\n" + "-" * 60)
    print("\n【最终回答】")
    print(response.get("dialectical_synthesis", "N/A")[:200] + "...")
    
    print("\n【多视角】")
    for label, view in response.get("perspectives", {}).items():
        print(f"  {label}: {view[:80]}...")
    
    print("\n" + "=" * 60)
    print("推理链追踪完成！")
    print("=" * 60)
    
    # 保存完整响应
    try:
        with open("reasoning_test.json", "w", encoding="utf-8") as f:
            json.dump(response, f, ensure_ascii=False, indent=2)
        print("\n完整响应已保存到 reasoning_test.json")
    except Exception as e:
        print(f"\n保存失败: {e}")

if __name__ == "__main__":
    test_reasoning()
