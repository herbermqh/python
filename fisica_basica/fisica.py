import sympy as sp
from sympy import *
from sympy import init_printing
# from sympy import init_session
init_printing(use_unicode=True)

x = symbols('x')
a = symbols('a')
U = symbols('U')
F = symbols('F')
s = symbols('s')
s1 = symbols('s1')
s2 = symbols('s2')


F = Function('F')(s)







# def trabaj(F=3,s1=1,s2=3,U=3):










def ecuacion_algebraica(primer_miembro,segundo_miembro,variable):
    equation = Eq(primer_miembro,segundo_miembro)
    print(pretty(equation))
    print(pretty(solveset(equation,variable))) 


# ecuacion_algebraica(x**2+2*x,a,x)




# class Trabajo:
#     def __init__(self,U=0,s1=0,s2=0,F=0):
#         self.U = U
#         self.s1 = s1
#         self.s2 = s2
#         self.F = F
#     def variable():    
#         pass
#     def constante():
#         pass
#     def peso():
#         pass
#     def resorte():
#         pass


























