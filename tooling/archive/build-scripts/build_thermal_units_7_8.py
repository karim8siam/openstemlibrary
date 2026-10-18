import json

# Unit 7: Radiation
u7 = {
    "unitNumber": 7,
    "title": "Thermal Radiation & Quantum Hypotheses",
    "description": "Kirchhoff's radiation law, blackbody cavity energy density, radiation pressure, Stefan-Boltzmann law, Wien's displacement law, Rayleigh-Jeans formula, Planck's quantum radiation law, and solar astrophysics.",
    "sections": [
        {
            "id": "u7-sec1",
            "title": "Spectral Emissive Powers, Absorptivity & Kirchhoff’s Law",
            "content": """
### 1. Thermal Radiation Fundamentals

All matter at non-zero absolute temperature continuously emits electromagnetic radiation due to thermal fluctuations and accelerating electrical charges within constituent atoms and molecules:
- **Spectral Emissive Power** $e_\\lambda$: Radiant energy emitted per unit surface area, per unit time, per unit wavelength interval in all outward directions (in $\\text{W/(m}^2\\cdot\\text{m)}$ or $\\text{W/m}^3$).
- **Total Emissive Power** $E$: Integrated radiant flux across all wavelengths:
$$E = \\int_0^\\infty e_\\lambda d\\lambda$$
- **Spectral Absorptive Power (Absorptivity)** $a_\\lambda$: The dimensionless fraction of incident radiation of wavelength $\\lambda$ absorbed by the surface ($0 \\le a_\\lambda \\le 1$). An idealized **blackbody** absorbs 100% of incident radiation across all wavelengths ($a_\\lambda \\equiv 1$).

### 2. Kirchhoff's Law of Thermal Radiation

Gustav Kirchhoff (1859) proved through second-law detailed balance that for any body in thermal equilibrium inside an isothermal enclosure at temperature $T$:
$$\\frac{e_\\lambda}{a_\\lambda} = E_\\lambda^{\\text{blackbody}}(T)$$
The ratio of spectral emissive power to absorptive power is an identical universal function of wavelength and temperature for all materials.
**Physical Consequences**:
1. A good absorber is inevitably a good emitter ($a_\\lambda = 1 \\implies e_\\lambda = E_\\lambda^{\\text{blackbody}}$). A poor absorber (or shiny mirror, $a_\\lambda \\ll 1$) is a poor emitter.
2. A body cannot emit more radiation at any wavelength than an ideal blackbody at the identical temperature.
3. Cavity Radiator: An isothermal hollow sphere with a small pinhole aperture acts as an experimental realization of a blackbody ($a_\\lambda \\approx 0.999$), as incoming rays undergo multiple diffuse reflections with internal absorption on every bounce.
            """
        },
        {
            "id": "u7-sec2",
            "title": "Energy Density, Radiation Pressure & Stefan-Boltzmann Law",
            "content": """
### 1. Radiation Pressure in an Isotropic Photon Gas

Electromagnetic radiation carries momentum density $\\vec{g} = \\vec{S}/c^2 = \\frac{u}{c} \\hat{k}$, where $u$ is the volumetric radiation energy density (in $\\text{J/m}^3$). When isotropic radiation impinges on a surface, time-averaged momentum transfer over all angles of incidence yields:
$$P = \\frac{1}{3} u$$
This isotropic **radiation pressure** is fundamental to the hydrostatic equilibrium of stars and stellar interiors.

### 2. Thermodynamic Derivation of the Stefan-Boltzmann Law

Treating the radiation field within an evacuated cavity of volume $V$ as a thermodynamic system:
- Internal energy: $U = u(T) V$.
- First Law with radiation pressure: $dU = T dS - P dV = T dS - \\frac{1}{3} u dV$.
- Differential entropy:
$$dS = \\frac{dU + P dV}{T} = \\frac{V \\frac{du}{dT} dT + u dV + \\frac{1}{3} u dV}{T} = \\frac{V}{T} \\frac{du}{dT} dT + \\frac{4 u}{3 T} dV$$
Since $dS$ is an exact differential, equating cross partial derivatives:
$$\\frac{\\partial}{\\partial V}\\left(\\frac{V}{T} \\frac{du}{dT}\\right) = \\frac{\\partial}{\\partial T}\\left(\\frac{4 u}{3 T}\\right)$$
$$\\frac{1}{T} \\frac{du}{dT} = \\frac{4}{3} \\left( \\frac{1}{T} \\frac{du}{dT} - \\frac{u}{T^2} \\right) = \\frac{4}{3 T} \\frac{du}{dT} - \\frac{4 u}{3 T^2}$$
$$\\frac{1}{3 T} \\frac{du}{dT} = \\frac{4 u}{3 T^2} \\implies \\frac{du}{u} = 4 \\frac{dT}{T}$$
Integrating both sides:
$$\\ln u = 4 \\ln T + \\text{const} \\implies u(T) = a T^4$$
where $a$ is the radiation density constant.
The total emissive power exiting a blackbody surface into a hemisphere is $E = \\frac{1}{4} c u$:
$$E = \\sigma T^4$$
where $\\sigma = \\frac{a c}{4} = \\frac{2\\pi^5 k_B^4}{15 c^2 h^3} \\approx 5.6704 \\times 10^{-8} \\text{ W/(m}^2\\cdot\\text{K}^4)$. This is the **Stefan-Boltzmann Law**.
            """
        },
        {
            "id": "u7-sec3",
            "title": "Wien’s Displacement Law & The Ultraviolet Catastrophe",
            "content": """
### 1. Wien's Displacement Law

Wilhelm Wien (1893) analyzed the adiabatic expansion of an evacuated spherical cavity with perfectly reflecting walls containing blackbody radiation. As the cavity expands, Doppler shifts upon reflection from receding walls stretch each wavelength proportionally to the cavity radius: $\\lambda \\propto R$. Since isentropic expansion preserves $V T^3 = \\text{const} \\implies R T = \\text{const}$, the product $\\lambda T$ remains invariant.
Consequently, the spectral energy distribution must take the general form:
$$u_\\lambda d\\lambda = \\frac{1}{\\lambda^5} \\phi(\\lambda T) d\\lambda$$
Differentiating with respect to $\\lambda$ and setting the derivative to zero locates the peak emission wavelength $\\lambda_{\\max}$:
$$\\lambda_{\\max} T = b$$
where $b \\approx 2.8978 \\times 10^{-3} \\text{ m}\\cdot\\text{K}$ is **Wien's Displacement Constant**. As temperature increases, the peak of blackbody emission shifts toward shorter wavelengths (from infrared to visible red, yellow, and blue-white).

### 2. Rayleigh-Jeans Law & The Ultraviolet Catastrophe

Lord Rayleigh and Sir James Jeans (1900–1905) applied classical electrodynamics and the Maxwell-Boltzmann equipartition theorem to standing electromagnetic waves in a cubical cavity of side $L$.
- Number of electromagnetic cavity standing wave modes between $\\nu$ and $\\nu + d\\nu$ (with 2 polarization states):
$$g(\\nu) d\\nu = \\frac{8\\pi V}{c^3} \\nu^2 d\\nu \\implies g(\\lambda) d\\lambda = \\frac{8\\pi V}{\\lambda^4} d\\lambda$$
- By classical equipartition, each harmonic standing wave mode possesses average thermal energy $\\langle E \\rangle = k_B T$.
- The spectral energy density becomes the **Rayleigh-Jeans Formula**:
$$u_\\lambda d\\lambda = \\frac{8\\pi k_B T}{\\lambda^4} d\\lambda$$
While accurate at very long wavelengths (infrared and radio), as $\\lambda \\to 0$ (ultraviolet, X-ray), the predicted energy density diverges:
$$\\lim_{\\lambda \\to 0} u_\\lambda = \\infty \\implies \\int_0^\\infty u_\\lambda d\\lambda = \\infty$$
This profound classical failure was termed the **Ultraviolet Catastrophe** by Paul Ehrenfest.
            """
        },
        {
            "id": "u7-sec4",
            "title": "Planck’s Quantum Radiation Law & High/Low Asymptotes",
            "content": """
### 1. Max Planck's Quantum Hypothesis

On October 19, 1900, Max Planck resolved the ultraviolet catastrophe by postulating that the material oscillators within the cavity walls emit and absorb electromagnetic radiation only in discrete, indivisible packets (quanta) of energy:
$$E_n = n h \\nu = n \\frac{h c}{\\lambda}, \\quad n = 0, 1, 2, \\dots$$
where $h \\approx 6.6261 \\times 10^{-34}\\text{ J}\\cdot\\text{s}$ is **Planck's constant**.

### 2. Derivation of Average Oscillator Energy

By the Boltzmann distribution, the probability of an oscillator occupying energy level $E_n$ is $P_n \\propto e^{-E_n / k_B T} = e^{-n \\beta h \\nu}$ (where $\\beta = 1/k_B T$):
$$\\langle E \\rangle = \\frac{\\sum_{n=0}^\\infty n h \\nu e^{-n \\beta h \\nu}}{\\sum_{n=0}^\\infty e^{-n \\beta h \\nu}} = -\\frac{d}{d\\beta} \\ln\\left( \\sum_{n=0}^\\infty (e^{-\\beta h \\nu})^n \\right) = -\\frac{d}{d\\beta} \\ln\\left(\\frac{1}{1 - e^{-\\beta h \\nu}}\\right)$$
$$\\langle E \\rangle = \\frac{h \\nu e^{-\\beta h \\nu}}{1 - e^{-\\beta h \\nu}} = \\frac{h \\nu}{e^{\\frac{h \\nu}{k_B T}} - 1}$$
Multiplying by the density of modes $g(\\lambda) d\\lambda = \\frac{8\\pi}{\\lambda^4} d\\lambda$:
$$u_\\lambda d\\lambda = \\frac{8\\pi h c}{\\lambda^5 \\left[ e^{\\frac{h c}{\\lambda k_B T}} - 1 \\right]} d\\lambda$$
This is **Planck's Radiation Law**.

### 3. Asymptotic Reductions

1. **Wien Approximation ($\lambda k_B T \\ll h c$, high frequencies)**:
$$e^{\\frac{h c}{\\lambda k_B T}} \\gg 1 \\implies u_\\lambda \\approx \\frac{8\\pi h c}{\\lambda^5} e^{-\\frac{h c}{\\lambda k_B T}}$$
Exponential decay eliminates the ultraviolet catastrophe.
2. **Rayleigh-Jeans Limit ($\lambda k_B T \\gg h c$, low frequencies)**:
Expanding $e^x \\approx 1 + x$:
$$e^{\\frac{h c}{\\lambda k_B T}} - 1 \\approx \\frac{h c}{\\lambda k_B T} \\implies u_\\lambda \\approx \\frac{8\\pi h c}{\\lambda^5 \\left(\\frac{h c}{\\lambda k_B T}\\right)} = \\frac{8\\pi k_B T}{\\lambda^4}$$
recovering the classical Rayleigh-Jeans formula.
            """
        },
        {
            "id": "u7-sec5",
            "title": "Solar Constant & Astrophysics of the Sun",
            "content": """
### 1. The Solar Constant

The **Solar Constant** $S$ is the total radiant energy received from the Sun per unit time, per unit area, on a surface oriented perpendicular to the solar rays at the top of Earth's atmosphere at Earth's mean orbital radius ($1\\text{ AU} \\approx 1.496 \\times 10^{11}\\text{ m}$):
$$S \\approx 1361 \\text{ W/m}^2$$

### 2. Determination of the Surface Temperature of the Sun

Let the Sun have radius $R_\\odot \\approx 6.963 \\times 10^8\\text{ m}$ and effective surface photospheric temperature $T_\\odot$.
By the Stefan-Boltzmann law, the total luminosity $L_\\odot$ emitted by the Sun is:
$$L_\\odot = 4\\pi R_\\odot^2 \\sigma T_\\odot^4$$
By energy conservation, this luminosity spreads spherically across space. At the mean Sun-Earth distance $d_{\\text{SE}}$:
$$S = \\frac{L_\\odot}{4\\pi d_{\\text{SE}}^2} = \\frac{4\\pi R_\\odot^2 \\sigma T_\\odot^4}{4\\pi d_{\\text{SE}}^2} = \\sigma T_\\odot^4 \\left(\\frac{R_\\odot}{d_{\\text{SE}}}\\right)^2$$
Solving for $T_\\odot$:
$$T_\\odot = \\left[ \\frac{S}{\\sigma} \\left(\\frac{d_{\\text{SE}}}{R_\\odot}\\right)^2 \\right]^{1/4}$$
Substituting values:
$$\\frac{d_{\\text{SE}}}{R_\\odot} = \\frac{1.496 \\times 10^{11}}{6.963 \\times 10^8} \\approx 214.85$$
$$\\left(\\frac{d_{\\text{SE}}}{R_\\odot}\\right)^2 = (214.85)^2 \\approx 46162$$
$$T_\\odot = \\left[ \\frac{1361}{5.6704 \\times 10^{-8}} \\times 46162 \\right]^{1/4} = \\left[ (2.4002 \\times 10^{10}) \\times 46162 \\right]^{1/4} = \\left[ 1.108 \\times 10^{15} \\right]^{1/4} \\approx 5778\\text{ K}$$
The effective temperature of the solar photosphere is approximately $5780\\text{ K}$.

### 3. Planetary Equilibrium Temperatures

For a planet with planetary radius $R_p$, orbital radius $d$, and Bond albedo $A$ (reflectivity), intercepted solar flux is $\\pi R_p^2 S(1 - A)$. Emitting as a sphere of area $4\\pi R_p^2$ with emissivity $\\epsilon$:
$$\\pi R_p^2 S (1 - A) = 4\\pi R_p^2 \\epsilon \\sigma T_p^4 \\implies T_p = \\left[ \\frac{S (1 - A)}{4 \\epsilon \\sigma} \\right]^{1/4}$$
For Earth ($A \\approx 0.30, \\epsilon \\approx 1$): $T_p \\approx 255\\text{ K}$ ($-18^\\circ\\text{C}$). Greenhouse atmospheric gases warm the actual mean surface temperature to $+15^\\circ\\text{C}$ ($288\\text{ K}$).
            """
        }
    ],
    "problems": [
        {
            "id": "u7-p1",
            "title": "Solar Surface Temperature & Terrestrial Radiation Budget",
            "statement": "The measured solar constant outside Earth's atmosphere is $S = 1361.0\\\\text{ W/m}^2$. The mean Earth-Sun distance is $d_{\\\\text{SE}} = 1.496\\\\times 10^{11}\\\\text{ m}$, and the solar radius is $R_\\\\odot = 6.963\\\\times 10^8\\\\text{ m}$. (a) Calculate the total electromagnetic luminosity $L_\\\\odot$ of the Sun. (b) Calculate the effective photospheric surface temperature $T_\\\\odot$ of the Sun assuming blackbody emission ($\\\\sigma = 5.6704\\\\times 10^{-8}\\\\text{ W/(m}^2\\\\cdot\\\\text{K}^4)$). (c) Calculate the peak emission wavelength $\\\\lambda_{\\\\max}$ of the solar spectrum using Wien's displacement law ($b = 2.8978\\\\times 10^{-3}\\\\text{ m}\\\\cdot\\\\text{K}$).",
            "steps": [
                {
                    "step": "Step 1: Calculate Total Solar Luminosity $L_\\\\odot$",
                    "detail": "The solar flux spreads over a sphere of radius $d_{\\\\text{SE}}$:\n$$L_\\\\odot = 4\\\\pi d_{\\\\text{SE}}^2 S = 4\\\\pi (1.496 \\\\times 10^{11}\\\\text{ m})^2 (1361.0\\\\text{ W/m}^2)$$\n$$4\\\\pi (2.2380 \\\\times 10^{22}) = 2.8124 \\\\times 10^{23}\\\\text{ m}^2$$\n$$L_\\\\odot = (2.8124 \\\\times 10^{23})(1361.0) = 3.8277 \\\\times 10^{26}\\\\text{ W}$$\nThe Sun radiates nearly $3.83 \\\\times 10^{26}\\\\text{ Joules}$ of energy every second."
                },
                {
                    "step": "Step 2: Calculate Effective Surface Temperature $T_\\\\odot$",
                    "detail": "Total solar surface area: $A_\\\\odot = 4\\\\pi R_\\\\odot^2 = 4\\\\pi (6.963 \\\\times 10^8)^2 = 4\\\\pi (4.8483 \\\\times 10^{17}) = 6.0927 \\\\times 10^{18}\\\\text{ m}^2$.\nBy the Stefan-Boltzmann law $L_\\\\odot = A_\\\\odot \\\\sigma T_\\\\odot^4$:\n$$T_\\\\odot^4 = \\\\frac{L_\\\\odot}{A_\\\\odot \\\\sigma} = \\\\frac{3.8277 \\\\times 10^{26}}{(6.0927 \\\\times 10^{18})(5.6704 \\\\times 10^{-8})} = \\\\frac{3.8277 \\\\times 10^{26}}{3.4548 \\\\times 10^{11}} = 1.1079 \\\\times 10^{15}\\\\text{ K}^4$$\n$$T_\\\\odot = (1.1079 \\\\times 10^{15})^{1/4} = 5777.6\\\\text{ K} \\\\approx 5778\\\\text{ K}$$"
                },
                {
                    "step": "Step 3: Calculate Peak Wavelength $\\\\lambda_{\\\\max}$",
                    "detail": "By Wien's displacement law:\n$$\\\\lambda_{\\\\max} = \\\\frac{b}{T_\\\\odot} = \\\\frac{2.8978 \\\\times 10^{-3}\\\\text{ m}\\\\cdot\\\\text{K}}{5777.6\\\\text{ K}} = 5.0156 \\\\times 10^{-7}\\\\text{ m} = 501.6\\\\text{ nm}$$\nThis peak wavelength corresponds to green visible light ($502\\\\text{ nm}$), explaining why human vision evolved its highest sensitivity in the green region of the spectrum."
                }
            ],
            "answer": "(a) Total solar luminosity $L_\\\\odot = 3.83\\\\times 10^{26}\\\\text{ W}$. (b) Effective solar temperature $T_\\\\odot = 5778\\\\text{ K}$. (c) Peak wavelength $\\\\lambda_{\\\\max} = 501.6\\\\text{ nm}$ (green visible light)."
        },
        {
            "id": "u7-p2",
            "title": "Cryogenic Radiation Shielding Between Concentric Spheres",
            "statement": "A spherical liquid helium storage dewar of radius $r_1 = 0.250\\\\text{ m}$ is maintained at $T_1 = 4.20\\\\text{ K}$ and has an emissivity of $\\\\epsilon_1 = 0.040$. It is enclosed within an outer concentric spherical vacuum jacket of radius $r_2 = 0.350\\\\text{ m}$ at ambient room temperature $T_2 = 300.0\\\\text{ K}$ with emissivity $\\\\epsilon_2 = 0.040$. (a) Calculate the net radiative heat influx without any intermediate radiation shields. (b) If a thin polished copper radiation shield ($\\\\epsilon_s = 0.030$) of radius $r_s = 0.300\\\\text{ m}$ is inserted in the vacuum space between them, calculate the equilibrium temperature $T_s$ of the shield. (c) Calculate the new net heat influx and the percentage reduction in cryogenic boil-off achieved by the shield.",
            "steps": [
                {
                    "step": "Step 1: Radiative Heat Influx Without Radiation Shield",
                    "detail": "For concentric spheres, net radiative heat exchange is:\n$$Q_{12} = \\\\frac{\\\\sigma (A_1)(T_2^4 - T_1^4)}{\\\\frac{1}{\\\\epsilon_1} + \\\\frac{A_1}{A_2} \\\\left(\\\\frac{1}{\\\\epsilon_2} - 1\\\\right)}$$\nInner area $A_1 = 4\\\\pi r_1^2 = 4\\\\pi (0.25)^2 = 0.7854\\\\text{ m}^2$.\nOuter area $A_2 = 4\\\\pi r_2^2 = 4\\\\pi (0.35)^2 = 1.5394\\\\text{ m}^2$.\nArea ratio: $A_1 / A_2 = (0.25 / 0.35)^2 = 0.5102$.\nDenominator: $\\\\frac{1}{0.04} + 0.5102 \\\\left(\\\\frac{1}{0.04} - 1\\\\right) = 25.0 + 0.5102 (24.0) = 25.0 + 12.245 = 37.245$.\nTemperature terms: $T_2^4 = (300)^4 = 8.10 \\\\times 10^9\\\\text{ K}^4$, $T_1^4 = (4.2)^4 \\\\approx 311 \\\\approx 0$.\n$$Q_{12} = \\\\frac{(5.6704 \\\\times 10^{-8})(0.7854)(8.10 \\\\times 10^9)}{37.245} = \\\\frac{360.75}{37.245} = 9.686\\\\text{ W}$$"
                },
                {
                    "step": "Step 2: Determine Equilibrium Shield Temperature $T_s$",
                    "detail": "In steady state, heat flowing from outer jacket (2) to shield (s) equals heat from shield (s) to inner dewar (1): $Q_{2s} = Q_{s1}$.\nShield area $A_s = 4\\\\pi (0.30)^2 = 1.1310\\\\text{ m}^2$.\n$$Q_{2s} = \\\\frac{\\\\sigma A_s (T_2^4 - T_s^4)}{\\\\frac{1}{\\\\epsilon_s} + \\\\frac{A_s}{A_2} \\\\left(\\\\frac{1}{\\\\epsilon_2} - 1\\\\right)}, \\quad Q_{s1} = \\\\frac{\\\\sigma A_1 (T_s^4 - T_1^4)}{\\\\frac{1}{\\\\epsilon_1} + \\\\frac{A_1}{A_s} \\\\left(\\\\frac{1}{\\\\epsilon_s} - 1\\\\right)}$$\nDenominator 1: $\\\\frac{1}{0.03} + \\\\left(\\\\frac{0.30}{0.35}\\\\right)^2 (24) = 33.33 + (0.7347)(24) = 33.33 + 17.63 = 50.96$.\nDenominator 2: $\\\\frac{1}{0.04} + \\\\left(\\\\frac{0.25}{0.30}\\\\right)^2 (32.33) = 25.0 + (0.6944)(32.33) = 25.0 + 22.45 = 47.45$.\nEquating fluxes and solving yields: $T_s^4 \\\\approx 0.528 T_2^4 \\implies T_s \\\\approx (0.528)^{1/4} (300\\\\text{ K}) = (0.852)(300) = 255.6\\\\text{ K}$."
                },
                {
                    "step": "Step 3: New Heat Influx and Boil-off Reduction",
                    "detail": "The new heat reaching the helium bath is:\n$$Q_{\\\\text{shielded}} = \\\\frac{(5.6704 \\\\times 10^{-8})(0.7854)(255.6^4)}{47.45} = \\\\frac{(4.4535 \\\\times 10^{-8})(4.270 \\\\times 10^9)}{47.45} = \\\\frac{190.16}{47.45} = 4.008\\\\text{ W}$$\nPercentage reduction:\n$$\\\\text{Reduction} = \\\\frac{9.686 - 4.008}{9.686} \\\\times 100\\\\% = 58.62\\\\%$$\nA single radiation shield cuts cryogenic heat leak and helium boil-off by nearly $59\\\\%$."
                }
            ],
            "answer": "(a) Unshielded heat influx $Q = 9.69\\\\text{ W}$. (b) Equilibrium shield temperature $T_s = 255.6\\\\text{ K}$ ($-17.5^\\\\circ\\\\text{C}$). (c) Shielded heat influx $Q_{\\\\text{shielded}} = 4.01\\\\text{ W}$, achieving a $58.6\\\\%$ reduction in helium boil-off."
        },
        {
            "id": "u7-p3",
            "title": "Planck Radiation Integrated Power & Wien Limit Verification",
            "statement": "Starting from Planck's spectral energy density $u_\\lambda = \\\\frac{8\\\\pi h c}{\\\\lambda^5 (e^{h c / \\\\lambda k_B T} - 1)}$: (a) derive the Stefan-Boltzmann law by performing the definite integral $u = \\\\int_0^\\\\infty u_\\lambda d\\\\lambda$, using the Riemann zeta identity $\\\\int_0^\\\\infty \\\\frac{x^3}{e^x - 1} dx = \\\\frac{\\\\pi^4}{15}$. (b) Derive Wien's displacement law and find the transcendental equation for $x = \\\\frac{h c}{\\\\lambda_{\\\\max} k_B T}$. (c) Solve the transcendental equation numerically to find Wien's displacement constant $b$.",
            "steps": [
                {
                    "step": "Step 1: Integrate Planck Formula to Derive Stefan-Boltzmann Law",
                    "detail": "Let $x = \\\\frac{h c}{\\\\lambda k_B T} \\implies \\\\lambda = \\\\frac{h c}{k_B T x}$ and $d\\\\lambda = -\\\\frac{h c}{k_B T x^2} dx$.\n$$u = \\\\int_0^\\\\infty \\\\frac{8\\\\pi h c}{\\\\lambda^5 (e^{h c / \\\\lambda k_B T} - 1)} d\\\\lambda = 8\\\\pi h c \\\\int_0^\\\\infty \\\\frac{1}{\\\\left(\\\\frac{h c}{k_B T x}\\\\right)^5 (e^x - 1)} \\\\left( \\\\frac{h c}{k_B T x^2} dx \\\\right)$$\n$$u = 8\\\\pi h c \\\\left(\\\\frac{k_B T}{h c}\\\\right)^4 \\\\int_0^\\\\infty \\\\frac{x^3}{e^x - 1} dx = \\\\frac{8\\\\pi k_B^4 T^4}{h^3 c^3} \\\\left(\\\\frac{\\\\pi^4}{15}\\\\right) = \\\\frac{8\\\\pi^5 k_B^4}{15 c^3 h^3} T^4$$\nSetting $a = \\\\frac{8\\\\pi^5 k_B^4}{15 c^3 h^3}$, the radiant emissive power is $E = \\\\frac{c}{4} u = \\\\sigma T^4$, where:\n$$\\\\sigma = \\\\frac{2\\\\pi^5 k_B^4}{15 c^2 h^3}$$\nThis confirms the Stefan-Boltzmann law directly from quantum first principles."
                },
                {
                    "step": "Step 2: Derive Wien's Transcendental Equation",
                    "detail": "To locate $\\\\lambda_{\\\\max}$, set $\\\\frac{d u_\\\\lambda}{d\\\\lambda} = 0$.\nWrite $u_\\\\lambda = C \\\\lambda^{-5} (e^{h c / \\\\lambda k_B T} - 1)^{-1}$ with $x = \\\\frac{h c}{\\\\lambda k_B T}$:\n$$\\\\frac{d u_\\\\lambda}{d\\\\lambda} = C \\\\left[ -5\\\\lambda^{-6} (e^x - 1)^{-1} - \\\\lambda^{-5} (e^x - 1)^{-2} e^x \\\\left(-\\\\frac{h c}{k_B T \\\\lambda^2}\\\\right) \\\\right] = 0$$\n$$-5 (e^x - 1) + x e^x = 0 \\implies x e^x = 5 (e^x - 1)$$\nDividing by $e^x$:\n$$x = 5 (1 - e^{-x}) \\implies 5 - x = 5 e^{-x}$$\nThis is Wien's classic transcendental equation."
                },
                {
                    "step": "Step 3: Numerical Root Finding for $x$ and Evaluation of $b$",
                    "detail": "Solving $f(x) = x + 5 e^{-x} - 5 = 0$ via Newton-Raphson iteration:\n- $x_0 = 5 \\implies f(5) = 5 + 5 e^{-5} - 5 = 5(0.006738) = 0.03369$.\n- $f'(x) = 1 - 5 e^{-x} \\implies f'(5) = 1 - 0.03369 = 0.9663$.\n- $x_1 = 5 - \\\\frac{0.03369}{0.9663} = 5 - 0.03487 = 4.9651$.\nConverged root: $x = 4.965114$.\nSince $x = \\\\frac{h c}{\\\\lambda_{\\\\max} k_B T} \\implies \\\\lambda_{\\\\max} T = \\\\frac{h c}{x k_B} = b$:\n$$b = \\\\frac{(6.62607 \\\\times 10^{-34}\\\\text{ J}\\\\cdot\\\\text{s})(2.99792 \\\\times 10^8\\\\text{ m/s})}{(4.965114)(1.38065 \\\\times 10^{-23}\\\\text{ J/K})} = \\\\frac{1.986445 \\\\times 10^{-25}}{6.855085 \\\\times 10^{-23}} = 2.89777 \\\\times 10^{-3}\\\\text{ m}\\\\cdot\\\\text{K}$$"
                }
            ],
            "answer": "(a) Exact Stefan-Boltzmann constant derived: $\\\\sigma = \\\\frac{2\\\\pi^5 k_B^4}{15 c^2 h^3}$. (b) Transcendental equation is $x = 5(1 - e^{-x})$ with root $x = 4.9651$. (c) Wien's displacement constant is $b = 2.898\\\\times 10^{-3}\\\\text{ m}\\\\cdot\\\\text{K}$."
        }
    ]
}

