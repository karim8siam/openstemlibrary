# Unit 3: Context-free languages

*Editorial draft; not approved for live publication.*

## Grammars
**Grammars: conceptual explanation**

### Context-free grammar semantics
A context-free grammar is a tuple (V,Σ,P,S) with nonterminal set V, terminal alphabet Σ, productions P of the form A→α, and start symbol S. A derivation rewrites one occurrence of a nonterminal according to a production. A generated word is a terminal string derivable from S in finitely many steps. The distinction between a sentential form, which may still contain nonterminals, and a completed word is essential. Ambiguity means some word has more than one parse tree, not merely more than one sequence of choosing independent rewrite positions.

For balanced parentheses, S→(S)S | ε generates all Dyck words with one parenthesis type. To derive ()(), first use (S)S, then set the enclosed S to ε, then expand the trailing S into (S)S with both remaining S instances becoming ε. A proof of soundness is by induction on the derivation tree: enclosing a balanced word with a matching pair preserves balance, and concatenating balanced words preserves balance. A proof of completeness identifies the first matching close parenthesis and recursively splits the word into the interior and remainder.

A grammar might generate the same terminal string through two distinct trees. In arithmetic, E→E+E | E*E | id is ambiguous for id+id*id. Operator precedence can be enforced by separate nonterminals for expressions, terms and factors. Ambiguity affects semantics when parse trees induce different evaluation orders. Even a formally unambiguous grammar can be challenging to parse efficiently with a particular parser family. Keep the language theorem and parser engineering assumptions distinct.

### Parse trees, ambiguity, and evaluation order
Distinguish a derivation sequence from a parse tree: two derivation sequences may expand independent nonterminals in different orders yet describe the same parse tree. Ambiguity occurs when one terminal word has two genuinely distinct parse trees rooted at the same start symbol. To test the classic grammar E→E+E | E*E | id, derive id+id*id with `+` at the root and with `*` at the root. These two trees encode different grouping and, under arithmetic semantics, can produce different values. Changing the lexer cannot resolve this grammatical ambiguity unless the tokenization changes the language.

An unambiguous grammar can impose a structural precedence hierarchy. Let E→E+T|T, T→T*F|F, F→id|(E). With this grammar a multiplication factor belongs inside a term, so id+id*id has only the expected grouping. However, left recursion in E and T is unsuitable for a naïve recursive-descent parser that calls itself before consuming input. An equivalent right-recursive or iterative parsing strategy is required. Grammar ambiguity and parser nontermination are distinct defects.

Some context-free languages are inherently ambiguous: no context-free grammar for that language can remove ambiguity. Proving inherent ambiguity is deeper than identifying ambiguity in one chosen grammar. In routine language design, it is more useful to start with specific required syntax, encode precedence and associativity explicitly, and save source spans in the resulting AST. For test values 2,3,4, expression `2+3*4` must evaluate to fourteen, whereas `(2+3)*4` evaluates to twenty. Those are semantic checks of the intended trees, not a proof of grammar correctness.

A classroom parser visualizer should display both derivation and parse-tree structure and permit an input that the grammar rejects. It should not return one arbitrary parse as if it were the unique valid interpretation of an ambiguous grammar.

## Pushdown Automata
**Pushdown Automata: conceptual explanation**

### Pushdown machines and stack invariants
A pushdown automaton augments finite control with a stack whose height is unbounded in the mathematical model. Transitions may inspect the input symbol or ε, the control state, and the top stack symbol; they can then change state and stack content. Acceptance may be defined by final state or empty stack with a suitable construction translating between conventions. Deterministic and nondeterministic pushdown automata differ in expressive power; do not import the NFA-to-DFA equivalence result into this setting.

For {0^n1^n:n≥0}, design a PDA that pushes one marker for every 0, switches modes on the first 1, and pops one marker for each 1. It must reject a later 0, too many ones, and any leftover marker. If ε is in the intended language, accept it explicitly. The invariant during the first phase is stack height equal to the number of zeros processed plus an optional bottom marker; during the second phase the number of pushed unmatched zeros equals remaining marker count. This invariant proves correctness on all inputs, not merely observed stack traces.

Compare with a balanced-parenthesis checker. It pushes on `(`, pops on `)`, rejects an unmatched closing parenthesis immediately, and accepts only when the stack returns to its initial depth at the end. Multiple bracket types require storing bracket types, not just one integer depth, because `([)]` has balanced counts but invalid nesting. Include maximum-stack-depth instrumentation as a practical diagnostic while explaining that a finite stack allocation may reject inputs the abstract PDA would accept.

