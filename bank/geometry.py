import math
from sympy import (Rational as R, symbols, solve, Eq, sqrt, pi, expand, simplify, Point, Circle,
                   Line, Triangle, acos, sin, cos, nsimplify)
from .common import Q

x, y, k, r, s, h = symbols("x y k r s h")

AV = "Area and volume"
LT = "Lines, angles, and triangles"
RT = "Right triangles and trigonometry"
CI = "Circles"


def _radius_sq(expr):
    """Given expr = 0 for a circle x^2 + y^2 + Dx + Ey + F (leading coeff 1), return r^2."""
    D = expr.coeff(x, 1); E = expr.coeff(y, 1); F = expr.subs({x: 0, y: 0})
    return (D/2)**2 + (E/2)**2 - F

Q(id="GEO-01", domain="GEO", skill=CI, diff=2, desmos=False,
  stem=r"\[x^2+10x+y^2-6y=k\]In the \(xy\)-plane, the graph of the given equation is a circle with a diameter of 14. What is the value of \(k\)?",
  answer="15", verify=lambda: solve(Eq(_radius_sq(x**2 + 10*x + y**2 - 6*y - k), 7**2), k)[0],
  explain=r"Complete the square: \((x+5)^2-25+(y-3)^2-9=k\), so \((x+5)^2+(y-3)^2=k+34\). "
          r"The radius is 7, so \(k+34=49\) and \(k=15\).")

Q(id="GEO-02", domain="GEO", skill=CI, diff=3, desmos=False,
  stem=r"\[2x^2+2y^2+12x-20y=-34\]In the \(xy\)-plane, the graph of the given equation is a circle. What is the radius of the circle?",
  choices=[r"\(\sqrt{17}\)", r"\(17\)", r"\(\sqrt{34}\)", r"\(2\sqrt{17}\)"],
  vals=[sqrt(17), 17, sqrt(34), 2*sqrt(17)], answer="A",
  verify=lambda: sqrt(_radius_sq(expand((2*x**2 + 2*y**2 + 12*x - 20*y + 34)/2))),
  explain=r"First divide every term by 2: \(x^2+y^2+6x-10y=-17\). Complete the square: \((x+3)^2+(y-5)^2=-17+9+25=17\). "
          r"So \(r^2=17\) and \(r=\sqrt{17}\). (Forgetting to divide by 2 first is the most common mistake.)")

Q(id="GEO-03", domain="GEO", skill=CI, diff=2, desmos=False,
  stem=r"In a circle with center \(O\), central angle \(AOB\) has a measure of \(\frac{2\pi}{5}\) radians. The length of arc \(AB\) (the arc intercepted by the angle) is \(6\pi\). What is the circumference of the circle?",
  choices=[r"\(12\pi\)", r"\(15\pi\)", r"\(30\pi\)", r"\(60\pi\)"], vals=[12*pi, 15*pi, 30*pi, 60*pi], answer="C",
  verify=lambda: 2*pi*solve(Eq(r*2*pi/5, 6*pi), r)[0],
  explain=r"Arc length \(=r\theta\): \(r\cdot\frac{2\pi}{5}=6\pi\), so \(r=15\). Circumference \(=2\pi r=30\pi\). "
          r"(Or: \(\frac{2\pi}{5}\) is \(\frac15\) of a full turn, so the circumference is \(5\times6\pi=30\pi\).)")

Q(id="GEO-04", domain="GEO", skill=CI, diff=2, desmos=False,
  stem=r"Points \(A\) and \(B\) lie on a circle with center \(O\) and radius 10. The length of chord \(AB\) is 12. What is the distance from \(O\) to chord \(AB\)?",
  answer="8", verify=lambda: sqrt(10**2 - 6**2),
  explain=r"The perpendicular from the center to a chord bisects the chord, forming a right triangle with hypotenuse 10 (a radius) and leg 6 (half of the chord). "
          r"The distance is \(\sqrt{100-36}=8\).")

def _geo05():
    C = Circle(Point(2, -1), 5)
    P = Point(5, 3)
    assert C.encloses_point(P) is False and (P.distance(C.center) == 5)
    tl = C.tangent_lines(P)[0]
    return tl.slope

Q(id="GEO-05", domain="GEO", skill=CI, diff=3, desmos=True,
  stem=r"In the \(xy\)-plane, the point \((5,3)\) lies on the circle \((x-2)^2+(y+1)^2=25\). What is the slope of the line tangent to the circle at \((5,3)\)?",
  answer="-3/4", verify=_geo05,
  explain=r"The center is \((2,-1)\). The radius to \((5,3)\) has slope \(\frac{3-(-1)}{5-2}=\frac43\). A tangent line is perpendicular to the radius at the point of tangency, "
          r"so its slope is \(-\frac34\).",
  tip=r"Graph the circle and type \(y-3=m(x-5)\) with a slider for \(m\). Adjust \(m\) until the line just touches the circle: \(m=-0.75\).")

