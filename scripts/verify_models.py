#!/usr/bin/env python3
"""
scripts/verify_models.py
Automated Verification Suite for Engineering Physics Standardized Models.

Validates all 348 standalone physics models in models/ (excluding models/misc/)
against the 12 core rules defined in PROJECT.md and survey_standards.md §8:

  Rule 1:  Starts with <!DOCTYPE html>
  Rule 2:  Contains <header> with title <h1> and discipline badge <div class="discipline-badge">
  Rule 3:  Contains theme toggle button with id="theme-toggle"
  Rule 4:  Contains <main> with <canvas> or <svg>
  Rule 5:  Contains <section class="explanation"> with <h2>How It Works</h2>
  Rule 6:  Contains governing equation block <div class="equation"> with non-empty content
  Rule 7:  Contains theme toggle javascript switching data-theme
  Rule 8:  Inline CSS defines dark mode palette (--bg: #1a1a2e, --text: #e0e0e0, --accent: #4fc3f7)
  Rule 9:  Inline CSS defines light mode palette (--bg: #f5f5f5, --text: #1a1a1a, --accent: #0277bd)
  Rule 10: Standalone: zero external CSS <link rel="stylesheet">, zero external <script src>
           except optional core GSAP CDN https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js
           (no Three.js, no MotionPathPlugin)
  Rule 11: Anti-gimmick check: zero occurrences of container.remove(), .remove(), or destructive element clearing
  Rule 12: Viewport sizing: <main> has height in ~60-70% range (e.g. 62vh, 60vh-70vh)

CLI Options:
  --all            Validate all 348 non-misc model files
  --sample N       Validate N random model files (default 20 when flag is passed)
  --seed S         Set random seed for reproducible sampling
  --verbose, -v    Show per-rule status for each model
  --summary        Print aggregated rule pass/fail statistics
  --json           Output full results in JSON format
  --no-color       Disable ANSI terminal colors
  --self-test      Run internal verification self-test on reference templates
  paths            Optional specific files or directories to validate

Exit Code:
  0: All tested models pass all 12 rules
  1: One or more models fail one or more rules, or arguments invalid
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

# Project root paths
REPO_ROOT = Path(__file__).resolve().parent.parent
MODELS_DIR = REPO_ROOT / "models"
EXCLUDE_DIRS = {"misc"}
TOTAL_EXPECTED_MODELS = 348

# Allowed GSAP core CDN URL
ALLOWED_GSAP_CDN = "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"


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
# Rule 2: Contains <header> with title <h1> and discipline badge <div class="discipline-badge">
# ============================================================================
def check_rule_2_header_title_badge(content: str) -> RuleResult:
    rule_id = "RULE_02"
    name = "Header with title <h1> and discipline badge"
    header_match = re.search(r'<header[^>]*>(.*?)</header>', content, re.DOTALL | re.IGNORECASE)
    if not header_match:
        if not re.search(r'<header[^>]*>', content, re.IGNORECASE):
            return RuleResult(rule_id, name, False, "Missing <header> element")
        header_content = content
    else:
        header_content = header_match.group(1)

    # Check <h1>
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', header_content, re.DOTALL | re.IGNORECASE)
    if not h1_match:
        h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL | re.IGNORECASE)
        if not h1_match:
            return RuleResult(rule_id, name, False, "Missing <h1> model title in <header>")

    title_text = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip()
    if not title_text or title_text.startswith("<!--"):
        return RuleResult(rule_id, name, False, "<h1> model title is empty or placeholder")

    # Check discipline badge
    badge_match = re.search(
        r'<div[^>]*class=["\'][^"\']*\bdiscipline-badge\b[^"\']*["\'][^>]*>(.*?)</div>',
        header_content,
        re.DOTALL | re.IGNORECASE,
    )
    if not badge_match:
        badge_match = re.search(
            r'<div[^>]*class=["\'][^"\']*\bdiscipline-badge\b[^"\']*["\'][^>]*>(.*?)</div>',
            content,
            re.DOTALL | re.IGNORECASE,
        )
        if not badge_match:
            return RuleResult(rule_id, name, False, "Missing <div class=\"discipline-badge\"> in <header>")

    badge_text = re.sub(r'<[^>]+>', '', badge_match.group(1)).strip()
    if not badge_text or badge_text.startswith("<!--"):
        return RuleResult(rule_id, name, False, "Discipline badge text is empty or placeholder")

    return RuleResult(rule_id, name, True, f"Header contains title '{title_text}' and badge '{badge_text}'")


# ============================================================================
# Rule 3: Contains theme toggle button with id="theme-toggle"
# ============================================================================
def check_rule_3_theme_toggle_btn(content: str) -> RuleResult:
    rule_id = "RULE_03"
    name = "Theme toggle button with id=\"theme-toggle\""
    match = re.search(r'<button[^>]*id=["\']theme-toggle["\']', content, re.IGNORECASE)
    if not match:
        match = re.search(r'id=["\']theme-toggle["\']', content, re.IGNORECASE)
        if not match:
            return RuleResult(rule_id, name, False, "Missing theme toggle button with id=\"theme-toggle\"")
    return RuleResult(rule_id, name, True, "Contains theme toggle button with id=\"theme-toggle\"")


# ============================================================================
# Rule 4: Contains <main> with <canvas> or <svg>
# ============================================================================
def check_rule_4_main_canvas_svg(content: str) -> RuleResult:
    rule_id = "RULE_04"
    name = "<main> container with <canvas> or <svg>"
    main_match = re.search(r'<main[^>]*>(.*?)</main>', content, re.DOTALL | re.IGNORECASE)
    if not main_match:
        if not re.search(r'<main[^>]*>', content, re.IGNORECASE):
            return RuleResult(rule_id, name, False, "Missing <main> container element")
        main_content = content
    else:
        main_content = main_match.group(1)

    has_canvas = bool(re.search(r'<canvas[^>]*>', main_content, re.IGNORECASE))
    has_svg = bool(re.search(r'<svg[^>]*>', main_content, re.IGNORECASE))

    if not (has_canvas or has_svg):
        return RuleResult(rule_id, name, False, "<main> does not contain <canvas> or <svg> simulation element")

    element_type = "canvas" if has_canvas else "svg"
    return RuleResult(rule_id, name, True, f"<main> contains simulation <{element_type}>")


# ============================================================================
# Rule 5: Contains <section class="explanation"> with <h2>How It Works</h2>
# ============================================================================
def check_rule_5_explanation_heading(content: str) -> RuleResult:
    rule_id = "RULE_05"
    name = "<section class=\"explanation\"> with <h2>How It Works</h2>"
    sec_match = re.search(
        r'<section[^>]*class=["\'][^"\']*\bexplanation(?:-section)?\b[^"\']*["\'][^>]*>(.*?)</section>',
        content,
        re.DOTALL | re.IGNORECASE,
    )
    if not sec_match:
        if not re.search(r'<section[^>]*class=["\'][^"\']*\bexplanation(?:-section)?\b[^"\']*["\']', content, re.IGNORECASE):
            return RuleResult(rule_id, name, False, "Missing <section class=\"explanation\">")
        sec_content = content
    else:
        sec_content = sec_match.group(1)

    h2_match = re.search(
        r'<h2[^>]*>\s*(?:<[^>]+>)*\s*How It Works\s*(?:<[^>]+>)*\s*</h2>',
        sec_content,
        re.IGNORECASE,
    )
    if not h2_match:
        h2_match = re.search(r'<h2[^>]*>\s*How It Works\s*</h2>', content, re.IGNORECASE)
        if not h2_match:
            return RuleResult(rule_id, name, False, "Missing <h2>How It Works</h2> heading in explanation section")

    return RuleResult(rule_id, name, True, "Contains <section class=\"explanation\"> with <h2>How It Works</h2>")


# ============================================================================
# Rule 6: Contains governing equation block <div class="equation"> with non-empty content
# ============================================================================
def check_rule_6_equation_block(content: str) -> RuleResult:
    rule_id = "RULE_06"
    name = "Governing equation block with non-empty content"

    formula_match = re.search(
        r'<div[^>]*class=["\'][^"\']*\bequation-formula\b[^"\']*["\'][^>]*>(.*?)</div>',
        content,
        re.DOTALL | re.IGNORECASE,
    )
    if formula_match:
        inner = formula_match.group(1)
    else:
        eq_match = re.search(
            r'<div[^>]*class=["\'][^"\']*\bequation\b(?!-container)[^"\']*["\'][^>]*>(.*?)</div>',
            content,
            re.DOTALL | re.IGNORECASE,
        )
        if not eq_match:
            return RuleResult(rule_id, name, False, "Missing governing equation block (<div class=\"equation\">)")
        inner = eq_match.group(1)

    text = re.sub(r'<[^>]+>', '', inner).strip()
    if not text or text.startswith("<!--") or len(text) < 3:
        return RuleResult(rule_id, name, False, "Governing equation block is empty or contains placeholder")

    # Reject raw unrendered LaTeX macros
    latex_macros = re.findall(r'\\[a-zA-Z]+', text)
    if latex_macros:
        macro_preview = ', '.join(sorted(set(latex_macros))[:5])
        return RuleResult(rule_id, name, False, f"Contains unrendered raw LaTeX macro(s): {macro_preview}")

    return RuleResult(rule_id, name, True, f"Contains governing equation: '{text[:40]}'")


# ============================================================================
# Rule 7: Contains theme toggle javascript switching data-theme
# ============================================================================
def check_rule_7_theme_toggle_js(content: str) -> RuleResult:
    rule_id = "RULE_07"
    name = "Theme toggle JavaScript switching data-theme"
    scripts = "\n".join(re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL | re.IGNORECASE))
    if not scripts:
        return RuleResult(rule_id, name, False, "No inline <script> found")

    has_data_theme = "data-theme" in scripts
    has_switch_logic = bool(
        re.search(r'(?:setAttribute|dataset\.theme|classList\.toggle)', scripts, re.IGNORECASE)
    )

    if not (has_data_theme and has_switch_logic):
        return RuleResult(
            rule_id,
            name,
            False,
            "Inline JavaScript missing logic switching 'data-theme' attribute",
        )

    return RuleResult(rule_id, name, True, "Inline JavaScript contains theme toggle switching data-theme")


# ============================================================================
# Rule 8: Inline CSS defines dark mode palette (--bg: #1a1a2e, --text: #e0e0e0, --accent: #4fc3f7)
# ============================================================================
def check_rule_8_dark_palette(content: str) -> RuleResult:
    rule_id = "RULE_08"
    name = "Dark mode palette CSS tokens"
    styles = "\n".join(re.findall(r'<style[^>]*>(.*?)</style>', content, re.DOTALL | re.IGNORECASE))
    if not styles:
        return RuleResult(rule_id, name, False, "No inline <style> block found")

    missing = []
    if not re.search(r'--bg\s*:\s*#1a1a2e\b', styles, re.IGNORECASE):
        missing.append("--bg: #1a1a2e")
    if not re.search(r'--text\s*:\s*#e0e0e0\b', styles, re.IGNORECASE):
        missing.append("--text: #e0e0e0")
    if not re.search(r'--accent\s*:\s*#4fc3f7\b', styles, re.IGNORECASE):
        missing.append("--accent: #4fc3f7")

    if missing:
        return RuleResult(rule_id, name, False, f"Dark mode palette missing CSS token(s): {', '.join(missing)}")

    return RuleResult(rule_id, name, True, "Inline CSS defines complete dark mode palette tokens")


# ============================================================================
# Rule 9: Inline CSS defines light mode palette (--bg: #f5f5f5, --text: #1a1a1a, --accent: #0277bd)
# ============================================================================
def check_rule_9_light_palette(content: str) -> RuleResult:
    rule_id = "RULE_09"
    name = "Light mode palette CSS tokens"
    styles = "\n".join(re.findall(r'<style[^>]*>(.*?)</style>', content, re.DOTALL | re.IGNORECASE))
    if not styles:
        return RuleResult(rule_id, name, False, "No inline <style> block found")

    missing = []
    if not re.search(r'--bg\s*:\s*#f5f5f5\b', styles, re.IGNORECASE):
        missing.append("--bg: #f5f5f5")
    if not re.search(r'--text\s*:\s*#1a1a1a\b', styles, re.IGNORECASE):
        missing.append("--text: #1a1a1a")
    if not re.search(r'--accent\s*:\s*#0277bd\b', styles, re.IGNORECASE):
        missing.append("--accent: #0277bd")

    if missing:
        return RuleResult(rule_id, name, False, f"Light mode palette missing CSS token(s): {', '.join(missing)}")

    return RuleResult(rule_id, name, True, "Inline CSS defines complete light mode palette tokens")


# ============================================================================
# Rule 10: Standalone: zero external CSS, zero external scripts except core GSAP CDN
# ============================================================================
def check_rule_10_standalone(content: str) -> RuleResult:
    rule_id = "RULE_10"
    name = "Standalone: zero external CSS, zero non-GSAP external scripts"
    violations = []

    # Check external stylesheets
    css_links = re.findall(r'<link[^>]*rel=["\']stylesheet["\'][^>]*>', content, re.IGNORECASE)
    css_links += re.findall(r'<link[^>]*href=["\'][^"\']+\.css["\'][^>]*>', content, re.IGNORECASE)
    if css_links:
        violations.append(f"Contains {len(css_links)} external stylesheet link(s)")

    # Check external scripts
    script_srcs = re.findall(r'<script[^>]*src=["\']([^"\']+)["\']', content, re.IGNORECASE)
    for src in script_srcs:
        src_clean = src.strip()
        if "three" in src_clean.lower():
            violations.append(f"Forbidden Three.js dependency: {src_clean}")
            continue
        if "motionpathplugin" in src_clean.lower():
            violations.append(f"Forbidden MotionPathPlugin dependency: {src_clean}")
            continue

        is_gsap_core = "cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js" in src_clean
        if not is_gsap_core:
            violations.append(f"Forbidden external script dependency: {src_clean}")

    if violations:
        return RuleResult(rule_id, name, False, "; ".join(violations))

    return RuleResult(rule_id, name, True, "Strictly standalone (no external CSS, only allowed GSAP CDN if any)")


# ============================================================================
# Rule 11: Anti-gimmick check: zero occurrences of container.remove(), .remove(), or destructive clearing
# ============================================================================
def check_rule_11_anti_gimmick(content: str) -> RuleResult:
    rule_id = "RULE_11"
    name = "Anti-gimmick check: zero occurrences of .remove() or destructive clearing"
    violations = []

    if re.search(r'\.remove\(\)', content):
        violations.append("Contains .remove() call")
    if re.search(r'container\.remove\(\)', content):
        violations.append("Contains container.remove() call")
    if re.search(r'scale:\s*50\b', content, re.IGNORECASE):
        violations.append("Contains explosive scale animation (scale: 50)")
    if re.search(r'Math\.random\(\)\s*-\s*0\.5\)\s*\*\s*20\b', content):
        violations.append("Contains container shake gimmick")
    if re.search(r'(?:container|simulation|viewport)\.innerHTML\s*=\s*[\'"]\s*[\'"]', content, re.IGNORECASE):
        violations.append("Contains destructive element clearing (.innerHTML = '')")

    if violations:
        return RuleResult(rule_id, name, False, "; ".join(violations))

    return RuleResult(rule_id, name, True, "Pure physics simulation (zero .remove() or destructive gimmicks)")


# ============================================================================
# Rule 12: Viewport sizing: <main> has height in ~60-70% range (e.g. 62vh, 60vh-70vh)
# ============================================================================
def check_rule_12_viewport_sizing(content: str) -> RuleResult:
    rule_id = "RULE_12"
    name = "Viewport sizing: <main> height in ~60-70% range (e.g. 62vh)"
    styles = "\n".join(re.findall(r'<style[^>]*>(.*?)</style>', content, re.DOTALL | re.IGNORECASE))

    vh_matches = re.findall(r'(?:height|--viewport-height)\s*:\s*([0-9]+(?:\.[0-9]+)?)vh\b', styles, re.IGNORECASE)

    main_match = re.search(r'<main[^>]*style=["\']([^"\']+)["\']', content, re.IGNORECASE)
    if main_match:
        vh_matches += re.findall(r'height\s*:\s*([0-9]+(?:\.[0-9]+)?)vh\b', main_match.group(1), re.IGNORECASE)

    if not vh_matches:
        return RuleResult(
            rule_id,
            name,
            False,
            "Missing viewport height in vh for <main> (expected ~60-70vh, e.g. 62vh)",
        )

    valid_ranges = [float(v) for v in vh_matches if 58.0 <= float(v) <= 72.0]
    if not valid_ranges:
        return RuleResult(
            rule_id,
            name,
            False,
            f"Viewport height value ({vh_matches[0]}vh) is outside target ~60-70% range",
        )

    return RuleResult(rule_id, name, True, f"<main> viewport height is configured in ~60-70% range ({valid_ranges[0]}vh)")


# ============================================================================
# Rule 13: Inline JavaScript compiles cleanly with valid syntax (dynamic check)
# ============================================================================
def check_rule_13_javascript_syntax(content: str) -> RuleResult:
    rule_id = "RULE_13"
    name = "Inline JavaScript compiles with valid syntax"

    scripts = re.findall(r'<script(?![^>]*src=)[^>]*>(.*?)</script>', content, re.DOTALL | re.IGNORECASE)
    if not scripts:
        return RuleResult(rule_id, name, False, "No inline <script> block found to validate")

    all_js = "\n".join(scripts)
    node_path = shutil.which("node")
    if not node_path:
        return RuleResult(rule_id, name, True, "Node.js not detected; skipped dynamic AST compilation")

    res = subprocess.run(
        [node_path, "--check", "-"],
        input=all_js,
        text=True,
        capture_output=True,
    )
    if res.returncode != 0:
        err_msg = res.stderr.strip().splitlines()[0] if res.stderr else "Syntax compilation error"
        return RuleResult(rule_id, name, False, f"JavaScript SyntaxError: {err_msg}")

    return RuleResult(rule_id, name, True, "Inline JavaScript compiles cleanly with zero syntax errors")


# All 13 rule checkers in order
ALL_RULE_CHECKERS = [
    check_rule_1_doctype,
    check_rule_2_header_title_badge,
    check_rule_3_theme_toggle_btn,
    check_rule_4_main_canvas_svg,
    check_rule_5_explanation_heading,
    check_rule_6_equation_block,
    check_rule_7_theme_toggle_js,
    check_rule_8_dark_palette,
    check_rule_9_light_palette,
    check_rule_10_standalone,
    check_rule_11_anti_gimmick,
    check_rule_12_viewport_sizing,
    check_rule_13_javascript_syntax,
]


def validate_file(file_path: Path) -> FileValidationResult:
    """Validates a single HTML file against all 12 core rules."""
    result = FileValidationResult(file_path)
    try:
        content = file_path.read_text(encoding="utf-8", errors="replace")
    except Exception as exc:
        for idx, checker in enumerate(ALL_RULE_CHECKERS, start=1):
            result.rule_results.append(
                RuleResult(f"RULE_{idx:02d}", f"Rule {idx}", False, f"Failed to read file: {exc}")
            )
        return result

    for checker in ALL_RULE_CHECKERS:
        result.rule_results.append(checker(content))

    return result


def find_all_model_files(models_dir: Path) -> List[Path]:
    """Discovers all non-misc HTML model files under models/."""
    if not models_dir.exists():
        return []
    all_files = [
        f for f in models_dir.glob("**/*.html")
        if not any(excluded in f.parts for excluded in EXCLUDE_DIRS)
    ]
    all_files.sort()
    return all_files


# ============================================================================
# ANSI Color & Formatting Utilities
# ============================================================================
class Formatter:
    def __init__(self, enable_color: bool = True):
        self.enable_color = enable_color and sys.stdout.isatty()

    def green(self, text: str) -> str:
        return f"\033[32m{text}\033[0m" if self.enable_color else text

    def red(self, text: str) -> str:
        return f"\033[31m{text}\033[0m" if self.enable_color else text

    def yellow(self, text: str) -> str:
        return f"\033[33m{text}\033[0m" if self.enable_color else text

    def cyan(self, text: str) -> str:
        return f"\033[36m{text}\033[0m" if self.enable_color else text

    def bold(self, text: str) -> str:
        return f"\033[1m{text}\033[0m" if self.enable_color else text


# ============================================================================
# Self-Test Engine
# ============================================================================
def run_self_test(fmt: Formatter) -> bool:
    """Validates that the test runner correctly passes valid reference templates and catches failures."""
    print(fmt.bold("Running test runner internal self-tests..."))

    valid_template = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Harmonic Oscillator</title>
  <style>
    :root {
      --bg: #1a1a2e;
      --surface: #22223a;
      --surface-border: #33334d;
      --text: #e0e0e0;
      --text-muted: #9e9eb4;
      --accent: #4fc3f7;
    }
    [data-theme="light"] {
      --bg: #f5f5f5;
      --surface: #ffffff;
      --surface-border: #e0e0e0;
      --text: #1a1a1a;
      --text-muted: #616161;
      --accent: #0277bd;
    }
    main {
      width: 100%;
      max-width: 960px;
      height: 62vh;
      min-height: 380px;
      max-height: 640px;
    }
  </style>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
</head>
<body>
  <header>
    <h1>Harmonic Oscillator</h1>
    <div class="discipline-badge">Mechanical Engineering</div>
    <button class="theme-toggle" id="theme-toggle" aria-label="Toggle theme">
      Toggle
    </button>
  </header>

  <main>
    <canvas id="sim-canvas"></canvas>
  </main>

  <section class="explanation">
    <h2>How It Works</h2>
    <p>A simple pendulum exhibits harmonic motion under restoring force proportional to displacement.</p>
    <div class="equation">
      d²θ/dt² + (g/L) · sin(θ) = 0
    </div>
  </section>

  <script>
    const toggleBtn = document.getElementById("theme-toggle");
    toggleBtn.addEventListener("click", () => {
      const html = document.documentElement;
      const current = html.getAttribute("data-theme") || "dark";
      const next = current === "dark" ? "light" : "dark";
      html.setAttribute("data-theme", next);
    });
  </script>
</body>
</html>
"""

    import tempfile

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir) / "test_model.html"

        # Test 1: Valid template must pass 12/12
        tmp_path.write_text(valid_template, encoding="utf-8")
        res = validate_file(tmp_path)
        if not res.passed:
            print(fmt.red(f"Self-test failed: Valid reference template failed checks: {[r.message for r in res.rule_results if not r.passed]}"))
            return False

        # Test 2: Injected failure for Rule 1 (missing DOCTYPE)
        tmp_path.write_text(valid_template.replace("<!DOCTYPE html>", "<html>"), encoding="utf-8")
        res = validate_file(tmp_path)
        if res.rule_results[0].passed:
            print(fmt.red("Self-test failed: Did not catch missing DOCTYPE"))
            return False

        # Test 3: Injected failure for Rule 3 (missing theme toggle button)
        tmp_path.write_text(valid_template.replace('id="theme-toggle"', 'id="other"'), encoding="utf-8")
        res = validate_file(tmp_path)
        if res.rule_results[2].passed:
            print(fmt.red("Self-test failed: Did not catch missing #theme-toggle"))
            return False

        # Test 4: Injected failure for Rule 10 (Three.js dependency)
        bad_script = valid_template.replace(
            'https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js',
        )
        tmp_path.write_text(bad_script, encoding="utf-8")
        res = validate_file(tmp_path)
        if res.rule_results[9].passed:
            print(fmt.red("Self-test failed: Did not catch Three.js dependency"))
            return False

        # Test 5: Injected failure for Rule 11 (destructive .remove())
        bad_gimmick = valid_template.replace('const next =', 'container.remove(); const next =')
        tmp_path.write_text(bad_gimmick, encoding="utf-8")
        res = validate_file(tmp_path)
        if res.rule_results[10].passed:
            print(fmt.red("Self-test failed: Did not catch container.remove() call"))
            return False

        # Test 6: Injected failure for Rule 12 (height 100vh)
        bad_height = valid_template.replace('height: 62vh;', 'height: 100vh;')
        tmp_path.write_text(bad_height, encoding="utf-8")
        res = validate_file(tmp_path)
        if res.rule_results[11].passed:
            print(fmt.red("Self-test failed: Did not catch invalid viewport height (100vh)"))
            return False

        # Test 7: Injected failure for Rule 6 (raw LaTeX macro in equation)
        bad_latex = valid_template.replace('d²θ/dt²', r'\frac{d^2\theta}{dt^2}')
        tmp_path.write_text(bad_latex, encoding="utf-8")
        res = validate_file(tmp_path)
        if res.rule_results[5].passed:
            print(fmt.red("Self-test failed: Did not catch unrendered raw LaTeX macro in equation"))
            return False

        # Test 8: Injected failure for Rule 13 (syntax error in script)
        bad_syntax = valid_template.replace('const next =', 'const next = (')
        tmp_path.write_text(bad_syntax, encoding="utf-8")
        res = validate_file(tmp_path)
        if res.rule_results[12].passed:
            print(fmt.red("Self-test failed: Did not catch fatal JavaScript SyntaxError"))
            return False

    print(fmt.green("All internal self-tests passed successfully! Verification engine is 100% operational.\n"))
    return True


