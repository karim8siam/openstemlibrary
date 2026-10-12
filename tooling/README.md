# Static library chapter pages

The deployed website remains buildless HTML/CSS/JavaScript on Cloudflare Pages.

The generated chapter pages contain the existing course text, worked solutions, metadata, and crawlable chapter links. They load the existing simulation engines and shared reader controller. Course data and simulation source files are not rewritten.

After changing course data or adding a book, regenerate and verify before committing:

```sh
npm install --prefix tooling jsdom@26.1.0 --no-save
node --expose-gc tooling/build-library.cjs
node --expose-gc tooling/verify-library.cjs
```

Run these commands from the repository root. The verification compares existing book content to the current Git HEAD; when checking a proposed update, run it before committing.

Commit the generated HTML pages and updated sitemap along with source changes. Cloudflare's existing Git integration publishes the production branch. No deployment settings need to change.
