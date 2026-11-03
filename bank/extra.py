"""Additional questions plus multiple-choice conversions of earlier grid-ins.

The real SAT is roughly 75% multiple choice. Several questions authored as
student-produced responses are converted here to multiple choice, with distractors
built from the most common mistakes. The original verify() still runs, and the build
checks that exactly one choice equals the computed answer.
"""
import random
import statistics
from fractions import Fraction as F
from sympy import Rational as R, symbols, solve, Eq, sqrt, Poly, real_roots, expand
from .common import Q, QUESTIONS

x, y, a, b, c, k, m, t = symbols("x y a b c k m t")

def _num(v):
    return r"\(" + str(v) + r"\)"

# id -> (choices, vals, answer letter)
CONVERT = {
    "ALG-04": ([1020, 1380, 1660, 1820], "C"),
    "ALG-10": ([37, 38, 41, 90], "A"),
    "ALG-13": ([4, 5, 6, 7], "C"),
    "ALG-14": ([15, 17, 20, 23], "C"),
    "ADV-10": ([R(9, 4), 81, 86, 167], "C"),
    "ADV-11": ([16, 24, 48, 96], "C"),
    "ADV-12": ([-15, -5, 5, 15], "B"),
    "ADV-17": ([2, 3, 4, 5], "C"),
    "ADV-18": ([-43, -37, 43, 57], "A"),
    "ADV-23": ([2, 3, 5, 15], "C"),
    "ADV-27": ([-2, R(-1, 2), R(1, 2), 2], "B"),
    "ADV-29": ([-24, 12, 24, 48], "C"),
    "PSD-02": ([16, 60, 110, 375], "B"),
    "PSD-04": ([10, 25, 40, 1500], "B"),
    "PSD-05": ([168, 208, 240, 268], "B"),
    "PSD-06": ([19, 20, 21, 22], "C"),
    "PSD-07": ([2, 13, 15, 29], "D"),
    "PSD-12": ([9, 10, 15, 18], "C"),
    "PSD-16": ([-3, 3, 39, 42], "B"),
    "PSD-17": ([46, 47, 48, 50], "C"),
    "PSD-21": ([90, 360, 900, 9000], "C"),
    "PSD-22": ([1650, 1682, 1700, 1740], "B"),
    "GEO-04": ([4, 6, 8, 2*sqrt(34)], "C"),
    "GEO-08": ([12, 18, 36, 36*sqrt(3)], "C"),
    "GEO-13": ([35, 70, 75, 85], "C"),
    "GEO-16": ([6, 12, 24, 48], "C"),
    "GEO-19": ([60, 78, 90, 117], "C"),
}
CONVERT_LABELS = {
    "ADV-10": [r"\(2.25\)", r"\(81\)", r"\(86\)", r"\(167\)"],
    "ADV-27": [r"\(-2\)", r"\(-\frac{1}{2}\)", r"\(\frac{1}{2}\)", r"\(2\)"],
    "PSD-02": ["16%", "60%", "110%", "375%"],
    "PSD-04": ["10", "25", "40", "1,500"],
    "PSD-21": ["90", "360", "900", "9,000"],
    "PSD-22": ["1,650", "1,682", "1,700", "1,740"],
    "GEO-04": [r"\(4\)", r"\(6\)", r"\(8\)", r"\(2\sqrt{34}\)"],
    "GEO-08": [r"\(12\)", r"\(18\)", r"\(36\)", r"\(36\sqrt3\)"],
    "ALG-04": ["1,020", "1,380", "1,660", "1,820"],
    "PSD-01": ["$76.95", "$85.26", "$90.00", "$97.20"],
    "PSD-18": ["$54.74", "$56.00", "$64.40", "$74.06"],
}
CONVERT["PSD-01"] = ([R(7695, 100), R(8526, 100), 90, R(972, 10)], "C")
CONVERT["PSD-18"] = ([R(5474, 100), 56, R(644, 10), R(7406, 100)], "B")

for q in QUESTIONS:
    if q["id"] in CONVERT:
        vals, ans = CONVERT[q["id"]]
        q["vals"] = vals
        q["choices"] = CONVERT_LABELS.get(q["id"]) or [_num(v) for v in vals]
        q["answer"] = ans

# Extra Desmos strategies for existing questions that Desmos handles well.
EXTRA_TIPS = {
    "PSD-19": r"Graph \(y=(1-x/100)(1+x/100)\) and \(y=0.96\). Click the positive intersection: \(x=20\).",
    "ADV-20": r"Graph \(y=2x^2-12x+k\) with a slider for \(k\). Its zeros are always centered at \(x=3\); slide \(k\) until the zeros are at 1 and 5 (4 apart): \(k=10\).",
}
for q in QUESTIONS:
    if q["id"] in EXTRA_TIPS:
        q["desmos"] = True
        q["tip"] = EXTRA_TIPS[q["id"]]

