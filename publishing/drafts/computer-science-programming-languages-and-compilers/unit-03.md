# Unit 3: Parsing

*Draft; not approved for public deployment. Eight-unit manuscript with source-specific cases and independent verification pending.*

## Lexical Analysis
**Lexical Analysis: conceptual explanation**

A lexer can be built from regular-language recognition, often via a deterministic finite automaton. Define token classes for identifiers, numbers, strings, comments, punctuation and keywords. If two token classes match a prefix, select the longest match under maximal munch and apply a deterministic priority rule. For example, scanning `===` under languages that support both `==` and `=` should not accidentally produce `==` then `=` when `===` is itself a valid token. The keyword `if` is recognized differently from identifier `iffy` even though both begin with the same two letters.

Track source offsets and line/column information deliberately. Columns may count bytes, Unicode code points or display graphemes; editors often display tabs and combining marks in nontrivial ways. A diagnostic should avoid slicing a UTF-8 multibyte character in half. Strings require escape processing and explicit end-of-input behavior; unterminated quotes must not force the scanner into an infinite loop. Test a lexer with an empty source, very long identifiers, malformed escape sequences, nested-looking comments and line-ending variations. Keep a clear contract for whitespace and comments: discard them for parsing if they are semantically irrelevant, but preserve trivia or token spans when a formatter and source-to-source tool require exact round trips.

### Design investigation: scanner ambiguity
Use the token vocabulary KEYWORD_IF, IDENT, ASSIGN, EQUAL, NUMBER and SEMICOLON. Scan `ifx=12; if x==12;` and show each token boundary. `ifx` must not split merely because its first two characters spell a keyword. If the language allows decimal fractions, test `.5`, `1.`, `1e-2` and `1e` and decide how malformed numeric tokens are reported. Implement source spans for both Unix and Windows newlines and verify the line number after a CRLF pair is incremented once. Add a quoted string containing `//` and ensure it does not start a comment inside the string. Run a fuzz test that constructs random prefixes and stops the scan if the token cursor ceases to advance. A deterministic lexer must either emit a token or an error that moves forward; infinite loops on malformed text are unacceptable. Document exact rejection rules rather than silently accepting host-language numeric syntax.

## Grammars
**Grammars: conceptual explanation**

A context-free grammar describes nested language structure via productions. The expression grammar `E -> E + T | T` is left recursive and natural for LR-style parsing, but a naive recursive-descent function that calls itself before consuming input will diverge. Eliminate immediate left recursion for an LL parser with `E -> T E'` and `E' -> + T E' | epsilon`; then construct left-associative AST nodes in the semantic action, because grammar shape and associativity must agree. An abstract syntax tree need not mirror every nonterminal in the concrete grammar.

Ambiguity is a property of a grammar relative to strings, not simply a parser implementation being confused. A grammar is ambiguous when at least one token sequence has more than one parse tree. The classic dangling-else example shows why a rule that associates `else` with the nearest unmatched `if` must be stated. For predictive parsing calculate FIRST and FOLLOW sets and check table conflicts; a FIRST/FIRST overlap or FIRST/FOLLOW overlap for an epsilon alternative prevents a simple LL(1) choice. When the grammar is not LL(1), possible responses include refactoring, more lookahead, Pratt parsing, LR parsing or a generalized parser. The right choice depends on the language’s requirements, not a universal ranking of techniques.

### Design investigation: precedence as a semantic contract
Build trees for `a+b*c`, `a*b+c`, `a-b-c`, and `a^b^c`. Use distinct input values to demonstrate associativity: with a=12,b=5,c=2, `(a-b)-c` equals five while `a-(b-c)` equals nine. A left-recursive grammar can naturally represent left associativity in bottom-up parsing, while a refactored LL grammar must construct the same AST intentionally. Show FIRST sets for the alternatives that begin with identifier, literal or left parenthesis. Add a production allowing epsilon and compute the conditions under which FOLLOW conflicts arise. Introduce the nested `if ... if ... else` example and state whether else matches the inner or outer if. Serialize each AST for review so a test can compare structure rather than just program output. The assignment is complete only when the grammar, AST policy and parser implementation agree.

## Parsing Algorithms
**Parsing Algorithms: conceptual explanation**

Top-down recursive descent is easy to inspect: each nonterminal has a parsing function that consumes tokens and either returns an AST or reports a structured error. Pratt parsing is an efficient option for expressions with many operators: each token supplies prefix or infix behavior and a binding power. Parsing `a+b*c` with multiplication at higher binding power produces an addition node with a multiplication right child. For left-associative operators use an appropriate right binding-power convention; exponentiation often requires right associativity. A parser needs a deterministic policy for equality comparison chains and non-associative operators.

