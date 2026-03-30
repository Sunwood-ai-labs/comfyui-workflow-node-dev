# Workflow 設計

## まず Baseline を守る

workflow 変更は元構造を見失うと危険になります。大きく触る前に:

- upstream の素の backup を保存する
- 構造変更ごとに milestone snapshot を残す
- helper node を足す前に upstream graph と比較する
- compatibility shim と native rewrite を別トラックとして扱う

## 入力モデルは先に決める

公開面はユーザーの mental model に合わせるのが重要です。

- 可変枚数の画像を扱うなら folder selector
- 単一ファイルを自然に差し替えるなら upload widget
- 本質が「集合から選ぶ」なら固定個数の upload slot を増やしすぎない
- ユーザーが一文で説明できるモデルを選ぶ

## Native Public Node Surface を優先する

canonical な node 名、カテゴリ、widget label が固まったら:

- sample workflow をその surface に統一する
- 旧互換レイヤーは明示的に隔離する
- convenience wrapper で大きな drift を隠さない

## Shareable Sample Workflow を保つ

- 公開向け workflow に machine-local path を埋め込まない
- 共有用サンプルの default は空にする
- sample asset の注入は automated smoke run のときだけ行う
- 重い production graph と軽い smoke workflow を分ける

## Layout も保守性

読みやすい graph は調査速度に直結します。次を監視します。

- group や node の重なり
- title band の衝突
- group からはみ出した node
- 実 widget 配置と App mode metadata のズレ

## リリース前チェック

- App mode の入力モデルを docs に説明する
- install / clone 手順を短く保つ
- 共有しやすく自動検証しやすい sample workflow を出す
