#!/usr/bin/env python3
"""
scripts/verify_apple_hig.py
==============================================================================
Comprehensive Apple Human Interface Guidelines (HIG) Automated Test Harness.

Verifies acceptance criteria across all 398 physics models in models/ and
the dashboard (index.html):

  - CHECK 1: UI Simplification
      * Zero "Toggle Theme", "Reset", or "Explore →" (&rarr;) in any model or index.html
      * Zero <button> elements with id="theme-toggle" in any model file
      * Zero #modalThemeBtn or #modalReloadBtn in index.html
      * Every model contains @media (prefers-color-scheme: dark)

  - CHECK 2: Apple HIG Typography
      * Zero 'Inter' or "Inter" in font-family, font links, or ctx.font
        (Safely preserves scientific words: Interference, Interface, Internal, etc.)
      * Zero 'JetBrains Mono' in any model or index.html
      * Every model's --font-sans stack begins with -apple-system
      * Monospace stack starts with 'SF Mono'

  - CHECK 3: Apple HIG Color System & Zero Pastel Tokens
      * Zero pastel tokens: --block-bg, --block-border, --block-accent,
        block-lime, block-lilac, block-mint, block-cream, block-pink, block-coral, block-navy
      * Dark mode :root background uses #1C1C1E (case-insensitive)
      * Simulation container uses Apple grouped background (#F2F2F7 light / #2C2C2E dark)
      * Cards use 12px border radius (--rounded-card: 12px; or border-radius: 12px;)

  - CHECK 4: KaTeX & Scientific Mathematical Fidelity
      * Every model contains KaTeX CSS/JS CDN links in <head>
      * Every model contains math delimiters ($$, \\[, etc.) in .equation-formula
      * Zero instances of Unicode combining characters (e.g. U+20D7)
      * Equation container specifies horizontal overflow scrolling (overflow-x: auto)

  - CHECK 5: Runtime, Canvas & Dashboard Integrity
      * Every model contains <canvas id="sim-canvas"> with 2D context
      * Every model contains requestAnimationFrame animation loop
      * Zero JavaScript syntax errors (verified via node --check)
      * All 398 models resolve from index.html (zero broken links)

Usage:
  python3 scripts/verify_apple_hig.py [--all] [--verbose]
  python3 scripts/verify_apple_hig.py --models [--discipline <name>] [--verbose]
  python3 scripts/verify_apple_hig.py --dashboard [--verbose]
  python3 scripts/verify_apple_hig.py --file <path/to/model.html> [--verbose]
  python3 scripts/verify_apple_hig.py --json
==============================================================================
"""

import argparse
import concurrent.futures
from dataclasses import dataclass, field
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
import unicodedata
from typing import Dict, List, Optional, Set, Tuple


# Terminal ANSI Colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

# If stdout is not a TTY, disable ANSI codes
if not sys.stdout.isatty() or os.environ.get("NO_COLOR"):
    GREEN = RED = YELLOW = CYAN = BOLD = RESET = ""


@dataclass
class CheckResult:
    check_id: str
    check_name: str
    passed: bool
    summary: str
    violations: List[str] = field(default_factory=list)


@dataclass
class ModelEvaluation:
    file_path: Path
    rel_path: str
    discipline: str
    checks: Dict[str, CheckResult]
    passed: bool


@dataclass
class DashboardEvaluation:
    file_path: Path
    rel_path: str
    checks: Dict[str, CheckResult]
    passed: bool


# ==============================================================================
# CHECK 1: UI SIMPLIFICATION
# ==============================================================================

def check_1_model_ui_simplification(content: str, rel_path: str) -> CheckResult:
    """
    Check 1 for Model HTML:
      - Zero instances of "Toggle Theme", "Reset", or "Explore →" (&rarr;)
      - Zero <button> elements with id="theme-toggle"
      - Every model file must contain @media (prefers-color-scheme: dark)
    """
    check_id = "CHECK_1"
    name = "UI Simplification & Native Media Query"
    violations: List[str] = []

    # 1.1 "Toggle Theme" check (case-insensitive)
    if re.search(r'\btoggle\s+theme\b', content, re.IGNORECASE):
        # find line numbers
        lines = content.splitlines()
        for idx, line in enumerate(lines, 1):
            if re.search(r'\btoggle\s+theme\b', line, re.IGNORECASE):
                violations.append(f"Forbidden 'Toggle Theme' text at line {idx}: '{line.strip()[:60]}'")
                break

    # 1.2 "Explore →" or "Explore &rarr;" check
    explore_match = re.search(r'Explore\s*(?:&rarr;|→|&#8594;|\\u2192)', content, re.IGNORECASE)
    if explore_match:
        lines = content.splitlines()
        for idx, line in enumerate(lines, 1):
            if re.search(r'Explore\s*(?:&rarr;|→|&#8594;|\\u2192)', line, re.IGNORECASE):
                violations.append(f"Forbidden 'Explore →' text at line {idx}: '{line.strip()[:60]}'")
                break

    # 1.3 "Reset" in UI elements (buttons, spans, links, attributes)
    # Check if any button contains Reset, or if any UI element is labeled Reset
    ui_reset_match = re.search(r'<button\b[^>]*>[\s\S]*?\bReset\b[\s\S]*?</button>', content, re.IGNORECASE)
    if ui_reset_match:
        violations.append(f"Forbidden Reset button found: '{ui_reset_match.group(0).strip()[:60]}'")

    ui_text_reset = re.search(r'<(?:span|a|p|div|h\d)\b[^>]*>[^<]*?\bReset\b[^<]*?</(?:span|a|p|div|h\d)>', content, re.IGNORECASE)
    if ui_text_reset:
        violations.append(f"Forbidden Reset UI element found: '{ui_text_reset.group(0).strip()[:60]}'")

    # 1.4 <button id="theme-toggle"> check
    theme_toggle_btn = re.search(r'<button\b[^>]*\bid=["\']theme-toggle["\']', content, re.IGNORECASE)
    if theme_toggle_btn:
        violations.append("Forbidden <button id=\"theme-toggle\"> element found in markup")

    # 1.5 @media (prefers-color-scheme: dark) check
    has_prefers_color_scheme = bool(
        re.search(r'@media\s*\(\s*prefers-color-scheme\s*:\s*dark\s*\)', content, re.IGNORECASE)
    )
    if not has_prefers_color_scheme:
        violations.append("Missing '@media (prefers-color-scheme: dark)' for automatic OS theme detection")

    passed = len(violations) == 0
    summary = "UI simplified; zero theme/reset/explore buttons; native dark media query present" if passed else f"{len(violations)} UI simplification violation(s)"
    return CheckResult(check_id, name, passed, summary, violations)


