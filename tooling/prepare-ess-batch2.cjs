const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'geomorphology',
    title: 'Geomorphology',
    subtitle: 'Fluvial Landscapes, Hillslope Processes, Glacial Dynamics, Coastal Landforms & Tectonic Geomorphology',
    seoTitle: 'Geomorphology: Fluvial Landscapes, Hillslopes & Coastal Landforms | OpenSTEM Library',
    badgeCredits: 'Geomorphology core',
    courseCodes: ['GEO 315', 'GEOM 301'],
    searchPlaceholder: 'Search stream power incision law, critical shear stress, hillslope diffusion and soil creep, debris flow rheology, glacial equilibrium line altitude (ELA), coastal wave refraction, tectonic knickpoint migration, cosmogenic isotope erosion rates…',
    probSecTitle: 'Step-by-Step Geomorphology Solutions',
    description: 'Comprehensive university textbook covering mechanical and chemical weathering, hillslope transport laws, channel network geometry, fluvial sediment routing, glacial valley evolution, periglacial landforms, coastal littoral drift, and tectonic landscape evolution with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university geomorphology courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating hillslope slope-flux relations, critical shear velocity, glacial ice discharge, coastal wave power, and steady-state landscape relief. Numerical checks and an editorial review support this edition.',
    keywords: ['Geomorphology', 'Fluvial Processes', 'Hillslope Mechanics', 'Glacial Dynamics', 'Coastal Landforms', 'Soil Creep', 'Stream Power Law', 'Landscape Evolution'],
    refPath: 'publishing/drafts/earth-space-sciences-geomorphology/references.json'
  },
  {
    slug: 'hydrology-and-hydrogeology',
    title: 'Hydrology and Hydrogeology',
    subtitle: 'Catchment Hydrology, Precipitation-Runoff Dynamics, Darcy Aquifer Flow & Contaminant Transport',
    seoTitle: 'Hydrology & Hydrogeology: Catchment Water Balances & Groundwater Flow | OpenSTEM Library',
    badgeCredits: 'Hydrogeology core',
    courseCodes: ['GEO 320', 'HYD 301'],
    searchPlaceholder: 'Search water balance equation, Penman-Monteith evapotranspiration, Horton vs Dunne overland flow, unit hydrograph routing, Darcy law hydraulic conductivity, Theis well hydraulics, Dupuit-Forchheimer unconfined flow, advection-dispersion plume migration…',
    probSecTitle: 'Step-by-Step Hydrogeology Solutions',
    description: 'Comprehensive university textbook covering surface hydrological cycles, precipitation metrics, infiltration models (Green-Ampt), streamflow hydrograph analysis, saturated and unsaturated groundwater flow, pumping test well hydraulics, aquifer storage properties, and subsurface solute transport with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university hydrology courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating water budget balances, infiltration capacity curves, Darcy discharge fluxes, Theis drawdown cones, and Gaussian solute dispersion plumes. Numerical checks and an editorial review support this edition.',
    keywords: ['Hydrology', 'Hydrogeology', 'Catchment Water Balance', 'Darcy Law', 'Aquifer Hydraulics', 'Theis Equation', 'Infiltration Kinetics', 'Contaminant Transport'],
    refPath: 'publishing/drafts/earth-space-sciences-hydrology-and-hydrogeology/references.json'
  },
  {
    slug: 'meteorology-and-atmospheric-science',
    title: 'Meteorology and Atmospheric Science',
    subtitle: 'Atmospheric Thermodynamics, Hydrostatic Balance, Synoptic Dynamics, Frontogenesis & Severe Storms',
    seoTitle: 'Meteorology: Atmospheric Thermodynamics, Synoptic Dynamics & Fronts | OpenSTEM Library',
    badgeCredits: 'Meteorology core',
    courseCodes: ['ATM 201', 'MET 201'],
    searchPlaceholder: 'Search hypsometric equation, dry and moist adiabatic lapse rates, skew-T log-P thermodynamic diagrams, CAPE and CIN convective stability, geostrophic and gradient wind approximations, thermal wind balance, quasi-geostrophic omega equation, polar front theory, Doppler radar reflectivity…',
    probSecTitle: 'Step-by-Step Meteorology Solutions',
    description: 'Comprehensive university textbook covering atmospheric structure and composition, radiative equilibrium, dry and saturated parcel thermodynamics, cloud microphysics, equations of horizontal motion, synoptic weather maps and jet streams, midlatitude cyclones, and convective storm dynamics with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university meteorology courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating hydrostatic layer thickness, adiabatic lapse cooling, geostrophic wind speeds, thermal wind shear, and convective CAPE integration. Numerical checks and an editorial review support this edition.',
    keywords: ['Meteorology', 'Atmospheric Science', 'Hydrostatic Balance', 'Adiabatic Lapse Rate', 'Skew-T Diagrams', 'Geostrophic Wind', 'Frontogenesis', 'Severe Weather'],
    refPath: 'publishing/drafts/earth-space-sciences-meteorology-and-atmospheric-science/references.json'
  },
  {
    slug: 'climatology-and-climate-science',
    title: 'Climatology and Climate Science',
    subtitle: 'Global Energy Budgets, General Circulation, Paleoclimate Forcings, Feedback Loops & Climate Modeling',
    seoTitle: 'Climatology: Global Energy Balance, Paleoclimate & Climate Forcings | OpenSTEM Library',
    badgeCredits: 'Climatology core',
    courseCodes: ['ATM 301', 'CLI 301'],
    searchPlaceholder: 'Search Stefan-Boltzmann planetary energy balance, greenhouse effect optical depth, Hadley cell circulation, trade winds and ITCZ, Milankovitch orbital cycles, ice-albedo and water vapor feedbacks, ocean overturning circulation (AMOC), transient climate response, carbon cycle reservoirs…',
    probSecTitle: 'Step-by-Step Climatology Solutions',
    description: 'Comprehensive university textbook covering Earth radiation budgets, planetary boundary layer climatology, ocean-atmosphere coupled systems, teleconnections (ENSO, NAO, PDO), Quaternary glacial-interglacial cycles, climate sensitivity metrics, biogeochemical climate feedbacks, and IPCC radiative forcing projections with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university climatology courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating zero-dimensional energy balances, greenhouse absorption fractions, orbital insolation variation, ice-albedo bifurcation tipping points, and radiative forcing temperature responses. Numerical checks and an editorial review support this edition.',
    keywords: ['Climatology', 'Climate Science', 'Planetary Energy Balance', 'Hadley Circulation', 'Milankovitch Cycles', 'Climate Feedbacks', 'Radiative Forcing', 'Carbon Cycle'],
    refPath: 'publishing/drafts/earth-space-sciences-climatology-and-climate-science/references.json'
  },
  {
    slug: 'oceanography',
    title: 'Oceanography',
    subtitle: 'Seawater Thermodynamics, Wind-Driven Gyres, Thermohaline Circulation, Tides & Marine Ecology',
    seoTitle: 'Oceanography: Physical Circulation, Waves, Tides & Marine Geochemistry | OpenSTEM Library',
    badgeCredits: 'Oceanography core',
    courseCodes: ['OCE 201', 'MAR 201'],
    searchPlaceholder: 'Search equation of state of seawater (TEOS-10), potential density and stratification, Ekman transport and spiral, geostrophic ocean currents, western boundary current intensification, deep ocean thermohaline circulation, shallow vs deep water waves, amphidromic tidal systems, oceanic nutrient profiles…',
    probSecTitle: 'Step-by-Step Oceanography Solutions',
    description: 'Comprehensive university textbook covering marine physiography, chemical composition of seawater, sound and light propagation in water, surface wind stress and Ekman dynamics, subtropical gyres and western boundary currents, abyssal ocean overturning, wave kinematics, tidal harmonic analysis, and marine primary production with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university oceanography courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating hydrostatic ocean pressure, Ekman drift velocities, geostrophic sea surface slopes, deep water wave celerity, and tidal resonance periods. Numerical checks and an editorial review support this edition.',
    keywords: ['Oceanography', 'Marine Science', 'Seawater Thermodynamics', 'Ekman Transport', 'Geostrophic Gyres', 'Thermohaline Circulation', 'Ocean Waves', 'Tidal Harmonics'],
    refPath: 'publishing/drafts/earth-space-sciences-oceanography/references.json'
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

  for (const el of d.querySelectorAll('script[src],link[rel="stylesheet"]')) {
    const attr = el.tagName === 'SCRIPT' ? 'src' : 'href';
    const src = el.getAttribute(attr);
    if (src && src.includes('statistical-simulation-and-monte-carlo-methods')) {
      el.setAttribute(attr, src.replace(/statistical-simulation-and-monte-carlo-methods/g, cfg.slug));
    }
  }

  const note = d.createElement('aside');
  note.className = 'stat-editorial-note';
  note.setAttribute('aria-label', 'About this textbook');
  note.innerHTML = cfg.editorialNote;
  d.querySelector('.unit-hero').after(note);

  const refs = JSON.parse(fs.readFileSync(path.join(root, cfg.refPath), 'utf8'));
  const trustNav = '<nav class="reader-trust-links" aria-label="Related reading">' +
    '<a href="index#dept-earth-space-sciences">Earth & Space Sciences Department</a>' +
    '<a href="physical-geology">Physical Geology</a>' +
    '<a href="mineralogy">Mineralogy</a>' +
    '<a href="igneous-metamorphic-petrology">Petrology</a>' +
    '<a href="sedimentology-and-stratigraphy">Sedimentology & Stratigraphy</a>' +
    '<a href="structural-geology">Structural Geology</a>' +
    '<a href="geomorphology">Geomorphology</a>' +
    '<a href="hydrology-and-hydrogeology">Hydrology & Hydrogeology</a>' +
    '<a href="meteorology-and-atmospheric-science">Meteorology</a>' +
    '<a href="climatology-and-climate-science">Climatology</a>' +
    '<a href="oceanography">Oceanography</a>' +
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
  let qBook = queueDept.books.find(b => b.id === 'earth-space-sciences-' + cfg.slug || b.id === 'earth-space-sciences-' + cfg.slug.replace('hydrology-and-', '').replace('-and-climate-science', '').replace('-and-atmospheric-science', ''));
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