ALG = {"L1": "Linear equations in one variable", "LF": "Linear functions",
       "L2": "Linear equations in two variables", "SY": "Systems of two linear equations in two variables",
       "IN": "Linear inequalities in one or two variables"}
EQ = "Equivalent expressions"
NE = "Nonlinear equations in one variable and systems of equations in two variables"
NF = "Nonlinear functions"

# ---------------------------------------------------------------------------
def _x01():
    sols = solve([Eq(y, x**2 - 8*x + 15), Eq(y, -x**2 + 4*x - 1)], [x, y], dict=True)
    return sum(s[y] for s in sols)

Q(id="ADV-31", domain="ADV", skill=NE, diff=3, desmos=True,
  stem=r"\[y=x^2-8x+15\]\[y=-x^2+4x-1\]The graphs of the given equations in the \(xy\)-plane intersect at two points. What is the sum of the \(y\)-coordinates of the two points?",
  choices=[r"\(-2\)", r"\(2\)", r"\(6\)", r"\(8\)"], vals=[-2, 2, 6, 8], answer="B", verify=_x01,
  explain=r"Set the expressions equal: \(x^2-8x+15=-x^2+4x-1\), so \(2x^2-12x+16=0\), or \(x^2-6x+8=0\), giving \(x=2\) or \(x=4\). "
          r"\(y\)-values: \(4-16+15=3\) and \(16-32+15=-1\). Sum: \(2\). (6 is the trap: the sum of the \(x\)-coordinates.)",
  tip=r"Graph both parabolas and click the two intersection points: \((2,3)\) and \((4,-1)\). Add the \(y\)-coordinates.")

def _x02():
    f = 2*x**3 - 3*x**2 - 12*x + 7
    cands = [0, 5] + [r for r in solve(f.diff(x), x) if 0 <= r <= 5]
    return min(f.subs(x, v) for v in cands)

Q(id="ADV-32", domain="ADV", skill=NF, diff=3, desmos=True,
  stem=r"The function \(f\) is defined by \(f(x)=2x^3-3x^2-12x+7\). What is the minimum value of \(f(x)\) for \(0\le x\le5\)?",
  answer="-13", verify=_x02,
  explain=r"This question is designed for Desmos. Graph \(f\) on the interval: it decreases from \(f(0)=7\) to a low point at \(x=2\), then increases to \(f(5)=122\). "
          r"The minimum value is \(f(2)=16-12-24+7=-13\).",
  tip=r"Type <code>f(x)=2x^3-3x^2-12x+7\{0\le x\le5\}</code> to restrict the domain, then click the lowest point: \((2,-13)\). The answer is the \(y\)-value, \(-13\), not \(x=2\).")

Q(id="ALG-24", domain="ALG", skill=ALG["SY"], diff=2, desmos=True,
  stem=r"\[y=0.5x+3.25\]\[1.75x-2.5y=-4.5\]The solution to the given system of equations is \((x,y)\). What is the value of \(x\)?",
  choices=[r"\(5.5\)", r"\(6.75\)", r"\(7.25\)", r"\(8.5\)"], vals=[R(11, 2), R(27, 4), R(29, 4), R(17, 2)], answer="C",
  verify=lambda: solve([Eq(y, R(1, 2)*x + R(13, 4)), Eq(R(7, 4)*x - R(5, 2)*y, R(-9, 2))], [x, y])[x],
  explain=r"Substitute: \(1.75x-2.5(0.5x+3.25)=-4.5\), so \(1.75x-1.25x-8.125=-4.5\). Then \(0.5x=3.625\), and \(x=7.25\).",
  tip=r"With decimal-heavy systems, Desmos is fastest: graph both and click the intersection, \((7.25, 6.875)\).")

Q(id="ADV-33", domain="ADV", skill=NE, diff=3, desmos=True,
  stem=r"\[y=x^2+6x+c\]\[y=2x+1\]In the given system of equations, \(c\) is a constant. What is the greatest integer value of \(c\) for which the system has two distinct real solutions?",
  answer="4", verify=lambda: max(v for v in range(-50, 50) if (4)**2 - 4*1*(v - 1) > 0),
  explain=r"Substitute: \(x^2+6x+c=2x+1\), so \(x^2+4x+(c-1)=0\). Two distinct real solutions require a positive discriminant: \(16-4(c-1)>0\), so \(c<5\). "
          r"The greatest integer is 4. (At \(c=5\), the line is tangent to the parabola: only one solution.)",
  tip=r"Graph both with a slider for \(c\). At \(c=5\) the line just touches the parabola; any smaller \(c\) gives two intersections. The greatest integer below 5 is 4.")

