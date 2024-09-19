#Cree una variable fuera de una función y úsela dentro de la función
x = "Johan Stevens"
def myfunc():
  print("Mi nombre es " + x)

myfunc()

#se puede crear una variable dentro de una función, con el mismo nombre que la variable global
a = "Johan Stevens"

def myfunc():
  a = "Azul"
  print("Mi color favorito es " + a)

myfunc()
print("Mi nombre es " + a)

#Si se usa la palabra clave (global), la variable pertenece al alcance global:
def myfunc():
  global y
  y = "Thor Odinson"

myfunc()
print("Mi personaje favorito es " + y)

# Para cambiar el valor de una variable global dentro de una función, use la palabra clave (global)
d = "Sanchez"

def myfunc():
  global d
  d = "Aponte"

myfunc()
print("Mi apellido es " + d)