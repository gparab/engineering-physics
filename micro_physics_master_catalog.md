# Micro-Scientific Physics Models — Master Catalog

> **344 models** across **24+ engineering disciplines**
> Each model defines a tiny animated icon (~20px), its idle physics animation, and a dramatic page-wide click-to-disappear motion.

---

## Table of Contents & Coverage

| # | Engineering Discipline | Models | Status |
|---|------------------------|:------:|:------:|
| 1 | Mechanical Engineering | 25 | ✅ |
| 2 | Aerospace Engineering | 15 | ✅ |
| 3 | Electrical Engineering | 25 | ✅ |
| 4 | Electronics Engineering | 20 | ✅ |
| 5 | Computer Engineering | 20 | ✅ |
| 6 | Computer Science | 20 | ✅ |
| 7 | Telecommunications | 20 | ✅ |
| 8 | Chemical Engineering | 20 | ✅ |
| 9 | Nuclear Engineering | 15 | ✅ |
| 10 | Civil Engineering | 20 | ✅ |
| 11 | Environmental Engineering | 10 | ✅ |
| 12 | Mining & Petroleum Engineering | 10 | ✅ |
| 13 | Biomedical Engineering | 15 | ✅ |
| 14 | Agricultural Engineering | 10 | ✅ |
| 15 | Marine/Ocean Engineering | 10 | ✅ |
| 16 | Materials Science & Engineering | 15 | ✅ |
| 17 | Nanotechnology | 10 | ✅ |
| 18 | Optical Engineering | 10 | ✅ |
| 19 | Acoustics Engineering | 8 | ✅ |
| 20 | Energy Engineering | 12 | ✅ |
| 21 | Robotics & Mechatronics | 12 | ✅ |
| 22 | Industrial & Systems Engineering | 10 | ✅ |
| 23 | Fundamental Physics | 12 | ✅ |
| | **TOTAL** | **344** | |

---

# PART 1 — MECHANICAL, AEROSPACE, ELECTRICAL, ELECTRONICS, CHEMICAL, NUCLEAR

---

## 1. MECHANICAL ENGINEERING (25 Models)

### 1. Free Body Diagram
- **Domain:** Statics | **Color:** `#E74C3C` | **Shape:** Square with three outward force arrows
- **Idle:** Arrows pulse in length, balancing in equilibrium
- **Click:** Block shatters; force vectors shoot across the screen in their respective directions
- **Physics:** Newton's First Law — Static Equilibrium (ΣF = 0)

### 2. Simple Pendulum
- **Domain:** Dynamics | **Color:** `#3498DB` | **Shape:** Circle on a string from a pivot
- **Idle:** Swings back and forth in sinusoidal arc
- **Click:** String snaps at pivot; bob launches in parabolic trajectory off-screen
- **Physics:** Conservation of energy, SHM (T = 2π√(L/g))

### 3. Four-Bar Linkage
- **Domain:** Kinematics / Mechanisms | **Color:** `#9B59B6` | **Shape:** Four connected line segments with pivot joints
- **Idle:** Input crank rotates continuously; output rocker oscillates
- **Click:** Joints detach; four links spin out chaotically from unconstrained DOF
- **Physics:** Grashof's condition and planar kinematics

### 4. PV Diagram (Carnot Cycle)
- **Domain:** Thermodynamics | **Color:** `#E67E22` | **Shape:** Closed loop on tiny coordinate axes
- **Idle:** Glowing dot traces the cycle path (expansion → compression)
- **Click:** Area inside the curve expands to fill the entire screen in a flash of heat energy
- **Physics:** Ideal Carnot cycle, First Law (W = ∮ P dV)

### 5. Venturi Tube
- **Domain:** Fluid Mechanics | **Color:** `#1ABC9C` | **Shape:** Pipe narrowing at center
- **Idle:** Dots speed up through the throat, stretch horizontally
- **Click:** Throat chokes; tube bursts outward, sending shockwave of particles across screen
- **Physics:** Bernoulli's principle and continuity (A₁V₁ = A₂V₂)

### 6. Damped Harmonic Oscillator
- **Domain:** Vibrations | **Color:** `#F1C40F` | **Shape:** Mass on spring + dashpot
- **Idle:** Mass oscillates with decaying amplitude
- **Click:** Damping drops to zero; amplitude grows exponentially, spring flings mass off-screen
- **Physics:** Underdamped 2nd-order systems (mẍ + cẋ + kx = 0)

### 7. Mohr's Circle
- **Domain:** Material Strength | **Color:** `#8E44AD` | **Shape:** Circle on σ-τ axes with principal axis line
- **Idle:** Circle rotates around center, simulating varying stress planes
- **Click:** Principal stress exceeds UTS; circle fractures along 45° shear plane
- **Physics:** 2D stress tensor transformation and principal stresses

### 8. Stress-Strain Curve
- **Domain:** Material Strength | **Color:** `#C0392B` | **Shape:** Graph with elastic region, yield, necking
- **Idle:** Stress marker crawls up linear region and rebounds (elastic)
- **Click:** Marker blasts past yield and UTS, curve snaps at fracture point
- **Physics:** Hooke's Law and ductile material failure mechanics

### 9. Poiseuille Pipe Flow
- **Domain:** Fluid Mechanics | **Color:** `#2980B9` | **Shape:** Pipe cross-section with parabolic velocity profile
- **Idle:** Central arrows glide faster than outer arrows (parabolic)
- **Click:** Reynolds number spikes; parabolic profile dissolves into chaotic turbulent eddies
- **Physics:** Laminar flow and no-slip boundary condition

### 10. Shell-and-Tube Heat Exchanger
- **Domain:** Heat Transfer | **Color:** `#D35400` | **Shape:** Cylinder with parallel tubes inside
- **Idle:** Counter-flowing red/blue gradient dots through shell and tubes
- **Click:** Thermal equilibrium reached; everything flashes grey and evaporates
- **Physics:** Convection, conduction, LMTD

### 11. Involute Gear Pair
- **Domain:** Gear Systems | **Color:** `#7F8C8D` | **Shape:** Two meshing gears (pinion + gear)
- **Idle:** Gears rotate, teeth engage along line of action
- **Click:** Torque spike shears teeth; fragments fly tangentially
- **Physics:** Fundamental law of gear-tooth action

### 12. Hydrodynamic Journal Bearing
- **Domain:** Tribology | **Color:** `#F39C12` | **Shape:** Off-center shaft inside outer ring with fluid wedge
- **Idle:** Shaft spins on converging fluid wedge without contact
- **Click:** Oil film breaks; shaft grinds wall, generating friction sparks
- **Physics:** Reynolds equation for hydrodynamic lubrication

### 13. Centrifugal Pump
- **Domain:** Turbomachinery | **Color:** `#16A085` | **Shape:** Volute casing with rotating impeller
- **Idle:** Impeller blades sweep fluid from eye outward
- **Click:** Cavitation — vapor bubbles implode, pump disintegrates
- **Physics:** Euler's turbomachine equation

### 14. Brayton Cycle
- **Domain:** Thermodynamics | **Color:** `#E74C3C` | **Shape:** Compressor → combustor → turbine → HX loop
- **Idle:** Gas flow loop, turning red in combustor, spinning turbine
- **Click:** Turbine overspeeds; blades shear off, exhaust rockets remains off-page
- **Physics:** Gas turbine thermodynamics, isentropic compression/expansion

### 15. Rankine Cycle
- **Domain:** Thermodynamics | **Color:** `#34495E` | **Shape:** T-s diagram with vapor dome
- **Idle:** Tracer moves through two-phase dome (boiling ↔ condensing)
- **Click:** Boiler overheats; dome pressurizes and explodes in high-pressure steam
- **Physics:** Steam power plant thermodynamics, phase-change physics

### 16. Thin-Walled Pressure Vessel
- **Domain:** Pressure Vessels | **Color:** `#2C3E50` | **Shape:** Cylindrical tank with hoop stress arrows
- **Idle:** Tank bulges imperceptibly as internal pressure fluctuates
- **Click:** Hoop stress exceeds limit; longitudinal zipper rupture splits tank
- **Physics:** Biaxial stress (σ_hoop = pr/t)

### 17. Boundary Layer Profile
- **Domain:** Fluid Mechanics | **Color:** `#8E44AD` | **Shape:** Flat plate with logarithmic velocity curve
- **Idle:** Velocity vectors flow from zero at wall to freestream
- **Click:** Adverse pressure gradient triggers separation; turbulent vortices consume screen
- **Physics:** Navier-Stokes boundary layer equations

### 18. Euler Buckling Column
- **Domain:** Statics / Strength | **Color:** `#C0392B` | **Shape:** Slender vertical beam, pinned ends, downward load
- **Idle:** Beam bows slightly, shimmering in unstable equilibrium
- **Click:** Load exceeds P_cr; column bows into half-sine, folds in half
- **Physics:** Euler's critical load (P_cr = π²EI/L²)

### 19. Gyroscope
- **Domain:** Dynamics | **Color:** `#F1C40F` | **Shape:** Spinning rotor in gimbal rings
- **Idle:** Rotor spins rapidly; assembly undergoes slow precession
- **Click:** Gimbal lock; rings align, gyroscope tumbles violently off-screen
- **Physics:** Conservation of angular momentum, gyroscopic precession

### 20. Spring-Mass-Damper System
- **Domain:** Vibrations | **Color:** `#3498DB` | **Shape:** Ceiling → spring → dashpot → mass block
- **Idle:** Steady forced vibration at low frequency
- **Click:** Forcing frequency matches ω_n (resonance); spring shatters, mass flies away
- **Physics:** Forced harmonic vibrations and resonance

### 21. Vapor Compression Refrigeration
- **Domain:** HVAC | **Color:** `#00CEC9` | **Shape:** Compressor → condenser → expansion valve → evaporator
- **Idle:** Refrigerant changes from hot red gas to cold blue liquid through loop
- **Click:** Expansion valve freezes open; liquid slugs compressor, frost wave covers screen
- **Physics:** Reversed Carnot cycle, latent heat of vaporization

### 22. Turning Operation (Lathe)
- **Domain:** Manufacturing | **Color:** `#95A5A6` | **Shape:** Spinning workpiece + cutting tool + chip
- **Idle:** Workpiece rotates, tool advances, continuous curling chip
- **Click:** Tool chatter → catastrophic failure; shrapnel flies, workpiece ejects
- **Physics:** Orthogonal metal cutting, shear plane theory

### 23. Conduction through Composite Wall
- **Domain:** Heat Transfer | **Color:** `#E67E22` | **Shape:** Three layered rectangles with temperature gradient
- **Idle:** Thermal waves pulse hot→cold, slowing in insulating layer
- **Click:** Infinite conductivity; gradient snaps flat, wall melts uniformly
- **Physics:** Fourier's Law, thermal resistance networks

### 24. Cam and Follower
- **Domain:** Mechanisms | **Color:** `#8E44AD` | **Shape:** Egg-shaped lobe rotating against vertical rod
- **Idle:** Cam rotates; rotary → linear motion conversion
- **Click:** RPM exceeds limit; follower jumps, rockets vertically off-screen
- **Physics:** Kinematic synthesis, jerk limits, contact mechanics

### 25. Torsion of Circular Shaft
- **Domain:** Material Strength | **Color:** `#D35400` | **Shape:** Cylinder with torque arrow, helical grid
- **Idle:** Shaft twists back and forth elastically
- **Click:** Ultimate torsional failure; shaft necks down and tears apart
- **Physics:** Hooke's law in shear, polar moment (τ = Tr/J)

---

## 2. AEROSPACE ENGINEERING (15 Models)

### 26. Airfoil Lift (Kutta-Joukowski)
- **Domain:** Aerodynamics | **Color:** `#3498DB` | **Shape:** Teardrop airfoil with streamlines
- **Idle:** Streamlines split around airfoil, faster flow over top
- **Click:** Angle of attack pitches up (stall); flow separates in swirling vortices, airfoil plummets
- **Physics:** Circulation theory of lift (L = ρVΓ)

### 27. Keplerian Orbit
- **Domain:** Orbital Mechanics | **Color:** `#9B59B6` | **Shape:** Central mass + elliptical path + satellite
- **Idle:** Satellite speeds up at periapsis, slows at apoapsis (equal areas)
- **Click:** Retrograde thrust at apoapsis; periapsis drops, satellite crashes into center
- **Physics:** Kepler's Laws, conservation of angular momentum

### 28. Hohmann Transfer
- **Domain:** Orbital Mechanics | **Color:** `#2ECC71` | **Shape:** Two circular orbits + elliptical transfer arc
- **Idle:** Ship executes ΔV₁, coasts, executes ΔV₂ (repeats)
- **Click:** Second burn fails; ship escapes on hyperbolic trajectory across screen
- **Physics:** Vis-viva equation, minimum-energy orbital maneuvers

### 29. Converging-Diverging Nozzle (De Laval)
- **Domain:** Propulsion | **Color:** `#E74C3C` | **Shape:** Hourglass nozzle with pressure contours
- **Idle:** Subsonic → Mach 1 at throat → supersonic expansion
- **Click:** Backpressure rises; violent normal shockwave shatters nozzle
- **Physics:** Compressible flow, choking, isentropic expansion

### 30. Shock Wave / Mach Cone
- **Domain:** Hypersonics | **Color:** `#F39C12` | **Shape:** Wedge trailing an angled shock line
- **Idle:** Cone flies forward dragging oblique shock with temperature gradients
- **Click:** Velocity drops below Mach 1; shock detaches, ripples forward, dissipates
- **Physics:** Oblique shock relations, supersonic compressibility

### 31. Aircraft Principal Axes (Roll/Pitch/Yaw)
- **Domain:** Flight Dynamics | **Color:** `#34495E` | **Shape:** Airplane silhouette with X/Y/Z axes
- **Idle:** Tiny stabilizing corrections along all three axes
- **Click:** Unrecoverable flat spin; aircraft corkscrews off the page
- **Physics:** Rigid body dynamics, aerodynamic stability derivatives

### 32. Escape Velocity
- **Domain:** Orbital Mechanics | **Color:** `#95A5A6` | **Shape:** Planet at bottom of 3D gravity well funnel
- **Idle:** Mass circles up funnel wall but stays trapped
- **Click:** Mass acquires v = √(2GM/r); shoots up and coasts across flat grid forever
- **Physics:** Kinetic energy overcoming gravitational potential

### 33. Turbojet Engine
- **Domain:** Propulsion | **Color:** `#D35400` | **Shape:** Cutaway: inlet → compressor → combustor → turbine
- **Idle:** Rotors spin, cool blue air → fiery red combustion → exhaust blast
- **Click:** Compressor stall; flow reverses, fireball out the front intake
- **Physics:** Jet propulsion, Newton's Third Law, Brayton cycle

### 34. Ion Thruster
- **Domain:** Propulsion | **Color:** `#00A8FF` | **Shape:** Cylindrical chamber with electrostatic grids
- **Idle:** Blue plasma ions accelerate across grid, faint blue beam
- **Click:** Neutralizer fails; spacecraft charges to kV, ion beam curls back, shorts out
- **Physics:** Electrostatic acceleration, specific impulse (I_sp)

### 35. Re-entry Blunt Body
- **Domain:** Re-entry Physics | **Color:** `#E67E22` | **Shape:** Capsule with detached bow shock
- **Idle:** Fiery plasma sheath wraps around blunt shield
- **Click:** Ablation shield depleted; hull incinerates into glowing dust in the wake
- **Physics:** Hypersonic aerodynamics, blunt-body theory

### 36. Solid Rocket Booster
- **Domain:** Propulsion | **Color:** `#C0392B` | **Shape:** Cylinder with star-shaped grain burning outward
- **Idle:** Core burns outward, constant pressure, bright exhaust
- **Click:** Propellant crack increases burn area; chamber overspikes, casing detonates
- **Physics:** Solid propellant burn rates, pressure-area equilibrium

### 37. Drag Polar
- **Domain:** Aerodynamics | **Color:** `#16A085` | **Shape:** Parabolic C_L vs C_D graph
- **Idle:** Marker traces parabola as angle of attack changes
- **Click:** Induced drag overwhelms; curve collapses to x-axis, wipes screen
- **Physics:** Parasitic vs induced drag (C_D = C_D0 + kC_L²)

### 38. Lifting Line Theory (Wing Vortices)
- **Domain:** Aerodynamics | **Color:** `#8E44AD` | **Shape:** Finite wing with trailing wingtip vortices
- **Idle:** Wing glides forward; vortices spin and roll up behind tips
- **Click:** Ground effect cancels vortices; wing slides frictionlessly off-screen
- **Physics:** Prandtl's lifting-line theory, downwash

### 39. Composite Sandwich Panel
- **Domain:** Composite Structures | **Color:** `#2C3E50` | **Shape:** Two face sheets + honeycomb core
- **Idle:** Panel flexes under bending; faces carry tension/compression, core carries shear
- **Click:** Core delamination; honeycomb rips, face sheets snap in opposite directions
- **Physics:** Anisotropic material properties, stiffness-to-weight optimization

### 40. Satellite Reaction Wheel
- **Domain:** Satellite Systems | **Color:** `#F1C40F` | **Shape:** Flywheel on motor inside satellite bus
- **Idle:** Wheel spins CW; satellite counter-rotates CCW slowly
- **Click:** Momentum saturation; wheel hits max RPM, satellite spins wildly off-screen
- **Physics:** Conservation of angular momentum, attitude control

---

## 3. ELECTRICAL ENGINEERING (25 Models)

### 41. Ohm's Law (Resistor)
- **Domain:** Circuit Analysis | **Color:** `#F39C12` | **Shape:** Zigzag line with flowing dots
- **Idle:** Dots pulse through zigzag, speed varies with width changes
- **Click:** Zigzag heats red and evaporates into thermal particles drifting upward
- **Physics:** V = IR, resistance dissipating energy as heat

### 42. Kirchhoff's Current Law (Node)
- **Domain:** Circuit Analysis | **Color:** `#3498DB` | **Shape:** Central dot with inward/outward arrows
- **Idle:** Spheres flow in and out maintaining perfect balance
- **Click:** All spheres converge on node, flash, explode outward symmetrically
- **Physics:** Conservation of charge (ΣI = 0)

### 43. Kirchhoff's Voltage Law (Loop)
- **Domain:** Circuit Analysis | **Color:** `#9B59B6` | **Shape:** Closed rectangular loop with circulating arrow
- **Idle:** Glowing segment travels endlessly around the loop
- **Click:** Loop shrinks inward to a zero-potential point, vanishes
- **Physics:** Conservation of energy in closed circuit (ΣV = 0)

### 44. Faraday's Law of Induction
- **Domain:** Electromagnetics | **Color:** `#E74C3C` | **Shape:** Helical coil on vertical axis
- **Idle:** Ghostly field lines pass through coil, sparks of induced current
- **Click:** Massive flux spike; blinding flash, coil launches off-screen like railgun
- **Physics:** ε = −dΦ_B/dt

### 45. Gauss's Law for Electricity
- **Domain:** Electromagnetics | **Color:** `#E67E22` | **Shape:** Positive charge sphere with outward vectors
- **Idle:** Outward vectors pulse representing constant electric flux
- **Click:** Vectors stretch to infinity; central charge dissolves as field collapses
- **Physics:** ∮ E·dA = Q/ε₀

### 46. Gauss's Law for Magnetism
- **Domain:** Electromagnetics | **Color:** `#2ECC71` | **Shape:** Bar magnet with looping field lines
- **Idle:** Field lines loop continuously N→S
- **Click:** Magnet snaps in half; two smaller loop systems form, shrink, fade (no monopoles)
- **Physics:** ∮ B·dA = 0

### 47. Ampere's Law
- **Domain:** Electromagnetics | **Color:** `#1ABC9C` | **Shape:** Vertical wire encircled by concentric ring
- **Idle:** Current flows up; magnetic ring rotates around wire
- **Click:** Current stops; ring expands outward like ripple, fades off-screen
- **Physics:** ∮ B·dl = μ₀I

### 48. Maxwell-Ampere Displacement Current
- **Domain:** Electromagnetics | **Color:** `#34495E` | **Shape:** Two parallel capacitor plates with gap
- **Idle:** Virtual current bridges gap; magnetic loops swirl around
- **Click:** Spark arcs across plates, structure vaporizes
- **Physics:** Changing electric flux acts as current producing B-field

