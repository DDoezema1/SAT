"""Top-band questions (aimed at students scoring 700+), mostly designed around Desmos.

These target the kinds of items that separate a 740 from a 790: parameter conditions
(tangency, number of solutions), regressions, systems with messy coefficients, and
statistics computed from lists, where a fluent Desmos user is far faster than algebra.
"""
import math
import statistics
from fractions import Fraction as F
from sympy import (Rational as R, symbols, solve, Eq, sqrt, Poly, real_roots, Point, Line, Circle,
                   reduce_inequalities, Interval, oo)
from .common import Q

x, y, a, b, c, k, m = symbols("x y a b c k m")

LF = "Linear functions"
L2 = "Linear equations in two variables"
SY = "Systems of two linear equations in two variables"
IN = "Linear inequalities in one or two variables"
EQ = "Equivalent expressions"
NE = "Nonlinear equations in one variable and systems of equations in two variables"
NF = "Nonlinear functions"
D1 = "One-variable data: distributions and measures of center and spread"
D2 = "Two-variable data: models and scatterplots"
CI = "Circles"
RT = "Right triangles and trigonometry"
LT = "Lines, angles, and triangles"


def _distinct_real(expr):
    return len(set(real_roots(Poly(expr, x))))


# --------------------------------------------------------------------------- Advanced Math
def _t01():
    bb = [v for v in solve(Eq(b**2 - 4*2*18, 0), b) if v < 0][0]
    roots = solve(2*x**2 + bb*x + 18, x)
    assert len(set(roots)) == 1
    return roots[0]

Q(id="TOP-01", domain="ADV", skill=NF, diff=3, desmos=True,
  stem=r"In the \(xy\)-plane, the graph of \(y=2x^2+bx+18\), where \(b\) is a negative constant, has exactly one \(x\)-intercept. What is the \(x\)-coordinate of that \(x\)-intercept?",
  answer="3", verify=_t01,
  explain=r"Exactly one \(x\)-intercept means the vertex sits on the \(x\)-axis: discriminant \(b^2-4(2)(18)=0\), so \(b^2=144\) and \(b=-12\) (negative). "
          r"The intercept is the vertex: \(x=-\frac{b}{2a}=\frac{12}{4}=3\). Check: \(2x^2-12x+18=2(x-3)^2\).",
  tip=r"Graph \(y=2x^2+bx+18\) and add a slider for \(b\) (set its range to about \(-20\) to \(0\)). Drag until the parabola just touches the \(x\)-axis (\(b=-12\)), then click the touching point: \((3,0)\).")

def _t02():
    good = [cv for cv in range(-60, 60) if _distinct_real(x**3 - 3*x**2 - 9*x + cv) == 3]
    return max(good)

Q(id="TOP-02", domain="ADV", skill=NF, diff=3, desmos=True,
  stem=r"\[f(x)=x^3-3x^2-9x+c\]In the given function, \(c\) is a constant. The equation \(f(x)=0\) has exactly three distinct real solutions. What is the greatest possible integer value of \(c\)?",
  answer="26", verify=_t02,
  explain=r"A cubic crosses the \(x\)-axis three times only if its local maximum is above the axis and its local minimum is below it. "
          r"The turning points of \(x^3-3x^2-9x\) are at \(x=-1\) (local max, value 5) and \(x=3\) (local min, value \(-27\)). Adding \(c\) shifts the graph up by \(c\): "
          r"we need \(5+c>0\) and \(-27+c<0\), so \(-5<c<27\). The greatest integer is 26. (At \(c=27\), the minimum touches the axis, giving only two distinct solutions.)",
  tip=r"Graph \(y=x^3-3x^2-9x+c\) with a slider for \(c\). Click the two turning points: their \(y\)-values are \(5+c\) and \(c-27\). Slide \(c\) up until the low point touches the axis at \(c=27\); the greatest integer just below that is 26.")

def _t03():
    f = lambda t: 2**t - t*t
    xs = [-20 + 0.0137*i for i in range(int(40/0.0137))]
    changes = sum(1 for u, v in zip(xs, xs[1:]) if f(u)*f(v) < 0)
    # for x > 20, 2^x grows far faster than x^2, so there are no more crossings
    return changes

