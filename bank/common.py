"""Shared helpers for authoring SAT math questions.

Every question is registered with Q(...). Fields:

  id       unique id, e.g. "ALG-01"
  domain   "ALG" | "ADV" | "PSD" | "GEO"
  skill    one of SKILLS[domain]
  diff     1 = medium, 2 = hard, 3 = very hard (top-band SAT difficulty)
  desmos   True if graphing in Desmos is the fastest/smartest route,
           False if the question is designed to be solved by reasoning/algebra
  stem     HTML; inline math in \\( ... \\), display math in \\[ ... \\]
  choices  list of 4 HTML strings for multiple choice; omit for student-produced response
  answer   "A".."D" for multiple choice, or a number string such as "41/3" or "-27"
  vals     (MC only, optional) machine values of each choice, used to check that
           exactly one choice equals the independently computed answer
  verify   function that re-derives the answer from scratch (SymPy / brute force).
           For MC with vals it returns the correct value; for MC without vals it
           returns the correct letter; for SPR it returns the numeric answer.
           None only for pure-interpretation questions (flagged reasoning=True).
  explain  HTML explanation shown in review
  tip      Desmos strategy (required when desmos=True)
"""

QUESTIONS = []

SKILLS = {
    "ALG": [
        "Linear equations in one variable",
        "Linear functions",
        "Linear equations in two variables",
        "Systems of two linear equations in two variables",
        "Linear inequalities in one or two variables",
    ],
    "ADV": [
        "Equivalent expressions",
        "Nonlinear equations in one variable and systems of equations in two variables",
        "Nonlinear functions",
    ],
    "PSD": [
        "Ratios, rates, proportional relationships, and units",
        "Percentages",
        "One-variable data: distributions and measures of center and spread",
        "Two-variable data: models and scatterplots",
        "Probability and conditional probability",
        "Inference from sample statistics and margin of error",
        "Evaluating statistical claims: observational studies and experiments",
    ],
    "GEO": [
        "Area and volume",
        "Lines, angles, and triangles",
        "Right triangles and trigonometry",
        "Circles",
    ],
}


def Q(**kw):
    kw.setdefault("reasoning", False)
    kw.setdefault("tip", "")
    QUESTIONS.append(kw)