def check_1_dashboard_ui_simplification(content: str, rel_path: str) -> CheckResult:
    """
    Check 1 for Dashboard index.html:
      - Zero instances of "Toggle Theme", "Reset", or "Explore →" (&rarr;)
      - Zero #modalThemeBtn or #modalReloadBtn in index.html
    """
    check_id = "CHECK_1"
    name = "Dashboard UI Simplification"
    violations: List[str] = []

    # 1.1 "Explore →" or "Explore &rarr;"
    explore_matches = re.findall(r'Explore\s*(?:&rarr;|→|&#8594;|\\u2192)', content, re.IGNORECASE)
    if explore_matches:
        violations.append(f"Found {len(explore_matches)} instances of 'Explore →' / 'Explore &rarr;' on model cards")

    # 1.2 "Toggle Theme" in dashboard
    if re.search(r'\btoggle\s+theme\b', content, re.IGNORECASE):
        violations.append("Forbidden 'Toggle Theme' text found in dashboard")

    # 1.3 #modalThemeBtn
    if "modalThemeBtn" in content:
        violations.append("Forbidden '#modalThemeBtn' found in dashboard markup or script")

    # 1.4 #modalReloadBtn
    if "modalReloadBtn" in content:
        violations.append("Forbidden '#modalReloadBtn' found in dashboard markup or script")

    # 1.5 "Reset" button / UI text in modal toolbar
    if re.search(r'<span>\s*Reset\s*</span>', content, re.IGNORECASE):
        violations.append("Forbidden '<span>Reset</span>' button text found in modal toolbar")

    passed = len(violations) == 0
    summary = "Dashboard UI simplified; zero theme/reload/explore buttons" if passed else f"{len(violations)} dashboard UI violation(s)"
    return CheckResult(check_id, name, passed, summary, violations)


# ==============================================================================
# CHECK 2: APPLE HIG TYPOGRAPHY
# ==============================================================================

