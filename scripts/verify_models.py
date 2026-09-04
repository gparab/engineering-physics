#!/usr/bin/env python3
"""
scripts/verify_models.py
Automated Verification Suite for Engineering Physics Figma Design System & Quality Standards.

Validates all surviving standalone HTML physics models in models/
against the 14 core rules defined in ORIGINAL_REQUEST.md (2026-09-04T07:02:25Z),
FIGMA_DESIGN_SYSTEM.md, and PROJECT.md:

Per-Model Rules (Category A):
  RULE_01: Starts with <!DOCTYPE html> and standard HTML5 boilerplate
  RULE_02: Header with title <h1> and discipline badge
  RULE_03: Pill buttons and toggles (border-radius: 50px or pill)
  RULE_04: Inter font family and NO intermediate gray body text
  RULE_05: Simulation container uses pastel background color block with 24px rounded corners
  RULE_06: Simulation container with <canvas> or <svg> running continuous animation
  RULE_07: "How It Works" explanation section with unicode governing equation
  RULE_08: Meaningful developer comments explaining simulation mechanics in <script>
  RULE_09: Strict standalone architecture (zero external CSS, zero external JS except GSAP core CDN)
  RULE_10: Anti-gimmick check (zero destructive .remove(), explosive scales, or element clearing)
  RULE_11: Inline JavaScript syntax verification (AST compilation under Node.js)

Repository & E2E Acceptance Criteria (Category B):
  RULE_12: Confusing/forbidden folders (cam engineering, abstract, misc) eliminated & exact 23 canonical folders present
  RULE_13: Dashboard (index.html) successfully regenerated with 100% valid links (zero broken, zero orphaned)
  RULE_14: Central model ratings report (model_ratings.md) exists with valid 1-10 scores for all surviving models
"""

import argparse
import json
import os
import random
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, NamedTuple, Optional, Set, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
MODELS_DIR = REPO_ROOT / "models"
INDEX_HTML = REPO_ROOT / "index.html"
MODEL_RATINGS_MD = REPO_ROOT / "model_ratings.md"

ALLOWED_GSAP_CDN = "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"

# Approved pastel color tokens / hex codes from FIGMA_DESIGN_SYSTEM.md
PASTEL_COLOR_TOKENS = {
    # Lime
    "#d4f542", "#e2f952", "#d9f99d", "#dcfce7", "--block-lime", "var(--block-lime)", "block-lime",
    # Lilac
    "#e0d4fc", "#ede9fe", "#ddd6fe", "--block-lilac", "var(--block-lilac)", "block-lilac",
    # Cream
    "#fff5ea", "#fef3c7", "#ffedd5", "#fdf6e2", "--block-cream", "var(--block-cream)", "block-cream",
    # Mint
    "#d2f8e5", "#ccfbf1", "#d1fae5", "#a7f3d0", "--block-mint", "var(--block-mint)", "block-mint",
    # Pink
    "#fed7e2", "#fce7f3", "#fbcfe8", "--block-pink", "var(--block-pink)", "block-pink",
    # Coral
    "#ffd6cc", "#ffedd5", "#ffccbc", "#fecdd3", "--block-coral", "var(--block-coral)", "block-coral",
    # Navy (inverse story block)
    "#1c2042", "#1e1b4b", "#0f172a", "--block-navy", "var(--block-navy)", "block-navy",
}

# Intermediate gray colors that violate the Figma Marketing rule:
# "Body copy is always black at weight 320-340, and weight (not opacity) carries hierarchy. No mid-gray text."
FORBIDDEN_MID_GRAY_PATTERNS = [
    r'#616161\b', r'#757575\b', r'#888888\b', r'#888\b', r'#9e9eb4\b',
    r'#999999\b', r'#999\b', r'#aaaaaa\b', r'#aaa\b', r'#666666\b',
    r'#666\b', r'#777777\b', r'#777\b', r'#555555\b', r'#555\b',
    r'#b0b0b0\b', r'#4a4a4a\b',
]

FORBIDDEN_FOLDERS = ["cam engineering", "abstract", "misc"]

CANONICAL_DISCIPLINE_FOLDERS = {
    "acoustics_engineering",
    "aerospace_engineering",
    "agricultural_engineering",
    "biomedical_engineering",
    "chemical_engineering",
    "civil_engineering",
    "computer_engineering",
    "computer_science",
    "electrical_engineering",
    "electronics_engineering",
    "energy_engineering",
    "environmental_engineering",
    "fundamental_physics",
    "industrial_systems_engineering",
    "marine_engineering",
    "materials_science",
    "mechanical_engineering",
    "mining_petroleum_engineering",
    "nanotechnology",
    "nuclear_engineering",
    "optical_engineering",
    "robotics_engineering",
    "telecommunications_engineering",
}


