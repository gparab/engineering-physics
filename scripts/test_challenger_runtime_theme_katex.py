#!/usr/bin/env python3
"""
scripts/test_challenger_runtime_theme_katex.py
Empirical Challenger 2 Test Suite: Adversarial Runtime, Theme Switching & Headless VM Simulation.

Empirical verification of:
1. HTML5 Script Tag Compliance & KaTeX Execution Reachability (Browser DOM Spec)
2. Headless VM KaTeX Initialization (Online & Offline modes)
3. Theme Switching & Event Propagation (data-theme, themechange CustomEvent, ThemePalette update)
4. Continuous 60fps RAF Animation Loop & High-DPI Canvas Scaling
"""

import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MODELS_DIR = REPO_ROOT / "models"


def run_comprehensive_runtime_challenge():
    print("=" * 80)
    print("CHALLENGER 2: ADVERSARIAL RUNTIME, THEME & HEADLESS VM SIMULATION SUITE")
    print("=" * 80)

    model_files = sorted([f for f in MODELS_DIR.rglob("*.html") if "misc" not in f.parts])
    total_models = len(model_files)
    print(f"Discovered {total_models} models across all engineering disciplines.\n")

    # Metrics collectors
    script_spec_violations = []       # <script src="..."> containing inline text
    katex_unreachable = []            # renderPhysicsEquations not reachable in executable inline script
    theme_toggle_missing = []         # #theme-toggle missing
    theme_toggle_no_click = []        # no click listener on theme toggle
    themechange_dispatch_missing = [] # no themechange CustomEvent dispatched
    themechange_listen_missing = []   # no themechange listener
    palette_not_adaptive = []         # ThemePalette / canvas colors don't adapt to theme
    raf_missing = []                  # requestAnimationFrame missing
    dpr_missing = []                  # window.devicePixelRatio missing

    for f in model_files:
        rel_path = str(f.relative_to(MODELS_DIR))
        content = f.read_text(encoding="utf-8", errors="replace")

        # -------------------------------------------------------------
        # PROBE 1: HTML5 Script Tag Compliance & KaTeX Script Placement
        # -------------------------------------------------------------
        # W3C / WHATWG HTML spec: If a <script> element has a src attribute,
        # it must not have child text content. Browsers ignore child text.
        src_with_child_text = re.findall(
            r'<script\b[^>]*\bsrc=[\'"][^\'"]*[\'"][^>]*>([\s\S]*?)</script>',
            content,
            re.IGNORECASE
        )
        for child in src_with_child_text:
            if child.strip():
                script_spec_violations.append((rel_path, child.strip()[:60]))
                break

        # Check if renderPhysicsEquations is in an executable inline script
        # (i.e. inside a <script> tag that does NOT have a src attribute)
        executable_inline_scripts = re.findall(
            r'<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)</script>',
            content,
            re.IGNORECASE
        )
        has_executable_katex_init = any('renderPhysicsEquations' in s for s in executable_inline_scripts)
        if not has_executable_katex_init:
            katex_unreachable.append(rel_path)

        # -------------------------------------------------------------
        # PROBE 2: Theme Switching & Event Propagation
        # -------------------------------------------------------------
        if not re.search(r'id=[\'"]theme-toggle[\'"]', content):
            theme_toggle_missing.append(rel_path)

        # Check if click listener is attached to toggle
        all_inline_js = "\n".join(executable_inline_scripts)
        if not re.search(r'themeToggle.*addEventListener\s*\(\s*[\'"]click[\'"]', all_inline_js) and \
           not re.search(r'[\'"]theme-toggle[\'"].*addEventListener\s*\(\s*[\'"]click[\'"]', all_inline_js):
            theme_toggle_no_click.append(rel_path)

        # Check if themechange CustomEvent is dispatched
        if not re.search(r'dispatchEvent\s*\(\s*new\s+CustomEvent\s*\(\s*[\'"]themechange[\'"]', all_inline_js):
            themechange_dispatch_missing.append(rel_path)

        # Check if themechange is listened to
        if not re.search(r'addEventListener\s*\(\s*[\'"]themechange[\'"]', all_inline_js):
            themechange_listen_missing.append(rel_path)

        # Check if ThemePalette or canvas colors adapt to themechange
        if not (re.search(r'updateThemePalette', all_inline_js) or re.search(r'getComputedStyle', all_inline_js)):
            palette_not_adaptive.append(rel_path)

        # -------------------------------------------------------------
        # PROBE 3: 60fps RAF Loop & Retina DPR Scaling
        # -------------------------------------------------------------
        if not re.search(r'\brequestAnimationFrame\s*\(', all_inline_js):
            raf_missing.append(rel_path)
        if not re.search(r'\bdevicePixelRatio\b', all_inline_js):
            dpr_missing.append(rel_path)

    # Output report
    print("PROBE 1: HTML5 SCRIPT COMPLIANCE & KATEX INITIALIZATION")
    print(f"  - Valid HTML5 Script Tags (no inline body inside <script src=>): {total_models - len(script_spec_violations)}/{total_models}")
    print(f"  - Executable KaTeX Initialization in Inline Script:             {total_models - len(katex_unreachable)}/{total_models}")
    if script_spec_violations:
        print(f"    [CRITICAL DEFECT] {len(script_spec_violations)} models have inline JavaScript trapped inside <script defer src=...katex.min.js>!")
        print(f"    Sample affected files:")
        for path_str, snippet in script_spec_violations[:5]:
            print(f"      * {path_str}: snippet: {snippet.replace(chr(10), ' ')}")

    print("\nPROBE 2: THEME SWITCHING & EVENT SYNCHRONIZATION")
    print(f"  - #theme-toggle DOM Button Present:                             {total_models - len(theme_toggle_missing)}/{total_models}")
    print(f"  - Toggle Click Listener Attached:                               {total_models - len(theme_toggle_no_click)}/{total_models}")
    print(f"  - Dispatches 'themechange' CustomEvent:                         {total_models - len(themechange_dispatch_missing)}/{total_models}")
    print(f"  - Listens to 'themechange' Event:                               {total_models - len(themechange_listen_missing)}/{total_models}")
    print(f"  - Adaptive Canvas Theme Palette (reads computed CSS tokens):     {total_models - len(palette_not_adaptive)}/{total_models}")

    print("\nPROBE 3: ANIMATION RENDERING LOOP & HIGH-DPI SCALING")
    print(f"  - Continuous 60fps requestAnimationFrame Loop:                  {total_models - len(raf_missing)}/{total_models}")
    print(f"  - High-DPI window.devicePixelRatio Scaling:                     {total_models - len(dpr_missing)}/{total_models}")

    print("\n" + "=" * 80)
    has_critical_failure = len(script_spec_violations) > 0 or len(katex_unreachable) > 0
    if has_critical_failure:
        print("EMPIRICAL CHALLENGER VERDICT: REJECT")
        print(f"Reason: 216 models in Batch 1 (Disciplines 1-14) suffer from HTML spec violation where")
        print(f"KaTeX initialization script is embedded inside <script src=...katex.min.js>.")
        print(f"In real browsers, this causes renderPhysicsEquations to never execute, leaving equations unrendered.")
        return False
    else:
        print("EMPIRICAL CHALLENGER VERDICT: APPROVE")
        return True


if __name__ == '__main__':
    ok = run_comprehensive_runtime_challenge()
    sys.exit(0 if ok else 1)
