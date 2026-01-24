[English](./README.md) | [简体中文](./README_zh-CN.md) | **繁體中文** | [日本語](./README_ja.md)

# Agent Skills 技能集合

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/技能數量-5-blue.svg)](https://github.com/qiaoshouqing/Skills)

精選的 Agent Skills 技能集合，旨在提升開發效率、自動化常見開發流程。

## 什麼是 Agent Skills？

[Agent Skills](https://agentskills.io/) 是一個為 AI 代理提供可複用能力的開放標準。技能遵循 `SKILL.md` 規範，可跨多個 AI 編碼工具使用：

**支援的工具：**

Claude Code · OpenAI Codex · Gemini CLI · Cursor · VS Code · Amp · TRAE · Roo Code · Goose 等

透過 `/` 前綴呼叫（例如 `/env-sync`），為特定任務提供專業功能。

### 核心特性

- **開放標準**：相容所有支援 [Agent Skills](https://agentskills.io/) 規範的工具
- **按需載入**：技能僅在需要時載入，保持上下文高效
- **自動發現**：放置在對應工具的技能目錄中即自動可用
- **可擴展**：輕鬆建立適合你工作流程的自訂技能

## 可用技能

### 🔄 env-sync

在 git worktree 之間同步 `.env` 檔案，內建安全機制。

**快速開始：**
```bash
/env-sync
# 或直接說：
# "sync env" / "同步 env" / "copy env"
```

**特性：**
- 🔒 安全優先：不顯示 `.env` 內容，覆蓋前詢問確認
- 🎯 自動偵測：自動偵測 git worktree 並驗證路徑
- 🌍 多語言：支援中英文觸發短語
- ✅ 驗證：確保來源檔案存在且目標是有效的 worktree

[📖 檢視詳細文件 →](./env-sync/SKILL.md)

---

### 🎨 daily-news（設計日報）

彙整 Dribbble、Awwwards、Product Hunt、Behance 及 31 位設計領域 Twitter/X 大 V 的內容，產生每日設計靈感與新奇事物報告。**自動偵測使用者語言**。

**快速開始：**
```bash
/daily-news
# 或直接說：
# "設計日報" / "design daily" / "デザインニュース" / "what's new in design"
```

**特性：**
- 🌍 自動語言偵測：以任何語言回應
- 🎨 設計聚焦：Dribbble、Awwwards、Behance、Muzli、Sidebar.io
- 🆕 新奇事物：Product Hunt 新產品、Show HN 創意工具
- 🐦 31 位設計大 V：Julie Zhuo、Don Norman、Jessica Walsh、Brad Frost 等
- 🤖 智慧回退：對 JS 重度網站使用 Chrome MCP

**資料來源（共 41 個）：**
| 類別 | 來源 |
|------|------|
| 設計平台 | Dribbble、Awwwards、Behance、Muzli、Sidebar.io |
| 新奇產品 | Product Hunt、Hacker News (Show HN)、Kickstarter、GitHub Trending |
| 設計媒體 | Dezeen |
| Twitter 大 V | @joulee、@jessicawalsh、@brad_frost、@scottbelsky、@lukew 等 26 位 |

[📖 檢視詳細文件 →](./daily-news/SKILL.md)

---

### 🎬 video-downloader

使用 yt-dlp 從 YouTube、Bilibili、Twitter 等 1000+ 個網站下載影片、音訊或字幕。

**快速開始：**
```bash
/video-downloader
# 或直接說：
# "下載影片" / "download video" / "extract audio"
```

**特性：**
- 🎥 多平台：YouTube、Bilibili、Twitter 等 1000+ 個網站
- 🎵 音訊擷取：從影片中擷取 MP3/M4A
- 📝 字幕：下載或內嵌字幕
- 🔧 自動安裝：自動安裝 yt-dlp 和 ffmpeg

[📖 檢視詳細文件 →](./video-downloader/SKILL.md)

---

### 🚀 ship

一鍵完成 commit、push 和建立 PR。自動產生 commit message 和詳細的 PR 描述（含影響分析）。

**快速開始：**
```bash
/ship
# 或直接說：
# "ship it" / "提交PR" / "發PR"
```

**特性：**
- ⚡ 一鍵流程：無確認提示，"ship" 即意圖
- 🧠 智慧分支：在 main/master 上自動建立 feature 分支
- 📝 自動 Commit Message：從 diff 產生規範的 commit message
- 📋 詳細 PR：摘要、檔案變更表、影響分析、測試計畫
- 📦 草稿支援：加 `--draft` 或說「草稿」建立草稿 PR

[📖 檢視詳細文件 →](./ship/SKILL.md)

---

### 📐 code-standards

為任何 AI 編碼工具產生通用程式碼品質標準。基於 Linus Torvalds 的「Good Taste」哲學，配備嚴格的 5 層程式碼審查框架。

**快速開始：**
```bash
/code-standards
# 或直接說：
# "setup code standards" / "代码规范" / "コード規約"
```

**特性：**
- 🔍 **自動偵測**：偵測專案中的 AI 工具（Claude、Codex、Cursor、Gemini、Copilot、Windsurf、Aider、Cline）
- 🌍 **4 種語言**：English、简体中文、繁體中文、日本語（自動偵測）
- 📋 **5 層程式碼審查**：資料結構 → 邊界情況 → 複雜度 → 破壞性分析 → 必要性
- 🚫 **反模式清單**：拒絕過度工程、不必要的抽象和設計模式濫用

**支援的工具：**
| 工具 | 產生檔案 |
|------|----------|
| Claude Code | `CLAUDE.md` |
| OpenAI Codex | `AGENTS.md` |
| Cursor | `.cursor/rules/code-standards.mdc` |
| Gemini CLI | `GEMINI.md` |
| GitHub Copilot | `.github/copilot-instructions.md` |
| Windsurf | `.windsurfrules` |
| Aider | `CONVENTIONS.md` |
| Cline / Roo Code | `.clinerules/code-standards.md` |

[📖 檢視詳細文件 →](./code-standards/SKILL.md)

## 📦 安裝

### 一鍵安裝（推薦）

使用 [skills.sh](https://skills.sh/) 生態的安裝方式，一條指令安裝所有技能。它會自動偵測你已安裝的 AI 工具，並將技能放入正確的目錄：

```bash
npx skills add qiaoshouqing/Skills
```

安裝單個技能：

```bash
npx skills add qiaoshouqing/Skills --skill env-sync
```

### 手動安裝

如果你更喜歡手動控制（以 Claude Code 為例）：

```bash
# 複製儲存庫
git clone git@github.com:qiaoshouqing/Skills.git ~/claude-skills

# 透過符號連結安裝所有技能
cd ~/claude-skills
for skill in */SKILL.md; do
  skill_name=$(dirname "$skill")
  ln -sf "$(pwd)/$skill_name" ~/.claude/skills/
done
```

安裝單個技能：

```bash
ln -sf ~/claude-skills/env-sync ~/.claude/skills/env-sync
```

> **注意：** 不同工具使用不同的技能目錄。`npx skills add` 會自動處理。手動安裝到其他工具時請參考對應文件。

### 驗證安裝

```bash
# 啟動 Claude Code 並測試
cc
> /env-sync --help
```

## 🚀 路線圖

- [x] **ship** - 一鍵 commit、push 和建立 PR
- [x] **code-standards** - 通用程式碼品質標準產生器（多工具、多語言）
- [ ] **test-runner** - 基於變更的智慧測試執行
- [ ] **code-review** - 自動化程式碼審查清單
- [ ] **docker-helper** - Docker 容器管理工具
- [ ] **api-tester** - 快速 API 端點測試
- [ ] **db-query** - 常見資料庫操作助手

有想法？[提個 Issue](https://github.com/qiaoshouqing/Skills/issues) 來建議新技能！

## ❓ FAQ

<details>
<summary><strong>技能存放在哪裡？</strong></summary>

技能預設存放在 `~/.claude/skills/`。每個技能是一個目錄，至少包含一個 `SKILL.md` 檔案。
</details>

<details>
<summary><strong>如何觸發技能？</strong></summary>

技能可以透過多種方式觸發：
1. 使用 `/` 前綴：`/skill-name`
2. 自然語言："sync env"、"同步 env"
3. 自動觸發：某些技能在特定場景下自動啟動（如缺少 .env 時）
</details>

<details>
<summary><strong>可以修改現有技能嗎？</strong></summary>

可以！如果安裝時使用了符號連結：
1. 編輯 `~/claude-skills/skill-name/SKILL.md`
2. 修改立即生效（無需重新啟動）
3. 可以透過 Pull Request 貢獻回來
</details>

<details>
<summary><strong>技能和命令有什麼區別？</strong></summary>

- **技能**：載入到 Claude 上下文中的可複用提示詞/工作流程
- **命令**：直接執行的系統級 CLI 命令
- 技能提供指導；命令執行操作
</details>

<details>
<summary><strong>技能是否限定程式語言？</strong></summary>

不！技能適用於任何程式語言。它們提供的指導會由 Claude 應用到你的具體上下文中。
</details>

## 🤝 貢獻

歡迎貢獻！這是一個不斷成長的技能集合，旨在涵蓋各種開發工作流程。

### 如何貢獻

1. **Fork 本儲存庫**
2. **建立新技能**，遵循以下結構
3. **充分測試**
4. **提交 Pull Request**，附清晰描述

### 技能結構

每個技能必須遵循此結構：

```
skill-name/
├── SKILL.md          # 主技能定義（必需）
├── references/       # 詳細文件（選用）
├── examples/         # 範例程式碼（選用）
└── scripts/          # 工具腳本（選用）
```

### 貢獻規範

- 確保技能文件完善且經過測試
- 遵循現有程式碼風格和結構
- 每個 Pull Request 一個技能
- 包含預期行為的範例
- 在程式碼審查期間積極回應回饋

## 🐛 故障排除

**技能未載入？**
```bash
# 檢查技能目錄是否存在
ls -la ~/.claude/skills/

# 驗證符號連結是否正確
ls -la ~/.claude/skills/env-sync

# 重新安裝
rm ~/.claude/skills/env-sync
ln -sf ~/claude-skills/env-sync ~/.claude/skills/env-sync
```

**技能未觸發？**
- 檢查 SKILL.md 中的 `description` 欄位是否包含觸發短語
- 嘗試使用提到的精確觸發短語
- 使用 `/skill-name` 手動呼叫

## 📋 環境需求

- **相容的 AI 工具** - Claude Code、Codex、Gemini CLI、Cursor、VS Code、Amp、TRAE 等
- **Node.js**（選用）- 使用 `npx skills add` 一鍵安裝時需要
- **Git**（選用）- 透過 git clone 安裝時需要

**支援平台：**
- macOS（已測試）
- Linux（應可用）
- Windows WSL（應可用）

## 📄 授權條款

MIT License - 詳見 [LICENSE](./LICENSE) 檔案。

## 👤 作者

**qiaoshouqing**
- GitHub: [@qiaoshouqing](https://github.com/qiaoshouqing)

## 💬 支援

- **Issues**: [GitHub Issues](https://github.com/qiaoshouqing/Skills/issues)
- **Discussions**: [GitHub Discussions](https://github.com/qiaoshouqing/Skills/discussions)
- **Email**: 1143878969@qq.com

---

**Made with ❤️ by the community**

如果覺得這些技能有幫助，歡迎：
- ⭐ Star 本儲存庫
- 🐛 回報 Bug
- 💡 建議新技能
- 🤝 貢獻你的技能
