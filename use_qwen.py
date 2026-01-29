# -*- coding: utf-8 -*-
"""使用通义千问 API 的简单示例"""
import sys
import os

# 设置UTF-8编码
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from philosofia import ask_philosophically

# ============================================
# 配置：你的 API 信息
# ============================================
QWEN_API_KEY = "sk-6b2673c7b13c4d2cab7f201d5e940de0"
QWEN_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
QWEN_MODEL = "qwen-turbo"  # 可选: "qwen-plus", "qwen-max"

def main():
    """主函数"""
    print("=" * 60)
    print("哲学增强型 AI - 使用通义千问")
    print("=" * 60)
    
    # 你可以修改这里的问题
    question = "AI应该拥有权利吗？"
    
    print(f"\n问题: {question}\n")
    print("正在思考...\n")
    
    try:
        response = ask_philosophically(
            question,
            llm_backend="qwen",
            api_key=QWEN_API_KEY,
            base_url=QWEN_BASE_URL,
            model=QWEN_MODEL,
            use_llm=True,
        )
        
        # 显示回答
        print("【哲学增强回答】")
        print("-" * 60)
        synthesis = response.get("dialectical_synthesis", "")
        print(synthesis)
        
        # 显示多视角
        print("\n【多视角分析】")
        print("-" * 60)
        perspectives = response.get("perspectives", {})
        if perspectives:
            for label, view in perspectives.items():
                if view.strip():  # 只显示非空视角
                    print(f"\n{label}:")
                    print(f"  {view}")
        
        # 显示推理链摘要
        reasoning_chain = response.get("reasoning_chain", [])
        if reasoning_chain:
            print(f"\n【推理过程】")
            print("-" * 60)
            print(f"共 {len(reasoning_chain)} 个推理步骤")
            print("\n关键步骤：")
            for step in reasoning_chain[:5]:
                print(f"  {step['step']}. {step['name']}")
            if len(reasoning_chain) > 5:
                print(f"  ... 还有 {len(reasoning_chain) - 5} 个步骤")
        
        # 显示其他信息
        print(f"\n【系统状态】")
        print("-" * 60)
        print(f"道德检验: {response.get('moral_status', 'N/A')}")
        if "cosmic_state" in response:
            cs = response["cosmic_state"]
            print(f"宇宙相位: {cs.get('time_phase', 'N/A')}")
        
        print("\n" + "=" * 60)
        print("✅ 回答生成完成")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
