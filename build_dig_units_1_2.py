import json

# ==========================================
# UNIT 1: Number Systems, Weighted Codes & Error-Correction Codes
# ==========================================
u1 = {
    "unitNumber": 1,
    "unitId": "unit1-number-systems-codes",
    "title": "Number Systems, Weighted Codes & Error-Correction Codes",
    "description": "Fundamental arithmetic and representations in digital computers: positional radix systems (binary, octal, decimal, hexadecimal) and fractional base conversions; weighted binary codes (8421 BCD, 2421, 84-2-1), self-complementing codes, Excess-3, and unit-distance reflected Gray codes; alphanumeric standards (7-bit and 8-bit ASCII) and parity generation; Richard Hamming's single error-correcting, double error-detecting (SEC-DED) block code syndrome analysis; and hardware code converter circuit architectures.",
    "sections": [
        {
            "id": "dig-1-1",
            "title": "Positional Number Systems: Radix Conversions & Fractional Arithmetic",
            "simulation": "dig-radix-converter-sim",
            "content": r"""<h4>1. General Radix Positional Number Representation</h4>
<p>In digital electronics, numbers are represented in a positional numeral system characterized by a <strong>base or radix ($r$)</strong>. Any real number $N$ possessing an integer part of $n$ digits and a fractional part of $m$ digits is expanded mathematically as a polynomial power series:</p>
<div class="math-display">
$$(N)_r = \sum_{i=-m}^{n-1} d_i \cdot r^i = d_{n-1} r^{n-1} + \dots + d_1 r^1 + d_0 r^0 + d_{-1} r^{-1} + \dots + d_{-m} r^{-m}$$
</div>
<p>where $d_i \in \{0, 1, \dots, r - 1\}$ represents the digit coefficient at weight $r^i$, and the period separating $d_0$ and $d_{-1}$ is the <strong>radix point</strong>. The four primary radices utilized in digital computation are:</p>
<ul>
<li><strong>Binary ($r = 2$):</strong> Digits (bits) $d_i \in \{0, 1\}$. Direct physical mapping to transistor cut-off and saturation states.</li>
<li><strong>Octal ($r = 8 = 2^3$):</strong> Digits $d_i \in \{0, 1, 2, 3, 4, 5, 6, 7\}$. Exactly three binary bits map to one octal digit.</li>
<li><strong>Decimal ($r = 10$):</strong> Digits $d_i \in \{0, 1, \dots, 9\}$. Standard human arithmetic convention.</li>
<li><strong>Hexadecimal ($r = 16 = 2^4$):</strong> Digits $d_i \in \{0, 1, \dots, 9, \text{A}(10), \text{B}(11), \text{C}(12), \text{D}(13), \text{E}(14), \text{F}(15)\}$. Exactly four binary bits (one nibble) map to one hexadecimal digit. Widely used for byte addresses and machine opcode representations.</li>
</ul>

<h4>2. Base Conversion Algorithms</h4>
<ol>
<li><strong>Radix-$r$ to Decimal:</strong> Directly evaluate the polynomial expansion $\sum d_i r^i$ using decimal arithmetic. For example:
<div class="math-display">
$$(11010.11)_2 = 1\cdot 2^4 + 1\cdot 2^3 + 0\cdot 2^2 + 1\cdot 2^1 + 0\cdot 2^0 + 1\cdot 2^{-1} + 1\cdot 2^{-2} = 16 + 8 + 2 + 0.5 + 0.25 = (26.75)_{10}$$
</div></li>
<li><strong>Decimal to Radix-$r$ (Successive Division / Multiplication):</strong>
<ul>
<li><strong>Integer Part:</strong> Repeatedly divide the decimal integer by radix $r$. The remainder generated at division step $k$ forms digit $d_k$, terminating when the quotient reaches zero. The first remainder is the <em>Least Significant Digit (LSD)</em>; the final remainder is the <em>Most Significant Digit (MSD)</em>.</li>
<li><strong>Fractional Part:</strong> Repeatedly multiply the fractional remainder by radix $r$. The integer carry extracted at each step forms digit $d_{-k}$, proceeding until the product terminates or reaches the desired precision. The first extracted integer is the most significant fractional digit $d_{-1}$.</li>
</ul></li>
<li><strong>Binary $\leftrightarrow$ Octal $\leftrightarrow$ Hexadecimal Grouping:</strong> Because $8 = 2^3$ and $16 = 2^4$, conversion between binary, octal, and hexadecimal requires zero polynomial arithmetic. Simply partition the binary string into groups of 3 bits (octal) or 4 bits (hexadecimal) radiating outward from the radix point, padding with leading and trailing zeros as necessary.</li>
</ol>"""
        },
        {
            "id": "dig-1-2",
            "title": "Weighted BCD Codes, Excess-3 & Reflected Gray Code",
            "content": r"""<h4>1. Binary Coded Decimal (BCD) & Weighted 4-Bit Codes</h4>
<p>To interface digital hardware with decimal displays without full binary polynomial division, decimal digits $0 - 9$ are encoded individually using 4-bit binary codewords. In a <strong>weighted code</strong>, each bit position $j$ is assigned an explicit numerical weight $w_j$, such that the decimal value is:</p>
<div class="math-display">
$$D = \sum_{j=0}^{3} b_j w_j \quad (b_j \in \{0, 1\})$$
</div>
<ul>
<li><strong>8421 BCD (Natural BCD):</strong> The standard weights are $w_3 = 8, w_2 = 4, w_1 = 2, w_0 = 1$. The 10 decimal digits map directly to binary patterns $0000_2$ through $1001_2$. The remaining six 4-bit patterns ($1010_2$ to $1111_2$, values 10 to 15) are <strong>forbidden / invalid states</strong> that never occur in legitimate BCD words.</li>
<li><strong>Self-Complementing Codes (2421 & Excess-3):</strong> A code is <em>self-complementing</em> if the 9's complement of any decimal digit $D$ (i.e., $9 - D$) is obtained simply by taking the 1's complement (inverting all bits $b_j \to \bar{b}_j$) of its codeword.
<ul>
<li><strong>2421 Code (Aikens Code):</strong> Weights $(2, 4, 2, 1)$ where $\sum w_j = 9$. Digit $2$ is $0010_2$, and its 9's complement $7$ is $1101_2 = \overline{0010}_2$.</li>
<li><strong>Excess-3 (XS-3) Code:</strong> An unweighted self-complementing code derived by adding $3_{10} = 0011_2$ to each natural 8421 BCD digit. For digit $0$: $0011_2$; for digit $9$: $1100_2 = \overline{0011}_2$. Excess-3 simplifies decimal subtraction in early mechanical and electronic ALUs.</li>
</ul></li>
<li><strong>Negative Weight Codes ($84\text{-}2\text{-}1$):</strong> Possesses weights $w_3 = 8, w_2 = 4, w_1 = -2, w_0 = -1$. For example, decimal $5$ is encoded as $1\cdot 8 + 0\cdot 4 + 1\cdot(-2) + 1\cdot(-1) = 8 - 3 = 5$, represented by $1011_2$.</li>
</ul>

<h4>2. The Unit-Distance Reflected Gray Code</h4>
<p>Frank Gray (1953) developed the <strong>reflected binary Gray code</strong>, an unweighted cyclic code exhibiting the critical property of <strong>unit distance</strong>: between any two adjacent decimal numbers $k$ and $k+1$, <strong>exactly one bit changes state</strong>.</p>
<p>In electromechanical shaft optical encoders, converting angular position using natural binary can produce disastrous transient read errors. If a shaft transitions from $7$ ($0111_2$) to $8$ ($1000_2$), all four bits must flip simultaneously. Because physical photodetectors cannot switch with infinitesimal synchronicity, intermediate false states (e.g., $1111_2 = 15$) can be latched momentarily. The Gray code eliminates this hazard entirely.</p>
<p><strong>Binary to Gray Conversion Algorithm:</strong> Given binary word $B = b_n b_{n-1} \dots b_0$ and Gray codeword $G = g_n g_{n-1} \dots g_0$:</p>
<div class="math-display">
$$g_n = b_n, \quad g_i = b_{i+1} \oplus b_i \quad (i = 0, 1, \dots, n-1)$$
</div>
<p><strong>Gray to Binary Conversion Algorithm:</strong></p>
<div class="math-display">
$$b_n = g_n, \quad b_i = b_{i+1} \oplus g_i \quad (i = 0, 1, \dots, n-1)$$
</div>"""
        },
        {
            "id": "dig-1-3",
            "title": "Alphanumeric Representation: ASCII Standard & Parity Checking",
            "content": r"""<h4>1. The ASCII Alphanumeric Encoding Standard</h4>
<p>Digital computer systems process non-numerical information (text characters, punctuation, control commands) through standardized alphanumeric binary lookup codes. The <strong>American Standard Code for Information Interchange (ASCII)</strong> is a 7-bit encoding scheme capable of defining $2^7 = 128$ distinct characters:</p>
<ul>
<li><strong>32 Control Characters ($00_{16} - 1\text{F}_{16}$):</strong> Non-printable device instructions (NUL: $00_{16}$, SOH: $01_{16}$, STX: $02_{16}$, ACK: $06_{16}$, BEL: $07_{16}$, BS: $08_{16}$, LF: $0\text{A}_{16}$, CR: $0\text{D}_{16}$, ESC: $1\text{B}_{16}$).</li>
<li><strong>96 Printable Characters ($20_{16} - 7\text{E}_{16}$):</strong> Comprising space ($20_{16}$), decimal digits '0'-'9' ($30_{16} - 39_{16}$), uppercase letters 'A'-'Z' ($41_{16} - 5\text{A}_{16}$), lowercase letters 'a'-'z' ($61_{16} - 7\text{A}_{16}$), and mathematical/punctuation symbols. Note that toggling bit 5 ($20_{16}$) converts between uppercase and lowercase letters (e.g., 'A' is $01000001_2$, 'a' is $01100001_2$).</li>
<li><strong>Extended 8-Bit ASCII ($00_{16} - \text{FF}_{16}$):</strong> Adds 128 characters ($80_{16} - \text{FF}_{16}$) for accented European letters, box-drawing graphics, and Greek scientific symbols.</li>
</ul>

<h4>2. Parity Bit Generation & Single-Bit Error Detection</h4>
<p>During data transmission across communication channels or memory buses, electrical noise, thermal fluctuations, or cosmic radiation can flip a binary bit ($0 \to 1$ or $1 \to 0$). The simplest hardware mechanism for error detection is the appendance of a <strong>parity bit ($P$)</strong>:</p>
<ul>
<li><strong>Even Parity:</strong> The parity bit $P$ is chosen so that the total count of 1s in the transmitted codeword (data bits plus parity bit) is strictly <strong>even</strong>. For an $n$-bit data vector $D = (d_{n-1}, \dots, d_0)$, the even parity bit is synthesized via cascaded XOR gates:
<div class="math-display">
$$P_{\text{even}} = d_{n-1} \oplus d_{n-2} \oplus \dots \oplus d_1 \oplus d_0$$
</div></li>
<li><strong>Odd Parity:</strong> The parity bit $P$ is chosen so that the total count of 1s is strictly <strong>odd</strong>:
<div class="math-display">
$$P_{\text{odd}} = \overline{d_{n-1} \oplus d_{n-2} \oplus \dots \oplus d_0} = \overline{P_{\text{even}}}$$
</div></li>
</ul>
<p>At the receiver, an identical XOR parity checker computes the parity of the received packet. If a single bit flips, the parity check fails, triggering an error interrupt. However, single-bit parity cannot detect <em>double-bit errors</em> (which restore parity count) and provides zero information regarding which specific bit flipped, rendering error correction impossible.</p>"""
        },
        {
            "id": "dig-1-4",
            "title": "Hamming Error-Correcting Code: SEC-DED Architecture",
            "simulation": "dig-hamming-code-sim",
            "content": r"""<h4>1. Richard Hamming's Geometric Code Distance Theory (1950)</h4>
<p>To enable automated in-flight error correction in telecommunications and memory ECC (Error-Correcting Code), Richard Hamming introduced the concept of <strong>Hamming Distance ($d_{\text{min}}$)</strong>, defined as the minimum number of bit positions in which any two valid codewords differ.</p>
<p>For a code to detect up to $t$ simultaneous bit errors and correct up to $c$ bit errors, the minimum Hamming distance must satisfy:</p>
<div class="math-display">
$$d_{\text{min}} \ge 2c + t + 1 \quad (c \le t)$$
</div>
<ul>
<li>To <strong>detect</strong> $t = 1$ single error: $d_{\text{min}} \ge 1 + 1 = 2$ (simple parity bit).</li>
<li>To <strong>correct</strong> $c = 1$ single error: $d_{\text{min}} \ge 2(1) + 1 = 3$ (standard Hamming code).</li>
<li>To <strong>correct single errors and detect double errors (SEC-DED)</strong>: $d_{\text{min}} \ge 2(1) + 1 + 1 = 4$ (Hamming code with overall parity bit).</li>
</ul>

<h4>2. Construction of the Hamming (7,4) Single-Error-Correcting Code</h4>
<p>Consider transmitting $m = 4$ data bits ($D_7, D_6, D_5, D_3$). To isolate the location of any single-bit error among the $n = m + k$ bits transmitted, or verify error-free transmission, the $k$ parity check bits must represent at least $n + 1$ distinct states:</p>
<div class="math-display">
$$2^k \ge m + k + 1 \implies 2^k \ge n + 1$$
</div>
<p>For $m = 4$, setting $k = 3$ satisfies $2^3 = 8 \ge 4 + 3 + 1 = 8$. Thus, $n = 7$ total bits are transmitted: 4 data bits and 3 parity bits.</p>
<p><strong>Parity Bit Placement:</strong> Parity bits $P_1, P_2, P_4$ are assigned to bit positions that are exact powers of 2 ($1, 2, 4$). The remaining positions ($3, 5, 6, 7$) hold the data bits:</p>
<div class="table-responsive">
<table class="table table-bordered">
<thead>
<tr><th>Bit Position</th><th>7</th><th>6</th><th>5</th><th>4</th><th>3</th><th>2</th><th>1</th></tr>
</thead>
<tbody>
<tr><td><strong>Binary Position Index</strong></td><td>$111_2$</td><td>$110_2$</td><td>$101_2$</td><td>$100_2$</td><td>$011_2$</td><td>$010_2$</td><td>$001_2$</td></tr>
<tr><td><strong>Bit Assignment</strong></td><td>$D_7$</td><td>$D_6$</td><td>$D_5$</td><td>$P_4$</td><td>$D_3$</td><td>$P_2$</td><td>$P_1$</td></tr>
</tbody>
</table>
</div>
<p>Each parity bit enforces even parity over all bit positions whose binary index contains a 1 in that parity bit's respective binary position:</p>
<div class="math-display">
$$P_1 = D_3 \oplus D_5 \oplus D_7 \quad (\text{Positions } 1, 3, 5, 7 \text{ have bit 0 = 1})$$
</div>
<div class="math-display">
$$P_2 = D_3 \oplus D_6 \oplus D_7 \quad (\text{Positions } 2, 3, 6, 7 \text{ have bit 1 = 1})$$
</div>
<div class="math-display">
$$P_4 = D_5 \oplus D_6 \oplus D_7 \quad (\text{Positions } 4, 5, 6, 7 \text{ have bit 2 = 1})$$
</div>

<h4>3. Syndrome Decoding and Hardware Error Correction</h4>
<p>At the receiver, the 7 received bits ($r_7, r_6, r_5, r_4, r_3, r_2, r_1$) are processed by three parity-check XOR trees to calculate the 3-bit <strong>Syndrome Vector $S = (S_4 S_2 S_1)$</strong>:</p>
<div class="math-display">
$$S_1 = r_1 \oplus r_3 \oplus r_5 \oplus r_7, \quad S_2 = r_2 \oplus r_3 \oplus r_6 \oplus r_7, \quad S_4 = r_4 \oplus r_5 \oplus r_6 \oplus r_7$$
</div>
<ul>
<li>If $S = 000_2$: No error occurred; data is valid.</li>
<li>If $S = S_4 S_2 S_1 \neq 0$: The binary integer value of $S$ points <strong>directly to the exact erroneous bit position</strong> ($1$ through $7$). The hardware simply inverts that specific bit ($r_S \leftarrow \overline{r_S}$) using an XOR gate driven by a 3-to-8 decoder, achieving automated instantaneous hardware error correction.</li>
</ul>"""
        },
        {
            "id": "dig-1-5",
            "title": "Hardware Code Converters: BCD, Gray & Excess-3 Logic",
            "content": r"""<h4>1. Combinational Code Conversion Architecture</h4>
<p>A digital code converter is an $n$-input, $m$-output combinational logic circuit that accepts input words represented in code $\mathcal{A}$ and produces equivalent codewords in code $\mathcal{B}$. The synthesis procedure follows systematic Boolean optimization:</p>
<ol>
<li>Construct a comprehensive truth table mapping each valid input codeword to its desired output codeword.</li>
<li>Treat unused or invalid input combinations as <strong>Don't Care states ($\times$)</strong> to maximize logic gate reduction.</li>
<li>Derive minimized Sum-of-Products (SOP) expressions for each output bit using Karnaugh maps or Quine-McCluskey tabulation.</li>
</ol>

<h4>2. Binary-to-Gray and Gray-to-Binary Hardware Circuits</h4>
<p>From the conversion equations $g_i = b_{i+1} \oplus b_i$, a 4-bit Binary-to-Gray converter requires only three two-input XOR gates:</p>
<div class="math-display">
$$g_3 = b_3, \quad g_2 = b_3 \oplus b_2, \quad g_1 = b_2 \oplus b_1, \quad g_0 = b_1 \oplus b_0$$
</div>
<p>Similarly, the Gray-to-Binary converter $b_i = b_{i+1} \oplus g_i$ utilizes three XOR gates in a ripple-feedback cascade:</p>
<div class="math-display">
$$b_3 = g_3, \quad b_2 = g_3 \oplus g_2, \quad b_1 = b_2 \oplus g_1, \quad b_0 = b_1 \oplus g_0$$
</div>

<h4>3. BCD-to-Excess-3 Hardware Synthesis</h4>
<p>To convert an 8421 BCD digit $(B_3, B_2, B_1, B_0)$ to Excess-3 $(E_3, E_2, E_1, E_0)$, the circuit adds $0011_2$. For input minterms $m_{10}$ through $m_{15}$, the outputs are defined as Don't Cares ($\times$). Minimizing via 4-variable K-maps yields:</p>
<div class="math-display">
$$E_0 = \overline{B_0}$$
</div>
<div class="math-display">
$$E_1 = B_1 \oplus B_0 = B_1 \overline{B_0} + \overline{B_1} B_0$$
</div>
<div class="math-display">
$$E_2 = B_2 \oplus (B_1 + B_0) = \overline{B_2}(B_1 + B_0) + B_2 \overline{B_1}\,\overline{B_0}$$
</div>
<div class="math-display">
$$E_3 = B_3 + B_2(B_1 + B_0) = B_3 + B_2 B_1 + B_2 B_0$$
</div>
<p>This compact logic network requires only four standard logic gates, illustrating the power of exploiting Don't Care conditions.</p>"""
        }
    ],
    "problems": [
        {
            "id": "dig-p-1-1",
            "title": "Fractional Base Conversion: Decimal to Binary, Octal and Hexadecimal",
            "statement": "Given the decimal number $N = (109.6875)_{10}$: (a) Convert the integer part $(109)_{10}$ and fractional part $(0.6875)_{10}$ into binary using successive division and multiplication. (b) Convert the resulting binary representation directly into Octal and Hexadecimal by bit grouping. (c) Verify your hexadecimal result by expanding $(N)_{16}$ back into decimal polynomial form.",
            "steps": [
                {
                    "stepName": "Step 1: Successive Division of Integer Part (109)",
                    "math": r"109 / 2 = 54 \text{ R } 1 \ (d_0), \quad 54 / 2 = 27 \text{ R } 0, \quad 27 / 2 = 13 \text{ R } 1, \quad 13 / 2 = 6 \text{ R } 1, \quad 6 / 2 = 3 \text{ R } 0, \quad 3 / 2 = 1 \text{ R } 1, \quad 1 / 2 = 0 \text{ R } 1 \ (d_6)",
                    "explanation": "Reading remainders from bottom to top yields (109)_10 = (1101101)_2."
                },
                {
                    "stepName": "Step 2: Successive Multiplication of Fractional Part (0.6875)",
                    "math": r"0.6875 \times 2 = 1.375 \ (\text{carry } 1), \quad 0.375 \times 2 = 0.75 \ (\text{carry } 0), \quad 0.75 \times 2 = 1.50 \ (\text{carry } 1), \quad 0.50 \times 2 = 1.00 \ (\text{carry } 1)",
                    "explanation": "Reading integer carries top to bottom yields (0.6875)_10 = (0.1011)_2. Combining: (109.6875)_10 = (1101101.1011)_2."
                },
                {
                    "stepName": "Step 3: Direct Grouping to Octal (Base 8)",
                    "math": r"(001 \ 101 \ 101 \ . \ 101 \ 100)_2 = (1 \ 5 \ 5 \ . \ 5 \ 4)_8 = (155.54)_8",
                    "explanation": "Pad left with zeros to 9 integer bits and right with zeros to 6 fractional bits; evaluate triads: 001=1, 101=5, 101=5, 101=5, 100=4."
                },
                {
                    "stepName": "Step 4: Direct Grouping to Hexadecimal (Base 16)",
                    "math": r"(0110 \ 1101 \ . \ 1011)_2 = (6 \ \text{D} \ . \ \text{B})_{16} = (6\text{D.B})_{16}",
                    "explanation": "Pad left to 8 integer bits; evaluate tetrads: 0110 = 6, 1101 = 13 = D, 1011 = 11 = B."
                },
                {
                    "stepName": "Step 5: Verification of Hexadecimal Representation",
                    "math": r"6 \times 16^1 + 13 \times 16^0 + 11 \times 16^{-1} = 96 + 13 + \frac{11}{16} = 109 + 0.6875 = 109.6875_{10}",
                    "explanation": "Exact decimal match confirms 100% precision."
                }
            ],
            "answer": "(109.6875)_{10} = (1101101.1011)_2 = (155.54)_8 = (6\\text{D.B})_{16}"
        },
        {
            "id": "dig-p-1-2",
            "title": "Hamming (7,4) Code Encoding, Transmission Error and Syndrome Correction",
            "statement": "A 4-bit data word $D = 1011_2$ ($D_7 = 1, D_6 = 0, D_5 = 1, D_3 = 1$) is to be transmitted using an even-parity Hamming (7,4) code. (a) Determine the parity bits $P_1, P_2, P_4$ and write the complete 7-bit transmitted codeword. (b) During transmission, an electrical noise burst flips bit 5 ($r_5: 1 \to 0$). Calculate the syndrome vector $S = (S_4 S_2 S_1)$ at the receiver. (c) Show how the syndrome vector pinpoints the error and state the corrected word.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate Parity Check Bits",
                    "math": r"P_1 = D_3 \oplus D_5 \oplus D_7 = 1 \oplus 1 \oplus 1 = 1, \quad P_2 = D_3 \oplus D_6 \oplus D_7 = 1 \oplus 0 \oplus 1 = 0, \quad P_4 = D_5 \oplus D_6 \oplus D_7 = 1 \oplus 0 \oplus 1 = 0",
                    "explanation": "Evaluate even parity check equations for positions 1, 2, 4."
                },
                {
                    "stepName": "Step 2: Construct the Transmitted 7-bit Codeword",
                    "math": r"C = (D_7 D_6 D_5 P_4 D_3 P_2 P_1) = (1 \ 0 \ 1 \ 0 \ 1 \ 0 \ 1)_2",
                    "explanation": "The transmitted codeword is 1010101_2."
                },
                {
                    "stepName": "Step 3: Evaluate Received Word with Error at Bit 5",
                    "math": r"\text{Bit 5 flips: } D_5 = 1 \to 0. \implies R = (r_7 r_6 r_5 r_4 r_3 r_2 r_1) = (1 \ 0 \ 0 \ 0 \ 1 \ 0 \ 1)_2",
                    "explanation": "Bit position 5 now contains 0 instead of 1."
                },
                {
                    "stepName": "Step 4: Compute Receiver Syndrome Vector",
                    "math": r"S_1 = r_1 \oplus r_3 \oplus r_5 \oplus r_7 = 1 \oplus 1 \oplus 0 \oplus 1 = 1, \quad S_2 = r_2 \oplus r_3 \oplus r_6 \oplus r_7 = 0 \oplus 1 \oplus 0 \oplus 1 = 0, \quad S_4 = r_4 \oplus r_5 \oplus r_6 \oplus r_7 = 0 \oplus 0 \oplus 0 \oplus 1 = 1",
                    "explanation": "Compute syndrome bits S1, S2, S4."
                },
                {
                    "stepName": "Step 5: Identify Error Location and Invert",
                    "math": r"S = (S_4 S_2 S_1) = (1 \ 0 \ 1)_2 = 5_{10}. \implies \text{Error is at Bit Position 5!}",
                    "explanation": "The syndrome decimal value 5 indicates bit 5 is inverted. Inverting r_5: 0 -> 1 restores the original transmitted codeword C = 1010101_2."
                }
            ],
            "answer": "C = 1010101_2, \\quad S = (101)_2 = 5_{10} \\implies \\text{Error in Bit 5 Corrected to } 1010101_2"
        },
        {
            "id": "dig-p-1-3",
            "title": "Reflected Gray Code Synthesis and Multi-Bit State Traversal",
            "statement": "An absolute optical shaft rotary encoder with $N = 16$ angular sectors ($22.5^\\circ$ resolution) encodes shaft positions $0$ through $15$. (a) Construct the 4-bit Binary and reflected Gray codewords for decimal sector positions $7$, $8$, and $9$. (b) Calculate the number of simultaneously switching bits during the transition from sector $7$ to $8$ in natural binary versus Gray code. (c) Using the conversion formulas, mathematically derive the Gray codeword for binary $B = (1101)_2$ ($13_{10}$).",
            "steps": [
                {
                    "stepName": "Step 1: Binary Codewords for Sectors 7, 8, 9",
                    "math": r"7_{10} = 0111_2, \quad 8_{10} = 1000_2, \quad 9_{10} = 1001_2",
                    "explanation": "Write 4-bit natural binary representations."
                },
                {
                    "stepName": "Step 2: Generate Reflected Gray Codewords",
                    "math": r"G(7) = 0111 \oplus 0011 = 0100_2, \quad G(8) = 1000 \oplus 0100 = 1100_2, \quad G(9) = 1001 \oplus 0100 = 1101_2",
                    "explanation": "Compute Gray code for each sector."
                },
                {
                    "stepName": "Step 3: Compare Transition Bit Flips (Sector 7 to 8)",
                    "math": r"\text{Binary: } 0111_2 \to 1000_2 \implies \text{Hamming distance } d = 4 \ (\text{All 4 bits flip simultaneously!})",
                    "explanation": "Natural binary undergoes 4 simultaneous bit transitions, creating severe asynchronous timing hazards."
                },
                {
                    "stepName": "Step 4: Evaluate Gray Transition Distance",
                    "math": r"\text{Gray: } 0100_2 \to 1100_2 \implies \text{Hamming distance } d = 1 \ (\text{Only MSB flips from 0 to 1})",
                    "explanation": "Gray code switches exactly 1 bit, completely eliminating encoder transition glitches."
                },
                {
                    "stepName": "Step 5: Convert Binary 1101 to Gray",
                    "math": r"g_3 = b_3 = 1, \quad g_2 = b_3 \oplus b_2 = 1 \oplus 1 = 0, \quad g_1 = b_2 \oplus b_1 = 1 \oplus 0 = 1, \quad g_0 = b_1 \oplus b_0 = 0 \oplus 1 = 1 \implies G = (1011)_2",
                    "explanation": "Apply conversion equations bit-by-bit."
                }
            ],
            "answer": "G(7)=0100_2, \\ G(8)=1100_2 \\ (d=1 \\text{ vs } d=4 \\text{ in binary}); \\quad G(1101_2) = 1011_2"
        }
    ]
}

