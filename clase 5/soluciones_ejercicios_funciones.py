"""Ejercicio 1
Genenerar su propia funcion map, que tome como parametro 
una funcion y una coleccion, aplicando dicha fn recibida como
param y se la aplique a cada elemento de la coleccion, retornando 
un objeto generador.
Luego pasar el objeto resultante por una fn list() e imprimirlo.

  Ej: 
    objeto_resultante = myMap(lambda x: x + 3, range(10))

    print(list(objeto_resultante))
    
    >>> [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
"""

# --- definición de la fn myMap


# def myMap(func, iterable):
#     for ele in iterable:
#         yield func(ele)


# objeto_resultante = myMap(lambda x: x + 3, range(10))

# print(list(objeto_resultante))


"""Ejercicio 2
Genenerar su propia funcion filter, que tome como parametro 
una funcion y una coleccion, devolviendo solo aquellos elementos
que cumplan con la condicion de dicha fn pasada como param.
Luego pasar el objeto resultante por una fn list() e imprimirlo.

  Ej: 
    objeto_resultante = myFilter(lambda x: x > 3, [3,1,10,8,6,2])

    print(list(objeto_resultante))
    
    >>> [10, 8, 6]
"""

# --- definición de la fn myFilter


# def myFilter(func, iterable):
#     for ele in iterable:
#         if func(ele):
#             yield ele


# objeto_resultante = myFilter(lambda x: x > 3, [3, 1, 10, 8, 6, 2])

# print(list(objeto_resultante))


"""Ejercicio 3
Genenerar su propia funcion reduce, que tome como parametro 
una funcion y una coleccion, devolviendo el acumulador resultante.
Luego imprimirlo.

  Ej: 
    acumulador = myReduce(lambda x, b: x + b, [3, 1, 10, 8, 6, 2])

    print(acumulador)
    
    >>> 30
"""

# --- definición de la fn myReduce


# def myReduce(func, iterable, acum=0):
#     for ele in iterable:
#         acum = func(acum, ele)
#     return acum


# acumulador = myReduce(lambda x, b: x + b, [3, 1, 10, 8, 6, 2])

# print(acumulador)


"""Ejercicio 4
Genenerar su propia funcion enumerate que agrega un contador a un 
iterable y lo devuelva en forma de objeto enumerador. 
Por ultimo convertirlo en un diccionario e imprimirlo.

  Ej: 
    objeto_enumerado = myEnumerate(
    ["Pasta", "Ensalada", "Bebida", "Carne", "Aperitivo"], 10)

    print(dict(list(objeto_enumerado)))
    
    >>> {10: 'Pasta', 11: 'Ensalada', 12: 'Bebida', 13: 'Carne', 14: 'Aperitivo'}
"""

# --- definición de la fn myEnumerate


def myEnumerate(iterable, contador):
    for ele in iterable:
        yield (contador, ele)
        contador += 1


objeto_enumerado = myEnumerate(
    ["Pasta", "Ensalada", "Bebida", "Carne", "Aperitivo"], 10)

print(dict(list(objeto_enumerado)))
