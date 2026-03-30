<div align="center">
  <h1>ComfyUI Workflow Node Dev</h1>
  <img src="./docs/public/logo.svg" alt="ComfyUI Workflow Node Dev" width="220">
  <p>
    <img src="https://img.shields.io/badge/Codex-Skill-0F766E" alt="Codex Skill">
    <img src="https://img.shields.io/badge/ComfyUI-Workflow%20%2B%20Custom%20Nodes-164E63" alt="ComfyUI">
    <img src="https://img.shields.io/badge/VitePress-Docs-0F172A?logo=vitepress&logoColor=white" alt="VitePress">
    <img src="https://img.shields.io/badge/GitHub%20Pages-CI%2FCD-1D4ED8?logo=githubpages&logoColor=white" alt="GitHub Pages">
    <img src="https://img.shields.io/badge/Bilingual-English%20%2B%20Japanese-475569" alt="Bilingual">
  </p>
  <p>
    <strong>English</strong> |
    <a href="./README.ja.md" lang="ja">日本語</a>
  </p>
</div>

Build, refactor, and debug ComfyUI workflows and custom nodes while keeping App mode,
backend schema truth, and runtime validation aligned. This Codex skill is designed for
workflow JSON edits, custom node surface design, App mode exposure, `/object_info`
inspection, and `/prompt` smoke verification.

## Overview

`comfyui-workflow-node-dev` helps Codex work like a careful ComfyUI maintainer instead of
only a code editor. It keeps the workflow graph, App mode metadata, backend schema, and
runtime evidence in one loop so user-facing changes stay trustworthy.

The repository packages:

- a focused skill definition in [`SKILL.md`](./SKILL.md)
- an OpenAI agent descriptor in [`agents/openai.yaml`](./agents/openai.yaml)
- reference guides for workflow design, App mode schema, and validation under
  [`references/`](./references/)
- bilingual VitePress docs for browsing the same guidance as a site

## Example Repository

A practical example already delivered with this workflow is
[ComfyUI-LTXLongAudio](https://github.com/Sunwood-ai-labs/ComfyUI-LTXLongAudio),
a public repository for native LTX custom nodes for long-audio workflows in ComfyUI.
Its published docs are also available at
[sunwood-ai-labs.github.io/ComfyUI-LTXLongAudio](https://sunwood-ai-labs.github.io/ComfyUI-LTXLongAudio/).

## Quick Start

1. Identify the active layer before editing anything:
   workflow JSON, custom node Python, App mode metadata, backend schema, or runtime
   execution.
2. Read the matching reference:
   [`design-patterns.md`](./references/design-patterns.md),
   [`app-mode-schema.md`](./references/app-mode-schema.md), or
   [`validation-and-ops.md`](./references/validation-and-ops.md).
3. Use the skill from Codex:

```text
Use $comfyui-workflow-node-dev to extend or debug this ComfyUI workflow or custom node,
then validate schema, App mode, and /prompt execution.
```

4. Verify with the smallest valid ladder:
   static checks first, then `/object_info`, then real `/prompt`, then Desktop/App mode
   spot checks when the user-facing runtime matters.

## What This Skill Covers

- preserving upstream workflow structure before refactors
- deciding between workflow rewrites and helper custom nodes
- choosing the right input model for App mode surfaces
- using widget-backed `extra.linearData` inputs and outputs safely
- validating COMBO metadata against `/object_info`
- separating stale Desktop backends from fresh API truth
- collecting runtime evidence such as commands, `prompt_id`, assets, and outputs
- preferring `uv run` for Python-based helpers and validation commands

## Working Principles

- Keep a clean upstream backup and milestone snapshots before major workflow changes.
- Prefer a native public node surface when canonical names and categories are known.
- Use folder selectors for variable-size image sets and upload widgets for natural
  single-file inputs.
- Do not call runtime-sensitive changes "working" until they have been exercised through
  a real `/prompt` smoke path.
- Treat Desktop ComfyUI and a fresh backend as separate sources of truth when debugging
  stale schema symptoms.

## Repository Layout

```text
comfyui-workflow-node-dev/
|- SKILL.md
|- README.md
|- README.ja.md
|- LICENSE
|- agents/
|  `- openai.yaml
|- references/
|  |- app-mode-schema.md
|  |- design-patterns.md
|  `- validation-and-ops.md
|- docs/
|  |- .vitepress/
|  |- guide/
|  |- ja/
|  `- public/
`- .github/workflows/
```

## Documentation

- English docs source: [`docs/index.md`](./docs/index.md)
- Japanese docs source: [`docs/ja/index.md`](./docs/ja/index.md)
- Local preview:

```bash
cd docs
npm install
npm run docs:dev
```

The repository also includes CI and GitHub Pages workflows so the docs site can be built
and published from the same source tree.

## Reference Map

- [`references/design-patterns.md`](./references/design-patterns.md):
  workflow structure, input-model choices, native public node surfaces, shareable samples
- [`references/app-mode-schema.md`](./references/app-mode-schema.md):
  App mode metadata, widget-backed inputs, COMBO definitions, `/object_info`, stale
  backend diagnosis
- [`references/validation-and-ops.md`](./references/validation-and-ops.md):
  validation ladder, `/prompt` smoke runs, Windows/Desktop operations, evidence checklists

## Current Boundaries

The current repository documents operating patterns and validation doctrine. It does not yet
ship example workflow JSON files, sample custom nodes, smoke fixtures, compatibility tables,
or captured runtime evidence such as example `prompt_id` histories.

## Notes

- Use `uv run` when Python execution is involved.
- Keep shareable sample workflows blank by default and inject machine-local assets only
  for smoke validation.
- If a task depends on runtime behavior, leave concrete evidence behind instead of only
  reporting a theoretical fix.
