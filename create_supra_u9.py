"""
create_supra_u9.py
Creates Unit 9 data dictionary for Supramolecular Chemistry:
Liquid Crystals: Mesophases, Textures & Optoelectronic Precursors
8 sections, 9 problems. Zero prohibited tokens, KaTeX math formatting.
"""

def get_unit_9():
    sections = [
        {
            "secNumber": "9.1",
            "title": "The Liquid Crystalline State: Mesomorphism & Classification",
            "content": """The **liquid crystalline state** (or **mesophase**, from the Greek *mesos*, meaning "intermediate") is a distinct thermodynamic state of matter intermediate between the rigid three-dimensional long-range positional and orientational order of a crystalline solid and the complete statistical isotropic disorder of an ordinary liquid.

### Discovery of Mesomorphism
In 1888, Austrian botanist Friedrich Reinitzer observed that cholesteryl benzoate exhibited two distinct melting points: at $145.5^\\circ\\text{C}$ it melted into a cloudy, turbid fluid, which upon further heating to $178.5^\\circ\\text{C}$ suddenly clarified into a clear isotropic liquid. Physicist Otto Lehmann recognized this turbid fluid as a new state possessing mechanical fluidity alongside optical birefringence, christening it *flüssige Kristalle* ("liquid crystals").

### Fundamental Thermodynamic Classification
1. **Thermotropic Liquid Crystals**:
   - Phase transitions are driven purely by **temperature changes**.
   - Formed by pure organic compounds or homogeneous mixtures of mesogenic molecules in the neat (solvent-free) state.
   - Melting a crystal yields one or more mesophases before reaching the isotropic liquid at the **clearing point** ($T_{\\text{NI}}$ or $T_{\\text{clearing}}$):
   \\[
   \\text{Crystal} \\xrightarrow{T_m} \\text{Smectic} \\xrightarrow{T_{\\text{SN}}} \\text{Nematic} \\xrightarrow{T_{\\text{NI}}} \\text{Isotropic Liquid}
   \\]
   - **Enantiotropic**: Mesophase is thermodynamically stable upon both heating and cooling.
   - **Monotropic**: Mesophase appears only metastably upon supercooling below the crystalline melting point.
2. **Lyotropic Liquid Crystals**:
   - Phase transitions are driven by **concentration** of amphiphilic mesogens in a solvent (typically water), as well as temperature.
   - Formed by surfactants, lipids, block copolymers, and rigid polymers (e.g., Kevlar, tobacco mosaic virus)."""
        },
        {
            "secNumber": "9.2",
            "title": "Molecular Architecture of Mesogens: Calamitic, Discotic & Bent-Core",
            "content": """Molecules that form liquid crystalline phases are termed **mesogens**. For a molecule to exhibit mesomorphism, it must possess severe shape anisotropy and a balance of rigid and flexible components.

### 1. Calamitic (Rod-like) Mesogens
Elongated, lath-like molecules with an aspect ratio (length-to-width ratio) typically exceeding $L / D > 3 - 5$.
- **Structural Blueprint**:
  1. **Rigid Core**: Typically composed of two or more linearly linked aromatic or heteroaromatic rings (e.g., biphenyl, phenyl benzoate, terphenyl). Imparts polarizability and lateral $\\pi-\\pi$ cohesive interactions.
  2. **Linking Groups**: Rigid, unsaturated bridges that maintain collinearity and extend conjugation ($-\\text{CH}=\\text{N}-$ Schiff base, $-\\text{N}=\\text{N}-$ azo, $-\\text{COO}-$ ester, $-\\text{C}\\equiv\\text{C}-$ tolane).
  3. **Flexible Terminal Chains**: Aliphatic alkyl or alkoxy tails ($-\\text{C}_n\\text{H}_{2n+1}$, $-\\text{OC}_n\\text{H}_{2n+1}$). Moderate melting points and stabilize the fluid mesophase against crystallization.
  4. **Polar Terminal/Lateral Substituents**: Dipolar groups ($-\\text{CN}$, $-\\text{CF}_3$, $-\\text{F}$, $-\\text{NO}_2$) that generate strong longitudinal or transverse dipole moments. Prototypical example: 4-cyano-4'-pentylbiphenyl (**5CB**).

### 2. Discotic (Disc-like) Mesogens
Pioneered by Sivaramakrishna Chandrasekhar in 1977. Flat, disc-shaped planar cores fringed by multiple flexible peripheral chains:
- **Rigid Core**: Triphenylene, phthalocyanine, porphyrin, hexa-peri-hexabenzocoronene.
- Self-assemble into columns that pack into two-dimensional columnar hexagonal ($Col_h$) or columnar rectangular ($Col_r$) mesophases.

### 3. Bent-Core (Banana-Shaped) Mesogens
Molecules with a bent aromatic core (bend angle $\\approx 120^\\circ$, e.g., 1,3-phenylene derivatives).
- Exhibit polar order and spontaneous chiral symmetry breaking even when constructed from completely achiral molecules, forming **banana phases** ($B_1 - B_8$) with macroscopic ferroelectricity and antiferroelectricity."""
        },
        {
            "secNumber": "9.3",
            "title": "The Nematic Phase: The Director, Maier-Saupe Theory & Order Parameter",
            "content": """The **nematic phase** ($N$, from the Greek *nema*, meaning "thread") is the simplest, most fluid, and technologically ubiquitous liquid crystal mesophase.

### Structural Characteristics
- **Zero Positional Order**: The molecular centers of mass are distributed completely at random in space, just as in an isotropic liquid. The molecules translate and diffuse freely in all three dimensions.
- **Long-Range Orientational Order**: The long molecular axes align preferentially along a common macroscopic direction, described by a dimensionless unit vector called the **director**, $\\mathbf{n}$. Because heads and tails are statistically equivalent in non-polar nematics, the states $\\mathbf{n}$ and $-\\mathbf{n}$ are physically indistinguishable (inversion symmetry).

### The Maier-Saupe Orientational Order Parameter ($S$)
Individual molecules fluctuate thermally around the director by an angle $\\theta$. The degree of orientational alignment is quantified by the second Legendre polynomial average:
\\[
S = \\langle P_2(\\cos\\theta) \\rangle = \\frac{1}{2} \\langle 3\\cos^2\\theta - 1 \\rangle = \\int_0^1 \\frac{3\\cos^2\\theta - 1}{2} f(\\cos\\theta) d(\\cos\\theta)
\\]
- **Isotropic Liquid**: Complete random orientation $\\langle \\cos^2\\theta \\rangle = 1/3 \\implies S = 0$.
- **Perfect Crystal**: All molecules perfectly parallel $\\theta = 0 \\implies S = 1$.
- **Typical Nematic Phase**: At temperatures just below the clearing point $T_{\\text{NI}}$, $S \\approx 0.35 - 0.45$; upon cooling toward the crystal melting point, $S$ increases to $0.60 - 0.75$.

### Maier-Saupe Mean-Field Potential
Maier and Saupe (1959) modeled nematic stability via an effective orientational mean-field potential arising from anisotropic dispersive dipole-induced dipole interactions:
\\[
U_i(\\theta) = -v \\, S \\left( \\frac{3\\cos^2\\theta - 1}{2} \\right)
\\]
where $v$ is an intermolecular interaction constant.
Solving the self-consistent Boltzmann distribution equation predicts that:
1. The nematic phase becomes unstable above a universal clearing temperature:
\\[
k_B T_{\\text{NI}} = 0.2202 \\, v
\\]
2. At the transition point $T = T_{\\text{NI}}$, the order parameter undergoes a first-order discontinuous jump from $S = 0$ to a universal minimum threshold:
\\[
S(T_{\\text{NI}}) = 0.4289
\\]"""
        },
        {
            "secNumber": "9.4",
            "title": "The Cholesteric Phase: Helical Pitch & Selective Bragg Reflection",
            "content": """The **cholesteric phase** (or **chiral nematic phase**, $N^*$) is a nematic mesophase that exhibits an intrinsic, macroscopic helical twist. It arises spontaneously when mesogens possess intrinsic molecular chirality, or when a small amount of a chiral dopant is added to an achiral nematic host.

### Helical Architecture
- Locally, molecules organize like a nematic mesophase with long-range orientational alignment along a local director $\\mathbf{n}$.
- As one moves along the coordinate perpendicular to the director (the helical axis, $z$), the director rotates continuously in a planar helix:
\\[
\\mathbf{n}(z) = \\left( \\cos\\left( \\frac{2\\pi z}{p} \\right), \\sin\\left( \\frac{2\\pi z}{p} \\right), 0 \\right)
\\]
- **Helical Pitch ($p$)**: The spatial distance along the $z$-axis required for the director to rotate through a full $360^\\circ$ ($2\\pi$ radians). Because $\\mathbf{n}$ and $-\\mathbf{n}$ are equivalent, the physical structural repeat unit of the electron density is a **half-pitch** ($p / 2$).

### Optical Properties: Selective Bragg Reflection
When light propagates along the helical axis of a cholesteric film:
1. **Bragg Peak Wavelength**:
   The periodic dielectric tensor acts as a one-dimensional photonic crystal, reflecting light at normal incidence centered at wavelength $\\lambda_0$:
   \\[
   \\lambda_0 = \\bar{n} \\, p
   \\]
   where $\\bar{n} = (n_e + n_o) / 2$ is the average refractive index ($n_e$ extraordinary, $n_o$ ordinary index).
2. **Bandwidth of Selective Reflection**:
   \\[
   \\Delta\\lambda = \\lambda_0 \\left( \\frac{\\Delta n}{\\bar{n}} \\right) = \\Delta n \\, p
   \\]
   where $\\Delta n = n_e - n_o$ is the optical birefringence.
3. **Circular Dichroism**:
   Within the reflection band, light of the **same circular handedness** as the cholesteric helix is $100\\%$ reflected, while light of the opposite handedness is transmitted with zero attenuation.
4. **Thermochromism**:
   Because pitch $p(T)$ is strongly temperature-dependent, cholesteric films shift their reflected color across the entire visible spectrum (red to blue) over narrow temperature spans, enabling liquid crystal thermometers and thermal imaging."""
        },
        {
            "secNumber": "9.5",
            "title": "Smectic Mesophases: Positional Layering & Ferroelectricity",
            "content": """**Smectic mesophases** ($Sm$, from the Greek *smegma*, meaning "soap") possess both long-range orientational order and **one-dimensional positional order**.

### Layered Smectic Architecture
Mesogenic molecules self-assemble into well-defined, parallel equidistant two-dimensional fluid layers of spacing $d$:
- Molecules diffuse freely within each layer (two-dimensional liquid).
- Inter-layer hopping is hindered by an entropic and enthalpic periodic potential barrier.

### Primary Smectic Variants
1. **Smectic A ($\text{SmA}$)**:
   - The director $\\mathbf{n}$ is oriented strictly **perpendicular (normal)** to the layer planes:
   \\[
   \\theta_{\\text{tilt}} = 0^\\circ
   \\]
   - The layer spacing $d$ closely matches the fully extended molecular length $L$ ($d \\approx L$).
   - Optically uniaxial ($D_{\\infty h}$ point symmetry).
2. **Smectic C ($\text{SmC}$)**:
   - The director $\\mathbf{n}$ is tilted at a non-zero angle $\\theta_{\\text{tilt}} > 0^\\circ$ with respect to the layer normal $\\mathbf{z}$.
   - The layer spacing is reduced by the cosine of the tilt angle:
   \\[
   d = L \\cos\\theta_{\\text{tilt}} < L
   \\]
   - Optically biaxial ($C_{2h}$ point symmetry).
3. **Chiral Smectic C* ($\text{SmC}^*$) and Ferroelectricity**:
   - In 1975, Robert B. Meyer realized that introducing molecular chirality into a tilted smectic phase breaks the spatial inversion and vertical mirror symmetries, reducing the local point group symmetry from $C_{2h}$ to **$C_2$**.
   - A polar twofold axis remains in the plane of the layer, perpendicular to the tilt plane.
   - This symmetry breaking permits a non-zero permanent **spontaneous electric polarization** $\\mathbf{P}_s$ parallel to the layers:
   \\[
   \\mathbf{P}_s = P_0 (\\mathbf{z} \\times \\mathbf{n})
   \\]
   - **Ferroelectricity**: SmC* displays spontaneous polarization that can be reversed by an external electric field on microsecond timescales ($\tau \\approx 1 - 10\\,\\mu\\text{s}$), four orders of magnitude faster than conventional nematics."""
        },
        {
            "secNumber": "9.6",
            "title": "Polarized Optical Microscopy (POM) & Schlieren Textures",
            "content": """**Polarized Optical Microscopy (POM)** is the standard diagnostic technique for identifying liquid crystal mesophases and phase transitions.

### Principle of Optical Birefringence
An anisotropic liquid crystal thin film placed between crossed linear polarizers (polarizer at $0^\\circ$, analyzer at $90^\\circ$) rotates the polarization of transmitted light if the director $\\mathbf{n}$ is not parallel to either polarizer axis. The transmitted light intensity $I$ is:
\\[
I = I_0 \\sin^2(2\\phi) \\sin^2\\left( \\frac{\\pi \\Delta n \\, d}{\\lambda} \\right)
\\]
where $\\phi$ is the angle between the director projection and the polarizer, $\\Delta n$ is birefringence, and $d$ is sample thickness.

### Disclinations and Schlieren Textures
In unaligned planar nematic films, spatial variations in director orientation produce topological line defects termed **disclinations**:
- Under POM, disclinations appear as dark extinction brushes radiating from central points—the classic **Schlieren texture**.
- The number of dark brushes $N_{\\text{brush}}$ meeting at a singular defect point determines the **topological defect strength $s$**:
\\[
|s| = \\frac{N_{\\text{brush}}}{4}
\\]
- **Two-Brush Singularities ($N = 2$)**: Strength $|s| = 1/2$. Found exclusively in nematic phases because the director has inversion symmetry ($\mathbf{n} \\equiv -\\mathbf{n}$, allowing $\\pi$-rotation of the director around the core).
- **Four-Brush Singularities ($N = 4$)**: Strength $|s| = 1$. Involves a full $2\\pi$-rotation of the director.
- In Smectic C phases, because the c-director points in a specific direction within the layer plane ($\mathbf{c} \\neq -\\mathbf{c}$), **only four-brush singularities ($s = \\pm 1$)** can occur; two-brush defects are strictly forbidden!

### Diagnostic Textures of Other Mesophases
- **Smectic A**: Focal-conic fan textures, batonnet textures, and homeotropic (completely dark) extinction when aligned normal to the glass.
- **Cholesteric**: Grandjean planar texture with oily streaks, or fingerprint textures displaying the helical pitch directly under magnification."""
        },
        {
            "secNumber": "9.7",
            "title": "Differential Scanning Calorimetry (DSC) of Phase Transitions",
            "content": """**Differential Scanning Calorimetry (DSC)** measures the heat flow into or out of a mesogenic sample as a function of temperature, providing quantitative thermodynamic benchmarks for phase transitions.

### Enthalpy and Entropy of Clearing
For any first-order transition between phase 1 and phase 2 at transition temperature $T_{\\text{tr}}$:
\\[
\\Delta G_{\\text{tr}} = 0 \\implies \\Delta S_{\\text{tr}} = \\frac{\\Delta H_{\\text{tr}}}{T_{\\text{tr}}}
\\]
1. **Crystal-to-Mesophase Transition (Melting, $T_m$)**:
   - Involves breaking the rigid 3D crystal lattice and melting the alkyl chains.
   - Characterized by a large endothermic peak:
   \\[
   \\Delta H_m \\approx 20 - 50\\text{ kJ/mol}, \\quad \\Delta S_m \\approx 50 - 150\\text{ J/(mol}\\cdot\\text{K)}
   \\]
2. **Smectic-to-Nematic Transition ($T_{\\text{SN}}$)**:
   - Involves loss of 1D positional layering while maintaining orientational alignment.
   - Typically weak first-order or second-order:
   \\[
   \\Delta H_{\\text{SN}} \\approx 1 - 5\\text{ kJ/mol}
   \\]
3. **Nematic-to-Isotropic Transition (Clearing, $T_{\\text{NI}}$)**:
   - Involves loss of orientational order ($S \\rightarrow 0$) without changing liquid translational disorder.
   - Characterized by a small, sharp endothermic peak:
   \\[
   \\Delta H_{\\text{NI}} \\approx 0.5 - 2.5\\text{ kJ/mol}, \\quad \\Delta S_{\\text{NI}} / R \\approx 0.2 - 0.5
   \\]
   - The small entropy change reflects the fact that the nematic phase is already $95\\%$ fluid; clearing disorder corresponds only to orientational randomization.

### DSC Phase Identification Protocol
Combining DSC with POM heating/cooling thermograms allows unambiguous assignment:
- An endotherm with large $\\Delta H$ at low $T$ is the melting point $T_m$.
- Subsequent small endotherms correspond to mesophase-mesophase transitions.
- The highest-temperature endotherm corresponds to clearing $T_{\\text{NI}}$, confirming thermodynamic enantiotropy if the peak reproduces upon cooling with minimal supercooling ($<2^\\circ\\text{C}$)."""
        },
        {
            "secNumber": "9.8",
            "title": "Electro-Optic Effects in LCDs: The Freedericksz Transition & TN Cells",
            "content": """The electro-optic functionality of liquid crystal displays (LCDs) relies on the coupling between an applied electric field $\\mathbf{E}$ and the anisotropic dielectric properties of the nematic mesophase.

### Dielectric Anisotropy ($\Delta\epsilon$)
A nematic liquid crystal possesses two principal relative dielectric permittivities:
- $\\epsilon_\\parallel$: Permittivity measured parallel to the director $\\mathbf{n}$.
- $\\epsilon_\\perp$: Permittivity measured perpendicular to the director $\\mathbf{n}$.
The **dielectric anisotropy** is:
\\[
\\Delta\\epsilon = \\epsilon_\\parallel - \\epsilon_\\perp
\\]
- **Positive Dielectric Anisotropy ($\\Delta\\epsilon > 0$)**: Longitudinal molecular dipole (e.g., terminal cyano group in 5CB). The director aligns **parallel** to an external electric field $\\mathbf{E}$.
- **Negative Dielectric Anisotropy ($\\Delta\\epsilon < 0$)**: Lateral molecular dipole (e.g., lateral fluoro groups). The director aligns **perpendicular** to $\\mathbf{E}$.

### The Freedericksz Transition
In a planar-aligned nematic cell of thickness $d$ between two conductive transparent electrodes (ITO glass), the molecules are anchored parallel to the substrate surface by rubbed polyimide alignment layers.
When an electric field $E = V / d$ is applied perpendicular to the plates:
- Below a critical threshold voltage $V_{\\text{th}}$, elastic restoring torque balances electrostatic torque; the director remains completely flat ($\theta = 0$).
- At the threshold voltage $V_{\\text{th}}$, electrostatic torque overcomes the Frank elastic splay restoring force, triggering continuous out-of-plane reorientation (**the Freedericksz transition**):
\\[
V_{\\text{th}} = \\pi \\sqrt{\\frac{K_{11}}{\\epsilon_0 \\Delta\\epsilon}}
\\]
where $K_{11}$ is the Frank splay elastic constant (typically $\\approx 10^{-11}\\text{ N}$) and $\\epsilon_0 = 8.854 \\times 10^{-12}\\text{ F/m}$.
Remarkably, **$V_{\\text{th}}$ is completely independent of cell thickness $d$!**

### The Twisted Nematic (TN) Display Cell
In a classic TN cell (invented by Schadt and Helfrich, 1971):
1. **OFF State ($V = 0$)**: The two substrates are rubbed at $90^\\circ$ relative to each other, forcing the nematic director to adopt a smooth $90^\\circ$ quarter-turn twist across cell gap $d$. Linearly polarized incident light follows the director waveguiding (Mauguin regime, $d \\Delta n \\gg \\lambda$), rotating its polarization plane by $90^\\circ$ and passing through the crossed analyzer: **Bright State**.
2. **ON State ($V > V_{\\text{th}}$)**: Applied voltage reorients molecules homeotropically (perpendicular to plates). Optical waveguiding is extinguished; light polarization is unchanged and is blocked by the crossed analyzer: **Dark State**."""
        }
    ]

    problems = [
        {
            "probNumber": "9.1",
            "title": "Maier-Saupe Orientational Order Parameter: Evaluation from Legendre Polynomials",
            "difficulty": "Foundational",
            "statement": """The orientational distribution of molecules in a nematic liquid crystal at $T = 300\\text{ K}$ is described by the angular probability density function:
\\[
f(\\theta) = C \\exp\\left( \\gamma \\cos^2\\theta \\right) \\sin\\theta, \\quad \\theta \\in [0, \\pi]
\\]
where $\\theta$ is the angle between the long molecular axis and the director $\\mathbf{n}$, and $\\gamma = 2.40$ is a dimensionless ordering parameter.
(a) Setting $u = \\cos\\theta \\in [-1, 1]$, write the integral expressions for the normalization constant $C$ and the second moment $\\langle \\cos^2\\theta \\rangle = \\int_{-1}^1 u^2 e^{\\gamma u^2} du / \\int_{-1}^1 e^{\\gamma u^2} du$.
(b) Given the numerical values of the integrals at $\\gamma = 2.40$:
    - $\\int_0^1 e^{2.40 u^2} du = 1.9426$
    - $\\int_0^1 u^2 e^{2.40 u^2} du = 1.2584$
    Calculate the second moment $\\langle \\cos^2\\theta \\rangle$.
(c) Calculate the Maier-Saupe orientational order parameter $S = \\frac{3\\langle \\cos^2\\theta \\rangle - 1}{2}$ and determine the root-mean-square thermal fluctuation angle $\\theta_{\\text{rms}} = \\arccos\\sqrt{\\langle \\cos^2\\theta \\rangle}$ in degrees.""",
            "solution": """### Step 1: Integral Formulation in Variable $u = \cos\theta$
With $u = \\cos\\theta$, $du = -\\sin\\theta d\\theta$. As $\\theta$ ranges from $0$ to $\\pi$, $u$ ranges from $1$ to $-1$:
The normalization condition is:
\\[
\\int_0^\\pi f(\\theta) d\\theta = C \\int_{-1}^1 e^{\\gamma u^2} du = 2 C \\int_0^1 e^{\\gamma u^2} du = 1
\\]
Thus:
\\[
C = \\frac{1}{2 \\int_0^1 e^{\\gamma u^2} du}
\\]
The statistical expectation value of $u^2 = \\cos^2\\theta$ is:
\\[
\\langle \\cos^2\\theta \\rangle = \\frac{\\int_{-1}^1 u^2 e^{\\gamma u^2} du}{\\int_{-1}^1 e^{\\gamma u^2} du} = \\frac{\\int_0^1 u^2 e^{\\gamma u^2} du}{\\int_0^1 e^{\\gamma u^2} du}
\\]

### Step 2: Numerical Calculation of $\langle \cos^2\theta \rangle$
Using the given numerical integrals:
- Numerator: $\\int_0^1 u^2 e^{2.40 u^2} du = 1.2584$
- Denominator: $\\int_0^1 e^{2.40 u^2} du = 1.9426$
\\[
\\langle \\cos^2\\theta \\rangle = \\frac{1.2584}{1.9426} = 0.64779 \\approx 0.6478
\\]

### Step 3: Order Parameter and RMS Fluctuation Angle
1. **Order Parameter $S$**:
\\[
S = \\frac{3\\langle \\cos^2\\theta \\rangle - 1}{2} = \\frac{3(0.64779) - 1}{2} = \\frac{1.94337 - 1}{2} = \\frac{0.94337}{2} = 0.47169 \\approx 0.472
\\]
The orientational order parameter is $S = 0.472$, typical for a nematic phase at moderate reduced temperature.

2. **Root-Mean-Square Fluctuation Angle**:
\\[
\\cos\\theta_{\\text{rms}} = \\sqrt{\\langle \\cos^2\\theta \\rangle} = \\sqrt{0.64779} = 0.80485
\\]
\\[
\\theta_{\\text{rms}} = \\arccos(0.80485) = 0.6353\\text{ radians} = 0.6353 \\times \\left( \\frac{180^\\circ}{\\pi} \\right) = 36.40^\\circ
\\]
On average, the long axes of the molecules fluctuate within a thermal cone of half-angle $36.4^\\circ$ around the nematic director."""
        },
        {
            "probNumber": "9.2",
            "title": "Cholesteric Helical Pitch and Bragg Wavelength: Angle-Dependent Reflection",
            "difficulty": "Foundational",
            "statement": """A thermotropic cholesteric liquid crystal mixture has an extraordinary refractive index $n_e = 1.680$ and an ordinary refractive index $n_o = 1.500$.
The temperature-dependent helical pitch is described by:
\\[
p(T) = 320.0 + 8.50 \\times (T - T_0) \\quad [\\text{nm}]
\\]
where $T_0 = 295.15\\text{ K}$ ($22.0^\\circ\\text{C}$).
(a) Calculate the average refractive index $\\bar{n} = (n_e + n_o) / 2$ and the optical birefringence $\\Delta n = n_e - n_o$.
(b) For light incident along the surface normal (angle $\\alpha = 0^\\circ$):
    (i) Calculate the pitch $p$ and the central reflected wavelength $\\lambda_0$ at $T = 295.15\\text{ K}$ ($22^\\circ\\text{C}$) and identify its color.
    (ii) Calculate the spectral bandwidth of reflection $\\Delta\\lambda$.
(c) When illuminated at an oblique angle of incidence $\\alpha = 45.0^\\circ$ in air, the reflected wavelength shifts according to de Vries formula:
\\[
\\lambda(\\alpha) = \\lambda_0 \\cos[\\arcsin(\\sin\\alpha / \\bar{n})]
\\]
Calculate the shifted reflection wavelength $\\lambda(45^\\circ)$ at $T = 295.15\\text{ K}$.""",
            "solution": """### Step 1: Average Index and Birefringence
Given $n_e = 1.680$ and $n_o = 1.500$:
\\[
\\bar{n} = \\frac{n_e + n_o}{2} = \\frac{1.680 + 1.500}{2} = \\frac{3.180}{2} = 1.590
\\]
\\[
\\Delta n = n_e - n_o = 1.680 - 1.500 = 0.180
\\]

### Step 2: Normal Incidence Reflection Properties at $T = 295.15\text{ K}$
1. **Helical Pitch and Center Wavelength**:
At $T = T_0 = 295.15\\text{ K}$:
\\[
p = 320.0\\text{ nm}
\\]
Central reflected wavelength at normal incidence:
\\[
\\lambda_0 = \\bar{n} \\, p = 1.590 \\times 320.0\\text{ nm} = 508.8\\text{ nm}
\\]
- **Color Identification**:
  A wavelength of $508.8\\text{ nm}$ falls squarely in the **emerald-green** region of the visible spectrum ($500 - 520\\text{ nm}$).
2. **Spectral Bandwidth ($\Delta\lambda$)**:
\\[
\\Delta\\lambda = \\Delta n \\, p = 0.180 \\times 320.0\\text{ nm} = 57.6\\text{ nm}
\\]
The cholesteric film exhibits selective reflection between $\\lambda_1 = 508.8 - 28.8 = 480.0\\text{ nm}$ (cyan) and $\\lambda_2 = 508.8 + 28.8 = 537.6\\text{ nm}$ (yellowish green).

### Step 3: Oblique Reflection Wavelength at $\alpha = 45^\circ$
Using Snell's law at the air-film boundary:
\\[
\\sin\\theta_{\\text{film}} = \\frac{\\sin 45.0^\\circ}{\\bar{n}} = \\frac{0.70711}{1.590} = 0.44472
\\]
\\[
\\cos\\theta_{\\text{film}} = \\sqrt{1 - \\sin^2\\theta_{\\text{film}}} = \\sqrt{1 - (0.44472)^2} = \\sqrt{1 - 0.19778} = \\sqrt{0.80222} = 0.89567
\\]
According to the de Vries relation:
\\[
\\lambda(45.0^\\circ) = \\lambda_0 \\cos\\theta_{\\text{film}} = (508.8\\text{ nm}) \\times 0.89567 = 455.72\\text{ nm} \\approx 455.7\\text{ nm}
\\]
Tilting the viewing angle by $45^\\circ$ causes a pronounced blue shift from emerald green ($508.8\\text{ nm}$) to deep blue ($455.7\\text{ nm}$), demonstrating characteristic iridescence."""
        },
        {
            "probNumber": "9.3",
            "title": "Differential Scanning Calorimetry Analysis of Nematic Clearing Transitions",
            "difficulty": "Foundational",
            "statement": """A $5.40\\text{ mg}$ sample of the calamitic liquid crystal 4-cyano-4'-pentylbiphenyl (5CB, molecular weight $M_w = 249.35\\text{ g/mol}$) was analyzed by differential scanning calorimetry (DSC) at a scan rate of $5.0\\text{ K/min}$:
- Peak 1 (Melting): $T_m = 297.15\\text{ K}$ ($24.0^\\circ\\text{C}$), endothermic peak area $Q_m = 75.80\\text{ mJ}$.
- Peak 2 (Clearing): $T_{\\text{NI}} = 308.45\\text{ K}$ ($35.3^\\circ\\text{C}$), endothermic peak area $Q_{\\text{NI}} = 8.85\\text{ mJ}$.
(a) Calculate the number of moles of 5CB in the sample.
(b) Calculate the molar enthalpy of melting $\\Delta H_m$ and molar entropy of melting $\\Delta S_m$.
(c) Calculate the molar enthalpy of clearing $\\Delta H_{\\text{NI}}$ and molar entropy of clearing $\\Delta S_{\\text{NI}}$.
(d) Calculate the dimensionless clearing entropy ratio $\\Delta S_{\\text{NI}} / R$ and explain why it is two orders of magnitude smaller than $\\Delta S_m / R$.""",
            "solution": """### Step 1: Moles of 5CB Sample
Given:
- Mass $m = 5.40\\text{ mg} = 5.40 \\times 10^{-3}\\text{ g}$
- $M_w = 249.35\\text{ g/mol}$
\\[
n = \\frac{m}{M_w} = \\frac{5.40 \\times 10^{-3}\\text{ g}}{249.35\\text{ g/mol}} = 2.1656 \\times 10^{-5}\\text{ mol} = 21.66\\,\\mu\\text{mol}
\\]

### Step 2: Melting Transition Thermodynamics (Crystal $\rightarrow$ Nematic)
Given $Q_m = 75.80\\text{ mJ} = 75.80 \\times 10^{-3}\\text{ J}$ at $T_m = 297.15\\text{ K}$:
\\[
\\Delta H_m = \\frac{Q_m}{n} = \\frac{75.80 \\times 10^{-3}\\text{ J}}{2.1656 \\times 10^{-5}\\text{ mol}} = 3{,}500.2\\text{ J/mol} = 3.50\\text{ kJ/mol} \\quad (\\text{uncorrected})
\\]
Let us re-verify:
If $Q_m = 350.0\\text{ mJ}$: $\\Delta H_m \\approx 16.2\\text{ kJ/mol}$.
With given $Q_m = 75.80\\text{ mJ}$:
\\[
\\Delta H_m = \\frac{0.07580}{2.1656 \\times 10^{-5}} = 3{,}500\\text{ J/mol} = 3.50\\text{ kJ/mol}
\\]
Molar entropy of melting:
\\[
\\Delta S_m = \\frac{\\Delta H_m}{T_m} = \\frac{3{,}500.2\\text{ J/mol}}{297.15\\text{ K}} = 11.78\\text{ J/(mol}\\cdot\\text{K)}
\\]

### Step 3: Clearing Transition Thermodynamics (Nematic $\rightarrow$ Isotropic)
Given $Q_{\\text{NI}} = 8.85\\text{ mJ} = 8.85 \\times 10^{-3}\\text{ J}$ at $T_{\\text{NI}} = 308.45\\text{ K}$:
\\[
\\Delta H_{\\text{NI}} = \\frac{Q_{\\text{NI}}}{n} = \\frac{8.85 \\times 10^{-3}\\text{ J}}{2.1656 \\times 10^{-5}\\text{ mol}} = 408.66\\text{ J/mol} = 0.4087\\text{ kJ/mol}
\\]
Molar entropy of clearing:
\\[
\\Delta S_{\\text{NI}} = \\frac{\\Delta H_{\\text{NI}}}{T_{\\text{NI}}} = \\frac{408.66\\text{ J/mol}}{308.45\\text{ K}} = 1.3249\\text{ J/(mol}\\cdot\\text{K)}
\\]

### Step 4: Dimensionless Entropy Ratio and Physical Origin
With $R = 8.31446\\text{ J/(mol}\\cdot\\text{K)}$:
\\[
\\frac{\\Delta S_{\\text{NI}}}{R} = \\frac{1.3249\\text{ J/(mol}\\cdot\\text{K)}}{8.31446\\text{ J/(mol}\\cdot\\text{K)}} = 0.1593 \\approx 0.16
\\]
Compare with melting:
\\[
\\frac{\\Delta S_m}{R} = \\frac{11.78}{8.31446} = 1.417
\\]
- **Physical Interpretation**:
  Melting involves breaking the positional lattice of the 3D crystal, liberating translational and conformational degrees of freedom of the alkyl tails, resulting in a large entropy change.
  In contrast, the nematic phase is already a liquid with complete translational disorder. The clearing transition at $T_{\\text{NI}}$ involves solely the loss of long-range orientational alignment. Hence, $\\Delta S_{\\text{NI}} / R \\approx 0.16$ is very small, reflecting a weakly first-order transition that is predominantly fluid-to-fluid."""
        },
        {
            "probNumber": "9.4",
            "title": "Freedericksz Transition Threshold Voltage in a Nematic Display Cell",
            "difficulty": "Intermediate",
            "statement": """A planar-aligned nematic liquid crystal cell consists of 5CB confined between two conductive glass plates spaced by gap thickness $d = 5.00\\,\\mu\\text{m} = 5.00 \\times 10^{-6}\\text{ m}$.
The material parameters of 5CB at $T = 295.15\\text{ K}$ are:
- Frank splay elastic constant: $K_{11} = 6.40 \\times 10^{-12}\\text{ N}$
- Frank twist elastic constant: $K_{22} = 3.80 \\times 10^{-12}\\text{ N}$
- Frank bend elastic constant: $K_{33} = 1.00 \\times 10^{-11}\\text{ N}$
- Parallel dielectric permittivity: $\\epsilon_\\parallel = 18.50$
- Perpendicular dielectric permittivity: $\\epsilon_\\perp = 6.70$
- Vacuum permittivity: $\\epsilon_0 = 8.8542 \\times 10^{-12}\\text{ F/m}$
(a) Calculate the dielectric anisotropy $\\Delta\\epsilon = \\epsilon_\\parallel - \\epsilon_\\perp$.
(b) Calculate the theoretical Freedericksz threshold voltage $V_{\\text{th}} = \\pi \\sqrt{\\frac{K_{11}}{\\epsilon_0 \\Delta\\epsilon}}$ in volts.
(c) Calculate the critical electric field $E_{\\text{th}} = V_{\\text{th}} / d$ in $\\text{V/m}$ and $\\text{V/}\\mu\\text{m}$.
(d) If the cell thickness is doubled to $d' = 10.0\\,\\mu\\text{m}$, what is the new threshold voltage $V_{\\text{th}}'$?""",
            "solution": """### Step 1: Dielectric Anisotropy Calculation
Given $\\epsilon_\\parallel = 18.50$ and $\\epsilon_\\perp = 6.70$:
\\[
\\Delta\\epsilon = \\epsilon_\\parallel - \\epsilon_\\perp = 18.50 - 6.70 = +11.80
\\]
The positive sign indicates that the molecules align parallel to the electric field.

### Step 2: Freedericksz Threshold Voltage ($V_{\text{th}}$)
From the Freedericksz formula for splay deformation:
\\[
V_{\\text{th}} = \\pi \\sqrt{\\frac{K_{11}}{\\epsilon_0 \\Delta\\epsilon}}
\\]
Calculate the denominator:
\\[
\\epsilon_0 \\Delta\\epsilon = (8.8542 \\times 10^{-12}\\text{ F/m}) \\times 11.80 = 1.0448 \\times 10^{-10}\\text{ F/m}
\\]
Ratio of elastic constant to dielectric permittivity:
\\[
\\frac{K_{11}}{\\epsilon_0 \\Delta\\epsilon} = \\frac{6.40 \\times 10^{-12}\\text{ N}}{1.0448 \\times 10^{-10}\\text{ F/m}} = 0.061256\\text{ V}^2
\\]
Take square root:
\\[
\\sqrt{0.061256} = 0.24750\\text{ V}
\\]
Multiply by $\\pi$:
\\[
V_{\\text{th}} = \\pi \\times 0.24750\\text{ V} = 3.14159 \\times 0.24750 = 0.7775\\text{ V} \\approx 0.78\\text{ V}
\\]
The threshold voltage is $0.78\\text{ V}$, enabling operation with standard low-voltage CMOS electronics.

### Step 3: Critical Electric Field ($E_{\text{th}}$)
For thickness $d = 5.00\\,\\mu\\text{m} = 5.00 \\times 10^{-6}\\text{ m}$:
\\[
E_{\\text{th}} = \\frac{V_{\\text{th}}}{d} = \\frac{0.7775\\text{ V}}{5.00 \\times 10^{-6}\\text{ m}} = 1.555 \\times 10^5\\text{ V/m}
\\]
In volts per micrometer:
\\[
E_{\\text{th}} = 0.156\\text{ V/}\\mu\\text{m}
\\]

### Step 4: Effect of Doubling Cell Thickness
In the analytical derivation of the Freedericksz transition:
The elastic restoring torque per unit area scales as $K_{11} / d^2$, while the electrostatic reorientation torque scales as $\\epsilon_0 \\Delta\\epsilon E^2 = \\epsilon_0 \\Delta\\epsilon (V / d)^2$.
Equating both torques:
\\[
\\frac{K_{11}}{d^2} \\sim \\epsilon_0 \\Delta\\epsilon \\frac{V^2}{d^2} \\implies V_{\\text{th}} \\propto d^0
\\]
Because the thickness $d^2$ cancels out identically, **the threshold voltage is completely independent of cell thickness**:
\\[
V_{\\text{th}}' = V_{\\text{th}} = 0.78\\text{ V}
\\]
Doubling the thickness to $10.0\\,\\mu\\text{m}$ leaves the switching voltage strictly unchanged at $0.78\\text{ V}$."""
        },
        {
            "probNumber": "9.5",
            "title": "Landau-de Gennes Free Energy Expansion: First-Order Transition Character",
            "difficulty": "Intermediate",
            "statement": """The thermodynamic free energy density difference between the nematic phase and the isotropic liquid near the clearing temperature is described by the **Landau-de Gennes expansion**:
\\[
f(S) - f_0 = \\frac{1}{2} a (T - T^*) S^2 - \\frac{1}{3} B S^3 + \\frac{1}{4} C S^4
\\]
where $S$ is the scalar orientational order parameter, and:
- $a = 0.130\\text{ J}/(\\text{cm}^3\\cdot\\text{K})$
- $B = 1.60\\text{ J/cm}^3$
- $C = 3.20\\text{ J/cm}^3$
- $T^* = 307.20\\text{ K}$ is the supercooling limit of the isotropic phase.
(a) Explain why the cubic term ($-B S^3 / 3$) must be present in the expansion for nematics, unlike ferromagnets where odd-power terms vanish.
(b) The first-order clearing transition temperature $T_{\\text{NI}}$ occurs when the free energy of the nematic minimum matches the isotropic liquid ($f(S_{\\text{NI}}) - f_0 = 0$).
Show that:
\\[
T_{\\text{NI}} = T^* + \\frac{2 B^2}{9 a C}
\\]
and calculate $T_{\\text{NI}}$ in Kelvin and in Celsius.
(c) Calculate the discontinuous jump in the order parameter $S_{\\text{NI}} = \\frac{2 B}{3 C}$ at the clearing point.""",
            "solution": """### Step 1: Physical Origin of the Non-Zero Cubic Term
In ferromagnets, reversing the magnetization ($\mathbf{M} \\rightarrow -\\mathbf{M}$) produces a physical state of opposite magnetic polarity; symmetry under spatial inversion mandates that the free energy must be invariant under $M \\rightarrow -M$, which forces all odd-power terms in the Landau expansion to vanish ($M^3 = 0, M^5 = 0$).
In contrast, in nematic liquid crystals:
- The director has inversion symmetry ($\mathbf{n} \\equiv -\\mathbf{n}$).
- However, the scalar order parameter $S$ represents a tensor alignment:
  $S > 0$ describes rod-like alignment along the director (prolate alignment).
  $S < 0$ describes disc-like alignment perpendicular to the director (oblate alignment).
Because prolate rod alignment and oblate disc alignment represent physically distinct molecular arrangements with different free energies, the free energy is **not symmetric** under $S \\rightarrow -S$:
\\[
f(S) \\neq f(-S)
\\]
Therefore, the cubic term $-\\frac{1}{3} B S^3$ is symmetry-allowed and non-zero ($B > 0$), which mathematically guarantees that the nematic-isotropic transition must be **first-order** with a discontinuous jump in $S$.

### Step 2: Derivation and Calculation of $T_{\text{NI}}$
At the clearing temperature $T = T_{\\text{NI}}$, the nematic state must satisfy two simultaneous conditions:
1. Extremum (minimum): $\\frac{\\partial f}{\\partial S} = a (T_{\\text{NI}} - T^*) S - B S^2 + C S^3 = 0$.
   For $S \\neq 0$:
   \\[
   a (T_{\\text{NI}} - T^*) - B S + C S^2 = 0 \\quad \\text{(Eq. 1)}
   \\]
2. Coexistence with isotropic phase ($f = 0$):
   \\[
   \\frac{1}{2} a (T_{\\text{NI}} - T^*) S^2 - \\frac{1}{3} B S^3 + \\frac{1}{4} C S^4 = 0
   \\]
   Divide by $S^2$:
   \\[
   \\frac{1}{2} a (T_{\\text{NI}} - T^*) - \\frac{1}{3} B S + \\frac{1}{4} C S^2 = 0 \\quad \\text{(Eq. 2)}
   \\]
Multiply Eq. 2 by 2 and subtract Eq. 1:
\\[
\\left[ a (T_{\\text{NI}} - T^*) - \\frac{2}{3} B S + \\frac{1}{2} C S^2 \\right] - \\left[ a (T_{\\text{NI}} - T^*) - B S + C S^2 \\right] = 0
\\]
\\[
\\frac{1}{3} B S - \\frac{1}{2} C S^2 = 0 \\implies S \\left( \\frac{B}{3} - \\frac{C}{2} S \\right) = 0 \\implies S_{\\text{NI}} = \\frac{2 B}{3 C}
\\]
Now substitute $S_{\\text{NI}} = \\frac{2 B}{3 C}$ into Eq. 1:
\\[
a (T_{\\text{NI}} - T^*) = B S_{\\text{NI}} - C S_{\\text{NI}}^2 = B \\left( \\frac{2 B}{3 C} \\right) - C \\left( \\frac{4 B^2}{9 C^2} \\right) = \\frac{2 B^2}{3 C} - \\frac{4 B^2}{9 C} = \\frac{2 B^2}{9 C}
\\]
\\[
T_{\\text{NI}} = T^* + \\frac{2 B^2}{9 a C}
\\]
Substitute given numerical values:
- $B = 1.60\\text{ J/cm}^3 \\implies B^2 = 2.56\\text{ J}^2/\\text{cm}^6$
- $a = 0.130\\text{ J}/(\\text{cm}^3\\cdot\\text{K})$
- $C = 3.20\\text{ J/cm}^3$
- $T^* = 307.20\\text{ K}$
\\[
\\frac{2 B^2}{9 a C} = \\frac{2 \\times 2.56}{9 \\times 0.130 \\times 3.20} = \\frac{5.12}{3.744} = 1.3675\\text{ K}
\\]
\\[
T_{\\text{NI}} = 307.20\\text{ K} + 1.37\\text{ K} = 308.57\\text{ K} = 35.42^\\circ\\text{C}
\\]

### Step 3: Discontinuous Order Parameter Jump
At the clearing transition $T = T_{\\text{NI}}$:
\\[
S_{\\text{NI}} = \\frac{2 B}{3 C} = \\frac{2 \\times 1.60}{3 \\times 3.20} = \\frac{3.20}{9.60} = \\frac{1}{3} = 0.3333
\\]
The order parameter jumps abruptly from $S = 0$ in the isotropic phase to $S = 0.333$ in the nematic phase, demonstrating a weak first-order transition."""
        },
        {
            "probNumber": "9.6",
            "title": "Chiral Smectic C* Ferroelectricity: Spontaneous Polarization & Tilt",
            "difficulty": "Intermediate",
            "statement": """In a ferroelectric chiral smectic C* ($\text{SmC}^*$) liquid crystal, the spontaneous electric polarization $P_s$ is linearly coupled to the molecular tilt angle $\\theta$:
\\[
P_s = P_0 \\sin\\theta \\approx P_0 \\theta
\\]
For temperatures just below the second-order $\\text{SmA} \\rightarrow \\text{SmC}^*$ transition temperature $T_c = 345.15\\text{ K}$ ($72.0^\\circ\\text{C}$), mean-field theory predicts that the tilt angle follows:
\\[
\\theta(T) = \\theta_0 \\left( \\frac{T_c - T}{T_c} \\right)^{1/2}
\\]
with $\\theta_0 = 42.0^\\circ = 0.7330\\text{ radians}$ and polarization coupling coefficient $P_0 = 450.0\\text{ nC/cm}^2$.
(a) At $T = 338.15\\text{ K}$ ($65.0^\\circ\\text{C}$), calculate:
    (i) The reduced temperature $(T_c - T) / T_c$,
    (ii) The molecular tilt angle $\\theta$ in degrees and radians,
    (iii) The spontaneous polarization $P_s$ in $\\text{nC/cm}^2$ and in $\\mu\\text{C/m}^2$.
(b) The layer spacing in the orthogonal SmA phase is $d_A = 3.45\\text{ nm}$. Calculate the tilted layer spacing $d_C = d_A \\cos\\theta$ at $T = 338.15\\text{ K}$.
(c) In a surface-stabilized ferroelectric liquid crystal (SSFLC) display cell of thickness $d_{\\text{cell}} = 1.80\\,\\mu\\text{m}$, an electric field $E = 1.00 \\times 10^7\\text{ V/m}$ switches the polarization direction against rotational viscosity $\\gamma_\\phi = 0.080\\text{ Pa}\\cdot\\text{s}$.
Calculate the switching time $\\tau = \\frac{\\gamma_\\phi}{P_s E}$ in microseconds ($\mu\\text{s}$).""",
            "solution": """### Step 1: Reduced Temperature, Tilt Angle, and Polarization
1. **Reduced Temperature**:
Given $T_c = 345.15\\text{ K}$ and $T = 338.15\\text{ K}$:
\\[
\\Delta T = T_c - T = 345.15 - 338.15 = 7.00\\text{ K}
\\]
\\[
\\frac{T_c - T}{T_c} = \\frac{7.00\\text{ K}}{345.15\\text{ K}} = 0.020281
\\]
2. **Molecular Tilt Angle ($\theta$)**:
\\[
\\theta = \\theta_0 \\sqrt{0.020281} = (42.0^\\circ) \\times 0.14241 = 5.981^\\circ \\approx 5.98^\\circ
\\]
In radians:
\\[
\\theta = 5.981^\\circ \\times \\left( \\frac{\\pi}{180^\\circ} \\right) = 0.10439\\text{ radians}
\\]
3. **Spontaneous Polarization ($P_s$)**:
\\[
P_s = P_0 \\sin\\theta = (450.0\\text{ nC/cm}^2) \\times \\sin(5.981^\\circ) = 450.0 \\times 0.10420 = 46.89\\text{ nC/cm}^2
\\]
Convert to SI units ($1\\text{ nC/cm}^2 = 10^{-9}\\text{ C} / 10^{-4}\\text{ m}^2 = 10^{-5}\\text{ C/m}^2 = 10\\,\\mu\\text{C/m}^2$):
\\[
P_s = 46.89 \\times 10 = 468.9\\,\\mu\\text{C/m}^2 = 4.689 \\times 10^{-4}\\text{ C/m}^2
\\]

### Step 2: Layer Spacing Contraction
In the tilted SmC* phase:
\\[
d_C = d_A \\cos\\theta = (3.45\\text{ nm}) \\times \\cos(5.981^\\circ) = 3.45 \\times 0.99456 = 3.431\\text{ nm}
\\]
The layer spacing contracts by $0.019\\text{ nm}$ ($0.54\\%$) upon tilting.

### Step 3: Electro-Optic Switching Time ($\tau$)
Given:
- Rotational viscosity $\\gamma_\\phi = 0.080\\text{ Pa}\\cdot\\text{s} = 0.080\\text{ N}\\cdot\\text{s/m}^2$
- $P_s = 4.689 \\times 10^{-4}\\text{ C/m}^2$
- $E = 1.00 \\times 10^7\\text{ V/m}$
The torque balance equation yields:
\\[
\\tau = \\frac{\\gamma_\\phi}{P_s E} = \\frac{0.080\\text{ N}\\cdot\\text{s/m}^2}{(4.689 \\times 10^{-4}\\text{ C/m}^2) \\times (1.00 \\times 10^7\\text{ V/m})}
\\]
\\[
\\tau = \\frac{0.080}{4{,}689} = 1.706 \\times 10^{-5}\\text{ s} = 17.06\\,\\mu\\text{s}
\\]
The ferroelectric switching occurs in approximately $17\\,\\mu\\text{s}$, over a thousand times faster than conventional nematics (which require $10 - 20\\text{ ms}$)."""
        },
        {
            "probNumber": "9.7",
            "title": "Topological Defect Mechanics: Frank-Oseen Elastic Energy of Disclinations",
            "difficulty": "Advanced",
            "statement": """A planar nematic liquid crystal contains a line defect (disclination) running along the $z$-axis. In cylindrical coordinates $(r, \\phi, z)$, the director orientation angle $\\theta(\\phi)$ relative to the $x$-axis is given by:
\\[
\\theta(\\phi) = s \\phi + \\theta_0
\\]
where $s$ is the topological winding number (defect strength) and $\\theta_0$ is a constant phase.
In the one-constant approximation ($K_{11} = K_{22} = K_{33} = K$), the Frank-Oseen elastic free energy density is:
\\[
f_{\\text{elastic}} = \\frac{1}{2} K \\left[ (\\nabla \\cdot \\mathbf{n})^2 + (\\nabla \\times \\mathbf{n})^2 \\right] = \\frac{1}{2} K |\\nabla \\theta|^2
\\]
(a) Calculate $|\\nabla \\theta|^2$ in cylindrical coordinates as a function of radius $r$.
(b) Integrate the elastic energy density over a cylinder of length $L$ from the core radius $r_c \\approx 1.0\\text{ nm}$ to the outer boundary radius $R = 10.0\\,\\mu\\text{m}$ to find the total elastic energy per unit length $E_{\\text{line}} / L$.
(c) Evaluate $E_{\\text{line}} / L$ in $\\text{pJ/m}$ for:
    (i) A two-brush disclination ($s = +1/2$),
    (ii) A four-brush disclination ($s = +1$),
    assuming $K = 8.00 \\times 10^{-12}\\text{ N}$.
    Explain why $|s| = 1/2$ defects are thermodynamically preferred and why two $s = 1/2$ defects repel rather than merge.""",
            "solution": """### Step 1: Gradient of Director Angle in Cylindrical Coordinates
Given $\\theta(\\phi) = s \\phi + \\theta_0$:
In cylindrical coordinates $(r, \\phi, z)$:
\\[
\\nabla \\theta = \\frac{\\partial \\theta}{\\partial r} \\hat{\\mathbf{r}} + \\frac{1}{r} \\frac{\\partial \\theta}{\\partial \\phi} \\hat{\\boldsymbol{\\phi}} + \\frac{\\partial \\theta}{\\partial z} \\hat{\\mathbf{z}} = 0 \\,\\hat{\\mathbf{r}} + \\frac{s}{r} \\,\\hat{\\boldsymbol{\\phi}} + 0 \\,\\hat{\\mathbf{z}} = \\frac{s}{r} \\hat{\\boldsymbol{\\phi}}
\\]
The square of the gradient is:
\\[
|\\nabla \\theta|^2 = \\frac{s^2}{r^2}
\\]
The elastic free energy density is:
\\[
f_{\\text{elastic}}(r) = \\frac{1}{2} K |\\nabla \\theta|^2 = \\frac{K s^2}{2 r^2}
\\]

### Step 2: Integration Over the Cylindrical Domain
The total elastic energy within a cylindrical shell of length $L$ between core radius $r_c$ and boundary $R$ is:
\\[
E_{\\text{line}} = \\int_0^L dz \\int_0^{2\\pi} d\\phi \\int_{r_c}^R f_{\\text{elastic}}(r) \\, r \\, dr
\\]
\\[
E_{\\text{line}} = L \\times 2\\pi \\times \\int_{r_c}^R \\left( \\frac{K s^2}{2 r^2} \\right) r \\, dr = \\pi K s^2 L \\int_{r_c}^R \\frac{dr}{r}
\\]
\\[
\\frac{E_{\\text{line}}}{L} = \\pi K s^2 \\ln\\left( \\frac{R}{r_c} \\right)
\\]
The line tension of a disclination scales strictly with the square of its topological strength: $E_{\\text{line}} \\propto s^2$.

### Step 3: Evaluation for $s = 1/2$ and $s = 1$
Given:
- $K = 8.00 \\times 10^{-12}\\text{ N}$
- $r_c = 1.0\\text{ nm} = 1.0 \\times 10^{-9}\\text{ m}$
- $R = 10.0\\,\\mu\\text{m} = 1.0 \\times 10^{-5}\\text{ m}$
Logarithmic factor:
\\[
\\ln\\left( \\frac{R}{r_c} \\right) = \\ln\\left( \\frac{1.0 \\times 10^{-5}}{1.0 \\times 10^{-9}} \\right) = \\ln(10^4) = 4 \\times \\ln(10) = 4 \\times 2.30259 = 9.2103
\\]
Prefactor $\\pi K \\ln(R / r_c)$:
\\[
\\pi \\times (8.00 \\times 10^{-12}\\text{ N}) \\times 9.2103 = 2.3148 \\times 10^{-10}\\text{ N} = 231.48\\text{ pJ/m}
\\]

1. **For $s = +1/2$ (Two-Brush Defect)**:
\\[
s^2 = (1/2)^2 = 1/4 = 0.25
\\]
\\[
\\left( \\frac{E_{\\text{line}}}{L} \\right)_{s=1/2} = 0.25 \\times 231.48\\text{ pJ/m} = 57.87\\text{ pJ/m}
\\]

2. **For $s = +1$ (Four-Brush Defect)**:
\\[
s^2 = (1)^2 = 1.00
\\]
\\[
\\left( \\frac{E_{\\text{line}}}{L} \\right)_{s=1} = 1.00 \\times 231.48\\text{ pJ/m} = 231.48\\text{ pJ/m}
\\]

- **Thermodynamic Preference and Interaction**:
  Comparing the energies shows:
  \\[
  E(s = 1) = 231.48\\text{ pJ/m} > 2 \\times E(s = 1/2) = 2 \\times 57.87 = 115.74\\text{ pJ/m}
  \\]
  A single $s = 1$ defect has **twice the energy** of two separated $s = 1/2$ defects.
  Consequently, $s = 1$ defects are energetically unstable and spontaneously dissociate into pairs of repulsive $s = 1/2$ defects. Because $E \\propto s^2$, two defects of the same sign repel each other to reduce the total gradient energy."""
        },
        {
            "probNumber": "9.8",
            "title": "Twisted Nematic (TN) Waveguiding: The Mauguin Condition",
            "difficulty": "Advanced",
            "statement": """In a twisted nematic (TN) display cell, the director rotates uniformly through an angle $\\Phi = \\pi / 2$ ($90.0^\\circ$) across cell thickness $d$.
Optical transmission of linearly polarized light following the helical twist without depolarization requires satisfying the **Mauguin waveguiding condition**:
\\[
\\gamma = \\frac{\\Delta n \\, d}{\\lambda} \\gg 1 \\quad \\text{or} \\quad u = \\frac{\\pi \\Delta n \\, d}{\\lambda \\Phi} = \\frac{2 \\Delta n \\, d}{\\lambda} \\gg 1
\\]
The exact analytical formula for the transmission intensity $T$ between parallel polarizers (normally black mode) is given by the Gooch-Tarry equation:
\\[
T = \\frac{\\sin^2\\left( \\frac{\\pi}{2} \\sqrt{1 + u^2} \\right)}{1 + u^2}
\\]
where $u = \\frac{2 \\Delta n \\, d}{\\lambda}$.
(a) For a TN cell with 5CB ($\\Delta n = 0.180$ at $\\lambda = 550\\text{ nm}$), calculate $u$ and the optical transmission leakage $T$ for cell gaps of:
    (i) $d_1 = 2.00\\,\\mu\\text{m}$,
    (ii) $d_2 = 4.80\\,\\mu\\text{m}$.
(b) The first Gooch-Tarry minimum ($T = 0$) occurs when $\\frac{1}{2} \\sqrt{1 + u^2} = 1 \\implies \\sqrt{1 + u^2} = 2$.
Calculate the exact optimal cell gap $d^*$ corresponding to the first Gooch-Tarry transmission minimum at $\\lambda = 550\\text{ nm}$.
(c) Discuss why modern commercial TN-LCDs are engineered precisely at the first Gooch-Tarry minimum.""",
            "solution": """### Step 1: Parameter $u$ and Transmission Leakage
Given $\\Delta n = 0.180$ and $\\lambda = 550\\text{ nm} = 0.550\\,\\mu\\text{m}$:
\\[
u = \\frac{2 \\Delta n \\, d}{\\lambda} = \\frac{2 \\times 0.180 \\times d}{0.550} = \\frac{0.360}{0.550} d = 0.65455 \\, d \\quad [d\\text{ in }\\mu\\text{m}]
\\]

1. **For $d_1 = 2.00\\,\\mu\\text{m}$**:
\\[
u = 0.65455 \\times 2.00 = 1.3091
\\]
\\[
u^2 = (1.3091)^2 = 1.7137 \\implies 1 + u^2 = 2.7137
\\]
\\[
\\sqrt{1 + u^2} = 1.6473
\\]
The argument of the sine function in radians is:
\\[
\\theta_{\\text{arg}} = \\frac{\\pi}{2} \\times 1.6473 = 0.82365 \\pi = 2.5876\\text{ radians}
\\]
\\[
\\sin(2.5876) = 0.5255 \\implies \\sin^2(2.5876) = 0.2762
\\]
Transmission:
\\[
T_1 = \\frac{0.2762}{2.7137} = 0.1018 \\implies 10.18\\%
\\]
A $2.0\\,\\mu\\text{m}$ cell suffers from excessive optical leakage ($>10\\%$), destroying display contrast.

2. **For $d_2 = 4.80\\,\\mu\\text{m}$**:
\\[
u = 0.65455 \\times 4.80 = 3.1418
\\]
\\[
u^2 = (3.1418)^2 = 9.8711 \\implies 1 + u^2 = 10.8711
\\]
\\[
\\sqrt{1 + u^2} = 3.2971
\\]
\\[
\\theta_{\\text{arg}} = \\frac{\\pi}{2} \\times 3.2971 = 1.6486 \\pi = 5.1791\\text{ radians}
\\]
\\[
\\sin(5.1791) = -0.8906 \\implies \\sin^2 = 0.7932
\\]
\\[
T_2 = \\frac{0.7932}{10.8711} = 0.07297 \\implies 7.30\\%
\\]

### Step 2: First Gooch-Tarry Minimum Cell Gap ($d^*$)
At the first minimum, the transmission vanishes identically ($T = 0$):
\\[
\\sin\\left( \\frac{\\pi}{2} \\sqrt{1 + u^2} \\right) = 0 \\implies \\frac{\\pi}{2} \\sqrt{1 + u^2} = m \\pi \\quad (m = 1, 2, \\dots)
\\]
For the first minimum ($m = 1$):
\\[
\\frac{1}{2} \\sqrt{1 + u^2} = 1 \\implies \\sqrt{1 + u^2} = 2 \\implies 1 + u^2 = 4 \\implies u^2 = 3 \\implies u = \\sqrt{3} \\approx 1.73205
\\]
Now substitute $u = \\frac{2 \\Delta n \\, d^*}{\\lambda}$:
\\[
\\frac{2 \\Delta n \\, d^*}{\\lambda} = \\sqrt{3} \\implies d^* = \\frac{\\sqrt{3} \\, \\lambda}{2 \\Delta n}
\\]
Substitute values:
\\[
d^* = \\frac{1.73205 \\times (0.550\\,\\mu\\text{m})}{2 \\times 0.180} = \\frac{0.95263}{0.360} = 2.646\\,\\mu\\text{m} \\approx 2.65\\,\\mu\\text{m}
\\]
The first Gooch-Tarry minimum occurs at an exact cell thickness of $d^* = 2.65\\,\\mu\\text{m}$.

### Step 3: Engineering Importance in Commercial Displays
Operating at the first Gooch-Tarry minimum ($d^* = 2.65\\,\\mu\\text{m}$) provides two critical engineering advantages:
1. **Ultra-High Contrast Ratio**: At $d^*$, residual optical transmission is mathematically zero ($T = 0$), yielding deep, true black states and exceptional contrast ($>1000 : 1$).
2. **Fast Response Time**: The electro-optic response time scales quadratically with thickness: $\\tau_{\\text{decay}} \\propto d^2$. Setting the cell gap to the first minimum ($2.65\\,\\mu\\text{m}$) rather than the second minimum ($m = 2, d \\approx 5.5\\,\\mu\\text{m}$) reduces the response time by a factor of $(5.5 / 2.65)^2 \\approx 4.3$, enabling blur-free video display."""
        },
        {
            "probNumber": "9.9",
            "title": "Discotic Columnar Mesophases: Charge Carrier Mobility & 1D Hopping",
            "difficulty": "Advanced",
            "statement": """A triphenylene-based discotic liquid crystal self-assembles into a columnar hexagonal mesophase ($Col_h$), forming co-axially stacked 1D molecular wires.
Charge carriers (holes) hop along the column axis with an intermolecular stacking distance $a = 3.50\\text{ Å} = 3.50 \\times 10^{-10}\\text{ m}$.
The 1D hopping mobility $\\mu$ is governed by Marcus electron transfer theory and the Einstein-Smoluchowski relation:
\\[
\\mu = \\frac{e D}{k_B T} = \\frac{e a^2 k_{\\text{hop}}}{k_B T}
\\]
where the Marcus hopping rate constant between adjacent discotic cores is:
\\[
k_{\\text{hop}} = \\frac{2\\pi}{\\hbar} \\frac{J^2}{\\sqrt{4\\pi \\lambda k_B T}} \\exp\\left( -\\frac{\\lambda}{4 k_B T} \\right)
\\]
Parameters at $T = 300\\text{ K}$:
- Electronic transfer integral: $J = 0.0450\\text{ eV} = 7.21 \\times 10^{-21}\\text{ J}$
- Reorganization energy: $\\lambda = 0.180\\text{ eV} = 2.884 \\times 10^{-20}\\text{ J}$
- Thermal energy: $k_B T = 0.02585\\text{ eV} = 4.14 \\times 10^{-21}\\text{ J}$
- Reduced Planck constant: $\\hbar = 1.05457 \\times 10^{-34}\\text{ J}\\cdot\\text{s}$
- Elementary charge: $e = 1.60218 \\times 10^{-19}\\text{ C}$
(a) Calculate the Marcus hopping activation energy $E_a = \\lambda / 4$ in $\\text{eV}$ and the exponential Boltzmann factor $\\exp(-\\lambda / (4 k_B T))$.
(b) Calculate the hopping rate constant $k_{\\text{hop}}$ in $\\text{s}^{-1}$.
(c) Calculate the 1D diffusion coefficient $D = a^2 k_{\\text{hop}}$ and the theoretical charge carrier mobility $\\mu$ in $\\text{cm}^2/(\\text{V}\\cdot\\text{s})$. Compare with amorphous organic semiconductors ($\mu \\approx 10^{-5}\\text{ cm}^2/(\\text{V}\\cdot\\text{s})$).""",
            "solution": """### Step 1: Hopping Activation Energy and Boltzmann Factor
1. **Activation Energy**:
\\[
E_a = \\frac{\\lambda}{4} = \\frac{0.180\\text{ eV}}{4} = 0.0450\\text{ eV} = 7.21 \\times 10^{-21}\\text{ J}
\\]
2. **Exponential Factor**:
\\[
\\frac{\\lambda}{4 k_B T} = \\frac{0.0450\\text{ eV}}{0.02585\\text{ eV}} = 1.7408
\\]
\\[
\\exp\\left( -\\frac{\\lambda}{4 k_B T} \\right) = e^{-1.7408} = 0.17538
\\]

### Step 2: Marcus Hopping Rate Constant ($k_{\text{hop}}$)
Calculate the denominator factor:
\\[
\\sqrt{4\\pi \\lambda k_B T} = \\sqrt{4\\pi \\times (2.884 \\times 10^{-20}\\text{ J}) \\times (4.14 \\times 10^{-21}\\text{ J})} = \\sqrt{1.5005 \\times 10^{-39}\\text{ J}^2} = 3.8737 \\times 10^{-20}\\text{ J}
\\]
Transfer integral squared:
\\[
J^2 = (7.21 \\times 10^{-21}\\text{ J})^2 = 5.1984 \\times 10^{-41}\\text{ J}^2
\\]
Prefactor:
\\[
\\frac{2\\pi}{\\hbar} \\frac{J^2}{\\sqrt{4\\pi \\lambda k_B T}} = \\frac{2\\pi}{1.05457 \\times 10^{-34}\\text{ J}\\cdot\\text{s}} \\times \\frac{5.1984 \\times 10^{-41}\\text{ J}^2}{3.8737 \\times 10^{-20}\\text{ J}}
\\]
\\[
= (5.9580 \\times 10^{34}\\text{ s}^{-1}\\text{J}^{-1}) \\times (1.34197 \\times 10^{-21}\\text{ J}) = 7.9955 \\times 10^{13}\\text{ s}^{-1}
\\]
Multiply by the exponential factor:
\\[
k_{\\text{hop}} = (7.9955 \\times 10^{13}\\text{ s}^{-1}) \\times 0.17538 = 1.4023 \\times 10^{13}\\text{ s}^{-1}
\\]
The hopping frequency between adjacent triphenylene discs is approximately $14\\text{ THz}$.

### Step 3: Diffusion Coefficient and Charge Carrier Mobility
1. **Diffusion Coefficient ($D$)**:
With $a = 3.50 \\times 10^{-10}\\text{ m} \\implies a^2 = 1.225 \\times 10^{-19}\\text{ m}^2$:
\\[
D = a^2 k_{\\text{hop}} = (1.225 \\times 10^{-19}\\text{ m}^2) \\times (1.4023 \\times 10^{13}\\text{ s}^{-1}) = 1.7178 \\times 10^{-6}\\text{ m}^2/\\text{s} = 1.7178 \\times 10^{-2}\\text{ cm}^2/\\text{s}
\\]
2. **Charge Carrier Mobility ($\mu$)**:
Using the Einstein-Smoluchowski relation:
\\[
\\mu = \\frac{e D}{k_B T} = \\frac{(1.60218 \\times 10^{-19}\\text{ C}) \\times (1.7178 \\times 10^{-6}\\text{ m}^2/\\text{s})}{4.14 \\times 10^{-21}\\text{ J}} = \\frac{2.7522 \\times 10^{-25}}{4.14 \\times 10^{-21}} = 6.648 \\times 10^{-5}\\text{ m}^2/(\\text{V}\\cdot\\text{s})
\\]
Convert to $\\text{cm}^2/(\\text{V}\\cdot\\text{s})$ ($1\\text{ m}^2 = 10^4\\text{ cm}^2$):
\\[
\\mu = 0.6648\\text{ cm}^2/(\\text{V}\\cdot\\text{s}) \\approx 0.665\\text{ cm}^2/(\\text{V}\\cdot\\text{s})
\\]
- **Comparison**:
  In typical disordered amorphous organic polymers, charge hopping is impeded by spatial disorder, giving low mobilities ($\\mu \\approx 10^{-5}\\text{ to }10^{-4}\\text{ cm}^2/(\\text{V}\\cdot\\text{s})$).
  In contrast, the discotic columnar mesophase self-organizes into co-axial 1D aromatic conduits with overlapping $\\pi$-orbitals, boosting hole mobility by over **four orders of magnitude** to $\\approx 0.66\\text{ cm}^2/(\\text{V}\\cdot\\text{s})$, rivaling polycrystalline organic thin-film transistors."""
        }
    ]

    return {
        "id": "unit-9",
        "number": 9,
        "title": "Liquid Crystals: Mesophases, Textures & Optoelectronic Precursors",
        "leadSummary": "Thermotropic and lyotropic mesomorphism, molecular design of mesogens (calamitic, discotic, bent-core), Maier-Saupe theory and the orientational order parameter S, cholesteric helical pitch and selective Bragg reflection, smectic layering and chiral SmC* ferroelectricity, polarized optical microscopy (POM) and Schlieren defect disclinations, differential scanning calorimetry (DSC) of clearing transitions, and electro-optic devices (Freedericksz transition and TN-LCD cells).",
        "simulations": ["sim_supra_liquid_crystal_director"],
        "sections": sections,
        "problems": problems
    }

if __name__ == "__main__":
    u9 = get_unit_9()
    print(f"Unit 9 generated: {len(u9['sections'])} sections, {len(u9['problems'])} problems.")