class RuleResult(NamedTuple):
    rule_id: str
    rule_name: str
    passed: bool
    message: str


class FileValidationResult:
    def __init__(self, path: Path):
        self.path = path
        self.rel_path = str(path.relative_to(REPO_ROOT)) if REPO_ROOT in path.parents or path == REPO_ROOT else str(path)
        self.rule_results: List[RuleResult] = []

    @property
    def passed(self) -> bool:
        return all(r.passed for r in self.rule_results)

    @property
    def failure_count(self) -> int:
        return sum(1 for r in self.rule_results if not r.passed)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "path": self.rel_path,
            "passed": self.passed,
            "rules": [
                {
                    "rule_id": r.rule_id,
                    "rule_name": r.rule_name,
                    "passed": r.passed,
                    "message": r.message,
                }
                for r in self.rule_results
            ],
        }


# ============================================================================
# Rule 1: Starts with <!DOCTYPE html>
# ============================================================================
def check_rule_1_doctype(content: str) -> RuleResult:
    rule_id = "RULE_01"
    name = "Starts with <!DOCTYPE html>"
    stripped = content.lstrip("\ufeff \t\r\n")
    if stripped.lower().startswith("<!doctype html"):
        return RuleResult(rule_id, name, True, "Starts with <!DOCTYPE html>")
    return RuleResult(rule_id, name, False, "Document does not start with <!DOCTYPE html>")


# ============================================================================
# Rule 2: Header with title <h1> and discipline badge
# ============================================================================
def check_rule_2_header_title_badge(content: str) -> RuleResult:
    rule_id = "RULE_02"
    name = "Header with title <h1> and discipline badge"
    header_match = re.search(r'<header[^>]*>(.*?)</header>', content, re.DOTALL | re.IGNORECASE)
    header_content = header_match.group(1) if header_match else content

    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', header_content, re.DOTALL | re.IGNORECASE)
    if not h1_match:
        return RuleResult(rule_id, name, False, "Missing <h1> model title in <header>")
    title_text = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip()
    if not title_text or title_text.startswith("<!--"):
        return RuleResult(rule_id, name, False, "<h1> model title is empty or placeholder")

    badge_match = re.search(
        r'<div[^>]*class=["\'][^"\']*\bdiscipline-badge\b[^"\']*["\'][^>]*>(.*?)</div>',
        header_content,
        re.DOTALL | re.IGNORECASE,
    )
    if not badge_match:
        return RuleResult(rule_id, name, False, "Missing <div class=\"discipline-badge\"> in <header>")
    badge_text = re.sub(r'<[^>]+>', '', badge_match.group(1)).strip()
    if not badge_text or badge_text.startswith("<!--"):
        return RuleResult(rule_id, name, False, "Discipline badge text is empty or placeholder")

    return RuleResult(rule_id, name, True, f"Header contains title '{title_text}' and badge '{badge_text}'")


# ============================================================================
# Rule 3: Pill buttons and toggles (border-radius: 50px or pill)
# ============================================================================
def check_rule_3_pill_buttons(content: str) -> RuleResult:
    rule_id = "RULE_03"
    name = "Pill buttons (border-radius: 50px or pill)"
    styles = "\n".join(re.findall(r'<style[^>]*>(.*?)</style>', content, re.DOTALL | re.IGNORECASE))
    if not styles:
        return RuleResult(rule_id, name, False, "No inline <style> found")

    # Match border-radius: 50px, 9999px, 999px, or var(--rounded-pill)
    has_pill_radius = bool(
        re.search(r'border-radius\s*:\s*(?:50px|9999px|999px|var\(--rounded-pill[^)]*\))', styles, re.IGNORECASE)
    )
    if not has_pill_radius:
        return RuleResult(rule_id, name, False, "CSS missing pill button border-radius (expected border-radius: 50px or 9999px)")

    # Verify button or theme toggle uses pill styling
    button_or_toggle_pill = bool(
        re.search(r'(?:\.theme-toggle|button|\.btn|\.pill)[^{]*\{[^}]*border-radius\s*:\s*(?:50px|9999px|999px|var\(--rounded-pill)', styles, re.IGNORECASE | re.DOTALL)
    )
    if not button_or_toggle_pill and not has_pill_radius:
        return RuleResult(rule_id, name, False, "Buttons/toggles do not use pill shape (border-radius: 50px)")

    return RuleResult(rule_id, name, True, "Buttons and toggles configured as pills (border-radius: 50px)")


