# Engineering Physics — Official Style Kit

> **Design Standard:** Apple Human Interface Guidelines (HIG)  
> **Aesthetic:** Content-First Scientific Reference & Technical Journal  
> **Adaptation:** Automatic Light & Dark Appearance via `prefers-color-scheme`

---

## 1. Design Principles

- **Clarity:** Uncompromising legibility of equations, diagrams, and data. High visual contrast between physical bodies and background surfaces.
- **Deference:** The interface chrome recedes so the physical phenomenon is the focal point. Zero decorative flourishes, neon effects, or distracting gimmicks.
- **Depth & Materials:** Translucent frosted materials (`backdrop-filter: blur(20px)`) for fixed navigation and modals; crisp 1px system separators for structural definition.
- **Precision:** 60fps continuous numerical integration, high-DPI Retina canvas scaling, and KaTeX-rendered LaTeX formulas.

---

## 2. Typography

The library uses Apple's native system typeface family to deliver native performance and typographic sharpness across devices without external webfont overhead.

### Font Stacks
```css
/* Primary Interface & Body */
--font-sans: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'SF Pro Display', 
             'Helvetica Neue', Helvetica, Arial, sans-serif;

/* Monospace & Metadata */
--font-mono: 'SF Mono', SFMono-Regular, ui-monospace, 
             Menlo, Monaco, Consolas, monospace;

/* Mathematical Typesetting */
KaTeX v0.16.9 (Computer Modern / Latin Modern Math via CDN)
```

### Type Scale & Hierarchy

| Role | Font | Size | Weight | Line Height | Tracking | Usage |
|---|---|---|---|---|---|---|
| **Large Title** | `font-sans` | 34px (`2.125rem`) | 700 (Bold) | 1.15 | -0.8px | Hero header on index dashboard |
| **Title 1** | `font-sans` | 28px (`1.75rem`) | 700 (Bold) | 1.20 | -0.6px | Model page primary title (`h1`) |
| **Title 2** | `font-sans` | 22px (`1.375rem`) | 700 (Bold) | 1.25 | -0.4px | Section titles, discipline headers (`h2`) |
| **Headline** | `font-sans` | 17px (`1.0625rem`) | 600 (Semibold) | 1.35 | -0.3px | Card titles, modal header title |
| **Body** | `font-sans` | 16px–17px | 400 (Regular) | 1.48 | -0.1px | Explanation paragraphs ("How It Works") |
| **Subhead** | `font-sans` | 14px–15px | 480 / 500 | 1.40 | 0.0px | Filter pills, secondary metadata |
| **Caption / Eyebrow** | `font-mono` | 11px–12px | 500 (Medium) | 1.30 | +0.08em | Category eyebrow, badge, model ID |
| **Formula Display** | KaTeX | ~18px–20px | Normal | 1.50 | 0.02em | Mathematical formulas (`.equation-formula`) |

---

## 3. Color System

The palette directly adopts Apple's Semantic System Colors for accessibility and seamless light/dark mode adaptation.

### Interface & Surfaces

| Token | Light Mode (`#ffffff` canvas) | Dark Mode (`#1c1c1e` canvas) | Role |
|---|---|---|---|
| `--color-canvas` | `#ffffff` | `#1c1c1e` | Base page background |
| `--color-surface` | `#f2f2f7` | `#2c2c2e` | Grouped container / card background |
| `--color-separator` | `rgba(60, 60, 67, 0.29)` | `rgba(84, 84, 88, 0.65)` | 1px borders, dividing lines |
| `--label-primary` | `#000000` | `#ffffff` | Primary headings, prominent body text |
| `--label-secondary` | `rgba(60, 60, 67, 0.60)` | `rgba(235, 235, 245, 0.60)` | Descriptions, secondary meta labels |
| `--label-tertiary` | `rgba(60, 60, 67, 0.30)` | `rgba(235, 235, 245, 0.30)` | Watermarks, subtle helper markers |
| `--color-accent` | `#007aff` (System Blue) | `#0a84ff` (System Blue) | Interactive pills, links, key vector focus |

### Scientific Simulation & Data Visualization Palette

