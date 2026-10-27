# Unit 1 — Structures and semantic evaluation

**Learning objective.** Every interpretation fixes a domain, vocabulary, and a recursive truth definition.

**Running application.** A library knowledge graph distinguishes claims about readers from syntactic strings representing those claims.

## Orientation: semantic commitments

The first unit's running model uses the directed relation E over {0,1,2}. Its value lies in being small enough to exhaustively enumerate. For example, if E={(0,1),(1,2)}, the choice of source vertex is essential to the truth of an edge statement. A sentence quantifying over all vertices sees the isolated outgoing behavior of 2 even when a casual diagram reader notices only the two connected edges.

The semantic reading of this topic starts by asking what the nonlogical symbols denote. A statement has no unconditional truth value before the domain and the relations or functions have been specified. In a mathematical proof, mark symbols belonging to the language separately from the variables in a meta-level explanation. Quoted formula text and an element of the domain are objects of different kinds. This distinction is easy to overlook when elements happen to have convenient written names. It becomes unavoidable when two isomorphic structures use entirely different notations for their domains.

A disciplined learning sequence begins with definitions, continues with a reproducible worked interpretation and ends with a search for a legitimate counterexample. You should be able to write a compact formal claim, list its hypotheses and decide whether it asserts satisfaction in one model, entailment by a theory, or a theorem about models. That choice determines the form of appropriate evidence. Keep one running example throughout the unit and modify its domain, relations, parameters or background theory only when you explicitly say so. Comparing these controlled interventions is more instructive than memorizing isolated definitions.

The five lessons proceed from a manageable definition to a mathematically consequential comparison. The first exercise of each lesson reconstructs its example; the second challenges an unjustified strengthening; the third transfers the idea to an applied specification. Each solution hint is guidance, not a substitute for checking the semantics line by line. Write formal answers with explicit witnesses or countermodels wherever possible.


## Lesson 1.1 — Signatures, arities, and equality

### The statement and its scope

**Core principle.** A first-order signature specifies relation, function, and constant symbols, each with a fixed arity. Logical equality is interpreted as actual identity.

### A worked semantic construction

For L={E binary, c constant}, a structure has a nonempty domain D, a subset E of D×D, and a chosen element c in D. The symbol E alone does not declare that it is symmetric. Analyze this example systematically. Record the language first, then the nonempty domain, the interpretations of constant, function and relation symbols actually in use, and finally the formula under investigation. If no concrete relation is present, interpret the example as an argument about all structures meeting the stated hypotheses and write that change of level explicitly. Each step should say why the mathematical object exists, not merely report the eventual result.

### Counterexample discipline and boundary conditions

**Frequent mistake.** Do not confuse a typed, many-sorted language with ordinary one-sorted first-order logic: sorts require explicit semantics or a careful translation. A meaningful counterexample preserves the hypotheses of the claim being tested while breaking only the proposed conclusion. If a supposed counterexample changes the language, silently changes its constants, or violates one of the axioms, it does not disprove the original claim. Conversely, when the claim is a universal assertion about all models, just one legal countermodel is decisive. Keep these two directions separate: finding a witness is enough for an existential conclusion in a fixed structure; proving universal entailment demands attention to every legal structure.

### Proof laboratory: what must be shown

Specify L before claiming a sentence has a unique interpretation. One rigorous route is to write the target as a precise mathematical judgment and split the argument into sound subgoals. A constructive case should produce the structure, map, formula, or witness promised by the judgment. A negative case should produce a legal countermodel or identify an explicit theorem barring the proposed definition. If an implication is being established, prove the forward direction under named assumptions; for an equivalence, prove both directions independently. Do not let a numerical screen result replace a structural proof when the statement ranges over unbounded domains.

### Transfer to applied reasoning

Knowledge-graph schemas should declare the allowed arities before accepting facts. The translation must include the mathematical object corresponding to a real-world identifier, the status of absent or unknown information, and a statement of what the formal model leaves unspecified. A theorem guarantees something *given* these premises. It cannot establish that the premises faithfully describe a laboratory, database or institutional policy without external evidence. Keep a record of unverifiable assumptions, because a formal derivation may be completely valid even when its data pipeline is flawed.

### Three exercises and instructor guidance

**Exercise 1.1a — Reconstruct.** Rebuild the worked example in the smallest signature needed. State the domain, all nonlogical interpretations and the central truth or preservation claim. Is the conclusion about a single structure or an entire class? **Guidance:** Begin from: For L={E binary, c constant}, a structure has a nonempty domain D, a subset E of D×D, and a chosen element c in D. The symbol E alone does not declare that it is symmetric. Write a sentence or a formula-with-assignment, and justify the conclusion from the relevant recursive semantic clause or theorem. Name every free variable and every parameter.

