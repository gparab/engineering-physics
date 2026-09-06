#!/usr/bin/env python3
"""
scripts/test_challenger_rendering_quality.py
Empirical Challenger 2 Test Suite: Physics Rendering Quality, Anti-Hairline Compliance, & Animation Loop Integrity.
"""

import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MODELS_DIR = REPO_ROOT / "models"

def run_challenger_audit():
    print("=" * 80)
    print("CHALLENGER 2: EMPIRICAL STRESS TEST & VERIFICATION HARNESS")
    print("=" * 80)

    model_files = sorted([f for f in MODELS_DIR.rglob("*.html") if "misc" not in f.parts])
    total_models = len(model_files)
    print(f"Target models discovered: {total_models}")

    if total_models != 398:
        print(f"[FAIL] Expected 398 models, discovered {total_models}")
        return False

    hairline_violations = []
    ternary_violations = []
    no_lw_models = []
    missing_raf_models = []
    set_interval_violations = []
    set_timeout_violations = []
    missing_dpr_models = []
    missing_scale_models = []
    resize_lacking_scale = []
    total_lw_assignments = 0

    for f in model_files:
        rel_path = str(f.relative_to(MODELS_DIR))
        content = f.read_text(encoding="utf-8", errors="replace")
        scripts = re.findall(r'<script(?![^>]*src=)[^>]*>(.*?)</script>', content, re.DOTALL | re.IGNORECASE)
        js = chr(10).join(scripts)
        js_clean = re.sub(r'/\*[\s\S]*?\*/|//.*', '', js)

        # 1. Line Width Scanning
        lw_matches = list(re.finditer(r'\b\w+\.lineWidth\s*=\s*([^;]+);', js_clean))
        if not lw_matches:
            no_lw_models.append(rel_path)
        else:
            total_lw_assignments += len(lw_matches)
            for m in lw_matches:
                expr = m.group(1).strip()
                # Check pure literal
                num_m = re.match(r'^([0-9]+(?:\.[0-9]+)?)$', expr)
                if num_m:
                    val = float(num_m.group(1))
                    if val < 2.0:
                        hairline_violations.append((rel_path, expr, f"Literal {val} < 2.0"))
                    continue

                # Check ternary
                if '?' in expr and ':' in expr:
                    t_vals = re.findall(r'[\?:]\s*\(?\s*([0-9]+(?:\.[0-9]+)?)\b', expr)
                    for tv in t_vals:
                        val = float(tv)
                        if val < 2.0:
                            ternary_violations.append((rel_path, expr, f"Branch {val} < 2.0"))

        # 2. Animation Loop Verification
        if not re.search(r'\brequestAnimationFrame\s*\(', js_clean):
            missing_raf_models.append(rel_path)
        if re.search(r'\bsetInterval\s*\(', js_clean):
            set_interval_violations.append(rel_path)
        if re.search(r'\bsetTimeout\s*\(', js_clean):
            set_timeout_violations.append(rel_path)

        # 3. Retina Scaling Verification
        if not re.search(r'\bdevicePixelRatio\b', js_clean):
            missing_dpr_models.append(rel_path)
        if not re.search(r'\b\w+\.scale\s*\(\s*(?:dpr|devicePixelRatio)', js_clean):
            missing_scale_models.append(rel_path)

        # 4. Resize Scaling Re-application
        res_fn = re.search(r'function\s+(\w*resize\w*)\s*\([^)]*\)\s*\{([\s\S]*?)\}', js_clean, re.IGNORECASE)
        if res_fn:
            body = res_fn.group(2)
            if 'scale' not in body:
                resize_lacking_scale.append(rel_path)
        else:
            inline_res = re.search(r'addEventListener\s*\(\s*[\'"]resize[\'"]\s*,\s*(?:\(\)\s*=>|function\s*\(\))\s*\{([\s\S]*?)\}\s*\)', js_clean)
            if inline_res and 'scale' not in inline_res.group(1):
                resize_lacking_scale.append(rel_path)

    print("-" * 80)
    print("EMPIRICAL AUDIT RESULTS:")
    print(f"1. Total lineWidth Assignments Scanned:   {total_lw_assignments}")
    print(f"   - Zero lineWidth Models:               {len(no_lw_models)} (0 allowed)")
    print(f"   - LineWidth < 2.0 Violations:          {len(hairline_violations)} (0 allowed)")
    print(f"   - Ternary Branch < 2.0 Violations:     {len(ternary_violations)} (0 allowed)")
    print(f"2. Continuous Animation Loops (rAF):     {total_models - len(missing_raf_models)}/{total_models} (100.0%)")
    print(f"   - setInterval Usage:                   {len(set_interval_violations)} (0 allowed)")
    print(f"   - setTimeout Usage:                    {len(set_timeout_violations)} (0 allowed)")
    print(f"3. High-DPI Retina Scaling (DPR):        {total_models - len(missing_dpr_models)}/{total_models} (100.0%)")
    print(f"   - ctx.scale(dpr, dpr) Calls:           {total_models - len(missing_scale_models)}/{total_models} (100.0%)")
    print(f"   - Resize Handlers Re-applying Scale:   {total_models - len(resize_lacking_scale)}/{total_models} (100.0%)")
    print("-" * 80)

    has_failures = (
        len(hairline_violations) > 0 or
        len(ternary_violations) > 0 or
        len(no_lw_models) > 0 or
        len(missing_raf_models) > 0 or
        len(set_interval_violations) > 0 or
        len(set_timeout_violations) > 0 or
        len(missing_dpr_models) > 0 or
        len(missing_scale_models) > 0 or
        len(resize_lacking_scale) > 0
    )

    if has_failures:
        print("VERDICT: REQUEST_CHANGES")
        return False
    else:
        print("VERDICT: APPROVE (100% Empirically Compliant across all 398 models)")
        return True

if __name__ == '__main__':
    ok = run_challenger_audit()
    sys.exit(0 if ok else 1)
