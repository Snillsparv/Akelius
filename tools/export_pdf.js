#!/usr/bin/env node
// Renderar export/build/cards-<lang>.html till PDF i stående A6 med systemets Chromium.
// Framsidans text, fråga och svar sätts i Verdana 11 och stegas ned till 7 tills de ryms
// under bilden; baksidans ordförklaringar stegas från 9,5 till 7. Storleken per kort
// skrivs i sidfoten och i en JSON-rapport. Ryms ett kort inte ens då avbryts körningen.
// Anropas av tools/export_cards.py:  node tools/export_pdf.js <html> <pdf> <sidor> <rapport.json>
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright-core');

const FRONT = [11, 10.5, 10, 9.5, 9, 8.5, 8, 7.5, 7];
const BACK = [9.5, 9, 8.5, 8, 7.5, 7];

(async () => {
  const [htmlPath, pdfPath, expectedPages, reportPath] = process.argv.slice(2);
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(htmlPath), { waitUntil: 'load' });
  await page.evaluate(async () => {
    await document.fonts.ready;
    await Promise.all([...document.images].map(img => img.decode().catch(() => {})));
  });
  const result = await page.evaluate(({ FRONT, BACK }) => {
    const overflows = el => el.scrollHeight > el.clientHeight + 1 || el.scrollWidth > el.clientWidth + 1;
    const fit = (sec, sel, prop, sizes) => {
      const box = sec.querySelector(sel);
      for (const pt of sizes) {
        sec.style.setProperty(prop, pt + 'pt');
        if (!overflows(box)) return pt;
      }
      return null;
    };
    const dec = document.documentElement.lang === 'sv' ? ',' : '.';
    const report = {}, failed = [];
    let broken = 0;
    for (const sec of document.querySelectorAll('section.card')) {
      const id = sec.dataset.id;
      report[id] = report[id] || {};
      if (sec.classList.contains('front')) {
        const pt = fit(sec, '.content', '--fs', FRONT);
        report[id].front = pt;
        if (pt === null) failed.push(id + ' framsida');
        else sec.querySelector('.fsz').textContent = String(pt).replace('.', dec);
      } else {
        const pt = fit(sec, '.expl', '--ws', BACK);
        report[id].back = pt;
        if (pt === null) failed.push(id + ' baksida');
      }
      broken += [...sec.querySelectorAll('img')].filter(i => !i.complete || i.naturalWidth === 0).length;
    }
    return { report, failed, broken, cards: document.querySelectorAll('section.front').length,
             pages: document.querySelectorAll('section.page').length };
  }, { FRONT, BACK });
  const fronts = Object.values(result.report).map(r => r.front).filter(x => x !== null);
  const hist = FRONT.map(pt => `${pt}: ${fronts.filter(x => x === pt).length}`).join(', ');
  const smallBack = Object.entries(result.report).filter(([, r]) => r.back !== null && r.back < BACK[0]);
  console.log(`${path.basename(pdfPath)}: ${result.pages} sidor, ${result.cards} kort, ` +
              `${result.broken} trasiga bilder`);
  console.log(`  framsidans textstorlek (pt: kort): ${hist}`);
  if (smallBack.length) console.log(`  baksidor med mindre ordtext: ${smallBack.length}`);
  fs.writeFileSync(reportPath, JSON.stringify(result.report));
  if (result.failed.length || result.broken || String(result.pages) !== String(expectedPages)) {
    console.error('AVBRYTER: ryms ej ' + JSON.stringify(result.failed) +
                  `, trasiga bilder ${result.broken}, sidor ${result.pages} (väntat ${expectedPages})`);
    await browser.close();
    process.exit(1);
  }
  await page.pdf({ path: pdfPath, width: '105mm', height: '148mm', printBackground: true,
                   preferCSSPageSize: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  await browser.close();
})();
