"""Questions with figures (graphs, plots, diagrams), plus two question types found in the
official practice tests that the bank lacked (squared-unit conversion, absolute value).

Calibration against College Board practice tests 4, 7 and 10 showed that official math
questions regularly use graphs, dot plots, histograms, scatterplots and geometry diagrams,
while the bank had almost none. Every figure here is drawn by code from the same numbers
the verifier uses, so a figure can never disagree with its answer key.
"""
import statistics
from fractions import Fraction as F
from sympy import Rational as R, symbols, solve, Eq, sqrt, Point, Line
from .common import Q

x, y = symbols("x y")

W, H = 320, 320
_ids = iter(range(1, 10_000))   # deterministic ids, so rebuilding produces identical output
STYLE = "font-family:system-ui,sans-serif;font-size:12px"


def _svg(body, w=W, h=H, label="figure"):
    return (f'<svg class="fig" viewBox="0 0 {w} {h}" width="{w}" role="img" aria-label="{label}" '
            f'xmlns="http://www.w3.org/2000/svg" style="{STYLE}">{body}</svg>')


def plane(xr, yr, items, step=1, label_every=2, w=W, h=H, label="graph in the xy-plane", ystep=None, ylabel_every=None):
    """Coordinate plane. items: ('line', m, b) | ('pts', [(x,y),...]) | ('curve', f) |
    ('circle', h, k, r) | ('dot', x, y, text)."""
    x0, x1 = xr; y0, y1 = yr
    ystep = ystep or step
    ylabel_every = ylabel_every or label_every
    pad = 24
    sx = lambda v: pad + (v - x0) / (x1 - x0) * (w - 2 * pad)
    sy = lambda v: h - pad - (v - y0) / (y1 - y0) * (h - 2 * pad)
    out = []
    v = x0
    while v <= x1 + 1e-9:
        out.append(f'<line x1="{sx(v):.1f}" y1="{sy(y0):.1f}" x2="{sx(v):.1f}" y2="{sy(y1):.1f}" stroke="#e3e5ea"/>')
        v += step
    v = y0
    while v <= y1 + 1e-9:
        out.append(f'<line x1="{sx(x0):.1f}" y1="{sy(v):.1f}" x2="{sx(x1):.1f}" y2="{sy(v):.1f}" stroke="#e3e5ea"/>')
        v += ystep
    out.append(f'<line x1="{sx(x0)}" y1="{sy(0):.1f}" x2="{sx(x1)}" y2="{sy(0):.1f}" stroke="#222" stroke-width="1.4"/>')
    out.append(f'<line x1="{sx(0):.1f}" y1="{sy(y0)}" x2="{sx(0):.1f}" y2="{sy(y1)}" stroke="#222" stroke-width="1.4"/>')
    out.append(f'<text x="{sx(x1) - 4:.1f}" y="{sy(0) - 6:.1f}" text-anchor="end" font-style="italic">x</text>')
    out.append(f'<text x="{sx(0) + 6:.1f}" y="{sy(y1) + 12:.1f}" font-style="italic">y</text>')
    v = x0
    while v <= x1 + 1e-9:
        if v != 0 and round(v / label_every) * label_every == v:
            out.append(f'<text x="{sx(v):.1f}" y="{sy(0) + 14:.1f}" text-anchor="middle" fill="#444">{v:g}</text>')
        v += step
    v = y0
    while v <= y1 + 1e-9:
        if v != 0 and round(v / ylabel_every) * ylabel_every == v:
            out.append(f'<text x="{sx(0) - 5:.1f}" y="{sy(v) + 4:.1f}" text-anchor="end" fill="#444">{v:g}</text>')
        v += ystep
    out.append(f'<text x="{sx(0) - 5:.1f}" y="{sy(0) + 14:.1f}" text-anchor="end" fill="#444">O</text>')
    clip = f'<clipPath id="clip{next(_ids)}"><rect x="{pad}" y="{pad}" width="{w - 2 * pad}" height="{h - 2 * pad}"/></clipPath>'
    cid = clip.split('"')[1]
    body = []
    for it in items:
        if it[0] == "line":
            _, m, b = it
            body.append(f'<line x1="{sx(x0):.1f}" y1="{sy(m * x0 + b):.1f}" x2="{sx(x1):.1f}" y2="{sy(m * x1 + b):.1f}" stroke="#1f3fbf" stroke-width="2"/>')
        elif it[0] == "curve":
            f = it[1]
            n = 240
            pts = []
            for i in range(n + 1):
                xv = x0 + (x1 - x0) * i / n
                try:
                    yv = float(f(xv))
                except (ValueError, OverflowError, ZeroDivisionError):
                    continue
                if y0 - 50 < yv < y1 + 50:
                    pts.append(f"{sx(xv):.1f},{sy(yv):.1f}")
            body.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#1f3fbf" stroke-width="2"/>')
        elif it[0] == "circle":
            _, hh, kk, rr = it
            body.append(f'<ellipse cx="{sx(hh):.1f}" cy="{sy(kk):.1f}" rx="{abs(sx(hh + rr) - sx(hh)):.1f}" ry="{abs(sy(kk + rr) - sy(kk)):.1f}" fill="none" stroke="#1f3fbf" stroke-width="2"/>')
        elif it[0] == "pts":
            for (px, py) in it[1]:
                body.append(f'<circle cx="{sx(px):.1f}" cy="{sy(py):.1f}" r="3.6" fill="#222"/>')
        elif it[0] == "dot":
            _, px, py, t = it
            body.append(f'<circle cx="{sx(px):.1f}" cy="{sy(py):.1f}" r="3.6" fill="#222"/>')
            if t:
                body.append(f'<text x="{sx(px) + 6:.1f}" y="{sy(py) - 6:.1f}">{t}</text>')
    return _svg(f'<defs>{clip}</defs>' + "".join(out) + f'<g clip-path="url(#{cid})">' + "".join(body) + "</g>", w, h, label)


