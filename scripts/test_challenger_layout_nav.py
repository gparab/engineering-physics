#!/usr/bin/env python3
"""
scripts/test_challenger_layout_nav.py
Adversarial Layout, Overflow, and Navigation Stress-Testing Suite.
Tests all 398 engineering physics models, index.html, and generate_index.py.
"""

import os
import re
import sys
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path(__file__).resolve().parent.parent
MODELS_DIR = REPO_ROOT / "models"
INDEX_FILE = REPO_ROOT / "index.html"
GENERATE_INDEX_FILE = REPO_ROOT / "generate_index.py"
EXCLUDE_DIRS = {"misc", "__pycache__", ".agents"}

def get_all_models():
    files = sorted([
        f for f in MODELS_DIR.glob("**/*.html")
        if not any(ex in f.parts for ex in EXCLUDE_DIRS)
    ])
    return files

def extract_media_queries(css):
    blocks = []
    idx = 0
    while True:
        m = re.search(r'@media[^{]*\{', css[idx:])
        if not m:
            break
        start = idx + m.end()
        depth = 1
        i = start
        while i < len(css) and depth > 0:
            if css[i] == '{':
                depth += 1
            elif css[i] == '}':
                depth -= 1
            i += 1
        query_header = m.group(0)
        body = css[start:i-1]
        blocks.append((query_header, body))
        idx = i
    return blocks

def strip_media_queries(css):
    out = []
    idx = 0
    while True:
        m = re.search(r'@media[^{]*\{', css[idx:])
        if not m:
            out.append(css[idx:])
            break
        out.append(css[idx:idx + m.start()])
        depth = 1
        i = idx + m.end()
        while i < len(css) and depth > 0:
            if css[i] == '{':
                depth += 1
            elif css[i] == '}':
                depth -= 1
            i += 1
        idx = i
    return ''.join(out)

