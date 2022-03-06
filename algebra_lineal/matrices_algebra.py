import sympy as sp
from sympy import *
init_printing(use_unicode=True)
  
  
def producto_matriz(A,B):
    _A = Matrix(A)
    _B = Matrix(B)
    print(f' &= {latex(_A)}{latex(_B)}\\\\')
    print(f' &= {latex(_A*_B)}')


A = [[1,2],[1,3]]
B = [[1,2],[1,3]]

producto_matriz(A,B)


