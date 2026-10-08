#!/usr/bin/env python3
"""
create_inorg1_unit3.py
Generates build_inorg1_unit3.py for Unit 3:
The Chemical Bond I: Ionic Bonding & Crystal Energetics
"""

import sys

content = r'''# -*- coding: utf-8 -*-
"""
Unit 3: The Chemical Bond I: Ionic Bonding & Crystal Energetics
Contains 5 comprehensive sections and 3 tiered solved problems with full derivations.
"""

def get_unit3():
    return {
        "id": "unit3",
        "title": "Unit 3: The Chemical Bond I: Ionic Bonding & Crystal Energetics",
        "simId": "sim_chem_born_haber_lattice_cycle",
        "simTitle": "Born-Haber Cycle & Lattice Energy Engine",
        "sections": [
            {
                "id": "sec3_1",
                "title": "§3.1 Energetics of Ionic Bond Formation & The Born-Haber Cycle",
                "content": r"""### Thermodynamic Foundations of the Ionic Lattice

An ionic bond is conventionally defined as the electrostatic attractive force operating between oppositely charged ions formed via complete or near-complete valence electron transfer from an electropositive element (typically an alkali or alkaline earth metal) to an electronegative nonmetal (typically a halogen or chalcogen). However, the intuitive depiction of an isolated gas-phase cation-anion pair reveals an immediate thermodynamic paradox: the ionization energy required to strip an electron from an alkali metal is substantially greater than the energy released when that electron is captured by a neutral halogen atom.

Consider the formation of an isolated gas-phase ion pair $\text{Na}^+(g) + \text{Cl}^-(g)$ from neutral gas-phase atoms $\text{Na}(g) + \text{Cl}(g)$:
1. First ionization energy of sodium:
   $$\text{Na}(g) \longrightarrow \text{Na}^+(g) + e^-, \quad \Delta H_{\text{IE}_1} = +495.8\text{ kJ}\cdot\text{mol}^{-1}$$
2. Electron affinity enthalpy of chlorine:
   $$\text{Cl}(g) + e^- \longrightarrow \text{Cl}^-(g), \quad \Delta H_{\text{EA}} = -348.6\text{ kJ}\cdot\text{mol}^{-1}$$
3. Net enthalpy for gas-phase ion pair generation:
   $$\Delta H_{\text{pair generation}} = \Delta H_{\text{IE}_1} + \Delta H_{\text{EA}} = +495.8 - 348.6 = +147.2\text{ kJ}\cdot\text{mol}^{-1}$$

The gas-phase ionization process is strictly **endothermic** by $+147.2\text{ kJ}\cdot\text{mol}^{-1}$. Even when Coulombic attraction between an isolated pair at their equilibrium internuclear distance $r_0 \approx 236\text{ pm}$ is accounted for ($\Delta E_{\text{Coulomb}} = -\frac{e^2}{4\pi\varepsilon_0 r_0} \approx -589\text{ kJ}\cdot\text{mol}^{-1}$), yielding an isolated gaseous diatomic molecule $\text{NaCl}(g)$, this represents only a fraction of the macroscopic stabilization observed in the solid state.

The primary thermodynamic driving force governing the formation and exceptional stability of ionic compounds is the **Lattice Energy** ($\Delta H_{\text{lattice}}$ or $U_0$), which represents the immense stabilization attained when an infinite, three-dimensional periodic array of cations and anions coalesces from the gaseous state into a crystalline solid lattice:
$$\text{M}^{z+}(g) + \text{X}^{z-}(g) \longrightarrow \text{MX}(s), \quad \Delta H_{\text{lattice}} < 0$$
*(Note: By IUPAC thermochemical convention, lattice enthalpy $\Delta H_{\text{lattice}}^\circ$ is defined as the enthalpy change for formation from gaseous ions, hence negative, whereas lattice dissociation energy $U_L = -\Delta H_{\text{lattice}}^\circ$ is defined as the energy required to break the crystal into gaseous ions, hence positive. In this text, we clearly state signs and conventions for every derivation).*

---

### The Born-Haber Thermochemical Cycle

Direct experimental measurement of lattice enthalpy cannot be executed in a calorimeter because gaseous ions cannot be quantitatively condensed into a crystal without competing neutral chemical pathways. To overcome this limitation, Max Born and Fritz Haber applied Hess's Law of Constant Heat Summation to formulate the **Born-Haber Cycle**, a closed thermodynamic state-function loop linking standard enthalpy of formation ($\Delta H_f^\circ$) with measurable spectroscopic, thermochemical, and calorimetric parameters.

For a binary crystalline ionic solid $\text{M}_p\text{X}_q(s)$ formed from elements in their standard reference states:
$$p\,\text{M}(s) + \frac{q}{2}\,\text{X}_2(g \text{ or } l \text{ or } s) \xrightarrow{\Delta H_f^\circ} \text{M}_p\text{X}_q(s)$$

The Born-Haber cycle decomposes this overarching transformation into five discrete, measurable fundamental physical steps:

```
                          p M(s) + (q/2) X2(std)
                           /                  \
   p * ΔH_sub             /                    \
                         v                      v  ΔH_f° (Formation)
                  p M(g) + (q/2) X2(std)         \
                         |                        \
   (q/2) * ΔH_diss       |                         \
                         v                          \
                  p M(g) + q X(g)                    \
                         |                            \
   p * Σ IE_i            |                             \
                         v                              \
                 p M^{z+}(g) + q X(g)                    \
                         |                                \
   q * ΔH_EA             |                                 v
                         v                            M_p X_q (s)
                 p M^{z+}(g) + q X^{z-}(g) ----------> (Crystalline Solid)
                                             ΔH_lattice
```

#### Mathematical Formulation of Hess's Law:
$$\Delta H_f^\circ[\text{M}_p\text{X}_q(s)] = p\,\Delta H_{\text{sub}}^\circ[\text{M}] + p\sum_{i=1}^{z_+} \text{IE}_i[\text{M}] + \frac{q}{2}\,\Delta H_{\text{diss}}^\circ[\text{X}_2] + q\sum_{j=1}^{z_-} \Delta H_{\text{EA}_j}[\text{X}] + \Delta H_{\text{lattice}}^\circ[\text{M}_p\text{X}_q(s)]$$

Solving directly for the experimental lattice enthalpy:
$$\Delta H_{\text{lattice}}^\circ = \Delta H_f^\circ[\text{M}_p\text{X}_q(s)] - \left[ p\,\Delta H_{\text{sub}}^\circ[\text{M}] + p\sum_{i=1}^{z_+} \text{IE}_i[\text{M}] + \frac{q}{2}\,\Delta H_{\text{diss}}^\circ[\text{X}_2] + q\sum_{j=1}^{z_-} \Delta H_{\text{EA}_j}[\text{X}] \right]$$

#### Detailed Breakdown of Energy Components for Halides and Oxides:

| Thermodynamic Parameter | Symbol | Sign | Physical Phenomenon & Quantum Origin |
| :--- | :--- | :--- | :--- |
| **Standard Enthalpy of Formation** | $\Delta H_f^\circ$ | Typically $(-)$ large | Calorimetrically measured heat of synthesis from elemental reference states. |
| **Enthalpy of Sublimation / Atomization** | $\Delta H_{\text{sub}}^\circ$ | $(+)$ always | Energy required to disrupt metallic bonding or cohesive lattice of the solid metal. |
| **Ionization Enthalpy** | $\sum \text{IE}_i$ | $(+)$ always | Sum of successive electronic ionization potentials stripping $z_+$ electrons to vacuum. |
| **Bond Dissociation Enthalpy** | $\Delta H_{\text{diss}}^\circ$ | $(+)$ always | Homolytic cleavage enthalpy of the covalent halogen-halogen or chalcogen bond. |
| **Electron Gain Enthalpy** | $\Delta H_{\text{EA}}$ | $(-)$ for 1st, $(+)$ for 2nd | Energy released upon capturing 1st electron; highly endothermic for $\text{O}^{2-}$ or $\text{S}^{2-}$. |
| **Lattice Enthalpy** | $\Delta H_{\text{lattice}}^\circ$ | $(-)$ very large | Cohesive electrostatic stabilization of the 3D periodic infinite crystal lattice. |

#### The Special Case of Oxides: The Second Electron Affinity of Oxygen
A critical insight revealed by the Born-Haber cycle involves divalent anions such as the oxide ion $\text{O}^{2-}$ and sulfide ion $\text{S}^{2-}$. The first electron affinity of atomic oxygen is exothermic:
$$\text{O}(g) + e^- \longrightarrow \text{O}^-(g), \quad \Delta H_{\text{EA}_1} = -141.0\text{ kJ}\cdot\text{mol}^{-1}$$
However, introducing a second electron to the already negatively charged $\text{O}^-(g)$ anion encounters fierce interelectronic Coulombic repulsion:
$$\text{O}^-(g) + e^- \longrightarrow \text{O}^{2-}(g), \quad \Delta H_{\text{EA}_2} = +744.0\text{ kJ}\cdot\text{mol}^{-1}$$
The total electron gain enthalpy for oxide ion formation in the gas phase is:
$$\Delta H_{\text{EA},\text{net}} = \Delta H_{\text{EA}_1} + \Delta H_{\text{EA}_2} = -141.0 + 744.0 = +603.0\text{ kJ}\cdot\text{mol}^{-1}$$
Thus, isolated $\text{O}^{2-}$ ions are thermodynamically unstable and non-existent in the gas phase. Solid oxides such as $\text{MgO}(s)$, $\text{CaO}(s)$, and $\text{Al}_2\text{O}_3(s)$ exist exclusively because the immense lattice energy ($U_0[\text{MgO}] \approx -3791\text{ kJ}\cdot\text{mol}^{-1}$) of the divalent lattice overwhelmingly compensates for the $+603\text{ kJ}\cdot\text{mol}^{-1}$ cost of generating $\text{O}^{2-}(g)$."""
            },
            {
                "id": "sec3_2",
                "title": "§3.2 Electrostatic Models & The Born-Landé Equation",
                "content": r"""### Rigorous Derivation of the Electrostatic Lattice Potential

To establish a predictive theory of ionic cohesion independent of empirical thermochemical cycles, Max Born and Alfred Landé formulated an electrostatic model treating the crystal as an infinite periodic assembly of point charges surrounded by short-range repulsive electron clouds.

#### 1. Coulombic Attractive Potential & The Madelung Constant
Let an ionic crystal contain cations of charge $+z_1 e$ and anions of charge $-z_2 e$ separated by equilibrium shortest internuclear distance $r_0$. Select a reference central ion $i$. The Coulombic potential energy between reference ion $i$ and all other ions $j$ located at distances $r_{ij}$ throughout the infinite lattice is:
$$E_{\text{Coulomb}} = \sum_{j \neq i} \frac{z_i z_j e^2}{4\pi\varepsilon_0 r_{ij}}$$

In any periodic crystal lattice, the distance $r_{ij}$ to the $j$-th ion can be expressed as a geometric multiple of the nearest-neighbor distance $r$:
$$r_{ij} = c_{ij} r, \quad c_{ij} \in \mathbb{R}^+$$
Factoring out the common terms:
$$E_{\text{Coulomb}} = -\frac{z_1 z_2 e^2}{4\pi\varepsilon_0 r} \sum_{j \neq i} \frac{(\pm)_j}{c_{ij}}$$

The infinite summation over all lattice points depends purely on the crystal geometry and coordination geometry, not on the chemical identity of the ions. This dimensionless geometric factor is the **Madelung Constant** ($M$ or $A$):
$$M = \sum_{j \neq i} \frac{(-1)^{s_j}}{c_{ij}}$$
where $(-1)^{s_j} = +1$ for ions of opposite charge (attractive) and $-1$ for ions of identical charge (repulsive).

Thus, the electrostatic attractive potential energy per mole of formula units ($N_A$ ions) is:
$$E_{\text{Coulomb}}(r) = -\frac{N_A M |z_1 z_2| e^2}{4\pi\varepsilon_0 r}$$

#### Madelung Constant Convergence in a One-Dimensional Alternating Chain:
Consider an infinite 1D chain of alternating $+e$ and $-e$ ions separated by interionic distance $r$:
$$\cdots -e \quad +e \quad -e \quad \mathbf{[+e]_0} \quad -e \quad +e \quad -e \cdots$$
For the reference central ion at position $0$:
- 2 nearest neighbors at distance $1r$ with opposite charge: contribution $+2 \cdot \frac{1}{1}$
- 2 next-nearest neighbors at distance $2r$ with same charge: contribution $-2 \cdot \frac{1}{2}$
- 2 neighbors at distance $3r$ with opposite charge: contribution $+2 \cdot \frac{1}{3}$
- 2 neighbors at distance $4r$ with same charge: contribution $-2 \cdot \frac{1}{4}$

The Madelung constant for the 1D infinite chain is:
$$M_{\text{1D}} = 2 \left( 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} - \cdots \right) = 2 \ln(2) \approx 2 \times 0.69315 = 1.38629$$

In three dimensions, calculating $M$ involves conditionally convergent alternating spherical series requiring Evjen or Ewald summation techniques.

| Crystal Structure Type | Coordination Numbers (Cation : Anion) | Madelung Constant ($M$, based on $r_0$) | Representative Compounds |
| :--- | :--- | :--- | :--- |
| **Rock Salt ($\text{NaCl}$)** | $6 : 6$ (Octahedral) | $1.74756$ | $\text{NaCl}, \text{KCl}, \text{MgO}, \text{CaO}$ |
| **Cesium Chloride ($\text{CsCl}$)** | $8 : 8$ (Cubic) | $1.76267$ | $\text{CsCl}, \text{CsBr}, \text{CsI}, \text{TlCl}$ |
| **Zinc Blende ($\text{ZnS}$, Sphalerite)** | $4 : 4$ (Tetrahedral) | $1.63805$ | $\beta\text{-ZnS}, \text{CuCl}, \text{GaAs}$ |
| **Wurtzite ($\text{ZnS}$)** | $4 : 4$ (Hexagonal) | $1.64132$ | $\alpha\text{-ZnS}, \text{ZnO}, \text{GaN}$ |
| **Fluorite ($\text{CaF}_2$)** | $8 : 4$ | $2.51939$ (geometric) / $5.0388$ | $\text{CaF}_2, \text{UO}_2, \text{ZrO}_2$ |
| **Rutile ($\text{TiO}_2$)** | $6 : 3$ | $2.408$ (geometric) | $\text{TiO}_2, \text{SnO}_2, \text{MnO}_2$ |

---

#### 2. Short-Range Quantum Born Repulsion
If only Coulombic forces operated, the crystal would spontaneously collapse to $r = 0$. However, as electron clouds interpenetrate, the Pauli Exclusion Principle enforces orthogonality between occupied core wavefunctions, creating a steep short-range repulsive force. Born modeled this repulsive potential empirically as:
$$E_{\text{repulsion}}(r) = \frac{N_A B}{r^n}$$
where $B$ is a repulsion coefficient and $n$ is the **Born exponent**, typically ranging between $5$ and $12$, reflecting the electronic compressibility of the closed-shell core configurations.

**Pauling's Values for Born Exponent ($n$):**
- $\text{He}$ core ($\text{Li}^+$): $n = 5$
- $\text{Ne}$ core ($\text{Na}^+, \text{F}^-, \text{Mg}^{2+}, \text{O}^{2-}$): $n = 7$
- $\text{Ar}$ core ($\text{K}^+, \text{Cl}^-, \text{Ca}^{2+}$) or $\text{Cu}^+$: $n = 9$
- $\text{Kr}$ core ($\text{Rb}^+, \text{Br}^-$) or $\text{Ag}^+$: $n = 10$
- $\text{Xe}$ core ($\text{Cs}^+, \text{I}^-$) or $\text{Au}^+$: $n = 12$
For a salt containing dissimilar cores, $n_{\text{avg}} = \frac{n_{\text{cation}} + n_{\text{anion}}}{2}$.

---

#### 3. Derivation of the Born-Landé Equation
The total molar potential energy of the crystal lattice as a function of internuclear separation $r$ is:
$$U(r) = E_{\text{Coulomb}}(r) + E_{\text{repulsion}}(r) = -\frac{N_A M |z_1 z_2| e^2}{4\pi\varepsilon_0 r} + \frac{N_A B}{r^n}$$

At mechanical equilibrium, the potential energy attains a minimum at the equilibrium distance $r = r_0$:
$$\left. \frac{dU}{dr} \right|_{r = r_0} = 0$$

Differentiating term by term:
$$\frac{dU}{dr} = \frac{N_A M |z_1 z_2| e^2}{4\pi\varepsilon_0 r^2} - \frac{n N_A B}{r^{n+1}}$$
Setting equal to zero at $r_0$:
$$\frac{N_A M |z_1 z_2| e^2}{4\pi\varepsilon_0 r_0^2} = \frac{n N_A B}{r_0^{n+1}} \implies B = \frac{M |z_1 z_2| e^2 r_0^{n-1}}{4\pi\varepsilon_0 n}$$

Substituting the expression for $B$ back into the total energy expression at $r = r_0$:
$$U_0 = U(r_0) = -\frac{N_A M |z_1 z_2| e^2}{4\pi\varepsilon_0 r_0} + \frac{N_A}{r_0^n} \left( \frac{M |z_1 z_2| e^2 r_0^{n-1}}{4\pi\varepsilon_0 n} \right)$$
$$U_0 = -\frac{N_A M |z_1 z_2| e^2}{4\pi\varepsilon_0 r_0} + \frac{N_A M |z_1 z_2| e^2}{4\pi\varepsilon_0 r_0 n}$$
Factoring out the electrostatic term yields the celebrated **Born-Landé Equation**:
$$U_0 = -\frac{N_A M |z_1 z_2| e^2}{4\pi\varepsilon_0 r_0} \left( 1 - \frac{1}{n} \right)$$

---

#### 4. The Born-Mayer Equation & Kapustinskii Simplification
Max Born and Joseph Mayer refined the repulsive potential by replacing the inverse power law $r^{-n}$ with a quantum-mechanically justified exponential term $B e^{-r/\rho}$, where $\rho \approx 34.5\text{ pm} = 0.345\text{ \AA}$ is the compressibility parameter:
$$U_{\text{Born-Mayer}} = -\frac{N_A M |z_1 z_2| e^2}{4\pi\varepsilon_0 r_0} \left( 1 - \frac{\rho}{r_0} \right)$$

#### Kapustinskii Equation (Structure-Independent Lattice Energy)
In 1943, Anatoli Kapustinskii realized that dividing the Madelung constant $M$ by the number of ions per formula unit $\nu = (\nu_+ + \nu_-)$ yielded a nearly invariant ratio across diverse crystal topologies:
$$\frac{M}{\nu} \approx 0.88 \pm 0.04$$
Kapustinskii combined this geometric invariance with the Born-Mayer potential to formulate an equation requiring **no knowledge of crystal structure or Madelung constant**, relying solely on ionic radii $r_+$ and $r_-$:
$$U_{\text{Kapustinskii}} = -\frac{120200 \cdot \nu \cdot |z_+ z_-|}{r_+ + r_-} \left( 1 - \frac{34.5}{r_+ + r_-} \right) \text{ kJ}\cdot\text{mol}^{-1}$$
*(where radii $r_+, r_-$ are expressed in picometers, $\text{pm}$)*."""
            },
            {
                "id": "sec3_3",
                "title": "§3.3 Coordination Number, Packing Geometry & Radius Ratio Rules",
                "content": r"""### Geometric Packing of Rigid Spherical Ions

In an idealized ionic crystal, ions are treated as hard, incompressible spheres of characteristic radii $r_+$ and $r_-$. Because electrostatic attractive forces are non-directional and extend spherically in all directions, an ionic crystal maximizes thermodynamic stability by:
1. Maximizing the **Coordination Number (CN)**: Packing as many counter-ions as possible around each central ion to optimize Coulombic attraction.
2. Maintaining **Cation-Anion Physical Contact**: Ensuring the central cation directly touches its coordinating anions.
3. Preventing **Anion-Anion Overlap**: Avoiding severe repulsive overlap between mutually adjacent like-charged coordinating anions.

The geometric stability threshold occurs at the critical **limiting radius ratio** $\rho_{\text{limit}} = \left(\frac{r_+}{r_-}\right)_{\text{crit}}$, where the coordinating anions are in mutual contact with each other while simultaneously touching the central cation. If $\frac{r_+}{r_-}$ drops below this critical ratio, the central cation "rattles" loosely in the coordination cavity, anion-anion repulsion destabilizes the lattice, and the crystal spontaneously collapses to a lower coordination number.

---

### Rigorous Derivation of Limiting Radius Ratios

```
   Trigonal Planar (CN = 3)        Tetrahedral (CN = 4)         Octahedral (CN = 6)
          O                                O                           O
        / | \                            / | \                       / | \
       O--C--O                          O--C--O                     O--C--O
                                                                     \ | /
   r+/r- >= 0.155                   r+/r- >= 0.225                     O
                                                                 r+/r- >= 0.414
```

#### 1. Trigonal Planar Coordination ($\text{CN} = 3$)
Three anions of radius $r_-$ surround a cation of radius $r_+$ in an equilateral triangle.
- Connect the centers of the three anions: they form an equilateral triangle of side $2r_-$.
- The distance from the triangle vertices to the centroid (where the cation sits) is $r_+ + r_-$.
- In an equilateral triangle, the angle from centroid to edge midpoint is $30^\circ$.
$$\cos(30^\circ) = \frac{r_-}{r_+ + r_-} = \frac{\sqrt{3}}{2}$$
$$\frac{r_+ + r_-}{r_-} = \frac{2}{\sqrt{3}} \implies \frac{r_+}{r_-} + 1 = \frac{2}{\sqrt{3}} \approx 1.1547$$
$$\left(\frac{r_+}{r_-}\right)_{\text{crit}} = \frac{2}{\sqrt{3}} - 1 = \frac{2 - \sqrt{3}}{\sqrt{3}} \approx 0.155$$

---

#### 2. Tetrahedral Coordination ($\text{CN} = 4$)
Four anions surround a cation at the vertices of a regular tetrahedron inscribed inside a cube of side $a$.
- Tetrahedral vertices occupy alternating corners of the cube: $(0,0,0), (a,a,0), (a,0,a), (0,a,a)$.
- Anion centers touch along the face diagonal of the cube:
  $$\text{Face diagonal} = a\sqrt{2} = 2r_- \implies a = \frac{2r_-}{\sqrt{2}} = r_-\sqrt{2}$$
- The cation sits at the body center of the cube $\left(\frac{a}{2}, \frac{a}{2}, \frac{a}{2}\right)$.
- The distance from body center to corner is half the cube body diagonal:
  $$\text{Distance} = \frac{a\sqrt{3}}{2} = r_+ + r_-$$
- Substituting $a = r_-\sqrt{2}$:
  $$r_+ + r_- = \frac{(r_-\sqrt{2})\sqrt{3}}{2} = r_-\frac{\sqrt{6}}{2} = r_-\sqrt{\frac{3}{2}}$$
$$\frac{r_+}{r_-} + 1 = \sqrt{\frac{3}{2}} = \frac{\sqrt{6}}{2} \approx 1.2247$$
$$\left(\frac{r_+}{r_-}\right)_{\text{crit}} = \sqrt{\frac{3}{2}} - 1 \approx 0.225$$

---

#### 3. Octahedral Coordination ($\text{CN} = 6$)
Six anions surround a central cation along Cartesian axes. Consider a square planar cross-section through the central cation and four coplanar anions:
- Cation of radius $r_+$ at $(0,0)$; four anions of radius $r_-$ at $(r_++r_-, 0)$, $(-r_+-r_-, 0)$, etc.
- Anions touch along the square edge: side length $s = 2r_-$.
- The diagonal of the square passes through two anion radii and the cation diameter:
  $$\text{Diagonal} = \sqrt{(2r_-)^2 + (2r_-)^2} = 2r_-\sqrt{2} = 2(r_+ + r_-)$$
- Simplifying:
  $$r_+ + r_- = r_-\sqrt{2}$$
$$\frac{r_+}{r_-} + 1 = \sqrt{2} \approx 1.4142$$
$$\left(\frac{r_+}{r_-}\right)_{\text{crit}} = \sqrt{2} - 1 \approx 0.414$$

---

#### 4. Cubic Coordination ($\text{CN} = 8$)
Eight anions occupy the eight corners of a cube of edge length $a$, surrounding a central cation at the body center.
- Coordinating anions touch along cube edges: $a = 2r_-$.
- Body diagonal passes through opposite corners: $\text{Body diagonal} = a\sqrt{3} = 2(r_+ + r_-)$.
- Substituting $a = 2r_-$:
  $$2r_-\sqrt{3} = 2(r_+ + r_-) \implies r_+ + r_- = r_-\sqrt{3}$$
$$\frac{r_+}{r_-} + 1 = \sqrt{3} \approx 1.7320$$
$$\left(\frac{r_+}{r_-}\right)_{\text{crit}} = \sqrt{3} - 1 \approx 0.732$$

---

### Master Summary of Radius Ratio Rules

| Limiting Ratio Range $\left(\frac{r_+}{r_-}\right)$ | Coordination Number (CN) | Coordination Geometry | Archetype Crystal Lattice |
| :--- | :--- | :--- | :--- |
| **$< 0.155$** | $2$ | Linear | Isolated gas molecules ($\text{BeCl}_2(g)$) |
| **$0.155 - 0.225$** | $3$ | Trigonal Planar | Borates ($\text{BO}_3^{3-}$), Nitrates ($\text{NO}_3^-$) |
| **$0.225 - 0.414$** | $4$ | Tetrahedral | Zinc Blende / Wurtzite ($\text{ZnS}, \text{CuCl}$) |
| **$0.414 - 0.732$** | $6$ | Octahedral | Rock Salt ($\text{NaCl}, \text{MgO}, \text{CaO}$) |
| **$0.732 - 1.000$** | $8$ | Cubic | Cesium Chloride ($\text{CsCl}, \text{CsBr}, \text{TlCl}$) |
| **$\ge 1.000$** | $12$ | Cuboctahedral / Close-Packed | Metals, Perovskite A-sites ($\text{CaTiO}_3$) |

#### Limitations & Deviations from Radius Ratio Rules:
While radius ratio rules provide elegant first-order geometric guidelines, experimental transition structures frequently violate them (e.g., $\text{LiCl}, \text{LiBr}, \text{LiI}$ have ratios $< 0.414$ but adopt 6-coordinate $\text{NaCl}$ structures; $\text{SrO}$ and $\text{BaO}$ adopt 6-coordination despite ratios $> 0.732$). These deviations arise because:
1. Ions are not hard incompressible spheres; their polarizabilities and effective radii vary dynamically with coordination number (Shannon crystal radii increase by $3\text{–}5\%$ per unit CN increase).
2. Electrostatic models neglect **partial covalency**, directionality of orbital overlap, and crystal field stabilization energy (CFSE) in transition metal compounds."""
            },
            {
                "id": "sec3_4",
                "title": "§3.4 Polarization of Ions & Fajan's Rules",
                "content": r"""### The Transition Continuum Between Ionic and Covalent Bonding

Pure ionic bonding and pure covalent bonding represent theoretical idealized asymptotic limits of a continuous chemical bonding spectrum. In realistic materials, when an electron cloud surrounds a polarizable anion in close proximity to a compact, highly charged cation, the spherically symmetric electron distribution of the anion is distorted toward the cation. This phenomenon is **anion polarization**, and the resulting electron cloud distortion introduces significant **covalent character** into the predominantly ionic lattice.

```
       Symmetric Non-Polarized                       Polarized Anion
              (Pure Ionic)                        (Partial Covalency)
            +             -                     +          (   -   )
         [ Cation ]   [ Anion ]              [ Cation ]  (  Anion   )
                                                         --> distortion -->
```

Kasimir Fajans systematized these effects into **Fajan's Rules**, which predict the onset and degree of covalent character in nominally ionic salts based on the polarizing power of the cation and the polarizability of the anion.

---

### Fajans' Three Governing Principles

#### 1. Cation Charge Density & Polarizing Power
A cation's ability to polarize an adjacent anion is defined as its **Polarizing Power** ($\phi$), proportional to its ionic charge density:
$$\phi = \frac{z_+}{r_+} \quad \text{or} \quad \text{Ionic Potential} = \frac{z_+ e}{4\pi\varepsilon_0 r_+^2}$$
- **Rule 1A: High Cationic Charge**: As the formal charge $z_+$ of the cation increases ($\text{Na}^+ < \text{Mg}^{2+} < \text{Al}^{3+} < \text{Si}^{4+}$), its Coulombic electric field gradient at the anion boundary escalates drastically, pulling the anion valence electrons into the internuclear region.
- **Rule 1B: Small Cationic Radius**: For cations of equal charge, smaller ionic radius concentrates charge into a diminutive volume, producing enormous local electric fields ($\text{Cs}^+ < \text{Rb}^+ < \text{K}^+ < \text{Na}^+ < \text{Li}^+$).
- *Consequence*: $\text{AlCl}_3$ has such high polarizing power ($\text{Al}^{3+}$ is small and highly charged) that it transitions from an ionic solid into a covalent dimer $\text{Al}_2\text{Cl}_6$ upon melting, subliming at $180^\circ\text{C}$, whereas $\text{NaCl}$ remains purely ionic with a melting point of $801^\circ\text{C}$.

---

#### 2. Anion Size & Polarizability
The susceptibility of an anion's electron cloud to deformation under an external electric field $\vec{E}$ is its **Electronic Polarizability** ($\alpha$):
$$\vec{\mu}_{\text{ind}} = \alpha \vec{E}$$
- **Rule 2A: Large Anionic Radius**: As the principal quantum number $n$ increases, valence electrons occupy diffuse orbitals located far from the nucleus, shielded by extensive core electrons. The loose nuclear grip permits facile distortion.
  $$\text{Polarizability sequence: } \text{F}^- < \text{Cl}^- < \text{Br}^- < \text{I}^- \quad \text{and} \quad \text{O}^{2-} < \text{S}^{2-} < \text{Se}^{2-} < \text{Te}^{2-}$$
- **Rule 2B: High Anionic Charge**: Anions with $-2$ or $-3$ charges have an excess of electron-electron repulsions expanding their valence shells, vastly augmenting $\alpha$.
- *Consequence*: Silver halides illustrate this trend starkly:
  - $\text{AgF}$: White, purely ionic, highly soluble in water ($1820\text{ g/L}$).
  - $\text{AgCl}$: White, weakly polarized, sparingly soluble ($1.9\times 10^{-3}\text{ g/L}$).
  - $\text{AgBr}$: Pale yellow, moderately polarized, highly insoluble ($1.4\times 10^{-4}\text{ g/L}$).
  - $\text{AgI}$: Deep yellow, intense polarization / covalency, insoluble ($3.0\times 10^{-6}\text{ g/L}$).
  The deepening yellow color reflects significant metal-ligand charge transfer (MLCT) facilitated by severe covalent orbital overlap.

---

#### 3. Cation Electronic Configuration: Non-Inert vs Inert Pair Gas Cores
Perhaps the most subtle and powerful rule concerns the difference between cations possessing a **noble gas core** ($s^2 p^6$, 8 valence core electrons) versus a **pseudo-noble gas core** ($d^{10}$ or $d^{10} s^2$, 18 valence core electrons).

Consider $\text{K}^+$ and $\text{Ag}^+$:
- Both cations possess identical formal charge: $z = +1$.
- Both have nearly identical ionic radii: $r(\text{K}^+) = 138\text{ pm}$, $r(\text{Ag}^+) = 126\text{ pm}$.
- Yet $\text{AgCl}$ is virtually insoluble in water ($K_{sp} = 1.8\times 10^{-10}$, melting point $455^\circ\text{C}$) whereas $\text{KCl}$ is highly soluble ($340\text{ g/L}$, melting point $770^\circ\text{C}$, completely ionic).

**Quantum Mechanical Origin**:
- $\text{K}^+$ has electron configuration $[\text{Ne}] 3s^2 3p^6$ (noble gas octet). The $s$ and $p$ electrons effectively shield nuclear charge.
- $\text{Ag}^+$ has electron configuration $[\text{Kr}] 4d^{10}$. The ten $d$ orbitals have diffuse angular lobes with nodal planes intersecting at the origin; their radial screening efficiency is notoriously poor ($\sigma_d \ll \sigma_s, \sigma_p$).
- Consequently, the effective nuclear charge $Z_{\text{eff}}$ leaking through the $4d^{10}$ shell of $\text{Ag}^+$ is substantially greater than that of $\text{K}^+$. The intense unshielded nuclear field reaches outside the core, violently polarizing adjacent anions.
- Therefore: **Cations with pseudo-noble gas cores ($18e^-$ configuration, $d^{10}$) have vastly greater polarizing power than cations of identical size and charge with noble gas cores ($8e^-$ configuration)**."""
            },
            {
                "id": "sec3_5",
                "title": "§3.5 Physical & Defect Properties of Ionic Solids",
                "content": r"""### Point Defects and Non-Stoichiometry in Real Crystals

In absolute thermodynamic equilibrium at any temperature above absolute zero ($T > 0\text{ K}$), an ideal, perfectly defect-free ionic crystal cannot exist. Gibbs free energy minimization dictates:
$$\Delta G_{\text{defect}} = \Delta H_{\text{defect}} - T \Delta S_{\text{config}}$$
While creating a crystal defect requires an endothermic enthalpy expenditure ($\Delta H_{\text{defect}} > 0$) to break lattice bonds, the introduction of disordered defect sites creates an astronomical increase in **configurational entropy** ($S_{\text{config}} = k_B \ln \Omega$). Because $-T \Delta S_{\text{config}}$ dominates at finite temperatures, a non-zero equilibrium concentration of point defects is thermodynamically mandated.

```
          Schottky Defect                          Frenkel Defect
     (Stoichiometric Pair Vacancy)            (Cation Vacancy + Interstitial)
      +   -   +   -   +                        +   -   +   -   +
      -  [ ]  -   +   -                        -   +   -  [ ]  -
      +   -   +  [ ]  +                        +   -   +   -   +
      -   +   -   +   -                        -   +  (+)  +   -  <-- Interstitial cation
```

---

### Classification of Stoichiometric Point Defects

Stoichiometric defects maintain the exact formal chemical ratio of cations to anions, preserving bulk electrical neutrality without altering overall stoichiometry.

#### 1. Schottky Defects
A Schottky defect consists of a pair of vacancies: one cation vacancy and one anion vacancy simultaneously absent from their normal lattice sites. The displaced ions migrate to the external crystal surface.
- **Occurrence Conditions**: Favored in strongly ionic compounds where cations and anions have comparable ionic radii ($\frac{r_+}{r_-} \approx 1$) and high coordination numbers ($6$ or $8$).
- **Archetype Systems**: $\text{NaCl}, \text{KCl}, \text{CsCl}, \text{KBr}$.
- **Physical Effect on Density**: Because vacant atomic sites leave unoccupied unit cell volume without mass, the **bulk crystal density decreases** significantly:
  $$\rho_{\text{defect}} = \rho_{\text{ideal}} \left(1 - \frac{n_s}{N}\right)$$
- **Equilibrium Defect Concentration**:
  $$n_s \approx N \exp\left(-\frac{\Delta H_s}{2 k_B T}\right)$$
  where $N$ is total lattice sites and $\Delta H_s$ is the formation enthalpy of a Schottky defect pair ($\sim 2\text{ eV}$ in $\text{NaCl}$).

---

#### 2. Frenkel Defects
A Frenkel defect occurs when an ion (almost universally the smaller cation) is dislodged from its regular lattice site and occupies an empty interstitial site within the crystal voids, creating a vacancy-interstitial pair.
- **Occurrence Conditions**: Favored when there is a large size disparity between cation and anion ($\frac{r_+}{r_-} \ll 1$), low coordination number ($4$), and high cation polarizability.
- **Archetype Systems**: $\text{AgCl}, \text{AgBr}, \text{ZnS}$.
- **Physical Effect on Density**: Because ions remain within the interior of the crystal lattice, the **density remains completely unchanged**.
- **Equilibrium Defect Concentration**:
  $$n_f \approx \sqrt{N N_i} \exp\left(-\frac{\Delta H_f}{2 k_B T}\right)$$
  where $N$ is regular lattice sites, $N_i$ is available interstitial positions, and $\Delta H_f$ is Frenkel pair formation enthalpy.

---

### Non-Stoichiometric Defects & Electronic Color Centers

When crystals deviate from ideal integer stoichiometric formulas, electrical neutrality is maintained through valence state switching of transition metal cations or trapped electrons.

#### 1. Metal Excess Due to Anion Vacancies: F-Centers (Farbe Centers)
When an alkali halide crystal such as $\text{NaCl}$ is heated in an atmosphere of sodium vapor:
1. Sodium atoms deposit on the crystal surface: $\text{Na}(g) \rightarrow \text{Na}^+ + e^-$.
2. Chloride anions $\text{Cl}^-$ diffuse outward to the surface to combine with $\text{Na}^+$.
3. To preserve electrical neutrality, the released electron diffuses inward and occupies the vacant anion site.

An electron trapped in an anion vacancy cavity surrounded by six coordinating cations forms an **F-Center** (*Farbe-Zentrum*, Color Center).
- Quantum mechanically, the trapped electron behaves as a **particle in a 3D finite spherical potential well**.
- Electronic transitions between ground and excited states absorb visible light:
  - $\text{NaCl}$ heated in $\text{Na}$ vapor turns **yellow**.
  - $\text{KCl}$ heated in $\text{K}$ vapor turns **violet / lilac**.
  - $\text{LiCl}$ heated in $\text{Li}$ vapor turns **pink / magenta**.
- The absorbed photon wavelength obeys Mollwo-Ivey relation: $\lambda \propto a^n$ ($a$ = lattice constant).

#### 2. Metal Deficiency Due to Cation Vacancies
In transition metal oxides such as $\text{FeO}$ (Wüstite, typically $\text{Fe}_{0.95}\text{O}$), some $\text{Fe}^{2+}$ ions are missing from their regular octahedral sites.
- For every missing $\text{Fe}^{2+}$ vacancy, electrical neutrality requires two neighboring ferrous ions to oxidize into ferric ions:
  $$2\,\text{Fe}^{2+} \longrightarrow 2\,\text{Fe}^{3+} + 2e^-$$
- The presence of adjacent $\text{Fe}^{2+}$ and $\text{Fe}^{3+}$ ions enables rapid electron hopping (polaron conduction), converting $\text{FeO}$ into a **p-type semiconductor** with elevated electrical conductivity."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational Level",
                "title": "Problem 3.1: Complete Born-Haber Thermochemical Cycle for Magnesium Oxide",
                "statement": r"""Calculate the standard lattice enthalpy ($\Delta H_{\text{lattice}}^\circ$) of crystalline magnesium oxide, $\text{MgO}(s)$, using the Born-Haber thermochemical cycle and the following experimentally determined calorimetric data:
- Standard enthalpy of formation of $\text{MgO}(s)$: $\Delta H_f^\circ = -601.7\text{ kJ}\cdot\text{mol}^{-1}$
- Enthalpy of sublimation of magnesium: $\Delta H_{\text{sub}}^\circ[\text{Mg}] = +147.1\text{ kJ}\cdot\text{mol}^{-1}$
- First ionization energy of magnesium: $\text{IE}_1[\text{Mg}] = +737.7\text{ kJ}\cdot\text{mol}^{-1}$
- Second ionization energy of magnesium: $\text{IE}_2[\text{Mg}] = +1450.7\text{ kJ}\cdot\text{mol}^{-1}$
- Bond dissociation enthalpy of gaseous oxygen: $\Delta H_{\text{diss}}^\circ[\text{O}_2] = +498.4\text{ kJ}\cdot\text{mol}^{-1}$
- First electron affinity enthalpy of oxygen: $\Delta H_{\text{EA}_1}[\text{O}] = -141.0\text{ kJ}\cdot\text{mol}^{-1}$
- Second electron affinity enthalpy of oxygen: $\Delta H_{\text{EA}_2}[\text{O}] = +744.0\text{ kJ}\cdot\text{mol}^{-1}$

Construct the formal Hess's law cycle equation, clearly identify every state transformation, and explain why the second electron affinity of oxygen is endothermic while the net compound remains extraordinarily stable.""",
                "solution": r"""### Step 1: Formulation of the Target Thermochemical Reaction
The standard lattice enthalpy $\Delta H_{\text{lattice}}^\circ$ is defined as the enthalpy change for the condensation of gaseous magnesium cations and gaseous oxide anions into crystalline magnesium oxide:
$$\text{Mg}^{2+}(g) + \text{O}^{2-}(g) \xrightarrow{\Delta H_{\text{lattice}}^\circ} \text{MgO}(s)$$

The standard enthalpy of formation corresponds to the reaction:
$$\text{Mg}(s) + \frac{1}{2}\,\text{O}_2(g) \xrightarrow{\Delta H_f^\circ} \text{MgO}(s), \quad \Delta H_f^\circ = -601.7\text{ kJ}\cdot\text{mol}^{-1}$$

---

### Step 2: Construction of the Stepwise Born-Haber Cycle
We construct an alternative thermodynamic pathway converting the elemental reactants into gaseous ions:
1. **Sublimation of solid magnesium**:
   $$\text{Mg}(s) \longrightarrow \text{Mg}(g), \quad \Delta H_1 = \Delta H_{\text{sub}}^\circ[\text{Mg}] = +147.1\text{ kJ}\cdot\text{mol}^{-1}$$
2. **First and second ionization of gaseous magnesium**:
   $$\text{Mg}(g) \longrightarrow \text{Mg}^+(g) + e^-, \quad \Delta H_2 = \text{IE}_1[\text{Mg}] = +737.7\text{ kJ}\cdot\text{mol}^{-1}$$
   $$\text{Mg}^+(g) \longrightarrow \text{Mg}^{2+}(g) + e^-, \quad \Delta H_3 = \text{IE}_2[\text{Mg}] = +1450.7\text{ kJ}\cdot\text{mol}^{-1}$$
   Total ionization enthalpy:
   $$\Delta H_{\text{IE},\text{total}} = 737.7 + 1450.7 = +2188.4\text{ kJ}\cdot\text{mol}^{-1}$$
3. **Dissociation of molecular oxygen (atomization)**:
   $$\frac{1}{2}\,\text{O}_2(g) \longrightarrow \text{O}(g), \quad \Delta H_4 = \frac{1}{2}\,\Delta H_{\text{diss}}^\circ[\text{O}_2] = \frac{1}{2}(+498.4) = +249.2\text{ kJ}\cdot\text{mol}^{-1}$$
4. **First and second electron affinities of gaseous oxygen**:
   $$\text{O}(g) + e^- \longrightarrow \text{O}^-(g), \quad \Delta H_5 = \Delta H_{\text{EA}_1} = -141.0\text{ kJ}\cdot\text{mol}^{-1}$$
   $$\text{O}^-(g) + e^- \longrightarrow \text{O}^{2-}(g), \quad \Delta H_6 = \Delta H_{\text{EA}_2} = +744.0\text{ kJ}\cdot\text{mol}^{-1}$$
   Net electron gain enthalpy:
   $$\Delta H_{\text{EA},\text{net}} = -141.0 + 744.0 = +603.0\text{ kJ}\cdot\text{mol}^{-1}$$
5. **Lattice condensation**:
   $$\text{Mg}^{2+}(g) + \text{O}^{2-}(g) \longrightarrow \text{MgO}(s), \quad \Delta H_7 = \Delta H_{\text{lattice}}^\circ$$

---

### Step 3: Application of Hess's Law
By Hess's law of constant heat summation:
$$\Delta H_f^\circ = \Delta H_{\text{sub}}^\circ + \text{IE}_1 + \text{IE}_2 + \frac{1}{2}\Delta H_{\text{diss}}^\circ + \Delta H_{\text{EA}_1} + \Delta H_{\text{EA}_2} + \Delta H_{\text{lattice}}^\circ$$

Rearranging for the unknown lattice enthalpy:
$$\Delta H_{\text{lattice}}^\circ = \Delta H_f^\circ - \left( \Delta H_{\text{sub}}^\circ + \text{IE}_1 + \text{IE}_2 + \frac{1}{2}\Delta H_{\text{diss}}^\circ + \Delta H_{\text{EA}_1} + \Delta H_{\text{EA}_2} \right)$$

Substitute the numerical values:
$$\Delta H_{\text{gas ions}} = 147.1 + 737.7 + 1450.7 + 249.2 + (-141.0) + 744.0 = 3187.7\text{ kJ}\cdot\text{mol}^{-1}$$
$$\Delta H_{\text{lattice}}^\circ = -601.7 - 3187.7 = -3789.4\text{ kJ}\cdot\text{mol}^{-1}$$

---

### Step 4: Physical Interpretation
1. **Lattice Enthalpy**: $\Delta H_{\text{lattice}}^\circ = -3789.4\text{ kJ}\cdot\text{mol}^{-1}$ (or lattice dissociation energy $U_L = +3789.4\text{ kJ}\cdot\text{mol}^{-1}$). This colossal energy is roughly five times larger than that of $\text{NaCl}$ ($-787\text{ kJ}\cdot\text{mol}^{-1}$), reflecting the product of divalent charges $|z_+ z_-| = |(+2)(-2)| = 4$ versus $|(+1)(-1)| = 1$ in the Coulomb potential.
2. **Endothermic Second Electron Affinity**: Adding an electron to an already negatively charged $\text{O}^-$ anion requires conquering intense electrostatic repulsive barriers ($+744\text{ kJ}\cdot\text{mol}^{-1}$). Gaseous $\text{O}^{2-}$ cannot exist in isolation. However, in the solid state, the $-3789.4\text{ kJ}\cdot\text{mol}^{-1}$ lattice energy overwhelmingly compensates for the $+603\text{ kJ}\cdot\text{mol}^{-1}$ net ionization cost, stabilizing the divalent lattice."""
            },
            {
                "tier": "Advanced Level",
                "title": "Problem 3.2: Theoretical Lattice Energy of NaCl via Born-Landé and Kapustinskii Equations",
                "statement": r"""For rock salt ($\text{NaCl}$), given the following physical constants and parameters:
- Madelung constant for rock-salt lattice: $M = 1.74756$
- Equilibrium internuclear separation: $r_0 = 282.0\text{ pm} = 2.820 \times 10^{-10}\text{ m}$
- Avogadro's constant: $N_A = 6.02214 \times 10^{23}\text{ mol}^{-1}$
- Elementary charge: $e = 1.60218 \times 10^{-19}\text{ C}$
- Vacuum permittivity: $\varepsilon_0 = 8.85419 \times 10^{-12}\text{ C}^2\cdot\text{N}^{-1}\cdot\text{m}^{-2}$
- Born exponents: $n(\text{Na}^+) = 7$, $n(\text{Cl}^-) = 9$
- Shannon crystal radii: $r(\text{Na}^+) = 102\text{ pm}$, $r(\text{Cl}^-) = 181\text{ pm}$

1. Compute the average Born exponent $n_{\text{avg}}$ and evaluate the theoretical lattice energy $U_0$ using the **Born-Landé equation**.
2. Compute the theoretical lattice energy using the structure-independent **Kapustinskii equation**.
3. Compare both theoretical values with the experimental Born-Haber cycle value ($\Delta H_{\text{lattice}}^\circ = -787\text{ kJ}\cdot\text{mol}^{-1}$) and quantify the percentage error for each model.""",
                "solution": r"""### Part 1: Calculation via the Born-Landé Equation
The Born-Landé formula is:
$$U_0 = -\frac{N_A M |z_1 z_2| e^2}{4\pi\varepsilon_0 r_0} \left( 1 - \frac{1}{n_{\text{avg}}} \right)$$

#### 1. Average Born Exponent:
$$n_{\text{avg}} = \frac{n(\text{Na}^+) + n(\text{Cl}^-)}{2} = \frac{7 + 9}{2} = 8.0$$

#### 2. Electrostatic Factor:
Evaluate the electrostatic constant factor $\frac{N_A e^2}{4\pi\varepsilon_0}$:
$$\frac{N_A e^2}{4\pi\varepsilon_0} = \frac{(6.02214 \times 10^{23}) \times (1.60218 \times 10^{-19})^2}{4\pi \times (8.85419 \times 10^{-12})}$$
$$\frac{N_A e^2}{4\pi\varepsilon_0} = \frac{(6.02214 \times 10^{23}) \times (2.56698 \times 10^{-38})}{1.11265 \times 10^{-10}} = \frac{1.54587 \times 10^{-14}}{1.11265 \times 10^{-10}} = 1.38936 \times 10^{-4}\text{ J}\cdot\text{m}\cdot\text{mol}^{-1}$$
$$= 138.936\text{ kJ}\cdot\text{nm}\cdot\text{mol}^{-1} = 1.38936 \times 10^5\text{ kJ}\cdot\text{pm}\cdot\text{mol}^{-1}$$

#### 3. Unshielded Coulomb Energy:
$$E_{\text{Coulomb}} = -\frac{1.38936 \times 10^5 \times 1.74756 \times |(+1)(-1)|}{282.0} = -\frac{242800}{282.0} = -861.0\text{ kJ}\cdot\text{mol}^{-1}$$

#### 4. Inclusion of Pauli Repulsion Factor:
$$\left( 1 - \frac{1}{n_{\text{avg}}} \right) = \left( 1 - \frac{1}{8} \right) = \frac{7}{8} = 0.875$$
$$U_0 = -861.0 \times 0.875 = -753.4\text{ kJ}\cdot\text{mol}^{-1}$$

---

### Part 2: Calculation via the Kapustinskii Equation
The Kapustinskii equation is:
$$U_{\text{Kap}} = -\frac{120200 \cdot \nu \cdot |z_+ z_-|}{r_+ + r_-} \left( 1 - \frac{34.5}{r_+ + r_-} \right) \text{ kJ}\cdot\text{mol}^{-1}$$
For $\text{NaCl}$: $\nu = 2$ ($\text{Na}^+$ and $\text{Cl}^-$), $z_+ = +1, z_- = -1$, and sum of radii $r_+ + r_- = 102 + 181 = 283\text{ pm}$.

#### 1. Substituting parameters:
$$U_{\text{Kap}} = -\frac{120200 \times 2 \times 1}{283} \left( 1 - \frac{34.5}{283} \right)$$
$$\frac{240400}{283} \approx 849.47\text{ kJ}\cdot\text{mol}^{-1}$$
$$\left( 1 - \frac{34.5}{283} \right) = 1 - 0.1219 = 0.8781$$
$$U_{\text{Kap}} = -849.47 \times 0.8781 = -745.9\text{ kJ}\cdot\text{mol}^{-1}$$

---

### Part 3: Comparison with Experimental Value and Discussion
The experimental lattice enthalpy is $\Delta H_{\text{lattice}}^\circ = -787.0\text{ kJ}\cdot\text{mol}^{-1}$.

1. **Born-Landé Discrepancy**:
   $$\text{Error}_{\text{BL}} = \frac{|-753.4 - (-787.0)|}{787.0} \times 100\% = \frac{33.6}{787.0} \times 100\% = 4.27\%$$
2. **Kapustinskii Discrepancy**:
   $$\text{Error}_{\text{Kap}} = \frac{|-745.9 - (-787.0)|}{787.0} \times 100\% = \frac{41.1}{787.0} \times 100\% = 5.22\%$$

Both simple electrostatic models match experiment within $4\text{–}5\%$. The remaining $\sim 33\text{–}41\text{ kJ}\cdot\text{mol}^{-1}$ deficit in the theoretical electrostatic energy arises from:
1. **London Dispersion Forces**: Attractive van der Waals dipole-induced dipole interactions contribute roughly $+20\text{ kJ}\cdot\text{mol}^{-1}$ of stabilization.
2. **Zero-Point Vibrational Energy**: Quantum zero-point phonons destabilize the lattice by $\approx \frac{9}{8} N_A h \nu_{\text{Debye}} \approx 7\text{ kJ}\cdot\text{mol}^{-1}$.
3. **Partial Covalent Character**: Minor polarization of the large chloride anion by the sodium cation introduces residual wavefunction overlap."""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 3.3: Rigorous Polarization Proof & Thermal Decomposition Energetics of Carbonates",
                "statement": r"""The thermal decomposition temperature of alkaline earth metal carbonates, $\text{MCO}_3(s) \longrightarrow \text{MO}(s) + \text{CO}_2(g)$, increases dramatically down Group 2:
- $\text{BeCO}_3$: $T_{\text{decomp}} \approx 373\text{ K}$ ($100^\circ\text{C}$)
- $\text{MgCO}_3$: $T_{\text{decomp}} \approx 813\text{ K}$ ($540^\circ\text{C}$)
- $\text{CaCO}_3$: $T_{\text{decomp}} \approx 1173\text{ K}$ ($900^\circ\text{C}$)
- $\text{SrCO}_3$: $T_{\text{decomp}} \approx 1563\text{ K}$ ($1290^\circ\text{C}$)
- $\text{BaCO}_3$: $T_{\text{decomp}} \approx 1633\text{ K}$ ($1360^\circ\text{C}$)

1. Using thermodynamic enthalpy cycles and lattice energy differentials, provide a rigorous mathematical proof demonstrating why $\Delta H_{\text{decomp}}^\circ$ must increase as the cation radius $r_{M^{2+}}$ increases.
2. Formulate the relationship between the decomposition temperature $T_{\text{decomp}}$ and the lattice energy difference $\Delta U = U_0[\text{MO}] - U_0[\text{MCO}_3]$.
3. Explain the phenomenon using Fajan's polarization model: analyze the deformation of the polyatomic planar $\text{CO}_3^{2-}$ anion by the polarizing field of $M^{2+}$, showing how polarized C-O bond cleavage leads to spontaneous $\text{CO}_2$ extrusion.""",
                "solution": r"""### Part 1: Thermodynamic Enthalpy Cycle Proof
The decomposition reaction is:
$$\text{MCO}_3(s) \longrightarrow \text{MO}(s) + \text{CO}_2(g)$$

We construct a thermochemical cycle decomposing the solids into gaseous ions $\text{M}^{2+}(g)$, $\text{CO}_3^{2-}(g)$, and $\text{O}^{2-}(g)$:
1. Dissociation of carbonate solid:
   $$\text{MCO}_3(s) \longrightarrow \text{M}^{2+}(g) + \text{CO}_3^{2-}(g), \quad \Delta H_1 = U_0[\text{MCO}_3]$$
2. Gas-phase cleavage of carbonate anion:
   $$\text{CO}_3^{2-}(g) \longrightarrow \text{O}^{2-}(g) + \text{CO}_2(g), \quad \Delta H_2 = \Delta H_{\text{gas cleave}}^\circ$$
   *(Note that $\Delta H_{\text{gas cleave}}^\circ$ is a pure constant independent of the cation identity)*.
3. Lattice condensation into oxide:
   $$\text{M}^{2+}(g) + \text{O}^{2-}(g) \longrightarrow \text{MO}(s), \quad \Delta H_3 = -U_0[\text{MO}]$$

Summing the cycle gives the net decomposition enthalpy:
$$\Delta H_{\text{decomp}}^\circ = U_0[\text{MCO}_3] - U_0[\text{MO}] + \Delta H_{\text{gas cleave}}^\circ = \Delta H_{\text{gas cleave}}^\circ - \left( U_0[\text{MO}] - U_0[\text{MCO}_3] \right)$$

---

### Part 2: Mathematical Derivative with Respect to Cation Radius
Using the Kapustinskii approximation for lattice energy $U_0 \approx \frac{C}{r_+ + r_-}$ where $C = 120200 \cdot \nu \cdot |z_+ z_-|$:
For both $\text{MO}$ and $\text{MCO}_3$, $\nu = 2$ and $z_+ z_- = 4$, so the constant $C$ is identical.
$$U_0[\text{MO}] \approx \frac{C}{r_{M^{2+}} + r_{O^{2-}}}$$
$$U_0[\text{MCO}_3] \approx \frac{C}{r_{M^{2+}} + r_{CO_3^{2-}}}$$

The difference in lattice energies is:
$$\Delta U(r_+) = U_0[\text{MO}] - U_0[\text{MCO}_3] = C \left( \frac{1}{r_+ + r_{O^{2-}}} - \frac{1}{r_+ + r_{CO_3^{2-}}} \right) = C \frac{r_{CO_3^{2-}} - r_{O^{2-}}}{(r_+ + r_{O^{2-}})(r_+ + r_{CO_3^{2-}})}$$

Because the oxide ion is compact ($r_{O^{2-}} \approx 140\text{ pm}$) while the carbonate ion is large and polyatomic ($r_{CO_3^{2-}} \approx 185\text{ pm}$), the numerator is strictly positive:
$$r_{CO_3^{2-}} - r_{O^{2-}} > 0$$

Now take the derivative of $\Delta U(r_+)$ with respect to cation radius $r_+$:
$$\frac{d}{dr_+} \left[ \Delta U(r_+) \right] = C (r_{CO_3^{2-}} - r_{O^{2-}}) \cdot \frac{d}{dr_+} \left[ \frac{1}{(r_+ + r_{O^{2-}})(r_+ + r_{CO_3^{2-}})} \right]$$
$$\frac{d}{dr_+} \left[ \frac{1}{(r_+ + r_1)(r_+ + r_2)} \right] = -\frac{2r_+ + r_1 + r_2}{(r_+ + r_1)^2 (r_+ + r_2)^2} < 0$$

Therefore:
$$\frac{d(\Delta U)}{dr_+} < 0$$
As the cation radius $r_{M^{2+}}$ increases from $\text{Be}^{2+}$ to $\text{Ba}^{2+}$, the lattice energy difference $\Delta U = U_0[\text{MO}] - U_0[\text{MCO}_3]$ **strictly decreases**.

Now substitute this into the decomposition enthalpy:
$$\frac{d(\Delta H_{\text{decomp}}^\circ)}{dr_+} = -\frac{d(\Delta U)}{dr_+} > 0$$

$$\mathbf{\frac{d(\Delta H_{\text{decomp}}^\circ)}{dr_+} > 0 \quad \text{(Proven)}}$$

Since the decomposition reaction produces gas ($\text{CO}_2(g)$), $\Delta S_{\text{decomp}}^\circ \approx \Delta S^\circ[\text{CO}_2(g)] \approx +160\text{ to } +175\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}$, which is approximately constant across all Group 2 carbonates.
At equilibrium decomposition:
$$\Delta G^\circ = \Delta H^\circ - T_{\text{decomp}} \Delta S^\circ = 0 \implies T_{\text{decomp}} \approx \frac{\Delta H_{\text{decomp}}^\circ}{\Delta S_{\text{decomp}}^\circ}$$
Because $\Delta H_{\text{decomp}}^\circ$ monotonically increases as cation radius expands, **$T_{\text{decomp}}$ must strictly escalate down the group**.

---

### Part 3: Physical Proof via Fajan's Polarization Mechanism
At the microscopic level:
1. The carbonate anion $\text{CO}_3^{2-}$ is a planar resonance hybrid where negative charge is delocalized over three electronegative oxygen atoms.
2. A small cation with immense charge density ($\text{Be}^{2+}$, ionic potential $\phi = \frac{2}{31\text{ pm}} \approx 0.065\text{ pm}^{-1}$) exerts an extreme non-uniform electric field on an adjacent oxygen atom.
3. This intense polarization pulls the electron density of the coordinating oxygen atom toward $\text{Be}^{2+}$, weakening the covalent $\text{C}-\text{O}$ single/double bond in the carbonate framework.
4. As the $\text{C}-\text{O}$ bond order decreases, the carbonate framework spontaneously undergoes concerted heterolytic fission into a stable neutral linear $\text{CO}_2$ molecule and a bound $\text{O}^{2-}$ ion coordinated to the cation.
5. In contrast, for the massive $\text{Ba}^{2+}$ cation ($\phi = \frac{2}{135\text{ pm}} \approx 0.015\text{ pm}^{-1}$), polarizing power is weak, the $\text{CO}_3^{2-}$ resonance stabilization remains unperturbed, and thermal cleavage requires extreme kinetic temperatures exceeding $1360^\circ\text{C}$."""
            }
        ]
    }
'''

with open("build_inorg1_unit3.py", "w", encoding="utf-8") as f:
    f.write(content)

print("build_inorg1_unit3.py written successfully.")
