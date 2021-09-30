"""   => Ejercicio 1:
    Realiza una función separar(lista) que tome una lista de números enteros 
    y devuelva dos listas la primera con los números pares 
    y la segunda con los números impares.

    Ej:
        pares, impares = separar([6,5,2,1,7])
        print(pares)
        print(impares)

        >>> [2, 6]
        >>> [1, 5, 7] """
        
# definicion de variables 
num_enteros = [6,5,2,1,7]


# definicion de la funcion "separar"
def separar(una_lista) :
    pares = list(filter(lambda x: x % 2 == 0, una_lista))
    impares = list(filter(lambda x: x % 2 != 0, una_lista))
    return (pares, impares)
    
    
# utilizacion de la funcion
pares, impares = separar(num_enteros)
print(pares)
print(impares)