### 49. Transformer
- **Domain:** Power Systems | **Color:** `#8E44AD` | **Shape:** Two coils sharing magnetic core
- **Idle:** Glowing pulses transfer through core at different intensities
- **Click:** Primary absorbs all energy; secondary shatters into sparks
- **Physics:** Electromagnetic induction for voltage step-up/step-down

### 50. AC Generator (Alternator)
- **Domain:** Power Systems | **Color:** `#D35400` | **Shape:** Rotating wire loop between magnet poles
- **Idle:** Loop rotates, emitting pulsating sine wave of light
- **Click:** Frequency goes infinite; blurs into disk of light, vanishes
- **Physics:** Mechanical → alternating electrical energy conversion

### 51. DC Motor
- **Domain:** Power Systems | **Color:** `#C0392B` | **Shape:** Rotor with split-ring commutator
- **Idle:** Sparks fly off commutator brushes as rotor spins
- **Click:** Back-EMF surge; rotor reverses violently, unwinds into straight wire
- **Physics:** Lorentz force on current-carrying conductors

### 52. Three-Phase Power
- **Domain:** Power Systems | **Color:** `#F1C40F` | **Shape:** Three interlocked 120°-shifted sine waves
- **Idle:** Three waves undulate perfectly out of phase
- **Click:** Waves align in-phase (zero sequence); massive constructive spike shatters screen
- **Physics:** Polyphase AC for constant power delivery

### 53. Transmission Line
- **Domain:** Power Systems | **Color:** `#7F8C8D` | **Shape:** Two parallel lines with distributed L and C
- **Idle:** Traveling wave pulse bounces back and forth
- **Click:** Open circuit reflection; wave doubles amplitude, blows out entire line in sparks
- **Physics:** Distributed parameter model, Z₀ = √(L/C)

### 54. High Voltage Corona Discharge
- **Domain:** Power Systems | **Color:** `#8E44AD` | **Shape:** Sharp needle emitting fractal tendrils
- **Idle:** Purple St. Elmo's fire flickers around sharp tip
- **Click:** Dielectric breakdown; huge lightning arc strikes screen edge, needle vanishes
- **Physics:** Ionization of fluid around high-voltage conductor

### 55. Fourier Transform
- **Domain:** Signal Processing | **Color:** `#16A085` | **Shape:** Time-domain squiggle ↔ frequency spikes
- **Idle:** Time signal morphs back and forth into frequency representation
- **Click:** Spikes spread to infinite bandwidth (Dirac delta); vanish with a pop
- **Physics:** Decomposition of function into constituent frequencies

### 56. Low-Pass Filter
- **Domain:** Signal Processing | **Color:** `#27AE60` | **Shape:** RC circuit with smooth output wave
- **Idle:** High-frequency jitters melt away leaving smooth output
- **Click:** Cutoff drops to zero; output flattens to nothing
- **Physics:** Attenuation of high-frequency components

### 57. High-Pass Filter
- **Domain:** Signal Processing | **Color:** `#2980B9` | **Shape:** CR circuit with spiky output
- **Idle:** Slow variations blocked; only sharp edges pass
- **Click:** Cutoff shoots to infinity; everything blocked, circuit dissolves
- **Physics:** Attenuation of low-frequency (DC) components

### 58. Nyquist-Shannon Sampling
- **Domain:** Signal Processing | **Color:** `#E84393` | **Shape:** Sine wave with discrete stem samples
- **Idle:** Stems slide along sine wave perfectly capturing shape
- **Click:** Rate drops below Nyquist; stems form distorted alias wave, spirals away
- **Physics:** Signal reconstruction (f_s > 2B)

### 59. Negative Feedback Loop
- **Domain:** Control Systems | **Color:** `#2C3E50` | **Shape:** Block diagram with forward + feedback paths
- **Idle:** Signal flows forward; feedback subtracts from input for steady output
- **Click:** Feedback becomes positive; signal amplifies infinitely, blocks explode
- **Physics:** System stabilization and error minimization

### 60. PID Controller
- **Domain:** Control Systems | **Color:** `#F39C12` | **Shape:** Three parallel P/I/D blocks → plant
- **Idle:** Error enters; P scales, I fills, D spikes → perfectly damped output
- **Click:** Derivative goes infinite from noise; erratic oscillations tear model apart
- **Physics:** Proportional-Integral-Derivative feedback mechanism

### 61. Bode Plot
- **Domain:** Control Systems | **Color:** `#8E44AD` | **Shape:** Log magnitude + phase drop curves
- **Idle:** Cursor sweeps frequency axis, highlighting roll-off
- **Click:** Gain margin drops below zero; plot resonates violently, shatters like glass
- **Physics:** Frequency response of LTI systems

### 62. Nyquist Stability Criterion
- **Domain:** Control Systems | **Color:** `#C0392B` | **Shape:** Polar plot contour near (-1,0)
- **Idle:** Point travels continuously along heart-shaped contour
- **Click:** Contour encloses -1 point; spirals outward infinitely (unstable)
- **Physics:** Closed-loop stability from open-loop frequency response

### 63. Power Inverter
- **Domain:** Power Electronics | **Color:** `#1ABC9C` | **Shape:** DC line → block → AC sine wave
- **Idle:** PWM bars pulse inside block to construct smooth AC
- **Click:** PWM frequency drops to zero; harsh DC step burns out block
- **Physics:** DC to AC conversion

### 64. Buck Converter
- **Domain:** Power Electronics | **Color:** `#3498DB` | **Shape:** Switch + diode + inductor + capacitor
- **Idle:** Switch chops voltage; inductor smooths to lower steady output
- **Click:** Switch stuck closed; full voltage fries capacitor in explosion
- **Physics:** DC-to-DC step-down conversion

### 65. Rectifier (Diode Bridge)
- **Domain:** Power Electronics | **Color:** `#9B59B6` | **Shape:** Four diodes in diamond bridge
- **Idle:** AC flows in; alternating diode pairs steer current to one DC direction
- **Click:** Reverse avalanche breakdown; all diodes short, bridge vanishes in smoke
- **Physics:** AC to DC conversion

---

## 4. ELECTRONICS ENGINEERING (20 Models)

### 66. P-N Junction (Depletion Region)
- **Domain:** Semiconductors | **Color:** `#F39C12` | **Shape:** Joined P/N blocks with barrier ions
- **Idle:** Carriers wander near barrier but are repelled by built-in field
- **Click:** Depletion widens under reverse bias until blocks tear apart (Zener breakdown)
- **Physics:** Diffusion/drift currents creating potential barrier

### 67. Diode
- **Domain:** Semiconductors | **Color:** `#E74C3C` | **Shape:** Triangle pointing to vertical bar
- **Idle:** Particles flow through triangle; blocked going backwards
- **Click:** Avalanche breakdown smashes particles through bar, shattering symbol
- **Physics:** One-way valve for current

### 68. BJT Transistor (NPN)
- **Domain:** Semiconductors | **Color:** `#3498DB` | **Shape:** Vertical line + base wire + collector/emitter arrows
- **Idle:** Tiny base trickle controls massive collector-emitter waterfall
- **Click:** Deep saturation overheating; transistor melts into silicon slag
- **Physics:** Current-controlled current source, minority carrier injection

### 69. MOSFET Transistor
- **Domain:** Semiconductors | **Color:** `#2ECC71` | **Shape:** Gate insulated from channel below
- **Idle:** Gate voltage pulls charge carriers to form channel
- **Click:** Gate oxide dielectric breakdown; spark punches through, device destroyed
- **Physics:** Voltage-controlled current source via electric field modulation

### 70. Operational Amplifier
- **Domain:** Analog Electronics | **Color:** `#9B59B6` | **Shape:** Large triangle with +/- inputs and output
- **Idle:** Small input difference multiplied hugely at output
- **Click:** Inputs diverge; output hits supply rails (clipping), triangle shatters
- **Physics:** High-gain differential voltage amplifier

### 71. AND Gate
- **Domain:** Digital Logic | **Color:** `#1ABC9C` | **Shape:** D-shaped logic gate
- **Idle:** Output only lights when both inputs pulse simultaneously
- **Click:** Logic collapses into quantum superposition cloud of 0s/1s, vanishes
- **Physics:** Boolean conjunction via transistor switches

### 72. OR Gate
- **Domain:** Digital Logic | **Color:** `#E67E22` | **Shape:** Curved shield-shaped gate
- **Idle:** Output glows if at least one input active
- **Click:** Gate malfunctions as NOR; rejects all inputs, shrinks into logic-zero black hole
- **Physics:** Boolean disjunction

### 73. NOT Gate (Inverter)
- **Domain:** Digital Logic | **Color:** `#C0392B` | **Shape:** Triangle with bubble at tip
- **Idle:** Continuous color swap: 1→0, 0→1
- **Click:** Input stuck in forbidden zone; inverter oscillates (rings) until disintegrating
- **Physics:** Boolean negation

### 74. XOR Gate
- **Domain:** Digital Logic | **Color:** `#8E44AD` | **Shape:** OR gate with double curved input
- **Idle:** Flashes only when inputs are strictly opposite
- **Click:** Both inputs go high; short-circuits parity, explodes into shower of bits
- **Physics:** Exclusive disjunction (parity generation)

### 75. Flip-Flop (D-Type)
- **Domain:** Digital Logic | **Color:** `#34495E` | **Shape:** Square with D, Q, and clock triangle
- **Idle:** Q holds state until clock pulse transfers D→Q
- **Click:** Metastability — clock and data arrive simultaneously; Q vibrates wildly, evaporates
- **Physics:** Edge-triggered bistable multivibrator

### 76. ADC (Analog-to-Digital)
- **Domain:** Mixed Signal | **Color:** `#16A085` | **Shape:** Staircase steps superimposed on smooth curve
- **Idle:** Continuous wave flows in; blocky binary numbers pop out
- **Click:** Quantization error overtakes signal; staircase turns to static, dissipates
- **Physics:** Sampling and quantization of continuous signals

### 77. DAC (Digital-to-Analog)
- **Domain:** Mixed Signal | **Color:** `#D35400` | **Shape:** R-2R resistor ladder
- **Idle:** Binary switches toggle; voltage levels merge into smooth wave
- **Click:** MSB stuck; massive glitch impulse blasts wave off-screen
- **Physics:** Weighted binary current summation

### 78. PCB Via & Trace
- **Domain:** PCB Design | **Color:** `#27AE60` | **Shape:** Green board with copper trace diving into plated via
- **Idle:** Current races along trace, spirals down via, continues on lower layer
- **Click:** Thermal runaway; via carries too much current, pops off like volcano
- **Physics:** Multi-layer routing, thermal conductivity in FR4

### 79. Dipole Antenna
- **Domain:** RF Engineering | **Color:** `#E84393` | **Shape:** Two collinear rods + toroid radiation pattern
- **Idle:** Oscillating currents generate expanding EM ripples
- **Click:** SWR goes infinite; all power reflects back, antenna vaporizes
- **Physics:** Radiation from accelerating charges

### 80. Waveguide
- **Domain:** RF Engineering | **Color:** `#7F8C8D` | **Shape:** Hollow rectangular metallic tube
- **Idle:** E/H field vectors crisscross down interior (TE10 mode)
- **Click:** Frequency drops below cutoff; waves decay (evanescent), tube crumples
- **Physics:** Boundary conditions guiding microwaves

### 81. Smith Chart (Impedance Matching)
- **Domain:** RF Engineering | **Color:** `#2980B9` | **Shape:** Circular grid of impedance/admittance circles
- **Idle:** Dot spirals inward toward 50Ω center (perfect match)
- **Click:** Dot spirals to edge (pure reactance); standing wave blasts chart apart
- **Physics:** Maximum power transfer, reflection coefficients

### 82. Microcontroller Clock Oscillator
- **Domain:** Embedded Systems | **Color:** `#2C3E50` | **Shape:** IC package with quartz crystal nearby
- **Idle:** Crystal vibrates, sending rhythmic pulses (heartbeats) into IC
- **Click:** Watchdog timer expires; system resets, IC shrinks out of existence
- **Physics:** Piezoelectric effect for precise timing

### 83. Hall Effect Sensor
- **Domain:** Sensors | **Color:** `#8E44AD` | **Shape:** Thin semiconductor slab with magnet passing over
- **Idle:** Electrons pushed sideways creating transverse voltage
- **Click:** Massive field scrambles carriers; chaotic swirl vanishes
- **Physics:** Lorentz force deflecting charge carriers

### 84. VLSI CMOS Inverter
- **Domain:** VLSI Design | **Color:** `#F39C12` | **Shape:** PMOS stacked on NMOS
- **Idle:** Complementary switching: one on = one off, near-zero static power
- **Click:** Both turn on (shoot-through); massive spike melts silicon
- **Physics:** Complementary MOS logic

### 85. Phase-Locked Loop (PLL)
- **Domain:** Electronics / RF | **Color:** `#D35400` | **Shape:** Feedback loop with phase detector + VCO
- **Idle:** Reference and VCO phases align until perfectly locked
- **Click:** Loop loses lock; VCO frequency spins out of control, components fly apart
- **Physics:** Phase synchronization of oscillator with reference

---

## 5. CHEMICAL ENGINEERING (20 Models)

### 86. CSTR (Continuous Stirred-Tank Reactor)
- **Domain:** Process Control | **Color:** `#00CED1` | **Shape:** Cylindrical tank with central impeller
- **Idle:** Impeller rotates generating subtle fluid vortex lines
- **Click:** Fluid mixes to uniform color, drains rapidly in a swirl
- **Physics:** Perfect mixing assumption in steady-state flow reactor

### 87. Plug Flow Reactor (PFR)
- **Domain:** Process Control | **Color:** `#FF8C00` | **Shape:** Horizontal tube with axial concentration gradients
- **Idle:** Colored plugs flow left→right, fading from reactant to product
- **Click:** Entire tube flushes rapidly to the right (high-velocity purge)
- **Physics:** Constant axial flow, no radial mixing

### 88. Distillation Column
- **Domain:** Separation Processes | **Color:** `#4682B4` | **Shape:** Vertical column with stacked equilibrium stages
- **Idle:** Vapor bubbles rise, liquid droplets cascade down
- **Click:** Column separates into discrete trays flying apart by volatility
- **Physics:** Vapor-liquid equilibrium, counter-current mass transfer

### 89. Arrhenius Kinetics (Activation Energy)
- **Domain:** Chemical Reactions | **Color:** `#DC143C` | **Shape:** Potential energy curve with peak barrier
- **Idle:** Particle vibrates at bottom of reactant well, occasionally creeping up
- **Click:** Particle gains energy, leaps over barrier, slides into product well
- **Physics:** Thermal activation to overcome Ea

### 90. Chemical Equilibrium (Le Chatelier)
- **Domain:** Chemical Reactions | **Color:** `#32CD32` | **Shape:** Double-headed arrow (⇌) on fulcrum
- **Idle:** Arrow tips oscillate like balanced scale
- **Click:** Scale violently tips to one side; structure vanishes (shift to products)
- **Physics:** Dynamic equilibrium and stress response

### 91. Heterogeneous Catalysis
- **Domain:** Chemical Reactions | **Color:** `#FFD700` | **Shape:** Solid surface lattice with floating gas molecules
- **Idle:** Molecules adsorb to active sites, break apart, desorb
- **Click:** All sites simultaneously desorb; molecules shoot upward off-screen
- **Physics:** Adsorption → surface reaction → desorption

### 92. Counter-Current Heat Exchanger
- **Domain:** Heat Transfer | **Color:** `#FF4500` / `#1E90FF` | **Shape:** Two parallel pipes, opposite flow arrows
- **Idle:** Heat gradient pulses between hot and cold pipes
- **Click:** Thermal equilibrium reached (both turn purple), fade to zero opacity
- **Physics:** Constant temperature driving force along exchanger length

### 93. Reverse Osmosis Membrane
- **Domain:** Separation Processes | **Color:** `#00FA9A` | **Shape:** Semi-permeable porous barrier
- **Idle:** Solvent molecules drift through pores under pressure; solute bounces off
- **Click:** Pressure breaks membrane; particles mix, structure dissipates in turbulent cloud
- **Physics:** Overcoming osmotic pressure for selective transport

### 94. Cake Filtration
- **Domain:** Separation Processes | **Color:** `#8B4513` | **Shape:** Porous filter mesh accumulating solids
- **Idle:** Particles pack onto growing cake; clear filtrate drips below
- **Click:** Backwash pulse blows entire cake off-screen in scattered debris
- **Physics:** Pressure drop through porous medium

### 95. Polymerization (Chain Growth)
- **Domain:** Polymer Engineering | **Color:** `#9370DB` | **Shape:** Growing chain of interlocking hexagonal monomers
- **Idle:** Free monomers snap onto active chain end
- **Click:** Chain terminated; polymer coils into random walk sphere, shrinks away
- **Physics:** Radical chain-growth kinetics

### 96. Viscoelasticity (Maxwell Model)
- **Domain:** Rheology | **Color:** `#FF1493` | **Shape:** Spring + dashpot in series
- **Idle:** Sinusoidal tension/compression showing spring response and dashpot drift
- **Click:** Massive step-strain; spring snaps, dashpot fluid leaks away
- **Physics:** Stress relaxation in viscous-elastic materials

### 97. Phase Diagram (Triple Point)
- **Domain:** Thermodynamics | **Color:** `#BA55D3` | **Shape:** Y-shaped phase boundary (P vs T)
- **Idle:** State point orbits triple point, background shifts solid/liquid/gas
- **Click:** State rockets past critical point; boundaries blur into supercritical haze
- **Physics:** Three-phase coexistence in thermodynamic equilibrium

### 98. Galvanic Cell
- **Domain:** Electrochemistry | **Color:** `#DAA520` | **Shape:** Two electrodes + salt bridge + wire
- **Idle:** Electrons pulse along wire; ions migrate through salt bridge
- **Click:** Anode completely dissolves; circuit breaks with localized spark
- **Physics:** Spontaneous redox reactions generating current

### 99. Pitting Corrosion
- **Domain:** Corrosion | **Color:** `#A0522D` | **Shape:** Metal surface with deep localized crater
- **Idle:** Anodic dissolution deepens pit; rust ions diffuse out
- **Click:** Stress concentration fractures metal plane into two falling pieces
- **Physics:** Localized passivation breakdown

### 100. Fluidized Bed Reactor
- **Domain:** Process Control | **Color:** `#F4A460` | **Shape:** Vertical column with suspended particles
- **Idle:** Upward gas keeps particles levitated in bubbling state
- **Click:** Gas flow cuts off; all particles drop and pack tightly under gravity
- **Physics:** Drag balancing gravitational force on granular particles

### 101. Fermentation (Microbial Growth)
- **Domain:** Biochemical Engineering | **Color:** `#FFE4B5` | **Shape:** Budding yeast cell in nutrient droplet
- **Idle:** Cell pulsates; daughter cell buds and detaches
- **Click:** Substrate depleted; cell shrinks to dormant spore, descends off-screen
- **Physics:** Monod kinetics, exponential growth

### 102. Enzyme Kinetics (Michaelis-Menten)
- **Domain:** Biochemical Engineering | **Color:** `#8A2BE2` | **Shape:** Enzyme with active site matching substrate
- **Idle:** Enzyme binds substrate, conformational change, releases products
- **Click:** Competitive inhibitor blocks active site; enzyme shatters into amino acids
- **Physics:** Saturation kinetics, enzyme-substrate complex

### 103. Fick's Law of Diffusion
- **Domain:** Transport Phenomena | **Color:** `#00BFFF` | **Shape:** High-concentration cluster dispersing
- **Idle:** Particles undergo Brownian motion, expanding cluster
- **Click:** Gradient flattens instantly; particles scatter evenly across screen, fade
- **Physics:** Molecular diffusion driven by concentration gradient

### 104. Langmuir Adsorption Isotherm
- **Domain:** Separation Processes | **Color:** `#40E0D0` | **Shape:** Grid of binding sites
- **Idle:** Molecules bind/release maintaining fractional coverage equilibrium
- **Click:** Total saturation; monolayer flashes, surface desorbs at once, clears screen
- **Physics:** Monolayer surface adsorption

### 105. Chromatography
- **Domain:** Separation Processes | **Color:** `#C71585` | **Shape:** Column with stationary phase matrix
- **Idle:** Mixed band enters top; separates into distinct bands at different speeds
- **Click:** Bands elute into separate vials; column flushes clean
- **Physics:** Differential partitioning between mobile and stationary phases