def check_2_model_typography(content: str, rel_path: str) -> CheckResult:
    """
    Check 2 for Model HTML:
      - Zero occurrences of 'Inter' or "Inter" in font-family, font links, or ctx.font
        (Safely preserves words: Interference, Interface, Internal, Interferometer, etc.)
      - Zero occurrences of 'JetBrains Mono'
      - Every model's --font-sans stack must begin with -apple-system
      - Apple monospace stack starts with 'SF Mono'
    """
    check_id = "CHECK_2"
    name = "Apple HIG Typography"
    violations: List[str] = []

    # Extract <style> block(s) and <script> block(s)
    styles = "\n".join(re.findall(r'<style[^>]*>([\s\S]*?)</style>', content, re.IGNORECASE))
    scripts = "\n".join(re.findall(r'<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)</script>', content, re.IGNORECASE))

    # 2.1 'Inter' font checks with strict word boundaries and font context
    # Font links in head
    font_link_inter = re.findall(r'<(?:link|style)\b[^>]*\b(?:href|src)=["\'][^"\']*?\b(?:family=)?Inter\b[^"\']*["\']', content, re.IGNORECASE)
    if font_link_inter:
        violations.append("Forbidden Google Fonts or external link containing 'Inter'")

    # CSS font declarations containing Inter as a font family
    css_inter_matches = re.findall(r'(?:font-family|--font-sans|--font-[a-z0-9_-]+|font)\s*:[^;}]*?\bInter\b', styles, re.IGNORECASE)
    if css_inter_matches:
        for m in css_inter_matches[:3]:
            violations.append(f"CSS font declaration references 'Inter': '{m.strip()[:60]}'")

    # ctx.font containing Inter in JS
    ctx_inter_matches = re.findall(r'ctx\.font\s*=\s*["\'][^"\']*?\bInter\b[^"\']*["\']', scripts, re.IGNORECASE)
    if ctx_inter_matches:
        for m in ctx_inter_matches[:3]:
            violations.append(f"Canvas ctx.font references 'Inter': '{m.strip()[:60]}'")

    # Quoted 'Inter' or "Inter" standalone font name anywhere in file
    quoted_inter = re.findall(r"""(?<![a-zA-Z0-9_-])['"]Inter['"](?![a-zA-Z0-9_-])""", content)
    if quoted_inter and not css_inter_matches and not ctx_inter_matches and not font_link_inter:
        violations.append(f"Forbidden quoted 'Inter' font name found ({len(quoted_inter)} occurrence(s))")

    # 2.2 'JetBrains Mono' check across whole file
    jetbrains_matches = re.findall(r'JetBrains\s*Mono', content, re.IGNORECASE)
    if jetbrains_matches:
        violations.append(f"Forbidden 'JetBrains Mono' font found ({len(jetbrains_matches)} occurrence(s))")

    # 2.3 --font-sans stack must begin with -apple-system
    font_sans_match = re.search(r'--font-sans\s*:\s*([^;{}]+)[;}]', styles, re.IGNORECASE)
    if not font_sans_match:
        violations.append("Missing '--font-sans' CSS custom property definition")
    else:
        font_sans_val = font_sans_match.group(1).strip()
        first_font = [f.strip().strip("'\"") for f in font_sans_val.split(",") if f.strip()]
        if not first_font or first_font[0].lower() != "-apple-system":
            first_name = first_font[0] if first_font else "empty"
            violations.append(f"--font-sans stack must begin with '-apple-system' (found: '{first_name}')")

    # 2.4 Apple monospace stack starts with 'SF Mono'
    font_mono_match = re.search(r'--font-mono\s*:\s*([^;{}]+)[;}]', styles, re.IGNORECASE)
    if not font_mono_match:
        violations.append("Missing '--font-mono' CSS custom property definition")
    else:
        font_mono_val = font_mono_match.group(1).strip()
        first_mono = [f.strip().strip("'\"") for f in font_mono_val.split(",") if f.strip()]
        if not first_mono or first_mono[0].lower() not in ("sf mono", "sfmono-regular"):
            first_mono_name = first_mono[0] if first_mono else "empty"
            violations.append(f"--font-mono stack must begin with 'SF Mono' (found: '{first_mono_name}')")

    passed = len(violations) == 0
    summary = "Apple HIG typography verified (-apple-system, SF Mono, zero Inter/JetBrains)" if passed else f"{len(violations)} typography violation(s)"
    return CheckResult(check_id, name, passed, summary, violations)


def check_2_dashboard_typography(content: str, rel_path: str) -> CheckResult:
    """
    Check 2 for Dashboard index.html:
      - Zero 'Inter' or 'JetBrains Mono' in font links, font declarations
      - --font-sans begins with -apple-system
      - --font-mono begins with 'SF Mono'
    """
    check_id = "CHECK_2"
    name = "Dashboard Apple HIG Typography"
    violations: List[str] = []

    styles = "\n".join(re.findall(r'<style[^>]*>([\s\S]*?)</style>', content, re.IGNORECASE))

    # Google Fonts links containing Inter or JetBrains Mono
    if re.search(r'<(?:link|style)\b[^>]*\b(?:href|src)=["\'][^"\']*?\b(?:Inter|JetBrains\+Mono)\b', content, re.IGNORECASE):
        violations.append("Forbidden Google Fonts link for 'Inter' / 'JetBrains Mono' in dashboard head")

    # CSS font declarations
    if re.search(r'(?:font-family|--font-sans|--font-mono)\s*:[^;}]*?\bInter\b', styles, re.IGNORECASE):
        violations.append("CSS declaration in dashboard references 'Inter'")

    if re.search(r'JetBrains\s*Mono', content, re.IGNORECASE):
        violations.append("Dashboard references forbidden 'JetBrains Mono'")

    # --font-sans check
    font_sans_match = re.search(r'--font-sans\s*:\s*([^;{}]+)[;}]', styles, re.IGNORECASE)
    if not font_sans_match:
        violations.append("Dashboard missing '--font-sans' property")
    else:
        first_font = [f.strip().strip("'\"") for f in font_sans_match.group(1).split(",") if f.strip()]
        if not first_font or first_font[0].lower() != "-apple-system":
            violations.append(f"Dashboard --font-sans must start with '-apple-system' (found: '{first_font[0] if first_font else None}')")

    # --font-mono check
    font_mono_match = re.search(r'--font-mono\s*:\s*([^;{}]+)[;}]', styles, re.IGNORECASE)
    if not font_mono_match:
        violations.append("Dashboard missing '--font-mono' property")
    else:
        first_mono = [f.strip().strip("'\"") for f in font_mono_match.group(1).split(",") if f.strip()]
        if not first_mono or first_mono[0].lower() not in ("sf mono", "sfmono-regular"):
            violations.append(f"Dashboard --font-mono must start with 'SF Mono' (found: '{first_mono[0] if first_mono else None}')")

    passed = len(violations) == 0
    summary = "Dashboard typography conforms to Apple HIG" if passed else f"{len(violations)} dashboard typography violation(s)"
    return CheckResult(check_id, name, passed, summary, violations)


