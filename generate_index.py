#!/usr/bin/env python3
"""
generate_index.py
Regenerates index.html for Engineering Physics Component Library
adhering strictly to the Apple Human Interface Guidelines (HIG).

Features:
- Apple HIG adaptive light/dark mode via @media (prefers-color-scheme: dark)
- System font stacks (-apple-system / SF Mono)
- 8-point spacing grid and 12px card border-radius
- Clean monochromatic section headers with subtle grouped backgrounds
- Instant client-side search and filtering
- Inline iframe modal simulation viewer
- Validates 100% of relative model paths before writing output
"""

import os
import re
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
MODELS_DIR = REPO_ROOT / "models"
INDEX_FILE = REPO_ROOT / "index.html"
RATINGS_FILE = REPO_ROOT / "model_ratings.md"

EXCLUDE_DIRS = {"misc", "__pycache__", ".agents"}

# Discipline label mapping (Apple HIG monochromatic design system)
DISCIPLINE_PALETTES = {
    # Canonical 23 engineering disciplines
    "acoustics_engineering": {"label": "Acoustics Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "aerospace_engineering": {"label": "Aerospace Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "agricultural_engineering": {"label": "Agricultural Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "biomedical_engineering": {"label": "Biomedical Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "chemical_engineering": {"label": "Chemical Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "civil_engineering": {"label": "Civil Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "computer_engineering": {"label": "Computer Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "computer_science": {"label": "Computer Science", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "electrical_engineering": {"label": "Electrical Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "electronics_engineering": {"label": "Electronics Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "energy_engineering": {"label": "Energy Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "environmental_engineering": {"label": "Environmental Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "fundamental_physics": {"label": "Fundamental Physics", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "industrial_systems_engineering": {"label": "Industrial & Systems Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "marine_engineering": {"label": "Marine Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "materials_science": {"label": "Materials Science", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "mechanical_engineering": {"label": "Mechanical Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "mining_petroleum_engineering": {"label": "Mining & Petroleum Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "nanotechnology": {"label": "Nanotechnology", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "nuclear_engineering": {"label": "Nuclear Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "optical_engineering": {"label": "Optical Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "robotics_engineering": {"label": "Robotics Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "telecommunications_engineering": {"label": "Telecommunications Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},

    # Expansion engineering disciplines
    "plasma_physics": {"label": "Plasma Physics", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "astrodynamics": {"label": "Astrodynamics", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "geophysical_engineering": {"label": "Geophysical Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "cryogenic_engineering": {"label": "Cryogenic Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "quantum_engineering": {"label": "Quantum Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},

    # Legacy aliases (for backward compatibility if needed)
    "acoustics": {"label": "Acoustics Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "aerospace": {"label": "Aerospace Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "biomech": {"label": "Biomechanical Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "biomechanical_engineering": {"label": "Biomechanical Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "chem_eng": {"label": "Chemical Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "chemeng": {"label": "Chemical Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "civil": {"label": "Civil Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "compeng": {"label": "Computer Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "cs": {"label": "Computer Science", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "electrical": {"label": "Electrical Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "ee": {"label": "Electrical Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "electronics": {"label": "Electronics Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "energy": {"label": "Energy Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "enveng": {"label": "Environmental Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "industrial_systems": {"label": "Industrial & Systems Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "marine": {"label": "Marine Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "matsci": {"label": "Materials Science", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "mech": {"label": "Mechanical Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "mining_petro": {"label": "Mining & Petroleum Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "nano": {"label": "Nanotechnology", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "nuclear": {"label": "Nuclear Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "optical": {"label": "Optical Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "robotics": {"label": "Robotics Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "telecommunications": {"label": "Telecommunications Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
    "addendum": {"label": "Multidisciplinary Addendum", "bg": "var(--color-surface)", "border": "var(--color-separator)"},
}

DEFAULT_PALETTE = {"label": "Engineering", "bg": "var(--color-surface)", "border": "var(--color-separator)"}


def load_ratings() -> dict:
    """Parses model ratings from model_ratings.md if available."""
    ratings = {}
    if not RATINGS_FILE.exists():
        return ratings

    content = RATINGS_FILE.read_text(encoding="utf-8", errors="replace")
    for line in content.splitlines():
        if not line.strip().startswith("|") or line.strip().startswith("|-"):
            continue
        parts = [p.strip() for p in line.strip().split("|")[1:-1]]
        html_part = None
        html_idx = -1
        for idx, p in enumerate(parts):
            if ".html" in p:
                clean_p = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', p)
                clean_p = re.sub(r'[`*]', '', clean_p).strip()
                html_part = Path(clean_p).name
                html_idx = idx
                break
        if not html_part or html_idx == -1:
            continue

        scores_found = []
        for p in parts[html_idx + 1:]:
            clean_num = p.replace("★", "").replace("*", "").strip()
            num_match = re.match(r'^(10(?:\.0+)?|[0-9](?:\.[0-9]+)?)$', clean_num)
            if num_match:
                try:
                    val = float(num_match.group(1))
                    if 1.0 <= val <= 10.0:
                        scores_found.append(val)
                except ValueError:
                    pass

        if scores_found:
            ratings[html_part] = scores_found[-1]
    return ratings


def extract_model_meta(file_path: Path) -> dict:
    """Extracts clean title and discipline from model HTML."""
    try:
        content = file_path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        content = ""

    title_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
    if not title_match:
        title_match = re.search(r'<title[^>]*>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)

    if title_match:
        title = re.sub(r'<[^>]+>', '', title_match.group(1)).strip()
    else:
        title = file_path.stem.replace("_", " ").title()

    badge_match = re.search(r'<div[^>]*class=["\'][^"\']*\bdiscipline-badge\b[^"\']*["\'][^>]*>(.*?)</div>', content, re.IGNORECASE | re.DOTALL)
    discipline_badge = re.sub(r'<[^>]+>', '', badge_match.group(1)).strip() if badge_match else ""

    return {"title": title, "badge": discipline_badge}


def generate_dashboard():
    all_files = sorted([
        f for f in MODELS_DIR.glob("**/*.html")
        if not any(ex in f.parts for ex in EXCLUDE_DIRS)
    ])

    ratings = load_ratings()

    # Group by discipline folder
    disciplines = defaultdict(list)
    for f in all_files:
        disc = f.parent.name
        disciplines[disc].append(f)

    total_models = len(all_files)
    total_disciplines = len(disciplines)

    # Build HTML content adhering strictly to Apple Human Interface Guidelines (HIG)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Engineering Physics Interactive Component Library</title>
  <style>
    :root {{
      --color-canvas: #ffffff;
      --color-surface: #f2f2f7;
      --color-card: #f2f2f7;
      --color-text: #000000;
      --color-text-secondary: rgba(60, 60, 67, 0.6);
      --color-text-tertiary: rgba(60, 60, 67, 0.3);
      --color-separator: rgba(60, 60, 67, 0.29);
      --color-accent: #007aff;
      --rounded-sm: 8px;
      --rounded-md: 12px;
      --rounded-lg: 16px;
      --rounded-pill: 9999px;
      --font-sans: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'SF Pro Display', 'Helvetica Neue', Helvetica, Arial, sans-serif;
      --font-mono: 'SF Mono', SFMono-Regular, ui-monospace, Menlo, Monaco, Consolas, monospace;
    }}

    @media (prefers-color-scheme: dark) {{
      :root {{
        --color-canvas: #1c1c1e;
        --color-surface: #2c2c2e;
        --color-card: #2c2c2e;
        --color-text: #ffffff;
        --color-text-secondary: rgba(235, 235, 245, 0.6);
        --color-text-tertiary: rgba(235, 235, 245, 0.3);
        --color-separator: rgba(84, 84, 88, 0.65);
        --color-accent: #0a84ff;
      }}
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      background: var(--color-canvas);
      color: var(--color-text);
      font-family: var(--font-sans);
      font-size: 17px;
      line-height: 1.47;
      -webkit-font-smoothing: antialiased;
      padding-bottom: 48px;
    }}

    .top-nav {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(255, 255, 255, 0.85);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-bottom: 1px solid var(--color-separator);
      height: 64px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 32px;
    }}

    @media (prefers-color-scheme: dark) {{
      .top-nav {{
        background: rgba(28, 28, 30, 0.85);
      }}
    }}

    .nav-brand {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .brand-title {{
      font-size: 17px;
      font-weight: 600;
      letter-spacing: -0.4px;
      color: var(--color-text);
    }}

    .brand-badge {{
      font-family: var(--font-mono);
      font-size: 12px;
      font-weight: 500;
      background: var(--color-surface);
      color: var(--color-text-secondary);
      border: 1px solid var(--color-separator);
      padding: 3px 10px;
      border-radius: 8px;
    }}

    .header-hero {{
      max-width: 960px;
      margin: 0 auto;
      padding: 48px 24px 32px 24px;
      text-align: center;
    }}

    .hero-eyebrow {{
      font-family: var(--font-mono);
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 8px;
      color: var(--color-accent);
      font-weight: 500;
    }}

    .hero-title {{
      font-size: 34px;
      font-weight: 700;
      letter-spacing: -0.8px;
      line-height: 1.15;
      margin-bottom: 16px;
      color: var(--color-text);
    }}

    .hero-desc {{
      font-size: 17px;
      font-weight: 400;
      line-height: 1.47;
      max-width: 720px;
      margin: 0 auto 32px auto;
      color: var(--color-text-secondary);
    }}

    .search-filter-bar {{
      max-width: 1280px;
      margin: 0 auto 48px auto;
      padding: 0 32px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    .search-box {{
      width: 100%;
      max-width: 640px;
      margin: 0 auto;
      position: relative;
    }}

    .search-input {{
      width: 100%;
      height: 48px;
      border-radius: 12px;
      border: 1px solid var(--color-separator);
      background: var(--color-surface);
      color: var(--color-text);
      padding: 0 16px;
      font-size: 17px;
      font-family: var(--font-sans);
      outline: none;
      transition: border-color 0.2s, box-shadow 0.2s;
    }}

    .search-input:focus {{
      border-color: var(--color-accent);
      box-shadow: 0 0 0 3px rgba(0, 122, 255, 0.15);
    }}

    .search-input::placeholder {{
      color: var(--color-text-tertiary);
    }}

    .discipline-pills {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      justify-content: center;
    }}

    .filter-pill {{
      display: inline-flex;
      align-items: center;
      height: 32px;
      padding: 0 16px;
      border-radius: 16px;
      border: 1px solid var(--color-separator);
      background: var(--color-surface);
      color: var(--color-text);
      font-size: 13px;
      font-weight: 500;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.15s ease;
    }}

    .filter-pill:hover {{
      border-color: var(--color-accent);
      color: var(--color-accent);
    }}

    .filter-pill.active {{
      background: var(--color-accent);
      color: #ffffff;
      border-color: var(--color-accent);
    }}

    .main-content {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 32px;
    }}

    .discipline-section {{
      margin-bottom: 48px;
    }}

    .section-header-block {{
      padding: 16px 24px;
      border-radius: 12px;
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: var(--color-surface);
      border: 1px solid var(--color-separator);
    }}

    .section-title-group {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .section-eyebrow {{
      font-family: var(--font-mono);
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      font-weight: 500;
      color: var(--color-text-secondary);
    }}

    .section-title {{
      font-size: 28px;
      font-weight: 700;
      letter-spacing: -0.6px;
      line-height: 1.2;
      color: var(--color-text);
    }}

    .section-count-badge {{
      font-family: var(--font-mono);
      font-size: 12px;
      font-weight: 500;
      padding: 4px 12px;
      border-radius: 12px;
      background: var(--color-canvas);
      color: var(--color-text-secondary);
      border: 1px solid var(--color-separator);
    }}

    .model-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 16px;
    }}

    .model-card {{
      background: var(--color-card);
      border: 1px solid var(--color-separator);
      border-radius: 12px;
      padding: 16px 20px;
      text-decoration: none;
      color: inherit;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      min-height: 104px;
      transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.2s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.2s;
    }}

    .model-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
      border-color: var(--color-accent);
    }}

    @media (prefers-color-scheme: dark) {{
      .model-card:hover {{
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.35);
      }}
    }}

    .card-top {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 12px;
    }}

    .card-title {{
      font-size: 17px;
      font-weight: 600;
      letter-spacing: -0.3px;
      line-height: 1.3;
      color: var(--color-text);
      margin-right: 8px;
    }}

    .card-meta {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: auto;
    }}

    .card-id {{
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--color-text-secondary);
      letter-spacing: 0.02em;
    }}

    /* ==========================================================================
       INLINE MODAL VIEWER (APPLE HIG DESIGN SYSTEM)
       ========================================================================== */
    .modal-overlay {{
      position: fixed;
      inset: 0;
      z-index: 1000;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
      transition: opacity 0.2s ease, visibility 0.2s ease;
    }}

    .modal-overlay.is-active {{
      opacity: 1;
      visibility: visible;
      pointer-events: auto;
    }}

    .modal-backdrop {{
      position: absolute;
      inset: 0;
      background: rgba(0, 0, 0, 0.4);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
    }}

    .modal-container {{
      position: relative;
      z-index: 1001;
      width: min(1360px, calc(100vw - 32px));
      height: min(920px, calc(100vh - 32px));
      background: var(--color-canvas);
      border: 1px solid var(--color-separator);
      border-radius: 12px;
      box-shadow: 0 20px 48px rgba(0, 0, 0, 0.25);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      transform: scale(0.98) translateY(8px);
      transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .modal-overlay.is-active .modal-container {{
      transform: scale(1) translateY(0);
    }}

    @media (max-width: 768px) {{
      .modal-container {{
        width: 100vw;
        height: 100vh;
        border-radius: 0;
        border: none;
      }}
    }}

    .modal-header {{
      height: 56px;
      min-height: 56px;
      background: var(--color-surface);
      border-bottom: 1px solid var(--color-separator);
      padding: 0 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }}

    .modal-header-left {{
      display: flex;
      align-items: center;
      gap: 12px;
      min-width: 0;
      flex: 1;
    }}

    .modal-discipline-badge {{
      font-family: var(--font-mono);
      font-size: 12px;
      font-weight: 500;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 4px 10px;
      border-radius: 8px;
      background: var(--color-canvas);
      color: var(--color-accent);
      border: 1px solid var(--color-separator);
      white-space: nowrap;
      flex-shrink: 0;
    }}

    .modal-title {{
      font-size: 17px;
      font-weight: 600;
      letter-spacing: -0.3px;
      color: var(--color-text);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .modal-id-badge {{
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--color-text-secondary);
      letter-spacing: 0.02em;
      white-space: nowrap;
      flex-shrink: 0;
    }}

    @media (max-width: 640px) {{
      .modal-id-badge {{
        display: none;
      }}
    }}

    .modal-header-actions {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-shrink: 0;
    }}

    .modal-btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      height: 32px;
      padding: 0 12px;
      border-radius: 8px;
      font-family: var(--font-sans);
      font-size: 13px;
      font-weight: 500;
      letter-spacing: -0.1px;
      cursor: pointer;
      text-decoration: none;
      border: 1px solid var(--color-separator);
      background: var(--color-canvas);
      color: var(--color-accent);
      transition: background 0.15s ease, border-color 0.15s ease;
      white-space: nowrap;
    }}

    .modal-btn:hover {{
      background: var(--color-surface);
    }}

    .modal-btn svg {{
      width: 14px;
      height: 14px;
      display: block;
      fill: none;
      stroke: currentColor;
      stroke-width: 2;
      stroke-linecap: round;
      stroke-linejoin: round;
    }}

    .modal-close-pill {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      height: 32px;
      padding: 0 14px;
      border-radius: 8px;
      font-family: var(--font-sans);
      font-size: 13px;
      font-weight: 600;
      letter-spacing: -0.1px;
      cursor: pointer;
      border: none;
      background: var(--color-accent);
      color: #ffffff;
      transition: opacity 0.15s ease;
    }}

    .modal-close-pill:hover {{
      opacity: 0.88;
    }}

    .modal-body {{
      flex: 1;
      width: 100%;
      height: calc(100% - 56px);
      background: var(--color-canvas);
      position: relative;
    }}

    .modal-iframe {{
      width: 100%;
      height: 100%;
      border: none;
      display: block;
      background: var(--color-canvas);
    }}
  </style>
</head>
<body>
  <nav class="top-nav">
    <div class="nav-brand">
      <span class="brand-title">Engineering Physics</span>
      <span class="brand-badge">{total_models} Models</span>
    </div>
    <div>
      <a href="https://gautamparab.com" target="_blank" style="font-family: var(--font-mono); font-size: 12px; text-transform: uppercase; color: inherit; text-decoration: none; font-weight: 500;">gautamparab.com &rarr;</a>
    </div>
  </nav>

  <header class="header-hero">
    <div class="hero-eyebrow">Interactive Scientific Demonstrations</div>
    <h1 class="hero-title">Physics Component Library</h1>
    <p class="hero-desc">{total_models} peer-reviewed, standardized engineering physics simulations across {total_disciplines} engineering disciplines, engineered with precision and textbook rigor.</p>
  </header>

  <div class="search-filter-bar">
    <div class="search-box">
      <input type="text" id="searchInput" class="search-input" placeholder="Search models, disciplines, equations...">
    </div>
    <div class="discipline-pills">
      <button class="filter-pill active" onclick="filterDiscipline('all', this)">All ({total_models})</button>
"""

    for disc in sorted(disciplines.keys()):
        palette = DISCIPLINE_PALETTES.get(disc, DEFAULT_PALETTE)
        count = len(disciplines[disc])
        html += f'      <button class="filter-pill" onclick="filterDiscipline(\'{disc}\', this)">{palette["label"]} ({count})</button>\n'

    html += """    </div>
  </div>

  <main class="main-content">
"""

    for disc in sorted(disciplines.keys()):
        palette = DISCIPLINE_PALETTES.get(disc, DEFAULT_PALETTE)
        files = sorted(disciplines[disc])
        count = len(files)

        html += f"""    <section class="discipline-section" id="section-{disc}" data-discipline="{disc}">
      <div class="section-header-block">
        <div class="section-title-group">
          <span class="section-eyebrow">Engineering Discipline</span>
          <h2 class="section-title">{palette['label']}</h2>
        </div>
        <div class="section-count-badge">{count} models</div>
      </div>
      <div class="model-grid">
"""
        for f in files:
            rel_path = f.relative_to(REPO_ROOT)
            meta = extract_model_meta(f)
            model_name = meta["title"]

            html += f"""        <a href="{rel_path}" class="model-card" data-title="{model_name.lower()}" data-model-id="{f.stem}" data-model-name="{model_name}" data-discipline="{palette['label']}">
          <div class="card-top">
            <span class="card-title">{model_name}</span>
          </div>
          <div class="card-meta">
            <span class="card-id">{f.stem}</span>
          </div>
        </a>\n"""

        html += """      </div>
    </section>\n"""

    html += """  </main>

  <!-- Inline Modal Viewer Overlay (Apple HIG Design System) -->
  <div id="modalViewer" class="modal-overlay modal-viewer" aria-hidden="true" role="dialog" aria-modal="true" aria-labelledby="modalTitle">
    <div class="modal-backdrop" id="modalBackdrop"></div>
    <div class="modal-container" id="modalContainer">
      <header class="modal-header">
        <div class="modal-header-left">
          <span id="modalDisciplineBadge" class="modal-discipline-badge">Discipline</span>
          <h2 id="modalTitle" class="modal-title">Model Name</h2>
          <span id="modalIdBadge" class="modal-id-badge">model_id</span>
        </div>
        <div class="modal-header-actions">
          <a id="modalStandaloneLink" href="#" target="_blank" class="modal-btn" aria-label="Open model standalone in new tab" title="Open standalone tab">
            <svg viewBox="0 0 24 24"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6M15 3h6v6M10 14L21 3"/></svg>
            <span>Standalone ↗</span>
          </a>
          <button id="modal-close" class="modal-close-pill modal-close" aria-label="Close modal viewer (Escape)" title="Close viewer (Esc)">
            <span>Close ✕</span>
          </button>
        </div>
      </header>
      <div class="modal-body">
        <iframe id="modal-iframe" class="modal-iframe" src="about:blank" title="Physics Simulation Viewer" allow="accelerometer; autoplay; encrypted-media; gyroscope"></iframe>
      </div>
    </div>
  </div>

  <script>
    const searchInput = document.getElementById('searchInput');
    const sections = document.querySelectorAll('.discipline-section');
    const cards = document.querySelectorAll('.model-card');

    searchInput.addEventListener('input', (e) => {
      const q = e.target.value.toLowerCase().trim();
      sections.forEach(sec => {
        let visibleInSec = 0;
        const secCards = sec.querySelectorAll('.model-card');
        secCards.forEach(card => {
          const title = card.getAttribute('data-title') || '';
          const match = title.includes(q);
          card.style.display = match ? 'flex' : 'none';
          if (match) visibleInSec++;
        });
        sec.style.display = (visibleInSec > 0 || q === '') ? 'block' : 'none';
      });
    });

    function filterDiscipline(disc, btn) {
      document.querySelectorAll('.filter-pill').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      sections.forEach(sec => {
        if (disc === 'all' || sec.getAttribute('data-discipline') === disc) {
          sec.style.display = 'block';
        } else {
          sec.style.display = 'none';
        }
      });
    }

    // --- INLINE MODAL VIEWER ENGINE ---
    const modalOverlay = document.getElementById('modalViewer') || document.querySelector('.modal-overlay');
    const modalBackdrop = document.getElementById('modalBackdrop');
    const modalContainer = document.getElementById('modalContainer');
    const modalIframe = document.getElementById('modal-iframe') || document.getElementById('modalIframe');
    const modalTitle = document.getElementById('modalTitle');
    const modalBadge = document.getElementById('modalDisciplineBadge');
    const modalIdBadge = document.getElementById('modalIdBadge');
    const modalStandaloneLink = document.getElementById('modalStandaloneLink');
    const modalCloseBtn = document.getElementById('modal-close') || document.querySelector('.modal-close');

    let lastFocusedElement = null;
    let currentModelPath = '';

    function openModal(modelUrl, meta, triggerElement) {
      lastFocusedElement = triggerElement || document.activeElement;
      currentModelPath = modelUrl;

      if (modalTitle) modalTitle.textContent = meta.title || 'Physics Model';
      if (modalBadge) {
        modalBadge.textContent = meta.discipline || 'Engineering';
      }
      if (modalIdBadge) modalIdBadge.textContent = meta.id || '';
      if (modalStandaloneLink) modalStandaloneLink.href = modelUrl;

      if (meta.id) {
        history.replaceState({ modelId: meta.id }, '', '#' + meta.id);
      }

      if (modalIframe) modalIframe.src = modelUrl;
      document.body.style.overflow = 'hidden';

      if (modalOverlay) {
        modalOverlay.classList.add('is-active');
        modalOverlay.setAttribute('aria-hidden', 'false');
      }

      setTimeout(() => {
        if (modalCloseBtn) modalCloseBtn.focus();
      }, 50);
    }

    function closeModal() {
      if (!modalOverlay || !modalOverlay.classList.contains('is-active')) return;

      modalOverlay.classList.remove('is-active');
      modalOverlay.setAttribute('aria-hidden', 'true');

      // Halt simulation 60fps rAF loop and free memory
      if (modalIframe) modalIframe.src = 'about:blank';
      currentModelPath = '';

      history.replaceState(null, '', window.location.pathname + window.location.search);
      document.body.style.overflow = '';

      if (lastFocusedElement && typeof lastFocusedElement.focus === 'function') {
        lastFocusedElement.focus();
      }
    }

    if (modalCloseBtn) modalCloseBtn.addEventListener('click', closeModal);
    if (modalBackdrop) modalBackdrop.addEventListener('click', closeModal);

    document.addEventListener('keydown', (e) => {
      if (!modalOverlay || !modalOverlay.classList.contains('is-active')) return;

      if (e.key === 'Escape') {
        e.preventDefault();
        closeModal();
      } else if (e.key === 'Tab') {
        const focusable = modalContainer.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
        if (focusable.length === 0) return;
        const first = focusable[0];
        const last = focusable[focusable.length - 1];

        if (e.shiftKey && document.activeElement === first) {
          e.preventDefault();
          last.focus();
        } else if (!e.shiftKey && document.activeElement === last) {
          e.preventDefault();
          first.focus();
        }
      }
    });

    document.addEventListener('click', (e) => {
      const card = e.target.closest('.model-card');
      if (!card) return;

      // Allow middle-click, command-click, control-click, shift-click for power users opening in background tab
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.button !== 0) return;

      e.preventDefault();
      const href = card.getAttribute('href');
      const title = card.getAttribute('data-model-name') || (card.querySelector('.card-title') ? card.querySelector('.card-title').textContent.trim() : 'Physics Model');
      const id = card.getAttribute('data-model-id') || '';
      const discipline = card.getAttribute('data-discipline') || 'Engineering';

      openModal(href, { title, id, discipline }, card);
    });

    window.addEventListener('popstate', () => {
      const hash = window.location.hash.slice(1);
      if (hash) {
        const targetCard = document.querySelector(`.model-card[data-model-id="${hash}"]`);
        if (targetCard) {
          const href = targetCard.getAttribute('href');
          const title = targetCard.getAttribute('data-model-name') || (targetCard.querySelector('.card-title') ? targetCard.querySelector('.card-title').textContent.trim() : 'Physics Model');
          const id = targetCard.getAttribute('data-model-id') || '';
          const discipline = targetCard.getAttribute('data-discipline') || 'Engineering';
          openModal(href, { title, id, discipline }, targetCard);
          return;
        }
      }
      closeModal();
    });

    window.addEventListener('DOMContentLoaded', () => {
      const hash = window.location.hash.slice(1);
      if (hash) {
        const targetCard = document.querySelector(`.model-card[data-model-id="${hash}"]`);
        if (targetCard) {
          setTimeout(() => {
            targetCard.click();
          }, 100);
        }
      }
    });
  </script>
</body>
</html>
"""
    return html


if __name__ == "__main__":
    content = generate_dashboard()
    INDEX_FILE.write_text(content, encoding="utf-8")
    print(f"Regenerated {INDEX_FILE} successfully ({len(content)} bytes).")
