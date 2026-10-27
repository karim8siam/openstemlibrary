# Unit 4 — Theories, axiom systems and equivalence

**Learning objective.** An axiom set defines a class of structures; understanding its models is different from proving that it has a favorite intended model.

**Running application.** An ontology specification must separate the meanings forced by axioms from unexpressed assumptions.

## Orientation: semantic commitments

The fourth unit uses a theory of an equivalence relation and a theory of groups. Both families allow many different models. The first gives partitions of a universe; the second prescribes algebraic operations. Axioms expressing reflexivity, symmetry and transitivity do not determine the number of equivalence classes, just as group axioms do not force commutativity.

A theory is a collection of constraints, not a single intended interpretation. Mathematical statements about its models must quantify over every structure satisfying those constraints. A property seen in one example may be accidental. To test whether an axiom is missing, construct different models that satisfy the current theory but disagree on the questioned sentence. Conversely, if the sentence is a consequence, make explicit how the axioms force it rather than merely showing it in a favored example. This habit prevents hidden assumptions from entering formal specifications.

A disciplined learning sequence begins with definitions, continues with a reproducible worked interpretation and ends with a search for a legitimate counterexample. You should be able to write a compact formal claim, list its hypotheses and decide whether it asserts satisfaction in one model, entailment by a theory, or a theorem about models. That choice determines the form of appropriate evidence. Keep one running example throughout the unit and modify its domain, relations, parameters or background theory only when you explicitly say so. Comparing these controlled interventions is more instructive than memorizing isolated definitions.

The five lessons proceed from a manageable definition to a mathematically consequential comparison. The first exercise of each lesson reconstructs its example; the second challenges an unjustified strengthening; the third transfers the idea to an applied specification. Each solution hint is guidance, not a substitute for checking the semantics line by line. Write formal answers with explicit witnesses or countermodels wherever possible.


## Lesson 4.1 — Theories and logical consequence

### The statement and its scope

**Core principle.** A theory T is a set of sentences; T⊨φ means every model of T satisfies φ, even when T contains infinitely many sentences.

### A worked semantic construction

From T={∀x(P(x)→Q(x)), P(c)}, one gets Q(c) in every model of T, by instantiation and implication. Analyze this example systematically. Record the language first, then the nonempty domain, the interpretations of constant, function and relation symbols actually in use, and finally the formula under investigation. If no concrete relation is present, interpret the example as an argument about all structures meeting the stated hypotheses and write that change of level explicitly. Each step should say why the mathematical object exists, not merely report the eventual result.

### Counterexample discipline and boundary conditions

**Frequent mistake.** One convenient model satisfying φ does not establish T⊨φ; a single model of T∪{¬φ} refutes entailment. A meaningful counterexample preserves the hypotheses of the claim being tested while breaking only the proposed conclusion. If a supposed counterexample changes the language, silently changes its constants, or violates one of the axioms, it does not disprove the original claim. Conversely, when the claim is a universal assertion about all models, just one legal countermodel is decisive. Keep these two directions separate: finding a witness is enough for an existential conclusion in a fixed structure; proving universal entailment demands attention to every legal structure.

### Proof laboratory: what must be shown

Translate an entailment claim into unsatisfiability of T∪{¬φ}. One rigorous route is to write the target as a precise mathematical judgment and split the argument into sound subgoals. A constructive case should produce the structure, map, formula, or witness promised by the judgment. A negative case should produce a legal countermodel or identify an explicit theorem barring the proposed definition. If an implication is being established, prove the forward direction under named assumptions; for an equivalence, prove both directions independently. Do not let a numerical screen result replace a structural proof when the statement ranges over unbounded domains.

### Transfer to applied reasoning

Policy engines need countermodel searches for purportedly necessary conclusions. The translation must include the mathematical object corresponding to a real-world identifier, the status of absent or unknown information, and a statement of what the formal model leaves unspecified. A theorem guarantees something *given* these premises. It cannot establish that the premises faithfully describe a laboratory, database or institutional policy without external evidence. Keep a record of unverifiable assumptions, because a formal derivation may be completely valid even when its data pipeline is flawed.

### Three exercises and instructor guidance

**Exercise 4.1a — Reconstruct.** Rebuild the worked example in the smallest signature needed. State the domain, all nonlogical interpretations and the central truth or preservation claim. Is the conclusion about a single structure or an entire class? **Guidance:** Begin from: From T={∀x(P(x)→Q(x)), P(c)}, one gets Q(c) in every model of T, by instantiation and implication. Write a sentence or a formula-with-assignment, and justify the conclusion from the relevant recursive semantic clause or theorem. Name every free variable and every parameter.

