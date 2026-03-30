# Validation And Ops

## Validation Ladder

Apply the deepest level needed by the change, but do not stop early when runtime behavior is in scope.

### Level 1: Unit Or Helper Checks

- validate segment math, index selection, slicing helpers, or other pure logic
- use these to stabilize custom helper code quickly

### Level 2: Static Workflow Validation

- parse workflow JSON
- validate node type existence
- detect missing required inputs
- detect linked COMBO misuse
- detect layout problems or App mode metadata mismatches

### Level 3: `object_info` Contract Validation

- confirm option lists
- confirm upload metadata such as `audio_upload` or `image_upload`
- confirm COMBO structure matches what the frontend expects

### Level 4: Real `/prompt` Smoke

- upload representative sample assets when the workflow expects uploaded files
- convert the workflow JSON into a prompt payload the backend accepts
- validate COMBO values before queueing
- wait for `/history/<prompt_id>` or equivalent completion evidence
- verify that execution reaches the output node path

### Level 5: Desktop Or App Mode Spot Check

- inspect the visible UI the user actually sees
- confirm the published inputs match the workflow intent
- confirm a stale backend is not masking the latest changes

## Smoke Workflow Rules

- Keep smoke workflows lighter than the full production graph whenever the main inference path is expensive.
- Use smoke workflows to validate node contracts, App mode exposure, uploads, and queue execution.
- Keep production workflows focused on the user-facing result, not on minimizing verification cost.

## Windows And Desktop Operations

- On Windows, linking the repository into `ComfyUI/custom_nodes` with a junction can speed up local iteration.
- Always confirm which process owns the backend port before trusting the current Desktop state.
- Fully close ComfyUI Desktop and verify the backend process is gone when stale schema is suspected.
- Treat Desktop ComfyUI as a frontend plus backend server, not as one opaque black box.

## Evidence To Leave Behind

- exact commands that were run
- test or checker results
- `prompt_id` values for `/prompt` smoke runs
- sample assets used during validation
- output files or history evidence
- anything still unverified and why

## Useful PowerShell Checks

```powershell
uv run pytest -q
uv run python scripts/check_workflow_layout.py --workflow path/to/workflow.json
Invoke-RestMethod http://127.0.0.1:8000/object_info/LTXLoadAudioUpload
Invoke-RestMethod http://127.0.0.1:8000/history/<prompt_id>
Get-NetTCPConnection -LocalPort 8000 | Select-Object LocalPort, State, OwningProcess
```

- Adapt node types and ports to the actual runtime under inspection.
- If a helper script is Python-based, keep it under `uv run` rather than invoking a bare interpreter.

## Recommended Closing Checklist

- Confirm whether the task changed workflow JSON, custom-node code, or both.
- Confirm whether App mode metadata was touched.
- Confirm whether the schema was checked through `/object_info`.
- Confirm whether runtime behavior was checked through `/prompt`.
- Confirm whether the Desktop runtime was spot-checked separately when user-facing UI mattered.
