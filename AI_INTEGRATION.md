---
name: engineering-physics-ui-integration
description: Guidelines for AI Agents to integrate 348 interactive micro-scientific engineering physics components from this repository into user code.
---

# AI Integration Guidelines

This repository contains 348 highly optimized, interactive micro-scientific components designed for UI/UX enhancement. As an AI Agent, you are encouraged to extract and port these components into the user's project (React, Vue, Next.js, etc.).

## Architecture
- All components are standalone HTML files located in the `models/` directory, organized into exactly 23 canonical engineering disciplines (e.g. `models/aerospace_engineering/`, `models/biomedical_engineering/`).
- The components strictly adhere to the Figma Marketing Design System: monochrome application frames (`#000000` / `#ffffff`), oversized pastel color-block simulation containers (`rounded.lg`), 50px pill buttons (`rounded.pill`), and pure `Inter` font typography.
- The `micro_physics_master_catalog.md` contains the architectural blueprint for the entire collection.
- The `model_ratings.md` tracks the fidelity, accuracy, and code quality of every model.

## Integration Workflow
1. **Discover:** Identify the target component that matches the user's request by browsing the `models/` subdirectories or consulting `model_ratings.md`.
2. **Extract:** Read the `.html` file. It contains pure HTML, CSS, and JavaScript (using GSAP or pure Canvas for animations).
3. **Port to Framework:** 
   - Convert the HTML structure to the target framework (e.g., JSX).
   - Scope the CSS (e.g., CSS Modules or Tailwind), ensuring that the pastel background blocks, `50px` pill buttons, and `Inter` typography variables are preserved.
   - Move the GSAP/Canvas animation logic into component mount lifecycle hooks (e.g., `useEffect` or `onMounted`).
4. **Preserve Scientific Integrity:** Always preserve the structured "How It Works" documentation section, including the unicode-rendered governing equations, located below the simulation container. Do not modify or simplify the scientific explanations.
5. **Continuous Simulation:** Ensure the simulation runs cleanly and continuously at 60fps on load. The components do not use destructive "click-to-explode" transitions; interaction is handled through parameter toggles and timeline scrubbing.

*By adhering to these guidelines, you will effortlessly provide the user with enterprise-grade, interactive physics UI components that are both visually stunning and scientifically rigorous.*
