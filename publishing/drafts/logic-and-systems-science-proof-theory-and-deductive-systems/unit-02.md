# Unit 2 — Propositional natural deduction

**Purpose.** Introduction and elimination rules govern the formation and use of connectives in proof trees.

**Running application.** A specification team needs auditable rules for combining and discharging assumptions.

**Dangerous assumption.** A discharged assumption is not available outside its derivation branch.

## Research orientation and operational meaning

Natural deduction is deliberately local: how we introduce a connective mirrors what evidence is needed for its truth, while elimination reveals how to use such evidence. The strongest beginner habit is to plan an argument backwards by the goal connective, then check the resulting steps forwards. An implication goal suggests temporarily assuming its antecedent; a conjunction goal creates two subgoals; a disjunction premise suggests cases.

Branch diagrams reveal why discharge bookkeeping matters. A proof from an assumption A may be reused in another scope only as a derived theorem if A was discharged. With disjunction elimination, the two branches can each assume a different fact, yet the shared conclusion survives when the branches close. The entire derivation is sound precisely because every valuation satisfying A∨B satisfies at least one case.

The continuing case in this unit is **University admission-policy rules**, specifically **the policy may be vague in natural language; formal soundness follows only after the formalization has been reviewed**. The main complication is **an academic policy written as conditionals, conjunctions and exceptions**. A formal report should record what is defined inside the logic and what requires a separate observation or human specification. The expected deliverable is: **Prove the abstract policy rule and separately flag interpretation questions.** This requirement makes the case genuinely useful rather than merely decorative; the proof language solves the implication problem only after the relevant facts have been expressed as formulas.

## Working with derivations rather than slogans

Introduction rules act as goal constructors. If the goal is an implication, create a temporary antecedent assumption; if it is a conjunction, solve both components; if it is a disjunction, choose one side when constructive evidence supports it. Elimination rules act on resources already available in the context. This discipline is an effective alternative to undirected symbol manipulation.

Draw brackets around subderivations and label each assumption. A temporary assumption may be used repeatedly inside its box, but once discharged it cannot be cited outside as a free premise. For disjunction elimination, the branch assumptions differ while the derived target must agree. This bookkeeping is part of the proof’s meaning.

A deliberately minimal audit record has five fields: formal premises, goal formula, inference-rule schema, concrete substitution into that schema, and remaining open obligations. The audit record should not confuse a witness term with an interpretation, a goal with an assumption, or a line of output with a theorem. When a rule has side conditions, record them just as carefully as the displayed conclusion. In a system that discharges assumptions, the scope of the discharge belongs to the proof object.

When the answer to a mathematical question is negative, supply evidence of the right kind. For finite propositional entailment, one satisfying valuation for the premises that falsifies the goal is decisive. For a claimed formula in a first-order setting, a legitimate structure and assignment can serve as a countermodel. For search failure on an undecidable class, however, no verdict follows. This evidence hierarchy will recur through every chapter, because it is central to responsible research and publication.

## Lesson 2.1 — Conjunction rules

### Exact rule or metatheorem

**Formal content.** The natural deduction rules ∧I combine independent derivations of A and B into A∧B. Rules ∧E₁ and ∧E₂ extract either component. They do not add new assumptions.

### Worked argument with line-by-line reasoning

**Worked demonstration.** Given Γ ⊢ P and Γ ⊢ Q, use ∧I to derive Γ ⊢ P∧Q. Conversely, from P∧Q infer Q by ∧E₂ and P by ∧E₁. Combining these yields a constructive derivation of (P∧Q)→(Q∧P).

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **conjunction rules** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Assuming one conjunct can be inferred from either side of a disjunction.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Write a natural deduction proof of (P∧Q)→(P∧P). **Solution or proof outline.** Assume P∧Q; extract P twice; introduce P∧P; discharge the assumption. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Does ∧I prove A∧B from Γ⊢A and unrelated Δ⊢B with no bookkeeping? **Expected explanation.** Only from the union of dependencies Γ∪Δ, not automatically from Γ alone. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **conjunction rules** to **university admission-policy rules** in the setting **the policy may be vague in natural language; formal soundness follows only after the formalization has been reviewed**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **an academic policy written as conditionals, conjunctions and exceptions**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 2.2 — Implication introduction and elimination

### Exact rule or metatheorem

**Formal content.** Implication elimination, →E, uses A and A→B to obtain B. Implication introduction, →I, discharges a marked temporary assumption A after deriving B from it.

### Worked argument with line-by-line reasoning

**Worked demonstration.** Derive P→(Q→P): assume P, assume Q, cite P, discharge Q to Q→P, then discharge P. In the outer proof the inner Q occurrence is not an open dependency; P is discharged only at the final step.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **implication introduction and elimination** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Applying →I when the conclusion B still depends on an assumption that has accidentally been omitted.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Derive (P→Q)→((Q→R)→(P→R)). **Solution or proof outline.** Assume P→Q, then Q→R, then P. Derive Q and R by →E; discharge P, Q→R, and P→Q in reverse order. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Can Q follow from only P→Q? **Expected explanation.** No. An implication does not assert its antecedent. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **implication introduction and elimination** to **university admission-policy rules** in the setting **the policy may be vague in natural language; formal soundness follows only after the formalization has been reviewed**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **an academic policy written as conditionals, conjunctions and exceptions**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 2.3 — Disjunction introductions

### Exact rule or metatheorem

**Formal content.** From A obtain A∨B by ∨I₁; from B obtain A∨B by ∨I₂. The unspecified other disjunct need not have a proof. Elimination instead requires reasoning by cases.

### Worked argument with line-by-line reasoning

