// Kör: NODE_PATH=node_modules node tools/measure_a6_fit.js [ut.json]
// Mäter hur kortens framsida får plats på stående A6 (105x148 mm) med bilden 3:2 överst i full bredd.
// För varje kort och språk: största Verdana-storlek (pt) där text, fråga och 2x2-svar ryms.
const fs = require('fs');
const { chromium } = require('playwright-core');
const data = JSON.parse(fs.readFileSync('/home/user/Akelius/data/cards.json', 'utf8'));
const SIZES = [11, 10.5, 10, 9.5, 9, 8.5, 8, 7.5, 7];
const esc = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const css = `
@page { size: 105mm 148mm; margin: 0; }
body { margin: 0; font-family: Verdana, 'DejaVu Sans', sans-serif; }
.f { width: 105mm; height: 148mm; padding: 6mm 6mm 5mm; box-sizing: border-box; display: flex; flex-direction: column; overflow: hidden; }
.pic { width: 93mm; height: 62mm; background: #ccc; flex: none; }
.body { flex: 1; display: flex; flex-direction: column; overflow: hidden; margin-top: 3mm; }
.text p { margin: 0; display: inline; }
.text { line-height: 1.3; }
.q { font-weight: bold; margin-top: 1.6mm; line-height: 1.25; }
.opts { display: grid; grid-template-columns: 1fr 1fr; gap: 1.2mm 3mm; margin-top: 1.6mm; }
.opts div { display: flex; gap: 1.6mm; line-height: 1.2; }
.opts i { width: 3.2mm; height: 3.2mm; border: .3mm solid #000; flex: none; margin-top: .3mm; }
.foot { font-size: 6.5pt; color: #555; margin-top: auto; padding-top: 1mm; flex: none; }`;
const cards = [];
for (const s of data.sets) s.cards.forEach((c, i) => {
  for (const lang of ['en', 'sv']) {
    const L = lang === 'sv' ? { t: c.sv.text_sentences, q: c.sv.question, o: c.sv.options } : { t: c.text_sentences, q: c.question, o: c.options };
    cards.push({ id: `${s.slug}-${i + 1}`, lang, level: c.level, words: L.t.join(' ').split(/\s+/).length,
      html: `<div class="f"><div class="pic"></div><div class="body"><div class="text">${L.t.map(x => '<p>' + esc(x) + ' </p>').join('')}</div>` +
            `<div class="q">${esc(L.q)}</div><div class="opts">${L.o.map(o => '<div><i></i><span>' + esc(o) + '</span></div>').join('')}</div></div>` +
            `<div class="foot">category · level</div></div>` });
  }
});
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await browser.newPage();
  await page.setContent(`<html><head><style>${css}</style></head><body>${cards.map((c, k) => `<section id="c${k}">${c.html}</section>`).join('')}</body></html>`);
  const res = await page.evaluate(({ n, SIZES }) => {
    const out = [];
    for (let k = 0; k < n; k++) {
      const sec = document.getElementById('c' + k), body = sec.querySelector('.body');
      let fit = null;
      for (const pt of SIZES) {
        body.style.fontSize = pt + 'pt';
        if (body.scrollHeight <= body.clientHeight + 1) { fit = pt; break; }
      }
      out.push(fit);
    }
    return out;
  }, { n: cards.length, SIZES });
  await browser.close();
  const rows = cards.map((c, k) => ({ id: c.id, lang: c.lang, level: c.level, words: c.words, fit: res[k] }));
  fs.writeFileSync(process.argv[2] || '/dev/null', JSON.stringify(rows));
  for (const lang of ['en', 'sv']) {
    const r = rows.filter(x => x.lang === lang);
    const line = [...SIZES, null].map(pt => `${pt === null ? 'ryms ej vid 7' : pt + 'pt'}: ${r.filter(x => x.fit === pt).length}`).join(' | ');
    console.log(lang, line);
    const at = t => r.filter(x => x.fit !== null && x.fit >= t).length;
    console.log(`  ryms vid minst 11pt: ${at(11)}, minst 10pt: ${at(10)}, minst 9pt: ${at(9)}, minst 8pt: ${at(8)} av ${r.length}`);
  }
})();
