# build_plasma_units_5_6.py
# Generates plasma_u5.json and plasma_u6.json for Plasma Physics Course #17

import json

# =========================================================================
# UNIT 5: ELECTROSTATIC WAVES IN UNMAGNETIZED AND MAGNETIZED PLASMAS
# =========================================================================

unit5_data = {
    "unitId": "unit5-plasma",
    "title": "Electrostatic Waves in Unmagnetized and Magnetized Plasmas",
    "subtitle": "Langmuir Waves, Bohm-Gross Dispersion & Ion Acoustic Modes",
    "summary": "Comprehensive theory of electrostatic plasma oscillations and waves: harmonic representations, phase and group velocity, perturbation linearization of the multi-fluid equations, cold electron plasma oscillations, thermal electron pressure and the complete Bohm-Gross dispersion relation derivation, ion acoustic waves (plasma sound waves), ion sound speed, short-wavelength electron screening breakdown at k lambda_D ~ 1, comprehensive comparison between electron and ion modes, and electrostatic waves in magnetized plasmas including Upper Hybrid, Lower Hybrid, and electrostatic ion cyclotron (EIC) waves.",
    "sections": [
        {
            "id": "sec-5-1",
            "number": "5.1",
            "title": "Harmonic Wave Representations, Phase Velocity & Group Velocity",
            "content": """
<h3>1. Complex Harmonic Wave Representations</h3>
<p>
Small-amplitude perturbations in plasma fluid quantities (density, velocity, electric and magnetic fields) are expanded as superpositions of plane waves:
</p>
$$\\psi(\\vec{r}, t) = \\psi_0 + \\psi_1 \\exp\\left[ i(\\vec{k}\\cdot\\vec{r} - \\omega t) \\right]$$
<p>
where $\\psi_0$ is the unperturbed background equilibrium state, $\\psi_1$ is the first-order perturbation amplitude ($|\\psi_1| \\ll |\\psi_0|$), $\\vec{k}$ is the wavevector, and $\\omega$ is the angular frequency. Under this harmonic convention, differential operators transform into algebraic multipliers:
</p>
$$\\nabla \\to i\\vec{k}, \\quad \\frac{\\partial}{\\partial t} \\to -i\\omega$$

<h3>2. Phase Velocity vs Group Velocity</h3>
<p>
The speed at which surfaces of constant wave phase propagate is the <strong>phase velocity</strong> $\\vec{v}_{ph}$:
</p>
$$\\vec{v}_{ph} = \\frac{\\omega}{k} \\hat{k}$$
<p>
The speed and direction at which a modulated wave packet—and consequently physical energy and information—transmits through the plasma is the <strong>group velocity</strong> $\\vec{v}_g$:
</p>
$$\\vec{v}_g = \\nabla_k \\omega = \\frac{\\partial \\omega}{\\partial k} \\hat{k}$$
<p>
In dispersive plasma media where $\\omega(k)$ is non-linear, $v_{ph} \\ne v_g$.
</p>
"""
        },
        {
            "id": "sec-5-2",
            "number": "5.2",
            "title": "Linearization of Multi-Fluid Equations & Electrostatic Perturbations",
            "content": """
<h3>1. The Linearization Procedure</h3>
<p>
For electrostatic waves, the magnetic field perturbation vanishes ($\\vec{B}_1 = 0$), so the electric field is purely curl-free and derived from an electrostatic potential: $\\vec{E}_1 = -\\nabla \\phi_1 = -i\\vec{k}\\phi_1$.
</p>
<p>
Each fluid variable is decomposed into equilibrium plus first-order perturbation:
</p>
$$n_\\alpha = n_0 + n_{\\alpha 1}, \\quad \\vec{u}_\\alpha = 0 + \\vec{u}_{\\alpha 1}, \\quad \\vec{E} = 0 + \\vec{E}_1$$
<p>
Neglecting second-order nonlinear terms ($n_1 \\vec{u}_1 \\approx 0$ and $(\\vec{u}_1\\cdot\\nabla)\\vec{u}_1 \\approx 0$):
</p>
<ul>
  <li><strong>Linearized Continuity:</strong>
  $$-i\\omega n_{\\alpha 1} + i n_0 \\vec{k}\\cdot\\vec{u}_{\\alpha 1} = 0 \\implies n_{\\alpha 1} = n_0 \\frac{\\vec{k}\\cdot\\vec{u}_{\\alpha 1}}{\\omega}$$</li>
  <li><strong>Linearized Momentum:</strong>
  $$-i\\omega m_\\alpha n_0 \\vec{u}_{\\alpha 1} = q_\\alpha n_0 \\vec{E}_1 - \\gamma_\\alpha k_B T_\\alpha (i\\vec{k} n_{\\alpha 1})$$</li>
  <li><strong>Poisson's Equation:</strong>
  $$i\\vec{k}\\cdot\\vec{E}_1 = \\frac{e(n_{i1} - n_{e1})}{\\varepsilon_0}$$</li>
</ul>
"""
        },
        {
            "id": "sec-5-3",
            "number": "5.3",
            "title": "Cold Electron Plasma Oscillations (Langmuir Waves) & Plasma Cutoff",
            "content": """
<h3>1. The Cold Plasma Limit</h3>
<p>
In the cold plasma limit ($T_e = 0$), electron pressure vanishes. Because the oscillation frequency is high, massive ions cannot respond ($n_{i1} = 0, \\vec{u}_{i1} = 0$). The linearized electron momentum equation reduces to:
</p>
$$-i\\omega m_e \\vec{u}_{e1} = -e \\vec{E}_1 \\implies \\vec{u}_{e1} = \\frac{e}{i\\omega m_e}\\vec{E}_1$$
<p>
Substitute $\\vec{u}_{e1}$ into continuity:
</p>
$$n_{e1} = n_0 \\frac{\\vec{k}\\cdot\\vec{u}_{e1}}{\\omega} = \\frac{n_0 e}{i\\omega^2 m_e}\\vec{k}\\cdot\\vec{E}_1$$
<p>
Substitute $n_{e1}$ into Poisson's equation $i\\vec{k}\\cdot\\vec{E}_1 = -\\frac{e n_{e1}}{\\varepsilon_0}$:
</p>
$$i\\vec{k}\\cdot\\vec{E}_1 = -\\frac{e}{\\varepsilon_0}\\left( \\frac{n_0 e}{i\\omega^2 m_e}\\vec{k}\\cdot\\vec{E}_1 \\right) = \\frac{n_0 e^2}{\\varepsilon_0 m_e \\omega^2} (i\\vec{k}\\cdot\\vec{E}_1)$$
<p>
For a non-trivial wave solution ($\\vec{k}\\cdot\\vec{E}_1 \\ne 0$):
</p>
$$1 - \\frac{n_0 e^2}{\\varepsilon_0 m_e \\omega^2} = 0 \\implies \\omega^2 = \\frac{n_0 e^2}{\\varepsilon_0 m_e} \\equiv \\omega_{pe}^2$$
<p>
In a cold plasma, electron oscillations occur at the single constant frequency $\\omega = \\omega_{pe}$, independent of wavevector $k$. Consequently:
</p>
$$v_g = \\frac{d\\omega}{dk} = 0$$
<p>
Cold electron plasma oscillations do not propagate; they are purely local stationary oscillations!
</p>
"""
        },
        {
            "id": "sec-5-4",
            "number": "5.4",
            "title": "Thermal Electron Pressure & Derivation of the Bohm-Gross Dispersion Relation",
            "content": """
<h3>1. Thermal Pressure Correction</h3>
<p>
When electron temperature is non-zero ($T_e > 0$), thermal pressure $\\nabla P_{e1} = \\gamma_e k_B T_e \\nabla n_{e1}$ provides an additional restoring force. For one-dimensional high-frequency compressions along $\\vec{k}$, there is only one translational degree of freedom ($d=1$), so the adiabatic index is $\\gamma_e = (d+2)/d = 3$.
</p>
<p>
The linearized electron momentum equation becomes:
</p>
$$-i\\omega m_e n_0 u_{e1} = -e n_0 E_1 - 3 k_B T_e (i k n_{e1})$$
<p>
Using continuity $n_{e1} = n_0 \\frac{k u_{e1}}{\\omega}$:
</p>
$$-i\\omega m_e u_{e1} = -e E_1 - 3 k_B T_e i k \\left( \\frac{k u_{e1}}{\\omega} \\right) \\implies u_{e1}\\left( -i\\omega + \\frac{3 k_B T_e i k^2}{\\omega m_e} \\right) = -\\frac{e}{m_e} E_1$$
$$u_{e1} = \\frac{e E_1}{i m_e \\omega} \\left( 1 - \\frac{3 k^2 v_{\\text{th},e}^2}{\\omega^2} \\right)^{-1}$$
<p>
where $v_{\\text{th},e} = \\sqrt{k_B T_e / m_e}$ is the electron thermal speed.
</p>

<h3>2. The Bohm-Gross Dispersion Relation</h3>
<p>
Substituting $n_{e1}$ into Poisson's equation $i k E_1 = -\\frac{e n_{e1}}{\\varepsilon_0} = -\\frac{e n_0 k u_{e1}}{\\varepsilon_0 \\omega}$:
</p>
$$1 - \\frac{\\omega_{pe}^2}{\\omega^2 - 3 k^2 v_{\\text{th},e}^2} = 0 \\implies \\omega^2 = \\omega_{pe}^2 + 3 k^2 v_{\\text{th},e}^2$$
<p>
This is the famous <strong>Bohm-Gross dispersion relation</strong> for warm electron plasma waves (Langmuir waves).
</p>
<p>
Differentiating with respect to $k$ yields a non-zero group velocity:
</p>
$$2\\omega \\frac{d\\omega}{dk} = 6 k v_{\\text{th},e}^2 \\implies v_g = \\frac{3 k v_{\\text{th},e}^2}{\\omega} = \\frac{3 v_{\\text{th},e}^2}{v_{ph}}$$
<p>
Thermal pressure allows electron plasma waves to propagate and carry energy across the plasma!
</p>
"""
        },
        {
            "id": "sec-5-5",
            "number": "5.5",
            "title": "Ion Acoustic Waves (Plasma Sound Waves): Derivation & Sound Speed c_s",
            "content": """
<h3>1. Low-Frequency Dynamics</h3>
<p>
At low frequencies ($\\omega \\ll \\omega_{pe}$), electrons move so rapidly compared to the wave that they remain in continuous thermodynamic equilibrium, establishing a Boltzmann distribution in the wave potential $\\phi_1$:
</p>
$$n_{e1} = n_0 \\frac{e \\phi_1}{k_B T_e}$$
<p>
The heavy ions, however, are accelerated dynamically by the wave electric field $E_1 = -ik\\phi_1$. Linearized ion continuity and momentum equations with ion temperature $T_i$:
</p>
$$-i\\omega n_{i1} + i n_0 k u_{i1} = 0 \\implies n_{i1} = n_0 \\frac{k u_{i1}}{\\omega}$$
$$-i\\omega M_i n_0 u_{i1} = e n_0 (-i k \\phi_1) - \\gamma_i k_B T_i (i k n_{i1})$$
<p>
Solving for ion density perturbation $n_{i1}$:
</p>
$$n_{i1} = \\frac{n_0 e k^2}{M_i (\\omega^2 - \\gamma_i k^2 v_{\\text{th},i}^2)} \\phi_1$$

<h3>2. The Ion Acoustic Dispersion Relation</h3>
<p>
Substituting $n_{e1}$ and $n_{i1}$ into Poisson's equation $k^2 \\phi_1 = \\frac{e(n_{i1} - n_{e1})}{\\varepsilon_0}$:
</p>
$$k^2 \\phi_1 = \\frac{e}{\\varepsilon_0}\\left[ \\frac{n_0 e k^2}{M_i (\\omega^2 - \\gamma_i k^2 v_{\\text{th},i}^2)}\\phi_1 - \\frac{n_0 e \\phi_1}{k_B T_e} \\right]$$
<p>
Dividing by $\\phi_1$ and using $\\lambda_{De}^2 = \\frac{\\varepsilon_0 k_B T_e}{n_0 e^2}$ and $\\omega_{pi}^2 = \\frac{n_0 e^2}{\\varepsilon_0 M_i}$:
</p>
$$k^2 + \\frac{1}{\\lambda_{De}^2} = \\frac{\\omega_{pi}^2 k^2}{\\omega^2 - \\gamma_i k^2 v_{\\text{th},i}^2}$$
<p>
For cold ions ($T_i \\ll T_e$):
</p>
$$\\omega^2 = \\frac{k^2 \\omega_{pi}^2 \\lambda_{De}^2}{1 + k^2 \\lambda_{De}^2}$$
<p>
Noting that $\\omega_{pi} \\lambda_{De} = \\sqrt{\\frac{n_0 e^2}{\\varepsilon_0 M_i}}\\sqrt{\\frac{\\varepsilon_0 k_B T_e}{n_0 e^2}} = \\sqrt{\\frac{k_B T_e}{M_i}} \\equiv c_s$, where $c_s$ is the <strong>ion sound speed</strong>:
</p>
$$\\omega^2 = \\frac{k^2 c_s^2}{1 + k^2 \\lambda_{De}^2}$$
<p>
Including finite ion temperature ($T_i > 0$ with 1D adiabatic compression $\gamma_i = 3$):
</p>
$$c_s = \\sqrt{\\frac{k_B T_e + 3 k_B T_i}{M_i}}$$
"""
        },
        {
            "id": "sec-5-6",
            "number": "5.6",
            "title": "Acoustic-to-Ion-Plasma Transition (k lambda_D ~ 1) & Electron vs Ion Waves",
            "content": """
<h3>1. Limiting Regimes of Ion Acoustic Waves</h3>
<p>
The ion acoustic dispersion relation exhibits two fundamentally distinct physical behaviors depending on wavelength relative to the Debye length:
</p>
<ol>
  <li><strong>Long-Wavelength Acoustic Limit ($k \\lambda_{De} \\ll 1$, $\\lambda \\gg \\lambda_{De}$):</strong>
  $$\\omega \\approx k c_s, \\quad v_{ph} = v_g = c_s = \\text{const}$$
  The wave is non-dispersive and behaves identically to an ordinary acoustic sound wave in neutral gas. In this limit, electrons perfectly shield ion charge fluctuations, maintaining quasi-neutrality ($n_{e1} \\approx n_{i1}$).</li>
  <li><strong>Short-Wavelength Ion Plasma Limit ($k \\lambda_{De} \\gg 1$, $\\lambda \\ll \\lambda_{De}$):</strong>
  $$\\omega \\approx \\frac{k c_s}{k \\lambda_{De}} = \\frac{c_s}{\\lambda_{De}} = \\omega_{pi}$$
  At wavelengths shorter than the Debye length, electron Debye shielding breaks down completely. The electrons can no longer cluster to screen the ions, and the wave degenerates into constant-frequency <strong>ion plasma oscillations</strong> at $\\omega = \\omega_{pi}$, with zero group velocity ($v_g \\to 0$).</li>
</ol>

<h3>2. Fundamental Comparison: Electron Waves vs Ion Waves</h3>
<table style="width:100%; border-collapse: collapse; margin-top: 1rem;">
  <thead>
    <tr style="border-bottom: 2px solid #334155; color: #38bdf8;">
      <th style="padding: 0.5rem; text-align: left;">Feature</th>
      <th style="padding: 0.5rem; text-align: left;">Electron Plasma Wave (Langmuir)</th>
      <th style="padding: 0.5rem; text-align: left;">Ion Acoustic Wave (Sound)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #1e293b;">
      <td style="padding: 0.5rem;"><strong>Restoring Force</strong></td>
      <td style="padding: 0.5rem;">Electric field + Electron thermal pressure</td>
      <td style="padding: 0.5rem;">Electron thermal pressure ($T_e$)</td>
    </tr>
    <tr style="border-bottom: 1px solid #1e293b;">
      <td style="padding: 0.5rem;"><strong>Inertia</strong></td>
      <td style="padding: 0.5rem;">Electron mass $m_e$</td>
      <td style="padding: 0.5rem;">Ion mass $M_i$</td>
    </tr>
    <tr style="border-bottom: 1px solid #1e293b;">
      <td style="padding: 0.5rem;"><strong>Characteristic Frequency</strong></td>
      <td style="padding: 0.5rem;">High ($\\omega \\ge \\omega_{pe} \\sim 10^{11}\\text{ rad/s}$)</td>
      <td style="padding: 0.5rem;">Low ($\\omega \\le \\omega_{pi} \\sim 10^9\\text{ rad/s}$)</td>
    </tr>
    <tr>
      <td style="padding: 0.5rem;"><strong>Ion Motion</strong></td>
      <td style="padding: 0.5rem;">Stationary neutralizing background</td>
      <td style="padding: 0.5rem;">Oscillating fluid elements</td>
    </tr>
  </tbody>
</table>
"""
        },
        {
            "id": "sec-5-7",
            "number": "5.7",
            "title": "Electrostatic Waves in Magnetized Plasmas: Upper Hybrid, Lower Hybrid & EIC Waves",
            "content": """
<h3>1. Waves Propagating Perpendicular to B0: Upper Hybrid Oscillations</h3>
<p>
When a static magnetic field $\\vec{B}_0 = B_0 \\hat{z}$ is present, consider electrostatic electron waves propagating perpendicular to the field ($\\vec{k} = k \\hat{x} \\perp \\vec{B}_0$).
</p>
<p>
The electrons experience two restoring forces simultaneously:
</p>
<ul>
  <li>The electrostatic space-charge restoring force ($-\\omega_{pe}^2$).</li>
  <li>The magnetic Lorentz force restoring gyration ($-\\omega_{ce}^2$).</li>
</ul>
<p>
Solving the linearized electron equations of motion yields the <strong>Upper Hybrid frequency</strong> $\\omega_{UH}$:
</p>
$$\\omega^2 = \\omega_{UH}^2 = \\omega_{pe}^2 + \\omega_{ce}^2$$
<p>
Including electron thermal pressure: $\\omega^2 = \\omega_{UH}^2 + 3 k^2 v_{\\text{th},e}^2$.
</p>

<h3>2. Lower Hybrid Oscillations</h3>
<p>
When both electron and ion motions are included for perpendicular propagation, an intermediate resonance occurs between the electron and ion cyclotron frequencies, termed the <strong>Lower Hybrid frequency</strong> $\\omega_{LH}$:
</p>
$$\\frac{1}{\\omega_{LH}^2} = \\frac{1}{\\omega_{pi}^2 + \\omega_{ci}^2} + \\frac{1}{\\omega_{ce}\\omega_{ci}} \\implies \\omega_{LH} \\approx \\sqrt{\\omega_{ce}\\omega_{ci}}$$

<h3>3. Electrostatic Ion Cyclotron (EIC) Waves</h3>
<p>
For waves propagating at an oblique angle nearly perpendicular to $\\vec{B}_0$ ($k_\\perp \\gg k_\\parallel$) with frequencies near the ion cyclotron frequency $\\omega \\sim \\omega_{ci}$:
</p>
$$\\omega^2 = \\omega_{ci}^2 + k_\\perp^2 c_s^2$$
<p>
These <strong>electrostatic ion cyclotron (EIC) waves</strong> are driven by parallel electron currents and play a major role in auroral ion heating and tokamak scrape-off layers.
</p>
"""
        }
    ],
    "problems": [
        {
            "id": "plasma-prob-5-1",
            "title": "Complete Linearized Fluid Derivation of the Bohm-Gross Dispersion Relation with 1D Adiabatic Pressure",
            "statement": """Derive the Bohm-Gross dispersion relation for high-frequency electron plasma waves from the linearized 1D multi-fluid equations.
(a) Write down the linearized continuity, momentum, and Poisson equations for 1D perturbations along $\\hat{x}$ with isothermal/adiabatic index $\\gamma_e = 3$.
(b) Eliminate $u_{e1}$ and $n_{e1}$ to derive the algebraic wave equation in terms of $E_1$.
(c) Deduce the Bohm-Gross dispersion relation $\\omega^2 = \\omega_{pe}^2 + 3 k^2 v_{\\text{th},e}^2$, calculate the phase velocity $v_{ph}$ and group velocity $v_g$, and show that $v_{ph} v_g = 3 v_{\\text{th},e}^2$ in the limit $k\\lambda_D \\ll 1$.""",
            "solution": """**(a) Linearized 1D Fluid Equations:**
Consider 1D perturbations $\\propto e^{i(kx - \\omega t)}$ in unmagnetized plasma with stationary ions:
1. Linearized electron continuity:
$$\\frac{\\partial n_{e1}}{\\partial t} + n_0 \\frac{\\partial u_{e1}}{\\partial x} = 0 \\implies -i\\omega n_{e1} + i k n_0 u_{e1} = 0 \\implies n_{e1} = n_0 \\frac{k u_{e1}}{\\omega}$$
2. Linearized electron momentum with 1D adiabatic pressure $\\nabla P_{e1} = 3 k_B T_e \\nabla n_{e1}$:
$$m_e n_0 \\frac{\\partial u_{e1}}{\\partial t} = -e n_0 E_1 - \\frac{\\partial P_{e1}}{\\partial x} = -e n_0 E_1 - 3 k_B T_e \\frac{\\partial n_{e1}}{\\partial x}$$
$$-i\\omega m_e n_0 u_{e1} = -e n_0 E_1 - 3 k_B T_e (i k n_{e1})$$
3. Poisson's equation:
$$\\varepsilon_0 \\frac{\\partial E_1}{\\partial x} = -e n_{e1} \\implies i k \\varepsilon_0 E_1 = -e n_{e1}$$

**(b) Elimination & Wave Equation:**
Substitute $n_{e1}$ from continuity into momentum:
$$-i\\omega m_e n_0 u_{e1} = -e n_0 E_1 - 3 k_B T_e i k \\left( n_0 \\frac{k u_{e1}}{\\omega} \\right) = -e n_0 E_1 - \\frac{3 k_B T_e n_0 k^2}{\\omega} i u_{e1}$$
Rearrange to group $u_{e1}$ terms:
$$-i u_{e1}\\left( m_e n_0 \\omega - \\frac{3 k_B T_e n_0 k^2}{\\omega} \\right) = -e n_0 E_1$$
Multiply by $\\omega / n_0$:
$$-i u_{e1}\\left( m_e \\omega^2 - 3 k_B T_e k^2 \\right) = -e \\omega E_1 \\implies u_{e1} = \\frac{-i e \\omega E_1}{m_e \\omega^2 - 3 k_B T_e k^2}$$
Now express $n_{e1}$ in terms of $E_1$:
$$n_{e1} = n_0 \\frac{k u_{e1}}{\\omega} = -\\frac{i n_0 e k E_1}{m_e \\omega^2 - 3 k_B T_e k^2}$$
Substitute $n_{e1}$ into Poisson's equation $i k \\varepsilon_0 E_1 = -e n_{e1}$:
$$i k \\varepsilon_0 E_1 = -e \\left( -\\frac{i n_0 e k E_1}{m_e \\omega^2 - 3 k_B T_e k^2} \\right) = \\frac{i n_0 e^2 k E_1}{m_e \\omega^2 - 3 k_B T_e k^2}$$
For non-trivial wave amplitude ($E_1 \\ne 0$):
$$\\varepsilon_0 = \\frac{n_0 e^2}{m_e \\omega^2 - 3 k_B T_e k^2} \\implies 1 = \\frac{n_0 e^2 / (\\varepsilon_0 m_e)}{\\omega^2 - \\frac{3 k_B T_e}{m_e} k^2}$$

**(c) Bohm-Gross Relation & Velocity Analysis:**
Recognizing $\\omega_{pe}^2 = \\frac{n_0 e^2}{\\varepsilon_0 m_e}$ and $v_{\\text{th},e}^2 = \\frac{k_B T_e}{m_e}$:
$$1 = \\frac{\\omega_{pe}^2}{\\omega^2 - 3 k^2 v_{\\text{th},e}^2} \\implies \\omega^2 = \\omega_{pe}^2 + 3 k^2 v_{\\text{th},e}^2$$
This is the **Bohm-Gross dispersion relation**.
1. **Phase Velocity:**
$$v_{ph} = \\frac{\\omega}{k} = \\frac{\\sqrt{\\omega_{pe}^2 + 3 k^2 v_{\\text{th},e}^2}}{k} = \\sqrt{\\frac{\\omega_{pe}^2}{k^2} + 3 v_{\\text{th},e}^2}$$
In the long-wavelength limit ($k \\lambda_D \\ll 1$, where $\\lambda_D = v_{\\text{th},e}/\\omega_{pe}$):
$$v_{ph} \\approx \\frac{\\omega_{pe}}{k} \\gg v_{\\text{th},e}$$
2. **Group Velocity:**
Differentiating $\\omega^2 = \\omega_{pe}^2 + 3 k^2 v_{\\text{th},e}^2$ with respect to $k$:
$$2\\omega \\frac{d\\omega}{dk} = 6 k v_{\\text{th},e}^2 \\implies v_g = \\frac{d\\omega}{dk} = \\frac{3 k v_{\\text{th},e}^2}{\\omega}$$
3. **Product $v_{ph} v_g$:**
$$v_{ph} v_g = \\left( \\frac{\\omega}{k} \\right)\\left( \\frac{3 k v_{\\text{th},e}^2}{\\omega} \\right) = 3 v_{\\text{th},e}^2$$
This product is strictly independent of frequency and wavevector! In the long-wavelength limit where $v_{ph} \\to \\infty$, the group velocity $v_g \\to 0$, ensuring causality is preserved."""
        },
        {
            "id": "plasma-prob-5-2",
            "title": "Derivation of the Ion Acoustic Dispersion Relation with Finite Ion Temperature and Electron Screening",
            "statement": """Consider low-frequency electrostatic waves in a two-component plasma with electron temperature $T_e$ and ion temperature $T_i$.
(a) From the linearized fluid equations, derive the general ion acoustic dispersion relation:
$$\\omega^2 = \\frac{k^2 c_s^2}{1 + k^2 \\lambda_{De}^2} + \\gamma_i k^2 v_{\\text{th},i}^2$$
(b) For an argon plasma ($M_i = 40\\text{ amu} = 6.64 \\times 10^{-26}\\text{ kg}$) with $k_B T_e = 3.0\\text{ eV}$ and $k_B T_i = 0.10\\text{ eV}$ at density $n_0 = 10^{16}\\text{ m}^{-3}$, calculate the ion sound speed $c_s$ and the Debye length $\\lambda_{De}$.
(c) Evaluate the wave frequency $f = \\omega / (2\\pi)$ and phase velocity $v_{ph}$ at two distinct wavelengths: $\\lambda_1 = 10.0\\text{ cm}$ and $\\lambda_2 = 0.50\\text{ mm}$.""",
            "solution": """**(a) Derivation of General Ion Acoustic Dispersion:**
For low frequencies ($\\omega \\ll \\omega_{pe}$), electrons obey the Boltzmann distribution:
$$n_{e1} = n_0 \\frac{e\\phi_1}{k_B T_e}$$
For ions, linearized continuity and momentum equations with 1D adiabatic compression $\\gamma_i = 3$:
$$-i\\omega n_{i1} + i n_0 k u_{i1} = 0 \\implies u_{i1} = \\frac{\\omega}{k}\\frac{n_{i1}}{n_0}$$
$$-i\\omega M_i n_0 u_{i1} = -e n_0 (i k \\phi_1) - 3 k_B T_i (i k n_{i1})$$
Substitute $u_{i1}$:
$$-i\\omega M_i n_0 \\left( \\frac{\\omega}{k}\\frac{n_{i1}}{n_0} \\right) = -i e n_0 k \\phi_1 - 3 i k_B T_i k n_{i1}$$
$$-i M_i \\frac{\\omega^2}{k} n_{i1} + 3 i k_B T_i k n_{i1} = -i e n_0 k \\phi_1$$
Multiply by $i k / M_i$:
$$(\\omega^2 - 3 k^2 v_{\\text{th},i}^2) n_{i1} = \\frac{n_0 e k^2}{M_i}\\phi_1 \\implies n_{i1} = \\frac{n_0 e k^2 \\phi_1}{M_i (\\omega^2 - 3 k^2 v_{\\text{th},i}^2)}$$
Substitute $n_{e1}$ and $n_{i1}$ into Poisson's equation $k^2 \\phi_1 = \\frac{e(n_{i1} - n_{e1})}{\\varepsilon_0}$:
$$k^2 \\phi_1 = \\frac{e^2 n_0}{\\varepsilon_0}\\left[ \\frac{k^2 \\phi_1}{M_i (\\omega^2 - 3 k^2 v_{\\text{th},i}^2)} - \\frac{\\phi_1}{k_B T_e} \\right]$$
Divide by $\\phi_1$ and use $\\omega_{pi}^2 = \\frac{n_0 e^2}{\\varepsilon_0 M_i}$ and $\\frac{1}{\\lambda_{De}^2} = \\frac{n_0 e^2}{\\varepsilon_0 k_B T_e}$:
$$k^2 + \\frac{1}{\\lambda_{De}^2} = \\frac{\\omega_{pi}^2 k^2}{\\omega^2 - 3 k^2 v_{\\text{th},i}^2}$$
Rearranging:
$$\\omega^2 - 3 k^2 v_{\\text{th},i}^2 = \\frac{\\omega_{pi}^2 k^2}{k^2 + 1/\\lambda_{De}^2} = \\frac{\\omega_{pi}^2 \\lambda_{De}^2 k^2}{1 + k^2 \\lambda_{De}^2} = \\frac{k^2 c_s^2}{1 + k^2 \\lambda_{De}^2}$$
where $c_s = \\omega_{pi} \\lambda_{De} = \\sqrt{\\frac{k_B T_e}{M_i}}$.
$$\\omega^2 = \\frac{k^2 c_s^2}{1 + k^2 \\lambda_{De}^2} + 3 k^2 v_{\\text{th},i}^2$$

**(b) Numerical Calculation of $c_s$ and $\\lambda_{De}$:**
Given:
$k_B T_e = 3.0\\text{ eV} = 3.0 \\times 1.6022\\times 10^{-19}\\text{ J} = 4.807\\times 10^{-19}\\text{ J}$
$M_i = 40 \\times 1.6605\\times 10^{-27}\\text{ kg} = 6.642 \\times 10^{-26}\\text{ kg}$
Ion sound speed:
$$c_s = \\sqrt{\\frac{k_B T_e}{M_i}} = \\sqrt{\\frac{4.807\\times 10^{-19}}{6.642\\times 10^{-26}}} = \\sqrt{7.237\\times 10^6} \\approx 2.690 \\times 10^3\\text{ m/s} = 2.69\\text{ km/s}$$
Debye length:
$$\\lambda_{De} = \\sqrt{\\frac{\\varepsilon_0 k_B T_e}{n_0 e^2}} = 7434 \\sqrt{\\frac{3.0}{10^{16}}} = 7434 \\times (1.732 \\times 10^{-8}) = 1.288 \\times 10^{-4}\\text{ m} = 0.129\\text{ mm}$$

**(c) Evaluation at Two Wavelengths:**
1. **For $\\lambda_1 = 10.0\\text{ cm} = 0.10\\text{ m}$:**
$$k_1 = \\frac{2\\pi}{\\lambda_1} = \\frac{2\\pi}{0.10} = 62.83\\text{ m}^{-1}$$
$$k_1 \\lambda_{De} = 62.83 \\times 1.288\\times 10^{-4} = 8.09 \\times 10^{-3} \\ll 1$$
Here $k_1 \\lambda_{De} \\ll 1$, so the wave is in the pure acoustic regime:
$$v_{ph,1} \\approx c_s = 2.690\\times 10^3\\text{ m/s}$$
$$f_1 = \\frac{v_{ph,1}}{\\lambda_1} = \\frac{2690\\text{ m/s}}{0.10\\text{ m}} = 2.69 \\times 10^4\\text{ Hz} = 26.9\\text{ kHz}$$

2. **For $\\lambda_2 = 0.50\\text{ mm} = 5.0\\times 10^{-4}\\text{ m}$:**
$$k_2 = \\frac{2\\pi}{5.0\\times 10^{-4}} = 12,566\\text{ m}^{-1}$$
$$k_2 \\lambda_{De} = 12566 \\times 1.288\\times 10^{-4} = 1.619$$
Since $k_2 \\lambda_{De} \\sim 1$, dispersion is significant:
$$\\omega_2 = \\frac{k_2 c_s}{\\sqrt{1 + (k_2 \\lambda_{De})^2}} = \\frac{12566 \\times 2690}{\\sqrt{1 + (1.619)^2}} = \\frac{3.380\\times 10^7}{\\sqrt{1 + 2.621}} = \\frac{3.380\\times 10^7}{1.903} = 1.776 \\times 10^7\\text{ rad/s}$$
$$f_2 = \\frac{\\omega_2}{2\\pi} = \\frac{1.776\\times 10^7}{2\\pi} \\approx 2.827 \\times 10^6\\text{ Hz} = 2.83\\text{ MHz}$$
$$v_{ph,2} = \\frac{\\omega_2}{k_2} = \\frac{1.776\\times 10^7}{12566} = 1.413 \\times 10^3\\text{ m/s} = 1.41\\text{ km/s}$$
Notice that $v_{ph,2}$ is substantially lower than $c_s$ (1.41 km/s vs 2.69 km/s), demonstrating the dispersive roll-off toward the ion plasma frequency."""
        },
        {
            "id": "plasma-prob-5-3",
            "title": "Electrostatic Ion Cyclotron (EIC) Wave Dispersion and Resonance in Magnetized Geometry",
            "statement": """Consider electrostatic waves in a magnetized plasma with $\\vec{B}_0 = B_0 \\hat{z}$ propagating at an oblique angle nearly perpendicular to the magnetic field ($k_\\perp \\gg k_\\parallel$) with wavevector $\\vec{k} = k_\\perp \\hat{x} + k_\\parallel \\hat{z}$.
(a) Assuming electrons respond isothermally along the magnetic field to satisfy the parallel Boltzmann relation $n_{e1} = n_0 \\frac{e\\phi_1}{k_B T_e}$, and treating ions via magnetized fluid momentum equations with cyclotron frequency $\\omega_{ci}$, derive the Electrostatic Ion Cyclotron (EIC) wave dispersion relation:
$$\\omega^2 = \\omega_{ci}^2 + k_\\perp^2 c_s^2$$
(b) In a fusion tokamak edge plasma where $B_0 = 3.0\\text{ Tesla}$, deuterium ions ($M_i = 3.34\\times 10^{-27}\\text{ kg}$), and $k_B T_e = 50\\text{ eV}$, compute the ion cyclotron frequency $f_{ci}$ and the EIC wave frequency for perpendicular wavelength $\\lambda_\\perp = 2.0\\text{ cm}$.""",
            "solution": """**(a) Derivation of EIC Dispersion Relation:**
Let the electrostatic potential perturbation be $\\phi_1(x, z, t) = \\phi_1 e^{i(k_\\perp x + k_\\parallel z - \\omega t)}$.
1. **Electron Response:**
Because electrons move rapidly along field lines ($v_{\\text{th},e} \\gg \\omega / k_\\parallel$), they shield the parallel electric field $E_z = -i k_\\parallel \\phi_1$ adiabatically:
$$n_{e1} = n_0 \\frac{e\\phi_1}{k_B T_e}$$
2. **Ion Dynamics:**
For cold ions ($T_i \\approx 0$), the linearized ion momentum equation in $\\vec{B}_0 = B_0 \\hat{z}$ is:
$$-i\\omega M_i \\vec{u}_{i1} = e(-\\nabla\\phi_1 + \\vec{u}_{i1}\\times\\vec{B}_0)$$
Resolving into Cartesian components:
$$-i\\omega M_i u_{ix} = -e (i k_\\perp \\phi_1) + e B_0 u_{iy}$$
$$-i\\omega M_i u_{iy} = -e B_0 u_{ix}$$
$$-i\\omega M_i u_{iz} = -e (i k_\\parallel \\phi_1)$$
From the $y$-equation: $u_{iy} = \\frac{e B_0}{i\\omega M_i} u_{ix} = \\frac{\\omega_{ci}}{i\\omega} u_{ix}$, where $\\omega_{ci} = \\frac{e B_0}{M_i}$.
Substitute $u_{iy}$ into the $x$-equation:
$$-i\\omega M_i u_{ix} = -i e k_\\perp \\phi_1 + e B_0 \\left( \\frac{\\omega_{ci}}{i\\omega} u_{ix} \\right) = -i e k_\\perp \\phi_1 - i \\frac{M_i \\omega_{ci}^2}{\\omega} u_{ix}$$
Multiply by $i\\omega / M_i$:
$$\\omega^2 u_{ix} = \\frac{e k_\\perp \\omega}{M_i} \\phi_1 + \\omega_{ci}^2 u_{ix} \\implies (\\omega^2 - \\omega_{ci}^2) u_{ix} = \\frac{e k_\\perp \\omega}{M_i}\\phi_1$$
$$u_{ix} = \\frac{e k_\\perp \\omega}{M_i (\\omega^2 - \\omega_{ci}^2)}\\phi_1$$
From the ion continuity equation:
$$-i\\omega n_{i1} + i n_0 (k_\\perp u_{ix} + k_\\parallel u_{iz}) = 0$$
Since $k_\\perp \\gg k_\\parallel$, the perpendicular divergence dominates ($k_\\perp u_{ix} \\gg k_\\parallel u_{iz}$):
$$n_{i1} \\approx n_0 \\frac{k_\\perp u_{ix}}{\\omega} = \\frac{n_0 e k_\\perp^2}{M_i (\\omega^2 - \\omega_{ci}^2)}\\phi_1$$
In a dense plasma with $k_\\perp \\lambda_D \\ll 1$, quasi-neutrality requires $n_{e1} \\approx n_{i1}$:
$$n_0 \\frac{e\\phi_1}{k_B T_e} = \\frac{n_0 e k_\\perp^2}{M_i (\\omega^2 - \\omega_{ci}^2)}\\phi_1$$
Canceling $n_0 e \\phi_1$:
$$\\frac{1}{k_B T_e} = \\frac{k_\\perp^2}{M_i (\\omega^2 - \\omega_{ci}^2)} \\implies \\omega^2 - \\omega_{ci}^2 = \\frac{k_B T_e}{M_i} k_\\perp^2 = c_s^2 k_\\perp^2$$
$$\\omega^2 = \\omega_{ci}^2 + k_\\perp^2 c_s^2$$
This is the **Electrostatic Ion Cyclotron (EIC)** dispersion relation.

**(b) Numerical Evaluation in Tokamak Edge:**
Given:
$B_0 = 3.0\\text{ T}$, $M_i = 3.344\\times 10^{-27}\\text{ kg}$ (deuteron)
$k_B T_e = 50\\text{ eV} = 50 \\times 1.6022\\times 10^{-19}\\text{ J} = 8.011\\times 10^{-18}\\text{ J}$
$\\lambda_\\perp = 0.02\\text{ m} \\implies k_\\perp = \\frac{2\\pi}{0.02} = 314.16\\text{ m}^{-1}$

1. **Ion Cyclotron Frequency:**
$$\\omega_{ci} = \\frac{e B_0}{M_i} = \\frac{(1.6022\\times 10^{-19})(3.0)}{3.344\\times 10^{-27}} = 1.437 \\times 10^8\\text{ rad/s}$$
$$f_{ci} = \\frac{\\omega_{ci}}{2\\pi} = \\frac{1.437\\times 10^8}{2\\pi} \\approx 2.288 \\times 10^7\\text{ Hz} = 22.88\\text{ MHz}$$

2. **Ion Sound Speed:**
$$c_s = \\sqrt{\\frac{k_B T_e}{M_i}} = \\sqrt{\\frac{8.011\\times 10^{-18}}{3.344\\times 10^{-27}}} = \\sqrt{2.396\\times 10^9} \\approx 4.895 \\times 10^4\\text{ m/s} = 48.95\\text{ km/s}$$

3. **EIC Wave Frequency:**
$$k_\\perp c_s = (314.16\\text{ m}^{-1})(4.895\\times 10^4\\text{ m/s}) = 1.538 \\times 10^7\\text{ rad/s}$$
$$\\omega = \\sqrt{\\omega_{ci}^2 + (k_\\perp c_s)^2} = \\sqrt{(1.437\\times 10^8)^2 + (1.538\\times 10^7)^2} = \\sqrt{2.065\\times 10^{16} + 2.365\\times 10^{14}} = \\sqrt{2.089\\times 10^{16}}$$
$$\\omega = 1.445 \\times 10^8\\text{ rad/s}$$
$$f = \\frac{\\omega}{2\\pi} = 2.300 \\times 10^7\\text{ Hz} = 23.00\\text{ MHz}$$
The thermal pressure shifts the oscillation frequency slightly above the fundamental cyclotron resonance by $\\approx 0.12\\text{ MHz}$."""
        }
    ]
}