def _geo06():
    # right angle at C; sin A = BC/AB = 12/13
    AB, BC = 13, 12
    AC = sqrt(AB**2 - BC**2)
    return AC / BC          # tan B = opposite(B)/adjacent(B) = AC/BC

Q(id="GEO-06", domain="GEO", skill=RT, diff=2, desmos=False,
  stem=r"In right triangle \(ABC\), angle \(C\) is a right angle and \(\sin A=\frac{12}{13}\). What is the value of \(\tan B\)?",
  answer="5/12", verify=_geo06,
  explain=r"\(\sin A=\frac{BC}{AB}=\frac{12}{13}\), so take \(BC=12\) and \(AB=13\). Then \(AC=\sqrt{169-144}=5\). "
          r"For angle \(B\), the opposite side is \(AC\) and the adjacent side is \(BC\): \(\tan B=\frac{5}{12}\). Acceptable entries include 5/12, .4166, and .4167.")

def _geo07():
    sols = [v for v in range(1, 90) if 0 < 3*v - 10 < 90 and math.isclose(math.sin(math.radians(v)), math.cos(math.radians(3*v - 10)))]
    assert len(sols) == 1
    return sols[0]

Q(id="GEO-07", domain="GEO", skill=RT, diff=2, desmos=False,
  stem=r"\[\sin(x^\circ)=\cos\big((3x-10)^\circ\big)\]In the given equation, the angles that measure \(x^\circ\) and \((3x-10)^\circ\) are both acute. What is the value of \(x\)?",
  answer="25", verify=_geo07,
  explain=r"For acute angles, \(\sin a^\circ=\cos b^\circ\) exactly when the angles are complementary: \(a+b=90\). So \(x+(3x-10)=90\). "
          r"So \(4x=100\) and \(x=25\).")

Q(id="GEO-08", domain="GEO", skill=AV, diff=2, desmos=False,
  stem=r"An equilateral triangle has an area of \(36\sqrt3\) square units. What is the perimeter, in units, of the triangle?",
  answer="36", verify=lambda: 3*[v for v in solve(Eq(sqrt(3)/4*s**2, 36*sqrt(3)), s) if v > 0][0],
  explain=r"Area of an equilateral triangle: \(\frac{\sqrt3}{4}s^2=36\sqrt3\), so \(s^2=144\) and \(s=12\). Perimeter: \(3(12)=36\).")

Q(id="GEO-09", domain="GEO", skill=LT, diff=3, desmos=False,
  stem=r"In triangle \(ABC\), point \(D\) lies on \(\overline{AB}\) and point \(E\) lies on \(\overline{AC}\) such that \(\overline{DE}\) is parallel to \(\overline{BC}\). The length of \(AD\) is 6, the length of \(DB\) is 4, and the area of triangle \(ADE\) is 54. What is the area of quadrilateral \(DBCE\)?",
  answer="96", verify=lambda: 54*R(6 + 4, 6)**2 - 54,
  explain=r"Triangles \(ADE\) and \(ABC\) are similar (parallel lines give equal corresponding angles), with scale factor \(\frac{AB}{AD}=\frac{10}{6}=\frac53\). "
          r"Areas scale by the square: \(\left(\frac53\right)^2=\frac{25}{9}\). Area of \(ABC=54\cdot\frac{25}{9}=150\). Area of \(DBCE=150-54=96\).")

Q(id="GEO-10", domain="GEO", skill=AV, diff=2, desmos=False,
  stem=r"A right circular cylinder has a volume of \(72\pi\) cubic inches. A right circular cone has the same radius as the cylinder and twice the height of the cylinder. What is the volume, in cubic inches, of the cone?",
  choices=[r"\(24\pi\)", r"\(36\pi\)", r"\(48\pi\)", r"\(144\pi\)"], vals=[24*pi, 36*pi, 48*pi, 144*pi], answer="C",
  verify=lambda: R(1, 3)*2*72*pi,
  explain=r"Cylinder: \(\pi r^2h=72\pi\). Cone: \(\frac13\pi r^2(2h)=\frac23(\pi r^2h)=\frac23(72\pi)=48\pi\).")

Q(id="GEO-11", domain="GEO", skill=AV, diff=2, desmos=False,
  stem=r"The length of a rectangular prism is increased by 20%, its width is decreased by 20%, and its height is increased by 50%. By what percent does the volume of the prism increase?",
  answer="44", verify=lambda: (R(12, 10)*R(8, 10)*R(15, 10) - 1)*100,
  explain=r"Volume scales by \(1.2\times0.8\times1.5=1.44\), a 44% increase.")

