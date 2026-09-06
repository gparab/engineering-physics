#!/usr/bin/env python3
"""
scripts/verify_ui_ux_rendering.py
Automated Acceptance Verification Suite for Engineering Physics UI/UX & High-Fidelity Rendering Pass.

Verifies the 8 Acceptance Checks defined in the 2026-09-06T09:43:29Z Milestone:
  CHECK A: Simulation Container Overflow Handling (overflow: hidden | auto)
  CHECK B: Uniform H1 Title Font Size (within 2px tolerance across all 398 models)
  CHECK C: Uniform Simulation Container Margins & Padding
  CHECK D: Dashboard Inline Navigation (Modal iframe viewer, NO target="_blank" on model cards)
  CHECK E: Physics Rendering Line Width (ctx.lineWidth >= 2, zero 1px hairline rendering)
  CHECK F: High-DPI Scaling (window.devicePixelRatio and ctx.scale)
  CHECK G: Animation Loop Integrity (requestAnimationFrame, zero setInterval/setTimeout for rendering)
  CHECK H: Theme Toggle Functionality Preservation (DOM button, CSS tokens, JS reactive sync)

Usage:
  python3 scripts/verify_ui_ux_rendering.py                  # Run all checks across all models & index.html
  python3 scripts/verify_ui_ux_rendering.py --all            # Explicit all checks mode
  python3 scripts/verify_ui_ux_rendering.py --check <LETTER> # Run single check (A, B, C, D, E, F, G, H, I)
  python3 scripts/verify_ui_ux_rendering.py --json           # Output JSON formatted results
  python3 scripts/verify_ui_ux_rendering.py -v, --verbose    # Output comprehensive per-file details
  python3 scripts/verify_ui_ux_rendering.py --sample [N]     # Sample N models (default 20)
  python3 scripts/verify_ui_ux_rendering.py models/folder/   # Test specific directory or files
"""

import argparse
import json
import os
import random
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, NamedTuple, Optional, Set, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
MODELS_DIR = REPO_ROOT / "models"
INDEX_HTML = REPO_ROOT / "index.html"


class CheckResult(NamedTuple):
    check_id: str
    check_name: str
    passed: bool
    message: str
    violations: List[str]


class ModelValidationResult:
    def __init__(self, file_path: Path):
        self.path = file_path
        self.rel_path = str(file_path.relative_to(REPO_ROOT)) if REPO_ROOT in file_path.parents else str(file_path)
        self.checks: Dict[str, CheckResult] = {}
        self.h1_px: Optional[float] = None

    @property
    def passed(self) -> bool:
        return all(c.passed for c in self.checks.values())


# ============================================================================
# CHECK A: Simulation Container Overflow Handling
# ============================================================================
def check_a_container_overflow(clean_style: str, rel_path: str) -> CheckResult:
    rule_id = "CHECK_A"
    name = "Simulation Container Overflow Handling"

    all_ov_matches = []
    found_container = False
    for block in re.finditer(r"([^{]+)\{([^}]+)\}", clean_style):
        selectors = [s.strip() for s in block.group(1).split(",")]
        if any(s in ["main", ".sim-container", ".simulation-viewport"] for s in selectors):
            found_container = True
            decl = block.group(2)
            ov_matches = re.findall(r"\boverflow(?:-[xy])?\s*:\s*([^;]+);", decl, re.IGNORECASE)
            all_ov_matches.extend(ov_matches)

    if not found_container:
        return CheckResult(rule_id, name, False, "No simulation container CSS rule found (<main> / .sim-container)", ["missing container rule"])

    if not all_ov_matches:
        return CheckResult(rule_id, name, False, "Missing overflow property on simulation container", ["no overflow property found"])

    effective_ov = all_ov_matches[-1].strip().lower()
    if any(val in effective_ov for val in ["hidden", "auto", "clip"]):
        return CheckResult(rule_id, name, True, f"Container has valid overflow: {effective_ov}", [])
    return CheckResult(rule_id, name, False, f"Invalid overflow value: '{effective_ov}' (expected 'hidden' or 'auto')", [effective_ov])


