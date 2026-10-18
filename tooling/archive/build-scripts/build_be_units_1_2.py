# Unit 1 & Unit 2 Builder for Basic Electronics
import json

u1 = {
    "unitNumber": 1,
    "number": 1,
    "title": "Semiconductor Diodes, Rectifiers & Filter Circuits",
    "subtitle": "Band Theory, PN Junctions, Shockley Diode Equation, Rectification, Smoothing Filters & Zener Regulators",
    "description": "Exhaustive treatment of semiconductor physics, energy band structures, intrinsic and extrinsic carrier statistics, PN junction built-in barriers, Shockley diode equation, half-wave and full-wave rectifiers with efficiency and ripple derivations, capacitor/inductor/choke-input/pi-section filters, and Zener diode shunt voltage regulators.",
    "topics": [
        "Energy Bands in Solids & Carrier Statistics",
        "PN Junction Formation & Built-in Potential Barrier",
        "Diode I-V Characteristics & Shockley Equation",
        "Half-Wave & Full-Wave Rectification Analysis",
        "Power Supply Smoothing Filters (C, L, LC, Pi-section)",
        "Zener Diode Breakdown & Voltage Stabilization"
    ],
    "sections": [
        {
            "id": "u1-sec1",
            "title": "Energy Band Description of Semiconductors & Carrier Statistics",
            "content": """
<h4>1. Energy Band Structure in Crystalline Solids</h4>
In isolated atoms, electronic energy levels are discrete. When $N$ atoms assemble into a periodic crystal lattice, the overlapping atomic orbitals split by the Pauli exclusion principle into dense quasi-continuous energy bands separated by forbidden energy gaps (bandgaps $E_g$):
<ul>
  <li><strong>Valence Band ($E_V$):</strong> The highest occupied energy band composed of valence electron states forming interatomic covalent bonds. At absolute zero ($T = 0\\text{ K}$), the valence band in pure semiconductors is completely filled.</li>
  <li><strong>Conduction Band ($E_C$):</strong> The lowest unoccupied band above the valence band. Electrons excited into this band are delocalized and free to accelerate under applied electric fields.</li>
  <li><strong>Forbidden Energy Gap ($E_g = E_C - E_V$):</strong> No quantum electron states can exist in this interval. For insulators, $E_g > 3.0\\text{ eV}$ (e.g., diamond $E_g \\approx 5.4\\text{ eV}$). For semiconductors, $E_g$ is moderate: Silicon has $E_g \\approx 1.12\\text{ eV}$, and Germanium has $E_g \\approx 0.67\\text{ eV}$ at $300\\text{ K}$. In metals, the conduction and valence bands overlap ($E_g = 0$).</li>
</ul>

<h4>2. Direct vs. Indirect Bandgap Semiconductors</h4>
In a <strong>direct bandgap</strong> semiconductor (e.g., GaAs with $E_g = 1.42\\text{ eV}$, InP), the minimum of the conduction band and maximum of the valence band align at the exact same crystal momentum $\\vec{k} = 0$. Electron-hole recombination can occur radiatively via single-photon emission, making them ideal for LEDs, laser diodes, and solid-state lighting.
In an <strong>indirect bandgap</strong> semiconductor (e.g., Si, Ge), the conduction band minimum is shifted in $\\vec{k}$-space relative to the valence band maximum. Recombination requires the simultaneous emission or absorption of a crystal lattice vibration (phonon) to conserve momentum:
<div class="math-display">$$\\hbar \\vec{k}_e = \\hbar \\vec{k}_h + \\hbar \\vec{q}_{\\text{phonon}}$$</div>
making radiative recombination highly inefficient.

<h4>3. Intrinsic Carrier Density & The Law of Mass Action</h4>
At finite temperature $T > 0\\text{ K}$, thermal phonons excite electrons across $E_g$ into the conduction band, leaving behind vacant bonding states in the valence band termed <strong>holes</strong>. A hole acts dynamically as a mobile carrier with positive elementary charge $+q$ and effective mass $m_h^*$.
The probability of electron occupancy at energy $E$ is governed by the <strong>Fermi-Dirac distribution</strong>:
<div class="math-display">$$f(E) = \\frac{1}{1 + e^{(E - E_F)/k_B T}}$$</div>
where $E_F$ is the <strong>Fermi energy level</strong>. In an intrinsic semiconductor, the free electron concentration $n$ in the conduction band and hole concentration $p$ in the valence band are:
<div class="math-display">$$n = N_C e^{-(E_C - E_F)/k_B T}, \\quad p = N_V e^{-(E_F - E_V)/k_B T}$$</div>
where $N_C = 2\\left(\\frac{2\\pi m_e^* k_B T}{h^2}\\right)^{3/2}$ and $N_V = 2\\left(\\frac{2\\pi m_h^* k_B T}{h^2}\\right)^{3/2}$ are the effective density of states.
Since each thermal generation creates one electron-hole pair, $n = p = n_i$. Multiplying $n$ and $p$ delivers the fundamental <strong>Law of Mass Action</strong>:
<div class="math-display">$$n p = n_i^2 = N_C N_V e^{-E_g / k_B T}$$</div>
In an intrinsic semiconductor, the intrinsic Fermi level lies almost precisely at mid-gap:
<div class="math-display">$$E_{Fi} = \\frac{E_C + E_V}{2} + \\frac{3}{4} k_B T \\ln\\left( \\frac{m_h^*}{m_e^*} \\right)$$</div>
"""
        },
        {
            "id": "u1-sec2",
            "title": "Extrinsic Semiconductors: N-Type & P-Type Doping",
            "content": """
<h4>1. Doping & Extrinsic Conduction</h4>
To control conductivity, precise trace quantities of impurity atoms (dopants, roughly 1 per $10^5$ to $10^8$ host atoms) are introduced into the host crystal lattice:
<ul>
  <li><strong>N-Type Semiconductors (Donor Doping):</strong> Group 14 elements (Si, Ge) are doped with pentavalent Group 15 impurities (Phosphorus, Arsenic, Antimony). Four valence electrons form covalent bonds with adjacent Si atoms; the fifth electron is loosely bound with small ionization energy ($E_d \\approx 0.045\\text{ eV}$ below $E_C$). At room temperature, essentially all donor atoms ionize:
  <div class="math-display">$$n \\approx N_D, \\quad p = \\frac{n_i^2}{N_D} \\ll n$$</div>
  Electrons are the <strong>majority carriers</strong>; holes are the <strong>minority carriers</strong>. The Fermi level shifts upwards toward the conduction band:
  <div class="math-display">$$E_F = E_C - k_B T \\ln\\left( \\frac{N_C}{N_D} \\right)$$</div></li>
  <li><strong>P-Type Semiconductors (Acceptor Doping):</strong> Doped with trivalent Group 13 impurities (Boron, Gallium, Indium). Three valence electrons form bonds, leaving an unfilled orbital that readily accepts an electron from an adjacent bond, creating a mobile hole with small acceptor ionization energy ($E_a \\approx 0.045\\text{ eV}$ above $E_V$). At room temperature:
  <div class="math-display">$$p \\approx N_A, \\quad n = \\frac{n_i^2}{N_A} \\ll p$$</div>
  Holes are the <strong>majority carriers</strong>; electrons are the <strong>minority carriers</strong>. The Fermi level shifts downward toward the valence band:
  <div class="math-display">$$E_F = E_V + k_B T \\ln\\left( \\frac{N_V}{N_A} \\right)$$</div></li>
</ul>

<h4>2. Total Conductivity & Temperature Regimes</h4>
The electrical conductivity $\\sigma$ of an extrinsic semiconductor is determined by carrier concentrations and mobilities $\\mu_n, \\mu_p$:
<div class="math-display">$$\\sigma = q (n \\mu_n + p \\mu_p)$$</div>
As temperature increases, extrinsic semiconductors exhibit three distinct regimes:
<ol>
  <li><strong>Freeze-out Regime ($T < 100\\text{ K}$):</strong> Thermal energy is insufficient to ionize all dopants; carrier concentration rises with $T$.</li>
  <li><strong>Extrinsic / Saturation Regime ($100\\text{ K} < T < 450\\text{ K}$):</strong> All dopants are ionized ($n \\approx N_D$), and carrier concentration is nearly constant. Conductivity decreases slightly due to acoustic phonon lattice scattering ($\mu \\propto T^{-3/2}$).</li>
  <li><strong>Intrinsic Regime ($T > 450\\text{ K}$):</strong> Thermal electron-hole generation across $E_g$ swamps dopant concentration ($n_i \\gg N_D$), causing exponential rise in conductivity and loss of semiconductor device functionality.</li>
</ol>
"""
        },
        {
            "id": "u1-sec3",
            "title": "Properties of the PN Junction & Shockley Diode Equation",
            "content": """
<h4>1. Formation of the Depletion Layer & Built-in Potential</h4>
When a P-type and an N-type semiconductor are joined metallurgically, a steep carrier gradient exists across the metallurgical junction. Electrons diffuse from the N-side into the P-side, and holes diffuse from the P-side into the N-side.
Near the metallurgical interface, recombining carriers leave behind uncompensated, fixed ionized dopant cores: positively charged donor ions ($N_D^+$) on the N-side, and negatively charged acceptor ions ($N_A^-$) on the P-side. This region devoid of free mobile carriers is termed the <strong>depletion layer</strong> (or space-charge region).
The resulting space-charge density $\\rho(x)$ sets up an internal electric field $\\vec{\\mathcal{E}}$ pointing from N to P that opposes further diffusion. In thermal equilibrium, the diffusion current is exactly balanced by the drift current:
<div class="math-display">$$J_{\\text{total}} = J_{\\text{drift}} + J_{\\text{diff}} = 0$$</div>
Integrating Poisson's equation $\\frac{d^2 V}{dx^2} = -\\frac{\\rho(x)}{\\varepsilon}$ across the junction yields the <strong>built-in contact potential barrier</strong> $V_{bi}$:
<div class="math-display">$$V_{bi} = \\frac{k_B T}{q} \\ln\\left( \\frac{N_A N_D}{n_i^2} \\right) = V_T \\ln\\left( \\frac{N_A N_D}{n_i^2} \\right)$$</div>
where $V_T = k_B T / q \\approx 25.86\\text{ mV}$ at $300\\text{ K}$ is the thermal voltage. For typical silicon PN junctions, $V_{bi} \\approx 0.65\\text{ V} - 0.85\\text{ V}$.

<h4>2. Depletion Width & Space-Charge Balance</h4>
By charge neutrality, the total negative charge per unit area on the P-side must equal the positive charge on the N-side: $q N_A x_p = q N_D x_n$. Under an applied external bias voltage $V$ (positive for forward bias, negative for reverse bias), the effective potential barrier is $V_{bi} - V$. The total depletion width $W = x_n + x_p$ is:
<div class="math-display">$$W = \\sqrt{ \\frac{2 \\varepsilon_s (V_{bi} - V)}{q} \\left( \\frac{1}{N_A} + \\frac{1}{N_D} \\right) }$$</div>
Under forward bias ($V > 0$), the barrier lowers to $V_{bi} - V$, shrinking $W$ and enabling massive majority carrier injection. Under reverse bias ($V < 0$), the barrier height increases to $V_{bi} + |V|$, widening the depletion region.

<h4>3. The Shockley Ideal Diode Equation</h4>
William Shockley (1949) derived the net terminal current by solving the minority carrier diffusion equations in the neutral regions under low-level injection:
<div class="math-display">$$I = I_s \\left( e^{\\frac{q V}{\\eta k_B T}} - 1 \\right) = I_s \\left( e^{\\frac{V}{\\eta V_T}} - 1 \\right)$$</div>
where $I_s$ is the reverse saturation current, given by:
<div class="math-display">$$I_s = q A \\left( \\frac{D_n n_{p0}}{L_n} + \\frac{D_p p_{n0}}{L_p} \\right) = q A n_i^2 \\left( \\frac{D_n}{L_n N_A} + \\frac{D_p}{L_p N_D} \\right)$$</div>
and $\\eta$ is the ideality factor ($\\eta \\approx 1$ for diffusion-dominated conduction, $\\eta \\approx 2$ when recombination in the depletion layer dominates at low currents).
The <strong>dynamic (AC) resistance</strong> of the forward-biased diode is:
<div class="math-display">$$r_d = \\frac{dV}{dI} = \\frac{\\eta V_T}{I + I_s} \\approx \\frac{\\eta V_T}{I}$$</div>
At room temperature with $\\eta = 1$ and $I = 1\\text{ mA}$, $r_d \\approx 26\\,\\Omega$.
"""
        },
        {
            "id": "u1-sec4",
            "title": "Half-Wave & Full-Wave Rectification Circuits",
            "content": """
<h4>1. Half-Wave Rectifier Circuit Analysis</h4>
A half-wave rectifier converts AC voltage $v_{\\text{in}}(t) = V_m \\sin(\\omega t)$ into pulsating unidirectional DC by utilizing a single diode in series with load resistor $R_L$.
During the positive half-cycle ($0 \\le \\omega t < \\pi$), the diode is forward-biased and conducts with forward diode resistance $r_f$:
<div class="math-display">$$i(t) = \\frac{V_m \\sin(\\omega t)}{r_f + R_L} = I_m \\sin(\\omega t), \\quad I_m = \\frac{V_m}{r_f + R_L}$$</div>
During the negative half-cycle ($\\pi \\le \\omega t < 2\\pi$), the diode is reverse-biased ($i(t) = 0$).
<ul>
  <li><strong>DC Output Current & Voltage:</strong>
  <div class="math-display">$$I_{dc} = \\frac{1}{2\\pi} \\int_0^\\pi I_m \\sin(\\omega t) d(\\omega t) = \\frac{I_m}{\\pi} \\approx 0.318 I_m, \\quad V_{dc} = I_{dc} R_L = \\frac{V_m}{\\pi}$$</div></li>
  <li><strong>RMS Output Current:</strong>
  <div class="math-display">$$I_{\\text{rms}} = \\sqrt{ \\frac{1}{2\\pi} \\int_0^\\pi I_m^2 \\sin^2(\\omega t) d(\\omega t) } = \\frac{I_m}{2} = 0.50 I_m$$</div></li>
  <li><strong>Rectification Efficiency $\\eta_{\\text{rec}}$:</strong>
  <div class="math-display">$$\\eta = \\frac{P_{dc}}{P_{ac}} = \\frac{I_{dc}^2 R_L}{I_{\\text{rms}}^2 (r_f + R_L)} = \\frac{(I_m/\\pi)^2 R_L}{(I_m/2)^2 (r_f + R_L)} = \\frac{4}{\\pi^2} \\frac{R_L}{r_f + R_L} \\le \\frac{4}{\\pi^2} \\approx 40.6\\%$$</div></li>
  <li><strong>Ripple Factor $r$:</strong> Measures AC fluctuation relative to DC:
  <div class="math-display">$$r = \\frac{I_{ac}}{I_{dc}} = \\sqrt{ \\left(\\frac{I_{\\text{rms}}}{I_{dc}}\\right)^2 - 1 } = \\sqrt{ \\left(\\frac{I_m/2}{I_m/\\pi}\\right)^2 - 1 } = \\sqrt{ \\frac{\\pi^2}{4} - 1 } \\approx 1.21$$</div></li>
  <li><strong>Peak Inverse Voltage (PIV):</strong> Maximum reverse voltage appearing across the diode during the negative half-cycle: $\\text{PIV} = V_m$.</li>
</ul>

<h4>2. Full-Wave Center-Tapped & Bridge Rectifiers</h4>
A full-wave rectifier conducts on both half-cycles. For a bridge rectifier using four diodes, two diodes conduct alternately during each half-cycle.
<ul>
  <li><strong>DC Output Current & Voltage:</strong>
  <div class="math-display">$$I_{dc} = \\frac{2 I_m}{\\pi} \\approx 0.637 I_m, \\quad V_{dc} = \\frac{2 V_m}{\\pi}$$</div></li>
  <li><strong>RMS Output Current:</strong>
  <div class="math-display">$$I_{\\text{rms}} = \\frac{I_m}{\\sqrt{2}} \\approx 0.707 I_m$$</div></li>
  <li><strong>Maximum Efficiency:</strong>
  <div class="math-display">$$\\eta = \\frac{I_{dc}^2 R_L}{I_{\\text{rms}}^2 (2r_f + R_L)} = \\frac{(2I_m/\\pi)^2}{(I_m/\\sqrt{2})^2} = \\frac{8}{\\pi^2} \\approx 81.2\\%$$</div></li>
  <li><strong>Ripple Factor:</strong>
  <div class="math-display">$$r = \\sqrt{ \\left(\\frac{I_{\\text{rms}}}{I_{dc}}\\right)^2 - 1 } = \\sqrt{ \\left(\\frac{I_m/\\sqrt{2}}{2I_m/\\pi}\\right)^2 - 1 } = \\sqrt{ \\frac{\\pi^2}{8} - 1 } \\approx 0.482$$</div></li>
  <li><strong>Peak Inverse Voltage (PIV):</strong>
    <ul>
      <li>Center-Tapped Full-Wave Rectifier: $\\text{PIV} = 2 V_m$.</li>
      <li>Bridge Rectifier: $\\text{PIV} = V_m$ (huge advantage for high-voltage power supplies).</li>
    </ul>
  </li>
  <li><strong>Fundamental Ripple Frequency:</strong> $f_{\\text{ripple}} = 2 f_{\\text{in}}$ ($100\\text{ Hz}$ or $120\\text{ Hz}$), making full-wave ripple substantially easier to filter than half-wave ($f_{\\text{ripple}} = f_{\\text{in}}$).</li>
</ul>
"""
        },
        {
            "id": "u1-sec5",
            "title": "Power Supply Smoothing Filters: C, L, LC & Pi-Sections",
            "content": """
<h4>1. Shunt Capacitor Filter</h4>
A capacitor of capacitance $C$ placed in parallel across the load resistor $R_L$ charges to the peak voltage $V_m$ when the rectifier conducts, and discharges slowly through $R_L$ during non-conducting intervals with time constant $\\tau = R_L C \\gg T/2$.
The peak-to-peak ripple voltage $V_{r(pp)}$ is given by:
<div class="math-display">$$V_{r(pp)} = \\frac{I_{dc}}{2 f C} = \\frac{V_{dc}}{2 f C R_L}$$</div>
where $f$ is the AC line frequency ($2f$ is the full-wave ripple frequency).
The DC output voltage is $V_{dc} = V_m - \\frac{V_{r(pp)}}{2} = V_m - \\frac{I_{dc}}{4 f C}$.
Approximating the triangular ripple waveform by its RMS value $V_{\\text{rms, ripple}} = \\frac{V_{r(pp)}}{2\\sqrt{3}}$, the <strong>ripple factor</strong> is:
<div class="math-display">$$r = \\frac{V_{\\text{rms, ripple}}}{V_{dc}} = \\frac{1}{4\\sqrt{3} f C R_L}$$</div>
Notice that for a capacitor filter, the ripple factor is inversely proportional to $R_L$: as load current increases ($R_L$ decreases), ripple worsens.

<h4>2. Series Inductor (Choke) Filter</h4>
An inductor of inductance $L$ placed in series with the load opposes changes in current through Faraday's back-EMF. By Fourier analysis of a full-wave rectified wave:
<div class="math-display">$$v(t) = \\frac{2V_m}{\\pi} - \\frac{4V_m}{3\\pi} \\cos(2\\omega t) - \\frac{4V_m}{15\\pi} \\cos(4\\omega t) - \\dots$$</div>
At the second harmonic ($2\\omega$), the impedance of the inductor is $2\\omega L$. For $2\\omega L \\gg R_L$:
<div class="math-display">$$r = \\frac{\\sqrt{2}}{3} \\frac{R_L}{2\\omega L} = \\frac{R_L}{3\\sqrt{2} \\omega L}$$</div>
Unlike the capacitor filter, the inductor filter ripple factor decreases as load current increases (smaller $R_L$), making it ideal for heavy current applications.

<h4>3. Choke-Input L-Section Filter (LC Filter)</h4>
Combining a series inductor $L$ and a shunt capacitor $C$: the inductor blocks AC harmonics while the capacitor shunts remaining AC to ground. For $2\\omega L \\gg \\frac{1}{2\\omega C}$:
<div class="math-display">$$r = \\frac{\\sqrt{2}}{3} \\frac{1}{(2\\omega)^2 L C} = \\frac{\\sqrt{2}}{12 \\omega^2 L C}$$</div>
<p><strong>Crucial Property:</strong> The ripple factor of an LC filter is <strong>completely independent of load resistance $R_L$</strong>, providing stable filtering across varying load currents, provided $L$ exceeds the critical inductance $L_c = \\frac{R_L}{3\\omega}$.</p>

<h4>4. Pi-Section (CLC) Filter</h4>
A $\\pi$-section filter consists of an input shunt capacitor $C_1$, a series choke $L$, and an output shunt capacitor $C_2$. It combines the high DC voltage of the capacitor filter with the superior ripple attenuation of the LC filter:
<div class="math-display">$$r = \\frac{\\sqrt{2}}{8 \\omega^3 C_1 C_2 L R_L}$$</div>
This provides an ultra-low ripple factor ($r < 0.001$) widely used in high-fidelity audio and communication power supplies.
"""
        },
        {
            "id": "u1-sec6",
            "title": "Zener Diode Breakdown & Shunt Voltage Regulation",
            "content": """
<h4>1. Breakdown Mechanisms in Reverse-Biased PN Junctions</h4>
When the reverse bias voltage across a PN junction exceeds a critical threshold, the reverse current increases dramatically. Two physical breakdown mechanisms occur:
<ul>
  <li><strong>Zener Breakdown (Quantum Tunneling):</strong> Occurs in heavily doped PN junctions ($N_A, N_D > 10^{18}\\text{ cm}^{-3}$) with very narrow depletion regions ($W < 10\\text{ nm}$). The intense electric field ($\\mathcal{E} > 10^6\\text{ V/cm}$) enables valence electrons to quantum tunnel directly into unoccupied conduction band states across the junction. Zener breakdown occurs at low voltages ($V_Z < 5.6\\text{ V}$) and has a <strong>negative temperature coefficient</strong> (breakdown voltage decreases as $T$ increases).</li>
  <li><strong>Avalanche Breakdown (Impact Ionization):</strong> Occurs in lightly doped PN junctions with wide depletion regions. The electric field accelerates thermally generated minority carriers to sufficient kinetic energy that they collide with lattice atoms, knocking valence electrons free in an impact ionization cascade. Avalanche breakdown occurs at higher voltages ($V_Z > 5.6\\text{ V}$) and has a <strong>positive temperature coefficient</strong>.</li>
</ul>

<h4>2. Zener Diode Shunt Voltage Regulator Circuit</h4>
A Zener diode operated in its reverse breakdown region maintains a nearly constant terminal voltage $V_Z$ across wide variations in input voltage $V_{\\text{in}}$ or load current $I_L$.
A current-limiting resistor $R_s$ is connected in series between the unregulated DC supply $V_{\\text{in}}$ and the parallel combination of the Zener diode and load resistor $R_L$:
<div class="math-display">$$I_s = \\frac{V_{\\text{in}} - V_Z}{R_s} = I_Z + I_L$$</div>
where $I_L = V_Z / R_L$.
<ul>
  <li><strong>Condition for Regulation:</strong> The Zener current must satisfy $I_{Z(\\text{min})} \\le I_Z \\le I_{Z(\\text{max})}$, where $I_{Z(\\text{min})}$ (knee current) ensures the diode remains in breakdown, and $I_{Z(\\text{max})} = P_{Z(\\text{max})} / V_Z$ prevents thermal destruction.</li>
  <li><strong>Design Formula for Series Resistor $R_s$:</strong>
  <div class="math-display">$$R_{s(\\text{max})} = \\frac{V_{\\text{in}(\\text{min})} - V_Z}{I_L(\\text{max}) + I_{Z(\\text{min})}}, \\quad R_{s(\\text{min})} = \\frac{V_{\\text{in}(\\text{max})} - V_Z}{I_L(\\text{min}) + I_{Z(\\text{max})}}$$</div></li>
  <li><strong>Line Regulation & Load Regulation:</strong> Line regulation measures output stability against input fluctuations $\\frac{\\Delta V_L}{\\Delta V_{\\text{in}}} = \\frac{r_z}{R_s + r_z}$, where $r_z$ is the dynamic Zener resistance. Load regulation measures output drop as load current increases: $\\frac{\\Delta V_L}{\\Delta I_L} = -(r_z \\parallel R_s) \\approx -r_z$.</li>
</ul>
"""
        }
    ],
    "problems": [
        {
            "id": "be-prob-1-1",
            "title": "Full-Wave Bridge Rectifier with Shunt Capacitor Filter Design",
            "statement": "A full-wave bridge rectifier is supplied by a secondary transformer winding providing $24\\text{ V}_{\\text{rms}}$ at $50\\text{ Hz}$. The rectifier feeds a load resistor $R_L = 200\\,\\Omega$. Diodes have forward voltage drop $V_D = 0.7\\text{ V}$. (a) Calculate the peak output voltage. (b) Determine the required filter capacitance $C$ to maintain the ripple factor below $r = 2.5\\%$. (c) Find the resulting DC load voltage $V_{dc}$.",
            "steps": [
                {
                    "step": "Step 1: Calculate Peak Secondary Voltage and Bridge Rectified Peak",
                    "math": "$$V_{s(m)} = \\sqrt{2} V_{\\text{rms}} = \\sqrt{2}(24\\text{ V}) \\approx 33.94\\text{ V}$$",
                    "explanation": "In a bridge rectifier, two diodes conduct simultaneously during each half-cycle, resulting in a total diode drop of $2 V_D = 1.4\\text{ V}$. The peak output voltage across the filter is $V_m = V_{s(m)} - 2 V_D = 33.94 - 1.4 = 32.54\\text{ V}$."
                },
                {
                    "step": "Step 2: Calculate Required Capacitance from Ripple Factor Formula",
                    "math": "$$r = \\frac{1}{4\\sqrt{3} f C R_L} \\implies C = \\frac{1}{4\\sqrt{3} f r R_L}$$",
                    "explanation": "Substituting $f = 50\\text{ Hz}$, $r = 0.025$, and $R_L = 200\\,\\Omega$: $C = \\frac{1}{4 \\sqrt{3} (50)(0.025)(200)} = \\frac{1}{1732.05} \\approx 5.77 \\times 10^{-4}\\text{ F} = 577 \\;\\mu\\text{F}$."
                },
                {
                    "step": "Step 3: Determine Resulting DC Load Voltage V_dc",
                    "math": "$$V_{dc} = \\frac{V_m}{1 + \\frac{1}{4 f C R_L}} = \\frac{32.54}{1 + \\frac{1}{4(50)(5.77 \\times 10^{-4})(200)}} = \\frac{32.54}{1 + 0.0433} \\approx 31.19\\text{ V}$$",
                    "explanation": "The DC output voltage is $31.19\\text{ V}$ with a peak-to-peak ripple of $V_{r(pp)} = 2\\sqrt{3} r V_{dc} \\approx 2(1.732)(0.025)(31.19) \\approx 2.70\\text{ V}$."
                }
            ],
            "answer": "(a) Vm = 32.54 V; (b) Required capacitance C = 577 μF; (c) DC output voltage Vdc = 31.19 V."
        },
        {
            "id": "be-prob-1-2",
            "title": "Zener Diode Shunt Voltage Regulator Design for Variable Load and Supply",
            "statement": "Design a Zener diode voltage regulator to supply a constant $V_L = 10.0\\text{ V}$ to a variable load drawing between $I_L = 5\\text{ mA}$ and $I_L = 40\\text{ mA}$. The input supply voltage fluctuates between $V_{\\text{in}} = 18\\text{ V}$ and $26\\text{ V}$. The Zener diode has $V_Z = 10.0\\text{ V}$, minimum knee current $I_{Z(\\text{min})} = 5\\text{ mA}$, and maximum power rating $P_{Z(\\text{max})} = 1.0\\text{ W}$. (a) Calculate the suitable value and power rating of series resistor $R_s$. (b) Verify that the Zener diode does not exceed its maximum power rating at minimum load.",
            "steps": [
                {
                    "step": "Step 1: Calculate Maximum Allowed Value of Rs for Worst-Case Minimum Input",
                    "math": "$$R_{s(\\text{max})} = \\frac{V_{\\text{in}(\\text{min})} - V_Z}{I_L(\\text{max}) + I_{Z(\\text{min})}} = \\frac{18\\text{ V} - 10\\text{ V}}{40\\text{ mA} + 5\\text{ mA}} = \\frac{8\\text{ V}}{45\\text{ mA}} \\approx 177.8\\,\\Omega$$",
                    "explanation": "To maintain regulation when $V_{\\text{in}}$ is minimum ($18\\text{ V}$) and load current is maximum ($40\\text{ mA}$), $R_s$ must be no larger than $177.8\\,\\Omega$. We choose standard commercial value $R_s = 150\\,\\Omega$."
                },
                {
                    "step": "Step 2: Check Maximum Zener Current Under Worst-Case Maximum Input",
                    "math": "$$I_{s(\\text{max})} = \\frac{V_{\\text{in}(\\text{max})} - V_Z}{R_s} = \\frac{26\\text{ V} - 10\\text{ V}}{150\\,\\Omega} = \\frac{16\\text{ V}}{150\\,\\Omega} \\approx 106.7\\text{ mA}$$",
                    "explanation": "At minimum load ($I_L(\\text{min}) = 5\\text{ mA}$), maximum Zener current is $I_{Z(\\text{max})} = I_{s(\\text{max})} - I_L(\\text{min}) = 106.7\\text{ mA} - 5\\text{ mA} = 101.7\\text{ mA}$."
                },
                {
                    "step": "Step 3: Calculate Power Dissipations in Zener Diode and Resistor Rs",
                    "math": "$$P_Z = V_Z I_{Z(\\text{max})} = (10.0\\text{ V})(101.7\\text{ mA}) = 1.017\\text{ W} \\approx 1.02\\text{ W}$$",
                    "explanation": "Since $1.02\\text{ W}$ slightly exceeds the $1.0\\text{ W}$ rating, we select $R_s = 160\\,\\Omega$. Then $I_{s(\\text{max})} = 16/160 = 100\\text{ mA}$, so $I_Z = 95\\text{ mA}$ and $P_Z = 0.95\\text{ W} < 1.0\\text{ W}$. The maximum power dissipated in $R_s$ is $P_{Rs} = I_{s(\\text{max})}^2 R_s = (0.10)^2(160) = 1.6\\text{ W}$ (select a $2\\text{ W}$ or $5\\text{ W}$ wire-wound resistor)."
                }
            ],
            "answer": "Series resistor Rs = 160 Ω (rated for at least 2 W); Maximum Zener power dissipation PZ = 0.95 W ≤ 1.0 W."
        },
        {
            "id": "be-prob-1-3",
            "title": "Dynamic AC Resistance and Diffusion Capacitance of a Forward-Biased Diode",
            "statement": "A silicon PN junction diode operates at room temperature ($T = 300\\text{ K}$) with ideality factor $\\eta = 1$ and minority carrier lifetime $\\tau_p = 50\\text{ ns}$. (a) Calculate the dynamic AC resistance $r_d$ at forward bias currents of $I_1 = 0.1\\text{ mA}$, $I_2 = 1.0\\text{ mA}$, and $I_3 = 10\\text{ mA}$. (b) Calculate the diffusion capacitance $C_d$ at $I = 10\\text{ mA}$.",
            "steps": [
                {
                    "step": "Step 1: Apply Dynamic Resistance Formula r_d = η V_T / I",
                    "math": "$$V_T = \\frac{k_B T}{q} \\approx 25.86\\text{ mV} \\implies r_d = \\frac{25.86\\text{ mV}}{I}$$",
                    "explanation": "Evaluating at each specified forward current: (1) At $0.1\\text{ mA}$: $r_d = 25.86 / 0.1 = 258.6\\,\\Omega$. (2) At $1.0\\text{ mA}$: $r_d = 25.86 / 1.0 = 25.86\\,\\Omega$. (3) At $10\\text{ mA}$: $r_d = 25.86 / 10 = 2.586\\,\\Omega$."
                },
                {
                    "step": "Step 2: Relate Diffusion Capacitance to Minority Carrier Lifetime and Current",
                    "math": "$$C_d = \\frac{\\tau_p I}{\\eta V_T} = \\frac{\\tau_p}{r_d}$$",
                    "explanation": "Diffusion capacitance arises from stored minority carrier charge in the neutral regions under forward bias: $Q = \\tau_p I$, so $C_d = dQ/dV = \\tau_p (dI/dV) = \\tau_p / r_d$."
                },
                {
                    "step": "Step 3: Calculate Numerical Value of C_d at 10 mA",
                    "math": "$$C_d = \\frac{50 \\times 10^{-9}\\text{ s}}{2.586\\,\\Omega} \\approx 1.933 \\times 10^{-8}\\text{ F} = 19.33\\text{ nF}$$",
                    "explanation": "Notice that diffusion capacitance $C_d$ scales linearly with forward current, becoming very large at high currents ($19.33\\text{ nF}$), which limits the high-frequency switching speed of forward-biased PN diodes."
                }
            ],
            "answer": "(a) rd = 258.6 Ω (at 0.1 mA), 25.86 Ω (at 1 mA), 2.59 Ω (at 10 mA); (b) Diffusion capacitance Cd = 19.33 nF at 10 mA."
        }
    ]
}