Bottom-up LR parsers shift input symbols and reduce recognized right-hand sides to nonterminals according to a parsing table. An LR item identifies a production and a dot position; closure and goto construct states. Shift/reduce conflicts often indicate either a genuine ambiguity or a grammar written without sufficient disambiguation. Generalized LR or Earley parsing can handle broader grammars but may produce forests or require later ambiguity resolution. Complexity statements should name the algorithm and grammar family; typical linear behavior of deterministic parsers does not imply every generalized parse is linear. Test both AST shape and consumption of the entire input so trailing junk cannot be accepted silently.

### Design investigation: choose a parsing algorithm consciously
Write a Pratt parser for three infix operators plus parentheses. The function `parseExpression(minPower)` consumes a prefix expression, then loops while the next operator's binding power permits attachment. Trace token consumption for `x + y * z` with the current minimum power at each recursion. Add a right-associative operator and show why its recursive right binding power differs. Compare this implementation to a hand-coded recursive-descent grammar and an LR parser generator on the same corpus. Judge maintainability, allowed grammars, error messages and debugging workflow, not a made-up absolute speed ranking. Stress-test long chains of parentheses and operators. An implementation using deep recursion may hit host stack limits even when the language grammar itself permits deep nesting; document an input-size policy and a recoverable failure. Confirm that successful parsing consumes the entire token sequence rather than ignoring garbage after a valid prefix.

## Error Recovery
**Error Recovery: conceptual explanation**

Error recovery is part of the language tool’s user interface. An immediate failure on the first malformed token is easy to implement, but a useful compiler should often continue and report independent errors in one run. Panic-mode recovery skips tokens until a synchronizing symbol such as a semicolon or closing brace is found. Phrase-level recovery inserts or deletes a likely missing token and attempts to continue. Every recovery path must guarantee progress; a parser that repeatedly reports the same token without consuming or changing state can loop forever.

A helpful diagnostic says where a problem occurred, what was expected, and one plausible fix without pretending the compiler knows the author's intention. For `let x = (2 + ;` the missing right operand should be localized near the semicolon, while the unmatched parenthesis may be a secondary error. Avoid cascaded messages produced by invented placeholder nodes unless they are clearly marked as consequences. Keep error nodes in the AST with well-defined downstream behavior: the type checker can ignore poisoned subtrees rather than manufacturing unrelated type errors. Compare recovery strategies using a corpus of intentionally broken programs, measuring false follow-on diagnostics, latency, and whether the final errors retain accurate positions.

### Design investigation: recover without lying
Feed a compiler three statements: a valid declaration, an assignment missing its right operand, and a later use of an undeclared identifier. In fail-fast mode, only the first error is reported. In panic-mode recovery, a semicolon can serve as a synchronization point so the later name-resolution error still appears. Require the parser to consume at least one token or change state after each recovery action. Track errors caused by synthetic placeholders separately: a placeholder expression should not trigger spurious division-by-zero or dozens of irrelevant type errors. Evaluate diagnostics with four criteria: accurate span, useful expected-token description, absence of misleading follow-ons, and stable behavior under one-character edits. Save before/after source snippets for a missed delimiter, stray brace and unclosed string. Explain why the “most likely fix” is a suggestion rather than a proof of author intent.

## Integrated Case Study and Model Limitations
The grammar `E -> E+E | id` accepts `a+b+c` with more than one parse tree. A precedence or associativity rule, or an unambiguous grammar with expression and term nonterminals, restricts the parses. Trace tokenization of `a>=10`, showing why a longest-match rule is needed for `>=`. Then demonstrate how recursive-descent parsing of a directly left-recursive grammar might recurse before consuming any token. A recovery strategy should consume or synchronize at an appropriate delimiter after an error, avoiding an infinite diagnostic loop.

### Laboratory: parser engineering for an intentionally difficult grammar

Define a tiny language with arithmetic, `if`, blocks, function calls, arrays and variable declarations. Implement a scanner before the parser. The scanner emits tokens with kinds, source spans and original spellings. Write fixtures for `x==y`, `x===y` if the language supports both operators, `ifelse` versus `if else`, negative literals, comments containing token-looking punctuation, and identifiers with Unicode letters if allowed. If the language does not support Unicode identifiers, specify and test the rejection behavior. A lexer should never return a token whose source span is outside the input or move backward unless explicitly requested by a parser backtracking interface.

