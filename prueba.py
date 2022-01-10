import sympy as sp
from sympy import *
from sympy import init_printing
init_printing(use_unicode=True)


 
a,b,c=symbols('a b c') 
x,y,z = symbols('x y z')
  
equation = Eq(x**2 + 2*x,a)

print(pretty(equation))
print(pretty(solveset(equation,x))) 




print(pretty(128-12-84.96))




# print(latex(equation))


























