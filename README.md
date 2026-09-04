<h1 align="center">Engineering Physics UI Component Library</h1>

<p align="center">
  <strong>348 Scientific Interactive Models Across 23 Engineering Disciplines</strong><br>
  <a href="https://gparab.github.io/engineering-physics/">View the Live Dashboard</a>
</p>

<hr>

## Overview

In modern software development, bridging the gap between deep technical capability and refined visual design is a persistent challenge. This repository provides a comprehensive, production-ready suite of 348 interactive physics models, designed to be seamlessly integrated into enterprise dashboards, educational platforms, and professional web applications.

Every model in this library conforms strictly to a high-fidelity, editorial design system inspired by top-tier SaaS marketing surfaces. The architecture relies on contrast: a stark monochrome canvas juxtaposed against oversized pastel simulation blocks, driven by fine-grained variable typography and continuous, fluid mechanics.

## Architectural Standards

This library was heavily refactored via a massive parallel engineering effort to guarantee 100% adherence to a unified, academic design system.

### The Design System
- **Monochrome Chrome:** The surrounding application frame strictly utilizes `#000000` (dark mode default) and `#ffffff` (light mode), carrying all primary text and interaction surfaces.
- **Pastel Simulation Blocks:** The physics simulations are housed within full-content-width containers featuring 24px (`rounded.lg`) corners, mapped to an approved palette of soft pastels (Lime, Lilac, Cream, Mint, Pink, Coral, Navy).
- **Variable Typography:** The system exclusively utilizes the `Inter` font family (or standard sans-serif fallbacks) at precise weight increments (320, 340, 480, 540, 700). Hierarchy is established through structural weight, entirely eliminating intermediate gray text.
- **Pill Interactions:** All user controls, themes, and interactive toggles are rendered as stark 50px pill buttons (`rounded.pill`).

### Technical & Scientific Integrity
- **Continuous Pure Mechanics:** All arbitrary gimmicks, click-to-explode transitions, and DOM-destroying events have been purged. The models display pure, continuous 60fps physical simulations utilizing Canvas, SVG, or CSS animations.
- **Textbook Documentation:** Every model includes a dedicated "How It Works" structural section, containing concise, textbook-quality explanations and governing equations rendered exclusively in standard HTML unicode (no external LaTeX dependencies).
- **Zero External Dependencies:** With the exception of the standard GSAP CDN for complex tweening, every model is a completely standalone HTML document with inline styles and isolated JavaScript execution contexts.

## Repository Structure

The 348 models are organized into 23 canonical academic engineering directories, representing fields from Aerospace to Quantum Mechanics. 

```text
models/
├── aerospace_engineering/
├── chemical_engineering/
├── civil_engineering/
├── computer_science/
├── electrical_engineering/
├── fundamental_physics/
├── materials_science/
├── mechanical_engineering/
├── robotics_engineering/
└── ... (14 additional disciplines)
```

## Quality Assurance & Ratings

Every component in this repository has undergone rigorous automated and adversarial auditing. The central `model_ratings.md` ledger tracks the evaluation of all 348 models across three axes: Code Quality, Scientific Accuracy, and Visual Fidelity. 

The current repository mean score is **9.59 / 10.0**.

## Integration Guide

These components are engineered for rapid porting to modern component-based frameworks (React, Vue, Svelte, Angular). For detailed AI agent integration patterns, consult `AI_INTEGRATION.md`.

1. **Review the Live Dashboard:** Navigate to the [GitHub Pages deployment](https://gparab.github.io/engineering-physics/) to inspect the models in action.
2. **Consult the Master Catalog:** `micro_physics_master_catalog.md` contains the architectural blueprint for the entire collection.
3. **Extract and Port:** Isolate the target `.html` file. Extract the CSS custom properties, convert the structural HTML to your framework's templating syntax (e.g., JSX), and map the inline GSAP/Canvas logic to your component's mount lifecycle (e.g., `useEffect`).

## License

MIT License. Copyright 2026 Gautam Parab.