These colors are specifically calibrated for high contrast against `--sim-bg` (`#f2f2f7` in Light Mode, `#2c2c2e` in Dark Mode):

| Semantic Channel | Light Token | Dark Token | Physical Meaning / Typical Role |
|---|---|---|---|
| **Primary / Blue** | `#007aff` | `#0a84ff` | Primary motion paths, velocity vectors $\vec{v}$, electric fields |
| **Secondary / Green** | `#34c759` | `#30d158` | Stable equilibrium, kinetic energy, ground planes |
| **Teal / Cyan** | `#30b0c7` | `#40c8e0` | Fluid streamlines, wave crests, pressure contours |
| **Amber / Orange** | `#ff9500` | `#ff9f0a` | Forces $\vec{F}$, potential energy, thermal flux, warning limits |
| **Red / Alert** | `#ff3b30` | `#ff453a` | Gravitational weight $\vec{W}$, stress concentration, damping |
| **Purple** | `#af52de` | `#bf5af2` | Magnetic field $\vec{B}$, torque $\vec{\tau}$, quantum probability |
| **Indigo** | `#5856d6` | `#5e5ce6` | Phase space trajectories, nodal surfaces |
| **Pink** | `#ff2d55` | `#ff375f` | Resonance markers, critical thresholds |
| **Grid Lines** | `rgba(60, 60, 67, 0.08)` | `rgba(255, 255, 255, 0.08)` | Coordinate reference grid |
| **Coordinate Axes** | `rgba(60, 60, 67, 0.35)` | `rgba(235, 235, 245, 0.35)` | Origin axes, datum lines |

---

## 4. Spacing & Elevation (8-Point Grid)

All dimensions, margins, and paddings align to increments of **8px**:

```
8px   · 1 unit   → Minimum padding, pill gap, badge padding
16px  · 2 units  → Grid gap, card padding (mobile), label offsets
24px  · 3 units  → Card padding (desktop), section margin bottom, container padding
32px  · 4 units  → Navigation horizontal padding, hero padding bottom
40px  · 5 units  → Input field height, modal controls
48px  · 6 units  → Section vertical spacing, page bottom padding
64px  · 8 units  → Navigation height, major section separation
```

### Geometry & Radii
- **Cards / Containers:** `12px` (`--rounded-md`) — Apple standard grouped content radius.
- **Badges / Buttons:** `8px` (`--rounded-sm`) — Compact status tags.
- **Pills / Search Inputs:** `9999px` (`--rounded-pill`) — Filter tabs and search fields.
- **Max Widths:**
  - Simulation Viewport: `960px`
  - Dashboard Main Grid: `1280px`

---

## 5. Component Specifications

### A. Navigation Bar (Top Nav)
- **Position:** Sticky (`top: 0`, `z-index: 100`).
- **Material:** Translucent glass surface (`backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px)`).
- **Background:** `rgba(255, 255, 255, 0.85)` (Light) / `rgba(28, 28, 30, 0.85)` (Dark).
- **Border:** `1px solid var(--color-separator)` at bottom.
- **Height:** `64px`.

### B. Model Card (Grid Item)
- **Container:** `background: var(--color-surface); border: 1px solid var(--color-separator); border-radius: 12px;`
- **Padding:** `20px 24px`.
- **Interaction:**
  - `transform: translateY(-2px);` on hover
  - `box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);` (Light) / `rgba(0, 0, 0, 0.28);` (Dark)
  - Cursor: `pointer` (opens inline iframe modal)

### C. Inline Modal Iframe Viewer
- **Overlay:** Fullscreen `fixed` overlay, `backdrop-filter: blur(16px)`, `background: rgba(0, 0, 0, 0.45)`.
- **Window:** Max width `1120px`, height `88vh`, `border-radius: 16px`, `border: 1px solid var(--color-separator)`.
- **Toolbar:** Displays discipline badge, model title, and an accessible `"Close ✕"` pill button.
- **Lifecycle:** Clears iframe `src` to `about:blank` on close to freeze Canvas animation loops and release memory.

