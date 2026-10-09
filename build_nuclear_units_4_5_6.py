# -*- coding: utf-8 -*-
"""
build_nuclear_units_4_5_6.py
Builds Units 4, 5, and 6 for Nuclear and Radiochemistry (#47):
- Unit 4: Nuclear Reaction Dynamics, Kinematics & Cross-Sections
- Unit 5: Nuclear Fission Mechanics & Reactor Physics
- Unit 6: Radiation Interaction with Matter & Energy Loss Mechanisms
Strictly Zero Course Numbers or Marks. All math in raw strings r\"\"\"...\"\"\".
"""

import json

def get_units_4_5_6():
    units = [
        # =====================================================================
        # UNIT 4
        # =====================================================================
        {
            "id": "unit-4-nuclear-reactions-kinematics-cross-sections",
            "unitNumber": 4,
            "title": "Unit 4: Nuclear Reaction Dynamics, Kinematics & Reaction Cross-Sections",
            "leadSummary": "Rigorous theoretical and mathematical treatise on nuclear reactions: conservation laws in nuclear transformations, laboratory versus center-of-mass kinematics, Coulomb potential barrier penetration via Gamow tunneling, exact derivation of reaction Q-values and endoergic threshold energies, the Bohr compound nucleus hypothesis versus direct reaction mechanisms, and cross-section resonance mechanics via the Breit-Wigner formula.",
            "simulations": ["sim_nuc_reaction_cross_section_q"],
            "sections": [
                {
                    "id": "sec-4-1",
                    "secNumber": "4.1",
                    "title": "Fundamentals of Nuclear Reactions: Conservation Laws & Reaction Channels",
                    "content": r"""A nuclear reaction occurs when two subatomic entities—typically an incident projectile particle $a$ and a target nucleus $X$—collide at close range, resulting in a rearrangement of nucleons to produce one or more product nuclei $Y$ and outgoing ejectile particles $b$:
$$a + X \longrightarrow Y + b \quad \text{or in Bethe shorthand} \quad X(a, b)Y$$
If multiple particles emerge, the reaction is written $X(a, b_1 b_2 \dots)Y$.

### Primary Reaction Types
1. **Elastic Scattering** ($a + X \to X + a$, denoted $X(a, a)X$):
The projectile and target are identical in species and internal quantum state before and after the collision. Kinetic energy is strictly conserved in the center-of-mass frame ($Q = 0$).
2. **Inelastic Scattering** ($a + X \to X^* + a$, denoted $X(a, a')X^*$):
A portion of the incident kinetic energy is transferred into internal excitation energy of the target nucleus $X^*$, which subsequently de-excites via gamma emission ($Q < 0$).
3. **Radiative Capture** ($a + X \to Y^* \to Y + \gamma$, denoted $X(a, \gamma)Y$):
The projectile is absorbed into the target nucleus, forming an excited compound state that de-excites solely by gamma photon emission (e.g., $^{115}\text{In}(n, \gamma)^{116}\text{In}$, $^{238}\text{U}(n, \gamma)^{239}\text{U}$).
4. **Transfer Reactions**:
One or a few nucleons are transferred between projectile and target during a fast peripheral transit:
- **Stripping**: Projectile loses nucleons to target (e.g., $(d, p)$, $(d, n)$, $(^3\text{He}, d)$).
- **Pickup**: Projectile captures nucleons from target (e.g., $(p, d)$, $(n, d)$, $(\alpha, ^6\text{Li})$).
5. **Knockout Reactions**:
Incident projectile collides directly with a single constituent nucleon, ejecting it promptly (e.g., $(p, 2p)$, $(p, pn)$).
6. **Spallation Reactions**:
Ultra-relativistic projectiles ($E > 100\text{ MeV}$) shatter a heavy nucleus into dozens of nucleons and nuclear fragments.
7. **Nuclear Fission and Fusion**:
Fission splits a heavy nucleus into two intermediate-mass fragments plus neutrons; fusion coalesces light nuclei into a heavier product.

### Exact Conservation Laws in Nuclear Reactions
Every nuclear reaction is constrained by fundamental physical conservation laws:

| Conserved Quantity | Mathematical Formalism | Symmetries & Invariances |
| :--- | :--- | :--- |
| **Total Mass-Energy** | $E_{\text{total}} = \sum (T_i + m_i c^2) = \text{constant}$ | Invariance under time translation |
| **Linear Momentum** | $\vec{P}_{\text{total}} = \sum \vec{p}_i = \text{constant}$ | Invariance under spatial translation |
| **Total Angular Momentum** | $\vec{J}_{\text{total}} = \sum (\vec{L}_i + \vec{I}_i) = \text{constant}$ | Invariance under spatial rotation |
| **Electric Charge** | $\sum Z_i = \text{constant}$ | $U(1)$ gauge invariance of electrodynamics |
| **Total Baryon Number** | $\sum A_i = \text{constant}$ | Global baryon number conservation |
| **Parity ($\pi$)** | $\pi_{\text{initial}} = \prod \pi_i (-1)^{l_{\text{in}}} = \pi_{\text{final}}$ | Strong & electromagnetic spatial inversion invariance |
| **Isospin ($T, T_3$)** | $\sum T_{3,i} = \text{constant}$; $T$ conserved in strong force | Charge symmetry and charge independence |

Violations of parity or isospin indicate weak force participation (e.g., beta decays or weak nuclear transitions).""",
                    "simulations": ["sim_nuc_reaction_cross_section_q"]
                },
                {
                    "id": "sec-4-2",
                    "secNumber": "4.2",
                    "title": "Laboratory Versus Center-of-Mass Kinematics: Coordinate Transformations & Energy Partition",
                    "content": r"""In experimental nuclear physics, measurements are performed in the **Laboratory (LAB) frame**, where the target nucleus $X$ of mass $M_X$ is initially at rest ($v_X = 0$) and the projectile $a$ of mass $m_a$ strikes it with incident laboratory kinetic energy $T_a^{\text{lab}}$ and momentum $\vec{p}_a = m_a \vec{v}_a$.

Theoretical analyses, however, are vastly simplified in the **Center-of-Mass (CM) frame**, where the total linear momentum is identically zero:
$$\vec{P}_{\text{CM}} = \vec{p}_a^{\text{CM}} + \vec{p}_X^{\text{CM}} = 0$$

### Center-of-Mass Velocity
The velocity of the center of mass in the laboratory frame is:
$$\vec{V}_{\text{CM}} = \frac{m_a \vec{v}_a + M_X \vec{v}_X}{m_a + M_X} = \frac{m_a}{m_a + M_X} \vec{v}_a$$

```
 LAB FRAME:                         CENTER-OF-MASS (CM) FRAME:
  m_a (v_a)      M_X (at rest)       m_a (v_a - V_cm)    M_X (-V_cm)
   ───►             O                 ───►                  ◄───
                                               \              /
                                                \   Zero     /
                                                 Total Momentum!
```

### Partition of Kinetic Energy
The total laboratory kinetic energy is:
$$T_{\text{total}}^{\text{lab}} = \frac{1}{2} m_a v_a^2 = T_a^{\text{lab}}$$
In the CM frame, the velocities of the particles are:
$$u_a = v_a - V_{\text{CM}} = v_a \left(1 - \frac{m_a}{m_a + M_X}\right) = \frac{M_X}{m_a + M_X} v_a$$
$$u_X = 0 - V_{\text{CM}} = -\frac{m_a}{m_a + M_X} v_a$$

The total kinetic energy available in the Center-of-Mass frame ($T_{\text{total}}^{\text{CM}}$) is:
$$T_{\text{total}}^{\text{CM}} = \frac{1}{2} m_a u_a^2 + \frac{1}{2} M_X u_X^2 = \frac{1}{2} m_a \left(\frac{M_X}{m_a + M_X}\right)^2 v_a^2 + \frac{1}{2} M_X \left(\frac{m_a}{m_a + M_X}\right)^2 v_a^2$$
Factoring:
$$T_{\text{total}}^{\text{CM}} = \frac{1}{2} \left[ \frac{m_a M_X^2 + M_X m_a^2}{(m_a + M_X)^2} \right] v_a^2 = \frac{1}{2} \left[ \frac{m_a M_X (M_X + m_a)}{(m_a + M_X)^2} \right] v_a^2 = \frac{1}{2} \left(\frac{m_a M_X}{m_a + M_X}\right) v_a^2$$
Defining the **reduced mass** $\mu$:
$$\mu \equiv \frac{m_a M_X}{m_a + M_X}$$
We obtain the fundamental relationship:
$$T_{\text{total}}^{\text{CM}} = \frac{1}{2} \mu v_a^2 = \left(\frac{M_X}{m_a + M_X}\right) T_a^{\text{lab}}$$

The remaining portion of laboratory kinetic energy is tied up in the irreducible forward motion of the center of mass:
$$T_{\text{motion}}^{\text{CM}} = \frac{1}{2} (m_a + M_X) V_{\text{CM}}^2 = \left(\frac{m_a}{m_a + M_X}\right) T_a^{\text{lab}}$$
Only the CM kinetic energy $T_{\text{total}}^{\text{CM}}$ is available to induce internal nuclear excitations, overcome reaction barriers, or satisfy endoergic reaction deficits.""",
                    "simulations": ["sim_nuc_reaction_cross_section_q"]
                },
                {
                    "id": "sec-4-3",
                    "secNumber": "4.3",
                    "title": "The Nuclear Coulomb Potential Barrier & Gamow Quantum Tunneling Factor",
                    "content": r"""When a positively charged projectile (such as a proton, deuteron, or alpha particle with charge $z e$) approaches a target nucleus with charge $Z e$, it experiences long-range electrostatic Coulomb repulsion.

### Coulomb Potential Barrier Height ($V_C$)
The repulsive Coulomb potential energy at center-to-center separation $r$ is:
$$V(r) = \frac{1}{4\pi\varepsilon_0} \frac{z Z e^2}{r}$$
As the projectile approaches the target, the potential rises monotonically until the surfaces of the two nuclei touch at the **contact radius** $R_c = R_a + R_X = R_0 (a^{1/3} + X^{1/3})$. At this radius, the attractive short-range strong nuclear force takes over, forming an attractive potential well.

The maximum electrostatic potential energy at contact defines the **Coulomb Barrier Height** $V_C$:
$$V_C = \frac{1}{4\pi\varepsilon_0} \frac{z Z e^2}{R_a + R_X} = \frac{1.43996\text{ MeV}\cdot\text{fm} \cdot z Z}{R_0 (a^{1/3} + X^{1/3})}$$

```
   Potential Energy V(r)
      ▲
  V_C │          /\  Coulomb Barrier Peak
      │         /  \
      │        /    \____ V(r) = (1/4πε₀) * (zZe²/r)
      │       /
    0 ┼──────/────────────────────────► Separation r
      │     │  R_c (Contact Radius)
 -V₀  │_____│  Attractive Strong Well
```

For an alpha particle ($z = 2, a = 4$) striking an uranium-238 nucleus ($Z = 92, X = 238$) with $R_0 = 1.25\text{ fm}$:
$$R_c = 1.25(4^{1/3} + 238^{1/3}) = 1.25(1.587 + 6.197) = 1.25(7.784) \approx 9.73\text{ fm}$$
$$V_C = \frac{(1.44\text{ MeV}\cdot\text{fm})(2)(92)}{9.73\text{ fm}} = \frac{264.96}{9.73} \approx 27.2\text{ MeV}$$

### Quantum Mechanical Gamow Tunneling Factor
Under classical mechanics, a projectile with kinetic energy $T < V_C$ is strictly forbidden from reaching the nucleus and undergoing a nuclear reaction.
In 1928, George Gamow (and independently Condon and Gurney) demonstrated that a quantum wavepacket has a non-zero probability of **tunneling through the classically forbidden barrier**.

Using the WKB (Wentzel-Kramers-Brillouin) approximation, the transmission probability $P$ through a barrier $V(r)$ from classical turning point $r_0$ to contact radius $R_c$ is:
$$P \approx \exp\left( -2 \int_{R_c}^{r_0} k(r) dr \right) = \exp\left( -\frac{2}{\hbar} \int_{R_c}^{r_0} \sqrt{2\mu [V(r) - E]} \, dr \right)$$
where $E$ is the center-of-mass energy and $r_0$ satisfies $V(r_0) = E \implies r_0 = \frac{z Z e^2}{4\pi\varepsilon_0 E}$.

Evaluating the integral analytically for $R_c \ll r_0$:
$$P \approx \exp(-2\pi \eta)$$
where $\eta$ is the dimensionless **Sommerfeld parameter**:
$$\eta = \frac{z Z e^2}{4\pi\varepsilon_0 \hbar v} = \frac{z Z \alpha}{v / c} = \sqrt{\frac{\mu c^2}{2E}} z Z \alpha$$
where $\alpha = \frac{e^2}{4\pi\varepsilon_0 \hbar c} \approx \frac{1}{137.036}$ is the fine-structure constant.

The factor $\exp(-2\pi \eta)$ is the famous **Gamow factor**. It explains:
1. Why low-energy alpha particles ($4 - 8\text{ MeV}$) can tunnel out of heavy nuclei despite the $25 - 30\text{ MeV}$ barrier (Geiger-Nuttall law).
2. Why thermonuclear fusion in stellar interiors (e.g., the Sun's core at $T \approx 1.5 \times 10^7\text{ K}$, where thermal kinetic energies are a mere $\sim 1.3\text{ keV}$) occurs at measurable rates through the **Gamow window**.""",
                    "simulations": ["sim_nuc_reaction_cross_section_q"]
                },
                {
                    "id": "sec-4-4",
                    "secNumber": "4.4",
                    "title": "The Q-Value Derivation, Exoergic Dynamics & Threshold Energy of Endoergic Reactions",
                    "content": r"""The energetics of any nuclear reaction $X(a, b)Y$ are governed by its **reaction energy**, designated as the **$Q$-value**.

### Derivation of the $Q$-Value from Mass-Energy Equivalence
By relativistic conservation of total mass-energy:
$$E_{\text{reactants}} = E_{\text{products}}$$
$$(T_a + m_a c^2) + (T_X + M_X c^2) = (T_b + m_b c^2) + (T_Y + M_Y c^2)$$
Rearranging terms:
$$(T_b + T_Y) - (T_a + T_X) = (m_a + M_X)c^2 - (m_b + M_Y)c^2$$
The $Q$-value is formally defined as the net change in kinetic energy, which equals the net difference in rest masses:
$$Q \equiv (T_b + T_Y) - (T_a + T_X) = \left[ (m_a + M_X) - (m_b + M_Y) \right] c^2$$

Because binding energy $B$ is defined as $B = [Z m_p + N m_n - M] c^2$, the nucleon numbers $Z$ and $N$ cancel identically, yielding:
$$Q = \left[ B(Y) + B(b) \right] - \left[ B(X) + B(a) \right] = \sum B_{\text{products}} - \sum B_{\text{reactants}}$$

### Energetic Classifications
1. **Exoergic (Exothermic) Reactions ($Q > 0$)**:
Rest mass is converted into kinetic energy ($\Delta m > 0$). The reaction can occur at arbitrarily low projectile kinetic energies (even at thermal energies $T_a \approx 0$ for uncharged neutrons).
2. **Endoergic (Endothermic) Reactions ($Q < 0$)**:
Kinetic energy is converted into rest mass ($\Delta m < 0$). The reaction is energetically impossible unless the incident projectile supplies sufficient kinetic energy to cover the mass deficit plus the unavoidable center-of-mass recoil motion.

### Exact Derivation of Threshold Energy ($E_{\text{th}}$)
For an endoergic reaction ($Q < 0$) in the laboratory frame with stationary target ($T_X = 0$), what is the minimum kinetic energy $T_a^{\text{lab}} = E_{\text{th}}$ required for the reaction to occur?

At the absolute threshold, all reaction products $Y$ and $b$ emerge with **zero relative velocity in the center-of-mass frame**; they move forward as a single consolidated mass $(M_Y + m_b)$ at the velocity of the center of mass $V_{\text{CM}}$.
By conservation of linear momentum:
$$m_a v_{\text{th}} = (M_Y + m_b) V_{\text{CM}} \approx (m_a + M_X) V_{\text{CM}} \implies V_{\text{CM}} = \frac{m_a}{m_a + M_X} v_{\text{th}}$$
The total laboratory kinetic energy of the products at threshold is:
$$T_{\text{products}}^{\text{lab}} = \frac{1}{2} (M_Y + m_b) V_{\text{CM}}^2 \approx \frac{1}{2} (m_a + M_X) \left(\frac{m_a}{m_a + M_X} v_{\text{th}}\right)^2 = \left(\frac{m_a}{m_a + M_X}\right) \left(\frac{1}{2} m_a v_{\text{th}}^2\right) = \left(\frac{m_a}{m_a + M_X}\right) E_{\text{th}}$$

From the definition of $Q$:
$$Q = T_{\text{products}}^{\text{lab}} - T_{\text{reactants}}^{\text{lab}} = \left(\frac{m_a}{m_a + M_X}\right) E_{\text{th}} - E_{\text{th}} = -E_{\text{th}} \left( 1 - \frac{m_a}{m_a + M_X} \right) = -E_{\text{th}} \left(\frac{M_X}{m_a + M_X}\right)$$
Solving for $E_{\text{th}}$ (with $Q < 0$):
$$E_{\text{th}} = -Q \left(\frac{m_a + M_X}{M_X}\right) = |Q| \left(1 + \frac{m_a}{M_X}\right)$$

This elegant formula shows that the threshold energy in the lab is always strictly greater than $|Q|$. The factor $(m_a / M_X) |Q|$ represents the inescapable kinetic energy locked in the forward recoil of the center of mass.""",
                    "simulations": ["sim_nuc_reaction_cross_section_q"]
                },
                {
                    "id": "sec-4-5",
                    "secNumber": "4.5",
                    "title": "Reaction Mechanisms: Bohr Compound Nucleus Hypothesis Versus Direct Nuclear Reactions",
                    "content": r"""In 1936, Niels Bohr proposed the **Compound Nucleus Hypothesis** to explain the narrow, intense resonance peaks observed in low-energy neutron capture reactions.

### The Two-Stage Compound Nucleus Model
Bohr posited that a nuclear reaction proceeds in two completely independent, decoupled stages:
1. **Formation Stage**: The incident projectile $a$ is absorbed by target $X$, merging into an intermediate excited compound state $C^*$:
$$a + X \longrightarrow C^*$$
The incident kinetic energy and binding energy are rapidly distributed among all nucleons through hundreds of stochastic nucleon-nucleon collisions. The compound nucleus reaches thermodynamic quasi-equilibrium within $\sim 10^{-16}\text{ to }10^{-18}\text{ seconds}$—an eternity compared to the nuclear transit time $\tau_{\text{transit}} \approx 2R/v \sim 10^{-22}\text{ seconds}$.
2. **Decay (De-excitation) Stage**: The compound nucleus "forgets" the specific manner in which it was formed (the **Bohr Independence Hypothesis**). It de-excites purely statistically through whatever open decay channel stochastic fluctuations concentrate enough energy into:
$$C^* \longrightarrow \begin{cases} X + a & \text{(Elastic / Shape Resonant Scattering)} \\ X^* + a' & \text{(Inelastic Scattering)} \\ Y_1 + b_1 & \text{(Particle Emission, e.g., } (n, p), (n, \alpha)) \\ C + \gamma & \text{(Radiative Capture)} \\ F_1 + F_2 & \text{(Nuclear Fission)} \end{cases}$$

```
 FORMATION (Fast: ~10⁻²² s)           EQUILIBRATION (~10⁻¹⁶ s)        DECAY (Statistical)
  a + X ────────────────────────►        [ Compound Nucleus C* ]     ───► Y₁ + b₁
                                         (Energy shared among all)   ───► Y₂ + b₂
                                                                     ───► C + γ
```

Mathematically, the cross-section for reaction channel $a \to b$ factorizes:
$$\sigma(a, b) = \sigma_{\text{formation}}(C^*) \cdot P_{\text{decay}}(b)$$
where $P_{\text{decay}}(b) = \Gamma_b / \Gamma_{\text{total}}$ is the branching fraction for decay into mode $b$.

Experimental proof was provided by Ghoshal (1950), who produced the identical compound nucleus $^{64}\text{Zn}^*$ via two completely different entrances:
$$p + ^{63}_{29}\text{Cu} \longrightarrow [^{64}_{30}\text{Zn}^*] \quad \text{and} \quad \alpha + ^{60}_{28}\text{Ni} \longrightarrow [^{64}_{30}\text{Zn}^*]$$
At identical excitation energies, the cross-section ratios for de-excitation via $(n)$, $(2n)$, and $(pn)$ channels were experimentally identical, proving the independence hypothesis.

### Direct Nuclear Reactions
In contrast, when the projectile energy is high ($E > 20\text{ MeV}$) or the impact parameter corresponds to the nuclear surface, the reaction bypasses compound nucleus formation:
- **Timescale**: Ultra-fast, $\tau \sim 10^{-22}\text{ s}$ (single transit).
- **Mechanism**: Projectile interacts directly with a single valence nucleon without exciting the bulk core.
- **Angular Distribution**: Strongly forward-peaked ($\theta \approx 0^\circ$).
- **Excitation Functions**: Smooth and monotonic with energy, showing no sharp resonances.""",
                    "simulations": ["sim_nuc_reaction_cross_section_q"]
                },
                {
                    "id": "sec-4-6",
                    "secNumber": "4.6",
                    "title": "Reaction Cross-Section Formalism: The Barn, Differential Cross-Sections & Excitation Functions",
                    "content": r"""The **nuclear reaction cross-section** $\sigma$ is an effective target area quantifying the intrinsic probability that a given nuclear reaction will take place between a projectile and a target nucleus.

### Physical Formulation of Cross-Section
Consider a uniform beam of incident particles with flux $\Phi$ (particles per unit area per unit time, $\text{cm}^{-2}\cdot\text{s}^{-1}$) striking a thin target foil of area $A$, thickness $dx$, and atomic number density $n$ ($\text{nuclei/cm}^3$).
The total number of target nuclei exposed to the beam is $N_T = n \cdot A \cdot dx$.

The reaction rate $R$ (number of nuclear events occurring per second) is experimentally found to be directly proportional to the incident flux and the total number of exposed target nuclei:
$$R = \sigma \cdot \Phi \cdot N_T = \sigma \cdot \Phi \cdot (n \cdot A \cdot dx)$$
Solving for $\sigma$:
$$\sigma = \frac{R}{\Phi \cdot N_T} = \frac{\text{Events / second}}{(\text{Incident particles / cm}^2\cdot\text{s}) \cdot (\text{Target nuclei})}$$
Cross-section has physical dimensions of **area** ($[\text{L}]^2$).

### The Unit of Cross-Section: The Barn
Because typical nuclear radii are $R \sim 5\text{ fm} = 5 \times 10^{-13}\text{ cm}$, the geometric cross-sectional area of a nucleus is:
$$\sigma_{\text{geom}} \approx \pi R^2 \approx \pi (5 \times 10^{-13}\text{ cm})^2 \approx 8 \times 10^{-25}\text{ cm}^2$$
During the Manhattan Project in 1942, physicists Purdue and Oppenheimer coined the term **barn** ($\text{b}$) to indicate an area "as big as a barn" for nuclear collisions:
$$1\text{ barn (b)} \equiv 10^{-24}\text{ cm}^2 = 10^{-28}\text{ m}^2 = 100\text{ fm}^2$$
Subunits:
- Millibarn ($\text{mb} = 10^{-3}\text{ b} = 10^{-27}\text{ cm}^2$)
- Microbarn ($\mu\text{b} = 10^{-6}\text{ b} = 10^{-30}\text{ cm}^2$)
- Kilobarn ($\text{kb} = 10^3\text{ b} = 10^{-21}\text{ cm}^2$)

### Differential Cross-Section ($d\sigma/d\Omega$)
To describe the angular distribution of reaction products, we define the **differential cross-section**:
$$\frac{d\sigma}{d\Omega}(\theta, \phi) = \frac{1}{\Phi \cdot N_T} \frac{dR(\theta, \phi)}{d\Omega}$$
where $d\Omega = \sin\theta d\theta d\phi$ is the element of solid angle (steradians, $\text{sr}$).
The total cross-section is obtained by integrating over all solid angles:
$$\sigma_{\text{total}} = \int_{4\pi} \left(\frac{d\sigma}{d\Omega}\right) d\Omega = \int_0^{2\pi} d\phi \int_0^\pi \left(\frac{d\sigma}{d\Omega}\right) \sin\theta d\theta$$

### Macroscopic Cross-Section ($\Sigma$) and Mean Free Path ($\lambda_{\text{mfp}}$)
In reactor physics and radiation shielding, the probability of interaction per unit path length in a bulk material is described by the **macroscopic cross-section** $\Sigma$:
$$\Sigma = n \cdot \sigma = \frac{\rho N_A}{M} \sigma \quad (\text{dimensions: } \text{cm}^{-1})$$
A beam of intensity $I(0)$ traversing distance $x$ through the medium is attenuated according to:
$$I(x) = I(0) e^{-\Sigma x}$$
The **nuclear mean free path** $\lambda_{\text{mfp}}$ between collisions is:
$$\lambda_{\text{mfp}} = \frac{1}{\Sigma} = \frac{1}{n \sigma}$$""",
                    "simulations": ["sim_nuc_reaction_cross_section_q"]
                },
                {
                    "id": "sec-4-7",
                    "secNumber": "4.7",
                    "title": "The Breit-Wigner Single-Level Resonance Formula & Neutron Absorption Cross-Sections",
                    "content": r"""When the incident kinetic energy of a projectile corresponds precisely to a discrete quasi-stationary quantum energy state of the compound nucleus ($E_{\text{inc}} \approx E_0$), the cross-section exhibits a sharp, dramatic spike known as a **nuclear resonance**.

### Quantum Derivation of the Breit-Wigner Single-Level Formula
In 1936, Gregory Breit and Eugene Wigner formulated the dispersion theory for nuclear resonances, analogizing the process to an optical oscillator or damped harmonic wave.
The wave function of an unstable compound state decaying with lifetime $\tau$ has the time dependence:
$$\psi(t) = \psi(0) \exp\left( -i \frac{E_0}{\hbar} t - \frac{t}{2\tau} \right) = \psi(0) \exp\left( -i \frac{E_0 - i\Gamma/2}{\hbar} t \right)$$
where the total resonance energy width $\Gamma$ is related to mean lifetime by the Heisenberg uncertainty principle:
$$\Gamma = \frac{\hbar}{\tau} = \sum_i \Gamma_i = \Gamma_n + \Gamma_\gamma + \Gamma_\alpha + \dots$$
Here, each $\Gamma_i$ is the **partial width** corresponding to the probability of decay into channel $i$.

Taking the Fourier transform of $\psi(t)$ into the energy domain yields the probability amplitude:
$$f(E) \propto \frac{1}{E - E_0 + i\Gamma/2}$$
The cross-section for reaction channel $a \to b$ is proportional to $|f(E)|^2$:
$$\sigma(a, b) = \pi \lambdabar^2 g_J \frac{\Gamma_a \Gamma_b}{(E - E_0)^2 + (\Gamma/2)^2}$$
where:
- $\lambdabar = \frac{\lambda}{2\pi} = \frac{\hbar}{p}$ is the reduced de Broglie wavelength of the incident particle.
- $g_J$ is the statistical spin factor accounting for angular momentum coupling between projectile spin $s_a$ and target nuclear spin $I_X$ to form compound spin $J$:
$$g_J = \frac{2J + 1}{(2s_a + 1)(2I_X + 1)}$$

```
   Cross Section σ(E)
    ▲
 σ₀ │             /\  Resonance Peak E₀
    │            /  \
    │           /    \
σ₀/2│----------/------\---------- FWHM = Γ (Total Width)
    │         /        \
    │_______/            \_______
    └───────┴─────┴──────┴───────► Projectile Energy E
                E₀-Γ/2  E₀+Γ/2
```

### The $1/v$ Law for Low-Energy Neutron Capture
For slow (thermal) s-wave neutrons ($l = 0$), the incident energy is far below the first resonance ($E \ll E_0$).
The de Broglie wavelength squared scales as:
$$\lambdabar^2 = \frac{\hbar^2}{p^2} = \frac{\hbar^2}{2 m_n E} \propto \frac{1}{E} \propto \frac{1}{v^2}$$
For s-wave neutrons, the neutron emission partial width $\Gamma_n$ is proportional to the outgoing neutron velocity (density of final states):
$$\Gamma_n \propto v$$
While the radiative capture width $\Gamma_\gamma$ is constant (independent of neutron speed).
Substituting these into the Breit-Wigner formula with $(E - E_0)^2 \approx E_0^2$:
$$\sigma(n, \gamma) \propto \lambdabar^2 \Gamma_n \Gamma_\gamma \propto \left(\frac{1}{v^2}\right) (v) (\text{constant}) \propto \frac{1}{v}$$

This yields the fundamental **$1/v$ Law of Slow Neutron Capture**:
$$\sigma(v) = \sigma_0 \left(\frac{v_0}{v}\right) = \sigma_0 \sqrt{\frac{E_0}{E}}$$
where standard thermal neutron cross-sections are tabulated at reference velocity $v_0 = 2200\text{ m/s}$ ($E_0 = 0.0253\text{ eV}$ at $T = 293.6\text{ K}$).
This explains why thermal neutrons have enormous capture cross sections (thousands of barns) compared to fast neutrons (a few barns).""",
                    "simulations": ["sim_nuc_reaction_cross_section_q"]
                }
            ],
            "problems": [
                {
                    "id": "prob-4-1",
                    "problemNumber": "4.1",
                    "title": "Exact Q-Value and Threshold Energy for C-12(alpha, n)O-15",
                    "difficulty": "Intermediate",
                    "statement": r"""Consider the endoergic nuclear reaction:
$$^{12}_{6}\text{C} + ^{4}_{2}\alpha \longrightarrow ^{15}_{8}\text{O} + ^{1}_{0}n$$
Given the atomic masses:
- $M(^{12}\text{C}) = 12.000000\text{ u}$
- $m(\alpha) = 4.001506\text{ u}$
- $M(^{15}\text{O}) = 15.003065\text{ u}$
- $m_n = 1.008665\text{ u}$
- $1\text{ u} = 931.4941\text{ MeV}/c^2$
1. Calculate the reaction $Q$-value in $\text{MeV}$.
2. Determine the minimum threshold kinetic energy $E_{\text{th}}$ in the laboratory frame required for incident alpha particles striking a stationary $^{12}\text{C}$ target.""",
                    "solution": r"""### Step 1: Calculate $Q$-Value
Sum of reactant masses:
$$m_{\text{reactants}} = M(^{12}\text{C}) + m(\alpha) = 12.000000 + 4.001506 = 16.001506\text{ u}$$
Sum of product masses:
$$m_{\text{products}} = M(^{15}\text{O}) + m_n = 15.003065 + 1.008665 = 16.011730\text{ u}$$
Mass difference $\Delta m$:
$$\Delta m = m_{\text{reactants}} - m_{\text{products}} = 16.001506 - 16.011730 = -0.010224\text{ u}$$
$Q$-value:
$$Q = -0.010224\text{ u} \times 931.4941\text{ MeV/u} \approx -9.5236\text{ MeV}$$
Because $Q < 0$, the reaction is endoergic.

### Step 2: Threshold Energy $E_{\text{th}}$
Laboratory threshold formula:
$$E_{\text{th}} = |Q| \left(1 + \frac{m_\alpha}{M_C}\right)$$
Using masses $m_\alpha \approx 4.0015\text{ u}$ and $M_C = 12.0000\text{ u}$:
$$\frac{m_\alpha}{M_C} = \frac{4.001506}{12.000000} \approx 0.333459$$
$$E_{\text{th}} = 9.5236\text{ MeV} \times (1 + 0.333459) = 9.5236 \times 1.333459 \approx 12.6995\text{ MeV}$$
The incident alpha particle must have a laboratory kinetic energy of at least **$12.70\text{ MeV}$** to initiate the reaction.""",
                    "hints": ["Mass difference Delta m = reactants - products.", "E_th = |Q| * (1 + m_projectile / M_target)."]
                },
                {
                    "id": "prob-4-2",
                    "problemNumber": "4.2",
                    "title": "Coulomb Barrier and Gamow Tunneling for D-T Fusion",
                    "difficulty": "Easy",
                    "statement": r"""In deuterium-tritium thermonuclear fusion:
$$^2_1\text{H} + ^3_1\text{H} \longrightarrow ^4_2\text{He} + ^1_0n + 17.59\text{ MeV}$$
Given the nuclear radius constant $R_0 = 1.30\text{ fm}$:
1. Calculate the contact radius $R_c = R_D + R_T$ in $\text{fm}$.
2. Determine the classical Coulomb barrier height $V_C$ in $\text{keV}$.
3. Explain why magnetically confined fusion reactors operate at plasma temperatures of $T \approx 15\text{ keV}$ ($150\text{ million K}$), far below $V_C$.""",
                    "solution": r"""### Step 1: Contact Radius $R_c$
$$R_D = R_0 (2)^{1/3} = 1.30 \times 1.2599 \approx 1.638\text{ fm}$$
$$R_T = R_0 (3)^{1/3} = 1.30 \times 1.4422 \approx 1.875\text{ fm}$$
$$R_c = R_D + R_T = 1.638 + 1.875 = 3.513\text{ fm}$$

### Step 2: Classical Coulomb Barrier $V_C$
Both deuteron and triton have $z_1 = 1, z_2 = 1$:
$$V_C = \frac{1}{4\pi\varepsilon_0} \frac{e^2}{R_c} = \frac{1.43996\text{ MeV}\cdot\text{fm}}{3.513\text{ fm}} \approx 0.4099\text{ MeV} = 410\text{ keV}$$

### Step 3: Physical Explanation of Plasma Temperature
Although the classical electrostatic barrier is $410\text{ keV}$:
1. **Gamow Quantum Tunneling**: Nuclei do not need to scale the crest of the barrier; quantum tunneling enables penetration with substantial probability at energies well below $V_C$.
2. **Maxwell-Boltzmann High-Energy Tail**: In a thermal plasma at $15\text{ keV}$, the Maxwellian distribution has an exponential tail where particles with $E \sim 4 - 5 k_B T \approx 60 - 80\text{ keV}$ exist in significant numbers.
3. The convolution of the rising tunneling probability $\exp(-2\pi \eta)$ with the falling Maxwellian distribution $\exp(-E/k_B T)$ forms the **Gamow peak** centered at $\approx 65\text{ keV}$, yielding immense reaction rates at an operating temperature of only $15\text{ keV}$.""",
                    "hints": ["Contact radius is R_1 + R_2 = R_0 * (A_1^(1/3) + A_2^(1/3)).", "Use e^2 / (4*pi*epsilon_0) = 1.44 MeV*fm."]
                },
                {
                    "id": "prob-4-3",
                    "problemNumber": "4.3",
                    "title": "Breit-Wigner Peak Cross-Section for Indium-115 Resonance",
                    "difficulty": "Intermediate",
                    "statement": r"""Indium-115 ($^{115}\text{In}$, ground spin $I_X = 9/2^+$) exhibits a famous thermal/epithermal neutron capture resonance at laboratory energy $E_0 = 1.457\text{ eV}$.
The resonance parameters are:
- Total width $\Gamma = 0.089\text{ eV}$
- Neutron partial width $\Gamma_n = 0.0033\text{ eV}$
- Radiative capture partial width $\Gamma_\gamma = 0.0857\text{ eV}$
- Compound nucleus resonance spin $J = 5$
- Neutron spin $s_a = 1/2$
1. Calculate the statistical spin factor $g_J$.
2. Compute the reduced de Broglie wavelength $\lambdabar$ of the neutron at $E_0$.
3. Calculate the peak radiative capture cross-section $\sigma(n, \gamma)$ at resonance in barns.""",
                    "solution": r"""### Step 1: Statistical Spin Factor $g_J$
$$g_J = \frac{2J + 1}{(2s_a + 1)(2I_X + 1)} = \frac{2(5) + 1}{(2(1/2) + 1)(2(9/2) + 1)} = \frac{11}{(2)(10)} = \frac{11}{20} = 0.550$$

### Step 2: Reduced de Broglie Wavelength $\lambdabar$
Neutron kinetic energy $E_0 = 1.457\text{ eV} = 1.457 \times 1.60218 \times 10^{-19}\text{ J} = 2.3344 \times 10^{-19}\text{ J}$.
Momentum:
$$p = \sqrt{2 m_n E} = \sqrt{2 (1.67493 \times 10^{-27}\text{ kg})(2.3344 \times 10^{-19}\text{ J})} = \sqrt{7.820 \times 10^{-46}} = 2.7964 \times 10^{-23}\text{ kg}\cdot\text{m/s}$$
$$\lambdabar = \frac{\hbar}{p} = \frac{1.05457 \times 10^{-34}\text{ J}\cdot\text{s}}{2.7964 \times 10^{-23}\text{ kg}\cdot\text{m/s}} \approx 3.7712 \times 10^{-12}\text{ m} = 3771.2\text{ fm}$$
$$\pi \lambdabar^2 = \pi (3.7712 \times 10^{-12}\text{ m})^2 = \pi (1.4222 \times 10^{-23}\text{ m}^2) = 4.468 \times 10^{-23}\text{ m}^2$$
In barns ($1\text{ b} = 10^{-28}\text{ m}^2$):
$$\pi \lambdabar^2 = \frac{4.468 \times 10^{-23}\text{ m}^2}{10^{-28}\text{ m}^2/\text{b}} = 446,800\text{ barns}$$

### Step 3: Peak Capture Cross-Section
At resonance peak ($E = E_0$), the energy denominator $(E - E_0)^2 + (\Gamma/2)^2$ reduces to $(\Gamma/2)^2 = \Gamma^2 / 4$:
$$\sigma_{\text{peak}} = 4\pi \lambdabar^2 g_J \frac{\Gamma_n \Gamma_\gamma}{\Gamma^2}$$
Substitute values:
$$\frac{\Gamma_n \Gamma_\gamma}{\Gamma^2} = \frac{(0.0033\text{ eV})(0.0857\text{ eV})}{(0.089\text{ eV})^2} = \frac{0.0002828}{0.007921} \approx 0.03570$$
$$\sigma_{\text{peak}} = 4 \times (446,800\text{ b}) \times (0.550) \times (0.03570) = 1,787,200 \times 0.019636 \approx 35,095\text{ barns}$$
The peak cross section is an astounding **$\approx 35,100\text{ barns}$** (explaining why indium foils are standard neutron detectors).""",
                    "hints": ["Use Breit-Wigner formula at E = E_0: denominator is Gamma^2 / 4.", "Statistical spin factor is (2J+1) / [(2s+1)(2I+1)]."]
                },
                {
                    "id": "prob-4-4",
                    "problemNumber": "4.4",
                    "title": "Macroscopic Cross-Section and Neutron Mean Free Path in Natural Uranium",
                    "difficulty": "Easy",
                    "statement": r"""Pure metallic uranium fuel has a mass density $\rho = 19.1\text{ g/cm}^3$ and atomic weight $M = 238.03\text{ g/mol}$.
For thermal neutrons ($v = 2200\text{ m/s}$):
- Total microscopic scattering cross-section $\sigma_s = 8.3\text{ barns}$
- Total microscopic absorption cross-section $\sigma_a = 7.6\text{ barns}$
1. Calculate the atomic number density $n$ of uranium in $\text{atoms/cm}^3$.
2. Calculate the macroscopic scattering cross-section $\Sigma_s$ and absorption cross-section $\Sigma_a$ in $\text{cm}^{-1}$.
3. Determine the total macroscopic cross-section $\Sigma_t$ and the mean free path $\lambda_{\text{mfp}}$ in centimeters.""",
                    "solution": r"""### Step 1: Number Density $n$
$$n = \frac{\rho N_A}{M} = \frac{(19.1\text{ g/cm}^3)(6.02214 \times 10^{23}\text{ atoms/mol})}{238.03\text{ g/mol}} \approx 4.832 \times 10^{22}\text{ atoms/cm}^3$$

### Step 2: Macroscopic Cross-Sections
Convert barns to $\text{cm}^2$: $1\text{ b} = 10^{-24}\text{ cm}^2$.
1. Scattering:
$$\sigma_s = 8.3 \times 10^{-24}\text{ cm}^2$$
$$\Sigma_s = n \sigma_s = (4.832 \times 10^{22}\text{ cm}^{-3})(8.3 \times 10^{-24}\text{ cm}^2) \approx 0.4011\text{ cm}^{-1}$$

2. Absorption:
$$\sigma_a = 7.6 \times 10^{-24}\text{ cm}^2$$
$$\Sigma_a = n \sigma_a = (4.832 \times 10^{22}\text{ cm}^{-3})(7.6 \times 10^{-24}\text{ cm}^2) \approx 0.3672\text{ cm}^{-1}$$

### Step 3: Total Macroscopic Cross-Section and Mean Free Path
$$\Sigma_t = \Sigma_s + \Sigma_a = 0.4011 + 0.3672 = 0.7683\text{ cm}^{-1}$$
The mean free path between collisions is:
$$\lambda_{\text{mfp}} = \frac{1}{\Sigma_t} = \frac{1}{0.7683\text{ cm}^{-1}} \approx 1.302\text{ cm}$$
A thermal neutron travels on average only **$1.30\text{ cm}$** in metallic uranium before undergoing a nuclear interaction.""",
                    "hints": ["Number density n = rho * N_A / M.", "Macroscopic cross section Sigma = n * sigma, with sigma in cm^2."]
                },
                {
                    "id": "prob-4-5",
                    "problemNumber": "4.5",
                    "title": "Thermal 1/v Cross-Section Scaling to Reactor Operating Temperatures",
                    "difficulty": "Intermediate",
                    "statement": r"""Boron-10 is widely used as a neutron absorber in reactor control rods via the $^{10}\text{B}(n, \alpha)^7\text{Li}$ reaction.
At room temperature ($T_0 = 293.6\text{ K}$, thermal energy $E_0 = 0.0253\text{ eV}$), its capture cross-section is $\sigma_0 = 3,840\text{ barns}$.
Assuming the cross-section strictly obeys the $1/v$ law:
1. Formulate the relationship between effective cross-section $\sigma(T)$ and absolute temperature $T$.
2. Calculate the absorption cross-section of $^{10}\text{B}$ in a pressurized water reactor operating at core temperature $T = 310^\circ\text{C}$ ($583.15\text{ K}$).""",
                    "solution": r"""### Step 1: Temperature Scaling Formulation
For thermal neutrons in Maxwellian equilibrium with a moderator at temperature $T$, the average kinetic energy scales linearly with temperature:
$$\bar{E} = \frac{3}{2} k_B T \implies v_{\text{thermal}} \propto \sqrt{T}$$
According to the $1/v$ law:
$$\sigma(v) \propto \frac{1}{v} \propto \frac{1}{\sqrt{T}}$$
Therefore:
$$\sigma(T) = \sigma_0 \sqrt{\frac{T_0}{T}} = \sigma_0 \sqrt{\frac{E_0}{k_B T}}$$

### Step 2: Numerical Calculation at Reactor Operating Temperature
Reference temperature: $T_0 = 293.6\text{ K}$ ($20.45^\circ\text{C}$).
Operating temperature: $T = 310 + 273.15 = 583.15\text{ K}$.
Temperature ratio:
$$\frac{T_0}{T} = \frac{293.6\text{ K}}{583.15\text{ K}} \approx 0.50347$$
Square root factor:
$$\sqrt{\frac{T_0}{T}} = \sqrt{0.50347} \approx 0.70956$$
Effective absorption cross-section:
$$\sigma(583.15\text{ K}) = 3,840\text{ b} \times 0.70956 \approx 2,725\text{ barns}$$
At $310^\circ\text{C}$, the cross-section decreases by nearly **$30\%$** due to thermal spectral hardening.""",
                    "hints": ["Remember that thermal velocity scales as sqrt(T), so cross-section scales as 1/sqrt(T).", "Always convert Celsius to Kelvin!"]
                },
                {
                    "id": "prob-4-6",
                    "problemNumber": "4.6",
                    "title": "Two-Body Reaction Ejectile Energy as Function of Emission Angle",
                    "difficulty": "Advanced",
                    "statement": r"""In the exoergic reaction $^7_3\text{Li}(p, \alpha)^4_2\text{He}$ ($Q = +17.347\text{ MeV}$), incident protons with kinetic energy $T_p = 3.00\text{ MeV}$ strike stationary lithium-7.
1. Using non-relativistic kinematics, derive the exact formula for ejectile kinetic energy $T_\alpha(\theta)$ as a function of laboratory emission angle $\theta$.
2. Calculate the kinetic energy of the alpha particle emitted at $\theta = 0^\circ$ (forward) and $\theta = 90^\circ$ (perpendicular).""",
                    "solution": r"""### Step 1: Kinematic Derivation
Let projectile $a$ ($p$, mass $m_a$), target $X$ ($^7\text{Li}$, mass $M_X$), ejectile $b$ ($\alpha$, mass $m_b$), and recoil $Y$ ($^4\text{He}$, mass $M_Y$).
By conservation of momentum:
$$\vec{p}_Y = \vec{p}_a - \vec{p}_b$$
$$p_Y^2 = p_a^2 + p_b^2 - 2 p_a p_b \cos\theta$$
Dividing by $2 M_Y$:
$$T_Y = \frac{p_Y^2}{2 M_Y} = \frac{m_a}{M_Y} T_a + \frac{m_b}{M_Y} T_b - \frac{2 \sqrt{m_a m_b}}{M_Y} \sqrt{T_a T_b} \cos\theta$$
Substitute into $Q = T_b + T_Y - T_a$:
$$Q = T_b + \left[ \frac{m_a}{M_Y} T_a + \frac{m_b}{M_Y} T_b - \frac{2 \sqrt{m_a m_b}}{M_Y} \sqrt{T_a T_b} \cos\theta \right] - T_a$$
Group powers of $\sqrt{T_b}$:
$$\left(1 + \frac{m_b}{M_Y}\right) T_b - \left(\frac{2 \sqrt{m_a m_b T_a}}{M_Y} \cos\theta\right) \sqrt{T_b} - \left[ Q + T_a\left(1 - \frac{m_a}{M_Y}\right) \right] = 0$$
Let:
$$A = \frac{M_Y + m_b}{M_Y}, \quad B = \frac{2 \sqrt{m_a m_b T_a} \cos\theta}{M_Y}, \quad C = Q + T_a\left(\frac{M_Y - m_a}{M_Y}\right)$$
The quadratic equation $A (\sqrt{T_b})^2 - B \sqrt{T_b} - C = 0$ yields:
$$\sqrt{T_b} = \frac{B + \sqrt{B^2 + 4 A C}}{2 A}$$

### Step 2: Numerical Calculation
Masses: $m_a \approx 1$, $M_X \approx 7$, $m_b \approx 4$, $M_Y \approx 4$.
$T_a = 3.00\text{ MeV}$, $Q = 17.347\text{ MeV}$.
- $A = \frac{4 + 4}{4} = 2.00$
- $C = 17.347 + 3.00\left(\frac{4 - 1}{4}\right) = 17.347 + 3.00(0.75) = 17.347 + 2.250 = 19.597\text{ MeV}$

1. **At $\theta = 0^\circ$ ($\cos 0^\circ = 1$)**:
$$B = \frac{2 \sqrt{1 \times 4 \times 3.00}}{4} (1) = \frac{2 \sqrt{12}}{4} = \frac{\sqrt{12}}{2} = \sqrt{3} \approx 1.73205$$
$$B^2 + 4 A C = 3 + 4(2.00)(19.597) = 3 + 156.776 = 159.776$$
$$\sqrt{B^2 + 4 A C} = \sqrt{159.776} \approx 12.64025$$
$$\sqrt{T_\alpha} = \frac{1.73205 + 12.64025}{4.00} = \frac{14.3723}{4.00} \approx 3.59308$$
$$T_\alpha(0^\circ) = (3.59308)^2 \approx 12.91\text{ MeV}$$

2. **At $\theta = 90^\circ$ ($\cos 90^\circ = 0 \implies B = 0$)**:
$$\sqrt{T_\alpha} = \frac{\sqrt{4 A C}}{2 A} = \sqrt{\frac{C}{A}} = \sqrt{\frac{19.597}{2.00}} = \sqrt{9.7985} \approx 3.13025$$
$$T_\alpha(90^\circ) = 9.80\text{ MeV}$$""",
                    "hints": ["Eliminate recoil momentum p_Y by setting p_Y^2 = p_a^2 + p_b^2 - 2*p_a*p_b*cos(theta).", "Solve the quadratic equation for sqrt(T_b)."]
                },
                {
                    "id": "prob-4-7",
                    "problemNumber": "4.7",
                    "title": "Ghoshal Compound Nucleus Verification Calculation",
                    "difficulty": "Intermediate",
                    "statement": r"""In Ghoshal's classic 1950 test of the Bohr independence hypothesis, the compound nucleus $^{64}_{30}\text{Zn}^*$ was formed via:
Channel A: $p + ^{63}_{29}\text{Cu} \to [^{64}_{30}\text{Zn}^*]$ ($Q_A = +7.71\text{ MeV}$)
Channel B: $\alpha + ^{60}_{28}\text{Ni} \to [^{64}_{30}\text{Zn}^*]$ ($Q_B = +3.98\text{ MeV}$)
1. For an incident proton kinetic energy $T_p^{\text{lab}} = 12.00\text{ MeV}$, calculate the excitation energy $E^*$ of the compound nucleus $^{64}\text{Zn}^*$.
2. Determine the laboratory alpha particle energy $T_\alpha^{\text{lab}}$ required to produce $^{64}\text{Zn}^*$ at the exact same excitation energy.""",
                    "solution": r"""### Step 1: Compound Nucleus Excitation Energy from Channel A
In channel A, the center-of-mass kinetic energy is:
$$T_{\text{CM}, A} = \left(\frac{M_{\text{Cu}}}{m_p + M_{\text{Cu}}}\right) T_p^{\text{lab}} = \left(\frac{63}{1 + 63}\right) 12.00\text{ MeV} = \frac{63}{64} \times 12.00 = 11.8125\text{ MeV}$$
The excitation energy $E^*$ equals the center-of-mass kinetic energy plus the reaction $Q$-value:
$$E^* = T_{\text{CM}, A} + Q_A = 11.8125\text{ MeV} + 7.71\text{ MeV} = 19.5225\text{ MeV}$$

### Step 2: Required Incident Alpha Energy from Channel B
For channel B to create the identical compound nucleus:
$$E^* = T_{\text{CM}, B} + Q_B = 19.5225\text{ MeV}$$
$$T_{\text{CM}, B} = E^* - Q_B = 19.5225\text{ MeV} - 3.98\text{ MeV} = 15.5425\text{ MeV}$$
Convert CM energy to laboratory frame for incident alpha:
$$T_{\text{CM}, B} = \left(\frac{M_{\text{Ni}}}{m_\alpha + M_{\text{Ni}}}\right) T_\alpha^{\text{lab}} = \left(\frac{60}{4 + 60}\right) T_\alpha^{\text{lab}} = \frac{60}{64} T_\alpha^{\text{lab}} = \frac{15}{16} T_\alpha^{\text{lab}}$$
$$T_\alpha^{\text{lab}} = \frac{16}{15} T_{\text{CM}, B} = \frac{16}{15} \times 15.5425\text{ MeV} \approx 16.5787\text{ MeV}$$
Incident alphas at **$16.58\text{ MeV}$** create the compound state at the identical excitation energy as protons at $12.00\text{ MeV}$.""",
                    "hints": ["Excitation energy E* = T_CM + Q.", "Remember to scale between LAB and CM frames using the reduced mass ratio."]
                }
            ]
        },

        # =====================================================================
        # UNIT 5
        # =====================================================================
        {
            "id": "unit-5-nuclear-fission-reactor-physics",
            "unitNumber": 5,
            "title": "Unit 5: Nuclear Fission Mechanics & Reactor Physics",
            "leadSummary": "Comprehensive physical and technological exposition of nuclear fission: the historical discovery by Hahn, Strassmann, Meitner, and Frisch; the Bohr-Wheeler liquid drop fission barrier; the asymmetric double-hump fragment mass yield curve; prompt versus delayed neutron kinetics; neutron moderation dynamics; the four-factor and six-factor criticality equations; and modern nuclear reactor systems.",
            "simulations": ["sim_nuc_fission_chain_reactor"],
            "sections": [
                {
                    "id": "sec-5-1",
                    "secNumber": "5.1",
                    "title": "Historical Discovery & Thermodynamics of Nuclear Fission: Hahn, Meitner & Frisch",
                    "content": r"""In December 1938, German radiochemists Otto Hahn and Fritz Strassmann at the Kaiser Wilhelm Institute in Berlin irradiated natural uranium with thermal neutrons. Expecting to identify transuranic elements ($Z > 92$), they performed fractional crystallization with barium carriers. Astonishingly, the radioactivity precipitated identically with barium ($Z = 56$), an element whose mass is barely half that of uranium.

### The Meitner-Frisch Theoretical Interpretation (January 1939)
In exile in Sweden, Lise Meitner and her nephew Otto Frisch interpreted the result using George Gamow and Niels Bohr's Liquid Drop Model of the nucleus:
$$^{235}_{92}\text{U} + ^{1}_{0}n \longrightarrow [^{236}_{92}\text{U}^*] \longrightarrow ^{141}_{56}\text{Ba} + ^{92}_{36}\text{Kr} + 3 \, ^{1}_{0}n + Q$$
Frisch coined the term **fission** by analogy with binary fission in cellular biology.

### Energetic Partition of Nuclear Fission
The total energy released per fission of uranium-235 is approximately **$200\text{ MeV}$** ($\approx 3.204 \times 10^{-11}\text{ J}$).
This immense thermodynamic yield arises from the drop in binding energy per nucleon: from $\approx 7.6\text{ MeV/nucleon}$ for $^{235}\text{U}$ to $\approx 8.5\text{ MeV/nucleon}$ for mid-mass fission fragments:
$$Q \approx 235 \times (8.5 - 7.6)\text{ MeV} \approx 200\text{ MeV}$$

```
 ENERGY COMPONENT                                     TYPICAL VALUE   FRACTION
 ─────────────────────────────────────────────────────────────────────────────
 Kinetic Energy of Fission Fragments (Prompt)        ~ 168 MeV        84.0%
 Kinetic Energy of Prompt Neutrons (~2.4 per fission) ~ 5 MeV           2.5%
 Prompt Gamma-Ray Photons                            ~ 7 MeV           3.5%
 Beta- Particles from Radioactive Fission Fragments  ~ 8 MeV           4.0%
 Antineutrinos (ν̄_e, escape reactor core completely)  ~ 12 MeV          6.0%
 Delayed Gamma Photons from Fragment Decay Chains    ~ 7 MeV           3.5%
 ─────────────────────────────────────────────────────────────────────────────
 TOTAL FISSION ENERGY RELEASE:                       ~ 207 MeV        100.0%
 RECOVERABLE THERMAL CORE ENERGY:                    ~ 195 MeV        94.0%
```

Over $80\%$ of the energy appears as kinetic energy of the two massive, highly charged fission fragments. They travel a mere $\sim 10\,\mu\text{m}$ in uranium metal before stopping, converting their kinetic energy into intense localized thermal heat via Coulomb ionization collisions.""",
                    "simulations": ["sim_nuc_fission_chain_reactor"]
                },
                {
                    "id": "sec-5-2",
                    "secNumber": "5.2",
                    "title": "The Bohr-Wheeler Liquid Drop Fission Barrier & Fissility Parameter",
                    "content": r"""In their 1939 paper, Niels Bohr and John Archibald Wheeler formulated the definitive classical theory of nuclear fission. They modeled the nucleus as an incompressible, charged liquid drop undergoing ellipsoidal quadrupole deformation.

### Deformation Energy of a Liquid Drop
Consider a spherical nucleus of radius $R_0$ distorted into an axisymmetric prolate spheroid with semi-major axis $a = R_0(1 + \epsilon)$ and semi-minor axis $b = R_0(1 - \epsilon/2)$, where $\epsilon$ is the eccentricity deformation parameter:
- **Volume**: Conserved ($\frac{4}{3}\pi a b^2 = \frac{4}{3}\pi R_0^3$).
- **Surface Area**: Increases with deformation:
$$S(\epsilon) = S_0 \left( 1 + \frac{2}{5} \epsilon^2 + \dots \right)$$
- **Coulomb Self-Energy**: Decreases with deformation (charge is pushed further apart):
$$E_C(\epsilon) = E_C^0 \left( 1 - \frac{1}{5} \epsilon^2 + \dots \right)$$

The net change in nuclear potential energy $\Delta E$ relative to the spherical ground state is:
$$\Delta E = \Delta E_S + \Delta E_C = E_S^0 \left( \frac{2}{5} \epsilon^2 \right) - E_C^0 \left( \frac{1}{5} \epsilon^2 \right) = \frac{1}{5} \epsilon^2 \left( 2 E_S^0 - E_C^0 \right)$$

```
   Potential Energy ΔE(ε)
      ▲
      │           /\  Fission Barrier E_f
      │          /  \
      │         /    \
      │        /      \____ Spontaneous Fission (Scission)
      │  ___  /
    0 ┼─( O )/────────────────► Deformation ε
        Spherical Ground State
```

### The Fissility Parameter ($x$)
The condition for spontaneous instability against infinitesimal deformation ($\Delta E < 0$) is:
$$2 E_S^0 - E_C^0 < 0 \implies \frac{E_C^0}{2 E_S^0} > 1$$
We define the dimensionless **Fissility Parameter** $x$:
$$x \equiv \frac{E_C^0}{2 E_S^0}$$
Substituting the SEMF expressions $E_S^0 = a_s A^{2/3}$ and $E_C^0 = a_c Z^2 / A^{1/3}$:
$$x = \frac{a_c \frac{Z^2}{A^{1/3}}}{2 a_s A^{2/3}} = \frac{a_c}{2 a_s} \left(\frac{Z^2}{A}\right)$$
Using $a_c \approx 0.711\text{ MeV}$ and $a_s \approx 17.80\text{ MeV}$:
$$\left(\frac{Z^2}{A}\right)_{\text{crit}} = \frac{2 a_s}{a_c} \approx \frac{2(17.80)}{0.711} \approx 50.1$$
$$x = \frac{Z^2 / A}{(Z^2 / A)_{\text{crit}}} \approx \frac{Z^2 / A}{50.1}$$

- If $x \ge 1.0$ ($Z^2/A \ge 50$): The spherical nucleus is unstable to immediate spontaneous fission ($\tau \sim 10^{-22}\text{ s}$).
- If $x < 1.0$: A finite **Fission Barrier** $E_f$ opposes deformation.

### Fissile Versus Fertile Radionuclides
- **Fissile Radionuclides**: Capable of undergoing fission with **zero-energy thermal neutrons** ($0.025\text{ eV}$). Examples: $^{233}\text{U}, ^{235}\text{U}, ^{239}\text{Pu}, ^{241}\text{Pu}$.
- **Fertile Radionuclides**: Do not fission with thermal neutrons because neutron binding energy $S_n < E_f$. They require fast neutrons ($E_n > 1.0\text{ MeV}$) to fission, but can capture a thermal neutron to breed a fissile isotope. Examples: $^{238}\text{U} \to ^{239}\text{Pu}$, $^{232}\text{Th} \to ^{233}\text{U}$.

The difference is rooted in the **pairing energy**:
When an odd-neutron nucleus ($^{235}_{92}\text{U}$) captures a neutron, it forms an even-even compound state ($[^{236}_{92}\text{U}^*]$), releasing an extra $+1.2\text{ MeV}$ of pairing binding energy ($S_n = 6.55\text{ MeV}$), which exceeds the $5.7\text{ MeV}$ fission barrier!
Capturing a neutron on even-even $^{238}_{92}\text{U}$ forms an odd-neutron state ($[^{239}_{92}\text{U}^*]$) with zero pairing bonus ($S_n = 4.80\text{ MeV}$), falling short of the $6.2\text{ MeV}$ barrier.""",
                    "simulations": ["sim_nuc_fission_chain_reactor"]
                },
                {
                    "id": "sec-5-3",
                    "secNumber": "5.3",
                    "title": "Energetics & Mass Distribution of Fission Fragments: Asymmetric Double-Hump Yields",
                    "content": r"""When a heavy nucleus such as uranium-235 undergoes low-energy thermal fission, it does not split into two equal halves ($A_1 = A_2 \approx 117$). Instead, the fragment mass yield distribution exhibits a pronounced **asymmetric double-humped morphology**.

```
 Fragment Yield (%)
  10 ▲        Peak 1 (Light)           Peak 2 (Heavy)
     │          A ≈ 95                   A ≈ 138
   8 │          (Kr, Sr, Zr)             (Xe, Cs, Ba)
     │          __                       __
   6 │         /  \                     /  \
     │        /    \                   /    \
   4 │       /      \                 /      \
     │      /        \               /        \
   2 │     /          \    Valley   /          \
     │____/            \__(A ≈ 117)/            \____
   0 └────┴─────────────┴──────────┴─────────────┴────► Mass Number A
          70            95        117           140   160
```

### The Double-Hump Peak Characteristics
For thermal neutron fission of $^{235}\text{U}$:
1. **Light Fragment Group**: Centered around $A_L \approx 95$ ($Z \approx 36 - 40$, elements $\text{Kr}, \text{Rb}, \text{Sr}, \text{Y}, \text{Zr}$).
2. **Heavy Fragment Group**: Centered around $A_H \approx 138$ ($Z \approx 53 - 57$, elements $\text{I}, \text{Xe}, \text{Cs}, \text{Ba}, \text{La}$).
3. **Symmetric Valley**: Symmetric fission ($A \approx 117$) occurs with a probability of less than **$0.01\%$** ($\sim 600$ times less frequent than asymmetric fission).

### Physical Origin: Quantum Shell Effects
The dominance of asymmetric fission is governed by **nuclear shell closures**:
The heavy fragment peak is anchored by the proximity of the doubly magic spherical shell closure:
$$Z = 50 \text{ (Protons)}, \quad N = 82 \text{ (Neutrons)} \implies ^{132}_{50}\text{Sn}_{82}$$
The extraordinary shell stabilization of nascent fragments near $Z = 50$ and $N = 82$ energetically favors asymmetric neck scission.

At high incident excitation energies ($E_n > 40\text{ MeV}$), individual single-particle shell structures wash out, and the fragment yield curve transitions into a single symmetric Gaussian peak centered at $A/2$.""",
                    "simulations": ["sim_nuc_fission_chain_reactor"]
                },
                {
                    "id": "sec-5-4",
                    "secNumber": "5.4",
                    "title": "Prompt and Delayed Neutrons: Precursor Kinetics & Reactor Control Stability",
                    "content": r"""In every fission event, an average of $\bar{\nu} \approx 2.4 - 3.0$ neutrons are released. Crucially for nuclear engineering, these neutrons are emitted via two distinct physical mechanisms:

### 1. Prompt Neutrons ($>99\%$)
Emitted directly from the scission neck and evaporating fragments within $\tau_{\text{prompt}} \sim 10^{-14}\text{ seconds}$ of scission.
They exhibit a continuous Maxwellian fission spectrum (Watt spectrum):
$$\chi(E) = c \cdot \sqrt{E} \exp(-E / E_0) \quad \text{with average energy } \bar{E} \approx 2.0\text{ MeV}$$

### 2. Delayed Neutrons ($<1\%$)
Fission fragments are neutron-rich and undergo cascades of negative beta decays. In certain daughter nuclei (termed **delayed neutron precursors**), the beta decay Q-value exceeds the neutron separation energy ($Q_\beta > S_n$).
The daughter is formed in an excited state that promptly ($<10^{-14}\text{ s}$) de-excites by boiling off a neutron:

```
  FISSION FRAGMENT PRECURSOR (e.g., ⁸⁷₃₅Br, T₁/₂ = 55.6 s)
        │
        ▼ (β⁻ decay, slow: governed by T₁/₂)
  EXCITED DAUGHTER [⁸⁷₃₆Kr*] (Excitation E* > S_n)
        │
        ▼ (Prompt neutron emission, fast: <10⁻¹⁴ s)
  STABLE RESIDUAL ⁸⁶₃₆Kr + ¹₀n (DELAYED NEUTRON!)
```

The appearance of the delayed neutron is rate-limited not by nuclear forces, but by the **half-life of the preceding beta decay**!

### Precursor Groups and the Delayed Neutron Fraction ($\beta$)
The fraction of all fission neutrons that are delayed is defined as $\beta$:
$$\beta \equiv \frac{\text{Delayed Neutrons}}{\text{Total Neutrons}} = \begin{cases} 0.0065 \quad (0.65\%) & \text{for } ^{235}\text{U} \\ 0.0021 \quad (0.21\%) & \text{for } ^{239}\text{Pu} \end{cases}$$

Delayed neutrons are categorized into six empirical precursor groups:

| Group $i$ | Representative Precursor | Half-Life $T_{1/2,i}$ | Decay Constant $\lambda_i$ ($\text{s}^{-1}$) | Yield Fraction $\beta_i$ ($^{235}\text{U}$) |
| :--- | :--- | :--- | :--- | :--- |
| **1** | $^{87}\text{Br}$ | $55.6\text{ s}$ | $0.0124$ | $0.00021$ |
| **2** | $^{137}\text{I}$ | $24.5\text{ s}$ | $0.0283$ | $0.00142$ |
| **3** | $^{138}\text{I}, ^{89}\text{Br}$ | $16.3\text{ s}$ | $0.0425$ | $0.00127$ |
| **4** | $^{139}\text{I}, ^{93}\text{Kr}$ | $5.21\text{ s}$ | $0.1330$ | $0.00257$ |
| **5** | $^{140}\text{I}, ^{91}\text{Br}$ | $2.37\text{ s}$ | $0.2920$ | $0.00075$ |
| **6** | $^{97}\text{Rb}$ | $0.23\text{ s}$ | $3.0100$ | $0.00028$ |
| **Total** | — | — | **$\bar{\tau}_d \approx 12.7\text{ s}$** | **$\beta = 0.00650$** |

### Criticality and Reactor Control Physics
Without delayed neutrons, the average neutron generation lifetime in a thermal reactor would be $\Lambda \approx l_p \approx 10^{-4}\text{ seconds}$.
If reactivity increased by just $\Delta k = +0.001$, reactor power would escalate as:
$$P(t) = P_0 \exp\left(\frac{\Delta k}{\Lambda} t\right) = P_0 \exp\left(\frac{0.001}{10^{-4}} t\right) = P_0 e^{10 t} \approx P_0 (22,000)^t$$
Power would multiply by 22,000 every single second, rendering mechanical control impossible.

With delayed neutrons, the effective neutron lifetime is dominated by precursor half-lives:
$$\Lambda_{\text{eff}} \approx (1 - \beta) l_p + \beta \bar{\tau}_d \approx (1 - 0.0065)(10^{-4}) + 0.0065(12.7\text{ s}) \approx 0.083\text{ seconds}$$
Power response slows by a factor of nearly $1,000$, enabling mechanical control rods to manage power levels safely.
- **Prompt Criticality** ($\rho \ge \beta$ or $k \ge 1 + \beta$): The reactor is critical on prompt neutrons alone; power explodes uncontrollably (Chernobyl scenario).
- **Delayed Criticality** ($1.000 \le k < 1 + \beta$): The normal, stable operational regime where criticality requires delayed neutrons.""",
                    "simulations": ["sim_nuc_fission_chain_reactor"]
                },
                {
                    "id": "sec-5-5",
                    "secNumber": "5.5",
                    "title": "Neutron Moderation Kinetics: Elastic Collisions, Logarithmic Decrement & Moderator Selection",
                    "content": r"""Prompt fission neutrons are born with high kinetic energies averaging $E_0 \approx 2\text{ MeV}$. However, the fission cross-section of $^{235}\text{U}$ is hundreds of times higher for thermal neutrons ($E_{\text{th}} \approx 0.025\text{ eV}$). To sustain a thermal chain reaction, fast neutrons must be slowed down via elastic collisions with moderator nuclei.

### Elastic Collision Kinematics in the LAB Frame
Consider a neutron of mass $m = 1$ colliding elastically with a stationary moderator nucleus of mass number $A$.
By conservation of momentum and energy in the center-of-mass frame, the ratio of final neutron energy $E'$ to initial energy $E$ after scattering through CM angle $\theta$ is:
$$\frac{E'}{E} = \frac{1 + A^2 + 2A \cos\theta}{(1 + A)^2}$$
- **Minimum Energy (Head-On Collision, $\theta = \pi$)**:
$$\left(\frac{E'}{E}\right)_{\min} = \left(\frac{A - 1}{A + 1}\right)^2 \equiv \alpha$$
where $\alpha = \left(\frac{A - 1}{A + 1}\right)^2$ is the collision parameter.
- For hydrogen ($A = 1$): $\alpha = 0$. A neutron can transfer **$100\%$** of its kinetic energy in a single collision!
- For carbon ($A = 12$): $\alpha = (11/13)^2 \approx 0.716$. The neutron retains at least $71.6\%$ of its energy.

### The Average Logarithmic Energy Decrement ($\xi$)
Because neutron energy loss is multiplicative rather than additive, the slowing-down power is characterized by the average decrease in the natural logarithm of energy per collision:
$$\xi \equiv \left\langle \ln\left(\frac{E}{E'}\right) \right\rangle = \int_\alpha^1 \ln\left(\frac{E}{E'}\right) P\left(\frac{E'}{E}\right) d\left(\frac{E'}{E}\right)$$
For isotropic s-wave scattering in the CM frame, $P(E'/E) = \frac{1}{1 - \alpha}$. Evaluating the integral:
$$\xi = 1 + \frac{(A - 1)^2}{2A} \ln\left(\frac{A - 1}{A + 1}\right) = 1 + \frac{\alpha \ln\alpha}{1 - \alpha}$$
For $A > 10$, this is approximated by:
$$\xi \approx \frac{2}{A + 2/3}$$

### Number of Collisions to Thermalize ($N_{\text{coll}}$)
The average number of collisions required to slow a neutron from fission energy $E_0 = 2\text{ MeV}$ to thermal energy $E_{\text{th}} = 0.025\text{ eV}$ is:
$$N_{\text{coll}} = \frac{\ln(E_0 / E_{\text{th}})}{\xi} = \frac{\ln(2 \times 10^6 / 0.025)}{\xi} = \frac{\ln(8.0 \times 10^7)}{\xi} = \frac{18.2}{\xi}$$

| Moderator | Mass Number $A$ | $\alpha = \left(\frac{A-1}{A+1}\right)^2$ | Decrement $\xi$ | Collisions to Thermalize $N_{\text{coll}}$ | Moderating Ratio ($\xi \Sigma_s / \Sigma_a$) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Light Water ($\text{H}_2\text{O}$)** | $1$ | $0.000$ | $1.000$ | **$18$** | $71$ |
| **Heavy Water ($\text{D}_2\text{O}$)** | $2$ | $0.111$ | $0.725$ | **$25$** | **$5,670$** |
| **Beryllium ($\text{Be}$)** | $9$ | $0.640$ | $0.207$ | **$86$** | $143$ |
| **Graphite ($\text{C}$)** | $12$ | $0.716$ | $0.158$ | **$115$** | $192$ |

Heavy water ($\text{D}_2\text{O}$) has the highest **moderating ratio** ($\xi \Sigma_s / \Sigma_a = 5,670$) because deuterium has an exceptionally small neutron capture cross-section ($0.5\text{ mb}$ vs $332\text{ mb}$ for $^1\text{H}$), enabling CANDU reactors to operate using **natural, unenriched uranium**.""",
                    "simulations": ["sim_nuc_fission_chain_reactor"]
                },
                {
                    "id": "sec-5-6",
                    "secNumber": "5.6",
                    "title": "Nuclear Chain Reactions: The Four-Factor Formula, Six-Factor Formula & Criticality Metrics",
                    "content": r"""The operational state of a nuclear reactor is governed by the **effective neutron multiplication factor** $k_{\text{eff}}$, defined as:
$$k_{\text{eff}} \equiv \frac{\text{Neutrons produced in generation } n+1}{\text{Neutrons absorbed or lost in generation } n}$$
- **Subcritical** ($k_{\text{eff}} < 1$): Chain reaction dies out exponentially; power decreases.
- **Critical** ($k_{\text{eff}} = 1.0000$): Steady-state chain reaction; power is exactly constant.
- **Supercritical** ($k_{\text{eff}} > 1$): Chain reaction diverges; power increases exponentially.

### The Four-Factor Formula for Infinite Media ($k_\infty$)
In an infinitely large reactor (where leakage is zero), the multiplication factor is governed by Fermi's **Four-Factor Formula**:
$$k_\infty = \eta \cdot \epsilon \cdot p \cdot f$$

```
 Fast Neutrons from Thermal Fission: η * f
            │
            ▼ Fast Fission Bonus (* ε)
 Total Fast Neutrons: ε * η * f
            │
            ▼ Resonance Escape (* p)
 Neutrons Reaching Thermal Energy: p * ε * η * f
            │
            ▼ Thermal Utilization (* f)
 Thermal Neutrons Absorbed in Fuel: f * p * ε * η * f  ──► Next Generation!
```

1. **Reproduction Factor ($\eta$)**:
Average number of fission neutrons produced per thermal neutron absorbed in the fuel:
$$\eta = \nu \frac{\Sigma_f^F}{\Sigma_a^F} = \nu \frac{\sigma_f^{235} N_{235}}{\sigma_a^{235} N_{235} + \sigma_a^{238} N_{238}}$$
For natural uranium, $\eta \approx 1.34$; for $3.5\%$ enriched fuel, $\eta \approx 1.80$.

2. **Fast Fission Factor ($\epsilon$)**:
Ratio of total fast neutrons (including those from fast fission of $^{238}\text{U}$) to neutrons from thermal fission alone:
$$\epsilon \approx 1.03 - 1.07$$

3. **Resonance Escape Probability ($p$)**:
Probability that a fast neutron slows down through the broad $^{238}\text{U}$ resonance absorption capture peaks ($10\text{ eV} - 1\text{ keV}$) without being absorbed:
$$p = \exp\left( -\frac{N_{238}}{\xi \Sigma_s} I_{\text{eff}} \right) \approx 0.85 - 0.92$$
Using heterogeneous fuel rods separated by moderator increases $p$ because neutrons slow down in the moderator away from $^{238}\text{U}$.

4. **Thermal Utilization Factor ($f$)**:
Fraction of thermal neutrons absorbed in the nuclear fuel compared to total thermal absorptions across fuel, moderator, cladding, and structure:
$$f = \frac{\Sigma_a^{\text{fuel}}}{\Sigma_a^{\text{fuel}} + \Sigma_a^{\text{mod}} + \Sigma_a^{\text{clad}} + \Sigma_a^{\text{poisons}}} \approx 0.88 - 0.95$$

### The Six-Factor Formula for Finite Reactors ($k_{\text{eff}}$)
In a real finite reactor core, neutrons can leak out across the boundary:
$$k_{\text{eff}} = k_\infty \cdot P_{NL,f} \cdot P_{NL,\text{th}} = \eta \cdot \epsilon \cdot p \cdot f \cdot P_{NL,f} \cdot P_{NL,\text{th}}$$
where:
- $P_{NL,f} = \frac{1}{1 + M_f^2 B_g^2} \approx \frac{1}{1 + \tau_F B_g^2}$ is the fast non-leakage probability (Fermi age $\tau_F$).
- $P_{NL,\text{th}} = \frac{1}{1 + L_{\text{th}}^2 B_g^2}$ is the thermal non-leakage probability ($L_{\text{th}}$ = thermal diffusion length).
- $B_g^2$ is the geometric buckling of the core geometry (e.g., $B_g^2 = (\pi/H)^2 + (2.405/R)^2$ for a finite cylinder).

The reactivity $\rho$ of a reactor core is defined as:
$$\rho \equiv \frac{k_{\text{eff}} - 1}{k_{\text{eff}}}$$
Reactivity is measured in percent ($\%\Delta k/k$), parts per hundred thousand ($\text{pcm} = 10^{-5}$), or dollars ($\$ = \rho / \beta$).""",
                    "simulations": ["sim_nuc_fission_chain_reactor"]
                },
                {
                    "id": "sec-5-7",
                    "secNumber": "5.7",
                    "title": "Commercial Reactor Architectures: PWR, BWR, CANDU, Fast Breeder Reactors & Safety Systems",
                    "content": r"""Commercial nuclear power generation utilizes distinct reactor designs engineered around specific neutron moderation, cooling, and isotopic fuel cycles.

### 1. Pressurized Water Reactor (PWR)
The dominant global reactor technology ($>65\%$ of worldwide capacity).
- **Coolant & Moderator**: Light water ($\text{H}_2\text{O}$) under high pressure ($15.5\text{ MPa} \approx 155\text{ bar}$) to prevent bulk boiling at operating temperatures of $\sim 315^\circ\text{C}$.
- **Steam Cycle**: Two distinct circuits (primary and secondary). The hot radioactive primary water passes through U-tube steam generators, boiling secondary water to drive the steam turbine.
- **Fuel**: Low-enriched uranium ($\text{UO}_2$ pellets, $3.0 - 5.0\%$ $^{235}\text{U}$) in Zircaloy cladding.

### 2. Boiling Water Reactor (BWR)
- **Coolant & Moderator**: Light water at lower operating pressure ($7.0\text{ MPa} \approx 70\text{ bar}$).
- **Steam Cycle**: Direct single loop. Water boils directly in the reactor core ($12 - 15\%$ steam void fraction at core exit), and radioactive steam flows straight to the turbine.
- **Control Rods**: Inserted from the **bottom** of the pressure vessel (because steam voids at the top reduce moderation, shifting flux to the bottom).

### 3. CANDU (Canada Deuterium Uranium)
- **Coolant & Moderator**: Heavy water ($\text{D}_2\text{O}$) in separate circuits. The low-pressure moderator is contained in a horizontal calandria vessel traversed by hundreds of pressurized fuel channels.
- **Fuel**: **Natural uranium** ($0.72\% \, ^{235}\text{U}$). Enabled by the low neutron capture of deuterium.
- **Refueling**: On-line refueling while operating at full power.

### 4. Liquid Metal Fast Breeder Reactor (LMFBR)
- **Moderator**: None (operates on fast neutron spectrum, $E_n > 100\text{ keV}$).
- **Coolant**: Liquid sodium ($\text{Na}$) or lead-bismuth eutectic at atmospheric pressure, with thermal conductivity $\sim 100\times$ water.
- **Breeding Cycle**: Breeds more fissile $^{239}\text{Pu}$ from $^{238}\text{U}$ blankets than it consumes ($BR > 1.0$), multiplying available nuclear fuel reserves by a factor of 60.

```
 REACTOR TYPE   MODERATOR    COOLANT       FUEL ENRICHMENT   THERMAL EFFICIENCY
 ──────────────────────────────────────────────────────────────────────────────
 PWR            Light Water  Water (15 MPa) 3.2 - 4.9% ²³⁵U   ~ 33 - 34%
 BWR            Light Water  Steam/Water    3.0 - 4.5% ²³⁵U   ~ 33 - 34%
 CANDU          Heavy Water  Heavy Water   Natural (0.72%)   ~ 30 - 31%
 LMFBR          None (Fast)  Liquid Sodium  15 - 20% ²³⁹Pu/U  ~ 39 - 41%
 HTGR           Graphite     Helium Gas    8 - 15% ²³⁵U      ~ 45 - 50%
```

### Inherent Passive Safety Principles
Modern Generation III+ and IV reactors incorporate **passive safety mechanisms** that operate without electrical power or operator intervention:
- **Negative Doppler Temperature Coefficient**: As fuel temperature rises, thermal agitation broadens $^{238}\text{U}$ resonance capture peaks (Doppler broadening), absorbing more neutrons and automatically shutting down the chain reaction.
- **Negative Moderator Void Coefficient**: Boiling of water removes moderator, decreasing reactivity.""",
                    "simulations": ["sim_nuc_fission_chain_reactor"]
                }
            ],
            "problems": [
                {
                    "id": "prob-5-1",
                    "problemNumber": "5.1",
                    "title": "Four-Factor Formula and Infinite Multiplication Factor Calculation",
                    "difficulty": "Easy",
                    "statement": r"""A low-enriched thermal reactor fuel lattice has the following neutron parameters:
- Reproduction factor $\eta = 1.340$
- Fast fission factor $\epsilon = 1.035$
- Resonance escape probability $p = 0.890$
- Thermal utilization factor $f = 0.885$
1. Calculate the infinite multiplication factor $k_\infty$.
2. If non-leakage probabilities are $P_{NL,f} = 0.940$ and $P_{NL,\text{th}} = 0.970$, determine the effective multiplication factor $k_{\text{eff}}$.
3. Determine whether the finite reactor is subcritical, critical, or supercritical, and compute core reactivity $\rho$ in pcm.""",
                    "solution": r"""### Step 1: Infinite Multiplication Factor $k_\infty$
Using the Four-Factor Formula:
$$k_\infty = \eta \cdot \epsilon \cdot p \cdot f$$
$$k_\infty = 1.340 \times 1.035 \times 0.890 \times 0.885$$
Multiply step-by-step:
$$\eta \cdot \epsilon = 1.340 \times 1.035 = 1.38690$$
$$1.38690 \times 0.890 = 1.23434$$
$$k_\infty = 1.23434 \times 0.885 \approx 1.0924$$

### Step 2: Effective Multiplication Factor $k_{\text{eff}}$
Using the Six-Factor Formula:
$$k_{\text{eff}} = k_\infty \cdot P_{NL,f} \cdot P_{NL,\text{th}}$$
$$k_{\text{eff}} = 1.0924 \times 0.940 \times 0.970 = 1.0924 \times 0.9118 \approx 0.99605$$

### Step 3: Criticality Evaluation and Reactivity
Because $k_{\text{eff}} = 0.99605 < 1.0000$, the finite reactor is **subcritical**.
Reactivity $\rho$:
$$\rho = \frac{k_{\text{eff}} - 1}{k_{\text{eff}}} = \frac{0.99605 - 1.0000}{0.99605} = \frac{-0.00395}{0.99605} \approx -0.003966$$
In percent:
$$\rho = -0.397\% \, \Delta k/k$$
In parts per hundred thousand ($\text{pcm} = 10^{-5}$):
$$\rho = -0.003966 \times 10^5 \approx -397\text{ pcm}$$
The reactor has a subcritical shutdown margin of **$397\text{ pcm}$**.""",
                    "hints": ["Four-factor formula: k_inf = eta * epsilon * p * f.", "Six-factor formula multiplies by both non-leakage probabilities."]
                },
                {
                    "id": "prob-5-2",
                    "problemNumber": "5.2",
                    "title": "Bohr-Wheeler Fissility Parameter and Critical Limit Comparison",
                    "difficulty": "Easy",
                    "statement": r"""Using the SEMF surface coefficient $a_s = 17.80\text{ MeV}$ and Coulomb coefficient $a_c = 0.711\text{ MeV}$:
1. Calculate the critical fissility ratio $(Z^2/A)_{\text{crit}}$.
2. Compute the fissility parameter $x$ for uranium-235 ($^{235}_{92}\text{U}$) and californium-252 ($^{252}_{98}\text{Cf}$).
3. Explain why $^{252}\text{Cf}$ has a high spontaneous fission branch ($3.09\%$) compared to $^{235}\text{U}$ ($7 \times 10^{-9}\%$).""",
                    "solution": r"""### Step 1: Critical Fissility Parameter
The liquid drop stability threshold against spontaneous deformation is:
$$\left(\frac{Z^2}{A}\right)_{\text{crit}} = \frac{2 a_s}{a_c} = \frac{2(17.80\text{ MeV})}{0.711\text{ MeV}} \approx 50.07$$

### Step 2: Compute Fissility Parameter $x$
1. For Uranium-235 ($Z = 92, A = 235$):
$$\frac{Z^2}{A} = \frac{92^2}{235} = \frac{8464}{235} \approx 36.017$$
$$x(^{235}\text{U}) = \frac{36.017}{50.07} \approx 0.719$$

2. For Californium-252 ($Z = 98, A = 252$):
$$\frac{Z^2}{A} = \frac{98^2}{252} = \frac{9604}{252} \approx 38.111$$
$$x(^{252}\text{Cf}) = \frac{38.111}{50.07} \approx 0.761$$

### Step 3: Physical Explanation
The fission barrier height $E_f$ decreases with fissility parameter $x$:
$$E_f \approx 0.83(1 - x)^3 E_S^0$$
For $^{235}\text{U}$, $x \approx 0.72 \implies E_f \approx 5.7\text{ MeV}$. The quantum tunneling probability is extremely small, giving a spontaneous fission half-life of $10^{19}\text{ years}$.
For $^{252}\text{Cf}$, $x \approx 0.76 \implies E_f \approx 3.7\text{ MeV}$. The barrier is $2\text{ MeV}$ lower and narrower, increasing quantum tunneling probability by 11 orders of magnitude! Californium-252 undergoes spontaneous fission with $T_{1/2,\text{SF}} = 85.5\text{ years}$, emitting $3.77$ neutrons per fission.""",
                    "hints": ["Critical ratio (Z^2/A)_crit = 2 * a_s / a_c.", "Fissility parameter is x = (Z^2/A) / (Z^2/A)_crit."]
                },
                {
                    "id": "prob-5-3",
                    "problemNumber": "5.3",
                    "title": "Nuclear Reactor Uranium-235 Burnup and Thermal Power Output",
                    "difficulty": "Intermediate",
                    "statement": r"""A commercial nuclear power plant operates at a steady electrical output of $P_e = 1,000\text{ MWe}$ with a net thermodynamic thermal efficiency $\eta_{\text{th}} = 33.3\%$.
Each fission of $^{235}\text{U}$ releases an average recoverable thermal energy $E_{\text{fiss}} = 200\text{ MeV}$.
1. Calculate the core thermal power $P_{\text{th}}$ in megawatts (MWth).
2. Determine the required number of fission events per second.
3. Calculate the mass of $^{235}\text{U}$ consumed (fissioned) per day in kilograms, and over a full operating year ($365\text{ days}$).""",
                    "solution": r"""### Step 1: Core Thermal Power
$$P_{\text{th}} = \frac{P_e}{\eta_{\text{th}}} = \frac{1000\text{ MWe}}{0.33333} \approx 3,000\text{ MWth} = 3.00 \times 10^9\text{ J/s}$$

### Step 2: Fissions per Second
Energy released per fission:
$$E_{\text{fiss}} = 200\text{ MeV} \times 1.60218 \times 10^{-13}\text{ J/MeV} = 3.20436 \times 10^{-11}\text{ J}$$
Fission rate $\dot{N}_f$:
$$\dot{N}_f = \frac{P_{\text{th}}}{E_{\text{fiss}}} = \frac{3.00 \times 10^9\text{ J/s}}{3.20436 \times 10^{-11}\text{ J/fission}} \approx 9.362 \times 10^{19}\text{ fissions/second}$$

### Step 3: Fissioned Mass per Day and Year
Number of fissions per day ($86,400\text{ s}$):
$$N_{\text{day}} = (9.362 \times 10^{19}\text{ s}^{-1}) \times 86400\text{ s} \approx 8.089 \times 10^{24}\text{ fissions/day}$$
Moles of $^{235}\text{U}$:
$$n = \frac{8.089 \times 10^{24}}{6.02214 \times 10^{23}\text{ mol}^{-1}} \approx 13.432\text{ moles/day}$$
Mass of $^{235}\text{U}$ fissioned per day:
$$m_{\text{day}} = 13.432\text{ mol} \times 235.04\text{ g/mol} \approx 3,157\text{ g/day} \approx 3.16\text{ kg/day}$$

Annual burnup:
$$m_{\text{year}} = 3.157\text{ kg/day} \times 365\text{ days} \approx 1,152\text{ kg/year} \approx 1.15\text{ metric tons/year}$$
A $1,000\text{ MWe}$ coal power plant burns over $3,000,000\text{ metric tons}$ of coal per year to produce the same energy as just **$1.15\text{ tons}$** of fissioned uranium!""",
                    "hints": ["Thermal power P_th = Electrical power / Efficiency.", "Energy per fission: 200 MeV = 3.204e-11 Joules."]
                },
                {
                    "id": "prob-5-4",
                    "problemNumber": "5.4",
                    "title": "Delayed Neutron Inhour Equation and Reactor Period",
                    "difficulty": "Advanced",
                    "statement": r"""A critical thermal reactor operating at $k = 1.0000$ experiences a small step reactivity insertion $\rho = +0.0010$ ($100\text{ pcm}$).
The delayed neutron fraction is $\beta = 0.0065$ and the average precursor decay constant is $\bar{\lambda} = 0.080\text{ s}^{-1}$ ($\bar{\tau} = 12.5\text{ s}$).
The prompt neutron generation time is $\Lambda = 1.0 \times 10^{-4}\text{ s}$.
1. Formulate the simplified one-delayed-group inhour equation for asymptotic reactor period $T$.
2. Calculate the reactor period $T$ in seconds.
3. Determine the reactor power multiplication factor after 60 seconds.""",
                    "solution": r"""### Step 1: One-Group Inhour Equation
The inhour equation relates reactivity $\rho$ to the asymptotic reactor period $T$ (where $P(t) = P_0 e^{t/T}$):
$$\rho = \frac{\Lambda}{T + \Lambda} + \sum_{i=1}^6 \frac{\beta_i}{1 + \lambda_i T}$$
In the single-delayed-group approximation for small reactivity ($\rho \ll \beta$ and $T \gg \Lambda$):
$$\rho \approx \frac{\Lambda}{T} + \frac{\beta}{1 + \bar{\lambda} T}$$
Because $\bar{\lambda} T$ is typically $\gg 1$:
$$\rho \approx \frac{\beta}{\bar{\lambda} T} \implies T \approx \frac{\beta - \rho}{\bar{\lambda} \rho} \approx \frac{\beta}{\bar{\lambda} \rho}$$
More precisely, solving $\rho (1 + \bar{\lambda} T) \approx \beta$:
$$\rho + \rho \bar{\lambda} T = \beta \implies T = \frac{\beta - \rho}{\rho \bar{\lambda}}$$

### Step 2: Calculate Reactor Period $T$
Substitute values ($\rho = 0.0010$, $\beta = 0.0065$, $\bar{\lambda} = 0.080\text{ s}^{-1}$):
$$\beta - \rho = 0.0065 - 0.0010 = 0.0055$$
$$\rho \bar{\lambda} = 0.0010 \times 0.080\text{ s}^{-1} = 8.0 \times 10^{-5}\text{ s}^{-1}$$
$$T = \frac{0.0055}{8.0 \times 10^{-5}\text{ s}^{-1}} = 68.75\text{ seconds}$$
The reactor power rises with an asymptotic period of **$T \approx 68.8\text{ seconds}$**.

### Step 3: Power Multiplication After 60 Seconds
$$\frac{P(60)}{P_0} = e^{t / T} = \exp\left(\frac{60\text{ s}}{68.75\text{ s}}\right) = e^{0.8727} \approx 2.39$$
Reactor power increases by a manageable factor of **$2.39$** over one minute, allowing operator and automated rod adjustments.""",
                    "hints": ["For rho << beta, period is given by T = (beta - rho) / (rho * lambda_bar).", "The reactor power evolves as P(t) = P_0 * exp(t / T)."]
                },
                {
                    "id": "prob-5-5",
                    "problemNumber": "5.5",
                    "title": "Fission Product Poisoning Kinetics: Iodine-135 and Xenon-135 Pit",
                    "difficulty": "Advanced",
                    "statement": r"""Xenon-135 is the strongest thermal neutron poison known ($\sigma_a = 2.65 \times 10^6\text{ barns}$).
In a reactor operating at thermal neutron flux $\Phi = 1.0 \times 10^{14}\text{ n/cm}^2\cdot\text{s}$:
- Fission yield of $^{135}\text{I}$: $\gamma_I = 0.0639$ ($T_{1/2,I} = 6.57\text{ h} \implies \lambda_I = 2.93 \times 10^{-5}\text{ s}^{-1}$)
- Direct fission yield of $^{135}\text{Xe}$: $\gamma_X = 0.0023$ ($T_{1/2,X} = 9.14\text{ h} \implies \lambda_X = 2.11 \times 10^{-5}\text{ s}^{-1}$)
1. Formulate the steady-state concentrations of $^{135}\text{I}$ and $^{135}\text{Xe}$ in terms of macroscopic fission cross-section $\Sigma_f$.
2. Explain the "xenon pit" (xenon poisoning peak) that occurs several hours after a sudden reactor shutdown.""",
                    "solution": r"""### Step 1: Steady-State Concentrations
1. **Iodine-135 Balance**:
At steady state, production by fission equals radioactive decay:
$$\gamma_I \Sigma_f \Phi = \lambda_I N_I \implies N_I^0 = \frac{\gamma_I \Sigma_f \Phi}{\lambda_I}$$

2. **Xenon-135 Balance**:
Production occurs via direct fission ($\gamma_X \Sigma_f \Phi$) and decay of $^{135}\text{I}$ ($\lambda_I N_I$).
Disappearance occurs via radioactive decay ($\lambda_X N_X$) and neutron burnup absorption ($\sigma_a^X \Phi N_X$):
$$\gamma_X \Sigma_f \Phi + \lambda_I N_I = \lambda_X N_X + \sigma_a^X \Phi N_X$$
Substituting $\lambda_I N_I = \gamma_I \Sigma_f \Phi$:
$$(\gamma_X + \gamma_I) \Sigma_f \Phi = (\lambda_X + \sigma_a^X \Phi) N_X$$
$$N_X^0 = \frac{(\gamma_I + \gamma_X) \Sigma_f \Phi}{\lambda_X + \sigma_a^X \Phi}$$

### Step 2: The Xenon Pit (Shutdown Transient)
Upon reactor shutdown, neutron flux drops to zero ($\Phi \to 0$):
1. **Loss of Burnup**: The primary destruction channel for xenon—neutron burnup ($\sigma_a^X \Phi N_X$)—instantly vanishes.
2. **Continued Production**: The massive reservoir of accumulated iodine-135 ($N_I^0 \gg N_X^0$) continues to decay into $^{135}\text{Xe}$ with half-life $6.57\text{ hours}$.
3. **Transient Peak**: Xenon-135 concentration builds up rapidly to a maximum at:
$$t_{\max} = \frac{1}{\lambda_X - \lambda_I} \ln\left[ \frac{\lambda_X}{\lambda_I} \left(1 - \frac{\lambda_X - \lambda_I}{\lambda_X} \frac{N_X^0}{N_I^0}\right) \right] \approx 10 - 11\text{ hours}$$
At $t \approx 11\text{ hours}$, xenon negative reactivity reaches a deep maximum ("xenon pit"). If control margins are inadequate, the reactor cannot be restarted until the xenon decays away ($\sim 30 - 40\text{ hours}$ later). Attempting an improper restart during a xenon transient contributed to the 1986 Chernobyl disaster.""",
                    "hints": ["At steady state, Iodine-135 production equals decay.", "In high flux, neutron burnup (sigma_a * Phi) dominates over radioactive decay for Xenon-135."]
                },
                {
                    "id": "prob-5-6",
                    "problemNumber": "5.6",
                    "title": "Breeding Ratio in Liquid Metal Fast Breeder Reactor",
                    "difficulty": "Intermediate",
                    "statement": r"""A sodium-cooled Fast Breeder Reactor operates with mixed oxide fuel ($^{239}\text{Pu}\text{O}_2 / ^{238}\text{U}\text{O}_2$).
In the fast neutron spectrum:
- Average neutrons per fission of $^{239}\text{Pu}$: $\nu = 2.92$
- Ratio of capture to fission cross-sections for $^{239}\text{Pu}$: $\alpha_c = \sigma_c / \sigma_f = 0.15$
- Fractional parasitic absorption in structure/sodium: $L_p = 0.18$
- Core leakage fraction: $L = 0.08$
1. Calculate the reproduction factor $\eta = \nu / (1 + \alpha_c)$ for $^{239}\text{Pu}$ in this spectrum.
2. Formulate and compute the breeding ratio $BR$ (excess fissile nuclei produced per fissile nucleus destroyed).
3. If $BR = 1.25$, calculate the fuel doubling time $T_D$ in years for a specific inventory of $3.0\text{ kg/MWe}$ and capacity factor $85\%$.""",
                    "solution": r"""### Step 1: Reproduction Factor $\eta$
Thermal neutrons yield $\eta \approx 2.11$ for Pu-239; in a fast spectrum, $\nu$ rises and capture $\alpha_c$ drops:
$$\eta = \frac{\nu}{1 + \alpha_c} = \frac{2.92}{1 + 0.15} = \frac{2.92}{1.15} \approx 2.539$$

### Step 2: Breeding Ratio Formulation
Of the $\eta$ neutrons produced per fissile $^{239}\text{Pu}$ destroyed:
- Exactly $1.00$ neutron must be absorbed in $^{239}\text{Pu}$ to sustain the chain reaction.
- $L_p$ neutrons are lost to parasitic capture.
- $L$ neutrons leak out of the blanket.
The remaining neutrons are captured by fertile $^{238}\text{U}$ to breed $^{239}\text{Pu}$:
$$BR = \eta - 1 - L_p - L$$
$$BR = 2.539 - 1.000 - 0.180 - 0.080 = 1.279$$
Because $BR = 1.28 > 1.00$, the reactor breeds $28\%$ more fuel than it consumes!

### Step 3: Doubling Time $T_D$
For $BR = 1.25$, the net breeding gain is $G = BR - 1 = 0.25$.
The fuel doubling time (simple compound formulation) is:
$$T_D = \frac{M_{\text{inv}}}{G \cdot \dot{M}_{\text{fiss}} \cdot CF}$$
At $1\text{ MWe}$ ($3\text{ MWth}$), annual fission burnup is $\approx 1.15\text{ kg/yr}$.
Annual fissile surplus:
$$\Delta M = 0.25 \times 1.15\text{ kg/yr} \times 0.85 \approx 0.244\text{ kg/yr}$$
Doubling time for $3.0\text{ kg}$ inventory:
$$T_D = \frac{3.0\text{ kg}}{0.244\text{ kg/yr}} \approx 12.3\text{ years}$$
The reactor doubles its initial fuel load in **$\approx 12\text{ years}$**.""",
                    "hints": ["Reproduction factor eta = nu / (1 + alpha_c).", "Breeding ratio BR = eta - 1 - losses."]
                },
                {
                    "id": "prob-5-7",
                    "problemNumber": "5.7",
                    "title": "CANDU Natural Uranium Heavy Water Moderation Optimization",
                    "difficulty": "Easy",
                    "statement": r"""In a CANDU reactor utilizing natural uranium fuel ($0.720\% \, ^{235}\text{U}$, $99.280\% \, ^{238}\text{U}$):
- Thermal capture cross-section of $^{235}\text{U}$: $\sigma_a^{235} = 680\text{ b}$ ($\sigma_f^{235} = 585\text{ b}$)
- Thermal capture cross-section of $^{238}\text{U}$: $\sigma_a^{238} = 2.70\text{ b}$
- Average neutrons per thermal fission of $^{235}\text{U}$: $\nu = 2.42$
1. Calculate the reproduction factor $\eta$ for natural uranium.
2. Explain why a light water moderated reactor cannot achieve criticality with natural uranium, whereas a heavy water moderated reactor can.""",
                    "solution": r"""### Step 1: Reproduction Factor $\eta$
The effective absorption cross-section per atom of natural uranium is:
$$\bar{\sigma}_a = 0.00720(680\text{ b}) + 0.99280(2.70\text{ b}) = 4.896 + 2.681 = 7.577\text{ barns}$$
The effective fission cross-section is:
$$\bar{\sigma}_f = 0.00720(585\text{ b}) = 4.212\text{ barns}$$
Reproduction factor:
$$\eta = \nu \frac{\bar{\sigma}_f}{\bar{\sigma}_a} = 2.42 \times \frac{4.212}{7.577} = 2.42 \times 0.5559 \approx 1.345$$

### Step 2: Physical Explanation of Moderator Choice
With $\eta \approx 1.345$, the product $\epsilon \cdot p \cdot f$ in the Four-Factor Formula must satisfy:
$$\epsilon \cdot p \cdot f \ge \frac{1}{\eta} = \frac{1}{1.345} \approx 0.743$$
- **In Light Water ($\text{H}_2\text{O}$)**:
Hydrogen has a significant thermal neutron capture cross-section ($\sigma_a(H) = 0.332\text{ barns}$). The thermal utilization factor $f$ drops severely ($f \sim 0.70$), driving $k_\infty = \eta \epsilon p f \approx 1.345 \times 1.03 \times 0.85 \times 0.70 \approx 0.825 < 1.000$. Light water absorbs too many neutrons to achieve criticality with natural uranium.
- **In Heavy Water ($\text{D}_2\text{O}$)**:
Deuterium has a negligible capture cross-section ($\sigma_a(D) = 0.0005\text{ barns}$—nearly $700\times$ lower than hydrogen). Thermal utilization remains high ($f \approx 0.94$), and with optimal lattice pitch, $p \approx 0.90$, yielding:
$$k_\infty \approx 1.345 \times 1.03 \times 0.90 \times 0.94 \approx 1.17 > 1.00$$
Heavy water easily sustains criticality with unenriched natural uranium!""",
                    "hints": ["Calculate the atom-weighted absorption and fission cross sections for natural uranium.", "Compare the capture cross section of H (0.33 b) versus D (0.0005 b)."]
                }
            ]
        },

        # =====================================================================
        # UNIT 6
        # =====================================================================
        {
            "id": "unit-6-radiation-interaction-with-matter",
            "unitNumber": 6,
            "title": "Unit 6: Radiation Interaction with Matter & Energy Loss Mechanisms",
            "leadSummary": "Comprehensive physical and analytical formulation of ionizing radiation interactions: heavy charged particle slowing down via the Bethe-Bloch stopping power equation, Bragg ionization peak dynamics, fast electron and positron collisional versus radiative Bremsstrahlung losses, the continuous beta spectrum and neutrino hypothesis, the Photoelectric Effect, Compton Scattering kinematics via the Klein-Nishina cross-section, and Pair Production attenuation mechanics.",
            "simulations": ["sim_nuc_bragg_peak_stopping_power", "sim_nuc_gamma_interaction_modes"],
            "sections": [
                {
                    "id": "sec-6-1",
                    "secNumber": "6.1",
                    "title": "Heavy Charged Particle Interactions: Ionization, Excitation & the Bethe-Bloch Equation",
                    "content": r"""Heavy charged particles—such as alpha particles ($^{4}\text{He}^{2+}$), protons ($p$), deuterons ($d$), and fission fragments—interact with matter almost entirely through **inelastic Coulomb collisions with atomic electrons** of the absorbing medium.

Because the mass of a heavy charged particle is thousands of times greater than the electron mass ($m_\alpha \approx 7300 m_e$), the projectile transfers only a tiny fraction of its kinetic energy in any single collision:
$$\Delta E_{\max} \approx \frac{4 m_e}{M} E \approx \frac{1}{1836} E \quad \text{for protons}$$
Consequently, heavy charged particles travel in essentially **straight-line trajectories**, losing energy continuously through hundreds of thousands of microscopic electrostatic interactions that ionize and excite absorber atoms.

### The Bethe-Bloch Stopping Power Equation
The linear stopping power $-dE/dx$ (energy loss per unit path length, $\text{MeV/cm}$) of a heavy charged particle with charge $z e$ and velocity $v = \beta c$ traversing a medium with atomic number $Z$ and number density $N$ ($\text{atoms/cm}^3$) is given by the relativistic **Bethe-Bloch formula**:
$$-\frac{dE}{dx} = \frac{4\pi z^2 e^4}{m_e v^2} N Z \left[ \ln\left( \frac{2 m_e v^2 \gamma^2}{I} \right) - \beta^2 - \frac{C}{Z} - \frac{\delta}{2} \right]$$
where in SI units:
$$-\frac{dE}{dx} = \frac{4\pi}{m_e c^2} \left(\frac{e^2}{4\pi\varepsilon_0}\right)^2 \frac{z^2}{\beta^2} N Z \left[ \ln\left( \frac{2 m_e c^2 \beta^2 \gamma^2}{I} \right) - \beta^2 - \frac{C}{Z} - \frac{\delta}{2} \right]$$

```
   Stopping Power -dE/dx
    ▲
    │ \                                                 Relativistic Rise
    │  \  1/v² Low-Energy Region                        (Density Effect δ)
    │   \                                                     /
    │    \                                     Minimum       /
    │     \                                    Ionizing     /
    │      \__________________________________(MIP: βγ ≈ 3-4)
    └────────────────────────────────────────────────────────► Particle Velocity βγ
```

### Physical Analysis of the Bethe-Bloch Terms
1. **$1/v^2$ (or $1/\beta^2$) Dependence**:
At non-relativistic velocities ($T \ll M c^2$), the stopping power is inversely proportional to the square of the projectile velocity. A slower particle spends more time in the electrostatic vicinity of each absorber electron, exerting a larger impulse and transferring more energy.
2. **$z^2$ Dependence**:
Stopping power scales with the square of the projectile charge. An alpha particle ($z = 2$) experiences **4 times** the stopping power of a proton ($z = 1$) moving at the identical velocity.
3. **Electron Density ($n_e = N Z = \rho N_A Z / A$)**:
Stopping power is directly proportional to the electron density of the absorbing medium.
4. **Mean Excitation Potential ($I$)**:
The average orbital ionization energy of the target atoms, empirically parameterized by Felix Bloch:
$$I \approx \begin{cases} 19.0\text{ eV} & \text{for } H_2 \\ 11.5 Z\text{ eV} & \text{for } Z \le 13 \\ 9.1 Z \left(1 + 1.19 Z^{-2/3}\right)\text{ eV} \approx 10 Z\text{ eV} & \text{for } Z > 13 \end{cases}$$
5. **Corrections**:
- **Shell Correction ($C/Z$)**: Accounts for orbital electron velocity when projectile speed is comparable to inner atomic shell electron speeds.
- **Density Effect ($\delta/2$, Fermi)**: Relativistic dielectric polarization of the medium shields distant electrons, truncating the relativistic logarithmic rise in condensed media.""",
                    "simulations": ["sim_nuc_bragg_peak_stopping_power"]
                },
                {
                    "id": "sec-6-2",
                    "secNumber": "6.2",
                    "title": "The Bragg Ionization Peak & Range-Energy Systematics in Absorbing Media",
                    "content": r"""As a heavy charged particle penetrates matter, its kinetic energy steadily decreases. Because the Bethe-Bloch stopping power scales inversely with velocity ($-dE/dx \propto 1/v^2$), the rate of energy loss **accelerates dramatically toward the very end of its track**.

### The Bragg Curve
Plotting the specific ionization (ion pairs generated per millimeter of path length) or stopping power $-dE/dx$ as a function of penetration depth produces the **Bragg Curve**:

```
 Specific Ionization (Ion Pairs / mm)
  ▲
  │                                     BRAGG PEAK
  │                                      /\
  │                                     /  \
  │                                    /    \
  │       Plateau Region              /      \
  │  ────────────────────────────────/        \  Tail (Straggling)
  │                                            \_____
  └─────────────────────────────────────────────┴────► Penetration Depth x
  0                                             R (Mean Range)
```

1. **Plateau Region**: Over the initial portion of the track, the high-energy particle travels at high velocity, depositing a relatively low, uniform dose.
2. **Bragg Peak**: As the particle slows into the keV energy regime, $-dE/dx$ surges to a sharp maximum, depositing the vast majority of its total kinetic energy within the final millimeters or micrometers of travel.
3. **Sharp Drop-off**: Immediately past the peak, the particle captures orbital electrons (neutralizing its charge from $z \to 0$), and its stopping power drops to zero at the **mean range** $R$.

### Hadrontherapy Application in Oncology
The Bragg peak is the physical foundation of **proton and carbon-ion radiation therapy**:
Unlike conventional megavoltage X-rays (which deposit their maximum dose near the skin surface and irradiate healthy tissue all the way through the patient), proton beams can be tuned in energy so that the sharp Bragg peak lands directly within deep-seated tumors (e.g., ocular or pediatric brain tumors), depositing zero exit dose in healthy tissue behind the tumor!

### Range-Energy Empirical Scaling
The mean range $R$ of a heavy charged particle is the integral of reciprocal stopping power:
$$R(T_0) = \int_0^{T_0} \left( -\frac{dE}{dx} \right)^{-1} dE$$
For alpha particles in dry air at STP ($15^\circ\text{C}, 1\text{ atm}$), the empirical **Geiger Rule** provides an accurate estimate for $4.0\text{ MeV} \le E_\alpha \le 8.5\text{ MeV}$:
$$R_{\text{air}}\text{ (cm)} = 0.318 \cdot E_\alpha^{3/2}\text{ (MeV)}$$

For any other absorbing medium of density $\rho$ and effective atomic mass $A$, the range can be scaled via the **Bragg-Kleeman Rule**:
$$\frac{R_1}{R_2} = \frac{\rho_2}{\rho_1} \sqrt{\frac{A_1}{A_2}}$$
Using air as reference ($\rho_{\text{air}} \approx 1.225 \times 10^{-3}\text{ g/cm}^3, A_{\text{air}} \approx 14.6$):
$$R_{\text{medium}}\text{ (cm)} \approx 3.2 \times 10^{-4} \frac{\sqrt{A}}{\rho\text{ (g/cm}^3)} R_{\text{air}}\text{ (cm)}$$
For biological soft tissue ($\rho \approx 1.0\text{ g/cm}^3, A \approx 11$):
$$R_{\text{tissue}} \approx \frac{R_{\text{air}}}{1000}$$
A $5.5\text{ MeV}$ alpha particle with a range of $4.0\text{ cm}$ in air travels only $\approx 40\,\mu\text{m}$ in soft tissue—less than the thickness of the dead cellular stratum corneum of human skin.""",
                    "simulations": ["sim_nuc_bragg_peak_stopping_power"]
                },
                {
                    "id": "sec-6-3",
                    "secNumber": "6.3",
                    "title": "Fast Electron & Positron Energy Loss: Collisional Ionization Versus Bremsstrahlung Radiation",
                    "content": r"""Unlike heavy ions, electrons ($\beta^-$) and positrons ($\beta^+$) have extremely small mass ($m_e$). When fast electrons traverse matter, they undergo two distinct, competing energy loss mechanisms:
$$\left( -\frac{dE}{dx} \right)_{\text{total}} = \left( -\frac{dE}{dx} \right)_{\text{coll}} + \left( -\frac{dE}{dx} \right)_{\text{rad}}$$

### 1. Collisional (Ionization) Stopping Power
Electrons lose energy through inelastic Coulomb collisions with atomic electrons, described by the relativistic Bethe-Bloch formula modified for identical particles (Møller scattering for electrons, Bhabha scattering for positrons):
$$\left( -\frac{dE}{dx} \right)_{\text{coll}} \propto \frac{Z}{v^2} \ln(\dots)$$

### 2. Radiative Stopping Power (Bremsstrahlung)
Because electrons have such tiny mass, when they pass close to a heavy nucleus with charge $+Ze$, the intense Coulomb field exerts massive centripetal acceleration $\vec{a} = \vec{F}/m_e \propto Ze / m_e$.
According to classical Larmor electrodynamics, an accelerating charge radiates electromagnetic power proportional to the square of its acceleration:
$$P \propto q^2 a^2 \propto \frac{e^2 (Z e)^2}{m_e^2} \propto \frac{Z^2}{m_e^2}$$
Notice that Bremsstrahlung radiation is inversely proportional to the **square of particle mass** ($m^2$):
$$\frac{P_{\text{rad}}(\text{electron})}{P_{\text{rad}}(\text{proton})} = \left(\frac{m_p}{m_e}\right)^2 = (1836)^2 \approx 3.37 \times 10^6$$
Bremsstrahlung is completely negligible for protons and alpha particles, but represents a dominant energy loss mechanism for fast electrons!

The radiative stopping power scales linearly with electron energy $E$ and quadratically with absorber atomic number $Z$:
$$\left( -\frac{dE}{dx} \right)_{\text{rad}} \approx N Z^2 \frac{e^4}{\hbar c (m_e c^2)^2} E \ln\left(\frac{183}{Z^{1/3}}\right) \propto Z^2 E$$

```
   Stopping Power -dE/dx
    ▲
    │                     / Radiative Loss (Bremsstrahlung) ~ Z² E
    │                    /
    │                   /
    │   Collisional    /
    │   Loss ~ Z ln(E)/
    │   ─────────────/───────── (Critical Energy E_c)
    │               /
    │              /
    └─────────────┴──────────────────────► Electron Energy E
```

### The Critical Energy ($E_c$)
The ratio of radiative stopping power to collisional stopping power is given by the empirical rule:
$$\frac{(-dE/dx)_{\text{rad}}}{(-dE/dx)_{\text{coll}}} \approx \frac{E \cdot Z}{800\text{ MeV}}$$
where $E$ is in $\text{MeV}$.

The **Critical Energy** $E_c$ is defined as the electron energy at which radiative loss equals collisional loss:
$$\frac{(-dE/dx)_{\text{rad}}}{(-dE/dx)_{\text{coll}}} = 1 \implies E_c \approx \frac{800\text{ MeV}}{Z}$$
- In Lead ($Z = 82$): $E_c \approx \frac{800}{82} \approx 9.8\text{ MeV}$. Above $10\text{ MeV}$, electrons in lead lose energy primarily by emitting Bremsstrahlung X-rays!
- In Water/Tissue ($Z_{\text{eff}} \approx 7.4$): $E_c \approx \frac{800}{7.4} \approx 108\text{ MeV}$.

### Golden Rule of Radiation Shielding for Beta Emitters
To shield pure beta-emitting radioisotopes (such as $^{90}\text{Sr}/^{90}\text{Y}$ or $^{32}\text{P}$), **high-$Z$ materials like lead must never be used directly**!
Directly placing lead around a high-energy beta source converts fast electrons into penetrating Bremsstrahlung X-ray photons via $Z^2$ scaling.
Correct protocol dictates:
1. Primary shield: Low-$Z$ material (Lucite acrylic plastic, Plexiglas, or aluminum) to absorb beta particles with minimal Bremsstrahlung.
2. Secondary shield: Outer layer of lead to attenuate any residual low-energy X-rays.""",
                    "simulations": ["sim_nuc_bragg_peak_stopping_power"]
                },
                {
                    "id": "sec-6-4",
                    "secNumber": "6.4",
                    "title": "The Continuous Beta Spectrum, Fermi Theory & Pauli's Neutrino Hypothesis",
                    "content": r"""Unlike alpha particles (which are ejected with sharp, discrete monoenergetic kinetic energies), beta particles are emitted with a **continuous kinetic energy spectrum** extending from zero up to a precise maximum endpoint energy $E_{\max}$ ($Q_\beta$).

### The Crisis of Conservation Laws (1920s)
In two-body nuclear decay ($A \to B + \beta$), conservation of energy and momentum requires the ejected beta particle to carry away a unique discrete energy:
$$T_\beta = Q_\beta \left(\frac{M_B}{M_B + m_e}\right) \approx Q_\beta$$
The experimental continuous spectrum (Chadwick, 1914) meant that the average kinetic energy carried by the beta particle was barely $\sim 30 - 40\%$ of $Q_\beta$. The missing energy appeared to vanish, prompting Niels Bohr to suggest that conservation of energy might hold only statistically in quantum mechanics!

```
 Number of Beta Particles N(E)
  ▲
  │         Continuous Beta Spectrum
  │              ___
  │            /     \
  │           /       \
  │          /         \
  │         /           \
  │        /             \
  │_______/               \________
  └───────┴──────┴─────────────────┴► Kinetic Energy T_β
          0     E_avg             E_max (Q_β Endpoint)
```

### Wolfgang Pauli's Neutrino Hypothesis (1930)
In December 1930, Wolfgang Pauli proposed a "desperate remedy": the nucleus emits an elusive, electrically neutral, spin-$1/2$ fermion of negligible or zero rest mass alongside the beta electron:
$$n \longrightarrow p + e^- + \bar{\nu}_e \quad (\beta^- \text{ decay: electron antineutrino})$$
$$p \longrightarrow n + e^+ + \nu_e \quad (\beta^+ \text{ decay: electron neutrino})$$
Because three bodies share the decay energy $Q_\beta$, the electron and neutrino share the energy stochastically:
$$T_e + E_\nu = Q_\beta$$
- When $E_\nu \to 0$: $T_e = E_{\max} = Q_\beta$ (the spectrum endpoint).
- When $T_e \to 0$: The neutrino carries away the entire decay energy undetected.

### Enrico Fermi's Theory of Beta Decay (1934)
Enrico Fermi developed the quantum field theory of beta decay using time-dependent perturbation theory (Fermi's Golden Rule):
$$\lambda = \frac{2\pi}{\hbar} |M_{fi}|^2 \rho(E_f)$$
The transition probability per unit time for an electron to be emitted with momentum $p$ in interval $dp$ is governed by the two-body phase space volume of the electron and neutrino:
$$d\lambda(p) = \frac{G_F^2 |M_{fi}|^2}{2\pi^3 \hbar^7 c^3} F(Z, E) \, p^2 (Q - T_e)^2 dp$$
where:
- $G_F \approx 1.436 \times 10^{-62}\text{ J}\cdot\text{m}^3$ is the Fermi weak coupling constant.
- $F(Z, E)$ is the **Fermi function**, correcting for Coulomb attraction ($\beta^-$) or repulsion ($\beta^+$) between the outgoing electron and daughter nucleus.

### The Fermi-Kurie Plot
Linearizing Fermi's spectral distribution:
$$\sqrt{\frac{N(p)}{p^2 F(Z, E)}} \propto (Q - T_e)$$
Plotting $\sqrt{N(p) / [p^2 F(Z, E)]}$ versus electron kinetic energy $T_e$ yields a straight line whose horizontal axis intercept determines the exact decay endpoint energy $Q_\beta$ and neutrino mass limit ($m_\nu \approx 0$).""",
                    "simulations": ["sim_nuc_bragg_peak_stopping_power"]
                },
                {
                    "id": "sec-6-5",
                    "secNumber": "6.5",
                    "title": "The Photoelectric Effect: K-Shell Ionization, Absorption Edges & Auger Cascades",
                    "content": r"""Unlike charged particles (which lose energy continuously in small increments), gamma-ray photons ($h\nu$) are electrically uncharged and interact with matter through discrete, catastrophic interactions in which the photon is either completely absorbed or scattered out of the beam.
The three primary photon interaction mechanisms are the **Photoelectric Effect**, **Compton Scattering**, and **Pair Production**.

### The Photoelectric Absorption Mechanism
In the photoelectric effect, an incident gamma photon strikes a tightly bound inner-shell atomic electron (predominantly the $K$-shell, $>80\%$ of events). The photon disappears completely, and its entire energy $h\nu$ is transferred to the atomic electron, which is ejected into the continuum as a **photoelectron**:
$$T_e = h\nu - B_K$$
where $B_K$ is the binding energy of the $K$-shell electron.

Conservation of linear momentum requires that a completely free electron **cannot** absorb a photon and conserve both energy and momentum simultaneously; the interaction requires a bound electron where the residual target nucleus acts as a third body to absorb momentum recoil.

```
       Incident Photon hν
      ────────────────────►  ● K-Shell Electron
                             │
                             ▼ Ejection
                    Photoelectron: T_e = hν - B_K
```

### Energy and Atomic Number Dependence
The atomic photoelectric cross-section $\tau$ per atom depends strongly on photon energy $E_\gamma = h\nu$ and absorber atomic number $Z$:
$$\tau \propto \frac{Z^n}{(h\nu)^m} \approx \frac{Z^4 \text{ to } Z^5}{(h\nu)^{3.5}}$$
- **High-$Z$ absorbers**: Materials like lead ($Z = 82$, $Z^5 \approx 3.7 \times 10^9$) have astronomical photoelectric cross-sections compared to aluminum ($Z = 13$, $Z^5 \approx 3.7 \times 10^5$)—a factor of $10,000$ greater!
- **Dominance Regime**: The photoelectric effect dominates at low photon energies ($E_\gamma < 100\text{ keV}$ in tissue, $E_\gamma < 500\text{ keV}$ in lead).

### Absorption Edges ($K$-Edge, $L$-Edges)
As photon energy decreases, the cross-section climbs steeply as $1/E^{3.5}$. However, when photon energy drops just below the binding energy of an electron shell ($h\nu < B_K$), photons suddenly lack sufficient energy to ionize electrons in that shell. The cross-section drops discontinuously by a factor of 5 to 10:

```
 Photoelectric Cross Section τ
  ▲
  │              /│
  │             / │
  │            /  │  K-EDGE (hν = B_K)
  │           /   │
  │          /    │___
  │        L-Edges│   \
  │_______/│______│____\___________
  └───────┴───────┴────────────────► Photon Energy hν
```

For lead ($Z = 82$), the $K$-edge occurs at $B_K = 88.00\text{ keV}$. Photons with $88.1\text{ keV}$ are absorbed violently, while photons with $87.9\text{ keV}$ penetrate much more deeply.

### De-excitation: Characteristic X-Rays Versus Auger Electrons
Photoelectric ionization leaves an inner-shell vacancy. An outer-shell electron drops into the vacancy, releasing transition energy $\Delta E = B_K - B_L$. This energy is emitted as either:
1. **Characteristic X-ray photon** with energy $h\nu = B_K - B_L$.
2. **Auger Electron**: The energy is transferred non-radiatively to an outer-shell electron, which is ejected with kinetic energy $T_{\text{Auger}} = (B_K - B_L) - B_M$.
The fluorescent yield $\omega_K$ (probability of X-ray emission vs Auger) scales with atomic number: $\omega_K \approx \frac{Z^4}{Z^4 + 10^6}$. Low-$Z$ tissue predominantly emits Auger electrons (delivering localized nanometer damage), while high-$Z$ lead emits characteristic X-rays.""",
                    "simulations": ["sim_nuc_gamma_interaction_modes"]
                },
                {
                    "id": "sec-6-6",
                    "secNumber": "6.6",
                    "title": "Compton Scattering Dynamics: The Klein-Nishina Cross-Section & the Compton Edge",
                    "content": r"""At intermediate gamma-ray energies ($0.5\text{ MeV} \le E_\gamma \le 5\text{ MeV}$), the dominant interaction mechanism is **Compton scattering**: the elastic scattering of a photon by a loosely bound or "free" atomic electron ($h\nu \gg B_e$).

### Derivation of the Compton Scattering Formula
Consider an incident photon of energy $E = h\nu$ and momentum $p = h\nu/c$ striking a stationary electron of rest mass $m_e$ at rest ($E_0 = m_e c^2$).
The photon scatters at angle $\theta$ with energy $E' = h\nu'$, while the electron recoils at angle $\phi$ with kinetic energy $T_e$.

```
                      scattered photon hν'
                           ^
                          /  θ (Scattering Angle)
  Incident hν            /
 ──────────────► ● (e⁻ at rest)
                         \
                          \  φ
                           v
                      Recoil Electron T_e
```

1. **Conservation of Energy**:
$$h\nu + m_e c^2 = h\nu' + E_e = h\nu' + \sqrt{p_e^2 c^2 + m_e^2 c^4}$$
$$\sqrt{p_e^2 c^2 + m_e^2 c^4} = h\nu - h\nu' + m_e c^2$$
Squaring both sides:
$$p_e^2 c^2 + m_e^2 c^4 = (h\nu - h\nu')^2 + 2 m_e c^2 (h\nu - h\nu') + m_e^2 c^4$$
$$p_e^2 c^2 = (h\nu)^2 + (h\nu')^2 - 2 (h\nu)(h\nu') + 2 m_e c^2 (h\nu - h\nu')$$

2. **Conservation of Linear Momentum**:
$$\vec{p}_\gamma = \vec{p}'_\gamma + \vec{p}_e \implies \vec{p}_e = \vec{p}_\gamma - \vec{p}'_\gamma$$
Squaring:
$$p_e^2 = p_\gamma^2 + (p'_\gamma)^2 - 2 p_\gamma p'_\gamma \cos\theta = \left(\frac{h\nu}{c}\right)^2 + \left(\frac{h\nu'}{c}\right)^2 - 2 \left(\frac{h\nu}{c}\right)\left(\frac{h\nu'}{c}\right)\cos\theta$$
Multiplying by $c^2$:
$$p_e^2 c^2 = (h\nu)^2 + (h\nu')^2 - 2 (h\nu)(h\nu')\cos\theta$$

3. **Equating Momentum Expressions**:
$$(h\nu)^2 + (h\nu')^2 - 2(h\nu)(h\nu') + 2 m_e c^2 (h\nu - h\nu') = (h\nu)^2 + (h\nu')^2 - 2(h\nu)(h\nu')\cos\theta$$
Cancelling common terms:
$$2 m_e c^2 (h\nu - h\nu') = 2 (h\nu)(h\nu')(1 - \cos\theta)$$
Dividing both sides by $2 m_e c^2 (h\nu)(h\nu')$:
$$\frac{1}{h\nu'} - \frac{1}{h\nu} = \frac{1}{m_e c^2}(1 - \cos\theta)$$
Multiplying by $h c$:
$$\lambda' - \lambda = \frac{h}{m_e c}(1 - \cos\theta) = \lambda_C (1 - \cos\theta)$$
where $\lambda_C = \frac{h}{m_e c} \approx 2.4263 \times 10^{-12}\text{ m} = 0.02426\text{ \AA}$ is the **Compton wavelength** of the electron.

Expressing scattered photon energy $E'$:
$$E' = \frac{E}{1 + \frac{E}{m_e c^2}(1 - \cos\theta)}$$

### The Compton Edge Energy ($E_C$)
The recoil electron kinetic energy is:
$$T_e = E - E' = E \left[ 1 - \frac{1}{1 + \frac{E}{m_e c^2}(1 - \cos\theta)} \right] = E \left[ \frac{\frac{E}{m_e c^2}(1 - \cos\theta)}{1 + \frac{E}{m_e c^2}(1 - \cos\theta)} \right]$$

The maximum energy transfer to the electron occurs during a **head-on collision where the photon backscatters directly at $\theta = 180^\circ$** ($\cos 180^\circ = -1 \implies 1 - \cos\theta = 2$):
$$T_{e,\max} = E_C = E \left[ \frac{\frac{2E}{m_e c^2}}{1 + \frac{2E}{m_e c^2}} \right] = \frac{2 E^2}{m_e c^2 + 2E}$$
This sharp cutoff $E_C$ is the **Compton Edge** in gamma spectroscopy.
The minimum energy of the backscattered photon is:
$$E'_{\min} = \frac{E}{1 + \frac{2E}{m_e c^2}} = E - E_C$$
For high-energy gammas ($E \gg m_e c^2$):
$$E'_{\min} \to \frac{m_e c^2}{2} \approx 255.5\text{ keV}$$
Regardless of incident gamma energy, a backscattered photon can never have more than $\approx 256\text{ keV}$!

### The Klein-Nishina Differential Cross-Section
Quantum electrodynamics (Oskar Klein and Yoshio Nishina, 1928) gives the differential cross-section per electron:
$$\frac{d\sigma_C}{d\Omega} = \frac{r_e^2}{2} \left(\frac{E'}{E}\right)^2 \left[ \frac{E'}{E} + \frac{E}{E'} - \sin^2\theta \right]$$
where $r_e = \frac{e^2}{4\pi\varepsilon_0 m_e c^2} \approx 2.818\text{ fm}$ is the classical electron radius.
Because Compton scattering occurs with individual atomic electrons, the atomic cross-section scales strictly with atomic number:
$$\sigma_{\text{atomic}}^{\text{Compton}} = Z \cdot \sigma_e$$""",
                    "simulations": ["sim_nuc_gamma_interaction_modes"]
                },
                {
                    "id": "sec-6-7",
                    "secNumber": "6.7",
                    "title": "Electron-Positron Pair Production & Total Gamma Attenuation Metrology (HVL/TVL)",
                    "content": r"""At high photon energies, a third interaction mechanism appears: **electron-positron pair production**.

### Pair Production Kinematics & Energy Threshold
In the presence of the strong Coulomb electric field of an atomic nucleus (to absorb recoil momentum), a high-energy gamma photon can spontaneously materialize into an electron-positron pair:
$$\gamma + \text{Nucleus} \longrightarrow e^- + e^+ + \text{Nucleus}'$$
The threshold photon energy required for pair production in the nuclear field is exactly the sum of the rest mass energies of the two leptons:
$$E_{\text{th}} = 2 m_e c^2 = 2 (0.5109989\text{ MeV}) = 1.0220\text{ MeV}$$
For photon energies $h\nu < 1.022\text{ MeV}$, pair production is **strictly impossible**.

Any excess photon energy above $1.022\text{ MeV}$ is partitioned into the kinetic energies of the created electron and positron:
$$T_{e^-} + T_{e^+} = h\nu - 2 m_e c^2 = h\nu - 1.022\text{ MeV}$$

```
                e⁻ (Electron, T_e⁻)
               ▲
              /
  hν > 1.022 MeV
 ────────────► ● Nucleus (Recoil)
              \
               \
                ▼ e⁺ (Positron, T_e⁺) ──► Slows ──► Annihilation (Two 511 keV γ)
```

The atomic pair production cross-section $\kappa$ scales with the square of the nuclear charge:
$$\kappa \propto Z^2 \ln(h\nu)$$
Pair production dominates at high energies ($h\nu > 5\text{ MeV}$ in lead; $h\nu > 20\text{ MeV}$ in tissue).

### Positron Annihilation & Escape Peaks
Once the created positron slows to thermal energies, it annihilates with an atomic electron in the medium:
$$e^+ + e^- \longrightarrow 2 \gamma \quad (\text{each photon } E_\gamma = m_e c^2 = 511.0\text{ keV})$$
To conserve momentum, the two annihilation photons are emitted **collinearly back-to-back ($180^\circ$)**.
In gamma spectroscopy, this produces characteristic peaks:
1. **Full Energy Peak (Photopeak)**: Both $511\text{ keV}$ photons are absorbed ($E$).
2. **Single Escape Peak**: One $511\text{ keV}$ photon escapes the detector ($E - 511\text{ keV}$).
3. **Double Escape Peak**: Both annihilation photons escape ($E - 1022\text{ keV}$).

### Total Linear & Mass Attenuation Coefficients
The total probability of photon interaction per unit distance is the sum of all three independent mechanisms:
$$\mu = \tau (\text{Photoelectric}) + \sigma_C (\text{Compton}) + \kappa (\text{Pair Production})$$
where $\mu$ is the **linear attenuation coefficient** ($\text{cm}^{-1}$).

For a narrow, collimated monoenergetic gamma beam traversing thickness $x$:
$$I(x) = I_0 e^{-\mu x}$$
To remove dependence on physical density $\rho$, we use the **mass attenuation coefficient** $\mu / \rho$ ($\text{cm}^2/\text{g}$):
$$I(x) = I_0 \exp\left[ -\left(\frac{\mu}{\rho}\right) (\rho x) \right]$$
where $\rho x$ is the area mass density ($\text{g/cm}^2$).

### Half-Value Layer (HVL) and Tenth-Value Layer (TVL)
- **Half-Value Layer (HVL)**: The thickness of shielding required to attenuate beam intensity by $50\%$ ($I = I_0 / 2$):
$$\frac{1}{2} = e^{-\mu \cdot \text{HVL}} \implies \text{HVL} = \frac{\ln 2}{\mu} \approx \frac{0.69315}{\mu}$$
- **Tenth-Value Layer (TVL)**: The thickness required to attenuate beam intensity by $90\%$ ($I = I_0 / 10$):
$$\frac{1}{10} = e^{-\mu \cdot \text{TVL}} \implies \text{TVL} = \frac{\ln 10}{\mu} \approx \frac{2.3026}{\mu} \approx 3.322 \cdot \text{HVL}$$

| Absorber Material | Density $\rho$ ($\text{g/cm}^3$) | Linear Attenuation $\mu$ ($1\text{ MeV}$) | Half-Value Layer HVL ($1\text{ MeV}$) | Tenth-Value Layer TVL ($1\text{ MeV}$) |
| :--- | :--- | :--- | :--- | :--- |
| **Lead ($\text{Pb}$)** | $11.35$ | $0.771\text{ cm}^{-1}$ | **$0.90\text{ cm}$** ($9.0\text{ mm}$) | **$2.99\text{ cm}$** |
| **Steel / Iron ($\text{Fe}$)** | $7.87$ | $0.470\text{ cm}^{-1}$ | **$1.47\text{ cm}$** | **$4.90\text{ cm}$** |
| **Standard Concrete** | $2.35$ | $0.149\text{ cm}^{-1}$ | **$4.65\text{ cm}$** | **$15.45\text{ cm}$** |
| **Water / Soft Tissue** | $1.00$ | $0.0706\text{ cm}^{-1}$ | **$9.82\text{ cm}$** | **$32.61\text{ cm}$** |

Three half-value layers attenuate a beam to $(1/2)^3 = 12.5\%$; seven half-value layers attenuate to $<1\%$; ten half-value layers attenuate to $<0.1\%$ ($1/1024$).""",
                    "simulations": ["sim_nuc_gamma_interaction_modes"]
                }
            ],
            "problems": [
                {
                    "id": "prob-6-1",
                    "problemNumber": "6.1",
                    "title": "Compton Scattering Wavelength Shift and Compton Edge for Cs-137 Gamma",
                    "difficulty": "Easy",
                    "statement": r"""Cesium-137 emits a prominent monoenergetic gamma-ray photon with energy $E_\gamma = 661.66\text{ keV}$.
1. Calculate the initial wavelength $\lambda$ of the photon in picometers ($\text{pm}$).
2. Determine the scattered photon wavelength $\lambda'$ and energy $E'$ for a scattering angle $\theta = 60.0^\circ$.
3. Calculate the maximum kinetic energy transfer to the electron (the Compton Edge $E_C$) occurring at $\theta = 180.0^\circ$.""",
                    "solution": r"""### Step 1: Initial Photon Wavelength
$$E = 661.66\text{ keV} = 661,660 \times 1.60218 \times 10^{-19}\text{ J} = 1.0601 \times 10^{-13}\text{ J}$$
$$\lambda = \frac{h c}{E} = \frac{(6.62607 \times 10^{-34}\text{ J}\cdot\text{s})(2.99792 \times 10^8\text{ m/s})}{1.0601 \times 10^{-13}\text{ J}} \approx 1.8738 \times 10^{-12}\text{ m} = 1.8738\text{ pm}$$

### Step 2: Compton Scattering at $\theta = 60.0^\circ$
Compton wavelength shift:
$$\Delta \lambda = \lambda_C (1 - \cos 60^\circ) = 2.4263\text{ pm} \times (1 - 0.500) = 1.2132\text{ pm}$$
Scattered wavelength:
$$\lambda' = \lambda + \Delta \lambda = 1.8738 + 1.2132 = 3.0870\text{ pm}$$
Scattered photon energy $E'$:
$$E' = \frac{h c}{\lambda'} = \frac{1239.84\text{ keV}\cdot\text{pm}}{3.0870\text{ pm}} \approx 401.63\text{ keV}$$
Alternatively:
$$E' = \frac{E}{1 + \frac{E}{m_e c^2}(1 - \cos 60^\circ)} = \frac{661.66}{1 + \frac{661.66}{511.0}(0.5)} = \frac{661.66}{1 + 0.6474} = \frac{661.66}{1.6474} \approx 401.64\text{ keV}$$

### Step 3: Compton Edge ($E_C$ at $\theta = 180.0^\circ$)
At $\theta = 180^\circ$, $1 - \cos\theta = 2$:
$$E'_{\min} = \frac{E}{1 + \frac{2E}{m_e c^2}} = \frac{661.66}{1 + \frac{2(661.66)}{511.0}} = \frac{661.66}{1 + 2.5897} = \frac{661.66}{3.5897} \approx 184.32\text{ keV}$$
The Compton Edge is:
$$E_C = E - E'_{\min} = 661.66\text{ keV} - 184.32\text{ keV} = 477.34\text{ keV}$$
In a $^{137}\text{Cs}$ gamma spectrum, the Compton edge is located precisely at **$477.3\text{ keV}$**, and the backscatter peak is at **$184.3\text{ keV}$**.""",
                    "hints": ["Delta lambda = lambda_C * (1 - cos(theta)) with lambda_C = 2.426 pm.", "Compton edge is E_C = E - E'_min at 180 degrees backscatter."]
                },
                {
                    "id": "prob-6-2",
                    "problemNumber": "6.2",
                    "title": "Lead Shielding Thickness Calculation for Co-60 Radiotherapy Beam",
                    "difficulty": "Easy",
                    "statement": r"""A cobalt-60 ($^{60}\text{Co}$) industrial irradiator emits penetrating gamma photons with average energy $1.25\text{ MeV}$ ($1173\text{ keV}$ and $1332\text{ keV}$).
The linear attenuation coefficient of lead at this energy is $\mu = 0.660\text{ cm}^{-1}$.
1. Calculate the Half-Value Layer (HVL) and Tenth-Value Layer (TVL) of lead for $^{60}\text{Co}$ in centimeters.
2. Determine the thickness of lead shielding required to attenuate the radiation intensity by a factor of $10,000$ ($10^4$).""",
                    "solution": r"""### Step 1: HVL and TVL
$$\text{HVL} = \frac{\ln 2}{\mu} = \frac{0.693147}{0.660\text{ cm}^{-1}} \approx 1.0502\text{ cm} = 10.5\text{ mm}$$
$$\text{TVL} = \frac{\ln 10}{\mu} = \frac{2.302585}{0.660\text{ cm}^{-1}} \approx 3.4888\text{ cm} = 34.9\text{ mm}$$

### Step 2: Shielding Thickness for $10^4$ Attenuation
We require:
$$\frac{I(x)}{I_0} = \frac{1}{10,000} = 10^{-4} = e^{-\mu x}$$
Taking the natural logarithm:
$$-\mu x = \ln(10^{-4}) = -4 \ln(10) \implies x = \frac{4 \ln(10)}{\mu} = 4 \cdot \text{TVL}$$
$$x = 4 \times 3.4888\text{ cm} \approx 13.96\text{ cm}$$
A lead shield of thickness **$14.0\text{ cm}$** ($140\text{ mm}$) reduces the beam intensity ten-thousand-fold.""",
                    "hints": ["HVL = ln(2)/mu and TVL = ln(10)/mu.", "An attenuation factor of 10^4 corresponds exactly to 4 Tenth-Value Layers (4 * TVL)."]
                },
                {
                    "id": "prob-6-3",
                    "problemNumber": "6.3",
                    "title": "Alpha Particle Range in Air and Biological Soft Tissue",
                    "difficulty": "Easy",
                    "statement": r"""Americium-241 ($^{241}\text{Am}$) is used in ionization smoke detectors, emitting alpha particles with kinetic energy $E_\alpha = 5.486\text{ MeV}$.
1. Using Geiger's rule ($R_{\text{air}} = 0.318 \cdot E^{3/2}$), calculate the range of these alpha particles in air at STP in centimeters.
2. Using the Bragg-Kleeman scaling relationship with tissue density $\rho_{\text{tissue}} = 1.02\text{ g/cm}^3$ and effective atomic mass $A_{\text{tissue}} = 11.5$:
$$\frac{R_{\text{tissue}}}{R_{\text{air}}} = \frac{\rho_{\text{air}}}{\rho_{\text{tissue}}} \sqrt{\frac{A_{\text{tissue}}}{A_{\text{air}}}}$$
(given $\rho_{\text{air}} = 0.001225\text{ g/cm}^3$ and $A_{\text{air}} = 14.6$), compute the penetration depth in human soft tissue in micrometers ($\mu\text{m}$).""",
                    "solution": r"""### Step 1: Alpha Range in Air
Using Geiger's rule:
$$R_{\text{air}} = 0.318 \times (5.486)^{3/2} = 0.318 \times (\sqrt{5.486})^3 = 0.318 \times (2.3422)^3 = 0.318 \times 12.849 \approx 4.086\text{ cm}$$
The alpha particles travel **$4.09\text{ cm}$** in room air.

### Step 2: Alpha Range in Tissue
Using the Bragg-Kleeman scaling relation:
$$\frac{R_{\text{tissue}}}{R_{\text{air}}} = \frac{0.001225\text{ g/cm}^3}{1.02\text{ g/cm}^3} \times \sqrt{\frac{11.5}{14.6}} = (0.001201) \times \sqrt{0.7877} = 0.001201 \times 0.8875 \approx 1.066 \times 10^{-3}$$
Penetration depth in tissue:
$$R_{\text{tissue}} = 4.086\text{ cm} \times 1.066 \times 10^{-3} \approx 4.356 \times 10^{-3}\text{ cm} = 43.6\,\mu\text{m}$$
The alpha particles penetrate only **$43.6\text{ micrometers}$** into tissue—completely stopped by the $50\,\mu\text{m}$ dead epidermis layer.""",
                    "hints": ["Geiger rule: R = 0.318 * E^(1.5) for alpha in air.", "Convert cm to micrometers: 1 cm = 10,000 micrometers."]
                },
                {
                    "id": "prob-6-4",
                    "problemNumber": "6.4",
                    "title": "Bremsstrahlung Fraction and Critical Energy for P-32 Beta Shielding",
                    "difficulty": "Intermediate",
                    "statement": r"""Phosphorus-32 ($^{32}\text{P}$) is a pure beta emitter ($E_{\max} = 1.710\text{ MeV}$, average energy $\bar{E} = 0.695\text{ MeV}$).
The fraction of beta energy converted into Bremsstrahlung radiation is parameterized by:
$$f_{\text{rad}} \approx 3.5 \times 10^{-4} \cdot Z \cdot E_{\max} \text{ (MeV)}$$
1. Calculate the Bremsstrahlung conversion fraction $f_{\text{rad}}$ if $^{32}\text{P}$ is shielded with:
   (a) Lead ($Z = 82$)
   (b) Lucite acrylic plastic ($Z_{\text{eff}} = 5.85$)
2. Compute the critical energy $E_c$ in lead and Lucite.
3. Quantify why Lucite is the superior primary radiation shield for $^{32}\text{P}$.""",
                    "solution": r"""### Step 1: Bremsstrahlung Conversion Fraction
1. **In Lead ($Z = 82$)**:
$$f_{\text{rad}}(\text{Pb}) = 3.5 \times 10^{-4} \times 82 \times 1.710 = 0.04907 \approx 4.91\%$$
Nearly **$5\%$** of all beta energy is converted into penetrating Bremsstrahlung X-rays!

2. **In Lucite ($Z_{\text{eff}} = 5.85$)**:
$$f_{\text{rad}}(\text{Lucite}) = 3.5 \times 10^{-4} \times 5.85 \times 1.710 = 0.00350 \approx 0.35\%$$
Only **$0.35\%$** of the beta energy converts to Bremsstrahlung in Lucite.

### Step 2: Critical Energy $E_c$
$$E_c \approx \frac{800\text{ MeV}}{Z}$$
- For Lead: $E_c = \frac{800}{82} \approx 9.76\text{ MeV}$.
- For Lucite: $E_c = \frac{800}{5.85} \approx 136.8\text{ MeV}$.

### Step 3: Comparative Conclusion
Lucite produces **$14$ times less** secondary Bremsstrahlung radiation than lead ($4.91\% / 0.35\% = 14.0$). A $1.0\text{ cm}$ thick Lucite acrylic block will absorb $100\%$ of the beta electrons ($R_{\max} \approx 0.8\text{ cm}$) while generating virtually zero penetrating secondary X-rays.""",
                    "hints": ["Use the empirical formula f_rad = 3.5e-4 * Z * E_max.", "Critical energy is E_c = 800 / Z MeV."]
                },
                {
                    "id": "prob-6-5",
                    "problemNumber": "6.5",
                    "title": "Pair Production Threshold Kinematics in Nuclear vs Electron Field",
                    "difficulty": "Intermediate",
                    "statement": r"""1. Show that for pair production occurring in the Coulomb field of a heavy nucleus of mass $M \gg m_e$, the threshold photon energy is $E_{\text{th}} \approx 2 m_e c^2 = 1.022\text{ MeV}$.
2. If pair production occurs in the field of an atomic electron at rest ($M = m_e$, termed "triplet production" $\gamma + e^- \to e^- + e^- + e^+$), derive the relativistic invariant threshold energy $E_{\text{th}}^{\text{triplet}}$ and show it equals $4 m_e c^2 \approx 2.044\text{ MeV}$.""",
                    "solution": r"""### Step 1: Threshold in Nuclear Field
Using relativistic 4-momentum invariant $s = P_{\text{total}}^\mu P_{\mu,\text{total}}$:
Before collision (photon $P_\gamma = (E/c, \vec{p})$ with $E = p c$; stationary nucleus $P_N = (M c, 0)$):
$$s = (P_\gamma + P_N)^2 = P_\gamma^2 + P_N^2 + 2 P_\gamma \cdot P_N = 0 + M^2 c^2 + 2 \left(\frac{E}{c}\right)(M c) = M^2 c^2 + 2 M E$$
At threshold in the CM frame, all products ($M + 2 m_e$) are at rest relative to each other:
$$s = (M c + 2 m_e c)^2 = M^2 c^2 + 4 M m_e c^2 + 4 m_e^2 c^2$$
Equating:
$$M^2 c^2 + 2 M E_{\text{th}} = M^2 c^2 + 4 M m_e c^2 + 4 m_e^2 c^2$$
$$2 M E_{\text{th}} = 4 M m_e c^2 + 4 m_e^2 c^2 \implies E_{\text{th}} = 2 m_e c^2 \left(1 + \frac{m_e}{M}\right)$$
For a heavy nucleus ($M \gg m_e$), $m_e / M \to 0$:
$$E_{\text{th}} = 2 m_e c^2 = 1.022\text{ MeV}$$

### Step 2: Threshold in Electron Field (Triplet Production)
Here the target is an electron ($M = m_e$). The final state consists of three electrons/positrons ($3 m_e$):
$$s = (P_\gamma + P_e)^2 = m_e^2 c^2 + 2 m_e E$$
At threshold, all three leptons move together with total invariant mass $3 m_e$:
$$s = (3 m_e c)^2 = 9 m_e^2 c^2$$
Equating:
$$m_e^2 c^2 + 2 m_e E_{\text{th}}^{\text{triplet}} = 9 m_e^2 c^2$$
$$2 m_e E_{\text{th}}^{\text{triplet}} = 8 m_e^2 c^2 \implies E_{\text{th}}^{\text{triplet}} = 4 m_e c^2 = 2.044\text{ MeV}$$
Triplet production requires twice the energy ($2.044\text{ MeV}$) because the light target electron recoils with massive kinetic energy!""",
                    "hints": ["Use the Mandelstam invariant s = (P_1 + P_2)^2.", "At threshold, all final particles are at rest in the center of mass frame."]
                },
                {
                    "id": "prob-6-6",
                    "problemNumber": "6.6",
                    "title": "Narrow-Beam Versus Broad-Beam Attenuation and Buildup Factor",
                    "difficulty": "Intermediate",
                    "statement": r"""A broad collimated gamma beam with intensity $I_0$ passes through a shielding slab.
Due to multiple Compton scattering, scattered photons deflect back into the detector path, requiring a **dose buildup factor** $B(x, E) > 1$:
$$I(x) = I_0 \cdot B(x, E) \cdot e^{-\mu x}$$
A $1.0\text{ MeV}$ gamma source is shielded by a concrete wall of thickness $x = 30.0\text{ cm}$.
For concrete: $\mu = 0.149\text{ cm}^{-1}$ and the Berger buildup factor parameters are $a = 1.25$ and $b = 0.080$ ($B = 1 + a \mu x e^{b \mu x}$).
1. Calculate the number of mean free paths (relaxation lengths) $\mu x$.
2. Calculate the buildup factor $B$.
3. Compute the actual transmitted intensity ratio $I/I_0$ and compare with the uncollided narrow-beam transmission $e^{-\mu x}$.""",
                    "solution": r"""### Step 1: Relaxation Lengths ($\mu x$)
$$\mu x = (0.149\text{ cm}^{-1})(30.0\text{ cm}) = 4.47$$
The shield is $4.47$ mean free paths thick.

### Step 2: Buildup Factor $B$
Using the Berger formula:
$$b \mu x = 0.080 \times 4.47 = 0.3576$$
$$e^{b \mu x} = e^{0.3576} \approx 1.4299$$
$$B = 1 + a \mu x e^{b \mu x} = 1 + (1.25)(4.47)(1.4299) = 1 + (5.5875)(1.4299) = 1 + 7.999 \approx 9.00$$
The buildup factor is **$9.00$** (scattered radiation increases the dose nine-fold compared to primary unscattered photons).

### Step 3: Intensity Transmissions
Uncollided (narrow-beam) transmission:
$$\frac{I_{\text{uncollided}}}{I_0} = e^{-\mu x} = e^{-4.47} \approx 0.01145 \quad (1.145\%)$$
Actual broad-beam transmission:
$$\frac{I_{\text{actual}}}{I_0} = B \cdot e^{-\mu x} = 9.00 \times 0.01145 \approx 0.1030 \quad (10.30\%)$$
Ignoring the buildup factor would dangerously underestimate the dose transmitted through the concrete wall by an entire order of magnitude!""",
                    "hints": ["Number of mean free paths is mu * x.", "Actual transmission multiplies uncollided transmission by buildup factor B."]
                },
                {
                    "id": "prob-6-7",
                    "problemNumber": "6.7",
                    "title": "Photoelectric Absorption Cross-Section Z-Scaling and Contrast Agents",
                    "difficulty": "Easy",
                    "statement": r"""In diagnostic X-ray imaging, iodine ($Z = 53$) and barium ($Z = 56$) are employed as radiocontrast media.
1. Assuming the atomic photoelectric cross-section scales as $\tau \propto Z^4 / E^{3.5}$, calculate the ratio of the photoelectric cross-section of iodine ($Z = 53$) to that of soft biological tissue ($Z_{\text{eff}} = 7.4$).
2. Explain how this cross-section ratio provides radiographic image contrast in angiography.""",
                    "solution": r"""### Step 1: Cross-Section Ratio
$$\frac{\tau(\text{Iodine})}{\tau(\text{Tissue})} = \left(\frac{Z_{\text{I}}}{Z_{\text{tissue}}}\right)^4 = \left(\frac{53}{7.4}\right)^4 = (7.1622)^4 \approx 2,631$$
The photoelectric absorption per atom of iodine is **$\approx 2,630$ times larger** than in surrounding soft tissue!

### Step 2: Radiographic Contrast Explanation
When an aqueous iodine contrast agent (e.g., iohexol) is injected into blood vessels, the blood becomes thousands of times more opaque to diagnostic X-ray photons ($30 - 80\text{ keV}$) than adjacent muscular, vascular, and adipose tissue. Photons passing through the iodine-filled lumen are absorbed photoelectrically, casting distinct radiopaque shadows on the detector and rendering the coronary vascular anatomy visible in fluoroscopic angiography.""",
                    "hints": ["Scale photoelectric cross-section with the fourth power of atomic number: (Z_1 / Z_2)^4.", "Compare contrast agent Z with biological tissue Z_eff."]
                }
            ]
        }
    ]
    return units

if __name__ == '__main__':
    u = get_units_4_5_6()
    print(f"Generated {len(u)} units.")
    for idx, unit in enumerate(u):
        print(f"Unit {unit['unitNumber']}: {unit['title']} -> {len(unit['sections'])} sections, {len(unit['problems'])} problems")