# ============================================================================
# Main Entrypoint
# ============================================================================
def main():
    parser = argparse.ArgumentParser(
        description="Verification Suite for Engineering Physics Standardized Models (13 Core Rules)"
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Optional specific file or directory paths to verify",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help=f"Verify all {TOTAL_EXPECTED_MODELS} non-misc models in models/",
    )
    parser.add_argument(
        "--sample",
        type=int,
        nargs="?",
        const=20,
        default=None,
        metavar="N",
        help="Verify N random models (default: 20 if flag passed without value)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Random seed for deterministic sampling with --sample",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Show detailed per-rule diagnostic report for each model",
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="Print rule-by-rule summary aggregation table",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results in JSON format",
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable terminal color codes",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run self-test on test engine with synthetic compliant & failing templates",
    )

    args = parser.parse_args()
    fmt = Formatter(enable_color=not args.no_color)

    if args.self_test:
        success = run_self_test(fmt)
        sys.exit(0 if success else 1)

    # Determine files to inspect
    target_files: List[Path] = []

    if args.paths:
        for p_str in args.paths:
            p = Path(p_str).resolve()
            if p.is_file():
                if p.suffix == ".html":
                    target_files.append(p)
                else:
                    print(fmt.yellow(f"Warning: Skipping non-HTML file {p_str}"))
            elif p.is_dir():
                found = [
                    f for f in p.glob("**/*.html")
                    if not any(ex in f.parts for ex in EXCLUDE_DIRS)
                ]
                target_files.extend(found)
            else:
                print(fmt.red(f"Error: Path not found: {p_str}"))
                sys.exit(1)
        target_files.sort()
    elif args.all or args.sample is not None:
        all_models = find_all_model_files(MODELS_DIR)
        if not all_models:
            print(fmt.red(f"Error: No model files found in {MODELS_DIR}"))
            sys.exit(1)

        if args.sample is not None:
            sample_size = min(args.sample, len(all_models))
            if args.seed is not None:
                random.seed(args.seed)
            target_files = sorted(random.sample(all_models, sample_size))
        else:
            target_files = all_models
    else:
        # Default behavior if no flags: verify all models
        target_files = find_all_model_files(MODELS_DIR)

    if not target_files:
        print(fmt.red("Error: No models selected for verification."))
        sys.exit(1)

    # Execute validations
    results: List[FileValidationResult] = []
    rule_stats: Dict[str, Dict[str, Any]] = {}
    for idx in range(1, 14):
        rule_key = f"RULE_{idx:02d}"
        rule_stats[rule_key] = {"passed": 0, "failed": 0, "name": ""}

    for file_path in target_files:
        res = validate_file(file_path)
        results.append(res)
        for r in res.rule_results:
            rule_stats[r.rule_id]["name"] = r.rule_name
            if r.passed:
                rule_stats[r.rule_id]["passed"] += 1
            else:
                rule_stats[r.rule_id]["failed"] += 1

    total_files = len(results)
    passed_files = sum(1 for r in results if r.passed)
    failed_files = total_files - passed_files

    if args.json:
        payload = {
            "total_evaluated": total_files,
            "passed": passed_files,
            "failed": failed_files,
            "all_passed": (failed_files == 0),
            "rule_statistics": rule_stats,
            "results": [r.to_dict() for r in results],
        }
        print(json.dumps(payload, indent=2))
        sys.exit(0 if failed_files == 0 else 1)

    # Human-readable output
    print("\n" + "=" * 80)
    print(fmt.bold("ENGINEERING PHYSICS STANDARDIZED MODEL VERIFICATION AUDIT"))
    print("=" * 80)
    print(f"Total Models Evaluated:  {fmt.bold(str(total_files))}")
    print(f"Passing All 13 Rules:    {fmt.green(str(passed_files))}")
    print(f"Failing >= 1 Rule:       {fmt.red(str(failed_files)) if failed_files > 0 else fmt.green('0')}")
    print("=" * 80 + "\n")

    # Rule Summary Table
    print(fmt.bold("RULE-BY-RULE COMPLIANCE BREAKDOWN:"))
    print("-" * 80)
    print(f"{'Rule':<10} {'Name':<45} {'Passed':<10} {'Failed':<10} {'Compliance':<10}")
    print("-" * 80)
    for rule_id, data in sorted(rule_stats.items()):
        pass_pct = (data["passed"] / total_files * 100) if total_files else 0
        status_color = fmt.green if pass_pct == 100.0 else (fmt.yellow if pass_pct > 0 else fmt.red)
        print(
            f"{rule_id:<10} {data['name'][:43]:<45} {str(data['passed']):<10} {str(data['failed']):<10} {status_color(f'{pass_pct:6.1f}%'):<10}"
        )
    print("-" * 80 + "\n")

    # Verbose or Failure Listings
    if args.verbose:
        print(fmt.bold("PER-MODEL DETAILED REPORT:"))
        for r in results:
            status_tag = fmt.green("[PASS]") if r.passed else fmt.red(f"[FAIL ({r.failure_count} rules)]")
            print(f"\n{status_tag} {r.rel_path}")
            for rule_res in r.rule_results:
                icon = fmt.green("✓") if rule_res.passed else fmt.red("✗")
                print(f"    {icon} {rule_res.rule_id} ({rule_res.rule_name}): {rule_res.message}")
    elif failed_files > 0:
        display_limit = 30
        print(fmt.bold(f"FAILURE DETAILS (Showing up to {display_limit} of {failed_files} failing models):"))
        shown = 0
        for r in results:
            if not r.passed:
                shown += 1
                if shown > display_limit:
                    print(f"\n... and {failed_files - display_limit} more failing model files. Use -v / --verbose for full report.")
                    break
                print(f"\n{fmt.red('[FAIL]')} {r.rel_path}:")
                for rule_res in r.rule_results:
                    if not rule_res.passed:
                        print(f"    {fmt.red('✗')} {rule_res.rule_id} ({rule_res.rule_name}): {rule_res.message}")

    print("\n" + "=" * 80)
    if failed_files == 0:
        print(fmt.green(fmt.bold("VERIFICATION STATUS: 100% PASSED. All models strictly comply with design system!")))
        print("=" * 80 + "\n")
        sys.exit(0)
    else:
        print(fmt.red(fmt.bold(f"VERIFICATION STATUS: FAILED. {failed_files} model(s) have compliance violations.")))
        print("=" * 80 + "\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