### Stack trace as a proof artifact
For Dyck words, push an open bracket when scanning `(` and pop for `)`. Maintain the invariant that the stack height equals the number of unmatched opening brackets in the prefix; any prefix with a negative balance is immediately invalid. For word `(()())`, show prefix heights 1,2,1,2,1,0, proving acceptance. For `())(`, the third symbol would require a pop from an empty stack, so rejection is unavoidable even though total numbers of each symbol match. This illustrates why a final-count-only algorithm is incorrect.

Multiple bracket types require a stronger invariant. On input `([{}])`, the stack stores a sequence of bracket types, and every closing delimiter must match the topmost opening delimiter. On `([)]`, an implementation tracking only a count would accept incorrectly at end because there are two opens and two closes. A correct stack-based checker rejects at `)` when top is `[`. Formalizing the invariant makes the implementation choice inevitable.

Pushdown automata may permit transitions that do not consume input. A careless ε-transition design can create an infinite loop in a simulator even on a word with a finite accepting run. An NFA's ε-closure is a finite set of states and can be fully computed because its control-state graph is finite. An arbitrary PDA ε-closure also involves an unbounded stack and cannot necessarily be enumerated by simply traversing a finite control graph. If a teaching simulator explores nondeterministic PDA configurations, use configuration memoization and bounded exploration with an explicitly inconclusive outcome when a budget is reached.

Acceptance by final state versus empty stack requires care when the input is exhausted, particularly for ε and premature stack emptying. Write the convention into the transition definition and show one standard translation between conventions before switching. A formal proof should not quietly change conventions to make a test case pass.

## Normal Forms
**Normal Forms: conceptual explanation**

### Normal forms without changing the language
Chomsky normal form uses productions A→BC or A→a, plus a carefully controlled exception S→ε when the empty word is included. Converting a grammar requires removing useless symbols, ε-productions, and unit productions, then binarizing long right-hand sides and replacing terminals inside mixed productions. The order and correctness of these transformations matter. If S derives ε, deleting all ε-productions indiscriminately loses a legitimate member. A new start variable is useful when the old start symbol occurs on right-hand sides.

Take S→aSb | ε. Introduce terminal representatives A→a and B→b, and an intermediate structure for concatenation; after handling the nullable rule, the grammar can be expressed in appropriate binary and terminal productions. The transformed grammar may contain many more nonterminals. This expansion is not evidence of a more complex language: formal normal form is a representation change preserving the set of generated words. Verify preservation on a bounded enumeration, but prove each transformation rule preserves derivations to establish unbounded equivalence.

Greibach normal form instead arranges nonempty productions to begin with a terminal, and is useful in some theoretical proofs. It is not simply a faster version of Chomsky form. Before comparing normal forms, specify whether ε belongs to the language, whether the grammar is reduced, and how new helper variables are mapped back to original constructs. The ability to transform a CFG into CNF enables the CYK membership algorithm when the input and grammar satisfy its assumptions.

### Normalization as a series of language-preserving passes
A reliable CFG-to-CNF converter should expose each intermediate grammar instead of applying a large opaque rewrite. First identify productive and reachable nonterminals; removing a variable that cannot derive any terminal word should not remove valid derivations. Then handle nullable variables: a production A→BCD with nullable B may need a corresponding A→CD to preserve words where B derives ε. Combinations of nullable symbols can generate multiple alternatives, so exponential production growth is possible in naïve conversion. Unit productions A→B may be removed by collecting unit reachability and copying appropriate non-unit productions.

Only after those passes should mixed terminals and long right-hand sides be transformed. For example, A→aBC can become A→X_a D, D→BC, X_a→a. Each helper nonterminal has a declared purpose, and newly introduced rules must not accidentally generate additional terminal strings. Start-symbol handling is especially important if ε is in the language or the start symbol occurs on right-hand sides. A fresh start symbol can isolate the ε exception permitted by the chosen CNF convention.

Verify a conversion on a small grammar by enumerating terminal strings through a fixed length and comparing membership in old and new grammars. That is a practical regression test but not sufficient to prove equality for all strings. The proof consists of simulations between derivation trees in both grammars after each pass. Every original derivation must be transformable into a new one, and every new derivation must correspond to an original one.

If the grammar includes semantic actions, normal-form conversion may change parse-tree shape even while preserving the generated language. An engineering compiler must preserve or reconstruct the intended semantics, perhaps through a parse-tree mapping. Language equivalence alone is not semantic equivalence.

## Parsing Properties
**Parsing Properties: conceptual explanation**