### D. Simulation Viewport (Canvas Container)
- **Container:** `background: var(--sim-bg); border-radius: 12px; border: 1px solid var(--sim-border);`
- **Aspect Ratio / Sizing:** `height: 62vh; min-height: 380px; max-height: 640px; width: 100%;`
- **Retina Scaling:** Automatic `window.devicePixelRatio` scaling via:
  ```javascript
  const dpr = window.devicePixelRatio || 1;
  canvas.width = Math.round(width * dpr);
  canvas.height = Math.round(height * dpr);
  ctx.resetTransform();
  ctx.scale(dpr, dpr);
  ```

### E. Scientific Explanation & Formula
- **Heading:** `Title 2` (22px bold) `"How It Works"`.
- **Description:** `Body` (16px regular, line-height 1.5), justified readability.
- **Formula Block:** Housed in `.equation-container` (`background: var(--sim-surface); border-radius: 8px; border: 1px solid var(--sim-border); padding: 14px 18px;`).
- **Equation Overflow:** `overflow-x: auto;` with subtle custom scrollbars for long KaTeX formulas.

---

## 6. Ready-to-Use CSS Custom Properties Block

```css
:root {
  /* Surface System */
  --color-canvas: #ffffff;
  --color-surface: #f2f2f7;
  --color-card: #f2f2f7;
  --color-separator: rgba(60, 60, 67, 0.29);
  --color-accent: #007aff;

  /* Typography & Text */
  --color-text: #000000;
  --color-text-secondary: rgba(60, 60, 67, 0.60);
  --color-text-tertiary: rgba(60, 60, 67, 0.30);
  --font-sans: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'SF Pro Display', 'Helvetica Neue', Helvetica, Arial, sans-serif;
  --font-mono: 'SF Mono', SFMono-Regular, ui-monospace, Menlo, Monaco, Consolas, monospace;

  /* Geometry */
  --rounded-sm: 8px;
  --rounded-md: 12px;
  --rounded-lg: 16px;
  --rounded-pill: 9999px;

  /* Simulation Canvas Colors */
  --sim-bg: #f2f2f7;
  --sim-surface: #ffffff;
  --sim-border: rgba(60, 60, 67, 0.29);
  --sim-text: #000000;
  --sim-text-muted: rgba(60, 60, 67, 0.60);
  --sim-grid: rgba(60, 60, 67, 0.08);
  --sim-axis: rgba(60, 60, 67, 0.35);

  /* Scientific Palette */
  --sim-blue: #007aff;
  --sim-teal: #30b0c7;
  --sim-green: #34c759;
  --sim-amber: #ff9500;
  --sim-orange: #ff9500;
  --sim-red: #ff3b30;
  --sim-purple: #af52de;
  --sim-indigo: #5856d6;
  --sim-pink: #ff2d55;
}

@media (prefers-color-scheme: dark) {
  :root {
    /* Surface System */
    --color-canvas: #1c1c1e;
    --color-surface: #2c2c2e;
    --color-card: #2c2c2e;
    --color-separator: rgba(84, 84, 88, 0.65);
    --color-accent: #0a84ff;

    /* Typography & Text */
    --color-text: #ffffff;
    --color-text-secondary: rgba(235, 235, 245, 0.60);
    --color-text-tertiary: rgba(235, 235, 245, 0.30);

    /* Simulation Canvas Colors */
    --sim-bg: #2c2c2e;
    --sim-surface: #3a3a3c;
    --sim-border: rgba(84, 84, 88, 0.65);
    --sim-text: #ffffff;
    --sim-text-muted: rgba(235, 235, 245, 0.60);
    --sim-grid: rgba(255, 255, 255, 0.08);
    --sim-axis: rgba(235, 235, 245, 0.35);

    /* Scientific Palette */
    --sim-blue: #0a84ff;
    --sim-teal: #40c8e0;
    --sim-green: #30d158;
    --sim-amber: #ff9f0a;
    --sim-orange: #ff9f0a;
    --sim-red: #ff453a;
    --sim-purple: #bf5af2;
    --sim-indigo: #5e5ce6;
    --sim-pink: #ff375f;
  }
}
```
