# Unit 2: Type systems

*Draft; not approved for public deployment. Eight-unit manuscript with source-specific cases and independent verification pending.*

## Type Checking
**Type Checking: conceptual explanation**

Static typing is often expressed by judgments of the form `Gamma |- e : T`. Gamma is a finite environment assigning types to variables, not a dictionary of their current numeric values. A judgment for integer addition requires that both operands have integer type and concludes that the resulting expression has integer type. For an if expression, a standard formulation requires a Boolean condition and branch expressions of compatible type. A typing derivation is a tree: its leaves are assumptions or literal typing rules, while inner nodes apply rules for composite constructs. Writing the rule precisely reveals whether implicit conversions, overloaded operators or bottom types are permitted.

Typing rules should be separated from parsing and runtime checking. `3 + true` may be a syntactically valid AST yet fail static checking; an array access may type-check with an integer index but fail at runtime if the index is out of bounds. In a language with gradual typing, a dynamic boundary inserts a runtime cast that can fail, and the error needs an informative blame location. An implementation should report two independent errors without corrupting the symbol environment, but careless error recovery may cascade hundreds of misleading diagnoses. Design type-checking tests from each rule, including wrong arity, shadowing, operator precedence and a conditional whose branches disagree. Sound diagnostics state expected and actual types and point to the smallest responsible source span.

### Design investigation: a derivation that exposes failure
Write typing judgments for integer and Boolean literals, addition, variables, functions and application. Derive the type of `lambda n:Int. n+1` and show the rule application tree with Gamma extended by n:Int. Apply the function to Boolean true and identify the exact failed premise: argument type Bool does not equal Int unless the language explicitly defines a compatible conversion. Now add a dynamic type and specify whether a boundary cast happens at compile time or runtime. Distinguish wrong-argument-type rejection from an array index error, which need not be statically ruled out by a plain Int index type. Generate tests that cover one positive and one negative example for every typing rule. A diagnostics test should compare not only whether compilation fails but also whether the error refers to the correct source expression. Explain how poisoned error nodes can prevent twenty misleading cascades from one bad operand.

## Polymorphism
**Polymorphism: conceptual explanation**

Parametric polymorphism gives code a uniform behavior independent of particular represented element types, subject to the language’s type rules. For a function `length : List[A] -> Int`, instantiating A with String or Boolean changes the container element type but not the algorithm used to count nodes. Generic identity `id : A -> A` should preserve its input’s type and value. In contrast, ad hoc polymorphism such as overloaded `+` selects different operations for integers, floating-point values or vectors. Subtype polymorphism relies on substitutability and dynamic or static dispatch; it is not identical to parametric polymorphism.

A type parameter may have bounds: `sort : List[A] -> List[A]` requires a comparison operation or comparator rather than working for arbitrary A. Different implementation strategies impose costs. Monomorphization can generate specialized machine code for each needed instantiation, potentially improving execution while increasing binary size. Dictionary passing carries operations such as equality at runtime. Type erasure can reduce duplicated code but may constrain reflection or representation. Show the generated function signature and runtime representation for each strategy before making speed claims. A polymorphic API must also specify variance. A mutable list of cats cannot safely be treated as a mutable list of arbitrary animals if someone can insert a dog; read-only views and immutable interfaces admit different variance rules.

### Design investigation: API representation and variance
Implement a generic immutable List interface containing `map`, `length`, and `headOption`. Instantiate List[Int] and List[String]. Record which methods require any knowledge of element representation and which ones need a supplied operation or type witness. Try making a mutable List[Cat] a subtype of mutable List[Animal]; inserting a Dog through the wider reference should demonstrate why unrestricted covariance is unsafe. Repeat the thought experiment for a read-only list whose only operations return existing elements; safe covariance may then be possible depending on language rules. Sketch how monomorphization and type erasure would compile `length`. For a heavily used numeric function, specialized code might remove boxing; for an application with many type instantiations it may increase code size. Neither tradeoff is resolved from the generic type signature alone. Identify a semantic regression test, a generated-code inspection, and an empirical performance measurement separately.

## Inference
**Inference: conceptual explanation**

Hindley–Milner style inference is best learned through explicit type constraints. For a lambda `lambda f. lambda x. f(x)`, assign fresh unknowns alpha to x and beta to f's result; function application requires f to have type alpha -> beta. The inferred function type is `(alpha -> beta) -> alpha -> beta`. In let-polymorphic systems a let-bound identity function may be instantiated independently at several use sites, whereas lambda-bound variables are commonly monomorphic within an inference context. This distinction prevents erroneous acceptance of self-application in a simply typed calculus.