def _x05():
    xs = [1, 2, 3, 4, 5]; ys = [3.1, 5.0, 6.8, 9.1, 10.9]
    mx, my = statistics.mean(xs), statistics.mean(ys)
    sl = sum((p - mx)*(q - my) for p, q in zip(xs, ys)) / sum((p - mx)**2 for p in xs)
    ic = my - sl*mx
    opts = {"A": (1.97, 1.07), "B": (1.07, 1.97), "C": (2.5, -0.5), "D": (-1.97, 12.89)}
    return min(opts, key=lambda L: abs(opts[L][0] - sl) + abs(opts[L][1] - ic))

Q(id="PSD-23", domain="PSD", skill="Two-variable data: models and scatterplots", diff=2, desmos=True,
  stem=r"The table shows five data points."
       r"<table class='data'><tr><th>\(x\)</th><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr>"
       r"<tr><th>\(y\)</th><td>3.1</td><td>5.0</td><td>6.8</td><td>9.1</td><td>10.9</td></tr></table>"
       r"Which of the following equations best represents the linear model that fits the data?",
  choices=[r"\(y=1.97x+1.07\)", r"\(y=1.07x+1.97\)", r"\(y=2.5x-0.5\)", r"\(y=-1.97x+12.89\)"], answer="A", verify=_x05,
  explain=r"The \(y\)-values increase by about 2 each time \(x\) increases by 1, so the slope is about 2. This rules out the equations with slope 1.07 and slope \(-1.97\). "
          r"At \(x=3\), the model should give about the middle value: \(1.97(3)+1.07=6.98\), which is close to 6.8. The equation \(y=2.5x-0.5\) gives 7.0 at \(x=3\) but 12 at \(x=5\), far from 10.9. "
          r"The least-squares line is \(y=1.97x+1.07\).",
  tip=r"Make a table in Desmos (+ &rarr; table), enter the data as \(x_1, y_1\), then type <code>y_1 ~ m x_1 + b</code>. Desmos reports \(m=1.97\), \(b=1.07\).")

def _x06():
    sols = solve([Eq((x - 3)**2 + (y + 2)**2, 20), Eq(y, 2*x - 3)], [x, y], dict=True)
    assert len(sols) == 2
    return expand(sols[0][x]*sols[1][x])

Q(id="GEO-24", domain="GEO", skill="Circles", diff=3, desmos=True,
  stem=r"In the \(xy\)-plane, the line \(y=2x-3\) intersects the circle \((x-3)^2+(y+2)^2=20\) at two points. What is the product of the \(x\)-coordinates of the two points?",
  choices=[r"\(-2\)", r"\(-1\)", r"\(2\)", r"\(4\)"], vals=[-2, -1, 2, 4], answer="A", verify=_x06,
  explain=r"Substitute \(y=2x-3\): \((x-3)^2+(2x-1)^2=20\). Expand: \(x^2-6x+9+4x^2-4x+1=20\), so \(5x^2-10x-10=0\), or \(x^2-2x-2=0\). "
          r"The product of the roots of \(x^2+bx+c\) is \(c\), so the product is \(-2\). (The roots are \(1\pm\sqrt3\), and \((1+\sqrt3)(1-\sqrt3)=1-3=-2\).)",
  tip=r"Graph both. The intersections are at \(x\approx2.732\) and \(x\approx-0.732\). Multiply them: \(\approx-2.000\).")

Q(id="ALG-25", domain="ALG", skill=ALG["SY"], diff=2, desmos=False,
  stem=r"\[3a-2b=11\]\[a+4b=13\]If \((a,b)\) is the solution to the given system of equations, what is the value of \(4a+2b\)?",
  choices=[r"\(12\)", r"\(18\)", r"\(24\)", r"\(30\)"], vals=[12, 18, 24, 30], answer="C",
  verify=lambda: (lambda d: 4*d[a] + 2*d[b])(solve([Eq(3*a - 2*b, 11), Eq(a + 4*b, 13)], [a, b])),
  explain=r"Look for a shortcut before solving: adding the two equations gives \(4a+2b=24\) directly.")

Q(id="ADV-34", domain="ADV", skill=EQ, diff=3, desmos=False,
  stem=r"Which of the following is equivalent to \(x^2-4xy+4y^2-9\)?",
  choices=[r"\((x-2y-3)(x-2y+3)\)", r"\((x-2y-9)(x-2y+1)\)", r"\((x+2y-3)(x+2y+3)\)", r"\((x-4y-3)(x+y+3)\)"],
  vals=["(x-2*y-3)*(x-2*y+3)", "(x-2*y-9)*(x-2*y+1)", "(x+2*y-3)*(x+2*y+3)", "(x-4*y-3)*(x+y+3)"], answer="A",
  verify=lambda: x**2 - 4*x*y + 4*y**2 - 9,
  explain=r"The first three terms form a perfect square: \(x^2-4xy+4y^2=(x-2y)^2\). So the expression is \((x-2y)^2-3^2\), a difference of squares: \((x-2y-3)(x-2y+3)\).")

