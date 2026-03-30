# Getting Started

## What This Skill Focuses On

`comfyui-workflow-node-dev` helps Codex make ComfyUI changes in a way that stays grounded in
the actual runtime. It is especially useful when a task touches several of these layers:

- workflow JSON structure
- custom node Python
- App mode metadata such as `extra.linearData`
- backend schema and `/object_info`
- runtime execution through `/prompt`

## Start With The Active Layer

Before editing anything, identify which layer is currently authoritative:

1. workflow JSON
2. custom node implementation
3. App mode metadata
4. backend schema
5. runtime execution

This keeps debugging sessions from mixing a UI symptom with the wrong source of truth.

## Which Reference To Read

- Read `references/design-patterns.md` for workflow rewrites, custom-node surface design,
  input modeling, and shareable sample workflows.
- Read `references/app-mode-schema.md` for App mode, `extra.linearData`, COMBO definitions,
  upload widgets, and `/object_info`.
- Read `references/validation-and-ops.md` for the validation ladder, `/prompt` smoke
  expectations, Windows/Desktop tips, and evidence capture.

## Core Operating Loop

1. Preserve the baseline workflow or node surface.
2. Choose the right interaction model before editing.
3. Validate the backend contract truth.
4. Run a real smoke path for runtime-sensitive changes.
5. Leave behind concrete evidence instead of only a narrative summary.

## Example Prompt

```text
Use $comfyui-workflow-node-dev to extend or debug this ComfyUI workflow or custom node,
then validate schema, App mode, and /prompt execution.
```

## Practical Defaults

- Keep upstream backups and milestone snapshots.
- Prefer `uv run` for Python-based helpers and validation commands.
- Keep shareable sample workflows blank by default.
- Use a lighter smoke workflow when the production graph is expensive.

## Current Boundaries

This repository currently ships guidance, not bundled workflow examples, smoke fixtures, or
captured runtime artifacts.