def dotplot(counts, lo, hi, w=360, h=150):
    pad = 26
    sx = lambda v: pad + (v - lo) / (hi - lo) * (w - 2 * pad)
    base = h - 34
    out = [f'<line x1="{pad - 8}" y1="{base}" x2="{w - pad + 8}" y2="{base}" stroke="#222"/>']
    for v in range(lo, hi + 1):
        out.append(f'<line x1="{sx(v):.1f}" y1="{base}" x2="{sx(v):.1f}" y2="{base + 5}" stroke="#222"/>')
        out.append(f'<text x="{sx(v):.1f}" y="{base + 19}" text-anchor="middle">{v}</text>')
        for i in range(counts.get(v, 0)):
            out.append(f'<circle cx="{sx(v):.1f}" cy="{base - 10 - i * 14}" r="5" fill="#222"/>')
    return _svg("".join(out), w, h, "dot plot")


def bars(labels, values, ymax, ytick, ylabel, w=360, h=250, histogram=False):
    padl, padb, padt = 46, 40, 14
    n = len(values)
    bw = (w - padl - 12) / n
    sy = lambda v: h - padb - v / ymax * (h - padb - padt)
    out = []
    v = 0
    while v <= ymax:
        out.append(f'<line x1="{padl}" y1="{sy(v):.1f}" x2="{w - 12}" y2="{sy(v):.1f}" stroke="#e3e5ea"/>')
        out.append(f'<text x="{padl - 5}" y="{sy(v) + 4:.1f}" text-anchor="end">{v:g}</text>')
        v += ytick
    for i, val in enumerate(values):
        gap = 0 if histogram else bw * 0.22
        out.append(f'<rect x="{padl + i * bw + gap / 2:.1f}" y="{sy(val):.1f}" width="{bw - gap:.1f}" height="{sy(0) - sy(val):.1f}" fill="#8da2e8" stroke="#1f3fbf"/>')
    if histogram:
        for i, lab in enumerate(labels):
            out.append(f'<text x="{padl + i * bw:.1f}" y="{h - padb + 15}" text-anchor="middle">{lab}</text>')
    else:
        for i, lab in enumerate(labels):
            out.append(f'<text x="{padl + (i + 0.5) * bw:.1f}" y="{h - padb + 15}" text-anchor="middle">{lab}</text>')
    out.append(f'<line x1="{padl}" y1="{sy(0)}" x2="{w - 12}" y2="{sy(0)}" stroke="#222"/>')
    out.append(f'<line x1="{padl}" y1="{sy(0)}" x2="{padl}" y2="{padt}" stroke="#222"/>')
    out.append(f'<text x="12" y="{(h - padb) / 2:.0f}" transform="rotate(-90 12 {(h - padb) / 2:.0f})" text-anchor="middle">{ylabel}</text>')
    return _svg("".join(out), w, h, "histogram" if histogram else "bar graph")


