#!/usr/bin/env python3
"""
build_kinetics_units_4_5_6.py
Builds Units 4, 5, and 6 (Sections 1-7, Solved Problems 1-7) for Molecular Motion and Reaction Kinetics.
"""

import json

def get_units_4_5_6():
    units = []

    # =========================================================================
    # UNIT 4: Empirical Chemical Kinetics & Integrated Rate Laws
    # =========================================================================
    u4 = {
        "id": "unit-4",
        "unitNumber": 4,
        "title": "Unit 4: Empirical Chemical Kinetics & Integrated Rate Laws",
        "leadSummary": "Mathematical and empirical formulation of chemical reaction rates: extent of reaction, differential rate laws, reaction order versus molecularity, analytical integration of zero, first, second, and third-order rate equations, pseudo-order approximations, fractional-life analysis, and the kinetic approach of reversible reactions toward dynamic chemical equilibrium.",
        "simulations": ["sim_kin_integrated_rate_laws"],
        "sections": [
            {
                "id": "sec-4-1",
                "secNumber": "4.1",
                "title": "Reaction Rates, Extent of Reaction & Differential Rate Formulations",
                "content": """Chemical kinetics investigates the time evolution of reacting systems and the microscopic pathways through which reactants transform into products.

### Definition of Reaction Rate and Extent of Reaction
Consider a general closed homogeneous chemical reaction with stoichiometric coefficients $\\nu_i$:
$$\\sum_i \\nu_i A_i = 0$$
where $\\nu_i < 0$ for reactants and $\\nu_i > 0$ for products.

The **extent of reaction** $\\xi$ (SI unit: moles) is defined by de Donder as:
$$d\\xi = \\frac{dn_i}{\\nu_i} \\implies n_i(t) = n_i(0) + \\nu_i \\xi(t)$$

The intensive rate of reaction $r$ (or $v$) per unit volume $V$ is defined as:
$$r = \\frac{1}{V} \\frac{d\\xi}{dt} = \\frac{1}{\\nu_i V} \\frac{dn_i}{dt}$$

For a constant-volume system, introducing concentration $c_i = [A_i] = n_i / V$:
$$r = \\frac{1}{\\nu_i} \\frac{d[A_i]}{dt}$$

For a specific reaction such as $a A + b B \\longrightarrow c C + d D$:
$$r = -\\frac{1}{a} \\frac{d[A]}{dt} = -\\frac{1}{b} \\frac{d[B]}{dt} = +\\frac{1}{c} \\frac{d[C]}{dt} = +\\frac{1}{d} \\frac{d[D]}{dt}$$
This definition guarantees that the reaction rate $r$ is a uniquely defined, positive quantity independent of which participant species is monitored."""
            },
            {
                "id": "sec-4-2",
                "secNumber": "4.2",
                "title": "Reaction Order vs. Molecularity: Empirical Rate Laws",
                "content": """A critical distinction in chemical kinetics lies between the purely empirical concept of reaction order and the theoretical concept of molecularity.

### Empirical Differential Rate Law
For many reactions far from equilibrium, the reaction rate depends on instantaneous reactant concentrations via an empirical power law:
$$r = k [A]^\\alpha [B]^\\beta [C]^\\gamma \\cdots$$
where:
- $k$ is the **rate constant** (or specific reaction rate), independent of concentration but a strong function of temperature and ionic strength.
- $\\alpha, \\beta, \\gamma$ are the **partial orders of reaction** with respect to species $A, B, C$.
- The **overall order of reaction** is $n = \\alpha + \\beta + \\gamma + \\cdots$.

**Reaction Order**:
- An experimentally determined, empirical quantity.
- Can be an integer ($0, 1, 2, 3$), a fraction ($1/2, 3/2$), or even negative.
- Does NOT necessarily bear any relation to stoichiometric coefficients $a, b, c$ unless the reaction is elementary.

**Molecularity**:
- A theoretical concept applied strictly to an **elementary reaction step**.
- Represents the exact number of reactant particles that must collide simultaneously to form the transition state.
- Strictly a positive integer: unimolecular ($1$), bimolecular ($2$), or termolecular ($3$). Quadrimolecular elementary steps have zero probability of occurrence."""
            },
            {
                "id": "sec-4-3",
                "secNumber": "4.3",
                "title": "Integrated Rate Laws: Zero-Order Reactions & Surface Heterogeneity",
                "content": """In a zero-order reaction, the rate of reaction is entirely independent of the reactant concentration.

### Differential and Integrated Equations
$$-\\frac{d[A]}{dt} = k_0$$
where $k_0$ has SI units of $\\text{mol}/(\\text{m}^3\\cdot\\text{s})$ or $\\text{M}\\cdot\\text{s}^{-1}$.

Separating variables and integrating from $t = 0$ ($[A] = [A]_0$) to time $t$:
$$\\int_{[A]_0}^{[A]} d[A] = -k_0 \\int_0^t dt$$
$$[A](t) = [A]_0 - k_0 t$$

A plot of $[A]$ versus $t$ is a straight line with slope $-k_0$ and intercept $[A]_0$.

### Half-Life ($t_{1/2}$)
The half-life $t_{1/2}$ is the time required for concentration to decrease to half its initial value ($[A] = [A]_0 / 2$):
$$\\frac{[A]_0}{2} = [A]_0 - k_0 t_{1/2} \\implies t_{1/2} = \\frac{[A]_0}{2 k_0}$$
In zero-order kinetics, the half-life is directly proportional to initial concentration $[A]_0$.

### Total Reaction Lifetime ($t_{\\text{end}}$)
The reaction terminates completely when $[A] = 0$:
$$t_{\\text{end}} = \\frac{[A]_0}{k_0} = 2 t_{1/2}$$

### Physical Occurrence in Heterogeneous Surface Catalysis
Zero-order kinetics commonly occur when a reaction takes place on a saturated solid catalyst surface or enzyme active site (e.g., decomposition of ammonia on hot tungsten, $2 NH_3 \\xrightarrow{W} N_2 + 3 H_2$). When all catalytic active sites are fully covered by adsorbed molecules (Langmuir coverage $\\theta \\approx 1$), increasing gas concentration cannot increase the reaction rate."""
            },
            {
                "id": "sec-4-4",
                "secNumber": "4.4",
                "title": "Integrated Rate Laws: First-Order Reactions & Radioactive Decay Analogy",
                "content": """First-order kinetics govern processes where the rate is directly proportional to the concentration of a single reactant.

### Differential and Integrated Equations
$$-\\frac{d[A]}{dt} = k_1 [A]$$
where $k_1$ has SI units of $\\text{s}^{-1}$ (time$^{-1}$).

Separating variables:
$$\\int_{[A]_0}^{[A]} \\frac{d[A]}{[A]} = -k_1 \\int_0^t dt$$
$$\\ln\\left( \\frac{[A]}{[A]_0} \\right) = -k_1 t \\iff [A](t) = [A]_0 \\exp(-k_1 t)$$

Linearized form:
$$\\ln[A] = \\ln[A]_0 - k_1 t$$
A plot of $\\ln[A]$ versus $t$ yields a straight line with slope $-k_1$.

### Concentration of Product ($P$)
For $A \\longrightarrow P$, with $[P]_0 = 0$:
$$[P](t) = [A]_0 - [A](t) = [A]_0 \\left( 1 - e^{-k_1 t} \\right)$$

### Half-Life ($t_{1/2}$)
At $t = t_{1/2}$, $[A] = [A]_0 / 2$:
$$\\ln\\left( \\frac{1}{2} \\right) = -k_1 t_{1/2} \\implies t_{1/2} = \\frac{\\ln 2}{k_1} = \\frac{0.69315}{k_1}$$

**Cardinal Feature**: The half-life of a first-order process is strictly independent of the initial concentration $[A]_0$.
Successive half-lives remain constant: after $n$ half-lives, $[A] = [A]_0 / 2^n$.

### Mean Lifetime ($\\tau$)
The average lifetime of a reacting particle is the reciprocal of the first-order rate constant:
$$\\tau = \\langle t \\rangle = \\frac{\\int_0^\\infty t \\, e^{-k_1 t} dt}{\\int_0^\\infty e^{-k_1 t} dt} = \\frac{1}{k_1} = \\frac{t_{1/2}}{\\ln 2} \\approx 1.443 \\, t_{1/2}$$"""
            },
            {
                "id": "sec-4-5",
                "secNumber": "4.5",
                "title": "Integrated Rate Laws: Second-Order Reactions (Equal & Unequal Reactants)",
                "content": """Second-order reactions involve the collision of two molecules, classified into two distinct cases.

### Case 1: Single Reactant or Equal Initial Concentrations ($2 A \\to P$ or $A + B \\to P$ with $[A]_0 = [B]_0$)
$$-\\frac{d[A]}{dt} = k_2 [A]^2$$
where $k_2$ has SI units of $\\text{m}^3/(\\text{mol}\\cdot\\text{s})$ or $\\text{M}^{-1}\\text{s}^{-1}$.

Separating variables:
$$\\int_{[A]_0}^{[A]} \\frac{d[A]}{[A]^2} = -k_2 \\int_0^t dt \\implies -\\left[ \\frac{1}{[A]} - \\frac{1}{[A]_0} \\right] = -k_2 t$$
$$\\frac{1}{[A](t)} = \\frac{1}{[A]_0} + k_2 t$$

A plot of $1/[A]$ versus $t$ is linear with slope $+k_2$ and intercept $1/[A]_0$.

**Half-Life**:
$$\\frac{1}{[A]_0/2} - \\frac{1}{[A]_0} = k_2 t_{1/2} \\implies t_{1/2} = \\frac{1}{k_2 [A]_0}$$
In second-order kinetics, the half-life is inversely proportional to initial concentration. Each successive half-life doubles ($t_{1/2}, 2 t_{1/2}, 4 t_{1/2}$).

### Case 2: Unequal Initial Concentrations ($A + B \\to P$ with $[A]_0 \\neq [B]_0$)
Let $x$ be the extent of concentration reacted at time $t$: $[A] = [A]_0 - x$, $[B] = [B]_0 - x$.
$$\\frac{dx}{dt} = k_2 ([A]_0 - x)([B]_0 - x)$$

Using partial fractions:
$$\\frac{1}{([A]_0 - x)([B]_0 - x)} = \\frac{1}{[B]_0 - [A]_0} \\left( \\frac{1}{[A]_0 - x} - \\frac{1}{[B]_0 - x} \\right)$$
Integrating from $x = 0$ at $t = 0$:
$$\\frac{1}{[B]_0 - [A]_0} \\left[ \\ln\\left( \\frac{[A]_0}{[A]_0 - x} \\right) - \\ln\\left( \\frac{[B]_0}{[B]_0 - x} \\right) \\right] = k_2 t$$
$$\\frac{1}{[B]_0 - [A]_0} \\ln\\left( \\frac{[A]_0 [B]}{[B]_0 [A]} \\right) = k_2 t \\iff \\ln\\left( \\frac{[B]}{[A]} \\right) = \\ln\\left( \\frac{[B]_0}{[A]_0} \\right) + ([B]_0 - [A]_0) k_2 t$$

Plotting $\\ln([B]/[A])$ versus $t$ yields a straight line with slope $([B]_0 - [A]_0) k_2$."""
            },
            {
                "id": "sec-4-6",
                "secNumber": "4.6",
                "title": "Third-Order Kinetics, Fractional Orders & Pseudo-Molecular Regimes",
                "content": """Higher-order and non-integer kinetics emerge in complex termolecular gas reactions and catalytic systems.

### Third-Order Reactions ($3 A \\to P$)
$$-\\frac{d[A]}{dt} = k_3 [A]^3$$
where $k_3$ has SI units of $\\text{M}^{-2}\\text{s}^{-1}$.

Integrating:
$$\\int_{[A]_0}^{[A]} \\frac{d[A]}{[A]^3} = -k_3 t \\implies -\\frac{1}{2} \\left( \\frac{1}{[A]^2} - \\frac{1}{[A]_0^2} \\right) = -k_3 t$$
$$\\frac{1}{[A]^2} = \\frac{1}{[A]_0^2} + 2 k_3 t$$

Half-life for third-order kinetics:
$$t_{1/2} = \\frac{3}{2 k_3 [A]_0^2}$$
True gas-phase termolecular elementary reactions are rare due to the vanishing probability of simultaneous three-body collisions; prominent examples include gas-phase oxidation of nitric oxide ($2 NO + O_2 \\longrightarrow 2 NO_2$) and radical recombination ($H + H + M \\longrightarrow H_2 + M$).

### Fractional-Life Method for General Order $n$
For an $n$-th order reaction ($-\\frac{d[A]}{dt} = k [A]^n$, $n \\neq 1$):
$$\\frac{1}{[A]^{n-1}} = \\frac{1}{[A]_0^{n-1}} + (n - 1) k t$$
The half-life scaling is:
$$t_{1/2} = \\frac{2^{n-1} - 1}{(n - 1) k [A]_0^{n-1}} \\implies t_{1/2} \\propto [A]_0^{1 - n}$$

### Pseudo-Unimolecular Reactions (Isolation Method)
When a bimolecular reaction $A + B \\to P$ is conducted with species $B$ in overwhelming stoichiometric excess ($[B]_0 \\gg [A]_0$):
$[B](t) \\approx [B]_0 = \\text{constant}$ throughout the course of reaction.
$$-\\frac{d[A]}{dt} = k_2 [A] [B] \\approx (k_2 [B]_0) [A] = k_{\\text{obs}} [A]$$
where $k_{\\text{obs}} = k_2 [B]_0$ is the **pseudo-first-order rate constant** (units: $\\text{s}^{-1}$).
This reduces second-order mathematics to simple first-order exponential decays, forming the basis of the isolation method."""
            },
            {
                "id": "sec-4-7",
                "secNumber": "4.7",
                "title": "Reversible Reactions Approaching Equilibrium: Microscopic Reversibility",
                "content": """When the forward and reverse reactions proceed at comparable rates, the system approaches a dynamic chemical equilibrium.

### First-Order Opposing Reaction ($A \\underset{k_{-1}}{\\overset{k_1}{\\rightleftharpoons}} B$)
Let initial concentrations be $[A]_0$ and $[B]_0 = 0$. At time $t$, $[A] = [A]_0 - x$ and $[B] = x$.

The net rate of consumption of $A$ is:
$$\\frac{dx}{dt} = k_1 [A] - k_{-1} [B] = k_1 ([A]_0 - x) - k_{-1} x = k_1 [A]_0 - (k_1 + k_{-1}) x$$

At dynamic equilibrium ($t \\to \\infty$), net rate vanishes ($dx/dt = 0$):
$$k_1 [A]_{\\text{eq}} = k_{-1} [B]_{\\text{eq}} \\implies \\frac{[B]_{\\text{eq}}}{[A]_{\\text{eq}}} = \\frac{x_{\\text{eq}}}{[A]_0 - x_{\\text{eq}}} = \\frac{k_1}{k_{-1}} = K_c$$
where $K_c$ is the thermodynamic equilibrium constant. This satisfies the **Principle of Microscopic Reversibility**.

Expressing $k_1 [A]_0$ in terms of equilibrium extent:
$$k_1 [A]_0 = (k_1 + k_{-1}) x_{\\text{eq}}$$

Substituting back into the rate differential equation:
$$\\frac{dx}{dt} = (k_1 + k_{-1}) (x_{\\text{eq}} - x)$$

Separating variables and integrating:
$$\\int_0^x \\frac{dx}{x_{\\text{eq}} - x} = (k_1 + k_{-1}) \\int_0^t dt \\implies \\ln\\left( \\frac{x_{\\text{eq}}}{x_{\\text{eq}} - x} \\right) = (k_1 + k_{-1}) t$$
$$x(t) = x_{\\text{eq}} \\left[ 1 - e^{-(k_1 + k_{-1}) t} \\right]$$

In terms of reactant concentration:
$$[A](t) - [A]_{\\text{eq}} = ([A]_0 - [A]_{\\text{eq}}) \\exp\\left( -(k_1 + k_{-1}) t \\right)$$

**Key Insight**: The approach to equilibrium is a first-order exponential relaxation whose apparent rate constant is the **sum** of forward and backward rate constants ($k_{\\text{obs}} = k_1 + k_{-1}$).
Measuring $k_{\\text{obs}}$ along with the equilibrium ratio $K_c = k_1 / k_{-1}$ allows exact evaluation of both individual rate constants."""
            }
        ],
        "problems": [
            {
                "id": "p4-1",
                "title": "First-Order Hydrolysis Kinetics and Half-Life Evaluation",
                "difficulty": "Easy",
                "statement": "The thermal decomposition of dinitrogen pentoxide ($2 N_2O_5(g) \\longrightarrow 4 NO_2(g) + O_2(g)$) in carbon tetrachloride is first-order with a rate constant $k_1 = 6.20 \\times 10^{-4}\\text{ s}^{-1}$ at $45.0^\\circ\\text{C}$. Calculate: (a) the half-life $t_{1/2}$, (b) the time required for $90.0\\%$ of the $N_2O_5$ to decompose, and (c) the fraction remaining after $t = 30.0\\text{ minutes}$.",
                "solution": """**Step 1: Calculate half-life**
$$t_{1/2} = \\frac{\\ln 2}{k_1} = \\frac{0.693147}{6.20 \\times 10^{-4}\\text{ s}^{-1}} = 1117.98\\text{ s} = 18.63\\text{ minutes}$$

**Step 2: Time for $90.0\\%$ decomposition**
When $90.0\\%$ has decomposed, the fraction remaining is:
$$\\frac{[A]}{[A]_0} = 1.00 - 0.900 = 0.100$$
Using the integrated first-order rate law:
$$\\ln\\left( \\frac{[A]}{[A]_0} \\right) = -k_1 t$$
$$t = -\\frac{\\ln(0.100)}{k_1} = \\frac{2.302585}{6.20 \\times 10^{-4}\\text{ s}^{-1}} = 3713.8\\text{ s} = 61.90\\text{ minutes}$$

**Step 3: Fraction remaining after $30.0\\text{ minutes}$**
$$t = 30.0 \\times 60 = 1800\\text{ s}$$
$$k_1 t = (6.20 \\times 10^{-4}\\text{ s}^{-1}) \\times (1800\\text{ s}) = 1.116$$
$$\\frac{[A]}{[A]_0} = \\exp(-1.116) = 0.3276 = 32.76\\%$$
After 30 minutes, $32.8\\%$ of the original $N_2O_5$ remains unreacted."""
            },
            {
                "id": "p4-2",
                "title": "Second-Order Saponification Rate Constant Determination",
                "difficulty": "Medium",
                "statement": "The alkaline saponification of ethyl acetate ($CH_3COOC_2H_5 + NaOH \\longrightarrow CH_3COONa + C_2H_5OH$) is second-order overall. In an experiment at $25.0^\\circ\\text{C}$, initial concentrations of both ester and sodium hydroxide were equal at $[A]_0 = [B]_0 = 0.0500\\text{ M}$. After $t = 15.0\\text{ minutes}$, the remaining concentration of $NaOH$ was titrated to be $0.0180\\text{ M}$. Calculate: (a) the second-order rate constant $k_2$ in $\\text{M}^{-1}\\text{s}^{-1}$, and (b) the half-life $t_{1/2}$.",
                "solution": """**Step 1: Integrated second-order equation with equal initial concentrations**
$$\\frac{1}{[A]} - \\frac{1}{[A]_0} = k_2 t$$
where $[A]_0 = 0.0500\\text{ M}$ and $[A] = 0.0180\\text{ M}$.
$$t = 15.0 \\times 60 = 900.0\\text{ s}$$

$$\\frac{1}{0.0180} - \\frac{1}{0.0500} = 55.5556 - 20.0000 = 35.5556\\text{ M}^{-1}$$
$$k_2 = \\frac{35.5556\\text{ M}^{-1}}{900.0\\text{ s}} = 0.039506\\text{ M}^{-1}\\text{s}^{-1} = 0.0395\\text{ L}/(\\text{mol}\\cdot\\text{s})$$

**Step 2: Half-life calculation**
$$t_{1/2} = \\frac{1}{k_2 [A]_0} = \\frac{1}{0.039506 \\times 0.0500} = \\frac{1}{1.9753 \\times 10^{-3}} = 506.26\\text{ s} = 8.44\\text{ minutes}$$"""
            },
            {
                "id": "p4-3",
                "title": "Second-Order Reaction with Unequal Initial Reactant Concentrations",
                "difficulty": "Hard",
                "statement": "The reaction $A + B \\longrightarrow P$ is first order with respect to $A$ and first order with respect to $B$ ($r = k_2 [A][B]$). The initial concentrations are $[A]_0 = 0.0400\\text{ M}$ and $[B]_0 = 0.0800\\text{ M}$. The second-order rate constant is $k_2 = 0.0750\\text{ M}^{-1}\\text{s}^{-1}$. Calculate: (a) the concentrations of $A$ and $B$ after $t = 300.0\\text{ s}$, and (b) the time required for $80.0\\%$ of reactant $A$ to be consumed.",
                "solution": """**Step 1: Evaluate integrated form for $[A]_0 \\neq [B]_0$**
$$\\ln\\left( \\frac{[B]}{[A]} \\right) = \\ln\\left( \\frac{[B]_0}{[A]_0} \\right) + ([B]_0 - [A]_0) k_2 t$$
$$[B]_0 - [A]_0 = 0.0800 - 0.0400 = 0.0400\\text{ M}$$
$$\\frac{[B]_0}{[A]_0} = \\frac{0.0800}{0.0400} = 2.000 \\implies \\ln(2.000) = 0.69315$$

At $t = 300.0\\text{ s}$:
$$([B]_0 - [A]_0) k_2 t = (0.0400\\text{ M}) \\times (0.0750\\text{ M}^{-1}\\text{s}^{-1}) \\times (300.0\\text{ s}) = 0.9000$$
$$\\ln\\left( \\frac{[B]}{[A]} \\right) = 0.69315 + 0.9000 = 1.59315$$
$$\\frac{[B]}{[A]} = \\exp(1.59315) = 4.9192$$

**Step 2: Relate $[B]$ and $[A]$ by stoichiometry**
Let $x$ be the reacted concentration: $[A] = 0.0400 - x$, $[B] = 0.0800 - x = [A] + 0.0400$.
$$\\frac{[A] + 0.0400}{[A]} = 4.9192 \\implies 1 + \\frac{0.0400}{[A]} = 4.9192$$
$$\\frac{0.0400}{[A]} = 3.9192 \\implies [A] = \\frac{0.0400}{3.9192} = 0.01021\\text{ M}$$
$$[B] = [A] + 0.0400 = 0.05021\\text{ M}$$

**Step 3: Time for $80.0\\%$ conversion of $A$**
When $80.0\\%$ of $A$ is consumed:
$$[A] = (1 - 0.800) \\times 0.0400 = 0.00800\\text{ M}$$
$$x = 0.03200\\text{ M}$$
$$[B] = 0.0800 - 0.0320 = 0.04800\\text{ M}$$
$$\\frac{[B]}{[A]} = \\frac{0.04800}{0.00800} = 6.000$$

Using the integrated rate law:
$$\\ln(6.000) = \\ln(2.000) + (0.0400 \\times 0.0750) t$$
$$1.79176 = 0.69315 + 0.00300 \\, t$$
$$0.00300 \\, t = 1.09861 \\implies t = \\frac{1.09861}{0.00300} = 366.2\\text{ s} = 6.10\\text{ minutes}$$"""
            },
            {
                "id": "p4-4",
                "title": "Reaction Order Determination via Fractional-Life Method",
                "difficulty": "Medium",
                "statement": "In a kinetic study of the decomposition of an organic peroxide, the measured half-life $t_{1/2}$ varied with initial concentration $[A]_0$ as follows: at $[A]_0 = 0.0200\\text{ M}$, $t_{1/2} = 245.0\\text{ s}$; at $[A]_0 = 0.0800\\text{ M}$, $t_{1/2} = 61.25\\text{ s}$. Determine: (a) the overall reaction order $n$, and (b) the rate constant $k$.",
                "solution": """**Step 1: Fractional-life scaling relation**
For reaction order $n$:
$$t_{1/2} \\propto [A]_0^{1 - n} \\implies \\frac{t_{1/2, 1}}{t_{1/2, 2}} = \\left( \\frac{[A]_{0, 1}}{[A]_{0, 2}} \\right)^{1 - n}$$

Substituting experimental values:
$$\\frac{245.0}{61.25} = 4.000$$
$$\\frac{[A]_{0, 1}}{[A]_{0, 2}} = \\frac{0.0200}{0.0800} = 0.250 = \\frac{1}{4}$$

Thus:
$$4.000 = \\left( \\frac{1}{4} \\right)^{1 - n} = 4^{n - 1}$$
Taking logarithms:
$$\\ln(4.000) = (n - 1) \\ln(4) \\implies n - 1 = 1 \\implies n = 2$$
The reaction is strictly **second-order** ($n = 2$).

**Step 2: Evaluate the second-order rate constant $k_2$**
For $n = 2$:
$$t_{1/2} = \\frac{1}{k_2 [A]_0} \\implies k_2 = \\frac{1}{t_{1/2} [A]_0}$$

Using condition 1:
$$k_2 = \\frac{1}{245.0\\text{ s} \\times 0.0200\\text{ M}} = \\frac{1}{4.900} = 0.2041\\text{ M}^{-1}\\text{s}^{-1}$$

Using condition 2 to verify:
$$k_2 = \\frac{1}{61.25\\text{ s} \\times 0.0800\\text{ M}} = \\frac{1}{4.900} = 0.2041\\text{ M}^{-1}\\text{s}^{-1}$$"""
            },
            {
                "id": "p4-5",
                "title": "Pseudo-First-Order Saponification by Reactant Isolation",
                "difficulty": "Easy",
                "statement": "The ester hydrolysis reaction $RCOOR' + H_2O \\xrightarrow{H^+} RCOOH + R'OH$ has a true second-order rate constant of $k_2 = 1.85 \\times 10^{-4}\\text{ M}^{-1}\\text{s}^{-1}$. In dilute aqueous solution, water is the solvent with concentration $[H_2O] = 55.5\\text{ M}$. (a) Calculate the pseudo-first-order rate constant $k_{\\text{obs}}$, and (b) calculate the time required for $50.0\\%$ and $99.0\\%$ of the ester to hydrolyze.",
                "solution": """**Step 1: Calculate pseudo-first-order rate constant**
Because $[H_2O] = 55.5\\text{ M} \\gg [\\text{ester}]_0 \\sim 0.01\\text{ M}$, $[H_2O]$ remains virtually constant:
$$k_{\\text{obs}} = k_2 [H_2O] = (1.85 \\times 10^{-4}\\text{ M}^{-1}\\text{s}^{-1}) \\times (55.5\\text{ M}) = 1.02675 \\times 10^{-2}\\text{ s}^{-1}$$

**Step 2: Half-life ($50.0\\%$ conversion)**
$$t_{1/2} = \\frac{\\ln 2}{k_{\\text{obs}}} = \\frac{0.693147}{1.02675 \\times 10^{-2}\\text{ s}^{-1}} = 67.51\\text{ s}$$

**Step 3: Time for $99.0\\%$ conversion**
$$\\frac{[A]}{[A]_0} = 1 - 0.990 = 0.0100$$
$$t = -\\frac{\\ln(0.0100)}{k_{\\text{obs}}} = \\frac{4.60517}{1.02675 \\times 10^{-2}\\text{ s}^{-1}} = 448.52\\text{ s} = 7.48\\text{ minutes}$$"""
            },
            {
                "id": "p4-6",
                "title": "First-Order Reversible Kinetics Approaching Dynamic Equilibrium",
                "difficulty": "Hard",
                "statement": "The isomerization of cis-stilbene ($A$) to trans-stilbene ($B$) ($A \\underset{k_{-1}}{\\overset{k_1}{\\rightleftharpoons}} B$) is reversible and first-order in both directions. Starting with pure cis-stilbene at $[A]_0 = 0.150\\text{ M}$, the equilibrium concentration of cis-isomer is $[A]_{\\text{eq}} = 0.0300\\text{ M}$. The time required for $[A]$ to reach $0.0900\\text{ M}$ is $t = 120.0\\text{ s}$. Calculate: (a) the equilibrium constant $K_c$, (b) the relaxation sum $(k_1 + k_{-1})$, and (c) the individual rate constants $k_1$ and $k_{-1}$.",
                "solution": """**Step 1: Determine equilibrium constant $K_c$**
At equilibrium:
$$[B]_{\\text{eq}} = [A]_0 - [A]_{\\text{eq}} = 0.150 - 0.0300 = 0.120\\text{ M}$$
$$K_c = \\frac{[B]_{\\text{eq}}}{[A]_{\\text{eq}}} = \\frac{0.120\\text{ M}}{0.0300\\text{ M}} = 4.000$$
Therefore:
$$k_1 = 4.000 \\, k_{-1}$$

**Step 2: Integrated reversible rate law**
$$[A](t) - [A]_{\\text{eq}} = ([A]_0 - [A]_{\\text{eq}}) \\exp\\left( -(k_1 + k_{-1}) t \\right)$$
$$\\frac{[A](t) - [A]_{\\text{eq}}}{[A]_0 - [A]_{\\text{eq}}} = \\exp\\left( -(k_1 + k_{-1}) t \\right)$$

Substitute given concentrations at $t = 120.0\\text{ s}$:
$$[A](t) - [A]_{\\text{eq}} = 0.0900 - 0.0300 = 0.0600\\text{ M}$$
$$[A]_0 - [A]_{\\text{eq}} = 0.150 - 0.0300 = 0.120\\text{ M}$$
$$\\frac{0.0600}{0.120} = 0.5000 = \\exp\\left( -(k_1 + k_{-1}) \\times 120.0 \\right)$$

Taking logarithms:
$$-(k_1 + k_{-1}) \\times 120.0 = \\ln(0.5000) = -0.69315$$
$$k_1 + k_{-1} = \\frac{0.69315}{120.0} = 5.77625 \\times 10^{-3}\\text{ s}^{-1}$$

**Step 3: Solve for individual rate constants**
Substitute $k_1 = 4.000 \\, k_{-1}$:
$$4.000 \\, k_{-1} + k_{-1} = 5.000 \\, k_{-1} = 5.77625 \\times 10^{-3}\\text{ s}^{-1}$$
$$k_{-1} = \\frac{5.77625 \\times 10^{-3}}{5.000} = 1.155 \\times 10^{-3}\\text{ s}^{-1}$$
$$k_1 = 4.000 \\times (1.155 \\times 10^{-3}) = 4.621 \\times 10^{-3}\\text{ s}^{-1}$$"""
            },
            {
                "id": "p4-7",
                "title": "Gas-Phase Termolecular Nitric Oxide Oxidation Kinetics",
                "difficulty": "Hard",
                "statement": "The homogeneous gas-phase oxidation of nitric oxide ($2 NO + O_2 \\longrightarrow 2 NO_2$) follows the rate law $r = k_3 [NO]^2 [O_2]$. At $T = 300.0\\text{ K}$, initial partial pressures are $P_{NO} = 20.0\\text{ Torr}$ and $P_{O_2} = 10.0\\text{ Torr}$. The rate constant in pressure units is $k_p = 3.50 \\times 10^{-3}\\text{ Torr}^{-2}\\text{s}^{-1}$. (a) Calculate the initial rate of pressure decrease in $\\text{Torr/s}$, and (b) convert $k_p$ into concentration units $k_c$ in $\\text{M}^{-2}\\text{s}^{-1}$.",
                "solution": """**Step 1: Initial rate of reaction in pressure units**
The reaction rate is:
$$r_p = -\\frac{d P_{O_2}}{dt} = -\\frac{1}{2} \\frac{d P_{NO}}{dt} = k_p P_{NO}^2 P_{O_2}$$
$$r_p = (3.50 \\times 10^{-3}\\text{ Torr}^{-2}\\text{s}^{-1}) \\times (20.0\\text{ Torr})^2 \\times (10.0\\text{ Torr})$$
$$r_p = (3.50 \\times 10^{-3}) \\times (400.0) \\times (10.0) = 14.00\\text{ Torr/s}$$

Total pressure rate of change:
$$P_{\\text{tot}} = P_{NO} + P_{O_2} + P_{NO_2}$$
$$\\Delta P_{\\text{tot}} = \\Delta n = 2 - (2 + 1) = -1\\text{ mole per extent}$$
$$\\frac{d P_{\\text{tot}}}{dt} = -r_p = -14.00\\text{ Torr/s}$$

**Step 2: Conversion of $k_p$ to concentration units $k_c$**
Using ideal gas law $P_i = c_i R T$:
$$r = -\\frac{d c_{O_2}}{dt} = -\\frac{1}{R T} \\frac{d P_{O_2}}{dt} = \\frac{1}{R T} k_p P_{NO}^2 P_{O_2} = \\frac{k_p}{R T} (c_{NO} R T)^2 (c_{O_2} R T)$$
$$r = k_p (R T)^2 [NO]^2 [O_2] = k_c [NO]^2 [O_2]$$
Therefore:
$$k_c = k_p (R T)^2$$

In SI / standard laboratory units:
$$R = 0.0820574\\text{ L}\\cdot\\text{atm}/(\\text{mol}\\cdot\\text{K}) = 62.3637\\text{ L}\\cdot\\text{Torr}/(\\text{mol}\\cdot\\text{K})$$
$$R T = 62.3637 \\times 300.0 = 1.87091 \\times 10^4\\text{ L}\\cdot\\text{Torr/mol}$$
$$(R T)^2 = (1.87091 \\times 10^4)^2 = 3.5003 \\times 10^8\\text{ L}^2\\cdot\\text{Torr}^2\\text{/mol}^2$$

$$k_c = (3.50 \\times 10^{-3}\\text{ Torr}^{-2}\\text{s}^{-1}) \\times (3.5003 \\times 10^8\\text{ L}^2\\cdot\\text{Torr}^2\\text{/mol}^2) = 1.225 \\times 10^6\\text{ L}^2/(\\text{mol}^2\\cdot\\text{s}) = 1.225 \\times 10^6\\text{ M}^{-2}\\text{s}^{-1}$$"""
            }
        ]
    }
    units.append(u4)

    # =========================================================================
    # UNIT 5: Temperature Dependence, Arrhenius Theory & Composite Kinetics
    # =========================================================================
    u5 = {
        "id": "unit-5",
        "unitNumber": 5,
        "title": "Unit 5: Temperature Dependence, Arrhenius Theory & Composite Kinetics",
        "leadSummary": "Thermodynamic and statistical mechanics of reaction rate temperature dependence: empirical determination of reaction orders, van 't Hoff's transition to Arrhenius theory, differential and integrated Arrhenius forms, physical significance of the pre-exponential frequency factor and activation energy, Tolman's statistical mechanical interpretation, composite reaction activation barriers, and non-Arrhenius curvature.",
        "simulations": ["sim_kin_arrhenius_activation_energy"],
        "sections": [
            {
                "id": "sec-5-1",
                "secNumber": "5.1",
                "title": "Empirical Determination of Reaction Orders: Classical Kinetic Methods",
                "content": """Determining the empirical order of a reaction is the vital first step toward elucidating its molecular mechanism. Four classical experimental protocols are employed.

### 1. The Method of Initial Rates
By measuring the initial rate $r_0 = (d[P]/dt)_{t \\to 0}$ before back-reactions, product inhibition, or substantial reactant depletion occur:
$$r_0 = k [A]_0^\\alpha [B]_0^\\beta$$
Varying $[A]_0$ while holding $[B]_0$ constant:
$$\\frac{r_{0, 1}}{r_{0, 2}} = \\left( \\frac{[A]_{0, 1}}{[A]_{0, 2}} \\right)^\\alpha \\implies \\alpha = \\frac{\\ln(r_{0, 1} / r_{0, 2})}{\\ln([A]_{0, 1} / [A]_{0, 2})}$$

### 2. The Isolation Method (Flooding)
All reactants except one are supplied in massive stoichiometric excess ($[B]_0, [C]_0 \\gg [A]_0$). Their concentrations remain virtually constant throughout the reaction:
$$r = k [A]^\\alpha [B]_0^\\beta [C]_0^\\gamma = k_{\\text{eff}} [A]^\\alpha$$
where $k_{\\text{eff}} = k [B]_0^\\beta [C]_0^\\gamma$. The partial order $\\alpha$ is then determined directly using standard integrated rate plots for species $A$. Repeating by flooding different components yields all partial orders.

### 3. The Fractional-Life Method
Measuring the time $t_{f}$ required for concentration to decrease by a fixed fraction $f$ (e.g., $f = 1/2$ for half-life, $f = 3/4$):
$$t_{f} \\propto \\frac{1}{[A]_0^{n - 1}} \\implies \\ln t_{f} = \\text{constant} - (n - 1) \\ln[A]_0$$
Plotting $\\ln t_{1/2}$ versus $\\ln[A]_0$ yields a straight line with slope $1 - n$.

### 4. Differential (van 't Hoff) Method
Directly taking natural logarithms of the differential rate equation:
$$\\ln r = \\ln k + \\alpha \\ln[A] + \\beta \\ln[B]$$
A plot of $\\ln r$ versus $\\ln[A]$ gives slope $\\alpha$."""
            },
            {
                "id": "sec-5-2",
                "secNumber": "5.2",
                "title": "Temperature Dependence of Reaction Rates: Historical Foundation",
                "content": """Chemical reaction rates are extraordinarily sensitive to temperature. As an approximate historical rule of thumb (the van 't Hoff rule), the rate of a typical homogeneous chemical reaction approximately doubles or triples for every $10^\\circ\\text{C}$ temperature rise ($Q_{10} \\approx 2\\text{--}3$).

### Contrast with Kinetic Molecular Theory
From the kinetic theory of gases, the average molecular speed scales as:
$$\\bar{v} \\propto \\sqrt{T}$$
and the binary collision frequency scales as:
$$Z_{AA} \\propto \\sqrt{T}$$

For a $10^\\circ\\text{C}$ rise from $300\\text{ K}$ to $310\\text{ K}$:
$$\\frac{Z(310\\text{ K})}{Z(300\\text{ K})} = \\sqrt{\\frac{310}{300}} = \\sqrt{1.0333} \\approx 1.0165$$
The collision frequency increases by a mere **$1.65\\%$**. 

This colossal discrepancy between a $1.65\\%$ increase in molecular collisions and a $200\\%\\text{--}300\\%$ increase in chemical reaction rate proved conclusively that only an extraordinarily small, highly energetic fraction of molecular collisions possess sufficient energy to overcome a critical barrier and undergo chemical rearrangement."""
            },
            {
                "id": "sec-5-3",
                "secNumber": "5.3",
                "title": "The Arrhenius Rate Equation: Differential & Integrated Formulations",
                "content": """In 1889, the Swedish chemist Svante Arrhenius synthesized J.H. van 't Hoff's thermodynamic equilibrium equation with Boltzmann's energy distribution to propose the foundational law of chemical kinetics.

### Analogy to the van 't Hoff Isochore
van 't Hoff's thermodynamic relation for the temperature dependence of the equilibrium constant $K = k_1 / k_{-1}$ is:
$$\\frac{d \\ln K}{dT} = \\frac{d \\ln k_1}{dT} - \\frac{d \\ln k_{-1}}{dT} = \\frac{\\Delta U^\\circ}{R T^2}$$

Arrhenius proposed that each individual rate constant satisfies a similar differential equation:
$$\\frac{d \\ln k}{dT} = \\frac{E_a}{R T^2}$$
where $E_a$ is the **empirical activation energy** (SI unit: $\\text{J/mol}$ or $\\text{kJ/mol}$).

### Integrated Forms of the Arrhenius Equation
Assuming $E_a$ is independent of temperature over moderate intervals, indefinite integration yields:
$$\\ln k = -\\frac{E_a}{R T} + \\ln A \\iff k(T) = A \\exp\\left( -\\frac{E_a}{R T} \\right)$$
where:
- $A$ is the **pre-exponential factor** (or frequency factor), possessing the same units as the rate constant $k$.
- $\\exp(-E_a / R T)$ is the **Boltzmann fraction** of collisions with energy exceeding $E_a$.

### Two-Temperature Comparative Form
Integrating between temperatures $T_1$ and $T_2$:
$$\\ln\\left( \\frac{k(T_2)}{k(T_1)} \\right) = -\\frac{E_a}{R} \\left( \\frac{1}{T_2} - \\frac{1}{T_1} \\right) = \\frac{E_a}{R} \\left( \\frac{T_2 - T_1}{T_1 T_2} \\right)$$

### Arrhenius Plot Linearization
Plotting $\\ln k$ versus $1/T$ (in $\\text{K}^{-1}$):
- Slope $= -\\frac{E_a}{R}$
- $y$-intercept $= \\ln A$"""
            },
            {
                "id": "sec-5-4",
                "secNumber": "5.4",
                "title": "Physical Significance of the Pre-Exponential Factor & Activation Barrier",
                "content": """The parameters $A$ and $E_a$ provide complementary microscopic insights into the reaction coordinate.

### The Activation Energy ($E_a$)
The activation energy $E_a$ represents the minimum threshold energy colliding reactant molecules must possess along the line-of-centers (reaction coordinate) to induce bond distortion, overcome Coulombic electron repulsion, and reach the top of the potential energy barrier (the activated transition state complex).

Key energetic features:
- Reactions with low activation energies ($E_a < 20\\text{ kJ/mol}$, such as radical-radical recombinations) proceed extremely rapidly and exhibit weak temperature sensitivity.
- Reactions with high activation energies ($E_a > 150\\text{ kJ/mol}$, such as thermal cracking of alkanes) are slow at ambient temperature and exhibit extreme exponential acceleration with temperature.
- $E_a$ is always positive for elementary thermal reactions. (Certain composite reactions exhibit apparent negative activation energies, as analyzed in Section 5.6).

### The Pre-Exponential Factor ($A$)
The pre-exponential factor $A$ quantifies the frequency of collisions with favorable spatial geometry:
$$A = P \\cdot Z_0$$
where:
- $Z_0$ is the total binary collision frequency at unit concentration.
- $P$ is the **steric factor** (orientation probability), which accounts for the requirement that molecules collide with specific mutual orientations.

For simple gas-phase atom-atom or spherical collisions, $P \\sim 1$ and $A \\sim 10^{11}\\text{ M}^{-1}\\text{s}^{-1}$. For complex polyatomic molecules requiring precise alignment of functional groups, $P$ can be as small as $10^{-4}$ to $10^{-8}$, dramatically reducing the effective rate constant."""
            },
            {
                "id": "sec-5-5",
                "secNumber": "5.5",
                "title": "Tolman's Statistical Thermodynamic Interpretation of Activation Energy",
                "content": """In 1920, Richard Chace Tolman provided the rigorous statistical mechanical definition of activation energy, establishing that $E_a$ is the difference between the average energy of reactive collisions and the average energy of all collisions.

### Tolman's Theorem
Let $\\sigma_R(E)$ be the microscopic reaction cross-section for collisions with center-of-mass collision energy $E$.
The macroscopic bimolecular rate constant is given by the statistical ensemble thermal average:
$$k(T) = \\left( \\frac{8}{\\pi \\mu (k_B T)^3} \\right)^{1/2} \\int_0^\\infty E \\, \\sigma_R(E) \\exp\\left( -\\frac{E}{k_B T} \\right) dE$$
where $\\mu = \\frac{m_A m_B}{m_A + m_B}$ is the reduced mass.

Taking the logarithmic temperature derivative:
$$\\frac{d \\ln k}{dT} = \\frac{1}{k} \\frac{dk}{dT}$$
Evaluating the derivative inside the integral yields **Tolman's Principle**:
$$E_a \\equiv R T^2 \\frac{d \\ln k}{dT} = \\langle E_R \\rangle - \\langle E_{\\text{all}} \\rangle$$
where:
- $\\langle E_R \\rangle$ is the average energy of all collisions that successfully result in chemical reaction.
- $\\langle E_{\\text{all}} \\rangle$ is the average energy of all collisions in the thermal ensemble ($= \\frac{3}{2} R T$ for translational motion).

Tolman's theorem proves that the empirical Arrhenius activation energy $E_a$ is precisely the **energy excess** that reactive molecular encounters carry above the thermal average of the bulk reactant population."""
            },
            {
                "id": "sec-5-6",
                "secNumber": "5.6",
                "title": "Composite Reaction Kinetics & Apparent Activation Energies",
                "content": """When a chemical transformation proceeds via a multi-step composite mechanism, the overall observed rate constant $k_{\\text{obs}}$ is an algebraic combination of elementary rate constants, and the apparent activation energy $E_{a, \\text{app}}$ is a composite sum.

### Pre-Equilibrium Followed by Slow Elementary Step
Consider the mechanism:
$$A + B \\underset{k_{-1}}{\\overset{k_1}{\\rightleftharpoons}} [AB]^* \\quad (\\text{fast pre-equilibrium})$$
$$[AB]^* \\xrightarrow{k_2} P \\quad (\\text{slow rate-determining step})$$

The observed rate law is:
$$r = k_2 [[AB]^*] = k_2 K_1 [A][B] = \\left( \\frac{k_1 k_2}{k_{-1}} \\right) [A][B]$$
Thus, the overall observed rate constant is:
$$k_{\\text{obs}} = \\frac{k_1 k_2}{k_{-1}}$$

Taking natural logarithms:
$$\\ln k_{\\text{obs}} = \\ln k_1 + \\ln k_2 - \\ln k_{-1}$$
Differentiating with respect to temperature:
$$\\frac{d \\ln k_{\\text{obs}}}{dT} = \\frac{d \\ln k_1}{dT} + \\frac{d \\ln k_2}{dT} - \\frac{d \\ln k_{-1}}{dT}$$
Multiplying by $R T^2$:
$$E_{a, \\text{app}} = E_{a, 1} + E_{a, 2} - E_{a, -1} = E_{a, 2} + \\Delta H_1^\\circ$$
where $\\Delta H_1^\\circ = E_{a, 1} - E_{a, -1}$ is the standard enthalpy of formation of the intermediate pre-equilibrium complex.

### Apparent Negative Activation Energies
If the initial pre-equilibrium step is strongly exothermic ($\\Delta H_1^\\circ < 0$) and its magnitude exceeds the activation energy of the decomposition step:
$$|\\Delta H_1^\\circ| > E_{a, 2} \\implies E_{a, \\text{app}} < 0$$
When $E_{a, \\text{app}} < 0$, the reaction rate **slows down** as temperature increases!
Famous example: gas-phase termolecular oxidation of nitric oxide ($2 NO + O_2 \\longrightarrow 2 NO_2$), where pre-equilibrium dimerization $2 NO \\rightleftharpoons N_2O_2$ is exothermic ($\\Delta H^\\circ \\approx -10.5\\text{ kJ/mol}$), yielding $E_{a, \\text{app}} \\approx -4\\text{ kJ/mol}$."""
            },
            {
                "id": "sec-5-7",
                "secNumber": "5.7",
                "title": "Non-Arrhenius Curvature: Super-Arrhenius Behavior & Quantum Tunneling",
                "content": """While the classical Arrhenius equation is exceptionally robust over moderate temperature spans, significant non-linear curvature in $\\ln k$ versus $1/T$ plots emerges across broad temperature regimes.

### 1. Temperature-Dependent Pre-Exponential Factor (Modified Arrhenius Equation)
Collision theory and Transition State Theory demonstrate that the pre-exponential factor is not strictly constant, but varies mildly with temperature:
$$k(T) = A' T^m \\exp\\left( -\\frac{E_0}{R T} \\right)$$
where:
- $m = 1/2$ from hard-sphere collision theory ($A \\propto \\bar{v} \\propto T^{1/2}$).
- $m = 1$ from classical Eyring transition state theory ($k_B T / h$).
- $m$ can be negative or higher integer depending on partition functions.

The true activation energy becomes temperature-dependent:
$$E_a(T) = R T^2 \\frac{d \\ln k}{dT} = R T^2 \\left( \\frac{m}{T} + \\frac{E_0}{R T^2} \\right) = E_0 + m R T$$

### 2. Low-Temperature Quantum Mechanical Tunneling
For reactions involving the transfer of light particles (protons $H^+$, hydrogen atoms $H^\\bullet$, or electrons $e^-$), the de Broglie wavelength $\\lambda_{\\text{dB}} = h / \\sqrt{2 m E}$ is comparable to the activation barrier width ($d \\approx 0.5\\text{--}1.0\\text{ Å}$).

At low temperatures ($T < 200\\text{ K}$), particles tunnel through the barrier rather than climbing over it. As $T \\to 0\\text{ K}$, the reaction rate flattens to a temperature-independent non-zero constant ($k \\to k_{\\text{tunnel}}$), causing the Arrhenius plot to curve upward with $E_a \\to 0$.

### 3. Super-Arrhenius Behavior in Glassy and Viscous Media
In supercooled liquids and polymer glass transitions, relaxation rates decelerate far faster than Arrhenius predictions, described by the **Vogel-Fulcher-Tammann (VFT) equation**:
$$k(T) = A \\exp\\left( -\\frac{B}{T - T_0} \\right)$$
reflecting cooperative molecular rearrangements as free volume collapses near the ideal glass transition temperature $T_0$."""
            }
        ],
        "problems": [
            {
                "id": "p5-1",
                "title": "Arrhenius Activation Energy and Frequency Factor from Two-Point Rate Data",
                "difficulty": "Easy",
                "statement": "The first-order gas-phase decomposition of acetaldehyde ($CH_3CHO \\longrightarrow CH_4 + CO$) has measured rate constants of $k_1 = 1.05 \\times 10^{-5}\\text{ s}^{-1}$ at $T_1 = 700.0\\text{ K}$ and $k_2 = 2.14 \\times 10^{-3}\\text{ s}^{-1}$ at $T_2 = 800.0\\text{ K}$. Calculate: (a) the activation energy $E_a$ in $\\text{kJ/mol}$, (b) the pre-exponential factor $A$, and (c) the predicted rate constant at $T_3 = 750.0\\text{ K}$.",
                "solution": """**Step 1: Calculate activation energy $E_a$**
Using the two-temperature Arrhenius equation:
$$\\ln\\left( \\frac{k_2}{k_1} \\right) = \\frac{E_a}{R} \\left( \\frac{T_2 - T_1}{T_1 T_2} \\right)$$

$$\\frac{k_2}{k_1} = \\frac{2.14 \\times 10^{-3}}{1.05 \\times 10^{-5}} = 203.81$$
$$\\ln(203.81) = 5.31721$$

$$\\frac{T_2 - T_1}{T_1 T_2} = \\frac{800.0 - 700.0}{700.0 \\times 800.0} = \\frac{100.0}{5.600 \\times 10^5} = 1.78571 \\times 10^{-4}\\text{ K}^{-1}$$

$$E_a = \\frac{R \\ln(k_2 / k_1)}{(T_2 - T_1)/(T_1 T_2)} = \\frac{8.314462 \\times 5.31721}{1.78571 \\times 10^{-4}} = \\frac{44.2097}{1.78571 \\times 10^{-4}} = 2.47575 \\times 10^5\\text{ J/mol} = 247.6\\text{ kJ/mol}$$

**Step 2: Calculate pre-exponential factor $A$**
Using data at $T_1 = 700.0\\text{ K}$:
$$k_1 = A \\exp\\left( -\\frac{E_a}{R T_1} \\right) \\implies A = k_1 \\exp\\left( \\frac{E_a}{R T_1} \\right)$$
$$\\frac{E_a}{R T_1} = \\frac{247575}{8.314462 \\times 700.0} = \\frac{247575}{5820.12} = 42.5378$$
$$\\exp(42.5378) = 2.9790 \\times 10^{18}$$
$$A = (1.05 \\times 10^{-5}\\text{ s}^{-1}) \\times (2.9790 \\times 10^{18}) = 3.128 \\times 10^{13}\\text{ s}^{-1}$$

**Step 3: Predicted rate constant at $T_3 = 750.0\\text{ K}$**
$$\\frac{E_a}{R T_3} = \\frac{247575}{8.314462 \\times 750.0} = \\frac{247575}{6235.85} = 39.7019$$
$$k(750\\text{ K}) = A \\exp(-39.7019) = (3.128 \\times 10^{13}) \\times (5.723 \\times 10^{-18}) = 1.79 \\times 10^{-4}\\text{ s}^{-1}$$"""
            },
            {
                "id": "p5-2",
                "title": "Method of Initial Rates for a Multicomponent Chemical System",
                "difficulty": "Medium",
                "statement": """The reaction $2 A + B + 2 C \\longrightarrow D + 2 E$ was investigated at $25.0^\\circ\\text{C}$ by the method of initial rates, yielding the following dataset:
- Run 1: $[A]_0 = 0.100\\text{ M}$, $[B]_0 = 0.100\\text{ M}$, $[C]_0 = 0.100\\text{ M}$, $r_0 = 3.20 \\times 10^{-3}\\text{ M/s}$
- Run 2: $[A]_0 = 0.200\\text{ M}$, $[B]_0 = 0.100\\text{ M}$, $[C]_0 = 0.100\\text{ M}$, $r_0 = 6.40 \\times 10^{-3}\\text{ M/s}$
- Run 3: $[A]_0 = 0.100\\text{ M}$, $[B]_0 = 0.200\\text{ M}$, $[C]_0 = 0.100\\text{ M}$, $r_0 = 1.28 \\times 10^{-2}\\text{ M/s}$
- Run 4: $[A]_0 = 0.100\\text{ M}$, $[B]_0 = 0.100\\text{ M}$, $[C]_0 = 0.300\\text{ M}$, $r_0 = 3.20 \\times 10^{-3}\\text{ M/s}$

Determine: (a) the partial reaction orders with respect to $A, B$, and $C$, (b) the overall reaction order, and (c) the rate constant $k$ with appropriate units.""",
                "solution": """**Step 1: Determine partial order with respect to $A$ (Runs 1 and 2)**
Between Run 1 and Run 2, $[B]_0$ and $[C]_0$ are constant while $[A]_0$ doubles:
$$\\frac{r_{0, 2}}{r_{0, 1}} = \\frac{6.40 \\times 10^{-3}}{3.20 \\times 10^{-3}} = 2.000 = \\left( \\frac{0.200}{0.100} \\right)^\\alpha = 2^\\alpha \\implies \\alpha = 1$$
First-order in $A$.

**Step 2: Determine partial order with respect to $B$ (Runs 1 and 3)**
Between Run 1 and Run 3, $[A]_0$ and $[C]_0$ are constant while $[B]_0$ doubles:
$$\\frac{r_{0, 3}}{r_{0, 1}} = \\frac{1.28 \\times 10^{-2}}{3.20 \\times 10^{-3}} = 4.000 = \\left( \\frac{0.200}{0.100} \\right)^\\beta = 2^\\beta \\implies \\beta = 2$$
Second-order in $B$.

**Step 3: Determine partial order with respect to $C$ (Runs 1 and 4)**
Between Run 1 and Run 4, $[A]_0$ and $[B]_0$ are constant while $[C]_0$ triples:
$$\\frac{r_{0, 4}}{r_{0, 1}} = \\frac{3.20 \\times 10^{-3}}{3.20 \\times 10^{-3}} = 1.000 = \\left( \\frac{0.300}{0.100} \\right)^\\gamma = 3^\\gamma \\implies \\gamma = 0$$
Zero-order in $C$.

**Step 4: Overall rate law and overall order**
$$r = k [A]^1 [B]^2 [C]^0 = k [A] [B]^2$$
Overall order: $n = 1 + 2 + 0 = 3$ (Third-order overall).

**Step 5: Rate constant $k$**
Using Run 1:
$$k = \\frac{r_0}{[A]_0 [B]_0^2} = \\frac{3.20 \\times 10^{-3}\\text{ M/s}}{(0.100\\text{ M}) \\times (0.100\\text{ M})^2} = \\frac{3.20 \\times 10^{-3}}{1.00 \\times 10^{-3}\\text{ M}^3} = 3.20\\text{ M}^{-2}\\text{s}^{-1}$$"""
            },
            {
                "id": "p5-3",
                "title": "Rule of Thumb $Q_{10}$ Temperature Sensitivity Analysis",
                "difficulty": "Medium",
                "statement": "A chemical reaction has an activation energy of $E_a = 52.0\\text{ kJ/mol}$. (a) Calculate the exact temperature coefficient $Q_{10} = k(T + 10\\text{ K}) / k(T)$ around ambient temperature ($T = 298.15\\text{ K}$). (b) What activation energy is required for a reaction to exactly double in rate between $298.15\\text{ K}$ and $308.15\\text{ K}$?",
                "solution": """**Step 1: Calculate $Q_{10}$ for $E_a = 52.0\\text{ kJ/mol}$**
$$T_1 = 298.15\\text{ K}, \\quad T_2 = 308.15\\text{ K}$$
$$\\Delta T = 10.0\\text{ K}$$
$$T_1 T_2 = 298.15 \\times 308.15 = 9.18749 \\times 10^4\\text{ K}^2$$
$$\\frac{T_2 - T_1}{T_1 T_2} = \\frac{10.0}{9.18749 \\times 10^4} = 1.08844 \\times 10^{-4}\\text{ K}^{-1}$$

Using the Arrhenius equation:
$$\\ln(Q_{10}) = \\frac{E_a}{R} \\left( \\frac{T_2 - T_1}{T_1 T_2} \\right) = \\frac{52000\\text{ J/mol}}{8.314462\\text{ J}/(\\text{mol}\\cdot\\text{K})} \\times (1.08844 \\times 10^{-4}\\text{ K}^{-1})$$
$$\\ln(Q_{10}) = 6254.16 \\times 1.08844 \\times 10^{-4} = 0.68073$$
$$Q_{10} = \\exp(0.68073) = 1.975$$
The rate increases by a factor of $1.98$, in excellent agreement with van 't Hoff's rule of thumb ($Q_{10} \\approx 2$).

**Step 2: Activation energy for exact rate doubling ($Q_{10} = 2.000$)**
$$\\ln(2.000) = 0.693147$$
$$\\frac{E_a}{R} \\times (1.08844 \\times 10^{-4}) = 0.693147$$
$$\\frac{E_a}{R} = \\frac{0.693147}{1.08844 \\times 10^{-4}} = 6368.26\\text{ K}$$
$$E_a = 6368.26 \\times 8.314462 = 5.2949 \\times 10^4\\text{ J/mol} = 52.95\\text{ kJ/mol}$$
An activation energy of approximately $53\\text{ kJ/mol}$ corresponds exactly to a rate doubling per $10^\\circ\\text{C}$ near room temperature."""
            },
            {
                "id": "p5-4",
                "title": "Composite Activation Energy and Apparent Negative Temperature Dependence",
                "difficulty": "Hard",
                "statement": """The gas-phase termolecular reaction $2 NO + O_2 \\longrightarrow 2 NO_2$ proceeds via a pre-equilibrium mechanism:
1. $2 NO \\underset{k_{-1}}{\\overset{k_1}{\\rightleftharpoons}} N_2O_2$ (fast pre-equilibrium, forward activation energy $E_{a, 1} = 2.1\\text{ kJ/mol}$, reverse activation energy $E_{a, -1} = 15.6\\text{ kJ/mol}$)
2. $N_2O_2 + O_2 \\xrightarrow{k_2} 2 NO_2$ (slow step, activation energy $E_{a, 2} = 8.5\\text{ kJ/mol}$)

(a) Derive the overall rate law and express the apparent rate constant $k_{\\text{obs}}$ in terms of elementary rate constants. (b) Calculate the standard enthalpy of dimerization $\\Delta H_1^\\circ$. (c) Calculate the overall apparent activation energy $E_{a, \\text{app}}$ and explain the physical meaning of its sign.""",
                "solution": """**Step 1: Mechanism derivation and rate law**
For the slow step:
$$r = k_2 [N_2O_2] [O_2]$$

From the fast pre-equilibrium:
$$K_1 = \\frac{k_1}{k_{-1}} = \\frac{[N_2O_2]}{[NO]^2} \\implies [N_2O_2] = \\frac{k_1}{k_{-1}} [NO]^2$$

Substituting:
$$r = \\frac{k_1 k_2}{k_{-1}} [NO]^2 [O_2] = k_{\\text{obs}} [NO]^2 [O_2]$$
where $k_{\\text{obs}} = \\frac{k_1 k_2}{k_{-1}}$.

**Step 2: Enthalpy of dimerization $\\Delta H_1^\\circ$**
$$\\Delta H_1^\\circ = E_{a, 1} - E_{a, -1} = 2.1 - 15.6 = -13.5\\text{ kJ/mol}$$
Dimerization of nitric oxide to $(NO)_2$ is exothermic.

**Step 3: Apparent activation energy $E_{a, \\text{app}}$**
$$E_{a, \\text{app}} = E_{a, 1} + E_{a, 2} - E_{a, -1} = E_{a, 2} + \\Delta H_1^\\circ$$
$$E_{a, \\text{app}} = 8.5 + (-13.5) = -5.0\\text{ kJ/mol}$$

**Physical Interpretation**:
The apparent activation energy is **negative** ($-5.0\\text{ kJ/mol}$). As temperature increases, Le Chatelier's principle shifts the exothermic dimerization pre-equilibrium backward, sharply decreasing the equilibrium concentration of $[N_2O_2]$. This decrease in intermediate concentration outweighs the modest kinetic acceleration of the $k_2$ step, causing the overall reaction rate to **decrease** with rising temperature."""
            },
            {
                "id": "p5-5",
                "title": "Modified Arrhenius Form with Temperature-Dependent Pre-Exponential Factor",
                "difficulty": "Medium",
                "statement": "A gas-phase bimolecular radical reaction is fitted to the modified Arrhenius equation $k(T) = A' T^{1/2} \\exp(-E_0 / R T)$ with $A' = 1.40 \\times 10^7\\text{ M}^{-1}\\text{s}^{-1}\\text{K}^{-1/2}$ and $E_0 = 28.5\\text{ kJ/mol}$. (a) Derive the expression for the experimental Arrhenius activation energy $E_a(T)$. (b) Calculate $E_a$ at $T = 300.0\\text{ K}$ and at $T = 1500.0\\text{ K}$.",
                "solution": """**Step 1: Derive $E_a(T)$ from the definition**
$$k(T) = A' T^{1/2} \\exp\\left( -\\frac{E_0}{R T} \\right)$$
Taking natural logarithms:
$$\\ln k = \\ln A' + \\frac{1}{2} \\ln T - \\frac{E_0}{R T}$$

Differentiating with respect to $T$:
$$\\frac{d \\ln k}{dT} = \\frac{1}{2 T} + \\frac{E_0}{R T^2}$$

By the Arrhenius definition $E_a \\equiv R T^2 \\frac{d \\ln k}{dT}$:
$$E_a(T) = R T^2 \\left( \\frac{1}{2 T} + \\frac{E_0}{R T^2} \\right) = E_0 + \\frac{1}{2} R T$$

**Step 2: Calculate $E_a$ at $T = 300.0\\text{ K}$**
$$\\frac{1}{2} R T = 0.5 \\times (8.314462\\text{ J}/(\\text{mol}\\cdot\\text{K})) \\times (300.0\\text{ K}) = 1247.17\\text{ J/mol} = 1.25\\text{ kJ/mol}$$
$$E_a(300\\text{ K}) = 28.5 + 1.25 = 29.75\\text{ kJ/mol}$$

**Step 3: Calculate $E_a$ at $T = 1500.0\\text{ K}$**
$$\\frac{1}{2} R T = 0.5 \\times (8.314462) \\times (1500.0) = 6235.85\\text{ J/mol} = 6.24\\text{ kJ/mol}$$
$$E_a(1500\\text{ K}) = 28.5 + 6.24 = 34.74\\text{ kJ/mol}$$
The effective activation energy increases by $5.0\\text{ kJ/mol}$ due to the thermal kinetic velocity contribution."""
            },
            {
                "id": "p5-6",
                "title": "Tolman Average Energy Balance for Hard-Sphere Collision Barrier",
                "difficulty": "Hard",
                "statement": "For a line-of-centers hard-sphere model, the reaction cross-section is $\\sigma_R(E) = \\pi d^2 (1 - E_0 / E)$ for $E \\ge E_0$, and $0$ for $E < E_0$. Prove that the average energy of reacting pairs is $\\langle E_R \\rangle = E_0 + 2 k_B T$, and verify Tolman's theorem that $E_a = E_0 + \\frac{1}{2} k_B T$ (per molecule).",
                "solution": """**Step 1: Energy probability density in collision space**
The collision energy probability density for colliding pairs is:
$$P(E) dE = \\frac{E}{(k_B T)^2} \\exp\\left( -\\frac{E}{k_B T} \\right) dE$$
The average energy of all collisions is:
$$\\langle E_{\\text{all}} \\rangle = \\int_0^\\infty E \\, P(E) dE = \\frac{1}{(k_B T)^2} \\int_0^\\infty E^2 e^{-E / k_B T} dE = \\frac{2! (k_B T)^3}{(k_B T)^2} = 2 k_B T$$

**Step 2: Average energy of reactive collisions $\\langle E_R \\rangle$**
Reactive collisions are weighted by $\\sigma_R(E) \\propto (1 - E_0 / E)$:
$$\\langle E_R \\rangle = \\frac{\\int_{E_0}^\\infty E \\cdot E (1 - E_0 / E) e^{-E / k_B T} dE}{\\int_{E_0}^\\infty E (1 - E_0 / E) e^{-E / k_B T} dE} = \\frac{\\int_{E_0}^\\infty (E^2 - E_0 E) e^{-E / k_B T} dE}{\\int_{E_0}^\\infty (E - E_0) e^{-E / k_B T} dE}$$

Let $x = E - E_0 \\implies E = x + E_0$:
Numerator:
$$\\int_0^\\infty [(x + E_0)^2 - E_0 (x + E_0)] e^{-(x + E_0)/k_B T} dx = e^{-E_0 / k_B T} \\int_0^\\infty (x^2 + E_0 x) e^{-x / k_B T} dx$$
$$= e^{-E_0 / k_B T} [ 2 (k_B T)^3 + E_0 (k_B T)^2 ]$$

Denominator:
$$e^{-E_0 / k_B T} \\int_0^\\infty x e^{-x / k_B T} dx = e^{-E_0 / k_B T} (k_B T)^2$$

Dividing numerator by denominator:
$$\\langle E_R \\rangle = \\frac{2 (k_B T)^3 + E_0 (k_B T)^2}{(k_B T)^2} = E_0 + 2 k_B T$$

**Step 3: Verification of Tolman's Theorem**
From collision theory, the rate constant is $k(T) = A' T^{1/2} e^{-E_0 / k_B T}$, so:
$$E_a = k_B T^2 \\frac{d \\ln k}{dT} = E_0 + \\frac{1}{2} k_B T$$
Comparing:
$$\\langle E_R \\rangle - \\langle E_{\\text{all}} \\rangle = (E_0 + 2 k_B T) - (2 k_B T) = E_0$$
Accounting for relative velocity weighting in three dimensions yields the exact Tolman balance $E_a = \\langle E_R \\rangle - \\langle E_{\\text{all}} \\rangle + \\frac{1}{2} k_B T$, verifying the statistical theorem."""
            },
            {
                "id": "p5-7",
                "title": "Quantum Tunneling Crossover Temperature for Proton Transfer",
                "difficulty": "Hard",
                "statement": "In an enzymatic proton-transfer reaction, the activation barrier is modeled as an inverted parabolic barrier of height $V_0 = 40.0\\text{ kJ/mol}$ and width $2 a = 0.800\\text{ Å}$ ($0.800 \\times 10^{-10}\\text{ m}$). The crossover temperature $T_c$ below which quantum mechanical tunneling dominates over classical thermal barrier hopping is given by Goldanskii's relation: $T_c = \\frac{\\hbar \\sqrt{\\kappa_{\\text{bar}} / m_p}}{2 \\pi k_B}$, where barrier curvature is $\\kappa_{\\text{bar}} = 2 V_0 / a^2$. Calculate: (a) $\\kappa_{\\text{bar}}$, (b) the crossover temperature $T_c$ for a proton ($m_p = 1.673 \\times 10^{-27}\\text{ kg}$), and (c) for a deuteron ($m_d = 3.344 \\times 10^{-27}\\text{ kg}$).",
                "solution": """**Step 1: Calculate barrier curvature $\\kappa_{\\text{bar}}$**
$$V_0 = \\frac{40.0 \\times 10^3\\text{ J/mol}}{6.02214 \\times 10^{23}\\text{ mol}^{-1}} = 6.64216 \\times 10^{-20}\\text{ J/molecule}$$
$$a = \\frac{0.800 \\times 10^{-10}}{2} = 4.00 \\times 10^{-11}\\text{ m}$$
$$\\kappa_{\\text{bar}} = \\frac{2 V_0}{a^2} = \\frac{2 \\times (6.64216 \\times 10^{-20})}{(4.00 \\times 10^{-11})^2} = \\frac{1.32843 \\times 10^{-19}}{1.600 \\times 10^{-21}} = 83.027\\text{ N/m}$$

**Step 2: Crossover temperature $T_c$ for proton**
$$m_p = 1.6726 \\times 10^{-27}\\text{ kg}$$
$$\\omega_0 = \\sqrt{\\frac{\\kappa_{\\text{bar}}}{m_p}} = \\sqrt{\\frac{83.027}{1.6726 \\times 10^{-27}}} = \\sqrt{4.96395 \\times 10^{28}} = 2.2280 \\times 10^{14}\\text{ rad/s}$$

$$T_c(H) = \\frac{\\hbar \\omega_0}{2 \\pi k_B} = \\frac{(1.05457 \\times 10^{-34}) \\times (2.2280 \\times 10^{14})}{2 \\pi \\times (1.380649 \\times 10^{-23})}$$
$$\\text{Numerator} = 2.3496 \\times 10^{-20}\\text{ J}$$
$$\\text{Denominator} = 8.6748 \\times 10^{-23}\\text{ J/K}$$
$$T_c(H) = \\frac{2.3496 \\times 10^{-20}}{8.6748 \\times 10^{-23}} = 270.85\\text{ K} = -2.3^\\circ\\text{C}$$
At physiological temperatures ($310\\text{ K}$), proton tunneling already contributes significantly to the enzyme rate.

**Step 3: Crossover temperature $T_c$ for deuteron**
Since $m_d = 2 m_p$, $\\omega_0(D) = \\omega_0(H) / \\sqrt{2}$:
$$T_c(D) = \\frac{T_c(H)}{\\sqrt{2}} = \\frac{270.85}{1.4142} = 191.5\\text{ K}$$
Because $T_c(D)$ is much lower, replacing $H$ with $D$ suppresses tunneling at room temperature, generating massive primary kinetic isotope effects ($k_H / k_D > 20$)."""
            }
        ]
    }
    units.append(u5)

    # =========================================================================
    # UNIT 6: Reaction Mechanisms, Approximations & Kinetic Isotope Effects
    # =========================================================================
    u6 = {
        "id": "unit-6",
        "unitNumber": 6,
        "title": "Unit 6: Reaction Mechanisms, Approximations & Kinetic Isotope Effects",
        "leadSummary": "Microscopic mechanisms and mathematical approximations in chemical reaction networks: consecutive reaction dynamics, rate-determining step theorems, the Bodenstein steady-state approximation (SSA), the pre-equilibrium quasi-steady state, Bigeleisen transition-state theory of primary and secondary kinetic isotope effects (KIE), and quantum tunneling corrections.",
        "simulations": ["sim_kin_consecutive_reactions_ssa"],
        "sections": [
            {
                "id": "sec-6-1",
                "secNumber": "6.1",
                "title": "Microscopic Reaction Mechanisms & Elementary Reaction Networks",
                "content": """A chemical reaction mechanism is a step-by-step description of the sequence of elementary steps by which overall chemical transformation occurs.

### Criteria for a Valid Reaction Mechanism
1. **Stoichiometric Consistency**: Summing all elementary steps must yield the balanced stoichiometric equation of the overall reaction.
2. **Kinetic Agreement**: The theoretical rate law derived from the mechanism must match the empirical rate law observed experimentally across all concentration regimes.
3. **Spectroscopic Verification**: Postulated reactive intermediates must be detectable (or trapped) experimentally via fast spectroscopic probes.

### Intermediates vs. Transition States
- **Reactive Intermediate**: Corresponds to a local potential energy minimum along the reaction coordinate. Has a finite lifetime (typically $> 10^{-13}\\text{ s}$, exceeding a vibrational period), and can in principle be isolated or spectroscopically observed.
- **Transition State** (Activated Complex): Corresponds to a first-order saddle point (maximum along reaction coordinate, minimum in all orthogonal coordinates). Lifetime is infinitesimal ($\\sim 10^{-14}\\text{ s}$, the timescale of a single molecular vibration), and cannot be trapped as a chemical substance."""
            },
            {
                "id": "sec-6-2",
                "secNumber": "6.2",
                "title": "Consecutive Elementary Reactions: Exact Mathematical Concentration Dynamics",
                "content": """Consider the simplest consecutive reaction sequence of two irreversible first-order steps:
$$A \\xrightarrow{k_1} B \\xrightarrow{k_2} C$$
Initial conditions at $t = 0$: $[A](0) = [A]_0$, $[B](0) = 0$, $[C](0) = 0$.

### System of Coupled Differential Equations
1. $$\\frac{d[A]}{dt} = -k_1 [A]$$
2. $$\\frac{d[B]}{dt} = k_1 [A] - k_2 [B]$$
3. $$\\frac{d[C]}{dt} = k_2 [B]$$

### Analytical Solution
Integrating the first equation:
$$[A](t) = [A]_0 \\exp(-k_1 t)$$

Substituting $[A](t)$ into the second equation:
$$\\frac{d[B]}{dt} + k_2 [B] = k_1 [A]_0 \\exp(-k_1 t)$$
This is a first-order linear ordinary differential equation. Using the integrating factor $e^{k_2 t}$:
$$\\frac{d}{dt} \\left( [B] e^{k_2 t} \\right) = k_1 [A]_0 e^{(k_2 - k_1) t}$$
Integrating with $[B](0) = 0$:
$$[B](t) = [A]_0 \\left( \\frac{k_1}{k_2 - k_1} \\right) \\left( e^{-k_1 t} - e^{-k_2 t} \\right) \\quad (k_1 \\neq k_2)$$

By mass conservation $[A]_0 = [A](t) + [B](t) + [C](t)$:
$$[C](t) = [A]_0 \\left[ 1 - \\frac{k_2 e^{-k_1 t} - k_1 e^{-k_2 t}}{k_2 - k_1} \\right]$$

### Peak Intermediate Concentration ($t_{\\max}$)
Setting $\\frac{d[B]}{dt} = 0$:
$$k_1 e^{-k_1 t_{\\max}} = k_2 e^{-k_2 t_{\\max}} \\implies t_{\\max} = \\frac{\\ln(k_1 / k_2)}{k_1 - k_2} = \\frac{\\ln(k_2 / k_1)}{k_2 - k_1}$$

Substituting $t_{\\max}$ into $[B](t)$:
$$[B]_{\\max} = [A]_0 \\left( \\frac{k_2}{k_1} \\right)^{\\frac{k_2}{k_1 - k_2}}$$"""
            },
            {
                "id": "sec-6-3",
                "secNumber": "6.3",
                "title": "The Rate-Determining Step (RDS) Principle & Microscopic Bottleneck Analysis",
                "content": """When one elementary step in a reaction sequence is substantially slower than all preceding and succeeding steps, it acts as a kinetic bottleneck that governs the overall rate.

### Formal Criteria for an RDS
Consider the consecutive sequence:
$$A \\xrightarrow{k_1} B \\xrightarrow{k_2} C$$

1. **Case 1: First Step Slow ($k_1 \\ll k_2$)**:
   The intermediate $B$ reacts to form $C$ as rapidly as it is generated. Therefore:
   $$e^{-k_2 t} \\to 0 \\text{ rapidly, and } k_2 - k_1 \\approx k_2$$
   $$[C](t) \\approx [A]_0 (1 - e^{-k_1 t})$$
   $$\\frac{d[C]}{dt} \\approx k_1 [A]_0 e^{-k_1 t} = k_1 [A]$$
   The overall rate is completely dictated by the first step ($k_1$). Step 1 is the **Rate-Determining Step**.

2. **Case 2: Second Step Slow ($k_1 \\gg k_2$)**:
   Reactant $A$ converts rapidly to intermediate $B$, which then slowly leaks into product $C$.
   $$[B](t) \\approx [A]_0 e^{-k_2 t}, \\quad [C](t) \\approx [A]_0 (1 - e^{-k_2 t})$$
   Step 2 is the Rate-Determining Step."""
            },
            {
                "id": "sec-6-4",
                "secNumber": "6.4",
                "title": "Bodenstein Steady-State Approximation (SSA): Mathematical Foundation",
                "content": """In complex multi-step reaction networks involving highly reactive intermediates (radicals, carbocations, excited states), solving coupled differential equations analytically is intractable. Max Bodenstein (1913) formulated the **Steady-State Approximation (SSA)**.

### Mathematical Formulation
If intermediate $[I]$ is highly reactive ($k_{\\text{consumption}} \\gg k_{\\text{formation}}$), its concentration remains vanishingly small compared to reactants and products throughout most of the reaction:
$$[I](t) \\ll [A](t), [P](t)$$

Consequently, after a negligible initial induction period $\\tau_{\\text{ind}} \\sim 1/k_{\\text{consumption}}$, the net time rate of change of the intermediate concentration is approximately zero:
$$\\frac{d[I]}{dt} \\approx 0 \\iff \\sum r_{\\text{formation}} - \\sum r_{\\text{consumption}} = 0$$

### Application to Consecutive Reactions
For $A \\xrightarrow{k_1} B \\xrightarrow{k_2} C$:
$$\\frac{d[B]}{dt} = k_1 [A] - k_2 [B] \\approx 0 \\implies [B]_{\\text{SSA}} = \\frac{k_1}{k_2} [A]$$

Substituting into the rate of product formation:
$$\\frac{d[C]}{dt} = k_2 [B]_{\\text{SSA}} = k_2 \\left( \\frac{k_1}{k_2} [A] \\right) = k_1 [A]$$

**Validity Condition**:
Comparison with the exact solution proves that the SSA is mathematically valid whenever:
$$k_2 \\gg k_1 \\iff \\frac{k_2}{k_1} > 20$$
Under this condition, $[B]_{\\max} / [A]_0 \\ll 1$, and the steady-state assumption introduces negligible error."""
            },
            {
                "id": "sec-6-5",
                "secNumber": "6.5",
                "title": "Pre-Equilibrium (Quasi-Equilibrium) Approximation vs. Steady-State",
                "content": """A common motif in chemistry involves a rapid reversible equilibrium establishing prior to a rate-limiting conversion.

### The Pre-Equilibrium Model
$$A + B \\underset{k_{-1}}{\\overset{k_1}{\\rightleftharpoons}} AB^* \\xrightarrow{k_2} P$$

1. **Pre-Equilibrium Assumption**:
   Assumes the reversible steps $k_1$ and $k_{-1}$ are much faster than the product formation step $k_2$ ($k_{-1} \\gg k_2$).
   Dynamic equilibrium is maintained between reactants and intermediate:
   $$\\frac{[AB^*]}{[A][B]} = \\frac{k_1}{k_{-1}} = K_c \\implies [AB^*] = K_c [A][B]$$
   $$r = \\frac{d[P]}{dt} = k_2 [AB^*] = k_2 K_c [A][B] = \\left( \\frac{k_1 k_2}{k_{-1}} \\right) [A][B]$$

2. **Rigorous SSA Treatment**:
   Applying the Bodenstein SSA to $[AB^*]$ without assuming $k_{-1} \\gg k_2$:
   $$\\frac{d[AB^*]}{dt} = k_1 [A][B] - k_{-1} [AB^*] - k_2 [AB^*] = 0$$
   $$[AB^*] = \\frac{k_1 [A][B]}{k_{-1} + k_2}$$
   $$r = k_2 [AB^*] = \\left( \\frac{k_1 k_2}{k_{-1} + k_2} \\right) [A][B]$$

**Hierarchy**:
- If $k_{-1} \\gg k_2$: $\\frac{k_1 k_2}{k_{-1} + k_2} \\to \\frac{k_1 k_2}{k_{-1}}$, recovering the pre-equilibrium result.
- If $k_2 \\gg k_{-1}$: $\\frac{k_1 k_2}{k_{-1} + k_2} \\to k_1$, meaning every encounter that forms $AB^*$ proceeds immediately to product, making initial encounter $k_1$ rate-determining.
The SSA is universally valid, whereas the pre-equilibrium approximation is a special limiting case."""
            },
            {
                "id": "sec-6-6",
                "secNumber": "6.6",
                "title": "Kinetic Isotope Effects (KIE): Bigeleisen Transition-State Theory",
                "content": """The Kinetic Isotope Effect (KIE) is the ratio of rate constants for reactions differing only in isotopic substitution:
$$\\text{KIE} = \\frac{k_L}{k_H}$$
where $k_L$ is the rate constant for the light isotope (e.g., $^1H$) and $k_H$ is for the heavy isotope (e.g., $^2H = D$).

### Origin in Zero-Point Vibrational Energy (ZPE)
Under the Born-Oppenheimer approximation, electronic potential energy surfaces are identical for isotopologs. However, quantum mechanical vibrational energy levels depend on reduced mass:
$$\\nu = \\frac{1}{2\\pi} \\sqrt{\\frac{k_{\\text{force}}}{\\mu}}$$
Zero-point vibrational energy is $E_0 = \\frac{1}{2} h \\nu$.

Because $m_D \\approx 2 m_H$, the reduced mass for a $C-D$ bond is roughly double that for a $C-H$ bond:
$$\\nu_{C-H} \\approx 2900\\text{ cm}^{-1} \\implies E_{0, C-H} = \\frac{1}{2} h c \\tilde{\\nu} \\approx 17.3\\text{ kJ/mol}$$
$$\\nu_{C-D} \\approx 2100\\text{ cm}^{-1} \\implies E_{0, C-D} \\approx 12.6\\text{ kJ/mol}$$
$$\\Delta E_0 = E_{0, C-H} - E_{0, C-D} \\approx 4.7\\text{ kJ/mol}$$

The heavier $C-D$ bond sits deeper in the potential well, requiring greater activation energy to reach the transition state:
$$\\frac{k_H}{k_D} = \\exp\\left( \\frac{\\Delta E_0}{R T} \\right) = \\exp\\left( \\frac{4700}{8.314 \\times 298.15} \\right) \\approx \\exp(1.896) \\approx 6.7$$

### Classification of KIEs
1. **Primary KIE**: The bond to the isotopically substituted atom is cleaved or formed in the rate-determining transition state ($k_H / k_D \\approx 2\\text{--}7$ at $298\\text{ K}$).
2. **Secondary KIE**: The isotopic substitution is at a neighboring atom not undergoing bond cleavage ($k_H / k_D \\approx 0.7\\text{--}1.4$), reflecting changes in hybridization ($sp^3 \\to sp^2$ or vice versa).
3. **Tunneling KIE**: Primary $k_H / k_D > 10$ indicates significant quantum mechanical tunneling."""
            },
            {
                "id": "sec-6-7",
                "secNumber": "6.7",
                "title": "Bell Model of Quantum Tunneling in Hydrogen/Proton Transfer",
                "content": """When hydrogen transfer occurs through a narrow activation barrier, quantum tunneling causes massive deviations from semi-classical Bigeleisen KIE theory.

### The Bell Truncated Parabolic Barrier
R.P. Bell (1980) formulated the semi-analytical correction factor $Q_t$ for tunneling through a one-dimensional parabolic barrier of height $E_b$ and half-width $a$:
$$Q_t = \\frac{u/2}{\\sin(u/2)} - \\sum_{n=1}^\\infty (-1)^n \\frac{\\exp\\left( \\frac{2\\pi n - u}{u} \\frac{E_b}{k_B T} \\right)}{\\frac{2\\pi n - u}{u}}$$
where $u = \\frac{h \\nu^*}{k_B T}$ and $\\nu^* = \\frac{1}{2\\pi a} \\sqrt{\\frac{2 E_b}{m}}$ is the imaginary barrier frequency.

For $u < 2\\pi$:
$$Q_t \\approx 1 + \\frac{1}{24} \\left( \\frac{h \\nu^*}{k_B T} \\right)^2$$

### Experimental Hallmarks of Quantum Tunneling
1. **Anomalously Large Primary KIE**: Experimental values of $k_H / k_D$ reaching $15\\text{--}100$ (e.g., in soybean lipoxygenase, $k_H / k_D \\approx 80$).
2. **Temperature Independence of KIE**: At low temperatures, the ratio $k_H / k_D$ approaches a plateau rather than diverging exponentially as $\\exp(\\Delta E / R T)$.
3. **Anomalous Arrhenius Pre-Exponential Ratio**: Semiclassical theory restricts $A_H / A_D$ to $0.7\\text{--}1.4$. With tunneling, $A_H / A_D < 0.1$ or $A_H / A_D > 10$ is observed, proving non-classical barrier penetration."""
            }
        ],
        "problems": [
            {
                "id": "p6-1",
                "title": "Exact Analytical Dynamics of Consecutive Radioactive/Kinetic Series",
                "difficulty": "Easy",
                "statement": "In a consecutive reaction sequence $A \\xrightarrow{k_1} B \\xrightarrow{k_2} C$, the rate constants are $k_1 = 0.500\\text{ min}^{-1}$ and $k_2 = 0.100\\text{ min}^{-1}$. The initial concentration of $A$ is $[A]_0 = 1.000\\text{ M}$, with $[B]_0 = [C]_0 = 0$. Calculate: (a) the time $t_{\\max}$ at which intermediate $B$ reaches maximum concentration, (b) the maximum concentration $[B]_{\\max}$, and (c) the concentration of product $C$ at $t = t_{\\max}$.",
                "solution": """**Step 1: Calculate $t_{\\max}$**
$$t_{\\max} = \\frac{\\ln(k_1 / k_2)}{k_1 - k_2} = \\frac{\\ln(0.500 / 0.100)}{0.500 - 0.100} = \\frac{\\ln(5.000)}{0.400\\text{ min}^{-1}} = \\frac{1.60944}{0.400} = 4.0236\\text{ minutes}$$

**Step 2: Calculate maximum concentration $[B]_{\\max}$**
Using the analytical formula:
$$[B]_{\\max} = [A]_0 \\left( \\frac{k_2}{k_1} \\right)^{\\frac{k_2}{k_1 - k_2}} = 1.000 \\times \\left( \\frac{0.100}{0.500} \\right)^{\\frac{0.100}{0.400}} = (0.200)^{0.250} = 0.66874\\text{ M}$$

Alternatively, evaluating $[B](t_{\\max})$ directly:
$$e^{-k_1 t_{\\max}} = e^{-0.500 \\times 4.0236} = e^{-2.0118} = 0.13375$$
$$e^{-k_2 t_{\\max}} = e^{-0.100 \\times 4.0236} = e^{-0.40236} = 0.66874$$
$$[B](t_{\\max}) = 1.000 \\times \\left( \\frac{0.500}{0.100 - 0.500} \\right) \\times (0.13375 - 0.66874) = (-1.25) \\times (-0.53499) = 0.66874\\text{ M}$$

**Step 3: Calculate $[C]$ at $t_{\\max}$**
$$[A](t_{\\max}) = [A]_0 e^{-k_1 t_{\\max}} = 1.000 \\times 0.13375 = 0.13375\\text{ M}$$
By mass balance:
$$[C](t_{\\max}) = [A]_0 - [A](t_{\\max}) - [B](t_{\\max}) = 1.000 - 0.13375 - 0.66874 = 0.19751\\text{ M}$$"""
            },
            {
                "id": "p6-2",
                "title": "Bodenstein Steady-State Approximation for Nitramide Decomposition",
                "difficulty": "Medium",
                "statement": """The base-catalyzed decomposition of nitramide ($H_2NNO_2 \\xrightarrow{OH^-} N_2O + H_2O$) follows the mechanism:
1. $H_2NNO_2 + H_2O \\underset{k_{-1}}{\\overset{k_1}{\\rightleftharpoons}} HNNO_2^- + H_3O^+$ (rapid equilibrium)
2. $HNNO_2^- \\xrightarrow{k_2} N_2O + OH^-$ (slow decomposition)
3. $H_3O^+ + OH^- \\xrightarrow{k_3} 2 H_2O$ (ultra-fast neutralization)

Applying the Bodenstein Steady-State Approximation to intermediate $HNNO_2^-$, derive the rate law for $d[N_2O]/dt$ and determine the apparent order with respect to hydronium ion $[H_3O^+].""",
                "solution": """**Step 1: Set up the rate equation for product formation**
$$\\frac{d[N_2O]}{dt} = k_2 [HNNO_2^-]$$

**Step 2: Apply the Bodenstein Steady-State Approximation to $[HNNO_2^-]$**
$$\\frac{d[HNNO_2^-]}{dt} = k_1 [H_2NNO_2][H_2O] - k_{-1} [HNNO_2^-][H_3O^+] - k_2 [HNNO_2^-] = 0$$

Solving for $[HNNO_2^-]$:
$$[HNNO_2^-] \\left( k_{-1} [H_3O^+] + k_2 \\right) = k_1 [H_2NNO_2] [H_2O]$$
$$[HNNO_2^-] = \\frac{k_1 [H_2O] [H_2NNO_2]}{k_{-1} [H_3O^+] + k_2}$$

**Step 3: Substitute into rate of product formation**
$$\\frac{d[N_2O]}{dt} = \\frac{k_1 k_2 [H_2O] [H_2NNO_2]}{k_{-1} [H_3O^+] + k_2}$$

In dilute aqueous solution, $k_{-1} [H_3O^+] \\gg k_2$ (the recombination with hydronium is much faster than decomposition):
$$\\frac{d[N_2O]}{dt} \\approx \\frac{k_1 k_2 [H_2O]}{k_{-1}} \\frac{[H_2NNO_2]}{[H_3O^+]} = k_{\\text{obs}} \\frac{[H_2NNO_2]}{[H_3O^+]}$$

**Conclusion**: The reaction is **first-order** in nitramide and exhibits an **inverse first-order** (order $-1$) dependence on $[H_3O^+]$, explaining why the reaction is catalyzed by bases and strongly inhibited by acid."""
            },
            {
                "id": "p6-3",
                "title": "Primary Kinetic Isotope Effect from Zero-Point Energy Frequencies",
                "difficulty": "Medium",
                "statement": "The stretching vibrational frequency of a carbon-hydrogen bond in an alkane is $\\tilde{\\nu}_{C-H} = 2960\\text{ cm}^{-1}$. For the deuterated bond, $\\tilde{\\nu}_{C-D} = 2180\\text{ cm}^{-1}$. Assuming the stretching vibration is completely lost at the transition state (symmetrical transition state with $\\nu^\\ddagger \\approx 0$): (a) calculate the zero-point energy difference $\\Delta E_0$ in $\\text{kJ/mol}$, and (b) calculate the theoretical maximum semiclassical primary kinetic isotope effect $k_H / k_D$ at $T = 298.15\\text{ K}$ and at $T = 500.0\\text{ K}$.",
                "solution": """**Step 1: Calculate zero-point vibrational energies**
$$E_0 = \\frac{1}{2} h c \\tilde{\\nu} N_A$$
where $h c N_A = (6.62607 \\times 10^{-34}) \\times (2.99792 \\times 10^{10}\\text{ cm/s}) \\times (6.02214 \\times 10^{23}) = 11.9627\\text{ J}\\cdot\\text{cm/mol} = 0.0119627\\text{ kJ}\\cdot\\text{cm/mol}$.

$$E_{0, C-H} = \\frac{1}{2} \\times 0.0119627 \\times 2960 = 17.705\\text{ kJ/mol}$$
$$E_{0, C-D} = \\frac{1}{2} \\times 0.0119627 \\times 2180 = 13.040\\text{ kJ/mol}$$

Zero-point energy difference:
$$\\Delta E_0 = E_{0, C-H} - E_{0, C-D} = 17.705 - 13.040 = 4.665\\text{ kJ/mol} = 4665\\text{ J/mol}$$

**Step 2: Semiclassical KIE at $T = 298.15\\text{ K}$**
$$\\frac{k_H}{k_D} = \\exp\\left( \\frac{\\Delta E_0}{R T} \\right) = \\exp\\left( \\frac{4665}{8.314462 \\times 298.15} \\right) = \\exp\\left( \\frac{4665}{2478.96} \\right) = \\exp(1.8818) = 6.565$$
At room temperature, the theoretical semiclassical primary KIE is approximately **$6.6$**.

**Step 3: Semiclassical KIE at $T = 500.0\\text{ K}$**
$$\\frac{k_H}{k_D} = \\exp\\left( \\frac{4665}{8.314462 \\times 500.0} \\right) = \\exp\\left( \\frac{4665}{4157.23} \\right) = \\exp(1.1221) = 3.071$$
As temperature increases, thermal excitation reduces the influence of zero-point differences, diminishing the KIE to **$3.1$**."""
            },
            {
                "id": "p6-4",
                "title": "Pre-Equilibrium vs. Steady-State Mathematical Accuracy Comparison",
                "difficulty": "Hard",
                "statement": "For the reaction scheme $A + B \\underset{k_{-1}}{\\overset{k_1}{\\rightleftharpoons}} I \\xrightarrow{k_2} P$, the rate constants are $k_1 = 1.00 \\times 10^5\\text{ M}^{-1}\\text{s}^{-1}$, $k_{-1} = 2.00 \\times 10^4\\text{ s}^{-1}$, and $k_2 = 5.00 \\times 10^3\\text{ s}^{-1}$. (a) Calculate the exact apparent second-order rate constant $k_{\\text{SSA}}$ using the Bodenstein Steady-State Approximation. (b) Calculate the approximate rate constant $k_{\\text{pre}}$ assuming pre-equilibrium. (c) Calculate the percent error incurred by using the pre-equilibrium approximation.",
                "solution": """**Step 1: Calculate $k_{\\text{SSA}}$**
From the steady-state derivation:
$$k_{\\text{SSA}} = \\frac{k_1 k_2}{k_{-1} + k_2}$$
$$\\text{Numerator} = (1.00 \\times 10^5) \\times (5.00 \\times 10^3) = 5.00 \\times 10^8\\text{ M}^{-1}\\text{s}^{-2}$$
$$\\text{Denominator} = 2.00 \\times 10^4 + 5.00 \\times 10^3 = 2.50 \\times 10^4\\text{ s}^{-1}$$
$$k_{\\text{SSA}} = \\frac{5.00 \\times 10^8}{2.50 \\times 10^4} = 2.000 \\times 10^4\\text{ M}^{-1}\\text{s}^{-1}$$

**Step 2: Calculate $k_{\\text{pre}}$**
Under pre-equilibrium, assuming $k_2 \\ll k_{-1}$:
$$k_{\\text{pre}} = \\frac{k_1 k_2}{k_{-1}} = \\frac{5.00 \\times 10^8}{2.00 \\times 10^4} = 2.500 \\times 10^4\\text{ M}^{-1}\\text{s}^{-1}$$

**Step 3: Percent error**
$$\\text{Error} = \\frac{k_{\\text{pre}} - k_{\\text{SSA}}}{k_{\\text{SSA}}} \\times 100\\% = \\frac{2.500 \\times 10^4 - 2.000 \\times 10^4}{2.000 \\times 10^4} \\times 100\\% = \\frac{0.500}{2.000} \\times 100\\% = +25.0\\%$$
The pre-equilibrium approximation overestimates the true rate constant by $25.0\\%$, because $k_2$ is $25\\%$ as large as $k_{-1}$, violating the condition $k_{-1} \\gg k_2$."""
            },
            {
                "id": "p6-5",
                "title": "Ozone Decomposition Catalytic Cycle & SSA Rate Law Derivation",
                "difficulty": "Hard",
                "statement": """The thermal decomposition of ozone ($2 O_3 \\longrightarrow 3 O_2$) proceeds via the Chapman mechanism:
1. $O_3 \\underset{k_{-1}}{\\overset{k_1}{\\rightleftharpoons}} O_2 + O$ (reversible collision dissociation)
2. $O + O_3 \\xrightarrow{k_2} 2 O_2$ (bimolecular atomic scavenging)

(a) Apply the steady-state approximation to oxygen atoms $[O]$ to derive the expression for $d[O_2]/dt$. (b) Determine the limiting rate laws at high $[O_2]$ and at low $[O_2]$.""",
                "solution": """**Step 1: Rate of product $O_2$ formation**
$$\\frac{d[O_2]}{dt} = k_1 [O_3] - k_{-1} [O_2][O] + 2 k_2 [O][O_3]$$

**Step 2: Apply the Bodenstein SSA to $[O]$**
$$\\frac{d[O]}{dt} = k_1 [O_3] - k_{-1} [O_2][O] - k_2 [O][O_3] = 0$$
Solving for $[O]$:
$$[O] (k_{-1} [O_2] + k_2 [O_3]) = k_1 [O_3]$$
$$[O] = \\frac{k_1 [O_3]}{k_{-1} [O_2] + k_2 [O_3]}$$

**Step 3: Overall decomposition rate of ozone**
$$\\text{Rate} = -\\frac{1}{2} \\frac{d[O_3]}{dt} = \\frac{1}{3} \\frac{d[O_2]}{dt}$$
The net rate of consumption of $O_3$ is:
$$-\\frac{d[O_3]}{dt} = k_1 [O_3] - k_{-1} [O_2][O] + k_2 [O][O_3]$$
From the SSA equation, $k_1 [O_3] - k_{-1} [O_2][O] = k_2 [O][O_3]$.
Thus:
$$-\\frac{d[O_3]}{dt} = 2 k_2 [O][O_3] = \\frac{2 k_1 k_2 [O_3]^2}{k_{-1} [O_2] + k_2 [O_3]}$$

**Step 4: Limiting regimes**
1. **High $[O_2]$ regime** ($k_{-1} [O_2] \\gg k_2 [O_3]$):
   $$-\\frac{d[O_3]}{dt} \\approx \\frac{2 k_1 k_2 [O_3]^2}{k_{-1} [O_2]} = k_{\\text{obs}} \\frac{[O_3]^2}{[O_2]}$$
   Second-order in ozone, and inhibited by molecular oxygen (order $-1$ in $O_2$), in exact agreement with experimental atmospheric measurements.
2. **Low $[O_2]$ regime** ($k_2 [O_3] \\gg k_{-1} [O_2]$):
   $$-\\frac{d[O_3]}{dt} \\approx 2 k_1 [O_3]$$
   The reaction becomes first-order in $O_3$."""
            },
            {
                "id": "p6-6",
                "title": "Quantum Mechanical Tunneling Correction in Soybean Lipoxygenase",
                "difficulty": "Hard",
                "statement": "Soybean lipoxygenase-1 catalyzes hydrogen atom abstraction from linoleic acid with an extraordinarily large primary kinetic isotope effect of $k_H / k_D = 81.0$ at $T = 298.15\\text{ K}$. Semiclassical transition state theory predicts a maximum $k_H / k_D = 6.80$. Assuming the excess KIE is entirely due to quantum tunneling ($k = k_{\\text{sc}} Q_t$): (a) calculate the ratio of tunneling transmission factors $Q_{t, H} / Q_{t, D}$, and (b) if $Q_{t, D} \\approx 1.25$ (deuteron tunnels minimally), determine the absolute tunneling transmission coefficient $Q_{t, H}$ for the proton.",
                "solution": """**Step 1: Formulate the observed KIE in terms of tunneling**
$$\\left( \\frac{k_H}{k_D} \\right)_{\\text{obs}} = \\left( \\frac{k_H}{k_D} \\right)_{\\text{sc}} \\times \\left( \\frac{Q_{t, H}}{Q_{t, D}} \\right)$$
where:
- $(k_H / k_D)_{\\text{obs}} = 81.0$
- $(k_H / k_D)_{\\text{sc}} = 6.80$

Solving for the ratio of tunneling factors:
$$\\frac{Q_{t, H}}{Q_{t, D}} = \\frac{(k_H / k_D)_{\\text{obs}}}{(k_H / k_D)_{\\text{sc}}} = \\frac{81.0}{6.80} = 11.912$$

**Step 2: Calculate absolute tunneling coefficient $Q_{t, H}$**
Given that $Q_{t, D} = 1.25$:
$$Q_{t, H} = 11.912 \\times 1.25 = 14.89 \\approx 14.9$$

**Step 3: Physical interpretation**
$Q_{t, H} = 14.9$ indicates that at room temperature, the rate of proton transfer is nearly **15 times faster** than classical transition-state theory predicts because the proton predominantly tunnels through the barrier rather than climbing over it. This landmark experimental finding in enzymology proves that biological catalysts harness quantum wave-particle duality to accelerate vital metabolic transformations."""
            },
            {
                "id": "p6-7",
                "title": "Equilibrium Constant Derivation from Microscopic Forward and Reverse Rates",
                "difficulty": "Medium",
                "statement": "The gas-phase reaction $NO(g) + NO_2(g) + H_2O(g) \\underset{k_{-1}}{\\overset{k_1}{\\rightleftharpoons}} 2 HNO_2(g)$ has a forward rate law $r_f = k_1 [NO][NO_2][H_2O]$ with $k_1 = 4.20 \\times 10^3\\text{ M}^{-2}\\text{s}^{-1}$ at $25.0^\\circ\\text{C}$. The reverse reaction is second-order in nitrous acid: $r_r = k_{-1} [HNO_2]^2$ with $k_{-1} = 2.80 \\times 10^{-2}\\text{ M}^{-1}\\text{s}^{-1}$. (a) Verify microscopic reversibility and calculate the concentration equilibrium constant $K_c$. (b) Calculate standard Gibbs free energy of reaction $\\Delta G^\\circ$.",
                "solution": """**Step 1: Principle of microscopic reversibility and $K_c$**
At dynamic chemical equilibrium:
$$r_f = r_r \\implies k_1 [NO][NO_2][H_2O] = k_{-1} [HNO_2]^2$$
$$K_c = \\frac{[HNO_2]^2}{[NO][NO_2][H_2O]} = \\frac{k_1}{k_{-1}}$$

Evaluating numerically:
$$K_c = \\frac{4.20 \\times 10^3\\text{ M}^{-2}\\text{s}^{-1}}{2.80 \\times 10^{-2}\\text{ M}^{-1}\\text{s}^{-1}} = 1.500 \\times 10^5\\text{ M}^{-1} = 1.50 \\times 10^5\\text{ L/mol}$$

**Step 2: Standard Gibbs free energy $\\Delta G^\\circ$**
Thermodynamic standard state: $c^\\circ = 1.00\\text{ M} = 1.00\\text{ mol/L}$.
Dimensionless equilibrium constant:
$$K^\\circ = K_c \\cdot c^\\circ = 1.500 \\times 10^5$$
$$\\Delta G^\\circ = -R T \\ln K^\\circ$$
$$R T = (8.314462\\text{ J}/(\\text{mol}\\cdot\\text{K})) \\times (298.15\\text{ K}) = 2478.96\\text{ J/mol} = 2.47896\\text{ kJ/mol}$$
$$\\ln(1.500 \\times 10^5) = 11.91839$$
$$\\Delta G^\\circ = -2.47896 \\times 11.91839 = -29.545\\text{ kJ/mol}$$"""
            }
        ]
    }
    units.append(u6)

    return units

if __name__ == "__main__":
    units = get_units_4_5_6()
    print(f"Built Units 4, 5, and 6 successfully! Total units: {len(units)}")
    for u in units:
        print(f"  - {u['title']}: {len(u['sections'])} sections, {len(u['problems'])} problems")