---

## 6. NUCLEAR ENGINEERING (15 Models)

### 106. Nuclear Fission (U-235)
- **Domain:** Reactor Physics | **Color:** `#FF00FF` | **Shape:** Oscillating liquid-drop nucleus
- **Idle:** Nucleus wobbles, electrostatic vs. strong force
- **Click:** Slow neutron strikes; nucleus splits into two fragments + three neutrons flying off
- **Physics:** Liquid drop model of induced fission

### 107. Chain Reaction (Criticality)
- **Domain:** Reactor Physics | **Color:** `#FFD700` | **Shape:** Branching tree of neutron paths
- **Idle:** One neutron → two → four; tree pulses at k=1 (critical)
- **Click:** k>1 (supercritical); branching exponentially fills screen in blinding flash
- **Physics:** Neutron multiplication factor

### 108. Nuclear Fusion (D-T Reaction)
- **Domain:** Fusion | **Color:** `#00FFFF` | **Shape:** Two small nuclei approaching each other
- **Idle:** Orbit common center of mass, vibrating against Coulomb barrier
- **Click:** Collide and merge; massive energy burst + high-speed neutron flies off
- **Physics:** Overcoming Coulomb barrier via strong force

### 109. Plasma Confinement (Tokamak)
- **Domain:** Fusion | **Color:** `#8A2BE2` | **Shape:** Toroidal magnetic field cage
- **Idle:** Plasma particles spiral along helical field lines around torus
- **Click:** Disruption — confinement breaks, plasma strikes wall, dissipates
- **Physics:** Lorentz force, Lawson criterion

### 110. Alpha Decay
- **Domain:** Radioactive Decay | **Color:** `#FF4500` | **Shape:** Heavy nucleus ejecting 4He cluster
- **Idle:** Alpha particle tunnels back and forth within nuclear potential well
- **Click:** Alpha escapes; shoots off in straight line, recoil nucleus drifts opposite
- **Physics:** Quantum tunneling, conservation of momentum

### 111. Beta Decay
- **Domain:** Radioactive Decay | **Color:** `#32CD32` | **Shape:** Neutron transforming into proton
- **Idle:** Nucleon fluctuates state via virtual W boson
- **Click:** Commits to transformation; electron + antineutrino ejected in opposite directions
- **Physics:** Weak nuclear force, quark flavor change

### 112. Gamma Emission
- **Domain:** Radioactive Decay | **Color:** `#FFFF00` | **Shape:** Excited nucleus with star glow
- **Idle:** Nucleus vibrates rapidly, shedding EM ripples
- **Click:** Relaxes to ground state; energetic sine wave photon travels off-screen at c
- **Physics:** Isomeric transition from excited nuclear state

### 113. Neutron Moderation
- **Domain:** Reactor Physics | **Color:** `#1E90FF` | **Shape:** Fast neutron bouncing among lattice nuclei
- **Idle:** Neutron scatters off light nuclei, losing energy each collision
- **Click:** Reaches thermal energy (turns red); absorbed by U-235, triggers fission flash
- **Physics:** Elastic scattering kinematics to thermalize neutrons

### 114. Control Rods
- **Domain:** Reactor Physics | **Color:** `#708090` | **Shape:** Vertical rods sliding into reactor core
- **Idle:** Rods move up/down absorbing neutrons to maintain k=1
- **Click:** SCRAM! Rods drop by gravity, absorb all neutrons, screen blacks out
- **Physics:** Strong neutron absorption (B, Cd) controlling reactivity

### 115. Half-Life (Decay Law)
- **Domain:** Radioactive Decay | **Color:** `#ADFF2F` | **Shape:** Cluster of 16 glowing radioactive isotopes
- **Idle:** Isotopes randomly pop into stable dark daughters at statistical rate
- **Click:** Exponential decay curve sweeps screen, all parents → zero instantly
- **Physics:** Statistical probability of spontaneous nuclear decay

### 116. Radiation Shielding
- **Domain:** Radiation Protection | **Color:** `#A9A9A9` | **Shape:** Radiation hitting layered shields (paper/Al/Pb)
- **Idle:** Alpha stops at paper, beta at Al, gamma penetrates deep into lead
- **Click:** Massive gamma flux; shield heats red, absorbs entire beam
- **Physics:** Photoelectric, Compton, pair production interactions

### 117. Gas Centrifuge (Isotope Separation)
- **Domain:** Fuel Cycle | **Color:** `#4B0082` | **Shape:** Rapidly spinning vertical rotor
- **Idle:** Heavy U-238 drifts to outer wall; light U-235 concentrates in center
- **Click:** Rotor halted; centrifugal field collapses, isotopes remix, fade
- **Physics:** Centripetal force radial pressure gradient

### 118. PET (Positron Emission Tomography)
- **Domain:** Nuclear Medicine | **Color:** `#FF1493` | **Shape:** Positron meeting electron
- **Idle:** Spiral toward each other (positronium dance)
- **Click:** Annihilate; two 511 keV gamma rays shoot 180° apart across screen
- **Physics:** Antimatter annihilation, conservation of momentum

### 119. Cyclotron
- **Domain:** Particle Physics | **Color:** `#0000CD` | **Shape:** Two D-shaped electrodes (Dees) + magnetic field
- **Idle:** Charged particle spirals outward, accelerating at each gap crossing
- **Click:** Reaches max radius; shoots tangentially at relativistic speed off-screen
- **Physics:** Lorentz force + alternating E-fields for acceleration

### 120. Bragg Peak (Dosimetry)
- **Domain:** Radiotherapy | **Color:** `#DC143C` | **Shape:** Dose vs depth curve with sharp peak
- **Idle:** Proton travels with low deposition until hitting distinct peak near end of track
- **Click:** Beam targeted at tumor; flashes brightly at Bragg peak, spares tissue beyond
- **Physics:** Stopping power increasing dramatically as velocity drops

---

# PART 2 — COMPUTER, TELECOM, CIVIL, ENVIRONMENTAL, MINING & PETROLEUM

---

## 7. COMPUTER ENGINEERING (20 Models)

### 121. AND Gate (Hardware)
- **Domain:** Logic Gates | **Color:** `#2ECC71` | **Shape:** D-shaped block with two inputs, one output
- **Idle:** Output lights only when both inputs pulse simultaneously
- **Click:** Back edge collapses into front; snaps into bright logic-1 point, vanishes
- **Physics:** TTL — series switches must all close for electron flow

### 122. D Flip-Flop
- **Domain:** Sequential Logic | **Color:** `#F39C12` | **Shape:** Square box with clock triangle
- **Idle:** Internal dot bounces 0↔1 in sync with clock flashes
- **Click:** Box splits into two stable halves shooting up and down
- **Physics:** Bistable multivibrator with positive feedback

### 123. SRAM Cell
- **Domain:** Memory | **Color:** `#9B59B6` | **Shape:** 6-transistor cross-coupled ring
- **Idle:** Electrons chase in infinite loop (retained state)
- **Click:** Loop breaks; dots spiral outward (power loss volatility)
- **Physics:** Cross-coupled inverters maintaining voltage states dynamically

### 124. Full Adder
- **Domain:** ALU Architecture | **Color:** `#3498DB` | **Shape:** Three arrows → Σ block → Sum + Carry
- **Idle:** Carry output glows brighter on overflow
- **Click:** Inputs sum into massive orb cascading right off-screen (carry over)
- **Physics:** Combinational Boolean logic routing voltage thresholds

### 125. Multiplexer (MUX)
- **Domain:** Routing | **Color:** `#E67E22` | **Shape:** Trapezoid (wide input → narrow output)
- **Idle:** Multiple streams push in; selector allows one through
- **Click:** Trapezoid collapses to single wire; unselected streams disintegrate in sparks
- **Physics:** Solid-state switching routing signals by control voltage

### 126. Program Counter
- **Domain:** CPU Registers | **Color:** `#1ABC9C` | **Shape:** Scrolling odometer dial
- **Idle:** Numbers click forward by fixed increment
- **Click:** Counter spins into blur (jump instruction); zips off to new address
- **Physics:** Sequential incrementing logic as spatial pointer in memory

### 127. Instruction Pipeline
- **Domain:** CPU Architecture | **Color:** `#34495E` | **Shape:** Segmented tube (Fetch/Decode/Execute/Writeback)
- **Idle:** Colored packets flow smoothly through stages
- **Click:** Pipeline stalls; packets pile up, tube shatters like glass (flush)
- **Physics:** Concurrent hardware execution paths operating on different phases

### 128. Data Bus
- **Domain:** Bus Systems | **Color:** `#7F8C8D` | **Shape:** Thick parallel metallic traces
- **Idle:** Voltage ripples wash synchronously across all traces
- **Click:** Traces snap like rubber bands (high-Z state); curl off page
- **Physics:** PCB transmission line theory for high-speed propagation

### 129. Phase-Locked Loop (PLL)
- **Domain:** Clock Generation | **Color:** `#E74C3C` | **Shape:** Circular feedback loop with oscillator
- **Idle:** Two waveforms stutter until perfectly phase-locked
- **Click:** Frequency ramps to infinity (loss of lock); straight line vanishes
- **Physics:** VCO continuously matching input phase

### 130. Arithmetic Logic Unit (ALU)
- **Domain:** CPU Processing | **Color:** `#F1C40F` | **Shape:** V-shaped block
- **Idle:** Left/right branches ingest operands; center churns out result
- **Click:** V folds like scissors, slicing data into binary dust
- **Physics:** Complex combinational semiconductor topologies

### 131. Shift Register
- **Domain:** Data Movement | **Color:** `#8E44AD` | **Shape:** Linear array of connected flip-flop squares
- **Idle:** Glowing bit enters left; shifts one box right per clock tick
- **Click:** Register tilts; all bits cascade out right side off-screen
- **Physics:** Cascaded bistable circuits transferring charge on clock edges

### 132. Cache Controller
- **Domain:** Memory Hierarchy | **Color:** `#D35400` | **Shape:** Layered pyramid (L1/L2/L3)
- **Idle:** Data bounces rapidly in L1 tip; slower waves reach L2/L3
- **Click:** Pyramid inverts and collapses — cache miss sinks into main memory
- **Physics:** Locality of reference, SRAM vs DRAM RC delays

### 133. DMA Controller
- **Domain:** I/O Interfaces | **Color:** `#16A085` | **Shape:** Bypass bridge arching over CPU
- **Idle:** Heavy data packets flow over bridge, bypassing idle CPU
- **Click:** Bridge drops into memory like stone, rippling the page
- **Physics:** Hardware taking direct control of memory bus

### 134. CMOS FET
- **Domain:** Hardware Description | **Color:** `#BDC3C7` | **Shape:** 3-terminal gate structure
- **Idle:** Gate pulse forms glowing channel between source and drain
- **Click:** Channel pinches off (saturation); spark, transistor vanishes
- **Physics:** Electric field modulating semiconductor conductivity

### 135. FPGA LUT (Look-Up Table)
- **Domain:** FPGA | **Color:** `#2980B9` | **Shape:** Grid matrix with programmable intersections
- **Idle:** Intersection nodes re-wire; light path changes through grid
- **Click:** Grid dissolves into flurry of 1s/0s as bitstream wipes
- **Physics:** SRAM-based MUXes routing by stored truth table

### 136. Network on Chip (NoC)
- **Domain:** SoC | **Color:** `#C0392B` | **Shape:** 2D mesh of routers and cores
- **Idle:** Flits navigate intersections in XY-routing at 90° turns
- **Click:** Mesh stretches infinitely; links break from tension
- **Physics:** Packet-switched on-chip micro-routers overcoming RC delays

### 137. UART
- **Domain:** Serial I/O | **Color:** `#8E44AD` | **Shape:** Two funnels (parallel↔serial)
- **Idle:** 8 parallel bits compress into single line, march at baud rate
- **Click:** Framing error; bits lose sync, crash, explode into noise
- **Physics:** Asynchronous shift registers with independent matched clocks

### 138. Interrupt Controller
- **Domain:** CPU Architecture | **Color:** `#E67E22` | **Shape:** Priority queue pyramid with exclamation mark
- **Idle:** Low-priority waits at bottom; high-priority flashes at top
- **Click:** NMI spikes through entire pyramid, shattering it to seize control
- **Physics:** Hardware arbitration asserting CPU pin to alter PC state machine

### 139. Watchdog Timer
- **Domain:** System Reliability | **Color:** `#C0392B` | **Shape:** Ticking analog timer with reset arm
- **Idle:** Timer ticks near zero; arm kicks it back repeatedly
- **Click:** Arm misses; timer hits zero — page-wide reboot flash of white
- **Physics:** Independent hardware counter driving hard reset if unserviced

### 140. H-Bridge
- **Domain:** Actuator Control | **Color:** `#27AE60` | **Shape:** Four switches in H around motor
- **Idle:** Diagonal pairs close alternately, reversing current/motor direction
- **Click:** Shoot-through — both sides close; short-circuit puff of smoke
- **Physics:** Power electronics directing high current through inductive loads

---

## 8. COMPUTER SCIENCE (20 Models)

### 141. Binary Search Tree
- **Domain:** Data Structures | **Color:** `#2ECC71` | **Shape:** Hierarchical branching tree
- **Idle:** Search probe trickles down, choosing left/right at each node
- **Click:** Tree balances into flat line, snaps out of existence
- **Physics:** Logarithmic traversal minimizing time complexity

### 142. Hash Table
- **Domain:** Data Structures | **Color:** `#9B59B6` | **Shape:** Grid of buckets with hash funnel
- **Idle:** Data falls through funnel into evenly distributed buckets
- **Click:** Massive collision; all items cram one bucket until it bursts
- **Physics:** Constant-time addressing via modulo arithmetic

### 143. Neural Network Perceptron
- **Domain:** AI/ML | **Color:** `#3498DB` | **Shape:** Central neuron with weighted input dendrites
- **Idle:** Inputs pulse at different intensities; node fires when threshold exceeded
- **Click:** Weights explode to infinity (exploding gradient); blinding white star fades
- **Physics:** Mathematical modeling of biological action potentials

### 144. Gradient Descent
- **Domain:** AI/ML | **Color:** `#E74C3C` | **Shape:** 3D topographic bowl with rolling ball
- **Idle:** Ball rolls down slopes seeking lowest point
- **Click:** Learning rate too high; ball overshoots, ricochets into orbit, disappears
- **Physics:** Moving in negative direction of local gradient

### 145. Quicksort
- **Domain:** Algorithms | **Color:** `#F1C40F` | **Shape:** Unsorted bars with highlighted pivot
- **Idle:** Bars swap places, clustering smaller left / larger right of pivot
- **Click:** Array divides recursively; single bars drop like rain
- **Physics:** Divide-and-conquer: partitioning chaos into ordered states

### 146. Dijkstra's Algorithm
- **Domain:** Graph Traversal | **Color:** `#1ABC9C` | **Shape:** Web of weighted-edge nodes
- **Idle:** Light wavefront expands from source, favoring cheapest edges
- **Click:** Shortest path illuminates blindingly; unselected paths wither to dust
- **Physics:** Greedy optimization like light seeking path of least resistance

### 147. Turing Machine
- **Domain:** Theory of Computation | **Color:** `#7F8C8D` | **Shape:** Infinite tape + read/write head
- **Idle:** Tape shuttles left/right; head clicks to read/write symbols
- **Click:** Halting Problem — locks up, catches fire, burns tape to ash
- **Physics:** Fundamental limit of discrete state machines

### 148. RSA Encryption
- **Domain:** Cryptography | **Color:** `#34495E` | **Shape:** Two interlocking keys (Public + Private)
- **Idle:** Message enters lock (public key → static); private key decrypts
- **Click:** Keys attempt prime factorization; shatter into prime fragments
- **Physics:** Computational intractability of prime factorization

### 149. SHA-256 Hashing
- **Domain:** Cryptography | **Color:** `#D35400` | **Shape:** Heavy metallic meat-grinder funnel
- **Idle:** Recognizable shapes enter; uniform chaotic blocks drop out
- **Click:** Avalanche effect — single bit flip causes entire output to explode
- **Physics:** Cryptographic diffusion and confusion

### 150. MapReduce
- **Domain:** Distributed Systems | **Color:** `#2980B9` | **Shape:** Block → many gears (Map) → single press (Reduce)
- **Idle:** Data scatters among parallel gears, squishes together at press
- **Click:** Straggler fails; system halts, vacuums data backward, blinks out
- **Physics:** Parallel processing overcoming single-machine bottlenecks

### 151. Paxos/Raft Consensus
- **Domain:** Distributed Systems | **Color:** `#8E44AD` | **Shape:** Three server nodes in triangle
- **Idle:** Heartbeat tokens pass continuously; one wears faint crown (Leader)
- **Click:** Network partition (jagged cut); nodes fail quorum, vanish into split-brain
- **Physics:** Fault-tolerant replication in unreliable async networks

### 152. B-Tree
- **Domain:** Databases | **Color:** `#27AE60` | **Shape:** Wide shallow tree with multi-key nodes
- **Idle:** Nodes split/merge horizontally as data falls in, maintaining balance
- **Click:** Root split forces tree upward violently, breaking page boundary
- **Physics:** Optimizing disk I/O via contiguous block reads

### 153. Abstract Syntax Tree (AST)
- **Domain:** Compiler Design | **Color:** `#E67E22` | **Shape:** Tree with operator branches and operand leaves
- **Idle:** Code parses top→bottom, operators light up during evaluation
- **Click:** Syntax error; tree unwinds into raw text strings falling to bottom
- **Physics:** Linguistic parsing to machine-level structural logic

### 154. Round-Robin Scheduler
- **Domain:** Operating Systems | **Color:** `#16A085` | **Shape:** Spinning carousel of process blocks
- **Idle:** CPU light illuminates each block for equal time quantum
- **Click:** Context switching overhead; wheel spins into torus, flies away
- **Physics:** Time-division multiplexing of single CPU core

### 155. Semaphore
- **Domain:** Operating Systems | **Color:** `#C0392B` | **Shape:** Railway signal arm guarding resource gate
- **Idle:** Arm drops to block; one thread uses resource; arm raises for next
- **Click:** Deadlock — two threads grab opposite ends, freeze gray
- **Physics:** Atomic hardware instructions preventing race conditions

### 156. Markov Chain
- **Domain:** AI/ML | **Color:** `#F39C12` | **Shape:** Bubbles connected by probability arrows
- **Idle:** Token jumps randomly between states, favoring thicker arrows
- **Click:** Token enters absorbing state (black hole); sucked in, graph collapses
- **Physics:** Stochastic memoryless processes

### 157. Bloom Filter
- **Domain:** Data Structures | **Color:** `#3498DB` | **Shape:** Bit array with intersecting hash functions
- **Idle:** Data lights specific overlapping bits ("possibly in" vs "definitely not")
- **Click:** False positive saturation; every bit turns on, array shatters
- **Physics:** Space-efficient probabilistic categorization

### 158. Page Table (Virtual Memory)
- **Domain:** Operating Systems | **Color:** `#9B59B6` | **Shape:** Ledger mapping virtual cloud → physical RAM grid
- **Idle:** Virtual addresses snap rigidly to physical block addresses
- **Click:** Page Fault — red flash; data hauled from slow disk
- **Physics:** Hardware MMU translating logical→physical addresses

### 159. Garbage Collector
- **Domain:** Runtimes | **Color:** `#2ECC71` | **Shape:** Sweeping radar over scattered memory nodes
- **Idle:** Radar pings active nodes; orphans dissolve into free space
- **Click:** Stop-The-World; page freezes, swept clean by laser, resumes
- **Physics:** Algorithmic reclamation of unreachable memory circuits

### 160. Dynamic Programming Matrix
- **Domain:** Algorithms | **Color:** `#E74C3C` | **Shape:** 2D grid filling top-left → bottom-right
- **Idle:** Cells light up absorbing combined glow of left+top neighbors
- **Click:** Grid traces optimal path backwards; non-optimal cells drop away
- **Physics:** Storing expensive state changes to avoid redundant recalculation

---

## 9. TELECOMMUNICATIONS (20 Models)

### 161. QAM Constellation
- **Domain:** Modulation | **Color:** `#3498DB` | **Shape:** 16-point I-Q grid
- **Idle:** Signal dot jumps between constellation points (phase + amplitude)
- **Click:** Points blur into Gaussian noise cloud; symbol boundaries lost, static
- **Physics:** Simultaneous amplitude and phase modulation