**Worked demonstration.** With premise P, infer P∨Q by ∨I₁. This says at least one disjunct holds. It does not entitle us to Q; for P=true, Q=false the original premise and disjunction are both true.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **disjunction introductions** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Treating ∨I as a license to infer the missing disjunct.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** From P∧Q derive P∨R, naming each rule. **Solution or proof outline.** First use ∧E₁ to get P; then ∨I₁ to derive P∨R. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Can ∨I prove R from P∨R? **Expected explanation.** Not without additional information; set P=true, R=false. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **disjunction introductions** to **university admission-policy rules** in the setting **the policy may be vague in natural language; formal soundness follows only after the formalization has been reviewed**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **an academic policy written as conditionals, conjunctions and exceptions**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 2.4 — Disjunction elimination

### Exact rule or metatheorem

**Formal content.** A∨B, a derivation of C from temporary A, and a derivation of C from temporary B jointly justify C by ∨E. Both branches must establish exactly the intended conclusion.

### Worked argument with line-by-line reasoning

**Worked demonstration.** Prove (P∨Q)→(Q∨P). Assume P∨Q. In the P branch infer Q∨P by ∨I₂. In the Q branch infer Q∨P by ∨I₁. Apply ∨E and discharge P∨Q.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **disjunction elimination** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Proving a goal in only one branch, or using a discharged branch assumption outside the case analysis.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Prove (P∨Q)→((P→R)→((Q→R)→R)). **Solution or proof outline.** Assume all three premises; in P branch use P→R, in Q branch use Q→R; apply ∨E and discharge assumptions. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** What happens if the Q branch proves S instead of R? **Expected explanation.** ∨E does not apply because both branches need a common conclusion. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **disjunction elimination** to **university admission-policy rules** in the setting **the policy may be vague in natural language; formal soundness follows only after the formalization has been reviewed**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **an academic policy written as conditionals, conjunctions and exceptions**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 2.5 — Negation, absurdity, and classical strength

### Exact rule or metatheorem

**Formal content.** In intuitionistic natural deduction, ¬A abbreviates A→⊥; from A and ¬A infer ⊥, and from ⊥ infer any B by ex falso. Classical reductio or double-negation elimination adds stronger steps.

### Worked argument with line-by-line reasoning

**Worked demonstration.** From P∧¬P infer ⊥ by extracting both P and P→⊥, then →E. From ⊥ obtain Q by ⊥E. This proof is intuitionistically valid. In contrast deriving P from ¬¬P generally needs classical principles.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **negation, absurdity, and classical strength** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Calling every use of contradiction classical; constructive negation introduction is not automatically classical reductio.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** From P→Q and P→¬Q derive ¬P without excluded middle. **Solution or proof outline.** Assume P; obtain Q and ¬Q, hence ⊥; discharge P to obtain P→⊥. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Why is ¬¬P→P not generally derivable intuitionistically? **Expected explanation.** A two-world Kripke countermodel suffices: P becomes true in a future world but is not forced at the root. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **negation, absurdity, and classical strength** to **university admission-policy rules** in the setting **the policy may be vague in natural language; formal soundness follows only after the formalization has been reviewed**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **an academic policy written as conditionals, conjunctions and exceptions**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Unit 2 capstone — Propositional natural deduction

**Design brief.** Build a reviewable specification for **University admission-policy rules**. Begin with the formal vocabulary that represents **the policy may be vague in natural language; formal soundness follows only after the formalization has been reviewed**. Use at least three of the unit’s five lesson rules in one coherent derivation and one adversarial countercase. Do not use a model screenshot as the sole supporting evidence for a general inference. Report the assumptions that can be checked mechanically and the application assumptions that cannot. The most important quality boundary is **an academic policy written as conditionals, conjunctions and exceptions**.

### Deliverables and answer checkpoints

1. Define the logical calculus, syntax and semantics you are using. This step prevents an unannounced change from classical to intuitionistic rules. 2. Construct a derivation with at least six labeled inference steps or give a checked proof-search tree where every leaf closes by a legitimate initial rule. 3. Provide a negative test case. For a propositional problem include a concrete valuation; for a rule-scope error show the illegal dependency; for a first-order issue give a finite countermodel when one exists. 4. Explain whether the produced artifact is a proof, refutation, illustrative simulation or incomplete search record. 5. Write a short assurance statement describing the remaining outside-the-logic questions.

**A sample critique.** A project report says that **university admission-policy rules** is correct because a demo displayed a green status and accepted two sample inputs. The critique should reject this as logically inadequate. The green status may show that the interface reacted, but not that the rule system is sound. Replace the vague claim with specific evidence: a formal statement of the goal, a complete proof trace, a verified derivation and an independent check of **an academic policy written as conditionals, conjunctions and exceptions**. The final write-up should make **prove the abstract policy rule and separately flag interpretation questions.** clear.

### Rubric (100 points)

Formal statement and declared logic: 20. Complete rule-by-rule argument: 25. Correct assumption/freshness or structural bookkeeping: 20. Negative tests and countercases: 15. Honest evidence classification: 10. Clarity and reproducibility: 10. An elegant but unchecked demonstration cannot receive full correctness marks. A correct theorem about a visibly mistranslated real-world specification requires an explicit qualification.

### End-of-unit oral examination

**Question 1.** What would count as decisive evidence for the claim in **propositional natural deduction**, and what would be merely illustrative?

**Question 2.** Choose the unit’s most important side condition and construct a case that violates it. Explain what changes in the conclusion.

**Question 3.** Explain how you could independently audit **prove the abstract policy rule and separately flag interpretation questions.** without trusting the original proof-search heuristic.
