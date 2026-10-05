import json

# ==========================================
# UNIT 3: Combinational Optimization, K-Maps & Arithmetic Circuits
# ==========================================
u3 = {
    "unitNumber": 3,
    "unitId": "unit3-k-maps-arithmetic-circuits",
    "title": "Combinational Optimization, K-Maps & Arithmetic Circuits",
    "description": "Exhaustive theory and practice of combinational logic minimization and arithmetic computation: minterms (m_i), maxterms (M_i), canonical Sum-of-Products (SOP) and Product-of-Sums (POS) representations; Karnaugh Map (K-Map) minimization across 2, 3, 4, and 5 variables with Gray code adjacency and Don't Care states; Quine-McCluskey tabular algorithm, prime implicants, and Petrick's method; radix and diminished radix complements (1's, 2's, 9's, 10's complement); half-adders, full-adders, parallel ripple-carry adders, carry-lookahead generators; BCD decimal adders with +6 correction logic, half/full subtractors, and array binary multipliers.",
    "sections": [
        {
            "id": "dig-3-1",
            "title": "Canonical Boolean Forms: Minterms, Maxterms, SOP & POS",
            "content": r"""<h4>1. Canonical Boolean Representations</h4>
<p>Every Boolean switching function of $n$ variables $F(x_1, x_2, \dots, x_n)$ can be expressed uniquely in two complementary canonical forms:</p>
<ol>
<li><strong>Minterms ($m_i$) and Canonical Sum-of-Products (SOP):</strong> A <strong>minterm</strong> is a product (AND) of all $n$ variables, with each variable appearing exactly once in either its uncomplemented or complemented form. An $n$-variable function possesses $2^n$ distinct minterms ($m_0$ through $m_{2^n-1}$). Minterm $m_i$ evaluates to <strong>1</strong> for exactly one input combination whose binary representation equals index $i$. Any function is uniquely defined as the logical sum (OR) of its 1-generating minterms:
<div class="math-display">
$$F(A, B, C) = \sum m(1, 4, 6, 7) = \bar{A}\bar{B}C + A\bar{B}\bar{C} + AB\bar{C} + ABC$$
</div></li>
<li><strong>Maxterms ($M_i$) and Canonical Product-of-Sums (POS):</strong> A <strong>maxterm</strong> is a sum (OR) of all $n$ variables. Maxterm $M_i$ evaluates to <strong>0</strong> for exactly one input combination whose binary representation equals index $i$. By De Morgan's theorem, each maxterm is the exact complement of the corresponding minterm:
<div class="math-display">
$$M_i = \overline{m_i}$$
</div>
Any function is uniquely defined as the logical product (AND) of its 0-generating maxterms:
<div class="math-display">
$$F(A, B, C) = \prod M(0, 2, 3, 5) = (A + B + C)(A + \bar{B} + C)(A + \bar{B} + \bar{C})(\bar{A} + B + \bar{C})$$
</div></li>
</ol>

<h4>2. Conversion Between Canonical SOP and POS</h4>
<p>Because the indices that do not belong to the minterm list $\sum m$ must generate 0s, they form the maxterm list $\prod M$:</p>
<div class="math-display">
$$F = \sum m(d_1, d_2, \dots) \iff F = \prod M(\text{remaining indices})$$
</div>
<p>Furthermore, the complement function $\bar{F}$ is simply the sum of all missing minterms:</p>
<div class="math-display">
$$\bar{F} = \sum m(\text{missing from } F) = \prod M(\text{present in } F)$$
</div>"""
        },
        {
            "id": "dig-3-2",
            "title": "Karnaugh Map (K-Map) Minimization & Don't Care Conditions",
            "simulation": "dig-kmap-minimizer-sim",
            "content": r"""<h4>1. Geometric Adjacency & Gray Code Ordering in K-Maps</h4>
<p>Maurice Karnaugh (1953) organized truth tables into a planar graphical grid termed the <strong>Karnaugh Map (K-map)</strong>. The rows and columns are arranged in <strong>reflected Gray code sequence</strong> ($00, 01, 11, 10$):</p>
<ul>
<li>Adjacent cells horizontally and vertically differ in <strong>exactly one literal</strong>.</li>
<li>The edges wrap around cyclically (toroidal topology): the leftmost column is geometrically adjacent to the rightmost column, and the top row is adjacent to the bottom row.</li>
<li>Four-corner cells ($m_0, m_2, m_8, m_{10}$ in a 4-variable map) are mutually adjacent and form a valid group of four.</li>
</ul>

<h4>2. Grouping Rules and Prime Implicant Extraction</h4>
<p>By applying the Boolean absorption identity $x y + x \bar{y} = x (y + \bar{y}) = x$, grouping adjacent cells containing 1s eliminates the differing literals:</p>
<ul>
<li>A group of $2^1 = 2$ adjacent cells (pair) eliminates <strong>1 literal</strong>.</li>
<li>A group of $2^2 = 4$ adjacent cells (quad) eliminates <strong>2 literals</strong>.</li>
<li>A group of $2^3 = 8$ adjacent cells (octet) eliminates <strong>3 literals</strong>.</li>
<li>A group of $2^k$ adjacent cells eliminates <strong>$k$ literals</strong>.</li>
</ul>
<p><strong>Fundamental K-Map Optimization Axioms:</strong></p>
<ol>
<li>Groups must be rectangular and contain a power-of-two number of cells ($1, 2, 4, 8, 16$).</li>
<li>Every 1 must be covered by at least one group.</li>
<li>Groups should be made as <strong>large as possible</strong> to maximize literal elimination.</li>
<li>The total number of groups must be <strong>minimized</strong> to minimize gate count.</li>
<li>A <strong>Prime Implicant (PI)</strong> is a group that cannot be combined with any other cells to form a larger group.</li>
<li>An <strong>Essential Prime Implicant (EPI)</strong> is a prime implicant that covers at least one '1' that is not covered by any other prime implicant. All EPIs <em>must</em> be included in the minimal sum.</li>
</ol>

<h4>3. Incompletely Specified Functions: Don't Care States ($\times$)</h4>
<p>In many digital circuits (e.g., BCD decoders), certain input combinations never occur physically (e.g., binary values $10 - 15$ in 4-bit BCD). The output for these combinations is immaterial and designated as a <strong>Don't Care ($\times$ or $d$)</strong>.</p>
<p>In K-map reduction, a Don't Care condition $\times$ may be treated as <strong>1</strong> if doing so allows a group to expand to a larger power-of-two size (eliminating more literals), or as <strong>0</strong> if it does not help enlarge any group. Don't Care cells are never grouped alone.</p>"""
        },
        {
            "id": "dig-3-3",
            "title": "Quine-McCluskey Tabulation & Prime Implicant Charts",
            "content": r"""<h4>1. Limitations of K-Maps and the Need for Algorithmic Reduction</h4>
<p>While Karnaugh maps are intuitive for 2, 3, and 4 variables, 5-variable maps require dual overlay planes, and 6-variable maps require 4 sub-cubes, becoming visually error-prone. For functions of $n \ge 6$ variables, algorithmic computer-aided design (CAD) relies on the <strong>Quine-McCluskey (Q-M) Tabulation Method</strong>.</p>

<h4>2. Step-by-Step Quine-McCluskey Algorithm</h4>
<ol>
<li><strong>Group by Hamming Weight:</strong> Express all minterms and don't cares in binary and partition them into groups based on the count of 1s (Hamming weight).</li>
<li><strong>Pairwise Comparison:</strong> Compare each term in group $k$ with every term in group $k+1$. If two terms differ in exactly one bit position, combine them by replacing that bit with a dash ($-$) and check off ($\checkmark$) both contributing terms:
<div class="math-display">
$$0101 \ (5) \text{ and } 0111 \ (7) \implies 01-1 \ (5, 7)$$
</div></li>
<li><strong>Iterative Expansion:</strong> Repeat the comparison process for 2-cell implicants, 4-cell implicants, etc., matching dashes in identical positions, until no further combinations are possible.</li>
<li><strong>Prime Implicants:</strong> All terms that remain unchecked at the end of the process are the <strong>Prime Implicants (PIs)</strong>.</li>
</ol>

<h4>3. Prime Implicant Selection Chart & Petrick's Method</h4>
<p>Construct a matrix where rows correspond to the PIs and columns correspond to the original function minterms (Don't Cares are omitted from columns):</p>
<ul>
<li>Place an $\times$ in each column covered by a given PI.</li>
<li>If a column contains only a single $\times$, the corresponding row is an <strong>Essential Prime Implicant (EPI)</strong>. Check this row and cross off all columns covered by it.</li>
<li>If uncovered minterms remain (cyclic prime implicant charts), apply <strong>Petrick's Method</strong>: formulate a product-of-sums Boolean expression $\prod (P_i + P_j + \dots)$ asserting that each column must be covered, and expand algebraically into SOP to identify the minimal literal solution.</li>
</ul>"""
        },
        {
            "id": "dig-3-4",
            "title": "Radix & Diminished Radix Complements: 1's & 2's Complement",
            "content": r"""<h4>1. Mathematical Definition of Radix Complements</h4>
<p>To perform binary subtraction using standard adder hardware (eliminating the need for separate borrow-subtractor units), modern ALUs utilize complement arithmetic. In base $r$ with $n$ digits:</p>
<ol>
<li><strong>Diminished Radix Complement ($r-1$'s Complement):</strong>
<div class="math-display">
$$(r - 1)\text{'s Complement of } N = (r^n - 1) - N$$
</div>
In binary ($r=2$), the $1$'s complement is $(2^n - 1) - N$, achieved simply by <strong>inverting every individual bit</strong> ($0 \to 1, 1 \to 0$). In decimal ($r=10$), the $9$'s complement is obtained by subtracting each digit from 9.</li>
<li><strong>Radix Complement ($r$'s Complement):</strong>
<div class="math-display">
$$r\text{'s Complement of } N = r^n - N = [(r^n - 1) - N] + 1 = (r - 1)\text{'s Complement} + 1$$
</div>
In binary, the <strong>2's complement</strong> is obtained by inverting all bits and adding 1:
<div class="math-display">
$$N_{2's} = \bar{N} + 1$$
</div>
Shortcut: Leave all least significant zeros and the first '1' unchanged; invert all remaining bits to the left.</li>
</ol>

<h4>2. Subtraction Using 2's Complement Arithmetic</h4>
<p>To compute $M - N$ for $n$-bit unsigned numbers, the ALU evaluates $M + (2^n - N) = M - N + 2^n$:</p>
<ul>
<li><strong>Case 1 ($M \ge N$):</strong> The sum produces an <strong>End Carry</strong> of $2^n$ ($C_{\text{out}} = 1$). Discarding the carry yields the correct positive difference $M - N$.</li>
<li><strong>Case 2 ($M < N$):</strong> No end carry occurs ($C_{\text{out}} = 0$). The result is negative and equals the 2's complement of the true magnitude: $-(2^n - \text{Sum})$.</li>
</ul>

<h4>3. Signed Binary Representation & Arithmetic Overflow</h4>
<p>In signed $n$-bit 2's complement representation, the Most Significant Bit (MSB) acts as the sign bit ($0 \leftrightarrow +, 1 \leftrightarrow -$):</p>
<div class="math-display">
$$\text{Range of Signed } n\text{-bit Integer: } -2^{n-1} \le X \le +2^{n-1} - 1$$
</div>
<p>For an 8-bit byte: $-128 \le X \le +127$. Crucially, 2's complement features a <strong>unique zero</strong> ($00000000_2$), unlike 1's complement which suffers from $+0$ and $-0$ ambiguities.</p>
<p><strong>Overflow Condition ($V$):</strong> When adding two numbers of identical sign, the magnitude may exceed the representable range. Hardware detects overflow via an XOR gate comparing the carry into the sign bit ($C_{n-1}$) with the carry out of the sign bit ($C_n$):</p>
<div class="math-display">
$$V = C_n \oplus C_{n-1}$$
</div>
<p>If $V = 1$, an arithmetic overflow exception is signaled.</p>"""
        },
        {
            "id": "dig-3-5",
            "title": "Adders & Subtractors: Half/Full Adders & Carry-Lookahead (CLA)",
            "simulation": "dig-adder-subtractor-sim",
            "content": r"""<h4>1. Half-Adder and Full-Adder Logic</h4>
<p>The elementary building blocks of binary addition:</p>
<ol>
<li><strong>Half-Adder (HA):</strong> Adds two 1-bit inputs $A$ and $B$, producing Sum $S$ and Carry $C$:
<div class="math-display">
$$S = A \oplus B, \quad C = A B$$
</div></li>
<li><strong>Full-Adder (FA):</strong> Adds three 1-bit inputs: operands $A, B$ and carry-in $C_{\text{in}}$:
<div class="math-display">
$$S = A \oplus B \oplus C_{\text{in}}$$
</div>
<div class="math-display">
$$C_{\text{out}} = A B + B C_{\text{in}} + A C_{\text{in}} = A B + C_{\text{in}}(A \oplus B)$$
</div>
A Full-Adder can be synthesized using two Half-Adders and one OR gate.</li>
</ol>

<h4>2. Ripple-Carry Parallel Adder Limitations</h4>
<p>An $n$-bit parallel adder cascades $n$ Full-Adders, with $C_{\text{out}, i}$ connected to $C_{\text{in}, i+1}$. While hardware cost is minimal, the critical path requires the carry bit to "ripple" sequentially through all $n$ stages:</p>
<div class="math-display">
$$t_{\text{ripple}} = n \cdot t_{\text{carry}}$$
</div>
<p>For a 64-bit adder with $t_{\text{carry}} = 1\text{ ns}$, the total propagation delay is $64\text{ ns}$, severely throttling CPU clock frequencies.</p>

<h4>3. Carry-Lookahead Adder (CLA) Acceleration</h4>
<p>To eliminate serial carry propagation, the Carry-Lookahead Adder generates all carry bits simultaneously in parallel using two auxiliary functions:</p>
<ul>
<li><strong>Carry Generate ($G_i$):</strong> $G_i = A_i B_i$ (a carry is generated inside stage $i$ regardless of carry-in).</li>
<li><strong>Carry Propagate ($P_i$):</strong> $P_i = A_i \oplus B_i$ (a carry-in to stage $i$ is propagated forward to stage $i+1$).</li>
</ul>
<p>Expressing stage carries recursively:</p>
<div class="math-display">
$$C_1 = G_0 + P_0 C_0$$
</div>
<div class="math-display">
$$C_2 = G_1 + P_1 C_1 = G_1 + P_1 G_0 + P_1 P_0 C_0$$
</div>
<div class="math-display">
$$C_3 = G_2 + P_2 G_1 + P_2 P_1 G_0 + P_2 P_1 P_0 C_0$$
</div>
<div class="math-display">
$$C_4 = G_3 + P_3 G_2 + P_3 P_2 G_1 + P_3 P_2 P_1 G_0 + P_3 P_2 P_1 P_0 C_0$$
</div>
<p>Each carry depends strictly on the input operands and initial carry $C_0$, bypassing intermediate stages. All carries are computed simultaneously within a constant <strong>two-gate delay</strong>, irrespective of word length.</p>"""
        },
        {
            "id": "dig-3-6",
            "title": "BCD Decimal Adders, Subtractors & Binary Multipliers",
            "content": r"""<h4>1. BCD Decimal Adder Architecture</h4>
<p>In a Binary Coded Decimal (BCD) adder, two 4-bit BCD digits ($A, B \in [0, 9]$) and carry-in $C_{\text{in}}$ are summed using a standard 4-bit binary adder. If the binary sum $K \le 9$, the result is a valid BCD digit. However, if the sum exceeds 9 ($10 \le K \le 19$), the 4-bit binary adder produces an invalid BCD codeword ($1010_2$ to $1111_2$) or an unrecorded carry:</p>
<ul>
<li><strong>Correction Condition:</strong> An invalid decimal state is flagged if:
<div class="math-display">
$$\text{Correction Carry } C_{\text{out}} = K_4 + S_3 S_2 + S_3 S_1$$
</div>
where $K_4$ is the binary carry-out, $S_3 S_2$ flags 12 and 13, and $S_3 S_1$ flags 10 and 11.</li>
<li><strong>Correction Circuit:</strong> Whenever $C_{\text{out}} = 1$, the hardware adds $6_{10} = 0110_2$ to the sum via a second 4-bit binary adder. Adding 6 skips the 6 invalid 4-bit states, correctly producing the lower BCD digit and propagating the decimal carry $C_{\text{out}} = 1$ to the next decade.</li>
</ul>

<h4>2. Controlled Adder/Subtractor Circuit</h4>
<p>A single hardware unit performs both binary addition and subtraction by routing operand $B$ through conditional XOR inverters controlled by mode bit $M$:</p>
<div class="math-display">
$$B_i^* = B_i \oplus M, \quad C_{\text{in}} = M$$
</div>
<ul>
<li>When $M = 0$: $B_i^* = B_i$ and $C_{\text{in}} = 0 \implies$ Evaluates $A + B$ (Addition).</li>
<li>When $M = 1$: $B_i^* = \bar{B}_i$ and $C_{\text{in}} = 1 \implies$ Evaluates $A + \bar{B} + 1 = A - B$ (2's complement Subtraction).</li>
</ul>

<h4>3. Binary Array Multipliers</h4>
<p>Multiplication of two unsigned binary numbers ($A = a_{m-1}\dots a_0$ and $B = b_{n-1}\dots b_0$) is synthesized as the accumulation of $m \times n$ partial products $P_{i,j} = a_i \cdot b_j$ generated by 2-input AND gates. In an $m \times n$ array multiplier, partial product rows are shifted and summed using a 2D matrix of full adders, yielding product bits with delay scaling linearly with word length.</p>"""
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
                    "math": r"\text{Rows } AB: 00, 01, 11, 10; \quad \text{Cols } CD: 00, 01, 11, 10. \implies m(1,3,7,11,15)=1; \ d(0,2,5)=\times; \ \text{Others}=0",
                    "explanation": "Fill K-map cells: m0=x, m1=1, m2=x, m3=1; m5=x, m7=1; m11=1; m15=1."
                },
                {
                    "stepName": "Step 2: Form Prime Implicant Groups Using Don't Cares",
                    "math": r"\text{Group 1 (Quad/Octet): Top row } (m_0, m_1, m_3, m_2) \text{ contains } (\times, 1, 1, \times). \text{ Combine with } (m_4=0, m_5=\times, m_7=1, m_6=0)? \text{ No.}",
                    "explanation": "Top row cells (0, 1, 3, 2) form a Quad of four cells: CD has all 4 states, AB = 00 -> Term: A'B'."
                },
                {
                    "stepName": "Step 3: Group the Vertical Column (m3, m7, m11, m15)",
                    "math": r"\text{Column } CD = 11: m_3, m_7, m_{11}, m_{15} \text{ are all 1s!} \implies \text{Column Quad covers all 4 cells} \to \text{Term: } C D",
                    "explanation": "Column CD=11 forms an essential quad covering 3, 7, 11, 15: eliminates A and B."
                },
                {
                    "stepName": "Step 4: Check Coverage of Minterm 1",
                    "math": r"m_1 \text{ is covered by Quad } (m_0, m_1, m_3, m_2) \to \bar{A}\bar{B}. \quad \text{Alternatively, Quad } (m_1, m_3, m_5, m_7) \text{ covers } 1, 3, 5, 7 \to \bar{A} D",
                    "explanation": "Choosing Quad (m1, m3, m5, m7) gives A'D. Column CD gives CD. Combined: F = A'D + CD = (A' + C)D."
                },
                {
                    "stepName": "Step 5: Compare Minimal SOP Options",
                    "math": r"F = \bar{A} D + C D = (\bar{A} + C) D \quad \text{or} \quad F = \bar{A}\bar{B} + C D",
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
                    "math": r"A = 01011000_2 \implies + (64 + 16 + 8) = +88_{10}. \quad B = 01100100_2 \implies + (64 + 32 + 4) = +100_{10}",
                    "explanation": "Both numbers have MSB = 0, representing positive decimal integers."
                },
                {
                    "stepName": "Step 2: Perform 8-bit Binary Addition",
                    "math": r"\begin{matrix} & 01011000 \quad (+88) \\ + & 01100100 \quad (+100) \\ \hline & 10111100 \end{matrix}",
                    "explanation": "Add bits from right to left: sum is 10111100_2."
                },
                {
                    "stepName": "Step 3: Evaluate Carries into and out of MSB",
                    "math": r"C_7 (\text{carry into bit 7}) = 1 \ (\text{from } 1 + 1 + 0 = 0 \text{ R } 1), \quad C_8 (\text{carry out of bit 7}) = 0 \ (\text{from } 0 + 0 + 1 = 1 \text{ R } 0)",
                    "explanation": "A carry of 1 entered the sign position (bit 7), but no carry exited bit 7."
                },
                {
                    "stepName": "Step 4: Compute Overflow Flag V",
                    "math": r"V = C_8 \oplus C_7 = 0 \oplus 1 = 1 \implies \text{OVERFLOW DETECTED!}",
                    "explanation": "Because V = 1, the arithmetic result is invalid."
                },
                {
                    "stepName": "Step 5: Physical Interpretation",
                    "math": r"\text{True sum: } +88 + 100 = +188_{10}. \quad \text{8-bit signed range: } [-128, +127]. \quad \text{Hardware interpretation of } 10111100_2 = -68_{10}",
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
                    "math": r"t_{\text{ripple}} = (n - 1) \cdot t_{\text{carry}} + t_{\text{sum}} = (16 - 1) \times 2\text{ ns} + 6\text{ ns} = 15 \times 2 + 6 = 36\text{ ns}",
                    "explanation": "The carry must ripple through 15 stages before the final stage generates its sum bit."
                },
                {
                    "stepName": "Step 2: Analyze 4-bit CLA Architecture Timing",
                    "math": r"t_{P,G} = 1\text{ gate delay } (2\text{ ns}), \quad t_{\text{carry, CLA}} = 2\text{ gate delays } (4\text{ ns}), \quad t_{\text{sum, CLA}} = 2\text{ gate delays } (4\text{ ns})",
                    "explanation": "Inside each 4-bit block, P and G terms take 2 ns; lookahead carry logic takes 4 ns."
                },
                {
                    "stepName": "Step 3: Compute Total CLA Delay Across 4 Blocks",
                    "math": r"t_{\text{total, CLA}} = t_{P,G} + (4 \text{ blocks} - 1) \cdot t_{\text{block carry}} + t_{\text{sum}} = 2\text{ ns} + (3 \times 4\text{ ns}) + 4\text{ ns} = 2 + 12 + 4 = 18\text{ ns}",
                    "explanation": "Evaluate total block lookahead propagation: 18 ns."
                },
                {
                    "stepName": "Step 4: Compute Speedup Factor",
                    "math": r"\text{Speedup} = \frac{t_{\text{ripple}}}{t_{\text{CLA}}} = \frac{36\text{ ns}}{18\text{ ns}} = 2.0 \times \quad (\text{100\% faster})",
                    "explanation": "For 32-bit and 64-bit word lengths, CLA speedup exceeds 4x to 8x."
                }
            ],
            "answer": "t_{\\text{ripple}} = 36\\text{ ns}, \\quad t_{\\text{CLA}} = 18\\text{ ns} \\implies \\text{Speedup Factor: } 2.0\\times"
        }
    ]
}