Q(id="TOP-03", domain="ADV", skill=NE, diff=3, desmos=True,
  stem=r"How many real solutions does the equation \(2^{x}=x^{2}\) have?",
  choices=["One", "Two", "Three", "Four"], vals=[1, 2, 3, 4], answer="C", verify=_t03,
  explain=r"Two solutions are easy to spot: \(x=2\) (\(4=4\)) and \(x=4\) (\(16=16\)). The trap is missing the third: for negative \(x\), \(2^x\) is between 0 and 1 while \(x^2\) grows, "
          r"so the graphs cross once more, near \(x\approx-0.77\). For \(x>4\), \(2^x\) stays above \(x^2\). Total: three.",
  tip=r"Graph \(y=2^x\) and \(y=x^2\) and count the gray intersection dots. Zoom out a little: the negative-\(x\) crossing near \(-0.77\) is easy to miss if you only look at \(x>0\).")

def _t05():
    def count(kv):
        sols = set()
        x1 = 2*(kv + 3)              # x >= 3:  x - 3 = x/2 + k
        if x1 >= 3: sols.add(x1)
        x2 = (3 - kv)/R(3, 2)        # x < 3:   3 - x = x/2 + k
        if x2 < 3: sols.add(x2)
        return len(sols)
    ks = [R(n, 10) for n in range(-60, 61) if count(R(n, 10)) == 1]
    assert len(ks) == 1, ks
    return ks[0]

Q(id="TOP-05", domain="ADV", skill=NE, diff=3, desmos=True,
  stem=r"In the \(xy\)-plane, the graph of \(y=|x-3|\) and the graph of \(y=\frac12x+k\), where \(k\) is a constant, intersect at exactly one point. What is the value of \(k\)?",
  answer="-3/2", verify=_t05,
  explain=r"The V-shaped graph has its vertex at \((3,0)\) and arms with slopes \(\pm1\). The line has slope \(\frac12\), which is less steep than either arm. "
          r"If the line is above the vertex, it crosses both arms (two points); if it's below, it misses the V entirely. Exactly one intersection happens only when the line passes through the vertex: "
          r"\(0=\frac12(3)+k\), so \(k=-\frac32=-1.5\).",
  tip=r"Graph \(y=|x-3|\) and \(y=0.5x+k\) with a slider. Watch the number of intersections change from 2 to 0 as \(k\) decreases. The switch happens when the line hits the vertex, at \(k=-1.5\).")

def _t07():
    d = R(-1, 2)*x**2 + 6*x - 10 - (2*x - 4)
    xv = solve(d.diff(x), x)[0]
    return d.subs(x, xv)

Q(id="TOP-07", domain="ADV", skill=NF, diff=2, desmos=True,
  stem=r"The functions \(f\) and \(g\) are defined by \(f(x)=-0.5x^2+6x-10\) and \(g(x)=2x-4\). What is the maximum value of \(f(x)-g(x)\)?",
  answer="2", verify=_t07,
  explain=r"\(f(x)-g(x)=-0.5x^2+4x-6\). The vertex is at \(x=-\frac{4}{2(-0.5)}=4\), and the value there is \(-8+16-6=2\).",
  tip=r"Define \(f(x)\) and \(g(x)\) in Desmos, then graph \(y=f(x)-g(x)\) and click its highest point: \((4,2)\). Don't stop at the maximum of \(f\) alone.")

def _t09():
    sol = solve([Eq(a + b, 7), Eq(a*R(3, 2)**2 + b, 12)], [a, b])
    return sol[a]*R(3, 2)**4 + sol[b]

Q(id="TOP-09", domain="ADV", skill=NF, diff=3, desmos=True,
  stem=r"The function \(f\) is defined by \(f(x)=a(1.5)^{x}+b\), where \(a\) and \(b\) are constants. The graph of \(y=f(x)\) passes through the points \((0,7)\) and \((2,12)\). What is the value of \(f(4)\)?",
  answer="93/4", verify=_t09,
  explain=r"\(f(0)=a+b=7\) and \(f(2)=2.25a+b=12\). Subtracting gives \(1.25a=5\), so \(a=4\) and \(b=3\). Then \(f(4)=4(1.5)^4+3=4(5.0625)+3=23.25\).",
  tip=r"Make a table with \(x_1\): 0, 2 and \(y_1\): 7, 12. Type <code>y_1 ~ a(1.5)^{x_1} + b</code>. Desmos fits \(a=4\), \(b=3\) exactly. Then type <code>4(1.5)^4+3</code> to get 23.25. Regression with your own model form works for any family of curves.")

