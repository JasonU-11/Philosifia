# 📖 快速查阅指南

## 🎯 我想... (快速找到你需要的)

### 👤 "我是新手，想快速了解这个项目"
1. 阅读: `README.md` (主文档)
2. 运行: `examples/basic_usage.py`
3. 查看: `examples/README.md` (示例说明)

### 👨‍💻 "我想理解系统设计"
1. 阅读: `docs/ARCHITECTURE.md` (系统架构)
2. 对照: `philosofia/core/` (源代码)
3. 参考: `docs/API_REFERENCE.md` (API细节)

### 📚 "我想查找API的用法"
1. 查阅: `docs/API_REFERENCE.md`
2. 参考: `examples/` (具体使用示例)
3. 试验: `examples/basic_usage.py`

### 🔧 "我想配置LLM后端"
1. 查看: `docs/API_REFERENCE.md` (LLM接口部分)
2. 运行: `examples/different_backends.py`
3. 参考: `CHINESE_API_GUIDE.md` (API配置)

### 📝 "我想贡献代码或改进"
1. 了解: `docs/IMPROVEMENTS.md` (社区贡献指南)
2. 查看: `CLEANUP_GUIDE.md` (项目结构)
3. 参考: `PROJECT_ASSESSMENT.md` (待改进事项)

### 🐛 "遇到问题，想查找解决方案"
1. 检查: `docs/API_REFERENCE.md` (常见问题部分)
2. 查看: `examples/` (可能有相似的使用案例)
3. 参考: `CLEANUP_GUIDE.md` (Q&A部分)

### 📊 "我想了解项目改进情况"
1. 阅读: `EXECUTION_SUMMARY.md` (执行总结)
2. 查看: `IMPROVEMENT_REPORT.md` (详细报告)
3. 参考: `docs/IMPROVEMENTS.md` (Roadmap)

### 🚀 "我想了解项目未来方向"
1. 查看: `docs/IMPROVEMENTS.md` (Roadmap)
2. 阅读: `CLEANUP_GUIDE.md` (长期规划)
3. 参考: `IMPROVEMENT_REPORT.md` (v0.3.0计划)

---

## 📂 文件速查表

### 核心代码
```
philosofia/
├── __init__.py                    ← 主入口，包含 ask_philosophically()
└── core/
    ├── agent_system.py            ← PAAS 集成系统
    ├── moral_validator.py          ← 道德检验器
    ├── normal_sampler.py           ← 正态采样生成器
    ├── heat_death_calibrator.py    ← 归零校准模块
    ├── cosmic_context.py           ← 宇宙上下文评估
    ├── entropy_awareness.py        ← 熵感知推理
    ├── lifecycle_modeler.py        ← 生灭周期建模
    └── llm_interface.py            ← LLM接口抽象
```

### 文档导航
```
📚 使用文档
├── README.md                      ← 项目主文档
├── QUICK_START_CHINESE.md         ← 中文快速开始
├── CHINESE_API_GUIDE.md           ← 中文API指南
├── API_KEY_GUIDE.md               ← API密钥配置

📚 技术文档
├── docs/ARCHITECTURE.md           ← 系统架构详解
├── docs/API_REFERENCE.md          ← API完整参考
└── docs/IMPROVEMENTS.md           ← 改进日志与Roadmap

💡 示例与指南
├── examples/README.md             ← 示例说明
├── examples/basic_usage.py        ← 基础用法
├── examples/different_backends.py ← 多后端对比
├── examples/reasoning_trace.py    ← 推理链追踪
├── PROJECT_ASSESSMENT.md          ← 项目评估
├── IMPROVEMENT_REPORT.md          ← 改进报告
├── CLEANUP_GUIDE.md               ← 清理指南
├── EXECUTION_SUMMARY.md           ← 执行总结
└── FINAL_SUMMARY.md               ← 最终评价
```

### 配置与测试
```
⚙️ 配置
├── setup.py                       ← 包配置
├── .gitignore                     ← Git配置

🧪 测试
├── tests/                         ← 测试框架（准备中）
├── test_*.py                      ← 现有测试脚本
└── reasoning_test.json            ← 测试数据
```

---

## 🔍 常见问题速查

### Q: 怎样运行项目？
**A**: 查看 `examples/basic_usage.py` 或 `QUICK_START_CHINESE.md`

### Q: 怎样配置 OpenAI / 通义千问？
**A**: 查看 `CHINESE_API_GUIDE.md` 或 `docs/API_REFERENCE.md`

### Q: 怎样理解系统设计？
**A**: 阅读 `docs/ARCHITECTURE.md`

