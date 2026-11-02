const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'fluid-mechanics-and-hydraulics',
    title: 'Fluid Mechanics and Hydraulics',
    subtitle: 'Fluid Properties, Hydrostatics, Pipe Networks, Pumps, Open Channels, Weirs & Similitude',
    seoTitle: 'Fluid Mechanics & Hydraulics: Hydrostatics, Pipe Flow & Open Channels | OpenSTEM Library',
    badgeCredits: 'Civil engineering core',
    courseCodes: ['CE 204', 'CIV 204', 'HYD 201'],
    searchPlaceholder: 'Search fluid density, dynamic and kinematic viscosity, surface tension, hydrostatic pressure distribution, center of pressure, submerged planar and curved surfaces, buoyant stability, metacenter, Bernoulli energy equation, head loss, Darcy-Weisbach friction factor, Moody chart, pipe networks, pump-system intersection, NPSH, open channel Manning equation, specific energy, critical depth, hydraulic jump, sharp-crested weirs, Venturi flumes, dimensional analysis, Buckingham Pi, Froude scale models…',
    probSecTitle: 'Step-by-Step Fluid Mechanics and Hydraulics Solutions',
    description: 'Comprehensive university textbook covering continuum fluid mechanics, hydrostatics and submerged gate forces, pressurized pipe friction and network hydraulics, pump characteristics and cavitation margins, open channel flow and specific energy, hydraulic jumps, flow measurement weirs and flumes, and dimensional similitude with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university fluid mechanics and engineering hydraulics courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating hydrostatic pressure profiles, orifice discharge, gate forces, pontoon floatation, Darcy-Weisbach pipe friction, parallel branch distribution, pump-system operating points, NPSH availability, Manning channel flow, critical depth, hydraulic jump conjugate depths, sharp-crested weirs, Venturi differential meters, culvert capacities, and Froude physical-model scaling. Numerical checks and an editorial review support this edition.',
    keywords: ['Fluid Mechanics', 'Hydraulics', 'Hydrostatics', 'Darcy-Weisbach', 'Manning Equation', 'Specific Energy', 'Hydraulic Jump', 'Centrifugal Pumps'],
    refPath: 'publishing/drafts/civil-engineering-fluid-mechanics-and-hydraulics/references.json'
  },
  {
    slug: 'hydrology',
    title: 'Hydrology',
    subtitle: 'Catchment Balances, Precipitation, Infiltration, Hydrographs, Flood Routing & Frequency Analysis',
    seoTitle: 'Engineering Hydrology: Water Balance, Runoff, Routing & Flood Frequency | OpenSTEM Library',
    badgeCredits: 'Civil engineering core',
    courseCodes: ['CE 304', 'CIV 304', 'HYD 301'],
    searchPlaceholder: 'Search catchment boundaries, hydrologic water balance equation, storage changes, Thiessen polygons, isohyetal maps, design storm hyetographs, rainfall intensity-duration-frequency (IDF) curves, evapotranspiration, Penman-Monteith, Green-Ampt infiltration, NRCS curve number method, Rational method, unit hydrograph theory, S-curve derivation, Muskingum channel routing, reservoir storage routing, flood frequency analysis, Gumbel extreme value distribution, Log-Pearson Type III, baseflow recession, urban stormwater detention basins, Nash-Sutcliffe efficiency…',
    probSecTitle: 'Step-by-Step Engineering Hydrology Solutions',
    description: 'Comprehensive university textbook covering catchment water accounting, precipitation spatial interpolation and IDF design curves, soil infiltration mechanics, rainfall-runoff transformation, unit hydrograph convolution, reservoir and Muskingum flood routing, statistical extreme value frequency analysis, urban drainage detention, and hydrologic simulation model evaluation with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university engineering hydrology courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating annual catchment water balances, Thiessen weighted basin rainfall, synthetic IDF curves, storm depth accumulation, reference ET estimation, Green-Ampt cumulative infiltration, NRCS curve-number event excess, Rational method peaks, triangular unit hydrographs, linear reservoir routing, Muskingum routing coefficients, reservoir storage balances, Gumbel annual-maximum flood quantiles, baseflow recession, and urban detention sizing. Numerical checks and an editorial review support this edition.',
    keywords: ['Hydrology', 'Water Balance', 'IDF Curves', 'Infiltration', 'Unit Hydrograph', 'Muskingum Routing', 'Flood Frequency', 'Gumbel Distribution'],
    refPath: 'publishing/drafts/civil-engineering-hydrology/references.json'
  },
  {
    slug: 'water-resources-engineering',
    title: 'Water Resources Engineering',
    subtitle: 'Basin Assessment, Allocation Rules, Storage Reservoirs, Irrigation, Groundwater & IWRM',
    seoTitle: 'Water Resources Engineering: Basin Accounting, Reservoirs & Irrigation | OpenSTEM Library',
    badgeCredits: 'Civil engineering core',
    courseCodes: ['CE 401', 'CIV 401', 'WRE 401'],
    searchPlaceholder: 'Search basin water accounting, consumable water yields, demographic demand projections, multi-sector water allocation rules, essential and optional water shares, storage reservoir sizing, Rippl mass curve, sequent peak algorithm, firm yield, irrigation crop water requirements, reference crop ET, canal conveyance hydraulics, unlined and lined canal design, river morphology, sediment transport mechanics, Shields parameter, groundwater basin yield, Theis non-equilibrium well equation, drought reliability metrics, flood damage reduction, integrated water resources management (IWRM)…',
    probSecTitle: 'Step-by-Step Water Resources Engineering Solutions',
    description: 'Comprehensive university textbook covering river basin water accounting, multi-sector allocation priority frameworks, storage reservoir capacity and yield optimization, agricultural irrigation demand and conveyance canal design, river sedimentation and training, confined and unconfined groundwater well hydraulics, system drought resilience, and climate-adaptive IWRM with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university water resources planning and engineering courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating basin water balances, multi-year municipal demand growth, priority-based water allocation, municipal vs. agricultural trade-offs, daily reservoir volume balancing, flood pulse outlet attenuation, crop irrigation requirements, canal conveyance capacity, sediment incipient motion, well drawdown cones, and system reliability under drought. Numerical checks and an editorial review support this edition.',
    keywords: ['Water Resources Engineering', 'Basin Water Accounting', 'Reservoir Yield', 'Irrigation Engineering', 'Canal Hydraulics', 'Groundwater Hydraulics', 'IWRM'],
    refPath: 'publishing/drafts/civil-engineering-water-resources-engineering/references.json'
  },
  {
    slug: 'water-supply-and-wastewater-engineering',
    title: 'Water Supply and Wastewater Engineering',
    subtitle: 'Demographic Demands, Distribution Networks, Treatment Trains, Disinfection, Sewers & Biological Treatment',
    seoTitle: 'Water Supply & Wastewater Engineering: Distribution, Treatment & Sewerage | OpenSTEM Library',
    badgeCredits: 'Civil engineering core',
    courseCodes: ['CE 402', 'CIV 402', 'ENV 401'],
    searchPlaceholder: 'Search population forecasting, geometric and logistic growth, per capita water demands, peak hour factors, water distribution network topology, Hardy Cross loop analysis, service storage balancing tanks, booster pumping stations, water treatment unit operations, rapid mixing, coagulation mechanisms, alum dosing, flocculation paddle design, sedimentation basin surface overflow rate, granular media rapid filtration, backwash hydraulics, chlorine disinfection kinetics, CT values, trihalomethane formation, separate sanitary sewer design, minimum self-cleansing velocity, wet-weather inflow and infiltration, activated sludge kinetics, BOD removal, aeration oxygen transfer, secondary clarifier solids flux, sludge thickening and anaerobic digestion…',
    probSecTitle: 'Step-by-Step Water Supply and Wastewater Engineering Solutions',
    description: 'Comprehensive university textbook covering municipal water demand forecasting, distribution pipe network hydraulics and storage tanks, coagulation-flocculation water clarification, granular media filtration, chlorine disinfection kinetics and distribution water quality, gravity sanitary sewer design, activated sludge biological wastewater treatment kinetics, secondary clarification, and sludge solids management with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university municipal water supply and sanitary/wastewater engineering courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating demographic demand peaking, source yield shortfalls, distribution service tank deficits, pipe friction headlosses, pump-system operating points, rapid mixing intensity (G and Gt), sedimentation basin surface overflow rates, clean-bed filter headloss, chlorine disinfection contact time (CT), gravity sewer Manning full-flow capacity, wet-weather runoff peaking, biochemical oxygen demand kinetics, activated sludge F/M loading, secondary clarifier surface overflow rates, and biological solids synthesis and wasting. Numerical checks and an editorial review support this edition.',
    keywords: ['Water Supply Engineering', 'Wastewater Engineering', 'Water Distribution', 'Coagulation and Filtration', 'Disinfection CT', 'Sewer Design', 'Activated Sludge', 'Clarifier Design'],
    refPath: 'publishing/drafts/civil-engineering-water-supply-and-wastewater-engineering/references.json'
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
  console.log('Updated departments-data.js with Batch 3 courses.');
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

console.log('Batch 3 preparation complete!');