# ============================================================================
# CHECK B: H1 Title Font Size Extraction
# ============================================================================
def check_b_h1_font_size(clean_style: str, body_html: str, rel_path: str) -> Tuple[CheckResult, Optional[float]]:
    rule_id = "CHECK_B"
    name = "Uniform H1 Title Font Size"

    # Inline style on <h1> tag takes highest precedence
    inline_h1 = re.search(r"<h1[^>]*style=[\"']([^\"']+)[\"']", body_html, re.IGNORECASE)
    fs_str = None
    if inline_h1:
        fs_m = re.search(r"font-size\s*:\s*([^;!]+)", inline_h1.group(1), re.IGNORECASE)
        if fs_m:
            fs_str = fs_m.group(1).strip()

    if not fs_str:
        for block in re.finditer(r"([^{]+)\{([^}]+)\}", clean_style):
            selectors = [s.strip() for s in block.group(1).split(",")]
            if any(s == "h1" for s in selectors):
                fs_matches = re.findall(r"\bfont-size\s*:\s*([^;!]+);", block.group(2), re.IGNORECASE)
                if fs_matches:
                    fs_str = fs_matches[-1].strip()

    if not fs_str:
        return CheckResult(rule_id, name, False, "No font-size specified for <h1>", ["missing font-size"]), None

    # Normalize units to px (base 16px)
    px_val = None
    fs_lower = fs_str.lower()
    if fs_lower.endswith("rem"):
        try:
            px_val = float(fs_lower[:-3].strip()) * 16.0
        except ValueError:
            pass
    elif fs_lower.endswith("em"):
        try:
            px_val = float(fs_lower[:-2].strip()) * 16.0
        except ValueError:
            pass
    elif fs_lower.endswith("px"):
        try:
            px_val = float(fs_lower[:-2].strip())
        except ValueError:
            pass

    if px_val is None:
        return CheckResult(rule_id, name, False, f"Unable to parse <h1> font-size '{fs_str}' to pixels", [fs_str]), None

    return CheckResult(rule_id, name, True, f"<h1> font-size: {fs_str} ({px_val:.1f}px)", []), px_val


# ============================================================================
# CHECK C: Uniform Simulation Container Margins & Padding
# ============================================================================
def check_c_container_margins_padding(clean_style: str, rel_path: str) -> CheckResult:
    rule_id = "CHECK_C"
    name = "Uniform Simulation Container Spacing (Margin & Padding)"

    all_mg_matches = []
    all_pd_matches = []
    found_container = False

    for block in re.finditer(r"([^{]+)\{([^}]+)\}", clean_style):
        selectors = [s.strip() for s in block.group(1).split(",")]
        if any(s in ["main", ".sim-container", ".simulation-viewport"] for s in selectors):
            found_container = True
            decl = block.group(2)
            mg_matches = re.findall(r"(?<!-)\bmargin\s*:\s*([^;]+);", decl, re.IGNORECASE)
            pd_matches = re.findall(r"(?<!-)\bpadding\s*:\s*([^;]+);", decl, re.IGNORECASE)
            all_mg_matches.extend(mg_matches)
            all_pd_matches.extend(pd_matches)

    if not found_container:
        return CheckResult(rule_id, name, False, "No simulation container rule found", ["missing container rule"])

    if not all_mg_matches or not all_pd_matches:
        return CheckResult(rule_id, name, False, "Missing margin or padding on simulation container", ["missing margin/padding"])

    eff_mg = re.sub(r"\s+", " ", all_mg_matches[-1].strip().lower())
    eff_pd = re.sub(r"\s+", " ", all_pd_matches[-1].strip().lower())

    valid_margins = {"0 auto 24px auto", "0 auto 24px"}
    valid_paddings = {"24px", "var(--spacing-lg, 24px)"}

    issues = []
    if eff_mg not in valid_margins:
        issues.append(f"Non-standard margin: '{eff_mg}' (expected '0 auto 24px auto')")
    if eff_pd not in valid_paddings:
        issues.append(f"Non-standard padding: '{eff_pd}' (expected '24px')")

    if issues:
        return CheckResult(rule_id, name, False, "; ".join(issues), issues)

    return CheckResult(rule_id, name, True, f"Uniform spacing verified (margin: {eff_mg}, padding: {eff_pd})", [])


