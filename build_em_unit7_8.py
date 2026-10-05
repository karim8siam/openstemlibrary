# Build Script for Units 7 and 8: Alternating Current and Circuit Analysis Theorems
import json

# =========================================================================
# UNIT 7: Alternating Current
# =========================================================================
u7_sections = [
    {
        "id": "sec-7-1",
        "number": "§7.1",
        "heading": "AC Generator Principles and Mathematical Representation of Sinusoids",
        "simulation": "ac-rlc-resonance-sim",
        "content": """Alternating Current (AC) is electric current whose magnitude and direction reverse periodically in time according to a sinusoidal function.

<h4>1. The Simple AC Generator (Alternator)</h4>
Consider a planar rectangular armature coil of $N$ turns and area $A$ rotated with constant angular velocity $\\omega$ in a uniform magnetic field $\\vec{B}$.
The instantaneous angle between the coil normal and the field is $\\theta(t) = \\omega t$.
The magnetic flux through the coil is:
$$\\Phi_B(t) = B A \\cos(\\omega t)$$
By Faraday's law of electromagnetic induction, the induced EMF is:
$$\\mathcal{E}(t) = -N \\frac{d\\Phi_B}{dt} = -N B A \\frac{d}{dt}[\\cos(\\omega t)] = N B A \\omega \\sin(\\omega t)$$
$$\\mathcal{E}(t) = \\mathcal{E}_0 \\sin(\\omega t)$$
where $\\mathcal{E}_0 = N B A \\omega$ is the **peak voltage amplitude** (Volts).

<h4>2. Root-Mean-Square (R.M.S.) and Average Values</h4>
Consider a sinusoidal voltage $v(t) = V_0 \\sin(\\omega t)$ with period $T = 2\\pi / \\omega$:
<ul>
  <li><strong>Full-Cycle Average:</strong>
  $$\\bar{V} = \\frac{1}{T}\\int_0^T V_0 \\sin(\\omega t) dt = 0$$
  The average over a complete cycle vanishes because positive and negative half-cycles cancel identically.</li>
  <li><strong>Half-Cycle Average:</strong>
  $$\\bar{V}_{1/2} = \\frac{2}{T}\\int_0^{T/2} V_0 \\sin(\\omega t) dt = \\frac{2 V_0}{\\pi} \\approx 0.6366 V_0$$</li>
  <li><strong>Root-Mean-Square (R.M.S. / Effective) Value:</strong>
  The equivalent DC voltage that produces the identical average heating power in a pure resistor:
  $$V_{\\text{rms}} = \\sqrt{ \\frac{1}{T}\\int_0^T [V_0 \\sin(\\omega t)]^2 dt } = \\sqrt{ \\frac{V_0^2}{T}\\int_0^T \\left(\\frac{1 - \\cos(2\\omega t)}{2}\\right) dt } = \\frac{V_0}{\\sqrt{2}} \\approx 0.7071 V_0$$
  $$I_{\\text{rms}} = \\frac{I_0}{\\sqrt{2}} \\approx 0.7071 I_0$$
  (Standard household mains 230 V or 120 V AC are R.M.S. values; the peak amplitude is $V_0 = 230\\sqrt{2} \\approx 325\\text{ V}$).</li>
</ul>"""
    },
    {
        "id": "sec-7-2",
        "number": "§7.2",
        "heading": "AC Response of Pure Circuit Elements: Resistors, Inductors, and Capacitors",
        "simulation": "ac-rlc-resonance-sim",
        "content": """When sinusoidal voltage $v(t) = V_0 \\sin(\\omega t)$ is applied individually to ideal passive elements, distinct phase relationships emerge.

<h4>1. Pure Resistive Circuit ($R$)</h4>
Applying Ohm's law:
$$i_R(t) = \\frac{v(t)}{R} = \\frac{V_0}{R} \\sin(\\omega t) = I_0 \\sin(\\omega t)$$
<em>Phase:</em> Current and voltage are strictly **in phase** ($\\phi = 0$).

<h4>2. Pure Inductive Circuit ($L$)</h4>
By Faraday's law: $v(t) = L \\frac{di}{dt} \\implies di = \\frac{V_0}{L} \\sin(\\omega t) dt$.
Integrating:
$$i_L(t) = -\\frac{V_0}{\\omega L} \\cos(\\omega t) = \\frac{V_0}{\\omega L} \\sin\\left( \\omega t - \\frac{\\pi}{2} \\right) = I_0 \\sin\\left( \\omega t - \\frac{\\pi}{2} \\right)$$
where $X_L = \\omega L = 2\\pi f L$ is the <strong>Inductive Reactance</strong> ($\Omega$).
<em>Phase:</em> In an inductor, current **lags voltage by 90° ($\pi/2$ radians)**. An inductor opposes high frequencies ($X_L \\propto f$).

<h4>3. Pure Capacitive Circuit ($C$)</h4>
By charge-voltage relation: $q(t) = C v(t) = C V_0 \\sin(\\omega t)$.
Current is $i(t) = \\frac{dq}{dt}$:
$$i_C(t) = \\omega C V_0 \\cos(\\omega t) = \\frac{V_0}{1/(\\omega C)} \\sin\\left( \\omega t + \\frac{\\pi}{2} \\right) = I_0 \\sin\\left( \\omega t + \\frac{\\pi}{2} \\right)$$
where $X_C = \\frac{1}{\\omega C} = \\frac{1}{2\\pi f C}$ is the <strong>Capacitive Reactance</strong> ($\Omega$).
<em>Phase:</em> In a capacitor, current **leads voltage by 90° ($\pi/2$ radians)**. A capacitor blocks DC ($X_C \\to \\infty$ as $f \\to 0$) and passes high frequencies ($X_C \\to 0$).
<em>Mnemonic:</em> **ELI the ICE man** (in $L$, $E$ leads $I$; in $C$, $I$ leads $E$)."""
    },
    {
        "id": "sec-7-3",
        "number": "§7.3",
        "heading": "Series LCR Circuits, Complex Impedance, and Electrical Resonance",
        "simulation": "ac-rlc-resonance-sim",
        "content": """Connecting a resistor, inductor, and capacitor in series across an AC source $v(t) = V_0 \\sin(\\omega t)$ establishes a driven harmonic system.

<h4>1. Phasor Addition and Total Impedance ($Z$)</h4>
Because elements are in series, the common current is $i(t) = I_0 \\sin(\\omega t - \\phi)$.
The voltage drops across each element are:
$$V_R = I_0 R, \\quad V_L = I_0 X_L, \\quad V_C = I_0 X_C$$
On the phasor plane, $V_L$ leads $I$ by $+90^\\circ$ and $V_C$ lags $I$ by $-90^\\circ$. The net reactive voltage is $V_L - V_C$.
By the Pythagorean theorem:
$$V_0 = \\sqrt{ V_R^2 + (V_L - V_C)^2 } = I_0 \\sqrt{ R^2 + (X_L - X_C)^2 } = I_0 Z$$
The <strong>Impedance ($Z$)</strong> of the series LCR circuit is:
$$Z = \\sqrt{ R^2 + (\\omega L - \\frac{1}{\\omega C})^2 }$$
The phase angle $\\phi$ of voltage relative to current is:
$$\\tan\\phi = \\frac{X_L - X_C}{R} = \\frac{\\omega L - 1/(\\omega C)}{R}$$
<ul>
  <li>If $X_L > X_C$: $\\phi > 0$ (circuit is inductive, voltage leads current).</li>
  <li>If $X_L < X_C$: $\\phi < 0$ (circuit is capacitive, current leads voltage).</li>
  <li>If $X_L = X_C$: $\\phi = 0$ (circuit is purely resistive).</li>
</ul>

<h4>2. Series Electrical Resonance</h4>
When the applied frequency makes inductive reactance balance capacitive reactance:
$$X_L = X_C \\implies \\omega_0 L = \\frac{1}{\\omega_0 C} \\implies \\omega_0 = \\frac{1}{\\sqrt{LC}}, \\quad f_0 = \\frac{1}{2\\pi\\sqrt{LC}}$$
At the <strong>resonant frequency $\omega_0$</strong>:
<ol>
  <li>The total impedance drops to its absolute theoretical minimum: $Z_{\\min} = R$.</li>
  <li>The current reaches its absolute theoretical maximum: $I_{\\max} = V_0 / R$.</li>
  <li>Current and voltage are perfectly in phase ($\phi = 0$, power factor $\cos\phi = 1$).</li>
</ol>

<h4>3. Quality Factor ($Q$) and Bandwidth</h4>
The Quality Factor $Q$ quantifies the sharpness and selectivity of resonance:
$$Q = \\frac{\\omega_0 L}{R} = \\frac{1}{\\omega_0 C R} = \\frac{1}{R}\\sqrt{\\frac{L}{C}}$$
The half-power bandwidth is $\\Delta\\omega = \\omega_2 - \\omega_1 = \\frac{R}{L} = \\frac{\\omega_0}{Q}$.
High $Q$ produces extreme selectivity, essential for radio tuning circuits."""
    },
    {
        "id": "sec-7-4",
        "number": "§7.4",
        "heading": "Power Dissipation in AC Circuits and Ideal Transformers",
        "simulation": "ac-rlc-resonance-sim",
        "content": """Unlike DC circuits where power is simply $P = V I$, AC power calculations must account for the phase angle between voltage and current.

<h4>1. Instantaneous and Real Average Power</h4>
Let $v(t) = V_0 \\sin(\\omega t)$ and $i(t) = I_0 \\sin(\\omega t - \\phi)$.
The instantaneous power is:
$$p(t) = v(t) i(t) = V_0 I_0 \\sin(\\omega t) [\\sin(\\omega t)\\cos\\phi - \\cos(\\omega t)\\sin\\phi]$$
$$p(t) = V_0 I_0 \\sin^2(\\omega t)\\cos\\phi - \\frac{1}{2} V_0 I_0 \\sin(2\\omega t)\\sin\\phi$$
Averaging over a complete cycle ($\langle \sin^2\omega t \rangle = 1/2$, $\langle \sin 2\omega t \rangle = 0$):
$$\\langle P \\rangle = \\frac{1}{2} V_0 I_0 \\cos\\phi = \\left(\\frac{V_0}{\\sqrt{2}}\\right) \\left(\\frac{I_0}{\\sqrt{2}}\\right) \\cos\\phi$$
$$\\langle P \\rangle = V_{\\text{rms}} I_{\\text{rms}} \\cos\\phi$$
where:
<ul>
  <li>$P$: <strong>Real (Active) Power</strong> dissipated as heat or mechanical work (Watts, W). Pure inductors and capacitors consume zero average real power!</li>
  <li>$S = V_{\\text{rms}} I_{\\text{rms}}$: <strong>Apparent Power</strong> (Volt-Amperes, VA).</li>
  <li>$Q_{\\text{react}} = V_{\\text{rms}} I_{\\text{rms}} \\sin\\phi$: <strong>Reactive Power</strong> surging back and forth between source and reactive fields (Volt-Amperes Reactive, VAR).</li>
  <li>$\\cos\\phi = \\frac{R}{Z}$: <strong>Power Factor</strong> ($0 \\le \\cos\\phi \\le 1$). Power companies mandate $\\cos\\phi \\ge 0.95$ using power factor correction capacitors to minimize transmission line $I^2 R$ heat losses.</li>
</ul>

<h4>2. The Ideal Transformer</h4>
A transformer consists of two coils (primary of $N_p$ turns and secondary of $N_s$ turns) wound around a common laminated ferromagnetic core.
Assuming zero flux leakage ($k = 1$) and zero resistance:
$$\\mathcal{E}_p = -N_p \\frac{d\\Phi_B}{dt}, \\quad \\mathcal{E}_s = -N_s \\frac{d\\Phi_B}{dt}$$
Dividing:
$$\\frac{V_s}{V_p} = \\frac{N_s}{N_p} = a \\quad (\\text{Transformation Ratio})$$
By energy conservation ($P_{\\text{in}} = P_{\\text{out}} \\implies V_p I_p = V_s I_s$):
$$\\frac{I_p}{I_s} = \\frac{V_s}{V_p} = \\frac{N_s}{N_p} = a \\implies I_s = \\frac{I_p}{a}$$
Impedance reflection: A load $R_L$ connected across the secondary reflects back to the primary as an equivalent impedance:
$$R_{\\text{in}} = \\frac{V_p}{I_p} = \\frac{V_s / a}{a I_s} = \\frac{1}{a^2}\\left(\\frac{V_s}{I_s}\\right) = \\frac{R_L}{a^2} = \\left(\\frac{N_p}{N_s}\\right)^2 R_L$$
This principle allows audio and RF engineers to achieve impedance matching for maximum power transfer."""
    }
]

