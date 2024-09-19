#Python tiene los siguientes tipos de datos integrados de forma predeterminada, 
# en estas categorías:
#Tipo de Texto:	str
#Tipos Numéricos:	int, float, complex
#Tipos de Secuencia:	list, tuple, range
#Tipo de Mapeo:	dict
#Establecer Tipos:	set, frozenset
#Tipo Booleano:	bool
#Tipos Binarios:	bytes, bytearray, memoryview
#Ninguno Tipo:	NoneType

#En Python, el tipo de dato se establece cuando se asigna el valor a la variable
a = "Hola mundo"	#str	
b = 20	#int	
c = 20.5	#float	
d = 1j	#complex	
e = ["manzana", "casa", "perro"]	#list	
f = ("computador", "banana", "fresa")	#tuple	
g = range(6)	#range	
h = {"nombre" : "Johan", "edad" : 36}	#dict	
i = {"leche", "queso", "yogur"}	#set	
j = frozenset({"apple", "banana", "fresas"})	#frozenset	
k = True	#bool	
l = b"Hello"	#bytes	
m = bytearray(5)	#bytearray	
n = memoryview(bytes(5))	#memoryview	
o = None  #Ningun tipo

#Se puede obtener el tipo de datos de cualquier objeto utilizando el type() función:
x = "Johan"
print(type(x))