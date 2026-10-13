# Draft review checkpoint

This is an internal critical review of saved Units 1–4, not independent expert peer review, full-book QA or publication approval.

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

## Unresolved work

- Units 5–10 are not yet drafted at this checkpoint.
- No simulations are implemented or tested yet. Planned simulations are design notes only.
- Reader assembly, equation rendering, mobile controls, static pages, search metadata, preservation checks, sitemap and live verification remain unperformed for this book.
- Complete-book repetition, coverage and substantive academic review must be conducted after assembly. Neither finite arithmetic checks nor this partial review count as completed-book acceptance.
- Publication is blocked. Keep all drafts outside COURSE_DATA, public catalog and sitemap until the full book passes.