def _fig(svg, note=""):
    return f'<div class="figwrap">{svg}{f"<div class=figcap>{note}</div>" if note else ""}</div>'


# ======================================================================== graphs
L1 = (-1, 6)       # y = -x + 6
L2 = (2, -3)       # y = 2x - 3

def _f01():
    s = solve([Eq(y, L1[0] * x + L1[1]), Eq(y, L2[0] * x + L2[1])], [x, y])
    third = s[x] + 4 * s[y] == 15            # does x + 4y = 15 pass through the intersection?
    parallel_to_existing = R(-1, 4) in (L1[0], L2[0])
    return 1 if third and not parallel_to_existing else (0 if not third else None)

Q(id="FIG-01", domain="ALG", skill="Systems of two linear equations in two variables", diff=3, desmos=True,
  stem=_fig(plane((-2, 8), (-4, 8), [("line", *L1), ("line", *L2)], label="two lines in the xy-plane")) +
       r"The graph of a system of two linear equations is shown. If the equation \(x+4y=15\) is added to the system, how many solutions \((x,y)\) will the resulting system of three equations have?",
  choices=["Zero", "Exactly one", "Exactly two", "Infinitely many"], vals=[0, 1, 2, 3], answer="B", verify=_f01,
  explain=r"From the graph, the lines are \(y=-x+6\) (through \((0,6)\) and \((6,0)\)) and \(y=2x-3\) (through \((0,-3)\) with slope 2). They intersect at \((3,3)\). "
          r"A solution to all three equations must be that point. Check \(x+4y=15\): \(3+4(3)=15\). ✓ So the third line passes through \((3,3)\), and the system has exactly one solution.",
  tip=r"Read the two lines off the graph, type them into Desmos along with \(x+4y=15\), and check whether all three cross at one point: \((3,3)\).")

def _f07():
    return x * (x - 4)

Q(id="FIG-02", domain="ADV", skill="Nonlinear functions", diff=2, desmos=True,
  stem=_fig(plane((-2, 6), (-6, 6), [("curve", lambda t: t * (t - 4)), ("dot", 2, -4, "(2, −4)")], label="parabola")) +
       r"The graph of \(y=f(x)\) is shown, where \(f\) is a quadratic function. Its vertex is \((2,-4)\). Which equation defines \(f\)?",
  choices=[r"\(f(x)=x(x-4)\)", r"\(f(x)=(x+2)^2-4\)", r"\(f(x)=-x(x-4)\)", r"\(f(x)=(x-2)^2+4\)"],
  vals=["x*(x-4)", "(x+2)**2-4", "-x*(x-4)", "(x-2)**2+4"], answer="A", verify=_f07,
  explain=r"The graph crosses the \(x\)-axis at 0 and 4, so \(f(x)=a\,x(x-4)\). At the vertex, \(f(2)=a(2)(-2)=-4a=-4\), so \(a=1\). "
          r"Vertex form gives the same function: \((x-2)^2-4=x^2-4x\). The traps \((x+2)^2-4\) and \((x-2)^2+4\) flip a sign, and \(-x(x-4)\) has the right zeros but opens downward.",
  tip=r"Type each choice into Desmos. Only \(x(x-4)\) passes through \((0,0)\), \((4,0)\), and \((2,-4)\) like the graph.")

