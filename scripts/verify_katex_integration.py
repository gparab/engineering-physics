#!/usr/bin/env python3
"""
scripts/verify_katex_integration.py
==============================================================================
Exhaustive Automated Verification Suite for KaTeX Integration Across Models.

Evaluates all 398 engineering physics models against 5 core KaTeX requirements:
  - CHECK 1: KaTeX CSS and JS CDN links present in <head>
  - CHECK 2: KaTeX math delimiters & syntax inside <div class="equation-formula">
  - CHECK 3: Zero occurrences of Unicode combining character U+20D7
  - CHECK 4: Equation container CSS includes 'overflow-x: auto'
  - CHECK 5: HTML5 script compliance & executable KaTeX initialization in inline script

Usage:
  python3 scripts/verify_katex_integration.py [--all] [--strict] [--verbose]
  python3 scripts/verify_katex_integration.py --file <path-to-model.html>
  python3 scripts/verify_katex_integration.py --json
==============================================================================
"""

import argparse
from dataclasses import dataclass, field
import json
from pathlib import Path
import re
import sys
from typing import Dict, List, Optional, Tuple


@dataclass
class CheckResult:
    check_id: str
    check_name: str
    passed: bool
    message: str
    details: List[str] = field(default_factory=list)


@dataclass
class ModelEvaluation:
    file_path: Path
    rel_path: str
    discipline: str
    checks: Dict[str, CheckResult]
    passed: bool


def check_1_katex_cdn_head(content: str) -> CheckResult:
    """Check 1: Every model's <head> includes KaTeX CSS and JS CDN links."""
    check_id = "CHECK_1"
    name = "KaTeX CDN Resources in <head>"
    violations = []

    m_head = re.search(r'<head\b[^>]*>(.*?)</head>', content, re.DOTALL | re.IGNORECASE)
    head_content = m_head.group(1) if m_head else content

    # KaTeX CSS stylesheet
    has_css = bool(
        re.search(r'<link\b[^>]*\brel=["\']?stylesheet["\']?[^>]*\bhref=["\'][^"\']*katex(\.min)?\.css', head_content, re.IGNORECASE) or
        re.search(r'<link\b[^>]*\bhref=["\'][^"\']*katex(\.min)?\.css[^"\']*\brel=["\']?stylesheet["\']?', head_content, re.IGNORECASE)
    )
    if not has_css:
        violations.append("Missing KaTeX stylesheet link (katex.min.css)")

    # KaTeX Core JS
    has_core_js = bool(
        re.search(r'<script\b[^>]*\bsrc=["\'][^"\']*katex(\.min)?\.js', head_content, re.IGNORECASE)
    )
    if not has_core_js:
        violations.append("Missing KaTeX core script link (katex.min.js)")

    # KaTeX Auto-render JS
    has_autorender_js = bool(
        re.search(r'<script\b[^>]*\bsrc=["\'][^"\']*auto-render(\.min)?\.js', head_content, re.IGNORECASE) or
        re.search(r'<script\b[^>]*\bsrc=["\'][^"\']*contrib/auto-render', head_content, re.IGNORECASE)
    )
    if not has_autorender_js:
        violations.append("Missing KaTeX auto-render script link (auto-render.min.js)")

    if violations:
        return CheckResult(check_id, name, False, "; ".join(violations), violations)

    return CheckResult(check_id, name, True, "All KaTeX CDN resources verified in <head>", [])


