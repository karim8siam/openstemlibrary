# Unit 1: Language concepts

*Draft; not approved for public deployment. Eight-unit manuscript with source-specific cases and independent verification pending.*

## Syntax
**Syntax: conceptual explanation**

A grammar for a small expression language can be specified before any interpreter exists. Take the terminals ID, NUM, PLUS, STAR, LEFT and RIGHT and productions E -> T E_tail, E_tail -> PLUS T E_tail | epsilon, T -> F T_tail, T_tail -> STAR F T_tail | epsilon, and F -> ID | NUM | LEFT E RIGHT. This grammar encodes the usual multiplication precedence structurally: a plus joins terms, while a star joins factors. A parse of 2+3*4 therefore places the multiplication inside the right term, not at the outer root. The precedence is not a numerical accident. It follows from the nonterminal dependency graph. If a language designer instead chooses a single ambiguous rule E -> E op E, the parser must consult additional declarations or choose one of several trees.

Tokenization is a distinct contract. The lexer must decide whether `letx` is one identifier or keyword `let` followed by identifier `x`; the answer usually follows maximal munch and an explicit reserved-word policy. Whitespace might be discarded between tokens yet preserved inside string literals. Negative literals illustrate another boundary: `-5` may be one signed number token or unary-minus operator followed by a positive number. Both designs can work, but their consequences appear in the grammar, error reporting and source positions. Record byte or character spans for every token so the compiler can later point to a precise source location. A grammar that accepts all its examples is not automatically correct: test nested parentheses, missing operands, trailing operators, repeated unary operators and non-ASCII identifier rules. Decide whether braces, comments and newlines are syntactically meaningful before extending the language.

### Design investigation: lossless source locations
Implement a token stream that retains `(kind, spelling, start, end)` for every token. Parse `sum + index*2` and print an AST containing one Add node and one Multiply node. Use the source locations to highlight the exact characters of the multiplication. Insert an extra space before index and verify that operator precedence stays unchanged while spans shift by one character. Replace index with a Unicode identifier and state whether offsets are counted in code points or UTF-8 bytes. If the parser discards source locations entirely, explain how an error in a large expression could be reported without guessing positions. Extend the grammar with unary minus. Show the AST for `-a*b` and decide whether negation binds before multiplication. A parser that only returns the numerical result would not expose a precedence defect when testing a=b=0; choose discriminating values. The final artifact should contain a grammar, parse-tree expectations and at least one malformed source test.

## Semantics
**Semantics: conceptual explanation**

A semantic rule must specify more than the result of ordinary arithmetic. For a minimal expression language, write a judgment `environment, store |- expression ⇓ value, new-store` or a set of small-step transitions from configurations to configurations. The environment maps identifiers to locations; the store maps locations to values. The difference matters when assignment and aliases exist. An environment entry `x -> l7` remains unchanged while `store[l7]` changes from 2 to 3. Without this separation a semantics may silently rule out observable mutation or wrongly treat a copy as an alias.

For addition, evaluate its operands according to a documented order, then combine numerical values. If one operand can print, throw or assign, the order is observable. For example, let `x=1` and evaluate `x + (x := 2)` under left-to-right rules with assignment returning its new value. The left subexpression reads 1; the right changes the store and returns 2; the result is 3, with the final stored x equal to 2. Different evaluation-order rules can change this example. A correct language definition should not rely on the host implementation’s unspecified evaluation order. If the language includes division, specify what zero denominators do, including whether evaluation of a later operand can occur after an earlier exception. The semantic relation is the authority used to test interpreters and compiler transformations, not an informal resemblance between outputs on a few happy paths.

### Design investigation: executable transitions
Define a state pair `(environment,store)` and a trace alphabet with Read, Write, Call, Return and Raise events. Interpret `let x=2 in (x:=x+3)+x` using your chosen left-to-right evaluation semantics. Record the first read of x, the store write setting it to five, the subsequent read, and the returned value ten if assignment yields the assigned value. A different assignment-result convention changes this calculation; specify it before running the interpreter. Alter the program to `x+(x:=x+3)` and calculate the final result again. Show that comparing only the final store does not establish equivalent evaluation: both programs may leave x=5 while returning different totals. Add a failure case with division by zero after a write and decide whether the write is rolled back. Most ordinary imperative languages do not automatically provide transactional rollback; explain why a semantic model needs this fact. Test the same trace through an interpreter and through a lowered program.

## Binding
**Binding: conceptual explanation**

Use lexical addresses to make scope resolution testable. In `let x=10 in let y=4 in let x=3 in x+y`, the innermost x is three, y is four, and the sum is seven. One representation stores a chain of frames with bindings; another resolves every identifier to a pair `(depth, slot)` during compilation. The inner x has depth zero, y has depth one, and the shadowed outer x is not read. A resolver should report a reference to an undeclared name with a source span rather than inventing a value. It should also distinguish a declaration from the local storage value that the runtime will eventually hold.

