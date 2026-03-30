# Workflow Design

## Preserve The Baseline First

Workflow iteration gets risky when the original structure is lost. Before large changes:

- save an untouched upstream workflow backup
- keep milestone snapshots for each structural revision
- compare against the upstream graph before introducing helper nodes
- treat compatibility shims and native rewrites as separate choices

## Choose The Input Model Early

The public workflow surface should match how the user thinks:

- use a folder selector when the workflow should consume a variable number of images
- use an upload widget when the user naturally replaces one file at a time
- avoid hard-coding multiple upload slots when the real need is "pick from a set"
- choose a model the user can explain in one sentence

## Prefer A Native Public Node Surface

Once the canonical node names, categories, and widget labels are clear:

- standardize sample workflows on that surface
- keep old compatibility layers explicit and isolated
- avoid hiding major workflow drift behind convenience wrappers

## Keep Sample Workflows Shareable

- do not ship machine-local paths in a workflow meant for others
- keep defaults blank for public examples
- inject sample assets only during automated smoke runs
- separate heavy production graphs from lightweight smoke workflows

## Treat Layout As Maintainability

Readable graphs are easier to debug and review. Watch for:

- overlapping groups or nodes
- title-band collisions
- nodes falling outside intended group bounds
- App mode metadata drifting away from actual widget layout

## Release Checklist

- explain the App mode input model in the published docs
- keep install or clone steps short enough for ephemeral environments
- publish sample workflows that are safe to share and safe to validate automatically