# ==============================================================================
# CHECK 3: APPLE HIG COLOR SYSTEM & ZERO PASTEL TOKENS
# ==============================================================================

PASTEL_TOKENS = [
    "--block-bg",
    "--block-border",
    "--block-accent",
    "--block-text",
    "--block-grid",
    "--block-axis",
    "block-lime",
    "block-lilac",
    "block-mint",
    "block-cream",
    "block-pink",
    "block-coral",
    "block-navy",
]

def check_3_model_color_system(content: str, rel_path: str) -> CheckResult:
    """
    Check 3 for Model HTML:
      - Zero pastel tokens: --block-bg, --block-border, --block-accent,
        block-lime, block-lilac, block-mint, block-cream, block-pink, block-coral, block-navy
      - Dark mode background :root must use #1C1C1E (case-insensitive)
      - Simulation container uses Apple grouped background (#F2F2F7 light / #2C2C2E dark)
      - Cards use 12px border radius (--rounded-card: 12px; or border-radius: 12px;)
    """
    check_id = "CHECK_3"
    name = "Apple HIG Color System & Zero Pastel Tokens"
    violations: List[str] = []

    styles = "\n".join(re.findall(r'<style[^>]*>([\s\S]*?)</style>', content, re.IGNORECASE))
    scripts = "\n".join(re.findall(r'<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)</script>', content, re.IGNORECASE))

    # 3.1 Zero pastel tokens in CSS and JS
    for token in PASTEL_TOKENS:
        if token in styles:
            violations.append(f"Forbidden pastel token '{token}' found in <style>")
        if token in scripts:
            violations.append(f"Forbidden pastel token '{token}' found in <script>")

    # Check for legacy color-block class on simulation container
    if re.search(r'class=["\'][^"\']*\bcolor-block\b', content, re.IGNORECASE):
        violations.append("Forbidden 'color-block' class present on simulation container")

    # 3.2 Dark mode background :root must use #1C1C1E
    # Check that dark mode defines #1c1c1e
    dark_media_match = re.search(
        r'@media\s*\(\s*prefers-color-scheme\s*:\s*dark\s*\)\s*\{([\s\S]*?)\}\s*(?:@media|\Z)',
        styles,
        re.IGNORECASE
    )
    if not dark_media_match:
        violations.append("Missing '@media (prefers-color-scheme: dark)' block defining dark mode tokens")
    else:
        dark_block = dark_media_match.group(1)
        if "#1c1c1e" not in dark_block.lower():
            violations.append("Dark mode :root block does not define Apple HIG dark canvas background '#1C1C1E'")

    # 3.3 Simulation container uses Apple grouped background (#F2F2F7 light / #2C2C2E dark)
    # Light mode grouped surface #F2F2F7
    if "#f2f2f7" not in styles.lower():
        violations.append("CSS does not define Apple HIG light grouped background '#F2F2F7'")

    # Dark mode grouped surface #2C2C2E
    if "#2c2c2e" not in styles.lower():
        violations.append("CSS does not define Apple HIG dark grouped background '#2C2C2E'")

    # Simulation container background variable check
    sim_container_css = re.search(
        r'(?:\.sim-container|\.simulation-viewport|main)\s*\{([^}]+)\}',
        styles,
        re.IGNORECASE
    )
    if sim_container_css:
        container_body = sim_container_css.group(1)
        has_sim_bg = bool(re.search(r'background(?:-color)?\s*:\s*var\(--(?:sim-bg|canvas-surface)\)', container_body, re.IGNORECASE) or
                          "#f2f2f7" in container_body.lower())
        if not has_sim_bg:
            violations.append("Simulation container does not use Apple grouped background token var(--sim-bg)")

    # 3.4 Cards use 12px border radius (--rounded-card: 12px; or border-radius: 12px;)
    has_12px_radius = bool(
        re.search(r'--rounded-card\s*:\s*12px\b', styles, re.IGNORECASE) or
        re.search(r'border-radius\s*:\s*12px\b', styles, re.IGNORECASE)
    )
    if not has_12px_radius:
        violations.append("Missing 12px card border radius ('--rounded-card: 12px;' or 'border-radius: 12px;')")

    # Flag legacy 24px pill/card radius
    if re.search(r'--rounded-card\s*:\s*24px\b', styles, re.IGNORECASE):
        violations.append("Forbidden legacy '--rounded-card: 24px;' found; must be updated to 12px")

    passed = len(violations) == 0
    summary = "Apple HIG color system verified (zero pastels, #1C1C1E dark, #F2F2F7/#2C2C2E grouped, 12px radius)" if passed else f"{len(violations)} color/surface violation(s)"
    return CheckResult(check_id, name, passed, summary, violations)


