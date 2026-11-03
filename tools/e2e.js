// End-to-end test: drives the real app in Chromium.
// Usage: node tools/e2e.js [screenshotDir]   (serves ./app on a local port)
const { chromium } = require("playwright");
const http = require("http");
const fs = require("fs");
const path = require("path");
const assert = require("assert");

const ROOT = path.join(__dirname, "..", "app");
const SHOTS = process.argv[2];
const TYPES = { ".html": "text/html", ".js": "text/javascript", ".css": "text/css", ".woff2": "font/woff2" };

const server = http.createServer((req, res) => {
  const p = path.join(ROOT, decodeURIComponent(req.url.split("?")[0]).replace(/^\/$/, "/index.html"));
  if (!p.startsWith(ROOT) || !fs.existsSync(p)) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { "Content-Type": TYPES[path.extname(p)] || "application/octet-stream" });
  fs.createReadStream(p).pipe(res);
});

(async () => {
  await new Promise((r) => server.listen(0, r));
  const url = `http://localhost:${server.address().port}/`;
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1366, height: 860 } });
  const errors = [];
  page.on("pageerror", (e) => errors.push(e.message));
  page.on("console", (m) => { if (m.type() === "error" && !/desmos/i.test(m.text())) errors.push(m.text()); });
  page.on("dialog", (d) => d.accept());
  // The sandbox that runs this test can't reach desmos.com, so serve a stand-in that
  // implements the parts of the Desmos API the app uses. Pass --real-desmos to skip.
  const calls = [];
  if (!process.argv.includes("--real-desmos")) {
    await page.route(/desmos\.com\/api/, (route) => route.fulfill({ contentType: "text/javascript", body: `
      window.Desmos = { GraphingCalculator(el, opts) {
        window.__desmosCalls = (window.__desmosCalls || []).concat(["create:" + JSON.stringify(opts)]);
        el.innerHTML = '<div class="dcg-container" style="height:100%;background:#f7f9fc;display:grid;place-items:center;color:#666">[Desmos calculator stand-in]</div>';
        return { resize() { window.__desmosCalls.push("resize"); }, destroy() { window.__desmosCalls.push("destroy"); } };
      } };` }));
  }
  const shot = async (name) => { if (SHOTS) await page.screenshot({ path: path.join(SHOTS, name + ".png") }); };
  const step = (s) => console.log("  - " + s);

  await page.goto(url);
  await page.fill("#nameIn", "Test Student");
  await page.press("#nameIn", "Tab");
  await shot("01-home");

  // Answer the current question. correct=true picks the key; false picks a wrong answer.
  async function answer(correct) {
    const id = await page.evaluate(() => {
      const s = JSON.parse(localStorage.getItem("satMathPractice.v1")).active;
      return s.items[s.idx].id;
    });
    const q = await page.evaluate((id) => window.SAT_QUESTIONS.find((q) => q.id === id), id);
    if (q.type === "mc") {
      const pick = correct ? q.answer : "ABCD".replace(q.answer, "")[0];
      await page.click(`.choice[data-o="${pick}"]`);
    } else {
      let v = q.answer;
      if (v.length > (v.startsWith("-") ? 6 : 5)) v = String(eval(v)).slice(0, v.startsWith("-") ? 6 : 5);
      await page.fill("#sprIn", correct ? v : "99999");
    }
    return q;
  }

  // ---------------------------------------------------------------- full section
  step("full section: module 1");
  await page.click("#fullBtn");
  assert.strictEqual(await page.textContent("#secTitle"), "Section 1, Module 1: Math");
  assert.match(await page.textContent("#timer"), /^3[45]:\d\d$/);
  assert.match(await page.textContent("#navBtn"), /Question 1 of 22/);
  let sawSpr = false, sawMc = false;
  for (let i = 0; i < 22; i++) {
    const q = await answer(i < 16);
    if (q.type === "spr" && !sawSpr) { sawSpr = true; await shot("03-spr-question"); }
    if (q.type === "mc" && !sawMc) { sawMc = true; await shot("02-mc-question"); }
    if (i === 2) {
      await page.click("#markBtn");
      assert.match(await page.textContent("#markBtn"), /Marked/);
    }
    await page.click("#nextBtn");
  }
  assert.match(await page.textContent("#qscroll"), /Check Your Work/);
  assert.strictEqual(await page.locator(".grid .gbox.ans").count(), 22);
  assert.strictEqual(await page.locator(".grid .gbox.flag").count(), 1);
  await shot("04-check-your-work");
  await page.click("#nextBtn");               // submit (dialog auto-accepted)
  await page.waitForSelector("#beginM2");
  const route = await page.evaluate(() => JSON.parse(localStorage.getItem("satMathPractice.v1")).active.route);
  assert.strictEqual(route, "m2hard", "16/22 correct must route to the harder module");
  step("routed to harder module 2 after 16/22");
  await page.click("#beginM2");
  assert.strictEqual(await page.textContent("#secTitle"), "Section 1, Module 2: Math");

  // calculator
  await page.click("#calcBtn");
  await page.waitForTimeout(4000);
  const desmosOk = await page.evaluate(() => !!document.querySelector("#desmos .dcg-container, #desmos .dcg-calculator-api-container"));
  if (!process.argv.includes("--real-desmos")) {
    assert(desmosOk, "Desmos stand-in should mount");
    await page.click("#calcWide");
    assert(await page.evaluate(() => document.querySelector("#calcPanel").classList.contains("wide")));
    assert((await page.evaluate(() => window.__desmosCalls)).includes("resize"));
  }
  const desmosMsg = await page.textContent("#desmos");
  step(desmosOk ? "Desmos calculator loaded" : "Desmos unavailable here; fallback message shown: " + /couldn't load/.test(desmosMsg));
  assert(desmosOk || /couldn't load/.test(desmosMsg));
  await shot("05-calculator");
  await page.click("#calcClose");

  // reference + navigator
  await page.click("#refBtn");
  assert.match(await page.textContent(".pop"), /Pythagorean/);
  await shot("06-reference");
  await page.click(".pop .close");
  await page.click("#navBtn");
  assert.strictEqual(await page.locator("#overlay .grid .gbox").count(), 22);
  await shot("07-navigator");
  await page.click("#overlay .gbox[data-i='5']");
  assert.match(await page.textContent("#navBtn"), /Question 6 of 22/);

  // module 2: answer half, leave rest blank, then submit via review page
  for (let i = 0; i < 6; i++) { await answer(i % 2 === 0); await page.click("#nextBtn"); }
  await page.click("#navBtn");
  await page.click("#toReview");
  await page.click("#nextBtn");
  await page.waitForSelector(".bigscore");
  const score = +(await page.textContent(".bigscore"));
  step(`results page: estimated score ${score}`);
  assert(score >= 200 && score <= 800);
  assert.strictEqual(await page.locator(".qitem").count(), 44);
  await page.click(".qitem summary");
  await shot("08-results");

  // ---------------------------------------------------------------- practice with feedback
  step("adaptive practice with feedback");
  await page.click("#homeBtn");
  await page.selectOption("#pLen", "10");
  await page.click("#practiceBtn");
  assert.match(await page.textContent("#nextBtn"), /Check Answer/);
  await answer(false);
  await page.click("#nextBtn");
  await page.waitForSelector(".feedback.no");
  assert.match(await page.textContent(".feedback"), /Not quite/);
  await shot("09-practice-feedback");
  await page.click("#nextBtn");
  for (let i = 1; i < 10; i++) {
    await answer(true);
    await page.click("#nextBtn");
    await page.waitForSelector(".feedback.ok");
    await page.click("#nextBtn");
  }
  await page.waitForSelector(".bigscore");
  assert.strictEqual((await page.textContent(".bigscore")).trim(), "9/10");
  step("practice results 9/10");

  // ---------------------------------------------------------------- resume
  step("save & resume");
  await page.click("#homeBtn");
  await page.click("#practiceBtn");
  await answer(true);
  await page.click("#moreBtn");
  await page.click("#saveExit");
  await page.reload();
  await page.click("#resumeBtn");
  assert(await page.locator("#test").count());
  await page.click("#moreBtn");
  await page.click("#endNow");
  await page.waitForSelector(".bigscore");

  // ---------------------------------------------------------------- parent area renders every question
  step("parent area: render every question");
  await page.click("#homeBtn");
  await shot("10-home-progress");
  await page.click("#parentBtn");
  const n = await page.locator(".bank-q").count();
  const katexErrors = await page.locator(".katex-error").count();
  const rawDelims = await page.evaluate(() => [...document.querySelectorAll(".bank-q")].filter((el) => /\\\(|\\\[/.test(el.innerText)).map((el) => el.querySelector("b").textContent));
  assert.strictEqual(n, await page.evaluate(() => window.SAT_QUESTIONS.length));
  assert.strictEqual(katexErrors, 0, "KaTeX errors in rendered bank");
  assert.deepStrictEqual(rawDelims, [], "unrendered math delimiters");
  await shot("11-parent");
  // remove a question
  const firstId = await page.textContent(".bank-q .head b");
  await page.check(`[data-dis="${firstId}"]`);
  const dis = await page.evaluate(() => JSON.parse(localStorage.getItem("satMathPractice.v1")).disabled);
  assert(dis[firstId]);

  // mobile layout sanity
  await page.setViewportSize({ width: 390, height: 844 });
  await page.click("#homeBtn");
  const overflow = await page.evaluate(() => [...document.querySelectorAll("body *")]
    .filter((e) => e.getBoundingClientRect().right > window.innerWidth + 1)
    .map((e) => e.tagName + "." + e.className));
  assert.deepStrictEqual(overflow, [], "no horizontal scroll on phone width");
  await shot("12-mobile-home");

  assert.deepStrictEqual(errors, [], "browser errors");
  console.log(`\nE2E passed (${n} questions rendered, 0 KaTeX errors, 0 page errors)`);
  await browser.close();
  server.close();
})().catch(async (e) => { console.error(e); process.exit(1); });
