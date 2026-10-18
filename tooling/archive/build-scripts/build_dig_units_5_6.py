import json

# ==========================================
# UNIT 5: Counters, Shift Registers & Combinational MSI Subsystems
# ==========================================
u5 = {
    "unitNumber": 5,
    "unitId": "unit5-counters-registers-msi",
    "title": "Counters, Shift Registers & Combinational MSI Subsystems",
    "description": "Comprehensive design and operational analysis of medium-scale integrated (MSI) digital building blocks: asynchronous (ripple) up/down counters, propagation delay accumulation, and MOD-N reset truncation; systematic synchronous counter synthesis via excitation tables, state transition graphs, and lockout protection; shift register architectures (SISO, SIPO, PISO, PIPO, universal bidirectional), Ring and Johnson twisted counters; decoders (3-to-8, BCD-to-7-segment), priority encoders, multiplexers as universal logic modules, and demultiplexers.",
    "sections": [
        {
            "id": "dig-5-1",
            "title": "Asynchronous (Ripple) Counters & MOD-N Truncation",
            "content": r"""<h4>1. Working Principle of Asynchronous (Ripple) Counters</h4>
<p>An <strong>asynchronous counter</strong> (or ripple counter) consists of a cascade of toggle flip-flops (T or JK flip-flops with $J=K=1$) where only the first flip-flop ($FF_0$) is clocked by the external master clock. Each subsequent flip-flop $FF_{i+1}$ is clocked by the output ($Q_i$ or $\bar{Q}_i$) of the preceding stage:</p>
<ul>
<li><strong>Negative Edge-Triggered Up-Counter:</strong> Clocking $FF_{i+1}$ from output $Q_i$ causes $FF_{i+1}$ to toggle whenever $Q_i$ transitions from $1 \to 0$, creating a standard binary count sequence ($0, 1, 2, \dots, 2^n - 1$).</li>
<li><strong>Negative Edge-Triggered Down-Counter:</strong> Clocking $FF_{i+1}$ from inverted output $\bar{Q}_i$ creates a downward counting sequence ($2^n - 1, \dots, 1, 0$).</li>
</ul>

<h4>2. Propagation Delay Accumulation & Maximum Operating Frequency</h4>
<p>Because each flip-flop must wait for the preceding stage to settle, the total propagation delay accumulates linearly with the number of stages $n$:</p>
<div class="math-display">
$$t_{\text{total}} = n \cdot t_{pd}$$
</div>
<p>To avoid false count sampling, the clock period $T_{\text{clk}}$ must be strictly greater than this accumulated delay:</p>
<div class="math-display">
$$T_{\text{clk}} \ge n \cdot t_{pd} + t_s \implies f_{\text{max}} \le \frac{1}{n \cdot t_{pd} + t_s}$$
</div>
<p>For an 8-bit ripple counter with $t_{pd} = 15\text{ ns}$, $t_{\text{total}} = 120\text{ ns}$, capping clock speed below $8.3\text{ MHz}$. During the transient settling window, intermediate invalid states produce severe false output "glitches".</p>

<h4>3. Truncated Modulus Counters (MOD-N Counters)</h4>
<p>An $n$-stage binary counter naturally recycles after $2^n$ counts (natural modulus $MOD = 2^n$). To construct a counter with an arbitrary modulus $N < 2^n$ (e.g., a <strong>decade / BCD counter</strong> with $MOD = 10$ using $n = 4$ flip-flops):</p>
<ol>
<li>Identify the binary representation of target modulus $N$. For $N = 10_{10} = 1010_2$, bits $Q_3 = 1$ and $Q_1 = 1$.</li>
<li>Connect $Q_3$ and $Q_1$ to the inputs of an asynchronous NAND gate, and connect the NAND output to the active-LOW asynchronous Clear ($\overline{CLR}$) pins of all four flip-flops.</li>
<li>As soon as the counter reaches state $1010_2$, the NAND gate output goes LOW, instantaneously resetting all flip-flops to $0000_2$. The state $1010_2$ persists for only a few nanoseconds (the clear propagation delay), yielding a stable 10-state sequence ($0$ through $9$).</li>
</ol>"""
        },
        {
            "id": "dig-5-2",
            "title": "Synchronous Counter Synthesis & State Machine Design",
            "simulation": "dig-synchronous-counter-sim",
            "content": r"""<h4>1. The Synchronous Architecture Advantage</h4>
<p>In a <strong>synchronous counter</strong>, all flip-flops are connected to the <strong>same common master clock signal</strong>. All state transitions occur simultaneously across all stages at the active clock edge. Propagation delay is independent of counter bit length, being limited solely to a single flip-flop delay plus one combinational gating level:</p>
<div class="math-display">
$$f_{\text{max, sync}} = \frac{1}{t_{pd, FF} + t_{pd, \text{gate}} + t_{su}}$$
</div>

<h4>2. Formal Step-by-Step Synthesis Algorithm</h4>
<ol>
<li><strong>State Diagram & State Transition Table:</strong> Formulate the sequence of present states $Q_n$ and required next states $Q_{n+1}$.</li>
<li><strong>Select Flip-Flop Type:</strong> Typically JK or D flip-flops. Reference the <strong>Excitation Table</strong>:
<div class="table-responsive">
<table class="table table-bordered">
<thead>
<tr><th>Transition ($Q_n \to Q_{n+1}$)</th><th>Required $J$</th><th>Required $K$</th><th>Required $D$</th><th>Required $T$</th></tr>
</thead>
<tbody>
<tr><td>$0 \to 0$</td><td>$0$</td><td>$\times$</td><td>$0$</td><td>$0$</td></tr>
<tr><td>$0 \to 1$</td><td>$1$</td><td>$\times$</td><td>$1$</td><td>$1$</td></tr>
<tr><td>$1 \to 0$</td><td>$\times$</td><td>$1$</td><td>$0$</td><td>$1$</td></tr>
<tr><td>$1 \to 1$</td><td>$\times$</td><td>$0$</td><td>$1$</td><td>$0$</td></tr>
</tbody>
</table>
</div></li>
<li><strong>K-Map Derivation of Flip-Flop Excitation Inputs:</strong> Plot $J_i, K_i$ (or $D_i$) as functions of present state variables $Q_k$, exploiting Don't Care states to obtain minimal Boolean equations.</li>
<li><strong>Lockout Verification:</strong> Analyze unassigned or unused states. If electrical noise drops the counter into an unused state, it must self-recover back to the valid sequence within a finite number of clock cycles rather than circulating indefinitely in a parasitic <strong>lockout cycle</strong>.</li>
</ol>"""
        },
        {
            "id": "dig-5-3",
            "title": "Shift Registers: SISO, SIPO, PISO, PIPO, Ring & Johnson",
            "simulation": "dig-shift-register-ring-sim",
            "content": r"""<h4>1. Shift Register Functional Topologies</h4>
<p>A <strong>shift register</strong> is an array of cascaded flip-flops configured such that stored binary data moves laterally by one bit position on each clock pulse. The four fundamental operational topologies are:</p>
<ol>
<li><strong>Serial-In Serial-Out (SISO):</strong> Data bits enter sequentially one bit per clock pulse and exit sequentially from the final stage. Requires $n$ clock cycles to load and $n$ clock cycles to read out an $n$-bit word. Acts as an accurate time delay line.</li>
<li><strong>Serial-In Parallel-Out (SIPO):</strong> Data is shifted in serially; once filled after $n$ clock pulses, all $n$ bits are read out simultaneously in parallel. Fundamental to UART serial communication receivers.</li>
<li><strong>Parallel-In Serial-Out (PISO):</strong> Data is loaded in parallel simultaneously via combinational steering gates, then shifted out serially one bit at a time. Fundamental to UART serial communication transmitters.</li>
<li><strong>Parallel-In Parallel-Out (PIPO):</strong> Universal high-speed buffer register. Loads and reads $n$ bits simultaneously in a single clock cycle.</li>
</ol>

<h4>2. The Universal Bidirectional Shift Register</h4>
<p>A 4-bit Universal Shift Register (e.g., standard 74HC194 IC) incorporates four 4-to-1 multiplexers at the inputs of each D flip-flop, controlled by two mode select lines $(S_1, S_0)$:</p>
<ul>
<li>$S_1 S_0 = 00$: <strong>Hold / No Change</strong> ($D_i = Q_i$).</li>
<li>$S_1 S_0 = 01$: <strong>Shift Right</strong> ($D_i = Q_{i-1}$, with $D_3 = \text{Serial Input Right}$).</li>
<li>$S_1 S_0 = 10$: <strong>Shift Left</strong> ($D_i = Q_{i+1}$, with $D_0 = \text{Serial Input Left}$).</li>
<li>$S_1 S_0 = 11$: <strong>Parallel Load</strong> ($D_i = I_i$).</li>
</ul>

<h4>3. Cyclic Shift Counters: Ring & Johnson Counters</h4>
<ol>
<li><strong>Ring Counter:</strong> Formed by circulating the serial output of the final stage directly back into the serial input of the first stage ($D_0 = Q_{n-1}$):
<div class="math-display">
\text{Initial State: } 1000_2 \longrightarrow 0100_2 \longrightarrow 0010_2 \longrightarrow 0001_2 \longrightarrow 1000_2
</div>
A single circulating '1' decodes directly into $n$ mutually exclusive timing pulses with <strong>zero decoding gates</strong>, but utilizes only $n$ states out of $2^n$ available states ($MOD = n$).</li>
<li><strong>Johnson (Twisted Ring / Moebius) Counter:</strong> Formed by feeding back the <em>inverted</em> output of the final stage into the first stage ($D_0 = \bar{Q}_{n-1}$):
<div class="math-display">
\text{States: } 0000 \to 1000 \to 1100 \to 1110 \to 1111 \to 0111 \to 0011 \to 0001 \to 0000
</div>
An $n$-stage Johnson counter produces $2n$ states ($MOD = 2n$). Adjacent states differ by only a single bit (unit distance), enabling completely glitch-free decoding with simple 2-input AND gates.</li>
</ol>"""
        },
        {
            "id": "dig-5-4",
            "title": "Decoders, Encoders & BCD-to-7-Segment Display Drivers",
            "content": r"""<h4>1. Binary Decoders</h4>
<p>A <strong>decoder</strong> is an MSI combinational circuit with $n$ input lines and up to $2^n$ unique output lines. It decodes an $n$-bit binary input code by activating exactly one output line corresponding to that input minterm:</p>
<ul>
<li><strong>3-to-8 Line Decoder (74138 IC):</strong> Three inputs $(A_2, A_1, A_0)$ select one of 8 active-LOW outputs ($\bar{Y}_0$ through $\bar{Y}_7$). Contains active-LOW enable inputs ($\bar{E}_1, \bar{E}_2, E_3$) used to cascade multiple decoders into large memory address decoding trees.</li>
<li><strong>Universal Logic Realization:</strong> Because each output of an active-LOW decoder produces an individual minterm $\bar{m}_i = \overline{A B C}$, any arbitrary Boolean function in SOP form can be implemented simply by feeding the appropriate decoder outputs into an external NAND gate (since $\overline{\bar{m}_1 \cdot \bar{m}_4} = m_1 + m_4$).</li>
</ul>

<h4>2. Encoders & Priority Encoders</h4>
<p>An <strong>encoder</strong> performs the inverse operation: it accepts $2^n$ input lines (where only one line is asserted at any time) and outputs an $n$-bit binary code. If multiple inputs can be asserted simultaneously, standard encoders fail.</p>
<p>A <strong>Priority Encoder (e.g., 74148 IC)</strong> resolves input contention by asserting the binary code of the <strong>highest-priority active input</strong>, ignoring all lower-priority inputs. It also generates an active Group Select ($GS$) signal indicating whether any valid input is active, forming the foundation of CPU interrupt request (IRQ) controllers.</p>

<h4>3. BCD-to-7-Segment Display Drivers (7447 IC)</h4>
<p>Drives numerical LED/LCD displays containing seven planar segments labeled $a, b, c, d, e, f, g$. Translates 4-bit BCD input $(D, C, B, A)$ into 7 segment drive signals. For common-anode LED displays, the 7447 provides open-collector active-LOW outputs ($a=0$ lights the segment), incorporating lamp test ($LT$) and automatic zero-blanking inputs ($RBI, RBO$).</p>"""
        },
        {
            "id": "dig-5-5",
            "title": "Multiplexers (MUX) & Demultiplexers (DEMUX)",
            "content": r"""<h4>1. Multiplexers (Data Selectors)</h4>
<p>A <strong>Multiplexer (MUX)</strong> is a combinational switching subsystem that directs binary information from one of $2^n$ data input channels ($I_0, I_1, \dots, I_{2^n-1}$) to a single output line $Y$, selected by $n$ control select lines ($S_{n-1}, \dots, S_0$):</p>
<div class="math-display">
$$Y = \sum_{k=0}^{2^n-1} m_k(S) \cdot I_k = \bar{S}_1 \bar{S}_0 I_0 + \bar{S}_1 S_0 I_1 + S_1 \bar{S}_0 I_2 + S_1 S_0 I_3 \quad (\text{4-to-1 MUX})$$
</div>

<h4>2. Implementing Arbitrary Logic Functions Using Multiplexers</h4>
<p>A $2^n$-to-1 multiplexer can implement <strong>any arbitrary Boolean function of $n+1$ variables</strong> without requiring any external logic gates:</p>
<ol>
<li>Assign $n$ variables to the MUX select lines $(S_{n-1}, \dots, S_0)$.</li>
<li>Express the remaining $(n+1)$-th variable $Z$ as the data input $I_k$ for each select combination. For each minterm pair, $I_k$ will evaluate to either $0$, $1$, $Z$, or $\bar{Z}$.</li>
</ol>
<p>Multiplexers thus function as universal, software-configurable look-up tables (LUTs), forming the core logic fabric of modern Field-Programmable Gate Arrays (FPGAs).</p>

<h4>3. Demultiplexers (DEMUX)</h4>
<p>A <strong>Demultiplexer</strong> takes a single data input line and routes it to one of $2^n$ output lines selected by $n$ address lines. A binary decoder with an enable input is functionally identical to a demultiplexer (the enable acts as the serial data input).</p>"""
        }
    ],
    "problems": [
        {
            "id": "dig-p-5-1",
            "title": "Design of a Synchronous MOD-6 Counter Using JK Flip-Flops",
            "statement": "Design a synchronous counter that counts through the cyclic sequence: $0 \to 1 \to 2 \to 3 \to 4 \to 5 \to 0$ using three JK flip-flops ($Q_2, Q_1, Q_0$). (a) Construct the state transition table and list the required $J$ and $K$ excitations for all three flip-flops. (b) Derive the minimal Boolean excitation equations using 3-variable K-maps. (c) Analyze the unused states $6$ ($110_2$) and $7$ ($111_2$) and verify whether the counter is self-correcting (lockout-free).",
            "steps": [
                {
                    "stepName": "Step 1: Construct the State Transition & Excitation Table",
                    "math": r"\begin{matrix} Q_2 Q_1 Q_0 & Q_2^+ Q_1^+ Q_0^+ & J_2 & K_2 & J_1 & K_1 & J_0 & K_0 \\ \hline 000 & 001 & 0 & \times & 0 & \times & 1 & \times \\ 001 & 010 & 0 & \times & 1 & \times & \times & 1 \\ 010 & 011 & 0 & \times & \times & 0 & 1 & \times \\ 011 & 100 & 1 & \times & \times & 1 & \times & 1 \\ 100 & 101 & \times & 0 & 0 & \times & 1 & \times \\ 101 & 000 & \times & 1 & 0 & \times & \times & 1 \end{matrix}",
                    "explanation": "Map valid transitions (0 to 5) to JK excitation rules: 0->0: (0,x); 0->1: (1,x); 1->0: (x,1); 1->1: (x,0)."
                },
                {
                    "stepName": "Step 2: Derive Minimized K-Map Equations for Flip-Flop 0",
                    "math": r"J_0: \text{cells } 0, 2, 4 = 1; \ 1, 3, 5 = \times \implies J_0 = 1. \quad K_0: \text{cells } 1, 3, 5 = 1; \ 0, 2, 4 = \times \implies K_0 = 1",
                    "explanation": "Flip-flop 0 toggles on every single clock pulse: J0 = 1, K0 = 1."
                },
                {
                    "stepName": "Step 3: Derive Equations for Flip-Flop 1 and Flip-Flop 2",
                    "math": r"J_1 = \bar{Q}_2 Q_0, \quad K_1 = Q_0. \qquad J_2 = Q_1 Q_0, \quad K_2 = Q_0",
                    "explanation": "Plot K-maps with unused states 6 and 7 as Don't Cares (x)."
                },
                {
                    "stepName": "Step 4: Lockout Analysis for Unused State 6 (110)",
                    "math": r"\text{For } Q = 110_2: J_2 = 0, K_2 = 0 \implies Q_2^+=1; \quad J_1 = 0, K_1 = 0 \implies Q_1^+=1; \quad J_0=1, K_0=1 \implies Q_0^+=1 \implies 110 \to 111",
                    "explanation": "State 6 transitions to State 7 on next clock pulse."
                },
                {
                    "stepName": "Step 5: Lockout Analysis for Unused State 7 (111)",
                    "math": r"\text{For } Q = 111_2: J_2=1, K_2=1 \implies Q_2^+=0; \quad J_1=0, K_1=1 \implies Q_1^+=0; \quad J_0=1, K_0=1 \implies Q_0^+=0 \implies 111 \to 000!",
                    "explanation": "State 7 transitions directly to valid state 000. Both unused states self-recover within 2 clock cycles: the design is completely lockout-free."
                }
            ],
            "answer": "J_0 = K_0 = 1; \\quad J_1 = \\bar{Q}_2 Q_0, \\ K_1 = Q_0; \\quad J_2 = Q_1 Q_0, \\ K_2 = Q_0 \\quad (\\text{Self-Correcting, Lockout-Free})"
        },
        {
            "id": "dig-p-5-2",
            "title": "Universal Shift Register State Transitions and Timing Sequence",
            "statement": "A 4-bit Universal Shift Register initially holds binary data $Q_3 Q_2 Q_1 Q_0 = 1010_2$. The register is clocked with the following control mode sequence: (1) One clock pulse with $S_1 S_0 = 01$ and Serial Input Right $SIR = 1$; (2) One clock pulse with $S_1 S_0 = 10$ and Serial Input Left $SIL = 0$; (3) One clock pulse with $S_1 S_0 = 11$ and Parallel Inputs $I = 1100_2$. Determine the register contents after each operational step.",
            "steps": [
                {
                    "stepName": "Step 1: Initial State",
                    "math": r"Q^{(0)} = 1010_2",
                    "explanation": "Register holds 1010."
                },
                {
                    "stepName": "Step 2: Clock Pulse 1 - Shift Right (S1 S0 = 01)",
                    "math": r"\text{Bits shift right: } Q_3 \leftarrow SIR = 1, \quad Q_2 \leftarrow Q_3 = 1, \quad Q_1 \leftarrow Q_2 = 0, \quad Q_0 \leftarrow Q_1 = 1 \implies Q^{(1)} = 1101_2",
                    "explanation": "Previous LSB (0) is shifted out and lost; SIR=1 shifts into MSB."
                },
                {
                    "stepName": "Step 3: Clock Pulse 2 - Shift Left (S1 S0 = 10)",
                    "math": r"\text{Bits shift left: } Q_3 \leftarrow Q_2 = 1, \quad Q_2 \leftarrow Q_1 = 0, \quad Q_1 \leftarrow Q_0 = 1, \quad Q_0 \leftarrow SIL = 0 \implies Q^{(2)} = 1010_2",
                    "explanation": "Previous MSB (1) is shifted out; SIL=0 shifts into LSB."
                },
                {
                    "stepName": "Step 4: Clock Pulse 3 - Parallel Load (S1 S0 = 11)",
                    "math": r"Q \leftarrow I \implies Q^{(3)} = 1100_2",
                    "explanation": "Parallel data 1100 is loaded directly into all four stages simultaneously in one clock cycle."
                }
            ],
            "answer": "Q^{(1)} = 1101_2 \\quad (\\text{Shift Right}), \\quad Q^{(2)} = 1010_2 \\quad (\\text{Shift Left}), \\quad Q^{(3)} = 1100_2 \\quad (\\text{Parallel Load})"
        },
        {
            "id": "dig-p-5-3",
            "title": "Synthesis of a 4-Variable Boolean Function Using an 8-to-1 Multiplexer",
            "statement": "Implement the 4-variable Boolean function $F(A, B, C, D) = \\sum m(1, 3, 4, 11, 12, 13, 14, 15)$ using a single 8-to-1 multiplexer (e.g., 74151). Assign variables $A, B, C$ to select lines $S_2, S_1, S_0$ and derive the required logic connections for data inputs $I_0$ through $I_7$ in terms of variable $D$, $0$, or $1$.",
            "steps": [
                {
                    "stepName": "Step 1: Construct MUX Partitioning Table",
                    "math": r"\begin{matrix} \text{Select } ABC & \text{Minterm } D=0 & \text{Minterm } D=1 & \text{Required } I_k \\ \hline 000 \ (0) & m_0 (0) & m_1 (1) & I_0 = D \\ 001 \ (1) & m_2 (0) & m_3 (1) & I_1 = D \\ 010 \ (2) & m_4 (1) & m_5 (0) & I_2 = \bar{D} \\ 011 \ (3) & m_6 (0) & m_7 (0) & I_3 = 0 \\ 100 \ (4) & m_8 (0) & m_9 (0) & I_4 = 0 \\ 101 \ (5) & m_{10} (0) & m_{11} (1) & I_5 = D \\ 110 \ (6) & m_{12} (1) & m_{13} (1) & I_6 = 1 \\ 111 \ (7) & m_{14} (1) & m_{15} (1) & I_7 = 1 \end{matrix}",
                    "explanation": "Group minterms in pairs of D=0 and D=1 for each select combination."
                },
                {
                    "stepName": "Step 2: Evaluate Each Data Line",
                    "math": r"I_0 = D, \quad I_1 = D, \quad I_2 = \bar{D}, \quad I_3 = 0, \quad I_4 = 0, \quad I_5 = D, \quad I_6 = 1, \quad I_7 = 1",
                    "explanation": "If only D=1 is in minterm list: I_k = D. If both are 1: I_k = 1. If only D=0 is 1: I_k = D_bar. If neither: I_k = 0."
                },
                {
                    "stepName": "Step 3: Hardware Implementation",
                    "math": r"S_2 = A, \ S_1 = B, \ S_0 = C; \quad I_0, I_1, I_5 \leftarrow D; \quad I_2 \leftarrow \bar{D}; \quad I_3, I_4 \leftarrow \text{GND}; \quad I_6, I_7 \leftarrow V_{CC}",
                    "explanation": "A single 8-to-1 MUX and one inverter for D_bar implements the complete 4-variable function."
                }
            ],
            "answer": "S_2=A, S_1=B, S_0=C; \\quad I_0=I_1=I_5=D, \\ I_2=\\bar{D}, \\ I_3=I_4=0, \\ I_6=I_7=1"
        }
    ]
}

