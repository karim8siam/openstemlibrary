# Unit 1 — Proofs as mathematical objects

**Purpose.** A proof is a finite derivation with declared hypotheses, inference rules and a conclusion.

**Running application.** An automated theorem-checking service must distinguish proof certificates from true answers.

**Dangerous assumption.** Do not replace rule-by-rule derivability with the output of a truth-table checker.

## Research orientation and operational meaning

A mathematical proof is not a persuasive story. A proof certificate must encode a finite tree or list, identify permitted inference patterns, and give enough context that every step has a valid parent. This point helps separate theorem discovery from trusted checking. A speculative language-model answer may suggest a theorem but its plausibility does not make it derivable. An evaluator should be able to replay the certificate with no access to the search method that produced it.

For the running service, store every formula as an abstract syntax tree, rather than accepting unvalidated user text. Store hypotheses as references with stable identifiers and represent discharge by a scoped object. The system should reject references to a line not yet introduced, circular proof dependencies, and mismatched formula schemas. Verification produces an evidence record, not a declaration that the user intended the right formalization.

The continuing case in this unit is **Formal verifier procurement**, specifically **every rule must have a verifier-side check, and timeouts must not be reported as counterexamples**. The main complication is **a purported proof search service advertising fully trustworthy derivations**. A formal report should record what is defined inside the logic and what requires a separate observation or human specification. The expected deliverable is: **A trace should remain checkable with the original heuristic unplugged.** This requirement makes the case genuinely useful rather than merely decorative; the proof language solves the implication problem only after the relevant facts have been expressed as formulas.

## Working with derivations rather than slogans

Read the judgment from right to left as a verification problem. Start with the conclusion; ask which inference rule could yield its outermost connective. Then look at the available premises and whether that rule permits the desired dependency. This is different from guessing the truth of the conclusion by intuition. A rule instance may be syntactically valid even though no human explanation about an application has yet been provided.

When a step fails, make the smallest possible diagnosis: wrong formula shape, missing premise, unclosed assumption, illicit substitution, or mismatched conclusion. An automated verifier can report these categories without solving the theorem. Proof search may use caches and heuristics, but it should feed ordinary certificates to the checker.

A deliberately minimal audit record has five fields: formal premises, goal formula, inference-rule schema, concrete substitution into that schema, and remaining open obligations. The audit record should not confuse a witness term with an interpretation, a goal with an assumption, or a line of output with a theorem. When a rule has side conditions, record them just as carefully as the displayed conclusion. In a system that discharges assumptions, the scope of the discharge belongs to the proof object.

When the answer to a mathematical question is negative, supply evidence of the right kind. For finite propositional entailment, one satisfying valuation for the premises that falsifies the goal is decisive. For a claimed formula in a first-order setting, a legitimate structure and assignment can serve as a countermodel. For search failure on an undecidable class, however, no verdict follows. This evidence hierarchy will recur through every chapter, because it is central to responsible research and publication.

## Lesson 1.1 — Judgments and entailment

### Exact rule or metatheorem

**Formal content.** A judgment Γ ⊢ A says formula A has a derivation from the finite hypotheses Γ under named rules. Semantic entailment Γ ⊨ A concerns every interpretation satisfying Γ. The turnstiles denote different relations.

### Worked argument with line-by-line reasoning

**Worked demonstration.** Let Γ={P, P→Q}. Assume P and P→Q, and apply implication elimination to obtain Q. This three-line derivation is a certificate for Γ ⊢ Q. Soundness later implies Γ ⊨ Q, but semantic truth was not the inference rule used.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **judgments and entailment** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Writing Γ ⊨ Q when only a syntactic proof object is being constructed.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** For Γ={P→Q,Q→R,P}, derive R without any semantic truth table. **Solution or proof outline.** From P and P→Q get Q; from Q and Q→R get R. Each inference is modus ponens. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Can Q be derived from {P→Q} alone? Produce a countervaluation. **Expected explanation.** No. Put P=false and Q=false; P→Q is true while Q is false. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **judgments and entailment** to **formal verifier procurement** in the setting **every rule must have a verifier-side check, and timeouts must not be reported as counterexamples**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a purported proof search service advertising fully trustworthy derivations**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 1.2 — Well-formed formulas and proof trees

### Exact rule or metatheorem

**Formal content.** Specify atoms, parenthesized compound formulas, and inference trees inductively. A proof tree has premises at parent nodes and one conclusion at its root; each node must match a rule.

### Worked argument with line-by-line reasoning

**Worked demonstration.** Let A=(P∧(P→Q)). Parse A as a conjunction whose second operand is an implication. Derive P by ∧ elimination and P→Q by ∧ elimination, then Q by → elimination. The syntax tree is not the proof tree, even though both are trees.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **well-formed formulas and proof trees** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Treating arbitrary strings as formulas or inferring logical consequences merely from matching substrings.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Construct a parse tree for (P∨Q)→(Q∨P) and identify its main connective. **Solution or proof outline.** The outermost connective is implication; the antecedent and consequent are disjunctions. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Would P∧→Q be well formed under an infix fully-parenthesized grammar? **Expected explanation.** No. The binary connective lacks a left or right formula in the required syntax. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **well-formed formulas and proof trees** to **formal verifier procurement** in the setting **every rule must have a verifier-side check, and timeouts must not be reported as counterexamples**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a purported proof search service advertising fully trustworthy derivations**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 1.3 — Assumptions and consequence relations

### Exact rule or metatheorem

**Formal content.** A derivation may depend on open assumptions. In systems with implication introduction, a derivation Γ,A ⊢ B can be transformed into Γ ⊢ A→B by discharging that occurrence of A.