def _t10():
    eqs = {"A": x**3 - 3*x + 3, "B": x**3 - 3*x + 1, "C": x**3 - 3*x + 2, "D": x**3 - 3*x + 5}
    good = [L for L, e in eqs.items() if _distinct_real(e) == 2]
    assert len(good) == 1
    return good[0]

Q(id="TOP-10", domain="ADV", skill=NE, diff=3, desmos=True,
  stem=r"Which of the following equations has exactly two distinct real solutions?",
  choices=[r"\(x^3-3x+3=0\)", r"\(x^3-3x+1=0\)", r"\(x^3-3x+2=0\)", r"\(x^3-3x+5=0\)"], answer="C", verify=_t10,
  explain=r"The graph of \(y=x^3-3x\) has a local maximum of 2 (at \(x=-1\)) and a local minimum of \(-2\) (at \(x=1\)). Adding a constant \(d\) shifts it up. "
          r"With \(d=2\), the local minimum is exactly 0, so the graph touches the axis at \(x=1\) and crosses it once more: \(x^3-3x+2=(x-1)^2(x+2)\), with two distinct solutions. "
          r"\(d=1\) gives three solutions; \(d=3\) and \(d=5\) give one.",
  tip=r"Type all four left sides into Desmos as \(y=\dots\) and count each graph's \(x\)-intercepts. Only \(y=x^3-3x+2\) touches at one point and crosses at another.")

Q(id="TOP-14", domain="ADV", skill=NF, diff=3, desmos=False,
  stem=r"The polynomial \(p(x)=x^3+ax^2+bx-6\), where \(a\) and \(b\) are constants, has \(x-3\) and \(x+1\) as factors. What is the value of \(a+b\)?",
  answer="-7", verify=lambda: (lambda s: s[a] + s[b])(solve([Eq((x**3 + a*x**2 + b*x - 6).subs(x, 3), 0), Eq((x**3 + a*x**2 + b*x - 6).subs(x, -1), 0)], [a, b])),
  explain=r"\(p(3)=27+9a+3b-6=0\) gives \(3a+b=-7\). \(p(-1)=-1+a-b-6=0\) gives \(a-b=7\). Adding: \(4a=0\), so \(a=0\) and \(b=-7\). So \(a+b=-7\). "
          r"(Shortcut: for this cubic the product of the roots is 6, so \(3\cdot(-1)\cdot r=6\) gives a third root \(r=-2\) and \(p(x)=(x-3)(x+1)(x+2)\). "
          r"Then \(p(1)=(-2)(2)(3)=-12\), and also \(p(1)=1+a+b-6\), so \(a+b=-7\).)")

Q(id="TOP-15", domain="ADV", skill=NF, diff=2, desmos=True,
  stem=r"The function \(f\) is defined by \(f(x)=3x^2-12x+k\), where \(k\) is a constant. The minimum value of \(f(x)\) is 5. What is the value of \(k\)?",
  choices=[r"\(5\)", r"\(12\)", r"\(17\)", r"\(29\)"], vals=[5, 12, 17, 29], answer="C",
  verify=lambda: solve(Eq((3*x**2 - 12*x + k).subs(x, 2), 5), k)[0],
  explain=r"The minimum occurs at the vertex, \(x=\frac{12}{6}=2\): \(f(2)=12-24+k=k-12\). Setting \(k-12=5\) gives \(k=17\).",
  tip=r"Graph \(y=3x^2-12x+k\) with a slider and click the vertex. Adjust \(k\) until the vertex's \(y\)-value is 5.")

def _t16():
    cc = solve(Eq((400 - 16*(23 - c)), (3*4)**2), c)[0]
    r = solve(4*x**2 - 20*x + 23 - cc, x)
    assert abs(r[0] - r[1]) == 3
    return cc

Q(id="TOP-16", domain="ADV", skill=NE, diff=3, desmos=True,
  stem=r"In the \(xy\)-plane, the line \(y=c\), where \(c\) is a constant, intersects the parabola \(y=4x^2-20x+23\) at two points that are 3 units apart. What is the value of \(c\)?",
  answer="7", verify=_t16,
  explain=r"The parabola is symmetric about \(x=\frac{20}{8}=2.5\), so two points 3 units apart are at \(x=2.5\pm1.5\), which is \(x=1\) and \(x=4\). "
          r"Then \(c=4(1)^2-20(1)+23=7\). Check: \(4(16)-80+23=7\). ✓",
  tip=r"Graph the parabola and \(y=c\) with a slider. Click the two intersections and adjust \(c\) until their \(x\)-values are 3 apart (1 and 4): \(c=7\).")