# ==========================================
# UNIT 2: Boolean Algebra, Logic Gates & Semiconductor Logic Families
# ==========================================
u2 = {
    "unitNumber": 2,
    "unitId": "unit2-boolean-algebra-logic-gates",
    "title": "Boolean Algebra, Logic Gates & Semiconductor Logic Families",
    "description": "Mathematical foundations and solid-state physical implementation of digital logic: George Boole's algebraic axioms and Huntington's postulates; duality principle; De Morgan's laws and algebraic multi-variable reduction; canonical digital logic gates (AND, OR, NOT, NAND, NOR, XOR, XNOR); functional completeness and universal gate synthesis (NAND-only and NOR-only networks); bipolar Transistor-Transistor Logic (TTL Totem-Pole) and complementary MOS (CMOS) inverter circuit electronics; propagation delay, fan-out, power dissipation, and high/low noise margins.",
    "sections": [
        {
            "id": "dig-2-1",
            "title": "Huntington's Postulates, Algebraic Axioms & The Duality Principle",
            "content": r"""<h4>1. Formal Mathematical Axioms of Boolean Algebra</h4>
<p>In 1904, Edward V. Huntington formalized George Boole's algebraic logic as a deductive mathematical system defined on a set of elements $B$ with two binary operators: logical OR ($+$) and logical AND ($\cdot$), satisfying six fundamental postulates:</p>
<ol>
<li><strong>Closure:</strong> For every $x, y \in B$:
<div class="math-display">
$$x + y \in B \quad \text{and} \quad x \cdot y \in B$$
</div></li>
<li><strong>Identity Elements:</strong> There exist unique elements $0, 1 \in B$ such that for every $x \in B$:
<div class="math-display">
$$x + 0 = x \quad \text{and} \quad x \cdot 1 = x$$
</div></li>
<li><strong>Commutative Laws:</strong> For every $x, y \in B$:
<div class="math-display">
$$x + y = y + x \quad \text{and} \quad x \cdot y = y \cdot x$$
</div></li>
<li><strong>Distributive Laws:</strong> Each operator distributes over the other:
<div class="math-display">
$$x \cdot (y + z) = (x \cdot y) + (x \cdot z)$$
</div>
<div class="math-display">
$$x + (y \cdot z) = (x + y) \cdot (x + z) \quad (\text{Crucial rule with no ordinary algebra analog!})$$
</div></li>
<li><strong>Complement:</strong> For every $x \in B$, there exists a unique complement $\bar{x} \in B$ such that:
<div class="math-display">
$$x + \bar{x} = 1 \quad \text{and} \quad x \cdot \bar{x} = 0$$
</div></li>
<li><strong>Distinct Elements:</strong> There exist at least two elements $x, y \in B$ such that $x \ne y$.</li>
</ol>

<h4>2. Fundamental Theorems of Boolean Algebra</h4>
<p>From Huntington's postulates, the standard operational theorems are deduced:</p>
<ul>
<li><strong>Idempotence:</strong> $x + x = x$ and $x \cdot x = x$.</li>
<li><strong>Null Elements (Dominance):</strong> $x + 1 = 1$ and $x \cdot 0 = 0$.</li>
<li><strong>Involution (Double Negation):</strong> $\overline{\bar{x}} = x$.</li>
<li><strong>Absorption Laws:</strong>
<div class="math-display">
$$x + (x \cdot y) = x \quad \text{and} \quad x \cdot (x + y) = x$$
</div>
<div class="math-display">
$$x + (\bar{x} \cdot y) = x + y \quad \text{and} \quad x \cdot (\bar{x} + y) = x \cdot y$$
</div></li>
<li><strong>Associative Laws:</strong>
<div class="math-display">
$$x + (y + z) = (x + y) + z \quad \text{and} \quad x \cdot (y \cdot z) = (x \cdot y) \cdot z$$
</div></li>
</ul>

<h4>3. The Principle of Duality</h4>
<p>The <strong>Principle of Duality</strong> states: <em>Any true Boolean algebraic identity remains strictly valid if the operators $+$ and $\cdot$ are interchanged, and the identity elements $0$ and $1$ are simultaneously interchanged.</em></p>
<p>For example, the dual of the distributive law $x \cdot (y + z) = (x \cdot y) + (x \cdot z)$ is directly obtained by swapping $\cdot \leftrightarrow +$:</p>
<div class="math-display">
$$x + (y \cdot z) = (x + y) \cdot (x + z)$$
</div>
<p>Duality halves the labor of Boolean mathematical proofs: proving one theorem automatically validates its dual.</p>"""
        },
        {
            "id": "dig-2-2",
            "title": "De Morgan's Theorems & Multi-Variable Function Reduction",
            "content": r"""<h4>1. Augustus De Morgan's Laws</h4>
<p>Augustus De Morgan (1847) established the two most celebrated theorems in digital circuit design, defining the rigorous relationship between conjunction, disjunction, and complementation:</p>
<div class="math-display">
$$\overline{A + B} = \bar{A} \cdot \bar{B} \quad (\text{The complement of a logical sum is the product of the complements})$$
</div>
<div class="math-display">
$$\overline{A \cdot B} = \bar{A} + \bar{B} \quad (\text{The complement of a logical product is the sum of the complements})$$
</div>
<p>In digital circuit topology, De Morgan's laws state that a NOR gate (OR followed by inversion) is functionally identical to an AND gate with inverted inputs (negative-AND), and a NAND gate is identical to a negative-OR gate:</p>
<div class="math-display">
$$\text{NOR}(A, B) \equiv \text{Negative-AND}(\bar{A}, \bar{B}), \qquad \text{NAND}(A, B) \equiv \text{Negative-OR}(\bar{A}, \bar{B})$$
</div>

<h4>2. Generalized Generalized Multi-Variable Formulation</h4>
<p>By mathematical induction, De Morgan's laws extend to an arbitrary number of $n$ variables:</p>
<div class="math-display">
$$\overline{A_1 + A_2 + \dots + A_n} = \bar{A}_1 \cdot \bar{A}_2 \dots \bar{A}_n$$
</div>
<div class="math-display">
$$\overline{A_1 \cdot A_2 \dots A_n} = \bar{A}_1 + \bar{A}_2 + \dots + \bar{A}_n$$
</div>
<p>To complement any arbitrary Boolean function $F(A, B, C, \dots, +, \cdot)$, one simultaneously applies De Morgan's rule across all levels: interchange all $+$ and $\cdot$ operators, and complement every individual literal ($A \to \bar{A}$ and $\bar{A} \to A$).</p>

<h4>3. The Consensus Theorem</h4>
<p>The <strong>Consensus Theorem</strong> provides a powerful shortcut for eliminating redundant terms in multi-variable equations without tedious K-map expansion:</p>
<div class="math-display">
$$A B + \bar{A} C + B C = A B + \bar{A} C$$
</div>
<p>where $B C$ is the <em>consensus term</em> formed from the conjunction of the two literals associated with the complemented pair $A$ and $\bar{A}$. In its dual form:</p>
<div class="math-display">
$$(A + B)(\bar{A} + C)(B + C) = (A + B)(\bar{A} + C)$$
</div>"""
        },
        {
            "id": "dig-2-3",
            "title": "Canonical Logic Gates: AND, OR, NOT, NAND, NOR, XOR & XNOR",
            "simulation": "dig-logic-gate-explorer-sim",
            "content": r"""<h4>1. Basic Logic Gates and Operational Truth Tables</h4>
<p>Digital logic gates are physical electronic circuits that perform elementary Boolean switching operations on binary voltage signals ($V_{LOW} \leftrightarrow 0$, $V_{HIGH} \leftrightarrow 1$):</p>
<ol>
<li><strong>NOT Gate (Inverter):</strong> Implements single-input complementation: $Y = \bar{A}$. If $A=0$, $Y=1$; if $A=1$, $Y=0$.</li>
<li><strong>AND Gate:</strong> Output is HIGH if and only if all inputs are HIGH: $Y = A \cdot B$.</li>
<li><strong>OR Gate:</strong> Output is HIGH if at least one input is HIGH: $Y = A + B$.</li>
<li><strong>NAND Gate:</strong> Negated AND operation: $Y = \overline{A \cdot B}$. Output is LOW if and only if all inputs are HIGH.</li>
<li><strong>NOR Gate:</strong> Negated OR operation: $Y = \overline{A + B}$. Output is HIGH if and only if all inputs are LOW.</li>
</ol>

<h4>2. Exclusive-OR (XOR) & Exclusive-NOR (XNOR) Gates</h4>
<p>The <strong>XOR gate ($\oplus$)</strong>, or modulo-2 adder, yields a HIGH output when the inputs are <em>different</em>:</p>
<div class="math-display">
$$Y = A \oplus B = A \bar{B} + \bar{A} B$$
</div>
<p>Properties of XOR:</p>
<ul>
<li>$A \oplus 0 = A$, \quad $A \oplus 1 = \bar{A}$ (programmable inverter).</li>
<li>$A \oplus A = 0$, \quad $A \oplus \bar{A} = 1$.</li>
<li>Commutative: $A \oplus B = B \oplus A$; Associative: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$.</li>
<li>For $n$ inputs, an XOR gate acts as an <strong>odd parity detector</strong>: output is 1 if and only if an odd number of inputs are 1.</li>
</ul>
<p>The <strong>XNOR gate ($\odot$)</strong>, or equivalence detector, produces a HIGH output when the inputs are <em>identical</em>:</p>
<div class="math-display">
$$Y = A \odot B = \overline{A \oplus B} = A B + \bar{A} \bar{B}$$
</div>"""
        },
        {
            "id": "dig-2-4",
            "title": "Universal Gate Synthesis: NAND-Only & NOR-Only Networks",
            "content": r"""<h4>1. Functional Completeness in Digital Logic</h4>
<p>A set of Boolean operators is defined as <strong>functionally complete</strong> if every arbitrary Boolean function can be expressed solely using operators from that set. The standard set $\{\text{AND}, \text{OR}, \text{NOT}\}$ is functionally complete. However, fabricating multiple distinct gate types on an integrated circuit increases silicon area and manufacturing complexity.</p>
<p>A <strong>Universal Gate</strong> is a single gate type capable of synthesizing all elementary logic functions (NOT, AND, OR, XOR) without requiring any other components. There exist precisely two universal logic gates in digital electronics: <strong>NAND</strong> and <strong>NOR</strong>.</p>

<h4>2. NAND-Only Gate Realizations</h4>
<ol>
<li><strong>NOT using NAND:</strong> Tie both inputs together:
<div class="math-display">
$$\overline{A \cdot A} = \bar{A}$$
</div></li>
<li><strong>AND using NAND:</strong> Feed the output of a NAND gate into a NAND-inverter:
<div class="math-display">
$$\overline{\overline{A \cdot B}} = A \cdot B \quad (\text{2 NAND gates})$$
</div></li>
<li><strong>OR using NAND:</strong> Invert each input with a NAND gate, then feed into a third NAND gate (De Morgan's law):
<div class="math-display">
$$\overline{\bar{A} \cdot \bar{B}} = \overline{\bar{A}} + \overline{\bar{B}} = A + B \quad (\text{3 NAND gates})$$
</div></li>
<li><strong>NOR using NAND:</strong> Invert the output of the NAND-synthesized OR gate:
<div class="math-display">
$$\overline{A + B} \quad (\text{4 NAND gates})$$
</div></li>
<li><strong>XOR using NAND:</strong> Synthesize $A \bar{B} + \bar{A} B$ with minimum four 2-input NAND gates:
<div class="math-display">
$$X = \overline{A B}, \quad Y = \overline{A \cdot X} \cdot \overline{B \cdot X} = A \oplus B \quad (\text{4 NAND gates})$$
</div></li>
</ol>

<h4>3. NOR-Only Gate Realizations</h4>
<ol>
<li><strong>NOT using NOR:</strong> Tie both inputs together: $\overline{A + A} = \bar{A}$ (1 NOR gate).</li>
<li><strong>OR using NOR:</strong> Invert the NOR output: $\overline{\overline{A + B}} = A + B$ (2 NOR gates).</li>
<li><strong>AND using NOR:</strong> Invert each input, then combine in a NOR gate: $\overline{\bar{A} + \bar{B}} = A \cdot B$ (3 NOR gates).</li>
<li><strong>NAND using NOR:</strong> Invert the output of the NOR-synthesized AND gate (4 NOR gates).</li>
<li><strong>XOR using NOR:</strong> Synthesized with five 2-input NOR gates.</li>
</ol>"""
        },
        {
            "id": "dig-2-5",
            "title": "Semiconductor Logic Families: TTL Totem-Pole vs CMOS Inverters",
            "simulation": "dig-ttl-cmos-inverter-sim",
            "content": r"""<h4>1. Transistor-Transistor Logic (TTL) & The Totem-Pole Output</h4>
<p>Standard BJT Transistor-Transistor Logic (7400 series) operates from a single $+5\text{ V}$ power supply ($V_{CC}$). The canonical TTL NAND gate consists of three stages:</p>
<ol>
<li><strong>Input Stage:</strong> Multi-emitter NPN transistor $Q_1$. If any input is LOW ($0.2\text{ V}$), $Q_1$ conducts base current to the LOW input, pulling $Q_1$'s collector voltage low and cutting off phase-splitter $Q_2$.</li>
<li><strong>Phase-Splitter Stage:</strong> Transistor $Q_2$ generates complementary out-of-phase drive voltages at its collector and emitter.</li>
<li><strong>Totem-Pole Output Stage:</strong> Consists of pull-up transistor $Q_4$, diode $D$, and pull-down transistor $Q_3$:
<ul>
<li><strong>Output LOW State ($Y = 0$):</strong> $Q_2$ and $Q_3$ are saturated. $Q_3$ pulls the output to $V_{OL} \approx V_{CE,\text{sat}} \approx 0.2\text{ V}$. Meanwhile, $Q_4$ is completely off because diode $D$ drops $0.7\text{ V}$, ensuring base-emitter voltage $V_{BE4}$ is insufficient to turn $Q_4$ on.</li>
<li><strong>Output HIGH State ($Y = 1$):</strong> $Q_2$ and $Q_3$ are cut off. $Q_4$ acts as an active pull-up emitter follower, charging the capacitive load rapidly to $V_{OH} = V_{CC} - V_{BE4} - V_D \approx 5.0 - 0.7 - 0.7 \approx 3.6\text{ V}$.</li>
</ul></li>
</ol>
<p>The totem-pole active pull-up provides low output impedance in both states, dramatically accelerating capacitive line charging compared to passive resistor pull-ups.</p>

<h4>2. Complementary MOS (CMOS) Inverter</h4>
<p>CMOS technology pairs an enhancement-mode pMOS pull-up transistor with an nMOS pull-down transistor in a symmetric, push-pull configuration:</p>
<ul>
<li><strong>Input LOW ($V_{\text{in}} = 0\text{ V}$):</strong> $V_{GS,n} = 0 < V_{tn} \implies$ nMOS is OFF. $V_{GS,p} = -V_{DD} < V_{tp} \implies$ pMOS is saturated/linear, pulling $V_{\text{out}}$ to exactly $V_{DD}$ with <strong>zero static current</strong>.</li>
<li><strong>Input HIGH ($V_{\text{in}} = V_{DD}$):</strong> $V_{GS,n} = V_{DD} > V_{tn} \implies$ nMOS is ON. $V_{GS,p} = 0 \implies$ pMOS is OFF. nMOS pulls $V_{\text{out}}$ to exactly $0\text{ V}$ with <strong>zero static current</strong>.</li>
<li><strong>Power Dissipation:</strong> Because one transistor is always cut off in the steady state, static power dissipation is virtually zero ($P_{\text{static}} \sim\text{nW}$). Power is consumed only during switching transitions as dynamic power:
<div class="math-display">
$$P_{\text{dynamic}} = C_L V_{DD}^2 f$$
</div>
where $C_L$ is load capacitance and $f$ is clock switching frequency.</li>
</ul>

<h4>3. Key Logic Family Performance Metrics</h4>
<div class="table-responsive">
<table class="table table-bordered">
<thead>
<tr><th>Metric</th><th>TTL (Standard 74xx)</th><th>CMOS (74HCxx / Modern)</th><th>Physical Significance</th></tr>
</thead>
<tbody>
<tr><td><strong>Supply Voltage ($V_{CC}/V_{DD}$)</strong></td><td>$5\text{ V} \pm 5\%$</td><td>$2\text{ V} - 6\text{ V}$ (Core: $0.8 - 1.8\text{ V}$)</td><td>Power rail tolerance</td></tr>
<tr><td><strong>$V_{IH,\text{min}} / V_{IL,\text{max}}$</strong></td><td>$2.0\text{ V} \ / \ 0.8\text{ V}$</td><td>$0.7 V_{DD} \ / \ 0.3 V_{DD}$</td><td>Input threshold boundaries</td></tr>
<tr><td><strong>$V_{OH,\text{min}} / V_{OL,\text{max}}$</strong></td><td>$2.4\text{ V} \ / \ 0.4\text{ V}$</td><td>$V_{DD} - 0.1\text{ V} \ / \ 0.1\text{ V}$</td><td>Output drive levels</td></tr>
<tr><td><strong>High Noise Margin ($NM_H$)</strong></td><td>$V_{OH} - V_{IH} = 2.4 - 2.0 = 0.4\text{ V}$</td><td>$V_{DD} - 0.7V_{DD} = 0.3 V_{DD} \ (1.5\text{ V})$</td><td>Immunity against positive spikes</td></tr>
<tr><td><strong>Low Noise Margin ($NM_L$)</strong></td><td>$V_{IL} - V_{OL} = 0.8 - 0.4 = 0.4\text{ V}$</td><td>$0.3 V_{DD} - 0.1 = 0.3 V_{DD} \ (1.5\text{ V})$</td><td>Immunity against ground bounce</td></tr>
<tr><td><strong>Propagation Delay ($t_{pd}$)</strong></td><td>$10\text{ ns}$</td><td>$8\text{ ns}$ (Advanced CMOS: $< 0.1\text{ ns}$)</td><td>Maximum operational clock speed</td></tr>
<tr><td><strong>Fan-Out</strong></td><td>$10$ standard loads</td><td>$> 50$ (limited only by capacitive delay)</td><td>Number of parallel gate inputs driven</td></tr>
</tbody>
</table>
</div>"""
        }
    ],
    "problems": [
        {
            "id": "dig-p-2-1",
            "title": "Algebraic Reduction and Proof of Boolean Absorption and Consensus",
            "statement": "Using only Huntington's postulates and fundamental Boolean theorems: (a) Prove algebraically that $A + A B = A$ (Absorption law). (b) Simplify the multi-variable expression $F(A, B, C) = A B + \bar{A} C + B C$ to its irreducible two-product form using the Consensus theorem. (c) Determine the complement of the function $G(W, X, Y, Z) = W X + \bar{Y}(Z + \bar{W})$ using De Morgan's laws.",
            "steps": [
                {
                    "stepName": "Step 1: Prove Absorption Law A + AB = A",
                    "math": r"A + A B = A \cdot 1 + A \cdot B = A \cdot (1 + B) = A \cdot (1) = A",
                    "explanation": "Apply identity (A = A*1), distributive law, null element (1 + B = 1), and identity element."
                },
                {
                    "stepName": "Step 2: Simplify Using the Consensus Theorem",
                    "math": r"F = A B + \bar{A} C + B C = A B + \bar{A} C + B C (A + \bar{A}) = A B + \bar{A} C + A B C + \bar{A} B C = A B (1 + C) + \bar{A} C (1 + B) = A B(1) + \bar{A} C(1) = A B + \bar{A} C",
                    "explanation": "Expand consensus term BC with (A + A_bar) = 1, absorb ABC into AB, and absorb A_bar*BC into A_bar*C."
                },
                {
                    "stepName": "Step 3: Determine the Complement of G via De Morgan's Law",
                    "math": r"\bar{G} = \overline{W X + \bar{Y}(Z + \bar{W})} = \overline{W X} \cdot \overline{\bar{Y}(Z + \bar{W})} = (\bar{W} + \bar{X}) \cdot (Y + \overline{Z + \bar{W}}) = (\bar{W} + \bar{X}) \cdot (Y + \bar{Z} \cdot W)",
                    "explanation": "Apply De Morgan's laws step-by-step: invert sums to products, invert products to sums."
                }
            ],
            "answer": "A + AB = A \\quad (\\text{Proved}); \\quad F = A B + \\bar{A} C; \\quad \\bar{G} = (\\bar{W} + \\bar{X})(Y + W \\bar{Z})"
        },
        {
            "id": "dig-p-2-2",
            "title": "Universal NAND Implementation of an Exclusive-OR (XOR) Function",
            "statement": "Given the Exclusive-OR logic expression $Y = A \oplus B = A \bar{B} + \bar{A} B$: (a) Derive an algebraic transformation expressing $Y$ strictly in terms of NAND operations with only 4 two-input NAND gates. (b) Draw the gate connection equations and verify with a truth table for all four input combinations $(0,0), (0,1), (1,0), (1,1)$.",
            "steps": [
                {
                    "stepName": "Step 1: Algebraic Transformation for 4-NAND Synthesis",
                    "math": r"Y = A \bar{B} + \bar{A} B = A(\bar{A} + \bar{B}) + B(\bar{A} + \bar{B}) = A \overline{A B} + B \overline{A B}",
                    "explanation": "Add null terms A*A_bar = 0 and B*B_bar = 0, then factor out (A_bar + B_bar) = (AB)_bar."
                },
                {
                    "stepName": "Step 2: Apply Double Negation",
                    "math": r"Y = \overline{\overline{A \overline{A B} + B \overline{A B}}} = \overline{\overline{A \cdot \overline{A B}} \cdot \overline{B \cdot \overline{A B}}}",
                    "explanation": "Apply De Morgan's law to convert the outer sum into an inverted product (NAND)."
                },
                {
                    "stepName": "Step 3: Define the 4-Gate Hardware Topology",
                    "math": r"G_1 = \overline{A B}, \quad G_2 = \overline{A \cdot G_1}, \quad G_3 = \overline{B \cdot G_1}, \quad Y = \overline{G_2 \cdot G_3}",
                    "explanation": "Gate 1 computes (AB)'. Gate 2 computes (A * G1)'. Gate 3 computes (B * G1)'. Gate 4 computes (G2 * G3)'."
                },
                {
                    "stepName": "Step 4: Verify Truth Table for (A=1, B=1)",
                    "math": r"G_1 = \overline{1 \cdot 1} = 0, \quad G_2 = \overline{1 \cdot 0} = 1, \quad G_3 = \overline{1 \cdot 0} = 1, \quad Y = \overline{1 \cdot 1} = 0 \quad (\text{Correct!})",
                    "explanation": "For A=1, B=1: output is 0. For (0,1): G1=1, G2=1, G3=0 => Y=1. For (1,0): G1=1, G2=0, G3=1 => Y=1. Exactly matches XOR."
                }
            ],
            "answer": "Y = \\overline{ \\overline{A \\cdot \\overline{AB}} \\cdot \\overline{B \\cdot \\overline{AB}} } \\quad (\\text{Exactly 4 two-input NAND gates})"
        },
        {
            "id": "dig-p-2-3",
            "title": "Noise Margin and Fan-Out Calculation for TTL and CMOS Gate Interfacing",
            "statement": "A standard 74-series TTL gate has the following guaranteed datasheet electrical parameters: $V_{OH} = 2.4\\text{ V}$, $V_{OL} = 0.4\\text{ V}$, $V_{IH} = 2.0\\text{ V}$, $V_{IL} = 0.8\\text{ V}$, $I_{OH} = -400\\text{ \\mu A}$, $I_{OL} = 16\\text{ mA}$, $I_{IH} = 40\\text{ \\mu A}$, and $I_{IL} = -1.6\\text{ mA}$. (a) Calculate the High and Low noise margins ($NM_H, NM_L$) of this TTL gate. (b) Calculate the maximum DC fan-out of the TTL driver. (c) A designer attempts to drive a standard CMOS gate ($V_{IH} = 3.5\\text{ V}$) directly from this TTL gate. Determine if direct driving is reliable and specify the required pull-up resistor solution.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate High and Low Noise Margins",
                    "math": r"NM_H = V_{OH} - V_{IH} = 2.4\text{ V} - 2.0\text{ V} = 0.4\text{ V}, \quad NM_L = V_{IL} - V_{OL} = 0.8\text{ V} - 0.4\text{ V} = 0.4\text{ V}",
                    "explanation": "Evaluate noise margins in Volts."
                },
                {
                    "stepName": "Step 2: Calculate High-State and Low-State Fan-Out",
                    "math": r"\text{Fan-Out}_{\text{High}} = \frac{|I_{OH}|}{I_{IH}} = \frac{400\text{ \mu A}}{40\text{ \mu A}} = 10, \quad \text{Fan-Out}_{\text{Low}} = \frac{I_{OL}}{|I_{IL}|} = \frac{16\text{ mA}}{1.6\text{ mA}} = 10",
                    "explanation": "Both states yield Fan-out = 10 standard 74-series TTL loads."
                },
                {
                    "stepName": "Step 3: Analyze TTL-to-CMOS Interfacing Hazard",
                    "math": r"V_{OH,\text{TTL}} = 2.4\text{ V} < V_{IH,\text{CMOS}} = 3.5\text{ V} \implies \text{Severe Incompatibility!}",
                    "explanation": "The maximum guaranteed HIGH output of TTL (2.4 V) falls far below the minimum required HIGH input of 5V CMOS (3.5 V = 0.7 V_DD), stranding the CMOS input in the forbidden linear region."
                },
                {
                    "stepName": "Step 4: Design External Pull-Up Resistor",
                    "math": r"R_{\text{pull-up}} \approx \frac{V_{CC} - V_{OH}}{I_{\text{leak}}} \approx \frac{5.0\text{ V} - 4.5\text{ V}}{100\text{ \mu A}} \approx 2.2 - 4.7\text{ k}\Omega",
                    "explanation": "Connecting a 2.2k to 4.7k pull-up resistor from the TTL output to +5V pulls V_OH all the way to 5.0 V, guaranteeing reliable switching."
                }
            ],
            "answer": "NM_H = 0.4\\text{ V}, \\ NM_L = 0.4\\text{ V}; \\quad \\text{Fan-Out} = 10; \\quad \\text{Direct TTL-to-CMOS unreliable } (2.4\\text{V} < 3.5\\text{V}) \\implies \\text{Requires } 2.2\\text{ k}\\Omega \\text{ pull-up resistor}"
        }
    ]
}

with open("dig_u1.json", "w", encoding="utf-8") as f:
    json.dump(u1, f, indent=2)
print("dig_u1.json created successfully!")

with open("dig_u2.json", "w", encoding="utf-8") as f:
    json.dump(u2, f, indent=2)
print("dig_u2.json created successfully!")
