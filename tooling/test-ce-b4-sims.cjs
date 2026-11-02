const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

const books = [
  'environmental-engineering',
  'transportation-engineering',
  'highway-and-pavement-engineering',
  'surveying-and-geomatics',
  'engineering-geology-for-civil-engineers'
];

let totalTests = 0;
let passedTests = 0;

books.forEach(slug => {
  console.log(`\nTesting simulation suite for: ${slug}`);
  const simPath = path.join(__dirname, '..', 'src', 'subjects', 'civil-engineering', slug, `${slug}-sims.js`);
  if (!fs.existsSync(simPath)) {
    console.error(`ERROR: File does not exist: ${simPath}`);
    process.exit(1);
  }
  const code = fs.readFileSync(simPath, 'utf8');

  for (let unit = 1; unit <= 8; unit++) {
    totalTests++;
    const dom = new JSDOM(`<!DOCTYPE html><html><body><div id="sim-container" class="simulation-slot"></div></body></html>`, {
      runScripts: 'dangerously'
    });

    try {
      dom.window.eval(code);
      dom.window.SimulationEngine.initSimulation('sim-container', `unit-${unit}`);
      const cards = dom.window.document.querySelectorAll('.ce-sim-card');
      if (cards.length === 0) {
        throw new Error(`No simulation cards rendered for unit ${unit}`);
      }
      
      cards.forEach(card => {
        const inputs = card.querySelectorAll('input[type="range"]');
        if (inputs.length > 0) {
          inputs[0].value = (Number(inputs[0].value) + Number(inputs[0].step || 1)).toString();
          inputs[0].dispatchEvent(new dom.window.Event('input'));
        }
      });

      passedTests++;
      process.stdout.write(`  Unit ${unit}: OK (${cards.length} cards) `);
    } catch (err) {
      console.error(`\nFAILED unit ${unit} for ${slug}:`, err.message);
      process.exit(1);
    }
  }
  console.log();
});

console.log(`\nAll Batch 4 Simulation Tests Passed: ${passedTests}/${totalTests}`);
