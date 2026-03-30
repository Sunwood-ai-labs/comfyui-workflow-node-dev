# App Mode と Schema

## App Mode の基本

App mode は graph 形状だけではなく workflow metadata に依存します。app 風の流れとして
見せたいときは:

- `extra.linearMode = true` を設定する
- user-facing widget を `extra.linearData.inputs` に公開する
- 出力を `extra.linearData.outputs` に公開する
- node が graph にあるだけで App mode に見えるとは考えない

## Widget-Backed Input だけを公開する

App mode は raw linked port ではなく widget-backed input のための面です。

- 公開対象が実在する widget または `widgets_values` に対応するか確認する
- `linearData.inputs` の名前を実 widget 名に合わせる
- linked port の受け口でしかないなら node か workflow 側を設計し直す

## COMBO は明示形を使う

選択肢や upload metadata を持つ入力では、backend schema に真実が残る明示形 COMBO を
優先します。

```python
{"audio": ("COMBO", {"options": files, "audio_upload": True})}
{"directory": ("COMBO", {"options": directories})}
```

## UI より先に Backend Truth を見る

実際に backend が何を公開しているかは `/object_info` で確認します。

```powershell
Invoke-RestMethod http://127.0.0.1:8000/object_info/LTXLoadAudioUpload
Invoke-RestMethod http://127.0.0.1:8000/object_info/LTXLoadImages
```

upload 可能な COMBO なら、その metadata が返却 schema に出てくるべきです。

## Stale Backend の症状

次のようなときは stale な Desktop backend を疑います。

- workflow JSON を更新したのに App mode UI が古い widget のまま
- fresh backend と Desktop backend で options や upload widget が食い違う
- `Value not in list` が古い値を参照している
- 別環境では `/prompt` が通るのに Desktop では旧 schema のように振る舞う

## Fresh Backend と Desktop は分けて観測する

- fresh backend は repository の現在真実を確認するために使う
- active Desktop backend はユーザーに見えている状態を確認するために使う
- この二つは別の問いに答えるので、一つの結論に潰してはいけません