def check_2_equation_katex_math(content: str) -> CheckResult:
    """Check 2: Every model's <div class="equation-formula"> contains KaTeX math."""
    check_id = "CHECK_2"
    name = "KaTeX Math Delimiters & Syntax in Equation Formula"

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
        return CheckResult(check_id, name, False, "Missing <div class=\"equation-formula\"> container", ["Missing equation container"])

    raw_eq = eq_match.group(1).strip()
    if not raw_eq or len(raw_eq) < 3 or raw_eq.startswith("<!--"):
        return CheckResult(check_id, name, False, "Equation formula is empty or placeholder", ["Empty or placeholder equation"])

    # Verify KaTeX math delimiters or pre-rendered elements
    has_katex_syntax = bool(
        ('$$' in raw_eq) or
        re.search(r'\\\[[\s\S]*?\\\]', raw_eq) or
        re.search(r'\\\([\s\S]*?\\\)', raw_eq) or
        re.search(r'\\begin\{[a-zA-Z*]+\}', raw_eq) or
        ('<span class="katex"' in raw_eq) or
        ("<span class='katex'" in raw_eq)
    )

    if not has_katex_syntax:
        return CheckResult(
            check_id,
            name,
            False,
            "Equation formula does not contain KaTeX math delimiters ($$, \\[, \\(, \\begin)",
            ["Missing KaTeX math delimiters"]
        )

    # Check for raw math symbols outside of KaTeX delimiters
    outside_delims = re.sub(r'\$\$[\s\S]*?\$\$', '', raw_eq)
    outside_delims = re.sub(r'\\\[[\s\S]*?\\\]', '', outside_delims)
    outside_delims = re.sub(r'\\begin\{[a-zA-Z*]+\}[\s\S]*?\\end\{[a-zA-Z*]+\}', '', outside_delims)
    outside_delims = re.sub(r'\\\([\s\S]*?\\\)', '', outside_delims)
    outside_delims = re.sub(r'<span[^>]*class=["\'][^"\']*\bkatex\b[^"\']*["\'][^>]*>[\s\S]*?</span>', '', outside_delims)
    outside_delims = re.sub(r'<[^>]+>', '', outside_delims)

    raw_symbols = ['∑', '√', '∫', '≤']
    flagged = [s for s in raw_symbols if s in outside_delims]
    if flagged:
        return CheckResult(
            check_id,
            name,
            False,
            f"Equation formula contains raw math symbol(s) outside KaTeX delimiters: {', '.join(flagged)}",
            [f"Raw math symbol '{s}' outside KaTeX delimiters" for s in flagged]
        )

    return CheckResult(check_id, name, True, "Equation formula contains properly delimited KaTeX LaTeX math", [])


def check_3_zero_u20d7(content: str) -> CheckResult:
    """Check 3: Zero occurrences of Unicode combining character U+20D7 in model file."""
    check_id = "CHECK_3"
    name = "Zero U+20D7 Combining Characters"

    count = content.count('\u20d7')
    if count > 0:
        lines = content.splitlines()
        details = []
        for line_idx, line in enumerate(lines, 1):
            if '\u20d7' in line:
                details.append(f"Line {line_idx}: {line.strip()[:80]}")
        return CheckResult(
            check_id,
            name,
            False,
            f"Found {count} forbidden U+20D7 combining right arrow character(s)",
            details
        )

    return CheckResult(check_id, name, True, "Zero U+20D7 occurrences found", [])


def check_4_equation_overflow_auto(content: str) -> CheckResult:
    """Check 4: Equation container CSS includes 'overflow-x: auto'."""
    check_id = "CHECK_4"
    name = "Equation Container Overflow Handling (overflow-x: auto)"

    styles = re.findall(r'<style[^>]*>([\s\S]*?)</style>', content, re.IGNORECASE)
    all_styles = "\n".join(styles)

    # Search for rules addressing equation-formula, equation, equation-container, or katex-display
    eq_css_rules = re.findall(
        r'(?:[^{}]*?(?:\.equation-formula|\.equation|\.equation-container|\.katex-display)[^{}]*?)\{([^}]+)\}',
        all_styles,
        re.IGNORECASE
    )

    has_overflow = False
    for block in eq_css_rules:
        if re.search(r'\boverflow(?:-x)?\s*:\s*(?:auto|scroll)\b', block, re.IGNORECASE):
            has_overflow = True
            break

    if not has_overflow:
        return CheckResult(
            check_id,
            name,
            False,
            "Equation container CSS is missing 'overflow-x: auto' property",
            ["Missing overflow-x: auto on equation block"]
        )

    return CheckResult(check_id, name, True, "Equation container specifies overflow-x: auto", [])


