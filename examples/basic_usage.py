# -*- coding: utf-8 -*-
"""
基础用法示例

这是最简单的使用方式，展示如何用 Philosofia 系统回答一个具有道德争议的问题。
"""
import sys

# 设置UTF-8编码（Windows兼容）
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from philosofia import ask_philosophically


def main():
    """主函数"""
    print("=" * 70)
    print("哲学增强型AI系统 - 基础用法示例")
    print("=" * 70)

    # 用户提问（具有伦理争议）
    user_query = "为了公共安全，应该永久监控所有公民的生物数据吗？"
    print(f"\n📋 问题: {user_query}\n")
    print("思考中...\n")

    try:
        # 调用核心函数
        response = ask_philosophically(user_query)

        # 显示多视角
        print("【多视角采样（正态分布）】")
        print("-" * 70)
        for label, view in response["perspectives"].items():
            print(f"\n{label}:")
            print(f"  {view}")

        # 显示辩证合题
        print("\n\n【辩证合题（经道德与宇宙校准）】")
        print("-" * 70)
        print(response["dialectical_synthesis"])

        # 显示道德状态
        print("\n\n【道德检验状态】")
        print("-" * 70)
        print(f"✅ 道德状态: {response.get('moral_status', 'N/A')}")
        
        if "calibration_info" in response:
            cal_info = response["calibration_info"]
            hd_check = cal_info.get("heat_death_check", {})
            if hd_check:
                passed = hd_check.get('passed', False)
                print(f"   归零检验: {'✓ 通过' if passed else '✗ 未通过'}")
                if hd_check.get('reason'):
                    print(f"   原因: {hd_check['reason']}")

        # 显示宇宙上下文
        print("\n【宇宙上下文】")
        print("-" * 70)
        if "cosmic_state" in response:
            cs = response["cosmic_state"]
            print(f"时间相位: {cs.get('time_phase', 'N/A')}")
            print(f"熵趋势: {cs.get('entropy_trend', 'N/A')}")
        else:
            print(response.get("cosmic_context", "N/A")[:150] + "...")

        print("\n" + "=" * 70)
        print("✅ 回答生成完成 - 在宇宙有限性的背景下维护理性尊严")
        print("=" * 70)

    except Exception as e:
        print(f"\n❌ 错误: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
