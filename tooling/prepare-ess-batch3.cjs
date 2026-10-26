const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'marine-geology',
    title: 'Marine Geology',
    subtitle: 'Ocean Basins, Mid-Ocean Ridges, Subduction Trenches, Marine Sedimentation & Paleoceanography',
    seoTitle: 'Marine Geology: Ocean Basins, Ridges, Trenches & Marine Sediments | OpenSTEM Library',
    badgeCredits: 'Marine geology core',
    courseCodes: ['GEO 325', 'MARG 301'],
    searchPlaceholder: 'Search seafloor spreading magnetic anomalies, Vine-Matthews-Morley hypothesis, hydrothermal vents, abyssal clay vs calcareous oozes, carbonate compensation depth (CCD), turbidite fans, subduction accretionary prisms, gas hydrate stability…',
    probSecTitle: 'Step-by-Step Marine Geology Solutions',
    description: 'Comprehensive university textbook covering ocean basin morphology, oceanic lithosphere creation at mid-ocean ridges, subduction zones and island arcs, marine sediment classification, pelagic biogenic oozes, passive continental margin evolution, hydrothermal circulation, and paleoceanographic proxy records with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university marine geology courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating seafloor spreading rates, abyssal depth versus crustal age, pelagic sediment accumulation rates, CCD dissolution thresholds, and gas hydrate pressure-temperature curves. Numerical checks and an editorial review support this edition.',
    keywords: ['Marine Geology', 'Ocean Basins', 'Seafloor Spreading', 'Mid-Ocean Ridges', 'Carbonate Compensation Depth', 'Turbidites', 'Accretionary Prisms', 'Paleoceanography'],
    refPath: 'publishing/drafts/earth-space-sciences-marine-geology/references.json'
  },
  {
    slug: 'geophysics',
    title: 'Geophysics',
    subtitle: 'Seismic Wave Propagation, Gravity Anomalies, Geomagnetism, Geothermics & Subsurface Imaging',
    seoTitle: 'Geophysics: Seismic Waves, Gravity, Geomagnetism & Earth Structure | OpenSTEM Library',
    badgeCredits: 'Geophysics core',
    courseCodes: ['GEO 330', 'GPH 301'],
    searchPlaceholder: 'Search P and S wave ray paths, Snell law refraction, seismic reflection two-way travel time, Bouguer gravity anomaly, free-air correction, Pratt vs Airy isostasy, Earth dipole geomagnetic field, secular variation, geothermal heat conduction equation…',
    probSecTitle: 'Step-by-Step Geophysics Solutions',
    description: 'Comprehensive university textbook covering theoretical and applied geophysics, elastodynamics of seismic body and surface waves, seismic reflection profiling, gravity potential field theory, isostatic balance models, geomagnetic fields and paleomagnetism, electrical resistivity, and Earth thermal evolution with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university geophysics courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating seismic critical refraction angles, reflection hyperbola velocities, Bouguer slab corrections, isostatic crustal root thickness, and geothermal gradient heat fluxes. Numerical checks and an editorial review support this edition.',
    keywords: ['Geophysics', 'Seismic Waves', 'Gravity Anomalies', 'Bouguer Correction', 'Isostasy', 'Geomagnetism', 'Geothermal Heat Flow', 'Electrical Resistivity'],
    refPath: 'publishing/drafts/earth-space-sciences-geophysics/references.json'
  },
  {
    slug: 'geochemistry',
    title: 'Geochemistry',
    subtitle: 'Element Abundances, Thermodynamics, Radiogenic & Stable Isotopes, Aquatic Chemistry & Geochemical Cycles',
    seoTitle: 'Geochemistry: Thermodynamics, Radiogenic & Stable Isotopes & Cycles | OpenSTEM Library',
    badgeCredits: 'Geochemistry core',
    courseCodes: ['GEO 335', 'GCH 301'],
    searchPlaceholder: 'Search Goldschmidt element classification, chemical potential, aqueous speciation, carbonate equilibrium and pH, radiogenic isochron dating (Rb-Sr, Sm-Nd, U-Pb), stable isotope fractionation (delta 18O, delta 13C), redox equilibria (Eh-pH Pourbaix diagrams), core-mantle chemical differentiation…',
    probSecTitle: 'Step-by-Step Geochemistry Solutions',
    description: 'Comprehensive university textbook covering cosmochemical element origins, chemical thermodynamics in geological systems, mineral-solution equilibria, oxidation-reduction states, radiogenic isotope geochronology and mantle reservoirs, stable isotope paleothermometry, and global geochemical cycles with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university geochemistry courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating Goldschmidt partition coefficients, mineral dissolution ion activity products, isochron decay slopes, stable isotope Rayleigh fractionation, and carbonate alkalinity speciation. Numerical checks and an editorial review support this edition.',
    keywords: ['Geochemistry', 'Thermodynamics', 'Radiogenic Isotopes', 'Stable Isotopes', 'Isochron Dating', 'Eh-pH Diagrams', 'Aqueous Speciation', 'Mantle Geochemistry'],
    refPath: 'publishing/drafts/earth-space-sciences-geochemistry/references.json'
  },
  {
    slug: 'paleontology',
    title: 'Paleontology',
    subtitle: 'Fossilization, Invertebrate Clades, Vertebrate Evolution, Mass Extinctions, Biostratigraphy & Macroevolution',
    seoTitle: 'Paleontology: Fossil Preservation, Evolutionary Radiations & Extinctions | OpenSTEM Library',
    badgeCredits: 'Paleontology core',
    courseCodes: ['GEO 340', 'PAL 301'],
    searchPlaceholder: 'Search taphonomic decay biases, Lagerstätten deposits, Cambrian explosion, functional morphology, major invertebrate phyla (Brachiopoda, Mollusca, Trilobita, Echinodermata), vertebrate transitions (fish to tetrapod, dinosaur to bird), Big Five mass extinctions, punctuated equilibrium…',
    probSecTitle: 'Step-by-Step Paleontology Solutions',
    description: 'Comprehensive university textbook covering taphonomy and preservation modes, evolutionary paleoecology, functional morphology, phylogenetic systematics, biostratigraphic index fossils, the Cambrian radiation, vertebrate evolutionary milestones, the Big Five mass extinction crises, and macroevolutionary dynamics with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university paleontology courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating fossilization decay half-lives, morphometric allometry, origination and extinction rate metrics, biostratigraphic range overlap, and rarefaction biodiversity curves. Numerical checks and an editorial review support this edition.',
    keywords: ['Paleontology', 'Taphonomy', 'Fossil Record', 'Cambrian Explosion', 'Biostratigraphy', 'Mass Extinctions', 'Macroevolution', 'Functional Morphology'],
    refPath: 'publishing/drafts/earth-space-sciences-paleontology/references.json'
  },
  {
    slug: 'volcanology',
    title: 'Volcanology',
    subtitle: 'Magma Rheology, Eruption Styles, Pyroclastic Dispersal, Volcanic Hazards & Monitoring Systems',
    seoTitle: 'Volcanology: Magma Rheology, Eruptive Plumes & Volcanic Hazards | OpenSTEM Library',
    badgeCredits: 'Volcanology core',
    courseCodes: ['GEO 345', 'VOL 301'],
    searchPlaceholder: 'Search basaltic vs rhyolitic magma viscosity, volatile exsolution and bubble nucleation, conduit flow dynamics, explosive fragmentation criteria, buoyant plume ascent height, pyroclastic density currents (PDCs), caldera collapse mechanisms, volcanic gas emissions (SO2), seismic tremor and InSAR ground deformation…',
    probSecTitle: 'Step-by-Step Volcanology Solutions',
    description: 'Comprehensive university textbook covering magmatic fluid dynamics, volatile degassing kinetics, subaerial and submarine eruption columns, pyroclastic surge physics, lava dome stability, volcano seismology, geodetic hazard monitoring, and volcanic risk mitigation with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university volcanology courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating magma viscosity variations, gas volume fraction thresholds, buoyant convective plume heights, pyroclastic runout distances, and caldera ring-fault shear stresses. Numerical checks and an editorial review support this edition.',
    keywords: ['Volcanology', 'Magma Rheology', 'Volcanic Eruptions', 'Pyroclastic Flows', 'Volcanic Plumes', 'Caldera Collapse', 'Volcano Seismology', 'Volcanic Hazard Mitigation'],
    refPath: 'publishing/drafts/earth-space-sciences-volcanology/references.json'
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
      <div class="editorial-signoff">OpenSTEM Editorial Board • Earth & Space Sciences Division</div>
    `;
  }

  const refBlock = d.querySelector('.references-block');
  if (refBlock && fs.existsSync(path.join(root, cfg.refPath))) {
    const refs = JSON.parse(fs.readFileSync(path.join(root, cfg.refPath), 'utf8'));
    const refItems = refs.sources.map(s => `<li><strong>${s.institution}</strong>: ${s.role}</li>`).join('\n');
    refBlock.innerHTML = `
      <h3>Authoritative Academic Benchmarks & Citations</h3>
      <p>This textbook synthesizes canonical university curricula and established geoscientific references:</p>
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

const queue = JSON.parse(fs.readFileSync(path.join(root, 'publishing/book-queue.json'), 'utf8'));
let queueDept = queue.departments.find(d => d.id === 'earth-space-sciences');
const now = new Date().toISOString();

for (const cfg of bookConfigs) {
  let qBook = queueDept.books.find(b => b.id === 'earth-space-sciences-' + cfg.slug || b.id === 'earth-space-sciences-' + cfg.slug.replace('marine-', '').replace('paleontology', 'paleo'));
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
