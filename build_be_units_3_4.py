import json

unit3 = {
    "id": "unit-3",
    "number": 3,
    "title": "Power Electronics: Thyristors, UJT & Phase Control",
    "description": "Comprehensive treatment of power semiconductor devices: the four-layer pnpn Silicon Controlled Rectifier (SCR) and its two-transistor regenerative latching model; Unijunction Transistors (UJT) and negative-resistance relaxation oscillators; bidirectional Triac and Diac switches in AC phase control systems; complete mathematical derivations and solved university exam problems.",
    "sections": [
        {
            "id": "u3-sec1",
            "title": "Silicon Controlled Rectifier (SCR): Structure & Two-Transistor Analogy",
            "content": """<h4>1. Physical Architecture and Operating Regimes</h4>
<p>The Silicon Controlled Rectifier (SCR) is a four-layer, three-junction ($p_1-n_1-p_2-n_2$) unidirectional semiconductor switching device with three terminals: <strong>Anode (A)</strong>, <strong>Cathode (K)</strong>, and <strong>Gate (G)</strong>. The outer layers are heavily doped $p_1$ (anode) and $n_2$ (cathode), while the inner $n_1$ and $p_2$ layers are moderately/lightly doped.</p>
<p>When an SCR is connected with an external anode-to-cathode voltage $V_{AK}$:
<ul>
<li><strong>Reverse Blocking State ($V_{AK} < 0$):</strong> Junctions $J_1$ and $J_3$ are reverse-biased, while $J_2$ is forward-biased. Only a minuscule reverse leakage current flows until the reverse breakdown voltage $V_{BR}$ is reached, at which point avalanche breakdown occurs.</li>
<li><strong>Forward Blocking State ($V_{AK} > 0$, $I_G = 0$):</strong> Outer junctions $J_1$ and $J_3$ are forward-biased, but central junction $J_2$ is reverse-biased, creating a wide depletion layer. The device supports high forward voltage with only a tiny forward leakage current flowing until the forward breakover voltage $V_{BO}$ is exceeded.</li>
<li><strong>Forward Conduction State ($V_{AK} > 0$, $I_G > I_{GT}$):</strong> Injection of a gate trigger pulse causes instantaneous regenerative switching (turn-on). Junction $J_2$ collapses, and the SCR drops into a low-impedance forward conduction state with a forward voltage drop of only $V_F \approx 1.0\\text{ to }1.5\\,\\text{V}$.</li>
</ul>
</p>

<h4>2. Mathematical Derivation of Two-Transistor Regenerative Analogy</h4>
<p>To mathematically understand regenerative latching, consider splitting the four-layer $p_1-n_1-p_2-n_2$ structure into two interconnected bipolar transistors: a PNP transistor $Q_1$ ($p_1-n_1-p_2$) and an NPN transistor $Q_2$ ($n_1-p_2-n_2$).</p>
<p>The collector of $Q_1$ feeds the base of $Q_2$, and the collector of $Q_2$ feeds the base of $Q_1$. Let $\\alpha_1$ and $\\alpha_2$ denote the common-base current gains of $Q_1$ and $Q_2$ respectively, and let $I_{CO1}, I_{CO2}$ be their reverse saturation currents.</p>
<div class="math-display">
$$I_{C1} = \\alpha_1 I_A + I_{CO1}$$
</div>
<div class="math-display">
$$I_{C2} = \\alpha_2 I_K + I_{CO2}$$
</div>
<p>Applying Kirchhoff's Current Law at the cathode: $I_K = I_A + I_G$. The total current crossing central junction $J_2$ is the sum of collector currents and reverse leakage:</p>
<div class="math-display">
$$I_A = I_{C1} + I_{C2} = \\alpha_1 I_A + I_{CO1} + \\alpha_2 (I_A + I_G) + I_{CO2}$$
</div>
<p>Collecting terms in $I_A$:</p>
<div class="math-display">
$$I_A (1 - (\\alpha_1 + \\alpha_2)) = \\alpha_2 I_G + (I_{CO1} + I_{CO2})$$
</div>
<div class="math-display">
$$I_A = \\frac{\\alpha_2 I_G + I_{CO1} + I_{CO2}}{1 - (\\alpha_1 + \\alpha_2)}$$
</div>
<p><strong>Latching Condition:</strong> At very low current levels, transistor gains $\\alpha_1$ and $\\alpha_2$ are very small ($\ll 0.5$), so $(\\alpha_1 + \\alpha_2) \\ll 1$, keeping $I_A$ negligible (off-state). However, when gate current $I_G$ is injected into the base of $Q_2$, $I_A$ increases, causing emitter currents to rise. Because transistor $\\alpha$ increases nonlinearly with emitter current, the loop gain sum reaches unity:</p>
<div class="math-display">
$$\\alpha_1 + \\alpha_2 \\to 1 \\implies [1 - (\\alpha_1 + \\alpha_2)] \\to 0 \\implies I_A \\to \\infty \\quad \\text{(limited only by external load } R_L\\text{)}$$
</div>
<p>Once $\\alpha_1 + \\alpha_2 = 1$, the internal regenerative loop feeds itself: $Q_1$ drives $Q_2$, which in turn drives $Q_1$. At this stage, the external gate signal $I_G$ loses control and can be safely removed; the device remains latched in the ON state.</p>

<h4>3. Latching Current ($I_L$) vs. Holding Current ($I_H$)</h4>
<ul>
<li><strong>Latching Current ($I_L$):</strong> The minimum anode current that must be attained immediately after gate triggering for the SCR to sustain conduction when the gate trigger pulse is terminated. If $I_A < I_L$ when $I_G$ ceases, the SCR falls back into the forward blocking state.</li>
<li><strong>Holding Current ($I_H$):</strong> The minimum anode current below which the SCR automatically turns OFF (re-enters the forward blocking mode) during commutation. If an external circuit reduces $I_A$ below $I_H$, the regenerative loop collapses.</li>
<li><strong>Crucial Relationship:</strong> For all thyristors, $I_L > I_H$, typically $I_L \\approx 2\\text{ to }3 \\times I_H$.</li>
</ul>"""
        },
        {
            "id": "u3-sec2",
            "title": "SCR Turn-On Mechanisms, Firing Angles & Phase-Controlled Rectification",
            "content": """<h4>1. Firing Angle $\\alpha$ and Conduction Angle $\\gamma$</h4>
<p>In AC power circuits, the point on the sinusoidal voltage waveform at which the SCR is triggered into conduction is quantified by the <strong>firing angle (or delay angle) $\\alpha$</strong> measured in electrical degrees or radians from the zero-crossing of the positive half-cycle ($0 \\le \\alpha \\le \\pi$).</p>
<p>The <strong>conduction angle $\\gamma$</strong> represents the duration over which the SCR conducts before natural line commutation turns it off:</p>
<div class="math-display">
$$\\gamma = \\pi - \\alpha$$
</div>

<h4>2. Half-Wave Phase-Controlled Rectifier with Resistive Load</h4>
<p>Consider an AC source $v_s(t) = V_m \\sin(\\omega t)$ connected to an SCR in series with a resistive load $R$. During the negative half-cycle ($\pi \\le \\omega t \\le 2\\pi$), the SCR is reverse-biased and $v_o(t) = 0$. During the positive half-cycle, conduction begins only when triggered at $\\omega t = \\alpha$ and extinguishes naturally at $\\omega t = \\pi$.</p>
<p>The average (DC) load voltage is derived via definite integration:</p>
<div class="math-display">
$$V_{dc} = \\frac{1}{2\\pi} \\int_{\\alpha}^{\\pi} V_m \\sin(\\omega t)\\, d(\\omega t) = \\frac{V_m}{2\\pi} \\left[ -\\cos(\\omega t) \\right]_{\\alpha}^{\\pi}$$
</div>
<div class="math-display">
$$V_{dc} = \\frac{V_m}{2\\pi} [ -(-1) - (-\\cos\\alpha) ] = \\frac{V_m}{2\\pi} (1 + \\cos\\alpha)$$
</div>
<p>The RMS load voltage is calculated by evaluating the root-mean-square integral:</p>
<div class="math-display">
$$V_{rms} = \\sqrt{ \\frac{1}{2\\pi} \\int_{\\alpha}^{\\pi} V_m^2 \\sin^2(\\omega t)\\, d(\\omega t) } = \\frac{V_m}{\\sqrt{2\\pi}} \\sqrt{ \\int_{\\alpha}^{\\pi} \\frac{1 - \\cos(2\\omega t)}{2}\\, d(\\omega t) }$$
</div>
<div class="math-display">
$$V_{rms} = \\frac{V_m}{2\\sqrt{\\pi}} \\sqrt{ (\\pi - \\alpha) + \\frac{1}{2} \\sin(2\\alpha) }$$
</div>

<h4>3. Full-Wave Mid-Point & Bridge Phase-Controlled Rectifier</h4>
<p>For a full-wave controlled bridge rectifier where SCR pairs are fired symmetrically at $\\alpha$ and $\\pi + \\alpha$:</p>
<div class="math-display">
$$V_{dc} = \\frac{1}{\\pi} \\int_{\\alpha}^{\\pi} V_m \\sin(\\omega t)\\, d(\\omega t) = \\frac{V_m}{\\pi} (1 + \\cos\\alpha)$$
</div>
<div class="math-display">
$$V_{rms} = \\frac{V_m}{\\sqrt{2}} \\sqrt{ 1 - \\frac{\\alpha}{\\pi} + \\frac{\\sin(2\\alpha)}{2\\pi} }$$
</div>
<p>When $\\alpha = 0$, $V_{dc} = \\frac{2V_m}{\\pi}$, which corresponds exactly to an uncontrolled full-wave diode rectifier. By modulating $\\alpha$ continuously from $0$ to $\\pi$, $V_{dc}$ smoothly varies from $\\frac{2V_m}{\\pi}$ down to $0\\,\\text{V}$, providing continuous DC motor speed and heating control.</p>"""
        },
        {
            "id": "u3-sec3",
            "title": "Unijunction Transistor (UJT): Intrinsic Standoff Ratio & Relaxation Oscillator",
            "content": """<h4>1. Architecture and Equivalent Circuit of UJT</h4>
<p>The Unijunction Transistor (UJT) is a three-terminal single-junction device consisting of a lightly doped $N$-type silicon bar with ohmic contacts at both ends, denoted as <strong>Base-1 ($B_1$)</strong> and <strong>Base-2 ($B_2$)</strong>. Near $B_2$, a heavily doped $P$-type emitter region is alloyed, forming a single $P-N$ junction with the bar.</p>
<p>The total resistance of the silicon bar between $B_1$ and $B_2$ when the emitter is open-circuited is the <strong>interbase resistance $R_{BB}$</strong>:</p>
<div class="math-display">
$$R_{BB} = R_{B1} + R_{B2} \\quad (\\text{typically } 4\\,\\text{k}\\Omega \\text{ to } 10\\,\\text{k}\\Omega)$$
</div>
<p>The internal voltage division between Base 1 and Base 2 defines the fundamental device parameter, the <strong>Intrinsic Standoff Ratio $\\eta$</strong>:</p>
<div class="math-display">
$$\\eta = \\frac{R_{B1}}{R_{B1} + R_{B2}} = \\frac{R_{B1}}{R_{BB}} \\quad (0.51 \\le \\eta \\le 0.82)$$
</div>

<h4>2. Dynamic Conduction & Negative Resistance Characteristic</h4>
<p>When an interbase bias $V_{BB}$ is applied with $B_2$ positive relative to $B_1$, the potential at the internal junction point $A$ inside the silicon bar is $V_A = \\eta V_{BB}$.</p>
<p>If emitter voltage $V_E < V_A + V_D$ (where $V_D \\approx 0.6\\,\\text{V}$ is the silicon diode forward barrier drop), the emitter junction is reverse-biased, permitting only a tiny reverse leakage current $I_{EO}$ to flow (Cutoff Region).</p>
<p>When $V_E$ reaches the <strong>Peak-Point Voltage $V_P$</strong>:</p>
<div class="math-display">
$$V_P = \\eta V_{BB} + V_D$$
</div>
<p>The emitter junction becomes forward-biased, injecting a burst of holes into the $N$-type channel between the emitter and $B_1$. This massive carrier injection drastically lowers the resistance $R_{B1}$ via <em>conductivity modulation</em>. As $I_E$ increases, $V_E$ rapidly plummets, establishing a dynamic <strong>Negative Differential Resistance region ($dV_E/dI_E < 0$)</strong> until reaching the <strong>Valley Point $(V_V, I_V)$</strong>, beyond which the device enters saturation.</p>

<h4>3. UJT Relaxation Oscillator Circuit & Derivation of Period</h4>
<p>In a relaxation oscillator, a timing resistor $R$ charges an external capacitor $C$ from $V_{BB}$. As $C$ charges, capacitor voltage rises exponentially:</p>
<div class="math-display">
$$v_C(t) = V_{BB} \\left( 1 - e^{-t / (RC)} \\right)$$
</div>
<p>When $v_C(t)$ reaches the peak point $V_P \\approx \\eta V_{BB}$ (neglecting small $V_D$ and assuming discharge to $V_V \\approx 0$):</p>
<div class="math-display">
$$\\eta V_{BB} = V_{BB} \\left( 1 - e^{-T / (RC)} \\right) \\implies 1 - \\eta = e^{-T / (RC)}$$
</div>
<p>Taking the natural logarithm of both sides yields the oscillation period $T$ and frequency $f$:</p>
<div class="math-display">
$$T = R C \\ln\\left( \\frac{1}{1 - \\eta} \\right)$$
</div>
<div class="math-display">
$$f = \\frac{1}{T} = \\frac{1}{R C \\ln\\left( \\frac{1}{1 - \\eta} \\right)}$$
</div>
<p>When the capacitor discharges rapidly through the low resistance of $R_{B1}$ and an external resistor $R_1$, a sharp, high-energy positive voltage pulse is developed across $R_1$, perfectly matched for reliably triggering SCR and Triac gates.</p>"""
        },
        {
            "id": "u3-sec4",
            "title": "Triac and Diac: Bidirectional AC Switching & Light Dimmer Circuits",
            "content": """<h4>1. Diac (Diode AC Switch): Symmetrical Bi-directional Trigger</h4>
<p>A Diac is a three-layer, two-terminal ($A_1$ and $A_2$) bidirectional semiconductor diode. It does not have a control gate. The device remains in forward or reverse blocking mode until the applied voltage across its terminals reaches the symmetrical breakover voltage $V_{BO}$ (typically $\\pm 30\\text{ to }35\\,\\text{V}$).</p>
<p>Once $|V| \\ge V_{BO}$, the Diac undergoes negative-resistance breakdown, dropping terminal voltage suddenly to $\\sim 20\\,\\text{V}$ and discharging a sharp spike of current in either positive or negative polarity. This makes Diacs the primary trigger element for driving Triac gates symmetrically on both alternating half-cycles.</p>

<h4>2. Triac (Triode AC Switch): Architecture and Quadrant Modes</h4>
<p>A Triac is functionally equivalent to two inverse-parallel (back-to-back) SCRs integrated monolithically on a single silicon chip with a single common gate terminal. The main power terminals are designated <strong>Main Terminal 1 (MT1)</strong> and <strong>Main Terminal 2 (MT2)</strong>, referenced to MT1.</p>
<p>A Triac can be triggered into conduction by either a positive or negative gate pulse for either polarity of terminal voltage $V_{MT2-MT1}$, operating across four quadrants:
<ul>
<li><strong>Mode I+ ($MT2+, G+$):</strong> Most sensitive mode. Both MT2 and Gate are positive with respect to MT1. Normal transistor junction action.</li>
<li><strong>Mode I- ($MT2+, G-$):</strong> MT2 positive, Gate negative with respect to MT1. Gate junction junction injection initiates turn-on.</li>
<li><strong>Mode III+ ($MT2-, G+$):</strong> MT2 negative, Gate positive with respect to MT1. Least sensitive mode requiring highest gate trigger current $I_{GT}$. Often avoided in symmetrical trigger circuits.</li>
<li><strong>Mode III- ($MT2-, G-$):</strong> Highly sensitive mode. MT2 negative, Gate negative. Remote gate injection triggering.</li>
</ul>
</p>

<h4>3. Full-Wave AC Phase Control (Light Dimmer Circuit)</h4>
<p>In a standard phase-controlled light dimmer or AC fan motor speed controller:
<ul>
<li>A potentiometer $R_v$ and fixed resistor $R_1$ charge capacitor $C$ from the AC mains line.</li>
<li>The voltage across $C$ lags behind the line voltage by phase angle $\\theta = \\arctan(\\omega R_{total} C)$.</li>
<li>When capacitor voltage $|v_C(t)|$ reaches the Diac breakdown voltage $V_{BO} \\approx 32\\,\\text{V}$, the Diac breaks down and rapidly dumps capacitor charge into the Triac gate.</li>
<li>The Triac fires into full conduction, applying the remaining portion of the mains half-cycle to the lamp or motor load.</li>
<li>At the end of the half-cycle, when AC load current crosses zero, the Triac commutates off naturally until the Diac fires in the opposite polarity during the subsequent half-cycle.</li>
</ul>
Adjusting $R_v$ varies the firing delay angle $\\alpha$ continuously from $\\approx 15^\\circ$ to $\\approx 165^\\circ$, smoothly controlling the RMS power delivered to the load from $\\approx 98\\%$ down to $0\\%$.</p>"""
        }
    ],
    "problems": [
        {
            "id": "u3-prob1",
            "title": "SCR Half-Wave Phase-Controlled Rectifier Analysis",
            "statement": "An SCR is used in a half-wave phase-controlled rectifier circuit supplied from a 230 V RMS, 50 Hz sinusoidal source, feeding a pure resistive load of R = 40 \\Omega. If the firing angle is set to \\alpha = 60^\\circ (\\pi/3 \\text{ rad}), calculate: (a) The peak supply voltage V_m, (b) The average (DC) load voltage V_{dc}, (c) The average DC load current I_{dc}, (d) The RMS load voltage V_{rms}, and (e) The total power delivered to the load.",
            "solution": """<p><strong>Step 1: Calculate Peak Supply Voltage $V_m$</strong></p>
<div class="math-display">
$$V_m = \\sqrt{2} \\times V_{rms,in} = \\sqrt{2} \\times 230\\,\\text{V} \\approx 325.27\\,\\text{V}$$
</div>

<p><strong>Step 2: Calculate Average (DC) Load Voltage $V_{dc}$</strong></p>
<p>Using the half-wave phase-controlled equation for firing angle $\\alpha = 60^\\circ$:</p>
<div class="math-display">
$$V_{dc} = \\frac{V_m}{2\\pi} (1 + \\cos\\alpha) = \\frac{325.27}{2\\pi} (1 + \\cos 60^\\circ) = \\frac{325.27}{2\\pi} (1 + 0.5) = \\frac{325.27 \\times 1.5}{6.28318} \\approx 77.65\\,\\text{V}$$
</div>

<p><strong>Step 3: Calculate Average DC Load Current $I_{dc}$</strong></p>
<div class="math-display">
$$I_{dc} = \\frac{V_{dc}}{R} = \\frac{77.65\\,\\text{V}}{40\\,\\Omega} \\approx 1.941\\,\\text{A}$$
</div>

<p><strong>Step 4: Calculate RMS Load Voltage $V_{rms}$</strong></p>
<p>Recall the RMS formula for half-wave phase control:</p>
<div class="math-display">
$$V_{rms} = \\frac{V_m}{2\\sqrt{\\pi}} \\sqrt{ (\\pi - \\alpha) + \\frac{1}{2} \\sin(2\\alpha) }$$
</div>
<p>Here $\\alpha = \\pi/3 \\approx 1.0472\\,\\text{rad}$, so $\\pi - \\alpha = 2\\pi/3 \\approx 2.0944\\,\\text{rad}$, and $\\sin(2\\alpha) = \\sin(120^\\circ) = \\frac{\\sqrt{3}}{2} \\approx 0.8660$:</p>
<div class="math-display">
$$\\text{Term inside root} = 2.0944 + \\frac{0.8660}{2} = 2.0944 + 0.4330 = 2.5274$$
</div>
<div class="math-display">
$$V_{rms} = \\frac{325.27}{2 \\times \\sqrt{3.14159}} \\times \\sqrt{2.5274} = \\frac{325.27}{3.5449} \\times 1.5898 \\approx 145.86\\,\\text{V}$$
</div>

<p><strong>Step 5: Total Power Delivered to Load $P_L$</strong></p>
<div class="math-display">
$$P_L = \\frac{V_{rms}^2}{R} = \\frac{(145.86\\,\\text{V})^2}{40\\,\\Omega} = \\frac{21275.14}{40} \\approx 531.88\\,\\text{W}$$
</div>"""
        },
        {
            "id": "u3-prob2",
            "title": "UJT Relaxation Oscillator Frequency & Peak Point Calculation",
            "statement": "A UJT has an intrinsic standoff ratio \\eta = 0.65, interbase resistance R_{BB} = 8\\,\\text{k}\\Omega, and forward diode drop V_D = 0.7\\,\\text{V}. It is connected in a relaxation oscillator circuit with V_{BB} = 15\\,\\text{V}, timing resistor R = 47\\,\\text{k}\\Omega, and timing capacitor C = 0.1\\,\\mu\\text{F}. Calculate: (a) Internal base resistances R_{B1} and R_{B2}, (b) The peak point voltage V_P, (c) The period of oscillation T, and (d) The oscillation frequency f.",
            "solution": """<p><strong>Step 1: Calculate Internal Base Resistances $R_{B1}$ and $R_{B2}$</strong></p>
<div class="math-display">
$$R_{B1} = \\eta \\cdot R_{BB} = 0.65 \\times 8\\,\\text{k}\\Omega = 5.2\\,\\text{k}\\Omega$$
</div>
<div class="math-display">
$$R_{B2} = R_{BB} - R_{B1} = 8.0\\,\\text{k}\\Omega - 5.2\\,\\text{k}\\Omega = 2.8\\,\\text{k}\\Omega$$
</div>

<p><strong>Step 2: Calculate Peak Point Voltage $V_P$</strong></p>
<div class="math-display">
$$V_P = \\eta V_{BB} + V_D = (0.65 \\times 15\\,\\text{V}) + 0.7\\,\\text{V} = 9.75\\,\\text{V} + 0.7\\,\\text{V} = 10.45\\,\\text{V}$$
</div>

<p><strong>Step 3: Calculate Period of Oscillation $T$</strong></p>
<p>Using the theoretical UJT charging equation with $V_V \\approx 0$:</p>
<div class="math-display">
$$T = R C \\ln\\left( \\frac{1}{1 - \\eta} \\right) = (47 \\times 10^3\\,\\Omega) \\times (0.1 \\times 10^{-6}\\,\\text{F}) \\times \\ln\\left( \\frac{1}{1 - 0.65} \\right)$$
</div>
<div class="math-display">
$$R C = 4.7 \\times 10^{-3}\\,\\text{s} = 4.7\\,\\text{ms}$$
</div>
<div class="math-display">
$$\\ln\\left(\\frac{1}{0.35}\\right) = \\ln(2.8571) \\approx 1.0498$$
</div>
<div class="math-display">
$$T = 4.7\\,\\text{ms} \\times 1.0498 \\approx 4.934\\,\\text{ms}$$
</div>

<p><strong>Step 4: Calculate Oscillation Frequency $f$</strong></p>
<div class="math-display">
$$f = \\frac{1}{T} = \\frac{1}{4.934 \\times 10^{-3}\\,\\text{s}} \\approx 202.67\\,\\text{Hz}$$
</div>"""
        },
        {
            "id": "u3-prob3",
            "title": "Full-Wave Bridge Controlled Rectifier with Inductive Load",
            "statement": "A single-phase full-wave controlled SCR bridge rectifier feeds a highly inductive load such that load current is continuous and ripple-free at I_o = 15\\,\\text{A}. The AC source is 240\\,\\text{V} RMS at 50 Hz. If the SCRs are fired at \\alpha = 45^\\circ: (a) Derive and calculate the average DC load voltage V_{dc}, (b) Calculate the active DC power absorbed by the load, and (c) Determine the input displacement power factor (DPF).",
            "solution": """<p><strong>Step 1: Calculate Average Output Voltage for Highly Inductive Load</strong></p>
<p>For a continuous-conduction inductive load, current continues through the zero crossing until the next pair of thyristors is fired at $\\pi + \\alpha$. Thus the integration limits are from $\\alpha$ to $\\pi + \\alpha$:</p>
<div class="math-display">
$$V_{dc} = \\frac{1}{\\pi} \\int_{\\alpha}^{\\pi + \\alpha} V_m \\sin(\\omega t)\\, d(\\omega t) = \\frac{V_m}{\\pi} [ -\\cos(\\pi + \\alpha) + \\cos\\alpha ] = \\frac{2V_m}{\\pi} \\cos\\alpha$$
</div>
<p>With $V_{rms} = 240\\,\\text{V}$, $V_m = 240\\sqrt{2} \\approx 339.41\\,\\text{V}$:</p>
<div class="math-display">
$$V_{dc} = \\frac{2 \\times 339.41}{\\pi} \\cos(45^\\circ) = 216.08 \\times 0.7071 \\approx 152.8\\,\\text{V}$$
</div>

<p><strong>Step 2: Calculate Active DC Power Delivered to Load</strong></p>
<div class="math-display">
$$P_{dc} = V_{dc} \\times I_o = 152.8\\,\\text{V} \\times 15\\,\\text{A} \\approx 2292\\,\\text{W} = 2.292\\,\\text{kW}$$
</div>

<p><strong>Step 3: Calculate Input Displacement Power Factor (DPF)</strong></p>
<p>For a phase-controlled converter with continuous current, the fundamental input AC current lags behind fundamental source voltage by exactly the firing angle $\\alpha$:</p>
<div class="math-display">
$$\\text{DPF} = \\cos(\\phi_1) = \\cos(\\alpha) = \\cos(45^\\circ) \\approx 0.7071 \\text{ (lagging)}$$
</div>"""
        }
    ]
}