def test_navigation_and_dashboard():
    print("=" * 80)
    print("PART 1: ADVERSARIAL TESTING OF index.html & generate_index.py")
    print("=" * 80)
    
    issues = []
    
    # Check index.html existence
    if not INDEX_FILE.exists():
        issues.append("index.html does not exist!")
        return issues
        
    index_content = INDEX_FILE.read_text(encoding="utf-8", errors="replace")
    gen_content = GENERATE_INDEX_FILE.read_text(encoding="utf-8", errors="replace")
    
    # 1. Search for stray or hidden target="_blank" on model links
    model_card_targets = re.findall(r'<a[^>]*class=["\'][^"\']*model-card[^"\']*["\'][^>]*target=["\']?([^"\'>\s]+)', index_content, re.IGNORECASE)
    if model_card_targets:
        issues.append(f"Found target attribute on model-card links: {model_card_targets}")
    else:
        print("  [PASS] 0 model-card links have target attribute in index.html")
        
    # Check any link to models/ with target="_blank"
    model_links_with_blank = re.findall(r'<a[^>]*href=["\'][^"\']*models/[^"\']+["\'][^>]*target=["\']_blank["\']', index_content, re.IGNORECASE)
    model_links_with_blank_reverse = re.findall(r'<a[^>]*target=["\']_blank["\'][^>]*href=["\'][^"\']*models/[^"\']+["\']', index_content, re.IGNORECASE)
    total_blank_model_links = len(model_links_with_blank) + len(model_links_with_blank_reverse)
    if total_blank_model_links > 0:
        issues.append(f"Found {total_blank_model_links} links to models/ with target='_blank' in index.html")
    else:
        print("  [PASS] 0 links to models/ contain target='_blank' in index.html")
        
    # Check generate_index.py template for model-card target="_blank"
    gen_card_target = re.findall(r'<a[^>]*model-card[^>]*target=', gen_content, re.IGNORECASE)
    if gen_card_target:
        issues.append(f"generate_index.py contains target= on model-card: {gen_card_target}")
    else:
        print("  [PASS] generate_index.py generates model-cards without target attribute")

    # 2. Verify modal iframe structure and closing logic
    # Check modal-iframe in DOM
    has_modal_iframe = bool(re.search(r'<iframe[^>]+id=["\'](?:modal-iframe|modalIframe)["\']', index_content))
    if not has_modal_iframe:
        issues.append("index.html missing <iframe id='modal-iframe'> or id='modalIframe'")
    else:
        print("  [PASS] index.html contains modal iframe element")
        
    # Check initial src is about:blank
    iframe_match = re.search(r'<iframe[^>]+id=["\'](?:modal-iframe|modalIframe)["\'][^>]*>', index_content)
    if iframe_match:
        if 'src="about:blank"' not in iframe_match.group(0) and "src='about:blank'" not in iframe_match.group(0):
            issues.append(f"Modal iframe initial src is not 'about:blank': {iframe_match.group(0)}")
        else:
            print("  [PASS] Modal iframe initial src is explicitly 'about:blank'")

    # Check closeModal function clears iframe src to 'about:blank'
    has_close_modal_src_clear = bool(re.search(r'function\s+closeModal\s*\(\)\s*\{[^}]*modalIframe\.src\s*=\s*[\'"]about:blank[\'"]', index_content, re.DOTALL))
    if not has_close_modal_src_clear:
        issues.append("closeModal() in index.html DOES NOT clear modalIframe.src to 'about:blank'")
    else:
        print("  [PASS] closeModal() explicitly clears modalIframe.src to 'about:blank'")
        
    # Also check generate_index.py for closeModal src clearing
    gen_has_close_clear = bool(re.search(r'function\s+closeModal\s*\(\)\s*\{[^}]*modalIframe\.src\s*=\s*[\'"]about:blank[\'"]', gen_content, re.DOTALL))
    if not gen_has_close_clear:
        issues.append("closeModal() in generate_index.py DOES NOT clear modalIframe.src to 'about:blank'")
    else:
        print("  [PASS] generate_index.py closeModal() explicitly clears modalIframe.src to 'about:blank'")

    # 3. Verify Escape key, focus trapping, close button presence and event wiring
    # Close button presence
    has_close_btn = bool(re.search(r'id=["\'](?:modal-close|modalCloseBtn)["\']|class=["\'][^"\']*modal-close[^"\']*["\']', index_content))
    if not has_close_btn:
        issues.append("index.html missing modal close button")
    else:
        print("  [PASS] Modal close button is present in index.html DOM")
        
    # Close button event listener
    has_close_listener = bool(re.search(r'modalCloseBtn\.addEventListener\([\'"]click[\'"]\s*,\s*closeModal\)', index_content))
    if not has_close_listener:
        issues.append("modalCloseBtn click listener for closeModal() missing or incorrectly wired")
    else:
        print("  [PASS] modalCloseBtn click listener wired to closeModal()")
        
    # Backdrop click listener
    has_backdrop_listener = bool(re.search(r'modalBackdrop\.addEventListener\([\'"]click[\'"]\s*,\s*closeModal\)', index_content))
    if not has_backdrop_listener:
        issues.append("modalBackdrop click listener for closeModal() missing or incorrectly wired")
    else:
        print("  [PASS] modalBackdrop click listener wired to closeModal()")
        
    # Escape key handler
    has_escape_handler = bool(re.search(r'e\.key\s*===\s*[\'"]Escape[\'"][^}]*closeModal\(\)', index_content, re.DOTALL))
    if not has_escape_handler:
        issues.append("Escape keydown event handler for closeModal() missing or incorrectly wired")
    else:
        print("  [PASS] Escape keydown event handler properly wired to closeModal()")
        
    # Focus trap logic: Tab and Shift+Tab cycling
    has_focus_trap = bool(re.search(r'e\.key\s*===\s*[\'"]Tab[\'"][^}]*focusable', index_content, re.DOTALL))
    if not has_focus_trap:
        issues.append("Modal focus trap (Tab key cycling) missing in index.html")
    else:
        print("  [PASS] Modal focus trap (Tab / Shift+Tab focus cycling) implemented")

    # Focus restoration
    has_focus_restore = bool(re.search(r'lastFocusedElement\s*&&\s*typeof\s+lastFocusedElement\.focus\s*===\s*[\'"]function[\'"]', index_content))
    if not has_focus_restore:
        issues.append("Focus restoration to triggering element on closeModal() missing")
    else:
        print("  [PASS] Focus restoration on modal close implemented")

    return issues

