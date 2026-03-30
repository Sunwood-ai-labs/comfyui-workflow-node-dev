# Validation And Operations

## Validation Ladder

Apply the deepest level needed by the change, but do not stop early when runtime behavior
is in scope.

### Level 1: Unit Or Helper Checks

- validate segment math, index selection, slicing helpers, or other pure logic
- use these checks to stabilize helper code quickly

### Level 2: Static Workflow Validation

- parse workflow JSON
- validate node type existence
- detect missing required inputs
- detect linked COMBO misuse
- detect layout problems or App mode metadata mismatches

### Level 3: `object_info` Contract Validation

- confirm option lists
- confirm upload metadata such as `audio_upload` or `image_upload`
- confirm COMBO structure matches frontend expectations

### Level 4: Real `/prompt` Smoke

- upload representative sample assets when needed
- convert workflow JSON into a prompt payload the backend accepts
- validate COMBO values before queueing
- wait for `/history/<prompt_id>` or similar completion evidence
- confirm execution reaches the intended output node path

### Level 5: Desktop Or App Mode Spot Check

- inspect the UI the user actually sees
- confirm the published inputs match the workflow intent
- confirm a stale backend is not masking the latest repository state

## Smoke Workflow Rules

- keep smoke workflows lighter than the full production graph when inference is expensive
- use smoke workflows to validate node contracts, App mode exposure, uploads, and queue execution
- keep production workflows focused on the user-facing result, not on verification cost

## Windows And Desktop Operations

- a junction into `ComfyUI/custom_nodes` can speed up local iteration on Windows
- confirm which process owns the backend port before trusting current state
- fully close ComfyUI Desktop when stale schema is suspected
- treat Desktop ComfyUI as a frontend plus backend server, not one opaque box

## Evidence To Leave Behind

- exact commands that were run
- test or checker results
- `prompt_id` values for `/prompt` smoke runs
- sample assets used during validation
- output files or history evidence
- anything still unverified and why

## Example Commands

```powershell
uv run pytest -q
uv run python scripts/check_workflow_layout.py --workflow path/to/workflow.json
Invoke-RestMethod http://127.0.0.1:8000/object_info/LTXLoadAudioUpload
Invoke-RestMethod http://127.0.0.1:8000/history/<prompt_id>
Get-NetTCPConnection -LocalPort 8000 | Select-Object LocalPort, State, OwningProcess
```