**Exercise 4.1b — Find a boundary.** Test the tempting stronger claim that the principle automatically survives an arbitrary change of vocabulary, domain or interpretation. Give a specific change that would invalidate the inference or explain which hypotheses prevent such a change. **Guidance:** The primary hazard is: One convenient model satisfying φ does not establish T⊨φ; a single model of T∪{¬φ} refutes entailment. Construct a countermodel if a universal claim is false; if the claim is valid, identify the preserving map or model-theoretic theorem. A failure to find a counterexample by enumeration does not resolve an unbounded question.

**Exercise 4.1c — Apply and audit.** Design an audit record for the application scenario below. Include the signature, an intended model, a checkable formula, and one risk of interpreting the result as an external fact. **Scenario:** Policy engines need countermodel searches for purportedly necessary conclusions. **Guidance:** State the proof obligation as: Translate an entailment claim into unsatisfiability of T∪{¬φ}. Then list the semantic evidence that a verifier can inspect and the external factual assumption that needs separate validation.


## Lesson 4.2 — Equivalence relations and quotient structures

### The statement and its scope

**Core principle.** Reflexivity, symmetry and transitivity can be stated by first-order sentences, and models of these axioms partition their domains.

### A worked semantic construction

The axioms ∀x E(x,x), ∀xy(E(x,y)→E(y,x)), and ∀xyz((E(x,y)∧E(y,z))→E(x,z)) hold for equality modulo 3 on integers. Analyze this example systematically. Record the language first, then the nonempty domain, the interpretations of constant, function and relation symbols actually in use, and finally the formula under investigation. If no concrete relation is present, interpret the example as an argument about all structures meeting the stated hypotheses and write that change of level explicitly. Each step should say why the mathematical object exists, not merely report the eventual result.

### Counterexample discipline and boundary conditions

**Frequent mistake.** These axioms do not force exactly three classes or finite classes; those are additional properties not inferred from equivalence alone. A meaningful counterexample preserves the hypotheses of the claim being tested while breaking only the proposed conclusion. If a supposed counterexample changes the language, silently changes its constants, or violates one of the axioms, it does not disprove the original claim. Conversely, when the claim is a universal assertion about all models, just one legal countermodel is decisive. Keep these two directions separate: finding a witness is enough for an existential conclusion in a fixed structure; proving universal entailment demands attention to every legal structure.

### Proof laboratory: what must be shown

For each proposed conclusion, build both a satisfying and a violating partition when possible. One rigorous route is to write the target as a precise mathematical judgment and split the argument into sound subgoals. A constructive case should produce the structure, map, formula, or witness promised by the judgment. A negative case should produce a legal countermodel or identify an explicit theorem barring the proposed definition. If an implication is being established, prove the forward direction under named assumptions; for an equivalence, prove both directions independently. Do not let a numerical screen result replace a structural proof when the statement ranges over unbounded domains.

### Transfer to applied reasoning

Clustering systems often assume more structure than an equivalence-class specification guarantees. The translation must include the mathematical object corresponding to a real-world identifier, the status of absent or unknown information, and a statement of what the formal model leaves unspecified. A theorem guarantees something *given* these premises. It cannot establish that the premises faithfully describe a laboratory, database or institutional policy without external evidence. Keep a record of unverifiable assumptions, because a formal derivation may be completely valid even when its data pipeline is flawed.

### Three exercises and instructor guidance

**Exercise 4.2a — Reconstruct.** Rebuild the worked example in the smallest signature needed. State the domain, all nonlogical interpretations and the central truth or preservation claim. Is the conclusion about a single structure or an entire class? **Guidance:** Begin from: The axioms ∀x E(x,x), ∀xy(E(x,y)→E(y,x)), and ∀xyz((E(x,y)∧E(y,z))→E(x,z)) hold for equality modulo 3 on integers. Write a sentence or a formula-with-assignment, and justify the conclusion from the relevant recursive semantic clause or theorem. Name every free variable and every parameter.

**Exercise 4.2b — Find a boundary.** Test the tempting stronger claim that the principle automatically survives an arbitrary change of vocabulary, domain or interpretation. Give a specific change that would invalidate the inference or explain which hypotheses prevent such a change. **Guidance:** The primary hazard is: These axioms do not force exactly three classes or finite classes; those are additional properties not inferred from equivalence alone. Construct a countermodel if a universal claim is false; if the claim is valid, identify the preserving map or model-theoretic theorem. A failure to find a counterexample by enumeration does not resolve an unbounded question.

