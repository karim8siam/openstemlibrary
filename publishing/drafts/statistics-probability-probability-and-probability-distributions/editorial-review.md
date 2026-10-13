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

## Historical unresolved work at the 8 AM checkpoint

- Units 8–10 are not yet drafted at this checkpoint.
- One Bayes explorer prototype has numerical and DOM evidence; remaining explorers, reader integration and rendered browser/mobile tests are pending.
- Reader assembly, equation rendering, mobile controls, static pages, search metadata, preservation checks, sitemap and live verification remain unperformed for this book.
- Complete-book repetition, coverage and substantive academic review must be conducted after assembly. Neither finite arithmetic checks nor this partial review count as completed-book acceptance.
- Publication is blocked. Keep all drafts outside COURSE_DATA, public catalog and sitemap until the full book passes.


## Complete-book review, 13 October 2026

Units 8–10 are now authored. The earlier unresolved-work list describes the morning checkpoint and is superseded by the actual verification artifacts produced below. This remains an AI-assisted editorial and computational review, not independent academic peer review.

- Unit 8: reviewed support and endpoint conventions, density versus probability, uniform transformations, time-unit conversions, exponential memorylessness, gamma rate versus scale, gamma moment domains, independent common-rate stage assumptions, integer-shape survival, censoring/truncation, and mixtures. Independently integrated the transformed uniform law and recalculated all exponential/gamma solutions with SciPy. Confirmed the mean-remaining-time expression for gamma shape two by integrating its conditional survival.
- Unit 9: reviewed normal variance notation, Gaussian normalization/Jacobian reasoning, standardization, CDF versus tail tables, individual distribution intervals versus confidence intervals, affine and independent/jointly-normal closure, the zero-covariance counterexample, beta boundary integrability and mode conditions, moment ratios, concentration, rescaling, order-statistic and shared-parameter constructions. Exact polynomial integration and independent SciPy/matrix calculations verify the three worked solutions. NIST formulas were checked using consistent rate/scale conversion; no source prose was reproduced.
- Unit 10: reviewed support/mechanism selection, parameter units, conditioning information, the distinctions among model, analytic, floating-point and Monte Carlo error, binomial/Poisson coupling bound, continuity correction, finite-variance independent identical assumptions for the stated LLN and CLT, Bernoulli Monte Carlo variance, Hoeffding assumptions, seeded replication, and latent-mixture prediction. The rare-event example now explicitly includes exact probability, approximation, absolute and relative error. Exact-rational precision planning avoids rounding a trial-count ceiling from binary floating-point error.
- Unchanged Units 1–7 retain their recorded review and have their executable checks rerun. All thirty questions contain complete stated problems and at least three solution steps. Numeric check scope and limitations are recorded in numeric-final-checks.json.
- Ten pedagogically useful explorers are implemented. Unit 5 deliberately uses exact algebra and existence arguments instead of a random animation. The normal explorer uses a tested numerical CDF approximation; beta explorer is explicitly limited to positive integer shapes 1–6. Other visual/model limitations are visible in each explorer.
- Simulation tests compare 321 independent fixtures using enumeration and SciPy, plus invalid inputs, deterministic boundaries, zero-probability evidence, zero conditioning rows, seeded sampling, labels, parameter changes and reset. Their saved evidence matches the shipped source hashes. Rendered browser verification is recorded separately, and must pass before production publication.
- All 1,303 delimited mathematical expressions parse using the deployed KaTeX version. All ten static chapters preserve their complete serialized sections and solutions, with unique headings/canonicals, crawlable navigation, matching explorer slots and sitemap entries.
- Exact long-paragraph duplication checks found no repeated substantial paragraphs. No exhaustive external plagiarism database scan is claimed. Chapters remain original explanatory teaching material with invented educational mechanisms, not current medical, legal or financial advice.
- Existing academic pages and data/simulation sources are preserved against the pre-publication repository baseline. Full-library verification reports no content or navigation failures. Metadata and sitemap verification report no failures.

Production acceptance still requires the rendered preview tests, the final structural publication gate and verified Cloudflare/live delivery. Those stages must be evidenced separately; this review record does not claim they happened before their tests.


## Rendered preview correction

The phone-width browser check found a genuine shared formatter defect: raw less-than signs inside TeX were parsed as HTML, silently dropping parts of a normal-probability question even though the source expressions parsed successfully with KaTeX. The formatter now HTML-escapes comparisons and ampersands inside inline/display mathematics before assigning innerHTML. Source textbook text remains unchanged. A regression check tests inline/display inequalities and a matrix separator, and checks survival of every delimited source expression after HTML serialization. Generated new-book pages use a refreshed controller asset version. This correction must be verified in the next preview before production acceptance.


## Corrected-preview acceptance

The corrected preview is verified in Cloud Chrome. Chapter 9 annotations retain P(90<X<115) and P(X>120) intact, without KaTeX errors. At a 390-pixel iframe viewport, client and scroll widths are both 375 pixels after loading; the wider Bayes table scrolls inside its own 265-pixel container. Chapter-menu open/Escape closure/navigation, font switching, answer open/close and parameter/reset behavior passed. Desktop finite committee and Bayes controls also passed. See browser-checks.json for actual observations and limitations. A rendered iframe is not a real-device touch test. Production deployment/live acceptance is the remaining stage.


## Production verification

Cloudflare commit 2ecde66745d4686393d105d76c151fd530793b40 completed successfully on 13 October 2026. All ten live clean canonical chapters return HTTP 200, with three worked questions each and full navigation; live asset hashes match reviewed sources. The 491-entry sitemap is unique and includes all ten URLs. The homepage has 59 books, the normal Statistics catalog/search opens Book 2, and the New textbook box is absent. A nonexistent route returns HTTP 404; ads.txt is preserved. Automation remains disabled. Actual checks, timestamps and limitations are retained in live-checks.json.