# ==========================================
# UNIT 6: Data Conversion Systems: Digital-to-Analog & Analog-to-Digital
# ==========================================
u6 = {
    "unitNumber": 6,
    "unitId": "unit6-data-converters-dac-adc",
    "title": "Data Conversion Systems: Digital-to-Analog & Analog-to-Digital",
    "description": "Theory, precision architectures, and error metrics of mixed-signal data converters: binary-weighted resistor DACs and operational amplifier virtual ground summing; R-2R ladder networks, Thevenin equivalent analysis, and constant input impedance; DAC resolution, monotonicity, settling time, differential non-linearity (DNL), and integral non-linearity (INL); Flash (simultaneous comparator) ADCs, priority decoding, and comparator count scaling; tracking ADCs, Successive Approximation Register (SAR) binary search algorithms; Dual-Slope integrating ADCs, line-frequency noise rejection, and Delta-Sigma oversampling modulation.",
    "sections": [
        {
            "id": "dig-6-1",
            "title": "D/A Conversion: Binary-Weighted Resistors & Virtual Ground",
            "content": r"""<h4>1. Digital-to-Analog Converter (DAC) Operational Concept</h4>
<p>A <strong>Digital-to-Analog Converter (DAC)</strong> translates an $N$-bit digital binary word $D = b_{N-1} b_{N-2} \dots b_0$ into an equivalent proportional analog output voltage $V_{\text{out}}$ or current $I_{\text{out}}$:</p>
<div class="math-display">
$$V_{\text{out}} = V_{\text{ref}} \sum_{i=0}^{N-1} b_i 2^{i - N} = \frac{V_{\text{ref}}}{2^N} \left( b_{N-1} 2^{N-1} + b_{N-2} 2^{N-2} + \dots + b_0 2^0 \right)$$
</div>
<p>where $V_{\text{ref}}$ is a precision voltage reference, and $\frac{V_{\text{ref}}}{2^N}$ defines the <strong>analog step size or resolution (1 LSB)</strong>.</p>

<h4>2. The Binary-Weighted Resistor DAC</h4>
<p>Constructed by connecting weighted resistors $R, 2R, 4R, \dots, 2^{N-1}R$ to the inverting summing junction of an operational amplifier. Binary switches connect resistor $i$ to $-V_{\text{ref}}$ when bit $b_i = 1$, or to ground when $b_i = 0$:</p>
<div class="math-display">
$$I_{\text{sum}} = \sum_{i=0}^{N-1} b_i \frac{V_{\text{ref}}}{2^{N-1-i} R}$$
</div>
<p>Because the inverting op-amp terminal is held at virtual ground ($0\text{ V}$), the output voltage is:</p>
<div class="math-display">
$$V_{\text{out}} = I_{\text{sum}} R_f = V_{\text{ref}} \frac{R_f}{R} \left( \frac{b_{N-1}}{2^1} + \frac{b_{N-2}}{2^2} + \dots + \frac{b_0}{2^N} \right)$$
</div>

<h4>3. Physical Limitations of Binary-Weighted Networks</h4>
<p>While conceptually elegant, binary-weighted DACs are severely impractical for high resolutions ($N \ge 8$):</p>
<ul>
<li><strong>Extreme Resistance Spread:</strong> For a 16-bit DAC with $R = 10\text{ k}\Omega$, the LSB resistor must be $2^{15} R = 327.68\text{ M}\Omega$—a ratio exceeding $32,000 : 1$.</li>
<li><strong>Impossibility of Monolithic Integration:</strong> Fabricating resistors spanning four orders of magnitude on a single silicon die with sub-$0.01\%$ thermal tracking is technologically impossible.</li>
</ul>"""
        },
        {
            "id": "dig-6-2",
            "title": "The R-2R Ladder Network DAC: Thevenin Analysis & Symmetry",
            "simulation": "dig-r2r-dac-sim",
            "content": r"""<h4>1. The R-2R Ladder Architecture</h4>
<p>Bernard Lippel (1953) resolved the resistance spread bottleneck with the ingenious <strong>$R$-$2R$ ladder network</strong>, which utilizes <strong>only two precision resistance values</strong>—$R$ and $2R$—regardless of the bit resolution $N$.</p>

<h4>2. Thevenin Equivalent & Constant Input Impedance Proof</h4>
<p>Looking into any node of an $R$-$2R$ ladder toward the terminated end, the equivalent resistance is identically <strong>$R$</strong>:</p>
<ol>
<li>At the termination end, two parallel $2R$ resistors combine to yield $2R \parallel 2R = R$.</li>
<li>Adding the series resistor $R$ gives $R + R = 2R$.</li>
<li>At the next node, this $2R$ is in parallel with that stage's vertical $2R$ branch: $2R \parallel 2R = R$.</li>
</ol>
<p>By mathematical induction, this perfect binary current division repeats identically across all $N$ stages. At each ladder node, the injected current splits into two equal halves ($50\% / 50\%$).</p>

<h4>3. Inverted R-2R Current-Steering DAC</h4>
<p>In modern monolithic CMOS DACs, the ladder is operated in the <strong>current-steering mode</strong>: the vertical $2R$ branches terminate in SPDT CMOS switches that steer currents either into the op-amp virtual ground ($I_{\text{out}}$) or into circuit analog ground ($I_{\text{out2}}$):</p>
<div class="math-display">
$$V_{\text{out}} = - V_{\text{ref}} \left( \frac{R_f}{R} \right) \sum_{i=0}^{N-1} b_i 2^{i - N}$$
</div>
<p>Key Engineering Advantages:</p>
<ul>
<li>Only two resistor values ($R$ and $2R$, typically $10\text{ k}\Omega$ and $20\text{ k}\Omega$), manufactured by laser-trimmed thin-film SiCr or polysilicon with perfect thermal tracking ($< 1\text{ ppm/}^\circ\text{C}$).</li>
<li>All nodes remain at fixed potentials ($0\text{ V}$), eliminating parasitic capacitance charging delays and achieving sub-nanosecond settling times.</li>
</ul>"""
        },
        {
            "id": "dig-6-3",
            "title": "DAC Performance Metrics: Resolution, Settling Time & Linearity",
            "content": r"""<h4>1. DAC Resolution & Full-Scale Range (FSR)</h4>
<p>The <strong>resolution</strong> of an $N$-bit DAC is the smallest output voltage increment it can resolve, equal to the weight of 1 LSB:</p>
<div class="math-display">
$$V_{\text{LSB}} = \frac{V_{\text{FSR}}}{2^N - 1} \quad (\text{or } \frac{V_{\text{ref}}}{2^N})$$
</div>
<p>The maximum analog output, attained when all bits are 1 ($11\dots1_2$), is strictly 1 LSB below full reference:</p>
<div class="math-display">
$$V_{\text{out, max}} = V_{\text{ref}} \left( 1 - \frac{1}{2^N} \right)$$
</div>

<h4>2. Dynamic Metrics: Settling Time & Glitch Impulse</h4>
<ul>
<li><strong>Settling Time ($t_s$):</strong> The elapsed time from the application of an input digital transition until the analog output settles and remains within a specified error band (typically $\pm \frac{1}{2}\text{ LSB}$) of its final value. Governed by op-amp slew rate and $RC$ time constants.</li>
<li><strong>Major Carry Glitch Impulse:</strong> When transitioning across mid-scale ($0111\dots1 \to 1000\dots0$), switch timing skews cause temporary false intermediate states ($1111\dots1$ or $0000\dots0$), ejecting massive voltage spikes (glitch area in $\text{pV}\cdot\text{s}$) into audio/video signals.</li>
</ul>

<h4>3. Static Accuracy: Non-Linearity Metrics (INL & DNL)</h4>
<ul>
<li><strong>Differential Non-Linearity (DNL):</strong> The difference between the actual step height between adjacent codes and the ideal step height ($1\text{ LSB}$):
<div class="math-display">
$$\text{DNL}(k) = \frac{V_{\text{out}}(k) - V_{\text{out}}(k-1) - V_{\text{LSB}}}{V_{\text{LSB}}}$$
</div>
If $\text{DNL} < -1\text{ LSB}$, the transfer function reverses direction, creating a <strong>non-monotonic DAC</strong>.</li>
<li><strong>Integral Non-Linearity (INL):</strong> The maximum deviation of the actual analog transfer curve from the ideal straight line across the entire range.</li>
</ul>"""
        },
        {
            "id": "dig-6-4",
            "title": "Fast Flash (Simultaneous Comparator) ADCs",
            "simulation": "dig-flash-sar-adc-sim",
            "content": r"""<h4>1. Operational Architecture of the Flash ADC</h4>
<p>An <strong>Analog-to-Digital Converter (ADC)</strong> quantizes a continuous analog input voltage $V_{\text{in}}$ into a discrete digital code. The <strong>Flash (Parallel) ADC</strong> is the fastest known data conversion architecture, completing conversion in a single clock cycle ($t_{\text{conv}} < 1\text{ ns}$, gigasample/second speeds).</p>

<h4>2. Circuit Topology</h4>
<p>An $N$-bit Flash ADC consists of:</p>
<ol>
<li><strong>Precision Resistor Ladder:</strong> A string of $2^N$ matched resistors $R$ connected between $V_{\text{ref}}$ and ground, establishing $2^N - 1$ equally spaced reference voltage taps:
<div class="math-display">
$$V_k = \frac{k - 0.5}{2^N} V_{\text{ref}} \quad (k = 1, 2, \dots, 2^N - 1)$$
</div></li>
<li><strong>Comparator Bank:</strong> Exactly $2^N - 1$ analog comparators operating in parallel. Each comparator compares $V_{\text{in}}$ to its respective reference tap $V_k$. All comparators below $V_{\text{in}}$ output 1; all above output 0, producing a <strong>Thermometer Code</strong> of height proportional to $V_{\text{in}}$.</li>
<li><strong>Priority Decoder:</strong> Converts the $(2^N - 1)$-bit thermometer code into an $N$-bit binary output word in a single gate delay.</li>
</ol>

<h4>3. Flash ADC Trade-Offs & Scaling Wall</h4>
<p>The monumental speed of Flash ADCs is offset by exponential hardware growth:</p>
<div class="math-display">
$$\text{Number of Comparators} = 2^N - 1$$
</div>
<ul>
<li>For $N = 2$ bits: $2^2 - 1 = 3$ comparators.</li>
<li>For $N = 3$ bits: $2^3 - 1 = 7$ comparators.</li>
<li>For $N = 8$ bits: $2^8 - 1 = 255$ comparators (practical limit for standalone flash).</li>
<li>For $N = 16$ bits: $2^{16} - 1 = 65,535$ precision comparators on a single chip—consuming excessive silicon area and hundreds of watts of power. High resolutions require alternative multi-step architectures.</li>
</ul>"""
        },
        {
            "id": "dig-6-5",
            "title": "Tracking, SAR & Dual-Slope Integrating ADCs",
            "content": r"""<h4>1. Successive Approximation Register (SAR) ADCs</h4>
<p>The <strong>SAR ADC</strong> is the industry workhorse for medium-to-high resolution ($10 - 18\text{ bits}$) at sample rates up to several megasamples per second. It utilizes a feedback loop containing a DAC, a single comparator, and a digital SAR control engine executing a <strong>binary search algorithm</strong>:</p>
<ol>
<li>Clock Cycle 1: SAR sets MSB to 1 ($1000\dots_2$), prompting internal DAC to output mid-scale $V_{\text{DAC}} = V_{\text{ref}} / 2$.</li>
<li>Comparator tests if $V_{\text{in}} > V_{\text{DAC}}$. If yes, MSB is retained as 1; if no, MSB is cleared to 0.</li>
<li>Clock Cycle 2: SAR sets next bit ($b_{N-2}$) to 1, tests against $V_{\text{in}}$, and retains or clears it.</li>
<li>The process repeats bit-by-bit until the LSB is resolved.</li>
</ol>
<p>An $N$-bit SAR ADC requires exactly <strong>$N$ clock cycles</strong> per conversion ($t_{\text{conv}} = N \cdot T_{\text{clk}}$), requiring only <strong>one comparator</strong> regardless of resolution.</p>

<h4>2. Dual-Slope Integrating ADC</h4>
<p>The premier architecture for high-precision digital multimeters (DMMs) where ultra-high accuracy and noise immunity outweigh conversion speed ($10 - 100\text{ conversions/sec}$):</p>
<ol>
<li><strong>Run-Up Phase ($T_1$, Fixed Time):</strong> An analog integrator integrates input voltage $V_{\text{in}}$ for a fixed time interval $T_1 = 2^N T_{\text{clk}}$:
<div class="math-display">
$$V_{\text{peak}} = - \frac{1}{R C} \int_0^{T_1} V_{\text{in}} dt = - \frac{V_{\text{in}} T_1}{R C}$$
</div></li>
<li><strong>Run-Down Phase ($T_2$, Measured Time):</strong> Integrator switches to precision negative reference $-V_{\text{ref}}$ and discharges back to zero at a constant slope:
<div class="math-display">
$$0 = V_{\text{peak}} + \frac{V_{\text{ref}} T_2}{R C} \implies \frac{V_{\text{in}} T_1}{R C} = \frac{V_{\text{ref}} T_2}{R C}$$
</div>
<div class="math-display">
$$T_2 = T_1 \left( \frac{V_{\text{in}}}{V_{\text{ref}}} \right)$$
</div></li>
</ol>
<p><strong>Monumental Advantage:</strong> Both $R$ and $C$ cancel out completely from the equation! Variations in resistor values, capacitor aging, and clock oscillator drift have <strong>zero effect</strong> on measurement accuracy. Setting $T_1 = 20\text{ ms}$ ($1/50\text{ Hz}$) provides infinite rejection of AC power line hum.</p>"""
        }
    ],
    "problems": [
        {
            "id": "dig-p-6-1",
            "title": "Analysis of a 4-Bit R-2R Ladder Digital-to-Analog Converter",
            "statement": "A 4-bit $R$-$2R$ ladder DAC operates with reference voltage $V_{\\text{ref}} = 10.0\\text{ V}$, ladder resistance $R = 10.0\\text{ k}\\Omega$ ($2R = 20.0\\text{ k}\\Omega$), and feedback resistor $R_f = 20.0\\text{ k}\\Omega$. (a) Calculate the voltage step size (1 LSB). (b) Determine the full-scale analog output voltage $V_{\\text{out, max}}$. (c) Calculate the exact output voltage when the digital input code is $D = 1011_2$ ($11_{10}$).",
            "steps": [
                {
                    "stepName": "Step 1: Calculate Step Size (1 LSB)",
                    "math": r"V_{\text{LSB}} = \frac{V_{\text{ref}}}{2^N} \left(\frac{R_f}{R}\right) = \frac{10.0\text{ V}}{2^4} \left(\frac{20\text{ k}\Omega}{10\text{ k}\Omega}\right) = \frac{10.0}{16} \times 2 = \frac{20.0}{16}\text{ V} = 1.250\text{ V}",
                    "explanation": "Compute voltage equivalent of one LSB."
                },
                {
                    "stepName": "Step 2: Determine Full-Scale Output Voltage",
                    "math": r"V_{\text{out, max}} = V_{\text{LSB}} \times (2^N - 1) = 1.250\text{ V} \times (16 - 1) = 1.250 \times 15 = 18.750\text{ V}",
                    "explanation": "Full-scale output occurs when all bits are 1 (code 1111)."
                },
                {
                    "stepName": "Step 3: Evaluate Output for Input Code 1011",
                    "math": r"D = (1011)_2 = 1 \times 2^3 + 0 \times 2^2 + 1 \times 2^1 + 1 \times 2^0 = 8 + 2 + 1 = 11_{10}",
                    "explanation": "Convert digital input code to decimal."
                },
                {
                    "stepName": "Step 4: Compute Final Output Voltage",
                    "math": r"V_{\text{out}} = 11 \times V_{\text{LSB}} = 11 \times 1.250\text{ V} = 13.750\text{ V}",
                    "explanation": "Multiply decimal value by step size: exactly 13.75 V."
                }
            ],
            "answer": "V_{\\text{LSB}} = 1.250\\text{ V}, \\quad V_{\\text{out, max}} = 18.75\\text{ V}, \\quad V_{\\text{out}}(1011_2) = 13.75\\text{ V}"
        },
        {
            "id": "dig-p-6-2",
            "title": "3-Bit Flash Analog-to-Digital Converter Architecture and Quantization",
            "statement": "A 3-bit Flash ADC has a full-scale analog reference of $V_{\\text{ref}} = 8.00\\text{ V}$. (a) Calculate the total number of analog comparators and precision divider resistors required. (b) Determine the reference voltage at each comparator threshold tap ($V_1$ through $V_7$). (c) If an analog input voltage of $V_{\\text{in}} = 5.20\\text{ V}$ is applied, determine the 7-bit comparator thermometer code and the 3-bit priority encoder binary output word.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate Component Counts",
                    "math": r"N = 3 \implies N_{\text{comparators}} = 2^N - 1 = 2^3 - 1 = 7 \text{ comparators}; \quad N_{\text{resistors}} = 2^3 = 8 \text{ matched resistors}",
                    "explanation": "A 3-bit flash ADC requires 7 comparators and 8 resistors."
                },
                {
                    "stepName": "Step 2: Determine Step Size and Comparator Reference Taps",
                    "math": r"V_{\text{step}} = \frac{V_{\text{ref}}}{8} = \frac{8.00\text{ V}}{8} = 1.00\text{ V}. \implies V_1=1.0\text{V}, \ V_2=2.0\text{V}, \ V_3=3.0\text{V}, \ V_4=4.0\text{V}, \ V_5=5.0\text{V}, \ V_6=6.0\text{V}, \ V_7=7.0\text{V}",
                    "explanation": "List all 7 threshold tap voltages."
                },
                {
                    "stepName": "Step 3: Evaluate Comparator Outputs for Vin = 5.20 V",
                    "math": r"5.20\text{ V} > V_1, V_2, V_3, V_4, V_5 \ (1.0 - 5.0\text{ V}) \implies C_1 = C_2 = C_3 = C_4 = C_5 = 1; \quad 5.20\text{ V} < V_6, V_7 \implies C_6 = C_7 = 0",
                    "explanation": "Comparators 1 through 5 output 1; comparators 6 and 7 output 0."
                },
                {
                    "stepName": "Step 4: Form Thermometer Code and Priority Binary Output",
                    "math": r"\text{Thermometer Code: } (C_7 C_6 C_5 C_4 C_3 C_2 C_1) = 0011111_2. \implies \text{Priority Encoder Output: } (101)_2 = 5_{10}",
                    "explanation": "Five 1s in thermometer code decodes to binary 101 (value 5, corresponding to 5V <= Vin < 6V)."
                }
            ],
            "answer": "N_{\\text{comp}} = 7, \\ N_{\\text{res}} = 8; \\quad \\text{Thermometer Code} = 0011111_2 \\implies \\text{Binary Output} = 101_2 \\ (5_{10})"
        },
        {
            "id": "dig-p-6-3",
            "title": "Dual-Slope Integrating ADC Noise Immunity and Conversion Timing",
            "statement": "A $4\\frac{1}{2}$-digit ($20,000$ count) Dual-Slope integrating ADC uses a clock frequency of $f_{\\text{clk}} = 200\\text{ kHz}$. (a) To completely eliminate $50.0\\text{ Hz}$ AC line hum, calculate the required number of integration cycles $N_1$ during run-up period $T_1$ if $T_1$ is set to exactly one $50\\text{ Hz}$ line period ($20.0\\text{ ms}$). (b) An unknown DC input voltage produces a run-down time of $T_2 = 12.80\\text{ ms}$. If reference voltage $V_{\\text{ref}} = 2.000\\text{ V}$, compute the measured input voltage $V_{\\text{in}}$.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate Integration Clock Cycles for 50 Hz Period",
                    "math": r"T_1 = \frac{1}{50.0\text{ Hz}} = 20.0\text{ ms} = 0.020\text{ s}. \implies N_1 = T_1 \cdot f_{\text{clk}} = 0.020\text{ s} \times 200,000\text{ Hz} = 4000 \text{ clock counts}",
                    "explanation": "Integrating over exactly one period (4000 counts) causes net sinusoidal AC noise integral to vanish identically."
                },
                {
                    "stepName": "Step 2: Calculate Measured Input Voltage Using Dual-Slope Equation",
                    "math": r"V_{\text{in}} = V_{\text{ref}} \left( \frac{T_2}{T_1} \right) = 2.000\text{ V} \times \left( \frac{12.80\text{ ms}}{20.00\text{ ms}} \right) = 2.000 \times 0.640 = 1.280\text{ V}",
                    "explanation": "Evaluate input voltage: exactly 1.280 V."
                },
                {
                    "stepName": "Step 3: Verification of Independence from Component Values",
                    "math": r"\text{Notice that } R, C, \text{ and } f_{\text{clk}} \text{ canceled completely in } V_{\text{in}} = V_{\text{ref}} (N_2 / N_1) = 2.000 \times (2560 / 4000) = 1.280\text{ V}",
                    "explanation": "The measurement is completely immune to RC component tolerances."
                }
            ],
            "answer": "N_1 = 4000 \\text{ counts } (T_1 = 20.0\\text{ ms}), \\quad V_{\\text{in}} = 1.280\\text{ V} \\quad (\\text{Infinite 50 Hz Hum Rejection})"
        }
    ]
}

with open("dig_u5.json", "w", encoding="utf-8") as f:
    json.dump(u5, f, indent=2)
print("dig_u5.json created successfully!")

with open("dig_u6.json", "w", encoding="utf-8") as f:
    json.dump(u6, f, indent=2)
print("dig_u6.json created successfully!")
