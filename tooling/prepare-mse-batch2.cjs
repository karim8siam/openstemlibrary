const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'phase-transformations',
    title: 'Phase Transformations',
    subtitle: 'Thermodynamics of Interfaces, Solidification, Spinodal Decomposition, Diffusional & Martensitic Transformations',
    seoTitle: 'Phase Transformations in Materials: Solidification, Nucleation & Interfaces | OpenSTEM Library',
    badgeCredits: 'Phase transformations core',
    courseCodes: ['MSE 320', 'MAT 320'],
    searchPlaceholder: 'Search interface thermodynamics, capillary pressure and Gibbs-Thomson effect, planar vs cellular vs dendritic solidification, spinodal decomposition Cahn-Hilliard equation, time-temperature-transformation (TTT) diagrams, continuous cooling transformation (CCT), diffusionless martensitic crystallography, Bain distortion…',
    probSecTitle: 'Step-by-Step Phase Transformations Solutions',
    description: 'Comprehensive university textbook covering interfacial energy and curvature, alloy solidification morphologies, solute redistribution and Scheil equation, diffusional precipitation kinetics, spinodal instability, massive transformations, and shear-dominant martensitic transitions with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university phase transformations courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating Gibbs-Thomson melting point depressions, Scheil partition profiles, homogeneous nucleation rates, Avrami growth curves, and habit plane orientation relationships. Numerical checks and an editorial review support this edition.',
    keywords: ['Phase Transformations', 'Solidification', 'Nucleation', 'Interfaces', 'Spinodal Decomposition', 'Martensite', 'TTT Diagrams', 'JMAK Kinetics'],
    refPath: 'publishing/drafts/materials-science-and-engineering-phase-transformations/references.json'
  },
  {
    slug: 'physical-metallurgy',
    title: 'Physical Metallurgy',
    subtitle: 'Alloy Phase Equilibria, Solid Solution Strengthening, Precipitation Hardening & Ferrous Metallurgy',
    seoTitle: 'Physical Metallurgy: Alloy Systems, Heat Treatment & Microstructures | OpenSTEM Library',
    badgeCredits: 'Metallurgy core',
    courseCodes: ['MSE 325', 'MAT 325'],
    searchPlaceholder: 'Search iron-carbon equilibrium phase diagram, austenite-ferrite-pearlite-bainite-martensite microconstituents, hardenability and Jominy end-quench test, solid solution lattice strain, Orowan dislocation bowing vs particle cutting, recovery, recrystallization, and grain growth kinetics…',
    probSecTitle: 'Step-by-Step Physical Metallurgy Solutions',
    description: 'Comprehensive university textbook covering binary and ternary alloy systems, solid solution thermodynamics, precipitation hardening pathways in aluminum alloys, ferrous heat treatments, quench-and-temper kinetics, grain boundary engineering, and microstructural characterization with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university physical metallurgy courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating iron-carbon phase fractions, Orowan looping shear stresses, precipitation aging hardness curves, Jominy hardenability curves, and grain growth kinetics. Numerical checks and an editorial review support this edition.',
    keywords: ['Physical Metallurgy', 'Alloys', 'Strengthening', 'Precipitation Hardening', 'Steels', 'Heat Treatment', 'Recrystallization', 'Grain Growth'],
    refPath: 'publishing/drafts/materials-science-and-engineering-physical-metallurgy/references.json'
  },
  {
    slug: 'ceramic-materials',
    title: 'Ceramic Materials',
    subtitle: 'Bonding, Crystal & Glass Structures, Point Defects, Sintering Kinetics & Dielectric Properties',
    seoTitle: 'Ceramic Materials: Structures, Processing, Sintering & Refractories | OpenSTEM Library',
    badgeCredits: 'Ceramics core',
    courseCodes: ['MSE 330', 'MAT 330'],
    searchPlaceholder: 'Search Pauling rules for ionic crystals, Kröger-Vink defect notation, Frenkel vs Schottky defects, Zachariasen glass forming criteria, solid-state sintering and grain growth, Weibull statistical modulus for brittle fracture, transformation toughening in zirconia (PSZ), piezoelectric ceramics (PZT)…',
    probSecTitle: 'Step-by-Step Ceramic Materials Solutions',
    description: 'Comprehensive university textbook covering coordination polyhedra, oxide and non-oxide crystal structures, glass formation kinetics, point defect thermodynamics, solid-state and liquid-phase sintering, brittle fracture mechanics, thermal shock resistance, and functional electroceramics with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university ceramics courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating Pauling radius ratio coordinates, Kröger-Vink defect concentrations, sintering shrinkage rates, Weibull survival probabilities, and dielectric polarization curves. Numerical checks and an editorial review support this edition.',
    keywords: ['Ceramics', 'Glass Structure', 'Point Defects', 'Sintering', 'Refractories', 'Dielectrics', 'Piezoelectrics', 'Toughness'],
    refPath: 'publishing/drafts/materials-science-and-engineering-ceramic-materials/references.json'
  },
  {
    slug: 'polymer-science',
    title: 'Polymer Science',
    subtitle: 'Synthesis, Molecular Weight, Chain Conformations, Glass Transition, Viscoelasticity & Crystallinity',
    seoTitle: 'Polymer Science: Synthesis, Viscoelasticity & Molecular Conformations | OpenSTEM Library',
    badgeCredits: 'Polymer core',
    courseCodes: ['MSE 335', 'MAT 335'],
    searchPlaceholder: 'Search step-growth vs chain-growth polymerization, Carothers equation, number-average vs weight-average molecular weight, polydispersity index (PDI), freely jointed chain root-mean-square end-to-end distance, Flory-Huggins solution theory, glass transition temperature (Tg) and free volume, Maxwell and Kelvin-Voigt viscoelastic models…',
    probSecTitle: 'Step-by-Step Polymer Science Solutions',
    description: 'Comprehensive university textbook covering macromolecular chemistry, step and chain polymerization kinetics, statistical thermodynamics of polymer coils and solutions, semi-crystalline polymer morphology, glass transition phenomena, linear viscoelastic relaxation, and polymer rheology with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university polymer science courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating Carothers conversion curves, molecular weight distribution curves, polymer coil radius of gyration, Flory-Huggins phase envelopes, and Maxwell stress relaxation decays. Numerical checks and an editorial review support this edition.',
    keywords: ['Polymer Science', 'Polymerization', 'Molecular Weight', 'Glass Transition', 'Viscoelasticity', 'Crystallinity', 'Rubber Elasticity', 'Rheology'],
    refPath: 'publishing/drafts/materials-science-and-engineering-polymer-science/references.json'
  },
  {
    slug: 'composite-materials',
    title: 'Composite Materials',
    subtitle: 'Fiber Reinforcements, Rule of Mixtures, Micromechanics, Laminate Theory & Failure Criteria',
    seoTitle: 'Composite Materials: Micromechanics, Laminates & Fiber Reinforcements | OpenSTEM Library',
    badgeCredits: 'Composites core',
    courseCodes: ['MSE 340', 'MAT 340'],
    searchPlaceholder: 'Search Voigt isostrain vs Reuss isostress rule of mixtures, Halpin-Tsai micromechanics equations, critical fiber length and shear lag theory, anisotropic lamina constitutive relations (Q-matrix), classical laminate plate theory (ABD matrix), symmetric vs balanced layups, Tsai-Hill and Tsai-Wu failure criteria, delamination toughness…',
    probSecTitle: 'Step-by-Step Composite Materials Solutions',
    description: 'Comprehensive university textbook covering reinforcement types (carbon, glass, aramid), polymer, metal, and ceramic matrix composites, fiber-matrix interface bonding, micromechanical stress transfer, Classical Lamination Theory (CLT), failure envelopes under multiaxial loading, and fatigue behavior with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university composite materials courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating rule of mixtures elastic bounds, Halpin-Tsai modulus predictions, shear-lag load transfer lengths, lamina stiffness transformations, and Tsai-Hill failure envelopes. Numerical checks and an editorial review support this edition.',
    keywords: ['Composite Materials', 'Fiber Reinforcement', 'Rule of Mixtures', 'Micromechanics', 'Laminates', 'Tsai-Hill Criterion', 'Delamination', 'Matrix'],
    refPath: 'publishing/drafts/materials-science-and-engineering-composite-materials/references.json'
  }
];