### 162. Dipole Antenna (Telecom)
- **Domain:** Antennas | **Color:** `#E67E22` | **Shape:** Two horizontal rods + AC source
- **Idle:** Electrons slosh; expanding sinusoidal EM waves radiate outward
- **Click:** Resonance; waves amplify infinitely, antenna glows white-hot, vaporizes
- **Physics:** Oscillating charges producing transverse EM fields

### 163. Phased Array
- **Domain:** Antennas | **Color:** `#9B59B6` | **Shape:** Grid of antenna elements with overlapping ripples
- **Idle:** Constructive interference forms tight beam sweeping like searchlight
- **Click:** Phase delays scramble; destructive interference collapses beam
- **Physics:** Wave interference via precise phase shifting

### 164. Total Internal Reflection (Fiber)
- **Domain:** Fiber Optics | **Color:** `#2ECC71` | **Shape:** Glass core cross-section with cladding
- **Idle:** Laser zig-zags flawlessly down core, bouncing off cladding
- **Click:** Bend radius too tight; light breaks through cladding, bleeds into void
- **Physics:** Snell's Law and critical angle

### 165. OFDM
- **Domain:** Modulation | **Color:** `#F1C40F` | **Shape:** Overlapping sinc-shaped subcarriers
- **Idle:** Each subcarrier peaks at neighbors' nulls, pulsing independently
- **Click:** Doppler shift destroys orthogonality; subcarriers crash, inter-carrier interference
- **Physics:** Frequency-domain orthogonality via FFT

### 166. MIMO
- **Domain:** Wireless | **Color:** `#1ABC9C` | **Shape:** Multiple TX antennas → multipath → multiple RX
- **Idle:** Waves bounce off obstacles, reconstructing at receiver
- **Click:** Environment loses scattering (LOS only); spatial streams collapse to single line
- **Physics:** Multipath propagation and spatial diversity

### 167. Hamming Code
- **Domain:** Coding Theory | **Color:** `#34495E` | **Shape:** Data bits with interspersed parity sentinels
- **Idle:** Bit flips; sentinels glow red, identify location, flip it back
- **Click:** Two bits flip; code can't correct, cascading failure wipes block
- **Physics:** Mathematical redundancy overcoming physical noise floor

### 168. Viterbi Decoder
- **Domain:** Coding Theory | **Color:** `#D35400` | **Shape:** Trellis diagram of nodes over time
- **Idle:** Survivor path weaves through trellis, shedding unlikely paths
- **Click:** Noise overwhelms signal; every path lights equally, trellis explodes
- **Physics:** Maximum likelihood decoding via dynamic programming

### 169. Turbo Code
- **Domain:** Coding Theory | **Color:** `#C0392B` | **Shape:** Two convolutional encoders + interleaver
- **Idle:** Data iterates between decoders, refining confidence each pass
- **Click:** Iterations accelerate to lightspeed, achieve Shannon limit, rocket off-screen
- **Physics:** Iterative soft-decision decoding near theoretical limits

### 170. TCP Sliding Window
- **Domain:** Network Protocols | **Color:** `#16A085` | **Shape:** Linear buffer with bright sliding window
- **Idle:** ACKs arrive; window slides forward to allow new blocks
- **Click:** Congestion; packet drops, window slams to size 1, buffer freezes
- **Physics:** Flow control preventing fast TX from overrunning slow RX

### 171. CSMA/CD
- **Domain:** MAC Layer | **Color:** `#27AE60` | **Shape:** Multiple nodes on shared wire
- **Idle:** Node listens, sends if clear; collision creates red ripple back to both
- **Click:** Collision → exponential backoff; nodes spin in timers, fade
- **Physics:** Voltage collision detection on shared copper

### 172. Wavelength Division Multiplexing (WDM)
- **Domain:** Fiber Optics | **Color:** `#8E44AD` | **Shape:** Prism injecting colored lasers into single fiber
- **Idle:** Red/green/blue interleave and travel simultaneously
- **Click:** Prism shatters; colors separate violently into rainbow spectrum
- **Physics:** EM waves at different frequencies don't interfere in glass

### 173. Shannon Channel Capacity
- **Domain:** Information Theory | **Color:** `#7F8C8D` | **Shape:** Bucket (bandwidth) filling amid noise mud
- **Idle:** C = B log₂(1+S/N) pulsates; noise narrows data pipe
- **Click:** Noise overwhelms signal; capacity→zero, system chokes itself out
- **Physics:** Fundamental thermodynamic limit on error-free data rate

### 174. Spread Spectrum (CDMA)
- **Domain:** Wireless | **Color:** `#E74C3C` | **Shape:** Narrow high-power signal → wide low-power block
- **Idle:** PN code smears signal across bandwidth, hiding below noise floor
- **Click:** Receiver loses chipping code; signal snaps back as visible spike, shatters
- **Physics:** Chipping sequence distributing energy across wide band

### 175. Phase Shift Keying (PSK)
- **Domain:** Modulation | **Color:** `#2980B9` | **Shape:** Sine wave with abrupt phase shifts
- **Idle:** Wave flips 180° at intervals for binary encoding
- **Click:** Phase jitter corrupts wave into flat DC line, vanishes
- **Physics:** Altering carrier phase to encode information

### 176. Yagi-Uda Antenna
- **Domain:** Antennas | **Color:** `#F39C12` | **Shape:** Backbone rod with reflector + directors
- **Idle:** Energy focused forward by directors into directional beam
- **Click:** Directors fall off; beam snaps back to inefficient omnidirectional blob
- **Physics:** Parasitic elements causing directional constructive/destructive interference

### 177. LDPC Code
- **Domain:** Coding Theory | **Color:** `#1ABC9C` | **Shape:** Sparse bipartite graph (variable↔check nodes)
- **Idle:** Probability messages pass back and forth, uncertain→solid bits
- **Click:** Trapping set; nodes oscillate endlessly until explosion
- **Physics:** Belief propagation approaching Shannon limit

### 178. OSPF Routing
- **Domain:** Protocols | **Color:** `#3498DB` | **Shape:** Router topology forming shortest-path tree
- **Idle:** Routers flash LSAs; paths recalculate dynamically
- **Click:** Routing loop; packet bounces infinitely between 3 nodes until TTL=0, vaporizes
- **Physics:** Graph theory optimizing bandwidth/latency metrics

### 179. Eye Diagram
- **Domain:** Signal Integrity | **Color:** `#2ECC71` | **Shape:** Overlapping oscilloscope traces forming "eye"
- **Idle:** Waveforms overlay; eye remains wide open (clean signal)
- **Click:** ISI hits; traces blur, eye violently closes into flat static
- **Physics:** Channel filtering, jitter, and noise on digital pulse trains

### 180. Smith Chart (Telecom)
- **Domain:** RF Matching | **Color:** `#8E44AD` | **Shape:** Circular impedance/reactance grid
- **Idle:** Point traces arc toward 50Ω center
- **Click:** Catastrophic mismatch; point flies to edge, standing wave blows up source
- **Physics:** Complex reflection coefficients solving transmission line equations

---

## 10. CIVIL ENGINEERING (20 Models)

### 181. Simply Supported Beam
- **Domain:** Structural Engineering | **Color:** `#D22B2B` | **Shape:** Horizontal line on triangle + circle supports
- **Idle:** Flexes into parabolic curve, springs back (elastic bending)
- **Click:** Snaps into V-shape (plastic hinge); crumbles into segments falling off-screen
- **Physics:** Euler-Bernoulli beam theory

### 182. Euler Column Buckling (Civil)
- **Domain:** Structural Engineering | **Color:** `#FF8C00` | **Shape:** Thin vertical line pinned at both ends
- **Idle:** Bulges slightly in sine-wave mode shape
- **Click:** Bows to extreme C-shape, snaps in half, top crashes down
- **Physics:** P_cr = π²EI/L²

### 183. Warren Truss Node
- **Domain:** Structural Engineering | **Color:** `#4682B4` | **Shape:** Three diagonal lines meeting at central dot
- **Idle:** Lines pulse inward (compression) / outward (tension)
- **Click:** Central rivet pops; members fly apart along axial vectors
- **Physics:** Method of joints, axial force transfer

### 184. Mohr's Circle (Geotechnical)
- **Domain:** Geotechnical / Solid Mechanics | **Color:** `#800080` | **Shape:** Circle on σ-τ axes with diagonal
- **Idle:** Circle rotates; point traverses circumference shifting stresses
- **Click:** Circle expands to touch Mohr-Coulomb failure envelope; shatters to dust
- **Physics:** 2D stress transformation and failure criterion

### 185. Consolidation Settlement
- **Domain:** Geotechnical Engineering | **Color:** `#8B4513` | **Shape:** Square with dots (grains) and lines (pressure)
- **Idle:** Blue water dots slowly squeeze out as square compresses
- **Click:** Weight drops; water blasts sideways, soil collapses to thin line
- **Physics:** Terzaghi's 1-D consolidation theory

### 186. Retaining Wall Active Earth Pressure
- **Domain:** Geotechnical Engineering | **Color:** `#CD853F` | **Shape:** Vertical block holding back soil wedge
- **Idle:** Wall leans slightly forward; soil wedge shifts down
- **Click:** Wall tips over; soil slides out along 45+φ/2 failure plane
- **Physics:** Rankine active earth pressure

### 187. Slope Stability (Slip Circle)
- **Domain:** Geotechnical Engineering | **Color:** `#6B8E23` | **Shape:** Slope face with dashed semi-circle
- **Idle:** Wedge above dashed line vibrates (imminent slide)
- **Click:** Mass rotates downward like wheel, spreads at base
- **Physics:** Method of slices, circular failure

### 188. Open Channel Flow
- **Domain:** Hydraulics | **Color:** `#1E90FF` | **Shape:** Trapezoidal cross-section with wavy water
- **Idle:** Waves undulate gently (uniform flow)
- **Click:** Turbulent hydraulic jump; water spills over sides, washes off-screen
- **Physics:** Manning's equation, subcritical/supercritical transitions

### 189. Pipe Friction (Darcy-Weisbach)
- **Domain:** Hydraulics | **Color:** `#00CED1` | **Shape:** Horizontal cylinder with flow arrows
- **Idle:** Arrows slower at edges (boundary layer), faster at center
- **Click:** Eddies choke flow until it stops; pipe scales to nothing
- **Physics:** Moody chart, friction loss

### 190. Hydraulic Jump
- **Domain:** Hydraulics | **Color:** `#4169E1` | **Shape:** Thin water line stepping up to turbulent block
- **Idle:** Constant frothy roller at step-up point
- **Click:** Roller expands as bore, sweeping upstream flow off-screen
- **Physics:** Momentum conservation, supercritical→subcritical

### 191. Unit Hydrograph
- **Domain:** Hydrology | **Color:** `#00008B` | **Shape:** Bell curve on x-y axes
- **Idle:** Rainfall bar blinks; bell curve rises and falls in response
- **Click:** Peak stretches infinitely; turns into flood wave washing out axes
- **Physics:** Catchment runoff routing, linear time-invariant systems

### 192. Traffic Shockwave
- **Domain:** Transportation | **Color:** `#DC143C` | **Shape:** Line of dots with dense cluster
- **Idle:** Dense cluster propagates backward as cars move forward
- **Click:** Red X at front; dots pile into dense square, fade out
- **Physics:** LWR kinematic wave theory

### 193. Seismic Base Isolation
- **Domain:** Earthquake Engineering | **Color:** `#FF4500` | **Shape:** Building on three springs
- **Idle:** Ground vibrates rapidly; building glides gently above
- **Click:** Springs snap; building shakes violently, shatters into blocks
- **Physics:** Decoupling from ground motion, period lengthening

### 194. Soil Liquefaction
- **Domain:** Earthquake Engineering | **Color:** `#BDB76B` | **Shape:** Soil particle matrix with interstitial water
- **Idle:** Particles shake; water expands between them
- **Click:** Particles sink; water geyser shoots out top (sand boil)
- **Physics:** Loss of effective stress from cyclic loading

### 195. Concrete Strut-and-Tie
- **Domain:** Structural / Materials | **Color:** `#708090` | **Shape:** Deep beam with compression struts + tension ties
- **Idle:** Struts thicken; ties pull tight
- **Click:** Diagonal shear crack zig-zags; halves slide apart
- **Physics:** Lower-bound plasticity theory

### 196. Steel Yield Surface (Von Mises)
- **Domain:** Materials Engineering | **Color:** `#C0C0C0` | **Shape:** 3D elliptical cylinder in principal stress space
- **Idle:** Red stress dot bounces within cylinder boundary
- **Click:** Dot hits surface; cylinder turns red, deforms to flat disk
- **Physics:** Von Mises distortion energy yield criterion

### 197. Arch Thrust Line
- **Domain:** Structural Engineering | **Color:** `#A0522D` | **Shape:** Masonry arch with internal parabolic curve
- **Idle:** Thrust line dances but stays in middle third
- **Click:** Thrust line exits blocks; hinges form, arch collapses to rubble
- **Physics:** Funicular polygons, masonry stability

### 198. Surveying Theodolite
- **Domain:** Geodesy | **Color:** `#FFD700` | **Shape:** Tripod with scope emitting laser lines to targets
- **Idle:** Lines sweep like radar, locking onto targets
- **Click:** Lines form triangle; zooms into topographic contour map
- **Physics:** Trigonometric leveling and resection

### 199. Pavement Stress Bulb
- **Domain:** Transportation | **Color:** `#696969` | **Shape:** Point load with expanding contours below
- **Idle:** Wheel rolls over; stress bulbs pulse downward
- **Click:** Excessive load; deep rut forms, contours shoot off bottom
- **Physics:** Boussinesq elastic half-space distribution

### 200. Cable Catenary
- **Domain:** Structural Engineering | **Color:** `#2F4F4F` | **Shape:** Sagging chain between two pylons
- **Idle:** Chain sways in invisible breeze
- **Click:** Tension→infinite; chain goes taut horizontal, snaps at supports, whips down
- **Physics:** Hyperbolic cosine function under self-weight

---

## 11. ENVIRONMENTAL ENGINEERING (10 Models)

### 201. Sedimentation (Stokes' Law)
- **Domain:** Water Treatment | **Color:** `#48D1CC` | **Shape:** Beaker with settling dots
- **Idle:** Dots drift down at terminal velocity
- **Click:** All dots plunge to bottom (sludge); clear water evaporates
- **Physics:** Settling velocity via viscosity, density, gravity

### 202. Flocculation
- **Domain:** Water Treatment | **Color:** `#8FBC8F` | **Shape:** Scattered particles + slow paddle
- **Idle:** Paddle turns; particles bump and join into larger flocs
- **Click:** Flocs coalesce into one massive particle crashing through screen bottom
- **Physics:** Orthokinetic flocculation, G-value

### 203. Activated Sludge Biofilm
- **Domain:** Wastewater | **Color:** `#556B2F` | **Shape:** Fuzzy microbial cluster on media bead
- **Idle:** Biofilm expands as BOD particles drift in and disappear
- **Click:** Over-thickened biofilm sloughs off in one chunk, washed away
- **Physics:** Monod kinetics, biofilm detachment

### 204. Gaussian Plume (Atmospheric Dispersion)
- **Domain:** Air Pollution | **Color:** `#A9A9A9` | **Shape:** Smokestack emitting cone-shaped cloud
- **Idle:** Plume wavers with turbulent eddies
- **Click:** Inversion layer clamps down; plume dives to ground, page suffocates in fog
- **Physics:** Gaussian dispersion, Pasquill stability classes

### 205. Greenhouse Effect (Radiative Forcing)
- **Domain:** Atmospheric Science | **Color:** `#FF6347` | **Shape:** Earth surface + atmospheric layer with trapped arrows
- **Idle:** Shortwave in; longwave reflects back down (trapped)
- **Click:** Layer thickens, glows red; surface vaporizes, icon burns away
- **Physics:** IR absorption by CO₂, CH₄

### 206. Groundwater Contaminant Plume
- **Domain:** Remediation | **Color:** `#9370DB` | **Shape:** Underground aquifer with expanding colored blob
- **Idle:** Blob translates right (advection) and spreads (dispersion)
- **Click:** Extraction well drops in; plume sucked to point, pulled to surface
- **Physics:** Advection-dispersion equation, pump-and-treat

### 207. Darcy's Law Filtration
- **Domain:** Water Treatment | **Color:** `#F4A460` | **Shape:** Vertical sand column
- **Idle:** Water flows through pores; dirt trapped in top layer
- **Click:** Filter clogs; backwash blasts sand out the top
- **Physics:** Flow through porous media, head loss

### 208. Noise Barrier Attenuation
- **Domain:** Noise Pollution | **Color:** `#BA55D3` | **Shape:** Speaker → expanding arcs → barrier
- **Idle:** Waves hit barrier; reduced amplitude on other side
- **Click:** Barrier removed; massive wave shakes interface elements before vanishing
- **Physics:** Inverse square law, acoustic diffraction

### 209. Carbon Cycle (Mass Balance)
- **Domain:** Sustainability / LCA | **Color:** `#32CD32` | **Shape:** Loop connecting factory → atmosphere → tree
- **Idle:** Carbon dots flow in balanced circle
- **Click:** Tree dies; carbon backs up at atmosphere node until it explodes
- **Physics:** Conservation of mass, biogeochemical cycling

### 210. Reverse Osmosis (Desalination)
- **Domain:** Desalination | **Color:** `#00FFFF` | **Shape:** Dashed barrier + piston forcing water through
- **Idle:** Piston pushes water molecules through; salt ions bounce back
- **Click:** Pressure exceeds burst strength; membrane ruptures, salt mixes across screen
- **Physics:** Osmotic pressure (π = iMRT)

---

## 12. MINING & PETROLEUM ENGINEERING (10 Models)

### 211. Reservoir Flow (Radial Darcy)
- **Domain:** Reservoir Engineering | **Color:** `#8B0000` | **Shape:** Wellbore with converging flow arrows in disc
- **Idle:** Oil dots flow radially inward toward wellbore
- **Click:** Pressure depletes; arrows stop, cone of depression swallows well
- **Physics:** Radial flow, diffusivity equation, drawdown

### 212. Hydraulic Fracturing
- **Domain:** Rock Mechanics | **Color:** `#9932CC` | **Shape:** Horizontal wellbore with vertical zigzag cracks
- **Idle:** Cracks pulse and expand as proppant enters
- **Click:** Pump pressure spikes; fracture propagates across entire screen, splitting page
- **Physics:** Linear elastic fracture mechanics, tensile failure

### 213. Capillary Pressure Curve
- **Domain:** Petrophysics | **Color:** `#20B2AA` | **Shape:** Pore throat with water/oil meniscus
- **Idle:** Meniscus flexes with pressure differential
- **Click:** Oil pressure overcomes entry pressure; meniscus pops, oil flushes pore
- **Physics:** Young-Laplace equation (P_c = 2σcosθ/r)

### 214. Drill Bit Penetration
- **Domain:** Drilling Mechanics | **Color:** `#B8860B` | **Shape:** Rotating tricone bit on jagged rock
- **Idle:** Bit spins; rock chips fly upward in drilling mud
- **Click:** High-pressure kick; bit blown upward by mud geyser (blowout)
- **Physics:** Rate of penetration, weight on bit, rotary friction

### 215. Froth Flotation
- **Domain:** Mineral Processing | **Color:** `#FFD700` | **Shape:** Tank with rising bubbles carrying mineral particles
- **Idle:** Bubbles float up carrying gold dots; gangue drops to bottom
- **Click:** Froth overflows; golden cascade covers UI
- **Physics:** Surface chemistry, hydrophobicity, bubble-particle attachment

### 216. Rock Blasting (Shockwave)
- **Domain:** Blasting Mechanics | **Color:** `#FF0000` | **Shape:** Borehole with explosive + radial cracks
- **Idle:** Burning fuse sparks continuously
- **Click:** Blinding flash; shockwave ring fragments rock into million polygons
- **Physics:** Detonation velocity, compressive shockwaves, tensile spalling

### 217. Subsidence Trough
- **Domain:** Mining Geomechanics | **Color:** `#556B2F` | **Shape:** Underground cavity with sagging surface
- **Idle:** Cavity roof peels; surface bows gently
- **Click:** Roof caves catastrophically; sinkhole pulls surface downward
- **Physics:** Ground relaxation, angle of draw, caving mechanics