# ============================================================================
# CHECK D: Dashboard Inline Navigation & Iframe Modal Viewer
# ============================================================================
def check_d_dashboard_inline_navigation(index_path: Path) -> CheckResult:
    rule_id = "CHECK_D"
    name = "Dashboard Inline Navigation (Iframe Modal Viewer)"

    if not index_path.exists():
        return CheckResult(rule_id, name, False, f"index.html not found at {index_path}", ["missing index.html"])

    content = index_path.read_text(encoding="utf-8", errors="replace")
    violations = []

    # 1. Zero target="_blank" on model cards
    anchors = re.findall(r"<a\b[^>]*>", content, re.IGNORECASE)
    cards_with_target_blank = []
    card_count = 0
    for a in anchors:
        if "model-card" in a:
            card_count += 1
            if re.search(r"target\s*=\s*[\"']_blank[\"']", a, re.IGNORECASE):
                cards_with_target_blank.append(a)

    if cards_with_target_blank:
        violations.append(f"Found {len(cards_with_target_blank)} model card(s) with target='_blank' (expected 0; must open inline)")

    # 2. Inline iframe element presence
    has_iframe = bool(re.search(r"<iframe\b[^>]*>", content, re.IGNORECASE))
    if not has_iframe:
        violations.append("Missing inline <iframe> element in index.html for modal viewing")

    # 3. Modal container presence
    has_modal = bool(re.search(r"id=[\"'](?:model-modal|modal-viewer|modalViewer)[\"']|class=[\"'][^\"']*\bmodal-(?:overlay|viewer|dialog)\b", content, re.IGNORECASE))
    if not has_modal:
        violations.append("Missing modal container element (<div id='model-modal'> or .modal-overlay)")

    # 4. Visible close button presence
    has_close_btn = bool(re.search(r"id=[\"']modal-close[\"']|class=[\"'][^\"']*\bmodal-close\b[^\"']*[\"']|aria-label=[\"']Close[^\"']*[\"']", content, re.IGNORECASE))
    if not has_close_btn:
        violations.append("Missing visible close button in modal (<button id='modal-close'>)")

    # 5. JavaScript event wiring
    scripts = "\n".join(re.findall(r"<script[^>]*>(.*?)</script>", content, re.DOTALL | re.IGNORECASE))
    has_open_handler = bool(re.search(r"\.model-card\b|\bcard\.addEventListener|\bopenModal\b", scripts, re.IGNORECASE))
    has_close_handler = bool(re.search(r"\bcloseModal\b|modalClose|modal-close|e\.key\s*===\s*['\"]Escape['\"]", scripts, re.IGNORECASE))
    if not (has_open_handler and has_close_handler):
        violations.append("JavaScript missing modal open or close click handlers for inline viewer")

    if violations:
        return CheckResult(rule_id, name, False, "; ".join(violations), violations)

    return CheckResult(rule_id, name, True, f"Dashboard 100% verified inline navigation ({card_count} cards, modal iframe, close button, zero target=_blank)", [])


# ============================================================================
# CHECK E: Physics Rendering Line Width (ctx.lineWidth >= 2)
# ============================================================================
def check_e_line_width(clean_js: str, rel_path: str) -> CheckResult:
    rule_id = "CHECK_E"
    name = "Physics Rendering Line Width (ctx.lineWidth >= 2)"

    lw_matches = list(re.finditer(r"\b(?:ctx|context)\.lineWidth\s*=\s*([^;]+);", clean_js))
    violations = []
    total_assignments = len(lw_matches)

    if total_assignments == 0:
        return CheckResult(
            rule_id,
            name,
            False,
            "No ctx.lineWidth assignment found (canvas defaults to 1px hairline rendering; must explicitly set ctx.lineWidth >= 2)",
            ["no ctx.lineWidth assignment found"]
        )

    for m in lw_matches:
        expr = m.group(1).strip()
        num_m = re.match(r"^([0-9]+(?:\.[0-9]+)?)$", expr)
        if num_m:
            val = float(num_m.group(1))
            if val < 2.0:
                violations.append(f"lineWidth = {val} (< 2.0)")
            continue

        # Ternary expressions check (e.g. cond ? 2.5 : 1)
        if "?" in expr and ":" in expr:
            ternary_vals = re.findall(r"[\?:]\s*\(?\s*([0-9]+(?:\.[0-9]+)?)\b", expr)
            for tv in ternary_vals:
                val = float(tv)
                if val < 2.0:
                    violations.append(f"lineWidth = {expr} (branch {val} < 2.0)")

        # Math.max check (e.g. Math.max(1, ...))
        max_m = re.match(r"Math\.max\s*\(\s*([0-9]+(?:\.[0-9]+)?)\s*,", expr)
        if max_m:
            val = float(max_m.group(1))
            if val < 2.0:
                violations.append(f"lineWidth = {expr} (Math.max min {val} < 2.0)")

    if violations:
        unique_v = sorted(set(violations))
        return CheckResult(
            rule_id,
            name,
            False,
            f"Found {len(violations)} hairline lineWidth assignment(s) < 2.0: {', '.join(unique_v[:5])}",
            violations,
        )

    return CheckResult(rule_id, name, True, f"All {total_assignments} canvas lineWidth assignments >= 2.0 (zero hairline strokes)", [])


