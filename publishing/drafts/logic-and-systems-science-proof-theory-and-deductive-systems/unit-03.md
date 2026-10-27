# Unit 3 — Quantifiers, identity, and dependencies

**Purpose.** Variable scope, instantiation and freshness conditions determine whether first-order proof steps are legal.

**Running application.** A research database contains measurements for every sampled object, not necessarily every object.

**Dangerous assumption.** A fresh arbitrary parameter is not a convenient witness selected for an existential premise.

## Research orientation and operational meaning

A quantified claim adds two moving parts absent from propositional logic: the individual objects in the domain and variable-binding rules. A single sample can establish an existential statement, but a universal one requires a genuinely arbitrary object. Conversely, an existential premise offers only a temporary witness whose identity must not leak into conclusions. Scope is therefore not just typography; it decides the truth conditions and legality of derivations.

When formalizing scientific data, distinguish the sampled population from the universe of discourse. “Every sampled material failed at 500°C” differs from “Every possible material fails at 500°C.” Logic can check the conditional reasoning from an assumed dataset, but cannot validate the dataset itself. Formal witnesses are also not necessarily searchable measurements; a theory may assert that something exists without providing an effective algorithm for finding it.

The continuing case in this unit is **Research-subject registration**, specifically **registered objects form an explicitly bounded domain rather than all possible specimens**. The main complication is **a registry of specimens and observed properties with quantified claims**. A formal report should record what is defined inside the logic and what requires a separate observation or human specification. The expected deliverable is: **A globally asserted universal law cannot be inferred from a finite cohort.** This requirement makes the case genuinely useful rather than merely decorative; the proof language solves the implication problem only after the relevant facts have been expressed as formulas.

## Working with derivations rather than slogans

Quantifier steps are never ordinary propositional replacements. An arbitrary parameter used for universal introduction must not rely on special open assumptions. A witness introduced for existential elimination remains temporary and cannot appear in the final derived statement. These restrictions are precisely the difference between a sound general argument and extrapolation from one individual.

Alpha-renaming is a logically harmless change of a bound variable name, but variable capture is not harmless. In a nested formula, replacing a free variable with a term containing a binder variable may change the set of possible assignments. Document substitutions explicitly and, when in doubt, rename the binder before introducing a term.

A deliberately minimal audit record has five fields: formal premises, goal formula, inference-rule schema, concrete substitution into that schema, and remaining open obligations. The audit record should not confuse a witness term with an interpretation, a goal with an assumption, or a line of output with a theorem. When a rule has side conditions, record them just as carefully as the displayed conclusion. In a system that discharges assumptions, the scope of the discharge belongs to the proof object.

When the answer to a mathematical question is negative, supply evidence of the right kind. For finite propositional entailment, one satisfying valuation for the premises that falsifies the goal is decisive. For a claimed formula in a first-order setting, a legitimate structure and assignment can serve as a countermodel. For search failure on an undecidable class, however, no verdict follows. This evidence hierarchy will recur through every chapter, because it is central to responsible research and publication.

## Lesson 3.1 — Universal elimination

### Exact rule or metatheorem

**Formal content.** From ∀x A(x) infer A(t) provided term t is free for x in A. Free-for means substitution must avoid binding variables occurring within t.

### Worked argument with line-by-line reasoning

**Worked demonstration.** From ∀x (Student(x)→Registered(x)) infer Student(a)→Registered(a), then with Student(a) obtain Registered(a). The proof uses one universal instantiation followed by implication elimination.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **universal elimination** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Instantiating a quantifier with a variable that becomes captured by an inner binder.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Derive P(c) from ∀x(P(x)∧Q(x)). **Solution or proof outline.** Instantiate x with c to obtain P(c)∧Q(c); use ∧E₁. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Why is substitution of y for x in ∀y R(x,y) delicate? **Expected explanation.** Naive substitution produces ∀y R(y,y), changing meaning. Alpha-rename bound y first. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **universal elimination** to **research-subject registration** in the setting **registered objects form an explicitly bounded domain rather than all possible specimens**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a registry of specimens and observed properties with quantified claims**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 3.2 — Universal introduction and eigenvariables

### Exact rule or metatheorem

**Formal content.** To infer ∀x A(x) by ∀I from A(a), the parameter a must be arbitrary: it may not occur in undischarged assumptions that determine its special properties.

### Worked argument with line-by-line reasoning

**Worked demonstration.** To prove ∀x(P(x)→P(x)), choose a fresh a, assume P(a), cite P(a), discharge to P(a)→P(a), then universally generalize because a is absent from undischarged assumptions.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **universal introduction and eigenvariables** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Generalizing from P(c) under open assumption P(c) to ∀xP(x).

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Give a proof of ∀x (R(x)→R(x)) from no assumptions. **Solution or proof outline.** Choose fresh a and prove R(a)→R(a) under temporary R(a); discharge, then use ∀I. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Provide a one-element counterexample to invalid generalization from P(c). **Expected explanation.** In domain {0,1}, with c=0 and P true only at 0, P(c) holds but ∀xP(x) fails. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **universal introduction and eigenvariables** to **research-subject registration** in the setting **registered objects form an explicitly bounded domain rather than all possible specimens**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a registry of specimens and observed properties with quantified claims**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 3.3 — Existential introduction

### Exact rule or metatheorem

**Formal content.** From A(t) infer ∃x A(x) when t is substitutable for x. This is a witness-producing direction: a particular example suffices for an existence claim.

### Worked argument with line-by-line reasoning

