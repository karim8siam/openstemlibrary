/**
 * Publish only public files to dist, preserving canonical URL filenames.
 * Future sources may live under src/subjects/<department>/<book>/.
 * Do not switch Cloudflare build settings until the build has been reviewed.
 */
'use strict';
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');

const root = path.resolve(__dirname, '..');
const destination = path.join(root, 'dist');
const subjectRoot = path.join(root, 'src', 'subjects');
const allowedExts = new Set(['.html', '.js', '.css', '.svg', '.png', '.jpg', '.jpeg',
  '.webp', '.ico', '.txt', '.xml', '.webmanifest', '.woff', '.woff2', '.ttf']);
const specialFiles = new Set(['_headers', '_redirects']);
const publishedFiles = new Map();

function addPublicFile(sourcePath) {
  const name = path.basename(sourcePath);
  if (!allowedExts.has(path.extname(name).toLowerCase()) && !specialFiles.has(name)) return;
  const earlier = publishedFiles.get(name);
  if (earlier) {
    throw Error('Duplicate public filename "' + name + '": ' + earlier + ' and ' + sourcePath);
  }
  publishedFiles.set(name, sourcePath);
}

for (const file of fs.readdirSync(root, { withFileTypes: true })) {
  if (file.isFile()) addPublicFile(path.join(root, file.name));
}

// After the host output switches to dist, book sources can be moved gradually.
// Each subject/book directory may contain ordinary static HTML/JS/CSS assets.
if (fs.existsSync(subjectRoot)) {
  for (const dept of fs.readdirSync(subjectRoot, { withFileTypes: true })) {
    if (!dept.isDirectory()) continue;
    const deptDir = path.join(subjectRoot, dept.name);
    for (const book of fs.readdirSync(deptDir, { withFileTypes: true })) {
      if (!book.isDirectory()) continue;
      const bookDir = path.join(deptDir, book.name);
      for (const source of fs.readdirSync(bookDir, { withFileTypes: true })) {
        if (source.isFile()) addPublicFile(path.join(bookDir, source.name));
      }
    }
  }
}

for (const mandatory of ['index.html', 'robots.txt', 'sitemap.xml', '_headers', '_redirects', 'departments-data.js']) {
  assert(publishedFiles.has(mandatory), 'Missing essential public file: ' + mandatory);
}

const sitemap = fs.readFileSync(publishedFiles.get('sitemap.xml'), 'utf8');
const sitemapUrls = [...sitemap.matchAll(/<loc>\s*(https:\/\/openstemlibrary\.com\/[^<\s]*)\s*<\/loc>/g)]
  .map(item => item[1]);
assert(sitemapUrls.length > 0, 'Sitemap has no URLs');
assert.equal(new Set(sitemapUrls).size, sitemapUrls.length, 'Duplicate URL in sitemap');
for (const url of sitemapUrls) {
  const route = url.slice('https://openstemlibrary.com/'.length);
  assert(!route.includes('?') && !route.includes('#') && !route.includes('..'), 'Invalid sitemap route: ' + url);
  const asset = route === '' ? 'index.html' : route + '.html';
  assert(publishedFiles.has(asset), 'Missing public HTML for sitemap URL: ' + url);
}

const ctx = { window: {} };
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(publishedFiles.get('departments-data.js'), 'utf8'), ctx,
  { filename: 'departments-data.js', timeout: 1500 });
const departments = ctx.window.LIBRARY_CATALOG.departments;
const subjectInventory = {};
for (const department of departments) {
  const courses = department.courses.filter(book => book.status === 'AVAILABLE');
  subjectInventory[department.id] = courses.map(book => {
    assert(publishedFiles.has(book.url), 'Missing textbook: ' + book.url);
    const stem = book.url.replace(/\.html$/, '');
    const chapters = [...publishedFiles.keys()]
      .filter(name => name.startsWith(stem + '-chapter-') && name.endsWith('.html'))
      .sort((a, b) => Number(a.match(/-chapter-(\d+)\.html$/)?.[1] || 0) -
        Number(b.match(/-chapter-(\d+)\.html$/)?.[1] || 0));
    return { id: book.id, title: book.title, entry: book.url, chapters: chapters.length + 1 };
  });
}

// Each change to the reading controller or styles must invalidate the old
// URL in students' browser caches, instead of reusing a fixed 20261016 suffix.
const readerAssets = ['app.js', 'styles.css', 'portal.js', 'portal.css'];
const assetFingerprints = Object.fromEntries(readerAssets
  .filter(name => publishedFiles.has(name))
  .map(name => [name, crypto.createHash('sha256')
    .update(fs.readFileSync(publishedFiles.get(name))).digest('hex').slice(0, 12)]));
let updatedReaderNotices = 0;
let versionedReferences = 0;
function preparePublicHTML(html) {
  // The old lock label was still visible in the static HTML until scripts ran.
  // Reading, selecting and printing should be communicated truthfully even
  // when JS is delayed, blocked or served from a stale browser cache.
  const normalized = html.replace(/🔒\s*<span>\s*In-Browser Protected\s*[•·]\s*Direct Download Disabled\s*<\/span>/g,
    () => { updatedReaderNotices++; return '<span>Read freely · Cite responsibly</span>'; });
  return normalized.replace(/((?:src|href)=["'])(?:\.\/)?(app\.js|styles\.css|portal\.js|portal\.css)(?:\?v=[^"']*)?(["'])/g,
    (original, prefix, asset, closing) => {
      if(!assetFingerprints[asset]) return original;
      versionedReferences++;
      return prefix + asset + '?v=' + assetFingerprints[asset] + closing;
    });
}
fs.rmSync(destination, { recursive: true, force: true });
fs.mkdirSync(destination, { recursive: true });
for (const [name, source] of publishedFiles) {
  const target = path.join(destination, name);
  if(name.endsWith('.html')) {
    fs.writeFileSync(target, preparePublicHTML(fs.readFileSync(source, 'utf8')), 'utf8');
  } else {
    fs.copyFileSync(source, target);
  }
}
const totalBooks = Object.values(subjectInventory).reduce((n, courses) => n + courses.length, 0);
const result = {
  output: 'dist/',
  publicAssets: publishedFiles.size,
  normalizedOutdatedReaderNotices: updatedReaderNotices,
  cacheVersionedAssetReferences: versionedReferences,
  assetFingerprints,
  sitemapUrls: sitemapUrls.length,
  availableBooks: totalBooks,
  subjects: Object.fromEntries(Object.entries(subjectInventory).map(([id, books]) => [id, books.length])),
  preservedRoutes: true,
  internalToolingExcluded: !fs.existsSync(path.join(destination, 'tooling')),
  draftContentExcluded: !fs.existsSync(path.join(destination, 'publishing'))
};
assert(result.internalToolingExcluded && result.draftContentExcluded, 'Internal folders reached dist');
console.log(JSON.stringify(result, null, 2));
