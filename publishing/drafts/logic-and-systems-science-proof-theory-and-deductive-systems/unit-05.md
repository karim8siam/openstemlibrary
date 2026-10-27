# Unit 5 — Normalization, cut and consistency

**Purpose.** Proof transformations remove detours and clarify how computational and logical content are related.

**Running application.** A proof optimizer rewrites large evidence graphs without changing final judgments.

**Dangerous assumption.** A cut-elimination theorem applies to a specified calculus, not automatically to any axiom-enriched theory.

## Research orientation and operational meaning

Normalization illuminates a subtle difference between shortening the logical explanation and minimizing storage. Eliminating a detour can simplify a proof locally; eliminating a shared lemma can duplicate entire subderivations elsewhere. Proof theory studies the rewrite relation and its termination properties, not just visually pleasing proof trees. A rewriting system must preserve types and avoid accidental variable capture.

The lambda-calculus analogy makes this concrete. A function produced by abstraction and then immediately applied is a redex. Substituting an argument into the function body is logically similar to replacing a discharged assumption by its proof. Variable names are incidental when binding structure is preserved, so alpha-equivalent terms should be regarded as representing the same abstraction. Untyped terms may diverge; typed fragments have stronger normalization behavior.

The continuing case in this unit is **Proof optimizer**, specifically **logical soundness must be preserved even if the resulting proof is larger**. The main complication is **a tool removing redundant inference detours from a proof certificate**. A formal report should record what is defined inside the logic and what requires a separate observation or human specification. The expected deliverable is: **Compare both term typing and the open-assumption context before and after rewriting.** This requirement makes the case genuinely useful rather than merely decorative; the proof language solves the implication problem only after the relevant facts have been expressed as formulas.

## Working with derivations rather than slogans

The normalization problem is a rewrite problem over structured proofs. Identify an introduction immediately followed by a matching elimination, then eliminate the redundant pair while preserving typing and the ambient judgment. At an implication redex this is capture-avoiding substitution of an argument proof for a discharged assumption.

Global transformation theorems require termination or a well-founded induction argument. An animation that simplifies five examples is useful evidence about the implementation, not a proof about all finite derivations. In sequent calculus, cut elimination interacts with contraction and can expand proof size severely.

A deliberately minimal audit record has five fields: formal premises, goal formula, inference-rule schema, concrete substitution into that schema, and remaining open obligations. The audit record should not confuse a witness term with an interpretation, a goal with an assumption, or a line of output with a theorem. When a rule has side conditions, record them just as carefully as the displayed conclusion. In a system that discharges assumptions, the scope of the discharge belongs to the proof object.

When the answer to a mathematical question is negative, supply evidence of the right kind. For finite propositional entailment, one satisfying valuation for the premises that falsifies the goal is decisive. For a claimed formula in a first-order setting, a legitimate structure and assignment can serve as a countermodel. For search failure on an undecidable class, however, no verdict follows. This evidence hierarchy will recur through every chapter, because it is central to responsible research and publication.

## Lesson 5.1 — Introduction–elimination detours

### Exact rule or metatheorem

**Formal content.** A detour introduces a connective and immediately eliminates it. Normalization contracts such local redexes while preserving the judgment and properly managing assumptions.

### Worked argument with line-by-line reasoning

**Worked demonstration.** From derivation dA of A and dB of B, apply ∧I to A∧B, then ∧E₁ to A. The entire detour contracts to dA. All assumptions needed by dA remain, while those used only by dB may disappear.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **introduction–elimination detours** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Assuming every rewrite preserves the same set of used hypotheses, rather than preserving derivability under an ambient context.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Normalize a proof of Q obtained by introducing P∧Q and then taking its right projection. **Solution or proof outline.** Replace ∧E₂(∧I(dP,dQ)) by dQ. Check the remaining dependencies. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** What is the risk of counting proof nodes without rewriting bound variables? **Expected explanation.** For implication reductions, substitution and alpha-renaming may be required to avoid capture. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **introduction–elimination detours** to **proof optimizer** in the setting **logical soundness must be preserved even if the resulting proof is larger**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a tool removing redundant inference detours from a proof certificate**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 5.2 — Beta reduction and implication proofs

### Exact rule or metatheorem

**Formal content.** Under the Curry–Howard reading, →I acts like lambda abstraction and →E like function application. The beta step (λx.t) u ↦ t[x:=u] corresponds to substituting a proof of an assumption into a discharged subderivation.

### Worked argument with line-by-line reasoning

**Worked demonstration.** Let t=λx.x of type A→A. Applying t to proof u:A yields (λx.x)u, which beta-reduces to u. Type A remains unchanged. If a bound variable of t would capture a free variable of u, alpha-rename first.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **beta reduction and implication proofs** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Performing textual substitution without guarding bound variables or confusing beta reduction with logical equivalence in every arbitrary programming language.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Reduce (λx.λy.x) a b and identify its result. **Solution or proof outline.** First substitute x:=a to obtain λy.a (renaming y if needed), then apply b, yielding a. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Does termination follow for untyped lambda calculus? **Expected explanation.** No. The untyped term (λx.xx)(λx.xx) reduces to itself forever. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **beta reduction and implication proofs** to **proof optimizer** in the setting **logical soundness must be preserved even if the resulting proof is larger**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a tool removing redundant inference detours from a proof certificate**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 5.3 — Cut elimination as a theorem schema

### Exact rule or metatheorem

**Formal content.** Gentzen-style cut elimination states that derivations in a specified sequent calculus can be transformed into cut-free derivations of the same end sequent. The argument measures formula complexity and proof height, with care for structural rules.

