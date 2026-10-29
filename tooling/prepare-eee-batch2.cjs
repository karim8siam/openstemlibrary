const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'electromagnetic-field-theory-ii',
    title: 'Electromagnetic Field Theory II',
    subtitle: 'Maxwell Equations, Time-Harmonic Fields, Plane Waves, Transmission Lines, Waveguides & Antennas',
    seoTitle: 'Electromagnetic Field Theory II: Waves, Transmission Lines, Waveguides & Antennas | OpenSTEM Library',
    badgeCredits: 'Electrical engineering core',
    courseCodes: ['EEE 301', 'ECE 301', 'PHYS 301'],
    searchPlaceholder: 'Search Maxwell equations, Faraday law, displacement current, wave equation, Helmholtz equation, Poynting vector, plane wave propagation, skin depth, Brewster angle, transmission lines, Smith chart, waveguide modes, dipole radiation…',
    probSecTitle: 'Step-by-Step Electromagnetic Field Theory II Solutions',
    description: 'Comprehensive university textbook covering Maxwell equations, Poynting theorem, uniform plane waves in lossless and lossy media, oblique reflection and refraction, transmission line transients and steady-state Smith charts, metallic rectangular waveguides, dielectric guides, and radiation from dipole antennas with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university advanced electromagnetic waves and transmission lines courses. Eight units with five solved questions per unit and 8 interactive simulations illustrating capacitor displacement currents, plane wave propagation, normal-incidence Fresnel power reflection, lossless line VSWR profiles, rectangular waveguide modal cutoffs, short dipole radiation patterns, and shield attenuation. Numerical checks and an editorial review support this edition.',
    keywords: ['Electromagnetic Field Theory II', 'Maxwell Equations', 'Plane Waves', 'Poynting Vector', 'Transmission Lines', 'Smith Chart', 'Waveguides', 'Antennas'],
    refPath: 'publishing/drafts/electrical-and-electronics-engineering-electromagnetic-field-theory-ii/references.json'
  },
  {
    slug: 'electrical-machines-i',
    title: 'Electrical Machines I',
    subtitle: 'Magnetic Circuits, Coenergy, Electromechanical Energy Conversion, Single-Phase & Three-Phase Transformers & DC Machines',
    seoTitle: 'Electrical Machines I: Magnetic Circuits, Transformers & DC Machines | OpenSTEM Library',
    badgeCredits: 'Electrical engineering core',
    courseCodes: ['EEE 302', 'ECE 302', 'EE 302'],
    searchPlaceholder: 'Search magnetomotive force, magnetic reluctance, B-H curves, magnetic hysteresis, coenergy force, torque production, single-phase transformers, equivalent circuits, regulation and efficiency, OC and SC tests, autotransformers, DC machine construction, armature reaction, DC motor characteristics, speed control…',
    probSecTitle: 'Step-by-Step Electrical Machines I Solutions',
    description: 'Comprehensive university textbook covering magnetic circuits, electromechanical energy conversion, magnetic coenergy, single-phase and three-phase transformers, equivalent circuit parameter determination, autotransformers, DC machines, armature reaction, motor speed-torque dynamics, starting and speed control, and generator characteristics with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university introductory electrical machinery courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating magnetic air-gap reluctance, core flux linkage, electromechanical coenergy force, transformer regulation, efficiency curves, open/short circuit parameter extraction, DC motor speed-torque lines, and generator terminal buildup. Numerical checks and an editorial review support this edition.',
    keywords: ['Electrical Machines', 'Magnetic Circuits', 'Transformers', 'DC Machines', 'Electromechanical Conversion', 'Coenergy', 'Armature Reaction', 'Speed Control'],
    refPath: 'publishing/drafts/electrical-and-electronics-engineering-electrical-machines-i/references.json'
  },
  {
    slug: 'electrical-machines-ii',
    title: 'Electrical Machines II',
    subtitle: 'Polyphase Induction Motors, Synchronous Alternators, Synchronous Motors, Permanent Magnet & Reluctance Machines',
    seoTitle: 'Electrical Machines II: Induction Motors, Synchronous Machines & PM Drives | OpenSTEM Library',
    badgeCredits: 'Electrical engineering core',
    courseCodes: ['EEE 303', 'ECE 303', 'EE 303'],
    searchPlaceholder: 'Search rotating magnetic field, synchronous speed, polyphase induction motor slip, torque-speed characteristics, blocked-rotor tests, synchronous alternators, cylindrical rotor phasor diagram, power-angle relation, salient-pole d-q theory, capability curves, synchronous motor V-curves, PMSM, BLDC drives, VFD scalar V/f modulation…',
    probSecTitle: 'Step-by-Step Electrical Machines II Solutions',
    description: 'Comprehensive university textbook covering rotating magnetic fields, polyphase induction motors, equivalent circuits, torque-slip analysis, starting and speed control, synchronous generators, cylindrical and salient-pole d-q models, parallel grid operation, synchronous motors, permanent magnet synchronous machines (PMSM), BLDC drives, and variable frequency control with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university advanced AC machinery and electric drives courses. Eight units with five solved questions per unit and 8 interactive simulations illustrating three-phase stator MMF distribution, induction motor torque-speed characteristics, equivalent circuit slip variations, synchronous generator power-angle curves, alternator V-curves, salient-pole d-q phasors, PMSM vector trajectories, and VFD scalar V/f modulation. Numerical checks and an editorial review support this edition.',
    keywords: ['Electrical Machines II', 'Induction Motors', 'Synchronous Generators', 'Synchronous Motors', 'PMSM', 'BLDC', 'VFD', 'D-Q Model'],
    refPath: 'publishing/drafts/electrical-and-electronics-engineering-electrical-machines-ii/references.json'
  },
  {
    slug: 'power-systems-i',
    title: 'Power Systems I',
    subtitle: 'Generation, Transmission Line Modeling, Per-Unit Systems, Admittance Bus, Gauss-Seidel & Newton-Raphson Power Flow',
    seoTitle: 'Power Systems I: Generation, Transmission Lines & Power Flow Analysis | OpenSTEM Library',
    badgeCredits: 'Electrical engineering core',
    courseCodes: ['EEE 304', 'ECE 304', 'EE 304'],
    searchPlaceholder: 'Search grid architecture, load duration curves, transmission line resistance, GMD GMR bundle conductors, short medium and long line models, ABCD parameters, Ferranti effect, per-unit systems, Y-bus formulation, Gauss-Seidel and Newton-Raphson power flow, fast decoupled load flow, voltage control, economic dispatch with losses…',
    probSecTitle: 'Step-by-Step Power Systems I Solutions',
    description: 'Comprehensive university textbook covering electric grid architectures, load duration curves, transmission line parameters (GMD/GMR, bundling), ABCD parameters, short/medium/long line models, Ferranti effect, per-unit systems, Y-bus formulation, Gauss-Seidel and Newton-Raphson power flow algorithms, voltage control, and economic generation dispatch with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university electric power systems analysis courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating transmission line inductive reactances, capacitive charging currents, nominal-pi line ABCD voltage profiles, Ferranti voltage rise, per-unit transformer impedance conversions, Y-bus modifications, Newton-Raphson power flow mismatch convergence, and economic dispatch incremental cost equalizations. Numerical checks and an editorial review support this edition.',
    keywords: ['Power Systems', 'Transmission Lines', 'GMD GMR', 'ABCD Parameters', 'Per-Unit System', 'Y-Bus Matrix', 'Newton-Raphson', 'Power Flow', 'Economic Dispatch'],
    refPath: 'publishing/drafts/electrical-and-electronics-engineering-power-systems-i/references.json'
  },
  {
    slug: 'power-systems-ii',
    title: 'Power Systems II',
    subtitle: 'Symmetrical Components, Unsymmetrical Faults, Rotor-Angle Transient Stability, Swing Equation, HVDC & Grid Control',
    seoTitle: 'Power Systems II: Fault Analysis, Transient Stability, HVDC & Power Grid Protection | OpenSTEM Library',
    badgeCredits: 'Electrical engineering core',
    courseCodes: ['EEE 305', 'ECE 305', 'EE 305'],
    searchPlaceholder: 'Search symmetrical components, positive negative zero sequence networks, symmetrical three-phase faults, unsymmetrical faults (SLG, LL, DLG), circuit breaker ratings, rotor angle stability, swing equation, equal-area criterion, critical clearing time, AGC, secondary frequency control, distance relaying, differential protection, HVDC transmission, FACTS controllers…',
    probSecTitle: 'Step-by-Step Power Systems II Solutions',
    description: 'Comprehensive university textbook covering symmetrical components, symmetrical and unsymmetrical fault calculations (SLG, LL, DLG), rotor-angle stability, swing equation, equal-area criterion, critical clearing times, automatic generation control (AGC), protective relaying (overcurrent, distance, differential), HVDC transmission, and FACTS controllers with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university advanced power systems stability, protection, and dynamics courses. Eight units with five solved questions per unit and 8 interactive simulations illustrating sequence network interconnections, unsymmetrical fault currents, single-machine swing curves, equal-area acceleration/deceleration energy areas, critical clearing angle determination, AGC secondary frequency recovery, distance relay impedance trajectory zones, and HVDC converter power flows. Numerical checks and an editorial review support this edition.',
    keywords: ['Power Systems II', 'Symmetrical Components', 'Fault Analysis', 'Transient Stability', 'Swing Equation', 'Equal Area Criterion', 'Protective Relaying', 'HVDC', 'AGC'],
    refPath: 'publishing/drafts/electrical-and-electronics-engineering-power-systems-ii/references.json'
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
      <div class="editorial-signoff">OpenSTEM Editorial Board • Electrical & Electronics Engineering Division</div>
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
      <p>This textbook synthesizes canonical university curricula and established electrical engineering references:</p>
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

  const bookDataJs = fs.readFileSync(path.join(groupedRoot, 'electrical-and-electronics-engineering', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
  w.eval(bookDataJs);
  const appJs = fs.readFileSync(path.join(root, 'app.js'), 'utf8').split('\nif (document.readyState === "loading")')[0];
  w.eval(appJs);
  w.startApp();

  d.getElementById('unit-title').textContent = w.COURSE_DATA.units[0].title;
  d.getElementById('unit-desc').textContent = w.COURSE_DATA.units[0].leadSummary || '';
  d.querySelectorAll('.mobile-chapters-button,.chapter-menu-close,.chapter-menu-backdrop').forEach(el => el.remove());
  d.querySelector('.sidebar').removeAttribute('id');

  const targetDir = path.join(groupedRoot, 'electrical-and-electronics-engineering', cfg.slug);
  const landingFile = path.join(targetDir, `${cfg.slug}.html`);
  fs.writeFileSync(landingFile, dom.serialize().replace(/^[ \t]+$/gm, ''), 'utf8');
  console.log(`Saved ${landingFile}`);
}

// Update departments-data.js
console.log('Updating departments-data.js...');
const deptDataPath = path.join(root, 'departments-data.js');
let deptCode = fs.readFileSync(deptDataPath, 'utf8');

const ctx = { window: {} };
vm.createContext(ctx);
vm.runInContext(deptCode, ctx);
const catalog = ctx.window.LIBRARY_CATALOG;
const eeeDept = catalog.departments.find(d => d.id === 'electrical-and-electronics-engineering');

if (eeeDept) {
  for (const cfg of bookConfigs) {
    if (!eeeDept.courses.some(c => c.id === cfg.slug)) {
      const dataJs = fs.readFileSync(path.join(groupedRoot, 'electrical-and-electronics-engineering', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
      const bCtx = { window: {} };
      vm.createContext(bCtx);
      vm.runInContext(dataJs, bCtx);
      const units = bCtx.window.COURSE_DATA.units.map(u => u.title);

      eeeDept.courses.push({
        id: cfg.slug,
        title: cfg.title,
        subtitle: cfg.subtitle,
        status: "AVAILABLE",
        url: `${cfg.slug}.html`,
        badge: "Free Interactive Textbook",
        description: cfg.description,
        topics: units
      });
      console.log(`Added ${cfg.slug} to departments-data.js`);
    }
  }
  fs.writeFileSync(deptDataPath, 'window.LIBRARY_CATALOG = ' + JSON.stringify(catalog, null, 2) + ';\n', 'utf8');
  console.log('Saved departments-data.js');
}

// Update publishing/book-queue.json
console.log('Updating publishing/book-queue.json...');
const bqPath = path.join(root, 'publishing', 'book-queue.json');
const bq = JSON.parse(fs.readFileSync(bqPath, 'utf8'));

let eeeQueue = bq.departments.find(d => d.id === 'electrical-electronics-engineering' || d.id === 'electrical-and-electronics-engineering');
if (eeeQueue) {
  const now = new Date().toISOString();
  for (const cfg of bookConfigs) {
    let qb = eeeQueue.books.find(b => b.id === `electrical-and-electronics-engineering-${cfg.slug}` || b.id === `electrical-electronics-engineering-${cfg.slug}` || b.id === cfg.slug);
    if (!qb) {
      qb = eeeQueue.books.find(b => b.title.toLowerCase() === cfg.title.toLowerCase());
    }
    if (qb) {
      qb.id = `electrical-and-electronics-engineering-${cfg.slug}`;
      qb.title = cfg.title;
      qb.status = 'published';
      qb.content_file = `${cfg.slug}-data.js`;
      qb.url = `${cfg.slug}.html`;
      qb.qa_report = `publishing/qa/electrical-and-electronics-engineering-${cfg.slug}.json`;
      qb.published_at = now;
      console.log(`Marked published: ${cfg.slug}`);
    } else {
      console.log(`Adding book ${cfg.slug} to queue...`);
      eeeQueue.books.push({
        id: `electrical-and-electronics-engineering-${cfg.slug}`,
        title: cfg.title,
        sequence: eeeQueue.books.length + 1,
        level_year: null,
        curriculum_status: "research_required",
        curriculum_course_codes: cfg.courseCodes,
        status: 'published',
        minimum_words: 25000,
        unit_range: [8, 8],
        content_file: `${cfg.slug}-data.js`,
        url: `${cfg.slug}.html`,
        qa_report: `publishing/qa/electrical-and-electronics-engineering-${cfg.slug}.json`,
        published_at: now
      });
    }
  }
  fs.writeFileSync(bqPath, JSON.stringify(bq, null, 2), 'utf8');
  console.log('Saved publishing/book-queue.json');
}

console.log('Batch 2 preparation complete!');