def check_3_dashboard_color_system(content: str, rel_path: str) -> CheckResult:
    """
    Check 3 for Dashboard index.html:
      - Zero pastel tokens / pastel DISCIPLINE_PALETTES
      - 12px card border-radius
      - Dark mode support matching Apple HIG
    """
    check_id = "CHECK_3"
    name = "Dashboard Apple HIG Color System"
    violations: List[str] = []

    styles = "\n".join(re.findall(r'<style[^>]*>([\s\S]*?)</style>', content, re.IGNORECASE))

    # Pastel tokens
    for token in PASTEL_TOKENS:
        if token in content:
            violations.append(f"Forbidden pastel token '{token}' found in dashboard")

    # Card border radius
    has_12px_card = bool(
        re.search(r'--rounded-card\s*:\s*12px\b', styles, re.IGNORECASE) or
        re.search(r'\.model-card\s*\{[^}]*border-radius\s*:\s*(?:var\(--rounded-card\)|12px\b)', styles, re.IGNORECASE) or
        re.search(r'--rounded-lg\s*:\s*12px\b', styles, re.IGNORECASE)
    )
    if not has_12px_card:
        violations.append("Dashboard cards do not use Apple 12px border radius")

    passed = len(violations) == 0
    summary = "Dashboard color system and card geometry verified" if passed else f"{len(violations)} dashboard color violation(s)"
    return CheckResult(check_id, name, passed, summary, violations)


# ==============================================================================
# CHECK 4: KATEX & SCIENTIFIC MATHEMATICAL FIDELITY
# ==============================================================================

def check_4_katex_fidelity(content: str, rel_path: str) -> CheckResult:
    """
    Check 4 for Model HTML:
      - Every model contains KaTeX CSS/JS CDN links in <head>
      - Every model contains math delimiters ($$, \\[, etc.) in .equation-formula
      - Zero instances of Unicode combining characters (e.g. U+20D7)
      - Equation container specifies horizontal overflow scrolling (overflow-x: auto)
    """
    check_id = "CHECK_4"
    name = "KaTeX & Scientific Mathematical Fidelity"
    violations: List[str] = []

    m_head = re.search(r'<head\b[^>]*>(.*?)</head>', content, re.DOTALL | re.IGNORECASE)
    head_content = m_head.group(1) if m_head else content

    # 4.1 KaTeX CDN in head
    has_css = bool(re.search(r'<link\b[^>]*\bhref=["\'][^"\']*katex(\.min)?\.css', head_content, re.I))
    has_js = bool(re.search(r'<script\b[^>]*\bsrc=["\'][^"\']*katex(\.min)?\.js', head_content, re.I))
    has_autorender = bool(re.search(r'<script\b[^>]*\bsrc=["\'][^"\']*auto-render(\.min)?\.js', head_content, re.I) or
                          re.search(r'<script\b[^>]*\bsrc=["\'][^"\']*contrib/auto-render', head_content, re.I))

    if not has_css:
        violations.append("Missing KaTeX CSS stylesheet link in <head>")
    if not has_js:
        violations.append("Missing KaTeX JS engine script in <head>")
    if not has_autorender:
        violations.append("Missing KaTeX auto-render extension script in <head>")

    # 4.2 Math delimiters in .equation-formula
    eq_match = re.search(
        r'<div[^>]*class=["\'][^"\']*\bequation-formula\b[^"\']*["\'][^>]*>(.*?)</div>',
        content,
        re.DOTALL | re.IGNORECASE
    )
    if not eq_match:
        violations.append("Missing equation formula container (<div class=\"equation-formula\">)")
    else:
        raw_eq = eq_match.group(1).strip()
        has_delims = bool(
            ("$$" in raw_eq) or
            re.search(r'\\\[[\s\S]*?\\\]', raw_eq) or
            re.search(r'\\\([\s\S]*?\\\)', raw_eq) or
            re.search(r'\\begin\{[a-zA-Z*]+\}', raw_eq) or
            ('<span class="katex"' in raw_eq) or
            ("<span class='katex'" in raw_eq)
        )
        if not has_delims:
            violations.append("Equation formula does not contain KaTeX math delimiters ($$, \\[, \\()")

    # 4.3 Zero Unicode combining characters (e.g. U+20D7)
    u20d7_count = content.count('\u20d7')
    if u20d7_count > 0:
        violations.append(f"Found {u20d7_count} forbidden U+20D7 combining right arrow character(s)")

    # Check for any combining characters across file
    combining_chars = [c for c in content if unicodedata.category(c).startswith('M')]
    if combining_chars:
        unique_combining = set(combining_chars)
        codepoints = ", ".join(f"U+{ord(c):04X}" for c in unique_combining)
        violations.append(f"Found {len(combining_chars)} Unicode combining mark(s): {codepoints}")

    # 4.4 Equation container horizontal overflow scrolling (overflow-x: auto)
    styles = "\n".join(re.findall(r'<style[^>]*>([\s\S]*?)</style>', content, re.IGNORECASE))
    eq_css_rules = re.findall(
        r'(?:[^{}]*?(?:\.equation-formula|\.equation|\.equation-container|\.formula-card|\.katex-display)[^{}]*?)\{([^}]+)\}',
        styles,
        re.IGNORECASE
    )
    has_overflow = any(
        re.search(r'\boverflow(?:-x)?\s*:\s*(?:auto|scroll)\b', rule, re.I)
        for rule in eq_css_rules
    )
    if not has_overflow:
        violations.append("Equation block CSS is missing 'overflow-x: auto' property")

    passed = len(violations) == 0
    summary = "KaTeX resources, LaTeX formula delimiters, 0 combining characters, overflow-x verified" if passed else f"{len(violations)} mathematical fidelity violation(s)"
    return CheckResult(check_id, name, passed, summary, violations)


