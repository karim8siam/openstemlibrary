const fs = require('fs');
const path = require('path');
const vm = require('vm');
const { JSDOM } = require('jsdom');

const root = path.resolve(__dirname, '..');
const ceDir = path.join(root, 'src', 'subjects', 'civil-engineering');

const books = [
  'civil-engineering-statics',
  'strength-of-materials',
  'structural-analysis-i',
  'structural-analysis-ii',
  'concrete-technology',
  'reinforced-concrete-design',
  'steel-structure-design',
  'soil-mechanics',
  'foundation-engineering',
  'fluid-mechanics-and-hydraulics',
  'hydrology',
  'water-resources-engineering',
  'water-supply-and-wastewater-engineering',
  'environmental-engineering',
  'transportation-engineering',
  'highway-and-pavement-engineering',
  'surveying-and-geomatics',
  'engineering-geology-for-civil-engineers'
];

console.log('================================================================');
console.log('STARTING EXHAUSTIVE QUALITY RECHECK FOR CIVIL ENGINEERING');
console.log(`Checking ${books.length} textbooks across all units, problems, and simulations...`);
console.log('================================================================\n');

function proseCount(text) {
  let t = String(text || '');
  t = t.replace(/\$\$[\s\S]*?\$\$/g, ' ');
  t = t.replace(/\$[^$\n]+\$/g, ' ');
  t = t.replace(/```[\s\S]*?```/g, ' ');
  t = t.replace(/`[^`\n]+`/g, ' ');
  t = t.replace(/<[^>]+>/g, ' ');
  t = t.replace(/^#+\s.*$/gm, ' ');
  t = t.replace(/^[-*+]\s+/gm, ' ');
  t = t.replace(/^\d+\.\s+/gm, ' ');
  t = t.replace(/\[([^\]]+)\]\([^)]+\)/g, '$1');
  const words = t.match(/\b[A-Za-z]+(?:['’\-][A-Za-z]+)*\b/g);
  return words ? words.length : 0;
}

let allPassed = true;
const summary = [];

books.forEach((slug, bIdx) => {
  console.log(`[${bIdx + 1}/${books.length}] Checking textbook: ${slug}`);
  const bDir = path.join(ceDir, slug);
  const dataFile = path.join(bDir, `${slug}-data.js`);
  const simsFile = path.join(bDir, `${slug}-sims.js`);
  const landingFile = path.join(bDir, `${slug}.html`);
  const cssFile = path.join(bDir, `${slug}.css`);

  const bookReport = {
    slug,
    totalWords: 0,
    unitsCount: 0,
    problemsCount: 0,
    simsMounted: 0,
    errors: []
  };

  // 1. Check file existence
  [dataFile, simsFile, landingFile, cssFile].forEach(f => {
    if (!fs.existsSync(f)) {
      bookReport.errors.push(`Missing required file: ${path.basename(f)}`);
    }
  });

  if (bookReport.errors.length > 0) {
    console.error(`  FAIL: File existence error in ${slug}:`, bookReport.errors);
    allPassed = false;
    summary.push(bookReport);
    return;
  }

  // 2. Syntax check on data and sims files
  try {
    const dataSrc = fs.readFileSync(dataFile, 'utf8');
    new vm.Script(dataSrc);
  } catch (err) {
    bookReport.errors.push(`Syntax error in data file: ${err.message}`);
  }

  try {
    const simsSrc = fs.readFileSync(simsFile, 'utf8');
    new vm.Script(simsSrc);
  } catch (err) {
    bookReport.errors.push(`Syntax error in sims file: ${err.message}`);
  }

  // 3. Inspect COURSE_DATA
  let courseData = null;
  try {
    const ctx = { window: {} };
    vm.createContext(ctx);
    vm.runInContext(fs.readFileSync(dataFile, 'utf8'), ctx);
    courseData = ctx.window.COURSE_DATA;
    if (!courseData || !courseData.units || !Array.isArray(courseData.units)) {
      bookReport.errors.push('COURSE_DATA.units is missing or not an array');
    }
  } catch (err) {
    bookReport.errors.push(`Failed to load COURSE_DATA: ${err.message}`);
  }

  if (courseData && courseData.units) {
    bookReport.unitsCount = courseData.units.length;
    let bWords = 0;
    let bProbs = 0;

    courseData.units.forEach((u, uIdx) => {
      let uWords = 0;
      if (u.sections && Array.isArray(u.sections)) {
        u.sections.forEach(s => {
          uWords += proseCount(s.content);
        });
      }
      bWords += uWords;

      const problems = u.problems || u.workedProblems || [];
      if (problems.length < 5) {
        bookReport.errors.push(`Unit ${uIdx + 1} has ${problems.length} worked problems (expected >= 5)`);
      } else {
        bProbs += problems.length;
        problems.forEach((p, pIdx) => {
          if (!p.question || p.question.trim().length < 15) {
            bookReport.errors.push(`Unit ${uIdx + 1} Problem ${pIdx + 1} has empty or short question`);
          }
          if (!p.solution || p.solution.trim().length < 30) {
            bookReport.errors.push(`Unit ${uIdx + 1} Problem ${pIdx + 1} has empty or short solution`);
          }
          if (!p.finalAnswer || p.finalAnswer.trim().length < 5) {
            bookReport.errors.push(`Unit ${uIdx + 1} Problem ${pIdx + 1} has empty finalAnswer`);
          }
        });
      }
    });

    bookReport.totalWords = bWords;
    bookReport.problemsCount = bProbs;

    if (bWords < 25000) {
      bookReport.errors.push(`Total prose words ${bWords} is below 25,000 threshold`);
    }
  }

  // 4. Test Simulation Mounting & Interactivity across every unit in JSDOM
  const simsCode = fs.readFileSync(simsFile, 'utf8');
  const targetUnits = bookReport.unitsCount || 8;
  let totalCardsMounted = 0;

  for (let u = 1; u <= targetUnits; u++) {
    const dom = new JSDOM(
      `<!DOCTYPE html><html><body data-chapter-index="${u - 1}"><div id="sim-container" class="simulation-slot"></div></body></html>`,
      { runScripts: 'dangerously' }
    );

    try {
      dom.window.eval(simsCode);
      if (!dom.window.SimulationEngine || typeof dom.window.SimulationEngine.initSimulation !== 'function') {
        throw new Error('SimulationEngine.initSimulation function missing');
      }

      dom.window.SimulationEngine.initSimulation('sim-container', `unit-${u}`);
      const cards = dom.window.document.querySelectorAll('.ce-sim-card');
      if (cards.length === 0) {
        throw new Error(`No simulation cards rendered for unit ${u}`);
      }
      totalCardsMounted += cards.length;

      // Test each slider and check for NaN or thrown exceptions
      cards.forEach((card, cIdx) => {
        const inputs = card.querySelectorAll('input[type="range"]');
        inputs.forEach(inp => {
          const originalVal = Number(inp.value);
          const step = Number(inp.step || 1);
          inp.value = String(originalVal + step);
          inp.dispatchEvent(new dom.window.Event('input'));
        });

        // Check if value readout contains NaN or undefined
        const readouts = card.querySelectorAll('.val-readout, .value, [id^="metric"]');
        readouts.forEach(r => {
          if (r.textContent && (r.textContent.includes('NaN') || r.textContent.includes('undefined'))) {
            bookReport.errors.push(`Unit ${u} card ${cIdx + 1} produced NaN or undefined: "${r.textContent.trim()}"`);
          }
        });
      });
    } catch (err) {
      bookReport.errors.push(`Simulation crash on unit ${u}: ${err.message}`);
    }
  }
  bookReport.simsMounted = totalCardsMounted;

  // 5. Check Landing Page and Canonical URL
  try {
    const landingHtml = fs.readFileSync(landingFile, 'utf8');
    const canonMatch = landingHtml.match(/<link\s+rel="canonical"\s+href="([^"]+)"/i);
    if (!canonMatch) {
      bookReport.errors.push('Landing page missing canonical link tag');
    } else if (canonMatch[1].endsWith('.html')) {
      bookReport.errors.push(`Landing page canonical URL ends in .html: ${canonMatch[1]}`);
    }

    if (!landingHtml.includes(`${slug}-data.js`)) {
      bookReport.errors.push(`Landing page does not reference ${slug}-data.js`);
    }
    if (!landingHtml.includes(`${slug}-sims.js`)) {
      bookReport.errors.push(`Landing page does not reference ${slug}-sims.js`);
    }

    // Check chapters generated
    for (let u = 2; u <= targetUnits; u++) {
      const chapFile = path.join(bDir, `${slug}-chapter-${u}.html`);
      if (!fs.existsSync(chapFile)) {
        bookReport.errors.push(`Missing chapter page: ${path.basename(chapFile)}`);
      } else {
        const chapHtml = fs.readFileSync(chapFile, 'utf8');
        const chapCanon = chapHtml.match(/<link\s+rel="canonical"\s+href="([^"]+)"/i);
        if (chapCanon && chapCanon[1].endsWith('.html')) {
          bookReport.errors.push(`Chapter ${u} canonical ends in .html: ${chapCanon[1]}`);
        }
      }
    }
  } catch (err) {
    bookReport.errors.push(`Landing/chapter check error: ${err.message}`);
  }

  if (bookReport.errors.length === 0) {
    console.log(`  PASS: ${bookReport.totalWords.toLocaleString()} words | ${bookReport.unitsCount} units | ${bookReport.problemsCount} problems | ${bookReport.simsMounted} sim instances mounted`);
  } else {
    console.error(`  FAIL with ${bookReport.errors.length} errors:`);
    bookReport.errors.forEach(e => console.error(`    - ${e}`));
    allPassed = false;
  }

  summary.push(bookReport);
});

console.log('\n================================================================');
console.log('RECHECK SUMMARY RESULTS');
console.log('================================================================');
console.log(`Total Textbooks Checked: ${summary.length}`);
const passCount = summary.filter(s => s.errors.length === 0).length;
console.log(`Passed: ${passCount}/${summary.length}`);
const totalWordsAll = summary.reduce((acc, s) => acc + s.totalWords, 0);
const totalProbsAll = summary.reduce((acc, s) => acc + s.problemsCount, 0);
console.log(`Total Substantive Words: ${totalWordsAll.toLocaleString()}`);
console.log(`Total Worked Problems: ${totalProbsAll}`);

if (allPassed) {
  console.log('\nSUCCESS: All Civil Engineering textbooks passed all quality, simulation, and prose checks!');
  process.exit(0);
} else {
  console.error('\nFAILURE: Some issues were discovered during recheck.');
  process.exit(1);
}