A closure exposes what plain local-variable lookup hides. Define `makeAdder(z)` returning a function `f(x)=x+z`. After `makeAdder(8)` returns, calling the returned function on 5 must produce 13. Capturing the caller's dynamic environment when f is later invoked would be incorrect for lexical scope. An implementation can capture a persistent environment object, copy an immutable value, or lift the captured variable into a hidden closure field. These strategies differ when mutation is allowed. Add `z := z+1` inside the closure and call it twice: does each closure have its own mutable cell or share one global cell? Derive the answer from the language’s binding rules and test it with two separately created closures. Do not confuse visibility of a declaration with lifetime of the object it references.

### Design investigation: capture without name collision
Analyze `let k=10; function outer(k){ return function(z){ return k+z } }`. Resolve the inner reference to k to the parameter of outer rather than the global binding. Draw declaration identifiers, not merely strings, and annotate each use. Construct closures `a=outer(3)` and `b=outer(5)`; expected results for a(2) and b(2) are five and seven. Now change k inside the returned closure on every call. Determine whether the closure stores a mutable captured cell, an immutable value or an address through which the caller can update data. Add a third nested function with its own k and test shadowing. Finally rename global k to q without changing other bindings; explain why the return values should remain unchanged. If your name resolver incorrectly selects the nearest spelling without respecting the lexical scope chain, the test should fail. Record separate allocation identifiers for each closure environment.

## Evaluation Strategies
**Evaluation Strategies: conceptual explanation**

Evaluation strategies can be contrasted with an expression that has both work and observable effects. Consider a function `twice(x)=x+x` and an argument `expensive()`. In call-by-value the argument is computed once before the function body. In call-by-name the argument expression can be computed twice when substituted at both uses of x. In call-by-need a delayed computation is shared, so only the first demand performs work. However, when the argument is never used, call-by-value still evaluates it and call-by-name/need need not. This changes termination: `const(x, y)=x` can return immediately under non-strict evaluation even if y diverges.

Mutation and exceptions complicate the comparison. If the argument increments a counter, repeated evaluation has visible consequences; if the argument throws, an unused delayed argument may never raise its exception. Make a trace table with columns for time, expression or thunk forced, store modification, result and exception state. Distinguish call-by-reference, where a parameter denotes a caller-owned storage location, from call-by-name, which is not simply an alias. A compiler implementing laziness also has to represent thunks, decide when to memoize them, and prevent a thunk from being forced recursively without a defined policy. The preferred evaluation strategy follows the language contract; performance measurements are secondary to semantic equivalence.

### Design investigation: strictness and effects
Define `first(a,b){return a}` and `expensive(){ print("computed"); return 9 }`. Under eager call-by-value, invoking first(4,expensive()) prints before returning four; under call-by-name and call-by-need, the second argument may remain unevaluated. Replace first with `repeat(a){return a+a}` and pass expensive as a. Count the number of prints under each strategy: eager evaluation once, call-by-name potentially twice, and memoizing call-by-need once. This trace assumes the functions and evaluation rules given, not an unspecified real language. Now make expensive throw. For first, determine whether the exception occurs; for repeat, determine when it occurs. Add a recursive delayed binding that forces itself and define the runtime policy for detecting a black hole or recursive thunk. Build a test table for the results, side effects and termination behavior. State why selecting one strategy for speed without specifying source semantics would invalidate compiler correctness.

## Integrated Case Study and Model Limitations
Consider a program with outer variable x=10 and function f declaring a local x=3. A lexically scoped language resolves x inside f to 3 even if f is called from a function with another x. A dynamically scoped model may instead search caller environments; the results differ. Draw an environment chain and specify evaluation order for a function call whose argument has a side effect. To discuss semantics rather than just syntax, state which store location changes and the final returned value. A parser can accept both expressions while the semantics still differ.

### Laboratory: define a language before writing its evaluator

Construct a language called MiniCalc with integers, local declarations, function application, assignment, conditionals and blocks. Begin by specifying a lexical alphabet and grammar with separate productions for assignment and expressions. Decide whether `a=b=c` means `(a=b)=c`, `a=(b=c)` or a syntax error. If assignments yield values, state the value and whether the left operand must designate a location. Define the Boolean condition rule: is integer zero false, or must a condition be an explicit Boolean? A full specification eliminates these ambiguities rather than delegating them accidentally to the implementation language.