Q(id="GEO-12", domain="GEO", skill=AV, diff=2, desmos=False,
  stem=r"A sphere has a surface area of \(144\pi\) square centimeters. The volume of the sphere is \(k\pi\) cubic centimeters. What is the value of \(k\)?",
  answer="288", verify=lambda: (lambda rr: R(4, 3)*rr**3)([v for v in solve(Eq(4*r**2, 144), r) if v > 0][0]),
  explain=r"\(4\pi r^2=144\pi\), so \(r=6\). Volume: \(\frac43\pi(6)^3=\frac43(216)\pi=288\pi\). So \(k=288\).")

Q(id="GEO-13", domain="GEO", skill=LT, diff=1, desmos=False,
  stem=r"In triangle \(PQR\), the measure of angle \(P\) is \(40^\circ\) greater than the measure of angle \(Q\), and the measure of angle \(R\) is twice the measure of angle \(Q\). What is the measure, in degrees, of angle \(P\)?",
  answer="75", verify=lambda: solve(Eq(x + (x + 40) + 2*x, 180), x)[0] + 40,
  explain=r"Let angle \(Q=x\). Then \(x+(x+40)+2x=180\), so \(4x=140\) and \(x=35\). Angle \(P=35+40=75^\circ\).")

Q(id="GEO-14", domain="GEO", skill=AV, diff=3, desmos=False,
  stem=r"A rectangular box has a square base and a height of 9 inches. The length of a diagonal of the box that runs from one corner through the interior to the opposite corner is 17 inches. What is the area, in square inches, of the base of the box?",
  answer="104", verify=lambda: solve(Eq(2*s + 81, 289), s)[0],
  explain=r"For a box with dimensions \(a,b,c\), the space diagonal is \(\sqrt{a^2+b^2+c^2}\). With base side \(s\): \(s^2+s^2+9^2=17^2\), so \(2s^2=208\) and \(s^2=104\). "
          r"The base area is \(s^2=104\). (No need to find \(s\) itself.)")

def _geo15():
    T = Triangle(Point(0, 8), Point(-6, 0), Point(6, 0))   # A apex, AB = AC = 10, BC = 12
    assert T.sides[0].length == 10 and T.sides[2].length == 10 and T.sides[1].length == 12
    angA = T.angles[Point(0, 8)]
    return simplify(sin(angA))

Q(id="GEO-15", domain="GEO", skill=RT, diff=3, desmos=False,
  stem=r"In triangle \(ABC\), \(AB=AC=10\) and \(BC=12\). What is the value of \(\sin A\)?",
  answer="24/25", verify=_geo15,
  explain=r"Draw the altitude from \(A\) to \(\overline{BC}\). It bisects \(BC\), so it splits the triangle into two right triangles with legs 6 and \(\sqrt{100-36}=8\). "
          r"The area of \(ABC\) is \(\frac12(12)(8)=48\). The area also equals \(\frac12(AB)(AC)\sin A=50\sin A\). So \(\sin A=\frac{48}{50}=\frac{24}{25}=0.96\).")

Q(id="GEO-16", domain="GEO", skill=CI, diff=1, desmos=False,
  stem=r"A sector of a circle with radius 8 has a central angle of \(135^\circ\). The area of the sector is \(k\pi\). What is the value of \(k\)?",
  answer="24", verify=lambda: R(135, 360)*8**2,
  explain=r"The sector is \(\frac{135}{360}=\frac38\) of the circle. Area: \(\frac38\cdot64\pi=24\pi\). So \(k=24\).")

Q(id="GEO-17", domain="GEO", skill=CI, diff=2, desmos=False,
  stem=r"Points \(A\), \(B\), and \(C\) lie on a circle with center \(O\) and radius 18. Inscribed angle \(ABC\) intercepts minor arc \(AC\) and has a measure of \(35^\circ\). What is the length of minor arc \(AC\)?",
  choices=[r"\(\dfrac{7\pi}{2}\)", r"\(7\pi\)", r"\(14\pi\)", r"\(35\pi\)"], vals=[7*pi/2, 7*pi, 14*pi, 35*pi], answer="B",
  verify=lambda: R(2*35, 360)*2*pi*18,
  explain=r"An inscribed angle is half its intercepted arc, so arc \(AC\) measures \(70^\circ\). Arc length: \(\frac{70}{360}\cdot2\pi(18)=\frac{7}{36}\cdot36\pi=7\pi\). "
          r"\(\frac{7\pi}{2}\) is the trap from using \(35^\circ\) as the arc measure.")

def _geo18():
    P1 = Line(Point(0, 0), Point(1, 2)).intersection(Line(Point(0, 9), Point(9, 0)))[0]
    T = Triangle(Point(0, 0), Point(9, 0), P1)
    return abs(T.area)