Unification solves equalities between type terms. Decompose `List[alpha] = List[Int]` into alpha = Int, but reject `alpha = List[alpha]` under ordinary finite-tree typing because it violates the occurs check. A unifier records substitutions and applies them transitively: if alpha = beta and beta = Int, both resolve to Int. Build a small implementation that assigns fresh variables, gathers constraints by AST traversal, checks occurs, and reports an explanation chain on failure. Inference is not a substitute for a language specification; overloaded numerical literals, coercions, effects, row polymorphism and higher-rank types can require annotations or more sophisticated constraint systems. A type hole may expose the constraints it could satisfy and become a learning tool rather than an unexplained compiler rejection.

### Design investigation: unification with an occurs check
Infer the type of `lambda f. lambda x. f(x)` by creating fresh variables alpha and beta. Write application constraint `type(f)=alpha->beta`; resolve to `(alpha->beta)->alpha->beta`. Then attempt `lambda x. x(x)`. Application requires type(x)=type(x)->result, which is an infinite equation under finite simple types. Make your occurs-check routine reject it and print the originating AST span. Solve `List[a]=List[Int]`, `(a->b)=(Int->Bool)`, and `Pair[a,b]=Pair[Int,String]` as positive tests. Introduce substitution chains a=b, b=c, c=Int and confirm that substitutions are normalized consistently. To expose order-dependent bugs, permute the order of constraints and compare resulting principal types modulo renaming of type variables. Explain why a wrong occurs check can lead to cyclic internal type objects and a crash much later in code generation, rather than a useful diagnostic near the source.

## Soundness
**Soundness: conceptual explanation**

Type soundness is typically a theorem about a specific formal language. Progress says that a closed well-typed term is a value or can take a reduction step. Preservation says that if a well-typed term takes a step, the resulting term retains its type under appropriately updated environments. Proving both prevents a large class of stuck states, but the theorem does not mean every program succeeds: division by zero, resource exhaustion or an explicitly allowed exception may remain possible. A language’s dynamic checks, heap typing, and exception states must be part of the theorem’s formal account.

For a simply typed arithmetic language, prove preservation by induction on the transition derivation. The arithmetic reduction case uses the typing premises of both operands; the congruence cases use the induction hypothesis. Add mutable references and the proof requires a store typing invariant describing which location contains which type. Add unsafe casts or foreign calls and the soundness claim may need to exclude those operations or specify a checked boundary. A testing suite cannot prove preservation over an infinite syntax space, but property-based generation can find gaps in the rules and implementation. When a compiler changes representation, distinguish sound source typing from preservation of source semantics through lowering and optimization.

### Design investigation: proof boundary versus test boundary
State progress and preservation for a simple typed arithmetic calculus. Prove the case `3+4` evaluates to an integer seven, and identify the typing premises used in the argument. Add a conditional that chooses between two integer expressions and explain why typing both branches avoids a result-type mismatch. Now extend the language with `head` on lists and apply it to the empty list. If the language permits a runtime exception, show why “well typed” does not automatically mean “returns a normal value.” Write the progress theorem so a permitted exception step or exception value is accounted for explicitly. Add references and point out the missing store-typing invariant in the earlier proof. Produce one deliberately broken operational rule that returns a Boolean from integer addition; a property-based test should identify a preservation failure. Explain what the proof establishes for the model and what compiler implementation bugs still require separate validation.

## Integrated Case Study and Model Limitations
An expression `head([])` can be well typed in a language whose list-head operation returns an element type but throws on empty input. Type soundness does not imply absence of all runtime errors unless the language's typing rules exclude such operations or model exceptions as permitted outcomes. For a polymorphic identity function, show why `id(3)` and `id("a")` can share an implementation while a numeric addition function cannot accept arbitrary types. In an inference exercise, unify type variables from `f(x)` constraints and explain when incompatible equalities should cause rejection.

### Laboratory: build a typing derivation and challenge it

Define a typed expression language with integers, booleans, pairs, functions and `let`. Give every construct a typing rule using a context Gamma. Literals infer their base types. A function literal introduces a parameter binding in a copied context; its body determines the result type. Function application requires the callee to have a function type whose argument matches the supplied expression. A pair has product type, and projections return the corresponding component. Distinguish a type-checking environment from the runtime environment used by the interpreter; a declared type does not tell you the value of a variable.

