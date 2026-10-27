# Unit 7 — Soundness, completeness and metatheory

**Purpose.** Theorems about provability rely on explicitly fixed languages, semantics and proof systems.

**Running application.** A model checker and proof generator are cross-audited against their advertised claims.

**Dangerous assumption.** First-order completeness does not assert that every true arithmetic sentence is provable in a chosen effective arithmetic theory.

## Research orientation and operational meaning

Soundness and completeness occupy opposite logical directions. Soundness excludes false theorems; completeness ensures semantically valid statements can be proved. Both are meaningful only after fixing the language and the semantics. Compactness and incompleteness are often misquoted because statements about all structures, the intended natural numbers and particular formal theories are conflated.

When reviewing an educational theorem, write the full quantifier structure of its metaclaim. “For every formula, if valid in every model then derivable” is not a claim that every question about a fixed model is decidable. The distinction matters for solver product claims: a tool may produce valid certificates whenever it terminates but still fail to terminate on some negative instances.

The continuing case in this unit is **Research theorem audit**, specifically **the quantifiers over formulas and models must be kept separate from intended structures**. The main complication is **a claim that a logical completeness theorem makes every question decidable**. A formal report should record what is defined inside the logic and what requires a separate observation or human specification. The expected deliverable is: **Differentiate consistency, satisfiability and effectiveness.** This requirement makes the case genuinely useful rather than merely decorative; the proof language solves the implication problem only after the relevant facts have been expressed as formulas.

## Working with derivations rather than slogans

A metatheorem quantifies over formulas, derivations and/or models rather than asserting a fact about an individual sentence. To understand it, write down the direction of implication and the background system. Soundness proves validity from derivability; completeness proves derivability from validity. Neither statement alone promises a short proof or a terminating algorithm.

Classical first-order logic is complete in the semantic/proof-theoretic sense, while an effective theory of arithmetic can leave arithmetic truths unproved. Compactness permits models of all finite fragments to be assembled into a model of an entire first-order theory; it does not guarantee that the intended standard model satisfies every fragment simultaneously.

A deliberately minimal audit record has five fields: formal premises, goal formula, inference-rule schema, concrete substitution into that schema, and remaining open obligations. The audit record should not confuse a witness term with an interpretation, a goal with an assumption, or a line of output with a theorem. When a rule has side conditions, record them just as carefully as the displayed conclusion. In a system that discharges assumptions, the scope of the discharge belongs to the proof object.

When the answer to a mathematical question is negative, supply evidence of the right kind. For finite propositional entailment, one satisfying valuation for the premises that falsifies the goal is decisive. For a claimed formula in a first-order setting, a legitimate structure and assignment can serve as a countermodel. For search failure on an undecidable class, however, no verdict follows. This evidence hierarchy will recur through every chapter, because it is central to responsible research and publication.

## Lesson 7.1 — Soundness by induction on proofs

### Exact rule or metatheorem

**Formal content.** A calculus is sound when Γ⊢A implies Γ⊨A. Prove soundness by induction on the finite derivation: assumptions are valid under valuations satisfying Γ; each inference rule preserves truth.

### Worked argument with line-by-line reasoning

**Worked demonstration.** For →E, suppose valuation v satisfies Γ, A and A→B. Material-implication truth conditions force v(B)=true. Thus the rule is sound. The global proof checks every primitive rule, not only this example.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **soundness by induction on proofs** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Arguing that several sample derivations prove soundness for all possible proofs.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Explain the soundness step for ∧E₁. **Solution or proof outline.** If v(A∧B)=true, then v(A)=true by semantics of ∧; so ∧E₁ preserves entailment. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Can soundness alone show every valid formula is provable? **Expected explanation.** No. That converse is completeness. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **soundness by induction on proofs** to **research theorem audit** in the setting **the quantifiers over formulas and models must be kept separate from intended structures**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a claim that a logical completeness theorem makes every question decidable**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 7.2 — Completeness and maximally consistent sets

### Exact rule or metatheorem

**Formal content.** Completeness is the converse direction Γ⊨A ⇒ Γ⊢A for a specified logic. Standard first-order proofs use extensions of consistent theories and construction of canonical or term models, with technical choices about equality and witnesses.

### Worked argument with line-by-line reasoning

**Worked demonstration.** For propositional logic, one may construct a satisfying valuation from a consistent set by assigning atom values coherently. If Γ∪{¬A} is inconsistent, then Γ⊢A in a classical calculus. Building the general argument requires a precise Lindenbaum lemma.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **completeness and maximally consistent sets** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Concluding first-order completeness by enumerating finitely many structures or assuming every theory has a finite model.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** State the contrapositive style of the completeness implication. **Solution or proof outline.** If Γ does not syntactically prove A, a completeness argument builds a model of Γ in which A fails (subject to the fixed classical first-order calculus). The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Does completeness mean theorem search always halts? **Expected explanation.** No. First-order validity is only semidecidable, not generally decidable. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **completeness and maximally consistent sets** to **research theorem audit** in the setting **the quantifiers over formulas and models must be kept separate from intended structures**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a claim that a logical completeness theorem makes every question decidable**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 7.3 — Compactness and finite support

### Exact rule or metatheorem

**Formal content.** The compactness theorem for classical first-order logic says a theory is satisfiable if every finite subset is satisfiable. Syntactically, a proof uses only finitely many premises, and completeness links this to models.

### Worked argument with line-by-line reasoning

