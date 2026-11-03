"""Harder math questions in the style of the College Board Question Bank's top band.

A sample of the official bank's hardest math questions (Hard, score band 7) showed that
much of their difficulty comes from traps and awkward numbers rather than advanced
concepts: percent-of-percent wording, "which function models this pricing plan" word
problems, squared and cubed unit conversions, messy-number geometry, and dependent systems
written with a parameter. These original questions target those patterns.
"""
import math
from sympy import Rational as R, symbols, solve, Eq, sqrt, expand, simplify, Poly, Point, Line, Circle
from .common import Q

x, y, r, p, w = symbols("x y r p w")

Q(id="HM-01", domain="PSD", skill="Percentages", diff=3, desmos=False,
  stem=r"The result of increasing the positive quantity \(x\) by \(250\%\) is \(91\). What is the value of \(x\)?",
  answer="26", verify=lambda: solve(Eq(x * (1 + R(250, 100)), 91), x)[0],
  explain=r"Increasing by 250% means adding 250% of \(x\) to \(x\) itself, so the result is \(x+2.5x=3.5x\). Then \(3.5x=91\) and \(x=26\). "
          r"The trap is \(2.5x=91\) (giving 36.4), which treats &ldquo;increasing by 250%&rdquo; as &ldquo;250% of.&rdquo;")

Q(id="HM-02", domain="PSD", skill="Percentages", diff=3, desmos=False,
  stem=r"The number \(a\) is \(35\%\) less than the positive number \(b\). The number \(c\) is \(80\%\) greater than \(a\). The number \(c\) is how many times \(b\)?",
  answer="117/100", verify=lambda: R(65, 100) * R(180, 100),
  explain=r"\(a=0.65b\) (35% less means 65% remains), and \(c=1.8a=1.8(0.65b)=1.17b\). So \(c\) is 1.17 times \(b\). "
          r"Adding the percents (\(-35+80=45\), giving 1.45) is the trap: each percent applies to a different base.")

Q(id="HM-03", domain="ALG", skill="Linear functions", diff=2, desmos=False,
  stem=r"A plumber charges \(\$95\) for the first hour of a job and \(\$62\) for each additional hour. Which function \(f\) gives the total charge, in dollars, for a job that takes \(x\) hours, where \(x\) is a whole number and \(x\ge1\)?",
  choices=[r"\(f(x)=62x+33\)", r"\(f(x)=62x+95\)", r"\(f(x)=95x+62\)", r"\(f(x)=62x-33\)"],
  vals=["62*x+33", "62*x+95", "95*x+62", "62*x-33"], answer="A",
  verify=lambda: 95 + 62 * (x - 1),
  explain=r"The first hour costs 95 and each of the remaining \(x-1\) hours costs 62: \(f(x)=95+62(x-1)=62x+33\). Check: \(f(1)=95\) ✓, \(f(2)=157\) ✓. "
          r"\(62x+95\) is the trap: it charges the first hour twice.")

Q(id="HM-04", domain="ALG", skill="Linear functions", diff=3, desmos=False,
  stem=r"A print shop charges a \(\$35\) setup fee plus \(\$0.18\) per page for the first \(500\) pages of an order and \(\$0.12\) per page for each page after the first \(500\). Which function \(C\) gives the total cost, in dollars, of an order of \(x\) pages, where \(x>500\)?",
  choices=[r"\(C(x)=0.12x+65\)", r"\(C(x)=0.12x+125\)", r"\(C(x)=0.18x+35\)", r"\(C(x)=0.12x+35\)"],
  vals=["12*x/100+65", "12*x/100+125", "18*x/100+35", "12*x/100+35"], answer="A",
  verify=lambda: 35 + R(18, 100) * 500 + R(12, 100) * (x - 500),
  explain=r"Setup: 35. First 500 pages: \(0.18(500)=90\). Remaining \(x-500\) pages: \(0.12(x-500)=0.12x-60\). Total: \(35+90+0.12x-60=0.12x+65\). "
          r"\(0.12x+125\) forgets to subtract the 500 pages already charged at the higher rate.")

Q(id="HM-05", domain="GEO", skill="Area and volume", diff=2, desmos=False,
  stem=r"Pentagon \(P\) and pentagon \(Q\) are similar. The length of each side of pentagon \(P\) is \(23\) times the length of the corresponding side of pentagon \(Q\). The area of pentagon \(P\) is how many times the area of pentagon \(Q\)?",
  answer="529", verify=lambda: 23 ** 2,
  explain=r"For similar figures, areas scale by the square of the length scale factor: \(23^2=529\). The trap is answering 23.")

