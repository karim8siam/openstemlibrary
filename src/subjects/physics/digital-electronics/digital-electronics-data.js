window.COURSE_DATA = {
  "courseId": "digital-electronics",
  "courseTitle": "Digital Electronics: Combinational & Sequential Systems, Data Converters, Memory & VLSI Fabrication",
  "courseDescription": "A comprehensive, university-grade digital textbook covering number systems, weighted codes, Hamming error correction, Boolean algebra, logic gates, TTL and CMOS semiconductor logic families, Karnaugh map minimization, Quine-McCluskey tabulation, arithmetic circuits, latches, edge-triggered flip-flops, 555 timer multivibrators, synchronous and ripple counters, shift registers, MSI logic, DAC and ADC data conversion systems, semiconductor memory architectures (SRAM, DRAM, ROM, Flash), and silicon integrated circuit VLSI microfabrication with 16 interactive 60 FPS simulations.",
  "units": [
    {
      "unitNumber": 1,
      "unitId": "unit1-number-systems-codes",
      "title": "Number Systems, Weighted Codes & Error-Correction Codes",
      "description": "Fundamental arithmetic and representations in digital computers: positional radix systems (binary, octal, decimal, hexadecimal) and fractional base conversions; weighted binary codes (8421 BCD, 2421, 84-2-1), self-complementing codes, Excess-3, and unit-distance reflected Gray codes; alphanumeric standards (7-bit and 8-bit ASCII) and parity generation; Richard Hamming's single error-correcting, double error-detecting (SEC-DED) block code syndrome analysis; and hardware code converter circuit architectures.",
      "sections": [
        {
          "id": "dig-1-1",
          "title": "Positional Number Systems: Radix Conversions & Fractional Arithmetic",
          "simulation": "dig-radix-converter-sim",
          "content": "<h4>1. General Radix Positional Number Representation</h4>\n<p>In digital electronics, numbers are represented in a positional numeral system characterized by a <strong>base or radix ($r$)</strong>. Any real number $N$ possessing an integer part of $n$ digits and a fractional part of $m$ digits is expanded mathematically as a polynomial power series:</p>\n<div class=\"math-display\">\n$$(N)_r = \\sum_{i=-m}^{n-1} d_i \\cdot r^i = d_{n-1} r^{n-1} + \\dots + d_1 r^1 + d_0 r^0 + d_{-1} r^{-1} + \\dots + d_{-m} r^{-m}$$\n</div>\n<p>where $d_i \\in \\{0, 1, \\dots, r - 1\\}$ represents the digit coefficient at weight $r^i$, and the period separating $d_0$ and $d_{-1}$ is the <strong>radix point</strong>. The four primary radices utilized in digital computation are:</p>\n<ul>\n<li><strong>Binary ($r = 2$):</strong> Digits (bits) $d_i \\in \\{0, 1\\}$. Direct physical mapping to transistor cut-off and saturation states.</li>\n<li><strong>Octal ($r = 8 = 2^3$):</strong> Digits $d_i \\in \\{0, 1, 2, 3, 4, 5, 6, 7\\}$. Exactly three binary bits map to one octal digit.</li>\n<li><strong>Decimal ($r = 10$):</strong> Digits $d_i \\in \\{0, 1, \\dots, 9\\}$. Standard human arithmetic convention.</li>\n<li><strong>Hexadecimal ($r = 16 = 2^4$):</strong> Digits $d_i \\in \\{0, 1, \\dots, 9, \\text{A}(10), \\text{B}(11), \\text{C}(12), \\text{D}(13), \\text{E}(14), \\text{F}(15)\\}$. Exactly four binary bits (one nibble) map to one hexadecimal digit. Widely used for byte addresses and machine opcode representations.</li>\n</ul>\n\n<h4>2. Base Conversion Algorithms</h4>\n<ol>\n<li><strong>Radix-$r$ to Decimal:</strong> Directly evaluate the polynomial expansion $\\sum d_i r^i$ using decimal arithmetic. For example:\n<div class=\"math-display\">\n$$(11010.11)_2 = 1\\cdot 2^4 + 1\\cdot 2^3 + 0\\cdot 2^2 + 1\\cdot 2^1 + 0\\cdot 2^0 + 1\\cdot 2^{-1} + 1\\cdot 2^{-2} = 16 + 8 + 2 + 0.5 + 0.25 = (26.75)_{10}$$\n</div></li>\n<li><strong>Decimal to Radix-$r$ (Successive Division / Multiplication):</strong>\n<ul>\n<li><strong>Integer Part:</strong> Repeatedly divide the decimal integer by radix $r$. The remainder generated at division step $k$ forms digit $d_k$, terminating when the quotient reaches zero. The first remainder is the <em>Least Significant Digit (LSD)</em>; the final remainder is the <em>Most Significant Digit (MSD)</em>.</li>\n<li><strong>Fractional Part:</strong> Repeatedly multiply the fractional remainder by radix $r$. The integer carry extracted at each step forms digit $d_{-k}$, proceeding until the product terminates or reaches the desired precision. The first extracted integer is the most significant fractional digit $d_{-1}$.</li>\n</ul></li>\n<li><strong>Binary $\\leftrightarrow$ Octal $\\leftrightarrow$ Hexadecimal Grouping:</strong> Because $8 = 2^3$ and $16 = 2^4$, conversion between binary, octal, and hexadecimal requires zero polynomial arithmetic. Simply partition the binary string into groups of 3 bits (octal) or 4 bits (hexadecimal) radiating outward from the radix point, padding with leading and trailing zeros as necessary.</li>\n</ol>"
        },
        {
          "id": "dig-1-2",
          "title": "Weighted BCD Codes, Excess-3 & Reflected Gray Code",
          "content": "<h4>1. Binary Coded Decimal (BCD) & Weighted 4-Bit Codes</h4>\n<p>To interface digital hardware with decimal displays without full binary polynomial division, decimal digits $0 - 9$ are encoded individually using 4-bit binary codewords. In a <strong>weighted code</strong>, each bit position $j$ is assigned an explicit numerical weight $w_j$, such that the decimal value is:</p>\n<div class=\"math-display\">\n$$D = \\sum_{j=0}^{3} b_j w_j \\quad (b_j \\in \\{0, 1\\})$$\n</div>\n<ul>\n<li><strong>8421 BCD (Natural BCD):</strong> The standard weights are $w_3 = 8, w_2 = 4, w_1 = 2, w_0 = 1$. The 10 decimal digits map directly to binary patterns $0000_2$ through $1001_2$. The remaining six 4-bit patterns ($1010_2$ to $1111_2$, values 10 to 15) are <strong>forbidden / invalid states</strong> that never occur in legitimate BCD words.</li>\n<li><strong>Self-Complementing Codes (2421 & Excess-3):</strong> A code is <em>self-complementing</em> if the 9's complement of any decimal digit $D$ (i.e., $9 - D$) is obtained simply by taking the 1's complement (inverting all bits $b_j \\to \\bar{b}_j$) of its codeword.\n<ul>\n<li><strong>2421 Code (Aikens Code):</strong> Weights $(2, 4, 2, 1)$ where $\\sum w_j = 9$. Digit $2$ is $0010_2$, and its 9's complement $7$ is $1101_2 = \\overline{0010}_2$.</li>\n<li><strong>Excess-3 (XS-3) Code:</strong> An unweighted self-complementing code derived by adding $3_{10} = 0011_2$ to each natural 8421 BCD digit. For digit $0$: $0011_2$; for digit $9$: $1100_2 = \\overline{0011}_2$. Excess-3 simplifies decimal subtraction in early mechanical and electronic ALUs.</li>\n</ul></li>\n<li><strong>Negative Weight Codes ($84\\text{-}2\\text{-}1$):</strong> Possesses weights $w_3 = 8, w_2 = 4, w_1 = -2, w_0 = -1$. For example, decimal $5$ is encoded as $1\\cdot 8 + 0\\cdot 4 + 1\\cdot(-2) + 1\\cdot(-1) = 8 - 3 = 5$, represented by $1011_2$.</li>\n</ul>\n\n<h4>2. The Unit-Distance Reflected Gray Code</h4>\n<p>Frank Gray (1953) developed the <strong>reflected binary Gray code</strong>, an unweighted cyclic code exhibiting the critical property of <strong>unit distance</strong>: between any two adjacent decimal numbers $k$ and $k+1$, <strong>exactly one bit changes state</strong>.</p>\n<p>In electromechanical shaft optical encoders, converting angular position using natural binary can produce disastrous transient read errors. If a shaft transitions from $7$ ($0111_2$) to $8$ ($1000_2$), all four bits must flip simultaneously. Because physical photodetectors cannot switch with infinitesimal synchronicity, intermediate false states (e.g., $1111_2 = 15$) can be latched momentarily. The Gray code eliminates this hazard entirely.</p>\n<p><strong>Binary to Gray Conversion Algorithm:</strong> Given binary word $B = b_n b_{n-1} \\dots b_0$ and Gray codeword $G = g_n g_{n-1} \\dots g_0$:</p>\n<div class=\"math-display\">\n$$g_n = b_n, \\quad g_i = b_{i+1} \\oplus b_i \\quad (i = 0, 1, \\dots, n-1)$$\n</div>\n<p><strong>Gray to Binary Conversion Algorithm:</strong></p>\n<div class=\"math-display\">\n$$b_n = g_n, \\quad b_i = b_{i+1} \\oplus g_i \\quad (i = 0, 1, \\dots, n-1)$$\n</div>"
        },
        {
          "id": "dig-1-3",
          "title": "Alphanumeric Representation: ASCII Standard & Parity Checking",
          "content": "<h4>1. The ASCII Alphanumeric Encoding Standard</h4>\n<p>Digital computer systems process non-numerical information (text characters, punctuation, control commands) through standardized alphanumeric binary lookup codes. The <strong>American Standard Code for Information Interchange (ASCII)</strong> is a 7-bit encoding scheme capable of defining $2^7 = 128$ distinct characters:</p>\n<ul>\n<li><strong>32 Control Characters ($00_{16} - 1\\text{F}_{16}$):</strong> Non-printable device instructions (NUL: $00_{16}$, SOH: $01_{16}$, STX: $02_{16}$, ACK: $06_{16}$, BEL: $07_{16}$, BS: $08_{16}$, LF: $0\\text{A}_{16}$, CR: $0\\text{D}_{16}$, ESC: $1\\text{B}_{16}$).</li>\n<li><strong>96 Printable Characters ($20_{16} - 7\\text{E}_{16}$):</strong> Comprising space ($20_{16}$), decimal digits '0'-'9' ($30_{16} - 39_{16}$), uppercase letters 'A'-'Z' ($41_{16} - 5\\text{A}_{16}$), lowercase letters 'a'-'z' ($61_{16} - 7\\text{A}_{16}$), and mathematical/punctuation symbols. Note that toggling bit 5 ($20_{16}$) converts between uppercase and lowercase letters (e.g., 'A' is $01000001_2$, 'a' is $01100001_2$).</li>\n<li><strong>Extended 8-Bit ASCII ($00_{16} - \\text{FF}_{16}$):</strong> Adds 128 characters ($80_{16} - \\text{FF}_{16}$) for accented European letters, box-drawing graphics, and Greek scientific symbols.</li>\n</ul>\n\n<h4>2. Parity Bit Generation & Single-Bit Error Detection</h4>\n<p>During data transmission across communication channels or memory buses, electrical noise, thermal fluctuations, or cosmic radiation can flip a binary bit ($0 \\to 1$ or $1 \\to 0$). The simplest hardware mechanism for error detection is the appendance of a <strong>parity bit ($P$)</strong>:</p>\n<ul>\n<li><strong>Even Parity:</strong> The parity bit $P$ is chosen so that the total count of 1s in the transmitted codeword (data bits plus parity bit) is strictly <strong>even</strong>. For an $n$-bit data vector $D = (d_{n-1}, \\dots, d_0)$, the even parity bit is synthesized via cascaded XOR gates:\n<div class=\"math-display\">\n$$P_{\\text{even}} = d_{n-1} \\oplus d_{n-2} \\oplus \\dots \\oplus d_1 \\oplus d_0$$\n</div></li>\n<li><strong>Odd Parity:</strong> The parity bit $P$ is chosen so that the total count of 1s is strictly <strong>odd</strong>:\n<div class=\"math-display\">\n$$P_{\\text{odd}} = \\overline{d_{n-1} \\oplus d_{n-2} \\oplus \\dots \\oplus d_0} = \\overline{P_{\\text{even}}}$$\n</div></li>\n</ul>\n<p>At the receiver, an identical XOR parity checker computes the parity of the received packet. If a single bit flips, the parity check fails, triggering an error interrupt. However, single-bit parity cannot detect <em>double-bit errors</em> (which restore parity count) and provides zero information regarding which specific bit flipped, rendering error correction impossible.</p>"
        },
        {
          "id": "dig-1-4",
          "title": "Hamming Error-Correcting Code: SEC-DED Architecture",
          "simulation": "dig-hamming-code-sim",
          "content": "<h4>1. Richard Hamming's Geometric Code Distance Theory (1950)</h4>\n<p>To enable automated in-flight error correction in telecommunications and memory ECC (Error-Correcting Code), Richard Hamming introduced the concept of <strong>Hamming Distance ($d_{\\text{min}}$)</strong>, defined as the minimum number of bit positions in which any two valid codewords differ.</p>\n<p>For a code to detect up to $t$ simultaneous bit errors and correct up to $c$ bit errors, the minimum Hamming distance must satisfy:</p>\n<div class=\"math-display\">\n$$d_{\\text{min}} \\ge 2c + t + 1 \\quad (c \\le t)$$\n</div>\n<ul>\n<li>To <strong>detect</strong> $t = 1$ single error: $d_{\\text{min}} \\ge 1 + 1 = 2$ (simple parity bit).</li>\n<li>To <strong>correct</strong> $c = 1$ single error: $d_{\\text{min}} \\ge 2(1) + 1 = 3$ (standard Hamming code).</li>\n<li>To <strong>correct single errors and detect double errors (SEC-DED)</strong>: $d_{\\text{min}} \\ge 2(1) + 1 + 1 = 4$ (Hamming code with overall parity bit).</li>\n</ul>\n\n<h4>2. Construction of the Hamming (7,4) Single-Error-Correcting Code</h4>\n<p>Consider transmitting $m = 4$ data bits ($D_7, D_6, D_5, D_3$). To isolate the location of any single-bit error among the $n = m + k$ bits transmitted, or verify error-free transmission, the $k$ parity check bits must represent at least $n + 1$ distinct states:</p>\n<div class=\"math-display\">\n$$2^k \\ge m + k + 1 \\implies 2^k \\ge n + 1$$\n</div>\n<p>For $m = 4$, setting $k = 3$ satisfies $2^3 = 8 \\ge 4 + 3 + 1 = 8$. Thus, $n = 7$ total bits are transmitted: 4 data bits and 3 parity bits.</p>\n<p><strong>Parity Bit Placement:</strong> Parity bits $P_1, P_2, P_4$ are assigned to bit positions that are exact powers of 2 ($1, 2, 4$). The remaining positions ($3, 5, 6, 7$) hold the data bits:</p>\n<div class=\"table-responsive\">\n<table class=\"table table-bordered\">\n<thead>\n<tr><th>Bit Position</th><th>7</th><th>6</th><th>5</th><th>4</th><th>3</th><th>2</th><th>1</th></tr>\n</thead>\n<tbody>\n<tr><td><strong>Binary Position Index</strong></td><td>$111_2$</td><td>$110_2$</td><td>$101_2$</td><td>$100_2$</td><td>$011_2$</td><td>$010_2$</td><td>$001_2$</td></tr>\n<tr><td><strong>Bit Assignment</strong></td><td>$D_7$</td><td>$D_6$</td><td>$D_5$</td><td>$P_4$</td><td>$D_3$</td><td>$P_2$</td><td>$P_1$</td></tr>\n</tbody>\n</table>\n</div>\n<p>Each parity bit enforces even parity over all bit positions whose binary index contains a 1 in that parity bit's respective binary position:</p>\n<div class=\"math-display\">\n$$P_1 = D_3 \\oplus D_5 \\oplus D_7 \\quad (\\text{Positions } 1, 3, 5, 7 \\text{ have bit 0 = 1})$$\n</div>\n<div class=\"math-display\">\n$$P_2 = D_3 \\oplus D_6 \\oplus D_7 \\quad (\\text{Positions } 2, 3, 6, 7 \\text{ have bit 1 = 1})$$\n</div>\n<div class=\"math-display\">\n$$P_4 = D_5 \\oplus D_6 \\oplus D_7 \\quad (\\text{Positions } 4, 5, 6, 7 \\text{ have bit 2 = 1})$$\n</div>\n\n<h4>3. Syndrome Decoding and Hardware Error Correction</h4>\n<p>At the receiver, the 7 received bits ($r_7, r_6, r_5, r_4, r_3, r_2, r_1$) are processed by three parity-check XOR trees to calculate the 3-bit <strong>Syndrome Vector $S = (S_4 S_2 S_1)$</strong>:</p>\n<div class=\"math-display\">\n$$S_1 = r_1 \\oplus r_3 \\oplus r_5 \\oplus r_7, \\quad S_2 = r_2 \\oplus r_3 \\oplus r_6 \\oplus r_7, \\quad S_4 = r_4 \\oplus r_5 \\oplus r_6 \\oplus r_7$$\n</div>\n<ul>\n<li>If $S = 000_2$: No error occurred; data is valid.</li>\n<li>If $S = S_4 S_2 S_1 \\neq 0$: The binary integer value of $S$ points <strong>directly to the exact erroneous bit position</strong> ($1$ through $7$). The hardware simply inverts that specific bit ($r_S \\leftarrow \\overline{r_S}$) using an XOR gate driven by a 3-to-8 decoder, achieving automated instantaneous hardware error correction.</li>\n</ul>"
        },
        {
          "id": "dig-1-5",
          "title": "Hardware Code Converters: BCD, Gray & Excess-3 Logic",
          "content": "<h4>1. Combinational Code Conversion Architecture</h4>\n<p>A digital code converter is an $n$-input, $m$-output combinational logic circuit that accepts input words represented in code $\\mathcal{A}$ and produces equivalent codewords in code $\\mathcal{B}$. The synthesis procedure follows systematic Boolean optimization:</p>\n<ol>\n<li>Construct a comprehensive truth table mapping each valid input codeword to its desired output codeword.</li>\n<li>Treat unused or invalid input combinations as <strong>Don't Care states ($\\times$)</strong> to maximize logic gate reduction.</li>\n<li>Derive minimized Sum-of-Products (SOP) expressions for each output bit using Karnaugh maps or Quine-McCluskey tabulation.</li>\n</ol>\n\n<h4>2. Binary-to-Gray and Gray-to-Binary Hardware Circuits</h4>\n<p>From the conversion equations $g_i = b_{i+1} \\oplus b_i$, a 4-bit Binary-to-Gray converter requires only three two-input XOR gates:</p>\n<div class=\"math-display\">\n$$g_3 = b_3, \\quad g_2 = b_3 \\oplus b_2, \\quad g_1 = b_2 \\oplus b_1, \\quad g_0 = b_1 \\oplus b_0$$\n</div>\n<p>Similarly, the Gray-to-Binary converter $b_i = b_{i+1} \\oplus g_i$ utilizes three XOR gates in a ripple-feedback cascade:</p>\n<div class=\"math-display\">\n$$b_3 = g_3, \\quad b_2 = g_3 \\oplus g_2, \\quad b_1 = b_2 \\oplus g_1, \\quad b_0 = b_1 \\oplus g_0$$\n</div>\n\n<h4>3. BCD-to-Excess-3 Hardware Synthesis</h4>\n<p>To convert an 8421 BCD digit $(B_3, B_2, B_1, B_0)$ to Excess-3 $(E_3, E_2, E_1, E_0)$, the circuit adds $0011_2$. For input minterms $m_{10}$ through $m_{15}$, the outputs are defined as Don't Cares ($\\times$). Minimizing via 4-variable K-maps yields:</p>\n<div class=\"math-display\">\n$$E_0 = \\overline{B_0}$$\n</div>\n<div class=\"math-display\">\n$$E_1 = B_1 \\oplus B_0 = B_1 \\overline{B_0} + \\overline{B_1} B_0$$\n</div>\n<div class=\"math-display\">\n$$E_2 = B_2 \\oplus (B_1 + B_0) = \\overline{B_2}(B_1 + B_0) + B_2 \\overline{B_1}\\,\\overline{B_0}$$\n</div>\n<div class=\"math-display\">\n$$E_3 = B_3 + B_2(B_1 + B_0) = B_3 + B_2 B_1 + B_2 B_0$$\n</div>\n<p>This compact logic network requires only four standard logic gates, illustrating the power of exploiting Don't Care conditions.</p>"
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
              "math": "109 / 2 = 54 \\text{ R } 1 \\ (d_0), \\quad 54 / 2 = 27 \\text{ R } 0, \\quad 27 / 2 = 13 \\text{ R } 1, \\quad 13 / 2 = 6 \\text{ R } 1, \\quad 6 / 2 = 3 \\text{ R } 0, \\quad 3 / 2 = 1 \\text{ R } 1, \\quad 1 / 2 = 0 \\text{ R } 1 \\ (d_6)",
              "explanation": "Reading remainders from bottom to top yields (109)_10 = (1101101)_2."
            },
            {
              "stepName": "Step 2: Successive Multiplication of Fractional Part (0.6875)",
              "math": "0.6875 \\times 2 = 1.375 \\ (\\text{carry } 1), \\quad 0.375 \\times 2 = 0.75 \\ (\\text{carry } 0), \\quad 0.75 \\times 2 = 1.50 \\ (\\text{carry } 1), \\quad 0.50 \\times 2 = 1.00 \\ (\\text{carry } 1)",
              "explanation": "Reading integer carries top to bottom yields (0.6875)_10 = (0.1011)_2. Combining: (109.6875)_10 = (1101101.1011)_2."
            },
            {
              "stepName": "Step 3: Direct Grouping to Octal (Base 8)",
              "math": "(001 \\ 101 \\ 101 \\ . \\ 101 \\ 100)_2 = (1 \\ 5 \\ 5 \\ . \\ 5 \\ 4)_8 = (155.54)_8",
              "explanation": "Pad left with zeros to 9 integer bits and right with zeros to 6 fractional bits; evaluate triads: 001=1, 101=5, 101=5, 101=5, 100=4."
            },
            {
              "stepName": "Step 4: Direct Grouping to Hexadecimal (Base 16)",
              "math": "(0110 \\ 1101 \\ . \\ 1011)_2 = (6 \\ \\text{D} \\ . \\ \\text{B})_{16} = (6\\text{D.B})_{16}",
              "explanation": "Pad left to 8 integer bits; evaluate tetrads: 0110 = 6, 1101 = 13 = D, 1011 = 11 = B."
            },
            {
              "stepName": "Step 5: Verification of Hexadecimal Representation",
              "math": "6 \\times 16^1 + 13 \\times 16^0 + 11 \\times 16^{-1} = 96 + 13 + \\frac{11}{16} = 109 + 0.6875 = 109.6875_{10}",
              "explanation": "Exact decimal match confirms 100% precision."
            }
          ],
          "answer": "(109.6875)_{10} = (1101101.1011)_2 = (155.54)_8 = (6\\text{D.B})_{16}"
        },
        {
          "id": "dig-p-1-2",
          "title": "Hamming (7,4) Code Encoding, Transmission Error and Syndrome Correction",
          "statement": "A 4-bit data word $D = 1011_2$ ($D_7 = 1, D_6 = 0, D_5 = 1, D_3 = 1$) is to be transmitted using an even-parity Hamming (7,4) code. (a) Determine the parity bits $P_1, P_2, P_4$ and write the complete 7-bit transmitted codeword. (b) During transmission, an electrical noise burst flips bit 5 ($r_5: 1 \\to 0$). Calculate the syndrome vector $S = (S_4 S_2 S_1)$ at the receiver. (c) Show how the syndrome vector pinpoints the error and state the corrected word.",
          "steps": [
            {
              "stepName": "Step 1: Calculate Parity Check Bits",
              "math": "P_1 = D_3 \\oplus D_5 \\oplus D_7 = 1 \\oplus 1 \\oplus 1 = 1, \\quad P_2 = D_3 \\oplus D_6 \\oplus D_7 = 1 \\oplus 0 \\oplus 1 = 0, \\quad P_4 = D_5 \\oplus D_6 \\oplus D_7 = 1 \\oplus 0 \\oplus 1 = 0",
              "explanation": "Evaluate even parity check equations for positions 1, 2, 4."
            },
            {
              "stepName": "Step 2: Construct the Transmitted 7-bit Codeword",
              "math": "C = (D_7 D_6 D_5 P_4 D_3 P_2 P_1) = (1 \\ 0 \\ 1 \\ 0 \\ 1 \\ 0 \\ 1)_2",
              "explanation": "The transmitted codeword is 1010101_2."
            },
            {
              "stepName": "Step 3: Evaluate Received Word with Error at Bit 5",
              "math": "\\text{Bit 5 flips: } D_5 = 1 \\to 0. \\implies R = (r_7 r_6 r_5 r_4 r_3 r_2 r_1) = (1 \\ 0 \\ 0 \\ 0 \\ 1 \\ 0 \\ 1)_2",
              "explanation": "Bit position 5 now contains 0 instead of 1."
            },
            {
              "stepName": "Step 4: Compute Receiver Syndrome Vector",
              "math": "S_1 = r_1 \\oplus r_3 \\oplus r_5 \\oplus r_7 = 1 \\oplus 1 \\oplus 0 \\oplus 1 = 1, \\quad S_2 = r_2 \\oplus r_3 \\oplus r_6 \\oplus r_7 = 0 \\oplus 1 \\oplus 0 \\oplus 1 = 0, \\quad S_4 = r_4 \\oplus r_5 \\oplus r_6 \\oplus r_7 = 0 \\oplus 0 \\oplus 0 \\oplus 1 = 1",
              "explanation": "Compute syndrome bits S1, S2, S4."
            },
            {
              "stepName": "Step 5: Identify Error Location and Invert",
              "math": "S = (S_4 S_2 S_1) = (1 \\ 0 \\ 1)_2 = 5_{10}. \\implies \\text{Error is at Bit Position 5!}",
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
              "math": "7_{10} = 0111_2, \\quad 8_{10} = 1000_2, \\quad 9_{10} = 1001_2",
              "explanation": "Write 4-bit natural binary representations."
            },
            {
              "stepName": "Step 2: Generate Reflected Gray Codewords",
              "math": "G(7) = 0111 \\oplus 0011 = 0100_2, \\quad G(8) = 1000 \\oplus 0100 = 1100_2, \\quad G(9) = 1001 \\oplus 0100 = 1101_2",
              "explanation": "Compute Gray code for each sector."
            },
            {
              "stepName": "Step 3: Compare Transition Bit Flips (Sector 7 to 8)",
              "math": "\\text{Binary: } 0111_2 \\to 1000_2 \\implies \\text{Hamming distance } d = 4 \\ (\\text{All 4 bits flip simultaneously!})",
              "explanation": "Natural binary undergoes 4 simultaneous bit transitions, creating severe asynchronous timing hazards."
            },
            {
              "stepName": "Step 4: Evaluate Gray Transition Distance",
              "math": "\\text{Gray: } 0100_2 \\to 1100_2 \\implies \\text{Hamming distance } d = 1 \\ (\\text{Only MSB flips from 0 to 1})",
              "explanation": "Gray code switches exactly 1 bit, completely eliminating encoder transition glitches."
            },
            {
              "stepName": "Step 5: Convert Binary 1101 to Gray",
              "math": "g_3 = b_3 = 1, \\quad g_2 = b_3 \\oplus b_2 = 1 \\oplus 1 = 0, \\quad g_1 = b_2 \\oplus b_1 = 1 \\oplus 0 = 1, \\quad g_0 = b_1 \\oplus b_0 = 0 \\oplus 1 = 1 \\implies G = (1011)_2",
              "explanation": "Apply conversion equations bit-by-bit."
            }
          ],
          "answer": "G(7)=0100_2, \\ G(8)=1100_2 \\ (d=1 \\text{ vs } d=4 \\text{ in binary}); \\quad G(1101_2) = 1011_2"
        }
      ]
    },
    {
      "unitNumber": 2,
      "unitId": "unit2-boolean-algebra-logic-gates",
      "title": "Boolean Algebra, Logic Gates & Semiconductor Logic Families",
      "description": "Mathematical foundations and solid-state physical implementation of digital logic: George Boole's algebraic axioms and Huntington's postulates; duality principle; De Morgan's laws and algebraic multi-variable reduction; canonical digital logic gates (AND, OR, NOT, NAND, NOR, XOR, XNOR); functional completeness and universal gate synthesis (NAND-only and NOR-only networks); bipolar Transistor-Transistor Logic (TTL Totem-Pole) and complementary MOS (CMOS) inverter circuit electronics; propagation delay, fan-out, power dissipation, and high/low noise margins.",
      "sections": [
        {
          "id": "dig-2-1",
          "title": "Huntington's Postulates, Algebraic Axioms & The Duality Principle",
          "content": "<h4>1. Formal Mathematical Axioms of Boolean Algebra</h4>\n<p>In 1904, Edward V. Huntington formalized George Boole's algebraic logic as a deductive mathematical system defined on a set of elements $B$ with two binary operators: logical OR ($+$) and logical AND ($\\cdot$), satisfying six fundamental postulates:</p>\n<ol>\n<li><strong>Closure:</strong> For every $x, y \\in B$:\n<div class=\"math-display\">\n$$x + y \\in B \\quad \\text{and} \\quad x \\cdot y \\in B$$\n</div></li>\n<li><strong>Identity Elements:</strong> There exist unique elements $0, 1 \\in B$ such that for every $x \\in B$:\n<div class=\"math-display\">\n$$x + 0 = x \\quad \\text{and} \\quad x \\cdot 1 = x$$\n</div></li>\n<li><strong>Commutative Laws:</strong> For every $x, y \\in B$:\n<div class=\"math-display\">\n$$x + y = y + x \\quad \\text{and} \\quad x \\cdot y = y \\cdot x$$\n</div></li>\n<li><strong>Distributive Laws:</strong> Each operator distributes over the other:\n<div class=\"math-display\">\n$$x \\cdot (y + z) = (x \\cdot y) + (x \\cdot z)$$\n</div>\n<div class=\"math-display\">\n$$x + (y \\cdot z) = (x + y) \\cdot (x + z) \\quad (\\text{Crucial rule with no ordinary algebra analog!})$$\n</div></li>\n<li><strong>Complement:</strong> For every $x \\in B$, there exists a unique complement $\\bar{x} \\in B$ such that:\n<div class=\"math-display\">\n$$x + \\bar{x} = 1 \\quad \\text{and} \\quad x \\cdot \\bar{x} = 0$$\n</div></li>\n<li><strong>Distinct Elements:</strong> There exist at least two elements $x, y \\in B$ such that $x \\ne y$.</li>\n</ol>\n\n<h4>2. Fundamental Theorems of Boolean Algebra</h4>\n<p>From Huntington's postulates, the standard operational theorems are deduced:</p>\n<ul>\n<li><strong>Idempotence:</strong> $x + x = x$ and $x \\cdot x = x$.</li>\n<li><strong>Null Elements (Dominance):</strong> $x + 1 = 1$ and $x \\cdot 0 = 0$.</li>\n<li><strong>Involution (Double Negation):</strong> $\\overline{\\bar{x}} = x$.</li>\n<li><strong>Absorption Laws:</strong>\n<div class=\"math-display\">\n$$x + (x \\cdot y) = x \\quad \\text{and} \\quad x \\cdot (x + y) = x$$\n</div>\n<div class=\"math-display\">\n$$x + (\\bar{x} \\cdot y) = x + y \\quad \\text{and} \\quad x \\cdot (\\bar{x} + y) = x \\cdot y$$\n</div></li>\n<li><strong>Associative Laws:</strong>\n<div class=\"math-display\">\n$$x + (y + z) = (x + y) + z \\quad \\text{and} \\quad x \\cdot (y \\cdot z) = (x \\cdot y) \\cdot z$$\n</div></li>\n</ul>\n\n<h4>3. The Principle of Duality</h4>\n<p>The <strong>Principle of Duality</strong> states: <em>Any true Boolean algebraic identity remains strictly valid if the operators $+$ and $\\cdot$ are interchanged, and the identity elements $0$ and $1$ are simultaneously interchanged.</em></p>\n<p>For example, the dual of the distributive law $x \\cdot (y + z) = (x \\cdot y) + (x \\cdot z)$ is directly obtained by swapping $\\cdot \\leftrightarrow +$:</p>\n<div class=\"math-display\">\n$$x + (y \\cdot z) = (x + y) \\cdot (x + z)$$\n</div>\n<p>Duality halves the labor of Boolean mathematical proofs: proving one theorem automatically validates its dual.</p>"
        },
        {
          "id": "dig-2-2",
          "title": "De Morgan's Theorems & Multi-Variable Function Reduction",
          "content": "<h4>1. Augustus De Morgan's Laws</h4>\n<p>Augustus De Morgan (1847) established the two most celebrated theorems in digital circuit design, defining the rigorous relationship between conjunction, disjunction, and complementation:</p>\n<div class=\"math-display\">\n$$\\overline{A + B} = \\bar{A} \\cdot \\bar{B} \\quad (\\text{The complement of a logical sum is the product of the complements})$$\n</div>\n<div class=\"math-display\">\n$$\\overline{A \\cdot B} = \\bar{A} + \\bar{B} \\quad (\\text{The complement of a logical product is the sum of the complements})$$\n</div>\n<p>In digital circuit topology, De Morgan's laws state that a NOR gate (OR followed by inversion) is functionally identical to an AND gate with inverted inputs (negative-AND), and a NAND gate is identical to a negative-OR gate:</p>\n<div class=\"math-display\">\n$$\\text{NOR}(A, B) \\equiv \\text{Negative-AND}(\\bar{A}, \\bar{B}), \\qquad \\text{NAND}(A, B) \\equiv \\text{Negative-OR}(\\bar{A}, \\bar{B})$$\n</div>\n\n<h4>2. Generalized Generalized Multi-Variable Formulation</h4>\n<p>By mathematical induction, De Morgan's laws extend to an arbitrary number of $n$ variables:</p>\n<div class=\"math-display\">\n$$\\overline{A_1 + A_2 + \\dots + A_n} = \\bar{A}_1 \\cdot \\bar{A}_2 \\dots \\bar{A}_n$$\n</div>\n<div class=\"math-display\">\n$$\\overline{A_1 \\cdot A_2 \\dots A_n} = \\bar{A}_1 + \\bar{A}_2 + \\dots + \\bar{A}_n$$\n</div>\n<p>To complement any arbitrary Boolean function $F(A, B, C, \\dots, +, \\cdot)$, one simultaneously applies De Morgan's rule across all levels: interchange all $+$ and $\\cdot$ operators, and complement every individual literal ($A \\to \\bar{A}$ and $\\bar{A} \\to A$).</p>\n\n<h4>3. The Consensus Theorem</h4>\n<p>The <strong>Consensus Theorem</strong> provides a powerful shortcut for eliminating redundant terms in multi-variable equations without tedious K-map expansion:</p>\n<div class=\"math-display\">\n$$A B + \\bar{A} C + B C = A B + \\bar{A} C$$\n</div>\n<p>where $B C$ is the <em>consensus term</em> formed from the conjunction of the two literals associated with the complemented pair $A$ and $\\bar{A}$. In its dual form:</p>\n<div class=\"math-display\">\n$$(A + B)(\\bar{A} + C)(B + C) = (A + B)(\\bar{A} + C)$$\n</div>"
        },
        {
          "id": "dig-2-3",
          "title": "Canonical Logic Gates: AND, OR, NOT, NAND, NOR, XOR & XNOR",
          "simulation": "dig-logic-gate-explorer-sim",
          "content": "<h4>1. Basic Logic Gates and Operational Truth Tables</h4>\n<p>Digital logic gates are physical electronic circuits that perform elementary Boolean switching operations on binary voltage signals ($V_{LOW} \\leftrightarrow 0$, $V_{HIGH} \\leftrightarrow 1$):</p>\n<ol>\n<li><strong>NOT Gate (Inverter):</strong> Implements single-input complementation: $Y = \\bar{A}$. If $A=0$, $Y=1$; if $A=1$, $Y=0$.</li>\n<li><strong>AND Gate:</strong> Output is HIGH if and only if all inputs are HIGH: $Y = A \\cdot B$.</li>\n<li><strong>OR Gate:</strong> Output is HIGH if at least one input is HIGH: $Y = A + B$.</li>\n<li><strong>NAND Gate:</strong> Negated AND operation: $Y = \\overline{A \\cdot B}$. Output is LOW if and only if all inputs are HIGH.</li>\n<li><strong>NOR Gate:</strong> Negated OR operation: $Y = \\overline{A + B}$. Output is HIGH if and only if all inputs are LOW.</li>\n</ol>\n\n<h4>2. Exclusive-OR (XOR) & Exclusive-NOR (XNOR) Gates</h4>\n<p>The <strong>XOR gate ($\\oplus$)</strong>, or modulo-2 adder, yields a HIGH output when the inputs are <em>different</em>:</p>\n<div class=\"math-display\">\n$$Y = A \\oplus B = A \\bar{B} + \\bar{A} B$$\n</div>\n<p>Properties of XOR:</p>\n<ul>\n<li>$A \\oplus 0 = A$, \\quad $A \\oplus 1 = \\bar{A}$ (programmable inverter).</li>\n<li>$A \\oplus A = 0$, \\quad $A \\oplus \\bar{A} = 1$.</li>\n<li>Commutative: $A \\oplus B = B \\oplus A$; Associative: $(A \\oplus B) \\oplus C = A \\oplus (B \\oplus C)$.</li>\n<li>For $n$ inputs, an XOR gate acts as an <strong>odd parity detector</strong>: output is 1 if and only if an odd number of inputs are 1.</li>\n</ul>\n<p>The <strong>XNOR gate ($\\odot$)</strong>, or equivalence detector, produces a HIGH output when the inputs are <em>identical</em>:</p>\n<div class=\"math-display\">\n$$Y = A \\odot B = \\overline{A \\oplus B} = A B + \\bar{A} \\bar{B}$$\n</div>"
        },
        {
          "id": "dig-2-4",
          "title": "Universal Gate Synthesis: NAND-Only & NOR-Only Networks",
          "content": "<h4>1. Functional Completeness in Digital Logic</h4>\n<p>A set of Boolean operators is defined as <strong>functionally complete</strong> if every arbitrary Boolean function can be expressed solely using operators from that set. The standard set $\\{\\text{AND}, \\text{OR}, \\text{NOT}\\}$ is functionally complete. However, fabricating multiple distinct gate types on an integrated circuit increases silicon area and manufacturing complexity.</p>\n<p>A <strong>Universal Gate</strong> is a single gate type capable of synthesizing all elementary logic functions (NOT, AND, OR, XOR) without requiring any other components. There exist precisely two universal logic gates in digital electronics: <strong>NAND</strong> and <strong>NOR</strong>.</p>\n\n<h4>2. NAND-Only Gate Realizations</h4>\n<ol>\n<li><strong>NOT using NAND:</strong> Tie both inputs together:\n<div class=\"math-display\">\n$$\\overline{A \\cdot A} = \\bar{A}$$\n</div></li>\n<li><strong>AND using NAND:</strong> Feed the output of a NAND gate into a NAND-inverter:\n<div class=\"math-display\">\n$$\\overline{\\overline{A \\cdot B}} = A \\cdot B \\quad (\\text{2 NAND gates})$$\n</div></li>\n<li><strong>OR using NAND:</strong> Invert each input with a NAND gate, then feed into a third NAND gate (De Morgan's law):\n<div class=\"math-display\">\n$$\\overline{\\bar{A} \\cdot \\bar{B}} = \\overline{\\bar{A}} + \\overline{\\bar{B}} = A + B \\quad (\\text{3 NAND gates})$$\n</div></li>\n<li><strong>NOR using NAND:</strong> Invert the output of the NAND-synthesized OR gate:\n<div class=\"math-display\">\n$$\\overline{A + B} \\quad (\\text{4 NAND gates})$$\n</div></li>\n<li><strong>XOR using NAND:</strong> Synthesize $A \\bar{B} + \\bar{A} B$ with minimum four 2-input NAND gates:\n<div class=\"math-display\">\n$$X = \\overline{A B}, \\quad Y = \\overline{A \\cdot X} \\cdot \\overline{B \\cdot X} = A \\oplus B \\quad (\\text{4 NAND gates})$$\n</div></li>\n</ol>\n\n<h4>3. NOR-Only Gate Realizations</h4>\n<ol>\n<li><strong>NOT using NOR:</strong> Tie both inputs together: $\\overline{A + A} = \\bar{A}$ (1 NOR gate).</li>\n<li><strong>OR using NOR:</strong> Invert the NOR output: $\\overline{\\overline{A + B}} = A + B$ (2 NOR gates).</li>\n<li><strong>AND using NOR:</strong> Invert each input, then combine in a NOR gate: $\\overline{\\bar{A} + \\bar{B}} = A \\cdot B$ (3 NOR gates).</li>\n<li><strong>NAND using NOR:</strong> Invert the output of the NOR-synthesized AND gate (4 NOR gates).</li>\n<li><strong>XOR using NOR:</strong> Synthesized with five 2-input NOR gates.</li>\n</ol>"
        },
        {
          "id": "dig-2-5",
          "title": "Semiconductor Logic Families: TTL Totem-Pole vs CMOS Inverters",
          "simulation": "dig-ttl-cmos-inverter-sim",
          "content": "<h4>1. Transistor-Transistor Logic (TTL) & The Totem-Pole Output</h4>\n<p>Standard BJT Transistor-Transistor Logic (7400 series) operates from a single $+5\\text{ V}$ power supply ($V_{CC}$). The canonical TTL NAND gate consists of three stages:</p>\n<ol>\n<li><strong>Input Stage:</strong> Multi-emitter NPN transistor $Q_1$. If any input is LOW ($0.2\\text{ V}$), $Q_1$ conducts base current to the LOW input, pulling $Q_1$'s collector voltage low and cutting off phase-splitter $Q_2$.</li>\n<li><strong>Phase-Splitter Stage:</strong> Transistor $Q_2$ generates complementary out-of-phase drive voltages at its collector and emitter.</li>\n<li><strong>Totem-Pole Output Stage:</strong> Consists of pull-up transistor $Q_4$, diode $D$, and pull-down transistor $Q_3$:\n<ul>\n<li><strong>Output LOW State ($Y = 0$):</strong> $Q_2$ and $Q_3$ are saturated. $Q_3$ pulls the output to $V_{OL} \\approx V_{CE,\\text{sat}} \\approx 0.2\\text{ V}$. Meanwhile, $Q_4$ is completely off because diode $D$ drops $0.7\\text{ V}$, ensuring base-emitter voltage $V_{BE4}$ is insufficient to turn $Q_4$ on.</li>\n<li><strong>Output HIGH State ($Y = 1$):</strong> $Q_2$ and $Q_3$ are cut off. $Q_4$ acts as an active pull-up emitter follower, charging the capacitive load rapidly to $V_{OH} = V_{CC} - V_{BE4} - V_D \\approx 5.0 - 0.7 - 0.7 \\approx 3.6\\text{ V}$.</li>\n</ul></li>\n</ol>\n<p>The totem-pole active pull-up provides low output impedance in both states, dramatically accelerating capacitive line charging compared to passive resistor pull-ups.</p>\n\n<h4>2. Complementary MOS (CMOS) Inverter</h4>\n<p>CMOS technology pairs an enhancement-mode pMOS pull-up transistor with an nMOS pull-down transistor in a symmetric, push-pull configuration:</p>\n<ul>\n<li><strong>Input LOW ($V_{\\text{in}} = 0\\text{ V}$):</strong> $V_{GS,n} = 0 < V_{tn} \\implies$ nMOS is OFF. $V_{GS,p} = -V_{DD} < V_{tp} \\implies$ pMOS is saturated/linear, pulling $V_{\\text{out}}$ to exactly $V_{DD}$ with <strong>zero static current</strong>.</li>\n<li><strong>Input HIGH ($V_{\\text{in}} = V_{DD}$):</strong> $V_{GS,n} = V_{DD} > V_{tn} \\implies$ nMOS is ON. $V_{GS,p} = 0 \\implies$ pMOS is OFF. nMOS pulls $V_{\\text{out}}$ to exactly $0\\text{ V}$ with <strong>zero static current</strong>.</li>\n<li><strong>Power Dissipation:</strong> Because one transistor is always cut off in the steady state, static power dissipation is virtually zero ($P_{\\text{static}} \\sim\\text{nW}$). Power is consumed only during switching transitions as dynamic power:\n<div class=\"math-display\">\n$$P_{\\text{dynamic}} = C_L V_{DD}^2 f$$\n</div>\nwhere $C_L$ is load capacitance and $f$ is clock switching frequency.</li>\n</ul>\n\n<h4>3. Key Logic Family Performance Metrics</h4>\n<div class=\"table-responsive\">\n<table class=\"table table-bordered\">\n<thead>\n<tr><th>Metric</th><th>TTL (Standard 74xx)</th><th>CMOS (74HCxx / Modern)</th><th>Physical Significance</th></tr>\n</thead>\n<tbody>\n<tr><td><strong>Supply Voltage ($V_{CC}/V_{DD}$)</strong></td><td>$5\\text{ V} \\pm 5\\%$</td><td>$2\\text{ V} - 6\\text{ V}$ (Core: $0.8 - 1.8\\text{ V}$)</td><td>Power rail tolerance</td></tr>\n<tr><td><strong>$V_{IH,\\text{min}} / V_{IL,\\text{max}}$</strong></td><td>$2.0\\text{ V} \\ / \\ 0.8\\text{ V}$</td><td>$0.7 V_{DD} \\ / \\ 0.3 V_{DD}$</td><td>Input threshold boundaries</td></tr>\n<tr><td><strong>$V_{OH,\\text{min}} / V_{OL,\\text{max}}$</strong></td><td>$2.4\\text{ V} \\ / \\ 0.4\\text{ V}$</td><td>$V_{DD} - 0.1\\text{ V} \\ / \\ 0.1\\text{ V}$</td><td>Output drive levels</td></tr>\n<tr><td><strong>High Noise Margin ($NM_H$)</strong></td><td>$V_{OH} - V_{IH} = 2.4 - 2.0 = 0.4\\text{ V}$</td><td>$V_{DD} - 0.7V_{DD} = 0.3 V_{DD} \\ (1.5\\text{ V})$</td><td>Immunity against positive spikes</td></tr>\n<tr><td><strong>Low Noise Margin ($NM_L$)</strong></td><td>$V_{IL} - V_{OL} = 0.8 - 0.4 = 0.4\\text{ V}$</td><td>$0.3 V_{DD} - 0.1 = 0.3 V_{DD} \\ (1.5\\text{ V})$</td><td>Immunity against ground bounce</td></tr>\n<tr><td><strong>Propagation Delay ($t_{pd}$)</strong></td><td>$10\\text{ ns}$</td><td>$8\\text{ ns}$ (Advanced CMOS: $< 0.1\\text{ ns}$)</td><td>Maximum operational clock speed</td></tr>\n<tr><td><strong>Fan-Out</strong></td><td>$10$ standard loads</td><td>$> 50$ (limited only by capacitive delay)</td><td>Number of parallel gate inputs driven</td></tr>\n</tbody>\n</table>\n</div>"
        }
      ],
      "problems": [
        {
          "id": "dig-p-2-1",
          "title": "Algebraic Reduction and Proof of Boolean Absorption and Consensus",
          "statement": "Using only Huntington's postulates and fundamental Boolean theorems: (a) Prove algebraically that $A + A B = A$ (Absorption law). (b) Simplify the multi-variable expression $F(A, B, C) = A B + \\bar{A} C + B C$ to its irreducible two-product form using the Consensus theorem. (c) Determine the complement of the function $G(W, X, Y, Z) = W X + \\bar{Y}(Z + \\bar{W})$ using De Morgan's laws.",
          "steps": [
            {
              "stepName": "Step 1: Prove Absorption Law A + AB = A",
              "math": "A + A B = A \\cdot 1 + A \\cdot B = A \\cdot (1 + B) = A \\cdot (1) = A",
              "explanation": "Apply identity (A = A*1), distributive law, null element (1 + B = 1), and identity element."
            },
            {
              "stepName": "Step 2: Simplify Using the Consensus Theorem",
              "math": "F = A B + \\bar{A} C + B C = A B + \\bar{A} C + B C (A + \\bar{A}) = A B + \\bar{A} C + A B C + \\bar{A} B C = A B (1 + C) + \\bar{A} C (1 + B) = A B(1) + \\bar{A} C(1) = A B + \\bar{A} C",
              "explanation": "Expand consensus term BC with (A + A_bar) = 1, absorb ABC into AB, and absorb A_bar*BC into A_bar*C."
            },
            {
              "stepName": "Step 3: Determine the Complement of G via De Morgan's Law",
              "math": "\\bar{G} = \\overline{W X + \\bar{Y}(Z + \\bar{W})} = \\overline{W X} \\cdot \\overline{\\bar{Y}(Z + \\bar{W})} = (\\bar{W} + \\bar{X}) \\cdot (Y + \\overline{Z + \\bar{W}}) = (\\bar{W} + \\bar{X}) \\cdot (Y + \\bar{Z} \\cdot W)",
              "explanation": "Apply De Morgan's laws step-by-step: invert sums to products, invert products to sums."
            }
          ],
          "answer": "A + AB = A \\quad (\\text{Proved}); \\quad F = A B + \\bar{A} C; \\quad \\bar{G} = (\\bar{W} + \\bar{X})(Y + W \\bar{Z})"
        },
        {
          "id": "dig-p-2-2",
          "title": "Universal NAND Implementation of an Exclusive-OR (XOR) Function",
          "statement": "Given the Exclusive-OR logic expression $Y = A \\oplus B = A \\bar{B} + \\bar{A} B$: (a) Derive an algebraic transformation expressing $Y$ strictly in terms of NAND operations with only 4 two-input NAND gates. (b) Draw the gate connection equations and verify with a truth table for all four input combinations $(0,0), (0,1), (1,0), (1,1)$.",
          "steps": [
            {
              "stepName": "Step 1: Algebraic Transformation for 4-NAND Synthesis",
              "math": "Y = A \\bar{B} + \\bar{A} B = A(\\bar{A} + \\bar{B}) + B(\\bar{A} + \\bar{B}) = A \\overline{A B} + B \\overline{A B}",
              "explanation": "Add null terms A*A_bar = 0 and B*B_bar = 0, then factor out (A_bar + B_bar) = (AB)_bar."
            },
            {
              "stepName": "Step 2: Apply Double Negation",
              "math": "Y = \\overline{\\overline{A \\overline{A B} + B \\overline{A B}}} = \\overline{\\overline{A \\cdot \\overline{A B}} \\cdot \\overline{B \\cdot \\overline{A B}}}",
              "explanation": "Apply De Morgan's law to convert the outer sum into an inverted product (NAND)."
            },
            {
              "stepName": "Step 3: Define the 4-Gate Hardware Topology",
              "math": "G_1 = \\overline{A B}, \\quad G_2 = \\overline{A \\cdot G_1}, \\quad G_3 = \\overline{B \\cdot G_1}, \\quad Y = \\overline{G_2 \\cdot G_3}",
              "explanation": "Gate 1 computes (AB)'. Gate 2 computes (A * G1)'. Gate 3 computes (B * G1)'. Gate 4 computes (G2 * G3)'."
            },
            {
              "stepName": "Step 4: Verify Truth Table for (A=1, B=1)",
              "math": "G_1 = \\overline{1 \\cdot 1} = 0, \\quad G_2 = \\overline{1 \\cdot 0} = 1, \\quad G_3 = \\overline{1 \\cdot 0} = 1, \\quad Y = \\overline{1 \\cdot 1} = 0 \\quad (\\text{Correct!})",
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
              "math": "NM_H = V_{OH} - V_{IH} = 2.4\\text{ V} - 2.0\\text{ V} = 0.4\\text{ V}, \\quad NM_L = V_{IL} - V_{OL} = 0.8\\text{ V} - 0.4\\text{ V} = 0.4\\text{ V}",
              "explanation": "Evaluate noise margins in Volts."
            },
            {
              "stepName": "Step 2: Calculate High-State and Low-State Fan-Out",
              "math": "\\text{Fan-Out}_{\\text{High}} = \\frac{|I_{OH}|}{I_{IH}} = \\frac{400\\text{ \\mu A}}{40\\text{ \\mu A}} = 10, \\quad \\text{Fan-Out}_{\\text{Low}} = \\frac{I_{OL}}{|I_{IL}|} = \\frac{16\\text{ mA}}{1.6\\text{ mA}} = 10",
              "explanation": "Both states yield Fan-out = 10 standard 74-series TTL loads."
            },
            {
              "stepName": "Step 3: Analyze TTL-to-CMOS Interfacing Hazard",
              "math": "V_{OH,\\text{TTL}} = 2.4\\text{ V} < V_{IH,\\text{CMOS}} = 3.5\\text{ V} \\implies \\text{Severe Incompatibility!}",
              "explanation": "The maximum guaranteed HIGH output of TTL (2.4 V) falls far below the minimum required HIGH input of 5V CMOS (3.5 V = 0.7 V_DD), stranding the CMOS input in the forbidden linear region."
            },
            {
              "stepName": "Step 4: Design External Pull-Up Resistor",
              "math": "R_{\\text{pull-up}} \\approx \\frac{V_{CC} - V_{OH}}{I_{\\text{leak}}} \\approx \\frac{5.0\\text{ V} - 4.5\\text{ V}}{100\\text{ \\mu A}} \\approx 2.2 - 4.7\\text{ k}\\Omega",
              "explanation": "Connecting a 2.2k to 4.7k pull-up resistor from the TTL output to +5V pulls V_OH all the way to 5.0 V, guaranteeing reliable switching."
            }
          ],
          "answer": "NM_H = 0.4\\text{ V}, \\ NM_L = 0.4\\text{ V}; \\quad \\text{Fan-Out} = 10; \\quad \\text{Direct TTL-to-CMOS unreliable } (2.4\\text{V} < 3.5\\text{V}) \\implies \\text{Requires } 2.2\\text{ k}\\Omega \\text{ pull-up resistor}"
        }
      ]
    },
    {
      "unitNumber": 3,
      "unitId": "unit3-k-maps-arithmetic-circuits",
      "title": "Combinational Optimization, K-Maps & Arithmetic Circuits",
      "description": "Exhaustive theory and practice of combinational logic minimization and arithmetic computation: minterms (m_i), maxterms (M_i), canonical Sum-of-Products (SOP) and Product-of-Sums (POS) representations; Karnaugh Map (K-Map) minimization across 2, 3, 4, and 5 variables with Gray code adjacency and Don't Care states; Quine-McCluskey tabular algorithm, prime implicants, and Petrick's method; radix and diminished radix complements (1's, 2's, 9's, 10's complement); half-adders, full-adders, parallel ripple-carry adders, carry-lookahead generators; BCD decimal adders with +6 correction logic, half/full subtractors, and array binary multipliers.",
      "sections": [
        {
          "id": "dig-3-1",
          "title": "Canonical Boolean Forms: Minterms, Maxterms, SOP & POS",
          "content": "<h4>1. Canonical Boolean Representations</h4>\n<p>Every Boolean switching function of $n$ variables $F(x_1, x_2, \\dots, x_n)$ can be expressed uniquely in two complementary canonical forms:</p>\n<ol>\n<li><strong>Minterms ($m_i$) and Canonical Sum-of-Products (SOP):</strong> A <strong>minterm</strong> is a product (AND) of all $n$ variables, with each variable appearing exactly once in either its uncomplemented or complemented form. An $n$-variable function possesses $2^n$ distinct minterms ($m_0$ through $m_{2^n-1}$). Minterm $m_i$ evaluates to <strong>1</strong> for exactly one input combination whose binary representation equals index $i$. Any function is uniquely defined as the logical sum (OR) of its 1-generating minterms:\n<div class=\"math-display\">\n$$F(A, B, C) = \\sum m(1, 4, 6, 7) = \\bar{A}\\bar{B}C + A\\bar{B}\\bar{C} + AB\\bar{C} + ABC$$\n</div></li>\n<li><strong>Maxterms ($M_i$) and Canonical Product-of-Sums (POS):</strong> A <strong>maxterm</strong> is a sum (OR) of all $n$ variables. Maxterm $M_i$ evaluates to <strong>0</strong> for exactly one input combination whose binary representation equals index $i$. By De Morgan's theorem, each maxterm is the exact complement of the corresponding minterm:\n<div class=\"math-display\">\n$$M_i = \\overline{m_i}$$\n</div>\nAny function is uniquely defined as the logical product (AND) of its 0-generating maxterms:\n<div class=\"math-display\">\n$$F(A, B, C) = \\prod M(0, 2, 3, 5) = (A + B + C)(A + \\bar{B} + C)(A + \\bar{B} + \\bar{C})(\\bar{A} + B + \\bar{C})$$\n</div></li>\n</ol>\n\n<h4>2. Conversion Between Canonical SOP and POS</h4>\n<p>Because the indices that do not belong to the minterm list $\\sum m$ must generate 0s, they form the maxterm list $\\prod M$:</p>\n<div class=\"math-display\">\n$$F = \\sum m(d_1, d_2, \\dots) \\iff F = \\prod M(\\text{remaining indices})$$\n</div>\n<p>Furthermore, the complement function $\\bar{F}$ is simply the sum of all missing minterms:</p>\n<div class=\"math-display\">\n$$\\bar{F} = \\sum m(\\text{missing from } F) = \\prod M(\\text{present in } F)$$\n</div>"
        },
        {
          "id": "dig-3-2",
          "title": "Karnaugh Map (K-Map) Minimization & Don't Care Conditions",
          "simulation": "dig-kmap-minimizer-sim",
          "content": "<h4>1. Geometric Adjacency & Gray Code Ordering in K-Maps</h4>\n<p>Maurice Karnaugh (1953) organized truth tables into a planar graphical grid termed the <strong>Karnaugh Map (K-map)</strong>. The rows and columns are arranged in <strong>reflected Gray code sequence</strong> ($00, 01, 11, 10$):</p>\n<ul>\n<li>Adjacent cells horizontally and vertically differ in <strong>exactly one literal</strong>.</li>\n<li>The edges wrap around cyclically (toroidal topology): the leftmost column is geometrically adjacent to the rightmost column, and the top row is adjacent to the bottom row.</li>\n<li>Four-corner cells ($m_0, m_2, m_8, m_{10}$ in a 4-variable map) are mutually adjacent and form a valid group of four.</li>\n</ul>\n\n<h4>2. Grouping Rules and Prime Implicant Extraction</h4>\n<p>By applying the Boolean absorption identity $x y + x \\bar{y} = x (y + \\bar{y}) = x$, grouping adjacent cells containing 1s eliminates the differing literals:</p>\n<ul>\n<li>A group of $2^1 = 2$ adjacent cells (pair) eliminates <strong>1 literal</strong>.</li>\n<li>A group of $2^2 = 4$ adjacent cells (quad) eliminates <strong>2 literals</strong>.</li>\n<li>A group of $2^3 = 8$ adjacent cells (octet) eliminates <strong>3 literals</strong>.</li>\n<li>A group of $2^k$ adjacent cells eliminates <strong>$k$ literals</strong>.</li>\n</ul>\n<p><strong>Fundamental K-Map Optimization Axioms:</strong></p>\n<ol>\n<li>Groups must be rectangular and contain a power-of-two number of cells ($1, 2, 4, 8, 16$).</li>\n<li>Every 1 must be covered by at least one group.</li>\n<li>Groups should be made as <strong>large as possible</strong> to maximize literal elimination.</li>\n<li>The total number of groups must be <strong>minimized</strong> to minimize gate count.</li>\n<li>A <strong>Prime Implicant (PI)</strong> is a group that cannot be combined with any other cells to form a larger group.</li>\n<li>An <strong>Essential Prime Implicant (EPI)</strong> is a prime implicant that covers at least one '1' that is not covered by any other prime implicant. All EPIs <em>must</em> be included in the minimal sum.</li>\n</ol>\n\n<h4>3. Incompletely Specified Functions: Don't Care States ($\\times$)</h4>\n<p>In many digital circuits (e.g., BCD decoders), certain input combinations never occur physically (e.g., binary values $10 - 15$ in 4-bit BCD). The output for these combinations is immaterial and designated as a <strong>Don't Care ($\\times$ or $d$)</strong>.</p>\n<p>In K-map reduction, a Don't Care condition $\\times$ may be treated as <strong>1</strong> if doing so allows a group to expand to a larger power-of-two size (eliminating more literals), or as <strong>0</strong> if it does not help enlarge any group. Don't Care cells are never grouped alone.</p>"
        },
        {
          "id": "dig-3-3",
          "title": "Quine-McCluskey Tabulation & Prime Implicant Charts",
          "content": "<h4>1. Limitations of K-Maps and the Need for Algorithmic Reduction</h4>\n<p>While Karnaugh maps are intuitive for 2, 3, and 4 variables, 5-variable maps require dual overlay planes, and 6-variable maps require 4 sub-cubes, becoming visually error-prone. For functions of $n \\ge 6$ variables, algorithmic computer-aided design (CAD) relies on the <strong>Quine-McCluskey (Q-M) Tabulation Method</strong>.</p>\n\n<h4>2. Step-by-Step Quine-McCluskey Algorithm</h4>\n<ol>\n<li><strong>Group by Hamming Weight:</strong> Express all minterms and don't cares in binary and partition them into groups based on the count of 1s (Hamming weight).</li>\n<li><strong>Pairwise Comparison:</strong> Compare each term in group $k$ with every term in group $k+1$. If two terms differ in exactly one bit position, combine them by replacing that bit with a dash ($-$) and check off ($\\checkmark$) both contributing terms:\n<div class=\"math-display\">\n$$0101 \\ (5) \\text{ and } 0111 \\ (7) \\implies 01-1 \\ (5, 7)$$\n</div></li>\n<li><strong>Iterative Expansion:</strong> Repeat the comparison process for 2-cell implicants, 4-cell implicants, etc., matching dashes in identical positions, until no further combinations are possible.</li>\n<li><strong>Prime Implicants:</strong> All terms that remain unchecked at the end of the process are the <strong>Prime Implicants (PIs)</strong>.</li>\n</ol>\n\n<h4>3. Prime Implicant Selection Chart & Petrick's Method</h4>\n<p>Construct a matrix where rows correspond to the PIs and columns correspond to the original function minterms (Don't Cares are omitted from columns):</p>\n<ul>\n<li>Place an $\\times$ in each column covered by a given PI.</li>\n<li>If a column contains only a single $\\times$, the corresponding row is an <strong>Essential Prime Implicant (EPI)</strong>. Check this row and cross off all columns covered by it.</li>\n<li>If uncovered minterms remain (cyclic prime implicant charts), apply <strong>Petrick's Method</strong>: formulate a product-of-sums Boolean expression $\\prod (P_i + P_j + \\dots)$ asserting that each column must be covered, and expand algebraically into SOP to identify the minimal literal solution.</li>\n</ul>"
        },
        {
          "id": "dig-3-4",
          "title": "Radix & Diminished Radix Complements: 1's & 2's Complement",
          "content": "<h4>1. Mathematical Definition of Radix Complements</h4>\n<p>To perform binary subtraction using standard adder hardware (eliminating the need for separate borrow-subtractor units), modern ALUs utilize complement arithmetic. In base $r$ with $n$ digits:</p>\n<ol>\n<li><strong>Diminished Radix Complement ($r-1$'s Complement):</strong>\n<div class=\"math-display\">\n$$(r - 1)\\text{'s Complement of } N = (r^n - 1) - N$$\n</div>\nIn binary ($r=2$), the $1$'s complement is $(2^n - 1) - N$, achieved simply by <strong>inverting every individual bit</strong> ($0 \\to 1, 1 \\to 0$). In decimal ($r=10$), the $9$'s complement is obtained by subtracting each digit from 9.</li>\n<li><strong>Radix Complement ($r$'s Complement):</strong>\n<div class=\"math-display\">\n$$r\\text{'s Complement of } N = r^n - N = [(r^n - 1) - N] + 1 = (r - 1)\\text{'s Complement} + 1$$\n</div>\nIn binary, the <strong>2's complement</strong> is obtained by inverting all bits and adding 1:\n<div class=\"math-display\">\n$$N_{2's} = \\bar{N} + 1$$\n</div>\nShortcut: Leave all least significant zeros and the first '1' unchanged; invert all remaining bits to the left.</li>\n</ol>\n\n<h4>2. Subtraction Using 2's Complement Arithmetic</h4>\n<p>To compute $M - N$ for $n$-bit unsigned numbers, the ALU evaluates $M + (2^n - N) = M - N + 2^n$:</p>\n<ul>\n<li><strong>Case 1 ($M \\ge N$):</strong> The sum produces an <strong>End Carry</strong> of $2^n$ ($C_{\\text{out}} = 1$). Discarding the carry yields the correct positive difference $M - N$.</li>\n<li><strong>Case 2 ($M < N$):</strong> No end carry occurs ($C_{\\text{out}} = 0$). The result is negative and equals the 2's complement of the true magnitude: $-(2^n - \\text{Sum})$.</li>\n</ul>\n\n<h4>3. Signed Binary Representation & Arithmetic Overflow</h4>\n<p>In signed $n$-bit 2's complement representation, the Most Significant Bit (MSB) acts as the sign bit ($0 \\leftrightarrow +, 1 \\leftrightarrow -$):</p>\n<div class=\"math-display\">\n$$\\text{Range of Signed } n\\text{-bit Integer: } -2^{n-1} \\le X \\le +2^{n-1} - 1$$\n</div>\n<p>For an 8-bit byte: $-128 \\le X \\le +127$. Crucially, 2's complement features a <strong>unique zero</strong> ($00000000_2$), unlike 1's complement which suffers from $+0$ and $-0$ ambiguities.</p>\n<p><strong>Overflow Condition ($V$):</strong> When adding two numbers of identical sign, the magnitude may exceed the representable range. Hardware detects overflow via an XOR gate comparing the carry into the sign bit ($C_{n-1}$) with the carry out of the sign bit ($C_n$):</p>\n<div class=\"math-display\">\n$$V = C_n \\oplus C_{n-1}$$\n</div>\n<p>If $V = 1$, an arithmetic overflow exception is signaled.</p>"
        },
        {
          "id": "dig-3-5",
          "title": "Adders & Subtractors: Half/Full Adders & Carry-Lookahead (CLA)",
          "simulation": "dig-adder-subtractor-sim",
          "content": "<h4>1. Half-Adder and Full-Adder Logic</h4>\n<p>The elementary building blocks of binary addition:</p>\n<ol>\n<li><strong>Half-Adder (HA):</strong> Adds two 1-bit inputs $A$ and $B$, producing Sum $S$ and Carry $C$:\n<div class=\"math-display\">\n$$S = A \\oplus B, \\quad C = A B$$\n</div></li>\n<li><strong>Full-Adder (FA):</strong> Adds three 1-bit inputs: operands $A, B$ and carry-in $C_{\\text{in}}$:\n<div class=\"math-display\">\n$$S = A \\oplus B \\oplus C_{\\text{in}}$$\n</div>\n<div class=\"math-display\">\n$$C_{\\text{out}} = A B + B C_{\\text{in}} + A C_{\\text{in}} = A B + C_{\\text{in}}(A \\oplus B)$$\n</div>\nA Full-Adder can be synthesized using two Half-Adders and one OR gate.</li>\n</ol>\n\n<h4>2. Ripple-Carry Parallel Adder Limitations</h4>\n<p>An $n$-bit parallel adder cascades $n$ Full-Adders, with $C_{\\text{out}, i}$ connected to $C_{\\text{in}, i+1}$. While hardware cost is minimal, the critical path requires the carry bit to \"ripple\" sequentially through all $n$ stages:</p>\n<div class=\"math-display\">\n$$t_{\\text{ripple}} = n \\cdot t_{\\text{carry}}$$\n</div>\n<p>For a 64-bit adder with $t_{\\text{carry}} = 1\\text{ ns}$, the total propagation delay is $64\\text{ ns}$, severely throttling CPU clock frequencies.</p>\n\n<h4>3. Carry-Lookahead Adder (CLA) Acceleration</h4>\n<p>To eliminate serial carry propagation, the Carry-Lookahead Adder generates all carry bits simultaneously in parallel using two auxiliary functions:</p>\n<ul>\n<li><strong>Carry Generate ($G_i$):</strong> $G_i = A_i B_i$ (a carry is generated inside stage $i$ regardless of carry-in).</li>\n<li><strong>Carry Propagate ($P_i$):</strong> $P_i = A_i \\oplus B_i$ (a carry-in to stage $i$ is propagated forward to stage $i+1$).</li>\n</ul>\n<p>Expressing stage carries recursively:</p>\n<div class=\"math-display\">\n$$C_1 = G_0 + P_0 C_0$$\n</div>\n<div class=\"math-display\">\n$$C_2 = G_1 + P_1 C_1 = G_1 + P_1 G_0 + P_1 P_0 C_0$$\n</div>\n<div class=\"math-display\">\n$$C_3 = G_2 + P_2 G_1 + P_2 P_1 G_0 + P_2 P_1 P_0 C_0$$\n</div>\n<div class=\"math-display\">\n$$C_4 = G_3 + P_3 G_2 + P_3 P_2 G_1 + P_3 P_2 P_1 G_0 + P_3 P_2 P_1 P_0 C_0$$\n</div>\n<p>Each carry depends strictly on the input operands and initial carry $C_0$, bypassing intermediate stages. All carries are computed simultaneously within a constant <strong>two-gate delay</strong>, irrespective of word length.</p>"
        },
        {
          "id": "dig-3-6",
          "title": "BCD Decimal Adders, Subtractors & Binary Multipliers",
          "content": "<h4>1. BCD Decimal Adder Architecture</h4>\n<p>In a Binary Coded Decimal (BCD) adder, two 4-bit BCD digits ($A, B \\in [0, 9]$) and carry-in $C_{\\text{in}}$ are summed using a standard 4-bit binary adder. If the binary sum $K \\le 9$, the result is a valid BCD digit. However, if the sum exceeds 9 ($10 \\le K \\le 19$), the 4-bit binary adder produces an invalid BCD codeword ($1010_2$ to $1111_2$) or an unrecorded carry:</p>\n<ul>\n<li><strong>Correction Condition:</strong> An invalid decimal state is flagged if:\n<div class=\"math-display\">\n$$\\text{Correction Carry } C_{\\text{out}} = K_4 + S_3 S_2 + S_3 S_1$$\n</div>\nwhere $K_4$ is the binary carry-out, $S_3 S_2$ flags 12 and 13, and $S_3 S_1$ flags 10 and 11.</li>\n<li><strong>Correction Circuit:</strong> Whenever $C_{\\text{out}} = 1$, the hardware adds $6_{10} = 0110_2$ to the sum via a second 4-bit binary adder. Adding 6 skips the 6 invalid 4-bit states, correctly producing the lower BCD digit and propagating the decimal carry $C_{\\text{out}} = 1$ to the next decade.</li>\n</ul>\n\n<h4>2. Controlled Adder/Subtractor Circuit</h4>\n<p>A single hardware unit performs both binary addition and subtraction by routing operand $B$ through conditional XOR inverters controlled by mode bit $M$:</p>\n<div class=\"math-display\">\n$$B_i^* = B_i \\oplus M, \\quad C_{\\text{in}} = M$$\n</div>\n<ul>\n<li>When $M = 0$: $B_i^* = B_i$ and $C_{\\text{in}} = 0 \\implies$ Evaluates $A + B$ (Addition).</li>\n<li>When $M = 1$: $B_i^* = \\bar{B}_i$ and $C_{\\text{in}} = 1 \\implies$ Evaluates $A + \\bar{B} + 1 = A - B$ (2's complement Subtraction).</li>\n</ul>\n\n<h4>3. Binary Array Multipliers</h4>\n<p>Multiplication of two unsigned binary numbers ($A = a_{m-1}\\dots a_0$ and $B = b_{n-1}\\dots b_0$) is synthesized as the accumulation of $m \\times n$ partial products $P_{i,j} = a_i \\cdot b_j$ generated by 2-input AND gates. In an $m \\times n$ array multiplier, partial product rows are shifted and summed using a 2D matrix of full adders, yielding product bits with delay scaling linearly with word length.</p>"
        }
      ],
      "problems": [
        {
          "id": "dig-p-3-1",
          "title": "4-Variable Karnaugh Map Optimization with Don't Care States",
          "statement": "A combinational switching function is defined by minterms and don't care conditions: $F(A, B, C, D) = \\sum m(1, 3, 7, 11, 15) + \\sum d(0, 2, 5)$. (a) Plot the function on a 4-variable Karnaugh map. (b) Identify all Prime Implicants and Essential Prime Implicants. (c) Derive the absolute minimal Sum-of-Products (SOP) expression and state the number of logic gates saved compared to the unsimplified canonical form.",
          "steps": [
            {
              "stepName": "Step 1: Plot Minterms and Don't Cares on K-Map",
              "math": "\\text{Rows } AB: 00, 01, 11, 10; \\quad \\text{Cols } CD: 00, 01, 11, 10. \\implies m(1,3,7,11,15)=1; \\ d(0,2,5)=\\times; \\ \\text{Others}=0",
              "explanation": "Fill K-map cells: m0=x, m1=1, m2=x, m3=1; m5=x, m7=1; m11=1; m15=1."
            },
            {
              "stepName": "Step 2: Form Prime Implicant Groups Using Don't Cares",
              "math": "\\text{Group 1 (Quad/Octet): Top row } (m_0, m_1, m_3, m_2) \\text{ contains } (\\times, 1, 1, \\times). \\text{ Combine with } (m_4=0, m_5=\\times, m_7=1, m_6=0)? \\text{ No.}",
              "explanation": "Top row cells (0, 1, 3, 2) form a Quad of four cells: CD has all 4 states, AB = 00 -> Term: A'B'."
            },
            {
              "stepName": "Step 3: Group the Vertical Column (m3, m7, m11, m15)",
              "math": "\\text{Column } CD = 11: m_3, m_7, m_{11}, m_{15} \\text{ are all 1s!} \\implies \\text{Column Quad covers all 4 cells} \\to \\text{Term: } C D",
              "explanation": "Column CD=11 forms an essential quad covering 3, 7, 11, 15: eliminates A and B."
            },
            {
              "stepName": "Step 4: Check Coverage of Minterm 1",
              "math": "m_1 \\text{ is covered by Quad } (m_0, m_1, m_3, m_2) \\to \\bar{A}\\bar{B}. \\quad \\text{Alternatively, Quad } (m_1, m_3, m_5, m_7) \\text{ covers } 1, 3, 5, 7 \\to \\bar{A} D",
              "explanation": "Choosing Quad (m1, m3, m5, m7) gives A'D. Column CD gives CD. Combined: F = A'D + CD = (A' + C)D."
            },
            {
              "stepName": "Step 5: Compare Minimal SOP Options",
              "math": "F = \\bar{A} D + C D = (\\bar{A} + C) D \\quad \\text{or} \\quad F = \\bar{A}\\bar{B} + C D",
              "explanation": "F = C D + A_bar D uses only 2 two-input gates. The unsimplified canonical form required 5 four-input AND gates plus a 5-input OR gate (30 inputs total), achieving a ~80% hardware reduction."
            }
          ],
          "answer": "F(A, B, C, D) = C D + \\bar{A} D \\quad \\text{or} \\quad F = C D + \\bar{A}\\bar{B} \\quad (\\text{Hardware reduced from 30 inputs to 5})"
        },
        {
          "id": "dig-p-3-2",
          "title": "Signed 2's Complement Addition, Subtraction and Overflow Detection",
          "statement": "Given two 8-bit signed binary numbers in 2's complement representation: $A = 01011000_2$ and $B = 01100100_2$. (a) Determine their decimal values. (b) Compute the sum $S = A + B$ in 8-bit 2's complement arithmetic. (c) Evaluate the carry into the sign bit $C_7$ and carry out of the sign bit $C_8$, determine the overflow flag $V = C_8 \\oplus C_7$, and explain the physical significance of the result.",
          "steps": [
            {
              "stepName": "Step 1: Convert Operands to Decimal",
              "math": "A = 01011000_2 \\implies + (64 + 16 + 8) = +88_{10}. \\quad B = 01100100_2 \\implies + (64 + 32 + 4) = +100_{10}",
              "explanation": "Both numbers have MSB = 0, representing positive decimal integers."
            },
            {
              "stepName": "Step 2: Perform 8-bit Binary Addition",
              "math": "\\begin{matrix} & 01011000 \\quad (+88) \\\\ + & 01100100 \\quad (+100) \\\\ \\hline & 10111100 \\end{matrix}",
              "explanation": "Add bits from right to left: sum is 10111100_2."
            },
            {
              "stepName": "Step 3: Evaluate Carries into and out of MSB",
              "math": "C_7 (\\text{carry into bit 7}) = 1 \\ (\\text{from } 1 + 1 + 0 = 0 \\text{ R } 1), \\quad C_8 (\\text{carry out of bit 7}) = 0 \\ (\\text{from } 0 + 0 + 1 = 1 \\text{ R } 0)",
              "explanation": "A carry of 1 entered the sign position (bit 7), but no carry exited bit 7."
            },
            {
              "stepName": "Step 4: Compute Overflow Flag V",
              "math": "V = C_8 \\oplus C_7 = 0 \\oplus 1 = 1 \\implies \\text{OVERFLOW DETECTED!}",
              "explanation": "Because V = 1, the arithmetic result is invalid."
            },
            {
              "stepName": "Step 5: Physical Interpretation",
              "math": "\\text{True sum: } +88 + 100 = +188_{10}. \\quad \\text{8-bit signed range: } [-128, +127]. \\quad \\text{Hardware interpretation of } 10111100_2 = -68_{10}",
              "explanation": "Adding two positive numbers produced an apparent negative result (-68) because +188 exceeds the maximum positive 8-bit bound (+127). The ALU sets V=1 to trap the overflow."
            }
          ],
          "answer": "A = +88, \\ B = +100; \\quad S = 10111100_2; \\quad C_7 = 1, \\ C_8 = 0 \\implies V = 1 \\quad (\\text{Arithmetic Overflow Exception})"
        },
        {
          "id": "dig-p-3-3",
          "title": "Carry-Lookahead Adder (CLA) vs Ripple-Carry Delay Analysis",
          "statement": "A 16-bit parallel adder is designed using (a) standard ripple-carry full adders where each full adder has gate delays: $t_{\\text{sum}} = 6\\text{ ns}$ and $t_{\\text{carry}} = 2\\text{ ns}$, versus (b) a 16-bit Carry-Lookahead Adder (CLA) partitioned into four 4-bit CLA blocks with lookahead carry generators. Calculate the total worst-case addition delay for both designs and evaluate the speedup factor achieved by the CLA architecture.",
          "steps": [
            {
              "stepName": "Step 1: Calculate Worst-Case Ripple-Carry Delay",
              "math": "t_{\\text{ripple}} = (n - 1) \\cdot t_{\\text{carry}} + t_{\\text{sum}} = (16 - 1) \\times 2\\text{ ns} + 6\\text{ ns} = 15 \\times 2 + 6 = 36\\text{ ns}",
              "explanation": "The carry must ripple through 15 stages before the final stage generates its sum bit."
            },
            {
              "stepName": "Step 2: Analyze 4-bit CLA Architecture Timing",
              "math": "t_{P,G} = 1\\text{ gate delay } (2\\text{ ns}), \\quad t_{\\text{carry, CLA}} = 2\\text{ gate delays } (4\\text{ ns}), \\quad t_{\\text{sum, CLA}} = 2\\text{ gate delays } (4\\text{ ns})",
              "explanation": "Inside each 4-bit block, P and G terms take 2 ns; lookahead carry logic takes 4 ns."
            },
            {
              "stepName": "Step 3: Compute Total CLA Delay Across 4 Blocks",
              "math": "t_{\\text{total, CLA}} = t_{P,G} + (4 \\text{ blocks} - 1) \\cdot t_{\\text{block carry}} + t_{\\text{sum}} = 2\\text{ ns} + (3 \\times 4\\text{ ns}) + 4\\text{ ns} = 2 + 12 + 4 = 18\\text{ ns}",
              "explanation": "Evaluate total block lookahead propagation: 18 ns."
            },
            {
              "stepName": "Step 4: Compute Speedup Factor",
              "math": "\\text{Speedup} = \\frac{t_{\\text{ripple}}}{t_{\\text{CLA}}} = \\frac{36\\text{ ns}}{18\\text{ ns}} = 2.0 \\times \\quad (\\text{100\\% faster})",
              "explanation": "For 32-bit and 64-bit word lengths, CLA speedup exceeds 4x to 8x."
            }
          ],
          "answer": "t_{\\text{ripple}} = 36\\text{ ns}, \\quad t_{\\text{CLA}} = 18\\text{ ns} \\implies \\text{Speedup Factor: } 2.0\\times"
        }
      ]
    },
    {
      "unitNumber": 4,
      "unitId": "unit4-flip-flops-multivibrators",
      "title": "Latches, Flip-Flops & Multivibrator Timing Circuits",
      "description": "Bistable memory primitives and relaxation oscillator timing: cross-coupled BJT transistor latches, active-LOW NAND and active-HIGH NOR latches; clocked level-triggered SR and D transparent latches; edge-triggered flip-flops (master-slave architecture, dynamic setup time t_su and hold time t_h); the JK flip-flop, race-around hazard elimination, characteristic equations Q(t+1), excitation tables, and T flip-flop conversion; multivibrator classes (astable, monostable, bistable) and Schmitt trigger hysteresis; the 555 integrated timer internal comparator architecture, astable frequency, and duty cycle design.",
      "sections": [
        {
          "id": "dig-4-1",
          "title": "Bistable Elements: Cross-Coupled Inverters & SR Latches",
          "content": "<h4>1. The Fundamental Bistable Circuit Principle</h4>\n<p>While combinational circuits produce outputs that depend strictly on current inputs, <strong>sequential circuits</strong> incorporate memory elements whose outputs depend on both current inputs and the past sequence of states. The most primitive electronic memory cell is the <strong>bistable multivibrator</strong>, formed by cross-coupling two inverting stages with positive feedback ($A_v > 1$):</p>\n<div class=\"math-display\">\n$$Q = \\overline{\\bar{Q}}, \\quad \\bar{Q} = \\bar{Q}$$\n</div>\n<p>The circuit possesses two stable equilibrium states: State 1 ($Q=1, \\bar{Q}=0$, \"SET\") and State 2 ($Q=0, \\bar{Q}=1$, \"RESET\"). The intermediate state where both inverters operate in their linear amplification region ($V_{\\text{in}} = V_{\\text{out}} \\approx V_{DD}/2$) is <strong>metastable</strong>; infinitesimal thermal noise forces the cell to regenerate into one of the two stable binary states.</p>\n\n<h4>2. Active-HIGH NOR Latch</h4>\n<p>Constructed by cross-coupling two 2-input NOR gates with inputs $S$ (Set) and $R$ (Reset):</p>\n<div class=\"math-display\">\n$$Q_{n+1} = \\overline{R + \\bar{Q}_n}, \\quad \\bar{Q}_{n+1} = \\overline{S + Q_n}$$\n</div>\n<ul>\n<li>$S=0, R=0$: <strong>Hold / Memory State</strong> ($Q_{n+1} = Q_n$). Latches the previous bit indefinitely.</li>\n<li>$S=1, R=0$: <strong>Set State</strong> ($Q_{n+1} = 1, \\bar{Q}_{n+1} = 0$).</li>\n<li>$S=0, R=1$: <strong>Reset State</strong> ($Q_{n+1} = 0, \\bar{Q}_{n+1} = 1$).</li>\n<li>$S=1, R=1$: <strong>Forbidden / Invalid State</strong>. Forces both outputs to $0$ ($Q = \\bar{Q} = 0$), violating complementarity. If both inputs return simultaneously to $0$, race conditions lead to unpredictable metastable collapse.</li>\n</ul>\n\n<h4>3. Active-LOW NAND Latch</h4>\n<p>Constructed by cross-coupling two 2-input NAND gates with active-LOW inputs $\\bar{S}$ and $\\bar{R}$:</p>\n<div class=\"math-display\">\n$$Q_{n+1} = \\overline{\\bar{S} \\cdot \\bar{Q}_n}, \\quad \\bar{Q}_{n+1} = \\overline{\\bar{R} \\cdot Q_n}$$\n</div>\n<ul>\n<li>$\\bar{S}=1, \\bar{R}=1$: <strong>Hold State</strong>.</li>\n<li>$\\bar{S}=0, \\bar{R}=1$: <strong>Set State</strong> ($Q=1$).</li>\n<li>$\\bar{S}=1, \\bar{R}=0$: <strong>Reset State</strong> ($Q=0$).</li>\n<li>$\\bar{S}=0, \\bar{R}=0$: <strong>Forbidden State</strong> ($Q = \\bar{Q} = 1$).</li>\n</ul>"
        },
        {
          "id": "dig-4-2",
          "title": "Clocked Latches: Synchronous SR & Transparent D Latch",
          "content": "<h4>1. Clocked SR Latch</h4>\n<p>To synchronize state transitions with a central clock signal ($CLK$), two steering NAND gates precede the basic NAND latch:</p>\n<div class=\"math-display\">\n$$S^* = \\overline{S \\cdot CLK}, \\quad R^* = \\overline{R \\cdot CLK}$$\n</div>\n<ul>\n<li>When $CLK = 0$: $S^* = R^* = 1$. The latch remains frozen in its hold state regardless of $S$ and $R$.</li>\n<li>When $CLK = 1$: $S^* = \\bar{S}$ and $R^* = \\bar{R}$. The latch responds directly to $S$ and $R$ inputs.</li>\n</ul>\n\n<h4>2. The Transparent D Latch</h4>\n<p>To eliminate the forbidden $S=R=1$ hazard, an inverter is placed between the inputs ($R = \\bar{S}$), creating the single-input <strong>Data or D Latch</strong> ($S = D, R = \\bar{D}$):</p>\n<div class=\"math-display\">\n$$Q_{n+1} = D \\quad (\\text{when } CLK = 1)$$\n</div>\n<ul>\n<li><strong>Transparent Mode ($CLK = 1$):</strong> The output $Q$ tracks input $D$ continuously in real time with minimal gate delay. Any noise or glitches on $D$ propagate directly to $Q$.</li>\n<li><strong>Latched Mode ($CLK = 0$):</strong> The output $Q$ freezes, holding the value present at $D$ at the instant the clock fell.</li>\n</ul>"
        },
        {
          "id": "dig-4-3",
          "title": "Edge-Triggered Flip-Flops: Master-Slave & Timing Windows",
          "simulation": "dig-flipflop-clock-sim",
          "content": "<h4>1. Edge-Triggering vs Level-Sensitivity</h4>\n<p>A <strong>latch</strong> is level-sensitive: it responds continuously as long as the clock enable remains active. In contrast, an <strong>edge-triggered flip-flop</strong> samples its input and changes state <em>only</em> during an infinitesimal transition edge of the clock signal—either the <strong>positive (rising) edge</strong> ($0 \\to 1$) or the <strong>negative (falling) edge</strong> ($1 \\to 0$).</p>\n\n<h4>2. Master-Slave Architecture</h4>\n<p>A classic edge-triggered flip-flop cascades two clocked latches in series controlled by complementary clock phases:</p>\n<ol>\n<li><strong>Master Latch:</strong> Enabled when $CLK = 1$. Samples data input $D$ while the slave is disabled ($\\overline{CLK} = 0$). Output $Q_M$ tracks $D$, but external output $Q$ remains isolated.</li>\n<li><strong>Slave Latch:</strong> Enabled when $CLK$ transitions from $1 \\to 0$ ($\\overline{CLK} \\to 1$). The master latch instantly freezes, and the slave copies the frozen state $Q_M$ to the external output $Q$.</li>\n</ol>\n<p>Because the master and slave are never enabled simultaneously, data cannot ripple through both stages in a single clock cycle, completely severing feedthrough loops in shift registers and counters.</p>\n\n<h4>3. Dynamic Timing Parameters: Setup Time & Hold Time</h4>\n<p>Reliable digital state capture requires strict adherence to dynamic timing windows:</p>\n<ul>\n<li><strong>Setup Time ($t_{su}$):</strong> The minimum duration that the data input $D$ must remain stable <em>before</em> the active clock edge arrives. Typically $1 - 5\\text{ ns}$ (down to tens of picoseconds in deep submicron CMOS).</li>\n<li><strong>Hold Time ($t_h$):</strong> The minimum duration that the data input $D$ must remain stable <em>after</em> the active clock edge has transitioned.</li>\n<li><strong>Propagation Delay ($t_{pd} = t_{CLK \\to Q}$):</strong> The time delay between the active clock edge and the appearance of the new valid state at output $Q$.</li>\n<li><strong>Metastability Hazard:</strong> If input $D$ transitions within the forbidden setup/hold aperture ($t_{su} + t_h$), internal regenerative feedback can hang in an indeterminate analog voltage state for an unbounded duration before collapsing randomly to 0 or 1, causing catastrophic hardware crashes.</li>\n</ul>"
        },
        {
          "id": "dig-4-4",
          "title": "The JK Flip-Flop: Race-Around Elimination & T Flip-Flops",
          "content": "<h4>1. The Race-Around Condition Hazard</h4>\n<p>In a level-triggered JK latch with inputs $J = K = 1$, the output toggles ($Q \\to \\bar{Q}$). If the clock pulse width $t_w$ is longer than the propagation delay of the flip-flop ($t_{pd}$):</p>\n<div class=\"math-display\">\n$$t_{pd} < t_w$$\n</div>\n<p>the newly toggled output will feed back to the input gates while the clock is still HIGH, causing the output to toggle repeatedly back and forth (\"race around\") throughout the pulse duration $t_w$. The final state of $Q$ when the clock falls is completely unpredictable.</p>\n<p><strong>Race-Around Elimination Methods:</strong></p>\n<ol>\n<li>Narrow clock pulses ($t_w < t_{pd}$, difficult to guarantee across temperature and process variations).</li>\n<li><strong>Edge-Triggered Design:</strong> State transitions occur only during clock edges ($\\sim 1\\text{ ns}$).</li>\n<li><strong>Master-Slave JK Flip-Flop:</strong> The master isolates inputs while the slave updates outputs.</li>\n</ol>\n\n<h4>2. Truth Table & Characteristic Equation of the JK Flip-Flop</h4>\n<div class=\"table-responsive\">\n<table class=\"table table-bordered\">\n<thead>\n<tr><th>$J$</th><th>$K$</th><th>$Q_{n+1}$</th><th>Operational Mode</th></tr>\n</thead>\n<tbody>\n<tr><td>$0$</td><td>$0$</td><td>$Q_n$</td><td>Hold / No Change</td></tr>\n<tr><td>$0$</td><td>$1$</td><td>$0$</td><td>Reset</td></tr>\n<tr><td>$1$</td><td>$0$</td><td>$1$</td><td>Set</td></tr>\n<tr><td>$1$</td><td>$1$</td><td>$\\bar{Q}_n$</td><td>Toggle</td></tr>\n</tbody>\n</table>\n</div>\n<p>From the K-map of next-state $Q_{n+1}$, the <strong>Characteristic Equation</strong> is:</p>\n<div class=\"math-display\">\n$$Q_{n+1} = J \\bar{Q}_n + \\bar{K} Q_n$$\n</div>\n\n<h4>3. The Toggle (T) Flip-Flop</h4>\n<p>Formed by tying the $J$ and $K$ inputs together ($J = K = T$):</p>\n<div class=\"math-display\">\n$$Q_{n+1} = T \\bar{Q}_n + \\bar{T} Q_n = T \\oplus Q_n$$\n</div>\n<ul>\n<li>When $T = 0$: $Q_{n+1} = Q_n$ (Hold).</li>\n<li>When $T = 1$: $Q_{n+1} = \\bar{Q}_n$ (Toggle). Divides the input clock frequency by exactly <strong>2</strong> ($f_{\\text{out}} = f_{\\text{clk}} / 2$), forming the foundational block for binary ripple counters.</li>\n</ul>"
        },
        {
          "id": "dig-4-5",
          "title": "Multivibrators: Astable, Monostable & Schmitt Triggers",
          "content": "<h4>1. Classification of Multivibrator Circuits</h4>\n<p>Multivibrators are regenerative switching circuits categorized by their number of permanently stable states:</p>\n<ol>\n<li><strong>Bistable:</strong> Two permanently stable states (Flip-Flops, Latches). Requires an external trigger pulse to transition between states.</li>\n<li><strong>Monostable (One-Shot):</strong> One stable state and one quasi-stable state. An incoming trigger pulse initiates a transition to the quasi-stable state, where it remains for a predetermined duration $\\tau = R C \\ln(2) \\approx 0.693 R C$ before returning automatically to the stable state. Used for pulse widening, debouncing switches, and fixed-delay generation.</li>\n<li><strong>Astable (Free-Running Oscillator):</strong> Zero stable states. The circuit oscillates continuously between two quasi-stable states without external excitation, generating square wave clock signals.</li>\n</ol>\n\n<h4>2. The Schmitt Trigger & Hysteresis</h4>\n<p>Otto Schmitt (1937) invented the <strong>Schmitt Trigger</strong>, a comparator circuit with positive feedback that exhibits <strong>hysteresis</strong>—two distinct switching threshold voltages:</p>\n<ul>\n<li><strong>Upper Trigger Point ($V_{UTP}$):</strong> When input voltage rises, output remains HIGH until $V_{\\text{in}} \\ge V_{UTP}$, at which point it snaps sharply to LOW.</li>\n<li><strong>Lower Trigger Point ($V_{LTP}$):</strong> When input voltage falls, output remains LOW until $V_{\\text{in}} \\le V_{LTP}$, at which point it snaps sharply back to HIGH.</li>\n<li><strong>Hysteresis Band ($\\Delta V_H = V_{UTP} - V_{LTP}$):</strong> Completely rejects electrical noise and slow input voltage transitions, preventing erratic multi-trigger ringing on clock inputs.</li>\n</ul>"
        },
        {
          "id": "dig-4-6",
          "title": "The 555 Integrated Timer: Internal Architecture & Astable Design",
          "simulation": "dig-555-timer-sim",
          "content": "<h4>1. Internal Architecture of the 555 Timer IC</h4>\n<p>The iconic 555 timer (Signetics, 1971) contains 23 transistors, 2 diodes, and 16 resistors integrated on silicon, structured into four functional blocks:</p>\n<ol>\n<li><strong>Precision Resistor Divider:</strong> Three matched $5\\text{ k}\\Omega$ resistors establish internal reference voltages of $\\frac{2}{3} V_{CC}$ and $\\frac{1}{3} V_{CC}$ (hence the name \"555\").</li>\n<li><strong>Threshold Comparator (Comp 1):</strong> Compares Pin 6 (Threshold) to $\\frac{2}{3} V_{CC}$. If $V_{\\text{thresh}} > \\frac{2}{3} V_{CC}$, sets the internal flip-flop ($R=1$).</li>\n<li><strong>Trigger Comparator (Comp 2):</strong> Compares Pin 2 (Trigger) to $\\frac{1}{3} V_{CC}$. If $V_{\\text{trig}} < \\frac{1}{3} V_{CC}$, resets the internal flip-flop ($S=1$).</li>\n<li><strong>RS Flip-Flop & Discharge Transistor ($Q_{\\text{dis}}$):</strong> Drives output Pin 3 through a high-current totem-pole driver ($\\pm 200\\text{ mA}$) and controls Pin 7 (Discharge open-collector transistor to ground).</li>\n</ol>\n\n<h4>2. Astable Multivibrator Frequency & Duty Cycle Equations</h4>\n<p>Connected with external timing resistors $R_A, R_B$ and capacitor $C$, the capacitor charges through $R_A + R_B$ toward $V_{CC}$ and discharges through $R_B$ toward ground:</p>\n<ul>\n<li><strong>Charge Interval ($t_{\\text{high}}$):</strong> $V_C(t)$ rises from $\\frac{1}{3} V_{CC}$ to $\\frac{2}{3} V_{CC}$:\n<div class=\"math-display\">\n$$t_{\\text{high}} = (R_A + R_B) C \\ln(2) \\approx 0.693 (R_A + R_B) C$$\n</div></li>\n<li><strong>Discharge Interval ($t_{\\text{low}}$):</strong> $V_C(t)$ falls from $\\frac{2}{3} V_{CC}$ to $\\frac{1}{3} V_{CC}$:\n<div class=\"math-display\">\n$$t_{\\text{low}} = R_B C \\ln(2) \\approx 0.693 R_B C$$\n</div></li>\n<li><strong>Total Oscillation Period ($T$):</strong>\n<div class=\"math-display\">\n$$T = t_{\\text{high}} + t_{\\text{low}} = 0.693 (R_A + 2 R_B) C$$\n</div></li>\n<li><strong>Output Frequency ($f$):</strong>\n<div class=\"math-display\">\n$$f = \\frac{1}{T} = \\frac{1.44}{(R_A + 2 R_B) C}$$\n</div></li>\n<li><strong>Duty Cycle ($D$):</strong>\n<div class=\"math-display\">\n$$D = \\frac{t_{\\text{high}}}{T} = \\frac{R_A + R_B}{R_A + 2 R_B} \\times 100\\%$$\n</div>\nBecause $R_A > 0$, standard astable connections have $D > 50\\%$. Connecting a steering diode across $R_B$ bypasses $R_B$ during charging, enabling $50\\%$ or lower duty cycles ($t_{\\text{high}} \\approx 0.693 R_A C$).</li>\n</ul>"
        }
      ],
      "problems": [
        {
          "id": "dig-p-4-1",
          "title": "Race-Around Condition Analysis in Level-Triggered JK Flip-Flops",
          "statement": "A level-triggered JK flip-flop has a clock pulse width of $t_w = 40\\text{ ns}$ and an internal propagation delay of $t_{pd} = 12\\text{ ns}$. (a) Determine if the race-around condition occurs when $J = K = 1$. (b) Calculate how many times the output toggles during a single clock pulse. (c) Explain how a Master-Slave JK flip-flop eliminates this hazard regardless of clock pulse width.",
          "steps": [
            {
              "stepName": "Step 1: Compare Clock Width to Propagation Delay",
              "math": "t_w = 40\\text{ ns} > t_{pd} = 12\\text{ ns} \\implies \\text{Condition for Race-Around: } t_w > t_{pd} \\text{ IS MET!}",
              "explanation": "Because the clock pulse remains HIGH longer than the propagation delay, outputs feed back to inputs while the clock is still enabled."
            },
            {
              "stepName": "Step 2: Calculate Number of Output Toggles",
              "math": "N_{\\text{toggles}} = \\left\\lfloor \\frac{t_w}{t_{pd}} \\right\\rfloor = \\left\\lfloor \\frac{40\\text{ ns}}{12\\text{ ns}} \\right\\rfloor = 3 \\text{ complete toggles}",
              "explanation": "The output toggles 3 times during the single pulse, leaving the final output unpredictable."
            },
            {
              "stepName": "Step 3: Master-Slave Elimination Mechanism",
              "math": "\\text{When } CLK=1: \\text{ Master samples } (J, K), \\text{ Slave is disabled}. \\quad \\text{When } CLK=0: \\text{ Master is isolated}, \\text{ Slave updates } Q.",
              "explanation": "Because Master and Slave are never enabled simultaneously, feedback from the slave cannot reach the master during the same clock cycle, completely extinguishing the race-around hazard."
            }
          ],
          "answer": "\\text{Race-around occurs } (t_w > t_{pd}); \\quad N = 3 \\text{ toggles per pulse}; \\quad \\text{Master-Slave isolates feedback path}"
        },
        {
          "id": "dig-p-4-2",
          "title": "555 Timer Astable Multivibrator Component Calculation",
          "statement": "Design an astable 555 timer clock generator to produce a square wave with frequency $f = 10.0\\text{ kHz}$ and duty cycle $D = 65.0\\%$. If a timing capacitor of $C = 10.0\\text{ nF}$ is chosen: (a) Calculate the required values for resistors $R_A$ and $R_B$. (b) Calculate the high time $t_{\\text{high}}$ and low time $t_{\\text{low}}$.",
          "steps": [
            {
              "stepName": "Step 1: Calculate Total Period T",
              "math": "T = \\frac{1}{f} = \\frac{1}{10.0 \\times 10^3\\text{ Hz}} = 100\\text{ \\mu s}",
              "explanation": "Compute total period: 100 microseconds."
            },
            {
              "stepName": "Step 2: Calculate High Time and Low Time",
              "math": "t_{\\text{high}} = D \\cdot T = 0.650 \\times 100\\text{ \\mu s} = 65.0\\text{ \\mu s}, \\quad t_{\\text{low}} = T - t_{\\text{high}} = 35.0\\text{ \\mu s}",
              "explanation": "Calculate high and low durations."
            },
            {
              "stepName": "Step 3: Solve for Resistor R_B",
              "math": "t_{\\text{low}} = 0.693 R_B C \\implies R_B = \\frac{t_{\\text{low}}}{0.693 C} = \\frac{35.0 \\times 10^{-6}\\text{ s}}{0.693 \\times (10.0 \\times 10^{-9}\\text{ F})} \\approx 5050\\text{ }\\Omega = 5.05\\text{ k}\\Omega",
              "explanation": "Evaluate R_B: approximately 5.05 kOhm (standard 5.1 kOhm)."
            },
            {
              "stepName": "Step 4: Solve for Resistor R_A",
              "math": "t_{\\text{high}} = 0.693 (R_A + R_B) C \\implies R_A + R_B = \\frac{65.0 \\times 10^{-6}}{0.693 \\times 10^{-8}} \\approx 9380\\text{ }\\Omega \\implies R_A = 9380 - 5050 = 4330\\text{ }\\Omega = 4.33\\text{ k}\\Omega",
              "explanation": "Evaluate R_A: approximately 4.33 kOhm (standard 4.3 kOhm)."
            }
          ],
          "answer": "R_A = 4.33\\text{ k}\\Omega, \\quad R_B = 5.05\\text{ k}\\Omega, \\quad t_{\\text{high}} = 65.0\\text{ \\mu s}, \\quad t_{\\text{low}} = 35.0\\text{ \\mu s}"
        },
        {
          "id": "dig-p-4-3",
          "title": "Flip-Flop Conversion: Synthesis of D Flip-Flop Using a JK Flip-Flop",
          "statement": "Convert a standard JK flip-flop into a D-type flip-flop: (a) Construct the excitation table showing required $J$ and $K$ inputs for all four desired $Q_n \\to Q_{n+1}$ state transitions under input $D$. (b) Derive the minimized Boolean equations for $J$ and $K$ in terms of $D$. (c) Draw the hardware gate connection logic.",
          "steps": [
            {
              "stepName": "Step 1: Construct the Conversion Excitation Table",
              "math": "\\begin{matrix} D & Q_n & Q_{n+1} & J & K \\\\ \\hline 0 & 0 & 0 & 0 & \\times \\\\ 0 & 1 & 0 & \\times & 1 \\\\ 1 & 0 & 1 & 1 & \\times \\\\ 1 & 1 & 1 & \\times & 0 \\end{matrix}",
              "explanation": "Map desired transition Q_n -> Q_(n+1) to JK excitation rules."
            },
            {
              "stepName": "Step 2: Derive Minimized K-Map Equations for J and K",
              "math": "J(D, Q_n): J(0,0)=0, J(1,0)=1, J(0,1)=\\times, J(1,1)=\\times \\implies J = D",
              "explanation": "K-map for J reduces to J = D."
            },
            {
              "stepName": "Step 3: Derive Equation for K",
              "math": "K(D, Q_n): K(0,0)=\\times, K(1,0)=\\times, K(0,1)=1, K(1,1)=0 \\implies K = \\bar{D}",
              "explanation": "K-map for K reduces to K = D_bar."
            },
            {
              "stepName": "Step 4: Hardware Realization",
              "math": "J = D, \\quad K = \\bar{D} = \\text{NOT}(D)",
              "explanation": "A single NOT gate connecting D to K, with D connected directly to J, converts any JK flip-flop into a D flip-flop."
            }
          ],
          "answer": "J = D, \\quad K = \\bar{D} \\quad (\\text{Single Inverter between } J \\text{ and } K)"
        }
      ]
    },
    {
      "unitNumber": 5,
      "unitId": "unit5-counters-registers-msi",
      "title": "Counters, Shift Registers & Combinational MSI Subsystems",
      "description": "Comprehensive design and operational analysis of medium-scale integrated (MSI) digital building blocks: asynchronous (ripple) up/down counters, propagation delay accumulation, and MOD-N reset truncation; systematic synchronous counter synthesis via excitation tables, state transition graphs, and lockout protection; shift register architectures (SISO, SIPO, PISO, PIPO, universal bidirectional), Ring and Johnson twisted counters; decoders (3-to-8, BCD-to-7-segment), priority encoders, multiplexers as universal logic modules, and demultiplexers.",
      "sections": [
        {
          "id": "dig-5-1",
          "title": "Asynchronous (Ripple) Counters & MOD-N Truncation",
          "content": "<h4>1. Working Principle of Asynchronous (Ripple) Counters</h4>\n<p>An <strong>asynchronous counter</strong> (or ripple counter) consists of a cascade of toggle flip-flops (T or JK flip-flops with $J=K=1$) where only the first flip-flop ($FF_0$) is clocked by the external master clock. Each subsequent flip-flop $FF_{i+1}$ is clocked by the output ($Q_i$ or $\\bar{Q}_i$) of the preceding stage:</p>\n<ul>\n<li><strong>Negative Edge-Triggered Up-Counter:</strong> Clocking $FF_{i+1}$ from output $Q_i$ causes $FF_{i+1}$ to toggle whenever $Q_i$ transitions from $1 \\to 0$, creating a standard binary count sequence ($0, 1, 2, \\dots, 2^n - 1$).</li>\n<li><strong>Negative Edge-Triggered Down-Counter:</strong> Clocking $FF_{i+1}$ from inverted output $\\bar{Q}_i$ creates a downward counting sequence ($2^n - 1, \\dots, 1, 0$).</li>\n</ul>\n\n<h4>2. Propagation Delay Accumulation & Maximum Operating Frequency</h4>\n<p>Because each flip-flop must wait for the preceding stage to settle, the total propagation delay accumulates linearly with the number of stages $n$:</p>\n<div class=\"math-display\">\n$$t_{\\text{total}} = n \\cdot t_{pd}$$\n</div>\n<p>To avoid false count sampling, the clock period $T_{\\text{clk}}$ must be strictly greater than this accumulated delay:</p>\n<div class=\"math-display\">\n$$T_{\\text{clk}} \\ge n \\cdot t_{pd} + t_s \\implies f_{\\text{max}} \\le \\frac{1}{n \\cdot t_{pd} + t_s}$$\n</div>\n<p>For an 8-bit ripple counter with $t_{pd} = 15\\text{ ns}$, $t_{\\text{total}} = 120\\text{ ns}$, capping clock speed below $8.3\\text{ MHz}$. During the transient settling window, intermediate invalid states produce severe false output \"glitches\".</p>\n\n<h4>3. Truncated Modulus Counters (MOD-N Counters)</h4>\n<p>An $n$-stage binary counter naturally recycles after $2^n$ counts (natural modulus $MOD = 2^n$). To construct a counter with an arbitrary modulus $N < 2^n$ (e.g., a <strong>decade / BCD counter</strong> with $MOD = 10$ using $n = 4$ flip-flops):</p>\n<ol>\n<li>Identify the binary representation of target modulus $N$. For $N = 10_{10} = 1010_2$, bits $Q_3 = 1$ and $Q_1 = 1$.</li>\n<li>Connect $Q_3$ and $Q_1$ to the inputs of an asynchronous NAND gate, and connect the NAND output to the active-LOW asynchronous Clear ($\\overline{CLR}$) pins of all four flip-flops.</li>\n<li>As soon as the counter reaches state $1010_2$, the NAND gate output goes LOW, instantaneously resetting all flip-flops to $0000_2$. The state $1010_2$ persists for only a few nanoseconds (the clear propagation delay), yielding a stable 10-state sequence ($0$ through $9$).</li>\n</ol>"
        },
        {
          "id": "dig-5-2",
          "title": "Synchronous Counter Synthesis & State Machine Design",
          "simulation": "dig-synchronous-counter-sim",
          "content": "<h4>1. The Synchronous Architecture Advantage</h4>\n<p>In a <strong>synchronous counter</strong>, all flip-flops are connected to the <strong>same common master clock signal</strong>. All state transitions occur simultaneously across all stages at the active clock edge. Propagation delay is independent of counter bit length, being limited solely to a single flip-flop delay plus one combinational gating level:</p>\n<div class=\"math-display\">\n$$f_{\\text{max, sync}} = \\frac{1}{t_{pd, FF} + t_{pd, \\text{gate}} + t_{su}}$$\n</div>\n\n<h4>2. Formal Step-by-Step Synthesis Algorithm</h4>\n<ol>\n<li><strong>State Diagram & State Transition Table:</strong> Formulate the sequence of present states $Q_n$ and required next states $Q_{n+1}$.</li>\n<li><strong>Select Flip-Flop Type:</strong> Typically JK or D flip-flops. Reference the <strong>Excitation Table</strong>:\n<div class=\"table-responsive\">\n<table class=\"table table-bordered\">\n<thead>\n<tr><th>Transition ($Q_n \\to Q_{n+1}$)</th><th>Required $J$</th><th>Required $K$</th><th>Required $D$</th><th>Required $T$</th></tr>\n</thead>\n<tbody>\n<tr><td>$0 \\to 0$</td><td>$0$</td><td>$\\times$</td><td>$0$</td><td>$0$</td></tr>\n<tr><td>$0 \\to 1$</td><td>$1$</td><td>$\\times$</td><td>$1$</td><td>$1$</td></tr>\n<tr><td>$1 \\to 0$</td><td>$\\times$</td><td>$1$</td><td>$0$</td><td>$1$</td></tr>\n<tr><td>$1 \\to 1$</td><td>$\\times$</td><td>$0$</td><td>$1$</td><td>$0$</td></tr>\n</tbody>\n</table>\n</div></li>\n<li><strong>K-Map Derivation of Flip-Flop Excitation Inputs:</strong> Plot $J_i, K_i$ (or $D_i$) as functions of present state variables $Q_k$, exploiting Don't Care states to obtain minimal Boolean equations.</li>\n<li><strong>Lockout Verification:</strong> Analyze unassigned or unused states. If electrical noise drops the counter into an unused state, it must self-recover back to the valid sequence within a finite number of clock cycles rather than circulating indefinitely in a parasitic <strong>lockout cycle</strong>.</li>\n</ol>"
        },
        {
          "id": "dig-5-3",
          "title": "Shift Registers: SISO, SIPO, PISO, PIPO, Ring & Johnson",
          "simulation": "dig-shift-register-ring-sim",
          "content": "<h4>1. Shift Register Functional Topologies</h4>\n<p>A <strong>shift register</strong> is an array of cascaded flip-flops configured such that stored binary data moves laterally by one bit position on each clock pulse. The four fundamental operational topologies are:</p>\n<ol>\n<li><strong>Serial-In Serial-Out (SISO):</strong> Data bits enter sequentially one bit per clock pulse and exit sequentially from the final stage. Requires $n$ clock cycles to load and $n$ clock cycles to read out an $n$-bit word. Acts as an accurate time delay line.</li>\n<li><strong>Serial-In Parallel-Out (SIPO):</strong> Data is shifted in serially; once filled after $n$ clock pulses, all $n$ bits are read out simultaneously in parallel. Fundamental to UART serial communication receivers.</li>\n<li><strong>Parallel-In Serial-Out (PISO):</strong> Data is loaded in parallel simultaneously via combinational steering gates, then shifted out serially one bit at a time. Fundamental to UART serial communication transmitters.</li>\n<li><strong>Parallel-In Parallel-Out (PIPO):</strong> Universal high-speed buffer register. Loads and reads $n$ bits simultaneously in a single clock cycle.</li>\n</ol>\n\n<h4>2. The Universal Bidirectional Shift Register</h4>\n<p>A 4-bit Universal Shift Register (e.g., standard 74HC194 IC) incorporates four 4-to-1 multiplexers at the inputs of each D flip-flop, controlled by two mode select lines $(S_1, S_0)$:</p>\n<ul>\n<li>$S_1 S_0 = 00$: <strong>Hold / No Change</strong> ($D_i = Q_i$).</li>\n<li>$S_1 S_0 = 01$: <strong>Shift Right</strong> ($D_i = Q_{i-1}$, with $D_3 = \\text{Serial Input Right}$).</li>\n<li>$S_1 S_0 = 10$: <strong>Shift Left</strong> ($D_i = Q_{i+1}$, with $D_0 = \\text{Serial Input Left}$).</li>\n<li>$S_1 S_0 = 11$: <strong>Parallel Load</strong> ($D_i = I_i$).</li>\n</ul>\n\n<h4>3. Cyclic Shift Counters: Ring & Johnson Counters</h4>\n<ol>\n<li><strong>Ring Counter:</strong> Formed by circulating the serial output of the final stage directly back into the serial input of the first stage ($D_0 = Q_{n-1}$):\n<div class=\"math-display\">\n$$\\text{Initial State: } 1000_2 \\longrightarrow 0100_2 \\longrightarrow 0010_2 \\longrightarrow 0001_2 \\longrightarrow 1000_2$$\n</div>\nA single circulating '1' decodes directly into $n$ mutually exclusive timing pulses with <strong>zero decoding gates</strong>, but utilizes only $n$ states out of $2^n$ available states ($MOD = n$).</li>\n<li><strong>Johnson (Twisted Ring / Moebius) Counter:</strong> Formed by feeding back the <em>inverted</em> output of the final stage into the first stage ($D_0 = \\bar{Q}_{n-1}$):\n<div class=\"math-display\">\n$$\\text{States: } 0000 \\to 1000 \\to 1100 \\to 1110 \\to 1111 \\to 0111 \\to 0011 \\to 0001 \\to 0000$$\n</div>\nAn $n$-stage Johnson counter produces $2n$ states ($MOD = 2n$). Adjacent states differ by only a single bit (unit distance), enabling completely glitch-free decoding with simple 2-input AND gates.</li>\n</ol>"
        },
        {
          "id": "dig-5-4",
          "title": "Decoders, Encoders & BCD-to-7-Segment Display Drivers",
          "content": "<h4>1. Binary Decoders</h4>\n<p>A <strong>decoder</strong> is an MSI combinational circuit with $n$ input lines and up to $2^n$ unique output lines. It decodes an $n$-bit binary input code by activating exactly one output line corresponding to that input minterm:</p>\n<ul>\n<li><strong>3-to-8 Line Decoder (74138 IC):</strong> Three inputs $(A_2, A_1, A_0)$ select one of 8 active-LOW outputs ($\\bar{Y}_0$ through $\\bar{Y}_7$). Contains active-LOW enable inputs ($\\bar{E}_1, \\bar{E}_2, E_3$) used to cascade multiple decoders into large memory address decoding trees.</li>\n<li><strong>Universal Logic Realization:</strong> Because each output of an active-LOW decoder produces an individual minterm $\\bar{m}_i = \\overline{A B C}$, any arbitrary Boolean function in SOP form can be implemented simply by feeding the appropriate decoder outputs into an external NAND gate (since $\\overline{\\bar{m}_1 \\cdot \\bar{m}_4} = m_1 + m_4$).</li>\n</ul>\n\n<h4>2. Encoders & Priority Encoders</h4>\n<p>An <strong>encoder</strong> performs the inverse operation: it accepts $2^n$ input lines (where only one line is asserted at any time) and outputs an $n$-bit binary code. If multiple inputs can be asserted simultaneously, standard encoders fail.</p>\n<p>A <strong>Priority Encoder (e.g., 74148 IC)</strong> resolves input contention by asserting the binary code of the <strong>highest-priority active input</strong>, ignoring all lower-priority inputs. It also generates an active Group Select ($GS$) signal indicating whether any valid input is active, forming the foundation of CPU interrupt request (IRQ) controllers.</p>\n\n<h4>3. BCD-to-7-Segment Display Drivers (7447 IC)</h4>\n<p>Drives numerical LED/LCD displays containing seven planar segments labeled $a, b, c, d, e, f, g$. Translates 4-bit BCD input $(D, C, B, A)$ into 7 segment drive signals. For common-anode LED displays, the 7447 provides open-collector active-LOW outputs ($a=0$ lights the segment), incorporating lamp test ($LT$) and automatic zero-blanking inputs ($RBI, RBO$).</p>"
        },
        {
          "id": "dig-5-5",
          "title": "Multiplexers (MUX) & Demultiplexers (DEMUX)",
          "content": "<h4>1. Multiplexers (Data Selectors)</h4>\n<p>A <strong>Multiplexer (MUX)</strong> is a combinational switching subsystem that directs binary information from one of $2^n$ data input channels ($I_0, I_1, \\dots, I_{2^n-1}$) to a single output line $Y$, selected by $n$ control select lines ($S_{n-1}, \\dots, S_0$):</p>\n<div class=\"math-display\">\n$$Y = \\sum_{k=0}^{2^n-1} m_k(S) \\cdot I_k = \\bar{S}_1 \\bar{S}_0 I_0 + \\bar{S}_1 S_0 I_1 + S_1 \\bar{S}_0 I_2 + S_1 S_0 I_3 \\quad (\\text{4-to-1 MUX})$$\n</div>\n\n<h4>2. Implementing Arbitrary Logic Functions Using Multiplexers</h4>\n<p>A $2^n$-to-1 multiplexer can implement <strong>any arbitrary Boolean function of $n+1$ variables</strong> without requiring any external logic gates:</p>\n<ol>\n<li>Assign $n$ variables to the MUX select lines $(S_{n-1}, \\dots, S_0)$.</li>\n<li>Express the remaining $(n+1)$-th variable $Z$ as the data input $I_k$ for each select combination. For each minterm pair, $I_k$ will evaluate to either $0$, $1$, $Z$, or $\\bar{Z}$.</li>\n</ol>\n<p>Multiplexers thus function as universal, software-configurable look-up tables (LUTs), forming the core logic fabric of modern Field-Programmable Gate Arrays (FPGAs).</p>\n\n<h4>3. Demultiplexers (DEMUX)</h4>\n<p>A <strong>Demultiplexer</strong> takes a single data input line and routes it to one of $2^n$ output lines selected by $n$ address lines. A binary decoder with an enable input is functionally identical to a demultiplexer (the enable acts as the serial data input).</p>"
        }
      ],
      "problems": [
        {
          "id": "dig-p-5-1",
          "title": "Design of a Synchronous MOD-6 Counter Using JK Flip-Flops",
          "statement": "Design a synchronous counter that counts through the cyclic sequence: $0 \\to 1 \\to 2 \\to 3 \\to 4 \\to 5 \\to 0$ using three JK flip-flops ($Q_2, Q_1, Q_0$). (a) Construct the state transition table and list the required $J$ and $K$ excitations for all three flip-flops. (b) Derive the minimal Boolean excitation equations using 3-variable K-maps. (c) Analyze the unused states $6$ ($110_2$) and $7$ ($111_2$) and verify whether the counter is self-correcting (lockout-free).",
          "steps": [
            {
              "stepName": "Step 1: Construct the State Transition & Excitation Table",
              "math": "\\begin{matrix} Q_2 Q_1 Q_0 & Q_2^+ Q_1^+ Q_0^+ & J_2 & K_2 & J_1 & K_1 & J_0 & K_0 \\\\ \\hline 000 & 001 & 0 & \\times & 0 & \\times & 1 & \\times \\\\ 001 & 010 & 0 & \\times & 1 & \\times & \\times & 1 \\\\ 010 & 011 & 0 & \\times & \\times & 0 & 1 & \\times \\\\ 011 & 100 & 1 & \\times & \\times & 1 & \\times & 1 \\\\ 100 & 101 & \\times & 0 & 0 & \\times & 1 & \\times \\\\ 101 & 000 & \\times & 1 & 0 & \\times & \\times & 1 \\end{matrix}",
              "explanation": "Map valid transitions (0 to 5) to JK excitation rules: 0->0: (0,x); 0->1: (1,x); 1->0: (x,1); 1->1: (x,0)."
            },
            {
              "stepName": "Step 2: Derive Minimized K-Map Equations for Flip-Flop 0",
              "math": "J_0: \\text{cells } 0, 2, 4 = 1; \\ 1, 3, 5 = \\times \\implies J_0 = 1. \\quad K_0: \\text{cells } 1, 3, 5 = 1; \\ 0, 2, 4 = \\times \\implies K_0 = 1",
              "explanation": "Flip-flop 0 toggles on every single clock pulse: J0 = 1, K0 = 1."
            },
            {
              "stepName": "Step 3: Derive Equations for Flip-Flop 1 and Flip-Flop 2",
              "math": "J_1 = \\bar{Q}_2 Q_0, \\quad K_1 = Q_0. \\qquad J_2 = Q_1 Q_0, \\quad K_2 = Q_0",
              "explanation": "Plot K-maps with unused states 6 and 7 as Don't Cares (x)."
            },
            {
              "stepName": "Step 4: Lockout Analysis for Unused State 6 (110)",
              "math": "\\text{For } Q = 110_2: J_2 = 0, K_2 = 0 \\implies Q_2^+=1; \\quad J_1 = 0, K_1 = 0 \\implies Q_1^+=1; \\quad J_0=1, K_0=1 \\implies Q_0^+=1 \\implies 110 \\to 111",
              "explanation": "State 6 transitions to State 7 on next clock pulse."
            },
            {
              "stepName": "Step 5: Lockout Analysis for Unused State 7 (111)",
              "math": "\\text{For } Q = 111_2: J_2=1, K_2=1 \\implies Q_2^+=0; \\quad J_1=0, K_1=1 \\implies Q_1^+=0; \\quad J_0=1, K_0=1 \\implies Q_0^+=0 \\implies 111 \\to 000!",
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
              "math": "Q^{(0)} = 1010_2",
              "explanation": "Register holds 1010."
            },
            {
              "stepName": "Step 2: Clock Pulse 1 - Shift Right (S1 S0 = 01)",
              "math": "\\text{Bits shift right: } Q_3 \\leftarrow SIR = 1, \\quad Q_2 \\leftarrow Q_3 = 1, \\quad Q_1 \\leftarrow Q_2 = 0, \\quad Q_0 \\leftarrow Q_1 = 1 \\implies Q^{(1)} = 1101_2",
              "explanation": "Previous LSB (0) is shifted out and lost; SIR=1 shifts into MSB."
            },
            {
              "stepName": "Step 3: Clock Pulse 2 - Shift Left (S1 S0 = 10)",
              "math": "\\text{Bits shift left: } Q_3 \\leftarrow Q_2 = 1, \\quad Q_2 \\leftarrow Q_1 = 0, \\quad Q_1 \\leftarrow Q_0 = 1, \\quad Q_0 \\leftarrow SIL = 0 \\implies Q^{(2)} = 1010_2",
              "explanation": "Previous MSB (1) is shifted out; SIL=0 shifts into LSB."
            },
            {
              "stepName": "Step 4: Clock Pulse 3 - Parallel Load (S1 S0 = 11)",
              "math": "Q \\leftarrow I \\implies Q^{(3)} = 1100_2",
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
              "math": "\\begin{matrix} \\text{Select } ABC & \\text{Minterm } D=0 & \\text{Minterm } D=1 & \\text{Required } I_k \\\\ \\hline 000 \\ (0) & m_0 (0) & m_1 (1) & I_0 = D \\\\ 001 \\ (1) & m_2 (0) & m_3 (1) & I_1 = D \\\\ 010 \\ (2) & m_4 (1) & m_5 (0) & I_2 = \\bar{D} \\\\ 011 \\ (3) & m_6 (0) & m_7 (0) & I_3 = 0 \\\\ 100 \\ (4) & m_8 (0) & m_9 (0) & I_4 = 0 \\\\ 101 \\ (5) & m_{10} (0) & m_{11} (1) & I_5 = D \\\\ 110 \\ (6) & m_{12} (1) & m_{13} (1) & I_6 = 1 \\\\ 111 \\ (7) & m_{14} (1) & m_{15} (1) & I_7 = 1 \\end{matrix}",
              "explanation": "Group minterms in pairs of D=0 and D=1 for each select combination."
            },
            {
              "stepName": "Step 2: Evaluate Each Data Line",
              "math": "I_0 = D, \\quad I_1 = D, \\quad I_2 = \\bar{D}, \\quad I_3 = 0, \\quad I_4 = 0, \\quad I_5 = D, \\quad I_6 = 1, \\quad I_7 = 1",
              "explanation": "If only D=1 is in minterm list: I_k = D. If both are 1: I_k = 1. If only D=0 is 1: I_k = D_bar. If neither: I_k = 0."
            },
            {
              "stepName": "Step 3: Hardware Implementation",
              "math": "S_2 = A, \\ S_1 = B, \\ S_0 = C; \\quad I_0, I_1, I_5 \\leftarrow D; \\quad I_2 \\leftarrow \\bar{D}; \\quad I_3, I_4 \\leftarrow \\text{GND}; \\quad I_6, I_7 \\leftarrow V_{CC}",
              "explanation": "A single 8-to-1 MUX and one inverter for D_bar implements the complete 4-variable function."
            }
          ],
          "answer": "S_2=A, S_1=B, S_0=C; \\quad I_0=I_1=I_5=D, \\ I_2=\\bar{D}, \\ I_3=I_4=0, \\ I_6=I_7=1"
        }
      ]
    },
    {
      "unitNumber": 6,
      "unitId": "unit6-data-converters-dac-adc",
      "title": "Data Conversion Systems: Digital-to-Analog & Analog-to-Digital",
      "description": "Theory, precision architectures, and error metrics of mixed-signal data converters: binary-weighted resistor DACs and operational amplifier virtual ground summing; R-2R ladder networks, Thevenin equivalent analysis, and constant input impedance; DAC resolution, monotonicity, settling time, differential non-linearity (DNL), and integral non-linearity (INL); Flash (simultaneous comparator) ADCs, priority decoding, and comparator count scaling; tracking ADCs, Successive Approximation Register (SAR) binary search algorithms; Dual-Slope integrating ADCs, line-frequency noise rejection, and Delta-Sigma oversampling modulation.",
      "sections": [
        {
          "id": "dig-6-1",
          "title": "D/A Conversion: Binary-Weighted Resistors & Virtual Ground",
          "content": "<h4>1. Digital-to-Analog Converter (DAC) Operational Concept</h4>\n<p>A <strong>Digital-to-Analog Converter (DAC)</strong> translates an $N$-bit digital binary word $D = b_{N-1} b_{N-2} \\dots b_0$ into an equivalent proportional analog output voltage $V_{\\text{out}}$ or current $I_{\\text{out}}$:</p>\n<div class=\"math-display\">\n$$V_{\\text{out}} = V_{\\text{ref}} \\sum_{i=0}^{N-1} b_i 2^{i - N} = \\frac{V_{\\text{ref}}}{2^N} \\left( b_{N-1} 2^{N-1} + b_{N-2} 2^{N-2} + \\dots + b_0 2^0 \\right)$$\n</div>\n<p>where $V_{\\text{ref}}$ is a precision voltage reference, and $\\frac{V_{\\text{ref}}}{2^N}$ defines the <strong>analog step size or resolution (1 LSB)</strong>.</p>\n\n<h4>2. The Binary-Weighted Resistor DAC</h4>\n<p>Constructed by connecting weighted resistors $R, 2R, 4R, \\dots, 2^{N-1}R$ to the inverting summing junction of an operational amplifier. Binary switches connect resistor $i$ to $-V_{\\text{ref}}$ when bit $b_i = 1$, or to ground when $b_i = 0$:</p>\n<div class=\"math-display\">\n$$I_{\\text{sum}} = \\sum_{i=0}^{N-1} b_i \\frac{V_{\\text{ref}}}{2^{N-1-i} R}$$\n</div>\n<p>Because the inverting op-amp terminal is held at virtual ground ($0\\text{ V}$), the output voltage is:</p>\n<div class=\"math-display\">\n$$V_{\\text{out}} = I_{\\text{sum}} R_f = V_{\\text{ref}} \\frac{R_f}{R} \\left( \\frac{b_{N-1}}{2^1} + \\frac{b_{N-2}}{2^2} + \\dots + \\frac{b_0}{2^N} \\right)$$\n</div>\n\n<h4>3. Physical Limitations of Binary-Weighted Networks</h4>\n<p>While conceptually elegant, binary-weighted DACs are severely impractical for high resolutions ($N \\ge 8$):</p>\n<ul>\n<li><strong>Extreme Resistance Spread:</strong> For a 16-bit DAC with $R = 10\\text{ k}\\Omega$, the LSB resistor must be $2^{15} R = 327.68\\text{ M}\\Omega$—a ratio exceeding $32,000 : 1$.</li>\n<li><strong>Impossibility of Monolithic Integration:</strong> Fabricating resistors spanning four orders of magnitude on a single silicon die with sub-$0.01\\%$ thermal tracking is technologically impossible.</li>\n</ul>"
        },
        {
          "id": "dig-6-2",
          "title": "The R-2R Ladder Network DAC: Thevenin Analysis & Symmetry",
          "simulation": "dig-r2r-dac-sim",
          "content": "<h4>1. The R-2R Ladder Architecture</h4>\n<p>Bernard Lippel (1953) resolved the resistance spread bottleneck with the ingenious <strong>$R$-$2R$ ladder network</strong>, which utilizes <strong>only two precision resistance values</strong>—$R$ and $2R$—regardless of the bit resolution $N$.</p>\n\n<h4>2. Thevenin Equivalent & Constant Input Impedance Proof</h4>\n<p>Looking into any node of an $R$-$2R$ ladder toward the terminated end, the equivalent resistance is identically <strong>$R$</strong>:</p>\n<ol>\n<li>At the termination end, two parallel $2R$ resistors combine to yield $2R \\parallel 2R = R$.</li>\n<li>Adding the series resistor $R$ gives $R + R = 2R$.</li>\n<li>At the next node, this $2R$ is in parallel with that stage's vertical $2R$ branch: $2R \\parallel 2R = R$.</li>\n</ol>\n<p>By mathematical induction, this perfect binary current division repeats identically across all $N$ stages. At each ladder node, the injected current splits into two equal halves ($50\\% / 50\\%$).</p>\n\n<h4>3. Inverted R-2R Current-Steering DAC</h4>\n<p>In modern monolithic CMOS DACs, the ladder is operated in the <strong>current-steering mode</strong>: the vertical $2R$ branches terminate in SPDT CMOS switches that steer currents either into the op-amp virtual ground ($I_{\\text{out}}$) or into circuit analog ground ($I_{\\text{out2}}$):</p>\n<div class=\"math-display\">\n$$V_{\\text{out}} = - V_{\\text{ref}} \\left( \\frac{R_f}{R} \\right) \\sum_{i=0}^{N-1} b_i 2^{i - N}$$\n</div>\n<p>Key Engineering Advantages:</p>\n<ul>\n<li>Only two resistor values ($R$ and $2R$, typically $10\\text{ k}\\Omega$ and $20\\text{ k}\\Omega$), manufactured by laser-trimmed thin-film SiCr or polysilicon with perfect thermal tracking ($< 1\\text{ ppm/}^\\circ\\text{C}$).</li>\n<li>All nodes remain at fixed potentials ($0\\text{ V}$), eliminating parasitic capacitance charging delays and achieving sub-nanosecond settling times.</li>\n</ul>"
        },
        {
          "id": "dig-6-3",
          "title": "DAC Performance Metrics: Resolution, Settling Time & Linearity",
          "content": "<h4>1. DAC Resolution & Full-Scale Range (FSR)</h4>\n<p>The <strong>resolution</strong> of an $N$-bit DAC is the smallest output voltage increment it can resolve, equal to the weight of 1 LSB:</p>\n<div class=\"math-display\">\n$$V_{\\text{LSB}} = \\frac{V_{\\text{FSR}}}{2^N - 1} \\quad (\\text{or } \\frac{V_{\\text{ref}}}{2^N})$$\n</div>\n<p>The maximum analog output, attained when all bits are 1 ($11\\dots1_2$), is strictly 1 LSB below full reference:</p>\n<div class=\"math-display\">\n$$V_{\\text{out, max}} = V_{\\text{ref}} \\left( 1 - \\frac{1}{2^N} \\right)$$\n</div>\n\n<h4>2. Dynamic Metrics: Settling Time & Glitch Impulse</h4>\n<ul>\n<li><strong>Settling Time ($t_s$):</strong> The elapsed time from the application of an input digital transition until the analog output settles and remains within a specified error band (typically $\\pm \\frac{1}{2}\\text{ LSB}$) of its final value. Governed by op-amp slew rate and $RC$ time constants.</li>\n<li><strong>Major Carry Glitch Impulse:</strong> When transitioning across mid-scale ($0111\\dots1 \\to 1000\\dots0$), switch timing skews cause temporary false intermediate states ($1111\\dots1$ or $0000\\dots0$), ejecting massive voltage spikes (glitch area in $\\text{pV}\\cdot\\text{s}$) into audio/video signals.</li>\n</ul>\n\n<h4>3. Static Accuracy: Non-Linearity Metrics (INL & DNL)</h4>\n<ul>\n<li><strong>Differential Non-Linearity (DNL):</strong> The difference between the actual step height between adjacent codes and the ideal step height ($1\\text{ LSB}$):\n<div class=\"math-display\">\n$$\\text{DNL}(k) = \\frac{V_{\\text{out}}(k) - V_{\\text{out}}(k-1) - V_{\\text{LSB}}}{V_{\\text{LSB}}}$$\n</div>\nIf $\\text{DNL} < -1\\text{ LSB}$, the transfer function reverses direction, creating a <strong>non-monotonic DAC</strong>.</li>\n<li><strong>Integral Non-Linearity (INL):</strong> The maximum deviation of the actual analog transfer curve from the ideal straight line across the entire range.</li>\n</ul>"
        },
        {
          "id": "dig-6-4",
          "title": "Fast Flash (Simultaneous Comparator) ADCs",
          "simulation": "dig-flash-sar-adc-sim",
          "content": "<h4>1. Operational Architecture of the Flash ADC</h4>\n<p>An <strong>Analog-to-Digital Converter (ADC)</strong> quantizes a continuous analog input voltage $V_{\\text{in}}$ into a discrete digital code. The <strong>Flash (Parallel) ADC</strong> is the fastest known data conversion architecture, completing conversion in a single clock cycle ($t_{\\text{conv}} < 1\\text{ ns}$, gigasample/second speeds).</p>\n\n<h4>2. Circuit Topology</h4>\n<p>An $N$-bit Flash ADC consists of:</p>\n<ol>\n<li><strong>Precision Resistor Ladder:</strong> A string of $2^N$ matched resistors $R$ connected between $V_{\\text{ref}}$ and ground, establishing $2^N - 1$ equally spaced reference voltage taps:\n<div class=\"math-display\">\n$$V_k = \\frac{k - 0.5}{2^N} V_{\\text{ref}} \\quad (k = 1, 2, \\dots, 2^N - 1)$$\n</div></li>\n<li><strong>Comparator Bank:</strong> Exactly $2^N - 1$ analog comparators operating in parallel. Each comparator compares $V_{\\text{in}}$ to its respective reference tap $V_k$. All comparators below $V_{\\text{in}}$ output 1; all above output 0, producing a <strong>Thermometer Code</strong> of height proportional to $V_{\\text{in}}$.</li>\n<li><strong>Priority Decoder:</strong> Converts the $(2^N - 1)$-bit thermometer code into an $N$-bit binary output word in a single gate delay.</li>\n</ol>\n\n<h4>3. Flash ADC Trade-Offs & Scaling Wall</h4>\n<p>The monumental speed of Flash ADCs is offset by exponential hardware growth:</p>\n<div class=\"math-display\">\n$$\\text{Number of Comparators} = 2^N - 1$$\n</div>\n<ul>\n<li>For $N = 2$ bits: $2^2 - 1 = 3$ comparators.</li>\n<li>For $N = 3$ bits: $2^3 - 1 = 7$ comparators.</li>\n<li>For $N = 8$ bits: $2^8 - 1 = 255$ comparators (practical limit for standalone flash).</li>\n<li>For $N = 16$ bits: $2^{16} - 1 = 65,535$ precision comparators on a single chip—consuming excessive silicon area and hundreds of watts of power. High resolutions require alternative multi-step architectures.</li>\n</ul>"
        },
        {
          "id": "dig-6-5",
          "title": "Tracking, SAR & Dual-Slope Integrating ADCs",
          "content": "<h4>1. Successive Approximation Register (SAR) ADCs</h4>\n<p>The <strong>SAR ADC</strong> is the industry workhorse for medium-to-high resolution ($10 - 18\\text{ bits}$) at sample rates up to several megasamples per second. It utilizes a feedback loop containing a DAC, a single comparator, and a digital SAR control engine executing a <strong>binary search algorithm</strong>:</p>\n<ol>\n<li>Clock Cycle 1: SAR sets MSB to 1 ($1000\\dots_2$), prompting internal DAC to output mid-scale $V_{\\text{DAC}} = V_{\\text{ref}} / 2$.</li>\n<li>Comparator tests if $V_{\\text{in}} > V_{\\text{DAC}}$. If yes, MSB is retained as 1; if no, MSB is cleared to 0.</li>\n<li>Clock Cycle 2: SAR sets next bit ($b_{N-2}$) to 1, tests against $V_{\\text{in}}$, and retains or clears it.</li>\n<li>The process repeats bit-by-bit until the LSB is resolved.</li>\n</ol>\n<p>An $N$-bit SAR ADC requires exactly <strong>$N$ clock cycles</strong> per conversion ($t_{\\text{conv}} = N \\cdot T_{\\text{clk}}$), requiring only <strong>one comparator</strong> regardless of resolution.</p>\n\n<h4>2. Dual-Slope Integrating ADC</h4>\n<p>The premier architecture for high-precision digital multimeters (DMMs) where ultra-high accuracy and noise immunity outweigh conversion speed ($10 - 100\\text{ conversions/sec}$):</p>\n<ol>\n<li><strong>Run-Up Phase ($T_1$, Fixed Time):</strong> An analog integrator integrates input voltage $V_{\\text{in}}$ for a fixed time interval $T_1 = 2^N T_{\\text{clk}}$:\n<div class=\"math-display\">\n$$V_{\\text{peak}} = - \\frac{1}{R C} \\int_0^{T_1} V_{\\text{in}} dt = - \\frac{V_{\\text{in}} T_1}{R C}$$\n</div></li>\n<li><strong>Run-Down Phase ($T_2$, Measured Time):</strong> Integrator switches to precision negative reference $-V_{\\text{ref}}$ and discharges back to zero at a constant slope:\n<div class=\"math-display\">\n$$0 = V_{\\text{peak}} + \\frac{V_{\\text{ref}} T_2}{R C} \\implies \\frac{V_{\\text{in}} T_1}{R C} = \\frac{V_{\\text{ref}} T_2}{R C}$$\n</div>\n<div class=\"math-display\">\n$$T_2 = T_1 \\left( \\frac{V_{\\text{in}}}{V_{\\text{ref}}} \\right)$$\n</div></li>\n</ol>\n<p><strong>Monumental Advantage:</strong> Both $R$ and $C$ cancel out completely from the equation! Variations in resistor values, capacitor aging, and clock oscillator drift have <strong>zero effect</strong> on measurement accuracy. Setting $T_1 = 20\\text{ ms}$ ($1/50\\text{ Hz}$) provides infinite rejection of AC power line hum.</p>"
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
              "math": "V_{\\text{LSB}} = \\frac{V_{\\text{ref}}}{2^N} \\left(\\frac{R_f}{R}\\right) = \\frac{10.0\\text{ V}}{2^4} \\left(\\frac{20\\text{ k}\\Omega}{10\\text{ k}\\Omega}\\right) = \\frac{10.0}{16} \\times 2 = \\frac{20.0}{16}\\text{ V} = 1.250\\text{ V}",
              "explanation": "Compute voltage equivalent of one LSB."
            },
            {
              "stepName": "Step 2: Determine Full-Scale Output Voltage",
              "math": "V_{\\text{out, max}} = V_{\\text{LSB}} \\times (2^N - 1) = 1.250\\text{ V} \\times (16 - 1) = 1.250 \\times 15 = 18.750\\text{ V}",
              "explanation": "Full-scale output occurs when all bits are 1 (code 1111)."
            },
            {
              "stepName": "Step 3: Evaluate Output for Input Code 1011",
              "math": "D = (1011)_2 = 1 \\times 2^3 + 0 \\times 2^2 + 1 \\times 2^1 + 1 \\times 2^0 = 8 + 2 + 1 = 11_{10}",
              "explanation": "Convert digital input code to decimal."
            },
            {
              "stepName": "Step 4: Compute Final Output Voltage",
              "math": "V_{\\text{out}} = 11 \\times V_{\\text{LSB}} = 11 \\times 1.250\\text{ V} = 13.750\\text{ V}",
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
              "math": "N = 3 \\implies N_{\\text{comparators}} = 2^N - 1 = 2^3 - 1 = 7 \\text{ comparators}; \\quad N_{\\text{resistors}} = 2^3 = 8 \\text{ matched resistors}",
              "explanation": "A 3-bit flash ADC requires 7 comparators and 8 resistors."
            },
            {
              "stepName": "Step 2: Determine Step Size and Comparator Reference Taps",
              "math": "V_{\\text{step}} = \\frac{V_{\\text{ref}}}{8} = \\frac{8.00\\text{ V}}{8} = 1.00\\text{ V}. \\implies V_1=1.0\\text{V}, \\ V_2=2.0\\text{V}, \\ V_3=3.0\\text{V}, \\ V_4=4.0\\text{V}, \\ V_5=5.0\\text{V}, \\ V_6=6.0\\text{V}, \\ V_7=7.0\\text{V}",
              "explanation": "List all 7 threshold tap voltages."
            },
            {
              "stepName": "Step 3: Evaluate Comparator Outputs for Vin = 5.20 V",
              "math": "5.20\\text{ V} > V_1, V_2, V_3, V_4, V_5 \\ (1.0 - 5.0\\text{ V}) \\implies C_1 = C_2 = C_3 = C_4 = C_5 = 1; \\quad 5.20\\text{ V} < V_6, V_7 \\implies C_6 = C_7 = 0",
              "explanation": "Comparators 1 through 5 output 1; comparators 6 and 7 output 0."
            },
            {
              "stepName": "Step 4: Form Thermometer Code and Priority Binary Output",
              "math": "\\text{Thermometer Code: } (C_7 C_6 C_5 C_4 C_3 C_2 C_1) = 0011111_2. \\implies \\text{Priority Encoder Output: } (101)_2 = 5_{10}",
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
              "math": "T_1 = \\frac{1}{50.0\\text{ Hz}} = 20.0\\text{ ms} = 0.020\\text{ s}. \\implies N_1 = T_1 \\cdot f_{\\text{clk}} = 0.020\\text{ s} \\times 200,000\\text{ Hz} = 4000 \\text{ clock counts}",
              "explanation": "Integrating over exactly one period (4000 counts) causes net sinusoidal AC noise integral to vanish identically."
            },
            {
              "stepName": "Step 2: Calculate Measured Input Voltage Using Dual-Slope Equation",
              "math": "V_{\\text{in}} = V_{\\text{ref}} \\left( \\frac{T_2}{T_1} \\right) = 2.000\\text{ V} \\times \\left( \\frac{12.80\\text{ ms}}{20.00\\text{ ms}} \\right) = 2.000 \\times 0.640 = 1.280\\text{ V}",
              "explanation": "Evaluate input voltage: exactly 1.280 V."
            },
            {
              "stepName": "Step 3: Verification of Independence from Component Values",
              "math": "\\text{Notice that } R, C, \\text{ and } f_{\\text{clk}} \\text{ canceled completely in } V_{\\text{in}} = V_{\\text{ref}} (N_2 / N_1) = 2.000 \\times (2560 / 4000) = 1.280\\text{ V}",
              "explanation": "The measurement is completely immune to RC component tolerances."
            }
          ],
          "answer": "N_1 = 4000 \\text{ counts } (T_1 = 20.0\\text{ ms}), \\quad V_{\\text{in}} = 1.280\\text{ V} \\quad (\\text{Infinite 50 Hz Hum Rejection})"
        }
      ]
    },
    {
      "unitNumber": 7,
      "unitId": "unit7-semiconductor-memory",
      "title": "Semiconductor Memory Architectures: SRAM, DRAM & Non-Volatile",
      "description": "Solid-state digital data storage architectures and device physics: memory organization, word length, bit capacity, 2D/3D matrix addressing, row/column address strobes (RAS/CAS); Static RAM (SRAM) 6-transistor (6T) CMOS bistable cell, precharge lines, read/write stability, and differential sense amplifiers; Dynamic RAM (DRAM) 1-transistor 1-capacitor (1T-1C) trench/stacked cell, destructive readout, capacitive leakage, and periodic refresh scheduling; Non-volatile memory technologies: Mask ROM, fuse PROM, UV-erasable EPROM, floating-gate tunneling EEPROM, and multi-level cell NAND/NOR Flash; SDRAM, DDR protocols, and multi-level cache memory hierarchy.",
      "sections": [
        {
          "id": "dig-7-1",
          "title": "Memory Organization, Matrix Addressing & Decoders",
          "content": "<h4>1. General Memory Architecture & Density Classification</h4>\n<p>A digital semiconductor memory stores binary data in a regular two-dimensional grid of binary memory cells. The overall storage capacity is expressed as:</p>\n<div class=\"math-display\">\n$$\\text{Capacity} = M \\times N \\quad (M \\text{ words, each of } N \\text{ bits})$$\n</div>\n<p>To access an individual word among $M = 2^k$ addressable locations, the memory requires $k$ binary address input lines ($A_{k-1}, \\dots, A_0$). For example, a $64\\text{ K} \\times 8$ memory chip possesses $2^{16} = 65,536$ words of 8 bits each, requiring $k = 16$ address lines, 8 bidirectional data lines ($D_7 - D_0$), and control lines: Chip Select ($\\overline{CS}$), Output Enable ($\\overline{OE}$), and Write Enable ($\\overline{WE}$).</p>\n\n<h4>2. 2D Matrix Addressing & Row/Column Decoders</h4>\n<p>If $2^k$ words were laid out in a single linear column, the required address decoder would have $2^k$ output lines—requiring an astronomical number of gates ($65,536$ outputs for $k=16$). To achieve high physical density and compact square silicon layouts, memory arrays utilize <strong>2D Matrix Coincident Addressing</strong>:</p>\n<ol>\n<li>The $k$ address bits are split into $r$ Row Address bits and $c$ Column Address bits ($k = r + c$).</li>\n<li>The <strong>Row Decoder</strong> activates exactly one horizontal <strong>Word-Line (WL)</strong> among $2^r$ rows, simultaneously enabling all $2^c$ storage cells along that row.</li>\n<li>The activated cells place their stored charges onto vertical <strong>Bit-Lines (BL)</strong>.</li>\n<li>The <strong>Column Decoder</strong> controls a bank of column pass-gates (multiplexers) that route the selected bit-line data to the chip's output buffers.</li>\n</ol>\n<p>A $64\\text{ K}$-bit array arranged as a $256 \\times 256$ matrix requires only one 8-to-256 row decoder and one 8-to-256 column decoder (512 total outputs instead of 65,536).</p>"
        },
        {
          "id": "dig-7-2",
          "title": "Static RAM (SRAM): The 6T CMOS Memory Cell",
          "simulation": "dig-sram-cell-sim",
          "content": "<h4>1. Structure of the 6-Transistor (6T) CMOS SRAM Cell</h4>\n<p>Static RAM (SRAM) retains stored data indefinitely as long as DC power is maintained ($V_{DD} > 0$), without requiring periodic refresh cycles. The canonical <strong>6T CMOS SRAM cell</strong> comprises:</p>\n<ul>\n<li>Two cross-coupled CMOS inverters ($M_1, M_2, M_3, M_4$) forming a bistable latch with complementary internal storage nodes $Q$ and $\\bar{Q}$.</li>\n<li>Two nMOS access pass-transistors ($M_5, M_6$) connecting nodes $Q$ and $\\bar{Q}$ to complementary bit-lines ($BL$ and $\\overline{BL}$), gated by Word-Line ($WL$).</li>\n</ul>\n\n<h4>2. Operational Cycles of the 6T Cell</h4>\n<ol>\n<li><strong>Read Cycle:</strong>\n<ol>\n<li>Precharge phase: Both $BL$ and $\\overline{BL}$ are precharged to $V_{DD}$ (or $V_{DD}/2$) and then floated.</li>\n<li>Assertion phase: Word-line $WL$ is driven HIGH, turning on access transistors $M_5$ and $M_6$.</li>\n<li>Discharge phase: If $Q=0$ and $\\bar{Q}=1$, node $Q$ discharges $BL$ through pull-down transistor $M_1$, creating a differential voltage swing $\\Delta V = V_{BLB} - V_{BL} \\approx 100 - 200\\text{ mV}$.</li>\n<li>Sensing phase: A sensitive analog <strong>differential sense amplifier</strong> strobes, detecting $\\Delta V$ and amplifying it rapidly to full CMOS logic levels ($0\\text{ V}$ or $V_{DD}$).</li>\n</ol></li>\n<li><strong>Write Cycle:</strong>\n<ol>\n<li>Strong write drivers overdrive $BL$ and $\\overline{BL}$ to opposite supply rails (e.g., $BL = 0\\text{ V}, \\overline{BL} = V_{DD}$ to write a 0).</li>\n<li>$WL$ is asserted HIGH. The strong pull-down on $BL$ overpowers the weaker internal pMOS pull-up transistor, flipping the cross-coupled latch into the new state.</li>\n</ol></li>\n</ol>\n<p><strong>Cell Sizing (Read Stability & Write Margin):</strong> To prevent the cell from accidentally flipping its state during a read operation (read disturbance), pull-down transistors $M_1, M_3$ must be made stronger than access transistors $M_5, M_6$ ($\\beta_{\\text{pull-down}} / \\beta_{\\text{access}} \\ge 1.2 - 1.5$). Conversely, to ensure data can be written successfully, access transistors must be stronger than pull-up transistors $M_2, M_4$ ($\\beta_{\\text{access}} / \\beta_{\\text{pull-up}} \\ge 1.0$).</p>"
        },
        {
          "id": "dig-7-3",
          "title": "Dynamic RAM (DRAM): The 1T-1C Cell & Refresh Scheduling",
          "simulation": "dig-dram-refresh-sim",
          "content": "<h4>1. The 1-Transistor 1-Capacitor (1T-1C) DRAM Cell</h4>\n<p>Robert Dennard (IBM, 1968) patented the <strong>1T-1C DRAM cell</strong>, which slashed silicon area from 6 transistors down to a single access transistor $M$ and an integrated storage capacitor $C_s$ ($C_s \\approx 25 - 35\\text{ fF}$):</p>\n<ul>\n<li>Logic '1' is stored as a packet of charge on $C_s$ ($V_C \\approx V_{DD}$).</li>\n<li>Logic '0' is stored as discharged state ($V_C \\approx 0\\text{ V}$).</li>\n</ul>\n<p>Because the cell area is minuscule ($4F^2 - 6F^2$, where $F$ is the lithographic feature size), DRAM achieves gigabit storage densities orders of magnitude higher than SRAM, making it the universal choice for computer main system memory.</p>\n\n<h4>2. Charge Sharing & Destructive Readout</h4>\n<p>When Word-Line $WL$ is asserted during a read operation, the storage capacitor $C_s$ shares its charge with the much larger parasitic capacitance of the long bit-line $C_{BL}$ ($C_{BL} \\sim 100 - 300\\text{ fF} \\approx 10 C_s$):</p>\n<div class=\"math-display\">\n$$V_{\\text{final}} = \\frac{C_{BL} V_{\\text{precharge}} + C_s V_C}{C_{BL} + C_s}$$\n</div>\n<p>Precharging the bit-line to $V_{DD}/2$ produces a minute voltage perturbation:</p>\n<div class=\"math-display\">\n$$\\Delta V = \\pm \\frac{C_s}{C_{BL} + C_s} \\left(\\frac{V_{DD}}{2}\\right) \\approx \\pm 100 - 150\\text{ mV}$$\n</div>\n<p>A cross-coupled regenerative sense amplifier detects $\\Delta V$ and swings the bit-line fully to $V_{DD}$ or $0\\text{ V}$. Because charge sharing partially discharges $C_s$, the readout is <strong>destructive</strong>. The sense amplifier must immediately rewrite the amplified logic level back into $C_s$ before closing the word-line (Restore Cycle).</p>\n\n<h4>3. Capacitor Leakage & Periodic Refresh Scheduling</h4>\n<p>Due to subthreshold MOSFET leakage and reverse-biased $p$-$n$ junction leakage currents, charge leaks off $C_s$ with a time constant of tens of milliseconds. To prevent catastrophic data loss, every row of the DRAM array must be read and rewritten (<strong>refreshed</strong>) periodically (typically every $64\\text{ ms}$ at $85^\\circ\\text{C}$):</p>\n<div class=\"math-display\">\n$$t_{\\text{refresh interval}} \\le 64\\text{ ms}$$\n</div>\n<p>Modern DRAM controllers interleave <em>Distributed Auto-Refresh</em> or <em>Self-Refresh</em> commands between normal read/write cycles, consuming less than $1 - 2\\%$ of total memory bus bandwidth.</p>"
        },
        {
          "id": "dig-7-4",
          "title": "Non-Volatile Memories: ROM, PROM, EPROM, EEPROM & Flash",
          "content": "<h4>1. Read-Only Memory (ROM) Evolution</h4>\n<p>Non-volatile semiconductor memories retain stored data indefinitely without requiring power supplies:</p>\n<ol>\n<li><strong>Mask ROM:</strong> Data is permanently hardwired during wafer fabrication using a custom photolithographic contact mask. Highest density and lowest cost per bit in mass production, but zero programmability.</li>\n<li><strong>Programmable ROM (PROM):</strong> Fabricated with microscopic Nichrome or polycrystalline silicon fuses in series with each memory cell. Programmed once by blowing selected fuses using high-current pulses (One-Time Programmable - OTP).</li>\n<li><strong>Erasable PROM (UV-EPROM):</strong> Utilizes a <strong>Floating-Gate MOSFET (FGMOS)</strong> with a completely isolated conductive polysilicon gate embedded inside silicon dioxide dielectric. High-voltage pulses ($V_{PP} \\approx 12 - 21\\text{ V}$) inject electrons onto the floating gate via <strong>Hot-Carrier Injection (HCI)</strong>. Stored electrons shift the transistor's threshold voltage ($V_t$), programming it to state 0. Erased by shining ultraviolet light ($254\\text{ nm}$) through a quartz window on the chip package for 20 minutes, exciting electrons over the $\\text{SiO}_2$ potential barrier.</li>\n<li><strong>Electrically Erasable PROM (EEPROM):</strong> Employs ultra-thin tunnel oxide ($d_{\\text{ox}} < 10\\text{ nm}$) beneath the floating gate, enabling bidirectional electrical erasure via <strong>Fowler-Nordheim (F-N) Quantum Mechanical Tunneling</strong>. Can be erased and reprogrammed byte-by-byte in circuit.</li>\n</ol>\n\n<h4>2. Modern Flash Memory: NAND vs NOR Architectures</h4>\n<p>Invented by Fujio Masuoka (Toshiba, 1984), Flash memory erases blocks of cells simultaneously in a single flash operation via Fowler-Nordheim tunneling:</p>\n<div class=\"table-responsive\">\n<table class=\"table table-bordered\">\n<thead>\n<tr><th>Attribute</th><th>NOR Flash</th><th>NAND Flash</th></tr>\n</thead>\n<tbody>\n<tr><td><strong>Cell Interconnection</strong></td><td>Parallel (like NOR gate)</td><td>Series strings of 32 to 128 cells (like NAND gate)</td></tr>\n<tr><td><strong>Random Access Speed</strong></td><td>Very Fast ($50 - 80\\text{ ns}$)</td><td>Slow initial access ($25\\text{ \\mu s}$)</td></tr>\n<tr><td><strong>Serial Throughput</strong></td><td>Moderate</td><td>Extremely High ($> 1\\text{ GB/s}$)</td></tr>\n<tr><td><strong>Cell Area Density</strong></td><td>Large ($10F^2$)</td><td>Extremely Compact ($4F^2$, 3D vertical stacked $> 200$ layers)</td></tr>\n<tr><td><strong>Primary Application</strong></td><td>BIOS, Router Firmware (eXecute-In-Place)</td><td>Solid-State Drives (SSDs), USB drives, Smartphones</td></tr>\n</tbody>\n</table>\n</div>"
        },
        {
          "id": "dig-7-5",
          "title": "Advanced Memory Architectures: SDRAM, DDR & Cache Hierarchy",
          "content": "<h4>1. Synchronous DRAM (SDRAM) & Double Data Rate (DDR)</h4>\n<p>Early asynchronous DRAMs required address strobe handshakes ($\\overline{RAS}, \\overline{CAS}$) that bottlenecked high-speed microprocessors. <strong>Synchronous DRAM (SDRAM)</strong> synchronizes all control, address, and data lines to the master CPU system clock using internal pipelining and multi-bank prefetching.</p>\n<p><strong>Double Data Rate (DDR) SDRAM:</strong> Transfers data on <strong>both the rising and falling edges</strong> of each clock cycle, doubling throughput at identical clock frequencies:</p>\n<ul>\n<li><strong>DDR1:</strong> 2-bit prefetch buffer (2 data words per clock cycle).</li>\n<li><strong>DDR2:</strong> 4-bit prefetch buffer.</li>\n<li><strong>DDR3:</strong> 8-bit prefetch buffer.</li>\n<li><strong>DDR4:</strong> 16-bit prefetch buffer with independent memory bank groups.</li>\n<li><strong>DDR5:</strong> Dual 32-bit channels per module, on-die ECC, data transfer rates exceeding $6400\\text{ MT/s}$.</li>\n</ul>\n\n<h4>2. Multi-Level Cache Memory Hierarchy</h4>\n<p>Because processor execution speed ($3 - 5\\text{ GHz}$, sub-nanosecond cycles) is orders of magnitude faster than DRAM latency ($50 - 70\\text{ ns}$), modern computer architecture incorporates a multi-tiered cache hierarchy exploiting the <strong>Principle of Locality</strong> (Temporal and Spatial):</p>\n<div class=\"math-display\">\n$$\\text{CPU Core Registers } (< 1\\text{ ns}) \\longrightarrow \\text{L1 Cache (SRAM, } 32\\text{ KB}, \\sim 1\\text{ ns}) \\longrightarrow \\text{L2 Cache (SRAM, } 512\\text{ KB}, \\sim 4\\text{ ns}) \\longrightarrow \\text{L3 Cache (SRAM, } 32\\text{ MB}, \\sim 12\\text{ ns}) \\longrightarrow \\text{Main Memory (DRAM, } 32\\text{ GB}, \\sim 60\\text{ ns}) \\longrightarrow \\text{Secondary Storage (NVMe SSD)}$$\n</div>\n<p>The <strong>Average Memory Access Time (AMAT)</strong> is:</p>\n<div class=\"math-display\">\n$$\\text{AMAT} = t_{\\text{hit}} + \\text{Miss Rate} \\times \\text{Miss Penalty}$$\n</div>"
        }
      ],
      "problems": [
        {
          "id": "dig-p-7-1",
          "title": "Design of a 64 KB Memory Subsystem Using 16 KB x 8 SRAM Chips",
          "statement": "Design a $64\\text{ KB}$ ($65,536 \\text{ bytes}$) microprocessor memory subsystem using standard $16\\text{ KB} \\times 8$ SRAM memory chips. (a) Determine the number of memory chips required. (b) Calculate the total number of address bus lines required for the subsystem and how many address lines connect directly to each chip. (c) Design the chip-select address decoding circuit using a 2-to-4 binary decoder and specify the hexadecimal address range for each memory block.",
          "steps": [
            {
              "stepName": "Step 1: Calculate Chip Count",
              "math": "N_{\\text{chips}} = \\frac{\\text{Total Capacity}}{\\text{Chip Capacity}} = \\frac{64\\text{ KB}}{16\\text{ KB}} = 4 \\text{ memory chips}",
              "explanation": "Four 16 KB x 8 chips are required to synthesize 64 KB."
            },
            {
              "stepName": "Step 2: Partition Address Bus Lines",
              "math": "64\\text{ KB} = 2^{16} \\implies 16 \\text{ total address lines } (A_{15} - A_0). \\quad 16\\text{ KB} = 2^{14} \\implies 14 \\text{ address lines } (A_{13} - A_0) \\text{ connect to each chip}",
              "explanation": "Address lines A0 through A13 connect in parallel to all 4 chips to select a byte within each chip."
            },
            {
              "stepName": "Step 3: Design Decoder for Chip Select",
              "math": "\\text{Remaining higher address lines } (A_{15}, A_{14}) \\text{ connect to a 2-to-4 line active-LOW decoder to drive } \\overline{CS}_0, \\overline{CS}_1, \\overline{CS}_2, \\overline{CS}_3",
              "explanation": "A 2-to-4 decoder decodes A15 and A14 to enable one of the four chips."
            },
            {
              "stepName": "Step 4: Determine Hexadecimal Memory Address Ranges",
              "math": "\\begin{aligned} \\text{Chip 0 } (A_{15}A_{14}=00): \\ & 0000_{16} \\text{ to } 3\\text{FFF}_{16} \\ (16,384 \\text{ bytes}) \\\\ \\text{Chip 1 } (A_{15}A_{14}=01): \\ & 4000_{16} \\text{ to } 7\\text{FFF}_{16} \\\\ \\text{Chip 2 } (A_{15}A_{14}=10): \\ & 8000_{16} \\text{ to } \\text{BFFF}_{16} \\\\ \\text{Chip 3 } (A_{15}A_{14}=11): \\ & \\text{C}000_{16} \\text{ to } \\text{FFFF}_{16} \\end{aligned}",
              "explanation": "List continuous address space from 0000H to FFFFH."
            }
          ],
          "answer": "N_{\\text{chips}} = 4; \\quad 16 \\text{ total address lines } (A_{13}-A_0 \\text{ to chips}, \\ A_{15}-A_{14} \\text{ to 2:4 decoder}); \\quad \\text{Range: } 0000_{16} - \\text{FFFF}_{16}"
        },
        {
          "id": "dig-p-7-2",
          "title": "DRAM Refresh Frequency, Time Overhead and Bandwidth Loss",
          "statement": "An $8\\text{ Gb}$ DDR4 DRAM memory chip is organized internally into $8192$ rows. All $8192$ rows must be refreshed within a maximum retention window of $t_{\\text{ret}} = 64.0\\text{ ms}$. Each individual row refresh cycle takes $t_{RC} = 45.0\\text{ ns}$. (a) Calculate the average refresh frequency (how often a refresh command must be issued). (b) Calculate the total time consumed per $64\\text{ ms}$ interval solely for refreshing. (c) Determine the percentage of memory bandwidth lost to refresh operations.",
          "steps": [
            {
              "stepName": "Step 1: Calculate Refresh Command Interval",
              "math": "t_{\\text{REFI}} = \\frac{t_{\\text{ret}}}{N_{\\text{rows}}} = \\frac{64.0 \\times 10^{-3}\\text{ s}}{8192} \\approx 7.8125 \\times 10^{-6}\\text{ s} = 7.81\\text{ \\mu s}",
              "explanation": "A refresh command must be executed every 7.81 microseconds."
            },
            {
              "stepName": "Step 2: Calculate Total Time Spent Refreshing per 64 ms",
              "math": "t_{\\text{refresh, total}} = N_{\\text{rows}} \\times t_{RC} = 8192 \\times (45.0 \\times 10^{-9}\\text{ s}) \\approx 3.6864 \\times 10^{-4}\\text{ s} = 368.64\\text{ \\mu s}",
              "explanation": "Multiply number of rows by row cycle time."
            },
            {
              "stepName": "Step 3: Calculate Bandwidth Overhead Percentage",
              "math": "\\text{Overhead} = \\frac{t_{\\text{refresh, total}}}{t_{\\text{ret}}} \\times 100\\% = \\frac{368.64\\text{ \\mu s}}{64,000\\text{ \\mu s}} \\times 100\\% \\approx 0.576\\%",
              "explanation": "Refresh consumes only 0.58% of total memory bandwidth."
            }
          ],
          "answer": "t_{\\text{REFI}} = 7.81\\text{ \\mu s}, \\quad t_{\\text{total}} = 368.6\\text{ \\mu s per } 64\\text{ ms}, \\quad \\text{Bandwidth Overhead} = 0.576\\%"
        },
        {
          "id": "dig-p-7-3",
          "title": "Average Memory Access Time (AMAT) in Multi-Level Cache Hierarchy",
          "statement": "A modern computer architecture features a two-level cache hierarchy: Level 1 ($L_1$) cache has an access time of $t_1 = 1.20\\text{ ns}$ and a hit rate of $H_1 = 94.0\\%$; Level 2 ($L_2$) cache has an access time of $t_2 = 6.00\\text{ ns}$ and a local hit rate of $H_2 = 85.0\\%$; Main DRAM memory has an access latency of $t_{MM} = 55.0\\text{ ns}$. (a) Calculate the global miss rate for the cache system. (b) Calculate the Average Memory Access Time (AMAT) of the processor. (c) By what factor would memory performance degrade if the caches were eliminated?",
          "steps": [
            {
              "stepName": "Step 1: Calculate Global Miss Rate",
              "math": "\\text{Miss Rate}_1 = 1 - 0.940 = 0.060. \\quad \\text{Global Miss Rate} = \\text{Miss Rate}_1 \\times (1 - H_2) = 0.060 \\times (1 - 0.850) = 0.060 \\times 0.150 = 0.0090 \\ (0.90\\%)",
              "explanation": "Only 0.9% of memory requests reach main DRAM."
            },
            {
              "stepName": "Step 2: Calculate Average Memory Access Time (AMAT)",
              "math": "\\text{AMAT} = t_1 + \\text{Miss Rate}_1 \\times [t_2 + (1 - H_2) \\times t_{MM}] = 1.20 + 0.060 \\times [6.00 + 0.150 \\times 55.0]\\text{ ns}",
              "explanation": "Formulate multi-level AMAT equation."
            },
            {
              "stepName": "Step 3: Evaluate AMAT",
              "math": "\\text{AMAT} = 1.20 + 0.060 \\times [6.00 + 8.25] = 1.20 + 0.060 \\times (14.25) = 1.20 + 0.855 = 2.055\\text{ ns}",
              "explanation": "Average access time is only 2.06 ns."
            },
            {
              "stepName": "Step 4: Compute Degradation Factor Without Caches",
              "math": "\\text{Degradation} = \\frac{t_{MM}}{\\text{AMAT}} = \\frac{55.0\\text{ ns}}{2.055\\text{ ns}} \\approx 26.8 \\times",
              "explanation": "Without caches, memory access would be nearly 27 times slower!"
            }
          ],
          "answer": "\\text{Global Miss Rate} = 0.90\\%, \\quad \\text{AMAT} = 2.055\\text{ ns}, \\quad \\text{Speedup over Raw DRAM: } 26.8\\times"
        }
      ]
    },
    {
      "unitNumber": 8,
      "unitId": "unit8-ic-technology-fabrication",
      "title": "Integrated Circuit (IC) Technology & Silicon VLSI Microfabrication",
      "description": "Solid-state microfabrication physics and silicon cleanroom processing: classification of integrated circuits (SSI, MSI, LSI, VLSI, ULSI); single-crystal silicon ingot preparation via the Czochralski (CZ) pulling method, wafer slicing, and chemical-mechanical planarization (CMP); epitaxial layer growth; thermal oxidation kinetics and the Deal-Grove model (linear-parabolic regimes); photolithographic pattern transfer, optical diffraction limits, deep ultraviolet (DUV), and extreme ultraviolet (EUV); impurity doping via thermal furnace diffusion (Fick's laws) versus high-energy ion implantation (LSS range theory); metallization, electromigration, vias, and packaging; complete monolithic fabrication sequences for planar NPN bipolar transistors and CMOS inverters, integrated resistors, MOS capacitors, and sheet resistance R_s.",
      "sections": [
        {
          "id": "dig-8-1",
          "title": "Silicon Crystal Growth, Czochralski Ingot Pulling & Wafers",
          "content": "<h4>1. Classification of Integrated Circuits</h4>\n<p>An <strong>Integrated Circuit (IC)</strong> is a complete electronic circuit fabricated as a single monolithic block on a thin planar substrate of single-crystal silicon. Integration density has expanded exponentially across decades (Moore's Law):</p>\n<ul>\n<li><strong>Small-Scale Integration (SSI, 1960s):</strong> $< 12$ equivalent logic gates (e.g., 7400 quad NAND gate).</li>\n<li><strong>Medium-Scale Integration (MSI, late 1960s):</strong> $12 - 100$ gates (e.g., counters, decoders, 4-bit adders).</li>\n<li><strong>Large-Scale Integration (LSI, 1970s):</strong> $100 - 10,000$ gates (e.g., 8-bit microprocessors like Intel 8080, early RAMs).</li>\n<li><strong>Very Large-Scale Integration (VLSI, 1980s):</strong> $10,000 - 1,000,000$ gates.</li>\n<li><strong>Ultra Large-Scale Integration (ULSI / Modern Nanoscale):</strong> $> 10^{9} - 10^{11}$ transistors on a single $200\\text{ mm}^2$ chip (e.g., multi-core CPUs, GPUs with 80+ billion transistors).</li>\n</ul>\n\n<h4>2. Electronic Grade Silicon (EGS) & The Czochralski (CZ) Method</h4>\n<p>Microfabrication begins with raw quartzite sand ($\\text{SiO}_2$), reduced in an electric arc furnace to Metallurgical Grade Silicon (MGS, $\\sim 98\\%$ pure). Chemical chlorination produces gaseous trichlorosilane ($\\text{SiHCl}_3$), which is fractionally distilled and reduced with hydrogen to synthesize polycrystalline <strong>Electronic Grade Silicon (EGS)</strong> with impurity levels below <strong>1 part per billion ($< 10^{-9}$)</strong>.</p>\n<p>To convert poly-silicon into a dislocation-free single crystal, Jan Czochralski's (1918) crystal pulling method is employed:</p>\n<ol>\n<li>EGS is melted in a high-purity fused silica crucible at $1420^\\circ\\text{C}$ in an inert Argon atmosphere. Controlled $p$-type (Boron) or $n$-type (Phosphorus) dopants are added.</li>\n<li>A small single-crystal seed of precise crystallographic orientation ($\\langle 100 \\rangle$ or $\\langle 111 \\rangle$) is lowered into the melt surface.</li>\n<li>The seed crystal is slowly rotated and pulled upward ($1 - 2\\text{ mm/min}$). Surface tension and heat extraction cause silicon atoms in the melt to freeze onto the seed in identical crystalline lattice orientation, producing a massive cylindrical single-crystal ingot (boule) up to $300\\text{ mm}$ ($12\\text{ inches}$) in diameter and weighing over $100\\text{ kg}$.</li>\n</ol>\n\n<h4>3. Wafer Shaping and Chemical-Mechanical Planarization (CMP)</h4>\n<p>The ingot is ground to uniform diameter, flat or notched for crystal orientation alignment, and sliced into thin discs ($775\\text{ \\mu m}$ thick) using diamond-coated high-speed wire saws. Wafers undergo edge rounding, chemical etching to relieve surface mechanical damage, and multi-stage <strong>Chemical-Mechanical Planarization (CMP)</strong> using colloidal silica slurry to achieve an atomically flat, mirror-polished surface with root-mean-square roughness $< 0.1\\text{ nm}$.</p>"
        },
        {
          "id": "dig-8-2",
          "title": "Epitaxy, Thermal Oxidation & The Deal-Grove Model",
          "simulation": "dig-deal-grove-oxidation-sim",
          "content": "<h4>1. Epitaxial Layer Growth</h4>\n<p><strong>Epitaxy</strong> (from Greek <em>epi</em> \"upon\" and <em>taxis</em> \"ordered\") is the deposition of a thin single-crystal silicon layer ($0.5 - 5\\text{ \\mu m}$) onto the substrate wafer, continuing the substrate's exact crystalline lattice. Unlike bulk substrates, the epitaxial layer's dopant type and concentration can be tailored with atomic precision. In <strong>Vapor-Phase Epitaxy (VPE)</strong>, silicon tetrachloride gas is reduced at $1200^\\circ\\text{C}$:</p>\n<div class=\"math-display\">\n$$\\text{SiCl}_4\\text{(g)} + 2\\text{H}_2\\text{(g)} \\overset{1200^\\circ\\text{C}}{\\rightleftharpoons} \\text{Si(s)} + 4\\text{HCl(g)}$$\n</div>\n\n<h4>2. Silicon Dioxide ($\\text{SiO}_2$) Thermal Oxidation</h4>\n<p>Silicon's pre-eminence as the king of semiconductor materials stems from its native oxide: silicon dioxide ($\\text{SiO}_2$), a chemically robust, impermeable dielectric insulator with an enormous band gap ($9.0\\text{ eV}$), high breakdown electric field ($10^7\\text{ V/cm}$), and exceptional dielectric masking properties against chemical dopants.</p>\n<p>Wafers are heated in high-temperature quartz tube furnaces ($900 - 1100^\\circ\\text{C}$):</p>\n<ul>\n<li><strong>Dry Oxidation:</strong> $\\text{Si} + \\text{O}_2 \\to \\text{SiO}_2$. Slower growth rate, but yields ultra-dense oxide with low interface trap density ($\\sim 10^{10}\\text{ cm}^{-2}$). Used for thin MOSFET gate oxides.</li>\n<li><strong>Wet Oxidation (Steam):</strong> $\\text{Si} + 2\\text{H}_2\\text{O} \\to \\text{SiO}_2 + 2\\text{H}_2$. Grows oxide 5 to 10 times faster due to high solubility of $\\text{H}_2\\text{O}$ in silica. Used for thick field isolation oxides ($300 - 500\\text{ nm}$).</li>\n</ul>\n\n<h4>3. The Deal-Grove Oxidation Kinetics Model</h4>\n<p>Bruce Deal and Andrew Grove (1965) formulated the kinetics of thermal oxidation. As oxide grows to thickness $x_0$, oxidant species must diffuse through the existing oxide layer before reacting at the $\\text{Si}\\text{-}\\text{SiO}_2$ interface:</p>\n<div class=\"math-display\">\n$$x_0^2 + A x_0 = B(t + \\tau)$$\n</div>\n<p>where $B$ is the parabolic rate constant ($\\mu\\text{m}^2/\\text{hr}$), $B/A$ is the linear rate constant ($\\mu\\text{m/hr}$), and $\\tau$ accounts for any initial oxide layer. Solving the quadratic equation:</p>\n<div class=\"math-display\">\n$$x_0(t) = \\frac{A}{2} \\left[ \\sqrt{1 + \\frac{4B(t + \\tau)}{A^2}} - 1 \\right]$$\n</div>\n<ul>\n<li><strong>Linear Regime ($t \\ll A^2 / 4B$, Thin Oxides):</strong> Growth is limited by chemical reaction rate at the silicon interface:\n<div class=\"math-display\">\n$$x_0(t) \\approx \\frac{B}{A}(t + \\tau)$$\n</div></li>\n<li><strong>Parabolic Regime ($t \\gg A^2 / 4B$, Thick Oxides):</strong> Growth is limited by diffusion of oxidant molecules through the thick oxide layer:\n<div class=\"math-display\">\n$$x_0^2(t) \\approx B \\cdot t \\implies x_0(t) \\propto \\sqrt{t}$$\n</div></li>\n</ul>"
        },
        {
          "id": "dig-8-3",
          "title": "Photolithography: Photoresist Chemistry & Pattern Transfer",
          "content": "<h4>1. The Photolithographic Process Sequence</h4>\n<p><strong>Photolithography</strong> is the optical printing process that transfers microscopic geometric circuit patterns from a photographic mask (reticle) onto the wafer surface:</p>\n<ol>\n<li><strong>Surface Preparation & HMDS Priming:</strong> Hexamethyldisilazane (HMDS) vapor prime makes the hydrophilic $\\text{SiO}_2$ surface hydrophobic to ensure photoresist adhesion.</li>\n<li><strong>Spin Coating:</strong> A liquid light-sensitive polymeric <strong>photoresist</strong> is dispensed onto the wafer, spun at $3000 - 5000\\text{ RPM}$ to form a uniform thin film ($0.5 - 1.0\\text{ \\mu m}$).</li>\n<li><strong>Soft Bake:</strong> Heated to $90 - 100^\\circ\\text{C}$ to evaporate solvents.</li>\n<li><strong>Mask Alignment & Exposure:</strong> High-precision reduction stepper lenses project UV light through a photomask.\n<ul>\n<li><strong>Positive Photoresist (Diazoquinone/Novolac):</strong> Exposed regions undergo photochemical scission, becoming highly soluble in alkaline aqueous developer solution. Unexposed regions remain insoluble. Leaves an exact duplicate of the dark mask pattern. Standard in VLSI due to superior resolution.</li>\n<li><strong>Negative Photoresist (Polyisoprene):</strong> Exposed regions cross-link and polymerize, becoming insoluble. Leaves the photographic negative. Swells during development, limiting resolution.</li>\n</ul></li>\n<li><strong>Post-Exposure Bake & Development:</strong> Dissolves soluble resist regions, exposing the underlying $\\text{SiO}_2$ film.</li>\n<li><strong>Hard Bake ($120 - 140^\\circ\\text{C}$):</strong> Hardens the resist polymer for etch resistance.</li>\n<li><strong>Etching:</strong> Pattern transfer into the underlying material.\n<ul>\n<li><strong>Wet Chemical Etching:</strong> Buffered Oxide Etch (BOE / HF). Isotropic (etches equally in all directions), producing undesirable lateral undercut.</li>\n<li><strong>Dry Plasma / Reactive-Ion Etching (RIE):</strong> High-energy reactive ions in an anisotropic RF plasma etch vertically with near-zero lateral undercut, preserving sub-micron feature fidelity.</li>\n</ul></li>\n<li><strong>Photoresist Stripping:</strong> Removed via oxygen plasma ashing ($\\text{O}_2$ plasma incinerates organic resist to $\\text{CO}_2$ and $\\text{H}_2\\text{O}$).</li>\n</ol>\n\n<h4>2. Optical Resolution Limits & EUV Lithography</h4>\n<p>The minimum resolvable feature size ($CD$, Critical Dimension) is governed by the Rayleigh diffraction criterion:</p>\n<div class=\"math-display\">\n$$CD = k_1 \\frac{\\lambda}{NA}$$\n</div>\n<p>where $\\lambda$ is illumination wavelength, $NA = n\\sin\\theta$ is numerical aperture, and $k_1$ is a process factor ($\\ge 0.25$). Modern semiconductor fabrication transitioned from Mercury arc lamps (G-line $436\\text{ nm}$, I-line $365\\text{ nm}$) to Excimer lasers (KrF $248\\text{ nm}$, ArF $193\\text{ nm}$ immersion lithography with water $n=1.44$). For sub-$7\\text{ nm}$ nodes, state-of-the-art foundries utilize <strong>Extreme Ultraviolet (EUV)</strong> lithography ($\\lambda = 13.5\\text{ nm}$) generated by pulsing high-power $\\text{CO}_2$ lasers into molten tin droplets in ultra-high vacuum.</p>"
        },
        {
          "id": "dig-8-4",
          "title": "Doping: Thermal Diffusion vs High-Energy Ion Implantation",
          "content": "<h4>1. Thermal Furnace Diffusion</h4>\n<p>Impurity doping introduces group-III acceptors (Boron) or group-V donors (Phosphorus, Arsenic) into the silicon crystal lattice. In classical <strong>thermal diffusion</strong>, wafers in a quartz furnace ($900 - 1200^\\circ\\text{C}$) are exposed to a gaseous dopant source ($\\text{POCl}_3, \\text{BBr}_3$):</p>\n<ol>\n<li><strong>Predeposition (Constant Source Diffusion):</strong> Dopant surface concentration is held fixed at solid solubility limit $C_s$. Governed by Fick's Second Law:\n<div class=\"math-display\">\n$$\\frac{\\partial C(x,t)}{\\partial t} = D \\frac{\\partial^2 C(x,t)}{\\partial x^2}$$\n</div>\nBoundary conditions ($C(0,t) = C_s, C(\\infty,t) = 0$) yield the <strong>Complementary Error Function (erfc)</strong> profile:\n<div class=\"math-display\">\n$$C(x, t) = C_s \\operatorname{erfc}\\left( \\frac{x}{2 \\sqrt{Dt}} \\right)$$\n</div></li>\n<li><strong>Drive-In Diffusion (Limited Source):</strong> Dopant vapor is shut off; the fixed deposited dose $Q$ drives deeper into the silicon at higher temperature, forming a <strong>Gaussian profile</strong>:\n<div class=\"math-display\">\n$$C(x, t) = \\frac{Q}{\\sqrt{\\pi D t}} \\exp\\left( - \\frac{x^2}{4 D t} \\right)$$\n</div></li>\n</ol>\n<p>Thermal diffusion is isotropic: dopants diffuse laterally under mask edges by $70 - 80\\%$ of the vertical junction depth ($x_{\\text{lat}} \\approx 0.8 x_j$), making it obsolete for shallow sub-micron source/drain junctions.</p>\n\n<h4>2. High-Energy Ion Implantation</h4>\n<p>The dominant doping technique in modern VLSI. Dopant atoms are ionized in an arc source, accelerated through high electrostatic potential differences ($10\\text{ keV} - 3\\text{ MeV}$), mass-analyzed using a bending dipole electromagnet to guarantee $100\\%$ chemical purity, and fired directly into the silicon wafer.</p>\n<p>According to Lindhard-Scharff-Schiøtt (LSS) stopping theory, the dopant profile follows a Gaussian distribution centered at the <strong>Projected Range ($R_p$)</strong> with standard deviation <strong>Projected Straggle ($\\Delta R_p$)</strong>:</p>\n<div class=\"math-display\">\n$$C(x) = \\frac{\\Phi}{\\sqrt{2\\pi}\\Delta R_p} \\exp\\left( - \\frac{(x - R_p)^2}{2 \\Delta R_p^2} \\right)$$\n</div>\n<p>where $\\Phi$ is the implanted ion dose (ions/$\\text{cm}^2$). The peak concentration occurs at depth $x = R_p$:</p>\n<div class=\"math-display\">\n$$C_{\\text{peak}} = \\frac{\\Phi}{\\sqrt{2\\pi}\\Delta R_p} \\approx \\frac{0.3989 \\Phi}{\\Delta R_p}$$\n</div>\n<p>Advantages over diffusion: Independent control of depth (via acceleration energy) and dose (via beam current integration); near-zero lateral straggle; room temperature operation; compatibility with photoresist masks.</p>\n<p><strong>Post-Implant Thermal Annealing:</strong> High-energy ion bombardment shatters the crystalline silicon lattice into an amorphous layer. Rapid Thermal Annealing (RTA, $1000^\\circ\\text{C}$ for seconds) recrystallizes the damaged lattice and shifts dopant atoms into substitutional lattice sites where they become electrically active.</p>"
        },
        {
          "id": "dig-8-5",
          "title": "CMOS Inverter Fabrication Sequence & Sheet Resistance",
          "simulation": "dig-cmos-inverter-fabrication-sim",
          "content": "<h4>1. Complete Monolithic CMOS Fabrication Sequence (Self-Aligned Twin-Well)</h4>\n<p>Fabricating a complementary pair of nMOS and pMOS transistors on a single substrate requires a sequence of approximately 30 lithographic mask levels:</p>\n<ol>\n<li><strong>Starting Substrate:</strong> Lightly doped $p$-type $\\langle 100 \\rangle$ silicon wafer.</li>\n<li><strong>Well Formation:</strong> Ion implantation of Phosphorus followed by high-temperature drive-in forms the <strong>$n$-well</strong> (in which pMOS transistors will reside).</li>\n<li><strong>Shallow Trench Isolation (STI):</strong> Etch narrow vertical trenches ($300\\text{ nm}$ deep) between active transistor areas, fill with CVD $\\text{SiO}_2$, and planarize via CMP to eliminate parasitic latchup.</li>\n<li><strong>Gate Stack:</strong> Thermally grow ultra-thin gate dielectric ($\\text{SiO}_2$ or high-$\\kappa$ Hafnium dioxide $\\text{HfO}_2$), deposit polycrystalline silicon (polysilicon) or metal gate layer, pattern via lithography, and etch vertical gate electrodes.</li>\n<li><strong>Lightly Doped Drain (LDD) Implantation:</strong> Shallow low-dose implants under gate edges suppress hot-carrier degradation.</li>\n<li><strong>Dielectric Sidewall Spacers:</strong> Conformally deposit $\\text{Si}_3\\text{N}_4$ or $\\text{SiO}_2$ and anisotropically plasma etch to leave insulating spacer sidewalls along gate edges.</li>\n<li><strong>Source/Drain Self-Aligned Implantation:</strong>\n<ul>\n<li>$n^+$ Implantation (Arsenic/Phosphorus) forms nMOS source/drain regions. The polysilicon gate acts as an impenetrable mask, naturally aligning the channel edges (Self-Aligned Gate).</li>\n<li>$p^+$ Implantation (Boron) forms pMOS source/drain regions.</li>\n</ul></li>\n<li><strong>Salicidation (Self-Aligned Silicide):</strong> Deposit thin Cobalt or Nickel, anneal at $700^\\circ\\text{C}$ to form low-resistance metal silicide ($\\text{NiSi}$) on all exposed silicon contacts and polysilicon gates, reducing contact resistance.</li>\n<li><strong>Pre-Metal Dielectric (PMD) & Tungsten Contacts:</strong> Deposit thick planarizing oxide, plasma etch contact vias down to source/drain/gate regions, and fill with refractory Tungsten (W) plugs.</li>\n<li><strong>Multi-Level Metallization:</strong> Deposit alternating copper (Cu) interconnect wire layers separated by low-$\\kappa$ dielectric insulators using the dual-damascene electroplating process (up to 12 - 15 metal wiring levels).</li>\n<li><strong>Passivation & Wire Bonding:</strong> Deposit protective silicon nitride ($\\text{Si}_3\\text{N}_4$) scratch coat, etch bond pad openings, slice die, mount to ceramic/plastic leadframe, bond gold/copper wires, and encapsulate in epoxy resin.</li>\n</ol>\n\n<h4>2. Integrated Passive Components & Sheet Resistance ($R_s$)</h4>\n<p>Passive circuit components inside integrated circuits:</p>\n<ul>\n<li><strong>Diffused Resistors:</strong> A semiconductor layer of length $L$, width $W$, thickness $t$, and resistivity $\\rho$ has resistance:\n<div class=\"math-display\">\n$$R = \\rho \\frac{L}{A} = \\frac{\\rho}{t} \\left(\\frac{L}{W}\\right) = R_s \\left(\\frac{L}{W}\\right)$$\n</div>\nwhere $R_s = \\rho / t$ is the <strong>Sheet Resistance</strong>, expressed in units of <strong>Ohms per square ($\\Omega/\\square$)</strong>. The ratio $L/W$ represents the number of squares. Right-angle square corners contribute approximately $0.56$ squares each due to current crowding.</li>\n<li><strong>MOS Capacitors:</strong> Formed by gate polysilicon electrode over thin dielectric oxide over an $n^+$ diffused silicon bottom plate:\n<div class=\"math-display\">\n$$C = \\frac{\\varepsilon_{\\text{ox}} \\varepsilon_0 A}{t_{\\text{ox}}}$$\n</div></li>\n</ul>"
        }
      ],
      "problems": [
        {
          "id": "dig-p-8-1",
          "title": "Deal-Grove Thermal Oxidation Thickness in Dry vs Wet Oxygen",
          "statement": "A silicon wafer is oxidized at $1000^\\circ\\text{C}$ starting with an initial native oxide of $x_i = 10\\text{ nm}$ (assume $\\tau \\approx 0$). The Deal-Grove rate constants are: Dry $\\text{O}_2$: $B = 0.0117\\text{ \\mu m}^2/\\text{hr}$, $B/A = 0.070\\text{ \\mu m/hr}$; Wet Steam: $B = 0.287\\text{ \\mu m}^2/\\text{hr}$, $B/A = 0.867\\text{ \\mu m/hr}$. (a) Calculate the parameter $A$ for both dry and wet processes. (b) Calculate the oxide thickness $x_0$ grown after $t = 2.0\\text{ hours}$ in dry $\\text{O}_2$. (c) Calculate the oxide thickness $x_0$ grown after $t = 2.0\\text{ hours}$ in wet steam and evaluate the growth acceleration factor.",
          "steps": [
            {
              "stepName": "Step 1: Calculate Parameter A",
              "math": "A = \\frac{B}{B/A}. \\quad \\text{Dry: } A = \\frac{0.0117}{0.070} \\approx 0.1671\\text{ \\mu m}. \\quad \\text{Wet: } A = \\frac{0.287}{0.867} \\approx 0.3310\\text{ \\mu m}",
              "explanation": "Compute A for both oxidation regimes."
            },
            {
              "stepName": "Step 2: Solve Deal-Grove Equation for Dry Oxidation",
              "math": "x_0(t) = \\frac{A}{2} \\left[ \\sqrt{1 + \\frac{4 B t}{A^2}} - 1 \\right] = \\frac{0.1671}{2} \\left[ \\sqrt{1 + \\frac{4(0.0117)(2.0)}{(0.1671)^2}} - 1 \\right] = 0.08355 \\left[ \\sqrt{1 + \\frac{0.0936}{0.02793}} - 1 \\right]",
              "explanation": "Substitute numerical values into the quadratic Deal-Grove formula."
            },
            {
              "stepName": "Step 3: Evaluate Dry Oxide Thickness",
              "math": "x_0 = 0.08355 \\left[ \\sqrt{1 + 3.351} - 1 \\right] = 0.08355 [2.086 - 1] = 0.08355 \\times 1.086 \\approx 0.0907\\text{ \\mu m} = 90.7\\text{ nm}",
              "explanation": "Dry oxidation yields ~91 nm after 2 hours."
            },
            {
              "stepName": "Step 4: Solve Deal-Grove Equation for Wet Steam Oxidation",
              "math": "x_0 = \\frac{0.3310}{2} \\left[ \\sqrt{1 + \\frac{4(0.287)(2.0)}{(0.3310)^2}} - 1 \\right] = 0.1655 \\left[ \\sqrt{1 + \\frac{2.296}{0.1096}} - 1 \\right] = 0.1655 [\\sqrt{21.95} - 1] = 0.1655 [4.685 - 1] \\approx 0.6099\\text{ \\mu m} = 610\\text{ nm}",
              "explanation": "Wet steam yields ~610 nm after 2 hours."
            },
            {
              "stepName": "Step 5: Compare Acceleration Factor",
              "math": "\\text{Acceleration} = \\frac{609.9\\text{ nm}}{90.7\\text{ nm}} \\approx 6.72 \\times",
              "explanation": "Wet oxidation is 6.7 times thicker than dry oxidation due to the high solubility of H2O in silica."
            }
          ],
          "answer": "x_{\\text{dry}} = 90.7\\text{ nm}, \\quad x_{\\text{wet}} = 610\\text{ nm} \\quad (\\text{Wet Steam is } 6.72\\times \\text{ faster})"
        },
        {
          "id": "dig-p-8-2",
          "title": "Integrated Diffused Resistor Serpentine Layout Design",
          "statement": "An integrated circuit requires a precision diffused resistor of value $R = 8.50\\text{ k}\\Omega$. A $p$-type diffused layer has a measured sheet resistance of $R_s = 40.0\\text{ }\\Omega/\\square$. The minimum design rule lithographic line width is $W = 2.50\\text{ \\mu m}$. The layout is routed in a serpentine geometry incorporating four $90^\\circ$ square corners (each corner contributes $0.56$ effective squares). (a) Calculate the total number of squares required. (b) Determine the effective number of squares in the straight sections. (c) Calculate the total physical length $L$ of the resistor track.",
          "steps": [
            {
              "stepName": "Step 1: Calculate Total Required Squares",
              "math": "N_{\\text{total squares}} = \\frac{R}{R_s} = \\frac{8500\\text{ }\\Omega}{40.0\\text{ }\\Omega/\\square} = 212.5 \\text{ squares}",
              "explanation": "Divide total target resistance by sheet resistance."
            },
            {
              "stepName": "Step 2: Account for Corner Squares",
              "math": "N_{\\text{corners}} = 4 \\times 0.56 = 2.24 \\text{ squares}",
              "explanation": "Four 90-degree corners contribute 2.24 squares."
            },
            {
              "stepName": "Step 3: Calculate Squares in Straight Run",
              "math": "N_{\\text{straight}} = N_{\\text{total}} - N_{\\text{corners}} = 212.5 - 2.24 = 210.26 \\text{ squares}",
              "explanation": "Subtract corner contribution."
            },
            {
              "stepName": "Step 4: Calculate Total Length of Straight Runs",
              "math": "L_{\\text{straight}} = N_{\\text{straight}} \\times W = 210.26 \\times 2.50\\text{ \\mu m} \\approx 525.65\\text{ \\mu m}",
              "explanation": "Multiply straight squares by line width."
            },
            {
              "stepName": "Step 5: Total Centerline Track Length",
              "math": "L_{\\text{total}} = L_{\\text{straight}} + 4 \\times W = 525.65 + (4 \\times 2.50)\\text{ \\mu m} = 535.65\\text{ \\mu m} \\approx 536\\text{ \\mu m}",
              "explanation": "Centerline length is ~536 micrometers."
            }
          ],
          "answer": "N_{\\text{squares}} = 212.5 \\text{ squares}, \\quad L_{\\text{straight}} = 525.7\\text{ \\mu m}, \\quad L_{\\text{total}} \\approx 536\\text{ \\mu m}"
        },
        {
          "id": "dig-p-8-3",
          "title": "Ion Implantation Peak Concentration and Junction Depth",
          "statement": "Boron ($^{11}\\text{B}$) is ion-implanted at an acceleration energy of $E = 100\\text{ keV}$ into an $n$-type silicon substrate with uniform background doping concentration $N_D = 2.0 \\times 10^{16}\\text{ atoms/cm}^3$. The implant dose is $\\Phi = 4.0 \\times 10^{14}\\text{ cm}^{-2}$. From LSS range tables, the projected range is $R_p = 0.30\\text{ \\mu m}$ ($3.0 \\times 10^{-5}\\text{ cm}$) and the projected straggle is $\\Delta R_p = 0.070\\text{ \\mu m}$ ($7.0 \\times 10^{-6}\\text{ cm}$). (a) Calculate the peak Boron dopant concentration $C_{\\text{peak}}$ at $x = R_p$. (b) Calculate the metallurgical $p$-$n$ junction depth $x_j$ where $C(x_j) = N_D$.",
          "steps": [
            {
              "stepName": "Step 1: Calculate Peak Concentration at x = R_p",
              "math": "C_{\\text{peak}} = \\frac{\\Phi}{\\sqrt{2\\pi}\\Delta R_p} = \\frac{4.0 \\times 10^{14}\\text{ cm}^{-2}}{\\sqrt{2\\pi}(7.0 \\times 10^{-6}\\text{ cm})} = \\frac{4.0 \\times 10^{14}}{1.7545 \\times 10^{-5}} \\approx 2.28 \\times 10^{19}\\text{ cm}^{-3}",
              "explanation": "Evaluate peak concentration at the center of the Gaussian profile."
            },
            {
              "stepName": "Step 2: Formulate Metallurgical Junction Condition",
              "math": "C(x_j) = C_{\\text{peak}} \\exp\\left( - \\frac{(x_j - R_p)^2}{2 \\Delta R_p^2} \\right) = N_D = 2.0 \\times 10^{16}\\text{ cm}^{-3}",
              "explanation": "Set Gaussian concentration equal to background substrate doping."
            },
            {
              "stepName": "Step 3: Solve for Distance from Peak",
              "math": "\\exp\\left( - \\frac{(x_j - R_p)^2}{2 \\Delta R_p^2} \\right) = \\frac{2.0 \\times 10^{16}}{2.28 \\times 10^{19}} \\approx 8.77 \\times 10^{-4} \\implies \\frac{(x_j - R_p)^2}{2 \\Delta R_p^2} = -\\ln(8.77 \\times 10^{-4}) \\approx 7.039",
              "explanation": "Take natural logarithm of concentration ratio."
            },
            {
              "stepName": "Step 4: Calculate Junction Depth x_j",
              "math": "|x_j - R_p| = \\Delta R_p \\sqrt{2 \\times 7.039} = (0.070\\text{ \\mu m}) \\times \\sqrt{14.078} = 0.070 \\times 3.752 \\approx 0.263\\text{ \\mu m}",
              "explanation": "Multiply straggle by square root factor: 0.263 um beyond peak."
            },
            {
              "stepName": "Step 5: Final Metallurgical Depth",
              "math": "x_j = R_p + 0.263\\text{ \\mu m} = 0.300 + 0.263 = 0.563\\text{ \\mu m} = 563\\text{ nm}",
              "explanation": "Add projected range Rp to find junction depth from wafer surface."
            }
          ],
          "answer": "C_{\\text{peak}} = 2.28 \\times 10^{19}\\text{ cm}^{-3}, \\quad x_j = 0.563\\text{ \\mu m} = 563\\text{ nm}"
        }
      ]
    }
  ]
};
