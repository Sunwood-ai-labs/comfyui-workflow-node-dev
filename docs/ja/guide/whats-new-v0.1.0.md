---
title: What's New in v0.1.0
description: ComfyUI Workflow Node Dev の初回公開リリースを解説します。
---

# What's New in v0.1.0

![Release header for v0.1.0](/release-header-v0.1.0.png)

公開日: 2026年3月30日

今回の最初の公開リリースでは、`comfyui-workflow-node-dev` を内部の作業用リポジトリ
から、再利用できる公開 skill パッケージへ引き上げました。中心にある考え方は、
workflow JSON、App mode metadata、backend schema の真実、runtime 証跡を別々に
扱わず、一つの運用ループとしてつなぐことです。

## 今回入ったもの

- `SKILL.md` の skill 定義と `agents/openai.yaml` の OpenAI agent descriptor
- はじめに、workflow 設計、App mode と schema、検証運用をまとめた日英 docs
- docs を継続公開できる CI と GitHub Pages の配信導線
- `uv run` 方針に合う workflow layout checker script

## このリリースの意味

ComfyUI の作業は、見えている UI、App mode の公開面、runtime の真実がずれると急に
不安定になります。このリリースは、そのズレを抑えたまま Codex が保守者のように
作業を進めるための運用パターンを、使える形でまとめたものです。

## 事例

すでに具体的な公開事例として
[ComfyUI-LTXLongAudio](https://github.com/Sunwood-ai-labs/ComfyUI-LTXLongAudio)
があります。理論だけでなく、custom node リポジトリと公開 docs の両方を支えられる
ことが分かる事例です。

## Validation Footprint

- docs は `npm run docs:build` でローカル build できます
- static な workflow check は `uv run python scripts/check_workflow_layout.py` で試せます
- GitHub Actions で repository validation と docs publish を回せます

## Known Caveat

一部の marketplace-hosted GitHub action は upstream 由来の Node 20 deprecation
warning をまだ表示します。リポジトリ側の workflow は現行 runtime 方針に合わせて
調整済みなので、`v0.1.0` の release blocker ではありません。
