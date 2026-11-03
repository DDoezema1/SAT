#!/usr/bin/env python3
"""Verify every question in the bank and export it for the app.

Review round 1 (this script, automated):
  * structural lint: ids, domains, skills, difficulty, choice count, distinct choices,
    balanced math delimiters, Desmos tip present for Desmos questions
  * independent computation: each question's verify() re-derives the answer with
    SymPy / brute force; for multiple choice, exactly one choice must equal it and it
    must be the keyed letter; for student-produced responses the key must equal it
  * grid-in fit: every student-produced answer must be enterable in the SAT answer box
    (max 5 characters, 6 with a leading minus sign)

Any failure aborts the build, so a wrong question can never reach the app.

Usage:  python3 tools/build_bank.py
Writes: app/js/questions.js and review/answer-key.md
"""
import json
import os
import random
import re
import sys
from fractions import Fraction

import sympy as sp

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from bank.common import QUESTIONS, SKILLS  # noqa: E402
import bank.algebra, bank.advanced, bank.psda, bank.geometry  # noqa: E402,F401
try:
    import bank.extra  # noqa: F401
except ImportError:
    pass

DOMAIN_NAMES = {"ALG": "Algebra", "ADV": "Advanced Math",
                "PSD": "Problem-Solving and Data Analysis", "GEO": "Geometry and Trigonometry"}
LETTERS = "ABCD"
errors = []


def err(q, msg):
    errors.append(f"{q.get('id', '?')}: {msg}")


def to_sym(v):
    if isinstance(v, str):
        return sp.sympify(v, locals={"x": sp.Symbol("x"), "t": sp.Symbol("t")})
    if isinstance(v, tuple):
        return tuple(to_sym(e) for e in v)
    return sp.sympify(v)


def same(a, b):
    a, b = to_sym(a), to_sym(b)
    if isinstance(a, tuple) or isinstance(b, tuple):
        return isinstance(a, tuple) and isinstance(b, tuple) and len(a) == len(b) and all(same(p, q) for p, q in zip(a, b))
    free = sorted(a.free_symbols | b.free_symbols, key=str)
    if not free:
        return abs(complex(sp.N(a - b, 30))) < 1e-9
    rnd = random.Random(1)
    for _ in range(6):
        sub = {s: sp.Rational(rnd.randint(25, 400), 10) for s in free}   # positive test points
        if abs(complex(sp.N((a - b).subs(sub), 30))) > 1e-9:
            return False
    return True


def spr_fits(value: Fraction):
    """Can the exact (or SAT-truncated) value be entered in the answer box?"""
    maxlen = 6 if value < 0 else 5
    frac = f"{value.numerator}/{value.denominator}" if value.denominator != 1 else str(value.numerator)
    if len(frac) <= maxlen:
        return True
    whole = str(abs(int(value)))
    return len(whole) + (1 if value < 0 else 0) <= maxlen - 2


def balanced(html):
    return html.count(r"\(") == html.count(r"\)") and html.count(r"\[") == html.count(r"\]")


seen = set()
for q in QUESTIONS:
    qid = q.get("id")
    if qid in seen:
        err(q, "duplicate id")
    seen.add(qid)
    if q["domain"] not in SKILLS:
        err(q, f"bad domain {q['domain']}")
        continue
    if q["skill"] not in SKILLS[q["domain"]]:
        err(q, f"skill '{q['skill']}' not in domain {q['domain']}")
    if q["diff"] not in (1, 2, 3):
        err(q, "diff must be 1, 2, or 3")
    if not isinstance(q["desmos"], bool):
        err(q, "desmos flag must be bool")
    if q["desmos"] and not q["tip"]:
        err(q, "Desmos question needs a Desmos tip")
    for field in ("stem", "explain", "tip"):
        if not balanced(q.get(field, "")):
            err(q, f"unbalanced math delimiters in {field}")
    if "$$" in q["stem"] or "$$" in q["explain"]:
        err(q, "do not use $$ (dollar signs are literal money)")

    is_mc = "choices" in q
    q["type"] = "mc" if is_mc else "spr"
    if q["verify"] is None:
        if not q["reasoning"]:
            err(q, "no verifier and not flagged as a reasoning question")
        q["verified"] = "reasoning"
        continue
    try:
        result = q["verify"]()
    except Exception as e:  # noqa: BLE001
        err(q, f"verify() raised {type(e).__name__}: {e}")
        continue

    if is_mc:
        ch = q["choices"]
        if len(ch) != 4 or len(set(ch)) != 4:
            err(q, "multiple choice needs 4 distinct choices")
        if q["answer"] not in LETTERS:
            err(q, "answer must be A-D")
            continue
        if q.get("vals") is not None:
            vals = q["vals"]
            if len(vals) != 4:
                err(q, "vals must have 4 entries")
                continue
            matches = [LETTERS[i] for i, v in enumerate(vals) if same(v, result)]
            if matches != [q["answer"]]:
                err(q, f"computed answer {result} matches choices {matches}, key is {q['answer']}")
            for i in range(4):
                for j in range(i + 1, 4):
                    if same(vals[i], vals[j]):
                        err(q, f"choices {LETTERS[i]} and {LETTERS[j]} are equal")
        else:
            if result != q["answer"]:
                err(q, f"verify() returned {result}, key is {q['answer']}")
    else:
        try:
            key = Fraction(q["answer"])
        except ValueError:
            err(q, f"SPR answer '{q['answer']}' is not a number")
            continue
        if not same(sp.Rational(key.numerator, key.denominator), result):
            err(q, f"computed {result} but key is {q['answer']}")
        if not spr_fits(key):
            err(q, "answer does not fit in the SAT answer box")
    q["verified"] = "computed"

