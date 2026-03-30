# App Mode And Schema

## App Mode Fundamentals

App mode depends on workflow metadata, not only graph shape. When a workflow should render
as an app-style flow:

- set `extra.linearMode = true`
- expose user-facing widgets through `extra.linearData.inputs`
- expose outputs through `extra.linearData.outputs`
- do not assume a node becomes visible in App mode only because it exists in the graph

## Expose Only Widget-Backed Inputs

App mode is for widget-backed inputs, not raw linked ports.

- confirm each exposed field maps to a real widget or `widgets_values` entry
- keep `linearData.inputs` names aligned with actual widget names
- redesign the node or workflow if the input exists only as a linked port target

## Use Explicit COMBO Definitions

When inputs have selectable options or upload-related metadata, prefer the explicit COMBO
shape so backend schema stays truthful:

```python
{"audio": ("COMBO", {"options": files, "audio_upload": True})}
{"directory": ("COMBO", {"options": directories})}
```

## Inspect Backend Truth Before Trusting The UI

Use `/object_info` to confirm what the backend is really publishing:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/object_info/LTXLoadAudioUpload
Invoke-RestMethod http://127.0.0.1:8000/object_info/LTXLoadImages
```

Expect upload-capable COMBO inputs to surface their metadata in the returned schema.

## Diagnose Stale Backend Symptoms

Suspect a stale Desktop backend when:

- the workflow JSON changed but the App mode UI still shows the old widget type
- a fresh backend and the Desktop backend disagree about option lists or upload widgets
- `Value not in list` errors refer to old values that should no longer exist
- `/prompt` succeeds elsewhere but Desktop still behaves like older schema

## Separate Fresh Backend Checks From Desktop Checks

- use a fresh backend to confirm the repository's true current state
- use the active Desktop backend to confirm the user's visible runtime state
- do not collapse those into one conclusion because they answer different questions
