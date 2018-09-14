## -*- encoding: utf-8 -*-
"""
This file (./calculus_doctest.sage) was *autogenerated* from ./calculus.tex,
with sagetex.sty version 2011/05/27 v2.3.1.
It contains the contents of all the sageexample environments from this file.
You should be able to doctest this file with:
sage -t ./calculus_doctest.sage
It is always safe to delete this file; it is not used in typesetting your
document.

Sage example in ./calculus.tex, line 76::

  sage: bool(arctan(1+abs(x)) == pi/2 - arctan(1/(1+abs(x))))
  False

Sage example in ./calculus.tex, line 121::

  sage: a, x = var('a, x'); y = cos(x+a) * (x+1); y
  (x + 1)*cos(a + x)
  sage: y.subs(a=-x); y.subs(x=pi/2, a=pi/3); y.subs(x=0.5, a=2.3)
  x + 1
  -1/4*sqrt(3)*(pi + 2)
  -1.41333351100299
  sage: y(a=-x); y(x=pi/2, a=pi/3); y(x=0.5, a=2.3)
  x + 1
  -1/4*sqrt(3)*(pi + 2)
  -1.41333351100299

Sage example in ./calculus.tex, line 143::

  sage: x, y, z = var('x, y, z') ; q = x*y + y*z + z*x
  sage: bool(q(x=y, y=z, z=x) == q), bool(q(z=y)(y=x) == 3*x^2)
  (True, True)

Sage example in ./calculus.tex, line 155::

  sage: y, z = var('y, z'); f = x^3 + y^2 + z
  sage: f.substitute(x^3 == y^2, z==1)
  2*y^2 + 1

Sage example in ./calculus.tex, line 176::

  sage: f(x)=(2*x+1)^3 ; f(-3)
  -125
  sage: f.expand()
  x |--> 8*x^3 + 12*x^2 + 6*x + 1

Sage example in ./calculus.tex, line 193::

  sage: y = var('y'); u = sin(x) + x*cos(y)
  sage: v = u.function(x, y); v
  (x, y) |--> x*cos(y) + sin(x)
  sage: w(x, y) = u; w
  (x, y) |--> x*cos(y) + sin(x)

Sage example in ./calculus.tex, line 240::

  sage: x, y = SR.var('x,y')
  sage: p = (x+y)*(x+1)^2
  sage: p2 = p.expand(); p2
  x^3 + x^2*y + 2*x^2 + 2*x*y + x + y

Sage example in ./calculus.tex, line 251::

  sage: p2.collect(x)
  x^3 + x^2*(y + 2) + x*(2*y + 1) + y

Sage example in ./calculus.tex, line 260::

  sage: ((x+y+sin(x))^2).expand().collect(sin(x))
  x^2 + 2*x*y + y^2 + 2*(x + y)*sin(x) + sin(x)^2

Sage example in ./calculus.tex, line 416::

  sage: (x^x/x).simplify()
  x^(x - 1)

Sage example in ./calculus.tex, line 426::

  sage: f = (e^x-1) / (1+e^(x/2)); f.canonicalize_radical()
  e^(1/2*x) - 1

Sage example in ./calculus.tex, line 435::

  sage: f = cos(x)^6 + sin(x)^6 + 3 * sin(x)^2 * cos(x)^2
  sage: f.simplify_trig()
  1

Sage example in ./calculus.tex, line 447::

  sage: f = cos(x)^6; f.reduce_trig()
  1/32*cos(6*x) + 3/16*cos(4*x) + 15/32*cos(2*x) + 5/16
  sage: f = sin(5 * x); f.expand_trig()
  5*cos(x)^4*sin(x) - 10*cos(x)^2*sin(x)^3 + sin(x)^5

Sage example in ./calculus.tex, line 482::

  sage: n = var('n'); f = factorial(n+1)/factorial(n)
  sage: f.simplify_factorial()
  n + 1

Sage example in ./calculus.tex, line 502::

  sage: f = sqrt(abs(x)^2); f.canonicalize_radical()
  abs(x)
  sage: f = log(x*y); f.canonicalize_radical()
  log(x) + log(y)

Sage example in ./calculus.tex, line 592::

  sage: assume(x > 0); bool(sqrt(x^2) == x)
  True
  sage: forget(x > 0); bool(sqrt(x^2) == x)
  False
  sage: n = var('n'); assume(n, 'integer'); sin(n*pi)
  0

Sage example in ./calculus.tex, line 600::

  sage: forget(n, 'integer');

Sage example in ./calculus.tex, line 690::

  sage: a = var('a')
  sage: c = (a+1)^2 - (a^2+2*a+1)

Sage example in ./calculus.tex, line 700::

  sage: eq =  c * x == 0

Sage example in ./calculus.tex, line 707::

  sage: eq2 = eq / c; eq2
  x == 0
  sage: solve(eq2, x)
  [x == 0]

Sage example in ./calculus.tex, line 715::

  sage: solve(eq, x)
  [x == x]

Sage example in ./calculus.tex, line 725::

  sage: expand(c)
  0

Sage example in ./calculus.tex, line 738::

  sage: c = cos(a)^2 + sin(a)^2 - 1
  sage: eq = c*x == 0
  sage: solve(eq, x)
  [x == 0]

Sage example in ./calculus.tex, line 750::

  sage: c.simplify_trig()
  0
  sage: c.is_zero()
  True

Sage example in ./calculus.tex, line 839::

  sage: z, phi = var('z, phi')
  sage: eq =  z**2 - 2/cos(phi)*z + 5/cos(phi)**2 - 4 == 0; eq
  z^2 - 2*z/cos(phi) + 5/cos(phi)^2 - 4 == 0

Sage example in ./calculus.tex, line 852::

  sage: eq.lhs()
  z^2 - 2*z/cos(phi) + 5/cos(phi)^2 - 4
  sage: eq.rhs()
  0

Sage example in ./calculus.tex, line 861::

  sage: solve(eq, z)
  [z == -(2*sqrt(cos(phi)^2 - 1) - 1)/cos(phi),
   z ==  (2*sqrt(cos(phi)^2 - 1) + 1)/cos(phi)]

Sage example in ./calculus.tex, line 871::

  sage: y = var('y'); solve(y^7==y, y)
  [y == 1/2*I*sqrt(3) + 1/2, y == 1/2*I*sqrt(3) - 1/2, y == -1,
   y == -1/2*I*sqrt(3) - 1/2, y == -1/2*I*sqrt(3) + 1/2, y == 1, y == 0]

Sage example in ./calculus.tex, line 880::

  sage: solve(x^2-1, x, solution_dict=True)
  [{x: -1}, {x: 1}]

Sage example in ./calculus.tex, line 894::

  sage: solve([x+y == 3, 2*x+2*y == 6], x, y)
  [[x == -r1 + 3, y == r1]]

Sage example in ./calculus.tex, line 910::

  sage: solve([cos(x)*sin(x) == 1/2, x+y == 0], x, y)
  [[x == 1/4*pi + pi*z..., y == -1/4*pi - pi*z...]]

Sage example in ./calculus.tex, line 920::

  sage: solve(x^2+x-1 > 0, x)
  [[x < -1/2*sqrt(5) - 1/2], [x > 1/2*sqrt(5) - 1/2]]

Sage example in ./calculus.tex, line 943::

  sage: x, y, z = var('x, y, z')
  sage: solve([x^2 * y * z == 18, x * y^3 * z == 24,\
  ....:        x * y * z^4 == 6], x, y, z)
  [[x == 3, y == 2, z == 1],
   [x == (1.337215067329613 - 2.685489874065195*I),
    y == (-1.700434271459228 + 1.052864325754712*I),
    z == (0.9324722294043555 - 0.3612416661871523*I)], ...]

Sage example in ./calculus.tex, line 975::

  sage: expr = sin(x) + sin(2 * x) + sin(3 * x)
  sage: solve(expr, x)
  [sin(3*x) == -sin(2*x) - sin(x)]

Sage example in ./calculus.tex, line 983::

  sage: find_root(expr, 0.1, pi)
  2.0943951023931957

Sage example in ./calculus.tex, line 989::

  sage: f = expr.simplify_trig(); f
  2*(2*cos(x)^2 + cos(x))*sin(x)
  sage: solve(f, x)
  [x == 0, x == 2/3*pi, x == 1/2*pi]

Sage example in ./calculus.tex, line 1022::

  sage: (x^3+2*x+1).roots(x)
  [(-1/2*(1/18*sqrt(59)*sqrt(3) - 1/2)^(1/3)*(I*sqrt(3) + 1)
     - 1/3*(I*sqrt(3) - 1)/(1/18*sqrt(59)*sqrt(3) - 1/2)^(1/3), 1),
    (-1/2*(1/18*sqrt(59)*sqrt(3) - 1/2)^(1/3)*(-I*sqrt(3) + 1)
     - 1/3*(-I*sqrt(3) - 1)/(1/18*sqrt(59)*sqrt(3) - 1/2)^(1/3), 1),
    ((1/18*sqrt(59)*sqrt(3) - 1/2)^(1/3)
     - 2/3/(1/18*sqrt(59)*sqrt(3) - 1/2)^(1/3), 1)]

Sage example in ./calculus.tex, line 1058::

  sage: (x^3+2*x+1).roots(x, ring=RR)
  [(-0.453397651516404, 1)]

Sage example in ./calculus.tex, line 1062::

  sage: (x^3+2*x+1).roots(x, ring=CC)
  [(-0.453397651516404, 1),
   (0.226698825758202 - 1.46771150871022*I, 1),
   (0.226698825758202 + 1.46771150871022*I, 1)]

Sage example in ./calculus.tex, line 1086::

  sage: solve(x^(1/x)==(1/x)^x, x)
  [(1/x)^x == x^(1/x)]

Sage example in ./calculus.tex, line 1124::

  sage: y = function('y')(x)
  sage: desolve(diff(y,x,x) + x*diff(y,x) + y == 0, y, [0,0,1])
  -1/2*I*sqrt(2)*sqrt(pi)*erf(1/2*I*sqrt(2)*x)*e^(-1/2*x^2)

Sage example in ./calculus.tex, line 1171::

  sage: k, n = var('k, n')
  sage: sum(k, k, 1, n).factor()
  1/2*(n + 1)*n

Sage example in ./calculus.tex, line 1179::

  sage: n, k, y = var('n, k, y')
  sage: sum(binomial(n,k) * x^k * y^(n-k), k, 0, n)
  (x + y)^n

Sage example in ./calculus.tex, line 1189::

  sage: k, n = var('k, n')
  sage: sum(binomial(n,k), k, 0, n),\
  ....: sum(k * binomial(n, k), k, 0, n),\
  ....: sum((-1)^k*binomial(n,k), k, 0, n)
  (2^n, 2^(n - 1)*n, 0)

Sage example in ./calculus.tex, line 1199::

  sage: a, q, k, n = var('a, q, k, n')
  sage: sum(a*q^k, k, 0, n)
  (a*q^(n + 1) - a)/(q - 1)

Sage example in ./calculus.tex, line 1212::

  sage: assume(abs(q) < 1)
  sage: sum(a*q^k, k, 0, infinity)
  -a/(q - 1)

Sage example in ./calculus.tex, line 1218::

  sage: forget(); assume(q > 1); sum(a*q^k, k, 0, infinity)
  Traceback (most recent call last):
  ...
  ValueError: Sum is divergent.

Sage example in ./calculus.tex, line 1300::

  sage: limit((x**(1/3) - 2) / ((x + 19)**(1/3) - 3), x = 8)
  9/4
  sage: f(x) = (cos(pi/4-x)-tan(x))/(1-sin(pi/4 + x))
  sage: limit(f(x), x = pi/4)
  Infinity

Sage example in ./calculus.tex, line 1317::

  sage: limit(f(x), x = pi/4, dir='minus')
  +Infinity
  sage: limit(f(x), x = pi/4, dir='plus')
  -Infinity

Sage example in ./calculus.tex, line 1368::

  sage: u(n) = n^100 / 100^n
  sage: u(1.);u(2.);u(3.);u(4.);u(5.);u(6.);u(7.);u(8.);u(9.);u(10.)
  0.0100000000000000
  1.26765060022823e26
  5.15377520732011e41
  1.60693804425899e52
  7.88860905221012e59
  6.53318623500071e65
  3.23447650962476e70
  2.03703597633449e74
  2.65613988875875e77
  1.00000000000000e80

Sage example in ./calculus.tex, line 1389::

  sage: plot(u(x), x, 1, 40)
  Graphics object consisting of 1 graphics primitive

Sage example in ./calculus.tex, line 1407::

  sage: v(x) = diff(u(x), x); sol = solve(v(x) == 0, x); sol
  [x == 50/log(10), x == 0]
  sage: floor(sol[0].rhs())
  21

Sage example in ./calculus.tex, line 1420::

  sage: limit(u(n), n=infinity)
  0
  sage: n0 = find_root(u(n) - 1e-8 == 0, 22, 1000); n0
  105.07496210187252

Sage example in ./calculus.tex, line 1502::

  sage: ((1+arctan(x))^(1/x)).series(x==0, 3)
  (e) + (-1/2*e)*x + (1/8*e)*x^2 + Order(x^3)

Sage example in ./calculus.tex, line 1507::

  sage: (ln(2*sin(x))).series(x==pi/6, 3)
  (sqrt(3))*(-1/6*pi + x) + (-2)*(-1/6*pi + x)^2
  + Order(-1/216*(pi - 6*x)^3)

Sage example in ./calculus.tex, line 1520::

  sage: (ln(2*sin(x))).series(x==pi/6, 3).truncate()
  -1/18*(pi - 6*x)^2 - 1/6*sqrt(3)*(pi - 6*x)

Sage example in ./calculus.tex, line 1537::

  sage: taylor((x**3+x)**(1/3) - (x**3-x)**(1/3), x, infinity, 2)
  2/3/x

Sage example in ./calculus.tex, line 1577::

  sage: tan(4*arctan(1/5)).simplify_trig()
  120/119
  sage: tan(pi/4+arctan(1/239)).simplify_trig()
  120/119

Sage example in ./calculus.tex, line 1591::

  sage: f = arctan(x).series(x, 10); f
  1*x + (-1/3)*x^3 + 1/5*x^5 + (-1/7)*x^7 + 1/9*x^9 + Order(x^10)
  sage: (16*f.subs(x==1/5) - 4*f.subs(x==1/239)).n(); pi.n()
  3.14159268240440
  3.14159265358979

Sage example in ./calculus.tex, line 1662::

  sage: k = var('k')
  sage: sum(1/k^2, k, 1, infinity),\
  ....: sum(1/k^4, k, 1, infinity),\
  ....: sum(1/k^5, k, 1, infinity)
  (1/6*pi^2, 1/90*pi^4, zeta(5))

Sage example in ./calculus.tex, line 1689::

  sage: s = 2*sqrt(2)/9801*(sum((factorial(4*k)) * (1103+26390*k) /
  ....:     ((factorial(k)) ^ 4 * 396 ^ (4 * k)) for k in (0..11)))
  sage: (1/s).n(digits=100)
  3.141592653589793238462643383279502884197169399375105820974...
  sage: (pi-1/s).n(digits=100).n()
  -4.36415445739398e-96

Sage example in ./calculus.tex, line 1722::

  sage: n = var('n'); u = sin(pi*(sqrt(4*n^2+1)-2*n))
  sage: taylor(u, n, infinity, 3)
  1/4*pi/n - 1/384*(6*pi + pi^3)/n^3

Sage example in ./calculus.tex, line 1762::

  sage: diff(sin(x^2), x)
  2*x*cos(x^2)
  sage: function('f')(x); function('g')(x); diff(f(g(x)), x)
  f(x)
  g(x)
  D[0](f)(g(x))*diff(g(x), x)
  sage: diff(ln(f(x)), x)
  diff(f(x), x)/f(x)

Sage example in ./calculus.tex, line 1780::

  sage: f(x,y) = x*y + sin(x^2) + e^(-x); derivative(f, x)
  (x, y) |--> 2*x*cos(x^2) + y - e^(-x)
  sage: derivative(f, y)
  (x, y) |--> x

Sage example in ./calculus.tex, line 1803::

  sage: x, y = var('x, y'); f = ln(x**2+y**2) / 2
  sage: delta = diff(f,x,2) + diff(f,y,2)
  sage: delta.simplify_rational()
  0

Sage example in ./calculus.tex, line 1854::

  sage: sin(x).integral(x, 0, pi/2)
  1
  sage: integrate(1/(1+x^2), x)
  arctan(x)
  sage: integrate(1/(1+x^2), x, -infinity, infinity)
  pi
  sage: integrate(exp(-x**2), x, 0, infinity)
  1/2*sqrt(pi)

Sage example in ./calculus.tex, line 1864::

  sage: integrate(exp(-x), x, -infinity, infinity)
  Traceback (most recent call last):
  ...
  ValueError: Integral is divergent.

Sage example in ./calculus.tex, line 1878::

  sage: u = var('u'); f = x * cos(u) / (u^2 + x^2)
  sage: assume(x>0); f.integrate(u, 0, infinity)
  1/2*pi*e^(-x)
  sage: forget(); assume(x<0); f.integrate(u, 0, infinity)
  -1/2*pi*e^x

Sage example in ./calculus.tex, line 1904::

  sage: integral_numerical(sin(x)/x, 0, 1)   # abs tol 1e-12
  (0.946083070367183, 1.0503632079297087e-14)
  sage: g = integrate(exp(-x**2), x, 0, infinity)
  sage: g, g.n()                             # abs tol 1e-12
  (1/2*sqrt(pi), 0.886226925452758)
  sage: approx = integral_numerical(exp(-x**2), 0, infinity)
  sage: approx                               # abs tol 1e-12
  (0.8862269254527568, 1.714774436012769e-08)
  sage: approx[0]-g.n()                      # abs tol 1e-12
  -1.11022302462516e-15

Sage example in ./calculus.tex, line 2228::

  sage: A = matrix(QQ, [[1,2],[3,4]]); A
  [1 2]
  [3 4]

Sage example in ./calculus.tex, line 2468::

  sage: A = matrix(QQ, [[2,4,3],[-4,-6,-3],[3,3,1]])
  sage: A.characteristic_polynomial()
  x^3 + 3*x^2 - 4
  sage: A.eigenvalues()
  [1, -2, -2]
  sage: A.minimal_polynomial().factor()
  (x - 1) * (x + 2)^2

Sage example in ./calculus.tex, line 2487::

  sage: A.eigenvectors_right()
  [(1, [
  (1, -1, 1)
  ], 1), (-2, [
  (1, -1, 0)
  ], 2)]

Sage example in ./calculus.tex, line 2499::

  sage: A.jordan_form(transformation=True)
  (
  [ 1| 0  0]
  [--+-----]  [ 1  1  1]
  [ 0|-2  1]  [-1 -1  0]
  [ 0| 0 -2], [ 1  0 -1]
  )

Sage example in ./calculus.tex, line 2533::

  sage: A = matrix(QQ, [[1,-1/2],[-1/2,-1]])
  sage: A.jordan_form()
  Traceback (most recent call last):
  ...
  RuntimeError: Some eigenvalue does not exist in Rational Field.

Sage example in ./calculus.tex, line 2543::

  sage: A = matrix(QQ, [[1,-1/2],[-1/2,-1]])
  sage: A.minimal_polynomial()
  x^2 - 5/4

Sage example in ./calculus.tex, line 2557::

  sage: R = QQ[sqrt(5)]
  sage: A = A.change_ring(R)
  sage: A.jordan_form(transformation=True, subdivide=False)
  (
  [ 1/2*sqrt5          0]  [         1          1]
  [         0 -1/2*sqrt5], [-sqrt5 + 2  sqrt5 + 2]
  )

Sage example in ./calculus.tex, line 2597::

  sage: K.<sqrt2> = NumberField(x^2 - 2)
  sage: L.<sqrt3> = K.extension(x^2 - 3)
  sage: A = matrix(L, [[2, sqrt2*sqrt3, sqrt2],  \
  ....:                [sqrt2*sqrt3, 3, sqrt3],  \
  ....:                [sqrt2, sqrt3, 1]])
  sage: A.jordan_form(transformation=True)
  (
  [6|0|0]
  [-+-+-]
  [0|0|0]  [              1               1               0]
  [-+-+-]  [1/2*sqrt2*sqrt3               0               1]
  [0|0|0], [      1/2*sqrt2          -sqrt2          -sqrt3]
  )

"""