Q(id="GEO-18", domain="GEO", skill=LT, diff=2, desmos=True,
  stem=r"In the \(xy\)-plane, the graphs of \(y=2x\), \(y=-x+9\), and the \(x\)-axis form a triangle. What is the area of the triangle?",
  answer="27", verify=_geo18,
  explain=r"The lines meet where \(2x=-x+9\): \(x=3\), \(y=6\). \(y=2x\) meets the \(x\)-axis at \((0,0)\), and \(y=-x+9\) meets it at \((9,0)\). "
          r"Base 9, height 6: area \(=\frac12(9)(6)=27\).",
  tip=r"Graph both lines. Click the three corners: \((0,0)\), \((9,0)\), and \((3,6)\). Then use \(\frac12bh\).")

Q(id="GEO-19", domain="GEO", skill=RT, diff=1, desmos=False,
  stem=r"The lengths of the legs of a right triangle are in the ratio 5 to 12. The length of the hypotenuse is 39. What is the perimeter of the triangle?",
  answer="90", verify=lambda: (lambda u: 5*u + 12*u + 39)([v for v in solve(Eq((5*k)**2 + (12*k)**2, 39**2), k) if v > 0][0]),
  explain=r"Sides are \(5k\), \(12k\), \(13k\) (a 5-12-13 triangle). \(13k=39\), so \(k=3\): sides 15, 36, 39. Perimeter \(=90\).")

Q(id="GEO-20", domain="GEO", skill=AV, diff=2, desmos=False,
  stem=r"What is the area of a regular hexagon with a side length of 6?",
  choices=[r"\(27\sqrt3\)", r"\(36\sqrt3\)", r"\(54\sqrt3\)", r"\(108\sqrt3\)"],
  vals=[27*sqrt(3), 36*sqrt(3), 54*sqrt(3), 108*sqrt(3)], answer="C",
  verify=lambda: 6*sqrt(3)/4*6**2,
  explain=r"A regular hexagon splits into 6 equilateral triangles with side 6. Each has area \(\frac{\sqrt3}{4}(36)=9\sqrt3\). Total: \(54\sqrt3\).")

Q(id="GEO-21", domain="GEO", skill=AV, diff=1, desmos=False,
  stem=r"A circle is inscribed in a square, so the circle touches all four sides of the square. The area of the square is 196 square units. What is the area, in square units, of the region inside the square but outside the circle?",
  choices=[r"\(196-196\pi\)", r"\(196-49\pi\)", r"\(196-14\pi\)", r"\(196-7\pi\)"],
  vals=[196 - 196*pi, 196 - 49*pi, 196 - 14*pi, 196 - 7*pi], answer="B",
  verify=lambda: 196 - pi*(sqrt(196)/2)**2,
  explain=r"Side of the square: \(\sqrt{196}=14\), which is the circle's diameter, so \(r=7\). Circle area: \(49\pi\). Region: \(196-49\pi\).")

Q(id="GEO-22", domain="GEO", skill=RT, diff=3, desmos=False,
  stem=r"In right triangle \(ABC\), the right angle is at \(C\). The altitude from \(C\) meets hypotenuse \(\overline{AB}\) at point \(D\). If \(AD=4\) and \(DB=9\), what is the length of \(\overline{CD}\)?",
  answer="6", verify=lambda: sqrt(4*9),
  explain=r"The altitude to the hypotenuse creates two triangles similar to each other: \(\triangle ACD\sim\triangle CBD\). So \(\frac{AD}{CD}=\frac{CD}{DB}\), "
          r"which gives \(CD^2=AD\cdot DB=36\) and \(CD=6\).")

def _geo23():
    pts = solve([Eq(x**2 + y**2, 25), Eq(y, x + 1)], [x, y])
    (x1, y1), (x2, y2) = pts
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

Q(id="GEO-23", domain="GEO", skill=CI, diff=3, desmos=True,
  stem=r"In the \(xy\)-plane, the line \(y=x+1\) intersects the circle \(x^2+y^2=25\) at two points. What is the distance between these two points?",
  choices=[r"\(7\)", r"\(5\sqrt2\)", r"\(7\sqrt2\)", r"\(14\)"], vals=[7, 5*sqrt(2), 7*sqrt(2), 14], answer="C",
  verify=_geo23,
  explain=r"Substitute: \(x^2+(x+1)^2=25\), so \(2x^2+2x-24=0\), or \(x^2+x-12=0\). Then \(x=3\) or \(x=-4\), giving points \((3,4)\) and \((-4,-3)\). "
          r"Distance: \(\sqrt{7^2+7^2}=7\sqrt2\).",
  tip=r"Graph both. Click the two intersection points, \((3,4)\) and \((-4,-3)\), then type <code>distance((3,4),(-4,-3))</code> into Desmos: 9.899, which is \(7\sqrt2\).")
