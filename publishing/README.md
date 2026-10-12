# OpenSTEM editorial and publishing protocol

User-authorized scope: original English textbooks for the departments in `book-queue.json`; publish automatically through the existing GitHub main → Cloudflare Pages integration. Start with Statistics & Probability. Preserve existing books. Do not change hosting, permissions, advertising accounts, or billing.

## Persistent records

- `book-queue.json`: all 35 new departments and 705 proposed books. Statistics is mapped; other departments require curriculum research. Titles can be consolidated or revised when mapping shows overlap or omissions.
- `run-state.json`: current book, saved stage, publication history and automation ID. Update together with related changes, using the latest main HEAD and a branch-update lease.
- `outlines/`: original teaching plans with syllabus mapping.
- `drafts/<book-id>/`: saved content, source references and unresolved issues. Never add incomplete drafts to `departments-data.js`, the sitemap or public homepage.
- `qa/<book-id>.json`: evidence and hashes from actual verification, not aspirational checklists.

This repository is the durable database for this static site; no external database has been provisioned. The scheduled ChatGPT task is the executor, not a GitHub Actions workflow or a continuously running daemon. No API spending has been configured.

## Run one iteration

1. Read the latest repository, this protocol, queue, state and the active outline. Check for concurrent changes and previously published books. If a prior commit has uncertain deployment status, resolve it before another publication.
2. Select the first unfinished book in department and book order, beginning with the active Statistics book. Before drafting another department, browse official curricula, compare suitable programs, record source URLs, version/date, duration and course codes, then map every proposed specialist book. Professional medical degrees need not be four years; record their real duration. Exclude unrelated/general education courses and examination-only courses. Link existing mathematics prerequisites rather than duplicate them. Cover subject-specific applications that are actually part of the major. Integrate laboratories and research practice in appropriate books. Use supplementary original sections to fill genuine gaps, recording that editorial choice rather than pretending it came from a university syllabus.
3. Write or resume one original book. Save substantive work in small commits before output/context limits. Use 7–10 units and at least 50,000 substantive English words across theory, derivations, examples, original problem statements and worked explanations. Prefer a 54,000–60,000 draft buffer. Do not count navigation, bibliographies, code, repeated formula markup, duplicated text or artificial filler toward the minimum. Never advertise a word count or curriculum coverage without measuring/checking it. Do not reproduce copyrighted textbook prose or problems. Do not claim professor/expert review unless it happened.
4. Each unit needs clear objectives, definitions, reasoning, assumptions, varied examples, 2–3 distinct fully worked questions (prefer three); additional practice exercises are optional. Use conceptual, numerical, derivation/proof, interpretation, counterexample and applied questions as appropriate. Quantitative solutions need independently computed checks. For qualitative subjects, substantial argued cases, source analysis and model answers replace artificial numerical exercises. Explain common misconceptions and limitations. Avoid repeating the same problem with changed numbers.
5. Add simulations only where they teach a specific phenomenon. Explain controls, model assumptions, expected results and what the simulation cannot show. Test initial state, reset, extreme/invalid input, numerical correctness and small-screen accessibility. A book can omit simulations if their lack of pedagogical value is justified in QA.
6. Conduct a separate critical review pass: reconcile every mapped topic, check definitions/proofs/units, recompute worked answers using independently written calculations, inspect originality and repetition, render equations, test reader/chapter/solution controls and simulations. Current consequential medical, legal and financial statements require current authoritative sources and clear scope; unresolved accuracy concerns block publication. Do not mistake a numerical word counter or self-declared pass for substantive academic review.
7. Integrate only a complete passing book using the site's existing COURSE_DATA structure, reader template and catalog. Produce complete readable static chapter pages, visible table of contents, unique descriptive metadata, clean canonical URLs, truthful Book/LearningResource structured data, glossary and related links. Do not create empty indexed placeholder pages or keyword-stuffed descriptions. Preserve AdSense code and keep ads distinct from reading/navigation/simulation controls; do not manufacture impressions or claim approval.
8. Prepare the QA report with `content_sha256`, date, per-unit coverage, problem-check evidence, simulation-test evidence or omission reason, and `checks` entries for `academic_review`, `curriculum_coverage`, `worked_solutions`, `originality`, `simulation_behavior`, `mobile_reader`, `static_pages`, `seo_metadata`. Each entry has `status: "pass"` and concrete `evidence`; include relative `artifacts` paths for executable quantitative check logs. Run `node tooling/check-new-book.cjs <book-id>`, the static generator and preservation checker. A fail is a publication blocker. Add appropriate independent checks; the script is only a structural gate.
9. Publish at most one book per Asia/Dhaka calendar date. Immediately before updating main, reread publication history and the latest branch head. Use an expected-head lease; stop and reconcile any conflicting update. Commit book sources, reader/chapter pages, catalog, sitemap, QA and state together. Mark the commit as `publication_pending` until the live pages are verified; record successful deployment and actual local publication date afterward. Never claim a deployment succeeded just because GitHub accepted a commit. Check the live book and representative chapter via available read/browsing tools, including canonical/heading/content and sitemap entries.
10. If the book is unfinished or a check fails, save progress and continue the same book on the next run. Never publish partial material to meet a date, and never publish multiple backlog books on one date. If a substantive blocker requires user input, send a concise blocker message. Otherwise keep routine runs quiet if supported. Completion and exact upload time are not guaranteed; the 20:00 schedule starts a work iteration.

