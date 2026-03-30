# Release QA Inventory

## Release Context

- repository: `comfyui-workflow-node-dev`
- release tag: `v0.1.0`
- compare range: `initial release from root commit e353be0c000bccc142d2ecefccadd775762e03bb to HEAD 9eb5a0d6f1d50ef5bc2caeb8e9f4545392e170a3`
- requested outputs: `GitHub release body, docs-backed release notes, companion walkthrough article`
- validation commands run: `npm install`, `npm run docs:build`, `uv run python scripts/check_workflow_layout.py --workflow tmp/release-smoke-workflow.json`, `powershell -ExecutionPolicy Bypass -File D:\Prj\gh-release-notes-skill\scripts\verify-svg-assets.ps1 -RepoPath . -Path docs/public/logo.svg,docs/public/release-header-v0.1.0.svg`
- release URLs: `pending pre-publish validation update`

## Claim Matrix

| claim | code refs | validation refs | docs surfaces touched | scope |
| --- | --- | --- | --- | --- |
| Initial release packages the public skill, bilingual docs surface, CI and Pages delivery, and the workflow layout checker | `SKILL.md`, `agents/openai.yaml`, `.github/workflows/ci.yml`, `.github/workflows/deploy-docs.yml`, `scripts/check_workflow_layout.py`, `docs/.vitepress/config.ts` | `npm run docs:build`, `uv run python scripts/check_workflow_layout.py --workflow tmp/release-smoke-workflow.json`, `powershell -ExecutionPolicy Bypass -File D:\Prj\gh-release-notes-skill\scripts\verify-svg-assets.ps1 -RepoPath . -Path docs/public/logo.svg,docs/public/release-header-v0.1.0.svg` | `README.md`, `README.ja.md`, `docs/index.md`, `docs/ja/index.md`, `docs/.vitepress/config.ts` | steady_state |
| The release evidence includes a real public example through ComfyUI-LTXLongAudio | `README.md`, `README.ja.md`, `docs/index.md`, `docs/ja/index.md` | `gh repo view Sunwood-ai-labs/ComfyUI-LTXLongAudio --json name,description,url,homepageUrl,visibility` | `README.md`, `README.ja.md`, `docs/index.md`, `docs/ja/index.md` | release_collateral |

## Steady-State Docs Review

| surface | status | evidence |
| --- | --- | --- |
| README.md | pass | Added latest-release links and kept the public scope wording aligned with the shipped repository surfaces |
| README.ja.md | pass | Synced the Japanese latest-release links and initial-release summary with the English README |
| docs/index.md | pass | Added latest-release entry points pointing at the release notes and walkthrough |
| docs/ja/index.md | pass | Added the same latest-release entry points for the Japanese docs home |
| docs/.vitepress/config.ts | pass | Added EN and JA release navigation and sidebar links without changing the established guide structure |

## QA Inventory

| criterion_id | status | evidence |
| --- | --- | --- |
| compare_range | pass | `git tag --list` returned no tags, collector resolved the initial-release scope from root commit `e353be0c000bccc142d2ecefccadd775762e03bb` to `HEAD` `9eb5a0d6f1d50ef5bc2caeb8e9f4545392e170a3` |
| release_claims_backed | pass | Claim matrix rows are tied to repo files, commit history, and executed local validation commands |
| docs_release_notes | pass | `docs/guide/release-notes-v0.1.0.md`, `docs/ja/guide/release-notes-v0.1.0.md` |
| companion_walkthrough | pass | `docs/guide/whats-new-v0.1.0.md`, `docs/ja/guide/whats-new-v0.1.0.md` |
| operator_claims_extracted | pass | Release notes and walkthrough are limited to the shipped skill, docs, CI, Pages, checker, and case-study surfaces |
| impl_sensitive_claims_verified | pass | `npm run docs:build`, `uv run python scripts/check_workflow_layout.py --workflow tmp/release-smoke-workflow.json`, and SVG validation were executed locally |
| steady_state_docs_reviewed | pass | README, Japanese README, docs home pages, and VitePress navigation were reviewed in the table above |
| claim_scope_precise | pass | Initial-release wording is scoped to the full shipped history and explicitly avoids claiming bundled runtime artifacts that are not present |
| latest_release_links_updated | pass | Added latest-release pointers in `README.md`, `README.ja.md`, `docs/index.md`, `docs/ja/index.md`, and `docs/.vitepress/config.ts` |
| svg_assets_validated | pass | `powershell -ExecutionPolicy Bypass -File D:\Prj\gh-release-notes-skill\scripts\verify-svg-assets.ps1 -RepoPath . -Path docs/public/logo.svg,docs/public/release-header-v0.1.0.svg` |
| docs_assets_committed_before_tag | not_applicable | Pre-publish draft inventory; will be updated to pass after the release collateral commit is created and before the tag is pushed |
| docs_deployed_live | not_applicable | Pre-publish draft inventory; will be updated after the docs collateral commit is pushed and the Pages URLs are verified live |
| tag_local_remote | not_applicable | Pre-publish draft inventory; `v0.1.0` has not been created yet |
| github_release_verified | not_applicable | Pre-publish draft inventory; the GitHub release does not exist yet |
| validation_commands_recorded | pass | Recorded in Release Context and repeated in claim matrix and validation evidence rows |
| publish_date_verified | not_applicable | Pre-publish draft inventory; the release publish timestamp does not exist yet |

## Notes

- blockers:
- waivers:
- follow-up docs tasks: update this inventory with live Pages and release verification evidence after publication