### Worked argument with line-by-line reasoning

**Worked demonstration.** To derive P→P, temporarily assume P, write P by assumption, then discharge that P by → introduction. The resulting theorem has no open assumptions. The subproof containing P is still part of the proof object.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **assumptions and consequence relations** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Forgetting that the dependency of a line depends on exactly which assumption labels remain open.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Derive P→(Q→P) with nested assumptions. **Solution or proof outline.** Assume P, then Q, then cite P. Discharge Q to infer Q→P and discharge P to infer P→(Q→P). The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Does discharge mean P becomes false? **Expected explanation.** No. It removes a dependency, rather than assigning a truth value. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **assumptions and consequence relations** to **formal verifier procurement** in the setting **every rule must have a verifier-side check, and timeouts must not be reported as counterexamples**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a purported proof search service advertising fully trustworthy derivations**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 1.4 — Substitution and schematic rules

### Exact rule or metatheorem

**Formal content.** A rule schema may be instantiated uniformly with formulas; substituting a formula for an atom must replace every free occurrence designated by the schema. First-order capture avoidance is a separate later issue.

### Worked argument with line-by-line reasoning

**Worked demonstration.** Start with schematic rule A,A→B / B. Substitute A := (P∨R) and B := (R∧S). The valid instance has premises P∨R and (P∨R)→(R∧S), with conclusion R∧S. The implication premise alone is not enough.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **substitution and schematic rules** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Replacing A by different formulas in different occurrences of the same schematic inference.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Instantiate conjunction elimination with A=(P→Q), B=R, and write the resulting rule instance. **Solution or proof outline.** From (P→Q)∧R infer P→Q, or infer R by the other elimination rule. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Could one replace A with P in the premise and Q in the conclusion? **Expected explanation.** Not in one uniform instance of a rule schema. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **substitution and schematic rules** to **formal verifier procurement** in the setting **every rule must have a verifier-side check, and timeouts must not be reported as counterexamples**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a purported proof search service advertising fully trustworthy derivations**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 1.5 — Proof checking versus theorem discovery

### Exact rule or metatheorem

**Formal content.** Proof verification checks each finite line against local inference rules; proof search attempts to discover a sequence of such steps. A verifier should be simpler and more trustworthy than a search heuristic.

### Worked argument with line-by-line reasoning

**Worked demonstration.** A candidate trace contains 1:P; 2:P→Q; 3:Q from 1 and 2 by →E. The checker verifies premises and rule instantiation. If line 3 were R, the trace would be rejected even if R happened to be true under a particular interpretation.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **proof checking versus theorem discovery** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Mistaking the absence of a discovered proof for a semantic counterexample or unprovability theorem.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Design a three-line proof certificate for {A,A→B}⊢B. State what a small checker must verify. **Solution or proof outline.** Record rule name →E and premise references. Check that one earlier formula is A and another A→B and that conclusion is B. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** If search reaches a time limit, what is established? **Expected explanation.** Only that this search run did not finish; no logical nonderivability follows. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **proof checking versus theorem discovery** to **formal verifier procurement** in the setting **every rule must have a verifier-side check, and timeouts must not be reported as counterexamples**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a purported proof search service advertising fully trustworthy derivations**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Unit 1 capstone — Proofs as mathematical objects

**Design brief.** Build a reviewable specification for **Formal verifier procurement**. Begin with the formal vocabulary that represents **every rule must have a verifier-side check, and timeouts must not be reported as counterexamples**. Use at least three of the unit’s five lesson rules in one coherent derivation and one adversarial countercase. Do not use a model screenshot as the sole supporting evidence for a general inference. Report the assumptions that can be checked mechanically and the application assumptions that cannot. The most important quality boundary is **a purported proof search service advertising fully trustworthy derivations**.

### Deliverables and answer checkpoints

1. Define the logical calculus, syntax and semantics you are using. This step prevents an unannounced change from classical to intuitionistic rules. 2. Construct a derivation with at least six labeled inference steps or give a checked proof-search tree where every leaf closes by a legitimate initial rule. 3. Provide a negative test case. For a propositional problem include a concrete valuation; for a rule-scope error show the illegal dependency; for a first-order issue give a finite countermodel when one exists. 4. Explain whether the produced artifact is a proof, refutation, illustrative simulation or incomplete search record. 5. Write a short assurance statement describing the remaining outside-the-logic questions.

**A sample critique.** A project report says that **formal verifier procurement** is correct because a demo displayed a green status and accepted two sample inputs. The critique should reject this as logically inadequate. The green status may show that the interface reacted, but not that the rule system is sound. Replace the vague claim with specific evidence: a formal statement of the goal, a complete proof trace, a verified derivation and an independent check of **a purported proof search service advertising fully trustworthy derivations**. The final write-up should make **a trace should remain checkable with the original heuristic unplugged.** clear.

### Rubric (100 points)

Formal statement and declared logic: 20. Complete rule-by-rule argument: 25. Correct assumption/freshness or structural bookkeeping: 20. Negative tests and countercases: 15. Honest evidence classification: 10. Clarity and reproducibility: 10. An elegant but unchecked demonstration cannot receive full correctness marks. A correct theorem about a visibly mistranslated real-world specification requires an explicit qualification.

### End-of-unit oral examination

**Question 1.** What would count as decisive evidence for the claim in **proofs as mathematical objects**, and what would be merely illustrative?

**Question 2.** Choose the unit’s most important side condition and construct a case that violates it. Explain what changes in the conclusion.

**Question 3.** Explain how you could independently audit **a trace should remain checkable with the original heuristic unplugged.** without trusting the original proof-search heuristic.
