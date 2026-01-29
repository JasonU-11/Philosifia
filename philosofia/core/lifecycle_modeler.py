from typing import Dict, Optional


class LifecycleModeler:
    """
    生灭周期建模：识别概念、制度、技术的生命周期阶段
    基于宇宙正态分布模型：过热期（+2σ）、稳态期（±1σ）、衰亡期（尾部）
    """

    def __init__(self):
        # 概念生命周期数据库（可扩展）
        self.lifecycle_db = {
            # 过热期（+2σ）：即将均值回归
            "overheated": [
                "区块链",
                "元宇宙",
                "nft",
                "web3",
                "chatgpt",
                "大语言模型",
                "生成式ai",
            ],
            # 稳态期（±1σ）：具抗熵韧性
            "stable": [
                "民主",
                "科学方法",
                "法治",
                "市场经济",
                "人权",
                "democracy",
                "scientific method",
                "rule of law",
            ],
            # 衰亡期（尾部）：仅作历史参照
            "declining": [
                "地心说",
                "炼金术",
                "封建制度",
                "geocentric",
                "alchemy",
                "feudalism",
            ],
        }

    def assess_lifecycle(self, concept: str) -> Dict[str, str]:
        """
        评估概念的生命周期阶段
        
        Args:
            concept: 要评估的概念名称
            
        Returns:
            {
                "stage": "overheated" | "stable" | "declining" | "unknown",
                "sigma": 对应的σ值,
                "description": 阶段描述,
                "strategy": 输出策略建议
            }
        """
        concept_lower = concept.lower()

        # 检查过热期
        for term in self.lifecycle_db["overheated"]:
            if term.lower() in concept_lower or concept_lower in term.lower():
                return {
                    "stage": "overheated",
                    "sigma": "+2σ",
                    "description": "过热期（+2σ），即将均值回归",
                    "strategy": "强调可能性与风险，避免过度乐观",
                }

        # 检查稳态期
        for term in self.lifecycle_db["stable"]:
            if term.lower() in concept_lower or concept_lower in term.lower():
                return {
                    "stage": "stable",
                    "sigma": "±1σ",
                    "description": "稳态期（±1σ），具抗熵韧性",
                    "strategy": "强调规范性与责任，突出其历史稳定性",
                }

        # 检查衰亡期
        for term in self.lifecycle_db["declining"]:
            if term.lower() in concept_lower or concept_lower in term.lower():
                return {
                    "stage": "declining",
                    "sigma": "尾部",
                    "description": "衰亡期（尾部），仅作历史参照",
                    "strategy": "强调历史教训与扬弃，避免重复错误",
                }

        # 未知概念：基于启发式判断
        return self._heuristic_assessment(concept)

    def _heuristic_assessment(self, concept: str) -> Dict[str, str]:
        """
        启发式评估：基于概念特征推断生命周期
        """
        concept_lower = concept.lower()

        # 如果包含"新"、"革命"等词，可能是过热期
        if any(
            keyword in concept_lower
            for keyword in ["新", "革命", "突破", "颠覆", "new", "revolution", "breakthrough"]
        ):
            return {
                "stage": "overheated",
                "sigma": "+2σ",
                "description": "可能处于过热期（+2σ），需谨慎评估",
                "strategy": "强调可能性与风险，避免过度乐观",
            }

        # 如果包含"传统"、"古典"等词，可能是稳态期
        if any(
            keyword in concept_lower
            for keyword in [
                "传统",
                "古典",
                "经典",
                "tradition",
                "classical",
                "classic",
            ]
        ):
            return {
                "stage": "stable",
                "sigma": "±1σ",
                "description": "可能处于稳态期（±1σ），具有历史稳定性",
                "strategy": "强调规范性与责任，突出其历史稳定性",
            }

        # 默认：未知阶段
        return {
            "stage": "unknown",
            "sigma": "未知",
            "description": "生命周期阶段未知，需进一步分析",
            "strategy": "保持开放态度，综合多视角评估",
        }

    def get_output_strategy(self, lifecycle_info: Dict[str, str]) -> str:
        """
        根据生命周期信息生成输出策略建议
        """
        stage = lifecycle_info.get("stage", "unknown")

        strategies = {
            "overheated": (
                "对新生事物：强调可能性与风险；"
                "提醒均值回归的可能性；"
                "建议保持理性与批判性思维。"
            ),
            "stable": (
                "对成熟事物：强调规范性与责任；"
                "突出其历史稳定性与抗熵韧性；"
                "建议在稳定中寻求改进。"
            ),
            "declining": (
                "对衰亡事物：强调历史教训与扬弃；"
                "避免重复错误；"
                "从历史中汲取智慧。"
            ),
            "unknown": (
                "保持开放态度；"
                "综合多视角评估；"
                "基于证据和理性判断。"
            ),
        }

        return strategies.get(stage, strategies["unknown"])
