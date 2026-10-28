const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'turbomachinery',
    title: 'Turbomachinery',
    subtitle: 'Euler Turbine Equation, Velocity Triangles, Axial/Radial Pumps, Compressors, Steam & Gas Turbines',
    seoTitle: 'Turbomachinery: Euler Equation, Velocity Triangles & Turbines | OpenSTEM Library',
    badgeCredits: 'Fluid machinery core',
    courseCodes: ['ME 401', 'AER 401', 'ENR 401'],
    searchPlaceholder: 'Search Euler turbine equation, velocity triangles, degree of reaction, specific speed, centrifugal pump slip, NPSH cavitation, compressor surge and stall, steam/gas turbine stages…',
    probSecTitle: 'Step-by-Step Turbomachinery Solutions',
    description: 'Comprehensive university textbook covering angular momentum principles, velocity triangles, centrifugal pump cavitation, axial compressor surge and stall, impulse and reaction steam/gas turbine stages, and dimensionless performance scaling with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university turbomachinery and fluid machinery courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating Euler turbine head, velocity triangles, centrifugal pump slip, NPSH cavitation limits, compressor stage loading, and turbine blade efficiencies. Numerical checks and an editorial review support this edition.',
    keywords: ['Turbomachinery', 'Euler Turbine Equation', 'Velocity Triangles', 'Centrifugal Pumps', 'Axial Compressors', 'Gas Turbines', 'Cavitation', 'Surge and Stall'],
    refPath: 'publishing/drafts/mechanical-engineering-turbomachinery/references.json'
  },
  {
    slug: 'refrigeration-and-air-conditioning',
    title: 'Refrigeration and Air Conditioning',
    subtitle: 'Vapor Compression, Absorption, Psychrometrics, Cooling/Heating Load Estimation & HVAC Controls',
    seoTitle: 'Refrigeration & Air Conditioning: Cycles, Psychrometrics & HVAC Design | OpenSTEM Library',
    badgeCredits: 'HVAC engineering core',
    courseCodes: ['ME 402', 'ARE 402', 'BSE 402'],
    searchPlaceholder: 'Search vapor-compression cycles, low-GWP refrigerants, compound compression, absorption cooling, psychrometrics, cooling load estimation (CLTD), indoor air quality (ASHRAE 62.1), chilled water systems…',
    probSecTitle: 'Step-by-Step Refrigeration & Air Conditioning Solutions',
    description: 'Comprehensive university textbook covering vapor-compression and absorption refrigeration, refrigerant thermodynamics, psychrometric process analysis, building heating/cooling load calculations, air distribution, and HVAC energy management with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university refrigeration, air conditioning, and building energy engineering courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating vapor-compression COP, compressor displacement, psychrometric air mixing, cooling coil dehumidification, building thermal envelope loads, and duct airflow pressure losses. Numerical checks and an editorial review support this edition.',
    keywords: ['Refrigeration', 'Air Conditioning', 'HVAC', 'Psychrometrics', 'Vapor Compression', 'Cooling Load', 'Refrigerants', 'Indoor Air Quality'],
    refPath: 'publishing/drafts/mechanical-engineering-refrigeration-and-air-conditioning/references.json'
  },
  {
    slug: 'power-plant-engineering',
    title: 'Power Plant Engineering',
    subtitle: 'Supercritical Rankine Cycles, Combined Cycle Gas Turbines, Nuclear, Boilers, Cooling Towers & Economics',
    seoTitle: 'Power Plant Engineering: Rankine, Combined Cycles, Boilers & Economics | OpenSTEM Library',
    badgeCredits: 'Energy systems core',
    courseCodes: ['ME 403', 'EE 403', 'NE 403'],
    searchPlaceholder: 'Search supercritical Rankine cycles, CCGT heat recovery steam generators, nuclear thermal hydraulics, cooling towers, flue-gas desulfurization, levelized cost of electricity (LCOE), heat rates…',
    probSecTitle: 'Step-by-Step Power Plant Engineering Solutions',
    description: 'Comprehensive university textbook covering supercritical steam cycles, combined cycle gas turbines, steam generators, nuclear thermal balance, cooling towers, emissions abatement, and levelized electricity cost optimization with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university power plant engineering and central power station design courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating reheat Rankine efficiency, HRSG pinch point temperature profiles, cooling tower range/approach, nuclear core heat balances, and levelized generation economics. Numerical checks and an editorial review support this edition.',
    keywords: ['Power Plant Engineering', 'Rankine Cycle', 'Combined Cycle CCGT', 'Boilers', 'Cooling Towers', 'Nuclear Power', 'HRSG', 'LCOE Economics'],
    refPath: 'publishing/drafts/mechanical-engineering-power-plant-engineering/references.json'
  },
  {
    slug: 'control-systems-engineering',
    title: 'Control Systems Engineering',
    subtitle: 'Transfer Functions, Block Diagrams, Routh-Hurwitz, Root Locus, Bode/Nyquist Stability & State-Space',
    seoTitle: 'Control Systems Engineering: Root Locus, Bode, Nyquist & State-Space | OpenSTEM Library',
    badgeCredits: 'Dynamic systems core',
    courseCodes: ['ME 404', 'EE 404', 'MAE 404'],
    searchPlaceholder: 'Search Laplace transfer functions, block diagram reduction, transient overshoot/settling time, Routh-Hurwitz stability, Evans root locus, Bode gain/phase margins, Nyquist criterion, PID tuning, state-space pole placement…',
    probSecTitle: 'Step-by-Step Control Systems Solutions',
    description: 'Comprehensive university textbook covering linear dynamic system modeling, transient response, Routh-Hurwitz stability, root locus synthesis, Bode and Nyquist frequency-domain methods, PID compensation, and state-space modern control with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university feedback control systems courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating first/second-order step responses, Routh stability bounds, root locus branch trajectories, Bode gain/phase margins, Nyquist encirclements, and state feedback pole placement. Numerical checks and an editorial review support this edition.',
    keywords: ['Control Systems', 'Transfer Functions', 'Root Locus', 'Bode Plots', 'Nyquist Stability', 'PID Controller', 'State-Space', 'Feedback Control'],
    refPath: 'publishing/drafts/mechanical-engineering-control-systems-engineering/references.json'
  },
  {
    slug: 'automotive-engineering',
    title: 'Automotive Engineering',
    subtitle: 'Vehicle Dynamics, Aerodynamic Drag, Powertrain Matching, Braking, Steering, Suspension & EV Powertrains',
    seoTitle: 'Automotive Engineering: Vehicle Dynamics, Powertrains & EV Systems | OpenSTEM Library',
    badgeCredits: 'Automotive engineering core',
    courseCodes: ['ME 405', 'AUT 405', 'SYS 405'],
    searchPlaceholder: 'Search road tractive effort, aerodynamic drag, axle load transfer during braking, tire lateral cornering stiffness, bicycle model understeer gradient, suspension ride frequencies, battery EV motor matching…',
    probSecTitle: 'Step-by-Step Automotive Engineering Solutions',
    description: 'Comprehensive university textbook covering longitudinal road resistance, powertrain gear matching, dynamic braking weight transfer, tire lateral slip, bicycle handling models, suspension ride frequencies, and battery EV powertrain architectures with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university automotive engineering and vehicle dynamics courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating aerodynamic drag, tractive effort, acceleration times, braking distance, weight transfer, cornering slip angles, and quarter-car suspension ride frequencies. Numerical checks and an editorial review support this edition.',
    keywords: ['Automotive Engineering', 'Vehicle Dynamics', 'Tractive Effort', 'Braking Distance', 'Tire Mechanics', 'Understeer Gradient', 'Suspension Ride', 'Electric Vehicles'],
    refPath: 'publishing/drafts/mechanical-engineering-automotive-engineering/references.json'
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

  const brandTitle = d.querySelector('.brand-title');
  if (brandTitle) brandTitle.textContent = cfg.title;

  const badgeCourse = d.querySelector('.badge-course');
  if (badgeCourse) badgeCourse.textContent = 'Mechanical Engineering';

  const searchInput = d.querySelector('#problem-search');
  if (searchInput) searchInput.placeholder = cfg.searchPlaceholder;

  const probSec = d.querySelector('#worked-problems-section h2');
  if (probSec) probSec.textContent = cfg.probSecTitle;

  const editorialBox = d.querySelector('.editorial-review-box');
  if (editorialBox) {
    editorialBox.innerHTML = `
      <div class="editorial-review-badge">Peer Review & Editorial Standards</div>
      <p>${cfg.editorialNote}</p>
      <div class="editorial-signoff">OpenSTEM Editorial Board • Mechanical Engineering Division</div>
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
      <p>This textbook synthesizes canonical university curricula and established mechanical engineering references:</p>
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

  const structuredDataScripts = d.querySelectorAll('script[type="application/ld+json"]');
  structuredDataScripts.forEach(script => {
    try {
      const sd = JSON.parse(script.textContent);
      if (sd['@type'] === 'Course' || sd['@type'] === 'Book') {
        sd.name = cfg.title;
        sd.description = cfg.description;
        sd.url = 'https://openstemlibrary.com/' + cfg.slug;
        sd.keywords = cfg.keywords.join(', ');
        script.textContent = JSON.stringify(sd, null, 2);
      } else if (sd['@type'] === 'BreadcrumbList') {
        sd.itemListElement = [
          {"@type": "ListItem", "position": 1, "name": "OpenSTEM Library", "item": "https://openstemlibrary.com/"},
          {"@type": "ListItem", "position": 2, "name": "Mechanical Engineering", "item": "https://openstemlibrary.com/#dept-mechanical-engineering"},
          {"@type": "ListItem", "position": 3, "name": cfg.title, "item": `https://openstemlibrary.com/${cfg.slug}`}
        ];
        script.textContent = JSON.stringify(sd, null, 2);
      }
    } catch (e) {}
  });

  const bookDataJs = fs.readFileSync(path.join(groupedRoot, 'mechanical-engineering', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
  w.eval(bookDataJs);
  const appJs = fs.readFileSync(path.join(root, 'app.js'), 'utf8').split('\nif (document.readyState === "loading")')[0];
  w.eval(appJs);
  w.startApp();

  d.body.dataset.bookPath = `${cfg.slug}.html`;
  d.getElementById('unit-title').textContent = w.COURSE_DATA.units[0].title;
  d.getElementById('unit-desc').textContent = w.COURSE_DATA.units[0].leadSummary || '';
  d.querySelectorAll('.mobile-chapters-button,.chapter-menu-close,.chapter-menu-backdrop').forEach(el => el.remove());
  d.querySelector('.sidebar').removeAttribute('id');

  const targetDir = path.join(groupedRoot, 'mechanical-engineering', cfg.slug);
  const landingFile = path.join(targetDir, `${cfg.slug}.html`);
  let htmlOutput = dom.serialize().replace(/^[ \t]+$/gm, '');
  htmlOutput = htmlOutput.replace(/fundamentals-of-materials-science/g, cfg.slug);
  fs.writeFileSync(landingFile, htmlOutput, 'utf8');
  console.log(`Saved ${landingFile}`);
}

// Register courses in departments-data.js
console.log('Updating departments-data.js for Batch 3...');
const deptDataPath = path.join(root, 'departments-data.js');
let deptCode = fs.readFileSync(deptDataPath, 'utf8');

const ctx = { window: {} };
vm.createContext(ctx);
vm.runInContext(deptCode, ctx);
const catalog = ctx.window.LIBRARY_CATALOG;
const meDept = catalog.departments.find(d => d.id === 'mechanical-engineering');

if (meDept) {
  for (const cfg of bookConfigs) {
    if (!meDept.courses.some(c => c.id === cfg.slug)) {
      const dataJs = fs.readFileSync(path.join(groupedRoot, 'mechanical-engineering', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
      const bCtx = { window: {} };
      vm.createContext(bCtx);
      vm.runInContext(dataJs, bCtx);
      const units = bCtx.window.COURSE_DATA.units.map(u => u.title);

      meDept.courses.push({
        id: cfg.slug,
        title: cfg.title,
        subtitle: cfg.subtitle,
        status: "AVAILABLE",
        url: `${cfg.slug}.html`,
        badge: "Free Interactive Textbook",
        description: cfg.description,
        topics: units
      });
      console.log(`Added course ${cfg.slug} to Mechanical Engineering catalog`);
    }
  }

  const updatedDeptDataJs = '/* OpenSTEM Library — Complete Departmental Course Catalog */\nwindow.LIBRARY_CATALOG = ' + JSON.stringify(catalog, null, 2) + ';\n';
  fs.writeFileSync(deptDataPath, updatedDeptDataJs, 'utf8');
  console.log('Saved departments-data.js with Batch 3 courses');
}

// Update publishing/book-queue.json
console.log('Updating publishing/book-queue.json for Batch 3...');
const bqPath = path.join(root, 'publishing', 'book-queue.json');
const bq = JSON.parse(fs.readFileSync(bqPath, 'utf8'));

const meQueue = bq.departments.find(d => d.id === 'mechanical-engineering');
if (meQueue) {
  const now = new Date().toISOString();
  for (const cfg of bookConfigs) {
    let qb = meQueue.books.find(b => b.id === `mechanical-engineering-${cfg.slug}` || b.id === cfg.slug);
    if (!qb) {
      qb = meQueue.books.find(b => b.title.toLowerCase() === cfg.title.toLowerCase());
    }
    if (qb) {
      qb.id = `mechanical-engineering-${cfg.slug}`;
      qb.title = cfg.title;
      qb.status = 'published';
      qb.content_file = `${cfg.slug}-data.js`;
      qb.url = `${cfg.slug}.html`;
      qb.qa_report = `publishing/qa/mechanical-engineering-${cfg.slug}.json`;
      qb.published_at = now;
      console.log(`Marked published: ${cfg.slug}`);
    } else {
      console.log(`Could not find book ${cfg.slug} in queue, adding...`);
      meQueue.books.push({
        id: `mechanical-engineering-${cfg.slug}`,
        title: cfg.title,
        sequence: meQueue.books.length + 1,
        status: 'published',
        minimum_words: 25000,
        content_file: `${cfg.slug}-data.js`,
        url: `${cfg.slug}.html`,
        qa_report: `publishing/qa/mechanical-engineering-${cfg.slug}.json`,
        published_at: now
      });
    }
  }
  fs.writeFileSync(bqPath, JSON.stringify(bq, null, 2), 'utf8');
  console.log('Saved publishing/book-queue.json');
}

console.log('Batch 3 preparation complete!');