Implement two expression parsers. First use a deliberately left-recursive expression grammar and explain why naive recursive descent diverges before reading a token. Refactor to factor and term productions or implement Pratt parsing with a binding-power table. Set addition left associative, multiplication higher precedence, and exponentiation right associative if the language includes it. For `2^3^2`, the right-associative tree is `2^(3^2)` rather than `(2^3)^2`; their values differ radically. Do not silently choose associativity based on how the host language evaluates its operator. Inspect both parse trees in a machine-readable AST dump.

Construct a FIRST/FOLLOW analysis for a simplified grammar. For each nonterminal, iterate until its FIRST and FOLLOW sets stop changing. Include epsilon alternatives, check that predictive choices are disjoint, and show the specific pair of productions responsible for any table conflict. When encountering a dangling-else ambiguity, encode the nearest-unmatched-if rule or split matched and unmatched statements. Explain how the policy appears in the AST of an `if` nested inside another `if`. An LR generator could resolve the ambiguity with a precedence declaration, but that does not remove the need to document the language rule.

Add structured diagnostics. Remove a closing parenthesis from a nested call and verify that an error is attached to the end-of-input or the next token with an informative expected-token list. Then remove a semicolon between statements and confirm that recovery can continue to find an independent undefined identifier later. Compare fail-fast and panic-mode recovery: the latter improves the number of independent issues detected but risks cascaded false messages. Define a recovery budget and require forward progress after a diagnostic. A recovery routine that retries the same token forever is itself a parser bug.

Fuzz the scanner and parser with bounded random token sequences, saving random seeds. Important invariants: no uncaught exception on user input, no infinite loop, spans remain within input boundaries, and a successful parse consumes the whole permitted program. Add metamorphic transformations: adding parentheses around an expression should preserve its meaning where the grammar allows it; renaming a bound identifier consistently should preserve resolution without capture; inserting irrelevant whitespace should preserve AST structure if whitespace is not significant. When a discrepancy appears, minimize it to the smallest input that still fails, then fix the grammar or implementation. A final test report distinguishes parsing acceptance from semantic and type correctness.

### Failure clinic: a parser that reports no useful errors

A compiler for a student language attempts to recover from every missing token by inserting an invisible semicolon or closing bracket. In the test program, the user forgets one right parenthesis; the parser invents three tokens, then produces eleven type errors on nodes that were never present in the source. The final compiler exit code is nonzero, but the report is nearly impossible for a student to act on. Diagnose the missing distinction between syntax recovery and verified program structure. A synthetic token must carry a marker showing that it was inserted; downstream analysis should not pretend the subtree is reliable.

Create a recovery strategy by specifying a limited set of synchronization tokens and a budget for inserted tokens. Statements may synchronize at a semicolon or closing brace; expressions may synchronize near a comma or matching delimiter. Every recovery step consumes real input or changes parser state toward completion. A diagnostics engine should suppress errors inside poisoned subtrees when they stem from the original syntax error, while still reporting truly independent errors in later statements. Design fixtures containing two unrelated mistakes separated by a valid declaration.

The original language grammar is ambiguous around nested conditionals. Some parser-generator conflicts were suppressed by default shift behavior without a documented nearest-else rule. Consequently the interactive playground’s hand-written recursive-descent parser produces a different AST from the batch compiler's generated parser. Use a minimal nested-if example where the two branches assign different values, then trace both ASTs. Resolve the grammar ambiguity explicitly, record expected tree shape, and run the same corpus through both parsers. One parser's successful return cannot prove that its choice matches the language definition.

Now add a denial-of-service test. Nested parentheses numbering in the thousands may cause recursive calls until the host process overflows its stack. The grammar may be valid, but the implementation has a resource limit. Accepting or rejecting extreme nesting should follow a documented policy and produce a controlled diagnostic. Add token-count, recursion-depth or execution-budget checks with clear limits. A parser should be robust against malformed and adversarial source, not just the collection of neat assignment examples used during development.

### Worked comparative study: parse errors versus semantic errors

Take four small inputs: `a + * b`, `a + b`, `a + b; garbage`, and `a + (b*c`. The first violates an expression grammar that expects an operand after plus. The second can be syntactically valid even if a and b are undeclared. The third illustrates a parser that accepts a valid prefix but ignores trailing tokens, which is not equivalent to accepting an entire program. The fourth has an unmatched parenthesis and may reach end-of-input while expecting a delimiter. Distinguish these failures before implementing diagnostics. Error category, span and recovery policy should be testable outputs.

