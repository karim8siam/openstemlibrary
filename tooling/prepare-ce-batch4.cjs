const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'environmental-engineering',
    title: 'Environmental Engineering',
    subtitle: 'Mass Balances, Water Quality, Drinking Water Treatment, Wastewater, Air Dispersion & Waste Systems',
    seoTitle: 'Environmental Engineering: Water Quality, Treatment & Air Dispersion | OpenSTEM Library',
    badgeCredits: 'Civil & environmental core',
    courseCodes: ['CE 305', 'ENV 301', 'CIV 305'],
    searchPlaceholder: 'Search mass balances, conservative and non-conservative pollutants, CSTR reactors, plug flow reactors, Streeter-Phelps oxygen sag curve, critical deficit, deoxygenation rate, reaeration coefficient, coagulation and flocculation, alum dosage, sedimentation overflow rate, granular media filtration, Darcy loss, chlorine disinfection kinetics, CT calculations, activated sludge F/M ratio, Monod kinetics, mean cell residence time, Gaussian air plume dispersion, electrostatic precipitators, cyclone separators, landfill methane production, environmental risk assessment, life-cycle assessment (LCA)…',
    probSecTitle: 'Step-by-Step Environmental Engineering Solutions',
    description: 'Comprehensive university textbook covering environmental mass balances, stream water quality and Streeter-Phelps oxygen sag, drinking water treatment separation processes, biological wastewater kinetics, atmospheric Gaussian plume dispersion, municipal solid waste and landfill engineering, environmental risk assessment, and life-cycle sustainability with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university environmental engineering courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating complete-mix reactors, pollutant exponential decay, river confluence mixing, Streeter-Phelps dissolved oxygen sag curves, clarifier settling capture, clean-bed filter head loss, disinfectant decay, activated-sludge F/M loading, Monod growth kinetics, nutrient mass balances, Gaussian atmospheric plume dispersion, particulate cyclone capture, landfill gas generation, chemical exposure intake, and carbon footprints. Numerical checks and an editorial review support this edition.',
    keywords: ['Environmental Engineering', 'Mass Balance', 'Streeter-Phelps', 'Water Treatment', 'Activated Sludge', 'Air Dispersion', 'Solid Waste', 'Risk Assessment'],
    refPath: 'publishing/drafts/civil-engineering-environmental-engineering/references.json'
  },
  {
    slug: 'transportation-engineering',
    title: 'Transportation Engineering',
    subtitle: 'Traffic Flow Theory, Roadway Performance, Geometric Alignment, Signalized Intersections & Transit Planning',
    seoTitle: 'Transportation Engineering: Traffic Flow, Geometric Design & Signals | OpenSTEM Library',
    badgeCredits: 'Civil engineering core',
    courseCodes: ['CE 306', 'CIV 306', 'TRN 301'],
    searchPlaceholder: 'Search Greenshields traffic stream model, speed-flow-density relationships, critical density, capacity, bottleneck queueing, shockwave propagation, peak-hour factor (PHF), Poisson arrivals, stopping sight distance (SSD), decision sight distance, horizontal curve minimum radius, superelevation, spiral transition curves, crest and sag vertical curves, signalized intersection capacity, Webster optimal cycle length, pedestrian clearance time, four-step travel demand modeling, transit route headway, Highway Safety Manual (HSM) crash modification factors, intelligent transportation systems (ITS)…',
    probSecTitle: 'Step-by-Step Transportation Engineering Solutions',
    description: 'Comprehensive university textbook covering microscopic and macroscopic traffic stream theory, highway capacity and level of service, roadway geometric alignment and sight distances, signal timing optimization and queueing dynamics, travel demand forecasting, public transit scheduling, traffic safety analytics, and intelligent transportation systems with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university transportation engineering courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating Greenshields speed-flow-density envelopes, bottleneck queue accumulation, peak-hour factors, stopping sight distance sensitivity, minimum horizontal curve radii, vertical crest profile elevations, signalized capacity and v/c ratios, Webster optimal cycle lengths, deterministic cycle queueing, equivalent axle load factors (ESALs), Westergaard slab rigidity, and rational roadway drainage. Numerical checks and an editorial review support this edition.',
    keywords: ['Transportation Engineering', 'Traffic Flow Theory', 'Greenshields', 'Geometric Design', 'Sight Distance', 'Signal Timing', 'Webster Formula', 'Highway Capacity'],
    refPath: 'publishing/drafts/civil-engineering-transportation-engineering/references.json'
  },
  {
    slug: 'highway-and-pavement-engineering',
    title: 'Highway and Pavement Engineering',
    subtitle: 'Highway Route Planning, Subgrade Soils, Bituminous Binders, Flexible & Rigid Pavement Structural Design',
    seoTitle: 'Highway & Pavement Engineering: Flexible & Rigid Pavement Design | OpenSTEM Library',
    badgeCredits: 'Civil engineering core',
    courseCodes: ['CE 403', 'CIV 403', 'HWY 401'],
    searchPlaceholder: 'Search highway reconnaissance, earthwork mass-haul diagrams, cut and fill volumes, prismoidal formula, subgrade resilient modulus (Mr), California Bearing Ratio (CBR), aggregate gradation, Fuller-Thompson maximum density curves, asphalt binder Superpave performance grading (PG), Marshall and Superpave volumetric mix design, AASHTO 1993 flexible pavement structural number (SN), layer coefficients, drainage coefficients, Boussinesq stress distribution, Burmister layered elastic theory, Westergaard rigid pavement corner/edge/interior stress, doweled joint load transfer, concrete slab curling and warping, pavement distress indices (PCI), life-cycle cost analysis (LCCA)…',
    probSecTitle: 'Step-by-Step Highway and Pavement Engineering Solutions',
    description: 'Comprehensive university textbook covering highway alignment economics, earthwork balancing, bituminous binder and aggregate characterization, Superpave asphalt mix volumetrics, AASHTO flexible pavement structural number design, Westergaard rigid concrete pavement mechanics, joint load transfer, subsurface pavement drainage, and life-cycle pavement management systems with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university highway and pavement engineering courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating earthwork volume end-area calculations, vertical parabolic grade profiles, stopping sight distances, minimum curve radii, aggregate gradation power curves, asphalt binder temperature susceptibility, Boussinesq subgrade vertical stresses, asphalt fatigue endurance, subgrade rutting accumulation, Westergaard slab flexural rigidity, doweled contraction joint expansion, and Proctor compaction density curves. Numerical checks and an editorial review support this edition.',
    keywords: ['Highway Engineering', 'Pavement Design', 'Superpave', 'AASHTO Flexible Pavement', 'Westergaard Rigid Pavement', 'Earthwork Mass Haul', 'Subgrade Resilient Modulus'],
    refPath: 'publishing/drafts/civil-engineering-highway-and-pavement-engineering/references.json'
  },
  {
    slug: 'surveying-and-geomatics',
    title: 'Surveying and Geomatics',
    subtitle: 'Geodetic Reference Frames, Distance & Angle Measurement, Leveling, Traversing, GNSS & Photogrammetry',
    seoTitle: 'Surveying & Geomatics: Leveling, Traversing, GNSS & Photogrammetry | OpenSTEM Library',
    badgeCredits: 'Civil engineering core',
    courseCodes: ['CE 205', 'CIV 205', 'SUR 201'],
    searchPlaceholder: 'Search reference ellipsoids, geoid undulation, orthometric heights, systematic and random errors, standard error propagation, EDM atmospheric and scale corrections, horizontal and vertical circle angle reading, optical and electronic leveling, two-peg collimation test, earth curvature and atmospheric refraction, closed loop traverse, latitude and departure computations, compass (Bowditch) rule balance, coordinate geometry (COGO), traverse area calculation, horizontal circular curves, deflection angles, GNSS satellite positioning, carrier phase differential GPS, GDOP, HDOP, aerial photogrammetry, ground sample distance (GSD), stereoscopic parallax, LiDAR point clouds, GIS spatial overlays…',
    probSecTitle: 'Step-by-Step Surveying and Geomatics Solutions',
    description: 'Comprehensive university textbook covering geodetic and plane surveying foundations, optical distance and angular measurement precision, leveling and refraction corrections, traverse closure balancing, coordinate transformations, GNSS positioning mechanics, aerial and UAV photogrammetry, LiDAR scanning, and route alignment geometry with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university surveying, geomatics, and geospatial engineering courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating steel tape thermal corrections, slope distance reduction, polygon angle misclosure distribution, differential leveling rise calculations, combined curvature and refraction corrections, traverse coordinate balancing, weighted mean position uncertainties, coordinate polygon land areas, GNSS dilution of precision (DOP) positioning bounds, geoid separation height reductions, photogrammetric ground sample distances, stereoscopic flight parallax depths, and LiDAR point pulse densities. Numerical checks and an editorial review support this edition.',
    keywords: ['Surveying', 'Geomatics', 'Differential Leveling', 'Traverse Adjustment', 'Bowditch Rule', 'GNSS Positioning', 'Photogrammetry', 'LiDAR'],
    refPath: 'publishing/drafts/civil-engineering-surveying-and-geomatics/references.json'
  },
  {
    slug: 'engineering-geology-for-civil-engineers',
    title: 'Engineering Geology for Civil Engineers',
    subtitle: 'Rock Minerals, Weathering, Structural Mapping, Seepage, Rock Mass Classification, Slopes & Geohazards',
    seoTitle: 'Engineering Geology: Rock Mechanics, Discontinuities & Slopes | OpenSTEM Library',
    badgeCredits: 'Civil engineering core',
    courseCodes: ['CE 206', 'CIV 206', 'GEO 201'],
    searchPlaceholder: 'Search geologic time scale, mineral cleavage and hardness, igneous, sedimentary, and metamorphic rock types, weathering indices, Rock Quality Designation (RQD), discontinuity dip and dip direction, stereographic projections, strike and dip of strata, fold geometry, fault classification, slickensides, hydrogeology, Darcy law in fractured rock, groundwater flow net, water-rock chemical interaction, borehole core drilling, geophysical seismic refraction, electrical resistivity imaging, planar and wedge rock slope failure, Markland kinematic test, rock bolt reinforcement, Hoek-Brown failure criterion, Rock Mass Rating (RMR), Q-system, tunnel support, earthquake liquefaction, fault rupture hazards, karst subsidence…',
    probSecTitle: 'Step-by-Step Engineering Geology Solutions',
    description: 'Comprehensive university textbook covering applied mineralogy and petrology, geological structures and stereonet discontinuity mapping, groundwater seepage and rock weathering mechanics, geophysical subsurface exploration, rock mass classification (RQD, RMR, Q), rock slope kinematic stability, underground excavation support, and earthquake/landslide geohazard assessment with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university engineering geology and applied geotechnics courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating stratigraphic age-depth rates, apparent dip geometry, rock weathering compressive strength decay, joint spacing frequency distributions, hydraulic conductivity porosity relations, piezometric seepage head drops, Terzaghi effective stress in submerged strata, core sample recovery metrics, seismic refraction interface depths, rock-water bulk electrical resistivity, planar slope safety factors, rock blast vibration attenuation, tunnel Kirsch stress concentrations, and earthquake ground acceleration amplification. Numerical checks and an editorial review support this edition.',
    keywords: ['Engineering Geology', 'Rock Mechanics', 'Rock Mass Rating', 'RMR', 'RQD', 'Discontinuities', 'Slope Stability', 'Tunneling'],
    refPath: 'publishing/drafts/civil-engineering-engineering-geology-for-civil-engineers/references.json'
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
  console.log('Updated departments-data.js with Batch 4 courses.');
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

console.log('Batch 4 preparation complete!');
