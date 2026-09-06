<h1 align="center">Engineering Physics UI Component Library</h1>

<p align="center">
  <strong>398 Scientific Interactive Models Across 28 Engineering Disciplines</strong><br>
  <a href="https://gparab.github.io/engineering-physics/">View the Live Dashboard</a>
</p>

<hr>

## Overview

This repository provides a comprehensive, production-ready suite of 398 interactive physics models, designed to be seamlessly integrated into enterprise dashboards, educational platforms, and professional web applications.

Every model is a genuine, continuously running 60fps physics simulation — not a static diagram. Particles move, fields evolve, waves propagate, mechanisms articulate, and fluids flow. Each simulation has been independently reviewed and certified by a council of domain engineers and design architects, scoring a minimum of 8.0/10.0 across Scientific Coherence, Aesthetic Design, and UI/UX Adherence.

## Design System

The library adheres to a unified editorial design system derived from top-tier SaaS marketing aesthetics.

### Visual Architecture
- **Monochrome Chrome:** The application frame uses strict black/white for all primary text, navigation, and interaction surfaces.
- **Pastel Simulation Blocks:** Physics simulations are housed within full-content-width containers with 24px rounded corners, mapped to an approved palette of soft pastels (Lime, Lilac, Cream, Mint, Pink, Coral, Navy).
- **Variable Typography:** The `Inter` font family at precise weight increments (320, 340, 480, 540, 700). Hierarchy is established through structural weight, eliminating intermediate gray text.
- **Pill Controls:** All interactive toggles and controls are rendered as 50px pill buttons.

### Dark & Light Theme
Every model features a fully functional dark/light theme toggle. The theme propagates directly into the simulation canvas — canvas backgrounds, grid lines, particles, vectors, and text annotations all invert cleanly. No jarring mismatched surfaces.

## Engineering Disciplines

The 398 models span 28 canonical engineering disciplines:

| Discipline | Models | Discipline | Models |
|---|:---:|---|:---:|
| Acoustics Engineering | 8 | Marine Engineering | 10 |
| Aerospace Engineering | 15 | Materials Science | 15 |
| Agricultural Engineering | 10 | Mechanical Engineering | 25 |
| Astrodynamics & Space Systems | 10 | Mining & Petroleum Engineering | 10 |
| Biomedical Engineering | 15 | Nanotechnology | 10 |
| Chemical Engineering | 20 | Nuclear Engineering | 16 |
| Civil Engineering | 20 | Optical Engineering | 10 |
| Computer Engineering | 20 | Plasma Physics | 10 |
| Computer Science | 21 | Quantum Engineering | 10 |
| Cryogenic Engineering | 10 | Robotics Engineering | 12 |
| Electrical Engineering | 25 | Telecommunications Engineering | 20 |
| Electronics Engineering | 20 | Fundamental Physics | 12 |
| Energy Engineering | 12 | Geophysical Engineering | 10 |
| Environmental Engineering | 10 | Industrial Systems Engineering | 12 |

## Quality Assurance

Every model has undergone:
- **6-gate automated verification** — rendering logic depth, frame-rate stability, theme coherence, equation authenticity, structural compliance, and anti-gimmick checks.
- **Adversarial multi-frame testing** — headless Canvas execution across 30 animation frames to verify non-zero coordinate variance (no static facades).
- **Independent council review** — scored on Scientific Coherence, Aesthetic Design, and UI/UX Adherence with a strict 8.0/10.0 minimum threshold.

Repository mean score: **9.60 / 10.0**. Full ratings available in `model_ratings.md`.

## Repository Structure

```text
models/
├── acoustics_engineering/
├── aerospace_engineering/
├── astrodynamics/
├── biomedical_engineering/
├── chemical_engineering/
├── civil_engineering/
├── computer_engineering/
├── computer_science/
├── cryogenic_engineering/
├── electrical_engineering/
├── electronics_engineering/
├── energy_engineering/
├── environmental_engineering/
├── fundamental_physics/
├── geophysical_engineering/
├── industrial_systems_engineering/
├── marine_engineering/
├── materials_science/
├── mechanical_engineering/
├── mining_petroleum_engineering/
├── nanotechnology/
├── nuclear_engineering/
├── optical_engineering/
├── plasma_physics/
├── quantum_engineering/
├── robotics_engineering/
└── telecommunications_engineering/
```

## Integration Guide

These components are engineered for rapid porting to modern frameworks (React, Vue, Svelte, Angular). For detailed AI agent integration patterns, consult `AI_INTEGRATION.md`.

1. **Review the Live Dashboard:** Navigate to the [GitHub Pages deployment](https://gparab.github.io/engineering-physics/) to inspect the models in action.
2. **Consult the Ratings:** `model_ratings.md` contains the council-approved quality scores for every model.
3. **Extract and Port:** Isolate the target `.html` file. Extract the CSS custom properties, convert the structural HTML to your framework's templating syntax, and map the Canvas/GSAP logic to your component's mount lifecycle.

## License

MIT License. Copyright 2026 Gautam Parab.