# ============================================================================
# CHECK F: High-DPI Scaling (window.devicePixelRatio and ctx.scale)
# ============================================================================
def check_f_hidpi_dpr(clean_js: str, rel_path: str) -> CheckResult:
    rule_id = "CHECK_F"
    name = "High-DPI Display Scaling (devicePixelRatio & ctx.scale)"

    has_dpr = "devicePixelRatio" in clean_js
    has_scale = bool(re.search(r"\b(?:ctx|context)\.scale\s*\(", clean_js))

    if not has_dpr:
        return CheckResult(rule_id, name, False, "Missing window.devicePixelRatio high-DPI retina scaling", ["missing devicePixelRatio"])
    if not has_scale:
        return CheckResult(rule_id, name, False, "Missing ctx.scale() for high-DPI scaling", ["missing ctx.scale"])

    return CheckResult(rule_id, name, True, "High-DPI canvas retina scaling fully verified (devicePixelRatio and ctx.scale)", [])


# ============================================================================
# CHECK G: Animation Loop Integrity (requestAnimationFrame)
# ============================================================================
def check_g_raf_animation(clean_js: str, rel_path: str) -> CheckResult:
    rule_id = "CHECK_G"
    name = "Animation Loop Integrity (requestAnimationFrame, zero setInterval/setTimeout)"

    has_raf = bool(re.search(r"\brequestAnimationFrame\s*\(", clean_js))
    has_set_interval = bool(re.search(r"\bsetInterval\s*\(", clean_js))
    has_set_timeout = bool(re.search(r"\bsetTimeout\s*\(", clean_js))

    violations = []
    if not has_raf:
        violations.append("Missing requestAnimationFrame continuous animation loop")
    if has_set_interval:
        violations.append("Contains forbidden setInterval call (animation must use requestAnimationFrame)")
    if has_set_timeout:
        violations.append("Contains forbidden setTimeout call for rendering")

    if violations:
        return CheckResult(rule_id, name, False, "; ".join(violations), violations)

    return CheckResult(rule_id, name, True, "Animation loop driven by requestAnimationFrame (zero setInterval/setTimeout)", [])


# ============================================================================
# CHECK H: Theme Toggle Functionality Preservation
# ============================================================================
def check_h_theme_toggle_preserved(content: str, clean_style: str, clean_js: str, rel_path: str) -> CheckResult:
    rule_id = "CHECK_H"
    name = "Theme Toggle Functionality Preservation"

    violations = []

    # 1. DOM toggle button
    has_toggle_btn = bool(re.search(r"id=[\"']theme-toggle[\"']", content, re.IGNORECASE))
    if not has_toggle_btn:
        violations.append("Missing #theme-toggle button in HTML header")

    # 2. Dual-theme CSS token contracts
    has_light_theme = bool(re.search(r"\[data-theme=[\"']light[\"']\]", clean_style, re.IGNORECASE))
    if not has_light_theme:
        violations.append("Missing [data-theme='light'] CSS token definition block")

    # 3. Theme change event and dynamic extraction
    has_listener = bool(
        re.search(r"['\"]themechange['\"]", clean_js) or
        re.search(r"['\"]#theme-toggle['\"]|\bthemeToggleBtn\b|\btheme-toggle\b", clean_js)
    )
    if not has_listener:
        violations.append("Missing themechange or #theme-toggle click listener in script")

    # 4. Active canvas background painting
    has_fill_rect = bool(re.search(r"\b(?:ctx|context)\.fillRect\s*\(\s*0\s*,\s*0\s*,", clean_js))
    if not has_fill_rect:
        violations.append("Canvas does not actively paint theme background (missing ctx.fillRect(0, 0, ...))")

    if violations:
        return CheckResult(rule_id, name, False, "; ".join(violations), violations)

    return CheckResult(rule_id, name, True, "Theme toggle functionality fully preserved (DOM, tokens, listener, active fillRect)", [])