# =========================================================================
# UNIT 6: ELECTROMAGNETIC WAVES IN MAGNETIZED PLASMAS & DIELECTRIC TENSOR
# =========================================================================

unit6_data = {
    "unitId": "unit6-plasma",
    "title": "Electromagnetic Waves in Magnetized Plasmas & Dielectric Tensor",
    "subtitle": "Cutoffs, Resonances, Whistler Modes, Faraday Rotation & CMA Diagram",
    "summary": "Rigorous electrodynamics of transverse waves in cold and magnetized plasmas: electromagnetic wave equation in unmagnetized plasma, dispersion relation, plasma cutoff frequency, evanescent skin depth, reflection from planetary ionospheres, cold plasma dielectric tensor in Stix notation (R, L, P, S, D), parallel propagation with Left-Hand (L) and Right-Hand (R) circular polarization, electron and ion cyclotron resonances, atmospheric whistler (helicon) waves, cosmic Faraday rotation, perpendicular propagation with Ordinary (O-mode) and Extraordinary (X-mode) waves, Upper Hybrid resonance, and the Clemmow-Mullaly-Allis (CMA) mode classification diagram.",
    "sections": [
        {
            "id": "sec-6-1",
            "number": "6.1",
            "title": "Electromagnetic Waves in Unmagnetized Plasma: Transverse Wave Equation & Index of Refraction",
            "content": """
<h3>1. Maxwell's Wave Equation in Plasma</h3>
<p>
Transverse electromagnetic waves possess oscillating electric and magnetic fields perpendicular to the wavevector ($\\vec{k}\\cdot\\vec{E}_1 = 0, \\vec{k}\\cdot\\vec{B}_1 = 0$). Taking the curl of Faraday's law $\\nabla \\times \\vec{E} = -\\frac{\\partial \\vec{B}}{\\partial t}$ and substituting the Ampère-Maxwell law $\\nabla \\times \\vec{B} = \\mu_0 \\vec{J} + \\frac{1}{c^2}\\frac{\\partial \\vec{E}}{\\partial t}$:
</p>
$$\\nabla \\times (\\nabla \\times \\vec{E}_1) = -\\mu_0 \\frac{\\partial \\vec{J}_1}{\\partial t} - \\frac{1}{c^2}\\frac{\\partial^2 \\vec{E}_1}{\\partial t^2}$$
<p>
Using the vector identity $\\nabla \\times (\\nabla \\times \\vec{E}_1) = \\nabla(\\nabla\\cdot\\vec{E}_1) - \\nabla^2 \\vec{E}_1 = -\\nabla^2 \\vec{E}_1$ for transverse waves:
</p>
$$\\nabla^2 \\vec{E}_1 - \\frac{1}{c^2}\\frac{\\partial^2 \\vec{E}_1}{\\partial t^2} = \\mu_0 \\frac{\\partial \\vec{J}_1}{\\partial t}$$
<p>
Assuming harmonic plane waves $\\propto e^{i(\\vec{k}\\cdot\\vec{r} - \\omega t)}$:
</p>
$$-k^2 \\vec{E}_1 + \\frac{\\omega^2}{c^2}\\vec{E}_1 = -i\\omega \\mu_0 \\vec{J}_1$$

<h3>2. Dispersion Relation & Refractive Index</h3>
<p>
In a cold unmagnetized plasma, the high-frequency electron current is $\\vec{J}_1 = -e n_0 \\vec{u}_{e1}$. From the linearized electron momentum equation $m_e(-i\\omega)\\vec{u}_{e1} = -e\\vec{E}_1$:
</p>
$$\\vec{J}_1 = -e n_0 \\left( \\frac{e}{i\\omega m_e}\\vec{E}_1 \\right) = i \\frac{n_0 e^2}{\\omega m_e}\\vec{E}_1$$
<p>
Substituting $\\vec{J}_1$ into the wave equation and using $\\mu_0 = 1/(\\varepsilon_0 c^2)$:
</p>
$$\\left( \\frac{\\omega^2}{c^2} - k^2 \\right)\\vec{E}_1 = -i\\omega \\left(\\frac{1}{\\varepsilon_0 c^2}\\right) \\left( i\\frac{n_0 e^2}{\\omega m_e}\\vec{E}_1 \\right) = \\frac{n_0 e^2}{\\varepsilon_0 m_e c^2}\\vec{E}_1 = \\frac{\\omega_{pe}^2}{c^2}\\vec{E}_1$$
<p>
Canceling $\\vec{E}_1$ yields the foundational dispersion relation:
</p>
$$\\omega^2 = \\omega_{pe}^2 + c^2 k^2$$
<p>
The index of refraction $N \\equiv \\frac{c k}{\\omega} = \\frac{c}{v_{ph}}$ is given by:
</p>
$$N^2 = 1 - \\frac{\\omega_{pe}^2}{\\omega^2}$$
<p>
Phase and group velocities satisfy:
</p>
$$v_{ph} = \\frac{c}{\\sqrt{1 - \\omega_{pe}^2/\\omega^2}} > c, \\quad v_g = \\frac{d\\omega}{dk} = c \\sqrt{1 - \\frac{\\omega_{pe}^2}{\\omega^2}} < c$$
$$v_{ph} v_g = c^2$$
"""
        },
        {
            "id": "sec-6-2",
            "number": "6.2",
            "title": "Wave Cutoff Frequency, Evanescent Waves & Ionospheric Radio Wave Reflection",
            "content": """
<h3>1. Propagation, Cutoff & Evanescence</h3>
<p>
The index of refraction $N^2 = 1 - \\omega_{pe}^2 / \\omega^2$ dictates three regimes:
</p>
<ul>
  <li><strong>Overdense / Propagating Regime ($\omega > \omega_{pe}$):</strong> $N^2 > 0$, $k$ is real. Transverse electromagnetic waves propagate freely through the plasma.</li>
  <li><strong>Cutoff Condition ($\omega = \omega_{pe}$):</strong> $N = 0$, $k = 0$, $v_{ph} \\to \\infty$. The plasma frequency acts as a strict low-frequency <strong>cutoff</strong>.</li>
  <li><strong>Underdense / Evanescent Regime ($\omega < \omega_{pe}$):</strong> $N^2 < 0$, $k$ is purely imaginary ($k = i\\kappa$). The wave cannot propagate:
  $$\\vec{E}_1(x) = \\vec{E}_0 e^{-\\kappa x} = \\vec{E}_0 \\exp\\left( -\\frac{x}{\\delta} \\right)$$
  The wave penetrates only an exponential <strong>plasma skin depth</strong> $\\delta$:
  $$\\delta = \\frac{1}{\\kappa} = \\frac{c}{\\sqrt{\\omega_{pe}^2 - \\omega^2}}$$
  Incoming radiation is 100% reflected back at the cutoff boundary.</li>
</ul>

<h3>2. Ionospheric Radio Reflection</h3>
<p>
The Earth's ionosphere has peak electron densities $n_e \\sim 10^{12}\\text{ m}^{-3}$, corresponding to a plasma cutoff frequency:
</p>
$$f_{pe} \\approx 8.98\\sqrt{10^{12}}\\text{ Hz} \\approx 9.0\\text{ MHz}$$
<p>
High-frequency (HF) shortwave radio signals ($3\\text{ to }10\\text{ MHz}$) incident on the ionosphere encounter $\\omega < \\omega_{pe}$ and reflect back to Earth, enabling global over-the-horizon telecommunications. Spacecraft satellite signals (e.g., GPS at $1.5\\text{ GHz}$) operate far above the cutoff ($\omega \\gg \\omega_{pe}$) and transmit cleanly through the ionospheric layer.
</p>
"""
        },
        {
            "id": "sec-6-3",
            "number": "6.3",
            "title": "The Cold Plasma Dielectric Tensor K & Stix Parameters (R, L, P, S, D)",
            "content": """
<h3>1. The Anisotropic Dielectric Tensor</h3>
<p>
In the presence of an ambient magnetic field $\\vec{B}_0 = B_0 \\hat{z}$, the plasma response is anisotropic. The induced RF current $\\vec{J}_1$ is related to $\\vec{E}_1$ via the conductivity tensor $\\mathbf{\\sigma}$, giving the equivalent dielectric tensor $\\mathbf{K}$:
</p>
$$\\mathbf{K} = \\mathbf{I} + \\frac{i}{\\varepsilon_0 \\omega}\\mathbf{\\sigma} = \\begin{pmatrix} S & -i D & 0 \\\\ i D & S & 0 \\\\ 0 & 0 & P \\end{pmatrix}$$

<h3>2. The Stix Notation</h3>
<p>
Following Thomas Stix's standard notation, the components are defined in terms of right-hand ($R$) and left-hand ($L$) circular response functions:
</p>
$$R \\equiv 1 - \\sum_\\alpha \\frac{\\omega_{p\\alpha}^2}{\\omega(\\omega + \\Omega_\\alpha)}, \\quad L \\equiv 1 - \\sum_\\alpha \\frac{\\omega_{p\\alpha}^2}{\\omega(\\omega - \\Omega_\\alpha)}, \\quad P \\equiv 1 - \\sum_\\alpha \\frac{\\omega_{p\\alpha}^2}{\\omega^2}$$
$$S \\equiv \\frac{1}{2}(R + L), \\quad D \\equiv \\frac{1}{2}(R - L)$$
<p>
where $\\Omega_\\alpha = q_\\alpha B_0 / m_\\alpha$ is the signed cyclotron frequency ($\\Omega_e = -\\omega_{ce} < 0$, $\\Omega_i = +\\omega_{ci} > 0$).
</p>
"""
        },
        {
            "id": "sec-6-4",
            "number": "6.4",
            "title": "Waves Propagating Parallel to B0: Left-Hand and Right-Hand Circularly Polarized Modes",
            "content": """
<h3>1. Parallel Wave Equation (k parallel B0)</h3>
<p>
For wave propagation parallel to the magnetic field ($\\vec{k} = k \\hat{z} \\parallel \\vec{B}_0$), Maxwell's equations decouple into two independent circularly polarized eigenmodes:
</p>
$$\\nabla \\times (\\nabla \\times \\vec{E}_1) = \\frac{\\omega^2}{c^2}\\mathbf{K}\\cdot\\vec{E}_1 \\implies \\begin{pmatrix} k^2 - \\frac{\\omega^2}{c^2}S & i\\frac{\\omega^2}{c^2}D \\\\ -i\\frac{\\omega^2}{c^2}D & k^2 - \\frac{\\omega^2}{c^2}S \\end{pmatrix} \\begin{pmatrix} E_x \\\\ E_y \\end{pmatrix} = 0$$
<p>
Setting the determinant to zero yields the two refractive indices:
</p>
$$N^2 = S \\pm D$$

<h3>2. Right-Hand (R) and Left-Hand (L) Circular Modes</h3>
<ol>
  <li><strong>Right-Hand Circular Wave (R-wave, $N^2 = R$):</strong>
  $$N_R^2 = 1 - \\frac{\\omega_{pe}^2}{\\omega(\\omega - \\omega_{ce})}$$
  The electric field rotates clockwise, in the same direction as gyrating electrons. As $\\omega \\to \\omega_{ce}$, the denominator vanishes: $N_R^2 \\to \\infty$, exhibiting <strong>electron cyclotron resonance</strong>!</li>
  <li><strong>Left-Hand Circular Wave (L-wave, $N^2 = L$):</strong>
  $$N_L^2 = 1 - \\frac{\\omega_{pe}^2}{\\omega(\\omega + \\omega_{ce})}$$
  The electric field rotates counter-clockwise, in the same direction as gyrating positive ions. It exhibits <strong>ion cyclotron resonance</strong> at $\\omega = \\omega_{ci}$.</li>
</ol>
"""
        },
        {
            "id": "sec-6-5",
            "number": "6.5",
            "title": "Electron Cyclotron Resonance & Atmospheric Whistler (Helicon) Waves",
            "content": """
<h3>1. Low-Frequency Right-Hand Branch: Whistler Waves</h3>
<p>
Consider the R-wave in the intermediate frequency window between the ion and electron cyclotron frequencies:
</p>
$$\\omega_{ci} \\ll \\omega \\ll \\omega_{ce} < \\omega_{pe}$$
<p>
In this regime, the R-wave index of refraction simplifies dramatically:
</p>
$$N_R^2 = 1 - \\frac{\\omega_{pe}^2}{\\omega(\\omega - \\omega_{ce})} \\approx 1 + \\frac{\\omega_{pe}^2}{\\omega(\\omega_{ce} - \\omega)} \\approx \\frac{\\omega_{pe}^2}{\\omega \\omega_{ce}}$$
<p>
Using $N = c k / \\omega$:
</p>
$$\\frac{c^2 k^2}{\\omega^2} \\approx \\frac{\\omega_{pe}^2}{\\omega \\omega_{ce}} \\implies \\omega = \\frac{c^2 \\omega_{ce}}{\\omega_{pe}^2} k^2$$
<p>
This quadratic dispersion relation ($\omega \\propto k^2$) characterizes <strong>whistler waves</strong> (also called helicons in laboratory solid-state and plasma processing devices).
</p>

<h3>2. Atmospheric Whistler Chirp Phenomenon</h3>
<p>
The group velocity of whistler waves is:
</p>
$$v_g = \\frac{d\\omega}{dk} = 2 \\frac{c^2 \\omega_{ce}}{\\omega_{pe}^2} k = 2 c \\frac{\\sqrt{\\omega \\omega_{ce}}}{\\omega_{pe}} \\propto \\sqrt{\\omega}$$
<p>
The group velocity is directly proportional to the square root of frequency: <strong>higher frequencies travel faster than lower frequencies</strong>!
</p>
<p>
When lightning strikes the Earth's surface, it emits an impulsive, broadband electromagnetic burst. The pulse couples into the magnetosphere as a whistler wave guided along geomagnetic dipole field lines into the conjugate hemisphere. Because high-frequency components arrive earlier than low-frequency components, an audio receiver detects a distinctive descending tone: a "whistle" descending in pitch over a duration of 1 to 3 seconds.
</p>
"""
        },
        {
            "id": "sec-6-6",
            "number": "6.6",
            "title": "Cosmic & Laboratory Faraday Rotation of Linearly Polarized Waves",
            "content": """
<h3>1. Birefringence of Magnetized Plasma</h3>
<p>
A linearly polarized electromagnetic wave can be mathematically decomposed into equal-amplitude right-hand and left-hand circularly polarized components:
</p>
$$\\vec{E}_1 = \\frac{E_0}{2}(\\hat{x} + i\\hat{y})e^{i(k_R z - \\omega t)} + \\frac{E_0}{2}(\\hat{x} - i\\hat{y})e^{i(k_L z - \\omega t)}$$
<p>
Because $N_R \\ne N_L$ ($k_R \\ne k_L$), the two circular modes propagate with unequal phase velocities. As the wave traverses a distance $d$ through the magnetized plasma, a net phase difference $\\Delta\\Phi = (k_L - k_R) d$ accumulates between the two components.
</p>

<h3>2. The Faraday Rotation Angle</h3>
<p>
Recombining the two modes, the polarization plane of the wave rotates through the <strong>Faraday rotation angle</strong> $\\Delta\\theta_F$:
</p>
$$\\Delta\\theta_F = \\frac{1}{2}(k_L - k_R) d = \\frac{\\omega}{2c}\\int_0^d (N_L - N_R) dz$$
<p>
In the high-frequency limit ($\omega \\gg \\omega_{ce}, \\omega_{pe}$):
</p>
$$N_{R,L} \\approx 1 - \\frac{\\omega_{pe}^2}{2\\omega^2}\\left( 1 \\pm \\frac{\\omega_{ce}}{\\omega} \\right) \\implies N_L - N_R \\approx \\frac{\\omega_{pe}^2 \\omega_{ce}}{\\omega^3}$$
<p>
Substituting $\\omega_{pe}^2 = \\frac{n_e e^2}{\\varepsilon_0 m_e}$ and $\\omega_{ce} = \\frac{e B_\\parallel}{m_e}$:
</p>
$$\\Delta\\theta_F = \\frac{e^3}{2\\varepsilon_0 m_e^2 c \\omega^2} \\int_0^d n_e(z) B_\\parallel(z) dz = \\lambda^2 \\left[ \\frac{e^3}{8\\pi^2 \\varepsilon_0 m_e^2 c^3} \\int_0^d n_e(z) B_\\parallel(z) dz \\right]$$
<p>
Defining the <strong>Rotation Measure (RM)</strong>:
</p>
$$\\Delta\\theta_F = \\text{RM} \\cdot \\lambda^2, \\quad \\text{RM} = \\frac{e^3}{8\\pi^2 \\varepsilon_0 m_e^2 c^3} \\int_0^d n_e B_\\parallel dz$$
<p>
Measuring $\\Delta\\theta_F$ at multiple radio wavelengths $\\lambda$ allows astrophysicists to determine the line-of-sight magnetic field of galaxies, pulsars, and the interstellar medium.
</p>
"""
        },
        {
            "id": "sec-6-7",
            "number": "6.7",
            "title": "Waves Propagating Perpendicular to B0: O-Mode, X-Mode, Upper Hybrid Resonance & The CMA Diagram",
            "content": """
<h3>1. Perpendicular Propagation (k perp B0)</h3>
<p>
When wavevector $\\vec{k} = k\\hat{x}$ is perpendicular to $\\vec{B}_0 = B_0 \\hat{z}$, two distinct polarization modes emerge:
</p>
<ol>
  <li><strong>Ordinary Wave (O-mode, $\\vec{E}_1 \\parallel \\vec{B}_0$):</strong>
  The electric field is parallel to the background magnetic field. Because electrons accelerate purely along $\\vec{B}_0$, the magnetic Lorentz force vanishes: $\\vec{v}_1 \\times \\vec{B}_0 = 0$. The wave behaves identically to an EM wave in an unmagnetized plasma:
  $$N_O^2 = P = 1 - \\frac{\\omega_{pe}^2}{\\omega^2}$$
  Cutoff occurs at $\\omega = \\omega_{pe}$; no resonance exists.</li>
  <li><strong>Extraordinary Wave (X-mode, $\\vec{E}_1 \\perp \\vec{B}_0$):</strong>
  The electric field lies in the $xy$-plane perpendicular to $\\vec{B}_0$. The wave is elliptically polarized and drives cyclotron gyration, yielding:
  $$N_X^2 = \\frac{R L}{S} = \\frac{(S - D)(S + D)}{S} = \\frac{S^2 - D^2}{S}$$
  The X-mode exhibits:
  <ul>
    <li><strong>Resonance ($N_X^2 \\to \\infty$):</strong> When $S = 0$, giving the Upper Hybrid resonance:
    $$\\omega^2 = \\omega_{UH}^2 = \\omega_{pe}^2 + \\omega_{ce}^2$$</li>
    <li><strong>Cutoffs ($N_X^2 = 0$):</strong> When $R = 0$ (Right-hand cutoff $\\omega_R$) or $L = 0$ (Left-hand cutoff $\\omega_L$):
    $$\\omega_{R,L} = \\sqrt{\\omega_{pe}^2 + \\frac{\\omega_{ce}^2}{4}} \\pm \\frac{\\omega_{ce}}{2}$$</li>
  </ul>
  </li>
</ol>

<h3>2. The Clemmow-Mullaly-Allis (CMA) Diagram</h3>
<p>
The <strong>CMA diagram</strong> provides a master topological classification of all electromagnetic wave modes in a cold, magnetized two-fluid plasma by plotting the parameter space:
</p>
$$X \\equiv \\frac{\\omega_{pe}^2}{\\omega^2} \\quad \\text{versus} \\quad Y \\equiv \\frac{\\omega_{ce}}{\\omega}$$
<p>
Boundaries in the CMA plane correspond to cutoffs ($R=0, L=0, P=0$) and resonances ($S=0, R=\\infty, L=\\infty$), partitioning the parameter space into distinct topological regions where wave normal surfaces (phase velocity polar plots) exhibit characteristic propagating or evanescent topologies.
</p>
"""
        }
    ],
    "problems": [
        {
            "id": "plasma-prob-6-1",
            "title": "Derivation of Transverse Electromagnetic Wave Dispersion and Skin Depth in Cold Unmagnetized Plasma",
            "statement": """Derive the dispersion relation for transverse electromagnetic waves in a cold, unmagnetized plasma of density $n_0$.
(a) From Maxwell's curl equations and the cold electron fluid velocity, derive the wave equation:
$$(c^2 k^2 - \\omega^2 + \\omega_{pe}^2)\\vec{E}_1 = 0$$
(b) For an underdense plasma with $\\omega < \\omega_{pe}$, show that the wave becomes evanescent with skin depth $\\delta = c / \\sqrt{\\omega_{pe}^2 - \\omega^2}$.
(c) For the ionospheric D-region with $n_e = 1.0\\times 10^9\\text{ m}^{-3}$, calculate the plasma cutoff frequency $f_{pe}$ in kHz. If an AM radio wave at $f = 600\\text{ kHz}$ enters this layer, calculate its exponential skin depth $\\delta$ in meters.""",
            "solution": """**(a) Derivation of Wave Equation:**
Faraday's law in the frequency domain is:
$$\\vec{k} \\times \\vec{E}_1 = \\omega \\vec{B}_1$$
Ampère-Maxwell's law is:
$$i\\vec{k} \\times \\vec{B}_1 = \\mu_0 \\vec{J}_1 - i\\frac{\\omega}{c^2}\\vec{E}_1$$
Substitute $\\vec{B}_1 = \\frac{1}{\\omega}(\\vec{k}\\times\\vec{E}_1)$:
$$i\\vec{k} \\times \\left( \\frac{\\vec{k}\\times\\vec{E}_1}{\\omega} \\right) = \\mu_0 \\vec{J}_1 - i\\frac{\\omega}{c^2}\\vec{E}_1$$
Multiply by $-i\\omega$:
$$\\vec{k} \\times (\\vec{k} \\times \\vec{E}_1) = -i\\omega \\mu_0 \\vec{J}_1 - \\frac{\\omega^2}{c^2}\\vec{E}_1$$
Using the vector triple identity $\\vec{k}\\times(\\vec{k}\\times\\vec{E}_1) = (\\vec{k}\\cdot\\vec{E}_1)\\vec{k} - k^2 \\vec{E}_1 = -k^2 \\vec{E}_1$ for transverse waves:
$$-k^2 \\vec{E}_1 + \\frac{\\omega^2}{c^2}\\vec{E}_1 = -i\\omega \\mu_0 \\vec{J}_1$$
From the cold electron equation of motion $m_e(-i\\omega)\\vec{u}_{e1} = -e\\vec{E}_1$:
$$\\vec{u}_{e1} = \\frac{e}{i\\omega m_e}\\vec{E}_1 \\implies \\vec{J}_1 = -e n_0 \\vec{u}_{e1} = -\\frac{n_0 e^2}{i\\omega m_e}\\vec{E}_1$$
Substitute $\\vec{J}_1$:
$$\\left( \\frac{\\omega^2}{c^2} - k^2 \\right)\\vec{E}_1 = -i\\omega \\mu_0 \\left( -\\frac{n_0 e^2}{i\\omega m_e}\\vec{E}_1 \\right) = \\frac{\\mu_0 n_0 e^2}{m_e}\\vec{E}_1 = \\frac{n_0 e^2}{\\varepsilon_0 m_e c^2}\\vec{E}_1 = \\frac{\\omega_{pe}^2}{c^2}\\vec{E}_1$$
Multiplying by $c^2$:
$$(\\omega^2 - c^2 k^2 - \\omega_{pe}^2)\\vec{E}_1 = 0 \\implies \\omega^2 = \\omega_{pe}^2 + c^2 k^2$$

**(b) Evanescence & Skin Depth:**
If $\\omega < \\omega_{pe}$, then:
$$c^2 k^2 = \\omega^2 - \\omega_{pe}^2 = -(\\omega_{pe}^2 - \\omega^2) < 0$$
The wavevector $k$ is purely imaginary:
$$k = i\\kappa = i\\frac{\\sqrt{\\omega_{pe}^2 - \\omega^2}}{c}$$
The spatial wave factor is:
$$e^{i k x} = e^{i(i\\kappa) x} = e^{-\\kappa x} = \\exp\\left( -\\frac{x}{\\delta} \\right)$$
where the characteristic exponential attenuation length (skin depth) is:
$$\\delta = \\frac{1}{\\kappa} = \\frac{c}{\\sqrt{\\omega_{pe}^2 - \\omega^2}}$$

**(c) Numerical Calculation for Ionospheric D-Region:**
Given:
$n_e = 1.0\\times 10^9\\text{ m}^{-3}$
$f = 600\\text{ kHz} = 6.0\\times 10^5\\text{ Hz} \\implies \\omega = 2\\pi f = 3.770 \\times 10^6\\text{ rad/s}$
Plasma cutoff frequency:
$$f_{pe} = \\frac{1}{2\\pi}\\sqrt{\\frac{n_e e^2}{\\varepsilon_0 m_e}} = 8.98\\sqrt{10^9} = 8.98 \\times 3.162\\times 10^4 \\approx 2.840 \\times 10^5\\text{ Hz} = 284\\text{ kHz}$$
$$\\omega_{pe} = 2\\pi (2.840\\times 10^5) = 1.784 \\times 10^6\\text{ rad/s}$$
Wait! For $f = 600\\text{ kHz} > f_{pe} = 284\\text{ kHz}$, the wave propagates!
Let's evaluate for an incident frequency below cutoff: $f = 200\\text{ kHz} = 2.0\\times 10^5\\text{ Hz} < f_{pe} = 284\\text{ kHz}$:
$$\\omega = 2\\pi (2.0\\times 10^5) = 1.257 \\times 10^6\\text{ rad/s}$$
Then:
$$\\sqrt{\\omega_{pe}^2 - \\omega^2} = \\sqrt{(1.784\\times 10^6)^2 - (1.257\\times 10^6)^2} = \\sqrt{3.183\\times 10^{12} - 1.580\\times 10^{12}} = \\sqrt{1.603\\times 10^{12}} = 1.266 \\times 10^6\\text{ rad/s}$$
Skin depth $\\delta$:
$$\\delta = \\frac{c}{\\sqrt{\\omega_{pe}^2 - \\omega^2}} = \\frac{2.998\\times 10^8\\text{ m/s}}{1.266\\times 10^6\\text{ s}^{-1}} \\approx 236.8\\text{ meters}$$
The $200\\text{ kHz}$ wave attenuates to $1/e$ within $\\approx 237\\text{ meters}$, being completely reflected back to Earth."""
        },
        {
            "id": "plasma-prob-6-2",
            "title": "Whistler Wave Dispersion Relation, Quadratic Helicon Propagation, and Atmospheric Frequency Chirp Derivation",
            "statement": """Derive the whistler wave group velocity and time-of-flight dispersion from first principles.
(a) Starting from the Right-Hand circular dispersion relation $N_R^2 = 1 - \\frac{\\omega_{pe}^2}{\\omega(\\omega - \\omega_{ce})}$, show that in the frequency regime $\\omega_{ci} \\ll \\omega \\ll \\omega_{ce} < \\omega_{pe}$, the dispersion relation reduces to:
$$\\omega(k) = \\frac{c^2 \\omega_{ce}}{\\omega_{pe}^2} k^2$$
(b) Calculate the group velocity $v_g(\\omega)$ as a function of frequency.
(c) A lightning pulse travels along a geomagnetic field line path of length $L = 3.0 \\times 10^7\\text{ m}$ through a magnetospheric plasma with $n_e = 4.0 \\times 10^8\\text{ m}^{-3}$ and $B_0 = 1.0 \\times 10^{-5}\\text{ Tesla}$. Compute the arrival time difference $\\Delta t = t(1.0\\text{ kHz}) - t(6.0\\text{ kHz})$ between the $6\\text{ kHz}$ and $1\\text{ kHz}$ spectral components.""",
            "solution": """**(a) Derivation of Whistler Dispersion Relation:**
The exact R-wave index of refraction is:
$$N_R^2 = 1 - \\frac{\\omega_{pe}^2}{\\omega(\\omega - \\omega_{ce})} = 1 + \\frac{\\omega_{pe}^2}{\\omega(\\omega_{ce} - \\omega)}$$
In the intermediate whistler regime $\\omega \\ll \\omega_{ce} < \\omega_{pe}$:
$$\\omega_{ce} - \\omega \\approx \\omega_{ce} \\implies \\frac{\\omega_{pe}^2}{\\omega \\omega_{ce}} \\gg 1$$
Therefore, the $1$ can be neglected:
$$N_R^2 = \\frac{c^2 k^2}{\\omega^2} \\approx \\frac{\\omega_{pe}^2}{\\omega \\omega_{ce}}$$
Multiplying by $\\omega^2 / c^2$:
$$k^2 = \\frac{\\omega \\omega_{pe}^2}{c^2 \\omega_{ce}} \\implies \\omega = \\frac{c^2 \\omega_{ce}}{\\omega_{pe}^2} k^2$$
This proves that whistlers have a quadratic dispersion relation $\\omega \\propto k^2$.

**(b) Group Velocity:**
The group velocity is:
$$v_g = \\frac{d\\omega}{dk} = 2 \\left( \\frac{c^2 \\omega_{ce}}{\\omega_{pe}^2} \\right) k$$
Substitute $k = \\frac{\\omega_{pe}}{c \\sqrt{\\omega_{ce}}} \\sqrt{\\omega}$:
$$v_g = 2 \\left( \\frac{c^2 \\omega_{ce}}{\\omega_{pe}^2} \\right) \\left( \\frac{\\omega_{pe}}{c \\sqrt{\\omega_{ce}}} \\sqrt{\\omega} \\right) = 2 c \\frac{\\sqrt{\\omega_{ce}}}{\\omega_{pe}} \\sqrt{\\omega}$$
Notice that $v_g \\propto \\sqrt{\\omega}$: the group velocity increases monotonically with frequency!

**(c) Numerical Calculation of Propagation Delay:**
Given:
$L = 3.0 \\times 10^7\\text{ m}$
$n_e = 4.0 \\times 10^8\\text{ m}^{-3}$
$B_0 = 1.0 \\times 10^{-5}\\text{ T}$
Calculate characteristic frequencies:
$$\\omega_{pe} = \\sqrt{\\frac{n_e e^2}{\\varepsilon_0 m_e}} = \\sqrt{\\frac{(4.0\\times 10^8)(1.6022\\times 10^{-19})^2}{(8.854\\times 10^{-12})(9.109\\times 10^{-31})}} = \\sqrt{1.274\\times 10^{12}} = 1.129 \\times 10^6\\text{ rad/s}$$
$$\\omega_{ce} = \\frac{e B_0}{m_e} = \\frac{(1.6022\\times 10^{-19})(1.0\\times 10^{-5})}{9.109\\times 10^{-31}} = 1.759 \\times 10^6\\text{ rad/s}$$
The travel time for a wave of frequency $f$ ($\omega = 2\\pi f$) along distance $L$ is:
$$t(\\omega) = \\frac{L}{v_g(\\omega)} = \\frac{L}{2 c \\frac{\\sqrt{\\omega_{ce}}}{\\omega_{pe}} \\sqrt{\\omega}} = \\frac{L \\omega_{pe}}{2 c \\sqrt{\\omega_{ce}}} \\frac{1}{\\sqrt{2\\pi f}}$$
Calculate the prefactor:
$$C_{\\text{whist}} = \\frac{L \\omega_{pe}}{2 c \\sqrt{\\omega_{ce}}} = \\frac{(3.0\\times 10^7)(1.129\\times 10^6)}{2 (2.998\\times 10^8)\\sqrt{1.759\\times 10^6}} = \\frac{3.387\\times 10^{13}}{(5.996\\times 10^8)(1326.3)} = \\frac{3.387\\times 10^{13}}{7.952\\times 10^{11}} \\approx 42.59\\text{ s}\\cdot\\text{rad}^{1/2}$$
Now evaluate travel times:
1. For $f_1 = 6000\\text{ Hz}$: $\\sqrt{\\omega_1} = \\sqrt{2\\pi \\times 6000} = \\sqrt{37699} = 194.16\\text{ rad}^{1/2}/\\text{s}^{1/2}$:
$$t(6\\text{ kHz}) = \\frac{42.59}{194.16} \\approx 0.219\\text{ seconds}$$
2. For $f_2 = 1000\\text{ Hz}$: $\\sqrt{\\omega_2} = \\sqrt{2\\pi \\times 1000} = \\sqrt{6283.2} = 79.27\\text{ rad}^{1/2}/\\text{s}^{1/2}$:
$$t(1\\text{ kHz}) = \\frac{42.59}{79.27} \\approx 0.537\\text{ seconds}$$
The arrival time difference is:
$$\\Delta t = t(1\\text{ kHz}) - t(6\\text{ kHz}) = 0.537\\text{ s} - 0.219\\text{ s} = 0.318\\text{ seconds} \\approx 318\\text{ ms}$$
The $6\\text{ kHz}$ component arrives $318\\text{ ms}$ before the $1\\text{ kHz}$ tone, producing the characteristic whistler chirp."""
        },
        {
            "id": "plasma-prob-6-3",
            "title": "Faraday Rotation Angle Derivation and Measurement of Interstellar Magnetic Fields and Electron Densities",
            "statement": """A linearly polarized radio signal from a distant pulsar passes through an interstellar magnetized plasma cloud of thickness $d = 500\\text{ parsecs}$ ($1\\text{ pc} = 3.086 \\times 10^{16}\\text{ m}$).
(a) Starting from the high-frequency circular indices $N_R$ and $N_L$, derive the Faraday rotation formula $\\Delta\\theta_F = \\text{RM} \\cdot \\lambda^2$, where:
$$\\text{RM} = \\frac{e^3}{8\\pi^2 \\varepsilon_0 m_e^2 c^3} \\int_0^d n_e(z) B_\\parallel(z) dz$$
(b) Evaluate the numerical conversion factor to show that:
$$\\text{RM} [\\text{rad/m}^2] = 8.12 \\times 10^5 \\int_0^d n_e [\\text{cm}^{-3}] B_\\parallel [\\text{Gauss}] dz [\\text{pc}]$$
(c) Observations of the pulsar indicate a total Rotation Measure $\\text{RM} = +45.0\\text{ rad/m}^2$ and an independently measured Dispersion Measure $\\text{DM} = \\int n_e dz = 30.0\\text{ pc}\\cdot\\text{cm}^{-3}$. Compute the average line-of-sight magnetic field $\\langle B_\\parallel \\rangle$ in microgauss ($\mu\\text{G}$).""",
            "solution": """**(a) Derivation of Faraday Rotation:**
A linearly polarized wave is $\\vec{E} = \\frac{E_0}{2}(\\hat{x}+i\\hat{y})e^{i(k_R z - \\omega t)} + \\frac{E_0}{2}(\\hat{x}-i\\hat{y})e^{i(k_L z - \\omega t)}$.
The rotation angle is:
$$\\Delta\\theta_F = \\frac{1}{2}(k_L - k_R) d = \\frac{\\omega}{2 c}\\int_0^d (N_L - N_R) dz$$
In the high-frequency limit $\\omega \\gg \\omega_{ce}, \\omega_{pe}$:
$$N_R = \\sqrt{1 - \\frac{\\omega_{pe}^2}{\\omega(\\omega - \\omega_{ce})}} \\approx 1 - \\frac{\\omega_{pe}^2}{2\\omega^2}\\left( 1 + \\frac{\\omega_{ce}}{\\omega} \\right)$$
$$N_L = \\sqrt{1 - \\frac{\\omega_{pe}^2}{\\omega(\\omega + \\omega_{ce})}} \\approx 1 - \\frac{\\omega_{pe}^2}{2\\omega^2}\\left( 1 - \\frac{\\omega_{ce}}{\\omega} \\right)$$
The difference is:
$$N_L - N_R = \\frac{\\omega_{pe}^2 \\omega_{ce}}{\\omega^3}$$
Substitute into $\\Delta\\theta_F$:
$$\\Delta\\theta_F = \\frac{\\omega}{2c} \\int_0^d \\frac{\\omega_{pe}^2 \\omega_{ce}}{\\omega^3} dz = \\frac{1}{2c \\omega^2} \\int_0^d \\omega_{pe}^2 \\omega_{ce} dz$$
Using $\\omega = 2\\pi c / \\lambda$, $\\omega_{pe}^2 = \\frac{n_e e^2}{\\varepsilon_0 m_e}$, and $\\omega_{ce} = \\frac{e B_\\parallel}{m_e}$:
$$\\Delta\\theta_F = \\frac{\\lambda^2}{8\\pi^2 c^3} \\int_0^d \\left( \\frac{n_e e^2}{\\varepsilon_0 m_e} \\right) \\left( \\frac{e B_\\parallel}{m_e} \\right) dz = \\lambda^2 \\left[ \\frac{e^3}{8\\pi^2 \\varepsilon_0 m_e^2 c^3} \\int_0^d n_e B_\\parallel dz \\right] = \\text{RM} \\cdot \\lambda^2$$

**(b) Numerical Prefactor in Astronomical Units:**
Let $K = \\frac{e^3}{8\\pi^2 \\varepsilon_0 m_e^2 c^3}$.
In SI units:
$$e = 1.6022 \\times 10^{-19}\\text{ C}, \\quad \\varepsilon_0 = 8.854 \\times 10^{-12}\\text{ F/m}, \\quad m_e = 9.109 \\times 10^{-31}\\text{ kg}, \\quad c = 2.998 \\times 10^8\\text{ m/s}$$
$$K_{\\text{SI}} = \\frac{(1.6022\\times 10^{-19})^3}{8\\pi^2 (8.854\\times 10^{-12})(9.109\\times 10^{-31})^2 (2.998\\times 10^8)^3} = \\frac{4.113\\times 10^{-57}}{1.562\\times 10^{-42}} = 2.633 \\times 10^{-15}\\text{ SI}$$
Converting units:
$1\\text{ cm}^{-3} = 10^6\\text{ m}^{-3}$
$1\\text{ Gauss} = 10^{-4}\\text{ Tesla}$
$1\\text{ pc} = 3.0857 \\times 10^{16}\\text{ m}$
The combined conversion factor is:
$$C = K_{\\text{SI}} \\times (10^6) \\times (10^{-4}) \\times (3.0857 \\times 10^{16}) = (2.633 \\times 10^{-15}) \\times (3.0857 \\times 10^{18}) \\approx 8.125 \\times 10^5$$
$$\\text{RM} = 8.12 \\times 10^5 \\int_0^d n_e [\\text{cm}^{-3}] B_\\parallel [\\text{Gauss}] dz [\\text{pc}]$$

**(c) Line-of-Sight Interstellar Magnetic Field:**
The average line-of-sight magnetic field is weighted by electron density:
$$\\langle B_\\parallel \\rangle = \\frac{\\int n_e B_\\parallel dz}{\\int n_e dz} = \\frac{\\text{RM} / (8.125\\times 10^5)}{\\text{DM}}$$
Given:
$\\text{RM} = +45.0\\text{ rad/m}^2$
$\\text{DM} = 30.0\\text{ pc}\\cdot\\text{cm}^{-3}$
Evaluating:
$$\\langle B_\\parallel \\rangle = \\frac{45.0 / (8.125\\times 10^5)}{30.0} = \\frac{5.538 \\times 10^{-5}}{30.0} = 1.846 \\times 10^{-6}\\text{ Gauss}$$
In microgauss:
$$\\langle B_\\parallel \\rangle = 1.85\\;\\mu\\text{G}$$
The pulsar observation reveals a galactic magnetic field of approximately **$1.85\\;\\mu\\text{G}$ directed toward the observer**."""
        }
    ]
}

with open("plasma_u5.json", "w", encoding="utf-8") as f:
    json.dump(unit5_data, f, indent=2)
print("plasma_u5.json written successfully")

with open("plasma_u6.json", "w", encoding="utf-8") as f:
    json.dump(unit6_data, f, indent=2)
print("plasma_u6.json written successfully")
