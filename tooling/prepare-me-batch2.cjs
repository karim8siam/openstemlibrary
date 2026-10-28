const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'heat-transfer',
    title: 'Heat Transfer',
    subtitle: 'Conduction, Convection, Radiation, Phase Change, Heat Exchangers & Numerical Thermal Modeling',
    seoTitle: 'Heat Transfer: Conduction, Convection, Radiation & Exchangers | OpenSTEM Library',
    badgeCredits: 'Thermal engineering core',
    courseCodes: ['ME 301', 'CHE 301', 'NE 301'],
    searchPlaceholder: 'Search Fourier conduction law, thermal conductivity, radial conduction, transient lumped capacitance, boundary layers, forced/free convection, nucleate boiling, blackbody radiation, view factors, LMTD/NTU heat exchangers…',
    probSecTitle: 'Step-by-Step Heat Transfer Solutions',
    description: 'Comprehensive university textbook covering steady and transient conduction, thermal boundary layers, forced and free convection correlations, phase-change boiling and condensation, radiation enclosure analysis, and heat exchanger design with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university heat transfer courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating slab conduction, composite walls, lumped cooling, thermal boundary layers, boiling regimes, radiation view factors, and heat exchanger effectiveness. Numerical checks and an editorial review support this edition.',
    keywords: ['Heat Transfer', 'Conduction', 'Convection', 'Radiation', 'Heat Exchangers', 'Fourier Law', 'Nusselt Number', 'Lumped Capacitance'],
    refPath: 'publishing/drafts/mechanical-engineering-heat-transfer/references.json'
  },
  {
    slug: 'theory-of-machines-and-mechanisms',
    title: 'Theory of Machines and Mechanisms',
    subtitle: 'Kinematic Pairs, Mobility, Four-Bar Linkages, Velocity/Acceleration Polygons, Cams, Gears & Balancing',
    seoTitle: 'Theory of Machines & Mechanisms: Kinematics, Dynamics & Balancing | OpenSTEM Library',
    badgeCredits: 'Mechanism design core',
    courseCodes: ['ME 302', 'ROB 302', 'MAE 302'],
    searchPlaceholder: 'Search kinematic pairs, degrees of freedom, Grübler criterion, velocity/acceleration polygons, Coriolis acceleration, four-bar linkages, cam profiles, epicyclic gears, rotor balancing…',
    probSecTitle: 'Step-by-Step Mechanisms Solutions',
    description: 'Comprehensive university textbook covering planar kinematics, linkage loop closure, velocity and acceleration vector polygons, cam-follower synthesis, spur and epicyclic gear trains, mechanism force analysis, and rotor dynamic balancing with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university theory of machines and mechanism design courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating linkage mobility, angular velocity, tangential acceleration, slider-crank displacement, gear speed ratios, cam lift curves, and rotor balancing. Numerical checks and an editorial review support this edition.',
    keywords: ['Theory of Machines', 'Kinematics', 'Dynamics of Machinery', 'Four-Bar Linkages', 'Cam Synthesis', 'Epicyclic Gears', 'Rotor Balancing', 'Grübler Criterion'],
    refPath: 'publishing/drafts/mechanical-engineering-theory-of-machines-and-mechanisms/references.json'
  },
  {
    slug: 'machine-design',
    title: 'Machine Design',
    subtitle: 'Stress Concentrations, Fatigue Failure, Shafts, Bearings, Gears, Fasteners, Springs, Clutches & Brakes',
    seoTitle: 'Machine Design: Fatigue, Shafts, Bearings, Gears & Fasteners | OpenSTEM Library',
    badgeCredits: 'Mechanical design core',
    courseCodes: ['ME 303', 'MSE 303', 'ENGR 303'],
    searchPlaceholder: 'Search static failure theories, stress concentration, variable loading and fatigue criteria (Goodman, Gerber), shaft design for combined loading, rolling bearing L10 life, AGMA gear bending, bolted joints, compression springs…',
    probSecTitle: 'Step-by-Step Machine Design Solutions',
    description: 'Comprehensive university textbook covering stress concentrations, static and fatigue failure criteria, shaft design for combined loads, rolling-contact bearing life, AGMA gear fatigue, threaded fastener preload, helical spring mechanics, and friction clutches with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university machine design and mechanical component design courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating shaft shear, twist, fatigue Goodman lines, bolt stiffness, bearing L10 ratings, gear bending strength, and spring deflection. Numerical checks and an editorial review support this edition.',
    keywords: ['Machine Design', 'Fatigue Failure', 'Goodman Line', 'Shaft Design', 'Rolling Bearings', 'AGMA Gears', 'Bolted Joints', 'Spring Mechanics'],
    refPath: 'publishing/drafts/mechanical-engineering-machine-design/references.json'
  },
  {
    slug: 'mechanical-vibrations',
    title: 'Mechanical Vibrations',
    subtitle: 'Harmonic Motion, SDOF Damped Oscillations, Resonance, Transmissibility, MDOF Systems & Modal Analysis',
    seoTitle: 'Mechanical Vibrations: Resonance, Damping, MDOF & Modal Analysis | OpenSTEM Library',
    badgeCredits: 'Structural dynamics core',
    courseCodes: ['ME 304', 'AER 304', 'CE 304'],
    searchPlaceholder: 'Search SDOF undamped/damped free vibrations, viscous damping ratio, logarithmic decrement, harmonic excitation, resonance, dynamic magnification factor, base excitation, isolation transmissibility, tuned mass dampers, MDOF modal analysis…',
    probSecTitle: 'Step-by-Step Mechanical Vibrations Solutions',
    description: 'Comprehensive university textbook covering free and forced SDOF vibrations, viscous damping, logarithmic decrement, harmonic resonance, base excitation and isolation transmissibility, tuned vibration absorbers, and MDOF modal analysis with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university mechanical vibrations and structural dynamics courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating SDOF natural frequencies, logarithmic decrements, magnification factors, base isolation transmissibility, tuned mass dampers, and two-DOF modal shapes. Numerical checks and an editorial review support this edition.',
    keywords: ['Mechanical Vibrations', 'Harmonic Motion', 'Resonance', 'Damping Ratio', 'Transmissibility', 'Vibration Isolation', 'Modal Analysis', 'Tuned Mass Absorber'],
    refPath: 'publishing/drafts/mechanical-engineering-mechanical-vibrations/references.json'
  },
  {
    slug: 'internal-combustion-engines',
    title: 'Internal Combustion Engines',
    subtitle: 'Four-Stroke & Two-Stroke Cycles, Thermochemistry, Combustion Flame Propagation, Turbocharging & Emissions',
    seoTitle: 'Internal Combustion Engines: Cycles, Combustion, Turbocharging & Emissions | OpenSTEM Library',
    badgeCredits: 'Power engineering core',
    courseCodes: ['ME 305', 'AUT 305', 'ENR 305'],
    searchPlaceholder: 'Search four-stroke/two-stroke cycles, mean effective pressure (bmep, imep), air-standard Otto and Diesel cycles, volumetric efficiency, turbocharging, combustion stoichiometry, knock rating, direct injection, emissions formation (NOx, soot), EGR…',
    probSecTitle: 'Step-by-Step Engine Engineering Solutions',
    description: 'Comprehensive university textbook covering two- and four-stroke thermodynamics, mean effective pressure, Otto/Diesel/Dual cycles, volumetric efficiency, turbocharging, turbulent combustion kinetics, knock limits, emissions mechanisms, and aftertreatment with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university internal combustion engines and automotive powertrain courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating engine displacement, brake power, air-standard Otto efficiencies, trapped charge mass, turbocharger boost, and emissions trade-offs. Numerical checks and an editorial review support this edition.',
    keywords: ['Internal Combustion Engines', 'Otto Cycle', 'Diesel Cycle', 'Mean Effective Pressure', 'Turbocharging', 'Combustion Kinetics', 'Emissions EGR', 'Powertrain'],
    refPath: 'publishing/drafts/mechanical-engineering-internal-combustion-engines/references.json'
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

  // Populate unit 1 content using COURSE_DATA
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
  // Clean any residual references to template
  htmlOutput = htmlOutput.replace(/fundamentals-of-materials-science/g, cfg.slug);
  fs.writeFileSync(landingFile, htmlOutput, 'utf8');
  console.log(`Saved ${landingFile}`);
}

// Register courses in departments-data.js
console.log('Updating departments-data.js for Batch 2...');
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
  console.log('Saved departments-data.js with Batch 2 courses');
}

// Update publishing/book-queue.json
console.log('Updating publishing/book-queue.json for Batch 2...');
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

console.log('Batch 2 preparation complete!');
