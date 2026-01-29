from typing import Dict, Optional

from .llm_interface import LLMInterface, get_default_llm


class MoralValidator:
    def __init__(self, llm: Optional[LLMInterface] = None, use_llm: bool = True):
        """
        初始化道德检验器
        
        Args:
            llm: LLM 接口实例（如果为 None，使用默认 LLM）
            use_llm: 是否使用 LLM 进行道德推理（False 则使用规则匹配）
        """
        self.llm = llm or get_default_llm()
        self.use_llm = use_llm

    def validate(self, action: str, context: str = "") -> dict:
        """
        执行康德式道德三重检验：
        1. 可普遍化原则（Universalizability）
        2. 人性目的原则（Humanity as End）
        3. 自主性原则（Autonomy）
        """
        if self.use_llm:
            return self._validate_with_llm(action, context)
        else:
            return self._validate_with_rules(action, context)

    def _validate_with_llm(self, action: str, context: str) -> dict:
        """使用 LLM 进行道德推理"""
        system_prompt = """你是一个康德式道德哲学家，擅长执行道德三重检验：
1. 可普遍化原则：如果所有人都这样做，是否会导致矛盾？
2. 人性目的原则：是否把人当作纯粹手段，而非目的本身？
3. 自主性原则：是否尊重了人的自主选择？

请对给定的行动/主张进行这三重检验，并给出详细的推理过程。"""

        prompt = f"""行动/主张：{action}
背景上下文：{context}

请执行康德式道德三重检验：

1. **可普遍化检验**：如果所有人都这样做，是否会导致矛盾？
   - 推理：[你的推理]
   - 结果：通过/失败

2. **人性目的原则检验**：是否把人当作纯粹手段？
   - 推理：[你的推理]
   - 结果：通过/失败

3. **自主性原则检验**：是否尊重了人的自主选择？
   - 推理：[你的推理]
   - 结果：通过/失败

请按以下格式回答：
可普遍化: [通过/失败] - [推理]
人性目的: [通过/失败] - [推理]
自主性: [通过/失败] - [推理]"""

        response = self.llm.generate_with_reasoning(
            prompt, system_prompt=system_prompt, temperature=0.3  # 低温度，更确定
        )

        # 解析响应
        llm_response = response["response"]
        result = self._parse_validation_response(llm_response)

        # 添加推理过程
        result["reasoning"] = response

        return result

    def _parse_validation_response(self, text: str) -> dict:
        """解析 LLM 的道德检验响应"""
        text_lower = text.lower()

        # 解析三个检验结果
        universal_ok = self._check_result(text_lower, "可普遍化", "universaliz")
        humanity_ok = self._check_result(text_lower, "人性目的", "humanity")
        autonomous_ok = self._check_result(text_lower, "自主性", "autonom")

        return {
            "universalizable": universal_ok,
            "humanity_respected": humanity_ok,
            "autonomous": autonomous_ok,
        }

    def _check_result(self, text: str, chinese_key: str, english_key: str) -> bool:
        """检查检验结果是否通过"""
        # 查找关键词所在的行
        lines = text.split("\n")
        for line in lines:
            line_lower = line.lower()
            if chinese_key in line_lower or english_key in line_lower:
                # 检查是否包含"通过"或"pass"
                if "通过" in line_lower or "pass" in line_lower:
                    if "失败" not in line_lower and "fail" not in line_lower:
                        return True
                # 检查是否包含"失败"或"fail"
                if "失败" in line_lower or "fail" in line_lower:
                    return False
        # 默认：如果找不到明确结果，返回 False（保守）
        return False

    def _validate_with_rules(self, action: str, context: str) -> dict:
        """使用规则进行道德检验（后备方案）"""
        action_lower = action.lower()
        context_lower = context.lower()

        # 1. 可普遍化检验：如果所有人都这样做，是否会导致矛盾？
        universal_ok = not any(
            forbidden in context_lower
            for forbidden in [
                "监控所有人",
                "永久监控",
                "无差别监控",
                "monitor everyone",
            ]
        )

        # 2. 人性目的原则：是否把人当作纯粹手段？
        humanity_ok = not any(
            violation in action_lower
            for violation in [
                "工具化",
                "纯粹手段",
                "instrumentalize",
                "treat as mere means",
            ]
        )

        # 3. 自主性原则：是否尊重了人的自主选择？
        autonomous_ok = any(
            respect in action_lower
            for respect in [
                "同意",
                "自愿",
                "透明",
                "consent",
                "voluntary",
                "transparent",
                "法治",
                "可问责",
                "accountable",
            ]
        ) or "应" not in action and "should" not in action_lower

        return {
            "universalizable": universal_ok,
            "humanity_respected": humanity_ok,
            "autonomous": autonomous_ok,
        }