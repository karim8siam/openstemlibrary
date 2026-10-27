# Unit 6 — Other proof calculi and proof search

**Purpose.** Hilbert axioms, tableaux, resolution and search strategies produce different kinds of proof evidence.

**Running application.** A satisfiability tool must return either a falsifying assignment or a checkable proof trace.

**Dangerous assumption.** A closed search branch needs a sound closure rule; mere lack of progress is not a proof.

## Research orientation and operational meaning

Different calculi illuminate different computational tasks. Hilbert systems make axioms sparse but proofs can be long; tableaux search for models or contradictions by expanding semantic constraints; resolution is well adapted to clause-based automated reasoning. Selecting a calculus is an engineering decision about certificate size, search behavior, and the trust boundary. They may prove the same propositions in a shared fragment but their derivations are different objects.

A defensible solver interface returns either an explicit satisfying valuation or a checkable unsatisfiability proof, depending on the problem and proof format. An incomplete trace is not a certificate. SAT and first-order reasoning also differ: a fixed propositional assignment space can be completely enumerated, while the range of first-order structures includes unbounded and infinite domains.

The continuing case in this unit is **SAT and first-order verification pipeline**, specifically **a Boolean counterassignment and an UNSAT resolution trace are not interchangeable certificates**. The main complication is **a verifier receiving claimed satisfiability or unsatisfiability results**. A formal report should record what is defined inside the logic and what requires a separate observation or human specification. The expected deliverable is: **An unresolved branch is not evidence of inconsistency.** This requirement makes the case genuinely useful rather than merely decorative; the proof language solves the implication problem only after the relevant facts have been expressed as formulas.

## Working with derivations rather than slogans

Semantic tableaux start by negating a target when checking validity, and search for a valuation satisfying the negated goal. Resolution starts with clauses and aims to derive the empty clause. The two approaches produce distinct artifacts: a branch valuation, a closed tableau, or a clause derivation.

Search quality is not soundness. A fast solver may make heuristic guesses about which branch to visit first; these choices do not license any new inference rule. Every reported UNSAT claim should be backed by a recognized proof format or a verified exhaustive method for the defined finite setting.

A deliberately minimal audit record has five fields: formal premises, goal formula, inference-rule schema, concrete substitution into that schema, and remaining open obligations. The audit record should not confuse a witness term with an interpretation, a goal with an assumption, or a line of output with a theorem. When a rule has side conditions, record them just as carefully as the displayed conclusion. In a system that discharges assumptions, the scope of the discharge belongs to the proof object.

When the answer to a mathematical question is negative, supply evidence of the right kind. For finite propositional entailment, one satisfying valuation for the premises that falsifies the goal is decisive. For a claimed formula in a first-order setting, a legitimate structure and assignment can serve as a countermodel. For search failure on an undecidable class, however, no verdict follows. This evidence hierarchy will recur through every chapter, because it is central to responsible research and publication.

## Lesson 6.1 — Hilbert systems and derivation lists

### Exact rule or metatheorem

**Formal content.** A Hilbert presentation uses a few axiom schemas and typically modus ponens as its central inference rule. Deduction theorems connect derivations with implication structure subject to the system’s hypotheses.

### Worked argument with line-by-line reasoning

**Worked demonstration.** With axiom schema A→(B→A), instantiate A=P and B=Q to obtain P→(Q→P). In a Hilbert system this is a theorem schema instance rather than a nested natural-deduction proof.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **hilbert systems and derivation lists** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Assuming a printed axiom pattern is an arbitrary theorem regardless of uniform substitution and syntax.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Instantiate A→(B→A) with A=R∧S, B=T. **Solution or proof outline.** The instance is (R∧S)→(T→(R∧S)). The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Does Hilbert proof checking require unrestricted semantic validity checking at every line? **Expected explanation.** Not if axiom-schema matching and modus ponens are decidable syntactic checks. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **hilbert systems and derivation lists** to **sat and first-order verification pipeline** in the setting **a Boolean counterassignment and an UNSAT resolution trace are not interchangeable certificates**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a verifier receiving claimed satisfiability or unsatisfiability results**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 6.2 — Semantic tableaux

### Exact rule or metatheorem

**Formal content.** A tableau decomposes formulas into branch constraints. Conjunction keeps both conditions on the same branch; disjunction creates alternatives. A branch closes when it requires both an atom and its negation.

### Worked argument with line-by-line reasoning

**Worked demonstration.** Test validity of P→P by starting from its negation. Negating the implication requires P and ¬P on one branch, which closes. With standard classical rules, if all branches close, no countervaluation exists.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **semantic tableaux** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Closing a branch merely because it contains a complicated formula or because search cannot expand it.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Test satisfiability of P∨Q with a tableau. **Solution or proof outline.** One branch contains P and one contains Q; at least one branch is open, yielding a valuation satisfying P∨Q. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** When is an open finite branch a model certificate? **Expected explanation.** After all relevant formulas are fully expanded and coherent atomic assignments can be read off. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **semantic tableaux** to **sat and first-order verification pipeline** in the setting **a Boolean counterassignment and an UNSAT resolution trace are not interchangeable certificates**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a verifier receiving claimed satisfiability or unsatisfiability results**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 6.3 — Propositional resolution

### Exact rule or metatheorem

**Formal content.** A clause is a disjunction of literals. Resolving (A∨x) and (B∨¬x) produces (A∨B). A resolution refutation derives the empty clause from an unsatisfiable clause set.

### Worked argument with line-by-line reasoning

