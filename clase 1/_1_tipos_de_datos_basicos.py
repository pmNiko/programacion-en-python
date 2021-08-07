""" 
  Tipo string
  """

mi_variable = "Este es el contenido de mi variable"

mi_variable_2 = 'Estas son comillas simples'

mi_variable_3 = ''' 
  Este es un comentario multilinea.
'''

mi_variable_4 = """
  Este es otro comentario
"""

# print(mi_variable)
# print(mi_variable_2)
# print(mi_variable_3)
# print(mi_variable_4)

# ### imprimir el tipo de dato #####
# utilizamos la funcion type() dentro de un print()
# print(type(mi_variable))


""" 
  Tipo Integer int
  """

numero_1 = 1
numero_2 = 2
# print(numero_1)
# print(numero_2)

# print(10 / 5)

# ### operaciones con numeros
# #####  // devuelve el modulo
# print(10 // 3)

# #####  % devuelve el residuo
# print(10 % 3)

suma_de_dos_numeros = numero_1 + numero_2
# print(suma_de_dos_numeros)

# ### imprimir el tipo de dato #####
# utilizamos la funcion type() dentro de un print()
# print(type(numero_1))

""" 
  Tipo float
  """

numero_decimal_1 = 2.0
numero_decimal_2 = 4.5
numero_decimal_3 = 0.5

# print(numero_decimal_1)
# print(numero_decimal_2)
# print(numero_decimal_3)

# ### imprimir el tipo de dato #####
# utilizamos la funcion type() dentro de un print()
# print(type(numero_decimal_1))

""" 
  Tipo bool  boolean
  """

verdadero = True
falso = False

# print(verdadero)
# print(falso)

# ### imprimir el tipo de dato #####
# utilizamos la funcion type() dentro de un print()
# print(type(verdadero))

""" 
  Input 
"""

# Como capturamos los datos ingresados por el usuario
# utilizamos la función input()
# A tener en cuenta el tipo de dato que captura input() será string

# ejemplo:
nombre = input("Ingrese su nombre: ")
print(nombre)
print(type(nombre))

# mi_lista = [nombre]
# print(mi_lista)
# print(nombre.split())
# print(type(mi_lista))

# ejemplo 2:
# edad = input("Ingrese su edad: ")
# print(edad)
# print(type(edad))

# ejemplo 2:
# numero = input("Ingrese su numero: ")
# print(numero)
# print(type(numero))

# obtendriamos un error
# suma = numero + 2
# print(suma)

# Se debe castear-convertir el tipo de dato
# numero_convertido = int(numero)
# suma = numero_convertido + 2
# print(type(numero_convertido))
# print(suma)

# Existen similares para float y string
# float()  str()