Q(id="HM-06", domain="GEO", skill="Area and volume", diff=3, desmos=False,
  stem=r"A right circular cylinder has a volume of \(17{,}640\pi\) cubic centimeters, and the area of its base is \(441\pi\) square centimeters. A plane through the cylinder's central axis cuts the cylinder in a rectangle. What is the length, in centimeters, of a diagonal of this rectangle?",
  answer="58", verify=lambda: (lambda rr, hh: sqrt((2 * rr) ** 2 + hh ** 2))(sqrt(441), R(17640, 441)),
  explain=r"Base area \(\pi r^2=441\pi\) gives \(r=21\), so the diameter is 42. Height: \(\frac{17{,}640\pi}{441\pi}=40\). "
          r"The cross-section through the axis is a 42-by-40 rectangle, whose diagonal is \(\sqrt{42^2+40^2}=\sqrt{3364}=58\). Using the radius (21) instead of the diameter is the trap.")

Q(id="HM-07", domain="PSD", skill="Ratios, rates, proportional relationships, and units", diff=3, desmos=False,
  stem=r"A farm has an area of \(7{,}744{,}000\) square yards. What is the area of the farm, in square miles? \((1\text{ mile}=1{,}760\text{ yards})\)",
  choices=[r"\(0.25\)", r"\(2.5\)", r"\(25\)", r"\(4{,}400\)"], vals=[R(1, 4), R(5, 2), 25, 4400], answer="B",
  verify=lambda: R(7744000, 1760 ** 2),
  explain=r"One square mile is \(1{,}760\times1{,}760=3{,}097{,}600\) square yards. So the area is \(\frac{7{,}744{,}000}{3{,}097{,}600}=2.5\) square miles. "
          r"Dividing by 1,760 only once gives 4,400, the most common mistake.")

def _hm08():
    side_cm = (R(35, 10) / 8960 * 10 ** 6) ** R(1, 3)
    return round(float(side_cm), 2)

Q(id="HM-08", domain="PSD", skill="Ratios, rates, proportional relationships, and units", diff=3, desmos=True,
  stem=r"Copper has a density of \(8{,}960\) kilograms per cubic meter. A solid copper cube has a mass of \(3.5\) kilograms. To the nearest hundredth of a centimeter, what is the length of one edge of the cube? \((1\text{ meter}=100\text{ centimeters})\)",
  choices=[r"\(0.07\)", r"\(3.91\)", r"\(7.31\)", r"\(19.76\)"], vals=[R(7, 100), R(391, 100), R(731, 100), R(1976, 100)], answer="C",
  verify=_hm08,
  explain=r"Volume \(=\frac{\text{mass}}{\text{density}}=\frac{3.5}{8960}\approx0.000390625\) cubic meters. One cubic meter is \(100^3=1{,}000{,}000\) cubic centimeters, so the volume is about \(390.625\) cm³. "
          r"Edge \(=\sqrt[3]{390.625}\approx7.31\) cm. The square root (19.76) and the edge in meters (0.07) are the traps.",
  tip=r"Type <code>cbrt(3.5/8960*100^3)</code> into Desmos: 7.311. Desmos keeps every digit, which avoids rounding errors in the unit conversion.")

Q(id="HM-09", domain="ADV", skill="Nonlinear functions", diff=3, desmos=True,
  stem=r"\[g(t)=800(0.9)^{t/2}\]For the given function \(g\), the value of \(g(t)\) decreases by \(p\%\) for every increase of \(t\) by \(6\). What is the value of \(p\)?",
  answer="271/10", verify=lambda: (1 - R(9, 10) ** 3) * 100,
  explain=r"An increase of 6 in \(t\) raises the exponent \(\frac t2\) by 3, so \(g\) is multiplied by \(0.9^3=0.729\). Multiplying by 0.729 is a decrease of \(1-0.729=0.271\), or 27.1%. "
          r"The trap is \(3\times10\%=30\%\): percent decreases compound.",
  tip=r"Type <code>g(t)=800(0.9)^{t/2}</code>, then <code>g(6)/g(0)</code>: 0.729, a 27.1% decrease.")

def _hm10():
    rv = symbols("rv")
    pts = {"A": (rv, (3 * rv - 10) / 4), "B": (rv, (10 - 3 * rv) / 4), "C": ((4 * rv - 10) / 3, rv), "D": (rv, 3 * rv - 10)}
    good = [L for L, (px, py) in pts.items()
            if simplify(3 * px - 4 * py - 10) == 0 and simplify(9 * px - 12 * py - 30) == 0]
    assert len(good) == 1
    return good[0]

