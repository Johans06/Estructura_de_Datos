#Existe tres tipos numericos en python: int, float, complex
x = 1    # int: es un número entero, positivo o negativo, sin decimales, de longitud ilimitada
y = 2.8  # float: es un número, positivo o negativo, que contiene uno o más decimales
Y = -87.7e100 #Float también puede ser números científicos con una "e" para indicar la potencia de 10.
z = 1j   # complex: es un número complejo se escribe con una "j" como parte imaginaria:

#Para verificar el tipo de cualquier objeto en Python, use la funcion type():
print(type(x))
print(type(y))
print(type(z))


#Puede convertir de un tipo a otro con el int(), float(), y complex() métodos:
a = 18    # int
b = 6.6  # floa
c = 6j   # complex

#convertir de int a float:
d = float(a)

#convertir de float a int:
e = int(b)

#convertir de int a complex:
f = complex(a)

print("De int a float: ",d)
print("De float a int: ",e)
print("De int a complex: ",f)

print(type(a))
print(type(b))
print(type(c))


#Se puede importar el módulo aleatorio y muestrar un número aleatorio entre 1 y 9 en este caso:
import random

print("Numero aleario: ", random.randrange(1, 10))