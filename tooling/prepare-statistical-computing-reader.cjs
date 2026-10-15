const fs = require('node:fs'), path = require('node:path'), vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');
const root = path.resolve(__dirname, '..');
const read = p => fs.readFileSync(path.join(root, p), 'utf8');
const slug = 'statistical-computing-with-python-and-r';

const dom = new JSDOM(read('introduction-to-statistics.html'), {
  url: 'https://openstemlibrary.com/' + slug,
  runScripts: 'outside-only'
});
const w = dom.window, d = w.document;
w.setTimeout = () => 0;
w.scrollTo = () => {};

const title = 'Statistical Computing with Python and R';
const description = 'Comprehensive university textbook covering NumPy/R memory models, tabular wrangling, Grammar of Graphics, numerical linear algebra & floating point, Monte Carlo & MCMC, resampling & bootstrap, numerical optimization, and reproducible statistical pipelines with 24 solved questions and 4 interactive simulations.';

d.title = title + ': Memory Models, Linear Algebra, Monte Carlo, Resampling & Optimization | OpenSTEM Library';
d.querySelector('meta[name="description"]').content = description;
d.querySelector('link[rel="canonical"]').href = 'https://openstemlibrary.com/' + slug;

for (const selector of ['meta[property="og:title"]', 'meta[name="twitter:title"]']) {
  d.querySelector(selector).content = d.title;
}
for (const selector of ['meta[property="og:description"]', 'meta[name="twitter:description"]']) {
  d.querySelector(selector).content = description;
}
d.querySelector('meta[property="og:url"]').content = 'https://openstemlibrary.com/' + slug;

d.body.dataset.bookPath = slug + '.html';
d.body.dataset.chapterIndex = '0';
d.querySelector('.brand-title').textContent = title;
d.querySelector('.badge-credits').textContent = 'Statistical computing major';
d.getElementById('topic-search-input').placeholder = 'Search memory strides, hash joins, ggplot2 grammar, SVD, rejection sampling, MCMC, bootstrap, Nelder-Mead…';

d.querySelectorAll('.textbook-section-card,.problem-card,.chapter-pagination,.stat-editorial-note,.mobile-chapters-button,.chapter-menu-close,.chapter-menu-backdrop').forEach(el => el.remove());
d.getElementById('textbook-sections').innerHTML = '';
(d.getElementById('problems-mount') || d.getElementById('problems-container') || d.getElementById('problem-cards-list')).innerHTML = '';
d.querySelector('.sidebar').removeAttribute('id');

d.querySelector('.prob-sec-title').textContent = 'Step-by-Step Statistical Computing Solutions';

for (const el of d.querySelectorAll('script[src],link[rel="stylesheet"]')) {
  const attr = el.tagName === 'SCRIPT' ? 'src' : 'href';
  const src = el.getAttribute(attr);
  if (src.startsWith('introduction-to-statistics')) {
    el.setAttribute(attr, src.replace('introduction-to-statistics', slug));
  }
}

const note = d.createElement('aside');
note.className = 'stat-editorial-note';
note.setAttribute('aria-label', 'About this textbook');
note.innerHTML = '<strong>About this textbook.</strong> Original English teaching material mapped to University of Dhaka Statistics B.S. Honours 2023–24, Stat H-108, Stat H-209, Stat H-310, and Stat H-311. Eight units and exactly three solved questions per unit. Interactive simulations illustrate core computational algorithms. Numerical checks and an editorial review support this edition; it has not received independent academic peer review. Curriculum mapping does not imply university endorsement.';
d.querySelector('.unit-hero').after(note);

