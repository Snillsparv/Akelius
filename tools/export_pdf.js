#!/usr/bin/env node
// Renderar export/build/cards-<lang>.html till PDF med systemets Chromium.
// Varje kortsida kontrolleras: flödar text, bilder eller bildbriefer över tilldelad yta
// stegas typografin ned (fit1..fit3). Finns överflöd kvar avbryts körningen.
// Anropas av tools/export_cards.py:  node tools/export_pdf.js <html> <pdf> <sidor>
const path = require('path');
const { chromium } = require('playwright-core');

(async () => {
  const [htmlPath, pdfPath, expectedPages] = process.argv.slice(2);
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(htmlPath), { waitUntil: 'load' });
  await page.evaluate(async () => {
    await Promise.all([...document.images].map(img => img.decode().catch(() => {})));
  });
  const result = await page.evaluate(() => {
    const overflows = el => el.scrollHeight > el.clientHeight + 1 || el.scrollWidth > el.clientWidth + 1;
    const check = sec => ['.textcol', '.text', '.right', '.back', '.body', '.ph.main', '.ph.side']
      .map(s => sec.querySelector(s)).filter(Boolean).some(overflows)
      || (() => { // sidobild eller baksidans innehåll får inte hamna utanför baksidan
        const back = sec.querySelector('.back');
        const last = back && back.lastElementChild;
        return last && last.getBoundingClientRect().bottom > back.getBoundingClientRect().bottom + 1;
      })();
    const fitted = {}, failed = [];
    let broken = 0;
    for (const sec of document.querySelectorAll('section.card')) {
      let level = 0;
      while (check(sec) && level < 3) {
        if (level) sec.classList.remove('fit' + level);
        level += 1;
        sec.classList.add('fit' + level);
      }
      if (check(sec)) failed.push(sec.dataset.id);
      else if (level) fitted[sec.dataset.id] = level;
      broken += [...sec.querySelectorAll('img')].filter(i => !i.complete || i.naturalWidth === 0).length;
    }
    return { fitted, failed, broken, cards: document.querySelectorAll('section.card').length,
             pages: document.querySelectorAll('section.page').length };
  });
  const fittedCount = Object.keys(result.fitted).length;
  console.log(`${path.basename(pdfPath)}: ${result.pages} sidor, ${result.cards} kort, ` +
              `${fittedCount} med tätare typografi, ${result.broken} trasiga bilder`);
  if (fittedCount) console.log('  tätare: ' + JSON.stringify(result.fitted));
  if (result.failed.length || result.broken || String(result.pages) !== String(expectedPages)) {
    console.error('AVBRYTER: överflöd ' + JSON.stringify(result.failed) +
                  `, trasiga bilder ${result.broken}, sidor ${result.pages} (väntat ${expectedPages})`);
    await browser.close();
    process.exit(1);
  }
  await page.pdf({ path: pdfPath, width: '297mm', height: '210mm', printBackground: true,
                   preferCSSPageSize: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  await browser.close();
})();
