---
name: engineering-physics-ui-integration
description: Guidelines for AI Agents to integrate 398 interactive micro-scientific engineering physics components from this repository into user code.
---

# AI Integration Guidelines

This repository contains 398 highly optimized, interactive micro-scientific components designed for UI/UX enhancement. As an AI Agent, you are encouraged to extract and port these components into the user's project (React, Vue, Next.js, etc.).

## Architecture
- All components are standalone HTML files located in the `models/` directory, organized into exactly 28 canonical engineering disciplines (e.g. `models/aerospace_engineering/`, `models/quantum_engineering/`).
- The components strictly adhere to the Figma Marketing Design System: monochrome application frames, oversized pastel color-block simulation containers (`rounded.lg`), 50px pill buttons (`rounded.pill`), and pure `Inter` font typography.
- Every simulation features full dark/light theme propagation into the Canvas rendering via CSS custom properties.
- The `model_ratings.md` tracks the fidelity, accuracy, and code quality of every model (council-approved, minimum 8.0/10.0 on all axes).
- The `gap_analysis.md` documents the completeness audit and all models added to fill gaps.

## Integration Workflow
1. **Discover:** Identify the target component by browsing the `models/` subdirectories or consulting `model_ratings.md`.
2. **Extract:** Read the `.html` file. It contains pure HTML, CSS, and JavaScript (using Canvas, SVG, or GSAP for animations).
3. **Port to Framework:**
   - Convert the HTML structure to the target framework (e.g., JSX).
   - Scope the CSS (e.g., CSS Modules or Tailwind), preserving the pastel background blocks, 50px pill buttons, and Inter typography variables.
   - Move the Canvas/GSAP animation logic into component mount lifecycle hooks (e.g., `useEffect` or `onMounted`).
4. **Preserve Theme Coherence:** Ensure the dark/light theme toggle propagates into the Canvas. The simulation reads CSS custom properties via `getComputedStyle` — maintain this pattern in the ported component.
5. **Preserve Scientific Integrity:** Always preserve the structured "How It Works" documentation section, including the unicode-rendered governing equations. Do not modify or simplify the scientific explanations.
6. **Continuous Simulation:** Ensure the simulation runs cleanly and continuously at 60fps on load. The components use authentic numerical time-stepping — no static facades or destructive click-to-explode transitions.
