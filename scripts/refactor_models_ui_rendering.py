#!/usr/bin/env python3
"""
scripts/refactor_models_ui_rendering.py
Batch refactoring script for all 398 engineering physics models in models/.

Implements:
- R1: Header overlap resolution (padding: 0 160px on desktop + responsive @media query)
      Canvas text label edge-clamping and boundary collision protection
- R2: Simulation container standardization & deduplication (removing duplicate padding: 0
      and duplicate border declarations)
- R4: Physics rendering line-width elevation (all ctx.lineWidth >= 2.0, zero hairline strokes,
      explicit ctx.lineWidth = 2 in models where unset)
"""

import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MODELS_DIR = REPO_ROOT / "models"


def refactor_header_css(content: str) -> str:
    """Adjusts .header horizontal padding to 0 160px on desktop and places responsive media query at end of <style>."""
    # 1. Update padding: 0 48px to padding: 0 160px inside .header
    content = re.sub(
        r'(\.header\s*\{[^}]*?)padding:\s*0\s+48px;',
        r'\1padding: 0 160px;',
        content
    )

    canonical_mq = (
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

    # 2. If canonical media query already present near the bottom, return
    if canonical_mq in content and content.rfind(canonical_mq) > content.rfind("button#theme-toggle"):
        return content

    # 3. Strip any existing misplaced @media (max-width: 768px) block(s)
    old_target = (
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
    if old_target in content:
        content = content.replace(old_target, "", 1)
    else:
        content = re.sub(
            r"\n*\s*@media\s*\(\s*max-width:\s*768px\s*\)\s*\{.*?\}\s*\}",
            "",
            content,
            flags=re.DOTALL
        )

    # 4. Insert canonical media query at the very bottom of <style>
    replacement_tail = f"\n\n{canonical_mq}\n  </style>"
    content = re.sub(r'\n*\s*</style>', replacement_tail, content, count=1)

    return content


def refactor_container_css(content: str) -> str:
    """Cleans up duplicate padding: 0; and duplicate border declarations in simulation container."""
    pattern = re.compile(
        r'(border:\s*1px solid var\(--sim-border\);\s*)?'
        r'padding:\s*0;\s*'
        r'(?:color:\s*var\(--block-text\);\s*)?'
        r'border-radius:\s*24px;\s*(?:/\*[^*]*\*/\s*)?'
        r'border:\s*1px solid var\(--block-border\);\s*'
        r'padding:\s*24px;'
    )

    replacement = (
        "border-radius: 24px;\n"
        "      border: 1px solid var(--block-border);\n"
        "      padding: 24px;"
    )

    content = pattern.sub(replacement, content)
    return content


def refactor_canvas_script(content: str) -> str:
    """Elevates canvas line weights to >= 2.0 and installs text boundary protection."""
    # 1. Inject default lineWidth = 2 and text label boundary clamping right after ctx initialization
    if 'const _origFillText = ctx.fillText.bind(ctx);' not in content:
        ctx_init_pattern = re.compile(r"const\s+ctx\s*=\s*canvas\.getContext\(['\"]2d['\"]\);")
        ctx_replacement = (
            "const ctx = canvas.getContext('2d');\n"
            "    ctx.lineWidth = 2;\n\n"
            "    // Canvas text label boundary protection & edge-clamping\n"
            "    const _origFillText = ctx.fillText.bind(ctx);\n"
            "    ctx.fillText = function(text, x, y, maxWidth) {\n"
            "      if (typeof x === 'number' && typeof y === 'number' && width > 0 && height > 0) {\n"
            "        const pad = 10;\n"
            "        const str = String(text);\n"
            "        const m = ctx.measureText(str);\n"
            "        const tw = (typeof maxWidth === 'number' && maxWidth < m.width) ? maxWidth : m.width;\n"
            "        const align = ctx.textAlign || 'left';\n"
            "        let minX = pad, maxX = width - pad;\n"
            "        let clampedX = x;\n"
            "        if (align === 'center') {\n"
            "          clampedX = Math.max(minX + tw / 2, Math.min(maxX - tw / 2, x));\n"
            "        } else if (align === 'right' || align === 'end') {\n"
            "          clampedX = Math.max(minX + tw, Math.min(maxX, x));\n"
            "        } else {\n"
            "          clampedX = Math.max(minX, Math.min(maxX - tw, x));\n"
            "        }\n"
            "        const clampedY = Math.max(pad + 12, Math.min(height - pad, y));\n"
            "        return maxWidth !== undefined ? _origFillText(str, clampedX, clampedY, maxWidth) : _origFillText(str, clampedX, clampedY);\n"
            "      }\n"
            "      return maxWidth !== undefined ? _origFillText(text, x, y, maxWidth) : _origFillText(text, x, y);\n"
            "    };"
        )
        content = ctx_init_pattern.sub(ctx_replacement, content, count=1)

    # 2. Add ctx.lineWidth = 2 in resize() if not already setting lineWidth
    if "function resize()" in content and "ctx.scale(dpr, dpr);" in content:
        if "ctx.scale(dpr, dpr);\n    ctx.lineWidth = 2;" not in content:
            content = content.replace(
                "ctx.scale(dpr, dpr);",
                "ctx.scale(dpr, dpr);\n    ctx.lineWidth = 2;"
            )

    # 3. Numeric literals < 2.0 -> 2
    def repl_lw(m):
        num_str = m.group(2).strip()
        try:
            val = float(num_str)
            if val < 2.0:
                return f"{m.group(1)}2;"
            return m.group(0)
        except ValueError:
            return m.group(0)

    content = re.sub(r'(\b(?:ctx|context)\.lineWidth\s*=\s*)([0-9]+(?:\.[0-9]+)?)\s*;', repl_lw, content)

    # 4. Ternary and dynamic expression hairlines
    expr_replacements = [
        ('(i === j) ? 2 : 1', '(i === j) ? 2.5 : 2'),
        ('(isOptimalPath || isActive) ? 2 : 1', '(isOptimalPath || isActive) ? 2.5 : 2'),
        ('(line === Math.floor(numLines / 2)) ? 3 : 1.8', '(line === Math.floor(numLines / 2)) ? 3 : 2'),
        ('(s === numSurfaces) ? 2.5 : 1.2', '(s === numSurfaces) ? 2.5 : 2'),
        ('isActive ? 2.5 : 1.5', 'isActive ? 2.5 : 2'),
        ('isActive ? 2.5 : 1', 'isActive ? 2.5 : 2'),
        ('isActive ? 3 : (isSettled ? 2.5 : 1.5)', 'isActive ? 3 : (isSettled ? 2.5 : 2)'),
        ('isActive ? 3 : 1.5', 'isActive ? 3 : 2'),
        ('isHead ? 2.5 : 1', 'isHead ? 2.5 : 2'),
        ('isMatch ? 2 : 1', 'isMatch ? 2.5 : 2'),
        ('isNash ? 2.5 : 1.2', 'isNash ? 2.5 : 2'),
        ('isSP ? 3.5 : 1.5', 'isSP ? 3.5 : 2'),
        ('isSelected ? 2 : 1', 'isSelected ? 2.5 : 2'),
        ('isTargetB ? 2 : 1', 'isTargetB ? 2.5 : 2'),
        ('isVisitedInSearch ? 2.5 : 1.5', 'isVisitedInSearch ? 2.5 : 2'),
        ('obj.reachable ? 2.5 : 1.5', 'obj.reachable ? 2.5 : 2'),
        ('req.active ? 2.5 : 1.5', 'req.active ? 2.5 : 2'),
        ('req.active ? 2.5 : 1', 'req.active ? 2.5 : 2'),
        ('s.defect ? 2.5 : 1.5', 's.defect ? 2.5 : 2'),
        ('sw.on ? 2.5 : 1.5', 'sw.on ? 2.5 : 2'),
        ('Math.max(1, Math.abs(eMag) * 3)', 'Math.max(2, Math.abs(eMag) * 3)'),
        ('3 * amp + 0.5', '3 * amp + 2'),
        ('uncutH / chipRatio * 0.45', 'Math.max(2.5, uncutH / chipRatio * 0.45)'),
        ('traceW * scale', 'Math.max(2, traceW * scale)'),
        ('Math.abs(weights[idx]) * 3', 'Math.max(2, Math.abs(weights[idx]) * 3)'),
    ]

    for old_s, new_s in expr_replacements:
        content = content.replace(old_s, new_s)

    return content


def refactor_model_file(path: Path) -> bool:
    """Applies R1, R2, and R4 refactoring to a single HTML model file."""
    original = path.read_text(encoding="utf-8")
    content = original

    content = refactor_header_css(content)
    content = refactor_container_css(content)
    content = refactor_canvas_script(content)

    if content != original:
        path.write_text(content, encoding="utf-8")
        return True
    return False


def main():
    models = sorted([
        f for f in MODELS_DIR.glob("**/*.html")
        if not any(ex in f.parts for ex in ["misc", "__pycache__"])
    ])

    print(f"Refactoring {len(models)} engineering physics models...")
    modified_count = 0

    for m in models:
        modified = refactor_model_file(m)
        if modified:
            modified_count += 1

    print(f"Refactoring complete: {modified_count} / {len(models)} models updated.")


if __name__ == "__main__":
    main()
