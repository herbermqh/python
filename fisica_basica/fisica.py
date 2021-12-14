import sympy as sp
from sympy import init_printing
from sympy import init_session
from sympy import *

init_printing(pretty_print=true, latex_printer=true) 


t = symbols('t')
s = symbols('s')
v = symbols('v')
x = symbols('x')

def mru(s,v,t):
    if s:
        print("verdadero")
    else:
        print("falso")
        

mru(s=2,v=3,t=4)

