---
title: Release Notes v0.1.0
description: ComfyUI Workflow Node Dev の最初の公開リリースです。
---

# Release Notes v0.1.0

![Release header for v0.1.0](/release-header-v0.1.0.png)

公開日: 2026年3月30日

`v0.1.0` は `comfyui-workflow-node-dev` の最初の公開リリースです。比較対象になる
前タグはないため、このノートは `9eb5a0d6f1d50ef5bc2caeb8e9f4545392e170a3` までの
履歴全体を対象にしています。

## Docs Mirror

- [What's New in v0.1.0](/ja/guide/whats-new-v0.1.0)
- [Repository README](https://github.com/Sunwood-ai-labs/comfyui-workflow-node-dev/blob/main/README.md)
- [実例リポジトリ: ComfyUI-LTXLongAudio](https://github.com/Sunwood-ai-labs/ComfyUI-LTXLongAudio)

## Highlights

- ComfyUI の workflow JSON、custom node、App mode metadata、schema inspection、
  `/prompt` ベースの検証までを扱う公開 Codex skill リポジトリとして立ち上がります。
- skill ガイドをリポジトリと公開サイトの両方から辿れるよう、日英 VitePress docs を
  まとめて公開します。
- 実運用の事例として
  [ComfyUI-LTXLongAudio](https://github.com/Sunwood-ai-labs/ComfyUI-LTXLongAudio) を
  含め、この運用が公開 ComfyUI リポジトリと docs 配信まで到達していることを示します。

## Tooling And Automation

- `.github/workflows/ci.yml` と `.github/workflows/deploy-docs.yml` を含み、同じ
  ソースツリーから検証と GitHub Pages 配信まで進められます。
- `scripts/check_workflow_layout.py` を含み、
  `uv run python scripts/check_workflow_layout.py` で軽量な静的チェックを回せます。
- JavaScript runtime 更新に合わせて workflow を調整済みです。なお一部の
  marketplace action は upstream 側の Node 20 deprecation warning をまだ出す場合が
  ありますが、現在の pin 方針では workflow 自体は成功します。

## Docs And Assets

- `README.md`、`README.ja.md`、`docs/index.md`、`docs/ja/index.md` を通じて
  repository-facing docs を公開します。
- `docs/public/logo.svg`、`docs/public/ogp.svg`、`docs/public/ogp.png`、
  `docs/public/favicon.svg`、そしてこの release header を含む公開アセットを同梱します。

## Steady-State Docs Sync

- `README.md`、`README.ja.md`、docs ホーム、VitePress navigation を release 導線として
  点検しました。
- GitHub と公開 docs の両方から最初のリリースを辿れるよう、versioned な release note
  と walkthrough ページを追加しました。

## Validation

- `npm install`
- `npm run docs:build`
- `uv run python scripts/check_workflow_layout.py --workflow tmp/release-smoke-workflow.json`
- `powershell -ExecutionPolicy Bypass -File D:\Prj\gh-release-notes-skill\scripts\verify-svg-assets.ps1 -RepoPath . -Path docs/public/logo.svg,docs/public/release-header-v0.1.0.svg`

## Upgrade Notes

初回公開リリースのため、既存タグからの upgrade 手順はありません。
