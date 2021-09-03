from functools import reduce


# Ejercicio 1
# ----- Funcion separar --------- #

def separar(lista_numeros: list) -> tuple:
    """ La función recibe como parametro una lista 
    de numeros y devuelve una tupla con dos listas 
    la primera de numeros pares y como segundo elemento 
    una lista con los numeros impares."""

    pares = list(filter(lambda num: num % 2 == 0 and num != 0, lista_numeros))
    impares = list(filter(lambda num: num % 2 != 0 or num == 0, lista_numeros))

    return (pares, impares)


# Lista de numeros
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Desempaquetamos la tupla que devuelve la fn
pares, impares = separar(numeros)

# Imprimimos por consola ambas listas
# print(pares)
# print(impares)


# Ejercicio 2
# ----- Funcion separar --------- #
def convertir(una_frase: str) -> list:
    """ La función recibe como parametro una cadena de caracteres 
    la separa por espacios en blanco y las devuelve como una lista
    de str en mayusculas."""

    palabras = una_frase.split()

    return list(map(lambda palabra: palabra.upper(), palabras))


mi_frase = "Este sabado tenemos el ultimo encuentro online"

# print(convertir(mi_frase))


# Ejercicio 3
# ----- Funcion ordenar --------- #
# Para usar reduce se debe importar del paquete functools
# from functools import reduce

def acumulado(numeros: list) -> int:
    """ La fn recibe como parametro una lista de numeros
    y devuelve el valor aculativo"""
    return reduce(lambda x, y: x + y, numeros, 100)


mis_numeros = [2, 4, 6]

# print(acumulado(mis_numeros))


# Ejercicio 4
# ----- Funcion mostrar --------- #

def mostrar(una_lista, un_numero) -> None:
    """ La fn recibe una lista de string y numero 
    e imprime una secuencia a partir de este asociado al elemento
    de la lista"""
    for indice, fruta in enumerate(una_lista, un_numero):
        print(indice, " ", fruta)


frutas = ['Banana', 'kiwi', 'Pera', 'Naranja', 'Manzana']
mostrar(frutas, 100)