def _t17():
    n = 0
    while R(1045, 1000)**n < 2:
        n += 1
    return n

Q(id="TOP-17", domain="ADV", skill=NF, diff=2, desmos=True,
  stem=r"An investment earns 4.5% interest, compounded annually. What is the least whole number of years after which the value of the investment will be at least double its initial value?",
  choices=[r"\(14\)", r"\(15\)", r"\(16\)", r"\(22\)"], vals=[14, 15, 16, 22], answer="C", verify=_t17,
  explain=r"Solve \(1.045^n\ge2\). \(1.045^{15}\approx1.935\), which is not yet double, and \(1.045^{16}\approx2.022\). So 16 years. "
          r"(22 is the trap from \(100\div4.5\), which ignores compounding.)",
  tip=r"Graph \(y=1.045^x\) and \(y=2\). They intersect at \(x\approx15.75\), so the first whole year is 16.")

Q(id="TOP-21", domain="ADV", skill=NF, diff=2, desmos=False,
  stem=r"The function \(f\) is defined by \(f(x)=x^2-6x+5\). The function \(g\) is defined by \(g(x)=f(x-k)\), where \(k\) is a constant. The \(x\)-intercepts of the graph of \(y=g(x)\) are at \(x=4\) and \(x=8\). What is the value of \(k\)?",
  choices=[r"\(-3\)", r"\(2\)", r"\(3\)", r"\(7\)"], vals=[-3, 2, 3, 7], answer="C",
  verify=lambda: (lambda zs: 4 - min(zs))(solve(x**2 - 6*x + 5, x)),
  explain=r"\(f(x)=(x-1)(x-5)\) has zeros 1 and 5. \(f(x-k)\) shifts the graph \(k\) units to the right, so the zeros become \(1+k\) and \(5+k\). These equal 4 and 8 when \(k=3\). "
          r"(\(-3\) is the trap from shifting in the wrong direction.)")

# --------------------------------------------------------------------------- Algebra
def _t04():
    lines = [Eq(y, 3*x + 2), Eq(y, -x + 10), Eq(y, 0)]
    best = None
    for i in range(3):
        for j in range(i + 1, 3):
            s = solve([lines[i], lines[j]], [x, y])
            if not s: continue
            X, Y = s[x], s[y]
            if Y <= 3*X + 2 and Y <= -X + 10 and Y >= 0:
                v = 2*X + Y
                best = v if best is None else max(best, v)
    return best

Q(id="TOP-04", domain="ALG", skill=IN, diff=3, desmos=True,
  stem=r"\[y\le3x+2\]\[y\le-x+10\]\[y\ge0\]Point \((x,y)\) lies in the solution region of the given system of inequalities. What is the maximum possible value of \(2x+y\)?",
  answer="20", verify=_t04,
  explain=r"The region is a triangle with vertices \(\left(-\frac23,0\right)\), \((2,8)\), and \((10,0)\). A linear expression like \(2x+y\) is greatest at a vertex: "
          r"\(-\frac43\), \(12\), and \(20\). The maximum is 20, at \((10,0)\). The trap is assuming the &ldquo;top&rdquo; corner \((2,8)\) wins.",
  tip=r"Graph the three inequalities and click the corners of the shaded triangle. Then evaluate \(2x+y\) at each corner. You can also graph \(2x+y=c\) with a slider and push \(c\) up until the line just leaves the region.")

Q(id="TOP-11", domain="ALG", skill=SY, diff=2, desmos=True,
  stem=r"\[0.35x+1.2y=8.95\]\[2.4x-0.75y=7.5\]If \((x,y)\) is the solution to the given system of equations, what is the value of \(xy\)?",
  answer="30",
  verify=lambda: (lambda s: s[x]*s[y])(solve([Eq(R(35, 100)*x + R(12, 10)*y, R(895, 100)), Eq(R(24, 10)*x - R(75, 100)*y, R(75, 10))], [x, y])),
  explain=r"Solving by elimination works but is slow with these decimals: the solution is \((5,6)\), so \(xy=30\).",
  tip=r"Don't do this by hand. Type both equations into Desmos exactly as written and click the intersection: \((5,6)\). Total time: about 20 seconds.")

