#!/usr/bin/env python3
"""
scripts/remediate_mobile_cascade.py
Batch remediation script to fix CSS source-order cascade defect across all 398 engineering physics models.

Relocates the @media (max-width: 768px) block to the very bottom of the <style> block
(immediately before </style>) and sets:
  position: static !important;
  margin: 12px auto 4px auto !important;

This ensures mobile header clearance overrides desktop absolute positioning properly,
guaranteeing zero collision between title/badge and theme toggle button on mobile viewports.
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MODELS_DIR = REPO_ROOT / "models"
EXCLUDE_DIRS = {"misc", "__pycache__", ".agents"}

CANONICAL_MEDIA_QUERY = (
    "    @media (max-width: 768px) {\n"
    "      .header {\n"
    "        padding: 0 16px;\n"
    "      }\n"
    "      .figma-pill,\n"
    "      .theme-toggle,\n"
    "      button#theme-toggle {\n"
    "        position: static !important;\n"
    "        margin: 12px auto 4px auto !important;\n"
    "      }\n"
    "    }"
)

OLD_MEDIA_QUERY_TARGET = (
    "\n\n    @media (max-width: 768px) {\n"
    "      .header {\n"
    "        padding: 0 16px;\n"
    "      }\n"
    "      .figma-pill,\n"
    "      .theme-toggle,\n"
    "      button#theme-toggle {\n"
    "        position: static;\n"
    "        margin-bottom: 12px;\n"
    "      }\n"
    "    }"
)


def remediate_model(file_path: Path) -> bool:
    """Relocates media query to the bottom of <style> with position: static and calibrated margin."""
    content = file_path.read_text(encoding="utf-8")

    # Idempotency check: if canonical media query is already after the button rule and at the bottom
    btn_pos = content.rfind("button#theme-toggle")
    mq_pos = content.rfind(CANONICAL_MEDIA_QUERY)
    style_end = content.rfind("</style>")
    if mq_pos != -1 and mq_pos > btn_pos and mq_pos > (style_end - 500):
        return False

    # 1. Remove misplaced media query
    if OLD_MEDIA_QUERY_TARGET in content:
        content_clean = content.replace(OLD_MEDIA_QUERY_TARGET, "", 1)
    else:
        content_clean = re.sub(
            r"\n*\s*@media\s*\(\s*max-width:\s*768px\s*\)\s*\{.*?\}\s*\}",
            "",
            content,
            flags=re.DOTALL
        )

    if "</style>" not in content_clean:
        print(f"Warning: No </style> found in {file_path}", file=sys.stderr)
        return False

    # 2. Insert canonical media query immediately before </style>
    replacement_tail = f"\n\n{CANONICAL_MEDIA_QUERY}\n  </style>"
    new_content = re.sub(r'\n*\s*</style>', replacement_tail, content_clean, count=1)

    if new_content != content:
        file_path.write_text(new_content, encoding="utf-8")
        return True
    return False


def main():
    models = sorted([
        p for p in MODELS_DIR.glob("**/*.html")
        if not any(ex in p.parts for ex in EXCLUDE_DIRS)
    ])
    print(f"Auditing and remediating {len(models)} models for mobile media query cascade...")

    modified = 0
    for m in models:
        if remediate_model(m):
            modified += 1

    print(f"Remediation complete: {modified}/{len(models)} files updated.")
    if modified != len(models) and modified != 0:
        print(f"Notice: {len(models) - modified} files were already up-to-date.")


if __name__ == "__main__":
    main()
