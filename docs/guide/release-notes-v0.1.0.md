---
title: Release Notes v0.1.0
description: Initial public release of ComfyUI Workflow Node Dev.
---

# Release Notes v0.1.0

![Release header for v0.1.0](/release-header-v0.1.0.png)

Released on March 30, 2026.

`v0.1.0` is the initial public release of `comfyui-workflow-node-dev`. There is no previous
tag for comparison, so this note covers the repository history up to
`9eb5a0d6f1d50ef5bc2caeb8e9f4545392e170a3`.

## Docs Mirror

- [What's New in v0.1.0](/guide/whats-new-v0.1.0)
- [Repository README](https://github.com/Sunwood-ai-labs/comfyui-workflow-node-dev/blob/main/README.md)
- [Example Repository: ComfyUI-LTXLongAudio](https://github.com/Sunwood-ai-labs/ComfyUI-LTXLongAudio)

## Highlights

- Launches a public Codex skill repository for ComfyUI workflow JSON, custom-node
  development, App mode metadata work, schema inspection, and `/prompt`-backed validation.
- Ships bilingual VitePress docs so the skill guidance is available as both repository
  content and a published site.
- Includes the real-world case study
  [ComfyUI-LTXLongAudio](https://github.com/Sunwood-ai-labs/ComfyUI-LTXLongAudio), showing
  that this workflow already supported a public ComfyUI repository and docs launch.

## Tooling And Automation

- Adds `.github/workflows/ci.yml` and `.github/workflows/deploy-docs.yml` so the same source
  tree covers validation and GitHub Pages deployment.
- Includes `scripts/check_workflow_layout.py` as a lightweight static checker that can be run
  with `uv run python scripts/check_workflow_layout.py`.
- Future-proofs the repository workflows around newer JavaScript runtimes; some upstream
  marketplace actions may still emit Node 20 deprecation warnings, but the workflows
  themselves pass under the current pinned runtime strategy.

## Docs And Assets

- Publishes repository-facing docs through `README.md`, `README.ja.md`, `docs/index.md`, and
  `docs/ja/index.md`.
- Ships reusable brand assets through `docs/public/logo.svg`, `docs/public/ogp.svg`,
  `docs/public/ogp.png`, `docs/public/favicon.svg`, and this release header.

## Steady-State Docs Sync

- Reviewed `README.md`, `README.ja.md`, docs home pages, and VitePress navigation for release
  entry points.
- Added versioned release-note and walkthrough pages so the first release can be discovered
  from both GitHub and the published docs.

## Validation

- `npm install`
- `npm run docs:build`
- `uv run python scripts/check_workflow_layout.py --workflow tmp/release-smoke-workflow.json`
- `powershell -ExecutionPolicy Bypass -File D:\Prj\gh-release-notes-skill\scripts\verify-svg-assets.ps1 -RepoPath . -Path docs/public/logo.svg,docs/public/release-header-v0.1.0.svg`

## Upgrade Notes

This is the first public release, so there is no upgrade path from an earlier tagged
version.
