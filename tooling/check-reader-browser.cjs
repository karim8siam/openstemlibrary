// Smoke-test the real reader in Chromium before production release.
// Run: python3 -m http.server 8765 & node tooling/check-reader-browser.cjs
const assert = require('node:assert/strict');
const fs = require('node:fs');
const { chromium } = require('playwright');

const base = process.env.OPENSTEM_TEST_URL || 'http://127.0.0.1:8765';
const pages = ['reader.html', 'calculus-1.html', 'statistical-estimation.html'];
const output = 'browser-test-artifacts';
fs.mkdirSync(output, { recursive: true });
const results = [];

async function verifyPage(browser, file, viewport, suffix) {
  const context = await browser.newContext({ viewport, reducedMotion: 'reduce' });
  const page = await context.newPage();
  const pageErrors = [];
  page.on('pageerror', e => pageErrors.push(e.message));
  const response = await page.goto(base + '/' + file, {waitUntil: 'domcontentloaded', timeout: 30000});
  assert.equal(response.status(), 200, file + ' returned ' + response.status());
  const button = page.locator('.reader-theme-toggle');
  await button.waitFor({ timeout: 20000 });
  assert.equal(await button.getAttribute('aria-pressed'), 'true', 'Calm paper theme should be default');
  assert.equal(await page.locator('body').evaluate(el => getComputedStyle(el).userSelect), 'text', 'Readers must be able to select and copy their study text');
  assert.ok(await page.locator('.textbook-section-card').count() > 0, 'Book must contain prerendered learning sections');
  const browserAccess = await page.evaluate(() => {
    const copyContext = new MouseEvent('contextmenu', {bubbles: true, cancelable: true});
    const printKey = new KeyboardEvent('keydown', {key: 'p', ctrlKey: true, bubbles: true, cancelable: true});
    return { contextMenuAllowed: document.dispatchEvent(copyContext),
      printShortcutAllowed: document.dispatchEvent(printKey) };
  });
  assert.ok(browserAccess.contextMenuAllowed, 'Right-click should not be globally blocked');
  assert.ok(browserAccess.printShortcutAllowed, 'Print shortcut should not be globally blocked');
  assert.equal(await button.textContent(), 'Night view', 'Paper theme must allow switching to Night view');
  const paper = await page.evaluate(() => {
    const section = document.querySelector('.textbook-section-card');
    return {
      body: getComputedStyle(document.body).backgroundColor,
      section: getComputedStyle(section).backgroundColor,
      select: getComputedStyle(section).userSelect,
      content: getComputedStyle(document.querySelector('.sec-content')).color,
      overflow: document.documentElement.scrollWidth - window.innerWidth
    };
  });
  assert.equal(paper.body, 'rgb(244, 242, 236)', 'Expected calm paper background on ' + file);
  assert.equal(paper.section, 'rgb(255, 254, 250)', 'Expected high-contrast reading section on ' + file);
  assert.ok(paper.overflow <= 8, 'Unexpected mobile horizontal overflow: ' + file + ' ' + paper.overflow);
  const increase = page.getByRole('button', {name: 'Increase reading text size'});
  const decrease = page.getByRole('button', {name: 'Decrease reading text size'});
  assert.equal(await increase.count(), 1, 'Reader font increase button missing');
  assert.equal(await decrease.isDisabled(), true, 'Default minimum font scale expected');
  const beforeFont = await page.locator('.sec-content').first().evaluate(el => getComputedStyle(el).fontSize);
  await increase.click();
  const afterFont = await page.locator('.sec-content').first().evaluate(el => getComputedStyle(el).fontSize);
  assert.ok(parseFloat(afterFont)>parseFloat(beforeFont), 'Font resizing did not increase reading text size');
  await page.reload({waitUntil:'domcontentloaded'});
  await button.waitFor({timeout:20000});
  const persistedFont=await page.locator('.sec-content').first().evaluate(el => getComputedStyle(el).fontSize);
  assert.equal(persistedFont,afterFont,'Reader size must persist across page reload');
  await decrease.click();

  await page.screenshot({ path: output + '/' + file.replace('.html','') + '-' + suffix + '-paper.png' });
  await page.reload({waitUntil: 'domcontentloaded'});
  await button.waitFor({timeout: 20000});
  assert.equal(await button.getAttribute('aria-pressed'), 'true', 'Paper theme preference should persist on reload');
  await button.click();
  assert.equal(await button.getAttribute('aria-pressed'), 'false', 'Night view should remain available');
  results.push({page: file, viewport: suffix, paper, runtimeWarnings: pageErrors.slice(0, 3)});
  await context.close();
}

(async () => {
  const browser = await chromium.launch({headless: true});
  try {
    for (const file of pages) {
      await verifyPage(browser, file, {width: 1440, height: 900}, 'desktop');
      await verifyPage(browser, file, {width: 390, height: 844}, 'mobile');
    }
    fs.writeFileSync(output + '/summary.json', JSON.stringify(results, null, 2));
    console.log(JSON.stringify({passed: results.length, pages, results}, null, 2));
  } finally {
    await browser.close();
  }
})().catch(e => { console.error(e); process.exit(1); });
