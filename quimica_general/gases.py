import sympy as sp
from sympy import init_printing
from sympy import init_session
from sympy import *


#-----------------------------ejemplo de una clase
class Persona:
    def __init__(self,nombre, edad): #el clase tiene parametro nombre y edad, y ademas inicializa
        self.nombre=nombre
        self.edad=edad

        #metodos
    def caminar(self):
        a=print("Hola, yo soy", self.nombre, "y estoy caminando")
        return a

    def dale_datos(self):
        a=print("hola, mi nombre es", self.nombre, "y mi edad es", self.edad)
        return a


#El clase ya es objeto
Persona.nombre="Juan"
Persona.edad=23
print(Persona.nombre)
print(Persona.edad)

#Creacion de objetos
persona1=Persona("Martin",50)
print(persona1.nombre)
print(persona1.edad)
#utlizacion de metodos
persona1.caminar()
persona1.dale_datos()







#-----------------------------Declarando variables
class Gas:
    def __init__(self,name,molecular_form):
        self.name=name
        self.molecular_form=molecular_form



#----------------------------ecuacion de estado




#----------------------------Operociones
#ecuacion de Van der Waals
# class vanDerWaals:
#     presion=0
#     volumen=0
#     temperatura=0
#     numeroMoles=0
#     R=a
#     a=b
#     b=c
    
#     def __init__(self,velocidad,distancia,tiempo):
#         self.velocidad=velocidad
#         self.distancia=distancia
#         self.tiempo=tiempo
    
#     def cVelocidad(self):
#         pass
    
#     def cDistancia(self):
#         velocidad*tiempo
#     def cTiempo(self):








