import sympy as sp
from sympy import *
import numpy as np

from matplotlib import pyplot as plt

#from sympy import init_session
#init_session()
#from sympy import init_printing
#init_printing()


s = symbols('s')
v = symbols('v')
m = 10
T_1 = 0
T_2 = 0.5*m*v**2
u_k = 0.2
g = 9.81
    
def F(s):
    return 25+9*s**2  

def plot_Fs():
    x = np.linspace(0,2,num=50)
    y = F(x)
    plt.plot(x,y,color='red')


# teo_trabajo_energia = Eq(T_1+integrate(F(s),(s,0,s))-m*g*u_k*s,T_2)

def vs(s):
    eq = solve(Eq(T_1+integrate(F(s),(s,0,s))-m*g*u_k*s,T_2),v)[1] 
    return eq


x = symbols('x')

print(pretty(vs(x)))






















