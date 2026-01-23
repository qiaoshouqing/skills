# Claude Code Skills Collection

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/skills-3-blue.svg)](https://github.com/qiaoshouqing/Skills)

A curated collection of custom skills for Claude Code, designed to enhance productivity and automate common development workflows.

## What are Claude Code Skills?

Skills are reusable, shareable prompts that extend Claude Code's capabilities. They are invoked using the `/` prefix (e.g., `/env-sync`) and provide specialized functionality for specific tasks.

### Key Features

- **Progressive Disclosure**: Skills load only what's needed, keeping context efficient
- **Auto-Discovery**: Place skills in `~/.claude/skills/` and they're automatically available
- **Extensible**: Easy to create custom skills for your specific workflows

## Available Skills

### 🔄 env-sync

Syncs `.env` files from git root repository to git worktrees with security built-in.

**Quick Start:**
```bash
# In your git worktree
/env-sync
# or simply ask:
# "sync env" / "copy env" / "同步 env"
```

**Features:**
- 🔒 **Security First**: Never displays `.env` contents, always asks before overwriting
- 🎯 **Auto-Detection**: Automatically detects git worktrees and validates paths
- 🌍 **Multilingual**: Supports English and Chinese trigger phrases
- ✅ **Validation**: Ensures source exists and target is a valid worktree

**Use Cases:**
- Working in a git worktree that lacks a .env file
- Setting up environment for a new worktree
- Keeping environment variables synchronized across worktrees

**Example:**
```bash
# You're in a worktree at: /project/.worktrees/feature-branch
# Root repo at: /project/ (has .env)
$ cc
> sync env
✓ Synced .env from /project/
```

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
- 🌍 **Auto Language Detection**: Responds in ANY language
- 🎨 **Design-Focused**: Dribbble, Awwwards, Behance, Muzli, Sidebar.io
- 🆕 **Novel Things**: Product Hunt new products, Show HN creative tools
- 🐦 **31 Design Influencers**: Julie Zhuo, Don Norman, Jessica Walsh, Brad Frost, Scott Belsky, and more
- 🤖 **Smart Fallback**: Uses Chrome MCP for JS-heavy sites

**Data Sources (41 total):**
| Category | Sources |
|----------|---------|
| Design Platforms | Dribbble, Awwwards, Behance, Muzli, Sidebar.io |
| Novel Products | Product Hunt, Hacker News (Show HN), Kickstarter, GitHub Trending |
| Design Media | Dezeen |
| Twitter Influencers | @joulee, @jessicawalsh, @brad_frost, @scottbelsky, @lukew, +26 more |

**Example:**
```bash
$ cc
> 设计日报

检测到中文，将以中文生成设计日报。
正在采集设计资讯...
✅ Sidebar.io (5 条)
✅ Dribbble (8 条)
✅ Awwwards (5 条)
✅ Product Hunt (5 条)
...
日报已保存至: NewsReport/2026-01-23-design-daily.md
```

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
- 🎥 **Multi-Platform**: YouTube, Bilibili, Twitter, and 1000+ sites
- 🎵 **Audio Extraction**: Extract MP3/M4A from videos
- 📝 **Subtitles**: Download or embed subtitles
- 🔧 **Auto-Install**: Automatically installs yt-dlp and ffmpeg

[📖 View detailed documentation →](./video-downloader/SKILL.md)

## 📦 Installation

### Prerequisites

- [Claude Code CLI](https://claude.ai/download) installed
- Skills directory at `~/.claude/skills/` (created automatically on first run)

### Quick Install (Recommended)

Install all skills at once using symlinks:

```bash
# Clone this repository
git clone git@github.com:qiaoshouqing/Skills.git ~/claude-skills

# Create symlinks for all skills
cd ~/claude-skills
for skill in */SKILL.md; do
  skill_name=$(dirname "$skill")
  ln -sf "$(pwd)/$skill_name" ~/.claude/skills/
done

# Verify installation
ls -la ~/.claude/skills/
```

### Individual Skill Installation

Install only specific skills you need:

```bash
# Clone the repository
git clone git@github.com:qiaoshouqing/Skills.git ~/claude-skills

# Install only env-sync
ln -sf ~/claude-skills/env-sync ~/.claude/skills/env-sync
```

### Manual Installation

Copy skills directly without git:

```bash
# Download and extract
curl -L https://github.com/qiaoshouqing/Skills/archive/refs/heads/main.zip -o skills.zip
unzip skills.zip
cd Skills-main

# Copy specific skill
cp -r env-sync ~/.claude/skills/

# Clean up
cd .. && rm -rf Skills-main skills.zip
```

### Verify Installation

```bash
# List installed skills
ls ~/.claude/skills/

# Start Claude Code and test
cc
> /env-sync --help
```

## 🚀 Roadmap

Planned skills for future releases:

- [ ] **git-commit-ai** - AI-assisted commit message generation
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

Yes! If you used symlinks during installation, you can:
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

### Creating a New Skill

**Step 1: Create the directory structure**

```bash
cd ~/claude-skills
mkdir -p my-skill/{references,examples,scripts}
touch my-skill/SKILL.md
```

**Step 2: Write SKILL.md with proper frontmatter**

```yaml
---
name: my-skill
description: "This skill should be used when the user asks to 'trigger phrase 1', 'trigger phrase 2', or mentions specific keywords. Be specific about when to activate."
version: "1.0.0"
metadata:
  author: your-name
---

# Skill Title

Brief description of what this skill does.

## When to Use

- Specific scenario 1
- Specific scenario 2
- Specific scenario 3

## Instructions for Agent

Step-by-step instructions on how Claude should use this skill...
```

**Step 3: Follow best practices**

- ✅ Use third-person in description ("This skill should be used when...")
- ✅ Include specific trigger phrases users would say
- ✅ Keep SKILL.md focused (~1,500-2,000 words)
- ✅ Use imperative form in instructions ("Do X" not "You should do X")
- ✅ Move detailed content to `references/` directory
- ✅ Provide working examples in `examples/` directory

**Step 4: Test your skill**

```bash
# Install locally
ln -sf ~/claude-skills/my-skill ~/.claude/skills/my-skill

# Test in Claude Code
cc
> /my-skill
```

**Step 5: Submit PR**

- Include a clear description of the skill's purpose
- Add usage examples
- Update this README to list your skill

### Contribution Guidelines

- Ensure skills are well-documented and tested
- Follow the existing code style and structure
- One skill per pull request
- Include examples of expected behavior
- Be responsive to feedback during code review

For detailed skill development guidelines, see [Claude Code's official skill development documentation](~/.claude/plugins/marketplaces/claude-plugins-official/plugins/plugin-dev/skills/skill-development/SKILL.md)

## 📋 Requirements

- **Claude Code CLI** - [Download here](https://claude.ai/download)
- **Git** (optional) - For installation via git clone
- **Bash/Zsh** - For running installation scripts

**Supported Platforms:**
- macOS (tested)
- Linux (should work)
- Windows WSL (should work)

## 📚 Resources

- [Claude Code Documentation](https://docs.anthropic.com/claude/docs)
- [Skill Development Guide](https://github.com/anthropics/claude-code)
- [Official Skills Marketplace](https://claude.ai/skills)

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

## 📄 License

MIT License - see [LICENSE](./LICENSE) file for details.

This means you can:
- ✅ Use commercially
- ✅ Modify and distribute
- ✅ Use privately
- ✅ Sublicense

## 👤 Author

**qiaoshouqing**
- GitHub: [@qiaoshouqing](https://github.com/qiaoshouqing)

## 💬 Support

- **Issues**: [GitHub Issues](https://github.com/qiaoshouqing/Skills/issues)
- **Discussions**: [GitHub Discussions](https://github.com/qiaoshouqing/Skills/discussions)
- **Email**: 1143878969@qq.com

For general Claude Code questions, visit [Claude Code Documentation](https://docs.anthropic.com/claude/docs).

## ⭐ Acknowledgments

Built with [Claude Code](https://claude.ai/code) - An AI-powered coding assistant.

---

**Made with ❤️ by the community**

If you find these skills helpful, please consider:
- ⭐ Starring this repository
- 🐛 Reporting bugs and issues
- 💡 Suggesting new skills
- 🤝 Contributing your own skills