Now consider precedence and associativity: `a-b-c` may be correctly tokenized and grammatically accepted while still yielding the wrong AST if a refactored grammar creates right nesting. A single arithmetic output is a weak test if test values accidentally make both nestings equal. Choose discriminating operands and serialize the AST. An operator table should contain binding power, associativity, arity and possibly contextual restrictions. Some constructs such as assignment are statements or expressions depending on the source language; their grammatical category must be explicit.

A production parser and a code formatter may share a syntax tree representation, but they have different goals. A formatter often needs source trivia and exact comments; an optimizer often wants a compact representation with irrelevant punctuation discarded. The language service may need incremental parsing as the user types incomplete code. This introduces error nodes and syntax trees that are temporarily invalid, a state that a batch compiler might simply reject. Name the target use case when evaluating parser architecture.

Write a test corpus that pairs each source string with expected token kinds, a success-or-failure parse classification, normalized AST, name-resolution classification and diagnostic spans. Run the corpus through a hand-written parser and a parser-generator implementation if both exist. A grammar conflict report should be investigated rather than suppressed because successful recognition does not certify the intended parse tree. Add a timeout or recursion budget to prevent pathological inputs from consuming unbounded resources. A final diagnostic review should ask whether a novice can locate and repair the source of the error without reading internal stack traces.

### Unit review: compare diagnostics with the same code base

Run the expression corpus under a scanner, a recursive-descent or Pratt parser and any alternate parser implementation available. For an accepted input, compare AST shape and full-token consumption. For a rejected input, compare primary error location and number of cascaded follow-on messages. Introduce malformed strings and unbalanced delimiters to test that recovery makes forward progress. An error-recovery technique is not better merely because it emits more diagnostics: many may be artifacts of synthetic recovery nodes. Include a stress case with deeply nested delimiters and enforce documented resource limits. Keep parser-generator conflicts and grammar ambiguity decisions as part of the test record. The purpose is to make syntax behavior reproducible for tools and learners, not to hide ambiguity behind one parser's default conflict resolution.

### Worked question: Operator precedence tree
Parse `2+3*4` under conventional precedence and calculate its value. Describe a grammar-level cause for the result.

**Set up definitions and premises**
A grammar separating expression, term and factor nonterminals places addition at expression level and multiplication at term level. The parser first groups 3*4 as one term.

**Derive the result**
The AST has Add at the root, left child Number(2) and right child Multiply(Number(3),Number(4)). Evaluate multiplication to 12, then addition to 14.

**Validate limits and interpretation**
If a single ambiguous rule E -> E op E is used without precedence, the alternative tree Multiply(Add(2,3),4) produces 20. A parser returning a value without a tree-shape test could hide the ambiguity with equal operands.

**Answer:** Correct tree is Add(2,Multiply(3,4)); value 14.

### Worked question: Eliminate left recursion
Rewrite `E -> E + T | T` for a predictive parser and explain what must be done to retain left associativity.

**Set up definitions and premises**
Immediate left recursion causes a naive recursive-descent function for E to call itself before consuming tokens. Factor the grammar as E -> T Eprime; Eprime -> + T Eprime | epsilon.

**Derive the result**
Parse the first T, then read a repetition of plus followed by T. To preserve left-associative semantics, fold the sequence into an accumulator: for a+b+c build Add(Add(a,b),c), not Add(a,Add(b,c)).

**Validate limits and interpretation**
Test 12-5-2 if subtraction is present: left associativity yields five, whereas right associativity yields nine. A grammar refactoring is correct only if the AST construction matches the intended language rule.

**Answer:** Use a non-left-recursive tail production plus a left fold for the AST.

### Worked question: Recovery from a missing operand
For `let x = 4 + ; let y = 2;`, choose a recovery point and explain how to avoid cascading diagnostics.

**Set up definitions and premises**
The parser recognizes `4+` and expects an expression but encounters a semicolon. Report the expected operand at that span rather than treating the semicolon as a legal expression.

**Derive the result**
Create a poisoned expression node or skip to a synchronizing semicolon under a documented recovery policy. Consume or otherwise advance parser state so the next iteration does not repeat the same error indefinitely.

**Validate limits and interpretation**
Continue parsing `let y=2` independently. Suppress type errors produced solely from the poisoned x initializer, while allowing a real error in later code to be reported. Test that the parser consumes the permitted entire token sequence.

**Answer:** Report one primary missing-operand syntax error; recover at semicolon and continue safely.