u7_problems = [
    {
        "id": "prob-7-1",
        "difficulty": "Undergraduate Standard Classical Exam",
        "title": "Series LCR Resonance and Resonance Magnification",
        "question": "A series LCR circuit has resistance $R = 8.00\\ \\Omega$, inductance $L = 40.0\\text{ mH}$, and capacitance $C = 2.50\\ \\mu\\text{F}$. It is driven by an AC voltage source of amplitude $V_0 = 120.0\\text{ V}$ with variable angular frequency $\\omega$.\\n(a) Determine the resonant angular frequency $\\omega_0$ and linear frequency $f_0$,\\n(b) Calculate the Quality Factor $Q$ and half-power bandwidth $\\Delta f$, and\\n(c) At resonance, compute the peak current $I_0$ and the peak voltages across the inductor ($V_{L0}$) and capacitor ($V_{C0}$).",
        "steps": [
            {
                "title": "Step 1: Compute resonance frequency",
                "math": "$$\\omega_0 = \\frac{1}{\\sqrt{LC}} = \\frac{1}{\\sqrt{(40.0 \\times 10^{-3} \\text{ H}) \\times (2.50 \\times 10^{-6} \\text{ F})}} = \\frac{1}{\\sqrt{1.000 \\times 10^{-7}}} = \\frac{1}{3.1623 \\times 10^{-4}}$$\n$$\\omega_0 = 3162.3 \\text{ rad/s}$$\n$$f_0 = \\frac{\\omega_0}{2\\pi} = \\frac{3162.3}{2\\pi} = 503.3 \\text{ Hz}$$",
                "explanation": "The circuit resonates at 3162 rad/s (503.3 Hz)."
            },
            {
                "title": "Step 2: Calculate Quality Factor and bandwidth",
                "math": "$$Q = \\frac{\\omega_0 L}{R} = \\frac{(3162.3 \\text{ rad/s}) \\times (0.0400 \\text{ H})}{8.00\\ \\Omega} = \\frac{126.49}{8.00} = 15.81$$\n$$\\Delta f = \\frac{f_0}{Q} = \\frac{503.3 \\text{ Hz}}{15.81} = 31.83 \\text{ Hz}$$",
                "explanation": "A high Quality Factor of 15.8 corresponds to a narrow, sharp resonance bandwidth of 31.8 Hz."
            },
            {
                "title": "Step 3: Current and voltages at resonance",
                "math": "$$\\text{At resonance, } Z = R = 8.00\\ \\Omega:$$\n$$I_0 = \\frac{V_0}{R} = \\frac{120.0 \\text{ V}}{8.00\\ \\Omega} = 15.00 \\text{ A}$$\n$$X_{L0} = \\omega_0 L = 3162.3 \\times 0.0400 = 126.49\\ \\Omega$$\n$$V_{L0} = I_0 X_{L0} = 15.00 \\times 126.49 = 1897.4 \\text{ Volts}$$\n$$V_{C0} = I_0 X_{C0} = 1897.4 \\text{ Volts}$$\n$$\\frac{V_{L0}}{V_0} = \\frac{1897.4}{120.0} = 15.81 = Q$$",
                "explanation": "Notice the dramatic resonance voltage magnification: the inductor and capacitor each sustain 1.90 kV (nearly 16 times the 120 V supply voltage!)."
            }
        ]
    },
    {
        "id": "prob-7-2",
        "difficulty": "Industrial AC Engineering Problem",
        "title": "AC Power Factor Correction with Shunt Capacitance",
        "question": "A small factory operating on a $V_{\\text{rms}} = 240\\text{ V}$, $f = 50.0\\text{ Hz}$ single-phase AC supply draws real power $P = 12.0\\text{ kW}$ at a lagging power factor $\\cos\\phi_1 = 0.650$ due to induction motors.\\n(a) Determine the initial apparent power $S_1$, reactive power $Q_1$, and total line current $I_{\\text{rms,1}}$,\\n(b) What reactive power $Q_C$ must be supplied by a shunt power factor correction capacitor to raise the overall power factor to $\\cos\\phi_2 = 0.950$ (lagging), and\\n(c) Calculate the required capacitance $C$ of the capacitor and the reduction in supply line current.",
        "steps": [
            {
                "title": "Step 1: Compute initial uncompensated parameters",
                "math": "$$\\cos\\phi_1 = 0.650 \\implies \\phi_1 = \\arccos(0.650) = 49.458^\\circ, \\quad \\tan\\phi_1 = 1.1691$$\n$$S_1 = \\frac{P}{\\cos\\phi_1} = \\frac{12.0 \\text{ kW}}{0.650} = 18.462 \\text{ kVA}$$\n$$I_{\\text{rms,1}} = \\frac{S_1}{V_{\\text{rms}}} = \\frac{18462 \\text{ VA}}{240 \\text{ V}} = 76.92 \\text{ A}$$\n$$Q_1 = P \\tan\\phi_1 = 12.0 \\times 1.1691 = 14.029 \\text{ kVAR}$$",
                "explanation": "The motors draw 76.9 A of line current and 14.0 kVAR of lagging reactive power."
            },
            {
                "title": "Step 2: Determine target compensated parameters",
                "math": "$$\\cos\\phi_2 = 0.950 \\implies \\phi_2 = \\arccos(0.950) = 18.195^\\circ, \\quad \\tan\\phi_2 = 0.3287$$\n$$Q_2 = P \\tan\\phi_2 = 12.0 \\times 0.3287 = 3.944 \\text{ kVAR}$$\n$$Q_C = Q_1 - Q_2 = 14.029 - 3.944 = 10.085 \\text{ kVAR}$$",
                "explanation": "The capacitor must inject 10.09 kVAR of leading reactive power."
            },
            {
                "title": "Step 3: Calculate required capacitance and new line current",
                "math": "$$Q_C = V_{\\text{rms}}^2 \\omega C = V_{\\text{rms}}^2 (2\\pi f) C$$\n$$C = \\frac{Q_C}{2\\pi f V_{\\text{rms}}^2} = \\frac{10085 \\text{ VAR}}{2\\pi \\times 50.0 \\times (240)^2} = \\frac{10085}{314.16 \\times 57600} = \\frac{10085}{1.80956 \\times 10^7} = 5.573 \\times 10^{-4} \\text{ F} = 557 \\ \\mu\\text{F}$$\n$$I_{\\text{rms,2}} = \\frac{P}{V_{\\text{rms}} \\cos\\phi_2} = \\frac{12000}{240 \\times 0.950} = \\frac{12000}{228} = 52.63 \\text{ A}$$\n$$\\Delta I = 76.92 - 52.63 = 24.29 \\text{ A (31.6% line current reduction)}$$",
                "explanation": "Installing a 557 microfarad capacitor slashes supply current by 24.3 A, reducing cable $I^2 R$ heat losses by 53%."
            }
        ]
    },
    {
        "id": "prob-7-3",
        "difficulty": "Standard University Exam Problem",
        "title": "Step-Down Transformer Efficiency and Reflected Impedance",
        "question": "A step-down power distribution transformer has $N_p = 2400$ primary turns and $N_s = 200$ secondary turns. The primary connects to an AC line of $V_p = 2400\\text{ V}$ (RMS) at $50\\text{ Hz}$. The secondary delivers electrical power to a resistive heating load $R_L = 4.00\\ \\Omega$. Assume an ideal transformer with zero losses.\\n(a) Determine the secondary voltage $V_s$ and secondary load current $I_s$,\\n(b) Find the primary current $I_p$ and total power delivered, and\\n(c) Calculate the equivalent reflected load impedance $R_{\\text{in}}$ seen by the primary supply line.",
        "steps": [
            {
                "title": "Step 1: Compute secondary voltage and current",
                "math": "$$\\text{Turns ratio: } a = \\frac{N_s}{N_p} = \\frac{200}{2400} = \\frac{1}{12}$$\n$$V_s = a V_p = \\frac{1}{12} \\times 2400 \\text{ V} = 200.0 \\text{ Volts}$$\n$$I_s = \\frac{V_s}{R_L} = \\frac{200.0 \\text{ V}}{4.00\\ \\Omega} = 50.00 \\text{ Amperes}$$",
                "explanation": "The transformer steps down the 2400 V primary voltage to 200 V, delivering 50 A."
            },
            {
                "title": "Step 2: Primary current and delivered power",
                "math": "$$I_p = a I_s = \\left(\\frac{1}{12}\\right) \\times 50.00 \\text{ A} = 4.167 \\text{ Amperes}$$\n$$P = V_s I_s = 200.0 \\text{ V} \\times 50.00 \\text{ A} = 10000 \\text{ Watts} = 10.0 \\text{ kW}$$\n$$P_{\\text{primary}} = V_p I_p = 2400 \\text{ V} \\times 4.167 \\text{ A} = 10000 \\text{ Watts}$$",
                "explanation": "Primary draw is only 4.17 A while delivering 10.0 kW of power."
            },
            {
                "title": "Step 3: Reflected input impedance",
                "math": "$$R_{\\text{in}} = \\frac{V_p}{I_p} = \\frac{2400 \\text{ V}}{4.167 \\text{ A}} = 576.0\\ \\Omega$$\n$$\\text{Check via formula: } R_{\\text{in}} = \\left(\\frac{N_p}{N_s}\\right)^2 R_L = (12)^2 \\times 4.00 = 144 \\times 4.00 = 576.0\\ \\Omega$$\n$$\\text{Q.E.D.}$$",
                "explanation": "The 4-ohm secondary resistor is reflected into the primary circuit as an equivalent 576-ohm load."
            }
        ]
    }
]

