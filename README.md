# se7en-skills

[Claude Code](https://claude.ai/code) 开源 Skills 合集。

## Skills 一览

| Skill | 说明 |
|-------|------|
| **[se7en-style-writer](skills/se7en-style-writer/)** | 万能文风写作——从任意文本中抽取写作风格，在新主题上复现。预装 20+ 经典作家风格库 |
| **[se7en-eight-constructs](skills/se7en-eight-constructs/)** | 八大建构方法论——提示词工程的核心教学体系，覆盖身份/人格/语言/方法/认知/风格/元工具/场域 |
| **[se7en-token-stats](skills/se7en-token-stats/)** | Token 用量统计——扫描 Claude Code 会话数据，生成可视化仪表盘和日历视图 |
| **[se7en-doc-converter](skills/se7en-doc-converter/)** | 文档转写——将 PDF、Word、PPT 转为结构化 Markdown |
| **[se7en-talkline](skills/se7en-talkline/)** | 演讲剧本生成器——把核心表达拆解为戏剧化的逐幕叙事结构 |
| **[se7en-bibigpt](skills/se7en-bibigpt/)** | BibiGPT 视频总结——自动提取视频的 AI 摘要和口播逐字稿 |
| **[se7en-fitness-tracker](skills/se7en-fitness-tracker/)** | 健身追踪——体测录入、体重打卡、饮食记录与营养估算、训练方案生成、看板可视化 |

## 安装

克隆到 Claude Code 插件目录：

```bash
git clone https://github.com/yiliqi78/se7en-skills.git ~/.claude/plugins/se7en-skills
```

也可以克隆到任意位置，然后在 Claude Code 设置中添加路径。

## 配置

部分 skill 需要 API key 或外部服务：

- **se7en-bibigpt**：需要 [BibiGPT](https://bibigpt.co) API token。设置环境变量 `BIBIGPT_TOKEN`，或直接编辑脚本。

## 目录结构

```
se7en-skills/
├── .claude-plugin/       # 插件清单
├── scripts/              # 辅助脚本
└── skills/
    ├── se7en-style-writer/
    │   ├── SKILL.md
    │   ├── EXTRACTION_ENGINE.md    # 风格抽取引擎
    │   ├── styles/                 # 20+ 预装作家风格
    │   └── my-styles/              # 个人风格库（可生长）
    ├── se7en-eight-constructs/
    │   └── SKILL.md
    ├── se7en-token-stats/
    │   ├── SKILL.md
    │   ├── token_stats.py          # 仪表盘
    │   └── token_calendar.py       # 日历视图
    ├── se7en-doc-converter/
    │   └── SKILL.md
    ├── se7en-talkline/
    │   └── SKILL.md
    ├── se7en-bibigpt/
    │   ├── SKILL.md
    │   └── scripts/
    │       └── bibigpt_fetch.py
    └── se7en-fitness-tracker/
        └── SKILL.md
```

## 贡献

欢迎提交新的 skill 或改进现有 skill。

### 添加新 skill

1. 在 `skills/` 下创建目录，命名格式：`{你的前缀}-{skill名}`
2. 目录内必须包含 `SKILL.md` 作为入口
3. 辅助文件放在 `references/`、`assets/`、`scripts/` 子目录
4. 提交 PR，在 PR 描述中说明 skill 的用途和触发方式

### 注意事项

- **不要提交 API key 或个人敏感信息**——用环境变量或配置文件引导用户自行设置
- **不要硬编码个人路径**——用相对路径或让用户自定义

## License

MIT
