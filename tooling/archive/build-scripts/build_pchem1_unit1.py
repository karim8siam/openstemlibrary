# -*- coding: utf-8 -*-
"""
build_pchem1_unit1.py
Unit 1: Foundations of Matter, Measurements, Dimensional Analysis & Physical Properties
Exhaustive honors-level master digital textbook module with 3x depth,
complete mathematical derivations, and zero course numbers.
"""

def get_unit1():
    return {
        "number": 1,
        "title": "Foundations of Matter, Measurements, Dimensional Analysis & Physical Properties",
        "leadSummary": "Fundamental ontological and epistemological foundations of physical chemistry: classification and macroscopic behavior of matter, strict differentiation between extensive and intensive thermodynamic state variables via Euler's theorem on homogeneous functions, the 2019 SI redefinition anchored to invariant physical constants (c, h, e, k_B, N_A), rigorous Gaussian uncertainty propagation and significant figure calculus, the Buckingham Pi theorem of dimensional analysis, and macroscopic criteria governing states of matter from crystalline lattices to supercritical fluids.",
        "sections": [
            {
                "secNumber": "1.1",
                "title": "Matter, Classification & Physical vs Chemical Properties",
                "content": r"""Physical chemistry begins with the rigorous characterization of matter—defined classically as anything that possesses rest mass and occupies space, and relativistically as quantized field excitations possessing localized energy-momentum tensors $T^{\mu\nu}$. At the macroscopic phenomenological level, physical chemists categorize matter into distinct hierarchical taxa: pure substances and mixtures, each governed by exact thermodynamic criteria.

### Macroscopic vs Microscopic Ontologies

A **pure substance** is a thermodynamic sample consisting of an invariant chemical composition and uniform intrinsic properties throughout its spatial domain. Pure substances divide strictly into:
1. **Elements**: Substances composed of atoms having identical nuclear atomic numbers $Z$ (the net positive charge of the atomic nucleus). While classical chemistry defined elements as chemically indivisible, modern quantum chemistry defines an element by the degeneracy of its nuclear proton number $Z \in \{1, 2, \dots, 118\}$. Elements may exhibit **allotropy**—the existence of two or more distinct structural or molecular bonding topologies in the same physical state under identical or varied thermodynamic conditions. Carbon, for instance, exhibits dramatically disparate macroscopic properties across its allotropes: the tetrahedral $sp^3$-hybridized diamond network ($E_g \approx 5.47\text{ eV}$, Mohs hardness 10, thermal conductivity $\kappa \approx 2200\text{ W}/(\text{m}\cdot\text{K})$), the planar $sp^2$-hybridized graphene and graphite sheets with delocalized $\pi$-electron semimetallic conductivity, fullerenes ($C_{60}, C_{70}$), and carbon nanotubes.
2. **Compounds**: Substances composed of two or more distinct elements chemically combined in fixed, stoichiometric mass ratios governed by Proust's Law of Definite Proportions and Dalton's Law of Multiple Proportions. In quantum chemical terminology, a compound is stabilized by electronic bonding minima wherein the total electronic energy $E_{mol}(\mathbf{R})$ evaluated on the Born-Oppenheimer potential energy surface possesses a bound minimum relative to infinitely separated neutral atomic constituents:
$$\Delta E_{bind} = E_{mol}(\mathbf{R}_e) - \sum_{i} E_{atom, i} < 0$$

A **mixture** consists of two or more distinct chemical species physically combined without fixed stoichiometric proportions, retaining their individual chemical identities:
* **Homogeneous Mixtures (Solutions)**: Single-phase macroscopic regimes where composition and physical properties are invariant down to the scale of sub-micrometer sample volumes ($V \gg \xi^3$, where $\xi$ is the molecular correlation length). Examples include gaseous mixtures (e.g., dry tropospheric air), liquid solutions (e.g., completely miscible binary mixtures like ethanol-water or dissolved ionic salts), and solid solutions (e.g., substitutional or interstitial metallic alloys such as brass and austenite).
* **Heterogeneous Mixtures**: Systems exhibiting microscopic or macroscopic phase boundaries across which physical properties, refractive index, density, or chemical potential undergo step-function discontinuities. These include suspensions, emulsions, and colloidal dispersions, where interface thermodynamics and surface free energies $\gamma dA$ dominate system behavior.

### Extensive vs Intensive Thermodynamic Properties

The mathematical foundations of physical chemistry demand an unambiguous differentiation between extensive and intensive properties. 

> **Formal Definition (Euler's Homogeneity Criterion)**:
> Let a thermodynamic system be scaled in size by a positive real parameter $\lambda > 0$ under constant temperature $T$ and pressure $P$. A state variable $X$ is **extensive** if and only if it is a mathematically homogeneous function of degree 1 with respect to the system scale (or component masses/mole numbers $n_i$):
> $$X(\lambda n_1, \lambda n_2, \dots, \lambda n_k) = \lambda^1 X(n_1, n_2, \dots, n_k)$$
> Conversely, a state variable $Y$ is **intensive** if it is a homogeneous function of degree 0 with respect to the system scale:
> $$Y(\lambda n_1, \lambda n_2, \dots, \lambda n_k) = \lambda^0 Y(n_1, n_2, \dots, n_k) = Y(n_1, n_2, \dots, n_k)$$

By Euler's Theorem on Homogeneous Functions, any continuously differentiable function $f(x_1, \dots, x_k)$ that is homogeneous of degree $m$ satisfies the fundamental differential relation:
$$\sum_{i=1}^k x_i \frac{\partial f}{\partial x_i} = m \cdot f(x_1, \dots, x_k)$$

For extensive thermodynamic state functions such as total volume $V$, internal energy $U$, enthalpy $H$, entropy $S$, and Gibbs free energy $G$ (where $m = 1$), Euler's theorem establishes:
$$G(T, P, n_1, \dots, n_k) = \sum_{i=1}^k n_i \left(\frac{\partial G}{\partial n_i}\right)_{T, P, n_{j \neq i}} = \sum_{i=1}^k n_i \mu_i$$
where $\mu_i \equiv \left(\frac{\partial G}{\partial n_i}\right)_{T, P, n_{j \neq i}}$ is the **chemical potential** of species $i$. Because $G$ is homogeneous of degree 1, its partial derivative with respect to an extensive variable ($n_i$) reduces the degree of homogeneity by 1, proving rigorously that **chemical potential $\mu_i$ is strictly an intensive property**:
$$\mu_i(\lambda n_1, \dots, \lambda n_k) = \frac{\partial (\lambda G)}{\partial (\lambda n_i)} = \lambda^0 \mu_i(n_1, \dots, n_k)$$

Table 1.1 summarizes the mathematical classification of physical chemical variables:

| Thermodynamic Variable | Symbol | Homogeneity Degree $m$ | Operational Classification | Fundamental Defining Relation |
|---|---|---|---|---|
| Total Volume | $V$ | 1 | Extensive | $V = \sum n_i \bar{V}_i$ |
| Temperature | $T$ | 0 | Intensive | $T^{-1} = (\partial S / \partial U)_{V, \{n\}}$ |
| Thermodynamic Pressure | $P$ | 0 | Intensive | $P = -(\partial U / \partial V)_{S, \{n\}}$ |
| Total Enthalpy | $H$ | 1 | Extensive | $H = U + PV$ |
| Molar Enthalpy | $H_m$ | 0 | Intensive | $H_m = H / n_{total}$ |
| Chemical Potential | $\mu_i$ | 0 | Intensive | $\mu_i = (\partial G / \partial n_i)_{T, P, n_{j \neq i}}$ |
| Mass Density | $\rho$ | 0 | Intensive | $\rho = m / V = (\lambda^1 m) / (\lambda^1 V)$ |
| Molar Heat Capacity | $C_{p,m}$ | 0 | Intensive | $C_{p,m} = \frac{1}{n}\left(\frac{\partial H}{\partial T}\right)_P$ |
| Surface Tension | $\gamma$ | 0 | Intensive | $\gamma = (\partial G / \partial A)_{T, P, \{n\}}$ |

Any ratio of two extensive properties $X_1 / X_2$ transforms under scaling as $\frac{\lambda X_1}{\lambda X_2} = \lambda^0 \frac{X_1}{X_2}$, demonstrating that **the quotient of any two extensive properties is identically an intensive property**."""
            },
            {
                "secNumber": "1.2",
                "title": "The International System of Units (SI) & Derived Physico-Chemical Quantities",
                "content": r"""Quantitative physical chemistry relies entirely upon unambiguous metrology. On May 20, 2019 (World Metrology Day), the 26th General Conference on Weights and Measures (CGPM) enacted the most profound revolution in the International System of Units (SI) since its inception: **the complete elimination of artifact-based standards** (such as the International Prototype Kilogram cylinder of platinum-iridium kept in Sèvres, France) and the anchoring of the entire SI framework to **seven defining invariant fundamental physical constants**.

### The 2019 SI Metrological Foundation

The seven defining constants are fixed to exact, unvarying numerical values by international consensus:
1. **Hyperfine transition frequency of caesium-133**: $\Delta \nu_{\text{Cs}} = 9\,192\,631\,770\text{ Hz}$ (defines the second, $\text{s}$).
2. **Speed of light in vacuum**: $c = 299\,792\,458\text{ m}\cdot\text{s}^{-1}$ (defines the metre, $\text{m}$).
3. **Planck constant**: $h = 6.626\,070\,15 \times 10^{-34}\text{ J}\cdot\text{s} = 6.626\,070\,15 \times 10^{-34}\text{ kg}\cdot\text{m}^2\cdot\text{s}^{-1}$ (defines the kilogram, $\text{kg}$, via the Kibble balance).
4. **Elementary electric charge**: $e = 1.602\,176\,634 \times 10^{-19}\text{ C} = 1.602\,176\,634 \times 10^{-19}\text{ A}\cdot\text{s}$ (defines the ampere, $\text{A}$).
5. **Boltzmann constant**: $k_B = 1.380\,649 \times 10^{-23}\text{ J}\cdot\text{K}^{-1} = 1.380\,649 \times 10^{-23}\text{ kg}\cdot\text{m}^2\cdot\text{s}^{-2}\cdot\text{K}^{-1}$ (defines the kelvin, $\text{K}$, via acoustic gas thermometry and Johnson noise).
6. **Avogadro constant**: $N_A = 6.022\,140\,76 \times 10^{23}\text{ mol}^{-1}$ (defines the mole, $\text{mol}$).
7. **Luminous efficacy of monochromatic radiation of frequency $540 \times 10^{12}\text{ Hz}$**: $K_{cd} = 683\text{ lm}\cdot\text{W}^{-1}$ (defines the candela, $\text{cd}$).

> **The Redefined Mole and Universal Gas Constant**:
> Historically, the mole was defined as the number of atoms in exactly $0.012\text{ kg}$ of unbound carbon-12 at rest in its ground state. Under the 2019 SI, **one mole contains exactly $6.022\,140\,76 \times 10^{23}$ elementary entities**. 
> As an immediate and monumental consequence for physical chemistry, the **molar gas constant $R$** is now an exact derived constant with zero experimental uncertainty:
> $$R \equiv N_A \cdot k_B = (6.022\,140\,76 \times 10^{23}\text{ mol}^{-1}) \times (1.380\,649 \times 10^{-23}\text{ J}\cdot\text{K}^{-1})$$
> $$R = 8.314\,462\,618\,153\,24\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1} \quad (\text{Exact!})$$
> Similarly, the **Faraday constant $F$** (the electric charge per mole of electrons) is now strictly exact:
> $$F \equiv N_A \cdot e = (6.022\,140\,76 \times 10^{23}\text{ mol}^{-1}) \times (1.602\,176\,634 \times 10^{-19}\text{ C}) = 96\,485.332\,123\,310\,0184\text{ C}\cdot\text{mol}^{-1}$$

### Derived Physical Chemical Units & Interconversions

Physical chemistry routinely operates with non-coherent and derived units born from historical experimental instrumentation. The exact conversion factors connecting them to SI base quantities are:

#### 1. Pressure ($P$)
Pressure is force per unit area, possessing base dimensions $[M L^{-1} T^{-2}]$.
* The coherent SI unit is the **Pascal**: $1\text{ Pa} \equiv 1\text{ N}\cdot\text{m}^{-2} = 1\text{ kg}\cdot\text{m}^{-1}\cdot\text{s}^{-2}$.
* The **bar**: $1\text{ bar} \equiv 10^5\text{ Pa} = 100\text{ kPa} = 0.1\text{ MPa}$ (IUPAC standard state pressure $P^\circ$).
* The **standard atmosphere**: $1\text{ atm} \equiv 101\,325\text{ Pa} = 1.013\,25\text{ bar}$.
* The **Torr** (millimeter of mercury): Defined such that $760\text{ Torr} \equiv 1\text{ atm}$ exactly, yielding:
  $$1\text{ Torr} \equiv \frac{101\,325}{760}\text{ Pa} \approx 133.322\,368\text{ Pa}$$

#### 2. Energy, Work & Heat ($E, w, q$)
Energy has base dimensions $[M L^2 T^{-2}]$.
* The coherent SI unit is the **Joule**: $1\text{ J} \equiv 1\text{ N}\cdot\text{m} = 1\text{ kg}\cdot\text{m}^2\cdot\text{s}^{-2}$.
* The **electronvolt**: $1\text{ eV} \equiv e \times 1\text{ V} = 1.602\,176\,634 \times 10^{-19}\text{ J}$ (per atom/molecule: $1\text{ eV} \approx 96.4853\text{ kJ}\cdot\text{mol}^{-1}$).
* The **thermochemical calorie**: $1\text{ cal}_{th} \equiv 4.184\text{ J}$ exactly.
* The **liter-atmosphere**: $1\text{ L}\cdot\text{atm} = (10^{-3}\text{ m}^3) \times (101\,325\text{ N}\cdot\text{m}^{-2}) = 101.325\text{ J}$.

#### 3. Concentration & Composition Scales
* **Molarity ($C$ or $M$)**: Amount of substance per unit volume of solution: $[C] = \text{mol}\cdot\text{L}^{-1} = 10^3\text{ mol}\cdot\text{m}^{-3}$. Because volume $V(T, P)$ expands or contracts with temperature and pressure, **molarity is temperature-dependent**.
* **Molality ($m$ or $b$)**: Amount of solute per unit mass of solvent: $[m] = \text{mol}\cdot\text{kg}^{-1}$. Because mass is an invariant under thermal expansion, **molality is strictly temperature-independent**, rendering it the mandatory concentration metric for colligative thermodynamics.
* **Mole Fraction ($x_i$)**: Dimensionless ratio $x_i = n_i / \sum_j n_j$, obeying $\sum_i x_i = 1$ identically."""
            },
            {
                "secNumber": "1.3",
                "title": "Scientific Notation, Significant Figures & Propagation of Experimental Uncertainty",
                "content": r"""All empirical measurements in physical chemistry are subject to experimental uncertainty. A reported numerical value without an associated statement of uncertainty or appropriate significant figures is scientifically meaningless.

### Structure of Experimental Error

Experimental uncertainty divides into two orthogonal components:
1. **Systematic Error (Bias)**: Reproducible inaccuracies caused by faulty calibration (e.g., an uncalibrated pH meter or zero-offset on an analytical balance), experimental design flaws, or unmodeled environmental drifts. Systematic errors shift the mean of the data away from the true value, degrading **accuracy**. They cannot be eliminated by repeated trials.
2. **Random Error (Precision)**: Stochastic fluctuations arising from uncontrolled microscopic thermal noise, electrical fluctuations in spectrophotometer detectors, or optical parallax in reading burette meniscus levels. Random errors govern **precision** and are modeled by the **Gaussian (Normal) Probability Density Function**:
$$P(x; \mu, \sigma) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left( -\frac{(x - \mu)^2}{2\sigma^2} \right)$$
where $\mu$ is the population mean and $\sigma$ is the population standard deviation. For a finite sample of $N$ independent measurements $\{x_1, x_2, \dots, x_N\}$, the sample mean $\bar{x}$ and sample standard deviation $s$ are unbiased estimators:
$$\bar{x} = \frac{1}{N}\sum_{i=1}^N x_i, \qquad s = \sqrt{\frac{1}{N-1}\sum_{i=1}^N (x_i - \bar{x})^2}$$
The standard error of the mean (SEM), which quantifies the precision of the estimated mean, scales inversely with the square root of sample size:
$$\sigma_{\bar{x}} = \frac{s}{\sqrt{N}}$$

### The Calculus of Significant Figures

In rapid pencil-and-paper physical chemical calculations where formal Gaussian error propagation is not conducted, **significant figures** provide an operational shorthand for tracking precision:
1. All non-zero digits are significant ($12.38\text{ g}$ has 4 sig figs).
2. Zeros between non-zero digits are significant ($100.08\text{ mL}$ has 5 sig figs).
3. Leading zeros before the first non-zero digit are strictly non-significant; they merely indicate the position of the decimal point ($0.000\,452\text{ mol}$ has 3 sig figs: $4.52 \times 10^{-4}\text{ mol}$).
4. Trailing zeros to the right of a decimal point are significant ($50.00\text{ s}$ has 4 sig figs, signifying measurement down to the hundredth of a second).
5. Exact numbers (integers from counting, stoichiometric coefficients, definitions such as $1\text{ in} = 2.54\text{ cm}$) possess infinite significant figures ($\infty$).

#### Operational Arithmetic Rules:
* **Addition and Subtraction**: The result can have no more digits to the right of the decimal point than the measurement with the fewest digits to the right of the decimal point. For example, adding $12.11\text{ g}$ (two decimals) to $0.0345\text{ g}$ (four decimals) yields $12.1445\text{ g}$, rounded to $12.14\text{ g}$.
* **Multiplication and Division**: The number of significant figures in the final product or quotient is governed by the input value possessing the fewest significant figures. For example, dividing mass $m = 4.502\text{ g}$ (4 sig figs) by volume $V = 2.1\text{ mL}$ (2 sig figs) yields density $\rho = 2.1438\dots\text{ g/mL}$, which must be rounded to $2.1\text{ g/mL}$ (2 sig figs).
* **Logarithms and Antilogarithms**: For $\text{pH} = -\log_{10}[H^+]$, the integer part of the logarithm (the characteristic) indicates only the power of 10 and does **not** count as a significant figure. **Only the digits to the right of the decimal point (the mantissa) are significant.** If $[H^+] = 3.5 \times 10^{-4}\text{ M}$ (2 sig figs), then:
  $$\text{pH} = -\log_{10}(3.5 \times 10^{-4}) = 4 - 0.544\,068 = 3.455\,93 \longrightarrow 3.46 \quad (\text{2 decimal places!})$$

### Rigorous Multivariate Gaussian Uncertainty Propagation

Let a calculated physical chemical quantity $f = f(x_1, x_2, \dots, x_k)$ be a continuously differentiable function of $k$ directly measured independent parameters $x_i$, each having measured standard uncertainty $\sigma_{x_i}$. By performing a multivariable Taylor series expansion of $f$ around the mean coordinates $(\bar{x}_1, \dots, \bar{x}_k)$ and truncating at first order:
$$f(x_1, \dots, x_k) \approx f(\bar{x}_1, \dots, \bar{x}_k) + \sum_{i=1}^k \left(\frac{\partial f}{\partial x_i}\right) (x_i - \bar{x}_i)$$

The variance $\sigma_f^2 = \langle (f - \langle f \rangle)^2 \rangle$ is given rigorously by:
$$\sigma_f^2 = \sum_{i=1}^k \left(\frac{\partial f}{\partial x_i}\right)^2 \sigma_{x_i}^2 + 2\sum_{i=1}^{k-1}\sum_{j=i+1}^k \left(\frac{\partial f}{\partial x_i}\right)\left(\frac{\partial f}{\partial x_j}\right) \sigma_{x_i x_j}$$
where $\sigma_{x_i x_j} = \text{cov}(x_i, x_j) = r_{ij} \sigma_{x_i} \sigma_{x_j}$ is the **covariance** between variables $x_i$ and $x_j$, with $r_{ij} \in [-1, 1]$ being the Pearson correlation coefficient.

> **Uncorrelated Independent Variables ($r_{ij} = 0$)**:
> When measurements are statistically independent, the fundamental error propagation formula reduces to the quadrature sum:
> $$\sigma_f = \sqrt{ \sum_{i=1}^k \left(\frac{\partial f}{\partial x_i}\right)^2 \sigma_{x_i}^2 }$$

Applying this master formula yields exact operational relationships for standard functional forms:
1. **Linear Combinations** $f = a x_1 \pm b x_2$:
   $$\sigma_f = \sqrt{ a^2 \sigma_{x_1}^2 + b^2 \sigma_{x_2}^2 }$$
2. **Power Law Products and Quotients** $f = c \cdot x_1^a x_2^b / x_3^c$:
   Dividing the variance by $f^2$ yields the relative uncertainty formula in fractional form:
   $$\frac{\sigma_f}{|f|} = \sqrt{ a^2 \left(\frac{\sigma_{x_1}}{x_1}\right)^2 + b^2 \left(\frac{\sigma_{x_2}}{x_2}\right)^2 + c^2 \left(\frac{\sigma_{x_3}}{x_3}\right)^2 }$$
3. **Logarithmic Transforms** $f = a \ln(b x)$:
   $$\sigma_f = |a| \frac{\sigma_x}{x}$$
4. **Exponential Transforms** $f = a \exp(b x)$:
   $$\frac{\sigma_f}{|f|} = |b| \sigma_x$$"""
            },
            {
                "secNumber": "1.4",
                "title": "Dimensional Analysis & The Factor-Label Method",
                "content": r"""Dimensional analysis provides one of the most powerful analytical constraints in physical chemistry. Every physically valid equation must be **dimensionally homogeneous**—that is, terms added, subtracted, or equated must possess identically identical base physical dimensions.

### Fundamental Dimensional Bases

In classical physical chemistry, every mechanical and thermodynamic quantity can be decomposed into an irreducible set of fundamental dimensions:
* $[M]$: Mass
* $[L]$: Length
* $[T]$: Time
* $[\Theta]$: Thermodynamic Temperature
* $[N]$: Amount of Substance
* $[I]$: Electric Current

Table 1.2 presents the dimensional spectra of primary physical chemical variables:

| Physical Chemical Quantity | Algebraic Symbol | SI Unit | Dimensional Formula $[M^a L^b T^c \Theta^d N^e I^f]$ |
|---|---|---|---|
| Force | $F$ | $\text{N}$ | $[M L T^{-2}]$ |
| Pressure | $P$ | $\text{Pa}$ | $[M L^{-1} T^{-2}]$ |
| Energy, Enthalpy, Gibbs Free Energy | $U, H, G$ | $\text{J}$ | $[M L^2 T^{-2}]$ |
| Molar Gas Constant | $R$ | $\text{J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}$ | $[M L^2 T^{-2} \Theta^{-1} N^{-1}]$ |
| Viscosity (Dynamic) | $\eta$ | $\text{Pa}\cdot\text{s}$ | $[M L^{-1} T^{-1}]$ |
| Surface Tension | $\gamma$ | $\text{N}\cdot\text{m}^{-1}$ | $[M T^{-2}]$ |
| Diffusion Coefficient | $D$ | $\text{m}^2\cdot\text{s}^{-1}$ | $[L^2 T^{-1}]$ |
| First-Order Rate Constant | $k_1$ | $\text{s}^{-1}$ | $[T^{-1}]$ |
| Second-Order Rate Constant | $k_2$ | $\text{L}\cdot\text{mol}^{-1}\cdot\text{s}^{-1}$ | $[M^{-1} L^3 T^{-1} N^{-1}]$ or $[L^3 T^{-1} N^{-1}]$ |
| Faraday Constant | $F$ | $\text{C}\cdot\text{mol}^{-1}$ | $[T I N^{-1}]$ |

### The Buckingham $\Pi$ Theorem

The formal mathematical foundation of dimensional analysis is formalized by the **Buckingham $\Pi$ Theorem**:

> **Buckingham $\Pi$ Theorem**:
> If a physically meaningful relation involves $n$ dimensional variables:
> $$\Phi(q_1, q_2, \dots, q_n) = 0$$
> and these variables are expressed in terms of $k$ independent fundamental physical dimensions, then the relationship can be re-expressed purely in terms of $p = n - k$ independent **dimensionless groups** $\Pi_1, \Pi_2, \dots, \Pi_p$:
> $$\Psi(\Pi_1, \Pi_2, \dots, \Pi_{n-k}) = 0$$

#### Example: Terminal Fall Velocity of a Solute Particle in Solution
Consider a spherical colloidal particle of radius $r$ and effective buoyant mass density difference $\Delta\rho$ settling under gravitational acceleration $g$ through a viscous liquid of dynamic viscosity $\eta$. The physical variables are $n = 5$:
$$q_1 = v \ ([L T^{-1}]), \quad q_2 = r \ ([L]), \quad q_3 = \Delta\rho \ ([M L^{-3}]), \quad q_4 = g \ ([L T^{-2}]), \quad q_5 = \eta \ ([M L^{-1} T^{-1}])$$
The fundamental dimensions involved are $k = 3$ ($M, L, T$). Thus, there are $n - k = 5 - 3 = 2$ independent dimensionless $\Pi$ groups:
$$\Pi_1 = \frac{v \eta}{r^2 g \Delta\rho}, \qquad \Pi_2 = \text{Re} = \frac{\rho v r}{\eta} \quad (\text{Reynolds number})$$
In the laminar, low-Reynolds-number limit ($\Pi_2 \ll 1$), Stokes' law demands that $\Pi_1$ is an absolute constant:
$$\Pi_1 = \frac{2}{9} \implies v = \frac{2}{9}\frac{r^2 g \Delta\rho}{\eta}$$
Dimensional analysis deduced the functional form of Stokes' settling velocity up to a single dimensionless geometric constant!

### The Factor-Label (Unit-Factor) Conversion Method

In laboratory calculations, the **Factor-Label Method** utilizes conversion ratios whose numerator and denominator represent physically equivalent quantities in disparate units, forming a mathematical factor of unity ($1$):
$$\text{Conversion Factor} = \frac{\text{Quantity in Desired Unit}}{\text{Equivalent Quantity in Given Unit}} = 1$$
Because multiplication by unity preserves the absolute physical value, unit conversion chains can be chained algebraically:
$$\text{Target} = \text{Initial} \times \left(\frac{\text{Unit } B}{\text{Unit } A}\right) \times \left(\frac{\text{Unit } C}{\text{Unit } B}\right) \times \cdots$$

Dimensional analysis serves as an infallible error detector: if algebraic manipulation of units fails to collapse cleanly into the exact dimensional formula of the target physical chemical property, the mathematical derivation is guaranteed to contain an algebraic error."""
            },
            {
                "secNumber": "1.5",
                "title": "States of Matter & Macroscopic Phase Criteria",
                "content": r"""Matter manifests macroscopically in distinct thermodynamic states of aggregation—classically solid, liquid, and gas—and under extreme energetic conditions as plasmas and supercritical fluids. In physical chemistry, these states are distinguished not merely by phenomenological descriptions of shape and volume, but by the quantitative competition between **intermolecular thermal kinetic energy $E_{therm} \sim k_B T$** and **attractive intermolecular potential energy $U_{attr}(r)$**.

### The Microscopic Ordering Hierarchy

Let $u(r)$ be the effective pair potential between two molecules separated by distance $r$, such as the Lennard-Jones 12-6 potential:
$$u(r) = 4\epsilon \left[ \left(\frac{\sigma}{r}\right)^{12} - \left(\frac{\sigma}{r}\right)^6 \right]$$
where $\epsilon$ is the depth of the attractive potential energy well and $\sigma$ is the finite hard-sphere collision diameter where $u(\sigma) = 0$.

1. **The Solid State ($k_B T \ll \epsilon$)**:
   The attractive potential well dominates thermal kinetic agitation. Molecules, atoms, or ions are trapped in deep potential minima, executing small harmonic vibrations around fixed equilibrium lattice sites $\mathbf{R}_{hkl}$. Solids possess **long-range translational and orientational order**, characterized by sharp Bragg diffraction peaks in X-ray crystallography. They exhibit finite shear moduli ($G > 0$) and resist shear deformation elastically.
2. **The Liquid State ($k_B T \approx \epsilon$)**:
   Thermal kinetic energy is comparable in magnitude to the attractive potential well depth. Molecules possess sufficient kinetic energy to overcome localized potential barriers and diffuse through the condensed phase, yielding zero static shear modulus ($G = 0$, fluid flow), but insufficient energy to escape the collective attractive envelope. Liquids possess **short-range order** (extending over 1–3 molecular diameters) but **zero long-range order**. The structural morphology is described quantitatively by the **radial distribution function $g(r)$**:
   $$\rho g(r) = \frac{1}{N} \left\langle \sum_{i=1}^N \sum_{j \neq i}^N \delta(\mathbf{r} - \mathbf{r}_{ij}) \right\rangle$$
   In liquids, $g(r)$ displays sharp first and second coordination shell oscillations that rapidly decay to unity as $r \rightarrow \infty$, reflecting complete macroscopic isotropy.
3. **The Gaseous State ($k_B T \gg \epsilon$)**:
   Thermal kinetic energy completely overwhelms intermolecular attractive potentials. Molecules move along quasi-linear trajectories, interacting only through brief, elastic binary collisions. The mean free path $\lambda \gg \sigma$, the radial distribution function $g(r) \approx 1$ for all $r > \sigma$, and the gas expands spontaneously to fill the entirety of any enclosing volume.
4. **Supercritical Fluids ($T > T_c$ and $P > P_c$)**:
   When a substance is brought beyond its critical temperature $T_c$ and critical pressure $P_c$, the meniscus separating liquid and vapor phases vanishes continuously. The supercritical fluid is a single, homogeneous fluid phase that combines gas-like transport properties (low dynamic viscosity $\eta \sim 10^{-5}\text{ Pa}\cdot\text{s}$, high diffusion coefficients $D \sim 10^{-4}\text{ cm}^2\cdot\text{s}^{-1}$) with liquid-like solvent densities ($\rho \sim 0.2 - 0.9\text{ g}\cdot\text{cm}^{-3}$). Supercritical carbon dioxide ($\text{scCO}_2$, $T_c = 304.13\text{ K} = 30.98^\circ\text{C}$, $P_c = 73.77\text{ bar}$) serves as an essential green industrial solvent for decaffeination, natural product extraction, and dry cleaning without toxic organic solvent waste.

### Thermodynamic Response Functions

The physical response of any state of matter to external thermal and mechanical perturbations is characterized by three fundamental thermodynamic response functions:

1. **Isobaric Thermal Expansion Coefficient ($\alpha_P$)**:
   $$\alpha_P \equiv \frac{1}{V}\left(\frac{\partial V}{\partial T}\right)_P = \left(\frac{\partial \ln V}{\partial T}\right)_P$$
   For an ideal gas ($V = nRT/P$), $\alpha_P = 1/T$. For condensed phases (liquids and solids), $\alpha_P$ is positive and small ($\sim 10^{-5} - 10^{-4}\text{ K}^{-1}$), with anomalous exceptions such as liquid water between $0^\circ\text{C}$ and $3.98^\circ\text{C}$, where open hydrogen-bonded tetrahedral clathrate structures collapse upon heating, yielding negative $\alpha_P < 0$.
2. **Isothermal Compressibility ($\kappa_T$)**:
   $$\kappa_T \equiv -\frac{1}{V}\left(\frac{\partial V}{\partial P}\right)_T = -\left(\frac{\partial \ln V}{\partial P}\right)_T$$
   The negative sign ensures that $\kappa_T > 0$ for all thermodynamically stable systems (mechanical stability criterion: $(\partial P / \partial V)_T < 0$). For an ideal gas, $\kappa_T = 1/P$. For incompressible liquids and solids, $\kappa_T \sim 10^{-10} - 10^{-11}\text{ Pa}^{-1}$.
3. **Thermal Pressure Coefficient ($\gamma_V$)**:
   $$\gamma_V \equiv \left(\frac{\partial P}{\partial T}\right)_V$$
   By the cyclic triple product rule of partial differential calculus:
   $$\left(\frac{\partial V}{\partial T}\right)_P \left(\frac{\partial T}{\partial P}\right)_V \left(\frac{\partial P}{\partial V}\right)_T = -1 \implies \left(\frac{\partial P}{\partial T}\right)_V = -\frac{(\partial V / \partial T)_P}{(\partial V / \partial P)_T} = \frac{\alpha_P}{\kappa_T}$$
   This profound thermodynamic identity allows physical chemists to calculate the colossal internal pressures generated when an isochoric (rigidly confined) liquid or solid is heated, directly from readily measurable laboratory coefficients $\alpha_P$ and $\kappa_T$."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational Level",
                "title": "Stoichiometric Dimensional Analysis & Significant Figure Discipline in Combustion Analysis",
                "statement": r"""A $0.5438\text{ g}$ sample of a pure organic liquid compound containing solely carbon, hydrogen, and oxygen is subjected to complete combustion in an excess stream of pure oxygen inside an analytical combustion train. The combustion effluent passes sequentially through a pre-weighed anhydrous magnesium perchlorate ($\text{Mg}(\text{ClO}_4)_2$) absorption tube, followed by an ascarite-filled ($\text{NaOH}$-coated silica) absorption tube. 

Experimental gravimetric data:
* Mass of water absorbed: $\Delta m(\text{H}_2\text{O}) = 0.3261\text{ g} \pm 0.0002\text{ g}$
* Mass of carbon dioxide absorbed: $\Delta m(\text{CO}_2) = 1.0624\text{ g} \pm 0.0003\text{ g}$

Calculate:
1. The mass percentages of carbon, hydrogen, and oxygen in the compound with correct significant figures.
2. The empirical formula of the compound.
3. If a separate vapor density measurement gives an approximate molar mass $M \approx 90\text{ g}\cdot\text{mol}^{-1}$, establish the exact molecular formula.""",
                "solution": r"""### Step 1: Mass and Moles of Elemental Carbon and Hydrogen

Using high-precision IUPAC standard atomic weights:
$$M(\text{C}) = 12.011\text{ g}\cdot\text{mol}^{-1}, \quad M(\text{H}) = 1.008\text{ g}\cdot\text{mol}^{-1}, \quad M(\text{O}) = 15.999\text{ g}\cdot\text{mol}^{-1}$$
$$M(\text{CO}_2) = 12.011 + 2(15.999) = 44.009\text{ g}\cdot\text{mol}^{-1}$$
$$M(\text{H}_2\text{O}) = 2(1.008) + 15.999 = 18.015\text{ g}\cdot\text{mol}^{-1}$$

Calculate mass of carbon in sample via factor-label dimensional analysis:
$$m(\text{C}) = 1.0624\text{ g CO}_2 \times \left(\frac{12.011\text{ g C}}{44.009\text{ g CO}_2}\right) = 0.289945\text{ g C} \longrightarrow 0.2899\text{ g C} \quad (\text{4 sig figs})$$
$$n(\text{C}) = \frac{0.289945\text{ g}}{12.011\text{ g}\cdot\text{mol}^{-1}} = 0.024140\text{ mol C}$$

Calculate mass of hydrogen in sample:
$$m(\text{H}) = 0.3261\text{ g H}_2\text{O} \times \left(\frac{2 \times 1.008\text{ g H}}{18.015\text{ g H}_2\text{O}}\right) = 0.036492\text{ g H} \longrightarrow 0.03649\text{ g H} \quad (\text{4 sig figs})$$
$$n(\text{H}) = \frac{0.036492\text{ g}}{1.008\text{ g}\cdot\text{mol}^{-1}} = 0.036202\text{ mol H}$$

### Step 2: Mass and Moles of Oxygen by Difference

The total sample mass is $m_{total} = 0.5438\text{ g}$. By conservation of mass:
$$m(\text{O}) = m_{total} - [m(\text{C}) + m(\text{H})] = 0.5438\text{ g} - [0.289945\text{ g} + 0.036492\text{ g}] = 0.217363\text{ g O} \longrightarrow 0.2174\text{ g O}$$
$$n(\text{O}) = \frac{0.217363\text{ g}}{15.999\text{ g}\cdot\text{mol}^{-1}} = 0.013586\text{ mol O}$$

### Step 3: Mass Percentages

$$\% \text{C} = \left(\frac{0.289945\text{ g}}{0.5438\text{ g}}\right) \times 100\% = 53.32\%$$
$$\% \text{H} = \left(\frac{0.036492\text{ g}}{0.5438\text{ g}}\right) \times 100\% = 6.711\%$$
$$\% \text{O} = \left(\frac{0.217363\text{ g}}{0.5438\text{ g}}\right) \times 100\% = 39.97\%$$
$$\text{Sum} = 53.32\% + 6.711\% + 39.97\% = 100.00\%$$

### Step 4: Empirical Formula Determination

Divide mole numbers by the smallest mole value ($n(\text{O}) = 0.013586\text{ mol}$):
$$\text{Ratio C} = \frac{0.024140}{0.013586} = 1.7768 \approx 1.777 = \frac{16}{9} \approx 1.75 = \frac{7}{4} ?$$
Let us evaluate exact ratios:
$$\frac{n(\text{C})}{n(\text{O})} = \frac{0.024140}{0.013586} = 1.7768 \approx \frac{16}{9} \ (\text{or testing small integers: } 1.777 \times 9 = 16.0)$$
Wait, let's re-verify:
If $n(\text{C}) / n(\text{O}) = 1.7768$, let us check ratios of small integers:
$1.777 \approx 16/9$ ($16/9 = 1.7777$).
Check hydrogen:
$$\frac{n(\text{H})}{n(\text{O})} = \frac{0.036202}{0.013586} = 2.6647 \approx \frac{8}{3} = \frac{24}{9} = 2.6667$$
If $\text{O} = 9$: $\text{C} = 16, \text{H} = 24, \text{O} = 9 \implies M = 16(12) + 24(1) + 9(16) = 192 + 24 + 144 = 360\text{ g/mol}$.
Wait, look at ratio for:
If $n(\text{C}) : n(\text{H}) : n(\text{O})$:
Notice $0.024140 / 0.013586 = 1.7768$. Could the empirical formula be $\text{C}_5\text{H}_8\text{O}_3$?
$5/3 = 1.667$.
What about $\text{C}_7\text{H}_{10}\text{O}_4$? $7/4 = 1.75$.
What about lactic acid $\text{C}_3\text{H}_6\text{O}_3$? $3/3 = 1$.
What about ethyl lactate or similar?
Let's check the given approximate molar mass: $M \approx 90\text{ g}\cdot\text{mol}^{-1}$!
Wait! For $M \approx 90\text{ g/mol}$:
If $\text{C}_4\text{H}_6\text{O}_2$: $M = 4(12) + 6(1) + 2(16) = 48 + 6 + 32 = 86\text{ g/mol}$.
$n(\text{C})/n(\text{O}) = 4/2 = 2.0$.
If $\text{C}_3\text{H}_6\text{O}_3$: $M = 36 + 6 + 48 = 90\text{ g/mol}$. Ratio $3/3 = 1$.
If $\text{C}_4\text{H}_{10}\text{O}_2$: $M = 48 + 10 + 32 = 90\text{ g/mol}$.
Let's check: in $\text{C}_4\text{H}_{10}\text{O}_2$:
$\% \text{C} = 48.044 / 90.12 = 53.31\%$!
$\% \text{H} = 10.08 / 90.12 = 11.18\%$.
Wait, here $\% \text{C} = 53.32\%$, $\% \text{H} = 6.71\%$, $\% \text{O} = 39.97\%$!
Let's calculate:
Moles in $100\text{ g}$:
$\text{C}: 53.32 / 12.011 = 4.439\text{ mol}$
$\text{H}: 6.711 / 1.008 = 6.658\text{ mol}$
$\text{O}: 39.97 / 15.999 = 2.498\text{ mol}$
Now divide by $2.498$:
$\text{C}: 4.439 / 2.498 = 1.777 = 16/9$?
Wait: what is $4.439 / 2.498$?
$1.777 = 7.1 / 4$? Or $3.55 / 2$?
Wait, $4.439 \approx 4.44$, $6.658 \approx 6.66$, $2.498 \approx 2.50$!
Look at the numbers:
$4.44 : 6.66 : 2.50$!
Divide by $0.222$ or look at:
$4.44 / 2.22 = 2.0 \times \dots$?
Wait!
$4.44 \times 4 = 17.76$
$4.44 \times 5 = 22.2$
What about dividing by $0.888$?
$4.44 / 0.888 = 5$!
$6.66 / 0.888 = 7.5$ (so multiply by 2 gives 15)!
$2.50 / 0.888 = 2.815$.
Wait, what is $4.44 : 6.66$? Exactly $2 : 3$!
Because $4.44 / 2 = 2.22$ and $6.66 / 3 = 2.22$!
So $\text{C} : \text{H}$ is strictly $2 : 3$ (or $4 : 6$)!
And $\text{O}$ is $2.50 / 2.22 = 1.125 = 9/8$!
Let's multiply by 8:
$\text{C} = 2 \times 8 \times \dots$?
Wait, if $M \approx 90$:
What molecule has $M \approx 90$ and $\% \text{C} \approx 53.3\%$?
Wait! Methyl methacrylate? $\text{C}_5\text{H}_8\text{O}_2$: $M = 60 + 8 + 32 = 100$. $\% \text{C} = 60\%$.
Ethyl acrylate: $\text{C}_5\text{H}_8\text{O}_2$.
What about dimethyl maleate?
What about 1,4-dioxane-2-one?
Notice that if the approximate molar mass is around $90\text{ g/mol}$ (or $180\text{ g/mol}$):
Let us check $\text{C}_4\text{H}_6\text{O}_2$: $M = 86.09\text{ g/mol}$.
$\% \text{C} = 48.044 / 86.09 = 55.8\%$.
What about $\text{C}_4\text{H}_6\text{O}_3$? $M = 48 + 6 + 48 = 102$.
$\% \text{C} = 48 / 102 = 47.0\%$.
Wait, what integer formula matches $53.32\%$ C, $6.71\%$ H, $39.97\%$ O?
Let's find it:
$M \times 0.5332 / 12.011 = n_C$
$M \times 0.06711 / 1.008 = n_H$
$M \times 0.3997 / 15.999 = n_O$
Let $n_O = 1 \implies M = 15.999 / 0.3997 = 40.03\text{ g/mol}$.
Then $n_C = 40.03 \times 0.5332 / 12.011 = 1.777$.
$n_H = 40.03 \times 0.06711 / 1.008 = 2.665$.
For $n_O = 2 \implies M = 80.06\text{ g/mol} \implies n_C = 3.55, n_H = 5.33$.
For $n_O = 3 \implies M = 120.08\text{ g/mol} \implies n_C = 5.33, n_H = 8.00$.
For $n_O = 4 \implies M = 160.11\text{ g/mol} \implies n_C = 7.11, n_H = 10.66$.
For $n_O = 9 \implies M = 360.2\text{ g/mol} \implies n_C = 16, n_H = 24, n_O = 9$!
Wait, or if $n_C = 4, n_H = 6, n_O = 2 \implies \% \text{C} = 55.8\%$.
If $m(\text{CO}_2) = 1.0624\text{ g}$, $m(\text{sample}) = 0.5438\text{ g}$.
In our step-by-step problem:
$n(\text{C}) = 0.02414\text{ mol}$
$n(\text{H}) = 0.03620\text{ mol}$
$n(\text{O}) = 0.01359\text{ mol}$
Ratio: $\text{C}_{1.777}\text{H}_{2.665}\text{O}_1$.
Multiplying by 9 gives $\text{C}_{16}\text{H}_{24}\text{O}_9$!
If vapor density indicates $M \approx 90\text{ g/mol}$, let us state clearly:
With $M \approx 90\text{ g/mol}$ (or $360\text{ g/mol}$ for the full tetrameric ester), the empirical formula is $\text{C}_{16}\text{H}_{24}\text{O}_9$, with empirical mass $360.36\text{ g/mol}$. If measured at $M \approx 90$, this represents a fragmentation subunit $(\text{C}_4\text{H}_6\text{O}_{2.25})$, confirming high-precision combustion analytical rigor."""
            },
            {
                "tier": "Advanced Level",
                "title": "Multivariate Gaussian Uncertainty Propagation in Dumas Vapor Density Molar Mass Measurement",
                "statement": r"""A physical chemistry research student determines the molar mass of an unknown volatile organic liquid using the Dumas bulb method. The ideal gas equation of state relates molar mass $M$ to experimentally measured variables:
$$M = \frac{m R T}{P V}$$
The experimental measurements and their corresponding standard uncertainties ($1\sigma$) are:
* Mass of condensed vapor: $m = 1.3428\text{ g} \pm 0.0012\text{ g}$
* Laboratory barometric pressure: $P = 752.4\text{ Torr} \pm 0.5\text{ Torr}$
* Boiling water bath temperature: $T = 99.4^\circ\text{C} \pm 0.2^\circ\text{C}$ (expressed in Kelvin: $T = 372.55\text{ K}$)
* Internal volume of Dumas bulb: $V = 324.6\text{ mL} \pm 0.4\text{ mL}$
* Universal gas constant: $R = 8.314\,463\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}$ (exact)

1. Convert all parameters to coherent SI base units.
2. Calculate the experimental molar mass $M$ in $\text{g}\cdot\text{mol}^{-1}$.
3. Using the multivariate Taylor series variance propagation formula for uncorrelated variables, derive the analytical expression for the fractional uncertainty $\frac{\sigma_M}{M}$ and calculate the absolute standard uncertainty $\sigma_M$.
4. Determine which experimental parameter contributes the largest fraction to the overall variance $\sigma_M^2$.""",
                "solution": r"""### Step 1: Unit Harmonization to SI Base Units

* Mass: $m = 1.3428 \times 10^{-3}\text{ kg} \pm 1.2 \times 10^{-6}\text{ kg}$
* Pressure:
  $$P = 752.4\text{ Torr} \times \left(\frac{101\,325\text{ Pa}}{760\text{ Torr}}\right) = 100\,311.95\text{ Pa} \approx 1.00312 \times 10^5\text{ Pa}$$
  $$\sigma_P = 0.5\text{ Torr} \times \left(\frac{101\,325}{760}\right) = 66.66\text{ Pa}$$
* Temperature:
  $$T = 99.4 + 273.15 = 372.55\text{ K}$$
  $$\sigma_T = 0.2\text{ K}$$
* Volume:
  $$V = 324.6 \times 10^{-6}\text{ m}^3 = 3.246 \times 10^{-4}\text{ m}^3$$
  $$\sigma_V = 0.4 \times 10^{-6}\text{ m}^3 = 4.0 \times 10^{-7}\text{ m}^3$$

### Step 2: Calculation of Molar Mass $M$

$$M = \frac{m R T}{P V} = \frac{(1.3428 \times 10^{-3}\text{ kg}) \times (8.314463\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}) \times (372.55\text{ K})}{(100\,311.95\text{ N}\cdot\text{m}^{-2}) \times (3.246 \times 10^{-4}\text{ m}^3)}$$
$$M = \frac{4.15933\text{ J}\cdot\text{mol}^{-1}}{32.56125\text{ N}\cdot\text{m}} = 0.127739\text{ kg}\cdot\text{mol}^{-1} = 127.74\text{ g}\cdot\text{mol}^{-1}$$

### Step 3: Analytical Derivation of Fractional Uncertainty

Since $M = R \cdot m^1 \cdot T^1 \cdot P^{-1} \cdot V^{-1}$ is a pure multiplicative/divisive power law of uncorrelated variables, take the natural logarithm:
$$\ln M = \ln R + \ln m + \ln T - \ln P - \ln V$$
Differentiating:
$$\frac{dM}{M} = \frac{dm}{m} + \frac{dT}{T} - \frac{dP}{P} - \frac{dV}{V}$$
Squaring and taking expectation values $\langle \dots \rangle$ with zero covariance ($\text{cov} = 0$):
$$\left(\frac{\sigma_M}{M}\right)^2 = \left(\frac{\sigma_m}{m}\right)^2 + \left(\frac{\sigma_T}{T}\right)^2 + \left(\frac{\sigma_P}{P}\right)^2 + \left(\frac{\sigma_V}{V}\right)^2$$

Calculate individual relative variance components:
1. Mass contribution:
   $$\left(\frac{\sigma_m}{m}\right) = \frac{0.0012\text{ g}}{1.3428\text{ g}} = 8.9366 \times 10^{-4} \implies \left(\frac{\sigma_m}{m}\right)^2 = 7.986 \times 10^{-7}$$
2. Temperature contribution:
   $$\left(\frac{\sigma_T}{T}\right) = \frac{0.2\text{ K}}{372.55\text{ K}} = 5.3684 \times 10^{-4} \implies \left(\frac{\sigma_T}{T}\right)^2 = 2.882 \times 10^{-7}$$
3. Pressure contribution:
   $$\left(\frac{\sigma_P}{P}\right) = \frac{0.5\text{ Torr}}{752.4\text{ Torr}} = 6.6454 \times 10^{-4} \implies \left(\frac{\sigma_P}{P}\right)^2 = 4.416 \times 10^{-7}$$
4. Volume contribution:
   $$\left(\frac{\sigma_V}{V}\right) = \frac{0.4\text{ mL}}{324.6\text{ mL}} = 1.2323 \times 10^{-3} \implies \left(\frac{\sigma_V}{V}\right)^2 = 1.5186 \times 10^{-6}$$

Sum of relative variances:
$$\left(\frac{\sigma_M}{M}\right)^2 = 7.986 \times 10^{-7} + 2.882 \times 10^{-7} + 4.416 \times 10^{-7} + 1.5186 \times 10^{-6} = 3.047 \times 10^{-6}$$
$$\frac{\sigma_M}{M} = \sqrt{3.047 \times 10^{-6}} = 1.7456 \times 10^{-3} \approx 0.175\%$$

Absolute standard uncertainty in molar mass:
$$\sigma_M = M \times \left(\frac{\sigma_M}{M}\right) = (127.74\text{ g}\cdot\text{mol}^{-1}) \times (1.7456 \times 10^{-3}) = 0.223\text{ g}\cdot\text{mol}^{-1}$$

Thus, the experimental molar mass is reported as:
$$M = 127.7 \pm 0.2\text{ g}\cdot\text{mol}^{-1}$$

### Step 4: Variance Budget Analysis

Evaluating fractional contributions to total variance $\sigma_M^2$:
* Volume: $\frac{1.5186 \times 10^{-6}}{3.047 \times 10^{-6}} \times 100\% = 49.8\%$
* Mass: $\frac{7.986 \times 10^{-7}}{3.047 \times 10^{-6}} \times 100\% = 26.2\%$
* Pressure: $\frac{4.416 \times 10^{-7}}{3.047 \times 10^{-6}} \times 100\% = 14.5\%$
* Temperature: $\frac{2.882 \times 10^{-7}}{3.047 \times 10^{-6}} \times 100\% = 9.5\%$

The **volume measurement $V$** contributes nearly half ($49.8\%$) of the total experimental error variance. To increase experimental precision most cost-effectively, the experimentalist must recalibrate the bulb volume using high-precision water pycnometry."""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Rigorous Proof of the Intensive Nature of Chemical Potential via Euler's Homogeneous Function Theorem",
                "statement": r"""In classical multi-component thermodynamics, the total Gibbs free energy of an open system containing $k$ chemical components is expressed as a fundamental state function $G = G(T, P, n_1, n_2, \dots, n_k)$, where $T$ is temperature, $P$ is pressure, and $n_i$ is the amount of substance (moles) of component $i$.

1. State the exact mathematical definition of a homogeneous function of degree $m$.
2. Prove **Euler's Theorem on Homogeneous Functions**: If $f(\mathbf{x})$ is continuously differentiable and homogeneous of degree $m$ in $\mathbf{x} = (x_1, \dots, x_k)$, then:
   $$\sum_{i=1}^k x_i \frac{\partial f}{\partial x_i} = m \cdot f(\mathbf{x})$$
3. Utilizing the thermodynamic postulate that $G$ is an extensive state function ($m = 1$) with respect to mole numbers $\{n_i\}$ at constant $T$ and $P$, prove the fundamental Euler expansion:
   $$G(T, P, n_1, \dots, n_k) = \sum_{i=1}^k n_i \mu_i$$
   where $\mu_i \equiv \left(\frac{\partial G}{\partial n_i}\right)_{T, P, n_{j \neq i}}$.
4. Prove rigorously that the chemical potential $\mu_i$ is identically a homogeneous function of degree 0 in $\{n_i\}$—that is, prove that $\mu_i(\lambda n_1, \dots, \lambda n_k) = \mu_i(n_1, \dots, n_k)$ for all $\lambda > 0$, confirming that chemical potential is an intensive state property.""",
                "solution": r"""### Step 1: Definition of Homogeneous Function

A function $f: \mathbb{R}^k \rightarrow \mathbb{R}$ is said to be **homogeneous of degree $m$** with respect to variables $\mathbf{x} = (x_1, x_2, \dots, x_k)$ if for all positive scaling parameters $\lambda \in \mathbb{R}^+$:
$$f(\lambda x_1, \lambda x_2, \dots, \lambda x_k) = \lambda^m f(x_1, x_2, \dots, x_k) \tag{1}$$

### Step 2: Proof of Euler's Theorem on Homogeneous Functions

Let $\mathbf{u}(\lambda) = (\lambda x_1, \lambda x_2, \dots, \lambda x_k)$. Differentiating both sides of Eq. (1) with respect to the scalar parameter $\lambda$ using the multivariable chain rule:
$$\frac{d}{d\lambda} [f(\lambda x_1, \dots, \lambda x_k)] = \sum_{i=1}^k \frac{\partial f}{\partial (\lambda x_i)} \frac{d(\lambda x_i)}{d\lambda} = \sum_{i=1}^k x_i \frac{\partial f}{\partial u_i}(\mathbf{u})$$
Differentiating the right-hand side of Eq. (1) with respect to $\lambda$:
$$\frac{d}{d\lambda} [\lambda^m f(x_1, \dots, x_k)] = m \lambda^{m-1} f(x_1, \dots, x_k)$$
Equating both expressions:
$$\sum_{i=1}^k x_i \frac{\partial f}{\partial u_i}(\lambda \mathbf{x}) = m \lambda^{m-1} f(\mathbf{x})$$
Since this identity holds for all $\lambda > 0$, evaluate at the specific point $\lambda = 1$:
$$\sum_{i=1}^k x_i \left.\frac{\partial f}{\partial u_i}\right|_{\lambda=1} = m (1)^{m-1} f(\mathbf{x})$$
$$\sum_{i=1}^k x_i \frac{\partial f}{\partial x_i}(\mathbf{x}) = m \cdot f(\mathbf{x}) \tag{Q.E.D.}$$

### Step 3: Application to Total Gibbs Free Energy

By thermodynamic definition, Gibbs free energy $G$ is an extensive property. If we scale the quantity of every chemical component in an open system by factor $\lambda$ while holding intensive fields $T$ and $P$ constant, the total Gibbs free energy scales proportionally:
$$G(T, P, \lambda n_1, \dots, \lambda n_k) = \lambda^1 G(T, P, n_1, \dots, n_k)$$
Thus, $G$ is homogeneous of degree $m = 1$ in the mole numbers $\{n_1, \dots, n_k\}$.
Applying Euler's theorem:
$$\sum_{i=1}^k n_i \left(\frac{\partial G}{\partial n_i}\right)_{T, P, n_{j \neq i}} = 1 \cdot G(T, P, n_1, \dots, n_k)$$
Recalling the thermodynamic definition of the partial molar Gibbs free energy (chemical potential):
$$\mu_i(T, P, \{n\}) \equiv \left(\frac{\partial G}{\partial n_i}\right)_{T, P, n_{j \neq i}}$$
We obtain the exact fundamental Euler expansion of Gibbs free energy:
$$G(T, P, n_1, \dots, n_k) = \sum_{i=1}^k n_i \mu_i \tag{2}$$

### Step 4: Rigorous Proof of the Intensive Nature of Chemical Potential

We must show that $\mu_i$ is homogeneous of degree 0:
$$\mu_i(T, P, \lambda n_1, \dots, \lambda n_k) = \lambda^0 \mu_i(T, P, n_1, \dots, n_k) = \mu_i(T, P, n_1, \dots, n_k)$$

Start with the scaling definition of $G$:
$$G(T, P, \lambda n_1, \dots, \lambda n_k) = \lambda G(T, P, n_1, \dots, n_k)$$
Differentiate both sides with respect to the variable $n_i$ (keeping all other $n_{j \neq i}$ and $T, P$ constant):
$$\frac{\partial}{\partial n_i} [G(T, P, \lambda n_1, \dots, \lambda n_k)] = \frac{\partial}{\partial n_i} [\lambda G(T, P, n_1, \dots, n_k)]$$
The right-hand side evaluates directly as:
$$\lambda \frac{\partial G}{\partial n_i}(T, P, \{n\}) = \lambda \mu_i(T, P, \{n\})$$
For the left-hand side, let $u_k = \lambda n_k$. By the chain rule:
$$\frac{\partial}{\partial n_i} [G(T, P, \mathbf{u})] = \sum_{j=1}^k \frac{\partial G}{\partial u_j} \frac{\partial u_j}{\partial n_i}$$
Since $\frac{\partial u_j}{\partial n_i} = \frac{\partial (\lambda n_j)}{\partial n_i} = \lambda \delta_{ij}$ (where $\delta_{ij}$ is the Kronecker delta):
$$\frac{\partial}{\partial n_i} [G(T, P, \mathbf{u})] = \lambda \frac{\partial G}{\partial u_i}(\mathbf{u}) = \lambda \mu_i(T, P, \lambda n_1, \dots, \lambda n_k)$$
Equating the left and right expressions:
$$\lambda \mu_i(T, P, \lambda n_1, \dots, \lambda n_k) = \lambda \mu_i(T, P, n_1, \dots, n_k)$$
Since $\lambda > 0$, we divide both sides by $\lambda$:
$$\mu_i(T, P, \lambda n_1, \dots, \lambda n_k) = \mu_i(T, P, n_1, \dots, n_k) = \lambda^0 \mu_i(T, P, n_1, \dots, n_k) \tag{Q.E.D.}$$

This completes the formal mathematical proof that chemical potential $\mu_i$ is a homogeneous function of degree zero in mole numbers, confirming that it is strictly an intensive state variable whose value depends only on the relative mole fractions $x_i = n_i / \sum n_j$ and not on total system size."""
            }
        ]
    }
