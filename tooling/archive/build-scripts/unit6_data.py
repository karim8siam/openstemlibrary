# -*- coding: utf-8 -*-
# Unit 6: Dispersion and the Drude-Lorentz Theory

UNIT_6 = {
    "id": "unit-6",
    "number": 6,
    "title": "Dispersion, Drude-Lorentz Theory & Optical Properties of Matter",
    "leadSummary": "Exhaustive theoretical investigation into electromagnetic dispersion in macroscopic media: normal versus anomalous dispersion, the Drude-Lorentz classical harmonic oscillator model of atomic dielectrics, complex dielectric permittivity tensor, real index of refraction and extinction coefficient, resonance absorption bands, Sellmeier dispersion equations, the Drude free-electron gas theory of metals, DC and optical AC conductivity, optical reflectivity and UV plasma transparency, and microscopic local field corrections via the Clausius-Mossotti and Lorentz-Lorenz relations.",
    "simulations": ["drude-lorentz"],
    "sections": [
        {
            "secNumber": "6.1",
            "heading": "Normal and Anomalous Optical Dispersion in Transparent Media",
            "content": """
#### Definition of Optical Dispersion
In a physical material medium, the phase velocity $v$ of an electromagnetic wave depends on the temporal frequency $\\omega$ (or free-space wavelength $\\lambda_0$) of the wave:
$$v(\\omega) = \\frac{c}{n(\\omega)}$$
where $n(\\omega)$ is the frequency-dependent **refractive index**. The variation of the refractive index with wavelength or frequency, $\\frac{dn}{d\\lambda}$ or $\\frac{dn}{d\\omega}$, is known as **optical dispersion**.

Because different spectral colors travel at different velocities, white light passing through a glass prism separates into its constituent spectral hues.

#### 1. Normal Dispersion ($\\frac{dn}{d\\lambda} < 0$)
In regions of the electromagnetic spectrum far away from any atomic or molecular resonant absorption bands, the refractive index decreases monotonically with increasing wavelength:
$$\\frac{dn}{d\\lambda} < 0 \\quad \\iff \\quad \\frac{dn}{d\\omega} > 0$$
Short wavelengths (blue light) experience a larger refractive index and bend more sharply than long wavelengths (red light):
$$n_{\\text{blue}} > n_{\\text{yellow}} > n_{\\text{red}}$$

In normal dispersion regimes, the empirical behavior is accurately modeled by **Cauchy's Equation** (Augustin-Louis Cauchy 1836):
$$n(\\lambda) = A + \\frac{B}{\\lambda^2} + \\frac{C}{\\lambda^4} + \\dots$$
where $A, B, C$ are empirical positive constants characteristic of the optical glass.

#### 2. Anomalous Dispersion ($\\frac{dn}{d\\lambda} > 0$)
In the immediate vicinity of an absorption band (where the incident photon frequency matches an atomic or molecular transition frequency), the situation reverses abruptly:
$$\\frac{dn}{d\\lambda} > 0 \\quad \\iff \\quad \\frac{dn}{d\\omega} < 0$$
Here, longer wavelengths experience a greater index of refraction than shorter wavelengths. Within this anomalous dispersion zone, the material exhibits intense resonant absorption of electromagnetic energy.
"""
        },
        {
            "secNumber": "6.2",
            "heading": "The Drude-Lorentz Classical Harmonic Oscillator Model of Dielectrics",
            "content": """
#### Microscopic Mechanical Equation of Motion
Hendrik Lorentz and Paul Drude formulated a microscopic classical model of dielectrics by picturing an atom as a nucleus surrounded by bound electrons. An electron of mass $m_e$ and charge $-e$ is subject to:
1. **Electrostatic Restoring Force:** $\\mathbf{F}_{\\text{restoring}} = -m_e \\omega_0^2 \\mathbf{r}$, where $\\omega_0$ is the natural resonant frequency of atomic binding.
2. **Dissipative Frictional Damping Force:** $\\mathbf{F}_{\\text{damping}} = -m_e \\gamma \\frac{d\\mathbf{r}}{dt}$, where $\\gamma$ accounts for radiative damping and atomic collisions.
3. **Driving Electric Force:** $\\mathbf{F}_{\\text{drive}} = -e \\mathbf{E}(t) = -e \\mathbf{E}_0 e^{-i\\omega t}$.

Newton's second law for the electron displacement is:
$$m_e \\left( \\frac{d^2 \\mathbf{r}}{dt^2} + \\gamma \\frac{d\\mathbf{r}}{dt} + \\omega_0^2 \\mathbf{r} \\right) = -e \\mathbf{E}_0 e^{-i\\omega t}$$

Looking for steady-state sinusoidal solutions $\\mathbf{r}(t) = \\mathbf{r}_0 e^{-i\\omega t}$:
$$m_e (-\\omega^2 - i\\gamma \\omega + \\omega_0^2) \\mathbf{r}_0 = -e \\mathbf{E}_0$$
$$\\mathbf{r}_0 = -\\frac{e / m_e}{\\omega_0^2 - \\omega^2 - i\\gamma \\omega} \\mathbf{E}_0$$

#### Induced Macroscopic Polarization ($\\mathbf{P}$)
Let the medium contain $N$ atoms per unit volume, with $Z$ electrons per atom distributed among different natural resonant frequencies $\\omega_j$ with oscillator strengths $f_j$ (satisfying the Thomas-Reiche-Kuhn sum rule $\\sum_j f_j = Z$). The macroscopic electric dipole polarization density is:
$$\\mathbf{P} = -N e \\sum_j f_j \\mathbf{r}_j = \\frac{N e^2}{m_e} \\left[ \\sum_j \\frac{f_j}{\\omega_j^2 - \\omega^2 - i\\gamma_j \\omega} \\right] \\mathbf{E}$$

#### The Complex Dielectric Function
From the macroscopic relation $\\mathbf{D} = \\epsilon_0 \\mathbf{E} + \\mathbf{P} \\equiv \\epsilon(\\omega) \\mathbf{E} = \\epsilon_r(\\omega) \\epsilon_0 \\mathbf{E}$:
$$\\tilde{\\epsilon}_r(\\omega) = 1 + \\frac{\\mathbf{P}}{\\epsilon_0 \\mathbf{E}} = 1 + \\frac{N e^2}{\\epsilon_0 m_e} \\sum_j \\frac{f_j}{\\omega_j^2 - \\omega^2 - i\\gamma_j \\omega}$$
This fundamental relation is the **Drude-Lorentz Complex Dielectric Function**.
"""
        },
        {
            "secNumber": "6.3",
            "heading": "Complex Index of Refraction and Extinction Coefficient",
            "content": """
#### Real and Imaginary Optical Constants
The complex index of refraction $\\tilde{n}$ is defined as the square root of the complex relative permittivity (for non-magnetic media $\\mu_r \\approx 1$):
$$\\tilde{n}(\\omega) \\equiv n(\\omega) + i\\kappa(\\omega) = \\sqrt{\\tilde{\\epsilon}_r(\\omega)}$$
where:
- $n(\\omega)$ is the **real refractive index** (governing phase velocity $v = c/n$ and refraction angles via Snell's law).
- $\\kappa(\\omega)$ is the **extinction coefficient** (governing optical absorption and wave attenuation).

Squaring both sides:
$$\\tilde{n}^2 = (n + i\\kappa)^2 = n^2 - \\kappa^2 + 2i n\\kappa = \\text{Re}(\\tilde{\\epsilon}_r) + i\\text{Im}(\\tilde{\\epsilon}_r)$$

Equating real and imaginary parts:
$$n^2 - \\kappa^2 = \\text{Re}(\\tilde{\\epsilon}_r)$$
$$2n\\kappa = \\text{Im}(\\tilde{\\epsilon}_r)$$

For a single dominant resonant transition of frequency $\\omega_0$ and oscillator strength $f$:
$$\\text{Re}(\\tilde{\\epsilon}_r) = 1 + \\frac{N e^2 f}{\\epsilon_0 m_e} \\frac{\\omega_0^2 - \\omega^2}{(\\omega_0^2 - \\omega^2)^2 + \\gamma^2 \\omega^2}$$
$$\\text{Im}(\\tilde{\\epsilon}_r) = \\frac{N e^2 f}{\\epsilon_0 m_e} \\frac{\\gamma \\omega}{(\\omega_0^2 - \\omega^2)^2 + \\gamma^2 \\omega^2}$$

#### Physical Consequences Across the Spectrum
1. **Well Below Resonance ($\\omega \\ll \\omega_0$):**
   $\\text{Im}(\\tilde{\\epsilon}_r) \\approx 0$, meaning $\\kappa \\approx 0$ (transparent medium). $\\text{Re}(\\tilde{\\epsilon}_r) > 1$, and $n$ increases with $\\omega$ (normal dispersion).
2. **Near Resonance ($\\omega \\approx \\omega_0$):**
   $\\text{Im}(\\tilde{\\epsilon}_r)$ reaches a sharp Lorentzian peak, causing strong **resonant absorption**. Simultaneously, $\\text{Re}(\\tilde{\\epsilon}_r)$ drops steeply, producing a negative slope $\\frac{dn}{d\\omega} < 0$ (**anomalous dispersion**).
3. **Well Above Resonance ($\\omega \\gg \\omega_0$):**
   The medium becomes transparent again, with $n < 1$, approaching $n \\to 1$ asymptotically at X-ray frequencies.
"""
        },
        {
            "secNumber": "6.4",
            "heading": "Resonance Absorption Bands and the Sellmeier Dispersion Equation",
            "content": """
#### Derivation of the Sellmeier Formula
In optical materials such as crown glass, fused silica, and quartz, the damping constants $\\gamma_j$ are typically much smaller than the resonant frequencies $\\omega_j$. In transparent optical windows far from absorption lines ($\\gamma_j \\ll |\\omega_j - \\omega|$):
$$\\tilde{\\epsilon}_r(\\omega) \\approx 1 + \\sum_j \\frac{B_j \\omega_j^2}{\\omega_j^2 - \\omega^2}$$
where $B_j = \\frac{N e^2 f_j}{\\epsilon_0 m_e \\omega_j^2}$.

Converting from angular frequencies $\\omega$ to free-space wavelengths $\\lambda$ using $\\omega = 2\\pi c/\\lambda$ yields the **Sellmeier Dispersion Formula** (Wolfgang von Sellmeier 1871):
$$n^2(\\lambda) = 1 + \\sum_{j=1}^m \\frac{B_j \\lambda^2}{\\lambda^2 - C_j}$$
where $C_j = \\lambda_j^2$ represents the square of the absorption resonance wavelengths, and $B_j$ are dimensionless empirical coefficients.

For fused silica ($\text{SiO}_2$), a standard three-term Sellmeier equation accurately predicts refractive index across the entire range from ultraviolet ($0.21\\,\\mu\\text{m}$) to mid-infrared ($3.71\\,\\mu\\text{m}$) with precision exceeding $10^{-5}$, enabling the design of precision camera lenses and fiber optic telecommunication systems.
"""
        },
        {
            "secNumber": "6.5",
            "heading": "The Drude Free-Electron Gas Theory of Metals",
            "content": """
#### Metals as an Unbound Electron Plasma
In electrical conductors and metals (such as silver, gold, and copper), valence electrons are not bound to individual atomic cores ($\\omega_0 = 0$). They move freely through a background of positive lattice ions, experiencing collisions with an average relaxation time $\\tau$ (damping rate $\\gamma = 1/\\tau$).

Setting $\\omega_0 = 0$ and $\\gamma = 1/\\tau$ in the equation of motion:
$$m_e \\left( \\frac{d^2 \\mathbf{r}}{dt^2} + \\frac{1}{\\tau} \\frac{d\\mathbf{r}}{dt} \\right) = -e \\mathbf{E}$$
$$\\mathbf{v}(t) = \\frac{d\\mathbf{r}}{dt} = -\\frac{e \\mathbf{E}_0 / m_e}{1/\\tau - i\\omega} e^{-i\\omega t} = -\\frac{e \\tau / m_e}{1 - i\\omega \\tau} \\mathbf{E}$$

#### Complex AC Conductivity ($\\tilde{\\sigma}(\\omega)$)
The macroscopic conduction current density is $\\mathbf{J} = -n_e e \\mathbf{v} = \\tilde{\\sigma}(\\omega) \\mathbf{E}$, where:
$$\\tilde{\\sigma}(\\omega) = \\frac{\\sigma_0}{1 - i\\omega \\tau}$$
and $\\sigma_0 = \\frac{n_e e^2 \\tau}{m_e}$ is the standard **DC electrical conductivity**.

#### Drude Dielectric Permittivity of Metals
Substituting into Maxwell's equations:
$$\\tilde{\\epsilon}_r(\\omega) = 1 + i \\frac{\\tilde{\\sigma}}{\\omega \\epsilon_0} = 1 - \\frac{\\sigma_0 / (\\epsilon_0 \\tau)}{\\omega^2 + i\\omega / \\tau} = 1 - \\frac{\\omega_p^2}{\\omega(\\omega + i/\\tau)}$$
where $\\omega_p = \\sqrt{\\frac{n_e e^2}{\\epsilon_0 m_e}}$ is the **bulk plasma frequency of the metal**.

#### High-Frequency Regime ($\\omega \\tau \\gg 1$)
At optical frequencies (visible and UV), $\\omega \\tau \\gg 1$, and collision damping can be neglected ($1/\\tau \\to 0$):
$$\\epsilon_r(\\omega) \\approx 1 - \\frac{\\omega_p^2}{\\omega^2}$$

1. **Below the Plasma Frequency ($\\omega < \\omega_p$):**
   $\\epsilon_r(\\omega) < 0$. The refractive index is purely imaginary: $\\tilde{n} = i\\kappa$. The wave cannot propagate and reflects totally ($R = 1.00$). This explains the brilliant silvery luster and mirror-like reflectance of metals.
2. **Above the Plasma Frequency ($\\omega > \\omega_p$):**
   $\\epsilon_r(\\omega) > 0$. The metal becomes transparent to electromagnetic radiation! For alkali metals, $\\omega_p$ lies in the near-ultraviolet, producing the famous **ultraviolet transparency of metals** discovered experimentally by Wood in 1933.
"""
        },
        {
            "secNumber": "6.6",
            "heading": "Local Field Corrections in Condensed Media (Clausius-Mossotti & Lorentz-Lorenz)",
            "content": """
#### The Microscopic Local Field ($\\mathbf{E}_{\\text{local}}$)
In a dilute gas, molecules are separated by large distances, so the local electric field polarizing a molecule is simply the macroscopic applied field $\\mathbf{E}$. However, in dense liquids and condensed solids, each molecule is polarized not only by external sources, but also by the intense dipolar electric fields of all neighboring polarized molecules.

By constructing a virtual spherical cavity (Lorentz sphere) around a given molecule, Hendrik Lorentz proved that the local field is:
$$\\mathbf{E}_{\\text{local}} = \\mathbf{E} + \\frac{\\mathbf{P}}{3\\epsilon_0}$$
where $\\frac{\\mathbf{P}}{3\\epsilon_0}$ is the depolarization field contribution from the inner surface of the Lorentz cavity.

#### The Clausius-Mossotti Relation
The induced dipole moment of a single molecule is $\\mathbf{p} = \\alpha \\mathbf{E}_{\\text{local}}$, where $\\alpha$ is the microscopic molecular polarizability. The macroscopic polarization is:
$$\\mathbf{P} = N \\mathbf{p} = N \\alpha \\left( \\mathbf{E} + \\frac{\\mathbf{P}}{3\\epsilon_0} \\right)$$

Using $\\mathbf{P} = \\epsilon_0 (\\epsilon_r - 1) \\mathbf{E}$:
$$\\epsilon_0 (\\epsilon_r - 1) \\mathbf{E} = N \\alpha \\mathbf{E} \\left[ 1 + \\frac{\\epsilon_r - 1}{3} \\right] = N \\alpha \\mathbf{E} \\left[ \\frac{\\epsilon_r + 2}{3} \\right]$$

Rearranging yields the celebrated **Clausius-Mossotti Relation**:
$$\\frac{\\epsilon_r - 1}{\\epsilon_r + 2} = \\frac{N \\alpha}{3\\epsilon_0}$$

#### The Lorentz-Lorenz Formula for Optical Frequencies
At optical frequencies, Maxwell's relation gives $\\epsilon_r = n^2$. Substituting into Clausius-Mossotti yields the **Lorentz-Lorenz Equation**:
$$\\frac{n^2 - 1}{n^2 + 2} = \\frac{N \\alpha}{3\\epsilon_0}$$

This equation links a macroscopic optical observable—the index of refraction $n$—directly to microscopic quantum atomic parameters: number density $N$ and molecular polarizability $\\alpha$.
"""
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
                    "explanation": "In terms of polarizability volume $\\alpha' = \\frac{\\alpha}{4\\pi\\epsilon_0} = 1.12 \\times 10^{-29}\\text{ m}^3 = 11.2\\text{ \u00c5}^3$, closely matching the physical volume of a $\\text{CCl}_4$ molecule."
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

print("Unit 6 built successfully. Sections:", len(UNIT_6["sections"]), "Problems:", len(UNIT_6["problems"]))
