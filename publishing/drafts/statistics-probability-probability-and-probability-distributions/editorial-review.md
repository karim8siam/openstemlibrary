# Draft review checkpoint

This is an internal critical review of saved Units 1–7, not independent expert peer review, full-book QA or publication approval.

## Unit 1

- Checked the sequence from experiment and sample space through event algebra, axioms, counting and independence against the active outline. All planned Unit 1 topics have draft treatment; the full curriculum has not yet been covered.
- Checked complement universes, inclusive versus exclusive union, disjointness versus independence, finite equal-weight assumptions, zero-probability events, and countable continuity. The sigma-algebra explanation intentionally limits scope to finite models and ordinary measurable measurement sets.
- Recomputed all three worked questions with independently encoded finite enumeration or exact linear-system elimination in `check-draft.py`. All 18 checks passed. The calculation methods and exact outputs are retained in `draft-checks.json`.
- Review clarified that existence of a valid eight-region model does not establish empirical accuracy, and pairwise independence does not establish mutual independence. Those limitations appear in the solutions.
- Original problems use labeled student selection, an invented overlap model and a parity counterexample. The parity construction is a standard mathematical example; its explanation is original. No source text or source problems were copied.

## Unit 2

- Checked positive-probability conditioning, the full-history chain rule, composite-complement likelihoods, partitions, ordinary and conditional independence, and the difference between conditioning and causation.
- Recomputed source updates using an exact integer population, urn questions by enumeration of all labeled paths, and shared-condition results through a full rational joint table. Outputs are saved by the same executable checker; this verifies the stipulated models, not any real production data.
- Checked the no-flag posterior and odds conversion separately. The unmarked third-draw condition is distinguished explicitly from conditioning on the complete three-draw composition.
- Current examples contain no real medical, financial or legal recommendations. All source rates and operating conditions are stated teaching assumptions.
- Unit 2 currently has 5,188 conservative prose words against an outline planning target of 6,000. The book-wide 50,000-word minimum remains mandatory. A per-unit target is a planning guide, not a pass claim; later expansion must add useful substance if the complete draft falls short.

## Unit 3

- Reviewed discrete versus absolutely continuous and mixed distributions, right-continuous CDFs, endpoint atoms, quantile conventions, and one-to-one versus many-to-one transformations.
- Recomputed the discrete transformation by aggregating the original rational masses, the triangular law through exact piecewise trapezoid integration and numerical quantile inversion, and the square transformation through original-space interval lengths and CDF differentiation checks.
- Checked the asymmetric square-transform support: both inverse branches contribute below one, but only the negative branch contributes above one. Its boundary singularity is integrable and is not a point mass.
- Added substantive sections on recording transformations, clipping atoms, CDF comparisons and generalized-inverse sampling. These sections are instructional supplements to the mapped random-variable scope.
- Unit 3 has 5,584 conservative prose words and three solved questions. No interactive simulation has yet been implemented.

## Unit 4

- Reviewed joint and marginal support, discrete column normalization, continuous conditional-density construction, expectation existence, linearity without independence, covariance versus dependence, and within/between decomposition.
- Independently recalculated the finite joint-table and mixture questions by exact centered weighted sums and full pair tables. Integrated the original triangular region numerically in nested coordinates rather than relying on the published marginal answers.
- Checked both region probabilities in the triangular question, including the change of bound at one half and the curved boundary. Tested three conditional slices by integration.
- Added convolution and nonlinear conditional-averaging sections to give further substantive treatment of functions of random variables and expectation products.
- Every drafted unit contains exactly three solved questions. The conservative counter now also removes repeated question/solution labels; the canonical current measurements are in `draft-checks.json`. Earlier counts in this narrative describe earlier counter versions and are superseded by that artifact.

## Unit 5

- Checked raw/central moment formulas, moment existence conditions, PGF factorial-versus-raw derivatives, MGF domains, independent-sum rules and the first four cumulant relations.
- Independently computed cumulants from exact truncated formal logarithm coefficients rather than substituting the printed identities. Enumerated all sixteen binary trial paths for the count problem. Numerically integrated four positive polynomial moments in the supplied transformed-normal example.
- Reviewed the lognormal example's divergence analytically: for every positive transform argument, the exponent tends to positive infinity on the right tail. Finite truncation is not accepted as evidence of a finite MGF. The series-ratio argument separately shows divergence of the formal positive-argument moment series.
- Verified primary official teaching sources for MGF neighborhood/uniqueness conditions and characteristic-function existence/products; URLs and actual inspection scope are recorded in `references.json`.
- Factorial moments, joint transforms and moment-feasibility inequalities are substantive supplements to the mapped generator topic. The unit omits a standalone random animation because exact algebra and existence arguments are the useful learning activity here; this does not excuse simulations in the rest of the book.

## Unit 6

- Checked that binomial assumptions include fixed trial count, common success probability and mutual independence; Bernoulli margins alone are insufficient.
- Reviewed hypergeometric support, uniform-subset assumptions, covariance derivation and finite-population variance. The one-object case is handled separately to avoid division by zero.
- Independently enumerated all eight-trial binary paths, all 15,504 five-object subsets of the twenty-object collection, and all 924 six-object subsets of the twelve-object collection. Compared exact masses, direct tail sums, centered variances and proportion variances with every worked answer.
- Reviewed conditional-binomial/hypergeometric linkage and shared-probability mixture variance using the prior conditional-probability and total-variance results. Supplements explicitly distinguish fixed finite populations from random superpopulation marking.
- The sampling explorer is still a design specification, not an implemented/tested simulation. No publication or simulation pass is claimed.

## Unit 7

- Reviewed failures versus total-trial supports, positive success probability, strict versus nonstrict survival events, geometric memorylessness and the nonmemorylessness of a multiple-success wait.
- Independently enumerated full finite trial paths for the worked stopping events and conditional survival; checked waiting means/variances by direct long PMF summation.
- Recomputed Poisson thinning through a mixture over total counts and binomial allocations, rather than directly evaluating the claimed thinned law. Verified the fixed-total marking probability by binary-path enumeration.
- Reviewed rate-versus-interval parameter units, independent aggregation/marking assumptions, random-rate total variance, censoring versus completed observations and a bounded numerical-tail remainder.
- Geometric and negative-binomial moment formulas are justified analytically in the text. Finite numerical sums verify selected values only; they are not represented as proofs about all infinite-support cases.

## Bayes explorer prototype

- Implemented exact source/flag/posterior calculations, reproducible seeded sampling and a labeled DOM interface in `bayes-explorer.js`.
- `check-bayes.cjs` passed 21 numerical/model checks and 17 DOM interaction/accessibility checks. This includes invalid probabilities, zero-probability evidence, deterministic sampling, parameter changes, reset, labels, table semantics and unavailable sampled posteriors.
- Stored source/test hashes and actual results in `bayes-checks.json`. This is a prototype verification artifact, not a whole-book simulation pass.
- Reader integration and rendered mobile/keyboard testing are still required. Other proposed explorers are not implemented yet.

## Unresolved work

- Units 8–10 are not yet drafted at this checkpoint.
- One Bayes explorer prototype has numerical and DOM evidence; remaining explorers, reader integration and rendered browser/mobile tests are pending.
- Reader assembly, equation rendering, mobile controls, static pages, search metadata, preservation checks, sitemap and live verification remain unperformed for this book.
- Complete-book repetition, coverage and substantive academic review must be conducted after assembly. Neither finite arithmetic checks nor this partial review count as completed-book acceptance.
- Publication is blocked. Keep all drafts outside COURSE_DATA, public catalog and sitemap until the full book passes.
