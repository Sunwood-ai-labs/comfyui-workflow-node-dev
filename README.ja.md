<div align="center">
  <h1>ComfyUI Workflow Node Dev</h1>
  <img src="./docs/public/logo.svg" alt="ComfyUI Workflow Node Dev" width="220">
  <p>
    <img src="https://img.shields.io/badge/Codex-Skill-0F766E" alt="Codex Skill">
    <img src="https://img.shields.io/badge/ComfyUI-Workflow%20%2B%20Custom%20Nodes-164E63" alt="ComfyUI">
    <img src="https://img.shields.io/badge/VitePress-Docs-0F172A?logo=vitepress&logoColor=white" alt="VitePress">
    <img src="https://img.shields.io/badge/GitHub%20Pages-CI%2FCD-1D4ED8?logo=githubpages&logoColor=white" alt="GitHub Pages">
    <img src="https://img.shields.io/badge/Bilingual-English%20%2B%20Japanese-475569" alt="Bilingual">
  </p>
  <p>
    <a href="./README.md">English</a> |
    <strong lang="ja">日本語</strong>
  </p>
</div>

ComfyUI の workflow JSON と custom node を扱うときに、App mode、バックエンドの
schema 真実、実ランタイム検証をずらさず進めるための Codex skill です。workflow の
構造変更、custom node の公開面設計、`/object_info` 検証、`/prompt` スモーク確認まで
を一つの流れで扱います。

## 概要

`comfyui-workflow-node-dev` は、Codex が単にコードを直すだけではなく、ComfyUI の
保守者として安全に進めるためのガイドをまとめたリポジトリです。workflow グラフ、
App mode メタデータ、バックエンド schema、実行証跡をつなげて、ユーザーに見える面の
変更でも根拠を持って判断できるようにします。

このリポジトリには次の内容があります。

- スキル本体の定義: [`SKILL.md`](./SKILL.md)
- OpenAI エージェント定義: [`agents/openai.yaml`](./agents/openai.yaml)
- 設計・App mode・検証運用の参照資料: [`references/`](./references/)
- 同じ内容を見やすく参照できる日英 VitePress docs

## 実例リポジトリ

この運用で実際に形にできた事例として
[ComfyUI-LTXLongAudio](https://github.com/Sunwood-ai-labs/ComfyUI-LTXLongAudio)
があります。これは ComfyUI 向けの long-audio workflow を支える native LTX custom
nodes をまとめた公開リポジトリで、公開 docs は
[sunwood-ai-labs.github.io/ComfyUI-LTXLongAudio](https://sunwood-ai-labs.github.io/ComfyUI-LTXLongAudio/)
で確認できます。

## クイックスタート

1. まず対象レイヤーを切り分けます。
   workflow JSON、custom node Python、App mode metadata、backend schema、runtime
   execution のどこが主戦場かを先に決めます。
2. 対応する資料を読みます。
   [`design-patterns.md`](./references/design-patterns.md)、
   [`app-mode-schema.md`](./references/app-mode-schema.md)、
   [`validation-and-ops.md`](./references/validation-and-ops.md) を使い分けます。
3. Codex では次のように呼び出します。

```text
Use $comfyui-workflow-node-dev to extend or debug this ComfyUI workflow or custom node,
then validate schema, App mode, and /prompt execution.
```

4. 検証は浅いところから順に進めます。
   静的確認、`/object_info`、実 `/prompt`、必要なら Desktop/App mode の目視確認まで
   段階的に進めます。

## この Skill が扱うこと

- 大きな workflow 変更前の upstream バックアップ保持
- workflow の再構成と helper custom node 追加の判断
- App mode に合う入力モデルの選定
- widget-backed な `extra.linearData` 入出力の設計
- COMBO metadata と `/object_info` の突き合わせ
- stale な Desktop backend と fresh API backend の切り分け
- 実行コマンド、`prompt_id`、使用アセット、出力物といった証跡の整理
- Python ベースの補助や検証で `uv run` を使う運用

## 作業原則

- 大きく触る前に upstream の素のバックアップと途中スナップショットを残します。
- canonical な node 名やカテゴリが固まったら native public node surface を優先します。
- 可変枚数の画像は folder selector、自然な単一ファイル入力は upload widget を優先します。
- ランタイム依存の変更は、実 `/prompt` を通してから初めて「動く」と判断します。
- stale schema の疑いがあるときは Desktop と fresh backend を別々に観測します。

## リポジトリ構成

```text
comfyui-workflow-node-dev/
|- SKILL.md
|- README.md
|- README.ja.md
|- LICENSE
|- agents/
|  `- openai.yaml
|- references/
|  |- app-mode-schema.md
|  |- design-patterns.md
|  `- validation-and-ops.md
|- docs/
|  |- .vitepress/
|  |- guide/
|  |- ja/
|  `- public/
`- .github/workflows/
```

## ドキュメント

- 英語 docs ソース: [`docs/index.md`](./docs/index.md)
- 日本語 docs ソース: [`docs/ja/index.md`](./docs/ja/index.md)
- ローカルプレビュー:

```bash
cd docs
npm install
npm run docs:dev
```

同じソースから CI と GitHub Pages 配信まで進められるように workflow も同梱しています。

## 参照マップ

- [`references/design-patterns.md`](./references/design-patterns.md):
  workflow 構造、入力モデル、公開 node surface、共有用サンプル
- [`references/app-mode-schema.md`](./references/app-mode-schema.md):
  App mode metadata、widget-backed inputs、COMBO 定義、`/object_info`、stale backend 診断
- [`references/validation-and-ops.md`](./references/validation-and-ops.md):
  検証ラダー、`/prompt` スモーク、Windows/Desktop 運用、証跡チェックリスト

## 現時点の制約

このリポジトリは運用パターンと検証方針を文書化したものです。example workflow JSON、
sample custom node、smoke fixture、互換性マトリクス、`prompt_id` 履歴のような実行証跡は
まだ同梱していません。

## メモ

- Python 実行が必要なときは `uv run` を使います。
- 共有用 workflow は空のまま保ち、ローカル依存アセットは smoke 検証時だけ注入します。
- ランタイム依存の修正では、理論上の説明だけでなく実証跡を残します。
