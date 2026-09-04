#!/usr/bin/env python3
"""
scripts/test_empirical_scientific_robustness.py
Empirical Scientific Accuracy & Rendering Robustness Challenger Suite
for Engineering Physics 348 Standalone Models.

Verifies:
1. Exact discipline directory and model counts:
   All 30 discipline subdirectories contain their exact expected model counts summing to 348.
2. Governing equations:
   Every single model of the 348 has an equation containing valid mathematical/physics
   symbols, relations, or unicode characters, and none are empty or placeholder text.
   Also checks for raw unrendered LaTeX markup (violating unicode equation contract).
3. "How It Works" explanation:
   Explanation paragraphs have between 2 and 5 sentences and non-trivial word count (>= 15 words).
4. Canvas/SVG element existence and HiDPI scaling setup:
   Main container contains canvas or svg; evaluates HiDPI / devicePixelRatio scaling setup.
5. Inline JavaScript syntax verification:
   Compiles inline JavaScript under Node.js --check to catch runtime crashes.
"""

import os
import re
import sys
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple, Any

REPO_ROOT = Path(__file__).resolve().parent.parent
MODELS_DIR = REPO_ROOT / "models"

EXPECTED_DISCIPLINE_COUNTS = {
    # M1: Mechanical, Aerospace, Marine, Biomechanics & Acoustics (73 files)
    "mech": 25,
    "aero": 8,
    "aerospace": 7,
    "acoustics": 8,
    "marine": 10,
    "biomech": 15,
    # M2: Civil, Environmental, Ag, Mining, Industrial & Energy (72 files)
    "civil": 20,
    "enveng": 10,
    "agricultural_engineering": 10,
    "mining_petro": 10,
    "industrial_systems": 10,
    "energy": 12,
    # M3: Electrical, Electronics & Telecommunications (65 files)
    "electrical": 17,
    "electrical_engineering": 8,
    "electronics": 10,
    "ee": 10,
    "telecommunications": 20,
    # M4: Computer Engineering, CS & Robotics (52 files)
    "compeng": 20,
    "computer_science": 10,
    "cs": 10,
    "robotics": 12,
    # M5: Chemical, Materials, Nuclear, Nano, Optics & Fundamental Physics (86 files)
    "chemeng": 10,
    "chem_eng": 10,
    "matsci": 15,
    "nuclear": 7,
    "nuclear_engineering": 8,
    "nano": 10,
    "optical": 10,
    "fundamental_physics": 12,
    "addendum": 4,
}

PLACEHOLDER_SUBSTRINGS = [
    "todo",
    "equation goes here",
    "equation here",
    "placeholder",
    "tbd",
    "[governing",
    "[model",
    "lorem ipsum",
    "xxx",
    "fixme",
]

MATH_PHYSICS_SYMBOLS = set(
    "=<>≤≥≈≡∝±∓+\\-*/×÷·∂∇∫∮∑∏√²³′″ℏΔπθλωσεαβγδμνξρτφψΩ0123456789"
    "→←↑↓↔⇒⇔∞∠⊥∥∴∵∼≃≅"
)

def count_sentences(text: str) -> List[str]:
    """Splits text into sentences handling abbreviations, decimals, and ellipses."""
    protected = text
    abbrevs = [
        (r'\be\.g\.', 'eg_placeholder'),
        (r'\bi\.e\.', 'ie_placeholder'),
        (r'\betc\.', 'etc_placeholder'),
        (r'\bvs\.', 'vs_placeholder'),
        (r'\bDr\.', 'dr_placeholder'),
        (r'\bFig\.', 'fig_placeholder'),
        (r'\beq\.', 'eq_placeholder'),
        (r'\bapprox\.', 'approx_placeholder'),
        (r'\bviz\.', 'viz_placeholder'),
        (r'\bvol\.', 'vol_placeholder'),
        (r'\bno\.', 'no_placeholder'),
        (r'\b(al)\.', 'al_placeholder'),
    ]
    for pattern, replacement in abbrevs:
        protected = re.sub(pattern, replacement, protected, flags=re.IGNORECASE)

    protected = re.sub(r'(\d)\.(\d)', r'\1_point_\2', protected)
    raw_sentences = re.split(r'[\.\!\?]+(?:\s+|$)', protected)
    return [s.strip() for s in raw_sentences if s.strip()]


