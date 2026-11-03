/* SAT Math Practice: user interface. Depends on window.SAT_QUESTIONS and window.Engine. */
(function () {
  "use strict";

  const QUESTIONS = window.SAT_QUESTIONS;
  const DOMAINS = window.SAT_DOMAINS;
  const SKILLS = window.SAT_SKILLS;
  const byId = Object.fromEntries(QUESTIONS.map((q) => [q.id, q]));
  const L = ["A", "B", "C", "D"];
  const STORE = "satMathPractice.v1";
  // Desmos's public demo API key. To use your own, replace it here (see README).
  const DESMOS_URL = "https://www.desmos.com/api/v1.9/calculator.js?apiKey=dcb31709b452b1cf9dc26972add0fda6";

  const app = document.getElementById("app");
  let state = load();
  let S = null;                 // the active session (also mirrored to state.active)
  let tickTimer = null, tickCount = 0, timerHidden = false, crossMode = false;
  let desmosCalc = null, desmosLoading = null, calcOpen = false, calcWide = false;

  // ------------------------------------------------------------------ storage
  function load() {
    try {
      const raw = JSON.parse(localStorage.getItem(STORE));
      if (raw && raw.version === 1) return Object.assign(Engine.defaultState(), raw);
    } catch (e) { /* storage unavailable or corrupt: start fresh */ }
    return Engine.defaultState();
  }
  function save() {
    state.active = S;
    try { localStorage.setItem(STORE, JSON.stringify(state)); } catch (e) { /* ignore */ }
  }

  // ------------------------------------------------------------------ helpers
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const $ = (sel, el) => (el || document).querySelector(sel);
  const $$ = (sel, el) => [...(el || document).querySelectorAll(sel)];
  function math(el) {
    if (window.renderMathInElement) {
      renderMathInElement(el, {
        delimiters: [{ left: "\\[", right: "\\]", display: true }, { left: "\\(", right: "\\)", display: false }],
        throwOnError: false,
      });
    }
  }
  function view(html) {
    stopTick();
    destroyCalc();
    app.innerHTML = html;
    math(app);
    window.scrollTo(0, 0);
  }
  const fmtTime = (s) => { s = Math.max(0, Math.round(s)); return `${Math.floor(s / 60)}:${String(s % 60).padStart(2, "0")}`; };
  const pct = (a, b) => (b ? Math.round((100 * a) / b) : 0);
  const shuffle = (arr) => { for (let i = arr.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [arr[i], arr[j]] = [arr[j], arr[i]]; } return arr; };
  const level = (theta) => Math.max(200, Math.min(800, Math.round((500 + 100 * theta) / 10) * 10));
  const lvlClass = (p) => (p == null ? "lvl-none" : p < 0.45 ? "lvl-low" : p < 0.7 ? "lvl-mid" : "lvl-hi");
  const diffTag = (d) => `<span class="tag">${Engine.DIFF_NAME[d]}</span>`;
  const calcTag = (q) => q.desmos ? `<span class="tag desmos">Desmos</span>` : `<span class="tag hand">By hand</span>`;

  function makeItem(q) {
    let order = [0, 1, 2, 3];
    if (q.type === "mc") order = q.ordered ? (Math.random() < 0.5 ? order : order.reverse()) : shuffle(order);
    return { id: q.id, resp: null, marked: false, crossed: [], secs: 0, locked: false, correct: null, order };
  }
  const displayLetter = (item, orig) => L[item.order.indexOf(L.indexOf(orig))];

  const ICON = {
    calc: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="5" y="2.5" width="14" height="19" rx="2"/><rect x="8" y="5.5" width="8" height="4" rx=".5"/><path d="M8.5 13h.01M12 13h.01M15.5 13h.01M8.5 16.5h.01M12 16.5h.01M15.5 16.5h.01" stroke-width="2.4" stroke-linecap="round"/></svg>',
    ref: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M4 4h11l5 5v11H4z"/><path d="M15 4v5h5M8 13h8M8 16.5h8M8 9.5h4"/></svg>',
    more: '<svg viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="5" r="1.8"/><circle cx="12" cy="12" r="1.8"/><circle cx="12" cy="19" r="1.8"/></svg>',
    mark: '<svg viewBox="0 0 24 24"><path d="M6 3h12v18l-6-4.5L6 21z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>',
  };

  // ================================================================== HOME
  function home() {
    S = state.active;
    const answered = Object.values(state.items).reduce((a, it) => a + it.n, 0);
    const missed = Object.entries(state.items).filter(([id, it]) => !it.lastCorrect && byId[id] && !state.disabled[id]).length;
    const resume = S ? `
      <div class="card resume">
        <h2>Resume: ${esc(S.title)}</h2>
        <p class="grow">${S.kind === "full" ? `Module ${S.moduleNo}, ` : ""}question ${S.idx + 1}${S.timed ? `, ${fmtTime(S.timeLeft)} left` : ""}.</p>
        <div><button class="btn primary" id="resumeBtn">Resume</button> <button class="btn warn small" id="abandonBtn">Discard</button></div>
      </div>` : "";
    view(`
    <div class="page">
      <div class="hero">
        <div><h1>SAT Math Practice</h1><p>Hard, verified questions &middot; Desmos built in &middot; adapts to what you miss</p></div>
        <label class="namefield">Student name <input id="nameIn" value="${esc(state.name)}" placeholder="Your name" maxlength="30"></label>
      </div>
      <div class="cards">
        ${resume}
        <div class="card">
          <h2>Full Math Section</h2>
          <p class="grow">Two 22-question modules, 35 minutes each, just like the digital SAT. How you do on Module 1 decides whether Module 2 is the harder or the standard version. You get an estimated score at the end.</p>
          <div><button class="btn primary" id="fullBtn" ${S ? "disabled" : ""}>Start full section</button></div>
        </div>
        <div class="card">
          <h2>Adaptive Practice</h2>
          <p>Each question is chosen from your weakest skills, at a difficulty just above your current level.</p>
          <div class="form grow">
            <label for="pLen">Questions</label><select id="pLen"><option>10</option><option selected>15</option><option>22</option></select>
            <label for="pDom">Focus</label><select id="pDom"><option value="ALL">All domains</option>${Object.entries(DOMAINS).map(([k, v]) => `<option value="${k}">${v}</option>`).join("")}</select>
            <label for="pCalc">Style</label><select id="pCalc"><option value="mix">Mix (Desmos + by hand)</option><option value="desmos">Desmos only</option><option value="hand">By hand only</option></select>
            <label for="pFb">Feedback</label><select id="pFb"><option value="1">After each question</option><option value="0">At the end (test-like)</option></select>
            <label for="pTime">Timing</label><select id="pTime"><option value="1">SAT pace (1:35 each)</option><option value="0">Untimed</option></select>
          </div>
          <div><button class="btn primary" id="practiceBtn" ${S ? "disabled" : ""}>Start practice</button></div>
        </div>
        <div class="card">
          <h2>Retry Missed Questions</h2>
          <p class="grow">${missed ? `${missed} question${missed === 1 ? "" : "s"} you got wrong last time. Explanations are shown after each one.` : "Nothing to retry yet. Questions you miss will show up here."}</p>
          <div><button class="btn primary" id="retryBtn" ${missed && !S ? "" : "disabled"}>Retry missed</button></div>
        </div>
      </div>
      ${S ? `<p class="small muted">Finish or discard the session in progress to start a new one.</p>` : ""}
      ${progressHTML(answered)}
      ${historyHTML()}
      <p class="small muted" style="margin-top:40px">${QUESTIONS.length} questions in the bank, each with an answer re-derived by a computer check.
        &middot; <button class="linkbtn" id="parentBtn">Parent area (answer key &amp; settings)</button></p>
    </div>`);

    $("#nameIn").addEventListener("change", (e) => { state.name = e.target.value.trim(); save(); });
    if (S) {
      $("#resumeBtn").onclick = () => S.phase === "between" ? betweenModules() : renderTest();
      $("#abandonBtn").onclick = () => { if (confirm("Discard the session in progress? Answers in it will not be saved.")) { S = null; save(); home(); } };
    }
    $("#fullBtn").onclick = startFull;
    $("#practiceBtn").onclick = () => startPractice({
      len: +$("#pLen").value, domain: $("#pDom").value, calc: $("#pCalc").value,
      feedback: $("#pFb").value === "1", timed: $("#pTime").value === "1",
    });
    $("#retryBtn").onclick = startRetry;
    $("#parentBtn").onclick = parentGate;
    $$("[data-session]").forEach((b) => (b.onclick = () => results(state.sessions.find((s) => s.id === b.dataset.session))));
  }

  function progressHTML(answered) {
    if (!answered) return `<h3 class="section-title">Your progress</h3><p class="muted">Answer some questions to see your skill levels here.</p>`;
    let rows = "";
    for (const [dom, skills] of Object.entries(SKILLS)) {
      rows += `<tr class="dom"><td colspan="4">${esc(DOMAINS[dom])}</td></tr>`;
      for (const sk of skills) {
        const rec = state.skills[sk];
        const p = rec ? Engine.mastery(state, sk) : null;
        rows += `<tr><td>${esc(sk)}</td>
          <td><div class="bar"><i class="${lvlClass(p)}" style="width:${p == null ? 0 : Math.round(p * 100)}%"></i></div></td>
          <td>${p == null ? '<span class="muted">not yet</span>' : `${Math.round(p * 100)}%`}</td>
          <td class="muted">${rec ? `${rec.correct}/${rec.n} correct` : ""}</td></tr>`;
      }
    }
    const split = desmosSplit();
    return `
      <h3 class="section-title">Your progress</h3>
      <div class="statrow">
        <div class="stat"><div class="v">${answered >= 10 ? level(state.theta) : "&mdash;"}</div><div class="l">Current level (score scale)${answered < 10 ? "<br>after 10 answers" : ""}</div></div>
        <div class="stat"><div class="v">${answered}</div><div class="l">Questions answered</div></div>
        <div class="stat"><div class="v">${split.d.n ? pct(split.d.c, split.d.n) + "%" : "&mdash;"}</div><div class="l">Desmos-question accuracy</div></div>
        <div class="stat"><div class="v">${split.h.n ? pct(split.h.c, split.h.n) + "%" : "&mdash;"}</div><div class="l">By-hand accuracy</div></div>
      </div>
      <div class="tablewrap"><table class="skills"><thead><tr><th>Skill</th><th>Chance on a hard question</th><th></th><th>History</th></tr></thead><tbody>${rows}</tbody></table></div>`;
  }

  function desmosSplit() {
    const d = { n: 0, c: 0 }, h = { n: 0, c: 0 };
    for (const [id, it] of Object.entries(state.items)) {
      const q = byId[id]; if (!q) continue;
      const t = q.desmos ? d : h; t.n += it.n; t.c += it.correct;
    }
    return { d, h };
  }

  function historyHTML() {
    if (!state.sessions.length) return "";
    const rows = state.sessions.slice().reverse().slice(0, 15).map((s) => {
      const all = s.modules.flatMap((m) => m.items);
      const c = all.filter((i) => i.correct).length;
      return `<tr><td>${new Date(s.date).toLocaleDateString()}</td><td>${esc(s.title)}</td><td>${c}/${all.length}</td>
        <td>${s.score ? `<b>${s.score.score}</b> <span class="muted small">(${s.score.low}&ndash;${s.score.high})</span>` : ""}</td>
        <td><button class="linkbtn" data-session="${s.id}">Review</button></td></tr>`;
    }).join("");
    return `<h3 class="section-title">Recent sessions</h3>
      <div class="tablewrap"><table class="skills"><thead><tr><th>Date</th><th>Session</th><th>Correct</th><th>Est. score</th><th></th></tr></thead><tbody>${rows}</tbody></table></div>`;
  }

  // ================================================================== START
  function newSession(o) {
    return Object.assign({ id: "s" + Date.now(), started: Date.now(), idx: 0, phase: "q", done: [], used: [], moduleNo: 1, route: null }, o);
  }

  function startFull() {
    const used = new Set();
    const qs = Engine.buildModule(state, QUESTIONS, "m1", used);
    S = newSession({ kind: "full", title: "Full Math Section", timed: true, timeLeft: Engine.MODULE_SEC, feedback: false, items: qs.map(makeItem), used: [...used] });
    save();
    renderTest();
  }

  function startPractice(opts) {
    const used = new Set();
    const q = Engine.nextPractice(state, QUESTIONS, opts, used);
    if (!q) { alert("No questions match those settings."); return; }
    used.add(q.id);
    const label = opts.domain === "ALL" ? "Adaptive Practice" : `Practice: ${DOMAINS[opts.domain]}`;
    S = newSession({ kind: "practice", title: label, opts, target: opts.len, timed: opts.timed, timeLeft: opts.len * Engine.PACE_SEC, feedback: opts.feedback, items: [makeItem(q)], used: [...used] });
    save();
    renderTest();
  }

  function startRetry() {
    const ids = Object.entries(state.items).filter(([id, it]) => !it.lastCorrect && byId[id] && !state.disabled[id]).map(([id]) => id);
    const opts = { len: Math.min(ids.length, 22), domain: "ALL", calc: "mix", onlyIds: ids, feedback: true, timed: false };
    const used = new Set();
    const q = Engine.nextPractice(state, QUESTIONS, opts, used);
    if (!q) return;
    used.add(q.id);
    S = newSession({ kind: "practice", title: "Retry Missed Questions", opts, target: opts.len, timed: false, timeLeft: 0, feedback: true, items: [makeItem(q)], used: [...used] });
    save();
    renderTest();
  }

  // ================================================================== TEST SHELL
  function sectionTitle() {
    if (S.kind === "full") return `Section 1, Module ${S.moduleNo}: Math`;
    return S.title;
  }

  function buildShell() {
    stopTick();
    destroyCalc();
    app.innerHTML = `
    <div class="test" id="test">
      <header class="tbar">
        <div><div class="sectitle" id="secTitle"></div><button class="dirbtn" id="dirBtn">Directions &#9662;</button></div>
        <div class="tcenter"><div class="timer" id="timer"></div>${S.timed ? '<button class="btn small" id="hideBtn">Hide</button>' : ""}</div>
        <div class="tright">
          <button class="tool" id="calcBtn">${ICON.calc}Calculator</button>
          <button class="tool" id="refBtn">${ICON.ref}Reference</button>
          <button class="tool" id="moreBtn">${ICON.more}More</button>
        </div>
      </header>
      <div class="tbody">
        <aside class="calc hidden" id="calcPanel">
          <div class="calchead">Desmos Graphing Calculator<span class="sp"></span><button id="calcWide">Expand</button><button id="calcClose">Close</button></div>
          <div id="desmos"><div class="calcmsg">Loading calculator&hellip;</div></div>
        </aside>
        <div class="qscroll" id="qscroll"></div>
      </div>
      <footer class="tfoot">
        <div class="fname">${esc(state.name || "Student")}</div>
        <button class="qnavbtn" id="navBtn"></button>
        <div class="fbtns"><button class="btn primary" id="backBtn">Back</button><button class="btn primary" id="nextBtn">Next</button></div>
      </footer>
    </div>`;
    $("#dirBtn").onclick = showDirections;
    $("#refBtn").onclick = showReference;
    $("#moreBtn").onclick = showMore;
    $("#calcBtn").onclick = () => toggleCalc();
    $("#calcClose").onclick = () => toggleCalc(false);
    $("#calcWide").onclick = () => { calcWide = !calcWide; $("#calcPanel").classList.toggle("wide", calcWide); $("#calcWide").textContent = calcWide ? "Collapse" : "Expand"; if (desmosCalc) desmosCalc.resize(); };
    if (S.timed) $("#hideBtn").onclick = () => { timerHidden = !timerHidden; updateTimer(); };
    $("#navBtn").onclick = showNavigator;
    $("#backBtn").onclick = goBack;
    $("#nextBtn").onclick = goNext;
    startTick();
  }

  function renderTest() {
    if (!$("#test")) buildShell();
    $("#secTitle").textContent = sectionTitle();
    updateTimer();
    if (S.phase === "review") return renderReviewPage();
    const item = S.items[S.idx], q = byId[item.id];
    const total = S.kind === "full" ? S.items.length : S.target;
    $("#navBtn").innerHTML = `Question ${S.idx + 1} of ${total} &#9652;`;
    $("#backBtn").disabled = S.idx === 0;
    $("#backBtn").classList.toggle("hidden", false);
    const nb = $("#nextBtn");
    nb.textContent = S.kind === "practice" && S.feedback && !item.locked ? "Check Answer" : "Next";

    const calcAllowed = state.settings.calc !== "desmos-only" || q.desmos;
    $("#calcBtn").disabled = !calcAllowed;
    $("#calcBtn").title = calcAllowed ? "" : "Calculator is turned off for by-hand questions (Parent area setting)";
    if (!calcAllowed && calcOpen) toggleCalc(false);

    const showTags = S.kind === "practice" && item.locked;
    const head = `<div class="qhead"><span class="qnum">${S.idx + 1}</span>
      <button class="mark ${item.marked ? "on" : ""}" id="markBtn">${ICON.mark}${item.marked ? "Marked for Review" : "Mark for Review"}</button>
      <span class="sp"></span>${showTags ? calcTag(q) + diffTag(q.diff) : ""}
      ${q.type === "mc" ? `<button class="abc ${crossMode ? "on" : ""}" id="abcBtn" title="Cross out answer choices">ABC</button>` : ""}</div>`;
    let body;
    if (q.type === "mc") {
      const rows = item.order.map((oi, di) => {
        const orig = L[oi];
        const crossed = item.crossed.includes(orig);
        let cls = item.resp === orig ? " sel" : "";
        if (item.locked && S.feedback) cls = orig === q.answer ? " correct" : item.resp === orig ? " wrong" : "";
        if (crossed && !item.locked) cls += " crossed";
        return `<div class="crow"><button class="choice${cls}" data-o="${orig}" ${item.locked ? "disabled" : ""}><span class="letter">${L[di]}</span><span class="ctext">${q.choices[oi]}</span></button>
          ${crossMode && !item.locked ? `<button class="xout ${crossed ? "undo" : ""}" data-x="${orig}" aria-label="Cross out ${L[di]}">${crossed ? "Undo" : L[di]}</button>` : ""}</div>`;
      }).join("");
      body = `<div class="qpanes"><div class="qpane"><div class="qcol">${head}<div class="stem">${q.stem}</div><div class="choices">${rows}</div>${feedbackHTML(item, q)}</div></div></div>`;
    } else {
      body = `<div class="qpanes"><div class="qpane dirpane">${sprDirections()}</div>
        <div class="qpane"><div class="qcol">${head}<div class="stem">${q.stem}</div>
          <div class="sprbox"><input id="sprIn" inputmode="text" autocomplete="off" spellcheck="false" value="${esc(item.resp || "")}" ${item.locked ? "disabled" : ""} aria-label="Your answer">
          <div class="sprwarn" id="sprWarn"></div><div class="preview">Answer Preview: <span id="preview"></span></div></div>
          ${feedbackHTML(item, q)}</div></div></div>`;
    }
    const qs = $("#qscroll");
    qs.innerHTML = body;
    math(qs);
    qs.scrollTop = 0;

    $("#markBtn").onclick = () => { item.marked = !item.marked; save(); renderTest(); };
    if (q.type === "mc") {
      if ($("#abcBtn")) $("#abcBtn").onclick = () => { crossMode = !crossMode; renderTest(); };
      $$(".choice", qs).forEach((b) => (b.onclick = () => {
        if (item.locked) return;
        const o = b.dataset.o;
        item.crossed = item.crossed.filter((x) => x !== o);
        item.resp = item.resp === o ? null : o;
        save(); renderTest();
      }));
      $$(".xout", qs).forEach((b) => (b.onclick = () => {
        const o = b.dataset.x;
        if (item.crossed.includes(o)) item.crossed = item.crossed.filter((x) => x !== o);
        else { item.crossed.push(o); if (item.resp === o) item.resp = null; }
        save(); renderTest();
      }));
    } else {
      const inp = $("#sprIn");
      const upd = () => {
        const v = inp.value.trim();
        const okChars = Engine.sprInputAllowed(v);
        $("#sprWarn").textContent = v && !okChars ? "Use digits, one decimal point or fraction bar, and a leading minus sign. Max 5 characters (6 if negative)." : "";
        renderPreview(v);
      };
      inp.addEventListener("input", () => {
        if (!Engine.sprInputAllowed(inp.value.trim()) && inp.value.trim().length > (inp.value.trim().startsWith("-") ? 6 : 5)) {
          inp.value = inp.value.trim().slice(0, inp.value.trim().startsWith("-") ? 6 : 5);
        }
        item.resp = inp.value.trim() || null;
        save(); upd();
      });
      upd();
      if (!item.locked) inp.focus();
    }
  }

  function sprDirections() {
    return `<h3 style="margin-top:0">Student-produced response directions</h3>
      <ul>
        <li>If you find <b>more than one correct answer</b>, enter only one answer.</li>
        <li>You can enter up to 5 characters for a <b>positive</b> answer and up to 6 characters (including the negative sign) for a <b>negative</b> answer.</li>
        <li>If your answer is a <b>fraction</b> that doesn't fit in the space, enter the decimal equivalent.</li>
        <li>If your answer is a <b>decimal</b> that doesn't fit, enter it by truncating or rounding at the fourth digit.</li>
        <li>If your answer is a <b>mixed number</b> (such as 3&frac12;), enter it as an improper fraction (7/2) or its decimal equivalent (3.5).</li>
        <li>Don't enter <b>symbols</b> such as a percent sign, comma, or dollar sign.</li>
      </ul>
      <table class="data"><tr><th>Answer</th><th>Acceptable ways to enter</th><th>Not acceptable</th></tr>
        <tr><td>3.5</td><td>3.5, 3.50, 7/2</td><td>31/2, 3 1/2</td></tr>
        <tr><td>2/3</td><td>2/3, .6666, .6667, 0.666, 0.667</td><td>0.66, .66, 0.67, .67</td></tr>
        <tr><td>&minus;1/3</td><td>&minus;1/3, &minus;.3333, &minus;0.333</td><td>&minus;.33, &minus;0.33</td></tr></table>`;
  }

  function renderPreview(v) {
    const el = $("#preview");
    if (!el) return;
    if (!v) { el.textContent = ""; return; }
    let tex = esc(v);
    const m = v.match(/^(-?)(\d*)\/(\d*)$/);
    if (m) tex = `${m[1]}\\dfrac{${m[2] || "\\square"}}{${m[3] || "\\square"}}`;
    try { katex.render(tex, el, { throwOnError: false }); } catch (e) { el.textContent = v; }
  }

  function feedbackHTML(item, q) {
    if (!(S.kind === "practice" && S.feedback && item.locked)) return "";
    const ok = item.correct;
    const yours = item.resp == null ? "No answer" : q.type === "mc" ? `You chose ${displayLetter(item, item.resp)}.` : `You entered ${esc(item.resp)}.`;
    const key = q.type === "mc" ? `Correct answer: ${displayLetter(item, q.answer)}` : `Correct answer: ${esc(q.answer)}`;
    return `<div class="feedback ${ok ? "ok" : "no"}"><h4>${ok ? "Correct!" : "Not quite."} <span class="muted small" style="font-weight:500">${yours} ${key}. Time: ${fmtTime(item.secs)}</span></h4>
      <div class="explain">${q.explain}</div>
      ${q.tip ? `<div class="tipbox"><b>Desmos strategy:</b> ${q.tip}</div>` : ""}</div>`;
  }

  // ------------------------------------------------------------------ navigation
  function goBack() {
    if (S.phase === "review") { S.phase = "q"; S.idx = S.items.length - 1; save(); return renderTest(); }
    if (S.idx > 0) { S.idx--; save(); renderTest(); }
  }

  function goNext() {
    if (S.phase === "review") return confirmSubmitModule();
    const item = S.items[S.idx];
    if (S.kind === "practice") {
      if (!item.locked) {
        if (item.resp == null && !confirm("You haven't answered this question. Skip it? It will count as incorrect.")) return;
        lockAndRecord(item);
        if (S.feedback) { save(); return renderTest(); }
      }
      return practiceAdvance();
    }
    if (S.idx < S.items.length - 1) { S.idx++; save(); return renderTest(); }
    S.phase = "review"; save(); renderTest();
  }

  function lockAndRecord(item) {
    const q = byId[item.id];
    item.locked = true;
    item.correct = Engine.isCorrect(q, item.resp);
    Engine.recordAnswer(state, q, item.correct);
  }

  function practiceAdvance() {
    if (S.idx < S.items.length - 1) { S.idx++; save(); return renderTest(); }
    if (S.items.length >= S.target) return finishSession();
    const used = new Set(S.used);
    const q = Engine.nextPractice(state, QUESTIONS, S.opts, used);
    if (!q) return finishSession();
    S.used.push(q.id);
    S.items.push(makeItem(q));
    S.idx++;
    save(); renderTest();
  }

  function renderReviewPage() {
    $("#navBtn").innerHTML = `Check Your Work &#9652;`;
    $("#backBtn").disabled = false;
    $("#nextBtn").textContent = "Next";
    const qs = $("#qscroll");
    qs.innerHTML = `<div class="reviewpage"><h2>Check Your Work</h2>
      <p>On test day, you won't be able to move on to the next module until time expires.<br>For these questions, you can click <b>Next</b> when you're ready to move on.</p>
      <div class="pop"><h3>${esc(sectionTitle())} Questions</h3>${navLegend()}${navGrid(false)}</div></div>`;
    bindGrid(qs);
  }

  function navLegend() {
    return `<div class="legend"><span>&#9660; Current</span><span><span class="gbox" style="width:18px;height:18px"></span> Unanswered</span><span><span class="gbox flag" style="width:18px;height:18px;border-style:solid"></span> For Review</span></div>`;
  }
  function navGrid(withCurrent) {
    return `<div class="grid">${S.items.map((it, i) => {
      let cls = it.resp != null ? "ans" : "";
      if (S.kind === "practice" && S.feedback && it.locked) cls = it.correct ? "ok" : "no";
      return `<button class="gbox ${cls} ${it.marked ? "flag" : ""} ${withCurrent && i === S.idx ? "cur" : ""}" data-i="${i}">${i + 1}</button>`;
    }).join("")}</div>`;
  }
  function bindGrid(el) {
    $$(".gbox[data-i]", el).forEach((b) => (b.onclick = () => { closeOverlay(); S.phase = "q"; S.idx = +b.dataset.i; save(); renderTest(); }));
  }

  function showNavigator() {
    if (S.phase === "review") return;
    const ov = overlay(`<div class="pop"><button class="close" aria-label="Close">&times;</button><h3>${esc(sectionTitle())} Questions</h3>${navLegend()}${navGrid(true)}
      ${S.kind === "full" ? `<div class="center"><button class="btn" id="toReview">Go to Review Page</button></div>` : ""}</div>`, true);
    bindGrid(ov);
    if ($("#toReview", ov)) $("#toReview", ov).onclick = () => { closeOverlay(); S.phase = "review"; save(); renderTest(); };
  }

  function overlay(html, clear) {
    closeOverlay();
    const ov = document.createElement("div");
    ov.className = "overlay" + (clear ? " clear" : "");
    ov.id = "overlay";
    ov.innerHTML = html;
    ov.addEventListener("click", (e) => { if (e.target === ov || e.target.classList.contains("close")) closeOverlay(); });
    document.body.appendChild(ov);
    math(ov);
    return ov;
  }
  function closeOverlay() { const o = $("#overlay"); if (o) o.remove(); }

  function showDirections() {
    overlay(`<div class="pop"><button class="close" aria-label="Close">&times;</button><h3>Directions</h3><div class="modal-body">
      <p>The questions in this section address a number of important math skills.</p>
      <p>Use of a calculator is permitted for all questions. A reference sheet, calculator, and these directions can be accessed throughout the test.</p>
      <p>Unless otherwise indicated:</p>
      <ul><li>All variables and expressions represent real numbers.</li>
      <li>Figures provided are drawn to scale.</li>
      <li>All figures lie in a plane.</li>
      <li>The domain of a given function \\(f\\) is the set of all real numbers \\(x\\) for which \\(f(x)\\) is a real number.</li></ul>
      <p>For <b>multiple-choice questions</b>, solve each problem and choose the correct answer from the choices provided. Each multiple-choice question has a single correct answer.</p>
      <p>For <b>student-produced response questions</b>, solve each problem and enter your answer as described in the directions shown next to the question.</p>
      ${S && S.kind === "practice" ? `<p class="note">Practice mode: questions are picked one at a time based on how you're doing, so you can go back to review earlier questions but can't change locked answers.</p>` : ""}
      </div><div class="center"><button class="btn primary" onclick="document.getElementById('overlay').remove()">Close</button></div></div>`);
  }

  function showReference() {
    overlay(`<div class="pop"><button class="close" aria-label="Close">&times;</button><h3>Reference</h3><div class="modal-body">
      <div class="refgrid">
        <div class="refcard"><b>Circle</b>\\(A=\\pi r^2\\)<br>\\(C=2\\pi r\\)</div>
        <div class="refcard"><b>Rectangle</b>\\(A=\\ell w\\)</div>
        <div class="refcard"><b>Triangle</b>\\(A=\\tfrac12 bh\\)</div>
        <div class="refcard"><b>Pythagorean theorem</b>\\(c^2=a^2+b^2\\)</div>
        <div class="refcard"><b>Special right triangles</b>\\(30^\\circ\\!\\text{-}60^\\circ\\!\\text{-}90^\\circ\\): \\(x,\\ x\\sqrt3,\\ 2x\\)<br>\\(45^\\circ\\!\\text{-}45^\\circ\\!\\text{-}90^\\circ\\): \\(s,\\ s,\\ s\\sqrt2\\)</div>
        <div class="refcard"><b>Rectangular prism</b>\\(V=\\ell wh\\)</div>
        <div class="refcard"><b>Cylinder</b>\\(V=\\pi r^2h\\)</div>
        <div class="refcard"><b>Sphere</b>\\(V=\\tfrac43\\pi r^3\\)</div>
        <div class="refcard"><b>Cone</b>\\(V=\\tfrac13\\pi r^2h\\)</div>
        <div class="refcard"><b>Pyramid</b>\\(V=\\tfrac13\\ell wh\\)</div>
      </div>
      <p>The number of degrees of arc in a circle is 360.<br>The number of radians of arc in a circle is \\(2\\pi\\).<br>The sum of the measures in degrees of the angles of a triangle is 180.</p>
      </div></div>`);
  }

  function showMore() {
    const ov = overlay(`<div class="pop" style="max-width:420px"><button class="close" aria-label="Close">&times;</button><h3>More</h3>
      <div class="modal-body" style="display:flex;flex-direction:column;gap:10px;align-items:stretch">
        <button class="btn" id="saveExit">Save and exit to home</button>
        ${S.kind === "practice" ? `<button class="btn" id="endNow">End practice now and see results</button>` : ""}
        <p class="small muted">The timer pauses while you're away and resumes when you come back. (On the real test, the timer never pauses.)</p>
      </div></div>`);
    $("#saveExit", ov).onclick = () => { closeOverlay(); save(); home(); };
    if ($("#endNow", ov)) $("#endNow", ov).onclick = () => { closeOverlay(); finishSession(); };
  }

  // ------------------------------------------------------------------ timer
  function startTick() {
    stopTick();
    tickTimer = setInterval(tick, 1000);
  }
  function stopTick() { if (tickTimer) clearInterval(tickTimer); tickTimer = null; }
  function tick() {
    if (!S || !$("#test")) return stopTick();
    if (S.phase === "q") { const it = S.items[S.idx]; if (!it.locked) it.secs++; }
    if (S.timed) {
      S.timeLeft--;
      if (S.timeLeft <= 0) { S.timeLeft = 0; updateTimer(); return timeUp(); }
    }
    updateTimer();
    if (++tickCount % 5 === 0) save();
  }
  function updateTimer() {
    const el = $("#timer");
    if (!el || !S) return;
    if (!S.timed) { el.innerHTML = `<span class="muted small">Untimed</span>`; return; }
    const low = S.timeLeft <= 300;
    if (low) timerHidden = false;      // like the real test: the clock reappears for the last 5 minutes
    el.classList.toggle("low", low);
    el.innerHTML = timerHidden ? `<span class="timer-icon">&#9201;</span>` : fmtTime(S.timeLeft);
    const hb = $("#hideBtn");
    if (hb) { hb.textContent = timerHidden ? "Show" : "Hide"; hb.disabled = low; }
  }
  function timeUp() {
    stopTick();
    if (S.kind === "full") {
      alert(`Time's up for Module ${S.moduleNo}. Your answers have been submitted.`);
      submitModule();
    } else {
      const it = S.items[S.idx];
      if (!it.locked) lockAndRecord(it);
      alert("Time's up for this practice set.");
      finishSession();
    }
  }

  // ------------------------------------------------------------------ calculator
  function loadDesmos() {
    if (window.Desmos) return Promise.resolve();
    if (desmosLoading) return desmosLoading;
    desmosLoading = new Promise((res, rej) => {
      const s = document.createElement("script");
      s.src = DESMOS_URL;
      s.onload = res;
      s.onerror = () => { desmosLoading = null; rej(new Error("load failed")); };
      document.head.appendChild(s);
    });
    return desmosLoading;
  }
  function toggleCalc(force) {
    calcOpen = force == null ? !calcOpen : force;
    const panel = $("#calcPanel");
    if (!panel) return;
    panel.classList.toggle("hidden", !calcOpen);
    $("#calcBtn").classList.toggle("on", calcOpen);
    if (!calcOpen) return;
    if (desmosCalc) { desmosCalc.resize(); return; }
    loadDesmos().then(() => {
      const el = $("#desmos");
      if (!el || desmosCalc) return;
      el.innerHTML = "";
      desmosCalc = Desmos.GraphingCalculator(el, { keypad: true, expressions: true, settingsMenu: true, zoomButtons: true, border: false });
    }).catch(() => {
      const el = $("#desmos");
      if (el) el.innerHTML = `<div class="calcmsg">The Desmos calculator couldn't load (it needs an internet connection).<br><br>
        You can open it in a new tab instead: <a href="https://www.desmos.com/calculator" target="_blank" rel="noopener">desmos.com/calculator</a></div>`;
    });
  }
  function destroyCalc() {
    if (desmosCalc) { try { desmosCalc.destroy(); } catch (e) { /* ignore */ } }
    desmosCalc = null; calcOpen = false; calcWide = false;
  }

  // ================================================================== MODULE FLOW
  function confirmSubmitModule() {
    const blank = S.items.filter((i) => i.resp == null).length;
    const msg = blank ? `You have ${blank} unanswered question${blank === 1 ? "" : "s"}. Submit Module ${S.moduleNo} anyway?` : `Submit Module ${S.moduleNo}? You won't be able to return to it.`;
    if (confirm(msg)) submitModule();
  }

  function submitModule() {
    for (const it of S.items) if (!it.locked) lockAndRecord(it);
    S.done.push({ label: `Module ${S.moduleNo}`, route: S.route, items: S.items });
    if (S.moduleNo === 1) {
      const used = new Set(S.used);
      S.route = Engine.route(S.items);
      const qs = Engine.buildModule(state, QUESTIONS, S.route, used);
      S.used = [...used];
      S.moduleNo = 2;
      S.items = qs.map(makeItem);
      S.idx = 0;
      S.phase = "between";
      S.timeLeft = Engine.MODULE_SEC;
      save();
      return betweenModules();
    }
    finishSession();
  }

  function betweenModules() {
    view(`<div class="between">
      <h1>Module 1 complete</h1>
      <p>Nice work. Module 2 has 22 questions and 35 minutes. On the real SAT, which version of Module 2 you get depends on how you did on Module 1. You'll find out which one you got on your score report.</p>
      <p class="muted">Take a moment to stretch. The timer starts when you click Begin.</p>
      <p><button class="btn primary" id="beginM2">Begin Module 2</button> <button class="btn" id="laterM2">Save and exit</button></p></div>`);
    $("#beginM2").onclick = () => { S.phase = "q"; save(); renderTest(); };
    $("#laterM2").onclick = () => { save(); home(); };
  }

  function finishSession() {
    stopTick();
    if (S.kind === "practice") {
      const it = S.items[S.idx];
      if (it && !it.locked && it.resp != null) lockAndRecord(it);
      S.done.push({ label: "Practice", items: S.items.filter((i) => i.locked) });
    }
    const rec = {
      id: S.id, kind: S.kind, title: S.title, date: Date.now(), route: S.route,
      modules: S.done.map((m) => ({ label: m.label, route: m.route, items: m.items.map((i) => ({ id: i.id, resp: i.resp, correct: !!i.correct, secs: i.secs, order: i.order })) })),
    };
    if (S.kind === "full") {
      rec.score = Engine.estimateScore(rec.modules.flatMap((m) => m.items.map((i) => ({ diff: byId[i.id].diff, correct: i.correct }))));
    }
    state.sessions.push(rec);
    if (state.sessions.length > 60) state.sessions.shift();
    S = null;
    save();
    results(rec);
  }

  // ================================================================== RESULTS
  function results(rec) {
    if (!rec) return home();
    const all = rec.modules.flatMap((m) => m.items);
    const correct = all.filter((i) => i.correct).length;
    const time = all.reduce((a, i) => a + i.secs, 0);
    const byDom = {};
    const split = { d: [0, 0], h: [0, 0] };
    for (const i of all) {
      const q = byId[i.id]; if (!q) continue;
      const d = (byDom[q.domain] = byDom[q.domain] || [0, 0]); d[0] += i.correct ? 1 : 0; d[1]++;
      const s = q.desmos ? split.d : split.h; s[0] += i.correct ? 1 : 0; s[1]++;
    }
    const domRows = Object.entries(byDom).map(([d, [c, n]]) => `<tr><td>${esc(DOMAINS[d])}</td>
      <td><div class="bar"><i class="${lvlClass(c / n)}" style="width:${pct(c, n)}%"></i></div></td><td>${c}/${n}</td></tr>`).join("");

    let header;
    if (rec.kind === "full" && rec.score) {
      const m1 = rec.modules[0], m2 = rec.modules[1];
      const c1 = m1.items.filter((i) => i.correct).length, c2 = m2 ? m2.items.filter((i) => i.correct).length : 0;
      header = `<div class="scorecard">
        <div><div class="muted small">Estimated math score</div><div class="bigscore">${rec.score.score}</div><div class="muted small">likely range ${rec.score.low}&ndash;${rec.score.high}</div></div>
        <div class="grow" style="flex:1;min-width:240px;line-height:1.7">
          Module 1: <b>${c1}/22</b><br>
          Module 2 (${rec.route === "m2hard" ? "<b>harder</b> version" : "standard version"}): <b>${c2}/${m2 ? m2.items.length : 22}</b><br>
          <span class="small muted">${rec.route === "m2hard" ? "You scored well enough on Module 1 to unlock the harder Module 2, which is required for the top score range." : `You needed ${Engine.ROUTE_THRESHOLD} correct on Module 1 for the harder Module 2. The standard Module 2 caps the score range, so Module 1 accuracy matters a lot.`}</span>
        </div></div>
        <p class="small muted">The estimate uses a statistical model of question difficulty. It's a rough guide, not an official College Board conversion.</p>`;
    } else {
      header = `<div class="scorecard"><div><div class="muted small">Correct</div><div class="bigscore">${correct}/${all.length}</div></div>
        <div style="line-height:1.7">Time used: <b>${fmtTime(time)}</b> (avg ${fmtTime(all.length ? time / all.length : 0)} per question; SAT pace is 1:35)<br>
        Current level: <b>${level(state.theta)}</b> on the score scale</div></div>`;
    }

    view(`<div class="page">
      <div class="hero"><div><h1>${esc(rec.title)}: Results</h1><p>${new Date(rec.date).toLocaleString()}</p></div>
        <div><button class="btn primary" id="homeBtn">Back to home</button></div></div>
      ${header}
      <div class="cards" style="margin-bottom:10px">
        <div class="card"><h2>By domain</h2><table class="skills"><tbody>${domRows}</tbody></table></div>
        <div class="card"><h2>Desmos vs. by hand</h2>
          <p>Desmos-friendly questions: <b>${split.d[0]}/${split.d[1]}</b><br>By-hand questions: <b>${split.h[0]}/${split.h[1]}</b></p>
          <p class="small">${split.d[1] && split.d[0] / split.d[1] < 0.7 ? "Tip: open each Desmos question's strategy below. Graphing would have solved several of these in under a minute." : "Desmos questions are marked with a green tag below. Review the strategy notes even when you got them right; they're often faster than algebra."}</p></div>
      </div>
      <h3 class="section-title">Question review</h3>
      <p class="small muted">Click a question to see the full solution.</p>
      ${rec.modules.map((m) => `${rec.modules.length > 1 ? `<h4>${esc(m.label)}${m.route ? (m.route === "m2hard" ? " (harder)" : " (standard)") : ""}</h4>` : ""}
        <div class="qlist">${m.items.map((i, n) => reviewItem(i, n)).join("")}</div>`).join("")}
    </div>`);
    $("#homeBtn").onclick = home;
  }

  function reviewItem(i, n) {
    const q = byId[i.id];
    if (!q) return "";
    const res = i.resp == null ? "skip" : i.correct ? "ok" : "no";
    const order = i.order || [0, 1, 2, 3];
    const it = { order };
    const yours = i.resp == null ? "&mdash;" : q.type === "mc" ? displayLetter(it, i.resp) : esc(i.resp);
    const key = q.type === "mc" ? displayLetter(it, q.answer) : esc(q.answer);
    const choices = q.type === "mc" ? `<div class="choices">${order.map((oi, di) => {
      const o = L[oi];
      const cls = o === q.answer ? " correct" : o === i.resp ? " wrong" : "";
      return `<div class="crow"><div class="choice${cls}"><span class="letter">${L[di]}</span><span class="ctext">${q.choices[oi]}</span></div></div>`;
    }).join("")}</div>` : "";
    return `<details class="qitem"><summary><span class="muted">${n + 1}</span><span class="res ${res}">${res === "ok" ? "&#10003;" : res === "no" ? "&#10007;" : "&ndash;"}</span>
      <span class="meta">${esc(q.skill)} ${calcTag(q)} ${diffTag(q.diff)}</span><span class="muted small">${fmtTime(i.secs)}</span></summary>
      <div class="body"><div class="stem">${q.stem}</div>${choices}
        <div class="answers"><span>Your answer: <b>${yours}</b></span><span>Correct answer: <b>${key}</b></span><span>Time: ${fmtTime(i.secs)}</span><span class="muted">${q.id}</span></div>
        <div class="explain">${q.explain}</div>${q.tip ? `<div class="tipbox"><b>Desmos strategy:</b> ${q.tip}</div>` : ""}</div></details>`;
  }

  // ================================================================== PARENT AREA
  function parentGate() {
    if (state.settings.pin) {
      const p = prompt("Enter the parent PIN:");
      if (p !== state.settings.pin) { if (p != null) alert("Incorrect PIN."); return; }
    }
    parent("ALL");
  }

  function parent(filter) {
    const list = QUESTIONS.filter((q) => filter === "ALL" || q.domain === filter || (filter === "OFF" && state.disabled[q.id]));
    const cards = list.map((q) => {
      const it = state.items[q.id];
      const choices = q.type === "mc" ? `<ol type="A">${q.choices.map((c, k) => `<li class="${L[k] === q.answer ? "key" : ""}">${c}</li>`).join("")}</ol>` : "";
      return `<div class="bank-q ${state.disabled[q.id] ? "off" : ""}">
        <div class="head"><b>${q.id}</b> ${esc(q.skill)} ${calcTag(q)} ${diffTag(q.diff)}
          <span class="tag">${q.type === "mc" ? "Multiple choice" : "Student-produced"}</span>
          <span class="tag" title="How the answer key was checked">${q.verified === "computed" ? "&#10003; computer-verified" : "&#10003; reviewed (interpretation)"}</span>
          <span class="muted small">${it ? `${it.correct}/${it.n} correct` : "not seen yet"}</span>
          <span class="sp" style="flex:1"></span>
          <label class="small"><input type="checkbox" data-dis="${q.id}" ${state.disabled[q.id] ? "checked" : ""}> Remove from practice</label></div>
        <div class="stem">${q.stem}</div>${choices}
        <p><b>Answer: ${esc(q.answer)}</b></p><div class="explain">${q.explain}</div>${q.tip ? `<div class="tipbox"><b>Desmos strategy:</b> ${q.tip}</div>` : ""}</div>`;
    }).join("");
    const nDis = Object.keys(state.disabled).filter((k) => state.disabled[k]).length;
    view(`<div class="page">
      <div class="hero"><div><h1>Parent area</h1><p>Answer key, question review, and settings</p></div><div><button class="btn primary" id="homeBtn">Back to home</button></div></div>
      <div class="cards">
        <div class="card"><h2>Settings</h2>
          <div class="form">
            <label for="calcSet">Calculator</label><select id="calcSet">
              <option value="always" ${state.settings.calc === "always" ? "selected" : ""}>Available on every question (like the real SAT)</option>
              <option value="desmos-only" ${state.settings.calc === "desmos-only" ? "selected" : ""}>Only on Desmos questions (builds by-hand skills)</option></select>
            <label for="pinSet">Parent PIN</label><input id="pinSet" placeholder="optional" value="${esc(state.settings.pin)}" maxlength="12">
          </div>
          <p class="small">The PIN keeps the answer key one click away from casual browsing. It is not real security.</p>
          <div><button class="btn small" id="saveSet">Save settings</button></div></div>
        <div class="card"><h2>Progress data</h2>
          <p class="grow">Progress is saved in this browser only. Export it to back it up or move it to another computer.</p>
          <div style="display:flex;gap:8px;flex-wrap:wrap"><button class="btn small" id="expBtn">Export</button>
            <label class="btn small">Import<input type="file" id="impIn" accept="application/json" class="hidden"></label>
            <button class="btn small warn" id="resetBtn">Reset all progress</button></div></div>
      </div>
      <h3 class="section-title">Question bank (${QUESTIONS.length} questions${nDis ? `, ${nDis} removed` : ""})</h3>
      <p class="small muted">Every answer here passed an automated check that re-solved the problem independently. If you find a question you don't like, check &ldquo;Remove from practice&rdquo; and it will never be served.</p>
      <div class="toolbar">${["ALL", ...Object.keys(DOMAINS), "OFF"].map((k) => `<button class="btn small ${k === filter ? "primary" : ""}" data-f="${k}">${k === "ALL" ? "All" : k === "OFF" ? "Removed" : DOMAINS[k]}</button>`).join("")}</div>
      ${cards || '<p class="muted">None.</p>'}
    </div>`);
    $("#homeBtn").onclick = home;
    $$("[data-f]").forEach((b) => (b.onclick = () => parent(b.dataset.f)));
    $$("[data-dis]").forEach((c) => (c.onchange = () => { state.disabled[c.dataset.dis] = c.checked; if (!c.checked) delete state.disabled[c.dataset.dis]; save(); c.closest(".bank-q").classList.toggle("off", c.checked); }));
    $("#saveSet").onclick = () => { state.settings.calc = $("#calcSet").value; state.settings.pin = $("#pinSet").value.trim(); save(); alert("Settings saved."); };
    $("#expBtn").onclick = () => {
      const blob = new Blob([JSON.stringify(state, null, 1)], { type: "application/json" });
      const a = document.createElement("a"); a.href = URL.createObjectURL(blob); a.download = `sat-math-progress-${new Date().toISOString().slice(0, 10)}.json`; a.click();
    };
    $("#impIn").onchange = (e) => {
      const f = e.target.files[0]; if (!f) return;
      f.text().then((t) => {
        try { const s = JSON.parse(t); if (s.version !== 1) throw new Error(); state = Object.assign(Engine.defaultState(), s); save(); alert("Progress imported."); home(); }
        catch (err) { alert("That file isn't a valid progress export."); }
      });
    };
    $("#resetBtn").onclick = () => {
      if (confirm("Erase all progress, history, and settings on this computer? This can't be undone.")) { const pin = state.settings.pin; state = Engine.defaultState(); state.settings.pin = pin; S = null; save(); home(); }
    };
  }

  // ------------------------------------------------------------------ boot
  window.addEventListener("beforeunload", () => { if (S) save(); });
  window.addEventListener("resize", () => { if (desmosCalc) desmosCalc.resize(); });
  window.SATApp = { home, state: () => state };
  home();
})();