def _f08():
    b = sqrt(R(12, 3))
    return 3 * b ** 3

Q(id="FIG-03", domain="ADV", skill="Nonlinear functions", diff=3, desmos=True,
  stem=_fig(plane((-2, 4), (-4, 28), [("curve", lambda t: 3 * 2 ** t), ("dot", 0, 3, "(0, 3)"), ("dot", 2, 12, "(2, 12)")],
                  step=1, label_every=1, ystep=4, ylabel_every=8, label="exponential curve")) +
       r"The graph of the exponential function \(f\), where \(f(x)=ab^{x}\) and \(a\) and \(b\) are positive constants, passes through the points \((0,3)\) and \((2,12)\), as shown. What is the value of \(f(3)\)?",
  answer="24", verify=_f08,
  explain=r"\(f(0)=a=3\). Then \(f(2)=3b^2=12\), so \(b^2=4\) and \(b=2\). So \(f(3)=3(2)^3=24\). (Reading the graph alone at \(x=3\) is hard to do precisely; use the two labeled points.)",
  tip=r"Make a table with \((0,3)\) and \((2,12)\), type <code>y_1 ~ a b^{x_1}</code> to get \(a=3\), \(b=2\), then evaluate <code>3(2)^3</code>.")

def _f09():
    c = (-2, 1); p = (1, 5)
    r2 = (p[0] - c[0]) ** 2 + (p[1] - c[1]) ** 2
    return "A" if r2 == 25 else "?"

Q(id="FIG-04", domain="GEO", skill="Circles", diff=2, desmos=True,
  stem=_fig(plane((-8, 4), (-5, 7), [("circle", -2, 1, 5), ("dot", -2, 1, "(−2, 1)"), ("dot", 1, 5, "(1, 5)")], label="circle")) +
       r"The circle shown in the \(xy\)-plane has its center at \((-2,1)\) and passes through the point \((1,5)\). Which of the following is an equation of the circle?",
  choices=[r"\((x+2)^2+(y-1)^2=25\)", r"\((x-2)^2+(y+1)^2=25\)", r"\((x+2)^2+(y-1)^2=5\)", r"\((x-2)^2+(y+1)^2=5\)"],
  answer="A", verify=_f09,
  explain=r"The radius is the distance from \((-2,1)\) to \((1,5)\): \(\sqrt{3^2+4^2}=5\), so \(r^2=25\). With center \((h,k)=(-2,1)\), the equation is \((x+2)^2+(y-1)^2=25\). "
          r"The other choices flip the signs of the center or forget to square the radius.",
  tip=r"Type each choice and check which one passes through \((1,5)\) with center \((-2,1)\). Watch the signs inside the parentheses.")

# ======================================================================== data displays
DOTS = {3: 1, 4: 3, 5: 4, 6: 2, 7: 1, 12: 1}

def _f02():
    data = [v for v, c in DOTS.items() for _ in range(c)]
    rest = sorted(data); rest.remove(12)
    dm = F(sum(rest), len(rest)) - F(sum(data), len(data))
    dmed = F(statistics.median(rest)) - F(statistics.median(data))
    key = ("dec" if dm < 0 else "inc" if dm > 0 else "same", "dec" if dmed < 0 else "inc" if dmed > 0 else "same")
    return {("dec", "same"): "A", ("dec", "dec"): "B", ("same", "same"): "C", ("same", "dec"): "D"}[key]

