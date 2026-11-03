/* Core logic: answer grading, the student model, adaptive question selection, and
 * score estimation. No DOM access here, so it can be unit-tested in Node. */
(function (root) {
  "use strict";

  // Item difficulty on a logit scale. The scale is anchored so that a student whose
  // ability theta equals b has a 50% chance on that item, and the SAT-like score is
  // roughly 500 + 100*theta. Medium is about a 550 item, hard 650, very hard 730.
  const B = { 1: 0.5, 2: 1.5, 3: 2.3 };
  const DIFF_NAME = { 1: "Medium", 2: "Hard", 3: "Very hard" };
  let PACE_SEC = 95;              // 35 min / 22 questions, about the real pace
  let SPEED_PACE_SEC = 80;        // training pace: builds a time buffer for the hardest questions
  // Time a strong student should need per question, by difficulty. Correct answers that
  // take more than SLOW_FACTOR times this count as "slow" (only partly mastered).
  const TARGET_SEC = { 1: 60, 2: 90, 3: 120 };
  const SLOW_FACTOR = 1.3;
  let DEFAULT_BASELINE = 740;     // most recent official SAT Math score (editable in the Parent area)
  let MODULE_SEC = 35 * 60;
  let MODULE_LEN = 22;
  // Per 22-question module. College Board: Algebra 13-15, Advanced Math 13-15, PSDA 5-7,
  // Geometry & Trig 5-7 of the 40 scored questions (+4 unscored pretest) -> 16/16/6/6 per test.
  const BLUEPRINT = { ALG: 8, ADV: 8, PSD: 3, GEO: 3 };
  let SPR_SHARE = 0.25;           // College Board: ~75% multiple choice, ~25% student-produced response
  // How questions are ordered within a module. Math: easiest to hardest. Reading & Writing:
  // by domain (in blueprint order), similar skills grouped, easiest to hardest within each.
  let ORDER = "difficulty";
  let SKILL_ORDER = [];
  let UNGROUPED_DOMAINS = [];     // domains sorted purely by difficulty regardless of skill
  const DIFF_MIX = {
    m1: { 1: 6, 2: 10, 3: 6 },
    m2hard: { 1: 2, 2: 9, 3: 11 },
    m2std: { 1: 9, 2: 10, 3: 3 },
    top: { 1: 0, 2: 8, 3: 14 },   // for students already scoring 700+: hard and very hard only
  };
  const ROUTE_THRESHOLD = 14;     // correct answers in module 1 (of 22) to reach the harder module 2
  const DAY = 86400000;

  const sigmoid = (z) => 1 / (1 + Math.exp(-z));

  // ---------------------------------------------------------------- grading
  function gcd(a, b) { a = Math.abs(a); b = Math.abs(b); while (b) [a, b] = [b, a % b]; return a; }

  /** Parse "41/3", "-2.5", ".75" into {n, d} (exact rational), or null. */
  function parseRational(str) {
    const s = String(str).trim();
    let m;
    if ((m = s.match(/^(-?)(\d+)\/(\d+)$/))) {
      const n = parseInt(m[2], 10) * (m[1] ? -1 : 1), d = parseInt(m[3], 10);
      if (d === 0) return null;
      const g = gcd(n, d) || 1;
      return { n: n / g, d: d / g };
    }
    if ((m = s.match(/^(-?)(\d*)\.?(\d*)$/)) && (m[2] + m[3]).length > 0) {
      const decs = m[3].length;
      const d = Math.pow(10, decs);
      const n = parseInt((m[2] || "0") + m[3], 10) * (m[1] ? -1 : 1);
      const g = gcd(n, d) || 1;
      return { n: n / g, d: d / g };
    }
    return null;
  }

  /** Validate characters/length the way the SAT answer box does. */
  function sprInputAllowed(str) {
    if (!/^-?[0-9./]*$/.test(str)) return false;
    const max = str.startsWith("-") ? 6 : 5;
    if (str.length > max) return false;
    if ((str.match(/\./g) || []).length > 1 || (str.match(/\//g) || []).length > 1) return false;
    if (str.includes(".") && str.includes("/")) return false;
    return true;
  }

  /**
   * SAT rules for student-produced responses: any exact equivalent is correct
   * (fraction or decimal). For a non-terminating value, a decimal is correct if it
   * fills the whole answer box and equals the value either truncated or rounded.
   */
  function gradeSPR(input, answer) {
    const s = String(input || "").trim();
    if (!s || !sprInputAllowed(s)) return false;
    const key = parseRational(answer), v = parseRational(s);
    if (!key || !v) return false;
    if (v.n * key.d === key.n * v.d) return true;
    if (!s.includes(".")) return false;
    const max = s.startsWith("-") ? 6 : 5;
    if (s.length < max) return false;                 // must use all available space
    const decs = s.split(".")[1].length;
    const exact = key.n / key.d;
    const scaled = Math.abs(exact) * Math.pow(10, decs);
    if ((v.n < 0) !== (exact < 0)) return false;
    const entered = Math.round(Math.abs(v.n / v.d) * Math.pow(10, decs));
    return entered === Math.floor(scaled + 1e-9) || entered === Math.round(scaled);
  }

  function isCorrect(q, response) {
    if (response == null || response === "") return false;
    return q.type === "mc" ? response === q.answer : gradeSPR(response, q.answer);
  }

  // ---------------------------------------------------------------- student model
  const scoreToTheta = (score) => (score - 500) / 100;
  const thetaToScore = (th) => Math.max(200, Math.min(800, Math.round((500 + 100 * th) / 10) * 10));

  function defaultState() {
    return {
      version: 1,
      name: "",
      settings: { calc: "always", pin: "", baseline: DEFAULT_BASELINE },
      theta: scoreToTheta(DEFAULT_BASELINE),   // overall ability on the score scale
      skills: {},           // skill -> {theta, n, correct}
      items: {},            // question id -> {n, correct, last, lastCorrect, lastSlow, lastSecs, lastCalc}
      sessions: [],
      disabled: {},         // question id -> true (parent removed it)
      active: null,         // in-progress session snapshot
    };
  }

  function skillRec(state, skill) {
    return state.skills[skill] || (state.skills[skill] = { theta: state.theta, n: 0, correct: 0 });
  }

  /** Set the starting level from an official score. Only moves the estimate while there is little data. */
  function setBaseline(state, score) {
    state.settings.baseline = score;
    if ((state.n || 0) < 20) {
      state.theta = scoreToTheta(score);
      for (const sk of Object.values(state.skills)) if (sk.n < 3) sk.theta = state.theta;
    }
  }

  const isSlow = (q, secs) => secs != null && secs > TARGET_SEC[q.diff] * SLOW_FACTOR;

  /**
   * Elo-style update after one answer. Unanswered counts as wrong. A correct answer that
   * took too long earns only partial credit (0.6), and so does one where the Desmos hint
   * was used (0.5): on test day both cost points through lost time.
   * extra = {secs, calc, hint}
   */
  function recordAnswer(state, q, correct, now, extra) {
    extra = extra || {};
    const slow = !!correct && isSlow(q, extra.secs);
    let y = correct ? (slow ? 0.6 : 1) : 0;
    if (extra.hint) y = Math.min(y, 0.5);
    const b = B[q.diff];
    const sk = skillRec(state, q.skill);
    const kSkill = Math.max(0.25, 0.9 / Math.sqrt(1 + sk.n / 4));
    sk.theta += kSkill * (y - sigmoid(sk.theta - b));
    sk.n += 1; sk.correct += correct ? 1 : 0;
    state.n = (state.n || 0) + 1;
    const kGlobal = Math.max(0.15, 0.5 / Math.sqrt(1 + state.n / 6));
    state.theta += kGlobal * (y - sigmoid(state.theta - b));
    const it = state.items[q.id] || (state.items[q.id] = { n: 0, correct: 0, last: 0, lastCorrect: false });
    it.n += 1; it.correct += correct ? 1 : 0; it.last = now || Date.now(); it.lastCorrect = !!correct;
    it.lastSlow = slow; it.lastSecs = extra.secs; it.lastCalc = !!extra.calc; it.lastHint = !!extra.hint;
    return { slow, credit: y };
  }

  /** A question is a trouble spot if the last attempt was wrong, slow, or needed the hint. */
  const isTrouble = (it) => !!it && (!it.lastCorrect || !!it.lastSlow || !!it.lastHint);
  function troubleIds(state, questions) {
    return questions.filter((q) => !state.disabled[q.id] && isTrouble(state.items[q.id])).map((q) => q.id);
  }

  /** Difficulty mix for a timed set, based on the current level. */
  function levelMix(state) {
    return state.theta >= 2.0 ? "top" : state.theta >= 1.2 ? "m2hard" : "m1";
  }

  /** Probability of answering a typical Hard question in this skill correctly. */
  function mastery(state, skill) {
    const sk = state.skills[skill];
    return sigmoid((sk ? sk.theta : state.theta) - B[2]);
  }

  // ---------------------------------------------------------------- selection
  function rand(rng) { return rng ? rng() : Math.random(); }

  /** Desirability of serving question q now (higher is better). */
  function priority(state, q, now, rng) {
    const it = state.items[q.id];
    let p = 2.0 * (1 - mastery(state, q.skill));     // weak skills first
    if (!it) p += 3;                                  // brand new
    else if (isTrouble(it) && now - it.last > 2 * DAY) p += it.lastCorrect ? 2.5 : 3;   // missed or slow before: spaced retry
    else if (isTrouble(it)) p -= 1;                   // just seen: wait a bit
    else p -= 3 + Math.min(it.correct, 3);            // answered correctly and quickly: rarely repeat
    if (it) p -= Math.max(0, 1.5 - (now - it.last) / (7 * DAY));     // seen in the past week
    return p + 0.6 * rand(rng);
  }

  function available(state, questions, exclude) {
    return questions.filter((q) => !state.disabled[q.id] && !exclude.has(q.id));
  }

  function pickBest(cands, state, now, rng) {
    let best = null, bestP = -Infinity;
    for (const q of cands) {
      const p = priority(state, q, now, rng);
      if (p > bestP) { bestP = p; best = q; }
    }
    return best;
  }

  /** Split n slots across difficulties in proportion to mix. */
  function allocate(n, mix) {
    const total = mix[1] + mix[2] + mix[3];
    const raw = [1, 2, 3].map((d) => (n * mix[d]) / total);
    const out = raw.map(Math.floor);
    let left = n - out.reduce((a, b) => a + b, 0);
    const order = [0, 1, 2].sort((i, j) => (raw[j] - out[j]) - (raw[i] - out[i]));
    for (let i = 0; left > 0; i = (i + 1) % 3, left--) out[order[i]]++;
    return { 1: out[0], 2: out[1], 3: out[2] };
  }

  /** Scale the 22-question domain blueprint to n questions (largest-remainder rounding). */
  function scaleBlueprint(n, domains) {
    const doms = domains || Object.keys(BLUEPRINT);
    const tot = doms.reduce((a, d) => a + BLUEPRINT[d], 0);
    const raw = doms.map((d) => (n * BLUEPRINT[d]) / tot);
    const out = raw.map(Math.floor);
    let left = n - out.reduce((a, b) => a + b, 0);
    const order = doms.map((_, i) => i).sort((i, j) => (raw[j] - out[j]) - (raw[i] - out[i]) || i - j);
    for (let i = 0; left > 0; i = (i + 1) % doms.length, left--) out[order[i]]++;
    return Object.fromEntries(doms.map((d, i) => [d, out[i]]));
  }

  /**
   * Assemble a module or timed set: domain blueprint scaled to n questions, a difficulty
   * mix, and within that, the questions the student most needs (weak skills, trouble spots,
   * unseen questions). opts.filter optionally restricts the pool (e.g. Desmos-only).
   */
  function buildModule(state, questions, mixKey, used, rng, now, n, opts) {
    now = now || Date.now();
    n = n || MODULE_LEN;
    opts = opts || {};
    const mix = DIFF_MIX[mixKey];
    const base = opts.filter ? questions.filter(opts.filter) : questions;
    const domains = opts.domain && opts.domain !== "ALL" ? [opts.domain] : null;
    const picked = [];
    // Student-produced responses: aim for SPR_SHARE of the set, spread across domains.
    let sprLeft = SPR_SHARE == null ? null : Math.round(n * SPR_SHARE);
    let slotsLeft = n;
    // Which formats to try for the next slot. The SPR share is a soft preference (spread
    // evenly across the module) until the end of the module, where it becomes a hard limit.
    const typeOrder = () => {
      if (sprLeft == null) return [null];
      if (sprLeft >= slotsLeft) return ["spr"];
      if (sprLeft <= 0) return ["mc"];
      return rand(rng) < sprLeft / slotsLeft ? ["spr", "mc"] : ["mc", "spr"];
    };
    for (const [dom, count] of Object.entries(scaleBlueprint(n, domains))) {
      const want = allocate(count, mix);
      for (const d of [3, 2, 1]) {
        for (let i = 0; i < want[d]; i++) {
          const pool = available(state, base, used).filter((q) => q.domain === dom);
          // Difficulty comes first: try the target difficulty in either allowed format before
          // stepping to the nearest difficulty.
          const order = d === 2 ? [2, 3, 1] : d === 3 ? [3, 2, 1] : [1, 2, 3];
          const types = typeOrder();
          let q = null;
          for (const dd of order) {
            for (const t of types) {
              q = pickBest(pool.filter((x) => x.diff === dd && (t == null || x.type === t)), state, now, rng);
              if (q) break;
            }
            if (q) break;
          }
          if (!q) {   // a hard format limit couldn't be met in this domain: relax it
            for (const dd of order) { q = pickBest(pool.filter((x) => x.diff === dd), state, now, rng); if (q) break; }
          }
          if (!q) q = pickBest(available(state, base, used), state, now, rng);
          if (!q) break;
          picked.push(q); used.add(q.id);
          slotsLeft--; if (q.type === "spr" && sprLeft != null) sprLeft--;
        }
      }
    }
    return orderModule(picked, rng);
  }

  /** Order a module the way the real test does (see ORDER). Ties are shuffled. */
  function orderModule(qs, rng) {
    const doms = Object.keys(BLUEPRINT);
    const key = (q) => {
      if (ORDER !== "domain") return [q.diff];
      const skill = UNGROUPED_DOMAINS.includes(q.domain) ? 0 : Math.max(0, SKILL_ORDER.indexOf(q.skill));
      return [doms.indexOf(q.domain), skill, q.diff];
    };
    return qs.map((q) => [key(q), rand(rng), q]).sort((a, b) => {
      for (let i = 0; i < a[0].length; i++) if (a[0][i] !== b[0][i]) return a[0][i] - b[0][i];
      return a[1] - b[1];
    }).map((p) => p[2]);
  }

  function route(module1Responses) {
    const correct = module1Responses.filter((r) => r.correct).length;
    return correct >= ROUTE_THRESHOLD ? "m2hard" : "m2std";
  }

  /**
   * Adaptive practice: choose the next question one at a time, favoring weak skills at a
   * difficulty slightly above the student's current level in that skill.
   */
  function nextPractice(state, questions, opts, used, rng, now) {
    now = now || Date.now();
    let pool = available(state, questions, used);
    if (opts.domain && opts.domain !== "ALL") pool = pool.filter((q) => q.domain === opts.domain);
    if (opts.calc === "desmos") pool = pool.filter((q) => q.desmos);
    if (opts.calc === "hand") pool = pool.filter((q) => !q.desmos);
    if (opts.onlyIds) pool = pool.filter((q) => opts.onlyIds.includes(q.id));
    if (!pool.length) return null;

    // Score every candidate: weak skills first (inside priority), difficulty close to
    // slightly above the student's level in that skill, and avoid repeating the skill
    // that was just practiced.
    const ids = [...used];
    const last = ids.length ? questions.find((q) => q.id === ids[ids.length - 1]) : null;
    let best = null, bestP = -Infinity;
    for (const q of pool) {
      const sk = state.skills[q.skill];
      const target = (sk ? sk.theta : state.theta) + 0.4;
      let p = priority(state, q, now, rng) - 1.5 * Math.abs(B[q.diff] - target);
      if (last && last.skill === q.skill) p -= 0.8;
      if (p > bestP) { bestP = p; best = q; }
    }
    return best;
  }

  // ---------------------------------------------------------------- scoring
  /**
   * Estimate an SAT-style math score (200-800) from responses [{diff, correct}] using a
   * one-parameter (Rasch) model with a mild prior, so all-correct or all-wrong still
   * gives a finite estimate. This is an approximation, not an official conversion.
   */
  function estimateScore(responses) {
    if (!responses.length) return null;
    const mu = 1.0, sd = 1.5;
    let th = mu;
    for (let iter = 0; iter < 50; iter++) {
      let g = -(th - mu) / (sd * sd), h = -1 / (sd * sd);
      for (const r of responses) {
        const p = sigmoid(th - B[r.diff]);
        g += (r.correct ? 1 : 0) - p;
        h -= p * (1 - p);
      }
      const step = g / h;
      th -= step;
      if (Math.abs(step) < 1e-6) break;
    }
    let info = 1 / (sd * sd);
    for (const r of responses) { const p = sigmoid(th - B[r.diff]); info += p * (1 - p); }
    const se = 1 / Math.sqrt(info);
    const clamp = (v) => Math.max(200, Math.min(800, Math.round(v / 10) * 10));
    return { score: clamp(500 + 100 * th), low: clamp(500 + 100 * (th - se)), high: clamp(500 + 100 * (th + se)), theta: th };
  }

  /**
   * Switch subject-specific settings (used by the Reading & Writing page). Must be called
   * before any state is created. cfg: {pace, speedPace, target, blueprint, moduleLen,
   * moduleSec, baseline}
   */
  function configure(cfg) {
    if (cfg.pace) PACE_SEC = cfg.pace;
    if (cfg.speedPace) SPEED_PACE_SEC = cfg.speedPace;
    if (cfg.target) Object.assign(TARGET_SEC, cfg.target);
    if (cfg.blueprint) { for (const k of Object.keys(BLUEPRINT)) delete BLUEPRINT[k]; Object.assign(BLUEPRINT, cfg.blueprint); }
    if (cfg.moduleLen) MODULE_LEN = cfg.moduleLen;
    if (cfg.moduleSec) MODULE_SEC = cfg.moduleSec;
    if (cfg.baseline) DEFAULT_BASELINE = cfg.baseline;
    if ("sprShare" in cfg) SPR_SHARE = cfg.sprShare;
    if (cfg.order) ORDER = cfg.order;
    if (cfg.skillOrder) SKILL_ORDER = cfg.skillOrder;
    if (cfg.ungrouped) UNGROUPED_DOMAINS = cfg.ungrouped;
    Object.assign(api, { PACE_SEC, SPEED_PACE_SEC, MODULE_LEN, MODULE_SEC, DEFAULT_BASELINE });
  }

  const api = {
    configure,
    B, DIFF_NAME, PACE_SEC, SPEED_PACE_SEC, TARGET_SEC, SLOW_FACTOR, MODULE_SEC, MODULE_LEN, BLUEPRINT, ROUTE_THRESHOLD, DEFAULT_BASELINE,
    parseRational, sprInputAllowed, gradeSPR, isCorrect, isSlow, isTrouble, troubleIds,
    defaultState, setBaseline, scoreToTheta, thetaToScore, recordAnswer, mastery, levelMix, scaleBlueprint,
    buildModule, orderModule, route, nextPractice, estimateScore,
  };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.Engine = api;
})(typeof window !== "undefined" ? window : globalThis);
