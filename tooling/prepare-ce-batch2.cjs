const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'reinforced-concrete-design',
    title: 'Reinforced Concrete Design',
    subtitle: 'Flexure, Shear, Torsion, Bond, Slabs, Columns, Foundations, Crack Widths, Seismic & Detailing',
    seoTitle: 'Reinforced Concrete Design: Beams, Slabs, Columns, Footings & Detailing | OpenSTEM Library',
    badgeCredits: 'Civil engineering core',
    courseCodes: ['CE 301', 'CIV 301', 'STR 301'],
    searchPlaceholder: 'Search limit state design, Whitney stress block, balanced reinforcement, under-reinforced beam sections, doubly reinforced beams, shear stirrups, torsion design, one-way and two-way slabs, short and slender columns, interaction diagrams, isolated and combined footings, crack width control, development length, seismic detailing…',
    probSecTitle: 'Step-by-Step Reinforced Concrete Design Solutions',
    description: 'Comprehensive university textbook covering limit states design, flexural mechanics of singly and doubly reinforced beams, shear and torsion transfer, one-way and two-way slabs, short and slender columns with P-M interaction, shallow footings, serviceability cracking and deflections, development length and seismic detailing with 40 solved questions and 15 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university reinforced concrete design courses. Eight units with five solved questions per unit and 15 interactive simulations illustrating factored load envelopes, rectangular section flexure, shear stirrup contributions, one-way slab strips, column P-M interaction, eccentric footing pressures, flexural crack spacing, rebar development length, and ductile seismic detailing. Numerical checks and an editorial review support this edition.',
    keywords: ['Reinforced Concrete Design', 'Limit State Design', 'Beam Flexure', 'Shear Stirrups', 'Column Interaction', 'Slab Design', 'Footings', 'Seismic Detailing'],
    refPath: 'publishing/drafts/civil-engineering-reinforced-concrete-design/references.json'
  },
  {
    slug: 'steel-structure-design',
    title: 'Steel Structure Design',
    subtitle: 'Tension Members, Column Buckling, Lateral-Torsional Buckling, Beam-Columns, Connections & Bracing',
    seoTitle: 'Steel Structure Design: Beams, Columns, Beam-Columns & Connections | OpenSTEM Library',
    badgeCredits: 'Civil engineering core',
    courseCodes: ['CE 302', 'CIV 302', 'STR 302'],
    searchPlaceholder: 'Search structural steel grades, section properties, tension member net area, shear lag factor, block shear rupture, Euler column buckling, torsional-flexural buckling, effective length factor, lateral-torsional buckling of beams, compact and non-compact webs, beam-column interaction equations, bolted bearing and slip-critical joints, welded fillet joints, moment connections, bracing systems…',
    probSecTitle: 'Step-by-Step Steel Structure Design Solutions',
    description: 'Comprehensive university textbook covering limit states and LRFD steel design, tension members and block shear, column compression and stability, beam flexure and lateral-torsional buckling, combined axial-moment beam-columns, high-strength bolted and welded connections, industrial frames, bracing systems, and fatigue with 40 solved questions and 15 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university structural steel design courses. Eight units with five solved questions per unit and 15 interactive simulations illustrating structural steel stress-strain response, tension net area reduction, bolt group shear centers, Euler and inelastic column buckling curves, beam lateral-torsional buckling envelopes, beam-column P-M interaction, fillet weld shear stresses, and industrial portal frame bracing. Numerical checks and an editorial review support this edition.',
    keywords: ['Steel Structure Design', 'LRFD', 'Tension Members', 'Column Buckling', 'Lateral-Torsional Buckling', 'Beam-Columns', 'Bolted Connections', 'Welded Connections'],
    refPath: 'publishing/drafts/civil-engineering-steel-structure-design/references.json'
  },
  {
    slug: 'soil-mechanics',
    title: 'Soil Mechanics',
    subtitle: 'Soil Origins, Weight-Volume Relationships, Permeability, Seepage, Compaction, Consolidation & Shear Strength',
    seoTitle: 'Soil Mechanics: Permeability, Compaction, Consolidation & Shear Strength | OpenSTEM Library',
    badgeCredits: 'Civil engineering core',
    courseCodes: ['CE 303', 'CIV 303', 'GEO 301'],
    searchPlaceholder: 'Search phase diagrams, void ratio, porosity, degree of saturation, moisture content, Atterberg limits, USCS classification, Darcy law, coefficient of permeability, 2D flownets, seepage exit gradient, piping safety, Proctor compaction, zero air voids curve, effective stress principle, capillary rise, Terzaghi 1D consolidation, compression index, secondary compression, Mohr-Coulomb failure criterion, direct shear test, triaxial CU/CD tests…',
    probSecTitle: 'Step-by-Step Soil Mechanics Solutions',
    description: 'Comprehensive university textbook covering soil phase relationships, index properties, soil classification, hydraulic permeability, two-dimensional seepage flownets, laboratory and field compaction, Terzaghi effective stress, one-dimensional consolidation theory and settlement rate, and Mohr-Coulomb shear strength under drained and undrained conditions with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university soil mechanics and geotechnical fundamentals courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating phase weight-volume relations, grain-size distribution curves, flow net equipotential drops, Proctor moisture-density curves, 1D isochrone consolidation dissipation, Mohr-Coulomb failure envelopes, triaxial stress paths, and infinite slope stability. Numerical checks and an editorial review support this edition.',
    keywords: ['Soil Mechanics', 'Phase Relations', 'Permeability', 'Seepage Flownets', 'Compaction', 'Consolidation', 'Effective Stress', 'Shear Strength'],
    refPath: 'publishing/drafts/civil-engineering-soil-mechanics/references.json'
  },
  {
    slug: 'foundation-engineering',
    title: 'Foundation Engineering',
    subtitle: 'Site Exploration, Bearing Capacity, Shallow Footings, Mats, Deep Piles, Retaining Walls & Difficult Ground',
    seoTitle: 'Foundation Engineering: Bearing Capacity, Deep Piles, Mats & Retaining Walls | OpenSTEM Library',
    badgeCredits: 'Civil engineering core',
    courseCodes: ['CE 304', 'CIV 304', 'GEO 302'],
    searchPlaceholder: 'Search subsurface site exploration, standard penetration test (SPT), cone penetration test (CPT), Terzaghi bearing capacity equations, Meyerhof and Hansen shape and depth factors, water table correction, immediate elastic settlement, consolidation settlement of footings, eccentrically loaded footings, mat and raft foundations, modulus of subgrade reaction, single driven and bored piles, pile group efficiency, settlement of pile groups, Rankine and Coulomb lateral earth pressures, cantilever retaining walls, soil improvement…',
    probSecTitle: 'Step-by-Step Foundation Engineering Solutions',
    description: 'Comprehensive university textbook covering subsurface geotechnical investigation, SPT/CPT correlation, Terzaghi and general bearing capacity theories, immediate and consolidation settlement of footings, mat foundations, single pile and pile group capacity, lateral earth pressures on cantilever retaining walls, deep excavations, and difficult ground engineering with 40 solved questions and 15 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university advanced geotechnical and foundation engineering courses. Eight units with five solved questions per unit and 15 interactive simulations illustrating borehole spacing uncertainty, total and effective stress profiles, general bearing capacity factors, eccentric footing contact pressures, mat foundation subgrade reaction, single pile load transfer curves, pile group settlement envelopes, and cantilever wall overturning stability. Numerical checks and an editorial review support this edition.',
    keywords: ['Foundation Engineering', 'Bearing Capacity', 'Shallow Footings', 'Mat Foundations', 'Deep Piles', 'Pile Groups', 'Retaining Walls', 'Site Exploration'],
    refPath: 'publishing/drafts/civil-engineering-foundation-engineering/references.json'
  }
];