unit7_data = {
    "number": 7,
    "title": "Alternating Current",
    "leadSummary": "AC generator dynamics, RMS and average effective values, response of pure resistive, inductive, and capacitive elements, phasor analysis and complex impedance, series LCR circuits, resonance sharpness and Quality factor, real and reactive power, power factor correction, and transformer physics.",
    "sections": u7_sections,
    "problems": u7_problems
}

with open("em_u7.json", "w") as f:
    json.dump(unit7_data, f, indent=2)

print("Unit 7 built successfully with", len(u7_sections), "sections and", len(u7_problems), "problems!")

# =========================================================================
# UNIT 8: Circuit Analysis & Network Theorems
# =========================================================================
u8_sections = [
    {
        "id": "sec-8-1",
        "number": "§8.1",
        "heading": "Thevenin's Theorem and Equivalent Voltage Generators",
        "simulation": "thevenin-norton-sim",
        "content": """Léon Charles Thévenin (1883) formulated one of the most powerful network reduction theorems in electrical engineering.

<h4>1. Statement of Thevenin's Theorem</h4>
<blockquote>
Any linear, bilateral, two-terminal electrical network containing independent voltage sources, current sources, and linear resistors can be replaced, across its two open terminals $A$ and $B$, by an equivalent circuit consisting of a single ideal voltage source $V_{\\text{th}}$ in series with a single internal resistance $R_{\\text{th}}$.
</blockquote>

<h4>2. Determination of Thevenin Parameters</h4>
<ol>
  <li><strong>Thevenin Equivalent Voltage ($V_{\\text{th}}$):</strong>
  The open-circuit potential difference appearing across terminals $A$ and $B$ when the load resistor $R_L$ is completely disconnected:
  $$V_{\\text{th}} = V_{AB,\\text{open}}$$</li>
  <li><strong>Thevenin Equivalent Resistance ($R_{\\text{th}}$):</strong>
  The equivalent resistance measured between terminals $A$ and $B$ with the load removed and all independent energy sources **deactivated**:
  <ul>
    <li>Independent voltage sources are replaced by **short circuits** (zero internal resistance, $V = 0$).</li>
    <li>Independent current sources are replaced by **open circuits** (infinite internal resistance, $I = 0$).</li>
  </ul>
  $$R_{\\text{th}} = R_{AB,\\text{deactivated}}$$</li>
</ol>

<h4>3. Calculation of Load Current and Voltage</h4>
When an arbitrary load resistance $R_L$ is connected across terminals $A$ and $B$, the load current $I_L$ and terminal voltage $V_L$ are given instantly by Ohm's law:
$$I_L = \\frac{V_{\\text{th}}}{R_{\\text{th}} + R_L}, \\quad V_L = I_L R_L = V_{\\text{th}} \\left( \\frac{R_L}{R_{\\text{th}} + R_L} \\right)$$
This eliminates the need to resolve the entire multi-loop system every time the load resistor changes."""
    },
    {
        "id": "sec-8-2",
        "number": "§8.2",
        "heading": "Norton's Theorem and Source Transformations",
        "simulation": "thevenin-norton-sim",
        "content": """Edward Lawry Norton (1926) independently established the dual current-source counterpart to Thevenin's theorem.

<h4>1. Statement of Norton's Theorem</h4>
<blockquote>
Any linear, bilateral, two-terminal electrical network can be replaced across its terminals by an equivalent circuit consisting of a single ideal current source $I_N$ connected in parallel with a single internal resistance $R_N$.
</blockquote>

<h4>2. Determination of Norton Parameters</h4>
<ol>
  <li><strong>Norton Equivalent Current ($I_N$):</strong>
  The short-circuit current that flows between terminals $A$ and $B$ when a zero-resistance conductor connects them:
  $$I_N = I_{AB,\\text{short}}$$</li>
  <li><strong>Norton Resistance ($R_N$):</strong>
  The equivalent resistance between terminals $A$ and $B$ with all independent sources deactivated.
  <em>Fundamental Identity:</em>
  $$R_N = R_{\\text{th}}$$</li>
</ol>

<h4>3. Thevenin-Norton Source Transformation Equivalence</h4>
Thevenin and Norton circuits are dual mathematical representations of the exact same physical reality:
$$V_{\\text{th}} = I_N R_{\\text{th}}, \\quad I_N = \\frac{V_{\\text{th}}}{R_{\\text{th}}}$$
For load resistor $R_L$:
By the current divider rule across parallel resistors $R_N$ and $R_L$:
$$I_L = I_N \\left( \\frac{R_N}{R_N + R_L} \\right) = \\left( \\frac{V_{\\text{th}}}{R_{\\text{th}}} \\right) \\left( \\frac{R_{\\text{th}}}{R_{\\text{th}} + R_L} \\right) = \\frac{V_{\\text{th}}}{R_{\\text{th}} + R_L}$$
Both theorems yield identical load current and voltage."""
    },
    {
        "id": "sec-8-3",
        "number": "§8.3",
        "heading": "The Superposition Theorem and Maximum Power Transfer",
        "simulation": "thevenin-norton-sim",
        "content": """Linear electrical networks obey the fundamental principles of superposition and impedance matching.

<h4>1. The Superposition Theorem</h4>
<blockquote>
In any linear, bilateral electrical network energized by multiple independent sources, the net current or voltage in any branch equals the algebraic sum of the currents or voltages produced by each independent source acting alone, with all other independent sources turned off.
</blockquote>
<ul>
  <li>Turn off independent voltage sources $\\to$ Replace with short circuits.</li>
  <li>Turn off independent current sources $\\to$ Replace with open circuits.</li>
</ul>
<em>Caution:</em> Superposition applies strictly to linear quantities (current and voltage: $I = I_1 + I_2$). It does **NOT** apply directly to power ($P \propto I^2 \ne I_1^2 + I_2^2$), because power is a quadratic, non-linear function of current!

<h4>2. The Maximum Power Transfer Theorem</h4>
Consider a linear source characterized by Thevenin equivalent parameters $V_{\\text{th}}$ and $R_{\\text{th}}$ driving an adjustable load resistance $R_L$.
The power delivered to the load resistor is:
$$P_L = I_L^2 R_L = \\left( \\frac{V_{\\text{th}}}{R_{\\text{th}} + R_L} \\right)^2 R_L = \\frac{V_{\\text{th}}^2 R_L}{(R_{\\text{th}} + R_L)^2}$$
To maximize power with respect to $R_L$, differentiate and set to zero:
$$\\frac{dP_L}{dR_L} = V_{\\text{th}}^2 \\left[ \\frac{(R_{\\text{th}} + R_L)^2 - 2 R_L (R_{\\text{th}} + R_L)}{(R_{\\text{th}} + R_L)^4} \\right] = 0$$
$$(R_{\\text{th}} + R_L) - 2 R_L = 0 \\implies R_{\\text{th}} - R_L = 0$$
$$R_L = R_{\\text{th}}$$
<em>Theorem:</em> A resistive load absorbs maximum power from a linear network when its resistance equals the Thevenin resistance of the network (**impedance matching**).
The maximum power delivered is:
$$P_{L,\\max} = \\frac{V_{\\text{th}}^2 R_{\\text{th}}}{(2 R_{\\text{th}})^2} = \\frac{V_{\\text{th}}^2}{4 R_{\\text{th}}}$$
<em>Efficiency at Maximum Power:</em>
$$\\eta = \\frac{P_{\\text{load}}}{P_{\\text{total}}} = \\frac{I_L^2 R_L}{I_L^2 (R_{\\text{th}} + R_L)} = \\frac{R_L}{2 R_L} = 50.0\\%$$
While essential in communications and weak-signal electronics to extract maximum signal power, maximum power transfer is deliberately avoided in electrical power grid distribution (where engineers aim for $R_L \\gg R_{\\text{th}}$ to achieve $> 98\\%$ transmission efficiency)."""
    },
    {
        "id": "sec-8-4",
        "number": "§8.4",
        "heading": "Transient Currents in Second-Order RLC Circuits",
        "simulation": "thevenin-norton-sim",
        "content": """When a circuit contains both inductive storage elements ($L$) and capacitive storage elements ($C$) along with damping resistance ($R$), its dynamic response is governed by a second-order linear differential equation.

<h4>1. The Governing Differential Equation</h4>
Applying Kirchhoff's voltage law to a series RLC loop discharging from initial charge $Q_0$:
$$L \\frac{di}{dt} + R i + \\frac{q}{C} = 0$$
Since $i = \\frac{dq}{dt}$:
$$L \\frac{d^2 q}{dt^2} + R \\frac{dq}{dt} + \\frac{1}{C} q = 0 \\implies \\frac{d^2 q}{dt^2} + 2\\gamma \\frac{dq}{dt} + \\omega_0^2 q = 0$$
where $\\gamma = \\frac{R}{2L}$ is the damping factor (s⁻¹) and $\\omega_0 = \\frac{1}{\\sqrt{LC}}$ is the natural undamped frequency.
Auxiliary equation:
$$\\lambda^2 + 2\\gamma \\lambda + \\omega_0^2 = 0 \\implies \\lambda = -\\gamma \\pm \\sqrt{\\gamma^2 - \\omega_0^2}$$

<h4>2. The Three Transient Regimes</h4>
<ol>
  <li><strong>Underdamped Oscillatory Regime ($R < 2\\sqrt{L/C} \\iff \\gamma < \\omega_0$):</strong>
  The roots are complex conjugates $\\lambda = -\\gamma \\pm i \\omega_d$, where $\\omega_d = \\sqrt{\\omega_0^2 - \\gamma^2}$.
  $$q(t) = Q_0 e^{-\\gamma t} \\cos(\\omega_d t + \\phi)$$
  The charge oscillates back and forth between capacitor plates while dying out exponentially.</li>
  <li><strong>Critically Damped Regime ($R = 2\\sqrt{L/C} \\iff \\gamma = \\omega_0$):</strong>
  $R_{\\text{crit}} = 2\\sqrt{\\frac{L}{C}}$.
  $$q(t) = (C_1 + C_2 t) e^{-\\gamma t}$$
  The capacitor discharges in the shortest possible time without ringing or overshoot.</li>
  <li><strong>Overdamped Aperiodic Regime ($R > 2\\sqrt{L/C} \\iff \\gamma > \\omega_0$):</strong>
  Two real negative roots. Non-oscillatory sluggish decay:
  $$q(t) = C_1 e^{-(\\gamma - \\sqrt{\\gamma^2-\\omega_0^2})t} + C_2 e^{-(\\gamma + \\sqrt{\\gamma^2-\\omega_0^2})t}$$</li>
</ol>"""
    }
]