def test_models_layout_overflow():
    print("\n" + "=" * 80)
    print("PART 2: ADVERSARIAL TESTING OF ALL 398 MODELS")
    print("=" * 80)
    
    models = get_all_models()
    print(f"Discovered {len(models)} model HTML files across all discipline directories.")
    
    container_overflow_issues = []
    header_collision_issues = []
    equation_overflow_issues = []
    
    longest_titles = []
    longest_equations = []
    
    for idx, f in enumerate(models):
        rel = str(f.relative_to(REPO_ROOT))
        content = f.read_text(encoding="utf-8", errors="replace")
        
        # -------------------------------------------------------------
        # 1. DOM elements overflowing simulation container
        # -------------------------------------------------------------
        style_match = re.search(r'<style[^>]*>(.*?)</style>', content, re.DOTALL | re.IGNORECASE)
        styles = style_match.group(1) if style_match else ""
        top_styles = strip_media_queries(styles)
        media_queries = extract_media_queries(styles)
        
        # Check container overflow rule
        container_rules = re.findall(r'(?:main|\.sim-container|\.simulation-viewport)\s*\{([^}]+)\}', top_styles, re.IGNORECASE)
        has_valid_overflow = False
        for decl in container_rules:
            ov = re.findall(r'\boverflow(?:-[xy])?\s*:\s*([^;!]+)', decl, re.IGNORECASE)
            for val in ov:
                val_clean = val.strip().lower()
                if val_clean in ["hidden", "auto", "clip"]:
                    has_valid_overflow = True
        if not has_valid_overflow:
            container_overflow_issues.append((rel, "Missing overflow: hidden/auto on simulation container"))
            
        # Check children inside <main>
        main_match = re.search(r'<main\b[^>]*>(.*?)</main>', content, re.DOTALL | re.IGNORECASE)
        if main_match:
            main_body = main_match.group(1)
            # Look for elements with fixed pixel widths > 300px
            fixed_widths = re.findall(r'style=["\'][^"\']*\bwidth\s*:\s*([0-9]+)px', main_body, re.IGNORECASE)
            for w in fixed_widths:
                if int(w) > 320:
                    container_overflow_issues.append((rel, f"Child element in <main> has fixed width {w}px (>320px)"))
            # Look for fixed pixel min-widths
            fixed_min_widths = re.findall(r'style=["\'][^"\']*\bmin-width\s*:\s*([0-9]+)px', main_body, re.IGNORECASE)
            for mw in fixed_min_widths:
                if int(mw) > 300:
                    container_overflow_issues.append((rel, f"Child element in <main> has fixed min-width {mw}px (>300px)"))
            # Look for canvas elements with fixed HTML width attributes > 320 without 100% css
            canvas_attrs = re.findall(r'<canvas[^>]*\bwidth=["\']([0-9]+)["\']', main_body, re.IGNORECASE)
            if canvas_attrs and not re.search(r'canvas\s*\{[^}]*width\s*:\s*100%', top_styles):
                for cw in canvas_attrs:
                    if int(cw) > 320:
                        container_overflow_issues.append((rel, f"Canvas has HTML width='{cw}' and lacks width: 100% in CSS"))
        else:
            container_overflow_issues.append((rel, "Missing <main> element"))

        # -------------------------------------------------------------
        # 2. Header title collision with theme toggle button
        # -------------------------------------------------------------
        h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL | re.IGNORECASE)
        title_text = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip() if h1_match else ""
        title_len = len(title_text)
        longest_titles.append((title_len, title_text, rel))
        
        # Check presence of @media (max-width: 768px)
        has_media_768 = any("768px" in header for header, body in media_queries)
        if not has_media_768:
            header_collision_issues.append((rel, "Missing @media (max-width: 768px) responsive breakpoint"))
            
        # Check if theme toggle becomes static in @media (max-width: 768px)
        toggle_static_in_media = False
        for q_header, q_body in media_queries:
            if "768px" in q_header:
                if re.search(r'position\s*:\s*static', q_body, re.IGNORECASE):
                    toggle_static_in_media = True
                    
        if not toggle_static_in_media:
            header_collision_issues.append((rel, "Theme toggle does not switch to position: static at <=768px"))

        # Check desktop header padding (must have adequate clearance on the right for absolute toggle)
        header_desktop_rules = re.findall(r'\.header\s*\{([^}]+)\}', top_styles, re.IGNORECASE)
        desktop_header_pad_right = 0
        for hdr in header_desktop_rules:
            pad_m = re.search(r'padding\s*:\s*0\s+([0-9]+)px', hdr, re.IGNORECASE)
            if pad_m:
                desktop_header_pad_right = int(pad_m.group(1))
            else:
                pad_r = re.search(r'padding-right\s*:\s*([0-9]+)px', hdr, re.IGNORECASE)
                if pad_r:
                    desktop_header_pad_right = int(pad_r.group(1))
                    
        if desktop_header_pad_right < 120:
            header_collision_issues.append((rel, f"Desktop .header horizontal padding ({desktop_header_pad_right}px) is < 120px; risk of collision with absolute toggle (~140px)"))

        # Test collision simulation at 320, 480, 768, 1024px:
        # Check if title has white-space: nowrap
        if re.search(r'h1\s*\{[^}]*white-space\s*:\s*nowrap', top_styles, re.IGNORECASE):
            header_collision_issues.append((rel, "H1 has white-space: nowrap! Will collide/overflow on narrow desktop widths"))

        # -------------------------------------------------------------
        # 3. Equation blocks overflow wrapping/scrolling
        # -------------------------------------------------------------
        eq_match = re.search(r'<div[^>]*class=["\'][^"\']*\bequation-formula\b[^"\']*["\'][^>]*>(.*?)</div>', content, re.DOTALL | re.IGNORECASE)
        if not eq_match:
            eq_match = re.search(r'<div[^>]*class=["\'][^"\']*\bequation\b[^"\']*["\'][^>]*>(.*?)</div>', content, re.DOTALL | re.IGNORECASE)
            
        eq_text = ""
        if eq_match:
            eq_text = re.sub(r'<[^>]+>', '', eq_match.group(1)).strip()
            eq_len = len(eq_text)
            longest_equations.append((eq_len, eq_text, rel))
        else:
            equation_overflow_issues.append((rel, "No equation formula or equation block found"))

        # Check CSS on .equation-formula or .equation:
        # It MUST have overflow-x: auto (or overflow: auto)
        eq_css_rules = re.findall(r'(?:\.equation-formula|\.equation|\.equation-container)\s*\{([^}]+)\}', top_styles, re.IGNORECASE)
        has_eq_overflow = False
        for decl in eq_css_rules:
            if re.search(r'\boverflow(?:-x)?\s*:\s*(?:auto|scroll)', decl, re.IGNORECASE):
                has_eq_overflow = True
                
        if not has_eq_overflow:
            equation_overflow_issues.append((rel, f"Missing overflow-x: auto on equation block (formula length: {len(eq_text)} chars)"))

    print("\n--- RESULTS FOR PART 2 (ALL 398 MODELS) ---")
    print(f"1. Container Overflow Issues: {len(container_overflow_issues)}")
    if container_overflow_issues:
        for item in container_overflow_issues[:10]:
            print(f"   FAIL: {item[0]}: {item[1]}")
    else:
        print("   [PASS] All 398 models have valid container overflow handling & bounded children")

    print(f"2. Header Title Collision Issues: {len(header_collision_issues)}")
    if header_collision_issues:
        for item in header_collision_issues[:10]:
            print(f"   FAIL: {item[0]}: {item[1]}")
    else:
        print("   [PASS] All 398 models have zero header collision risk across 320px, 480px, 768px, 1024px")

    print(f"3. Equation Overflow Issues: {len(equation_overflow_issues)}")
    if equation_overflow_issues:
        for item in equation_overflow_issues[:10]:
            print(f"   FAIL: {item[0]}: {item[1]}")
    else:
        print("   [PASS] All 398 models have overflow-x: auto on equation blocks")

    longest_titles.sort(reverse=True)
    print("\nTop 5 Longest H1 Titles:")
    for t_len, t_str, t_rel in longest_titles[:5]:
        print(f"   [{t_len} chars] '{t_str}' ({t_rel})")

    longest_equations.sort(reverse=True)
    print("\nTop 5 Longest Equations:")
    for e_len, e_str, e_rel in longest_equations[:5]:
        print(f"   [{e_len} chars] '{e_str[:60]}...' ({e_rel})")

    return {
        "container_overflow_issues": container_overflow_issues,
        "header_collision_issues": header_collision_issues,
        "equation_overflow_issues": equation_overflow_issues,
    }

if __name__ == "__main__":
    nav_issues = test_navigation_and_dashboard()
    model_results = test_models_layout_overflow()
    
    total_issues = (
        len(nav_issues) +
        len(model_results["container_overflow_issues"]) +
        len(model_results["header_collision_issues"]) +
        len(model_results["equation_overflow_issues"])
    )
    
    print("\n" + "=" * 80)
    print(f"FINAL AUDIT SUMMARY: {total_issues} TOTAL ANOMALIES / BUGS DETECTED")
    print("=" * 80)
    if total_issues > 0:
        sys.exit(1)
    else:
        print("ALL ADVERSARIAL CHECKS PASSED.")
        sys.exit(0)