**Exercise 1.1b — Find a boundary.** Test the tempting stronger claim that the principle automatically survives an arbitrary change of vocabulary, domain or interpretation. Give a specific change that would invalidate the inference or explain which hypotheses prevent such a change. **Guidance:** The primary hazard is: Do not confuse a typed, many-sorted language with ordinary one-sorted first-order logic: sorts require explicit semantics or a careful translation. Construct a countermodel if a universal claim is false; if the claim is valid, identify the preserving map or model-theoretic theorem. A failure to find a counterexample by enumeration does not resolve an unbounded question.

**Exercise 1.1c — Apply and audit.** Design an audit record for the application scenario below. Include the signature, an intended model, a checkable formula, and one risk of interpreting the result as an external fact. **Scenario:** Knowledge-graph schemas should declare the allowed arities before accepting facts. **Guidance:** State the proof obligation as: Specify L before claiming a sentence has a unique interpretation. Then list the semantic evidence that a verifier can inspect and the external factual assumption that needs separate validation.


## Lesson 1.2 — Domains and interpretations

### The statement and its scope

**Core principle.** An L-structure M interprets each constant as an element, function symbol as a total operation, and relation symbol as a set of tuples.

### A worked semantic construction

Take D={a,b,c}, cᴹ=a and Eᴹ={(a,b),(b,c)}. Then E(c,b) is true after b is named or assigned, but E(b,a) is false; E is directed. Analyze this example systematically. Record the language first, then the nonempty domain, the interpretations of constant, function and relation symbols actually in use, and finally the formula under investigation. If no concrete relation is present, interpret the example as an argument about all structures meeting the stated hypotheses and write that change of level explicitly. Each step should say why the mathematical object exists, not merely report the eventual result.

### Counterexample discipline and boundary conditions

**Frequent mistake.** The name of a domain element is not necessarily a constant symbol of the formal language, and a function cannot simply be left undefined in a classical structure. A meaningful counterexample preserves the hypotheses of the claim being tested while breaking only the proposed conclusion. If a supposed counterexample changes the language, silently changes its constants, or violates one of the axioms, it does not disprove the original claim. Conversely, when the claim is a universal assertion about all models, just one legal countermodel is decisive. Keep these two directions separate: finding a witness is enough for an existential conclusion in a fixed structure; proving universal entailment demands attention to every legal structure.

### Proof laboratory: what must be shown

Write every interpretation as a set, tuple or mapping before evaluating formulas. One rigorous route is to write the target as a precise mathematical judgment and split the argument into sound subgoals. A constructive case should produce the structure, map, formula, or witness promised by the judgment. A negative case should produce a legal countermodel or identify an explicit theorem barring the proposed definition. If an implication is being established, prove the forward direction under named assumptions; for an equivalence, prove both directions independently. Do not let a numerical screen result replace a structural proof when the statement ranges over unbounded domains.

### Transfer to applied reasoning

Database tables can stand for finite relations, with explicit policy for missing values. The translation must include the mathematical object corresponding to a real-world identifier, the status of absent or unknown information, and a statement of what the formal model leaves unspecified. A theorem guarantees something *given* these premises. It cannot establish that the premises faithfully describe a laboratory, database or institutional policy without external evidence. Keep a record of unverifiable assumptions, because a formal derivation may be completely valid even when its data pipeline is flawed.

### Three exercises and instructor guidance

**Exercise 1.2a — Reconstruct.** Rebuild the worked example in the smallest signature needed. State the domain, all nonlogical interpretations and the central truth or preservation claim. Is the conclusion about a single structure or an entire class? **Guidance:** Begin from: Take D={a,b,c}, cᴹ=a and Eᴹ={(a,b),(b,c)}. Then E(c,b) is true after b is named or assigned, but E(b,a) is false; E is directed. Write a sentence or a formula-with-assignment, and justify the conclusion from the relevant recursive semantic clause or theorem. Name every free variable and every parameter.

**Exercise 1.2b — Find a boundary.** Test the tempting stronger claim that the principle automatically survives an arbitrary change of vocabulary, domain or interpretation. Give a specific change that would invalidate the inference or explain which hypotheses prevent such a change. **Guidance:** The primary hazard is: The name of a domain element is not necessarily a constant symbol of the formal language, and a function cannot simply be left undefined in a classical structure. Construct a countermodel if a universal claim is false; if the claim is valid, identify the preserving map or model-theoretic theorem. A failure to find a counterexample by enumeration does not resolve an unbounded question.