# ============================================================================
# CHECK I: Mobile Header Clearance & Media Query Cascade Order
# ============================================================================
def check_i_mobile_header_cascade(clean_style: str, rel_path: str) -> CheckResult:
    rule_id = "CHECK_I"
    name = "Mobile Header Clearance & Media Query Cascade Order"

    # 1. Locate @media (max-width: 768px) block(s)
    mq_matches = list(re.finditer(r"@media\s*\([^{]*max-width\s*:\s*768px[^{]*\)\s*\{", clean_style, re.IGNORECASE))
    if not mq_matches:
        return CheckResult(
            rule_id,
            name,
            False,
            "Missing @media (max-width: 768px) responsive block",
            ["missing @media (max-width: 768px)"]
        )

    # Extract full text and character ranges of all 768px media blocks (handling nested braces)
    mq_blocks: List[Tuple[int, int, str]] = []
    for m in mq_matches:
        mq_start = m.start()
        start_brace = m.end() - 1
        depth = 1
        i = start_brace + 1
        while i < len(clean_style) and depth > 0:
            if clean_style[i] == '{':
                depth += 1
            elif clean_style[i] == '}':
                depth -= 1
            i += 1
        mq_block_content = clean_style[start_brace + 1:i - 1]
        mq_blocks.append((mq_start, i, mq_block_content))

    # 2. Check for theme toggle position: static inside media query
    has_static = False
    has_important = False
    winning_mq_start = -1

    for mq_start, mq_end, block_content in mq_blocks:
        static_m = re.search(
            r"(?:figma-pill|theme-toggle)[^{]*\{[^}]*\bposition\s*:\s*static(\s*!important)?",
            block_content,
            re.IGNORECASE
        )
        if static_m:
            has_static = True
            winning_mq_start = mq_start
            if static_m.group(1):
                has_important = True
            break

    if not has_static:
        return CheckResult(
            rule_id,
            name,
            False,
            "Media query does not reset theme toggle to position: static",
            ["missing position: static in media query"]
        )

    # 3. Find base rules declaring position: absolute on theme toggle
    abs_matches = list(re.finditer(
        r"(?:\.figma-pill|\.theme-toggle|button#theme-toggle)[^{]*\{[^}]*\bposition\s*:\s*absolute(\s*!important)?",
        clean_style,
        re.IGNORECASE
    ))

    violations = []
    for am in abs_matches:
        abs_pos = am.start()
        base_important = bool(am.group(1))
        is_inside_mq = any(mq_s <= abs_pos < mq_e for mq_s, mq_e, _ in mq_blocks)
        if not is_inside_mq:
            if abs_pos > winning_mq_start and not has_important:
                violations.append(
                    f"Base rule with position: absolute (offset {abs_pos}) appears AFTER @media (max-width: 768px) "
                    f"(offset {winning_mq_start}), causing cascade override of position: static"
                )
            elif base_important and not has_important:
                violations.append("Base rule has position: absolute !important, preventing media query override")

    if violations:
        return CheckResult(
            rule_id,
            name,
            False,
            f"CSS Cascade Defect: {len(violations)} competing rule(s) override media query position: static: {violations[0]}",
            violations
        )

    return CheckResult(
        rule_id,
        name,
        True,
        "Mobile header clearance & media query cascade order verified (position: static wins on <= 768px)",
        []
    )