u8_problems = [
    {
        "id": "prob-8-1",
        "difficulty": "Undergraduate Standard Classical Exam",
        "title": "Thevenin and Norton Equivalent Circuit of a Bridge T-Network",
        "question": "A linear DC circuit consists of an independent voltage source $\\mathcal{E} = 36.0\\text{ V}$ connected across a resistive T-network: resistor $R_1 = 12.0\\ \\Omega$ in series with the source, a shunt resistor $R_2 = 24.0\\ \\Omega$ across the line, and an output resistor $R_3 = 8.00\\ \\Omega$ leading to output terminals $A$ and $B$. A variable load resistor $R_L$ is connected between $A$ and $B$.\\n(a) Determine the Thevenin equivalent voltage $V_{\\text{th}}$ and Thevenin resistance $R_{\\text{th}}$,\\n(b) Find the Norton equivalent current $I_N$, and\\n(c) Calculate the load current $I_L$ and power dissipated in $R_L$ when $R_L = 16.0\\ \\Omega$.",
        "steps": [
            {
                "title": "Step 1: Determine Thevenin voltage and resistance",
                "math": "$$\\text{Open circuit across A-B: no current flows through } R_3.$$\n$$V_{\\text{th}} = V_{R2} = \\mathcal{E} \\left( \\frac{R_2}{R_1 + R_2} \\right) = 36.0 \\times \\left( \\frac{24.0}{12.0 + 24.0} \\right) = 36.0 \\times \\left(\\frac{24.0}{36.0}\\right) = 24.00 \\text{ Volts}$$\n$$\\text{Deactivate voltage source (short circuit): } R_1 \\text{ is in parallel with } R_2:$$\n$$R_{12} = \\frac{R_1 R_2}{R_1 + R_2} = \\frac{12.0 \\times 24.0}{12.0 + 24.0} = \\frac{288}{36.0} = 8.00\\ \\Omega$$\n$$R_{\\text{th}} = R_{12} + R_3 = 8.00 + 8.00 = 16.00\\ \\Omega$$",
                "explanation": "The entire network simplifies to a 24.0 V voltage source in series with 16.0 ohms."
            },
            {
                "title": "Step 2: Norton equivalent current",
                "math": "$$I_N = \\frac{V_{\\text{th}}}{R_{\\text{th}}} = \\frac{24.00 \\text{ V}}{16.00\\ \\Omega} = 1.500 \\text{ Amperes}$$\n$$R_N = R_{\\text{th}} = 16.00\\ \\Omega$$",
                "explanation": "The Norton equivalent is a 1.50 A current source in parallel with 16.0 ohms."
            },
            {
                "title": "Step 3: Load analysis for RL = 16.0 ohms",
                "math": "$$I_L = \\frac{V_{\\text{th}}}{R_{\\text{th}} + R_L} = \\frac{24.00 \\text{ V}}{16.00 + 16.00} = \\frac{24.00}{32.00} = 0.750 \\text{ A}$$\n$$P_L = I_L^2 R_L = (0.750 \\text{ A})^2 \\times 16.00\\ \\Omega = 0.5625 \\times 16.00 = 9.00 \\text{ Watts}$$",
                "explanation": "Because $R_L = R_{\\text{th}} = 16\\ \\Omega$, this represents the exact maximum power transfer condition ($P_{\\max} = 9.00$ W)."
            }
        ]
    },
    {
        "id": "prob-8-2",
        "difficulty": "Honors Circuit Analysis Standard",
        "title": "Superposition Theorem with Dual Independent Sources",
        "question": "A linear network contains an independent DC voltage source $\\mathcal{E}_1 = 28.0\\text{ V}$, an independent DC current source $I_s = 3.00\\text{ A}$, and three resistors: $R_1 = 4.00\\ \\Omega$, $R_2 = 6.00\\ \\Omega$, and $R_3 = 12.0\\ \\Omega$. The voltage source is in series with $R_1$. The current source is in parallel with $R_3$. Resistor $R_2$ connects between the common nodes.\\n(a) Use the Superposition Theorem to determine the current $I_2$ through resistor $R_2$ by activating each source individually, and\\n(b) Verify the result using nodal analysis.",
        "steps": [
            {
                "title": "Step 1: Case A - Voltage source alone (Current source opened)",
                "math": "$$\\text{Current source is open circuit. } R_2 \\text{ and } R_3 \\text{ are in series:}$$\n$$R_{23} = R_2 + R_3 = 6.00 + 12.0 = 18.0\\ \\Omega$$\n$$R_{\\text{total}} = R_1 + R_{23} = 4.00 + 18.0 = 22.0\\ \\Omega$$\n$$I_2' = \\frac{\\mathcal{E}_1}{R_{\\text{total}}} = \\frac{28.0 \\text{ V}}{22.0\\ \\Omega} = 1.2727 \\text{ A}$$",
                "explanation": "The voltage source acting alone drives 1.27 A through resistor $R_2$."
            },
            {
                "title": "Step 2: Case B - Current source alone (Voltage source shorted)",
                "math": "$$\\text{Voltage source is shorted to ground. } R_1 \\text{ and } R_2 \\text{ are in series across } R_3:$$\n$$R_{12} = R_1 + R_2 = 4.00 + 6.00 = 10.0\\ \\Omega$$\n$$\\text{By current divider rule, current splitting through the } (R_1+R_2) \\text{ branch:}$$\n$$I_2'' = -I_s \\left( \\frac{R_3}{R_{12} + R_3} \\right) = -3.00 \\times \\left( \\frac{12.0}{10.0 + 12.0} \\right) = -3.00 \\times \\left(\\frac{12.0}{22.0}\\right) = -1.6364 \\text{ A}$$",
                "explanation": "The current source drives 1.64 A in the opposite direction through $R_2$."
            },
            {
                "title": "Step 3: Algebraic superposition sum",
                "math": "$$I_2 = I_2' + I_2'' = 1.2727 - 1.6364 = -0.3636 \\text{ A} = -364 \\text{ mA}$$",
                "explanation": "Superposing the two states yields a net current of 364 mA flowing upward against the voltage source."
            }
        ]
    },
    {
        "id": "prob-8-3",
        "difficulty": "Second-Order RLC Transient Standard Exam",
        "title": "RLC Transient Oscillation and Critical Damping Resistance",
        "question": "A series RLC circuit has an inductor $L = 50.0\\text{ mH}$ and a capacitor $C = 2.00\\ \\mu\\text{F}$.\\n(a) Calculate the critical damping resistance $R_{\\text{crit}}$,\\n(b) If the actual resistance in the circuit is $R = 60.0\\ \\Omega$, determine whether the transient discharge is underdamped, overdamped, or critically damped, and\\n(c) Calculate the damped oscillation frequency $\\omega_d$ and the logarithmic decrement $\\delta$.",
        "steps": [
            {
                "title": "Step 1: Compute critical resistance and natural frequency",
                "math": "$$\\omega_0 = \\frac{1}{\\sqrt{LC}} = \\frac{1}{\\sqrt{(50.0 \\times 10^{-3} \\text{ H}) \\times (2.00 \\times 10^{-6} \\text{ F})}} = \\frac{1}{\\sqrt{1.000 \\times 10^{-7}}} = 3162.3 \\text{ rad/s}$$\n$$R_{\\text{crit}} = 2\\sqrt{\\frac{L}{C}} = 2\\sqrt{\\frac{50.0 \\times 10^{-3}}{2.00 \\times 10^{-6}}} = 2\\sqrt{25000} = 2 \\times 158.11 = 316.2\\ \\Omega$$",
                "explanation": "Critical damping requires a resistance of 316.2 ohms."
            },
            {
                "title": "Step 2: Regime identification for R = 60.0 ohms",
                "math": "$$R = 60.0\\ \\Omega < R_{\\text{crit}} = 316.2\\ \\Omega \\implies \\text{UNDERDAMPED OSCILLATORY REGIME}$$\n$$\\gamma = \\frac{R}{2L} = \\frac{60.0\\ \\Omega}{2 \\times (50.0 \\times 10^{-3} \\text{ H})} = \\frac{60.0}{0.100} = 600.0 \\text{ s}^{-1}$$",
                "explanation": "Because $R < R_{\\text{crit}}$, the circuit oscillates with decaying amplitude."
            },
            {
                "title": "Step 3: Damped frequency and logarithmic decrement",
                "math": "$$\\omega_d = \\sqrt{\\omega_0^2 - \\gamma^2} = \\sqrt{(3162.3)^2 - (600.0)^2} = \\sqrt{1.000 \\times 10^7 - 3.60 \\times 10^5} = \\sqrt{9.640 \\times 10^6} = 3104.8 \\text{ rad/s}$$\n$$f_d = \\frac{\\omega_d}{2\\pi} = \\frac{3104.8}{2\\pi} = 494.1 \\text{ Hz}$$\n$$T_d = \\frac{1}{f_d} = 2.0238 \\times 10^{-3} \\text{ s}$$\n$$\\delta = \\gamma T_d = 600.0 \\times (2.0238 \\times 10^{-3}) = 1.214$$",
                "explanation": "The circuit rings at 494 Hz with a logarithmic decrement $\delta = 1.21$."
            }
        ]
    }
]

unit8_data = {
    "number": 8,
    "title": "Circuit Analysis & Network Theorems",
    "leadSummary": "Comprehensive network analysis methods: Thevenin's theorem and equivalent voltage generators, Norton's theorem and dual current generators, the Superposition theorem, Maximum Power Transfer theorem with impedance matching proofs, and second-order RLC transient dynamics (underdamped, critically damped, overdamped).",
    "sections": u8_sections,
    "problems": u8_problems
}

with open("em_u8.json", "w") as f:
    json.dump(unit8_data, f, indent=2)

print("Unit 8 built successfully with", len(u8_sections), "sections and", len(u8_problems), "problems!")
