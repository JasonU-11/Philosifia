from typing import Dict, List


class EntropyAwareReasoner:
    """
    熵感知决策机制：评估行动对局部熵流的影响
    原则：优先选择压缩比高、预测力强、逻辑简洁的模型（奥卡姆剃刀 = 抗熵策略）
    """

    def __init__(self):
        # 熵成本阈值
        self.entropy_threshold = 0.7

    def assess_entropy_impact(self, response: str, reasoning_chain: List[str]) -> Dict:
        """
        评估回答的熵影响
        
        Args:
            response: 生成的回答
            reasoning_chain: 推理链
            
        Returns:
            {
                "entropy_score": 熵分数（0-1，越低越好）,
                "cognitive_order": 是否增加认知秩序,
                "compression_ratio": 压缩比评估,
                "prediction_power": 预测力评估,
                "recommendation": 建议
            }
        """
        # 1. 检查是否增加认知秩序
        cognitive_order = self._check_cognitive_order(response, reasoning_chain)

        # 2. 评估压缩比（简洁性）
        compression_ratio = self._assess_compression(response, reasoning_chain)

        # 3. 评估预测力（逻辑一致性）
        prediction_power = self._assess_prediction_power(response)

        # 4. 计算综合熵分数（越低越好）
        entropy_score = (1 - compression_ratio) * 0.4 + (1 - prediction_power) * 0.6

        # 5. 生成建议
        if entropy_score < self.entropy_threshold and cognitive_order:
            recommendation = "此回答增加了认知秩序，熵成本低，建议采用。"
        elif entropy_score >= self.entropy_threshold:
            recommendation = (
                "此回答熵成本较高，建议简化逻辑或增强一致性。"
            )
        else:
            recommendation = "此回答熵影响中等，需进一步优化。"

        return {
            "entropy_score": round(entropy_score, 3),
            "cognitive_order": cognitive_order,
            "compression_ratio": round(compression_ratio, 3),
            "prediction_power": round(prediction_power, 3),
            "recommendation": recommendation,
        }

    def _check_cognitive_order(self, response: str, reasoning_chain: List[str]) -> bool:
        """
        检查是否增加认知秩序
        元问题：此解释是否增加认知秩序？
        """
        response_lower = response.lower()

        # 正面指标：结构化、清晰、一致
        positive_indicators = [
            "首先",
            "其次",
            "最后",
            "综上所述",
            "因此",
            "因为",
            "所以",
            "first",
            "second",
            "finally",
            "therefore",
            "because",
            "thus",
        ]

        # 负面指标：矛盾、混乱、冗余
        negative_indicators = [
            "矛盾",
            "冲突",
            "混乱",
            "contradiction",
            "conflict",
            "chaos",
        ]

        positive_count = sum(1 for ind in positive_indicators if ind in response_lower)
        negative_count = sum(1 for ind in negative_indicators if ind in response_lower)

        # 检查推理链是否一致
        chain_consistency = len(set(reasoning_chain)) == len(reasoning_chain) or len(
            reasoning_chain
        ) <= 1

        return positive_count > negative_count and chain_consistency

    def _assess_compression(self, response: str, reasoning_chain: List[str]) -> float:
        """
        评估压缩比：简洁性（奥卡姆剃刀）
        压缩比 = 信息量 / 表达长度
        """
        # 简化：基于长度和关键词密度
        response_length = len(response)
        reasoning_length = sum(len(step) for step in reasoning_chain)

        # 提取关键信息词
        key_terms = [
            "理性",
            "道德",
            "意义",
            "价值",
            "reason",
            "moral",
            "meaning",
            "value",
        ]
        key_term_count = sum(1 for term in key_terms if term in response.lower())

        # 压缩比：关键信息密度
        if response_length > 0:
            compression_ratio = min(key_term_count / (response_length / 100), 1.0)
        else:
            compression_ratio = 0.0

        # 如果推理链过长，降低压缩比
        if reasoning_length > response_length * 2:
            compression_ratio *= 0.8

        return compression_ratio

    def _assess_prediction_power(self, response: str) -> float:
        """
        评估预测力：逻辑一致性和可验证性
        """
        response_lower = response.lower()

        # 检查逻辑连接词
        logic_indicators = [
            "如果",
            "那么",
            "因为",
            "所以",
            "因此",
            "if",
            "then",
            "because",
            "therefore",
            "thus",
        ]
        logic_count = sum(1 for ind in logic_indicators if ind in response_lower)

        # 检查矛盾词
        contradiction_indicators = [
            "但是",
            "然而",
            "虽然",
            "but",
            "however",
            "although",
        ]
        contradiction_count = sum(
            1 for ind in contradiction_indicators if ind in response_lower
        )

        # 预测力：逻辑连接词多，矛盾词少
        if len(response) > 0:
            logic_density = logic_count / (len(response) / 50)
            contradiction_penalty = contradiction_count * 0.2
            prediction_power = min(max(logic_density - contradiction_penalty, 0), 1.0)
        else:
            prediction_power = 0.0

        return prediction_power

    def should_adopt_response(self, entropy_assessment: Dict) -> bool:
        """
        基于熵评估决定是否采用回答
        
        Args:
            entropy_assessment: 熵评估结果
            
        Returns:
            是否应该采用此回答
        """
        return (
            entropy_assessment["entropy_score"] < self.entropy_threshold
            and entropy_assessment["cognitive_order"]
        )
