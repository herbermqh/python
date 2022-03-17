import sympy as sp 
from sympy import symbols, sin, cos, diff

A, w, t, k, x, c = symbols('A w t k x c', real=True)

y = A*cos(w*t - k*x + c)

velocity = diff(y, t)
acceleration = diff(velocity, t)

print(sp.latex(acceleration))