### 218. Well Logging (Resistivity)
- **Domain:** Well Logging | **Color:** `#00FA9A` | **Shape:** Logging tool in borehole drawing squiggly graph
- **Idle:** Graph bounces between low (shale) and high (hydrocarbon)
- **Click:** Pure oil zone; resistivity shoots horizontally off-screen, breaking graph
- **Physics:** Archie's Equation, formation fluid conductivity

### 219. Porosity/Permeability Network
- **Domain:** Reservoir Engineering | **Color:** `#D8BFD8` | **Shape:** 3D network of spheres (pores) + tubes (throats)
- **Idle:** Fluid trickles through most direct pathways
- **Click:** Stress crushes spheres flat; fluid ejects sideways, permeability→zero
- **Physics:** Kozeny-Carman equation, tortuosity

### 220. Enhanced Oil Recovery (Waterflood)
- **Domain:** Reservoir Engineering | **Color:** `#1E90FF` | **Shape:** Displacement front (blue water pushing black oil)
- **Idle:** Water pushes oil; viscous fingering spikes begin forming
- **Click:** Water breaks through; stranded oil turns solid unmovable block
- **Physics:** Buckley-Leverett fractional flow, mobility ratio

---

# PART 3 — BIOMEDICAL, AGRICULTURAL, MARINE, MATERIALS, NANO, OPTICS, ACOUSTICS

---
# Micro-Scientific Physics Models Catalog

## 1. BIOMEDICAL ENGINEERING

### 1. BONE COMPRESSION STRESS
- **Domain:** Biomechanics (Stress in Bones)
- **Symbol/Shape:** A vertical trabecular cylinder composed of a honeycomb lattice
- **Color:** #E8DCC4 (Bone White)
- **Idle Animation:** The lattice micro-fractures and heals continuously, gently compressing and expanding by 1-2 pixels vertically.
- **Click Disappearance Motion:** Buckles plastically in the center, snapping horizontally into microscopic rigid fragments that scatter off the bottom of the screen.
- **Physics Basis:** Hooke's Law of elasticity, Young's Modulus, and compressive yield strength of trabecular bone.

### 2. JOINT KINEMATICS PENDULUM
- **Domain:** Biomechanics (Gait Analysis)
- **Symbol/Shape:** A minimalist knee-joint hinge with two connecting vector line segments
- **Color:** #FF5733 (Kinematic Orange)
- **Idle Animation:** Swings rhythmically back and forth in a natural walking cadence, tracing a faint arc.
- **Click Disappearance Motion:** The hinge pin dissolves, causing the two segments to succumb to free-fall gravity, rotating chaotically as they drop off-screen.
- **Physics Basis:** Rotational kinematics, torque, and pendulum dynamics of human locomotion.

### 3. LARMOR PRECESSION SPIN
- **Domain:** Medical Imaging (MRI)
- **Symbol/Shape:** A central sphere (proton) with an arrow pointing upward through its axis
- **Color:** #00C3FF (Magnetic Cyan)
- **Idle Animation:** The arrow precesses (wobbles) in a continuous tight cone, simulating magnetic alignment.
- **Click Disappearance Motion:** A sudden RF pulse strikes; the spin tips exactly 90 degrees into the transverse plane, spirals outward (T2 dephasing), and fades into static noise.
- **Physics Basis:** Nuclear magnetic resonance and Larmor precession frequency.

### 4. X-RAY ATTENUATION BLOCK
- **Domain:** Medical Imaging (X-Ray, CT)
- **Symbol/Shape:** A solid isometric cube with parallel wave lines striking its left face and emerging thinner on the right
- **Color:** #FFFFFF (Radiograph White)
- **Idle Animation:** Photons continuously pass through, visibly losing opacity as they traverse the medium.
- **Click Disappearance Motion:** The cube's density goes to infinity, instantly absorbing all light. The block turns pitch black and collapses into a single dense singularity.
- **Physics Basis:** Beer-Lambert Law and X-ray photon attenuation coefficients.

### 5. ACOUSTIC IMPEDANCE ECHO
- **Domain:** Medical Imaging (Ultrasound)
- **Symbol/Shape:** A curved piezoelectric transducer emitting concentric semicircular sound waves
- **Color:** #4A90E2 (Sonogram Blue)
- **Idle Animation:** Pulses emit downward, bouncing off an invisible horizontal boundary and returning as fainter echoes.
- **Click Disappearance Motion:** The frequency shifts to ultrasonic extreme; the waves shatter the boundary into millions of specular reflection particles that scatter in all directions.
- **Physics Basis:** Acoustic impedance mismatch, reflection, and refraction.

### 6. ACTION POTENTIAL SPIKE
- **Domain:** Neural Engineering (EEG, Brain-Computer Interfaces)
- **Symbol/Shape:** A sharp waveform peak straddling a resting membrane potential line
- **Color:** #FF00FF (Synaptic Magenta)
- **Idle Animation:** The baseline vibrates slightly with thermal noise, occasionally initiating a tiny sub-threshold bump.
- **Click Disappearance Motion:** Depolarizes violently, shooting a massive voltage spike upward that leaves a glowing refractory trail before zipping off the right side of the screen.
- **Physics Basis:** Hodgkin-Huxley model and ion channel electrodynamics.

