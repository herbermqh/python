import sympy as sp
from sympy.abc import x
from sympy import Poly
from sympy import init_session
from sympy import *
import numpy as np

#import desigualdadesInecuaciones as di


p, q, r = symbols('p,q,r')

P=(~q|(~q&~p))>>(~p&q)


print(simplify_logic(P))