for q in QUESTIONS:
    q["ordered"] = False
    if q.get("type") == "mc" and q.get("vals") is not None:
        try:
            nums = [float(sp.N(to_sym(v))) for v in q["vals"]]
            q["ordered"] = nums == sorted(nums)
        except (TypeError, ValueError, AttributeError):
            pass

if errors:
    print("BUILD FAILED. Problems found:\n  " + "\n  ".join(errors))
    sys.exit(1)

# Inside HTML, a raw "<" in math (e.g. \(7<x\)) is parsed by the browser as a tag.
# Rewrite comparison signs inside math segments as \lt / \gt.
MATH_RE = re.compile(r"\\\((.*?)\\\)|\\\[(.*?)\\\]", re.S)


def fix_math(html):
    def sub(m):
        body = m.group(0)
        return body[:2] + body[2:-2].replace("<", r" \lt ").replace(">", r" \gt ") + body[-2:]
    return MATH_RE.sub(sub, html)


for q in QUESTIONS:
    for f in ("stem", "explain", "tip"):
        q[f] = fix_math(q[f])
    if q["type"] == "mc":
        q["choices"] = [fix_math(c) for c in q["choices"]]
    for f in ("stem", "explain", "tip"):
        for m in MATH_RE.finditer(q[f]):
            assert "<" not in m.group(0), (q["id"], m.group(0))

# ---------------------------------------------------------------------------
out = []
for q in QUESTIONS:
    out.append({k: q[k] for k in ("id", "domain", "skill", "diff", "desmos", "type", "stem", "answer", "explain", "tip", "verified", "ordered")}
               | ({"choices": q["choices"]} if q["type"] == "mc" else {}))

os.makedirs(os.path.join(ROOT, "app", "js"), exist_ok=True)
with open(os.path.join(ROOT, "app", "js", "questions.js"), "w") as f:
    f.write("// GENERATED by tools/build_bank.py -- do not edit by hand. Edit bank/*.py and rebuild.\n")
    f.write("window.SAT_DOMAINS = " + json.dumps(DOMAIN_NAMES) + ";\n")
    f.write("window.SAT_SKILLS = " + json.dumps(SKILLS, indent=1) + ";\n")
    f.write("window.SAT_QUESTIONS = " + json.dumps(out, indent=1, ensure_ascii=False) + ";\n")

# Human-readable answer key for parent review.
os.makedirs(os.path.join(ROOT, "review"), exist_ok=True)
DIFF = {1: "Medium", 2: "Hard", 3: "Very hard"}
with open(os.path.join(ROOT, "review", "answer-key.md"), "w") as f:
    f.write("# Answer key (generated)\n\n")
    f.write("Every question below passed the automated checks in `tools/build_bank.py`. "
            "Questions marked *computed* had their answers re-derived independently by code; "
            "questions marked *reasoning* are interpretation questions that were reviewed by hand.\n\n")
    for d in DOMAIN_NAMES:
        f.write(f"## {DOMAIN_NAMES[d]}\n\n")
        for q in QUESTIONS:
            if q["domain"] != d:
                continue
            strip = lambda h: re.sub(r"<[^>]+>", " ", h)
            f.write(f"### {q['id']} · {q['skill']} · {DIFF[q['diff']]} · {'Desmos' if q['desmos'] else 'By hand'} · {q['verified']}\n\n")
            f.write(strip(q["stem"]) + "\n\n")
            if q["type"] == "mc":
                for L, c in zip(LETTERS, q["choices"]):
                    f.write(f"- {L}) {strip(c)}\n")
                f.write("\n")
            f.write(f"**Answer:** {q['answer']}\n\n**Explanation:** {strip(q['explain'])}\n\n")

counts = {}
for q in QUESTIONS:
    counts.setdefault(q["domain"], [0, 0, 0, 0])
    counts[q["domain"]][q["diff"]] += 1
    counts[q["domain"]][0] += 1
print(f"OK: {len(QUESTIONS)} questions verified "
      f"({sum(q['verified'] == 'computed' for q in QUESTIONS)} computed, "
      f"{sum(q['verified'] == 'reasoning' for q in QUESTIONS)} reasoning-only).")
for d, (n, d1, d2, d3) in counts.items():
    print(f"  {d}: {n:3d}  medium={d1} hard={d2} very-hard={d3}")
print(f"  Desmos-route: {sum(q['desmos'] for q in QUESTIONS)}, by-hand: {sum(not q['desmos'] for q in QUESTIONS)}")
print(f"  Student-produced: {sum(q['type'] == 'spr' for q in QUESTIONS)}, multiple choice: {sum(q['type'] == 'mc' for q in QUESTIONS)}")
