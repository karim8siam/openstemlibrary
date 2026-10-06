window.COURSE_DATA = {
  "courseId": "basic-algebra",
  "courseTitle": "Basic Algebra: Complex Numbers, Theory of Equations, Matrices & Leontief Systems",
  "courseDescription": "An exhaustive, university honors-level digital textbook and interactive algebraic laboratory covering classical and modern algebraic foundations: Part A establishes the complex number field and trigonometric polynomials across two units (axiomatic construction of C, Argand plane geometry, modulus and complex conjugates, geometric and reverse triangle inequalities, polar and Euler exponential representations, complex loci for lines, circles, and Apollonian circles; De Moivre's theorem proof via induction, binomial expansions of cos(nθ) and sin(nθ), power reductions of cosⁿθ and sinⁿθ, geometry of n-th roots of complex numbers, primitive roots of unity, cyclic group structures, and cyclotomic polynomials). Part B establishes the theory of equations and series summation across three units (d'Alembert-Gauss Fundamental Theorem of Algebra, conjugate root pair theorem, Viète's formulas for cubic and quartic polynomials, elementary symmetric polynomials, Newton-Girard recursive power sum identities sₖ, polynomial Euclidean division, Horner's synthetic scheme, Descartes' rule of signs bounding real and non-real roots, root multiplicity derivative criteria, square-free GCD factorization, Tschirnhaus root shifts and transformations, reciprocal equations; mathematical induction, finite differences and telescoping sums, factorial polynomials, arithmetico-geometric progressions (AGP), partial fraction summation, and trigonometric series summation via the C + iS complex phasor method). Part C establishes matrix algebra, linear systems, and macroeconomic input-output analysis across three comprehensive units (matrix ring M_{m×n}, transpose, trace cyclic invariance, taxonomy of symmetric, skew-symmetric, orthogonal, Hermitian, skew-Hermitian, unitary, idempotent, and nilpotent matrices; axiomatic multilinear alternating determinants, Leibniz permutation formula, Laplace cofactor expansion, Cauchy-Binet multiplicativity det(AB) = det(A)det(B), classical adjugate inversion, Cramer's rule; elementary row operations, elementary matrices, row equivalence, Row Echelon Form, uniqueness of Reduced Row Echelon Form (RREF), row/column rank equality, Rank-Nullity theorem, Rouché-Capelli consistency theorem, Gauss-Jordan inversion [A | I] → [I | A⁻¹], block matrices and Schur complement inversion; and the Leontief Input-Output Economic Model: inter-industry technological consumption matrices, the Leontief balance equation (I - C)X = D, Hawkins-Simon economic viability conditions, Leontief inverse multipliers via Neumann series expansion, and the dual Leontief equilibrium price model). Accompanied by 8 interactive 60 FPS algebraic canvas calculators and 24 tiered solved university examination problems.",
  "units": [
    {
      "unit_id": "unit_1",
      "unit_title": "The Complex Number Field & Geometry of the Complex Plane",
      "unit_subtitle": "Field Axioms, Modulus-Conjugate Algebra, Triangle Inequalities, Polar Forms & Complex Loci",
      "sections": [
        {
          "id": "sec_1_1",
          "title": "Axiomatic Construction of the Complex Number Field",
          "content": "\n<h3>1. Algebraic Construction of $\\mathbb{C}$</h3>\n<p>\nThe set of real numbers $\\mathbb{R}$ is algebraically incomplete: polynomial equations such as $x^2 + 1 = 0$ possess no real roots. We construct the <strong>field of complex numbers</strong> $\\mathbb{C}$ as the set of ordered pairs of real numbers:\n$$\\mathbb{C} \\equiv \\{(x, y) \\in \\mathbb{R}^2\\}$$\nequipped with two binary operations, <em>addition</em> ($+$) and <em>multiplication</em> ($\\cdot$):\n</p>\n<div class=\"math-display\">\n$$(x_1, y_1) + (x_2, y_2) \\equiv (x_1 + x_2, \\; y_1 + y_2)$$\n$$(x_1, y_1) \\cdot (x_2, y_2) \\equiv (x_1 x_2 - y_1 y_2, \\; x_1 y_2 + x_2 y_1)$$\n</div>\n\n<h3>2. Verification of Field Axioms</h3>\n<p>\nThe algebraic structure $(\\mathbb{C}, +, \\cdot)$ satisfies all nine field axioms:\n<ul>\n  <li><strong>Additive Identity:</strong> $0_{\\mathbb{C}} = (0, 0)$. For any $z = (x, y)$, $z + 0_{\\mathbb{C}} = (x+0, y+0) = z$.</li>\n  <li><strong>Additive Inverse:</strong> For each $z = (x, y)$, $-z = (-x, -y)$, yielding $z + (-z) = (0, 0)$.</li>\n  <li><strong>Multiplicative Identity:</strong> $1_{\\mathbb{C}} = (1, 0)$. For any $z = (x, y)$, $(x, y)(1, 0) = (x\\cdot 1 - y\\cdot 0, x\\cdot 0 + y\\cdot 1) = (x, y)$.</li>\n  <li><strong>Multiplicative Inverse:</strong> For every non-zero $z = (x, y) \\ne (0, 0)$, $x^2 + y^2 > 0$. The inverse is:\n  $$z^{-1} = \\left(\\frac{x}{x^2 + y^2}, \\; \\frac{-y}{x^2 + y^2}\\right)$$\n  Direct calculation yields $z \\cdot z^{-1} = \\left(\\frac{x^2 + y^2}{x^2 + y^2}, \\; \\frac{-xy + yx}{x^2 + y^2}\\right) = (1, 0)$.</li>\n  <li><strong>Distributivity & Commutativity:</strong> Multiplication distributes over addition, and both operations are commutative and associative.</li>\n</ul>\n</p>\n\n<h3>3. Canonical Form and the Imaginary Unit</h3>\n<p>\nThe map $\\iota: \\mathbb{R} \\hookrightarrow \\mathbb{C}$ defined by $\\iota(x) = (x, 0)$ is an injective field homomorphism, allowing us to identify $\\mathbb{R}$ as a subfield of $\\mathbb{C}$. Defining the <strong>imaginary unit</strong> $i \\equiv (0, 1)$:\n$$i^2 = (0, 1) \\cdot (0, 1) = (0\\cdot 0 - 1\\cdot 1, \\; 0\\cdot 1 + 1\\cdot 0) = (-1, 0) \\equiv -1$$\nAny element $z = (x, y)$ can be written in the canonical Cartesian form:\n$$\\mathbf{z = (x, 0) + (0, y) = x(1, 0) + y(0, 1) = x + iy}$$\nwhere $x = \\text{Re}(z) \\in \\mathbb{R}$ is the <strong>real part</strong> and $y = \\text{Im}(z) \\in \\mathbb{R}$ is the <strong>imaginary part</strong>.\n</p>\n\n<h3>4. Non-Orderability of $\\mathbb{C}$</h3>\n<p>\n<strong>Theorem:</strong> The complex field $\\mathbb{C}$ cannot be endowed with the structure of an ordered field.<br>\n<em>Proof:</em> In any ordered field, squares of non-zero elements are strictly positive: $a \\ne 0 \\implies a^2 > 0$. Consequently, $1^2 = 1 > 0$, which implies $-1 < 0$. If $\\mathbb{C}$ were ordered, $i \\ne 0$ would force $i^2 > 0 \\implies -1 > 0$, contradicting $-1 < 0$. Hence, no compatible total order exists on $\\mathbb{C}$. $\\blacksquare$\n</p>\n"
        },
        {
          "id": "sec_1_2",
          "title": "The Argand Plane, Modulus & Complex Conjugation",
          "content": "\n<h3>1. The Argand Representation</h3>\n<p>\nJean-Robert Argand and Carl Friedrich Gauss introduced the geometric representation of $\\mathbb{C}$ as a two-dimensional Euclidean plane $\\mathbb{R}^2$: the horizontal axis represents the <strong>real axis</strong> ($\\text{Re}$), and the vertical axis represents the <strong>imaginary axis</strong> ($\\text{Im}$). Every complex number $z = x + iy$ corresponds to the unique point $P(x, y)$ or the position vector $\\vec{OP}$.\n</p>\n\n<h3>2. The Complex Conjugate</h3>\n<p>\nFor $z = x + iy \\in \\mathbb{C}$, its <strong>complex conjugate</strong> $\\bar{z}$ is defined by:\n$$\\mathbf{\\bar{z} \\equiv x - iy}$$\nGeometrically, $\\bar{z}$ is the orthogonal reflection of $z$ across the real axis.\n<strong>Fundamental Properties of Conjugation:</strong>\n<ul>\n  <li>$\\overline{z_1 \\pm z_2} = \\bar{z}_1 \\pm \\bar{z}_2$ and $\\overline{z_1 z_2} = \\bar{z}_1 \\bar{z}_2$.</li>\n  <li>$\\overline{(z_1 / z_2)} = \\bar{z}_1 / \\bar{z}_2$ for $z_2 \\ne 0$.</li>\n  <li>$\\overline{\\bar{z}} = z$.</li>\n  <li>$\\text{Re}(z) = \\frac{z + \\bar{z}}{2}, \\quad \\text{Im}(z) = \\frac{z - \\bar{z}}{2i}$.</li>\n  <li>$z \\in \\mathbb{R} \\iff z = \\bar{z}; \\quad z \\text{ is purely imaginary} \\iff z = -\\bar{z}$.</li>\n</ul>\n</p>\n\n<h3>3. The Modulus (Absolute Value)</h3>\n<p>\nThe <strong>modulus</strong> of $z = x + iy$, denoted $|z|$, is the Euclidean distance from the origin to $(x, y)$:\n$$\\mathbf{|z| \\equiv \\sqrt{x^2 + y^2} = \\sqrt{z \\bar{z}}}$$\nKey algebraic properties:\n<ul>\n  <li>$|z| \\ge 0$, and $|z| = 0 \\iff z = 0$.</li>\n  <li>$|z| = |\\bar{z}| = |-z| = |-\\bar{z}|$.</li>\n  <li>$z \\bar{z} = |z|^2$. Thus, division can be computed algebraically as $\\frac{w}{z} = \\frac{w \\bar{z}}{|z|^2}$.</li>\n  <li>$|z_1 z_2| = |z_1| |z_2|$. <em>Proof:</em> $|z_1 z_2|^2 = (z_1 z_2)\\overline{(z_1 z_2)} = z_1 z_2 \\bar{z}_1 \\bar{z}_2 = (z_1 \\bar{z}_1)(z_2 \\bar{z}_2) = |z_1|^2 |z_2|^2$. Taking non-negative square roots gives $|z_1 z_2| = |z_1||z_2|$.</li>\n  <li>$\\left|\\frac{z_1}{z_2}\\right| = \\frac{|z_1|}{|z_2|}$ for $z_2 \\ne 0$.</li>\n</ul>\n</p>\n"
        },
        {
          "id": "sec_1_3",
          "title": "The Triangle Inequality & Vector Geometry",
          "content": "\n<h3>1. The Fundamental Triangle Inequality</h3>\n<p>\n<strong>Theorem:</strong> For any two complex numbers $z_1, z_2 \\in \\mathbb{C}$:\n$$\\mathbf{|z_1 + z_2| \\le |z_1| + |z_2|}$$\n<em>Rigorous Proof:</em>\nExpanding the squared modulus:\n$$|z_1 + z_2|^2 = (z_1 + z_2)\\overline{(z_1 + z_2)} = (z_1 + z_2)(\\bar{z}_1 + \\bar{z}_2) = z_1 \\bar{z}_1 + z_1 \\bar{z}_2 + z_2 \\bar{z}_1 + z_2 \\bar{z}_2$$\nSince $z_2 \\bar{z}_1 = \\overline{z_1 \\bar{z}_2}$, their sum is $2\\text{Re}(z_1 \\bar{z}_2)$:\n$$|z_1 + z_2|^2 = |z_1|^2 + 2\\text{Re}(z_1 \\bar{z}_2) + |z_2|^2$$\nFor any complex number $w$, $\\text{Re}(w) \\le |w|$. Therefore:\n$$\\text{Re}(z_1 \\bar{z}_2) \\le |z_1 \\bar{z}_2| = |z_1||\\bar{z}_2| = |z_1||z_2|$$\nSubstituting this upper bound:\n$$|z_1 + z_2|^2 \\le |z_1|^2 + 2|z_1||z_2| + |z_2|^2 = (|z_1| + |z_2|)^2$$\nTaking the positive square root on both sides yields:\n$$|z_1 + z_2| \\le |z_1| + |z_2| \\quad \\blacksquare$$\n</p>\n\n<h3>2. Condition for Equality</h3>\n<p>\nEquality holds if and only if $\\text{Re}(z_1 \\bar{z}_2) = |z_1 \\bar{z}_2|$, which requires $z_1 \\bar{z}_2$ to be a non-negative real number. If $z_2 \\ne 0$, this means:\n$$\\frac{z_1}{z_2} = \\frac{z_1 \\bar{z}_2}{|z_2|^2} = \\lambda \\ge 0$$\nGeometrically, equality holds if and only if the vectors $z_1$ and $z_2$ lie on the same ray emanating from the origin (same direction).\n</p>\n\n<h3>3. The Reverse Triangle Inequality</h3>\n<p>\n<strong>Theorem:</strong> For any $z_1, z_2 \\in \\mathbb{C}$:\n$$\\mathbf{||z_1| - |z_2|| \\le |z_1 - z_2|}$$\n<em>Proof:</em> Write $z_1 = (z_1 - z_2) + z_2$. By the triangle inequality:\n$$|z_1| = |(z_1 - z_2) + z_2| \\le |z_1 - z_2| + |z_2| \\implies |z_1| - |z_2| \\le |z_1 - z_2|$$\nSimilarly, interchanging $z_1$ and $z_2$:\n$$|z_2| - |z_1| \\le |z_2 - z_1| = |z_1 - z_2| \\implies -(|z_1| - |z_2|) \\le |z_1 - z_2|$$\nCombining these two inequalities gives $||z_1| - |z_2|| \\le |z_1 - z_2|$. $\\blacksquare$\n</p>\n<p>\nCombining both results yields the complete bounds:\n$$\\mathbf{||z_1| - |z_2|| \\le |z_1 \\pm z_2| \\le |z_1| + |z_2|}$$\n</p>\n"
        },
        {
          "id": "sec_1_4",
          "title": "Polar Form, Euler's Formula & Argument Geometry",
          "content": "\n<h3>1. Modulus-Argument (Polar) Representation</h3>\n<p>\nLet $z = x + iy \\ne 0$. Introducing plane polar coordinates $x = r\\cos\\theta$ and $y = r\\sin\\theta$, where $r = |z| = \\sqrt{x^2 + y^2} > 0$:\n$$\\mathbf{z = r(\\cos\\theta + i\\sin\\theta)}$$\nThe angle $\\theta$ is the <strong>argument</strong> of $z$, denoted $\\arg(z)$. Because $\\sin$ and $\\cos$ are $2\\pi$-periodic, the argument is multi-valued:\n$$\\arg(z) = \\text{Arg}(z) + 2k\\pi, \\quad k \\in \\mathbb{Z}$$\nThe <strong>principal argument</strong> $\\text{Arg}(z)$ is uniquely chosen in the interval $(-\\pi, \\pi]$:\n$$\\text{Arg}(z) = \\begin{cases} \\arctan(y/x) & x > 0 \\\\ \\arctan(y/x) + \\pi & x < 0, \\; y \\ge 0 \\\\ \\arctan(y/x) - \\pi & x < 0, \\; y < 0 \\\\ \\pi/2 & x = 0, \\; y > 0 \\\\ -\\pi/2 & x = 0, \\; y < 0 \\end{cases}$$\n</p>\n\n<h3>2. Euler's Formula</h3>\n<p>\nBy expanding the complex exponential function via its Taylor series:\n$$e^{i\\theta} = \\sum_{n=0}^\\infty \\frac{(i\\theta)^n}{n!} = \\sum_{k=0}^\\infty \\frac{(-1)^k \\theta^{2k}}{(2k)!} + i \\sum_{k=0}^\\infty \\frac{(-1)^k \\theta^{2k+1}}{(2k+1)!} = \\cos\\theta + i\\sin\\theta$$\nThis gives Euler's celebrated representation:\n$$\\mathbf{z = r e^{i\\theta}}$$\n</p>\n\n<h3>3. Multiplication and Division in Polar Form</h3>\n<p>\nLet $z_1 = r_1 e^{i\\theta_1}$ and $z_2 = r_2 e^{i\\theta_2}$. Then:\n$$z_1 z_2 = r_1 r_2 e^{i(\\theta_1 + \\theta_2)} = r_1 r_2 [\\cos(\\theta_1 + \\theta_2) + i\\sin(\\theta_1 + \\theta_2)]$$\n$$\\frac{z_1}{z_2} = \\frac{r_1}{r_2} e^{i(\\theta_1 - \\theta_2)} = \\frac{r_1}{r_2} [\\cos(\\theta_1 - \\theta_2) + i\\sin(\\theta_1 - \\theta_2)]$$\n<strong>Geometric Interpretation:</strong>\nMultiplying $z_1$ by $z_2$ scales the magnitude of $z_1$ by $r_2$ and rotates the vector counterclockwise by angle $\\theta_2$. In particular, multiplying any complex number by $i = e^{i\\pi/2}$ performs an exact $90^\\circ$ counterclockwise rotation.\n</p>\n"
        },
        {
          "id": "sec_1_5",
          "title": "Complex Equations of Lines, Circles & Apollonian Loci",
          "content": "\n<h3>1. Equation of a Straight Line in $\\mathbb{C}$</h3>\n<p>\nA line in the Cartesian plane has the equation $Ax + By + C = 0$ ($A, B, C \\in \\mathbb{R}$). Substituting $x = \\frac{z + \\bar{z}}{2}$ and $y = \\frac{z - \\bar{z}}{2i}$:\n$$A\\left(\\frac{z + \\bar{z}}{2}\\right) + B\\left(\\frac{z - \\bar{z}}{2i}\\right) + C = 0 \\iff \\left(\\frac{A - iB}{2}\\right)z + \\left(\\frac{A + iB}{2}\\right)\\bar{z} + C = 0$$\nDefining the complex coefficient $\\alpha \\equiv \\frac{A + iB}{2} \\in \\mathbb{C}$ and real constant $\\beta \\equiv C \\in \\mathbb{R}$:\n$$\\mathbf{\\bar{\\alpha} z + \\alpha \\bar{z} + \\beta = 0}$$\n</p>\n\n<h3>2. Equation of a Circle in $\\mathbb{C}$</h3>\n<p>\nA circle centered at $z_0 \\in \\mathbb{C}$ with radius $R > 0$ is the locus $|z - z_0| = R$. Squaring both sides:\n$$(z - z_0)\\overline{(z - z_0)} = R^2 \\iff z \\bar{z} - \\bar{z}_0 z - z_0 \\bar{z} + (|z_0|^2 - R^2) = 0$$\nThe general circle equation in $\\mathbb{C}$ is:\n$$\\mathbf{z \\bar{z} + \\bar{\\alpha} z + \\alpha \\bar{z} + k = 0, \\quad k \\in \\mathbb{R}, \\; |\\alpha|^2 - k > 0}$$\nwith center $z_c = -\\alpha$ and radius $R = \\sqrt{|\\alpha|^2 - k}$.\n</p>\n\n<h3>3. Apollonian Circles in the Complex Plane</h3>\n<p>\n<strong>Theorem:</strong> For two distinct points $z_1, z_2 \\in \\mathbb{C}$ and a constant $k > 0$, the locus of points satisfying:\n$$\\left|\\frac{z - z_1}{z - z_2}\\right| = k$$\nis:\n<ul>\n  <li>For $k = 1$: The perpendicular bisector of the segment connecting $z_1$ and $z_2$.</li>\n  <li>For $k \\ne 1$: A circle (termed the <em>Apollonian circle</em>) with center $z_c$ and radius $R$:\n  $$\\mathbf{z_c = \\frac{z_1 - k^2 z_2}{1 - k^2}, \\qquad R = \\frac{k |z_1 - z_2|}{|1 - k^2|}}$$\n  </li>\n</ul>\n</p>\n",
          "simulation": "algebra-complex-plane-sim",
          "simulations": [
            "algebra-complex-plane-sim"
          ]
        }
      ],
      "simulation": {
        "sim_id": "algebra-complex-plane-sim",
        "title": "Interactive Argand Diagram & Complex Operation Visualizer",
        "description": "Drag complex numbers z₁ and z₂ in the Gauss plane to interactively inspect vector addition (parallelogram rule), complex multiplication (moduli scaling and argument addition), and dynamic triangle inequality bounds."
      },
      "problems": [
        {
          "difficulty": "Tier 1: Foundational",
          "difficultyLabel": "Foundational Mechanics",
          "title": "Example 1.1: Modulus, Conjugate & Polar Transformation",
          "statement": "Given the complex expression $z = \\frac{(1 + i\\sqrt{3})^3}{(1 - i)^2}$: (a) Express $z$ in polar exponential form $r e^{i\\theta}$. (b) Compute the exact Cartesian form $x + iy$. (c) Determine $|z|$ and $\\bar{z}$.",
          "steps": [
            {
              "step": "Step 1: Convert Numerator and Denominator to Polar Form",
              "math": "1 + i\\sqrt{3} = 2\\left(\\frac{1}{2} + i\\frac{\\sqrt{3}}{2}\\right) = 2 e^{i\\pi/3} \\\\ 1 - i = \\sqrt{2}\\left(\\frac{1}{\\sqrt{2}} - \\frac{i}{\\sqrt{2}}\\right) = \\sqrt{2} e^{-i\\pi/4}",
              "explanation": "Compute modulus and argument for both numerator base and denominator base."
            },
            {
              "step": "Step 2: Apply Powers and Divide",
              "math": "(1 + i\\sqrt{3})^3 = (2 e^{i\\pi/3})^3 = 8 e^{i\\pi} \\\\ (1 - i)^2 = (\\sqrt{2} e^{-i\\pi/4})^2 = 2 e^{-i\\pi/2} \\\\ z = \\frac{8 e^{i\\pi}}{2 e^{-i\\pi/2}} = 4 e^{i(\\pi - (-\\pi/2))} = 4 e^{i(3\\pi/2)} = 4 e^{-i\\pi/2}",
              "explanation": "Subtract the argument of the denominator from the numerator argument, normalizing to $(-\\pi, \\pi]$."
            },
            {
              "step": "Step 3: Convert to Cartesian Form and Find Conjugate",
              "math": "z = 4[\\cos(-\\pi/2) + i\\sin(-\\pi/2)] = 4[0 - i] = -4i \\\\ \\bar{z} = 4i, \\quad |z| = 4",
              "explanation": "Expanding $e^{-i\\pi/2}$ gives a purely imaginary result $-4i$."
            }
          ],
          "answer": "z = 4 e^{-i\\pi/2} = -4i; \\quad |z| = 4, \\quad \\bar{z} = 4i"
        },
        {
          "difficulty": "Tier 2: Intermediate Exam",
          "difficultyLabel": "Intermediate University Exam",
          "title": "Example 1.2: Equilateral Triangle Inscribed in the Unit Circle",
          "statement": "Let $z_1, z_2, z_3 \\in \\mathbb{C}$ satisfy $|z_1| = |z_2| = |z_3| = 1$ and $z_1 + z_2 + z_3 = 0$. Prove that $z_1, z_2, z_3$ form the vertices of an equilateral triangle, and calculate $|z_1 - z_2|^2 + |z_2 - z_3|^2 + |z_3 - z_1|^2$.",
          "steps": [
            {
              "step": "Step 1: Compute Centroid and Circumcentre",
              "math": "\\text{Centroid } z_G = \\frac{z_1 + z_2 + z_3}{3} = \\frac{0}{3} = 0",
              "explanation": "Since $|z_1| = |z_2| = |z_3| = 1$, the circumcentre $z_O$ of the triangle is at the origin $0$. Thus the circumcentre and centroid coincide at the origin."
            },
            {
              "step": "Step 2: Equilateral Geometry via Coincident Centers",
              "math": "z_O = z_G = 0 \\implies \\text{The triangle is strictly equilateral!}",
              "explanation": "In Euclidean geometry, a triangle whose circumcentre and centroid coincide is necessarily equilateral."
            },
            {
              "step": "Step 3: Expand the Sum of Squared Side Lengths",
              "math": "|z_1 - z_2|^2 = (z_1 - z_2)(\\bar{z}_1 - \\bar{z}_2) = |z_1|^2 + |z_2|^2 - (z_1 \\bar{z}_2 + z_2 \\bar{z}_1) = 2 - 2\\text{Re}(z_1 \\bar{z}_2) \\\\ \\sum_{\\text{cyclic}} |z_1 - z_2|^2 = 6 - 2\\text{Re}(z_1 \\bar{z}_2 + z_2 \\bar{z}_3 + z_3 \\bar{z}_1) \\\\ |z_1 + z_2 + z_3|^2 = 0 \\implies |z_1|^2 + |z_2|^2 + |z_3|^2 + 2\\text{Re}(z_1 \\bar{z}_2 + z_2 \\bar{z}_3 + z_3 \\bar{z}_1) = 0 \\\\ 3 + 2\\text{Re}(z_1 \\bar{z}_2 + z_2 \\bar{z}_3 + z_3 \\bar{z}_1) = 0 \\implies 2\\text{Re}(\\dots) = -3 \\\\ \\sum_{\\text{cyclic}} |z_1 - z_2|^2 = 6 - (-3) = 9",
              "explanation": "The sum of the squares of the sides of the inscribed equilateral triangle equals 9, corresponding to individual side lengths of $\\sqrt{3}$."
            }
          ],
          "answer": "\\text{The vertices form an equilateral triangle with side lengths } \\sqrt{3}, \\text{ and the sum of squared sides is } 9."
        },
        {
          "difficulty": "Tier 3: Honors / Proof Challenge",
          "difficultyLabel": "Honors / Proof Challenge",
          "title": "Example 1.3: Derivation of the Apollonian Circle & Conjugate Orthogonality",
          "statement": "Given two distinct points $z_1, z_2 \\in \\mathbb{C}$ and $k \\in \\mathbb{R}^+ \\setminus \\{1\\}$: (a) Derive the equation of the Apollonius locus $|z - z_1| = k |z - z_2|$ in the form $|z - z_c|^2 = R^2$, explicitly finding the center $z_c$ and radius $R$. (b) Prove that any circle passing through $z_1$ and $z_2$ intersects this Apollonian circle orthogonally.",
          "steps": [
            {
              "step": "Step 1: Algebraic Reduction of the Locus",
              "math": "|z - z_1|^2 = k^2 |z - z_2|^2 \\iff (z - z_1)(\\bar{z} - \\bar{z}_1) = k^2 (z - z_2)(\\bar{z} - \\bar{z}_2) \\\\ z\\bar{z} - \\bar{z}_1 z - z_1 \\bar{z} + |z_1|^2 = k^2 [z\\bar{z} - \\bar{z}_2 z - z_2 \\bar{z} + |z_2|^2] \\\\ (1 - k^2) z\\bar{z} - (\\bar{z}_1 - k^2 \\bar{z}_2) z - (z_1 - k^2 z_2) \\bar{z} + (|z_1|^2 - k^2 |z_2|^2) = 0",
              "explanation": "Expand squared moduli and collect terms into the general complex circle equation."
            },
            {
              "step": "Step 2: Complete the Square to Determine Center and Radius",
              "math": "z\\bar{z} - \\bar{z}_c z - z_c \\bar{z} + \\frac{|z_1|^2 - k^2 |z_2|^2}{1 - k^2} = 0 \\quad \\text{where } z_c = \\frac{z_1 - k^2 z_2}{1 - k^2} \\\\ |z - z_c|^2 = |z_c|^2 - \\frac{|z_1|^2 - k^2 |z_2|^2}{1 - k^2} = \\frac{|z_1 - k^2 z_2|^2 - (1 - k^2)(|z_1|^2 - k^2 |z_2|^2)}{(1 - k^2)^2} \\\\ \\text{Numerator simplifies to: } k^2 |z_1 - z_2|^2 \\\\ R = \\frac{k |z_1 - z_2|}{|1 - k^2|}",
              "explanation": "Complete the square to obtain the canonical center $z_c$ and radius $R$."
            },
            {
              "step": "Step 3: Prove Orthogonality with Circles Passing Through z_1 and z_2",
              "math": "\\text{Power of } z_c \\text{ with respect to any circle } C_{12} \\text{ through } z_1, z_2 \\text{ is } (z_c - z_1)(z_c - z_2) \\\\ z_c - z_1 = \\frac{z_1 - k^2 z_2 - z_1(1 - k^2)}{1 - k^2} = \\frac{-k^2(z_2 - z_1)}{1 - k^2} = \\frac{k^2(z_1 - z_2)}{1 - k^2} \\\\ z_c - z_2 = \\frac{z_1 - k^2 z_2 - z_2(1 - k^2)}{1 - k^2} = \\frac{z_1 - z_2}{1 - k^2} \\\\ (z_c - z_1)(\\overline{z_c - z_2}) = \\frac{k^2 |z_1 - z_2|^2}{(1 - k^2)^2} = R^2",
              "explanation": "Because the product of distances from the center $z_c$ to the collinear points $z_1, z_2$ equals $R^2$, the points $z_1, z_2$ are inverse points with respect to the Apollonian circle. Consequently, any circle through $z_1, z_2$ cuts the Apollonian circle orthogonally."
            }
          ],
          "answer": "\\mathbf{z_c = \\frac{z_1 - k^2 z_2}{1 - k^2}}, \\quad \\mathbf{R = \\frac{k |z_1 - z_2|}{|1 - k^2|}}; \\quad \\text{Orthogonality follows from } (z_c - z_1)(\\overline{z_c - z_2}) = R^2."
        }
      ],
      "simulations": [
        "algebra-complex-plane-sim"
      ],
      "id": "unit1",
      "unitId": "unit1-algebra",
      "number": 1,
      "unitNumber": 1,
      "leadSummary": "Field Axioms, Modulus-Conjugate Algebra, Triangle Inequalities, Polar Forms & Complex Loci",
      "title": "The Complex Number Field & Geometry of the Complex Plane"
    },
    {
      "unit_id": "unit_2",
      "unit_title": "De Moivre’s Theorem, Roots of Unity & Trigonometric Expansions",
      "unit_subtitle": "Inductive Proof, Multiple-Angle Expansions, Power Reductions, Complex n-th Roots & Cyclotomic Geometry",
      "sections": [
        {
          "id": "sec_2_1",
          "title": "Statement and Rigorous Proof of De Moivre’s Theorem",
          "content": "\n<h3>1. Statement of De Moivre's Theorem</h3>\n<p>\nAbraham de Moivre established one of the foundational bridges between complex analysis and trigonometry:\n$$\\mathbf{(\\cos\\theta + i\\sin\\theta)^n = \\cos(n\\theta) + i\\sin(n\\theta)}$$\nIn compact Euler notation, this expresses the exponential property $(e^{i\\theta})^n = e^{in\\theta}$.\n</p>\n\n<h3>2. Rigorous Proof for Positive Integers ($n \\in \\mathbb{N}$)</h3>\n<p>\nWe prove the theorem by the Principle of Mathematical Induction on $n$:<br>\n<strong>Base Step ($n = 1$):</strong> $(\\cos\\theta + i\\sin\\theta)^1 = \\cos(1\\cdot\\theta) + i\\sin(1\\cdot\\theta)$, which is trivially true.<br>\n<strong>Inductive Hypothesis:</strong> Assume the identity holds for some positive integer $k \\ge 1$:\n$$(\\cos\\theta + i\\sin\\theta)^k = \\cos(k\\theta) + i\\sin(k\\theta)$$\n<strong>Inductive Step:</strong> Consider $n = k + 1$:\n$$(\\cos\\theta + i\\sin\\theta)^{k+1} = (\\cos\\theta + i\\sin\\theta)^k \\cdot (\\cos\\theta + i\\sin\\theta)$$\nUsing the inductive hypothesis:\n$$= [\\cos(k\\theta) + i\\sin(k\\theta)] [\\cos\\theta + i\\sin\\theta]$$\nExpanding the complex multiplication:\n$$= [\\cos(k\\theta)\\cos\\theta - \\sin(k\\theta)\\sin\\theta] + i[\\sin(k\\theta)\\cos\\theta + \\cos(k\\theta)\\sin\\theta]$$\nApplying standard trigonometric angle-addition identities:\n$$\\cos(k\\theta)\\cos\\theta - \\sin(k\\theta)\\sin\\theta = \\cos((k+1)\\theta)$$\n$$\\sin(k\\theta)\\cos\\theta + \\cos(k\\theta)\\sin\\theta = \\sin((k+1)\\theta)$$\nThus:\n$$(\\cos\\theta + i\\sin\\theta)^{k+1} = \\cos((k+1)\\theta) + i\\sin((k+1)\\theta)$$\nBy induction, the theorem is proved for all $n \\in \\mathbb{N}$. $\\blacksquare$\n</p>\n\n<h3>3. Extension to Negative Integers and Rational Powers</h3>\n<p>\n<strong>Case $n = 0$:</strong> $(\\cos\\theta + i\\sin\\theta)^0 = 1 = \\cos 0 + i\\sin 0$.<br>\n<strong>Case $n = -m$ where $m \\in \\mathbb{N}$:</strong>\n$$(\\cos\\theta + i\\sin\\theta)^{-m} = \\frac{1}{(\\cos\\theta + i\\sin\\theta)^m} = \\frac{1}{\\cos(m\\theta) + i\\sin(m\\theta)}$$\nMultiplying numerator and denominator by $\\cos(m\\theta) - i\\sin(m\\theta)$:\n$$= \\frac{\\cos(m\\theta) - i\\sin(m\\theta)}{\\cos^2(m\\theta) + \\sin^2(m\\theta)} = \\cos(-m\\theta) + i\\sin(-m\\theta) = \\cos(n\\theta) + i\\sin(n\\theta)$$\n<strong>Rational Powers $n = p/q$ ($q > 0$):</strong> One of the values of $(\\cos\\theta + i\\sin\\theta)^{p/q}$ is $\\cos(p\\theta/q) + i\\sin(p\\theta/q)$, with exactly $q$ distinct complex values given by $\\cos\\left(\\frac{p\\theta + 2k\\pi}{q}\\right) + i\\sin\\left(\\frac{p\\theta + 2k\\pi}{q}\\right)$ for $k = 0, 1, \\dots, q-1$.\n</p>\n"
        },
        {
          "id": "sec_2_2",
          "title": "Expansions of $\\cos(n\theta)$ and $\\sin(n\theta)$ in Powers of $\\cos\theta$ and $\\sin\theta$",
          "content": "\n<h3>1. Binomial Expansion Technique</h3>\n<p>\nBy De Moivre's theorem, $\\cos(n\\theta) + i\\sin(n\\theta) = (\\cos\\theta + i\\sin\\theta)^n$. Expanding the right-hand side using the Binomial Theorem:\n$$(\\cos\\theta + i\\sin\\theta)^n = \\sum_{k=0}^n \\binom{n}{k} \\cos^{n-k}\\theta \\, (i\\sin\\theta)^k$$\nSince $i^k$ alternates signs for even powers ($i^0 = 1, i^2 = -1, i^4 = 1$) and yields imaginary units for odd powers ($i^1 = i, i^3 = -i, i^5 = i$), we equate real and imaginary parts.\n</p>\n\n<h3>2. Explicit Formulas</h3>\n<p>\n<strong>Expansion of $\\cos(n\\theta)$ (Real Part):</strong>\n$$\\mathbf{\\cos(n\\theta) = \\cos^n\\theta - \\binom{n}{2}\\cos^{n-2}\\theta\\sin^2\\theta + \\binom{n}{4}\\cos^{n-4}\\theta\\sin^4\\theta - \\dots}$$\nSubstituting $\\sin^2\\theta = 1 - \\cos^2\\theta$ expresses $\\cos(n\\theta)$ purely as a polynomial in $\\cos\\theta$ of degree $n$, matching the celebrated <strong>Chebyshev Polynomial of the First Kind</strong> $T_n(x)$ where $x = \\cos\\theta$: $\\cos(n\\theta) = T_n(\\cos\\theta)$.\n</p>\n<p>\n<strong>Expansion of $\\sin(n\\theta)$ (Imaginary Part):</strong>\n$$\\mathbf{\\sin(n\\theta) = \\binom{n}{1}\\cos^{n-1}\\theta\\sin\\theta - \\binom{n}{3}\\cos^{n-3}\\theta\\sin^3\\theta + \\binom{n}{5}\\cos^{n-5}\\theta\\sin^5\\theta - \\dots}$$\nDividing by $\\sin\\theta$ yields the <strong>Chebyshev Polynomial of the Second Kind</strong> $U_{n-1}(\\cos\\theta)$.\n</p>\n\n<h3>3. Expansion of $\\tan(n\\theta)$</h3>\n<p>\nTaking the quotient $\\frac{\\sin(n\\theta)}{\\cos(n\\theta)}$ and dividing both numerator and denominator by $\\cos^n\\theta$:\n$$\\mathbf{\\tan(n\\theta) = \\frac{\\binom{n}{1}\\tan\\theta - \\binom{n}{3}\\tan^3\\theta + \\binom{n}{5}\\tan^5\\theta - \\dots}{1 - \\binom{n}{2}\\tan^2\\theta + \\binom{n}{4}\\tan^4\\theta - \\dots}}$$\n</p>\n"
        },
        {
          "id": "sec_2_3",
          "title": "Expansions of $\\cos^n\theta$ and $\\sin^n\theta$ in Terms of Sines and Cosines of Multiple Angles",
          "content": "\n<h3>1. The Reciprocal Exponential Variables</h3>\n<p>\nLet $x = e^{i\\theta} = \\cos\\theta + i\\sin\\theta$. Then $\\frac{1}{x} = e^{-i\\theta} = \\cos\\theta - i\\sin\\theta$.<br>\nAdding and subtracting these relations:\n$$\\mathbf{2\\cos\\theta = x + \\frac{1}{x}, \\qquad 2i\\sin\\theta = x - \\frac{1}{x}}$$\nMore generally, for any integer $k \\ge 1$:\n$$\\mathbf{2\\cos(k\\theta) = x^k + \\frac{1}{x^k}, \\qquad 2i\\sin(k\\theta) = x^k - \\frac{1}{x^k}}$$\n</p>\n\n<h3>2. Systematic Power Reduction for $\\cos^n\\theta$</h3>\n<p>\nRaising $2\\cos\\theta$ to the $n$-th power and applying the Binomial Theorem:\n$$(2\\cos\\theta)^n = \\left(x + \\frac{1}{x}\\right)^n = \\sum_{k=0}^n \\binom{n}{k} x^{n-k} \\left(\\frac{1}{x}\\right)^k = \\sum_{k=0}^n \\binom{n}{k} x^{n-2k}$$\nPairing terms symmetrically from the ends: $\\binom{n}{k} = \\binom{n}{n-k}$, so:\n$$x^{n-2k} + \\frac{1}{x^{n-2k}} = 2\\cos((n - 2k)\\theta)$$\nFor example, for $n = 4$:\n$$2^4 \\cos^4\\theta = \\left(x + \\frac{1}{x}\\right)^4 = \\left(x^4 + \\frac{1}{x^4}\\right) + 4\\left(x^2 + \\frac{1}{x^2}\\right) + 6$$\n$$16\\cos^4\\theta = 2\\cos(4\\theta) + 4[2\\cos(2\\theta)] + 6 \\implies \\mathbf{\\cos^4\\theta = \\frac{1}{8}[\\cos(4\\theta) + 4\\cos(2\\theta) + 3]}$$\n</p>\n\n<h3>3. Systematic Power Reduction for $\\sin^n\\theta$</h3>\n<p>\nSimilarly, raising $2i\\sin\\theta$ to the $n$-th power:\n$$(2i\\sin\\theta)^n = \\left(x - \\frac{1}{x}\\right)^n = \\sum_{k=0}^n (-1)^k \\binom{n}{k} x^{n-2k}$$\nFor odd $n$, the terms pair into $2i\\sin((n-2k)\\theta)$. For even $n$, the terms pair into $2\\cos((n-2k)\\theta)$, providing closed forms essential for calculus and physics integrals!\n</p>\n"
        },
        {
          "id": "sec_2_4",
          "title": "The $n$-th Roots of Arbitrary Complex Numbers",
          "content": "\n<h3>1. The Fundamental Root Equation</h3>\n<p>\nLet $w = R e^{i\\phi}$ be a given non-zero complex number, where $R = |w| > 0$ and $\\phi = \\text{Arg}(w)$. We seek all complex solutions $z = r e^{i\\theta}$ to the polynomial equation:\n$$z^n = w \\iff r^n e^{in\\theta} = R e^{i\\phi}$$\nEquating moduli and arguments:\n$$r^n = R \\implies r = \\sqrt[n]{R} \\in \\mathbb{R}^+$$\n$$n\\theta = \\phi + 2k\\pi \\implies \\theta_k = \\frac{\\phi + 2k\\pi}{n}, \\quad k \\in \\mathbb{Z}$$\n</p>\n\n<h3>2. The Exactly $n$ Distinct Complex Roots</h3>\n<p>\nAs $k$ ranges through $0, 1, 2, \\dots, n-1$, we obtain $n$ distinct values of $\\theta_k$ within a span of $2\\pi$. For $k \\ge n$, the arguments differ from previous ones by multiples of $2\\pi$, producing the identical complex numbers.\nThus, the equation $z^n = w$ possesses exactly $n$ distinct roots:\n$$\\mathbf{z_k = \\sqrt[n]{R} \\exp\\left(i \\frac{\\phi + 2k\\pi}{n}\\right) = \\sqrt[n]{R} \\left[ \\cos\\left(\\frac{\\phi + 2k\\pi}{n}\\right) + i\\sin\\left(\\frac{\\phi + 2k\\pi}{n}\\right) \\right]}$$\nfor $k = 0, 1, 2, \\dots, n-1$.\n</p>\n\n<h3>3. Geometric Configuration of Roots</h3>\n<p>\nIn the Argand plane:\n<ul>\n  <li>All $n$ roots have identical modulus $r = \\sqrt[n]{R}$, placing them on a circle of radius $\\sqrt[n]{R}$ centered at the origin.</li>\n  <li>The angular separation between adjacent roots is constantly $\\Delta\\theta = \\frac{2\\pi}{n}$.</li>\n  <li>The roots form the vertices of a <strong>regular $n$-sided polygon</strong> inscribed in the circle $|z| = \\sqrt[n]{R}$.</li>\n</ul>\n</p>\n"
        },
        {
          "id": "sec_2_5",
          "title": "The $n$-th Roots of Unity & Cyclotomic Geometry",
          "content": "\n<h3>1. The Roots of Unity</h3>\n<p>\nSetting $w = 1 = 1 \\cdot e^{i\\cdot 0}$, the solutions to $z^n = 1$ are the <strong>$n$-th roots of unity</strong>:\n$$\\mathbf{\\omega_k = e^{i\\frac{2k\\pi}{n}} = \\cos\\left(\\frac{2k\\pi}{n}\\right) + i\\sin\\left(\\frac{2k\\pi}{n}\\right), \\quad k = 0, 1, \\dots, n-1}$$\nDefining the fundamental root $\\omega \\equiv \\omega_1 = e^{i 2\\pi/n}$, the complete set of roots is:\n$$U_n = \\{1, \\omega, \\omega^2, \\omega^3, \\dots, \\omega^{n-1}\\}$$\nUnder complex multiplication, $(U_n, \\cdot)$ forms a finite <strong>cyclic group</strong> of order $n$ isomorphic to $\\mathbb{Z}/n\\mathbb{Z}$.\n</p>\n\n<h3>2. The Fundamental Algebraic Identities</h3>\n<p>\n<ul>\n  <li><strong>Sum of Roots Identity:</strong>\n  Since $z^n - 1 = (z - 1)(z^{n-1} + z^{n-2} + \\dots + z + 1) = 0$, for any root $\\omega \\ne 1$:\n  $$\\mathbf{1 + \\omega + \\omega^2 + \\dots + \\omega^{n-1} = \\sum_{k=0}^{n-1} \\omega^k = 0}$$\n  Geometrically, the centroid of the regular $n$-gon is at the origin $\\sum z_k / n = 0$.</li>\n  <li><strong>Product of Roots Identity:</strong>\n  $$\\prod_{k=0}^{n-1} \\omega_k = (-1)^{n-1}$$</li>\n</ul>\n</p>\n\n<h3>3. Primitive Roots and Cyclotomic Polynomials</h3>\n<p>\nA root $\\omega_k$ is a <strong>primitive $n$-th root of unity</strong> if its multiplicative order is exactly $n$—that is, $\\omega_k^m \\ne 1$ for all $1 \\le m < n$.<br>\n<strong>Theorem:</strong> $\\omega_k = e^{i 2k\\pi/n}$ is primitive if and only if $\\gcd(k, n) = 1$. The number of primitive $n$-th roots of unity is given by Euler's totient function $\\phi(n)$.<br>\nThe $n$-th <strong>cyclotomic polynomial</strong> $\\Phi_n(x)$ is defined as the monic polynomial whose roots are precisely the primitive $n$-th roots of unity:\n$$\\Phi_n(x) \\equiv \\prod_{\\substack{1 \\le k \\le n \\\\ \\gcd(k, n) = 1}} \\left(x - e^{i\\frac{2k\\pi}{n}}\\right)$$\nRemarkably, $\\Phi_n(x)$ always has integer coefficients and is irreducible over $\\mathbb{Q}$, with $x^n - 1 = \\prod_{d | n} \\Phi_d(x)$.\n</p>\n",
          "simulation": "algebra-demoivre-roots-sim",
          "simulations": [
            "algebra-demoivre-roots-sim"
          ]
        }
      ],
      "simulation": {
        "sim_id": "algebra-demoivre-roots-sim",
        "title": "Interactive n-th Roots of Unity & Regular Polygon Generator",
        "description": "Adjust the order slider n from 2 to 12 to visualize the n-th roots of unity forming regular polygons on the unit circle. Highlights primitive roots, root multiplication dynamics, and verified algebraic sums equal to zero."
      },
      "problems": [
        {
          "difficulty": "Tier 1: Foundational",
          "difficultyLabel": "Foundational Mechanics",
          "title": "Example 2.1: Expansions of Multiple Angles via Binomial De Moivre",
          "statement": "Use De Moivre's theorem to: (a) Express $\\cos(5\\theta)$ in terms of powers of $\\cos\\theta$. (b) Find all complex solutions to the equation $z^3 + 8 = 0$.",
          "steps": [
            {
              "step": "Step 1: Expand cos(5θ) via Binomial Theorem",
              "math": "\\cos(5\\theta) + i\\sin(5\\theta) = (\\cos\\theta + i\\sin\\theta)^5 = \\cos^5\\theta + 5i\\cos^4\\theta\\sin\\theta - 10\\cos^3\\theta\\sin^2\\theta - 10i\\cos^2\\theta\\sin^3\\theta + 5\\cos\\theta\\sin^4\\theta + i\\sin^5\\theta",
              "explanation": "Expand $(\\cos\\theta + i\\sin\\theta)^5$ using binomial coefficients $(1, 5, 10, 10, 5, 1)$."
            },
            {
              "step": "Step 2: Equate Real Parts and Eliminate sin²θ",
              "math": "\\cos(5\\theta) = \\cos^5\\theta - 10\\cos^3\\theta\\sin^2\\theta + 5\\cos\\theta\\sin^4\\theta \\\\ = \\cos^5\\theta - 10\\cos^3\\theta(1 - \\cos^2\\theta) + 5\\cos\\theta(1 - \\cos^2\\theta)^2 \\\\ = \\cos^5\\theta - 10\\cos^3\\theta + 10\\cos^5\\theta + 5\\cos\\theta(1 - 2\\cos^2\\theta + \\cos^4\\theta) \\\\ = 16\\cos^5\\theta - 20\\cos^3\\theta + 5\\cos\\theta",
              "explanation": "Substitute $\\sin^2\\theta = 1 - \\cos^2\\theta$ and collect like powers of $\\cos\\theta$."
            },
            {
              "step": "Step 3: Solve z³ + 8 = 0",
              "math": "z^3 = -8 = 8 e^{i\\pi} \\implies z_k = \\sqrt[3]{8} e^{i(\\pi + 2k\\pi)/3} = 2 e^{i(2k+1)\\pi/3}, \\quad k = 0, 1, 2 \\\\ z_0 = 2 e^{i\\pi/3} = 2\\left(\\frac{1}{2} + i\\frac{\\sqrt{3}}{2}\\right) = 1 + i\\sqrt{3} \\\\ z_1 = 2 e^{i\\pi} = -2 \\\\ z_2 = 2 e^{i 5\\pi/3} = 2\\left(\\frac{1}{2} - i\\frac{\\sqrt{3}}{2}\\right) = 1 - i\\sqrt{3}",
              "explanation": "Compute the three cube roots of $-8$ on the circle of radius 2."
            }
          ],
          "answer": "\\cos(5\\theta) = 16\\cos^5\\theta - 20\\cos^3\\theta + 5\\cos\\theta; \\quad \\text{Roots: } z \\in \\{-2, \\; 1 \\pm i\\sqrt{3}\\}."
        },
        {
          "difficulty": "Tier 2: Intermediate Exam",
          "difficultyLabel": "Intermediate University Exam",
          "title": "Example 2.2: Rational Fraction Polynomial Roots via De Moivre",
          "statement": "Solve the polynomial equation $(z + 1)^5 + (z - 1)^5 = 0$ over $\\mathbb{C}$, proving that all roots are purely imaginary.",
          "steps": [
            {
              "step": "Step 1: Rewrite into Ratio Form",
              "math": "(z + 1)^5 = -(z - 1)^5 \\iff \\left(\\frac{z + 1}{z - 1}\\right)^5 = -1 = e^{i\\pi}",
              "explanation": "Note that $z = 1$ is not a solution, so dividing by $(z - 1)^5$ is valid."
            },
            {
              "step": "Step 2: Find the 5th Roots of -1",
              "math": "\\frac{z + 1}{z - 1} = e^{i(2k + 1)\\pi/5}, \\quad k = 0, 1, 2, 3, 4",
              "explanation": "The five roots of $-1$ have unit magnitude and odd multiples of $\\pi/5$."
            },
            {
              "step": "Step 3: Solve for z and Prove Pure Imaginariness",
              "math": "\\text{Let } w_k = e^{i(2k+1)\\pi/5}. \\quad z_k = \\frac{w_k + 1}{w_k - 1} = \\frac{e^{i\\theta_k} + 1}{e^{i\\theta_k} - 1} \\\\ z_k = \\frac{e^{i\\theta_k/2}(e^{i\\theta_k/2} + e^{-i\\theta_k/2})}{e^{i\\theta_k/2}(e^{i\\theta_k/2} - e^{-i\\theta_k/2})} = \\frac{2\\cos(\\theta_k/2)}{2i\\sin(\\theta_k/2)} = -i \\cot\\left(\\frac{(2k+1)\\pi}{10}\\right) \\\\ \\text{For } k = 0, 1, 2, 3, 4: \\quad z_k \\in \\left\\{ -i\\cot(\\pi/10), \\; -i\\cot(3\\pi/10), \\; -i\\cot(5\\pi/10), \\; -i\\cot(7\\pi/10), \\; -i\\cot(9\\pi/10) \\right\\} \\\\ \\text{Since } \\cot(5\\pi/10) = \\cot(\\pi/2) = 0: \\quad z_2 = 0 \\\\ \\text{Since } \\cot(\\theta) \\in \\mathbb{R}, \\text{ every root } z_k \\text{ has zero real part and is purely imaginary!}",
              "explanation": "Express $z$ as $-i\\cot(\\theta_k/2)$, confirming that $\\text{Re}(z_k) = 0$ for all roots."
            }
          ],
          "answer": "z_k = -i\\cot\\left(\\frac{(2k+1)\\pi}{10}\\right) \\implies z \\in \\{0, \\; \\pm i\\cot(\\pi/10), \\; \\pm i\\cot(3\\pi/10)\\}; \\quad \\text{All roots are purely imaginary}."
        },
        {
          "difficulty": "Tier 3: Honors / Proof Challenge",
          "difficultyLabel": "Honors / Proof Challenge",
          "title": "Example 2.3: Closed Product Identity for Primitive Roots of Unity",
          "statement": "Let $\\omega_k = e^{i 2k\\pi/n}$ be the $n$-th roots of unity for $n \\ge 2$. (a) Prove that $\\prod_{k=1}^{n-1} (1 - \\omega_k) = n$. (b) Deduce the celebrated trigonometric product theorem: $\\prod_{k=1}^{n-1} \\sin\\left(\\frac{k\\pi}{n}\\right) = \\frac{n}{2^{n-1}}$.",
          "steps": [
            {
              "step": "Step 1: Factor Polynomial zⁿ - 1",
              "math": "z^n - 1 = (z - 1)\\prod_{k=1}^{n-1} (z - \\omega_k) \\\\ \\frac{z^n - 1}{z - 1} = z^{n-1} + z^{n-2} + \\dots + z + 1 = \\prod_{k=1}^{n-1} (z - \\omega_k)",
              "explanation": "Divide $z^n - 1$ by $z - 1$ to form the cyclotomic product of the non-trivial roots."
            },
            {
              "step": "Step 2: Evaluate at z = 1",
              "math": "\\lim_{z \\to 1} \\frac{z^n - 1}{z - 1} = 1^{n-1} + 1^{n-2} + \\dots + 1 = n \\\\ \\prod_{k=1}^{n-1} (1 - \\omega_k) = n",
              "explanation": "Setting $z = 1$ establishes the first fundamental product identity."
            },
            {
              "step": "Step 3: Relate (1 - ω_k) to Sine Function",
              "math": "1 - \\omega_k = 1 - e^{i 2k\\pi/n} = e^{i k\\pi/n} (e^{-i k\\pi/n} - e^{i k\\pi/n}) = -2i e^{i k\\pi/n} \\sin\\left(\\frac{k\\pi}{n}\\right) \\\\ |1 - \\omega_k| = |-2i| |e^{i k\\pi/n}| \\left|\\sin\\left(\\frac{k\\pi}{n}\\right)\\right| = 2\\sin\\left(\\frac{k\\pi}{n}\\right) \\quad \\left(\\text{since } 0 < \\frac{k\\pi}{n} < \\pi \\implies \\sin > 0\\right) \\\\ \\prod_{k=1}^{n-1} |1 - \\omega_k| = \\prod_{k=1}^{n-1} \\left[2\\sin\\left(\\frac{k\\pi}{n}\\right)\\right] = 2^{n-1} \\prod_{k=1}^{n-1} \\sin\\left(\\frac{k\\pi}{n}\\right)",
              "explanation": "Take the absolute value of both sides and isolate the trigonometric product."
            },
            {
              "step": "Step 4: Conclude the Product Value",
              "math": "2^{n-1} \\prod_{k=1}^{n-1} \\sin\\left(\\frac{k\\pi}{n}\\right) = n \\implies \\prod_{k=1}^{n-1} \\sin\\left(\\frac{k\\pi}{n}\\right) = \\frac{n}{2^{n-1}} \\quad \\blacksquare",
              "explanation": "Divide by $2^{n-1}$ to complete the proof."
            }
          ],
          "answer": "\\prod_{k=1}^{n-1} (1 - \\omega_k) = n; \\qquad \\prod_{k=1}^{n-1} \\sin\\left(\\frac{k\\pi}{n}\\right) = \\frac{n}{2^{n-1}}."
        }
      ],
      "simulations": [
        "algebra-demoivre-roots-sim"
      ],
      "id": "unit2",
      "unitId": "unit2-algebra",
      "number": 2,
      "unitNumber": 2,
      "leadSummary": "Inductive Proof, Multiple-Angle Expansions, Power Reductions, Complex n-th Roots & Cyclotomic Geometry",
      "title": "De Moivre’s Theorem, Roots of Unity & Trigonometric Expansions"
    },
    {
      "unit_id": "unit_3",
      "unit_title": "Theory of Equations: Roots, Coefficients & Symmetric Functions",
      "unit_subtitle": "Fundamental Theorem of Algebra, Viète's Formulas, Symmetric Reductions & Newton-Girard Identities",
      "sections": [
        {
          "id": "sec_3_1",
          "title": "Fundamental Theorem of Algebra & Factorization",
          "content": "\n<h3>1. The Fundamental Theorem of Algebra</h3>\n<p>\n<strong>Theorem (d'Alembert–Gauss):</strong> Every non-constant single-variable polynomial with complex coefficients has at least one complex root.<br>\nAs an immediate corollary, any polynomial of degree $n \\ge 1$:\n$$P(x) = a_n x^n + a_{n-1} x^{n-1} + \\dots + a_1 x + a_0, \\quad a_n \\ne 0, \\; a_i \\in \\mathbb{C}$$\ncan be completely factored into linear factors over $\\mathbb{C}$:\n$$\\mathbf{P(x) = a_n (x - \\alpha_1)(x - \\alpha_2)\\cdots(x - \\alpha_n) = a_n \\prod_{i=1}^n (x - \\alpha_i)}$$\nwhere $\\alpha_1, \\alpha_2, \\dots, \\alpha_n \\in \\mathbb{C}$ are the $n$ roots (counted with multiplicity).\n</p>\n\n<h3>2. The Conjugate Pairs Theorem for Real Polynomials</h3>\n<p>\n<strong>Theorem:</strong> If $P(x)$ is a polynomial with real coefficients ($a_i \\in \\mathbb{R}$) and $\\alpha = u + iv$ is a complex root ($v \\ne 0$), then its complex conjugate $\\bar{\\alpha} = u - iv$ is also a root of $P(x)$ of identical multiplicity.<br>\n<em>Proof:</em> Since $P(\\alpha) = \\sum_{k=0}^n a_k \\alpha^k = 0$, taking complex conjugates yields:\n$$\\overline{P(\\alpha)} = \\overline{\\sum_{k=0}^n a_k \\alpha^k} = \\sum_{k=0}^n \\bar{a}_k (\\bar{\\alpha})^k = \\sum_{k=0}^n a_k (\\bar{\\alpha})^k = P(\\bar{\\alpha}) = \\bar{0} = 0$$\nThus $P(\\bar{\\alpha}) = 0$. $\\blacksquare$\n</p>\n<p>\nConsequently, every complex root pair yields an irreducible real quadratic factor:\n$$(x - \\alpha)(x - \\bar{\\alpha}) = x^2 - 2u x + (u^2 + v^2) \\in \\mathbb{R}[x]$$\nThis guarantees that any real polynomial can be factored over $\\mathbb{R}$ into linear and irreducible quadratic factors. In particular, every real polynomial of odd degree has at least one real root.\n</p>\n"
        },
        {
          "id": "sec_3_2",
          "title": "Viète's Formulas Relating Roots and Coefficients",
          "content": "\n<h3>1. General Formulation for Degree $n$</h3>\n<p>\nFrançois Viète discovered the universal algebraic relations connecting the roots $\\alpha_1, \\dots, \\alpha_n$ of a monic polynomial $x^n + p_1 x^{n-1} + p_2 x^{n-2} + \\dots + p_n = 0$ to its coefficients:\n$$\\prod_{i=1}^n (x - \\alpha_i) = x^n - \\left(\\sum \\alpha_i\\right)x^{n-1} + \\left(\\sum_{i < j} \\alpha_i \\alpha_j\\right)x^{n-2} - \\dots + (-1)^n (\\alpha_1 \\cdots \\alpha_n)$$\nEquating coefficients of identical powers of $x$:\n$$\\mathbf{p_k = (-1)^k e_k(\\alpha_1, \\dots, \\alpha_n), \\quad k = 1, 2, \\dots, n}$$\nwhere $e_k$ is the $k$-th elementary symmetric polynomial.\n</p>\n\n<h3>2. Explicit Relations for the Cubic Equation</h3>\n<p>\nFor the cubic polynomial $x^3 + p x^2 + q x + r = 0$ with roots $\\alpha, \\beta, \\gamma$:\n<div class=\"math-display\">\n$$\\mathbf{\\sum \\alpha = \\alpha + \\beta + \\gamma = -p}$$\n$$\\mathbf{\\sum \\alpha\\beta = \\alpha\\beta + \\beta\\gamma + \\gamma\\alpha = q}$$\n$$\\mathbf{\\alpha\\beta\\gamma = -r}$$\n</div>\n</p>\n\n<h3>3. Explicit Relations for the Quartic Equation</h3>\n<p>\nFor the quartic polynomial $x^4 + p x^3 + q x^2 + r x + s = 0$ with roots $\\alpha, \\beta, \\gamma, \\delta$:\n<div class=\"math-display\">\n$$\\mathbf{\\sum \\alpha = -p}$$\n$$\\mathbf{\\sum \\alpha\\beta = q}$$\n$$\\mathbf{\\sum \\alpha\\beta\\gamma = -r}$$\n$$\\mathbf{\\alpha\\beta\\gamma\\delta = s}$$\n</div>\nThese relations permit setting up auxiliary algebraic equations when roots satisfy known constraints (e.g., arithmetic, geometric, or harmonic progressions).\n</p>\n"
        },
        {
          "id": "sec_3_3",
          "title": "Elementary Symmetric Polynomials & Invariance",
          "content": "\n<h3>1. Definition of Symmetric Polynomials</h3>\n<p>\nA polynomial $f(x_1, x_2, \\dots, x_n)$ is called <strong>symmetric</strong> if it remains strictly invariant under every permutation $\\sigma \\in S_n$ of its variables:\n$$f(x_{\\sigma(1)}, x_{\\sigma(2)}, \\dots, x_{\\sigma(n)}) = f(x_1, x_2, \\dots, x_n)$$\n</p>\n\n<h3>2. The Elementary Symmetric Polynomials</h3>\n<p>\nThe elementary symmetric polynomials $e_1, e_2, \\dots, e_n$ in $n$ variables are defined as:\n$$e_1 = \\sum_{1 \\le i \\le n} x_i, \\quad e_2 = \\sum_{1 \\le i < j \\le n} x_i x_j, \\quad \\dots, \\quad e_n = x_1 x_2 \\cdots x_n$$\nwith generating function:\n$$\\prod_{i=1}^n (1 + t x_i) = 1 + e_1 t + e_2 t^2 + \\dots + e_n t^n = \\sum_{k=0}^n e_k t^k$$\n</p>\n\n<h3>3. The Fundamental Theorem of Symmetric Polynomials</h3>\n<p>\n<strong>Theorem:</strong> Every symmetric polynomial $f(x_1, \\dots, x_n)$ with coefficients in a ring $R$ can be written uniquely as a polynomial in the elementary symmetric polynomials $e_1, \\dots, e_n$ with coefficients in $R$:\n$$\\mathbf{f(x_1, \\dots, x_n) = P(e_1, e_2, \\dots, e_n)}$$\n<em>Significance:</em> Any symmetric combination of the roots of a polynomial equation can be evaluated purely in terms of the polynomial's given coefficients without ever explicitly solving for the roots!\n</p>\n"
        },
        {
          "id": "sec_3_4",
          "title": "Symmetric Functions of the Roots & Classical Reductions",
          "content": "\n<h3>1. Classical Symmetric Sums for Cubic Roots</h3>\n<p>\nLet $\\alpha, \\beta, \\gamma$ be the roots of $x^3 + p x^2 + q x + r = 0$, so $e_1 = -p$, $e_2 = q$, $e_3 = -r$.\nWe express classical symmetric combinations in terms of $p, q, r$:\n<ul>\n  <li><strong>Sum of Squares:</strong>\n  $$\\mathbf{\\sum \\alpha^2 \\equiv \\alpha^2 + \\beta^2 + \\gamma^2 = e_1^2 - 2e_2 = p^2 - 2q}$$</li>\n  <li><strong>Product-Cross Sum:</strong>\n  $$\\mathbf{\\sum \\alpha^2 \\beta = e_1 e_2 - 3e_3 = -pq + 3r}$$</li>\n  <li><strong>Sum of Cubes:</strong>\n  $$\\mathbf{\\sum \\alpha^3 = e_1^3 - 3e_1 e_2 + 3e_3 = -p^3 + 3pq - 3r}$$</li>\n  <li><strong>Sum of Squares of Differences:</strong>\n  $$(\\alpha - \\beta)^2 + (\\beta - \\gamma)^2 + (\\gamma - \\alpha)^2 = 2\\sum \\alpha^2 - 2\\sum \\alpha\\beta = 2(p^2 - 2q) - 2q = \\mathbf{2p^2 - 6q}$$</li>\n</ul>\n</p>\n\n<h3>2. The Polynomial Discriminant</h3>\n<p>\nThe <strong>discriminant</strong> of a polynomial $P(x)$ of degree $n$ with roots $\\alpha_1, \\dots, \\alpha_n$ is defined by:\n$$\\mathbf{\\Delta \\equiv a_n^{2n-2} \\prod_{1 \\le i < j \\le n} (\\alpha_i - \\alpha_j)^2}$$\nSince $\\Delta$ is symmetric in the roots, it is a polynomial in the coefficients. For the depressed cubic $x^3 + px + q = 0$, its roots satisfy:\n$$\\mathbf{\\Delta = -4p^3 - 27q^2}$$\nIf $\\Delta > 0$, the cubic has 3 distinct real roots; if $\\Delta = 0$, it has repeated roots; if $\\Delta < 0$, it has 1 real root and 2 non-real conjugate roots.\n</p>\n"
        },
        {
          "id": "sec_3_5",
          "title": "Sums of Powers of Roots & Newton-Girard Identities",
          "content": "\n<h3>1. Definition of Power Sums</h3>\n<p>\nFor a monic polynomial $P(x) = x^n + p_1 x^{n-1} + \\dots + p_n = 0$ with roots $\\alpha_1, \\dots, \\alpha_n$, we define the $k$-th <strong>power sum</strong> as:\n$$\\mathbf{s_k \\equiv \\sum_{i=1}^n \\alpha_i^k = \\alpha_1^k + \\alpha_2^k + \\dots + \\alpha_n^k}$$\nFor $k = 0$, $s_0 = n$.\n</p>\n\n<h3>2. The Newton-Girard Recurrence Relations</h3>\n<p>\nIsaac Newton and Albert Girard derived the recursive relations connecting power sums $s_k$ directly to the polynomial coefficients $p_1, \\dots, p_n$:\n<div class=\"math-display\">\n$$\\mathbf{s_k + p_1 s_{k-1} + p_2 s_{k-2} + \\dots + p_{k-1} s_1 + k p_k = 0, \\quad \\text{for } 1 \\le k \\le n}$$\n$$\\mathbf{s_k + p_1 s_{k-1} + p_2 s_{k-2} + \\dots + p_n s_{k-n} = 0, \\quad \\text{for } k > n}$$\n</div>\n</p>\n\n<h3>3. Derivation via Logarithmic Differentiation</h3>\n<p>\nWriting $P(x) = \\prod_{i=1}^n (x - \\alpha_i)$, taking the formal logarithmic derivative:\n$$\\frac{P'(x)}{P(x)} = \\sum_{i=1}^n \\frac{1}{x - \\alpha_i} = \\frac{1}{x} \\sum_{i=1}^n \\frac{1}{1 - \\alpha_i/x} = \\sum_{i=1}^n \\sum_{k=0}^\\infty \\frac{\\alpha_i^k}{x^{k+1}} = \\sum_{k=0}^\\infty \\frac{s_k}{x^{k+1}}$$\nMultiplying both sides by $P(x) = x^n + p_1 x^{n-1} + \\dots + p_n$ and equating coefficients of corresponding powers of $x$ establishes the Newton-Girard identities for all $k \\ge 1$. $\\blacksquare$\n</p>\n",
          "simulation": "algebra-viete-symmetric-sim",
          "simulations": [
            "algebra-viete-symmetric-sim"
          ]
        }
      ],
      "simulation": {
        "sim_id": "algebra-viete-symmetric-sim",
        "title": "Interactive Polynomial Roots & Viète Symmetric Invariant Explorer",
        "description": "Drag the real roots α, β, γ along the horizontal axis to dynamically reconstruct the cubic polynomial curve P(x). Live computes Viète coefficients, symmetric sums, and verifies Newton-Girard power sums s₁ through s₄."
      },
      "problems": [
        {
          "difficulty": "Tier 1: Foundational",
          "difficultyLabel": "Foundational Mechanics",
          "title": "Example 3.1: Cubic Roots in Arithmetic Progression",
          "statement": "Solve the cubic equation $x^3 - 12x^2 + 39x - 28 = 0$, given that its roots are in Arithmetic Progression (A.P.).",
          "steps": [
            {
              "step": "Step 1: Parametrize Roots in A.P.",
              "math": "\\text{Let the roots be } \\alpha = a - d, \\quad \\beta = a, \\quad \\gamma = a + d",
              "explanation": "Using symmetric parameterization simplifies the sum of roots."
            },
            {
              "step": "Step 2: Apply Viète's Formula for Sum of Roots",
              "math": "\\sum \\text{roots} = (a - d) + a + (a + d) = 3a = -(-12) = 12 \\implies a = 4",
              "explanation": "The sum eliminates the common difference $d$, directly giving middle root $a = 4$."
            },
            {
              "step": "Step 3: Apply Viète's Product Formula to Find d",
              "math": "\\text{Product of roots: } (a - d)a(a + d) = a(a^2 - d^2) = -(-28) = 28 \\\\ 4(16 - d^2) = 28 \\implies 16 - d^2 = 7 \\implies d^2 = 9 \\implies d = \\pm 3",
              "explanation": "Substitute $a = 4$ into the product relation and solve for $d$."
            },
            {
              "step": "Step 4: Compute All Roots",
              "math": "\\text{For } d = 3: \\quad \\alpha = 4 - 3 = 1, \\quad \\beta = 4, \\quad \\gamma = 4 + 3 = 7 \\\\ \\text{Check } \\sum \\alpha\\beta: 1\\cdot 4 + 4\\cdot 7 + 7\\cdot 1 = 4 + 28 + 7 = 39 \\quad \\checkmark",
              "explanation": "The roots are 1, 4, and 7, matching all coefficients."
            }
          ],
          "answer": "\\text{The roots of the equation are } x \\in \\{1, 4, 7\\}."
        },
        {
          "difficulty": "Tier 2: Intermediate Exam",
          "difficultyLabel": "Intermediate University Exam",
          "title": "Example 3.2: Symmetric Function Evaluation and Transformed Cubic",
          "statement": "If $\\alpha, \\beta, \\gamma$ are the roots of the cubic equation $x^3 + px + q = 0$, find: (a) The value of $\\sum \\frac{1}{\\alpha^2 + \\beta\\gamma}$. (b) The cubic equation whose roots are $y_1 = \\beta + \\gamma - \\alpha$, $y_2 = \\gamma + \\alpha - \\beta$, and $y_3 = \\alpha + \\beta - \\gamma$.",
          "steps": [
            {
              "step": "Step 1: Simplify Denominator via Viète Product",
              "math": "\\text{Since } \\sum \\alpha = 0, \\quad \\sum \\alpha\\beta = p, \\quad \\alpha\\beta\\gamma = -q \\\\ \\beta\\gamma = -\\frac{q}{\\alpha} \\implies \\alpha^2 + \\beta\\gamma = \\alpha^2 - \\frac{q}{\\alpha} = \\frac{\\alpha^3 - q}{\\alpha} \\\\ \\text{Since } \\alpha \\text{ satisfies } \\alpha^3 + p\\alpha + q = 0: \\quad \\alpha^3 - q = -p\\alpha - 2q \\\\ \\frac{1}{\\alpha^2 + \\beta\\gamma} = \\frac{\\alpha}{-p\\alpha - 2q}",
              "explanation": "Rewrite $\\beta\\gamma$ using the root equation $\\alpha^3 = -p\\alpha - q$."
            },
            {
              "step": "Step 2: Construct the Transformed Equation for y",
              "math": "\\text{Since } \\alpha + \\beta + \\gamma = 0: \\quad \\beta + \\gamma = -\\alpha \\\\ y_1 = -\\alpha - \\alpha = -2\\alpha, \\quad y_2 = -2\\beta, \\quad y_3 = -2\\gamma",
              "explanation": "Substitute $\\beta + \\gamma = -\\alpha$ to obtain the direct root transformation $y = -2x$."
            },
            {
              "step": "Step 3: Transform the Polynomial Equation",
              "math": "x = -\\frac{y}{2} \\implies \\left(-\\frac{y}{2}\\right)^3 + p\\left(-\\frac{y}{2}\\right) + q = 0 \\\\ -\\frac{y^3}{8} - \\frac{py}{2} + q = 0 \\iff y^3 + 4py - 8q = 0",
              "explanation": "Substitute $x = -y/2$ into the original cubic and multiply by $-8$."
            }
          ],
          "answer": "\\text{Transformed Cubic: } \\mathbf{y^3 + 4py - 8q = 0}; \\quad \\text{Roots are } -2\\alpha, -2\\beta, -2\\gamma."
        },
        {
          "difficulty": "Tier 3: Honors / Proof Challenge",
          "difficultyLabel": "Honors / Proof Challenge",
          "title": "Example 3.3: Recursive Newton-Girard Power Sums for a Quartic",
          "statement": "For the monic quartic equation $x^4 + p x^3 + q x^2 + r x + s = 0$ with roots $\\alpha_1, \\alpha_2, \\alpha_3, \\alpha_4$, use the Newton-Girard identities to derive explicit expressions for $s_1, s_2, s_3, s_4$, and prove that $s_4 = p^4 - 4p^2 q + 4pr + 2q^2 - 4s$.",
          "steps": [
            {
              "step": "Step 1: Compute s₁ and s₂ via Newton-Girard",
              "math": "k = 1: \\quad s_1 + p = 0 \\implies s_1 = -p \\\\ k = 2: \\quad s_2 + p s_1 + 2q = 0 \\implies s_2 = -p(-p) - 2q = p^2 - 2q",
              "explanation": "Apply $s_k + p_1 s_{k-1} + \\dots + k p_k = 0$ for $k = 1$ and $k = 2$."
            },
            {
              "step": "Step 2: Compute s₃",
              "math": "k = 3: \\quad s_3 + p s_2 + q s_1 + 3r = 0 \\\\ s_3 = -p(p^2 - 2q) - q(-p) - 3r = -p^3 + 2pq + pq - 3r = -p^3 + 3pq - 3r",
              "explanation": "Apply the recurrence for $k = 3$."
            },
            {
              "step": "Step 3: Compute s₄ and Conclude Proof",
              "math": "k = 4: \\quad s_4 + p s_3 + q s_2 + r s_1 + 4s = 0 \\\\ s_4 = -p s_3 - q s_2 - r s_1 - 4s \\\\ s_4 = -p(-p^3 + 3pq - 3r) - q(p^2 - 2q) - r(-p) - 4s \\\\ = (p^4 - 3p^2 q + 3pr) - (p^2 q - 2q^2) + pr - 4s \\\\ = p^4 - 4p^2 q + 4pr + 2q^2 - 4s \\quad \\blacksquare",
              "explanation": "Substitute $s_1, s_2, s_3$ into the order-4 recurrence relation and expand algebraically."
            }
          ],
          "answer": "\\mathbf{s_1 = -p}, \\quad \\mathbf{s_2 = p^2 - 2q}, \\quad \\mathbf{s_3 = -p^3 + 3pq - 3r}, \\quad \\mathbf{s_4 = p^4 - 4p^2 q + 4pr + 2q^2 - 4s}."
        }
      ],
      "simulations": [
        "algebra-viete-symmetric-sim"
      ],
      "id": "unit3",
      "unitId": "unit3-algebra",
      "number": 3,
      "unitNumber": 3,
      "leadSummary": "Fundamental Theorem of Algebra, Viète's Formulas, Symmetric Reductions & Newton-Girard Identities",
      "title": "Theory of Equations: Roots, Coefficients & Symmetric Functions"
    },
    {
      "unit_id": "unit_4",
      "unit_title": "Polynomial Division, Descartes' Rule of Signs & Transformations",
      "unit_subtitle": "Horner's Synthetic Division, Descartes' Sign Criteria, Multiple Root GCD Analysis & Reciprocal Solvers",
      "sections": [
        {
          "id": "sec_4_1",
          "title": "Euclidean Division Algorithm & Horner’s Synthetic Scheme",
          "content": "\n<h3>1. The Division Algorithm for Polynomials</h3>\n<p>\nFor any polynomial dividend $P(x)$ and non-zero divisor $D(x)$, there exist unique quotient $Q(x)$ and remainder $R(x)$ such that:\n$$\\mathbf{P(x) = D(x) Q(x) + R(x), \\quad \\text{where } \\deg(R) < \\deg(D) \\text{ or } R(x) = 0}$$\n<strong>Remainder Theorem:</strong> When divided by a linear factor $(x - c)$, the remainder is the constant $R = P(c)$.<br>\n<strong>Factor Theorem:</strong> A linear binomial $(x - c)$ is a factor of $P(x)$ if and only if $P(c) = 0$.\n</p>\n\n<h3>2. Horner’s Synthetic Division Algorithm</h3>\n<p>\nWilliam George Horner formalized a streamlined algorithm for dividing a polynomial $P(x) = a_n x^n + \\dots + a_0$ by $(x - c)$ using only $n$ multiplications and $n$ additions:\n$$\\begin{array}{c|cccccc}\nc & a_n & a_{n-1} & a_{n-2} & \\dots & a_1 & a_0 \\\\ \n  &     & c b_{n-1} & c b_{n-2} & \\dots & c b_1 & c b_0 \\\\ \\hline\n  & b_{n-1} & b_{n-2} & b_{n-3} & \\dots & b_0 & R\n\\end{array}$$\nwhere the recurrence is initialized by $b_{n-1} = a_n$ and generated by:\n$$\\mathbf{b_{k-1} = a_k + c \\, b_k, \\quad \\text{with remainder } R = P(c) = a_0 + c \\, b_0}$$\nThe quotient polynomial is $Q(x) = b_{n-1} x^{n-1} + b_{n-2} x^{n-2} + \\dots + b_0$.\n</p>\n"
        },
        {
          "id": "sec_4_2",
          "title": "Descartes’ Rule of Signs",
          "content": "\n<h3>1. Statement of Descartes’ Theorem</h3>\n<p>\nRené Descartes established an analytical bound on the real roots of a real polynomial $P(x) = a_n x^n + \\dots + a_0$:\n<ul>\n  <li>Let $V$ denote the number of <strong>sign variations</strong> between consecutive non-zero coefficients of $P(x)$.</li>\n  <li>The number of positive real roots $N_+$ of $P(x)$ is either equal to $V$ or less than $V$ by an even non-negative integer:\n  $$\\mathbf{N_+ = V - 2k, \\quad k \\in \\{0, 1, 2, \\dots\\}, \\quad N_+ \\le V}$$</li>\n  <li>The number of negative real roots $N_-$ of $P(x)$ is bounded similarly by the sign variations $V_-$ in the polynomial $P(-x)$:\n  $$\\mathbf{N_- = V_- - 2m, \\quad m \\in \\{0, 1, 2, \\dots\\}, \\quad N_- \\le V_-}$$</li>\n</ul>\n</p>\n\n<h3>2. Proof Outline & Bounding Imaginary Roots</h3>\n<p>\nMultiplying a polynomial by $(x - r)$ where $r > 0$ increases the number of sign variations by at least 1 and always by an odd number. Since non-real complex roots of real polynomials occur strictly in conjugate pairs (contributing in multiples of 2), the discrepancy between $V$ and $N_+$ must be an even integer.\n<strong>Lower Bound on Non-Real Complex Roots:</strong>\nSince the total number of complex roots is $n$, the number of non-real roots $N_c$ satisfies:\n$$\\mathbf{N_c = n - (N_+ + N_-) \\ge n - (V + V_-)}$$\n</p>\n"
        },
        {
          "id": "sec_4_3",
          "title": "Multiplicity of Roots & Polynomial Derivative GCD",
          "content": "\n<h3>1. Definition and Derivative Criteria</h3>\n<p>\nA root $c$ of $P(x)$ has <strong>multiplicity $m \\ge 1$</strong> if $(x - c)^m$ divides $P(x)$ but $(x - c)^{m+1}$ does not, so $P(x) = (x - c)^m g(x)$ with $g(c) \\ne 0$.<br>\n<strong>Theorem:</strong> A number $c$ is a root of $P(x)$ of multiplicity $m$ if and only if:\n$$\\mathbf{P(c) = P'(c) = P''(c) = \\dots = P^{(m-1)}(c) = 0 \\quad \\text{and} \\quad P^{(m)}(c) \\ne 0}$$\n<em>Proof:</em> Differentiating $P(x) = (x - c)^m g(x)$ by the Product Rule:\n$$P'(x) = m(x - c)^{m-1} g(x) + (x - c)^m g'(x) = (x - c)^{m-1} [m g(x) + (x - c) g'(x)]$$\nAt $x = c$, $(x - c)^{m-1}$ is a factor, so $P'(c) = 0$ for $m \\ge 2$. Repeated differentiation continues until order $m-1$. $\\blacksquare$\n</p>\n\n<h3>2. Square-Free Factorization via Greatest Common Divisor</h3>\n<p>\nThe greatest common divisor of $P(x)$ and its derivative $P'(x)$ isolates all repeated roots:\n$$\\mathbf{\\gcd(P(x), P'(x)) = \\prod_{i=1}^k (x - c_i)^{m_i - 1}}$$\nThe <strong>square-free part</strong> $P_{\\text{red}}(x) = \\frac{P(x)}{\\gcd(P(x), P'(x))}$ has identical roots to $P(x)$ but with all multiplicities reduced to 1, allowing Euclidean algorithm polynomial GCD routines to isolate repeated roots without numerical root-finding!\n</p>\n"
        },
        {
          "id": "sec_4_4",
          "title": "Systematic Transformation of Polynomial Equations",
          "content": "\n<h3>1. Shifting Roots by a Constant $h$</h3>\n<p>\nTo transform an equation $P(x) = 0$ into an equation whose roots are diminished by $h$ (i.e., $y = x - h \\implies x = y + h$):\n$$P(y + h) = A_n y^n + A_{n-1} y^{n-1} + \\dots + A_1 y + A_0 = 0$$\nThe transformed coefficients $A_k$ are determined efficiently by performing $n$ successive synthetic divisions by $h$:\n$$A_k = \\frac{P^{(k)}(h)}{k!}$$\n</p>\n\n<h3>2. Scaling and Reciprocal Transformations</h3>\n<p>\n<ul>\n  <li><strong>Multiplying Roots by $m$ ($y = mx \\implies x = y/m$):</strong>\n  $$a_n \\left(\\frac{y}{m}\\right)^n + a_{n-1}\\left(\\frac{y}{m}\\right)^{n-1} + \\dots + a_0 = 0 \\iff a_n y^n + m a_{n-1} y^{n-1} + m^2 a_{n-2} y^{n-2} + \\dots + m^n a_0 = 0$$</li>\n  <li><strong>Reciprocal Roots ($y = 1/x \\implies x = 1/y$):</strong>\n  $$a_n \\left(\\frac{1}{y}\\right)^n + \\dots + a_0 = 0 \\iff a_0 y^n + a_1 y^{n-1} + \\dots + a_{n-1} y + a_n = 0$$\n  This simply reverses the order of the original coefficients!</li>\n</ul>\n</p>\n"
        },
        {
          "id": "sec_4_5",
          "title": "Removal of Terms & Reciprocal Equations",
          "content": "\n<h3>1. Eliminating the Second Term (Tschirnhaus Shift)</h3>\n<p>\nGiven $a_0 x^n + a_1 x^{n-1} + \\dots + a_n = 0$, shifting roots by $x = y + h$:\n$$a_0 (y + h)^n + a_1 (y + h)^{n-1} + \\dots = a_0 [y^n + n h y^{n-1} + \\dots] + a_1 [y^{n-1} + \\dots] = 0$$\nThe coefficient of $y^{n-1}$ is $n a_0 h + a_1$. Setting this to zero yields:\n$$\\mathbf{h = -\\frac{a_1}{n a_0}}$$\nThis canonical shift removes the degree $n-1$ term, reducing any general cubic $a x^3 + b x^2 + c x + d = 0$ to the depressed cubic $y^3 + p y + q = 0$!\n</p>\n\n<h3>2. Reciprocal Equations of First and Second Class</h3>\n<p>\nAn equation is <strong>reciprocal</strong> if substituting $x \\to 1/x$ leaves the equation unchanged:\n$$a_k = a_{n-k} \\quad (\\text{Standard Class}) \\qquad \\text{or} \\qquad a_k = -a_{n-k} \\quad (\\text{Second Class})$$\n<strong>Solution Strategy:</strong>\n<ul>\n  <li>If degree $n$ is odd, $x = -1$ (Class 1) or $x = 1$ (Class 2) is always a root. Factoring out $(x \\pm 1)$ reduces the equation to an even-degree reciprocal equation.</li>\n  <li>For an even degree reciprocal equation $a x^4 + b x^3 + c x^2 + b x + a = 0$, divide by $x^2$:\n  $$a\\left(x^2 + \\frac{1}{x^2}\\right) + b\\left(x + \\frac{1}{x}\\right) + c = 0$$\n  Substituting $z = x + \\frac{1}{x} \\implies x^2 + \\frac{1}{x^2} = z^2 - 2$ reduces the quartic to a quadratic in $z$:\n  $$\\mathbf{a(z^2 - 2) + bz + c = 0}$$\n  Solving for $z$ and then solving $x^2 - zx + 1 = 0$ yields all roots!</li>\n</ul>\n</p>\n",
          "simulation": "algebra-descartes-multiplicity-sim",
          "simulations": [
            "algebra-descartes-multiplicity-sim"
          ]
        }
      ],
      "simulation": {
        "sim_id": "algebra-descartes-multiplicity-sim",
        "title": "Interactive Descartes Sign Variations & Root Multiplicity Inspector",
        "description": "Examine polynomial sign changes, live Descartes upper bounds on positive/negative real roots, and inspect root multiplicity by visualizing simultaneous tangent touching points where P(x) = 0 and P'(x) = 0."
      },
      "problems": [
        {
          "difficulty": "Tier 1: Foundational",
          "difficultyLabel": "Foundational Mechanics",
          "title": "Example 4.1: Horner's Synthetic Division & Remainder Evaluation",
          "statement": "Use Horner's synthetic division algorithm to divide $P(x) = 2x^4 - 5x^3 + 3x^2 - 7x + 12$ by $x - 3$. State the quotient polynomial $Q(x)$ and the exact remainder $R = P(3)$.",
          "steps": [
            {
              "step": "Step 1: Set Up the Synthetic Division Table",
              "math": "\\begin{array}{c|rrrrr} 3 & 2 & -5 & 3 & -7 & 12 \\\\ & & 6 & 3 & 18 & 33 \\\\ \\hline & 2 & 1 & 6 & 11 & 45 \\end{array}",
              "explanation": "Multiply each accumulated entry by $c = 3$ and add to the column above."
            },
            {
              "step": "Step 2: Read Off the Coefficients",
              "math": "b_3 = 2, \\quad b_2 = 1, \\quad b_1 = 6, \\quad b_0 = 11, \\quad R = 45",
              "explanation": "The bottom row supplies quotient polynomial coefficients and the terminal remainder."
            },
            {
              "step": "Step 3: Construct the Factorization",
              "math": "Q(x) = 2x^3 + x^2 + 6x + 11 \\\\ P(x) = (x - 3)(2x^3 + x^2 + 6x + 11) + 45",
              "explanation": "Verify by checking $P(3) = 2(81) - 5(27) + 3(9) - 7(3) + 12 = 162 - 135 + 27 - 21 + 12 = 45$."
            }
          ],
          "answer": "Q(x) = 2x^3 + x^2 + 6x + 11; \\quad R = P(3) = 45."
        },
        {
          "difficulty": "Tier 2: Intermediate Exam",
          "difficultyLabel": "Intermediate University Exam",
          "title": "Example 4.2: Descartes' Sign Analysis of Higher-Degree Polynomial",
          "statement": "Apply Descartes' Rule of Signs to $P(x) = x^7 - 3x^4 + 2x^3 - x + 5 = 0$. Determine: (a) Maximum number of positive real roots. (b) Maximum number of negative real roots. (c) Minimum number of non-real complex roots.",
          "steps": [
            {
              "step": "Step 1: Count Sign Variations in P(x)",
              "math": "\\text{Coefficients of } P(x): \\quad +1, \\; -3, \\; +2, \\; -1, \\; +5 \\\\ \\text{Signs: } (+, -, +, -, +) \\implies V = 4 \\text{ sign changes}",
              "explanation": "There are 4 transitions between consecutive non-zero coefficients."
            },
            {
              "step": "Step 2: Determine Possible Positive Real Roots N₊",
              "math": "N_+ \\in \\{4, 2, 0\\}",
              "explanation": "By Descartes' rule, $N_+$ is 4 or less by an even integer."
            },
            {
              "step": "Step 3: Count Sign Variations in P(-x)",
              "math": "P(-x) = (-x)^7 - 3(-x)^4 + 2(-x)^3 - (-x) + 5 = -x^7 - 3x^4 - 2x^3 + x + 5 \\\\ \\text{Signs: } (-, -, -, +, +) \\implies V_- = 1 \\text{ sign change} \\\\ N_- = 1",
              "explanation": "Because $V_- = 1$, there is exactly 1 negative real root."
            },
            {
              "step": "Step 4: Bound Non-Real Complex Roots",
              "math": "\\text{Total degree } n = 7. \\\\ \\text{If } N_+ = 4: \\quad N_c = 7 - (4 + 1) = 2 \\\\ \\text{If } N_+ = 2: \\quad N_c = 7 - (2 + 1) = 4 \\\\ \\text{If } N_+ = 0: \\quad N_c = 7 - (0 + 1) = 6 \\\\ \\min(N_c) = 2 \\text{ complex roots}",
              "explanation": "Since $N_+ \\le 4$ and $N_- = 1$, the polynomial must have at least 2 non-real complex roots (and may have up to 6)."
            }
          ],
          "answer": "\\text{Positive roots: } N_+ \\in \\{0, 2, 4\\}; \\quad \\text{Negative roots: } N_- = 1; \\quad \\text{Complex roots: } N_c \\in \\{2, 4, 6\\} \\implies \\text{At least 2 complex conjugate roots}."
        },
        {
          "difficulty": "Tier 3: Honors / Proof Challenge",
          "difficultyLabel": "Honors / Proof Challenge",
          "title": "Example 4.3: Complete Analytical Solution of a Reciprocal Sextic Equation",
          "statement": "Solve the reciprocal equation $2x^6 - 9x^5 + 14x^4 - 14x^3 + 14x^2 - 9x + 2 = 0$ by reducing it to a cubic equation in $z = x + \\frac{1}{x}$.",
          "steps": [
            {
              "step": "Step 1: Divide by x³ and Group Symmetric Terms",
              "math": "\\text{Divide by } x^3 \\ne 0: \\\\ 2\\left(x^3 + \\frac{1}{x^3}\\right) - 9\\left(x^2 + \\frac{1}{x^2}\\right) + 14\\left(x + \\frac{1}{x}\\right) - 14 = 0",
              "explanation": "Pair equidistant symmetric powers from both ends."
            },
            {
              "step": "Step 2: Express Powers in Terms of z = x + 1/x",
              "math": "x + \\frac{1}{x} = z \\\\ x^2 + \\frac{1}{x^2} = z^2 - 2 \\\\ x^3 + \\frac{1}{x^3} = z^3 - 3z \\\\ 2(z^3 - 3z) - 9(z^2 - 2) + 14z - 14 = 0 \\\\ 2z^3 - 6z - 9z^2 + 18 + 14z - 14 = 0 \\\\ 2z^3 - 9z^2 + 8z + 4 = 0",
              "explanation": "Substitute power reductions to yield a reduced cubic polynomial in $z$."
            },
            {
              "step": "Step 3: Factor the Cubic in z",
              "math": "\\text{Testing integer roots: at } z = 2: \\quad 2(8) - 9(4) + 8(2) + 4 = 16 - 36 + 16 + 4 = 0 \\quad \\checkmark \\\\ \\text{Synthetic division gives: } (z - 2)(2z^2 - 5z - 2) = 0 \\\\ z_1 = 2, \\quad z_{2,3} = \\frac{5 \\pm \\sqrt{25 - 4(2)(-2)}}{4} = \\frac{5 \\pm \\sqrt{41}}{4}",
              "explanation": "Factor $(z - 2)$ out and apply the quadratic formula."
            },
            {
              "step": "Step 4: Solve for x from Each z",
              "math": "\\text{For } z = 2: \\quad x + \\frac{1}{x} = 2 \\iff x^2 - 2x + 1 = 0 \\implies (x - 1)^2 = 0 \\implies x = 1 \\text{ (double root)} \\\\ \\text{For } z = \\frac{5 \\pm \\sqrt{41}}{4}: \\quad x^2 - z x + 1 = 0 \\implies x = \\frac{z \\pm \\sqrt{z^2 - 4}}{2}",
              "explanation": "Each value of $z$ yields two reciprocal roots for $x$."
            }
          ],
          "answer": "x = 1 \\text{ (multiplicity 2)}, \\quad \\text{and } x = \\frac{z \\pm \\sqrt{z^2 - 4}}{2} \\text{ where } z = \\frac{5 \\pm \\sqrt{41}}{4}."
        }
      ],
      "simulations": [
        "algebra-descartes-multiplicity-sim"
      ],
      "id": "unit4",
      "unitId": "unit4-algebra",
      "number": 4,
      "unitNumber": 4,
      "leadSummary": "Horner's Synthetic Division, Descartes' Sign Criteria, Multiple Root GCD Analysis & Reciprocal Solvers",
      "title": "Polynomial Division, Descartes' Rule of Signs & Transformations"
    },
    {
      "unit_id": "unit_5",
      "unit_title": "Summation of Algebraic & Trigonometric Series",
      "unit_subtitle": "Mathematical Induction, Telescoping Differences, AGP Closed Forms, Partial Fractions & C + iS Phasors",
      "sections": [
        {
          "id": "sec_5_1",
          "title": "Mathematical Induction & Polynomial Power Sums",
          "content": "\n<h3>1. The Axiom of Mathematical Induction</h3>\n<p>\nThe Principle of Mathematical Induction is fundamentally equivalent to the Well-Ordering Principle of the natural numbers $\\mathbb{N}$:\n<ul>\n  <li><strong>Weak Induction:</strong> If a proposition $P(n)$ is true for $n = 1$, and for every $k \\ge 1$ the truth of $P(k)$ implies $P(k+1)$, then $P(n)$ is true for all $n \\in \\mathbb{N}$.</li>\n  <li><strong>Strong Induction:</strong> If $P(1)$ is true, and the truth of $P(1), P(2), \\dots, P(k)$ collectively implies $P(k+1)$, then $P(n)$ is true for all $n \\in \\mathbb{N}$.</li>\n</ul>\n</p>\n\n<h3>2. Canonical Power Sum Identities</h3>\n<p>\nInductive proofs establish the classic closed forms for integer power sums:\n<div class=\"math-display\">\n$$\\mathbf{S_1(n) = \\sum_{k=1}^n k = \\frac{n(n+1)}{2}}$$\n$$\\mathbf{S_2(n) = \\sum_{k=1}^n k^2 = \\frac{n(n+1)(2n+1)}{6}}$$\n$$\\mathbf{S_3(n) = \\sum_{k=1}^n k^3 = \\left[\\frac{n(n+1)}{2}\\right]^2 = [S_1(n)]^2}$$\n</div>\nThe remarkable identity $S_3(n) = [S_1(n)]^2$ (Nicomachus's Theorem) states that the sum of the first $n$ cubes equals the square of the sum of the first $n$ integers.\n</p>\n"
        },
        {
          "id": "sec_5_2",
          "title": "Finite Differences & The Telescoping Sum Method",
          "content": "\n<h3>1. The Difference Operator $\\Delta$</h3>\n<p>\nFor a sequence $f(n)$, the forward difference operator is defined by:\n$$\\mathbf{\\Delta f(n) \\equiv f(n+1) - f(n)}$$\nThe Fundamental Theorem of Summation Calculus states that the sum of differences telescopes:\n$$\\mathbf{\\sum_{k=1}^n \\Delta f(k) = \\sum_{k=1}^n [f(k+1) - f(k)] = f(n+1) - f(1)}$$\nAll intermediate terms cancel pairwise, leaving only the boundary evaluations!\n</p>\n\n<h3>2. Factorial Polynomials</h3>\n<p>\nWe define the falling factorial polynomial of degree $r$:\n$$n^{(r)} \\equiv n(n-1)(n-2)\\cdots(n-r+1)$$\nIts forward difference mirrors standard polynomial differentiation:\n$$\\Delta [n^{(r)}] = (n+1)^{(r)} - n^{(r)} = r \\, n^{(r-1)}$$\nThus, summation follows the discrete power rule:\n$$\\mathbf{\\sum_{k=1}^n k^{(r)} = \\frac{(n+1)^{(r+1)} - 1^{(r+1)}}{r + 1} = \\frac{(n+1)^{(r+1)}}{r + 1}}$$\nAny polynomial can be converted to factorial powers via Stirling numbers of the second kind, rendering summation algorithmic!\n</p>\n"
        },
        {
          "id": "sec_5_3",
          "title": "Arithmetico-Geometric Progressions (AGP)",
          "content": "\n<h3>1. Definition of an AGP</h3>\n<p>\nAn <strong>Arithmetico-Geometric Progression</strong> is a sequence whose $k$-th term is the product of corresponding terms of an Arithmetic Progression ($a, a+d, a+2d, \\dots$) and a Geometric Progression ($1, r, r^2, \\dots$):\n$$\\mathbf{u_k = [a + (k-1)d] r^{k-1}}$$\nThe finite sum to $n$ terms is:\n$$S_n = a + (a + d)r + (a + 2d)r^2 + \\dots + [a + (n-1)d]r^{n-1}$$\n</p>\n\n<h3>2. Closed-Form Derivation</h3>\n<p>\nMultiply $S_n$ by the common ratio $r$:\n$$r S_n = ar + (a + d)r^2 + \\dots + [a + (n-2)d]r^{n-1} + [a + (n-1)d]r^n$$\nSubtracting this equation from $S_n$:\n$$(1 - r)S_n = a + d[r + r^2 + \\dots + r^{n-1}] - [a + (n-1)d]r^n$$\nThe bracketed terms form a standard finite geometric series with sum $\\frac{r(1 - r^{n-1})}{1 - r}$:\n$$(1 - r)S_n = a + \\frac{dr(1 - r^{n-1})}{1 - r} - [a + (n-1)d]r^n$$\nDividing by $(1 - r)$ yields the exact closed form:\n$$\\mathbf{S_n = \\frac{a}{1 - r} + \\frac{dr(1 - r^{n-1})}{(1 - r)^2} - \\frac{[a + (n-1)d]r^n}{1 - r}}$$\n</p>\n\n<h3>3. Sum to Infinity</h3>\n<p>\nFor $|r| < 1$, as $n \\to \\infty$, $r^n \\to 0$ and $n r^n \\to 0$. The infinite sum simplifies to:\n$$\\mathbf{S_\\infty = \\frac{a}{1 - r} + \\frac{dr}{(1 - r)^2}}$$\n</p>\n"
        },
        {
          "id": "sec_5_4",
          "title": "Summation of Series by Partial Fraction Decomposition",
          "content": "\n<h3>1. The Method of Partial Fractions for Series</h3>\n<p>\nWhen terms of an infinite series are reciprocal products of linear factors, we decompose each term $u_k$ into partial fractions to induce telescoping cancellation:\n$$u_k = \\frac{1}{(k + a)(k + b)} = \\frac{1}{b - a} \\left[ \\frac{1}{k + a} - \\frac{1}{k + b} \\right]$$\nSumming from $k = 1$ to $n$:\n$$S_n = \\frac{1}{b - a} \\sum_{k=1}^n \\left( \\frac{1}{k + a} - \\frac{1}{k + b} \\right)$$\nDepending on the shift $b - a$, intermediate terms cancel, leaving a finite number of uncancelled boundary fractions.\n</p>\n\n<h3>2. Higher-Order Factor Decompositions</h3>\n<p>\nFor three factors in arithmetic progression:\n$$u_k = \\frac{1}{(a k + b)(a(k+1) + b)(a(k+2) + b)} = \\frac{1}{2a} \\left[ \\frac{1}{(ak+b)(a(k+1)+b)} - \\frac{1}{(a(k+1)+b)(a(k+2)+b)} \\right]$$\nDefining $v_k = \\frac{1}{(ak+b)(a(k+1)+b)}$, we observe that $u_k = \\frac{1}{2a}[v_k - v_{k+1}]$.\nThe sum to $n$ terms telescopes directly:\n$$\\sum_{k=1}^n u_k = \\frac{1}{2a}[v_1 - v_{n+1}]$$\nand as $n \\to \\infty$, $v_{n+1} \\to 0$, giving the exact limit $S_\\infty = \\frac{v_1}{2a}$!\n</p>\n"
        },
        {
          "id": "sec_5_5",
          "title": "Summation of Trigonometric Series via the $C + iS$ Method",
          "content": "\n<h3>1. The Complex Phasor Coupling Technique</h3>\n<p>\nTo sum a cosine series $C = \\sum_{k=0}^{n-1} a_k \\cos(\\theta_k)$ and sine series $S = \\sum_{k=0}^{n-1} a_k \\sin(\\theta_k)$, we form the complex linear combination:\n$$\\mathbf{C + iS = \\sum_{k=0}^{n-1} a_k [\\cos(\\theta_k) + i\\sin(\\theta_k)] = \\sum_{k=0}^{n-1} a_k e^{i\\theta_k}}$$\nThis converts trigonometric sums into geometric or binomial series in the complex domain! After evaluating $C + iS$ in closed form, equating real parts recovers $C$, and equating imaginary parts recovers $S$.\n</p>\n\n<h3>2. Sum of Sines and Cosines in Arithmetic Progression</h3>\n<p>\nLet $\\theta_k = \\alpha + k\\beta$:\n$$C + iS = \\sum_{k=0}^{n-1} e^{i(\\alpha + k\\beta)} = e^{i\\alpha} \\sum_{k=0}^{n-1} (e^{i\\beta})^k = e^{i\\alpha} \\frac{1 - e^{in\\beta}}{1 - e^{i\\beta}}$$\nFactoring out half-angles:\n$$1 - e^{in\\beta} = -e^{in\\beta/2}(e^{in\\beta/2} - e^{-in\\beta/2}) = -2i e^{in\\beta/2}\\sin(n\\beta/2)$$\n$$1 - e^{i\\beta} = -2i e^{i\\beta/2}\\sin(\\beta/2)$$\nDividing:\n$$C + iS = e^{i\\alpha} \\frac{-2i e^{in\\beta/2}\\sin(n\\beta/2)}{-2i e^{i\\beta/2}\\sin(\\beta/2)} = \\frac{\\sin(n\\beta/2)}{\\sin(\\beta/2)} e^{i\\left(\\alpha + \\frac{n-1}{2}\\beta\\right)}$$\nEquating real and imaginary parts gives the famous closed forms:\n<div class=\"math-display\">\n$$\\mathbf{C = \\sum_{k=0}^{n-1} \\cos(\\alpha + k\\beta) = \\frac{\\sin(n\\beta/2)}{\\sin(\\beta/2)} \\cos\\left(\\alpha + \\frac{n-1}{2}\\beta\\right)}$$\n$$\\mathbf{S = \\sum_{k=0}^{n-1} \\sin(\\alpha + k\\beta) = \\frac{\\sin(n\\beta/2)}{\\sin(\\beta/2)} \\sin\\left(\\alpha + \\frac{n-1}{2}\\beta\\right)}$$\n</div>\n</p>\n",
          "simulation": "algebra-series-cis-phasor-sim",
          "simulations": [
            "algebra-series-cis-phasor-sim"
          ]
        }
      ],
      "simulation": {
        "sim_id": "algebra-series-cis-phasor-sim",
        "title": "Interactive C + iS Complex Phasor & Trigonometric Sum Visualizer",
        "description": "Visualize trigonometric summation by chaining complex phasors exp(i(α + kβ)) in the Argand plane. Adjust angle parameters and term count n to see the polygon of chords close onto circular arcs, verifying the closed form."
      },
      "problems": [
        {
          "difficulty": "Tier 1: Foundational",
          "difficultyLabel": "Foundational Mechanics",
          "title": "Example 5.1: Finite Arithmetico-Geometric Series Evaluation",
          "statement": "Evaluate the sum of the first $n$ terms of the arithmetico-geometric series $S_n = 1\\cdot 2 + 2\\cdot 2^2 + 3\\cdot 2^3 + \\dots + n\\cdot 2^n$.",
          "steps": [
            {
              "step": "Step 1: Identify Parameters and Multiply by Common Ratio",
              "math": "a = 1, \\quad d = 1, \\quad r = 2 \\\\ S_n = 1\\cdot 2^1 + 2\\cdot 2^2 + 3\\cdot 2^3 + \\dots + n\\cdot 2^n \\\\ 2 S_n = 1\\cdot 2^2 + 2\\cdot 2^3 + \\dots + (n-1)\\cdot 2^n + n\\cdot 2^{n+1}",
              "explanation": "Shift by the common ratio $r = 2$."
            },
            {
              "step": "Step 2: Subtract the Shifted Series",
              "math": "S_n - 2S_n = 2^1 + (2^2 + 2^3 + \\dots + 2^n) - n\\cdot 2^{n+1} \\\\ -S_n = \\sum_{k=1}^n 2^k - n\\cdot 2^{n+1}",
              "explanation": "Subtracting aligns terms with unit differences."
            },
            {
              "step": "Step 3: Evaluate the Geometric Sum and Solve for Sₙ",
              "math": "\\sum_{k=1}^n 2^k = \\frac{2(2^n - 1)}{2 - 1} = 2^{n+1} - 2 \\\\ -S_n = (2^{n+1} - 2) - n\\cdot 2^{n+1} = (1 - n)2^{n+1} - 2 \\\\ S_n = (n - 1)2^{n+1} + 2",
              "explanation": "Multiply by $-1$ to isolate $S_n$."
            }
          ],
          "answer": "\\mathbf{S_n = (n - 1)2^{n+1} + 2}."
        },
        {
          "difficulty": "Tier 2: Intermediate Exam",
          "difficultyLabel": "Intermediate University Exam",
          "title": "Example 5.2: Telescoping Partial Fraction Infinite Series",
          "statement": "Find the sum to $n$ terms and the infinite sum of the series $S = \\sum_{k=1}^\\infty \\frac{1}{(2k-1)(2k+1)(2k+3)}$.",
          "steps": [
            {
              "step": "Step 1: Decompose the General Term into Partial Differences",
              "math": "u_k = \\frac{1}{(2k-1)(2k+1)(2k+3)} \\\\ \\text{Difference between outer factors: } (2k+3) - (2k-1) = 4 \\\\ u_k = \\frac{1}{4} \\left[ \\frac{(2k+3) - (2k-1)}{(2k-1)(2k+1)(2k+3)} \\right] = \\frac{1}{4} \\left[ \\frac{1}{(2k-1)(2k+1)} - \\frac{1}{(2k+1)(2k+3)} \\right]",
              "explanation": "Split the three-factor denominator into differences of two-factor denominators."
            },
            {
              "step": "Step 2: Form the Telescoping Sum",
              "math": "v_k = \\frac{1}{(2k-1)(2k+1)} \\implies u_k = \\frac{1}{4}[v_k - v_{k+1}] \\\\ S_n = \\sum_{k=1}^n u_k = \\frac{1}{4}[v_1 - v_{n+1}] = \\frac{1}{4}\\left[ \\frac{1}{1\\cdot 3} - \\frac{1}{(2n+1)(2n+3)} \\right] = \\frac{1}{12} - \\frac{1}{4(2n+1)(2n+3)}",
              "explanation": "All interior terms cancel out pairwise."
            },
            {
              "step": "Step 3: Evaluate the Infinite Limit",
              "math": "S_\\infty = \\lim_{n \\to \\infty} S_n = \\frac{1}{12} - 0 = \\frac{1}{12}",
              "explanation": "The terminal boundary term approaches zero as $n \\to \\infty$."
            }
          ],
          "answer": "\\mathbf{S_n = \\frac{1}{12} - \\frac{1}{4(2n+1)(2n+3)}}, \\qquad \\mathbf{S_\\infty = \\frac{1}{12}}."
        },
        {
          "difficulty": "Tier 3: Honors / Proof Challenge",
          "difficultyLabel": "Honors / Proof Challenge",
          "title": "Example 5.3: Binomial Trigonometric Sums via the C + iS Method",
          "statement": "Use the complex $C + iS$ method to evaluate $C = \\sum_{k=0}^n \\binom{n}{k} \\cos(k\\theta)$ and $S = \\sum_{k=0}^n \\binom{n}{k} \\sin(k\\theta)$, and prove that $C = 2^n \\cos^n(\\theta/2) \\cos(n\\theta/2)$.",
          "steps": [
            {
              "step": "Step 1: Set Up the Complex Linear Combination C + iS",
              "math": "C + iS = \\sum_{k=0}^n \\binom{n}{k} [\\cos(k\\theta) + i\\sin(k\\theta)] = \\sum_{k=0}^n \\binom{n}{k} (e^{i\\theta})^k",
              "explanation": "Combine the real cosine and imaginary sine sums."
            },
            {
              "step": "Step 2: Apply the Binomial Theorem",
              "math": "C + iS = (1 + e^{i\\theta})^n",
              "explanation": "The sum matches the binomial expansion of $(1 + z)^n$ where $z = e^{i\\theta}$."
            },
            {
              "step": "Step 3: Factor Half-Angles and Apply Euler's Formula",
              "math": "1 + e^{i\\theta} = e^{i\\theta/2}(e^{-i\\theta/2} + e^{i\\theta/2}) = e^{i\\theta/2}[2\\cos(\\theta/2)] = 2\\cos(\\theta/2) e^{i\\theta/2} \\\\ (1 + e^{i\\theta})^n = [2\\cos(\\theta/2) e^{i\\theta/2}]^n = 2^n \\cos^n(\\theta/2) e^{i n\\theta/2} \\\\ = 2^n \\cos^n(\\theta/2) [\\cos(n\\theta/2) + i\\sin(n\\theta/2)]",
              "explanation": "Factor $e^{i\\theta/2}$ from the base to convert to polar form."
            },
            {
              "step": "Step 4: Equate Real and Imaginary Parts",
              "math": "C = 2^n \\cos^n(\\theta/2) \\cos(n\\theta/2) \\quad \\blacksquare \\\\ S = 2^n \\cos^n(\\theta/2) \\sin(n\\theta/2)",
              "explanation": "Real part yields $C$, and imaginary part yields $S$."
            }
          ],
          "answer": "\\mathbf{C = 2^n \\cos^n(\\theta/2) \\cos(n\\theta/2)}, \\qquad \\mathbf{S = 2^n \\cos^n(\\theta/2) \\sin(n\\theta/2)}."
        }
      ],
      "simulations": [
        "algebra-series-cis-phasor-sim"
      ],
      "id": "unit5",
      "unitId": "unit5-algebra",
      "number": 5,
      "unitNumber": 5,
      "leadSummary": "Mathematical Induction, Telescoping Differences, AGP Closed Forms, Partial Fractions & C + iS Phasors",
      "title": "Summation of Algebraic & Trigonometric Series"
    },
    {
      "unit_id": "unit_6",
      "unit_title": "Matrix Algebra & Determinants",
      "unit_subtitle": "Matrix Rings, Special Matrix Classes, Multilinear Determinants, Cauchy-Binet Multiplicativity & Adjugate Inverses",
      "sections": [
        {
          "id": "sec_6_1",
          "title": "Algebra of Matrices: Rings, Transposition & Trace",
          "content": "\n<h3>1. The Matrix Ring</h3>\n<p>\nThe collection of $m \\times n$ matrices with entries in a field $\\mathbb{F}$ ($\\mathbb{R}$ or $\\mathbb{C}$), denoted $M_{m \\times n}(\\mathbb{F})$, forms a vector space under entrywise addition and scalar multiplication.<br>\nFor $A \\in M_{m \\times p}(\\mathbb{F})$ and $B \\in M_{p \\times n}(\\mathbb{F})$, their <strong>matrix product</strong> $C = AB \\in M_{m \\times n}(\\mathbb{F})$ has entries:\n$$\\mathbf{c_{ij} = \\sum_{k=1}^p a_{ik} b_{kj}}$$\nThe product is associative ($A(BC) = (AB)C$) and distributes over addition, but is strictly non-commutative ($AB \\ne BA$ in general). The square matrices $M_n(\\mathbb{F})$ form a non-commutative ring with identity $I_n$.\n</p>\n\n<h3>2. The Transpose & Conjugate Transpose</h3>\n<p>\nThe <strong>transpose</strong> $A^T$ of $A = [a_{ij}]$ is defined by $(A^T)_{ij} = a_{ji}$. Key properties:\n$$(A + B)^T = A^T + B^T, \\quad (cA)^T = c A^T, \\quad (A^T)^T = A, \\quad \\mathbf{(AB)^T = B^T A^T}$$\nFor complex matrices, the <strong>Hermitian adjoint</strong> (conjugate transpose) is $A^\\dagger \\equiv (\\bar{A})^T$, satisfying $(AB)^\\dagger = B^\\dagger A^\\dagger$.\n</p>\n\n<h3>3. The Trace Function</h3>\n<p>\nFor a square matrix $A \\in M_n(\\mathbb{F})$, the <strong>trace</strong> is the sum of its diagonal elements:\n$$\\mathbf{\\text{tr}(A) \\equiv \\sum_{i=1}^n a_{ii}}$$\n<strong>Cyclic Invariance Theorem:</strong> For any $A \\in M_{m \\times n}$ and $B \\in M_{n \\times m}$:\n$$\\mathbf{\\text{tr}(AB) = \\text{tr}(BA)}$$\n<em>Proof:</em> $\\text{tr}(AB) = \\sum_{i=1}^m (AB)_{ii} = \\sum_{i=1}^m \\sum_{j=1}^n a_{ij} b_{ji} = \\sum_{j=1}^n \\sum_{i=1}^m b_{ji} a_{ij} = \\sum_{j=1}^n (BA)_{jj} = \\text{tr}(BA)$. $\\blacksquare$\n</p>\n"
        },
        {
          "id": "sec_6_2",
          "title": "Taxonomy of Special Classes of Matrices",
          "content": "\n<h3>1. Real Special Matrices</h3>\n<p>\nLet $A \\in M_n(\\mathbb{R})$:\n<ul>\n  <li><strong>Symmetric:</strong> $A^T = A \\iff a_{ij} = a_{ji}$.</li>\n  <li><strong>Skew-Symmetric:</strong> $A^T = -A \\iff a_{ij} = -a_{ji}$ (diagonal entries must be zero: $a_{ii} = 0$).</li>\n  <li><strong>Orthogonal:</strong> $A^T A = A A^T = I \\iff A^{-1} = A^T$. Rows (and columns) form an orthonormal basis of $\\mathbb{R}^n$. Orthogonal transformations preserve Euclidean lengths and angles: $\\|Ax\\| = \\|x\\|$.</li>\n</ul>\n</p>\n\n<h3>2. Complex Special Matrices</h3>\n<p>\nLet $A \\in M_n(\\mathbb{C})$:\n<ul>\n  <li><strong>Hermitian:</strong> $A^\\dagger = A \\iff a_{ij} = \\bar{a}_{ji}$ (diagonal entries must be purely real: $a_{ii} \\in \\mathbb{R}$).</li>\n  <li><strong>Skew-Hermitian:</strong> $A^\\dagger = -A \\iff a_{ij} = -\\bar{a}_{ji}$ (diagonal entries must be purely imaginary).</li>\n  <li><strong>Unitary:</strong> $A^\\dagger A = I \\iff A^{-1} = A^\\dagger$. Unitary matrices preserve the complex inner product: $\\langle Ux, Uy \\rangle = \\langle x, y \\rangle$.</li>\n</ul>\n</p>\n\n<h3>3. Algebraic Operational Classes</h3>\n<p>\n<ul>\n  <li><strong>Idempotent:</strong> $A^2 = A$ (represents projection operators).</li>\n  <li><strong>Nilpotent:</strong> $A^k = 0$ for some integer $k \\ge 1$ (the smallest such $k$ is the index of nilpotency).</li>\n  <li><strong>Involutory:</strong> $A^2 = I \\iff A^{-1} = A$ (represents reflection operators).</li>\n</ul>\n</p>\n"
        },
        {
          "id": "sec_6_3",
          "title": "Axiomatic Characterization & Laplace Expansion of Determinants",
          "content": "\n<h3>1. Axiomatic Definition of the Determinant</h3>\n<p>\nThe <strong>determinant</strong> is the unique function $\\det: M_n(\\mathbb{F}) \\to \\mathbb{F}$ satisfying three fundamental axioms:\n<ol>\n  <li><strong>Multilinearity:</strong> $\\det$ is a linear function of each row when all other rows are held fixed.</li>\n  <li><strong>Alternating Property:</strong> Swapping any two rows negates the determinant: $\\det(R_1, \\dots, R_i, \\dots, R_j, \\dots, R_n) = -\\det(R_1, \\dots, R_j, \\dots, R_i, \\dots, R_n)$. Consequently, if two rows are identical, $\\det A = 0$.</li>\n  <li><strong>Normalization:</strong> $\\det(I_n) = 1$.</li>\n</ol>\n</p>\n\n<h3>2. The Leibniz Permutation Formula</h3>\n<p>\nFrom the axioms, the explicit determinant formula is:\n$$\\mathbf{\\det(A) = \\sum_{\\sigma \\in S_n} \\text{sgn}(\\sigma) \\prod_{i=1}^n a_{i, \\sigma(i)}}$$\nwhere the sum ranges over all $n!$ permutations $\\sigma$ of the symmetric group $S_n$, and $\\text{sgn}(\\sigma) \\in \\{+1, -1\\}$ is the permutation parity.\n</p>\n\n<h3>3. Laplace's Cofactor Expansion Theorem</h3>\n<p>\nThe $(i, j)$-th <strong>minor</strong> $M_{ij}$ is the determinant of the $(n-1) \\times (n-1)$ submatrix formed by deleting row $i$ and column $j$. The $(i, j)$-th <strong>cofactor</strong> is:\n$$C_{ij} \\equiv (-1)^{i+j} M_{ij}$$\n<strong>Theorem (Laplace):</strong> The determinant can be evaluated by expanding along any arbitrary row $i$ or column $j$:\n$$\\mathbf{\\det(A) = \\sum_{j=1}^n a_{ij} C_{ij} \\quad (\\text{Expansion along row } i)}$$\n$$\\mathbf{\\det(A) = \\sum_{i=1}^n a_{ij} C_{ij} \\quad (\\text{Expansion along column } j)}$$\n</p>\n"
        },
        {
          "id": "sec_6_4",
          "title": "Fundamental Determinant Properties & Multiplicativity",
          "content": "\n<h3>1. Invariance and Operational Properties</h3>\n<p>\n<ul>\n  <li><strong>Transpose Invariance:</strong> $\\det(A^T) = \\det(A)$. Row operations and column operations have identical effects on determinants!</li>\n  <li><strong>Triangular Matrices:</strong> If $A$ is upper-triangular, lower-triangular, or diagonal, its determinant is simply the product of its diagonal entries:\n  $$\\det(A) = a_{11} a_{22} \\cdots a_{nn}$$</li>\n  <li><strong>Type III Row Operations:</strong> Adding a scalar multiple of one row to another preserves the determinant strictly unchanged: $\\det(A) = \\det(E A)$ where $\\det(E) = 1$.</li>\n  <li><strong>Scalar Multiplication:</strong> For an $n \\times n$ matrix, $\\det(c A) = c^n \\det(A)$.</li>\n</ul>\n</p>\n\n<h3>2. The Multiplicative Theorem</h3>\n<p>\n<strong>Theorem (Cauchy–Binet):</strong> For any two $n \\times n$ matrices $A$ and $B$:\n$$\\mathbf{\\det(AB) = \\det(A) \\det(B)}$$\n<em>Immediate Corollaries:</em>\n<ul>\n  <li>A matrix $A$ is invertible if and only if $\\det(A) \\ne 0$.</li>\n  <li>If $A$ is invertible: $\\det(A^{-1}) = \\frac{1}{\\det(A)}$.</li>\n  <li>If $A$ and $B$ are similar ($B = P^{-1} A P$): $\\det(B) = \\det(P^{-1})\\det(A)\\det(P) = \\det(A)$.</li>\n  <li>If $Q$ is orthogonal: $Q^T Q = I \\implies [\\det(Q)]^2 = 1 \\implies \\det(Q) = \\pm 1$.</li>\n</ul>\n</p>\n"
        },
        {
          "id": "sec_6_5",
          "title": "The Classical Adjugate Matrix, Matrix Inversion & Cramer's Rule",
          "content": "\n<h3>1. The Classical Adjugate (Adjoint)</h3>\n<p>\nThe <strong>adjugate</strong> $\\text{adj}(A)$ of an $n \\times n$ matrix $A$ is the transpose of its cofactor matrix $C = [C_{ij}]$:\n$$\\mathbf{\\text{adj}(A) \\equiv C^T \\implies [\\text{adj}(A)]_{ij} = C_{ji} = (-1)^{i+j} M_{ji}}$$\n</p>\n\n<h3>2. The Fundamental Inversion Theorem</h3>\n<p>\n<strong>Theorem:</strong> For any $n \\times n$ matrix $A$:\n$$\\mathbf{A \\cdot \\text{adj}(A) = \\text{adj}(A) \\cdot A = (\\det A) I_n}$$\n<em>Proof:</em> The $(i, k)$-th entry of $A \\cdot \\text{adj}(A)$ is $\\sum_{j=1}^n a_{ij} [\\text{adj}(A)]_{jk} = \\sum_{j=1}^n a_{ij} C_{kj}$.\nIf $i = k$, this is the Laplace expansion of $\\det(A)$ along row $i$.\nIf $i \\ne k$, this represents the expansion of a matrix with two identical rows ($i$ and $k$), which vanishes identically (alien cofactors). Thus $[A \\cdot \\text{adj}(A)]_{ik} = \\delta_{ik} \\det(A)$. $\\blacksquare$\n</p>\n<p>\nConsequently, whenever $\\det(A) \\ne 0$, the unique matrix inverse is:\n$$\\mathbf{A^{-1} = \\frac{1}{\\det(A)} \\text{adj}(A)}$$\n</p>\n\n<h3>3. Cramer’s Rule for Linear Systems</h3>\n<p>\nFor an $n \\times n$ system $AX = B$ with $\\det(A) \\ne 0$, $X = A^{-1} B = \\frac{1}{\\det A}\\text{adj}(A) B$. Entrywise:\n$$\\mathbf{x_i = \\frac{\\det(A_i)}{\\det(A)}}$$\nwhere $A_i$ is the matrix obtained by replacing the $i$-th column of $A$ with the constant vector $B$.\n</p>\n",
          "simulation": "algebra-matrix-determinant-sim",
          "simulations": [
            "algebra-matrix-determinant-sim"
          ]
        }
      ],
      "simulation": {
        "sim_id": "algebra-matrix-determinant-sim",
        "title": "Interactive Matrix Transformation & Signed Determinant Visualizer",
        "description": "Drag the column basis vectors of a 2x2 matrix to visualize linear geometric deformations of the unit square. Live computes signed area det(A), matrix trace, orientation parity, and checks singularity conditions det(A) = 0."
      },
      "problems": [
        {
          "difficulty": "Tier 1: Foundational",
          "difficultyLabel": "Foundational Mechanics",
          "title": "Example 6.1: Determinant Evaluation via Row Operations & Cofactor Inversion",
          "statement": "Given the $3 \\times 3$ matrix $A = \\begin{pmatrix} 2 & 1 & 3 \\\\ 1 & 0 & 2 \\\\ 4 & 2 & 1 \\end{pmatrix}$: (a) Compute $\\det(A)$. (b) Construct the adjugate matrix $\\text{adj}(A)$ and find $A^{-1}$.",
          "steps": [
            {
              "step": "Step 1: Compute det(A) via Row Operations",
              "math": "\\det(A) = \\begin{vmatrix} 2 & 1 & 3 \\\\ 1 & 0 & 2 \\\\ 4 & 2 & 1 \\end{vmatrix} \\xrightarrow{R_3 \\to R_3 - 2R_1} \\begin{vmatrix} 2 & 1 & 3 \\\\ 1 & 0 & 2 \\\\ 0 & 0 & -5 \\end{vmatrix} \\\\ \\text{Expand along row 3: } \\det(A) = (-5) \\cdot (-1)^{3+3} \\begin{vmatrix} 2 & 1 \\\\ 1 & 0 \\end{vmatrix} = (-5)(1)(0 - 1) = 5",
              "explanation": "Subtracting $2R_1$ from $R_3$ produces two zeros in row 3, making cofactor expansion trivial."
            },
            {
              "step": "Step 2: Compute All 9 Cofactors",
              "math": "C_{11} = +\\begin{vmatrix} 0 & 2 \\\\ 2 & 1 \\end{vmatrix} = -4, \\quad C_{12} = -\\begin{vmatrix} 1 & 2 \\\\ 4 & 1 \\end{vmatrix} = 7, \\quad C_{13} = +\\begin{vmatrix} 1 & 0 \\\\ 4 & 2 \\end{vmatrix} = 2 \\\\ C_{21} = -\\begin{vmatrix} 1 & 3 \\\\ 2 & 1 \\end{vmatrix} = 5, \\quad C_{22} = +\\begin{vmatrix} 2 & 3 \\\\ 4 & 1 \\end{vmatrix} = -10, \\quad C_{23} = -\\begin{vmatrix} 2 & 1 \\\\ 4 & 2 \\end{vmatrix} = 0 \\\\ C_{31} = +\\begin{vmatrix} 1 & 3 \\\\ 0 & 2 \\end{vmatrix} = 2, \\quad C_{32} = -\\begin{vmatrix} 2 & 3 \\\\ 1 & 2 \\end{vmatrix} = -1, \\quad C_{33} = +\\begin{vmatrix} 2 & 1 \\\\ 1 & 0 \\end{vmatrix} = -1",
              "explanation": "Evaluate the signed minors for each position."
            },
            {
              "step": "Step 3: Transpose to Form adj(A) and Compute A⁻¹",
              "math": "\\text{adj}(A) = C^T = \\begin{pmatrix} -4 & 5 & 2 \\\\ 7 & -10 & -1 \\\\ 2 & 0 & -1 \\end{pmatrix} \\\\ A^{-1} = \\frac{1}{5} \\begin{pmatrix} -4 & 5 & 2 \\\\ 7 & -10 & -1 \\\\ 2 & 0 & -1 \\end{pmatrix} = \\begin{pmatrix} -0.8 & 1.0 & 0.4 \\\\ 1.4 & -2.0 & -0.2 \\\\ 0.4 & 0.0 & -0.2 \\end{pmatrix}",
              "explanation": "Divide the transposed cofactor matrix by $\\det(A) = 5$."
            }
          ],
          "answer": "\\det(A) = 5; \\quad \\mathbf{A^{-1} = \\frac{1}{5}\\begin{pmatrix} -4 & 5 & 2 \\\\ 7 & -10 & -1 \\\\ 2 & 0 & -1 \\end{pmatrix}}."
        },
        {
          "difficulty": "Tier 2: Intermediate Exam",
          "difficultyLabel": "Intermediate University Exam",
          "title": "Example 6.2: Symmetric-Skew Decomposition & Vandermonde Determinant",
          "statement": "(a) Prove that every square matrix $A$ can be uniquely decomposed as $A = S + K$, where $S$ is symmetric and $K$ is skew-symmetric. (b) Evaluate the $3 \\times 3$ Vandermonde determinant $V(a, b, c) = \\begin{vmatrix} 1 & a & a^2 \\\\ 1 & b & b^2 \\\\ 1 & c & c^2 \\end{vmatrix}$.",
          "steps": [
            {
              "step": "Step 1: Construct the Unique Decomposition",
              "math": "S \\equiv \\frac{A + A^T}{2}, \\quad K \\equiv \\frac{A - A^T}{2} \\\\ S^T = \\frac{A^T + (A^T)^T}{2} = \\frac{A^T + A}{2} = S \\quad (\\text{Symmetric}) \\\\ K^T = \\frac{A^T - (A^T)^T}{2} = \\frac{A^T - A}{2} = -K \\quad (\\text{Skew-symmetric}) \\\\ S + K = \\frac{A + A^T + A - A^T}{2} = A",
              "explanation": "Construct $S$ and $K$ explicitly, demonstrating existence."
            },
            {
              "step": "Step 2: Prove Uniqueness",
              "math": "\\text{Suppose } A = S' + K'. \\text{ Then } A^T = S'^T + K'^T = S' - K' \\\\ A + A^T = 2S' \\implies S' = \\frac{A + A^T}{2} = S \\\\ A - A^T = 2K' \\implies K' = \\frac{A - A^T}{2} = K \\quad \\blacksquare",
              "explanation": "Taking transposes and adding/subtracting establishes uniqueness."
            },
            {
              "step": "Step 3: Evaluate Vandermonde Determinant via Row Operations",
              "math": "V(a, b, c) = \\begin{vmatrix} 1 & a & a^2 \\\\ 1 & b & b^2 \\\\ 1 & c & c^2 \\end{vmatrix} \\xrightarrow{\\substack{R_2 \\to R_2 - R_1 \\\\ R_3 \\to R_3 - R_1}} \\begin{vmatrix} 1 & a & a^2 \\\\ 0 & b - a & b^2 - a^2 \\\\ 0 & c - a & c^2 - a^2 \\end{vmatrix} \\\\ = \\begin{vmatrix} b - a & (b - a)(b + a) \\\\ c - a & (c - a)(c + a) \\end{vmatrix} = (b - a)(c - a) \\begin{vmatrix} 1 & b + a \\\\ 1 & c + a \\end{vmatrix} \\\\ = (b - a)(c - a) [(c + a) - (b + a)] = (b - a)(c - a)(c - b) = (c - b)(b - a)(c - a)",
              "explanation": "Factoring $(b-a)$ and $(c-a)$ leaves a simple $2 \\times 2$ determinant."
            }
          ],
          "answer": "\\mathbf{A = \\frac{A + A^T}{2} + \\frac{A - A^T}{2}} \\text{ is unique; } \\quad \\mathbf{V(a, b, c) = (b - a)(c - a)(c - b)}."
        },
        {
          "difficulty": "Tier 3: Honors / Proof Challenge",
          "difficultyLabel": "Honors / Proof Challenge",
          "title": "Example 6.3: Closed Formula for Circulant Determinants via Roots of Unity",
          "statement": "For the $3 \\times 3$ circulant matrix $C = \\begin{pmatrix} a & b & c \\\\ c & a & b \\\\ b & c & a \\end{pmatrix}$, prove that $\\det(C) = (a + b + c)(a + \\omega b + \\omega^2 c)(a + \\omega^2 b + \\omega c) = a^3 + b^3 + c^3 - 3abc$, where $\\omega = e^{i 2\\pi/3}$ is the cube root of unity.",
          "steps": [
            {
              "step": "Step 1: Direct Column Transformation using Roots of Unity",
              "math": "\\text{Let } \\omega \\text{ satisfy } \\omega^3 = 1, \\; 1 + \\omega + \\omega^2 = 0 \\\\ \\text{Add } \\omega \\cdot \\text{Col}_2 + \\omega^2 \\cdot \\text{Col}_3 \\text{ to } \\text{Col}_1: \\\\ \\text{Row 1: } a + \\omega b + \\omega^2 c \\\\ \\text{Row 2: } c + \\omega a + \\omega^2 b = \\omega(a + \\omega b + \\omega^2 c) \\quad (\\text{since } \\omega^3 c = c) \\\\ \\text{Row 3: } b + \\omega c + \\omega^2 a = \\omega^2(a + \\omega b + \\omega^2 c)",
              "explanation": "The linear combination produces a common factor $(a + \\omega b + \\omega^2 c)$ down the entire first column!"
            },
            {
              "step": "Step 2: Factor Out Eigenvalues",
              "math": "\\text{For each } k \\in \\{0, 1, 2\\}, \\text{ substituting the root } \\omega^k \\text{ proves that } \\lambda_k = a + \\omega^k b + \\omega^{2k} c \\text{ is an eigenvalue of } C! \\\\ \\det(C) = \\prod_{k=0}^2 \\lambda_k = (a + b + c)(a + \\omega b + \\omega^2 c)(a + \\omega^2 b + \\omega c)",
              "explanation": "The determinant of any matrix equals the product of its eigenvalues."
            },
            {
              "step": "Step 3: Expand the Product",
              "math": "(a + \\omega b + \\omega^2 c)(a + \\omega^2 b + \\omega c) = a^2 + \\omega^2 ab + \\omega ac + \\omega ab + b^2 + \\omega^2 bc + \\omega^2 ac + \\omega bc + c^2 \\\\ = a^2 + b^2 + c^2 + (\\omega + \\omega^2)(ab + bc + ca) = a^2 + b^2 + c^2 - (ab + bc + ca) \\\\ \\det(C) = (a + b + c)[a^2 + b^2 + c^2 - ab - bc - ca] = a^3 + b^3 + c^3 - 3abc \\quad \\blacksquare",
              "explanation": "Using $1 + \\omega + \\omega^2 = 0 \\implies \\omega + \\omega^2 = -1$ recovers Euler's classical cubic product factorization."
            }
          ],
          "answer": "\\mathbf{\\det(C) = a^3 + b^3 + c^3 - 3abc = (a + b + c)(a + \\omega b + \\omega^2 c)(a + \\omega^2 b + \\omega c)}."
        }
      ],
      "simulations": [
        "algebra-matrix-determinant-sim"
      ],
      "id": "unit6",
      "unitId": "unit6-algebra",
      "number": 6,
      "unitNumber": 6,
      "leadSummary": "Matrix Rings, Special Matrix Classes, Multilinear Determinants, Cauchy-Binet Multiplicativity & Adjugate Inverses",
      "title": "Matrix Algebra & Determinants"
    },
    {
      "unit_id": "unit_7",
      "unit_title": "Elementary Operations, RREF & Block Matrices",
      "unit_subtitle": "Elementary Row Operations, Echelon Uniqueness, Rank-Nullity Theorem, Rouché-Capelli Consistency & Schur Complements",
      "sections": [
        {
          "id": "sec_7_1",
          "title": "Elementary Row Operations & Elementary Matrices",
          "content": "\n<h3>1. The Three Elementary Row Operations</h3>\n<p>\nFor a matrix $A \\in M_{m \\times n}(\\mathbb{F})$, the elementary row operations are:\n<ol>\n  <li><strong>Type I (Row Interchange):</strong> $R_i \\leftrightarrow R_j$ (swap rows $i$ and $j$).</li>\n  <li><strong>Type II (Row Scaling):</strong> $R_i \\to c R_i$ with $c \\ne 0$ (multiply row $i$ by a non-zero scalar).</li>\n  <li><strong>Type III (Row Addition):</strong> $R_i \\to R_i + c R_j$ with $i \\ne j$ (add a scalar multiple of row $j$ to row $i$).</li>\n</ol>\nEach operation is strictly reversible by an elementary operation of the identical type!\n</p>\n\n<h3>2. Elementary Matrices</h3>\n<p>\nAn <strong>elementary matrix</strong> $E$ is obtained by applying a single elementary row operation to the identity matrix $I_m$.<br>\n<strong>Fundamental Principle:</strong> Performing a row operation on $A$ is algebraically identical to pre-multiplying $A$ by the corresponding elementary matrix:\n$$\\mathbf{A \\xrightarrow{\\text{Row Op}} B \\iff B = E A}$$\nSince each elementary matrix is invertible, two matrices $A$ and $B$ are <strong>row equivalent</strong> ($A \\sim B$) if and only if there exist elementary matrices $E_1, \\dots, E_k$ such that:\n$$B = E_k \\cdots E_2 E_1 A = P A, \\quad \\text{where } P \\text{ is invertible}$$\n</p>\n"
        },
        {
          "id": "sec_7_2",
          "title": "Row Echelon Form (REF) & Reduced Row Echelon Form (RREF)",
          "content": "\n<h3>1. Row Echelon Form (REF)</h3>\n<p>\nA matrix is in <strong>Row Echelon Form</strong> if:\n<ul>\n  <li>All rows consisting entirely of zeros are at the bottom.</li>\n  <li>The leading entry (first non-zero entry from the left, called the <em>pivot</em>) of each non-zero row is strictly to the right of the leading entry of the row above it.</li>\n  <li>All entries in a column below a leading pivot are zero.</li>\n</ul>\n</p>\n\n<h3>2. Reduced Row Echelon Form (RREF)</h3>\n<p>\nA matrix is in <strong>Reduced Row Echelon Form (RREF)</strong> if it satisfies REF and additionally:\n<ol>\n  <li>Every leading pivot entry is equal to $1$.</li>\n  <li>Each leading pivot $1$ is the <em>sole non-zero entry</em> in its column (all entries above and below the pivot are zero).</li>\n</ol>\n<strong>Theorem (Uniqueness of RREF):</strong> Every matrix $A \\in M_{m \\times n}$ is row equivalent to a <em>uniquely determined</em> reduced row echelon matrix $\\text{rref}(A)$.\n</p>\n"
        },
        {
          "id": "sec_7_3",
          "title": "The Rank of a Matrix & The Rank-Nullity Theorem",
          "content": "\n<h3>1. Row Rank, Column Rank & Matrix Rank</h3>\n<p>\n<ul>\n  <li>The <strong>row space</strong> $\\text{Row}(A) \\subseteq \\mathbb{F}^n$ is the subspace spanned by the row vectors of $A$. Its dimension is the <em>row rank</em>.</li>\n  <li>The <strong>column space</strong> $\\text{Col}(A) \\subseteq \\mathbb{F}^m$ is the subspace spanned by the column vectors of $A$. Its dimension is the <em>column rank</em>.</li>\n</ul>\n<strong>Fundamental Rank Theorem:</strong> For any matrix $A \\in M_{m \\times n}$:\n$$\\mathbf{\\text{row rank}(A) = \\text{column rank}(A) = \\text{rank}(A)}$$\nThe rank equals the number of non-zero rows (or pivot columns) in $\\text{rref}(A)$.\n</p>\n\n<h3>2. The Rank-Nullity Theorem</h3>\n<p>\nThe <strong>nullspace</strong> (kernel) of $A$ is $\\text{Null}(A) = \\{X \\in \\mathbb{F}^n \\mid AX = 0\\}$. Its dimension is the <strong>nullity</strong> of $A$, which equals the number of free variables (non-pivot columns) in $\\text{rref}(A)$.<br>\n<strong>Theorem (Rank-Nullity):</strong> For any $m \\times n$ matrix $A$:\n$$\\mathbf{\\text{rank}(A) + \\text{nullity}(A) = n \\quad (\\text{number of columns})}$$\n</p>\n"
        },
        {
          "id": "sec_7_4",
          "title": "Systems of Linear Equations & The Rouché-Capelli Theorem",
          "content": "\n<h3>1. The Augmented Matrix</h3>\n<p>\nA system of $m$ linear equations in $n$ variables $AX = B$ is represented by the augmented matrix $[A \\mid B] \\in M_{m \\times (n+1)}$. Applying Gauss-Jordan elimination transforms $[A \\mid B]$ into $[R \\mid B']$ in RREF without altering the solution set.\n</p>\n\n<h3>2. The Rouché–Capelli Consistency Theorem</h3>\n<p>\n<strong>Theorem:</strong> The linear system $AX = B$ is <strong>consistent</strong> (possesses at least one solution) if and only if the rank of the coefficient matrix equals the rank of the augmented matrix:\n$$\\mathbf{\\text{rank}(A) = \\text{rank}([A \\mid B])}$$\n<em>Classification of Solution Sets:</em>\n<ul>\n  <li><strong>Inconsistent (No Solutions):</strong> $\\text{rank}(A) < \\text{rank}([A \\mid B])$. This occurs if and only if $\\text{rref}([A \\mid B])$ contains a row of the form $[0, 0, \\dots, 0 \\mid 1]$.</li>\n  <li><strong>Unique Solution:</strong> $\\text{rank}(A) = \\text{rank}([A \\mid B]) = n$ (every column has a pivot, nullity = 0).</li>\n  <li><strong>Infinitely Many Solutions:</strong> $\\text{rank}(A) = \\text{rank}([A \\mid B]) = r < n$. The general solution depends on $k = n - r$ arbitrary parameters (free variables).</li>\n</ul>\n</p>\n"
        },
        {
          "id": "sec_7_5",
          "title": "Gauss-Jordan Inversion & Block Matrices",
          "content": "\n<h3>1. Gauss-Jordan Inversion Algorithm</h3>\n<p>\nTo invert an $n \\times n$ matrix $A$, form the partitioned augmented matrix $[A \\mid I_n]$. Apply elementary row operations to reduce $A$ to $I_n$:\n$$\\mathbf{[A \\mid I_n] \\xrightarrow{\\text{Gauss-Jordan}} [I_n \\mid A^{-1}]}$$\nIf $\\text{rref}(A)$ has fewer than $n$ pivots, $A$ is singular and has no inverse.\n</p>\n\n<h3>2. Block Matrices and the Schur Complement</h3>\n<p>\nLet $M = \\begin{pmatrix} A & B \\\\ C & D \\end{pmatrix}$ be a partitioned block matrix with $A$ invertible.<br>\nThe <strong>Schur complement</strong> of $A$ in $M$ is defined by:\n$$\\mathbf{S \\equiv D - C A^{-1} B}$$\nWe factor $M$ via block Gaussian elimination:\n$$\\begin{pmatrix} A & B \\\\ C & D \\end{pmatrix} = \\begin{pmatrix} I & 0 \\\\ C A^{-1} & I \\end{pmatrix} \\begin{pmatrix} A & 0 \\\\ 0 & S \\end{pmatrix} \\begin{pmatrix} I & A^{-1} B \\\\ 0 & I \\end{pmatrix}$$\nConsequently:\n$$\\det(M) = \\det(A) \\det(S) = \\det(A) \\det(D - C A^{-1} B)$$\nIf $S$ is also invertible, the explicit block inverse is:\n$$\\mathbf{M^{-1} = \\begin{pmatrix} A^{-1} + A^{-1} B S^{-1} C A^{-1} & -A^{-1} B S^{-1} \\\\ -S^{-1} C A^{-1} & S^{-1} \\end{pmatrix}}$$\n</p>\n",
          "simulation": "algebra-gauss-jordan-rref-sim",
          "simulations": [
            "algebra-gauss-jordan-rref-sim"
          ]
        }
      ],
      "simulation": {
        "sim_id": "algebra-gauss-jordan-rref-sim",
        "title": "Interactive Gauss-Jordan Elimination & RREF Stepper",
        "description": "Step through Gauss-Jordan row operations on an augmented matrix [A | B]. Live highlights pivot selections, applies row multipliers and row additions, and produces the canonical Reduced Row Echelon Form (RREF)."
      },
      "problems": [
        {
          "difficulty": "Tier 1: Foundational",
          "difficultyLabel": "Foundational Mechanics",
          "title": "Example 7.1: Computing RREF and Matrix Rank",
          "statement": "Find the Reduced Row Echelon Form (RREF) and determine the rank of the $3 \\times 4$ matrix $A = \\begin{pmatrix} 1 & 2 & -1 & 3 \\\\ 2 & 4 & 1 & 9 \\\\ 3 & 6 & 2 & 14 \\end{pmatrix}$.",
          "steps": [
            {
              "step": "Step 1: Eliminate Entries Below Pivot 1",
              "math": "\\begin{pmatrix} 1 & 2 & -1 & 3 \\\\ 2 & 4 & 1 & 9 \\\\ 3 & 6 & 2 & 14 \\end{pmatrix} \\xrightarrow{\\substack{R_2 \\to R_2 - 2R_1 \\\\ R_3 \\to R_3 - 3R_1}} \\begin{pmatrix} 1 & 2 & -1 & 3 \\\\ 0 & 0 & 3 & 3 \\\\ 0 & 0 & 5 & 5 \\end{pmatrix}",
              "explanation": "Create zeros in column 1 below row 1."
            },
            {
              "step": "Step 2: Normalize Pivot 2",
              "math": "\\xrightarrow{R_2 \\to \\frac{1}{3}R_2} \\begin{pmatrix} 1 & 2 & -1 & 3 \\\\ 0 & 0 & 1 & 1 \\\\ 0 & 0 & 5 & 5 \\end{pmatrix}",
              "explanation": "Scale row 2 so pivot in column 3 becomes 1."
            },
            {
              "step": "Step 3: Eliminate Entries Above and Below Pivot 2",
              "math": "\\xrightarrow{\\substack{R_1 \\to R_1 + R_2 \\\\ R_3 \\to R_3 - 5R_2}} \\begin{pmatrix} 1 & 2 & 0 & 4 \\\\ 0 & 0 & 1 & 1 \\\\ 0 & 0 & 0 & 0 \\end{pmatrix}",
              "explanation": "Eliminate above and below pivot column 3. Row 3 vanishes completely."
            },
            {
              "step": "Step 4: Conclude Rank and Pivot Positions",
              "math": "\\text{Pivots are at } (1, 1) \\text{ and } (2, 3). \\quad \\text{Number of non-zero rows} = 2 \\implies \\text{rank}(A) = 2",
              "explanation": "There are 2 pivot columns (1 and 3) and 2 free columns (2 and 4)."
            }
          ],
          "answer": "\\mathbf{\\text{rref}(A) = \\begin{pmatrix} 1 & 2 & 0 & 4 \\\\ 0 & 0 & 1 & 1 \\\\ 0 & 0 & 0 & 0 \\end{pmatrix}}; \\qquad \\mathbf{\\text{rank}(A) = 2}."
        },
        {
          "difficulty": "Tier 2: Intermediate Exam",
          "difficultyLabel": "Intermediate University Exam",
          "title": "Example 7.2: Gauss-Jordan Matrix Inversion & Parametric System",
          "statement": "Use Gauss-Jordan elimination on $[A \\mid I_3]$ to compute the inverse of $A = \\begin{pmatrix} 1 & 1 & 2 \\\\ 2 & 1 & 1 \\\\ 1 & 2 & 1 \\end{pmatrix}$.",
          "steps": [
            {
              "step": "Step 1: Set Up Augmented Matrix [A | I₃]",
              "math": "\\left(\\begin{array}{ccc|ccc} 1 & 1 & 2 & 1 & 0 & 0 \\\\ 2 & 1 & 1 & 0 & 1 & 0 \\\\ 1 & 2 & 1 & 0 & 0 & 1 \\end{array}\\right) \\xrightarrow{\\substack{R_2 \\to R_2 - 2R_1 \\\\ R_3 \\to R_3 - R_1}} \\left(\\begin{array}{ccc|ccc} 1 & 1 & 2 & 1 & 0 & 0 \\\\ 0 & -1 & -3 & -2 & 1 & 0 \\\\ 0 & 1 & -1 & -1 & 0 & 1 \\end{array}\\right)",
              "explanation": "Eliminate entries below first pivot."
            },
            {
              "step": "Step 2: Pivot on Column 2",
              "math": "\\xrightarrow{R_2 \\to -R_2} \\left(\\begin{array}{ccc|ccc} 1 & 1 & 2 & 1 & 0 & 0 \\\\ 0 & 1 & 3 & 2 & -1 & 0 \\\\ 0 & 1 & -1 & -1 & 0 & 1 \\end{array}\\right) \\xrightarrow{\\substack{R_1 \\to R_1 - R_2 \\\\ R_3 \\to R_3 - R_2}} \\left(\\begin{array}{ccc|ccc} 1 & 0 & -1 & -1 & 1 & 0 \\\\ 0 & 1 & 3 & 2 & -1 & 0 \\\\ 0 & 0 & -4 & -3 & 1 & 1 \\end{array}\\right)",
              "explanation": "Clear column 2 above and below row 2."
            },
            {
              "step": "Step 3: Pivot on Column 3 and Clean Columns Above",
              "math": "\\xrightarrow{R_3 \\to -\\frac{1}{4}R_3} \\left(\\begin{array}{ccc|ccc} 1 & 0 & -1 & -1 & 1 & 0 \\\\ 0 & 1 & 3 & 2 & -1 & 0 \\\\ 0 & 0 & 1 & 3/4 & -1/4 & -1/4 \\end{array}\\right) \\xrightarrow{\\substack{R_1 \\to R_1 + R_3 \\\\ R_2 \\to R_2 - 3R_3}} \\left(\\begin{array}{ccc|ccc} 1 & 0 & 0 & -1/4 & 3/4 & -1/4 \\\\ 0 & 1 & 0 & -1/4 & -1/4 & 3/4 \\\\ 0 & 0 & 1 & 3/4 & -1/4 & -1/4 \\end{array}\\right)",
              "explanation": "Normalize pivot 3 and eliminate above."
            }
          ],
          "answer": "\\mathbf{A^{-1} = \\frac{1}{4}\\begin{pmatrix} -1 & 3 & -1 \\\\ -1 & -1 & 3 \\\\ 3 & -1 & -1 \\end{pmatrix}}."
        },
        {
          "difficulty": "Tier 3: Honors / Proof Challenge",
          "difficultyLabel": "Honors / Proof Challenge",
          "title": "Example 7.3: Rouché-Capelli Parameter-Dependent System Analysis",
          "statement": "Analyze the consistency and determine the complete solution set of the system for all values of $\\lambda \\in \\mathbb{R}$: $\\begin{cases} x + y + z = 1 \\\\ x + 2y + 4z = \\lambda \\\\ x + 4y + 10z = \\lambda^2 \\end{cases}$.",
          "steps": [
            {
              "step": "Step 1: Set Up Augmented Matrix and Perform Row Reduction",
              "math": "\\left(\\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\\\ 1 & 2 & 4 & \\lambda \\\\ 1 & 4 & 10 & \\lambda^2 \\end{array}\\right) \\xrightarrow{\\substack{R_2 \\to R_2 - R_1 \\\\ R_3 \\to R_3 - R_1}} \\left(\\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\\\ 0 & 1 & 3 & \\lambda - 1 \\\\ 0 & 3 & 9 & \\lambda^2 - 1 \\end{array}\\right) \\\\ \\xrightarrow{R_3 \\to R_3 - 3R_2} \\left(\\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\\\ 0 & 1 & 3 & \\lambda - 1 \\\\ 0 & 0 & 0 & (\\lambda^2 - 1) - 3(\\lambda - 1) \\end{array}\\right)",
              "explanation": "Reduce coefficient matrix toward upper triangular form."
            },
            {
              "step": "Step 2: Analyze the Inconsistency Entry",
              "math": "R_3 \\text{ entry: } \\lambda^2 - 1 - 3\\lambda + 3 = \\lambda^2 - 3\\lambda + 2 = (\\lambda - 1)(\\lambda - 2) \\\\ \\text{Rank condition: } \\text{rank}(A) = 2 \\text{ always.} \\\\ \\text{If } (\\lambda - 1)(\\lambda - 2) \\ne 0 \\implies \\text{rank}([A \\mid B]) = 3 > 2 \\implies \\text{Inconsistent (No solutions)!}",
              "explanation": "If $\\lambda \\notin \\{1, 2\\}$, the third equation is $0 = \\text{non-zero}$, so no solution exists."
            },
            {
              "step": "Step 3: Solve for Consistent Values λ = 1 and λ = 2",
              "math": "\\text{Case 1: } \\lambda = 1: \\quad \\left(\\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\\\ 0 & 1 & 3 & 0 \\\\ 0 & 0 & 0 & 0 \\end{array}\\right) \\xrightarrow{R_1 \\to R_1 - R_2} \\left(\\begin{array}{ccc|c} 1 & 0 & -2 & 1 \\\\ 0 & 1 & 3 & 0 \\\\ 0 & 0 & 0 & 0 \\end{array}\\right) \\\\ \\text{Let } z = t \\implies x = 1 + 2t, \\; y = -3t, \\; z = t \\\\ \\text{Case 2: } \\lambda = 2: \\quad \\left(\\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\\\ 0 & 1 & 3 & 1 \\\\ 0 & 0 & 0 & 0 \\end{array}\\right) \\xrightarrow{R_1 \\to R_1 - R_2} \\left(\\begin{array}{ccc|c} 1 & 0 & -2 & 0 \\\\ 0 & 1 & 3 & 1 \\\\ 0 & 0 & 0 & 0 \\end{array}\\right) \\\\ \\text{Let } z = t \\implies x = 2t, \\; y = 1 - 3t, \\; z = t",
              "explanation": "For $\\lambda \\in \\{1, 2\\}$, $\\text{rank}(A) = \\text{rank}([A \\mid B]) = 2 < 3$, yielding 1 free variable $t$."
            }
          ],
          "answer": "\\begin{cases} \\lambda \\ne 1, 2: & \\text{Inconsistent (No solution)} \\\\ \\lambda = 1: & (x, y, z) = (1 + 2t, -3t, t), \\; t \\in \\mathbb{R} \\\\ \\lambda = 2: & (x, y, z) = (2t, 1 - 3t, t), \\; t \\in \\mathbb{R} \\end{cases}"
        }
      ],
      "simulations": [
        "algebra-gauss-jordan-rref-sim"
      ],
      "id": "unit7",
      "unitId": "unit7-algebra",
      "number": 7,
      "unitNumber": 7,
      "leadSummary": "Elementary Row Operations, Echelon Uniqueness, Rank-Nullity Theorem, Rouché-Capelli Consistency & Schur Complements",
      "title": "Elementary Operations, RREF & Block Matrices"
    },
    {
      "unit_id": "unit_8",
      "unit_title": "The Leontief Input-Output Economic Model",
      "unit_subtitle": "Inter-Industry Technological Matrices, The Open Leontief Equation, Hawkins-Simon Viability & Neumann Multipliers",
      "sections": [
        {
          "id": "sec_8_1",
          "title": "Economic Foundations of Inter-Industry Analysis",
          "content": "\n<h3>1. The Inter-Industry Economic Network</h3>\n<p>\nWassily Leontief (1973 Nobel Laureate in Economics) developed input-output analysis to model the interdependence of industries in an economy. In an economy divided into $n$ sectors (e.g., Agriculture, Manufacturing, Energy, Transportation), the output of any one sector serves a dual role:\n<ul>\n  <li><strong>Intermediate Output:</strong> Consumed by other industries (and by itself) as inputs required for production.</li>\n  <li><strong>Final Demand:</strong> Consumed by households, government, capital investment, or export.</li>\n</ul>\n</p>\n\n<h3>2. The Flow Matrix of Transactions</h3>\n<p>\nLet $x_{ij}$ denote the dollar value of output from sector $i$ consumed as intermediate input by sector $j$ during a given production period.<br>\nLet $d_i$ be the external final consumer demand for sector $i$'s product.<br>\nLet $x_i$ be the total gross output produced by sector $i$. Conservation of economic output requires:\n$$\\mathbf{x_i = \\sum_{j=1}^n x_{ij} + d_i, \\quad i = 1, 2, \\dots, n}$$\nTotal Gross Output = Total Intermediate Inputs Consumed + Final Demand.\n</p>\n"
        },
        {
          "id": "sec_8_2",
          "title": "The Consumption (Technological) Matrix $C$",
          "content": "\n<h3>1. The Technological Coefficients</h3>\n<p>\nAssuming constant returns to scale and fixed production recipes, the <strong>technological coefficient</strong> $c_{ij}$ is the dollar amount of sector $i$'s goods required to produce one dollar's worth of sector $j$'s output:\n$$\\mathbf{c_{ij} \\equiv \\frac{x_{ij}}{x_j} \\iff x_{ij} = c_{ij} x_j}$$\nThe $n \\times n$ matrix $C = [c_{ij}]$ is called the <strong>consumption matrix</strong> (or technological matrix).\n</p>\n\n<h3>2. Properties of the Consumption Matrix</h3>\n<p>\n<ul>\n  <li>Every entry is non-negative: $c_{ij} \\ge 0$.</li>\n  <li>Column $j$ represents the complete cost recipe per dollar produced by industry $j$:\n  $$\\mathbf{C_{*, j} = \\begin{pmatrix} c_{1j} \\\\ c_{2j} \\\\ \\vdots \\\\ c_{nj} \\end{pmatrix}}$$</li>\n  <li><strong>Economic Profitability Condition:</strong> In an economy where industries create value rather than destroying resources, the sum of intermediate material costs per dollar of output must be strictly less than one:\n  $$\\sum_{i=1}^n c_{ij} < 1, \\quad \\text{for all } j = 1, \\dots, n$$\n  The remainder $v_j = 1 - \\sum_{i=1}^n c_{ij} > 0$ represents the <strong>value added</strong> (wages, taxes, and operating profit) per dollar of production!</li>\n</ul>\n</p>\n"
        },
        {
          "id": "sec_8_3",
          "title": "The Open Leontief Production Equation",
          "content": "\n<h3>1. Derivation of the Matrix Equation</h3>\n<p>\nSubstituting $x_{ij} = c_{ij} x_j$ into the economic conservation balance:\n$$x_i = \\sum_{j=1}^n c_{ij} x_j + d_i \\iff X = C X + D$$\nwhere:\n$$X = \\begin{pmatrix} x_1 \\\\ x_2 \\\\ \\vdots \\\\ x_n \\end{pmatrix} \\quad (\\text{Gross Output Vector}), \\qquad D = \\begin{pmatrix} d_1 \\\\ d_2 \\\\ \\vdots \\\\ d_n \\end{pmatrix} \\quad (\\text{Final Demand Vector})$$\nRewriting into canonical linear system form:\n$$\\mathbf{(I_n - C) X = D}$$\nThe matrix $I_n - C$ is called the <strong>Leontief Matrix</strong>.\n</p>\n\n<h3>2. The Equilibrium Production Solution</h3>\n<p>\nIf the Leontief matrix $I_n - C$ is invertible, the gross output required across all sectors to satisfy final demand $D$ is uniquely determined by:\n$$\\mathbf{X = (I_n - C)^{-1} D}$$\nThe inverse matrix $(I - C)^{-1}$ is termed the <strong>Leontief Inverse</strong> (or Total Requirements Matrix). Its $(i, j)$-th entry represents the total dollar amount that sector $i$ must produce directly and indirectly to supply one dollar of final demand to sector $j$!\n</p>\n"
        },
        {
          "id": "sec_8_4",
          "title": "The Hawkins-Simon Economic Viability Conditions",
          "content": "\n<h3>1. The Economic Viability Problem</h3>\n<p>\nIn real-world economics, negative production is impossible ($X \\ge 0$). An economy is defined as <strong>economically viable</strong> if for <em>every</em> non-negative final demand vector $D \\ge 0$, there exists a unique non-negative gross production vector $X \\ge 0$ satisfying $(I - C)X = D$.\n</p>\n\n<h3>2. The Hawkins–Simon Theorem</h3>\n<p>\n<strong>Theorem (David Hawkins & Herbert Simon, 1949):</strong> An input-output system with consumption matrix $C \\ge 0$ is economically viable if and only if all leading principal minors of the Leontief matrix $I - C$ are strictly positive:\n<div class=\"math-display\">\n$$\\Delta_1 = 1 - c_{11} > 0$$\n$$\\Delta_2 = \\begin{vmatrix} 1 - c_{11} & -c_{12} \\\\ -c_{21} & 1 - c_{22} \\end{vmatrix} > 0$$\n$$\\dots$$\n$$\\Delta_n = \\det(I - C) > 0$$\n</div>\n<em>Economic Intuition:</em>\n<ul>\n  <li>$\\Delta_1 > 0 \\iff c_{11} < 1$: Sector 1 cannot consume more of its own product than it produces.</li>\n  <li>$\\Delta_2 > 0 \\iff (1 - c_{11})(1 - c_{22}) > c_{12} c_{21}$: The combined direct and indirect feedback loops between sectors 1 and 2 must not consume more than their collective net capacity.</li>\n</ul>\n</p>\n"
        },
        {
          "id": "sec_8_5",
          "title": "Neumann Series Multipliers & The Dual Leontief Price Model",
          "content": "\n<h3>1. The Neumann Power Series Expansion</h3>\n<p>\nIf the spectral radius $\\rho(C) < 1$, the Leontief inverse can be expanded as a convergent geometric matrix series (the <strong>Neumann Series</strong>):\n$$\\mathbf{(I - C)^{-1} = I + C + C^2 + C^3 + \\dots = \\sum_{k=0}^\\infty C^k}$$\nSubstituting into the output equation $X = (I - C)^{-1} D$:\n$$\\mathbf{X = D + C D + C^2 D + C^3 D + \\dots}$$\n<strong>Economic Multiplier Breakdown:</strong>\n<ul>\n  <li>$D$: Direct final consumer demand.</li>\n  <li>$CD$: First-round intermediate inputs required by industries to produce $D$.</li>\n  <li>$C^2 D$: Second-round inputs required to produce the intermediate inputs $CD$.</li>\n  <li>$C^k D$: $k$-th generation indirect supply chain requirements throughout the economy.</li>\n</ul>\n</p>\n\n<h3>2. The Dual Leontief Price Model</h3>\n<p>\nLet $P = (p_1, p_2, \\dots, p_n)$ be the unit price row vector across sectors, and let $V = (v_1, v_2, \\dots, v_n)$ be the value-added row vector (wages + profits per unit).\nThe equilibrium pricing relation states that price equals intermediate material costs plus value added:\n$$P = P C + V \\iff P(I - C) = V$$\nMultiplying by the Leontief inverse from the right yields the equilibrium price structure:\n$$\\mathbf{P = V (I - C)^{-1}}$$\nThis allows governments and central banks to calculate how changes in wages or energy tax ($V$) propagate throughout the entire price level of the macroeconomy!\n</p>\n",
          "simulation": "algebra-leontief-economy-sim",
          "simulations": [
            "algebra-leontief-economy-sim"
          ]
        }
      ],
      "simulation": {
        "sim_id": "algebra-leontief-economy-sim",
        "title": "Interactive Leontief Multi-Sector Economy & Supply Chain Simulator",
        "description": "Simulate a 3-sector macroeconomy (Agriculture, Manufacturing, Energy). Adjust consumer demand sliders D and inter-industry dependencies to watch dynamic matrix inversion (I - C)⁻¹, verify Hawkins-Simon viability, and trace supply chain flows."
      },
      "problems": [
        {
          "difficulty": "Tier 1: Foundational",
          "difficultyLabel": "Foundational Mechanics",
          "title": "Example 8.1: Two-Sector Leontief Economy and Production Equilibrium",
          "statement": "A two-sector economy consisting of Energy ($E$) and Manufacturing ($M$) has consumption matrix $C = \\begin{pmatrix} 0.2 & 0.4 \\\\ 0.3 & 0.1 \\end{pmatrix}$. (a) Verify the Hawkins-Simon conditions. (b) Compute the Leontief inverse $(I - C)^{-1}$. (c) Find the gross production vector $X$ required to satisfy final demand $D = \\begin{pmatrix} 100 \\\\ 200 \\end{pmatrix}$ million dollars.",
          "steps": [
            {
              "step": "Step 1: Verify Hawkins-Simon Viability Conditions",
              "math": "I - C = \\begin{pmatrix} 1 - 0.2 & -0.4 \\\\ -0.3 & 1 - 0.1 \\end{pmatrix} = \\begin{pmatrix} 0.8 & -0.4 \\\\ -0.3 & 0.9 \\end{pmatrix} \\\\ \\Delta_1 = 0.8 > 0 \\quad \\checkmark \\\\ \\Delta_2 = \\det(I - C) = (0.8)(0.9) - (-0.4)(-0.3) = 0.72 - 0.12 = 0.60 > 0 \\quad \\checkmark",
              "explanation": "Both principal minors are strictly positive, guaranteeing that the economy is viable."
            },
            {
              "step": "Step 2: Invert the 2x2 Leontief Matrix",
              "math": "(I - C)^{-1} = \\frac{1}{\\det(I - C)} \\begin{pmatrix} 0.9 & 0.4 \\\\ 0.3 & 0.8 \\end{pmatrix} = \\frac{1}{0.6} \\begin{pmatrix} 0.9 & 0.4 \\\\ 0.3 & 0.8 \\end{pmatrix} = \\begin{pmatrix} 1.5 & 0.667 \\\\ 0.5 & 1.333 \\end{pmatrix}",
              "explanation": "Apply the $2 \\times 2$ matrix inverse formula."
            },
            {
              "step": "Step 3: Compute the Gross Output Vector X",
              "math": "X = (I - C)^{-1} D = \\frac{1}{0.6} \\begin{pmatrix} 0.9 & 0.4 \\\\ 0.3 & 0.8 \\end{pmatrix} \\begin{pmatrix} 100 \\\\ 200 \\end{pmatrix} \\\\ = \\frac{1}{0.6} \\begin{pmatrix} 0.9(100) + 0.4(200) \\\\ 0.3(100) + 0.8(200) \\end{pmatrix} = \\frac{1}{0.6} \\begin{pmatrix} 90 + 80 \\\\ 30 + 160 \\end{pmatrix} = \\frac{1}{0.6} \\begin{pmatrix} 170 \\\\ 190 \\end{pmatrix} = \\begin{pmatrix} 283.33 \\\\ 316.67 \\end{pmatrix}",
              "explanation": "Multiply the Leontief inverse by the external demand vector."
            }
          ],
          "answer": "\\text{Hawkins-Simon conditions are satisfied; } \\mathbf{(I - C)^{-1} = \\begin{pmatrix} 1.5 & 0.667 \\\\ 0.5 & 1.333 \\end{pmatrix}}; \\quad \\mathbf{X = \\begin{pmatrix} 283.33 \\\\ 316.67 \\end{pmatrix}} \\text{ million dollars}."
        },
        {
          "difficulty": "Tier 2: Intermediate Exam",
          "difficultyLabel": "Intermediate University Exam",
          "title": "Example 8.2: Three-Sector Economic Shift and Output Reallocation",
          "statement": "A 3-sector economy with technological matrix $C = \\begin{pmatrix} 0.1 & 0.2 & 0.2 \\\\ 0.2 & 0.1 & 0.1 \\\\ 0.1 & 0.2 & 0.1 \\end{pmatrix}$ has current final demand $D = \\begin{pmatrix} 50 \\\\ 60 \\\\ 40 \\end{pmatrix}$. If consumer demand in Sector 2 increases by 50% while others remain unchanged, compute the required change in gross output vector $\\Delta X$.",
          "steps": [
            {
              "step": "Step 1: Form the Leontief Matrix I - C",
              "math": "I - C = \\begin{pmatrix} 0.9 & -0.2 & -0.2 \\\\ -0.2 & 0.9 & -0.1 \\\\ -0.1 & -0.2 & 0.9 \\end{pmatrix}",
              "explanation": "Subtract consumption matrix $C$ from identity matrix $I_3$."
            },
            {
              "step": "Step 2: Determine Demand Shift ΔD",
              "math": "\\Delta D = \\begin{pmatrix} 0 \\\\ 0.50 \\times 60 \\\\ 0 \\end{pmatrix} = \\begin{pmatrix} 0 \\\\ 30 \\\\ 0 \\end{pmatrix}",
              "explanation": "Only sector 2 experiences an external demand increase of 30 units."
            },
            {
              "step": "Step 3: Solve (I - C) ΔX = ΔD",
              "math": "\\begin{pmatrix} 0.9 & -0.2 & -0.2 \\\\ -0.2 & 0.9 & -0.1 \\\\ -0.1 & -0.2 & 0.9 \\end{pmatrix} \\begin{pmatrix} \\Delta x_1 \\\\ \\Delta x_2 \\\\ \\Delta x_3 \\end{pmatrix} = \\begin{pmatrix} 0 \\\\ 30 \\\\ 0 \\end{pmatrix} \\\\ \\det(I - C) = 0.9(0.81 - 0.02) + 0.2(-0.18 - 0.01) - 0.2(0.04 + 0.09) \\\\ = 0.9(0.79) + 0.2(-0.19) - 0.2(0.13) = 0.711 - 0.038 - 0.026 = 0.647 \\\\ \\text{Using Cramer's Rule for Column 2 of } (I - C)^{-1}: \\\\ \\text{Cofactors: } C_{12} = -(-0.18 - 0.01) = 0.19, \\quad C_{22} = 0.81 - 0.02 = 0.79, \\quad C_{32} = -(-0.09 - 0.02) = 0.11 \\\\ \\Delta X = \\frac{30}{0.647} \\begin{pmatrix} 0.19 \\\\ 0.79 \\\\ 0.11 \\end{pmatrix} \\approx \\begin{pmatrix} 8.81 \\\\ 36.63 \\\\ 5.10 \\end{pmatrix}",
              "explanation": "Compute the direct and indirect multiplier impact using cofactors."
            }
          ],
          "answer": "\\mathbf{\\Delta X \\approx \\begin{pmatrix} 8.81 \\\\ 36.63 \\\\ 5.10 \\end{pmatrix}} \\implies \\text{All three sectors must expand output to support Sector 2's demand growth}."
        },
        {
          "difficulty": "Tier 3: Honors / Proof Challenge",
          "difficultyLabel": "Honors / Proof Challenge",
          "title": "Example 8.3: Neumann Series Convergence & The Dual Price Equilibrium",
          "statement": "Given an $n$-sector economy with non-negative consumption matrix $C$: (a) Prove that if the maximum column sum satisfies $\\|C\\|_1 = \\max_j \\sum_{i=1}^n c_{ij} < 1$, the spectral radius satisfies $\\rho(C) < 1$, and the Neumann series $\\sum_{k=0}^\\infty C^k$ converges strictly to $(I - C)^{-1}$. (b) If $C = \\begin{pmatrix} 0.3 & 0.2 \\\\ 0.1 & 0.4 \\end{pmatrix}$ and the value-added vector per unit output is $V = (14, 21)$ dollars, determine the equilibrium price vector $P = (p_1, p_2)$.",
          "steps": [
            {
              "step": "Step 1: Prove Neumann Series Convergence",
              "math": "\\text{For any induced matrix norm } \\|\\cdot\\|, \\quad \\rho(C) \\le \\|C\\|_1 < 1 \\\\ \\text{Consider partial sum } S_m = \\sum_{k=0}^m C^k. \\quad (I - C) S_m = I - C^{m+1} \\\\ \\text{Since } \\rho(C) < 1, \\quad \\lim_{m \\to \\infty} C^{m+1} = 0 \\\\ \\lim_{m \\to \\infty} (I - C) S_m = I \\implies \\sum_{k=0}^\\infty C^k = (I - C)^{-1} \\quad \\blacksquare",
              "explanation": "Use operator norm and Gelfand's formula to prove absolute convergence of the matrix power series."
            },
            {
              "step": "Step 2: Formulate the Dual Price Equation P = V(I - C)⁻¹",
              "math": "P(I - C) = V \\iff \\begin{pmatrix} p_1 & p_2 \\end{pmatrix} \\begin{pmatrix} 0.7 & -0.2 \\\\ -0.1 & 0.6 \\end{pmatrix} = \\begin{pmatrix} 14 & 21 \\end{pmatrix}",
              "explanation": "Set up the horizontal row equation $P(I - C) = V$."
            },
            {
              "step": "Step 3: Invert (I - C) and Compute Equilibrium Prices",
              "math": "\\det(I - C) = (0.7)(0.6) - (-0.2)(-0.1) = 0.42 - 0.02 = 0.40 \\\\ (I - C)^{-1} = \\frac{1}{0.40} \\begin{pmatrix} 0.6 & 0.2 \\\\ 0.1 & 0.7 \\end{pmatrix} = \\begin{pmatrix} 1.5 & 0.5 \\\\ 0.25 & 1.75 \\end{pmatrix} \\\\ P = \\begin{pmatrix} 14 & 21 \\end{pmatrix} \\begin{pmatrix} 1.5 & 0.5 \\\\ 0.25 & 1.75 \\end{pmatrix} \\\\ p_1 = 14(1.5) + 21(0.25) = 21 + 5.25 = 26.25 \\\\ p_2 = 14(0.5) + 21(1.75) = 7 + 36.75 = 43.75",
              "explanation": "Multiply the value-added row vector by the Leontief inverse."
            }
          ],
          "answer": "\\mathbf{P = (26.25, \\; 43.75)} \\implies p_1 = \\$26.25 \\text{ and } p_2 = \\$43.75 \\text{ per unit}."
        }
      ],
      "simulations": [
        "algebra-leontief-economy-sim"
      ],
      "id": "unit8",
      "unitId": "unit8-algebra",
      "number": 8,
      "unitNumber": 8,
      "leadSummary": "Inter-Industry Technological Matrices, The Open Leontief Equation, Hawkins-Simon Viability & Neumann Multipliers",
      "title": "The Leontief Input-Output Economic Model"
    }
  ]
};
