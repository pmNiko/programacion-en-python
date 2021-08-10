""" 
    Tuplas en Python
  """

tupla_1 = 1, 2, 3, 4, 5, 2, 10, 2
tupla_2 = 'hola', 34, True, 2.5
tupla_3 = 1, 2, [9, 6, 3], 'Hola', 'personaje'
tupla_4 = tuple([2, True, 'palabra'])


# Acceso a los elementos de una tupla
# print(tupla_2[0])
# print(tupla_2[-1])

# print(tupla_3)
# tupla_3[2].append('c')
# print(tupla_3)
# print(type(tupla_3))

# Pedirle su longitud
# print(len(tupla_3))

# Ver la cantidad de ocurrencias de un elemento
# print(tupla_1.count(2))

# Corroborar la exitencia de un elemento
# print(340 in tupla_2)

# tuple unpacking desempaquetando una tupla
# tupla_5 = 4, "una palabra", False
# elem_1, elem_2, elem_3 = tupla_5
# print(elem_2)


# Estructura ciclica o iterativa
# Recorrer los elementos e imprimirlos
print(tupla_1)
# for elemento in tupla_1:
#     print(elemento)


# Estrutura selectiva
# Imprimir un mensaje en base a una condición
# if 2.5 in tupla_2:
#     print('El elemento 2.5 esta contenido en la tupla 2.')


# Tambien podemos ejecutar un bloque de codigo si la
# condicion da False
if 101 in tupla_2:
    print('El elemento 101 existe dentro de la tupla 2')
else:
    print('La condición no se cumplio.')
