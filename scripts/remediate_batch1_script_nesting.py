#!/usr/bin/env python3
"""
scripts/remediate_batch1_script_nesting.py
==============================================================================
Remediation script for Batch 1 (216 models across Disciplines 1-14):
1. Cleans the <head> KaTeX CDN scripts so that <script defer src="..."></script>
   tags contain no inner child text.
2. Relocates renderPhysicsEquations() and its DOMContentLoaded invocation into
   the main executable inline <script> block at the bottom of <body>.
==============================================================================
"""

import os
import re
import sys
from pathlib import Path

BATCH1_DISCIPLINES = [
    "acoustics_engineering",
    "aerospace_engineering",
    "agricultural_engineering",
    "astrodynamics",
    "biomedical_engineering",
    "chemical_engineering",
    "civil_engineering",
    "computer_engineering",
    "computer_science",
    "cryogenic_engineering",
    "electrical_engineering",
    "electronics_engineering",
    "energy_engineering",
    "environmental_engineering",
]

CLEAN_KATEX_HEAD = (
    '  <!-- KaTeX LaTeX Typesetting Engine -->\n'
    '  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">\n'
    '  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>\n'
    '  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>'
)

KATEX_INLINE_BOTTOM = r'''

    // --- KATEX MATHEMATICAL RENDERING INITIALIZATION ---
    function renderPhysicsEquations() {
      if (typeof renderMathInElement === 'function') {
        renderMathInElement(document.body, {
          delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '\\[', right: '\\]', display: true },
            { left: '\\(', right: '\\)', display: false }
          ],
          throwOnError: false
        });
      } else if (typeof katex !== 'undefined') {
        document.querySelectorAll('.equation-formula').forEach(el => {
          const raw = el.textContent.trim().replace(/^\$\$|\$\$$/g, '').trim();
          try {
            katex.render(raw, el, {
              displayMode: true,
              throwOnError: false
            });
          } catch (err) {
            console.warn('KaTeX direct render error:', err);
          }
        });
      }
    }

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', renderPhysicsEquations);
    } else {
      renderPhysicsEquations();
    }
  </script>'''

HEAD_REGEX = re.compile(
    r'[ \t]*<!--\s*KaTeX LaTeX Typesetting Engine\s*-->\s*'
    r'<link\s+rel=[\'"]stylesheet[\'"]\s+href=[\'"]https://cdn\.jsdelivr\.net/npm/katex@0\.16\.9/dist/katex\.min\.css[\'"]>\s*'
    r'<script\s+defer\s+src=[\'"]https://cdn\.jsdelivr\.net/npm/katex@0\.16\.9/dist/katex\.min\.js[\'"]>[\s\S]*?</script>\s*'
    r'<script\s+defer\s+src=[\'"]https://cdn\.jsdelivr\.net/npm/katex@0\.16\.9/dist/contrib/auto-render\.min\.js[\'"]></script>',
    re.IGNORECASE
)


def remediate_file(file_path: Path) -> bool:
    content = file_path.read_text(encoding="utf-8")

    # 1. Clean head KaTeX block
    if not HEAD_REGEX.search(content):
        print(f"WARNING: Head regex did not match in {file_path}", file=sys.stderr)
        return False

    new_content = HEAD_REGEX.sub(CLEAN_KATEX_HEAD, content, count=1)

    # 2. Place renderPhysicsEquations into bottom inline script before </script>
    last_script_close = new_content.rfind("</script>")
    if last_script_close == -1:
        print(f"WARNING: Could not find closing </script> in {file_path}", file=sys.stderr)
        return False

    # Insert before the last </script>
    prefix = new_content[:last_script_close].rstrip()
    suffix = new_content[last_script_close + len("</script>"):]
    final_content = prefix + KATEX_INLINE_BOTTOM + suffix

    # Sanity checks
    # Check no script src tag has child text
    src_tags = re.findall(
        r'<script\b[^>]*\bsrc=[\'"][^\'"]*[\'"][^>]*>([\s\S]*?)</script>',
        final_content,
        re.IGNORECASE
    )
    for s in src_tags:
        if s.strip():
            print(f"ERROR: File still contains script with child text: {file_path}", file=sys.stderr)
            return False

    # Check executable inline script contains renderPhysicsEquations
    executable_inline_scripts = re.findall(
        r'<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)</script>',
        final_content,
        re.IGNORECASE
    )
    if not any("renderPhysicsEquations" in s for s in executable_inline_scripts):
        print(f"ERROR: renderPhysicsEquations missing in executable inline script: {file_path}", file=sys.stderr)
        return False

    file_path.write_text(final_content, encoding="utf-8")
    return True


def main():
    repo_root = Path(__file__).resolve().parent.parent
    models_dir = repo_root / "models"

    total_files = 0
    success_files = 0

    for disc in BATCH1_DISCIPLINES:
        disc_dir = models_dir / disc
        if not disc_dir.exists():
            print(f"Discipline directory not found: {disc_dir}", file=sys.stderr)
            continue

        html_files = sorted(list(disc_dir.glob("*.html")))
        print(f"Processing {disc}: {len(html_files)} models")
        for f in html_files:
            total_files += 1
            if remediate_file(f):
                success_files += 1

    print(f"\nRemediation complete: {success_files}/{total_files} models successfully updated.")
    if success_files == total_files and total_files == 216:
        print("ALL 216 BATCH 1 MODELS REMEDIATED CLEANLY.")
        sys.exit(0)
    else:
        print(f"FAIL: Expected 216 models, updated {success_files}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
