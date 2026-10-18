# -*- coding: utf-8 -*-
"""
Builder for Nuclear Reactor Physics Units 1 & 2
Unit 1: Fundamentals of Nuclear Energy, Atom Densities & Fission Fuel Breeding
Unit 2: Neutron Interactions, Cross Sections & Nuclear Reaction Rates
"""
import json

u1_data = {
    "title": "Fundamentals of Nuclear Energy, Atom Densities & Fission Fuel Breeding",
    "subtitle": "Fission Energetics, Mass Defect, Separation Energies, Maxwellian Flux & Atom Density Formalism",
    "summary": "Foundational principles of nuclear reactor physics: comparison of fission and fusion energetics, microscopic nuclear force characteristics, classification of nuclear materials into fissile (U-235, Pu-239, U-233), fissionable (U-238, Th-232), and fertile isotopes; breeding reaction chains and breeding ratio/doubling time kinetics in fast breeder reactors; relativistic mass-energy equivalence, mass defect, binding energy systematics, and nucleon separation energy criteria; Maxwell-Boltzmann thermal neutron gas velocity distributions; and rigorous mathematical formulation of elemental, isotopic, and molecular atom densities for nuclear fuel and moderator compounds.",
    "sections": [
        {
            "id": "sec-1-1",
            "title": "Nuclear Reactor Physics Overview, Fission vs Fusion & Nuclear Force",
            "content": r"""
<h3>1. Scope of Nuclear Reactor Physics</h3>
<p>
Nuclear reactor physics is the branch of applied nuclear physics and engineering that governs the distribution, transport, slowing down, and multiplication of neutrons inside a nuclear reactor core. The central objective is to sustain and control a steady-state or time-dependent chain reaction, converting microscopic nuclear binding energy into macroscopic thermal power:
$$\text{Nuclear Energy} \longrightarrow \text{Thermal Energy} \longrightarrow \text{Mechanical Turbine Work} \longrightarrow \text{Electrical Power}$$
</p>
<p>
At the subatomic level, atomic nuclei are held together by the <strong>residual strong nuclear force</strong>, a phenomenological interaction mediated primarily by virtual meson exchange between nucleons (protons and neutrons). Key physical characteristics include:
<ul>
  <li><strong>Colossal Magnitude:</strong> Approximately $100$ to $1000$ times stronger than the electromagnetic Coulomb repulsion at distances $r \approx 1\text{ fm}$.</li>
  <li><strong>Extremely Short Range:</strong> Effective only over nuclear dimensions ($r \sim 1\text{ to }2\text{ fm}$), decaying exponentially as $\sim \frac{e^{-\mu r}}{r}$ for $r > 2\text{ fm}$.</li>
  <li><strong>Saturation Property:</strong> A nucleon interacts only with its immediate nearest neighbors, meaning the binding energy per nucleon ($B/A \approx 8\text{ MeV}$) is approximately constant across intermediate and heavy nuclei.</li>
  <li><strong>Hard Repulsive Core:</strong> Becomes fiercely repulsive at $r < 0.4\text{ fm}$, preventing the collapse of atomic nuclei into point singularities.</li>
</ul>
</p>

<h3>2. Energetics of Fission vs Fusion</h3>
<p>
The curve of binding energy per nucleon ($B/A$ versus mass number $A$) exhibits a prominent maximum near iron-56 (${}^{56}\text{Fe}$, where $B/A \approx 8.79\text{ MeV/nucleon}$). Because nature favors higher binding energy per nucleon (deeper potential wells), energy can be liberated exothermically via two distinct nuclear pathways:
</p>
<ol>
  <li><strong>Nuclear Fusion (Light Nuclei, $A < 56$):</strong> Fusing two light nuclei (such as deuterium and tritium, ${}^2\text{H} + {}^3\text{H} \to {}^4\text{He} + n + 17.6\text{ MeV}$) moves the products up the steep initial incline toward ${}^4\text{He}$ ($B/A \approx 7.07\text{ MeV}$), yielding $\sim 3.5\text{ MeV/nucleon}$.</li>
  <li><strong>Nuclear Fission (Heavy Nuclei, $A > 230$):</strong> Splitting a massive actinide nucleus (${}^{235}\text{U}$) into two intermediate fragments ($A_1 \sim 95, A_2 \sim 140$) shifts the system from $B/A \approx 7.56\text{ MeV}$ up to $B/A \approx 8.5\text{ MeV}$:
  $$\Delta(B/A) \approx 8.5\text{ MeV} - 7.56\text{ MeV} \approx 0.94\text{ MeV/nucleon}$$
  Multiplying by $A = 236$ nucleons:
  $$Q_{\text{fission}} \approx 236 \times 0.94\text{ MeV} \approx \mathbf{200\text{ MeV per fission event}}$$
  </li>
</ol>
<p>
This energy density is astronomical: the complete fission of $1\text{ kg}$ of ${}^{235}\text{U}$ releases $8.2 \times 10^{13}\text{ Joules}$ of energy—equivalent to burning approximately $2,500\text{ metric tons}$ of high-grade coal or $14{,}000\text{ barrels}$ of crude oil!
</p>
"""
        },
        {
            "id": "sec-1-2",
            "title": "Classification of Nuclear Materials: Fissile, Fissionable & Fertile",
            "content": r"""
<h3>1. Fissile Isotopes</h3>
<p>
<strong>Fissile materials</strong> are nuclides capable of undergoing nuclear fission upon capturing a neutron of <em>any</em> kinetic energy, including thermal neutrons with zero or near-zero kinetic energy ($E \approx 0.0253\text{ eV}$):
$$n_{\text{th}} + {}^{A}_Z\text{X} \longrightarrow [{}^{A+1}_Z\text{X}]^* \longrightarrow \text{Fission Fragments} + \nu \, n + Q$$
The three practical fissile fuels of modern nuclear technology are:
<ul>
  <li><strong>Uranium-235 (${}^{235}_{92}\text{U}$):</strong> The only naturally occurring fissile isotope on Earth, comprising $0.7204\%$ of natural uranium.</li>
  <li><strong>Plutonium-239 (${}^{239}_{94}\text{Pu}$):</strong> Artificially produced via neutron capture in fertile ${}^{238}\text{U}$.</li>
  <li><strong>Uranium-233 (${}^{233}_{92}\text{U}$):</strong> Artificially produced via neutron capture in fertile ${}^{232}\text{Th}$.</li>
</ul>
</p>

<h3>2. Fissionable Isotopes</h3>
<p>
<strong>Fissionable materials</strong> are nuclides capable of undergoing fission when struck by neutrons, but whose compound nucleus requires a threshold kinetic energy (typically $E_n > 1.0\text{ to }1.5\text{ MeV}$) to overcome the fission activation barrier:
$$n_{\text{fast}} (E_n > E_{\text{th}}) + {}^{238}_{92}\text{U} \longrightarrow [{}^{239}_{92}\text{U}]^* \longrightarrow \text{Fission}$$
Examples include even-$N$ actinides such as ${}^{238}_{92}\text{U}$, ${}^{232}_{90}\text{Th}$, and ${}^{240}_{94}\text{Pu}$.
All fissile materials are fissionable, but not all fissionable materials are fissile.
</p>

<h3>3. Fertile Isotopes and Nuclear Transmutation</h3>
<p>
<strong>Fertile materials</strong> are nuclides that are not themselves fissile by thermal neutrons, but can be converted into fissile isotopes through neutron radiative capture $(n, \gamma)$ followed by subsequent beta-minus ($\beta^-$) decays:
<ol>
  <li><strong>The Uranium-Plutonium Cycle:</strong>
  $${}^{238}_{92}\text{U} + n \longrightarrow {}^{239}_{92}\text{U} \xrightarrow[\beta^-, \, 23.5\text{ min}]{} {}^{239}_{93}\text{Np} \xrightarrow[\beta^-, \, 2.356\text{ days}]{} {}^{239}_{94}\text{Pu} \quad (\text{Fissile!})$$
  </li>
  <li><strong>The Thorium-Uranium Cycle:</strong>
  $${}^{232}_{90}\text{Th} + n \longrightarrow {}^{233}_{90}\text{Th} \xrightarrow[\beta^-, \, 22.3\text{ min}]{} {}^{233}_{91}\text{Pa} \xrightarrow[\beta^-, \, 26.97\text{ days}]{} {}^{233}_{92}\text{U} \quad (\text{Fissile!})$$
  </li>
</ol>
Fertile isotopes constitute $>99.27\%$ of natural uranium (${}^{238}\text{U}$) and $100\%$ of natural thorium (${}^{232}\text{Th}$), representing over $99\%$ of the planet's mineable nuclear fuel reserves.
</p>
"""
        },
        {
            "id": "sec-1-3",
            "title": "Breeding Physics: Conversion Ratio, Breeding Gain & Doubling Time",
            "content": r"""
<h3>1. Conversion Ratio and Breeding Ratio</h3>
<p>
In any nuclear reactor containing fertile material (${}^{238}\text{U}$ or ${}^{232}\text{Th}$), fissile fuel is simultaneously consumed by fission and produced by transmutation. We quantify this balance through the <strong>Conversion Ratio</strong> ($CR$), defined as:
$$CR \equiv \frac{\text{Average rate of production of new fissile nuclei}}{\text{Average rate of consumption (fission + capture) of fissile nuclei}} = \frac{\dot{N}_{\text{fissile, produced}}}{\dot{N}_{\text{fissile, consumed}}}$$
Classification based on $CR$:
<ul>
  <li><strong>Burner / Converter Reactor ($CR < 1$):</strong> Produces fewer fissile nuclei than it consumes. Commercial Light Water Reactors (LWRs) operate with $CR \approx 0.55\text{ to }0.65$.</li>
  <li><strong>Break-Even Reactor ($CR = 1$):</strong> Exactly replaces every fissile atom consumed.</li>
  <li><strong>Breeder Reactor ($CR > 1$):</strong> Produces more fissile fuel than it consumes. When $CR > 1$, it is designated the <strong>Breeding Ratio</strong> ($BR \equiv CR$).</li>
</ul>
The net excess fissile production rate is governed by the <strong>Breeding Gain</strong> ($G$):
$$G \equiv BR - 1$$
</p>

<h3>2. The Doubling Time ($T_d$)</h3>
<p>
The <strong>doubling time</strong> $T_d$ is the operating time required for a breeder reactor to generate enough excess fissile material to completely fuel an identical second reactor (including out-of-pile reprocessing losses):
$$T_d \approx \frac{M_{\text{core}}}{G \cdot \dot{M}_{\text{fissile, consumed}}}$$
In terms of reactor electric power $P_e$, thermal efficiency $\eta_{\text{th}}$, and capacity factor $CF$:
$$T_d = \frac{M_{\text{fissile, inventory}}}{(BR - 1) \cdot (1 + \alpha) \cdot \dot{N}_{\text{fiss}} \cdot m_{\text{fiss}}}$$
Fast Breeder Reactors (FBRs) utilizing liquid metal cooling (Sodium or Lead) achieve breeding ratios of $BR \approx 1.20\text{ to }1.35$, yielding practical doubling times of $10\text{ to }20\text{ years}$.
</p>
""",
            "simulation": "reactor-atom-density-breeder-sim"
        },
        {
            "id": "sec-1-4",
            "title": "Mass-Energy Equivalence, Nuclear Mass Defect & Binding Energy",
            "content": r"""
<h3>1. Mass Defect $\Delta m$</h3>
<p>
According to Einstein's mass-energy equivalence relation $E = m c^2$, the ground-state mass of any bound nucleus $M(A, Z)$ is strictly less than the combined rest mass of its constituent free protons and neutrons:
$$\Delta m \equiv \left[ Z m_p + (A - Z) m_n \right] - M(A, Z)$$
where $m_p = 1.007276466\text{ u}$ is the proton mass, $m_n = 1.008664916\text{ u}$ is the neutron mass, and $1\text{ u} = 931.494\text{ MeV}/c^2$.
In terms of neutral atomic masses $M_{\text{atomic}}(A, Z)$ and hydrogen atom mass $m({}^1\text{H}) = 1.007825\text{ u}$:
$$\Delta m = \left[ Z m({}^1\text{H}) + (A - Z) m_n \right] - M_{\text{atomic}}(A, Z)$$
</p>

<h3>2. Total Binding Energy and Binding Energy per Nucleon</h3>
<p>
The total nuclear binding energy $B(A, Z)$ is the energy required to disassemble the bound nucleus into isolated, non-interacting nucleons:
$$B(A, Z) = \Delta m \cdot c^2 = \left( \left[ Z m({}^1\text{H}) + (A - Z) m_n \right] - M_{\text{atomic}}(A, Z) \right) \times 931.494\text{ MeV}$$
The binding energy per nucleon:
$$\frac{B}{A} = \frac{B(A, Z)}{A}$$
</p>
<table style="width:100%; border-collapse:collapse; margin:16px 0; font-size:0.95em;">
<thead>
<tr style="border-bottom:2px solid var(--border-color); text-align:left;">
<th style="padding:8px;">Isotope</th>
<th style="padding:8px;">Atomic Mass $M$ (u)</th>
<th style="padding:8px;">Total BE $B$ (MeV)</th>
<th style="padding:8px;">BE per Nucleon $B/A$ (MeV)</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid var(--border-color);">
<td style="padding:8px;">${}^2_1\text{H}$ (Deuteron)</td>
<td style="padding:8px;">$2.014102$</td>
<td style="padding:8px;">$2.2245$</td>
<td style="padding:8px;">$1.112$</td>
</tr>
<tr style="border-bottom:1px solid var(--border-color);">
<td style="padding:8px;">${}^4_2\text{He}$ (Alpha)</td>
<td style="padding:8px;">$4.002603$</td>
<td style="padding:8px;">$28.296$</td>
<td style="padding:8px;">$7.074$</td>
</tr>
<tr style="border-bottom:1px solid var(--border-color);">
<td style="padding:8px;">${}^{56}_{26}\text{Fe}$ (Peak Stability)</td>
<td style="padding:8px;">$55.934937$</td>
<td style="padding:8px;">$492.26$</td>
<td style="padding:8px;">$\mathbf{8.790}$</td>
</tr>
<tr style="border-bottom:1px solid var(--border-color);">
<td style="padding:8px;">${}^{235}_{92}\text{U}$</td>
<td style="padding:8px;">$235.043930$</td>
<td style="padding:8px;">$1783.87$</td>
<td style="padding:8px;">$7.590$</td>
</tr>
<tr>
<td style="padding:8px;">${}^{238}_{92}\text{U}$</td>
<td style="padding:8px;">$238.050788$</td>
<td style="padding:8px;">$1801.69$</td>
<td style="padding:8px;">$7.570$</td>
</tr>
</tbody>
</table>
"""
        },
        {
            "id": "sec-1-5",
            "title": "Neutron & Proton Separation Energies and the Fission Barrier",
            "content": r"""
<h3>1. Neutron Separation Energy ($S_n$)</h3>
<p>
The <strong>neutron separation energy</strong> $S_n$ is the minimum energy required to remove a single neutron from a nucleus $(A, Z)$, ejecting it to infinity at rest. It is the nuclear equivalent of the atomic ionization potential:
$${}^{A}_{Z}\text{X} + S_n \longrightarrow {}^{A-1}_{Z}\text{X} + n$$
Using binding energies or atomic masses:
$$S_n = B(A, Z) - B(A-1, Z) = \left[ M(A-1, Z) + m_n - M(A, Z) \right] c^2$$
Similarly, the proton separation energy is:
$$S_p = B(A, Z) - B(A-1, Z-1) = \left[ M(A-1, Z-1) + m({}^1\text{H}) - M(A, Z) \right] c^2$$
</p>

<h3>2. The Fission Barrier and Why ${}^{235}\text{U}$ is Fissile but ${}^{238}\text{U}$ is Not</h3>
<p>
When an incident neutron with kinetic energy $E_n$ is absorbed by target nucleus ${}^{A}_Z\text{X}$, the resulting compound nucleus $[{}^{A+1}_Z\text{X}]^*$ is formed in an excited state with excitation energy $E^*$:
$$E^* = S_n({}^{A+1}_Z\text{X}) + E_{\text{cm}} \approx S_n({}^{A+1}_Z\text{X}) + E_n \left( \frac{A}{A + 1} \right)$$
For thermal neutrons ($E_n \approx 0$), the entire excitation energy is simply the separation energy: $E^* \approx S_n$.
To induce fission, $E^*$ must exceed the <strong>critical fission barrier energy</strong> $E_{\text{crit}}$ required to deform the nucleus past the saddle point of the liquid drop potential:
</p>
<table style="width:100%; border-collapse:collapse; margin:16px 0; font-size:0.95em;">
<thead>
<tr style="border-bottom:2px solid var(--border-color); text-align:left;">
<th style="padding:8px;">Target Nucleus</th>
<th style="padding:8px;">Compound Nucleus</th>
<th style="padding:8px;">Separation Energy $S_n$</th>
<th style="padding:8px;">Fission Barrier $E_{\text{crit}}$</th>
<th style="padding:8px;">$S_n - E_{\text{crit}}$</th>
<th style="padding:8px;">Fissile by Thermal Neutrons?</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid var(--border-color);">
<td style="padding:8px;"><strong>${}^{235}_{92}\text{U}$ (Odd $N=143$)</strong></td>
<td style="padding:8px;">${}^{236}_{92}\text{U}$ (Even-Even)</td>
<td style="padding:8px;"><strong>$6.55\text{ MeV}$</strong></td>
<td style="padding:8px;">$5.70\text{ MeV}$</td>
<td style="padding:8px;">$+0.85\text{ MeV}$</td>
<td style="padding:8px;"><strong style="color:#10b981;">YES (Fissile!)</strong></td>
</tr>
<tr style="border-bottom:1px solid var(--border-color);">
<td style="padding:8px;"><strong>${}^{238}_{92}\text{U}$ (Even $N=146$)</strong></td>
<td style="padding:8px;">${}^{239}_{92}\text{U}$ (Even-Odd)</td>
<td style="padding:8px;"><strong>$4.81\text{ MeV}$</strong></td>
<td style="padding:8px;">$5.85\text{ MeV}$</td>
<td style="padding:8px;">$-1.04\text{ MeV}$</td>
<td style="padding:8px;"><span style="color:#ef4444;">NO (Threshold $\sim 1.1\text{ MeV}$)</span></td>
</tr>
<tr style="border-bottom:1px solid var(--border-color);">
<td style="padding:8px;"><strong>${}^{239}_{94}\text{Pu}$ (Odd $N=145$)</strong></td>
<td style="padding:8px;">${}^{240}_{94}\text{Pu}$ (Even-Even)</td>
<td style="padding:8px;"><strong>$6.53\text{ MeV}$</strong></td>
<td style="padding:8px;">$5.50\text{ MeV}$</td>
<td style="padding:8px;">$+1.03\text{ MeV}$</td>
<td style="padding:8px;"><strong style="color:#10b981;">YES (Fissile!)</strong></td>
</tr>
<tr>
<td style="padding:8px;"><strong>${}^{232}_{90}\text{Th}$ (Even $N=142$)</strong></td>
<td style="padding:8px;">${}^{233}_{90}\text{Th}$ (Even-Odd)</td>
<td style="padding:8px;"><strong>$4.79\text{ MeV}$</strong></td>
<td style="padding:8px;">$5.95\text{ MeV}$</td>
<td style="padding:8px;">$-1.16\text{ MeV}$</td>
<td style="padding:8px;"><span style="color:#ef4444;">NO (Threshold $\sim 1.2\text{ MeV}$)</span></td>
</tr>
</tbody>
</table>
<p>
The profound physical origin is the <strong>pairing term</strong> in the semi-empirical mass formula: when a neutron is added to odd-$N$ $^{235}\text{U}$, it forms a neutron pair in even-even $^{236}\text{U}$, releasing an extra $\sim 1.2\text{ MeV}$ of pairing energy ($\delta_{\text{pair}} \approx +12 A^{-1/2}\text{ MeV}$). This extra pairing energy pushes $E^*$ well above the critical fission barrier, making $^{235}\text{U}$ readily fissile by zero-energy thermal neutrons!
</p>
"""
        },
        {
            "id": "sec-1-6",
            "title": "Thermal Neutrons: Maxwell-Boltzmann Velocity Distribution & Energy Standards",
            "content": r"""
<h3>1. Thermalization and Thermodynamic Equilibrium</h3>
<p>
In a thermal reactor, fast fission neutrons undergo repeated elastic collisions with light moderator nuclei until they reach approximate thermodynamic equilibrium with the thermal motion of the moderator atoms at core temperature $T$.
The velocity distribution of thermal neutrons is given by the <strong>Maxwell-Boltzmann distribution</strong>:
$$n(v) dv = \frac{4 n_0}{\sqrt{\pi}} \left( \frac{m}{2 k_B T} \right)^{3/2} v^2 \exp\left( -\frac{m v^2}{2 k_B T} \right) dv$$
where $n_0$ is the total thermal neutron number density ($\text{neutrons/cm}^3$) and $k_B = 8.61733 \times 10^{-5}\text{ eV/K} = 1.38065 \times 10^{-23}\text{ J/K}$.
</p>

<h3>2. Characteristic Thermal Parameters</h3>
<p>
From the Maxwellian distribution, three characteristic velocities and energies arise:
<ol>
  <li><strong>Most Probable Speed ($v_0$):</strong> Located at the peak of $n(v)$ where $dn/dv = 0$:
  $$v_0 = \sqrt{\frac{2 k_B T}{m}}$$
  The corresponding kinetic energy is:
  $$E_0 = \frac{1}{2} m v_0^2 = k_B T$$
  At the international standard reference temperature $T_0 = 293.61\text{ K}$ ($20.46^\circ\text{C}$):
  $$E_0 = (8.61733 \times 10^{-5}\text{ eV/K})(293.61\text{ K}) = \mathbf{0.0253\text{ eV}}$$
  $$v_0 = \sqrt{\frac{2(0.0253 \times 1.6022 \times 10^{-19}\text{ J})}{1.67493 \times 10^{-27}\text{ kg}}} = \mathbf{2200\text{ m/s}}$$
  This defines the universally tabulated <strong>$2200\text{ m/s}$ standard cross-section reference state</strong>.</li>
  <li><strong>Average Speed ($\bar{v}$):</strong>
  $$\bar{v} = \int_0^\infty v \frac{n(v)}{n_0} dv = \sqrt{\frac{8 k_B T}{\pi m}} = \frac{2}{\sqrt{\pi}} v_0 \approx 1.128 v_0$$</li>
  <li><strong>Root-Mean-Square Speed ($v_{\text{rms}}$):</strong>
  $$v_{\text{rms}} = \sqrt{\langle v^2 \rangle} = \sqrt{\frac{3 k_B T}{m}} = \sqrt{\frac{3}{2}} v_0 \approx 1.225 v_0$$
  The average kinetic energy of the thermal neutron distribution is:
  $$\bar{E} = \frac{1}{2} m \langle v^2 \rangle = \frac{3}{2} k_B T = 1.5 E_0$$</li>
</ol>
</p>
"""
        },
        {
            "id": "sec-1-7",
            "title": "Atom Density Formalism: Elemental, Isotopic & Compound Formulations",
            "content": r"""
<h3>1. Atom Density of a Pure Element</h3>
<p>
In reactor physics, reaction rates are evaluated using the macroscopic cross section $\Sigma = N \sigma$, where $N$ is the <strong>atom density</strong> (number of target nuclei per unit volume, typically expressed in $\text{atoms/cm}^3$ or $\text{atoms/b}\cdot\text{cm}$, where $1\text{ b}\cdot\text{cm} = 10^{-24}\text{ cm}^3$).
For a pure element with mass density $\rho$ ($\text{g/cm}^3$) and atomic weight $M$ ($\text{g/mol}$):
$$N = \frac{\rho \cdot N_A}{M}$$
where $N_A = 6.02214076 \times 10^{23}\text{ atoms/mol}$ is Avogadro's number.
</p>

<h3>2. Isotopic Atom Densities in an Enriched Mixture</h3>
<p>
For an element composed of multiple isotopes $i$, if $a_i$ denotes the <em>atomic fraction</em> ($\sum a_i = 1$), the atomic weight of the mixture is $M = \sum a_i M_i$, and the individual isotopic density is:
$$N_i = a_i N = a_i \frac{\rho N_A}{M}$$
If the enrichment is given as a <em>weight (mass) fraction</em> $w_i \equiv m_i / m_{\text{total}}$ ($\sum w_i = 1$):
$$N_i = \frac{w_i \cdot \rho \cdot N_A}{M_i}$$
The corresponding atomic fraction $a_i$ can be converted via:
$$a_i = \frac{w_i / M_i}{\sum_j (w_j / M_j)}$$
</p>

<h3>3. Atom Densities in Chemical Compounds ($\text{A}_x\text{B}_y$)</h3>
<p>
For a homogeneous chemical compound with chemical formula $\text{A}_x\text{B}_y$, molecular weight $M_{\text{mol}} = x M_A + y M_B$, and mass density $\rho_{\text{comp}}$:
The molecular density $N_{\text{mol}}$ is:
$$N_{\text{mol}} = \frac{\rho_{\text{comp}} \cdot N_A}{M_{\text{mol}}}$$
The constituent elemental atom densities are:
$$N_A = x \cdot N_{\text{mol}} = x \frac{\rho_{\text{comp}} N_A}{M_{\text{mol}}}, \qquad N_B = y \cdot N_{\text{mol}} = y \frac{\rho_{\text{comp}} N_A}{M_{\text{mol}}}$$
For example, in water ($\text{H}_2\text{O}$, $\rho = 1.0\text{ g/cm}^3$, $M_{\text{mol}} = 18.015\text{ g/mol}$):
$$N_{\text{mol}} = \frac{1.0 \times 6.022 \times 10^{23}}{18.015} \approx 3.343 \times 10^{22}\text{ molecules/cm}^3$$
$$N_H = 2 N_{\text{mol}} \approx 6.686 \times 10^{22}\text{ atoms/cm}^3, \qquad N_O = N_{\text{mol}} \approx 3.343 \times 10^{22}\text{ atoms/cm}^3$$
</p>
"""
        }
    ],
    "problems": [
        {
            "id": "rp-prob-1-1",
            "title": "Atom Density and Cross Section Calculation in Enriched UO2 Fuel",
            "statement": r"""A commercial Pressurized Water Reactor uses uranium dioxide fuel ($\text{UO}_2$) enriched to $4.0\text{ wt}\%$ in $^{235}\text{U}$ (with the remaining $96.0\text{ wt}\%$ being $^{238}\text{U}$).
The bulk density of the sintered fuel pellets is $\rho = 10.45\text{ g/cm}^3$.
Atomic masses: $M({}^{235}\text{U}) = 235.044\text{ g/mol}$, $M({}^{238}\text{U}) = 238.051\text{ g/mol}$, $M({}^{16}\text{O}) = 15.999\text{ g/mol}$.
Thermal microscopic fission cross sections: $\sigma_f({}^{235}\text{U}) = 585\text{ b}$, $\sigma_f({}^{238}\text{U}) \approx 0\text{ b}$.
Thermal microscopic absorption cross sections: $\sigma_a({}^{235}\text{U}) = 680\text{ b}$, $\sigma_a({}^{238}\text{U}) = 2.70\text{ b}$, $\sigma_a({}^{16}\text{O}) = 0.0002\text{ b}$.
(a) Calculate the average atomic weight of the uranium mixture and the molecular weight of the enriched $\text{UO}_2$.
(b) Calculate the atom densities $N({}^{235}\text{U})$, $N({}^{238}\text{U})$, and $N({}^{16}\text{O})$ in units of $\text{atoms/cm}^3$ and $\text{atoms/b}\cdot\text{cm}$.
(c) Calculate the thermal macroscopic fission cross section $\Sigma_f$ and absorption cross section $\Sigma_a$ of the fuel pellet in $\text{cm}^{-1}$.""",
            "solution": r"""**(a) Average Atomic and Molecular Weights:**
Using weight fractions $w_{235} = 0.040$ and $w_{238} = 0.960$:
The average atomic weight of uranium $M_U$ is:
$$\frac{1}{M_U} = \frac{w_{235}}{M_{235}} + \frac{w_{238}}{M_{238}} = \frac{0.040}{235.044} + \frac{0.960}{238.051} = 1.7018 \times 10^{-4} + 4.0328 \times 10^{-3} = 4.2030 \times 10^{-3}\text{ mol/g}$$
$$M_U = \frac{1}{4.2030 \times 10^{-3}} \approx \mathbf{237.927\text{ g/mol}}$$
Molecular weight of $\text{UO}_2$:
$$M_{\text{UO}_2} = M_U + 2 M_O = 237.927 + 2(15.999) = \mathbf{269.925\text{ g/mol}}$$

**(b) Atom Densities:**
Molecular density of $\text{UO}_2$:
$$N_{\text{mol}} = \frac{\rho \cdot N_A}{M_{\text{UO}_2}} = \frac{10.45\text{ g/cm}^3 \times 6.02214 \times 10^{23}\text{ molecules/mol}}{269.925\text{ g/mol}} \approx \mathbf{2.3314 \times 10^{22}\text{ molecules/cm}^3}$$
Total Uranium density $N_U = N_{\text{mol}} = 2.3314 \times 10^{22}\text{ atoms/cm}^3$.
Oxygen density:
$$N_O = 2 N_{\text{mol}} = 2 \times 2.3314 \times 10^{22} \approx \mathbf{4.6628 \times 10^{22}\text{ atoms/cm}^3} = \mathbf{0.04663\text{ atoms/b}\cdot\text{cm}}$$
Using mass fraction formulas directly for individual uranium isotopes:
$$N_{235} = \frac{w_{235} \cdot (M_U / M_{\text{UO}_2}) \cdot \rho \cdot N_A}{M_{235}} = \frac{w_{235} \rho_U N_A}{M_{235}}$$
Since the mass fraction of Uranium in $\text{UO}_2$ is $f_U = M_U / M_{\text{UO}_2} = 237.927 / 269.925 \approx 0.88146$:
$$\rho_U = 0.88146 \times 10.45\text{ g/cm}^3 \approx 9.2113\text{ g }U/\text{cm}^3$$
$$\rho_{235} = 0.040 \times 9.2113 = 0.36845\text{ g/cm}^3$$
$$N_{235} = \frac{0.36845 \times 6.02214 \times 10^{23}}{235.044} \approx \mathbf{9.440 \times 10^{20}\text{ atoms/cm}^3} = \mathbf{9.440 \times 10^{-4}\text{ atoms/b}\cdot\text{cm}}$$
For ${}^{238}\text{U}$:
$$\rho_{238} = 0.960 \times 9.2113 = 8.8428\text{ g/cm}^3$$
$$N_{238} = \frac{8.8428 \times 6.02214 \times 10^{23}}{238.051} \approx \mathbf{2.2370 \times 10^{22}\text{ atoms/cm}^3} = \mathbf{0.02237\text{ atoms/b}\cdot\text{cm}}$$
Check: $N_{235} + N_{238} = 0.0944 \times 10^{22} + 2.2370 \times 10^{22} = 2.3314 \times 10^{22} = N_U$. (Exact match!)

**(c) Macroscopic Fission and Absorption Cross Sections:**
Recall $1\text{ b} = 10^{-24}\text{ cm}^2$:
$$\Sigma_f = N_{235} \sigma_f^{235} + N_{238} \sigma_f^{238} = (9.440 \times 10^{20}\text{ cm}^{-3})(585 \times 10^{-24}\text{ cm}^2) + 0 \approx \mathbf{0.5522\text{ cm}^{-1}}$$
Macroscopic absorption cross section:
$$\Sigma_a = N_{235}\sigma_a^{235} + N_{238}\sigma_a^{238} + N_O\sigma_a^O$$
$$\Sigma_a = (9.440 \times 10^{20})(680 \times 10^{-24}) + (2.2370 \times 10^{22})(2.70 \times 10^{-24}) + (4.6628 \times 10^{22})(0.0002 \times 10^{-24})$$
$$\Sigma_a = 0.64192\text{ cm}^{-1} + 0.06040\text{ cm}^{-1} + 9.3 \times 10^{-6}\text{ cm}^{-1} \approx \mathbf{0.7023\text{ cm}^{-1}}$$
The thermal macroscopic fission cross section is **$0.552\text{ cm}^{-1}$** and the total absorption cross section is **$0.702\text{ cm}^{-1}$**."""
        },
        {
            "id": "rp-prob-1-2",
            "title": "Neutron Separation Energies and Critical Fission Barrier Evaluation",
            "statement": r"""Given the high-precision atomic masses:
$M({}^{235}\text{U}) = 235.043930\text{ u}$
$M({}^{236}\text{U}) = 236.045568\text{ u}$
$M({}^{238}\text{U}) = 238.050788\text{ u}$
$M({}^{239}\text{U}) = 239.054293\text{ u}$
$m_n = 1.0086649\text{ u}$, $1\text{ u} = 931.494\text{ MeV}/c^2$.
The critical deformation barriers against fission are $E_{\text{crit}}({}^{236}\text{U}) = 5.70\text{ MeV}$ and $E_{\text{crit}}({}^{239}\text{U}) = 5.85\text{ MeV}$.
(a) Calculate the neutron separation energy $S_n$ for the compound nucleus $^{236}\text{U}^*$ formed by neutron capture on $^{235}\text{U}$.
(b) Calculate the neutron separation energy $S_n$ for the compound nucleus $^{239}\text{U}^*$ formed by neutron capture on $^{238}\text{U}$.
(c) Comparing $S_n$ with the critical fission barriers, determine whether zero-energy thermal neutrons can induce fission in $^{235}\text{U}$ and $^{238}\text{U}$, and compute the minimum threshold laboratory kinetic energy $E_{\text{th}}$ required for neutrons to induce fission in $^{238}\text{U}$.""",
            "solution": r"""**(a) Neutron Separation Energy of $^{236}\text{U}^*$:**
The capture reaction is $n + {}^{235}\text{U} \to {}^{236}\text{U}^*$.
$$\Delta m({}^{236}\text{U}) = \left[ M({}^{235}\text{U}) + m_n \right] - M({}^{236}\text{U})$$
$$\Delta m({}^{236}\text{U}) = [235.043930 + 1.0086649] - 236.045568 = 236.0525949 - 236.045568 = 0.0070269\text{ u}$$
In energy units:
$$S_n({}^{236}\text{U}^*) = 0.0070269\text{ u} \times 931.494\text{ MeV/u} \approx \mathbf{6.5455\text{ MeV}}$$

**(b) Neutron Separation Energy of $^{239}\text{U}^*$:**
The capture reaction is $n + {}^{238}\text{U} \to {}^{239}\text{U}^*$.
$$\Delta m({}^{239}\text{U}) = \left[ M({}^{238}\text{U}) + m_n \right] - M({}^{239}\text{U})$$
$$\Delta m({}^{239}\text{U}) = [238.050788 + 1.0086649] - 239.054293 = 239.0594529 - 239.054293 = 0.0051599\text{ u}$$
In energy units:
$$S_n({}^{239}\text{U}^*) = 0.0051599\text{ u} \times 931.494\text{ MeV/u} \approx \mathbf{4.8064\text{ MeV}}$$

**(c) Comparison with Fission Barriers & Threshold Energy:**
1. **For $^{235}\text{U}$:**
   $$E^* = S_n({}^{236}\text{U}^*) = 6.546\text{ MeV}$$
   $$E_{\text{crit}}({}^{236}\text{U}) = 5.70\text{ MeV}$$
   $$E^* - E_{\text{crit}} = 6.546 - 5.70 = \mathbf{+0.846\text{ MeV} > 0}$$
   Because the excitation energy delivered purely by neutron binding exceeds the fission barrier by $0.85\text{ MeV}$, **thermal neutrons readily induce fission in $^{235}\text{U}$ with colossal cross section ($\sigma_f = 585\text{ b}$)**!
2. **For $^{238}\text{U}$:**
   $$E^* = S_n({}^{239}\text{U}^*) = 4.806\text{ MeV}$$
   $$E_{\text{crit}}({}^{239}\text{U}) = 5.85\text{ MeV}$$
   $$E^* - E_{\text{crit}} = 4.806 - 5.85 = \mathbf{-1.044\text{ MeV} < 0}$$
   Thermal neutrons leave the compound nucleus $1.04\text{ MeV}$ short of the saddle point.
   To overcome this deficit, the incident neutron must supply kinetic energy in the center-of-mass frame:
   $$E_{\text{cm}} \ge E_{\text{crit}} - S_n = 5.85\text{ MeV} - 4.806\text{ MeV} = 1.044\text{ MeV}$$
   Converting to laboratory frame kinetic energy ($E_{\text{lab}} = E_{\text{cm}} \frac{m_n + M_{238}}{M_{238}}$):
   $$E_{\text{th}} = 1.044\text{ MeV} \times \left( \frac{1 + 238}{238} \right) = 1.044 \times 1.0042 \approx \mathbf{1.048\text{ MeV}}$$
   Neutrons must have at least **$\approx 1.05\text{ MeV}$** of kinetic energy to induce fission in $^{238}\text{U}$!"""
        },
        {
            "id": "rp-prob-1-3",
            "title": "Breeder Reactor Breeding Ratio, Breeding Gain and Doubling Time",
            "statement": r"""A liquid-metal fast breeder reactor (LMFBR) generates a steady thermal power of $P_{\text{th}} = 2500\text{ MWth}$.
The reactor core operates with a breeding ratio $BR = 1.25$ and an initial core fissile inventory of $M_{\text{fiss}} = 3200\text{ kg}$ of $^{239}\text{Pu}$.
Each fission of $^{239}\text{Pu}$ releases an average recoverable energy of $Q = 205\text{ MeV}$.
The ratio of parasitic capture to fission in the core fissile fuel is $\alpha \equiv \sigma_c / \sigma_f = 0.15$.
Out-of-pile reprocessing and refabrication losses are $2.0\%$ of the bred fuel, and the reactor capacity factor is $CF = 0.85$.
(a) Calculate the daily fission rate $\dot{N}_f$ and the daily mass of $^{239}\text{Pu}$ consumed by fission and absorption.
(b) Calculate the net daily production rate of excess fissile $^{239}\text{Pu}$.
(c) Determine the simple doubling time $T_d$ of the breeder reactor in calendar years.""",
            "solution": r"""**(a) Fission Rate and Daily Consumption:**
Energy per fission in Joules:
$$E_f = 205\text{ MeV} \times 1.60218 \times 10^{-13}\text{ J/MeV} = 3.2845 \times 10^{-11}\text{ J/fission}$$
At $P_{\text{th}} = 2500\text{ MWth} = 2.5 \times 10^9\text{ J/s}$:
$$\dot{N}_f = \frac{P_{\text{th}}}{E_f} = \frac{2.5 \times 10^9\text{ J/s}}{3.2845 \times 10^{-11}\text{ J/fission}} \approx 7.6115 \times 10^{19}\text{ fissions/sec}$$
Daily fissions ($1\text{ day} = 86400\text{ s}$):
$$N_{f, \text{day}} = 7.6115 \times 10^{19} \times 86400 \approx \mathbf{6.576 \times 10^{24}\text{ fissions/day}}$$
Mass consumed by fission alone per day:
$$m_{f, \text{day}} = \frac{N_{f, \text{day}} \cdot M_{239}}{N_A} = \frac{(6.576 \times 10^{24})(0.23905\text{ kg/mol})}{6.02214 \times 10^{23}} \approx \mathbf{2.610\text{ kg/day}}$$
Total fissile consumption includes radiative capture ($1 + \alpha = 1 + 0.15 = 1.15$):
$$\dot{m}_{\text{consumed}} = (1 + \alpha) \cdot m_{f, \text{day}} = 1.15 \times 2.610\text{ kg/day} \approx \mathbf{3.002\text{ kg } {}^{239}\text{Pu/day}}$$

**(b) Net Daily Production Rate of Excess Fissile $^{239}\text{Pu}$:**
By definition of breeding ratio:
$$\dot{m}_{\text{produced}} = BR \cdot \dot{m}_{\text{consumed}} = 1.25 \times 3.002\text{ kg/day} \approx 3.7525\text{ kg/day}$$
Gross excess production:
$$\Delta\dot{m}_{\text{gross}} = \dot{m}_{\text{produced}} - \dot{m}_{\text{consumed}} = (BR - 1) \cdot \dot{m}_{\text{consumed}} = 0.25 \times 3.002 = 0.7505\text{ kg/day}$$
Accounting for $2.0\%$ reprocessing loss ($\eta_{\text{rep}} = 0.98$):
$$\Delta\dot{m}_{\text{net, operating}} = 0.7505\text{ kg/day} - 0.02(3.7525\text{ kg/day}) = 0.7505 - 0.0751 \approx \mathbf{0.6754\text{ kg/day}}$$
Accounting for capacity factor $CF = 0.85$:
$$\Delta\dot{m}_{\text{annual}} = 0.6754\text{ kg/day} \times (365.25 \times 0.85\text{ days}) = 0.6754 \times 310.46 \approx \mathbf{209.7\text{ kg/calendar year}}$$

**(c) Simple Doubling Time $T_d$:**
The doubling time is the time required to accumulate the initial core inventory $M_{\text{fiss}} = 3200\text{ kg}$:
$$T_d = \frac{M_{\text{fiss}}}{\Delta\dot{m}_{\text{annual}}} = \frac{3200\text{ kg}}{209.7\text{ kg/yr}} \approx \mathbf{15.26\text{ calendar years}}$$
The simple doubling time of the breeder reactor is **$\approx 15.3\text{ years}$**."""
        }
    ]
}