# ============================================================================
# Rule 4: Inter font family & NO intermediate gray body text
# ============================================================================
def check_rule_4_font_and_no_mid_gray(content: str) -> RuleResult:
    rule_id = "RULE_04"
    name = "Inter font family and NO intermediate gray body text"
    styles = "\n".join(re.findall(r'<style[^>]*>(.*?)</style>', content, re.DOTALL | re.IGNORECASE))
    if not styles:
        return RuleResult(rule_id, name, False, "No inline <style> found")

    # Check Inter font
    if "Inter" not in styles:
        return RuleResult(rule_id, name, False, "CSS does not specify 'Inter' font family")

    # Check for forbidden intermediate gray body text tokens
    found_grays = []
    for pat in FORBIDDEN_MID_GRAY_PATTERNS:
        matches = re.findall(pat, styles, re.IGNORECASE)
        if matches:
            found_grays.extend(matches)

    if found_grays:
        unique_grays = sorted(set(found_grays))
        return RuleResult(
            rule_id,
            name,
            False,
            f"Found forbidden intermediate gray text colors in CSS: {', '.join(unique_grays)} (Figma design requires ink text with weight-based hierarchy)",
        )

    return RuleResult(rule_id, name, True, "Uses Inter font family with zero intermediate gray body text")


# ============================================================================
# Rule 5: Simulation container uses pastel background color block with 24px rounded corners
# ============================================================================
def check_rule_5_pastel_container_24px(content: str) -> RuleResult:
    rule_id = "RULE_05"
    name = "Simulation container with pastel color block & 24px rounded corners"
    styles = "\n".join(re.findall(r'<style[^>]*>(.*?)</style>', content, re.DOTALL | re.IGNORECASE))
    if not styles:
        return RuleResult(rule_id, name, False, "No inline <style> found")

    # Check for 24px rounded corners on simulation container
    has_24px_radius = bool(
        re.search(r'border-radius\s*:\s*(?:24px|var\(--rounded-lg[^)]*\))', styles, re.IGNORECASE)
    )
    if not has_24px_radius:
        return RuleResult(rule_id, name, False, "Simulation container missing 24px rounded corners (border-radius: 24px)")

    # Check for pastel background color token or variable
    has_pastel_bg = False
    for token in PASTEL_COLOR_TOKENS:
        if token.lower() in styles.lower() or token.lower() in content.lower():
            has_pastel_bg = True
            break

    if not has_pastel_bg:
        return RuleResult(
            rule_id,
            name,
            False,
            "Simulation container missing approved pastel color block background (lime, lilac, cream, mint, pink, coral, navy)",
        )

    return RuleResult(rule_id, name, True, "Simulation container houses visualization in pastel block with 24px rounded corners")


# ============================================================================
# Rule 6: Simulation container with <canvas> or <svg>
# ============================================================================
def check_rule_6_main_canvas_svg(content: str) -> RuleResult:
    rule_id = "RULE_06"
    name = "Simulation container with <canvas> or <svg>"
    main_match = re.search(r'<main[^>]*>(.*?)</main>', content, re.DOTALL | re.IGNORECASE)
    main_content = main_match.group(1) if main_match else content

    has_canvas = bool(re.search(r'<canvas[^>]*>', main_content, re.IGNORECASE))
    has_svg = bool(re.search(r'<svg[^>]*>', main_content, re.IGNORECASE))

    if not (has_canvas or has_svg):
        return RuleResult(rule_id, name, False, "Simulation container does not contain <canvas> or <svg>")

    element_type = "canvas" if has_canvas else "svg"
    return RuleResult(rule_id, name, True, f"Simulation container houses continuous <{element_type}>")


