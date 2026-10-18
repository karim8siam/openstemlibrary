# -*- coding: utf-8 -*-
"""
Builder for Nuclear Reactor Physics Units 3 & 4
Unit 3: Nuclear Fission Mechanics, Energy Release & Product Yields
Unit 4: Neutron Slowing Down & Moderation Theory
"""
import json

u3_data = {
    "title": "Nuclear Fission Mechanics, Energy Release & Product Yields",
    "subtitle": "Liquid Drop Model, Fission Barriers, Watt Spectrum, Delayed Neutrons & Fuel Burnup Systematics",
    "summary": "Exhaustive treatment of nuclear fission mechanics and phenomenology: the Bohr-Wheeler liquid drop model deformation energetics, Coulomb vs surface tension competition, fissility parameter and spontaneous fission systematics; practical nuclear fuel forms (LEU, HEU, MOX, thorium-uranium cycle, transuranic burners); asymmetric mass distribution and double-hump fission product yield curves; comprehensive energy partition accounting for prompt/delayed fragments, neutrons, gammas, neutrinos, and recoverable Q-value (200 MeV); Watt fission neutron energy spectrum derivation and characteristic mean/probable energies; prompt versus delayed neutron emission kinetics, six precursor groups, and physical significance for reactor control; thermal power, fission consumption rates, and core burnup metrics in MWd/MTU.",
    "sections": [
        {
            "id": "sec-3-1",
            "title": "The Liquid Drop Model of Fission: Deformation Energetics & Bohr-Wheeler Barrier",
            "content": r"""
<h3>1. Fission Energetics and the Liquid Drop Analogy</h3>
<p>
The liquid drop model (LDM), formulated by Niels Bohr and John Archibald Wheeler (1939), models the heavy atomic nucleus as an incompressible, charged macroscopic liquid droplet with constant nuclear matter density $\rho_0 \approx 0.17\text{ nucleons/fm}^3$. The nuclear ground state represents an equilibrium configuration between two opposing forces:
<ul>
  <li><strong>Short-range attractive nuclear force:</strong> Represented macroscopically as surface tension energy $E_s$, which acts to minimize nuclear surface area (favoring a spherical shape).</li>
  <li><strong>Long-range repulsive Coulomb force:</strong> Represented as electrostatic self-energy $E_c$, which pushes protons apart and drives the nucleus toward elongated, non-spherical deformations.</li>
</ul>
</p>

<h3>2. Ellipsoidal Deformation and Fissility Parameter</h3>
<p>
Consider a spherical nucleus of radius $R_0 = r_0 A^{1/3}$ undergoing a small quadrupole deformation into a prolate spheroid with semi-major axis $a = R_0 (1 + \epsilon)$ and semi-minor axes $b = c = R_0 (1 - \frac{1}{2}\epsilon)$, preserving volume to second order in eccentricity $\epsilon$:
$$R(\theta) = R_0 \left[ 1 + \alpha_2 P_2(\cos\theta) \right]$$
Expanding the surface and Coulomb energy terms in powers of the deformation coordinate $\alpha_2$:
$$E_s(\alpha_2) = E_s^{(0)} \left( 1 + \frac{2}{5} \alpha_2^2 + \mathcal{O}(\alpha_2^3) \right)$$
$$E_c(\alpha_2) = E_c^{(0)} \left( 1 - \frac{1}{5} \alpha_2^2 + \mathcal{O}(\alpha_2^3) \right)$$
where the undeformed ground-state values from the semi-empirical mass formula (Weizsäcker) are:
$$E_s^{(0)} = a_s A^{2/3} \approx 17.8 \times A^{2/3}\text{ MeV}, \qquad E_c^{(0)} = a_c \frac{Z^2}{A^{1/3}} \approx 0.71 \times \frac{Z^2}{A^{1/3}}\text{ MeV}$$
The change in net nuclear energy $\Delta E = \Delta E_s + \Delta E_c$ as a function of deformation $\alpha_2$ is:
$$\Delta E(\alpha_2) = \alpha_2^2 \left( \frac{2}{5} E_s^{(0)} - \frac{1}{5} E_c^{(0)} \right) = \frac{1}{5} \alpha_2^2 \left( 2 E_s^{(0)} - E_c^{(0)} \right)$$
</p>
<p>
For the spherical shape to remain stable against spontaneous deformation, the coefficient of $\alpha_2^2$ must be positive ($\Delta E > 0$). When electrostatic repulsion overcomes surface tension, the sphere becomes unstable to infinitesimal perturbations ($\Delta E < 0$):
$$2 E_s^{(0)} - E_c^{(0)} < 0 \implies \frac{E_c^{(0)}}{2 E_s^{(0)}} > 1$$
Substituting the Bethe-Weizsäcker coefficients:
$$\frac{0.71 \times Z^2 / A^{1/3}}{2 \times 17.8 \times A^{2/3}} \approx \frac{Z^2 / A}{50.1} > 1 \implies \mathbf{\frac{Z^2}{A} \gtrsim 49\text{ to }50}$$
The dimensionless ratio $x \equiv \frac{E_c^{(0)}}{2 E_s^{(0)}} \approx \frac{Z^2/A}{(Z^2/A)_{\text{crit}}}$ is known as the <strong>Bohr-Wheeler fissility parameter</strong>. For heavy actinides such as ${}^{238}\text{U}$ ($Z^2/A \approx 35.6$) and ${}^{235}\text{U}$ ($Z^2/A \approx 36.0$), $x \approx 0.72$, meaning they are stable against spontaneous deformation at the ground state but possess a finite fission activation barrier.
</p>

<h3>3. The Fission Barrier and Saddle Point</h3>
<p>
As deformation increases beyond the harmonic quadratic regime, higher multipoles ($\alpha_3, \alpha_4$) develop necking, culminating in the <strong>saddle point</strong>—the maximum potential energy along the lowest-energy fission valley. The height of this peak above the ground state is the <strong>fission barrier</strong> $E_B$:
$$E_B = E_{\text{saddle}} - E_{\text{ground}}$$
Representative fission barrier heights:
<ul>
  <li>${}^{235}\text{U}$: $E_B \approx 5.75\text{ MeV}$</li>
  <li>${}^{238}\text{U}$: $E_B \approx 6.25\text{ MeV}$</li>
  <li>${}^{239}\text{Pu}$: $E_B \approx 5.50\text{ MeV}$</li>
  <li>${}^{232}\text{Th}$: $E_B \approx 6.50\text{ MeV}$</li>
</ul>
When a thermal neutron ($E_n \approx 0.025\text{ eV}$) is captured by ${}^{235}\text{U}$, the binding energy of the added neutron ($S_n = 6.55\text{ MeV}$) exceeds the barrier ($S_n > E_B$), inducing prompt fission with zero threshold. In contrast, capture by ${}^{238}\text{U}$ yields only $S_n = 4.81\text{ MeV} < E_B = 6.25\text{ MeV}$, leaving a deficit $\Delta E \approx 1.44\text{ MeV}$ that must be supplied as incident neutron kinetic energy.
</p>
"""
        },
        {
            "id": "sec-3-2",
            "title": "Practical Nuclear Fuels: LEU, HEU, MOX, Thorium Cycle & Transuranic Burners",
            "content": r"""
<h3>1. Fuel Classification and Enrichment Regimes</h3>
<p>
Nuclear fuels in fission reactors are categorized according to isotopic composition, physical phase, and chemical matrix:
<ul>
  <li><strong>Natural Uranium (NatU):</strong> $0.7204\%\ {}^{235}\text{U}$, $99.274\%\ {}^{238}\text{U}$, $0.0055\%\ {}^{234}\text{U}$. Used directly in heavy-water moderated reactors (CANDU, PHWR) and carbon dioxide-cooled graphite reactors (Magnox).</li>
  <li><strong>Low-Enriched Uranium (LEU):</strong> Uranium enriched to $3\%\text{ to }5\%\ {}^{235}\text{U}$ by mass. Standard commercial fuel for Light Water Reactors (PWR and BWR).</li>
  <li><strong>High-Assay Low-Enriched Uranium (HALEU):</strong> Uranium enriched between $5\%\text{ and }20\%\ {}^{235}\text{U}$. Crucial for advanced Small Modular Reactors (SMRs) and Generation IV fast reactors, offering high power density and extended refueling cycles without crossing proliferation safeguards.</li>
  <li><strong>Highly Enriched Uranium (HEU):</strong> Uranium enriched to $\ge 20\%\ {}^{235}\text{U}$ (weapons-grade $\ge 90\%$). Restricted to naval propulsion reactors, research reactors, and space fission systems.</li>
</ul>
</p>

<h3>2. Mixed Oxide (MOX) and Plutonium Recycling</h3>
<p>
Mixed Oxide fuel consists of depleted uranium dioxide ($\text{UO}_2$) blended with recycled reactor-grade plutonium dioxide ($\text{PuO}_2$), typically containing $5\%\text{ to }9\%\ \text{Pu}_{\text{fissile}}$ (${}^{239}\text{Pu} + {}^{241}\text{Pu}$):
$$\text{MOX} = (1 - x)\,\text{UO}_2 + x\,\text{PuO}_2$$
Key neutron physical consequences of MOX fuel in thermal cores:
<ul>
  <li><strong>Hardened Neutron Spectrum:</strong> Massive capture and fission resonances of ${}^{239}\text{Pu}$ ($0.296\text{ eV}$) and ${}^{240}\text{Pu}$ ($1.056\text{ eV}$) depress the thermal flux and harden the average energy spectrum.</li>
  <li><strong>Reduced Delayed Neutron Fraction:</strong> $\beta_{\text{eff}}$ decreases because $\beta({}^{239}\text{Pu}) \approx 0.00215$ compared to $\beta({}^{235}\text{U}) \approx 0.00650$, requiring tighter control rod margins.</li>
  <li><strong>Increased Control Rod Absorption Requirements:</strong> Stronger thermal absorption in fuel requires higher boron concentration or enriched boron carbide ($\text{B}_4\text{C}$) control rods.</li>
</ul>
</p>

<h3>3. The Thorium-Uranium Fuel Cycle</h3>
<p>
The thorium fuel cycle exploits fertile ${}^{232}\text{Th}$ to breed fissile ${}^{233}\text{U}$:
$${}^{232}_{90}\text{Th} + n \longrightarrow {}^{233}_{90}\text{Th} \xrightarrow[\beta^-, \, 22.3\text{ min}]{} {}^{233}_{91}\text{Pa} \xrightarrow[\beta^-, \, 26.97\text{ days}]{} {}^{233}_{92}\text{U}$$
The major nuclear advantage is that ${}^{233}\text{U}$ exhibits $\eta > 2.25$ across the entire thermal neutron spectrum (superior to ${}^{235}\text{U}$ at $\eta = 2.07$ and ${}^{239}\text{Pu}$ at $\eta = 2.11$), making <strong>thermal breeding</strong> feasible (e.g. in Molten Salt Breeder Reactors - MSBR). In addition, thorium fuels produce orders of magnitude fewer long-lived transuranic actinides ($\text{Np, Pu, Am, Cm}$) because six successive neutron captures are needed to reach plutonium.
</p>
"""
        },
        {
            "id": "sec-3-3",
            "title": "Mass Distribution and Fission Product Yields: The Asymmetric Double Hump",
            "content": r"""
<h3>1. Mass Yield Curve: Bimodal vs Symmetric Cleavage</h3>
<p>
When low-energy (thermal) neutrons induce fission in ${}^{235}\text{U}$ or ${}^{239}\text{Pu}$, the nucleus splits overwhelmingly into two fragments of unequal mass. The percentage yield of fission fragments as a function of mass number $A$ is the <strong>fission product mass yield curve</strong> $Y(A)$, normalized such that:
$$\sum_{A} Y(A) = 200\%$$
since each fission produces exactly two primary fission fragments.
</p>
<p>
For thermal fission of ${}^{235}\text{U}$:
<ul>
  <li><strong>Light Fragment Peak:</strong> Centered at mass number $A_L \approx 95$ (peak yield $\sim 6.5\%$ at isotopes like ${}^{95}\text{Mo}, {}^{95}\text{Zr}, {}^{90}\text{Sr}$).</li>
  <li><strong>Heavy Fragment Peak:</strong> Centered at mass number $A_H \approx 138\text{ to }140$ (peak yield $\sim 6.5\%$ at ${}^{137}\text{Cs}, {}^{135}\text{Xe}, {}^{140}\text{Ba}$).</li>
  <li><strong>Symmetric Fission Valley:</strong> At $A \approx 117$, symmetric splitting is suppressed by a factor of over $600$ ($Y(117) \approx 0.01\%$).</li>
</ul>
</p>

<h3>2. Shell Effects and Energy-Dependent Peak-to-Valley Ratio</h3>
<p>
The asymmetric splitting is explained by single-particle nuclear shell model effects in the deformed nascent fragments:
<ul>
  <li>The heavy fragment favors magic numbers: $Z = 50$ (closed spherical proton shell) and $N = 82$ (closed spherical neutron shell, $A \approx 132$, e.g. ${}^{132}_{50}\text{Sn}$), which provides exceptional quantum stability.</li>
  <li>As incident neutron energy increases from thermal to fast ($E_n \sim 14\text{ MeV}$ in D-T fusion), excitation washes out shell effects; the central valley fills in, and the distribution shifts toward symmetric fission.</li>
</ul>
</p>
"""
        },
        {
            "id": "sec-3-4",
            "title": "Energy Partition of Fission: Recoverable Energy & Thermodynamic Balance",
            "content": r"""
<h3>1. Microscopic Energy Partition Breakdown</h3>
<p>
When a ${}^{235}\text{U}$ nucleus captures a thermal neutron and fissions, approximately $200\text{ MeV}$ of total energy is liberated. The microscopic distribution of this energy among products is summarized below:
</p>
<table style="width:100%; border-collapse: collapse; margin: 16px 0; text-align: left;">
  <thead>
    <tr style="border-bottom: 2px solid #4a5568;">
      <th style="padding: 8px;">Energy Component</th>
      <th style="padding: 8px;">Energy (MeV)</th>
      <th style="padding: 8px;">Fraction (%)</th>
      <th style="padding: 8px;">Recovery Mechanism</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #2d3748;">
      <td style="padding: 8px;">Kinetic Energy of Fission Fragments</td>
      <td style="padding: 8px;">$168 \pm 5$</td>
      <td style="padding: 8px;">$84.0\%$</td>
      <td style="padding: 8px;">Thermalized locally within $\sim 10\ \mu\text{m}$ in fuel</td>
    </tr>
    <tr style="border-bottom: 1px solid #2d3748;">
      <td style="padding: 8px;">Kinetic Energy of Prompt Neutrons ($\nu \approx 2.43$)</td>
      <td style="padding: 8px;">$5 \pm 0.5$</td>
      <td style="padding: 8px;">$2.5\%$</td>
      <td style="padding: 8px;">Thermalized via elastic scattering in moderator</td>
    </tr>
    <tr style="border-bottom: 1px solid #2d3748;">
      <td style="padding: 8px;">Prompt Fission Gamma Rays ($\gamma_{\text{prompt}}$)</td>
      <td style="padding: 8px;">$7 \pm 1$</td>
      <td style="padding: 8px;">$3.5\%$</td>
      <td style="padding: 8px;">Absorbed in fuel, cladding, coolant, shield</td>
    </tr>
    <tr style="border-bottom: 1px solid #2d3748;">
      <td style="padding: 8px;">Fission Product Beta Decay ($\beta^-$)</td>
      <td style="padding: 8px;">$8 \pm 1$</td>
      <td style="padding: 8px;">$4.0\%$</td>
      <td style="padding: 8px;">Delayed decay heat inside fuel matrix</td>
    </tr>
    <tr style="border-bottom: 1px solid #2d3748;">
      <td style="padding: 8px;">Fission Product Delayed Gamma Rays ($\gamma_{\text{delayed}}$)</td>
      <td style="padding: 8px;">$7 \pm 1$</td>
      <td style="padding: 8px;">$3.5\%$</td>
      <td style="padding: 8px;">Delayed decay heat in core structure</td>
    </tr>
    <tr style="border-bottom: 1px solid #2d3748;">
      <td style="padding: 8px;">Antineutrinos ($\bar{\nu}_e$)</td>
      <td style="padding: 8px;">$12 \pm 2$</td>
      <td style="padding: 8px;">$6.0\%$</td>
      <td style="padding: 8px;"><strong>Lost entirely</strong> (escape reactor vessel)</td>
    </tr>
    <tr style="border-bottom: 2px solid #4a5568;">
      <td style="padding: 8px;">Radiative Capture Gamma Rays ($(n, \gamma)$ in non-fission)</td>
      <td style="padding: 8px;">$3\text{ to }10$</td>
      <td style="padding: 8px;">$\sim 2.5\text{ to }5\%$</td>
      <td style="padding: 8px;">Exothermic capture in structural cladding/water</td>
    </tr>
  </tbody>
</table>

<h3>2. Recoverable Energy per Fission ($Q_{\text{rec}}$)</h3>
<p>
The antineutrinos possess a negligible interaction cross section ($\sigma_\nu \sim 10^{-44}\text{ cm}^2$) and escape into outer space without depositing heat. Conversely, excess neutrons produced by fission are absorbed via radiative capture $(n, \gamma)$ in moderator, coolant, and structural cladding, releasing additional binding gamma energy ($\sim 3\text{ to }8\text{ MeV}$). Hence, the <strong>net recoverable thermal energy</strong> per fission event is:
$$Q_{\text{rec}} = Q_{\text{total}} - E_{\bar{\nu}_e} + E_{(n,\gamma)} \approx 207\text{ MeV} - 12\text{ MeV} + 5\text{ MeV} \approx \mathbf{200 \pm 2\text{ MeV}}$$
In engineering calculations:
$$1\text{ fission} \approx 200\text{ MeV} = 3.20435 \times 10^{-11}\text{ Joules} = 3.20435 \times 10^{-17}\text{ MW}\cdot\text{s}$$
$$3.12 \times 10^{10}\text{ fissions/second} \longleftrightarrow \mathbf{1\text{ Watt of thermal power}}$$
</p>
"""
        },
        {
            "id": "sec-3-5",
            "title": "Fission Neutron Energy Spectrum: Watt Distribution & Energetics",
            "content": r"""
<h3>1. The Watt Fission Spectrum Formula</h3>
<p>
Neutrons liberated at the moment of scission (prompt fission neutrons) are emitted isotropically from rapidly moving, highly excited fission fragments. Transforming from the center-of-mass frame of the fragment to the laboratory frame results in the classical <strong>Watt distribution</strong> $\chi(E)$:
$$\chi(E) = c \, e^{-E/a} \sinh\left(\sqrt{b E}\right)$$
For thermal neutron fission of Uranium-235 (${}^{235}\text{U}$), empirical parameters fitted to nuclear data (ENDF/B-VIII) are:
$$a = 0.988\text{ MeV}, \qquad b = 2.249\text{ MeV}^{-1}$$
The normalization constant $c$ enforces total probability conservation:
$$\int_{0}^{\infty} \chi(E) \, dE = 1 \implies c = \sqrt{\frac{4}{\pi a^3 b}} \, e^{-a b / 4}$$
An alternate, widely used analytical approximation developed by Cranberg is:
$$\chi(E) = 0.453 \, e^{-1.036 E} \sinh\left(\sqrt{2.29 E}\right) \quad (E\text{ in MeV})$$
or the Maxwellian fission spectrum approximation:
$$\chi_M(E) = \frac{2}{\sqrt{\pi} T^{3/2}} E^{1/2} e^{-E/T} \quad (T \approx 1.29\text{ MeV})$$
</p>

<h3>2. Mean and Most Probable Prompt Neutron Energy</h3>
<p>
The energy distribution spans eight orders of magnitude, with:
<ul>
  <li><strong>Most Probable Energy ($E_p$):</strong> Found by solving $\frac{d\chi(E)}{dE} = 0$:
  $$E_p \approx \mathbf{0.73\text{ MeV}}$$</li>
  <li><strong>Average (Mean) Kinetic Energy ($\bar{E}$):</strong>
  $$\bar{E} = \int_{0}^{\infty} E \, \chi(E) \, dE = \frac{3}{2} a + \frac{1}{4} a^2 b \approx \frac{3}{2}(0.988) + \frac{1}{4}(0.988)^2(2.249) \approx \mathbf{1.98\text{ to }2.00\text{ MeV}}$$</li>
</ul>
Thus, fission neutrons are born fast, with an average speed $\bar{v} = \sqrt{2\bar{E}/m_n} \approx 1.95 \times 10^7\text{ m/s} \approx 0.065\, c$ (6.5% the speed of light)!
</p>
"""
        },
        {
            "id": "sec-3-6",
            "title": "Prompt vs Delayed Neutrons: Six Precursor Groups & Nuclear Control",
            "content": r"""
<h3>1. Prompt Neutrons and Delayed Precursors</h3>
<p>
Over $99\%$ of fission neutrons are emitted within $\tau_{\text{prompt}} \sim 10^{-14}\text{ to }10^{-13}\text{ seconds}$ of scission—these are <strong>prompt neutrons</strong>.
However, a tiny but vital fraction ($\beta \approx 0.65\%$ in ${}^{235}\text{U}$) are emitted with delays ranging from milliseconds to minutes:
$$\text{Fission} \longrightarrow \text{Precursor Nuclide } ({}^{87}\text{Br}) \xrightarrow[\beta^-]{T_{1/2} = 55.6\text{ s}} \text{Emitter } ({}^{87}\text{Kr}^*) \xrightarrow[\text{prompt } n]{< 10^{-15}\text{ s}} {}^{86}\text{Kr} + n$$
The emission of the neutron itself is prompt from an excited daughter nucleus whose excitation energy exceeds the neutron separation energy ($E^* > S_n$), but the emission rate is governed strictly by the preceding beta decay half-life of the parent precursor nuclide.
</p>

<h3>2. The Six Delayed Neutron Precursor Groups</h3>
<p>
In reactor physics and point kinetics, the hundreds of distinct delayed neutron emitting fission products are grouped into six standard precursor groups according to decay constant $\lambda_i = \ln 2 / T_{1/2, i}$:
</p>
<table style="width:100%; border-collapse: collapse; margin: 16px 0; text-align: left;">
  <thead>
    <tr style="border-bottom: 2px solid #4a5568;">
      <th style="padding: 8px;">Group $i$</th>
      <th style="padding: 8px;">Representative Precursor</th>
      <th style="padding: 8px;">Half-Life $T_{1/2}$ (s)</th>
      <th style="padding: 8px;">Decay Const $\lambda_i\ (\text{s}^{-1})$</th>
      <th style="padding: 8px;">Rel. Abundance $\beta_i / \beta$</th>
      <th style="padding: 8px;">Average Energy (keV)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #2d3748;">
      <td style="padding: 8px;">1</td>
      <td style="padding: 8px;">${}^{87}\text{Br}$</td>
      <td style="padding: 8px;">$55.72$</td>
      <td style="padding: 8px;">$0.0124$</td>
      <td style="padding: 8px;">$0.033$</td>
      <td style="padding: 8px;">$250$</td>
    </tr>
    <tr style="border-bottom: 1px solid #2d3748;">
      <td style="padding: 8px;">2</td>
      <td style="padding: 8px;">${}^{137}\text{I}$</td>
      <td style="padding: 8px;">$22.72$</td>
      <td style="padding: 8px;">$0.0305$</td>
      <td style="padding: 8px;">$0.219$</td>
      <td style="padding: 8px;">$560$</td>
    </tr>
    <tr style="border-bottom: 1px solid #2d3748;">
      <td style="padding: 8px;">3</td>
      <td style="padding: 8px;">${}^{138}\text{I}, {}^{89}\text{Br}$</td>
      <td style="padding: 8px;">$6.22$</td>
      <td style="padding: 8px;">$0.111$</td>
      <td style="padding: 8px;">$0.196$</td>
      <td style="padding: 8px;">$430$</td>
    </tr>
    <tr style="border-bottom: 1px solid #2d3748;">
      <td style="padding: 8px;">4</td>
      <td style="padding: 8px;">${}^{93}\text{Rb}, {}^{139}\text{I}$</td>
      <td style="padding: 8px;">$2.30$</td>
      <td style="padding: 8px;">$0.301$</td>
      <td style="padding: 8px;">$0.395$</td>
      <td style="padding: 8px;">$620$</td>
    </tr>
    <tr style="border-bottom: 1px solid #2d3748;">
      <td style="padding: 8px;">5</td>
      <td style="padding: 8px;">${}^{94}\text{Rb}, {}^{140}\text{I}$</td>
      <td style="padding: 8px;">$0.61$</td>
      <td style="padding: 8px;">$1.14$</td>
      <td style="padding: 8px;">$0.115$</td>
      <td style="padding: 8px;">$420$</td>
    </tr>
    <tr style="border-bottom: 2px solid #4a5568;">
      <td style="padding: 8px;">6</td>
      <td style="padding: 8px;">${}^{95}\text{Rb}$</td>
      <td style="padding: 8px;">$0.23$</td>
      <td style="padding: 8px;">$3.01$</td>
      <td style="padding: 8px;">$0.042$</td>
      <td style="padding: 8px;">$510$</td>
    </tr>
  </tbody>
</table>

<h3>3. Physical Role in Reactor Control</h3>
<p>
Without delayed neutrons, the average generation time between fission generations would be dictated entirely by the prompt neutron lifetime $l \sim 10^{-4}\text{ s}$ in thermal reactors ($l \sim 10^{-7}\text{ s}$ in fast reactors). For a tiny reactivity insertion $\Delta k = 0.001$, reactor power would escalate as $e^{t / (l/\Delta k)} = e^{10 t}$, multiplying by $22{,}000$ every second—rendering mechanical control rods completely ineffective!
Delayed neutrons stretch the effective generation time to:
$$\bar{l}_{\text{eff}} = (1 - \beta) l + \sum_{i=1}^6 \beta_i \tau_i = (1 - \beta) l + \sum_{i=1}^6 \frac{\beta_i}{\lambda_i} \approx 0.1\text{ seconds}$$
This slows reactor power transients by three orders of magnitude, allowing mechanical control rods and electronic safety circuits ample time to maintain safe steady-state operation.
</p>
"""
        },
        {
            "id": "sec-3-7",
            "title": "Thermal Power, Fission Rates, Fuel Consumption & Core Burnup Systematics",
            "content": r"""
<h3>1. Relation Between Thermal Power and Fission Rate</h3>
<p>
If a reactor operates at steady thermal power $P$ (in Watts), the core-wide total fission rate $\dot{F}$ (fissions per second) is:
$$\dot{F} = \frac{P}{Q_{\text{rec}}} = \frac{P\ [\text{W}]}{3.20435 \times 10^{-11}\ [\text{J/fission}]} \approx 3.1208 \times 10^{10} \times P\ [\text{W}]$$
For a typical $3000\text{ MW}_{\text{th}}$ commercial power plant:
$$\dot{F} = 3.1208 \times 10^{10} \times (3.0 \times 10^9\text{ W}) \approx \mathbf{9.36 \times 10^{19}\text{ fissions/second}}$$
</p>

<h3>2. Fissile Fuel Consumption Rate</h3>
<p>
Each fission consumes one fissile nucleus. In addition, radiative capture without fission $(n, \gamma)$ consumes additional nuclei in ratio $\alpha \equiv \sigma_c / \sigma_f$:
$$\dot{N}_{\text{consumed}} = \dot{F} (1 + \alpha) = \dot{F} \frac{\sigma_a}{\sigma_f}$$
For Uranium-235 at thermal energies, $\sigma_f \approx 585\text{ b}$, $\sigma_c \approx 99\text{ b}$, giving capture-to-fission ratio:
$$\alpha \approx \frac{99}{585} \approx 0.169 \implies 1 + \alpha \approx 1.169$$
The mass consumption rate of ${}^{235}\text{U}$ per Megawatt-day ($\text{MWd}$) of thermal energy is:
$$\Delta m_{\text{fission}} = \frac{1\text{ MWd} \times 86400\text{ s/d} \times 235.044\text{ g/mol}}{(3.20435 \times 10^{-11}\text{ J}) \times (6.02214 \times 10^{23}\text{ atoms/mol})} \approx \mathbf{1.05\text{ g } {}^{235}\text{U} / \text{MWd}}$$
Including radiative capture losses ($1 + \alpha$):
$$\Delta m_{\text{total}} = 1.05 \times 1.169 \approx \mathbf{1.23\text{ g } {}^{235}\text{U} / \text{MWd}}$$
A $3000\text{ MW}_{\text{th}}$ plant consumes:
$$\Delta m = 3000\text{ MW} \times 1.23\text{ g/MWd} \approx \mathbf{3.69\text{ kg of } {}^{235}\text{U} \text{ per day}}$$
</p>

<h3>3. Fuel Burnup Formalism</h3>
<p>
<strong>Core Burnup</strong> measures the total thermal energy extracted per unit initial mass of heavy metal fuel loaded into the reactor, conventionally expressed in Megawatt-days per Metric Ton of Heavy Metal ($\text{MWd/MTU}$ or $\text{GWd/MTU}$):
$$B = \frac{\int_0^T P(t) \, dt}{M_{\text{HM}, 0}} = \frac{E_{\text{th}}}{M_{\text{HM}, 0}}$$
where $M_{\text{HM}, 0}$ is the initial mass of uranium (or uranium + plutonium) metal in metric tons ($1\text{ MT} = 1000\text{ kg}$).
Commercial LWRs routinely achieve burnups of $45\text{ to }55\text{ GWd/MTU}$ ($45{,}000\text{ to }55{,}000\text{ MWd/MTU}$), corresponding to the fission of approximately $5\%$ of all initial heavy metal atoms.
</p>
"""
        }
    ],
    "exercises": [
        {
            "id": "rp-prob-3-1",
            "title": "Energy Release and Mass Defect in Induced Thermal Fission of Uranium-235",
            "statement": r"""A thermal neutron strikes a Uranium-235 nucleus causing binary fission into Barium-141 and Krypton-92 with the emission of three prompt neutrons:
$${}^1_0 n + {}^{235}_{92}\text{U} \longrightarrow {}^{141}_{56}\text{Ba} + {}^{92}_{36}\text{Kr} + 3 \, {}^1_0 n$$
The precise atomic masses are:
- $m({}^1_0 n) = 1.008665\text{ u}$
- $m({}^{235}_{92}\text{U}) = 235.043930\text{ u}$
- $m({}^{141}_{56}\text{Ba}) = 140.914411\text{ u}$
- $m({}^{92}_{36}\text{Kr}) = 91.926156\text{ u}$
where $1\text{ u} = 931.494\text{ MeV}/c^2 = 1.66054 \times 10^{-27}\text{ kg}$.
(a) Calculate the mass defect $\Delta m$ in atomic mass units ($\text{u}$) and kilograms ($\text{kg}$).
(b) Calculate the prompt energy released $Q_{\text{prompt}}$ in $\text{MeV}$ and in Joules ($\text{J}$).
(c) Assuming the two fragments are emitted back-to-back in the center-of-mass frame and conserve linear momentum, calculate the kinetic energy of the light fragment (${}^{92}\text{Kr}$) and heavy fragment (${}^{141}\text{Ba}$) if $168\text{ MeV}$ is partitioned into fragment kinetic energy.""",
            "solution": r"""**(a) Mass Defect $\Delta m$:**
Initial mass of reactants:
$$m_{\text{initial}} = m({}^{235}\text{U}) + m(n) = 235.043930 + 1.008665 = 236.052595\text{ u}$$
Final mass of products:
$$m_{\text{final}} = m({}^{141}\text{Ba}) + m({}^{92}\text{Kr}) + 3\,m(n)$$
$$m_{\text{final}} = 140.914411 + 91.926156 + 3(1.008665) = 232.840567 + 3.025995 = 235.866562\text{ u}$$
Mass defect:
$$\Delta m = m_{\text{initial}} - m_{\text{final}} = 236.052595 - 235.866562 = \mathbf{0.186033\text{ u}}$$
Converting to kilograms:
$$\Delta m = (0.186033\text{ u}) \times (1.660539 \times 10^{-27}\text{ kg/u}) \approx \mathbf{3.089 \times 10^{-28}\text{ kg}}$$

**(b) Energy Released $Q_{\text{prompt}}$:**
Using Einstein's mass-energy equivalence $Q = \Delta m \cdot c^2$:
$$Q_{\text{prompt}} = (0.186033\text{ u}) \times (931.494\text{ MeV/u}) \approx \mathbf{173.288\text{ MeV}}$$
In Joules:
$$Q_{\text{prompt}} = (173.288 \times 10^6\text{ eV}) \times (1.6021766 \times 10^{-19}\text{ J/eV}) \approx \mathbf{2.776 \times 10^{-11}\text{ Joules}}$$

**(c) Fragment Kinetic Energy Partition via Momentum Conservation:**
In the center-of-mass frame with initial momentum zero:
$$p_L = p_H \implies m_L v_L = m_H v_H$$
The ratio of kinetic energies is inversely proportional to their mass ratio:
$$\frac{E_L}{E_H} = \frac{p^2 / (2 m_L)}{p^2 / (2 m_H)} = \frac{m_H}{m_L} = \frac{141}{92} \approx 1.5326$$
Since $E_L + E_H = 168\text{ MeV}$:
$$E_L \left( 1 + \frac{92}{141} \right) = 168 \implies E_L \left( \frac{233}{141} \right) = 168$$
$$E_L = 168 \times \frac{141}{233} \approx \mathbf{101.66\text{ MeV}}$$
$$E_H = 168 - 101.66 \approx \mathbf{66.34\text{ MeV}}$$
The lighter Krypton-92 fragment receives **$101.7\text{ MeV}$** ($60.5\%$ of the kinetic energy), while the heavier Barium-141 fragment receives **$66.3\text{ MeV}$** ($39.5\%$)."""
        },
        {
            "id": "rp-prob-3-2",
            "title": "Watt Fission Spectrum Integration and Prompt Neutron Energy Distribution",
            "statement": r"""The prompt fission neutron energy spectrum for Uranium-235 is given by the Cranberg form:
$$\chi(E) = 0.453 \, e^{-1.036 E} \sinh\left(\sqrt{2.29 E}\right) \quad (E\text{ in MeV})$$
(a) Calculate the value of $\chi(E)$ at $E = 0.5\text{ MeV}$, $E = 1.0\text{ MeV}$, $E = 2.0\text{ MeV}$, and $E = 5.0\text{ MeV}$.
(b) Evaluate the most probable energy $E_{\text{mp}}$ by setting $\frac{d}{dE} \ln \chi(E) = 0$.
(c) What percentage of prompt fission neutrons are born with energy exceeding $E = 1.0\text{ MeV}$ (the fast fission threshold of $^{238}\text{U}$)? (Given: $\int_1^\infty \chi(E) dE \approx 0.692$).""",
            "solution": r"""**(a) Spectrum Values at Selected Energies:**
Recall $\sinh(x) = \frac{e^x - e^{-x}}{2}$:
- At $E = 0.5\text{ MeV}$:
  $$\sqrt{2.29 \times 0.5} = \sqrt{1.145} \approx 1.0700 \implies \sinh(1.0700) \approx 1.2862$$
  $$e^{-1.036 \times 0.5} = e^{-0.518} \approx 0.5957$$
  $$\chi(0.5) = 0.453 \times 0.5957 \times 1.2862 \approx \mathbf{0.347\text{ MeV}^{-1}}$$

- At $E = 1.0\text{ MeV}$:
  $$\sqrt{2.29} \approx 1.5133 \implies \sinh(1.5133) \approx 2.1645$$
  $$e^{-1.036} \approx 0.35487$$
  $$\chi(1.0) = 0.453 \times 0.35487 \times 2.1645 \approx \mathbf{0.348\text{ MeV}^{-1}}$$

- At $E = 2.0\text{ MeV}$:
  $$\sqrt{4.58} \approx 2.1401 \implies \sinh(2.1401) \approx 4.1952$$
  $$e^{-2.072} \approx 0.12593$$
  $$\chi(2.0) = 0.453 \times 0.12593 \times 4.1952 \approx \mathbf{0.239\text{ MeV}^{-1}}$$

- At $E = 5.0\text{ MeV}$:
  $$\sqrt{11.45} \approx 3.3838 \implies \sinh(3.3838) \approx 14.733$$
  $$e^{-5.18} \approx 0.005628$$
  $$\chi(5.0) = 0.453 \times 0.005628 \times 14.733 \approx \mathbf{0.0376\text{ MeV}^{-1}}$$

**(b) Most Probable Energy $E_{\text{mp}}$:**
Taking the natural logarithm:
$$\ln \chi(E) = \ln(0.453) - 1.036 E + \ln \sinh(\sqrt{2.29 E})$$
Differentiating with respect to $E$:
$$\frac{d}{dE} \ln \chi(E) = -1.036 + \frac{\cosh(\sqrt{2.29 E})}{\sinh(\sqrt{2.29 E})} \cdot \frac{1}{2\sqrt{2.29 E}} \cdot 2.29 = 0$$
$$\frac{\sqrt{2.29}}{2\sqrt{E}} \coth(\sqrt{2.29 E}) = 1.036 \implies \frac{0.7566}{\sqrt{E}} \coth(1.5133 \sqrt{E}) = 1.036$$
Testing $E = 0.72\text{ MeV}$:
$$\sqrt{E} = 0.8485, \quad 1.5133 \times 0.8485 = 1.284$$
$$\coth(1.284) = \frac{1}{\tanh(1.284)} = \frac{1}{0.8576} \approx 1.166$$
$$\frac{0.7566}{0.8485} \times 1.166 = 0.8917 \times 1.166 \approx 1.040 \approx 1.036$$
Thus, the most probable neutron energy is:
$$E_{\text{mp}} \approx \mathbf{0.73\text{ MeV}}$$

**(c) Fast Fission Fraction:**
Evaluating the integral above the fast threshold $E_{\text{th}} = 1.0\text{ MeV}$:
$$F(E > 1.0\text{ MeV}) = \int_{1.0}^{\infty} \chi(E) \, dE \approx \mathbf{0.692} = \mathbf{69.2\%}$$
Approximately **$69.2\%$** of all prompt fission neutrons possess sufficient kinetic energy ($> 1.0\text{ MeV}$) to induce fast fission in $^{238}\text{U}$."""
        },
        {
            "id": "rp-prob-3-3",
            "title": "Fuel Consumption Rate and Annual Core Burnup of a 3000 MWth Commercial Nuclear Power Plant",
            "statement": r"""A nuclear power station operates at a constant thermal power of $P_{\text{th}} = 3400\text{ MW}_{\text{th}}$ with net thermodynamic plant efficiency $\eta_{\text{th}} = 34\%$.
The reactor core is initially loaded with $M_0 = 85.0\text{ metric tons}$ of heavy metal fuel in the form of low-enriched uranium dioxide ($\text{UO}_2$) with an average enrichment of $4.2\%\ {}^{235}\text{U}$ by mass.
The recoverable energy per fission is $Q_{\text{rec}} = 200\text{ MeV}$. The capture-to-fission ratio for $^{235}\text{U}$ is $\alpha = 0.170$.
(a) Determine the net electrical output power $P_e$ of the station in $\text{MW}_e$.
(b) Calculate the daily rate of ${}^{235}\text{U}$ destroyed (by fission plus capture) in $\text{kg/day}$.
(c) After an 18-month (548-day) continuous baseload operating cycle at full power, calculate the total cumulative core burnup in $\text{MWd/MTU}$ and the fraction of initial ${}^{235}\text{U}$ remaining.""",
            "solution": r"""**(a) Net Electrical Power Output $P_e$:**
$$P_e = \eta_{\text{th}} \times P_{\text{th}} = 0.34 \times 3400\text{ MW}_{\text{th}} = \mathbf{1156\text{ MW}_e}$$

**(b) Daily Consumption Rate of $^{235}\text{U}$:**
Daily thermal energy produced:
$$E_{\text{daily}} = 3400\text{ MW} \times 1\text{ day} = 3400\text{ MWd}$$
Fission rate per second:
$$\dot{F} = \frac{3400 \times 10^6\text{ W}}{3.20435 \times 10^{-11}\text{ J/fission}} \approx 1.061 \times 10^{20}\text{ fissions/s}$$
Number of fissions per day:
$$F_{\text{day}} = (1.061 \times 10^{20}\text{ s}^{-1}) \times 86400\text{ s} \approx 9.167 \times 10^{24}\text{ fissions/day}$$
Total atoms of $^{235}\text{U}$ consumed (fission + capture):
$$N_{\text{cons}} = F_{\text{day}} \times (1 + \alpha) = (9.167 \times 10^{24}) \times (1 + 0.170) = 1.0725 \times 10^{25}\text{ atoms/day}$$
Mass consumed per day:
$$\Delta m_{235} = \frac{N_{\text{cons}} \times M({}^{235}\text{U})}{N_A} = \frac{(1.0725 \times 10^{25}) \times 235.044\text{ g/mol}}{6.02214 \times 10^{23}\text{ atoms/mol}}$$
$$\Delta m_{235} \approx 4186\text{ g/day} = \mathbf{4.186\text{ kg of } {}^{235}\text{U} \text{ per day}}$$

**(c) Cumulative Core Burnup and Fuel Inventory:**
Total thermal energy produced over 548 days:
$$E_{\text{total}} = 3400\text{ MW} \times 548\text{ days} = 1{,}863{,}200\text{ MWd}$$
Cumulative fuel burnup:
$$B = \frac{E_{\text{total}}}{M_0} = \frac{1{,}863{,}200\text{ MWd}}{85.0\text{ MTU}} \approx \mathbf{21{,}920\text{ MWd/MTU}} \approx \mathbf{21.92\text{ GWd/MTU}}$$
Initial mass of $^{235}\text{U}$ loaded:
$$M_{235, 0} = 0.042 \times 85{,}000\text{ kg} = 3570\text{ kg}$$
Total mass of $^{235}\text{U}$ consumed over 548 days:
$$\Delta M_{235} = 548\text{ days} \times 4.186\text{ kg/day} \approx 2294\text{ kg}$$
Remaining mass of $^{235}\text{U}$:
$$M_{235, \text{final}} = 3570\text{ kg} - 2294\text{ kg} = 1276\text{ kg}$$
Fraction of initial $^{235}\text{U}$ remaining:
$$\frac{M_{235, \text{final}}}{M_{235, 0}} = \frac{1276}{3570} \approx \mathbf{0.357} = \mathbf{35.7\%}$$
After 18 months, **$64.3\%$** of the original Uranium-235 has been burned, with the core operating partly on bred Plutonium-239."""
        }
    ]
}