def check_5_html5_script_spec_and_inline_init(content: str) -> CheckResult:
    """Check 5: No <script src="..."> contains inner text, and renderPhysicsEquations exists in executable inline script."""
    check_id = "CHECK_5"
    name = "HTML5 Script Spec & Executable Inline KaTeX Init"
    violations = []

    # 1. W3C/WHATWG HTML spec: <script src="..."> must not have child text content
    src_with_child_text = re.findall(
        r'<script\b[^>]*\bsrc=[\'"][^\'"]*[\'"][^>]*>([\s\S]*?)</script>',
        content,
        re.IGNORECASE
    )
    for child in src_with_child_text:
        if child.strip():
            snippet = child.strip()[:40].replace('\n', ' ')
            violations.append(f"Forbidden inline child text inside <script src=...>: '{snippet}...'")
            break

    # 2. renderPhysicsEquations must exist in executable inline script (without src)
    executable_inline_scripts = re.findall(
        r'<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)</script>',
        content,
        re.IGNORECASE
    )
    has_executable_katex_init = any('renderPhysicsEquations' in s for s in executable_inline_scripts)
    if not has_executable_katex_init:
        violations.append("Missing executable 'renderPhysicsEquations' initialization in inline <script>")

    if violations:
        return CheckResult(check_id, name, False, "; ".join(violations), violations)

    return CheckResult(check_id, name, True, "Valid HTML5 script tags and executable KaTeX initialization verified", [])