## Topic discoverability and sitemap acceptance

For each book and unit, map the specific study topics and learner questions to self-contained chapter content. Use clear topic names in page titles, H1/H2 headings and readable URLs, original explanations and worked answers, and related-topic internal links. Make content readable without a JavaScript click. Use natural terminology and common synonyms where useful; avoid keyword repetition and fabricated ranking promises.

Treat `sitemap.xml` verification as a required publication check: every new book and chapter must have a unique entry matching its clean canonical URL, accurate lastmod and a verified live response. Drafts stay excluded. Save the URL/canonical/sitemap check evidence in QA. Search Console submission remains manual.

## Search and advertising quality

The 50,000-word floor is the user's editorial requirement, not a Google ranking requirement. Optimize for complete, accurate learning, original worked solutions and useful navigation. Google has no preferred word count and warns against scaled content without user value. Index only completed books. Use honest publication/last-modified dates and actual canonicals; never bulk-refresh dates for unchanged chapters. Include each new book landing URL and its chapter URLs in `sitemap.xml`, staying under the 50,000-URL sitemap limit; split into a sitemap index if needed. The user submits Search Console manually. No ranking, AI recommendation, traffic, approval or revenue guarantees.

Sources checked 2026-10-11:

- https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- https://developers.google.com/search/docs/fundamentals/using-gen-ai-content
- https://www.stat.du.ac.bd/wp-content/uploads/2025/06/Syllabus.Undergraduate.Final-2023-24-1.pdf
- https://www.du.ac.bd/undergrad/ISR

## Usage and interruptions

The executor cannot read private ChatGPT five-hour or weekly quota balances through the currently exposed tools. Do not imply it can. Work until the available execution allowance, save progress early, and resume after interruptions. Do not evade usage limits or switch accounts. Do not introduce paid API generation without user authorization. Long drafts can require multiple scheduled runs; quality takes precedence over cadence.

## Website verification commands

Use installed jsdom or `OPENSTEM_JSDOM_PATH`; avoid reinstalling dependencies when already present.

```sh
node tooling/check-new-book.cjs <book-id>
node --expose-gc tooling/build-library.cjs
node --expose-gc tooling/verify-library.cjs
```

Run before committing. Check new-book pages separately from existing-book preservation. The scheduled task must inspect all returned errors and retain evidence. Only move a queue item to published after confirmed live delivery.

## One-time manual-first-book request

On 11 October 2026 the user requested the first Introduction to Statistics book immediately and asked the scheduled sequence to begin with book two on 12 October at 20:00 Asia/Dhaka. Record the real deployment timestamp even if the manual work crosses midnight. Only this authorized manual first publication is exempt from consuming a scheduled daily publication slot. All later scheduled runs remain limited to one verified new book per local date. Do not recreate or republish the first book as book two.
