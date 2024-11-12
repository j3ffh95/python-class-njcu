from sympy import *

init_printing()

x = sympify("x")
f = x**2*sin(x)

plot(f)