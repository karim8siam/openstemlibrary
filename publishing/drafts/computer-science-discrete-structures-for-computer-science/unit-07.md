# Unit 7: Algebraic structures


## Modular Arithmetic

**Core model — Modular Arithmetic**

Modular arithmetic identifies integers with equal remainders modulo a positive m. Addition and multiplication respect congruence classes.

**Original worked illustration**

17 congruent to 2 mod 5, and 17*3 congruent to 6 congruent to 1 mod 5. This permits compact arithmetic in clock and hashing algorithms.

**Boundary conditions and checks**

Division modulo m is only valid by a factor with a multiplicative inverse, namely one coprime to m.

### Congruence is arithmetic on residue classes
Integers a and b are congruent modulo m>0 when m divides a−b. This is an equivalence relation, and each residue class has a representative among 0,...,m−1. Addition and multiplication respect congruence: if a≡b (mod m), then a+c≡b+c and ac≡bc (mod m). This property justifies doing arithmetic on reduced representatives. Division does not obey the same rule in general; canceling a factor requires that the factor have a multiplicative inverse modulo m.

### Worked inverse and congruence solution
To solve 7x≡1 (mod 26), use the extended Euclidean algorithm or inspection. Since 7×15=105=4×26+1, the inverse of 7 is 15 modulo 26. Multiplying both sides by 15 gives x≡15 (mod 26). More generally, ax≡b (mod m) has solutions exactly when gcd(a,m) divides b, with gcd(a,m) incongruent solution classes modulo m under the usual counting. For example, 6x≡9 (mod 15) has three solutions modulo 15 because gcd(6,15)=3 divides 9; reducing gives 2x≡3 (mod 5), so x≡4 (mod 5), represented by 4,9,14 modulo 15.

### Euclid's algorithm as a correctness proof
The greatest common divisor satisfies gcd(a,b)=gcd(b,a mod b) for b≠0. Any common divisor of a and b divides a−qb for each integer q, so it divides the remainder; the converse is immediate. Replacing (a,b) by (b,r) reduces the second nonnegative argument until zero, proving termination. At termination gcd(a,0)=|a|. This algorithm is essential for testing whether modular inverses exist and for simplifying rational or integer relationships.

### Chinese remainder construction
Suppose x≡2 (mod 3) and x≡3 (mod 5). Checking candidates 2,5,8,11,... modulo 3 shows 8≡3 (mod 5), so x≡8 (mod 15). Because 3 and 5 are coprime, every pair of residue conditions has a unique solution modulo 15. For noncoprime moduli, consistency requires their residues to agree modulo the greatest common divisor. The Chinese remainder theorem helps organize independent periodic constraints and underlies some multiprecision arithmetic techniques.

### Cryptographic caution
Modular exponentiation is a mathematical primitive, not by itself a secure encryption system. RSA-style security depends on key generation, padding schemes, attack models and implementation details beyond modular multiplication. Tiny moduli used in teaching demonstrations are trivially breakable and must never be deployed for real secrets. Clearly separate demonstrating congruences from claiming to have built a secure cryptosystem.



## Groups

**Core model — Groups**

A group comprises a set and an associative operation with identity and inverses. Commutativity is an additional condition defining an abelian group.

**Original worked illustration**

Integers with addition form an abelian group: identity 0, inverse of a is -a, and integer addition is associative.

**Boundary conditions and checks**

Natural numbers under addition lack additive inverses within the set and therefore do not form a group.

### Algebraic structures abstract operations
A group consists of a set G and one binary operation satisfying closure, associativity, existence of an identity, and an inverse for each element. The integers under addition form a group: zero is the identity and −a is the inverse of a. The nonzero integers under multiplication do not form a group because, for example, 2 has no integer multiplicative inverse. The definition distinguishes a mathematical object from an implementation: merely exposing a function named multiply does not establish the axioms.

### A finite cyclic group
Under addition modulo 6, the elements {0,1,2,3,4,5} form a group. The identity is 0, and each element a has inverse 6−a modulo 6. Starting from 1 and repeatedly adding 1 visits all six elements, so 1 generates the group. Starting from 2 visits {0,2,4}, a subgroup of order three. The order of an element is the least positive k for which repeating the operation k times yields the identity. In this example, 2 has order three, not six.

### Homomorphisms preserve structure
A group homomorphism h:G→H satisfies h(a⋆b)=h(a)◇h(b) for all a,b, where the two operation symbols may differ. For the map h:Z→Z/5Z sending an integer to its residue, h(a+b)=h(a)+h(b) modulo 5. The kernel consists of multiples of five, which all map to zero. The image consists of all five residue classes. Kernel and image are not arbitrary bookkeeping sets: their algebraic properties reveal what information the map forgets and which target states it can represent.

