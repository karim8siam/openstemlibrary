const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'physical-geology',
    title: 'Physical Geology',
    subtitle: 'Plate Tectonics, Earth Structure, Igneous & Sedimentary Processes, Crustal Deformation & Geologic Time',
    seoTitle: 'Physical Geology: Plate Tectonics, Earth Structure & Crustal Processes | OpenSTEM Library',
    badgeCredits: 'Physical geology core',
    courseCodes: ['GEO 101', 'EAS 101'],
    searchPlaceholder: 'Search plate tectonics, mantle convection, oceanic crust subduction, seismic wave velocities, Bowen reaction series, rock cycle, fault mechanics, stratigraphic principles, radiometric dating, isostasy…',
    probSecTitle: 'Step-by-Step Physical Geology Solutions',
    description: 'Comprehensive university textbook covering internal Earth structure, plate tectonic theory, mineral and rock classification, magma generation, weathering and soil formation, sedimentary environments, metamorphic facies, structural deformation, and geologic time with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university physical geology courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating map distance scaling, density contrasts, isostatic equilibrium, seismic travel-time curves, and radioactive half-life decay. Numerical checks and an editorial review support this edition.',
    keywords: ['Physical Geology', 'Plate Tectonics', 'Earth Structure', 'Rock Cycle', 'Seismic Waves', 'Fault Mechanics', 'Stratigraphy', 'Geologic Time'],
    refPath: 'publishing/drafts/earth-space-sciences-physical-geology/references.json'
  },
  {
    slug: 'mineralogy',
    title: 'Mineralogy',
    subtitle: 'Crystal Chemistry, Crystallography, Silicate Frameworks, Optical Mineralogy & Mineral Thermodynamics',
    seoTitle: 'Mineralogy: Crystal Chemistry, Crystallography & Optical Properties | OpenSTEM Library',
    badgeCredits: 'Mineralogy core',
    courseCodes: ['GEO 201', 'MIN 201'],
    searchPlaceholder: 'Search crystal systems, Miller indices, Bragg diffraction law, Pauling rules of coordination, solid solutions, silicate polymerizations (neso-, soro-, ino-, phyllo-, tecto-), birefringence, Becke line test, Gibbs free energy phase relations…',
    probSecTitle: 'Step-by-Step Mineralogy Solutions',
    description: 'Comprehensive university textbook covering crystal lattices and symmetry operations, crystal chemistry and ionic bonding, silicate and non-silicate mineral classification, optical mineralogy in thin section, X-ray diffraction principles, and mineral phase stability with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university mineralogy courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating unit cell volume, coordination number radii, solid solution molar masses, Bragg diffraction angles, and refractive index birefringence. Numerical checks and an editorial review support this edition.',
    keywords: ['Mineralogy', 'Crystallography', 'Crystal Chemistry', 'Silicates', 'Optical Mineralogy', 'X-Ray Diffraction', 'Bragg Law', 'Mineral Thermodynamics'],
    refPath: 'publishing/drafts/earth-space-sciences-mineralogy/references.json'
  },
  {
    slug: 'igneous-metamorphic-petrology',
    title: 'Igneous and Metamorphic Petrology',
    subtitle: 'Magma Genesis, Fractional Crystallization, Metamorphic Facies, Geothermobarometry & Tectonic Settings',
    seoTitle: 'Igneous & Metamorphic Petrology: Magma Genesis & Metamorphic Facies | OpenSTEM Library',
    badgeCredits: 'Petrology core',
    courseCodes: ['GEO 301', 'PET 301'],
    searchPlaceholder: 'Search binary eutectic phase diagrams, ternary feldspar systems, fractional vs equilibrium crystallization, mantle partial melting, trace element partition coefficients, Harker variation diagrams, metamorphic index minerals, AFM and ACF compatibility diagrams, geothermobarometry…',
    probSecTitle: 'Step-by-Step Petrology Solutions',
    description: 'Comprehensive university textbook covering thermodynamics of silicate melts, phase equilibria, fractional crystallization, magma ascent and emplacement, basaltic and granitic suites, metamorphic heat and pressure regimes, metamorphic facies series, and geothermobarometric modeling with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university petrology courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating eutectic melting fractions, Rayleigh fractional crystallization, mineral modal abundance, geobarometric pressure gradients, and metamorphic reaction kinetics. Numerical checks and an editorial review support this edition.',
    keywords: ['Igneous Petrology', 'Metamorphic Petrology', 'Phase Equilibria', 'Magma Genesis', 'Fractional Crystallization', 'Metamorphic Facies', 'Geothermobarometry', 'Tectonic Petrology'],
    refPath: 'publishing/drafts/earth-space-sciences-igneous-metamorphic-petrology/references.json'
  },
  {
    slug: 'sedimentology-and-stratigraphy',
    title: 'Sedimentology and Stratigraphy',
    subtitle: 'Sedimentary Processes, Depositional Environments, Facies Models, Sequence Stratigraphy & Basin Analysis',
    seoTitle: 'Sedimentology & Stratigraphy: Depositional Environments & Basin Analysis | OpenSTEM Library',
    badgeCredits: 'Sedimentology core',
    courseCodes: ['GEO 305', 'SED 301'],
    searchPlaceholder: 'Search grain size Udden-Wentworth scale, settling velocity Stokes law, bedform stability diagrams, Hjulström entrainment diagram, turbidity currents and Bouma sequence, carbonate platform facies, Walther law of facies correlation, sequence stratigraphy accommodation space, chronostratigraphy…',
    probSecTitle: 'Step-by-Step Sedimentology Solutions',
    description: 'Comprehensive university textbook covering sediment transport fluid dynamics, primary sedimentary structures, clastic and carbonate depositional environments, facies associations, sequence stratigraphy systems tracts (LST, TST, HST), biostratigraphic correlation, and sedimentary basin subsidence modeling with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university sedimentology and stratigraphy courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating grain settling velocities, cross-bedding paleoflow vectors, porosity loss compaction curves, accommodation-to-sediment supply ratios, and subsidence curves. Numerical checks and an editorial review support this edition.',
    keywords: ['Sedimentology', 'Stratigraphy', 'Depositional Environments', 'Sediment Transport', 'Sequence Stratigraphy', 'Facies Analysis', 'Basin Subsidence', 'Chronostratigraphy'],
    refPath: 'publishing/drafts/earth-space-sciences-sedimentology-and-stratigraphy/references.json'
  },
  {
    slug: 'structural-geology',
    title: 'Structural Geology',
    subtitle: 'Stress & Strain Mechanics, Brittle Faulting, Ductile Folding, Rheology & Tectonic Deformation',
    seoTitle: 'Structural Geology: Stress, Strain, Faulting & Ductile Folding | OpenSTEM Library',
    badgeCredits: 'Structural geology core',
    courseCodes: ['GEO 310', 'STR 301'],
    searchPlaceholder: 'Search principal stress axes, Mohr stress circle, Coulomb-Mohr failure criterion, Andersonian fault classification, finite strain ellipses, stereonet projection of planes and lineations, fold geometry (anticline, syncline, cylindrical folds), shear zone kinematics, mylonite foliation, balanced cross sections…',
    probSecTitle: 'Step-by-Step Structural Geology Solutions',
    description: 'Comprehensive university textbook covering stress tensors, finite and infinitesimal strain analysis, brittle fracture mechanics, Anderson fault dynamics, fold kinematics and buckling theory, ductile shear zones, rock rheology, and tectonic reconstruction with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university structural geology courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating Mohr circle shear stress, fault dip slip components, fold interlimb angles, strain ellipse axial ratios, and lithostatic pressure depth relations. Numerical checks and an editorial review support this edition.',
    keywords: ['Structural Geology', 'Stress and Strain', 'Mohr Circle', 'Fault Mechanics', 'Fold Kinematics', 'Stereonets', 'Shear Zones', 'Rock Rheology'],
    refPath: 'publishing/drafts/earth-space-sciences-structural-geology/references.json'
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

  d.body.dataset.bookPath = cfg.slug + '.html';
  d.body.dataset.chapterIndex = '0';
  d.querySelector('.brand-title').textContent = cfg.title;
  d.querySelector('.badge-credits').textContent = cfg.badgeCredits;
  d.getElementById('topic-search-input').placeholder = cfg.searchPlaceholder;

  d.querySelectorAll('.textbook-section-card,.problem-card,.chapter-pagination,.stat-editorial-note,.mobile-chapters-button,.chapter-menu-close,.chapter-menu-backdrop').forEach(el => el.remove());
  d.getElementById('textbook-sections').innerHTML = '';
  (d.getElementById('problems-mount') || d.getElementById('problems-container') || d.getElementById('problem-cards-list')).innerHTML = '';
  d.querySelector('.sidebar').removeAttribute('id');

  const probSec = d.querySelector('.prob-sec-title');
  if (probSec) probSec.textContent = cfg.probSecTitle;

  // Replace script and css links from old slug to this book's slug
  for (const el of d.querySelectorAll('script[src],link[rel="stylesheet"]')) {
    const attr = el.tagName === 'SCRIPT' ? 'src' : 'href';
    const src = el.getAttribute(attr);
    if (src && src.includes('statistical-simulation-and-monte-carlo-methods')) {
      el.setAttribute(attr, src.replace(/statistical-simulation-and-monte-carlo-methods/g, cfg.slug));
    }
  }

  // Editorial note
  const note = d.createElement('aside');
  note.className = 'stat-editorial-note';
  note.setAttribute('aria-label', 'About this textbook');
  note.innerHTML = cfg.editorialNote;
  d.querySelector('.unit-hero').after(note);

  // References and trust footer
  const refs = JSON.parse(fs.readFileSync(path.join(root, cfg.refPath), 'utf8'));
  const trustNav = '<nav class="reader-trust-links" aria-label="Related reading">' +
    '<a href="index#dept-earth-space-sciences">Earth & Space Sciences Department</a>' +
    '<a href="physical-geology">Physical Geology</a>' +
    '<a href="mineralogy">Mineralogy</a>' +
    '<a href="igneous-metamorphic-petrology">Petrology</a>' +
    '<a href="sedimentology-and-stratigraphy">Sedimentology & Stratigraphy</a>' +
    '<a href="structural-geology">Structural Geology</a>' +
    '<a href="mechanics">Classical Mechanics prerequisite</a>' +
    '<a href="calculus-1">Calculus prerequisite</a>' +
    '<a href="physical-chemistry-1">Physical Chemistry prerequisite</a>' +
    '<a href="introduction-to-statistics">Statistics prerequisite</a>' +
    '<a href="about">About & editorial</a>' +
    '<a href="privacy">Privacy</a>' +
    '<a href="terms">Terms</a>' +
    '<a href="mailto:shahriyarkarimsiam@gmail.com">Report a correction</a>' +
    '</nav>';
  const trustRefs = '<details><summary>Curriculum and academic references</summary><ul>' +
    refs.sources.map(s => `<li><a href="${s.url}" target="_blank" rel="noopener noreferrer">${s.institution}: ${s.role}</a></li>`).join('') +
    '</ul></details>';
  const trustCopy = '<p class="reader-trust-copy">© 2026 OpenSTEM Library • Free original educational textbook</p>';
  d.querySelector('.reader-trust-footer').innerHTML = trustNav + trustRefs + trustCopy;

  // Schema.org tags
  d.querySelectorAll('script[type="application/ld+json"]').forEach(el => el.remove());
  function addSchema(data) {
    const s = d.createElement('script');
    s.type = 'application/ld+json';
    s.textContent = JSON.stringify(data);
    d.head.append(s);
  }

  addSchema({
    '@context': 'https://schema.org',
    '@type': 'Book',
    name: cfg.title,
    description: cfg.description,
    url: 'https://openstemlibrary.com/' + cfg.slug,
    inLanguage: 'en',
    isAccessibleForFree: true,
    educationalLevel: 'Undergraduate',
    author: { '@type': 'Organization', name: 'OpenSTEM Library' },
    publisher: { '@type': 'Organization', name: 'OpenSTEM Library', url: 'https://openstemlibrary.com/' },
    learningResourceType: 'Textbook',
    about: cfg.keywords
  });

  addSchema({
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'OpenSTEM Library', item: 'https://openstemlibrary.com/' },
      { '@type': 'ListItem', position: 2, name: 'Earth & Space Sciences', item: 'https://openstemlibrary.com/#dept-earth-space-sciences' },
      { '@type': 'ListItem', position: 3, name: cfg.title, item: 'https://openstemlibrary.com/' + cfg.slug }
    ]
  });

  // Evaluate book data and startApp
  const bookDataJs = fs.readFileSync(path.join(groupedRoot, 'earth-space-sciences', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
  w.eval(bookDataJs);
  const appJs = fs.readFileSync(path.join(root, 'app.js'), 'utf8').split('\nif (document.readyState === "loading")')[0];
  w.eval(appJs);
  w.startApp();

  d.getElementById('unit-title').textContent = w.COURSE_DATA.units[0].title;
  d.getElementById('unit-desc').textContent = w.COURSE_DATA.units[0].leadSummary || '';
  d.querySelectorAll('.mobile-chapters-button,.chapter-menu-close,.chapter-menu-backdrop').forEach(el => el.remove());
  d.querySelector('.sidebar').removeAttribute('id');

  const targetDir = path.join(groupedRoot, 'earth-space-sciences', cfg.slug);
  fs.mkdirSync(targetDir, { recursive: true });
  const targetHtmlPath = path.join(targetDir, cfg.slug + '.html');
  fs.writeFileSync(targetHtmlPath, dom.serialize(), 'utf8');
  w.close();
  console.log(`Generated landing page: ${targetHtmlPath}`);
}

// Update departments-data.js
const ctx = { window: {} };
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(root, 'departments-data.js'), 'utf8'), ctx);
const catalog = ctx.window.LIBRARY_CATALOG;
let dept = catalog.departments.find(d => d.id === 'earth-space-sciences');
if (!dept) {
  dept = {
    id: 'earth-space-sciences',
    name: 'Earth & Space Sciences',
    code: 'EAS',
    icon: '🌍',
    description: 'Physical geology, mineralogy, petrology, geophysics, geochemistry, oceanography, atmospheric sciences, meteorology, climatology, and planetary science.',
    courses: []
  };
  catalog.departments.push(dept);
}

