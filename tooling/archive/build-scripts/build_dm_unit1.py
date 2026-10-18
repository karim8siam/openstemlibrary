# -*- coding: utf-8 -*-
"""
build_dm_unit1.py
Constructs Unit 1: Propositional & Predicate Logic, Inference & Formal Proof Techniques
Strictly ZERO course numbers.
"""

def get_unit1():
    u1 = {
        "number": 1,
        "title": "Propositional & Predicate Logic, Inference & Formal Proof Techniques",
        "leadSummary": "Foundations of formal mathematical logic: truth tables, logical connectives, conjunctive and disjunctive normal forms, predicate calculus with nested quantifiers, classical rules of inference, detection of deductive fallacies, and rigorous proof methods including direct, contrapositive, contradiction, case exhaustion, and non-constructive existence proofs.",
        "simulations": ["sim_dm_logic_truth_tables"],
        "sections": [
            {
                "secNumber": "1.1",
                "title": "Propositional Logic, Truth Tables, Logical Equivalences & Normal Forms",
                "content": r"""### 1. Propositions and Logical Connectives

A **proposition** is a declarative statement that is either strictly **true** ($T$ or $1$) or strictly **false** ($F$ or $0$), but not both simultaneously. Propositional variables (typically denoted $p, q, r, s$) represent atomic propositions that cannot be decomposed into simpler assertions.

Compound propositions are synthesized from atomic variables using formal truth-functional operators:

| Operator Name | Notation | Meaning / Truth Condition |
| :--- | :---: | :--- |
| **Negation** | $\neg p$ or $\sim p$ | True precisely when $p$ is false. |
| **Conjunction** | $p \land q$ | True if and only if both $p$ and $q$ are true. |
| **Disjunction** | $p \lor q$ | True if at least one of $p$ or $q$ is true (inclusive OR). |
| **Exclusive OR** | $p \oplus q$ | True if exactly one of $p, q$ is true; $p \oplus q \equiv (p \lor q) \land \neg(p \land q)$. |
| **Conditional (Implication)** | $p \implies q$ | False only when $p$ is true and $q$ is false; otherwise true. |
| **Biconditional** | $p \iff q$ | True if $p$ and $q$ possess identical truth values; $(p \implies q) \land (q \implies p)$. |

> **Crucial Insight on Material Implication:**
> In classical formal logic, the conditional $p \implies q$ is truth-functional: if the antecedent $p$ is false, the compound proposition $p \implies q$ is **vacuously true**, regardless of the truth value of the consequent $q$. Thus, $p \implies q \equiv \neg p \lor q$.

---

### 2. Tautologies, Contradictions, and Logical Equivalence

- A compound proposition that is true for all possible assignments of truth values to its propositional variables is a **tautology** (denoted $\mathbf{T}$).
- A compound proposition that is false under every truth assignment is a **contradiction** (denoted $\mathbf{F}$).
- A compound proposition that is neither a tautology nor a contradiction is a **contingency**.

> **Definition 1.1 (Logical Equivalence):**
> Two compound propositions $P$ and $Q$ are **logically equivalent** (written $P \equiv Q$ or $P \iff Q$ is a tautology) if they evaluate to identical truth values across all $2^n$ interpretations in their truth table.

#### Essential System of Logical Equivalences

1. **Identity Laws:** $p \land \mathbf{T} \equiv p$, $p \lor \mathbf{F} \equiv p$.
2. **Domination Laws:** $p \lor \mathbf{T} \equiv \mathbf{T}$, $p \land \mathbf{F} \equiv \mathbf{F}$.
3. **Idempotent Laws:** $p \lor p \equiv p$, $p \land p \equiv p$.
4. **Double Negation:** $\neg(\neg p) \equiv p$.
5. **Commutative Laws:** $p \lor q \equiv q \lor p$, $p \land q \equiv q \land p$.
6. **Associative Laws:** $(p \lor q) \lor r \equiv p \lor (q \lor r)$, $(p \land q) \land r \equiv p \land (q \land r)$.
7. **Distributive Laws:**
   $$p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$$
   $$p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$$
8. **De Morgan's Laws:**
   $$\neg(p \land q) \equiv \neg p \lor \neg q$$
   $$\neg(p \lor q) \equiv \neg p \land \neg q$$
9. **Absorption Laws:** $p \lor (p \land q) \equiv p$, $p \land (p \lor q) \equiv p$.
10. **Negation Laws (Excluded Middle and Contradiction):** $p \lor \neg p \equiv \mathbf{T}$, $p \land \neg p \equiv \mathbf{F}$.
11. **Contrapositive Law:** $p \implies q \equiv \neg q \implies \neg p$.

---

### 3. Normal Forms and Functional Completeness

A **literal** is a propositional variable $x$ or its formal negation $\neg x$.

#### Disjunctive Normal Form (DNF)
A proposition is in **Disjunctive Normal Form (DNF)** if it is expressed as a disjunction of minterms (conjunctions of literals):
$$\bigvee_{i=1}^m \left( \bigwedge_{j=1}^{k_i} L_{i,j} \right)$$
Every truth table row that evaluates to $1$ generates exactly one minterm.

#### Conjunctive Normal Form (CNF)
A proposition is in **Conjunctive Normal Form (CNF)** if it is expressed as a conjunction of maxterms (clauses, which are disjunctions of literals):
$$\bigwedge_{i=1}^m \left( \bigvee_{j=1}^{k_i} L_{i,j} \right)$$
Every truth table row that evaluates to $0$ generates a clause consisting of the negations of the literal assignments.

> **Theorem 1.1 (Functional Completeness):**
> A set of logical connectives is **functionally complete** if every possible truth function of $n$ variables can be expressed using only operators from that set.
> - The standard set $\{\neg, \land, \lor\}$ is functionally complete.
> - By De Morgan's laws, $\{\neg, \land\}$ and $\{\neg, \lor\}$ are functionally complete.
> - The singleton sets consisting of either **NAND** (Sheffer stroke $\uparrow$) or **NOR** (Peirce arrow $\downarrow$) are individually functionally complete:
>   $$p \uparrow q \equiv \neg(p \land q), \qquad p \downarrow q \equiv \neg(p \lor q)$$"""
            },
            {
                "secNumber": "1.2",
                "title": "Predicate Logic, Quantifiers, Nested Quantification & Negation Duality",
                "content": r"""### 1. Predicates and the Universe of Discourse

A **predicate** $P(x)$ is a statement containing one or more free variables $x$ that becomes a proposition with a definite truth value whenever specific constants from a specified domain (the **universe of discourse** $\mathcal{U}$) are assigned to those variables. The set of all $x \in \mathcal{U}$ such that $P(x)$ is true is known as the **truth set** (or extension) of $P(x)$.

---

### 2. The Universal and Existential Quantifiers

Quantification converts open predicate formulas into definitive mathematical propositions over a non-empty domain $\mathcal{U}$:

1. **Universal Quantifier ($\forall$):**
   $$\forall x \, P(x)$$
   Asserts that $P(x)$ is true for every element $x \in \mathcal{U}$. If $\mathcal{U} = \{x_1, x_2, \dots, x_n\}$ is finite:
   $$\forall x \, P(x) \equiv P(x_1) \land P(x_2) \land \dots \land P(x_n)$$
   A single element $c \in \mathcal{U}$ for which $P(c)$ is false constitutes a **counterexample**, immediately refuting $\forall x \, P(x)$.

2. **Existential Quantifier ($\exists$):**
   $$\exists x \, P(x)$$
   Asserts that there exists at least one element $x \in \mathcal{U}$ such that $P(x)$ is true. Over a finite domain:
   $$\exists x \, P(x) \equiv P(x_1) \lor P(x_2) \lor \dots \lor P(x_n)$$

3. **Uniqueness Quantifier ($\exists!$):**
   The notation $\exists! x \, P(x)$ signifies that there exists one and only one element $x$ satisfying $P(x)$:
   $$\exists! x \, P(x) \equiv \exists x \left( P(x) \land \forall y (P(y) \implies y = x) \right)$$

---

### 3. De Morgan's Laws for Quantifiers (Duality)

> **Theorem 1.2 (Quantifier Negation Duality):**
> Let $P(x)$ be an arbitrary predicate over domain $\mathcal{U}$. Then:
> $$\neg \forall x \, P(x) \equiv \exists x \, \neg P(x)$$
> $$\neg \exists x \, P(x) \equiv \forall x \, \neg P(x)$$

*Proof:*
- $\neg \forall x \, P(x)$ is true $\iff$ It is not the case that $P(x)$ holds for all $x \in \mathcal{U}$ $\iff$ There exists at least one $x_0 \in \mathcal{U}$ such that $P(x_0)$ is false $\iff$ There exists $x_0 \in \mathcal{U}$ such that $\neg P(x_0)$ is true $\iff \exists x \, \neg P(x)$.
- Replacing $P(x)$ with $\neg P(x)$ and using double negation yields the second identity immediately. $\blacksquare$

---

### 4. Nested Quantifiers and Order Dependence

When multiple variables are bound, the order of distinct quantifiers is critical and generally non-commutative:

- $\forall x \forall y \, P(x, y) \equiv \forall y \forall x \, P(x, y)$ (Commutative for identical quantifiers).
- $\exists x \exists y \, P(x, y) \equiv \exists y \exists x \, P(x, y)$ (Commutative for identical quantifiers).
- **Non-Commutativity of Alternating Quantifiers:**
  $$\exists y \forall x \, P(x, y) \implies \forall x \exists y \, P(x, y)$$
  However, the converse **does not hold**!
  - $\exists y \forall x \, P(x, y)$: There exists a single universal element $y$ that works for every choice of $x$.
  - $\forall x \exists y \, P(x, y)$: For every choice of $x$, there exists a corresponding $y$ (which may depend entirely on $x$, i.e., $y = y(x)$).

> **Classic Mathematical Formulation (Cauchy Continuity):**
> A function $f: \mathbb{R} \to \mathbb{R}$ is continuous at $x_0$ if:
> $$\forall \epsilon > 0 \; \exists \delta > 0 \; \forall x \; \left( |x - x_0| < \delta \implies |f(x) - f(x_0)| < \epsilon \right)$$
> Uniform continuity on an interval $I$ swaps the quantifiers:
> $$\forall \epsilon > 0 \; \exists \delta > 0 \; \forall x_1 \in I \; \forall x_2 \in I \; \left( |x_1 - x_2| < \delta \implies |f(x_1) - f(x_2)| < \epsilon \right)$$
> In uniform continuity, $\delta$ depends solely on $\epsilon$, whereas in point-wise continuity $\delta$ depends on both $\epsilon$ and $x_0$."""
            },
            {
                "secNumber": "1.3",
                "title": "Rules of Inference, Valid Arguments & Logical Fallacies",
                "content": r"""### 1. Argument Forms and Validity

An **argument** in propositional logic is a sequence of propositions $p_1, p_2, \dots, p_k$ called **premises**, followed by a final proposition $q$ called the **conclusion**:
$$\frac{p_1, \, p_2, \, \dots, \, p_k}{\therefore q}$$
An argument form is **valid** if the conditional statement:
$$(p_1 \land p_2 \land \dots \land p_k) \implies q$$
is a **tautology**. Validity is a structural property: if all premises are true, the conclusion is guaranteed to be true. An argument is **sound** if it is valid and all its premises are factually true in reality.

---

### 2. Classical Rules of Inference

| Rule of Inference | Premise Structure | Conclusion | Tautological Basis |
| :--- | :--- | :---: | :--- |
| **Modus Ponens** (Affirming the Antecedent) | $p \implies q$, $p$ | $\therefore q$ | $[(p \implies q) \land p] \implies q$ |
| **Modus Tollens** (Denying the Consequent) | $p \implies q$, $\neg q$ | $\therefore \neg p$ | $[(p \implies q) \land \neg q] \implies \neg p$ |
| **Hypothetical Syllogism** (Transitivity) | $p \implies q$, $q \implies r$ | $\therefore p \implies r$ | $[(p \implies q) \land (q \implies r)] \implies (p \implies r)$ |
| **Disjunctive Syllogism** | $p \lor q$, $\neg p$ | $\therefore q$ | $[(p \lor q) \land \neg p] \implies q$ |
| **Addition** | $p$ | $\therefore p \lor q$ | $p \implies (p \lor q)$ |
| **Simplification** | $p \land q$ | $\therefore p$ | $(p \land q) \implies p$ |
| **Conjunction** | $p$, $q$ | $\therefore p \land q$ | $(p \land q) \implies (p \land q)$ |
| **Resolution** | $p \lor q$, $\neg p \lor r$ | $\therefore q \lor r$ | $[(p \lor q) \land (\neg p \lor r)] \implies (q \lor r)$ |

> **Remark on Resolution:**
> The resolution rule is the foundation of automated theorem proving and logic programming (e.g., Prolog). Two clauses containing complementary literals $p$ and $\neg p$ are resolved into a single resolvent clause $q \lor r$.

---

### 3. Rules of Inference for Quantified Statements

1. **Universal Instantiation (UI):** If $\forall x P(x)$ is true, then $P(c)$ is true for any arbitrary element $c \in \mathcal{U}$.
2. **Universal Generalization (UG):** If $P(c)$ is proved for an arbitrary, generic element $c \in \mathcal{U}$ (with no special assumptions on $c$), then $\forall x P(x)$ is true.
3. **Existential Instantiation (EI):** If $\exists x P(x)$ is true, then there exists an element $c \in \mathcal{U}$ such that $P(c)$ is true (introducing a fresh constant symbol $c$).
4. **Existential Generalization (EG):** If $P(c)$ is true for some specific witness $c \in \mathcal{U}$, then $\exists x P(x)$ is true.

---

### 4. Common Deductive Fallacies

Arguments that mimic valid rules of inference but fail to be tautologies are **fallacies**:

#### Fallacy of Affirming the Consequent
- Form: $p \implies q$, $q$, therefore $\therefore p$.
- Fallacy verification: If $p$ is false and $q$ is true, the premises $(p \implies q)$ and $q$ are both true, but the conclusion $p$ is false. The conditional $[(p \implies q) \land q] \implies p$ evaluates to false when $(p, q) = (0, 1)$, hence it is **not** a tautology.

#### Fallacy of Denying the Antecedent
- Form: $p \implies q$, $\neg p$, therefore $\therefore \neg q$.
- Fallacy verification: If $p$ is false and $q$ is true, then $p \implies q$ is true, $\neg p$ is true, yet $\neg q$ is false.

#### Fallacy of Circular Reasoning (Begging the Question)
- Occurs when one of the premises assumes the truth of the conclusion being demonstrated."""
            },
            {
                "secNumber": "1.4",
                "title": "Formal Proof Techniques: Direct, Contrapositive, Contradiction, Cases & Exhaustion",
                "content": r"""### 1. Mathematical Proof Taxonomy

A **proof** is a rigorous, deductive argument demonstrating that a mathematical proposition is necessarily true under a set of accepted axioms and previously proven theorems.

```
                    Mathematical Proof Techniques
                                   │
         ┌─────────────────────────┴─────────────────────────┐
         ▼                                                   ▼
 Direct Proofs                                       Indirect Proofs
 (P ⟹ Q via derivations)                                     │
                                       ┌─────────────────────┴─────────────────────┐
                                       ▼                                           ▼
                             Contrapositive Proof                        Proof by Contradiction
                             (¬Q ⟹ ¬P)                                   (Assume P ∧ ¬Q ⟹ False)
```

---

### 2. Direct Proof Method

To prove an implication $P \implies Q$:
1. Assume the premise $P$ is true.
2. Unpack the formal mathematical definitions inherent in $P$.
3. Apply logical deductive steps, algebraic manipulations, and established lemmas.
4. Arrive at the conclusion $Q$.

> **Theorem 1.3:** If $n$ is an odd integer, then $n^2$ is an odd integer.
> *Direct Proof:* Let $n$ be an odd integer. By definition of odd integers, there exists an integer $k \in \mathbb{Z}$ such that $n = 2k + 1$.
> Squaring both sides:
> $$n^2 = (2k + 1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$$
> Since the integers are closed under multiplication and addition, $m = 2k^2 + 2k$ is an integer. Thus $n^2 = 2m + 1$, which satisfies the definition of an odd integer. $\blacksquare$

---

### 3. Proof by Contraposition

To prove $P \implies Q$, we establish the logically equivalent contrapositive statement:
$$\neg Q \implies \neg P$$
This technique is particularly powerful when the negation $\neg Q$ provides more structured algebraic or algebraic-geometric information than $P$.

> **Theorem 1.4:** Let $n \in \mathbb{Z}$. If $3n + 2$ is odd, then $n$ is odd.
> *Proof by Contraposition:*
> - The statement has the form $P(n) \implies Q(n)$, where $P(n): 3n+2 \text{ is odd}$ and $Q(n): n \text{ is odd}$.
> - The contrapositive is $\neg Q(n) \implies \neg P(n)$, i.e., "If $n$ is even, then $3n + 2$ is even."
> - Assume $n$ is even. By definition, $n = 2k$ for some $k \in \mathbb{Z}$.
> - Substitute $n = 2k$ into the expression:
>   $$3n + 2 = 3(2k) + 2 = 6k + 2 = 2(3k + 1)$$
> - Since $k \in \mathbb{Z}$, $3k + 1$ is an integer. Therefore, $3n + 2$ is divisible by 2 and is even ($\neg P(n)$ holds).
> - Since $\neg Q \implies \neg P$ is proved, the original implication $P \implies Q$ is true. $\blacksquare$

---

### 4. Proof by Contradiction (Reductio ad Absurdum)

To prove a theorem $T$, we assume its formal negation $\neg T$ and deduce a logical contradiction of the form $R \land \neg R$ (or equivalently derive $\mathbf{F}$). Since mathematics is consistent, the assumption $\neg T$ must be false, so $T$ must be true.

> **Theorem 1.5 (Euclidean Irrationality of $\sqrt{2}$):** The number $\sqrt{2}$ is irrational.
> *Proof by Contradiction:*
> 1. Assume for contradiction that $\sqrt{2}$ is rational. Then there exist integers $a, b \in \mathbb{Z}$ with $b \ne 0$ such that $\sqrt{2} = \frac{a}{b}$.
> 2. Without loss of generality, assume the fraction is in irreducible lowest terms: $\gcd(a, b) = 1$.
> 3. Squaring both sides yields $2 = \frac{a^2}{b^2} \implies a^2 = 2b^2$.
> 4. Thus $a^2$ is even, which implies $a$ is even (by contrapositive: if $a$ were odd, $a^2$ would be odd).
> 5. Since $a$ is even, write $a = 2k$ for some $k \in \mathbb{Z}$.
> 6. Substitute $a = 2k$ into the equation: $(2k)^2 = 2b^2 \implies 4k^2 = 2b^2 \implies b^2 = 2k^2$.
> 7. Hence $b^2$ is even, which implies $b$ is even.
> 8. Both $a$ and $b$ are even, so $2 \mid a$ and $2 \mid b$, which implies $\gcd(a, b) \ge 2$.
> 9. This directly contradicts the assumption that $\gcd(a, b) = 1$.
> 10. Therefore, the initial assumption is false, and $\sqrt{2}$ is irrational. $\blacksquare$

---

### 5. Proof by Cases and Exhaustion

When proving a proposition $\forall x P(x)$, if the domain $\mathcal{U}$ can be partitioned into mutually exhaustive cases $C_1 \cup C_2 \cup \dots \cup C_k = \mathcal{U}$, we establish:
$$(C_1 \implies P) \land (C_2 \implies P) \land \dots \land (C_k \implies P)$$
Exhaustive proofs systematically test every finite case (e.g., verifying that no integer $x$ in $\{1, 2, 3, 4\}$ satisfies $x^3 + x = 20$)."""
            },
            {
                "secNumber": "1.5",
                "title": "Constructive vs Non-Constructive Proofs & Interactive Truth Table Engine",
                "content": r"""### 1. Constructive Existence Proofs

An **existence proof** for a statement $\exists x P(x)$ is called **constructive** if it explicitly produces a concrete witness $c \in \mathcal{U}$ and demonstrates directly that $P(c)$ holds, or provides an effective algorithm that computes such a witness in finite time.

> **Example 1.2 (Constructive Existence):**
> *Claim:* There exist two distinct perfect cubes whose sum is a perfect cube.
> *Witness:* Euler showed that no positive solution exists for $n=3$, but allowing negative integers:
> $$(-1)^3 + 1^3 = 0 = 0^3$$
> Or in the famous taxicab number problem, Ramanujan showed $1729 = 1^3 + 12^3 = 9^3 + 10^3$, constructively proving that a number expressible as the sum of two positive cubes in two distinct ways exists.

---

### 2. Non-Constructive Existence Proofs

A **non-constructive existence proof** proves that $\exists x P(x)$ must be true without providing any explicit witness or algorithm to construct it. This is typically achieved using the Law of the Excluded Middle ($P \lor \neg P$), the Mean Value Theorem, or Cantor's diagonal argument.

> **Theorem 1.6 (Irrational Powers Yielding a Rational Number):**
> There exist irrational numbers $a$ and $b$ such that $a^b$ is rational.
>
> *Non-Constructive Proof:*
> Consider the number $\sqrt{2}^{\sqrt{2}}$. We know $\sqrt{2}$ is irrational (Theorem 1.5).
> By the Law of the Excluded Middle, $\sqrt{2}^{\sqrt{2}}$ is either rational or irrational:
> - **Case 1:** If $\sqrt{2}^{\sqrt{2}}$ is rational, then choosing $a = \sqrt{2}$ and $b = \sqrt{2}$ provides the required pair, since both $a, b$ are irrational and $a^b$ is rational.
> - **Case 2:** If $\sqrt{2}^{\sqrt{2}}$ is irrational, then choose $a = \sqrt{2}^{\sqrt{2}}$ (which is irrational by the case hypothesis) and $b = \sqrt{2}$ (which is irrational). Then:
>   $$a^b = \left( \sqrt{2}^{\sqrt{2}} \right)^{\sqrt{2}} = \sqrt{2}^{\sqrt{2} \cdot \sqrt{2}} = \sqrt{2}^2 = 2$$
>   Since $2 = \frac{2}{1}$, it is rational!
> In either case, there exist irrational numbers $a$ and $b$ such that $a^b$ is rational. $\blacksquare$
>
> *Remark on Non-Constructivism:*
> Notice that the proof does not determine whether $\sqrt{2}^{\sqrt{2}}$ is actually rational or irrational (the Gelfond-Schneider theorem later proved that $\sqrt{2}^{\sqrt{2}}$ is indeed transcendental and irrational, vindicating Case 2, but the proof above succeeds independently of that knowledge).

---

### 3. Interactive Truth Table & Logic Circuit Engine

The simulation below provides an interactive workspace for Boolean logic and circuit synthesis:
- **Truth Table Generator:** Evaluate arbitrary compound formulas involving $\neg, \land, \lor, \implies, \iff, \oplus$ over multiple variables.
- **Circuit Gate Synthesizer:** Observe real-time logic signal propagation through AND, OR, NOT, NAND, NOR, and XOR gates.
- **Normal Form Decomposer:** Inspect step-by-step minterm extraction for DNF and maxterm clauses for CNF."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational Level",
                "title": "Problem 1.1: Canonical Normal Forms and Sheffer Stroke Synthesis",
                "statement": r"""Consider the compound propositional formula:
$$\phi(p, q, r) = (p \land \neg q) \lor (q \implies r)$$
1. Construct the complete truth table for $\phi(p, q, r)$ across all 8 possible truth assignments.
2. Write down the Canonical Disjunctive Normal Form (DNF) as a disjunction of minterms.
3. Write down the Canonical Conjunctive Normal Form (CNF) as a conjunction of maxterms.
4. Using only the NAND operator ($\uparrow$, Sheffer stroke), synthesize an equivalent formula for $\neg p \land q$.""",
                "hints": [
                    "Recall that $q \implies r \equiv \neg q \lor r$.",
                    "For DNF, identify all rows where $\phi = 1$. For CNF, identify all rows where $\phi = 0$ and negate the conditions.",
                    r"Recall that $\neg x \equiv x \uparrow x$ and $x \land y \equiv (x \uparrow y) \uparrow (x \uparrow y)$."
                ],
                "solution": r"""### 1. Truth Table Construction
First expand the sub-expressions:
$p \land \neg q$ is true only when $p = 1$ and $q = 0$.
$q \implies r \equiv \neg q \lor r$ is false only when $q = 1$ and $r = 0$.

| Row | $p$ | $q$ | $r$ | $\neg q$ | $p \land \neg q$ | $q \implies r$ | $\phi(p, q, r)$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 0 | 0 | 0 | 1 | 0 | 1 | **1** |
| 2 | 0 | 0 | 1 | 1 | 0 | 1 | **1** |
| 3 | 0 | 1 | 0 | 0 | 0 | 0 | **0** |
| 4 | 0 | 1 | 1 | 0 | 0 | 1 | **1** |
| 5 | 1 | 0 | 0 | 1 | 1 | 1 | **1** |
| 6 | 1 | 0 | 1 | 1 | 1 | 1 | **1** |
| 7 | 1 | 1 | 0 | 0 | 0 | 0 | **0** |
| 8 | 1 | 1 | 1 | 0 | 0 | 1 | **1** |

Notice that $\phi(p, q, r) = 0$ precisely on Rows 3 and 7:
- Row 3: $(p, q, r) = (0, 1, 0)$
- Row 7: $(p, q, r) = (1, 1, 0)$
On all other 6 rows, $\phi(p, q, r) = 1$.

---

### 2. Canonical Disjunctive Normal Form (DNF)
The DNF is the disjunction of the minterms corresponding to rows where $\phi = 1$ (Rows 1, 2, 4, 5, 6, 8):
$$\begin{aligned}
\text{DNF} = & (\neg p \land \neg q \land \neg r) \lor (\neg p \land \neg q \land r) \lor (\neg p \land q \land r) \\
& \lor (p \land \neg q \land \neg r) \lor (p \land \neg q \land r) \lor (p \land q \land r)
\end{aligned}$$

---

### 3. Canonical Conjunctive Normal Form (CNF)
The CNF is formed by the conjunction of maxterms for the rows where $\phi = 0$ (Rows 3 and 7):
- For Row 3: $(p=0, q=1, r=0)$, the maxterm is $(p \lor \neg q \lor r)$.
- For Row 7: $(p=1, q=1, r=0)$, the maxterm is $(\neg p \lor \neg q \lor r)$.

Therefore:
$$\text{CNF} = (p \lor \neg q \lor r) \land (\neg p \lor \neg q \lor r)$$
Notice that this simplifies algebraically to $(\neg q \lor r)$, which matches the truth table!

---

### 4. NAND Synthesis of $\neg p \land q$
Recall the Sheffer stroke definition: $x \uparrow y \equiv \neg(x \land y)$.
- Negation in NAND: $\neg x \equiv x \uparrow x$.
- Conjunction in NAND: $x \land y \equiv \neg(x \uparrow y) \equiv (x \uparrow y) \uparrow (x \uparrow y)$.

Let $A = \neg p = p \uparrow p$ and $B = q$.
Then:
$$\neg p \land q = A \land B = (A \uparrow B) \uparrow (A \uparrow B)$$
Substituting $A = p \uparrow p$:
$$\neg p \land q = \Big( (p \uparrow p) \uparrow q \Big) \uparrow \Big( (p \uparrow p) \uparrow q \Big)$$
This formula uses exclusively the NAND operator $\uparrow$. $\blacksquare$"""
            },
            {
                "tier": "Advanced Level",
                "title": "Problem 1.2: Validity of Deductive Arguments and Resolution Refutation",
                "statement": r"""Consider the following argument in propositional logic:
1. $p \implies (q \lor r)$
2. $\neg q$
3. $s \implies \neg r$
4. $p \land s$
Conclusion: An explicit contradiction occurs (i.e., prove the set of premises is inconsistent using the Resolution Refutation algorithm).

1. Translate each premise into Conjunctive Normal Form (clausal form).
2. Apply the resolution inference rule step-by-step to derive the empty clause $\square$ (indicating inconsistency).
3. Verify the result using a direct truth-value assignment deduction.""",
                "hints": [
                    "Convert $p \implies (q \lor r)$ to $\neg p \lor q \lor r$.",
                    "Convert $s \implies \neg r$ to $\neg s \lor \neg r$.",
                    "$p \land s$ produces two separate unit clauses: $\{p\}$ and $\{s\}$."
                ],
                "solution": r"""### 1. Conversion to Clausal Form (CNF)
Each premise is transformed into a set of disjunctive clauses (literals connected by $\lor$):

- **Premise 1:** $p \implies (q \lor r) \equiv \neg p \lor q \lor r$.
  $$\text{Clause } C_1: \{\neg p, q, r\}$$
- **Premise 2:** $\neg q$.
  $$\text{Clause } C_2: \{\neg q\}$$
- **Premise 3:** $s \implies \neg r \equiv \neg s \lor \neg r$.
  $$\text{Clause } C_3: \{\neg s, \neg r\}$$
- **Premise 4:** $p \land s$. This splits into two distinct unit clauses:
  $$\text{Clause } C_4: \{p\}$$
  $$\text{Clause } C_5: \{s\}$$

The initial clause set is $\mathcal{S} = \{C_1, C_2, C_3, C_4, C_5\}$.

---

### 2. Resolution Refutation
Recall the resolution rule: from clauses $\{A, \ell\}$ and $\{B, \neg \ell\}$, deduce $\{A, B\}$.

- **Step 1:** Resolve $C_1 = \{\neg p, q, r\}$ with $C_4 = \{p\}$ on literal $p$:
  $$\text{Resolvent } C_6: \{q, r\}$$
- **Step 2:** Resolve $C_6 = \{q, r\}$ with $C_2 = \{\neg q\}$ on literal $q$:
  $$\text{Resolvent } C_7: \{r\}$$
- **Step 3:** Resolve $C_3 = \{\neg s, \neg r\}$ with $C_7 = \{r\}$ on literal $r$:
  $$\text{Resolvent } C_8: \{\neg s\}$$
- **Step 4:** Resolve $C_8 = \{\neg s\}$ with $C_5 = \{s\}$ on literal $s$:
  $$\text{Resolvent } C_9: \square \quad (\text{the empty clause})$$

Deriving the empty clause $\square$ rigorously proves that the conjunction of all premises is unsatisfiable:
$$(p \implies (q \lor r)) \land \neg q \land (s \implies \neg r) \land (p \land s) \equiv \mathbf{F}$$

---

### 3. Direct Truth Assignment Verification
Assume all premises are simultaneously true:
1. From Premise 4 ($p \land s$), we must have $p = 1$ and $s = 1$.
2. From Premise 2 ($\neg q$), we must have $q = 0$.
3. Since $s = 1$, Premise 3 ($s \implies \neg r$) requires $1 \implies \neg r$, which forces $\neg r = 1 \implies r = 0$.
4. Now examine Premise 1 ($p \implies (q \lor r)$):
   $$1 \implies (0 \lor 0) \iff 1 \implies 0 \iff 0$$
Premise 1 evaluates to False, directly contradicting the assumption that Premise 1 is true.
Thus, no satisfying truth assignment exists. $\blacksquare$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 1.3: Rigorous Analysis of Alternating Quantifiers in Function Analysis",
                "statement": r"""Let $f: \mathbb{R} \to \mathbb{R}$ be a real-valued function.
Consider the following two quantified propositions:
$$\Phi_1: \quad \forall \epsilon > 0 \; \exists \delta > 0 \; \forall x \in \mathbb{R} \; (|x - 2| < \delta \implies |f(x) - 7| < \epsilon)$$
$$\Phi_2: \quad \exists \delta > 0 \; \forall \epsilon > 0 \; \forall x \in \mathbb{R} \; (|x - 2| < \delta \implies |f(x) - 7| < \epsilon)$$

1. Formulate the precise mathematical meaning of both propositions $\Phi_1$ and $\Phi_2$.
2. Prove that $\Phi_2 \implies \Phi_1$.
3. Construct an explicit function $f(x)$ such that $\Phi_1$ is true, but $\Phi_2$ is false, proving that the converse implication does NOT hold.
4. Characterize all functions $f(x)$ for which $\Phi_2$ is true.""",
                "hints": [
                    "$\Phi_1$ is the definition of $\lim_{x \to 2} f(x) = 7$.",
                    "In $\Phi_2$, $\delta$ cannot depend on $\epsilon$. If $|f(x) - 7| < \epsilon$ for every $\epsilon > 0$, what must $|f(x) - 7|$ equal?",
                    "Recall that if a real number $a \ge 0$ satisfies $a < \epsilon$ for all $\epsilon > 0$, then $a = 0$."
                ],
                "solution": r"""### 1. Mathematical Interpretations
- **Proposition $\Phi_1$:**
  This is the classical Cauchy definition of a function limit:
  $$\lim_{x \to 2} f(x) = 7$$
  It asserts that for every desired tolerance $\epsilon > 0$, there exists some neighborhood radius $\delta(\epsilon) > 0$ such that all $x$ within distance $\delta$ of 2 have values $f(x)$ within distance $\epsilon$ of 7.

- **Proposition $\Phi_2$:**
  This states that there exists a **fixed** radius $\delta_0 > 0$ such that for **all** $\epsilon > 0$, whenever $|x - 2| < \delta_0$, $|f(x) - 7| < \epsilon$.

---

### 2. Proof that $\Phi_2 \implies \Phi_1$
Assume $\Phi_2$ is true.
1. Then there exists $\delta_0 > 0$ such that for all $\epsilon > 0$ and all $x \in \mathbb{R}$, $|x - 2| < \delta_0 \implies |f(x) - 7| < \epsilon$.
2. To prove $\Phi_1$, let an arbitrary $\epsilon_0 > 0$ be given.
3. Choose $\delta = \delta_0$.
4. Then for all $x \in \mathbb{R}$, if $|x - 2| < \delta = \delta_0$, the hypothesis of $\Phi_2$ applies to the specific choice $\epsilon = \epsilon_0$, guaranteeing that $|f(x) - 7| < \epsilon_0$.
5. Thus $\Phi_1$ holds. $\blacksquare$

---

### 3. Counterexample Demonstrating $\Phi_1 \not\implies \Phi_2$
Consider the linear function:
$$f(x) = 3x + 1$$
- **Verification of $\Phi_1$:**
  Observe $|f(x) - 7| = |(3x + 1) - 7| = |3x - 6| = 3|x - 2|$.
  For any given $\epsilon > 0$, choose $\delta = \frac{\epsilon}{3} > 0$.
  Then $|x - 2| < \delta \implies 3|x - 2| < 3\left(\frac{\epsilon}{3}\right) = \epsilon$.
  Hence $\lim_{x \to 2} f(x) = 7$, so $\Phi_1$ is true.

- **Refutation of $\Phi_2$:**
  Suppose for contradiction that $\Phi_2$ were true for $f(x) = 3x + 1$.
  Then there exists some fixed $\delta_0 > 0$ such that:
  $$\forall \epsilon > 0 \; \forall x \; (|x - 2| < \delta_0 \implies 3|x - 2| < \epsilon)$$
  Consider the point $x_1 = 2 + \frac{\delta_0}{2}$.
  Clearly $|x_1 - 2| = \frac{\delta_0}{2} < \delta_0$.
  Then for every $\epsilon > 0$, we must have:
  $$3|x_1 - 2| = 3\left(\frac{\delta_0}{2}\right) = \frac{3\delta_0}{2} < \epsilon$$
  Now choose $\epsilon = \delta_0 > 0$.
  This implies $\frac{3}{2}\delta_0 < \delta_0 \implies \frac{3}{2} < 1$, which is an absurd contradiction!
  Therefore, $\Phi_2$ is false for $f(x) = 3x + 1$.

---

### 4. Complete Characterization of Functions Satisfying $\Phi_2$
> **Lemma:** If a non-negative real number $y \ge 0$ satisfies $y < \epsilon$ for every $\epsilon > 0$, then $y = 0$.
> *Proof:* If $y > 0$, choose $\epsilon = y/2 > 0$. Then $y < y/2 \implies 1 < 1/2$, a contradiction.

Applying this lemma to $\Phi_2$:
For any $x$ satisfying $|x - 2| < \delta_0$, we have $|f(x) - 7| < \epsilon$ for all $\epsilon > 0$.
Therefore, $|f(x) - 7| = 0 \iff f(x) = 7$.

**Conclusion:** $\Phi_2$ is true if and only if $f(x)$ is **identically equal to 7** on some open neighborhood $(2 - \delta_0, 2 + \delta_0)$ of $x = 2$.
This reveals the enormous structural difference produced by swapping the order of the quantifiers $\forall \epsilon$ and $\exists \delta$! $\blacksquare$"""
            }
        ]
    }
    return u1

if __name__ == "__main__":
    u1 = get_unit1()
    print(f"Loaded Unit 1: {u1['title']} with {len(u1['sections'])} sections and {len(u1['problems'])} problems.")