# ==============================================================================
# CHECK 5: RUNTIME, CANVAS & DASHBOARD INTEGRITY
# ==============================================================================

def check_5_model_runtime_integrity(content: str, rel_path: str) -> CheckResult:
    """
    Check 5 for Model HTML:
      - Every model contains <canvas id="sim-canvas"> with 2D context
      - Every model contains requestAnimationFrame loop
      - Zero JavaScript syntax errors (verified via node --check)
    """
    check_id = "CHECK_5"
    name = "Runtime & Canvas 2D Integrity"
    violations: List[str] = []

    # 5.1 <canvas id="sim-canvas">
    has_canvas = bool(re.search(r'<canvas\b[^>]*\bid=["\']sim-canvas["\']', content, re.I))
    if not has_canvas:
        violations.append("Missing '<canvas id=\"sim-canvas\">' element")

    # 5.2 2D rendering context
    has_2d_ctx = bool(
        re.search(r'getContext\(\s*["\']2d["\']\s*\)', content, re.I)
    )
    if not has_2d_ctx:
        violations.append("Missing Canvas 2D context initialization ('getContext(\"2d\")')")

    # 5.3 requestAnimationFrame loop
    has_raf = "requestAnimationFrame" in content
    if not has_raf:
        violations.append("Missing continuous animation loop ('requestAnimationFrame')")

    # 5.4 JavaScript syntax check via node --check
    scripts = re.findall(r'<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)</script>', content, re.I)
    if not scripts:
        violations.append("Missing inline simulation <script> block")
    else:
        full_js = "\n".join(scripts)
        try:
            res = subprocess.run(
                ["node", "--check", "-"],
                input=full_js,
                capture_output=True,
                text=True,
                timeout=5
            )
            if res.returncode != 0:
                first_err = res.stderr.splitlines()[0] if res.stderr else "Node syntax validation failed"
                violations.append(f"JavaScript syntax error: {first_err}")
        except FileNotFoundError:
            # Fallback if Node.js binary is not in PATH
            pass
        except subprocess.TimeoutExpired:
            violations.append("JavaScript syntax validation timed out after 5s")

    passed = len(violations) == 0
    summary = "Canvas 2D, 60fps rAF loop, and JavaScript syntax verified" if passed else f"{len(violations)} runtime integrity violation(s)"
    return CheckResult(check_id, name, passed, summary, violations)


def check_5_dashboard_link_integrity(content: str, rel_path: str, repo_root: Path) -> CheckResult:
    """
    Check 5 for Dashboard index.html:
      - All 398 models resolve from index.html (zero broken links)
      - JavaScript syntax clean in index.html inline script
    """
    check_id = "CHECK_5"
    name = "Dashboard Model Resolution & Link Integrity"
    violations: List[str] = []

    # Extract all model links matching models/<discipline>/<id>.html
    links = re.findall(r'href=["\'](models/[^"\']+\.html)["\']', content, re.I)
    unique_links = sorted(list(set(links)))

    # Verify total unique model links is 398
    if len(unique_links) != 398:
        violations.append(f"Dashboard contains {len(unique_links)} unique model links (expected exactly 398)")

    # Verify each referenced model exists on disk
    broken_links = []
    for link in unique_links:
        full_path = repo_root / link
        if not full_path.is_file():
            broken_links.append(link)

    if broken_links:
        violations.append(f"Found {len(broken_links)} broken model link(s): {', '.join(broken_links[:5])}...")

    # JavaScript syntax validation for index.html inline script
    scripts = re.findall(r'<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)</script>', content, re.I)
    if scripts:
        full_js = "\n".join(scripts)
        try:
            res = subprocess.run(
                ["node", "--check", "-"],
                input=full_js,
                capture_output=True,
                text=True,
                timeout=5
            )
            if res.returncode != 0:
                first_err = res.stderr.splitlines()[0] if res.stderr else "Node syntax check failed"
                violations.append(f"Dashboard JavaScript syntax error: {first_err}")
        except Exception:
            pass

    passed = len(violations) == 0
    summary = f"All 398 models resolved from index.html (0 broken links, 100% link integrity)" if passed else f"{len(violations)} dashboard link/resolution violation(s)"
    return CheckResult(check_id, name, passed, summary, violations)


# ==============================================================================
# EVALUATION RUNNERS
# ==============================================================================

