# Unit 8 — Constructive logic and machine-checked proofs

**Purpose.** Proofs can carry constructions and can be checked by small kernels under typed rules.

**Running application.** Students translate informal arguments into explicit programs and proof terms.

**Dangerous assumption.** A finite interactive model is a teaching aid, not a formally verified kernel or proof of a universal theorem.

## Research orientation and operational meaning

Constructive proof terms connect logical reasoning with typed programming. A proof of A→B behaves like a function converting evidence for A to evidence for B. A proof of A∧B packages two pieces of evidence; a proof of A∨B chooses a tagged alternative. This correspondence is most precise in chosen type theories, and it does not license transferring every programming-language behavior into logic unchanged.

Machine-assisted checking reduces certain classes of error but cannot choose the correct real-world problem statement for the human. A proof assistant kernel may establish an exact theorem about an incorrectly modeled hardware circuit, chemical process or regulatory requirement. Strong publication practice therefore combines formal checking with specification review, independent mathematics review and clear disclosure of demonstrational simulations.

The continuing case in this unit is **Machine-checked student submissions**, specifically **kernel checking cannot verify what the student meant by the chosen specification**. The main complication is **a course where submissions mix code, mathematical proof and empirical data**. A formal report should record what is defined inside the logic and what requires a separate observation or human specification. The expected deliverable is: **Present a proof certificate, a specification audit and a separate empirical justification.** This requirement makes the case genuinely useful rather than merely decorative; the proof language solves the implication problem only after the relevant facts have been expressed as formulas.

## Working with derivations rather than slogans

In constructive interpretations, a proof may carry a computational witness. An implication proof acts like a function on evidence, a conjunction proof produces a pair, and a disjunction proof selects a tagged branch. The correspondence is specified within an actual type system and its reduction relation.

A proof assistant tactic can automate search, but the trusted kernel checks resulting terms. This separation should guide educational tools as well: interactive simulations can make students curious, yet a robust claim of machine verification requires a formal language, proof object, declared axioms and a small trusted verifier.

A deliberately minimal audit record has five fields: formal premises, goal formula, inference-rule schema, concrete substitution into that schema, and remaining open obligations. The audit record should not confuse a witness term with an interpretation, a goal with an assumption, or a line of output with a theorem. When a rule has side conditions, record them just as carefully as the displayed conclusion. In a system that discharges assumptions, the scope of the discharge belongs to the proof object.

When the answer to a mathematical question is negative, supply evidence of the right kind. For finite propositional entailment, one satisfying valuation for the premises that falsifies the goal is decisive. For a claimed formula in a first-order setting, a legitimate structure and assignment can serve as a countermodel. For search failure on an undecidable class, however, no verdict follows. This evidence hierarchy will recur through every chapter, because it is central to responsible research and publication.

## Lesson 8.1 — Constructive provability

### Exact rule or metatheorem

**Formal content.** Intuitionistic logic emphasizes proofs that supply evidence: a proof of A∨B identifies a side, and a proof of ∃xA(x) presents a witness in common constructive interpretations. Classical excluded middle is not a theorem without extra principles.

### Worked argument with line-by-line reasoning

**Worked demonstration.** Prove (P∧Q)→P constructively by pairing elimination. The proof extracts an actual first component. To assert P∨¬P with arbitrary P requires classical reasoning; a finite sampled model cannot provide that constructive proof in general.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **constructive provability** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Equating constructive logic with merely avoiding computers or with empirical verifiability of all propositions.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Give constructive proof of P→(Q→P). **Solution or proof outline.** A function taking evidence p:P, then q:Q, returns p; formally λp.λq.p. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** What evidence should accompany ∃n(n=3)? **Expected explanation.** A witness 3 and a proof that 3=3. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **constructive provability** to **machine-checked student submissions** in the setting **kernel checking cannot verify what the student meant by the chosen specification**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a course where submissions mix code, mathematical proof and empirical data**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 8.2 — Types as propositions

### Exact rule or metatheorem

**Formal content.** Under Curry–Howard, propositions are types and proofs are terms. Conjunction corresponds to product type, implication to function type, and disjunction to sum type in suitable constructive type theories.

### Worked argument with line-by-line reasoning

**Worked demonstration.** A term λp.p of type A→A checks because under p:A the body p has type A; abstraction discharges the context entry. Pair (a,b) has product type A×B when a:A and b:B. Projection recovers the components.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **types as propositions** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Assuming arbitrary executable code is automatically a proof of its advertised type without type checking or trusted axioms.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Give term and type for swapping a product A×B to B×A. **Solution or proof outline.** λp.(snd p, fst p) has type (A×B)→(B×A). The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Does inhabitation of A+B reveal which proposition has evidence? **Expected explanation.** Yes: a term is constructed as inl a or inr b in the ordinary sum-type interpretation. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **types as propositions** to **machine-checked student submissions** in the setting **kernel checking cannot verify what the student meant by the chosen specification**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a course where submissions mix code, mathematical proof and empirical data**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 8.3 — Proof assistants and trusted kernels

### Exact rule or metatheorem

**Formal content.** A proof assistant uses elaboration and tactics to construct proof terms, then a smaller kernel checks them against the logical calculus. Trust depends on implementation, axioms and compilation boundary.

### Worked argument with line-by-line reasoning

