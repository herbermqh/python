import sympy as sp
from sympy import *
init_printing(use_unicode=True)

# syntax matrix_elements_declarator_symbols([[1,'b','c'],['d','e','f'],['g','h','i']])
def matrix_elements_declarator_symbols(matrix):
    for i in range(len(matrix)):
        if isinstance(matrix[i], list):
            for j in range(len(matrix[i])):
                matrix[i][j] = symbols(f'{matrix[i][j]}')
        else:
            matrix[i] = symbols(f'{matrix[i]}')

def matrix_print_latex(matrix):
    matrix_elements_declarator_symbols(matrix)
    print(latex(Matrix(matrix)))

def producto_matriz(A,B):
    _A = Matrix(A)
    _B = Matrix(B)
    print(f' &= {latex(_A)}{latex(_B)}\\\\')
    print(f' &= {latex(_A*_B)}')

M = ['c','b','a']
matrix_print_latex(M)


