# Cloudflare Pages build configuration cutover

This operational note triggers a fresh production deployment after setting the Cloudflare Pages build command to `node tooling/prepare-static-site.cjs` and output directory to `dist`.

Source repository: `karim8siam/openstemlibrary`
Production branch: `main`
Canonical site: `https://openstemlibrary.com/`

Acceptance checks:
- Homepage, textbooks, stylesheet, JavaScript, robots and sitemap: HTTP 200.
- Nonexistent routes, `/tooling/README.md`, and `/publishing/README.md`: HTTP 404.
- No textbook path or canonical URL changes.

The generated `dist/` output intentionally excludes `tooling/` and `publishing/`.
The migration draft PR #4 must remain unmerged until this production cutover has passed validation.

## Ecosystem Integration (October 21, 2026)
- Connected OpenSTEM Replicate (`https://openstemreplicate.org/`) to Card 2.
- Integrated OpenSTEM Tools (`https://openstemtool.org/`) with 155+ scientific calculators on Card 4.
