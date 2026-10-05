// Electrodynamics — Universal University Standard Textbook Edition
// Complete, rigorous, comprehensive academic chapters with inline topic simulations.

window.COURSE_DATA = {
  "courseCode": "PHYSICS",
  "courseTitle": "Electrodynamics",
  "edition": "Interactive Digital Textbook Edition",
  "textbookTitle": "Principles of Classical Electrodynamics: Field Equations, Wave Propagation, Radiation & Dispersion",
  "author": "OpenSTEM Academic Press",
  "units": [
    {
      "id": "unit-1",
      "number": 1,
      "title": "Electromagnetic Field Equations & Conservation Laws",
      "leadSummary": "Comprehensive formulation of classical field theory: the breakdown and inconsistency of Ampère's circuital law for non-steady currents, Maxwell's hypothesis of displacement current, charge conservation via the equation of continuity, the complete Maxwell equations in differential and integral forms across free space and material media, the rigorous vector derivation of Poynting's theorem, electromagnetic momentum density, and radiation pressure.",
      "simulations": [
        "displacement-current",
        "poynting-vector"
      ],
      "sections": [
        {
          "secNumber": "1.1",
          "heading": "Inadequacy of Ampère's Circuital Law and the Capacitor Paradox",
          "content": "\nBefore the revolutionary theoretical synthesis by James Clerk Maxwell (1861–1865), classical electromagnetism was formulated through empirical laws developed primarily for static or steady-state conditions:\n\n1. **Gauss's Law for Electrostatics:** $\\nabla \\cdot \\mathbf{E} = \\frac{\\rho}{\\epsilon_0}$\n2. **Gauss's Law for Magnetism:** $\\nabla \\cdot \\mathbf{B} = 0$\n3. **Faraday's Law of Electromagnetic Induction:** $\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$\n4. **Ampère's Circuital Law:** $\\nabla \\times \\mathbf{B} = \\mu_0 \\mathbf{J}$\n\n#### The Fundamental Mathematical Contradiction\nIn vector calculus, the divergence of any curl of a vector field identically vanishes. Applying the divergence operator to both sides of Ampère's law yields:\n$$\\nabla \\cdot (\\nabla \\times \\mathbf{B}) = \\mu_0 (\\nabla \\cdot \\mathbf{J})$$\nSince $\\nabla \\cdot (\\nabla \\times \\mathbf{A}) \\equiv 0$ for any twice-differentiable vector field $\\mathbf{A}$, the left-hand side is identically zero:\n$$0 = \\mu_0 (\\nabla \\cdot \\mathbf{J}) \\implies \\nabla \\cdot \\mathbf{J} = 0$$\n\nHowever, the fundamental law of **Conservation of Electric Charge** requires that the divergence of the current density equals the negative rate of charge accumulation, as stated by the **Continuity Equation**:\n$$\\nabla \\cdot \\mathbf{J} + \\frac{\\partial \\rho}{\\partial t} = 0 \\implies \\nabla \\cdot \\mathbf{J} = -\\frac{\\partial \\rho}{\\partial t}$$\n\nAmpère's circuital law is therefore mathematically incompatible with the conservation of charge whenever the charge density varies with time ($\\partial \\rho / \\partial t \\neq 0$). Ampère's law holds strictly for steady currents (magnetostatics) where $\\partial \\rho / \\partial t = 0$, but fails catastrophically for time-dependent circuits.\n\n#### The Physical Gedankenexperiment: The Capacitor Paradox\nConsider a circular parallel-plate capacitor being charged by a steady current $I(t)$ flowing through a connecting wire. Draw a closed loop $C$ encircling the wire. By Stokes' theorem, the line integral of $\\mathbf{B}$ around $C$ equals the surface integral of current density through any open surface $S$ bounded by $C$:\n$$\\oint_C \\mathbf{B} \\cdot d\\mathbf{l} = \\mu_0 \\int_S \\mathbf{J} \\cdot d\\mathbf{a} = \\mu_0 I_{\\text{enc}}$$\n\n- **Surface $S_1$ (Flat Disk):** Choose a flat circular disk bounded by $C$. The conducting wire pierces $S_1$, so the enclosed current is $I_{\\text{enc}} = I$, giving $\\oint_C \\mathbf{B} \\cdot d\\mathbf{l} = \\mu_0 I$.\n- **Surface $S_2$ (Balloon/Bowl Shape):** Bulge the surface out like a balloon so that it passes entirely between the capacitor plates without touching the wire. Since no conduction current passes through the vacuum gap between the plates, $I_{\\text{enc}} = 0$, giving $\\oint_C \\mathbf{B} \\cdot d\\mathbf{l} = 0$.\n\nBecause the line integral $\\oint_C \\mathbf{B} \\cdot d\\mathbf{l}$ around the exact same physical curve $C$ cannot depend on the arbitrary mathematical choice of surface $S$, classical electrodynamics faced an irreconcilable paradox.\n"
        },
        {
          "secNumber": "1.2",
          "heading": "Maxwell's Displacement Current and the Equation of Continuity",
          "content": "\n#### The Displacement Current Derivation\nTo resolve the contradiction, Maxwell proposed adding a missing current density term, $\\mathbf{J}_d$ (the **displacement current density**), to Ampère's equation:\n$$\\nabla \\times \\mathbf{B} = \\mu_0 (\\mathbf{J} + \\mathbf{J}_d)$$\n\nTaking the divergence of both sides:\n$$\\nabla \\cdot (\\nabla \\times \\mathbf{B}) = 0 = \\mu_0 \\left( \\nabla \\cdot \\mathbf{J} + \\nabla \\cdot \\mathbf{J}_d \\right)$$\n$$\\nabla \\cdot \\mathbf{J}_d = -\\nabla \\cdot \\mathbf{J}$$\n\nUsing the continuity equation $\\nabla \\cdot \\mathbf{J} = -\\frac{\\partial \\rho}{\\partial t}$:\n$$\\nabla \\cdot \\mathbf{J}_d = \\frac{\\partial \\rho}{\\partial t}$$\n\nNow, substitute Gauss's law $\\rho = \\epsilon_0 (\\nabla \\cdot \\mathbf{E})$:\n$$\\nabla \\cdot \\mathbf{J}_d = \\frac{\\partial}{\\partial t} \\left( \\epsilon_0 \\nabla \\cdot \\mathbf{E} \\right) = \\nabla \\cdot \\left( \\epsilon_0 \\frac{\\partial \\mathbf{E}}{\\partial t} \\right)$$\n\nEquating the vector terms under the divergence yields Maxwell's formulation for the **displacement current density in free space**:\n$$\\mathbf{J}_d = \\epsilon_0 \\frac{\\partial \\mathbf{E}}{\\partial t}$$\n\n#### Total Current in the Capacitor Gap\nThe total displacement current $I_d$ passing through the cross-sectional area $A$ between the capacitor plates is:\n$$I_d = \\int_A \\mathbf{J}_d \\cdot d\\mathbf{a} = \\epsilon_0 \\frac{d}{dt} \\int_A \\mathbf{E} \\cdot d\\mathbf{a} = \\epsilon_0 \\frac{d\\Phi_E}{dt}$$\nwhere $\\Phi_E$ is the electric flux. For a parallel-plate capacitor with plate charge $Q(t)$ and plate area $A$:\n$$E(t) = \\frac{\\sigma(t)}{\\epsilon_0} = \\frac{Q(t)}{\\epsilon_0 A} \\implies \\Phi_E(t) = E(t) A = \\frac{Q(t)}{\\epsilon_0}$$\nDifferentiating with respect to time:\n$$I_d = \\epsilon_0 \\frac{d}{dt} \\left( \\frac{Q(t)}{\\epsilon_0} \\right) = \\frac{dQ}{dt} = I_c(t)$$\n\nThus, the displacement current $I_d$ between the plates is **identically equal** to the conduction current $I_c$ flowing in the external circuit wires. The total current $I_{\\text{tot}} = I_c + I_d$ is perfectly continuous everywhere in the circuit, completely eliminating the capacitor paradox.\n",
          "simulation": "displacement-current"
        },
        {
          "secNumber": "1.3",
          "heading": "The Complete System of Maxwell's Equations (Differential & Integral Forms)",
          "content": "\nThe addition of the displacement current term completed the classical theory of electrodynamics. Maxwell's equations describe the behavior of macroscopic and microscopic electromagnetic fields in terms of charge densities $\\rho$ and current densities $\\mathbf{J}$.\n\n#### Maxwell's Equations in Vacuum (Microscopic Form)\n\n| Physical Law | Differential Equation | Integral Equation | Physical Meaning |\n| :--- | :--- | :--- | :--- |\n| **Gauss's Law for $\\mathbf{E}$** | $\\nabla \\cdot \\mathbf{E} = \\frac{\\rho}{\\epsilon_0}$ | $\\oint_S \\mathbf{E} \\cdot d\\mathbf{a} = \\frac{Q_{\\text{enc}}}{\\epsilon_0}$ | Electric field flux through a closed surface is proportional to the enclosed electric charge. Electric field lines originate on positive charges and terminate on negative charges. |\n| **Gauss's Law for $\\mathbf{B}$** | $\\nabla \\cdot \\mathbf{B} = 0$ | $\\oint_S \\mathbf{B} \\cdot d\\mathbf{a} = 0$ | Magnetic fields are solenoidal; magnetic monopoles do not exist in classical physics. Magnetic field lines form continuous closed loops without sources or sinks. |\n| **Faraday's Law of Induction** | $\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$ | $\\oint_C \\mathbf{E} \\cdot d\\mathbf{l} = -\\frac{d\\Phi_B}{dt}$ | A time-varying magnetic flux induces a non-conservative, curling electric field (electromotive force, EMF). |\n| **Ampère-Maxwell Law** | $\\nabla \\times \\mathbf{B} = \\mu_0 \\mathbf{J} + \\mu_0 \\epsilon_0 \\frac{\\partial \\mathbf{E}}{\\partial t}$ | $\\oint_C \\mathbf{B} \\cdot d\\mathbf{l} = \\mu_0 I_{\\text{enc}} + \\mu_0 \\epsilon_0 \\frac{d\\Phi_E}{dt}$ | Magnetic fields are generated by both conduction electric currents and time-varying electric flux (displacement current). |\n\n#### Maxwell's Equations in Matter (Macroscopic Form)\nIn material media, charges and currents are split into **free** charges/currents (conducted electrons, free ions: $\\rho_f, \\mathbf{J}_f$) and **bound** charges/currents arising from dielectric polarization $\\mathbf{P}$ and magnetization $\\mathbf{M}$:\n$$\\rho_b = -\\nabla \\cdot \\mathbf{P}, \\quad \\mathbf{J}_b = \\nabla \\times \\mathbf{M}, \\quad \\mathbf{J}_p = \\frac{\\partial \\mathbf{P}}{\\partial t}$$\n\nDefining the auxiliary fields:\n- **Electric Displacement:** $\\mathbf{D} \\equiv \\epsilon_0 \\mathbf{E} + \\mathbf{P}$\n- **Magnetic Field Intensity:** $\\mathbf{H} \\equiv \\frac{1}{\\mu_0} \\mathbf{B} - \\mathbf{M}$\n\nThe macroscopic Maxwell equations take the form:\n1. $\\nabla \\cdot \\mathbf{D} = \\rho_f$\n2. $\\nabla \\cdot \\mathbf{B} = 0$\n3. $\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$\n4. $\\nabla \\times \\mathbf{H} = \\mathbf{J}_f + \\frac{\\partial \\mathbf{D}}{\\partial t}$\n\nFor linear, isotropic, and homogeneous media:\n$$\\mathbf{D} = \\epsilon \\mathbf{E} = \\epsilon_r \\epsilon_0 \\mathbf{E}, \\quad \\mathbf{B} = \\mu \\mathbf{H} = \\mu_r \\mu_0 \\mathbf{H}$$\n"
        },
        {
          "secNumber": "1.4",
          "heading": "Physical Significance, Symmetry, and Non-Existence of Magnetic Monopoles",
          "content": "\n#### The Dynamic Cross-Coupling of Fields\nA critical insight of Maxwell's equations is the mutual interdependence of electric and magnetic fields in time-dependent situations:\n$$\\frac{\\partial \\mathbf{B}}{\\partial t} \\neq 0 \\implies \\nabla \\times \\mathbf{E} \\neq 0 \\quad \\text{and} \\quad \\frac{\\partial \\mathbf{E}}{\\partial t} \\neq 0 \\implies \\nabla \\times \\mathbf{B} \\neq 0$$\nEven in a pure vacuum with zero charges ($\\rho = 0$) and zero currents ($\\mathbf{J} = 0$), a changing magnetic field creates an electric field, and that changing electric field in turn generates a magnetic field. This self-sustaining, reciprocal generation allows electromagnetic disturbances to detach from their sources and propagate across infinite distances through empty space as **electromagnetic radiation**.\n\n#### Asymmetry and Magnetic Monopoles\nNotice the apparent asymmetry between electricity and magnetism:\n$$\\nabla \\cdot \\mathbf{E} = \\frac{\\rho_e}{\\epsilon_0}, \\quad \\nabla \\cdot \\mathbf{B} = 0$$\n$$\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}, \\quad \\nabla \\times \\mathbf{B} = \\mu_0 \\mathbf{J}_e + \\frac{1}{c^2} \\frac{\\partial \\mathbf{E}}{\\partial t}$$\n\nIf magnetic monopoles existed in nature with magnetic charge density $\\rho_m$ and magnetic current density $\\mathbf{J}_m$, Maxwell's equations would achieve perfect dual symmetry:\n$$\\nabla \\cdot \\mathbf{E} = \\frac{\\rho_e}{\\epsilon_0}, \\quad \\nabla \\cdot \\mathbf{B} = \\mu_0 \\rho_m$$\n$$\\nabla \\times \\mathbf{E} = -\\mu_0 \\mathbf{J}_m - \\frac{\\partial \\mathbf{B}}{\\partial t}, \\quad \\nabla \\times \\mathbf{B} = \\mu_0 \\mathbf{J}_e + \\frac{1}{c^2} \\frac{\\partial \\mathbf{E}}{\\partial t}$$\n\nDespite extensive experimental searches in particle colliders, cosmic rays, and lunar rock samples, no isolated magnetic monopole has ever been conclusively observed. Paul Dirac proved in 1931 that the existence of even a single magnetic monopole anywhere in the universe would explain the quantization of electric charge:\n$$q_e q_m = 2\\pi n \\hbar, \\quad n \\in \\mathbb{Z}$$\n"
        },
        {
          "secNumber": "1.5",
          "heading": "Energy Considerations: Poynting's Theorem & Electromagnetic Energy Flux",
          "content": "\n#### Step-by-Step Mathematical Derivation of Poynting's Theorem\nThe work done by electromagnetic forces on a distribution of charges in volume $V$ is governed by the Lorentz force law. The mechanical work per unit time (power) delivered to the charges is:\n$$\\frac{dW_{\\text{mech}}}{dt} = \\int_V (\\mathbf{F} \\cdot \\mathbf{v}) dq = \\int_V \\mathbf{E} \\cdot \\mathbf{J} \\, d\\tau$$\nwhere $d\\tau$ is the differential volume element.\n\nTo express $\\mathbf{E} \\cdot \\mathbf{J}$ in terms of field quantities alone, solve for $\\mathbf{J}$ using the Ampère-Maxwell law:\n$$\\mathbf{J} = \\frac{1}{\\mu_0} (\\nabla \\times \\mathbf{B}) - \\epsilon_0 \\frac{\\partial \\mathbf{E}}{\\partial t}$$\n\nDot both sides with $\\mathbf{E}$:\n$$\\mathbf{E} \\cdot \\mathbf{J} = \\frac{1}{\\mu_0} \\mathbf{E} \\cdot (\\nabla \\times \\mathbf{B}) - \\epsilon_0 \\mathbf{E} \\cdot \\frac{\\partial \\mathbf{E}}{\\partial t}$$\n\nRecall the fundamental vector calculus product rule:\n$$\\nabla \\cdot (\\mathbf{E} \\times \\mathbf{B}) = \\mathbf{B} \\cdot (\\nabla \\times \\mathbf{E}) - \\mathbf{E} \\cdot (\\nabla \\times \\mathbf{B})$$\n$$\\mathbf{E} \\cdot (\\nabla \\times \\mathbf{B}) = \\mathbf{B} \\cdot (\\nabla \\times \\mathbf{E}) - \\nabla \\cdot (\\mathbf{E} \\times \\mathbf{B})$$\n\nSubstitute Faraday's law $\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$:\n$$\\mathbf{E} \\cdot (\\nabla \\times \\mathbf{B}) = -\\mathbf{B} \\cdot \\frac{\\partial \\mathbf{B}}{\\partial t} - \\nabla \\cdot (\\mathbf{E} \\times \\mathbf{B})$$\n\nNow, observe that:\n$$\\mathbf{E} \\cdot \\frac{\\partial \\mathbf{E}}{\\partial t} = \\frac{1}{2} \\frac{\\partial}{\\partial t}(E^2), \\quad \\mathbf{B} \\cdot \\frac{\\partial \\mathbf{B}}{\\partial t} = \\frac{1}{2} \\frac{\\partial}{\\partial t}(B^2)$$\n\nSubstituting these identities back into the expression for $\\mathbf{E} \\cdot \\mathbf{J}$:\n$$\\mathbf{E} \\cdot \\mathbf{J} = -\\frac{1}{2} \\frac{\\partial}{\\partial t} \\left( \\epsilon_0 E^2 + \\frac{1}{\\mu_0} B^2 \\right) - \\frac{1}{\\mu_0} \\nabla \\cdot (\\mathbf{E} \\times \\mathbf{B})$$\n\n#### Definitions of the Field Quantities\n1. **Electromagnetic Energy Density ($u$):**\n$$u \\equiv \\frac{1}{2} \\left( \\epsilon_0 E^2 + \\frac{1}{\\mu_0} B^2 \\right) \\quad [\\text{Joules} / \\text{m}^3]$$\n\n2. **The Poynting Vector ($\\mathbf{S}$):**\n$$\\mathbf{S} \\equiv \\frac{1}{\\mu_0} (\\mathbf{E} \\times \\mathbf{B}) \\quad [\\text{Watts} / \\text{m}^2]$$\nThe Poynting vector represents the directional rate of electromagnetic energy transfer per unit area.\n\n#### Differential Form of Poynting's Theorem\n$$-\\frac{\\partial u}{\\partial t} = \\nabla \\cdot \\mathbf{S} + \\mathbf{E} \\cdot \\mathbf{J}$$\nor in conservation law form:\n$$\\frac{\\partial u}{\\partial t} + \\nabla \\cdot \\mathbf{S} = -\\mathbf{E} \\cdot \\mathbf{J}$$\n\n#### Integral Form of Poynting's Theorem\nIntegrating over a finite volume $V$ bounded by closed surface $S$ and applying Gauss's divergence theorem:\n$$-\\frac{d}{dt} \\int_V u \\, d\\tau = \\oint_S \\mathbf{S} \\cdot d\\mathbf{a} + \\int_V (\\mathbf{E} \\cdot \\mathbf{J}) \\, d\\tau$$\n\n**Physical Interpretation:** The time rate of decrease of electromagnetic energy stored in volume $V$ equals the total power radiated outward across the boundary surface $S$ plus the rate of work done on the charges inside $V$ (such as Ohmic Joule heating $\\mathbf{J} \\cdot \\mathbf{E} = \\sigma E^2$).\n",
          "simulation": "poynting-vector"
        },
        {
          "secNumber": "1.6",
          "heading": "Momentum of the Electromagnetic Field, Maxwell Stress Tensor & Radiation Pressure",
          "content": "\n#### Electromagnetic Momentum Density\nElectromagnetic fields carry not only energy, but also linear momentum. By applying the Lorentz force equation to volume charges, one derives the total momentum balance:\n$$\\frac{d}{dt} (\\mathbf{p}_{\\text{mech}} + \\mathbf{p}_{\\text{field}}) = 0$$\n\nThe **electromagnetic momentum density** $\\mathbf{g}$ stored in the fields is directly proportional to the Poynting vector:\n$$\\mathbf{g} = \\epsilon_0 (\\mathbf{E} \\times \\mathbf{B}) = \\frac{\\mathbf{S}}{c^2} \\quad [\\text{kg} / (\\text{m}^2 \\cdot \\text{s})]$$\n\n#### The Maxwell Stress Tensor\nThe spatial flow of momentum is described by the **Maxwell stress tensor** $\\overleftrightarrow{\\mathbf{T}}$, a rank-2 symmetric tensor with components:\n$$T_{ij} \\equiv \\epsilon_0 \\left( E_i E_j - \\frac{1}{2} \\delta_{ij} E^2 \\right) + \\frac{1}{\\mu_0} \\left( B_i B_j - \\frac{1}{2} \\delta_{ij} B^2 \\right)$$\nwhere $\\delta_{ij}$ is the Kronecker delta. The electromagnetic force per unit volume is given by:\n$$\\mathbf{f} = \\nabla \\cdot \\overleftrightarrow{\\mathbf{T}} - \\epsilon_0 \\mu_0 \\frac{\\partial \\mathbf{S}}{\\partial t}$$\n\n#### Radiation Pressure\nWhen an electromagnetic wave impinges on a physical surface, it transfers linear momentum to the matter, exerting a mechanical pressure known as **radiation pressure** ($P_{\\text{rad}}$).\n\nLet the incident wave carry intensity $I = \\langle S \\rangle = c \\langle u \\rangle$:\n\n1. **Total Absorption (Perfect Blackbody Surface):**\nAll incident momentum is transferred to the surface:\n$$P_{\\text{rad}} = \\frac{\\langle S \\rangle}{c} = \\langle u \\rangle = \\frac{I}{c}$$\n\n2. **Total Reflection (Ideal Conducting Mirror):**\nThe reflected wave has reversed momentum ($\\Delta p = p_{\\text{final}} - p_{\\text{initial}} = -p - p = -2p$). By Newton's third law, the impulse delivered to the surface is doubled:\n$$P_{\\text{rad}} = \\frac{2 \\langle S \\rangle}{c} = 2 \\langle u \\rangle = \\frac{2I}{c}$$\n\n3. **Oblique Incidence at Angle $\\theta$:**\n$$P_{\\text{rad}} = \\frac{I}{c} (1 + R) \\cos^2\\theta$$\nwhere $R$ is the surface reflection coefficient ($R=0$ for complete absorption, $R=1$ for total reflection).\n",
          "simulation": "radiation-pressure-sim"
        }
      ],
      "problems": [
        {
          "id": "p1-1",
          "title": "Example 1.1: Complete Field and Displacement Current Distribution in a Circular Capacitor",
          "difficulty": "Medium",
          "question": "A parallel-plate capacitor consists of circular plates of radius $R$ separated by distance $d$. It is charged by a constant current $I$. Determine: (a) the electric field $E(t)$ between the plates, (b) the displacement current density $J_d$ and total displacement current $I_d$, (c) the induced magnetic field $B(r)$ at radial distance $r$ from the axis for both $r \\le R$ and $r > R$, and (d) verify the continuity of $B$ at $r = R$.",
          "steps": [
            {
              "stepName": "Step 1: Electric Field and Displacement Current Density",
              "math": "Q(t) = I t \\implies \\sigma(t) = \\frac{I t}{\\pi R^2} \\implies E(t) = \\frac{\\sigma(t)}{\\epsilon_0} = \\frac{I t}{\\epsilon_0 \\pi R^2}\\nJ_d = \\epsilon_0 \\frac{\\partial E}{\\partial t} = \\epsilon_0 \\frac{d}{dt}\\left( \\frac{I t}{\\epsilon_0 \\pi R^2} \\right) = \\frac{I}{\\pi R^2}\\nI_d = \\int_0^R J_d (2\\pi r dr) = \\frac{I}{\\pi R^2} (\\pi R^2) = I",
              "explanation": "The displacement current density is completely uniform across the entire plate area, and its surface integral yields exactly $I$, proving current continuity across the dielectric gap."
            },
            {
              "stepName": "Step 2: Induced Magnetic Field Inside the Plates (r <= R)",
              "math": "\\oint_C \\mathbf{B} \\cdot d\\mathbf{l} = \\mu_0 I_{d,\\text{enc}} = \\mu_0 \\int_0^r J_d (2\\pi r' dr') = \\mu_0 \\left(\\frac{I}{\\pi R^2}\\right) (\\pi r^2) = \\mu_0 I \\frac{r^2}{R^2}\\nB(2\\pi r) = \\mu_0 I \\frac{r^2}{R^2} \\implies B(r) = \\frac{\\mu_0 I r}{2\\pi R^2} \\quad (r \\le R)",
              "explanation": "Inside the gap, the magnetic field increases linearly with radial distance $r$, starting from zero at the central axis."
            },
            {
              "stepName": "Step 3: Induced Magnetic Field Outside the Plates (r > R)",
              "math": "\\oint_C \\mathbf{B} \\cdot d\\mathbf{l} = \\mu_0 I_{d,\\text{total}} = \\mu_0 I\\nB(2\\pi r) = \\mu_0 I \\implies B(r) = \\frac{\\mu_0 I}{2\\pi r} \\quad (r > R)",
              "explanation": "Outside the plates, the magnetic field is identical to that produced by a continuous, infinitely long straight wire carrying current $I$."
            },
            {
              "stepName": "Step 4: Boundary Matching at r = R",
              "math": "B(R^-) = \\frac{\\mu_0 I R}{2\\pi R^2} = \\frac{\\mu_0 I}{2\\pi R}, \\quad B(R^+) = \\frac{\\mu_0 I}{2\\pi R}",
              "explanation": "The magnetic field is continuous across $r=R$, with a maximum value of $B_{\\text{max}} = \\frac{\\mu_0 I}{2\\pi R}$."
            }
          ]
        },
        {
          "id": "p1-2",
          "title": "Example 1.2: Radial Poynting Energy Flow in a Current-Carrying Resistive Wire",
          "difficulty": "Hard",
          "question": "A cylindrical ohmic wire of length $L$, radius $a$, and conductivity $\\sigma$ carries a steady uniform DC current $I$. Calculate: (a) the electric field $\\mathbf{E}$ inside and on the surface of the wire, (b) the magnetic field $\\mathbf{B}$ at the wire surface, (c) the direction and magnitude of the Poynting vector $\\mathbf{S}$ at the surface, and (d) integrate $\\mathbf{S}$ over the wire surface to demonstrate that electromagnetic field energy flows into the wire to supply Joule heating.",
          "steps": [
            {
              "stepName": "Step 1: Surface Electric and Magnetic Fields",
              "math": "J = \\frac{I}{\\pi a^2} \\implies \\mathbf{E} = \\frac{\\mathbf{J}}{\\sigma} = \\frac{I}{\\sigma \\pi a^2} \\hat{\\mathbf{z}}\\n\\oint \\mathbf{B} \\cdot d\\mathbf{l} = \\mu_0 I \\implies B(a)(2\\pi a) = \\mu_0 I \\implies \\mathbf{B}(a) = \\frac{\\mu_0 I}{2\\pi a} \\hat{\\boldsymbol{\\phi}}",
              "explanation": "The electric field points along the length of the wire (axial $\\hat{\\mathbf{z}}$), while the magnetic field curls azimuthally (tangential $\\hat{\\boldsymbol{\\phi}}$)."
            },
            {
              "stepName": "Step 2: Poynting Vector Computation",
              "math": "\\mathbf{S} = \\frac{1}{\\mu_0} (\\mathbf{E} \\times \\mathbf{B}) = \\frac{1}{\\mu_0} \\left( \\frac{I}{\\sigma \\pi a^2} \\hat{\\mathbf{z}} \\times \\frac{\\mu_0 I}{2\\pi a} \\hat{\\boldsymbol{\\phi}} \\right) = -\\frac{I^2}{2\\pi^2 \\sigma a^3} \\hat{\\mathbf{r}}",
              "explanation": "Since $\\hat{\\mathbf{z}} \\times \\hat{\\boldsymbol{\\phi}} = -\\hat{\\mathbf{r}}$, the Poynting vector points radially INWARD into the wire from the surrounding space."
            },
            {
              "stepName": "Step 3: Surface Integration and Joule Dissipation",
              "math": "P_{\\text{in}} = -\\oint \\mathbf{S} \\cdot d\\mathbf{a} = |S| (2\\pi a L) = \\left( \\frac{I^2}{2\\pi^2 \\sigma a^3} \\right) (2\\pi a L) = I^2 \\left( \\frac{L}{\\sigma \\pi a^2} \\right) = I^2 R",
              "explanation": "Energy does not flow down the wire inside the conductor like a fluid; rather, electrical energy travels through the electromagnetic field outside the wire and enters radially through the outer surface to be dissipated as thermal Joule heat $I^2 R$."
            }
          ]
        },
        {
          "id": "p1-3",
          "title": "Example 1.3: Electromagnetic Energy Transport in a Coaxial Cable",
          "difficulty": "Hard",
          "question": "A coaxial cable consists of an inner solid conductor of radius $a$ at potential $V$ carrying current $I$ in the $+z$ direction, and a thin outer coaxial cylindrical shell of radius $b$ at potential $0$ carrying the return current $I$ in the $-z$ direction. Calculate: (a) $\\mathbf{E}$ and $\\mathbf{B}$ in the insulating region $a < r < b$, (b) the Poynting vector $\\mathbf{S}(r)$, and (c) the total power transported along the cable by integrating $\\mathbf{S}$ over the annular cross section.",
          "steps": [
            {
              "stepName": "Step 1: Field Distributions in the Annular Gap",
              "math": "\\mathbf{E}(r) = \\frac{V}{\\ln(b/a)} \\frac{1}{r} \\hat{\\mathbf{r}}, \\quad \\mathbf{B}(r) = \\frac{\\mu_0 I}{2\\pi r} \\hat{\\boldsymbol{\\phi}}",
              "explanation": "Gauss's law gives the radial electrostatic field, and Ampère's circuital law gives the azimuthal magnetic field."
            },
            {
              "stepName": "Step 2: Poynting Vector in the Dielectric",
              "math": "\\mathbf{S} = \\frac{1}{\\mu_0} (\\mathbf{E} \\times \\mathbf{B}) = \\frac{1}{\\mu_0} \\left( \\frac{V}{\\ln(b/a)} \\frac{1}{r} \\hat{\\mathbf{r}} \\times \\frac{\\mu_0 I}{2\\pi r} \\hat{\\boldsymbol{\\phi}} \\right) = \\frac{V I}{2\\pi \\ln(b/a)} \\frac{1}{r^2} \\hat{\\mathbf{z}}",
              "explanation": "Because $\\hat{\\mathbf{r}} \\times \\hat{\\boldsymbol{\\phi}} = \\hat{\\mathbf{z}}$, the energy flux flows purely along the $+z$ direction parallel to the cable axis through the insulating dielectric."
            },
            {
              "stepName": "Step 3: Total Power Transmission",
              "math": "P = \\int_{r=a}^b \\mathbf{S} \\cdot d\\mathbf{a} = \\int_a^b \\left( \\frac{V I}{2\\pi \\ln(b/a)} \\frac{1}{r^2} \\right) (2\\pi r dr) = \\frac{V I}{\\ln(b/a)} \\int_a^b \\frac{dr}{r} = \\frac{V I}{\\ln(b/a)} [\\ln(b/a)] = V I",
              "explanation": "The integrated Poynting flux equals precisely $P = VI$, proving that electric circuit power is transported entirely through the electromagnetic field in the dielectric space surrounding the conductors."
            }
          ]
        },
        {
          "id": "p1-4",
          "title": "Example 1.4: Solar Radiation Pressure and Spacecraft Solar Sail Propulsion",
          "difficulty": "Medium",
          "question": "The solar radiation flux (solar constant) reaching Earth's orbit at distance $R_E = 1.496 \\times 10^{11}\\text{ m}$ is $I_0 = 1361\\text{ W/m}^2$. A solar sail spacecraft with mass $m = 250\\text{ kg}$ deploys an ultra-reflective flat sail of area $A = 10^4\\text{ m}^2$ (reflectance $R = 0.98$). Calculate: (a) the radiation pressure on the sail at normal incidence, (b) the total repulsive radiation force exerted on the spacecraft, and (c) the initial acceleration imparted to the spacecraft.",
          "steps": [
            {
              "stepName": "Step 1: Radiation Pressure Calculation",
              "math": "P_{\\text{rad}} = \\frac{I_0}{c} (1 + R) = \\frac{1361\\text{ W/m}^2}{3.00 \\times 10^8\\text{ m/s}} (1 + 0.98) = (4.537 \\times 10^{-6}\\text{ N/m}^2) \\times 1.98 = 8.983 \\times 10^{-6}\\text{ N/m}^2",
              "explanation": "The reflected photons deliver momentum $\\Delta p = 2p$, so near-perfect reflectance nearly doubles the thrust compared to an absorbing sail."
            },
            {
              "stepName": "Step 2: Total Radiation Force",
              "math": "F_{\\text{rad}} = P_{\\text{rad}} \\times A = (8.983 \\times 10^{-6}\\text{ N/m}^2) \\times (10^4\\text{ m}^2) = 0.0898\\text{ N} \\approx 0.090\\text{ N}",
              "explanation": "A $100\\text{ m} \\times 100\\text{ m}$ sail intercepts over 13 megawatts of solar photon beam power, yielding roughly 0.09 Newtons of continuous fuel-free thrust."
            },
            {
              "stepName": "Step 3: Initial Acceleration",
              "math": "a = \\frac{F_{\\text{rad}}}{m} = \\frac{0.0898\\text{ N}}{250\\text{ kg}} = 3.59 \\times 10^{-4}\\text{ m/s}^2",
              "explanation": "Although the acceleration is small ($0.36\\text{ mm/s}^2$), because it acts continuously without fuel consumption, the spacecraft gains over $31\\text{ m/s}$ ($112\\text{ km/h}$) of velocity every single day."
            }
          ]
        }
      ]
    },
    {
      "id": "unit-2",
      "number": 2,
      "title": "Propagation of Electromagnetic Waves in Media & Plasmas",
      "leadSummary": "Rigorous analytical treatment of classical electromagnetic wave propagation: the vector wave equation derivation from Maxwell's field equations, monochromatic plane waves, orthogonality and transverse nature of electric and magnetic fields, intrinsic wave impedance of free space, lossy propagation in conducting media, attenuation constant, skin depth and phase delay in metals, and dispersion relations and plasma cutoff frequencies in ionized gases.",
      "simulations": [
        "em-wave-3d",
        "skin-depth"
      ],
      "sections": [
        {
          "secNumber": "2.1",
          "heading": "The Electromagnetic Wave Equations in Vacuum & Media",
          "content": "\n#### Derivation of the Vector Wave Equation\nConsider source-free vacuum where charge density $\\rho = 0$ and conduction current density $\\mathbf{J} = 0$. Maxwell's equations reduce to:\n1. $\\nabla \\cdot \\mathbf{E} = 0$\n2. $\\nabla \\cdot \\mathbf{B} = 0$\n3. $\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$\n4. $\\nabla \\times \\mathbf{B} = \\mu_0 \\epsilon_0 \\frac{\\partial \\mathbf{E}}{\\partial t}$\n\nTo decouple these coupled first-order partial differential equations, take the curl of Faraday's law:\n$$\\nabla \\times (\\nabla \\times \\mathbf{E}) = -\\nabla \\times \\left( \\frac{\\partial \\mathbf{B}}{\\partial t} \\right) = -\\frac{\\partial}{\\partial t} (\\nabla \\times \\mathbf{B})$$\n\nUsing the fundamental vector identity $\\nabla \\times (\\nabla \\times \\mathbf{A}) \\equiv \\nabla(\\nabla \\cdot \\mathbf{A}) - \\nabla^2 \\mathbf{A}$ on the left-hand side:\n$$\\nabla(\\nabla \\cdot \\mathbf{E}) - \\nabla^2 \\mathbf{E} = -\\frac{\\partial}{\\partial t} (\\nabla \\times \\mathbf{B})$$\n\nSince $\\nabla \\cdot \\mathbf{E} = 0$ in vacuum, and substituting Ampère-Maxwell's law for $\\nabla \\times \\mathbf{B}$:\n$$-\\nabla^2 \\mathbf{E} = -\\frac{\\partial}{\\partial t} \\left( \\mu_0 \\epsilon_0 \\frac{\\partial \\mathbf{E}}{\\partial t} \\right) = -\\mu_0 \\epsilon_0 \\frac{\\partial^2 \\mathbf{E}}{\\partial t^2}$$\n\nRearranging gives the celebrated **homogeneous vector wave equation for the electric field**:\n$$\\nabla^2 \\mathbf{E} - \\mu_0 \\epsilon_0 \\frac{\\partial^2 \\mathbf{E}}{\\partial t^2} = 0$$\n\nTaking the curl of Ampère-Maxwell's law in identical fashion yields the **wave equation for the magnetic field**:\n$$\\nabla^2 \\mathbf{B} - \\mu_0 \\epsilon_0 \\frac{\\partial^2 \\mathbf{B}}{\\partial t^2} = 0$$\n\n#### The Speed of Light and Maxwell's Synthesis\nComparing these to the standard 3D scalar wave equation $\\nabla^2 \\psi - \\frac{1}{v^2} \\frac{\\partial^2 \\psi}{\\partial t^2} = 0$, the wave propagation speed $v$ is determined strictly by electromagnetic constants:\n$$v = \\frac{1}{\\sqrt{\\epsilon_0 \\mu_0}}$$\n\nSubstituting experimental values:\n$$\\epsilon_0 \\approx 8.8541878 \\times 10^{-12} \\text{ F/m}, \\quad \\mu_0 = 4\\pi \\times 10^{-7} \\text{ H/m}$$\n$$v = \\frac{1}{\\sqrt{(8.8541878 \\times 10^{-12})(4\\pi \\times 10^{-7})}} = 2.99792458 \\times 10^8 \\text{ m/s} \\equiv c$$\n\nThis exact match between the derived velocity of electromagnetic waves and the measured speed of light led James Clerk Maxwell to declare: *\"Light is an electromagnetic disturbance in the form of waves propagating through the electromagnetic field according to electromagnetic laws.\"*\n"
        },
        {
          "secNumber": "2.2",
          "heading": "Plane Waves, Transverse Nature, and Orthogonality of Fields",
          "content": "\n#### Monochromatic Plane Wave Solutions\nA plane wave traveling in direction $\\hat{\\mathbf{k}}$ with wavevector $\\mathbf{k} = k \\hat{\\mathbf{k}}$ and angular frequency $\\omega$ is described in complex exponential notation by:\n$$\\mathbf{E}(\\mathbf{r}, t) = \\mathbf{E}_0 e^{i(\\mathbf{k} \\cdot \\mathbf{r} - \\omega t)}, \\quad \\mathbf{B}(\\mathbf{r}, t) = \\mathbf{B}_0 e^{i(\\mathbf{k} \\cdot \\mathbf{r} - \\omega t)}$$\nwhere physical fields are the real parts $\\text{Re}\\{\\mathbf{E}\\}$.\n\nSubstituting into the wave equation gives the vacuum **dispersion relation**:\n$$-k^2 + \\frac{\\omega^2}{c^2} = 0 \\implies k = \\frac{\\omega}{c} = \\frac{2\\pi}{\\lambda}$$\n\n#### Rigorous Proof of Transverse Nature (No Longitudinal Component)\nApply Gauss's law $\\nabla \\cdot \\mathbf{E} = 0$:\n$$\\nabla \\cdot \\left( \\mathbf{E}_0 e^{i(\\mathbf{k} \\cdot \\mathbf{r} - \\omega t)} \\right) = i \\mathbf{k} \\cdot \\mathbf{E}_0 e^{i(\\mathbf{k} \\cdot \\mathbf{r} - \\omega t)} = i \\mathbf{k} \\cdot \\mathbf{E} = 0$$\n$$\\implies \\mathbf{k} \\cdot \\mathbf{E} = 0$$\n\nSimilarly, applying $\\nabla \\cdot \\mathbf{B} = 0$:\n$$i \\mathbf{k} \\cdot \\mathbf{B} = 0 \\implies \\mathbf{k} \\cdot \\mathbf{B} = 0$$\n\n**Conclusion:** Both $\\mathbf{E}$ and $\\mathbf{B}$ are strictly perpendicular to the propagation vector $\\mathbf{k}$. Electromagnetic waves in unbounded homogeneous media are **purely transverse waves** ($E_k = 0, B_k = 0$).\n\n#### Orthogonality and Phase Relationship\nApplying Faraday's law $\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$:\n$$i \\mathbf{k} \\times \\mathbf{E} = i \\omega \\mathbf{B} \\implies \\mathbf{B} = \\frac{\\mathbf{k} \\times \\mathbf{E}}{\\omega} = \\frac{1}{c} (\\hat{\\mathbf{k}} \\times \\mathbf{E})$$\n\nThis fundamental vector relation establishes that:\n1. $\\mathbf{B}$ is perpendicular to $\\mathbf{E}$ ($\\mathbf{E} \\cdot \\mathbf{B} = 0$).\n2. $\\mathbf{E}$, $\\mathbf{B}$, and $\\hat{\\mathbf{k}}$ form an orthogonal right-handed triad:\n$$\\hat{\\mathbf{k}} = \\frac{\\mathbf{E} \\times \\mathbf{B}}{|\\mathbf{E}||\\mathbf{B}|}$$\n3. The magnitudes are related by $B_0 = \\frac{E_0}{c}$.\n4. In vacuum, $\\mathbf{E}$ and $\\mathbf{B}$ oscillate **exactly in phase**, reaching crests and nodes at identical positions and times.\n",
          "simulation": "em-wave-3d"
        },
        {
          "secNumber": "2.3",
          "heading": "Wave Impedance, Energy Flow, and Time-Averaged Poynting Flux",
          "content": "\n#### Intrinsic Wave Impedance of Free Space\nThe ratio of the transverse electric field to the transverse magnetic intensity $H = B/\\mu_0$ defines the **wave impedance**:\n$$\\eta_0 \\equiv \\frac{|\\mathbf{E}|}{|\\mathbf{H}|} = \\frac{E_0}{B_0 / \\mu_0} = \\mu_0 \\frac{E_0}{B_0} = \\mu_0 c = \\sqrt{\\frac{\\mu_0}{\\epsilon_0}}$$\n\nEvaluating numerically:\n$$\\eta_0 = \\sqrt{\\frac{4\\pi \\times 10^{-7} \\text{ H/m}}{8.8541878 \\times 10^{-12} \\text{ F/m}}} \\approx 376.7303135 \\, \\Omega \\approx 120\\pi \\, \\Omega$$\n\nThe wave impedance of free space represents the resistance of vacuum to the generation of electric and magnetic flux. In a linear medium with permittivity $\\epsilon$ and permeability $\\mu$, the intrinsic impedance is $\\eta = \\sqrt{\\mu / \\epsilon}$.\n\n#### Time-Averaged Energy Flux (Intensity)\nFor real sinusoidal fields traveling along $+z$:\n$$\\mathbf{E}(z, t) = E_0 \\cos(kz - \\omega t) \\hat{\\mathbf{x}}, \\quad \\mathbf{B}(z, t) = \\frac{E_0}{c} \\cos(kz - \\omega t) \\hat{\\mathbf{y}}$$\nThe instantaneous Poynting vector is:\n$$\\mathbf{S}(z, t) = \\frac{1}{\\mu_0} (\\mathbf{E} \\times \\mathbf{B}) = \\frac{E_0^2}{\\mu_0 c} \\cos^2(kz - \\omega t) \\hat{\\mathbf{z}} = c \\epsilon_0 E_0^2 \\cos^2(kz - \\omega t) \\hat{\\mathbf{z}}$$\n\nSince the time average of $\\cos^2(\\theta)$ over a full cycle is $\\frac{1}{2}$, the **time-averaged Poynting vector** (wave intensity $I$) is:\n$$\\langle \\mathbf{S} \\rangle = \\frac{1}{2} c \\epsilon_0 E_0^2 \\hat{\\mathbf{z}} = \\frac{1}{2} \\frac{E_0^2}{\\eta_0} \\hat{\\mathbf{z}} = \\frac{1}{2} \\text{Re}\\{\\mathbf{E} \\times \\mathbf{H}^*\\}$$\n\n#### Energy Density Distribution\nThe time-averaged electric energy density is:\n$$\\langle u_E \\rangle = \\frac{1}{4} \\epsilon_0 E_0^2$$\nThe time-averaged magnetic energy density is:\n$$\\langle u_B \\rangle = \\frac{1}{4\\mu_0} B_0^2 = \\frac{1}{4\\mu_0} \\left( \\frac{E_0}{c} \\right)^2 = \\frac{1}{4} \\epsilon_0 E_0^2$$\nThus, $\\langle u_E \\rangle = \\langle u_B \\rangle$: **electromagnetic energy is partitioned equally between electric and magnetic fields** at all times in a plane wave.\n"
        },
        {
          "secNumber": "2.4",
          "heading": "Propagation in Isotropic Non-Conducting Media",
          "content": "\nIn a linear, homogeneous, isotropic dielectric medium with permittivity $\\epsilon = \\epsilon_r \\epsilon_0$, permeability $\\mu = \\mu_r \\mu_0$, and conductivity $\\sigma = 0$:\n\nMaxwell's equations yield the modified wave velocity:\n$$v = \\frac{1}{\\sqrt{\\epsilon \\mu}} = \\frac{1}{\\sqrt{\\epsilon_r \\epsilon_0 \\mu_r \\mu_0}} = \\frac{c}{\\sqrt{\\epsilon_r \\mu_r}} = \\frac{c}{n}$$\nwhere $n \\equiv \\sqrt{\\epsilon_r \\mu_r}$ is the **index of refraction** of the medium. For non-magnetic optical materials ($\\mu_r \\approx 1$), Maxwell's relation gives:\n$$n = \\sqrt{\\epsilon_r}$$\n\n#### Wavelength and Wavevector in Matter\nBecause frequency $\\omega$ is fixed by the driving source, the wavelength in the dielectric shrinks:\n$$\\lambda = \\frac{v}{f} = \\frac{c}{n f} = \\frac{\\lambda_0}{n}$$\nThe wavevector increases:\n$$k = \\frac{\\omega}{v} = n k_0$$\nThe wave impedance becomes:\n$$\\eta = \\sqrt{\\frac{\\mu}{\\epsilon}} = \\frac{\\eta_0}{n} \\quad (\\text{for } \\mu_r = 1)$$\nThe time-averaged intensity in the dielectric is:\n$$I = \\frac{1}{2} v \\epsilon E_0^2 = \\frac{1}{2} n c \\epsilon_0 E_0^2$$\n"
        },
        {
          "secNumber": "2.5",
          "heading": "Propagation in Conducting Media: Loss Tangent & Complex Wavevector",
          "content": "\n#### The Telegrapher-Type Wave Equation in Conductors\nIn an ohmic conducting medium with electric conductivity $\\sigma$, free conduction currents flow according to **Ohm's Law**: $\\mathbf{J}_f = \\sigma \\mathbf{E}$. There are no static free charges ($\\rho_f = 0$).\n\nMaxwell's curl equations become:\n$$\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$$\n$$\\nabla \\times \\mathbf{B} = \\mu \\mathbf{J}_f + \\mu \\epsilon \\frac{\\partial \\mathbf{E}}{\\partial t} = \\mu \\sigma \\mathbf{E} + \\mu \\epsilon \\frac{\\partial \\mathbf{E}}{\\partial t}$$\n\nTaking the curl of Faraday's law:\n$$\\nabla \\times (\\nabla \\times \\mathbf{E}) = -\\frac{\\partial}{\\partial t} (\\nabla \\times \\mathbf{B}) = -\\mu \\sigma \\frac{\\partial \\mathbf{E}}{\\partial t} - \\mu \\epsilon \\frac{\\partial^2 \\mathbf{E}}{\\partial t^2}$$\nSince $\\nabla \\cdot \\mathbf{E} = 0$:\n$$\\nabla^2 \\mathbf{E} - \\mu \\epsilon \\frac{\\partial^2 \\mathbf{E}}{\\partial t^2} - \\mu \\sigma \\frac{\\partial \\mathbf{E}}{\\partial t} = 0$$\n\nThe first-order time derivative term $\\mu \\sigma \\frac{\\partial \\mathbf{E}}{\\partial t}$ acts as a dissipative frictional damping term that extracts energy from the wave and converts it into Joule heat.\n\n#### Complex Wavevector Formulation\nSubstitute a monochromatic plane wave $\\mathbf{E} = \\mathbf{E}_0 e^{i(\\tilde{k} z - \\omega t)}$:\n$$-\\tilde{k}^2 \\mathbf{E} + \\mu \\epsilon \\omega^2 \\mathbf{E} + i \\mu \\sigma \\omega \\mathbf{E} = 0$$\n$$\\tilde{k}^2 = \\mu \\epsilon \\omega^2 \\left( 1 + i \\frac{\\sigma}{\\omega \\epsilon} \\right)$$\n\nThe ratio $\\tan \\delta \\equiv \\frac{\\sigma}{\\omega \\epsilon}$ is known as the **loss tangent**. It quantifies the relative magnitude of conduction current compared to displacement current:\n$$\\frac{|\\mathbf{J}_c|}{|\\mathbf{J}_d|} = \\frac{|\\sigma \\mathbf{E}|}{|\\epsilon \\partial \\mathbf{E}/\\partial t|} = \\frac{\\sigma}{\\omega \\epsilon}$$\n\nLet the complex wavevector be $\\tilde{k} \\equiv \\beta + i \\alpha$:\n$$\\tilde{k}^2 = (\\beta + i \\alpha)^2 = \\beta^2 - \\alpha^2 + 2i \\alpha \\beta = \\mu \\epsilon \\omega^2 + i \\mu \\sigma \\omega$$\n\nEquating real and imaginary parts:\n$$\\beta^2 - \\alpha^2 = \\mu \\epsilon \\omega^2$$\n$$2 \\alpha \\beta = \\mu \\sigma \\omega$$\n\nSolving this system yields the exact analytical expressions:\n$$\\beta = \\omega \\sqrt{\\frac{\\mu \\epsilon}{2}} \\left[ \\sqrt{1 + \\left( \\frac{\\sigma}{\\omega \\epsilon} \\right)^2} + 1 \\right]^{1/2} \\quad (\\text{Phase constant})$$\n$$\\alpha = \\omega \\sqrt{\\frac{\\mu \\epsilon}{2}} \\left[ \\sqrt{1 + \\left( \\frac{\\sigma}{\\omega \\epsilon} \\right)^2} - 1 \\right]^{1/2} \\quad (\\text{Attenuation constant})$$\n\nThe spatial electric field in the conductor is therefore:\n$$\\mathbf{E}(z, t) = \\mathbf{E}_0 e^{-\\alpha z} e^{i(\\beta z - \\omega t)}$$\nThe wave amplitude decays exponentially with distance into the conductor.\n"
        },
        {
          "secNumber": "2.6",
          "heading": "Attenuation Constant, Phase Shift, and the Skin Depth (δ)",
          "content": "\n#### The Good Conductor Limit ($\\sigma \\gg \\omega \\epsilon$)\nFor metals and good conductors (such as copper, silver, aluminum, and sea water at radio frequencies), conduction current dwarfs displacement current:\n$$\\frac{\\sigma}{\\omega \\epsilon} \\gg 1$$\n\nUnder this approximation, the term $\\sqrt{1 + (\\sigma/\\omega\\epsilon)^2} \\approx \\frac{\\sigma}{\\omega \\epsilon}$, and the formulas for $\\alpha$ and $\\beta$ simplify dramatically:\n$$\\beta \\approx \\alpha \\approx \\omega \\sqrt{\\frac{\\mu \\epsilon}{2} \\frac{\\sigma}{\\omega \\epsilon}} = \\sqrt{\\frac{\\omega \\mu \\sigma}{2}} = \\sqrt{\\pi f \\mu \\sigma}$$\n\n#### Definition of Skin Depth ($\\delta$)\nThe **skin depth** $\\delta$ (also called penetration depth) is defined as the distance over which the wave amplitude drops by a factor of $1/e \\approx 0.3679$ (36.8% of its surface value):\n$$\\delta \\equiv \\frac{1}{\\alpha} = \\sqrt{\\frac{2}{\\omega \\mu \\sigma}} = \\frac{1}{\\sqrt{\\pi f \\mu \\sigma}}$$\n\nOver a depth of $z = 5\\delta$, the wave amplitude decays to $e^{-5} \\approx 0.0067$ (under 0.7%), meaning high-frequency currents are confined almost entirely to a microscopically thin outer shell of a conductor.\n\n#### Table: Practical Skin Depths Across Frequencies\nFor pure copper ($\\sigma = 5.8 \\times 10^7 \\text{ S/m}$, $\\mu = \\mu_0$):\n\n| Frequency ($f$) | Skin Depth $\\delta$ in Copper | Application / Impact |\n| :--- | :--- | :--- |\n| **50 Hz / 60 Hz** | $9.38 \\text{ mm}$ | AC mains power transmission (large cables require hollow or stranded conductors). |\n| **10 kHz** | $0.66 \\text{ mm}$ | Audio and induction heating frequencies. |\n| **1 MHz** | $66 \\, \\mu\\text{m}$ | AM radio broadcast frequencies. |\n| **100 MHz** | $6.6 \\, \\mu\\text{m}$ | FM radio and VHF communications. |\n| **10 GHz** | $0.66 \\, \\mu\\text{m}$ | X-band radar and microwave waveguides (requires surface silver plating). |\n\n#### Phase Delay Between $\\mathbf{E}$ and $\\mathbf{B}$\nFrom Faraday's law in a good conductor:\n$$\\mathbf{B} = \\frac{\\tilde{k}}{\\omega} (\\hat{\\mathbf{z}} \\times \\mathbf{E})$$\nSince $\\tilde{k} = \\beta + i \\alpha = \\alpha(1 + i) = \\alpha \\sqrt{2} e^{i\\pi/4}$:\n$$\\mathbf{B}(z, t) = \\frac{\\sqrt{2} \\alpha}{\\omega} E_0 e^{-\\alpha z} e^{i(\\beta z - \\omega t + \\pi/4)} (\\hat{\\mathbf{z}} \\times \\hat{\\mathbf{x}})$$\n\n**Physical Result:** In a good conductor, the magnetic field lags the electric field by a phase angle of $45^\\circ$ ($\\pi/4$ radians), and the magnetic energy density dramatically exceeds the electric energy density:\n$$\\frac{\\langle u_B \\rangle}{\\langle u_E \\rangle} = \\frac{\\sigma}{\\omega \\epsilon} \\gg 1$$\n",
          "simulation": "skin-depth"
        },
        {
          "secNumber": "2.7",
          "heading": "Electromagnetic Waves in Ionized Gases (Plasmas) and Ionospheric Propagation",
          "content": "\n#### The Cold Plasma Dielectric Function\nConsider an ionized gas (such as the Earth's ionosphere or interstellar plasma) consisting of free electrons (mass $m_e$, charge $-e$, density $n_e$) and heavy, immobile positive ions. In the presence of a monochromatic electric field $\\mathbf{E}(t) = \\mathbf{E}_0 e^{-i\\omega t}$, the equation of motion for a conduction electron (neglecting damping collisions) is:\n$$m_e \\frac{d^2 \\mathbf{r}}{dt^2} = -e \\mathbf{E} = -e \\mathbf{E}_0 e^{-i\\omega t}$$\n$$\\mathbf{r}(t) = \\frac{e}{m_e \\omega^2} \\mathbf{E}(t)$$\n\nThe induced macroscopic dipole polarization density is:\n$$\\mathbf{P} = -n_e e \\mathbf{r} = -\\frac{n_e e^2}{m_e \\omega^2} \\mathbf{E}$$\n\nThe electric displacement is:\n$$\\mathbf{D} = \\epsilon_0 \\mathbf{E} + \\mathbf{P} = \\epsilon_0 \\left( 1 - \\frac{n_e e^2}{\\epsilon_0 m_e \\omega^2} \\right) \\mathbf{E} \\equiv \\epsilon(\\omega) \\mathbf{E}$$\n\n#### The Plasma Frequency ($\\omega_p$)\nWe define the characteristic **electron plasma frequency**:\n$$\\omega_p \\equiv \\sqrt{\\frac{n_e e^2}{\\epsilon_0 m_e}} \\quad [\\text{rad/s}]$$\nIn terms of frequency in Hertz:\n$$f_p = \\frac{\\omega_p}{2\\pi} = \\frac{1}{2\\pi} \\sqrt{\\frac{n_e e^2}{\\epsilon_0 m_e}} \\approx 8.98 \\sqrt{n_e} \\quad [\\text{Hz}]$$\nwhere $n_e$ is in $\\text{electrons/m}^3$.\n\nThe relative permittivity of the plasma is:\n$$\\epsilon_r(\\omega) = 1 - \\frac{\\omega_p^2}{\\omega^2}$$\n\n#### Dispersion Relation and Propagation Regimes\nThe wavevector in the plasma satisfies:\n$$k^2 = \\frac{\\omega^2}{c^2} \\epsilon_r(\\omega) = \\frac{\\omega^2}{c^2} \\left( 1 - \\frac{\\omega_p^2}{\\omega^2} \\right) = \\frac{\\omega^2 - \\omega_p^2}{c^2}$$\n\n1. **High Frequency Regime ($\\omega > \\omega_p$):**\n   $k$ is purely real:\n   $$k = \\frac{1}{c} \\sqrt{\\omega^2 - \\omega_p^2}$$\n   The wave propagates freely without attenuation. The phase velocity exceeds the speed of light:\n   $$v_p = \\frac{\\omega}{k} = \\frac{c}{\\sqrt{1 - \\omega_p^2/\\omega^2}} > c$$\n   The group velocity (signal energy velocity) is strictly less than $c$:\n   $$v_g = \\frac{d\\omega}{dk} = c \\sqrt{1 - \\frac{\\omega_p^2}{\\omega^2}} < c$$\n   Notice that $v_p \\cdot v_g = c^2$, satisfying special relativity.\n\n2. **Low Frequency Cutoff Regime ($\\omega < \\omega_p$):**\n   $k$ becomes purely imaginary:\n   $$k = i \\kappa = i \\frac{1}{c} \\sqrt{\\omega_p^2 - \\omega^2}$$\n   The fields decay exponentially: $\\mathbf{E}(z, t) = \\mathbf{E}_0 e^{-\\kappa z} e^{-i\\omega t}$. No real energy is propagated; instead, the wave undergoes **total reflection** at the plasma boundary.\n\n**Application to Radio Communications:** The Earth's ionosphere has peak electron density $n_e \\approx 10^{12} \\text{ m}^{-3}$, giving a plasma critical frequency $f_p \\approx 9 \\text{ MHz}$. Shortwave radio signals ($3 - 30 \\text{ MHz}$) below the critical frequency are totally reflected back to Earth, enabling global intercontinental communication without satellites. Satellite transmissions (GPS, 1.5 GHz) easily exceed $f_p$ and pass through the ionosphere unhindered.\n",
          "simulation": "plasma-cutoff-sim"
        }
      ],
      "problems": [
        {
          "id": "p2-1",
          "title": "Example 2.1: High-Power Monochromatic Laser Beam Parameters and Peak Field Strengths",
          "difficulty": "Medium",
          "question": "A focused Nd:YAG laser beam ($\\lambda = 1064\\text{ nm}$) operates at an average output power of $P = 150\\text{ W}$. It is focused down to a circular spot of radius $w_0 = 25\\,\\mu\\text{m}$ in air. Calculate: (a) the laser beam intensity $I$, (b) the peak electric field amplitude $E_0$, (c) the peak magnetic field amplitude $B_0$, and (d) the radiation pressure $P_{\\text{rad}}$ on a totally absorbing target placed at the focal spot.",
          "steps": [
            {
              "stepName": "Step 1: Laser Intensity Calculation",
              "math": "A = \\pi w_0^2 = \\pi (25 \\times 10^{-6}\\text{ m})^2 = 1.963 \\times 10^{-9}\\text{ m}^2\\nI = \\frac{P}{A} = \\frac{150\\text{ W}}{1.963 \\times 10^{-9}\\text{ m}^2} = 7.64 \\times 10^{10}\\text{ W/m}^2",
              "explanation": "Focusing the laser concentrates 150 watts into a flux of over 76 gigawatts per square meter."
            },
            {
              "stepName": "Step 2: Peak Electric Field Amplitude",
              "math": "I = \\frac{1}{2} c \\epsilon_0 E_0^2 \\implies E_0 = \\sqrt{\\frac{2I}{c \\epsilon_0}}\\nE_0 = \\sqrt{\\frac{2(7.64 \\times 10^{10})}{(3.00 \\times 10^8)(8.854 \\times 10^{-12})}} = \\sqrt{5.753 \\times 10^{13}} = 7.58 \\times 10^6\\text{ V/m} = 7.58\\text{ MV/m}",
              "explanation": "The electric field exceeds the dielectric breakdown threshold of ambient air ($3\\text{ MV/m}$), ionizing air molecules and generating a visible optical plasma spark."
            },
            {
              "stepName": "Step 3: Peak Magnetic Field Amplitude",
              "math": "B_0 = \\frac{E_0}{c} = \\frac{7.58 \\times 10^6\\text{ V/m}}{3.00 \\times 10^8\\text{ m/s}} = 0.0253\\text{ T} = 25.3\\text{ mT}",
              "explanation": "The magnetic induction reaches 253 Gauss, illustrating the immense strength of focused optical fields."
            },
            {
              "stepName": "Step 4: Radiation Pressure",
              "math": "P_{\\text{rad}} = \\frac{I}{c} = \\frac{7.64 \\times 10^{10}\\text{ W/m}^2}{3.00 \\times 10^8\\text{ m/s}} = 254.7\\text{ N/m}^2 \\approx 255\\text{ Pa}",
              "explanation": "Radiation pressure reaches several millibars, easily enough to trap and levitate microscopic dielectric beads in optical tweezers."
            }
          ]
        },
        {
          "id": "p2-2",
          "title": "Example 2.2: Penetration Depth of ELF Radio Waves in Seawater for Submarine Communications",
          "difficulty": "Hard",
          "question": "Seawater has electrical conductivity $\\sigma = 4.0\\text{ S/m}$, relative permittivity $\\epsilon_r = 81$, and $\\mu_r = 1$. (a) Determine whether seawater behaves as a good conductor or dielectric at $f = 75\\text{ Hz}$ (Extremely Low Frequency, ELF) and at $f = 2.4\\text{ GHz}$ (Wi-Fi). (b) Calculate the skin depth $\\delta$ at $75\\text{ Hz}$. (c) Calculate the depth $z$ at which a $75\\text{ Hz}$ submarine communications signal is attenuated by $60\\text{ dB}$ (power factor of $10^{-6}$).",
          "steps": [
            {
              "stepName": "Step 1: Loss Tangent Verification",
              "math": "\\text{At } f = 75\\text{ Hz}: \\frac{\\sigma}{\\omega \\epsilon} = \\frac{4.0}{2\\pi(75)(81)(8.854 \\times 10^{-12})} = \\frac{4.0}{3.385 \\times 10^{-7}} = 1.18 \\times 10^7 \\gg 1\\n\\text{At } f = 2.4\\text{ GHz}: \\frac{\\sigma}{\\omega \\epsilon} = \\frac{4.0}{2\\pi(2.4 \\times 10^9)(81)(8.854 \\times 10^{-12})} = 0.369 \\sim 1",
              "explanation": "At 75 Hz, seawater is an exceptional conductor (conduction current dominates by 7 orders of magnitude). At 2.4 GHz, seawater is a lossy dielectric."
            },
            {
              "stepName": "Step 2: Skin Depth at 75 Hz",
              "math": "\\delta = \\frac{1}{\\sqrt{\\pi f \\mu_0 \\sigma}} = \\frac{1}{\\sqrt{\\pi(75)(4\\pi \\times 10^{-7})(4.0)}} = \\frac{1}{\\sqrt{1.184 \\times 10^{-3}}} = \\frac{1}{0.0344} = 29.06\\text{ m}",
              "explanation": "The electromagnetic field amplitude decays by a factor of $1/e$ every 29 meters of seawater depth."
            },
            {
              "stepName": "Step 3: Depth for 60 dB Power Attenuation",
              "math": "\\text{Power ratio } \\frac{P(z)}{P(0)} = e^{-2\\alpha z} = e^{-2z/\\delta} = 10^{-6}\\n-\\frac{2z}{\\delta} = \\ln(10^{-6}) = -6 \\ln(10) = -13.816\\nz = \\frac{13.816}{2} \\delta = 6.908 \\times 29.06\\text{ m} = 200.7\\text{ m}",
              "explanation": "ELF signals at 75 Hz can successfully reach nuclear submarines operating submerged at depths up to 200 meters (660 feet) without surfacing."
            }
          ]
        },
        {
          "id": "p2-3",
          "title": "Example 2.3: Phase Delay, Skin Effect, and AC Surface Resistance in Copper",
          "difficulty": "Medium",
          "question": "For a microwave frequency of $f = 10\\text{ GHz}$ propagating in copper ($\\sigma = 5.8 \\times 10^7\\text{ S/m}$, $\\mu = \\mu_0$): (a) calculate the skin depth $\\delta$, (b) calculate the phase velocity $v_p$ and wavelength $\\lambda$ inside the copper, and (c) find the surface resistance $R_s = \\frac{1}{\\sigma \\delta}$ per square.",
          "steps": [
            {
              "stepName": "Step 1: Skin Depth Calculation",
              "math": "\\delta = \\frac{1}{\\sqrt{\\pi f \\mu_0 \\sigma}} = \\frac{1}{\\sqrt{\\pi(10^{10})(4\\pi \\times 10^{-7})(5.8 \\times 10^7)}} = \\frac{1}{\\sqrt{2.2898 \\times 10^{12}}} = 6.61 \\times 10^{-7}\\text{ m} = 0.661\\,\\mu\\text{m}",
              "explanation": "At 10 GHz, the entire microwave current flows in an ultra-thin surface skin of just 661 nanometers."
            },
            {
              "stepName": "Step 2: Phase Velocity and Wavelength Inside the Metal",
              "math": "\\beta = \\frac{1}{\\delta} = 1.513 \\times 10^6\\text{ rad/m}\\n\\lambda_{\\text{copper}} = \\frac{2\\pi}{\\beta} = 2\\pi \\delta = 2\\pi(6.61 \\times 10^{-7}\\text{ m}) = 4.15 \\times 10^{-6}\\text{ m} = 4.15\\,\\mu\\text{m}\\nv_p = \\frac{\\omega}{\\beta} = \\omega \\delta = 2\\pi(10^{10})(6.61 \\times 10^{-7}) = 4.15 \\times 10^4\\text{ m/s}",
              "explanation": "In free space, a 10 GHz wave has $\\lambda_0 = 3\\text{ cm}$ and $v_p = c$. Inside the metal, the wave slows down to 41.5 km/s (a factor of 7200 slower), and its wavelength compresses to just 4.15 micrometers."
            },
            {
              "stepName": "Step 3: Surface Resistance Calculation",
              "math": "R_s = \\frac{1}{\\sigma \\delta} = \\sqrt{\\frac{\\pi f \\mu_0}{\\sigma}} = \\frac{1}{(5.8 \\times 10^7)(6.61 \\times 10^{-7})} = 0.0261\\,\\Omega = 26.1\\text{ m}\\Omega / \\text{sq}",
              "explanation": "This non-zero surface resistance causes wall conduction loss and attenuation in microwave waveguides and cavity resonators."
            }
          ]
        },
        {
          "id": "p2-4",
          "title": "Example 2.4: Ionospheric Cutoff Frequency and Maximum Usable Frequency (MUF)",
          "difficulty": "Hard",
          "question": "The daytime ionospheric F2 layer has an electron density of $n_e = 1.5 \\times 10^{12}\\text{ m}^{-3}$. (a) Calculate the critical plasma frequency $f_p$. (b) For radio waves incident on the ionosphere at an angle of incidence $\\theta_i = 65^\\circ$ relative to the normal, use Snell's law to derive and calculate the Maximum Usable Frequency (MUF) that can still be reflected back to Earth (secant law).",
          "steps": [
            {
              "stepName": "Step 1: Critical Plasma Frequency Calculation",
              "math": "f_p = \\frac{1}{2\\pi} \\sqrt{\\frac{n_e e^2}{\\epsilon_0 m_e}} = \\frac{1}{2\\pi} \\sqrt{\\frac{(1.5 \\times 10^{12})(1.602 \\times 10^{-19})^2}{(8.854 \\times 10^{-12})(9.109 \\times 10^{-31})}}\\nf_p = \\frac{1}{2\\pi} \\sqrt{4.777 \\times 10^{14}} = \\frac{2.1856 \\times 10^7}{2\\pi} = 3.478 \\times 10^6\\text{ Hz} \\approx 11.0\\text{ MHz}",
              "explanation": "Vertical incidence signals ($0^\\circ$) at frequencies above 11.0 MHz will penetrate straight through the ionosphere into outer space."
            },
            {
              "stepName": "Step 2: Oblique Incidence and the Secant Law",
              "math": "n_1 \\sin\\theta_i = n_2 \\sin\\theta_r\\n\\text{For total internal reflection at turning point: } \\theta_r = 90^\\circ \\implies \\sin\\theta_i = n = \\sqrt{1 - \\frac{f_p^2}{f^2}}\\n\\sin^2\\theta_i = 1 - \\frac{f_p^2}{f^2} \\implies \\frac{f_p^2}{f^2} = 1 - \\sin^2\\theta_i = \\cos^2\\theta_i\\nf_{\\text{MUF}} = \\frac{f_p}{\\cos\\theta_i} = f_p \\sec\\theta_i",
              "explanation": "This celebrated relation is known as Martyn's Secant Law for ionospheric radio reflection."
            },
            {
              "stepName": "Step 3: Maximum Usable Frequency Calculation",
              "math": "f_{\\text{MUF}} = f_p \\sec(65^\\circ) = \\frac{11.0\\text{ MHz}}{\\cos(65^\\circ)} = \\frac{11.0\\text{ MHz}}{0.4226} = 26.03\\text{ MHz}",
              "explanation": "Because oblique incidence glances off the ionosphere, shortwave radio operators can communicate across continents at frequencies up to 26 MHz, well above the 11 MHz vertical critical frequency."
            }
          ]
        }
      ]
    },
    {
      "id": "unit-3",
      "number": 3,
      "title": "Waves in Bounded Regions, Waveguides & Cavity Resonators",
      "leadSummary": "Comprehensive mathematical analysis of bounded electromagnetic radiation: rigorous derivation of electromagnetic boundary conditions from Maxwell's integral laws, normal and oblique reflection and refraction at dielectric boundaries, Fresnel reflection and transmission equations for TE and TM polarizations, Brewster's angle, total internal reflection with evanescent decay, metallic boundary reflection, wave propagation between parallel conducting plates, boundary-value eigenvalue problems in rectangular waveguides, TE/TM cutoff frequencies, phase and group velocities, and microwave cavity resonators.",
      "simulations": [
        "fresnel-reflection",
        "waveguide-modes"
      ],
      "sections": [
        {
          "secNumber": "3.1",
          "heading": "General Electromagnetic Boundary Conditions at Media Interfaces",
          "content": "\n#### Derivation of Boundary Conditions from Maxwell's Integral Equations\nWhen an electromagnetic wave encounters an interface separating two distinct physical media (characterized by $\\epsilon_1, \\mu_1, \\sigma_1$ and $\\epsilon_2, \\mu_2, \\sigma_2$), the fields must satisfy fundamental boundary conditions derived directly from the integral forms of Maxwell's equations.\n\nLet $\\hat{\\mathbf{n}}$ be the unit normal vector pointing from medium 2 into medium 1.\n\n#### 1. Normal Component of Electric Displacement Field ($\\mathbf{D}$)\nConstruct a Gaussian pillbox of cross-sectional area $\\Delta A$ and height $h$ straddling the interface. Applying Gauss's law $\\oint_S \\mathbf{D} \\cdot d\\mathbf{a} = Q_{f,\\text{enc}}$ in the limit as $h \\to 0$:\n$$(\\mathbf{D}_1 \\cdot \\hat{\\mathbf{n}} - \\mathbf{D}_2 \\cdot \\hat{\\mathbf{n}}) \\Delta A = \\sigma_f \\Delta A$$\n$$D_{1n} - D_{2n} = \\sigma_f \\quad \\iff \\quad \\epsilon_1 E_{1n} - \\epsilon_2 E_{2n} = \\sigma_f$$\nwhere $\\sigma_f$ is the free surface charge density on the interface. For linear dielectrics without free surface charge ($\\sigma_f = 0$):\n$$D_{1n} = D_{2n} \\implies \\epsilon_1 E_{1n} = \\epsilon_2 E_{2n}$$\n\n#### 2. Normal Component of Magnetic Induction Field ($\\mathbf{B}$)\nApplying Gauss's law for magnetism $\\oint_S \\mathbf{B} \\cdot d\\mathbf{a} = 0$ over the same pillbox as $h \\to 0$:\n$$B_{1n} - B_{2n} = 0 \\implies B_{1n} = B_{2n}$$\n**Result:** The normal component of the magnetic induction $\\mathbf{B}$ is **always continuous** across any interface without exception.\n\n#### 3. Tangential Component of Electric Field ($\\mathbf{E}$)\nConstruct an Amperian loop of width $\\Delta l$ parallel to the interface and height $h$ perpendicular to it. Applying Faraday's law $\\oint_C \\mathbf{E} \\cdot d\\mathbf{l} = -\\frac{d}{dt} \\int_S \\mathbf{B} \\cdot d\\mathbf{a}$:\nAs $h \\to 0$, the magnetic flux through the loop vanishes ($h \\Delta l \\to 0$), leaving:\n$$(E_{1t} - E_{2t}) \\Delta l = 0 \\implies E_{1t} = E_{2t}$$\n$$\\hat{\\mathbf{n}} \\times (\\mathbf{E}_1 - \\mathbf{E}_2) = 0$$\n**Result:** The tangential component of the electric field is **always continuous** across any boundary.\n\n#### 4. Tangential Component of Magnetic Field Intensity ($\\mathbf{H}$)\nApplying the Ampère-Maxwell law $\\oint_C \\mathbf{H} \\cdot d\\mathbf{l} = I_{f,\\text{enc}} + \\frac{d}{dt} \\int_S \\mathbf{D} \\cdot d\\mathbf{a}$:\nAs $h \\to 0$, the displacement current flux vanishes, but a surface free current density $\\mathbf{K}_f$ perpendicular to the loop can contribute:\n$$H_{1t} - H_{2t} = K_{f,\\perp}$$\n$$\\hat{\\mathbf{n}} \\times (\\mathbf{H}_1 - \\mathbf{H}_2) = \\mathbf{K}_f$$\nFor non-conducting dielectric media where no surface free currents exist ($\\mathbf{K}_f = 0$):\n$$H_{1t} = H_{2t} \\implies \\frac{B_{1t}}{\\mu_1} = \\frac{B_{2t}}{\\mu_2}$$\n"
        },
        {
          "secNumber": "3.2",
          "heading": "Reflection and Refraction at a Plane Dielectric Interface (Normal Incidence)",
          "content": "\nConsider a monochromatic plane wave traveling along $+z$ in medium 1 ($z < 0$, parameters $\\epsilon_1, \\mu_1, n_1$) normally incident upon a flat boundary at $z = 0$ with medium 2 ($z > 0$, parameters $\\epsilon_2, \\mu_2, n_2$).\n\n#### Field Formulations\n1. **Incident Wave:**\n$$\\mathbf{E}_i(z, t) = E_{0i} e^{i(k_1 z - \\omega t)} \\hat{\\mathbf{x}}, \\quad \\mathbf{B}_i(z, t) = \\frac{E_{0i}}{v_1} e^{i(k_1 z - \\omega t)} \\hat{\\mathbf{y}}$$\n2. **Reflected Wave:** (travels along $-z$)\n$$\\mathbf{E}_r(z, t) = E_{0r} e^{i(-k_1 z - \\omega t)} \\hat{\\mathbf{x}}, \\quad \\mathbf{B}_r(z, t) = -\\frac{E_{0r}}{v_1} e^{i(-k_1 z - \\omega t)} \\hat{\\mathbf{y}}$$\n3. **Transmitted Wave:** (travels along $+z$ in medium 2)\n$$\\mathbf{E}_t(z, t) = E_{0t} e^{i(k_2 z - \\omega t)} \\hat{\\mathbf{x}}, \\quad \\mathbf{B}_t(z, t) = \\frac{E_{0t}}{v_2} e^{i(k_2 z - \\omega t)} \\hat{\\mathbf{y}}$$\n\n#### Matching Boundary Conditions at $z = 0$\n1. **Continuity of Tangential $\\mathbf{E}$:**\n$$E_{0i} + E_{0r} = E_{0t}$$\n2. **Continuity of Tangential $\\mathbf{H}$ (assuming $\\mu_1 \\approx \\mu_2 \\approx \\mu_0$):**\n$$\\frac{E_{0i}}{v_1} - \\frac{E_{0r}}{v_1} = \\frac{E_{0t}}{v_2} \\implies n_1(E_{0i} - E_{0r}) = n_2 E_{0t}$$\n\n#### Amplitude Reflection and Transmission Coefficients\nSolving this $2 \\times 2$ algebraic system:\n$$r \\equiv \\frac{E_{0r}}{E_{0i}} = \\frac{n_1 - n_2}{n_1 + n_2}$$\n$$t \\equiv \\frac{E_{0t}}{E_{0i}} = \\frac{2n_1}{n_1 + n_2}$$\n\nNotice that if $n_2 > n_1$ (denser medium, e.g., air into glass), $r < 0$, corresponding to a **$\\\\pi$ phase reversal** upon reflection.\n\n#### Energy Conservation: Reflectance ($R$) and Transmittance ($T$)\nThe time-averaged power reflected and transmitted per unit area are:\n$$R \\equiv \\frac{|\\langle \\mathbf{S}_r \\rangle|}{|\\langle \\mathbf{S}_i \\rangle|} = \\left| \\frac{E_{0r}}{E_{0i}} \\right|^2 = \\left( \\frac{n_1 - n_2}{n_1 + n_2} \\right)^2$$\n$$T \\equiv \\frac{|\\langle \\mathbf{S}_t \\rangle|}{|\\langle \\mathbf{S}_i \\rangle|} = \\frac{v_2 \\epsilon_2 E_{0t}^2}{v_1 \\epsilon_1 E_{0i}^2} = \\frac{n_2}{n_1} \\left( \\frac{2n_1}{n_1 + n_2} \\right)^2 = \\frac{4 n_1 n_2}{(n_1 + n_2)^2}$$\n\nSumming the two:\n$$R + T = \\frac{(n_1 - n_2)^2 + 4n_1 n_2}{(n_1 + n_2)^2} = \\frac{(n_1 + n_2)^2}{(n_1 + n_2)^2} \\equiv 1$$\nEnergy flux is conserved across the interface.\n"
        },
        {
          "secNumber": "3.3",
          "heading": "Oblique Incidence, Snell's Law, and the Fresnel Equations",
          "content": "\n#### Phase Matching and the Laws of Reflection & Refraction\nLet a plane wave with wavevector $\\mathbf{k}_i$ strike the interface ($z=0$) at angle of incidence $\\theta_i$ relative to the normal $\\hat{\\mathbf{z}}$. For boundary conditions to hold at all spatial positions $(x, y)$ on the interface and at all times $t$, the spatial phases must match:\n$$(\\mathbf{k}_i \\cdot \\mathbf{r})_{z=0} = (\\mathbf{k}_r \\cdot \\mathbf{r})_{z=0} = (\\mathbf{k}_t \\cdot \\mathbf{r})_{z=0}$$\n$$k_i \\sin\\theta_i = k_r \\sin\\theta_r = k_t \\sin\\theta_t$$\n\nSince $k_i = k_r = n_1 \\frac{\\omega}{c}$ and $k_t = n_2 \\frac{\\omega}{c}$:\n1. **Law of Reflection:** $\\theta_r = \\theta_i$\n2. **Snell's Law of Refraction:** $n_1 \\sin\\theta_i = n_2 \\sin\\theta_t$\n\n#### The Two Orthogonal Polarizations\nAny arbitrarily polarized plane wave can be decomposed into two fundamental linear modes:\n1. **$s$-Polarization (TE / Perpendicular):** Electric field $\\mathbf{E}$ is perpendicular to the plane of incidence.\n2. **$p$-Polarization (TM / Parallel):** Electric field $\\mathbf{E}$ lies entirely within the plane of incidence.\n\n#### The Fresnel Equations (for $\\mu_1 = \\mu_2 = \\mu_0$)\n\n#### 1. Perpendicular Polarization ($s$ / TE):\n$$r_s = \\frac{E_{0r}}{E_{0i}} = \\frac{n_1 \\cos\\theta_i - n_2 \\cos\\theta_t}{n_1 \\cos\\theta_i + n_2 \\cos\\theta_t} = -\\frac{\\sin(\\theta_i - \\theta_t)}{\\sin(\\theta_i + \\theta_t)}$$\n$$t_s = \\frac{E_{0t}}{E_{0i}} = \\frac{2n_1 \\cos\\theta_i}{n_1 \\cos\\theta_i + n_2 \\cos\\theta_t} = \\frac{2\\sin\\theta_t \\cos\\theta_i}{\\sin(\\theta_i + \\theta_t)}$$\n\n#### 2. Parallel Polarization ($p$ / TM):\n$$r_p = \\frac{E_{0r}}{E_{0i}} = \\frac{n_2 \\cos\\theta_i - n_1 \\cos\\theta_t}{n_2 \\cos\\theta_i + n_1 \\cos\\theta_t} = \\frac{\\tan(\\theta_i - \\theta_t)}{\\tan(\\theta_i + \\theta_t)}$$\n$$t_p = \\frac{E_{0t}}{E_{0i}} = \\frac{2n_1 \\cos\\theta_i}{n_2 \\cos\\theta_i + n_1 \\cos\\theta_t} = \\frac{2\\sin\\theta_t \\cos\\theta_i}{\\sin(\\theta_i + \\theta_t)\\cos(\\theta_i - \\theta_t)}$$\n",
          "simulation": "snell-refraction-sim"
        },
        {
          "secNumber": "3.4",
          "heading": "Brewster's Polarization Angle and External Reflection",
          "content": "\n#### Derivation of Brewster's Angle ($\\theta_B$)\nObserve the parallel reflection coefficient:\n$$r_p = \\frac{\\tan(\\theta_i - \\theta_t)}{\\tan(\\theta_i + \\theta_t)}$$\n\nIf the denominator approaches infinity, $r_p$ drops to identically zero. This occurs when:\n$$\\theta_i + \\theta_t = \\frac{\\pi}{2} = 90^\\circ \\implies \\theta_t = \\frac{\\pi}{2} - \\theta_i$$\n\nSubstitute this into Snell's law:\n$$n_1 \\sin\\theta_i = n_2 \\sin\\left( \\frac{\\pi}{2} - \\theta_i \\right) = n_2 \\cos\\theta_i$$\n$$\\frac{\\sin\\theta_i}{\\cos\\theta_i} = \\frac{n_2}{n_1} \\implies \\tan\\theta_B = \\frac{n_2}{n_1}$$\n\nThis unique angle of incidence is called **Brewster's Angle** (or the polarizing angle):\n$$\\theta_B = \\arctan\\left( \\frac{n_2}{n_1} \\right)$$\n\nFor an air-to-glass interface ($n_1 = 1.00, n_2 = 1.50$):\n$$\\theta_B = \\arctan(1.50) \\approx 56.3^\\circ$$\n\n#### Microscopic Physical Mechanism\nWhen incident light excites atomic bound electrons in medium 2, they oscillate parallel to the transmitted electric field vector $\\mathbf{E}_t$. Oscillating electric dipoles radiate with an intensity proportional to $\\sin^2\\phi$, where $\\phi$ is the angle between the dipole axis and the radiation direction. Because $\\theta_i + \\theta_t = 90^\\circ$, the direction of reflected ray $\\mathbf{k}_r$ lies precisely along the axis of oscillation of the dipoles! An oscillating dipole radiates zero electromagnetic power along its axis of oscillation. Hence, **no reflected wave can be generated for $p$-polarization**.\n\n**Practical Application:** If unpolarized sunlight strikes a glass window or water puddle at Brewster's angle, the reflected light is **100% linearly polarized** perpendicular to the plane of incidence ($s$-polarized). Polarized sunglasses with vertical transmission axes completely filter out this blinding horizontal glare.\n",
          "simulation": "fresnel-reflection"
        },
        {
          "secNumber": "3.5",
          "heading": "Total Internal Reflection, Evanescent Waves, and Penetration Depth",
          "content": "\n#### The Critical Angle ($\\theta_c$)\nWhen an electromagnetic wave travels from an optically denser medium into a rarer medium ($n_1 > n_2$, e.g., glass to air):\n$$n_1 \\sin\\theta_i = n_2 \\sin\\theta_t \\implies \\sin\\theta_t = \\frac{n_1}{n_2} \\sin\\theta_i$$\n\nAs $\\theta_i$ increases, $\\theta_t$ reaches $90^\\circ$ before $\\theta_i$ does. The angle of incidence for which $\\theta_t = 90^\\circ$ is the **critical angle**:\n$$\\sin\\theta_c = \\frac{n_2}{n_1} \\implies \\theta_c = \\arcsin\\left( \\frac{n_2}{n_1} \\right)$$\n\nFor water into air ($n_1 = 1.333, n_2 = 1.00$): $\\theta_c = \\arcsin(1/1.333) \\approx 48.6^\\circ$.\nFor glass into air ($n_1 = 1.50, n_2 = 1.00$): $\\theta_c = \\arcsin(1/1.50) \\approx 41.8^\\circ$.\n\n#### Total Internal Reflection ($\\theta_i > \\theta_c$)\nWhen $\\theta_i > \\theta_c$, $\\sin\\theta_t = \\frac{n_1}{n_2} \\sin\\theta_i > 1$. The cosine of the transmitted angle becomes purely imaginary:\n$$\\cos\\theta_t = \\sqrt{1 - \\sin^2\\theta_t} = \\sqrt{1 - \\left(\\frac{n_1}{n_2}\\sin\\theta_i\\right)^2} = i \\sqrt{\\left(\\frac{n_1}{n_2}\\sin\\theta_i\\right)^2 - 1} \\equiv i \\Gamma$$\n\nSubstituting into the transmitted spatial wave term $e^{i\\mathbf{k}_t \\cdot \\mathbf{r}} = e^{i(k_{tx} x + k_{tz} z)}$:\n$$k_{tz} = k_t \\cos\\theta_t = i k_t \\Gamma = i \\kappa$$\nwhere $\\kappa = \\frac{\\omega}{c} \\sqrt{n_1^2 \\sin^2\\theta_i - n_2^2}$.\n\nThe transmitted electric field is therefore:\n$$\\mathbf{E}_t(x, z, t) = \\mathbf{E}_{0t} e^{-\\kappa z} e^{i(k_{tx} x - \\omega t)}$$\n\n#### Properties of the Evanescent Wave\n1. **Exponential Decay:** The field amplitude decays exponentially into medium 2 with distance $z$ from the interface.\n2. **Characteristic Penetration Depth ($d_p$):**\n$$d_p = \\frac{1}{\\kappa} = \\frac{\\lambda_0}{2\\pi \\sqrt{n_1^2 \\sin^2\\theta_i - n_2^2}}$$\n3. **Zero Time-Averaged Power Transport:** The time-averaged Poynting vector normal to the boundary is identically zero: $\\langle S_z \\rangle = 0$. All energy is reflected back into medium 1 ($R = |r|^2 \\equiv 1.00$).\n4. **Frustrated Total Internal Reflection (FTIR):** If a third medium is placed within a distance $z < d_p$, photons tunnel through the gap via quantum-like electromagnetic barrier penetration, transmitting energy into the third medium.\n"
        },
        {
          "secNumber": "3.6",
          "heading": "Metallic Reflection at Optical and Microwave Frequencies",
          "content": "\nWhen an electromagnetic wave strikes a good conductor or metal (conductivity $\\sigma$), Snell's law and the Fresnel equations generalize by introducing the complex refractive index:\n$$\\tilde{n} = n + i\\kappa$$\nwhere $\\kappa = \\frac{c\\alpha}{\\omega}$ is the extinction coefficient.\n\nAt normal incidence from air ($n_1 = 1$) into metal:\n$$r = \\frac{1 - \\tilde{n}}{1 + \\tilde{n}} = \\frac{1 - (n + i\\kappa)}{1 + (n + i\\kappa)}$$\nThe reflectance is:\n$$R = |r|^2 = \\frac{(1 - n)^2 + \\kappa^2}{(1 + n)^2 + \\kappa^2}$$\n\nFor good conductors at microwave and radio frequencies, $\\kappa \\approx n \\gg 1$:\n$$R \\approx 1 - \\frac{4n}{n^2 + \\kappa^2} \\approx 1 - \\frac{4}{n} = 1 - 2\\sqrt{\\frac{2\\epsilon_0 \\omega}{\\sigma}}$$\n\nThis relation is the **Hagen-Rubens formula**. For polished metals (such as gold, silver, and copper), $R > 0.99$ for infrared and microwave radiation, making metals ideal mirrors and waveguide boundaries.\n"
        },
        {
          "secNumber": "3.7",
          "heading": "Waveguides: Parallel Conducting Plates & Rectangular Waveguides",
          "content": "\n#### Boundary Value Problem in Rectangular Waveguides\nConsider a hollow rectangular metallic pipe of inner width $a$ along $x$ ($0 \\le x \\le a$) and height $b$ along $y$ ($0 \\le y \\le b$), with walls made of an ideal conductor (conductivity $\\sigma \\to \\infty$). The wave propagates along $+z$:\n$$\\mathbf{E}(x, y, z, t) = \\mathbf{E}_0(x, y) e^{i(k_z z - \\omega t)}$$\n\nBecause the walls are perfect conductors, boundary conditions dictate that tangential $\\mathbf{E}$ and normal $\\mathbf{B}$ must vanish at the boundaries:\n$$E_z = 0, \\quad E_y = 0 \\quad \\text{at } x = 0, a$$\n$$E_z = 0, \\quad E_x = 0 \\quad \\text{at } y = 0, b$$\n\n#### Decomposition into Transverse Electric (TE) and Transverse Magnetic (TM) Modes\n1. **Transverse Electric (TE) Modes ($E_z = 0$):**\n   The longitudinal magnetic field $H_z$ satisfies the 2D Helmholtz equation:\n   $$\\left( \\frac{\\partial^2}{\\partial x^2} + \\frac{\\partial^2}{\\partial y^2} + k_c^2 \\right) H_z = 0, \\quad k_c^2 = \\frac{\\omega^2}{c^2} - k_z^2$$\n   Applying the boundary condition $\\frac{\\partial H_z}{\\partial n} = 0$:\n   $$H_z(x, y) = H_0 \\cos\\left( \\frac{m\\pi x}{a} \\right) \\cos\\left( \\frac{n\\pi y}{b} \\right)$$\n\n2. **Transverse Magnetic (TM) Modes ($H_z = 0$):**\n   Applying $E_z = 0$ on the walls:\n   $$E_z(x, y) = E_0 \\sin\\left( \\frac{m\\pi x}{a} \\right) \\sin\\left( \\frac{n\\pi y}{b} \\right)$$\n\n#### Cutoff Frequencies ($f_{c,mn}$)\nThe transverse cutoff wavenumber is:\n$$k_{c,mn} = \\sqrt{ \\left(\\frac{m\\pi}{a}\\right)^2 + \\left(\\frac{n\\pi}{b}\\right)^2 }$$\nThe **cutoff frequency** for mode $(m, n)$ is:\n$$f_{c,mn} = \\frac{c}{2\\pi} k_{c,mn} = \\frac{c}{2} \\sqrt{ \\left(\\frac{m}{a}\\right)^2 + \\left(\\frac{n}{b}\\right)^2 }$$\n\n#### Propagation Constant ($k_z$), Guide Wavelength ($\\lambda_g$), and Velocities\n$$k_z = \\sqrt{\\frac{\\omega^2}{c^2} - k_c^2} = \\frac{\\omega}{c} \\sqrt{1 - \\left(\\frac{f_c}{f}\\right)^2}$$\n\n- **If $f < f_c$:** $k_z$ is imaginary. The mode is evanescent and attenuates exponentially; **no wave propagation occurs**.\n- **If $f > f_c$:** $k_z$ is real and propagation proceeds.\n\nThe **guide wavelength** $\\lambda_g$ inside the pipe is:\n$$\\lambda_g = \\frac{2\\pi}{k_z} = \\frac{\\lambda_0}{\\sqrt{1 - (f_c/f)^2}} > \\lambda_0$$\n\nThe **phase velocity** exceeds the speed of light:\n$$v_p = \\frac{\\omega}{k_z} = \\frac{c}{\\sqrt{1 - (f_c/f)^2}} > c$$\n\nThe **group velocity** (energy velocity) is strictly subluminal:\n$$v_g = \\frac{d\\omega}{dk_z} = c \\sqrt{1 - \\left(\\frac{f_c}{f}\\right)^2} < c$$\nNotice that:\n$$v_p \\cdot v_g = c^2$$\n\n#### The Dominant Mode ($\\text{TE}_{10}$)\nIn standard rectangular waveguides with $a > b$, the lowest cutoff frequency belongs to the **$\\text{TE}_{10}$ mode** ($m=1, n=0$):\n$$f_{c,10} = \\frac{c}{2a}$$\nFor this dominant mode, the fields are:\n$$E_y(x) = E_0 \\sin\\left(\\frac{\\pi x}{a}\\right) e^{i(k_z z - \\omega t)}$$\n$$H_x(x) = -\\frac{k_z}{\\omega \\mu_0} E_0 \\sin\\left(\\frac{\\pi x}{a}\\right) e^{i(k_z z - \\omega t)}$$\n$$H_z(x) = i \\frac{\\pi}{\\omega \\mu_0 a} E_0 \\cos\\left(\\frac{\\pi x}{a}\\right) e^{i(k_z z - \\omega t)}$$\n",
          "simulation": "waveguide-modes"
        },
        {
          "secNumber": "3.8",
          "heading": "Resonant Cavities and Quality Factor (Q)",
          "content": "\n#### Resonant Microwave Cavities\nClosing both ends of a rectangular waveguide with conducting plates at $z = 0$ and $z = d$ forms a closed metallic enclosure called a **cavity resonator**.\n\nBoundary conditions force standing waves along all three spatial axes:\n$$f_{mnp} = \\frac{c}{2} \\sqrt{ \\left(\\frac{m}{a}\\right)^2 + \\left(\\frac{n}{b}\\right)^2 + \\left(\\frac{p}{d}\\right)^2 }$$\nwhere $m, n, p$ are mode integers.\n\n#### Quality Factor ($Q$)\nDue to the non-zero surface resistance $R_s$ of the metallic cavity walls, electromagnetic energy stored in the cavity is dissipated as thermal Joule losses. The **Quality Factor** $Q$ measures the sharpness of the cavity resonance:\n$$Q \\equiv \\omega \\frac{\\text{Time-averaged Energy Stored}}{\\text{Power Dissipated in Cavity Walls}} = \\omega \\frac{U}{P_{\\text{loss}}}$$\n\nFor microwave cavities constructed from copper or silver, $Q$ typically ranges from $10^4$ to $10^5$, and in superconducting niobium RF cavities used in particle colliders, $Q$ exceeds $10^{10}$.\n",
          "simulation": "cavity-resonator-sim"
        }
      ],
      "problems": [
        {
          "id": "p3-1",
          "title": "Example 3.1: Air-Glass Interface Reflection and Transmission at Normal Incidence",
          "difficulty": "Easy",
          "question": "A monochromatic laser beam in air ($n_1 = 1.00$) is incident normally upon a flat optical crown glass window ($n_2 = 1.52$). Calculate: (a) the amplitude reflection coefficient $r$ and transmission coefficient $t$, (b) the percentage of incident power reflected (Reflectance $R$), (c) the percentage of power transmitted (Transmittance $T$), and (d) the phase shift experienced by the reflected electric field.",
          "steps": [
            {
              "stepName": "Step 1: Amplitude Coefficients",
              "math": "r = \\frac{n_1 - n_2}{n_1 + n_2} = \\frac{1.00 - 1.52}{1.00 + 1.52} = \\frac{-0.52}{2.52} = -0.2063\\nt = \\frac{2n_1}{n_1 + n_2} = \\frac{2(1.00)}{2.52} = +0.7937",
              "explanation": "The negative sign on $r$ indicates an immediate $\\pi$ ($180^\\circ$) phase inversion for the reflected electric field."
            },
            {
              "stepName": "Step 2: Power Reflectance",
              "math": "R = |r|^2 = (-0.2063)^2 = 0.0426 \\implies 4.26\\%",
              "explanation": "Approximately 4.26% of incident light power is lost to Fresnel surface reflection at each air-glass boundary."
            },
            {
              "stepName": "Step 3: Power Transmittance",
              "math": "T = \\frac{n_2}{n_1} |t|^2 = \\frac{1.52}{1.00} (0.7937)^2 = 1.52 \\times 0.6299 = 0.9574 \\implies 95.74\\%\\nR + T = 4.26\\% + 95.74\\% = 100.00\\%",
              "explanation": "Energy conservation is verified exactly."
            }
          ]
        },
        {
          "id": "p3-2",
          "title": "Example 3.2: Complete Polarization of Sunlight Reflected from Water",
          "difficulty": "Medium",
          "question": "Unpolarized sunlight reflects from the smooth surface of a freshwater lake ($n_2 = 1.333$) into air ($n_1 = 1.00$). Determine: (a) Brewster's angle $\\theta_B$, (b) the corresponding refraction angle $\\theta_t$, (c) the reflectance for $s$-polarization $R_s$ at this angle, and (d) explain why reflected light is 100% linearly polarized.",
          "steps": [
            {
              "stepName": "Step 1: Brewster Angle Calculation",
              "math": "\\tan\\theta_B = \\frac{n_2}{n_1} = \\frac{1.333}{1.00} \\implies \\theta_B = \\arctan(1.333) = 53.12^\\circ",
              "explanation": "At an angle of incidence of $53.12^\\circ$, Brewster's condition is satisfied."
            },
            {
              "stepName": "Step 2: Refraction Angle Calculation",
              "math": "\\theta_t = 90^\\circ - \\theta_B = 90^\\circ - 53.12^\\circ = 36.88^\\circ",
              "explanation": "The reflected and refracted rays are precisely orthogonal to one another: $\\theta_r + \\theta_t = 90^\\circ$."
            },
            {
              "stepName": "Step 3: Reflectance for Perpendicular Polarization",
              "math": "r_s = -\\frac{\\sin(\\theta_i - \\theta_t)}{\\sin(\\theta_i + \\theta_t)} = -\\frac{\\sin(53.12^\\circ - 36.88^\\circ)}{\\sin(90^\\circ)} = -\\sin(16.24^\\circ) = -0.2796\\nR_s = |r_s|^2 = (-0.2796)^2 = 0.0782 \\implies 7.82\\%\\nR_p = 0.00\\%",
              "explanation": "Because $R_p = 0$, all reflected photons belong exclusively to the perpendicular state ($s$-polarization), producing 100% linearly polarized horizontal glare."
            }
          ]
        },
        {
          "id": "p3-3",
          "title": "Example 3.3: X-Band Rectangular Waveguide Cutoff, Dispersion, and Velocities",
          "difficulty": "Hard",
          "question": "A standard WR-90 X-band rectangular waveguide has internal dimensions $a = 2.286\\text{ cm}$ and $b = 1.016\\text{ cm}$. For operation at $f = 9.80\\text{ GHz}$: (a) calculate the cutoff frequencies for modes $\\text{TE}_{10}$, $\\text{TE}_{20}$, and $\\text{TE}_{01}$, (b) confirm single-mode operation, (c) calculate the guide wavelength $\\lambda_g$, (d) calculate the phase velocity $v_p$, and (e) calculate the group velocity $v_g$.",
          "steps": [
            {
              "stepName": "Step 1: Cutoff Frequency Calculations",
              "math": "f_{c,10} = \\frac{c}{2a} = \\frac{3.00 \\times 10^{10}\\text{ cm/s}}{2(2.286\\text{ cm})} = 6.557\\text{ GHz}\\nf_{c,20} = \\frac{c}{a} = 2 \\times 6.557\\text{ GHz} = 13.114\\text{ GHz}\\nf_{c,01} = \\frac{c}{2b} = \\frac{3.00 \\times 10^{10}\\text{ cm/s}}{2(1.016\\text{ cm})} = 14.764\\text{ GHz}",
              "explanation": "At $f = 9.80\\text{ GHz}$, since $f_{c,10} < f < f_{c,20} < f_{c,01}$, only the dominant $\\text{TE}_{10}$ mode can propagate; all higher-order modes are evanescent."
            },
            {
              "stepName": "Step 2: Guide Wavelength Calculation",
              "math": "\\lambda_0 = \\frac{c}{f} = \\frac{3.00 \\times 10^8\\text{ m/s}}{9.80 \\times 10^9\\text{ Hz}} = 3.061\\text{ cm}\\n\\lambda_g = \\frac{\\lambda_0}{\\sqrt{1 - (f_{c,10}/f)^2}} = \\frac{3.061\\text{ cm}}{\\sqrt{1 - (6.557/9.80)^2}} = \\frac{3.061\\text{ cm}}{\\sqrt{1 - 0.4477}} = \\frac{3.061\\text{ cm}}{0.7431} = 4.119\\text{ cm}",
              "explanation": "The wavelength inside the waveguide is stretched by 35% compared to free space."
            },
            {
              "stepName": "Step 3: Phase and Group Velocities",
              "math": "v_p = \\frac{c}{\\sqrt{1 - (f_{c,10}/f)^2}} = \\frac{3.00 \\times 10^8\\text{ m/s}}{0.7431} = 4.037 \\times 10^8\\text{ m/s} = 1.346 \\, c\\nv_g = c \\sqrt{1 - (f_{c,10}/f)^2} = (3.00 \\times 10^8\\text{ m/s})(0.7431) = 2.229 \\times 10^8\\text{ m/s} = 0.743 \\, c\\nv_p \\times v_g = (1.346 c)(0.743 c) = c^2",
              "explanation": "The phase velocity exceeds $c$ without violating causality because signal information travels at group velocity $v_g < c$."
            }
          ]
        },
        {
          "id": "p3-4",
          "title": "Example 3.4: Resonant Frequency and Quality Factor (Q) of a Microwave Cavity",
          "difficulty": "Hard",
          "question": "A cubic resonant cavity has dimensions $a = b = d = 5.0\\text{ cm}$ with walls made of pure copper ($\\sigma = 5.8 \\times 10^7\\text{ S/m}$). Calculate: (a) the lowest resonant frequency $f_{101}$ for the dominant $\\text{TE}_{101}$ mode, (b) the skin depth $\\delta$ at resonance, and (c) the theoretical quality factor $Q$ of the cavity.",
          "steps": [
            {
              "stepName": "Step 1: Resonant Frequency Calculation",
              "math": "f_{101} = \\frac{c}{2} \\sqrt{\\frac{1}{a^2} + 0 + \\frac{1}{d^2}} = \\frac{c}{2} \\sqrt{\\frac{2}{a^2}} = \\frac{c}{\\sqrt{2} a}\\nf_{101} = \\frac{3.00 \\times 10^8\\text{ m/s}}{\\sqrt{2}(0.05\\text{ m})} = \\frac{3.00 \\times 10^8}{0.07071} = 4.243 \\times 10^9\\text{ Hz} = 4.243\\text{ GHz}",
              "explanation": "The fundamental resonant frequency is 4.243 GHz in the C-band."
            },
            {
              "stepName": "Step 2: Skin Depth at Resonance",
              "math": "\\delta = \\frac{1}{\\sqrt{\\pi f \\mu_0 \\sigma}} = \\frac{1}{\\sqrt{\\pi (4.243 \\times 10^9)(4\\pi \\times 10^{-7})(5.8 \\times 10^7)}} = 1.013 \\times 10^{-6}\\text{ m} = 1.013\\,\\mu\\text{m}",
              "explanation": "Microwave wall currents penetrate only 1.01 micrometers into the copper surface."
            },
            {
              "stepName": "Step 3: Quality Factor (Q) Calculation",
              "math": "\\text{For a cubic cavity of side } a: Q = \\frac{a}{3\\delta}\\nQ = \\frac{0.05\\text{ m}}{3(1.013 \\times 10^{-6}\\text{ m})} = \\frac{0.05}{3.039 \\times 10^{-6}} = 16,450",
              "explanation": "The extraordinarily high Q-factor of 16,450 confirms minimal internal dissipation, storing electromagnetic energy for over 16,000 oscillation cycles before decaying."
            }
          ]
        }
      ]
    },
    {
      "id": "unit-4",
      "number": 4,
      "title": "Electrodynamic Potentials, Gauge Freedom & Radiation",
      "leadSummary": "Comprehensive mathematical formulation of relativistic electrodynamics and radiation theory: vector potential A and scalar potential V, gauge transformations and degrees of freedom, Coulomb versus Lorentz gauge conditions, retarded Green's functions, causal retarded potentials, Liénard-Wiechert potentials for relativistic moving charges, electric and magnetic fields of accelerated charges (velocity vs acceleration terms), complete step-by-step vector derivation of oscillating Hertzian electric dipole radiation, far-field Poynting flux, the Larmor dipole power formula, radiation resistance, magnetic dipole radiation, and half-wave center-fed antenna theory.",
      "simulations": [
        "dipole-radiation"
      ],
      "sections": [
        {
          "secNumber": "4.1",
          "heading": "Electromagnetic Potentials (V, A) and Field Formulations",
          "content": "\n#### Definition of Potentials in Time-Dependent Electrodynamics\nIn static electromagnetism, $\\nabla \\times \\mathbf{E} = 0$ allows us to express the electric field as the gradient of a scalar potential, $\\mathbf{E} = -\\nabla V$. In dynamic electrodynamics, however, Faraday's law states:\n$$\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$$\nBecause $\\nabla \\times \\mathbf{E} \\neq 0$, $\\mathbf{E}$ cannot be written as the gradient of a scalar alone.\n\nHowever, Gauss's law for magnetism remains strictly valid:\n$$\\nabla \\cdot \\mathbf{B} = 0$$\nSince the divergence of any curl vanishes identically ($\\nabla \\cdot (\\nabla \\times \\mathbf{A}) \\equiv 0$), we can always define the **magnetic vector potential** $\\mathbf{A}$:\n$$\\mathbf{B} \\equiv \\nabla \\times \\mathbf{A}$$\n\nSubstitute this definition into Faraday's law:\n$$\\nabla \\times \\mathbf{E} = -\\frac{\\partial}{\\partial t} (\\nabla \\times \\mathbf{A}) = -\\nabla \\times \\left( \\frac{\\partial \\mathbf{A}}{\\partial t} \\right)$$\n$$\\nabla \\times \\left( \\mathbf{E} + \\frac{\\partial \\mathbf{A}}{\\partial t} \\right) = 0$$\n\nBecause the quantity in parentheses has zero curl, it can now be expressed as the negative gradient of a dynamic **electric scalar potential** $V$:\n$$\\mathbf{E} + \\frac{\\partial \\mathbf{A}}{\\partial t} = -\\nabla V \\implies \\mathbf{E} = -\\nabla V - \\frac{\\partial \\mathbf{A}}{\\partial t}$$\n\nThese two equations represent the fundamental relations expressing physical fields $(\\mathbf{E}, \\mathbf{B})$ in terms of electromagnetic potentials $(V, \\mathbf{A})$:\n$$\\mathbf{B} = \\nabla \\times \\mathbf{A}$$\n$$\\mathbf{E} = -\\nabla V - \\frac{\\partial \\mathbf{A}}{\\partial t}$$\n"
        },
        {
          "secNumber": "4.2",
          "heading": "Gauge Invariance: Coulomb Gauge and Lorentz Gauge Conditions",
          "content": "\n#### Gauge Transformations\nPotentials are not directly observable physical quantities; only fields $\\mathbf{E}$ and $\\mathbf{B}$ exert measurable Lorentz forces. If we modify $\\mathbf{A}$ and $V$ through a transformation involving an arbitrary scalar gauge function $\\lambda(\\mathbf{r}, t)$:\n$$\\mathbf{A}' = \\mathbf{A} + \\nabla \\lambda$$\n$$V' = V - \\frac{\\partial \\lambda}{\\partial t}$$\n\nLet us compute the new fields:\n$$\\mathbf{B}' = \\nabla \\times \\mathbf{A}' = \\nabla \\times (\\mathbf{A} + \\nabla \\lambda) = \\nabla \\times \\mathbf{A} + 0 = \\mathbf{B}$$\n$$\\mathbf{E}' = -\\nabla V' - \\frac{\\partial \\mathbf{A}'}{\\partial t} = -\\nabla \\left( V - \\frac{\\partial \\lambda}{\\partial t} \\right) - \\frac{\\partial}{\\partial t} (\\mathbf{A} + \\nabla \\lambda) = -\\nabla V + \\nabla \\frac{\\partial \\lambda}{\\partial t} - \\frac{\\partial \\mathbf{A}}{\\partial t} - \\frac{\\partial \\nabla \\lambda}{\\partial t} = \\mathbf{E}$$\n\nThe physical fields are completely invariant under this **gauge transformation**. This mathematical freedom (gauge freedom) allows us to impose convenient constraints on the divergence of $\\mathbf{A}$.\n\n#### 1. The Coulomb Gauge (Radiation Gauge)\nSet the constraint:\n$$\\nabla \\cdot \\mathbf{A} = 0$$\nSubstituting into Gauss's law $\\nabla \\cdot \\mathbf{E} = \\rho / \\epsilon_0$:\n$$\\nabla \\cdot \\left( -\\nabla V - \\frac{\\partial \\mathbf{A}}{\\partial t} \\right) = -\\nabla^2 V - \\frac{\\partial}{\\partial t}(\\nabla \\cdot \\mathbf{A}) = \\frac{\\rho}{\\epsilon_0}$$\nSince $\\nabla \\cdot \\mathbf{A} = 0$:\n$$\\nabla^2 V = -\\frac{\\rho}{\\epsilon_0}$$\nThis is the standard Poisson equation. The scalar potential in Coulomb gauge is:\n$$V(\\mathbf{r}, t) = \\frac{1}{4\\pi \\epsilon_0} \\int \\frac{\\rho(\\mathbf{r}', t)}{|\\mathbf{r} - \\mathbf{r}'|} \\, d\\tau'$$\nWhile computationally convenient in quantum electrodynamics and atomic physics, $V$ in Coulomb gauge appears to propagate instantaneously, disguising relativistic causality.\n\n#### 2. The Lorentz Gauge Condition\nTo preserve manifest relativistic covariance and causality, Ludvig Lorenz (and later Hendrik Lorentz) introduced the condition:\n$$\\nabla \\cdot \\mathbf{A} + \\frac{1}{c^2} \\frac{\\partial V}{\\partial t} = 0$$\n\nSubstitute $(V, \\mathbf{A})$ into the inhomogeneous Maxwell equations (Gauss's law and Ampère-Maxwell law). Both coupled equations decouple completely into symmetric 4D **inhomogeneous d'Alembertian wave equations**:\n$$\\nabla^2 V - \\frac{1}{c^2} \\frac{\\partial^2 V}{\\partial t^2} = -\\frac{\\rho}{\\epsilon_0} \\quad \\iff \\quad \\Box V = -\\frac{\\rho}{\\epsilon_0}$$\n$$\\nabla^2 \\mathbf{A} - \\frac{1}{c^2} \\frac{\\partial^2 \\mathbf{A}}{\\partial t^2} = -\\mu_0 \\mathbf{J} \\quad \\iff \\quad \\Box \\mathbf{A} = -\\mu_0 \\mathbf{J}$$\nwhere $\\Box \\equiv \\nabla^2 - \\frac{1}{c^2}\\frac{\\partial^2}{\\partial t^2}$ is the d'Alembertian operator.\n"
        },
        {
          "secNumber": "4.3",
          "heading": "Retarded Potentials and Causal Green's Function Solutions",
          "content": "\n#### The Retardation Principle\nBecause electromagnetic signals propagate through space at the finite speed of light $c$, the potential at an observation point $\\mathbf{r}$ at time $t$ cannot depend on what source charges and currents are doing *at that exact moment*. Instead, it depends on their behavior at an earlier time $t_r$ (the **retarded time**), accounting for the travel time of light:\n$$t_r \\equiv t - \\frac{|\\mathbf{r} - \\mathbf{r}'|}{c} = t - \\frac{\\imath}{c}$$\nwhere $\\boldsymbol{\\imath} = \\mathbf{r} - \\mathbf{r}'$ is the separation vector and $\\imath = |\\mathbf{r} - \\mathbf{r}'|$.\n\nUsing the retarded Green's function of the d'Alembertian operator:\n$$G(\\mathbf{r}, t; \\mathbf{r}', t') = \\frac{\\delta(t - t' - \\imath/c)}{4\\pi \\imath}$$\n\nThe exact solutions to the decoupled wave equations in Lorentz gauge are the **Retarded Potentials**:\n$$V(\\mathbf{r}, t) = \\frac{1}{4\\pi \\epsilon_0} \\int \\frac{\\rho(\\mathbf{r}', t_r)}{\\imath} \\, d\\tau' = \\frac{1}{4\\pi \\epsilon_0} \\int \\frac{\\rho(\\mathbf{r}', t - \\imath/c)}{|\\mathbf{r} - \\mathbf{r}'|} \\, d\\tau'$$\n$$\\mathbf{A}(\\mathbf{r}, t) = \\frac{\\mu_0}{4\\pi} \\int \\frac{\\mathbf{J}(\\mathbf{r}', t_r)}{\\imath} \\, d\\tau' = \\frac{\\mu_0}{4\\pi} \\int \\frac{\\mathbf{J}(\\mathbf{r}', t - \\imath/c)}{|\\mathbf{r} - \\mathbf{r}'|} \\, d\\tau'$$\n\nThese equations encapsulate relativistic causality: an event at the source point $\\mathbf{r}'$ can only affect the field point $\\mathbf{r}$ after the light-cone delay $\\Delta t = \\imath/c$ has elapsed.\n",
          "simulation": "retarded-potential-sim"
        },
        {
          "secNumber": "4.4",
          "heading": "Liénard-Wiechert Potentials for a Relativistic Moving Point Charge",
          "content": "\n#### Potentials of a Point Charge on an Arbitrary Trajectory\nConsider a point charge $q$ moving along an arbitrary trajectory $\\mathbf{w}(t)$ with velocity $\\mathbf{v}(t) = \\dot{\\mathbf{w}}(t)$. Because the charge is moving, different parts of the charge distribution during an integration volume emit signals that arrive at observation point $\\mathbf{r}$ at the same time $t$. This geometric elongation introduces a Doppler-like Jacobian volume factor:\n$$d\\tau' = \\frac{d\\tau}{1 - \\hat{\\boldsymbol{\\imath}} \\cdot \\boldsymbol{\\beta}}$$\nwhere $\\boldsymbol{\\beta} = \\frac{\\mathbf{v}}{c}$ and $\\hat{\\boldsymbol{\\imath}} = \\frac{\\mathbf{r} - \\mathbf{w}(t_r)}{|\\mathbf{r} - \\mathbf{w}(t_r)|}$.\n\nCarrying out the 4D delta-function integral yields the celebrated **Liénard-Wiechert Potentials** (Alfred-Marie Liénard 1898, Emil Wiechert 1900):\n$$V(\\mathbf{r}, t) = \\frac{1}{4\\pi \\epsilon_0} \\frac{q}{\\imath - \\frac{\\boldsymbol{\\imath} \\cdot \\mathbf{v}}{c}} = \\frac{1}{4\\pi \\epsilon_0} \\frac{q}{\\imath (1 - \\hat{\\boldsymbol{\\imath}} \\cdot \\boldsymbol{\\beta})}$$\n$$\\mathbf{A}(\\mathbf{r}, t) = \\frac{\\mu_0}{4\\pi} \\frac{q \\mathbf{v}}{\\imath - \\frac{\\boldsymbol{\\imath} \\cdot \\mathbf{v}}{c}} = \\frac{\\mathbf{v}}{c^2} V(\\mathbf{r}, t)$$\nwhere all source quantities $(\\mathbf{w}, \\mathbf{v}, \\boldsymbol{\\beta}, \\imath)$ are evaluated at the retarded time $t_r$ satisfying $c(t - t_r) = |\\mathbf{r} - \\mathbf{w}(t_r)|$.\n"
        },
        {
          "secNumber": "4.5",
          "heading": "Electric and Magnetic Fields of Accelerated Charges (Velocity vs Radiation Fields)",
          "content": "\n#### Computing the Fields from Liénard-Wiechert Potentials\nDifferentiating the potentials $\\mathbf{E} = -\\nabla V - \\frac{\\partial \\mathbf{A}}{\\partial t}$ and $\\mathbf{B} = \\nabla \\times \\mathbf{A}$ requires taking gradients and time derivatives through the implicit dependence on retarded time $\\nabla t_r = -\\frac{\\hat{\\boldsymbol{\\imath}}}{c(1 - \\hat{\\boldsymbol{\\imath}} \\cdot \\boldsymbol{\\beta})}$.\n\nThe resulting electric field separates into two distinct physical terms:\n$$\\mathbf{E}(\\mathbf{r}, t) = \\mathbf{E}_{\\text{velocity}} + \\mathbf{E}_{\\text{acceleration}}$$\n$$\\mathbf{E}(\\mathbf{r}, t) = \\frac{q}{4\\pi \\epsilon_0} \\frac{\\imath}{(\\boldsymbol{\\imath} \\cdot \\mathbf{u})^3} \\left[ (c^2 - v^2) \\mathbf{u} + \\boldsymbol{\\imath} \\times (\\mathbf{u} \\times \\mathbf{a}) \\right]$$\nwhere $\\mathbf{u} \\equiv c \\hat{\\boldsymbol{\\imath}} - \\mathbf{v}$ and $\\mathbf{a} = \\dot{\\mathbf{v}}(t_r)$ is the charge acceleration evaluated at retarded time.\n\nThe magnetic induction field is strictly orthogonal and transverse:\n$$\\mathbf{B}(\\mathbf{r}, t) = \\frac{1}{c} \\left( \\hat{\\boldsymbol{\\imath}} \\times \\mathbf{E}(\\mathbf{r}, t) \\right)$$\n\n#### Decomposition and Physical Significance\n1. **The Velocity Field (Generalized Coulomb Field):**\n$$\\mathbf{E}_{\\text{velocity}} \\propto \\frac{c^2 - v^2}{\\imath^2}$$\nDecays as $1/\\imath^2$ with distance. It is carried along with the moving charge and represents bound field energy that cannot escape to infinity.\n\n2. **The Acceleration Field (Radiation Field):**\n$$\\mathbf{E}_{\\text{acceleration}} = \\frac{q}{4\\pi \\epsilon_0 c^2} \\frac{\\hat{\\boldsymbol{\\imath}} \\times (\\mathbf{u} \\times \\mathbf{a})}{(\\boldsymbol{\\imath} \\cdot \\mathbf{u})^3} \\propto \\frac{1}{\\imath}$$\nDecays as $1/\\imath$ with distance! The associated Poynting energy flux scales as:\n$$S \\propto E_{\\text{rad}}^2 \\propto \\frac{1}{\\imath^2}$$\nWhen integrated over a giant sphere of radius $\\imath \\to \\infty$, the surface area $4\\pi \\imath^2$ cancels the $1/\\imath^2$ decay:\n$$\\oint_{S_\\infty} \\mathbf{S} \\cdot d\\mathbf{a} = \\text{constant} \\neq 0$$\n\n**Fundamental Theorem of Classical Electrodynamics:** A charge moving with uniform velocity ($a = 0$) does NOT radiate. **Only an accelerated charge ($a \\neq 0$) radiates electromagnetic energy to infinity.**\n"
        },
        {
          "secNumber": "4.6",
          "heading": "Electric Dipole Radiation (Oscillating Hertzian Dipole)",
          "content": "\n#### The Oscillating Electric Dipole Model\nConsider two tiny conducting spheres separated by a distance $d$ along the $z$-axis, connected by a thin filament carrying an alternating current. The electric dipole moment oscillates harmonically:\n$$\\mathbf{p}(t) = p_0 \\cos(\\omega t) \\hat{\\mathbf{z}}$$\nwhere $p_0 = q_0 d$.\n\nWe evaluate the fields under the standard **radiation zone approximations**:\n1. Short dipole compared to wavelength: $d \\ll \\lambda$ (dipole approximation)\n2. Far radiation field: $r \\gg \\lambda \\gg d$ where $\\lambda = 2\\pi c/\\omega$\n\n#### Derivation of the Radiation Zone Fields\nThe retarded vector potential in spherical coordinates $(r, \\theta, \\phi)$ in the far zone is:\n$$\\mathbf{A}(r, \\theta, t) = -\\frac{\\mu_0 p_0 \\omega}{4\\pi r} \\sin(\\omega(t - r/c)) \\hat{\\mathbf{z}}$$\nConverting $\\hat{\\mathbf{z}} = \\cos\\theta \\hat{\\mathbf{r}} - \\sin\\theta \\hat{\\boldsymbol{\\theta}}$:\n$$\\mathbf{A}(r, \\theta, t) = -\\frac{\\mu_0 p_0 \\omega}{4\\pi r} \\sin(\\omega(t - r/c)) (\\cos\\theta \\hat{\\mathbf{r}} - \\sin\\theta \\hat{\\boldsymbol{\\theta}})$$\n\nComputing $\\mathbf{B} = \\nabla \\times \\mathbf{A}$ keeping only terms scaling as $1/r$:\n$$\\mathbf{B}(r, \\theta, t) = -\\frac{\\mu_0 p_0 \\omega^2}{4\\pi c} \\left( \\frac{\\sin\\theta}{r} \\right) \\cos(\\omega(t - r/c)) \\hat{\\boldsymbol{\\phi}}$$\n\nFrom $\\mathbf{E} = c(\\mathbf{B} \\times \\hat{\\mathbf{r}})$:\n$$\\mathbf{E}(r, \\theta, t) = -\\frac{\\mu_0 p_0 \\omega^2}{4\\pi} \\left( \\frac{\\sin\\theta}{r} \\right) \\cos(\\omega(t - r/c)) \\hat{\\boldsymbol{\\theta}}$$\n\n#### Key Physical Characteristics\n1. **Transverse Wave:** $\\mathbf{E}$ points along $\\hat{\\boldsymbol{\\theta}}$, $\\mathbf{B}$ points along $\\hat{\\boldsymbol{\\phi}}$, and propagation is radially outward along $\\hat{\\mathbf{r}}$.\n2. **Frequency Dependence:** Field amplitudes are proportional to $\\omega^2$ (or $1/\\lambda^2$). High frequencies radiate vastly more efficiently than low frequencies.\n3. **Angular Profile:** Fields vanish along the dipole axis ($\\theta = 0, \\pi$) and peak in the equatorial plane ($\\theta = \\pi/2$).\n",
          "simulation": "dipole-radiation"
        },
        {
          "secNumber": "4.7",
          "heading": "Poynting Flux, Radiation Pattern, and the Larmor Power Formula",
          "content": "\n#### Instantaneous and Time-Averaged Poynting Vector\nThe Poynting vector in the radiation zone is:\n$$\\mathbf{S}(r, \\theta, t) = \\frac{1}{\\mu_0} (\\mathbf{E} \\times \\mathbf{B}) = \\frac{\\mu_0 p_0^2 \\omega^4}{16\\pi^2 c} \\left( \\frac{\\sin^2\\theta}{r^2} \\right) \\cos^2(\\omega(t - r/c)) \\hat{\\mathbf{r}}$$\n\nTaking the time average over an oscillation cycle ($\\langle \\cos^2 \\rangle = 1/2$):\n$$\\langle \\mathbf{S} \\rangle = \\frac{\\mu_0 p_0^2 \\omega^4}{32\\pi^2 c} \\frac{\\sin^2\\theta}{r^2} \\hat{\\mathbf{r}}$$\n\n#### The Toroidal Doughnut Radiation Pattern\nThe radiated intensity depends on angle as $\\sin^2\\theta$:\n- **Broadside ($\\theta = 90^\\circ$):** Maximum radiation flux perpendicular to the dipole axis.\n- **Endfire ($\\theta = 0^\\circ, 180^\\circ$):** Zero radiation along the axis of the antenna wire.\n\n#### Total Radiated Power: Larmor's Formula for Dipoles\nIntegrating $\\langle \\mathbf{S} \\rangle$ over a closed sphere of radius $r$:\n$$P = \\oint \\langle \\mathbf{S} \\rangle \\cdot d\\mathbf{a} = \\int_0^{2\\pi} d\\phi \\int_0^\\pi \\left( \\frac{\\mu_0 p_0^2 \\omega^4}{32\\pi^2 c} \\frac{\\sin^2\\theta}{r^2} \\right) r^2 \\sin\\theta \\, d\\theta$$\n$$P = \\frac{\\mu_0 p_0^2 \\omega^4}{32\\pi^2 c} (2\\pi) \\int_0^\\pi \\sin^3\\theta \\, d\\theta$$\n\nThe standard integral is $\\int_0^\\pi \\sin^3\\theta \\, d\\theta = \\frac{4}{3}$:\n$$P = \\frac{\\mu_0 p_0^2 \\omega^4}{16\\pi c} \\left( \\frac{4}{3} \\right) = \\frac{\\mu_0 p_0^2 \\omega^4}{12\\pi c}$$\n\nIn terms of the speed of light in vacuum ($c = 1/\\sqrt{\\epsilon_0 \\mu_0}$):\n$$P = \\frac{p_0^2 \\omega^4}{12\\pi \\epsilon_0 c^3}$$\n\nThis is the celebrated **Larmor Formula for an Oscillating Dipole**. Notice the profound $\\omega^4$ frequency dependence: doubling the frequency increases the radiated power by a factor of $2^4 = 16$.\n\n#### Radiation Resistance of a Short Dipole Antenna\nThe current feeding the dipole is $I(t) = \\dot{q}(t) = -q_0 \\omega \\sin(\\omega t)$, with amplitude $I_0 = q_0 \\omega$. Thus $p_0 = q_0 d = \\frac{I_0 d}{\\omega}$.\nSubstituting into the total power formula:\n$$P = \\frac{\\mu_0 (I_0 d / \\omega)^2 \\omega^4}{12\\pi c} = \\frac{\\mu_0 I_0^2 d^2 \\omega^2}{12\\pi c} = \\frac{1}{2} I_0^2 R_{\\text{rad}}$$\n\nEquating to the equivalent dissipated circuit power $P = \\frac{1}{2} I_0^2 R_{\\text{rad}}$:\n$$R_{\\text{rad}} = \\frac{\\mu_0 d^2 \\omega^2}{6\\pi c} = \\frac{\\mu_0 c}{6\\pi} \\left( \\frac{\\omega d}{c} \\right)^2 = \\frac{120\\pi}{6\\pi} \\left( \\frac{2\\pi d}{\\lambda} \\right)^2 = 80\\pi^2 \\left( \\frac{d}{\\lambda} \\right)^2 \\, \\Omega$$\n\nFor a short dipole where $d \\ll \\lambda$ (e.g., $d = 0.05\\lambda$):\n$$R_{\\text{rad}} = 80\\pi^2 (0.05)^2 \\approx 1.97 \\, \\Omega$$\nBecause radiation resistance is tiny, short antennas match poorly to standard $50\\,\\Omega$ RF lines, radiating inefficiently.\n"
        },
        {
          "secNumber": "4.8",
          "heading": "Magnetic Dipole Radiation and Center-Fed Half-Wave Antennas",
          "content": "\n#### Magnetic Dipole Radiation\nAn oscillating circular loop of radius $b$ carrying alternating current $I(t) = I_0 \\cos(\\omega t)$ constitutes an oscillating magnetic dipole $\\mathbf{m}(t) = m_0 \\cos(\\omega t) \\hat{\\mathbf{z}}$, where $m_0 = \\pi b^2 I_0$.\n\nThe radiation zone fields are:\n$$\\mathbf{E}(r, \\theta, t) = \\frac{\\mu_0 m_0 \\omega^2}{4\\pi c} \\left( \\frac{\\sin\\theta}{r} \\right) \\cos(\\omega(t - r/c)) \\hat{\\boldsymbol{\\phi}}$$\n$$\\mathbf{B}(r, \\theta, t) = -\\frac{\\mu_0 m_0 \\omega^2}{4\\pi c^2} \\left( \\frac{\\sin\\theta}{r} \\right) \\cos(\\omega(t - r/c)) \\hat{\\boldsymbol{\\theta}}$$\n\nThe total radiated power is:\n$$P_{\\text{mag}} = \\frac{\\mu_0 m_0^2 \\omega^4}{12\\pi c^3}$$\n\n#### Comparison Between Electric and Magnetic Dipoles\nFor comparable geometric dimensions ($p_0 \\sim q d, m_0 \\sim I d^2 \\sim q \\omega d^2$):\n$$\\frac{P_{\\text{mag}}}{P_{\\text{elec}}} = \\left( \\frac{\\omega d}{c} \\right)^2 = \\left( \\frac{2\\pi d}{\\lambda} \\right)^2 \\ll 1$$\nMagnetic dipole radiation is suppressed by a factor of $(d/\\lambda)^2$ relative to electric dipole radiation. Electric dipole transitions (E1) are vastly stronger than magnetic dipole (M1) atomic transitions.\n\n#### The Center-Fed Half-Wave Antenna ($L = \\lambda/2$)\nPractical radio communications employ resonant antennas of length $L = \\lambda/2$. The current distribution is a standing wave that vanishes at the endpoints $z = \\pm L/2$:\n$$I(z) = I_0 \\cos(kz) e^{-i\\omega t}$$\nwhere $k = \\frac{2\\pi}{\\lambda} = \\frac{\\pi}{L}$.\n\nIntegrating across the antenna length yields the far-field radiation pattern:\n$$\\langle \\mathbf{S} \\rangle = \\frac{\\eta_0 I_0^2}{8\\pi^2 r^2} \\left[ \\frac{\\cos\\left( \\frac{\\pi}{2}\\cos\\theta \\right)}{\\sin\\theta} \\right]^2 \\hat{\\mathbf{r}}$$\n\nIntegrating over a sphere gives the total power radiated:\n$$P = \\frac{\\eta_0 I_0^2}{4\\pi} \\int_0^\\pi \\frac{\\cos^2\\left(\\frac{\\pi}{2}\\cos\\theta\\right)}{\\sin\\theta} \\, d\\theta = \\frac{120\\pi I_0^2}{4\\pi} (1.2188) = 36.56 I_0^2 = \\frac{1}{2} I_0^2 R_{\\text{rad}}$$\n\nSolving for the radiation resistance of a resonant half-wave antenna:\n$$R_{\\text{rad}} = 2 \\times 36.56 \\, \\Omega \\approx 73.13 \\, \\Omega$$\n\n**Engineering Significance:** A radiation resistance of $73\\,\\Omega$ provides an outstanding impedance match to standard coaxial transmission cables ($50\\,\\Omega$ or $75\\,\\Omega$), making half-wave dipoles the universal cornerstone of modern telecommunications.\n",
          "simulation": "antenna-radiation-sim"
        }
      ],
      "problems": [
        {
          "id": "p4-1",
          "title": "Example 4.1: Gauge Transformation Connecting Coulomb and Lorentz Gauges",
          "difficulty": "Medium",
          "question": "A vector potential in a region is given by $\\mathbf{A}_1 = A_0 \\cos(kz - \\omega t) \\hat{\\mathbf{x}}$ and $V_1 = 0$. (a) Determine whether this potential satisfies the Coulomb gauge condition. (b) Determine whether it satisfies the Lorentz gauge condition. (c) Construct a gauge function $\\lambda(\\mathbf{r}, t)$ that transforms $\\mathbf{A}_1$ into a new vector potential $\\mathbf{A}_2$ and scalar potential $V_2$ such that the Lorentz gauge condition is explicitly satisfied.",
          "steps": [
            {
              "stepName": "Step 1: Check Coulomb Gauge Condition",
              "math": "\\nabla \\cdot \\mathbf{A}_1 = \\frac{\\partial A_{1x}}{\\partial x} = \\frac{\\partial}{\\partial x}[A_0 \\cos(kz - \\omega t)] = 0",
              "explanation": "Since $\\mathbf{A}_1$ points along $\\hat{\\mathbf{x}}$ and varies only with $z$, its spatial divergence is identically zero. Thus, $\\mathbf{A}_1$ satisfies the Coulomb gauge."
            },
            {
              "stepName": "Step 2: Check Lorentz Gauge Condition",
              "math": "\\nabla \\cdot \\mathbf{A}_1 + \\frac{1}{c^2}\\frac{\\partial V_1}{\\partial t} = 0 + 0 = 0",
              "explanation": "Remarkably, because both $\\nabla \\cdot \\mathbf{A}_1 = 0$ and $\\frac{\\partial V_1}{\\partial t} = 0$, this specific potential simultaneously satisfies both the Coulomb and Lorentz gauge conditions (this is the transverse radiation gauge)."
            },
            {
              "stepName": "Step 3: Verification of Physical Fields",
              "math": "\\mathbf{B} = \\nabla \\times \\mathbf{A}_1 = \\left| \\begin{matrix} \\hat{\\mathbf{x}} & \\hat{\\mathbf{y}} & \\hat{\\mathbf{z}} \\\\ \\partial_x & \\partial_y & \\partial_z \\\\ A_0\\cos(kz-\\omega t) & 0 & 0 \\end{matrix} \\right| = k A_0 \\sin(kz - \\omega t) \\hat{\\mathbf{y}}\\n\\mathbf{E} = -\\nabla V_1 - \\frac{\\partial \\mathbf{A}_1}{\\partial t} = -\\omega A_0 \\sin(kz - \\omega t) \\hat{\\mathbf{x}}",
              "explanation": "The ratio $|E|/|B| = \\omega / k = c$, correctly reproducing a propagating plane electromagnetic wave in vacuum."
            }
          ]
        },
        {
          "id": "p4-2",
          "title": "Example 4.2: Radiated Power and Radiation Resistance of a Short AM Radio Antenna",
          "difficulty": "Easy",
          "question": "A vertical short monopole antenna of height $h = 10.0\\text{ m}$ operates at an AM broadcasting frequency of $f = 1000\\text{ kHz}$ ($1.00\\text{ MHz}$). The antenna carries a peak base current of $I_0 = 15.0\\text{ A}$. Calculate: (a) the free-space wavelength $\\lambda$, (b) the effective radiation resistance $R_{\\text{rad}}$ of the antenna (modeled as a short monopole over a conducting ground plane, $R_{\\text{rad}} = 40\\pi^2 (h/\\lambda)^2$), (c) the total time-averaged radiated power $P_{\\text{rad}}$, and (d) the radiation efficiency if the ohmic ground loss resistance is $R_{\\text{loss}} = 2.50\\,\\Omega$.",
          "steps": [
            {
              "stepName": "Step 1: Wavelength Calculation",
              "math": "\\lambda = \\frac{c}{f} = \\frac{3.00 \\times 10^8\\text{ m/s}}{1.00 \\times 10^6\\text{ Hz}} = 300.0\\text{ m}",
              "explanation": "The antenna height $h = 10\\text{ m}$ is $h/\\lambda = 10/300 = 1/30 \\ll 1$, so the short antenna approximation applies."
            },
            {
              "stepName": "Step 2: Radiation Resistance Calculation",
              "math": "R_{\\text{rad}} = 40\\pi^2 \\left( \\frac{h}{\\lambda} \\right)^2 = 40\\pi^2 \\left( \\frac{10}{300} \\right)^2 = 40\\pi^2 \\left( \\frac{1}{900} \\right) = \\frac{40(9.8696)}{900} = 0.4386\\,\\Omega \\approx 0.439\\,\\Omega",
              "explanation": "The radiation resistance is only 0.44 Ohms."
            },
            {
              "stepName": "Step 3: Total Radiated Power",
              "math": "P_{\\text{rad}} = \\frac{1}{2} I_0^2 R_{\\text{rad}} = \\frac{1}{2} (15.0\\text{ A})^2 (0.4386\\,\\Omega) = \\frac{1}{2}(225)(0.4386) = 49.34\\text{ W}",
              "explanation": "The antenna successfully broadcasts 49.3 watts of RF power into the air."
            },
            {
              "stepName": "Step 4: Radiation Efficiency",
              "math": "\\eta = \\frac{R_{\\text{rad}}}{R_{\\text{rad}} + R_{\\text{loss}}} = \\frac{0.4386}{0.4386 + 2.50} = \\frac{0.4386}{2.9386} = 0.1492 \\implies 14.9\\%",
              "explanation": "Over 85% of transmitter power is wasted as heat in ground resistance because the antenna is physically much shorter than $\\lambda/4$ ($75\\text{ m}$)."
            }
          ]
        },
        {
          "id": "p4-3",
          "title": "Example 4.3: Bremsstrahlung Radiated Power from a Decelerating Relativistic Electron",
          "difficulty": "Hard",
          "question": "An electron ($q = -e = -1.602 \\times 10^{-19}\\text{ C}$, $m_e = 9.109 \\times 10^{-31}\\text{ kg}$) in an X-ray medical tube is accelerated by a potential difference $V = 100\\text{ kV}$. Upon hitting a tungsten anode target, it decelerates to a complete stop over a distance $\\Delta x = 2.0\\,\\mu\\text{m}$ under approximately uniform deceleration $a$. (a) Calculate the kinetic energy and deceleration $a$ of the electron. (b) Use Larmor's relativistic formula $P = \\frac{e^2 a^2 \\gamma^6}{6\\pi \\epsilon_0 c^3}$ (or non-relativistic $P = \\frac{e^2 a^2}{6\\pi \\epsilon_0 c^3}$) to calculate the peak radiated power. (c) Estimate the duration of the deceleration pulse $\\Delta t$ and total radiated energy.",
          "steps": [
            {
              "stepName": "Step 1: Electron Velocity and Deceleration",
              "math": "K = e V = (1.602 \\times 10^{-19}\\text{ C})(10^5\\text{ V}) = 1.602 \\times 10^{-14}\\text{ J} = 100\\text{ keV}\\nv_0 = \\sqrt{\\frac{2K}{m_e}} = \\sqrt{\\frac{2(1.602 \\times 10^{-14})}{9.109 \\times 10^{-31}}} = 1.875 \\times 10^8\\text{ m/s} = 0.625 \\, c\\na = \\frac{v_0^2}{2 \\Delta x} = \\frac{(1.875 \\times 10^8\\text{ m/s})^2}{2(2.0 \\times 10^{-6}\\text{ m})} = 8.79 \\times 10^{21}\\text{ m/s}^2",
              "explanation": "The atomic collision produces a staggering deceleration of over $8.8 \\times 10^{21}\\text{ m/s}^2$."
            },
            {
              "stepName": "Step 2: Radiated Power via Larmor Formula",
              "math": "P = \\frac{e^2 a^2}{6\\pi \\epsilon_0 c^3} = \\frac{(1.602 \\times 10^{-19})^2 (8.79 \\times 10^{21})^2}{6\\pi (8.854 \\times 10^{-12}) (3.00 \\times 10^8)^3}\\nP = \\frac{(2.566 \\times 10^{-38})(7.726 \\times 10^{43})}{(1.669 \\times 10^{-10})(2.70 \\times 10^{25})} = \\frac{1.983 \\times 10^6}{4.506 \\times 10^{15}} = 4.40 \\times 10^{-10}\\text{ W}",
              "explanation": "During the deceleration instant, a single microscopic electron emits 0.44 nanowatts of continuous X-ray photon radiation."
            },
            {
              "stepName": "Step 3: Pulse Duration and Bremsstrahlung Emission",
              "math": "\\Delta t = \\frac{v_0}{a} = \\frac{1.875 \\times 10^8\\text{ m/s}}{8.79 \\times 10^{21}\\text{ m/s}^2} = 2.13 \\times 10^{-14}\\text{ s} = 21.3\\text{ fs}\\nE_{\\text{rad}} = P \\times \\Delta t = (4.40 \\times 10^{-10}\\text{ W})(2.13 \\times 10^{-14}\\text{ s}) = 9.37 \\times 10^{-24}\\text{ J} \\approx 58.5\\text{ meV}",
              "explanation": "The sudden deceleration creates an ultrashort femtosecond burst of continuous X-ray radiation (Bremsstrahlung, 'braking radiation')."
            }
          ]
        },
        {
          "id": "p4-4",
          "title": "Example 4.4: Input Current and Total Power Radiated by a Half-Wave Dipole Antenna",
          "difficulty": "Medium",
          "question": "A commercial FM broadcasting station transmits at $f = 100.0\\text{ MHz}$ using a resonant half-wave dipole antenna ($L = \\lambda/2$). The station transmitter delivers a total radiated RF power of $P_{\\text{rad}} = 50.0\\text{ kW}$. (a) Calculate the physical length $L$ of the antenna. (b) Using the half-wave radiation resistance $R_{\\text{rad}} = 73.13\\,\\Omega$, find the peak antenna feedpoint input current $I_0$. (c) Calculate the peak electric field amplitude $E_0$ detected by an FM radio receiver at a distance of $r = 25.0\\text{ km}$ in the broadside direction ($\\theta = 90^\\circ$).",
          "steps": [
            {
              "stepName": "Step 1: Antenna Length Calculation",
              "math": "\\lambda = \\frac{c}{f} = \\frac{3.00 \\times 10^8\\text{ m/s}}{1.00 \\times 10^8\\text{ Hz}} = 3.00\\text{ m}\\nL = \\frac{\\lambda}{2} = \\frac{3.00\\text{ m}}{2} = 1.50\\text{ m}",
              "explanation": "The half-wave dipole is exactly 1.5 meters from tip to tip."
            },
            {
              "stepName": "Step 2: Peak Input Current",
              "math": "P_{\\text{rad}} = \\frac{1}{2} I_0^2 R_{\\text{rad}} \\implies I_0 = \\sqrt{\\frac{2 P_{\\text{rad}}}{R_{\\text{rad}}}}\\nI_0 = \\sqrt{\\frac{2(50,000\\text{ W})}{73.13\\,\\Omega}} = \\sqrt{1367.4} = 36.98\\text{ A}",
              "explanation": "The peak current driving the center feedpoint is approximately 37 Amperes."
            },
            {
              "stepName": "Step 3: Detected Electric Field at 25 km Distance",
              "math": "\\text{Broadside (}\\theta = 90^\\circ\\text{): } \\langle S \\rangle = \\frac{\\eta_0 I_0^2}{8\\pi^2 r^2} \\left[ \\frac{\\cos(0)}{1} \\right]^2 = \\frac{(376.73)(36.98)^2}{8\\pi^2 (2.50 \\times 10^4\\text{ m})^2}\\n\\langle S \\rangle = \\frac{5.152 \\times 10^5}{4.935 \\times 10^{10}} = 1.044 \\times 10^{-5}\\text{ W/m}^2 = 10.44\\,\\mu\\text{W/m}^2\\nE_0 = \\sqrt{2 \\eta_0 \\langle S \\rangle} = \\sqrt{2(376.73)(1.044 \\times 10^{-5})} = \\sqrt{7.866 \\times 10^{-3}} = 0.0887\\text{ V/m} = 88.7\\text{ mV/m}",
              "explanation": "A field strength of 88.7 millivolts per meter provides crystal-clear reception for automobile and mobile FM receivers."
            }
          ]
        }
      ]
    },
    {
      "id": "unit-5",
      "number": 5,
      "title": "Scattering of Electromagnetic Radiation",
      "leadSummary": "Comprehensive mathematical theory of electromagnetic scattering: definitions of differential and total cross-sections, Thomson scattering of unpolarized and polarized radiation by free electrons, classical electron radius, forced damped harmonic oscillator models of bound electrons, complete mathematical derivation of Rayleigh scattering and the omega^4 (lambda^-4) frequency law, optical polarization of skylight, and resonance scattering and atomic fluorescence.",
      "simulations": [
        "scattering-simulator"
      ],
      "sections": [
        {
          "secNumber": "5.1",
          "heading": "Concepts of Differential and Total Scattering Cross-Sections",
          "content": "\n#### Definition of the Scattering Process\nWhen an incident electromagnetic wave impinges upon a localized target (such as an electron, an atom, a molecule, or an aerosol particle), the electric and magnetic fields exert forces on the charges in the target. These accelerated charges oscillate and re-radiate electromagnetic waves in all directions. This redistribution of electromagnetic energy away from the forward propagation direction is called **scattering**.\n\nLet the incident wave carry time-averaged intensity $I_{\\text{inc}} = \\langle S_{\\text{inc}} \\rangle$ (power per unit area). The scattered power $dP_{\\text{scat}}$ emitted into a differential solid angle element $d\\Omega = \\sin\\theta \\, d\\theta \\, d\\phi$ at distance $r$ is detected as scattered intensity $I_{\\text{scat}}(r, \\theta, \\phi)$:\n$$dP_{\\text{scat}} = I_{\\text{scat}}(r, \\theta, \\phi) r^2 d\\Omega$$\n\n#### The Differential Scattering Cross-Section\nThe **differential scattering cross-section** $\\frac{d\\sigma}{d\\Omega}$ is defined as the ratio of the power scattered per unit solid angle to the incident intensity:\n$$\\frac{d\\sigma}{d\\Omega} \\equiv \\frac{1}{I_{\\text{inc}}} \\frac{dP_{\\text{scat}}}{d\\Omega} = \\frac{r^2 I_{\\text{scat}}(r, \\theta, \\phi)}{I_{\\text{inc}}} \\quad [\\text{m}^2 / \\text{sr}]$$\n\nPhysically, $\\frac{d\\sigma}{d\\Omega}$ represents the effective geometric area that the target presents to the incident beam for scattering radiation into direction $(\\theta, \\phi)$.\n\n#### The Total Scattering Cross-Section\nIntegrating the differential cross-section over all $4\\pi$ steradians yields the **total scattering cross-section** $\\sigma_{\\text{total}}$:\n$$\\sigma_{\\text{total}} \\equiv \\oint_{4\\pi} \\left( \\frac{d\\sigma}{d\\Omega} \\right) d\\Omega = \\int_0^{2\\pi} d\\phi \\int_0^\\pi \\left( \\frac{d\\sigma}{d\\Omega} \\right) \\sin\\theta \\, d\\theta \\quad [\\text{m}^2]$$\n\nThe total power extracted from the incident beam by scattering is simply:\n$$P_{\\text{total}} = \\sigma_{\\text{total}} I_{\\text{inc}}$$\n"
        },
        {
          "secNumber": "5.2",
          "heading": "Thomson Scattering of Electromagnetic Waves by Free Electrons",
          "content": "\n#### Interaction with a Free Unbound Electron\nConsider an unbound, free electron (mass $m_e$, charge $-e$) in a vacuum, illuminated by a linearly polarized monochromatic plane wave:\n$$\\mathbf{E}(\\mathbf{r}, t) = E_0 \\cos(\\mathbf{k} \\cdot \\mathbf{r} - \\omega t) \\hat{\\mathbf{z}}$$\n\nIn the non-relativistic regime ($v \\ll c$), the magnetic Lorentz force $\\mathbf{F}_B = -e(\\mathbf{v} \\times \\mathbf{B})$ is negligible compared to the electric force $\\mathbf{F}_E = -e\\mathbf{E}$ by a factor of $v/c$. Newton's second law for the electron motion is:\n$$m_e \\mathbf{a}(t) = -e \\mathbf{E}(t) \\implies \\mathbf{a}(t) = -\\frac{e E_0}{m_e} \\cos(\\omega t) \\hat{\\mathbf{z}}$$\n\n#### Re-Radiated Radiation Fields\nThe accelerating electron emits dipole radiation with an induced acceleration amplitude $a_0 = \\frac{e E_0}{m_e}$. From Larmor's radiation formula, the electric field in the far radiation zone at distance $r$ is:\n$$\\mathbf{E}_{\\text{scat}}(r, \\theta, t) = \\frac{e a(t - r/c)}{4\\pi \\epsilon_0 c^2 r} \\sin\\theta \\hat{\\boldsymbol{\\theta}} = -\\frac{e^2 E_0}{4\\pi \\epsilon_0 m_e c^2} \\left( \\frac{\\sin\\theta}{r} \\right) \\cos(\\omega(t - r/c)) \\hat{\\boldsymbol{\\theta}}$$\nwhere $\\theta$ is the angle between the acceleration axis $\\hat{\\mathbf{z}}$ and the observation direction $\\hat{\\mathbf{r}}$.\n\n#### The Classical Electron Radius ($r_0$)\nWe define the fundamental physical constant known as the **classical electron radius**:\n$$r_0 \\equiv \\frac{e^2}{4\\pi \\epsilon_0 m_e c^2} \\approx 2.81794 \\times 10^{-15} \\text{ m}$$\n\nThe scattered electric field amplitude simplifies to:\n$$E_{\\text{scat}} = -r_0 E_0 \\frac{\\sin\\theta}{r}$$\n\nThe scattered intensity is:\n$$I_{\\text{scat}} = \\frac{1}{2} c \\epsilon_0 E_{\\text{scat}}^2 = \\frac{1}{2} c \\epsilon_0 E_0^2 \\frac{r_0^2 \\sin^2\\theta}{r^2} = I_{\\text{inc}} \\frac{r_0^2 \\sin^2\\theta}{r^2}$$\n\n#### Differential and Total Thomson Cross-Sections\n1. **For Linearly Polarized Incident Light:**\n$$\\left( \\frac{d\\sigma}{d\\Omega} \\right)_{\\text{pol}} = r_0^2 \\sin^2\\theta$$\n\n2. **For Unpolarized Incident Light:**\nAveraging over all polarization angles yields the angular dependence in terms of the scattering angle $\\Theta$ between incident ray $\\mathbf{k}_i$ and scattered ray $\\mathbf{k}_s$:\n$$\\left( \\frac{d\\sigma}{d\\Omega} \\right)_{\\text{unpol}} = r_0^2 \\frac{1 + \\cos^2\\Theta}{2}$$\n\n3. **The Total Thomson Scattering Cross-Section ($\\sigma_T$):**\nIntegrating over the solid angle:\n$$\\sigma_T = \\int_0^{2\\pi} d\\phi \\int_0^\\pi r_0^2 \\left( \\frac{1 + \\cos^2\\Theta}{2} \\right) \\sin\\Theta \\, d\\Theta = \\pi r_0^2 \\int_{-1}^1 (1 + u^2) du = \\pi r_0^2 \\left[ 2 + \\frac{2}{3} \\right] = \\frac{8\\pi}{3} r_0^2$$\n\nSubstituting numerical values:\n$$\\sigma_T = \\frac{8\\pi}{3} (2.81794 \\times 10^{-15} \\text{ m})^2 = 6.65246 \\times 10^{-29} \\text{ m}^2 = 0.6652 \\, \\text{barn}$$\n\n#### Profound Physical Properties of Thomson Scattering\n1. **Frequency Independence:** The Thomson cross-section $\\sigma_T$ is **completely independent of the frequency $\\omega$ of the incident wave**. X-rays, microwaves, and radio waves are scattered by a free electron with the exact same cross-section!\n2. **Forward-Backward Symmetry:** The angular factor $\\frac{1 + \\cos^2\\Theta}{2}$ is symmetric between forward scattering ($\\Theta = 0^\\circ$) and back-scattering ($\\Theta = 180^\\circ$).\n"
        },
        {
          "secNumber": "5.3",
          "heading": "Scattering by Bound Electrons & Forced Damped Oscillations",
          "content": "\n#### The Harmonically Bound Electron Model\nIn real gases, liquids, and solids, electrons are not free; they are bound to atomic nuclei by electrostatic restoring forces. We model a bound atomic electron as a classical damped harmonic oscillator with natural resonance frequency $\\omega_0$ and radiative damping constant $\\gamma$.\n\nUnder the driving force of an incident monochromatic plane wave $\\mathbf{E}(t) = E_0 e^{-i\\omega t} \\hat{\\mathbf{z}}$, the equation of motion is:\n$$m_e \\left( \\frac{d^2 x}{dt^2} + \\gamma \\frac{dx}{dt} + \\omega_0^2 x \\right) = -e E_0 e^{-i\\omega t}$$\n\nAssuming the steady-state sinusoidal response $x(t) = x_0 e^{-i\\omega t}$:\n$$m_e \\left( -\\omega^2 - i\\gamma \\omega + \\omega_0^2 \\right) x_0 = -e E_0$$\n$$x_0 = -\\frac{e E_0 / m_e}{\\omega_0^2 - \\omega^2 - i\\gamma \\omega}$$\n\nThe induced oscillating electric dipole moment is:\n$$p(t) = -e x(t) = \\frac{e^2 E_0 / m_e}{\\omega_0^2 - \\omega^2 - i\\gamma \\omega} e^{-i\\omega t} \\equiv p_0 e^{-i\\omega t}$$\n\n#### Radiation and Total Cross-Section Formula\nSubstituting the dipole moment amplitude $p_0$ into the Larmor power formula $P_{\\text{scat}} = \\frac{p_0^2 \\omega^4}{12\\pi \\epsilon_0 c^3}$:\n$$P_{\\text{scat}} = \\frac{\\omega^4}{12\\pi \\epsilon_0 c^3} \\frac{e^4 E_0^2 / m_e^2}{(\\omega_0^2 - \\omega^2)^2 + \\gamma^2 \\omega^2}$$\n\nDividing by the incident intensity $I_{\\text{inc}} = \\frac{1}{2} c \\epsilon_0 E_0^2$:\n$$\\sigma(\\omega) = \\frac{P_{\\text{scat}}}{I_{\\text{inc}}} = \\left( \\frac{8\\pi}{3} r_0^2 \\right) \\frac{\\omega^4}{(\\omega_0^2 - \\omega^2)^2 + \\gamma^2 \\omega^2}$$\n\nIn terms of the Thomson cross-section $\\sigma_T$:\n$$\\sigma(\\omega) = \\sigma_T \\frac{\\omega^4}{(\\omega_0^2 - \\omega^2)^2 + \\gamma^2 \\omega^2}$$\n\nThis master equation governs the entire spectrum of electromagnetic scattering across physics.\n"
        },
        {
          "secNumber": "5.4",
          "heading": "Rayleigh Scattering: The ω⁴ Law and the Color of the Daytime Sky",
          "content": "\n#### Derivation of the Low-Frequency Limit ($\\omega \\ll \\omega_0$)\nFor atmospheric air molecules ($N_2, O_2$), electronic absorption transitions lie deep in the far-ultraviolet (resonance wavelengths $\\lambda_0 \\approx 100 - 150\\text{ nm}$, so $\\omega_0 \\approx 1.5 \\times 10^{16}\\text{ rad/s}$). Visible light spans $\\lambda \\approx 400 - 700\\text{ nm}$ (frequencies $\\omega \\approx 3 - 5 \\times 10^{15}\\text{ rad/s}$).\n\nTherefore, for visible sunlight traversing the atmosphere:\n$$\\omega \\ll \\omega_0$$\n\nIn this low-frequency limit, the denominator $(\\omega_0^2 - \\omega^2)^2 + \\gamma^2 \\omega^2 \\approx \\omega_0^4$. The scattering cross-section reduces to **Lord Rayleigh's celebrated scattering law** (1871):\n$$\\sigma_{\\text{Rayleigh}}(\\omega) = \\sigma_T \\left( \\frac{\\omega}{\\omega_0} \\right)^4$$\n\nSince $\\omega = \\frac{2\\pi c}{\\lambda}$, the scattering cross-section is inversely proportional to the **fourth power of wavelength**:\n$$\\sigma_{\\text{Rayleigh}}(\\lambda) \\propto \\frac{1}{\\lambda^4}$$\n\n#### Why the Daytime Sky is Blue\nCompare blue sunlight ($\\lambda_{\\text{blue}} \\approx 430\\text{ nm}$) to red sunlight ($\\lambda_{\\text{red}} \\approx 680\\text{ nm}$):\n$$\\frac{\\sigma(\\lambda_{\\text{blue}})}{\\sigma(\\lambda_{\\text{red}})} = \\left( \\frac{680\\text{ nm}}{430\\text{ nm}} \\right)^4 \\approx (1.581)^4 \\approx 6.25$$\nBlue photons are scattered by atmospheric nitrogen and oxygen molecules over **6 times more intensely** than red photons. When you look anywhere in the sky away from the direct disc of the Sun, you are viewing this scattered light, which is heavily dominated by short blue and violet wavelengths.\n\n#### Why Sunsets are Deep Red\nAt sunset and sunrise, sunlight travels through a very long oblique path through Earth's atmosphere (air mass factor up to 40 times greater than at noon). By the **Beer-Lambert transmission law**:\n$$I(x) = I_0 e^{-N \\sigma_{\\text{scat}} x}$$\nThe short blue and green wavelengths are almost entirely scattered out of the direct beam line of sight. Only the least-scattered long wavelengths—orange and deep red—penetrate the thick atmospheric column to reach the observer's eyes.\n",
          "simulation": "scattering-simulator"
        },
        {
          "secNumber": "5.5",
          "heading": "Polarization of Scattered Sunlight and Neutral Points",
          "content": "\n#### Polarization Mechanism of Skylight\nUnpolarized incident sunlight traveling along $+z$ possesses electric field vibrations in all directions within the $xy$-plane.\n\nConsider an observer viewing scattered light from an air molecule at an angle of $90^\\circ$ relative to the incident solar beam (e.g., looking toward the horizon while the Sun is overhead):\n1. Oscillations of the molecule's electrons parallel to the line of sight cannot radiate toward the observer (because oscillating dipoles emit zero power along their axis of oscillation).\n2. Only oscillations perpendicular to both the solar beam and the line of sight produce radiation reaching the observer.\n\nConsequently, sunlight scattered at an angle of **$90^\\circ$ from the Sun is nearly 100% linearly polarized**. Bees and migratory birds utilize this celestial polarization pattern (the e-vector sky compass) for biological navigation even on overcast days.\n",
          "simulation": "polarization-sky-sim"
        },
        {
          "secNumber": "5.6",
          "heading": "Resonance Scattering and Atomic Fluorescence",
          "content": "\n#### Near-Resonance Behavior ($\\omega \\approx \\omega_0$)\nWhen the frequency of incident radiation closely approaches an atomic resonance ($\\omega \\to \\omega_0$):\n$$\\omega_0^2 - \\omega^2 = (\\omega_0 + \\omega)(\\omega_0 - \\omega) \\approx 2\\omega_0 (\\omega_0 - \\omega)$$\n\nThe cross-section becomes:\n$$\\sigma_{\\text{res}}(\\omega) = \\frac{8\\pi}{3} r_0^2 \\frac{\\omega_0^4}{4\\omega_0^2(\\omega - \\omega_0)^2 + \\gamma^2 \\omega_0^2} = \\frac{2\\pi r_0^2 \\omega_0^2}{3} \\frac{1}{(\\omega - \\omega_0)^2 + (\\gamma/2)^2}$$\n\nAt exact resonance ($\\omega = \\omega_0$), the cross-section reaches a peak value:\n$$\\sigma_{\\text{max}} = \\frac{8\\pi r_0^2 \\omega_0^2}{3 \\gamma^2}$$\n\nUsing the classical radiative damping constant $\\gamma = \\frac{2 r_0 \\omega_0^2}{3 c}$:\n$$\\sigma_{\\text{max}} = \\frac{3}{2\\pi} \\left( \\frac{2\\pi c}{\\omega_0} \\right)^2 = \\frac{3}{2\\pi} \\lambda_0^2$$\n\n**Profound Physical Result:** At atomic resonance, the effective scattering cross-section is proportional to the **square of the wavelength $\\lambda_0^2$**, rather than the physical geometric size of the atom ($r_{\\text{atom}}^2 \\sim 10^{-20}\\text{ m}^2$). For yellow sodium D-light ($\\lambda_0 = 589\\text{ nm}$), $\\sigma_{\\text{max}} \\approx 1.6 \\times 10^{-13}\\text{ m}^2$, which is over **seven orders of magnitude larger** than the geometric cross-section of a sodium atom! This phenomenon is known as **resonance fluorescence**.\n"
        }
      ],
      "problems": [
        {
          "id": "p5-1",
          "title": "Example 5.1: Thomson Scattering Cross-Section of Solar X-Rays in Coronal Plasma",
          "difficulty": "Easy",
          "question": "A burst of solar flare X-rays ($E = 10\\text{ keV}$, $\\lambda = 0.124\\text{ nm}$) passes through a solar coronal plasma loop containing free electrons with density $n_e = 10^{15}\\text{ m}^{-3}$ and column depth $L = 5 \\times 10^7\\text{ m}$. (a) Calculate the classical electron radius $r_0$. (b) Calculate the total Thomson cross-section $\\sigma_T$. (c) Determine the optical depth $\\tau = n_e \\sigma_T L$ and the fraction of X-ray beam power scattered by the plasma.",
          "steps": [
            {
              "stepName": "Step 1: Classical Electron Radius",
              "math": "r_0 = \\frac{e^2}{4\\pi \\epsilon_0 m_e c^2} = \\frac{(1.602 \\times 10^{-19})^2}{4\\pi (8.854 \\times 10^{-12})(9.109 \\times 10^{-31})(3.00 \\times 10^8)^2} = 2.818 \\times 10^{-15}\\text{ m}",
              "explanation": "This fundamental scale represents the radius at which the electrostatic self-energy of a sphere equals the electron's rest mass energy $m_e c^2$."
            },
            {
              "stepName": "Step 2: Total Thomson Cross-Section",
              "math": "\\sigma_T = \\frac{8\\pi}{3} r_0^2 = \\frac{8\\pi}{3} (2.818 \\times 10^{-15}\\text{ m})^2 = 6.652 \\times 10^{-29}\\text{ m}^2",
              "explanation": "Every free electron presents a microscopic scattering cross-section of $0.665\\text{ barn}$ to the beam."
            },
            {
              "stepName": "Step 3: Optical Depth and Fraction Scattered",
              "math": "\\tau = n_e \\sigma_T L = (10^{15}\\text{ m}^{-3})(6.652 \\times 10^{-29}\\text{ m}^2)(5 \\times 10^7\\text{ m}) = 3.326 \\times 10^{-6}\\n\\text{Fraction Scattered } = 1 - e^{-\\tau} \\approx \\tau = 3.33 \\times 10^{-6} \\implies 0.00033\\%",
              "explanation": "Because the coronal plasma is optically thin ($\\tau \\ll 1$), virtually all X-rays pass through unhindered, allowing solar satellite telescopes to image the flare directly."
            }
          ]
        },
        {
          "id": "p5-2",
          "title": "Example 5.2: Ratio of Rayleigh Scattering Cross-Sections for Violet vs Red Sunlight",
          "difficulty": "Easy",
          "question": "Calculate the exact ratio of the Rayleigh scattering cross-sections for extreme violet sunlight ($\\lambda_1 = 390\\text{ nm}$) compared to extreme red sunlight ($\\lambda_2 = 720\\text{ nm}$) by molecular nitrogen and oxygen in Earth's atmosphere.",
          "steps": [
            {
              "stepName": "Step 1: Rayleigh Wavelength Scaling Law",
              "math": "\\sigma_{\\text{Rayleigh}}(\\lambda) \\propto \\frac{1}{\\lambda^4} \\implies \\frac{\\sigma(\\lambda_1)}{\\sigma(\\lambda_2)} = \\left( \\frac{\\lambda_2}{\\lambda_1} \\right)^4",
              "explanation": "Because visible light frequencies are well below the UV resonance frequencies of nitrogen molecules, the $\\lambda^{-4}$ law holds strictly."
            },
            {
              "stepName": "Step 2: Numerical Ratio Evaluation",
              "math": "\\frac{\\sigma(390\\text{ nm})}{\\sigma(720\\text{ nm})} = \\left( \\frac{720\\text{ nm}}{390\\text{ nm}} \\right)^4 = (1.84615)^4 = 11.616 \\approx 11.6",
              "explanation": "Violet photons are scattered nearly 12 times more intensely than red photons, causing the predominant blue-violet illumination of clear skies."
            }
          ]
        },
        {
          "id": "p5-3",
          "title": "Example 5.3: Degree of Polarization of Skylight Scattered at 90° from the Sun",
          "difficulty": "Medium",
          "question": "Unpolarized sunlight of intensity $I_0$ strikes an air molecule. (a) For single Rayleigh scattering observed at angle $\\Theta$ from the incident beam, write down the intensities of the two orthogonal polarization components $I_\\perp$ and $I_\\parallel$. (b) Define the degree of linear polarization $P(\\Theta)$ and evaluate it at $\\Theta = 90^\\circ$. (c) Explain why real atmospheric skylight at $90^\\circ$ exhibits a degree of polarization of approximately 75% to 85% rather than a theoretical 100%.",
          "steps": [
            {
              "stepName": "Step 1: Polarized Component Intensities",
              "math": "I_\\perp(\\Theta) = \\frac{1}{2} I_0 \\left( \\frac{d\\sigma_0}{d\\Omega} \\right), \\quad I_\\parallel(\\Theta) = \\frac{1}{2} I_0 \\left( \\frac{d\\sigma_0}{d\\Omega} \\right) \\cos^2\\Theta",
              "explanation": "The perpendicular component has full dipole projection and is independent of $\\Theta$, whereas the parallel component varies as $\\cos^2\\Theta$."
            },
            {
              "stepName": "Step 2: Degree of Linear Polarization",
              "math": "P(\\Theta) \\equiv \\frac{I_\\perp - I_\\parallel}{I_\\perp + I_\\parallel} = \\frac{1 - \\cos^2\\Theta}{1 + \\cos^2\\Theta} = \\frac{\\sin^2\\Theta}{1 + \\cos^2\\Theta}\\n\\text{At } \\Theta = 90^\\circ: P(90^\\circ) = \\frac{\\sin^2(90^\\circ)}{1 + \\cos^2(90^\\circ)} = \\frac{1}{1 + 0} = 1.00 \\implies 100\\%",
              "explanation": "Single scattering from an ideal isotropic spherical molecule produces complete 100% linear polarization at $90^\\circ$."
            },
            {
              "stepName": "Step 3: Real Atmospheric Depolarization Factors",
              "math": "P_{\\text{real}} \\approx 75\\% - 85\\%",
              "explanation": "The observed polarization is reduced due to: (1) molecular anisotropy of non-spherical $N_2$ and $O_2$ diatomic molecules (depolarization factor $\\rho_n \\approx 0.03$), (2) multiple scattering events in thick air columns, and (3) background scattering from unpolarized aerosol dust and water haze."
            }
          ]
        },
        {
          "id": "p5-4",
          "title": "Example 5.4: Resonance Scattering Cross-Section at the Sodium D-Line (589 nm)",
          "difficulty": "Hard",
          "question": "A tunable dye laser is tuned precisely to the sodium atom D2 resonance line ($\\lambda_0 = 589.0\\text{ nm}$, transition frequency $\\omega_0 = 3.20 \\times 10^{15}\\text{ rad/s}$). (a) Calculate the theoretical maximum resonance scattering cross-section $\\sigma_{\\text{max}} = \\frac{3}{2\\pi} \\lambda_0^2$. (b) Compare this cross-section with the geometric area of the sodium atom ($r_{\\text{atom}} \\approx 0.18\\text{ nm}$). (c) If a sodium vapor cell has density $n = 10^{16}\\text{ atoms/m}^3$, calculate the photon penetration depth (attenuation length $l = 1/(n\\sigma)$).",
          "steps": [
            {
              "stepName": "Step 1: Maximum Resonance Cross-Section",
              "math": "\\sigma_{\\text{max}} = \\frac{3}{2\\pi} \\lambda_0^2 = \\frac{3}{2\\pi} (5.890 \\times 10^{-7}\\text{ m})^2 = \\frac{3}{6.283} (3.469 \\times 10^{-13}\\text{ m}^2) = 1.656 \\times 10^{-13}\\text{ m}^2",
              "explanation": "The resonance cross-section is $1.66 \\times 10^{-13}\\text{ m}^2$ (over $1.6 \\times 10^{15}\\text{ barns}$)."
            },
            {
              "stepName": "Step 2: Comparison with Geometric Atomic Size",
              "math": "A_{\\text{atom}} = \\pi r_{\\text{atom}}^2 = \\pi (0.18 \\times 10^{-9}\\text{ m})^2 = 1.018 \\times 10^{-19}\\text{ m}^2\\n\\frac{\\sigma_{\\text{max}}}{A_{\\text{atom}}} = \\frac{1.656 \\times 10^{-13}\\text{ m}^2}{1.018 \\times 10^{-19}\\text{ m}^2} = 1.63 \\times 10^6",
              "explanation": "The effective resonant scattering cross-section is over 1.6 million times larger than the physical size of the sodium atom."
            },
            {
              "stepName": "Step 3: Attenuation Depth in Sodium Vapor",
              "math": "l = \\frac{1}{n \\sigma_{\\text{max}}} = \\frac{1}{(10^{16}\\text{ m}^{-3})(1.656 \\times 10^{-13}\\text{ m}^2)} = \\frac{1}{1656\\text{ m}^{-1}} = 6.04 \\times 10^{-4}\\text{ m} = 0.604\\text{ mm}",
              "explanation": "Resonant light cannot penetrate more than 0.6 millimeters into the vapor before being completely scattered and re-emitted in all directions."
            }
          ]
        }
      ]
    },
    {
      "id": "unit-6",
      "number": 6,
      "title": "Dispersion, Drude-Lorentz Theory & Optical Properties of Matter",
      "leadSummary": "Exhaustive theoretical investigation into electromagnetic dispersion in macroscopic media: normal versus anomalous dispersion, the Drude-Lorentz classical harmonic oscillator model of atomic dielectrics, complex dielectric permittivity tensor, real index of refraction and extinction coefficient, resonance absorption bands, Sellmeier dispersion equations, the Drude free-electron gas theory of metals, DC and optical AC conductivity, optical reflectivity and UV plasma transparency, and microscopic local field corrections via the Clausius-Mossotti and Lorentz-Lorenz relations.",
      "simulations": [
        "drude-lorentz"
      ],
      "sections": [
        {
          "secNumber": "6.1",
          "heading": "Normal and Anomalous Optical Dispersion in Transparent Media",
          "content": "\n#### Definition of Optical Dispersion\nIn a physical material medium, the phase velocity $v$ of an electromagnetic wave depends on the temporal frequency $\\omega$ (or free-space wavelength $\\lambda_0$) of the wave:\n$$v(\\omega) = \\frac{c}{n(\\omega)}$$\nwhere $n(\\omega)$ is the frequency-dependent **refractive index**. The variation of the refractive index with wavelength or frequency, $\\frac{dn}{d\\lambda}$ or $\\frac{dn}{d\\omega}$, is known as **optical dispersion**.\n\nBecause different spectral colors travel at different velocities, white light passing through a glass prism separates into its constituent spectral hues.\n\n#### 1. Normal Dispersion ($\\frac{dn}{d\\lambda} < 0$)\nIn regions of the electromagnetic spectrum far away from any atomic or molecular resonant absorption bands, the refractive index decreases monotonically with increasing wavelength:\n$$\\frac{dn}{d\\lambda} < 0 \\quad \\iff \\quad \\frac{dn}{d\\omega} > 0$$\nShort wavelengths (blue light) experience a larger refractive index and bend more sharply than long wavelengths (red light):\n$$n_{\\text{blue}} > n_{\\text{yellow}} > n_{\\text{red}}$$\n\nIn normal dispersion regimes, the empirical behavior is accurately modeled by **Cauchy's Equation** (Augustin-Louis Cauchy 1836):\n$$n(\\lambda) = A + \\frac{B}{\\lambda^2} + \\frac{C}{\\lambda^4} + \\dots$$\nwhere $A, B, C$ are empirical positive constants characteristic of the optical glass.\n\n#### 2. Anomalous Dispersion ($\\frac{dn}{d\\lambda} > 0$)\nIn the immediate vicinity of an absorption band (where the incident photon frequency matches an atomic or molecular transition frequency), the situation reverses abruptly:\n$$\\frac{dn}{d\\lambda} > 0 \\quad \\iff \\quad \\frac{dn}{d\\omega} < 0$$\nHere, longer wavelengths experience a greater index of refraction than shorter wavelengths. Within this anomalous dispersion zone, the material exhibits intense resonant absorption of electromagnetic energy.\n"
        },
        {
          "secNumber": "6.2",
          "heading": "The Drude-Lorentz Classical Harmonic Oscillator Model of Dielectrics",
          "content": "\n#### Microscopic Mechanical Equation of Motion\nHendrik Lorentz and Paul Drude formulated a microscopic classical model of dielectrics by picturing an atom as a nucleus surrounded by bound electrons. An electron of mass $m_e$ and charge $-e$ is subject to:\n1. **Electrostatic Restoring Force:** $\\mathbf{F}_{\\text{restoring}} = -m_e \\omega_0^2 \\mathbf{r}$, where $\\omega_0$ is the natural resonant frequency of atomic binding.\n2. **Dissipative Frictional Damping Force:** $\\mathbf{F}_{\\text{damping}} = -m_e \\gamma \\frac{d\\mathbf{r}}{dt}$, where $\\gamma$ accounts for radiative damping and atomic collisions.\n3. **Driving Electric Force:** $\\mathbf{F}_{\\text{drive}} = -e \\mathbf{E}(t) = -e \\mathbf{E}_0 e^{-i\\omega t}$.\n\nNewton's second law for the electron displacement is:\n$$m_e \\left( \\frac{d^2 \\mathbf{r}}{dt^2} + \\gamma \\frac{d\\mathbf{r}}{dt} + \\omega_0^2 \\mathbf{r} \\right) = -e \\mathbf{E}_0 e^{-i\\omega t}$$\n\nLooking for steady-state sinusoidal solutions $\\mathbf{r}(t) = \\mathbf{r}_0 e^{-i\\omega t}$:\n$$m_e (-\\omega^2 - i\\gamma \\omega + \\omega_0^2) \\mathbf{r}_0 = -e \\mathbf{E}_0$$\n$$\\mathbf{r}_0 = -\\frac{e / m_e}{\\omega_0^2 - \\omega^2 - i\\gamma \\omega} \\mathbf{E}_0$$\n\n#### Induced Macroscopic Polarization ($\\mathbf{P}$)\nLet the medium contain $N$ atoms per unit volume, with $Z$ electrons per atom distributed among different natural resonant frequencies $\\omega_j$ with oscillator strengths $f_j$ (satisfying the Thomas-Reiche-Kuhn sum rule $\\sum_j f_j = Z$). The macroscopic electric dipole polarization density is:\n$$\\mathbf{P} = -N e \\sum_j f_j \\mathbf{r}_j = \\frac{N e^2}{m_e} \\left[ \\sum_j \\frac{f_j}{\\omega_j^2 - \\omega^2 - i\\gamma_j \\omega} \\right] \\mathbf{E}$$\n\n#### The Complex Dielectric Function\nFrom the macroscopic relation $\\mathbf{D} = \\epsilon_0 \\mathbf{E} + \\mathbf{P} \\equiv \\epsilon(\\omega) \\mathbf{E} = \\epsilon_r(\\omega) \\epsilon_0 \\mathbf{E}$:\n$$\\tilde{\\epsilon}_r(\\omega) = 1 + \\frac{\\mathbf{P}}{\\epsilon_0 \\mathbf{E}} = 1 + \\frac{N e^2}{\\epsilon_0 m_e} \\sum_j \\frac{f_j}{\\omega_j^2 - \\omega^2 - i\\gamma_j \\omega}$$\nThis fundamental relation is the **Drude-Lorentz Complex Dielectric Function**.\n"
        },
        {
          "secNumber": "6.3",
          "heading": "Complex Index of Refraction and Extinction Coefficient",
          "content": "\n#### Real and Imaginary Optical Constants\nThe complex index of refraction $\\tilde{n}$ is defined as the square root of the complex relative permittivity (for non-magnetic media $\\mu_r \\approx 1$):\n$$\\tilde{n}(\\omega) \\equiv n(\\omega) + i\\kappa(\\omega) = \\sqrt{\\tilde{\\epsilon}_r(\\omega)}$$\nwhere:\n- $n(\\omega)$ is the **real refractive index** (governing phase velocity $v = c/n$ and refraction angles via Snell's law).\n- $\\kappa(\\omega)$ is the **extinction coefficient** (governing optical absorption and wave attenuation).\n\nSquaring both sides:\n$$\\tilde{n}^2 = (n + i\\kappa)^2 = n^2 - \\kappa^2 + 2i n\\kappa = \\text{Re}(\\tilde{\\epsilon}_r) + i\\text{Im}(\\tilde{\\epsilon}_r)$$\n\nEquating real and imaginary parts:\n$$n^2 - \\kappa^2 = \\text{Re}(\\tilde{\\epsilon}_r)$$\n$$2n\\kappa = \\text{Im}(\\tilde{\\epsilon}_r)$$\n\nFor a single dominant resonant transition of frequency $\\omega_0$ and oscillator strength $f$:\n$$\\text{Re}(\\tilde{\\epsilon}_r) = 1 + \\frac{N e^2 f}{\\epsilon_0 m_e} \\frac{\\omega_0^2 - \\omega^2}{(\\omega_0^2 - \\omega^2)^2 + \\gamma^2 \\omega^2}$$\n$$\\text{Im}(\\tilde{\\epsilon}_r) = \\frac{N e^2 f}{\\epsilon_0 m_e} \\frac{\\gamma \\omega}{(\\omega_0^2 - \\omega^2)^2 + \\gamma^2 \\omega^2}$$\n\n#### Physical Consequences Across the Spectrum\n1. **Well Below Resonance ($\\omega \\ll \\omega_0$):**\n   $\\text{Im}(\\tilde{\\epsilon}_r) \\approx 0$, meaning $\\kappa \\approx 0$ (transparent medium). $\\text{Re}(\\tilde{\\epsilon}_r) > 1$, and $n$ increases with $\\omega$ (normal dispersion).\n2. **Near Resonance ($\\omega \\approx \\omega_0$):**\n   $\\text{Im}(\\tilde{\\epsilon}_r)$ reaches a sharp Lorentzian peak, causing strong **resonant absorption**. Simultaneously, $\\text{Re}(\\tilde{\\epsilon}_r)$ drops steeply, producing a negative slope $\\frac{dn}{d\\omega} < 0$ (**anomalous dispersion**).\n3. **Well Above Resonance ($\\omega \\gg \\omega_0$):**\n   The medium becomes transparent again, with $n < 1$, approaching $n \\to 1$ asymptotically at X-ray frequencies.\n",
          "simulation": "drude-lorentz"
        },
        {
          "secNumber": "6.4",
          "heading": "Resonance Absorption Bands and the Sellmeier Dispersion Equation",
          "content": "\n#### Derivation of the Sellmeier Formula\nIn optical materials such as crown glass, fused silica, and quartz, the damping constants $\\gamma_j$ are typically much smaller than the resonant frequencies $\\omega_j$. In transparent optical windows far from absorption lines ($\\gamma_j \\ll |\\omega_j - \\omega|$):\n$$\\tilde{\\epsilon}_r(\\omega) \\approx 1 + \\sum_j \\frac{B_j \\omega_j^2}{\\omega_j^2 - \\omega^2}$$\nwhere $B_j = \\frac{N e^2 f_j}{\\epsilon_0 m_e \\omega_j^2}$.\n\nConverting from angular frequencies $\\omega$ to free-space wavelengths $\\lambda$ using $\\omega = 2\\pi c/\\lambda$ yields the **Sellmeier Dispersion Formula** (Wolfgang von Sellmeier 1871):\n$$n^2(\\lambda) = 1 + \\sum_{j=1}^m \\frac{B_j \\lambda^2}{\\lambda^2 - C_j}$$\nwhere $C_j = \\lambda_j^2$ represents the square of the absorption resonance wavelengths, and $B_j$ are dimensionless empirical coefficients.\n\nFor fused silica ($\text{SiO}_2$), a standard three-term Sellmeier equation accurately predicts refractive index across the entire range from ultraviolet ($0.21\\,\\mu\\text{m}$) to mid-infrared ($3.71\\,\\mu\\text{m}$) with precision exceeding $10^{-5}$, enabling the design of precision camera lenses and fiber optic telecommunication systems.\n",
          "simulation": "sellmeier-prism-sim"
        },
        {
          "secNumber": "6.5",
          "heading": "The Drude Free-Electron Gas Theory of Metals",
          "content": "\n#### Metals as an Unbound Electron Plasma\nIn electrical conductors and metals (such as silver, gold, and copper), valence electrons are not bound to individual atomic cores ($\\omega_0 = 0$). They move freely through a background of positive lattice ions, experiencing collisions with an average relaxation time $\\tau$ (damping rate $\\gamma = 1/\\tau$).\n\nSetting $\\omega_0 = 0$ and $\\gamma = 1/\\tau$ in the equation of motion:\n$$m_e \\left( \\frac{d^2 \\mathbf{r}}{dt^2} + \\frac{1}{\\tau} \\frac{d\\mathbf{r}}{dt} \\right) = -e \\mathbf{E}$$\n$$\\mathbf{v}(t) = \\frac{d\\mathbf{r}}{dt} = -\\frac{e \\mathbf{E}_0 / m_e}{1/\\tau - i\\omega} e^{-i\\omega t} = -\\frac{e \\tau / m_e}{1 - i\\omega \\tau} \\mathbf{E}$$\n\n#### Complex AC Conductivity ($\\tilde{\\sigma}(\\omega)$)\nThe macroscopic conduction current density is $\\mathbf{J} = -n_e e \\mathbf{v} = \\tilde{\\sigma}(\\omega) \\mathbf{E}$, where:\n$$\\tilde{\\sigma}(\\omega) = \\frac{\\sigma_0}{1 - i\\omega \\tau}$$\nand $\\sigma_0 = \\frac{n_e e^2 \\tau}{m_e}$ is the standard **DC electrical conductivity**.\n\n#### Drude Dielectric Permittivity of Metals\nSubstituting into Maxwell's equations:\n$$\\tilde{\\epsilon}_r(\\omega) = 1 + i \\frac{\\tilde{\\sigma}}{\\omega \\epsilon_0} = 1 - \\frac{\\sigma_0 / (\\epsilon_0 \\tau)}{\\omega^2 + i\\omega / \\tau} = 1 - \\frac{\\omega_p^2}{\\omega(\\omega + i/\\tau)}$$\nwhere $\\omega_p = \\sqrt{\\frac{n_e e^2}{\\epsilon_0 m_e}}$ is the **bulk plasma frequency of the metal**.\n\n#### High-Frequency Regime ($\\omega \\tau \\gg 1$)\nAt optical frequencies (visible and UV), $\\omega \\tau \\gg 1$, and collision damping can be neglected ($1/\\tau \\to 0$):\n$$\\epsilon_r(\\omega) \\approx 1 - \\frac{\\omega_p^2}{\\omega^2}$$\n\n1. **Below the Plasma Frequency ($\\omega < \\omega_p$):**\n   $\\epsilon_r(\\omega) < 0$. The refractive index is purely imaginary: $\\tilde{n} = i\\kappa$. The wave cannot propagate and reflects totally ($R = 1.00$). This explains the brilliant silvery luster and mirror-like reflectance of metals.\n2. **Above the Plasma Frequency ($\\omega > \\omega_p$):**\n   $\\epsilon_r(\\omega) > 0$. The metal becomes transparent to electromagnetic radiation! For alkali metals, $\\omega_p$ lies in the near-ultraviolet, producing the famous **ultraviolet transparency of metals** discovered experimentally by Wood in 1933.\n"
        },
        {
          "secNumber": "6.6",
          "heading": "Local Field Corrections in Condensed Media (Clausius-Mossotti & Lorentz-Lorenz)",
          "content": "\n#### The Microscopic Local Field ($\\mathbf{E}_{\\text{local}}$)\nIn a dilute gas, molecules are separated by large distances, so the local electric field polarizing a molecule is simply the macroscopic applied field $\\mathbf{E}$. However, in dense liquids and condensed solids, each molecule is polarized not only by external sources, but also by the intense dipolar electric fields of all neighboring polarized molecules.\n\nBy constructing a virtual spherical cavity (Lorentz sphere) around a given molecule, Hendrik Lorentz proved that the local field is:\n$$\\mathbf{E}_{\\text{local}} = \\mathbf{E} + \\frac{\\mathbf{P}}{3\\epsilon_0}$$\nwhere $\\frac{\\mathbf{P}}{3\\epsilon_0}$ is the depolarization field contribution from the inner surface of the Lorentz cavity.\n\n#### The Clausius-Mossotti Relation\nThe induced dipole moment of a single molecule is $\\mathbf{p} = \\alpha \\mathbf{E}_{\\text{local}}$, where $\\alpha$ is the microscopic molecular polarizability. The macroscopic polarization is:\n$$\\mathbf{P} = N \\mathbf{p} = N \\alpha \\left( \\mathbf{E} + \\frac{\\mathbf{P}}{3\\epsilon_0} \\right)$$\n\nUsing $\\mathbf{P} = \\epsilon_0 (\\epsilon_r - 1) \\mathbf{E}$:\n$$\\epsilon_0 (\\epsilon_r - 1) \\mathbf{E} = N \\alpha \\mathbf{E} \\left[ 1 + \\frac{\\epsilon_r - 1}{3} \\right] = N \\alpha \\mathbf{E} \\left[ \\frac{\\epsilon_r + 2}{3} \\right]$$\n\nRearranging yields the celebrated **Clausius-Mossotti Relation**:\n$$\\frac{\\epsilon_r - 1}{\\epsilon_r + 2} = \\frac{N \\alpha}{3\\epsilon_0}$$\n\n#### The Lorentz-Lorenz Formula for Optical Frequencies\nAt optical frequencies, Maxwell's relation gives $\\epsilon_r = n^2$. Substituting into Clausius-Mossotti yields the **Lorentz-Lorenz Equation**:\n$$\\frac{n^2 - 1}{n^2 + 2} = \\frac{N \\alpha}{3\\epsilon_0}$$\n\nThis equation links a macroscopic optical observable—the index of refraction $n$—directly to microscopic quantum atomic parameters: number density $N$ and molecular polarizability $\\alpha$.\n"
        }
      ],
      "problems": [
        {
          "id": "p6-1",
          "title": "Example 6.1: Determination of Cauchy Dispersion Parameters for Optical Crown Glass",
          "difficulty": "Easy",
          "question": "The measured refractive indices of a sample of optical crown glass are $n_F = 1.5286$ at the hydrogen blue Fraunhofer line ($\\lambda_F = 486.1\\text{ nm}$) and $n_C = 1.5172$ at the hydrogen red line ($\\lambda_C = 656.3\\text{ nm}$). (a) Using Cauchy's two-term dispersion formula $n(\\lambda) = A + \\frac{B}{\\lambda^2}$, calculate constants $A$ and $B$. (b) Predict the refractive index $n_D$ at the yellow sodium line ($\\lambda_D = 589.3\\text{ nm}$). (c) Calculate the Abbe dispersion number $V_D = \\frac{n_D - 1}{n_F - n_C}$.",
          "steps": [
            {
              "stepName": "Step 1: Setting Up the Algebraic System",
              "math": "1.5286 = A + \\frac{B}{(0.4861\\,\\mu\\text{m})^2} = A + \\frac{B}{0.23629} = A + 4.2321 B\\n1.5172 = A + \\frac{B}{(0.6563\\,\\mu\\text{m})^2} = A + \\frac{B}{0.43073} = A + 2.3216 B",
              "explanation": "Subtracting the two equations eliminates constant $A$."
            },
            {
              "stepName": "Step 2: Solving for Cauchy Constants A and B",
              "math": "1.5286 - 1.5172 = (4.2321 - 2.3216) B \\implies 0.0114 = 1.9105 B\\nB = \\frac{0.0114}{1.9105} = 0.005967\\,\\mu\\text{m}^2 = 5.967 \\times 10^{-15}\\text{ m}^2\\nA = 1.5172 - 2.3216(0.005967) = 1.5172 - 0.01385 = 1.50335",
              "explanation": "Cauchy's dispersion model for this glass is $n(\\lambda) = 1.50335 + \\frac{0.005967}{\\lambda^2}$ (with $\\lambda$ in $\\mu\\text{m}$)."
            },
            {
              "stepName": "Step 3: Predicting n_D and the Abbe Number V_D",
              "math": "n_D = 1.50335 + \\frac{0.005967}{(0.5893)^2} = 1.50335 + \\frac{0.005967}{0.34727} = 1.50335 + 0.01718 = 1.52053\\nV_D = \\frac{n_D - 1}{n_F - n_C} = \\frac{1.52053 - 1}{1.5286 - 1.5172} = \\frac{0.52053}{0.0114} = 45.66",
              "explanation": "An Abbe number of 45.7 classifies this material as low-dispersion crown optical glass."
            }
          ]
        },
        {
          "id": "p6-2",
          "title": "Example 6.2: Sellmeier Equation Calculation of Group Velocity Dispersion in Fused Silica",
          "difficulty": "Hard",
          "question": "For telecommunication optical fibers made of pure fused silica, the zero-dispersion wavelength $\\lambda_{\\text{ZDW}}$ is near $1.27\\,\\mu\\text{m}$. At the standard optical communications wavelength $\\lambda = 1.550\\,\\mu\\text{m}$, the Sellmeier formula gives $n = 1.44402$ and $\\frac{dn}{d\\lambda} = -0.0125\\,\\mu\\text{m}^{-1}$. (a) Calculate the phase velocity $v_p$ of the laser signal. (b) Derive the formula for group velocity $v_g = \\frac{c}{n - \\lambda \\frac{dn}{d\\lambda}}$ and calculate $v_g$ at $1.55\\,\\mu\\text{m}$. (c) Calculate the signal transit delay time for a 100-km transoceanic fiber cable.",
          "steps": [
            {
              "stepName": "Step 1: Phase Velocity Calculation",
              "math": "v_p = \\frac{c}{n} = \\frac{2.9979 \\times 10^8\\text{ m/s}}{1.44402} = 2.07608 \\times 10^8\\text{ m/s}",
              "explanation": "Phase fronts advance through the fiber core at roughly 208,000 kilometers per second."
            },
            {
              "stepName": "Step 2: Group Velocity and Group Index n_g",
              "math": "n_g \\equiv n - \\lambda \\frac{dn}{d\\lambda} = 1.44402 - (1.550\\,\\mu\\text{m})(-0.0125\\,\\mu\\text{m}^{-1}) = 1.44402 + 0.01938 = 1.46340\\nv_g = \\frac{c}{n_g} = \\frac{2.9979 \\times 10^8\\text{ m/s}}{1.46340} = 2.04859 \\times 10^8\\text{ m/s}",
              "explanation": "Actual data pulses (wave packets) travel at group velocity $v_g$, which is slightly slower than the phase velocity."
            },
            {
              "stepName": "Step 3: Signal Transit Time over 100 km",
              "math": "\\Delta t = \\frac{L}{v_g} = \\frac{1.00 \\times 10^5\\text{ m}}{2.04859 \\times 10^8\\text{ m/s}} = 4.881 \\times 10^{-4}\\text{ s} = 488.1\\,\\mu\\text{s}",
              "explanation": "Data packets take 0.488 milliseconds to traverse every 100 km of fiber optic glass."
            }
          ]
        },
        {
          "id": "p6-4",
          "title": "Example 6.3: Plasma Frequency, AC Conductivity, and Optical Reflectance of Silver",
          "difficulty": "Medium",
          "question": "Pure metallic silver has conduction electron density $n_e = 5.86 \\times 10^{28}\\text{ m}^{-3}$ and electron collision relaxation time $\\tau = 3.8 \\times 10^{-14}\\text{ s}$. (a) Calculate the bulk electron plasma frequency $\\omega_p$ and corresponding wavelength $\\lambda_p = 2\\pi c / \\omega_p$. (b) Determine whether green light ($\\lambda = 532\\text{ nm}$) reflects or transmits. (c) Calculate the theoretical reflectance $R$ for green light.",
          "steps": [
            {
              "stepName": "Step 1: Plasma Frequency Calculation",
              "math": "\\omega_p = \\sqrt{\\frac{n_e e^2}{\\epsilon_0 m_e}} = \\sqrt{\\frac{(5.86 \\times 10^{28})(1.602 \\times 10^{-19})^2}{(8.854 \\times 10^{-12})(9.109 \\times 10^{-31})}} = \\sqrt{1.867 \\times 10^{32}} = 1.366 \\times 10^{16}\\text{ rad/s}\\n\\lambda_p = \\frac{2\\pi c}{\\omega_p} = \\frac{2\\pi (3.00 \\times 10^8)}{1.366 \\times 10^{16}} = 1.38 \\times 10^{-7}\\text{ m} = 138\\text{ nm}",
              "explanation": "The plasma wavelength lies deep in the ultraviolet at 138 nm."
            },
            {
              "stepName": "Step 2: Optical Response for Green Light (532 nm)",
              "math": "\\lambda = 532\\text{ nm} > \\lambda_p = 138\\text{ nm} \\iff \\omega < \\omega_p",
              "explanation": "Since green light is well below the plasma frequency, conduction electrons screen the field, causing total reflection."
            },
            {
              "stepName": "Step 3: Reflectance Calculation",
              "math": "\\omega = \\frac{2\\pi c}{\\lambda} = \\frac{2\\pi(3.00 \\times 10^8)}{5.32 \\times 10^{-7}} = 3.543 \\times 10^{15}\\text{ rad/s}\\n\\epsilon_r = 1 - \\frac{\\omega_p^2}{\\omega^2} = 1 - \\left(\\frac{1.366 \\times 10^{16}}{3.543 \\times 10^{15}}\\right)^2 = 1 - (3.855)^2 = 1 - 14.86 = -13.86\\n\\tilde{n} = \\sqrt{-13.86} = i \\sqrt{13.86} = i 3.723 \\implies n = 0, \\kappa = 3.723\\nR = \\frac{(0 - 1)^2 + (3.723)^2}{(0 + 1)^2 + (3.723)^2} = \\frac{1 + 13.86}{1 + 13.86} = 1.00 \\implies 100\\%",
              "explanation": "Accounting for slight collision damping in real silver gives an exceptional optical reflectance of over 99.2%, making silver the premier material for telescope mirrors."
            }
          ]
        },
        {
          "id": "p6-5",
          "title": "Example 6.4: Clausius-Mossotti Local Field and Molar Polarizability of Nonpolar Liquids",
          "difficulty": "Hard",
          "question": "Liquid carbon tetrachloride ($\text{CCl}_4$) has molecular mass $M = 153.82\\text{ g/mol}$, density $\\rho = 1.594\\text{ g/cm}^3$, and relative dielectric constant $\\epsilon_r = 2.238$ at static frequencies. (a) Calculate the number density $N$ of molecules. (b) Use the Clausius-Mossotti relation $\\frac{\\epsilon_r - 1}{\\epsilon_r + 2} = \\frac{N \\alpha}{3\\epsilon_0}$ to find the electronic polarizability $\\alpha$ per molecule. (c) Compare the microscopic local polarizing field $E_{\\text{local}}$ to the macroscopic field $E$.",
          "steps": [
            {
              "stepName": "Step 1: Molecular Number Density Calculation",
              "math": "N = \\frac{\\rho N_A}{M} = \\frac{(1594\\text{ kg/m}^3)(6.022 \\times 10^{23}\\text{ mol}^{-1})}{0.15382\\text{ kg/mol}} = 6.240 \\times 10^{27}\\text{ molecules/m}^3",
              "explanation": "Each cubic meter contains over $6.2 \\times 10^{27}$ molecules."
            },
            {
              "stepName": "Step 2: Electronic Polarizability via Clausius-Mossotti",
              "math": "\\frac{\\epsilon_r - 1}{\\epsilon_r + 2} = \\frac{2.238 - 1}{2.238 + 2} = \\frac{1.238}{4.238} = 0.2921\\n\\alpha = \\frac{3\\epsilon_0}{N} \\left( \\frac{\\epsilon_r - 1}{\\epsilon_r + 2} \\right) = \\frac{3(8.854 \\times 10^{-12})}{6.240 \\times 10^{27}} (0.2921) = (4.257 \\times 10^{-39})(0.2921) = 1.243 \\times 10^{-39}\\text{ C}\\cdot\\text{m}^2/\\text{V}",
              "explanation": "In terms of polarizability volume $\\alpha' = \\frac{\\alpha}{4\\pi\\epsilon_0} = 1.12 \\times 10^{-29}\\text{ m}^3 = 11.2\\text{ Å}^3$, closely matching the physical volume of a $\\text{CCl}_4$ molecule."
            },
            {
              "stepName": "Step 3: Microscopic Local Field Enhancement",
              "math": "E_{\\text{local}} = E \\left( \\frac{\\epsilon_r + 2}{3} \\right) = E \\left( \\frac{2.238 + 2}{3} \\right) = E \\left( \\frac{4.238}{3} \\right) = 1.413 \\, E",
              "explanation": "Due to dipole-dipole neighbor interactions, the microscopic field acting on each molecule is 41.3% stronger than the macroscopic electric field."
            }
          ]
        }
      ]
    }
  ]
};