unit4 = {
    "id": "unit-4",
    "number": 4,
    "title": "Transistor Amplifiers: Small-Signal, Multistage & Power Stages",
    "description": "Exhaustive analysis of small-signal amplifiers using hybrid h-parameters; high- and low-frequency cutoffs and Bode plots; multistage RC-coupled, transformer, and direct-coupled cascaded systems; Class A, B, AB, and C power amplifier topologies, push-pull configurations, theoretical efficiency limits, and crossover distortion remedies.",
    "sections": [
        {
            "id": "u4-sec1",
            "title": "Small-Signal Analysis & Hybrid h-Parameter Model of CE BJT",
            "content": """<h4>1. Two-Port Network Formalism and Hybrid h-Parameters</h4>
<p>For small alternating signals superimposed on DC quiescent operating points, a bipolar junction transistor in Common Emitter (CE) configuration is modeled linearly as a two-port network relating input voltage $v_b$, input current $i_b$, output current $i_c$, and output voltage $v_c$:</p>
<div class="math-display">
$$v_b = h_{ie} i_b + h_{re} v_c$$
</div>
<div class="math-display">
$$i_c = h_{fe} i_b + h_{oe} v_c$$
</div>
<p>The four parameters are precisely defined under AC short-circuit and open-circuit conditions:
<ul>
<li><strong>$h_{ie} = \\left.\\frac{v_b}{i_b}\\right|_{v_c = 0}$ :</strong> Short-circuit input impedance $(\\Omega)$</li>
<li><strong>$h_{re} = \\left.\\frac{v_b}{v_c}\\right|_{i_b = 0}$ :</strong> Open-circuit reverse voltage ratio (dimensionless, typically $\\sim 10^{-4}$)</li>
<li><strong>$h_{fe} = \\left.\\frac{i_c}{i_b}\\right|_{v_c = 0}$ :</strong> Short-circuit forward current transfer ratio / AC current gain $(\\beta_{ac})$</li>
<li><strong>$h_{oe} = \\left.\\frac{i_c}{v_c}\\right|_{i_b = 0}$ :</strong> Open-circuit output admittance $(\\text{S} = \\Omega^{-1}$, typically $\\sim 20\\,\\mu\\text{S}$)</li>
</ul>
</p>

<h4>2. Simplified CE Hybrid Model & Gain Derivations</h4>
<p>In standard practical audio and RF amplifier design, $h_{re} \\approx 0$ (reverse feedback negligible) and $h_{oe} R_L \\ll 0.1$ (output conductances much smaller than load conductance). The circuit simplifies to an input resistor $h_{ie}$ and a dependent current source $h_{fe} i_b$.</p>
<p>With an effective AC collector load $R_L' = R_C \\parallel R_L$:</p>
<div class="math-display">
$$v_{out} = - i_c R_L' = - h_{fe} i_b R_L'$$
</div>
<div class="math-display">
$$v_{in} = i_b h_{ie}$$
</div>
<p>Hence, the <strong>Voltage Gain $A_v$</strong> is:</p>
<div class="math-display">
$$A_v = \\frac{v_{out}}{v_{in}} = - \\frac{h_{fe} R_L'}{h_{ie}}$$
</div>
<p>The negative sign reflects the fundamental $180^\\circ$ phase inversion between input base signal and output collector signal in a Common Emitter amplifier.</p>
<p>The <strong>Current Gain $A_i$</strong>, <strong>Input Impedance $Z_{in}$</strong>, and <strong>Output Impedance $Z_{out}$</strong> are:</p>
<div class="math-display">
$$A_i = \\frac{i_{out}}{i_b} = - h_{fe} \\frac{R_C}{R_C + R_L}, \\quad Z_{in} = h_{ie}, \\quad Z_{out} \\approx R_C$$
</div>

<h4>3. Frequency Response and Cutoff Frequencies</h4>
<p>The frequency response curve of a CE amplifier exhibits three distinct regimes:
<ul>
<li><strong>Low-Frequency Range ($f < f_L$):</strong> The reactances of coupling capacitors $C_1, C_2$ and emitter bypass capacitor $C_E$ ($X_C = 1/(2\pi f C)$) grow large. This introduces voltage division and degenerative negative feedback across $R_E$, reducing voltage gain at a slope of $+20\\,\\text{dB/decade}$ per dominant pole.</li>
<li><strong>Midband Range ($f_L \\le f \\le f_H$):</strong> Coupling/bypass capacitors act as virtual short circuits ($X_C \\approx 0$), while internal parasitic transistor capacitances act as virtual open circuits. The gain remains flat at maximum midband gain $A_{vm}$.</li>
<li><strong>High-Frequency Range ($f > f_H$):</strong> The internal depletion and diffusion capacitances (base-emitter capacitance $C_\\pi$ and base-collector Miller capacitance $C_\\mu$) introduce shunting paths to ground, rolling off gain at $-20\\,\\text{dB/decade}$.</li>
</ul>
</p>
<p>The <strong>Bandwidth ($BW$)</strong> is defined between the half-power ($-3\\,\\text{dB}$) points:</p>
<div class="math-display">
$$BW = f_H - f_L \\approx f_H \\quad (\\text{since } f_H \\gg f_L)$$
</div>"""
        },
        {
            "id": "u4-sec2",
            "title": "Multistage Amplifiers: RC-Coupled, Transformer & Direct Coupling",
            "content": """<h4>1. Cascading Amplifiers & Decibel Gain Formalism</h4>
<p>A single transistor stage often cannot simultaneously provide adequate voltage gain, current drive, and impedance matching. Multiple amplifier stages are therefore cascaded in series, where the output of stage $n$ serves as the input to stage $n+1$.</p>
<p>The overall voltage gain is the multiplicative product of individual loaded gains:</p>
<div class="math-display">
$$A_v = A_{v1} \\times A_{v2} \\times A_{v3} \\times \\dots \\times A_{vn}$$
</div>
<p>Expressed logarithmically in <strong>Decibels (dB)</strong>:</p>
<div class="math-display">
$$A_v(\\text{dB}) = 20 \\log_{10} |A_v| = 20 \\log_{10} |A_{v1}| + 20 \\log_{10} |A_{v2}| + \\dots + 20 \\log_{10} |A_{vn}|$$
</div>
<p>Decibels convert complicated cascading products into simple additions.</p>

<h4>2. Comparative Analysis of Coupling Schemes</h4>
<table class="data-table" style="width:100%; border-collapse:collapse; margin:16px 0;">
<thead>
<tr style="background:rgba(255,255,255,0.05); text-align:left;">
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Coupling Type</th>
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Frequency Response</th>
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Impedance Matching</th>
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Cost & Size</th>
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Primary Applications</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);"><strong>RC Coupling</strong></td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Excellent flat midband (audio 20 Hz – 20 kHz); rolls off at DC and very high RF</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Poor (collector $R_C$ shunts next stage $Z_{in}$)</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Extremely low cost, compact, highly reliable</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Audio preamplifiers, general-purpose voltage gain</td>
</tr>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);"><strong>Transformer Coupling</strong></td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Poor audio flatness; resonant peaking; zero response at DC</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Superior ($Z_p/Z_s = (N_p/N_s)^2$) for maximum power transfer</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Bulky, heavy, expensive, magnetic hum pickup</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">RF tuned amplifiers, driver stages to low-impedance speakers</td>
</tr>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);"><strong>Direct Coupling</strong></td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Extends down to DC ($0\\,\\text{Hz}$); no lower cutoff frequency</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Moderate</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Minimal parts, ideal for monolithic IC fabrication</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Operational amplifiers, biosensors, DC instrumentation</td>
</tr>
</tbody>
</table>

<h4>3. Loading Effect in RC-Coupled Cascades</h4>
<p>When stage 1 is coupled to stage 2 through capacitor $C_c$, the effective AC load seen by collector 1 is not simply $R_{C1}$, but the parallel combination of $R_{C1}$ and the input impedance of stage 2:</p>
<div class="math-display">
$$R_{L1}' = R_{C1} \\parallel R_{12} \\parallel R_{22} \\parallel h_{ie2}$$
</div>
<p>Because $R_{L1}' < R_{C1}$, the loaded gain $A_{v1}$ is significantly smaller than the open-circuit gain of an isolated stage. Neglecting this loading effect produces massive design errors.</p>"""
        },
        {
            "id": "u4-sec3",
            "title": "Power Amplifiers: Classification (Class A, B, AB, C) & Efficiency Limits",
            "content": """<h4>1. Large-Signal Operation & Conduction Angle Classifications</h4>
<p>Unlike small-signal voltage amplifiers that handle millivolt signals, <strong>Power Amplifiers (large-signal amplifiers)</strong> deliver significant power (watts to kilowatts) into low-impedance loads (speakers, antennas) with high efficiency while keeping device dissipation within thermal tolerances ($T_j < T_{j,max}$).</p>
<p>Amplifier classes are categorized strictly by the <strong>conduction angle $\\theta_c$</strong> of the collector current during one complete sinusoidal input cycle ($360^\\circ$):
<ul>
<li><strong>Class A ($\theta_c = 360^\circ$ or $2\pi$ radians):</strong> The transistor conducts continuously for the entire input cycle. The Q-point is biased in the center of the active linear region. Distortions are minimal, but static DC power is continually wasted even with zero signal.</li>
<li><strong>Class B ($\theta_c = 180^\circ$ or $\pi$ radians):</strong> The transistor is biased exactly at cutoff ($I_{CQ} = 0$). Conduction occurs for exactly one half-cycle ($180^\\circ$). Zero static DC power at idle.</li>
<li><strong>Class AB ($180^\circ < \theta_c < 360^\circ$):</strong> Biased slightly above cutoff with a small quiescent current ($I_{CQ} > 0$). Conduction occurs for slightly more than half a cycle, eliminating Class B crossover distortion.</li>
<li><strong>Class C ($\theta_c < 180^\circ$):</strong> Biased well beyond cutoff. Conduction occurs in brief pulses ($80^\circ - 120^\circ$). High harmonic distortion; used exclusively with tuned resonant LC tanks in high-efficiency RF transmitters.</li>
</ul>
</p>

<h4>2. Mathematical Derivation of Maximum Collector Efficiency</h4>
<p><strong>Collector Efficiency $\\eta$</strong> is defined as the ratio of average AC output power delivered to the load to the average DC power drawn from the power supply:</p>
<div class="math-display">
$$\\eta = \\frac{P_{ac,out}}{P_{dc,in}} \\times 100\\%$$
</div>

<h5>(a) Series-Fed Class A Amplifier</h5>
<p>For a series-fed Class A amplifier with supply $V_{CC}$ and collector resistor $R_C$:</p>
<div class="math-display">
$$V_{CQ} = \\frac{V_{CC}}{2}, \\quad I_{CQ} = \\frac{V_{CC}}{2 R_C}$$
</div>
<div class="math-display">
$$P_{dc,in} = V_{CC} I_{CQ} = \\frac{V_{CC}^2}{2 R_C}$$
</div>
<p>Under maximum unclipped sinusoidal swing, $V_m = V_{CC}/2$ and $I_m = I_{CQ} = V_{CC}/(2 R_C)$:</p>
<div class="math-display">
$$P_{ac,max} = \\frac{V_m I_m}{2} = \\frac{(V_{CC}/2)(V_{CC}/(2 R_C))}{2} = \\frac{V_{CC}^2}{8 R_C}$$
</div>
<div class="math-display">
$$\\eta_{max, \\text{Series-Fed Class A}} = \\frac{P_{ac,max}}{P_{dc,in}} = \\frac{V_{CC}^2 / (8 R_C)}{V_{CC}^2 / (2 R_C)} = \\frac{2}{8} = 25\\%$$
</div>
<p>For a transformer-coupled Class A amplifier, the DC drop across the primary is near zero, allowing peak-to-peak voltage swing up to $2 V_{CC}$, doubling the theoretical limit to <strong>$\eta_{max} = 50\%$</strong>.</p>

<h5>(b) Push-Pull Class B Amplifier</h5>
<p>In a complementary-symmetry push-pull Class B configuration operating from a supply $V_{CC}$ (or dual $\pm V_{CC}$):</p>
<p>For peak load voltage $V_m$ across load $R_L$, peak collector current is $I_m = V_m / R_L$. The average current drawn from the DC supply during half-wave pulses by each rail is $I_{dc} = \\frac{2}{\\pi} I_m$. Thus:</p>
<div class="math-display">
$$P_{dc,in} = V_{CC} \\left( \\frac{2}{\\pi} I_m \\right) = \\frac{2}{\\pi} \\frac{V_{CC} V_m}{R_L}$$
</div>
<p>The AC power delivered to the load is:</p>
<div class="math-display">
$$P_{ac,out} = \\frac{V_m^2}{2 R_L}$$
</div>
<p>Collector efficiency as a function of output swing is:</p>
<div class="math-display">
$$\\eta = \\frac{P_{ac,out}}{P_{dc,in}} = \\frac{V_m^2 / (2 R_L)}{2 V_{CC} V_m / (\\pi R_L)} = \\frac{\\pi}{4} \\left( \\frac{V_m}{V_{CC}} \\right)$$
</div>
<p>Under maximum theoretical output voltage swing where $V_m = V_{CC}$:</p>
<div class="math-display">
$$\\eta_{max, \\text{Class B}} = \\frac{\\pi}{4} \\approx 0.7854 = 78.54\\%$$
</div>"""
        },
        {
            "id": "u4-sec4",
            "title": "Push-Pull Configurations, Crossover Distortion & Class AB Biasing",
            "content": """<h4>1. Push-Pull Operation & Harmonic Distortion Cancellation</h4>
<p>A push-pull amplifier utilizes two matched transistors ($Q_1$ and $Q_2$) operating in anti-phase: $Q_1$ conducts during the positive half-cycle of the input signal, pushing current into the load, while $Q_2$ conducts during the negative half-cycle, pulling current from the load.</p>
<p>Mathematically, expanding the nonlinear collector current transfer characteristics in a Taylor series:</p>
<div class="math-display">
$$i_{c1} = I_Q + a_1 v_{in} + a_2 v_{in}^2 + a_3 v_{in}^3 + \\dots$$
</div>
<div class="math-display">
$$i_{c2} = I_Q + a_1 (-v_{in}) + a_2 (-v_{in})^2 + a_3 (-v_{in})^3 + \\dots = I_Q - a_1 v_{in} + a_2 v_{in}^2 - a_3 v_{in}^3 + \\dots$$
</div>
<p>In a balanced push-pull output transformer, net load current is proportional to the difference $i_{c1} - i_{c2}$:</p>
<div class="math-display">
$$i_{load} = k (i_{c1} - i_{c2}) = 2 k \\left( a_1 v_{in} + a_3 v_{in}^3 + a_5 v_{in}^5 + \\dots \\right)$$
</div>
<p><strong>Crucial Result:</strong> All even-order harmonic distortion terms ($a_2 v_{in}^2, a_4 v_{in}^4$) completely cancel out! Furthermore, DC core saturation in output transformers is eliminated because quiescent currents produce opposing magnetic fluxes.</p>

<h4>2. Crossover Distortion in Pure Class B</h4>
<p>In a pure Class B push-pull stage, transistors are biased at $V_{BE} = 0$. However, real silicon bipolar transistors require a threshold forward voltage $V_{BE} \\approx 0.6\\text{ to }0.7\\,\\text{V}$ before base-emitter conduction begins.</p>
<p>Consequently, whenever the input signal passes through the zero-crossing within the deadband $-0.7\\,\\text{V} < v_{in} < +0.7\\,\\text{V}$, neither transistor conducts ($i_{c1} = i_{c2} = 0$). The output waveform flattens to zero near every crossing, generating severe high-order harmonic distortion known as <strong>Crossover Distortion</strong>.</p>

<h4>3. Class AB Biasing and Diode Thermal Tracking</h4>
<p>To eliminate crossover distortion, the transistors are biased into <strong>Class AB</strong> by applying a slight forward bias ($V_{bias} \\approx 2 V_D \\approx 1.4\\,\\text{V}$) across the base terminals using two series silicon diodes ($D_1, D_2$) or an active $V_{BE}$-multiplier circuit.</p>
<p>This maintains both transistors barely conducting at an idle quiescent current $I_{CQ} \\approx 10\\text{ to }50\\,\\text{mA}$. When the input swings through zero, the conduction smoothly transfers from $Q_1$ to $Q_2$ with zero deadband. Mounting the biasing diodes on the same physical heatsink as the power output transistors ensures <strong>thermal tracking</strong>: as junction temperature rises, diode voltage drops at $-2\\,\\text{mV}/^\\circ\\text{C}$, matching the transistor $V_{BE}$ drop and preventing thermal runaway.</p>"""
        }
    ],
    "problems": [
        {
            "id": "u4-prob1",
            "title": "Small-Signal CE Amplifier Analysis via Hybrid h-Parameters",
            "statement": "A Common Emitter BJT amplifier operates with a load resistance R_L = 10\\,\\text{k}\\Omega and collector bias resistor R_C = 4.7\\,\\text{k}\\Omega. The transistor has the following hybrid h-parameters: h_{ie} = 1.2\\,\\text{k}\\Omega, h_{fe} = 120, h_{re} = 2.5 \\times 10^{-4}, and h_{oe} = 25\\,\\mu\\text{S}. Using the exact and simplified h-parameter models: (a) Determine the effective AC load resistance R_L', (b) Calculate the voltage gain A_v, (c) Calculate the current gain A_i, and (d) Calculate the input impedance Z_{in}.",
            "solution": """<p><strong>Step 1: Calculate Effective AC Collector Load $R_L'$</strong></p>
<p>The AC collector resistance is the parallel combination of $R_C$ and external load $R_L$:</p>
<div class="math-display">
$$R_L' = R_C \\parallel R_L = \\frac{4.7\\,\\text{k}\\Omega \\times 10\\,\\text{k}\\Omega}{4.7\\,\\text{k}\\Omega + 10\\,\\text{k}\\Omega} = \\frac{47}{14.7} \\approx 3.197\\,\\text{k}\\Omega$$
</div>

<p><strong>Step 2: Check Simplified Model Validity</strong></p>
<div class="math-display">
$$h_{oe} R_L' = (25 \\times 10^{-6}\\,\\text{S}) \\times (3.197 \\times 10^3\\,\\Omega) = 0.0799 < 0.1$$
</div>
<p>Since $h_{oe} R_L' < 0.1$, the simplified model yields high accuracy within $5\\%$.</p>

<p><strong>Step 3: Calculate Voltage Gain $A_v$</strong></p>
<p>Using the simplified formula:</p>
<div class="math-display">
$$A_v = - \\frac{h_{fe} R_L'}{h_{ie}} = - \\frac{120 \\times 3.197\\,\\text{k}\\Omega}{1.2\\,\\text{k}\\Omega} = - \\frac{383.64}{1.2} \\approx -319.7$$
</div>
<p>Using the exact formula including $h_{re}$ and $h_{oe}$:</p>
<div class="math-display">
$$A_v = \\frac{- h_{fe} R_L'}{h_{ie} + (h_{ie} h_{oe} - h_{fe} h_{re}) R_L'}$$
</div>
<div class="math-display">
$$\\Delta h = h_{ie} h_{oe} - h_{fe} h_{re} = (1200 \\times 2.5 \\times 10^{-5}) - (120 \\times 2.5 \\times 10^{-4}) = 0.030 - 0.030 = 0$$
</div>
<p>Remarkably, $\\Delta h \\approx 0$ here, so the exact gain equals precisely the simplified gain: $A_v = -319.7$.</p>

<p><strong>Step 4: Calculate Current Gain $A_i$ and Input Impedance $Z_{in}$</strong></p>
<div class="math-display">
$$A_i = \\frac{- h_{fe}}{1 + h_{oe} R_L'} = \\frac{-120}{1 + 0.0799} = \\frac{-120}{1.0799} \\approx -111.1$$
</div>
<div class="math-display">
$$Z_{in} = h_{ie} - \\frac{h_{re} h_{fe} R_L'}{1 + h_{oe} R_L'} = 1200 - \\frac{(2.5 \\times 10^{-4})(120)(3197)}{1.0799} = 1200 - 88.8 = 1111.2\\,\\Omega \\approx 1.11\\,\\text{k}\\Omega$$
</div>"""
        },
        {
            "id": "u4-prob2",
            "title": "Two-Stage RC-Coupled Amplifier Cascaded Analysis",
            "statement": "A two-stage RC-coupled BJT amplifier consists of identical Common Emitter stages. For each transistor, h_{ie} = 1.5\\,\\text{k}\\Omega, h_{fe} = 100, and h_{oe} = h_{re} \\approx 0. Circuit component values are: R_{C1} = R_{C2} = 3.3\\,\\text{k}\\Omega, biasing network R_1 \\parallel R_2 = 15\\,\\text{k}\\Omega, and the final load connected to Stage 2 is R_L = 4.7\\,\\text{k}\\Omega. Calculate: (a) The loaded voltage gain of the second stage A_{v2}, (b) The input impedance of the second stage Z_{in2}, (c) The loaded voltage gain of the first stage A_{v1}, (d) The overall voltage gain A_v, and (e) The overall gain in decibels (dB).",
            "solution": """<p><strong>Step 1: Calculate Input Impedance of Stage 2 ($Z_{in2}$)</strong></p>
<p>The input impedance of Stage 2 includes the bias resistors in parallel with the transistor base input:</p>
<div class="math-display">
$$Z_{in2} = (R_1 \\parallel R_2) \\parallel h_{ie2} = 15\\,\\text{k}\\Omega \\parallel 1.5\\,\\text{k}\\Omega = \\frac{15 \\times 1.5}{15 + 1.5} = \\frac{22.5}{16.5} \\approx 1.364\\,\\text{k}\\Omega$$
</div>

<p><strong>Step 2: Calculate Loaded Voltage Gain of Stage 2 ($A_{v2}$)</strong></p>
<p>The effective AC load on Stage 2 is $R_{L2}' = R_{C2} \\parallel R_L$:</p>
<div class="math-display">
$$R_{L2}' = 3.3\\,\\text{k}\\Omega \\parallel 4.7\\,\\text{k}\\Omega = \\frac{3.3 \\times 4.7}{3.3 + 4.7} = \\frac{15.51}{8.0} \\approx 1.939\\,\\text{k}\\Omega$$
</div>
<div class="math-display">
$$A_{v2} = - \\frac{h_{fe} R_{L2}'}{h_{ie2}} = - \\frac{100 \\times 1.939\\,\\text{k}\\Omega}{1.5\\,\\text{k}\\Omega} \\approx -129.27$$
</div>

<p><strong>Step 3: Calculate Loaded Voltage Gain of Stage 1 ($A_{v1}$)</strong></p>
<p>Stage 1 is loaded by its own collector resistor $R_{C1}$ in parallel with the entire input impedance $Z_{in2}$ of Stage 2:</p>
<div class="math-display">
$$R_{L1}' = R_{C1} \\parallel Z_{in2} = 3.3\\,\\text{k}\\Omega \\parallel 1.364\\,\\text{k}\\Omega = \\frac{3.3 \\times 1.364}{3.3 + 1.364} = \\frac{4.501}{4.664} \\approx 0.965\\,\\text{k}\\Omega$$
</div>
<div class="math-display">
$$A_{v1} = - \\frac{h_{fe} R_{L1}'}{h_{ie1}} = - \\frac{100 \\times 0.965\\,\\text{k}\\Omega}{1.5\\,\\text{k}\\Omega} \\approx -64.33$$
</div>

<p><strong>Step 4: Calculate Overall Voltage Gain $A_v$ and Decibel Gain</strong></p>
<div class="math-display">
$$A_v = A_{v1} \\times A_{v2} = (-64.33) \\times (-129.27) \\approx +8315.9$$
</div>
<p>Note that the double phase inversion produces an overall positive gain (in-phase output).</p>
<div class="math-display">
$$A_v(\\text{dB}) = 20 \\log_{10}(8315.9) = 20 \\times 3.9199 \\approx 78.4\\,\\text{dB}$$
</div>"""
        },
        {
            "id": "u4-prob3",
            "title": "Class B Push-Pull Power Amplifier Performance & Thermal Dissipation",
            "statement": "A complementary-symmetry Class B push-pull amplifier operates from dual power supplies of \\pm V_{CC} = \\pm 18\\,\\text{V} and delivers power to an 8\\,\\Omega loudspeaker load. Under maximum unclipped output signal swing (V_m \\approx V_{CC}): (a) Calculate the maximum AC power delivered to the load P_{ac,max}, (b) Calculate the DC power drawn from the supply rails P_{dc}, (c) Determine the maximum collector efficiency \\eta_{max}, (d) Calculate the maximum power dissipated by each transistor P_{D1}, and (e) Calculate the transistor peak collector dissipation condition and value.",
            "solution": """<p><strong>Step 1: Calculate Maximum AC Power Delivered to Load $P_{ac,max}$</strong></p>
<p>With peak output voltage $V_m = V_{CC} = 18\\,\\text{V}$ and load $R_L = 8\\,\\Omega$:</p>
<div class="math-display">
$$P_{ac,max} = \\frac{V_m^2}{2 R_L} = \\frac{(18\\,\\text{V})^2}{2 \\times 8\\,\\Omega} = \\frac{324}{16} = 20.25\\,\\text{W}$$
</div>

<p><strong>Step 2: Calculate DC Power Drawn from Supply $P_{dc}$</strong></p>
<p>Peak output current is $I_m = V_m / R_L = 18 / 8 = 2.25\\,\\text{A}$. Average supply current is $I_{dc} = \\frac{2}{\\pi} I_m$:</p>
<div class="math-display">
$$I_{dc} = \\frac{2}{\\pi} \\times 2.25\\,\\text{A} = \\frac{4.5}{\\pi} \\approx 1.432\\,\\text{A}$$
</div>
<div class="math-display">
$$P_{dc} = V_{CC} I_{dc} = 18\\,\\text{V} \\times 1.4324\\,\\text{A} \\approx 25.78\\,\\text{W}$$
</div>

<p><strong>Step 3: Collector Efficiency $\\eta$ at Maximum Swing</strong></p>
<div class="math-display">
$$\\eta = \\frac{P_{ac,max}}{P_{dc}} \\times 100\\% = \\frac{20.25\\,\\text{W}}{25.78\\,\\text{W}} \\times 100\\% \\approx 78.54\\%$$
</div>

<p><strong>Step 4: Power Dissipated by Transistors at Maximum Swing</strong></p>
<p>The total heat power dissipated across both transistors is:</p>
<div class="math-display">
$$P_{D,total} = P_{dc} - P_{ac,max} = 25.78\\,\\text{W} - 20.25\\,\\text{W} = 5.53\\,\\text{W}$$
</div>
<p>For each individual transistor:</p>
<div class="math-display">
$$P_{D1} = \\frac{P_{D,total}}{2} = \\frac{5.53\\,\\text{W}}{2} \\approx 2.765\\,\\text{W}$$
</div>

<p><strong>Step 5: Worst-Case Transistor Thermal Dissipation Peak</strong></p>
<p>In Class B amplifiers, maximum transistor dissipation does NOT occur at maximum signal swing! Total dissipation is $P_D(V_m) = \\frac{2 V_{CC} V_m}{\\pi R_L} - \\frac{V_m^2}{2 R_L}$. Differentiating with respect to $V_m$ and setting to zero:</p>
<div class="math-display">
$$\\frac{d P_D}{d V_m} = \\frac{2 V_{CC}}{\\pi R_L} - \\frac{V_m}{R_L} = 0 \\implies V_m = \\frac{2}{\\pi} V_{CC} \\approx 0.6366 V_{CC}$$
</div>
<div class="math-display">
$$V_m^* = 0.6366 \\times 18\\,\\text{V} \\approx 11.46\\,\\text{V}$$
</div>
<p>At this specific output voltage swing, the worst-case transistor dissipation is:</p>
<div class="math-display">
$$P_{D,max}(\\text{per transistor}) = \\frac{V_{CC}^2}{\\pi^2 R_L} = \\frac{(18\\,\\text{V})^2}{\\pi^2 \\times 8\\,\\Omega} = \\frac{324}{78.957} \\approx 4.10\\,\\text{W}$$
</div>
<p>Heatsink sizing must be designed to withstand this $4.10\\,\\text{W}$ peak dissipation rather than the $2.765\\,\\text{W}$ full-power condition.</p>"""
        }
    ]
}

with open("be_u3.json", "w") as f:
    json.dump(unit3, f, indent=2)

with open("be_u4.json", "w") as f:
    json.dump(unit4, f, indent=2)

print("be_u3.json and be_u4.json generated successfully!")
