# -*- coding: utf-8 -*-
"""
build_pchem1_unit7.py
Unit 7: Chemical Equilibrium: Dynamic Equilibria, Law of Mass Action & Le Chatelier's Principle
Exhaustive honors-level master digital textbook module with 3x depth,
complete mathematical derivations, and zero course numbers.
"""

def get_unit7():
    return {
        "number": 7,
        "title": "Chemical Equilibrium: Dynamic Equilibria, Law of Mass Action & Le Chatelier's Principle",
        "leadSummary": "Thermodynamics and physical chemistry of dynamic chemical equilibrium: microscopic reversibility and kinetic-thermodynamic bridges, the Law of Mass Action, the thermodynamic equilibrium constant K° and its relation to standard Gibbs free energy (ΔG° = -RT ln K°), relationships connecting Kp, Kc, and Kx, homogeneous versus heterogeneous phase equilibria and invariant activities, the reaction quotient Q as an arrow of spontaneity, quantitative perturbation thermodynamics via Le Châtelier's Principle, the differential van 't Hoff equation and integrated temperature shifts, and aqueous chemical equilibria (pH, Henderson-Hasselbalch buffer mechanics, and Ksp solubility products).",
        "sections": [
            {
                "secNumber": "7.1",
                "title": "The Nature of Dynamic Chemical Equilibrium & The Equilibrium Constant",
                "content": r"""In physical chemistry, a chemical transformation does not generally proceed to complete unidirectional exhaustion of reactants. Instead, as product concentrations accumulate, the reverse reaction accelerates until a state of **Dynamic Chemical Equilibrium** is established.

### The Microscopic Nature of Dynamic Equilibrium

At equilibrium, the macroscopic properties of the system—concentrations, color, pressure, temperature, and refractive index—remain completely invariant with time. However, this macroscopic quiescence masks intense microscopic activity:
$$\text{Reactants} \xrightleftharpoons[r_r]{r_f} \text{Products}$$
Equilibrium is reached when the forward reaction rate $r_f$ equals the reverse reaction rate $r_r$ identically:
$$r_f = r_r \tag{7.1}$$
Chemical bonds continue to break and form at colossal frequencies, but the net rate of change of every chemical species is zero: $\frac{d[A_i]}{dt} = 0$.

> **The Principle of Detailed Balance (Microscopic Reversibility)**:
> In an isolated system at thermodynamic equilibrium, every microscopic elementary process must be in exact balance with its time-reversed counterpart. A system cannot maintain equilibrium by establishing cyclical reaction flows ($A \rightarrow B \rightarrow C \rightarrow A$).

### The Law of Mass Action & Equilibrium Constants ($K_c, K_p, K_x$)

In 1864, Cato Maximilian Guldberg and Peter Waage formulated the **Law of Mass Action**: For a reversible reaction at constant temperature:
$$a A + b B \rightleftharpoons c C + d D$$
The ratio of the product of the active masses of the products to the product of the active masses of the reactants, each raised to their respective stoichiometric coefficients, is a constant:

1. **Concentration Equilibrium Constant ($K_c$)**:
   $$K_c = \frac{[C]^c [D]^d}{[A]^a [B]^b} \tag{7.2}$$
2. **Pressure Equilibrium Constant ($K_p$)**:
   For gas-phase reactions expressed in partial pressures $P_i$:
   $$K_p = \frac{P_C^c P_D^d}{P_A^a P_B^b} \tag{7.3}$$
3. **Mole Fraction Equilibrium Constant ($K_x$)**:
   $$K_x = \frac{x_C^c x_D^d}{x_A^a x_B^b} \tag{7.4}$$

### Exact Relationship Between $K_p, K_c$, and $K_x$

For ideal gases, partial pressure is related to molar concentration by $P_i = \left(\frac{n_i}{V}\right) R T = [A_i] R T$.
Substituting into $K_p$:
$$K_p = \frac{([C] R T)^c ([D] R T)^d}{([A] R T)^a ([B] R T)^b} = \frac{[C]^c [D]^d}{[A]^a [B]^b} (R T)^{(c + d) - (a + b)}$$
Defining $\Delta n_g \equiv (c + d) - (a + b)$ as the stoichiometric change in moles of gas:
$$K_p = K_c (R T)^{\Delta n_g} \tag{7.5}$$
* If $\Delta n_g = 0$ (e.g., $\text{H}_2(g) + \text{I}_2(g) \rightleftharpoons 2\text{HI}(g)$): $K_p = K_c$ identically.
* If $\Delta n_g > 0$ (dissociation): $K_p > K_c$ (at $R T > 1$).
* If $\Delta n_g < 0$ (condensation/synthesis): $K_p < K_c$.

From Dalton's law of partial pressures, $P_i = x_i P_{total}$. Substituting into $K_p$:
$$K_p = \frac{(x_C P_{total})^c (x_D P_{total})^d}{(x_A P_{total})^a (x_B P_{total})^b} = \frac{x_C^c x_D^d}{x_A^a x_B^b} P_{total}^{\Delta n_g} = K_x P_{total}^{\Delta n_g}$$
$$K_x = K_p P_{total}^{-\Delta n_g} \tag{7.6}$$
While $K_p$ depends only on temperature, **$K_x$ depends explicitly on total system pressure whenever $\Delta n_g \neq 0$**!

### Thermodynamic Foundation: $\Delta G^\circ = -R T \ln K^\circ$

Thermodynamically, equilibrium is the state of minimum Gibbs free energy at constant $T$ and $P$ ($dG = 0$).
For any reaction $\sum \nu_i A_i = 0$, the reaction Gibbs energy is:
$$\Delta_r G = \left(\frac{\partial G}{\partial \xi}\right)_{T, P} = \sum_{i} \nu_i \mu_i$$
The chemical potential of species $i$ in a mixture is:
$$\mu_i = \mu_i^\circ + R T \ln a_i$$
where $a_i$ is the dimensionless **thermodynamic activity** ($a_i = P_i / P^\circ$ for ideal gases with $P^\circ = 1\text{ bar}$, $a_i \approx [C_i] / C^\circ$ for ideal dilute solutions with $C^\circ = 1\text{ M}$).

Substituting into the reaction Gibbs energy:
$$\Delta_r G = \sum_{i} \nu_i \mu_i^\circ + R T \sum_{i} \nu_i \ln a_i = \Delta_r G^\circ + R T \ln \left( \prod_{i} a_i^{\nu_i} \right)$$
Defining the **Reaction Quotient** $Q \equiv \prod_i a_i^{\nu_i}$:
$$\Delta_r G = \Delta_r G^\circ + R T \ln Q \tag{7.7}$$

At thermodynamic equilibrium, the driving force vanishes: $\Delta_r G = 0$, and the reaction quotient reaches its equilibrium value $Q \rightarrow K^\circ$:
$$0 = \Delta_r G^\circ + R T \ln K^\circ \implies \Delta_r G^\circ = -R T \ln K^\circ \tag{7.8}$$
Or expressing $K^\circ$ in exponential form:
$$K^\circ = \exp\left( -\frac{\Delta_r G^\circ}{R T} \right) \tag{7.9}$$
Because $\Delta_r G^\circ$ is a pure standard-state property evaluated at $P^\circ = 1\text{ bar}$, **the thermodynamic equilibrium constant $K^\circ$ is dimensionless and depends strictly upon temperature alone**."""
            },
            {
                "secNumber": "7.2",
                "title": "Homogeneous vs Heterogeneous Equilibria & Multiple Equilibria",
                "content": r"""The algebraic formulation of the equilibrium constant expression depends upon the number and nature of thermodynamic phases present in the reacting system.

### Homogeneous vs Heterogeneous Equilibria

1. **Homogeneous Equilibria**: All reacting chemical species reside within a single, continuous physical phase:
   * Gas phase: $\text{N}_2\text{O}_4(g) \rightleftharpoons 2\text{NO}_2(g)$
   * Liquid aqueous phase: $\text{CH}_3\text{COOH}(aq) + \text{H}_2\text{O}(l) \rightleftharpoons \text{CH}_3\text{COO}^-(aq) + \text{H}_3\text{O}^+(aq)$
2. **Heterogeneous Equilibria**: Reacting species occupy two or more distinct physical phases in contact (solid-gas, solid-liquid, liquid-gas):
   * Thermal decomposition of limestone:
     $$\text{CaCO}_3(s) \rightleftharpoons \text{CaO}(s) + \text{CO}_2(g)$$
   * Iron-steam equilibrium:
     $$3\text{Fe}(s) + 4\text{H}_2\text{O}(g) \rightleftharpoons \text{Fe}_3\text{O}_4(s) + 4\text{H}_2(g)$$

### The Rule of Invariant Condensed Phase Activities

> **Fundamental Convention of Heterogeneous Equilibria**:
> **Pure solids and pure liquids are completely omitted from equilibrium constant expressions.**
> *Thermodynamic Proof*: The thermodynamic activity of a pure solid or pure liquid in its standard state at pressure $P$ is:
> $$a_i = \exp\left( \frac{\mu_i(P) - \mu_i^\circ(P^\circ)}{R T} \right) = \exp\left( \frac{\int_{P^\circ}^P V_{m,i} dP'}{R T} \right) \approx \exp\left( \frac{V_{m,i} (P - P^\circ)}{R T} \right)$$
> Because the molar volumes of solids and liquids are minuscule ($V_m \sim 10^{-5}\text{ m}^3\cdot\text{mol}^{-1}$), even under several atmospheres of pressure, the Poynting factor correction is negligible:
> $$a_{solid} \equiv 1, \qquad a_{liquid} \equiv 1 \quad (\text{to high precision})$$

Applying this rigorous rule to the limestone decomposition:
$$K^\circ = \frac{a(\text{CaO}, s) \cdot a(\text{CO}_2, g)}{a(\text{CaCO}_3, s)} = \frac{(1) \cdot (P_{\text{CO}_2} / P^\circ)}{(1)} = \frac{P_{\text{CO}_2}}{P^\circ}$$
At a given temperature, the equilibrium partial pressure of carbon dioxide above decomposing calcium carbonate is fixed and independent of the amounts of solid $\text{CaCO}_3$ or $\text{CaO}$ present:
$$K_p = P_{\text{CO}_2} \tag{7.10}$$

### Mathematical Rules for Manipulating Equilibrium Constants

When balancing and combining chemical equilibria:
1. **Reversing a Reaction**:
   If $A \rightleftharpoons B$ has constant $K_1$, then $B \rightleftharpoons A$ has constant $K_2$:
   $$K_2 = \frac{1}{K_1} = K_1^{-1}$$
2. **Multiplying Stoichiometric Coefficients by a Factor $n$**:
   If $A \rightleftharpoons B$ has constant $K_1$, then $n A \rightleftharpoons n B$ has constant $K_n$:
   $$K_n = (K_1)^n$$
3. **Adding Consecutive Reactions (Multiple Equilibria)**:
   If Reaction 1 ($A \rightleftharpoons B$, constant $K_1$) is added to Reaction 2 ($B \rightleftharpoons C$, constant $K_2$) to yield the net reaction ($A \rightleftharpoons C$):
   $$K_{net} = \frac{[C]}{[A]} = \frac{[B]}{[A]} \times \frac{[C]}{[B]} = K_1 \cdot K_2 \tag{7.11}$$
   **When chemical equations are added, their equilibrium constants are multiplied.**"""
            },
            {
                "secNumber": "7.3",
                "title": "The Reaction Quotient Q & Direction of Spontaneous Shift",
                "content": r"""Before a chemical system reaches dynamic equilibrium, or when an equilibrium system is subjected to external perturbations, physical chemists must determine the spontaneous direction of reaction.

### The Reaction Quotient ($Q$) as a Thermodynamic Compass

For a general reaction $a A + b B \rightleftharpoons c C + d D$, the **Reaction Quotient ($Q_c$ or $Q_p$)** has an identical mathematical algebraic form to the equilibrium constant, but is evaluated using **instantaneous non-equilibrium concentrations or pressures**:
$$Q_c = \frac{[C]_{inst}^c [D]_{inst}^d}{[A]_{inst}^a [B]_{inst}^b}, \qquad Q_p = \frac{P_{C, inst}^c P_{D, inst}^d}{P_{A, inst}^a P_{B, inst}^b} \tag{7.12}$$

Comparing the instantaneous quotient $Q$ with the equilibrium constant $K$ reveals the thermodynamic driving force from $\Delta_r G = R T \ln(Q / K)$:

| Condition | Sign of $\Delta_r G = R T \ln(Q/K)$ | Thermodynamic State | Spontaneous Direction of Shift |
|---|---|---|---|
| $Q < K$ | $\Delta_r G < 0$ (Negative) | Reactant excess / Product deficit | **Forward ($\rightarrow$)**: Reactants convert into products until $Q = K$. |
| $Q = K$ | $\Delta_r G = 0$ (Zero) | Dynamic Thermodynamic Equilibrium | **No Net Shift**: Forward and reverse rates are equal ($r_f = r_r$). |
| $Q > K$ | $\Delta_r G > 0$ (Positive) | Product excess / Reactant deficit | **Reverse ($\leftarrow$)**: Products decompose into reactants until $Q = K$. |

### Quantitative Equilibrium Calculations: The ICE Table Method

The systematic solution of equilibrium concentrations relies on the **ICE (Initial, Change, Equilibrium)** algorithmic framework:

1. **I (Initial)**: Tabulate initial concentrations or pressures of all species $[A]_0, [B]_0, \dots$
2. **C (Change)**: Introduce an unknown extent of reaction $x$. Use stoichiometric coefficients to define changes in moles/concentration: $-a x$ for reactants, $+c x$ for products.
3. **E (Equilibrium)**: Formulate algebraic equilibrium expressions: $[A]_{eq} = [A]_0 - a x, [C]_{eq} = [C]_0 + c x$.
4. **Solve**: Substitute equilibrium terms into $K_c = \frac{[C]_{eq}^c [D]_{eq}^d}{[A]_{eq}^a [B]_{eq}^b}$ and solve the resulting polynomial (linear, quadratic, or cubic) for physical roots ($x > 0$ and $[A_i]_{eq} \ge 0$).

#### The 5% Approximation Rule:
When $K_c \ll 1$ (typically $K_c < 10^{-4}$ and initial concentration $[A]_0 / K_c > 1000$), the extent of reaction $x$ is exceedingly small compared to $[A]_0$:
$$[A]_0 - a x \approx [A]_0$$
This avoids solving complex quadratic equations. The approximation is scientifically valid if the calculated $x$ is less than $5\%$ of $[A]_0$:
$$\frac{a x}{[A]_0} \times 100\% < 5\%$$"""
            },
            {
                "secNumber": "7.4",
                "title": "Le Chatelier's Principle & Perturbation Analysis",
                "content": r"""In 1884, Henri Louis Le Chatelier formulated one of the most profound qualitative generalizations in physical chemistry:

> **Le Chatelier's Principle**:
> If a chemical system at dynamic equilibrium is subjected to an external perturbation or stress (a change in concentration, pressure, volume, or temperature), the system will spontaneously adjust its equilibrium state in such a direction as to partially counteract and relieve the imposed stress.

Rather than treating Le Chatelier's principle as an empirical rule, modern physical chemistry derives all shifts directly from the thermodynamic response of the reaction quotient $Q$ and equilibrium constant $K$.

### 1. Effect of Concentration Perturbations
* **Adding a Reactant ($+[A]$)**: Denominator of $Q$ increases $\implies Q < K$. The system spontaneously shifts **forward ($\rightarrow$)**, consuming added $A$ to form products until $Q = K$.
* **Removing a Product ($- [C]$)**: Numerator of $Q$ decreases $\implies Q < K$. System shifts **forward ($\rightarrow$)**, replenishing the removed product.
* *Industrial Application*: In the synthesis of ethyl acetate via esterification ($\text{CH}_3\text{COOH} + \text{C}_2\text{H}_5\text{OH} \rightleftharpoons \text{CH}_3\text{COOC}_2\text{H}_5 + \text{H}_2\text{O}$), continuous distillation of water drives the reaction to near $100\%$ completion.

### 2. Effect of Volume and Pressure Perturbations (Gas Reactions)
Decreasing container volume by compression ($V \downarrow$) increases total pressure ($P \uparrow$) and inflates every partial pressure $P_i = n_i R T / V$.
Recall Eq. (7.6): $K_x = K_p P_{total}^{-\Delta n_g}$.
* If $\Delta n_g > 0$ (e.g., $\text{N}_2\text{O}_4(g) \rightleftharpoons 2\text{NO}_2(g), \Delta n_g = +1$):
  $Q_p = \frac{P_{\text{NO}_2}^2}{P_{\text{N}_2\text{O}_4}} \propto \frac{(1/V)^2}{1/V} = \frac{1}{V}$. Compressing ($V \downarrow$) causes $Q_p > K_p$. System shifts **reverse ($\leftarrow$) toward fewer moles of gas**.
* If $\Delta n_g < 0$ (e.g., $\text{N}_2(g) + 3\text{H}_2(g) \rightleftharpoons 2\text{NH}_3(g), \Delta n_g = -2$):
  Compressing causes $Q_p < K_p$. System shifts **forward ($\rightarrow$) toward fewer moles of gas**.
* If $\Delta n_g = 0$: Pressure changes have zero effect on equilibrium composition.

#### Addition of an Inert Gas (e.g., Argon):
* *At Constant Volume ($V = \text{const}$)*: Total pressure rises, but individual partial pressures $P_i = n_i R T / V$ are unchanged. $Q_p$ is unchanged $\implies$ **Zero effect on equilibrium!**
* *At Constant Pressure ($P = \text{const}$)*: The container must expand ($V \uparrow$) to accommodate the inert gas. This dilutes all reacting partial pressures, acting identically to a volume expansion, shifting equilibrium toward the side with **more moles of gas**.

### 3. Effect of Temperature: The van 't Hoff Equation

Temperature is the **only variable that changes the numerical value of the equilibrium constant $K$**.

Differentiating the fundamental thermodynamic relation $\ln K^\circ = -\frac{\Delta_r G^\circ}{R T}$ with respect to temperature at constant pressure:
$$\frac{d\ln K^\circ}{dT} = -\frac{1}{R} \frac{d}{dT}\left(\frac{\Delta_r G^\circ}{T}\right)$$
Using the Gibbs-Helmholtz equation $\frac{d(\Delta G^\circ / T)}{dT} = -\frac{\Delta H^\circ}{T^2}$:
$$\frac{d\ln K^\circ}{dT} = \frac{\Delta_r H^\circ}{R T^2} \tag{7.13}$$
This is the differential **van 't Hoff Equation**.

1. **Endothermic Reactions ($\Delta_r H^\circ > 0$)**:
   $$\frac{d\ln K^\circ}{dT} > 0$$
   Increasing temperature **increases $K^\circ$**. The system shifts **forward ($\rightarrow$)**, absorbing heat to counteract the temperature increase.
2. **Exothermic Reactions ($\Delta_r H^\circ < 0$)**:
   $$\frac{d\ln K^\circ}{dT} < 0$$
   Increasing temperature **decreases $K^\circ$**. The system shifts **reverse ($\leftarrow$)**, releasing less heat.

Integrating the van 't Hoff equation between $T_1$ and $T_2$ assuming constant $\Delta_r H^\circ$:
$$\ln\left(\frac{K_2}{K_1}\right) = -\frac{\Delta_r H^\circ}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right) = \frac{\Delta_r H^\circ}{R}\left(\frac{T_2 - T_1}{T_1 T_2}\right) \tag{7.14}$$
A plot of $\ln K$ versus $1/T$ is a straight line with slope $-\frac{\Delta_r H^\circ}{R}$, providing a purely non-calorimetric method to determine reaction enthalpies!

### 4. Effect of a Catalyst

A catalyst lowers the activation energy of both the forward and reverse reactions by an identical amount: $\Delta E_a^{forward} = \Delta E_a^{reverse}$.
$$k_f^{cat} = k_f \cdot \chi, \qquad k_r^{cat} = k_r \cdot \chi \implies K = \frac{k_f^{cat}}{k_r^{cat}} = \frac{k_f}{k_r}$$
**A catalyst has zero effect on the equilibrium constant $K$, zero effect on equilibrium concentrations, and causes zero shift in the position of equilibrium.** It merely accelerates the rate at which equilibrium is reached."""
            },
            {
                "secNumber": "7.5",
                "title": "Equilibrium in Aqueous Acid-Base & Solubility Systems",
                "content": r"""Aqueous solutions host vital dynamic equilibria governing biological cells, industrial wet chemistry, and environmental geochemistry.

### The Autoionization of Water & The pH Scale

Pure liquid water undergoes dynamic self-ionization:
$$2\text{H}_2\text{O}(l) \rightleftharpoons \text{H}_3\text{O}^+(aq) + \text{OH}^-(aq)$$
The thermodynamic equilibrium constant is the **Ion Product of Water ($K_w$)**:
$$K_w = [\text{H}_3\text{O}^+][\text{OH}^-] \tag{7.15}$$
At $298.15\text{ K}$, $K_w = 1.008 \times 10^{-14} \approx 1.00 \times 10^{-14}$.
Because autoionization is endothermic ($\Delta H_{auto}^\circ = +55.8\text{ kJ}\cdot\text{mol}^{-1}$), $K_w$ increases steeply with temperature: at $373.15\text{ K}$ ($100^\circ\text{C}$), $K_w \approx 5.4 \times 10^{-13}$, and neutral pH drops to $6.13$!

In 1909, Søren Sørensen introduced the logarithmic **pH scale**:
$$\text{pH} \equiv -\log_{10} a_{\text{H}^+} \approx -\log_{10}[\text{H}_3\text{O}^+], \qquad \text{pOH} \equiv -\log_{10}[\text{OH}^-]$$
Taking the negative logarithm of $K_w$:
$$\text{pH} + \text{pOH} = \text{p}K_w = 14.00 \quad (\text{at } 298.15\text{ K}) \tag{7.16}$$

### Weak Acid Dissociation ($K_a$) & Conjugate Pairs

A Brønsted-Lowry weak acid $\text{HA}$ ionizes reversibly in water:
$$\text{HA}(aq) + \text{H}_2\text{O}(l) \rightleftharpoons \text{H}_3\text{O}^+(aq) + \text{A}^-(aq)$$
$$K_a = \frac{[\text{H}_3\text{O}^+][\text{A}^-]}{[\text{HA}]}, \qquad \text{p}K_a = -\log_{10} K_a \tag{7.17}$$
Its conjugate base $\text{A}^-$ hydrolyzes water:
$$\text{A}^-(aq) + \text{H}_2\text{O}(l) \rightleftharpoons \text{HA}(aq) + \text{OH}^-(aq)$$
$$K_b = \frac{[\text{HA}][\text{OH}^-]}{[\text{A}^-]}, \qquad \text{p}K_b = -\log_{10} K_b$$
Multiplying $K_a$ and $K_b$:
$$K_a \cdot K_b = \frac{[\text{H}_3\text{O}^+][\text{A}^-]}{[\text{HA}]} \times \frac{[\text{HA}][\text{OH}^-]}{[\text{A}^-]} = [\text{H}_3\text{O}^+][\text{OH}^-] = K_w \tag{7.18}$$
$$\text{p}K_a + \text{p}K_b = \text{p}K_w = 14.00$$

### Buffer Solutions & The Henderson-Hasselbalch Equation

A **buffer solution** resists changes in pH upon the addition of small amounts of strong acid or base. It consists of a conjugate acid-base pair in roughly equimolar proportions:
* Acidic buffer: Weak acid $+$ conjugate base salt (e.g., $\text{CH}_3\text{COOH} / \text{CH}_3\text{COONa}$).
* Basic buffer: Weak base $+$ conjugate acid salt (e.g., $\text{NH}_3 / \text{NH}_4\text{Cl}$).

Taking the logarithm of the $K_a$ expression:
$$\log_{10} K_a = \log_{10}[\text{H}_3\text{O}^+] + \log_{10}\left(\frac{[\text{A}^-]}{[\text{HA}]}\right)$$
$$-\text{p}K_a = -\text{pH} + \log_{10}\left(\frac{[\text{A}^-]}{[\text{HA}]}\right)$$
Rearranging yields the **Henderson-Hasselbalch Equation (1908/1916)**:
$$\text{pH} = \text{p}K_a + \log_{10}\left(\frac{[\text{A}^-]}{[\text{HA}]}\right) = \text{p}K_a + \log_{10}\left(\frac{[\text{conjugate base}]}{[\text{weak acid}]}\right) \tag{7.19}$$
* When $[\text{A}^-] = [\text{HA}]$ (the half-equivalence point in a titration): $\text{pH} = \text{p}K_a$.
* Optimal buffer capacity occurs within the range $\text{pH} = \text{p}K_a \pm 1$.

### Solubility Equilibria: The Solubility Product Constant ($K_{sp}$)

For a sparingly soluble ionic solid $M_p X_q$ in equilibrium with its dissolved aqueous ions:
$$M_p X_q(s) \rightleftharpoons p M^{z+}(aq) + q X^{z-}(aq)$$
Since the activity of the pure solid is unity ($a_{solid} = 1$):
$$K_{sp} = [M^{z+}]^p [X^{z-}]^q \tag{7.20}$$

#### The Ion Product ($Q_{sp}$) & Precipitation Criteria:
* $Q_{sp} < K_{sp}$: Unsaturated solution; more solid can dissolve.
* $Q_{sp} = K_{sp}$: Saturated dynamic equilibrium solution.
* $Q_{sp} > K_{sp}$: Supersaturated metastable solution; spontaneous **precipitation occurs** until $Q_{sp} = K_{sp}$.

#### The Common Ion Effect on Solubility:
According to Le Chatelier's Principle, adding an external soluble salt sharing an ion with the precipitate (e.g., adding $\text{NaCl}$ to a saturated $\text{AgCl}$ solution, adding $\text{Cl}^-$) drives the dissolution equilibrium reverse ($\leftarrow$), drastically **decreasing the molar solubility** of the sparingly soluble salt."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational Level",
                "title": "ICE Table Equilibrium Calculations for Gaseous Phosphorus Pentachloride Dissociation",
                "statement": r"""Solid phosphorus pentachloride sublimes and vaporizes into an equilibrium mixture of phosphorus trichloride and chlorine gas:
$$\text{PCl}_5(g) \rightleftharpoons \text{PCl}_3(g) + \text{Cl}_2(g)$$

At $T = 523.15\text{ K}$ ($250^\circ\text{C}$), the equilibrium constant for this gas-phase reaction is $K_c = 0.0420\text{ M}$. Exactly $0.500\text{ mol}$ of pure $\text{PCl}_5(g)$ is introduced into an evacuated, rigid $2.000\text{ L}$ stainless steel reaction vessel and heated to $523.15\text{ K}$.

1. Calculate the initial concentration $[\text{PCl}_5]_0$ in $\text{mol}\cdot\text{L}^{-1}$.
2. Construct an ICE table defining the extent of reaction $x$.
3. Calculate the equilibrium concentrations of $\text{PCl}_5, \text{PCl}_3$, and $\text{Cl}_2$.
4. Calculate the degree of dissociation $\alpha$ of $\text{PCl}_5$ at this temperature.
5. Calculate the pressure equilibrium constant $K_p$ and the total equilibrium pressure $P_{total}$ inside the vessel in atmospheres.""",
                "solution": r"""### Step 1: Initial Concentration

$$[\text{PCl}_5]_0 = \frac{n_0}{V} = \frac{0.500\text{ mol}}{2.000\text{ L}} = 0.2500\text{ M}$$
$$[\text{PCl}_3]_0 = 0.000\text{ M}, \qquad [\text{Cl}_2]_0 = 0.000\text{ M}$$

### Step 2: ICE Table Formulation

| Reaction | $\text{PCl}_5(g)$ | $\rightleftharpoons$ | $\text{PCl}_3(g)$ | $+$ | $\text{Cl}_2(g)$ |
|---|---|---|---|---|---|
| **Initial (I)** | $0.2500$ | | $0$ | | $0$ |
| **Change (C)** | $-x$ | | $+x$ | | $+x$ |
| **Equilibrium (E)** | $0.2500 - x$ | | $x$ | | $x$ |

### Step 3: Solve for Equilibrium Extent $x$

From the equilibrium expression:
$$K_c = \frac{[\text{PCl}_3][\text{Cl}_2]}{[\text{PCl}_5]} = \frac{x^2}{0.2500 - x} = 0.0420$$
$$x^2 = 0.0420(0.2500 - x) = 0.01050 - 0.0420x$$
$$x^2 + 0.0420x - 0.01050 = 0$$

Using the quadratic formula $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ with $a = 1, b = 0.0420, c = -0.01050$:
$$b^2 - 4ac = (0.0420)^2 - 4(1)(-0.01050) = 0.001764 + 0.04200 = 0.043764$$
$$\sqrt{b^2 - 4ac} = \sqrt{0.043764} = 0.20920$$
$$x = \frac{-0.0420 + 0.20920}{2} = \frac{0.16720}{2} = 0.08360\text{ M}$$
(The negative root is discarded as unphysical).

Calculate equilibrium concentrations:
$$[\text{PCl}_3]_{eq} = x = 0.0836\text{ M}$$
$$[\text{Cl}_2]_{eq} = x = 0.0836\text{ M}$$
$$[\text{PCl}_5]_{eq} = 0.2500 - 0.0836 = 0.1664\text{ M}$$

Check $K_c$:
$$\frac{(0.0836)^2}{0.1664} = \frac{0.006989}{0.1664} = 0.04200\text{ M} \quad (\text{Exact!})$$

### Step 4: Degree of Dissociation $\alpha$

$$\alpha = \frac{x}{[\text{PCl}_5]_0} = \frac{0.08360\text{ M}}{0.2500\text{ M}} = 0.3344 \approx 33.4\%$$
Under these conditions, **$33.4\%$ of the $\text{PCl}_5$ molecules are dissociated**.

### Step 5: Calculation of $K_p$ and Total Pressure

Change in stoichiometric gas moles: $\Delta n_g = (1 + 1) - 1 = +1$.
$$K_p = K_c (R T)^{\Delta n_g} = K_c (R T)^1$$
Using $R = 0.082057\text{ L}\cdot\text{atm}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}$ and $T = 523.15\text{ K}$:
$$R T = 0.082057 \times 523.15 = 42.928\text{ L}\cdot\text{atm}\cdot\text{mol}^{-1}$$
$$K_p = 0.0420 \times 42.928 = 1.803\text{ atm}$$

Total molar concentration at equilibrium:
$$C_{total} = [\text{PCl}_5] + [\text{PCl}_3] + [\text{Cl}_2] = 0.1664 + 0.0836 + 0.0836 = 0.3336\text{ M}$$
Total equilibrium pressure:
$$P_{total} = C_{total} R T = (0.3336\text{ mol/L}) \times (42.928\text{ L}\cdot\text{atm/mol}) = 14.32\text{ atm} \quad (\approx 14.51\text{ bar})$$"""
            },
            {
                "tier": "Advanced Level",
                "title": "Thermodynamic Van 't Hoff Analysis of High-Temperature Ammonia Synthesis Equilibrium Shift",
                "statement": r"""The industrial Haber-Bosch ammonia synthesis is governed by the exothermic equilibrium:
$$\text{N}_2(g) + 3\text{H}_2(g) \rightleftharpoons 2\text{NH}_3(g)$$

Standard thermodynamic parameters at $T_1 = 298.15\text{ K}$:
* Standard reaction enthalpy: $\Delta_r H^\circ = -92.22\text{ kJ}\cdot\text{mol}^{-1}$
* Standard reaction entropy: $\Delta_r S^\circ = -198.75\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}$
* Gas constant: $R = 8.314\,463\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}$

