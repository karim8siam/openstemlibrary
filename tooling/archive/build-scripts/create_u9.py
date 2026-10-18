import json

def get_unit_9():
    u9 = {
        "id": "unit-9",
        "number": 9,
        "title": "Extended Imperfections, Dislocations & Doped Semiconductors",
        "leadSummary": "1D line defects (edge and screw dislocations, Burgers vectors), Peach-Koehler force, Peierls-Nabarro lattice friction, Schmid's law, 2D planar defects (grain boundaries, Read-Shockley theory, stacking faults), extrinsic semiconductor charge transport, and the quantum Hall effect.",
        "simulations": ["sim_ssc_dislocation_mechanics"],
        "sections": [
            {
                "secNumber": "9.1",
                "title": "Line Imperfections: Edge Dislocations, Dislocation Line & Burgers Vector",
                "content": r"""Unlike 0D point defects (which are thermodynamically stable at $T > 0\\text{ K}$), 1D line defects—**dislocations**—possess high elastic strain energies ($E_{\\text{line}} \\sim 10^9\\text{ eV/cm}$) and are non-equilibrium mechanical imperfections introduced during crystal growth, thermal quenching, or plastic shear.

### The Edge Dislocation Concept
An edge dislocation (introduced by Taylor, Orowan, and Polanyi in 1934) can be visualized as inserting an extra half-plane of atoms into an otherwise perfect crystal:
- **Dislocation Line ($\mathbf{t}$)**: The line along the bottom edge of the extra half-plane, forming the boundary between the slipped and unslipped regions of the crystal.
- **Stress Distribution**: Above the slip plane, atomic planes are squeezed together, creating a localized hydrostatic **compression zone**. Below the slip plane, atomic bonds are stretched, creating a hydrostatic **tension zone**.
- **Symbol**: Represented by $\\bot$ (positive edge dislocation, extra half-plane above slip plane) or $\\top$ (negative edge dislocation, extra half-plane below).

### The Burgers Circuit and Burgers Vector ($\mathbf{b}$)
The fundamental mathematical descriptor of any dislocation is its **Burgers vector** $\\mathbf{b}$ (J. M. Burgers, 1939), determined via the right-hand finish-to-start (RH/FS) convention:
1. In the dislocated crystal, construct a closed atom-to-atom loop (Burgers circuit) encircling the dislocation line $\\mathbf{t}$.
2. Traverse the identical sequence of lattice translation vectors in an ideal, defect-free reference lattice.
3. The closure failure vector pointing from the finish point to the start point in the perfect lattice is the **Burgers vector** $\\mathbf{b}$.
- **Geometric Orthogonality**: For a pure **edge dislocation**, the Burgers vector is strictly **perpendicular** to the dislocation line vector:
\\[
\\mathbf{b} \\perp \\mathbf{t} \\quad (\\mathbf{b} \\cdot \\mathbf{t} = 0)
\\]
The slip plane is uniquely defined as the plane containing both $\\mathbf{b}$ and $\\mathbf{t}$ (normal vector $\\mathbf{n} \\propto \\mathbf{b} \\times \\mathbf{t}$)."""
            },
            {
                "secNumber": "9.2",
                "title": "Screw Dislocations, Mixed Dislocations & Frank-Read Sources",
                "content": r"""A **screw dislocation** transforms the parallel atomic planes of a crystal into a continuous helical spiral staircase (Riemann surface) winding around the dislocation axis.

### Geometric Characteristics of Screw Dislocations
- **Shear Topology**: Formed by cutting a crystal halfway through and shifting one side parallel to the cut boundary by one lattice vector.
- **Burgers Vector Alignment**: For a pure **screw dislocation**, the Burgers vector is strictly **parallel** to the dislocation line vector:
\\[
\\mathbf{b} \\parallel \\mathbf{t} \\quad (\\mathbf{b} \\times \\mathbf{t} = \\mathbf{0})
\\]
- **Cross-Slip**: Because $\\mathbf{b} \\parallel \\mathbf{t}$, the normal vector $\\mathbf{b} \\times \\mathbf{t} = \\mathbf{0}$ does not define a unique slip plane. A screw dislocation can move along any crystallographic plane passing through $\\mathbf{t}$ that has high packing density (**cross-slip**).

### Mixed Dislocations
Real dislocations in crystals are generally neither pure edge nor pure screw, but curve continuously through the lattice as **mixed dislocations**:
- At an arbitrary segment of a curved dislocation with local tangent $\\hat{\\mathbf{t}}$, the Burgers vector $\\mathbf{b}$ can be decomposed into:
\\[
\\mathbf{b} = \\mathbf{b}_{\\parallel} + \\mathbf{b}_{\\perp} = (\\mathbf{b} \\cdot \\hat{\\mathbf{t}})\\hat{\\mathbf{t}} + \\left[\\hat{\\mathbf{t}} \\times (\\mathbf{b} \\times \\hat{\\mathbf{t}})\\right] = \\mathbf{b}_{\\text{screw}} + \\mathbf{b}_{\\text{edge}}
\\]
where the angle $\\theta$ between $\\mathbf{b}$ and $\\mathbf{t}$ dictates the screw component ($b\\cos\\theta$) and edge component ($b\\sin\\theta$).

### Dislocation Multiplication: The Frank-Read Source
Plastic deformation requires billions of new dislocations. Charles Frank and W. T. Read (1950) proposed the regenerative dislocation multiplication mechanism:
1. A dislocation segment of length $L$ is pinned at both ends by solute atoms or node intersections.
2. Under an applied resolved shear stress $\\tau$, the pinned segment bows outward into a circular arc of radius $R = \\frac{G b}{2\\tau}$.
3. When $\\tau$ exceeds the critical activation stress:
\\[
\\tau_{\\text{crit}} = \\frac{2 T_{\\text{line}}}{b L} \\approx \\frac{G b}{L}
\\]
the arc becomes semicircular ($R = L/2$) and becomes unstable, wrapping around the pinning points.
4. Opposite segments meet, annihilate, and detach as an expanding closed dislocation loop, while the original segment regenerates to repeat the cycle indefinitely."""
            },
            {
                "secNumber": "9.3",
                "title": "Stress Fields of Dislocations, Strain Energy & Peach-Koehler Force",
                "content": r"""The atomic displacements surrounding a dislocation core induce long-range elastic strain fields governed by continuum linear elasticity theory.

### Elastic Stress Fields in Isotropic Media
Using cylindrical coordinates $(r, \\theta, z)$ with the dislocation line along the $z$-axis:
1. **Pure Screw Dislocation** ($\mathbf{b} = (0, 0, b)$):
   Exhibits pure shear strain with zero hydrostatic dilatation (no volume change, $\\Delta V = 0$):
   \\[
   \\sigma_{\\theta z} = \\sigma_{z \\theta} = \\frac{G b}{2\\pi r}, \\quad \\sigma_{rr} = \\sigma_{\\theta\\theta} = \\sigma_{zz} = 0
   \\]
   where $G$ is the shear modulus.

2. **Pure Edge Dislocation** ($\mathbf{b} = (b, 0, 0)$):
   Exhibits both shear and hydrostatic normal stresses:
   \\[
   \\sigma_{rr} = \\sigma_{\\theta\\theta} = -\\frac{G b}{2\\pi(1-\\nu)} \\frac{\\sin\\theta}{r}
   \\]
   \\[
   \\sigma_{r\\theta} = \\frac{G b}{2\\pi(1-\\nu)} \\frac{\\cos\\theta}{r}
   \\]
   \\[
   \\sigma_{zz} = \\nu (\\sigma_{rr} + \\sigma_{\\theta\\theta}) = -\\frac{\\nu G b}{\\pi(1-\\nu)} \\frac{\\sin\\theta}{r}
   \\]
   where $\\nu$ is Poisson's ratio. Notice the characteristic $1/r$ divergence as $r \\to 0$.

### Dislocation Line Strain Energy
Integrating the elastic strain energy density $w = \\frac{1}{2} \\boldsymbol{\\sigma} : \\boldsymbol{\\varepsilon}$ from the core radius $r_0 \\approx b$ out to the crystal boundary radius $R$:
\\[
E_{\\text{screw}} = \\frac{G b^2}{4\\pi} \\ln\\left(\\frac{R}{r_0}\\right)
\\]
\\[
E_{\\text{edge}} = \\frac{G b^2}{4\\pi(1-\\nu)} \\ln\\left(\\frac{R}{r_0}\\right) = \\frac{E_{\\text{screw}}}{1-\\nu}
\\]
Because $(1-\\nu) \\approx 0.7$, an edge dislocation has approximately $40\\%$ higher strain energy than a screw dislocation.

### The Peach-Koehler Force
The virtual mechanical force per unit length $\\mathbf{f}$ exerted on a dislocation by an external stress tensor $\\boldsymbol{\\sigma}$ is given by the **Peach-Koehler equation**:
\\[
\\mathbf{f} = (\\boldsymbol{\\sigma} \\cdot \\mathbf{b}) \\times \\mathbf{t}
\\]
For a pure shear stress $\\tau$ resolved in the slip plane in the direction of $\\mathbf{b}$, the glide force per unit length is simply $f_{\\text{glide}} = \\tau b$."""
            },
            {
                "secNumber": "9.4",
                "title": "Dislocation Slip, Peierls-Nabarro Stress & Schmid's Law",
                "content": r"""Plastic deformation in crystalline materials proceeds via the conservative motion of dislocations along well-defined slip systems (**dislocation slip**).

### The Peierls-Nabarro Lattice Friction Stress
Even in a pure, defect-free crystal, a dislocation experiences an intrinsic periodic potential barrier as it glides from one lattice valley to the next. The minimum shear stress required to move a dislocation through the crystal without thermal activation is the **Peierls-Nabarro stress** ($\\tau_{\\text{PN}}$):
\\[
\\tau_{\\text{PN}} = \\frac{2G}{1 - \\nu} \\exp\\left( -\\frac{2\\pi w}{b} \\right) = \\frac{2G}{1 - \\nu} \\exp\\left( -\\frac{2\\pi d}{(1-\\nu)b} \\right)
\\]
where $w = d/(1-\\nu)$ is the dislocation core width, $d$ is the interplanar spacing of the slip planes, and $b$ is the magnitude of the Burgers vector.
- **Physical Meaning**: $\\tau_{\\text{PN}}$ decreases exponentially with the ratio $d/b$. Therefore, dislocations slip with the lowest resistance along **the most widely spaced crystallographic planes** (maximum $d$), which correspond to the **densest atomic close-packed planes** (e.g., $\{111\}$ in FCC, $\{0001\}$ in HCP).
- In FCC metals (wide core width, $w/b \\approx 2-3$), $\\tau_{\\text{PN}} \\approx 10^{-5} G$ (extremely ductile).
- In covalent semiconductors like Si or GaAs (narrow core width due to directional covalent bonds, $w/b \\approx 1$), $\\tau_{\\text{PN}} \\approx 10^{-1} G$ (brittle at room temperature).

### Schmid's Law and Resolved Shear Stress
Under a uniaxial tensile stress $\\sigma$ applied to a single crystal:
- Let $\\phi$ be the angle between the tensile loading axis and the slip plane normal $\\hat{\\mathbf{n}}$.
- Let $\\lambda$ be the angle between the tensile axis and the slip direction $\\hat{\\mathbf{b}}$.
The resolved shear stress $\\tau_{\\text{RSS}}$ acting on the slip system is:
\\[
\\tau_{\\text{RSS}} = \\frac{F_{\\text{shear}}}{A_{\\text{slip}}} = \\frac{F \\cos\\lambda}{A_0 / \\cos\\phi} = \\sigma \\cos\\phi \\cos\\lambda = m \\sigma
\\]
where $m = \\cos\\phi \\cos\\lambda$ is the **Schmid factor** ($0 \\le m \\le 0.5$).
- **Schmid's Law**: Dislocation slip initiates when $\\tau_{\\text{RSS}}$ reaches a critical threshold characteristic of the material, the **Critical Resolved Shear Stress (CRSS)** $\\tau_{\\text{CRSS}}$:
\\[
\\sigma_y = \\frac{\\tau_{\\text{CRSS}}}{\\cos\\phi \\cos\\lambda} = \\frac{\\tau_{\\text{CRSS}}}{m_{\\max}}
\\]"""
            },
            {
                "secNumber": "9.5",
                "title": "Planar Defects: Grain Boundaries, Read-Shockley Theory & Stacking Faults",
                "content": r"""Planar (2D) defects interrupt the continuous periodicity of the crystal lattice across two-dimensional interfaces.

### Low-Angle vs High-Angle Grain Boundaries
1. **Low-Angle Tilt Boundaries ($\theta < 10^\circ$)**:
   Formed by an array of parallel edge dislocations aligned vertically one above the other with uniform spacing $D$:
   \\[
   \\sin\\left(\\frac{\\theta}{2}\\right) \\approx \\frac{\\theta}{2} = \\frac{b}{2D} \\implies D = \\frac{b}{\\theta}
   \\]
   **Read-Shockley Theory**: The interfacial energy per unit area $\\gamma(\\theta)$ of a low-angle boundary is:
   \\[
   \\gamma(\\theta) = E_0 \\theta (A - \\ln\\theta)
   \\]
   where $E_0 = \\frac{G b}{4\\pi(1-\\nu)}$ and $A$ is an integration constant reflecting the core energy.
2. **High-Angle Grain Boundaries ($\theta > 15^\circ$)**:
   Dislocation cores overlap completely ($D \\sim b$). The interface becomes an amorphous-like disordered zone characterized by high interfacial energy ($\\gamma_{\\text{HAGB}} \\approx 0.3 - 0.8\\text{ J/m}^2$) that serves as sinks for impurities and high-diffusivity pathways.

### Stacking Faults and Partial Dislocations
In close-packed FCC structures ($\dots ABCABC \dots$ along $[111]$), a localized error in the close-packing sequence creates a **stacking fault**:
- **Intrinsic Stacking Fault**: One layer missing: $\dots ABC | BCABC \dots$ (locally creates four layers of HCP packing $BCBC$).
- **Extrinsic Stacking Fault**: Extra layer inserted: $\dots ABCA | B | CABC \dots$.
- **Shockley Partial Dislocations**: A full dislocation $\\frac{a}{2}[110]$ dissociates into two Shockley partials bounding a ribbon of stacking fault to minimize total strain energy:
\\[
\\frac{a}{2}[110] \\to \\frac{a}{6}[211] + \\frac{a}{6}[12\\bar{1}]
\\]
By Frank's energy rule ($E \\propto b^2$):
\\[
b_1^2 = \\left(\\frac{a}{2}\\right)^2 (1^2 + 1^2 + 0) = \\frac{a^2}{2}
\\]
\\[
b_2^2 + b_3^2 = 2 \\times \\left(\\frac{a}{6}\\right)^2 (4 + 1 + 1) = 2 \\times \\frac{6a^2}{36} = \\frac{a^2}{3} < \\frac{a^2}{2}
\\]
Because $\\frac{a^2}{3} < \\frac{a^2}{2}$, dissociation is energetically favorable! The equilibrium separation width $d_{\\text{eq}}$ between partials is inversely proportional to the **Stacking Fault Energy** $\\gamma_{\\text{SFE}}$:
\\[
d_{\\text{eq}} = \\frac{G b_2 \\cdot b_3}{2\\pi \\gamma_{\\text{SFE}}}
\\]"""
            },
            {
                "secNumber": "9.6",
                "title": "Extrinsic Semiconductor Physics: Hydrogenic Impurity States & Compensation",
                "content": r"""The electronic behavior of extrinsic semiconductors is governed by isolated donor and acceptor states that introduce localized energy levels within the forbidden band gap.

### The Hydrogenic Effective-Mass Model
Consider a pentavalent phosphorus atom ($\\text{P}$) substituting on a tetravalent silicon site. Four valence electrons participate in tetrahedral covalent $sp^3$ bonding, while the fifth electron experiences the Coulomb attraction of the net $+1e$ core of the $\\text{P}^+$ nucleus.
Because this electron moves through the host dielectric medium of relative permittivity $\\varepsilon_r$, its potential is:
\\[
V(r) = -\\frac{e^2}{4\\pi \\varepsilon_0 \\varepsilon_r r}
\\]
Adapting the Bohr model of the hydrogen atom by replacing electron rest mass $m_0$ with conduction-band effective mass $m_e^*$ and free-space permittivity with $\\varepsilon_0 \\varepsilon_r$:
1. **Donor Binding Energy ($E_d$)**:
\\[
E_d = \\left( \\frac{m_e^*}{m_0} \\right) \\left( \\frac{1}{\\varepsilon_r^2} \\right) E_{H} = \\left( \\frac{m_e^*}{m_0} \\right) \\frac{13.6\\text{ eV}}{\\varepsilon_r^2}
\\]
For silicon ($\varepsilon_r = 11.7$, $m_e^* \\approx 0.26 m_0$):
\\[
E_d = (0.26) \\frac{13.6\\text{ eV}}{(11.7)^2} = \\frac{3.536}{136.89} = 0.0258\\text{ eV} \\approx 26\\text{ meV}
\\]
Because $E_d \\sim k_B T_{\\text{room}} = 25.9\\text{ meV}$, virtually $100\\%$ of donors are ionized at room temperature.

2. **Donor Bohr Radius ($a_d$)**:
\\[
a_d = \\left( \\frac{\\varepsilon_r}{m_e^*/m_0} \\right) a_0 = \\left( \\frac{11.7}{0.26} \\right) (0.529\\text{ Å}) = 45 \\times 0.529\\text{ Å} \\approx 24\\text{ Å}
\\]
The electron wavepacket spans dozens of silicon unit cells, justifying the macroscopic dielectric continuum approximation.

### Impurity Compensation
When both donors ($N_d$) and acceptors ($N_a$) are present simultaneously in the same semiconductor crystal:
- If $N_d > N_a$, electrons from the donors fill all the acceptor states ($N_a^-$), leaving $N_d - N_a$ active net donors (**compensated $n$-type**):
\\[
n \\approx N_d - N_a
\\]
- The Fermi level is pinned closer to midgap, and ionized impurity scattering increases, reducing carrier mobility."""
            },
            {
                "secNumber": "9.7",
                "title": "Semiconductor Transport Mechanics: Drift Mobility & The Einstein Relation",
                "content": r"""The macroscopic movement of charge carriers in semiconductors is governed by two complementary transport mechanisms: **drift** (driven by electric fields) and **diffusion** (driven by concentration gradients).

### Drift Transport and Carrier Mobility
Under an applied electric field $\\mathbf{E}$, electrons and holes experience electrostatic forces and drift with average velocities:
\\[
\\mathbf{v}_{d, e} = -\\mu_e \\mathbf{E}, \\quad \\mathbf{v}_{d, h} = +\\mu_h \\mathbf{E}
\\]
where $\\mu_e$ and $\\mu_h$ are the electron and hole **drift mobilities**, related to the momentum relaxation time $\\tau$ by:
\\[
\\mu = \\frac{e \\tau}{m^*}
\\]
Total drift current density is:
\\[
\\mathbf{J}_{\\text{drift}} = (n e \\mu_e + p e \\mu_h) \\mathbf{E} = \\sigma \\mathbf{E}
\\]
Mobility is limited by two primary microscopic scattering mechanisms (Matthiessen's rule, $1/\\mu = 1/\\mu_{\\text{phonon}} + 1/\\mu_{\\text{impurity}}$):
1. **Acoustic Phonon Scattering**: Increases with temperature ($T$) as lattice vibrations increase: $\\mu_{\\text{ph}} \\propto T^{-3/2}$.
2. **Ionized Impurity Scattering (Brooks-Herring)**: High-velocity carriers at high $T$ spend less time near charged ions: $\\mu_{\\text{imp}} \\propto T^{+3/2} / N_I$.

### Diffusion Transport and The Einstein Relation
When a spatial concentration gradient exists, random Brownian thermal motion produces a net diffusion current density (Fick's first law):
\\[
\\mathbf{J}_{\\text{diff}} = +e D_n \\nabla n - e D_p \\nabla p
\\]
where $D_n$ and $D_p$ are diffusion coefficients.
In thermodynamic equilibrium under an internal built-in electric field (such as inside a $p-n$ junction), the drift and diffusion current densities must cancel exactly:
\\[
J_{n} = n e \\mu_n E + e D_n \\frac{dn}{dx} = 0
\\]
Using the Maxwell-Boltzmann distribution $n(x) = n_0 e^{-e V(x)/k_B T}$ where $E = -dV/dx$:
\\[
\\frac{dn}{dx} = n(x) \\left( \\frac{e}{k_B T} \\right) E
\\]
Substituting into the equilibrium current condition yields the **Einstein relation**:
\\[
\\frac{D_n}{\\mu_n} = \\frac{k_B T}{e}, \\quad \\frac{D_p}{\\mu_p} = \\frac{k_B T}{e}
\\]
At room temperature ($300\\text{ K}$), the thermal voltage is $k_B T / e = 0.02585\\text{ V} \\approx 26\\text{ mV}$."""
            },
            {
                "secNumber": "9.8",
                "title": "The Hall Effect: Carrier Concentration, Hall Coefficient & Mobility",
                "content": r"""Edwin Hall (1879) discovered that when a magnetic field is applied perpendicular to a current-carrying conductor, a transverse electric field develops across the material. This provides the standard method to determine carrier sign, density, and mobility.

### Derivation of the Hall Voltage
Consider a rectangular semiconductor bar of thickness $t$, width $w$, and length $L$.
- A direct current $I_x$ flows along the $+x$-direction (current density $J_x = I_x / (w t)$).
- A uniform magnetic field $B_z$ is applied along the $+z$-direction.
- Moving charge carriers with drift velocity $v_x$ experience the Lorentz force:
\\[
\\mathbf{F}_L = q (\\mathbf{E} + \\mathbf{v} \\times \\mathbf{B})
\\]
- Along the transverse $y$-direction, the magnetic force $F_y = -q v_x B_z$ deflects carriers toward one edge until an opposing transverse electrostatic field (**Hall field** $E_H$) builds up to balance it:
\\[
q E_y + q v_x B_z = 0 \\implies E_H = -v_x B_z
\\]
Since $J_x = n q v_x \\implies v_x = \\frac{J_x}{n q}$:
\\[
E_H = -\\frac{J_x B_z}{n q}
\\]

### The Hall Coefficient ($R_H$)
The **Hall coefficient** $R_H$ is defined as:
\\[
R_H = \\frac{E_y}{J_x B_z} = \\frac{1}{n q} = \\begin{cases} -\\frac{1}{n e} & (n\\text{-type, electrons}) \\\\ +\\frac{1}{p e} & (p\\text{-type, holes}) \\end{cases}
\\]
- **Sign of Carriers**: The polarity of the measured transverse Hall voltage $V_H = E_H w$ directly establishes whether conduction is dominated by electrons ($V_H < 0$) or holes ($V_H > 0$).
- Expressing in terms of measurable experimental quantities ($J_x = I_x / (wt)$):
\\[
V_H = E_H w = R_H \\frac{I_x B_z}{w t} w = \\frac{R_H I_x B_z}{t} \\implies R_H = \\frac{V_H t}{I_x B_z}
\\]

### Hall Mobility ($\\mu_H$)
Combining the Hall coefficient with the longitudinal electrical conductivity $\\sigma = n e \\mu$:
\\[
\\mu_H = |R_H| \\sigma
\\]
This allows direct decoupled determination of both carrier concentration ($n = 1/(e |R_H|)$) and carrier mobility without requiring assumptions about effective mass or relaxation times."""
            }
        ],
        "problems": [
            {
                "probNumber": "9.1",
                "title": "Elastic Strain Energy per Unit Length of Dislocation in Copper",
                "difficulty": "Foundational",
                "statement": "In face-centered cubic copper, the shear modulus is $G = 48.0\\text{ GPa}$, Poisson's ratio is $\\nu = 0.34$, and the lattice constant is $a = 3.615\\text{ Å}$.\\n(a) Determine the magnitude of the Burgers vector for a full $\\frac{a}{2}\\langle 110 \\rangle$ dislocation.\\n(b) Calculate the elastic strain energy per unit length (in $\\text{J/m}$ and $\\text{eV/Å}$) for a pure screw dislocation and a pure edge dislocation (using core radius $r_0 = b$ and outer cutoff radius $R = 1.0\\text{ }\\mu\\text{m}$).\\n(c) For a typical cold-worked copper with dislocation density $\\rho = 1.0 \\times 10^{11}\\text{ cm}^{-2}$, compute the total stored elastic energy in $\\text{J/mol}$.",
                "solution": r"""### Step 1: Magnitude of the Burgers Vector
In FCC copper, the primary slip direction is along $\\langle 110 \\rangle$ with Burgers vector:
\\[
\\mathbf{b} = \\frac{a}{2}\\langle 110 \\rangle
\\]
Magnitude:
\\[
b = |\\mathbf{b}| = \\frac{a}{2}\\sqrt{1^2 + 1^2 + 0^2} = \\frac{a}{\\sqrt{2}} = \\frac{3.615\\text{ Å}}{\\sqrt{2}} = 2.556\\text{ Å} = 2.556 \\times 10^{-10}\\text{ m}
\\]

### Step 2: Strain Energy per Unit Length
Cutoff ratio:
\\[
\\frac{R}{r_0} = \\frac{1.0 \\times 10^{-6}\\text{ m}}{2.556 \\times 10^{-10}\\text{ m}} = 3912.4
\\]
\\[
\\ln\\left(\\frac{R}{r_0}\\right) = \\ln(3912.4) = 8.2719
\\]
Prefactor:
\\[
\\frac{G b^2}{4\\pi} = \\frac{(48.0 \\times 10^9\\text{ Pa})(2.556 \\times 10^{-10}\\text{ m})^2}{4\\pi} = \\frac{(48.0 \\times 10^9)(6.533 \\times 10^{-20})}{12.5664} = 2.4955 \\times 10^{-10}\\text{ J/m}
\\]

1. **Screw Dislocation**:
\\[
E_{\\text{screw}} = \\frac{G b^2}{4\\pi} \\ln\\left(\\frac{R}{r_0}\\right) = (2.4955 \\times 10^{-10}\\text{ J/m})(8.2719) = 2.064 \\times 10^{-9}\\text{ J/m}
\\]
Converting to $\\text{eV/Å}$ ($1\\text{ J/m} = \\frac{1}{1.60218 \\times 10^{-19}} \\times 10^{-10}\\text{ eV/Å} = 0.62415\\text{ eV/Å}$):
\\[
E_{\\text{screw}} = 2.064 \\times 10^{-9} \\times 0.62415 \\times 10^9 = 1.288\\text{ eV/Å}
\\]

2. **Edge Dislocation**:
\\[
E_{\\text{edge}} = \\frac{E_{\\text{screw}}}{1 - \\nu} = \\frac{2.064 \\times 10^{-9}\\text{ J/m}}{1 - 0.34} = \\frac{2.064 \\times 10^{-9}}{0.66} = 3.127 \\times 10^{-9}\\text{ J/m} = 1.952\\text{ eV/Å}
\\]

### Step 3: Stored Elastic Energy in Cold-Worked Copper
Average dislocation energy:
\\[
\\bar{E} = \\frac{E_{\\text{screw}} + E_{\\text{edge}}}{2} = \\frac{2.064 + 3.127}{2} \\times 10^{-9} = 2.596 \\times 10^{-9}\\text{ J/m}
\\]
Dislocation density:
\\[
\\rho = 1.0 \\times 10^{11}\\text{ cm}^{-2} = 1.0 \\times 10^{15}\\text{ m/m}^3
\\]
Stored volumetric energy:
\\[
U_{\\text{vol}} = \\rho \\bar{E} = (1.0 \\times 10^{15}\\text{ m}^{-2})(2.596 \\times 10^{-9}\\text{ J/m}) = 2.596 \\times 10^6\\text{ J/m}^3
\\]
Molar volume of copper ($M = 63.546\\text{ g/mol}, \\rho_m = 8.96\\text{ g/cm}^3$):
\\[
V_m = \\frac{63.546\\text{ g/mol}}{8.96\\text{ g/cm}^3} = 7.092\\text{ cm}^3/\\text{mol} = 7.092 \\times 10^{-6}\\text{ m}^3/\\text{mol}
\\]
Molar stored energy:
\\[
U_{\\text{molar}} = U_{\\text{vol}} V_m = (2.596 \\times 10^6\\text{ J/m}^3)(7.092 \\times 10^{-6}\\text{ m}^3/\\text{mol}) = 18.41\\text{ J/mol}
\\]
This stored energy drives recrystallization during annealing."""
            },
            {
                "probNumber": "9.2",
                "title": "Critical Resolved Shear Stress and Schmid Factor Analysis for Single-Crystal FCC",
                "difficulty": "Intermediate",
                "statement": "A single crystal of aluminum (FCC) with tensile axis oriented along $[123]$ is pulled in tension until plastic yield occurs at applied tensile stress $\\sigma_y = 3.25\\text{ MPa}$.\\n(a) Identify the primary slip system $(hkl)[uvw]$ by determining the maximum Schmid factor $m = \\cos\\phi\\cos\\lambda$ among the $12$ possible $\{111\}\langle 110 \rangle$ slip systems.\\n(b) Compute the numerical value of the maximum Schmid factor $m_{\\max}$.\\n(c) Calculate the critical resolved shear stress $\\tau_{\\text{CRSS}}$ of pure aluminum.",
                "solution": r"""### Step 1: Direction Cosines and Schmid Factor Formulation
The tensile loading axis is $\\mathbf{t} = [1, 2, 3]$ with norm:
\\[
|\\mathbf{t}| = \\sqrt{1^2 + 2^2 + 3^2} = \\sqrt{14}
\\]
Slip occurs on $\{111\}$ planes along $\\langle 1\\bar{1}0 \\rangle$ directions.
The Schmid factor is:
\\[
m = \\cos\\phi \\cos\\lambda = \\frac{\\mathbf{n} \\cdot \\mathbf{t}}{|\\mathbf{n}||\\mathbf{t}|} \\frac{\\mathbf{d} \\cdot \\mathbf{t}}{|\\mathbf{d}||\\mathbf{t}|}
\\]
where $|\\mathbf{n}| = \\sqrt{3}$ (for plane $(hkl)$) and $|\\mathbf{d}| = \\sqrt{2}$ (for direction $[uvw]$).
Thus:
\\[
m = \\frac{|(h + 2k + 3l)(u + 2v + 3w)|}{\\sqrt{3}\\sqrt{14}\\sqrt{2}\\sqrt{14}} = \\frac{|(h + 2k + 3l)(u + 2v + 3w)|}{14\\sqrt{6}}
\\]

### Step 2: Evaluation of Candidate Slip Systems
1. **Slip Plane Selection**:
   Evaluate $\\mathbf{n} \\cdot \\mathbf{t} = h + 2k + 3l$ for the four $\{111\}$ planes:
   - $(111)$: $1(1) + 1(2) + 1(3) = 6$
   - $(11\\bar{1})$: $1(1) + 1(2) - 1(3) = 0$
   - $(1\\bar{1}1)$: $1(1) - 1(2) + 1(3) = 2$
   - $(\\bar{1}11)$: $-1(1) + 1(2) + 1(3) = 4$
   The $(111)$ plane has the largest dot product ($6$), and $(\\bar{1}11)$ has $4$.

2. **Slip Direction Selection on $(111)$**:
   The three allowed slip directions in $(111)$ (satisfying $\\mathbf{n} \\cdot \\mathbf{d} = 0$) are:
   - $[1\\bar{1}0]$: $\\mathbf{d} \\cdot \\mathbf{t} = 1(1) - 1(2) + 0(3) = -1 \\implies |\\mathbf{d} \\cdot \\mathbf{t}| = 1$.
   - $[01\\bar{1}]$: $\\mathbf{d} \\cdot \\mathbf{t} = 0(1) + 1(2) - 1(3) = -1 \\implies |\\mathbf{d} \\cdot \\mathbf{t}| = 1$.
   - $[10\\bar{1}]$: $\\mathbf{d} \\cdot \\mathbf{t} = 1(1) + 0(2) - 1(3) = -2 \\implies |\\mathbf{d} \\cdot \\mathbf{t}| = 2$.
   Product for $(111)[10\\bar{1}]$:
   \\[
   |(\\mathbf{n} \\cdot \\mathbf{t})(\\mathbf{d} \\cdot \\mathbf{t})| = 6 \\times 2 = 12
   \\]

3. **Check $(\\bar{1}11)$ Plane**:
   Directions in $(\\bar{1}11)$:
   - $[110]$: $\\mathbf{d} \\cdot \\mathbf{t} = 1 + 2 = 3 \\implies 4 \\times 3 = 12$.
   - $[101]$: $\\mathbf{d} \\cdot \\mathbf{t} = 1 + 3 = 4 \\implies 4 \\times 4 = 16$.
   Product for $(\\bar{1}11)[101]$:
   \\[
   |(\\mathbf{n} \\cdot \\mathbf{t})(\\mathbf{d} \\cdot \\mathbf{t})| = 4 \\times 4 = 16
   \\]
   Notice that $16 > 12$!

Evaluate Schmid factor for $(\\bar{1}11)[101]$:
\\[
m_{\\max} = \\frac{16}{14\\sqrt{6}} = \\frac{16}{14 \\times 2.44949} = \\frac{16}{34.293} = 0.46656 \\approx 0.467
\\]

### Step 3: Critical Resolved Shear Stress
Using Schmid's Law:
\\[
\\tau_{\\text{CRSS}} = m_{\\max} \\sigma_y = (0.4666)(3.25\\text{ MPa}) = 1.516\\text{ MPa}
\\]
The intrinsic critical resolved shear stress of single-crystal aluminum is approximately $1.52\\text{ MPa}$."""
            },
            {
                "probNumber": "9.3",
                "title": "Peierls-Nabarro Stress Calculation as a Function of Core Width",
                "difficulty": "Intermediate",
                "statement": "The Peierls-Nabarro stress is given by $\\tau_{\\text{PN}} = \\frac{2G}{1-\\nu} \\exp\\left(-\\frac{2\\pi d}{(1-\\nu)b}\\right)$.\\n(a) For copper (FCC, $\\nu = 0.34$), slip occurs on $\{111\}$ with $d_{111} = a/\\sqrt{3}$ and $b = a/\\sqrt{2}$. Compute the core width parameter $\\xi = \\frac{d}{(1-\\nu)b}$ and the ratio $\\tau_{\\text{PN}}/G$.\\n(b) For covalent silicon (diamond cubic, $\\nu = 0.22$), slip on $\{111\}$ has $d = a/\\sqrt{3} = 3.135\\text{ Å}$ and $b = a/\\sqrt{2} = 3.840\\text{ Å}$, but directional covalent bonding restricts core relaxation, resulting in an effective core width parameter $\\xi = 0.60$. Compute $\\tau_{\\text{PN}}/G$.\\n(c) Explain why copper is ductile at room temperature while silicon is brittle.",
                "solution": r"""### Step 1: Calculations for Copper
For FCC copper:
- $d = \\frac{a}{\\sqrt{3}}$
- $b = \\frac{a}{\\sqrt{2}}$
The ratio $d/b$ is:
\\[
\\frac{d}{b} = \\frac{a/\\sqrt{3}}{a/\\sqrt{2}} = \\sqrt{\\frac{2}{3}} = 0.8165
\\]
With $\\nu = 0.34$:
\\[
\\xi = \\frac{d}{(1 - \\nu)b} = \\frac{0.8165}{1 - 0.34} = \\frac{0.8165}{0.66} = 1.2371
\\]
Exponent:
\\[
2\\pi \\xi = 2\\pi (1.2371) = 7.773
\\]
\\[
\\exp(-7.773) = 4.209 \\times 10^{-4}
\\]
Prefactor:
\\[
\\frac{2}{1 - \\nu} = \\frac{2}{0.66} = 3.030
\\]
Peierls stress ratio:
\\[
\\frac{\\tau_{\\text{PN}}}{G} = 3.030 \\times (4.209 \\times 10^{-4}) = 1.275 \\times 10^{-3}
\\]
(Accounting for Shockley partial dissociation expands core width further to $w/b \\approx 2.5$, reducing $\\tau_{\\text{PN}}/G$ to $\\sim 10^{-5}$).

### Step 2: Calculations for Silicon
For covalent silicon with $\\xi = 0.60$ and $\\nu = 0.22$:
Prefactor:
\\[
\\frac{2}{1 - \\nu} = \\frac{2}{0.78} = 2.564
\\]
Exponent:
\\[
2\\pi \\xi = 2\\pi (0.60) = 3.770
\\]
\\[
\\exp(-3.770) = 0.02305
\\]
Peierls stress ratio:
\\[
\\frac{\\tau_{\\text{PN}}}{G} = 2.564 \\times 0.02305 = 0.0591 \\approx 5.91 \\times 10^{-2}
\\]

### Step 3: Mechanical Ductility vs Brittleness
Comparison of Peierls barriers:
\\[
\\frac{(\\tau_{\\text{PN}}/G)_{\\text{Si}}}{(\\tau_{\\text{PN}}/G)_{\\text{Cu}}} = \\frac{5.91 \\times 10^{-2}}{1.28 \\times 10^{-3}} \\approx 46
\\]
In silicon, the lattice friction stress is nearly $6\\%$ of the shear modulus (several $\\text{GPa}$), which exceeds the Griffith fracture stress for crack propagation. Consequently, uncracked silicon cleaves via brittle fracture at room temperature before dislocations can move. In copper, $\\tau_{\\text{PN}}$ is minuscule ($< 1\\text{ MPa}$), allowing dislocations to glide effortlessly under minimal applied loads, imparting extraordinary ductility."""
            },
            {
                "probNumber": "9.4",
                "title": "Frank-Read Source Critical Activation Stress and Dislocation Loop Generation",
                "difficulty": "Intermediate",
                "statement": "A Frank-Read dislocation source in iron ($G = 80.0\\text{ GPa}$, $b = 2.48\\text{ Å}$) consists of a pinned dislocation line segment of length $L = 0.50\\text{ }\\mu\\text{m}$.\\n(a) Derive the relationship between applied shear stress $\\tau$ and the radius of curvature $R$ of the bowed segment using line tension $T = \\frac{1}{2} G b^2$.\\n(b) Compute the critical activation stress $\\tau_{\\text{crit}}$ required to initiate continuous operation of the source.\\n(c) If work hardening increases the forest dislocation density, reducing the average pinning length to $L' = 0.050\\text{ }\\mu\\text{m}$, compute the new yield strength contribution $\\Delta \\tau$.",
                "solution": r"""### Step 1: Force Balance on Bowed Dislocation
The mechanical Peach-Koehler force per unit length pushing the dislocation outward is:
\\[
f_{\\text{PK}} = \\tau b
\\]
This force is balanced by the restoring force from the dislocation line tension $T$.
For an arc of radius of curvature $R$, the inward restoring force per unit length is:
\\[
f_{\\text{tension}} = \\frac{T}{R}
\\]
Equating forces:
\\[
\\tau b = \\frac{T}{R} \\implies R = \\frac{T}{\\tau b}
\\]
Using $T = \\frac{1}{2} G b^2$:
\\[
R = \\frac{\\frac{1}{2} G b^2}{\\tau b} = \\frac{G b}{2 \\tau}
\\]

### Step 2: Critical Activation Stress
As applied stress $\\tau$ increases, the radius of curvature $R$ decreases.
The maximum resistance occurs when the bowed segment forms a perfect semicircle, at which point the radius reaches its minimum value:
\\[
R_{\\min} = \\frac{L}{2}
\\]
Substituting $R_{\\min} = L/2$ gives the critical activation stress:
\\[
\\frac{L}{2} = \\frac{G b}{2 \\tau_{\\text{crit}}} \\implies \\tau_{\\text{crit}} = \\frac{G b}{L}
\\]
Numerical evaluation for $L = 0.50\\text{ }\\mu\\text{m} = 5.0 \\times 10^{-7}\\text{ m}$:
\\[
\\tau_{\\text{crit}} = \\frac{(80.0 \\times 10^9\\text{ Pa})(2.48 \\times 10^{-10}\\text{ m})}{5.0 \\times 10^{-7}\\text{ m}} = \\frac{19.84}{5.0 \\times 10^{-7}} = 3.968 \\times 10^7\\text{ Pa} = 39.7\\text{ MPa}
\\]

### Step 3: Hardened State ($L' = 0.050\\text{ }\\mu\\text{m}$)
When pinning spacing decreases by a factor of 10 to $L' = 5.0 \\times 10^{-8}\\text{ m}$:
\\[
\\tau_{\\text{crit}}' = \\frac{(80.0 \\times 10^9)(2.48 \\times 10^{-10})}{5.0 \\times 10^{-8}\\text{ m}} = 396.8\\text{ MPa}
\\]
Stress increase:
\\[
\\Delta \\tau = 396.8 - 39.7 = 357.1\\text{ MPa}
\\]
This demonstrates the microscopic mechanism of Taylor work hardening (where $\\tau_y \\propto G b \\sqrt{\\rho}$)."""
            },
            {
                "probNumber": "9.5",
                "title": "Grain Boundary Energy and Read-Shockley Low-Angle Tilt Boundary Analysis",
                "difficulty": "Intermediate",
                "statement": "A symmetrical low-angle tilt boundary in nickel ($G = 76.0\\text{ GPa}$, $\\nu = 0.31$, $b = 2.49\\text{ Å}$) has misorientation angle $\\theta = 2.00^\\circ$.\\n(a) Compute the spacing $D$ between adjacent edge dislocations in the boundary.\\n(b) Using the Read-Shockley relation $\\gamma(\\theta) = E_0 \\theta (A - \\ln\\theta)$ with $E_0 = \\frac{G b}{4\\pi(1-\\nu)}$ and core parameter $A = 0.25$, calculate the grain boundary interfacial energy $\\gamma$ in $\\text{J/m}^2$.\\n(c) Find the misorientation angle $\\theta_m$ at which the Read-Shockley energy reaches its theoretical maximum.",
                "solution": r"""### Step 1: Dislocation Spacing
Convert misorientation angle to radians:
\\[
\\theta = 2.00^\\circ = 2.00 \\times \\frac{\\pi}{180} = 0.034907\\text{ rad}
\\]
Dislocation spacing:
\\[
D = \\frac{b}{\\theta} = \\frac{2.49 \\times 10^{-10}\\text{ m}}{0.034907\\text{ rad}} = 7.133 \\times 10^{-9}\\text{ m} = 71.3\\text{ Å} = 7.13\\text{ nm}
\\]

### Step 2: Read-Shockley Boundary Energy
Calculate prefactor $E_0$:
\\[
E_0 = \\frac{G b}{4\\pi(1-\\nu)} = \\frac{(76.0 \\times 10^9\\text{ Pa})(2.49 \\times 10^{-10}\\text{ m})}{4\\pi(1 - 0.31)} = \\frac{18.924}{4\\pi(0.69)} = \\frac{18.924}{8.6708} = 2.1825\\text{ J/m}^2
\\]
Logarithmic term:
\\[
\\ln\\theta = \\ln(0.034907) = -3.3550
\\]
\\[
A - \\ln\\theta = 0.25 - (-3.3550) = 0.25 + 3.3550 = 3.6050
\\]
Interfacial energy:
\\[
\\gamma = E_0 \\theta (A - \\ln\\theta) = (2.1825\\text{ J/m}^2)(0.034907)(3.6050) = 0.2746\\text{ J/m}^2 = 275\\text{ mJ/m}^2
\\]

### Step 3: Maximum Energy Misorientation Angle
To find the maximum of $\\gamma(\\theta)$:
\\[
\\frac{d\\gamma}{d\\theta} = E_0 (A - \\ln\\theta) + E_0 \\theta \\left(-\\frac{1}{\\theta}\\right) = E_0 (A - \\ln\\theta - 1) = 0
\\]
\\[
A - 1 - \\ln\\theta_m = 0 \\implies \\ln\\theta_m = A - 1
\\]
\\[
\\theta_m = \\exp(A - 1) = \\exp(0.25 - 1.0) = \\exp(-0.75) = 0.4724\\text{ rad} = 27.06^\\circ
\\]
*(Note: At $\\theta > 15^\circ$, dislocation cores overlap and the continuum Read-Shockley model breaks down, transitioning into the constant energy plateau of high-angle boundaries).*"""
            },
            {
                "probNumber": "9.6",
                "title": "Hydrogenic Bohr Model of Donor Binding Energy and Orbital Radius",
                "difficulty": "Foundational",
                "statement": "In germanium, the relative dielectric constant is $\\varepsilon_r = 16.0$ and the conduction-band electron effective mass is $m_e^* = 0.12 m_0$.\\n(a) Using the hydrogenic model, compute the donor ionization energy $E_d$ in $\\text{meV}$.\\n(b) Compute the effective Bohr radius $a_d$ of the donor state in $\\text{Å}$.\\n(c) Using the Mott transition criterion $n_c^{1/3} a_d \\approx 0.26$, compute the critical donor density $n_c$ (Mott density) above which impurity states merge into the conduction band, causing a semiconductor-to-metal transition.",
                "solution": r"""### Step 1: Donor Ionization Energy
The hydrogenic formula is:
\\[
E_d = \\left(\\frac{m_e^*}{m_0}\\right) \\frac{E_H}{\\varepsilon_r^2}
\\]
where $E_H = 13.606\\text{ eV}$.
Substitute $m_e^*/m_0 = 0.12$ and $\\varepsilon_r = 16.0$:
\\[
\\varepsilon_r^2 = (16.0)^2 = 256
\\]
\\[
E_d = (0.12) \\frac{13.606\\text{ eV}}{256} = \\frac{1.6327}{256} = 0.006378\\text{ eV} = 6.38\\text{ meV}
\\]
In germanium, donor binding energy is only $6.4\\text{ meV}$, ensuring complete ionization even down to cryogenic temperatures ($T \\sim 30\\text{ K}$).

### Step 2: Donor Bohr Radius
The effective Bohr radius is:
\\[
a_d = \\varepsilon_r \\left(\\frac{m_0}{m_e^*}\\right) a_0
\\]
where $a_0 = 0.52918\\text{ Å}$.
\\[
a_d = (16.0) \\left(\\frac{1}{0.12}\\right) (0.52918\\text{ Å}) = (133.33)(0.52918\\text{ Å}) = 70.56\\text{ Å} = 7.06\\text{ nm}
\\]
The donor electron wavefunction is gigantic, encompassing thousands of germanium unit cells!

### Step 3: Mott Semiconductor-to-Metal Transition
According to Sir Nevill Mott's criterion:
\\[
n_c^{1/3} a_d \\approx 0.26 \\implies n_c^{1/3} = \\frac{0.26}{a_d}
\\]
With $a_d = 70.56 \\times 10^{-8}\\text{ cm}$:
\\[
n_c^{1/3} = \\frac{0.26}{7.056 \\times 10^{-7}\\text{ cm}} = 3.685 \\times 10^5\\text{ cm}^{-1}
\\]
Cubing both sides:
\\[
n_c = (3.685 \\times 10^5)^3 = 5.00 \\times 10^{16}\\text{ cm}^{-3}
\\]
Above $N_d = 5.0 \\times 10^{16}\\text{ cm}^{-3}$, donor wavefunctions overlap sufficiently to form an impurity band that merges into the conduction band, turning doped germanium into a degenerate metallic conductor."""
            },
            {
                "probNumber": "9.7",
                "title": "Hall Effect Measurement: Carrier Type, Density, and Drift Mobility",
                "difficulty": "Intermediate",
                "statement": "A rectangular semiconductor slice of thickness $t = 0.50\\text{ mm}$, width $w = 4.0\\text{ mm}$, and length $L = 12.0\\text{ mm}$ carries a current of $I_x = 5.0\\text{ mA}$. A magnetic field of $B_z = 0.60\\text{ T}$ is applied normal to the broad face.\\n- Measured longitudinal voltage along $L$: $V_x = 1.80\\text{ V}$.\\n- Measured transverse Hall voltage: $V_H = -15.0\\text{ mV}$.\\n(a) Identify the majority carrier type and compute the Hall coefficient $R_H$.\\n(b) Calculate the majority carrier density $n$ in $\\text{cm}^{-3}$.\\n(c) Determine the electrical conductivity $\\sigma$ and the drift mobility $\\mu_H$ in $\\text{cm}^2/(\\text{V}\\cdot\\text{s})$.",
                "solution": r"""### Step 1: Carrier Type and Hall Coefficient
The measured Hall voltage is negative ($V_H = -15.0\\text{ mV} < 0$).
This definitively establishes that the majority charge carriers are **electrons** ($n$-type semiconductor).
The Hall coefficient is:
\\[
R_H = \\frac{V_H t}{I_x B_z}
\\]
Given:
- $V_H = -15.0 \\times 10^{-3}\\text{ V}$
- $t = 0.50 \\times 10^{-3}\\text{ m}$
- $I_x = 5.0 \\times 10^{-3}\\text{ A}$
- $B_z = 0.60\\text{ T}$

\\[
R_H = \\frac{(-15.0 \\times 10^{-3}\\text{ V})(0.50 \\times 10^{-3}\\text{ m})}{(5.0 \\times 10^{-3}\\text{ A})(0.60\\text{ T})} = \\frac{-7.50 \\times 10^{-6}}{3.00 \\times 10^{-3}} = -2.50 \\times 10^{-3}\\text{ m}^3/\\text{C}
\\]
In $\\text{cm}^3/\\text{C}$:
\\[
R_H = -2.50 \\times 10^{-3} \\times 10^6 = -2500\\text{ cm}^3/\\text{C}
\\]

### Step 2: Majority Carrier Concentration
Carrier concentration:
\\[
n = \\frac{1}{e |R_H|} = \\frac{1}{(1.60218 \\times 10^{-19}\\text{ C})(2.50 \\times 10^{-3}\\text{ m}^3/\\text{C})} = \\frac{1}{4.0055 \\times 10^{-22}} = 2.497 \\times 10^{21}\\text{ m}^{-3} = 2.50 \\times 10^{15}\\text{ cm}^{-3}
\\]

### Step 3: Conductivity and Mobility
Resistance:
\\[
R = \\frac{V_x}{I_x} = \\frac{1.80\\text{ V}}{5.0 \\times 10^{-3}\\text{ A}} = 360\\text{ }\\Omega
\\]
Cross-sectional area:
\\[
A = w t = (4.0 \\times 10^{-3}\\text{ m})(0.50 \\times 10^{-3}\\text{ m}) = 2.0 \\times 10^{-6}\\text{ m}^2 = 0.020\\text{ cm}^2
\\]
Conductivity:
\\[
\\sigma = \\frac{L}{R A} = \\frac{12.0 \\times 10^{-3}\\text{ m}}{(360\\text{ }\\Omega)(2.0 \\times 10^{-6}\\text{ m}^2)} = \\frac{1.20 \\times 10^{-2}}{7.20 \\times 10^{-4}} = 16.67\\text{ S/m} = 0.1667\\text{ S/cm}
\\]
Hall drift mobility:
\\[
\\mu_H = |R_H| \\sigma = (2.50 \\times 10^{-3}\\text{ m}^3/\\text{C})(16.67\\text{ S/m}) = 0.04167\\text{ m}^2/(\\text{V}\\cdot\\text{s}) = 416.7\\text{ cm}^2/(\\text{V}\\cdot\\text{s})
\\]"""
            },
            {
                "probNumber": "9.8",
                "title": "Thermoelectric Seebeck Coefficient and Figure of Merit in Bismuth Telluride",
                "difficulty": "Advanced",
                "statement": "An engineered $p$-type bismuth telluride ($\\text{Bi}_2\\text{Te}_3$) thermoelectric alloy at $T = 300\\text{ K}$ has Seebeck coefficient $S = +220.0\\text{ }\\mu\\text{V/K}$, electrical conductivity $\\sigma = 1.05 \\times 10^5\\text{ S/m}$, and total thermal conductivity $\\kappa = 1.45\\text{ W/(m}\\cdot\\text{K)}$.\\n(a) Compute the thermoelectric power factor $\\text{PF} = S^2 \\sigma$ in $\\text{mW/(m}\\cdot\\text{K}^2\\text{)}$.\\n(b) Compute the dimensionless thermoelectric figure of merit $zT$ at $300\\text{ K}$.\\n(c) Using the Wiedemann-Franz law with Lorenz number $L_0 = 2.44 \\times 10^{-8}\\text{ W}\\cdot\\Omega/\\text{K}^2$, separate $\\kappa$ into electronic ($\\kappa_e$) and lattice ($\\kappa_L$) contributions.",
                "solution": r"""### Step 1: Thermoelectric Power Factor
Given $S = +220.0\\text{ }\\mu\\text{V/K} = 2.20 \\times 10^{-4}\\text{ V/K}$ and $\\sigma = 1.05 \\times 10^5\\text{ S/m}$:
\\[
S^2 = (2.20 \\times 10^{-4}\\text{ V/K})^2 = 4.84 \\times 10^{-8}\\text{ V}^2/\\text{K}^2
\\]
Power factor:
\\[
\\text{PF} = S^2 \\sigma = (4.84 \\times 10^{-8}\\text{ V}^2/\\text{K}^2)(1.05 \\times 10^5\\text{ S/m}) = 5.082 \\times 10^{-3}\\text{ W/(m}\\cdot\\text{K}^2) = 5.08\\text{ mW/(m}\\cdot\\text{K}^2)
\\]

### Step 2: Dimensionless Figure of Merit $zT$
The thermoelectric figure of merit is:
\\[
zT = \\frac{S^2 \\sigma}{\\kappa} T = \\frac{\\text{PF} \\cdot T}{\\kappa}
\\]
With $\\kappa = 1.45\\text{ W/(m}\\cdot\\text{K)}$ and $T = 300\\text{ K}$:
\\[
zT = \\frac{(5.082 \\times 10^{-3}\\text{ W/(m}\\cdot\\text{K}^2))(300\\text{ K})}{1.45\\text{ W/(m}\\cdot\\text{K)}} = \\frac{1.5246}{1.45} = 1.051
\\]
A $zT \\approx 1.05$ at room temperature represents high-performance commercial thermoelectric cooling material.

### Step 3: Separation of Thermal Conductivity
By the Wiedemann-Franz law:
\\[
\\kappa_e = L_0 \\sigma T = (2.44 \\times 10^{-8}\\text{ W}\\cdot\\Omega/\\text{K}^2)(1.05 \\times 10^5\\text{ S/m})(300\\text{ K}) = 0.7686\\text{ W/(m}\\cdot\\text{K)}
\\]
Lattice thermal conductivity:
\\[
\\kappa_L = \\kappa - \\kappa_e = 1.450 - 0.7686 = 0.6814\\text{ W/(m}\\cdot\\text{K)}
\\]
Electronic transport accounts for $53\\%$ of total heat conduction, and lattice phonons account for $47\\%$. Modern nanostructuring aims to suppress $\\kappa_L$ via grain boundary scattering without degrading $\\sigma$."""
            },
            {
                "probNumber": "9.9",
                "title": "Stacking Fault Energy and Shockley Partial Dissociation in FCC Metals",
                "difficulty": "Advanced",
                "statement": "In an FCC metal, a full dislocation $\\mathbf{b}_1 = \\frac{a}{2}[110]$ dissociates into two Shockley partials $\\mathbf{b}_2 = \\frac{a}{6}[211]$ and $\\mathbf{b}_3 = \\frac{a}{6}[12\\bar{1}]$ bounding an intrinsic stacking fault of energy $\\gamma_{\\text{SFE}}$.\\n(a) Show that the angle between the two partial Burgers vectors is $60^\\circ$.\\n(b) Balancing the repulsive elastic force per unit length $f_{\\text{rep}} = \\frac{G (\\mathbf{b}_2 \\cdot \\mathbf{b}_3)}{2\\pi d} = \\frac{G a^2}{24\\pi d}$ with the stacking fault surface tension $\\gamma_{\\text{SFE}}$, derive the equilibrium ribbon width $d_{\\text{eq}}$.\\n(c) For silver ($a = 4.086\\text{ Å}$, $G = 30.0\\text{ GPa}$, $\\gamma_{\\text{SFE}} = 22.0\\text{ mJ/m}^2$) and aluminum ($a = 4.050\\text{ Å}$, $G = 26.0\\text{ GPa}$, $\\gamma_{\\text{SFE}} = 160.0\\text{ mJ/m}^2$), compute $d_{\\text{eq}}$ and explain why aluminum exhibits extensive cross-slip while silver does not.",
                "solution": r"""### Step 1: Angle Between Shockley Partials
The two partial Burgers vectors are:
\\[
\\mathbf{b}_2 = \\frac{a}{6}(2\\hat{\\mathbf{x}} + \\hat{\\mathbf{y}} + \\hat{\\mathbf{z}}), \\quad \\mathbf{b}_3 = \\frac{a}{6}(\\hat{\\mathbf{x}} + 2\\hat{\\mathbf{y}} - \\hat{\\mathbf{z}})
\\]
Dot product:
\\[
\\mathbf{b}_2 \\cdot \\mathbf{b}_3 = \\left(\\frac{a}{6}\\right)^2 [2(1) + 1(2) + 1(-1)] = \\frac{a^2}{36} (2 + 2 - 1) = \\frac{3a^2}{36} = \\frac{a^2}{12}
\\]
Magnitudes:
\\[
|\\mathbf{b}_2|^2 = \\frac{a^2}{36}(4 + 1 + 1) = \\frac{6a^2}{36} = \\frac{a^2}{6}
\\]
\\[
|\\mathbf{b}_3|^2 = \\frac{a^2}{36}(1 + 4 + 1) = \\frac{6a^2}{36} = \\frac{a^2}{6}
\\]
Cosine of angle:
\\[
\\cos\\theta = \\frac{\\mathbf{b}_2 \\cdot \\mathbf{b}_3}{|\\mathbf{b}_2||\\mathbf{b}_3|} = \\frac{a^2/12}{a^2/6} = \\frac{6}{12} = \\frac{1}{2} \\implies \\theta = 60.0^\\circ
\\]

### Step 2: Equilibrium Ribbon Width Derivation
The repulsive elastic force per unit length between the partials is:
\\[
f_{\\text{rep}} = \\frac{G (\\mathbf{b}_2 \\cdot \\mathbf{b}_3)}{2\\pi d} = \\frac{G (a^2/12)}{2\\pi d} = \\frac{G a^2}{24\\pi d}
\\]
The attractive force per unit length exerted by the stacking fault surface tension is:
\\[
f_{\\text{attr}} = \\gamma_{\\text{SFE}}
\\]
Equating $f_{\\text{rep}} = f_{\\text{attr}}$ at equilibrium:
\\[
\\frac{G a^2}{24\\pi d_{\\text{eq}}} = \\gamma_{\\text{SFE}} \\implies d_{\\text{eq}} = \\frac{G a^2}{24\\pi \\gamma_{\\text{SFE}}}
\\]

### Step 3: Comparison between Silver and Aluminum
1. **For Silver ($\text{Ag}$)**:
   - $a = 4.086 \\times 10^{-10}\\text{ m} \\implies a^2 = 1.6695 \\times 10^{-19}\\text{ m}^2$
   - $G = 30.0 \\times 10^9\\text{ Pa}$
   - $\\gamma_{\\text{SFE}} = 0.0220\\text{ J/m}^2$
   \\[
   G a^2 = (30.0 \\times 10^9)(1.6695 \\times 10^{-19}) = 5.0086 \\times 10^{-9}\\text{ N}\\cdot\\text{m}
   \\]
   \\[
   24\\pi \\gamma_{\\text{SFE}} = 24\\pi (0.0220) = 1.6588\\text{ J/m}^2
   \\]
   \\[
   d_{\\text{eq}}(\\text{Ag}) = \\frac{5.0086 \\times 10^{-9}}{1.6588} = 3.019 \\times 10^{-9}\\text{ m} = 30.2\\text{ Å} = 3.02\\text{ nm}
   \\]

2. **For Aluminum ($\text{Al}$)**:
   - $a = 4.050 \\times 10^{-10}\\text{ m} \\implies a^2 = 1.6403 \\times 10^{-19}\\text{ m}^2$
   - $G = 26.0 \\times 10^9\\text{ Pa}$
   - $\\gamma_{\\text{SFE}} = 0.160\\text{ J/m}^2$
   \\[
   G a^2 = (26.0 \\times 10^9)(1.6403 \\times 10^{-19}) = 4.2647 \\times 10^{-9}\\text{ N}\\cdot\\text{m}
   \\]
   \\[
   24\\pi \\gamma_{\\text{SFE}} = 24\\pi (0.160) = 12.064\\text{ J/m}^2
   \\]
   \\[
   d_{\\text{eq}}(\\text{Al}) = \\frac{4.2647 \\times 10^{-9}}{12.064} = 3.535 \\times 10^{-10}\\text{ m} = 3.54\\text{ Å} = 0.35\\text{ nm}
   \\]

### Physical Implications:
In aluminum, the high stacking fault energy pulls partials so tightly together that $d_{\\text{eq}} \\approx 3.5\\text{ Å} \\approx 1.2 b$. The dislocation behaves essentially as an unextended full dislocation, enabling cross-slip out of the $\{111\}$ plane. In silver, the wide stacking fault ribbon ($30\\text{ Å}$) restricts the dislocation strictly to its primary slip plane, preventing cross-slip and resulting in rapid work hardening."""
            }
        ]
    }
    return u9

if __name__ == '__main__':
    u9 = get_unit_9()
    print("Unit 9 successfully generated:")
    print("Title:", u9["title"])
    print("Sections:", len(u9["sections"]))
    print("Problems:", len(u9["problems"]))