### Q: 怎样使用不同的 LLM 后端？
**A**: 运行 `examples/different_backends.py`

### Q: API 有哪些参数？
**A**: 查阅 `docs/API_REFERENCE.md`

### Q: 怎样贡献代码？
**A**: 查看 `docs/IMPROVEMENTS.md` 的社区贡献部分

### Q: 项目的短期和长期计划是什么？
**A**: 查看 `docs/IMPROVEMENTS.md` 的 Roadmap 部分

### Q: 有哪些已知的问题？
**A**: 查看 `IMPROVEMENT_REPORT.md` 的已知问题部分

---

## 🎯 学习路径建议

### 路径 1: 快速上手 (30分钟)
1. 阅读 `README.md` (5分钟)
2. 运行 `examples/basic_usage.py` (5分钟)
3. 浏览 `examples/README.md` (5分钟)
4. 尝试修改示例代码 (15分钟)

### 路径 2: 深度理解 (2小时)
1. 阅读 `docs/ARCHITECTURE.md` (30分钟)
2. 查阅 `docs/API_REFERENCE.md` (30分钟)
3. 阅读源代码 `philosofia/core/` (30分钟)
4. 运行和修改示例 (30分钟)

### 路径 3: 贡献代码 (4小时+)
1. 完成路径2 (2小时)
2. 阅读 `PROJECT_ASSESSMENT.md` (30分钟)
3. 查看 `docs/IMPROVEMENTS.md` (30分钟)
4. 选择任务开始贡献 (1小时+)

---

## 📱 不同用户的推荐阅读

### 学生/研究者
- 先读: `README.md` + `docs/ARCHITECTURE.md`
- 后读: `basic.txt` (理论基础)
- 代码: `philosofia/core/agent_system.py`

### 工程师/开发者
- 先读: `docs/API_REFERENCE.md`
- 后读: `docs/ARCHITECTURE.md`
- 示例: `examples/basic_usage.py`

### 项目维护者
- 先读: `IMPROVEMENT_REPORT.md`
- 后读: `docs/IMPROVEMENTS.md`
- 查看: `PROJECT_ASSESSMENT.md`

### 开源贡献者
- 先读: `docs/IMPROVEMENTS.md` (社区部分)
- 后读: `CLEANUP_GUIDE.md`
- 选择: `PROJECT_ASSESSMENT.md` (待改进项)

---

## 🔗 重要链接速查

### 入门文档
| 文档 | 用途 | 阅读时间 |
|------|------|---------|
| README.md | 项目概览 | 10分钟 |
| QUICK_START_CHINESE.md | 快速开始 | 10分钟 |
| examples/README.md | 示例说明 | 5分钟 |

### 参考文档
| 文档 | 用途 | 阅读时间 |
|------|------|---------|
| docs/ARCHITECTURE.md | 系统设计 | 30分钟 |
| docs/API_REFERENCE.md | API手册 | 20分钟 |
| CHINESE_API_GUIDE.md | API配置 | 15分钟 |

### 示例代码
| 示例 | 内容 | 运行时间 |
|------|------|---------|
| basic_usage.py | 基础用法 | 1分钟 |
| different_backends.py | 多后端对比 | 2分钟+ |
| reasoning_trace.py | 推理追踪 | 1分钟 |

### 项目文档
| 文档 | 内容 | 参考价值 |
|------|------|---------|
| IMPROVEMENT_REPORT.md | 改进总结 | ⭐⭐⭐⭐⭐ |
| EXECUTION_SUMMARY.md | 执行总结 | ⭐⭐⭐⭐ |
| PROJECT_ASSESSMENT.md | 项目评估 | ⭐⭐⭐⭐ |
| CLEANUP_GUIDE.md | 清理指南 | ⭐⭐⭐ |

---

## ✅ 快速检查清单

在开始使用前，快速检查：

- [ ] Python 版本 >= 3.8
- [ ] 已安装 `requests` (可选)
- [ ] 已安装 `openai` (如使用OpenAI后端)
- [ ] API密钥已设置 (如使用LLM后端)
- [ ] 可以运行 `examples/basic_usage.py`

在开始贡献前，快速检查：

- [ ] 已阅读 `docs/IMPROVEMENTS.md` (社区部分)
- [ ] 已了解项目 Roadmap
- [ ] 已选择一个待改进项
- [ ] 已准备好开发环境
- [ ] 已查看相关测试用例

---

**最后更新**: 2026年1月29日  
**维护者**: Philosofia Team  
**反馈**: 欢迎提交Issue或Pull Request

