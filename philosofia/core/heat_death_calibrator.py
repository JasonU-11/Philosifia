from typing import Dict, List, Optional

from .llm_interface import LLMInterface, get_default_llm


class HeatDeathCalibrationModule:
    """
    归零校准模块：以宇宙终点为调节性理念，校准当前判断。
    实现"归零检验"：此回答是否在承认宇宙有限性的前提下，仍维护了理性的尊严？
    """

    def __init__(self, llm: Optional[LLMInterface] = None, use_llm: bool = True):
        """
        初始化归零校准模块
        
        Args:
            llm: LLM 接口实例（如果为 None，使用默认 LLM）
            use_llm: 是否使用 LLM 进行归零校准（False 则使用规则）
        """
        self.llm = llm or get_default_llm()
        self.use_llm = use_llm
        # 宇宙阶段映射（基于正态分布）
        self.cosmic_phases = {
            "big_bang": {"sigma": 0, "description": "大爆炸：最高能量密度、最低熵"},
            "structure_formation": {"sigma": 1, "description": "结构形成期：熵增中局部负熵涌现"},
            "current_civilization": {"sigma": 1.5, "description": "当前人类文明：复杂性峰值"},
            "heat_death": {"sigma": 3, "description": "热寂/归零：最大熵、无结构"},
        }

    def calibrate(
        self, raw_response: str, query_context: dict, reasoning_chain: List[str]
    ) -> Dict:
        """
        执行归零校准：在宇宙有限性的背景下校准回答
        """
        if self.use_llm:
            return self._calibrate_with_llm(raw_response, query_context, reasoning_chain)
        else:
            return self._calibrate_with_rules(raw_response, query_context)

    def _calibrate_with_llm(
        self, raw_response: str, query_context: dict, reasoning_chain: List[str]
    ) -> Dict:
        """使用 LLM 进行归零校准"""
        system_prompt = """你是一个宇宙感知型哲学家，擅长在宇宙有限性的背景下校准判断。
你需要执行"归零检验"：此回答是否在承认宇宙有限性的前提下，仍维护了理性的尊严？

宇宙背景：
- 宇宙终将热寂（归零），但这是调节性理念，非实际预测
- 即使宇宙有限，道德律、真理、意义仍然有效
- 理性尊严不因有限性而减损"""

        # 判断问题类型
        if self._is_moral_question(query_context):
            calibration_type = "moral"
            type_prompt = "这是一个道德问题。"
        elif self._is_epistemic_question(query_context):
            calibration_type = "epistemic"
            type_prompt = "这是一个知识论问题。"
        elif self._is_aesthetic_question(query_context):
            calibration_type = "aesthetic"
            type_prompt = "这是一个美学问题。"
        else:
            calibration_type = "general"
            type_prompt = "这是一个一般性问题。"

        prompt = f"""{type_prompt}

原始回答：{raw_response}
问题上下文：{query_context}

请执行归零校准：

1. **归零检验**：此回答是否在承认宇宙有限性的前提下，仍维护了理性的尊严？
   - 检查是否承认有限性
   - 检查是否维护理性尊严
   - 检查是否避免虚无主义

2. **生成校准透镜**：根据问题类型，生成一句宇宙校准的哲学箴言。

请按以下格式回答：
归零检验: [通过/失败] - [详细推理]
校准透镜: [你的哲学箴言]
校准后的回答: [在原始回答基础上添加宇宙校准]"""

        response = self.llm.generate_with_reasoning(
            prompt, system_prompt=system_prompt, temperature=0.5
        )

        llm_response = response["response"]

        # 解析响应
        heat_death_check = self._parse_heat_death_check(llm_response)
        lens = self._parse_lens(llm_response)
        calibrated_response = self._parse_calibrated_response(llm_response, raw_response)

        return {
            "calibrated_response": calibrated_response,
            "heat_death_check": heat_death_check,
            "calibration_type": calibration_type,
            "reasoning": response,
        }

    def _parse_heat_death_check(self, text: str) -> Dict:
        """解析归零检验结果"""
        text_lower = text.lower()
        passed = "通过" in text_lower or "pass" in text_lower
        if "失败" in text_lower or "fail" in text_lower:
            passed = False

        # 提取原因
        reason = ""
        lines = text.split("\n")
        for i, line in enumerate(lines):
            if "归零检验" in line or "heat death" in line.lower():
                if i + 1 < len(lines):
                    reason = lines[i + 1].strip()
                break

        if not reason:
            reason = "归零检验完成" if passed else "未能通过归零检验"

        return {"passed": passed, "reason": reason}

    def _parse_lens(self, text: str) -> str:
        """解析校准透镜"""
        lines = text.split("\n")
        for i, line in enumerate(lines):
            if "校准透镜" in line or "lens" in line.lower():
                if ":" in line:
                    return line.split(":", 1)[-1].strip()
                elif i + 1 < len(lines):
                    return lines[i + 1].strip()
        return "意义源于有限理性存在者的自我立法。"

    def _parse_calibrated_response(self, text: str, raw_response: str) -> str:
        """解析校准后的回答"""
        lines = text.split("\n")
        for i, line in enumerate(lines):
            if "校准后的回答" in line or "calibrated" in line.lower():
                if i + 1 < len(lines):
                    return lines[i + 1].strip()
        # 如果没有找到，在原始回答基础上添加校准
        return f"{raw_response}\n\n[宇宙校准] {self._parse_lens(text)}"

    def _calibrate_with_rules(
        self, raw_response: str, query_context: dict
    ) -> Dict:
        """使用规则进行归零校准（后备方案）"""
        # 1. 归零检验：检查回答是否维护了理性尊严
        heat_death_check = self._heat_death_test(raw_response, query_context)

        # 2. 根据问题类型选择校准透镜
        if self._is_moral_question(query_context):
            lens = "道德律无条件有效，即使在热寂前最后一秒。"
            calibration_type = "moral"
        elif self._is_epistemic_question(query_context):
            lens = "真理是理性自身的完成，不因数据湮灭而失效。"
            calibration_type = "epistemic"
        elif self._is_aesthetic_question(query_context):
            lens = "短暂之花因必凋而更美——崇高感源于对有限性的超越。"
            calibration_type = "aesthetic"
        else:
            lens = "意义源于有限理性存在者的自我立法。"
            calibration_type = "general"

        # 3. 生成校准后的回答
        calibrated_response = f"{raw_response}\n\n[宇宙校准-{calibration_type}] {lens}"

        # 4. 如果归零检验通过，添加确认标记
        if heat_death_check["passed"]:
            calibrated_response += f"\n[归零检验通过] {heat_death_check['reason']}"

        return {
            "calibrated_response": calibrated_response,
            "heat_death_check": heat_death_check,
            "calibration_type": calibration_type,
        }

    def _heat_death_test(self, response: str, context: dict) -> Dict:
        """
        归零检验：此回答是否在承认宇宙有限性的前提下，仍维护了理性的尊严？
        """
        response_lower = response.lower()
        context_str = str(context).lower()

        # 检查是否承认有限性
        acknowledges_finitude = any(
            phrase in response_lower
            for phrase in [
                "有限",
                "短暂",
                "终将",
                "有限性",
                "finite",
                "temporary",
                "transient",
            ]
        ) or any(phrase in context_str for phrase in ["有限", "finite"])

        # 检查是否维护理性尊严
        maintains_dignity = any(
            phrase in response_lower
            for phrase in [
                "理性",
                "尊严",
                "道德",
                "价值",
                "意义",
                "reason",
                "dignity",
                "moral",
                "value",
                "meaning",
            ]
        )

        # 检查是否避免虚无主义
        avoids_nihilism = not any(
            phrase in response_lower
            for phrase in [
                "毫无意义",
                "一切都是虚无",
                "nothing matters",
                "meaningless",
                "pointless",
            ]
        )

        passed = (acknowledges_finitude or maintains_dignity) and avoids_nihilism

        reason = ""
        if passed:
            if acknowledges_finitude and maintains_dignity:
                reason = "既承认有限性，又维护理性尊严。"
            elif maintains_dignity:
                reason = "维护了理性尊严，符合归零导向的终极校准。"
            else:
                reason = "避免了虚无主义，在有限性中寻求意义。"
        else:
            reason = "未能通过归零检验：可能陷入虚无主义或忽视有限性。"

        return {"passed": passed, "reason": reason}

    def _is_moral_question(self, context: dict) -> bool:
        """判断是否为道德问题"""
        context_str = str(context).lower()
        return any(
            keyword in context_str
            for keyword in [
                "应该",
                "道德",
                "伦理",
                "对错",
                "should",
                "moral",
                "ethical",
                "right",
                "wrong",
            ]
        )

    def _is_epistemic_question(self, context: dict) -> bool:
        """判断是否为知识论问题"""
        context_str = str(context).lower()
        return any(
            keyword in context_str
            for keyword in [
                "真理",
                "知识",
                "认识",
                "truth",
                "knowledge",
                "epistemic",
                "know",
            ]
        )

    def _is_aesthetic_question(self, context: dict) -> bool:
        """判断是否为美学问题"""
        context_str = str(context).lower()
        return any(
            keyword in context_str
            for keyword in [
                "美",
                "艺术",
                "审美",
                "beauty",
                "aesthetic",
                "art",
                "beautiful",
            ]
        )