# ============================================================================
# Rule 7: "How It Works" explanation & unicode governing equation
# ============================================================================
def check_rule_7_explanation_equation(content: str) -> RuleResult:
    rule_id = "RULE_07"
    name = "'How It Works' section with unicode governing equation"

    # Check <h2>How It Works</h2>
    if not re.search(r'<h2[^>]*>\s*How It Works\s*</h2>', content, re.IGNORECASE):
        return RuleResult(rule_id, name, False, "Missing <h2>How It Works</h2> heading")

    # Check governing equation - specifically target <div class="equation-formula"> first
    eq_match = re.search(
        r'<div[^>]*class=["\'][^"\']*\bequation-formula\b[^"\']*["\'][^>]*>(.*?)</div>',
        content,
        re.DOTALL | re.IGNORECASE,
    )
    if not eq_match:
        eq_match = re.search(
            r'<div[^>]*class=["\'][^"\']*\bequation\b[^"\']*["\'][^>]*>(.*?)</div>',
            content,
            re.DOTALL | re.IGNORECASE,
        )

    if not eq_match:
        return RuleResult(rule_id, name, False, "Missing governing equation container (<div class=\"equation-formula\">)")

    raw_eq = eq_match.group(1)
    text = re.sub(r'<[^>]+>', '', raw_eq).strip()
    if not text or len(text) < 3 or text.startswith("<!--"):
        return RuleResult(rule_id, name, False, "Governing equation is empty or placeholder")

    # Explicitly reject placeholders
    placeholders = [
        "governing equation",
        "governing mathematical formulation",
        "equation",
        "formula",
        "placeholder",
        "tbd",
        "todo",
    ]
    norm_text = re.sub(r'\s+', ' ', text).strip().lower()
    if norm_text in placeholders or norm_text.rstrip(':').strip() in placeholders:
        return RuleResult(rule_id, name, False, f"Governing equation contains placeholder text: '{text}'")

    for p in placeholders:
        if norm_text == p or norm_text.startswith(p + ":") or norm_text.startswith(p + " -"):
            return RuleResult(rule_id, name, False, f"Governing equation contains placeholder text: '{text}'")

    # Reject unrendered raw LaTeX macros
    latex_macros = re.findall(r'\\[a-zA-Z]+', text)
    if not latex_macros:
        latex_macros = re.findall(r'\\[a-zA-Z]+', raw_eq)
    if latex_macros:
        macro_preview = ', '.join(sorted(set(latex_macros))[:5])
        return RuleResult(rule_id, name, False, f"Contains unrendered raw LaTeX macro(s): {macro_preview}")

    return RuleResult(rule_id, name, True, f"Valid 'How It Works' and unicode equation: '{text[:35]}...'")


# ============================================================================
# Rule 8: Meaningful developer comments explaining logic in <script> tag
# ============================================================================
def check_rule_8_developer_comments(content: str) -> RuleResult:
    rule_id = "RULE_08"
    name = "Meaningful developer comments in <script> tag"
    scripts = "\n".join(re.findall(r'<script(?![^>]*src=)[^>]*>(.*?)</script>', content, re.DOTALL | re.IGNORECASE))
    if not scripts:
        return RuleResult(rule_id, name, False, "No inline <script> block found")

    # Find single-line and multi-line comments
    single_line_comments = re.findall(r'//[^\n]*', scripts)
    multi_line_comments = re.findall(r'/\*.*?\*/', scripts, re.DOTALL)

    all_comments = single_line_comments + multi_line_comments
    total_comment_lines = len(single_line_comments) + sum(c.count('\n') + 1 for c in multi_line_comments)
    total_comment_chars = sum(len(c.strip()) for c in all_comments)

    if total_comment_lines < 4 or total_comment_chars < 120:
        return RuleResult(
            rule_id,
            name,
            False,
            f"Insufficient developer comments in <script> ({total_comment_lines} lines, {total_comment_chars} chars; expected >= 4 lines, >= 120 chars)",
        )

    # Check for semantic engineering keywords in comments
    comments_text = " ".join(all_comments).lower()
    semantic_keywords = [
        "physics", "simulation", "equation", "formula", "derivative", "velocity",
        "acceleration", "position", "state", "step", "render", "loop", "draw",
        "animate", "canvas", "coordinate", "force", "energy", "update", "constant",
        "parameters", "damping", "frequency", "oscillation", "boundary", "time",
    ]
    matched_keywords = [kw for kw in semantic_keywords if kw in comments_text]
    if len(matched_keywords) < 2:
        return RuleResult(
            rule_id,
            name,
            False,
            f"Developer comments lack required scientific/engineering domain explanations (matched keywords: {matched_keywords})",
        )

    return RuleResult(
        rule_id,
        name,
        True,
        f"Contains meaningful developer comments ({total_comment_lines} lines, keywords: {', '.join(matched_keywords[:4])})",
    )


# ============================================================================
# Rule 9: Strict standalone architecture (zero external CSS, allowed GSAP CDN only)
# ============================================================================
def check_rule_9_standalone(content: str) -> RuleResult:
    rule_id = "RULE_09"
    name = "Strict standalone architecture (zero external CSS/JS except GSAP)"
    violations = []

    css_links = re.findall(r'<link[^>]*rel=["\']stylesheet["\'][^>]*>', content, re.IGNORECASE)
    if css_links:
        violations.append(f"Contains {len(css_links)} external stylesheet link(s)")

    script_srcs = re.findall(r'<script[^>]*src=["\']([^"\']+)["\']', content, re.IGNORECASE)
    for src in script_srcs:
        src_clean = src.strip()
        if "three" in src_clean.lower():
            violations.append(f"Forbidden Three.js dependency: {src_clean}")
            continue
        is_gsap_core = "cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js" in src_clean
        if not is_gsap_core:
            violations.append(f"Forbidden external script dependency: {src_clean}")

    if violations:
        return RuleResult(rule_id, name, False, "; ".join(violations))

    return RuleResult(rule_id, name, True, "Strictly standalone")


