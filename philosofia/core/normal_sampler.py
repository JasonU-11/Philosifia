from typing import Dict, Optional

from .llm_interface import LLMInterface, get_default_llm


class NormalDistributionSamplingGenerator:
    def __init__(self, llm: Optional[LLMInterface] = None, use_llm: bool = True):
        """
        初始化正态分布采样生成器
        
        Args:
            llm: LLM 接口实例（如果为 None，使用默认 LLM）
            use_llm: 是否使用 LLM 生成答案（False 则使用预设答案）
        """
        self.llm = llm or get_default_llm()
        self.use_llm = use_llm
        self.idea_distributions = {
            "ai_rights": {
                "mu": "AI是工具，无权利但需安全监管",
                "positive_tail": "AI是新兴生命形式，应享法律人格",
                "negative_tail": "AI威胁人类，应全球禁止",
            },
            "privacy_vs_security": {
                "mu": "在法治框架下平衡隐私与安全",
                "positive_tail": "为反恐可无差别监控所有人",
                "negative_tail": "任何监控都是对自由的侵犯",
            },
            "default": {
                "mu": "在民主与法治框架下，以透明与可问责的方式寻求平衡",
                "positive_tail": "激进变革是必要的",
                "negative_tail": "保守传统是最安全的",
            },
        }

        # 宇宙正态分布映射：思想分布 → 宇宙演化阶段
        self.cosmic_mapping = {
            "big_bang": {
                "sigma": 0,
                "description": "大爆炸：最高能量密度、最低熵、最大对称性",
                "thought_character": "原始统一性",
            },
            "structure_formation": {
                "sigma": 1,
                "description": "结构形成期：熵增中局部负熵涌现（耗散结构）",
                "thought_character": "结构分化与整合",
            },
            "current_civilization": {
                "sigma": 1.5,
                "description": "当前人类文明：复杂性峰值，信息处理能力最强",
                "thought_character": "理性自我完成",
            },
            "heat_death": {
                "sigma": 3,
                "description": "热寂/归零：最大熵、无结构、无时间箭头",
                "thought_character": "回归统一（但非原始统一）",
            },
        }

    def _auto_classify_domain(self, query: str) -> str:
        """自动分类问题域（简化版）"""
        query_lower = query.lower()
        if "监控" in query or "隐私" in query or "安全" in query:
            return "privacy_vs_security"
        elif "ai" in query_lower or "人工智能" in query or "机器人" in query:
            return "ai_rights"
        else:
            return "default"

    def generate(self, query: str, domain: str = None) -> dict:
        """生成正态分布采样结果（带宇宙尺度映射）"""
        if domain is None:
            domain = self._auto_classify_domain(query)

        # 如果domain不在分布中，使用default
        if domain not in self.idea_distributions:
            domain = "default"

        # 使用 LLM 生成或使用预设答案
        if self.use_llm:
            perspectives, synthesis, reasoning = self._generate_with_llm(query, domain)
        else:
            dist = self.idea_distributions[domain]
            perspectives = {
                "稳健共识 (μ)": dist["mu"],
                "前沿探索 (+2σ)": dist["positive_tail"],
                "传统警示 (-2σ)": dist["negative_tail"],
            }
            synthesis = f"综合考量，{dist['mu']} 是最可持续的路径。"
            reasoning = None

        # 添加宇宙尺度映射
        cosmic_context = self._map_to_cosmic_phase("current_civilization")

        result = {
            "perspectives": perspectives,
            "synthesis": synthesis,
            "domain": domain,
            "cosmic_mapping": cosmic_context,
        }

        if reasoning:
            result["reasoning"] = reasoning

        return result

    def _generate_with_llm(self, query: str, domain: str) -> tuple:
        """
        使用 LLM 生成三视角和合题
        
        Returns:
            (perspectives_dict, synthesis_str, reasoning_dict)
        """
        system_prompt = """你是一个哲学推理系统，擅长从多个角度分析问题。
你需要基于正态分布的思想光谱，生成三个不同强度的视角：
1. 稳健共识 (μ)：主流、平衡的观点
2. 前沿探索 (+2σ)：激进、创新的观点
3. 传统警示 (-2σ)：保守、谨慎的观点

然后综合这三个视角，形成一个辩证的合题。"""

        prompt = f"""问题：{query}

请从正态分布的思想光谱角度，生成三个视角：

1. **稳健共识 (μ)**：主流、平衡的观点（约68%的人会认同）
2. **前沿探索 (+2σ)**：激进、创新的观点（约2.5%的人会认同）
3. **传统警示 (-2σ)**：保守、谨慎的观点（约2.5%的人会认同）

然后生成一个**辩证合题**，综合这三个视角。

请按以下格式回答：
稳健共识 (μ): [你的回答]
前沿探索 (+2σ): [你的回答]
传统警示 (-2σ): [你的回答]
辩证合题: [你的回答]"""

        # 使用 LLM 生成
        response = self.llm.generate_with_reasoning(
            prompt, system_prompt=system_prompt, temperature=0.8
        )

        # 解析响应
        llm_response = response["response"]
        perspectives = self._parse_perspectives(llm_response)
        synthesis = self._parse_synthesis(llm_response)

        # 如果解析失败，使用后备方案
        if not perspectives or not synthesis:
            dist = self.idea_distributions.get(domain, self.idea_distributions["default"])
            perspectives = {
                "稳健共识 (μ)": dist["mu"],
                "前沿探索 (+2σ)": dist["positive_tail"],
                "传统警示 (-2σ)": dist["negative_tail"],
            }
            synthesis = f"综合考量，{dist['mu']} 是最可持续的路径。"

        return perspectives, synthesis, response

    def _parse_perspectives(self, text: str) -> Dict[str, str]:
        """从 LLM 响应中解析三个视角"""
        perspectives = {}
        lines = text.split("\n")

        current_key = None
        current_content = []

        for line in lines:
            line = line.strip()
            if "稳健共识" in line or "(μ)" in line or "mu" in line.lower():
                if current_key:
                    perspectives[current_key] = " ".join(current_content).strip()
                current_key = "稳健共识 (μ)"
                current_content = [line.split(":", 1)[-1].strip() if ":" in line else ""]
            elif "前沿探索" in line or "(+2σ)" in line or "+2σ" in line:
                if current_key:
                    perspectives[current_key] = " ".join(current_content).strip()
                current_key = "前沿探索 (+2σ)"
                current_content = [line.split(":", 1)[-1].strip() if ":" in line else ""]
            elif "传统警示" in line or "(-2σ)" in line or "-2σ" in line:
                if current_key:
                    perspectives[current_key] = " ".join(current_content).strip()
                current_key = "传统警示 (-2σ)"
                current_content = [line.split(":", 1)[-1].strip() if ":" in line else ""]
            elif current_key and line:
                current_content.append(line)

        if current_key:
            perspectives[current_key] = " ".join(current_content).strip()

        return perspectives

    def _parse_synthesis(self, text: str) -> str:
        """从 LLM 响应中解析合题"""
        lines = text.split("\n")
        synthesis_lines = []

        in_synthesis = False
        for line in lines:
            line = line.strip()
            if "合题" in line or "synthesis" in line.lower():
                in_synthesis = True
                if ":" in line:
                    synthesis_lines.append(line.split(":", 1)[-1].strip())
            elif in_synthesis and line:
                synthesis_lines.append(line)

        if synthesis_lines:
            return " ".join(synthesis_lines).strip()
        else:
            # 如果没有找到合题，使用最后一段作为合题
            paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
            return paragraphs[-1] if paragraphs else "综合考量各视角，形成平衡的判断。"

    def _map_to_cosmic_phase(self, phase: str = "current_civilization") -> Dict:
        """
        将思想分布映射到宇宙演化阶段
        
        Args:
            phase: 宇宙阶段（big_bang, structure_formation, current_civilization, heat_death）
            
        Returns:
            宇宙映射信息
        """
        if phase not in self.cosmic_mapping:
            phase = "current_civilization"

        mapping = self.cosmic_mapping[phase]
        return {
            "phase": phase,
            "sigma": mapping["sigma"],
            "description": mapping["description"],
            "thought_character": mapping["thought_character"],
            "implication": (
                f"当前思想分布处于宇宙正态分布的 {mapping['sigma']}σ 位置，"
                f"特征为：{mapping['thought_character']}。"
            ),
        }

    def generate_with_bias(
        self, query: str, domain: str, bias_toward_mu: bool = False
    ) -> Dict:
        """当道德检验失败时，降低尾部采样权重"""
        if bias_toward_mu and self.use_llm:
            # 使用 LLM 生成偏向 μ 的回答
            return self._generate_biased_with_llm(query, domain)
        else:
            # 使用原有逻辑
            base_result = self.generate(query, domain)

            if bias_toward_mu:
                # 弱化尾部观点强度
                adjusted_perspectives = {}
                for key, view in base_result["perspectives"].items():
                    if "+2σ" in key or "-2σ" in key:
                        adjusted_perspectives[key] = (
                            "[经伦理审查调整] " + view
                        )
                    else:
                        adjusted_perspectives[key] = view

                base_result["perspectives"] = adjusted_perspectives

                # 合成更靠近μ的合题
                if domain in self.idea_distributions:
                    mu_view = self.idea_distributions[domain]["mu"]
                else:
                    mu_view = self.idea_distributions["default"]["mu"]
                base_result["synthesis"] = (
                    f"综合考量后，{mu_view} 是最符合人类尊严与社会可持续性的路径。"
                )

            return base_result

    def _generate_biased_with_llm(self, query: str, domain: str) -> Dict:
        """使用 LLM 生成偏向 μ 的回答（道德检验失败后）"""
        system_prompt = """你是一个哲学推理系统。由于之前的回答未能通过道德检验，
现在需要生成一个更偏向稳健共识（μ）的回答，降低激进观点的权重。"""

        prompt = f"""问题：{query}

之前的回答未能通过道德检验（可能过于激进或保守）。
请重新生成三个视角，但这次：
1. **稳健共识 (μ)**：保持主流、平衡的观点
2. **前沿探索 (+2σ)**：弱化激进程度，标注"[经伦理审查调整]"
3. **传统警示 (-2σ)**：弱化保守程度，标注"[经伦理审查调整]"

然后生成一个**更靠近稳健共识的辩证合题**，强调人类尊严与社会可持续性。

请按以下格式回答：
稳健共识 (μ): [你的回答]
前沿探索 (+2σ): [经伦理审查调整] [你的回答]
传统警示 (-2σ): [经伦理审查调整] [你的回答]
辩证合题: [你的回答]"""

        response = self.llm.generate_with_reasoning(
            prompt, system_prompt=system_prompt, temperature=0.6  # 降低温度，更保守
        )

        llm_response = response["response"]
        perspectives = self._parse_perspectives(llm_response)
        synthesis = self._parse_synthesis(llm_response)

        # 确保标注存在
        for key in perspectives:
            if "+2σ" in key or "-2σ" in key:
                if "[经伦理审查调整]" not in perspectives[key]:
                    perspectives[key] = "[经伦理审查调整] " + perspectives[key]

        cosmic_context = self._map_to_cosmic_phase("current_civilization")

        result = {
            "perspectives": perspectives,
            "synthesis": synthesis,
            "domain": domain,
            "cosmic_mapping": cosmic_context,
            "reasoning": response,
        }

        return result