Add a source example. Initialize `x=4`, define `f(y){ let x=2; return x+y; }`, and call `f(x+1)`. Under lexical scoping and call-by-value, the argument is evaluated in the caller to five, the function body reads its local x as two, and the result is seven. If f instead assigns to x, the local x changes, but the outer x remains four unless explicit reference capture or external mutable storage is involved. Draw environments E0 and E1, map x to two distinct locations, then describe the stores before and after each step. A shallow evaluation that returns seven without tracking storage misses why the program behaves that way.

Next implement a deliberately minimal operational evaluator. Use value variants `Int(n)`, `Bool(b)`, `Closure(params,body,capturedEnv)` and `Error(type,span)`. Define evaluation as a function of an environment and store, with an explicit fuel counter that prevents a nonterminating sample from hanging the test suite. Functions evaluate arguments under a documented order. The interpreter's output includes a value and a trace of writes and calls. Test lexical shadowing, a closure returned from its enclosing function, nested assignment, a short-circuit Boolean expression, and a function whose unused argument would throw if evaluated. These tests force you to specify whether `and` and `or` are short-circuiting. If you keep a big-step interpreter, add explicit propagation for exceptions and fuel exhaustion.

Compare two optimization candidates. Candidate A replaces `2*3` with `6`, which is sound for exact mathematical integers with no effectful operands. Candidate B rewrites `f()+0` to `f()`; this may be sound only if arithmetic conversions, exception behavior and type rules do not change. If `f` returns floating-point NaN, signed zero or a custom overloaded type, the laws of algebra require attention. The source semantics determines when a transformation is valid. Your lab report must give the specific assumptions, a counterexample when an assumption fails, and a regression test that would detect the error.

Finally ask two independent student teams to implement the grammar and evaluator from your specification without sharing code. Compare AST shapes on the same source corpus and outputs on an enumerated set of short programs. When teams disagree, find the ambiguous specification clause and revise it. This exercise demonstrates why compiler architecture begins with language definitions and testable operational meaning, not with a favorite parser library. The result is a language implementation whose decisions can be explained and defended, even though it remains much smaller than a production language.

### Failure clinic: inconsistent precedence between tools

A language implementation has a parser, an interactive console, a formatter, and a source-code indexer. The parser correctly interprets `1+2*3` as seven, but the formatter prints the AST as `(1+2)*3` and the IDE indexer records the variable inside a call expression as part of the wrong scope. All components compile, yet their interpretations are inconsistent. Diagnose the three boundaries separately. The formatter needs parenthesization rules derived from AST operator precedence, including associativity and any non-associative operators. The indexer needs resolved symbol identities rather than guessing relationships from token adjacency. The parser needs source spans so errors can be localized after comments or whitespace are rewritten.

Create an observation matrix covering original source, AST, formatting output, reparsed AST, resolved names and interpreter trace. A round-trip test need not preserve exact whitespace, but should preserve semantic tree shape. Construct a smaller failing input for each defect: `a+b*c` for precedence, a nested let for scope and a string literal containing punctuation for lexical trivia. Explain why simply running the formatted program and comparing one numeric result is inadequate. A variable may be assigned the same value in both erroneous scope choices, causing a false pass. Choose a discriminating environment where the inner and outer bindings differ.

Now add a language-version transition. Version 1 interprets `^` as exponentiation; version 2 reassigns it to bitwise XOR. A parser cache serialized under version 1 cannot safely be reused without a version marker. Record grammar and semantic version in parse caches and invalidate affected artifacts. Error messages should describe the active language version. A grammar change can also affect code highlight rules and formatter spacing, so tests should cover the entire toolchain rather than only the evaluator. If your editor plugin and compiler are separate products, specify a compatibility contract for parser or protocol versions.

Close the investigation with a teaching comparison: syntax recognition, binding, and evaluation are logically distinct proofs. A program can be grammatically valid, fail to resolve a name, and have no runtime meaning. Another can parse and type-check but trap on a permitted error. A third can execute correctly while a pretty-printer loses essential parentheses. Treating “compile succeeded” as equivalent to “every language tool understands the program” hides each of these failure modes.

### Worked comparative study: source-level equivalence and observational tests

Consider two programs in a small eager language. Program P is `let x=2 in let y=x+1 in y*y`. Program Q is `let x=2 in (x+1)*(x+1)`. Both compute nine for this particular fixed input. Yet rewriting a program by duplicating arbitrary expressions is not automatically valid. Replace x+1 with `readAndIncrementCounter()`: Program P evaluates that expression once, stores its result in y, and multiplies the saved value by itself; Program Q may evaluate it twice, obtaining different values and recording a different number of side effects. If a language's arithmetic multiplication can also overflow or throw, the exact order of evaluation and exception handling becomes relevant. Observational equivalence asks whether two programs have indistinguishable externally visible behavior in all allowed contexts, not whether one test returned the same integer.

