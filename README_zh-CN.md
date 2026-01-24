[English](./README.md) | **简体中文** | [繁體中文](./README_zh-TW.md) | [日本語](./README_ja.md)

# Agent Skills 技能集合

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/技能数量-5-blue.svg)](https://github.com/qiaoshouqing/Skills)

精选的 Agent Skills 技能集合，旨在提升开发效率、自动化常见开发流程。

## 什么是 Agent Skills？

[Agent Skills](https://agentskills.io/) 是一个为 AI 代理提供可复用能力的开放标准。技能遵循 `SKILL.md` 规范，可跨多个 AI 编码工具使用：

**支持的工具：**

Claude Code · OpenAI Codex · Gemini CLI · Cursor · VS Code · Amp · TRAE · Roo Code · Goose 等

通过 `/` 前缀调用（例如 `/env-sync`），为特定任务提供专业功能。

### 核心特性

- **开放标准**：兼容所有支持 [Agent Skills](https://agentskills.io/) 规范的工具
- **按需加载**：技能仅在需要时加载，保持上下文高效
- **自动发现**：放置在对应工具的技能目录中即自动可用
- **可扩展**：轻松创建适合你工作流的自定义技能

## 可用技能

### 🔄 env-sync

在 git worktree 之间同步 `.env` 文件，内置安全机制。

**快速开始：**
```bash
/env-sync
# 或直接说：
# "sync env" / "同步 env" / "copy env"
```

**特性：**
- 🔒 安全优先：不显示 `.env` 内容，覆盖前询问确认
- 🎯 自动检测：自动检测 git worktree 并验证路径
- 🌍 多语言：支持中英文触发短语
- ✅ 验证：确保源文件存在且目标是有效的 worktree

[📖 查看详细文档 →](./env-sync/SKILL.md)

---

### 🎨 daily-news（设计日报）

聚合 Dribbble、Awwwards、Product Hunt、Behance 及 31 位设计领域 Twitter/X 大 V 的内容，生成每日设计灵感与新奇事物报告。**自动检测用户语言**。

**快速开始：**
```bash
/daily-news
# 或直接说：
# "设计日报" / "design daily" / "デザインニュース" / "what's new in design"
```

**特性：**
- 🌍 自动语言检测：以任何语言响应
- 🎨 设计聚焦：Dribbble、Awwwards、Behance、Muzli、Sidebar.io
- 🆕 新奇事物：Product Hunt 新产品、Show HN 创意工具
- 🐦 31 位设计大 V：Julie Zhuo、Don Norman、Jessica Walsh、Brad Frost 等
- 🤖 智能回退：对 JS 重度站点使用 Chrome MCP

**数据源（共 41 个）：**
| 类别 | 来源 |
|------|------|
| 设计平台 | Dribbble、Awwwards、Behance、Muzli、Sidebar.io |
| 新奇产品 | Product Hunt、Hacker News (Show HN)、Kickstarter、GitHub Trending |
| 设计媒体 | Dezeen |
| Twitter 大 V | @joulee、@jessicawalsh、@brad_frost、@scottbelsky、@lukew 等 26 位 |

[📖 查看详细文档 →](./daily-news/SKILL.md)

---

### 🎬 video-downloader

使用 yt-dlp 从 YouTube、Bilibili、Twitter 等 1000+ 个站点下载视频、音频或字幕。

**快速开始：**
```bash
/video-downloader
# 或直接说：
# "下载视频" / "download video" / "extract audio"
```

**特性：**
- 🎥 多平台：YouTube、Bilibili、Twitter 等 1000+ 个站点
- 🎵 音频提取：从视频中提取 MP3/M4A
- 📝 字幕：下载或内嵌字幕
- 🔧 自动安装：自动安装 yt-dlp 和 ffmpeg

[📖 查看详细文档 →](./video-downloader/SKILL.md)

---

### 🚀 ship

一键完成 commit、push 和创建 PR。自动生成 commit message 和详细的 PR 描述（含影响分析）。

**快速开始：**
```bash
/ship
# 或直接说：
# "ship it" / "提交PR" / "发PR"
```

**特性：**
- ⚡ 一键流程：无确认提示，"ship" 即意图
- 🧠 智能分支：在 main/master 上自动创建 feature 分支
- 📝 自动 Commit Message：从 diff 生成规范的 commit message
- 📋 详细 PR：摘要、文件变更表、影响分析、测试计划
- 📦 草稿支持：加 `--draft` 或说 "草稿" 创建草稿 PR

[📖 查看详细文档 →](./ship/SKILL.md)

---

### 📐 code-standards

为任何 AI 编码工具生成通用代码质量标准。基于 Linus Torvalds 的 "Good Taste" 哲学，配备严格的 5 层代码审查框架。

**快速开始：**
```bash
/code-standards
# 或直接说：
# "setup code standards" / "代码规范" / "コード規約"
```

**特性：**
- 🔍 **自动检测**：检测项目中的 AI 工具（Claude、Codex、Cursor、Gemini、Copilot、Windsurf、Aider、Cline）
- 🌍 **4 种语言**：English、简体中文、繁體中文、日本語（自动检测）
- 📋 **5 层代码审查**：数据结构 → 边界情况 → 复杂度 → 破坏性分析 → 必要性
- 🚫 **反模式清单**：拒绝过度工程、不必要的抽象和设计模式滥用

**支持的工具：**
| 工具 | 生成文件 |
|------|----------|
| Claude Code | `CLAUDE.md` |
| OpenAI Codex | `AGENTS.md` |
| Cursor | `.cursor/rules/code-standards.mdc` |
| Gemini CLI | `GEMINI.md` |
| GitHub Copilot | `.github/copilot-instructions.md` |
| Windsurf | `.windsurfrules` |
| Aider | `CONVENTIONS.md` |
| Cline / Roo Code | `.clinerules/code-standards.md` |

[📖 查看详细文档 →](./code-standards/SKILL.md)

## 📦 安装

### 一键安装（推荐）

使用 [skills.sh](https://skills.sh/) 生态的安装方式，一条命令安装所有技能。它会自动检测你已安装的 AI 工具，并将技能放入正确的目录：

```bash
npx skills add qiaoshouqing/Skills
```

安装单个技能：

```bash
npx skills add qiaoshouqing/Skills --skill env-sync
```

### 手动安装

如果你更喜欢手动控制（以 Claude Code 为例）：

```bash
# 克隆仓库
git clone git@github.com:qiaoshouqing/Skills.git ~/claude-skills

# 通过符号链接安装所有技能
cd ~/claude-skills
for skill in */SKILL.md; do
  skill_name=$(dirname "$skill")
  ln -sf "$(pwd)/$skill_name" ~/.claude/skills/
done
```

安装单个技能：

```bash
ln -sf ~/claude-skills/env-sync ~/.claude/skills/env-sync
```

> **注意：** 不同工具使用不同的技能目录。`npx skills add` 会自动处理。手动安装到其他工具时请参考对应文档。

### 验证安装

```bash
# 启动 Claude Code 并测试
cc
> /env-sync --help
```

## 🚀 路线图

- [x] **ship** - 一键 commit、push 和创建 PR
- [x] **code-standards** - 通用代码质量标准生成器（多工具、多语言）
- [ ] **test-runner** - 基于变更的智能测试执行
- [ ] **code-review** - 自动化代码审查清单
- [ ] **docker-helper** - Docker 容器管理工具
- [ ] **api-tester** - 快速 API 端点测试
- [ ] **db-query** - 常见数据库操作助手

有想法？[提个 Issue](https://github.com/qiaoshouqing/Skills/issues) 来建议新技能！

## ❓ FAQ

<details>
<summary><strong>技能存放在哪里？</strong></summary>

技能默认存放在 `~/.claude/skills/`。每个技能是一个目录，至少包含一个 `SKILL.md` 文件。
</details>

<details>
<summary><strong>如何触发技能？</strong></summary>

技能可以通过多种方式触发：
1. 使用 `/` 前缀：`/skill-name`
2. 自然语言："sync env"、"同步 env"
3. 自动触发：某些技能在特定场景下自动激活（如缺少 .env 时）
</details>

<details>
<summary><strong>可以修改现有技能吗？</strong></summary>

可以！如果安装时使用了符号链接：
1. 编辑 `~/claude-skills/skill-name/SKILL.md`
2. 修改立即生效（无需重启）
3. 可以通过 Pull Request 贡献回来
</details>

<details>
<summary><strong>技能和命令有什么区别？</strong></summary>

- **技能**：加载到 Claude 上下文中的可复用提示词/工作流
- **命令**：直接执行的系统级 CLI 命令
- 技能提供指导；命令执行操作
</details>

<details>
<summary><strong>技能是否限定编程语言？</strong></summary>

不！技能适用于任何编程语言。它们提供的指导会由 Claude 应用到你的具体上下文中。
</details>

## 🤝 贡献

欢迎贡献！这是一个不断成长的技能集合，旨在覆盖各种开发工作流。

### 如何贡献

1. **Fork 本仓库**
2. **创建新技能**，遵循以下结构
3. **充分测试**
4. **提交 Pull Request**，附清晰描述

### 技能结构

每个技能必须遵循此结构：

```
skill-name/
├── SKILL.md          # 主技能定义（必需）
├── references/       # 详细文档（可选）
├── examples/         # 示例代码（可选）
└── scripts/          # 工具脚本（可选）
```

### 贡献规范

- 确保技能文档完善且经过测试
- 遵循现有代码风格和结构
- 每个 Pull Request 一个技能
- 包含预期行为的示例
- 在代码审查期间积极响应反馈

## 🐛 故障排除

**技能未加载？**
```bash
# 检查技能目录是否存在
ls -la ~/.claude/skills/

# 验证符号链接是否正确
ls -la ~/.claude/skills/env-sync

# 重新安装
rm ~/.claude/skills/env-sync
ln -sf ~/claude-skills/env-sync ~/.claude/skills/env-sync
```

**技能未触发？**
- 检查 SKILL.md 中的 `description` 字段是否包含触发短语
- 尝试使用提到的精确触发短语
- 使用 `/skill-name` 手动调用

## 📋 环境要求

- **兼容的 AI 工具** - Claude Code、Codex、Gemini CLI、Cursor、VS Code、Amp、TRAE 等
- **Node.js**（可选）- 使用 `npx skills add` 一键安装时需要
- **Git**（可选）- 通过 git clone 安装时需要

**支持平台：**
- macOS（已测试）
- Linux（应可用）
- Windows WSL（应可用）

## 📄 许可证

MIT License - 详见 [LICENSE](./LICENSE) 文件。

## 👤 作者

**qiaoshouqing**
- GitHub: [@qiaoshouqing](https://github.com/qiaoshouqing)

## 💬 支持

- **Issues**: [GitHub Issues](https://github.com/qiaoshouqing/Skills/issues)
- **Discussions**: [GitHub Discussions](https://github.com/qiaoshouqing/Skills/discussions)
- **Email**: 1143878969@qq.com

---

**Made with ❤️ by the community**

如果觉得这些技能有帮助，欢迎：
- ⭐ Star 本仓库
- 🐛 报告 Bug
- 💡 建议新技能
- 🤝 贡献你的技能