# Unit 2: Transistor Devices & Biasing Circuits (BJT, JFET & MOSFET)
u2 = {
    "unitNumber": 2,
    "number": 2,
    "title": "Transistors: BJT, JFET & MOSFET Biasing Circuits",
    "subtitle": "BJT Action, CB/CE/CC Configurations, DC/AC Load Lines, Bias Stability Factors, JFET Pinch-Off & MOSFET Characteristics",
    "description": "Comprehensive analysis of three-terminal semiconductor amplifiers: BJT structure and current relations, Common Emitter/Base/Collector characteristics, DC and AC load line analysis, Q-point stabilization and bias techniques (fixed, collector-feedback, and voltage divider with stability factor S derivation), JFET operation, Shockley drain current equation, and Depletion/Enhancement MOSFETs.",
    "topics": [
        "BJT Structure & Transistor Action Mechanism",
        "CB, CE & CC Configurations and Current Gains (α, β)",
        "DC and AC Load Line Analysis & Q-Point Selection",
        "Transistor Biasing Methods & Thermal Stability Factor (S)",
        "JFET Construction, Pinch-Off & Shockley's Equation",
        "Depletion & Enhancement MOSFETs (D-MOSFET, E-MOSFET)"
    ],
    "sections": [
        {
            "id": "u2-sec1",
            "title": "Bipolar Junction Transistors (BJT): Structure & Transistor Action",
            "content": """
<h4>1. Physical Structure of the Bipolar Junction Transistor</h4>
A <strong>bipolar junction transistor (BJT)</strong> consists of a single crystal of semiconductor with three alternating doped regions forming two back-to-back PN junctions:
<ul>
  <li><strong>Emitter ($E$):</strong> Heavily doped ($N_E \\gg 10^{19}\\text{ cm}^{-3}$) to inject a massive stream of majority carriers into the base. Moderate geometric physical width.</li>
  <li><strong>Base ($B$):</strong> Extremely narrow ($W_B \\ll L_n, L_p$, typically $< 1\\;\\mu\\text{m}$) and lightly doped ($N_B \\sim 10^{16}\\text{ cm}^{-3}$) to minimize electron-hole recombination so that nearly all injected carriers traverse it safely.</li>
  <li><strong>Collector ($C$):</strong> Moderately doped and physically largest in volume to dissipate heat generated by carrier collection under high reverse bias voltages.</li>
</ul>
Transistors are fabricated in two complementary polarity types: <strong>NPN</strong> (majority carriers electrons) and <strong>PNP</strong> (majority carriers holes).

<h4>2. The Transistor Action Mechanism (NPN in Active Mode)</h4>
To operate a BJT as a linear amplifier in the <strong>forward-active mode</strong>:
<ol>
  <li>The <strong>Base-Emitter (B-E) junction</strong> is <strong>forward-biased</strong> ($V_{BE} \\approx 0.7\\text{ V}$ for Silicon).</li>
  <li>The <strong>Collector-Base (C-B) junction</strong> is <strong>reverse-biased</strong> ($V_{CB} > 0$, typically $5\\text{ V} - 20\\text{ V}$).</li>
</ol>
Because the B-E junction is forward-biased, the heavily doped emitter injects a large flux of electrons into the base. Because the base is extremely thin ($W_B \\ll L_n$) and lightly doped, only a tiny fraction (typically $< 1\\%$) of electrons recombine with base holes, contributing to the tiny base current $I_B$.
The remaining $> 99\\%$ of electrons diffuse across the base to the edge of the reverse-biased collector-base space-charge layer, where the strong electric field sweeps them across into the collector, constituting the collector current $I_C$.

<h4>3. Terminal Current Relations</h4>
By Kirchhoff's Current Law:
<div class="math-display">$$I_E = I_B + I_C$$</div>
The fraction of emitter current collected is the <strong>common-base current gain $\\alpha$</strong>:
<div class="math-display">$$\\alpha = \\frac{I_C - I_{CBO}}{I_E} \\approx \\frac{I_C}{I_E}$$</div>
Typically, $\\alpha$ ranges between $0.98$ and $0.998$. Here $I_{CBO}$ is the tiny collector-to-base reverse leakage current with emitter open.
"""
        },
        {
            "id": "u2-sec2",
            "title": "Transistor Configurations: CB, CE, CC & Characteristics",
            "content": """
<h4>1. Common Base (CB) Configuration</h4>
The base terminal is common to both input (emitter-base) and output (collector-base) circuits.
<ul>
  <li><strong>Input Characteristics:</strong> Curve of $I_E$ vs. $V_{EB}$ at constant $V_{CB}$. Resembles a forward-biased diode. Dynamic input resistance is very low ($R_{\\text{in}} \\approx 20\\,\\Omega - 50\\,\\Omega$).</li>
  <li><strong>Output Characteristics:</strong> Curve of $I_C$ vs. $V_{CB}$ at constant $I_E$. In the active region, $I_C$ is nearly horizontal and independent of $V_{CB}$, yielding high output resistance ($R_{\\text{out}} \\approx 1\\text{ M}\\Omega$).</li>
  <li><strong>Current Gain:</strong> $\\alpha = \\Delta I_C / \\Delta I_E < 1$ (no current amplification; provides voltage and power gain).</li>
</ul>

<h4>2. Common Emitter (CE) Configuration (Most Widely Used)</h4>
The emitter terminal is grounded/common to both input (base-emitter) and output (collector-emitter) circuits.
<ul>
  <li><strong>Current Gain $\\beta$ (or $h_{fe}$):</strong>
  <div class="math-display">$$I_C = \\alpha I_E + I_{CBO} = \\alpha (I_B + I_C) + I_{CBO} \\implies I_C(1 - \\alpha) = \\alpha I_B + I_{CBO}$$</div>
  <div class="math-display">$$I_C = \\left( \\frac{\\alpha}{1 - \\alpha} \\right) I_B + \\left( \\frac{1}{1 - \\alpha} \\right) I_{CBO} = \\beta I_B + I_{CEO}$$</div>
  where the <strong>common-emitter current gain $\\beta$</strong> is:
  <div class="math-display">$$\\beta = \\frac{\\alpha}{1 - \\alpha}, \\quad \\alpha = \\frac{\\beta}{1 + \\beta}$$</div>
  Typically, $\\beta$ ranges from $50$ to $300$. The collector-to-emitter leakage current is $I_{CEO} = (1 + \\beta) I_{CBO}$.</li>
  <li><strong>Input Characteristics:</strong> $I_B$ vs. $V_{BE}$ for constant $V_{CE}$. Input resistance $R_{\\text{in}} \\approx 1\\text{ k}\\Omega - 2\\text{ k}\\Omega$.</li>
  <li><strong>Output Characteristics:</strong> $I_C$ vs. $V_{CE}$ for constant $I_B$. Shows three operating regions:
    <ol>
      <li><strong>Active Region:</strong> B-E forward-biased, C-B reverse-biased ($V_{CE} > 0.3\\text{ V}$). Curves have a slight upward slope due to <em>base-width modulation (Early effect)</em>. Ideal for linear amplification.</li>
      <li><strong>Saturation Region:</strong> Both B-E and C-B forward-biased ($V_{CE} < V_{CE(\\text{sat})} \\approx 0.2\\text{ V}$). Transistor acts as an ON switch with negligible voltage drop.</li>
      <li><strong>Cutoff Region:</strong> Both B-E and C-B reverse-biased ($I_B = 0, I_C = I_{CEO} \\approx 0$). Transistor acts as an OFF switch.</li>
    </ol>
  </li>
</ul>

<h4>3. Common Collector (CC) Configuration (Emitter Follower)</h4>
Collector is AC ground. Input applied to base, output extracted from emitter.
<div class="math-display">$$\\gamma = \\frac{I_E}{I_B} = 1 + \\beta$$</div>
Features <strong>very high input impedance</strong> ($R_{\\text{in}} > 100\\text{ k}\\Omega$), <strong>very low output impedance</strong> ($R_{\\text{out}} < 50\\,\\Omega$), and near-unity voltage gain ($A_v \\approx 1$). Used ubiquitously for impedance matching and output buffer stages.
"""
        },
        {
            "id": "u2-sec3",
            "title": "DC and AC Load Line Analysis & Q-Point Selection",
            "content": """
<h4>1. The DC Load Line</h4>
Consider a Common Emitter circuit with collector supply voltage $V_{CC}$ and collector load resistor $R_C$. Applying Kirchhoff's Voltage Law to the output loop:
<div class="math-display">$$V_{CC} = V_{CE} + I_C R_C \\implies I_C = -\\frac{1}{R_C} V_{CE} + \\frac{V_{CC}}{R_C}$$</div>
This is the equation of a straight line on the $I_C - V_{CE}$ output characteristic plane, termed the <strong>DC Load Line</strong>:
<ul>
  <li><strong>Cutoff Point (X-axis intercept):</strong> Set $I_C = 0 \\implies V_{CE} = V_{CC}$.</li>
  <li><strong>Saturation Point (Y-axis intercept):</strong> Set $V_{CE} = 0 \\implies I_C = \\frac{V_{CC}}{R_C}$.</li>
  <li><strong>Slope:</strong> $-\\frac{1}{R_C}$.</li>
</ul>

<h4>2. The Quiescent Operating Point (Q-Point)</h4>
The intersection of the DC load line with the transistor output characteristic corresponding to the base bias current $I_B$ establishes the <strong>quiescent operating point (Q-point)</strong> $(V_{CEQ}, I_{CQ})$.
For maximum symmetrical undistorted output voltage swing (Class A operation), the Q-point should be positioned precisely at the <strong>midpoint of the DC load line</strong>:
<div class="math-display">$$V_{CEQ} = \\frac{V_{CC}}{2}, \\quad I_{CQ} = \\frac{V_{CC}}{2 R_C}$$</div>

<h4>3. The AC Load Line</h4>
When an external load $R_L$ is capacitively coupled to the collector, the effective AC load resistance seen by the collector signal is $r_c = R_C \\parallel R_L$.
Because $r_c < R_C$, the <strong>AC load line</strong> passes through the same DC Q-point $(V_{CEQ}, I_{CQ})$ but has a steeper slope $-\\frac{1}{r_c}$:
<div class="math-display">$$i_c = -\\frac{1}{r_c} v_{ce} \\implies I_C - I_{CQ} = -\\frac{1}{R_C \\parallel R_L} (V_{CE} - V_{CEQ})$$</div>
The maximum peak-to-peak undistorted output voltage swing is limited by the distance to cutoff or saturation along the AC load line:
<div class="math-display">$$V_{o(\\text{p-p, max})} = 2 \\min\\left( V_{CEQ}, I_{CQ} r_c \\right)$$</div>
"""
        },
        {
            "id": "u2-sec4",
            "title": "Transistor Biasing Methods & Thermal Stability Factor (S)",
            "content": """
<h4>1. Need for Biasing & Thermal Runaway</h4>
The Q-point coordinates $(I_C, V_{CE})$ are temperature-sensitive due to three factors:
<ol>
  <li>Reverse saturation current $I_{CBO}$ doubles approximately every $10^\\circ\\text{C}$ rise in temperature.</li>
  <li>Base-emitter voltage $V_{BE}$ decreases at a rate of approximately $-2.5\\text{ mV}/^\\circ\\text{C}$.</li>
  <li>Current gain $\\beta$ increases with temperature.</li>
</ol>
Without proper stabilization, an increase in temperature causes $I_C$ to rise, increasing collector power dissipation $P_C = V_{CE} I_C$. This heats the junction further, causing a catastrophic regenerative positive feedback loop known as <strong>thermal runaway</strong>.

<h4>2. Definition of Stability Factor $S$</h4>
The <strong>stability factor $S$</strong> is defined as the rate of change of collector current with respect to leakage current $I_{CBO}$:
<div class="math-display">$$S = \\frac{\\partial I_C}{\\partial I_{CBO}}$$</div>
An ideal bias circuit has $S \\to 1$ (complete thermal immunity). Higher values ($S \\gg 1$) indicate severe instability.

<h4>3. Comparative Analysis of Biasing Topologies</h4>
<ul>
  <li><strong>Fixed Base Resistor Bias:</strong> A single resistor $R_B$ connects from $V_{CC}$ to the base:
  <div class="math-display">$$I_B = \\frac{V_{CC} - V_{BE}}{R_B} \\approx \\text{const} \\implies S = 1 + \\beta$$</div>
  For $\\beta = 100$, $S = 101$. Extremely unstable; completely unsuitable for linear amplifiers.</li>
  <li><strong>Collector Feedback Bias:</strong> $R_B$ is connected directly from the collector to the base:
  <div class="math-display">$$S = \\frac{1 + \\beta}{1 + \\beta \\frac{R_C}{R_C + R_B}}$$</div>
  Provides negative feedback: if $I_C$ rises, $V_C = V_{CC} - I_C R_C$ drops, reducing $I_B$ and checking the rise. Moderate stability.</li>
  <li><strong>Voltage Divider Bias (Universal Bias):</strong> Two resistors $R_1, R_2$ form a potential divider across $V_{CC}$, combined with an emitter degeneration resistor $R_E$:
  <div class="math-display">$$V_{\\text{th}} = V_{CC} \\frac{R_2}{R_1 + R_2}, \\quad R_{\\text{th}} = R_1 \\parallel R_2 = \\frac{R_1 R_2}{R_1 + R_2}$$</div>
  The input loop equation is $V_{\\text{th}} = I_B R_{\\text{th}} + V_{BE} + I_E R_E$.
  Differentiating delivers the stability factor:
  <div class="math-display">$$S = \\frac{1 + \\beta}{1 + \\beta \\left( \\frac{R_E}{R_{\\text{th}} + R_E} \\right)}$$</div>
  By designing $R_{\\text{th}} \\ll \\beta R_E$ (rule of thumb: $R_{\\text{th}} \\le 0.1 \\beta R_E$ or $R_2 \\le 0.1 \\beta R_E$), the fraction approaches 1:
  <div class="math-display">$$S \\approx \\frac{1 + \\beta}{1 + \\beta} = 1$$</div>
  The Q-point becomes virtually independent of transistor $\\beta$ and temperature variations.</li>
</ul>
"""
        },
        {
            "id": "u2-sec5",
            "title": "Field Effect Transistors: JFET & MOSFET Characteristics",
            "content": """
<h4>1. Junction Field Effect Transistor (JFET)</h4>
The JFET is a unipolar three-terminal device where conduction is governed entirely by majority carriers through a semiconductor channel controlled by an electric field:
<ul>
  <li><strong>Construction:</strong> An N-channel JFET consists of a lightly doped n-type silicon bar with Ohmic contacts at both ends designated <strong>Drain ($D$)</strong> and <strong>Source ($S$)</strong>. Two heavily doped $p^+$ regions diffused on opposite sides are connected to form the <strong>Gate ($G$)</strong>.</li>
  <li><strong>Pinch-Off Voltage $V_P$:</strong> Operating with reverse-biased gate-source junction ($V_{GS} \\le 0$). Reverse bias widens the depletion regions into the channel. At a critical drain-source voltage $V_{DS} = V_{DS(\\text{sat})} = V_{GS} - V_P$, the two depletion boundaries touch at the drain end, a condition termed <strong>pinch-off</strong>. Beyond pinch-off, the drain current saturates at an almost constant level.</li>
  <li><strong>Shockley's Drain Current Equation:</strong> In the saturation/active region ($V_{DS} \\ge V_{GS} - V_P$):
  <div class="math-display">$$I_D = I_{DSS} \\left( 1 - \\frac{V_{GS}}{V_P} \\right)^2$$</div>
  where $I_{DSS}$ is the maximum saturation drain current at $V_{GS} = 0$.</li>
  <li><strong>Transconductance $g_m$:</strong>
  <div class="math-display">$$g_m = \\frac{\\partial I_D}{\\partial V_{GS}} = \\frac{2 I_{DSS}}{|V_P|} \\left( 1 - \\frac{V_{GS}}{V_P} \\right) = g_{m0} \\left( 1 - \\frac{V_{GS}}{V_P} \\right)$$</div></li>
</ul>

<h4>2. Metal-Oxide-Semiconductor FETs (MOSFETs)</h4>
The gate electrode is physically insulated from the channel by an ultra-thin dielectric layer of Silicon Dioxide ($\\text{SiO}_2$), resulting in an astronomical input impedance ($R_{\\text{in}} > 10^{12}\\,\\Omega$):
<ul>
  <li><strong>Depletion-Type MOSFET (D-MOSFET):</strong> Fabricated with a physical channel. Can operate in either <em>depletion mode</em> (negative $V_{GS}$ repels channel electrons) or <em>enhancement mode</em> (positive $V_{GS}$ attracts additional electrons, boosting $I_D$ above $I_{DSS}$). Follows Shockley's square-law equation for both positive and negative $V_{GS}$.</li>
  <li><strong>Enhancement-Type MOSFET (E-MOSFET):</strong> The cornerstone of modern VLSI and microprocessor technology (CMOS). Has no physical channel at zero bias ($I_D = 0$ at $V_{GS} = 0$). When $V_{GS}$ exceeds the positive <strong>threshold voltage $V_{th}$</strong>, an inversion layer forms at the $\\text{Si}-\\text{SiO}_2$ interface, creating an n-channel. In saturation ($V_{DS} \\ge V_{GS} - V_{th}$):
  <div class="math-display">$$I_D = k_n (V_{GS} - V_{th})^2 = \\frac{1}{2} \\mu_n C_{ox} \\left( \\frac{W}{L} \\right) (V_{GS} - V_{th})^2$$</div>
  where $C_{ox} = \\varepsilon_{ox}/t_{ox}$ is the gate oxide capacitance per unit area, and $W/L$ is the transistor aspect ratio.</li>
</ul>
"""
        }
    ],
    "problems": [
        {
            "id": "be-prob-2-1",
            "title": "Voltage Divider Biasing Circuit Design for Stable Q-Point",
            "statement": "Design a voltage divider bias circuit for an NPN silicon transistor operating from a single supply $V_{CC} = 15.0\\text{ V}$ to establish the quiescent operating point at $V_{CEQ} = 7.5\\text{ V}$ and $I_{CQ} = 2.0\\text{ mA}$. The transistor has $\\beta = 100$ and $V_{BE} = 0.7\\text{ V}$. Allocate $1.5\\text{ V}$ across the emitter resistor $R_E$ for thermal stability, and ensure the divider bleeder current is $10$ times the base current ($I_{\\text{div}} = 10 I_B$). Find resistors $R_E$, $R_C$, $R_1$, and $R_2$.",
            "steps": [
                {
                    "step": "Step 1: Calculate Emitter Resistor RE and Collector Resistor RC",
                    "math": "$$I_E \\approx I_C = 2.0\\text{ mA} \\implies R_E = \\frac{V_E}{I_E} = \\frac{1.5\\text{ V}}{2.0\\text{ mA}} = 750\\,\\Omega$$",
                    "explanation": "Applying KVL to the collector-emitter loop: $V_{CC} = I_C R_C + V_{CEQ} + V_E$. Substituting values: $15.0 = (2.0\\text{ mA}) R_C + 7.5 + 1.5 \\implies (2.0\\text{ mA}) R_C = 6.0\\text{ V} \\implies R_C = \\frac{6.0\\text{ V}}{2.0\\text{ mA}} = 3.0\\text{ k}\\Omega$."
                },
                {
                    "step": "Step 2: Calculate Base Voltage VB and Base Current IB",
                    "math": "$$V_B = V_E + V_{BE} = 1.5\\text{ V} + 0.7\\text{ V} = 2.2\\text{ V}, \\quad I_B = \\frac{I_C}{\\beta} = \\frac{2.0\\text{ mA}}{100} = 20\\;\\mu\\text{A}$$",
                    "explanation": "The required base potential is $2.2\\text{ V}$, and the base current is $20\\;\\mu\\text{A}$."
                },
                {
                    "step": "Step 3: Size the Voltage Divider Resistors R1 and R2",
                    "math": "$$I_2 = 10 I_B = 10(20\\;\\mu\\text{A}) = 200\\;\\mu\\text{A} \\implies R_2 = \\frac{V_B}{I_2} = \\frac{2.2\\text{ V}}{0.20\\text{ mA}} = 11.0\\text{ k}\\Omega$$",
                    "explanation": "Current through $R_1$ is $I_1 = I_2 + I_B = 200\\;\\mu\\text{A} + 20\\;\\mu\\text{A} = 220\\;\\mu\\text{A}$. Thus $R_1 = \\frac{V_{CC} - V_B}{I_1} = \\frac{15.0\\text{ V} - 2.2\\text{ V}}{0.22\\text{ mA}} = \\frac{12.8\\text{ V}}{0.22\\text{ mA}} \\approx 58.18\\text{ k}\\Omega$ (standard commercial values: $R_1 = 56\\text{ k}\\Omega$, $R_2 = 11\\text{ k}\\Omega$)."
                }
            ],
            "answer": "RE = 750 Ω; RC = 3.0 kΩ; R1 ≈ 58.2 kΩ (use 56 kΩ); R2 = 11.0 kΩ."
        },
        {
            "id": "be-prob-2-2",
            "title": "Thermal Stability Factor S Comparison: Fixed Bias vs. Voltage Divider Bias",
            "statement": "A silicon transistor with $\\beta = 120$ is used in two different biasing configurations: (a) Fixed base resistor bias with $R_B = 470\\text{ k}\\Omega$ and $R_C = 2.2\\text{ k}\\Omega$. (b) Voltage divider bias with $R_1 = 39\\text{ k}\\Omega$, $R_2 = 8.2\\text{ k}\\Omega$, $R_C = 2.2\\text{ k}\\Omega$, and $R_E = 1.0\\text{ k}\\Omega$. Calculate the stability factor $S = \\partial I_C / \\partial I_{CBO}$ for both circuits and comment on their thermal stability.",
            "steps": [
                {
                    "step": "Step 1: Calculate Stability Factor for Fixed Base Bias",
                    "math": "$$S_{\\text{fixed}} = 1 + \\beta = 1 + 120 = 121$$",
                    "explanation": "In fixed bias, any change in leakage current $\\Delta I_{CBO}$ is amplified by a factor of 121 directly in the collector current, causing severe temperature vulnerability."
                },
                {
                    "step": "Step 2: Calculate Thevenin Equivalent Resistance for Voltage Divider Bias",
                    "math": "$$R_{\\text{th}} = R_1 \\parallel R_2 = \\frac{(39\\text{ k}\\Omega)(8.2\\text{ k}\\Omega)}{39\\text{ k}\\Omega + 8.2\\text{ k}\\Omega} = \\frac{319.8}{47.2} \\approx 6.775\\text{ k}\\Omega$$",
                    "explanation": "The Thevenin base resistance is $6.775\\text{ k}\\Omega$."
                },
                {
                    "step": "Step 3: Evaluate Stability Factor for Voltage Divider Bias",
                    "math": "$$S_{\\text{div}} = \\frac{1 + \\beta}{1 + \\beta \\left( \\frac{R_E}{R_{\\text{th}} + R_E} \\right)} = \\frac{1 + 120}{1 + 120 \\left( \\frac{1.0}{6.775 + 1.0} \\right)} = \\frac{121}{1 + 120 \\left( \\frac{1.0}{7.775} \\right)} = \\frac{121}{1 + 15.434} = \\frac{121}{16.434} \\approx 7.36$$",
                    "explanation": "Voltage divider bias reduces the stability factor from $121$ down to $7.36$, providing a $16.4\\times$ improvement in thermal stability and completely preventing thermal runaway."
                }
            ],
            "answer": "Fixed bias: S = 121 (severely unstable); Voltage divider bias: S = 7.36 (highly stable, 16.4x better thermal immunity)."
        },
        {
            "id": "be-prob-2-3",
            "title": "JFET Self-Bias Circuit Analysis via Shockley's Equation",
            "statement": "An N-channel JFET with parameters $I_{DSS} = 12\\text{ mA}$ and pinch-off voltage $V_P = -4.0\\text{ V}$ is biased using a self-bias circuit with supply voltage $V_{DD} = 18.0\\text{ V}$, drain resistor $R_D = 1.2\\text{ k}\\Omega$, and source resistor $R_S = 330\\,\\Omega$. The gate resistor is $R_G = 1.0\\text{ M}\\Omega$. (a) Calculate the quiescent operating point $(I_{DQ}, V_{GSQ}, V_{DSQ})$. (b) Determine the transconductance $g_m$ at the Q-point.",
            "steps": [
                {
                    "step": "Step 1: Set Up the Self-Bias Line Equation",
                    "math": "$$V_{GS} = -I_D R_S = -(330\\,\\Omega) I_D$$",
                    "explanation": "Since gate current is zero ($I_G = 0$), $V_G = 0$, so $V_{GS} = V_G - V_S = -I_D R_S$."
                },
                {
                    "step": "Step 2: Solve Non-Linear Quadratic Equation for Drain Current",
                    "math": "$$I_D = I_{DSS} \\left( 1 - \\frac{V_{GS}}{V_P} \\right)^2 = 12 \\left( 1 - \\frac{-0.330 I_D}{-4.0} \\right)^2 = 12 \\left( 1 - 0.0825 I_D \\right)^2$$",
                    "explanation": "Expanding: $I_D = 12(1 - 0.165 I_D + 0.006806 I_D^2) = 12 - 1.98 I_D + 0.08167 I_D^2$. Rearranging into standard quadratic form: $0.08167 I_D^2 - 2.98 I_D + 12 = 0$. Solving roots: $I_D = \\frac{2.98 \\pm \\sqrt{(2.98)^2 - 4(0.08167)(12)}}{2(0.08167)} = \\frac{2.98 \\pm 2.227}{0.1633}$. The physical root ($I_D < I_{DSS}$) is $I_{DQ} = \\frac{0.753}{0.1633} \\approx 4.61\\text{ mA}$."
                },
                {
                    "step": "Step 3: Calculate V_GSQ, V_DSQ and Transconductance g_m",
                    "math": "$$V_{GSQ} = -(4.61\\text{ mA})(330\\,\\Omega) = -1.52\\text{ V}, \\quad V_{DSQ} = V_{DD} - I_{DQ}(R_D + R_S) = 18 - 4.61(1.2 + 0.33) = 10.95\\text{ V}$$",
                    "explanation": "Transconductance is $g_m = \\frac{2 I_{DSS}}{|V_P|} \\left( 1 - \\frac{V_{GSQ}}{V_P} \\right) = \\frac{2(12\\text{ mA})}{4.0\\text{ V}} \\left( 1 - \\frac{-1.52}{-4.0} \\right) = 6.0\\text{ mS} (1 - 0.38) = 3.72\\text{ mS}$ (or $3.72\\text{ mA/V}$)."
                }
            ],
            "answer": "Q-point: IDQ = 4.61 mA, VGSQ = -1.52 V, VDSQ = 10.95 V; Transconductance gm = 3.72 mS."
        }
    ]
}

with open("be_u1.json", "w", encoding="utf-8") as f:
    json.dump(u1, f, indent=2)

with open("be_u2.json", "w", encoding="utf-8") as f:
    json.dump(u2, f, indent=2)

print("be_u1.json and be_u2.json generated successfully!")
