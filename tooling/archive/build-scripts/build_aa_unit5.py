# -*- coding: utf-8 -*-
"""
build_aa_unit5.py
Constructs Unit 5: Group Homomorphisms, Isomorphism Theorems & Automorphisms
"""

def get_unit5():
    u5 = {
        "number": 5,
        "title": "Group Homomorphisms, Isomorphism Theorems & Automorphisms",
        "leadSummary": "Exhaustive exploration of structure-preserving maps in abstract algebra: group homomorphisms, kernels, images, the First, Second (Diamond), and Third Isomorphism Theorems with complete formal proofs, Cayley's representation theorem, the automorphism group Aut(G), inner automorphisms Inn(G), and characteristic subgroups.",
        "simulations": ["sim_aa_homomorphism_kernel"],
        "sections": [
            {
                "secNumber": "5.1",
                "title": "Group Homomorphisms, Kernels & Fundamental Properties",
                "content": r"""### 1. Definition of a Group Homomorphism

Let $(G, \cdot)$ and $(H, *)$ be two groups.

> **Definition 5.1 (Homomorphism):**
> A function $\phi: G \to H$ is called a **group homomorphism** if it preserves the group operation:
> $$\phi(a \cdot b) = \phi(a) * \phi(b), \quad \forall a, b \in G$$

- If $\phi$ is injective (one-to-one), it is called a **monomorphism** (or embedding).
- If $\phi$ is surjective (onto), it is called an **epimorphism**.
- If $\phi$ is bijective (both injective and surjective), it is called an **isomorphism**, denoted $G \cong H$.
- An isomorphism from $G$ to itself ($\phi: G \to G$) is called an **automorphism**.
- A homomorphism from $G$ to itself is called an **endomorphism**.

---

### 2. Fundamental Properties of Homomorphisms

> **Proposition 5.1 (Elementary Properties):**
> Let $\phi: G \to H$ be a homomorphism. Then:
> 1. $\phi(e_G) = e_H$.
> 2. $\phi(g^{-1}) = (\phi(g))^{-1}$ for all $g \in G$.
> 3. $\phi(g^n) = (\phi(g))^n$ for all $g \in G$ and $n \in \mathbb{Z}$.
> 4. If $|g|$ is finite, then $|\phi(g)|$ divides $|g|$.
> 5. If $K \le G$, then $\phi(K) \le H$.
> 6. If $L \le H$, then the preimage $\phi^{-1}(L) \le G$.

#### Proof of 1, 2, and 4:
- **Proof of 1:** $\phi(e_G) = \phi(e_G \cdot e_G) = \phi(e_G) * \phi(e_G)$.
  Multiplying both sides by $(\phi(e_G))^{-1}$ in $H$:
  $$e_H = \phi(e_G) \quad \blacksquare$$
- **Proof of 2:** $\phi(g) * \phi(g^{-1}) = \phi(g \cdot g^{-1}) = \phi(e_G) = e_H$.
  By uniqueness of inverses in $H$, $\phi(g^{-1}) = (\phi(g))^{-1}$. $\blacksquare$
- **Proof of 4:** Let $n = |g|$. Then $g^n = e_G$.
  Applying $\phi$: $(\phi(g))^n = \phi(g^n) = \phi(e_G) = e_H$.
  By Proposition 2.3, this implies $|\phi(g)|$ divides $n = |g|$. $\blacksquare$

---

### 3. Kernel and Image

> **Definition 5.2 (Kernel and Image):**
> Let $\phi: G \to H$ be a group homomorphism.
> 1. The **kernel** of $\phi$ is:
>    $$\ker(\phi) = \{ g \in G : \phi(g) = e_H \} = \phi^{-1}(\{e_H\})$$
> 2. The **image** of $\phi$ is:
>    $$\text{im}(\phi) = \phi(G) = \{ \phi(g) : g \in G \} \subseteq H$$

> **Theorem 5.1 (Kernel is a Normal Subgroup):**
> Let $\phi: G \to H$ be a group homomorphism. Then:
> 1. $\ker(\phi) \trianglelefteq G$.
> 2. $\text{im}(\phi) \le H$.
> 3. $\phi$ is injective if and only if $\ker(\phi) = \{e_G\}$.

#### Complete Proof:
1. **Normality of $\ker(\phi)$:**
   - **Non-emptiness:** $\phi(e_G) = e_H \implies e_G \in \ker(\phi)$.
   - **Subgroup test:** Let $x, y \in \ker(\phi)$. Then:
     $$\phi(x y^{-1}) = \phi(x) * \phi(y^{-1}) = \phi(x) * (\phi(y))^{-1} = e_H * e_H^{-1} = e_H$$
     Thus $x y^{-1} \in \ker(\phi)$, so $\ker(\phi) \le G$.
   - **Normality:** For any $g \in G$ and $k \in \ker(\phi)$:
     $$\phi(g k g^{-1}) = \phi(g) * \phi(k) * \phi(g^{-1}) = \phi(g) * e_H * (\phi(g))^{-1} = \phi(g) * (\phi(g))^{-1} = e_H$$
     Hence $g k g^{-1} \in \ker(\phi)$ for all $g \in G$.
     Therefore, $\ker(\phi) \trianglelefteq G$. $\blacksquare$
2. **Subgroup property of $\text{im}(\phi)$:**
   Let $u, v \in \text{im}(\phi)$. Then $u = \phi(a)$ and $v = \phi(b)$ for some $a, b \in G$.
   $$u v^{-1} = \phi(a) * (\phi(b))^{-1} = \phi(a) * \phi(b^{-1}) = \phi(a b^{-1}) \in \text{im}(\phi)$$
   Thus $\text{im}(\phi) \le H$. $\blacksquare$
3. **Injectivity Criterion:**
   - $(\implies)$ If $\phi$ is injective and $\phi(x) = e_H = \phi(e_G)$, then injectivity implies $x = e_G$. Thus $\ker(\phi) = \{e_G\}$.
   - $(\impliedby)$ Suppose $\ker(\phi) = \{e_G\}$. If $\phi(a) = \phi(b)$, then:
     $$\phi(a b^{-1}) = \phi(a) * (\phi(b))^{-1} = \phi(a) * (\phi(a))^{-1} = e_H$$
     Thus $a b^{-1} \in \ker(\phi) = \{e_G\}$, meaning $a b^{-1} = e_G \implies a = b$.
     Therefore $\phi$ is injective. $\blacksquare$"""
            },
            {
                "secNumber": "5.2",
                "title": "The First Isomorphism Theorem for Groups",
                "content": r"""### 1. Statement of the First Isomorphism Theorem

The First Isomorphism Theorem (often called the **Fundamental Theorem of Homomorphisms**) reveals that every homomorphism $\phi: G \to H$ can be factored into a canonical projection onto a quotient group followed by an isomorphism onto its image.

> **Theorem 5.2 (First Isomorphism Theorem):**
> Let $\phi: G \to H$ be a group homomorphism with kernel $K = \ker(\phi)$.
> Then the quotient group $G/K$ is isomorphic to the image $\text{im}(\phi)$:
> $$G/\ker(\phi) \cong \text{im}(\phi)$$
> Specifically, the mapping:
> $$\Phi: G/K \to \text{im}(\phi), \quad \Phi(gK) = \phi(g)$$
> is a well-defined group isomorphism.

```
       G ------------ \phi ------------> H
       |                                ^
       | \pi                            |
       v                                | \Phi
      G/K ------------ \cong -----------> im(\phi)
```

---

### 2. Complete Rigorous Proof

We must verify four assertions:
1. $\Phi$ is well-defined (independent of coset representative).
2. $\Phi$ is a homomorphism.
3. $\Phi$ is injective.
4. $\Phi$ is surjective.

#### Step 1: Well-Definedness
Suppose $g_1 K = g_2 K$ for $g_1, g_2 \in G$.
Then $g_1^{-1} g_2 \in K = \ker(\phi)$.
This means $\phi(g_1^{-1} g_2) = e_H$.
Since $\phi$ is a homomorphism:
$$\phi(g_1)^{-1} \phi(g_2) = e_H \implies \phi(g_1) = \phi(g_2)$$
Therefore, $\Phi(g_1 K) = \phi(g_1) = \phi(g_2) = \Phi(g_2 K)$.
The value of $\Phi(gK)$ is completely independent of the representative $g$.

#### Step 2: Homomorphism Property
For any cosets $aK, bK \in G/K$:
$$\Phi((aK)(bK)) = \Phi((ab)K) = \phi(ab)$$
Since $\phi$ is a homomorphism:
$$\phi(ab) = \phi(a) \phi(b) = \Phi(aK) \Phi(bK)$$
Thus $\Phi$ preserves the group operation.

#### Step 3: Injectivity
We examine the kernel of $\Phi$:
$$\ker(\Phi) = \{ gK \in G/K : \Phi(gK) = e_H \}$$
Now $\Phi(gK) = e_H \iff \phi(g) = e_H \iff g \in \ker(\phi) = K$.
By coset equality (Lemma 4.1), $g \in K \iff gK = K = e_{G/K}$.
Therefore:
$$\ker(\Phi) = \{ K \} = \{ e_{G/K} \}$$
By Theorem 5.1, $\ker(\Phi) = \{ e_{G/K} \}$ implies $\Phi$ is injective.

#### Step 4: Surjectivity
Let $y \in \text{im}(\phi)$. By definition of the image, there exists some $g \in G$ such that $\phi(g) = y$.
Then for the coset $gK \in G/K$, we have:
$$\Phi(gK) = \phi(g) = y$$
Thus every element of $\text{im}(\phi)$ is hit by $\Phi$. $\Phi$ is surjective.

**Conclusion:**
$\Phi$ is a bijective homomorphism, hence an isomorphism:
$$G/\ker(\phi) \cong \text{im}(\phi) \quad \blacksquare$$"""
            },
            {
                "secNumber": "5.3",
                "title": "The Second (Diamond) and Third Isomorphism Theorems",
                "content": r"""### 1. The Second Isomorphism Theorem (Diamond Isomorphism Theorem)

The Second Isomorphism Theorem describes the relationship between the intersection and product of a subgroup and a normal subgroup.

> **Theorem 5.3 (Second Isomorphism Theorem):**
> Let $G$ be a group, $H \le G$ a subgroup, and $N \trianglelefteq G$ a normal subgroup.
> Then:
> 1. $HN = \{ hn : h \in H, n \in N \} \le G$.
> 2. $N \trianglelefteq HN$.
> 3. $H \cap N \trianglelefteq H$.
> 4. The quotient groups are isomorphic:
>    $$\frac{HN}{N} \cong \frac{H}{H \cap N}$$

```
           HN
         /    \
        H      N
         \    /
         H \cap N
```

#### Complete Proof:
1. **$HN \le G$:** Let $h_1 n_1, h_2 n_2 \in HN$. Then:
   $$(h_1 n_1)(h_2 n_2)^{-1} = h_1 n_1 n_2^{-1} h_2^{-1} = h_1 (n_1 n_2^{-1}) h_2^{-1}$$
   Since $N \trianglelefteq G$, $h_2^{-1} N h_2 = N$, so there exists $n_3 \in N$ such that $(n_1 n_2^{-1}) h_2^{-1} = h_2^{-1} n_3$.
   Then:
   $$(h_1 n_1)(h_2 n_2)^{-1} = h_1 h_2^{-1} n_3 = (h_1 h_2^{-1}) n_3 \in HN$$
   By the one-step subgroup test, $HN \le G$.
2. **$N \trianglelefteq HN$:** For any $hn \in HN$ and $m \in N$:
   $$(hn) m (hn)^{-1} = h n m n^{-1} h^{-1} = h (n m n^{-1}) h^{-1}$$
   Since $N \trianglelefteq G$, $n m n^{-1} \in N$, and $h (n m n^{-1}) h^{-1} \in N$.
   Thus $N \trianglelefteq HN$.
3. **Application of First Isomorphism Theorem:**
   Define the map:
   $$\theta: H \to \frac{HN}{N}, \quad \theta(h) = hN$$
   - **Homomorphism:** $\theta(h_1 h_2) = (h_1 h_2) N = (h_1 N)(h_2 N) = \theta(h_1) \theta(h_2)$.
   - **Surjectivity:** Any element of $HN/N$ is a coset of the form $(hn)N = h(nN) = hN$ (since $n \in N \implies nN = N$).
     Thus $\theta(h) = hN = (hn)N$, so $\theta$ is surjective!
   - **Kernel:**
     $$\ker(\theta) = \{ h \in H : \theta(h) = N \} = \{ h \in H : hN = N \} = \{ h \in H : h \in N \} = H \cap N$$
   By Theorem 5.1, the kernel of any homomorphism is normal in the domain, so $H \cap N \trianglelefteq H$.
   Applying the First Isomorphism Theorem (Theorem 5.2) to $\theta$:
   $$\frac{H}{\ker(\theta)} \cong \text{im}(\theta) \implies \frac{H}{H \cap N} \cong \frac{HN}{N} \quad \blacksquare$$

---

### 2. The Third Isomorphism Theorem

> **Theorem 5.4 (Third Isomorphism Theorem):**
> Let $G$ be a group, and let $N$ and $K$ be normal subgroups of $G$ such that $N \le K \trianglelefteq G$.
> Then:
> 1. $K/N \trianglelefteq G/N$.
> 2. The quotient of quotients satisfies:
>    $$\frac{G/N}{K/N} \cong \frac{G}{K}$$

#### Complete Proof:
Define the map $\psi: G/N \to G/K$ by:
$$\psi(gN) = gK, \quad \forall g \in G$$
- **Well-definedness:** If $g_1 N = g_2 N$, then $g_1^{-1} g_2 \in N$. Since $N \subseteq K$, $g_1^{-1} g_2 \in K$, which implies $g_1 K = g_2 K$.
- **Homomorphism:** $\psi((aN)(bN)) = \psi((ab)N) = (ab)K = (aK)(bK) = \psi(aN) \psi(bN)$.
- **Surjectivity:** For any coset $gK \in G/K$, $\psi(gN) = gK$.
- **Kernel:**
  $$\ker(\psi) = \{ gN \in G/N : \psi(gN) = K \} = \{ gN \in G/N : gK = K \} = \{ gN \in G/N : g \in K \} = K/N$$
Applying the First Isomorphism Theorem to $\psi$:
$$\frac{G/N}{\ker(\psi)} \cong \text{im}(\psi) \implies \frac{G/N}{K/N} \cong \frac{G}{K} \quad \blacksquare$$"""
            },
            {
                "secNumber": "5.4",
                "title": "Cayley's Representation Theorem",
                "content": r"""### 1. The Concrete Universality of Symmetric Groups

Can every abstract group—no matter how exotic—be viewed as a group of permutations of some set?
Arthur Cayley answered this affirmatively in 1854.

> **Theorem 5.5 (Cayley's Theorem):**
> Every group $G$ is isomorphic to a subgroup of the symmetric group $\text{Sym}(G)$.
> In particular, if $G$ is a finite group of order $n$, then $G$ is isomorphic to a subgroup of $S_n$.

---

### 2. Complete Constructive Proof

For each element $g \in G$, define the **left-multiplication map**:
$$L_g: G \to G, \quad L_g(x) = gx, \quad \forall x \in G$$

#### Step 1: $L_g$ is a Permutation of $G$
We show $L_g \in \text{Sym}(G)$ by showing it is bijective:
- **Injective:** If $L_g(x) = L_g(y)$, then $gx = gy$. Multiplying by $g^{-1}$ on the left gives $x = y$.
- **Surjective:** For any $y \in G$, $L_g(g^{-1}y) = g(g^{-1}y) = y$.
Thus $L_g: G \to G$ is a bijection, meaning $L_g \in \text{Sym}(G)$.

#### Step 2: The Left Regular Representation
Now define the mapping:
$$\phi: G \to \text{Sym}(G), \quad \phi(g) = L_g$$
We prove that $\phi$ is a group homomorphism:
For any $a, b \in G$ and any $x \in G$:
$$[L_a \circ L_b](x) = L_a(L_b(x)) = L_a(bx) = a(bx) = (ab)x = L_{ab}(x)$$
Since this holds for all $x \in G$:
$$L_a \circ L_b = L_{ab} \implies \phi(a) \circ \phi(b) = \phi(ab)$$
Therefore, $\phi$ is a homomorphism.

#### Step 3: $\phi$ is Injective
We examine the kernel of $\phi$:
$$\ker(\phi) = \{ g \in G : \phi(g) = \text{id}_G \} = \{ g \in G : L_g = \text{id}_G \}$$
If $L_g = \text{id}_G$, then $L_g(x) = x$ for all $x \in G$.
Evaluating at $x = e$:
$$L_g(e) = e \implies ge = e \implies g = e$$
Thus $\ker(\phi) = \{e\}$.
By Theorem 5.1, $\phi$ is injective.

#### Step 4: Applying First Isomorphism Theorem
By the First Isomorphism Theorem (Theorem 5.2):
$$G \cong G / \{e\} = G / \ker(\phi) \cong \text{im}(\phi) \le \text{Sym}(G)$$
Therefore, $G$ is isomorphic to the subgroup $\text{im}(\phi) = \{ L_g : g \in G \} \le \text{Sym}(G)$. $\blacksquare$"""
            },
            {
                "secNumber": "5.5",
                "title": "Automorphisms, Inner Automorphisms & Characteristic Subgroups",
                "content": r"""### 1. The Automorphism Group $\text{Aut}(G)$

An **automorphism** of $G$ is an isomorphism $\alpha: G \to G$.

> **Theorem 5.6 (The Group $\text{Aut}(G)$):**
> Under functional composition $\circ$, the set of all automorphisms of $G$, denoted $\text{Aut}(G)$, forms a group.

- Identity: $\text{id}_G(x) = x$.
- Inverse: The functional inverse $\alpha^{-1}$ of an isomorphism is an isomorphism.
- Associativity: Inherited from composition of functions.

---

### 2. Inner Automorphisms $\text{Inn}(G)$

For any fixed element $g \in G$, define the **conjugation map** by $g$:
$$\gamma_g: G \to G, \quad \gamma_g(x) = g x g^{-1}, \quad \forall x \in G$$

> **Lemma 5.2:**
> $\gamma_g$ is an automorphism of $G$, called the **inner automorphism** induced by $g$.

#### Proof:
- **Homomorphism:** $\gamma_g(xy) = g(xy)g^{-1} = (gxg^{-1})(gyg^{-1}) = \gamma_g(x) \gamma_g(y)$.
- **Bijective:** $\gamma_g \circ \gamma_{g^{-1}} = \gamma_{g^{-1}} \circ \gamma_g = \text{id}_G$. Thus $\gamma_g \in \text{Aut}(G)$. $\blacksquare$

The set of all inner automorphisms is denoted $\text{Inn}(G) = \{ \gamma_g : g \in G \}$.

> **Theorem 5.7 ($\text{Inn}(G) \cong G / Z(G)$):**
> 1. $\text{Inn}(G)$ is a normal subgroup of $\text{Aut}(G)$ ($\text{Inn}(G) \trianglelefteq \text{Aut}(G)$).
> 2. $\text{Inn}(G) \cong G / Z(G)$, where $Z(G)$ is the center of $G$.

#### Complete Proof:
Define the map $\Gamma: G \to \text{Aut}(G)$ by $\Gamma(g) = \gamma_g$.
1. **Homomorphism:** For any $a, b \in G$ and $x \in G$:
   $$\gamma_{ab}(x) = (ab)x(ab)^{-1} = a(bxb^{-1})a^{-1} = \gamma_a(\gamma_b(x)) = (\gamma_a \circ \gamma_b)(x)$$
   Thus $\Gamma(ab) = \Gamma(a) \circ \Gamma(b)$.
2. **Kernel of $\Gamma$:**
   $$\begin{aligned}
   \ker(\Gamma) &= \{ g \in G : \Gamma(g) = \text{id}_G \} = \{ g \in G : \gamma_g(x) = x, \; \forall x \in G \} \\
   &= \{ g \in G : gxg^{-1} = x, \; \forall x \in G \} = \{ g \in G : gx = xg, \; \forall x \in G \} \\
   &= Z(G)
   \end{aligned}$$
3. **Application of First Isomorphism Theorem:**
   The image of $\Gamma$ is by definition $\text{Inn}(G)$.
   By Theorem 5.2:
   $$G / \ker(\Gamma) \cong \text{im}(\Gamma) \implies G / Z(G) \cong \text{Inn}(G) \quad \blacksquare$$

---

### 3. Outer Automorphisms & Characteristic Subgroups

> **Definition 5.3 (Outer Automorphism Group):**
> The quotient group:
> $$\text{Out}(G) = \frac{\text{Aut}(G)}{\text{Inn}(G)}$$
> is called the **outer automorphism group** of $G$. Elements of $\text{Out}(G)$ are cosets of $\text{Inn}(G)$ called outer automorphism classes.

> **Definition 5.4 (Characteristic Subgroup):**
> A subgroup $H \le G$ is called **characteristic** in $G$ (denoted $H \text{ char } G$) if for every $\alpha \in \text{Aut}(G)$:
> $$\alpha(H) = H$$

**Key Distinctions:**
- Normal: Invariant under inner automorphisms ($\gamma_g(N) = N$ for all $g \in G$).
- Characteristic: Invariant under **all** automorphisms.
- Every characteristic subgroup is normal ($H \text{ char } G \implies H \trianglelefteq G$).
- Transitivity: While normality is NOT transitive in general ($K \trianglelefteq H \trianglelefteq G \not\implies K \trianglelefteq G$), characteristic subgroups ARE transitive:
  $$K \text{ char } H \quad \text{and} \quad H \trianglelefteq G \implies K \trianglelefteq G \quad \blacksquare$$"""
            }
        ],
        "problems": [
            {
                "tier": "Foundational",
                "title": "The Determinant Homomorphism and the Structure of $GL_n(\\mathbb{R}) / SL_n(\\mathbb{R})$",
                "statement": r"1. Let $GL_n(\mathbb{R})$ be the general linear group of invertible $n \times n$ real matrices under matrix multiplication, and let $\mathbb{R}^* = \mathbb{R} \setminus \{0\}$ be the multiplicative group of non-zero real numbers. Prove that the determinant mapping $\det: GL_n(\mathbb{R}) \to \mathbb{R}^*$ is an epimorphism (surjective homomorphism). 2. Determine its kernel $\ker(\det)$ and use the First Isomorphism Theorem to deduce the quotient group $GL_n(\mathbb{R}) / SL_n(\mathbb{R})$. 3. Determine the center $Z(GL_n(\mathbb{R}))$.",
                "hints": [
                    "Recall that $\\det(AB) = \\det(A)\\det(B)$ for any square matrices.",
                    "To prove surjectivity, construct an explicit diagonal matrix $D = \\text{diag}(c, 1, \\dots, 1)$ for any $c \\in \\mathbb{R}^*$.",
                    "A matrix in $Z(GL_n(\\mathbb{R}))$ must commute with all elementary matrices $E_{ij}$."
                ],
                "solution": r"""**Step 1: Homomorphism and Surjectivity of $\det$**

Let $A, B \in GL_n(\mathbb{R})$.
By the multiplicative property of determinants:
$$\det(A B) = \det(A) \cdot \det(B)$$
Since $A, B$ are invertible, $\det(A) \ne 0$ and $\det(B) \ne 0$, so $\det(A), \det(B) \in \mathbb{R}^*$.
Thus $\det: GL_n(\mathbb{R}) \to \mathbb{R}^*$ is a group homomorphism.

To show surjectivity, let $c \in \mathbb{R}^*$ be any non-zero real scalar.
Consider the diagonal matrix:
$$D_c = \begin{pmatrix} c & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{pmatrix} \in M_n(\mathbb{R})$$
Its determinant is $\det(D_c) = c \cdot 1 \cdots 1 = c \ne 0$.
Thus $D_c \in GL_n(\mathbb{R})$ and $\det(D_c) = c$.
Hence $\det$ is surjective (an epimorphism).

---

**Step 2: Kernel and Application of First Isomorphism Theorem**

The kernel of $\det$ is:
$$\ker(\det) = \{ A \in GL_n(\mathbb{R}) : \det(A) = 1_{\mathbb{R}^*} = 1 \}$$
By definition, the set of all $n \times n$ real matrices with determinant $1$ is the **special linear group**:
$$\ker(\det) = SL_n(\mathbb{R})$$
By Theorem 5.1, $SL_n(\mathbb{R}) \trianglelefteq GL_n(\mathbb{R})$.
Applying the First Isomorphism Theorem (Theorem 5.2):
$$\frac{GL_n(\mathbb{R})}{\ker(\det)} \cong \text{im}(\det) \implies \frac{GL_n(\mathbb{R})}{SL_n(\mathbb{R})} \cong \mathbb{R}^* \quad \blacksquare$$

---

**Step 3: Center of $GL_n(\mathbb{R})$**

An element $A \in GL_n(\mathbb{R})$ is in $Z(GL_n(\mathbb{R}))$ if and only if $A M = M A$ for all $M \in GL_n(\mathbb{R})$.
Let $E_{ij}$ denote the matrix with $1$ in entry $(i, j)$ and $0$ elsewhere.
For $i \ne j$, the elementary shear matrix $I + E_{ij} \in GL_n(\mathbb{R})$.
The condition $A(I + E_{ij}) = (I + E_{ij})A$ simplifies to:
$$A E_{ij} = E_{ij} A$$
Computing both sides:
- The $k$-th row of $A E_{ij}$ has entry $(k, j)$ equal to $A_{ki}$, and 0 elsewhere.
- The $k$-th row of $E_{ij} A$ has entry $(i, l)$ equal to $A_{jl}$ when $k=i$, and 0 for $k \ne i$.
Setting $k \ne i$ forces $A_{ki} = 0$ for all $k \ne i$, so $A$ must be diagonal.
Setting $k = i$ and $l = j$ forces $A_{ii} = A_{jj}$ for all $i, j$.
Thus all diagonal entries of $A$ are equal: $A_{11} = A_{22} = \dots = A_{nn} = \lambda \ne 0$.
Therefore, the center consists solely of non-zero scalar multiples of the identity:
$$Z(GL_n(\mathbb{R})) = \{ \lambda I_n : \lambda \in \mathbb{R}^* \} \cong \mathbb{R}^* \quad \blacksquare$$"""
            },
            {
                "tier": "Advanced",
                "title": "Automorphism Groups of Cyclic Groups and the Klein Four-Group",
                "statement": r"1. Prove that for any positive integer $n$, the automorphism group of the cyclic group $\mathbb{Z}_n$ is isomorphic to the group of units $U(n) = (\mathbb{Z}_n)^\times$: $\text{Aut}(\mathbb{Z}_n) \cong U(n)$. 2. Let $V_4 = \mathbb{Z}_2 \times \mathbb{Z}_2$ be the Klein four-group. Prove that $\text{Aut}(V_4) \cong S_3 \cong GL_2(\mathbb{F}_2)$.",
                "hints": [
                    "For Part 1, an automorphism of a cyclic group $\\langle 1 \\rangle$ is completely determined by the image of the generator $1$. What must $\\phi(1)$ be for $\\phi$ to be an automorphism?",
                    "For Part 2, view $\\mathbb{Z}_2 \\times \\mathbb{Z}_2$ as a 2-dimensional vector space over the finite field $\\mathbb{F}_2$."
                ],
                "solution": r"""**Part 1: $\text{Aut}(\mathbb{Z}_n) \cong U(n)$**

Let $G = \mathbb{Z}_n = \langle 1 \rangle$ under addition modulo $n$.
Any endomorphism $\alpha: \mathbb{Z}_n \to \mathbb{Z}_n$ is completely determined by $\alpha(1)$:
$$\alpha(k) = \alpha(\underbrace{1 + \dots + 1}_{k \text{ times}}) = k \cdot \alpha(1)$$
Let $a = \alpha(1) \in \mathbb{Z}_n$.
For $\alpha$ to be an automorphism, it must be surjective (and since $\mathbb{Z}_n$ is finite, this is equivalent to being bijective).
A linear map $k \mapsto ka$ is surjective on $\mathbb{Z}_n$ if and only if $a$ generates $\mathbb{Z}_n$.
By Theorem 2.4, $\langle a \rangle = \mathbb{Z}_n$ if and only if $\gcd(a, n) = 1$.
Thus each $a \in U(n) = (\mathbb{Z}_n)^\times$ defines a unique automorphism $\alpha_a(k) = ka \pmod n$.

Define the map $\Psi: \text{Aut}(\mathbb{Z}_n) \to U(n)$ by:
$$\Psi(\alpha) = \alpha(1) \pmod n$$
- **Bijective:** As shown above, every $a \in U(n)$ yields a unique automorphism $\alpha_a$, and $\Psi(\alpha_a) = a$.
- **Homomorphism:** For $\alpha_a, \alpha_b \in \text{Aut}(\mathbb{Z}_n)$:
  $$\Psi(\alpha_a \circ \alpha_b) = (\alpha_a \circ \alpha_b)(1) = \alpha_a(\alpha_b(1)) = \alpha_a(b) = b \cdot a \equiv a b \pmod n$$
  Thus $\Psi(\alpha_a \circ \alpha_b) = \Psi(\alpha_a) \cdot \Psi(\alpha_b)$.
Therefore, $\Psi$ is an isomorphism:
$$\text{Aut}(\mathbb{Z}_n) \cong U(n) \quad \blacksquare$$

---

**Part 2: $\text{Aut}(V_4) \cong S_3 \cong GL_2(\mathbb{F}_2)$**

Let $V_4 = \{ (0,0), (1,0), (0,1), (1,1) \}$ under component-wise addition modulo 2.
Every non-zero element has order 2:
$$e = (0,0), \quad a = (1,0), \quad b = (0,1), \quad c = (1,1)$$
Notice that $a + b = c, \; b + c = a, \; a + c = b$.

**Method 1 (Permutation of non-identity elements):**
Any automorphism $\sigma \in \text{Aut}(V_4)$ must fix $e = (0,0)$: $\sigma(e) = e$.
Therefore, $\sigma$ must permute the 3 non-identity elements $X = \{a, b, c\}$.
This defines a homomorphism:
$$\rho: \text{Aut}(V_4) \to \text{Sym}(X) \cong S_3, \quad \rho(\sigma) = \sigma|_X$$
- **Injectivity of $\rho$:** If $\rho(\sigma) = \text{id}_X$, then $\sigma$ fixes $a, b, c$ and fixes $e$, so $\sigma = \text{id}_{V_4}$.
  Thus $\ker(\rho) = \{\text{id}_{V_4}\}$, meaning $\rho$ is injective.
- **Surjectivity of $\rho$:** Any permutation of $\{a, b, c\}$ preserves the group operation!
  For instance, consider the transposition $(a \; b)$:
  $\sigma(a) = b$, $\sigma(b) = a$, and $\sigma(c) = \sigma(a+b) = \sigma(a) + \sigma(b) = b + a = c$.
  This is a valid automorphism!
  Similarly, the 3-cycle $(a \; b \; c)$ gives $\sigma(a)=b, \sigma(b)=c, \sigma(c)=a$, with $\sigma(a+b) = b+c = a = \sigma(c)$.
  Since the transpositions generate $S_3$, every permutation in $S_3$ is realized by an automorphism of $V_4$.
Thus $|\text{Aut}(V_4)| = |S_3| = 6$, and:
$$\text{Aut}(V_4) \cong S_3$$

**Method 2 (Vector Space Approach):**
$V_4$ is canonically isomorphic to the 2-dimensional vector space $\mathbb{F}_2^2$ over the field with 2 elements $\mathbb{F}_2 = \{0, 1\}$.
Since addition of vectors is the group operation, and scalar multiplication by $0$ and $1$ is trivial, any group automorphism of $V_4$ is automatically $\mathbb{F}_2$-linear!
Thus:
$$\text{Aut}(V_4) \cong GL_2(\mathbb{F}_2)$$
The order of $GL_2(\mathbb{F}_2)$ is:
$$|GL_2(\mathbb{F}_2)| = (2^2 - 1)(2^2 - 2) = (3)(2) = 6$$
The only non-abelian group of order 6 is $S_3$.
Therefore:
$$\text{Aut}(V_4) \cong S_3 \cong GL_2(\mathbb{F}_2) \quad \blacksquare$$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Complete Classification of Groups of Order $2p$ ($p$ Odd Prime)",
                "statement": r"Let $p$ be an odd prime number ($p \ge 3$), and let $G$ be a group of order $2p$. 1. Prove that $G$ contains a normal subgroup $N$ of order $p$, and that $N$ is cyclic. 2. Prove that $G$ contains an element $s$ of order 2. 3. By studying the conjugation action of $s$ on $N$ via $\text{Aut}(N)$, prove that $G$ is isomorphic to either the cyclic group $\mathbb{Z}_{2p}$ or the dihedral group $D_{2p}$.",
                "hints": [
                    "By Cauchy's Theorem, $G$ contains elements of orders $p$ and 2. Alternatively, use Lagrange and cosets.",
                    "Since $[G : N] = 2$, $N$ must be normal (Proposition 4.1).",
                    "The conjugation map $\\gamma_s: N \\to N$ defined by $\\gamma_s(r) = s r s^{-1}$ must be an automorphism of $N$ whose square is the identity, since $s^2 = e$."
                ],
                "solution": r"""**Step 1: Existence and Normality of Cyclic Subgroup of Order $p$**

We first show that $G$ contains an element of order $p$.
By Corollary 4.2.1, the possible orders of elements in $G$ are divisors of $2p$: $\{1, 2, p, 2p\}$.
If $G$ contains an element of order $2p$, then $G \cong \mathbb{Z}_{2p}$ is cyclic, and $N = \langle g^2 \rangle$ has order $p$.
Suppose $G$ does not contain an element of order $2p$.
Can all non-identity elements have order 2?
If every $g \ne e$ has order 2, then for all $x, y \in G$:
$$x y = (x y)^{-1} = y^{-1} x^{-1} = y x$$
So $G$ would be abelian. In an abelian group where every non-identity element has order 2, $G \cong (\mathbb{Z}_2)^k$, so $|G| = 2^k$.
However, $|G| = 2p$ where $p \ge 3$ is odd, which is never a power of 2!
Hence $G$ **must** contain an element $r$ of order $p$.

Let $N = \langle r \rangle = \{1, r, r^2, \dots, r^{p-1}\}$.
Since $|r| = p$, $|N| = p$, and $N$ is cyclic: $N \cong \mathbb{Z}_p$.
The index of $N$ in $G$ is:
$$[G : N] = \frac{|G|}{|N|} = \frac{2p}{p} = 2$$
By Proposition 4.1, any subgroup of index 2 is normal:
$$N \trianglelefteq G$$

---

**Step 2: Existence of an Element of Order 2**

Since $|N| = p$ and $|G| = 2p$, there are $p$ elements in the complement $G \setminus N$.
Let $x \in G \setminus N$.
Since $N \trianglelefteq G$, the quotient group $G/N$ has order 2, so:
$$(xN)^2 = x^2 N = N \implies x^2 \in N$$
Thus $x^2 = r^k$ for some $k \in \{0, 1, \dots, p-1\}$.
The order of $x$ must divide $2p$, so $|x| \in \{2, p, 2p\}$.
- If $|x| = 2$, we are done: set $s = x$.
- If $|x| = p$, then $\langle x \rangle$ is a subgroup of order $p$ distinct from $N$ (since $x \notin N$).
  Then $N \cap \langle x \rangle = \{e\}$, so $|N \langle x \rangle| = \frac{p \cdot p}{1} = p^2 > 2p$, a contradiction! (Since $p \ge 3$).
  Thus no element outside $N$ can have order $p$.
- If $|x| = 2p$, then $x^p$ has order 2: set $s = x^p \in G \setminus N$.
Therefore, there always exists an element $s \in G$ with $|s| = 2$.
Note that since $s$ has order 2 and $|N| = p$ is odd, $s \notin N$.

---

**Step 3: Action by Conjugation and Final Classification**

Since $N \trianglelefteq G$ and $s \in G$, conjugation by $s$ is an automorphism of $N$:
$$\gamma_s: N \to N, \quad \gamma_s(r) = s r s^{-1} = s r s \quad (\text{since } s = s^{-1})$$
Since $N = \langle r \rangle$, $s r s \in N$, so:
$$s r s = r^k \quad \text{for some } k \in \{1, 2, \dots, p-1\}$$
Now compute $s^2 r s^{-2}$:
$$r = s^2 r s^{-2} = s (s r s) s = s r^k s = (s r s)^k = (r^k)^k = r^{k^2}$$
Therefore:
$$r^{k^2 - 1} = e \implies k^2 \equiv 1 \pmod p$$
Since $p$ is prime, the congruence $k^2 \equiv 1 \pmod p$ factors as:
$$(k - 1)(k + 1) \equiv 0 \pmod p \implies p \mid (k-1) \quad \text{or} \quad p \mid (k+1)$$
This yields exactly two solutions modulo $p$:
$$k \equiv 1 \pmod p \quad \text{or} \quad k \equiv -1 \equiv p-1 \pmod p$$

#### Case 1: $k \equiv 1 \pmod p$
Then $s r s = r \implies s r = r s$.
Here $s$ and $r$ commute!
Since $|r| = p$ and $|s| = 2$ with $\gcd(p, 2) = 1$, the element $g = rs$ has order:
$$|g| = |rs| = \text{lcm}(|r|, |s|) = \text{lcm}(p, 2) = 2p$$
Therefore, $G = \langle rs \rangle$ is cyclic:
$$G \cong \mathbb{Z}_{2p}$$

#### Case 2: $k \equiv -1 \pmod p$
Then $s r s = r^{-1} \implies s r s = r^{-1}$.
Together with $r^p = 1$ and $s^2 = 1$, the group presentation of $G$ is:
$$G = \langle r, s \mid r^p = 1, \; s^2 = 1, \; s r s = r^{-1} \rangle$$
This is precisely the presentation of the **dihedral group** of order $2p$:
$$G \cong D_{2p}$$

**Conclusion:**
Every group of order $2p$ ($p$ odd prime) is isomorphic to either $\mathbb{Z}_{2p}$ or $D_{2p}$. $\blacksquare$"""
            }
        ]
    }
    return u5

if __name__ == "__main__":
    u = get_unit5()
    print("Unit 5 generated successfully:", u["title"])
    print("Sections:", len(u["sections"]))
    print("Problems:", len(u["problems"]))