# ============================================================================
# Model File Validator
# ============================================================================
def validate_model(file_path: Path) -> ModelValidationResult:
    res = ModelValidationResult(file_path)
    try:
        content = file_path.read_text(encoding="utf-8", errors="replace")
    except Exception as exc:
        for cid in ["CHECK_A", "CHECK_B", "CHECK_C", "CHECK_E", "CHECK_F", "CHECK_G", "CHECK_H", "CHECK_I"]:
            res.checks[cid] = CheckResult(cid, cid, False, f"Failed to read file: {exc}", [str(exc)])
        return res

    styles = "\n".join(re.findall(r"<style[^>]*>(.*?)</style>", content, re.DOTALL | re.IGNORECASE))
    clean_style = re.sub(r"/\*.*?\*/", "", styles, flags=re.DOTALL)

    scripts = "\n".join(re.findall(r"<script(?![^>]*src=)[^>]*>(.*?)</script>", content, re.DOTALL | re.IGNORECASE))
    clean_js = re.sub(r"/\*.*?\*/", "", scripts, flags=re.DOTALL)
    clean_js = re.sub(r"//[^\n]*", "", clean_js)

    body_match = re.search(r"<body[^>]*>(.*?)</body>", content, re.DOTALL | re.IGNORECASE)
    body_html = body_match.group(1) if body_match else content

    res.checks["CHECK_A"] = check_a_container_overflow(clean_style, res.rel_path)
    b_res, h1_px = check_b_h1_font_size(clean_style, body_html, res.rel_path)
    res.checks["CHECK_B"] = b_res
    res.h1_px = h1_px
    res.checks["CHECK_C"] = check_c_container_margins_padding(clean_style, res.rel_path)
    res.checks["CHECK_E"] = check_e_line_width(clean_js, res.rel_path)
    res.checks["CHECK_F"] = check_f_hidpi_dpr(clean_js, res.rel_path)
    res.checks["CHECK_G"] = check_g_raf_animation(clean_js, res.rel_path)
    res.checks["CHECK_H"] = check_h_theme_toggle_preserved(content, clean_style, clean_js, res.rel_path)
    res.checks["CHECK_I"] = check_i_mobile_header_cascade(clean_style, res.rel_path)

    return res


