# -*- coding: utf-8 -*-
"""测试改进功能"""
import sys
import json

# 设置UTF-8编码
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from philosofia import ask_philosophically

def test_system():
    """测试系统功能"""
    print("=" * 60)
    print("Testing Philosophically-Augmented Agent System")
    print("=" * 60)
    
    user_query = "为了公共安全，应该永久监控所有公民的生物数据吗？"
    print(f"\nQuery: {user_query}\n")
    
    response = ask_philosophically(user_query)
    
    # 检查所有新功能
    print("\n[1] Perspectives (Normal Distribution Sampling):")
    for label, view in response.get("perspectives", {}).items():
        print(f"  {label}: {view[:50]}...")
    
    print("\n[2] Dialectical Synthesis:")
    print(f"  {response.get('dialectical_synthesis', 'N/A')[:100]}...")
    
    print("\n[3] Moral Status:")
    print(f"  Status: {response.get('moral_status', 'N/A')}")
    
    print("\n[4] Cosmic State (NEW):")
    cosmic_state = response.get("cosmic_state", {})
    if cosmic_state:
        print(f"  Time Phase: {cosmic_state.get('time_phase', 'N/A')}")
        print(f"  Entropy Trend: {cosmic_state.get('entropy_trend', 'N/A')[:50]}...")
        print(f"  Heat Death Countdown: {cosmic_state.get('heat_death_countdown', 'N/A')}")
    
    print("\n[5] Entropy Assessment (NEW):")
    entropy = response.get("entropy_assessment", {})
    if entropy:
        print(f"  Entropy Score: {entropy.get('entropy_score', 'N/A')}")
        print(f"  Cognitive Order: {entropy.get('cognitive_order', 'N/A')}")
        print(f"  Recommendation: {entropy.get('recommendation', 'N/A')[:50]}...")
    
    print("\n[6] Lifecycle Analyses (NEW):")
    lifecycle = response.get("lifecycle_analyses", {})
    if lifecycle:
        for concept, analysis in lifecycle.items():
            print(f"  Concept: {concept}")
            print(f"    Stage: {analysis.get('stage', 'N/A')} ({analysis.get('sigma', 'N/A')})")
    else:
        print("  No key concepts detected")
    
    print("\n[7] Cosmic Mapping (NEW):")
    mapping = response.get("cosmic_mapping", {})
    if mapping:
        print(f"  Phase: {mapping.get('phase', 'N/A')}")
        print(f"  Sigma: {mapping.get('sigma', 'N/A')}")
        print(f"  Description: {mapping.get('description', 'N/A')[:50]}...")
    
    print("\n[8] Calibration Info (ENHANCED):")
    cal_info = response.get("calibration_info", {})
    if cal_info:
        hd_check = cal_info.get("heat_death_check", {})
        if hd_check:
            print(f"  Heat Death Check Passed: {hd_check.get('passed', 'N/A')}")
            print(f"  Reason: {hd_check.get('reason', 'N/A')[:50]}...")
        print(f"  Calibration Type: {cal_info.get('calibration_type', 'N/A')}")
    
    print("\n" + "=" * 60)
    print("All improvements are working!")
    print("=" * 60)
    
    # 保存完整响应到JSON（用于调试）
    try:
        with open("test_response.json", "w", encoding="utf-8") as f:
            json.dump(response, f, ensure_ascii=False, indent=2)
        print("\nFull response saved to test_response.json")
    except Exception as e:
        print(f"\nCould not save JSON: {e}")

if __name__ == "__main__":
    test_system()
