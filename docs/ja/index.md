---
layout: home

hero:
  name: "ComfyUI Workflow Node Dev"
  text: "ComfyUI workflow を schema 真実と runtime 証跡付きで育てる。"
  tagline: "workflow JSON、custom node、App mode metadata、/object_info、/prompt スモーク検証を一つの流れで扱う Codex skill です。"
  image:
    src: /logo.svg
    alt: ComfyUI Workflow Node Dev
  actions:
    - theme: brand
      text: はじめに
      link: /ja/guide/getting-started
    - theme: alt
      text: English Docs
      link: /
    - theme: alt
      text: GitHub
      link: https://github.com/Sunwood-ai-labs/comfyui-workflow-node-dev

features:
  - title: Workflow の意図を守る
    details: upstream 構造、途中スナップショット、読みやすい graph layout を保ったまま、helper node や再構成の判断を進めます。
  - title: App Mode を正しく設計する
    details: widget-backed input、COMBO metadata、fresh backend と Desktop backend の切り分けを前提に進めます。
  - title: 実証跡で閉じる
    details: 静的確認から /object_info、/prompt、必要なら Desktop 目視確認まで進め、理論だけで終わらせません。
---

## 概要

`comfyui-workflow-node-dev` は、ComfyUI の作業が複数レイヤーにまたがるときに
Codex が迷わないようにするための skill です。workflow JSON、App mode metadata、
backend schema、runtime execution を分断せず扱えるようにします。

## 実例

この運用で実際に公開まで進められた事例として
[ComfyUI-LTXLongAudio](https://github.com/Sunwood-ai-labs/ComfyUI-LTXLongAudio)
があります。これは long-audio workflow 向けの native LTX custom nodes を提供する
ComfyUI リポジトリで、公開 docs は
[sunwood-ai-labs.github.io/ComfyUI-LTXLongAudio](https://sunwood-ai-labs.github.io/ComfyUI-LTXLongAudio/)
から参照できます。

## 最新リリース

最初の公開リリース `v0.1.0` の内容は、次の 2 ページで追えるようにしています。

- [Release Notes v0.1.0](/guide/release-notes-v0.1.0)
- [What's New in v0.1.0](/guide/whats-new-v0.1.0)

## ドキュメント導線

- [はじめに](/ja/guide/getting-started)
- [Workflow 設計](/ja/guide/workflow-design)
- [App Mode と Schema](/ja/guide/app-mode-and-schema)
- [検証と運用](/ja/guide/validation-and-ops)

## 向いている作業

- upstream の意図を崩したくない workflow 改修
- 公開面を整理したい custom node 開発
- widget 公開や upload COMBO を含む App mode 再設計
- stale な Desktop 状態と fresh backend の差分調査
- 静的説明ではなく `/prompt` 実行証跡まで必要なタスク
