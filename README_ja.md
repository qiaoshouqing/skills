[English](./README.md) | [简体中文](./README_zh-CN.md) | [繁體中文](./README_zh-TW.md) | **日本語**

# Agent Skills コレクション

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/スキル数-5-blue.svg)](https://github.com/qiaoshouqing/Skills)

開発効率の向上と一般的な開発ワークフローの自動化を目的とした、Agent Skills のコレクションです。

## Agent Skills とは？

[Agent Skills](https://agentskills.io/) は、AI エージェントに再利用可能な能力を提供するオープンスタンダードです。スキルは `SKILL.md` 仕様に準拠し、複数の AI コーディングツールで利用可能です：

**対応ツール：**

Claude Code · OpenAI Codex · Gemini CLI · Cursor · VS Code · Amp · TRAE · Roo Code · Goose など

`/` プレフィックスで呼び出し（例：`/env-sync`）、特定のタスクに特化した機能を提供します。

### 主な特徴

- **オープンスタンダード**：[Agent Skills](https://agentskills.io/) 仕様をサポートする全ツールに対応
- **段階的ロード**：必要な時だけスキルをロードし、コンテキストを効率的に維持
- **自動検出**：対応ツールのスキルディレクトリに配置するだけで自動的に利用可能
- **拡張性**：ワークフローに合わせたカスタムスキルを簡単に作成可能

## 利用可能なスキル

### 🔄 env-sync

git ルートリポジトリから git worktree へ `.env` ファイルを同期。セキュリティ機能内蔵。

**クイックスタート：**
```bash
/env-sync
# または：
# "sync env" / "同步 env" / "copy env"
```

**機能：**
- 🔒 セキュリティ優先：`.env` の内容を表示せず、上書き前に確認
- 🎯 自動検出：git worktree を自動検出しパスを検証
- 🌍 多言語対応：英語・中国語のトリガーフレーズに対応
- ✅ バリデーション：ソースの存在とターゲットが有効な worktree であることを確認

[📖 詳細ドキュメント →](./env-sync/SKILL.md)

---

### 🎨 daily-news（デザインデイリー）

Dribbble、Awwwards、Product Hunt、Behance、Twitter/X の31人のデザインインフルエンサーから集約し、デザインインスピレーション＆新しいものレポートを毎日生成。**ユーザー言語を自動検出**。

**クイックスタート：**
```bash
/daily-news
# または：
# "デザインニュース" / "design daily" / "设计日报" / "what's new in design"
```

**機能：**
- 🌍 自動言語検出：あらゆる言語で応答
- 🎨 デザイン特化：Dribbble、Awwwards、Behance、Muzli、Sidebar.io
- 🆕 新しいもの：Product Hunt の新製品、Show HN のクリエイティブツール
- 🐦 31人のデザインインフルエンサー：Julie Zhuo、Don Norman、Jessica Walsh、Brad Frost など
- 🤖 スマートフォールバック：JS 多用サイトには Chrome MCP を使用

**データソース（全41件）：**
| カテゴリ | ソース |
|----------|--------|
| デザインプラットフォーム | Dribbble、Awwwards、Behance、Muzli、Sidebar.io |
| 新製品 | Product Hunt、Hacker News (Show HN)、Kickstarter、GitHub Trending |
| デザインメディア | Dezeen |
| Twitter インフルエンサー | @joulee、@jessicawalsh、@brad_frost、@scottbelsky、@lukew 他26名 |

[📖 詳細ドキュメント →](./daily-news/SKILL.md)

---

### 🎬 video-downloader

yt-dlp を使用して YouTube、Bilibili、Twitter など1000以上のサイトから動画・音声・字幕をダウンロード。

**クイックスタート：**
```bash
/video-downloader
# または：
# "download video" / "下载视频" / "動画ダウンロード"
```

**機能：**
- 🎥 マルチプラットフォーム：YouTube、Bilibili、Twitter など1000以上のサイト
- 🎵 音声抽出：動画から MP3/M4A を抽出
- 📝 字幕：字幕のダウンロードまたは埋め込み
- 🔧 自動インストール：yt-dlp と ffmpeg を自動インストール

[📖 詳細ドキュメント →](./video-downloader/SKILL.md)

---

### 🚀 ship

ワンステップで commit、push、PR 作成。コミットメッセージと詳細な PR 説明（影響分析付き）を自動生成。

**クイックスタート：**
```bash
/ship
# または：
# "ship it" / "提交PR" / "PRを作成"
```

**機能：**
- ⚡ ワンクリックフロー：確認プロンプトなし - "ship" が意図
- 🧠 スマートブランチ：main/master 上なら自動的に feature ブランチを作成
- 📝 自動コミットメッセージ：diff からコンベンショナルなコミットメッセージを生成
- 📋 詳細な PR：概要、ファイル変更テーブル、影響分析、テストプラン
- 📦 ドラフト対応：`--draft` を追加するか「草稿」と言えばドラフト PR に

[📖 詳細ドキュメント →](./ship/SKILL.md)

---

### 📐 code-standards

あらゆる AI コーディングツール向けの汎用コード品質基準を生成。Linus Torvalds の「Good Taste」哲学に基づき、厳格な 5 層コードレビューフレームワークを備えています。

**クイックスタート：**
```bash
/code-standards
# または：
# "setup code standards" / "代码规范" / "コード規約"
```

**機能：**
- 🔍 **自動検出**：プロジェクト内の AI ツールを検出（Claude、Codex、Cursor、Gemini、Copilot、Windsurf、Aider、Cline）
- 🌍 **4 言語対応**：English、简体中文、繁體中文、日本語（自動検出）
- 📋 **5 層コードレビュー**：データ構造 → エッジケース → 複雑度 → 破壊的分析 → 必要性
- 🚫 **アンチパターンリスト**：過剰設計、不要な抽象化、デザインパターンの濫用を拒否

**対応ツール：**
| ツール | 生成ファイル |
|--------|-------------|
| Claude Code | `CLAUDE.md` |
| OpenAI Codex | `AGENTS.md` |
| Cursor | `.cursor/rules/code-standards.mdc` |
| Gemini CLI | `GEMINI.md` |
| GitHub Copilot | `.github/copilot-instructions.md` |
| Windsurf | `.windsurfrules` |
| Aider | `CONVENTIONS.md` |
| Cline / Roo Code | `.clinerules/code-standards.md` |

[📖 詳細ドキュメント →](./code-standards/SKILL.md)

## 📦 インストール

### ワンコマンドインストール（推奨）

[skills.sh](https://skills.sh/) エコシステムの方式で、一つのコマンドで全スキルをインストール。インストール済みの AI ツールを自動検出し、正しいディレクトリにスキルを配置します：

```bash
npx skills add qiaoshouqing/Skills
```

個別のスキルをインストール：

```bash
npx skills add qiaoshouqing/Skills --skill env-sync
```

### 手動インストール

手動で管理したい場合（Claude Code の例）：

```bash
# リポジトリをクローン
git clone git@github.com:qiaoshouqing/Skills.git ~/claude-skills

# シンボリックリンクで全スキルをインストール
cd ~/claude-skills
for skill in */SKILL.md; do
  skill_name=$(dirname "$skill")
  ln -sf "$(pwd)/$skill_name" ~/.claude/skills/
done
```

個別のスキルをインストール：

```bash
ln -sf ~/claude-skills/env-sync ~/.claude/skills/env-sync
```

> **注意：** ツールごとにスキルディレクトリが異なります。`npx skills add` は自動的に処理します。他のツールへの手動インストールは各ドキュメントを参照してください。

### インストールの確認

```bash
# Claude Code を起動してテスト
cc
> /env-sync --help
```

## 🚀 ロードマップ

- [x] **ship** - ワンクリックで commit、push、PR 作成
- [x] **code-standards** - 汎用コード品質基準ジェネレーター（マルチツール・多言語対応）
- [ ] **test-runner** - 変更に基づくスマートテスト実行
- [ ] **code-review** - 自動コードレビューチェックリスト
- [ ] **docker-helper** - Docker コンテナ管理ユーティリティ
- [ ] **api-tester** - クイック API エンドポイントテスト
- [ ] **db-query** - 一般的なデータベース操作ヘルパー

アイデアがありますか？[Issue を作成](https://github.com/qiaoshouqing/Skills/issues)して新しいスキルを提案してください！

## ❓ FAQ

<details>
<summary><strong>スキルはどこに保存されますか？</strong></summary>

スキルはデフォルトで `~/.claude/skills/` に保存されます。各スキルは最低限 `SKILL.md` ファイルを含むディレクトリです。
</details>

<details>
<summary><strong>スキルの呼び出し方は？</strong></summary>

スキルは複数の方法でトリガーできます：
1. `/` プレフィックスを使用：`/skill-name`
2. 自然言語："sync env"、"同步 env"
3. 自動トリガー：特定のシナリオで自動的にアクティブ化（例：.env がない場合）
</details>

<details>
<summary><strong>既存のスキルを変更できますか？</strong></summary>

はい！シンボリックリンクでインストールした場合：
1. `~/claude-skills/skill-name/SKILL.md` を編集
2. 変更は即座に反映（再起動不要）
3. Pull Request で貢献も可能
</details>

<details>
<summary><strong>スキルとコマンドの違いは？</strong></summary>

- **スキル**：Claude のコンテキストにロードされる再利用可能なプロンプト/ワークフロー
- **コマンド**：直接実行されるシステムレベルの CLI コマンド
- スキルはガイダンスを提供、コマンドはアクションを実行
</details>

<details>
<summary><strong>スキルは特定のプログラミング言語に限定されますか？</strong></summary>

いいえ！スキルはどのプログラミング言語でも動作します。Claude があなたの具体的なコンテキストに適用するガイダンスを提供します。
</details>

## 🤝 コントリビュート

コントリビューションを歓迎します！これは様々な開発ワークフローをカバーすることを目指す、成長中のスキルコレクションです。

### コントリビュート方法

1. **このリポジトリを Fork**
2. **新しいスキルを作成**（以下の構造に従う）
3. **十分にテスト**
4. **Pull Request を提出**（明確な説明を添えて）

### スキル構造

各スキルは以下の構造に従う必要があります：

```
skill-name/
├── SKILL.md          # メインスキル定義（必須）
├── references/       # 詳細ドキュメント（オプション）
├── examples/         # コード例（オプション）
└── scripts/          # ユーティリティスクリプト（オプション）
```

### コントリビューションガイドライン

- スキルが十分に文書化・テストされていることを確認
- 既存のコードスタイルと構造に従う
- Pull Request ごとに1つのスキル
- 期待される動作の例を含める
- コードレビュー中のフィードバックに積極的に対応

## 🐛 トラブルシューティング

**スキルがロードされない場合：**
```bash
# スキルディレクトリの存在確認
ls -la ~/.claude/skills/

# シンボリックリンクの確認
ls -la ~/.claude/skills/env-sync

# 再インストール
rm ~/.claude/skills/env-sync
ln -sf ~/claude-skills/env-sync ~/.claude/skills/env-sync
```

**スキルがトリガーされない場合：**
- SKILL.md の `description` フィールドにトリガーフレーズが含まれているか確認
- 記載されている正確なトリガーフレーズを試す
- `/skill-name` で手動呼び出し

## 📋 動作要件

- **互換性のある AI ツール** - Claude Code、Codex、Gemini CLI、Cursor、VS Code、Amp、TRAE など
- **Node.js**（オプション）- `npx skills add` ワンコマンドインストールに必要
- **Git**（オプション）- git clone でのインストールに必要

**対応プラットフォーム：**
- macOS（テスト済み）
- Linux（動作するはず）
- Windows WSL（動作するはず）

## 📄 ライセンス

MIT License - 詳細は [LICENSE](./LICENSE) ファイルを参照。

## 👤 作者

**qiaoshouqing**
- GitHub: [@qiaoshouqing](https://github.com/qiaoshouqing)

## 💬 サポート

- **Issues**: [GitHub Issues](https://github.com/qiaoshouqing/Skills/issues)
- **Discussions**: [GitHub Discussions](https://github.com/qiaoshouqing/Skills/discussions)
- **Email**: 1143878969@qq.com

---

**Made with ❤️ by the community**

このスキルが役に立ったと思ったら：
- ⭐ このリポジトリにスターを付ける
- 🐛 バグを報告する
- 💡 新しいスキルを提案する
- 🤝 あなたのスキルを貢献する
