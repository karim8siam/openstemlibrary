# OpenSTEM Library: Subject Organization Without URL Changes

## Why the root contains many HTML files
This site is made of static pages. Google crawls production URLs, not GitHub directory layouts.
Do not rename indexed public URLs simply to tidy the repository.

## Planned source layout (after Cloudflare build settings are switched)
    src/
      subjects/
        physics/
          quantum-mechanics/
            reader.html
            reader-chapter-2.html
            course-data.js
            simulations.js
        mathematics/
          calculus-1/
            calculus-1.html
            calculus-1-chapter-2.html
            calculus-1-data.js
            calculus-1-sims.js
        chemistry/
        statistics-probability/
    tooling/
    publishing/
    dist/  # generated, gitignored

The build script tooling/prepare-static-site.cjs copies root assets and subject/book leaf files into dist/, preserving original filenames.

Example:
    Git source: src/subjects/physics/quantum-mechanics/reader-chapter-2.html
    Deployed file: dist/reader-chapter-2.html
    Public URL: https://openstemlibrary.com/reader-chapter-2

departments-data.js remains the one authoritative catalog. No duplicate catalog needs manual updates.

## Stage 1: safe initial build (does not modify live hosting)
Run: node tooling/prepare-static-site.cjs
Checks sitemap targets and catalog references; copies public assets while excluding tooling and publishing drafts.
Never commit the dist folder.

## Stage 2: future Cloudflare Pages configuration switch
Only after reviewing staging build and HTTP responses:
- Build command: node tooling/prepare-static-site.cjs
- Build output directory: dist
- Production branch: main
- Verify the homepage, chapter routes, styles, simulations, _headers, _redirects, sitemap, robots and ads.txt.
Changing Cloudflare build settings is a separate operation: do not move source files beforehand.

## Stage 3: gradual subject migration
After the new dist deployment has been proven safe, move exactly one book's HTML, data and simulation assets to its src/subjects folder.
Do not change its output name. Build and test before moving another book.

## Crawling and resilience
Googlebot requests the deployed public URLs. Folder grouping in Git has no direct effect on request concurrency.
Check actual 429/5xx responses and host analytics before considering crawler rate limits.

## Production cutover verification (October 20, 2026)

Cloudflare Pages now uses `node tooling/prepare-static-site.cjs` with output `dist` on `main`. The immutable Pages deployment and `https://openstemlibrary.com` both return HTTP 404 for `/tooling/README.md` and `/publishing/README.md`, while textbook pages return HTTP 200. The first actual subject move is staged as a separate draft pull request and must pass all checks before release.