**Exercise 4.2c — Apply and audit.** Design an audit record for the application scenario below. Include the signature, an intended model, a checkable formula, and one risk of interpreting the result as an external fact. **Scenario:** Clustering systems often assume more structure than an equivalence-class specification guarantees. **Guidance:** State the proof obligation as: For each proposed conclusion, build both a satisfying and a violating partition when possible. Then list the semantic evidence that a verifier can inspect and the external factual assumption that needs separate validation.


## Lesson 4.3 — Algebraic structures as models

### The statement and its scope

**Core principle.** The group axioms in the language {·,e,inv} are first-order sentences, while additional axioms characterize rings, fields, or orders.

### A worked semantic construction

The integers under addition with e=0 and inv(n)=−n form a group; positive integers under addition do not supply an additive inverse for each element. Analyze this example systematically. Record the language first, then the nonempty domain, the interpretations of constant, function and relation symbols actually in use, and finally the formula under investigation. If no concrete relation is present, interpret the example as an argument about all structures meeting the stated hypotheses and write that change of level explicitly. Each step should say why the mathematical object exists, not merely report the eventual result.

### Counterexample discipline and boundary conditions

**Frequent mistake.** The axioms of groups permit both finite and infinite groups, and commutativity must be separately added for abelian groups. A meaningful counterexample preserves the hypotheses of the claim being tested while breaking only the proposed conclusion. If a supposed counterexample changes the language, silently changes its constants, or violates one of the axioms, it does not disprove the original claim. Conversely, when the claim is a universal assertion about all models, just one legal countermodel is decisive. Keep these two directions separate: finding a witness is enough for an existential conclusion in a fixed structure; proving universal entailment demands attention to every legal structure.

### Proof laboratory: what must be shown

Write identity, associativity and inverse properties with correct quantifier order. One rigorous route is to write the target as a precise mathematical judgment and split the argument into sound subgoals. A constructive case should produce the structure, map, formula, or witness promised by the judgment. A negative case should produce a legal countermodel or identify an explicit theorem barring the proposed definition. If an implication is being established, prove the forward direction under named assumptions; for an equivalence, prove both directions independently. Do not let a numerical screen result replace a structural proof when the statement ranges over unbounded domains.

### Transfer to applied reasoning

An API contract for algebraic operations can be tested on finite samples but not certified in infinite domains by testing alone. The translation must include the mathematical object corresponding to a real-world identifier, the status of absent or unknown information, and a statement of what the formal model leaves unspecified. A theorem guarantees something *given* these premises. It cannot establish that the premises faithfully describe a laboratory, database or institutional policy without external evidence. Keep a record of unverifiable assumptions, because a formal derivation may be completely valid even when its data pipeline is flawed.

### Three exercises and instructor guidance

**Exercise 4.3a — Reconstruct.** Rebuild the worked example in the smallest signature needed. State the domain, all nonlogical interpretations and the central truth or preservation claim. Is the conclusion about a single structure or an entire class? **Guidance:** Begin from: The integers under addition with e=0 and inv(n)=−n form a group; positive integers under addition do not supply an additive inverse for each element. Write a sentence or a formula-with-assignment, and justify the conclusion from the relevant recursive semantic clause or theorem. Name every free variable and every parameter.

**Exercise 4.3b — Find a boundary.** Test the tempting stronger claim that the principle automatically survives an arbitrary change of vocabulary, domain or interpretation. Give a specific change that would invalidate the inference or explain which hypotheses prevent such a change. **Guidance:** The primary hazard is: The axioms of groups permit both finite and infinite groups, and commutativity must be separately added for abelian groups. Construct a countermodel if a universal claim is false; if the claim is valid, identify the preserving map or model-theoretic theorem. A failure to find a counterexample by enumeration does not resolve an unbounded question.

**Exercise 4.3c — Apply and audit.** Design an audit record for the application scenario below. Include the signature, an intended model, a checkable formula, and one risk of interpreting the result as an external fact. **Scenario:** An API contract for algebraic operations can be tested on finite samples but not certified in infinite domains by testing alone. **Guidance:** State the proof obligation as: Write identity, associativity and inverse properties with correct quantifier order. Then list the semantic evidence that a verifier can inspect and the external factual assumption that needs separate validation.


## Lesson 4.4 — Complete versus incomplete theories

### The statement and its scope

**Core principle.** A theory is complete if, for each sentence in its language, it entails the sentence or its negation; completeness is not the same as Gödel completeness of a proof calculus.

### A worked semantic construction

