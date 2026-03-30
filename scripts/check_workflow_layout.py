"""Lightweight static checks for ComfyUI workflow graph layout.

This helper is intentionally dependency-free so it can run via:

    uv run python scripts/check_workflow_layout.py --workflow path/to/workflow.json

It does not attempt full ComfyUI schema validation. Instead, it checks a few
high-signal structural issues that are helpful during repository-side QA:

- workflow file parses as JSON
- top-level ``nodes`` list exists and is non-empty
- node ids are unique
- node type/class_type labels exist
- node positions are finite numbers
- node rectangles with known size do not overlap excessively
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class Finding:
    level: str
    message: str


@dataclass
class NodeRect:
    node_id: str
    label: str
    x: float
    y: float
    width: float
    height: float


def _coerce_xy(value: Any) -> tuple[float, float] | None:
    if isinstance(value, (list, tuple)) and len(value) >= 2:
        return _coerce_pair(value[0], value[1])

    if isinstance(value, dict):
        if "x" in value and "y" in value:
            return _coerce_pair(value["x"], value["y"])

        if 0 in value and 1 in value:
            return _coerce_pair(value[0], value[1])

        if "0" in value and "1" in value:
            return _coerce_pair(value["0"], value["1"])

    return None


def _coerce_pair(first: Any, second: Any) -> tuple[float, float] | None:
    try:
        x = float(first)
        y = float(second)
    except (TypeError, ValueError):
        return None

    if not math.isfinite(x) or not math.isfinite(y):
        return None

    return x, y


def _extract_nodes(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, dict) and isinstance(payload.get("nodes"), list):
        return [node for node in payload["nodes"] if isinstance(node, dict)]
    return []


def _node_id(node: dict[str, Any], fallback: int) -> str:
    return str(node.get("id", fallback))


def _node_label(node: dict[str, Any], fallback: str) -> str:
    for key in ("type", "class_type", "title"):
        value = node.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return fallback


def _node_rect(node: dict[str, Any], fallback: int) -> NodeRect | None:
    pos = _coerce_xy(node.get("pos"))
    size = _coerce_xy(node.get("size"))
    if pos is None or size is None:
        return None

    width, height = size
    if width <= 0 or height <= 0:
        return None

    return NodeRect(
        node_id=_node_id(node, fallback),
        label=_node_label(node, f"node-{fallback}"),
        x=pos[0],
        y=pos[1],
        width=width,
        height=height,
    )


def _rectangles_overlap(left: NodeRect, right: NodeRect) -> bool:
    horizontal = left.x < right.x + right.width and left.x + left.width > right.x
    vertical = left.y < right.y + right.height and left.y + left.height > right.y
    return horizontal and vertical


def inspect_workflow(path: Path) -> tuple[list[Finding], int]:
    findings: list[Finding] = []

    if not path.exists():
        return [Finding("error", f"Workflow file does not exist: {path}")], 2

    try:
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError as exc:
        return [Finding("error", f"Invalid JSON: {exc}")], 2

    if not isinstance(payload, dict):
        return [Finding("error", "Workflow root must be a JSON object.")], 2

    nodes = _extract_nodes(payload)
    if not nodes:
        return [Finding("error", "Top-level 'nodes' list is missing or empty.")], 2

    seen_ids: set[str] = set()
    rects: list[NodeRect] = []

    for index, node in enumerate(nodes, start=1):
        node_id = _node_id(node, index)
        label = _node_label(node, f"node-{index}")

        if node_id in seen_ids:
            findings.append(Finding("error", f"Duplicate node id detected: {node_id}"))
        else:
            seen_ids.add(node_id)

        if label.startswith("node-"):
            findings.append(Finding("warning", f"Node {node_id} is missing a type/class_type/title label."))

        if _coerce_xy(node.get("pos")) is None:
            findings.append(Finding("warning", f"Node {node_id} ({label}) has no valid position tuple."))

        rect = _node_rect(node, index)
        if rect is not None:
            rects.append(rect)

    overlap_pairs: list[str] = []
    for i, left in enumerate(rects):
        for right in rects[i + 1 :]:
            if _rectangles_overlap(left, right):
                overlap_pairs.append(f"{left.node_id} ({left.label}) overlaps {right.node_id} ({right.label})")

    if overlap_pairs:
        findings.append(Finding("warning", f"Detected {len(overlap_pairs)} overlapping node rectangle(s)."))
        for pair in overlap_pairs[:10]:
            findings.append(Finding("warning", f"  - {pair}"))
        if len(overlap_pairs) > 10:
            findings.append(Finding("warning", "  - additional overlaps omitted"))

    return findings, 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workflow", required=True, help="Path to a ComfyUI workflow JSON file.")
    args = parser.parse_args()

    findings, status = inspect_workflow(Path(args.workflow))
    has_error = any(finding.level == "error" for finding in findings)

    if not findings:
        print("OK: workflow parsed successfully and no layout warnings were detected.")
        return 0

    for finding in findings:
        print(f"{finding.level.upper()}: {finding.message}")

    if has_error:
        return status or 1

    print("Completed with warnings. Review the findings above.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