# Unit 8: Transport Phenomena in Gases
u8 = {
    "unitNumber": 8,
    "title": "Transport Phenomena in Gases & Real Equations of State",
    "description": "Kinetic theory of mean free path, viscosity, thermal conductivity, diffusion, Brownian motion, Van der Waals real gases, critical constants, Gibbs phase rule, and regenerative Joule-Thomson liquefaction.",
    "sections": [
        {
            "id": "u8-sec1",
            "title": "Kinetic Theory & Mean Free Path",
            "content": """
### 1. The Concept of Mean Free Path

In the kinetic theory of gases, molecules are in constant, randomized rectilinear motion interrupted by elastic collisions. The **Mean Free Path** $\\lambda$ is the average distance traversed by a molecule between two successive collisions.

Consider a gas of spherical molecules with collision diameter $d$ and number density $n = N/V$. If one test molecule moves with speed $\\bar{v}$ while all others are stationary, its effective collision cross-section is $\\sigma = \\pi d^2$. In time $\\Delta t$, it sweeps out a collision cylinder of volume $\\sigma \\bar{v} \\Delta t = \\pi d^2 \\bar{v} \\Delta t$, encountering $n \\pi d^2 \\bar{v} \\Delta t$ target molecules.
The collision frequency is $Z_1 = n \\pi d^2 \\bar{v}$, yielding Clausius's initial estimate:
$$\\lambda_{\\text{Clausius}} = \\frac{\\bar{v} \\Delta t}{Z_1 \\Delta t} = \\frac{1}{n \\pi d^2}$$

### 2. Maxwell's Relative Velocity Correction

James Clerk Maxwell (1860) showed that other molecules are also moving with a Maxwell-Boltzmann velocity distribution. The average relative velocity between two colliding molecules is $\\bar{v}_{\\text{rel}} = \\sqrt{2} \\bar{v}$. Hence the true collision frequency is $Z = \\sqrt{2} n \\pi d^2 \\bar{v}$, yielding:
$$\\lambda = \\frac{1}{\\sqrt{2} n \\pi d^2}$$
Using the ideal gas law $P = n k_B T \\implies n = \\frac{P}{k_B T}$:
$$\\lambda = \\frac{k_B T}{\\sqrt{2} \\pi d^2 P}$$
**Key Dependences**:
- At constant temperature, mean free path is inversely proportional to pressure: $\\lambda \\propto 1/P$.
- At constant volume ($n = \\text{const}$), mean free path is independent of temperature.
- In atmospheric air ($P = 1\\text{ atm}$, $d \\approx 0.37\\text{ nm}$), $\\lambda \\approx 68\\text{ nm}$. In ultra-high vacuum ($P \\sim 10^{-10}\\text{ torr}$), $\\lambda$ exceeds several kilometers.

### 3. Collision Probability
The probability that a molecule travels a distance $x$ without undergoing any collisions is given by the Poisson survival distribution:
$$P(x) = e^{-x / \\lambda}$$
            """
        },
        {
            "id": "u8-sec2",
            "title": "Transport Phenomena: Viscosity, Conduction & Diffusion",
            "content": """
### 1. Viscosity (Transport of Momentum)

Consider a gas with a macroscopic velocity gradient $du/dz$ along the $z$-axis. Molecules crossing a plane $z = z_0$ from layer $z_0 + \\lambda$ carry momentum $m [u(z_0) + \\lambda du/dz]$, while molecules from $z_0 - \\lambda$ carry $m [u(z_0) - \\lambda du/dz]$.
By kinetic theory, the molecular flux crossing in each direction is $\\frac{1}{6} n \\bar{v}$. The net rate of momentum transfer per unit area (shear stress $\\tau$) is:
$$\\tau = \\frac{1}{6} n \\bar{v} \\left[ m \\left(u + \\lambda \\frac{du}{dz}\\right) - m \\left(u - \\lambda \\frac{du}{dz}\\right) \\right] = \\frac{1}{3} n m \\bar{v} \\lambda \\frac{du}{dz} = \\frac{1}{3} \\rho \\bar{v} \\lambda \\frac{du}{dz}$$
Comparing with Newton's law of viscosity $\\tau = \\eta \\frac{du}{dz}$:
$$\\eta = \\frac{1}{3} \\rho \\bar{v} \\lambda$$
Substituting $\\rho = n m$ and $\\lambda = \\frac{1}{\\sqrt{2} n \\pi d^2}$:
$$\\eta = \\frac{m \\bar{v}}{3 \\sqrt{2} \\pi d^2} = \\frac{m \\sqrt{8 k_B T / \\pi m}}{3 \\sqrt{2} \\pi d^2} = \\frac{2}{3 \\pi^{3/2} d^2} \\sqrt{m k_B T}$$
**Remarkable Conclusions**:
1. **Independence of Pressure**: Over a wide pressure range ($10^{-3}\\text{ atm} \\le P \\le 10\\text{ atm}$), the viscosity of an ideal gas is completely independent of pressure/density (experimentally verified by Maxwell in 1866).
2. **Temperature Dependence**: Unlike liquids (whose viscosity decreases with $T$), the viscosity of gases increases with temperature: $\\eta \\propto \\sqrt{T}$.

### 2. Thermal Conductivity (Transport of Energy)

When a temperature gradient $dT/dz$ exists, molecules carry internal kinetic energy across planes. The conductive heat flux is:
$$q = -\\frac{1}{3} \\rho \\bar{v} \\lambda c_v \\frac{dT}{dz} \\implies k = \\frac{1}{3} \\rho \\bar{v} \\lambda c_v = \\eta c_v$$
Like viscosity, gaseous thermal conductivity is independent of pressure over moderate ranges.

### 3. Diffusion (Transport of Mass)

When a concentration gradient $dn/dz$ exists, net particle flux is $J = -D \\frac{dn}{dz}$.
The coefficient of self-diffusion is:
$$D = \\frac{1}{3} \\bar{v} \\lambda = \\frac{\\eta}{\\rho}$$
Because $\\rho \\propto P$ and $\\lambda \\propto 1/P$, diffusion is inversely proportional to pressure: $D \\propto 1/P$.
            """
        },
        {
            "id": "u8-sec3",
            "title": "Brownian Motion & Einstein-Smoluchowski Fluctuation Theory",
            "content": """
### 1. Robert Brown's Discovery & Kinetic Interpretation

In 1827, Scottish botanist Robert Brown observed under a microscope that microscopic pollen grains suspended in water perform perpetual, erratic, jittery zigzag motions. In 1905, Albert Einstein and Marian Smoluchowski proved that Brownian motion is the direct macroscopic consequence of relentless, unbalanced thermal molecular collisions.

### 2. Langevin Equation & Mean Squared Displacement

Paul Langevin (1908) formulated the equation of motion for a Brownian particle of mass $m$ and radius $r$ suspended in a fluid of viscosity $\\eta$:
$$m \\frac{d^2 x}{dt^2} = -6\\pi \\eta r \\frac{dx}{dt} + F_{\\text{random}}(t)$$
where $-6\\pi \\eta r v$ is Stokes drag and $F_{\\text{random}}(t)$ is a zero-mean Gaussian white-noise thermal bombardment force.
Multiplying by $x$ and taking the statistical ensemble average $\\langle \\dots \\rangle$:
$$m \\left\\langle x \\frac{d^2 x}{dt^2} \\right\\rangle = -6\\pi \\eta r \\left\\langle x \\frac{dx}{dt} \\right\\rangle + \\langle x F_{\\text{random}} \\rangle$$
Using $x \\frac{d^2 x}{dt^2} = \\frac{1}{2} \\frac{d^2 (x^2)}{dt^2} - \\left(\\frac{dx}{dt}\\right)^2$ and the equipartition theorem $m \\langle v_x^2 \\rangle = k_B T$, with $\\langle x F_{\\text{random}} \\rangle = 0$:
$$\\frac{m}{2} \\frac{d^2 \\langle x^2 \\rangle}{dt^2} + 3\\pi \\eta r \\frac{d \\langle x^2 \\rangle}{dt} = k_B T$$
For observational timescales ($t \\gg m / 6\\pi\\eta r \\sim 10^{-7}\\text{ s}$), inertial term vanishes:
$$\\frac{d \\langle x^2 \\rangle}{dt} = \\frac{k_B T}{3\\pi \\eta r} = 2 D \\implies \\langle x^2(t) \\rangle = 2 D t = \\frac{k_B T}{3\\pi \\eta r} t$$
For 3D motion: $\\langle r^2(t) \\rangle = 6 D t = \\frac{k_B T}{\\pi \\eta r} t$.

### 3. Perrin's Determination of Avogadro's Number

In 1908, Jean Perrin tracked individual mastic and gamboge colloidal particles under a microscope, plotting $\\langle r^2 \\rangle$ vs $t$ and measuring sedimentation equilibrium. Using $k_B = R / N_A$, Perrin measured $N_A \\approx 6.5 \\times 10^{23}\\text{ mol}^{-1}$, providing undeniable empirical proof for the reality of atoms and winning the 1926 Nobel Prize in Physics.
            """
        },
        {
            "id": "u8-sec4",
            "title": "Van der Waals Real Gas & Critical Phenomena",
            "content": """
### 1. The Van der Waals Equation of State

Johannes Diderik van der Waals (1873) modified the ideal gas law to account for two microscopic realities of real gas molecules:
1. **Finite Molecular Volume (Co-volume $b$)**: Molecules are hard spheres; the free volume available for motion is $(V_m - b)$, where $b = 4 N_A \\left(\\frac{4}{3}\\pi r^3\\right)$ is four times the true molecular volume.
2. **Intermolecular Attractive Forces ($a/V_m^2$)**: Molecules near the container wall experience an inward net pull from interior molecules, reducing impact pressure by an internal cohesion pressure proportional to density squared: $P_{\\text{int}} = a / V_m^2$.

Combining these corrections yields:
$$\\left( P + \\frac{a}{V_m^2} \\right) (V_m - b) = R T$$

### 2. Critical Point Constants

On a $P$-$V$ diagram, isotherms exhibit cubic behavior. At the **Critical Temperature** $T_c$, the liquid-gas coexistence curve terminates at an inflection point with horizontal tangent:
$$\\left(\\frac{\\partial P}{\\partial V_m}\\right)_{T_c} = 0, \\quad \\left(\\frac{\\partial^2 P}{\\partial V_m^2}\\right)_{T_c} = 0$$
Differentiating $P = \\frac{R T}{V_m - b} - \\frac{a}{V_m^2}$:
$$\\left(\\frac{\\partial P}{\\partial V_m}\\right) = -\\frac{R T}{(V_m - b)^2} + \\frac{2a}{V_m^3} = 0 \\implies R T_c = \\frac{2a (V_c - b)^2}{V_c^3}$$
$$\\left(\\frac{\\partial^2 P}{\\partial V_m^2}\\right) = \\frac{2 R T}{(V_m - b)^3} - \\frac{6a}{V_m^4} = 0 \\implies R T_c = \\frac{3a (V_c - b)^3}{V_c^4}$$
Equating both expressions gives:
$$\\frac{2a (V_c - b)^2}{V_c^3} = \\frac{3a (V_c - b)^3}{V_c^4} \\implies 2 V_c = 3 (V_c - b) \\implies V_c = 3 b$$
Substituting $V_c = 3b$ back:
$$T_c = \\frac{8a}{27 R b}, \\quad P_c = \\frac{a}{27 b^2}$$

### 3. Law of Corresponding States
The critical compressibility factor is a universal dimensionless number:
$$Z_c = \\frac{P_c V_c}{R T_c} = \\frac{\\left(\\frac{a}{27 b^2}\\right)(3b)}{R \\left(\\frac{8a}{27 R b}\\right)} = \\frac{3}{8} = 0.375$$
Defining reduced coordinates $P_r = P/P_c$, $V_r = V/V_c$, and $T_r = T/T_c$:
$$\\left( P_r + \\frac{3}{V_r^2} \\right) (3 V_r - 1) = 8 T_r$$
In reduced coordinates, all gases obey the **identical universal equation of state**, independent of parameters $a$ and $b$.
            """
        },
        {
            "id": "u8-sec5",
            "title": "Gibbs Phase Rule & Regenerative Gas Liquefaction",
            "content": """
### 1. Gibbs' Phase Rule

Josiah Willard Gibbs (1876) derived the thermodynamic degree of freedom $F$ for a multi-phase, multi-component heterogeneous system in equilibrium:
$$F = C - P + 2$$
where $C$ is the number of independent chemical components and $P$ is the number of coexisting phases.
For a single-component system ($C = 1$, e.g., pure water):
- Single phase ($P = 1$, liquid or vapor): $F = 1 - 1 + 2 = 2$ (can independently vary both $T$ and $P$).
- Two coexisting phases ($P = 2$, liquid-vapor boiling curve): $F = 1 - 2 + 2 = 1$ (univariant; fixing $T$ automatically fixes equilibrium vapor pressure $P$).
- Three coexisting phases ($P = 3$, Triple Point): $F = 1 - 3 + 2 = 0$ (invariant; triple point occurs at a unique, immutable temperature and pressure: $T_t = 0.01^\\circ\\text{C}$, $P_t = 611.65\\text{ Pa}$ for water).

### 2. Regenerative Gas Liquefaction (Linde and Claude Cycles)

Because the Joule-Thomson temperature drop $\\Delta T = \\mu_{\\text{JT}} \\Delta P$ across a single throttle valve is typically $20\\text{ K}$ to $40\\text{ K}$, liquefaction from room temperature requires **regenerative heat exchange**:
- **Linde Cycle**: High-pressure gas ($200\\text{ atm}$) flows through the inner tube of a counter-current heat exchanger, throttles through a porous nozzle, cools, and the unliquefied cold gas returns via the outer annular tube to pre-cool incoming compressed gas. As the cycle repeats, the pre-throttling temperature drops progressively until it enters the liquid-vapor dome, yielding continuous liquid air, nitrogen, or oxygen.
- **Claude Cycle**: Replaces a portion of the throttling valve with an adiabatic expansion engine doing external mechanical work against a piston, achieving greater cooling ($\Delta T_{\\text{rev, ad}} \\gg \\Delta T_{\\text{JT}}$) and higher liquefaction efficiency.
            """
        }
    ],
    "problems": [
        {
            "id": "u8-p1",
            "title": "Van der Waals Critical Constants & Boyle Temperature of Argon",
            "statement": "For argon gas ($\\\\text{Ar}$), experimental critical constants are measured as $P_c = 4.87\\\\times 10^6\\\\text{ Pa}$ ($48.7\\\\text{ bar}$) and $T_c = 150.8\\\\text{ K}$. (a) Calculate the Van der Waals parameters $a$ and $b$ for argon. (b) Calculate the critical molar volume $V_{c, m}$ and the critical compressibility factor $Z_c$. (c) Determine the Boyle temperature $T_B = \\\\frac{a}{R b}$ at which the second Virial coefficient vanishes.",
            "steps": [
                {
                    "step": "Step 1: Calculate Van der Waals Parameters $a$ and $b$",
                    "detail": "From the critical point formulas:\n$$P_c = \\\\frac{a}{27 b^2}, \\quad T_c = \\\\frac{8a}{27 R b}$$\nDividing $T_c$ by $P_c$:\n$$\\\\frac{T_c}{P_c} = \\\\frac{8a / 27 R b}{a / 27 b^2} = \\\\frac{8 b}{R} \\implies b = \\\\frac{R T_c}{8 P_c}$$\n$$b = \\\\frac{(8.314\\\\text{ J/(mol}\\\\cdot\\\\text{K)})(150.8\\\\text{ K})}{8 (4.87 \\\\times 10^6\\\\text{ Pa})} = \\\\frac{1253.75}{3.896 \\\\times 10^7} = 3.218 \\\\times 10^{-5}\\\\text{ m}^3\\\\text{/mol}$$\nNow solving for $a$ from $P_c = \\\\frac{a}{27 b^2}$:\n$$a = 27 P_c b^2 = 27 (4.87 \\\\times 10^6)(3.218 \\\\times 10^{-5})^2$$\n$$b^2 = 1.0356 \\\\times 10^{-9}\\\\text{ m}^6\\\\text{/mol}^2$$\n$$a = 27 (4.87 \\\\times 10^6)(1.0356 \\\\times 10^{-9}) = 0.1362\\\\text{ J}\\\\cdot\\\\text{m}^3\\\\text{/mol}^2$$"
                },
                {
                    "step": "Step 2: Calculate Critical Molar Volume and $Z_c$",
                    "detail": "The theoretical critical molar volume is:\n$$V_{c, m} = 3 b = 3(3.218 \\\\times 10^{-5}) = 9.654 \\\\times 10^{-5}\\\\text{ m}^3\\\\text{/mol} = 0.0965\\\\text{ L/mol}$$\nCritical compressibility factor:\n$$Z_c = \\\\frac{P_c V_{c, m}}{R T_c} = \\\\frac{(4.87 \\\\times 10^6)(9.654 \\\\times 10^{-5})}{(8.314)(150.8)} = \\\\frac{470.15}{1253.75} = 0.3750$$\nThis exactly verifies the universal Van der Waals ratio $Z_c = 3/8$."
                },
                {
                    "step": "Step 3: Calculate the Boyle Temperature $T_B$",
                    "detail": "The Boyle temperature is the temperature at which the attractive and repulsive corrections cancel, causing real gas behavior to emulate an ideal gas over low pressures:\n$$T_B = \\\\frac{a}{R b} = \\\\frac{0.1362}{(8.314)(3.218 \\\\times 10^{-5})} = \\\\frac{0.1362}{2.6754 \\\\times 10^{-4}} = 509.08\\\\text{ K}$$\nNotice that $T_B = \\\\frac{27}{8} T_c = 3.375 T_c = (3.375)(150.8\\\\text{ K}) = 508.95\\\\text{ K}$."
                }
            ],
            "answer": "(a) Van der Waals parameters: $a = 0.136\\\\text{ J}\\\\cdot\\\\text{m}^3\\\\text{/mol}^2$ and $b = 3.22\\\\times 10^{-5}\\\\text{ m}^3\\\\text{/mol}$. (b) Critical volume $V_c = 9.65\\\\times 10^{-5}\\\\text{ m}^3\\\\text{/mol}$, $Z_c = 0.375$. (c) Boyle temperature $T_B = 509.1\\\\text{ K}$ ($235.9^\\\\circ\\\\text{C}$)."
        },
        {
            "id": "u8-p2",
            "title": "Argon Viscosity & Molecular Collision Diameter Determination",
            "statement": "At temperature $T = 273.15\\\\text{ K}$ and standard atmospheric pressure $P = 1.013\\\\times 10^5\\\\text{ Pa}$, the dynamic viscosity of gaseous argon ($M = 39.95\\\\text{ g/mol}$) is experimentally measured as $\\\\eta = 2.10\\\\times 10^{-5}\\\\text{ Pa}\\\\cdot\\\\text{s}$. (a) Calculate the average molecular speed $\\\\bar{v}$ of argon atoms. (b) Using the kinetic theory viscosity formula $\\\\eta = \\\\frac{m \\\\bar{v}}{3\\\\sqrt{2}\\\\pi d^2}$, calculate the molecular collision diameter $d$ of an argon atom. (c) Calculate the mean free path $\\\\lambda$ and the collision frequency $Z$ under these standard conditions.",
            "steps": [
                {
                    "step": "Step 1: Calculate Average Molecular Speed $\\\\bar{v}$",
                    "detail": "From the Maxwell-Boltzmann distribution:\n$$\\\\bar{v} = \\\\sqrt{\\\\frac{8 k_B T}{\\\\pi m}} = \\\\sqrt{\\\\frac{8 R T}{\\\\pi M}}$$\n$$\\\\bar{v} = \\\\sqrt{\\\\frac{8 (8.314)(273.15)}{\\\\pi (0.03995\\\\text{ kg/mol})}} = \\\\sqrt{\\\\frac{18171.7}{0.12551}} = \\\\sqrt{144785} = 380.51\\\\text{ m/s}$$"
                },
                {
                    "step": "Step 2: Calculate Molecular Collision Diameter $d$",
                    "detail": "Mass of one argon atom: $m = \\\\frac{M}{N_A} = \\\\frac{0.03995}{6.022 \\\\times 10^{23}} = 6.634 \\\\times 10^{-26}\\\\text{ kg}$.\nFrom $\\\\eta = \\\\frac{m \\\\bar{v}}{3 \\\\sqrt{2} \\\\pi d^2}$:\n$$d^2 = \\\\frac{m \\\\bar{v}}{3 \\\\sqrt{2} \\\\pi \\\\eta}$$\n$$m \\\\bar{v} = (6.634 \\\\times 10^{-26})(380.51) = 2.5243 \\\\times 10^{-23}\\\\text{ kg}\\\\cdot\\\\text{m/s}$$\n$$3 \\\\sqrt{2} \\\\pi \\\\eta = 3 (1.4142)(\\\\pi)(2.10 \\\\times 10^{-5}) = (13.3286)(2.10 \\\\times 10^{-5}) = 2.7990 \\\\times 10^{-4}\\\\text{ Pa}\\\\cdot\\\\text{s}$$\n$$d^2 = \\\\frac{2.5243 \\\\times 10^{-23}}{2.7990 \\\\times 10^{-4}} = 9.0186 \\\\times 10^{-20}\\\\text{ m}^2$$\n$$d = \\\\sqrt{9.0186 \\\\times 10^{-20}} = 3.003 \\\\times 10^{-10}\\\\text{ m} = 0.300\\\\text{ nm} = 3.00\\\\text{ \\\\AA}$$"
                },
                {
                    "step": "Step 3: Calculate Mean Free Path $\\\\lambda$ and Collision Frequency $Z$",
                    "detail": "Number density $n = \\\\frac{P}{k_B T} = \\\\frac{1.013 \\\\times 10^5}{(1.38065 \\\\times 10^{-23})(273.15)} = \\\\frac{1.013 \\\\times 10^5}{3.7712 \\\\times 10^{-21}} = 2.686 \\\\times 10^{25}\\\\text{ m}^{-3}$.\n$$\\\\lambda = \\\\frac{1}{\\\\sqrt{2} n \\\\pi d^2} = \\\\frac{1}{\\\\sqrt{2} (2.686 \\\\times 10^{25}) \\\\pi (9.0186 \\\\times 10^{-20})} = \\\\frac{1}{1.0766 \\\\times 10^7} = 9.288 \\\\times 10^{-8}\\\\text{ m} = 92.9\\\\text{ nm}$$\nCollision frequency:\n$$Z = \\\\frac{\\\\bar{v}}{\\\\lambda} = \\\\frac{380.51\\\\text{ m/s}}{9.288 \\\\times 10^{-8}\\\\text{ m}} = 4.097 \\\\times 10^9\\\\text{ collisions/second}$$\nEach argon atom undergoes over 4 billion collisions every second."
                }
            ],
            "answer": "(a) Mean speed $\\\\bar{v} = 380.5\\\\text{ m/s}$. (b) Molecular diameter $d = 0.300\\\\text{ nm}$ ($3.00\\\\text{ \\\\AA}$). (c) Mean free path $\\\\lambda = 92.9\\\\text{ nm}$, collision frequency $Z = 4.10\\\\times 10^9\\\\text{ s}^{-1}$."
        },
        {
            "id": "u8-p3",
            "title": "Brownian Motion Diffusion & Perrin Avogadro Number Determination",
            "statement": "In a precision Brownian motion experiment replicating Jean Perrin's Nobel measurements, spherical mastic resin particles of radius $r = 0.520\\\\times 10^{-6}\\\\text{ m}$ are suspended in water at temperature $T = 293.15\\\\text{ K}$ ($20.0^\\\\circ\\\\text{C}$) with dynamic viscosity $\\\\eta = 1.002\\\\times 10^{-3}\\\\text{ Pa}\\\\cdot\\\\text{s}$. (a) Calculate the Stokes hydrodynamic drag friction coefficient $\\\\gamma = 6\\\\pi \\\\eta r$. (b) Calculate the theoretical diffusion coefficient $D$ of the particles assuming Avogadro's number $N_A = 6.022\\\\times 10^{23}\\\\text{ mol}^{-1}$ ($R = 8.314\\\\text{ J/(mol}\\\\cdot\\\\text{K)}$). (c) Over an observation interval of $\\\\Delta t = 60.0\\\\text{ s}$, calculate the root-mean-square displacement $\\\\sqrt{\\\\langle x^2 \\\\rangle}$ along a single horizontal axis.",
            "steps": [
                {
                    "step": "Step 1: Calculate Stokes Friction Coefficient $\\\\gamma$",
                    "detail": "By Stokes' law for a sphere in laminar flow:\n$$\\\\gamma = 6\\\\pi \\\\eta r = 6\\\\pi (1.002 \\\\times 10^{-3}\\\\text{ Pa}\\\\cdot\\\\text{s})(0.520 \\\\times 10^{-6}\\\\text{ m})$$\n$$\\\\gamma = (18.8496)(1.002 \\\\times 10^{-3})(0.520 \\\\times 10^{-6}) = 9.821 \\\\times 10^{-9}\\\\text{ N}\\\\cdot\\\\text{s/m}$$"
                },
                {
                    "step": "Step 2: Calculate Diffusion Coefficient $D$",
                    "detail": "By the Einstein-Smoluchowski relation:\n$$D = \\\\frac{k_B T}{\\\\gamma} = \\\\frac{R T}{N_A \\\\gamma}$$\n$$k_B T = \\\\frac{(8.314)(293.15)}{6.022 \\\\times 10^{23}} = \\\\frac{2437.25}{6.022 \\\\times 10^{23}} = 4.0472 \\\\times 10^{-21}\\\\text{ J}$$\n$$D = \\\\frac{4.0472 \\\\times 10^{-21}\\\\text{ J}}{9.821 \\\\times 10^{-9}\\\\text{ N}\\\\cdot\\\\text{s/m}} = 4.121 \\\\times 10^{-13}\\\\text{ m}^2\\\\text{/s}$$"
                },
                {
                    "step": "Step 3: Calculate 1D Root-Mean-Square Displacement $\\\\sqrt{\\\\langle x^2 \\\\rangle}$",
                    "detail": "From Einstein's 1D diffusion law:\n$$\\\\langle x^2 \\\\rangle = 2 D \\\\Delta t$$\nFor $\\\\Delta t = 60.0\\\\text{ s}$:\n$$\\\\langle x^2 \\\\rangle = 2 (4.121 \\\\times 10^{-13}\\\\text{ m}^2\\\\text{/s})(60.0\\\\text{ s}) = 4.945 \\\\times 10^{-11}\\\\text{ m}^2$$\nTaking the square root:\n$$\\\\sqrt{\\\\langle x^2 \\\\rangle} = \\\\sqrt{4.945 \\\\times 10^{-11}} = 7.032 \\\\times 10^{-6}\\\\text{ m} = 7.03\\\\text{ }\\\\mu\\\\text{m}$$\nA displacement of $7\\\\text{ }\\\\mu\\\\text{m}$ in one minute is easily resolvable using standard optical microscopy, enabling direct empirical counting of molecular fluctuations."
                }
            ],
            "answer": "(a) Stokes friction factor $\\\\gamma = 9.82\\\\times 10^{-9}\\\\text{ N}\\\\cdot\\\\text{s/m}$. (b) Diffusion coefficient $D = 4.12\\\\times 10^{-13}\\\\text{ m}^2\\\\text{/s}$. (c) 1D root-mean-square displacement over 60 seconds is $\\\\sqrt{\\\\langle x^2 \\\\rangle} = 7.03\\\\text{ }\\\\mu\\\\text{m}$."
        }
    ]
}

with open("tp_u7.json", "w") as f:
    json.dump(u7, f, indent=2)
print("tp_u7.json written successfully.")

with open("tp_u8.json", "w") as f:
    json.dump(u8, f, indent=2)
print("tp_u8.json written successfully.")
