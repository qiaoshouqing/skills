**English** | [简体中文](./README_zh-CN.md) | [繁體中文](./README_zh-TW.md) | [日本語](./README_ja.md)

# Agent Skills Collection

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/skills-6-blue.svg)](https://github.com/qiaoshouqing/Skills)

A curated collection of agent skills designed to enhance productivity and automate common development workflows.

## What are Agent Skills?

[Agent Skills](https://agentskills.io/) are an open standard for giving AI agents reusable capabilities. Skills follow the `SKILL.md` specification and work across multiple AI coding tools:

**Supported Agents:**

Claude Code · OpenAI Codex · Gemini CLI · Cursor · VS Code · Amp · TRAE · Roo Code · Goose · and more

Skills are invoked using the `/` prefix (e.g., `/env-sync`) and provide specialized functionality for specific tasks.

### Key Features

- **Open Standard**: Works across all agents that support the [Agent Skills](https://agentskills.io/) specification
- **Progressive Disclosure**: Skills load only what's needed, keeping context efficient
- **Auto-Discovery**: Place skills in your agent's skills directory and they're automatically available
- **Extensible**: Easy to create custom skills for your specific workflows

## Available Skills

### 🔄 env-sync

Syncs `.env` files from git root repository to git worktrees with security built-in.

**Quick Start:**
```bash
/env-sync
# or simply ask:
# "sync env" / "copy env" / "同步 env"
```

**Features:**
- 🔒 Security First: Never displays `.env` contents, always asks before overwriting
- 🎯 Auto-Detection: Automatically detects git worktrees and validates paths
- 🌍 Multilingual: Supports English and Chinese trigger phrases
- ✅ Validation: Ensures source exists and target is a valid worktree

[📖 View detailed documentation →](./env-sync/SKILL.md)

---

### 🎨 daily-news (Design Daily)

Generate daily design inspiration & novel things reports by aggregating from Dribbble, Awwwards, Product Hunt, Behance, and 31 design influencers on Twitter/X. **Auto-detects user language**.

**Quick Start:**
```bash
/daily-news
# or simply ask:
# "design daily" / "设计日报" / "デザインニュース" / "what's new in design"
```

**Features:**
- 🌍 Auto Language Detection: Responds in ANY language
- 🎨 Design-Focused: Dribbble, Awwwards, Behance, Muzli, Sidebar.io
- 🆕 Novel Things: Product Hunt new products, Show HN creative tools
- 🐦 31 Design Influencers: Julie Zhuo, Don Norman, Jessica Walsh, Brad Frost, and more
- 🤖 Smart Fallback: Uses Chrome MCP for JS-heavy sites

**Data Sources (41 total):**
| Category | Sources |
|----------|---------|
| Design Platforms | Dribbble, Awwwards, Behance, Muzli, Sidebar.io |
| Novel Products | Product Hunt, Hacker News (Show HN), Kickstarter, GitHub Trending |
| Design Media | Dezeen |
| Twitter Influencers | @joulee, @jessicawalsh, @brad_frost, @scottbelsky, @lukew, +26 more |

[📖 View detailed documentation →](./daily-news/SKILL.md)

---

### 🎬 video-downloader

Download videos, audio, or subtitles from YouTube, Bilibili, Twitter and 1000+ sites using yt-dlp.

**Quick Start:**
```bash
/video-downloader
# or simply ask:
# "download video" / "下载视频" / "extract audio"
```

**Features:**
- 🎥 Multi-Platform: YouTube, Bilibili, Twitter, and 1000+ sites
- 🎵 Audio Extraction: Extract MP3/M4A from videos
- 📝 Subtitles: Download or embed subtitles
- 🔧 Auto-Install: Automatically installs yt-dlp and ffmpeg

[📖 View detailed documentation →](./video-downloader/SKILL.md)

---

### 🚀 ship

Commit, push, and create a PR in one step. Auto-generates commit messages and detailed PR descriptions with impact analysis.

**Quick Start:**
```bash
/ship
# or simply ask:
# "ship it" / "提交PR" / "发PR"
```

**Features:**
- ⚡ One-Click Flow: No confirmation prompts - "ship" is the intent
- 🧠 Smart Branch: Auto-creates feature branch if on main/master
- 📝 Auto Commit Message: Generates conventional commit messages from diff
- 📋 Detailed PR: Summary, file changes table, impact analysis, test plan
- 📦 Draft Support: Add `--draft` or say "草稿" for draft PRs

[📖 View detailed documentation →](./ship/SKILL.md)

---

### 🔁 pr-review-loop

Submit or monitor a GitHub pull request with a short polling loop that waits for automated review, fixes actionable feedback, pushes updates, and stops when the PR is merge-ready.

**Quick Start:**
```bash
/pr-review-loop
# or simply ask:
# "create a PR and watch reviews" / "keep checking PR feedback" / "PR review loop"
```

**Features:**
- 🤖 Agent-Agnostic: Works with any agent that can use GitHub CLI, git, and repo-native tests
- 🔁 Short Polling Loop: Default 3-minute review/check cadence
- 🧵 Thread-Aware Review State: Uses GitHub review threads, not only flat comments
- 🔧 Actionable Feedback Fixes: Implements review comments with focused verification
- 🛑 Clear Stop Conditions: Stops when merged, closed, merge-ready, or truly blocked

[📖 View detailed documentation →](./pr-review-loop/SKILL.md)

---

### 📐 code-standards

Generate universal code quality standards for any AI coding tool. Based on Linus Torvalds' "Good Taste" philosophy with a rigorous 5-layer code review framework.

**Quick Start:**
```bash
/code-standards
# or simply ask:
# "setup code standards" / "代码规范" / "コード規約"
```

**Features:**
- 🔍 **Auto-Detection**: Detects AI tools in your project (Claude, Codex, Cursor, Gemini, Copilot, Windsurf, Aider, Cline)
- 🌍 **4 Languages**: English, 简体中文, 繁體中文, 日本語 (auto-detected)
- 📋 **5-Layer Code Review**: Data structures → Edge cases → Complexity → Destructive analysis → Necessity
- 🚫 **Anti-Pattern List**: Reject over-engineering, unnecessary abstractions, and design pattern abuse

**Supported Tools:**
| Tool | Generated File |
|------|---------------|
| Claude Code | `CLAUDE.md` |
| OpenAI Codex | `AGENTS.md` |
| Cursor | `.cursor/rules/code-standards.mdc` |
| Gemini CLI | `GEMINI.md` |
| GitHub Copilot | `.github/copilot-instructions.md` |
| Windsurf | `.windsurfrules` |
| Aider | `CONVENTIONS.md` |
| Cline / Roo Code | `.clinerules/code-standards.md` |

[📖 View detailed documentation →](./code-standards/SKILL.md)

## 📦 Installation

### One-Command Install (Recommended)

Install all skills with a single command using the [skills.sh](https://skills.sh/) ecosystem. It auto-detects your installed agents and places skills in the correct directories:

```bash
npx skills add qiaoshouqing/Skills
```

Install a single skill:

```bash
npx skills add qiaoshouqing/Skills --skill env-sync
```

### Manual Installation

If you prefer manual control (example for Claude Code):

```bash
# Clone the repository
git clone git@github.com:qiaoshouqing/Skills.git ~/claude-skills

# Install all skills via symlinks
cd ~/claude-skills
for skill in */SKILL.md; do
  skill_name=$(dirname "$skill")
  ln -sf "$(pwd)/$skill_name" ~/.claude/skills/
done
```

Install a single skill:

```bash
ln -sf ~/claude-skills/env-sync ~/.claude/skills/env-sync
```

> **Note:** Different agents use different skill directories. `npx skills add` handles this automatically. For manual installation to other agents, refer to their documentation.

### Verify Installation

```bash
# Start Claude Code and test
cc
> /env-sync --help
```

## 🚀 Roadmap

- [x] **ship** - One-click commit, push, and PR creation
- [x] **pr-review-loop** - Poll PR reviews, fix feedback, and stop when merge-ready
- [x] **code-standards** - Universal code quality standards generator (multi-tool, multi-language)
- [ ] **test-runner** - Smart test execution based on changes
- [ ] **code-review** - Automated code review checklist
- [ ] **docker-helper** - Docker container management utilities
- [ ] **api-tester** - Quick API endpoint testing
- [ ] **db-query** - Database query helper for common operations

Have ideas? [Open an issue](https://github.com/qiaoshouqing/Skills/issues) to suggest new skills!

## ❓ FAQ

<details>
<summary><strong>Where are skills stored?</strong></summary>

Skills are stored in `~/.claude/skills/` by default. Each skill is a directory containing at minimum a `SKILL.md` file.
</details>

<details>
<summary><strong>How do I trigger a skill?</strong></summary>

Skills can be triggered in multiple ways:
1. Using the `/` prefix: `/skill-name`
2. Natural language: "sync env", "copy env"
3. Auto-trigger: Some skills activate automatically (e.g., when .env is missing)
</details>

<details>
<summary><strong>Can I modify existing skills?</strong></summary>

Yes! If you used symlinks during installation:
1. Edit the skill in `~/claude-skills/skill-name/SKILL.md`
2. Changes are immediately available (no restart needed)
3. Commit and contribute back via pull request
</details>

<details>
<summary><strong>How do skills differ from commands?</strong></summary>

- **Skills**: Reusable prompts/workflows loaded into Claude's context
- **Commands**: System-level CLI commands that execute directly
- Skills provide guidance; commands execute actions
</details>

<details>
<summary><strong>Are skills language-specific?</strong></summary>

No! Skills work with any programming language. They provide guidance that Claude applies to your specific context.
</details>

## 🤝 Contributing

We welcome contributions! This is a growing collection of skills designed to cover various development workflows.

### How to Contribute

1. **Fork this repository**
2. **Create a new skill** following the structure below
3. **Test thoroughly** in your own environment
4. **Submit a pull request** with a clear description

### Skill Structure

Each skill must follow this structure:

```
skill-name/
├── SKILL.md          # Main skill definition (required)
├── references/       # Detailed documentation (optional)
├── examples/         # Working code examples (optional)
└── scripts/          # Utility scripts (optional)
```

### Contribution Guidelines

- Ensure skills are well-documented and tested
- Follow the existing code style and structure
- One skill per pull request
- Include examples of expected behavior
- Be responsive to feedback during code review

## 🐛 Troubleshooting

**Skills not loading?**
```bash
# Check skills directory exists
ls -la ~/.claude/skills/

# Verify symlinks are correct
ls -la ~/.claude/skills/env-sync

# Reinstall
rm ~/.claude/skills/env-sync
ln -sf ~/claude-skills/env-sync ~/.claude/skills/env-sync
```

**Skill not triggering?**
- Check the `description` field in SKILL.md for trigger phrases
- Try using the exact trigger phrase mentioned
- Use `/skill-name` to manually invoke

## 📋 Requirements

- **A compatible AI agent** - Claude Code, Codex, Gemini CLI, Cursor, VS Code, Amp, TRAE, etc.
- **Node.js** (optional) - Required for `npx skills add` one-command install
- **Git** (optional) - For installation via git clone

**Supported Platforms:**
- macOS (tested)
- Linux (should work)
- Windows WSL (should work)

## 📄 License

MIT License - see [LICENSE](./LICENSE) file for details.

## 👤 Author

**qiaoshouqing**
- GitHub: [@qiaoshouqing](https://github.com/qiaoshouqing)

## 💬 Support

- **Issues**: [GitHub Issues](https://github.com/qiaoshouqing/Skills/issues)
- **Discussions**: [GitHub Discussions](https://github.com/qiaoshouqing/Skills/discussions)
- **Email**: 1143878969@qq.com

---

**Made with ❤️ by the community**

If you find these skills helpful, please consider:
- ⭐ Starring this repository
- 🐛 Reporting bugs and issues
- 💡 Suggesting new skills
- 🤝 Contributing your own skills
