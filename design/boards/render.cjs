// Render HTML files to PNG with Playwright's Chromium.
// Usage: node render.cjs jobs.json
// jobs.json: [{ "html": "/abs/file.html", "w": 512, "h": 512, "out": "/abs/out.png", "scale": 1, "fullPage": false }]
// Uses HTTPS_PROXY when set so Google Fonts load; waits for fonts before each shot.
const fs = require('fs');
let pw;
try { pw = require('playwright'); } catch (e) { pw = require('/opt/node-tools/node_modules/playwright'); }

(async () => {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const proxy = process.env.HTTPS_PROXY || process.env.https_proxy;
  const browser = await pw.chromium.launch(proxy ? { proxy: { server: proxy } } : {});
  const ctx = await browser.newContext({ ignoreHTTPSErrors: true });
  for (const j of jobs) {
    const page = await ctx.newPage({});
    await page.setViewportSize({ width: j.w, height: j.h });
    if (j.scale && j.scale !== 1) {
      await page.close();
      const c2 = await browser.newContext({ ignoreHTTPSErrors: true, viewport: { width: j.w, height: j.h }, deviceScaleFactor: j.scale });
      const p2 = await c2.newPage();
      await shoot(p2, j);
      await c2.close();
      continue;
    }
    await shoot(page, j);
    await page.close();
  }
  await browser.close();
})();

async function shoot(page, j) {
  await page.goto('file://' + j.html, { waitUntil: 'networkidle', timeout: 60000 }).catch(() => {});
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: j.out, fullPage: !!j.fullPage, omitBackground: !!j.transparent });
  console.log('png', j.out.split('/').slice(-2).join('/'));
}