**Worked demonstration.** Given Prime(7), introduce ∃x Prime(x) using witness 7. The witness need not be unique. To infer ∃x(P(x)∧Q(x)), however, the same term must support both conjuncts.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **existential introduction** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Combining P(a) and Q(b) to conclude ∃x(P(x)∧Q(x)) without evidence that a=b.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** From P(k)∧R(k) prove ∃x(P(x)∧R(x)). **Solution or proof outline.** Apply ∃I directly with witness k and matrix P(x)∧R(x). The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Do ∃xP(x) and ∃xQ(x) entail ∃x(P(x)∧Q(x))? **Expected explanation.** No: a two-element model with disjoint predicates provides a counterexample. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **existential introduction** to **research-subject registration** in the setting **registered objects form an explicitly bounded domain rather than all possible specimens**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a registry of specimens and observed properties with quantified claims**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 3.4 — Existential elimination and fresh witnesses

### Exact rule or metatheorem

**Formal content.** From ∃x A(x), temporarily assume A(c) for a fresh c and derive C. If c occurs neither in the outer undischarged assumptions nor in C, discharge A(c) to obtain C.

### Worked argument with line-by-line reasoning

**Worked demonstration.** From ∃x(P(x)∧Q(x)) derive ∃xP(x). Open a fresh c with P(c)∧Q(c); eliminate ∧ to P(c); introduce ∃xP(x); close the ∃E branch. The conclusion does not mention c.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **existential elimination and fresh witnesses** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Assuming that an existential premise names a globally fixed specific element; this violates freshness.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** From ∃x(P(x)∧Q(x)) derive ∃xQ(x). **Solution or proof outline.** Use ∃E on a fresh a, extract Q(a), introduce ∃xQ(x), then close the branch. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Why cannot ∃E conclude P(c) for the fresh temporary c? **Expected explanation.** The witness name would escape the local branch and make an illicit global choice. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **existential elimination and fresh witnesses** to **research-subject registration** in the setting **registered objects form an explicitly bounded domain rather than all possible specimens**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a registry of specimens and observed properties with quantified claims**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 3.5 — Equality rules and substitution

### Exact rule or metatheorem

**Formal content.** Equality reflexivity gives t=t. Equality elimination permits replacement of equals within formulas where substitution is legitimate; predicate positions and scope must be respected.

### Worked argument with line-by-line reasoning

**Worked demonstration.** Given a=b and F(a), equality elimination yields F(b). If equality appears beneath quantifiers, alpha-renaming avoids variable capture. Symmetry can be derived from reflexivity plus substitution, not assumed as an unexplained semantic step.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **equality rules and substitution** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Replacing a term across a binder even when the replacement captures a variable or changes bound-variable dependencies.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Derive b=a from a=b and equality reflexivity. **Solution or proof outline.** Start with a=a; by substituting b for the first a using a=b in the predicate X↦(X=a), infer b=a. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** From a=b and P(a), what additional step is required to infer ∃x P(x)? **Expected explanation.** Use equality elimination to obtain P(b) if desired, then existential introduction; the existential actually follows from P(a) alone. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **equality rules and substitution** to **research-subject registration** in the setting **registered objects form an explicitly bounded domain rather than all possible specimens**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a registry of specimens and observed properties with quantified claims**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Unit 3 capstone — Quantifiers, identity, and dependencies

**Design brief.** Build a reviewable specification for **Research-subject registration**. Begin with the formal vocabulary that represents **registered objects form an explicitly bounded domain rather than all possible specimens**. Use at least three of the unit’s five lesson rules in one coherent derivation and one adversarial countercase. Do not use a model screenshot as the sole supporting evidence for a general inference. Report the assumptions that can be checked mechanically and the application assumptions that cannot. The most important quality boundary is **a registry of specimens and observed properties with quantified claims**.

### Deliverables and answer checkpoints

1. Define the logical calculus, syntax and semantics you are using. This step prevents an unannounced change from classical to intuitionistic rules. 2. Construct a derivation with at least six labeled inference steps or give a checked proof-search tree where every leaf closes by a legitimate initial rule. 3. Provide a negative test case. For a propositional problem include a concrete valuation; for a rule-scope error show the illegal dependency; for a first-order issue give a finite countermodel when one exists. 4. Explain whether the produced artifact is a proof, refutation, illustrative simulation or incomplete search record. 5. Write a short assurance statement describing the remaining outside-the-logic questions.

**A sample critique.** A project report says that **research-subject registration** is correct because a demo displayed a green status and accepted two sample inputs. The critique should reject this as logically inadequate. The green status may show that the interface reacted, but not that the rule system is sound. Replace the vague claim with specific evidence: a formal statement of the goal, a complete proof trace, a verified derivation and an independent check of **a registry of specimens and observed properties with quantified claims**. The final write-up should make **a globally asserted universal law cannot be inferred from a finite cohort.** clear.

### Rubric (100 points)

Formal statement and declared logic: 20. Complete rule-by-rule argument: 25. Correct assumption/freshness or structural bookkeeping: 20. Negative tests and countercases: 15. Honest evidence classification: 10. Clarity and reproducibility: 10. An elegant but unchecked demonstration cannot receive full correctness marks. A correct theorem about a visibly mistranslated real-world specification requires an explicit qualification.

### End-of-unit oral examination

**Question 1.** What would count as decisive evidence for the claim in **quantifiers, identity, and dependencies**, and what would be merely illustrative?

**Question 2.** Choose the unit’s most important side condition and construct a case that violates it. Explain what changes in the conclusion.

**Question 3.** Explain how you could independently audit **a globally asserted universal law cannot be inferred from a finite cohort.** without trusting the original proof-search heuristic.