Q(id="ADV-35", domain="ADV", skill=EQ, diff=3, desmos=False,
  stem=r"If \(x>0\) and \(x-\dfrac{1}{x}=3\), what is the value of \(x^2+\dfrac{1}{x^2}\)?",
  answer="11", verify=lambda: (lambda v: expand(v**2 + 1/v**2))([s for s in solve(Eq(x - 1/x, 3), x) if s > 0][0]),
  explain=r"Square both sides: \(\left(x-\frac1x\right)^2=x^2-2+\frac{1}{x^2}=9\). So \(x^2+\frac1{x^2}=11\).")

def _x10():
    vals = [1]*3 + [2]*5 + [3]*4 + [4]*6 + [5]*2
    mean, med = F(sum(vals), len(vals)), F(statistics.median(vals))
    return "A" if mean < med else ("B" if mean == med else "C")

Q(id="PSD-24", domain="PSD", skill="One-variable data: distributions and measures of center and spread", diff=3, desmos=False,
  stem=r"The frequency table summarizes a data set of 20 values."
       r"<table class='data'><tr><th>Value</th><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr>"
       r"<tr><th>Frequency</th><td>3</td><td>5</td><td>4</td><td>6</td><td>2</td></tr></table>"
       r"Which of the following is true about the mean and the median of the data set?",
  choices=["The mean is less than the median.", "The mean is equal to the median.", "The mean is greater than the median.",
           "There is not enough information to compare them."],
  answer="A", verify=_x10,
  explain=r"Mean: \(\frac{1(3)+2(5)+3(4)+4(6)+5(2)}{20}=\frac{59}{20}=2.95\). Median: the average of the 10th and 11th values. "
          r"The cumulative counts are 3, 8, 12, &hellip;, so the 9th through 12th values are all 3, and the median is 3. Since \(2.95<3\), the mean is less than the median.")

Q(id="GEO-25", domain="GEO", skill="Right triangles and trigonometry", diff=3, desmos=False,
  stem=r"Angle \(\theta\) is measured in radians, with \(\pi<\theta<\frac{3\pi}{2}\), and \(\tan\theta=\frac34\). What is the value of \(\sin\theta\)?",
  choices=[r"\(-\dfrac45\)", r"\(-\dfrac35\)", r"\(\dfrac35\)", r"\(\dfrac45\)"], vals=[R(-4, 5), R(-3, 5), R(3, 5), R(4, 5)], answer="B",
  verify=lambda: __import__("sympy").simplify(__import__("sympy").sin(__import__("sympy").pi + __import__("sympy").atan(R(3, 4)))),
  explain=r"An angle between \(\pi\) and \(\frac{3\pi}{2}\) is in Quadrant III, where sine and cosine are both negative (and tangent is positive). "
          r"\(\tan\theta=\frac34\) means a 3-4-5 reference triangle with opposite 3 and adjacent 4, so \(|\sin\theta|=\frac35\). In Quadrant III, \(\sin\theta=-\frac35\).")

def _x12():
    import math
    A, B, C = (-2, 1), (4, 1), (1, 7)
    d = lambda P, Q_: math.dist(P, Q_)
    per = d(A, B) + d(B, C) + d(C, A)
    return 6 + 6*sqrt(5) if abs(per - (6 + 6*5**0.5)) < 1e-9 else per

Q(id="GEO-26", domain="GEO", skill="Lines, angles, and triangles", diff=2, desmos=True,
  stem=r"In the \(xy\)-plane, a triangle has vertices at \((-2,1)\), \((4,1)\), and \((1,7)\). What is the perimeter of the triangle?",
  choices=[r"\(6+6\sqrt5\)", r"\(12+3\sqrt5\)", r"\(18\)", r"\(6+3\sqrt5\)"], vals=[6 + 6*sqrt(5), 12 + 3*sqrt(5), 18, 6 + 3*sqrt(5)], answer="A",
  verify=_x12,
  explain=r"The base from \((-2,1)\) to \((4,1)\) has length 6. Each slanted side runs 3 horizontally and 6 vertically: \(\sqrt{3^2+6^2}=\sqrt{45}=3\sqrt5\). "
          r"Perimeter: \(6+2(3\sqrt5)=6+6\sqrt5\).",
  tip=r"Type <code>distance((-2,1),(1,7))</code> and <code>distance((4,1),(1,7))</code> into Desmos. Each gives 6.708. The perimeter is about 19.42, which matches \(6+6\sqrt5\approx19.42\).")