def _t19():
    sol = solve(Eq(m*(3*x + 1) + c, 6*x + 11), [m, c], dict=True)[0]
    return sol[m]*7 + sol[c]

Q(id="TOP-19", domain="ALG", skill=LF, diff=3, desmos=False,
  stem=r"The function \(f\) is linear, and \(f(3x+1)=6x+11\) for all values of \(x\). What is the value of \(f(7)\)?",
  answer="23", verify=_t19,
  explain=r"Fast route: find the \(x\) that makes the input equal 7. \(3x+1=7\) gives \(x=2\), so \(f(7)=6(2)+11=23\). "
          r"(General route: let \(u=3x+1\); then \(x=\frac{u-1}{3}\) and \(f(u)=2(u-1)+11=2u+9\).)")

Q(id="TOP-24", domain="ALG", skill=SY, diff=2, desmos=True,
  stem=r"\[y=\tfrac23x+4\]\[y=kx-2\]In the given system of equations, \(k\) is a constant. The solution to the system has an \(x\)-coordinate of 9. What is the value of \(k\)?",
  answer="4/3", verify=lambda: solve(Eq(k*9 - 2, R(2, 3)*9 + 4), k)[0],
  explain=r"At \(x=9\), the first equation gives \(y=6+4=10\). That point is on the second line: \(10=9k-2\), so \(k=\frac{12}{9}=\frac43\). Acceptable entries include 4/3 and 1.333.",
  tip=r"Graph \(y=\frac23x+4\) and \(y=kx-2\) with a slider for \(k\). Adjust until the intersection is at \(x=9\). Or click the first line at \(x=9\) to get \(y=10\), then solve.")

def _t25():
    kk = solve(Eq((4 - k)/3, -2), k)[0]
    sol = reduce_inequalities(4 - 3*x <= kk, x)
    assert sol == (x >= -2) or str(sol) in ("(-2 <= x) & (x < oo)",), sol
    return kk

Q(id="TOP-25", domain="ALG", skill=IN, diff=2, desmos=False,
  stem=r"The solutions to the inequality \(4-3x\le k\), where \(k\) is a constant, are all values of \(x\) such that \(x\ge-2\). What is the value of \(k\)?",
  answer="10", verify=_t25,
  explain=r"\(4-3x\le k\) gives \(-3x\le k-4\). Dividing by \(-3\) flips the inequality: \(x\ge\frac{4-k}{3}\). Setting \(\frac{4-k}{3}=-2\) gives \(k=10\). "
          r"Check: \(4-3x\le10\) gives \(x\ge-2\). ✓")

def _t26():
    s = solve([Eq(3*x - y, 7), Eq(x + 2*y, 7)], [x, y])
    return (s[y] - (-4)) / (s[x] - 1)

Q(id="TOP-26", domain="ALG", skill=L2, diff=2, desmos=True,
  stem=r"A line in the \(xy\)-plane passes through the point \((1,-4)\) and through the point where the graphs of \(3x-y=7\) and \(x+2y=7\) intersect. What is the slope of the line?",
  answer="3", verify=_t26,
  explain=r"Solve the system: \(y=3x-7\), so \(x+2(3x-7)=7\), \(7x=21\), \(x=3\), \(y=2\). Slope from \((1,-4)\) to \((3,2)\): \(\frac{2-(-4)}{3-1}=3\).",
  tip=r"Graph both equations and click the intersection, \((3,2)\). Then compute the slope from \((1,-4)\).")

# --------------------------------------------------------------------------- Problem-Solving & Data
def _t06():
    old = [12, 15, 15, 18, 21, 24, 26, 29, 33, 37]
    new = old[:-1] + [47]
    I = abs(statistics.mean(new) - statistics.mean(old) - 1) < 1e-12
    II = statistics.median(new) == statistics.median(old)
    III = statistics.pstdev(new) > statistics.pstdev(old)
    return {(True, True, False): "A", (True, False, True): "B", (False, True, True): "C", (True, True, True): "D"}[(I, II, III)]