Q(id="FIG-05", domain="PSD", skill="One-variable data: distributions and measures of center and spread", diff=2, desmos=False,
  stem=_fig(dotplot(DOTS, 2, 13)) +
       r"The dot plot shows the 12 values in a data set. If the value 12 is removed from the data set, which of the following is true about the mean and median of the remaining 11 values compared with those of the original 12 values?",
  choices=["The mean decreases, and the median stays the same.", "The mean decreases, and the median decreases.",
           "The mean stays the same, and the median stays the same.", "The mean stays the same, and the median decreases."],
  answer="A", verify=_f02,
  explain=r"Mean: the original sum is 66, so the mean is \(\frac{66}{12}=5.5\); without 12 it is \(\frac{54}{11}\approx4.9\), a decrease. "
          r"Median: the original median is the average of the 6th and 7th values (both 5), so it's 5. The new median is the 6th of 11 values, which is also 5. "
          r"An extreme value pulls the mean but barely affects the median.")

BINS = [3, 8, 10, 6, 3]

def _f04():
    cum, vals = 0, []
    for i, f_ in enumerate(BINS):
        vals += [(i * 10, i * 10 + 10)] * f_
    n = len(vals)
    lo = vals[(n - 1) // 2][0]; hi = vals[n // 2][1]
    cands = {"A": 12, "B": 18, "C": 24, "D": 35}
    good = [L for L, v in cands.items() if lo <= v <= hi]
    assert len(good) == 1
    return good[0]

Q(id="FIG-06", domain="PSD", skill="One-variable data: distributions and measures of center and spread", diff=2, desmos=False,
  stem=_fig(bars(["0", "10", "20", "30", "40"] + [], BINS, 12, 2, "Frequency", histogram=True)
            .replace("</svg>", f'<text x="{46 + 5 * (360 - 58) / 5:.1f}" y="225" text-anchor="middle">50</text></svg>')) +
       r"The histogram summarizes the distribution of 30 values in a data set. Each bar includes its left endpoint but not its right endpoint (for example, the first bar represents values from 0 up to but not including 10). Which of the following could be the median of the data set?",
  choices=[r"\(12\)", r"\(18\)", r"\(24\)", r"\(35\)"], answer="C", verify=_f04,
  explain=r"With 30 values, the median is the average of the 15th and 16th values. Counting from the left: 3 values below 10, then 8 more (11 total) below 20, then 10 more (21 total) below 30. "
          r"So the 15th and 16th values are both between 20 and 30, and the median must be in that interval. Only 24 is.")

SCATTER = [(1, 2.8), (2, 2.6), (3, 3.9), (4, 3.5), (5, 4.9), (6, 4.6), (7, 5.8), (8, 5.6), (9, 6.9), (10, 6.6)]
FIT = (R(1, 2), 2)

def _f03():
    return FIT[0] * 14 + FIT[1]

Q(id="FIG-07", domain="PSD", skill="Two-variable data: models and scatterplots", diff=1, desmos=False,
  stem=_fig(plane((0, 16), (0, 12), [("pts", SCATTER), ("line", float(FIT[0]), FIT[1])], step=1, label_every=2, label="scatterplot with line of best fit")) +
       r"The scatterplot shows the relationship between two variables, \(x\) and \(y\), along with a line of best fit that passes through \((0,2)\) and \((10,7)\). Based on the line of best fit, what is the predicted value of \(y\) when \(x=14\)?",
  answer="9", verify=_f03,
  explain=r"The slope of the line is \(\frac{7-2}{10-0}=0.5\), so the line is \(y=0.5x+2\). At \(x=14\): \(y=0.5(14)+2=9\).")

def _f05():
    above = sum(1 for (px, py) in SCATTER if py > FIT[0] * px + FIT[1])
    return above

Q(id="FIG-08", domain="PSD", skill="Two-variable data: models and scatterplots", diff=2, desmos=False,
  stem=_fig(plane((0, 12), (0, 9), [("pts", SCATTER), ("line", float(FIT[0]), FIT[1])], step=1, label_every=2, label="scatterplot with line of best fit")) +
       r"The scatterplot shows 10 data points and a line of best fit, \(y=0.5x+2\). For how many of the data points is the actual \(y\)-value greater than the \(y\)-value predicted by the line of best fit?",
  answer="5", verify=_f05,
  explain=r"Points above the line have actual values greater than predicted. The points at \(x=1,3,5,7,9\) lie above the line (for example, at \(x=3\) the actual value is 3.9 and the predicted value is 3.5). "
          r"The points at \(x=2,4,6,8,10\) lie below it. That makes 5.")

SALES = [40, 50, 65, 45]

def _f10():
    return R(SALES[2] - SALES[0], SALES[0]) * 100

Q(id="FIG-09", domain="PSD", skill="Percentages", diff=2, desmos=False,
  stem=_fig(bars(["Q1", "Q2", "Q3", "Q4"], SALES, 70, 10, "Sales (thousands of $)")) +
       r"The bar graph shows a company's sales, in thousands of dollars, for each quarter of a year. By what percent did sales increase from the first quarter (Q1) to the third quarter (Q3)?",
  answer="125/2", verify=_f10,
  explain=r"From the graph, Q1 sales were 40 and Q3 sales were 65 (thousand dollars). Percent increase: \(\frac{65-40}{40}\times100=62.5\). Enter 62.5 (no percent sign).")

# ======================================================================== geometry diagrams
def _parallel_svg():
    # two horizontal parallel lines and a transversal; labels at the upper-right angle of each intersection
    return _svg('<line x1="20" y1="80" x2="320" y2="80" stroke="#222" stroke-width="2"/>'
                '<line x1="20" y1="200" x2="320" y2="200" stroke="#222" stroke-width="2"/>'
                '<line x1="110" y1="260" x2="250" y2="20" stroke="#222" stroke-width="2"/>'
                '<text x="300" y="72">ℓ</text><text x="300" y="192">m</text>'
                '<text x="230" y="72">(3x + 15)°</text>'
                '<text x="160" y="192">(5x − 25)°</text>'
                '<text x="160" y="222">y°</text>', 340, 280, "two parallel lines cut by a transversal")

def _f06():
    xv = solve(Eq(3 * x + 15, 5 * x - 25), x)[0]
    return 180 - (5 * xv - 25)

Q(id="FIG-10", domain="GEO", skill="Lines, angles, and triangles", diff=2, desmos=False,
  stem=_fig(_parallel_svg(), "Note: Figure not drawn to scale.") +
       r"In the figure, line \(\ell\) is parallel to line \(m\), and both are intersected by a transversal. The angle marked \((3x+15)^\circ\) and the angle marked \((5x-25)^\circ\) are corresponding angles, each lying above its line and to the right of the transversal. "
       r"The angle marked \(y^\circ\) lies below line \(m\) and to the right of the transversal. What is the value of \(y\)?",
  answer="105", verify=_f06,
  explain=r"Corresponding angles formed by parallel lines are equal: \(3x+15=5x-25\), so \(x=20\) and each angle is \(75^\circ\). "
          r"The angle \(y^\circ\) and the \(75^\circ\) angle at line \(m\) are adjacent and share the part of \(m\) to the right of the transversal; their other sides point in opposite directions along the transversal. So they form a linear pair and are supplementary: \(y=180-75=105\).")

def _tri_svg():
    # right angle at C; legs AC = 15 (vertical), BC = 20 (horizontal); D = foot of altitude from C to AB
    s = 9.0
    C = (40, 230); A = (C[0], C[1] - 15 * s); B = (C[0] + 20 * s, C[1])
    t = (15 * 15) / (25 * 25)                     # AD/AB = AC^2/AB^2
    D = (A[0] + (B[0] - A[0]) * t, A[1] + (B[1] - A[1]) * t)
    pts = f'{A[0]},{A[1]} {B[0]},{B[1]} {C[0]},{C[1]}'
    return _svg(f'<polygon points="{pts}" fill="none" stroke="#222" stroke-width="2"/>'
                f'<line x1="{C[0]}" y1="{C[1]}" x2="{D[0]:.1f}" y2="{D[1]:.1f}" stroke="#222" stroke-width="1.6"/>'
                f'<polyline points="{C[0]},{C[1] - 12} {C[0] + 12},{C[1] - 12} {C[0] + 12},{C[1]}" fill="none" stroke="#222"/>'
                f'<text x="{A[0] - 14}" y="{A[1] + 4}">A</text><text x="{B[0] + 6}" y="{B[1] + 4}">B</text>'
                f'<text x="{C[0] - 14}" y="{C[1] + 14}">C</text><text x="{D[0] + 6:.1f}" y="{D[1] - 6:.1f}">D</text>'
                f'<text x="{C[0] - 26}" y="{(A[1] + C[1]) / 2:.0f}">15</text><text x="{(C[0] + B[0]) / 2:.0f}" y="{C[1] + 18}">20</text>',
                260, 260, "right triangle with altitude")

def _f11():
    A, B, C = Point(0, 15), Point(20, 0), Point(0, 0)
    D = Line(A, B).projection(C)
    return A.distance(D)

Q(id="FIG-11", domain="GEO", skill="Right triangles and trigonometry", diff=3, desmos=False,
  stem=_fig(_tri_svg()) +
       r"In right triangle \(ABC\), angle \(C\) is a right angle, \(AC=15\), and \(BC=20\). Point \(D\) lies on \(\overline{AB}\) such that \(\overline{CD}\) is perpendicular to \(\overline{AB}\). What is the length of \(\overline{AD}\)?",
  answer="9", verify=_f11,
  explain=r"\(AB=\sqrt{15^2+20^2}=25\). Triangles \(ADC\) and \(ACB\) are similar (each has a right angle and shares angle \(A\)), so \(\frac{AD}{AC}=\frac{AC}{AB}\). "
          r"That gives \(AD=\frac{15^2}{25}=9\).")

# ======================================================================== other types from the official tests
Q(id="FIG-12", domain="PSD", skill="Ratios, rates, proportional relationships, and units", diff=3, desmos=False,
  stem=r"A car accelerates at a constant rate of 3.2 meters per second squared. What is this rate in kilometers per minute squared? (1 kilometer = 1,000 meters)",
  answer="11.52", verify=lambda: R(32, 10) * 60 ** 2 / 1000,
  explain=r"Convert meters to kilometers (divide by 1,000) and seconds squared to minutes squared. Since 1 minute = 60 seconds, 1 minute squared = \(60^2=3{,}600\) seconds squared, "
          r"so multiply by 3,600: \(3.2\times\frac{3600}{1000}=11.52\) kilometers per minute squared. The trap is multiplying by 60 instead of \(60^2\), which gives 0.192.")

Q(id="FIG-13", domain="ALG", skill="Linear equations in one variable", diff=2, desmos=True,
  stem=r"\[|-4x+9|=31\]What is the sum of the solutions to the given equation?",
  answer="9/2", verify=lambda: sum(solve(Eq(-4 * x + 9, 31), x) + solve(Eq(-4 * x + 9, -31), x)),
  explain=r"An absolute value equals 31 when the inside is 31 or \(-31\). \(-4x+9=31\) gives \(x=-5.5\); \(-4x+9=-31\) gives \(x=10\). The sum is \(4.5\).",
  tip=r"Graph \(y=|-4x+9|\) and \(y=31\), click the two intersections (\(x=-5.5\) and \(x=10\)), and add them.")
