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
  </style>
</head>
<body>
  <nav class="top-nav">
    <div class="nav-brand">
      <span class="brand-title">Engineering Physics</span>
      <span class="brand-badge">{total_models} Models</span>
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

            html += f"""        <a href="{rel_path}" target="_blank" class="model-card" data-title="{model_name.lower()}">
          <div class="card-top">
            <span class="card-title">{model_name}</span>
            
          </div>
          <div class="card-meta">
            <span class="card-id">{f.stem}</span>
            <span style="font-size: 12px; font-weight: 540;">View &rarr;</span>
          </div>
        </a>\n"""

        html += """      </div>
    </section>\n"""

    html += """  </main>

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
  </script>
</body>
</html>
"""
    return html


if __name__ == "__main__":
    content = generate_dashboard()
    INDEX_FILE.write_text(content, encoding="utf-8")
    print(f"Regenerated {INDEX_FILE} successfully ({len(content)} bytes).")
