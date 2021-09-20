import time


def calcular_tiempo(name):
    """ Decodador para calcular el tiempo de ejecución.
    Recibe como parametro el nombre de la fn y retorna la fn wrapper"""

    def wrapper(function):
        """ Recibe la function como param y retorna la fn anidada."""

        def wrapper2(*args, **kwargs):
            """ Recibe los argumentos y retorna el resultado de la 
            fn a decorar."""
            start = time.time()
            result = function(*args, **kwargs)
            print(f'Tiempo total de {name}: ', time.time() - start)

            return result  # Retorna el resultado de la fn decorada

        return wrapper2  # Retorna la funcion anidada

    return wrapper  # Retorna la fn decoradora


if __name__ == '__main__':
    @calcular_tiempo('Suma')
    def suma(numero_1, numero_2):
        time.sleep(3)
        return numero_1 + numero_2

    print(suma(3, 9))
