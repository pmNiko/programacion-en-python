# Importacion de modulos
from functools import reduce
from operator import add

""" Cómo se define una función anónima en Python
La sintaxis para definir una función lambda es la siguiente: 

    lambda parámetros: expresión
"""

""" A continuación se detallan las características principales de una función anónima:

    - Son funciones que pueden definir cualquier número de parámetros pero una única expresión. 
      Esta expresión es evaluada y devuelta.
    - Se pueden usar en cualquier lugar en el que una función sea requerida.
    - Estas funciones están restringidas al uso de una sola expresión.
    - Se suelen usar en combinación con otras funciones, generalmente como argumentos de otra función. 
    Como por ejemplo funciones como map, filter y reduce
    """


""" Las funciones de orden superior son aquellas que permiten recibir otras fn como parametro """

"""  map()  
    La función map() en Python aplica una función a cada uno de los elementos de una lista.

                                                                                          """
enteros = [1, 2, 4, 7]


def cuadradoDeUnNumero(numero):
    return numero ** 2

# resultado = map(cuadradoDeUnNumero, enteros)
# print(list(resultado))

# ----- Podriamos resumirlo en una linea ------ #
# print(list(map(cuadradoDeUnNumero, enteros)))


# ----- También podriamos optar por utilizar una fn lambda ------ #
# cuadrados = list(map(lambda x: x ** 2, enteros))
# print(cuadrados)

# ----- Otros casos de uso ------ #

# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]

# result = map(lambda x, y: x + y, numbers1, numbers2)
# print(list(result))


"""  filter()  
    La función filter() filtra una lista de elementos para los que una función devuelve True.

                                                                                          """
# valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# def numeroPares(numero):
#     if numero % 2 == 0:
#         return numero


# numeros_pares = list(filter(numeroPares, valores))
# print(numeros_pares)

# ----- Veamoslo con una fn lambda ------ #
# pares = list(filter(lambda x: x % 2 == 0, valores))
# print(pares)


"""  reduce()  
    Esta función se utiliza principalmente para llevar a 
    cabo un cálculo acumulativo sobre una lista de valores y devolver el resultado.
 
                                                                                """
# -----  Fn para sumar dos numeros----- #


def sumandos(numero1, numero2):
    return numero1 + numero2


# reduce recibe tres parametros una funcion, la coleccion
# y un tercer parametro opcional para inicializar el acumulador
# print(reduce(sumandos, valores, 3))

# ----- Podemos hacerlo con una funcion lambda ----- #
# suma = reduce(lambda x, y: x + y, valores)
# print(suma)

# ----- Podemos hacerlo usando un modulo de operator ----- #
# print(reduce(add, valores, 0))
# print(reduce(add, valores, 2))


"""  enumerate()  
    El método enumerate() agrega un contador a un iterable y lo devuelve 
    en forma de objeto enumerador. 
    Este objeto enumerado se puede usar directamente para bucles o convertirse 
    en una lista de tuplas usando el método list ().   """


# Listas de objetos
mi_lista = ["Notebook", "PC Desktop", "Mouse", "Parlantes", "Pad"]

# Por defecto nos devolverá una secuencia de tuplas
# for ele in enumerate(mi_lista):
#     print(ele)

# La fn enumerate() recibe como parametro un iterable y in int para su contador
# for indice, elemento in enumerate(mi_lista, 1):
#     print(indice, " => ", elemento)


# Mediante la función dict podemos recuperar un diccionario de elementos
# en base a nuestra mi_lista y el metodo enumerate()
# elementos_informaticos_dict = dict(list(enumerate(mi_lista, 1)))

# print(elementos_informaticos_dict)


""" Investigar que hace y para que sirve la función zip """