Q(id="TOP-06", domain="PSD", skill=D1, diff=2, desmos=True,
  stem=r"A data set consists of the values 12, 15, 15, 18, 21, 24, 26, 29, 33, and 37. The value 37 is replaced with 47. Which of the following statements about the new data set, compared with the original, are true?"
       r"<p style='margin:10px 0 0 18px;line-height:1.9'>I. The mean increases by 1.<br>II. The median does not change.<br>III. The standard deviation increases.</p>",
  choices=["I and II only", "I and III only", "II and III only", "I, II, and III"], answer="D", verify=_t06,
  explain=r"I: the sum increases by 10 across 10 values, so the mean increases by \(\frac{10}{10}=1\). ✓ "
          r"II: the median is the average of the 5th and 6th values (21 and 24), and neither changes. ✓ "
          r"III: the largest value moves farther from the mean, so the spread increases. ✓",
  tip=r"Type <code>A=[12,15,15,18,21,24,26,29,33,37]</code> and <code>B=[12,15,15,18,21,24,26,29,33,47]</code>, then compare <code>mean(A)</code>, <code>mean(B)</code>, <code>median(A)</code>, <code>median(B)</code>, <code>stdev(A)</code>, and <code>stdev(B)</code>. That checks all three statements in about 30 seconds.")

def _t12():
    pts = [(0, 3), (1, 2), (2, 3), (3, 6), (4, 11)]
    sol = solve([Eq(a*p**2 + b*p + c, q) for p, q in pts[:3]], [a, b, c])
    for p, q in pts:
        assert sol[a]*p**2 + sol[b]*p + sol[c] == q
    return sol[a]*49 + sol[b]*7 + sol[c]

Q(id="TOP-12", domain="PSD", skill=D2, diff=2, desmos=True,
  stem=r"The table shows five data points that lie exactly on the graph of a quadratic function."
       r"<table class='data'><tr><th>\(x\)</th><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr>"
       r"<tr><th>\(y\)</th><td>3</td><td>2</td><td>3</td><td>6</td><td>11</td></tr></table>"
       r"What is the value of \(y\) when \(x=7\)?",
  answer="38", verify=_t12,
  explain=r"The \(y\)-values change by \(-1,1,3,5\); the second differences are constant at 2, so \(a=\frac22=1\). With \(c=3\) (the value at \(x=0\)) and \(1+b+3=2\), \(b=-2\). "
          r"So \(y=x^2-2x+3\), and at \(x=7\): \(49-14+3=38\).",
  tip=r"Enter the table in Desmos and type <code>y_1 ~ a x_1^2 + b x_1 + c</code>. Desmos gives \(a=1\), \(b=-2\), \(c=3\) with \(R^2=1\). Evaluate at 7.")

def _t20():
    best = None
    for A in range(1, 14):
        for B_ in range(A, 14):
            for D in range(13, 61):
                E = 60 - A - B_ - 13 - D
                if E < D: continue
                vals = [A, B_, 13, D, E]
                counts = {v: vals.count(v) for v in vals}
                if counts.get(15, 0) and all(counts[15] > n for v, n in counts.items() if v != 15):
                    best = A if best is None else max(best, A)
    return best

Q(id="TOP-20", domain="PSD", skill=D1, diff=3, desmos=False,
  stem=r"A list of 5 positive integers has a mean of 12 and a median of 13. The list has a unique mode of 15. What is the greatest possible value of the smallest integer in the list?",
  answer="8", verify=_t20,
  explain=r"The sum is \(5\times12=60\). In order, the list is \(a\le b\le13\le d\le e\). A unique mode of 15 needs at least two 15s, and both must be above the median, so \(d=e=15\). "
          r"Then \(a+b=60-13-30=17\). For 15 to be the <em>unique</em> mode, \(a\neq b\) and \(b\neq13\). Making \(a\) as large as possible with \(a<b\): \(a=8\), \(b=9\).")

def _t23():
    sets = {"A": [2, 4, 6, 8, 10], "B": [1, 5, 6, 7, 11], "C": [4, 5, 6, 7, 8], "D": [1, 1, 6, 11, 11]}
    sd = {L: statistics.pstdev(v) for L, v in sets.items()}
    return max(sd, key=sd.get)

