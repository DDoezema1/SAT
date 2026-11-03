# SAT Math Practice

A practice app for the math section of the digital SAT. It's tuned for a student who already scores in the 700s, so the goal is the last 50–60 points. In practice that means three things: more accuracy on the hardest questions, faster pacing, and reaching for Desmos whenever it's the fastest route.

## What's in it

**Timed Set (the everyday mode).** A short, test-like block: 11 questions (half a module, 17:25) or 22 (one module, 35:00). It's built at her level, so a 740 student gets only Hard and Very hard questions. The questions are drawn from her trouble spots and weak skills. Pace is either SAT pace (1:35 per question) or **speed training** (1:20 per question, which builds a time buffer for test day). It can focus on one domain or on Desmos questions only.

**Pacing coach** (optional, in any timed mode):

- under the timer, a live **ahead / on pace / behind** indicator
- on each question, a **stopwatch** that turns amber at the target time and red when it's time to guess, mark the question, and move on

**Desmos Speed Drill.** 8 Desmos-route questions. The calculator opens automatically, each question has a target time, and a "Desmos hint" button is available if she's stuck (it counts as half credit). The Desmos solution appears after each answer.

**Trouble Spots.** Re-serves every question she **missed, answered slowly, or needed a hint on**. A correct answer that took too long counts as a trouble spot, because on test day time costs points.

**Adaptive Practice.** Questions are chosen one at a time based on accuracy *and speed*, with feedback after each question or only at the end.

**Full Math Section.** Both modules, 2 × 22 questions at 35 minutes each. A student who gets 14 or more right on Module 1 is routed to the harder Module 2. You can save and exit between modules. At the end you get an estimated score.

**Desmos Playbook.** One page of the Desmos techniques that matter on the SAT: sliders for unknown constants, counting solutions, max/min, regression from a table, lists for statistics, equivalent expressions, degree mode, and when *not* to use Desmos. It's also reachable from inside the calculator panel.

**Results after every session** cover:

- **Timing:** time used vs. allowed, average per question, correct-but-slow count, time spent on missed questions, and the biggest time sinks
- **Desmos use:** how often she opened Desmos on Desmos questions; accuracy and time with vs. without it; "missed Desmos opportunities"
- a worked solution and Desmos strategy for every question

**Starting level.** The app starts at **740** (the latest official SAT Math score). It changes in the Parent area. After about 20 answers, the app's own estimate takes over.

**Test-like interface.** Timer with Hide, Calculator (Desmos) panel, Reference sheet, Directions, Mark for Review, answer cross-out, grid-in answer preview, question navigator, and a Check Your Work page.

**Parent area** (bottom of the home page, optional PIN):

- answer key with explanations
- "Remove from practice" switch for each question
- baseline score and calculator setting
- export, import, and reset of progress

## The question bank

There are 156 original questions:

| Domain | Count | Medium / Hard / Very hard |
|---|---|---|
| Algebra | 34 | 8 / 18 / 8 |
| Advanced Math | 52 | 4 / 20 / 28 |
| Problem-Solving & Data Analysis | 37 | 9 / 19 / 9 |
| Geometry & Trigonometry | 33 | 4 / 16 / 13 |

- **65 are Desmos-route questions** (graphing is the intended fast route).
- **23 by-hand questions also show a "Desmos alternative"**, so 88 questions teach a Desmos method.
- A top-band set of 26 questions targets what separates 740 from 790: tangency and number-of-solutions conditions with parameters, regressions, cubic behavior, messy systems, and statistics from lists.
- All 19 official SAT math skills are covered.

Every answer key went through several review rounds before it could reach the app. See [review/REVIEW.md](review/REVIEW.md) for the details and [review/answer-key.md](review/answer-key.md) for a readable answer key.

## Running it

It is a static web page with no server and no install.

- **On one computer:** open `app/index.html` in Chrome, Edge, or Safari. The math renders offline. The Desmos calculator needs an internet connection.
- **As a website (recommended):** the included GitHub workflow publishes `app/` to GitHub Pages. One-time setup: in the repo, go to **Settings → Pages → Source** and choose **GitHub Actions**. After the next push to `main`, the site is at `https://<your-user>.github.io/<repo>/`.

Progress is saved in the browser, so use the same computer and browser each time. To move to another computer, use Export/Import in the Parent area.

### Desmos API key

The app loads Desmos with the public demo API key from Desmos's documentation (in `app/js/app.js`, `DESMOS_URL`). If Desmos ever rejects that key, request a free key at <https://www.desmos.com/api> and paste it in. If the calculator can't load, the panel shows a link to open desmos.com/calculator in a new tab.

## Adding or editing questions

Questions are written in Python under `bank/`. Each one has a `verify` function that re-derives the answer from scratch with SymPy. The build refuses to export a question if its key doesn't match the computed answer.

```bash
pip install sympy
cd tools && npm ci && cd ..
python3 tools/build_bank.py     # verify every question and regenerate app/js/questions.js
node tools/check_render.js      # compile every math snippet with KaTeX
node tools/test_engine.js       # grading, adaptivity, pacing, and scoring tests
node tools/e2e.js               # drives the real app in a browser (needs Playwright)
```

Math goes inside `\( ... \)` or `\[ ... \]`. A plain `$` is just a dollar sign.

## Notes and limits

- The score estimate comes from a statistical model of question difficulty (a Rasch model). It's a useful guide, not an official College Board conversion.
- Target times per question: 1:00 for Medium, 1:30 for Hard, 2:00 for Very hard. A correct answer more than 30% over its target is counted as "slow".
- Questions are text-only (tables, but no drawn figures), so geometry questions describe their figures in words.
- At the top difficulty mix, there are enough unseen Hard and Very hard questions for roughly 3–4 one-module sets per domain mix. After that, the app re-serves trouble spots first.
- This is an independent practice tool and isn't affiliated with or endorsed by College Board. SAT is a trademark of College Board.
