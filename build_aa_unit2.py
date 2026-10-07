# -*- coding: utf-8 -*-
"""
build_aa_unit2.py
Constructs Unit 2: Groups, Subgroups, Cyclic Structures & Element Orders
"""

def get_unit2():
    u2 = {
        "number": 2,
        "title": "Groups, Subgroups, Cyclic Structures & Element Orders",
        "leadSummary": "Subgroup definitions and testing theorems (One-Step, Two-Step, Finite Subgroup Tests), order of an element, generator orbits, cyclic group structure, the Fundamental Theorem of Cyclic Groups, generator enumeration via Euler's phi-function, and external direct products.",
        "simulations": ["sim_aa_subgroup_lattices"],
        "sections": [
            {
                "secNumber": "2.1",
                "title": "Subgroups, Subgroup Criteria, Centralizers & Normalizers",
                "content": r"""### 1. The Notion of a Subgroup

Let $(G, *)$ be a group.

> **Definition 2.1 (Subgroup):**
> A subset $H \subseteq G$ is called a **subgroup** of $G$, denoted by $H \le G$, if $H$ is itself a group under the operation of $G$.
> If $H \le G$ and $H \ne G$, we write $H < G$ ($H$ is a **proper subgroup**).
> The trivial subgroups of any group $G$ are $\{e\}$ and $G$ itself.

---

### 2. Subgroup Testing Criteria

Rather than verifying all four group axioms, we can determine subgroup status using specialized, concise tests:

> **Theorem 2.1 (Two-Step Subgroup Test):**
> A non-empty subset $H \subseteq G$ is a subgroup of $G$ if and only if:
> 1. **Closure under operation:** $\forall a, b \in H \implies a * b \in H$.
> 2. **Closure under inverses:** $\forall a \in H \implies a^{-1} \in H$.

> **Theorem 2.2 (One-Step Subgroup Test):**
> A non-empty subset $H \subseteq G$ is a subgroup of $G$ if and only if:
> $$\forall a, b \in H \implies a * b^{-1} \in H$$

#### Complete Proof of the One-Step Test:
$(\implies)$ If $H \le G$, then for any $b \in H$, $b^{-1} \in H$ by inverse axiom. By closure, $a * b^{-1} \in H$.

$(\impliedby)$ Suppose $H \ne \emptyset$ and $a * b^{-1} \in H$ for all $a, b \in H$.
1. **Identity:** Since $H \ne \emptyset$, choose any element $x \in H$. Setting $a = x$ and $b = x$ gives:
   $$e = x * x^{-1} \in H$$
   Thus the identity of $G$ belongs to $H$.
2. **Inverses:** For any $x \in H$, setting $a = e$ and $b = x$ gives:
   $$x^{-1} = e * x^{-1} \in H$$
   Thus every element in $H$ has its inverse in $H$.
3. **Closure:** For any $x, y \in H$, since $y \in H \implies y^{-1} \in H$. Setting $a = x$ and $b = y^{-1}$ gives:
   $$x * y = x * (y^{-1})^{-1} \in H$$
4. **Associativity:** Inherited automatically from $G$ since $H \subseteq G$.
Therefore, $H \le G$. $\blacksquare$

> **Theorem 2.3 (Finite Subgroup Test):**
> Let $H$ be a non-empty **finite** subset of a group $G$. Then $H \le G$ if and only if $H$ is closed under multiplication:
> $$\forall a, b \in H \implies a * b \in H$$
*(Inverses are guaranteed automatically by pigeonhole finiteness: the sequence $a, a^2, a^3, \dots$ must eventually repeat, generating $a^{-1} = a^{k-1}$!)*

---

### 3. Centralizers, Normalizers and the Center

Let $G$ be a group.
- **The Center of $G$, $Z(G)$:** The set of elements that commute with every element of $G$:
  $$Z(G) = \{ z \in G : z g = g z, \; \forall g \in G \}$$
- **The Centralizer of an Element $a \in G$, $C_G(a)$:**
  $$C_G(a) = \{ g \in G : g a = a g \}$$
- **The Normalizer of a Subset $S \subseteq G$, $N_G(S)$:**
  $$N_G(S) = \{ g \in G : g S g^{-1} = S \}$$

*Theorem:* $Z(G)$, $C_G(a)$, and $N_G(S)$ are always subgroups of $G$."""
            },
            {
                "secNumber": "2.2",
                "title": "Order of Elements, Cyclic Groups & Generator Orbits",
                "content": r"""### 1. Order of an Element

Let $G$ be a group and $a \in G$.

> **Definition 2.2 (Order of an Element):**
> The **order** of an element $a \in G$, denoted by $|a|$ or $\text{ord}(a)$, is the smallest positive integer $n \in \mathbb{Z}^+$ such that:
> $$a^n = e$$
> If no such positive integer exists, $a$ is said to have **infinite order** ($|a| = \infty$).

#### Theorem 2.4 (Properties of Element Order):
Let $a \in G$ with $|a| = n$.
1. $a^k = e$ if and only if $n$ divides $k$ ($n \mid k$).
2. $a^i = a^j$ if and only if $i \equiv j \pmod n$.
3. For any integer $k \in \mathbb{Z}$, the order of $a^k$ is given by:
   $$|a^k| = \frac{n}{\gcd(n, k)}$$

---

### 2. Cyclic Groups

> **Definition 2.3 (Cyclic Group):**
> A group $G$ is called **cyclic** if there exists an element $a \in G$ such that every element of $G$ is an integral power of $a$:
> $$G = \langle a \rangle = \{ a^k : k \in \mathbb{Z} \}$$
> The element $a$ is called a **generator** of $G$.

#### Theorem 2.5 (Abelian Nature of Cyclic Groups):
Every cyclic group is Abelian.
*Proof:* Let $x, y \in \langle a \rangle$. Then $x = a^r$ and $y = a^s$ for some $r, s \in \mathbb{Z}$.
$$x y = a^r a^s = a^{r + s} = a^{s + r} = a^s a^r = y x \quad \blacksquare$$

---

### 3. The Fundamental Theorem of Cyclic Groups

> **Theorem 2.6 (Fundamental Theorem of Cyclic Groups):**
> Let $G = \langle a \rangle$ be a cyclic group of order $n$.
> 1. **Subgroups are cyclic:** Every subgroup of $G$ is cyclic.
> 2. **Order of Subgroups:** The order of any subgroup $H \le G$ is a divisor of $n$.
> 3. **Existence and Uniqueness:** For each positive divisor $d$ of $n$, there exists **one and only one** subgroup of $G$ of order $d$, given explicitly by:
>    $$H_d = \langle a^{n/d} \rangle$$

#### Complete Proof of Part 1 (Subgroups are Cyclic):
Let $H \le G$. If $H = \{e\}$, then $H = \langle e \rangle$ is cyclic.
Suppose $H \ne \{e\}$. Since $G = \langle a \rangle$, every element in $H$ has the form $a^k$ for some $k \in \mathbb{Z}$.
Since $H$ is a subgroup, if $a^k \in H$ with $k < 0$, then $(a^k)^{-1} = a^{-k} \in H$ where $-k > 0$.
Thus $H$ must contain positive powers of $a$.
Let $m$ be the **smallest positive integer** such that $a^m \in H$ (well-ordering principle of $\mathbb{Z}^+$).
We claim that $H = \langle a^m \rangle$.
- Clearly $\langle a^m \rangle \subseteq H$ since $a^m \in H$ and $H$ is closed under powers.
- Conversely, let $h \in H$. Then $h = a^s$ for some $s \in \mathbb{Z}$.
  By the Division Algorithm, divide $s$ by $m$:
  $$s = q m + r, \quad 0 \le r < m$$
  Then:
  $$a^s = a^{qm + r} = (a^m)^q a^r \implies a^r = a^s (a^m)^{-q}$$
  Since $a^s \in H$ and $a^m \in H \implies (a^m)^{-q} \in H$, their product $a^r \in H$.
  Since $0 \le r < m$ and $m$ was defined as the *minimal* positive integer with $a^m \in H$, we must have $r = 0$.
  Therefore $s = q m$, which means:
  $$h = a^s = (a^m)^q \in \langle a^m \rangle$$
  Hence $H \subseteq \langle a^m \rangle$.
Thus $H = \langle a^m \rangle$, proving that $H$ is cyclic! $\blacksquare$"""
            },
            {
                "secNumber": "2.3",
                "title": "Euler's Totient Function, Generator Counting & Subgroup Lattices",
                "content": r"""### 1. Counting Generators of a Finite Cyclic Group

Let $G = \langle a \rangle$ be a cyclic group of order $n$.
By Theorem 2.4, an element $a^k$ has order:
$$|a^k| = \frac{n}{\gcd(n, k)}$$
For $a^k$ to be a generator of $G$, we require $|a^k| = n$, which is true if and only if:
$$\gcd(n, k) = 1$$

> **Theorem 2.7 (Number of Generators):**
> A cyclic group of order $n$ has exactly $\phi(n)$ generators, where $\phi$ is Euler's totient function.
> Specifically, the generators of $\langle a \rangle$ are:
> $$\{ a^k : 1 \le k < n, \; \gcd(n, k) = 1 \}$$

#### Gauss's Identity:
Every element of $\langle a \rangle$ generates a cyclic subgroup of some divisor order $d \mid n$.
Since the number of elements of exact order $d$ is $\phi(d)$, partitioning the group by element orders proves Gauss's classical identity:
$$\sum_{d \mid n} \phi(d) = n$$

---

### 2. Subgroup Lattices

The collection of all subgroups of a group $G$, ordered by set inclusion $\subseteq$, forms a complete algebraic lattice called the **Subgroup Lattice** $\mathcal{L}(G)$.
- In a cyclic group $\mathbb{Z}_n$, by the Fundamental Theorem, the lattice of subgroups is isomorphic to the **divisor lattice** of $n$, ordered by divisibility:
  $$\langle a^{n/d_1} \rangle \le \langle a^{n/d_2} \rangle \iff d_1 \mid d_2$$
- In prime-power cyclic groups $\mathbb{Z}_{p^k}$, the subgroup lattice is a strictly linear chain:
  $$\{0\} = \langle p^k \rangle < \langle p^{k-1} \rangle < \dots < \langle p \rangle < \langle 1 \rangle = \mathbb{Z}_{p^k}$$"""
            },
            {
                "secNumber": "2.4",
                "title": "External Direct Products & Structure of Finite Products",
                "content": r"""### 1. External Direct Products

Let $G_1, G_2, \dots, G_n$ be groups.

> **Definition 2.4 (External Direct Product):**
> The **external direct product** $G_1 \times G_2 \times \dots \times G_n$ is the Cartesian product equipped with component-wise group operations:
> $$(g_1, g_2, \dots, g_n) * (h_1, h_2, \dots, h_n) = (g_1 h_1, g_2 h_2, \dots, g_n h_n)$$
> - Identity element: $(e_1, e_2, \dots, e_n)$.
> - Inverse element: $(g_1, \dots, g_n)^{-1} = (g_1^{-1}, \dots, g_n^{-1})$.

---

### 2. Order of Elements in Direct Products

> **Theorem 2.8 (Order Formula for Direct Products):**
> The order of an element $(g_1, g_2, \dots, g_n) \in G_1 \times G_2 \times \dots \times G_n$ is the least common multiple of the orders of its components:
> $$|(g_1, g_2, \dots, g_n)| = \text{lcm}(|g_1|, |g_2|, \dots, |g_n|)$$

#### Proof:
Let $m = |(g_1, \dots, g_n)|$ and $L = \text{lcm}(|g_1|, \dots, |g_n|)$.
$$(g_1, \dots, g_n)^L = (g_1^L, \dots, g_n^L)$$
Since each $|g_i|$ divides $L$, $g_i^L = e_i$ for all $i$. Thus $(g_1, \dots, g_n)^L = (e_1, \dots, e_n)$.
By Theorem 2.4, this implies $m \mid L$.
Conversely, $(g_1, \dots, g_n)^m = (e_1, \dots, e_n) \implies g_i^m = e_i$ for all $i$.
Hence each $|g_i| \mid m$. By definition of least common multiple, $L \mid m$.
Since $m \mid L$ and $L \mid m$ with $m, L > 0$, we have $m = L$. $\blacksquare$

---

### 3. Criterion for Cyclicity of Direct Products

> **Theorem 2.9 (Cyclicity of $\mathbb{Z}_m \times \mathbb{Z}_n$):**
> The direct product $\mathbb{Z}_m \times \mathbb{Z}_n$ is cyclic if and only if $m$ and $n$ are relatively prime:
> $$\mathbb{Z}_m \times \mathbb{Z}_n \cong \mathbb{Z}_{mn} \iff \gcd(m, n) = 1$$

#### Proof:
$(\impliedby)$ If $\gcd(m, n) = 1$, consider the element $(1, 1) \in \mathbb{Z}_m \times \mathbb{Z}_n$.
$$|(1, 1)| = \text{lcm}(|1|, |1|) = \text{lcm}(m, n) = \frac{m n}{\gcd(m, n)} = mn$$
Since the order of $(1, 1)$ equals the order of the group $|\mathbb{Z}_m \times \mathbb{Z}_n| = mn$, $(1, 1)$ is a generator, so the group is cyclic.

$(\implies)$ Suppose $\gcd(m, n) = d > 1$. Then $\text{lcm}(m, n) = \frac{mn}{d} < mn$.
For any element $(x, y) \in \mathbb{Z}_m \times \mathbb{Z}_n$, $|(x, y)| = \text{lcm}(|x|, |y|)$.
Since $|x| \mid m$ and $|y| \mid n$, $\text{lcm}(|x|, |y|) \mid \text{lcm}(m, n) = \frac{mn}{d}$.
Hence no element can have order $mn$. Thus the group cannot be cyclic. $\blacksquare$"""
            }
        ],
        "problems": [
            {
                "tier": "Foundational",
                "title": "Subgroup Lattice and Generator Classification in Z_36",
                "statement": r"Consider the cyclic additive group $G = \mathbb{Z}_{36}$. 1. List all positive divisors $d$ of 36 and write down the unique subgroup $H_d$ of order $d$ for each divisor. 2. How many generators does $\mathbb{Z}_{36}$ have? List all of them explicitly. 3. Find the exact order of the element $[20] \in \mathbb{Z}_{36}$ and determine which subgroup it generates.",
                "hints": [
                    "Divisors of 36: $1, 2, 3, 4, 6, 9, 12, 18, 36$.",
                    "By the Fundamental Theorem, the subgroup of order $d$ is generated by $\\langle 36/d \\rangle$.",
                    "Order formula: $|[a]| = \\frac{n}{\\gcd(n, a)}$."
                ],
                "solution": r"""**Step 1: Positive Divisors and Unique Subgroups**
Divisors of $36$: $d \in \{1, 2, 3, 4, 6, 9, 12, 18, 36\}$.
For each divisor $d$, the unique subgroup of order $d$ is $H_d = \langle 36/d \rangle$:
- $d = 1$: $H_1 = \langle 36 \rangle = \langle 0 \rangle = \{0\}$
- $d = 2$: $H_2 = \langle 18 \rangle = \{0, 18\}$
- $d = 3$: $H_3 = \langle 12 \rangle = \{0, 12, 24\}$
- $d = 4$: $H_4 = \langle 9 \rangle = \{0, 9, 18, 27\}$
- $d = 6$: $H_6 = \langle 6 \rangle = \{0, 6, 12, 18, 24, 30\}$
- $d = 9$: $H_9 = \langle 4 \rangle = \{0, 4, 8, 12, 16, 20, 24, 28, 32\}$
- $d = 12$: $H_{12} = \langle 3 \rangle = \{0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33\}$
- $d = 18$: $H_{18} = \langle 2 \rangle = \{0, 2, 4, \dots, 34\}$ (all even residues)
- $d = 36$: $H_{36} = \langle 1 \rangle = \mathbb{Z}_{36}$

---

**Step 2: Number and List of Generators**
The number of generators of $\mathbb{Z}_{36}$ is $\phi(36)$:
$$36 = 2^2 \times 3^2 \implies \phi(36) = 36 \left(1 - \frac{1}{2}\right) \left(1 - \frac{1}{3}\right) = 36 \times \frac{1}{2} \times \frac{2}{3} = 12$$
The generators are residues $k \in \{1, \dots, 35\}$ coprime to $36$:
$$\text{Generators} = \{1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35\}$$

---

**Step 3: Order and Subgroup Generated by $[20]$**
Using the order formula with $n = 36$ and $a = 20$:
$$\gcd(36, 20) = 4$$
$$|[20]| = \frac{36}{\gcd(36, 20)} = \frac{36}{4} = 9$$
Since $|[20]| = 9$, by the uniqueness assertion of the Fundamental Theorem of Cyclic Groups, $[20]$ generates the unique subgroup of order $9$:
$$\langle 20 \rangle = \langle 4 \rangle = H_9 = \{0, 4, 8, 12, 16, 20, 24, 28, 32\}$$"""
            },
            {
                "tier": "Advanced",
                "title": "Centralizers and Normalizers in the Dihedral Group D_4",
                "statement": r"Consider the Dihedral group $D_4$ of symmetries of a square, with presentation: $$D_4 = \langle r, s \mid r^4 = s^2 = 1, \; s r s = r^{-1} \rangle = \{e, r, r^2, r^3, s, sr, sr^2, sr^3\}$$ 1. Compute the center $Z(D_4)$. 2. Compute the centralizer $C_{D_4}(s)$ of the reflection $s$. 3. Let $H = \{e, s\}$. Compute the normalizer $N_{D_4}(H)$ and determine whether $H$ is a normal subgroup of $D_4$.",
                "hints": [
                    "Recall that $s r = r^{-1} s = r^3 s$. Use this relation to check commutation.",
                    "An element $g$ belongs to $Z(D_4)$ if it commutes with both generators $r$ and $s$."
                ],
                "solution": r"""**Step 1: Compute $Z(D_4)$**
An element $z \in Z(D_4)$ must commute with both generators $r$ and $s$.
- Powers of $r$:
  $r s = s r^{-1} = s r^3 \ne s r \implies r \notin Z(D_4)$.
  $r^3 s = s (r^3)^{-1} = s r \ne s r^3 \implies r^3 \notin Z(D_4)$.
  For $r^2$:
  $$r^2 s = r(r s) = r(s r^3) = (r s) r^3 = (s r^3) r^3 = s r^6 = s r^2$$
  Since $r^2$ also commutes with $r$, $r^2$ commutes with all elements of $D_4$.
- Reflections $s r^k$:
  $s(s r) = r \ne (s r) s = r^{-1} = r^3$.
  Thus no reflection commutes with $s$.
Therefore, the center of $D_4$ is:
$$Z(D_4) = \{e, r^2\}$$
with $|Z(D_4)| = 2$.

---

**Step 2: Compute Centralizer $C_{D_4}(s)$**
By definition:
$$C_{D_4}(s) = \{ g \in D_4 : g s = s g \}$$
Test each element:
1. $e \in C(s)$ trivially.
2. $r \cdot s = s r^3 \ne s r \implies r \notin C(s)$.
3. $r^2 \cdot s = s r^2 \implies r^2 \in C(s)$.
4. $r^3 \cdot s = s r \ne s r^3 \implies r^3 \notin C(s)$.
5. $s \cdot s = s^2 = e = s \cdot s \implies s \in C(s)$.
6. $(s r) s = s(r s) = s(s r^3) = r^3 \ne s(s r) = r \implies s r \notin C(s)$.
7. $(s r^2) s = s(r^2 s) = s(s r^2) = r^2$, while $s(s r^2) = r^2$. They match! So $s r^2 \in C(s)$.
8. $s r^3 s = r \ne s(s r^3) = r^3 \implies s r^3 \notin C(s)$.

Therefore:
$$C_{D_4}(s) = \{e, r^2, s, s r^2\}$$
Notice that $|C_{D_4}(s)| = 4$. This is a subgroup isomorphic to the Klein 4-group $V_4$.

---

**Step 3: Compute Normalizer $N_{D_4}(H)$ for $H = \{e, s\}$**
The normalizer is:
$$N_{D_4}(H) = \{ g \in D_4 : g H g^{-1} = H \}$$
Since $H = \{e, s\}$, $g H g^{-1} = \{g e g^{-1}, g s g^{-1}\} = \{e, g s g^{-1}\}$.
Thus $g H g^{-1} = H \iff g s g^{-1} = s \iff g s = s g \iff g \in C_{D_4}(s)$!
Hence:
$$N_{D_4}(H) = C_{D_4}(s) = \{e, r^2, s, s r^2\}$$
Since $|N_{D_4}(H)| = 4 < |D_4| = 8$, $N_{D_4}(H) \ne D_4$.
For example, for $g = r$:
$$r H r^{-1} = \{e, r s r^{-1}\} = \{e, r(s r^3)\} = \{e, r(r s)\} = \{e, r^2 s\} \ne H$$
Therefore, $H = \{e, s\}$ is **NOT a normal subgroup** of $D_4$."""
            },
            {
                "tier": "Rigorous Examination / Derivation",
                "title": "Complete Proof of the Fundamental Theorem of Cyclic Groups",
                "statement": r"Let $G = \langle a \rangle$ be a finite cyclic group of order $n$. 1. Prove that for every positive divisor $d$ of $n$, the element $b = a^{n/d}$ has order $d$, and generates a subgroup of order $d$. 2. Prove that if $H$ is ANY subgroup of $G$ having order $d$, then $H = \langle a^{n/d} \rangle$ (uniqueness proof). 3. Prove that $\langle a^k \rangle = \langle a^{\gcd(n, k)} \rangle$ for all $k \in \mathbb{Z}$.",
                "hints": [
                    "Use the order formula: $|a^m| = \\frac{n}{\\gcd(n, m)}$.",
                    "For uniqueness, recall that every subgroup $H$ is generated by $a^m$ where $m$ is the smallest positive power in $H$."
                ],
                "solution": r"""**Part 1: Order of $b = a^{n/d}$**

Let $d \mid n$, so $n = d \cdot k$ where $k = n/d \in \mathbb{Z}^+$.
Consider $b = a^k = a^{n/d}$.
Using the element order theorem:
$$|b| = |a^{n/d}| = \frac{n}{\gcd(n, n/d)}$$
Since $n/d$ divides $n$, $\gcd(n, n/d) = n/d$.
Therefore:
$$|b| = \frac{n}{n/d} = d$$
Since the order of a cyclic group equals the order of its generator:
$$|\langle a^{n/d} \rangle| = |b| = d$$
This proves existence of a subgroup of order $d$. $\blacksquare$

---

**Part 2: Proof of Uniqueness of the Subgroup of Order $d$**

Let $H$ be ANY subgroup of $G$ with $|H| = d$. We must prove $H = \langle a^{n/d} \rangle$.
By Part 1 of Theorem 2.6 (already proven in Section 2.2), every subgroup of a cyclic group is cyclic.
Therefore, $H = \langle a^m \rangle$, where $m$ is the smallest positive integer such that $a^m \in H$.

By the order theorem:
$$d = |H| = |a^m| = \frac{n}{\gcd(n, m)}$$
We now establish that $m = \gcd(n, m)$:
Since $\gcd(n, m) \mid m$, we can write $\gcd(n, m) = m x + n y$ by Bézout's identity.
Then:
$$a^{\gcd(n, m)} = a^{mx + ny} = (a^m)^x (a^n)^y = (a^m)^x e^y = (a^m)^x \in H$$
Since $m$ is the MINIMAL positive integer such that $a^m \in H$, and $1 \le \gcd(n, m) \le m$, minimality forces:
$$m = \gcd(n, m)$$
Consequently:
$$m \mid n$$
Substituting $m = \gcd(n, m)$ into the order equation:
$$d = \frac{n}{m} \implies m = \frac{n}{d}$$
Therefore:
$$H = \langle a^m \rangle = \langle a^{n/d} \rangle$$
Since $H$ was an arbitrary subgroup of order $d$, this proves that $\langle a^{n/d} \rangle$ is the **unique** subgroup of order $d$. $\blacksquare$

---

**Part 3: Proof that $\langle a^k \rangle = \langle a^{\gcd(n, k)} \rangle$**

Let $g = \gcd(n, k)$.
1. Since $g \mid k$, $k = g \cdot q$ for some $q \in \mathbb{Z}$.
   Then $a^k = (a^g)^q \in \langle a^g \rangle$.
   Therefore, $\langle a^k \rangle \subseteq \langle a^g \rangle$.
2. By Bézout's identity, there exist $x, y \in \mathbb{Z}$ such that:
   $$g = \gcd(n, k) = k x + n y$$
   Then:
   $$a^g = a^{kx + ny} = (a^k)^x (a^n)^y = (a^k)^x e^y = (a^k)^x \in \langle a^k \rangle$$
   Therefore, $\langle a^g \rangle \subseteq \langle a^k \rangle$.

Combining both inclusions:
$$\langle a^k \rangle = \langle a^{\gcd(n, k)} \rangle \quad \blacksquare$$"""
            }
        ]
    }
    return u2

if __name__ == "__main__":
    u = get_unit2()
    print("Unit 2 generated successfully:", u["title"])
    print("Sections:", len(u["sections"]))
    print("Problems:", len(u["problems"]))
