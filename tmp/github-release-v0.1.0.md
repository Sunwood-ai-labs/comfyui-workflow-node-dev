![Release header for v0.1.0](https://sunwood-ai-labs.github.io/comfyui-workflow-node-dev/release-header-v0.1.0.png)

[Release Notes](https://sunwood-ai-labs.github.io/comfyui-workflow-node-dev/guide/release-notes-v0.1.0) | [Walkthrough](https://sunwood-ai-labs.github.io/comfyui-workflow-node-dev/guide/whats-new-v0.1.0)

## Initial release scope

`v0.1.0` is the first release of `comfyui-workflow-node-dev`. These notes cover the full
shipped history from the repository root commit through current `HEAD`.

## Highlights

### Public ComfyUI workflow-dev skill and docs surface

- Ship the core Codex skill for ComfyUI workflow JSON, custom nodes, App mode metadata,
  `/object_info` checks, and `/prompt` smoke validation.
- Publish bilingual README and VitePress docs for getting started, workflow design, App
  mode and schema guidance, and validation and operations.
- Encode concrete maintainer rules around preserving upstream workflow intent, exposing only
  widget-backed App mode inputs, separating stale Desktop state from fresh backend truth,
  and closing runtime-sensitive work with evidence.

### Executable workflow layout smoke checks

- Add a lightweight `uv run` static checker for ComfyUI workflow JSON.
- Accept UTF-8 BOM input and report missing or empty `nodes`, duplicate node IDs, missing
  labels, invalid positions, and overlapping node rectangles.
- Give the repository its first concrete executable QA helper instead of docs-only
  validation guidance.

### Docs publishing and workflow hardening

- Add CI to build the VitePress site and a GitHub Pages workflow to build, upload, and
  deploy the docs artifact from the same repository.
- Configure the docs site for the GitHub Pages base path, sitemap generation, bilingual
  navigation, and branded logo, favicon, and OGP assets.
- Opt GitHub JavaScript actions into Node 24 to reduce action-runtime deprecation risk
  without changing the docs publishing path.

### Example in practice

- Add [ComfyUI-LTXLongAudio](https://github.com/Sunwood-ai-labs/ComfyUI-LTXLongAudio) as a
  linked case study across the README and docs home page so readers can see the workflow
  patterns applied in a shipped public repo.

## Validation

- `npm install`
- `npm run docs:build`
- `uv run python scripts/check_workflow_layout.py --workflow tmp/release-smoke-workflow.json`
- `powershell -ExecutionPolicy Bypass -File D:\Prj\gh-release-notes-skill\scripts\verify-svg-assets.ps1 -RepoPath . -Path docs/public/logo.svg,docs/public/release-header-v0.1.0.svg`

## Caveats

- This is an initial release and the notes intentionally cover the full history, not a
  delta from an earlier tag.
- The current scope is guidance-heavy: the repo does not yet ship example workflow JSON
  files, sample custom nodes, smoke fixtures, compatibility tables, or captured runtime
  evidence such as example `prompt_id` histories.
- Some marketplace-hosted GitHub actions may still emit upstream Node 20 deprecation
  warnings. The repository workflows are already aligned with the current runtime strategy,
  so this is not a blocker for `v0.1.0`.