Q(id="ALG-26", domain="ALG", skill=ALG["L2"], diff=2, desmos=False,
  stem=r"The monthly cost \(C\), in dollars, of a phone plan is given by \(C=0.08m+0.12t+25\), where \(m\) is the number of minutes of calls and \(t\) is the number of text messages sent that month. "
       r"If next month a customer sends 50 more text messages and uses 100 fewer minutes than this month, how will the customer's cost change?",
  choices=["It will decrease by $2.00.", "It will increase by $2.00.", "It will decrease by $14.00.", "It will increase by $14.00."],
  vals=[-2, 2, -14, 14], answer="A",
  verify=lambda: R(12, 100)*50 + R(8, 100)*(-100),
  explain=r"Change in cost: \(0.12(50)+0.08(-100)=6-8=-2\). The cost decreases by $2.00.")

def _x14():
    sols = [d for d in solve([Eq(a*b, 6), Eq(a*b**3, 54)], [a, b], dict=True) if d[b].is_real and d[b] > 0]
    assert len(sols) == 1
    return sols[0][a]*sols[0][b]**4

Q(id="ADV-36", domain="ADV", skill=NF, diff=2, desmos=False,
  stem=r"The exponential function \(f\) is defined by \(f(x)=ab^{x}\), where \(a\) and \(b\) are positive constants. The graph of \(y=f(x)\) passes through the points \((1,6)\) and \((3,54)\). What is the value of \(f(4)\)?",
  choices=[r"\(108\)", r"\(162\)", r"\(216\)", r"\(486\)"], vals=[108, 162, 216, 486], answer="B", verify=_x14,
  explain=r"Divide: \(\frac{ab^3}{ab}=b^2=\frac{54}{6}=9\), so \(b=3\) and \(a=2\). Then \(f(4)=2\cdot3^4=162\). "
          r"(108 is the trap from treating the function as linear: \(54+54\).)")

def _x15():
    rr = [r for r in real_roots(Poly(x**3 - 2*x - 21, x))]
    assert len(set(rr)) == 1
    return rr[0]

Q(id="ADV-37", domain="ADV", skill=NE, diff=2, desmos=True,
  stem=r"What is the real solution to the equation \(x^3-2x-21=0\)?",
  choices=[r"\(-3\)", r"\(3\)", r"\(7\)", r"\(21\)"], vals=[-3, 3, 7, 21], answer="B", verify=_x15,
  explain=r"Test the choices: \(3^3-2(3)-21=27-6-21=0\). ✓ Factoring gives \((x-3)(x^2+3x+7)\), and the quadratic has no real roots (discriminant \(9-28<0\)), so 3 is the only real solution.",
  tip=r"Graph \(y=x^3-2x-21\) and click the single \(x\)-intercept: \((3,0)\).")

Q(id="PSD-25", domain="PSD", skill="Inference from sample statistics and margin of error", diff=1, desmos=False,
  stem=r"A town has 18,000 households. In a random sample of 250 of these households, 35 had solar panels. Based on the sample, which of the following is the best estimate of the number of households in the town that have solar panels?",
  choices=["2,520", "3,500", "4,500", "6,300"], vals=[2520, 3500, 4500, 6300], answer="A",
  verify=lambda: R(35, 250)*18000,
  explain=r"Sample proportion: \(\frac{35}{250}=0.14\). Estimate: \(0.14\times18{,}000=2{,}520\).")

def _x17():
    from sympy import Circle, Point
    return Circle(Point(0, 0), Point(8, 0), Point(0, 6)).radius

Q(id="GEO-27", domain="GEO", skill="Circles", diff=2, desmos=False,
  stem=r"In the \(xy\)-plane, a circle passes through the points \((0,0)\), \((8,0)\), and \((0,6)\). What is the radius of the circle?",
  answer="5", verify=_x17,
  explain=r"The points \((8,0)\), \((0,0)\), and \((0,6)\) form a right angle at the origin. An inscribed right angle intercepts a semicircle, "
          r"so the segment from \((8,0)\) to \((0,6)\) is a diameter. Its length is \(\sqrt{64+36}=10\), so the radius is 5.")

Q(id="ALG-27", domain="ALG", skill=ALG["LF"], diff=1, desmos=False,
  stem=r"In the \(xy\)-plane, the graph of the linear function \(f\) passes through the points \((-2,5)\) and \((4,-7)\). If \(f(x)=mx+b\), what is the value of \(m-b\)?",
  answer="-3", verify=lambda: (lambda sl: sl - (5 - sl*(-2)))(R(-7 - 5, 4 - (-2))),
  explain=r"Slope: \(m=\frac{-7-5}{4-(-2)}=-2\). Using \((-2,5)\): \(5=-2(-2)+b\), so \(b=1\). Then \(m-b=-2-1=-3\).")

