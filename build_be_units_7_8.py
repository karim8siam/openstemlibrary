import json

unit7 = {
    "id": "unit-7",
    "number": 7,
    "title": "Operational Amplifiers (Op-Amps) & Linear Analog Computing",
    "description": "Comprehensive mathematical exposition of operational amplifiers: ideal characteristics vs. practical silicon limits; the Virtual Ground theorem; inverting, non-inverting, and buffer topologies; summing adders, difference subtractors, and high-CMRR 3-op-amp instrumentation amplifiers; exact derivations and stability criteria for practical analog integrators and differentiators.",
    "sections": [
        {
            "id": "u7-sec1",
            "title": "Ideal Op-Amp Model, 741 Architecture & Virtual Ground Concept",
            "content": """<h4>1. Ideal Op-Amp Characteristics vs. Practical 741 IC</h4>
<p>An Operational Amplifier (Op-Amp) is a direct-coupled, high-gain differential voltage amplifier. The ideal op-amp model provides an indispensable mathematical abstraction for circuit analysis:</p>
<table class="data-table" style="width:100%; border-collapse:collapse; margin:16px 0;">
<thead>
<tr style="background:rgba(255,255,255,0.05); text-align:left;">
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Parameter</th>
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Ideal Value</th>
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Typical Practical IC (uA741)</th>
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Physical Implication</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);"><strong>Open-Loop Voltage Gain ($A_{OL}$)</strong></td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$A_{OL} \\to \\infty$</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$2 \\times 10^5$ ($106\\,\\text{dB}$)</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Differential input voltage is forced to near zero</td>
</tr>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);"><strong>Input Impedance ($R_{in}$)</strong></td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$R_{in} \\to \\infty$</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$2\\,\\text{M}\\Omega$ (BJT) / $10^{12}\\,\\Omega$ (FET)</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Draws zero current from driving source ($I^+ = I^- = 0$)</td>
</tr>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);"><strong>Output Impedance ($R_{out}$)</strong></td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$R_{out} = 0$</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$75\\,\\Omega$</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Can drive any load resistance without terminal voltage drop</td>
</tr>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);"><strong>Bandwidth ($BW$)</strong></td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$BW \\to \\infty$</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$1\\,\\text{MHz}$ (Unity Gain $f_T$)</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Amplifies signals uniformly from DC to high frequencies</td>
</tr>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);"><strong>Input Offset Voltage ($V_{os}$)</strong></td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$V_{os} = 0$</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$1\\text{ to }5\\,\\text{mV}$</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$V_o = 0$ when differential input is strictly zero</td>
</tr>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);"><strong>CMRR</strong></td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$\\text{CMRR} \\to \\infty$</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$90\\,\\text{dB}$</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Completely rejects common-mode noise and interference</td>
</tr>
</tbody>
</table>

<h4>2. The Golden Rules & Virtual Ground Principle</h4>
<p>In any linear op-amp circuit operating under <strong>negative feedback</strong> where output remains unclipped between the supply rails ($-V_{EE} < V_o < +V_{CC}$), two fundamental axioms (the <em>Golden Rules</em>) govern behavior:
<ol>
<li><strong>Axiom 1 (Virtual Short):</strong> The voltage difference between the inverting input ($-$) and non-inverting input ($+$) is infinitesimally small:
<div class="math-display">
$$V_d = V^+ - V^- = \\frac{V_o}{A_{OL}} \\xrightarrow{A_{OL} \\to \\infty} 0 \\implies V^- = V^+$$
</div>
When the non-inverting terminal is connected to physical ground ($V^+ = 0$), the inverting terminal is held at ground potential ($V^- = 0$) by the feedback loop. This node is termed a <strong>Virtual Ground</strong>: it has the potential of ground ($0\\,\\text{V}$), yet no current can flow directly to physical earth through the terminal.</li>
<li><strong>Axiom 2 (Zero Input Bias Current):</strong> Because input impedance is infinite ($R_{in} \\to \\infty$), no current enters either input terminal:
<div class="math-display">
$$I^+ = I^- = 0$$
</div>
All incoming signal currents are forced entirely into the feedback loop.</li>
</ol>
</p>"""
        },
        {
            "id": "u7-sec2",
            "title": "Fundamental Closed-Loop Configurations: Inverting, Non-Inverting & Buffer",
            "content": """<h4>1. Inverting Amplifier Configuration</h4>
<p>In the inverting amplifier, input voltage $v_{in}$ is applied through resistor $R_1$ to the inverting terminal ($-$), with feedback resistor $R_f$ connected from output $v_o$ back to the inverting terminal. The non-inverting terminal ($+$) is tied to ground ($V^+ = 0$).</p>
<p>By Axiom 1, $V^- = V^+ = 0\\,\\text{V}$ (virtual ground). Applying Kirchhoff's Current Law at the inverting summing node:</p>
<div class="math-display">
$$I_1 = I_f + I^-$$
</div>
<p>Since $I^- = 0$, $I_1 = I_f$:</p>
<div class="math-display">
$$\\frac{v_{in} - V^-}{R_1} = \\frac{V^- - v_o}{R_f} \\implies \\frac{v_{in} - 0}{R_1} = \\frac{0 - v_o}{R_f}$$
</div>
<p>Solving for the closed-loop voltage gain $A_v$:</p>
<div class="math-display">
$$A_v = \\frac{v_o}{v_{in}} = - \\frac{R_f}{R_1}$$
</div>
<p>The input impedance seen by the source is strictly $Z_{in} = R_1$. Output impedance is $Z_{out} \\approx 0$.</p>

<h4>2. Non-Inverting Amplifier Configuration</h4>
<p>In the non-inverting amplifier, input voltage $v_{in}$ is applied directly to the high-impedance non-inverting terminal ($+$), so $V^+ = v_{in}$. Resistors $R_1$ and $R_f$ form a voltage divider from output $v_o$ to ground, feeding the inverting node.</p>
<p>By Axiom 1, $V^- = V^+ = v_{in}$. Applying KCL at the inverting node:</p>
<div class="math-display">
$$\\frac{0 - V^-}{R_1} + \\frac{v_o - V^-}{R_f} = 0 \\implies \\frac{v_o - v_{in}}{R_f} = \\frac{v_{in}}{R_1}$$
</div>
<div class="math-display">
$$v_o = v_{in} \\left( 1 + \\frac{R_f}{R_1} \\right)$$
</div>
<p>Thus, the non-inverting gain is always positive and strictly $\\ge 1$:</p>
<div class="math-display">
$$A_v = \\frac{v_o}{v_{in}} = 1 + \\frac{R_f}{R_1}$$
</div>
<p>Input impedance is extremely high ($Z_{in} \\approx R_{in} (1 + A_{OL}\\beta) \\sim 10^{9}\\,\\Omega$ for BJT), preventing any loading on preceding stages.</p>

<h4>3. Voltage Follower (Unity-Gain Buffer)</h4>
<p>Setting $R_f = 0$ (direct short from output to inverting terminal) and $R_1 = \\infty$ (open circuit):</p>
<div class="math-display">
$$A_v = 1 + \\frac{0}{\\infty} = 1 \\implies v_o = v_{in}$$
</div>
<p>The voltage follower provides unity voltage gain, zero phase shift, astronomical input impedance ($Z_{in} \\to \\infty$), and near-zero output impedance ($Z_{out} \\to 0$). It acts as the universal impedance-matching buffer, isolating sensitive high-impedance sensors (such as pH glass electrodes or piezoelectric transducers) from low-impedance measuring loads.</p>"""
        },
        {
            "id": "u7-sec3",
            "title": "Linear Operations: Summing Adder & Difference Amplifier",
            "content": """<h4>1. Inverting Summing Amplifier (Analog Adder)</h4>
<p>Multiple input voltages $v_1, v_2, \\dots, v_n$ are connected through respective resistors $R_1, R_2, \\dots, R_n$ to the common inverting virtual ground node. Applying KCL:</p>
<div class="math-display">
$$I_1 + I_2 + \\dots + I_n = I_f$$
</div>
<div class="math-display">
$$\\frac{v_1 - 0}{R_1} + \\frac{v_2 - 0}{R_2} + \\dots + \\frac{v_n - 0}{R_n} = \\frac{0 - v_o}{R_f}$$
</div>
<p>Solving for output voltage $v_o$:</p>
<div class="math-display">
$$v_o = - \\left( \\frac{R_f}{R_1} v_1 + \\frac{R_f}{R_2} v_2 + \\dots + \\frac{R_f}{R_n} v_n \\right)$$
</div>
<p>If all input resistors are chosen equal ($R_1 = R_2 = \\dots = R_n = R$):</p>
<div class="math-display">
$$v_o = - \\frac{R_f}{R} (v_1 + v_2 + \\dots + v_n)$$
</div>
<p>By selecting binary-weighted resistor values ($R, 2R, 4R, 8R$), the summing amplifier operates as a digital-to-analog converter (DAC).</p>

<h4>2. Difference Subtractor Amplifier</h4>
<p>The difference amplifier rejects common-mode voltages and amplifies the differential voltage between two signals $v_1$ and $v_2$. Applying superposition or voltage division:</p>
<p>At non-inverting terminal ($+$): $V^+ = v_2 \\left( \\frac{R_4}{R_3 + R_4} \\right)$.</p>
<p>At inverting terminal ($-$), using virtual short $V^- = V^+$ and nodal analysis:</p>
<div class="math-display">
$$v_o = - \\frac{R_2}{R_1} v_1 + \\left( 1 + \\frac{R_2}{R_1} \\right) \\left( \\frac{R_4}{R_3 + R_4} \\right) v_2$$
</div>
<p>Setting the bridge balance condition $\\frac{R_2}{R_1} = \\frac{R_4}{R_3}$:</p>
<div class="math-display">
$$v_o = \\frac{R_2}{R_1} (v_2 - v_1)$$
</div>
<p>The circuit precisely subtracts $v_1$ from $v_2$ with differential gain $A_d = R_2 / R_1$. Any common-mode noise present equally on both leads cancels out.</p>

<h4>3. Three-Op-Amp Instrumentation Amplifier</h4>
<p>While the single op-amp difference amplifier is simple, its input impedances are low and asymmetrical ($Z_{in1} = R_1$, $Z_{in2} = R_3 + R_4$).</p>
<p>The <strong>Three-Op-Amp Instrumentation Amplifier</strong> overcomes this by placing two non-inverting buffers ($A_1, A_2$) before the differential stage ($A_3$). Differential gain is set by a single variable gain resistor $R_G$:</p>
<div class="math-display">
$$A_d = \\left( 1 + \\frac{2 R_1}{R_G} \\right) \\left( \\frac{R_3}{R_2} \\right)$$
</div>
<p>Common-mode signals pass through the input buffers with unity gain ($A_{cm,1} = 1$) while differential signals are heavily amplified, yielding common-mode rejection ratios exceeding $120\\,\\text{dB}$ with gigohm input impedances.</p>"""
        },
        {
            "id": "u7-sec4",
            "title": "Analog Integrator & Differentiator: Ideal vs. Practical Frequency Response",
            "content": """<h4>1. Ideal Op-Amp Integrator</h4>
<p>Replacing the feedback resistor $R_f$ with a capacitor $C$ in an inverting configuration yields an integrator. By virtual ground ($V^- = 0$):</p>
<div class="math-display">
$$i_{in}(t) = \\frac{v_{in}(t)}{R}, \\quad i_f(t) = C \\frac{d(0 - v_o)}{dt} = - C \\frac{d v_o}{dt}$$
</div>
<p>Equating currents $i_{in} = i_f$ and integrating from $t = 0$ to $t$:</p>
<div class="math-display">
$$v_o(t) = - \\frac{1}{R C} \\int_{0}^{t} v_{in}(\\tau)\\, d\\tau + v_o(0)$$
</div>
<p>In Laplace transform domain:</p>
<div class="math-display">
$$H(s) = \\frac{V_o(s)}{V_{in}(s)} = - \\frac{1}{s R C}$$
</div>
<p><strong>The DC Drift/Saturation Problem:</strong> At DC ($s \\to 0$ or $\\omega = 0$), capacitor impedance is infinite ($X_C \\to \\infty$). The op-amp operates open-loop with astronomical DC gain $A_{OL} \\sim 10^5$. Any minuscule input offset voltage $V_{os}$ or bias current $I_B$ charges the capacitor continually, driving the op-amp into saturation at $\\pm V_{sat}$ within seconds!</p>

<h4>2. Practical (Lossy) Integrator</h4>
<p>To prevent DC saturation, a large stabilizing resistor $R_f$ (typically $10 R$ to $100 R$) is placed in parallel with $C$. The transfer function becomes:</p>
<div class="math-display">
$$H(s) = - \\frac{R_f \\parallel \\frac{1}{sC}}{R} = - \\frac{ \\frac{R_f}{1 + s R_f C} }{R} = - \\frac{R_f / R}{1 + s R_f C}$$
</div>
<p>At DC ($\omega = 0$), the gain is securely clamped to a finite value $A_{dc} = - R_f / R$.</p>
<p>The lower corner frequency separating amplifier behavior from true integration is:</p>
<div class="math-display">
$$f_L = \\frac{1}{2\\pi R_f C}$$
</div>
<p>For input frequencies $f \\gg f_L$ (at least $10 f_L$), the capacitor impedance dominates $R_f$, and the circuit performs pure integration with a $-20\\,\\text{dB/decade}$ roll-off.</p>

<h4>3. Ideal vs. Practical Differentiator</h4>
<p>Inverting the positions—placing $C$ at input and $R$ in feedback—produces an ideal differentiator:</p>
<div class="math-display">
$$v_o(t) = - R C \\frac{d v_{in}}{dt}$$
</div>
<div class="math-display">
$$H(s) = - s R C \\implies |H(j\\omega)| = \\omega R C$$
</div>
<p><strong>The Noise and Instability Problem:</strong> Gain $|H(j\\omega)|$ increases linearly with frequency at $+20\\,\\text{dB/decade}$ indefinitely! High-frequency thermal noise, radio pickup, and power transients are amplified enormously, overwhelming the desired signal and causing parasitic oscillations.</p>
<p><strong>Practical Differentiator:</strong> A small resistor $R_1$ is added in series with $C$, and a small capacitor $C_f$ is placed in parallel with $R_f$. The high-frequency cutoff is set to:</p>
<div class="math-display">
$$f_H = \\frac{1}{2\\pi R_1 C} = \\frac{1}{2\\pi R_f C_f}$$
</div>
<p>For frequencies $f \\ll f_H$, the circuit differentiates cleanly; for frequencies $f > f_H$, the response rolls off at $-20\\,\\text{dB/decade}$, guaranteeing total high-frequency noise immunity and closed-loop stability.</p>"""
        }
    ],
    "problems": [
        {
            "id": "u7-prob1",
            "title": "Design of Analog Computing Linear Combination Circuit",
            "statement": "Using standard op-amps operating with dual \\pm 15\\,\\text{V} supplies and resistors in the range 10\\,\\text{k}\\Omega to 100\\,\\text{k}\\Omega, design an analog computing circuit that calculates the linear algebraic relation: v_o = 4 v_1 - 2 v_2 + 5 v_3. Specify the topology, draw the mathematical node equations, and compute all exact resistor values assuming a feedback resistor R_f = 100\\,\\text{k}\\Omega.",
            "solution": """<p><strong>Step 1: Circuit Topology Architecture</strong></p>
<p>Because an inverting summing amplifier produces an inverted sum $- (\\sum k_i v_i)$, we can invert $v_1$ and $v_3$ first using inverting unity/gain stages, or invert the output of a summing amplifier:</p>
<p>Rewrite $v_o$ in terms of an inverting sum:</p>
<div class="math-display">
$$v_o = - [ -4 v_1 + 2 v_2 - 5 v_3 ] = - [ 2 v_2 - (4 v_1 + 5 v_3) ]$$
</div>
<p>Alternatively, use a two-stage configuration:
Stage 1: Invert $v_2$ using a unity-gain inverting amplifier: $v_2' = - v_2$.
Stage 2: Feed $v_1, v_2', v_3$ into a four-input summing inverter where:</p>
<div class="math-display">
$$v_o = - \\left( - \\frac{R_f}{R_1} v_1 + \\frac{R_f}{R_2} v_2' - \\frac{R_f}{R_3} v_3 \\right) \\dots$$
</div>
<p>The cleanest approach:
1. Invert $v_1$ and $v_3$ with unity gain: $v_1^* = -v_1$, $v_3^* = -v_3$.
2. Sum $v_1^*, v_2, v_3^*$ into a standard inverting adder with feedback resistor $R_f = 100\\,\\text{k}\\Omega$:</p>
<div class="math-display">
$$v_o = - \\left( \\frac{R_f}{R_1} v_1^* + \\frac{R_f}{R_2} v_2 + \\frac{R_f}{R_3} v_3^* \\right) = - \\left( -\\frac{R_f}{R_1} v_1 + \\frac{R_f}{R_2} v_2 - \\frac{R_f}{R_3} v_3 \\right) = \\frac{R_f}{R_1} v_1 - \\frac{R_f}{R_2} v_2 + \\frac{R_f}{R_3} v_3$$
</div>

<p><strong>Step 2: Calculate Resistor Values for Stage 2 ($R_f = 100\\,\\text{k}\\Omega$)</strong></p>
<div class="math-display">
$$\\frac{R_f}{R_1} = 4 \\implies R_1 = \\frac{100\\,\\text{k}\\Omega}{4} = 25\\,\\text{k}\\Omega$$
</div>
<div class="math-display">
$$\\frac{R_f}{R_2} = 2 \\implies R_2 = \\frac{100\\,\\text{k}\\Omega}{2} = 50\\,\\text{k}\\Omega$$
</div>
<div class="math-display">
$$\\frac{R_f}{R_3} = 5 \\implies R_3 = \\frac{100\\,\\text{k}\\Omega}{5} = 20\\,\\text{k}\\Omega$$
</div>
<p>All resistors are standard values and fit comfortably within the specified $10\\,\\text{k}\\Omega - 100\\,\\text{k}\\Omega$ range.</p>"""
        },
        {
            "id": "u7-prob2",
            "title": "Three-Op-Amp Instrumentation Amplifier Gain & CMRR Analysis",
            "statement": "A biomedical electrocardiogram (ECG) data acquisition system uses a 3-op-amp instrumentation amplifier with R_1 = 25\\,\\text{k}\\Omega, R_2 = 10\\,\\text{k}\\Omega, and R_3 = 100\\,\\text{k}\\Omega. The gain-setting resistor is adjusted to R_G = 1.0\\,\\text{k}\\Omega. (a) Derive and calculate the overall differential voltage gain A_d, (b) If the differential biopotential signal is V_d = 2.5\\,\\text{mV}$ and a 50 Hz power-line hum common-mode interference of V_{cm} = 1.2\\,\\text{V}$ is present on both electrodes, find the differential output voltage, and (c) If the actual measured common-mode output is 2.4 mV, calculate the Common-Mode Rejection Ratio (CMRR) in decibels.",
            "solution": """<p><strong>Step 1: Calculate Differential Voltage Gain $A_d$</strong></p>
<p>Using the instrumentation amplifier gain formula:</p>
<div class="math-display">
$$A_d = \\left( 1 + \\frac{2 R_1}{R_G} \\right) \\times \\left( \\frac{R_3}{R_2} \\right)$$
</div>
<div class="math-display">
$$1 + \\frac{2(25\\,\\text{k}\\Omega)}{1.0\\,\\text{k}\\Omega} = 1 + \\frac{50}{1} = 51$$
</div>
<div class="math-display">
$$\\frac{R_3}{R_2} = \\frac{100\\,\\text{k}\\Omega}{10\\,\\text{k}\\Omega} = 10$$
</div>
<div class="math-display">
$$A_d = 51 \\times 10 = 510$$
</div>

<p><strong>Step 2: Calculate Differential Output Voltage</strong></p>
<div class="math-display">
$$V_{o,d} = A_d \\times V_d = 510 \\times 2.5\\,\\text{mV} = 1275\\,\\text{mV} = 1.275\\,\\text{V}$$
</div>

<p><strong>Step 3: Calculate Common-Mode Gain $A_{cm}$ and CMRR</strong></p>
<div class="math-display">
$$A_{cm} = \\frac{V_{o,cm}}{V_{cm}} = \\frac{2.4\\,\\text{mV}}{1.2\\,\\text{V}} = \\frac{2.4 \\times 10^{-3}}{1.2} = 2.0 \\times 10^{-3}$$
</div>
<div class="math-display">
$$\\text{CMRR} = \\frac{A_d}{|A_{cm}|} = \\frac{510}{2.0 \\times 10^{-3}} = 255,000$$
</div>
<div class="math-display">
$$\\text{CMRR}(\\text{dB}) = 20 \\log_{10}(255,000) \\approx 20 \\times 5.4065 = 108.13\\,\\text{dB}$$
</div>
<p>The amplifier attenuates the 1.2 V hum to negligible levels while cleanly boosting the tiny 2.5 mV heart signal to 1.275 V.</p>"""
        },
        {
            "id": "u7-prob3",
            "title": "Practical Analog Integrator Waveform & Frequency Response",
            "statement": "A practical op-amp integrator has R = 10\\,\\text{k}\\Omega, C = 0.01\\,\\mu\\text{F}$, and feedback stabilizing resistor R_f = 100\\,\\text{k}\\Omega. (a) Determine the DC gain of the integrator, (b) Calculate the lower corner frequency f_L, (c) If a 5 kHz square wave of peak-to-peak amplitude 4 V (symmetrical \\pm 2\\,\\text{V}) with zero DC offset is applied, verify that the circuit integrates cleanly, and (d) Calculate the peak-to-peak amplitude and waveform shape of the resulting output signal.",
            "solution": """<p><strong>Step 1: Calculate DC Gain and Corner Frequency $f_L$</strong></p>
<div class="math-display">
$$A_{dc} = - \\frac{R_f}{R} = - \\frac{100\\,\\text{k}\\Omega}{10\\,\\text{k}\\Omega} = -10 \\quad (20\\,\\text{dB})$$
</div>
<div class="math-display">
$$f_L = \\frac{1}{2\\pi R_f C} = \\frac{1}{2\\pi \\times 10^5\\,\\Omega \\times 10^{-8}\\,\\text{F}} = \\frac{1}{2\\pi \\times 10^{-3}} = \\frac{1000}{6.2832} \\approx 159.15\\,\\text{Hz}$$
</div>

<p><strong>Step 2: Integration Validity Check</strong></p>
<p>The input frequency is $f = 5000\\,\\text{Hz}$. Since $f / f_L = 5000 / 159.15 \\approx 31.4 \\gg 10$, the input operates well into the pure integration $-20\\,\\text{dB/decade}$ band.</p>

<p><strong>Step 3: Output Waveform Shape & Amplitude</strong></p>
<p>The integral of a symmetrical square wave is a symmetrical triangular wave. For a square wave of frequency $f = 5\\,\\text{kHz}$, the half-period duration is:</p>
<div class="math-display">
$$\\frac{T}{2} = \\frac{1}{2 \\times 5000\\,\\text{s}} = 0.1\\,\\text{ms} = 100\\,\\mu\\text{s}$$
</div>
<p>During the positive half-cycle ($v_{in} = +2\\,\\text{V}$), output ramps downward linearly with constant slope:</p>
<div class="math-display">
$$\\frac{dv_o}{dt} = - \\frac{v_{in}}{R C} = - \\frac{2\\,\\text{V}}{(10^4\\,\\Omega)(10^{-8}\\,\\text{F})} = - \\frac{2}{10^{-4}} = -20,000\\,\\text{V/s}$$
</div>
<p>The change in output voltage during this half-period is the peak-to-peak triangular amplitude $\\Delta V_{o,pp}$:</p>
<div class="math-display">
$$\\Delta V_{o,pp} = \\left| \\frac{dv_o}{dt} \\right| \\times \\frac{T}{2} = (20,000\\,\\text{V/s}) \\times (100 \\times 10^{-6}\\,\\text{s}) = 2.0\\,\\text{V}$$
</div>
<p>The output is an unclipped, pure triangular wave of $2.0\\,\\text{V}$ peak-to-peak ($\pm 1.0\\,\\text{V}$ peak).</p>"""
        }
    ]
}