Derive a type for `let id = lambda x. x in (id(3), id(true))`. Under a let-polymorphic system, id receives type schema forall alpha. alpha -> alpha. The first application instantiates alpha to Int, while the second independently instantiates it to Bool, producing pair type `(Int,Bool)`. Under a monomorphic alternative the same code may be rejected. Record both systems precisely rather than describing one as inherently correct. Now examine `lambda f. f(f)`: unification leads to an occurs-check problem under standard simple types because a type variable would need to contain itself as a function type. A language with explicit recursive types changes the design; it does not excuse skipping the check in a finite-tree implementation.

Implement constraint generation from an AST. Every node gets a fresh type variable or a type known by rule. Generate equations for application and conditionals. Solve equations by unification with substitution composition, keeping the original source span of each constraint. For a failure such as `3 + true`, the diagnostic should identify the conflicting expected Int and actual Bool at the addition operand, not just report a generic “unification failed.” A constraints log allows a reviewer to reproduce each inferred type. Include a test for nested shadowing that verifies a local variable’s type does not mutate a differently scoped binding.

To reason about soundness, specify a simple small-step relation and prove one progress case and one preservation case. An integer addition with two integer literal operands steps to an integer; an application of a lambda to a value steps by substitution or environment extension and must preserve declared parameter type. The substitution lemma carries much of this proof. Adding references makes the proof longer because a store typing relation must track allocated locations. Say exactly which features your theorem covers. Do not call the implementation sound merely because it passes ordinary examples.

Build a property-based test generator that creates well-typed expressions from expected types rather than generating arbitrary strings and filtering afterward. Use bounded recursion depth and fuel. For each generated program, assert that the interpreter either returns a value of the expected type or produces a specifically permitted runtime condition such as fuel exhaustion. Inject a deliberately broken rule allowing a Boolean as the operand of integer addition. The generator should then discover a term that gets stuck. Save the minimized failing term, the inference trace, and the corrected rule. This lab contrasts mathematical guarantees, algorithmic implementation, and finite testing evidence.

### Failure clinic: polymorphic API accepted unsafely

A team publishes a mutable generic container, chooses covariance for convenience, and later adds a new subtype. Their demo passes because it only reads values. A client obtains a `List[Cat]` through a wider `List[Animal]` reference and inserts a Dog. The original caller then assumes every element is a Cat and calls a cat-only method. If the type checker accepted the program without a protective runtime check or restricted interface, the variance rule has violated its intended guarantee. Diagnose whether the API is mutable, whether the language enforces runtime store checks, and whether the subtype relation is actually declared for mutable containers. Immutable read-only containers have different safe variance conditions.

Write two alternative API designs. Invariant MutableList[A] rejects the dangerous assignment statically. A covariant ReadOnlyList[+A] offers safe observation methods without accepting arbitrary Animal elements into a list of Cats. In some languages a built-in array type is covariant with dynamic store checking, but this moves the potential failure to runtime rather than erasing it. Compare programmer ergonomics, static guarantees, dispatch overhead and generated representation without making unsupported absolute performance claims.

The same project has a type inference bug. The implementation omits the occurs check and assigns alpha = List[alpha] while analyzing a recursive-looking generic use. Its internal type graph becomes cyclic, and an unrelated error-reporting formatter overflows its recursion stack. Add a unification test that attempts to bind a variable to a type term containing itself. A correct finite-tree implementation rejects the equation at the point where it arises, preserving a useful source span. Testing only successful generic calls would not expose the defect.

Finally distinguish type safety from product reliability. The application can have type-sound source programs and still crash from exhausted memory, intentional exceptions or foreign code that violates the runtime boundary. State which constructs are included in the proof and which are entrusted to dynamic checks. A test suite should include invalid casts, API variance, monomorphic lambda bindings, let-polymorphism and FFI error behavior. The objective is to identify exactly where a guarantee comes from, rather than attaching a vague “safe language” label to the entire application.

### Worked comparative study: static soundness versus useful expressiveness

A language designer might reject every expression that the checker cannot prove safe. This yields a conservative system, but it may make ordinary programs difficult to express. Consider a list lookup. A type signature `get : List[A] × Int -> A` describes the element type, but it does not prove that every integer index lies inside the list. A checker could use a richer dependent type requiring a proof that `0 <= index < length`, or the runtime could perform a bounds check and return an option or throw a specified exception. Neither approach is universally superior: the design determines annotation burden, ergonomics, runtime overhead and guarantees. The important academic distinction is between an invariant the checker establishes and a condition the runtime enforces.

