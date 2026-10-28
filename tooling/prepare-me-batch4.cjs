const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'finite-element-analysis-and-computational-mechanics',
    title: 'Finite Element Analysis and Computational Mechanics',
    subtitle: 'Variational Methods, 1D/2D Elements, Isoparametric Formulations, Plate Bending, Dynamics & Non-Linear FEA',
    seoTitle: 'Finite Element Analysis & Computational Mechanics | OpenSTEM Library',
    badgeCredits: 'Computational mechanics core',
    courseCodes: ['ME 411', 'CE 411', 'AER 411'],
    searchPlaceholder: 'Search principle of virtual work, Rayleigh-Ritz method, 1D bar and beam elements, CST and Q4 plane elements, isoparametric mapping, Gauss quadrature, patch tests, shear locking, modal extraction, Newton-Raphson nonlinear tangent stiffness…',
    probSecTitle: 'Step-by-Step Computational Mechanics Solutions',
    description: 'Comprehensive university textbook covering variational formulations, 1D bar and beam elements, 2D plane elasticity, isoparametric mapping, Gauss quadrature, dynamic modal extraction, and nonlinear iterations with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university finite element analysis (FEA) and computational mechanics courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating bar stiffness, beam deflection matrices, CST strain interpolation, Gauss quadrature coordinates, modal eigenvalue extraction, and Newton-Raphson convergence. Numerical checks and an editorial review support this edition.',
    keywords: ['Finite Element Analysis', 'Computational Mechanics', 'FEA', 'Stiffness Matrix', 'Isoparametric Elements', 'Gauss Quadrature', 'Modal Analysis', 'Nonlinear FEA'],
    refPath: 'publishing/drafts/mechanical-engineering-finite-element-analysis-and-computational-mechanics/references.json'
  },
  {
    slug: 'mechatronics-engineering',
    title: 'Mechatronics Engineering',
    subtitle: 'Sensor Transducers, Actuators, Power Electronics, Microcontrollers, PLC Interfaces & Motion Control',
    seoTitle: 'Mechatronics Engineering: Sensors, Actuators, Embedded Control & Drives | OpenSTEM Library',
    badgeCredits: 'Mechatronics core',
    courseCodes: ['ME 412', 'EE 412', 'ROB 412'],
    searchPlaceholder: 'Search strain gauges, Wheatstone bridge, thermocouples, op-amp signal conditioning, ADC quantization, DC and stepper motor drives, H-bridge PWM, microcontroller GPIO interrupts, SPI/I2C/CAN bus, digital PID motion control…',
    probSecTitle: 'Step-by-Step Mechatronics Solutions',
    description: 'Comprehensive university textbook covering sensor transduction, operational amplifier signal conditioning, DC/stepper motor electromechanics, H-bridge PWM drives, microcontroller embedded architecture, industrial communication buses, and digital servo control with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university mechatronics and electromechanical systems courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating sorting gate timing, encoder pulse resolution, motor torque-speed curves, ADC quantization, H-bridge PWM duty cycles, and PID servo tracking. Numerical checks and an editorial review support this edition.',
    keywords: ['Mechatronics', 'Sensors', 'Actuators', 'DC Motors', 'PWM H-Bridge', 'Signal Conditioning', 'Microcontrollers', 'Motion Control'],
    refPath: 'publishing/drafts/mechanical-engineering-mechatronics-engineering/references.json'
  },
  {
    slug: 'robotics-and-automation',
    title: 'Robotics and Automation',
    subtitle: 'Spatial Transformations, Forward/Inverse Kinematics, Jacobians, Dynamics, Path Planning & Industrial Cells',
    seoTitle: 'Robotics & Automation: Kinematics, Jacobians, Dynamics & Planning | OpenSTEM Library',
    badgeCredits: 'Robotics core',
    courseCodes: ['ME 413', 'CS 413', 'ROB 413'],
    searchPlaceholder: 'Search SE(3) transformation matrices, Denavit-Hartenberg parameters, forward/inverse kinematics, manipulator Jacobians, singularities, Lagrangian multi-body dynamics, polynomial trajectory generation, industrial workcell automation…',
    probSecTitle: 'Step-by-Step Robotics Solutions',
    description: 'Comprehensive university textbook covering spatial rotation matrices, Denavit-Hartenberg conventions, forward and inverse manipulator kinematics, Jacobian singularities, Lagrangian multi-body dynamics, polynomial trajectory generation, and industrial cell automation with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university robotics and industrial automation courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating planar arm reach, DH frame transformations, Jacobian singularity boundaries, joint torque balances, cubic trajectory splines, and workcell cycle times. Numerical checks and an editorial review support this edition.',
    keywords: ['Robotics', 'Automation', 'Denavit-Hartenberg', 'Forward Kinematics', 'Inverse Kinematics', 'Jacobians', 'Robot Dynamics', 'Trajectory Generation'],
    refPath: 'publishing/drafts/mechanical-engineering-robotics-and-automation/references.json'
  },
  {
    slug: 'engineering-reliability-and-maintenance',
    title: 'Engineering Reliability and Maintenance',
    subtitle: 'Failure Distributions, MTTF, Weibull Analysis, Markov Systems, FMEA, RCM & Condition Monitoring',
    seoTitle: 'Engineering Reliability & Maintenance: Weibull, Markov, FMEA & RCM | OpenSTEM Library',
    badgeCredits: 'Reliability engineering core',
    courseCodes: ['ME 414', 'IE 414', 'SYS 414'],
    searchPlaceholder: 'Search hazard rate, MTTF, MTBF, exponential and Weibull distributions, bathtub curve, redundant system reliability, Markov state transition modeling, FMEA risk priority, Fault Tree cut sets, reliability centered maintenance (RCM)…',
    probSecTitle: 'Step-by-Step Reliability & Maintenance Solutions',
    description: 'Comprehensive university textbook covering hazard functions, Weibull failure parameter estimation, series/parallel and standby system dependability, Markov availability modeling, FMEA risk ranking, Fault Tree minimal cut sets, and predictive maintenance with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university reliability engineering, asset management, and maintenance courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating constant failure rates, Weibull shape/scale plots, redundant system reliability, Markov steady-state availability, FMEA risk priority, and optimal maintenance replacement intervals. Numerical checks and an editorial review support this edition.',
    keywords: ['Engineering Reliability', 'Maintenance', 'Weibull Analysis', 'Hazard Rate', 'MTBF', 'Markov Modeling', 'FMEA', 'Reliability Centered Maintenance'],
    refPath: 'publishing/drafts/mechanical-engineering-engineering-reliability-and-maintenance/references.json'
  },
  {
    slug: 'mechanical-systems-design-and-optimization',
    title: 'Mechanical Systems Design and Optimization',
    subtitle: 'System Architecture, Multidisciplinary Design Optimization (MDO), Gradient Methods, Pareto Fronts & Robust Design',
    seoTitle: 'Mechanical Systems Design & Optimization: MDO, Pareto & Robust Design | OpenSTEM Library',
    badgeCredits: 'Systems optimization core',
    courseCodes: ['ME 415', 'SYS 415', 'EM 415'],
    searchPlaceholder: 'Search system decomposition, KKT necessary optimality conditions, gradient descent and BFGS algorithms, sequential quadratic programming (SQP), multidisciplinary design optimization (MDO), multi-objective Pareto frontiers, Taguchi robust design…',
    probSecTitle: 'Step-by-Step Optimization Solutions',
    description: 'Comprehensive university textbook covering system decomposition, KKT optimality conditions, gradient and Newton optimization, sequential quadratic programming, multidisciplinary co-design, multi-objective Pareto frontiers, and Taguchi robust parameter optimization with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university mechanical systems design and engineering optimization courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating objective contours, constraint boundaries, gradient descent steps, SQP convergence, Pareto trade-off curves, and robust variance minimization. Numerical checks and an editorial review support this edition.',
    keywords: ['Mechanical Systems Design', 'Engineering Optimization', 'MDO', 'KKT Conditions', 'Pareto Frontier', 'Sequential Quadratic Programming', 'Robust Design', 'Genetic Algorithms'],
    refPath: 'publishing/drafts/mechanical-engineering-mechanical-systems-design-and-optimization/references.json'
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
console.log('Updating departments-data.js for Batch 4...');
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
  console.log('Saved departments-data.js with Batch 4 courses');
}

// Update publishing/book-queue.json
console.log('Updating publishing/book-queue.json for Batch 4...');
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

console.log('Batch 4 preparation complete!');
