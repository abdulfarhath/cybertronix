const { chromium } = require('/opt/node-tools/node_modules/playwright');
const fs = require('fs');
(async () => {
  const b = await chromium.launch();
  const out = {};
  for (const f of fs.readdirSync('canvas/project').filter(f => /^(Main|P\d|StyleGuide)/.test(f) && f.endsWith('.dc.html'))) {
    const w = f.includes('phone') ? 390 : 1440;
    const p = await b.newPage({ viewport: { width: w, height: 800 } });
    await p.route('**/*', r => r.request().url().startsWith('file:') ? r.continue() : r.abort());
    await p.goto('file://' + process.cwd() + '/canvas/project/' + f);
    out[f] = await p.evaluate(() => { const d = document.querySelector('x-dc > div'); d.style.minHeight = '0'; return [Math.ceil(d.scrollHeight), document.documentElement.scrollWidth]; });
    if (f === 'Main.dc.html' || f === 'P2-Humanoid-phone.dc.html') await p.screenshot({ path: 'shot-' + f + '.png', fullPage: true });
    await p.close();
  }
  console.log(JSON.stringify(out));
  await b.close();
})();
