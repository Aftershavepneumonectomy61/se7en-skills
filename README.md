# se7en-skills

Personal [Claude Code](https://claude.ai/code) skills collection by se7en.

## Skills

| Skill | Description |
|-------|-------------|
| **[se7en-style-writer](skills/se7en-style-writer/)** | 万能文风写作——从任意文本中抽取写作风格，在新主题上复现。预装 20+ 经典作家风格库 |
| **[se7en-eight-constructs](skills/se7en-eight-constructs/)** | 八大建构方法论——提示词工程的核心教学体系，覆盖身份/人格/语言/方法/认知/风格/元工具/场域 |
| **[se7en-token-stats](skills/se7en-token-stats/)** | Token 用量统计——扫描 Claude Code 会话数据，生成可视化仪表盘和日历视图 |
| **[se7en-doc-converter](skills/se7en-doc-converter/)** | 文档转写——将 PDF、Word、PPT 转为结构化 Markdown |
| **[se7en-talkline](skills/se7en-talkline/)** | 演讲剧本生成器——把核心表达拆解为戏剧化的逐幕叙事结构 |
| **[se7en-bibigpt](skills/se7en-bibigpt/)** | BibiGPT 视频总结——自动提取视频的 AI 摘要和口播逐字稿 |

## Installation

Clone this repo to your Claude Code plugins directory:

```bash
git clone https://github.com/yiliqi78/se7en-skills.git ~/.claude/plugins/se7en-skills
```

Or clone anywhere and add the path to your Claude Code settings.

## Configuration

Some skills require API keys or external services:

- **se7en-bibigpt**: Requires a [BibiGPT](https://bibigpt.co) API token. Set `BIBIGPT_TOKEN` environment variable or edit the script directly.

## Structure

```
se7en-skills/
├── .claude-plugin/       # Plugin manifest
├── scripts/              # Helper scripts
└── skills/
    ├── se7en-style-writer/
    │   ├── SKILL.md
    │   ├── EXTRACTION_ENGINE.md
    │   ├── styles/           # 20+ pre-built author styles
    │   └── my-styles/        # User's personal style library
    ├── se7en-eight-constructs/
    │   └── SKILL.md
    ├── se7en-token-stats/
    │   ├── SKILL.md
    │   ├── token_stats.py
    │   └── token_calendar.py
    ├── se7en-doc-converter/
    │   └── SKILL.md
    ├── se7en-talkline/
    │   └── SKILL.md
    └── se7en-bibigpt/
        ├── SKILL.md
        └── scripts/
            └── bibigpt_fetch.py
```

## License

MIT
