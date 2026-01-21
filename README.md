# Claude Code Skills Collection

A curated collection of custom skills for Claude Code, designed to enhance productivity and automate common development workflows.

## What are Claude Code Skills?

Skills are reusable, shareable prompts that extend Claude Code's capabilities. They are invoked using the `/` prefix (e.g., `/env-sync`) and provide specialized functionality for specific tasks.

## Available Skills

### env-sync

Syncs `.env` files from git root repository to git worktrees.

**Usage:** `/env-sync` or ask Claude to "sync env" or "copy env"

**Use cases:**
- Working in a git worktree that lacks a .env file
- Setting up environment for a new worktree
- Keeping environment variables synchronized across worktrees

[View detailed documentation →](./env-sync/SKILL.md)

## Installation

### Installing Individual Skills

1. Copy the skill directory to your Claude skills folder:
   ```bash
   cp -r env-sync ~/.claude/skills/
   ```

2. The skill will be automatically available in Claude Code

### Installing All Skills

```bash
# Clone this repository
git clone <your-repo-url> ~/claude-skills

# Create symlinks to your Claude skills directory
ln -s ~/claude-skills/env-sync ~/.claude/skills/env-sync
```

## Contributing

This is a growing collection of skills. More skills will be added over time to cover various development workflows.

### Skill Structure

Each skill should follow this structure:
```
skill-name/
├── SKILL.md          # Main skill definition (required)
└── README.md         # Additional documentation (optional)
```

### Creating a New Skill

1. Create a new directory with your skill name
2. Add a `SKILL.md` file with frontmatter:
   ```yaml
   ---
   name: skill-name
   description: "Brief description"
   version: "1.0.0"
   metadata:
     author: your-name
   ---
   ```
3. Document the skill's purpose, usage, and instructions

## Requirements

- Claude Code CLI
- Skills are stored in `~/.claude/skills/` by default

## License

MIT License - see [LICENSE](./LICENSE) file for details

## Author

Created by qiaoshouqing

## Support

For issues, questions, or suggestions, please open an issue in this repository.