1. Calculate the standard Gibbs free energy of reaction $\Delta_r G^\circ(298.15\text{ K})$ and the thermodynamic equilibrium constant $K_p^\circ(298.15\text{ K})$.
2. Using the integrated van 't Hoff equation assuming constant $\Delta_r H^\circ$, calculate the equilibrium constant $K_p^\circ$ at the industrial reactor operating temperature $T_2 = 723.15\text{ K}$ ($450.0^\circ\text{C}$).
3. Explain the industrial "Haber Paradox": Why must chemical plants operate this reaction at a high temperature ($450^\circ\text{C}$) that thermodynamically suppresses the equilibrium yield by orders of magnitude, and how is this compensated using high pressure ($200\text{ bar}$) and iron catalysts?""",
                "solution": r"""### Step 1: Standard Gibbs Free Energy & $K_p^\circ$ at $298.15\text{ K}$

$$\Delta_r G^\circ(298.15\text{ K}) = \Delta_r H^\circ - T \Delta_r S^\circ$$
$$\Delta_r G^\circ = -92\,220\text{ J}\cdot\text{mol}^{-1} - (298.15\text{ K}) \times (-198.75\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1})$$
$$\Delta_r G^\circ = -92\,220 + 59\,257.3 = -32\,962.7\text{ J}\cdot\text{mol}^{-1} = -32.963\text{ kJ}\cdot\text{mol}^{-1}$$

