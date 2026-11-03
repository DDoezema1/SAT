# How the questions were reviewed

No question reaches the app unless it passes every round below. Rounds 1, 2, and 4 are automated and run again on every change, both through `tools/build_bank.py` and in the GitHub workflow. That means an edit that breaks a question also breaks the build.

## Round 1: Independent computation of every answer key

Each question in `bank/*.py` comes with a `verify()` function that solves the problem again from the original data. It uses SymPy (exact algebra), brute-force search, or simulation. It does **not** copy the key.

- **Multiple choice:** exactly one of the four choices must equal the computed answer, that choice must be the keyed letter, and no two choices may be equal.
- **Grid-in:** the key must equal the computed value, and it must be enterable in the SAT answer box (5 characters, or 6 with a minus sign).
- **"Must be true" questions:** random simulations test every choice. For example, PSD-10 runs 4,000 random score lists and ADV-08 runs 40 random polynomials. Only the keyed choice may hold in every case.

Results: **151 of 156** questions were verified by computation. The other 5 (PSD-13, PSD-14, PSD-15, PSD-32, PSD-33) test the interpretation of a study's design, which can't be computed. They were reviewed by hand in Round 3.

*Checking the checker:* wrong keys were planted on purpose (a wrong grid-in answer, a wrong letter, and two identical choices). The build caught all three and refused to export.

## Round 2: Rendering

- `tools/check_render.js` compiles all 1,817 math snippets with KaTeX in strict mode: **0 errors**.
- `tools/e2e.js` opens the real app in Chromium and renders the entire bank. It found **one real bug**: in PSD-08, `\(7<x<9\)` was read by the browser as an HTML tag, which broke that explanation. The fix applies to the whole bank: the build now rewrites `<` and `>` inside math as `\lt` and `\gt`, and a lint rule fails the build if a raw `<` ever appears inside math again.

## Round 3: Line-by-line read-through

Every stem, choice, key, and explanation was re-read and re-solved, looking for anything the computer can't judge: ambiguous wording, conventions that differ from the SAT's, misleading distractors, and explanations that don't match their question. Fixes made:

| Question | Problem | Fix |
|---|---|---|
| ADV-05 | Asked "which of the following *equivalent* functions…", but three of the choices are not equivalent | Now asks which function "is equivalent to \(f\) and shows…" |
| ADV-12 | Asked for "the value of A" while the answer choices are also labeled A–D | Renamed the constant to \(r\) |
| PSD-12 | "A ratio of 3 to 5" didn't say which color was which | Now "The ratio of red marbles to blue marbles is 3 to 5" |
| GEO-07 | The stem mixed two descriptions of the same setup | Rewritten in the standard form: \(\sin x^\circ=\cos(3x-10)^\circ\), both angles acute |
| PSD-01, PSD-18 | Asked for an answer "in dollars" while the choices already show $ | Removed the redundant phrase |
| ALG-17 | The explanation listed a decimal that is not accepted | Explanation corrected |

## Round 4: Fairness and format

- **Answer-letter balance:** as written, few keys landed on D. A test-savvy student could exploit that. The app now shuffles statement choices on each attempt and randomly reverses numeric choices, so the numbers stay in order. Seven explanations that referred to choices by letter ("Choice B…") were rewritten to describe the choice itself, so they stay correct after shuffling.
- **Grid-in grading** follows the SAT rules, and every grid-in key in the bank was checked against the grader: any exact equivalent is accepted (7/2, 3.5, 3.50); a repeating decimal must fill the answer box and may be truncated or rounded (2/3 accepts .6666, .6667, 0.666, 0.667, but not .66 or .67).
- **Blueprint:** module assembly is tested to always produce 22 unique questions in the SAT domain mix (7 Algebra, 7 Advanced Math, 4 Problem-Solving & Data Analysis, 4 Geometry & Trigonometry), with the harder Module 2 measurably harder than the standard one.

## Top-band additions (second batch)

26 questions aimed at 740+ students (`bank/top.py`, ids `TOP-xx`) and 23 "Desmos alternative" notes on by-hand questions (`bank/desmos_alt.py`) went through the same rounds:

- **Round 1:** all 26 verified by computation. Examples: TOP-02 counts distinct real roots for every integer \(c\) from \(-60\) to \(59\); TOP-03 scans \(2^x-x^2\) for sign changes; TOP-20 brute-forces every list of 5 positive integers. Wrong keys were planted in two of them, and the build caught both.
- **Round 2:** rendered in KaTeX and in the browser with no errors.
- **Round 3:** read through and re-solved. One fix: TOP-06 asked what "must be true" about one specific data set; it now asks which statements "are true".
- Every Desmos alternative was checked against the question's own numbers. For example, the GEO-02 note gives the diameter as \(2\sqrt{17}\approx8.25\), and the PSD-24 list has the right 20 values.

## Reading & Writing questions

English answers can't be computed, so these 67 questions went through different rounds. They are labeled "reviewed", not "computer-verified".

1. **Automated consistency checks** (`tools/build_rw.py`, run on every build and in CI):
   - every question links to a real rule
   - 4 distinct choices and exactly one blank in fill-in questions
   - passages within SAT length
   - no explanation refers to a choice by its letter (choices are shuffled)
   - **each explanation must quote the keyed choice exactly** in quotation marks, which catches a key typed with the wrong letter

   To test the checks, wrong letters were planted on three questions, and the build caught all three. (While doing this, I found that Python could run a stale cached copy of the bank; the build scripts now bypass that cache.)
2. **Separate re-solve:** I printed the reading and rhetoric questions with the answers hidden, solved each one again, and compared with the keys. Every key matched. Two items were tightened:
   - **RW-INF-01:** a wrong quotation could arguably support the original claim, so the claim was rewritten until exactly one quotation fits.
   - **RW-EXP-12:** the keyed answer said "became widely known", which the notes never state. Notes answers must stick to the notes, so it now says only what the notes support.
3. **Grammar items** were written against the rule they test, with distractors that each break a specific rule, and re-checked against that rule.
4. **Browser check:** all 67 questions render in the app, in the Parent area and in practice.

Passages use well-established facts (for example the 1815 Tambora eruption, the 1994 Card–Krueger study, and Fleming's 1928 observation). The quoted literary texts are public domain (Dickinson; Austen's *Pride and Prejudice*) and were checked against their standard wording.

## Your round

In the app, the **Parent area** (link at the bottom of the home page) shows every question with its answer and explanation. If anything looks off to you, check **Remove from practice** and that question will never be served. [answer-key.md](answer-key.md) (Math) and [rw-answer-key.md](rw-answer-key.md) (Reading & Writing, grouped by rule) have the same content as plain documents you can read through or print.