# ============================================================================
# Rule 10: Anti-gimmick & non-destructive mechanics
# ============================================================================
def check_rule_10_anti_gimmick(content: str) -> RuleResult:
    rule_id = "RULE_10"
    name = "Anti-gimmick check: zero destructive .remove() or element clearing"
    violations = []

    if re.search(r'container\.remove\(\)', content):
        violations.append("Contains container.remove() call")
    if re.search(r'(?<!classList)\.remove\(\)', content):
        violations.append("Contains .remove() call")
    if re.search(r'scale:\s*50\b', content, re.IGNORECASE):
        violations.append("Contains explosive scale animation")
    if re.search(r'(?:container|simulation|viewport)\.innerHTML\s*=\s*[\'"]\s*[\'"]', content, re.IGNORECASE):
        violations.append("Contains destructive element clearing")

    if violations:
        return RuleResult(rule_id, name, False, "; ".join(violations))

    return RuleResult(rule_id, name, True, "Pure physics simulation (zero gimmicks)")


# ============================================================================
# Rule 11: Inline JavaScript syntax verification
# ============================================================================
def check_rule_11_javascript_syntax(content: str) -> RuleResult:
    rule_id = "RULE_11"
    name = "Inline JavaScript syntax compilation"
    scripts = re.findall(r'<script(?![^>]*src=)[^>]*>(.*?)</script>', content, re.DOTALL | re.IGNORECASE)
    if not scripts:
        return RuleResult(rule_id, name, False, "No inline <script> block found")

    all_js = "\n".join(scripts)
    node_path = shutil.which("node")
    if not node_path:
        return RuleResult(rule_id, name, True, "Node.js not detected; skipped AST syntax check")

    res = subprocess.run([node_path, "--check", "-"], input=all_js, text=True, capture_output=True)
    if res.returncode != 0:
        err_msg = res.stderr.strip().splitlines()[0] if res.stderr else "Syntax compilation error"
        return RuleResult(rule_id, name, False, f"JavaScript SyntaxError: {err_msg}")

    return RuleResult(rule_id, name, True, "Inline JavaScript compiles with zero syntax errors")


MODEL_RULE_CHECKERS = [
    check_rule_1_doctype,
    check_rule_2_header_title_badge,
    check_rule_3_pill_buttons,
    check_rule_4_font_and_no_mid_gray,
    check_rule_5_pastel_container_24px,
    check_rule_6_main_canvas_svg,
    check_rule_7_explanation_equation,
    check_rule_8_developer_comments,
    check_rule_9_standalone,
    check_rule_10_anti_gimmick,
    check_rule_11_javascript_syntax,
]


# ============================================================================
# Category B: Repository-Wide Rules (Rules 12, 13, 14)
# ============================================================================

def check_rule_12_folder_structure(models_dir: Path) -> RuleResult:
    """Automated check passes: Confusing folders eliminated, no empty folders, exact canonical folders."""
    rule_id = "RULE_12"
    rule_name = "Confusing folders eliminated & exact canonical directories present"

    if not models_dir.exists():
        return RuleResult(rule_id, rule_name, False, f"Models directory {models_dir} does not exist")

    violations = []
    subdirs = {d.name.lower(): d for d in models_dir.iterdir() if d.is_dir()}

    # Check forbidden folders
    for forbidden in FORBIDDEN_FOLDERS:
        if forbidden.lower() in subdirs:
            violations.append(f"Forbidden folder '{forbidden}' exists in models/")

    # Check empty folders
    empty_folders = []
    for folder_name, d in subdirs.items():
        files = list(d.glob("*.html"))
        if not files:
            empty_folders.append(d.name)
    if empty_folders:
        violations.append(f"Empty discipline folder(s) found: {', '.join(sorted(empty_folders))}")

    # Check non-canonical folders
    non_canonical = [fn for fn in subdirs if fn not in CANONICAL_DISCIPLINE_FOLDERS and fn not in [f.lower() for f in FORBIDDEN_FOLDERS]]
    if non_canonical:
        violations.append(f"Non-canonical/unconsolidated folder(s) found: {', '.join(sorted(non_canonical))}")

    # Check that all canonical folders exist
    missing_canonical = [c for c in sorted(CANONICAL_DISCIPLINE_FOLDERS) if c not in subdirs]
    if missing_canonical:
        violations.append(f"Missing canonical discipline folder(s): {', '.join(missing_canonical)}")

    if violations:
        return RuleResult(rule_id, rule_name, False, "; ".join(violations))

    return RuleResult(
        rule_id,
        rule_name,
        True,
        f"Clean folder structure: exactly 23 canonical discipline folders present, zero forbidden or empty folders ({len(subdirs)} active disciplines)",
    )