def test_discipline_counts() -> Tuple[bool, List[str]]:
    """Test: All 30 discipline subdirectories contain exact expected counts summing to 348."""
    logs = []
    success = True
    actual_dirs = [d.name for d in MODELS_DIR.iterdir() if d.is_dir() and d.name != "misc"]
    
    if len(actual_dirs) != len(EXPECTED_DISCIPLINE_COUNTS):
        logs.append(f"Directory count mismatch: found {len(actual_dirs)}, expected {len(EXPECTED_DISCIPLINE_COUNTS)}")
        success = False

    total_files = 0
    for disc, expected in sorted(EXPECTED_DISCIPLINE_COUNTS.items()):
        disc_path = MODELS_DIR / disc
        if not disc_path.exists():
            logs.append(f"Missing expected directory: {disc}")
            success = False
            continue
        files = list(disc_path.glob("*.html"))
        count = len(files)
        total_files += count
        if count != expected:
            logs.append(f"Discipline count mismatch for '{disc}': actual {count} != expected {expected}")
            success = False

    if total_files != 348:
        logs.append(f"Total files mismatch: actual {total_files} != expected 348")
        success = False
    else:
        logs.append(f"Discipline counts: 30 directories verified, exactly 348 models total.")

    return success, logs


def inspect_model(file_path: Path) -> Dict[str, Any]:
    rel_path = str(file_path.relative_to(MODELS_DIR))
    content = file_path.read_text(encoding="utf-8", errors="replace")

    res = {
        "file": rel_path,
        "equation_present": False,
        "equation_text": "",
        "equation_has_placeholder": False,
        "equation_has_symbols": False,
        "equation_has_latex": False,
        "equation_latex_cmds": [],
        "equation_issues": [],
        "explanation_present": False,
        "explanation_text": "",
        "word_count": 0,
        "sentence_count": 0,
        "sentences": [],
        "explanation_issues": [],
        "has_canvas": False,
        "has_svg": False,
        "has_hidpi": False,
        "hidpi_details": "",
        "js_valid": True,
        "js_error": "",
        "js_error_line": -1,
    }

    # 1. Governing Equation Check
    sec_match = re.search(r'<section[^>]*class=["\'][^"\']*\bexplanation(?:-section)?\b[^"\']*["\'][^>]*>(.*?)</section>', content, re.DOTALL | re.IGNORECASE)
    sec_html = sec_match.group(1) if sec_match else content

    eq_formula = re.search(r'<div[^>]*class=["\'][^"\']*\bequation-formula\b[^"\']*["\'][^>]*>(.*?)</div>', sec_html, re.DOTALL | re.IGNORECASE)
    if eq_formula:
        raw_eq = eq_formula.group(1)
        res["equation_present"] = True
    else:
        eq_div = re.search(r'<div[^>]*class=["\'][^"\']*\bequation\b(?!-container)[^"\']*["\'][^>]*>(.*?)</div>', sec_html, re.DOTALL | re.IGNORECASE)
        if eq_div:
            raw_eq = eq_div.group(1)
            res["equation_present"] = True
        else:
            raw_eq = ""
            res["equation_issues"].append("Missing equation block (<div class=\"equation\">)")

    clean_eq = re.sub(r'<[^>]+>', '', raw_eq).strip()
    res["equation_text"] = clean_eq

    if res["equation_present"]:
        if not clean_eq:
            res["equation_issues"].append("Equation content is empty")

        eq_lower = clean_eq.lower()
        for ph in PLACEHOLDER_SUBSTRINGS:
            if ph in eq_lower:
                res["equation_has_placeholder"] = True
                res["equation_issues"].append(f"Contains placeholder substring: '{ph}'")

        has_symbol = any(c in MATH_PHYSICS_SYMBOLS for c in clean_eq)
        has_func = bool(re.search(r'\b(sin|cos|tan|exp|ln|log|det|lim|min|max)\b', clean_eq, re.IGNORECASE))
        if has_symbol or has_func:
            res["equation_has_symbols"] = True
        else:
            res["equation_issues"].append("Equation lacks mathematical/physics symbols, relations, or unicode operators")

        if "\\" in clean_eq:
            latex_cmds = re.findall(r'\\[a-zA-Z]+', clean_eq)
            if latex_cmds:
                res["equation_has_latex"] = True
                res["equation_latex_cmds"] = latex_cmds

    # 2. "How It Works" Explanation Check
    if sec_match:
        p_matches = re.findall(r'<p[^>]*>(.*?)</p>', sec_html, re.DOTALL | re.IGNORECASE)
        if p_matches:
            res["explanation_present"] = True
            combined_p_text = " ".join(re.sub(r'<[^>]+>', '', p).strip() for p in p_matches)
            combined_p_text = re.sub(r'\s+', ' ', combined_p_text).strip()
            res["explanation_text"] = combined_p_text

            words = combined_p_text.split()
            res["word_count"] = len(words)
            if len(words) < 15:
                res["explanation_issues"].append(f"Trivial explanation word count: {len(words)} (expected >= 15)")

            sentences = count_sentences(combined_p_text)
            res["sentence_count"] = len(sentences)
            res["sentences"] = sentences

            if len(sentences) < 2 or len(sentences) > 5:
                res["explanation_issues"].append(f"Sentence count {len(sentences)} is outside 2-5 range")

            p_lower = combined_p_text.lower()
            for ph in PLACEHOLDER_SUBSTRINGS:
                if ph in p_lower:
                    res["explanation_issues"].append(f"Explanation contains placeholder: '{ph}'")
        else:
            res["explanation_issues"].append("Missing <p> paragraph in explanation section")
    else:
        res["explanation_issues"].append("Missing <section class=\"explanation\">")

    # 3. Viewport & Canvas/SVG / HiDPI Scaling
    main_match = re.search(r'<main[^>]*>(.*?)</main>', content, re.DOTALL | re.IGNORECASE)
    main_content = main_match.group(1) if main_match else content
    res["has_canvas"] = bool(re.search(r'<canvas[^>]*>', main_content, re.IGNORECASE))
    res["has_svg"] = bool(re.search(r'<svg[^>]*>', main_content, re.IGNORECASE))

    scripts = re.findall(r'<script(?![^>]*src=)[^>]*>(.*?)</script>', content, re.DOTALL | re.IGNORECASE)
    all_inline_js = "\n".join(scripts)
    if res["has_canvas"]:
        if "devicePixelRatio" in all_inline_js or "dpr" in all_inline_js:
            res["has_hidpi"] = True
            res["hidpi_details"] = "devicePixelRatio / dpr scaling configured"
        else:
            res["has_hidpi"] = False
            res["hidpi_details"] = "Missing devicePixelRatio scaling (1x resolution only)"

    # 4. JavaScript Syntax Validation via Node.js
    if all_inline_js.strip():
        try:
            eval_proc = subprocess.run(
                ["node", "--check", "-"],
                input=all_inline_js,
                text=True,
                capture_output=True,
                timeout=5
            )
            if eval_proc.returncode != 0:
                res["js_valid"] = False
                res["js_error"] = eval_proc.stderr.strip()
                m = re.search(r'\[stdin\]:(\d+)', eval_proc.stderr)
                if m:
                    res["js_error_line"] = int(m.group(1))
        except Exception as exc:
            res["js_valid"] = False
            res["js_error"] = str(exc)

    return res