const refs = JSON.parse(read('publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/references.json'));
d.querySelector('.reader-trust-footer').innerHTML = '<nav class="reader-trust-links" aria-label="Related reading"><a href="index#dept-statistics-probability">Statistics department</a><a href="introduction-to-statistics">Introduction to Statistics</a><a href="probability-and-probability-distributions">Probability and Probability Distributions</a><a href="sample-surveys-and-sampling-theory">Sample Surveys and Sampling Theory</a><a href="basic-algebra">Algebra prerequisite</a><a href="calculus-1">Calculus prerequisite</a><a href="about">About & editorial</a><a href="privacy">Privacy</a><a href="terms">Terms</a><a href="mailto:shahriyarkarimsiam@gmail.com">Report a correction</a></nav><details><summary>Curriculum and mathematical references</summary><ul>' + refs.sources.map(s => `<li><a href="${s.url}" target="_blank" rel="noopener noreferrer">${s.institution}: ${s.role}</a></li>`).join('') + '</ul></details><p class="reader-trust-copy">© 2026 OpenSTEM Library • Free original educational textbook</p>';

d.querySelectorAll('script[type="application/ld+json"]').forEach(el => el.remove());

function schema(data) {
  const s = d.createElement('script');
  s.type = 'application/ld+json';
  s.textContent = JSON.stringify(data);
  d.head.append(s);
}

schema({
  '@context': 'https://schema.org',
  '@type': 'Book',
  name: title,
  description,
  url: 'https://openstemlibrary.com/' + slug,
  inLanguage: 'en',
  isAccessibleForFree: true,
  educationalLevel: 'Undergraduate',
  author: { '@type': 'Organization', name: 'OpenSTEM Library' },
  publisher: { '@type': 'Organization', name: 'OpenSTEM Library', url: 'https://openstemlibrary.com/' },
  learningResourceType: 'Textbook',
  about: ['Statistical computing', 'NumPy and R memory models', 'Tabular data wrangling', 'Grammar of graphics', 'Numerical linear algebra', 'Monte Carlo methods', 'Markov chain Monte Carlo', 'Bootstrap and resampling', 'Numerical optimization']
});

schema({
  '@context': 'https://schema.org',
  '@type': 'BreadcrumbList',
  itemListElement: [
    { '@type': 'ListItem', position: 1, name: 'OpenSTEM Library', item: 'https://openstemlibrary.com/' },
    { '@type': 'ListItem', position: 2, name: 'Statistics & Probability', item: 'https://openstemlibrary.com/#dept-statistics-probability' },
    { '@type': 'ListItem', position: 3, name: title, item: 'https://openstemlibrary.com/' + slug }
  ]
});

w.eval(read(slug + '-data.js'));
w.eval(read('app.js').split('\nif (document.readyState === "loading")')[0]);
w.startApp();

d.getElementById('unit-title').textContent = w.COURSE_DATA.units[0].title;
d.getElementById('unit-desc').textContent = w.COURSE_DATA.units[0].leadSummary;
d.querySelectorAll('.mobile-chapters-button,.chapter-menu-close,.chapter-menu-backdrop').forEach(el => el.remove());
d.querySelector('.sidebar').removeAttribute('id');

fs.writeFileSync(path.join(root, slug + '.html'), dom.serialize());

const context = { window: {} };
vm.createContext(context);
vm.runInContext(read('departments-data.js'), context);
const catalog = context.window.LIBRARY_CATALOG;
const department = catalog.departments.find(d => d.id === 'statistics-probability');
department.courses = department.courses.filter(b => b.id !== slug);
department.courses.push({
  id: slug,
  title,
  subtitle: 'Memory Models, Tabular Wrangling, Numerical Linear Algebra, Monte Carlo, Resampling & Optimization',
  status: 'AVAILABLE',
  url: slug + '.html',
  badge: 'Free Interactive Textbook',
  description,
  topics: w.COURSE_DATA.units.map(u => u.title)
});

fs.writeFileSync(path.join(root, 'departments-data.js'), '// OpenSTEM academic catalog: only completed books appear as available.\nwindow.LIBRARY_CATALOG = ' + JSON.stringify(catalog, null, 2) + ';\n');
w.close();
console.log(JSON.stringify({ reader: slug + '.html', statisticsBooks: department.courses.length }));
