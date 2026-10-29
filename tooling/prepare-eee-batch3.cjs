const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'control-systems-i',
    title: 'Control Systems I',
    subtitle: 'Transfer Functions, Block Diagrams, Time-Domain Transient Response, Stability & Frequency-Response Design',
    seoTitle: 'Control Systems I: Modeling, Time-Domain Response, Stability & Root Locus | OpenSTEM Library',
    badgeCredits: 'Electrical engineering core',
    courseCodes: ['EEE 306', 'ECE 306', 'EE 306'],
    searchPlaceholder: 'Search open-loop transfer functions, block diagram algebra, signal flow graphs, Mason gain formula, first- and second-order step response, damping ratio, natural frequency, settling time, Routh-Hurwitz stability criterion, steady-state error constants, root locus sketching rules, Bode diagrams, gain and phase margins, Nyquist stability criterion, lead-lag compensator design…',
    probSecTitle: 'Step-by-Step Control Systems I Solutions',
    description: 'Comprehensive university textbook covering mathematical modeling of physical systems, transfer functions, block diagrams, time-domain transient and steady-state responses, Routh-Hurwitz stability, root locus techniques, frequency-response analysis (Bode and Nyquist), and lead-lag controller synthesis with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university classical feedback and control systems courses. Eight units with five solved questions per unit and 8 interactive simulations illustrating first-order transients, second-order overshoot, sensitivity functions, root locus migration, Bode delay margins, PI anti-windup, mass-spring-damper dynamics, and sampled feedback stability. Numerical checks and an editorial review support this edition.',
    keywords: ['Control Systems', 'Transfer Functions', 'Root Locus', 'Bode Plots', 'Nyquist Stability', 'PID Controller', 'Steady-State Error'],
    refPath: 'publishing/drafts/electrical-and-electronics-engineering-control-systems-i/references.json'
  },
  {
    slug: 'control-systems-ii',
    title: 'Control Systems II',
    subtitle: 'State-Space Methods, Controllability, Observability, Full-State Feedback, Observers, LQR & Digital Control',
    seoTitle: 'Control Systems II: State-Space Analysis, Observers, Optimal Control & LQR | OpenSTEM Library',
    badgeCredits: 'Electrical engineering core',
    courseCodes: ['EEE 307', 'ECE 307', 'EE 307'],
    searchPlaceholder: 'Search state-space models, state transition matrix, Cayley-Hamilton theorem, controllability and observability Gramians, PBH test, Kalman canonical decomposition, Ackermann pole placement, full-order and reduced-order observers, separation principle, Linear Quadratic Regulator (LQR), algebraic Riccati equation, discrete state equations, deadbeat control, robust control, Lyapunov stability…',
    probSecTitle: 'Step-by-Step Control Systems II Solutions',
    description: 'Comprehensive university textbook covering continuous and discrete state-space representations, state transition matrices, controllability, observability, full-state feedback pole placement, observer synthesis, LQR optimal control, discrete-time state systems, and Lyapunov stability with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university modern and state-space control engineering courses. Eight units with five solved questions per unit and 8 interactive simulations illustrating sensitivity bounds, continuous-time LQR decay, Kalman state updates, one-step MPC horizon bounds, Lyapunov phase trajectories, recursive least squares parameter estimation, multivariable cross-coupling, and sampled-delay stability. Numerical checks and an editorial review support this edition.',
    keywords: ['Control Systems II', 'State Space', 'Controllability', 'Observability', 'Pole Placement', 'LQR', 'Kalman Filter', 'Discrete Control'],
    refPath: 'publishing/drafts/electrical-and-electronics-engineering-control-systems-ii/references.json'
  },
  {
    slug: 'communication-systems-i',
    title: 'Communication Systems I',
    subtitle: 'Analog Modulation (AM, FM, PM), Noise Analysis, Pulse Modulation (PAM, PCM) & Baseband Transmission',
    seoTitle: 'Communication Systems I: Analog Modulation, Noise Analysis & Pulse Systems | OpenSTEM Library',
    badgeCredits: 'Electrical engineering core',
    courseCodes: ['EEE 308', 'ECE 308', 'EE 308'],
    searchPlaceholder: 'Search spectral analysis, Fourier transforms, baseband channels, amplitude modulation, DSB-FC, DSB-SC, SSB, VSB, frequency modulation, Carson rule, phase modulation, superheterodyne receivers, noise figure, SNR in analog systems, sampling theorem, aliasing, PAM, uniform and non-uniform quantization, A-law, mu-law, PCM, ISI, Nyquist pulse shaping…',
    probSecTitle: 'Step-by-Step Communication Systems I Solutions',
    description: 'Comprehensive university textbook covering continuous-wave analog modulation (AM, FM, PM), superheterodyne receiver architectures, thermal noise analysis, SNR derivations, sampling theorems, pulse code modulation (PCM), and baseband transmission with Nyquist pulse shaping with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university introductory communications and signal transmission courses. Eight units with five solved questions per unit and 8 interactive simulations illustrating link budgets, sampling and aliasing folds, AM modulation depths, FM Carson bandwidths, uniform quantization steps, coherent BPSK BER curves, Shannon channel capacity bounds, and noisy QPSK constellation scatters. Numerical checks and an editorial review support this edition.',
    keywords: ['Communication Systems', 'Amplitude Modulation', 'Frequency Modulation', 'Noise Figure', 'Sampling Theorem', 'PCM', 'Inter-Symbol Interference'],
    refPath: 'publishing/drafts/electrical-and-electronics-engineering-communication-systems-i/references.json'
  },
  {
    slug: 'communication-systems-ii',
    title: 'Communication Systems II',
    subtitle: 'Digital Passband Modulation (BPSK, QPSK, M-QAM), Information Theory, Entropy & Error-Control Coding',
    seoTitle: 'Communication Systems II: Digital Modulation, Information Theory & Error Coding | OpenSTEM Library',
    badgeCredits: 'Electrical engineering core',
    courseCodes: ['EEE 309', 'ECE 309', 'EE 309'],
    searchPlaceholder: 'Search Gram-Schmidt orthogonalization, signal space, AWGN channels, matched filter receivers, BASK, BFSK, BPSK, QPSK, M-PSK, M-QAM, constellation error probability, non-coherent DPSK, entropy, Shannon-Fano and Huffman coding, mutual information, channel capacity theorem, linear block codes, generator matrices, syndrome decoding, convolutional codes, Viterbi decoding…',
    probSecTitle: 'Step-by-Step Communication Systems II Solutions',
    description: 'Comprehensive university textbook covering geometric signal representation, matched filtering, coherent and non-coherent digital passband modulation (BPSK, QPSK, M-QAM), source coding and entropy, Shannon channel capacity, linear block codes, and convolutional error-control codes with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university digital communications and information theory courses. Eight units with five solved questions per unit and 8 interactive simulations illustrating Hamming (7,4) single-bit correction syndromes, BPSK log-likelihood and BER, adaptive LMS tracking, OFDM carrier frequency offset leakage, Rayleigh fading outages, DSSS correlation peaks, fiber attenuation budgets, and M/M/1 queuing latencies. Numerical checks and an editorial review support this edition.',
    keywords: ['Communication Systems II', 'Digital Modulation', 'QPSK', 'QAM', 'Information Theory', 'Channel Capacity', 'Viterbi Algorithm', 'Error-Correcting Codes'],
    refPath: 'publishing/drafts/electrical-and-electronics-engineering-communication-systems-ii/references.json'
  },
  {
    slug: 'digital-signal-processing',
    title: 'Digital Signal Processing',
    subtitle: 'Discrete-Time Systems, Z-Transforms, DFT, FFT Algorithms, FIR/IIR Filter Synthesis & Multirate DSP',
    seoTitle: 'Digital Signal Processing: Discrete Systems, DFT, FFT, FIR & IIR Filter Design | OpenSTEM Library',
    badgeCredits: 'Electrical engineering core',
    courseCodes: ['EEE 310', 'ECE 310', 'EE 310'],
    searchPlaceholder: 'Search discrete-time signals, linear constant-coefficient difference equations, Z-transform region of convergence, DTFT, Discrete Fourier Transform (DFT), radix-2 decimation-in-time and decimation-in-frequency FFT algorithms, Direct Form I/II filter structures, FIR linear phase filter design, windowing methods, Parks-McClellan Remez exchange, IIR filter synthesis, bilinear transformation, impulse invariance, finite wordlength effects, decimation and interpolation…',
    probSecTitle: 'Step-by-Step Digital Signal Processing Solutions',
    description: 'Comprehensive university textbook covering discrete-time signals and systems, Z-transforms, DTFT, DFT, FFT decimation algorithms, digital filter realizations, FIR filter design (windowing, Remez), IIR filter synthesis (bilinear transform), coefficient quantization, and multirate DSP with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university digital signal processing and discrete systems courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating aliasing fold, ADC quantization noise, FIR step responses, DFT leakage, Hann window sidebands, FFT computational scaling, moving-average magnitude, windowed-sinc lowpass, linear phase delays, one-pole IIR steps, resonance poles, fixed-point rounding, noise filtering, LMS convergence, decimation aliasing, and Welch spectral estimation. Numerical checks and an editorial review support this edition.',
    keywords: ['Digital Signal Processing', 'Z-Transform', 'DFT', 'FFT', 'FIR Filters', 'IIR Filters', 'Bilinear Transform', 'Multirate DSP'],
    refPath: 'publishing/drafts/electrical-and-electronics-engineering-digital-signal-processing/references.json'
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
  const ogTitle = d.querySelector('meta[property="og:title"]');
  if (ogTitle) ogTitle.content = cfg.seoTitle;
  const ogDesc = d.querySelector('meta[property="og:description"]');
  if (ogDesc) ogDesc.content = cfg.description;
  const ogUrl = d.querySelector('meta[property="og:url"]');
  if (ogUrl) ogUrl.content = 'https://openstemlibrary.com/' + cfg.slug;
  const twTitle = d.querySelector('meta[name="twitter:title"]');
  if (twTitle) twTitle.content = cfg.seoTitle;
  const twDesc = d.querySelector('meta[name="twitter:description"]');
  if (twDesc) twDesc.content = cfg.description;

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

console.log('Batch 3 preparation complete!');