def main():
    parser = argparse.ArgumentParser(
        description="Engineering Physics Acceptance Verification Suite (Milestone 2026-09-06T09:43:29Z: Checks A-I)"
    )
    parser.add_argument("paths", nargs="*", help="Optional specific model file or directory paths to verify")
    parser.add_argument("--all", action="store_true", help="Run full acceptance checks across all 398 models & index.html")
    parser.add_argument(
        "--check",
        choices=["A", "B", "C", "D", "E", "F", "G", "H", "I", "a", "b", "c", "d", "e", "f", "g", "h", "i"],
        help="Run only a specific check (A: overflow, B: h1, C: spacing, D: dashboard, E: lineWidth, F: highDPI, G: rAF, H: theme, I: cascade)"
    )
    parser.add_argument("--sample", type=int, nargs="?", const=20, default=None, metavar="N", help="Verify N random models (default: 20)")
    parser.add_argument("--seed", type=int, default=None, help="Set random seed for reproducible sampling")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show detailed per-file output and full failure lists")
    parser.add_argument("--json", action="store_true", help="Output results in machine-readable JSON format")
    args = parser.parse_args()

    selected_check = args.check.upper() if args.check else None

    # Check D (Dashboard) standalone
    if selected_check == "D":
        d_res = check_d_dashboard_inline_navigation(INDEX_HTML)
        if args.json:
            out = {
                "check": "CHECK_D",
                "name": d_res.check_name,
                "target": str(INDEX_HTML.relative_to(REPO_ROOT)),
                "passed": d_res.passed,
                "message": d_res.message,
                "violations": d_res.violations,
            }
            print(json.dumps(out, indent=2))
        else:
            tag = "[PASS]" if d_res.passed else "[FAIL]"
            print(f"\n{tag} CHECK_D: {d_res.check_name}")
            print(f"Target:   {INDEX_HTML.relative_to(REPO_ROOT)}")
            print(f"Message:  {d_res.message}")
            if not d_res.passed and d_res.violations:
                print("\nViolations:")
                for v in d_res.violations:
                    print(f"  ✗ {v}")
        sys.exit(0 if d_res.passed else 1)

    all_models = sorted([
        f for f in MODELS_DIR.glob("**/*.html")
        if not any(ex in f.parts for ex in ["misc", "__pycache__"])
    ])

    if args.seed is not None:
        random.seed(args.seed)

    if args.sample is not None:
        sample_count = min(args.sample, len(all_models))
        target_files = random.sample(all_models, sample_count)
    elif args.paths:
        target_files = []
        for p in args.paths:
            rp = Path(p).resolve()
            if rp.is_file() and rp.suffix == ".html":
                target_files.append(rp)
            elif rp.is_dir():
                target_files.extend(sorted(rp.glob("**/*.html")))
            else:
                print(f"Warning: path not found or not an HTML file: {p}", file=sys.stderr)
        if not target_files:
            print("Error: No matching HTML model files found for provided paths.", file=sys.stderr)
            sys.exit(1)
    else:
        target_files = all_models

    results = [validate_model(f) for f in target_files]
    total_models = len(results)

    # Cross-catalog H1 check
    h1_sizes = [r.h1_px for r in results if r.h1_px is not None]
    if h1_sizes and len(h1_sizes) == total_models:
        sorted_h1 = sorted(h1_sizes)
        median_h1 = sorted_h1[len(sorted_h1) // 2]
        min_h1 = min(h1_sizes)
        max_h1 = max(h1_sizes)
        h1_spread = max_h1 - min_h1

        for r in results:
            if r.h1_px is not None and abs(r.h1_px - median_h1) > 2.0:
                r.checks["CHECK_B"] = CheckResult(
                    "CHECK_B",
                    "Uniform H1 Title Font Size",
                    False,
                    f"<h1> font-size {r.h1_px:.1f}px deviates by >2px from catalog baseline ({median_h1:.1f}px)",
                    [f"{r.h1_px:.1f}px"]
                )
        h1_passed = h1_spread <= 2.0 and all(r.checks["CHECK_B"].passed for r in results)
    else:
        min_h1 = max_h1 = h1_spread = 0.0
        h1_passed = False

    # Check D execution (for multi-check mode)
    check_d_res = check_d_dashboard_inline_navigation(INDEX_HTML)

    check_ids = ["CHECK_A", "CHECK_B", "CHECK_C", "CHECK_E", "CHECK_F", "CHECK_G", "CHECK_H", "CHECK_I"]
    check_pass_counts = {cid: sum(1 for r in results if r.checks[cid].passed) for cid in check_ids}

    # Single check execution (A, B, C, E, F, G, H)
    if selected_check and selected_check in ["A", "B", "C", "E", "F", "G", "H", "I"]:
        cid = f"CHECK_{selected_check}"
        passed_c = check_pass_counts[cid]
        failed_c = total_models - passed_c
        all_passed = (failed_c == 0)
        name = results[0].checks[cid].check_name if results else cid

        failures = [
            {"path": r.rel_path, "message": r.checks[cid].message, "violations": r.checks[cid].violations}
            for r in results if not r.checks[cid].passed
        ]

        if args.json:
            print(json.dumps({
                "check": cid,
                "name": name,
                "total": total_models,
                "passed": passed_c,
                "failed": failed_c,
                "all_passed": all_passed,
                "failures": failures
            }, indent=2))
        else:
            tag = "[PASS]" if all_passed else "[FAIL]"
            print(f"\n{tag} {cid}: {name}")
            print(f"Models Evaluated: {total_models}")
            print(f"Models Passing:   {passed_c} ({passed_c/total_models*100:.1f}%)")
            print(f"Models Failing:   {failed_c} ({failed_c/total_models*100:.1f}%)")

            if failed_c > 0:
                limit = len(failures) if args.verbose else min(5, len(failures))
                print(f"\nFailures ({'showing all ' + str(len(failures)) if args.verbose else 'showing first ' + str(limit)}):")
                for f in failures[:limit]:
                    print(f"  ✗ {f['path']}: {f['message']}")
                if not args.verbose and len(failures) > 5:
                    print(f"  ... and {len(failures) - 5} more (use --verbose or -v to view all)")
            elif args.verbose:
                print("\nAll models passed:")
                for r in results:
                    print(f"  ✓ {r.rel_path}: {r.checks[cid].message}")

        sys.exit(0 if all_passed else 1)

    # Full acceptance suite execution
    all_model_checks_ok = all(check_pass_counts[cid] == total_models for cid in check_ids)
    all_ok = all_model_checks_ok and check_d_res.passed

    check_titles = {
        "CHECK_A": "Container Overflow Handling (overflow: hidden/auto)",
        "CHECK_B": f"Uniform H1 Font Size (Spread: {h1_spread:.1f}px, Limit: 2.0px)",
        "CHECK_C": "Uniform Container Spacing (Margin & Padding)",
        "CHECK_D": "Dashboard Inline Navigation (Modal Iframe Viewer)",
        "CHECK_E": "Physics Rendering Line Width (ctx.lineWidth >= 2)",
        "CHECK_F": "High-DPI Retina Scaling (devicePixelRatio & scale)",
        "CHECK_G": "Continuous Animation Loop (requestAnimationFrame)",
        "CHECK_H": "Theme Toggle Functionality Preservation",
        "CHECK_I": "Mobile Header Clearance & Media Query Cascade Order",
    }

    if args.json:
        checks_data = {}
        for cid in ["CHECK_A", "CHECK_B", "CHECK_C"]:
            checks_data[cid] = {
                "name": check_titles[cid],
                "total": total_models,
                "passed": check_pass_counts[cid],
                "failed": total_models - check_pass_counts[cid],
                "all_passed": check_pass_counts[cid] == total_models,
            }
        checks_data["CHECK_D"] = {
            "name": check_titles["CHECK_D"],
            "total": 1,
            "passed": 1 if check_d_res.passed else 0,
            "failed": 0 if check_d_res.passed else 1,
            "all_passed": check_d_res.passed,
            "message": check_d_res.message,
            "violations": check_d_res.violations,
        }
        for cid in ["CHECK_E", "CHECK_F", "CHECK_G", "CHECK_H", "CHECK_I"]:
            checks_data[cid] = {
                "name": check_titles[cid],
                "total": total_models,
                "passed": check_pass_counts[cid],
                "failed": total_models - check_pass_counts[cid],
                "all_passed": check_pass_counts[cid] == total_models,
            }

        failures_by_check = {}
        for cid in check_ids:
            fails = [
                {"path": r.rel_path, "message": r.checks[cid].message, "violations": r.checks[cid].violations}
                for r in results if not r.checks[cid].passed
            ]
            if fails:
                failures_by_check[cid] = fails

        passed_checks_count = sum(1 for c in checks_data.values() if c["all_passed"])
        out = {
            "summary": {
                "total_models": total_models,
                "all_passed": all_ok,
                "checks_passed": passed_checks_count,
                "checks_total": len(checks_data),
            },
            "checks": checks_data,
            "failures_by_check": failures_by_check,
        }
        print(json.dumps(out, indent=2))
        sys.exit(0 if all_ok else 1)

    print("\n" + "=" * 80)
    print("ENGINEERING PHYSICS ACCEPTANCE VERIFICATION AUDIT (CHECKS A - I)")
    print("=" * 80)
    print(f"Models Evaluated:        {total_models}")
    print("-" * 80)

    for cid in ["CHECK_A", "CHECK_B", "CHECK_C"]:
        c = check_pass_counts[cid]
        pct = c / total_models * 100 if total_models else 0.0
        tag = "[PASS]" if c == total_models else "[FAIL]"
        print(f"  {cid}: {check_titles[cid]:<52} {c:>3}/{total_models:>3} ({pct:>5.1f}%) {tag}")

    d_tag = "[PASS]" if check_d_res.passed else "[FAIL]"
    print(f"  CHECK_D: {check_titles['CHECK_D']:<52} {'1/1' if check_d_res.passed else '0/1':>7} {'(100.0%)' if check_d_res.passed else '  (0.0%)'} {d_tag}")
    if not check_d_res.passed:
        for v in check_d_res.violations:
            print(f"           ↳ {v}")

    for cid in ["CHECK_E", "CHECK_F", "CHECK_G", "CHECK_H", "CHECK_I"]:
        c = check_pass_counts[cid]
        pct = c / total_models * 100 if total_models else 0.0
        tag = "[PASS]" if c == total_models else "[FAIL]"
        print(f"  {cid}: {check_titles[cid]:<52} {c:>3}/{total_models:>3} ({pct:>5.1f}%) {tag}")

    print("=" * 80)
    if all_ok:
        print("ACCEPTANCE STATUS: 100% PASSED (All Checks A-I Compliant)")
    else:
        failing_checks = [cid for cid in check_ids if check_pass_counts[cid] < total_models]
        if not check_d_res.passed:
            failing_checks.append("CHECK_D")
        print(f"ACCEPTANCE STATUS: PENDING COMPLETION ({len(failing_checks)} check(s) requiring remediation: {', '.join(sorted(failing_checks))})")
    print("=" * 80 + "\n")

    if args.verbose:
        for cid in check_ids:
            fails = [r for r in results if not r.checks[cid].passed]
            if fails:
                print(f"--- Verbose Failure Breakdown for {cid} ({len(fails)} files) ---")
                for r in fails:
                    print(f"  ✗ {r.rel_path}: {r.checks[cid].message}")
                print()

    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