### Parsing, ambiguity and dynamic programming
The CYK algorithm decides membership for a grammar in Chomsky normal form. For input length n, create a chart cell for every substring interval. Each cell stores the nonterminals that can derive the corresponding substring. Start with length-one intervals using terminal productions; for longer intervals, try each split and each binary production A→BC. If B derives the left interval and C derives the right, include A in the enclosing cell. The word belongs to the language if the start symbol appears in the full-span cell. Empty input requires separate handling.

There are n(n+1)/2 nonempty substring intervals. There are O(n^3) combinations of interval and split; multiplying by grammar-size factors yields the standard polynomial parsing bound for fixed grammar. This analysis does not imply that every parsing algorithm runs in cubic time on every grammar. LL and LR parsers support linear-time recognition for suitable deterministic grammars, while generalized parsers address broader cases and may build packed parse forests for ambiguity. A parser should return not only acceptance but enough structure to recover derivations or semantic values.

For a short word, fill the chart by hand and record precisely which production justified each entry. For an ambiguous grammar, the same nonterminal may enter a cell through multiple split choices. A Boolean recognizer can discard the alternatives; a parse forest must preserve them. Regression tests should include invalid sentences differing by one token, deeply nested inputs, ε, and inputs that are legal only under one intended precedence rule.

### CYK as an explicit recurrence
Write T[i,j] for the set of nonterminals deriving the substring from position i through j, inclusive. If length one contains terminal a, include A whenever production A→a exists. For a longer interval [i,j], try every split k with i≤k<j; include A when there exists production A→BC, B∈T[i,k], and C∈T[k+1,j]. This is a recursive definition turned into a bottom-up algorithm by increasing interval length. After the chart is filled, accept precisely when S∈T[1,n].

The chart contains n(n+1)/2 cells. Each interval of length ℓ has ℓ−1 split positions, and there are n−ℓ+1 intervals of that length. Summing gives Σ_{ℓ=1}^n (n−ℓ+1)(ℓ−1) = (n³−n)/6 split examinations. This derivation explains why the algorithm's triple-nested structure gives cubic dependence on n for a fixed finite grammar. The cost per split depends on how binary productions and chart symbol sets are represented. Sparse grammars and bitset operations can change constant factors.

To recover a parse tree, store a backpointer whenever A is introduced: the chosen split k and the production A→BC. For an ambiguous grammar, store multiple backpointers rather than overwriting previous possibilities. A packed parse forest can represent many parse trees compactly. Counting trees or selecting the cheapest tree then becomes another dynamic program over this forest. Recognition and parsing are related but not identical output requirements.

The mathematical recurrence assumes grammar in CNF and nonempty input. An implementation that directly includes ε-productions or unit productions without preprocessing may violate the recurrence. Make these preconditions visible to the user, handle ε separately, and test a grammar that derives the empty string so the boundary is not silently ignored.

## Integrated Case Study and Model Limitations
**Unit synthesis: Context-free languages.** The following case study integrates formal definitions, correctness reasoning, limitations and realistic testing.

### Grammar design for nested configuration files
A configuration format might allow `list` values nested inside other lists, separated by commas. Its grammar could contain Value→NUMBER | '[' Elements ']' and Elements→ε | Value Tail, Tail→ε | ',' Value Tail. This grammar accepts an empty list, a single element list, and arbitrary nested lists. State whether trailing commas are allowed: as written, `[1,]` is rejected. If your parser accepts it accidentally, the implementation has diverged from the declared language. Different grammar choices may support trailing commas deliberately; this is a specification decision rather than a software bug by itself.

Build both a simple recursive-descent parser and an independent stack recognizer. For each input, record whether recognition succeeds, where parsing stops, and the shape of the parse tree. Recovering from a missing closing bracket is an error-reporting policy, not evidence that the original grammar generated the incomplete input. Add a parser-depth limit in the implementation and specify the resource error separately from invalid syntax.

For the laboratory, generate depth-d lists for d up to a chosen small bound and insert single-character defects: an extra comma, a closing bracket of the wrong type, or an omitted value. Compare results with a grammar-driven oracle. Then reason by structural induction to show that valid generated trees always have balanced brackets. The bounded test campaign can catch implementation mistakes but cannot replace the induction proof.

### A testable nested-list grammar
Extend the nested-list grammar with Boolean values and quoted strings. A possible value rule is Value→NUMBER|TRUE|FALSE|STRING|'[' Elements ']'. The tokenization policy must prevent the letters in TRUE from being reinterpreted as a sequence of identifiers. If strings permit escaped quotation marks, the lexer must recognize escaped delimiters before the grammar sees them. State whether whitespace is significant between tokens; typically it is ignored except inside strings, but the format designer must decide.

