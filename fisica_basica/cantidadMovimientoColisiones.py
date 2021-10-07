import sympy as sp
from sympy import init_printing
from sympy import init_session
from sympy import *


class Principio_impulso_cantidad_movimiento:
    def __init__(self,v,t,F):
        self.__v=v
        self.__t=t
        self.__F=F

    def v(self):
        self.__tiempo=tiempo

    def prop1(self):
        print(self.__v[0][0])
        print(self.__t)
        print(self.__F)



    #def v(self):
    #def t(self):
    #def m(self):


#p1 = Principio_impulso_cantidad_movimiento(v(0):0, ) 
#p1.prop1()

init_printing()
v = Function("v")
F = Function("F")
t = symbols("t")
m = symbols("m")

ed = Eq(F(t), m*v(t).diff())

print(dsolve(ed,v(t),ics={v(0):0}))





#p1 = Principio_impulso_cantidad_movimiento(t[1] = 1, v[1] = 10, t[2] = 50, F=[10,F(t)], F(t)=)




    














   #para leer
    #def get_m(self):
    #    self.__m = m 

    #para modificar
    #def set_m(self):
    #    self.__m = m