### Symmetry and permutations
The permutations of three labeled objects form the symmetric group S3 under composition. There are 3!=6 elements, and composition is generally not commutative. For example, swapping positions 1 and 2 and then swapping positions 2 and 3 yields a different permutation than performing those swaps in reverse order. This is why transformations in graphics, robotics and data pipelines may depend on operation order. A group-based model can prove reversibility of composite actions when each component action has an inverse.

### Beyond groups
A monoid needs an associative operation and identity but does not require inverses. Strings under concatenation form a monoid with the empty string as identity; ordinary strings generally lack inverses under concatenation. Many parallel reduction and fold operations exploit associativity so that data chunks can be combined in different parenthesizations while preserving the result. The operation must truly be associative in its implemented arithmetic; floating-point addition is not exactly associative due to rounding, which can make parallel reductions differ slightly from sequential ones.



## Finite Fields

**Core model — Finite Fields**

A finite field has operations addition and multiplication satisfying field axioms; every nonzero element has a multiplicative inverse. Prime-modulus integers form a field.

**Original worked illustration**

In F7, 3*5=15 congruent 1, so 5 is the multiplicative inverse of 3. By contrast modulo 8, 2 is a zero divisor.

**Boundary conditions and checks**

Z/mZ is a field precisely when m is prime; moduli that are composite do not meet the field axioms.

### Finite fields are not arbitrary modular rings
A field supports addition, subtraction, multiplication and division by every nonzero element according to the field axioms. The residues Z/pZ form a field when p is prime because every nonzero residue has a multiplicative inverse. Modulo 6 this fails: 2×3≡0 even though neither factor is zero, so division by nonzero elements cannot always be defined. Modulo 7, by contrast, the inverse of 3 is 5 because 3×5=15≡1 (mod 7).

### Polynomial arithmetic over a base field
A field with 2^m elements can be constructed by representing field elements as polynomials over GF(2) of degree less than m and reducing products modulo an irreducible polynomial of degree m. For GF(2^3), one may use f(x)=x³+x+1, which is irreducible over GF(2). The polynomial x represents a field element; multiplying x² by x gives x³, and reduction by f(x)=0 yields x³=x+1 because subtraction and addition coincide in characteristic two. The resulting arithmetic is not ordinary integer arithmetic modulo 8: the element representation and reduction polynomial determine the multiplication rule.

### Why irreducibility matters
If the reduction polynomial factors, the quotient ring contains zero divisors, preventing multiplicative inverses for some nonzero elements. Over GF(2), a degree-three polynomial is irreducible exactly when it has no root in GF(2). For x³+x+1, evaluating at zero yields one and evaluating at one yields 1+1+1=1 modulo two, so it has no root and is irreducible. This short argument works for degree two or three, but higher degrees may require more involved irreducibility tests.

### Connection to error-correcting codes
Reed–Solomon codes evaluate polynomials over finite fields at distinct field points. A degree less than k polynomial has at most k−1 roots unless it is the zero polynomial. Consequently two distinct low-degree polynomials cannot agree on too many evaluation points; this supplies the distance property needed for error detection and correction. The argument requires a genuine field and enough distinct evaluation points. A toy field with seven elements cannot supply dozens of distinct evaluation coordinates without extension or a different construction.

### Test vectors and mistakes
For arithmetic modulo 7, verify closure, identities, inverses of 1 through 6, distributivity and the zero-product rule on all bounded operands. For a GF(2^3) implementation, test carryless polynomial multiplication followed by reduction, not ordinary modulo-eight multiplication. Add a zero-division check and verify that all seven nonzero elements have inverses. Exhaustive verification of a small field is practical and makes a strong complement to the axiomatic proof.



## Computational Applications

**Core model — Computational Applications**

Discrete algebra underpins checksum constructions, cyclic codes, cryptographic groups and modular indexing. Security depends on complete algorithm and threat assumptions, not only on choosing a large modulus.

**Original worked illustration**

A checksum of data [2,4,6] modulo 7 is (2+4+6) mod 7=5. Changing a byte can change the checksum, allowing some corruption to be detected.

**Boundary conditions and checks**

A simple modular checksum is not a cryptographic authentication tag and cannot resist intentional forgery.

### Algebra can improve an algorithm's structure
Many computational operations form monoids, groups or semirings. A semiring has addition and multiplication-like operations satisfying appropriate associativity, distributivity and identity conditions; ordinary nonnegative integers with + and × form a familiar example. Boolean reachability can be computed using a Boolean semiring where logical OR acts as addition and logical AND as multiplication. Matrix multiplication over this semiring summarizes whether any intermediate vertex connects two graph vertices. This is algebra applied directly to an algorithmic problem.