unit8 = {
    "id": "unit-8",
    "number": 8,
    "title": "Nonlinear Op-Amp Circuits, Schmitt Triggers & Active Filters",
    "description": "Comprehensive theory of nonlinear operational amplifier applications: open-loop voltage comparators, zero-crossing detectors, and slew-rate limits; positive-feedback Schmitt Triggers with analytical hysteresis loop derivations; active square/triangular waveform generators; detailed design of first- and second-order Sallen-Key Butterworth active filters.",
    "sections": [
        {
            "id": "u8-sec1",
            "title": "Open-Loop Comparators, Zero-Crossing Detectors & Slew Rate Limits",
            "content": """<h4>1. Voltage Comparator Operation and Transfer Characteristics</h4>
<p>An open-loop operational amplifier without negative feedback functions as a <strong>Voltage Comparator</strong>. Because open-loop gain is colossal ($A_{OL} \\sim 10^5$), an infinitesimally small differential input voltage $\\Delta V = v^+ - v^-$ drives the output into hard saturation at the power supply rails:</p>
<div class="math-display">
$$v_o = \\begin{cases} +V_{sat} \\approx V_{CC} - 1.5\\,\\text{V} & \\text{if } v^+ > v^- \\\\ -V_{sat} \\approx -V_{EE} + 1.5\\,\\text{V} & \\text{if } v^+ < v^- \\end{cases}$$
</div>
<p>A reference voltage $V_{ref}$ applied to one terminal establishes the threshold. When an analog signal crosses $V_{ref}$, the output transitions cleanly between binary saturation rails, acting as an analog-to-digital 1-bit converter.</p>

<h4>2. Zero-Crossing Detector & Noise Chattering Problem</h4>
<p>When $V_{ref} = 0\\,\\text{V}$, the circuit is a <strong>Zero-Crossing Detector</strong>, converting any arbitrary AC waveform (such as a sine wave) into a synchronous square wave.</p>
<p><strong>The Chattering Problem:</strong> In practical industrial environments, real-world input signals contain high-frequency noise spikes. As a slowly moving signal passes through $0\\,\\text{V}$, noise causes multiple rapid false crossings above and below zero. The comparator output chatters uncontrollably, firing dozens of false pulses per cycle. To eliminate this chattering, <em>positive feedback</em> is introduced to create hysteresis.</p>

<h4>3. Slew Rate and Full-Power Bandwidth</h4>
<p>The switching speed of an op-amp is fundamentally constrained by its <strong>Slew Rate ($SR$)</strong>: the maximum rate of change of output voltage per unit time that the internal compensation capacitor can sustain when driven by the input differential stage's tail current source ($I_{tail}$):</p>
<div class="math-display">
$$SR = \\left. \\frac{d v_o}{dt} \\right|_{max} = \\frac{I_{tail}}{C_c} \\quad (\\text{expressed in } \\text{V}/\\mu\\text{s})$$
</div>
<p>For a sinusoidal output $v_o(t) = V_m \\sin(2\\pi f t)$, the maximum slope occurs at the zero-crossing:</p>
<div class="math-display">
$$\\left. \\frac{d v_o}{dt} \\right|_{max} = 2\\pi f V_m$$
</div>
<p>To avoid severe triangular distortion (slew-rate limiting), this slope must not exceed $SR$:</p>
<div class="math-display">
$$2\\pi f V_m \\le SR \\implies f_{max} = \\frac{SR}{2\\pi V_m}$$
</div>
<p>The frequency $f_{max}$ is the <strong>Full-Power Bandwidth</strong> of the op-amp. For a $\\mu\\text{A}741$ with $SR = 0.5\\,\\text{V}/\\mu\\text{s}$ and $V_m = 10\\,\\text{V}$, $f_{max} = \\frac{0.5 \\times 10^6}{2\\pi \\times 10} \\approx 7.96\\,\\text{kHz}$. Above this frequency, full-amplitude sine waves distort into triangles.</p>"""
        },
        {
            "id": "u8-sec2",
            "title": "Schmitt Trigger (Regenerative Comparator) & Hysteresis Loops",
            "content": """<h4>1. Positive Feedback Mechanism and Regenerative Action</h4>
<p>A <strong>Schmitt Trigger</strong> incorporates positive feedback by routing a fraction of the output voltage back to the <em>non-inverting ($+$) terminal</em>. This creates two distinct switching thresholds, imparting memory (hysteresis) to the system.</p>

<h4>2. Inverting Schmitt Trigger Equations</h4>
<p>In an inverting Schmitt trigger, the input signal $v_{in}$ is applied to the inverting terminal ($-$). The non-inverting terminal ($+$) is connected to a resistive voltage divider ($R_1, R_2$) from output $v_o$ to ground. The potential at the non-inverting terminal is:</p>
<div class="math-display">
$$V^+ = \\frac{R_1}{R_1 + R_2} v_o$$
</div>
<p>Since $v_o$ can only assume $+V_{sat}$ or $-V_{sat}$, there exist two distinct trip thresholds:
<ol>
<li><strong>Upper Trip Point ($V_{UTP}$):</strong> When $v_o = +V_{sat}$, the reference threshold is:
<div class="math-display">
$$V_{UTP} = + \\frac{R_1}{R_1 + R_2} V_{sat}$$
</div>
The output remains clamped at $+V_{sat}$ until $v_{in}$ rises above $V_{UTP}$, at which instant regenerative switching snaps the output to $-V_{sat}$.</li>
<li><strong>Lower Trip Point ($V_{LTP}$):</strong> Once $v_o = -V_{sat}$, the reference threshold switches to:
<div class="math-display">
$$V_{LTP} = - \\frac{R_1}{R_1 + R_2} V_{sat}$$
</div>
The output cannot return to $+V_{sat}$ until $v_{in}$ falls below $V_{LTP}$.</li>
</ol>
</p>
<p>The width of the hysteresis loop is the <strong>Hysteresis Voltage $\\Delta V_H$</strong>:</p>
<div class="math-display">
$$\\Delta V_H = V_{UTP} - V_{LTP} = \\frac{2 R_1}{R_1 + R_2} V_{sat}$$
</div>
<p>Any noise riding on the input with peak-to-peak amplitude less than $\\Delta V_H$ is completely ignored, providing total immunity to false triggering.</p>

<h4>3. Astable Relaxation Multivibrator (Square-Wave Generator)</h4>
<p>By connecting an external $RC$ timing network between the output and inverting terminal of a Schmitt trigger, a free-running relaxation oscillator is formed:</p>
<p>The output square wave charges capacitor $C$ toward $\\pm V_{sat}$ through resistor $R$. As soon as $v_C(t)$ reaches the trip threshold, the Schmitt trigger snaps to the opposite rail, and $C$ begins charging in reverse. The period of oscillation is:</p>
<div class="math-display">
$$T = 2 R C \\ln\\left( \\frac{1 + \\beta}{1 - \\beta} \\right) \\quad \\text{where } \\beta = \\frac{R_1}{R_1 + R_2}$$
</div>
<p>If resistors are chosen such that $R_1 = 0.86 R_2$ ($\beta \\approx 0.462$):</p>
<div class="math-display">
$$\\ln\\left(\\frac{1 + 0.462}{1 - 0.462}\\right) = \\ln(2.718) = 1.00 \\implies T = 2 R C \\implies f_0 = \\frac{1}{2 R C}$$
</div>"""
        },
        {
            "id": "u8-sec3",
            "title": "Active Filter Fundamentals: Butterworth, Chebyshev & Bessel Responses",
            "content": """<h4>1. Advantages of Active Filters over Passive Networks</h4>
<p>Active filters combine operational amplifiers with resistors and capacitors (no inductors required). They provide decisive advantages over passive RLC filters:
<ul>
<li><strong>Elimination of Bulky Inductors:</strong> Inductors are heavy, lossy, expensive, and act as antennas picking up 50/60 Hz magnetic hum. At audio frequencies ($< 20\\,\\text{kHz}$), required inductors are several henries in size.</li>
<li><strong>Impedance Isolation:</strong> High input impedance and near-zero output impedance mean active filter stages can be cascaded without loading effects altering their cutoff points.</li>
<li><strong>Gain Flexibility:</strong> Built-in passband voltage amplification and buffering.</li>
<li><strong>Simple Tunability:</strong> Cutoff frequencies can be adjusted smoothly over decades using dual-ganged potentiometers.</li>
</ul>
</p>

<h4>2. Classic Filter Approximations</h4>
<table class="data-table" style="width:100%; border-collapse:collapse; margin:16px 0;">
<thead>
<tr style="background:rgba(255,255,255,0.05); text-align:left;">
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Response Type</th>
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Passband Characteristic</th>
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Transition Roll-off</th>
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Phase Linearity</th>
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Applications</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);"><strong>Butterworth</strong></td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Maximally flat; zero ripple</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Moderate ($-20n\\,\\text{dB/decade}$)</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Moderate phase distortion</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Precision audio, biomedical instrumentation, anti-aliasing</td>
</tr>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);"><strong>Chebyshev</strong></td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Equiripple (e.g. 0.5 dB, 1 dB)</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Extremely steep skirt transition</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Severe nonlinear phase distortion</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">RF channel selectivity where frequency skirt matters most</td>
</tr>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);"><strong>Bessel</strong></td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Drooping gradual rolloff</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Slowest transition</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Strictly linear phase; constant group delay</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Digital pulse transmission, radar, pulse-code modulation (zero ringing)</td>
</tr>
</tbody>
</table>"""
        },
        {
            "id": "u8-sec4",
            "title": "First- & Second-Order Sallen-Key Active Butterworth Filters",
            "content": """<h4>1. First-Order Active Filters</h4>
<p>A first-order active low-pass filter comprises a passive $RC$ low-pass network feeding a non-inverting op-amp with gain $A_0 = 1 + R_f / R_1$:</p>
<div class="math-display">
$$H(s) = \\frac{A_0}{1 + s R C} = \\frac{A_0}{1 + s / \\omega_c}$$
</div>
<p>Cutoff frequency where gain drops by $3\\,\\text{dB}$:</p>
<div class="math-display">
$$f_c = \\frac{1}{2\\pi R C}$$
</div>
<p>Beyond $f_c$, the gain falls off at a gentle slope of <strong>$-20\\,\\text{dB/decade}$ ($-6\\,\\text{dB/octave}$)</strong>.</p>

<h4>2. Second-Order Sallen-Key Low-Pass Filter Topology</h4>
<p>To double the roll-off sharpness to <strong>$-40\\,\\text{dB/decade}$ ($-12\\,\\text{dB/octave}$)</strong>, a second-order Sallen-Key topology is employed. It utilizes two resistors ($R_1, R_2$) and two capacitors ($C_1, C_2$) with positive feedback through $C_1$ bootstrap.</p>
<p>The general transfer function is:</p>
<div class="math-display">
$$H(s) = \\frac{A_0 \\, \\omega_0^2}{s^2 + 2 \\zeta \\omega_0 s + \\omega_0^2} = \\frac{A_0 \\, \\omega_0^2}{s^2 + \\alpha \\omega_0 s + \\omega_0^2}$$
</div>
<p>where $\\alpha = 2\\zeta = 1/Q$ is the damping factor.</p>

<h4>3. Equal-Component Butterworth Design Derivation</h4>
<p>For an equal-component design where $R_1 = R_2 = R$ and $C_1 = C_2 = C$:</p>
<div class="math-display">
$$\\omega_0 = \\frac{1}{R C} \\implies f_c = \\frac{1}{2\\pi R C}$$
</div>
<p>The damping coefficient is set by the op-amp passband gain $A_0 = 1 + R_f / R_A$:</p>
<div class="math-display">
$$\\alpha = 3 - A_0$$
</div>
<p>For a maximally flat <strong>Butterworth response</strong>, the required damping coefficient is:</p>
<div class="math-display">
$$\\alpha = \\sqrt{2} \\approx 1.4142 \\quad (Q = \\frac{1}{\\sqrt{2}} \\approx 0.7071)$$
</div>
<p>Equating coefficients:</p>
<div class="math-display">
$$3 - A_0 = \\sqrt{2} \\implies A_0 = 3 - \\sqrt{2} \\approx 1.5858$$
</div>
<p>Therefore, the ratio of gain resistors must be strictly set to:</p>
<div class="math-display">
$$\\frac{R_f}{R_A} = A_0 - 1 = 0.5858$$
</div>
<p>If $A_0 > 1.586$, the circuit exhibits Chebyshev peaking and ringing; if $A_0 \\ge 3$, the damping factor becomes zero or negative, causing the filter to burst into spontaneous oscillation!</p>"""
        }
    ],
    "problems": [
        {
            "id": "u8-prob1",
            "title": "Op-Amp Slew Rate & Full-Power Bandwidth Limitation",
            "statement": "An operational amplifier has a specified slew rate of SR = 2.0\\,\\text{V}/\\mu\\text{s}$. (a) If the op-amp is configured as an amplifier delivering a sinusoidal output of peak voltage V_m = 8.0\\,\\text{V}$, calculate the maximum unclipped signal frequency (full-power bandwidth f_{max}), (b) If an input signal of frequency f = 80\\,\\text{kHz} is applied, what is the maximum peak output voltage V_{m,max} achievable without slew-rate induced triangular distortion, and (c) If a 10 V step voltage is applied, what is the minimum transition rise time (10% to 90%)?",
            "solution": """<p><strong>Step 1: Calculate Full-Power Bandwidth $f_{max}$</strong></p>
<p>For an $8.0\\,\\text{V}$ peak sinusoidal signal ($16\\,\\text{V}$ peak-to-peak):</p>
<div class="math-display">
$$2\\pi f_{max} V_m = SR = 2.0\\,\\text{V}/\\mu\\text{s} = 2.0 \\times 10^6\\,\\text{V/s}$$
</div>
<div class="math-display">
$$f_{max} = \\frac{SR}{2\\pi V_m} = \\frac{2.0 \\times 10^6}{2\\pi \\times 8.0} = \\frac{2.0 \\times 10^6}{50.265} \\approx 39,789\\,\\text{Hz} \\approx 39.79\\,\\text{kHz}$$
</div>

<p><strong>Step 2: Calculate Maximum Voltage at $f = 80\\,\\text{kHz}$</strong></p>
<div class="math-display">
$$V_{m,max} = \\frac{SR}{2\\pi f} = \\frac{2.0 \\times 10^6\\,\\text{V/s}}{2\\pi \\times 80,000\\,\\text{s}^{-1}} = \\frac{2.0 \\times 10^6}{502,655} \\approx 3.98\\,\\text{V}$$
</div>
<p>At $80\\,\\text{kHz}$, attempting to drive the output past $3.98\\,\\text{V}$ peak will cause the sine wave to distort into a triangle.</p>

<p><strong>Step 3: Calculate Transition Rise Time for 10 V Step</strong></p>
<p>The voltage change between 10% and 90% of a 10 V step is $\\Delta V = 0.8 \\times 10\\,\\text{V} = 8.0\\,\\text{V}$:</p>
<div class="math-display">
$$t_r = \\frac{\\Delta V}{SR} = \\frac{8.0\\,\\text{V}}{2.0\\,\\text{V}/\\mu\\text{s}} = 4.0\\,\\mu\\text{s}$$
</div>"""
        },
        {
            "id": "u8-prob2",
            "title": "Inverting Schmitt Trigger Design with Specified Trip Points",
            "statement": "Design an inverting Schmitt trigger using an operational amplifier with supply rails of \\pm 15\\,\\text{V} (assume saturation levels \\pm V_{sat} = \\pm 13.5\\,\\text{V}). The specifications require an Upper Trip Point V_{UTP} = +3.0\\,\\text{V}$ and a Lower Trip Point V_{LTP} = -3.0\\,\\text{V}$. (a) Calculate the required hysteresis voltage \\Delta V_H, (b) Find the ratio of feedback resistors R_1 / R_2, and (c) If R_1 is chosen as 10\\,\\text{k}\\Omega, calculate the exact value of R_2 and the input noise immunity margin.",
            "solution": """<p><strong>Step 1: Calculate Hysteresis Voltage $\\Delta V_H$</strong></p>
<div class="math-display">
$$\\Delta V_H = V_{UTP} - V_{LTP} = (+3.0\\,\\text{V}) - (-3.0\\,\\text{V}) = 6.0\\,\\text{V}$$
</div>

<p><strong>Step 2: Derive and Calculate Feedback Resistor Ratio</strong></p>
<p>Using the trip point relation:</p>
<div class="math-display">
$$V_{UTP} = \\frac{R_1}{R_1 + R_2} V_{sat}$$
</div>
<div class="math-display">
$$3.0 = \\frac{R_1}{R_1 + R_2} (13.5) \\implies \\frac{R_1 + R_2}{R_1} = \\frac{13.5}{3.0} = 4.5$$
</div>
<div class="math-display">
$$1 + \\frac{R_2}{R_1} = 4.5 \\implies \\frac{R_2}{R_1} = 3.5$$
</div>

<p><strong>Step 3: Component Values and Noise Margin</strong></p>
<p>Given $R_1 = 10\\,\\text{k}\\Omega$:</p>
<div class="math-display">
$$R_2 = 3.5 \\times R_1 = 3.5 \\times 10\\,\\text{k}\\Omega = 35\\,\\text{k}\\Omega$$
</div>
<p>Noise Immunity: Any spurious noise spikes riding on the input waveform with peak-to-peak amplitude less than $\\Delta V_H = 6.0\\,\\text{V}$ are completely suppressed, guaranteeing 100% chatter-free digital state transitions.</p>"""
        },
        {
            "id": "u8-prob3",
            "title": "Second-Order Sallen-Key Butterworth Low-Pass Filter Design",
            "statement": "Design a second-order Sallen-Key low-pass filter with a maximally flat Butterworth response having a cutoff frequency f_c = 2.5\\,\\text{kHz}$. Using the equal-component architecture with standard capacitors C_1 = C_2 = 0.01\\,\\mu\\text{F}$: (a) Calculate the required resistance values R_1 = R_2 = R, (b) Determine the required passband gain A_0 and feedback resistor ratio R_f / R_A, (c) If R_A = 10\\,\\text{k}\\Omega, calculate R_f, and (d) Calculate the filter attenuation in decibels at a frequency f = 25\\,\\text{kHz} (one decade above cutoff).",
            "solution": """<p><strong>Step 1: Calculate Filter Resistors $R_1 = R_2 = R$</strong></p>
<p>Using the equal-component cutoff frequency formula:</p>
<div class="math-display">
$$f_c = \\frac{1}{2\\pi R C} \\implies R = \\frac{1}{2\\pi f_c C}$$
</div>
<div class="math-display">
$$R = \\frac{1}{2\\pi \\times 2500\\,\\text{Hz} \\times 0.01 \\times 10^{-6}\\,\\text{F}} = \\frac{1}{2\\pi \\times 2.5 \\times 10^{-5}} = \\frac{10^5}{5\\pi} = \\frac{20,000}{\\pi} \\approx 6366.2\\,\\Omega \\approx 6.37\\,\\text{k}\\Omega$$
</div>
<p>Standard precision resistors of $6.34\\,\\text{k}\\Omega$ (1% metal film) can be used.</p>

<p><strong>Step 2: Determine Passband Gain and Feedback Resistors</strong></p>
<p>For a maximally flat Butterworth response ($\alpha = \sqrt{2} = 1.414$):</p>
<div class="math-display">
$$A_0 = 3 - \\sqrt{2} = 3 - 1.4142 = 1.5858$$
</div>
<div class="math-display">
$$A_0 = 1 + \\frac{R_f}{R_A} \\implies \\frac{R_f}{R_A} = 0.5858$$
</div>
<p>With $R_A = 10\\,\\text{k}\\Omega$:</p>
<div class="math-display">
$$R_f = 0.5858 \\times 10\\,\\text{k}\\Omega = 5.858\\,\\text{k}\\Omega \\approx 5.86\\,\\text{k}\\Omega$$
</div>

<p><strong>Step 3: Attenuation at $f = 25\\,\\text{kHz}$</strong></p>
<p>At $f = 25\\,\\text{kHz}$, the normalized frequency ratio is $f / f_c = 25000 / 2500 = 10$ (exactly one decade above cutoff).</p>
<p>For a second-order Butterworth filter, magnitude response is:</p>
<div class="math-display">
$$|H(j\\omega)| = \\frac{A_0}{\\sqrt{1 + (f/f_c)^4}} = \\frac{1.5858}{\\sqrt{1 + 10^4}} = \\frac{1.5858}{\\sqrt{10001}} \\approx \\frac{1.5858}{100.005} \\approx 0.015857$$
</div>
<p>Attenuation relative to passband gain $A_0$ is:</p>
<div class="math-display">
$$\\text{Attenuation}(\\text{dB}) = 20 \\log_{10}\\left(\\frac{1}{\\sqrt{1 + 10^4}}\\right) \\approx -20 \\log_{10}(100) = -40.0\\,\\text{dB}$$
</div>
<p>The filter attenuates signals at $25\\,\\text{kHz}$ by exactly $40\\,\\text{dB}$ (a 100-fold reduction in voltage).</p>"""
        }
    ]
}

with open("be_u7.json", "w") as f:
    json.dump(unit7, f, indent=2)

with open("be_u8.json", "w") as f:
    json.dump(unit8, f, indent=2)

print("be_u7.json and be_u8.json generated successfully!")
