# Definicion de nuestro decorador
def decorador_custom(func) -> function:
    """ Decorador devuelve una nueva función. """
    def nuevaFuncion():
        print("Vamos a ejecutar la función.")
        func()
        print("Se ejecuto la función.")

    return nuevaFuncion


@decorador_custom  # <= aplicamos el decorador
def saluda():
    """ Imprime un hola mundo. """
    print("Hola mundo")


@decorador_custom  # <= aplicamos el decorador
def suma():
    """ Suma dos numeros e imprime el reesultado. """
    n1 = 10
    n2 = 20
    suma = n1 + n2
    print(f'La suma de {n1} + {n2} es: {suma}')


if __name__ == '__main__':
    saluda()
    # suma()