Q(id="HM-10", domain="ALG", skill="Systems of two linear equations in two variables", diff=3, desmos=False,
  stem=r"\[3x-4y=10\]\[9x-12y=30\]For each real number \(r\), which of the following points lies on the graph of each equation in the \(xy\)-plane for the given system?",
  choices=[r"\(\left(r,\ \dfrac{3r-10}{4}\right)\)", r"\(\left(r,\ \dfrac{10-3r}{4}\right)\)", r"\(\left(\dfrac{4r-10}{3},\ r\right)\)", r"\(\left(r,\ 3r-10\right)\)"],
  answer="A", verify=_hm10,
  explain=r"The second equation is 3 times the first, so both describe the same line, and every point on \(3x-4y=10\) works. Let \(x=r\): \(3r-4y=10\), so \(y=\frac{3r-10}{4}\). "
          r"Check the others: \(\left(\frac{4r-10}{3},r\right)\) gives \(3x-4y=4r-10-4r=-10\), not 10, and the remaining two don't satisfy the equation for every \(r\).")

def _hm11():
    C = Circle(Point(2, -3), Point(2, -3).distance(Point(7, 9)))   # radius 13
    T = C.tangent_lines(Point(7, 9))[0]
    cands = {"A": Point(19, 4), "B": Point(19, 14), "C": Point(12, 21), "D": Point(-5, 4)}
    good = [L for L, P in cands.items() if T.contains(P)]
    assert len(good) == 1
    return good[0]

Q(id="HM-11", domain="GEO", skill="Circles", diff=3, desmos=True,
  stem=r"A circle in the \(xy\)-plane has its center at \((2,-3)\). Line \(t\) is tangent to this circle at the point \((7,9)\). Which of the following points also lies on line \(t\)?",
  choices=[r"\((19,4)\)", r"\((19,14)\)", r"\((12,21)\)", r"\((-5,4)\)"], answer="A", verify=_hm11,
  explain=r"The radius to \((7,9)\) has slope \(\frac{9-(-3)}{7-2}=\frac{12}{5}\), and a tangent is perpendicular to the radius, so line \(t\) has slope \(-\frac{5}{12}\). "
          r"From \((7,9)\), moving 12 right means moving 5 down: \((19,4)\). \((12,21)\) lies on the radius line, the trap.",
  tip=r"Graph the circle \((x-2)^2+(y+3)^2=169\) (since \(5^2+12^2=169\)), type <code>y-9=-5/12(x-7)</code>, and check which point lies on that line.")

def _hm12():
    sol = solve(Eq((11 * x - 40), p * (x + 3) + w * (x - 5)), [p, w])
    return sol[p] + sol[w]

Q(id="HM-12", domain="ADV", skill="Equivalent expressions", diff=3, desmos=False,
  stem=r"The expression \(\dfrac{11x-40}{(x-5)(x+3)}\) is equivalent to \(\dfrac{p}{x-5}+\dfrac{w}{x+3}\), where \(p\) and \(w\) are constants. What is the value of \(p+w\)?",
  answer="11", verify=_hm12,
  explain=r"Combine the right side: \(\frac{p(x+3)+w(x-5)}{(x-5)(x+3)}\). The numerators must match: \(p(x+3)+w(x-5)=11x-40\). "
          r"Comparing the \(x\)-coefficients gives \(p+w=11\) immediately, with no need to find \(p\) and \(w\) separately. (They are \(\frac{15}{8}\) and \(\frac{73}{8}\).)")

def _hm13():
    rad = 14 * sqrt(3)
    side = rad * sqrt(3)      # an equilateral triangle inscribed in a circle of radius r has side r*sqrt(3)
    return 3 * side

Q(id="HM-13", domain="GEO", skill="Right triangles and trigonometry", diff=3, desmos=False,
  stem=r"An equilateral triangle is inscribed in a circle, so all three of its vertices lie on the circle. The radius of the circle is \(14\sqrt3\) centimeters. What is the perimeter, in centimeters, of the triangle?",
  answer="126", verify=_hm13,
  explain=r"The center of the circle is also the triangle's center, and the segments from the center to two vertices form a 30-30-120 triangle. Splitting it in half gives a 30-60-90 triangle with hypotenuse \(r\) and long leg \(\frac{s}{2}\), so \(\frac s2=\frac{\sqrt3}{2}r\) and \(s=r\sqrt3\). "
          r"Then \(s=14\sqrt3\cdot\sqrt3=42\), and the perimeter is \(3(42)=126\).")
