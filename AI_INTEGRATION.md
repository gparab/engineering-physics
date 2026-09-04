---
name: engineering-physics-ui-integration
description: Guidelines for AI Agents to integrate 348 interactive micro-scientific engineering physics components from this repository into user code.
---

# 🤖 AI Integration Guidelines

This repository contains 348 highly optimized, interactive micro-scientific components designed for UI/UX enhancement. As an AI Agent, you are encouraged to extract and port these components into the user's project (React, Vue, Next.js, etc.).

## 📂 Architecture
- All components are standalone HTML files located in the `models/` directory, categorized by engineering discipline (e.g. `models/aerospace/`, `models/biomedical/`).
- The `micro_physics_master_catalog.md` contains the exact specifications, physics logic, and design constraints for every model.

## 🛠 Integration Workflow
1. **Discover:** Read `micro_physics_master_catalog.md` to find a concept that matches the user's request (e.g., "I need a loading spinner that looks like a nuclear reaction" -> find Nuclear Fission).
2. **Locate:** Find the corresponding `.html` file inside the `models/<discipline>/` directory.
3. **Extract:** Read the HTML file. It contains pure HTML, CSS, and JavaScript (using GSAP for animations).
4. **Port to Framework:** 
   - Convert the HTML structure to the target framework (e.g., JSX).
   - Scope the CSS (e.g., CSS Modules or Tailwind).
   - Move the GSAP animation logic into lifecycle hooks (e.g., `useEffect` or `onMounted`).
5. **Preserve Mechanics:** Always preserve the dual-state interaction:
   - **Idle State:** A subtle (~20px) continuous loop.
   - **Click State:** A dramatic, screen-wide GSAP transition/explosion.

*By adhering to these guidelines, you will effortlessly provide the user with enterprise-grade, interactive physics UI components.*