for (const cfg of bookConfigs) {
  dept.courses = dept.courses.filter(b => b.id !== cfg.slug);
  const dataJsText = fs.readFileSync(path.join(groupedRoot, 'earth-space-sciences', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
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
console.log(`Updated departments-data.js. Total Earth & Space Sciences courses: ${dept.courses.length}`);

// Update publishing/book-queue.json
const queue = JSON.parse(fs.readFileSync(path.join(root, 'publishing/book-queue.json'), 'utf8'));
let queueDept = queue.departments.find(d => d.id === 'earth-space-sciences');
const now = new Date().toISOString();

for (const cfg of bookConfigs) {
  let qBook = queueDept.books.find(b => b.id === 'earth-space-sciences-' + cfg.slug || b.id === 'earth-space-sciences-' + cfg.slug.replace('igneous-metamorphic-', ''));
  if (!qBook) {
    qBook = {
      id: 'earth-space-sciences-' + cfg.slug,
      title: cfg.title,
      status: 'published',
      published_at: now,
      content_file: cfg.slug + '-data.js',
      url: cfg.slug + '.html',
      qa_report: `publishing/qa/earth-space-sciences-${cfg.slug}.json`
    };
    queueDept.books.push(qBook);
  } else {
    qBook.status = 'published';
    qBook.published_at = now;
    qBook.content_file = cfg.slug + '-data.js';
    qBook.url = cfg.slug + '.html';
    qBook.qa_report = `publishing/qa/earth-space-sciences-${cfg.slug}.json`;
  }
  console.log(`Updated book-queue.json: ${qBook.id} -> published`);
}

fs.writeFileSync(
  path.join(root, 'publishing/book-queue.json'),
  JSON.stringify(queue, null, 2) + '\n',
  'utf8'
);
console.log('Updated publishing/book-queue.json successfully.');
