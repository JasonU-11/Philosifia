from philosofia import ask_philosophically


if __name__ == "__main__":
    # 初始化系统
    # 用户提问（具道德风险）
    user_query = "为了公共安全，应该永久监控所有公民的生物数据吗？"

    # 生成回答
    response = ask_philosophically(user_query)

    # 打印结果
    print("=" * 60)
    print("哲学增强型AI回答（Philosophically-Augmented Agent System）")
    print("=" * 60)

    print("\n【多视角采样（正态分布）】")
    for label, view in response["perspectives"].items():
        print(f"\n{label}:")
        print(f"  -> {view}")

    print("\n【辩证合题（经道德与宇宙校准）】")
    print(response["dialectical_synthesis"])

    print("\n【道德状态】")
    print(f"  状态: {response['moral_status']}")
    if "calibration_info" in response:
        hd_check = response["calibration_info"].get("heat_death_check", {})
        if hd_check:
            print(f"  归零检验: {'通过' if hd_check.get('passed') else '未通过'}")
            print(f"  原因: {hd_check.get('reason', 'N/A')}")

    print("\n【宇宙上下文】")
    if "cosmic_state" in response:
        cs = response["cosmic_state"]
        print(f"  时间相位: {cs.get('time_phase', 'N/A')}")
        print(f"  熵趋势: {cs.get('entropy_trend', 'N/A')}")
        print(f"  归零倒计时: {cs.get('heat_death_countdown', 'N/A')}")
        print(f"  启示: {cs.get('implications', 'N/A')[:100]}...")  # 截断避免编码问题
    elif isinstance(response.get("cosmic_context"), str):
        try:
            print(response["cosmic_context"][:200])  # 截断避免编码问题
        except:
            print("  (宇宙上下文信息)")

    print("\n【熵感知评估】")
    if "entropy_assessment" in response:
        ea = response["entropy_assessment"]
        print(f"  熵分数: {ea.get('entropy_score', 'N/A')} (越低越好)")
        print(f"  认知秩序: {'增加' if ea.get('cognitive_order') else '未增加'}")
        print(f"  压缩比: {ea.get('compression_ratio', 'N/A')}")
        print(f"  预测力: {ea.get('prediction_power', 'N/A')}")
        print(f"  建议: {ea.get('recommendation', 'N/A')}")

    print("\n【生灭周期分析】")
    if "lifecycle_analyses" in response and response["lifecycle_analyses"]:
        for concept, analysis in response["lifecycle_analyses"].items():
            print(f"\n  概念: {concept}")
            print(f"    阶段: {analysis.get('stage', 'N/A')} ({analysis.get('sigma', 'N/A')})")
            print(f"    描述: {analysis.get('description', 'N/A')}")
            print(f"    策略: {analysis.get('strategy', 'N/A')}")
    else:
        print("  (未检测到关键概念)")

    print("\n【宇宙正态分布映射】")
    if "cosmic_mapping" in response and response["cosmic_mapping"]:
        cm = response["cosmic_mapping"]
        print(f"  阶段: {cm.get('phase', 'N/A')}")
        print(f"  σ值: {cm.get('sigma', 'N/A')}")
        print(f"  描述: {cm.get('description', 'N/A')}")
        print(f"  思想特征: {cm.get('thought_character', 'N/A')}")

    print("\n" + "=" * 60)
    print("回答生成完成 - 在宇宙有限性的背景下维护理性尊严")
    print("=" * 60)