For a teaching language without side effects, the compiler can exploit referential transparency: substituting an expression for a binding can preserve results if capture is avoided and the expression does not diverge in a context that was previously lazy. Capture avoidance matters even in a pure language. Substituting a free variable into the body of a lambda can accidentally bind it if names are not renamed safely. Use alpha-renaming or explicit symbol identities before performing beta-reduction. Distinguish alpha-equivalence, which changes bound variable spellings, from beta-reduction, which applies functions, and eta-reduction, which simplifies extensional function expressions under suitable assumptions.

Define a small observational test harness that runs programs with initialized environments and captures value, printed output, final exposed store and exception category. Generate P and Q variations with arithmetic-only expressions, effectful expressions, and expressions that may throw. The goal is to observe which assumptions make the proposed equivalence valid. If the language lacks first-class effects, explicitly state that rather than using an interpreter that happens not to implement them. Write a counterexample for a different evaluation strategy: a lazy language can avoid evaluating an unused binding where an eager language would not. Finally explain why a compiler optimization cannot be judged solely by its source syntax: the transformation's validity depends on the complete semantic context, including memory aliasing, evaluation order, exceptions and arithmetic conventions.

### Unit review: distinguish three semantic questions

For every example in this chapter, label the earliest phase that can reject it: lexical recognition, parsing, name resolution, typing or execution. Then check whether the final value is affected by scope, call strategy or evaluation order. A precise response to a wrong result should identify the environment binding read at each identifier occurrence and the sequence of side effects. A compiler may legally choose a different instruction ordering only where the source semantics makes that order unobservable. Revisit the earlier closure example and separately test two closure instances, a shadowed local declaration and a delayed argument that is never forced. What passes as one arithmetic calculation can still violate binding or evaluation semantics. These tests establish why a language implementation needs a written semantic contract and why automated outputs must be interpreted relative to that contract.

### Worked question: Grammar versus meaning
A language accepts `let x=2 in x+3`. Explain why parsing success alone does not guarantee correct evaluation; identify the stages and expected outcome.

**Set up definitions and premises**
The scanner produces tokens for let, identifier x, equals, integer two, in, x, plus and three. The parser builds a declaration whose body is an addition. The grammar specifies the valid arrangement but not the binding location or numeric semantics.

**Derive the result**
The resolver maps the x use to the declaration. Under ordinary lexical semantics the environment maps x to a location with value two, and integer addition combines two and three. A static type checker can establish that both operands are integers.

**Validate limits and interpretation**
The interpreter returns five. Construct `let x=true in x+3`: it may parse to the same syntactic form while failing a static type rule. Construct an unbound identifier to demonstrate name resolution failure. Therefore the syntactic language is wider than the set of semantically accepted executions.

**Answer:** Result 5 for the original expression under stated integer semantics; parsing, binding, typing and evaluation must be checked separately.

### Worked question: Scope shadowing
Compute `let a=8 in let b=3 in let a=2 in a+b`; draw the binding chain and explain which a is used.

**Set up definitions and premises**
Label the outer a as declaration A0, b as B1 and inner a as A2. Their associated values are 8, 3 and 2. Names alone are not enough to identify declarations; a nested environment or lexical address is needed.

**Derive the result**
Lookup a from the innermost environment finds A2 first, so its value is two. Lookup b first misses the innermost environment but finds B1 in its parent. The value of A0 stays eight and is shadowed rather than overwritten.

**Validate limits and interpretation**
Compute 2+3=5. Rename A0 to q and verify that the result remains five. Rename A2 to q without changing its use and a now resolves to A0; this changes the result to eleven and illustrates why consistent binding-aware renaming matters.

**Answer:** The expression evaluates to 5; shadowing changes lookup identity without modifying the outer value.

### Worked question: Evaluation cost and effects
A function `twice(x)=x+x` receives an expression g() that prints once per evaluation and returns four. Compare call-by-value, call-by-name and call-by-need.

**Set up definitions and premises**
In call-by-value g is evaluated before calling twice. Its result four is bound to x, and two reads of x do not reexecute g. One print occurs, and the result is eight.

**Derive the result**
In call-by-name x denotes the unevaluated argument expression. Each use re-evaluates g, so two prints occur under the simplified semantics. In call-by-need the argument is represented by a memoizing thunk: the first use prints once and caches four, and the second use reads the cache.

**Validate limits and interpretation**
All strategies return eight in this example, but the side-effect traces differ. If g throws or never terminates and x is unused, strict and non-strict evaluation can differ even in termination. The language contract must specify which traces are permitted.

**Answer:** Value 8 in all three cases; print counts 1, 2, and 1 respectively under the stated conventions.
