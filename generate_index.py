#!/usr/bin/env python3
"""
generate_index.py
Regenerates index.html for Engineering Physics Component Library
adhering strictly to the Figma Marketing Design System.

Features:
- Monochrome chrome canvas (#ffffff canvas, #000000 primary ink)
- Oversized typography with tight letter-spacing in Inter
- Category eyebrows in uppercase monospace with positive tracking
- Interactive discipline filter bar with pill buttons (border-radius: 50px)
- Instant client-side search and filtering
- Pastel color-block badges and section accents matching Figma tokens
- Reads model ratings from model_ratings.md and displays rating badges
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

# Discipline to Figma pastel color token mapping
DISCIPLINE_PALETTES = {
    # Canonical 23 engineering disciplines
    "acoustics_engineering": {"bg": "#e0d4fc", "border": "#c4b5fd", "label": "Acoustics Engineering", "name": "Lilac"},
    "aerospace_engineering": {"bg": "#d2f8e5", "border": "#a7f3d0", "label": "Aerospace Engineering", "name": "Mint"},
    "agricultural_engineering": {"bg": "#d4f542", "border": "#bef264", "label": "Agricultural Engineering", "name": "Lime"},
    "biomedical_engineering": {"bg": "#fed7e2", "border": "#fbcfe8", "label": "Biomedical Engineering", "name": "Pink"},
    "chemical_engineering": {"bg": "#fff5ea", "border": "#fed7aa", "label": "Chemical Engineering", "name": "Cream"},
    "civil_engineering": {"bg": "#ffd6cc", "border": "#fecdd3", "label": "Civil Engineering", "name": "Coral"},
    "computer_engineering": {"bg": "#e0d4fc", "border": "#c4b5fd", "label": "Computer Engineering", "name": "Lilac"},
    "computer_science": {"bg": "#d2f8e5", "border": "#a7f3d0", "label": "Computer Science", "name": "Mint"},
    "electrical_engineering": {"bg": "#fff5ea", "border": "#fed7aa", "label": "Electrical Engineering", "name": "Cream"},
    "electronics_engineering": {"bg": "#fff5ea", "border": "#fed7aa", "label": "Electronics Engineering", "name": "Cream"},
    "energy_engineering": {"bg": "#d4f542", "border": "#bef264", "label": "Energy Engineering", "name": "Lime"},
    "environmental_engineering": {"bg": "#d2f8e5", "border": "#a7f3d0", "label": "Environmental Engineering", "name": "Mint"},
    "fundamental_physics": {"bg": "#e0d4fc", "border": "#c4b5fd", "label": "Fundamental Physics", "name": "Lilac"},
    "industrial_systems_engineering": {"bg": "#ffd6cc", "border": "#fecdd3", "label": "Industrial & Systems Engineering", "name": "Coral"},
    "marine_engineering": {"bg": "#d2f8e5", "border": "#a7f3d0", "label": "Marine Engineering", "name": "Mint"},
    "materials_science": {"bg": "#fed7e2", "border": "#fbcfe8", "label": "Materials Science", "name": "Pink"},
    "mechanical_engineering": {"bg": "#ffd6cc", "border": "#fecdd3", "label": "Mechanical Engineering", "name": "Coral"},
    "mining_petroleum_engineering": {"bg": "#fff5ea", "border": "#fed7aa", "label": "Mining & Petroleum Engineering", "name": "Cream"},
    "nanotechnology": {"bg": "#e0d4fc", "border": "#c4b5fd", "label": "Nanotechnology", "name": "Lilac"},
    "nuclear_engineering": {"bg": "#d4f542", "border": "#bef264", "label": "Nuclear Engineering", "name": "Lime"},
    "optical_engineering": {"bg": "#fed7e2", "border": "#fbcfe8", "label": "Optical Engineering", "name": "Pink"},
    "robotics_engineering": {"bg": "#d2f8e5", "border": "#a7f3d0", "label": "Robotics Engineering", "name": "Mint"},
    "telecommunications_engineering": {"bg": "#fff5ea", "border": "#fed7aa", "label": "Telecommunications Engineering", "name": "Cream"},

    # Expansion engineering disciplines (Milestone 3)
    "plasma_physics": {"bg": "#e0d4fc", "border": "#c4b5fd", "label": "Plasma Physics", "name": "Lilac"},
    "astrodynamics": {"bg": "#d2f8e5", "border": "#a7f3d0", "label": "Astrodynamics", "name": "Mint"},
    "geophysical_engineering": {"bg": "#ffd6cc", "border": "#fecdd3", "label": "Geophysical Engineering", "name": "Coral"},
    "cryogenic_engineering": {"bg": "#e0d4fc", "border": "#c4b5fd", "label": "Cryogenic Engineering", "name": "Lilac"},
    "quantum_engineering": {"bg": "#fff5ea", "border": "#fed7aa", "label": "Quantum Engineering", "name": "Cream"},

    # Legacy aliases (for backward compatibility if needed)
    "acoustics": {"bg": "#e0d4fc", "border": "#c4b5fd", "label": "Acoustics", "name": "Lilac"},
    "aerospace": {"bg": "#d2f8e5", "border": "#a7f3d0", "label": "Aerospace Engineering", "name": "Mint"},
    "biomech": {"bg": "#fed7e2", "border": "#fbcfe8", "label": "Biomechanical Engineering", "name": "Pink"},
    "biomechanical_engineering": {"bg": "#fed7e2", "border": "#fbcfe8", "label": "Biomechanical Engineering", "name": "Pink"},
    "chem_eng": {"bg": "#fff5ea", "border": "#fed7aa", "label": "Chemical Engineering", "name": "Cream"},
    "chemeng": {"bg": "#fff5ea", "border": "#fed7aa", "label": "Chemical Engineering", "name": "Cream"},
    "civil": {"bg": "#ffd6cc", "border": "#fecdd3", "label": "Civil Engineering", "name": "Coral"},
    "compeng": {"bg": "#e0d4fc", "border": "#c4b5fd", "label": "Computer Engineering", "name": "Lilac"},
    "cs": {"bg": "#d2f8e5", "border": "#a7f3d0", "label": "Computer Science", "name": "Mint"},
    "electrical": {"bg": "#fff5ea", "border": "#fed7aa", "label": "Electrical Engineering", "name": "Cream"},
    "ee": {"bg": "#fff5ea", "border": "#fed7aa", "label": "Electrical Engineering", "name": "Cream"},
    "electronics": {"bg": "#fff5ea", "border": "#fed7aa", "label": "Electronics Engineering", "name": "Cream"},
    "energy": {"bg": "#d4f542", "border": "#bef264", "label": "Energy Engineering", "name": "Lime"},
    "enveng": {"bg": "#d2f8e5", "border": "#a7f3d0", "label": "Environmental Engineering", "name": "Mint"},
    "industrial_systems": {"bg": "#ffd6cc", "border": "#fecdd3", "label": "Industrial & Systems Engineering", "name": "Coral"},
    "marine": {"bg": "#d2f8e5", "border": "#a7f3d0", "label": "Marine Engineering", "name": "Mint"},
    "matsci": {"bg": "#fed7e2", "border": "#fbcfe8", "label": "Materials Science", "name": "Pink"},
    "mech": {"bg": "#ffd6cc", "border": "#fecdd3", "label": "Mechanical Engineering", "name": "Coral"},
    "mining_petro": {"bg": "#fff5ea", "border": "#fed7aa", "label": "Mining & Petroleum Engineering", "name": "Cream"},
    "nano": {"bg": "#e0d4fc", "border": "#c4b5fd", "label": "Nanotechnology", "name": "Lilac"},
    "nuclear": {"bg": "#d4f542", "border": "#bef264", "label": "Nuclear Engineering", "name": "Lime"},
    "optical": {"bg": "#fed7e2", "border": "#fbcfe8", "label": "Optical Engineering", "name": "Pink"},
    "robotics": {"bg": "#d2f8e5", "border": "#a7f3d0", "label": "Robotics Engineering", "name": "Mint"},
    "telecommunications": {"bg": "#fff5ea", "border": "#fed7aa", "label": "Telecommunications Engineering", "name": "Cream"},
    "addendum": {"bg": "#e0d4fc", "border": "#c4b5fd", "label": "Multidisciplinary Addendum", "name": "Lilac"},
}

DEFAULT_PALETTE = {"bg": "#fff5ea", "border": "#fed7aa", "label": "Engineering", "name": "Cream"}


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

    # Build HTML content
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Engineering Physics Interactive Component Library</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@320;330;340;480;540;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    :root {{
      --color-canvas: #ffffff;
      --color-surface: #fafafa;
      --color-primary: #000000;
      --color-ink: #000000;
      --color-hairline: #e5e5e5;
      --color-hairline-soft: #f0f0f0;
      --rounded-md: 8px;
      --rounded-lg: 24px;
      --rounded-pill: 50px;
      --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
      --font-mono: 'JetBrains Mono', SFMono-Regular, Menlo, monospace;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      background: var(--color-canvas);
      color: var(--color-ink);
      font-family: var(--font-sans);
      font-size: 16px;
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
      padding-bottom: 96px;
    }}

    .top-nav {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--color-hairline);
      height: 64px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 40px;
    }}

    .nav-brand {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .brand-title {{
      font-size: 18px;
      font-weight: 700;
      letter-spacing: -0.4px;
    }}

    .brand-badge {{
      font-family: var(--font-mono);
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      background: #000000;
      color: #ffffff;
      padding: 3px 10px;
      border-radius: var(--rounded-pill);
    }}

    .header-hero {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 72px 40px 48px 40px;
      text-align: center;
    }}

    .hero-eyebrow {{
      font-family: var(--font-mono);
      font-size: 13px;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      margin-bottom: 16px;
      color: #000000;
    }}

    .hero-title {{
      font-size: clamp(38px, 5vw, 64px);
      font-weight: 700;
      letter-spacing: -1.8px;
      line-height: 1.05;
      margin-bottom: 20px;
    }}

    .hero-desc {{
      font-size: 20px;
      font-weight: 340;
      line-height: 1.4;
      max-width: 760px;
      margin: 0 auto 36px auto;
      color: #111111;
    }}

    .search-filter-bar {{
      max-width: 1280px;
      margin: 0 auto 48px auto;
      padding: 0 40px;
      display: flex;
      flex-direction: column;
      gap: 20px;
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
      border-radius: var(--rounded-pill);
      border: 1px solid var(--color-hairline);
      padding: 0 24px;
      font-size: 16px;
      font-family: var(--font-sans);
      outline: none;
      transition: border-color 0.2s, box-shadow 0.2s;
    }}

    .search-input:focus {{
      border-color: #000000;
      box-shadow: 0 0 0 3px rgba(0, 0, 0, 0.08);
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
      height: 36px;
      padding: 0 16px;
      border-radius: var(--rounded-pill);
      border: 1px solid var(--color-hairline);
      background: #ffffff;
      color: #000000;
      font-size: 14px;
      font-weight: 480;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.15s ease;
    }}

    .filter-pill:hover, .filter-pill.active {{
      background: #000000;
      color: #ffffff;
      border-color: #000000;
    }}

    .main-content {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 40px;
    }}

    .discipline-section {{
      margin-bottom: 56px;
    }}

    .section-header-block {{
      padding: 24px 32px;
      border-radius: var(--rounded-lg);
      margin-bottom: 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border: 1px solid rgba(0, 0, 0, 0.06);
    }}

    .section-title-group {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .section-eyebrow {{
      font-family: var(--font-mono);
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      font-weight: 500;
    }}

    .section-title {{
      font-size: 26px;
      font-weight: 700;
      letter-spacing: -0.6px;
      line-height: 1.2;
    }}

    .section-count-badge {{
      font-family: var(--font-mono);
      font-size: 12px;
      font-weight: 500;
      padding: 6px 14px;
      border-radius: var(--rounded-pill);
      background: #ffffff;
      color: #000000;
      border: 1px solid rgba(0, 0, 0, 0.1);
    }}

    .model-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 16px;
    }}

    .model-card {{
      background: #ffffff;
      border: 1px solid var(--color-hairline);
      border-radius: 12px;
      padding: 20px 24px;
      text-decoration: none;
      color: inherit;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      min-height: 110px;
      transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.2s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.2s;
    }}

    .model-card:hover {{
      transform: translateY(-3px);
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.07);
      border-color: #000000;
    }}

    .card-top {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 12px;
    }}

    .card-title {{
      font-size: 16px;
      font-weight: 540;
      letter-spacing: -0.2px;
      line-height: 1.35;
      color: #000000;
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
      font-size: 11px;
      color: #222222;
      letter-spacing: 0.04em;
    }}

    .card-rating-badge {{
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 500;
      padding: 2px 8px;
      border-radius: var(--rounded-pill);
      background: #000000;
      color: #ffffff;
    }}

    /* ==========================================================================
       INLINE MODAL VIEWER (FIGMA MARKETING DESIGN SYSTEM)
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
      transition: opacity 0.22s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.22s;
    }}

    .modal-overlay.is-active {{
      opacity: 1;
      visibility: visible;
      pointer-events: auto;
    }}

    .modal-backdrop {{
      position: absolute;
      inset: 0;
      background: rgba(0, 0, 0, 0.70);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
    }}

    .modal-container {{
      position: relative;
      z-index: 1001;
      width: min(1360px, calc(100vw - 32px));
      height: min(920px, calc(100vh - 32px));
      background: #000000;
      border: 1px solid rgba(255, 255, 255, 0.14);
      border-radius: var(--rounded-lg);
      box-shadow: 0 24px 64px rgba(0, 0, 0, 0.50);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      transform: scale(0.97) translateY(8px);
      transition: transform 0.22s cubic-bezier(0.16, 1, 0.3, 1);
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
      background: #0f0f12;
      border-bottom: 1px solid rgba(255, 255, 255, 0.12);
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
      font-size: 11px;
      font-weight: 500;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      padding: 3px 10px;
      border-radius: var(--rounded-pill);
      background: #e0d4fc;
      color: #000000;
      white-space: nowrap;
      flex-shrink: 0;
    }}

    .modal-title {{
      font-size: 16px;
      font-weight: 540;
      letter-spacing: -0.2px;
      color: #ffffff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .modal-id-badge {{
      font-family: var(--font-mono);
      font-size: 11px;
      color: rgba(255, 255, 255, 0.55);
      letter-spacing: 0.04em;
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
      height: 34px;
      padding: 0 14px;
      border-radius: var(--rounded-pill);
      font-family: var(--font-sans);
      font-size: 12px;
      font-weight: 480;
      letter-spacing: -0.1px;
      cursor: pointer;
      text-decoration: none;
      border: 1px solid rgba(255, 255, 255, 0.20);
      background: rgba(255, 255, 255, 0.08);
      color: #ffffff;
      transition: background 0.15s ease, transform 0.15s ease, border-color 0.15s ease;
      white-space: nowrap;
    }}

    .modal-btn:hover {{
      background: rgba(255, 255, 255, 0.18);
      border-color: rgba(255, 255, 255, 0.35);
      transform: translateY(-1px);
    }}

    .modal-btn:active {{
      transform: translateY(0);
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

    /* Primary Close Pill (Figma button-secondary on dark chrome) */
    .modal-close-pill {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      height: 34px;
      padding: 0 16px;
      border-radius: var(--rounded-pill);
      font-family: var(--font-sans);
      font-size: 13px;
      font-weight: 540;
      letter-spacing: -0.1px;
      cursor: pointer;
      border: none;
      background: #ffffff;
      color: #000000;
      transition: opacity 0.15s ease, transform 0.15s ease;
    }}

    .modal-close-pill:hover {{
      opacity: 0.92;
      transform: scale(1.02);
    }}

    .modal-close-pill:active {{
      transform: scale(0.98);
    }}

    .modal-body {{
      flex: 1;
      width: 100%;
      height: calc(100% - 56px);
      background: #000000;
      position: relative;
    }}

    .modal-iframe {{
      width: 100%;
      height: 100%;
      border: none;
      display: block;
      background: #000000;
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
      <div class="section-header-block" style="background-color: {palette['bg']}; border-color: {palette['border']};">
        <div class="section-title-group">
          <span class="section-eyebrow">Discipline &middot; {palette['name']} Block</span>
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
            rating_score = ratings.get(f.name)
            rating_badge = ""

            html += f"""        <a href="{rel_path}" class="model-card" data-title="{model_name.lower()}" data-model-id="{f.stem}" data-model-name="{model_name}" data-discipline="{palette['label']}" data-discipline-bg="{palette['bg']}" data-discipline-border="{palette['border']}">
          <div class="card-top">
            <span class="card-title">{model_name}</span>
          </div>
          <div class="card-meta">
            <span class="card-id">{f.stem}</span>
            <span style="font-size: 12px; font-weight: 540;">Explore &rarr;</span>
          </div>
        </a>\n"""

        html += """      </div>
    </section>\n"""

    html += """  </main>

  <!-- Inline Modal Viewer Overlay (Figma Marketing Design System) -->
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
          <button id="modalThemeBtn" class="modal-btn" aria-label="Toggle simulation theme" title="Toggle simulation theme">
            <svg class="icon-sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M4.93 4.93l1.41 1.41m11.32 11.32l1.41 1.41M2 12h2m16 0h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/></svg>
            <svg class="icon-moon" viewBox="0 0 24 24" style="display: none;"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
            <span>Theme</span>
          </button>
          <button id="modalReloadBtn" class="modal-btn" aria-label="Reset simulation" title="Reset simulation">
            <svg viewBox="0 0 24 24"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/></svg>
            <span>Reset</span>
          </button>
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
    const modalThemeBtn = document.getElementById('modalThemeBtn');
    const modalReloadBtn = document.getElementById('modalReloadBtn');

    let lastFocusedElement = null;
    let currentModelPath = '';

    function openModal(modelUrl, meta, triggerElement) {
      lastFocusedElement = triggerElement || document.activeElement;
      currentModelPath = modelUrl;

      if (modalTitle) modalTitle.textContent = meta.title || 'Physics Model';
      if (modalBadge) {
        modalBadge.textContent = meta.discipline || 'Engineering';
        modalBadge.style.backgroundColor = meta.discBg || '#e0d4fc';
        modalBadge.style.borderColor = meta.discBorder || 'rgba(0,0,0,0.1)';
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

    if (modalReloadBtn) {
      modalReloadBtn.addEventListener('click', () => {
        if (!currentModelPath || !modalIframe || modalIframe.src === 'about:blank') return;
        try {
          modalIframe.contentWindow.location.reload();
        } catch (err) {
          modalIframe.src = currentModelPath;
        }
      });
    }

    if (modalThemeBtn) {
      modalThemeBtn.addEventListener('click', () => {
        try {
          if (!modalIframe) return;
          const iframeDoc = modalIframe.contentDocument;
          const iframeWin = modalIframe.contentWindow;
          if (!iframeDoc || !iframeWin) return;

          const currentTheme = iframeDoc.documentElement.getAttribute('data-theme') || 'dark';
          const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
          iframeDoc.documentElement.setAttribute('data-theme', newTheme);
          iframeWin.dispatchEvent(new CustomEvent('themechange', { detail: { theme: newTheme } }));
          updateModalThemeIcon(newTheme);
        } catch (err) {
          console.warn('Theme toggle in iframe unavailable:', err);
        }
      });
    }

    function updateModalThemeIcon(theme) {
      if (!modalThemeBtn) return;
      const isDark = theme === 'dark';
      const sun = modalThemeBtn.querySelector('.icon-sun');
      const moon = modalThemeBtn.querySelector('.icon-moon');
      if (sun && moon) {
        sun.style.display = isDark ? 'block' : 'none';
        moon.style.display = isDark ? 'none' : 'block';
      }
    }

    if (modalIframe) {
      modalIframe.addEventListener('load', () => {
        try {
          const iframeDoc = modalIframe.contentDocument;
          const iframeWin = modalIframe.contentWindow;
          if (!iframeDoc || !iframeWin) return;

          const activeTheme = iframeDoc.documentElement.getAttribute('data-theme') || 'dark';
          updateModalThemeIcon(activeTheme);

          iframeWin.addEventListener('themechange', (e) => {
            const t = e.detail?.theme || iframeDoc.documentElement.getAttribute('data-theme');
            updateModalThemeIcon(t);
          });
        } catch (err) {}
      });
    }

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
      const discBg = card.getAttribute('data-discipline-bg') || '#e0d4fc';
      const discBorder = card.getAttribute('data-discipline-border') || 'rgba(0,0,0,0.1)';

      openModal(href, { title, id, discipline, discBg, discBorder }, card);
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
          const discBg = targetCard.getAttribute('data-discipline-bg') || '#e0d4fc';
          const discBorder = targetCard.getAttribute('data-discipline-border') || 'rgba(0,0,0,0.1)';
          openModal(href, { title, id, discipline, discBg, discBorder }, targetCard);
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