Calculate $K_p^\circ$ at $298.15\text{ K}$:
$$\ln K_p^\circ(298.15\text{ K}) = -\frac{\Delta_r G^\circ}{R T} = -\frac{-32\,962.7}{8.3145 \times 298.15} = +\frac{32\,962.7}{2478.96} = +13.297$$
$$K_p^\circ(298.15\text{ K}) = \exp(13.297) = 5.95 \times 10^5$$
At room temperature, the equilibrium constant is colossal ($K_p \approx 6 \times 10^5$), predicting virtually $100\%$ theoretical conversion to ammonia!

### Step 2: Van 't Hoff Calculation of $K_p^\circ$ at $T_2 = 723.15\text{ K}$

Using the integrated van 't Hoff equation:
$$\ln\left(\frac{K_2}{K_1}\right) = -\frac{\Delta_r H^\circ}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right)$$
$$\frac{1}{T_2} - \frac{1}{T_1} = \frac{1}{723.15} - \frac{1}{298.15} = 0.0013828 - 0.0033540 = -1.9712 \times 10^{-3}\text{ K}^{-1}$$
$$-\frac{\Delta_r H^\circ}{R} = -\frac{-92\,220}{8.3145} = +11\,091.5\text{ K}$$
$$\ln\left(\frac{K_2}{K_1}\right) = (11\,091.5\text{ K}) \times (-1.9712 \times 10^{-3}\text{ K}^{-1}) = -21.863$$
$$\frac{K_2}{K_1} = \exp(-21.863) = 3.20 \times 10^{-10}$$

