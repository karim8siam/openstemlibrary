// Test all 4 Batch 3 simulation suites in JSDOM
const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

const BOOKS = [
  'chemical-reaction-engineering-i',
  'chemical-reaction-engineering-ii',
  'process-dynamics-and-control',
  'process-simulation'
];

let totalPasses = 0;
let totalFails = 0;

for (const slug of BOOKS) {
  const filePath = path.join(__dirname, '..', 'src', 'subjects', 'chemical-process-engineering', slug, `${slug}-sims.js`);
  if (!fs.existsSync(filePath)) {
    console.error(`FAIL: Missing ${filePath}`);
    totalFails++;
    continue;
  }
  const code = fs.readFileSync(filePath, 'utf8');

  for (let u = 1; u <= 8; u++) {
    const dom = new JSDOM(`<!DOCTYPE html><html><body data-chapter-index="${u - 1}"><div id="sim-container"></div></body></html>`, {
      runScripts: 'dangerously'
    });
    const { window } = dom;

    try {
      window.eval(code);
      if (typeof window.SimulationEngine?.initSimulation === 'function') {
        window.SimulationEngine.initSimulation('sim-container', `sim-${u}`);
      }

      const card = window.document.querySelector('.cpe-sim-card');
      if (!card) {
        console.error(`FAIL: ${slug} Unit ${u} did not render .cpe-sim-card`);
        totalFails++;
        continue;
      }

      const svg = card.querySelector('svg');
      if (!svg || !svg.innerHTML) {
        console.error(`FAIL: ${slug} Unit ${u} missing SVG plot content`);
        totalFails++;
        continue;
      }

      const text = card.textContent;
      if (text.includes('NaN') || text.includes('undefined')) {
        console.error(`FAIL: ${slug} Unit ${u} rendered NaN or undefined in card text`);
        totalFails++;
        continue;
      }

      totalPasses++;
    } catch (err) {
      console.error(`FAIL: ${slug} Unit ${u} threw exception:`, err);
      totalFails++;
    }
  }
}

console.log(`\n=== Batch 3 Simulation Test Results ===`);
console.log(`Passed: ${totalPasses} / ${BOOKS.length * 8}`);
console.log(`Failed: ${totalFails}`);

if (totalFails > 0) {
  process.exit(1);
} else {
  console.log('ALL BATCH 3 SIMULATIONS PASSED CLEANLY!\n');
}