**Worked demonstration.** Let Γ={c>n : n∈N} in the language of ordered fields with a new constant c. Every finite fragment is satisfiable in real numbers by choosing c large enough; compactness gives a model of the first-order theory of real closed fields with c larger than every standard numeral. That model is non-Archimedean.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **compactness and finite support** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Inferring that a single ordinary real c satisfies every inequality because each finite collection does.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Explain the finite-subset property for Γ={P₁,P₂,...} with no conflicting constraints. **Solution or proof outline.** Assign all atoms true; every finite subset and the entire propositional theory are satisfiable. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Why is compactness not a theorem about an arbitrary fixed standard structure? **Expected explanation.** It concerns existence of some model, which need not be the initially chosen intended structure. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **compactness and finite support** to **research theorem audit** in the setting **the quantifiers over formulas and models must be kept separate from intended structures**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a claim that a logical completeness theorem makes every question decidable**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 7.4 — Deduction and decidability

### Exact rule or metatheorem

**Formal content.** The deduction theorem connects Γ,A⊢B with Γ⊢A→B under familiar Hilbert and natural-deduction settings. Decidability asks for a terminating yes/no procedure for every input; recursively enumerable theorem sets need not be decidable.

### Worked argument with line-by-line reasoning

**Worked demonstration.** Propositional validity with n atoms is decidable by a 2^n truth-table scan. Classical first-order validity has complete proof enumeration for theorems but no general total decision procedure. Completeness does not collapse these complexity distinctions.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **deduction and decidability** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Treating enumerability of proofs as a guaranteed terminating refutation procedure for every invalid formula.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Define a terminating entailment test for a formula over at most three propositional atoms. **Solution or proof outline.** Evaluate all eight valuations; reject if any satisfies assumptions but falsifies conclusion, otherwise accept. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** What if no first-order proof is found after a million steps? **Expected explanation.** No conclusion follows about validity; the search may simply require longer. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **deduction and decidability** to **research theorem audit** in the setting **the quantifiers over formulas and models must be kept separate from intended structures**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a claim that a logical completeness theorem makes every question decidable**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 7.5 — Incompleteness and scope of metatheorems

### Exact rule or metatheorem

**Formal content.** Gödel incompleteness concerns sufficiently expressive, consistent, effectively axiomatized formal theories of arithmetic, under precise representability conditions. It does not contradict completeness of first-order logic.

### Worked argument with line-by-line reasoning

**Worked demonstration.** First-order logical completeness says every logically valid formula has a formal derivation. Arithmetic incompleteness says a fixed effective consistent arithmetic theory cannot capture every arithmetical truth in the intended natural-number structure. The domains of the claims differ.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **incompleteness and scope of metatheorems** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Calling every undecided practical problem a consequence of Gödel or using incompleteness as a reason to distrust ordinary deductions.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** State the contrast between semantic first-order validity and truth in standard N. **Solution or proof outline.** Logical validity ranges over all structures; standard arithmetic truth concerns one intended structure. A theory can be incomplete about the latter although the underlying logical proof calculus is complete. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Does first-order completeness give a decision procedure for the halting problem? **Expected explanation.** No. Soundness/completeness are metatheorems about derivability, not universal decision algorithms. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **incompleteness and scope of metatheorems** to **research theorem audit** in the setting **the quantifiers over formulas and models must be kept separate from intended structures**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a claim that a logical completeness theorem makes every question decidable**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Unit 7 capstone — Soundness, completeness and metatheory

**Design brief.** Build a reviewable specification for **Research theorem audit**. Begin with the formal vocabulary that represents **the quantifiers over formulas and models must be kept separate from intended structures**. Use at least three of the unit’s five lesson rules in one coherent derivation and one adversarial countercase. Do not use a model screenshot as the sole supporting evidence for a general inference. Report the assumptions that can be checked mechanically and the application assumptions that cannot. The most important quality boundary is **a claim that a logical completeness theorem makes every question decidable**.

### Deliverables and answer checkpoints

1. Define the logical calculus, syntax and semantics you are using. This step prevents an unannounced change from classical to intuitionistic rules. 2. Construct a derivation with at least six labeled inference steps or give a checked proof-search tree where every leaf closes by a legitimate initial rule. 3. Provide a negative test case. For a propositional problem include a concrete valuation; for a rule-scope error show the illegal dependency; for a first-order issue give a finite countermodel when one exists. 4. Explain whether the produced artifact is a proof, refutation, illustrative simulation or incomplete search record. 5. Write a short assurance statement describing the remaining outside-the-logic questions.

**A sample critique.** A project report says that **research theorem audit** is correct because a demo displayed a green status and accepted two sample inputs. The critique should reject this as logically inadequate. The green status may show that the interface reacted, but not that the rule system is sound. Replace the vague claim with specific evidence: a formal statement of the goal, a complete proof trace, a verified derivation and an independent check of **a claim that a logical completeness theorem makes every question decidable**. The final write-up should make **differentiate consistency, satisfiability and effectiveness.** clear.

### Rubric (100 points)

Formal statement and declared logic: 20. Complete rule-by-rule argument: 25. Correct assumption/freshness or structural bookkeeping: 20. Negative tests and countercases: 15. Honest evidence classification: 10. Clarity and reproducibility: 10. An elegant but unchecked demonstration cannot receive full correctness marks. A correct theorem about a visibly mistranslated real-world specification requires an explicit qualification.

### End-of-unit oral examination

**Question 1.** What would count as decisive evidence for the claim in **soundness, completeness and metatheory**, and what would be merely illustrative?

**Question 2.** Choose the unit’s most important side condition and construct a case that violates it. Explain what changes in the conclusion.

**Question 3.** Explain how you could independently audit **differentiate consistency, satisfiability and effectiveness.** without trusting the original proof-search heuristic.