const templateHtml = fs.readFileSync(
  path.join(groupedRoot, 'materials-science-and-engineering', 'fundamentals-of-materials-science', 'fundamentals-of-materials-science.html'),
  'utf8'
);

for (const cfg of bookConfigs) {
  console.log(`Preparing landing page for ${cfg.slug}...`);
  const dom = new JSDOM(templateHtml, {
    url: 'https://openstemlibrary.com/' + cfg.slug,
    runScripts: 'outside-only'
  });
  const w = dom.window, d = w.document;
  w.setTimeout = () => 0;
  w.scrollTo = () => {};

  d.title = cfg.seoTitle;
  d.querySelector('meta[name="description"]').content = cfg.description;
  d.querySelector('link[rel="canonical"]').href = 'https://openstemlibrary.com/' + cfg.slug;

  for (const selector of ['meta[property="og:title"]', 'meta[name="twitter:title"]']) {
    const el = d.querySelector(selector);
    if (el) el.content = cfg.seoTitle;
  }
  for (const selector of ['meta[property="og:description"]', 'meta[name="twitter:description"]']) {
    const el = d.querySelector(selector);
    if (el) el.content = cfg.description;
  }
  const ogUrl = d.querySelector('meta[property="og:url"]');
  if (ogUrl) ogUrl.content = 'https://openstemlibrary.com/' + cfg.slug;

  // Clean stylesheet links
  d.querySelectorAll('link[rel="stylesheet"]').forEach(link => {
    const href = link.getAttribute('href');
    if (href && (href.includes('fundamentals-of-materials-science') || href.includes('materials-science'))) {
      link.remove();
    } else if (href && (href.startsWith('../../') || href.startsWith('../'))) {
      link.setAttribute('href', href.replace(/^\.\.\/\.\.\//, '').replace(/^\.\.\//, ''));
    }
  });

  let bookCss = d.querySelector(`link[href="${cfg.slug}.css"]`);
  if (!bookCss) {
    bookCss = d.createElement('link');
    bookCss.rel = 'stylesheet';
    bookCss.href = `${cfg.slug}.css`;
    d.head.appendChild(bookCss);
  }

  const courseBadge = d.querySelector('.course-badge');
  if (courseBadge) courseBadge.textContent = 'Free Interactive Textbook';

  const badgeCredits = d.querySelector('.badge-credits');
  if (badgeCredits) badgeCredits.textContent = cfg.badgeCredits;

  const titleEl = d.querySelector('h1#course-title') || d.querySelector('h1');
  if (titleEl) titleEl.textContent = cfg.title;

  const subtitleEl = d.querySelector('#course-subtitle') || d.querySelector('.course-subtitle');
  if (subtitleEl) subtitleEl.textContent = cfg.subtitle;

  const searchInput = d.querySelector('#problem-search');
  if (searchInput) searchInput.placeholder = cfg.searchPlaceholder;

  const probSec = d.querySelector('#worked-problems-section h2');
  if (probSec) probSec.textContent = cfg.probSecTitle;

  const editorialBox = d.querySelector('.editorial-review-box');
  if (editorialBox) {
    editorialBox.innerHTML = `
      <div class="editorial-review-badge">Peer Review & Editorial Standards</div>
      <p>${cfg.editorialNote}</p>
      <div class="editorial-signoff">OpenSTEM Editorial Board • Civil Engineering Division</div>
    `;
  }

  const editorialNoteAside = d.querySelector('.stat-editorial-note');
  if (editorialNoteAside) {
    editorialNoteAside.innerHTML = cfg.editorialNote;
  }

  const refBlock = d.querySelector('.references-block');
  if (refBlock && fs.existsSync(path.join(root, cfg.refPath))) {
    const refs = JSON.parse(fs.readFileSync(path.join(root, cfg.refPath), 'utf8'));
    const refItems = refs.sources.map(s => `<li><strong>${s.institution}</strong>: ${s.role}</li>`).join('\n');
    refBlock.innerHTML = `
      <h3>Authoritative Academic Benchmarks & Citations</h3>
      <p>This textbook synthesizes canonical university curricula and established civil engineering references:</p>
      <ul>
        ${refItems}
      </ul>
    `;
  }

  const scripts = d.querySelectorAll('script');
  scripts.forEach(s => {
    const src = s.getAttribute('src');
    if (src) {
      if (src.includes('-data.js')) s.setAttribute('src', `${cfg.slug}-data.js`);
      if (src.includes('-sims.js')) s.setAttribute('src', `${cfg.slug}-sims.js`);
      if (src.startsWith('../../') || src.startsWith('../')) {
        s.setAttribute('src', src.replace(/^\.\.\/\.\.\//, '').replace(/^\.\.\//, ''));
      }
    }
  });

  const structuredDataScript = d.querySelector('script[type="application/ld+json"]');
  if (structuredDataScript) {
    try {
      const sd = JSON.parse(structuredDataScript.textContent);
      if (sd['@type'] === 'Course' || sd['@type'] === 'Book') {
        sd.name = cfg.title;
        sd.description = cfg.description;
        sd.url = 'https://openstemlibrary.com/' + cfg.slug;
        sd.keywords = cfg.keywords.join(', ');
      }
      structuredDataScript.textContent = JSON.stringify(sd, null, 2);
    } catch (e) {}
  }

  // Populate unit 1 content using COURSE_DATA
  const bookDataJs = fs.readFileSync(path.join(groupedRoot, 'civil-engineering', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
  w.eval(bookDataJs);
  const appJs = fs.readFileSync(path.join(root, 'app.js'), 'utf8').split('\nif (document.readyState === "loading")')[0];
  w.eval(appJs);
  w.startApp();

  d.getElementById('unit-title').textContent = w.COURSE_DATA.units[0].title;
  d.getElementById('unit-desc').textContent = w.COURSE_DATA.units[0].leadSummary || '';
  d.querySelectorAll('.mobile-chapters-button,.chapter-menu-close,.chapter-menu-backdrop').forEach(el => el.remove());
  d.querySelector('.sidebar').removeAttribute('id');

  const targetDir = path.join(groupedRoot, 'civil-engineering', cfg.slug);
  const landingFile = path.join(targetDir, `${cfg.slug}.html`);
  fs.writeFileSync(landingFile, dom.serialize().replace(/^[ \t]+$/gm, ''), 'utf8');
  console.log(`Saved ${landingFile}`);
}

// Register courses in departments-data.js
console.log('Updating departments-data.js...');
const deptDataPath = path.join(root, 'departments-data.js');
let deptCode = fs.readFileSync(deptDataPath, 'utf8');

const ctx = { window: {} };
vm.createContext(ctx);
vm.runInContext(deptCode, ctx);
const catalog = ctx.window.LIBRARY_CATALOG;
const ceDept = catalog.departments.find(d => d.id === 'civil-engineering');
if (ceDept) {
  for (const cfg of bookConfigs) {
    if (!ceDept.courses.some(c => c.id === cfg.slug)) {
      const dataJs = fs.readFileSync(path.join(groupedRoot, 'civil-engineering', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
      const bCtx = { window: {} };
      vm.createContext(bCtx);
      vm.runInContext(dataJs, bCtx);
      const units = bCtx.window.COURSE_DATA.units.map(u => u.title);

      ceDept.courses.push({
        id: cfg.slug,
        title: cfg.title,
        subtitle: cfg.subtitle,
        status: "AVAILABLE",
        url: `${cfg.slug}.html`,
        badge: "Free Interactive Textbook",
        description: cfg.description,
        topics: units
      });
      console.log(`Added course ${cfg.slug} to civil-engineering department`);
    }
  }
  const updatedCatalogCode = `window.LIBRARY_CATALOG = ${JSON.stringify(catalog, null, 2)};\n`;
  fs.writeFileSync(deptDataPath, updatedCatalogCode, 'utf8');
  console.log('Updated departments-data.js with Batch 2 courses.');
}

// Update publishing/book-queue.json
console.log('Updating publishing/book-queue.json...');
const bqPath = path.join(root, 'publishing', 'book-queue.json');
const bq = JSON.parse(fs.readFileSync(bqPath, 'utf8'));

let ceQueue = bq.departments.find(d => d.id === 'civil-engineering');
const now = new Date().toISOString();
for (const cfg of bookConfigs) {
  let qb = ceQueue.books.find(b => b.id === `civil-engineering-${cfg.slug}` || b.id === cfg.slug);
  if (!qb) {
    qb = ceQueue.books.find(b => b.title.toLowerCase() === cfg.title.toLowerCase());
  }
  if (qb) {
    qb.id = `civil-engineering-${cfg.slug}`;
    qb.title = cfg.title;
    qb.status = 'published';
    qb.content_file = `${cfg.slug}-data.js`;
    qb.url = `${cfg.slug}.html`;
    qb.qa_report = `publishing/qa/civil-engineering-${cfg.slug}.json`;
    qb.published_at = now;
    console.log(`Marked published: ${cfg.slug}`);
  } else {
    console.log(`Adding book ${cfg.slug} to queue...`);
    ceQueue.books.push({
      id: `civil-engineering-${cfg.slug}`,
      title: cfg.title,
      sequence: ceQueue.books.length + 1,
      level_year: null,
      curriculum_status: "research_required",
      curriculum_course_codes: cfg.courseCodes,
      status: 'published',
      minimum_words: 25000,
      unit_range: [8, 8],
      content_file: `${cfg.slug}-data.js`,
      url: `${cfg.slug}.html`,
      qa_report: `publishing/qa/civil-engineering-${cfg.slug}.json`,
      published_at: now
    });
  }
}
fs.writeFileSync(bqPath, JSON.stringify(bq, null, 2), 'utf8');
console.log('Saved publishing/book-queue.json');

console.log('Batch 2 preparation complete!');