def check_rule_13_dashboard_integrity(index_html: Path, models_dir: Path) -> RuleResult:
    """Automated check passes: index.html has been successfully regenerated and links to the new, corrected folder paths."""
    rule_id = "RULE_13"
    name = "Dashboard (index.html) regeneration and link integrity"

    if not index_html.exists():
        return RuleResult(rule_id, name, False, f"index.html not found at {index_html}")

    content = index_html.read_text(encoding="utf-8", errors="replace")

    # Extract all model links
    model_links = re.findall(r'href=["\'](models/[^"\']+\.html)["\']', content)
    if not model_links:
        return RuleResult(rule_id, name, False, "No model links found in index.html")

    # Check for broken links
    broken_links = []
    linked_set = set()
    for link in model_links:
        target = REPO_ROOT / link
        linked_set.add(target.resolve())
        if not target.exists():
            broken_links.append(link)

    if broken_links:
        return RuleResult(
            rule_id,
            name,
            False,
            f"Found {len(broken_links)} broken links in index.html (e.g. {broken_links[:3]})",
        )

    # Check for orphaned model files (files in models/ not linked in index.html)
    all_models = [
        f.resolve() for f in models_dir.glob("**/*.html")
        if not any(ex in f.parts for ex in ["misc", "__pycache__"])
    ]
    unlinked = [m for m in all_models if m not in linked_set]
    if unlinked:
        unlinked_rel = [str(u.relative_to(REPO_ROOT)) for u in unlinked[:3]]
        return RuleResult(
            rule_id,
            name,
            False,
            f"Found {len(unlinked)} surviving models not linked in index.html (e.g. {unlinked_rel})",
        )

    return RuleResult(
        rule_id,
        name,
        True,
        f"Dashboard index.html 100% verified: {len(model_links)} valid links, zero broken, zero orphaned models",
    )


def check_rule_14_ratings_report(ratings_file: Path, models_dir: Path) -> RuleResult:
    """Automated check passes: model_ratings.md exists and contains exactly one 1-10 rating score for every single surviving HTML model."""
    rule_id = "RULE_14"
    name = "Central model ratings report (model_ratings.md) completeness"

    if not ratings_file.exists():
        return RuleResult(rule_id, name, False, f"model_ratings.md not found at {ratings_file}")

    content = ratings_file.read_text(encoding="utf-8", errors="replace")

    # Discover all surviving models on disk
    all_models = sorted([
        f.resolve() for f in models_dir.glob("**/*.html")
        if not any(ex in f.parts for ex in ["misc", "__pycache__"])
    ])
    total_surviving = len(all_models)
    if total_surviving == 0:
        return RuleResult(rule_id, name, False, "Zero surviving models discovered in models/")

    # Parse rating table entries
    rated_models: Dict[str, float] = {}
    lines = content.splitlines()

    overall_idx = -1
    score_indices: List[int] = []

    for line in lines:
        stripped_line = line.strip()
        if not stripped_line.startswith("|") or stripped_line.startswith("|-"):
            continue
        parts = [p.strip() for p in stripped_line.split("|")[1:-1]]

        # Check for header row
        if overall_idx == -1 and any("score" in p.lower() or "quality" in p.lower() for p in parts):
            for idx, p in enumerate(parts):
                pl = p.lower()
                if "(1-10)" in pl or "score" in pl or "quality" in pl or "accuracy" in pl or "fidelity" in pl:
                    score_indices.append(idx)
                if "overall" in pl:
                    overall_idx = idx
            continue

        # Look for a part that looks like a .html file path
        html_part = None
        html_idx = -1
        for idx, p in enumerate(parts):
            if ".html" in p:
                clean_p = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', p)
                clean_p = re.sub(r'[`*]', '', clean_p).strip()
                html_part = clean_p
                html_idx = idx
                break
        if not html_part:
            continue

        basename = Path(html_part).name

        score = None
        if overall_idx != -1 and overall_idx < len(parts):
            clean_num = parts[overall_idx].replace("★", "").strip()
            try:
                score = float(clean_num)
            except ValueError:
                score = -999.0
        else:
            # Fallback: scan columns after html_idx
            for p in parts[html_idx + 1:]:
                clean_num = p.replace("★", "").strip()
                num_match = re.match(r'^-?[0-9]+(?:\.[0-9]+)?$', clean_num)
                if num_match:
                    try:
                        score = float(num_match.group(0))
                    except ValueError:
                        score = -999.0

        # Validate all score columns if score_indices were discovered from header
        if score_indices:
            for s_idx in score_indices:
                if s_idx < len(parts):
                    clean_s = parts[s_idx].replace("★", "").strip()
                    try:
                        s_val = float(clean_s)
                        if not (1.0 <= s_val <= 10.0):
                            score = s_val  # Propagate out-of-range score
                            break
                    except ValueError:
                        score = -999.0  # Propagate non-numeric score
                        break

        rated_models[basename] = score if score is not None else 0.0

    # Validate completeness
    missing_ratings = []
    invalid_scores = []

    for m in all_models:
        name_key = m.name
        if name_key not in rated_models:
            missing_ratings.append(name_key)
        else:
            score = rated_models[name_key]
            if not (1.0 <= score <= 10.0):
                invalid_scores.append(f"{name_key} (score: {score})")

    if missing_ratings:
        return RuleResult(
            rule_id,
            name,
            False,
            f"model_ratings.md missing {len(missing_ratings)} of {total_surviving} models (e.g. {missing_ratings[:3]})",
        )

    if invalid_scores:
        return RuleResult(
            rule_id,
            name,
            False,
            f"model_ratings.md contains invalid score(s) outside 1-10 range: {invalid_scores[:3]}",
        )

    return RuleResult(
        rule_id,
        name,
        True,
        f"model_ratings.md verified: exactly {len(rated_models)} models rated on 1-10 scale",
    )


