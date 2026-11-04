const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'chemical-reaction-engineering-i',
    title: 'Chemical Reaction Engineering I',
    subtitle: 'Reaction Kinetics, Rate Laws, Ideal Reactor Design, Multiple Reactions, Thermal Stability & Residence Time Distributions',
    seoTitle: 'Chemical Reaction Engineering I: Kinetics, Ideal Reactors & Thermal Runaway | OpenSTEM Library',
    badgeCredits: 'Chemical engineering core',
    courseCodes: ['CHE 306', 'CPE 306', 'CRE 306'],
    searchPlaceholder: 'Search reaction kinetics, Arrhenius temperature dependence, activation energy, differential and integral rate data analysis, batch reactor design, continuous stirred tank reactor CSTR, plug flow reactor PFR, space time and space velocity, reactor sizing and comparison, parallel and series multiple reactions, instantaneous and overall yield, selectivity optimization, non-isothermal energy balances, adiabatic temperature rise, thermal runaway and Semenov extinction, residence time distribution RTD, E(t) and F(t) curves, segregated flow model…',
    probSecTitle: 'Step-by-Step Chemical Reaction Engineering I Solutions',
    description: 'Comprehensive university textbook covering elementary reaction kinetics, Arrhenius rate laws, batch, CSTR and PFR reactor sizing, yield and selectivity in complex multiple reaction networks, non-isothermal energy balances and thermal stability, and residence time distributions with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university chemical reaction engineering courses. Eight units with five solved questions per unit and eight interactive simulations illustrating Arrhenius rate temperature sensitivity, integral method linear regression, batch vs. CSTR vs. PFR conversion trajectories, parallel reaction selectivity optimization, CSTR adiabatic thermal runaway and ignition, pulse tracer residence time distribution E(t), segregated flow vs. maximum mixedness conversion bounds, and multi-reactor staging volume minimization. Numerical checks and an editorial review support this edition.',
    keywords: ['Chemical Reaction Engineering', 'Reaction Kinetics', 'CSTR Sizing', 'PFR Design', 'Arrhenius Law', 'Thermal Runaway', 'Residence Time Distribution'],
    refPath: 'publishing/drafts/chemical-process-engineering-chemical-reaction-engineering-i/references.json'
  },
  {
    slug: 'chemical-reaction-engineering-ii',
    title: 'Chemical Reaction Engineering II',
    subtitle: 'Heterogeneous Catalysis, Deactivation, Intraparticle Diffusion, Packed & Fluidized Beds & Multiphase Reactors',
    seoTitle: 'Chemical Reaction Engineering II: Catalysis, Thiele Modulus, Fixed & Fluidized Beds | OpenSTEM Library',
    badgeCredits: 'Chemical engineering core',
    courseCodes: ['CHE 402', 'CPE 402', 'CRE 402'],
    searchPlaceholder: 'Search heterogeneous catalysis, Langmuir-Hinshelwood kinetics, Eley-Rideal mechanisms, adsorption isotherms, catalyst deactivation, coking and sintering kinetics, intraparticle pore diffusion, Thiele modulus, internal effectiveness factor, Weisz-Prater observable criterion, external mass and heat transfer film resistance, packed-bed catalytic reactors, Ergun equation pressure loss, parametric sensitivity and thermal runaway in fixed beds, Kunii-Levenspiel bubbling fluidized beds, gas-solid non-catalytic shrinking core model, slurry and trickle-bed multiphase reactors…',
    probSecTitle: 'Step-by-Step Chemical Reaction Engineering II Solutions',
    description: 'Comprehensive university textbook covering heterogeneous surface catalysis, Langmuir-Hinshelwood rate formulations, catalyst deactivation dynamics, pore diffusion with Thiele modulus and effectiveness factor, packed-bed reactor design with Ergun pressure loss, bubbling fluidized beds, and shrinking core gas-solid kinetics with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university advanced heterogeneous reactor engineering courses. Eight units with five solved questions per unit and eight interactive simulations illustrating Langmuir-Hinshelwood catalytic surface coverage, catalyst coking and sintering activity decay, intraparticle radial concentration profiles and Thiele modulus, packed-bed Ergun pressure loss and voidage sensitivity, van Heerden fixed-bed multiple steady-state ignition, Kunii-Levenspiel two-phase fluidized bed bubble dynamics, fluid-solid shrinking core resistance breakdown, and tanks-in-series RTD variance dispersion scale-up. Numerical checks and an editorial review support this edition.',
    keywords: ['Heterogeneous Catalysis', 'Langmuir-Hinshelwood', 'Thiele Modulus', 'Catalyst Deactivation', 'Packed Bed Reactors', 'Fluidized Bed Reactors', 'Shrinking Core Model'],
    refPath: 'publishing/drafts/chemical-process-engineering-chemical-reaction-engineering-ii/references.json'
  },
  {
    slug: 'process-dynamics-and-control',
    title: 'Process Dynamics and Control',
    subtitle: 'First & Second-Order Dynamic Models, Transfer Functions, Feedback Stability, PID Tuning & Plantwide Control',
    seoTitle: 'Process Dynamics and Control: Transfer Functions, Stability, PID Tuning & Cascade Loops | OpenSTEM Library',
    badgeCredits: 'Chemical engineering core',
    courseCodes: ['CHE 307', 'CPE 307', 'PDC 307'],
    searchPlaceholder: 'Search dynamic conservation equations, first-order process time constants, gravity drained liquid surge tanks, second-order underdamped oscillations, damping ratio and natural frequency, percent overshoot and decay ratio, Laplace domain transfer functions, poles and zeros, Routh-Hurwitz stability criterion, root locus analysis, Bode and Nyquist frequency response, gain and phase margins, PID controller algorithms, Ziegler-Nichols and Cohen-Coon tuning rules, control valve sizing, valve authority and installed trim characteristics, feedforward-feedback disturbance rejection, discrete digital sampling and anti-aliasing, plantwide cascade and override control schemes…',
    probSecTitle: 'Step-by-Step Process Dynamics and Control Solutions',
    description: 'Comprehensive university textbook covering dynamic modeling of chemical processes from conservation laws, first and second-order time-domain responses, transfer function algebra, closed-loop feedback stability, PID controller sizing and tuning, control valve trim authority, feedforward decoupling, digital discrete control, and plantwide cascade architectures with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university process dynamics and automatic feedback control courses. Eight units with five solved questions per unit and eight interactive simulations illustrating first-order surge tank step response, second-order underdamped oscillation envelopes, closed-loop feedback stability boundaries and dead-time ultimate gain, PID controller setpoint tracking, control valve installed authority distortion, feedforward disturbance rejection cancellation, Nyquist digital sampling aliasing, and master-slave cascade reactor temperature control. Numerical checks and an editorial review support this edition.',
    keywords: ['Process Dynamics and Control', 'Feedback Control', 'Transfer Functions', 'PID Tuning', 'Control Valve Sizing', 'Root Locus', 'Cascade Control'],
    refPath: 'publishing/drafts/chemical-process-engineering-process-dynamics-and-control/references.json'
  },
  {
    slug: 'process-simulation',
    title: 'Process Simulation',
    subtitle: 'Flowsheet Architecture, Degree-of-Freedom Solvability, Equation-Oriented Modeling, Thermodynamic Packages & Recycle Convergence',
    seoTitle: 'Process Simulation: Flowsheet Solvability, Thermodynamic EOS, Unit Blocks & Tear Stream Convergence | OpenSTEM Library',
    badgeCredits: 'Chemical engineering core',
    courseCodes: ['CHE 403', 'CPE 403', 'PSIM 403'],
    searchPlaceholder: 'Search process flowsheet synthesis, degrees of freedom accounting, equation-oriented vs sequential modular architecture, thermodynamic property packages, Peng-Robinson equation of state, NRTL and UNIQUAC activity coefficient models, vapor-liquid-liquid equilibria, rigorous unit operation blocks, Rachford-Rice flash drum algorithm, stoichiometric and kinetic PFR/CSTR reactor modules, Fenske-Underwood-Gilliland shortcut and rigorous RadFrac distillation columns, recycle tear streams, direct substitution vs Wegstein secant convergence acceleration, Broyden quasi-Newton methods, pinch analysis heat integration composite curves, sensitivity analysis, Guthrie bare module capital cost estimation, 10-year Net Present Value (NPV)…',
    probSecTitle: 'Step-by-Step Process Simulation Solutions',
    description: 'Comprehensive university textbook covering chemical process flowsheet synthesis, degree-of-freedom solvability accounting, equation-of-state thermodynamic property method selection, rigorous unit operation modeling, flash separation solvers, shortcut and rigorous distillation columns, recycle tear stream convergence acceleration, plantwide pinch heat integration, and Guthrie CAPEX economic sizing with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university computer-aided process engineering and flowsheet simulation courses. Eight units with five solved questions per unit and eight interactive simulations illustrating flowsheet degree-of-freedom balance matrices, Peng-Robinson EOS non-ideal VLE curves, Rachford-Rice flash drum phase splitting, plug flow reaction conversion profiles, Fenske-Underwood-Gilliland column sizing, Wegstein recycle tear stream secant convergence acceleration, plantwide pinch energy composite curves, and Guthrie modular economic CAPEX/NPV sensitivity. Numerical checks and an editorial review support this edition.',
    keywords: ['Process Simulation', 'Flowsheet Modeling', 'Degrees of Freedom', 'Peng-Robinson EOS', 'Rachford-Rice Solver', 'Wegstein Acceleration', 'Pinch Analysis'],
    refPath: 'publishing/drafts/chemical-process-engineering-process-simulation/references.json'
  }
];

