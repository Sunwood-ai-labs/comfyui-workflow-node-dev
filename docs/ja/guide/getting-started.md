# はじめに

## この Skill が重視すること

`comfyui-workflow-node-dev` は、ComfyUI の変更を実ランタイムに根ざして進めるための
ガイドです。特に次のレイヤーが絡むタスクで力を発揮します。

- workflow JSON 構造
- custom node Python
- `extra.linearData` を含む App mode metadata
- backend schema と `/object_info`
- `/prompt` による runtime execution

## 最初に決めること

編集前に、いまの主戦場をはっきりさせます。

1. workflow JSON
2. custom node 実装
3. App mode metadata
4. backend schema
5. runtime execution

これを先に決めると、UI の症状と本当の原因を取り違えにくくなります。

## どの資料を読むか

- workflow の再構成、input model、共有用 sample workflow なら
  `references/design-patterns.md`
- App mode、`extra.linearData`、COMBO、upload widget、`/object_info` なら
  `references/app-mode-schema.md`
- 検証ラダー、`/prompt`、Windows/Desktop 運用、証跡整理なら
  `references/validation-and-ops.md`

## 基本ループ

1. baseline を保護する
2. 入力モデルを先に決める
3. backend contract の真実を確認する
4. runtime-sensitive な変更は実スモークを通す
5. 説明だけでなく実証跡を残す

## 呼び出し例

```text
Use $comfyui-workflow-node-dev to extend or debug this ComfyUI workflow or custom node,
then validate schema, App mode, and /prompt execution.
```

## 実務上のデフォルト

- upstream backup と milestone snapshot を残す
- Python ベースの補助や検証は `uv run` を使う
- 共有用 workflow は空のまま保つ
- 重い production graph とは別に軽い smoke workflow を用意する

## 現時点の制約

このリポジトリはガイド中心で、bundled workflow example、smoke fixture、
runtime artifact はまだ同梱していません。