# ==========================================
# UNIT 4: Latches, Flip-Flops & Multivibrator Timing Circuits
# ==========================================
u4 = {
    "unitNumber": 4,
    "unitId": "unit4-flip-flops-multivibrators",
    "title": "Latches, Flip-Flops & Multivibrator Timing Circuits",
    "description": "Bistable memory primitives and relaxation oscillator timing: cross-coupled BJT transistor latches, active-LOW NAND and active-HIGH NOR latches; clocked level-triggered SR and D transparent latches; edge-triggered flip-flops (master-slave architecture, dynamic setup time t_su and hold time t_h); the JK flip-flop, race-around hazard elimination, characteristic equations Q(t+1), excitation tables, and T flip-flop conversion; multivibrator classes (astable, monostable, bistable) and Schmitt trigger hysteresis; the 555 integrated timer internal comparator architecture, astable frequency, and duty cycle design.",
    "sections": [
        {
            "id": "dig-4-1",
            "title": "Bistable Elements: Cross-Coupled Inverters & SR Latches",
            "content": r"""<h4>1. The Fundamental Bistable Circuit Principle</h4>
<p>While combinational circuits produce outputs that depend strictly on current inputs, <strong>sequential circuits</strong> incorporate memory elements whose outputs depend on both current inputs and the past sequence of states. The most primitive electronic memory cell is the <strong>bistable multivibrator</strong>, formed by cross-coupling two inverting stages with positive feedback ($A_v > 1$):</p>
<div class="math-display">
$$Q = \overline{\bar{Q}}, \quad \bar{Q} = \bar{Q}$$
</div>
<p>The circuit possesses two stable equilibrium states: State 1 ($Q=1, \bar{Q}=0$, "SET") and State 2 ($Q=0, \bar{Q}=1$, "RESET"). The intermediate state where both inverters operate in their linear amplification region ($V_{\text{in}} = V_{\text{out}} \approx V_{DD}/2$) is <strong>metastable</strong>; infinitesimal thermal noise forces the cell to regenerate into one of the two stable binary states.</p>

<h4>2. Active-HIGH NOR Latch</h4>
<p>Constructed by cross-coupling two 2-input NOR gates with inputs $S$ (Set) and $R$ (Reset):</p>
<div class="math-display">
$$Q_{n+1} = \overline{R + \bar{Q}_n}, \quad \bar{Q}_{n+1} = \overline{S + Q_n}$$
</div>
<ul>
<li>$S=0, R=0$: <strong>Hold / Memory State</strong> ($Q_{n+1} = Q_n$). Latches the previous bit indefinitely.</li>
<li>$S=1, R=0$: <strong>Set State</strong> ($Q_{n+1} = 1, \bar{Q}_{n+1} = 0$).</li>
<li>$S=0, R=1$: <strong>Reset State</strong> ($Q_{n+1} = 0, \bar{Q}_{n+1} = 1$).</li>
<li>$S=1, R=1$: <strong>Forbidden / Invalid State</strong>. Forces both outputs to $0$ ($Q = \bar{Q} = 0$), violating complementarity. If both inputs return simultaneously to $0$, race conditions lead to unpredictable metastable collapse.</li>
</ul>

<h4>3. Active-LOW NAND Latch</h4>
<p>Constructed by cross-coupling two 2-input NAND gates with active-LOW inputs $\bar{S}$ and $\bar{R}$:</p>
<div class="math-display">
$$Q_{n+1} = \overline{\bar{S} \cdot \bar{Q}_n}, \quad \bar{Q}_{n+1} = \overline{\bar{R} \cdot Q_n}$$
</div>
<ul>
<li>$\bar{S}=1, \bar{R}=1$: <strong>Hold State</strong>.</li>
<li>$\bar{S}=0, \bar{R}=1$: <strong>Set State</strong> ($Q=1$).</li>
<li>$\bar{S}=1, \bar{R}=0$: <strong>Reset State</strong> ($Q=0$).</li>
<li>$\bar{S}=0, \bar{R}=0$: <strong>Forbidden State</strong> ($Q = \bar{Q} = 1$).</li>
</ul>"""
        },
        {
            "id": "dig-4-2",
            "title": "Clocked Latches: Synchronous SR & Transparent D Latch",
            "content": r"""<h4>1. Clocked SR Latch</h4>
<p>To synchronize state transitions with a central clock signal ($CLK$), two steering NAND gates precede the basic NAND latch:</p>
<div class="math-display">
$$S^* = \overline{S \cdot CLK}, \quad R^* = \overline{R \cdot CLK}$$
</div>
<ul>
<li>When $CLK = 0$: $S^* = R^* = 1$. The latch remains frozen in its hold state regardless of $S$ and $R$.</li>
<li>When $CLK = 1$: $S^* = \bar{S}$ and $R^* = \bar{R}$. The latch responds directly to $S$ and $R$ inputs.</li>
</ul>

<h4>2. The Transparent D Latch</h4>
<p>To eliminate the forbidden $S=R=1$ hazard, an inverter is placed between the inputs ($R = \bar{S}$), creating the single-input <strong>Data or D Latch</strong> ($S = D, R = \bar{D}$):</p>
<div class="math-display">
$$Q_{n+1} = D \quad (\text{when } CLK = 1)$$
</div>
<ul>
<li><strong>Transparent Mode ($CLK = 1$):</strong> The output $Q$ tracks input $D$ continuously in real time with minimal gate delay. Any noise or glitches on $D$ propagate directly to $Q$.</li>
<li><strong>Latched Mode ($CLK = 0$):</strong> The output $Q$ freezes, holding the value present at $D$ at the instant the clock fell.</li>
</ul>"""
        },
        {
            "id": "dig-4-3",
            "title": "Edge-Triggered Flip-Flops: Master-Slave & Timing Windows",
            "simulation": "dig-flipflop-clock-sim",
            "content": r"""<h4>1. Edge-Triggering vs Level-Sensitivity</h4>
<p>A <strong>latch</strong> is level-sensitive: it responds continuously as long as the clock enable remains active. In contrast, an <strong>edge-triggered flip-flop</strong> samples its input and changes state <em>only</em> during an infinitesimal transition edge of the clock signal—either the <strong>positive (rising) edge</strong> ($0 \to 1$) or the <strong>negative (falling) edge</strong> ($1 \to 0$).</p>

<h4>2. Master-Slave Architecture</h4>
<p>A classic edge-triggered flip-flop cascades two clocked latches in series controlled by complementary clock phases:</p>
<ol>
<li><strong>Master Latch:</strong> Enabled when $CLK = 1$. Samples data input $D$ while the slave is disabled ($\overline{CLK} = 0$). Output $Q_M$ tracks $D$, but external output $Q$ remains isolated.</li>
<li><strong>Slave Latch:</strong> Enabled when $CLK$ transitions from $1 \to 0$ ($\overline{CLK} \to 1$). The master latch instantly freezes, and the slave copies the frozen state $Q_M$ to the external output $Q$.</li>
</ol>
<p>Because the master and slave are never enabled simultaneously, data cannot ripple through both stages in a single clock cycle, completely severing feedthrough loops in shift registers and counters.</p>

<h4>3. Dynamic Timing Parameters: Setup Time & Hold Time</h4>
<p>Reliable digital state capture requires strict adherence to dynamic timing windows:</p>
<ul>
<li><strong>Setup Time ($t_{su}$):</strong> The minimum duration that the data input $D$ must remain stable <em>before</em> the active clock edge arrives. Typically $1 - 5\text{ ns}$ (down to tens of picoseconds in deep submicron CMOS).</li>
<li><strong>Hold Time ($t_h$):</strong> The minimum duration that the data input $D$ must remain stable <em>after</em> the active clock edge has transitioned.</li>
<li><strong>Propagation Delay ($t_{pd} = t_{CLK \to Q}$):</strong> The time delay between the active clock edge and the appearance of the new valid state at output $Q$.</li>
<li><strong>Metastability Hazard:</strong> If input $D$ transitions within the forbidden setup/hold aperture ($t_{su} + t_h$), internal regenerative feedback can hang in an indeterminate analog voltage state for an unbounded duration before collapsing randomly to 0 or 1, causing catastrophic hardware crashes.</li>
</ul>"""
        },
        {
            "id": "dig-4-4",
            "title": "The JK Flip-Flop: Race-Around Elimination & T Flip-Flops",
            "content": r"""<h4>1. The Race-Around Condition Hazard</h4>
<p>In a level-triggered JK latch with inputs $J = K = 1$, the output toggles ($Q \to \bar{Q}$). If the clock pulse width $t_w$ is longer than the propagation delay of the flip-flop ($t_{pd}$):</p>
<div class="math-display">
$$t_{pd} < t_w$$
</div>
<p>the newly toggled output will feed back to the input gates while the clock is still HIGH, causing the output to toggle repeatedly back and forth ("race around") throughout the pulse duration $t_w$. The final state of $Q$ when the clock falls is completely unpredictable.</p>
<p><strong>Race-Around Elimination Methods:</strong></p>
<ol>
<li>Narrow clock pulses ($t_w < t_{pd}$, difficult to guarantee across temperature and process variations).</li>
<li><strong>Edge-Triggered Design:</strong> State transitions occur only during clock edges ($\sim 1\text{ ns}$).</li>
<li><strong>Master-Slave JK Flip-Flop:</strong> The master isolates inputs while the slave updates outputs.</li>
</ol>

<h4>2. Truth Table & Characteristic Equation of the JK Flip-Flop</h4>
<div class="table-responsive">
<table class="table table-bordered">
<thead>
<tr><th>$J$</th><th>$K$</th><th>$Q_{n+1}$</th><th>Operational Mode</th></tr>
</thead>
<tbody>
<tr><td>$0$</td><td>$0$</td><td>$Q_n$</td><td>Hold / No Change</td></tr>
<tr><td>$0$</td><td>$1$</td><td>$0$</td><td>Reset</td></tr>
<tr><td>$1$</td><td>$0$</td><td>$1$</td><td>Set</td></tr>
<tr><td>$1$</td><td>$1$</td><td>$\bar{Q}_n$</td><td>Toggle</td></tr>
</tbody>
</table>
</div>
<p>From the K-map of next-state $Q_{n+1}$, the <strong>Characteristic Equation</strong> is:</p>
<div class="math-display">
$$Q_{n+1} = J \bar{Q}_n + \bar{K} Q_n$$
</div>

<h4>3. The Toggle (T) Flip-Flop</h4>
<p>Formed by tying the $J$ and $K$ inputs together ($J = K = T$):</p>
<div class="math-display">
$$Q_{n+1} = T \bar{Q}_n + \bar{T} Q_n = T \oplus Q_n$$
</div>
<ul>
<li>When $T = 0$: $Q_{n+1} = Q_n$ (Hold).</li>
<li>When $T = 1$: $Q_{n+1} = \bar{Q}_n$ (Toggle). Divides the input clock frequency by exactly <strong>2</strong> ($f_{\text{out}} = f_{\text{clk}} / 2$), forming the foundational block for binary ripple counters.</li>
</ul>"""
        },
        {
            "id": "dig-4-5",
            "title": "Multivibrators: Astable, Monostable & Schmitt Triggers",
            "content": r"""<h4>1. Classification of Multivibrator Circuits</h4>
<p>Multivibrators are regenerative switching circuits categorized by their number of permanently stable states:</p>
<ol>
<li><strong>Bistable:</strong> Two permanently stable states (Flip-Flops, Latches). Requires an external trigger pulse to transition between states.</li>
<li><strong>Monostable (One-Shot):</strong> One stable state and one quasi-stable state. An incoming trigger pulse initiates a transition to the quasi-stable state, where it remains for a predetermined duration $\tau = R C \ln(2) \approx 0.693 R C$ before returning automatically to the stable state. Used for pulse widening, debouncing switches, and fixed-delay generation.</li>
<li><strong>Astable (Free-Running Oscillator):</strong> Zero stable states. The circuit oscillates continuously between two quasi-stable states without external excitation, generating square wave clock signals.</li>
</ol>

<h4>2. The Schmitt Trigger & Hysteresis</h4>
<p>Otto Schmitt (1937) invented the <strong>Schmitt Trigger</strong>, a comparator circuit with positive feedback that exhibits <strong>hysteresis</strong>—two distinct switching threshold voltages:</p>
<ul>
<li><strong>Upper Trigger Point ($V_{UTP}$):</strong> When input voltage rises, output remains HIGH until $V_{\text{in}} \ge V_{UTP}$, at which point it snaps sharply to LOW.</li>
<li><strong>Lower Trigger Point ($V_{LTP}$):</strong> When input voltage falls, output remains LOW until $V_{\text{in}} \le V_{LTP}$, at which point it snaps sharply back to HIGH.</li>
<li><strong>Hysteresis Band ($\Delta V_H = V_{UTP} - V_{LTP}$):</strong> Completely rejects electrical noise and slow input voltage transitions, preventing erratic multi-trigger ringing on clock inputs.</li>
</ul>"""
        },
        {
            "id": "dig-4-6",
            "title": "The 555 Integrated Timer: Internal Architecture & Astable Design",
            "simulation": "dig-555-timer-sim",
            "content": r"""<h4>1. Internal Architecture of the 555 Timer IC</h4>
<p>The iconic 555 timer (Signetics, 1971) contains 23 transistors, 2 diodes, and 16 resistors integrated on silicon, structured into four functional blocks:</p>
<ol>
<li><strong>Precision Resistor Divider:</strong> Three matched $5\text{ k}\Omega$ resistors establish internal reference voltages of $\frac{2}{3} V_{CC}$ and $\frac{1}{3} V_{CC}$ (hence the name "555").</li>
<li><strong>Threshold Comparator (Comp 1):</strong> Compares Pin 6 (Threshold) to $\frac{2}{3} V_{CC}$. If $V_{\text{thresh}} > \frac{2}{3} V_{CC}$, sets the internal flip-flop ($R=1$).</li>
<li><strong>Trigger Comparator (Comp 2):</strong> Compares Pin 2 (Trigger) to $\frac{1}{3} V_{CC}$. If $V_{\text{trig}} < \frac{1}{3} V_{CC}$, resets the internal flip-flop ($S=1$).</li>
<li><strong>RS Flip-Flop & Discharge Transistor ($Q_{\text{dis}}$):</strong> Drives output Pin 3 through a high-current totem-pole driver ($\pm 200\text{ mA}$) and controls Pin 7 (Discharge open-collector transistor to ground).</li>
</ol>

<h4>2. Astable Multivibrator Frequency & Duty Cycle Equations</h4>
<p>Connected with external timing resistors $R_A, R_B$ and capacitor $C$, the capacitor charges through $R_A + R_B$ toward $V_{CC}$ and discharges through $R_B$ toward ground:</p>
<ul>
<li><strong>Charge Interval ($t_{\text{high}}$):</strong> $V_C(t)$ rises from $\frac{1}{3} V_{CC}$ to $\frac{2}{3} V_{CC}$:
<div class="math-display">
$$t_{\text{high}} = (R_A + R_B) C \ln(2) \approx 0.693 (R_A + R_B) C$$
</div></li>
<li><strong>Discharge Interval ($t_{\text{low}}$):</strong> $V_C(t)$ falls from $\frac{2}{3} V_{CC}$ to $\frac{1}{3} V_{CC}$:
<div class="math-display">
$$t_{\text{low}} = R_B C \ln(2) \approx 0.693 R_B C$$
</div></li>
<li><strong>Total Oscillation Period ($T$):</strong>
<div class="math-display">
$$T = t_{\text{high}} + t_{\text{low}} = 0.693 (R_A + 2 R_B) C$$
</div></li>
<li><strong>Output Frequency ($f$):</strong>
<div class="math-display">
$$f = \frac{1}{T} = \frac{1.44}{(R_A + 2 R_B) C}$$
</div></li>
<li><strong>Duty Cycle ($D$):</strong>
<div class="math-display">
$$D = \frac{t_{\text{high}}}{T} = \frac{R_A + R_B}{R_A + 2 R_B} \times 100\%$$
</div>
Because $R_A > 0$, standard astable connections have $D > 50\%$. Connecting a steering diode across $R_B$ bypasses $R_B$ during charging, enabling $50\%$ or lower duty cycles ($t_{\text{high}} \approx 0.693 R_A C$).</li>
</ul>"""
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
                    "math": r"t_w = 40\text{ ns} > t_{pd} = 12\text{ ns} \implies \text{Condition for Race-Around: } t_w > t_{pd} \text{ IS MET!}",
                    "explanation": "Because the clock pulse remains HIGH longer than the propagation delay, outputs feed back to inputs while the clock is still enabled."
                },
                {
                    "stepName": "Step 2: Calculate Number of Output Toggles",
                    "math": r"N_{\text{toggles}} = \left\lfloor \frac{t_w}{t_{pd}} \right\rfloor = \left\lfloor \frac{40\text{ ns}}{12\text{ ns}} \right\rfloor = 3 \text{ complete toggles}",
                    "explanation": "The output toggles 3 times during the single pulse, leaving the final output unpredictable."
                },
                {
                    "stepName": "Step 3: Master-Slave Elimination Mechanism",
                    "math": r"\text{When } CLK=1: \text{ Master samples } (J, K), \text{ Slave is disabled}. \quad \text{When } CLK=0: \text{ Master is isolated}, \text{ Slave updates } Q.",
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
                    "math": r"T = \frac{1}{f} = \frac{1}{10.0 \times 10^3\text{ Hz}} = 100\text{ \mu s}",
                    "explanation": "Compute total period: 100 microseconds."
                },
                {
                    "stepName": "Step 2: Calculate High Time and Low Time",
                    "math": r"t_{\text{high}} = D \cdot T = 0.650 \times 100\text{ \mu s} = 65.0\text{ \mu s}, \quad t_{\text{low}} = T - t_{\text{high}} = 35.0\text{ \mu s}",
                    "explanation": "Calculate high and low durations."
                },
                {
                    "stepName": "Step 3: Solve for Resistor R_B",
                    "math": r"t_{\text{low}} = 0.693 R_B C \implies R_B = \frac{t_{\text{low}}}{0.693 C} = \frac{35.0 \times 10^{-6}\text{ s}}{0.693 \times (10.0 \times 10^{-9}\text{ F})} \approx 5050\text{ }\Omega = 5.05\text{ k}\Omega",
                    "explanation": "Evaluate R_B: approximately 5.05 kOhm (standard 5.1 kOhm)."
                },
                {
                    "stepName": "Step 4: Solve for Resistor R_A",
                    "math": r"t_{\text{high}} = 0.693 (R_A + R_B) C \implies R_A + R_B = \frac{65.0 \times 10^{-6}}{0.693 \times 10^{-8}} \approx 9380\text{ }\Omega \implies R_A = 9380 - 5050 = 4330\text{ }\Omega = 4.33\text{ k}\Omega",
                    "explanation": "Evaluate R_A: approximately 4.33 kOhm (standard 4.3 kOhm)."
                }
            ],
            "answer": "R_A = 4.33\\text{ k}\\Omega, \\quad R_B = 5.05\\text{ k}\\Omega, \\quad t_{\\text{high}} = 65.0\\text{ \\mu s}, \\quad t_{\\text{low}} = 35.0\\text{ \\mu s}"
        },
        {
            "id": "dig-p-4-3",
            "title": "Flip-Flop Conversion: Synthesis of D Flip-Flop Using a JK Flip-Flop",
            "statement": "Convert a standard JK flip-flop into a D-type flip-flop: (a) Construct the excitation table showing required $J$ and $K$ inputs for all four desired $Q_n \to Q_{n+1}$ state transitions under input $D$. (b) Derive the minimized Boolean equations for $J$ and $K$ in terms of $D$. (c) Draw the hardware gate connection logic.",
            "steps": [
                {
                    "stepName": "Step 1: Construct the Conversion Excitation Table",
                    "math": r"\begin{matrix} D & Q_n & Q_{n+1} & J & K \\ \hline 0 & 0 & 0 & 0 & \times \\ 0 & 1 & 0 & \times & 1 \\ 1 & 0 & 1 & 1 & \times \\ 1 & 1 & 1 & \times & 0 \end{matrix}",
                    "explanation": "Map desired transition Q_n -> Q_(n+1) to JK excitation rules."
                },
                {
                    "stepName": "Step 2: Derive Minimized K-Map Equations for J and K",
                    "math": r"J(D, Q_n): J(0,0)=0, J(1,0)=1, J(0,1)=\times, J(1,1)=\times \implies J = D",
                    "explanation": "K-map for J reduces to J = D."
                },
                {
                    "stepName": "Step 3: Derive Equation for K",
                    "math": r"K(D, Q_n): K(0,0)=\times, K(1,0)=\times, K(0,1)=1, K(1,1)=0 \implies K = \bar{D}",
                    "explanation": "K-map for K reduces to K = D_bar."
                },
                {
                    "stepName": "Step 4: Hardware Realization",
                    "math": r"J = D, \quad K = \bar{D} = \text{NOT}(D)",
                    "explanation": "A single NOT gate connecting D to K, with D connected directly to J, converts any JK flip-flop into a D flip-flop."
                }
            ],
            "answer": "J = D, \\quad K = \\bar{D} \\quad (\\text{Single Inverter between } J \\text{ and } K)"
        }
    ]
}

with open("dig_u3.json", "w", encoding="utf-8") as f:
    json.dump(u3, f, indent=2)
print("dig_u3.json created successfully!")

with open("dig_u4.json", "w", encoding="utf-8") as f:
    json.dump(u4, f, indent=2)
print("dig_u4.json created successfully!")