### 7. HEMODYNAMIC BIFURCATION
- **Domain:** Biofluid Mechanics (Blood Flow)
- **Symbol/Shape:** A Y-shaped vessel junction with internal flow vectors
- **Color:** #D0021B (Arterial Red)
- **Idle Animation:** Vectors pulse rhythmically, simulating a heartbeat, with flow separation (slower vectors) at the outer walls of the branch.
- **Click Disappearance Motion:** Turbulence overtakes the laminar flow; the vectors spin into microscopic vortex streets (Reynold's number exceeds critical limit) and dissolve into fluid chaos.
- **Physics Basis:** Navier-Stokes equations, Womersley flow, and Poiseuille's law.

### 8. FICKIAN DRUG DIFFUSION
- **Domain:** Drug Delivery Systems
- **Symbol/Shape:** A concentrated cluster of dots expanding radially outward through a gradient
- **Color:** #50E3C2 (Pharma Teal)
- **Idle Animation:** The core pulses softly, slowly releasing singular dots that undergo Brownian motion around the periphery.
- **Click Disappearance Motion:** The concentration gradient inverts; all particles rapidly reverse entropy, collapsing back into a single, perfectly dense dot that vanishes.
- **Physics Basis:** Fick's Laws of Diffusion and Brownian motion.

### 9. SCAFFOLD PERCOLATION
- **Domain:** Tissue Engineering (Cell Growth)
- **Symbol/Shape:** A cubic lattice network with expanding spherical nodes (cells) at the intersections
- **Color:** #7ED321 (Bio Green)
- **Idle Animation:** Nodes slowly pulsate and reach out tiny tendrils to connect to adjacent empty lattice points.
- **Click Disappearance Motion:** Rapid cellular apoptosis; the cells rapidly detach, shrink into apoptotic bodies, and the underlying scaffold enzymatically degrades into dust.
- **Physics Basis:** Percolation theory and reaction-diffusion kinetics.

### 10. POSITRON ANNIHILATION
- **Domain:** Medical Imaging (PET)
- **Symbol/Shape:** Two colliding particles (electron and positron) inside a circular detector ring
- **Color:** #F8E71C (Isotope Yellow)
- **Idle Animation:** The particles dance around each other in a decaying orbital spiral.
- **Click Disappearance Motion:** They collide and vanish, emitting two brilliant, perfectly opposed 180-degree gamma ray beams that shoot completely across the web page.
- **Physics Basis:** Conservation of momentum, matter-antimatter annihilation, and E=mc².

### 11. MYOELECTRIC THRESHOLD
- **Domain:** Prosthetics & Implants
- **Symbol/Shape:** A jagged EMG interference pattern feeding into a logic gate
- **Color:** #8B572A (Muscle Bronze)
- **Idle Animation:** The signal crackles constantly below a dotted horizontal threshold line.
- **Click Disappearance Motion:** The signal crosses the threshold; the logic gate snaps open, transforming the jagged wave into a perfectly smooth digital square wave that zooms forward.
- **Physics Basis:** Electromyography, signal processing, and motor unit action potentials.

### 12. DNA TORSION
- **Domain:** Genetic Engineering (CRISPR, DNA)
- **Symbol/Shape:** A twisting double helix with distinct base pair rungs
- **Color:** #9013FE (Genomic Purple)
- **Idle Animation:** The helix rotates continuously, subtly stretching and compressing.
- **Click Disappearance Motion:** A CRISPR guide RNA cuts the strand; supercoiling tension releases instantly, unwinding the helix into two straight, parallel lines that snap like rubber bands off the screen.
- **Physics Basis:** Molecular dynamics, torsional strain, and hydrogen bonding.

### 13. EVANESCENT PLASMON
- **Domain:** Biosensors (Surface Plasmon Resonance)
- **Symbol/Shape:** A metallic gold film with an incident light ray creating a glowing surface wave
- **Color:** #F5A623 (Plasmonic Gold)
- **Idle Animation:** The surface wave ripples smoothly, trapped perfectly at the metal-dielectric interface.
- **Click Disappearance Motion:** Target molecules bind to the surface; the resonance angle shifts drastically, causing the trapped light to bounce directly out into the user's view, blinding the icon away.
- **Physics Basis:** Surface plasmon polaritons and total internal reflection.

### 14. IMPEDANCE OSCILLATOR
- **Domain:** Rehabilitation Engineering (Exoskeletons)
- **Symbol/Shape:** A mass suspended between a coiled spring and a dashpot damper
- **Color:** #4A4A4A (Mechanical Grey)
- **Idle Animation:** The mass bobs in a critically damped, smooth oscillation.
- **Click Disappearance Motion:** Damping goes to zero; the mass enters uncontrolled resonance, oscillating wider and faster until it shatters the spring and flies off-axis.
- **Physics Basis:** Harmonic oscillator dynamics and impedance control.

### 15. CARDIAC DIPOLE
- **Domain:** Biomedical Instrumentation (ECG)
- **Symbol/Shape:** A 3D heart wireframe with a shifting internal electrical vector arrow
- **Color:** #E02020 (Myocardium Red)
- **Idle Animation:** The vector sweeps through the standard PQRST sequence, rotating its angle.
- **Click Disappearance Motion:** Fibrillation sets in; the single dipole fractures into hundreds of chaotic micro-vectors spinning wildly before the baseline goes entirely flat (asystole).
- **Physics Basis:** Cardiac dipole vector theory and volume conductor electric fields.


## 2. AGRICULTURAL ENGINEERING

### 1. CAPILLARY DRIP
- **Domain:** Irrigation (Drip Systems)
- **Symbol/Shape:** A water droplet touching a porous soil cross-section
- **Color:** #007AFF (Water Blue)
- **Idle Animation:** The droplet slowly seeps downward, creating hemispherical moisture expansion rings in the soil.
- **Click Disappearance Motion:** Evapotranspiration hits maximum; the moisture rings violently reverse direction, shooting upward as vapor columns into the page.
- **Physics Basis:** Darcy's Law, capillary action, and fluid dynamics in porous media.

### 2. SOIL CONSOLIDATION
- **Domain:** Soil Mechanics for Agriculture
- **Symbol/Shape:** An aggregate matrix of soil grains with water trapped between them
- **Color:** #8B4513 (Loam Brown)
- **Idle Animation:** A subtle downward pressure applies, pushing a tiny amount of pore water out of the top.
- **Click Disappearance Motion:** Sudden liquefaction; the effective stress hits zero, the soil grains lose all contact friction, and the matrix collapses into a fluid mudslide off the bottom of the screen.
- **Physics Basis:** Terzaghi's principle of effective stress and soil consolidation.

### 3. PSYCHROMETRIC EVAPORATION
- **Domain:** Crop Processing (Drying)
- **Symbol/Shape:** A spherical grain kernel emitting wavy vapor lines
- **Color:** #F5C200 (Harvest Yellow)
- **Idle Animation:** Heat arrows point in, and vapor lines drift out, slowly shrinking the grain's blue water core.
- **Click Disappearance Motion:** Flash-drying occurs; the kernel rapidly expands from internal steam pressure and pops like popcorn, scattering starchy fragments.
- **Physics Basis:** Psychrometrics, heat and mass transfer, and latent heat of vaporization.

### 4. PHOTOSYNTHETIC EXCITATION
- **Domain:** Biosystems (Photosynthesis)
- **Symbol/Shape:** A chloroplast disc struck by a wavy photon ray, emitting an electron
- **Color:** #27AE60 (Chlorophyll Green)
- **Idle Animation:** Photons rhythmically strike, pulsing a glowing electron down a transport chain curve.
- **Click Disappearance Motion:** Photoinhibition overload; too many photons strike at once, causing the reaction center to burst in a flare of dissipated heat and fluorescence, leaving nothing behind.
- **Physics Basis:** Quantum optics, resonance energy transfer, and the photoelectric effect.

### 5. TRILATERATION FIX
- **Domain:** Precision Agriculture (GPS)
- **Symbol/Shape:** Three intersecting spherical transmission ranges
- **Color:** #9B9B9B (Satellite Silver)
- **Idle Animation:** The three spheres pulse outward like radio waves, perfectly intersecting at a blinking central coordinate.
- **Click Disappearance Motion:** Signal spoofing/multipath error; the spheres decouple and wildly drift apart, dropping the coordinate point endlessly into the void.
- **Physics Basis:** Trilateration, signal propagation, and relativistic time dilation correction.

### 6. RADIATIVE TRAPPING
- **Domain:** Greenhouse Climate Control
- **Symbol/Shape:** A transparent dome with short-wave arrows entering and long-wave arrows trapped inside
- **Color:** #B8E986 (Glasshouse Mint)
- **Idle Animation:** High-frequency waves enter easily, convert to low-frequency red waves, and bounce off the interior roof.
- **Click Disappearance Motion:** Thermal runaway; the internal trapped waves multiply exponentially, turning bright red until the glass dome shatters outward from the simulated heat pressure.
- **Physics Basis:** Blackbody radiation, Wien's displacement law, and the greenhouse effect.

### 7. PROJECTILE DRAG
- **Domain:** Irrigation (Sprinkler Systems)
- **Symbol/Shape:** A parabolic trajectory arc of water droplets
- **Color:** #5AC8FA (Aero Blue)
- **Idle Animation:** Droplets continuously follow the arc, subtly flattening at the top due to air resistance.
- **Click Disappearance Motion:** A simulated hurricane-force crosswind shears across the screen, instantly blowing the entire parabolic stream horizontally into mist.
- **Physics Basis:** Kinematics, projectile motion, and aerodynamic drag.

### 8. FRACTURE COMMINUTION
- **Domain:** Crop Processing (Milling)
- **Symbol/Shape:** A solid crystalline seed caught between two grinding rollers
- **Color:** #D8D8D8 (Millstone Grey)
- **Idle Animation:** The rollers turn slowly, propagating tiny, glowing stress fractures through the seed.
- **Click Disappearance Motion:** Critical shear is reached; the seed shatters perfectly along its cleavage planes into mathematically precise microscopic dust particles.
- **Physics Basis:** Fracture mechanics, Rittinger's Law, and Kick's Law.

### 9. GAS SOLUBILIZATION
- **Domain:** Aquaculture Systems
- **Symbol/Shape:** An aeration bubbler emitting oxygen spheres into a column of water
- **Color:** #E0F2FE (Oxygenated Cyan)
- **Idle Animation:** Bubbles rise; as they rise, they visibly shrink, dissolving into the surrounding fluid medium.
- **Click Disappearance Motion:** Depressurization (the bends); the dissolved oxygen violently comes out of solution, filling the entire icon with a massive frothing boil that evaporates.
- **Physics Basis:** Henry's Law of gas solubility and mass transfer kinetics.

### 10. SOIL SHEAR DRAFT
- **Domain:** Agricultural Machinery (Tractor Implements)
- **Symbol/Shape:** A metallic tillage tine slicing horizontally through a layered soil block
- **Color:** #4A4A4A (Implement Steel)
- **Idle Animation:** The tine moves steadily, creating a permanent shear plane and bulging the soil upward ahead of it.
- **Click Disappearance Motion:** The draft force overcomes the implement yield strength; the tine violently shears off and flips end-over-end off the screen, leaving a perfectly un-tilled soil block.
- **Physics Basis:** Coulomb's earth pressure theory, shear stress, and draft force dynamics.


## 3. MARINE/OCEAN ENGINEERING

### 1. ARCHIMEDES BUOYANCY
- **Domain:** Naval Architecture (Hull Design)
- **Symbol/Shape:** A cross-section of a ship's hull partially submerged in fluid
- **Color:** #003366 (Deep Navy)
- **Idle Animation:** The hull bobs gently, perfectly balancing the displaced fluid volume (shown as upward buoyant arrows) against gravity (downward arrow).
- **Click Disappearance Motion:** The density of the hull suddenly multiplies; it drops like a stone, displacing a massive splash of vector particles up across the page before sinking out of sight.
- **Physics Basis:** Archimedes' Principle and hydrostatic equilibrium.

### 2. METACENTRIC TORQUE
- **Domain:** Naval Architecture (Stability)
- **Symbol/Shape:** A tilted ship cross-section showing the Center of Gravity (G) and Center of Buoyancy (B)
- **Color:** #F5A623 (Warning Amber)
- **Idle Animation:** The ship oscillates slightly, with the buoyancy vector shifting outward to create a righting lever (GZ) that pushes it back upright.
- **Click Disappearance Motion:** The Center of Gravity is artificially shifted too high (negative metacentric height); the righting lever flips, and the ship capsizes in a rapid 180-degree barrel roll.
- **Physics Basis:** Metacentric height (GM), statics, and torque.

### 3. ORBITAL WAVE KINEMATICS
- **Domain:** Ocean Currents & Waves
- **Symbol/Shape:** A surface wave sine curve with circular particle orbits beneath it
- **Color:** #00BFFF (Deep Sky Blue)
- **Idle Animation:** The wave translates forward, while the particles beneath roll in continuous circles that decrease in radius with depth.
- **Click Disappearance Motion:** The wave enters shallow water; the circular orbits crush into extreme ellipses until the wave steepens past 1:7 steepness, breaking violently and crashing off-screen.
- **Physics Basis:** Airy linear wave theory, potential flow, and shoaling.

### 4. ACOUSTIC SPREADING
- **Domain:** Underwater Acoustics (Sonar)
- **Symbol/Shape:** A submerged pinging source radiating expanding spherical acoustic pressure fronts
- **Color:** #7ED321 (Sonar Green)
- **Idle Animation:** Wavefronts expand and slowly fade in intensity, demonstrating spherical spreading loss.
- **Click Disappearance Motion:** An extreme thermocline (temperature inversion) forms; the sound waves violently refract downward, bending sharply into the abyss and silencing the ping.
- **Physics Basis:** The acoustic wave equation, geometric spreading, and Snell's Law of refraction.

### 5. PROPELLER CAVITATION
- **Domain:** Marine Propulsion
- **Symbol/Shape:** A spinning hydrofoil cross-section generating trailing vapor bubbles
- **Color:** #9B9B9B (Alloy Silver)
- **Idle Animation:** As the foil spins, low-pressure zones on the trailing edge flash into tiny bubbles that immediately collapse.
- **Click Disappearance Motion:** The RPM spikes to infinity; local pressure drops instantly to zero. A massive cavitation bubble engulfs the propeller, violently imploding and destroying the foil in a shockwave.
- **Physics Basis:** Bernoulli's principle, fluid dynamics, and vapor pressure.

### 6. KINETIC EXTRACTION
- **Domain:** Tidal Energy
- **Symbol/Shape:** A horizontal-axis tidal turbine submerged in bidirectional flow vectors
- **Color:** #50E3C2 (Tidal Aqua)
- **Idle Animation:** Fluid vectors push through the rotor disk, slowing down on the exit side while spinning the turbine.
- **Click Disappearance Motion:** The Betz limit is exceeded. The turbine locks up, and the fluid vectors violently divert completely *around* the immovable disk in massive eddies.
- **Physics Basis:** Fluid kinetic energy, the Betz limit, and actuator disk theory.

### 7. GALVANIC EXCHANGE
- **Domain:** Marine Corrosion
- **Symbol/Shape:** Two dissimilar metal blocks (anode and cathode) connected by a wire, submerged in an electrolyte
- **Color:** #D0021B (Rust Red)
- **Idle Animation:** Microscopic ion particles detach from the anode block and drift slowly across the electrolyte to deposit on the cathode.
- **Click Disappearance Motion:** A massive stray current is applied; the anode undergoes rapid, extreme oxidation, dissolving entirely into a cloud of rust-colored pixels that diffuse away.
- **Physics Basis:** Electrochemistry, the Nernst equation, and galvanic corrosion.

### 8. CATENARY TENSION
- **Domain:** Offshore Platforms (Mooring)
- **Symbol/Shape:** A heavy mooring chain curving down from a floating platform to the seabed
- **Color:** #8B572A (Iron Brown)
- **Idle Animation:** The platform drifts slightly, causing the lower segment of the chain to lift off and lay back down on the seabed in a fluid catenary response.
- **Click Disappearance Motion:** Extreme heave motion snaps the line tight; tension exceeds breaking strength, snapping the chain at the fairlead. The heavy chain whips backward and plummets to the seabed.
- **Physics Basis:** The catenary equation, statics, and tensile stress.

### 9. GEOSTROPHIC DEFLECTION
- **Domain:** Ocean Currents
- **Symbol/Shape:** A fluid parcel moving on a rotating spherical grid
- **Color:** #4A90E2 (Oceanic Blue)
- **Idle Animation:** As the fluid parcel moves forward, it is continuously deflected to the right (in the Northern Hemisphere) into a steady circular gyre.
- **Click Disappearance Motion:** The Earth's rotation (Coriolis parameter) drops to zero; the pressure gradient takes entirely over, shooting the fluid parcel in a perfectly straight line off the screen.
- **Physics Basis:** Coriolis force, pressure gradients, and geostrophic flow.

### 10. HYDROSTATIC BUCKLING
- **Domain:** Submersible Design
- **Symbol/Shape:** A spherical pressure hull surrounded by inwardly directed pressure arrows
- **Color:** #111111 (Abyssal Black)
- **Idle Animation:** The arrows continuously press inward; the sphere imperceptibly compresses and rebounds elastically.
- **Click Disappearance Motion:** The depth increases past the yield point; the sphere undergoes catastrophic instantaneous buckling, imploding into a dense singularity before expanding outward as a shockwave.
- **Physics Basis:** Pascal's principle, hydrostatic pressure, and thin-wall shell buckling mechanics.

# Micro-Scientific Physics Models Catalog

## MATERIALS SCIENCE & ENGINEERING

### 1. Simple Cubic Unit Cell
- **Domain:** Materials Science (Crystallography)
- **Symbol/Shape:** A 3D cube wireframe with solid spheres at each of the 8 vertices.
- **Color:** #3498db (Sapphire Blue)
- **Idle Animation:** Slowly rotates on a diagonal axis while the corner atoms subtly pulse in size to mimic thermal vibration.
- **Click Disappearance Motion:** The corner atoms instantly translate outward along the 8 diagonal vectors off the screen, leaving the wireframe to shatter into dust.
- **Physics Basis:** Visualizes the fundamental repeating structure of a crystal lattice and atomic thermal fluctuations.

### 2. Edge Dislocation
- **Domain:** Materials Science (Defects & Plasticity)
- **Symbol/Shape:** A grid of dots (atoms) with an extra half-plane of dots wedged into the top half, forming a subtle "T" distortion.
- **Color:** #e74c3c (Crimson Red)
- **Idle Animation:** The lattice lines subtly undulate, while the core of the dislocation glows faintly, showing localized strain energy.
- **Click Disappearance Motion:** The extra half-plane glides laterally across the entire page (slip), pushing adjacent columns apart like a zipper until it exits the screen boundary, relaxing the remaining lattice into invisibility.
- **Physics Basis:** Visualizes dislocation glide, the fundamental mechanism of plastic deformation in metals.

### 3. Stress-Strain Curve
- **Domain:** Materials Science (Mechanical Properties)
- **Symbol/Shape:** A miniature set of Cartesian axes with a curve showing a linear rise, a yield peak, and a breaking point curve.
- **Color:** #2ecc71 (Emerald Green)
- **Idle Animation:** A tiny glowing point travels up the elastic linear region and snaps back to the origin, representing reversible elastic deformation.
- **Click Disappearance Motion:** The glowing point breaches the yield point, travels along the plastic deformation curve to the fracture point, whereupon the entire icon snaps in half horizontally and the two halves recoil off opposite edges of the screen.
- **Physics Basis:** Visualizes the Hookean elastic regime, yield strength, plastic deformation, and ultimate tensile fracture.

### 4. Eutectic Point
- **Domain:** Materials Science (Phase Diagrams)
- **Symbol/Shape:** A V-shaped set of liquidus curves meeting at a central point above a horizontal solidus line.
- **Color:** #9b59b6 (Amethyst)
- **Idle Animation:** A droplet shape hovers at the V-junction, shimmering as it rapidly alternates between two distinct solid phases (stripes and dots).
- **Click Disappearance Motion:** The droplet plummets below the horizontal line, instantly crystallizing into alternating lamellae (stripes) that explosively grow to fill the screen before fading.
- **Physics Basis:** Visualizes the eutectic reaction where a single liquid phase transforms simultaneously into two distinct solid phases upon cooling.

### 5. Polycrystalline Grain Boundary
- **Domain:** Materials Science (Microstructure)
- **Symbol/Shape:** Three intersecting regions of angled parallel lines, meeting at a central Y-junction.
- **Color:** #f1c40f (Gold)
- **Idle Animation:** The atoms at the boundary shimmer chaotically to show high energy and disorder, while the bulk crystalline lines remain static.
- **Click Disappearance Motion:** A simulated thermal annealing occurs—one grain grows rapidly, consuming the other two as its parallel lines sweep across the screen, erasing the boundaries until uniform space remains, then fades.
- **Physics Basis:** Visualizes grain boundary energetics and grain growth/coarsening driven by the reduction of interfacial energy.

### 6. Shape Memory Alloy
- **Domain:** Materials Science (Smart Materials)
- **Symbol/Shape:** A zig-zag martensitic lattice next to a square austenitic lattice.
- **Color:** #e67e22 (Carrot Orange)
- **Idle Animation:** The structure morphs continuously between the sheared zig-zag (martensite) and the rigid square (austenite) states.
- **Click Disappearance Motion:** The icon is mechanically "crushed" flat into detwinned martensite, then flashes red (heat) and violently snaps back to its original square austenite shape, expanding so large it exceeds the screen bounds.
- **Physics Basis:** Visualizes the diffusionless, reversible phase transformation between austenite and martensite triggered by temperature and stress.

### 7. Polymer Cross-linking
- **Domain:** Materials Science (Polymers)
- **Symbol/Shape:** Two wavy, parallel spaghetti-like chains connected by short perpendicular bridges.
- **Color:** #1abc9c (Turquoise)
- **Idle Animation:** The long chains wiggle (Brownian motion), but the cross-link bridges violently snap them back into place, demonstrating elasticity.
- **Click Disappearance Motion:** The cross-links suddenly multiply, rigidifying the chains into a dense 3D network that turns brittle, fractures into shards, and falls off the bottom of the screen.
- **Physics Basis:** Visualizes the vulcanization or curing process where chemical bonds link polymer chains, transforming a viscous liquid/thermoplastic into a rigid thermoset or elastomer.

### 8. Fiber-Reinforced Composite
- **Domain:** Materials Science (Composites)
- **Symbol/Shape:** A transparent matrix block containing highly aligned parallel cylinders (fibers).
- **Color:** #34495e (Wet Asphalt)
- **Idle Animation:** Stress arrows pulse along the axis of the fibers, showing load transfer from the weak matrix to the strong fibers.
- **Click Disappearance Motion:** Transverse force is applied; the matrix dissolves, and the fibers splinter and pull out (fiber pull-out fracture mechanism) in slow motion across the page.
- **Physics Basis:** Visualizes load transfer mechanisms and fracture toughness in anisotropic composite materials.

### 9. Substitutional Solid Solution
- **Domain:** Materials Science (Alloying)
- **Symbol/Shape:** A 4x4 grid of gray atoms with two randomly placed slightly larger blue atoms substituting the grid nodes.
- **Color:** #7f8c8d (Concrete)
- **Idle Animation:** The lattice surrounding the blue atoms visibly bulges and compresses, showing local strain fields.
- **Click Disappearance Motion:** The solute (blue) atoms begin a random walk (diffusion) jumping to adjacent lattice sites, multiplying until the entire screen is alloyed, then evaporating.
- **Physics Basis:** Visualizes Hume-Rothery rules and solid solution strengthening via lattice strain.

### 10. Interstitial Diffusion
- **Domain:** Materials Science (Kinetics)
- **Symbol/Shape:** A primary lattice of large spheres with a tiny glowing sphere sitting in the void (interstice) between them.
- **Color:** #f39c12 (Orange)
- **Idle Animation:** The tiny sphere vibrates intensely inside its cage of larger atoms, occasionally bumping against them.
- **Click Disappearance Motion:** The interstitial atom gains activation energy, squeezing through the bottleneck between host atoms and rapidly hopping from interstice to interstice across the entire page, leaving a glowing trail.
- **Physics Basis:** Visualizes Fick's laws of diffusion and the activation energy barrier for atomic migration.

### 11. Miller Indices Plane (111)
- **Domain:** Materials Science (Crystallography)
- **Symbol/Shape:** A cubic unit cell intersected by a glowing triangular plane cutting across its three axes.
- **Color:** #8e44ad (Wisteria)
- **Idle Animation:** A perpendicular normal vector pulses slowly from the origin to the plane.
- **Click Disappearance Motion:** The crystal plane acts as a mirror, reflecting a beam of X-rays into a bright diffraction spot that blinds the screen, referencing Bragg's Law.
- **Physics Basis:** Visualizes crystallographic planes used to define slip systems and X-ray diffraction peaks.

### 12. Creep Void Formation
- **Domain:** Materials Science (High-Temp Failure)
- **Symbol/Shape:** A grain boundary subjected to constant outward tension, with tiny spherical micro-voids forming along it.
- **Color:** #d35400 (Pumpkin)
- **Idle Animation:** The voids slowly pulse and slightly elongate along the tension axis over time.
- **Click Disappearance Motion:** The voids rapidly coalesce into a massive intergranular crack that unzips the screen diagonally into two completely separated halves.
- **Physics Basis:** Visualizes high-temperature time-dependent deformation and cavitation failure under constant load.

### 13. Piezoelectric Effect
- **Domain:** Materials Science (Electronic Ceramics)
- **Symbol/Shape:** A perovskite unit cell (like PZT) with an off-center central cation causing a built-in dipole moment.
- **Color:** #16a085 (Sea Green)
- **Idle Animation:** As the cell is mechanically compressed vertically, a spark of electricity arcs across the top and bottom faces.
- **Click Disappearance Motion:** An alternating electric field is applied, causing the cell to resonate violently (inverse piezoelectric effect) until it emits a visible acoustic shockwave that ripples across the page and clears the screen.
- **Physics Basis:** Visualizes electromechanical coupling in non-centrosymmetric crystals.

### 14. Glass Transition
- **Domain:** Materials Science (Amorphous Solids)
- **Symbol/Shape:** A disordered tangle of polymer chains next to a tiny thermometer.
- **Color:** #bdc3c7 (Silver)
- **Idle Animation:** The chains are frozen solid. As the thermometer pulses up, the chains suddenly become rubbery and fluid, wiggling freely.
- **Click Disappearance Motion:** The temperature drops instantly; the chains freeze mid-wiggle into a brittle glass state. A virtual hammer strikes them, shattering the structure into fractal glass shards.
- **Physics Basis:** Visualizes the Tg point where an amorphous material transitions from a hard, glassy state to a viscous, rubbery state.

### 15. Quenching (Martensitic Transformation)
- **Domain:** Materials Science (Metallurgy)
- **Symbol/Shape:** A glowing red-hot Face-Centered Cubic (FCC) lattice.
- **Color:** #c0392b (Dark Red)
- **Idle Animation:** The red-hot lattice vibrates rapidly with high thermal energy.
- **Click Disappearance Motion:** Plunged into a virtual liquid bath (bubbles appear); the FCC lattice instantly shears without diffusion into a highly strained, needle-like Body-Centered Tetragonal (BCT) lattice, freezing with an audible "ping" before fading.
- **Physics Basis:** Visualizes the diffusionless shear transformation of austenite to hard, brittle martensite during rapid cooling.


## NANOTECHNOLOGY

### 16. Quantum Dot
- **Domain:** Nanotechnology (Nanomaterials)
- **Symbol/Shape:** A tiny sphere composed of a few dozen atoms glowing with an intense core color.
- **Color:** #ff00ff (Magenta)
- **Idle Animation:** The dot fluctuates in size. As it shrinks, its emitted glow shifts to blue; as it grows, the glow shifts to red.
- **Click Disappearance Motion:** Absorbs a massive UV photon, an electron-hole pair (exciton) spirals outward, and upon recombining, emits a brilliant, blinding flash of specific-wavelength light that washes out the entire page.
- **Physics Basis:** Visualizes quantum confinement where the bandgap (and emission color) of a semiconductor nanoparticle is strictly dependent on its physical size.

### 17. Single-Walled Carbon Nanotube (SWCNT)
- **Domain:** Nanotechnology (Carbon Allotropes)
- **Symbol/Shape:** A microscopic cylinder of rolled hexagonal carbon rings.
- **Color:** #2c3e50 (Midnight Blue)
- **Idle Animation:** Electrons whiz ballistically down the chiral axis of the tube with zero resistance.
- **Click Disappearance Motion:** The tube unrolls itself flat into a massive 2D sheet of graphene, which then ripples like a flag in the wind until it flies off the screen.
- **Physics Basis:** Visualizes the 1D quantum confinement and ballistic electron transport of rolled graphene.

### 18. Molecular Motor (Kinesin)
- **Domain:** Nanotechnology (Nanomachines)
- **Symbol/Shape:** A tiny protein structure with two "feet" gripping a tubular track (microtubule).
- **Color:** #8e44ad (Purple)
- **Idle Animation:** The motor hydrolyzes an ATP molecule (flashing yellow spark) and takes a single tiny, mechanical "step" forward.
- **Click Disappearance Motion:** Consumes a massive wave of ATP, causing the motor to sprint furiously across the screen, dragging a massive cargo vesicle that obscures and wipes away the entire page content.
- **Physics Basis:** Visualizes biological molecular machines converting chemical energy into directed mechanical work at the nanoscale.

### 19. AFM Cantilever (Scanning Probe)
- **Domain:** Nanotechnology (Metrology)
- **Symbol/Shape:** A sharp pyramidal tip at the end of a micro-cantilever, positioned above a bumpy surface.
- **Color:** #2980b9 (Belize Hole)
- **Idle Animation:** A laser beam reflects off the back of the cantilever as the tip gently taps the surface (tapping mode), oscillating rapidly.
- **Click Disappearance Motion:** The tip engages contact mode, dragging across the entire page, mapping the topography. A 3D topological map of the screen's pixels renders and then dissipates.
- **Physics Basis:** Visualizes Atomic Force Microscopy, using van der Waals forces and laser deflection to map surfaces at the atomic level.

### 20. Self-Assembly (Liposome)
- **Domain:** Nanotechnology (Bottom-Up Fabrication)
- **Symbol/Shape:** A collection of tadpole-shaped amphiphilic molecules (hydrophilic heads, hydrophobic tails) floating randomly.
- **Color:** #27ae60 (Nephritis)
- **Idle Animation:** The hydrophobic tails aggressively repel water particles (tiny blue dots), constantly reorienting.
- **Click Disappearance Motion:** Thermodynamics takes over; the molecules rapidly self-organize into a massive perfectly spherical bilayer vesicle (liposome) that encapsulates the screen before dissolving.
- **Physics Basis:** Visualizes entropy-driven self-assembly and the hydrophobic effect utilized in nanomedicine delivery.

### 21. Nanofluidic Channel
- **Domain:** Nanotechnology (Nanofluidics)
- **Symbol/Shape:** A microscopic pipe, barely wider than a few water molecules, with overlapping electrical double layers.
- **Color:** #3498db (Blue)
- **Idle Animation:** Water molecules flow through in a highly ordered, single-file line due to extreme confinement.
- **Click Disappearance Motion:** An electric field is applied; electroosmotic flow kicks in, shooting a high-velocity jet of hydrated ions out of the channel that washes across the screen like a fluid wave.
- **Physics Basis:** Visualizes anomalous fluid dynamics and overlapping Debye lengths at the nanoscale.

### 22. Photolithography Exposure
- **Domain:** Nanotechnology (Nanofabrication)
- **Symbol/Shape:** A silicon wafer with photoresist, topped by a patterned photomask, bathed in UV light.
- **Color:** #f1c40f (UV Yellow)
- **Idle Animation:** Photons strike the unmasked regions, breaking chemical bonds in the photoresist (indicated by tiny pops).
- **Click Disappearance Motion:** A developer solution washes over; the exposed regions dissolve, revealing a complex labyrinthine nano-circuit that etches itself deep into the page before vanishing.
- **Physics Basis:** Visualizes top-down nanofabrication via UV exposure and chemical etching.

### 23. MEMS Comb Drive
- **Domain:** Nanotechnology (NEMS/MEMS)
- **Symbol/Shape:** Two sets of interdigitated microscopic silicon fingers (like two combs interlocking).
- **Color:** #7f8c8d (Silicon Gray)
- **Idle Animation:** A voltage is applied, and electrostatic forces pull the combs slightly closer together, then release.
- **Click Disappearance Motion:** A resonant frequency voltage is applied, causing the comb drive to oscillate wildly until it acts as a micro-actuator, literally pushing the text/content of the page out of the way.
- **Physics Basis:** Visualizes micro-electromechanical electrostatic actuation and capacitive sensing.

### 24. Graphene Dirac Cone
- **Domain:** Nanotechnology (Quantum Physics)
- **Symbol/Shape:** A 3D plot of two cones touching at their apices (Dirac point) over a hexagonal lattice.
- **Color:** #9b59b6 (Amethyst)
- **Idle Animation:** Electrons (dots) speed across the intersecting point without scattering, exhibiting zero effective mass.
- **Click Disappearance Motion:** The Dirac cones flatten out as a bandgap is artificially forced upon the graphene, stopping electron flow instantly. The lattice then rolls up into a buckyball (C60) and bounces away.
- **Physics Basis:** Visualizes the linear dispersion relation of graphene where charge carriers behave as massless Dirac fermions.

### 25. Plasmonic Nanoparticle
- **Domain:** Nanotechnology (Nanophotonics)
- **Symbol/Shape:** A gold nanoparticle interacting with an electromagnetic wave.
- **Color:** #f39c12 (Gold)
- **Idle Animation:** The electron cloud of the nanoparticle sloshes back and forth in perfect resonance with the electric field of the light wave.
- **Click Disappearance Motion:** The localized surface plasmon resonance peaks, creating an intense local near-field enhancement that scorches a glowing hot spot into the page before exploding into photons.
- **Physics Basis:** Visualizes Localized Surface Plasmon Resonance (LSPR), where conductive nanoparticles confine light to subwavelength dimensions.


## OPTICAL ENGINEERING

### 26. Stimulated Emission
- **Domain:** Optical Engineering (Lasers)
- **Symbol/Shape:** An excited atom (electron in upper shell). An incident photon approaches.
- **Color:** #e74c3c (Laser Red)
- **Idle Animation:** The incident photon hits the atom, forcing the electron to drop, emitting a second identical, in-phase photon.
- **Click Disappearance Motion:** The two photons hit two more atoms, yielding four, then eight in a massive cascade. A brilliant, coherent laser beam shoots horizontally across the screen, slicing through the UI.
- **Physics Basis:** Visualizes Einstein's theory of stimulated emission, the core mechanism of laser amplification.

### 27. Fabry-Perot Resonator
- **Domain:** Optical Engineering (Cavities)
- **Symbol/Shape:** Two parallel highly reflective mirrors with light bouncing between them.
- **Color:** #2ecc71 (Green)
- **Idle Animation:** A standing wave of light forms between the mirrors, constructively interfering.
- **Click Disappearance Motion:** The distance between the mirrors shifts by a fraction of a wavelength, destroying the resonance; the stored light escapes in a series of concentric Airy rings that expand infinitely across the page.
- **Physics Basis:** Visualizes optical cavities, longitudinal modes, and optical filtering.

### 28. Snell's Law Refraction
- **Domain:** Optical Engineering (Geometrical Optics)
- **Symbol/Shape:** A light ray hitting a horizontal boundary between air and glass, bending toward the normal.
- **Color:** #3498db (Blue)
- **Idle Animation:** The refractive index of the bottom medium subtly fluctuates, causing the transmitted ray angle to sweep slightly back and forth.
- **Click Disappearance Motion:** The incident angle increases past the critical angle. The refracted ray disappears, transitioning instantly to Total Internal Reflection, bouncing wildly around the screen edges like a trapped beam.
- **Physics Basis:** Visualizes refraction and the conservation of momentum parallel to a dielectric interface.

### 29. Single Slit Diffraction
- **Domain:** Optical Engineering (Physical Optics)
- **Symbol/Shape:** A plane wave of light passing through a tiny vertical slit in a barrier.
- **Color:** #9b59b6 (Purple)
- **Idle Animation:** The wavefront curves as it exits the slit (Huygens' principle) forming a central bright spot with faint side lobes.
- **Click Disappearance Motion:** The slit narrows to a point; the diffraction pattern expands infinitely into a massive sinc-squared intensity graph (Sinc²(x)) that overtakes the entire screen in fluctuating brightness.
- **Physics Basis:** Visualizes the wave nature of light and the Heisenberg uncertainty principle applied to photon momentum.

### 30. Step-Index Optical Fiber
- **Domain:** Optical Engineering (Fiber Optics)
- **Symbol/Shape:** A cylindrical core surrounded by cladding, with a light ray zig-zagging inside.
- **Color:** #1abc9c (Cyan)
- **Idle Animation:** Shows modal dispersion—different zig-zag paths (modes) arrive at the end of the fiber at slightly different times, widening a pulse.
- **Click Disappearance Motion:** The fiber profile shifts to a Graded-Index. The jagged light rays curve smoothly into perfect sine waves, synchronizing their arrival time, then shoot out of the screen at the speed of light.
- **Physics Basis:** Visualizes Total Internal Reflection, numerical aperture, and modal dispersion in telecommunications.

### 31. Holographic Interference
- **Domain:** Optical Engineering (Holography)
- **Symbol/Shape:** A reference beam and an object beam crossing paths on a photographic plate.
- **Color:** #f1c40f (Yellow)
- **Idle Animation:** Microscopic interference fringes (light and dark bands) form where the coherent waves overlap.
- **Click Disappearance Motion:** A reconstruction beam hits the plate, instantly projecting a glowing, rotating 3D hologram of a complex object that floats in front of the page before dissolving.
- **Physics Basis:** Visualizes phase and amplitude recording via interference, and 3D reconstruction via diffraction.

### 32. Linear Polarizer
- **Domain:** Optical Engineering (Polarization)
- **Symbol/Shape:** Unpolarized light (waves oscillating in all 3D directions) hitting a vertical wire-grid.
- **Color:** #34495e (Dark Slate)
- **Idle Animation:** Only vertically oscillating waves pass through; the rest are absorbed.
- **Click Disappearance Motion:** A second polarizer (analyzer) appears and rotates to 90 degrees (crossed polarizers). The light is completely extinguished in a pitch-black shadow that consumes the screen from the center out.
- **Physics Basis:** Visualizes Malus's Law and the transverse wave nature of light.

### 33. Photonic Crystal Bandgap
- **Domain:** Optical Engineering (Nanophotonics)
- **Symbol/Shape:** A periodic 3D lattice of dielectric spheres (like a synthetic opal).
- **Color:** #e67e22 (Orange)
- **Idle Animation:** Certain wavelengths of light effortlessly pass through, while a specific color hits the structure and is completely reflected.
- **Click Disappearance Motion:** A defect is introduced into the crystal lattice, creating an optical waveguide. The trapped light violently races through the defect channel, carving a glowing path across the page before exiting.
- **Physics Basis:** Visualizes photonic bandgaps where periodic dielectric variations prevent the propagation of certain electromagnetic frequencies.

### 34. Adaptive Optics
- **Domain:** Optical Engineering (Astronomical Optics)
- **Symbol/Shape:** A wavefront distorted by atmospheric turbulence hitting a deformable mirror.
- **Color:** #2980b9 (Ocean Blue)
- **Idle Animation:** Tiny actuators behind the mirror constantly push and pull, flattening the distorted wavefront into a perfect plane wave.
- **Click Disappearance Motion:** A laser guide star shoots straight up out of the icon, projecting a grid across the screen to measure aberrations, correcting the entire page focus from blurry to razor-sharp.
- **Physics Basis:** Visualizes active wavefront correction using Shack-Hartmann sensors and micro-actuators to overcome atmospheric seeing.

### 35. Raman Scattering
- **Domain:** Optical Engineering (Spectroscopy)
- **Symbol/Shape:** A green laser photon hitting a vibrating diatomic molecule.
- **Color:** #27ae60 (Green)
- **Idle Animation:** 99.9% of the time, the photon scatters elastically (Rayleigh, still green).
- **Click Disappearance Motion:** An inelastic collision occurs! The molecule absorbs a quantum of vibrational energy, and the scattered photon shifts instantly to red (Stokes shift). A massive spectrograph plots the peak across the screen.
- **Physics Basis:** Visualizes inelastic photon scattering used to identify molecular vibrational modes.


## ACOUSTICS ENGINEERING

### 36. Longitudinal Wave (Compression/Rarefaction)
- **Domain:** Acoustics Engineering (Fundamentals)
- **Symbol/Shape:** A horizontal spring or series of vertical lines spaced at varying densities.
- **Color:** #34495e (Slate Gray)
- **Idle Animation:** Dense regions (compressions) and sparse regions (rarefactions) travel continuously from left to right.
- **Click Disappearance Motion:** A massive impulse is applied. The wave turns into a nonlinear acoustic shockwave (sonic boom) that blasts across the screen, distorting the page pixels as it passes.
- **Physics Basis:** Visualizes the propagation of sound through a fluid via local pressure variations.

### 37. Helmholtz Resonator
- **Domain:** Acoustics Engineering (Resonance)
- **Symbol/Shape:** A cavity with a narrow neck (like a glass bottle).
- **Color:** #16a085 (Teal)
- **Idle Animation:** A mass of air in the neck bobs up and down on the "springiness" of the air volume inside the cavity, radiating a low-frequency hum.
- **Click Disappearance Motion:** The incident sound perfectly matches the resonant frequency. The oscillation builds to an extreme amplitude until the "bottle" shatters, and shattered sound waves dissipate in all directions.
- **Physics Basis:** Visualizes lumped-parameter acoustic resonance (acoustic mass and acoustic compliance).

### 38. Standing Wave in a Pipe
- **Domain:** Acoustics Engineering (Musical Acoustics)
- **Symbol/Shape:** A cylindrical pipe open at one end and closed at the other, containing a sinusoidal wave envelope.
- **Color:** #8e44ad (Deep Purple)
- **Idle Animation:** The pressure wave creates a node (no pressure change) at the open end and an antinode (max pressure change) at the closed end, pulsing in place.
- **Click Disappearance Motion:** The wave jumps to the next harmonic (overtone), dividing into multiple nodes, vibrating so fast the pipe bursts open and transforms into a full spectrogram rolling off the screen.
- **Physics Basis:** Visualizes acoustic boundary conditions and resonant modes of air columns.

### 39. Acoustic Impedance Mismatch
- **Domain:** Acoustics Engineering (Transducers/Medical)
- **Symbol/Shape:** A sound wave traveling from a sparse medium (air) to a dense medium (water).
- **Color:** #2980b9 (Blue)
- **Idle Animation:** The wave hits the boundary; almost all of it reflects back, with a tiny sliver transmitting.
- **Click Disappearance Motion:** A quarter-wave matching layer is inserted at the boundary. 100% of the acoustic energy suddenly transmits through, sweeping entirely off the screen without reflection.
- **Physics Basis:** Visualizes characteristic acoustic impedance (Z = ρc) and the necessity of matching layers (like ultrasound gel).

### 40. Doppler Effect
- **Domain:** Acoustics Engineering (Wave Kinematics)
- **Symbol/Shape:** A dot emitting concentric circles of sound, moving towards the right.
- **Color:** #e74c3c (Red)
- **Idle Animation:** The wavefronts bunch up on the right (higher frequency/pitch) and spread out on the left (lower frequency/pitch).
- **Click Disappearance Motion:** The dot accelerates past the speed of sound (Mach 1). A sharp, V-shaped Mach cone forms, sweeping across the page and muting all elements it touches.
- **Physics Basis:** Visualizes the change in frequency of a wave in relation to an observer moving relative to the wave source.

### 41. Piezoelectric Ultrasonic Transducer
- **Domain:** Acoustics Engineering (Non-Destructive Testing)
- **Symbol/Shape:** A backing block attached to a piezoceramic disc, sending out high-frequency pulses.
- **Color:** #f39c12 (Orange)
- **Idle Animation:** The disc rings briefly, sending out a short ultrasonic pulse that bounces off a microscopic flaw and returns.
- **Click Disappearance Motion:** The transducer sweeps in a phased array pattern, steering the acoustic beam dynamically to scan the entire screen, revealing a hidden structural crack in the page layout.
- **Physics Basis:** Visualizes pulse-echo ultrasonics, acoustic attenuation, and time-of-flight measurements.

### 42. Anechoic Wedge (Absorption)
- **Domain:** Acoustics Engineering (Noise Control)
- **Symbol/Shape:** A series of deep, triangular foam wedges lining a wall.
- **Color:** #2c3e50 (Dark Blue/Gray)
- **Idle Animation:** Sound waves enter the wedges, bounce deep into the crevice, and steadily lose amplitude (turn to heat) until extinguished.
- **Click Disappearance Motion:** The wedges suddenly extend and cover the entire screen. Complete silence (visualized by absorbing all background light/color) consumes the page, leaving a void.
- **Physics Basis:** Visualizes acoustic impedance matching to air and complete absorption of acoustic energy to simulate a free field.

### 43. Room Reverberation Ray Tracing
- **Domain:** Acoustics Engineering (Architectural Acoustics)
- **Symbol/Shape:** A tiny enclosed rectangular room with a source emitting discrete acoustic rays.
- **Color:** #1abc9c (Aquamarine)
- **Idle Animation:** Rays bounce off the walls, losing energy with each reflection (specular reflection), creating a diffuse sound field.
- **Click Disappearance Motion:** The room scales up to a massive concert hall. The rays multiply into thousands, mapping the impulse response (RT60) curve across the screen, before decaying exponentially into silence.
- **Physics Basis:** Visualizes architectural acoustic parameters, early reflections, late reverberation tails, and Sabine's equation.



---

# PART 4 — ENERGY, ROBOTICS, INDUSTRIAL, FUNDAMENTAL PHYSICS

---
# Micro-Scientific Physics Models Catalog

## ENERGY ENGINEERING

### 1. PHOTOVOLTAIC EFFECT
- **Domain:** Energy Engineering (Solar Energy)
- **Symbol/Shape:** A multi-layered square with a tiny sunburst and a rising arrow (~20px scale).
- **Color:** `#FFD700` (Solar Gold)
- **Idle Animation:** A small white dot (electron) continuously jumps from the bottom layer to the top layer, leaving a hollow circle (hole) behind.
- **Click Disappearance Motion:** Emits a radial burst of photons, and the layers peel away outwards before fading into pure light.
- **Physics Basis:** The photoelectric effect, where photons excite electrons across the bandgap of a semiconductor, generating a current.

### 2. BETZ LIMIT TURBINE
- **Domain:** Energy Engineering (Wind Energy)
- **Symbol/Shape:** A sleek three-blade propeller inside a stylized stream tube.
- **Color:** `#87CEEB` (Sky Blue)
- **Idle Animation:** The blades rotate slowly while the stream tube slightly expands downwind.
- **Click Disappearance Motion:** The wind stream abruptly accelerates, scattering the turbine blades in a spiral vortex downwind as they shrink to zero.
- **Physics Basis:** Betz's law, which states that no turbine can capture more than 16/27 (59.3%) of the kinetic energy in wind.

### 3. PELTON WHEEL BUCKET
- **Domain:** Energy Engineering (Hydroelectric)
- **Symbol/Shape:** A dual-cupped bucket hit by a single straight line.
- **Color:** `#000080` (Deep Water Blue)
- **Idle Animation:** A continuous pulse of water hits the center ridge and elegantly splits into two symmetrical U-turns.
- **Click Disappearance Motion:** The bucket shatters into a massive splash of tiny blue droplets that rain down the screen.
- **Physics Basis:** Impulse turbines using momentum transfer from high-velocity water jets striking split buckets to maximize energy extraction.

### 4. GEOTHERMAL HEAT PUMP
- **Domain:** Energy Engineering (Geothermal)
- **Symbol/Shape:** A U-shaped pipe descending into a stratified ground layer with arrows indicating flow.
- **Color:** `#CD5C5C` (Earth Red)
- **Idle Animation:** Color gradients (red and blue) slowly circulate through the U-pipe loop.
- **Click Disappearance Motion:** The pipe rapidly glows white-hot from the bottom up, then instantly sinks into the ground and vanishes.
- **Physics Basis:** Harnessing the stable thermal mass of the earth for heat exchange and thermodynamic cycles.

### 5. LITHIUM-ION INTERCALATION
- **Domain:** Energy Engineering (Batteries)
- **Symbol/Shape:** Two parallel lattice structures separated by a distinct gap.
- **Color:** `#32CD32` (Battery Green)
- **Idle Animation:** Tiny spheres (lithium ions) rhythmically migrate back and forth between the two lattices.
- **Click Disappearance Motion:** The lattices slam together, neutralizing the ions in a bright flash before collapsing into a single dot.
- **Physics Basis:** Electrochemical charging and discharging via lithium ions moving between the anode and cathode lattices.

### 6. SOLID-STATE ELECTROLYTE
- **Domain:** Energy Engineering (Batteries)
- **Symbol/Shape:** A rigid, dense crystalline grid between two solid electrodes.
- **Color:** `#00FA9A` (Neon Green)
- **Idle Animation:** A faint pulse of energy perfectly navigates the rigid lattice without distorting it.
- **Click Disappearance Motion:** The lattice shatters into perfect geometric shards that rapidly drift apart.
- **Physics Basis:** High-density energy storage using solid electrodes and a solid electrolyte, eliminating liquid flammability and dendrite formation.

### 7. PEM FUEL CELL
- **Domain:** Energy Engineering (Fuel Cells)
- **Symbol/Shape:** A central membrane block with H2 entering one side and H2O exiting the other.
- **Color:** `#1E90FF` (Hydrogen Blue)
- **Idle Animation:** Small pairs of dots (H2) split at the membrane; one crosses, the other loops around as an electron.
- **Click Disappearance Motion:** The membrane flashes, and the entire icon transforms into a single drop of water that falls off the screen.
- **Physics Basis:** Proton Exchange Membrane separating protons and electrons from hydrogen to create current before reacting with oxygen.

### 8. FLYWHEEL ROTOR
- **Domain:** Energy Engineering (Energy Storage)
- **Symbol/Shape:** A thick, heavy rimmed disk mounted on a magnetic bearing axle.
- **Color:** `#C0C0C0` (Steel Silver)
- **Idle Animation:** The disk spins at a high, constant speed with faint kinetic motion blur lines.
- **Click Disappearance Motion:** Spins so fast it undergoes radial expansion, fragmenting into dust due to simulated centripetal failure.
- **Physics Basis:** Kinetic energy storage using rotational inertia, limited by the tensile strength of the rotor material.

### 9. SUPERCAPACITOR DOUBLE-LAYER
- **Domain:** Energy Engineering (Energy Storage)
- **Symbol/Shape:** Two porous plates packed with opposite charges perfectly aligned across a microscopic gap.
- **Color:** `#FF8C00` (Electric Orange)
- **Idle Animation:** The charges vibrate rapidly in place, maintaining a high-tension static gap.
- **Click Disappearance Motion:** The two layers instantly arc across the gap in a massive electrical discharge, evaporating the icon.
- **Physics Basis:** Helmholtz double-layer capacitance storing energy electrostatically without chemical reactions.

### 10. SEEBECK THERMOCOUPLE
- **Domain:** Energy Engineering (Thermoelectric)
- **Symbol/Shape:** Two dissimilar wires joined at a hot junction (red) and a cold junction (blue).
- **Color:** `#800080` (Gradient Purple)
- **Idle Animation:** A continuous loop of small glowing dots flows from the hot side to the cold side.
- **Click Disappearance Motion:** Thermal equalization; the red and blue instantly turn dull grey, and the wires dissolve into ash.
- **Physics Basis:** The Seebeck effect, where a temperature difference between two dissimilar semiconductors/metals produces a voltage.

### 11. COMPRESSED AIR CAVERN
- **Domain:** Energy Engineering (Energy Storage)
- **Symbol/Shape:** A stylized underground cavern filled with dense air molecules, topped with a valve.
- **Color:** `#A4C639` (Pressure Green)
- **Idle Animation:** The air molecules bounce furiously inside the confined cavern.
- **Click Disappearance Motion:** The top valve blows off, and the cavern forcefully exhales all contents upward like a geyser before collapsing.
- **Physics Basis:** Compressed Air Energy Storage (CAES), using elastic potential energy of air in constant-volume underground formations.

### 12. SMART GRID NODE
- **Domain:** Energy Engineering (Grid Integration)
- **Symbol/Shape:** A central hexagon connected to multiple smaller nodes via dashed lines.
- **Color:** `#00FFFF` (Cyan)
- **Idle Animation:** Data packets (bright pulses) run back and forth along the lines in an optimized rhythm.
- **Click Disappearance Motion:** A cascading blackout effect; the nodes flicker and go dark one by one, shrinking into the background.
- **Physics Basis:** Bi-directional flow of electricity and data to dynamically balance loads and integrate distributed generation.

## ROBOTICS & MECHATRONICS

### 13. DENAVIT-HARTENBERG KINEMATICS
- **Domain:** Robotics (Kinematics)
- **Symbol/Shape:** Three segmented lines connected by two rotational joints with coordinate frames.
- **Color:** `#FF4500` (Orange Red)
- **Idle Animation:** The arm subtly traces a smooth, tiny figure-eight pattern.
- **Click Disappearance Motion:** The joints unhinge, and the segments fold perfectly into a single point before winking out.
- **Physics Basis:** Forward and inverse kinematics mapping joint space to Cartesian space via rigid body transformations.

### 14. PID CONTROLLER
- **Domain:** Robotics (Control Systems)
- **Symbol/Shape:** A feedback loop diagram with three parallel blocks (P, I, D) summing into a plant.
- **Color:** `#2E8B57` (Sea Green)
- **Idle Animation:** A signal wave travels the loop, dynamically flattening out as it reaches the end.
- **Click Disappearance Motion:** The error signal wildly overshoots, causing the loop to oscillate infinitely and vibrate apart into static.
- **Physics Basis:** Proportional-Integral-Derivative control calculating error values and applying corrective continuous adjustments.

### 15. LIDAR POINT CLOUD
- **Domain:** Robotics (Sensors)
- **Symbol/Shape:** A spinning central emitter casting a fan of discrete dots against an invisible corner.
- **Color:** `#FF1493` (Deep Pink)
- **Idle Animation:** The emitter continuously sweeps, lighting up a corner of dots upon contact.
- **Click Disappearance Motion:** The central emitter fires one 360-degree blinding pulse, vaporizing all the points and itself.
- **Physics Basis:** Time-of-flight laser ranging used to construct high-resolution 3D spatial maps.

### 16. IMU (GYRO & ACCELEROMETER)
- **Domain:** Robotics (Sensors)
- **Symbol/Shape:** A tiny 3D gimbal with an inner proof mass.
- **Color:** `#DAA520` (Goldenrod)
- **Idle Animation:** The gimbal rings slowly rotate while the inner mass bobs gently in the Z-axis.
- **Click Disappearance Motion:** Loses its reference frame, spinning chaotically faster and faster until it blurs into nothing.
- **Physics Basis:** Inertial navigation using MEMS tuning forks for Coriolis-based angular rate and spring-mass systems for acceleration.

### 17. A* PATHFINDING
- **Domain:** Robotics (Path Planning)
- **Symbol/Shape:** A grid with a start point, end point, and a jagged optimal path weaving around a block.
- **Color:** `#4169E1` (Royal Blue)
- **Idle Animation:** A bright pulse travels the jagged path from start to finish repeatedly.
- **Click Disappearance Motion:** The grid instantly fills with dead-end search nodes (flood fill) before dissolving entirely.
- **Physics Basis:** Heuristic search algorithms minimizing f(n) = g(n) + h(n) for optimal navigation in configuration space.

### 18. IMPEDANCE CONTROL
- **Domain:** Robotics (Haptics/Control)
- **Symbol/Shape:** A robotic end-effector interacting with a virtual spring-damper system on a surface.
- **Color:** `#9932CC` (Dark Orchid)
- **Idle Animation:** The end-effector gently pushes into the spring, which resists and bounces it back smoothly.
- **Click Disappearance Motion:** The spring becomes infinitely stiff; the end-effector hits it, shatters, and flies off-screen.
- **Physics Basis:** Controlling the dynamic relationship (mass-spring-damper) between a manipulator and its environment rather than pure position.

### 19. MODEL PREDICTIVE CONTROL
- **Domain:** Robotics (Control)
- **Symbol/Shape:** A current state dot projecting multiple faint future trajectory curves, converging on one bold line.
- **Color:** `#00CED1` (Dark Turquoise)
- **Idle Animation:** The future trajectories constantly recalculate and wiggle as the dot moves slightly forward.
- **Click Disappearance Motion:** The time horizon rapidly stretches to infinity, thinning the trajectories until they snap.
- **Physics Basis:** Solving finite-horizon optimal control problems in real-time, accounting for system constraints.

### 20. BOIDS SWARM
- **Domain:** Robotics (Swarm Robotics)
- **Symbol/Shape:** A cluster of 5 tiny triangles pointing in the same general direction.
- **Color:** `#FF69B4` (Hot Pink)
- **Idle Animation:** The triangles undulate in a synchronized flocking motion without colliding.
- **Click Disappearance Motion:** The cohesion rule breaks; the triangles aggressively scatter in perfectly opposite directions off-screen.
- **Physics Basis:** Emergent decentralized behavior based on separation, alignment, and cohesion rules.

### 21. SLAM GRAPH
- **Domain:** Robotics (Computer Vision/Navigation)
- **Symbol/Shape:** A robot moving along a path, leaving pose nodes and landmark observation edges.
- **Color:** `#F4A460` (Sandy Brown)
- **Idle Animation:** The robot moves, adding a new node, while the whole graph gently shifts (loop closure optimization).
- **Click Disappearance Motion:** A catastrophic loop-closure failure; the graph violently folds in on itself into a tangled knot and disappears.
- **Physics Basis:** Simultaneous Localization and Mapping, solving a probabilistic graph optimization problem using sensor data.

### 22. SOFT PNEUMATIC ACTUATOR
- **Domain:** Robotics (Soft Robotics)
- **Symbol/Shape:** A ribbed, flexible finger-like appendage.
- **Color:** `#98FB98` (Pale Green)
- **Idle Animation:** Rhythmically inflates (curling inward) and deflates (straightening).
- **Click Disappearance Motion:** Over-pressurizes like a balloon and loudly pops, leaving nothing but a puff of air.
- **Physics Basis:** Fluidic elastomer actuators relying on asymmetric strain to generate continuous bending motion.

### 23. POTENTIAL FIELD NAVIGATION
- **Domain:** Robotics (Path Planning)
- **Symbol/Shape:** A topographic contour map with a deep "valley" (goal) and "hills" (obstacles).
- **Color:** `#BDB76B` (Dark Khaki)
- **Idle Animation:** A particle rolls smoothly down the gradient, sliding precisely around a hill.
- **Click Disappearance Motion:** The particle gets trapped in a local minimum and spirals infinitely fast into the ground.
- **Physics Basis:** Artificial potential functions where goals exert attractive forces and obstacles exert repulsive forces on a robot.

### 24. HARMONIC DRIVE GEAR
- **Domain:** Robotics (Actuators)
- **Symbol/Shape:** A rigid circular spline enclosing a flexible flexspline and an elliptical wave generator.
- **Color:** `#4682B4` (Steel Blue)
- **Idle Animation:** The elliptical core rotates fast, causing the outer flexible gear to rotate very slowly.
- **Click Disappearance Motion:** The flexspline snaps from metal fatigue and unspools like a loose ribbon off the screen.
- **Physics Basis:** Strain wave gearing utilizing metal elasticity to achieve zero-backlash, high-ratio torque reduction.

## INDUSTRIAL & SYSTEMS ENGINEERING

### 25. SIMPLEX ALGORITHM
- **Domain:** Industrial (Optimization)
- **Symbol/Shape:** A 3D convex polyhedron (feasible region).
- **Color:** `#DDA0DD` (Plum)
- **Idle Animation:** A glowing dot hops sequentially from one vertex to an adjacent higher vertex.
- **Click Disappearance Motion:** The polyhedron flattens into 2D, then 1D, then collapses into the absolute origin.
- **Physics Basis:** Linear programming optimization, traversing the edges of a convex polytope to find the absolute maximum/minimum.

### 26. M/M/1 QUEUE
- **Domain:** Industrial (Queuing Theory)
- **Symbol/Shape:** A line of uniform dots entering a single processing box and exiting at a different rate.
- **Color:** `#F0E68C` (Khaki)
- **Idle Animation:** Dots arrive randomly (Poisson) and are processed continuously, causing the line length to breathe.
- **Click Disappearance Motion:** Arrival rate suddenly exceeds processing rate; the line extends infinitely off the screen until the system crashes.
- **Physics Basis:** Stochastic modeling of wait times and throughput using Markovian arrival and service processes.

### 27. RULA ERGONOMICS
- **Domain:** Industrial (Ergonomics)
- **Symbol/Shape:** A stylized stick figure sitting at a workstation with colored joint angles.
- **Color:** `#FFA07A` (Light Salmon)
- **Idle Animation:** The figure subtly adjusts its posture, shifting joints from yellow (strain) to green (optimal).
- **Click Disappearance Motion:** The figure completely collapses into a heap due to accumulated biomechanical fatigue.
- **Physics Basis:** Anthropometry and biomechanics applied to evaluate human physical exposure to risk factors.

### 28. SHEWHART CONTROL CHART
- **Domain:** Industrial (Quality Control)
- **Symbol/Shape:** A time-series graph with a mean line, UCL, and LCL, and plotted data points.
- **Color:** `#20B2AA` (Light Sea Green)
- **Idle Animation:** New data points appear sequentially, bouncing randomly but staying neatly within the control limits.
- **Click Disappearance Motion:** Seven points suddenly trend wildly above the Upper Control Limit, snapping the graph lines and pulling the entire chart off-screen.
- **Physics Basis:** Statistical Process Control separating common cause variance from special cause variance.

### 29. ECONOMIC ORDER QUANTITY (EOQ)
- **Domain:** Industrial (Supply Chain)
- **Symbol/Shape:** A perfectly jagged sawtooth wave graph representing inventory levels.
- **Color:** `#6B8E23` (Olive Drab)
- **Idle Animation:** The wave slowly drains down to a reorder point, then instantly shoots vertically back up.
- **Click Disappearance Motion:** Demand instantly flatlines, the inventory stack piles infinitely high, and falls over.
- **Physics Basis:** Cost-minimization calculus balancing inventory holding costs against fixed ordering costs.

### 30. WEIBULL BATHTUB CURVE
- **Domain:** Industrial (Reliability)
- **Symbol/Shape:** A distinct "bathtub" shaped curve showing failure rates over time.
- **Color:** `#DC143C` (Crimson)
- **Idle Animation:** A marker traces the curve, moving fast down the "infant mortality" slope, cruising the flat bottom, and climbing the "wear-out" end.
- **Click Disappearance Motion:** A catastrophic random failure occurs in the middle flat zone, tearing the curve in half.
- **Physics Basis:** Reliability engineering hazard functions integrating early failures, random failures, and age-related wear.

### 31. NASH EQUILIBRIUM
- **Domain:** Industrial (Operations Research)
- **Symbol/Shape:** A 2x2 payoff matrix with one highlighted quadrant.
- **Color:** `#9370DB` (Medium Purple)
- **Idle Animation:** Faint highlights flicker between options, but always settle back on the stable mutually optimal quadrant.
- **Click Disappearance Motion:** Players switch to irrational strategies; the matrix spins rapidly and dissolves into chaotic noise.
- **Physics Basis:** Non-cooperative game theory where no player can gain by unilaterally changing their strategy.

### 32. KANBAN PULL SYSTEM
- **Domain:** Industrial (Lean Manufacturing)
- **Symbol/Shape:** Three columns (To Do, Doing, Done) with tiny cards.
- **Color:** `#FFA500` (Orange)
- **Idle Animation:** A card smoothly transfers from left to right only when there is empty space in the next column.
- **Click Disappearance Motion:** The WIP limit is ignored, cards flood the middle column until it explodes like a piñata.
- **Physics Basis:** Just-In-Time production governed by Little's Law, limiting Work-In-Progress to maximize throughput.

### 33. MONTE CARLO SIMULATION
- **Domain:** Industrial (Simulation)
- **Symbol/Shape:** A bell curve filled with a dense cloud of semi-transparent dots.
- **Color:** `#00BFFF` (Deep Sky Blue)
- **Idle Animation:** Hundreds of tiny dots continuously rain down, building up the perfect Gaussian distribution.
- **Click Disappearance Motion:** The random seed breaks; all dots fall in a single straight, impossible vertical line.
- **Physics Basis:** Utilizing pseudo-random stochastic sampling to numerically solve complex deterministic problems.

### 34. PETRI NET
- **Domain:** Industrial (Discrete Event)
- **Symbol/Shape:** Circles (places) and bars (transitions) connected by directed arcs, with a token inside one circle.
- **Color:** `#8B4513` (Saddle Brown)
- **Idle Animation:** The token fires through the transition bar, splitting into two tokens in the subsequent places.
- **Click Disappearance Motion:** A deadlock occurs; tokens get trapped, turn red, and the entire network slowly fades to black.
- **Physics Basis:** Mathematical modeling of distributed, concurrent, and asynchronous discrete event systems.

## FUNDAMENTAL PHYSICS MODELS

### 35. NEWTON'S INERTIA & ACTION-REACTION
- **Domain:** Fundamental Physics (Mechanics)
- **Symbol/Shape:** A classic Newton's Cradle with 5 steel spheres.
- **Color:** `#C0C0C0` (Silver)
- **Idle Animation:** The end spheres rhythmically click back and forth, perfectly conserving momentum.
- **Click Disappearance Motion:** The spheres become completely inelastic; they hit with a dull thud, freeze in place, and turn to stone.
- **Physics Basis:** Conservation of momentum, elastic collisions, and Newton's Third Law.

### 36. SCHRÖDINGER'S PROBABILITY CLOUD
- **Domain:** Fundamental Physics (Quantum Mechanics)
- **Symbol/Shape:** A hydrogen atom orbital (e.g., the dumbbell-shaped p-orbital) made of a dense cloud of tiny points.
- **Color:** `#4B0082` (Indigo)
- **Idle Animation:** The density of the dots constantly shifts and shimmers, representing varying probability densities.
- **Click Disappearance Motion:** Wavefunction collapse: the entire cloud instantly coalesces into a single, perfectly defined point, which then vanishes.
- **Physics Basis:** The Schrödinger equation dictating that particles exist in a superposition of probable states until measured.

### 37. SPACETIME CURVATURE
- **Domain:** Fundamental Physics (General Relativity)
- **Symbol/Shape:** A 2D grid bending down into a deep gravity well with a heavy mass at the center.
- **Color:** `#6A5ACD` (Slate Blue)
- **Idle Animation:** A small moon seamlessly orbits the central mass along the geodesic curves of the grid.
- **Click Disappearance Motion:** The central mass goes supernova, flattening the grid violently, catapulting the moon off-screen.
- **Physics Basis:** General Relativity, where massive objects warp the fabric of spacetime, and gravity is simply geometry.

### 38. TIME DILATION (LORENTZ FACTOR)
- **Domain:** Fundamental Physics (Special Relativity)
- **Symbol/Shape:** Two clocks; one stationary and ticking normally, one moving fast and ticking slowly.
- **Color:** `#FF0000` (Red)
- **Idle Animation:** The moving clock stretches horizontally (length contraction) and its hands move noticeably slower.
- **Click Disappearance Motion:** The fast clock reaches the speed of light; time stops entirely, its width goes to zero, and it vanishes into a photon streak.
- **Physics Basis:** As velocity approaches the speed of light, time slows down and length contracts relative to a stationary observer.

### 39. DOUBLE-SLIT INTERFERENCE
- **Domain:** Fundamental Physics (Wave-Particle Duality)
- **Symbol/Shape:** A wave front hitting a barrier with two slits, emerging as overlapping ripples hitting a back screen.
- **Color:** `#00FA9A` (Medium Spring Green)
- **Idle Animation:** The overlapping ripples continuously generate an interference pattern (stripes) on the back screen.
- **Click Disappearance Motion:** An "observer" eye blinks open; the waves instantly turn into two boring bullet-hole clusters, ruining the pattern.
- **Physics Basis:** Particles (like electrons or photons) act as waves creating interference, until measured, forcing particle behavior.

### 40. ENTROPY ARROW OF TIME
- **Domain:** Fundamental Physics (Thermodynamics)
- **Symbol/Shape:** A closed box with neatly stacked hot (red) particles on the left and cold (blue) on the right.
- **Color:** `#FF6347` (Tomato) & `#4682B4` (Steel Blue)
- **Idle Animation:** The particles slowly drift, mixing into a uniform purple chaos.
- **Click Disappearance Motion:** The Second Law is violated; the purple chaos magically sorts itself perfectly back into red and blue, then blinks out of existence.
- **Physics Basis:** The Second Law of Thermodynamics, stating that the total entropy (disorder) of an isolated system always increases over time.

### 41. QUANTUM TUNNELING
- **Domain:** Fundamental Physics (Quantum Mechanics)
- **Symbol/Shape:** A small wave approaching a tall, thick energy barrier.
- **Color:** `#FFFF00` (Yellow)
- **Idle Animation:** The wave hits the wall, most reflects back, but a faint, lower-amplitude wave emerges on the other side.
- **Click Disappearance Motion:** The particle loses all energy inside the barrier, freezing mid-tunnel, before the barrier crushes it.
- **Physics Basis:** Quantum probability allowing particles to pass through potential energy barriers they classically shouldn't be able to overcome.

### 42. HEISENBERG UNCERTAINTY
- **Domain:** Fundamental Physics (Quantum Mechanics)
- **Symbol/Shape:** A particle whose position and velocity vectors are visually competing.
- **Color:** `#FF00FF` (Magenta)
- **Idle Animation:** When the particle becomes visually sharp (known position), its speed vector blurs wildly. When the speed vector sharpens, the particle turns into a blurry cloud.
- **Click Disappearance Motion:** Both are measured perfectly at once; the resulting mathematical impossibility tears a hole in the screen.
- **Physics Basis:** The fundamental limit to the precision with which certain pairs of physical properties (position/momentum) can be known simultaneously.

### 43. QUANTUM ENTANGLEMENT
- **Domain:** Fundamental Physics (Quantum Mechanics)
- **Symbol/Shape:** Two glowing particles spinning in opposite directions, connected by a faint, glowing thread.
- **Color:** `#7FFFD4` (Aquamarine)
- **Idle Animation:** If one particle's axis tilts up, the other instantaneously tilts down, maintaining anti-symmetry.
- **Click Disappearance Motion:** The thread is cut; local hidden variables fail, they spin independently for a second, then annihilate each other.
- **Physics Basis:** Spooky action at a distance, where the quantum state of each particle cannot be described independently of the state of the others.

### 44. CONSERVATION OF ENERGY
- **Domain:** Fundamental Physics (Mechanics)
- **Symbol/Shape:** A simple pendulum swinging inside a U-shaped potential energy well.
- **Color:** `#3CB371` (Medium Sea Green)
- **Idle Animation:** The pendulum swings. Two bar charts (Kinetic and Potential Energy) perfectly invert each other; their sum never changes.
- **Click Disappearance Motion:** Friction is turned to max; the pendulum screeches to a halt at the bottom, converting all energy to a burst of red heat.
- **Physics Basis:** The First Law of Thermodynamics: energy cannot be created or destroyed, only transformed.

### 45. E=MC² (MASS-ENERGY EQUIVALENCE)
- **Domain:** Fundamental Physics (Special Relativity)
- **Symbol/Shape:** A heavy, solid cube (mass) resting on a scale, glowing with internal light.
- **Color:** `#FFD700` (Gold)
- **Idle Animation:** The cube subtly breathes, converting tiny amounts of mass into bright sparks of energy and back.
- **Click Disappearance Motion:** The entire mass instantly converts to energy, creating a blinding, silent flash that bleaches the entire page.
- **Physics Basis:** Mass and energy are mutually convertible, with a tiny amount of mass holding a colossal amount of rest energy.

### 46. FEYNMAN DIAGRAM (QED)
- **Domain:** Fundamental Physics (Particle Physics)
- **Symbol/Shape:** Two straight electron paths converging, exchanging a squiggly photon, and repelling.
- **Color:** `#1E90FF` (Dodger Blue)
- **Idle Animation:** The particles flow in along the time axis, the photon ripples across the vertex, and they scatter away.
- **Click Disappearance Motion:** A virtual particle loop goes out of control; an infinite series of loops spawns, turning the diagram into fractal static.
- **Physics Basis:** Quantum Electrodynamics, visually representing the mathematical expressions governing the behavior of subatomic particles.

---

# PART 5 — ADDENDUM (COMPLETENESS GAPS)

---

### 267. COMPUTATIONAL COMPLEXITY (BIG O)
- **Domain:** Computer Science (Algorithms)
- **Symbol/Shape:** A miniature line graph with an exponential curve (red) and a logarithmic curve (green).
- **Color:** `#E74C3C` (Exponential Red)
- **Idle Animation:** A small processing dot races along the green curve smoothly, while another dot struggles slowly up the steep red curve.
- **Click Disappearance Motion:** The input size (x-axis) suddenly approaches infinity; the exponential curve explodes upwards past the screen boundary, dragging the entire graph with it until it snaps.
- **Physics Basis:** Mathematical bounds of algorithmic efficiency and resource scaling.

### 268. RADIOACTIVE DECAY SERIES
- **Domain:** Nuclear Engineering (Radioactivity)
- **Symbol/Shape:** A stepping-stone path descending diagonally across a tiny N-Z (neutron-proton) grid.
- **Color:** `#FF4500` (Decay Orange)
- **Idle Animation:** A heavy nucleus jumps down the steps, changing color and emitting tiny alpha/beta particles at each step.
- **Click Disappearance Motion:** The nucleus finally hits the stable "lead" square at the bottom, solidifies into a heavy, unmoving block, and immediately sinks through the bottom of the screen.
- **Physics Basis:** Secular equilibrium and sequential transmutation of unstable isotopes into stable elements.

### 269. SYSTEM DYNAMICS (CAUSAL LOOP)
- **Domain:** Systems Engineering
- **Symbol/Shape:** A figure-eight loop of arrows with '+' (reinforcing) and '-' (balancing) nodes.
- **Color:** `#8E44AD` (Systems Purple)
- **Idle Animation:** Energy pulses flow around the loop; the '+' node accelerates them, while the '-' node smoothly acts as a governor to maintain steady state.
- **Click Disappearance Motion:** The balancing node fails; the reinforcing loop spirals out of control, spinning faster and faster until the loop tears itself apart into flying arrows.
- **Physics Basis:** Non-linear feedback control theory and macro-system interconnectedness.

### 270. FAULT TREE ANALYSIS (FTA)
- **Domain:** Systems/Safety Engineering
- **Symbol/Shape:** A top-down logic tree with AND/OR gates leading to a central "Top Event" hazard box.
- **Color:** `#C0392B` (Hazard Red)
- **Idle Animation:** Tiny red fault signals sporadically trickle up from the bottom leaves but are stopped by functioning AND gates.
- **Click Disappearance Motion:** A perfect storm of simultaneous bottom-level faults perfectly aligns through all gates, triggering the "Top Event" box which flashes blindingly and melts down the entire screen.
- **Physics Basis:** Probabilistic risk assessment, Boolean logic failure pathways, and redundancy.
