const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'seismology',
    title: 'Seismology',
    subtitle: 'Earthquake Source Mechanics, Wave Propagation, Earth Interior Structure & Seismic Inversion',
    seoTitle: 'Seismology: Earthquake Mechanics, Ray Paths & Earth Structure | OpenSTEM Library',
    badgeCredits: 'Seismology core',
    courseCodes: ['GEO 350', 'SEIS 301'],
    searchPlaceholder: 'Search elastodynamics wave equation, P and S body waves, Rayleigh and Love surface waves, Snell ray parameter, Wadati-Benioff zones, seismic moment tensor (M0), focal mechanism beachballs, Gutenberg-Richter frequency-magnitude relation…',
    probSecTitle: 'Step-by-Step Seismology Solutions',
    description: 'Comprehensive university textbook covering stress and strain tensors, elastodynamic wave propagation, travel time curves, spherical Earth ray tracing, earthquake source kinematics, double-couple moment tensors, free oscillations, and tomography with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university seismology courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating seismic ray refraction angles, surface wave dispersion velocities, moment tensor focal mechanisms, and earthquake magnitude scaling. Numerical checks and an editorial review support this edition.',
    keywords: ['Seismology', 'Earthquakes', 'Seismic Waves', 'Moment Tensor', 'Ray Tracing', 'Earth Structure', 'Focal Mechanism', 'Seismic Tomography'],
    refPath: 'publishing/drafts/earth-space-sciences-seismology/references.json'
  },
  {
    slug: 'geodesy-and-earth-observation',
    title: 'Geodesy and Earth Observation',
    subtitle: 'Reference Frames, Satellite Positioning (GNSS), Satellite Gravity, InSAR & Remote Sensing',
    seoTitle: 'Geodesy & Earth Observation: GNSS, InSAR, Satellite Gravity & Remote Sensing | OpenSTEM Library',
    badgeCredits: 'Geodesy core',
    courseCodes: ['GEO 355', 'GEOD 301'],
    searchPlaceholder: 'Search geodetic reference ellipsoids (WGS84, GRS80), geoid undulation, spherical harmonics, GNSS carrier phase positioning, ionospheric/tropospheric delays, satellite gravimetry (GRACE, GOCE), InSAR interferograms and phase unwrapping, multispectral remote sensing…',
    probSecTitle: 'Step-by-Step Geodesy & Earth Observation Solutions',
    description: 'Comprehensive university textbook covering geometric and physical geodesy, global terrestrial reference frames (ITRF), satellite orbital mechanics, GNSS precise positioning, gravity potential fields, satellite altimetry, radar interferometry (InSAR), and multispectral Earth observation with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university geodesy and remote sensing courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating ellipsoid coordinate conversions, geoid height calculations, GNSS baseline vectors, InSAR ground displacement fringes, and spectral reflectance signatures. Numerical checks and an editorial review support this edition.',
    keywords: ['Geodesy', 'Earth Observation', 'GNSS', 'GPS', 'InSAR', 'Satellite Gravity', 'Geoid', 'Remote Sensing'],
    refPath: 'publishing/drafts/earth-space-sciences-geodesy-and-earth-observation/references.json'
  },
  {
    slug: 'planetary-science',
    title: 'Planetary Science',
    subtitle: 'Solar System Formation, Planetary Geology, Atmospheres, Magnetospheres & Small Bodies',
    seoTitle: 'Planetary Science: Solar System Formation, Planetary Geology & Atmospheres | OpenSTEM Library',
    badgeCredits: 'Planetary science core',
    courseCodes: ['AST 310', 'PLAN 301'],
    searchPlaceholder: 'Search protoplanetary disk collapse, oligarchic planet growth, crater scaling laws, planetary differentiation and core dynamos, greenhouse effect on Venus vs Earth vs Mars, tidal heating of Io and Europa, Kuiper belt and Oort cloud dynamics…',
    probSecTitle: 'Step-by-Step Planetary Science Solutions',
    description: 'Comprehensive university textbook covering nebular accretion, meteorite petrology, cratering mechanics, planetary interiors and volcanism, atmospheric structure and escape mechanisms, magnetospheric interactions, icy ocean moons, and exoplanet demographics with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university planetary science courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating protoplanetary disk temperatures, Keplerian orbital periods, impact crater diameters, atmospheric scale heights, and tidal dissipation energy fluxes. Numerical checks and an editorial review support this edition.',
    keywords: ['Planetary Science', 'Solar System Formation', 'Impact Cratering', 'Planetary Atmospheres', 'Icy Moons', 'Planetary Geology', 'Exoplanets', 'Meteorites'],
    refPath: 'publishing/drafts/earth-space-sciences-planetary-science/references.json'
  },
  {
    slug: 'astrobiology',
    title: 'Astrobiology',
    subtitle: 'Origin of Life, Extreme Environments, Planetary Habitability, Biosignatures & Exoplanets',
    seoTitle: 'Astrobiology: Origin of Life, Habitability, Biosignatures & Exoplanets | OpenSTEM Library',
    badgeCredits: 'Astrobiology core',
    courseCodes: ['BIO 380', 'AST 320'],
    searchPlaceholder: 'Search prebiotic chemistry (Miller-Urey), RNA world hypothesis, hydrothermal vent ecosystems, extremophiles (halophiles, thermophiles, psychrophiles), circumstellar habitable zone boundaries, atmospheric biosignature gases (O2, O3, CH4, N2O), Enceladus and Europa plume analysis, Drake equation…',
    probSecTitle: 'Step-by-Step Astrobiology Solutions',
    description: 'Comprehensive university textbook covering prebiotic organic synthesis, geochemical environments of early Earth, metabolic evolutionary pathways, extremophile adaptations, habitability criteria for rocky planets and icy satellites, false-positive biosignature screening, and exoplanet transmission spectroscopy with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university astrobiology courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating prebiotic chemical equilibria, circumstellar habitable zone limits, atmospheric absorption transit depths, metabolic free energy yields, and Bayesian biosignature detection probabilities. Numerical checks and an editorial review support this edition.',
    keywords: ['Astrobiology', 'Origin of Life', 'Planetary Habitability', 'Biosignatures', 'Extremophiles', 'Exoplanet Atmospheres', 'Prebiotic Chemistry', 'Habitable Zone'],
    refPath: 'publishing/drafts/earth-space-sciences-astrobiology/references.json'
  },
  {
    slug: 'environmental-geoscience',
    title: 'Environmental Geoscience',
    subtitle: 'Anthropogenic Impacts, Hydrogeological Contamination, Waste Management & Geoheritage',
    seoTitle: 'Environmental Geoscience: Soil Contamination, Water Quality & Geohazards | OpenSTEM Library',
    badgeCredits: 'Environmental geoscience core',
    courseCodes: ['ENV 301', 'GEO 360'],
    searchPlaceholder: 'Search acid mine drainage (AMD) oxidation kinetics, heavy metal speciation and sorption isotherms, chlorinated solvent dense non-aqueous phase liquids (DNAPL), municipal landfill leachate liners, carbon capture and deep geological storage (CCS), environmental site assessment (ESA) protocols…',
    probSecTitle: 'Step-by-Step Environmental Geoscience Solutions',
    description: 'Comprehensive university textbook covering geological resources and footprint, hydrogeochemical contaminant fate and transport, soil degradation and remediation, geological radioactive waste disposal, mining environmental engineering, carbon mineralization and sequestration, and geohazard risk assessment with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university environmental geoscience courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating sorption partition coefficients, contaminant retardation factors, acid generation neutralization potentials, carbon storage reservoir capacities, and slope factor geohazard risks. Numerical checks and an editorial review support this edition.',
    keywords: ['Environmental Geoscience', 'Acid Mine Drainage', 'Contaminant Transport', 'Waste Disposal', 'Carbon Capture and Storage', 'Hydrogeochemistry', 'Soil Remediation', 'Geohazards'],
    refPath: 'publishing/drafts/earth-space-sciences-environmental-geoscience/references.json'
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
      <p>This textbook synthesizes canonical university curricula and established geoscientants references:</p>
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
  let qBook = queueDept.books.find(b => b.id === 'earth-space-sciences-' + cfg.slug || b.id === 'earth-space-sciences-' + cfg.slug.replace('geodesy-and-earth-observation', 'remote-sensing-of-earth').replace('environmental-geoscience', 'earth-system-science'));
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