The bare theory of groups is incomplete: the sentence ∀xy(x·y=y·x) holds in abelian groups but fails in some nonabelian groups. Analyze this example systematically. Record the language first, then the nonempty domain, the interpretations of constant, function and relation symbols actually in use, and finally the formula under investigation. If no concrete relation is present, interpret the example as an argument about all structures meeting the stated hypotheses and write that change of level explicitly. Each step should say why the mathematical object exists, not merely report the eventual result.

### Counterexample discipline and boundary conditions

**Frequent mistake.** A complete theory may have nonisomorphic models; sentence-level agreement does not imply structural identity. A meaningful counterexample preserves the hypotheses of the claim being tested while breaking only the proposed conclusion. If a supposed counterexample changes the language, silently changes its constants, or violates one of the axioms, it does not disprove the original claim. Conversely, when the claim is a universal assertion about all models, just one legal countermodel is decisive. Keep these two directions separate: finding a witness is enough for an existential conclusion in a fixed structure; proving universal entailment demands attention to every legal structure.

### Proof laboratory: what must be shown

Exhibit two models of the same axioms disagreeing on one sentence to prove incompleteness. One rigorous route is to write the target as a precise mathematical judgment and split the argument into sound subgoals. A constructive case should produce the structure, map, formula, or witness promised by the judgment. A negative case should produce a legal countermodel or identify an explicit theorem barring the proposed definition. If an implication is being established, prove the forward direction under named assumptions; for an equivalence, prove both directions independently. Do not let a numerical screen result replace a structural proof when the statement ranges over unbounded domains.

### Transfer to applied reasoning

Specification coverage should distinguish undecided requirements from inconsistent requirements. The translation must include the mathematical object corresponding to a real-world identifier, the status of absent or unknown information, and a statement of what the formal model leaves unspecified. A theorem guarantees something *given* these premises. It cannot establish that the premises faithfully describe a laboratory, database or institutional policy without external evidence. Keep a record of unverifiable assumptions, because a formal derivation may be completely valid even when its data pipeline is flawed.

### Three exercises and instructor guidance

**Exercise 4.4a — Reconstruct.** Rebuild the worked example in the smallest signature needed. State the domain, all nonlogical interpretations and the central truth or preservation claim. Is the conclusion about a single structure or an entire class? **Guidance:** Begin from: The bare theory of groups is incomplete: the sentence ∀xy(x·y=y·x) holds in abelian groups but fails in some nonabelian groups. Write a sentence or a formula-with-assignment, and justify the conclusion from the relevant recursive semantic clause or theorem. Name every free variable and every parameter.

**Exercise 4.4b — Find a boundary.** Test the tempting stronger claim that the principle automatically survives an arbitrary change of vocabulary, domain or interpretation. Give a specific change that would invalidate the inference or explain which hypotheses prevent such a change. **Guidance:** The primary hazard is: A complete theory may have nonisomorphic models; sentence-level agreement does not imply structural identity. Construct a countermodel if a universal claim is false; if the claim is valid, identify the preserving map or model-theoretic theorem. A failure to find a counterexample by enumeration does not resolve an unbounded question.

**Exercise 4.4c — Apply and audit.** Design an audit record for the application scenario below. Include the signature, an intended model, a checkable formula, and one risk of interpreting the result as an external fact. **Scenario:** Specification coverage should distinguish undecided requirements from inconsistent requirements. **Guidance:** State the proof obligation as: Exhibit two models of the same axioms disagreeing on one sentence to prove incompleteness. Then list the semantic evidence that a verifier can inspect and the external factual assumption that needs separate validation.


## Lesson 4.5 — Elementary equivalence and diagrams

### The statement and its scope

**Core principle.** M≡N means the structures satisfy exactly the same sentences; elementary diagrams additionally name domain elements with constants.

### A worked semantic construction

Any two dense linear orders without endpoints that are countable are isomorphic; Q and R as pure linear orders are elementarily equivalent but not isomorphic, as their cardinalities differ. Analyze this example systematically. Record the language first, then the nonempty domain, the interpretations of constant, function and relation symbols actually in use, and finally the formula under investigation. If no concrete relation is present, interpret the example as an argument about all structures meeting the stated hypotheses and write that change of level explicitly. Each step should say why the mathematical object exists, not merely report the eventual result.

### Counterexample discipline and boundary conditions

**Frequent mistake.** The real-order example is about the pure language {<}; adding a predicate or arithmetic functions can change the resulting theory. A meaningful counterexample preserves the hypotheses of the claim being tested while breaking only the proposed conclusion. If a supposed counterexample changes the language, silently changes its constants, or violates one of the axioms, it does not disprove the original claim. Conversely, when the claim is a universal assertion about all models, just one legal countermodel is decisive. Keep these two directions separate: finding a witness is enough for an existential conclusion in a fixed structure; proving universal entailment demands attention to every legal structure.