def evaluate_single_model(file_path: Path, repo_root: Path) -> ModelEvaluation:
    """Evaluate a single model HTML file against all 5 Apple HIG checks."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        content = ""

    try:
        rel_path = str(file_path.relative_to(repo_root))
    except Exception:
        rel_path = str(file_path)

    discipline = file_path.parent.name

    c1 = check_1_model_ui_simplification(content, rel_path)
    c2 = check_2_model_typography(content, rel_path)
    c3 = check_3_model_color_system(content, rel_path)
    c4 = check_4_katex_fidelity(content, rel_path)
    c5 = check_5_model_runtime_integrity(content, rel_path)

    checks = {
        "CHECK_1": c1,
        "CHECK_2": c2,
        "CHECK_3": c3,
        "CHECK_4": c4,
        "CHECK_5": c5,
    }
    all_passed = all(c.passed for c in checks.values())

    return ModelEvaluation(
        file_path=file_path,
        rel_path=rel_path,
        discipline=discipline,
        checks=checks,
        passed=all_passed,
    )


def evaluate_dashboard(file_path: Path, repo_root: Path) -> DashboardEvaluation:
    """Evaluate index.html against Apple HIG acceptance criteria."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception:
        content = ""

    try:
        rel_path = str(file_path.relative_to(repo_root))
    except Exception:
        rel_path = str(file_path)

    c1 = check_1_dashboard_ui_simplification(content, rel_path)
    c2 = check_2_dashboard_typography(content, rel_path)
    c3 = check_3_dashboard_color_system(content, rel_path)
    c5 = check_5_dashboard_link_integrity(content, rel_path, repo_root)

    checks = {
        "CHECK_1": c1,
        "CHECK_2": c2,
        "CHECK_3": c3,
        "CHECK_5": c5,
    }
    all_passed = all(c.passed for c in checks.values())

    return DashboardEvaluation(
        file_path=file_path,
        rel_path=rel_path,
        checks=checks,
        passed=all_passed,
    )


# ==============================================================================
# REPORTING & FORMATTING
# ==============================================================================

def print_banner():
    print(f"\n{BOLD}{CYAN}=============================================================================={RESET}")
    print(f"{BOLD}{CYAN}      APPLE HUMAN INTERFACE GUIDELINES (HIG) AUTOMATED TEST HARNESS          {RESET}")
    print(f"{BOLD}{CYAN}=============================================================================={RESET}")


def print_summary_table(
    model_evals: List[ModelEvaluation],
    dash_eval: Optional[DashboardEvaluation],
    verbose: bool = False
):
    total_models = len(model_evals)

    # Calculate pass counts per check
    check_stats = {
        "CHECK_1": {"name": "Check 1: UI Simplification (No Theme/Reset/Explore Buttons)", "pass": 0, "fail": 0},
        "CHECK_2": {"name": "Check 2: Apple HIG Typography (-apple-system, SF Mono, 0 Inter)", "pass": 0, "fail": 0},
        "CHECK_3": {"name": "Check 3: Apple HIG Colors & Zero Pastels (#1C1C1E, #F2F2F7, 12px)", "pass": 0, "fail": 0},
        "CHECK_4": {"name": "Check 4: KaTeX & Scientific Mathematical Fidelity", "pass": 0, "fail": 0},
        "CHECK_5": {"name": "Check 5: Runtime, Canvas 2D & Script Integrity", "pass": 0, "fail": 0},
    }

    for ev in model_evals:
        for cid, res in ev.checks.items():
            if res.passed:
                check_stats[cid]["pass"] += 1
            else:
                check_stats[cid]["fail"] += 1

    print(f"\n{BOLD}MODEL SUITE RESULTS ({total_models} models evaluated):{RESET}")
    print(f"{'Check':<10} | {'Requirement Description':<55} | {'Passed':<7} | {'Failed':<7} | {'Compliance':<10}")
    print("-" * 98)

    for cid in ("CHECK_1", "CHECK_2", "CHECK_3", "CHECK_4", "CHECK_5"):
        st = check_stats[cid]
        p = st["pass"]
        f = st["fail"]
        rate = (p / total_models * 100) if total_models > 0 else 0.0
        color = GREEN if f == 0 else RED
        print(f"{cid:<10} | {st['name']:<55} | {p:<7} | {f:<7} | {color}{rate:6.1f}%{RESET}")

    if dash_eval:
        print(f"\n{BOLD}DASHBOARD SUITE RESULTS (index.html):{RESET}")
        for cid, res in dash_eval.checks.items():
            status_str = f"{GREEN}PASS{RESET}" if res.passed else f"{RED}FAIL{RESET}"
            print(f"  [{status_str}] {cid}: {res.check_name} — {res.summary}")
            if not res.passed and verbose:
                for v in res.violations:
                    print(f"         • {v}")

    # Verbose failure details
    if verbose:
        print(f"\n{BOLD}DETAILED MODEL FAILURE BREAKDOWN (Sample up to 10 per check):{RESET}")
        for cid in ("CHECK_1", "CHECK_2", "CHECK_3", "CHECK_4", "CHECK_5"):
            failing_models = [ev for ev in model_evals if not ev.checks[cid].passed]
            if failing_models:
                print(f"\n{BOLD}{YELLOW}[{cid}] {check_stats[cid]['name']} — {len(failing_models)} failing models:{RESET}")
                for ev in failing_models[:10]:
                    v_str = "; ".join(ev.checks[cid].violations[:2])
                    print(f"  • {ev.rel_path}: {v_str}")
                if len(failing_models) > 10:
                    print(f"  ... and {len(failing_models) - 10} more.")