Define a tree-valued semantics: parsing `[1,[2,3],true]` produces a list with three elements, the second of which is another two-element list. A recognizer that returns only yes/no membership does not suffice if the application must construct such a tree. Show how the Elements/Tail nonterminals translate into a list of values while preserving order. An error in a tail-production semantic action may reverse the order without changing membership recognition, demonstrating the need for semantic tests.

Design metamorphic tests. If x and y are valid values, `[x,y]` should parse as a two-element list. If x is valid, surrounding it with list brackets yields another valid value. Inserting a comma after a closing bracket without a following value should be invalid under the given grammar. Also test empty lists and whitespace variants. Generate invalid inputs by removing exactly one delimiter or replacing a closing bracket type. Keep a separate class for resource-limit errors when recursion exceeds the configured maximum.

As a security note, a parser that accepts far deeper nesting than a downstream serializer can handle may trigger denial-of-service behavior. The formal grammar's unbounded nesting and the deployed system's resource policy should be documented as separate constraints, and errors should be distinguishable to the caller.

### Context-free parsing notebook
For grammar S→(S)S|ε, construct a recursive proof that every derived word has nonnegative prefix balance and final balance zero. Then prove the converse by splitting a nonempty balanced word at the first parenthesis that matches the opening symbol. This gives the decomposition `(u)v`, where u and v are themselves balanced. The production S→(S)S reconstructs that decomposition, completing induction on total word length. A proof only in one direction would establish an inclusion, not exact equality with the Dyck language.

Use a stack simulator to trace `()(()())`, logging the stack height after every character. For malformed `())(`, identify the earliest failing prefix rather than only comparing final counts. Translate a small CFG into CNF while tracking nullable symbols, and run CYK on a short input. Distinguish the parser's Boolean answer from the parse tree it could construct. Finally, add a deliberately ambiguous arithmetic grammar and show that a single accepted sentence may have two evaluation trees. Language membership and unambiguous semantics are separate achievements.

### Independent self-check: grammar versus parser
Provide a CFG, an example derivation, and a concrete parser routine for the same tiny language. Specify whether ε is accepted and which terminal-token policy is in effect. Then give a malformed input whose parser error location is near the end even though the underlying syntactic mistake occurred earlier. A grammar describes accepted words; a parser's error message and recovery strategy are engineering features outside pure membership. Distinguish ambiguity of a parse tree from multiple derivation orders, and distinguish an implementation stack limit from a formal context-free restriction.

### Worked question: Count balanced-parenthesis words
How many balanced words contain exactly four pairs of one bracket type? Explain why simple choose(8,4) overcounts.

**State the formal contract**
Every balanced word has four opening and four closing brackets, but not every arrangement is balanced. For instance, the arrangement beginning with ) violates prefix balance.

**Derive the result**
The Catalan number C4=choose(8,4)/(4+1)=70/5=14. This counts valid Dyck words with four pairs through the standard reflection-principle or recursive decomposition argument.

**Check the scope and a counterexample**
A checker can enumerate all choose(8,4)=70 arrangements and retain only those whose running balance never becomes negative and ends at zero. Exactly fourteen pass.

**Answer:** Four pairs give fourteen balanced words.

### Worked question: Stack invariant for 0^n1^n
A PDA pushes one X for each 0, then pops one X for each 1. Determine membership of 000111 and 00111.

**State the formal contract**
For 000111 the push phase produces three X markers; the three ones pop them all, leaving the bottom marker and a valid end of input.

**Derive the result**
For 00111 the push phase produces two X markers; the first two ones pop them, but the third one requires a nonexistent marker, so the machine rejects.

**Check the scope and a counterexample**
The algorithm also rejects 0101 if switching from one phase to the next is irreversible, even though total counts match. The invariant concerns both ordering and outstanding markers.

**Answer:** 000111 is in the language; 00111 is not.

### Worked question: CYK chart capacity
For a nonempty length-six input, how many distinct nonempty substring cells does the CYK dynamic-programming chart contain?

**State the formal contract**
A cell is identified by interval endpoints (i,j) satisfying 1≤i≤j≤6. There are six cells of length one, five of length two, down to one of length six.

**Derive the result**
The total is 6+5+4+3+2+1=6×7/2=21. This chart count is not the same as the number of grammar-rule applications across all splits.

**Check the scope and a counterexample**
CYK may consider O(n^3) split positions in total for a fixed grammar. Showing only 21 chart cells cannot establish an O(n^2) time bound for the full algorithm.

**Answer:** There are 21 nonempty interval cells.
