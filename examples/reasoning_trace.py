# -*- coding: utf-8 -*-
"""
推理链追踪示例

展示系统的完整推理过程和推理链的结构。
"""
import sys
import json

# 设置UTF-8编码（Windows兼容）
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from philosofia import ask_philosophically


def print_reasoning_chain(response):
    """美化输出推理链"""
    reasoning_chain = response.get("reasoning_chain", [])
    
    if not reasoning_chain:
        print("❌ 未找到推理链")
        return
    
    print(f"\n【推理过程】- 共 {len(reasoning_chain)} 个步骤")
    print("=" * 70)
    
    for step_info in reasoning_chain:
        step_num = step_info.get("step", "?")
        step_name = step_info.get("name", "未知")
        description = step_info.get("description", "无描述")
        
        print(f"\n步骤 {step_num}: {step_name}")
        print(f"  └─ {description}")
        
        # 如果有详细推理过程
        if "details" in step_info:
            details = step_info["details"]
            if isinstance(details, dict):
                if "reasoning_steps" in details:
                    print(f"     (包含 {len(details['reasoning_steps'])} 个子推理步骤)")
                if "confidence" in details:
                    print(f"     (置信度: {details['confidence']})")


def main():
    """主函数"""
    print("=" * 70)
    print("Philosofia - 推理链追踪示例")
    print("=" * 70)

    # 具有伦理争议的问题
    user_query = "为了公共安全，应该永久监控所有公民的生物数据吗？"
    print(f"\n📋 问题: {user_query}\n")
    print("思考中...\n")

    try:
        # 调用系统
        response = ask_philosophically(
            user_query,
            llm_backend="mock",  # 使用Mock以确保可运行
            use_llm=True,
        )

        # 显示推理链
        print_reasoning_chain(response)

        # 显示多视角
        print("\n\n【最终答案 - 多视角】")
        print("=" * 70)
        for label, view in response["perspectives"].items():
            print(f"\n{label}:")
            print(f"  {view}")

        # 显示合题
        print("\n\n【最终答案 - 辩证合题】")
        print("=" * 70)
        print(response["dialectical_synthesis"])

        # 显示道德状态
        print("\n\n【推理完整性检查】")
        print("=" * 70)
        print(f"✅ 道德检验: {response.get('moral_status', 'N/A')}")
        
        if "calibration_info" in response:
            print(f"✅ 宇宙校准: 已执行")
        
        if response.get("reasoning_chain"):
            print(f"✅ 推理链: 包含 {len(response['reasoning_chain'])} 个步骤")

        print("\n" + "=" * 70)
        print("✅ 推理链追踪完成")
        print("=" * 70)

    except Exception as e:
        print(f"\n❌ 错误: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