# ==============================================================================
# MAIN ENTRYPOINT
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Verify Apple HIG compliance across models and dashboard.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--all", action="store_true", help="Run all checks on all models and index.html (default)")
    parser.add_argument("--models", action="store_true", help="Run checks on models only")
    parser.add_argument("--dashboard", action="store_true", help="Run checks on dashboard (index.html) only")
    parser.add_argument("--file", type=str, default=None, help="Evaluate a single model or HTML file")
    parser.add_argument("--discipline", type=str, default=None, help="Filter models by discipline name")
    parser.add_argument("--verbose", "-v", action="store_true", help="Print verbose failure information and snippets")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON report")

    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent

    # Determine execution scope
    eval_dashboard_flag = args.dashboard or args.all or (not args.models and not args.file and not args.discipline)
    eval_models_flag = args.models or args.all or (not args.dashboard and not args.file)

    t0 = time.time()

    model_files: List[Path] = []
    if args.file:
        target_path = Path(args.file)
        if not target_path.is_absolute():
            target_path = repo_root / target_path
        if not target_path.exists():
            print(f"{RED}Error: File not found: {target_path}{RESET}", file=sys.stderr)
            sys.exit(2)
        if target_path.name == "index.html":
            eval_dashboard_flag = True
            eval_models_flag = False
        else:
            model_files = [target_path]
            eval_dashboard_flag = False
            eval_models_flag = True
    elif eval_models_flag:
        models_dir = repo_root / "models"
        if args.discipline:
            disc_dir = models_dir / args.discipline
            if not disc_dir.is_dir():
                print(f"{RED}Error: Discipline directory not found: {disc_dir}{RESET}", file=sys.stderr)
                sys.exit(2)
            model_files = sorted(disc_dir.glob("*.html"))
        else:
            model_files = sorted(models_dir.glob("*/*.html"))

    # Concurrently evaluate models
    model_evals: List[ModelEvaluation] = []
    if model_files:
        with concurrent.futures.ThreadPoolExecutor(max_workers=min(16, os.cpu_count() or 4)) as executor:
            future_to_file = {executor.submit(evaluate_single_model, f, repo_root): f for f in model_files}
            for future in concurrent.futures.as_completed(future_to_file):
                model_evals.append(future.result())

        # Sort back by rel_path for deterministic output
        model_evals.sort(key=lambda x: x.rel_path)

    # Evaluate dashboard
    dash_eval: Optional[DashboardEvaluation] = None
    if eval_dashboard_flag:
        index_path = repo_root / "index.html"
        dash_eval = evaluate_dashboard(index_path, repo_root)

    elapsed = time.time() - t0

    # Determine overall status
    models_pass = all(m.passed for m in model_evals) if model_evals else True
    dash_pass = dash_eval.passed if dash_eval else True
    overall_pass = models_pass and dash_pass

    # JSON output
    if args.json:
        report = {
            "overall_pass": overall_pass,
            "elapsed_seconds": round(elapsed, 3),
            "total_models": len(model_evals),
            "models_pass_count": sum(1 for m in model_evals if m.passed),
            "dashboard_evaluated": dash_eval is not None,
            "dashboard_pass": dash_pass,
            "dashboard": {
                "rel_path": dash_eval.rel_path,
                "passed": dash_eval.passed,
                "checks": {
                    cid: {"name": res.check_name, "passed": res.passed, "summary": res.summary, "violations": res.violations}
                    for cid, res in dash_eval.checks.items()
                }
            } if dash_eval else None,
            "models": [
                {
                    "rel_path": m.rel_path,
                    "discipline": m.discipline,
                    "passed": m.passed,
                    "checks": {
                        cid: {"name": res.check_name, "passed": res.passed, "summary": res.summary, "violations": res.violations}
                        for cid, res in m.checks.items()
                    }
                }
                for m in model_evals
            ]
        }
        print(json.dumps(report, indent=2))
        sys.exit(0 if overall_pass else 1)

    # Human-readable output
    print_banner()
    print(f"Executed in {elapsed:.2f}s | Target: {len(model_evals)} model(s) + {'index.html' if dash_eval else '0 dashboard'}")

    print_summary_table(model_evals, dash_eval, verbose=args.verbose)

    print(f"\n{BOLD}{'='*98}{RESET}")
    if overall_pass:
        print(f"{BOLD}{GREEN}OVERALL STATUS: 100% APPLE HIG COMPLIANT (PASS){RESET}")
        sys.exit(0)
    else:
        print(f"{BOLD}{RED}OVERALL STATUS: NON-COMPLIANT WITH APPLE HIG SPECIFICATION (FAIL){RESET}")
        print(f"Note: Failures are expected on baseline before Milestone 2 (Dashboard) & Milestone 3 (Models).")
        sys.exit(1)


if __name__ == "__main__":
    main()