u4_data = {
    "title": "Neutron Slowing Down & Moderation Theory",
    "subtitle": "Elastic Scattering Kinematics, Energy Decrement, Lethargy & Resonance Escape Probability",
    "summary": "Mathematical theory of neutron moderation and slowing down: elastic scattering kinematics in the center-of-mass (CM) and laboratory (LAB) frames; collision parameter alpha, maximum fractional energy loss, and scattered neutron energy probability distributions; forward scattering anisotropy in the laboratory system, average scattering cosine, and transport cross section correction; exact analytical derivation of the average logarithmic energy decrement xi and collision count to thermalize; Fermi lethargy variable u and continuous slowing-down mechanics; moderator figures of merit, slowing down power, and moderating ratios for H2O, D2O, Be, and Graphite; slowing-down density q(E) in non-absorbing media versus resonance capture; and the resonance escape probability p with effective resonance integrals.",
    "sections": [
        {
            "id": "sec-4-1",
            "title": "Elastic Collision Kinematics in LAB and Center-of-Mass (CM) Frames",
            "content": r"""
<h3>1. Coordinate Systems for Two-Body Collisions</h3>
<p>
Neutrons born in fission possess an average kinetic energy of $\sim 2\text{ MeV}$, whereas thermal fission requires neutron energies of $\sim 0.0253\text{ eV}$—a reduction by eight orders of magnitude! This slowing down occurs via repeated <strong>billiard-ball elastic scattering collisions</strong> $(n, n)$ with stationary target nuclei of mass number $A$ ($m \approx A \, m_n$).
To analyze the kinematics:
<ul>
  <li><strong>Laboratory (LAB) Frame:</strong> Target nucleus is initially at rest ($V = 0$). Incident neutron has velocity $\vec{v}_1$ and kinetic energy $E_1 = \frac{1}{2} m_n v_1^2$. After scattering at angle $\theta$ relative to the incident direction, the neutron has velocity $\vec{v}_2$ and energy $E_2$.</li>
  <li><strong>Center-of-Mass (CM) Frame:</strong> The center of mass moves with constant laboratory velocity:
  $$\vec{V}_{\text{CM}} = \frac{m_n \vec{v}_1 + M \vec{0}}{m_n + M} = \frac{1}{A + 1} \vec{v}_1$$
  In the CM system, total linear momentum is identically zero both before and after collision.</li>
</ul>
</p>

<h3>2. CM Velocities and Elastic Conservation</h3>
<p>
Before collision in CM:
$$u_1 = v_1 - V_{\text{CM}} = v_1 \left( 1 - \frac{1}{A+1} \right) = \frac{A}{A + 1} v_1$$
$$U_1 = 0 - V_{\text{CM}} = -\frac{1}{A + 1} v_1$$
Because elastic scattering conserves kinetic energy in the CM frame, the speeds of the particles are unchanged after collision; only their direction rotates through scattering angle $\theta_{\text{CM}}$:
$$u_2 = u_1 = \frac{A}{A + 1} v_1, \qquad U_2 = |U_1| = \frac{1}{A + 1} v_1$$
</p>
"""
        },
        {
            "id": "sec-4-2",
            "title": "Collision Parameter Alpha & Energy Distribution of Scattered Neutrons",
            "content": r"""
<h3>1. Velocity Vector Addition and Energy Ratio</h3>
<p>
Transforming back to the Laboratory system, the final neutron velocity vector is the vector sum:
$$\vec{v}_2 = \vec{u}_2 + \vec{V}_{\text{CM}}$$
Using the law of cosines:
$$v_2^2 = u_2^2 + V_{\text{CM}}^2 + 2 u_2 V_{\text{CM}} \cos\theta_{\text{CM}}$$
Substituting $u_2 = \frac{A}{A+1} v_1$ and $V_{\text{CM}} = \frac{1}{A+1} v_1$:
$$v_2^2 = v_1^2 \left[ \left(\frac{A}{A+1}\right)^2 + \left(\frac{1}{A+1}\right)^2 + \frac{2 A}{(A+1)^2} \cos\theta_{\text{CM}} \right]$$
Factoring out $(A+1)^2$:
$$\frac{E_2}{E_1} = \frac{v_2^2}{v_1^2} = \frac{A^2 + 1 + 2 A \cos\theta_{\text{CM}}}{(A+1)^2}$$
We define the fundamental <strong>collision parameter</strong> $\alpha$:
$$\alpha \equiv \left( \frac{A - 1}{A + 1} \right)^2$$
Rewriting $A^2 + 1 = \frac{1}{2} [(A+1)^2 + (A-1)^2]$:
$$\mathbf{\frac{E_2}{E_1} = \frac{1 + \alpha}{2} + \frac{1 - \alpha}{2} \cos\theta_{\text{CM}}}$$
</p>

<h3>2. Extreme Collision Scenarios</h3>
<p>
<ul>
  <li><strong>Glancing Collision ($\theta_{\text{CM}} = 0$, $\cos\theta_{\text{CM}} = 1$):</strong>
  $$\frac{E_2}{E_1} = \frac{1+\alpha}{2} + \frac{1-\alpha}{2} = 1 \implies E_2 = E_1 \quad (\text{No energy lost})$$</li>
  <li><strong>Head-on Collision ($\theta_{\text{CM}} = \pi$, $\cos\theta_{\text{CM}} = -1$):</strong>
  $$\frac{E_2}{E_1} = \frac{1+\alpha}{2} - \frac{1-\alpha}{2} = \alpha \implies E_2 = \alpha E_1 \quad (\text{Maximum possible energy loss!})$$</li>
</ul>
The scattered neutron energy is bounded strictly in the interval:
$$\alpha E_1 \le E_2 \le E_1$$
For hydrogen ($A = 1$): $\alpha = 0$, meaning a neutron can lose $100\%$ of its kinetic energy in a single head-on collision! For Carbon-12 ($A = 12$): $\alpha = (11/13)^2 = 0.716$, meaning at most $28.4\%$ can be lost per collision. For Uranium-238 ($A = 238$): $\alpha = (237/239)^2 = 0.983$, so at most $1.7\%$ can be lost.
</p>

<h3>3. Uniform Scattered Energy Probability Distribution</h3>
<p>
In the CM frame, for energies below $\sim 1\text{ MeV}$, elastic scattering is spherically symmetric (s-wave scattering):
$$P(\theta_{\text{CM}}) \, d\Omega_{\text{CM}} = \frac{2\pi \sin\theta_{\text{CM}} \, d\theta_{\text{CM}}}{4\pi} = \frac{1}{2} d(\cos\theta_{\text{CM}})$$
Since $E_2$ depends linearly on $\cos\theta_{\text{CM}}$, $dE_2 = \frac{1-\alpha}{2} E_1 \, d(\cos\theta_{\text{CM}})$:
$$P(E_1 \to E_2) \, dE_2 = \frac{dE_2}{(1 - \alpha) E_1} \quad \text{for } \alpha E_1 \le E_2 \le E_1$$
The probability distribution is perfectly flat (uniform) between $\alpha E_1$ and $E_1$, with zero probability outside.
</p>
"""
        },
        {
            "id": "sec-4-3",
            "title": "Forward Scattering Anisotropy in LAB System & Transport Cross Section",
            "content": r"""
<h3>1. Laboratory Scattering Angle Cosine $\mu_0$</h3>
<p>
Even though scattering is isotropic in the Center-of-Mass frame, the forward motion of the center of mass biases collisions forward in the Laboratory frame.
From the velocity vector triangle:
$$v_2 \cos\theta = u_2 \cos\theta_{\text{CM}} + V_{\text{CM}} = \frac{A v_1 \cos\theta_{\text{CM}} + v_1}{A + 1}$$
Dividing by $v_2 = v_1 \sqrt{\frac{1+\alpha}{2} + \frac{1-\alpha}{2}\cos\theta_{\text{CM}}}$:
$$\mu_0 \equiv \cos\theta_{\text{LAB}} = \frac{1 + A \cos\theta_{\text{CM}}}{\sqrt{A^2 + 1 + 2 A \cos\theta_{\text{CM}}}}$$
</p>

<h3>2. The Average Cosine of the Scattering Angle $\bar{\mu}_0$</h3>
<p>
Averaging $\mu_0$ over all isotropic CM solid angles:
$$\bar{\mu}_0 \equiv \langle \cos\theta_{\text{LAB}} \rangle = \int_{-1}^{1} \mu_0(\cos\theta_{\text{CM}}) \, \frac{d(\cos\theta_{\text{CM}})}{2}$$
Evaluating this integral yields the celebrated exact result:
$$\mathbf{\bar{\mu}_0 = \frac{2}{3 A}}$$
Key values:
<ul>
  <li>For Hydrogen ($A = 1$): $\bar{\mu}_0 = 2/3 \approx 0.667$ (strongly forward-peaked).</li>
  <li>For Deuterium ($A = 2$): $\bar{\mu}_0 = 1/3 \approx 0.333$.</li>
  <li>For Carbon-12 ($A = 12$): $\bar{\mu}_0 = 2/36 \approx 0.056$.</li>
  <li>For Heavy Nuclei ($A \gg 1$): $\bar{\mu}_0 \to 0$ (nearly isotropic in LAB frame).</li>
</ul>
</p>

<h3>3. Transport Cross Section $\Sigma_{\text{tr}}$</h3>
<p>
Because forward-scattered neutrons preserve forward momentum, they diffuse farther than if scattering were isotropic. To account for this persistence of velocity, transport theory defines the <strong>transport cross section</strong>:
$$\mathbf{\Sigma_{\text{tr}} = \Sigma_s (1 - \bar{\mu}_0) = \Sigma_s \left( 1 - \frac{2}{3A} \right)}$$
The corresponding <strong>transport mean free path</strong> $\lambda_{\text{tr}}$ is:
$$\lambda_{\text{tr}} = \frac{1}{\Sigma_{\text{tr}}} = \frac{\lambda_s}{1 - \bar{\mu}_0}$$
In Hydrogen, $\lambda_{\text{tr}} = \frac{\lambda_s}{1 - 2/3} = 3 \, \lambda_s$: forward-peaked scattering triples the effective diffusion length per collision!
</p>
"""
        },
        {
            "id": "sec-4-4",
            "title": "Average Logarithmic Energy Decrement Xi & Collisions to Thermalize",
            "content": r"""
<h3>1. Definition of Logarithmic Energy Decrement $\xi$</h3>
<p>
Because the fractional energy remaining after a collision is independent of initial energy, the change in the natural logarithm of neutron energy is a constant property of the moderating nuclide:
$$\xi \equiv \left\langle \ln\left(\frac{E_1}{E_2}\right) \right\rangle = \int_{\alpha E_1}^{E_1} \ln\left(\frac{E_1}{E_2}\right) P(E_1 \to E_2) \, dE_2$$
Substituting the uniform probability density $P(E_1 \to E_2) = \frac{1}{(1-\alpha)E_1}$ and letting $x = E_2 / E_1$:
$$\xi = \frac{1}{1 - \alpha} \int_{\alpha}^{1} \ln\left(\frac{1}{x}\right) dx = -\frac{1}{1 - \alpha} [x \ln x - x]_\alpha^1$$
Evaluating at the integration limits:
$$\mathbf{\xi = 1 + \frac{\alpha}{1 - \alpha} \ln \alpha}$$
</p>

<h3>2. Asymptotic Approximations</h3>
<p>
Using $\alpha = \left(\frac{A-1}{A+1}\right)^2$:
<ul>
  <li><strong>For Hydrogen ($A = 1, \alpha = 0$):</strong>
  $$\xi_{\text{H}} = 1 + 0 = \mathbf{1.000}$$</li>
  <li><strong>For Intermediate and Heavy Nuclei ($A > 10$):</strong>
  Taylor series expansion in powers of $1/A$ yields:
  $$\mathbf{\xi \approx \frac{2}{A + \frac{2}{3}} \approx \frac{2}{A}}$$
  This approximation is accurate to within $1\%$ for all $A \ge 10$.</li>
</ul>
</p>

<h3>3. Average Number of Collisions to Thermalize</h3>
<p>
To slow a neutron from fission birth energy ($E_0 = 2.0\text{ MeV}$) to thermal energy ($E_{\text{th}} = 0.0253\text{ eV}$):
$$\ln\left(\frac{E_0}{E_{\text{th}}}\right) = \ln\left(\frac{2.0 \times 10^6\text{ eV}}{0.0253\text{ eV}}\right) = \ln(7.905 \times 10^7) \approx 18.186$$
The average number of elastic collisions $N_{\text{coll}}$ required is:
$$\mathbf{N_{\text{coll}} = \frac{\ln(E_0 / E_{\text{th}})}{\xi} = \frac{18.2}{\xi}}$$
Comparing candidate moderators:
<ul>
  <li><strong>Hydrogen (${}^1\text{H}$):</strong> $\xi = 1.000 \implies N_{\text{coll}} \approx \mathbf{18\text{ collisions}}$</li>
  <li><strong>Deuterium (${}^2\text{H}$):</strong> $\xi = 0.725 \implies N_{\text{coll}} \approx \mathbf{25\text{ collisions}}$</li>
  <li><strong>Beryllium (${}^9\text{Be}$):</strong> $\xi = 0.207 \implies N_{\text{coll}} \approx \mathbf{88\text{ collisions}}$</li>
  <li><strong>Carbon (${}^{12}\text{C}$):</strong> $\xi = 0.158 \implies N_{\text{coll}} \approx \mathbf{115\text{ collisions}}$</li>
  <li><strong>Uranium (${}^{238}\text{U}$):</strong> $\xi = 0.0084 \implies N_{\text{coll}} \approx \mathbf{2170\text{ collisions}}$</li>
</ul>
</p>
"""
        },
        {
            "id": "sec-4-5",
            "title": "Fermi Lethargy Variable & Continuous Slowing-Down Mechanics",
            "content": r"""
<h3>1. The Lethargy Variable $u$</h3>
<p>
As a neutron slows down, its energy decreases over several orders of magnitude. In 1944, Enrico Fermi introduced the dimensionless <strong>lethargy</strong> variable $u$ to linearize the logarithmic energy scale:
$$u \equiv \ln\left( \frac{E_0}{E} \right)$$
where $E_0$ is an arbitrary reference maximum energy (typically the top of the fission spectrum, $E_0 = 10\text{ MeV}$).
Key properties:
<ul>
  <li>At high energy $E = E_0$: $u = 0$.</li>
  <li>As energy slows down ($E \to 0$): lethargy increases ($u \to \infty$).</li>
  <li>Differential relationship:
  $$du = - \frac{dE}{E} \implies \phi(u) \, du = \phi(E) \, dE \implies \phi(u) = E \, \phi(E)$$</li>
</ul>
</p>

<h3>2. Lethargy Gain Per Collision</h3>
<p>
The average increase in lethargy per elastic scattering collision is precisely equal to the logarithmic energy decrement:
$$\langle \Delta u \rangle = \left\langle \ln\frac{E_1}{E_2} \right\rangle = \xi$$
In lethargy space, neutron slowing down appears as a steady drift toward increasing $u$ at an average rate of $\xi$ units per collision.
</p>
"""
        },
        {
            "id": "sec-4-6",
            "title": "Moderator Figures of Merit: Slowing Down Power & Moderating Ratio",
            "content": r"""
<h3>1. Slowing Down Power (SDP)</h3>
<p>
A superior moderator must not only reduce neutron energy rapidly per collision ($\xi$), but must also have a high collision probability per centimeter of travel ($\Sigma_s$). We define the <strong>Macroscopic Slowing Down Power</strong>:
$$\mathbf{\text{SDP} \equiv \xi \, \Sigma_s\quad [\text{cm}^{-1}]}$$
This represents the average decrease in logarithmic energy per unit path length traveled by the neutron.
</p>

<h3>2. Moderating Ratio (MR)</h3>
<p>
A high slowing down power is useless if the material simultaneously swallows neutrons via radiative capture! The true figure of merit for a nuclear reactor moderator is the <strong>Moderating Ratio</strong> ($MR$):
$$\mathbf{\text{MR} \equiv \frac{\xi \, \Sigma_s}{\Sigma_a} = \frac{\text{Slowing Down Power}}{\text{Thermal Absorption Cross Section}}}$$
Comparing the primary commercial moderators:
</p>
<table style="width:100%; border-collapse: collapse; margin: 16px 0; text-align: left;">
  <thead>
    <tr style="border-bottom: 2px solid #4a5568;">
      <th style="padding: 8px;">Moderator</th>
      <th style="padding: 8px;">$\xi$</th>
      <th style="padding: 8px;">$\Sigma_s\ (\text{cm}^{-1})$</th>
      <th style="padding: 8px;">$\Sigma_a\ (\text{cm}^{-1})$</th>
      <th style="padding: 8px;">SDP ($\xi\Sigma_s,\ \text{cm}^{-1}$)</th>
      <th style="padding: 8px;">Moderating Ratio ($\xi\Sigma_s/\Sigma_a$)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #2d3748;">
      <td style="padding: 8px;">Light Water ($\text{H}_2\text{O}$)</td>
      <td style="padding: 8px;">$0.920$</td>
      <td style="padding: 8px;">$1.47$</td>
      <td style="padding: 8px;">$0.022$</td>
      <td style="padding: 8px;">$\mathbf{1.35}$ (Best SDP)</td>
      <td style="padding: 8px;">$\mathbf{61}$</td>
    </tr>
    <tr style="border-bottom: 1px solid #2d3748;">
      <td style="padding: 8px;">Heavy Water ($\text{D}_2\text{O}$)</td>
      <td style="padding: 8px;">$0.509$</td>
      <td style="padding: 8px;">$0.35$</td>
      <td style="padding: 8px;">$3.3 \times 10^{-5}$</td>
      <td style="padding: 8px;">$0.18$</td>
      <td style="padding: 8px;">$\mathbf{5670}$ (Unmatched MR!)</td>
    </tr>
    <tr style="border-bottom: 1px solid #2d3748;">
      <td style="padding: 8px;">Beryllium ($\text{Be}$)</td>
      <td style="padding: 8px;">$0.207$</td>
      <td style="padding: 8px;">$0.76$</td>
      <td style="padding: 8px;">$1.2 \times 10^{-3}$</td>
      <td style="padding: 8px;">$0.16$</td>
      <td style="padding: 8px;">$\mathbf{133}$</td>
    </tr>
    <tr style="border-bottom: 2px solid #4a5568;">
      <td style="padding: 8px;">Graphite ($\text{C}$)</td>
      <td style="padding: 8px;">$0.158$</td>
      <td style="padding: 8px;">$0.38$</td>
      <td style="padding: 8px;">$3.2 \times 10^{-4}$</td>
      <td style="padding: 8px;">$0.06$</td>
      <td style="padding: 8px;">$\mathbf{192}$</td>
    </tr>
  </tbody>
</table>
<p>
<strong>Key Engineering Insights:</strong>
<ul>
  <li>$\text{H}_2\text{O}$ has the highest Slowing Down Power ($1.35\text{ cm}^{-1}$), allowing ultra-compact reactor cores (PWR, BWR). However, its moderate MR ($61$) requires enriched uranium fuel ($\ge 3\%\ {}^{235}\text{U}$) because natural uranium cannot achieve criticality in light water!</li>
  <li>$\text{D}_2\text{O}$ has an astonishing Moderating Ratio ($5670$) because deuterium captures virtually zero neutrons. This enables CANDU reactors to achieve criticality using cheap, un-enriched natural uranium ($0.72\%\ {}^{235}\text{U}$).</li>
</ul>
</p>
"""
        },
        {
            "id": "sec-4-7",
            "title": "Slowing Down Density, Resonance Escape Probability & Resonance Integrals",
            "content": r"""
<h3>1. The Slowing Down Density $q(E)$</h3>
<p>
The <strong>slowing down density</strong> $q(E, \vec{r})$ is defined as the number of neutrons per unit volume per second that slow down past energy $E$.
In a non-absorbing infinite medium with constant scattering cross section:
$$q(E) = \xi \, \Sigma_s \, E \, \phi(E) = \text{constant} = S$$
where $S$ is the source rate of fast fission neutrons. Hence, the epithermal slowing down flux exhibits the famous universal $1/E$ dependence:
$$\mathbf{\phi(E) = \frac{S}{\xi \, \Sigma_s \, E} \propto \frac{1}{E}}$$
</p>

<h3>2. Resonance Absorption and Escape Probability $p$</h3>
<p>
In real reactor fuels containing fertile ${}^{238}\text{U}$, the epithermal range ($1\text{ eV} \le E \le 1000\text{ eV}$) features hundreds of giant, razor-sharp $(n, \gamma)$ absorption resonances.
As neutrons slow through an energy increment $dE$, the fraction absorbed is $\frac{\Sigma_a(E)}{\Sigma_t(E)} \frac{dE}{\xi E}$:
$$\frac{dq}{q} = \frac{\Sigma_a(E)}{\xi \Sigma_s(E) + \Sigma_a(E)} \frac{dE}{E}$$
Integrating from fission energy $E_0$ down to thermal cut-off energy $E_{\text{th}}$ yields the <strong>Resonance Escape Probability</strong> ($p$):
$$\mathbf{p = \exp\left( - \int_{E_{\text{th}}}^{E_0} \frac{\Sigma_a(E)}{\xi \Sigma_s + \Sigma_a(E)} \frac{dE}{E} \right)}$$
For a homogeneous fuel-moderator mixture where $\Sigma_a \ll \xi \Sigma_s$:
$$\mathbf{p = \exp\left( - \frac{N_F}{\xi \Sigma_s} I_{\text{eff}} \right)}$$
where $I_{\text{eff}} \equiv \int_{E_{\text{th}}}^{E_0} \sigma_{a, \text{eff}}^F(E) \frac{dE}{E}$ is the <strong>Effective Resonance Integral</strong> (in barns).
In heterogeneous lattices (fuel rods separated by moderator), resonance absorption is drastically reduced because neutrons moderate in the pure moderator without seeing fuel resonances, and self-shielding depresses the resonance flux inside the rod!
</p>
"""
        }
    ],
    "exercises": [
        {
            "id": "rp-prob-4-1",
            "title": "Moderation Collisions and Energy Degradation in Light Water vs Heavy Water vs Graphite",
            "statement": r"""Compare the slowing down capability of Light Water ($\text{H}_2\text{O}$), Heavy Water ($\text{D}_2\text{O}$), and Graphite ($\text{C}$) for neutrons born at $E_0 = 2.0\text{ MeV}$ slowing to $E_{\text{th}} = 0.0253\text{ eV}$.
(a) For a composite molecule with multiple atomic species, the effective logarithmic energy decrement is given by:
$$\bar{\xi} = \frac{\sum_i \sigma_{s, i} \, \xi_i}{\sum_i \sigma_{s, i}}$$
Given:
- For ${}^1\text{H}$: $\xi_1 = 1.000, \sigma_s = 20.5\text{ b}$
- For ${}^2\text{H}$: $\xi_2 = 0.725, \sigma_s = 3.4\text{ b}$
- For ${}^{16}\text{O}$: $\xi_{\text{O}} \approx 0.120, \sigma_s = 3.8\text{ b}$
- For ${}^{12}\text{C}$: $\xi_{\text{C}} = 0.158, \sigma_s = 4.8\text{ b}$
Calculate $\bar{\xi}$ for molecular $\text{H}_2\text{O}$ and $\text{D}_2\text{O}$.
(b) Calculate the average number of collisions $N_{\text{coll}}$ required to thermalize a fission neutron in $\text{H}_2\text{O}$, $\text{D}_2\text{O}$, and pure Graphite.
(c) Assuming a neutron has an average speed of $10^6\text{ m/s}$ during moderation and mean free path $\lambda_s = 0.7\text{ cm}$ in light water, estimate the total time required for thermalization in light water.""",
            "solution": r"""**(a) Molecular Average Decrement $\bar{\xi}$:**
- For $\text{H}_2\text{O}$ (two H atoms and one O atom):
  $$\sum \sigma_{s, i} \xi_i = 2 \times (20.5 \times 1.000) + 1 \times (3.8 \times 0.120) = 41.0 + 0.456 = 41.456\text{ b}$$
  $$\sum \sigma_{s, i} = 2 \times 20.5 + 3.8 = 41.0 + 3.8 = 44.8\text{ b}$$
  $$\bar{\xi}(\text{H}_2\text{O}) = \frac{41.456}{44.8} \approx \mathbf{0.9254}$$

- For $\text{D}_2\text{O}$ (two D atoms and one O atom):
  $$\sum \sigma_{s, i} \xi_i = 2 \times (3.4 \times 0.725) + 1 \times (3.8 \times 0.120) = 4.930 + 0.456 = 5.386\text{ b}$$
  $$\sum \sigma_{s, i} = 2 \times 3.4 + 3.8 = 6.8 + 3.8 = 10.6\text{ b}$$
  $$\bar{\xi}(\text{D}_2\text{O}) = \frac{5.386}{10.6} \approx \mathbf{0.5081}$$

**(b) Average Number of Collisions to Thermalize:**
Total lethargy span:
$$u_{\text{tot}} = \ln\left( \frac{E_0}{E_{\text{th}}} \right) = \ln\left( \frac{2.0 \times 10^6}{0.0253} \right) \approx 18.186$$
- In Light Water ($\text{H}_2\text{O}$):
  $$N_{\text{coll}}(\text{H}_2\text{O}) = \frac{18.186}{0.9254} \approx \mathbf{19.65 \approx 20\text{ collisions}}$$
- In Heavy Water ($\text{D}_2\text{O}$):
  $$N_{\text{coll}}(\text{D}_2\text{O}) = \frac{18.186}{0.5081} \approx \mathbf{35.79 \approx 36\text{ collisions}}$$
- In Graphite ($\text{C}$):
  $$N_{\text{coll}}(\text{C}) = \frac{18.186}{0.158} \approx \mathbf{115.1 \approx 115\text{ collisions}}$$

**(c) Estimated Thermalization Time in Light Water:**
The mean collision time between scatterings is:
$$\Delta t_1 = \frac{\lambda_s}{\bar{v}} = \frac{0.7 \times 10^{-2}\text{ m}}{10^6\text{ m/s}} = 7.0 \times 10^{-9}\text{ s} = 7.0\text{ ns}$$
Multiplying by $N_{\text{coll}} \approx 20$ collisions:
$$t_{\text{therm}} \approx 20 \times 7.0\text{ ns} \approx \mathbf{1.4 \times 10^{-7}\text{ s}} = \mathbf{0.14\ \mu\text{s}}$$
A fast neutron completes its entire journey to thermal equilibrium in just **$0.14\text{ microseconds}$**!"""
        },
        {
            "id": "rp-prob-4-2",
            "title": "Derivation of the Exact Formula for Average Logarithmic Energy Decrement Xi(A)",
            "statement": r"""Starting from first principles of two-body elastic collision kinematics:
(a) Write the probability distribution $P(E_1 \to E_2)$ for isotropic scattering in the center-of-mass frame.
(b) Evaluate the integral defining the average logarithmic energy decrement:
$$\xi = \int_{\alpha E_1}^{E_1} \ln\left( \frac{E_1}{E_2} \right) P(E_1 \to E_2) \, dE_2$$
showing all steps to derive $\xi = 1 + \frac{\alpha}{1 - \alpha} \ln \alpha$.
(c) Using the Taylor series expansion $\ln(1 - x) = -x - \frac{x^2}{2} - \frac{x^3}{3} - \dots$, demonstrate that for $A \gg 1$:
$$\xi \approx \frac{2}{A + 2/3}$$""",
            "solution": r"""**(a) Probability Distribution:**
In the center-of-mass frame, s-wave scattering is isotropic:
$$P(\Omega_{\text{CM}}) d\Omega_{\text{CM}} = \frac{d(\cos\theta_{\text{CM}})}{2}$$
The laboratory scattered energy is:
$$E_2 = E_1 \left[ \frac{1+\alpha}{2} + \frac{1-\alpha}{2} \cos\theta_{\text{CM}} \right]$$
Taking the differential:
$$dE_2 = E_1 \frac{1-\alpha}{2} d(\cos\theta_{\text{CM}}) \implies d(\cos\theta_{\text{CM}}) = \frac{2 dE_2}{(1-\alpha) E_1}$$
Hence:
$$P(E_1 \to E_2) \, dE_2 = \frac{1}{(1-\alpha) E_1} \, dE_2 \quad \text{for } \alpha E_1 \le E_2 \le E_1$$

**(b) Exact Integration for $\xi$:**
Let dimensionless variable $y = E_2 / E_1$, so $dy = dE_2 / E_1$ and $y$ ranges from $\alpha$ to $1$:
$$\xi = \frac{1}{1-\alpha} \int_{\alpha}^{1} \ln\left( \frac{1}{y} \right) dy = - \frac{1}{1-\alpha} \int_{\alpha}^{1} \ln y \, dy$$
Using integration by parts $\int \ln y \, dy = y \ln y - y$:
$$\int_{\alpha}^{1} \ln y \, dy = [y \ln y - y]_\alpha^1 = (0 - 1) - (\alpha \ln\alpha - \alpha) = -1 - \alpha \ln\alpha + \alpha = -(1 - \alpha) - \alpha \ln\alpha$$
Substituting back:
$$\xi = - \frac{1}{1-\alpha} [-(1 - \alpha) - \alpha \ln\alpha] = 1 + \frac{\alpha \ln\alpha}{1 - \alpha}$$
Thus:
$$\mathbf{\xi = 1 + \frac{\alpha}{1 - \alpha} \ln\alpha} \quad \text{(Q.E.D.)}$$

**(c) Large-A Approximation:**
Recall $\alpha = \left( \frac{A-1}{A+1} \right)^2 = \left( \frac{1 - 1/A}{1 + 1/A} \right)^2 \approx \left( 1 - \frac{2}{A} + \frac{2}{A^2} \right)^2 \approx 1 - \frac{4}{A} + \frac{8}{A^2}$.
Let $\epsilon = \frac{2}{A}$. Then $\frac{A-1}{A+1} = \frac{1 - \epsilon/2}{1 + \epsilon/2} = 1 - \epsilon + \frac{\epsilon^2}{2} - \frac{\epsilon^3}{4} + \dots$
Squaring gives $\alpha = 1 - 2\epsilon + 2\epsilon^2 - \frac{4}{3}\epsilon^3 + \dots$
Expanding $\ln\alpha = \ln(1 - (1-\alpha))$ in powers of $1/A$ and evaluating yields:
$$\xi = \frac{2}{A} - \frac{4}{3 A^2} + \frac{8}{9 A^3} - \dots$$
Comparing with the reciprocal expansion:
$$\frac{2}{A + 2/3} = \frac{2}{A (1 + 2/(3A))} = \frac{2}{A} \left( 1 - \frac{2}{3A} + \frac{4}{9A^2} - \dots \right) = \frac{2}{A} - \frac{4}{3A^2} + \frac{8}{9A^3} - \dots$$
The two series match identically up to second order in $1/A$! Thus:
$$\mathbf{\xi \approx \frac{2}{A + 2/3}} \quad \text{(Q.E.D.)}$$"""
        },
        {
            "id": "rp-prob-4-3",
            "title": "Resonance Escape Probability and Effective Resonance Integral in a Fuel Lattice",
            "statement": r"""A homogeneous thermal reactor core consists of a mixture of natural uranium fuel and graphite moderator with atomic ratio $N_C / N_U = 450$.
The effective resonance integral of natural uranium in this mixture is $I_{\text{eff}} = 12.5\text{ barns} = 12.5 \times 10^{-24}\text{ cm}^2$.
For Carbon ($C$): $\xi_C = 0.158$, $\sigma_{s, C} = 4.8\text{ b}$.
For Uranium ($U$): $\sigma_{s, U} = 8.9\text{ b}$.
(a) Calculate the average macroscopic slowing down power per uranium atom $\frac{\xi \Sigma_s}{N_U}$ in barns.
(b) Calculate the resonance escape probability $p$ for this homogeneous mixture.
(c) If the fuel is redesigned into a heterogeneous lumped fuel rod lattice, resonance self-shielding reduces $I_{\text{eff}}$ from $12.5\text{ b}$ down to $8.2\text{ b}$. Recalculate $p$ and determine the percentage gain in $p$.""",
            "solution": r"""**(a) Average Slowing Down Power per Uranium Atom:**
The total macroscopic scattering cross section per uranium atom is:
$$\frac{\Sigma_s}{N_U} = \frac{N_U \sigma_{s, U} + N_C \sigma_{s, C}}{N_U} = \sigma_{s, U} + \frac{N_C}{N_U} \sigma_{s, C}$$
$$\frac{\Sigma_s}{N_U} = 8.9\text{ b} + (450 \times 4.8\text{ b}) = 8.9 + 2160 = 2168.9\text{ b}$$
Because the moderator atoms dominate ($99.6\%$ of scatterings are on Carbon), the average logarithmic energy decrement is:
$$\bar{\xi} \approx \xi_C = 0.158$$
Therefore:
$$\frac{\xi \Sigma_s}{N_U} = 0.158 \times 2168.9\text{ b} \approx \mathbf{342.69\text{ b}}$$

**(b) Resonance Escape Probability in Homogeneous Mixture:**
Using the resonance formula:
$$p_{\text{hom}} = \exp\left( - \frac{N_U \cdot I_{\text{eff}}}{\xi \Sigma_s} \right) = \exp\left( - \frac{I_{\text{eff}}}{\frac{\xi \Sigma_s}{N_U}} \right)$$
$$p_{\text{hom}} = \exp\left( - \frac{12.5\text{ b}}{342.69\text{ b}} \right) = \exp(-0.036476) \approx \mathbf{0.96418}$$
The resonance escape probability is **$96.42\%$**.

**(c) Heterogeneous Lattice Lumped Fuel Effect:**
With reduced effective resonance integral $I_{\text{eff}} = 8.2\text{ b}$:
$$p_{\text{het}} = \exp\left( - \frac{8.2\text{ b}}{342.69\text{ b}} \right) = \exp(-0.023928) \approx \mathbf{0.97636}$$
Percentage increase in resonance escape probability:
$$\Delta p = \frac{p_{\text{het}} - p_{\text{hom}}}{p_{\text{hom}}} \times 100\% = \frac{0.97636 - 0.96418}{0.96418} \times 100\% \approx \mathbf{+1.26\%}$$
While $+1.26\%$ appears modest, an increase of $\Delta p \approx +0.0122$ in neutron economy raises $k_\infty$ directly by $+1220\text{ pcm}$—easily the difference between a subcritical assembly and a functioning critical reactor!"""
        }
    ]
}

with open("rp_u3.json", "w", encoding="utf-8") as f:
    json.dump(u3_data, f, indent=2, ensure_ascii=False)

with open("rp_u4.json", "w", encoding="utf-8") as f:
    json.dump(u4_data, f, indent=2, ensure_ascii=False)

print("rp_u3.json and rp_u4.json successfully written!")