u2_data = {
    "title": "Neutron Interactions, Cross Sections & Nuclear Reaction Rates",
    "subtitle": "Microscopic & Macroscopic Cross Sections, Mean Free Path, Beam Attenuation & Reaction Rates",
    "summary": "Detailed exploration of neutron interactions with matter: classification of neutrons across seven energy decades from relativistic to cold thermal states; laboratory and reactor neutron production mechanisms; physical definitions and units of microscopic cross sections (barns) and macroscopic cross sections (cm⁻¹); the concept of neutron mean free path; exponential beam attenuation through bulk materials; scalar neutron flux φ = nv and vector current density; volumetric nuclear reaction rate calculations R = Σφ; energy-dependent cross section phenomena including the low-energy 1/v absorption law, Doppler-broadened Breit-Wigner resonances, and fission thresholds; and thermal Maxwellian-averaged cross sections with Westcott g-factor corrections.",
    "sections": [
        {
            "id": "sec-2-1",
            "title": "Classification of Neutrons by Kinetic Energy & Nuclear Sources",
            "content": r"""
<h3>1. The Energy Spectrum of Neutrons</h3>
<p>
Neutrons produced in nuclear fission are born with high kinetic energies averaging $\bar{E} \approx 2\text{ MeV}$, but subsequently moderate across nine orders of magnitude down to thermal equilibrium ($E \sim 0.025\text{ eV}$). Reactor physics categorizes neutrons into well-defined energy regimes:
</p>
<table style="width:100%; border-collapse:collapse; margin:16px 0; font-size:0.95em;">
<thead>
<tr style="border-bottom:2px solid var(--border-color); text-align:left;">
<th style="padding:8px;">Neutron Classification</th>
<th style="padding:8px;">Energy Range</th>
<th style="padding:8px;">Typical Speed</th>
<th style="padding:8px;">Dominant Interaction Mechanism</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid var(--border-color);">
<td style="padding:8px;"><strong>Relativistic / High Energy</strong></td>
<td style="padding:8px;">$E > 20\text{ MeV}$</td>
<td style="padding:8px;">$> 0.2 c$</td>
<td style="padding:8px;">Nuclear spallation, meson production</td>
</tr>
<tr style="border-bottom:1px solid var(--border-color);">
<td style="padding:8px;"><strong>Fast Neutrons</strong></td>
<td style="padding:8px;">$0.1\text{ MeV} < E \le 20\text{ MeV}$</td>
<td style="padding:8px;">$\sim 1.4 \times 10^7\text{ m/s}$</td>
<td style="padding:8px;">Fission spectrum; elastic & inelastic scattering</td>
</tr>
<tr style="border-bottom:1px solid var(--border-color);">
<td style="padding:8px;"><strong>Epithermal / Intermediate</strong></td>
<td style="padding:8px;">$1\text{ eV} < E \le 0.1\text{ MeV}$</td>
<td style="padding:8px;">$\sim 10^5\text{ to }10^6\text{ m/s}$</td>
<td style="padding:8px;">Elastic moderation ($1/E$ slowing-down spectrum)</td>
</tr>
<tr style="border-bottom:1px solid var(--border-color);">
<td style="padding:8px;"><strong>Resonance Neutrons</strong></td>
<td style="padding:8px;">$1\text{ eV} \le E \le 1\text{ keV}$</td>
<td style="padding:8px;">$\sim 10^4\text{ to }10^5\text{ m/s}$</td>
<td style="padding:8px;">Sharp $(n,\gamma)$ capture resonances ($^{238}\text{U}$)</td>
</tr>
<tr style="border-bottom:1px solid var(--border-color);">
<td style="padding:8px;"><strong>Thermal Neutrons</strong></td>
<td style="padding:8px;">$0.01\text{ eV} \le E \le 0.5\text{ eV}$</td>
<td style="padding:8px;">$2200\text{ m/s}$</td>
<td style="padding:8px;">Thermal equilibrium with moderator; fission in $^{235}\text{U}$</td>
</tr>
<tr>
<td style="padding:8px;"><strong>Cold & Ultracold (UCN)</strong></td>
<td style="padding:8px;">$E < 0.005\text{ eV}$ (UCN $< 10^{-7}\text{ eV}$)</td>
<td style="padding:8px;">$< 100\text{ m/s}$ ($< 5\text{ m/s}$)</td>
<td style="padding:8px;">Bragg reflection, total internal reflection in pipes</td>
</tr>
</tbody>
</table>

<h3>2. Laboratory and Startup Neutron Sources</h3>
<p>
To start up a subcritical nuclear reactor safely, external neutron sources are installed to provide an initial detectable neutron flux for nuclear instrumentation:
</p>
<ul>
  <li><strong>Alpha-Neutron $(\alpha, n)$ Sources:</strong> Utilize alpha decay from actinides mixed with beryllium-9:
  $${}^9_4\text{Be} + \alpha \longrightarrow {}^{12}_6\text{C} + n + 5.70\text{ MeV}$$
  Standard commercial sources include $\text{Am-Be}$ ($T_{1/2} = 432\text{ yr}$) and $\text{Pu-Be}$.</li>
  <li><strong>Photoneutron $(\gamma, n)$ Sources:</strong> Photons exceeding the low neutron binding energy of deuterium ($2.22\text{ MeV}$) or beryllium ($1.67\text{ MeV}$):
  $${}^9_4\text{Be} + \gamma (> 1.67\text{ MeV}) \longrightarrow {}^8_4\text{Be} + n$$
  A common source is Antimony-Beryllium (${}^{124}\text{Sb}\text{-Be}$), where $^{124}\text{Sb}$ emits $1.69\text{ MeV}$ gammas.</li>
  <li><strong>Spontaneous Fission Sources:</strong> Californium-252 (${}^{252}_{98}\text{Cf}$, $T_{1/2} = 2.645\text{ yr}$) decays $3.09\%$ by spontaneous fission, emitting an intense stream of $3.76$ neutrons per fission ($2.3 \times 10^{12}\text{ n/s per gram}$).</li>
</ul>
"""
        },
        {
            "id": "sec-2-2",
            "title": "Microscopic Cross Sections: Geometric Analogy & Probability Units",
            "content": r"""
<h3>1. Definition of the Microscopic Cross Section $\sigma$</h3>
<p>
Consider a monodirectional, uniform beam of neutrons of intensity $I$ ($\text{neutrons/cm}^2\cdot\text{s}$) impinging perpendicularly upon a thin target containing a single isolated nucleus.
The probability per unit time that a specific nuclear reaction occurs is directly proportional to the incident beam intensity $I$:
$$\text{Interaction Rate} = \sigma \cdot I$$
The constant of proportionality $\sigma$ has dimensions of <strong>area</strong> ($\text{cm}^2/\text{nucleus}$) and represents the <strong>effective target area</strong> that the nucleus presents to the passing neutron.
</p>
<p>
Because nuclear radii are on the order of $R \sim 10^{-12}\text{ cm}$, typical geometric cross sections are:
$$\sigma_{\text{geom}} \approx \pi R^2 \approx \pi (10^{-12}\text{ cm})^2 = 3.14 \times 10^{-24}\text{ cm}^2$$
To establish a convenient unit, nuclear physicists in the 1940s Manhattan Project coined the <strong>barn</strong> ($\text{b}$):
$$1\text{ barn (b)} \equiv 10^{-24}\text{ cm}^2 = 10^{-28}\text{ m}^2$$
Sub-units include millibarns ($1\text{ mb} = 10^{-3}\text{ b} = 10^{-27}\text{ cm}^2$) and microbarns ($1\text{ }\mu\text{b} = 10^{-6}\text{ b}$).
</p>

<h3>2. Partial and Total Cross Sections</h3>
<p>
A neutron can interact with a nucleus through multiple mutually exclusive reaction channels:
$$\sigma_t = \sigma_s + \sigma_a$$
<ol>
  <li><strong>Scattering Cross Section ($\sigma_s$):</strong>
  $$\sigma_s = \sigma_e + \sigma_i$$
  where $\sigma_e$ is elastic potential and resonance scattering $(n, n)$ (kinetic energy conserved in CM frame), and $\sigma_i$ is inelastic scattering $(n, n')$ (leaving target nucleus in an excited state).</li>
  <li><strong>Absorption Cross Section ($\sigma_a$):</strong>
  $$\sigma_a = \sigma_\gamma + \sigma_f + \sigma_\alpha + \sigma_p$$
  where $\sigma_\gamma$ is radiative capture $(n, \gamma)$, $\sigma_f$ is neutron-induced fission $(n, f)$, $\sigma_\alpha$ is alpha emission $(n, \alpha)$, and $\sigma_p$ is proton ejection $(n, p)$.</li>
</ol>
The total interaction probability is governed by the <strong>total microscopic cross section</strong> $\sigma_t$.
</p>
"""
        },
        {
            "id": "sec-2-3",
            "title": "Macroscopic Cross Sections & Neutron Mean Free Path",
            "content": r"""
<h3>1. The Macroscopic Cross Section $\Sigma$</h3>
<p>
In a macroscopic medium containing target nuclei with atom density $N$ ($\text{nuclei/cm}^3$), the <strong>macroscopic cross section</strong> $\Sigma$ represents the total interaction probability per unit distance traveled by a neutron:
$$\Sigma \equiv N \cdot \sigma \quad [\text{cm}^{-1}]$$
Physical significance of dimensions:
$$\Sigma = \left( \frac{\text{nuclei}}{\text{cm}^3} \right) \times \left( \frac{\text{cm}^2}{\text{nucleus}} \right) = \mathbf{\text{cm}^{-1}}$$
For a homogeneous mixture of $K$ distinct isotopic species:
$$\Sigma = \sum_{i=1}^K N_i \sigma_i = N_1 \sigma_1 + N_2 \sigma_2 + \dots + N_K \sigma_K$$
Total macroscopic cross section:
$$\Sigma_t = \Sigma_s + \Sigma_a = \Sigma_e + \Sigma_i + \Sigma_\gamma + \Sigma_f$$
</p>

<h3>2. The Neutron Mean Free Path $\lambda$</h3>
<p>
The <strong>mean free path</strong> $\lambda$ is the average distance a neutron travels through a medium between two successive collisions.
The probability that a neutron travels distance $x$ without interaction is $e^{-\Sigma_t x}$, and the probability of colliding in differential slice $dx$ is $\Sigma_t dx$. Thus, the collision probability density is:
$$p(x) dx = \Sigma_t e^{-\Sigma_t x} dx$$
The expectation value of travel distance is:
$$\lambda \equiv \langle x \rangle = \int_0^\infty x \, p(x) dx = \Sigma_t \int_0^\infty x e^{-\Sigma_t x} dx = \Sigma_t \left[ \frac{1}{\Sigma_t^2} \right] = \mathbf{\frac{1}{\Sigma_t}}$$
Partial mean free paths:
$$\lambda_s = \frac{1}{\Sigma_s} \quad \text{(Mean free path for scattering)}, \qquad \lambda_a = \frac{1}{\Sigma_a} \quad \text{(Mean free path for absorption)}$$
Because $\Sigma_t = \Sigma_s + \Sigma_a$:
$$\frac{1}{\lambda_t} = \frac{1}{\lambda_s} + \frac{1}{\lambda_a}$$
In light water, thermal neutrons have $\lambda_s \approx 0.3\text{ cm}$ and $\lambda_a \approx 45\text{ cm}$, demonstrating that a neutron scatters over a hundred times before undergoing absorption!
</p>
"""
        },
        {
            "id": "sec-2-4",
            "title": "Neutron Beam Attenuation & Transmission Probability",
            "content": r"""
<h3>1. Derivation of the Exponential Attenuation Law</h3>
<p>
Consider a collimated, monoenergetic neutron beam of initial intensity $I_0$ ($\text{neutrons/cm}^2\cdot\text{s}$) entering a slab of material at normal incidence ($x = 0$).
Let $I(x)$ denote the uncollided beam intensity at depth $x$. In traversing a differential layer of thickness $dx$:
The number of collisions occurring in unit area per second is:
$$-dI(x) = I(x) \cdot \Sigma_t \cdot dx$$
Rearranging into a differential equation:
$$\frac{dI(x)}{dx} = -\Sigma_t I(x)$$
Integrating with boundary condition $I(0) = I_0$:
$$\int_{I_0}^{I(x)} \frac{dI}{I} = -\Sigma_t \int_0^x dx \implies \ln\left( \frac{I(x)}{I_0} \right) = -\Sigma_t x$$
$$I(x) = I_0 \exp(-\Sigma_t x)$$
This is the fundamental <strong>exponential attenuation law for uncollided neutrons</strong>.
</p>

<h3>2. Transmission, Absorption, and Half-Value Thickness</h3>
<p>
For a shield slab of total physical thickness $t$:
<ul>
  <li><strong>Transmission Probability ($T$):</strong> The fraction of the beam penetrating without undergoing any interaction:
  $$T \equiv \frac{I(t)}{I_0} = e^{-\Sigma_t t}$$</li>
  <li><strong>Interaction Probability ($P_{\text{int}}$):</strong> The fraction undergoing at least one collision:
  $$P_{\text{int}} = 1 - T = 1 - e^{-\Sigma_t t}$$</li>
  <li><strong>Half-Value Layer ($HVL$):</strong> The thickness of material required to reduce the uncollided beam intensity by exactly $50\%$ ($I/I_0 = 1/2$):
  $$e^{-\Sigma_t \cdot HVL} = \frac{1}{2} \implies HVL = \frac{\ln 2}{\Sigma_t} = \frac{0.69315}{\Sigma_t} \approx 0.693 \lambda_t$$</li>
  <li><strong>Tenth-Value Layer ($TVL$):</strong> The thickness required to attenuate the uncollided beam by a factor of 10:
  $$TVL = \frac{\ln 10}{\Sigma_t} = \frac{2.3026}{\Sigma_t}$$</li>
</ul>
</p>
""",
            "simulation": "reactor-neutron-attenuation-flux-sim"
        },
        {
            "id": "sec-2-5",
            "title": "Neutron Flux, Current Density & Total Reaction Rates",
            "content": r"""
<h3>1. Scalar Neutron Flux $\phi(\vec{r}, E)$</h3>
<p>
In a reactor core, neutrons are not collimated into a single beam; they travel isotropically in all directions. If $n(\vec{r}, E) dE$ is the density of neutrons ($\text{neutrons/cm}^3$) at position $\vec{r}$ with energy in $dE$, and $v$ is their speed:
The <strong>scalar neutron flux</strong> $\phi(\vec{r}, E)$ is defined as:
$$\phi(\vec{r}, E) \equiv n(\vec{r}, E) \cdot v \quad [\text{neutrons/cm}^2\cdot\text{s}]$$
Physical interpretation: $\phi$ is the total track length swept out by all neutrons contained within a unit volume per second ($\text{cm of track} / \text{cm}^3\cdot\text{s} = \text{cm}^{-2}\text{s}^{-1}$).
</p>

<h3>2. Neutron Current Density Vector $\vec{J}(\vec{r}, E)$</h3>
<p>
While scalar flux $\phi$ is an orientation-independent scalar measure of neutron activity, the <strong>neutron current density</strong> $\vec{J}$ is a vector describing the net rate of flow of neutrons across a unit surface oriented perpendicular to $\vec{J}$:
$$\vec{J}(\vec{r}, E) \equiv \int_{4\pi} \vec{\Omega} \, \psi(\vec{r}, \vec{\Omega}, E) \, d\Omega$$
where $\psi(\vec{r}, \vec{\Omega}, E) = v \cdot n(\vec{r}, \vec{\Omega}, E)$ is the angular flux.
In an isotropic neutron field, the current vanishes ($\vec{J} = 0$), but the scalar flux remains non-zero ($\phi > 0$).
</p>

<h3>3. Volumetric Reaction Rate Density</h3>
<p>
The volumetric reaction rate density $R_x(\vec{r})$ (number of reactions of type $x$ occurring per unit volume per second) is given by:
$$R_x(\vec{r}) = \int_0^\infty \Sigma_x(\vec{r}, E) \, \phi(\vec{r}, E) \, dE \quad [\text{reactions/cm}^3\cdot\text{s}]$$
For a monoenergetic or one-group thermal flux $\phi_{\text{th}}$:
$$R_x = \Sigma_x \phi_{\text{th}} = N \sigma_x \phi_{\text{th}}$$
Integrating over the entire reactor core volume $V_{\text{core}}$ gives the total core reaction rate:
$$\mathcal{R}_x = \int_{V_{\text{core}}} \Sigma_x(\vec{r}) \phi(\vec{r}) d^3r \quad [\text{reactions/s}]$$
For nuclear fission, the total thermal power $P$ released is:
$$P = Q_f \cdot \mathcal{R}_f = Q_f \int_{V_{\text{core}}} \Sigma_f(\vec{r}) \phi(\vec{r}) d^3r \quad [\text{Watts}]$$
</p>
"""
        },
        {
            "id": "sec-2-6",
            "title": "Energy Dependence of Cross Sections: 1/v Law, Resonances & Fission",
            "content": r"""
<h3>1. The $1/v$ Low-Energy Law</h3>
<p>
In the low-energy region below isolated resonances ($E \lesssim 0.1\text{ eV}$), quantum perturbation theory predicts that the probability of absorbing an $s$-wave ($l = 0$) neutron is proportional to the time the neutron spends in the vicinity of the nuclear potential well:
$$\text{Interaction Time} \Delta t \propto \frac{R_{\text{nuc}}}{v} \propto \frac{1}{\sqrt{E}}$$
Consequently, for almost all non-threshold absorption reactions, the microscopic cross section follows the universal <strong>$1/v$ law</strong>:
$$\sigma_a(v) = \sigma_a(v_0) \frac{v_0}{v} = \sigma_a(E_0) \sqrt{\frac{E_0}{E}}$$
where $v_0 = 2200\text{ m/s}$ and $E_0 = 0.0253\text{ eV}$.
Plotted on a $\log\sigma_a$ versus $\log E$ graph, the $1/v$ cross section is a straight line with a characteristic slope of $-1/2$:
$$\log\sigma_a = \text{const} - \frac{1}{2}\log E$$
</p>

<h3>2. Breit-Wigner Resonances and Doppler Broadening</h3>
<p>
In the intermediate energy regime ($1\text{ eV} \le E \le 10\text{ keV}$), incident neutron energies match discrete compound nuclear quasi-bound states. The cross section exhibits colossal resonance peaks accurately parameterized by the single-level <strong>Breit-Wigner dispersion formula</strong>:
$$\sigma_\gamma(E) = \frac{\pi}{k^2} g_J \frac{\Gamma_n \Gamma_\gamma}{(E - E_0)^2 + (\Gamma/2)^2}$$
where $E_0$ is the resonance energy, $\Gamma = \Gamma_n + \Gamma_\gamma + \Gamma_f$ is the total resonance width, and $g_J$ is the statistical spin factor.
</p>
<p>
As the reactor fuel temperature $T$ increases, thermal vibrations of the actinide lattice nuclei broaden the relative velocity distribution between target nuclei and incident neutrons. This phenomenon—<strong>Doppler Broadening</strong>—flattens the peak height but broadens the resonance wings without altering the total area:
$$\Psi(\theta, x) = \frac{\theta}{2\sqrt{\pi}} \int_{-\infty}^\infty \frac{\exp\left( -\frac{\theta^2}{4}(x - y)^2 \right)}{1 + y^2} dy, \quad \theta \equiv \frac{\Gamma}{\Delta_{\text{Doppler}}}$$
In thick fuel rods, Doppler broadening exposes more neutrons to resonance capture (reducing self-shielding), providing an instantaneous, inherently safe <strong>negative temperature reactivity feedback</strong>!
</p>
"""
        },
        {
            "id": "sec-2-7",
            "title": "Thermal Maxwellian-Averaged Cross Sections & The Westcott g-Factor",
            "content": r"""
<h3>1. Maxwellian Average of $1/v$ Cross Sections</h3>
<p>
Because thermal neutrons are distributed across a continuous Maxwellian spectrum $n(v)$, the effective reaction rate in a thermal reactor is:
$$R_a = \int_0^\infty N \sigma_a(v) v \, n(v) \, dv$$
If the absorber obeys the ideal $1/v$ law ($\sigma_a(v) = \sigma_0 v_0 / v$):
$$R_a = N \sigma_0 v_0 \int_0^\infty n(v) dv = N \sigma_0 v_0 n_0$$
Defining the conventional 2200 m/s thermal flux $\phi_0 \equiv n_0 v_0$:
$$R_a = N \sigma_0 \phi_0 = \Sigma_0 \phi_0$$
Remarkably, for a pure $1/v$ absorber, the reaction rate is <em>independent</em> of the moderator temperature $T$ when evaluated using the 2200 m/s cross section $\sigma_0$ and the standard flux $\phi_0 = n_0 v_0$!
</p>

<h3>2. The Westcott $g$-Factor for Non-$1/v$ Absorbers</h3>
<p>
For nuclides that possess low-lying resonances near thermal energies (such as $^{235}\text{U}$, $^{239}\text{Pu}$, $^{241}\text{Pu}$, and $^{113}\text{Cd}$), the absorption cross section deviates significantly from $1/v$.
Carl Westcott introduced the dimensionless <strong>Westcott $g$-factor</strong> $g(T)$ to correct the 2200 m/s cross section:
$$g(T) \equiv \frac{1}{\sigma_0 v_0} \frac{\int_0^\infty \sigma_a(v) v \, n(v) \, dv}{\int_0^\infty n(v) \, dv} = \frac{\bar{\sigma}_a(T)}{\sigma_0} \frac{\bar{v}}{v_0} \frac{\sqrt{\pi}}{2}$$
The true thermal reaction rate is then calculated as:
$$R_a = g(T) \cdot \Sigma_0 \cdot \phi_0$$
<ul>
  <li>For an ideal $1/v$ absorber (such as Boron-10): $g(T) \equiv 1.000$ at all temperatures.</li>
  <li>For Uranium-235: $g_a(293.6\text{ K}) = 0.9780$, $g_f(293.6\text{ K}) = 0.9766$.</li>
  <li>For Plutonium-239: Due to a massive resonance at $0.296\text{ eV}$, $g_a(293.6\text{ K}) = 1.072$, rising above $1.4$ as coolant temperature rises to $600\text{ K}$!</li>
</ul>
</p>
"""
        }
    ],
    "problems": [
        {
            "id": "rp-prob-2-1",
            "title": "Neutron Beam Attenuation and Half-Value Thickness in Borated Polyethylene",
            "statement": r"""A narrow, collimated beam of thermal neutrons ($E = 0.0253\text{ eV}$) with initial intensity $I_0 = 1.5 \times 10^7\text{ neutrons/cm}^2\cdot\text{s}$ impinges perpendicularly upon a shielding slab of borated polyethylene ($5.0\text{ wt}\%$ natural Boron).
The mass density of the borated polyethylene is $\rho = 0.95\text{ g/cm}^3$.
Composition by weight: $5.0\%$ Boron ($M_B = 10.811\text{ g/mol}$), $13.6\%$ Hydrogen ($M_H = 1.008\text{ g/mol}$), and $81.4\%$ Carbon ($M_C = 12.011\text{ g/mol}$).
Microscopic cross sections at $0.0253\text{ eV}$:
- Boron: $\sigma_a = 767\text{ b}$, $\sigma_s = 4.0\text{ b}$
- Hydrogen: $\sigma_a = 0.332\text{ b}$, $\sigma_s = 21.0\text{ b}$
- Carbon: $\sigma_a = 0.0035\text{ b}$, $\sigma_s = 4.8\text{ b}$
(a) Calculate the atom densities $N_B, N_H, N_C$ in $\text{atoms/cm}^3$.
(b) Calculate the total macroscopic cross section $\Sigma_t$ in $\text{cm}^{-1}$ and the neutron mean free path $\lambda_t$ in $\text{cm}$.
(c) Determine the Half-Value Layer ($HVL$) and Tenth-Value Layer ($TVL$) of the shield.
(d) Calculate the thickness $t$ of the slab required to attenuate the uncollided beam intensity down to $I(t) = 100\text{ neutrons/cm}^2\cdot\text{s}$.""",
            "solution": r"""**(a) Atom Densities:**
Using $N_i = \frac{w_i \cdot \rho \cdot N_A}{M_i}$:
$$N_B = \frac{0.050 \times 0.95\text{ g/cm}^3 \times 6.02214 \times 10^{23}}{10.811\text{ g/mol}} \approx \mathbf{2.6457 \times 10^{21}\text{ atoms/cm}^3} = 2.6457 \times 10^{-3}\text{ b}^{-1}\text{cm}^{-1}$$
$$N_H = \frac{0.136 \times 0.95 \times 6.02214 \times 10^{23}}{1.008} \approx \mathbf{7.7214 \times 10^{22}\text{ atoms/cm}^3} = 0.07721\text{ b}^{-1}\text{cm}^{-1}$$
$$N_C = \frac{0.814 \times 0.95 \times 6.02214 \times 10^{23}}{12.011} \approx \mathbf{3.8757 \times 10^{22}\text{ atoms/cm}^3} = 0.03876\text{ b}^{-1}\text{cm}^{-1}$$

**(b) Total Macroscopic Cross Section $\Sigma_t$ and Mean Free Path $\lambda_t$:**
Total microscopic cross sections ($\sigma_t = \sigma_a + \sigma_s$):
$$\sigma_t(B) = 767 + 4.0 = 771\text{ b} = 771 \times 10^{-24}\text{ cm}^2$$
$$\sigma_t(H) = 0.332 + 21.0 = 21.332\text{ b} = 21.332 \times 10^{-24}\text{ cm}^2$$
$$\sigma_t(C) = 0.0035 + 4.8 = 4.8035\text{ b} = 4.8035 \times 10^{-24}\text{ cm}^2$$
Macroscopic cross section components:
$$\Sigma_t(B) = (2.6457 \times 10^{-3}\text{ b}^{-1}\text{cm}^{-1})(771\text{ b}) = 2.0398\text{ cm}^{-1}$$
$$\Sigma_t(H) = (0.07721)(21.332) = 1.6470\text{ cm}^{-1}$$
$$\Sigma_t(C) = (0.03876)(4.8035) = 0.1862\text{ cm}^{-1}$$
Total macroscopic cross section:
$$\Sigma_t = 2.0398 + 1.6470 + 0.1862 = \mathbf{3.873\text{ cm}^{-1}}$$
Mean free path:
$$\lambda_t = \frac{1}{\Sigma_t} = \frac{1}{3.873\text{ cm}^{-1}} \approx \mathbf{0.2582\text{ cm}} = \mathbf{2.58\text{ mm}}$$

**(c) Half-Value Layer ($HVL$) and Tenth-Value Layer ($TVL$):**
$$HVL = \frac{\ln 2}{\Sigma_t} = \frac{0.69315}{3.873\text{ cm}^{-1}} \approx \mathbf{0.1790\text{ cm}} \approx \mathbf{1.79\text{ mm}}$$
$$TVL = \frac{\ln 10}{\Sigma_t} = \frac{2.30259}{3.873\text{ cm}^{-1}} \approx \mathbf{0.5945\text{ cm}} \approx \mathbf{5.95\text{ mm}}$$

**(d) Required Shield Thickness for $I(t) = 100\text{ n/cm}^2\cdot\text{s}$:**
Using $I(t) = I_0 e^{-\Sigma_t t}$:
$$\frac{I(t)}{I_0} = \frac{100}{1.5 \times 10^7} = 6.6667 \times 10^{-6}$$
$$\ln\left( \frac{I(t)}{I_0} \right) = \ln(6.6667 \times 10^{-6}) = -11.9184$$
$$t = \frac{11.9184}{\Sigma_t} = \frac{11.9184}{3.873\text{ cm}^{-1}} \approx \mathbf{3.077\text{ cm}} \approx \mathbf{30.8\text{ mm}}$$
A shield plate of only **$3.08\text{ cm}$** ($1.2\text{ inches}$) thickness reduces the beam intensity by over five orders of magnitude!"""
        },
        {
            "id": "rp-prob-2-2",
            "title": "Thermal Reaction Rates and Westcott g-Factor Correction for Plutonium-239",
            "statement": r"""A research reactor core contains a high-purity foil of Plutonium-239 (${}^{239}\text{Pu}$) placed in a thermal neutron flux.
The 2200 m/s standard microscopic cross sections are $\sigma_0(f) = 748\text{ b}$ and $\sigma_0(a) = 1017\text{ b}$.
The neutron density in the thermal column is $n_0 = 5.0 \times 10^7\text{ neutrons/cm}^3$.
(a) Calculate the conventional 2200 m/s thermal flux $\phi_0$ in $\text{neutrons/cm}^2\cdot\text{s}$.
(b) At room temperature ($T_1 = 293.6\text{ K}$), the Westcott $g$-factors for $^{239}\text{Pu}$ are $g_f(T_1) = 1.055$ and $g_a(T_1) = 1.072$. Calculate the true effective thermal cross sections $\hat{\sigma}_f$ and $\hat{\sigma}_a$, and compute the microscopic fission rate per $^{239}\text{Pu}$ nucleus.
(c) When the core heats up to operating temperature $T_2 = 600\text{ K}$, the $0.296\text{ eV}$ resonance increases the Westcott factors to $g_f(T_2) = 1.340$ and $g_a(T_2) = 1.425$. For the same neutron density $n_0$, calculate the percentage increase in the fission rate per nucleus due to thermal spectrum hardening.""",
            "solution": r"""**(a) Conventional 2200 m/s Flux $\phi_0$:**
With standard reference velocity $v_0 = 2200\text{ m/s} = 2.2 \times 10^5\text{ cm/s}$:
$$\phi_0 = n_0 \cdot v_0 = (5.0 \times 10^7\text{ cm}^{-3})(2.2 \times 10^5\text{ cm/s}) = \mathbf{1.10 \times 10^{13}\text{ neutrons/cm}^2\cdot\text{s}}$$

**(b) Effective Cross Sections and Reaction Rates at $T_1 = 293.6\text{ K}$:**
The Westcott effective cross sections are $\hat{\sigma} = g(T) \cdot \sigma_0$:
$$\hat{\sigma}_f(T_1) = g_f(T_1) \cdot \sigma_0(f) = 1.055 \times 748\text{ b} \approx \mathbf{789.14\text{ b}} = 7.8914 \times 10^{-21}\text{ cm}^2$$
$$\hat{\sigma}_a(T_1) = g_a(T_1) \cdot \sigma_0(a) = 1.072 \times 1017\text{ b} \approx \mathbf{1090.22\text{ b}} = 1.0902 \times 10^{-20}\text{ cm}^2$$
Fission reaction rate per nucleus:
$$R_{f, 1} = \hat{\sigma}_f(T_1) \cdot \phi_0 = (7.8914 \times 10^{-21}\text{ cm}^2)(1.10 \times 10^{13}\text{ cm}^{-2}\text{s}^{-1}) \approx \mathbf{8.681 \times 10^{-8}\text{ fissions/nucleus}\cdot\text{s}}$$

**(c) Spectrum Hardening Effect at $T_2 = 600\text{ K}$:**
At $T_2 = 600\text{ K}$:
$$\hat{\sigma}_f(T_2) = g_f(T_2) \cdot \sigma_0(f) = 1.340 \times 748\text{ b} \approx \mathbf{1002.32\text{ b}} = 1.0023 \times 10^{-20}\text{ cm}^2$$
Since neutron density $n_0$ is held constant, the reference flux $\phi_0 = n_0 v_0 = 1.10 \times 10^{13}\text{ cm}^{-2}\text{s}^{-1}$ remains unchanged:
$$R_{f, 2} = \hat{\sigma}_f(T_2) \cdot \phi_0 = (1.0023 \times 10^{-20})(1.10 \times 10^{13}) \approx \mathbf{1.1025 \times 10^{-7}\text{ fissions/nucleus}\cdot\text{s}}$$
Percentage increase in fission rate:
$$\text{Increase} = \frac{R_{f, 2} - R_{f, 1}}{R_{f, 1}} \times 100\% = \frac{g_f(T_2) - g_f(T_1)}{g_f(T_1)} \times 100\%$$
$$\text{Increase} = \frac{1.340 - 1.055}{1.055} \times 100\% = \frac{0.285}{1.055} \times 100\% \approx \mathbf{+27.01\%}$$
The fission rate per nucleus jumps by **$+27.0\%$** simply due to thermal spectrum hardening moving toward the $0.296\text{ eV}$ resonance of Plutonium-239!"""
        },
        {
            "id": "rp-prob-2-3",
            "title": "Volumetric Fission Rate, Power Density and Thermal Neutron Flux in a PWR Fuel Pin",
            "statement": r"""A cylindrical $\text{UO}_2$ fuel pin in a commercial Pressurized Water Reactor has fuel pellet radius $R = 0.41\text{ cm}$ and active fuel length $H = 366\text{ cm}$.
The linear heat generation rate at the axial core midplane is $q' = 18.5\text{ kW/m} = 185\text{ W/cm}$.
The average energy released per fission is $Q = 200\text{ MeV} = 3.204 \times 10^{-11}\text{ J}$.
The macroscopic thermal fission cross section of the fuel is $\Sigma_f = 0.355\text{ cm}^{-1}$.
(a) Calculate the volumetric power density $q'''$ in $\text{W/cm}^3$ and $\text{MW/m}^3$ within the fuel pellet.
(b) Calculate the volumetric fission rate $R_f$ in $\text{fissions/cm}^3\cdot\text{s}$.
(c) Determine the required average thermal neutron flux $\phi_{\text{th}}$ inside the fuel pellet in $\text{neutrons/cm}^2\cdot\text{s}$.""",
            "solution": r"""**(a) Volumetric Power Density $q'''$:**
The cross-sectional area of the cylindrical fuel pellet is:
$$A_{\text{pellet}} = \pi R^2 = \pi (0.41\text{ cm})^2 \approx 0.5281\text{ cm}^2$$
The volumetric heat generation rate is the linear power divided by cross-sectional area:
$$q''' = \frac{q'}{A_{\text{pellet}}} = \frac{185\text{ W/cm}}{0.5281\text{ cm}^2} \approx \mathbf{350.3\text{ W/cm}^3}$$
In standard engineering units:
$$q''' = 350.3 \times 10^6\text{ W/m}^3 = \mathbf{350.3\text{ MW/m}^3}$$

**(b) Volumetric Fission Rate $R_f$:**
Since power density is $q''' = Q \cdot R_f$:
$$R_f = \frac{q'''}{Q} = \frac{350.3\text{ J/s}\cdot\text{cm}^3}{3.20436 \times 10^{-11}\text{ J/fission}} \approx \mathbf{1.0932 \times 10^{13}\text{ fissions/cm}^3\cdot\text{s}}$$

**(c) Required Average Thermal Neutron Flux $\phi_{\text{th}}$:**
Using $R_f = \Sigma_f \cdot \phi_{\text{th}}$:
$$\phi_{\text{th}} = \frac{R_f}{\Sigma_f} = \frac{1.0932 \times 10^{13}\text{ fissions/cm}^3\cdot\text{s}}{0.355\text{ cm}^{-1}} \approx \mathbf{3.079 \times 10^{13}\text{ neutrons/cm}^2\cdot\text{s}}$$
The required local thermal neutron flux inside the fuel pellet is **$3.08 \times 10^{13}\text{ neutrons/cm}^2\cdot\text{s}$**."""
        }
    ]
}

with open("rp_u1.json", "w", encoding="utf-8") as f:
    json.dump(u1_data, f, indent=2, ensure_ascii=False)

with open("rp_u2.json", "w", encoding="utf-8") as f:
    json.dump(u2_data, f, indent=2, ensure_ascii=False)

print("rp_u1.json and rp_u2.json successfully written!")
