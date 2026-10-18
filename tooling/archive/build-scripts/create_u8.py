import json

def get_unit_8():
    u8 = {
        "id": "unit-8",
        "number": 8,
        "title": "Point Defects, Defect Thermodynamics & Non-Stoichiometry",
        "leadSummary": "Thermodynamics of 0D point defects, Schottky and Frenkel equilibria, Kröger-Vink defect notation, non-stoichiometry in transition metal oxides (Fe1-xO, ZnO, TiO2-x), color centers (F-centers, Mollwo-Ivey law), Brouwer defect diagrams, and crystallographic shear structures (Magnéli phases).",
        "simulations": ["sim_ssc_point_defect_thermodynamics"],
        "sections": [
            {
                "secNumber": "8.1",
                "title": "Thermodynamics of Intrinsic Point Defects: Entropy of Mixing & Defect Concentration",
                "content": r"""At any finite temperature ($T > 0\\text{ K}$), an ideal, defect-free crystal lattice is thermodynamically unstable. The spontaneous formation of point defects increases the internal enthalpy ($\Delta H_d > 0$), but this energetic penalty is overcome by the enormous increase in configurational entropy ($\Delta S_{\\text{conf}} > 0$).

### Free Energy Formulation
Consider creating $n$ isolated vacancies in a crystal containing $N$ regular atomic lattice sites.
The Gibbs free energy change of defect formation is:
\\[
\\Delta G(n) = \\Delta H(n) - T \\Delta S(n) = n \\Delta H_v - T (\\Delta S_{\\text{vib}} + \\Delta S_{\\text{conf}})
\\]
where $\\Delta H_v$ is the enthalpy of vacancy formation and $\\Delta S_{\\text{vib}}$ is the local vibrational entropy change due to altered phonon frequencies around the vacancy.
The number of distinct ways $W$ to distribute $n$ vacancies among $N+n$ available sites is:
\\[
W = \\frac{(N+n)!}{N!\\, n!}
\\]
Applying Boltzmann's entropy formula $S = k_B \\ln W$ and Stirling's approximation ($\\ln x! \\approx x\\ln x - x$):
\\[
\\Delta S_{\\text{conf}} = k_B \\ln W \\approx k_B \\left[ (N+n)\\ln(N+n) - N\\ln N - n\\ln n \\right]
\\]

### Minimization and Equilibrium Concentration
Thermodynamic equilibrium at constant temperature and pressure requires:
\\[
\\left( \\frac{\\partial \\Delta G}{\\partial n} \\right)_{T, P} = 0
\\]
Differentiating $\\Delta G$:
\\[
\\frac{\\partial \\Delta G}{\\partial n} = \\Delta H_v - T \\Delta S_{\\text{vib}} + k_B T \\ln\\left(\\frac{n}{N+n}\\right) = 0
\\]
\\[
\\ln\\left(\\frac{n}{N+n}\\right) = -\\frac{\\Delta H_v - T \\Delta S_{\\text{vib}}}{k_B T} = -\\frac{\\Delta G_v}{k_B T}
\\]
Since $n \\ll N$, $N+n \\approx N$:
\\[
\\frac{n}{N} = \\exp\\left(\\frac{\\Delta S_{\\text{vib}}}{k_B}\\right) \\exp\\left(-\\frac{\\Delta H_v}{k_B T}\\right) = C_0 \\exp\\left(-\\frac{\\Delta H_v}{k_B T}\\right)
\\]
Because $\\left( \\frac{\\partial^2 \\Delta G}{\\partial n^2} \\right) = \\frac{k_B T}{n} > 0$, this represents a true global minimum. Point defects are equilibrium thermodynamic entities, unlike dislocations or grain boundaries."""
            },
            {
                "secNumber": "8.2",
                "title": "Schottky Defects: Formation Energy & Equilibrium Constant",
                "content": r"""In ionic crystals, point defects must preserve macroscopic electrical neutrality. Walter Schottky (1935) identified the stoichiometric stoichiometric defect pair known as the **Schottky defect**.

### Definition and Mechanism
A Schottky defect consists of a stoichiometric pair of vacancies: one cation vacancy and one anion vacancy (for a $1:1$ binary crystal $MX$).
- To maintain crystal density and surface integrity, the displaced cation and anion migrate to the exterior crystal surface, creating new regular lattice sites:
\\[
\\text{Null} \\rightleftharpoons \\text{V}_M' + \\text{V}_X^\\bullet
\\]
- Both sublattices lose ions in equal proportions, preserving charge neutrality and stoichiometric composition.
- Crystal density decreases because the crystal volume increases while mass remains constant.

### Equilibrium Mass-Action Law
Let $N$ be the number of cation sites (equal to anion sites in $MX$).
If $n_S$ Schottky pairs are formed, the number of ways to arrange $n_S$ cation vacancies on $N$ cation sites is $W_c = \\frac{N!}{(N-n_S)! n_S!}$, and similarly for anion vacancies $W_a = \\frac{N!}{(N-n_S)! n_S!}$.
Total configurational entropy:
\\[
\\Delta S_{\\text{conf}} = k_B \\ln(W_c W_a) = 2 k_B \\left[ N\\ln N - (N-n_S)\\ln(N-n_S) - n_S\\ln n_S \\right]
\\]
Minimizing $\\Delta G = n_S \\Delta H_S - T \\Delta S_{\\text{conf}}$:
\\[
\\frac{\\partial \\Delta G}{\\partial n_S} = \\Delta H_S - 2 k_B T \\ln\\left( \\frac{N-n_S}{n_S} \\right) = 0
\\]
Assuming $n_S \\ll N$:
\\[
\\frac{n_S}{N} = \\exp\\left(-\\frac{\\Delta H_S}{2 k_B T}\\right)
\\]
Notice the crucial factor of **$1/2$ in the exponent**: because the defect is a binary pair, the effective activation energy is half the total pair formation enthalpy $\\Delta H_S/2$.
- Typical formation enthalpies in alkali halides are $\\Delta H_S \\approx 2.0 - 2.5\\text{ eV}$, yielding $n_S/N \\sim 10^{-5}$ near the melting point and $n_S/N \\sim 10^{-16}$ at room temperature."""
            },
            {
                "secNumber": "8.3",
                "title": "Frenkel Defects: Interstitial Formation Mechanics & Spatial Energetics",
                "content": r"""Yakov Frenkel (1926) formulated an alternative stoichiometric defect mechanism: the **Frenkel defect**.

### Microscopic Mechanism
A Frenkel defect consists of an ion that leaves its normal crystallographic lattice site and squeezes into an unoccupied **interstitial void**, creating a vacancy-interstitial pair:
\\[
M_M^\\times \\rightleftharpoons \\text{V}_M' + M_i^\\bullet
\\]
- The stoichiometry and total mass remain unaltered.
- The overall macroscopic crystal volume remains virtually unchanged, so crystal density does not decrease appreciably.
- Frenkel defects typically occur on the **cation sublattice** (cation Frenkel defect) because cations are substantially smaller than anions ($r^+ \\ll r^-$) and fit much more readily into tight interstitial cavities.
- Anion Frenkel defects ($\text{V}_X^\\bullet + X_i'$) are rare due to severe steric overlap, but occur in fluorite-type crystals ($\\text{CaF}_2, \\text{UO}_2$) where empty interstitial cubes accommodate fluoride or oxide ions.

### Thermodynamic Formulation
Let $N$ be the number of normal lattice sites and $N_i$ be the number of available interstitial sites.
The number of ways to distribute $n_F$ vacancies among $N$ normal sites is $\\frac{N!}{(N-n_F)! n_F!}$, and $n_F$ interstitials among $N_i$ interstitial sites is $\\frac{N_i!}{(N_i-n_F)! n_F!}$.
Minimizing $\\Delta G$:
\\[
\\frac{n_F}{\\sqrt{N N_i}} = \\exp\\left(-\\frac{\\Delta H_F}{2 k_B T}\\right)
\\]
Again, the exponent contains the factor $1/2$.
- **Frenkel Archetype**: Silver halides ($\\text{AgCl}, \\text{AgBr}$). The polarizable $4d^{10}$ shell of $\\text{Ag}^+$ enables easy deformation and stabilization in tetrahedral interstitial sites of the FCC bromide lattice ($\Delta H_F \\approx 1.2\\text{ eV}$), providing the photographic and fast ionic conduction mechanism of silver salts."""
            },
            {
                "secNumber": "8.4",
                "title": "Kröger-Vink Notation: Formalism, Effective Charges & Defect Equations",
                "content": r"""F. A. Kröger and H. J. Vink (1956) developed a systematic chemical notation for writing point defect equilibria in crystalline solids.

### The Kröger-Vink Notation Syntax: $A_S^C$
A defect species is represented by three components:
1. **Main Symbol ($A$)**: Indicates the entity currently occupying the site.
   - Element symbol (e.g., $\\text{Na}, \\text{Cl}, \\text{Fe}$).
   - $\\text{V}$ represents a **vacancy** (empty site).
   - $e$ or $e'$ represents a free conduction electron.
   - $h$ or $h^\\bullet$ represents an electron hole in the valence band.
2. **Subscript ($S$)**: Indicates the crystallographic site type.
   - Element symbol whose site is occupied (e.g., $M, X, \\text{Na}, \\text{Cl}$).
   - $i$ represents an **interstitial site**.
3. **Superscript ($C$)**: Indicates the **effective (virtual) charge** relative to the perfect, unperturbed crystal lattice:
   - $\\times$ represents **neutral** effective charge ($q_{\\text{eff}} = 0$).
   - $\\bullet$ represents **positive** effective charge ($q_{\\text{eff}} = +1$).
   - $'$ (prime) represents **negative** effective charge ($q_{\\text{eff}} = -1$).
   \\[
   q_{\\text{eff}} = q_{\\text{actual}} - q_{\\text{normal lattice site}}
   \\]

### Rules for Balancing Defect Equations
1. **Conservation of Mass**: Chemical atoms must balance identically on both sides (vacancies $\\text{V}$ have zero mass).
2. **Conservation of Effective Charge**: The algebraic sum of effective charges on the left must equal the sum on the right:
\\[
\\sum q_{\\text{eff}}^{\\text{reactants}} = \\sum q_{\\text{eff}}^{\\text{products}}
\\]
3. **Conservation of Site Ratio**: The ratio of cation sites to anion sites in the crystal host must remain constant according to the host stoichiometry. Sites cannot be created or destroyed independently on one sublattice alone.

### Examples of Standard Defect Reactions
- Schottky defect in $\\text{NaCl}$:
  \\[
  \\text{Null} \\rightleftharpoons \\text{V}_{\\text{Na}}' + \\text{V}_{\\text{Cl}}^\\bullet, \\quad K_S = [\\text{V}_{\\text{Na}}'][\\text{V}_{\\text{Cl}}^\\bullet]
  \\]
- Frenkel defect in $\\text{AgBr}$:
  \\[
  \\text{Ag}_{\\text{Ag}}^\\times \\rightleftharpoons \\text{V}_{\\text{Ag}}' + \\text{Ag}_i^\\bullet, \\quad K_F = [\\text{V}_{\\text{Ag}}'][\\text{Ag}_i^\\bullet]
  \\]
- Electron-hole thermal excitation across the band gap:
  \\[
  \\text{Null} \\rightleftharpoons e' + h^\\bullet, \\quad K_i = n p
  \\]"""
            },
            {
                "secNumber": "8.5",
                "title": "Non-Stoichiometry in Binary Oxides: Metal-Deficient and Anion-Deficient Systems",
                "content": r"""Many transition metal oxides, sulfides, and halides deviate measurably from ideal integer stoichiometry depending on temperature and ambient oxygen partial pressure ($P_{\\text{O}_2}$). These are classified into two broad regimes:

### 1. Metal-Deficient Oxides ($M_{1-x}O$, e.g., $\\text{Fe}_{1-x}\\text{O}, \\text{Ni}_{1-x}\\text{O}, \\text{CoO}$)
- **Structural Nature**: Cation vacancies are created when the crystal is exposed to oxidizing atmospheres (high $P_{\\text{O}_2}$).
- **Defect Reaction**: Oxygen gas incorporates into the lattice, creating regular oxygen sites and an equivalent number of cation vacancies:
\\[
\\frac{1}{2}\\text{O}_2(g) \\rightleftharpoons \\text{O}_O^\\times + \\text{V}_M'' + 2h^\\bullet
\\]
- To preserve charge neutrality, two metal cations are oxidized to higher valence states (e.g., $2\\text{Fe}^{2+} \\to 2\\text{Fe}^{3+}$, represented as two electron holes $2h^\\bullet$).
- By the law of mass action:
\\[
K = \\frac{[\\text{V}_M''][h^\\bullet]^2}{P_{\\text{O}_2}^{1/2}}
\\]
Under electroneutrality $[h^\\bullet] = 2[\\text{V}_M'']$:
\\[
K = \\frac{[\\text{V}_M''](2[\\text{V}_M''])^2}{P_{\\text{O}_2}^{1/2}} = 4[\\text{V}_M'']^3 P_{\\text{O}_2}^{-1/2} \\implies [\\text{V}_M''] \\propto P_{\\text{O}_2}^{1/6}
\\]
The vacancy concentration and hole electrical conductivity ($\sigma = p e \mu_h$) scale as $P_{\\text{O}_2}^{1/6}$ (**$p$-type semiconductor**).

### 2. Anion-Deficient Oxides ($MO_{2-x}$ or $M_{1+x}O$, e.g., $\\text{ZnO}, \\text{TiO}_{2-x}, \\text{CeO}_{2-x}$)
- **Structural Nature**: Oxygen leaves the lattice into the gas phase under reducing conditions (low $P_{\\text{O}_2}$), leaving behind oxygen vacancies and conduction electrons:
\\[
\\text{O}_O^\\times \\rightleftharpoons \\frac{1}{2}\\text{O}_2(g) + \\text{V}_O^{\\bullet\\bullet} + 2e'
\\]
- Mass action relation:
\\[
K = [\\text{V}_O^{\\bullet\\bullet}][e']^2 P_{\\text{O}_2}^{1/2}
\\]
Under electroneutrality $[e'] = 2[\\text{V}_O^{\\bullet\\bullet}]$:
\\[
4[\\text{V}_O^{\\bullet\\bullet}]^3 P_{\\text{O}_2}^{1/2} = K \\implies [\\text{V}_O^{\\bullet\\bullet}] \\propto P_{\\text{O}_2}^{-1/6}, \\quad n = [e'] \\propto P_{\\text{O}_2}^{-1/6}
\\]
Conductivity scales inversely with oxygen pressure as $P_{\\text{O}_2}^{-1/6}$ (**$n$-type semiconductor**)."""
            },
            {
                "secNumber": "8.6",
                "title": "Color Centers & Trapped Electrons: The F-Center & Mollwo-Ivey Relation",
                "content": r"""When an alkali halide crystal (e.g., colorless $\\text{NaCl}$) is heated in an excess alkali metal vapor (e.g., sodium vapor) and rapidly quenched, it develops intense coloration (yellow for $\\text{NaCl}$, violet for $\\text{KCl}$, blue for $\\text{KBr}$). This is caused by the formation of an **F-center** (*Farbzentrum*, German for color center).

### Microscopic Architecture of an F-Center
1. Gaseous sodium atoms deposit on the crystal surface:
\\[
\\text{Na}(g) \\rightleftharpoons \\text{Na}_{\\text{Na}}^\\times + \\text{V}_{\\text{Cl}}^\\bullet + e'
\\]
2. The sodium atom ionizes to $\\text{Na}^+$, incorporating into the cation lattice and creating an empty chloride vacancy ($\\text{V}_{\\text{Cl}}^\\bullet$).
3. The liberated electron diffuses rapidly into the crystal bulk and is captured by the electrostatic potential well of the positive anion vacancy:
\\[
\\text{V}_{\\text{Cl}}^\\bullet + e' \\rightleftharpoons \\text{V}_{\\text{Cl}}^\\times \\quad (\\text{or } F)
\\]
An F-center is an **electron trapped in an anion vacancy**, surrounded symmetrically by six regular nearest-neighbor cations ($\text{Na}^+$).

### Particle-in-a-Spherical-Box Model & The Mollwo-Ivey Law
The trapped electron behaves quantum mechanically as a particle in a three-dimensional potential well of diameter approximately equal to the lattice parameter $a$.
The ground state is an $s$-like orbital ($1s$), and optical absorption promotes the electron to an excited $p$-like state ($2p$):
\\[
\\Delta E = h\\nu = \\frac{\\hbar^2 \\pi^2}{2m_e^* a^2} \\left(2^2 - 1^2\\right) \\propto \\frac{1}{a^2}
\\]
Empirically, E. Mollwo (1931) and H. Ivey (1947) demonstrated that the optical absorption maximum wavelength $\\lambda_{\\max}$ across all alkali halides follows the power law:
\\[
\\lambda_{\\max} = C a^n \\quad \\text{or} \\quad E_{\\text{abs}} = A a^{-n}
\\]
where $a$ is the cubic lattice parameter and the empirical exponent $n \\approx 1.8 - 2.0$. For example, $\\text{NaCl}$ ($a = 5.64\\text{ Å}$) absorbs at $\\lambda = 465\\text{ nm}$ (blue light absorption, reflecting complementary yellow)."""
            },
            {
                "secNumber": "8.7",
                "title": "Brouwer Defect Diagrams: Partial Pressure Regimes",
                "content": r"""A **Brouwer diagram** (or Kröger-Vink diagram) is a double-logarithmic plot displaying the concentrations of all point defects ($\log [D_j]$) as a continuous function of thermodynamic activity (most commonly $\\log P_{\\text{O}_2}$) at constant temperature.

### Brouwer Approximation Method
The full electroneutrality equation for a metal oxide with vacancies, electrons, and holes is:
\\[
2[\\text{V}_M''] + [e'] = 2[\\text{V}_O^{\\bullet\\bullet}] + [h^\\bullet]
\\]
Because solving this high-order polynomial analytically is cumbersome, G. Brouwer (1954) proposed dividing the diagram into distinct pressure regimes where **only the two largest dominant defect species are balanced**:

1. **Regime I: High Oxygen Partial Pressure (Oxidizing / p-type)**:
   - Dominant neutrality condition: $2[\\text{V}_M''] \\approx [h^\\bullet]$.
   - Defect slopes:
   \\[
   \\log[h^\\bullet] \\propto +\\frac{1}{6} \\log P_{\\text{O}_2}, \\quad \\log[\\text{V}_M''] \\propto +\\frac{1}{6} \\log P_{\\text{O}_2}
   \\]
   - Minority defects: $[e'] \\propto P_{\\text{O}_2}^{-1/6}$, $[\\text{V}_O^{\\bullet\\bullet}] \\propto P_{\\text{O}_2}^{-1/3}$.

2. **Regime II: Intermediate Oxygen Partial Pressure (Stoichiometric / Intrinsic)**:
   - Thermal electronic excitation dominates: $[e'] \\approx [h^\\bullet] = \\sqrt{K_i} = \\text{constant}$ (independent of $P_{\\text{O}_2}$).
   - Or Schottky equilibrium dominates: $[\\text{V}_M''] \\approx [\\text{V}_O^{\\bullet\\bullet}] = \\sqrt{K_S} = \\text{constant}$.

3. **Regime III: Low Oxygen Partial Pressure (Reducing / n-type)**:
   - Dominant neutrality condition: $[e'] \\approx 2[\\text{V}_O^{\\bullet\\bullet}]$.
   - Defect slopes:
   \\[
   \\log[e'] \\propto -\\frac{1}{6} \\log P_{\\text{O}_2}, \\quad \\log[\\text{V}_O^{\\bullet\\bullet}] \\propto -\\frac{1}{6} \\log P_{\\text{O}_2}
   \\]
   - Minority defects: $[h^\\bullet] \\propto P_{\\text{O}_2}^{+1/6}$, $[\\text{V}_M''] \\propto P_{\\text{O}_2}^{-1/3}$.
In each regime, defect concentrations plot as straight lines with rational fractional slopes ($0, \\pm 1/6, \\pm 1/4, \\pm 1/2$)."""
            },
            {
                "secNumber": "8.8",
                "title": "Defect Clustering, Shear Structures & Magnéli Phases",
                "content": r"""When the departure from stoichiometry becomes large ($x > 0.01$), isolated point defects interact electrostatically and elastically, condensing into complex **defect clusters** and **crystallographic shear structures**.

### Defect Clusters in Wüstite (Fe_{1-x}O)
In $\\text{Fe}_{1-x}\\text{O}$ ($0.05 \\le x \\le 0.15$), cation vacancies do not remain randomly dispersed.
- **Roth Clusters (4:1 Cluster)**: Four octahedral $\\text{Fe}^{2+}$ vacancies group together around a central tetrahedral interstitial site occupied by an oxidized $\\text{Fe}^{3+}$ cation.
- **Koch-Cohen Clusters (13:4 Cluster)**: Aggregations of 13 octahedral vacancies and 4 tetrahedral $\\text{Fe}^{3+}$ ions surrounded by relaxed neighboring ions, forming a localized inverse-spinel sub-microdomain (pre-nucleation of magnetite $\\text{Fe}_3\\text{O}_4$).

### Crystallographic Shear (CS) & Magnéli Phases
In early transition metal oxides with high formal oxidation states ($\\text{WO}_3, \\text{TiO}_2, \\text{MoO}_3$), large non-stoichiometry is accommodated without creating point vacancies. Instead, the crystal eliminates entire planes of oxygen atoms through **crystallographic shear (CS)**:
1. Corner-sharing octahedra collapse along a specific crystallographic plane (e.g., $(121)$ or $(132)$ in rutile).
2. The collapsed region slips, transforming corner-sharing octahedra into denser **edge-sharing or face-sharing octahedra**.
3. Periodic recurrence of these shear planes generates discrete homologous series of fully ordered, stoichiometric compounds known as **Magnéli phases**:
   - Titanium oxides: $\\text{Ti}_n\\text{O}_{2n-1}$ ($4 \\le n \\le 10$, e.g., $\\text{Ti}_4\\text{O}_7$).
   - Tungsten oxides: $\\text{W}_n\\text{O}_{3n-1}$ and $\\text{W}_n\\text{O}_{3n-2}$ (e.g., $\\text{W}_{20}\\text{O}_{58}$).
Magnéli phases exhibit high electrical conductivities and chemical inertness, functioning as corrosion-resistant electrocatalyst supports."""
            }
        ],
        "problems": [
            {
                "probNumber": "8.1",
                "title": "Thermodynamic Derivation of Schottky Defect Equilibrium in Rock Salt",
                "difficulty": "Foundational",
                "statement": "In crystalline $\\text{NaCl}$, the formation enthalpy of a Schottky defect pair is $\\Delta H_S = 2.30\\text{ eV}$, and the vibrational entropy contribution is $\\Delta S_{\\text{vib}} = 4.50 k_B$.\\n(a) Derive the equilibrium Schottky defect pair fraction $x_S = n_S/N$ by setting $d\\Delta G/dn_S = 0$.\\n(b) Calculate $x_S$ and the absolute number of Schottky pairs per $\\text{cm}^3$ at $T = 300\\text{ K}$ and near the melting point at $T = 1000\\text{ K}$ (given unit cell volume $V_c = 1.794 \\times 10^{-22}\\text{ cm}^3$ with $Z = 4$).\\n(c) Compute the energy required to form $1\\text{ mol}$ of Schottky pairs.",
                "solution": r"""### Step 1: Equilibrium Defect Fraction Derivation
For an $MX$ crystal with $N$ cation and $N$ anion sites, forming $n_S$ Schottky pairs creates $n_S$ cation vacancies and $n_S$ anion vacancies.
The total Gibbs free energy change is:
\\[
\\Delta G = n_S \\Delta H_S - T \\left[ n_S \\Delta S_{\\text{vib}} + 2 k_B \\left( N\\ln N - (N - n_S)\\ln(N - n_S) - n_S\\ln n_S \\right) \\right]
\\]
Minimizing with respect to $n_S$:
\\[
\\frac{\\partial \\Delta G}{\\partial n_S} = \\Delta H_S - T \\Delta S_{\\text{vib}} - 2 k_B T \\ln\\left(\\frac{N - n_S}{n_S}\\right) = 0
\\]
For $n_S \\ll N$, $\\frac{N - n_S}{n_S} \\approx \\frac{N}{n_S}$:
\\[
2 k_B T \\ln\\left(\\frac{N}{n_S}\\right) = \\Delta H_S - T \\Delta S_{\\text{vib}}
\\]
\\[
\\ln\\left(\\frac{n_S}{N}\\right) = \\frac{\\Delta S_{\\text{vib}}}{2 k_B} - \\frac{\\Delta H_S}{2 k_B T}
\\]
\\[
x_S = \\frac{n_S}{N} = \\exp\\left(\\frac{\\Delta S_{\\text{vib}}}{2 k_B}\\right) \\exp\\left(-\\frac{\\Delta H_S}{2 k_B T}\\right)
\\]

### Step 2: Numerical Calculations
Given $\\Delta S_{\\text{vib}} = 4.50 k_B$:
\\[
\\exp\\left(\\frac{\\Delta S_{\\text{vib}}}{2 k_B}\\right) = \\exp(2.25) = 9.4877
\\]
Number of cation sites per $\\text{cm}^3$:
\\[
N = \\frac{4}{1.794 \\times 10^{-22}\\text{ cm}^3} = 2.230 \\times 10^{22}\\text{ cm}^{-3}
\\]

1. **At $T = 300\\text{ K}$**:
   $k_B T = 0.025852\\text{ eV}$.
   \\[
   \\frac{\\Delta H_S}{2 k_B T} = \\frac{2.30\\text{ eV}}{2(0.025852\\text{ eV})} = 44.484
   \\]
   \\[
   x_S = 9.4877 \\times \\exp(-44.484) = 9.4877 \\times 4.795 \\times 10^{-20} = 4.55 \\times 10^{-19}
   \\]
   Number of defects per $\\text{cm}^3$:
   \\[
   n_S = x_S N = (4.55 \\times 10^{-19})(2.230 \\times 10^{22}\\text{ cm}^{-3}) = 1.01 \\times 10^4\\text{ cm}^{-3}
   \\]
   (Practically zero intrinsic defects at room temperature).

2. **At $T = 1000\\text{ K}$**:
   $k_B T = 8.6173 \\times 10^{-5} \\times 1000 = 0.086173\\text{ eV}$.
   \\[
   \\frac{\\Delta H_S}{2 k_B T} = \\frac{2.30\\text{ eV}}{2(0.086173\\text{ eV})} = 13.345
   \\]
   \\[
   x_S = 9.4877 \\times \\exp(-13.345) = 9.4877 \\times 1.6008 \\times 10^{-6} = 1.519 \\times 10^{-5}
   \\]
   Number of defects per $\\text{cm}^3$:
   \\[
   n_S = (1.519 \\times 10^{-5})(2.230 \\times 10^{22}\\text{ cm}^{-3}) = 3.39 \\times 10^{17}\\text{ cm}^{-3}
   \\]

### Step 3: Molar Enthalpy of Defect Formation
For $1\\text{ mol}$ of Schottky pairs ($N_A = 6.02214 \\times 10^{23}$ pairs):
\\[
\\Delta H_{\\text{molar}} = N_A \\Delta H_S = (6.02214 \\times 10^{23})(2.30\\text{ eV} \\times 1.60218 \\times 10^{-19}\\text{ J/eV}) = 2.219 \\times 10^5\\text{ J/mol} = 221.9\\text{ kJ/mol}
\\]"""
            },
            {
                "probNumber": "8.2",
                "title": "Thermodynamic Derivation of Frenkel Defect Concentration in AgBr",
                "difficulty": "Foundational",
                "statement": "In silver bromide ($\\text{AgBr}$, rock salt structure), Frenkel defects on the $\\text{Ag}^+$ sublattice dominate. The enthalpy of Frenkel defect formation is $\\Delta H_F = 1.16\\text{ eV}$. There are two tetrahedral interstitial sites per silver lattice site ($N_i/N = 2$).\\n(a) Write the equilibrium expression for the cation Frenkel defect fraction $x_F = n_F/N$.\\n(b) At $T = 500\\text{ K}$, compute the fraction $x_F$ (neglecting vibrational entropy).\\n(c) If the electrical conductivity of $\\text{AgBr}$ is $\\sigma = n_F e (\\mu_v + \\mu_i)$ with interstitial mobility $\\mu_i = 1.2 \\times 10^{-2}\\text{ cm}^2/(\\text{V}\\cdot\\text{s})$ and vacancy mobility $\\mu_v = 1.8 \\times 10^{-3}\\text{ cm}^2/(\\text{V}\\cdot\\text{s})$, calculate $\\sigma$ at $500\\text{ K}$ (given $N = 2.10 \\times 10^{22}\\text{ cm}^{-3}$).",
                "solution": r"""### Step 1: Equilibrium Frenkel Defect Expression
Formation of a Frenkel pair:
\\[
\\text{Ag}_{\\text{Ag}}^\\times \\rightleftharpoons \\text{V}_{\\text{Ag}}' + \\text{Ag}_i^\\bullet
\\]
With $N$ regular sites and $N_i = 2N$ interstitial sites:
\\[
W = \\frac{N!}{(N - n_F)!\\, n_F!} \\times \\frac{N_i!}{(N_i - n_F)!\\, n_F!}
\\]
Minimizing the free energy yields:
\\[
n_F = \\sqrt{N N_i} \\exp\\left(-\\frac{\\Delta H_F}{2 k_B T}\\right)
\\]
Dividing by $N$:
\\[
x_F = \\frac{n_F}{N} = \\sqrt{\\frac{N_i}{N}} \\exp\\left(-\\frac{\\Delta H_F}{2 k_B T}\\right) = \\sqrt{2} \\exp\\left(-\\frac{\\Delta H_F}{2 k_B T}\\right)
\\]

### Step 2: Frenkel Fraction at $500\\text{ K}$
At $T = 500\\text{ K}$:
\\[
k_B T = (8.6173 \\times 10^{-5}\\text{ eV/K})(500\\text{ K}) = 0.0430865\\text{ eV}
\\]
The exponential factor:
\\[
\\frac{\\Delta H_F}{2 k_B T} = \\frac{1.16\\text{ eV}}{2(0.0430865\\text{ eV})} = \\frac{1.16}{0.086173} = 13.4613
\\]
\\[
\\exp(-13.4613) = 1.4251 \\times 10^{-6}
\\]
The defect fraction is:
\\[
x_F = \\sqrt{2} \\times 1.4251 \\times 10^{-6} = 1.41421 \\times 1.4251 \\times 10^{-6} = 2.015 \\times 10^{-6}
\\]
The defect concentration is:
\\[
n_F = x_F N = (2.015 \\times 10^{-6})(2.10 \\times 10^{22}\\text{ cm}^{-3}) = 4.232 \\times 10^{16}\\text{ cm}^{-3}
\\]

### Step 3: Ionic Conductivity Calculation
Both interstitial silver ions and silver vacancies contribute to charge transport:
\\[
\\sigma = n_F e (\\mu_i + \\mu_v)
\\]
Total mobility:
\\[
\\mu_{\\text{total}} = 1.2 \\times 10^{-2} + 1.8 \\times 10^{-3} = 1.38 \\times 10^{-2}\\text{ cm}^2/(\\text{V}\\cdot\\text{s})
\\]
Conductivity:
\\[
\\sigma = (4.232 \\times 10^{16}\\text{ cm}^{-3})(1.60218 \\times 10^{-19}\\text{ C})(1.38 \\times 10^{-2}\\text{ cm}^2/(\\text{V}\\cdot\\text{s}))
\\]
\\[
\\sigma = (6.780 \\times 10^{-3}) \\times (1.38 \\times 10^{-2}) = 9.36 \\times 10^{-5}\\text{ S/cm} = 9.36 \\times 10^{-3}\\text{ S/m}
\\]"""
            },
            {
                "probNumber": "8.3",
                "title": "Writing Balanced Kröger-Vink Defect Reactions for Dopants in ZrO2 and NaCl",
                "difficulty": "Intermediate",
                "statement": "Write fully balanced Kröger-Vink defect reactions (conserving mass, charge, and lattice site ratio) for the following solid-state incorporation processes:\\n(a) Dissolution of yttrium oxide ($\\text{Y}_2\\text{O}_3$) into zirconia ($\\text{ZrO}_2$) to create oxygen vacancies for fast-ion transport (YSZ).\\n(b) Dissolution of calcium chloride ($\\text{CaCl}_2$) into rock-salt $\\text{NaCl}$.\\n(c) Dissolution of alumina ($\\text{Al}_2\\text{O}_3$) into magnesium oxide ($\\text{MgO}$).",
                "solution": r"""### Step 1: Incorporation of $\\text{Y}_2\\text{O}_3$ into $\\text{ZrO}_2$
- Host lattice: $\\text{ZrO}_2$ has a site ratio of $1\\text{ cation site} : 2\\text{ anion sites}$.
- Solute: $\\text{Y}_2\\text{O}_3$ has $2\\text{ Y}^{3+}$ and $3\\text{ O}^{2-}$.
- Substituting $\\text{Y}^{3+}$ for $\\text{Zr}^{4+}$ creates effective negative charge: $\\text{Y}_{\\text{Zr}}'$.
- To maintain the $1:2$ site ratio, $2\\text{ Y}$ atoms require $2$ cation sites, which must be accompanied by $4$ anion sites in $\\text{ZrO}_2$.
- Since $\\text{Y}_2\\text{O}_3$ provides only $3$ oxygen atoms, the fourth anion site remains empty, forming an oxygen vacancy $\\text{V}_O^{\\bullet\\bullet}$:
\\[
\\text{Y}_2\\text{O}_3 \\xrightarrow{\\text{ZrO}_2} 2\\text{Y}_{\\text{Zr}}' + 3\\text{O}_O^\\times + \\text{V}_O^{\\bullet\\bullet}
\\]
- **Verification**:
  - Mass: $2\\text{ Y}$, $3\\text{ O}$ on both sides.
  - Sites: $2$ cation sites ($\\text{Zr}$) and $3+1 = 4$ anion sites ($\\text{O}$); ratio $2:4 = 1:2$.
  - Charge: $2(-1) + 3(0) + (+2) = 0$. Completely balanced!

### Step 2: Incorporation of $\\text{CaCl}_2$ into $\\text{NaCl}$
- Host lattice: $\\text{NaCl}$ has a $1:1$ site ratio.
- Solute: $\\text{CaCl}_2$ contains $1\\text{ Ca}^{2+}$ and $2\\text{ Cl}^-$.
- Substituting $\\text{Ca}^{2+}$ for $\\text{Na}^+$ creates effective positive charge: $\\text{Ca}_{\\text{Na}}^\\bullet$.
- Incorporating $2\\text{ Cl}^-$ requires $2$ anion sites, which mandates $2$ cation sites in $\\text{NaCl}$.
- Since only $1\\text{ Ca}^{2+}$ is added, the second cation site remains empty, forming a sodium vacancy $\\text{V}_{\\text{Na}}'$:
\\[
\\text{CaCl}_2 \\xrightarrow{\\text{NaCl}} \\text{Ca}_{\\text{Na}}^\\bullet + \\text{V}_{\\text{Na}}' + 2\\text{Cl}_{\\text{Cl}}^\\times
\\]
- **Verification**:
  - Mass: $1\\text{ Ca}$, $2\\text{ Cl}$ balanced.
  - Sites: $2$ cation sites ($\text{Na}$), $2$ anion sites ($\text{Cl}$); ratio $1:1$.
  - Charge: $(+1) + (-1) + 2(0) = 0$. Perfectly balanced!

### Step 3: Incorporation of $\\text{Al}_2\\text{O}_3$ into $\\text{MgO}$
- Host lattice: $\\text{MgO}$ has a $1:1$ site ratio.
- Solute: $\\text{Al}_2\\text{O}_3$ contains $2\\text{ Al}^{3+}$ and $3\\text{ O}^{2-}$.
- Substituting $\\text{Al}^{3+}$ on $\\text{Mg}^{2+}$ gives $\\text{Al}_{\\text{Mg}}^\\bullet$.
- The $3\\text{ O}^{2-}$ occupy $3$ oxygen sites, requiring $3$ magnesium sites.
- With only $2\\text{ Al}^{3+}$ cations, one magnesium vacancy $\\text{V}_{\\text{Mg}}''$ is created:
\\[
\\text{Al}_2\\text{O}_3 \\xrightarrow{\\text{MgO}} 2\\text{Al}_{\\text{Mg}}^\\bullet + \\text{V}_{\\text{Mg}}'' + 3\\text{O}_O^\\times
\\]
- **Verification**:
  - Mass: $2\\text{ Al}$, $3\\text{ O}$ balanced.
  - Sites: $3$ cation sites ($\text{Mg}$), $3$ anion sites ($\text{O}$); ratio $1:1$.
  - Charge: $2(+1) + (-2) + 3(0) = 0$. Fully balanced!"""
            },
            {
                "probNumber": "8.4",
                "title": "Oxygen Partial Pressure Dependence of Defect Concentrations in Metal-Deficient Fe_{1-x}O",
                "difficulty": "Intermediate",
                "statement": "At high temperatures ($T = 1200\\text{ K}$), wüstite ($\\text{Fe}_{1-x}\\text{O}$) incorporates oxygen according to:\\n\\[ \\frac{1}{2}\\text{O}_2(g) \\rightleftharpoons \\text{O}_O^\\times + \\text{V}_{\\text{Fe}}'' + 2h^\\bullet \\]\\n(a) Write the equilibrium constant $K_{\\text{ox}}$ for this reaction.\\n(b) Using the electroneutrality condition $[h^\\bullet] = 2[\\text{V}_{\\text{Fe}}'']$, prove that the concentration of cation vacancies and the electrical conductivity vary as $P_{\\text{O}_2}^{1/6}$.\\n(c) If the non-stoichiometry parameter $x$ increases from $0.050$ at $P_{\\text{O}_2} = 10^{-12}\\text{ atm}$ to $x_2$ when the oxygen partial pressure is raised to $P_{\\text{O}_2} = 10^{-6}\\text{ atm}$, compute $x_2$.",
                "solution": r"""### Step 1: Equilibrium Constant Expression
Applying the law of mass action to the defect reaction:
\\[
K_{\\text{ox}} = \\frac{[\\text{O}_O^\\times] [\\text{V}_{\\text{Fe}}''] [h^\\bullet]^2}{P_{\\text{O}_2}^{1/2}}
\\]
Since oxygen sites are virtually fully occupied, $[\\text{O}_O^\\times] \\approx 1$ (activity of lattice host $= 1$):
\\[
K_{\\text{ox}} = [\\text{V}_{\\text{Fe}}''] [h^\\bullet]^2 P_{\\text{O}_2}^{-1/2}
\\]

### Step 2: Proof of $P_{\\text{O}_2}^{1/6}$ Scaling
Charge neutrality requires:
\\[
[h^\\bullet] = 2[\\text{V}_{\\text{Fe}}'']
\\]
Substitute this into the equilibrium expression:
\\[
K_{\\text{ox}} = [\\text{V}_{\\text{Fe}}''] \\left(2[\\text{V}_{\\text{Fe}}'']\\right)^2 P_{\\text{O}_2}^{-1/2} = 4 [\\text{V}_{\\text{Fe}}'']^3 P_{\\text{O}_2}^{-1/2}
\\]
Solving for $[\\text{V}_{\\text{Fe}}'']$:
\\[
[\\text{V}_{\\text{Fe}}'']^3 = \\frac{K_{\\text{ox}}}{4} P_{\\text{O}_2}^{1/2}
\\]
Taking the cube root of both sides:
\\[
[\\text{V}_{\\text{Fe}}''] = \\left(\\frac{K_{\\text{ox}}}{4}\\right)^{1/3} P_{\\text{O}_2}^{1/6} \\propto P_{\\text{O}_2}^{1/6}
\\]
Since $[h^\\bullet] = 2[\\text{V}_{\\text{Fe}}'']$, the hole concentration also scales as $P_{\\text{O}_2}^{1/6}$.
The electrical conductivity $\\sigma = p e \\mu_h = [h^\\bullet] e \\mu_h$ is directly proportional to $[h^\\bullet]$, hence:
\\[
\\sigma \\propto P_{\\text{O}_2}^{1/6}
\\]

### Step 3: Calculation of Non-Stoichiometry Parameter $x_2$
The non-stoichiometry parameter $x$ in $\\text{Fe}_{1-x}\\text{O}$ equals the fractional concentration of iron vacancies: $x = [\\text{V}_{\\text{Fe}}'']$.
Using the scaling relation:
\\[
\\frac{x_2}{x_1} = \\left( \\frac{P_{\\text{O}_2, 2}}{P_{\\text{O}_2, 1}} \\right)^{1/6}
\\]
Given $x_1 = 0.050$, $P_{\\text{O}_2, 1} = 10^{-12}\\text{ atm}$, and $P_{\\text{O}_2, 2} = 10^{-6}\\text{ atm}$:
\\[
\\frac{P_{\\text{O}_2, 2}}{P_{\\text{O}_2, 1}} = \\frac{10^{-6}}{10^{-12}} = 10^6
\\]
\\[
\\left(10^6\\right)^{1/6} = 10^1 = 10.0
\\]
Therefore:
\\[
x_2 = 10.0 \\times x_1 = 10.0 \\times 0.050 = 0.50
\\]
*(Note: In reality, wüstite disproportionates to $\\text{Fe}_3\\text{O}_4$ before reaching $x = 0.50$, as the phase field terminates near $x \\approx 0.15$).*"""
            },
            {
                "probNumber": "8.5",
                "title": "Derivation of Defect Concentrations in Zinc Oxide (ZnO) as a Function of Oxygen Pressure",
                "difficulty": "Intermediate",
                "statement": "Zinc oxide is an $n$-type semiconductor due to oxygen deficiency. At high temperatures, reduction occurs via:\\n\\[ \\text{O}_O^\\times \\rightleftharpoons \\frac{1}{2}\\text{O}_2(g) + \\text{V}_O^{\\bullet\\bullet} + 2e' \\]\\n(a) Formulate the mass-action equation and find the power-law exponent $m$ in $[e'] \\propto P_{\\text{O}_2}^m$.\\n(b) If instead oxygen vacancies are singly ionized ($\\text{V}_O^\\bullet$), derive the new scaling exponent $m$.\\n(c) An experimental measurement of electrical conductivity in a $\\text{ZnO}$ single crystal yields $\\sigma \\propto P_{\\text{O}_2}^{-1/4}$. Which defect model (singly vs doubly ionized vacancy or interstitial zinc) is consistent with this observation?",
                "solution": r"""### Step 1: Doubly Ionized Vacancy Model
The equilibrium constant for doubly ionized vacancies is:
\\[
K_1 = [\\text{V}_O^{\\bullet\\bullet}] [e']^2 P_{\\text{O}_2}^{1/2}
\\]
The electroneutrality condition is $[e'] = 2[\\text{V}_O^{\\bullet\\bullet}] \\implies [\\text{V}_O^{\\bullet\\bullet}] = \\frac{1}{2}[e']$.
Substitute into $K_1$:
\\[
K_1 = \\left(\\frac{1}{2}[e']\\right) [e']^2 P_{\\text{O}_2}^{1/2} = \\frac{1}{2} [e']^3 P_{\\text{O}_2}^{1/2}
\\]
\\[
[e']^3 = 2 K_1 P_{\\text{O}_2}^{-1/2} \\implies [e'] = (2K_1)^{1/3} P_{\\text{O}_2}^{-1/6}
\\]
Exponent: $m = -1/6$.

### Step 2: Singly Ionized Vacancy Model
For singly ionized oxygen vacancies:
\\[
\\text{O}_O^\\times \\rightleftharpoons \\frac{1}{2}\\text{O}_2(g) + \\text{V}_O^\\bullet + e'
\\]
Equilibrium constant:
\\[
K_2 = [\\text{V}_O^\\bullet] [e'] P_{\\text{O}_2}^{1/2}
\\]
Electroneutrality: $[e'] = [\\text{V}_O^\\bullet]$.
Substitute into $K_2$:
\\[
K_2 = [e']^2 P_{\\text{O}_2}^{1/2} \\implies [e']^2 = K_2 P_{\\text{O}_2}^{-1/2}
\\]
\\[
[e'] = K_2^{1/2} P_{\\text{O}_2}^{-1/4}
\\]
Exponent: $m = -1/4$.

### Step 3: Analysis of Experimental Data
The experimental conductivity scales as $\\sigma \\propto P_{\\text{O}_2}^{-1/4}$.
Since $\\sigma = n e \\mu_e = [e'] e \\mu_e$:
- The doubly ionized model predicts $m = -1/6$.
- The singly ionized vacancy model ($\text{V}_O^\\bullet$) predicts $m = -1/4$.
- Singly ionized zinc interstitials ($\\text{Zn}_i^\\bullet$) also yield $m = -1/4$ via $\\text{ZnO} \\rightleftharpoons \\text{Zn}_i^\\bullet + e' + \\frac{1}{2}\\text{O}_2(g)$.
Therefore, the observation $\\sigma \\propto P_{\\text{O}_2}^{-1/4}$ definitively rules out doubly ionized vacancies and confirms that **singly ionized defect centers** (either $\\text{V}_O^\\bullet$ or $\\text{Zn}_i^\\bullet$) dominate the defect chemistry."""
            },
            {
                "probNumber": "8.6",
                "title": "Quantum Well Model of an F-Center: Energy Absorption and Mollwo-Ivey Law",
                "difficulty": "Intermediate",
                "statement": "An F-center can be modeled as an electron in a 3D cubic infinite potential well of side length $L = a/\\sqrt{2}$, where $a$ is the cubic unit cell parameter.\\n(a) Derive the energy of the $1s \\to 2p$ optical transition $\\Delta E = E_{211} - E_{111}$ in terms of $h, m_e^*, L$.\\n(b) Using effective mass $m_e^* = 0.60 m_0$, calculate the theoretical transition energy $\\Delta E$ in $\\text{eV}$ and absorption wavelength $\\lambda$ in $\\text{nm}$ for potassium chloride ($\\text{KCl}$, $a = 6.29\\text{ Å}$).\\n(c) Compare with the experimental absorption band at $\\lambda_{\\text{exp}} = 560\\text{ nm}$ and verify the Mollwo-Ivey scaling relation $\\lambda \\propto a^2$.",
                "solution": r"""### Step 1: Particle-in-a-Box Transition Energy
For a 3D cubic well of width $L$, the energy levels are:
\\[
E(n_x, n_y, n_z) = \\frac{h^2}{8 m_e^* L^2} (n_x^2 + n_y^2 + n_z^2)
\\]
- Ground state ($1s$-like): $(n_x, n_y, n_z) = (1, 1, 1)$.
  \\[
  E_{111} = \\frac{h^2}{8 m_e^* L^2} (1^2 + 1^2 + 1^2) = \\frac{3 h^2}{8 m_e^* L^2}
  \\]
- First excited state ($2p$-like, 3-fold degenerate): $(2, 1, 1), (1, 2, 1), (1, 1, 2)$.
  \\[
  E_{211} = \\frac{h^2}{8 m_e^* L^2} (2^2 + 1^2 + 1^2) = \\frac{6 h^2}{8 m_e^* L^2}
  \\]
The optical absorption energy is:
\\[
\\Delta E = E_{211} - E_{111} = \\frac{3 h^2}{8 m_e^* L^2}
\\]
Since $L = a/\\sqrt{2} \\implies L^2 = a^2/2$:
\\[
\\Delta E = \\frac{3 h^2}{8 m_e^* (a^2/2)} = \\frac{3 h^2}{4 m_e^* a^2}
\\]

### Step 2: Numerical Calculation for KCl
Given $a = 6.29\\text{ Å} = 6.29 \\times 10^{-10}\\text{ m}$, $m_e^* = 0.60 m_0 = 0.60 \\times 9.10938 \\times 10^{-31}\\text{ kg} = 5.4656 \\times 10^{-31}\\text{ kg}$:
\\[
a^2 = (6.29 \\times 10^{-10}\\text{ m})^2 = 3.9564 \\times 10^{-19}\\text{ m}^2
\\]
\\[
h^2 = (6.62607 \\times 10^{-34}\\text{ J}\\cdot\\text{s})^2 = 4.3905 \\times 10^{-67}\\text{ J}^2\\cdot\\text{s}^2
\\]
Numerator:
\\[
3 h^2 = 3 \\times 4.3905 \\times 10^{-67} = 1.3171 \\times 10^{-66}\\text{ J}^2\\cdot\\text{s}^2
\\]
Denominator:
\\[
4 m_e^* a^2 = 4(5.4656 \\times 10^{-31}\\text{ kg})(3.9564 \\times 10^{-19}\\text{ m}^2) = 8.650 \\times 10^{-49}\\text{ kg}\\cdot\\text{m}^2
\\]
Transition energy:
\\[
\\Delta E = \\frac{1.3171 \\times 10^{-66}}{8.650 \\times 10^{-49}} = 1.5227 \\times 10^{-19}\\text{ J}
\\]
Converting to $\\text{eV}$:
\\[
\\Delta E = \\frac{1.5227 \\times 10^{-19}\\text{ J}}{1.60218 \\times 10^{-19}\\text{ J/eV}} = 2.19\\text{ eV}
\\]
Absorption wavelength:
\\[
\\lambda = \\frac{h c}{\\Delta E} = \\frac{1239.84\\text{ eV}\\cdot\\text{nm}}{2.19\\text{ eV}} = 566\\text{ nm}
\\]

### Step 3: Comparison with Experiment and Mollwo-Ivey Law
The calculated value $\\lambda = 566\\text{ nm}$ agrees with the experimental absorption peak $\\lambda_{\\text{exp}} = 560\\text{ nm}$ (error $< 1.1\\%$!).
Because $\\Delta E = h c / \\lambda \\propto a^{-2}$, this model predicts:
\\[
\\lambda \\propto a^2
\\]
This provides a rigorous quantum mechanical derivation of the empirical Mollwo-Ivey law ($n \\approx 2.0$). Absorption at $560\\text{ nm}$ removes yellow-green light, giving $\\text{KCl}$ its characteristic violet color."""
            },
            {
                "probNumber": "8.7",
                "title": "Construction and Analysis of a Brouwer Diagram for an Undoped Metal Oxide MO",
                "difficulty": "Advanced",
                "statement": "An undoped divalent metal oxide $MO$ contains Schottky defects and electronic carriers with equilibrium constants: Schottky $K_S = [\\text{V}_M''][\\text{V}_O^{\\bullet\\bullet}] = 10^{-10}$, intrinsic electronic $K_i = n p = 10^{-14}$, and oxidation $K_{\\text{ox}} = [\\text{V}_M''] p^2 P_{\\text{O}_2}^{-1/2} = 10^{-8}$.\\n(a) Determine the boundary oxygen partial pressures $P_1$ and $P_2$ separating the three Brouwer regimes.\\n(b) Write the algebraic formulas and slopes for $\\log[\\text{V}_M'']$, $\\log[\\text{V}_O^{\\bullet\\bullet}]$, $\\log n$, and $\\log p$ versus $\\log P_{\\text{O}_2}$ in all three regimes.\\n(c) Sketch the schematic defect diagram and evaluate all defect concentrations at $P_{\\text{O}_2} = 1\\text{ atm}$.",
                "solution": r"""### Step 1: Determination of Regime Boundaries
The electroneutrality condition is:
\\[
2[\\text{V}_M''] + n = 2[\\text{V}_O^{\\bullet\\bullet}] + p
\\]
Since $K_S = 10^{-10} \\gg K_i = 10^{-14}$, the stoichiometric plateau (Regime II) is dominated by **Schottky equilibrium** rather than intrinsic electronic excitation:
In Regime II:
\\[
[\\text{V}_M''] = [\\text{V}_O^{\\bullet\\bullet}] = \\sqrt{K_S} = \\sqrt{10^{-10}} = 10^{-5}
\\]
Using $K_{\\text{ox}} = [\\text{V}_M''] p^2 P_{\\text{O}_2}^{-1/2} = 10^{-8}$:
\\[
10^{-5} p^2 P_{\\text{O}_2}^{-1/2} = 10^{-8} \\implies p^2 = 10^{-3} P_{\\text{O}_2}^{1/4} \\implies p = 10^{-1.5} P_{\\text{O}_2}^{1/8}
\\]

1. **Upper boundary $P_2$ (Transition to Regime I, Oxidizing)**:
   Regime I begins when hole concentration exceeds the Schottky background: $p = 2[\\text{V}_M''] = 2 \\times 10^{-5}$:
   \\[
   10^{-1.5} P_2^{1/8} = 2 \\times 10^{-5} \\implies P_2^{1/8} = 2 \\times 10^{-3.5} = 6.325 \\times 10^{-4}
   \\]
   \\[
   P_2 = (6.325 \\times 10^{-4})^8 \\approx 2.5 \\times 10^{-26}\\text{ atm}
   \\]

### Step 2: Slopes in the Three Regimes
1. **Regime I ($P_{\\text{O}_2} > P_2$, Oxidizing)**:
   - Neutrality: $p = 2[\\text{V}_M'']$.
   - $K_{\\text{ox}} = [\\text{V}_M''](2[\\text{V}_M''])^2 P_{\\text{O}_2}^{-1/2} = 4[\\text{V}_M'']^3 P_{\\text{O}_2}^{-1/2} \\implies [\\text{V}_M''] \\propto P_{\\text{O}_2}^{1/6}$, slope $= +1/6$.
   - $p \\propto P_{\\text{O}_2}^{1/6}$, slope $= +1/6$.
   - $n = K_i / p \\propto P_{\\text{O}_2}^{-1/6}$, slope $= -1/6$.
   - $[\\text{V}_O^{\\bullet\\bullet}] = K_S / [\\text{V}_M''] \\propto P_{\\text{O}_2}^{-1/6}$, slope $= -1/6$.

2. **Regime II ($P_1 < P_{\\text{O}_2} < P_2$, Stoichiometric)**:
   - Neutrality: $[\\text{V}_M''] = [\\text{V}_O^{\\bullet\\bullet}] = 10^{-5}$ (slope $= 0$).
   - $p = \\left(\\frac{K_{\\text{ox}}}{[\\text{V}_M'']}\\right)^{1/2} P_{\\text{O}_2}^{1/4} \\propto P_{\\text{O}_2}^{1/4}$, slope $= +1/4$.
   - $n = K_i / p \\propto P_{\\text{O}_2}^{-1/4}$, slope $= -1/4$.

3. **Regime III ($P_{\\text{O}_2} < P_1$, Reducing)**:
   - Neutrality: $n = 2[\\text{V}_O^{\\bullet\\bullet}]$.
   - $[\\text{V}_O^{\\bullet\\bullet}] \\propto P_{\\text{O}_2}^{-1/6}$, slope $= -1/6$.
   - $n \\propto P_{\\text{O}_2}^{-1/6}$, slope $= -1/6$.
   - $p \\propto P_{\\text{O}_2}^{+1/6}$, slope $= +1/6$.
   - $[\\text{V}_M''] \\propto P_{\\text{O}_2}^{+1/6}$, slope $= +1/6$.

### Step 3: Evaluation at $P_{\\text{O}_2} = 1\\text{ atm}$
At $1\\text{ atm}$, the system is deep in Regime I:
\\[
[\\text{V}_M''] = \\left(\\frac{K_{\\text{ox}}}{4}\\right)^{1/3} (1)^{1/6} = \\left(\\frac{10^{-8}}{4}\\right)^{1/3} = (2.5 \\times 10^{-9})^{1/3} = 1.357 \\times 10^{-3}
\\]
\\[
p = 2[\\text{V}_M''] = 2(1.357 \\times 10^{-3}) = 2.714 \\times 10^{-3}
\\]
\\[
n = \\frac{K_i}{p} = \\frac{10^{-14}}{2.714 \\times 10^{-3}} = 3.685 \\times 10^{-12}
\\]
\\[
[\\text{V}_O^{\\bullet\\bullet}] = \\frac{K_S}{[\\text{V}_M'']} = \\frac{10^{-10}}{1.357 \\times 10^{-3}} = 7.369 \\times 10^{-8}
\\]
The dominant defects are metal vacancies $[\\text{V}_M'']$ and holes $p$, confirming strong $p$-type semiconducting character."""
            },
            {
                "probNumber": "8.8",
                "title": "Non-Stoichiometry and Cation Vacancy Fraction in Wüstite (Fe_{0.92}O)",
                "difficulty": "Intermediate",
                "statement": "A sample of non-stoichiometric wüstite has chemical formula $\\text{Fe}_{0.920}\\text{O}$.\\n(a) Determine the fractions of total iron atoms that exist as $\\text{Fe}^{2+}$ and $\\text{Fe}^{3+}$.\\n(b) If the crystal maintains an FCC rock-salt oxygen sublattice with lattice parameter $a = 4.305\\text{ Å}$, calculate the theoretical X-ray crystal density $\\rho_{\\text{calc}}$ accounting for cation vacancies ($M_{\\text{Fe}} = 55.845\\text{ g/mol}, M_{\\text{O}} = 15.999\\text{ g/mol}$).\\n(c) Compare this density with the hypothetical stoichiometric $\\text{FeO}$ lattice having identical lattice parameter.",
                "solution": r"""### Step 1: Oxidation State Distribution
Let the total number of oxygen atoms be $1.000$ (charge $=-2.000$).
Let the fraction of $\\text{Fe}^{3+}$ per formula unit be $y$, so the fraction of $\\text{Fe}^{2+}$ is $0.920 - y$.
Charge neutrality requires:
\\[
2(0.920 - y) + 3y = 2.000
\\]
\\[
1.840 - 2y + 3y = 2.000 \\implies 1.840 + y = 2.000 \\implies y = 0.160
\\]
Thus:
- Concentration of $\\text{Fe}^{3+}$: $0.160$ per formula unit.
- Concentration of $\\text{Fe}^{2+}$: $0.920 - 0.160 = 0.760$ per formula unit.
Fraction of iron atoms in the $+3$ oxidation state:
\\[
f(\\text{Fe}^{3+}) = \\frac{0.160}{0.920} = 0.1739 = 17.39\\%
\\]
Fraction of iron atoms in the $+2$ oxidation state:
\\[
f(\\text{Fe}^{2+}) = \\frac{0.760}{0.920} = 0.8261 = 82.61\\%
\\]

### Step 2: Theoretical Density Calculation
For non-stoichiometric wüstite, the unit cell contains $Z = 4$ oxygen atoms and $4 \\times 0.920 = 3.680$ iron atoms.
Total mass of the unit cell contents:
\\[
M_{\\text{cell}} = 4 M_{\\text{O}} + 3.680 M_{\\text{Fe}} = 4(15.999) + 3.680(55.845) = 63.996 + 205.510 = 269.506\\text{ g/mol}
\\]
Unit cell volume:
\\[
V_c = a^3 = (4.305 \\times 10^{-8}\\text{ cm})^3 = 7.9785 \\times 10^{-23}\\text{ cm}^3
\\]
Density:
\\[
\\rho_{\\text{calc}} = \\frac{M_{\\text{cell}}}{N_A V_c} = \\frac{269.506\\text{ g/mol}}{(6.02214 \\times 10^{23}\\text{ mol}^{-1})(7.9785 \\times 10^{-23}\\text{ cm}^3)} = \\frac{269.506}{48.047} = 5.609\\text{ g/cm}^3
\\]

### Step 3: Comparison with Stoichiometric FeO
For hypothetical stoichiometric $\\text{FeO}$ ($4\\text{ Fe}$ and $4\\text{ O}$):
\\[
M_{\\text{cell, stoich}} = 4(55.845 + 15.999) = 4(71.844) = 287.376\\text{ g/mol}
\\]
Density:
\\[
\\rho_{\\text{stoich}} = \\frac{287.376}{48.047} = 5.981\\text{ g/cm}^3
\\]
Density difference:
\\[
\\Delta \\rho = 5.609 - 5.981 = -0.372\\text{ g/cm}^3 \\quad (-6.22\\%)
\\]
The presence of $8.0\\%$ cation vacancies measurably reduces the crystal density by over $6\\%$, which historically provided definitive experimental proof that wüstite contains cation vacancies rather than anion interstitials."""
            },
            {
                "probNumber": "8.9",
                "title": "Defect Associative Equilibria: Schottky Pair Neutral Dipole Association Free Energy",
                "difficulty": "Advanced",
                "statement": "At moderate temperatures in $\\text{NaCl}$, oppositely charged cation vacancies $\\text{V}_{\\text{Na}}'$ and anion vacancies $\\text{V}_{\\text{Cl}}^\\bullet$ associate to form neutral bound vacancy dipoles $(\\text{V}_{\\text{Na}}\\text{V}_{\\text{Cl}})^\\times$:\\n\\[ \\text{V}_{\\text{Na}}' + \\text{V}_{\\text{Cl}}^\\bullet \\rightleftharpoons (\\text{V}_{\\text{Na}}\\text{V}_{\\text{Cl}})^\\times \\]\\n(a) Formulate the binding energy $\\Delta H_b$ from Coulomb's law using dielectric constant $\\varepsilon_r = 5.90$ and nearest-neighbor distance $d = a/2 = 2.82\\text{ Å}$.\\n(b) Using configurational entropy arguments, derive the association equilibrium constant $K_{\\text{assoc}} = z \\exp(-\\Delta G_b/k_B T)$ where $z = 6$ is the coordination number.\\n(c) At $T = 600\\text{ K}$, if isolated vacancy concentrations are $[\\text{V}_{\\text{Na}}'] = [\\text{V}_{\\text{Cl}}^\\bullet] = 1.0 \\times 10^{-6}$, calculate the bound dipole concentration $[(\\text{V}_{\\text{Na}}\\text{V}_{\\text{Cl}})^\\times]$ and determine the fraction of vacancies that are bound.",
                "solution": r"""### Step 1: Coulombic Binding Enthalpy
The electrostatic attraction between a singly negatively charged cation vacancy and a singly positively charged anion vacancy separated by distance $d = 2.82\\text{ Å}$ in a medium of static dielectric constant $\\varepsilon_r = 5.90$ is:
\\[
\\Delta H_b = -\\frac{e^2}{4\\pi \\varepsilon_0 \\varepsilon_r d}
\\]
Evaluating:
\\[
\\frac{e^2}{4\\pi \\varepsilon_0} = 14.3996\\text{ eV}\\cdot\\text{Å}
\\]
\\[
\\Delta H_b = -\\frac{14.3996\\text{ eV}\\cdot\\text{Å}}{(5.90)(2.82\\text{ Å})} = -\\frac{14.3996}{16.638} = -0.8655\\text{ eV}
\\]
The association enthalpy is $\\Delta H_{\\text{assoc}} = -0.866\\text{ eV}$ (binding stabilization).

### Step 2: Association Equilibrium Constant
Let $N$ be regular lattice sites. An anion vacancy adjacent to a cation vacancy can occupy any of $z = 6$ nearest-neighbor octahedral orientations.
The mass action expression for pair association is:
\\[
\\frac{[(\\text{V}_{\\text{Na}}\\text{V}_{\\text{Cl}})^\\times]}{[\\text{V}_{\\text{Na}}'][\\text{V}_{\\text{Cl}}^\\bullet]} = K_{\\text{assoc}} = z \\exp\\left(-\\frac{\\Delta G_{\\text{assoc}}}{k_B T}\\right) = 6 \\exp\\left(+\\frac{|\\Delta H_b|}{k_B T}\\right)
\\]
assuming negligible vibrational entropy change.

### Step 3: Bound Dipole Concentration at $600\\text{ K}$
At $T = 600\\text{ K}$:
\\[
k_B T = (8.6173 \\times 10^{-5}\\text{ eV/K})(600\\text{ K}) = 0.051704\\text{ eV}
\\]
The exponent:
\\[
\\frac{|\\Delta H_b|}{k_B T} = \\frac{0.8655\\text{ eV}}{0.051704\\text{ eV}} = 16.7395
\\]
\\[
\\exp(16.7395) = 1.8615 \\times 10^7
\\]
Equilibrium constant:
\\[
K_{\\text{assoc}} = 6 \\times (1.8615 \\times 10^7) = 1.1169 \\times 10^8
\\]
Given isolated vacancy concentrations $[\\text{V}_{\\text{Na}}'] = [\\text{V}_{\\text{Cl}}^\\bullet] = 1.0 \\times 10^{-6}$:
\\[
[(\\text{V}_{\\text{Na}}\\text{V}_{\\text{Cl}})^\\times] = K_{\\text{assoc}} [\\text{V}_{\\text{Na}}'] [\\text{V}_{\\text{Cl}}^\\bullet] = (1.1169 \\times 10^8)(1.0 \\times 10^{-6})(1.0 \\times 10^{-6}) = 1.117 \\times 10^{-4}
\\]
Fraction of vacancies that are bound:
Total cation vacancies:
\\[
[\\text{V}_{\\text{total}}] = [\\text{V}_{\\text{free}}] + [(\\text{V}_{\\text{Na}}\\text{V}_{\\text{Cl}})^\\times] = 1.0 \\times 10^{-6} + 1.117 \\times 10^{-4} = 1.127 \\times 10^{-4}
\\]
Bound fraction:
\\[
f_{\\text{bound}} = \\frac{1.117 \\times 10^{-4}}{1.127 \\times 10^{-4}} = 0.9911 = 99.11\\%
\\]
Over $99\\%$ of vacancies are bound as neutral vacancy pairs! Because neutral dipoles do not carry net charge, they do not contribute to DC electrical conductivity, though they contribute to dielectric relaxation and tracer self-diffusion."""
            }
        ]
    }
    return u8

if __name__ == '__main__':
    u8 = get_unit_8()
    print("Unit 8 successfully generated:")
    print("Title:", u8["title"])
    print("Sections:", len(u8["sections"]))
    print("Problems:", len(u8["problems"]))
