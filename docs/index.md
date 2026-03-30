---
layout: home

hero:
  name: "ComfyUI Workflow Node Dev"
  text: "Build ComfyUI workflows with schema truth and runtime evidence."
  tagline: "A Codex skill for workflow JSON, custom nodes, App mode metadata, /object_info checks, and /prompt smoke runs."
  image:
    src: /logo.svg
    alt: ComfyUI Workflow Node Dev
  actions:
    - theme: brand
      text: Getting Started
      link: /guide/getting-started
    - theme: alt
      text: Japanese Docs
      link: /ja/
    - theme: alt
      text: GitHub
      link: https://github.com/Sunwood-ai-labs/comfyui-workflow-node-dev

features:
  - title: Preserve Workflow Intent
    details: Keep upstream structure, stage-by-stage snapshots, and maintainable graph layout in view before introducing helper nodes or compatibility layers.
  - title: Model App Mode Correctly
    details: Expose only widget-backed inputs, validate COMBO metadata against backend truth, and separate stale Desktop symptoms from fresh backend reality.
  - title: Close With Real Evidence
    details: Move from static checks to /object_info, /prompt smoke runs, and Desktop spot checks so runtime-sensitive changes do not stop at theory.
---

## Overview

`comfyui-workflow-node-dev` is built for Codex sessions where ComfyUI work spans more than
one layer at once. Instead of treating workflow JSON, App mode metadata, backend schema,
and runtime execution as separate concerns, the skill keeps them connected.

## Documentation Paths

- [Getting Started](/guide/getting-started)
- [Workflow Design](/guide/workflow-design)
- [App Mode and Schema](/guide/app-mode-and-schema)
- [Validation and Operations](/guide/validation-and-ops)

## Best Fit

- workflow refactors that must preserve upstream intent
- custom node work that needs a clear public-facing surface
- App mode redesigns involving widget exposure or upload-capable COMBO inputs
- debugging sessions where stale Desktop state and fresh backend state disagree
- tasks that require proof through `/prompt` instead of static reasoning alone