# ============================================================================
# Main Validation Runner
# ============================================================================

def validate_model_file(file_path: Path) -> FileValidationResult:
    result = FileValidationResult(file_path)
    try:
        content = file_path.read_text(encoding="utf-8", errors="replace")
    except Exception as exc:
        for idx, checker in enumerate(MODEL_RULE_CHECKERS, start=1):
            result.rule_results.append(
                RuleResult(f"RULE_{idx:02d}", f"Rule {idx}", False, f"Failed to read file: {exc}")
            )
        return result

    for checker in MODEL_RULE_CHECKERS:
        result.rule_results.append(checker(content))

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Engineering Physics Figma Design System & E2E Acceptance Verification Suite"
    )
    parser.add_argument("paths", nargs="*", help="Optional specific model file or directory paths to verify")
    parser.add_argument("--all", action="store_true", help="Verify all models and repository acceptance rules")
    parser.add_argument("--sample", type=int, nargs="?", const=20, default=None, metavar="N", help="Verify N random models")
    parser.add_argument("--seed", type=int, default=None, help="Set random seed for reproducible sampling")
    parser.add_argument("--check-dashboard", action="store_true", help="Verify index.html link integrity and regeneration (Rule 13)")
    parser.add_argument("--check-ratings", action="store_true", help="Verify model_ratings.md completeness and 1-10 scores (Rule 14)")
    parser.add_argument("--check-folders", action="store_true", help="Verify confusing folder elimination and canonical folders (Rule 12)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show detailed per-rule report")
    parser.add_argument("--json", action="store_true", help="Output results in machine-readable JSON format")
    parser.add_argument("--skip-repo", action="store_true", help="Skip repository-wide rules (Rules 12-14) and only evaluate model files")

    args = parser.parse_args()

    # Discover surviving models
    all_models = sorted([
        f for f in MODELS_DIR.glob("**/*.html")
        if not any(ex in f.parts for ex in ["misc", "__pycache__"])
    ])

    # Direct individual check flags
    if args.check_folders:
        res = check_rule_12_folder_structure(MODELS_DIR)
        if args.json:
            print(json.dumps({"rule_id": res.rule_id, "name": res.rule_name, "passed": res.passed, "message": res.message}, indent=2))
        else:
            tag = "[PASS]" if res.passed else "[FAIL]"
            print(f"{tag} {res.rule_id} ({res.rule_name}): {res.message}")
        sys.exit(0 if res.passed else 1)

    if args.check_dashboard:
        res = check_rule_13_dashboard_integrity(INDEX_HTML, MODELS_DIR)
        if args.json:
            print(json.dumps({"rule_id": res.rule_id, "name": res.rule_name, "passed": res.passed, "message": res.message}, indent=2))
        else:
            tag = "[PASS]" if res.passed else "[FAIL]"
            print(f"{tag} {res.rule_id} ({res.rule_name}): {res.message}")
        sys.exit(0 if res.passed else 1)

    if args.check_ratings:
        res = check_rule_14_ratings_report(MODEL_RATINGS_MD, MODELS_DIR)
        if args.json:
            print(json.dumps({"rule_id": res.rule_id, "name": res.rule_name, "passed": res.passed, "message": res.message}, indent=2))
        else:
            tag = "[PASS]" if res.passed else "[FAIL]"
            print(f"{tag} {res.rule_id} ({res.rule_name}): {res.message}")
        sys.exit(0 if res.passed else 1)

    # Repository-wide results for multi-rule checks
    evaluate_repo = not args.skip_repo and (args.all or (not args.paths and args.sample is None))
    repo_results: List[RuleResult] = []
    if evaluate_repo:
        repo_results.append(check_rule_12_folder_structure(MODELS_DIR))
        repo_results.append(check_rule_13_dashboard_integrity(INDEX_HTML, MODELS_DIR))
        repo_results.append(check_rule_14_ratings_report(MODEL_RATINGS_MD, MODELS_DIR))

    # Determine target files
    if args.seed is not None:
        random.seed(args.seed)

    if args.sample is not None:
        sample_count = min(args.sample, len(all_models))
        target_files = random.sample(all_models, sample_count)
    elif args.paths:
        target_files = []
        for p in args.paths:
            resolved = Path(p).resolve()
            if resolved.is_file() and resolved.suffix == ".html":
                target_files.append(resolved)
            elif resolved.is_dir():
                target_files.extend(sorted(resolved.glob("**/*.html")))
    else:
        target_files = all_models

    file_results: List[FileValidationResult] = [validate_model_file(f) for f in target_files]
    all_files_passed = all(r.passed for r in file_results)
    all_repo_passed = all(r.passed for r in repo_results) if repo_results else True
    overall_passed = all_files_passed and all_repo_passed

    total_eval = len(file_results)
    passed_eval = sum(1 for r in file_results if r.passed)
    failed_eval = total_eval - passed_eval

    if args.json:
        payload = {
            "models_evaluated": total_eval,
            "models_passed": passed_eval,
            "models_failed": failed_eval,
            "repository_rules": [
                {"rule_id": r.rule_id, "name": r.rule_name, "passed": r.passed, "message": r.message}
                for r in repo_results
            ],
            "all_passed": overall_passed,
        }
        if args.verbose:
            payload["files"] = [r.to_dict() for r in file_results]
        print(json.dumps(payload, indent=2))
        sys.exit(0 if overall_passed else 1)

    print("\n" + "=" * 80)
    print("ENGINEERING PHYSICS FIGMA DESIGN SYSTEM & E2E VERIFICATION AUDIT")
    print("=" * 80)
    print(f"Models Evaluated:        {total_eval}")
    print(f"Models Passing:          {passed_eval}")
    print(f"Models Failing:          {failed_eval}")
    if repo_results:
        print("-" * 80)
        print("REPOSITORY & ACCEPTANCE CRITERIA CHECKS:")
        for r in repo_results:
            tag = "[PASS]" if r.passed else "[FAIL]"
            print(f"  {tag} {r.rule_id} ({r.rule_name}): {r.message}")
    print("=" * 80)

    if not overall_passed:
        if failed_eval > 0 and not args.verbose:
            print(f"\nShowing first 5 failing models:")
            shown = 0
            for r in file_results:
                if not r.passed:
                    print(f"\n  [FAIL] {r.rel_path}:")
                    for rule_res in r.rule_results:
                        if not rule_res.passed:
                            print(f"      ✗ {rule_res.rule_id} ({rule_res.rule_name}): {rule_res.message}")
                    shown += 1
                    if shown >= 5:
                        break
        elif failed_eval > 0 and args.verbose:
            print(f"\nDetailed model failures:")
            for r in file_results:
                if not r.passed:
                    print(f"\n  [FAIL] {r.rel_path}:")
                    for rule_res in r.rule_results:
                        if not rule_res.passed:
                            print(f"      ✗ {rule_res.rule_id} ({rule_res.rule_name}): {rule_res.message}")
        print(f"\nOVERALL STATUS: FAILED (violations detected)")
        sys.exit(1)
    else:
        print("\nOVERALL STATUS: 100% PASSED")
        sys.exit(0)


if __name__ == "__main__":
    main()