const templateHtml = fs.readFileSync(
  path.join(groupedRoot, 'statistics-probability', 'statistical-simulation-and-monte-carlo-methods', 'statistical-simulation-and-monte-carlo-methods.html'),
  'utf8'
);

for (const cfg of bookConfigs) {
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

  d.querySelectorAll('link[rel="stylesheet"]').forEach(link => {
    const href = link.getAttribute('href');
    if (href && (href.startsWith('../../') || href.startsWith('../'))) {
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
      <div class="editorial-signoff">OpenSTEM Editorial Board • Materials Science & Engineering Division</div>
    `;
  }

  const refBlock = d.querySelector('.references-block');
  if (refBlock && fs.existsSync(path.join(root, cfg.refPath))) {
    const refs = JSON.parse(fs.readFileSync(path.join(root, cfg.refPath), 'utf8'));
    const refItems = refs.sources.map(s => `<li><strong>${s.institution}</strong>: ${s.role}</li>`).join('\n');
    refBlock.innerHTML = `
      <h3>Authoritative Academic Benchmarks & Citations</h3>
      <p>This textbook synthesizes canonical university curricula and established materials science references:</p>
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

  const bookDataJs = fs.readFileSync(path.join(groupedRoot, 'materials-science-and-engineering', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
  w.eval(bookDataJs);
  const appJs = fs.readFileSync(path.join(root, 'app.js'), 'utf8').split('\nif (document.readyState === "loading")')[0];
  w.eval(appJs);
  w.startApp();

  d.getElementById('unit-title').textContent = w.COURSE_DATA.units[0].title;
  d.getElementById('unit-desc').textContent = w.COURSE_DATA.units[0].leadSummary || '';
  d.querySelectorAll('.mobile-chapters-button,.chapter-menu-close,.chapter-menu-backdrop').forEach(el => el.remove());
  d.querySelector('.sidebar').removeAttribute('id');

  const targetDir = path.join(groupedRoot, 'materials-science-and-engineering', cfg.slug);
  fs.mkdirSync(targetDir, { recursive: true });
  const targetHtmlPath = path.join(targetDir, cfg.slug + '.html');
  fs.writeFileSync(targetHtmlPath, dom.serialize(), 'utf8');
  w.close();
  console.log(`Generated landing page: ${targetHtmlPath}`);
}

const ctx = { window: {} };
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(root, 'departments-data.js'), 'utf8'), ctx);
const catalog = ctx.window.LIBRARY_CATALOG;
let dept = catalog.departments.find(d => d.id === 'materials-science-and-engineering');
if (!dept) {
  dept = {
    id: 'materials-science-and-engineering',
    name: 'Materials Science & Engineering',
    code: 'MSE',
    icon: '🔬',
    description: 'Crystallography, thermodynamics of materials, phase transformations, mechanical behavior, polymers, ceramics, semiconductors, and biomaterials.',
    courses: []
  };
  catalog.departments.push(dept);
}

for (const cfg of bookConfigs) {
  dept.courses = dept.courses.filter(b => b.id !== cfg.slug);
  const dataJsText = fs.readFileSync(path.join(groupedRoot, 'materials-science-and-engineering', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
  const courseData = JSON.parse(dataJsText.replace(/^[\s\S]*?window\.COURSE_DATA\s*=\s*/, '').replace(/;\s*$/, ''));
  dept.courses.push({
    id: cfg.slug,
    title: cfg.title,
    subtitle: cfg.subtitle,
    status: 'AVAILABLE',
    url: cfg.slug + '.html',
    badge: 'Free Interactive Textbook',
    description: cfg.description,
    topics: courseData.units.map(u => u.title)
  });
}

fs.writeFileSync(
  path.join(root, 'departments-data.js'),
  '// OpenSTEM academic catalog: only completed books appear as available.\nwindow.LIBRARY_CATALOG = ' + JSON.stringify(catalog, null, 2) + ';\n',
  'utf8'
);
console.log(`Updated departments-data.js. Total Materials Science & Engineering courses: ${dept.courses.length}`);

const queue = JSON.parse(fs.readFileSync(path.join(root, 'publishing/book-queue.json'), 'utf8'));
let queueDept = queue.departments.find(d => d.id === 'materials-science-and-engineering');
if (!queueDept) {
  queueDept = {
    id: 'materials-science-and-engineering',
    name: 'Materials Science & Engineering',
    books: []
  };
  queue.departments.push(queueDept);
}
const now = new Date().toISOString();

for (const cfg of bookConfigs) {
  let qBook = queueDept.books.find(b => b.id === 'materials-science-and-engineering-' + cfg.slug);
  if (!qBook) {
    qBook = {
      id: 'materials-science-and-engineering-' + cfg.slug,
      title: cfg.title,
      status: 'published',
      published_at: now,
      content_file: cfg.slug + '-data.js',
      url: cfg.slug + '.html',
      qa_report: `publishing/qa/materials-science-and-engineering-${cfg.slug}.json`
    };
    queueDept.books.push(qBook);
  } else {
    qBook.status = 'published';
    qBook.published_at = now;
    qBook.content_file = cfg.slug + '-data.js';
    qBook.url = cfg.slug + '.html';
    qBook.qa_report = `publishing/qa/materials-science-and-engineering-${cfg.slug}.json`;
  }
  console.log(`Updated book-queue.json: ${qBook.id} -> published`);
}

fs.writeFileSync(
  path.join(root, 'publishing/book-queue.json'),
  JSON.stringify(queue, null, 2) + '\n',
  'utf8'
);
console.log('Updated publishing/book-queue.json successfully.');