### Hashing and modular residues
A basic rolling hash for a string of character codes c0,...,c_{n−1} may compute h=Σ ci B^{n−1−i} mod p. Appending a character c updates h to (Bh+c) mod p in constant time. A prime modulus can simplify some algebraic properties, but two different strings can still collide because infinitely many strings map to only p hash values. Equality of hashes is evidence useful for lookup or filtering, not proof of identical content. Collision resistance against adversaries needs a cryptographic construction rather than a small classroom polynomial hash.

### Discrete transforms and cyclic convolution
For sequences indexed cyclically modulo n, convolution combines shifted products of entries. Algebraic transforms such as the discrete Fourier transform turn convolution into pointwise multiplication under suitable conventions. Over finite fields containing appropriate roots of unity, related number-theoretic transforms can compute exact integer-like convolutions without floating-point rounding. Preconditions on modulus, transform length, and root order matter; blindly substituting a modulus into a floating-point FFT implementation does not produce a valid finite-field transform.

### A checksum example
A simple checksum assigns weights w0,...,w_{m−1} to message digits d0,...,d_{m−1} and calculates Σ wi di modulo 11. A one-digit error by amount e in position j changes the checksum by wj e modulo 11. If wj is invertible and e is not a multiple of 11, the error is detected. This argument depends on digit range and arithmetic domain. A checksum detects some accidental errors; it is not a cryptographic message-authentication code, because an attacker who can alter both message and checksum can recompute it.

### Design discipline
When a data structure relies on associativity, specify the binary operation and verify its identity element. A segment tree can then combine interval summaries while permitting logarithmic-time updates and range queries. A segment tree storing interval sums uses + with identity zero; one storing minima uses min with identity positive infinity under an extended numerical model. Changing the aggregate from sum to average requires storing both sum and count, because average alone is not associative under naive averaging of unequal-sized groups.

### Extended laboratory: algebraic checks for a toy message system
A message system stores symbols 0 through 6 and combines checksums using addition modulo seven. The operation is associative, has identity zero, and every symbol has an additive inverse. For example, the inverse of 3 is 4 because 3+4≡0 mod 7. Thus the seven checksum states form a cyclic group under addition. If a programmer instead treats these states as ordinary integers and truncates values beyond six without taking modulo seven, the implementation no longer follows the declared group operation.

Suppose a message has symbols 2,4,6. Its additive checksum is (2+4+6) mod 7 =12 mod 7=5. If one symbol changes from 4 to 5, the checksum changes from 5 to 6. This detects that single substitution when the alteration is nonzero modulo seven. But swapping the first two symbols leaves a plain sum unchanged. This checksum does not detect every kind of corruption; it certainly does not authenticate the sender. Weighted-position checksums can detect additional alterations but introduce new assumptions about allowable positions and weights.

Now form a rolling polynomial hash h=(c0 B²+c1 B+c2) mod 7 with base B=3. For the same message, h=(2×9+4×3+6) mod 7=36 mod 7=1. Appending a fourth symbol c3=1 updates h'=(3h+1) mod 7=4. The operation uses the previously computed residue, avoiding recomputation from scratch. A collision is unavoidable for sufficiently many different messages because the output has only seven possible values. Any claim that distinct messages always receive unique hashes would violate the pigeonhole principle.

Consider affine transformations of residues x↦ax+b modulo seven. Such a transformation is bijective when a is nonzero modulo seven. For a=3,b=2, compute y=3x+2 mod 7. To recover x, subtract two and multiply by inverse(3)=5, yielding x=5(y−2) mod 7. For x=4, the forward map gives y=14 mod 7=0; the inverse gives x=5(−2) mod 7=−10 mod 7=4. This concrete verification demonstrates invertibility of a simple modular map, not security of an encryption algorithm.

Extend the idea to GF(2^3) with polynomial representation. Let f(t)=t³+t+1 and represent each element by a polynomial of degree at most two with coefficients zero or one. To multiply t² by t, obtain t³, then reduce f(t)=0 to t³=t+1. Addition is XOR of coefficient vectors, whereas multiplication involves polynomial multiplication followed by reduction. Testing both operations on all eight elements is practical. Crucially, standard integer multiplication modulo eight gives different results and is not a substitute for this finite-field arithmetic.

Finite-field operations are useful in error-correcting codes. If two distinct polynomials of degree at most k−1 agree at k distinct field points, their difference is a nonzero polynomial with at least k roots, contradicting the root bound. Therefore k observations determine such a polynomial uniquely. This mathematical fact motivates polynomial evaluation codes but does not specify a deployed coding scheme's frame format, error model or decoder behavior.

