import numpy as np
import sympy as sp
from sympy import *
import matplotlib as plt
from matplotlib import *


def f(x):
    return(35*x)


def paresEnteros(domInicial, domFinal):
    domFinal=domFinal+1
    dominio=np.arange(domInicial,domFinal, dtype=float)
    i=0
    while i < dominio.size:
        y=f(dominio[i])
        if y.is_integer():
            print('El punto P(',dominio[i],';',y,') cumple con la condición')
        i=i+1



paresEnteros(0,20)