### Worked argument with line-by-line reasoning

**Worked demonstration.** If a final cut is on A∧B, one can often push the cut above a last ∧ introduction or elimination, replacing it with cuts on smaller formulas A and B. This is one principal-case intuition; it does not cover every permutation case by itself.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **cut elimination as a theorem schema** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Treating a few propositional examples as a full proof of the Hauptsatz for arbitrary first-order theories.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Explain how the subformula property becomes plausible after removal of cut. **Solution or proof outline.** Without cut, logical rules introduce or decompose formulas related to the end sequent; a formal induction handles all rules in the chosen calculus. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Why may proof size increase dramatically? **Expected explanation.** Cut can share lemmas; elimination expands and duplicates derivations, especially near contraction. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **cut elimination as a theorem schema** to **proof optimizer** in the setting **logical soundness must be preserved even if the resulting proof is larger**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a tool removing redundant inference detours from a proof certificate**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 5.4 — Subformula property and consistency

### Exact rule or metatheorem

**Formal content.** Cut-free proofs in standard analytic calculi satisfy an appropriate subformula property: formulas used are subformulas of goal and premises, accounting for instantiation where needed. This constrains possible proofs.

### Worked argument with line-by-line reasoning

**Worked demonstration.** In a cut-free propositional derivation of ⇒P→P, only P and P→P arise. A derivation of the empty sequent with no axioms cannot start from identity (which has a formula) and cannot be built by analytic rules alone.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **subformula property and consistency** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Declaring a theory consistent simply because its proof search did not find a contradiction.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** State how cut elimination for pure propositional LK supports consistency. **Solution or proof outline.** If the empty sequent had a derivation, it could be made cut free; then subformula analysis rules out an initial sequent or final rule creating it. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Do extra nonlogical axioms preserve this argument automatically? **Expected explanation.** No; special axioms can break analyticity or introduce contradictions. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **subformula property and consistency** to **proof optimizer** in the setting **logical soundness must be preserved even if the resulting proof is larger**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a tool removing redundant inference detours from a proof certificate**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 5.5 — Proof complexity and sharing

### Exact rule or metatheorem

**Formal content.** A short proof with lemmas may become very long if every lemma is expanded. Proof complexity studies size, depth, and simulation relationships of proof systems rather than just validity.

### Worked argument with line-by-line reasoning

**Worked demonstration.** An implication chain A₀→A₁,…,Aₙ₋₁→Aₙ plus A₀ has a linear forward derivation. A naively repeated search may recompute intermediate goals. A proof DAG shares intermediate nodes; a tree duplicates them.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **proof complexity and sharing** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Assuming a proof-normalization procedure improves both elegance and running time in every instance.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Count the distinct intermediate chain atoms for length n=6 and compare DAG reuse with repeated recomputation. **Solution or proof outline.** Seven atoms A₀ through A₆ appear; derivation needs six modus ponens uses with shared intermediate results. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Is an exponentially large cut-free proof logically weaker than the original? **Expected explanation.** No. It may prove the same sequent while being much more expensive to construct or inspect. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **proof complexity and sharing** to **proof optimizer** in the setting **logical soundness must be preserved even if the resulting proof is larger**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a tool removing redundant inference detours from a proof certificate**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Unit 5 capstone — Normalization, cut and consistency

**Design brief.** Build a reviewable specification for **Proof optimizer**. Begin with the formal vocabulary that represents **logical soundness must be preserved even if the resulting proof is larger**. Use at least three of the unit’s five lesson rules in one coherent derivation and one adversarial countercase. Do not use a model screenshot as the sole supporting evidence for a general inference. Report the assumptions that can be checked mechanically and the application assumptions that cannot. The most important quality boundary is **a tool removing redundant inference detours from a proof certificate**.

### Deliverables and answer checkpoints

1. Define the logical calculus, syntax and semantics you are using. This step prevents an unannounced change from classical to intuitionistic rules. 2. Construct a derivation with at least six labeled inference steps or give a checked proof-search tree where every leaf closes by a legitimate initial rule. 3. Provide a negative test case. For a propositional problem include a concrete valuation; for a rule-scope error show the illegal dependency; for a first-order issue give a finite countermodel when one exists. 4. Explain whether the produced artifact is a proof, refutation, illustrative simulation or incomplete search record. 5. Write a short assurance statement describing the remaining outside-the-logic questions.

**A sample critique.** A project report says that **proof optimizer** is correct because a demo displayed a green status and accepted two sample inputs. The critique should reject this as logically inadequate. The green status may show that the interface reacted, but not that the rule system is sound. Replace the vague claim with specific evidence: a formal statement of the goal, a complete proof trace, a verified derivation and an independent check of **a tool removing redundant inference detours from a proof certificate**. The final write-up should make **compare both term typing and the open-assumption context before and after rewriting.** clear.

### Rubric (100 points)

Formal statement and declared logic: 20. Complete rule-by-rule argument: 25. Correct assumption/freshness or structural bookkeeping: 20. Negative tests and countercases: 15. Honest evidence classification: 10. Clarity and reproducibility: 10. An elegant but unchecked demonstration cannot receive full correctness marks. A correct theorem about a visibly mistranslated real-world specification requires an explicit qualification.

### End-of-unit oral examination

**Question 1.** What would count as decisive evidence for the claim in **normalization, cut and consistency**, and what would be merely illustrative?

**Question 2.** Choose the unit’s most important side condition and construct a case that violates it. Explain what changes in the conclusion.

**Question 3.** Explain how you could independently audit **compare both term typing and the open-assumption context before and after rewriting.** without trusting the original proof-search heuristic.
