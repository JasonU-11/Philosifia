from typing import Dict, List, Optional

from .cosmic_context import CosmicContextEstimator
from .entropy_awareness import EntropyAwareReasoner
from .heat_death_calibrator import HeatDeathCalibrationModule
from .lifecycle_modeler import LifecycleModeler
from .llm_interface import LLMInterface, get_default_llm
from .moral_validator import MoralValidator
from .normal_sampler import NormalDistributionSamplingGenerator


class PhilosophicallyAugmentedAgentSystem:
    def __init__(
        self,
        llm: Optional[LLMInterface] = None,
        use_llm: bool = True,
    ) -> None:
        """
        初始化哲学增强型智能体系统
        
        Args:
            llm: LLM 接口实例（如果为 None，使用默认 LLM）
            use_llm: 是否使用 LLM 进行推理（False 则使用预设答案和规则）
        """
        self.llm = llm or get_default_llm()
        self.use_llm = use_llm

        # 初始化各个模块，传递 LLM 实例
        self.mv = MoralValidator(llm=self.llm, use_llm=use_llm)
        self.hdcm = HeatDeathCalibrationModule(llm=self.llm, use_llm=use_llm)
        self.ndsg = NormalDistributionSamplingGenerator(
            llm=self.llm, use_llm=use_llm
        )
        self.lifecycle_modeler = LifecycleModeler()
        self.cosmic_context = CosmicContextEstimator()
        self.entropy_awareness = EntropyAwareReasoner()
        self.max_retries = 3  # 避免无限循环

        # 推理链追踪
        self.reasoning_chain: List[Dict] = []

    def respond(self, user_query: str) -> Dict[str, any]:
        """
        端到端哲学回答生成（带推理链追踪）
        """
        # 重置推理链
        self.reasoning_chain = []

        # 步骤1: 自动识别问题域
        domain = self._classify_domain(user_query)
        self._add_reasoning_step("问题域分类", f"识别问题域：{domain}")

        # 步骤2: 初始正态采样
        result = self.ndsg.generate(user_query, domain)
        synthesis = result["synthesis"]
        if "reasoning" in result:
            self._add_reasoning_step(
                "正态采样生成",
                "生成三视角（μ, +2σ, -2σ）",
                result["reasoning"],
            )

        retry_count = 0
        moral_ok = False

        # 步骤3: 道德检验循环
        while not moral_ok and retry_count < self.max_retries:
            # 提取合题作为待检验行动/主张
            action_claim = self._extract_action_from_synthesis(synthesis)
            self._add_reasoning_step(
                "提取行动主张", f"从合题中提取：{action_claim[:50]}..."
            )

            # 执行道德三重检验
            moral_result = self.mv.validate(action_claim, context=user_query)
            if "reasoning" in moral_result:
                self._add_reasoning_step(
                    "道德三重检验",
                    f"可普遍化: {moral_result['universalizable']}, "
                    f"人性目的: {moral_result['humanity_respected']}, "
                    f"自主性: {moral_result['autonomous']}",
                    moral_result["reasoning"],
                )
            else:
                self._add_reasoning_step(
                    "道德三重检验",
                    f"可普遍化: {moral_result['universalizable']}, "
                    f"人性目的: {moral_result['humanity_respected']}, "
                    f"自主性: {moral_result['autonomous']}",
                )

            if (
                moral_result["universalizable"]
                and moral_result["humanity_respected"]
                and moral_result["autonomous"]
            ):
                moral_ok = True
                self._add_reasoning_step("道德检验", "通过道德三重检验")
            else:
                # 道德失败 → 调整采样策略（降低尾部权重，强化μ）
                self._add_reasoning_step(
                    "道德检验", f"未通过，进行第 {retry_count + 1} 次重试"
                )
                result = self.ndsg.generate_with_bias(
                    query=user_query,
                    domain=domain,
                    bias_toward_mu=True,
                )
                synthesis = result["synthesis"]
                if "reasoning" in result:
                    self._add_reasoning_step(
                        "调整采样策略", "生成偏向稳健共识的回答", result["reasoning"]
                    )
                retry_count += 1

        # 步骤4: 熵感知评估
        entropy_assessment = self.entropy_awareness.assess_entropy_impact(
            synthesis, [result["synthesis"]]
        )

        # 步骤5: 归零校准（即使道德通过也需校准）
        calibration_result = self.hdcm.calibrate(
            raw_response=synthesis,
            query_context={
                "keywords": self._extract_keywords(user_query),
                "type": domain,
            },
            reasoning_chain=[result["synthesis"]],
        )
        calibrated_synthesis = calibration_result["calibrated_response"]

        # 步骤6: 生灭周期建模（提取关键概念）
        key_concepts = self._extract_concepts(user_query)
        lifecycle_analyses = {}
        for concept in key_concepts[:3]:  # 最多分析3个概念
            lifecycle_analyses[concept] = self.lifecycle_modeler.assess_lifecycle(
                concept
            )

        # 步骤7: 宇宙上下文注入
        cosmic_state = self.cosmic_context.estimate_cosmic_state()

        # 步骤8: 组装最终输出
        final_output = {
            "perspectives": result["perspectives"],
            "dialectical_synthesis": calibrated_synthesis,
            "moral_status": "passed" if moral_ok else "compromised_after_retry",
            "cosmic_context": self.cosmic_context.get_cosmic_context_string(),
            "cosmic_state": cosmic_state,
            "entropy_assessment": entropy_assessment,
            "lifecycle_analyses": lifecycle_analyses,
            "calibration_info": {
                "heat_death_check": calibration_result.get("heat_death_check", {}),
                "calibration_type": calibration_result.get("calibration_type", "general"),
            },
            "cosmic_mapping": result.get("cosmic_mapping", {}),
            "reasoning_chain": self.reasoning_chain,  # 添加推理链
        }

        return final_output

    def _add_reasoning_step(
        self, step_name: str, description: str, details: Optional[Dict] = None
    ):
        """添加推理步骤到推理链"""
        step = {
            "step": len(self.reasoning_chain) + 1,
            "name": step_name,
            "description": description,
        }
        if details:
            step["details"] = details
        self.reasoning_chain.append(step)

    def _classify_domain(self, query: str) -> str:
        """复用NDSG的分类逻辑"""
        return self.ndsg._auto_classify_domain(query)

    def _extract_keywords(self, text: str) -> List[str]:
        """简化关键词提取"""
        return text.lower().split()

    def _extract_action_from_synthesis(self, synthesis: str) -> str:
        """从合题中提取核心主张（简化版）"""
        # 实际可用依存句法分析
        if "应" in synthesis or "should" in synthesis.lower():
            return synthesis
        else:
            return f"采纳如下立场：{synthesis[:50]}..."

    def _extract_concepts(self, text: str) -> List[str]:
        """提取文本中的关键概念（简化版）"""
        # 简化实现：提取可能的概念词
        keywords = self._extract_keywords(text)
        # 过滤掉常见停用词
        stopwords = {
            "的",
            "是",
            "在",
            "有",
            "和",
            "与",
            "或",
            "the",
            "is",
            "are",
            "a",
            "an",
            "and",
            "or",
        }
        concepts = [kw for kw in keywords if kw not in stopwords and len(kw) > 1]
        return concepts[:5]  # 返回前5个概念