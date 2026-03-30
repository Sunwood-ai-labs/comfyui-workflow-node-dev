# App Mode And Schema

## App Mode Fundamentals

- App mode depends on workflow metadata, not only graph shape.
- Set `extra.linearMode = true` when the workflow should render as an app-style flow.
- Expose user-facing widgets through `extra.linearData.inputs` and outputs through `extra.linearData.outputs`.
- Do not assume a node becomes visible in App mode merely because it exists in the graph.

## Only Expose Widget-Backed Inputs

- App mode is for widget-backed inputs, not raw linked ports.
- Before exposing an input, confirm it maps to a real widget or `widgets_values` entry.
- Keep the names used in `linearData.inputs` aligned with the actual widget names on the node.
- If the input exists only as a link target, redesign the node or the workflow instead of forcing it into App mode.

## Use Explicit COMBO Definitions

- Prefer the explicit COMBO form when an input has selectable options or upload-related metadata.

```python
{"audio": ("COMBO", {"options": files, "audio_upload": True})}
{"directory": ("COMBO", {"options": directories})}
```

- Avoid the older shorthand tuple form when App mode or upload metadata must survive into the backend schema.
- Treat `/object_info` as the source of truth for whether the backend is publishing the intended metadata.

## Inspect Backend Truth Before Trusting The UI

Use checks like these in PowerShell:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/object_info/LTXLoadAudioUpload
Invoke-RestMethod http://127.0.0.1:8000/object_info/LTXLoadImages
```

Expect upload-capable COMBO inputs to surface metadata in the returned schema, not only in local Python code.

## Diagnose Stale Backend Symptoms

Suspect a stale Desktop backend when any of the following happen:

- the workflow JSON is updated but the App mode UI still shows the old widget type
- a fresh backend and the Desktop backend disagree about option lists or upload widgets
- `Value not in list` errors refer to old values that should no longer exist
- `/prompt` smoke succeeds elsewhere but the Desktop runtime still behaves like the old schema

## Separate Fresh Backend Checks From Desktop Checks

- Use a fresh backend to confirm the repository's true current state.
- Use the active Desktop backend to confirm the user's visible runtime state.
- Do not collapse those into one conclusion; they answer different questions.
