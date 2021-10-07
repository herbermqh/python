#----------------------------
import sympy as sp
from sympy.abc import x
from sympy import Poly
from sympy import init_session
from sympy import *
import numpy as np

#----------------------------



#---------------------CLASSES
class inecuacion:
    #atributos
    x, y, z, a, b, c, m, n, p, q = symbols('x y z a b c m n p q')
    #constructor
    def __init__(self,primerMiembro,simbolo,segundoMiembro):
        self._primerMiembro=primerMiembro
        self._simbolo=simbolo
        self._segundoMiembro=segundoMiembro
    #metodos
    def cs(self):
        #pm = Poly(self._primerMiembro)
        #sr = self._simbolo
        #sm = Poly(self._segundoMiembro)
        conjuntoSolucion(self._primerMiembro,self._simbolo,self._segundoMiembro)

#---------------------------


 
        
#--------------------FUNCIONES
def conjuntoSolucion(pm,sr,sm):
    print(latex(pm))
    
#-----------------------------



    
#--------------------PRUEBAS

x = inecuacion(sqrt(5), '<', 2*x + 3)
x.cs()
#---------------------------





#---------------------------