def evaluate_model(file_path: Path) -> ModelEvaluation:
    """Evaluate a single HTML model against all 5 KaTeX checks."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        content = ""

    rel_path = str(file_path)
    if "models/" in rel_path:
        rel_path = rel_path.split("models/", 1)[1]
        rel_path = f"models/{rel_path}"

    discipline = file_path.parent.name

    c1 = check_1_katex_cdn_head(content)
    c2 = check_2_equation_katex_math(content)
    c3 = check_3_zero_u20d7(content)
    c4 = check_4_equation_overflow_auto(content)
    c5 = check_5_html5_script_spec_and_inline_init(content)

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
        passed=all_passed
    )


def discover_models(repo_root: Path) -> List[Path]:
    """Discover all 398 HTML models across engineering discipline directories."""
    models_dir = repo_root / "models"
    if not models_dir.exists():
        return []
    models = sorted(
        [p for p in models_dir.glob("*/*.html") if p.parent.name != "misc"],
        key=lambda p: str(p)
    )
    return models


def main():
    parser = argparse.ArgumentParser(
        description="Verify KaTeX integration across Engineering Physics HTML simulation models."
    )
    parser.add_argument(
        "--all",
        action="store_true",
        default=True,
        help="Evaluate all models across all disciplines (default)."
    )
    parser.add_argument(
        "--file",
        type=str,
        help="Evaluate a single specific HTML model file."
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output structured JSON results."
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Enforce 100%% passing quality gate (exit code 1 if any model fails)."
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Display verbose violation details."
    )

    args = parser.parse_args()

    # Determine repo root
    current = Path.cwd()
    if (current / "models").is_dir():
        repo_root = current
    elif (current.parent / "models").is_dir():
        repo_root = current.parent
    else:
        repo_root = current

    # Handle single file evaluation
    if args.file:
        target_path = Path(args.file)
        if not target_path.is_absolute():
            target_path = repo_root / target_path

        if not target_path.exists():
            print(f"Error: File not found: {target_path}", file=sys.stderr)
            sys.exit(1)

        evaluation = evaluate_model(target_path)

        if args.json:
            out = {
                "file": evaluation.rel_path,
                "discipline": evaluation.discipline,
                "passed": evaluation.passed,
                "checks": {
                    cid: {
                        "name": c.check_name,
                        "passed": c.passed,
                        "message": c.message,
                        "details": c.details
                    }
                    for cid, c in evaluation.checks.items()
                }
            }
            print(json.dumps(out, indent=2))
        else:
            status_tag = "[PASS]" if evaluation.passed else "[FAIL]"
            print(f"\n{status_tag} KaTeX Evaluation: {evaluation.rel_path}")
            print("=" * 80)
            for cid in ["CHECK_1", "CHECK_2", "CHECK_3", "CHECK_4", "CHECK_5"]:
                c = evaluation.checks[cid]
                tag = "[PASS]" if c.passed else "[FAIL]"
                print(f"  {tag} {c.check_id}: {c.check_name}")
                print(f"         {c.message}")
                if not c.passed and args.verbose and c.details:
                    for d in c.details:
                        print(f"           - {d}")
            print("=" * 80)

        sys.exit(0 if evaluation.passed else 1)

    # Full catalog evaluation
    model_paths = discover_models(repo_root)
    total_models = len(model_paths)
    if total_models == 0:
        print(f"Error: No models discovered under {repo_root / 'models'}", file=sys.stderr)
        sys.exit(1)

    evaluations: List[ModelEvaluation] = [evaluate_model(p) for p in model_paths]

    check_ids = ["CHECK_1", "CHECK_2", "CHECK_3", "CHECK_4", "CHECK_5"]
    check_names = {
        "CHECK_1": "KaTeX CDN Resources in <head>",
        "CHECK_2": "KaTeX Math in Equation Formula",
        "CHECK_3": "Zero U+20D7 Combining Characters",
        "CHECK_4": "Equation Container Overflow (overflow-x: auto)",
        "CHECK_5": "HTML5 Script Spec & Executable Inline KaTeX Init",
    }

    check_pass_counts = {cid: sum(1 for e in evaluations if e.checks[cid].passed) for cid in check_ids}
    fully_integrated_count = sum(1 for e in evaluations if e.passed)

    all_passed = (fully_integrated_count == total_models)

    # Group by discipline
    disciplines = sorted(list(set(e.discipline for e in evaluations)))
    disc_summary = {}
    for d in disciplines:
        d_evals = [e for e in evaluations if e.discipline == d]
        disc_summary[d] = {
            "total": len(d_evals),
            "fully_integrated": sum(1 for e in d_evals if e.passed),
            "checks": {cid: sum(1 for e in d_evals if e.checks[cid].passed) for cid in check_ids}
        }

    if args.json:
        out = {
            "total_models": total_models,
            "fully_integrated_models": fully_integrated_count,
            "pass_percentage": round(fully_integrated_count / total_models * 100, 1),
            "all_passed": all_passed,
            "checks": {
                cid: {
                    "name": check_names[cid],
                    "passed_count": check_pass_counts[cid],
                    "total_count": total_models,
                    "pass_percentage": round(check_pass_counts[cid] / total_models * 100, 1)
                }
                for cid in check_ids
            },
            "disciplines": disc_summary,
            "failures": [
                {
                    "file": e.rel_path,
                    "discipline": e.discipline,
                    "failed_checks": [
                        {"check_id": cid, "name": c.check_name, "message": c.message}
                        for cid, c in e.checks.items() if not c.passed
                    ]
                }
                for e in evaluations if not e.passed
            ]
        }
        print(json.dumps(out, indent=2))
    else:
        print("\n" + "=" * 80)
        print("ENGINEERING PHYSICS KATEX INTEGRATION & SCIENTIFIC TYPESETTING SUITE")
        print("=" * 80)
        print(f"Models Evaluated:        {total_models}")
        print(f"Fully Integrated Models: {fully_integrated_count}/{total_models} ({fully_integrated_count/total_models*100:.1f}%)")
        print("-" * 80)
        print("CORE KATEX CHECKS BREAKDOWN:")
        for cid in check_ids:
            cnt = check_pass_counts[cid]
            pct = (cnt / total_models) * 100
            status = "[PASS]" if cnt == total_models else "[PENDING]"
            print(f"  {status} {cid}: {check_names[cid]:<52} {cnt:>3}/{total_models} ({pct:5.1f}%)")
        print("-" * 80)

        # Print failure summary if any
        failed_evals = [e for e in evaluations if not e.passed]
        if failed_evals and (args.verbose or fully_integrated_count > 0):
            sample_size = len(failed_evals) if args.verbose else min(5, len(failed_evals))
            print(f"\nMigration Progress / Pending Models (showing {sample_size} of {len(failed_evals)}):")
            for e in failed_evals[:sample_size]:
                failed_cids = [cid for cid, c in e.checks.items() if not c.passed]
                reasons = [f"{cid} ({e.checks[cid].message})" for cid in failed_cids]
                print(f"  - {e.rel_path}: {'; '.join(reasons)}")
            if not args.verbose and len(failed_evals) > 5:
                print(f"  ... and {len(failed_evals) - 5} more (use --verbose to view all)")

        print("=" * 80)
        if all_passed:
            print("OVERALL STATUS: 100% PASSED (All 398 Models Fully KaTeX Integrated)")
        else:
            print(f"KATEX MIGRATION STATUS: {fully_integrated_count}/{total_models} models fully integrated.")
            print("Test suite is operational and ready for M2 & M3 batch implementations.")
            if args.strict:
                print("Quality gate failed: --strict flag was specified.")
        print("=" * 80 + "\n")

    if args.strict:
        sys.exit(0 if all_passed else 1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        try:
            sys.stdout.close()
        except Exception:
            pass
        sys.exit(0)
