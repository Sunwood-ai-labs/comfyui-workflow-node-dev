# 検証と運用

## 検証ラダー

変更に必要な深さまで検証しますが、runtime behavior が論点なら浅い段階で止めません。

### Level 1: Unit / Helper Checks

- segment math、index selection、slice helper など純粋ロジックを検証する
- helper コードを早く安定させるために使う

### Level 2: Static Workflow Validation

- workflow JSON を parse する
- node type の存在を確認する
- required input 欠落を検出する
- linked COMBO misuse を検出する
- layout 問題や App mode metadata mismatch を検出する

### Level 3: `object_info` Contract Validation

- option list を確認する
- `audio_upload` や `image_upload` など upload metadata を確認する
- COMBO 構造が frontend の期待に合うか確認する

### Level 4: Real `/prompt` Smoke

- 必要な sample asset をアップロードする
- workflow JSON を backend が受ける prompt payload に変換する
- queue 前に COMBO 値を検証する
- `/history/<prompt_id>` などで完了証跡を待つ
- 意図した output node path まで処理が届くか確認する

### Level 5: Desktop / App Mode Spot Check

- ユーザーが実際に見る UI を確認する
- 公開 input が workflow 意図と合うか確認する
- stale backend が最新 state を隠していないか確認する

## Smoke Workflow のルール

- heavy な production graph より軽い smoke workflow を用意する
- smoke workflow で node contract、App mode exposure、upload、queue 実行を確認する
- production workflow は検証コスト最小化より user-facing result を優先する

## Windows / Desktop 運用

- Windows では `ComfyUI/custom_nodes` への junction が反復開発を速くする
- backend port を握っている process を確認してから現在 state を信じる
- stale schema が疑わしいときは ComfyUI Desktop を完全終了する
- Desktop ComfyUI は frontend と backend server の組み合わせとして扱う

## 残すべき証跡

- 実行した正確な command
- test や checker の結果
- `/prompt` smoke の `prompt_id`
- 使用した sample asset
- output file や history evidence
- 未検証項目とその理由

## 例コマンド

```powershell
uv run pytest -q
uv run python scripts/check_workflow_layout.py --workflow path/to/workflow.json
Invoke-RestMethod http://127.0.0.1:8000/object_info/LTXLoadAudioUpload
Invoke-RestMethod http://127.0.0.1:8000/history/<prompt_id>
Get-NetTCPConnection -LocalPort 8000 | Select-Object LocalPort, State, OwningProcess
```
