# Design Patterns

## Preserve the Baseline First

- Save an untouched upstream workflow backup before editing.
- Keep milestone snapshots when a workflow goes through multiple structural revisions.
- Compare against the upstream structure before introducing helper nodes or compatibility layers.
- Treat "compatibility shim" and "native rewrite" as separate tracks. Do not mix them accidentally.

## Choose the Input Model Early

- Use a folder selector when the user supplies a variable number of images and the workflow will choose among them dynamically.
- Use a direct upload widget when the user naturally thinks in terms of replacing one file at a time, such as a single source audio file.
- Avoid hard-coding a fixed number of upload slots when the real requirement is "any number of frames" or "pick one image from a set."
- Prefer a mental model the user can explain in one sentence.

### Good defaults for the LTX-style pattern

- Images: folder selector plus batched image loading plus index selection.
- Audio: load once, compute per-segment timing, and slice only the needed span.
- Timing or frame-rate edge cases: provide explicit fallback behavior for short tail segments.

## Prefer a Native Public Node Surface

- Decide the canonical node type names, categories, and widget labels before publishing the helper repository.
- Standardize workflow examples on the canonical node surface once it exists.
- Remove legacy naming only after the public workflow examples no longer depend on it.
- If backward compatibility is still required, keep the compatibility layer clearly labeled and isolated.

## Keep Sample Workflows Shareable

- Do not bake machine-local file paths into the workflow JSON you expect other users to open.
- Prefer blank defaults for shareable workflows and inject sample assets only during automated validation.
- If the production workflow is expensive, create a separate smoke workflow that exercises the node contracts without full model cost.

## Treat Layout as Maintainability

- Watch for group overlap, title-band overlap, node overlap, and nodes falling outside their intended group bounds.
- Treat workflow JSON as code: static structure, layout, and App mode metadata deserve linting or scripted checks.
- If the graph stops being readable, maintenance and debugging slow down even when execution still works.

## Release Checklist

- Explain the App mode input model in the published README or workflow notes.
- Keep clone or install steps short enough for Colab or other ephemeral environments.
- Publish sample workflows that are safe to share and safe to validate automatically.
