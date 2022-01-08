import sympy as sp
from sympy import *
from sympy import sympify
from sympy import init_printing
from pytexit import py2tex
# from sympy import init_session
init_printing(use_unicode=True)

# a = symbols('a')
# b = symbols('b')
# U = symbols('U')
# F = symbols('F')
s = symbols('s')
  
def ecuacion_algebraica(primer_miembro,segundo_miembro,variable):
    equation = Eq(primer_miembro,segundo_miembro)
    print(pretty(equation))
    print(pretty(solveset(equation,variable))) 

def solve_h(primer_miembro,segundo_miembro,incognita):
    equation = Eq(primer_miembro,segundo_miembro)
    resp = solveset(equation,incognita)
    return resp

# def work(s1=1,s2=3,F=s**2+s,hallar=U):
def work(**datos):
    #token
    lista_datos = sorted(list(datos))
    #
    s2 = lista_datos[-1]
    s1 = lista_datos[-2]
    #subindices
    indice_s2 = sorted(list(s2))[0]
    indice_s1 = sorted(list(s1))[0]
    #symbols
    symb_s2 = symbols(s2)
    symb_s1 = symbols(s1)
    symb_F = symbols('F')
    symb_U = symbols(f'U_{indice_s1}\\to{indice_s2}')
    #valores
    valor_s2 = datos[s2] if s2 in datos else symb_s2 
    valor_s1 = datos[s1] if s1 in datos else symb_s1 
    valor_F = datos['F'] if 'F' in datos else symb_F 
    valor_U = datos['U'] if 'U' in datos else symb_U
    #determinar incognita
    if datos['hallar'] =='U':
        incognita = valor_U
    #tipo de problema
    if type(valor_F) == int or type(valor_F) == float:
        formula = f'{latex(symb_U)} &= {latex(symb_F)} \\left( {latex(symb_s2)} - {latex(symb_s1)} \\right)'
        reemplazo_datos = f'{latex(valor_U)} &= {latex(valor_F)} \\left( {latex(valor_s2)} - {latex(valor_s1)} \\right)'
        resultado = f'{latex(incognita)} &= {latex(solve_h(valor_U,valor_F*(valor_s2-valor_s1),incognita))}'  
    else:
        formula = f'{latex(symb_U)} &= {latex(Integral(symb_F,(s,symb_s1,symb_s2)))}'
        reemplazo_datos = f'{latex(valor_U)} &= {latex(Integral(valor_F,(s,valor_s1,valor_s2)))}'
        resultado = f'{latex(incognita)} &= {latex(solve_h(valor_U,integrate(valor_F,(s,valor_s1,valor_s2)),incognita))}'
    # proceso
    # imprimir procedimiento
    print(formula)
    print(reemplazo_datos)
    print(resultado)


# work(s4=1,s5=3,F=20,hallar=U,U=2)
work(s4=1,s5=2,F=10,hallar='U')
 

 