**Worked demonstration.** Take {P}, {¬P∨Q}, {¬Q}. Resolve {P} with {¬P∨Q} to get {Q}. Resolve {Q} with {¬Q} to obtain the empty clause. This finite derivation certifies inconsistency of the clause set.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **propositional resolution** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Deriving arbitrary clause conclusions without complementary literals, or treating an empty *set of clauses* as an empty *clause*.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Resolve {P,R} with {¬P,Q}. **Solution or proof outline.** The resolvent is {R,Q}; only P and ¬P are removed. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Can {P,Q} resolve with {P,R} on P? **Expected explanation.** Not by standard resolution because both have positive P, not complementary literals. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **propositional resolution** to **sat and first-order verification pipeline** in the setting **a Boolean counterassignment and an UNSAT resolution trace are not interchangeable certificates**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a verifier receiving claimed satisfiability or unsatisfiability results**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 6.4 — Unification and first-order resolution

### Exact rule or metatheorem

**Formal content.** First-order resolution combines clause reasoning with substitutions that make complementary atoms identical. Occurs checks prevent cyclic substitutions in ordinary first-order term algebra.

### Worked argument with line-by-line reasoning

**Worked demonstration.** Unify P(x,f(a)) with P(b,f(a)) by substitution x:=b. Then clauses P(x,f(a))∨R and ¬P(b,f(a))∨S resolve to R∨S under that substitution.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **unification and first-order resolution** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Omitting the occurs check, e.g. pretending x=f(x) has a finite first-order unifier.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Find an mgu for P(x,a) and P(f(b),y). **Solution or proof outline.** Use {x↦f(b), y↦a}; the resulting atoms are identical. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Why can unification fail for P(x) and P(f(x))? **Expected explanation.** The occurs check detects x inside f(x); no finite term substitutes for x. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **unification and first-order resolution** to **sat and first-order verification pipeline** in the setting **a Boolean counterassignment and an UNSAT resolution trace are not interchangeable certificates**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a verifier receiving claimed satisfiability or unsatisfiability results**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 6.5 — Search strategies and countermodels

### Exact rule or metatheorem

**Formal content.** Backward chaining, breadth-first enumeration and heuristic-guided proof search are strategies, not logical rules. A sound derivation is a proof; exhaustive terminating failure may support a negative result only for decidable fragments.

### Worked argument with line-by-line reasoning

**Worked demonstration.** For a finite propositional formula, enumerate 2^n assignments to search for a countermodel. If one falsifies the goal while satisfying premises, it disproves entailment. For unrestricted first-order logic, the same finite search is incomplete.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **search strategies and countermodels** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Describing a timeout, finite model-size bound or heuristic failure as an unprovability theorem.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Give a countermodel to {P∨Q} ⊨ P. **Solution or proof outline.** Set P=false, Q=true. Premise holds and conclusion fails. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Does failure to find a finite model imply unsatisfiability in first-order logic? **Expected explanation.** No. Some satisfiable first-order theories have only infinite models. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **search strategies and countermodels** to **sat and first-order verification pipeline** in the setting **a Boolean counterassignment and an UNSAT resolution trace are not interchangeable certificates**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a verifier receiving claimed satisfiability or unsatisfiability results**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Unit 6 capstone — Other proof calculi and proof search

**Design brief.** Build a reviewable specification for **SAT and first-order verification pipeline**. Begin with the formal vocabulary that represents **a Boolean counterassignment and an UNSAT resolution trace are not interchangeable certificates**. Use at least three of the unit’s five lesson rules in one coherent derivation and one adversarial countercase. Do not use a model screenshot as the sole supporting evidence for a general inference. Report the assumptions that can be checked mechanically and the application assumptions that cannot. The most important quality boundary is **a verifier receiving claimed satisfiability or unsatisfiability results**.

### Deliverables and answer checkpoints

1. Define the logical calculus, syntax and semantics you are using. This step prevents an unannounced change from classical to intuitionistic rules. 2. Construct a derivation with at least six labeled inference steps or give a checked proof-search tree where every leaf closes by a legitimate initial rule. 3. Provide a negative test case. For a propositional problem include a concrete valuation; for a rule-scope error show the illegal dependency; for a first-order issue give a finite countermodel when one exists. 4. Explain whether the produced artifact is a proof, refutation, illustrative simulation or incomplete search record. 5. Write a short assurance statement describing the remaining outside-the-logic questions.

**A sample critique.** A project report says that **sat and first-order verification pipeline** is correct because a demo displayed a green status and accepted two sample inputs. The critique should reject this as logically inadequate. The green status may show that the interface reacted, but not that the rule system is sound. Replace the vague claim with specific evidence: a formal statement of the goal, a complete proof trace, a verified derivation and an independent check of **a verifier receiving claimed satisfiability or unsatisfiability results**. The final write-up should make **an unresolved branch is not evidence of inconsistency.** clear.

### Rubric (100 points)

Formal statement and declared logic: 20. Complete rule-by-rule argument: 25. Correct assumption/freshness or structural bookkeeping: 20. Negative tests and countercases: 15. Honest evidence classification: 10. Clarity and reproducibility: 10. An elegant but unchecked demonstration cannot receive full correctness marks. A correct theorem about a visibly mistranslated real-world specification requires an explicit qualification.

### End-of-unit oral examination

**Question 1.** What would count as decisive evidence for the claim in **other proof calculi and proof search**, and what would be merely illustrative?

**Question 2.** Choose the unit’s most important side condition and construct a case that violates it. Explain what changes in the conclusion.

**Question 3.** Explain how you could independently audit **an unresolved branch is not evidence of inconsistency.** without trusting the original proof-search heuristic.
