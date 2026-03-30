---
name: comfyui-workflow-node-dev
description: Develop, refactor, and debug ComfyUI workflows and custom nodes, especially when Codex must preserve upstream workflow structure, redesign App mode inputs, fix COMBO or upload schema issues, inspect `/object_info`, separate stale Desktop backends from fresh API servers, or verify execution with `/prompt` smoke runs.
---

# ComfyUI Workflow Node Dev

## Start Here

- Identify the active layer before editing anything: workflow JSON, custom node Python, App mode metadata, backend schema, or runtime execution.
- Read [references/design-patterns.md](./references/design-patterns.md) when the task involves workflow rewrites, custom-node surface design, input modeling, or shareable sample workflows.
- Read [references/app-mode-schema.md](./references/app-mode-schema.md) when the task involves App mode, `extra.linearData`, widget exposure, COMBO definitions, upload widgets, `/object_info`, or stale backend symptoms.
- Read [references/validation-and-ops.md](./references/validation-and-ops.md) when the task needs runtime verification, `/prompt` smoke coverage, Desktop-versus-fresh backend diagnosis, Windows local development tips, or release-ready evidence.

## Build Context Before Editing

- Preserve an untouched backup of the upstream workflow JSON and keep stage-by-stage snapshots when iterating.
- Decide early whether the task should be solved by restructuring the workflow itself or by adding a helper custom node. Do not hide major workflow drift behind a compatibility shim unless backward compatibility is the explicit goal.
- Map every user-facing input to the right interaction model before editing: folder selector, upload widget, numeric widget, seed widget, or internal linked value.
- Separate what must be validated in clean-room API runs from what must be verified against the user's current Desktop runtime.

## Follow These Guardrails

- Prefer a native public node surface once the canonical node names, categories, and widget labels are clear.
- Prefer folder selectors for variable-size image sets and upload widgets for natural single-file inputs such as source audio.
- Load long audio once and slice segments downstream instead of reloading per segment.
- Keep public sample workflows shareable and blank by default. Inject machine-local assets only during automated smoke runs.
- Separate a lightweight smoke workflow from a heavy production workflow whenever the full inference path is expensive.
- Use `uv run` for Python-based checks, helpers, and verification scripts.

## Verify Before Closing

1. Run the smallest applicable unit or helper-level checks first.
2. Validate static workflow structure, required inputs, and layout assumptions.
3. Validate backend contract truth with `/object_info`.
4. Run a real `/prompt` smoke path for runtime-sensitive changes.
5. Spot-check the actual Desktop or App mode UI when the user-facing runtime matters.

- Do not call a ComfyUI workflow or custom node "working" if the task depends on runtime behavior and has not been exercised through step 4.
- Record concrete evidence such as commands, `prompt_id`, uploaded sample assets, output files, and anything still unverified.

## Resources

- [references/design-patterns.md](./references/design-patterns.md): workflow structure, input-model decisions, custom-node surface rules, sample-workflow patterns
- [references/app-mode-schema.md](./references/app-mode-schema.md): App mode metadata, widget-backed inputs, COMBO schema, `/object_info`, stale backend diagnosis
- [references/validation-and-ops.md](./references/validation-and-ops.md): validation ladder, `/prompt` smoke expectations, Windows/Desktop runtime operations, evidence checklist