const templateHtml = fs.readFileSync(
  path.join(groupedRoot, 'chemical-process-engineering', 'chemical-engineering-fundamentals', 'chemical-engineering-fundamentals.html'),
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
    if (href && (href.includes('chemical-engineering-fundamentals') || href.includes('chemical-process-engineering'))) {
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
      <div class="editorial-signoff">OpenSTEM Editorial Board • Chemical & Process Engineering Division</div>
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
      <p>This textbook synthesizes canonical university curricula and established chemical engineering references:</p>
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
  const bookDataJs = fs.readFileSync(path.join(groupedRoot, 'chemical-process-engineering', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
  w.eval(bookDataJs);
  const appJs = fs.readFileSync(path.join(root, 'app.js'), 'utf8').split('\nif (document.readyState === "loading")')[0];
  w.eval(appJs);
  w.startApp();

  d.getElementById('unit-title').textContent = w.COURSE_DATA.units[0].title;
  d.getElementById('unit-desc').textContent = w.COURSE_DATA.units[0].leadSummary || '';
  d.querySelectorAll('.mobile-chapters-button,.chapter-menu-close,.chapter-menu-backdrop').forEach(el => el.remove());
  d.querySelector('.sidebar').removeAttribute('id');

  const targetDir = path.join(groupedRoot, 'chemical-process-engineering', cfg.slug);
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
const cpeDept = catalog.departments.find(d => d.id === 'chemical-process-engineering');

if (cpeDept) {
  for (const cfg of bookConfigs) {
    if (!cpeDept.courses.some(c => c.id === cfg.slug)) {
      const dataJs = fs.readFileSync(path.join(groupedRoot, 'chemical-process-engineering', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
      const bCtx = { window: {} };
      vm.createContext(bCtx);
      vm.runInContext(dataJs, bCtx);
      const units = bCtx.window.COURSE_DATA.units.map(u => u.title);

      cpeDept.courses.push({
        id: cfg.slug,
        title: cfg.title,
        subtitle: cfg.subtitle,
        status: "AVAILABLE",
        url: `${cfg.slug}.html`,
        badge: "Free Interactive Textbook",
        description: cfg.description,
        topics: units
      });
      console.log(`Added course ${cfg.slug} to chemical-process-engineering department`);
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

let cpeQueue = bq.departments.find(d => d.id === 'chemical-process-engineering');
const now = new Date().toISOString();

for (const cfg of bookConfigs) {
  let qb = cpeQueue.books.find(b => b.id === `chemical-process-engineering-${cfg.slug}` || b.id === cfg.slug);
  if (!qb) {
    qb = cpeQueue.books.find(b => b.title.toLowerCase() === cfg.title.toLowerCase());
  }
  if (qb) {
    qb.id = `chemical-process-engineering-${cfg.slug}`;
    qb.title = cfg.title;
    qb.status = 'published';
    qb.content_file = `${cfg.slug}-data.js`;
    qb.url = `${cfg.slug}.html`;
    qb.qa_report = `publishing/qa/chemical-process-engineering-${cfg.slug}.json`;
    qb.published_at = now;
    console.log(`Marked published: ${cfg.slug}`);
  } else {
    console.log(`Adding book ${cfg.slug} to queue...`);
    cpeQueue.books.push({
      id: `chemical-process-engineering-${cfg.slug}`,
      title: cfg.title,
      sequence: cpeQueue.books.length + 1,
      level_year: null,
      curriculum_status: "research_required",
      curriculum_course_codes: cfg.courseCodes,
      status: 'published',
      minimum_words: 25000,
      unit_range: [8, 9],
      content_file: `${cfg.slug}-data.js`,
      url: `${cfg.slug}.html`,
      qa_report: `publishing/qa/chemical-process-engineering-${cfg.slug}.json`,
      published_at: now
    });
  }
}
fs.writeFileSync(bqPath, JSON.stringify(bq, null, 2), 'utf8');
console.log('Saved publishing/book-queue.json');

console.log('Batch 3 preparation complete!\n');