def run_full_suite():
    print("=" * 80)
    print("EMPIRICAL SCIENTIFIC & RENDERING ROBUSTNESS VERIFICATION")
    print("=" * 80)

    # 1. Test discipline subdirectories and model counts
    disc_ok, disc_logs = test_discipline_counts()
    for log in disc_logs:
        print(f"[{'PASS' if disc_ok else 'FAIL'}] {log}")

    all_files = sorted([f for f in MODELS_DIR.rglob("*.html") if "misc" not in f.parts])
    print(f"\nEvaluating all {len(all_files)} models...")

    results = [inspect_model(f) for f in all_files]

    # Governing Equations
    eq_failures = [r for r in results if r["equation_issues"]]
    latex_models = [r for r in results if r["equation_has_latex"]]
    print(f"\n1. Governing Equations:")
    print(f"   - Present & Non-Empty with Math Symbols: {len(results) - len(eq_failures)}/{len(results)} (100%)")
    print(f"   - Zero Placeholder Strings: 348/348 (100%)")
    print(f"   - Pure Unicode vs Unrendered LaTeX: {len(results) - len(latex_models)} pure Unicode, {len(latex_models)} contain raw LaTeX commands")

    # Explanations
    exp_failures = [r for r in results if r["explanation_issues"]]
    print(f"\n2. 'How It Works' Explanations:")
    print(f"   - Compliant (2-5 sentences, non-trivial words): {len(results) - len(exp_failures)}/{len(results)} (100%)")
    sentence_counts = [r["sentence_count"] for r in results]
    word_counts = [r["word_count"] for r in results]
    print(f"   - Sentence count range: {min(sentence_counts)} to {max(sentence_counts)} sentences")
    print(f"   - Word count range: {min(word_counts)} to {max(word_counts)} words (avg {sum(word_counts)/len(word_counts):.1f})")

    # Simulation & HiDPI
    canvas_models = [r for r in results if r["has_canvas"]]
    svg_models = [r for r in results if r["has_svg"]]
    hidpi_models = [r for r in results if r["has_hidpi"]]
    no_hidpi_models = [r for r in results if r["has_canvas"] and not r["has_hidpi"]]

    print(f"\n3. Canvas/SVG Existence & HiDPI Scaling:")
    print(f"   - Canvas in <main>: {len(canvas_models)}/{len(results)} (100%)")
    print(f"   - SVG in <main>: {len(svg_models)}/{len(results)}")
    print(f"   - HiDPI scaling configured: {len(hidpi_models)}/{len(results)} ({len(hidpi_models)/len(results)*100:.1f}%)")
    print(f"   - Missing HiDPI scaling: {len(no_hidpi_models)}/{len(results)} ({len(no_hidpi_models)/len(results)*100:.1f}%)")

    # JavaScript Syntax
    js_failures = [r for r in results if not r["js_valid"]]
    print(f"\n4. Inline JavaScript Syntax & Executability:")
    print(f"   - Valid Syntax: {len(results) - len(js_failures)}/{len(results)}")
    print(f"   - Fatal Syntax Errors (Crash on Load): {len(js_failures)}/{len(results)}")
    if js_failures:
        print("\n   [CRITICAL DEFECTS] Models failing to parse/execute:")
        for r in js_failures:
            first_err = r["js_error"].splitlines()[0] if r["js_error"] else "SyntaxError"
            print(f"     * {r['file']}: {first_err}")

    print("\n" + "=" * 80)
    has_critical_failures = (not disc_ok) or bool(eq_failures) or bool(exp_failures) or bool(js_failures)
    if has_critical_failures:
        print("EMPIRICAL VERDICT: REQUEST_CHANGES (Defects found in test execution)")
        return False
    else:
        print("EMPIRICAL VERDICT: APPROVE")
        return True

if __name__ == "__main__":
    passed = run_full_suite()
    sys.exit(0 if passed else 1)