Q(id="TOP-23", domain="PSD", skill=D1, diff=2, desmos=True,
  stem=r"Each of the following data sets has a mean of 6. Which data set has the greatest standard deviation?",
  choices=["2, 4, 6, 8, 10", "1, 5, 6, 7, 11", "4, 5, 6, 7, 8", "1, 1, 6, 11, 11"], answer="D", verify=_t23,
  explain=r"Standard deviation measures typical distance from the mean. In 1, 1, 6, 11, 11, four of the five values are 5 away from the mean, more than in any other set. "
          r"(1, 5, 6, 7, 11 has the same range, but most of its values are clustered near 6.)",
  tip=r"Type <code>stdev([1,1,6,11,11])</code> (and the same for each set) into Desmos: 4.47 for D, compared with 3.16, 3.16, and 1.58. Desmos also has <code>mean()</code>, <code>median()</code>, and <code>stdevp()</code>.")

# --------------------------------------------------------------------------- Geometry & Trig
def _t08():
    return Point(4, 3).distance(Line(Point(0, 2), Point(4, -1)))

Q(id="TOP-08", domain="GEO", skill=CI, diff=3, desmos=True,
  stem=r"In the \(xy\)-plane, a circle with center \((4,3)\) and radius \(r\) is tangent to the line \(y=-\frac34x+2\). What is the value of \(r\)?",
  answer="16/5", verify=_t08,
  explain=r"The radius to a point of tangency is perpendicular to the tangent line, so \(r\) is the distance from \((4,3)\) to the line \(3x+4y-8=0\): "
          r"\(\frac{|3(4)+4(3)-8|}{\sqrt{3^2+4^2}}=\frac{16}{5}=3.2\).",
  tip=r"Graph \((x-4)^2+(y-3)^2=r^2\) with a slider for \(r\), plus the line. Increase \(r\) until the circle just touches the line: \(r=3.2\).")

Q(id="TOP-13", domain="GEO", skill=RT, diff=2, desmos=True,
  stem=r"In right triangle \(ABC\), angle \(B\) is a right angle, the measure of angle \(A\) is \(32^\circ\), and \(AC=25\). Which of the following is closest to the length of \(\overline{BC}\)?",
  choices=[r"\(12.5\)", r"\(13.2\)", r"\(15.6\)", r"\(21.2\)"], vals=[R(125, 10), R(132, 10), R(156, 10), R(212, 10)], answer="B",
  verify=lambda: R(str(round(25*math.sin(math.radians(32)), 1))),
  explain=r"\(\overline{AC}\) is the hypotenuse, and \(\overline{BC}\) is opposite angle \(A\): \(BC=25\sin32^\circ\approx13.2\). "
          r"21.2 comes from using cosine (that gives \(AB\)), and 15.6 comes from tangent.",
  tip=r"Make sure Desmos is in <b>degree</b> mode (wrench icon, then Degrees). Then type <code>25sin(32)</code>: 13.248. In radian mode you'd get a wrong answer, 13.8.")

def _t18():
    pts = solve([Eq(x**2 + y**2, 25), Eq((x - 6)**2 + y**2, 13)], [x, y])
    (x1, y1), (x2, y2) = pts
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

Q(id="TOP-18", domain="GEO", skill=CI, diff=3, desmos=True,
  stem=r"In the \(xy\)-plane, the circles \(x^2+y^2=25\) and \((x-6)^2+y^2=13\) intersect at two points. What is the distance between these two points?",
  answer="6", verify=_t18,
  explain=r"Subtract the equations: \(x^2-(x-6)^2=12\), so \(12x-36=12\) and \(x=4\). Then \(y^2=25-16=9\), so the points are \((4,3)\) and \((4,-3)\), which are 6 apart.",
  tip=r"Graph both circles and click the two intersections: \((4,3)\) and \((4,-3)\). They're 6 apart vertically.")

def _t22():
    T = Line(Point(10, 0), Point(4, 8))
    return Point(0, 0).distance(T)

Q(id="TOP-22", domain="GEO", skill=LT, diff=3, desmos=False,
  stem=r"In the \(xy\)-plane, a triangle has vertices at \((0,0)\), \((10,0)\), and \((4,8)\). What is the length of the altitude from \((0,0)\) to the opposite side?",
  answer="8", verify=_t22,
  explain=r"Area using the base on the \(x\)-axis: \(\frac12(10)(8)=40\). The side opposite \((0,0)\) runs from \((10,0)\) to \((4,8)\) and has length \(\sqrt{36+64}=10\). "
          r"The same area with that side as the base: \(\frac12(10)h=40\), so \(h=8\).")
