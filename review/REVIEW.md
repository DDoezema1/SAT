# How the questions were reviewed

No question reaches the app unless it passes every round below. Rounds 1, 2, and 4 are automated and run again on every change, both through `tools/build_bank.py` and in the GitHub workflow. That means an edit that breaks a question also breaks the build.

## Round 1: Independent computation of every answer key

Each question in `bank/*.py` comes with a `verify()` function that solves the problem again from the original data. It uses SymPy (exact algebra), brute-force search, or simulation. It does **not** copy the key.

- **Multiple choice:** exactly one of the four choices must equal the computed answer, that choice must be the keyed letter, and no two choices may be equal.
- **Grid-in:** the key must equal the computed value, and it must be enterable in the SAT answer box (5 characters, or 6 with a minus sign).
- **"Must be true" questions:** random simulations test every choice. For example, PSD-10 runs 4,000 random score lists and ADV-08 runs 40 random polynomials. Only the keyed choice may hold in every case.

Results: **125 of 130** questions were verified by computation. The other 5 (PSD-13, PSD-14, PSD-15, PSD-32, PSD-33) test the interpretation of a study's design, which can't be computed. They were reviewed by hand in Round 3.

*Checking the checker:* wrong keys were planted on purpose (a wrong grid-in answer, a wrong letter, and two identical choices). The build caught all three and refused to export.

## Round 2: Rendering

- `tools/check_render.js` compiles all 1,385 math snippets with KaTeX in strict mode: **0 errors**.
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

## Your round

In the app, the **Parent area** (link at the bottom of the home page) shows every question with its answer and explanation. If anything looks off to you, check **Remove from practice** and that question will never be served. This file's companion, [answer-key.md](answer-key.md), has the same content as a plain document you can read through or print.
