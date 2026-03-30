---
title: What's New in v0.1.0
description: Walkthrough of the first public release for ComfyUI Workflow Node Dev.
---

# What's New in v0.1.0

![Release header for v0.1.0](/release-header-v0.1.0.png)

Released on March 30, 2026.

The first public release turns `comfyui-workflow-node-dev` from an internal working
repository into a reusable public skill package. The main idea is simple: keep workflow
JSON edits, App mode metadata, backend schema truth, and runtime evidence in one operating
loop instead of treating them as separate cleanup tasks.

## What Shipped

- A focused skill definition in `SKILL.md` and an OpenAI agent descriptor in
  `agents/openai.yaml`
- Bilingual docs covering getting started, workflow design, App mode and schema work, and
  validation operations
- CI and GitHub Pages delivery so the docs surface stays publishable
- A workflow layout checker script that fits the repository guidance around `uv run`

## Why This Release Matters

ComfyUI work often becomes fragile when the visible UI, App mode exposure, and runtime
truth drift apart. This release packages the operating pattern that keeps those layers in
sync, so Codex can make changes more like a maintainer than a blind editor.

## Case Study

The repository already has a concrete public example:
[ComfyUI-LTXLongAudio](https://github.com/Sunwood-ai-labs/ComfyUI-LTXLongAudio).
That project shows the skill can support a real custom-node repository and published docs,
not just theory.

## Validation Footprint

- The docs build locally with `npm run docs:build`
- Static workflow checks can be exercised with `uv run python scripts/check_workflow_layout.py`
- GitHub Actions are set up to validate the repository and publish the docs site

## Known Caveat

Some marketplace-hosted GitHub actions still surface Node 20 deprecation warnings upstream.
The repository workflows have already been adjusted to the current runtime strategy, so the
warning is worth watching but is not a release blocker for `v0.1.0`.