Calculate $K_p^\circ(723.15\text{ K})$:
$$K_2 = K_1 \times (3.20 \times 10^{-10}) = (5.95 \times 10^5) \times (3.20 \times 10^{-10}) = 1.90 \times 10^{-4}$$
At $450^\circ\text{C}$, the equilibrium constant has collapsed from $6 \times 10^5$ down to **$1.9 \times 10^{-4}$**—a reduction of nearly **ten orders of magnitude**!

### Step 3: Resolution of the "Haber Paradox"

1. **The Kinetic Barrier**: Although ammonia formation is thermodynamically favored at room temperature, the triple covalent bond of molecular nitrogen possesses an immense bond dissociation energy:
   $$D(\text{N}\equiv\text{N}) = 945\text{ kJ}\cdot\text{mol}^{-1}$$
   The activation energy for uncatalyzed nitrogen dissociation is so colossal that at $298\text{ K}$, the reaction rate is identically zero; not a single molecule of ammonia forms over a human lifetime.
2. **The High-Temperature Compromise**: Elevating the temperature to $450^\circ\text{C}$ ($723\text{ K}$) provides sufficient thermal activation for iron catalysts to cleave the $\text{N}\equiv\text{N}$ bond at an acceptable reaction velocity ($r \propto e^{-E_a/RT}$).
3. **High-Pressure Compensation via Le Chatelier**: To overcome the unfavorable thermodynamic equilibrium shift caused by high temperature, the plant operates at colossal pressures of $P = 150 - 250\text{ bar}$.
   Since $\Delta n_g = 2 - (1 + 3) = -2$:
   $$K_x = K_p P^2$$
   Multiplying by $P^2 = (200)^2 = 40\,000$ drives the mole fraction equilibrium constant $K_x$ up by a factor of 40,000, forcing a commercially viable $15 - 20\%$ yield per single pass through the catalytic converter, which is continuously recycled."""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Thermodynamic Proof of the Pressure Dependence of the Mole Fraction Equilibrium Constant Kx",
                "statement": r"""For an ideal gas reaction $\sum_i \nu_i A_i = 0$, the thermodynamic equilibrium constant $K_p^\circ$ is defined in terms of partial pressures relative to standard pressure $P^\circ = 1\text{ bar}$:
