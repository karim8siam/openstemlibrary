# -*- coding: utf-8 -*-
"""
build_aa_unit4.py
Constructs Unit 4: Cosets, Lagrange's Theorem, Normal Subgroups & Quotient Groups
"""

def get_unit4():
    u4 = {
        "number": 4,
        "title": "Cosets, Lagrange's Theorem, Normal Subgroups & Quotient Groups",
        "leadSummary": "Comprehensive study of coset partitions, Lagrange's Theorem and its foundational corollaries, Euler's totient function and Fermat's Little Theorem, normal subgroups, quotient groups (factor groups), conjugacy classes, the class equation, and the structural decomposition of finite groups.",
        "simulations": ["sim_aa_coset_partition"],
        "sections": [
            {
                "secNumber": "4.1",
                "title": "Left and Right Cosets & Equivalence Relations",
                "content": r"""### 1. Definition of Left and Right Cosets

Let $G$ be a group and let $H$ be a subgroup of $G$ ($H \le G$). For any element $g \in G$:

> **Definition 4.1 (Left Coset):**
> The **left coset** of $H$ in $G$ containing $g$ is the subset:
> $$gH = \{ gh : h \in H \}$$

> **Definition 4.2 (Right Coset):**
> The **right coset** of $H$ in $G$ containing $g$ is the subset:
> $$Hg = \{ hg : h \in H \}$$

The element $g$ is called a **coset representative** of $gH$ (or $Hg$). Notice that if $e \in G$ is the identity element, then $eH = H = He$. Therefore, the subgroup $H$ itself is always both a left coset and a right coset (represented by $e$ or any element $h \in H$).

---

### 2. Equivalence Relation Induced by a Subgroup

Cosets arise naturally from an equivalence relation on the elements of $G$.

> **Theorem 4.1 (Coset Equivalence Relation):**
> Let $H \le G$. Define a binary relation $\sim_L$ on $G$ by:
> $$a \sim_L b \iff a^{-1} b \in H$$
> Then $\sim_L$ is an equivalence relation on $G$, and the equivalence class of $a \in G$ is precisely the left coset $aH$.

#### Complete Proof:
1. **Reflexivity:**
   For any $a \in G$, $a^{-1} a = e$. Since $H$ is a subgroup, $e \in H$. Thus $a^{-1} a \in H$, which implies $a \sim_L a$.
2. **Symmetry:**
   Suppose $a \sim_L b$. Then $a^{-1} b \in H$.
   Since $H$ is closed under inversion:
   $$(a^{-1} b)^{-1} = b^{-1} (a^{-1})^{-1} = b^{-1} a \in H$$
   Therefore, $b \sim_L a$.
3. **Transitivity:**
   Suppose $a \sim_L b$ and $b \sim_L c$. Then $a^{-1} b \in H$ and $b^{-1} c \in H$.
   Since $H$ is closed under the group operation:
   $$(a^{-1} b)(b^{-1} c) = a^{-1} (b b^{-1}) c = a^{-1} e c = a^{-1} c \in H$$
   Therefore, $a \sim_L c$.

Thus $\sim_L$ is an equivalence relation.
Now let us compute the equivalence class $[a]$:
$$[a] = \{ x \in G : a \sim_L x \} = \{ x \in G : a^{-1} x \in H \}$$
If $a^{-1} x = h \in H$, multiplying on the left by $a$ yields $x = ah \in aH$.
Conversely, if $x \in aH$, then $x = ah$ for some $h \in H$, so $a^{-1} x = h \in H$, meaning $x \in [a]$.
Thus $[a] = aH$. $\blacksquare$

---

### 3. Fundamental Properties of Cosets

> **Lemma 4.1 (Coset Properties):**
> Let $H \le G$ and $a, b \in G$.
> 1. $a \in aH$ (since $e \in H$, $a = ae \in aH$).
> 2. $aH = H \iff a \in H$.
> 3. $aH = bH \iff a^{-1} b \in H \iff b \in aH$.
> 4. Either $aH = bH$ or $aH \cap bH = \emptyset$ (left cosets partition $G$).
> 5. There exists a bijection between $H$ and any left coset $aH$, so $|aH| = |H|$.
> 6. There exists a bijection between any left coset $aH$ and the right coset $Ha^{-1}$, so the number of left cosets equals the number of right cosets.

#### Proof of Cardinality Equality ($|aH| = |H|$):
Define the mapping $\psi: H \to aH$ by $\psi(h) = ah$ for all $h \in H$.
- **Surjectivity:** By definition of $aH$, any element $x \in aH$ has the form $x = ah$ for some $h \in H$, so $\psi(h) = x$.
- **Injectivity:** Suppose $\psi(h_1) = \psi(h_2)$. Then $ah_1 = ah_2$.
  Multiplying on the left by $a^{-1}$:
  $$a^{-1}(ah_1) = a^{-1}(ah_2) \implies (a^{-1}a)h_1 = (a^{-1}a)h_2 \implies h_1 = h_2$$
Thus $\psi$ is a bijection, and $|aH| = |H|$. In the case of finite groups, every left coset has identical cardinality $|H|$. $\blacksquare$"""
            },
            {
                "secNumber": "4.2",
                "title": "Lagrange's Theorem & Foundational Corollaries",
                "content": r"""### 1. Lagrange's Theorem for Finite Groups

Lagrange's Theorem is widely regarded as the cornerstone of finite group theory.

> **Theorem 4.2 (Lagrange's Theorem):**
> If $G$ is a finite group and $H$ is a subgroup of $G$, then the order of $H$ divides the order of $G$:
> $$|H| \;\Big|\; |G|$$
> Moreover, the number of distinct left (or right) cosets of $H$ in $G$, denoted by $[G : H]$ (the **index** of $H$ in $G$), satisfies:
> $$|G| = [G : H] \cdot |H| \iff [G : H] = \frac{|G|}{|H|}$$

#### Complete Proof:
1. By Theorem 4.1, the relation $a \sim b \iff a^{-1} b \in H$ is an equivalence relation on $G$.
2. By the Fundamental Theorem of Equivalence Relations (Theorem 1.1), the equivalence classes—which are the distinct left cosets $a_1 H, a_2 H, \dots, a_k H$—form a partition of $G$.
3. Therefore:
   $$G = a_1 H \cup a_2 H \cup \dots \cup a_k H$$
   where $a_i H \cap a_j H = \emptyset$ for all $i \ne j$.
4. Taking the cardinality of both sides:
   $$|G| = \sum_{i=1}^k |a_i H|$$
5. By Lemma 4.1, every left coset has exactly $|H|$ elements: $|a_i H| = |H|$ for all $i = 1, \dots, k$.
6. Substituting this into the sum:
   $$|G| = \sum_{i=1}^k |H| = k \cdot |H|$$
7. Here $k$ is by definition the number of distinct left cosets, denoted $[G : H]$.
8. Thus $|G| = [G : H] \cdot |H|$, which proves that $|H|$ divides $|G|$ and $[G : H] = |G| / |H|$. $\blacksquare$

---

### 2. Immediate Corollaries of Lagrange's Theorem

Lagrange's theorem yields profound structural consequences across group theory:

> **Corollary 4.2.1 (Element Order Divides Group Order):**
> Let $G$ be a finite group. For any element $g \in G$, the order of $g$ divides the order of $G$:
> $$|g| \;\Big|\; |G|$$

#### Proof:
The cyclic subgroup generated by $g$, $\langle g \rangle = \{ g^k : k \in \mathbb{Z} \}$, has order $|\langle g \rangle| = |g|$.
Since $\langle g \rangle \le G$, Lagrange's Theorem immediately implies that $|\langle g \rangle| \Big| |G|$, hence $|g| \Big| |G|$. $\blacksquare$

> **Corollary 4.2.2 (Group Power Exponent):**
> Let $G$ be a finite group of order $n = |G|$. For every element $g \in G$:
> $$g^n = g^{|G|} = e$$

#### Proof:
Let $m = |g|$. By Corollary 4.2.1, $m \mid n$, so there exists an integer $k \in \mathbb{Z}^+$ such that $n = m \cdot k$.
Then:
$$g^n = g^{m \cdot k} = (g^m)^k = e^k = e \quad \blacksquare$$

> **Corollary 4.2.3 (Groups of Prime Order are Cyclic):**
> Let $G$ be a group of prime order $p$. Then $G$ is cyclic, and any non-identity element $g \ne e$ is a generator of $G$:
> $$G \cong \mathbb{Z}_p$$

#### Proof:
Since $|G| = p \ge 2$, choose any element $g \in G$ with $g \ne e$.
Consider the subgroup $H = \langle g \rangle$. Since $g \ne e$, $|H| \ge 2$.
By Lagrange's Theorem, $|H|$ must divide $|G| = p$.
Because $p$ is a prime number, its only positive divisors are $1$ and $p$.
Since $|H| \ne 1$, it must be that $|H| = p$.
Therefore, $H = G$, meaning $G = \langle g \rangle$. Thus $G$ is cyclic and isomorphic to $\mathbb{Z}_p$. $\blacksquare$"""
            },
            {
                "secNumber": "4.3",
                "title": "Euler's Totient Function, Euler's Theorem & Fermat's Little Theorem",
                "content": r"""### 1. The Group of Units $U(n)$

Recall from Unit 1 that for any integer $n \ge 2$, the set of invertible elements modulo $n$ under multiplication forms a group:
$$U(n) = (\mathbb{Z}_n)^\times = \{ [a] \in \mathbb{Z}_n : \gcd(a, n) = 1 \}$$

> **Definition 4.3 (Euler's Totient Function $\phi(n)$):**
> The **totient function** $\phi(n)$ is defined as the number of integers in $\{1, 2, \dots, n\}$ that are coprime to $n$:
> $$\phi(n) = |U(n)|$$

#### Formula for $\phi(n)$:
If $n = p_1^{k_1} p_2^{k_2} \cdots p_r^{k_r}$ is the prime factorization of $n$, then:
$$\phi(n) = n \prod_{i=1}^r \left(1 - \frac{1}{p_i}\right) = \prod_{i=1}^r p_i^{k_i - 1}(p_i - 1)$$

---

### 2. Euler's Totient Theorem

We now obtain Euler's celebrated theorem in number theory as a direct 1-line corollary of Lagrange's Theorem!

> **Theorem 4.3 (Euler's Theorem):**
> If $a$ and $n$ are coprime integers ($\gcd(a, n) = 1$ with $n \ge 1$), then:
> $$a^{\phi(n)} \equiv 1 \pmod n$$

#### Group-Theoretic Proof:
1. Consider the group of units $G = U(n) = (\mathbb{Z}_n)^\times$.
2. The order of this group is $|G| = \phi(n)$.
3. Since $\gcd(a, n) = 1$, the equivalence class $[a]$ is an element of $G$.
4. By Corollary 4.2.2 (Group Power Exponent), for every element $g \in G$, $g^{|G|} = e$.
5. Applying this to $g = [a]$ and $|G| = \phi(n)$:
   $$[a]^{\phi(n)} = [1] \in U(n)$$
6. In modular congruence notation, this translates directly to:
   $$a^{\phi(n)} \equiv 1 \pmod n \quad \blacksquare$$

---

### 3. Fermat's Little Theorem

> **Corollary 4.3.1 (Fermat's Little Theorem):**
> If $p$ is a prime number and $a \in \mathbb{Z}$ is not divisible by $p$ ($p \nmid a$), then:
> $$a^{p-1} \equiv 1 \pmod p$$
> Equivalent formulation for all $a \in \mathbb{Z}$:
> $$a^p \equiv a \pmod p$$

#### Proof:
Since $p$ is prime, all integers $1, 2, \dots, p-1$ are coprime to $p$, so $\phi(p) = p - 1$.
Applying Euler's Theorem directly with $n = p$:
$$a^{\phi(p)} = a^{p-1} \equiv 1 \pmod p$$
Multiplying both sides by $a$ gives $a^p \equiv a \pmod p$.
If $p \mid a$, then $a \equiv 0 \pmod p$, so $0^p \equiv 0 \pmod p$ trivially holds.
Thus $a^p \equiv a \pmod p$ holds for all $a \in \mathbb{Z}$. $\blacksquare$"""
            },
            {
                "secNumber": "4.4",
                "title": "Normal Subgroups, Conjugacy & The Class Equation",
                "content": r"""### 1. The Necessity of Normal Subgroups

When can the set of left cosets $G/H = \{ gH : g \in G \}$ be endowed with a natural group structure?
Suppose we attempt to define coset multiplication by:
$$(aH)(bH) = (ab)H$$
This operation is **well-defined** if and only if the product does not depend on the choice of representatives $a$ and $b$. That is, if $a_1 \in aH$ and $b_1 \in bH$, we must have $(a_1 b_1)H = (ab)H$.
As we will prove, this holds **if and only if** $H$ is a **normal subgroup**.

> **Definition 4.4 (Normal Subgroup):**
> A subgroup $N \le G$ is called a **normal subgroup** of $G$, denoted by $N \trianglelefteq G$ (or $N \triangleleft G$ if proper), if:
> $$g N g^{-1} = N, \quad \forall g \in G$$
> where $g N g^{-1} = \{ g n g^{-1} : n \in N \}$.

---

### 2. Equivalent Characterizations of Normality

> **Theorem 4.4 (Characterization of Normal Subgroups):**
> Let $N \le G$. The following statements are mutually equivalent:
> 1. $N \trianglelefteq G$ (i.e., $g N g^{-1} = N$ for all $g \in G$).
> 2. $g N g^{-1} \subseteq N$ for all $g \in G$.
> 3. $g N = N g$ for all $g \in G$ (every left coset is a right coset).
> 4. $(aN)(bN) = (ab)N$ is a well-defined binary operation on the set of cosets $G/N$.

#### Proof of Equivalence ($2 \implies 1$ and $1 \iff 3$):
- **$2 \implies 1$:** Suppose $g N g^{-1} \subseteq N$ for all $g \in G$.
  Replacing $g$ with $g^{-1} \in G$:
  $$g^{-1} N (g^{-1})^{-1} \subseteq N \implies g^{-1} N g \subseteq N$$
  Now multiply on the left by $g$ and on the right by $g^{-1}$:
  $$g (g^{-1} N g) g^{-1} \subseteq g N g^{-1} \implies N \subseteq g N g^{-1}$$
  Combining $g N g^{-1} \subseteq N$ and $N \subseteq g N g^{-1}$ yields $g N g^{-1} = N$.
- **$1 \iff 3$:** Suppose $g N g^{-1} = N$. Multiplying both sides on the right by $g$:
  $$(g N g^{-1}) g = N g \implies g N (g^{-1} g) = N g \implies g N = N g$$
  Conversely, if $g N = N g$, multiplying on the right by $g^{-1}$ gives $g N g^{-1} = N$. $\blacksquare$

> **Proposition 4.1 (Subgroups of Index 2 are Normal):**
> If $H \le G$ with $[G : H] = 2$, then $H \trianglelefteq G$.

#### Proof:
Since $[G : H] = 2$, there are exactly two left cosets of $H$ in $G$. One is $eH = H$.
The other must be the complement of $H$ in $G$:
$$gH = G \setminus H, \quad \forall g \notin H$$
Similarly, there are exactly two right cosets of $H$ in $G$: $He = H$ and $Hg = G \setminus H$ for all $g \notin H$.
Thus, for all $g \in G$:
- If $g \in H$, $gH = H = Hg$.
- If $g \notin H$, $gH = G \setminus H = Hg$.
In both cases $gH = Hg$. Therefore $H \trianglelefteq G$. $\blacksquare$

---

### 3. Conjugacy Classes and the Class Equation

Recall the action of $G$ on itself by conjugation: $g \cdot x = g x g^{-1}$.
The orbit of an element $x \in G$ under this action is its **conjugacy class**:
$$\text{Cl}(x) = \{ g x g^{-1} : g \in G \}$$
The stabilizer of $x$ is the **centralizer** $C_G(x) = \{ g \in G : gx = xg \}$.
By the Orbit-Stabilizer Theorem (Theorem 3.4):
$$|\text{Cl}(x)| = [G : C_G(x)] = \frac{|G|}{|C_G(x)|}$$
An element $x$ has $|\text{Cl}(x)| = 1 \iff g x g^{-1} = x$ for all $g \in G \iff gx = xg$ for all $g \in G \iff x \in Z(G)$, where $Z(G)$ is the **center** of $G$.

> **Theorem 4.5 (The Class Equation):**
> Let $G$ be a finite group. Let $x_1, x_2, \dots, x_k$ be representatives of the distinct conjugacy classes of size $> 1$. Then:
> $$|G| = |Z(G)| + \sum_{i=1}^k [G : C_G(x_i)]$$

#### Proof:
Since conjugacy is an equivalence relation, $G$ is partitioned into disjoint conjugacy classes:
$$G = \bigcup_{x} \text{Cl}(x)$$
The classes of size 1 are precisely the elements in $Z(G)$, of which there are $|Z(G)|$.
Summing the cardinalities of all disjoint classes yields:
$$|G| = |Z(G)| + \sum_{i=1}^k |\text{Cl}(x_i)| = |Z(G)| + \sum_{i=1}^k [G : C_G(x_i)] \quad \blacksquare$$"""
            },
            {
                "secNumber": "4.5",
                "title": "Quotient Groups & The Group Structure of $G/N$",
                "content": r"""### 1. Construction of the Quotient Group (Factor Group)

Let $N \trianglelefteq G$. The collection of all cosets of $N$ in $G$ is denoted:
$$G/N = \{ gN : g \in G \}$$
Read as "$G$ modulo $N$" or "$G \bmod N$".

> **Theorem 4.6 (Quotient Group Axioms):**
> Let $N$ be a normal subgroup of $G$. The set $G/N$ forms a group under coset multiplication:
> $$(aN)(bN) = (ab)N, \quad \forall a, b \in G$$

#### Complete Verification of Group Axioms:
1. **Well-Definedness:**
   Suppose $a_1 N = a_2 N$ and $b_1 N = b_2 N$.
   Then $a_2 = a_1 n_1$ and $b_2 = b_1 n_2$ for some $n_1, n_2 \in N$.
   We must show $(a_2 b_2)N = (a_1 b_1)N$, which is equivalent to showing $(a_1 b_1)^{-1} (a_2 b_2) \in N$:
   $$\begin{aligned}
   (a_1 b_1)^{-1} (a_2 b_2) &= b_1^{-1} a_1^{-1} (a_1 n_1) (b_1 n_2) \\
   &= b_1^{-1} (a_1^{-1} a_1) n_1 b_1 n_2 \\
   &= b_1^{-1} n_1 b_1 n_2
   \end{aligned}$$
   Since $N \trianglelefteq G$, $b_1^{-1} n_1 (b_1^{-1})^{-1} = b_1^{-1} n_1 b_1 \in N$.
   Let $n_3 = b_1^{-1} n_1 b_1 \in N$.
   Then $(a_1 b_1)^{-1} (a_2 b_2) = n_3 n_2 \in N$ (by closure of $N$).
   Thus $(a_2 b_2)N = (a_1 b_1)N$. The operation is well-defined!
2. **Associativity:**
   For any $a, b, c \in G$:
   $$\begin{aligned}
   ((aN)(bN))(cN) &= ((ab)N)(cN) = ((ab)c)N \\
   &= (a(bc))N = (aN)((bc)N) = (aN)((bN)(cN))
   \end{aligned}$$
   Inherited directly from associativity of $G$.
3. **Identity Element:**
   The coset $eN = N$ serves as the identity element:
   $$(aN)(eN) = (ae)N = aN \quad \text{and} \quad (eN)(aN) = (ea)N = aN$$
4. **Inverses:**
   For any $aN \in G/N$, the inverse is $(aN)^{-1} = a^{-1}N$:
   $$(aN)(a^{-1}N) = (a a^{-1})N = eN = N$$
   $$(a^{-1}N)(aN) = (a^{-1} a)N = eN = N$$
Thus $(G/N, \cdot)$ is a group! $\blacksquare$

---

### 2. The Canonical (Natural) Projection

> **Definition 4.5 (Canonical Projection):**
> The map $\pi: G \to G/N$ defined by $\pi(g) = gN$ is a surjective group homomorphism called the **canonical projection** (or natural projection).
> Its kernel is precisely $N$:
> $$\ker(\pi) = \{ g \in G : \pi(g) = e_{G/N} \} = \{ g \in G : gN = N \} = N$$

This establishes the profound duality: **every normal subgroup is the kernel of a homomorphism, and the kernel of every homomorphism is a normal subgroup**."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational",
                "title": "Coset Decomposition of the Dihedral Group $D_8$ and Index Calculation",
                "statement": r"Consider the dihedral group of symmetries of the square: $D_8 = \langle r, s \mid r^4 = 1, s^2 = 1, srs = r^{-1} \rangle = \{1, r, r^2, r^3, s, sr, sr^2, sr^3\}$. 1. Let $H = \langle s \rangle = \{1, s\}$. Compute all left cosets of $H$ in $D_8$ and show explicitly that they partition $D_8$. 2. Compute all right cosets of $H$ in $D_8$. Is $H$ normal in $D_8$? 3. Let $K = \langle r^2 \rangle = \{1, r^2\}$. Show that $K$ is a normal subgroup of $D_8$, compute the quotient group $D_8/K$, and determine its isomorphism type.",
                "hints": [
                    "For left cosets, compute $gH = \{g, gs\}$ for representative elements $g \\in D_8$.",
                    "To test normality, check whether $r H = H r$.",
                    "For $D_8/K$, note that $|D_8/K| = 8/2 = 4$. Any group of order 4 is either $\\mathbb{Z}_4$ or the Klein four-group $V_4$."
                ],
                "solution": r"""**Step 1: Left Cosets of $H = \{1, s\}$**

The order of $D_8$ is $8$ and $|H| = 2$. By Lagrange's Theorem, the number of cosets is $[D_8 : H] = 8/2 = 4$.
- $1H = \{1, s\}$
- $rH = \{r \cdot 1, r \cdot s\} = \{r, rs\} = \{r, sr^3\}$ (since $rs = sr^{-1} = sr^3$)
- $r^2 H = \{r^2, r^2 s\} = \{r^2, sr^2\}$
- $r^3 H = \{r^3, r^3 s\} = \{r^3, sr\}$

Notice:
$$1H \cup rH \cup r^2H \cup r^3H = \{1, s\} \cup \{r, sr^3\} \cup \{r^2, sr^2\} \cup \{r^3, sr\} = D_8$$
The cosets are disjoint and their union is all 8 elements of $D_8$.

---

**Step 2: Right Cosets of $H$ and Normality Check**

Compute the right cosets $Hg = \{g, sg\}$:
- $H1 = \{1, s\}$
- $Hr = \{r, sr\}$
- $Hr^2 = \{r^2, sr^2\}$
- $Hr^3 = \{r^3, sr^3\}$

Comparing left and right cosets:
$$rH = \{r, sr^3\} \quad \text{while} \quad Hr = \{r, sr\}$$
Since $\{r, sr^3\} \ne \{r, sr\}$, we have $rH \ne Hr$.
Therefore, $H = \langle s \rangle$ is **not normal** in $D_8$.

---

**Step 3: Subgroup $K = \langle r^2 \rangle$ and Quotient Group $D_8/K$**

We have $K = \{1, r^2\}$. Check normality of $K$:
- For any rotation $r^k$: $r^k (r^2) r^{-k} = r^{k+2-k} = r^2 \in K$.
- For any reflection $s r^k$:
  $$(s r^k) r^2 (s r^k)^{-1} = s r^k r^2 r^{-k} s = s r^2 s = (s r s)^2 = (r^{-1})^2 = r^{-2} = r^2 \in K$$
Since $g K g^{-1} \subseteq K$ for all $g \in D_8$, $K$ is in the center $Z(D_8)$, hence $K \trianglelefteq D_8$.

#### Quotient Group $D_8/K$:
The order is $|D_8/K| = 8/2 = 4$.
The elements of $D_8/K$ are:
$$D_8/K = \{ K, \; rK, \; sK, \; srK \}$$
Let us check the orders of the non-identity elements:
- $(rK)^2 = r^2 K = K$ (since $r^2 \in K$). Thus $|rK| = 2$.
- $(sK)^2 = s^2 K = 1K = K$. Thus $|sK| = 2$.
- $(srK)^2 = (sr)^2 K = 1K = K$ (since reflections have order 2). Thus $|srK| = 2$.

Every non-identity element in $D_8/K$ has order $2$!
Therefore, the quotient group is isomorphic to the **Klein four-group**:
$$D_8 / \langle r^2 \rangle \cong V_4 \cong \mathbb{Z}_2 \times \mathbb{Z}_2 \quad \blacksquare$$"""
            },
            {
                "tier": "Advanced",
                "title": "Subgroups of Smallest Prime Index & Abelian Nature of Order $p^2$ Groups",
                "statement": r"1. Let $G$ be a finite group and let $p$ be the smallest prime dividing $|G|$. Prove that if $H \le G$ has index $[G : H] = p$, then $H \trianglelefteq G$. 2. Use the Class Equation to prove that if $p$ is prime and $|G| = p^2$, then $G$ must be abelian.",
                "hints": [
                    "For Part 1, consider the group action of $G$ on the set of left cosets $G/H$ via left multiplication: $g \\cdot (xH) = (gx)H$. This induces a homomorphism $\\phi: G \\to S_p$. Examine $|G / \\ker(\\phi)|$.",
                    "For Part 2, express $|G| = |Z(G)| + \\sum [G : C_G(x_i)]$. Each term $[G : C_G(x_i)]$ must divide $p^2$ and be $> 1$."
                ],
                "solution": r"""**Part 1: Proof that a Subgroup of Smallest Prime Index is Normal**

Let $G$ be a finite group, and let $p$ be the smallest prime dividing $|G|$.
Suppose $H \le G$ with $[G : H] = p$.
Let $S = G/H = \{ x_1 H, x_2 H, \dots, x_p H \}$ be the set of left cosets, with $|S| = p$.
Define the action of $G$ on $S$ by left multiplication:
$$g \cdot (x H) = (gx) H, \quad \forall g \in G, \; xH \in S$$
This action induces a permutation representation:
$$\phi: G \to \text{Sym}(S) \cong S_p$$
where $\phi(g)$ is the permutation $\pi_g(xH) = (gx)H$.

Let $K = \ker(\phi)$. By definition of kernel, $K \trianglelefteq G$.
Notice that if $k \in K$, then $\phi(k)$ is the identity permutation, so $k \cdot (eH) = eH \implies kH = H \implies k \in H$.
Thus:
$$K \le H \le G$$
By the First Isomorphism Theorem:
$$G/K \cong \text{im}(\phi) \le S_p$$
Therefore, $|G/K|$ divides $|S_p| = p!$.
On the other hand, by Lagrange's Theorem applied to $K \le H \le G$:
$$|G/K| = [G : K] = [G : H][H : K] = p \cdot [H : K]$$
Hence $p \cdot [H : K]$ divides $|G|$ and also divides $p!$.
This means $[H : K]$ divides $\frac{p!}{p} = (p-1)!$.
However, every prime factor of $[H : K]$ must divide $|G|$ (since $[H : K]$ divides $|G|$).
By hypothesis, $p$ is the **smallest** prime dividing $|G|$.
Therefore, $|G|$ has NO prime divisors strictly less than $p$!
Since all prime factors of $(p-1)!$ are strictly less than $p$, $\gcd(|G|, (p-1)!) = 1$.
Consequently, $[H : K]$ cannot have any prime divisors $> 1$, which forces:
$$[H : K] = 1 \implies H = K$$
Since $K = \ker(\phi)$ is normal in $G$, it follows that $H \trianglelefteq G$. $\blacksquare$

---

**Part 2: Groups of Order $p^2$ are Abelian**

Let $|G| = p^2$ where $p$ is prime.
By the Class Equation (Theorem 4.5):
$$|G| = |Z(G)| + \sum_{i=1}^k [G : C_G(x_i)]$$
where each $x_i$ is a representative of a non-central conjugacy class, so $[G : C_G(x_i)] > 1$.
By Lagrange's Theorem, each index $[G : C_G(x_i)]$ must divide $|G| = p^2$.
Since $[G : C_G(x_i)] > 1$, it must be that $[G : C_G(x_i)]$ is either $p$ or $p^2$.
In either case, $p \;\Big|\; [G : C_G(x_i)]$ for every term in the sum.
Therefore:
$$|Z(G)| = |G| - \sum_{i=1}^k [G : C_G(x_i)] \equiv 0 - 0 \equiv 0 \pmod p$$
Thus $p$ divides $|Z(G)|$.
Since $Z(G) \le G$, $|Z(G)|$ must divide $|G| = p^2$, so $|Z(G)| \in \{1, p, p^2\}$.
Since $p \mid |Z(G)|$, $|Z(G)| \ne 1$.
Hence $|Z(G)|$ is either $p$ or $p^2$.

**Case 1: $|Z(G)| = p^2$**
Then $Z(G) = G$, which means $G$ is abelian!

**Case 2: Suppose $|Z(G)| = p$**
Then $|G / Z(G)| = \frac{|G|}{|Z(G)|} = \frac{p^2}{p} = p$.
Since $p$ is prime, by Corollary 4.2.3, the quotient group $G / Z(G)$ is cyclic!
We now invoke the fundamental lemma:
> *If $G / Z(G)$ is cyclic, then $G$ is abelian.*
*(Proof: Let $G / Z(G) = \langle g Z(G) \rangle$. Any element $x \in G$ can be written as $x = g^a z_1$ and any $y \in G$ as $y = g^b z_2$ with $z_1, z_2 \in Z(G)$. Then $xy = g^a z_1 g^b z_2 = g^{a+b} z_1 z_2 = g^b z_2 g^a z_1 = yx$.)*

If $G$ is abelian, then $Z(G) = G$, so $|Z(G)| = p^2$, contradicting $|Z(G)| = p$!
Therefore, Case 2 is impossible.
The only possibility is $|Z(G)| = p^2$, which proves that $G$ is abelian. $\blacksquare$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Classification of Groups of Order $p^2$ and the $G/Z(G)$ Theorem",
                "statement": r"1. Provide a rigorous, self-contained proof that if $G / Z(G)$ is cyclic, then $G$ is abelian. 2. Using this result along with Part 2 of the previous problem, classify all groups of order $p^2$ up to isomorphism, proving that any group of order $p^2$ is isomorphic to either $\mathbb{Z}_{p^2}$ or $\mathbb{Z}_p \times \mathbb{Z}_p$.",
                "hints": [
                    "For Part 1, pick a generator $g Z(G)$ of the cyclic quotient $G/Z(G)$, and write any two elements $x, y \\in G$ as $g^a z_1$ and $g^b z_2$ where $z_1, z_2 \\in Z(G)$.",
                    "For Part 2, if $G$ contains an element of order $p^2$, it is cyclic. If every non-identity element has order $p$, pick $x \\in G \\setminus \\{e\\}$ and $y \\notin \\langle x \\rangle$, and construct an isomorphism to $\\mathbb{Z}_p \\times \\mathbb{Z}_p$."
                ],
                "solution": r"""**Part 1: Rigorous Proof of the $G/Z(G)$ Theorem**

> **Theorem:** If $G / Z(G)$ is cyclic, then $G$ is abelian.

#### Proof:
Let $G / Z(G)$ be cyclic, generated by the coset $g Z(G)$ for some $g \in G$:
$$G / Z(G) = \langle g Z(G) \rangle = \{ (g Z(G))^k : k \in \mathbb{Z} \} = \{ g^k Z(G) : k \in \mathbb{Z} \}$$
Let $x, y \in G$ be arbitrary elements.
Since $x Z(G), y Z(G) \in G / Z(G)$, there exist integers $m, n \in \mathbb{Z}$ such that:
$$x Z(G) = g^m Z(G) \quad \text{and} \quad y Z(G) = g^n Z(G)$$
By definition of coset equality, this implies there exist elements $z_1, z_2 \in Z(G)$ such that:
$$x = g^m z_1 \quad \text{and} \quad y = g^n z_2$$
Now compute the product $x y$:
$$x y = (g^m z_1)(g^n z_2)$$
Since $z_1 \in Z(G)$, it commutes with every element in $G$, in particular with $g^n$:
$$x y = g^m (z_1 g^n) z_2 = g^m (g^n z_1) z_2 = (g^m g^n)(z_1 z_2) = g^{m+n}(z_1 z_2)$$
Similarly, compute $y x$:
$$y x = (g^n z_2)(g^m z_1) = g^n (z_2 g^m) z_1 = g^n (g^m z_2) z_1 = (g^n g^m)(z_2 z_1) = g^{n+m}(z_2 z_1)$$
Since $g^m g^n = g^{m+n} = g^{n+m}$ and $z_1, z_2 \in Z(G)$ commute ($z_1 z_2 = z_2 z_1$):
$$x y = g^{m+n}(z_1 z_2) = g^{n+m}(z_2 z_1) = y x$$
Since $x$ and $y$ were arbitrary elements of $G$, $G$ is abelian. $\blacksquare$

---

**Part 2: Classification of Groups of Order $p^2$**

Let $G$ be a group of order $p^2$ ($p$ prime).
From our previous result, $G$ is abelian.
By Corollary 4.2.1, the order of any element $g \in G$ divides $|G| = p^2$.
Hence for all $g \ne e$, $|g| \in \{p, p^2\}$.

**Subcase A: There exists an element $a \in G$ with $|a| = p^2$.**
In this case, the cyclic subgroup $\langle a \rangle$ has order $p^2 = |G|$.
Therefore, $G = \langle a \rangle \cong \mathbb{Z}_{p^2}$.

**Subcase B: Every non-identity element $g \in G \setminus \{e\}$ has order $p$.**
Choose an element $x \in G$ with $x \ne e$. Then $|x| = p$, and $H = \langle x \rangle$ is a cyclic subgroup of order $p$.
Since $|H| = p < p^2 = |G|$, there exists an element $y \in G$ such that $y \notin H$.
The element $y$ also has order $p$, so $K = \langle y \rangle$ is a cyclic subgroup of order $p$.
Consider the intersection $H \cap K$:
$H \cap K$ is a subgroup of both $H$ and $K$.
By Lagrange's Theorem, $|H \cap K|$ must divide $|H| = p$.
Since $y \notin H$ and $y \in K$, $K \not\subseteq H$, which means $H \cap K \ne K$.
Thus $|H \cap K| < p$. The only positive divisor of $p$ strictly less than $p$ is $1$.
Therefore:
$$H \cap K = \{e\}$$

Now consider the product set:
$$H K = \{ h k : h \in H, k \in K \} = \{ x^i y^j : 0 \le i, j < p \}$$
Since $G$ is abelian, $H K \le G$.
The number of elements in $H K$ is given by:
$$|H K| = \frac{|H| \cdot |K|}{|H \cap K|} = \frac{p \cdot p}{1} = p^2 = |G|$$
Therefore, $H K = G$.
Since $G$ is abelian, both $H$ and $K$ are normal subgroups of $G$.
Because $H \cap K = \{e\}$ and $H K = G$, $G$ is the internal direct product of $H$ and $K$:
$$G \cong H \times K$$
Since $H = \langle x \rangle \cong \mathbb{Z}_p$ and $K = \langle y \rangle \cong \mathbb{Z}_p$:
$$G \cong \mathbb{Z}_p \times \mathbb{Z}_p$$

**Conclusion:**
Every group of order $p^2$ is isomorphic to either $\mathbb{Z}_{p^2}$ or $\mathbb{Z}_p \times \mathbb{Z}_p$.
There are exactly two isomorphism classes of groups of order $p^2$, and both are abelian. $\blacksquare$"""
            }
        ]
    }
    return u4

if __name__ == "__main__":
    u = get_unit4()
    print("Unit 4 generated successfully:", u["title"])
    print("Sections:", len(u["sections"]))
    print("Problems:", len(u["problems"]))