def _x19():
    rnd = random.Random(3)
    claims = {"A": lambda A, B, C: A > 0, "B": lambda A, B, C: B < 0, "C": lambda A, B, C: C > 0, "D": lambda A, B, C: B > 0}
    always = set(claims)
    for _ in range(3000):
        A_ = -rnd.uniform(0.1, 5); h = -rnd.uniform(0.1, 10); kv = rnd.uniform(0.1, 10)
        B_, C_ = -2*A_*h, A_*h*h + kv
        always = {L for L in always if claims[L](A_, B_, C_)}
    assert len(always) == 1
    return always.pop()

Q(id="ADV-38", domain="ADV", skill=NF, diff=3, desmos=False,
  stem=r"In the \(xy\)-plane, the graph of \(y=ax^2+bx+c\), where \(a\), \(b\), and \(c\) are constants, is a parabola that opens downward and has its vertex in Quadrant II. Which of the following must be true?",
  choices=[r"\(a>0\)", r"\(b<0\)", r"\(c>0\)", r"\(b>0\)"], answer="B", verify=_x19,
  explain=r"Opens downward, so \(a<0\), not \(a>0\). The vertex is in Quadrant II, so its \(x\)-coordinate \(-\frac{b}{2a}\) is negative. "
          r"Since \(2a<0\), \(-\frac{b}{2a}<0\) means \(\frac{b}{2a}>0\), so \(b\) has the same sign as \(a\): \(b<0\). "
          r"The \(y\)-intercept \(c\) can be positive or negative, depending on how high the vertex is and how steep the parabola is, so \(c>0\) is not guaranteed.")

def _x20():
    X = [10, 12, 14, 16, 18]; Y = [6, 12, 14, 16, 22]
    same_mean = statistics.mean(X) == statistics.mean(Y)
    return "C" if same_mean and statistics.pstdev(Y) > statistics.pstdev(X) else "?"

Q(id="PSD-26", domain="PSD", skill="One-variable data: distributions and measures of center and spread", diff=1, desmos=False,
  stem=r"Data set X consists of the values 10, 12, 14, 16, and 18. Data set Y consists of the values 6, 12, 14, 16, and 22. Which of the following is true?",
  choices=["The data sets have different means, and the standard deviation of X is greater.",
           "The data sets have the same mean, and the standard deviation of X is greater.",
           "The data sets have the same mean, and the standard deviation of Y is greater.",
           "The data sets have the same mean and the same standard deviation."],
  answer="C", verify=_x20,
  explain=r"Both sums are 70, so both means are 14. The two sets differ only in their end values: Y's extreme values (6 and 22) are farther from 14 than X's (10 and 18), so Y is more spread out and has the greater standard deviation.")

Q(id="GEO-28", domain="GEO", skill="Lines, angles, and triangles", diff=2, desmos=False,
  stem=r"Two parallel lines are intersected by a transversal. Two same-side interior angles formed by the transversal have measures \((5x+10)^\circ\) and \((3x+30)^\circ\). What is the value of \(x\)?",
  answer="35/2", verify=lambda: solve(Eq(5*x + 10 + 3*x + 30, 180), x)[0],
  explain=r"Same-side interior angles between parallel lines are supplementary: \((5x+10)+(3x+30)=180\). So \(8x=140\) and \(x=17.5\). "
          r"(Setting the angles <em>equal</em> is the trap; that applies to alternate interior angles.)")

def _x22():
    n = 0
    while 1500*R(104, 100)**n <= 2500:
        n += 1
    return n

Q(id="ADV-39", domain="ADV", skill=NF, diff=3, desmos=True,
  stem=r"The function \(p(t)=1{,}500(1.04)^{t}\) gives the value, in dollars, of an investment \(t\) years after it was made. What is the least whole number of years after which the value of the investment is greater than $2,500?",
  answer="14", verify=_x22,
  explain=r"Solve \(1500(1.04)^t>2500\), which is \((1.04)^t>\frac53\). Test values: \(1.04^{13}\approx1.665\), and \(1500(1.665)\approx2{,}497.60\), which is just <em>below</em> 2,500. "
          r"\(1.04^{14}\approx1.732\), and \(1500(1.732)\approx2{,}597.70\). So the answer is 14. (13 is the trap.)",
  tip=r"Graph \(y=1500(1.04)^x\) and \(y=2500\). The intersection is at \(x\approx13.02\), so the first <em>whole</em> year above 2,500 is 14.")