An experimental test harness should verify closure (every output remains between zero and six for modulo-seven arithmetic), identities, inverse correctness and distributivity, and should reject division by zero. For modular exponentiation, compare fast repeated squaring against ordinary repeated multiplication at small exponents. For an affine transform, loop over all seven inputs and assert seven distinct outputs when a is invertible. Exhaustive small-domain checks provide powerful diagnostic evidence while the axiomatic proofs establish the general properties of the mathematical structures.

### Experiment card: modular inverses and fast exponentiation
The first algebra model returns the multiplicative inverse of input n modulo the prime thirteen, for 1≤n≤12. Verify that the returned value r satisfies (n×r) mod 13=1. Examples: the inverse of 1 is 1, inverse of 2 is 7 because 14≡1, and inverse of 12 is 12 because 144≡1 modulo thirteen. Every supported input is coprime to the modulus, so an inverse exists. If the slider were extended to n=13, its residue would be zero, which has no inverse; therefore the endpoint is a meaningful mathematical restriction.

The separate model computes 3^n modulo seventeen by repeated squaring. For n=1 the answer is three. For n=2 it is nine. For n=3 it is twenty-seven modulo seventeen, or ten. The algorithm maintains an accumulator and a current power of three; whenever the current exponent bit is one, it multiplies the accumulator by that power modulo seventeen. Squaring the current power and halving the exponent progresses through all binary exponent digits. The invariant is that the accumulated product times the current base raised to the remaining exponent equals the original 3^n modulo seventeen.

Test the fast algorithm against a deliberately simpler oracle that multiplies by three exactly n times and reduces modulo seventeen after each step. The two implementations use different control structures, making it less likely that they share the same coding mistake. Because n≤12, both use exact small integers. The fast method requires O(log n) modular multiplications in the exponent length, whereas the repeated-multiplication oracle uses O(n); that cost difference is not significant for the toy domain but is the reason to teach the faster technique.

Do not label these models as cryptographic key tools. A prime modulus of thirteen or seventeen is deliberately tiny and offers no security. Their educational value is the exact group and field arithmetic that can be checked completely by hand. A production cryptographic implementation requires secure parameter sizes, constant-time behavior where appropriate, formal protocol design and many other properties not supplied by a slider that outputs modular residues.



## Fully worked questions

### Question 1: Modular Arithmetic: worked application 1

Compute 17×3 modulo 5.


**Set up the model and conditions:** Reduce 17 to residue 2 modulo 5.


**Carry out the calculation or proof:** Multiply residues: 2×3=6, then reduce 6 mod 5.


**State the result and its scope:** The result is 1.


**Independent reasoning check and edge conditions:** Compute the ordinary product 17×3=51. Divide by five: 51=10×5+1. The remainder is therefore one, and 17×3≡1 (mod 5). An equivalent method reduces 17≡2 and 3≡3, multiplies 2×3=6, then reduces 6≡1. The agreement illustrates compatibility of congruence with multiplication. The modulus must be positive when using the stated standard remainder convention. This exercise alone makes no statement about multiplicative inverses of 17 modulo five, although it happens to be invertible.


**Answer:** The result is 1.


### Question 2: Groups: worked application 2

Find the multiplicative inverse of 3 modulo 7.


**Set up the model and conditions:** Test nonzero residues or use extended Euclid; 3×5=15.


**Carry out the calculation or proof:** Since 15 mod 7=1, residue 5 is an inverse.


**State the result and its scope:** The inverse of 3 in F7 is 5.


**Independent reasoning check and edge conditions:** An inverse of a residue a modulo seven is a residue b satisfying ab≡1 (mod 7). Test 3×5=15=2×7+1, so 5 is an inverse. Because seven is prime and three is nonzero modulo seven, an inverse is guaranteed to exist and is unique as a residue class. Testing 3×5 in ordinary arithmetic without reducing modulo seven would not reveal the correct definition. In modulus six, the element three would have no inverse because its greatest common divisor with six is not one.


**Answer:** The inverse of 3 in F7 is 5.


### Question 3: Finite Fields: worked application 3

Show why integers under addition form a group.


**Set up the model and conditions:** Addition is associative; zero is an identity.


**Carry out the calculation or proof:** Every integer a has additive inverse −a within Z.


**State the result and its scope:** All group axioms hold, and addition also commutes.


**Independent reasoning check and edge conditions:** The binary operation is integer addition, which is closed on Z: a+b remains an integer. It is associative because (a+b)+c=a+(b+c). Zero is an identity: a+0=0+a=a. Every integer a has additive inverse −a because a+(−a)=0. These four properties establish a group; commutativity a+b=b+a further makes it an abelian group. The argument concerns Z under addition, not under multiplication, where most nonzero integers lack inverses inside Z. The distinction between the set and the operation is indispensable.


**Answer:** All group axioms hold, and addition also commutes.