**Exercise 1.2c — Apply and audit.** Design an audit record for the application scenario below. Include the signature, an intended model, a checkable formula, and one risk of interpreting the result as an external fact. **Scenario:** Database tables can stand for finite relations, with explicit policy for missing values. **Guidance:** State the proof obligation as: Write every interpretation as a set, tuple or mapping before evaluating formulas. Then list the semantic evidence that a verifier can inspect and the external factual assumption that needs separate validation.


## Lesson 1.3 — Term evaluation and assignments

### The statement and its scope

**Core principle.** A variable assignment s maps variables to domain elements; term evaluation proceeds recursively through function symbols.

### A worked semantic construction

For D=integers, fᴹ(n)=n+1, cᴹ=0 and s(x)=2, the term f(f(x)) denotes 4 and f(c) denotes 1. Its value depends on the structure and assignment. Analyze this example systematically. Record the language first, then the nonempty domain, the interpretations of constant, function and relation symbols actually in use, and finally the formula under investigation. If no concrete relation is present, interpret the example as an argument about all structures meeting the stated hypotheses and write that change of level explicitly. Each step should say why the mathematical object exists, not merely report the eventual result.

### Counterexample discipline and boundary conditions

**Frequent mistake.** A free variable does not have a truth value by itself, and substitution can capture variables unless bound-variable renaming is respected. A meaningful counterexample preserves the hypotheses of the claim being tested while breaking only the proposed conclusion. If a supposed counterexample changes the language, silently changes its constants, or violates one of the axioms, it does not disprove the original claim. Conversely, when the claim is a universal assertion about all models, just one legal countermodel is decisive. Keep these two directions separate: finding a witness is enough for an existential conclusion in a fixed structure; proving universal entailment demands attention to every legal structure.

### Proof laboratory: what must be shown

Compute denotations from inside out, recording the assignment used at each step. One rigorous route is to write the target as a precise mathematical judgment and split the argument into sound subgoals. A constructive case should produce the structure, map, formula, or witness promised by the judgment. A negative case should produce a legal countermodel or identify an explicit theorem barring the proposed definition. If an implication is being established, prove the forward direction under named assumptions; for an equivalence, prove both directions independently. Do not let a numerical screen result replace a structural proof when the statement ranges over unbounded domains.

### Transfer to applied reasoning

A query engine needs a variable environment separate from the stored interpretation. The translation must include the mathematical object corresponding to a real-world identifier, the status of absent or unknown information, and a statement of what the formal model leaves unspecified. A theorem guarantees something *given* these premises. It cannot establish that the premises faithfully describe a laboratory, database or institutional policy without external evidence. Keep a record of unverifiable assumptions, because a formal derivation may be completely valid even when its data pipeline is flawed.

### Three exercises and instructor guidance

**Exercise 1.3a — Reconstruct.** Rebuild the worked example in the smallest signature needed. State the domain, all nonlogical interpretations and the central truth or preservation claim. Is the conclusion about a single structure or an entire class? **Guidance:** Begin from: For D=integers, fᴹ(n)=n+1, cᴹ=0 and s(x)=2, the term f(f(x)) denotes 4 and f(c) denotes 1. Its value depends on the structure and assignment. Write a sentence or a formula-with-assignment, and justify the conclusion from the relevant recursive semantic clause or theorem. Name every free variable and every parameter.

**Exercise 1.3b — Find a boundary.** Test the tempting stronger claim that the principle automatically survives an arbitrary change of vocabulary, domain or interpretation. Give a specific change that would invalidate the inference or explain which hypotheses prevent such a change. **Guidance:** The primary hazard is: A free variable does not have a truth value by itself, and substitution can capture variables unless bound-variable renaming is respected. Construct a countermodel if a universal claim is false; if the claim is valid, identify the preserving map or model-theoretic theorem. A failure to find a counterexample by enumeration does not resolve an unbounded question.

**Exercise 1.3c — Apply and audit.** Design an audit record for the application scenario below. Include the signature, an intended model, a checkable formula, and one risk of interpreting the result as an external fact. **Scenario:** A query engine needs a variable environment separate from the stored interpretation. **Guidance:** State the proof obligation as: Compute denotations from inside out, recording the assignment used at each step. Then list the semantic evidence that a verifier can inspect and the external factual assumption that needs separate validation.


## Lesson 1.4 — Tarski truth clauses

### The statement and its scope

**Core principle.** Atomic truths are determined by the interpretation, Boolean connectives by truth conditions, and quantifiers by varying assignments over the whole domain.

### A worked semantic construction