**Worked demonstration.** For goal P→P, a tactic interface may introduce variable h:P and close the goal with exact h. The kernel checks the resulting function λh.h; the tactic itself need not be part of the trusted mathematical core.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **proof assistants and trusted kernels** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Claiming machine verification guarantees correctness of external specifications, modeling assumptions or a compromised checker.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Write a Lean-like pseudocode proof of P→P and explain which part is trusted. **Solution or proof outline.** theorem self (P : Prop) : P → P := by intro h; exact h. A small checker validates the resulting term according to its axioms. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Can a theorem prover validate a false specification as true of the world? **Expected explanation.** It can prove a theorem about an incorrect formalization; model adequacy remains external. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **proof assistants and trusted kernels** to **machine-checked student submissions** in the setting **kernel checking cannot verify what the student meant by the chosen specification**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a course where submissions mix code, mathematical proof and empirical data**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 8.4 — Proof-carrying verification

### Exact rule or metatheorem

**Formal content.** Proof-carrying systems attach a checkable certificate to a program, transformation or mathematical claim. A checker validates the certificate under a formally specified semantics; independent testing targets the implementation and interface.

### Worked argument with line-by-line reasoning

**Worked demonstration.** A SAT solver returns UNSAT plus a resolution-like trace. A verifier checks each step against the original clauses and detects a final empty clause. A GUI saying “valid” is not, by itself, the trace.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **proof-carrying verification** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Accepting an opaque success flag or untyped string as proof evidence; substituting a random sample test for a complete certificate.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Specify the minimal certificate for the clauses P and ¬P. **Solution or proof outline.** Include the two input clauses and a resolution step on P yielding the empty clause; the checker verifies the complementary pivot. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Why is source validation still needed after certificate checking? **Expected explanation.** The formalized inputs may omit real requirements or mistranslate the user’s original problem. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **proof-carrying verification** to **machine-checked student submissions** in the setting **kernel checking cannot verify what the student meant by the chosen specification**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a course where submissions mix code, mathematical proof and empirical data**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 8.5 — Research synthesis and responsible claims

### Exact rule or metatheorem

**Formal content.** A rigorous submission distinguishes a proved theorem, a checked derivation, an illustrative finite simulation, a conjecture and a reported empirical observation. Reproducibility requires exact rule versions and data provenance.

### Worked argument with line-by-line reasoning

**Worked demonstration.** A browser model tests thirty valuations and finds no counterexample to A→A. This is supporting pedagogy, not the general theorem. The theorem is established by a rule derivation from assumption A followed by implication introduction, or by a semantic argument for all valuations.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **research synthesis and responsible claims** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Writing that a visually animated or heavily tested claim has been formally verified when only a few sampled cases were checked.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Design an evidence table for (P∧Q)→P listing proof, model and limitation. **Solution or proof outline.** Proof: assume P∧Q, infer P, discharge. Model: all four two-atom valuations satisfy the formula. Limitation: model checks alone do not justify claims about richer infinite languages. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** How should a failed proof attempt be reported? **Expected explanation.** As an incomplete attempt with open obligations, not as proof of the negation. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **research synthesis and responsible claims** to **machine-checked student submissions** in the setting **kernel checking cannot verify what the student meant by the chosen specification**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a course where submissions mix code, mathematical proof and empirical data**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Unit 8 capstone — Constructive logic and machine-checked proofs

**Design brief.** Build a reviewable specification for **Machine-checked student submissions**. Begin with the formal vocabulary that represents **kernel checking cannot verify what the student meant by the chosen specification**. Use at least three of the unit’s five lesson rules in one coherent derivation and one adversarial countercase. Do not use a model screenshot as the sole supporting evidence for a general inference. Report the assumptions that can be checked mechanically and the application assumptions that cannot. The most important quality boundary is **a course where submissions mix code, mathematical proof and empirical data**.

### Deliverables and answer checkpoints

1. Define the logical calculus, syntax and semantics you are using. This step prevents an unannounced change from classical to intuitionistic rules. 2. Construct a derivation with at least six labeled inference steps or give a checked proof-search tree where every leaf closes by a legitimate initial rule. 3. Provide a negative test case. For a propositional problem include a concrete valuation; for a rule-scope error show the illegal dependency; for a first-order issue give a finite countermodel when one exists. 4. Explain whether the produced artifact is a proof, refutation, illustrative simulation or incomplete search record. 5. Write a short assurance statement describing the remaining outside-the-logic questions.

**A sample critique.** A project report says that **machine-checked student submissions** is correct because a demo displayed a green status and accepted two sample inputs. The critique should reject this as logically inadequate. The green status may show that the interface reacted, but not that the rule system is sound. Replace the vague claim with specific evidence: a formal statement of the goal, a complete proof trace, a verified derivation and an independent check of **a course where submissions mix code, mathematical proof and empirical data**. The final write-up should make **present a proof certificate, a specification audit and a separate empirical justification.** clear.

### Rubric (100 points)

Formal statement and declared logic: 20. Complete rule-by-rule argument: 25. Correct assumption/freshness or structural bookkeeping: 20. Negative tests and countercases: 15. Honest evidence classification: 10. Clarity and reproducibility: 10. An elegant but unchecked demonstration cannot receive full correctness marks. A correct theorem about a visibly mistranslated real-world specification requires an explicit qualification.

### End-of-unit oral examination

**Question 1.** What would count as decisive evidence for the claim in **constructive logic and machine-checked proofs**, and what would be merely illustrative?

**Question 2.** Choose the unit’s most important side condition and construct a case that violates it. Explain what changes in the conclusion.

**Question 3.** Explain how you could independently audit **present a proof certificate, a specification audit and a separate empirical justification.** without trusting the original proof-search heuristic.