def _x23():
    sols = [s for s in solve(Eq(3*(x - 2), x + 4), x) if s >= 2] + [s for s in solve(Eq(-3*(x - 2), x + 4), x) if s < 2]
    assert len(sols) == 2
    return sum(sols)

Q(id="ADV-40", domain="ADV", skill=NE, diff=3, desmos=True,
  stem=r"In the \(xy\)-plane, the graphs of \(y=3|x-2|\) and \(y=x+4\) intersect at two points. What is the sum of the \(x\)-coordinates of the two points?",
  answer="11/2", verify=_x23,
  explain=r"Case \(x\ge2\): \(3(x-2)=x+4\), so \(2x=10\) and \(x=5\). Case \(x<2\): \(-3(x-2)=x+4\), so \(-3x+6=x+4\) and \(x=\frac12\). Both satisfy their case conditions. Sum: \(5+\frac12=\frac{11}{2}=5.5\).",
  tip=r"Graph both. Click the two intersections, \((0.5,4.5)\) and \((5,9)\), and add the \(x\)-coordinates: 5.5.")

Q(id="PSD-27", domain="PSD", skill="Percentages", diff=3, desmos=False,
  stem=r"In 2020, 30% of a company's employees worked remotely. In 2022, the number of employees was 25% greater than in 2020, and the number of employees who worked remotely was 60% greater than in 2020. What percent of the company's employees worked remotely in 2022?",
  choices=["36%", "38.4%", "48%", "54%"], vals=[36, R(384, 10), 48, 54], answer="B",
  verify=lambda: R(30, 100)*R(160, 100) / R(125, 100) * 100,
  explain=r"Imagine 100 employees in 2020, 30 of them remote. In 2022: \(125\) employees and \(30\times1.6=48\) remote. Percent: \(\frac{48}{125}=0.384=38.4\%\). "
          r"48% is the trap: 48 is the number of remote workers, but there are 125 employees, not 100.")

Q(id="GEO-29", domain="GEO", skill="Area and volume", diff=3, desmos=False,
  stem=r"A right circular cone has a height of 12 centimeters and a slant height of 13 centimeters. A cylinder has the same base radius as the cone and the same volume as the cone. What is the height, in centimeters, of the cylinder?",
  choices=[r"\(4\)", r"\(5\)", r"\(12\)", r"\(36\)"], vals=[4, 5, 12, 36], answer="A",
  verify=lambda: R(1, 3)*12,
  explain=r"The cone's radius is \(\sqrt{13^2-12^2}=5\), but you don't actually need it: equal volumes with equal radii give \(\pi r^2h=\frac13\pi r^2(12)\), so \(h=4\). "
          r"(The slant height is extra information. 5 is the trap: that's the radius.)")

Q(id="ALG-28", domain="ALG", skill=ALG["IN"], diff=3, desmos=True,
  stem=r"\[y\le -2x+10\]\[y\ge \tfrac12x\]\[x\ge0\]In the \(xy\)-plane, the solution region of the given system of inequalities is a triangle. What is the greatest possible \(y\)-coordinate of any point in the solution region?",
  answer="10",
  verify=lambda: max(vy for (vx, vy) in [(0, 0), (0, 10), tuple(solve([Eq(y, -2*x + 10), Eq(y, x/2)], [x, y]).values())]),
  explain=r"The vertices of the triangle are where the boundary lines meet: \((0,0)\) from \(y=\frac12x\) and \(x=0\); \((0,10)\) from \(y=-2x+10\) and \(x=0\); "
          r"and \((4,2)\) from \(-2x+10=\frac12x\). The greatest \(y\)-value in a triangle occurs at a vertex: 10.",
  tip=r"Graph all three inequalities. The overlap is a triangle with corners \((0,0)\), \((4,2)\), and \((0,10)\). The highest point is \((0,10)\).")

# ---------------------------------------------------------------------------
# Strengthen thinly covered skills.
D2 = "Two-variable data: models and scatterplots"
PRB = "Probability and conditional probability"
EVC = "Evaluating statistical claims: observational studies and experiments"

Q(id="PSD-28", domain="PSD", skill=D2, diff=1, desmos=True,
  stem=r"A line of best fit for a scatterplot passes through the points \((2,14)\) and \((10,46)\). Based on the line of best fit, what is the predicted value of \(y\) when \(x=7\)?",
  answer="34", verify=lambda: (lambda sl: 14 + sl*(7 - 2))(R(46 - 14, 10 - 2)),
  explain=r"Slope: \(\frac{46-14}{10-2}=4\). Line: \(y=14+4(x-2)=4x+6\). At \(x=7\): \(y=34\).",
  tip=r"Plot the two points, type <code>y=m(x-2)+14</code> with \(m=4\), and click the line at \(x=7\) (or type <code>4(7)+6</code>).")