In D={0,1,2} with Pᴹ={0,2}, M satisfies ∃x P(x) but not ∀x P(x). A witness may be 0; the counterexample to the universal sentence is 1. Analyze this example systematically. Record the language first, then the nonempty domain, the interpretations of constant, function and relation symbols actually in use, and finally the formula under investigation. If no concrete relation is present, interpret the example as an argument about all structures meeting the stated hypotheses and write that change of level explicitly. Each step should say why the mathematical object exists, not merely report the eventual result.

### Counterexample discipline and boundary conditions

**Frequent mistake.** Enumerating domain elements proves a quantifier only for the specified finite structure, not for every possible structure. A meaningful counterexample preserves the hypotheses of the claim being tested while breaking only the proposed conclusion. If a supposed counterexample changes the language, silently changes its constants, or violates one of the axioms, it does not disprove the original claim. Conversely, when the claim is a universal assertion about all models, just one legal countermodel is decisive. Keep these two directions separate: finding a witness is enough for an existential conclusion in a fixed structure; proving universal entailment demands attention to every legal structure.

### Proof laboratory: what must be shown

Apply semantic clauses in syntax-tree order and preserve the scope of each quantifier. One rigorous route is to write the target as a precise mathematical judgment and split the argument into sound subgoals. A constructive case should produce the structure, map, formula, or witness promised by the judgment. A negative case should produce a legal countermodel or identify an explicit theorem barring the proposed definition. If an implication is being established, prove the forward direction under named assumptions; for an equivalence, prove both directions independently. Do not let a numerical screen result replace a structural proof when the statement ranges over unbounded domains.

### Transfer to applied reasoning

Rule-based systems should log counterexamples rather than only returning a red status light. The translation must include the mathematical object corresponding to a real-world identifier, the status of absent or unknown information, and a statement of what the formal model leaves unspecified. A theorem guarantees something *given* these premises. It cannot establish that the premises faithfully describe a laboratory, database or institutional policy without external evidence. Keep a record of unverifiable assumptions, because a formal derivation may be completely valid even when its data pipeline is flawed.

### Three exercises and instructor guidance

**Exercise 1.4a — Reconstruct.** Rebuild the worked example in the smallest signature needed. State the domain, all nonlogical interpretations and the central truth or preservation claim. Is the conclusion about a single structure or an entire class? **Guidance:** Begin from: In D={0,1,2} with Pᴹ={0,2}, M satisfies ∃x P(x) but not ∀x P(x). A witness may be 0; the counterexample to the universal sentence is 1. Write a sentence or a formula-with-assignment, and justify the conclusion from the relevant recursive semantic clause or theorem. Name every free variable and every parameter.

**Exercise 1.4b — Find a boundary.** Test the tempting stronger claim that the principle automatically survives an arbitrary change of vocabulary, domain or interpretation. Give a specific change that would invalidate the inference or explain which hypotheses prevent such a change. **Guidance:** The primary hazard is: Enumerating domain elements proves a quantifier only for the specified finite structure, not for every possible structure. Construct a countermodel if a universal claim is false; if the claim is valid, identify the preserving map or model-theoretic theorem. A failure to find a counterexample by enumeration does not resolve an unbounded question.

**Exercise 1.4c — Apply and audit.** Design an audit record for the application scenario below. Include the signature, an intended model, a checkable formula, and one risk of interpreting the result as an external fact. **Scenario:** Rule-based systems should log counterexamples rather than only returning a red status light. **Guidance:** State the proof obligation as: Apply semantic clauses in syntax-tree order and preserve the scope of each quantifier. Then list the semantic evidence that a verifier can inspect and the external factual assumption that needs separate validation.


## Lesson 1.5 — Free variables, parameters, and sentences

### The statement and its scope

**Core principle.** Truth of a formula with free variables is relative to an assignment; sentences have assignment-independent truth in a fixed structure.

### A worked semantic construction

For φ(x)=E(x,c) on D={a,b,c} with cᴹ=b and Eᴹ={(a,b)}, φ is true for s(x)=a but false for s(x)=c. The closed sentence ∃x E(x,c) is true. Analyze this example systematically. Record the language first, then the nonempty domain, the interpretations of constant, function and relation symbols actually in use, and finally the formula under investigation. If no concrete relation is present, interpret the example as an argument about all structures meeting the stated hypotheses and write that change of level explicitly. Each step should say why the mathematical object exists, not merely report the eventual result.

### Counterexample discipline and boundary conditions

**Frequent mistake.** Do not describe an open formula simply as true without supplying a structure and assignment; changing an interpretation can reverse a sentence. A meaningful counterexample preserves the hypotheses of the claim being tested while breaking only the proposed conclusion. If a supposed counterexample changes the language, silently changes its constants, or violates one of the axioms, it does not disprove the original claim. Conversely, when the claim is a universal assertion about all models, just one legal countermodel is decisive. Keep these two directions separate: finding a witness is enough for an existential conclusion in a fixed structure; proving universal entailment demands attention to every legal structure.