Refinement types can express predicates such as an integer strictly greater than zero. Suppose a function divides by a denominator typed `PositiveInt`. If values of this type can only be constructed through a checked operation, the division-by-zero case can be excluded from that function's valid inputs. However, the guarantee depends on hiding unsafe constructors and maintaining the predicate through mutation, serialization and foreign input. A compiler may need a constraint solver and a graceful policy when it cannot prove a predicate. “Unknown” should not silently become “true.”

Contrast explicit type annotations with inference. An annotation can improve error localization and API communication; inference can reduce boilerplate. In a modular system, separate compilation may require public type signatures even when local terms can be inferred. More powerful type systems introduce harder questions: termination of inference, decidable checking, higher-rank quantifiers, variance, effects and module abstractions. A classroom implementation should be clear about the subset supported rather than suggesting that Hindley–Milner inference automatically covers every feature of modern languages.

Create a design table for a checked division function, a list-head function and a user-provided callback. For each, record compile-time checks, runtime checks, possible failures, error signaling and caller obligations. Then generate tests at valid and invalid boundaries. A proof that well-typed terms do not get stuck under an idealized formal semantics does not automatically prove that generated machine code preserves it. Separate source typing, compiler correctness, runtime representation invariants and FFI boundary checks as four distinct engineering responsibilities.

### Unit review: make type judgments falsifiable

Choose one rule from the type checker and attempt to construct the smallest program that would be accepted if a premise were accidentally omitted. For function application remove the argument-type equality check; for unification omit occurs checking; for polymorphism generalize a mutable reference unsafely. Trace the implementation until it produces an ill-typed value or an internal contradiction. This is a mutation test for the static semantics, not a statement that a soundness theorem has already been proven. Verify separately that error messages retain source locations and describe actual versus expected types. A type system should distinguish ordinary dynamic checks, intentionally unsafe operations and code whose static type is genuinely sufficient to rule out a bad state. The boundary of the guarantee is part of the educational result.

### Worked question: Construct a typing derivation
For `lambda x:Int. x+1`, derive the function type and explain which premise rejects applying it to Boolean true.

**Set up definitions and premises**
Extend Gamma with x:Int. The variable rule gives Gamma,x:Int |- x:Int, and the literal rule gives 1:Int. Integer-addition typing requires two Int operands; therefore Gamma,x:Int |- x+1:Int.

**Derive the result**
Apply the lambda rule: Gamma |- lambda x:Int. x+1 : Int -> Int. For application to true, the function requires an Int argument but the literal true has type Bool. In a simply typed language with no implicit coercions, the application rule premise fails.

**Validate limits and interpretation**
A successful application to 3 evaluates to 4. Typing the function does not establish that every integer computation terminates or avoids explicit runtime exceptions; those questions belong to language semantics and additional proofs.

**Answer:** Function type Int -> Int; passing true is a static type error without a defined conversion.

### Worked question: Unification constraints
Unify `(a -> List[b])` with `(Int -> List[Bool])`, then explain what happens for `a=List[a]`.

**Set up definitions and premises**
Decompose equality of arrow constructors: parameter types require a=Int and result types require List[b]=List[Bool]. Decompose equal List constructors to obtain b=Bool.

**Derive the result**
Compose substitutions consistently: apply a->Int and b->Bool to the original type and obtain Int -> List[Bool] on both sides. This is a finite substitution and satisfies every constraint.

**Validate limits and interpretation**
For a=List[a], the type variable a occurs inside the term to which it would be bound. Ordinary finite Hindley–Milner type inference rejects this via the occurs check. Omitting the check can produce an internal cycle rather than a principal finite type.

**Answer:** Substitution {a:Int,b:Bool}; the self-containing equation fails the finite-tree occurs check.

### Worked question: Progress and preservation
Show one progress and preservation step for typed integer addition; explain why this does not mean that all well-typed programs return normally.

**Set up definitions and premises**
Take a closed expression 2+5. Typing rules classify both literals as Int and their addition as Int. The operational rule computes a value seven, so the expression can take a step rather than being stuck.

**Derive the result**
Preservation holds in this case because the result seven is also an integer literal of type Int. A full theorem requires induction across every operational and typing rule, including contexts, stores and exceptions when those features are included.

**Validate limits and interpretation**
A typed program can explicitly throw an exception, run forever, exhaust memory or perform a permitted bounds check that fails. A soundness theorem must specify the allowed terminal states and exception steps; it is not a universal total-correctness proof.

**Answer:** The example steps from 2+5:Int to 7:Int; progress/preservation have precise formal scope.