### Proof laboratory: what must be shown

Fix the language and explain whether the comparison is isomorphism or only elementary equivalence. One rigorous route is to write the target as a precise mathematical judgment and split the argument into sound subgoals. A constructive case should produce the structure, map, formula, or witness promised by the judgment. A negative case should produce a legal countermodel or identify an explicit theorem barring the proposed definition. If an implication is being established, prove the forward direction under named assumptions; for an equivalence, prove both directions independently. Do not let a numerical screen result replace a structural proof when the statement ranges over unbounded domains.

### Transfer to applied reasoning

Data snapshots may agree on every test from a restricted language while having different sizes. The translation must include the mathematical object corresponding to a real-world identifier, the status of absent or unknown information, and a statement of what the formal model leaves unspecified. A theorem guarantees something *given* these premises. It cannot establish that the premises faithfully describe a laboratory, database or institutional policy without external evidence. Keep a record of unverifiable assumptions, because a formal derivation may be completely valid even when its data pipeline is flawed.

### Three exercises and instructor guidance

**Exercise 4.5a — Reconstruct.** Rebuild the worked example in the smallest signature needed. State the domain, all nonlogical interpretations and the central truth or preservation claim. Is the conclusion about a single structure or an entire class? **Guidance:** Begin from: Any two dense linear orders without endpoints that are countable are isomorphic; Q and R as pure linear orders are elementarily equivalent but not isomorphic, as their cardinalities differ. Write a sentence or a formula-with-assignment, and justify the conclusion from the relevant recursive semantic clause or theorem. Name every free variable and every parameter.

**Exercise 4.5b — Find a boundary.** Test the tempting stronger claim that the principle automatically survives an arbitrary change of vocabulary, domain or interpretation. Give a specific change that would invalidate the inference or explain which hypotheses prevent such a change. **Guidance:** The primary hazard is: The real-order example is about the pure language {<}; adding a predicate or arithmetic functions can change the resulting theory. Construct a countermodel if a universal claim is false; if the claim is valid, identify the preserving map or model-theoretic theorem. A failure to find a counterexample by enumeration does not resolve an unbounded question.

**Exercise 4.5c — Apply and audit.** Design an audit record for the application scenario below. Include the signature, an intended model, a checkable formula, and one risk of interpreting the result as an external fact. **Scenario:** Data snapshots may agree on every test from a restricted language while having different sizes. **Guidance:** State the proof obligation as: Fix the language and explain whether the comparison is isomorphism or only elementary equivalence. Then list the semantic evidence that a verifier can inspect and the external factual assumption that needs separate validation.


## Unit 4 capstone — Build, vary and defend one model

**Part A: specify the vocabulary.** From this unit's running application, choose one nonempty domain and a minimal signature. Interpret each constant, function and relation explicitly. Write at least two sentences: one intended to hold and one intended to fail. If the unit focuses on a metatheorem rather than one finite example, explain why the running finite structure is illustrative rather than the theorem's proof.

**Part B: produce a controlled comparison.** Construct a second structure, a second theory or a modified formula connected with one of this unit's five lessons. Change exactly one semantically significant feature and compute what happened to the truth conditions. If the proposed preservation theorem is invalid, supply a legal counterexample. If it is valid, outline the inductive or theorem-based reason that every relevant formula is preserved.

**Part C: critique the claim.** A hypothetical reviewer states that the exercise establishes the result 'for all structures of any size'. Explain whether that is justified, using this unit's central distinction: An axiom set defines a class of structures; understanding its models is different from proving that it has a favorite intended model. State the strongest conclusion that the evidence supports. Identify one mathematical assumption and one practical assumption that would need separate checking before applying the result to the real-world scenario.

**Suggested response framework.** Include the written signature; a complete interpretation table; formulas with all quantifiers and parentheses; one explicit witness or countermodel; a short derivation of the outcome; and a paragraph describing the limitations. Students working collaboratively should swap their artifacts and test whether another reader can reproduce the same evaluation without informal clarification.

## Unit 4 mastery checklist

- I can restate the five definitions of this unit accurately, with all needed hypotheses.
- I can build a legitimate small example and evaluate its key formulas.
- I can name at least one tempting invalid strengthening and diagnose it.
- I can distinguish first-order truth from real-world empirical truth.
- I can identify which claims require proof beyond a finite simulation.
