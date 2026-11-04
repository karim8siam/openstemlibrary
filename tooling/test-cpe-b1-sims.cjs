const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

const b1_slugs = [
  'chemical-engineering-fundamentals',
  'material-and-energy-balances',
  'chemical-engineering-thermodynamics',
  'transport-phenomena',
  'fluid-flow-in-processes'
];

console.log('Testing Batch 1 Chemical Engineering Simulation Suites in JSDOM...');

let totalPassed = 0;
let totalModels = 0;

for (const slug of b1_slugs) {
  const simPath = path.join(__dirname, '..', 'src', 'subjects', 'chemical-process-engineering', slug, `${slug}-sims.js`);
  if (!fs.existsSync(simPath)) {
    console.error(`FAIL: Missing ${simPath}`);
    process.exit(1);
  }
  const code = fs.readFileSync(simPath, 'utf8');

  for (let unit = 1; unit <= 8; unit++) {
    const dom = new JSDOM(`<!DOCTYPE html><html><body data-chapter-index="${unit - 1}"><div id="sim-container" class="simulation-slot"></div></body></html>`, {
      runScripts: 'dangerously'
    });
    dom.window.eval(code);
    dom.window.SimulationEngine.initSimulation('sim-container', `sim-${unit}`);
    const container = dom.window.document.getElementById('sim-container');
    const cards = container.querySelectorAll('.cpe-sim-card');
    if (cards.length === 0) {
      console.error(`FAIL: ${slug} Unit ${unit} did not mount any simulation card!`);
      process.exit(1);
    }
    totalModels += cards.length;

    // Test slider inputs
    cards.forEach(card => {
      const sliders = card.querySelectorAll('input[type="range"]');
      sliders.forEach(slider => {
        slider.value = (parseFloat(slider.min) + parseFloat(slider.max)) / 2;
        slider.dispatchEvent(new dom.window.Event('input'));
      });
      // Check outputs for NaN
      const outputs = card.querySelectorAll('output');
      outputs.forEach(out => {
        if (out.textContent.includes('NaN')) {
          console.error(`FAIL: ${slug} Unit ${unit} output contains NaN: ${out.textContent}`);
          process.exit(1);
        }
      });
    });
    totalPassed++;
  }
  console.log(`  PASS: ${slug} (8 units, models mounted & verified)`);
}

console.log(`\nSUCCESS: All 5 Batch 1 simulation suites passed (${totalModels} models verified in JSDOM with zero errors)!`);