$$K_p^\circ \equiv \prod_i \left(\frac{P_i}{P^\circ}\right)^{\nu_i}$$
Because $K_p^\circ = \exp(-\Delta_r G^\circ / R T)$ depends solely on temperature, $\left(\frac{\partial K_p^\circ}{\partial P}\right)_T = 0$.

However, the mole fraction equilibrium constant is:
$$K_x \equiv \prod_i x_i^{\nu_i}$$

1. Using Dalton's law of partial pressures $P_i = x_i P$, express $K_x$ in terms of $K_p^\circ, P$, and standard pressure $P^\circ$.
2. Differentiate $\ln K_x$ with respect to total pressure $P$ at constant temperature $T$ to prove:
   $$\left(\frac{\partial \ln K_x}{\partial P}\right)_T = -\frac{\Delta n_g}{P}$$
   where $\Delta n_g = \sum \nu_i$.
3. For an arbitrary non-ideal real solution or dense fluid where chemical potential is given by $\mu_i = \mu_i^\circ + R T \ln(x_i \gamma_i)$, use the fundamental thermodynamic identity $\left(\frac{\partial \mu_i}{\partial P}\right)_T = V_{m,i}$ to prove the general relation:
   $$\left(\frac{\partial \ln K_x}{\partial P}\right)_T = -\frac{\Delta V_{rxn}^\circ}{R T}$$
   where $\Delta V_{rxn}^\circ \equiv \sum \nu_i V_{m,i}^\circ$ is the standard molar volume change of reaction, thereby providing the exact thermodynamic proof of Le Chatelier's pressure principle.""",
                "solution": r"""### Step 1: Algebraic Relation Between $K_x$ and $K_p^\circ$

By Dalton's law for ideal gas mixtures:
$$P_i = x_i P$$
Substitute into the definition of $K_p^\circ$:
$$K_p^\circ = \prod_i \left(\frac{x_i P}{P^\circ}\right)^{\nu_i} = \left(\prod_i x_i^{\nu_i}\right) \left(\frac{P}{P^\circ}\right)^{\sum \nu_i} = K_x \left(\frac{P}{P^\circ}\right)^{\Delta n_g}$$
where $\Delta n_g \equiv \sum_i \nu_i$.
Solving for $K_x$:
$$K_x = K_p^\circ \left(\frac{P}{P^\circ}\right)^{-\Delta n_g} \tag{1}$$

### Step 2: Pressure Derivative for Ideal Gases

Take the natural logarithm of Eq. (1):
$$\ln K_x = \ln K_p^\circ - \Delta n_g \ln\left(\frac{P}{P^\circ}\right) = \ln K_p^\circ - \Delta n_g (\ln P - \ln P^\circ) \tag{2}$$

Differentiate with respect to total pressure $P$ at constant temperature $T$:
$$\left(\frac{\partial \ln K_x}{\partial P}\right)_T = \left(\frac{\partial \ln K_p^\circ}{\partial P}\right)_T - \Delta n_g \frac{d\ln P}{dP}$$
Since $K_p^\circ$ is a function strictly of temperature alone ($\Delta_r G^\circ$ is evaluated at standard pressure $P^\circ$), $\left(\frac{\partial \ln K_p^\circ}{\partial P}\right)_T = 0$.
Therefore:
$$\left(\frac{\partial \ln K_x}{\partial P}\right)_T = 0 - \Delta n_g \left(\frac{1}{P}\right) = -\frac{\Delta n_g}{P} \tag{Q.E.D.}$$

#### Physical Interpretation:
* If $\Delta n_g < 0$ (reaction reduces moles of gas): $-\Delta n_g / P > 0 \implies \left(\frac{\partial \ln K_x}{\partial P}\right)_T > 0$. Increasing pressure increases $K_x$, shifting the equilibrium toward products (forward).
* If $\Delta n_g > 0$ (reaction produces moles of gas): $\left(\frac{\partial \ln K_x}{\partial P}\right)_T < 0$. Increasing pressure decreases $K_x$, shifting the equilibrium toward reactants (reverse).
* If $\Delta n_g = 0$: $\left(\frac{\partial \ln K_x}{\partial P}\right)_T = 0$. Equilibrium composition is invariant with pressure.

### Step 3: General Thermodynamic Proof for Dense Fluids & Real Solutions

For any chemical equilibrium in an arbitrary phase:
$$\sum_i \nu_i \mu_i = 0 \tag{3}$$
In an ideal solution:
$$\mu_i(T, P, x_i) = \mu_i^\circ(T, P) + R T \ln x_i \tag{4}$$
Substitute Eq. (4) into Eq. (3):
$$\sum_i \nu_i \mu_i^\circ(T, P) + R T \sum_i \nu_i \ln x_i = 0$$
$$\Delta_r G^\circ(T, P) + R T \ln K_x = 0 \implies \ln K_x = -\frac{\Delta_r G^\circ(T, P)}{R T} \tag{5}$$

Differentiate Eq. (5) with respect to pressure $P$ at constant temperature:
$$\left(\frac{\partial \ln K_x}{\partial P}\right)_T = -\frac{1}{R T} \left(\frac{\partial \Delta_r G^\circ(T, P)}{\partial P}\right)_T \tag{6}$$

From the fundamental differential of Gibbs free energy $dG = V dP - S dT$:
$$\left(\frac{\partial G}{\partial P}\right)_T = V \implies \left(\frac{\partial \mu_i^\circ}{\partial P}\right)_T = V_{m,i}^\circ$$
where $V_{m,i}^\circ$ is the standard partial molar volume of species $i$.
Applying this to the reaction Gibbs energy:
$$\left(\frac{\partial \Delta_r G^\circ}{\partial P}\right)_T = \sum_i \nu_i \left(\frac{\partial \mu_i^\circ}{\partial P}\right)_T = \sum_i \nu_i V_{m,i}^\circ \equiv \Delta V_{rxn}^\circ \tag{7}$$

Substitute Eq. (7) into Eq. (6):
$$\left(\frac{\partial \ln K_x}{\partial P}\right)_T = -\frac{\Delta V_{rxn}^\circ}{R T} \tag{Q.E.D.}$$

This completes the rigorous proof.
* When a reaction proceeds with a net contraction in volume ($\Delta V_{rxn}^\circ < 0$), the right-hand side is positive, proving mathematically that **compression ($P \uparrow$) unconditionally shifts equilibrium toward the more compact, lower-volume state**.
* For an ideal gas where $V_{m,i}^\circ = R T / P$:
  $$\Delta V_{rxn}^\circ = \sum \nu_i \left(\frac{R T}{P}\right) = \Delta n_g \frac{R T}{P}$$
  Substituting this into the general relation yields $-\frac{\Delta n_g (R T / P)}{R T} = -\frac{\Delta n_g}{P}$, perfectly recovering the ideal gas result as a special case."""
            }
        ]
    }
