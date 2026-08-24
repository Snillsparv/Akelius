#!/usr/bin/env node
// Bygger Word-underlagen till poängpromenaden i Vara från poangpromenad/stationer.md:
//   poangpromenad/Historia-poangpromenad-Vara.docx   (skyltunderlag till Claes, utan facit)
//   poangpromenad/Historia-poangpromenad-facit.docx  (separat facit)
// Förhandsvisningsbilder (nedskalade) läses från poangpromenad/bilder-preview/.
// Kör: node tools/build_poangpromenad_docx.js

const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, ImageRun, HeadingLevel,
  Table, TableRow, TableCell, WidthType, BorderStyle, AlignmentType, PageBreak,
} = require('docx');

const ROOT = path.resolve(__dirname, '..');
const MD = fs.readFileSync(path.join(ROOT, 'poangpromenad', 'stationer.md'), 'utf8');
const PREVIEW_DIR = path.join(ROOT, 'poangpromenad', 'bilder-preview');

function parse(md) {
  const signs = [];
  for (const block of md.split(/^## Skylt /m).slice(1)) {
    const nr = parseInt(block, 10);
    if (!nr) continue;
    const qs = [];
    for (const qb of block.split(/^### /m).slice(1)) {
      const head = qb.match(/^(Lätt|Normal) \((årskurs [\d-]+)\) · kategori: (\S+) · bild: (\S+)/);
      if (!head) continue;
      const text = [...qb.matchAll(/^> (.+)$/gm)].map(m => m[1]);
      const opts = [...qb.matchAll(/^- (✅|⬜) (.+)$/gm)].map(m => ({ correct: m[1] === '✅', text: m[2] }));
      const fraga = (qb.match(/Fråga: (.+?)$/m) || [])[1];
      qs.push({ level: head[1], arskurs: head[2], kategori: head[3], bild: head[4], text, opts, fraga });
    }
    if (qs.length === 2) signs.push({ nr, latt: qs[0], normal: qs[1] });
  }
  return signs;
}

const signs = parse(MD);
if (signs.length !== 10) throw new Error(`förväntade 10 skyltar, fick ${signs.length}`);
for (const s of signs) for (const q of [s.latt, s.normal]) {
  if (q.opts.length !== 4 || q.opts.filter(o => o.correct).length !== 1)
    throw new Error(`skylt ${s.nr} ${q.level}: alternativfel`);
  if (q.text.length < 5 || q.text.length > 8)
    throw new Error(`skylt ${s.nr} ${q.level}: ${q.text.length} meningar`);
}

const FONT = 'Verdana';
const p = (text, opts = {}) => new Paragraph({
  children: [new TextRun({ text, font: FONT, size: opts.size || 22, bold: opts.bold, italics: opts.italics, color: opts.color })],
  spacing: { after: opts.after ?? 80 },
  ...(opts.heading ? { heading: opts.heading } : {}),
});

function questionBlock(signNr, q, includeFacit) {
  const out = [];
  out.push(new Paragraph({
    children: [
      new TextRun({ text: `Skylt ${signNr} · ${q.level} (${q.arskurs})`, font: FONT, size: 28, bold: true }),
      new TextRun({ text: `   ·   kategori: ${q.kategori}`, font: FONT, size: 22, color: '555555' }),
    ],
    spacing: { before: 160, after: 140 },
  }));
  const img = path.join(PREVIEW_DIR, q.bild);
  if (fs.existsSync(img)) {
    out.push(new Paragraph({
      children: [new ImageRun({ type: 'jpg', data: fs.readFileSync(img), transformation: { width: 300, height: 200 } })],
      spacing: { after: 40 },
    }));
  }
  out.push(p(`Bildfil: ${q.bild}`, { size: 16, color: '888888', after: 120 }));
  for (const t of q.text) out.push(p(t));
  out.push(p(' ', { after: 20 }));
  for (const o of q.opts) {
    const mark = includeFacit && o.correct ? '✅' : '☐';
    out.push(new Paragraph({
      children: [new TextRun({
        text: `${mark}  ${o.text}`, font: FONT, size: 22,
        bold: includeFacit && o.correct,
      })],
      spacing: { after: 40 },
    }));
  }
  return out;
}

// ---- Skyltunderlaget (utan facit) ----
const stationChildren = [
  p('Historia till poängpromenaden', { size: 40, bold: true, after: 120 }),
  p('Akelius Math Factory, Vara', { size: 26, color: '555555', after: 240 }),
  p('Tio skyltar med två historiefrågor vardera: en lätt (årskurs 6-9) och en normal (årskurs 9-12), i kronologisk ordning från Mesopotamien till Djingis khan. Frågorna är hämtade ur den pågående produktionen av Akelius quiz cards och följer samma upplägg som geografiunderlaget: kort ledtrådstext, ett kategoriord och fyra svarsalternativ.'),
  p('Bilderna följer med som separata JPEG-filer i full upplösning (1536 x 1024, liggande 3:2). Förhandsvisningarna i detta dokument är förminskade. Bilderna är AI-illustrationer i enhetlig stil, framtagna och faktagranskade för korten.'),
  p('De rätta svaren står i ett separat facitdokument, inte här, så att detta underlag kan användas direkt för skyltlayout.'),
  p('Frågor? Jonas von Essen, jonas.superminne@gmail.com', { italics: true, after: 240 }),
];
for (const s of signs) {
  for (const q of [s.latt, s.normal]) {
    stationChildren.push(new Paragraph({ children: [new PageBreak()] }));
    stationChildren.push(...questionBlock(s.nr, q, false));
  }
}

// ---- Facit ----
const cell = (text, opts = {}) => new TableCell({
  width: { size: opts.w, type: WidthType.DXA },
  children: [new Paragraph({
    children: [new TextRun({ text, font: FONT, size: 20, bold: opts.bold })],
    spacing: { after: 20 },
  })],
});
const facitRows = [new TableRow({ children: [
  cell('Skylt', { w: 900, bold: true }),
  cell('Lätt (årskurs 6-9)', { w: 4050, bold: true }),
  cell('Normal (årskurs 9-12)', { w: 4050, bold: true }),
] })];
for (const s of signs) {
  const answer = q => `${q.opts.find(o => o.correct).text}  (${q.kategori})`;
  facitRows.push(new TableRow({ children: [
    cell(String(s.nr), { w: 900 }),
    cell(answer(s.latt), { w: 4050 }),
    cell(answer(s.normal), { w: 4050 }),
  ] }));
}
const facitChildren = [
  p('Facit: historia till poängpromenaden', { size: 36, bold: true, after: 120 }),
  p('Akelius Math Factory, Vara. Endast för funktionärer, ska inte sitta på skyltarna.', { color: '555555', after: 240 }),
  new Table({ columnWidths: [900, 4050, 4050], width: { size: 9000, type: WidthType.DXA }, rows: facitRows }),
];

async function main() {
  for (const [file, children] of [
    ['Historia-poangpromenad-Vara.docx', stationChildren],
    ['Historia-poangpromenad-facit.docx', facitChildren],
  ]) {
    const doc = new Document({ sections: [{ children }] });
    fs.writeFileSync(path.join(ROOT, 'poangpromenad', file), await Packer.toBuffer(doc));
    console.log('skrev', file);
  }
}
main();