### Proof laboratory: what must be shown

Distinguish M⊨φ[s] from M⊨σ for a closed sentence σ. One rigorous route is to write the target as a precise mathematical judgment and split the argument into sound subgoals. A constructive case should produce the structure, map, formula, or witness promised by the judgment. A negative case should produce a legal countermodel or identify an explicit theorem barring the proposed definition. If an implication is being established, prove the forward direction under named assumptions; for an equivalence, prove both directions independently. Do not let a numerical screen result replace a structural proof when the statement ranges over unbounded domains.

### Transfer to applied reasoning

Parameterized data filters differ from global integrity constraints in precisely this way. The translation must include the mathematical object corresponding to a real-world identifier, the status of absent or unknown information, and a statement of what the formal model leaves unspecified. A theorem guarantees something *given* these premises. It cannot establish that the premises faithfully describe a laboratory, database or institutional policy without external evidence. Keep a record of unverifiable assumptions, because a formal derivation may be completely valid even when its data pipeline is flawed.

### Three exercises and instructor guidance

**Exercise 1.5a — Reconstruct.** Rebuild the worked example in the smallest signature needed. State the domain, all nonlogical interpretations and the central truth or preservation claim. Is the conclusion about a single structure or an entire class? **Guidance:** Begin from: For φ(x)=E(x,c) on D={a,b,c} with cᴹ=b and Eᴹ={(a,b)}, φ is true for s(x)=a but false for s(x)=c. The closed sentence ∃x E(x,c) is true. Write a sentence or a formula-with-assignment, and justify the conclusion from the relevant recursive semantic clause or theorem. Name every free variable and every parameter.

**Exercise 1.5b — Find a boundary.** Test the tempting stronger claim that the principle automatically survives an arbitrary change of vocabulary, domain or interpretation. Give a specific change that would invalidate the inference or explain which hypotheses prevent such a change. **Guidance:** The primary hazard is: Do not describe an open formula simply as true without supplying a structure and assignment; changing an interpretation can reverse a sentence. Construct a countermodel if a universal claim is false; if the claim is valid, identify the preserving map or model-theoretic theorem. A failure to find a counterexample by enumeration does not resolve an unbounded question.

**Exercise 1.5c — Apply and audit.** Design an audit record for the application scenario below. Include the signature, an intended model, a checkable formula, and one risk of interpreting the result as an external fact. **Scenario:** Parameterized data filters differ from global integrity constraints in precisely this way. **Guidance:** State the proof obligation as: Distinguish M⊨φ[s] from M⊨σ for a closed sentence σ. Then list the semantic evidence that a verifier can inspect and the external factual assumption that needs separate validation.


## Unit 1 capstone — Build, vary and defend one model

**Part A: specify the vocabulary.** From this unit's running application, choose one nonempty domain and a minimal signature. Interpret each constant, function and relation explicitly. Write at least two sentences: one intended to hold and one intended to fail. If the unit focuses on a metatheorem rather than one finite example, explain why the running finite structure is illustrative rather than the theorem's proof.

**Part B: produce a controlled comparison.** Construct a second structure, a second theory or a modified formula connected with one of this unit's five lessons. Change exactly one semantically significant feature and compute what happened to the truth conditions. If the proposed preservation theorem is invalid, supply a legal counterexample. If it is valid, outline the inductive or theorem-based reason that every relevant formula is preserved.

**Part C: critique the claim.** A hypothetical reviewer states that the exercise establishes the result 'for all structures of any size'. Explain whether that is justified, using this unit's central distinction: Every interpretation fixes a domain, vocabulary, and a recursive truth definition. State the strongest conclusion that the evidence supports. Identify one mathematical assumption and one practical assumption that would need separate checking before applying the result to the real-world scenario.

**Suggested response framework.** Include the written signature; a complete interpretation table; formulas with all quantifiers and parentheses; one explicit witness or countermodel; a short derivation of the outcome; and a paragraph describing the limitations. Students working collaboratively should swap their artifacts and test whether another reader can reproduce the same evaluation without informal clarification.

## Unit 1 mastery checklist

- I can restate the five definitions of this unit accurately, with all needed hypotheses.
- I can build a legitimate small example and evaluate its key formulas.
- I can name at least one tempting invalid strengthening and diagnose it.
- I can distinguish first-order truth from real-world empirical truth.
- I can identify which claims require proof beyond a finite simulation.