def _x28():
    bb = sqrt(R(867, 1200))
    return round(float(1200*bb**4))

Q(id="PSD-29", domain="PSD", skill=D2, diff=3, desmos=True,
  stem=r"An exponential model of the form \(y=ab^{x}\), where \(a\) and \(b\) are positive constants, is fit to a scatterplot. The model predicts \(y=1{,}200\) when \(x=0\) and \(y=867\) when \(x=2\). Which of the following is closest to the value of \(y\) that the model predicts when \(x=4\)?",
  choices=[r"\(534\)", r"\(600\)", r"\(626\)", r"\(650\)"], vals=[534, 600, 626, 650], answer="C", verify=_x28,
  explain=r"\(a=1200\). Then \(b^2=\frac{867}{1200}=0.7225\), so \(b=0.85\). At \(x=4\): \(y=1200(b^2)^2=1200(0.7225)^2\approx626.4\). "
          r"534 is the trap from treating the model as linear (subtracting 333 twice).",
  tip=r"Make a table with \((0,1200)\) and \((2,867)\), then type <code>y_1 ~ a b^{x_1}</code>. Desmos finds \(a=1200\), \(b=0.85\). Evaluate <code>1200(0.85)^4</code>.")

Q(id="PSD-30", domain="PSD", skill=PRB, diff=2, desmos=False,
  stem=r"A club has 120 members: 45 juniors and 75 seniors. Of the juniors, 18 play a musical instrument; of the seniors, 42 play a musical instrument. If a member who does <em>not</em> play a musical instrument is selected at random, what is the probability that the member is a junior?",
  answer="9/20", verify=lambda: R(45 - 18, (45 - 18) + (75 - 42)),
  explain=r"Members who don't play: juniors \(45-18=27\), seniors \(75-42=33\), total 60. Probability of a junior: \(\frac{27}{60}=\frac{9}{20}=0.45\). "
          r"(\(\frac{27}{120}\) and \(\frac{27}{45}\) are the traps; the condition limits the group to the 60 non-players.)")

Q(id="PSD-31", domain="PSD", skill=PRB, diff=3, desmos=False,
  stem=r"An integer from 1 to 60, inclusive, is selected at random. What is the probability that the integer is a multiple of 4 or a multiple of 6 (or both)?",
  answer="1/3", verify=lambda: R(sum(1 for n in range(1, 61) if n % 4 == 0 or n % 6 == 0), 60),
  explain=r"Multiples of 4: 15. Multiples of 6: 10. Multiples of both, which are the multiples of 12: 5, and these were counted twice. "
          r"Total: \(15+10-5=20\). Probability: \(\frac{20}{60}=\frac13\). Acceptable entries include 1/3, .3333, and 0.333.")

Q(id="PSD-32", domain="PSD", skill=EVC, diff=2, desmos=False, reasoning=True,
  stem=r"Researchers surveyed 1,000 randomly selected adults in a country. Adults who reported walking at least 30 minutes per day had lower average blood pressure than adults who did not. Which of the following is the most appropriate conclusion?",
  choices=["Walking at least 30 minutes per day causes lower blood pressure for adults in the country.",
           "There is an association between daily walking and lower blood pressure for adults in the country, but a cause-and-effect conclusion can't be made.",
           "There is an association between daily walking and lower blood pressure for all adults in the world.",
           "No conclusion about adults in the country can be made, because the adults were not assigned to walk."],
  answer="B", verify=None,
  explain=r"The adults were randomly <em>selected</em>, so the results generalize to adults in that country. But they were not randomly <em>assigned</em> to walk; this is an observational study. "
          r"So it shows an association, not cause and effect. (Other differences, such as diet or age, could explain the pattern.) The claim about all adults in the world over-generalizes, and an association can still be concluded without assignment.")

Q(id="PSD-33", domain="PSD", skill=EVC, diff=2, desmos=False, reasoning=True,
  stem=r"A principal wants to know whether a new online study tool improves test scores for the students at her school. Which of the following study designs would best allow her to conclude that using the tool <em>causes</em> higher scores for students at the school?",
  choices=["Let students choose whether to use the tool, then compare the scores of users and nonusers.",
           "Select a random sample of students at the school, randomly assign half of them to use the tool and half not to, and compare the scores of the two groups.",
           "Have every student in one class use the tool, and compare that class's scores with another class's scores.",
           "Ask students who already use the tool whether they think it improved their scores."],
  answer="B", verify=None,
  explain=r"A cause-and-effect conclusion requires random <em>assignment</em> to the treatment, and generalizing to the school requires a random <em>sample</em> from the school. "
          r"Letting students choose introduces self-selection: motivated students may both use the tool and score higher. Comparing two existing classes confounds the tool with the teacher and class. Self-reports measure opinions, not scores.")
